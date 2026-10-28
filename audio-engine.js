/**
 * UNIFIED TOKYO JAPANESE AUDIO ENGINE (DUAL ENGINE)
 * ==========================================================================
 * Engine 1 (Primary): Google Studio High-Fidelity Japanese TTS (Tokyo Native)
 * Engine 2 (Fallback): Web Speech API (macOS Kyoko, Otoya, Google 日本語)
 * Compatibility: Cốc Cốc, Chrome, Safari, Edge, Firefox, iOS, Android
 * Referrer Policy: Explicit 'no-referrer' to bypass 403 Forbidden blocks
 * ==========================================================================
 */

(function (window, document) {
    'use strict';

    let currentAudio = null;
    let cachedJaVoices = [];
    let isVoicesReady = false;

    // 1. Inject pulse animation style for active audio buttons if not already present
    function injectAudioStyles() {
        if (document.getElementById('unified-audio-engine-styles')) return;
        const style = document.createElement('style');
        style.id = 'unified-audio-engine-styles';
        style.textContent = `
            .btn-speak.audio-playing, 
            .sound-btn.audio-playing, 
            .fc-audio-btn.audio-playing, 
            .quiz-sound-btn.audio-playing {
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
                if (cachedJaVoices.length > 0) isVoicesReady = true;
            };
            update();
            if (window.speechSynthesis.onvoiceschanged !== undefined) {
                window.speechSynthesis.onvoiceschanged = update;
            }
        } catch (e) {}
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            injectAudioStyles();
            initVoices();
        });
    } else {
        injectAudioStyles();
        initVoices();
    }

    // 3. Bulletproof Japanese Text Normalizer (Preserves Japanese phrases in brackets like （ドアを）あけます)
    function cleanJapaneseText(text) {
        if (!text) return '';
        let t = String(text).trim();

        // Remove ruby / furigana HTML elements cleanly
        t = t.replace(/<rt>.*?<\/rt>/gi, '').replace(/<[^>]*>/g, '');

        // Remove angle bracketed non-Japanese notes (e.g. 〈Số đếm〉)
        t = t.replace(/〈[^〉]*〉/g, '');

        // If slash alternative exists (e.g. しゃけ／さけ, そふ／おじいさん), pick the first one
        if (t.includes('/') || t.includes('／')) {
            t = t.split('/')[0].split('／')[0].trim();
        }

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

        // Strip lone tildes, bullets, arrows, decorative symbols, question marks
        t = t.replace(/[～〜・→➔*#_?？]/g, '');

        // Collapse multiple spaces
        t = t.replace(/\s+/g, ' ').trim();

        return t;
    }

    // 4. Secondary Fallback: Web Speech API with Tokyo Native Voices
    function playWithWebSpeech(cleanText, targetBtn) {
        if (!('speechSynthesis' in window)) {
            if (targetBtn && targetBtn.classList) targetBtn.classList.remove('audio-playing');
            return;
        }

        try {
            window.speechSynthesis.cancel();
            setTimeout(() => {
                const utter = new SpeechSynthesisUtterance(cleanText);
                utter.lang = 'ja-JP';
                utter.rate = 0.92;
                utter.pitch = 1.0;

                const voices = cachedJaVoices.length > 0 ? cachedJaVoices : (window.speechSynthesis.getVoices() || []).filter(v => v.lang && v.lang.startsWith('ja'));
                
                // Prioritize natural Tokyo voices (Kyoko on Mac, Google 日本語 on Chrome, Otoya, Nanami, etc.)
                const bestVoice = voices.find(v => v.name.includes('Kyoko'))
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
                    if (targetBtn && targetBtn.classList) targetBtn.classList.remove('audio-playing');
                };

                utter.onerror = () => {
                    if (targetBtn && targetBtn.classList) targetBtn.classList.remove('audio-playing');
                };

                if (window.speechSynthesis.paused) {
                    window.speechSynthesis.resume();
                }
                window.speechSynthesis.speak(utter);
            }, 50);
        } catch (e) {
            if (targetBtn && targetBtn.classList) targetBtn.classList.remove('audio-playing');
        }
    }

    // 5. Main Dispatcher: Dual-Engine Japanese Speech
    function speakJapanese(text, btnElement) {
        if (!text) return;
        const clean = cleanJapaneseText(text);
        if (!clean) return;

        // Resolve trigger button for visual feedback
        let targetBtn = btnElement;
        if (!targetBtn && window.event) {
            const ev = window.event;
            targetBtn = ev.currentTarget || (ev.target && ev.target.closest('button'));
        }
        if (targetBtn && targetBtn.classList) {
            targetBtn.classList.add('audio-playing');
        }

        // Cancel previous audio
        if (currentAudio) {
            try {
                currentAudio.pause();
                currentAudio.currentTime = 0;
            } catch (e) {}
            currentAudio = null;
        }
        if ('speechSynthesis' in window) {
            try { window.speechSynthesis.cancel(); } catch (e) {}
        }

        // Primary Engine: Google Studio Native Japanese Voice
        const encoded = encodeURIComponent(clean);
        const audioUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=ja&client=tw-ob&q=${encoded}`;

        const audio = new Audio();
        audio.referrerPolicy = 'no-referrer';
        audio.src = audioUrl;
        currentAudio = audio;

        let hasStarted = false;
        let fallbackInvoked = false;

        const invokeFallback = () => {
            if (fallbackInvoked) return;
            fallbackInvoked = true;
            playWithWebSpeech(clean, targetBtn);
        };

        // If audio does not start playing within 1.2 seconds, invoke fallback
        const timeoutId = setTimeout(() => {
            if (!hasStarted) {
                invokeFallback();
            }
        }, 1200);

        audio.onplaying = () => {
            hasStarted = true;
            clearTimeout(timeoutId);
        };

        audio.onended = () => {
            clearTimeout(timeoutId);
            if (targetBtn && targetBtn.classList) {
                targetBtn.classList.remove('audio-playing');
            }
        };

        audio.onerror = () => {
            clearTimeout(timeoutId);
            invokeFallback();
        };

        const playPromise = audio.play();
        if (playPromise !== undefined) {
            playPromise.catch(() => {
                clearTimeout(timeoutId);
                invokeFallback();
            });
        }
    }

    // Expose globally under all commonly used names across the project
    window.speakJapanese = speakJapanese;
    window.speakText = speakJapanese;
    window.cleanJapaneseText = cleanJapaneseText;

})(window, document);
