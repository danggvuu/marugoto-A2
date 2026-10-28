# -*- coding: utf-8 -*-
"""
inject_motion_model_js.py
Injects advanced interactive KanjiVG stroke animation motion model,
debounced multi-field search, enriched table renderer, and flashcard logic into Tu_Vung_Marugoto_A1_16_A2_1_10.html
"""

import re

with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'r', encoding='utf-8') as f:
    html = f.read()

# JavaScript replacement for applyFilter, renderTable, renderCard, copyQuizletFormat, and the Kanji Motion Engine
new_js_logic = '''
    // ==========================================
    // FILTER LOGIC (Kanji, Kana, Han-Viet, Romaji, Vietnamese)
    // ==========================================
    function applyFilter() {
        const query = document.getElementById('searchInput').value.trim().toLowerCase();

        currentFiltered = rawVocab.filter(item => {
            const matchLesson = selectedLessons.has(item.l);
            if (!matchLesson) return false;
            if (!query) return true;

            return (item.kanji && item.kanji.toLowerCase().includes(query)) ||
                   (item.kana && item.kana.toLowerCase().includes(query)) ||
                   (item.hv && item.hv.toLowerCase().includes(query)) ||
                   (item.romaji && item.romaji.toLowerCase().includes(query)) ||
                   (item.vi && item.vi.toLowerCase().includes(query)) ||
                   (item.jp && item.jp.toLowerCase().includes(query));
        });

        // Cập nhật Badge số lượng & Quizlet count
        const summary = document.getElementById('selectionSummary');
        if (summary) {
            if (selectedLessons.size === LESSON_ORDER.length) {
                summary.textContent = `Đang chọn: Toàn bộ ${LESSON_ORDER.length} bài (${currentFiltered.length} từ)`;
            } else if (selectedLessons.size === 0) {
                summary.textContent = `Chưa chọn bài nào (vui lòng chọn bài)`;
            } else {
                const sortedSel = LESSON_ORDER.filter(l => selectedLessons.has(l));
                summary.textContent = `Đang chọn: ${sortedSel.length} bài [${sortedSel.join(', ')}] (${currentFiltered.length} từ)`;
            }
        }

        const quizCountEl = document.getElementById('quizletCount');
        if (quizCountEl) quizCountEl.innerText = currentFiltered.length;

        const footerCount = document.getElementById('lessonSelectionCount');
        if (footerCount) {
            footerCount.textContent = `Đang chọn: ${selectedLessons.size} bài (${currentFiltered.length} từ)`;
        }

        renderTable();
        currentCardIndex = 0;
        cardFlipped = false;
        if (document.getElementById('view-flashcard').classList.contains('active')) {
            renderCard();
        }
        if (document.getElementById('view-quiz').classList.contains('active')) {
            startNewQuizTest();
        }
    }

    // ==========================================
    // RENDER TABLE (7 Columns with Kanji, Kana, Han-Viet & Motion Trigger)
    // ==========================================
    function renderTable() {
        const tbody = document.getElementById('vocabTableBody');
        if (!tbody) return;

        if (currentFiltered.length === 0) {
            tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--gray); padding: 30px;">Không tìm thấy từ vựng nào phù hợp!</td></tr>`;
            return;
        }

        const rows = currentFiltered.map((item, idx) => {
            const safeKana = (item.kana || item.jp).replace(/'/g, "\\\\'");
            const safeKanji = (item.kanji || item.jp).replace(/'/g, "\\\\'");
            const hasKanji = item.kanji_chars && item.kanji_chars.length > 0;
            const strokeBtn = hasKanji ? `
                <button type="button" class="btn-stroke-model" onclick="event.stopPropagation(); openStrokeModel(${idx})" title="Xem mô hình animation chuyển động nét viết">
                    ✍️ Nét viết
                </button>
            ` : `<span class="no-stroke-tag">Kana</span>`;

            return `
                <tr class="vocab-row" onclick="onRowClick(${idx})">
                    <td class="col-stt"><strong>${idx + 1}</strong></td>
                    <td class="col-lesson"><span class="tag-lesson">${item.l}</span></td>
                    <td class="col-kanji">
                        <span class="kanji-word ${hasKanji ? 'clickable-kanji' : ''}" onclick="event.stopPropagation(); ${hasKanji ? `openStrokeModel(${idx})` : ''}" title="${hasKanji ? 'Click để xem chuyển động nét Kanji' : ''}">
                            ${item.kanji}
                        </span>
                    </td>
                    <td class="col-kana">
                        <span class="kana-word">${item.kana}</span>
                    </td>
                    <td class="col-hv">
                        <span class="badge-hv">${item.hv || ''}</span>
                    </td>
                    <td class="col-vi">
                        <span class="vi-word">${item.vi}</span>
                    </td>
                    <td class="col-actions">
                        <div class="action-btn-group">
                            <button type="button" class="btn-speak-inline fc-speaker-btn" onclick="event.stopPropagation(); speakJapanese('${safeKana}', this)" title="Nghe phát âm chuẩn Tokyo">🔊</button>
                            ${strokeBtn}
                        </div>
                    </td>
                </tr>
            `;
        }).join('');
        tbody.innerHTML = rows;
    }

    function onRowClick(idx) {
        const item = currentFiltered[idx];
        if (!item) return;
        if (item.kanji_chars && item.kanji_chars.length > 0) {
            loadMiniMotionChar(item.kanji_chars[0], item);
        }
    }

    // ==========================================
    // AUDIO HELPER (Dual Engine via audio-engine.js)
    // ==========================================
    function speakJapanese(text, btnEl) {
        if (window.speakText) {
            window.speakText(text, btnEl);
        }
    }

    function speakCurrent(e) {
        if (e) e.stopPropagation();
        if (currentFiltered.length === 0) return;
        const item = currentFiltered[currentCardIndex];
        speakJapanese(item.kana || item.jp);
    }

    // ==========================================
    // FLASHCARD LOGIC (QUIZLET STYLE 3D FLIP)
    // ==========================================
    let cardSidePrompt = 'jp'; // 'jp' = Mặt trước tiếng Nhật, 'vi' = Mặt trước tiếng Việt

    function renderCard() {
        const cardInner = document.getElementById('fcCardInner');
        const progressFill = document.getElementById('fcProgressFill');
        const fcProgress = document.getElementById('fcProgress');
        const fcCounter = document.getElementById('fcCounter');

        if (currentFiltered.length === 0) {
            document.getElementById('fcLessonFront').innerText = 'Trống';
            document.getElementById('fcLessonBack').innerText = 'Trống';
            document.getElementById('fcFront').innerHTML = 'Không có từ nào';
            document.getElementById('fcBackSub').innerText = '';
            document.getElementById('fcBack').innerHTML = 'Vui lòng chọn bài học';
            if (fcProgress) fcProgress.innerText = '0 / 0';
            if (fcCounter) fcCounter.innerText = '0 / 0';
            if (progressFill) progressFill.style.width = '0%';
            if (cardInner) cardInner.classList.remove('is-flipped');
            return;
        }

        const item = currentFiltered[currentCardIndex];
        const total = currentFiltered.length;
        const pct = Math.round(((currentCardIndex + 1) / total) * 100);

        document.getElementById('fcLessonFront').innerText = item.l;
        document.getElementById('fcLessonBack').innerText = item.l;

        const hasKanji = item.kanji_chars && item.kanji_chars.length > 0;
        const motionBtnHtml = hasKanji ? `
            <div style="margin-top: 14px;">
                <button type="button" class="btn-fc-motion" onclick="event.stopPropagation(); openStrokeModelForCurrent()">
                    ✍️ Xem chuyển động nét viết (${item.kanji_chars.join(', ')})
                </button>
            </div>
        ` : '';

        if (cardSidePrompt === 'jp') {
            document.getElementById('fcFront').innerHTML = `
                <div class="fc-kanji-huge">${item.kanji}</div>
                <div class="fc-kana-sub">${item.kana !== item.kanji ? item.kana : ''}</div>
                ${item.hv ? `<div class="fc-hv-badge">${item.hv}</div>` : ''}
                ${motionBtnHtml}
            `;
            document.getElementById('fcBackSub').innerHTML = `
                <strong>${item.kanji}</strong> ${item.kana !== item.kanji ? `[${item.kana}]` : ''}
                ${item.hv ? `<span class="badge-hv" style="margin-left: 8px;">${item.hv}</span>` : ''}
            `;
            document.getElementById('fcBack').innerHTML = `
                <div class="fc-meaning-text">${item.vi}</div>
                ${item.romaji ? `<div style="font-size: 0.95rem; color: #64748b; margin-top: 6px;">${item.romaji}</div>` : ''}
                ${motionBtnHtml}
            `;
        } else {
            document.getElementById('fcFront').innerHTML = `
                <div class="fc-meaning-text" style="font-size: 1.8rem; color: #0f172a;">${item.vi}</div>
            `;
            document.getElementById('fcBackSub').innerText = item.vi;
            document.getElementById('fcBack').innerHTML = `
                <div class="fc-kanji-huge">${item.kanji}</div>
                <div class="fc-kana-sub">${item.kana}</div>
                ${item.hv ? `<div class="fc-hv-badge">${item.hv}</div>` : ''}
                ${motionBtnHtml}
            `;
        }

        if (fcProgress) fcProgress.innerText = `${currentCardIndex + 1} / ${total}`;
        if (fcCounter) fcCounter.innerText = `${currentCardIndex + 1} / ${total}`;
        if (progressFill) progressFill.style.width = `${pct}%`;

        if (cardInner) {
            cardInner.classList.toggle('is-flipped', cardFlipped);
        }

        if (hasKanji) {
            loadMiniMotionChar(item.kanji_chars[0], item);
        }
    }

    function openStrokeModelForCurrent() {
        if (currentFiltered.length === 0) return;
        openStrokeModel(currentCardIndex);
    }

    function copyQuizletFormat() {
        if (currentFiltered.length === 0) {
            showToast("Không có từ nào để copy!");
            return;
        }

        const text = currentFiltered.map(item => {
            const jpText = item.kanji !== item.kana ? `${item.kanji} [${item.kana}]` : item.kanji;
            const hvText = item.hv ? ` ${item.hv}` : '';
            return `${jpText}${hvText}\\t${item.vi}`;
        }).join('\\n');

        navigator.clipboard.writeText(text).then(() => {
            showToast(`✅ Đã copy ${currentFiltered.length} từ vựng sang format Quizlet!`);
        }).catch(err => {
            const ta = document.createElement('textarea');
            ta.value = text;
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            showToast(`✅ Đã copy ${currentFiltered.length} từ vựng sang format Quizlet!`);
        });
    }

    // =========================================================================
    // KANJIVG STROKE ANIMATION MOTION MODEL ENGINE (INTERACTIVE SVG PLAYER)
    // =========================================================================
    const motionSvgCache = new Map();
    let currentMotionItem = null;
    let currentMotionChar = null;
    let motionPlayer = {
        char: '',
        totalStrokes: 0,
        currentStroke: 0,
        isPlaying: false,
        showNumbers: true,
        speed: 1.0,
        paths: [],
        ghostPaths: [],
        numbersGroup: null,
        timer: null
    };

    async function fetchKanjiSvg(char) {
        if (motionSvgCache.has(char)) return motionSvgCache.get(char);
        const hex = char.codePointAt(0).toString(16).padStart(5, '0');
        const urls = [
            `https://cdn.jsdelivr.net/gh/KanjiVG/kanjivg/kanji/${hex}.svg`,
            `https://raw.githubusercontent.com/KanjiVG/kanjivg/master/kanji/${hex}.svg`,
            `https://unpkg.com/kanjivg@latest/kanji/${hex}.svg`
        ];

        for (const url of urls) {
            try {
                const res = await fetch(url);
                if (res.ok) {
                    const text = await res.text();
                    if (text && text.includes('<path')) {
                        motionSvgCache.set(char, text);
                        return text;
                    }
                }
            } catch (e) {}
        }
        return null;
    }

    function openStrokeModel(itemIndex) {
        const item = currentFiltered[itemIndex];
        if (!item || !item.kanji_chars || item.kanji_chars.length === 0) {
            showToast("Từ này không chứa chữ Hán Kanji.");
            return;
        }

        currentMotionItem = item;
        document.getElementById('motionLessonBadge').innerText = item.l;
        document.getElementById('motionWordKanji').innerText = item.kanji;
        document.getElementById('motionWordKana').innerText = item.kana;
        document.getElementById('motionWordHv').innerText = item.hv || '';

        // Build character tabs
        const tabsWrap = document.getElementById('motionCharTabs');
        tabsWrap.innerHTML = item.kanji_chars.map((c, i) => `
            <button type="button" class="char-tab-btn ${i === 0 ? 'active' : ''}" onclick="selectMotionChar('${c}', this)">
                <span style="font-size:1.15rem; font-family:'Hiragino Mincho ProN', serif;">${c}</span>
            </button>
        `).join('');

        // Open modal backdrop
        const modal = document.getElementById('kanjiMotionModal');
        modal.classList.add('open');

        // Select first character
        selectMotionChar(item.kanji_chars[0]);

        // Init practice canvas
        initPracticeCanvas();
    }

    function closeStrokeModel() {
        if (motionPlayer.timer) clearTimeout(motionPlayer.timer);
        motionPlayer.isPlaying = false;
        const modal = document.getElementById('kanjiMotionModal');
        if (modal) modal.classList.remove('open');
    }

    function closeStrokeModelOnBackdrop(e) {
        if (e.target.id === 'kanjiMotionModal') {
            closeStrokeModel();
        }
    }

    function speakMotionWord() {
        if (currentMotionItem) {
            speakJapanese(currentMotionItem.kana || currentMotionItem.jp);
        }
    }

    async function selectMotionChar(char, btnEl) {
        if (motionPlayer.timer) clearTimeout(motionPlayer.timer);
        motionPlayer.isPlaying = false;
        currentMotionChar = char;

        if (btnEl) {
            document.querySelectorAll('.char-tab-btn').forEach(b => b.classList.remove('active'));
            btnEl.classList.add('active');
        }

        // Update Sidebar
        document.getElementById('charHugeDisplay').innerText = char;
        document.getElementById('charMetaHv').innerHTML = `Chữ: <strong>${char}</strong>`;
        document.getElementById('charMetaMeaning').innerText = currentMotionItem ? currentMotionItem.vi : '';

        const container = document.getElementById('kanjiSvgContainer');
        container.innerHTML = `<div class="motion-loading-spinner">Đang tải nét chữ <strong>${char}</strong>...</div>`;

        const svgText = await fetchKanjiSvg(char);
        if (svgText) {
            setupMotionSvgPlayer(char, svgText);
            loadMiniMotionChar(char, currentMotionItem);
        } else {
            container.innerHTML = `
                <div style="text-align:center; padding:20px; color:#64748b;">
                    <div style="font-size:3.5rem; font-family:'Hiragino Mincho ProN',serif; color:#0f172a;">${char}</div>
                    <div style="font-size:0.85rem; margin-top:8px;">(Đang hiển thị phông chữ hệ thống)</div>
                </div>
            `;
            document.getElementById('stepStripScroll').innerHTML = '<span style="font-size:0.82rem; color:#94a3b8;">Không có dữ liệu phân rã cho chữ này.</span>';
        }
    }

    function setupMotionSvgPlayer(char, svgText) {
        const container = document.getElementById('kanjiSvgContainer');
        const parser = new DOMParser();
        const doc = parser.parseFromString(svgText, 'image/svg+xml');
        const rawSvg = doc.querySelector('svg');
        if (!rawSvg) return;

        const rawPaths = Array.from(rawSvg.querySelectorAll('path'));
        const total = rawPaths.length;
        document.getElementById('charStrokeCountVal').innerText = total;

        motionPlayer.char = char;
        motionPlayer.totalStrokes = total;
        motionPlayer.currentStroke = total;
        motionPlayer.isPlaying = false;
        motionPlayer.paths = [];
        motionPlayer.ghostPaths = [];

        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('viewBox', '0 0 109 109');

        // 1. Ghost Strokes Group
        const ghostGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        rawPaths.forEach(rp => {
            const gp = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            gp.setAttribute('d', rp.getAttribute('d'));
            gp.setAttribute('fill', 'none');
            gp.setAttribute('stroke', '#e2e8f0');
            gp.setAttribute('stroke-width', '4');
            gp.setAttribute('stroke-linecap', 'round');
            gp.setAttribute('stroke-linejoin', 'round');
            ghostGroup.appendChild(gp);
            motionPlayer.ghostPaths.push(gp);
        });
        svg.appendChild(ghostGroup);

        // 2. Active Strokes Group
        const activeGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        rawPaths.forEach(rp => {
            const ap = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            ap.setAttribute('d', rp.getAttribute('d'));
            ap.setAttribute('fill', 'none');
            ap.setAttribute('stroke', '#0f172a');
            ap.setAttribute('stroke-width', '4.5');
            ap.setAttribute('stroke-linecap', 'round');
            ap.setAttribute('stroke-linejoin', 'round');
            activeGroup.appendChild(ap);
            motionPlayer.paths.push(ap);
        });
        svg.appendChild(activeGroup);

        // 3. Stroke Numbers Group
        const rawNumbers = rawSvg.querySelector('[id*="StrokeNumbers"]');
        if (rawNumbers) {
            const numbersGroup = rawNumbers.cloneNode(true);
            numbersGroup.querySelectorAll('text').forEach(t => {
                t.setAttribute('fill', '#e11d48');
                t.setAttribute('font-size', '8');
                t.setAttribute('font-weight', 'bold');
            });
            svg.appendChild(numbersGroup);
            motionPlayer.numbersGroup = numbersGroup;
            numbersGroup.style.display = motionPlayer.showNumbers ? 'inline' : 'none';
        }

        container.innerHTML = '';
        container.appendChild(svg);

        // Prep stroke lengths
        motionPlayer.paths.forEach(p => {
            try {
                const len = p.getTotalLength();
                p.style.strokeDasharray = `${len} ${len}`;
                p.style.strokeDashoffset = '0';
            } catch (e) {}
        });

        // Generate Step Breakdown Strip
        generateStepBreakdown(rawPaths);

        // Update play button text
        const playBtn = document.getElementById('btnMotionPlay');
        if (playBtn) playBtn.innerHTML = '🔄 Vẽ lại';
    }

    function generateStepBreakdown(rawPaths) {
        const strip = document.getElementById('stepStripScroll');
        strip.innerHTML = '';

        for (let step = 1; step <= rawPaths.length; step++) {
            const thumb = document.createElement('div');
            thumb.className = `step-thumb ${step === rawPaths.length ? 'active' : ''}`;
            thumb.onclick = () => jumpToStroke(step);

            const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
            svg.setAttribute('viewBox', '0 0 109 109');

            // ghost all
            rawPaths.forEach(rp => {
                const gp = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                gp.setAttribute('d', rp.getAttribute('d'));
                gp.setAttribute('fill', 'none');
                gp.setAttribute('stroke', '#e2e8f0');
                gp.setAttribute('stroke-width', '5');
                svg.appendChild(gp);
            });

            // active up to step
            for (let i = 0; i < step; i++) {
                const ap = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                ap.setAttribute('d', rawPaths[i].getAttribute('d'));
                ap.setAttribute('fill', 'none');
                ap.setAttribute('stroke', i === step - 1 ? '#0284c7' : '#0f172a');
                ap.setAttribute('stroke-width', i === step - 1 ? '6' : '5');
                svg.appendChild(ap);
            }

            thumb.appendChild(svg);
            const num = document.createElement('span');
            num.className = 'step-num-badge';
            num.innerText = step;
            thumb.appendChild(num);

            strip.appendChild(thumb);
        }
    }

    function jumpToStroke(targetStep) {
        if (motionPlayer.timer) clearTimeout(motionPlayer.timer);
        motionPlayer.isPlaying = false;
        motionPlayer.currentStroke = targetStep;

        motionPlayer.paths.forEach((p, idx) => {
            try {
                const len = p.getTotalLength();
                if (idx < targetStep) {
                    p.style.transition = 'none';
                    p.style.strokeDashoffset = '0';
                    p.setAttribute('stroke', idx === targetStep - 1 ? '#0284c7' : '#0f172a');
                } else {
                    p.style.transition = 'none';
                    p.style.strokeDashoffset = `${len}`;
                }
            } catch (e) {}
        });

        // Update strip active state
        document.querySelectorAll('.step-thumb').forEach((th, i) => {
            th.classList.toggle('active', i + 1 === targetStep);
        });

        const playBtn = document.getElementById('btnMotionPlay');
        if (playBtn) playBtn.innerHTML = '▶️ Tiếp tục';
    }

    function toggleMotionPlay() {
        if (motionPlayer.isPlaying) {
            if (motionPlayer.timer) clearTimeout(motionPlayer.timer);
            motionPlayer.isPlaying = false;
            document.getElementById('btnMotionPlay').innerHTML = '▶️ Tiếp tục';
        } else {
            if (motionPlayer.currentStroke >= motionPlayer.totalStrokes) {
                replayMotion();
            } else {
                playNextStroke();
            }
        }
    }

    function playNextStroke() {
        if (motionPlayer.currentStroke >= motionPlayer.totalStrokes) {
            motionPlayer.isPlaying = false;
            document.getElementById('btnMotionPlay').innerHTML = '🔄 Vẽ lại';
            return;
        }

        motionPlayer.isPlaying = true;
        document.getElementById('btnMotionPlay').innerHTML = '⏸️ Tạm dừng';

        const strokeIdx = motionPlayer.currentStroke;
        const path = motionPlayer.paths[strokeIdx];
        if (!path) return;

        try {
            const len = path.getTotalLength();
            path.style.transition = 'none';
            path.style.strokeDashoffset = `${len}`;
            path.setAttribute('stroke', '#0284c7');

            setTimeout(() => {
                const duration = (650 / motionPlayer.speed);
                path.style.transition = `stroke-dashoffset ${duration}ms cubic-bezier(0.4, 0, 0.2, 1)`;
                path.style.strokeDashoffset = '0';

                motionPlayer.currentStroke++;
                jumpToStripActive(motionPlayer.currentStroke);

                motionPlayer.timer = setTimeout(() => {
                    path.setAttribute('stroke', '#0f172a');
                    if (motionPlayer.isPlaying) {
                        playNextStroke();
                    }
                }, duration + 150);
            }, 30);
        } catch (e) {
            motionPlayer.currentStroke++;
            if (motionPlayer.isPlaying) playNextStroke();
        }
    }

    function jumpToStripActive(step) {
        document.querySelectorAll('.step-thumb').forEach((th, i) => {
            th.classList.toggle('active', i + 1 === step);
        });
    }

    function replayMotion() {
        if (motionPlayer.timer) clearTimeout(motionPlayer.timer);
        motionPlayer.currentStroke = 0;
        motionPlayer.paths.forEach(p => {
            try {
                const len = p.getTotalLength();
                p.style.transition = 'none';
                p.style.strokeDashoffset = `${len}`;
                p.setAttribute('stroke', '#0f172a');
            } catch (e) {}
        });
        jumpToStripActive(0);
        playNextStroke();
    }

    function stepMotionNext() {
        if (motionPlayer.timer) clearTimeout(motionPlayer.timer);
        motionPlayer.isPlaying = false;
        if (motionPlayer.currentStroke < motionPlayer.totalStrokes) {
            jumpToStroke(motionPlayer.currentStroke + 1);
        }
    }

    function stepMotionPrev() {
        if (motionPlayer.timer) clearTimeout(motionPlayer.timer);
        motionPlayer.isPlaying = false;
        if (motionPlayer.currentStroke > 1) {
            jumpToStroke(motionPlayer.currentStroke - 1);
        } else {
            jumpToStroke(1);
        }
    }

    function toggleMotionNumbers() {
        motionPlayer.showNumbers = !motionPlayer.showNumbers;
        if (motionPlayer.numbersGroup) {
            motionPlayer.numbersGroup.style.display = motionPlayer.showNumbers ? 'inline' : 'none';
        }
        document.getElementById('btnMotionNumbers').classList.toggle('active', motionPlayer.showNumbers);
    }

    function setMotionSpeed(speed, btn) {
        motionPlayer.speed = speed;
        document.querySelectorAll('.speed-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
    }

    // ==========================================
    // PRACTICE CANVAS DRAWING LOGIC
    // ==========================================
    let isDrawing = false;
    let practiceCtx = null;

    function initPracticeCanvas() {
        const canvas = document.getElementById('motionCanvas');
        if (!canvas) return;
        practiceCtx = canvas.getContext('2d');
        practiceCtx.lineWidth = 8;
        practiceCtx.lineCap = 'round';
        practiceCtx.lineJoin = 'round';
        practiceCtx.strokeStyle = '#0284c7';

        const getPos = (e) => {
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            return {
                x: (clientX - rect.left) * (canvas.width / rect.width),
                y: (clientY - rect.top) * (canvas.height / rect.height)
            };
        };

        const startDraw = (e) => {
            e.preventDefault();
            isDrawing = true;
            const pos = getPos(e);
            practiceCtx.beginPath();
            practiceCtx.moveTo(pos.x, pos.y);
        };

        const moveDraw = (e) => {
            if (!isDrawing) return;
            e.preventDefault();
            const pos = getPos(e);
            practiceCtx.lineTo(pos.x, pos.y);
            practiceCtx.stroke();
        };

        const endDraw = (e) => {
            isDrawing = false;
        };

        canvas.onmousedown = startDraw;
        canvas.onmousemove = moveDraw;
        canvas.onmouseup = endDraw;
        canvas.onmouseleave = endDraw;

        canvas.ontouchstart = startDraw;
        canvas.ontouchmove = moveDraw;
        canvas.ontouchend = endDraw;
    }

    function switchMotionMode(mode) {
        const canvas = document.getElementById('motionCanvas');
        const actions = document.getElementById('practiceActionsRow');
        const btnWatch = document.getElementById('btnModeWatch');
        const btnDraw = document.getElementById('btnModeDraw');

        if (mode === 'draw') {
            canvas.classList.add('active');
            actions.style.display = 'flex';
            btnDraw.classList.add('active');
            btnWatch.classList.remove('active');
            clearPracticeCanvas();
        } else {
            canvas.classList.remove('active');
            actions.style.display = 'none';
            btnWatch.classList.add('active');
            btnDraw.classList.remove('active');
        }
    }

    function clearPracticeCanvas() {
        const canvas = document.getElementById('motionCanvas');
        if (practiceCtx && canvas) {
            practiceCtx.clearRect(0, 0, canvas.width, canvas.height);
        }
    }

    let ghostHidden = false;
    function togglePracticeGhost() {
        ghostHidden = !ghostHidden;
        const svgContainer = document.getElementById('kanjiSvgContainer');
        if (svgContainer) {
            svgContainer.style.opacity = ghostHidden ? '0' : '1';
        }
        document.getElementById('btnToggleGhost').innerText = ghostHidden ? '👁️ Hiện nét mờ' : '👁️ Ẩn nét mờ';
    }

    // ==========================================
    // FLOATING MINI MOTION WIDGET
    // ==========================================
    async function loadMiniMotionChar(char, item) {
        const charEl = document.getElementById('miniMotionChar');
        const hvEl = document.getElementById('miniMotionHv');
        const descEl = document.getElementById('miniWordDesc');
        const container = document.getElementById('miniSvgContainer');

        if (charEl) charEl.innerText = char;
        if (hvEl) hvEl.innerText = item.hv ? item.hv.replace(/[\\[\\]]/g, '') : '';
        if (descEl) descEl.innerText = item.vi;

        if (!container) return;
        const svgText = await fetchKanjiSvg(char);
        if (!svgText) {
            container.innerHTML = `<span style="font-size:3rem; font-family:'Hiragino Mincho ProN',serif; color:#0f172a;">${char}</span>`;
            return;
        }

        const parser = new DOMParser();
        const doc = parser.parseFromString(svgText, 'image/svg+xml');
        const rawSvg = doc.querySelector('svg');
        if (!rawSvg) return;

        container.innerHTML = '';
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('viewBox', '0 0 109 109');

        const paths = Array.from(rawSvg.querySelectorAll('path'));
        paths.forEach(rp => {
            const p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            p.setAttribute('d', rp.getAttribute('d'));
            p.setAttribute('fill', 'none');
            p.setAttribute('stroke', '#0284c7');
            p.setAttribute('stroke-width', '5');
            p.setAttribute('stroke-linecap', 'round');
            p.setAttribute('stroke-linejoin', 'round');
            svg.appendChild(p);
        });

        container.appendChild(svg);
    }

    function expandMiniMotion() {
        if (currentMotionItem) {
            const idx = currentFiltered.indexOf(currentMotionItem);
            if (idx !== -1) {
                openStrokeModel(idx);
                return;
            }
        }
        if (currentFiltered.length > 0) {
            openStrokeModel(0);
        }
    }

    function toggleMiniMotionMinimize() {
        const widget = document.getElementById('miniMotionWidget');
        const btn = document.getElementById('btnMiniToggle');
        if (widget) {
            widget.classList.toggle('minimized');
            btn.innerText = widget.classList.contains('minimized') ? '+' : '–';
        }
    }
'''

# Find the block in html from `function applyFilter()` to `function copyQuizletFormat()`
# and replace it with `new_js_logic`
start_marker = "    // Filter Logic Chính (Kết hợp các bài đã chọn + Từ khóa)\n    function applyFilter() {"
end_marker = "    function copyQuizletFormat() {"

idx_start = html.find(start_marker)
if idx_start == -1:
    idx_start = html.find("function applyFilter() {")

idx_copy = html.find(end_marker)
if idx_copy != -1:
    # Find end of copyQuizletFormat function
    idx_end = html.find("    function toggleQuizSettings() {", idx_copy)
    if idx_end == -1:
        idx_end = html.find("    let quizSettings =", idx_copy)
    
    if idx_start != -1 and idx_end != -1:
        html = html[:idx_start] + new_js_logic + "\n" + html[idx_end:]
        print("Replaced old filter/table/card logic with enriched Kanji Motion Engine!")
    else:
        print(f"Error finding markers: start={idx_start}, end={idx_end}")
else:
    print("Could not find copyQuizletFormat marker!")

with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Tu_Vung_Marugoto_A1_16_A2_1_10.html JS update complete!")
