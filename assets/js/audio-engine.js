/**
 * UNIFIED TOKYO JAPANESE AUDIO ENGINE (DUAL ENGINE)
 * ==========================================================================
 * Engine 1 (Primary): Google Studio High-Fidelity Japanese TTS (Tokyo Native)
 * Engine 2 (Fallback): Web Speech API (Kyoko, O-ren, Otoya, Google 日本語)
 * Compatibility: Cốc Cốc, Chrome, Safari, Edge, Firefox, iOS, Android
 * Referrer Policy: Explicit 'no-referrer' to bypass 403 Forbidden blocks
 * ==========================================================================
 */

(function (window, document) {
    'use strict';

    let currentAudio = null;
    let currentActiveBtn = null;
    let activeTimeoutId = null;
    let activeSpeechTimerId = null;
    let playbackToken = 0;
    let cachedJaVoices = [];

    // 1. Inject pulse animation style for active audio buttons if not already present
    function injectAudioStyles() {
        if (!document || !document.head || document.getElementById('unified-audio-engine-styles')) return;
        const style = document.createElement('style');
        style.id = 'unified-audio-engine-styles';
        style.textContent = `
            .btn-speak.audio-playing,
            .sound-btn.audio-playing,
            .fc-audio-btn.audio-playing,
            .quiz-sound-btn.audio-playing,
            .audio-btn.audio-playing,
            .btn-speak-inline.audio-playing,
            .fc-speaker-btn.audio-playing,
            .btn-sound-small.audio-playing,
            .tp-tts-btn.audio-playing,
            .v3d-speak-btn.audio-playing,
            #tpCardSpeakBtn.audio-playing {
                animation: audioPlayingPulse 0.9s infinite alternate !important;
                background: #059669 !important;
                color: #ffffff !important;
                border-color: #047857 !important;
                transform: scale(1.12) !important;
            }
            @keyframes audioPlayingPulse {
                0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
                100% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
            }
        `;
        document.head.appendChild(style);
    }

    // 2. Pre-cache Japanese voices for Web Speech fallback
    function initVoices() {
        if (!('speechSynthesis' in window)) return;
        try {
            const update = () => {
                const voices = window.speechSynthesis.getVoices() || [];
                cachedJaVoices = voices.filter(v => v.lang && (v.lang === 'ja' || v.lang.startsWith('ja')));
            };
            update();
            if (window.speechSynthesis.onvoiceschanged !== undefined) {
                window.speechSynthesis.onvoiceschanged = update;
            }
        } catch (e) {}
    }

    if (document && document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            injectAudioStyles();
            initVoices();
        });
    } else {
        injectAudioStyles();
        initVoices();
    }

    function clearActiveTimers() {
        if (activeTimeoutId !== null) {
            clearTimeout(activeTimeoutId);
            activeTimeoutId = null;
        }
        if (activeSpeechTimerId !== null) {
            clearTimeout(activeSpeechTimerId);
            activeSpeechTimerId = null;
        }
    }

    function detachAudio(audio) {
        if (!audio) return;
        audio.onplaying = null;
        audio.onended = null;
        audio.onerror = null;
        try {
            audio.pause();
            if (typeof audio.removeAttribute === 'function') {
                audio.removeAttribute('src');
            }
            if (typeof audio.load === 'function') {
                audio.load();
            }
        } catch (e) {}
    }

    function clearActiveButton() {
        if (currentActiveBtn && currentActiveBtn.classList) {
            try {
                currentActiveBtn.classList.remove('audio-playing');
            } catch (e) {}
        }
        currentActiveBtn = null;
    }

    // Stop any currently playing/pending audio or fallback speech cleanly
    function stopCurrentAudio() {
        playbackToken += 1;
        clearActiveTimers();
        if (currentAudio) {
            detachAudio(currentAudio);
            currentAudio = null;
        }
        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel();
            } catch (e) {}
        }
        clearActiveButton();
    }

    // 3. Bulletproof Japanese Text Normalizer (Preserves Japanese phrases in brackets like （ドアを）あけます)
    function cleanJapaneseText(text) {
        if (!text) return '';
        let t = String(text).trim();

        // Remove ruby / furigana HTML elements cleanly
        t = t.replace(/<rt>.*?<\/rt>/gi, '').replace(/<[^>]*>/g, '');

        // Remove angle bracketed non-Japanese notes (e.g. 〈Số đếm〉)
        t = t.replace(/〈[^〉]*〉/g, '');

        // Strip inline alternate variants like （／あたまが...） or (/...) BEFORE slash splitting
        t = t.replace(/[（(]\s*[／/][^）)]*[）)]/g, '');

        // Strip fill-in-the-blank placeholders before slash/bracket filtering
        t = t.replace(/\[[_\s＿…・\-]+\]/g, ' ');
        t = t.replace(/[＿_]{2,}/g, ' ');

        // If slash alternative exists (e.g. しゃけ／さけ, そふ／おじいさん), pick the first one
        if (t.includes('/') || t.includes('／')) {
            t = t.split('/')[0].split('／')[0].trim();
        }

        // Remove dialogue speaker labels (e.g. A: 「...」 -> 「...」) and standalone dialogue dashes
        t = t.replace(/(?:^|\s)[A-Z]\s*[:：]\s*/g, ' ');
        t = t.replace(/([。」！？])\s*ー+\s*/g, '$1 ').replace(/\s+ー+\s+/g, ' ');

        // Replace em-dashes and dialogue separators with natural sentence break
        t = t.replace(/[―—–-]+/g, ' ');

        // Smart bracket handling:
        // If content inside brackets is purely Latin notes/translations (e.g. (Coat), (km), (size), (N)), strip it.
        // If content inside brackets contains Japanese kana/kanji (e.g. （ドアを）あけます, （します）), KEEP the Japanese!
        const hasJapanese = str => /[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]/.test(str);
        const parenFilter = (match, inner) => {
            let trimmed = (inner || '').trim();
            // Remove standalone grammar placeholders inside parentheses like (の ＋ N) -> (の)
            trimmed = trimmed.replace(/\s*[+＋]\s*/g, ' ').replace(/(^|\s)[NPV]($|\s)/g, ' ').trim();
            return hasJapanese(trimmed) ? trimmed : '';
        };

        t = t.replace(/\((.*?)\)/g, parenFilter);
        t = t.replace(/（(.*?)）/g, parenFilter);
        t = t.replace(/\[(.*?)\]/g, parenFilter);
        t = t.replace(/【(.*?)】/g, parenFilter);

        // Keep Tシャツ together
        t = t.replace(/T\s*シャツ/gi, 'Tシャツ');

        // Remove standalone grammar variable placeholders like N, P, V
        t = t.replace(/(^|[\s（(])[NPV](?=[\s)）をがにはでにへと])/g, '$1');
        t = t.replace(/([をがにはでにへと\s])[NPV]($|[\s)）])/g, '$1');
        t = t.replace(/[~～]\s*V\s*/g, '');
        t = t.replace(/\s*[+＋]\s*/g, ' ');
        t = t.replace(/(^|\s)[NPV]($|\s)/g, ' ');

        // Convert ～時 / ~時の to natural reading "なんじの"
        t = t.replace(/[～~]時の/g, 'なんじの');
        t = t.replace(/[～~]時/g, 'なんじ');

        // Strip decorative symbols and standalone question marks (preserve Japanese question intonation "？")
        t = t.replace(/[～〜・→➔*#_＿…]/g, '');
        t = t.replace(/(?:^|\s)[?？]+(?=\s|$)/g, ' ');

        // Collapse unnatural bunsetsu spaces around Japanese characters and punctuation
        t = t.replace(/[ \t\u3000]+([、。！？])/g, '$1');
        t = t.replace(/([、。！？])[ \t\u3000]+/g, '$1');
        t = t.replace(/([\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF々ー])[ \t\u3000]+(?=[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF々ー0-9A-Za-z])/g, '$1');
        t = t.replace(/([0-9A-Za-z])[ \t\u3000]+(?=[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF々ー])/g, '$1');

        // Collapse remaining whitespace cleanly
        t = t.replace(/\s+/g, ' ').trim();

        return t;
    }

    // Split long Japanese passages into natural chunks (safe for Google TTS ~200 char limit)
    function splitJapaneseChunks(text, maxLen) {
        const limit = maxLen || 160;
        const clean = String(text || '').trim();
        if (!clean) return [];
        if (clean.length <= limit) return [clean];

        const rawSentences = clean.split(/([。！？!?\n]+)/);
        const sentences = [];
        for (let i = 0; i < rawSentences.length; i += 2) {
            const body = rawSentences[i] || '';
            const delim = rawSentences[i + 1] || '';
            const combined = (body + delim).trim();
            if (combined) sentences.push(combined);
        }

        const finePieces = [];
        sentences.forEach(s => {
            if (s.length <= limit) {
                finePieces.push(s);
                return;
            }
            const rawClauses = s.split(/([、，,;；]+)/);
            for (let i = 0; i < rawClauses.length; i += 2) {
                const part = ((rawClauses[i] || '') + (rawClauses[i + 1] || '')).trim();
                if (!part) continue;
                if (part.length <= limit) {
                    finePieces.push(part);
                } else {
                    for (let pos = 0; pos < part.length; pos += limit) {
                        const slice = part.slice(pos, pos + limit).trim();
                        if (slice) finePieces.push(slice);
                    }
                }
            }
        });

        const chunks = [];
        let buf = '';
        finePieces.forEach(piece => {
            if (!buf) {
                buf = piece;
            } else if ((buf + piece).length <= limit) {
                buf += piece;
            } else {
                chunks.push(buf);
                buf = piece;
            }
        });
        if (buf) chunks.push(buf);
        return chunks;
    }

    function resolveTriggerButton(explicitBtn) {
        if (explicitBtn && explicitBtn.classList) return explicitBtn;
        try {
            if (window.event) {
                const ev = window.event;
                const cand = ev.currentTarget || (ev.target && ev.target.closest && ev.target.closest('button'));
                if (cand && cand.classList && cand.tagName === 'BUTTON') return cand;
            }
        } catch (e) {}
        return null;
    }

    function isExternallyMuted() {
        try {
            const noopCompact = 'function(){}';
            if (typeof window.speakText === 'function' && String(window.speakText).replace(/\s+/g, '') === noopCompact) {
                return true;
            }
            if (window.AudioEngine && typeof window.AudioEngine.speak === 'function' && String(window.AudioEngine.speak).replace(/\s+/g, '') === noopCompact) {
                return true;
            }
        } catch (e) {}
        return false;
    }

    // 4. Secondary Fallback: Web Speech API with Tokyo Native Voices
    function playWithWebSpeechChunk(cleanText, myToken, onDone) {
        if (myToken !== playbackToken || !('speechSynthesis' in window)) {
            if (myToken === playbackToken && typeof onDone === 'function') onDone();
            return;
        }

        try {
            window.speechSynthesis.cancel();
            activeSpeechTimerId = setTimeout(() => {
                activeSpeechTimerId = null;
                if (myToken !== playbackToken) return;

                const utter = new SpeechSynthesisUtterance(cleanText);
                utter.lang = 'ja-JP';
                utter.rate = 0.94;
                utter.pitch = 1.0;

                const voices = cachedJaVoices.length > 0
                    ? cachedJaVoices
                    : (window.speechSynthesis.getVoices() || []).filter(v => v.lang && (v.lang === 'ja' || v.lang.startsWith('ja')));

                // Prioritize natural Tokyo voices (Kyoko, O-ren on macOS, Google 日本語, Otoya, Nanami, etc.)
                const bestVoice = voices.find(v => v.name.includes('Kyoko'))
                    || voices.find(v => v.name.includes('O-ren'))
                    || voices.find(v => v.name.includes('Google') && v.lang.startsWith('ja'))
                    || voices.find(v => v.name.includes('Otoya'))
                    || voices.find(v => v.name.includes('Nanami'))
                    || voices.find(v => v.name.includes('Keita'))
                    || voices.find(v => v.name.includes('Natural'))
                    || voices.find(v => v.name.includes('Enhanced'))
                    || voices[0];

                if (bestVoice) {
                    utter.voice = bestVoice;
                }

                utter.onend = () => {
                    if (myToken === playbackToken && typeof onDone === 'function') onDone();
                };
                utter.onerror = () => {
                    if (myToken === playbackToken && typeof onDone === 'function') onDone();
                };

                if (window.speechSynthesis.paused) {
                    window.speechSynthesis.resume();
                }
                window.speechSynthesis.speak(utter);
            }, 40);
        } catch (e) {
            if (myToken === playbackToken && typeof onDone === 'function') onDone();
        }
    }

    function playChunkDualEngine(chunk, myToken, onDone) {
        if (myToken !== playbackToken || !chunk) return;

        // Primary Engine: Google Studio Native Japanese Voice
        const audioUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=ja&client=tw-ob&q=${encodeURIComponent(chunk)}`;
        const audio = new Audio();
        audio.referrerPolicy = 'no-referrer';
        audio.preload = 'auto';
        audio.src = audioUrl;
        currentAudio = audio;

        let hasStarted = false;
        let finished = false;
        let fallbackInvoked = false;

        const finishChunk = () => {
            if (finished || myToken !== playbackToken) return;
            finished = true;
            clearActiveTimers();
            if (currentAudio === audio) {
                detachAudio(audio);
                currentAudio = null;
            }
            if (typeof onDone === 'function') onDone();
        };

        const invokeFallback = () => {
            if (fallbackInvoked || finished || myToken !== playbackToken) return;
            fallbackInvoked = true;
            clearActiveTimers();
            // CRITICAL: Stop and detach HTML5 Audio BEFORE starting Web Speech to prevent double-talk
            detachAudio(audio);
            if (currentAudio === audio) {
                currentAudio = null;
            }
            playWithWebSpeechChunk(chunk, myToken, () => {
                if (!finished && myToken === playbackToken) {
                    finished = true;
                    if (typeof onDone === 'function') onDone();
                }
            });
        };

        // Allow up to 2.6s for Google TTS buffering before failing over to Web Speech
        activeTimeoutId = setTimeout(() => {
            activeTimeoutId = null;
            if (!hasStarted && !finished && myToken === playbackToken) {
                invokeFallback();
            }
        }, 2600);

        audio.onplaying = () => {
            if (myToken !== playbackToken || fallbackInvoked) return;
            hasStarted = true;
            if (activeTimeoutId !== null) {
                clearTimeout(activeTimeoutId);
                activeTimeoutId = null;
            }
        };

        audio.onended = finishChunk;

        audio.onerror = () => {
            if (finished || myToken !== playbackToken) return;
            invokeFallback();
        };

        try {
            const playPromise = audio.play();
            if (playPromise && typeof playPromise.catch === 'function') {
                playPromise.catch(() => {
                    if (!hasStarted && !finished && myToken === playbackToken) {
                        invokeFallback();
                    }
                });
            }
        } catch (e) {
            invokeFallback();
        }
    }

    // 5. Queue & Main Dispatcher: Sequential Dual-Engine Japanese Speech
    function speakQueue(items, btnOrOpts, maybeOpts) {
        let explicitBtn = null;
        let opts = {};
        if (btnOrOpts && btnOrOpts.classList) {
            explicitBtn = btnOrOpts;
            if (maybeOpts && typeof maybeOpts === 'object') opts = maybeOpts;
        } else if (btnOrOpts && typeof btnOrOpts === 'object') {
            opts = btnOrOpts;
            explicitBtn = opts.btn || null;
        }

        const list = Array.isArray(items) ? items : [];
        if (!list.length) return;

        // Respect checkpoint-sync silence during state restoration
        if (isExternallyMuted()) {
            list.forEach(entry => {
                if (entry && typeof entry === 'object') {
                    if (typeof entry.onStart === 'function') entry.onStart();
                    if (typeof entry.onEnd === 'function') entry.onEnd();
                }
            });
            if (typeof opts.onEnd === 'function') opts.onEnd();
            return;
        }

        const queueBtn = resolveTriggerButton(explicitBtn);
        stopCurrentAudio();
        const myToken = playbackToken;

        if (queueBtn && queueBtn.classList) {
            currentActiveBtn = queueBtn;
            currentActiveBtn.classList.add('audio-playing');
        }

        function runItem(idx) {
            if (myToken !== playbackToken) return;
            if (idx >= list.length) {
                clearActiveButton();
                if (typeof opts.onEnd === 'function') opts.onEnd();
                return;
            }

            const entry = typeof list[idx] === 'string' ? { text: list[idx] } : (list[idx] || {});
            if (typeof entry.onStart === 'function') {
                try { entry.onStart(); } catch (e) {}
            }
            if (myToken !== playbackToken) return;

            const clean = cleanJapaneseText(entry.text);
            const chunks = splitJapaneseChunks(clean, 160);
            if (!chunks.length) {
                if (typeof entry.onEnd === 'function') {
                    try { entry.onEnd(); } catch (e) {}
                }
                runItem(idx + 1);
                return;
            }

            if (entry.btn && entry.btn.classList) {
                clearActiveButton();
                currentActiveBtn = entry.btn;
                currentActiveBtn.classList.add('audio-playing');
            }

            function runChunk(cIdx) {
                if (myToken !== playbackToken) return;
                if (cIdx >= chunks.length) {
                    if (typeof entry.onEnd === 'function') {
                        try { entry.onEnd(); } catch (e) {}
                    }
                    runItem(idx + 1);
                    return;
                }
                playChunkDualEngine(chunks[cIdx], myToken, () => runChunk(cIdx + 1));
            }

            runChunk(0);
        }

        runItem(0);
    }

    function speakJapanese(text, btnOrOpts, maybeOpts) {
        if (!text) return;
        const clean = cleanJapaneseText(text);
        if (!clean) return;
        speakQueue([{ text: clean }], btnOrOpts, maybeOpts);
    }

    // Expose globally under all commonly used names across the project
    window.speakJapanese = speakJapanese;
    window.speakText = speakJapanese;
    window.cleanJapaneseText = cleanJapaneseText;
    window.AudioEngine = {
        speak: speakJapanese,
        queue: speakQueue,
        stop: stopCurrentAudio,
        clean: cleanJapaneseText,
        splitChunks: splitJapaneseChunks
    };

})(window, document);
