/**
 * TỰ ĐỘNG TỪ VS THA ĐỘNG TỪ (自動詞・他動詞) - MASTER CONTROLLER
 * Đồng bộ với hệ thống Marugoto A1-A2 Design System & Tokyo Audio Engine.
 */

(function () {
    'use strict';

    const STORAGE_KEY = 'marugoto_tu_tha_checkpoint_v1';
    const CONTENT_VERSION = 2;
    window.__MARUGOTO_CP_EXTRA_KEYS__ = [...new Set([...(window.__MARUGOTO_CP_EXTRA_KEYS__ || []), STORAGE_KEY])];
    let currentCategory = 'all';
    let currentHideMode = 'none'; // 'none' | 'hide_ji' | 'hide_ta'
    let currentSearchQuery = '';

    // State cho Quiz
    let userQuizAnswers = {}; // qId -> selectedIndex
    let isQuizGraded = false;

    // State cho Lab
    let selectedLabPairId = 1;
    let selectedLabTense = 'masu'; // 'masu' | 'te_iru' | 'te_aru' | 'ta'

    // ==========================================
    // 1. KHỞI TẠO & RENDER BẢNG 50 CẶP ĐỘNG TỪ
    // ==========================================
    function init() {
        restoreCheckpoint();
        renderPairsTable();
        renderQuiz();
        renderLab();
        bindEvents();
    }

    function renderPairsTable() {
        const tableBody = document.getElementById('pairsTableBody');
        if (!tableBody || !window.TU_THA_PAIRS_DATA) return;

        const filtered = window.TU_THA_PAIRS_DATA.filter(item => {
            const matchCat = (currentCategory === 'all' || item.cat === currentCategory);
            if (!matchCat) return false;

            if (!currentSearchQuery) return true;
            const q = currentSearchQuery.toLowerCase().trim();
            const textToSearch = [
                item.meaning,
                item.pattern,
                item.ji.kanji, item.ji.kana, item.ji.masu, item.ji.example, item.ji.exVi,
                item.ta.kanji, item.ta.kana, item.ta.masu, item.ta.example, item.ta.exVi
            ].join(' ').toLowerCase();

            return textToSearch.includes(q);
        });

        const countBadge = document.getElementById('filterCountBadge');
        if (countBadge) countBadge.textContent = `${filtered.length} / ${window.TU_THA_PAIRS_DATA.length} cặp`;

        if (filtered.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="5" style="text-align:center; padding:32px; color:var(--text-muted);">
                🔍 Không tìm thấy cặp động từ nào phù hợp với từ khóa "<strong>${escapeHtml(currentSearchQuery)}</strong>".
            </td></tr>`;
            return;
        }

        tableBody.innerHTML = filtered.map((pair, idx) => {
            const hideJi = (currentHideMode === 'hide_ji');
            const hideTa = (currentHideMode === 'hide_ta');

            return `
            <tr class="pair-row" id="pair-row-${pair.id}">
                <td class="col-stt">
                    <span class="stt-badge">${idx + 1}</span>
                    <span class="pattern-tag">${escapeHtml(pair.pattern)}</span>
                </td>
                <td class="col-meaning">
                    <strong class="meaning-title">${escapeHtml(pair.meaning)}</strong>
                    <span class="cat-pill">${escapeHtml(pair.catName)}</span>
                    <div class="note-pill">${escapeHtml(pair.note)}</div>
                </td>
                <td class="col-verb col-ji">
                    <div class="verb-cell ${hideJi ? 'is-hidden-mask' : ''}" onclick="revealHiddenCell(this)">
                        <div class="verb-main">
                            <span class="verb-kanji">${escapeHtml(pair.ji.kanji)}</span>
                            <span class="verb-kana">【${escapeHtml(pair.ji.kana)}】</span>
                            <button type="button" class="audio-mini-btn" onclick="event.stopPropagation(); playVerb('${pair.ji.masu}', this)" title="Nghe phát âm">🔊</button>
                        </div>
                        <div class="verb-masu-tag">
                            <span class="particle-badge particle-ga">が</span>
                            <code class="jp-code">${escapeHtml(pair.ji.masu)}</code>
                        </div>
                        <div class="verb-example">
                            <span class="ex-jp">${escapeHtml(pair.ji.example)}</span>
                            <span class="ex-vi">${escapeHtml(pair.ji.exVi)}</span>
                        </div>
                        ${hideJi ? '<div class="mask-overlay">🙈 Chạm để lật mở Tự Động Từ</div>' : ''}
                    </div>
                </td>
                <td class="col-verb col-ta">
                    <div class="verb-cell ${hideTa ? 'is-hidden-mask' : ''}" onclick="revealHiddenCell(this)">
                        <div class="verb-main">
                            <span class="verb-kanji">${escapeHtml(pair.ta.kanji)}</span>
                            <span class="verb-kana">【${escapeHtml(pair.ta.kana)}】</span>
                            <button type="button" class="audio-mini-btn" onclick="event.stopPropagation(); playVerb('${pair.ta.masu}', this)" title="Nghe phát âm">🔊</button>
                        </div>
                        <div class="verb-masu-tag">
                            <span class="particle-badge particle-wo">を</span>
                            <code class="jp-code">${escapeHtml(pair.ta.masu)}</code>
                        </div>
                        <div class="verb-example">
                            <span class="ex-jp">${escapeHtml(pair.ta.example)}</span>
                            <span class="ex-vi">${escapeHtml(pair.ta.exVi)}</span>
                        </div>
                        ${hideTa ? '<div class="mask-overlay">🙈 Chạm để lật mở Tha Động Từ</div>' : ''}
                    </div>
                </td>
                <td class="col-action">
                    <button type="button" class="btn-lab-quick" onclick="openPairInLab(${pair.id})" title="Thử nghiệm cặp này trong Lab">🧪 So sánh</button>
                </td>
            </tr>
            `;
        }).join('');
    }

    // ==========================================
    // 2. PHÒNG THÍ NGHIỆM SO SÁNH TỰ - THA (LAB)
    // ==========================================
    function renderLab() {
        if (!window.TU_THA_PAIRS_DATA) return;
        const pair = window.TU_THA_PAIRS_DATA.find(p => p.id === selectedLabPairId) || window.TU_THA_PAIRS_DATA[0];
        if (!pair) return;

        // Cập nhật Select Cặp từ
        const select = document.getElementById('labPairSelect');
        if (select && select.children.length === 0) {
            select.innerHTML = window.TU_THA_PAIRS_DATA.map(p => `
                <option value="${p.id}" ${p.id === selectedLabPairId ? 'selected' : ''}>
                    ${p.id}. ${p.meaning} (${p.ji.kanji} vs ${p.ta.kanji})
                </option>
            `).join('');
        }
        if (select) select.value = String(pair.id);
        document.querySelectorAll('.lab-tense-pill').forEach(btn => {
            btn.classList.toggle('active', (btn.getAttribute('onclick') || '').includes(`'${selectedLabTense}'`));
        });
        // Explicit sentence frames avoid splicing a kana form onto a Kanji stem.
        const frame = window.TU_THA_LAB_FRAMES[pair.id - 1];
        const viFor = (role, tense) => tense === 'masu' ? pair[role].exVi
            : tense === 'ta' ? `Ví dụ dạng quá khứ: ${pair.meaning}.`
                : tense === 'te_aru' ? 'Trạng thái được chuẩn bị sẵn bằng hành động có chủ ý.'
                    : role === 'ji' ? 'Hành động hoặc trạng thái của sự vật/chủ thể.'
                        : 'Hành động của người tác động lên đối tượng.';

        // Card Tự động từ
        const jiCard = document.getElementById('labJiCard');
        if (jiCard) {
            let jiVerbForm = pair.ji.masu;
            let jiContext = pair.ji.example;
            let jiGrammarExplain = "Mô tả trạng thái hoặc hiện tượng tự thân diễn ra (không cần người làm).";

            if (selectedLabTense === 'te_iru') {
                jiVerbForm = `${pair.ji.te} います`;
                jiContext = `${frame.ji} ${pair.ji.te}います。`;
                jiGrammarExplain = "Tùy động từ, ～ています diễn tả hành động, thói quen hoặc trạng thái kết quả; không phải mọi tự động từ đều chỉ trạng thái.";
            } else if (selectedLabTense === 'te_aru') {
                jiVerbForm = `<span style="color:#ef4444; font-size:0.85rem;">⚠️ Tự động từ KHÔNG ĐI với ～てあります!</span>`;
                jiContext = `❌ Không dùng với Tự động từ. (～てあります chỉ đi với Tha động từ có chủ ý!)`;
                jiGrammarExplain = "Quy tắc ngữ pháp quan trọng: ～てあります biểu thị hành động có chủ ý của con người nên chỉ đi với THA ĐỘNG TỪ.";
            } else if (selectedLabTense === 'ta') {
                jiVerbForm = pair.ji.masu.replace('ます', 'ました');
                jiContext = `${frame.ji} ${jiVerbForm}。`;
                jiGrammarExplain = "Hành động/sự biến đổi đã hoàn thành trong quá khứ.";
            }

            jiCard.innerHTML = `
                <div class="lab-card-header is-ji">
                    <span class="lab-role-tag">🟢 TỰ ĐỘNG TỪ (自動詞 - Jidoushi)</span>
                    <span class="lab-particle-pill">Trợ từ: <strong>が</strong></span>
                </div>
                <div class="lab-card-body">
                    <div class="lab-word-hero">
                        <span class="lab-kanji">${escapeHtml(pair.ji.kanji)}</span>
                        <span class="lab-kana">【${escapeHtml(pair.ji.kana)}】</span>
                        <button type="button" class="audio-mini-btn" onclick="playVerb('${pair.ji.masu}', this)">🔊</button>
                    </div>
                    <div class="lab-tense-display">
                        <span class="lab-tense-lbl">Dạng đang chọn:</span>
                        <div class="lab-tense-val">${jiVerbForm}</div>
                    </div>
                    <div class="lab-sentence-box">
                        <div class="lab-sentence-jp">${escapeHtml(jiContext)}</div>
                        <div class="lab-sentence-vi">${escapeHtml(viFor('ji', selectedLabTense))}</div>
                    </div>
                    <div class="lab-explain-box">
                        💡 <strong>Bản chất:</strong> ${jiGrammarExplain}
                    </div>
                </div>
            `;
        }

        // Card Tha động từ
        const taCard = document.getElementById('labTaCard');
        if (taCard) {
            let taVerbForm = pair.ta.masu;
            let taContext = pair.ta.example;
            let taGrammarExplain = "Có con người chủ động tác động lực hoặc ý chí lên đồ vật.";

            if (selectedLabTense === 'te_iru') {
                taVerbForm = `${pair.ta.te} います`;
                taContext = `${frame.ta} ${pair.ta.te}います。`;
                taGrammarExplain = "Hành động của con người đang diễn tiến trong thời điểm nói (ví dụ: đang mở cửa).";
            } else if (selectedLabTense === 'te_aru') {
                taVerbForm = `${pair.ta.te} あります`;
                // Đổi trợ từ sang が khi đi với te aru
                taContext = `${frame.aru} ${pair.ta.te}あります。`;
                taGrammarExplain = "Vật đã được ai đó làm sẵn nhằm một mục đích nhất định (vẫn còn lưu lại kết quả).";
                if (!frame.aru) {
                    taVerbForm = '<span style="font-size:.85rem;">Không dùng ví dụ ～てある cho cặp này</span>';
                    taContext = 'Không áp dụng máy móc ～てあります cho cặp này.';
                    taGrammarExplain = 'Chỉ dùng ～てあります khi hành động có chủ ý và để lại kết quả phù hợp ngữ cảnh. Hãy dùng cặp mở cửa, xếp đĩa hoặc dán tem để luyện mẫu này.';
                }
            } else if (selectedLabTense === 'ta') {
                taVerbForm = pair.ta.masu.replace('ます', 'ました');
                taContext = `${frame.ta} ${taVerbForm}。`;
                taGrammarExplain = "Người nào đó đã thực hiện xong hành động trong quá khứ.";
            }

            taCard.innerHTML = `
                <div class="lab-card-header is-ta">
                    <span class="lab-role-tag">🔴 THA ĐỘNG TỪ (他動詞 - Tadoushi)</span>
                    <span class="lab-particle-pill">Trợ từ: <strong>を</strong> (hoặc が khi + てある)</span>
                </div>
                <div class="lab-card-body">
                    <div class="lab-word-hero">
                        <span class="lab-kanji">${escapeHtml(pair.ta.kanji)}</span>
                        <span class="lab-kana">【${escapeHtml(pair.ta.kana)}】</span>
                        <button type="button" class="audio-mini-btn" onclick="playVerb('${pair.ta.masu}', this)">🔊</button>
                    </div>
                    <div class="lab-tense-display">
                        <span class="lab-tense-lbl">Dạng đang chọn:</span>
                        <div class="lab-tense-val">${taVerbForm}</div>
                    </div>
                    <div class="lab-sentence-box">
                        <div class="lab-sentence-jp">${escapeHtml(taContext)}</div>
                        <div class="lab-sentence-vi">${escapeHtml(viFor('ta', selectedLabTense))}</div>
                    </div>
                    <div class="lab-explain-box">
                        🎯 <strong>Bản chất:</strong> ${taGrammarExplain}
                    </div>
                </div>
            `;
        }
    }

    // ==========================================
    // 3. TRẮC NGHIỆM PHẢN XẠ 20 CÂU (QUIZ)
    // ==========================================
    function renderQuiz() {
        const quizContainer = document.getElementById('quizContainer');
        if (!quizContainer || !window.TU_THA_QUIZ_DATA) return;

        let totalCorrect = 0;
        let answeredCount = 0;

        quizContainer.innerHTML = window.TU_THA_QUIZ_DATA.map((q, idx) => {
            const userChoice = userQuizAnswers[q.id];
            const hasAnswered = (userChoice !== undefined);
            if (hasAnswered) answeredCount++;

            const isCorrect = (userChoice === q.answer);
            if (isCorrect) totalCorrect++;

            let cardCls = 'quiz-card';
            if (isQuizGraded && hasAnswered) {
                cardCls += isCorrect ? ' is-correct' : ' is-wrong';
            }

            return `
            <div class="${cardCls}" id="quiz-card-${q.id}">
                <div class="quiz-q-header">
                    <span class="quiz-num">Câu ${idx + 1} / ${window.TU_THA_QUIZ_DATA.length}</span>
                    ${isQuizGraded && hasAnswered ? (isCorrect ? '<span class="quiz-status correct">✅ Chính xác</span>' : '<span class="quiz-status wrong">❌ Chưa đúng</span>') : ''}
                </div>
                <div class="quiz-question">${escapeHtml(q.question)}</div>
                <div class="quiz-options-grid">
                    ${q.options.map((opt, optIdx) => {
                        let optCls = 'quiz-opt-btn';
                        if (userChoice === optIdx) optCls += ' selected';
                        if (isQuizGraded) {
                            if (optIdx === q.answer) optCls += ' correct-answer';
                            else if (userChoice === optIdx) optCls += ' wrong-answer';
                        }
                        return `
                        <button type="button" class="${optCls}" onclick="selectQuizAnswer(${q.id}, ${optIdx})" ${isQuizGraded ? 'disabled' : ''}>
                            <span class="opt-key">${['A', 'B', 'C', 'D'][optIdx]}</span>
                            <span class="opt-text">${escapeHtml(opt)}</span>
                        </button>
                        `;
                    }).join('')}
                </div>
                ${isQuizGraded ? `
                <div class="quiz-explain-panel">
                    💡 <strong>Giải thích vì sao:</strong> ${q.explain}
                </div>` : ''}
            </div>
            `;
        }).join('');

        // Cập nhật banner điểm
        const scoreBanner = document.getElementById('quizScoreBanner');
        if (scoreBanner) {
            if (isQuizGraded) {
                const percent = Math.round((totalCorrect / window.TU_THA_QUIZ_DATA.length) * 100);
                scoreBanner.className = 'quiz-score-banner show';
                scoreBanner.innerHTML = `
                    <div style="font-size:1.15rem; font-weight:800; color:var(--dark);">
                        🎯 Kết Quả: <strong>${totalCorrect} / ${window.TU_THA_QUIZ_DATA.length} câu đúng</strong> (${percent}%)
                    </div>
                    <div style="font-size:0.9rem; color:var(--text-muted); margin-top:4px;">
                        ${percent >= 80 ? '🎉 Xuất sắc! Bạn đã làm chủ hoàn toàn các cặp Tự - Tha động từ và trợ từ が / を!' : '💪 Đọc kỹ phần giải thích chi tiết bên dưới mỗi câu để khắc phục các bẫy trợ từ nhé!'}
                    </div>
                `;
            } else {
                scoreBanner.className = 'quiz-score-banner';
                scoreBanner.innerHTML = '';
            }
        }
    }

    // ==========================================
    // 4. CÁC HÀM XỬ LÝ SỰ KIỆN (EVENT HANDLERS)
    // ==========================================
    function selectQuizAnswer(qId, optIdx) {
        if (isQuizGraded) return;
        userQuizAnswers[qId] = optIdx;
        saveCheckpoint();
        renderQuiz();
    }

    function gradeQuiz() {
        isQuizGraded = true;
        saveCheckpoint();
        renderQuiz();
        const banner = document.getElementById('quizScoreBanner');
        if (banner) banner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function resetQuiz() {
        userQuizAnswers = {};
        isQuizGraded = false;
        saveCheckpoint();
        renderQuiz();
    }

    function setCategory(cat, btn) {
        currentCategory = cat;
        document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        renderPairsTable();
    }

    function setHideMode(mode, btn) {
        currentHideMode = mode;
        document.querySelectorAll('.flashcard-toggle-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        renderPairsTable();
    }

    function handleSearch(inp) {
        currentSearchQuery = inp.value;
        renderPairsTable();
    }

    function revealHiddenCell(cell) {
        cell.classList.remove('is-hidden-mask');
        const overlay = cell.querySelector('.mask-overlay');
        if (overlay) overlay.remove();
    }

    function openPairInLab(pairId) {
        selectedLabPairId = pairId;
        switchTab('tab-lab');
        const select = document.getElementById('labPairSelect');
        if (select) select.value = pairId;
        renderLab();
        saveCheckpoint();
        window.scrollTo({ top: 300, behavior: 'smooth' });
    }

    function changeLabPair(selectEl) {
        selectedLabPairId = parseInt(selectEl.value, 10);
        renderLab();
        saveCheckpoint();
    }

    function setLabTense(tense, btn) {
        selectedLabTense = tense;
        document.querySelectorAll('.lab-tense-pill').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        renderLab();
        saveCheckpoint();
    }

    function playVerb(text, btn) {
        if (typeof window.speakJapanese === 'function') {
            window.speakJapanese(text, btn);
        } else {
            console.log("Playing fallback audio:", text);
        }
    }

    function switchTab(tabId) {
        document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));

        const targetBtn = document.querySelector(`.nav-tab-btn[onclick*="${tabId}"]`);
        const targetPanel = document.getElementById(tabId);

        if (targetBtn) targetBtn.classList.add('active');
        if (targetPanel) targetPanel.classList.add('active');

        // Scroll top on mobile
        if (window.innerWidth <= 768) {
            window.scrollTo({ top: 200, behavior: 'smooth' });
        }
    }

    // ==========================================
    // 5. LƯU & PHỤC HỒI CHECKPOINT
    // ==========================================
    function saveCheckpoint() {
        try {
            const state = {
                version: CONTENT_VERSION,
                userQuizAnswers: userQuizAnswers,
                isQuizGraded: isQuizGraded,
                selectedLabPairId: selectedLabPairId,
                selectedLabTense: selectedLabTense
            };
            localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
        } catch (e) {}
    }

    function restoreCheckpoint() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY);
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed.version === CONTENT_VERSION && parsed.userQuizAnswers && typeof parsed.userQuizAnswers === 'object') {
                    for (const q of window.TU_THA_QUIZ_DATA) {
                        const answer = parsed.userQuizAnswers[q.id];
                        if (Number.isInteger(answer) && answer >= 0 && answer < q.options.length) userQuizAnswers[q.id] = answer;
                    }
                    isQuizGraded = parsed.isQuizGraded === true;
                }
                if (window.TU_THA_PAIRS_DATA.some(p => p.id === parsed.selectedLabPairId)) selectedLabPairId = parsed.selectedLabPairId;
                if (['masu', 'te_iru', 'te_aru', 'ta'].includes(parsed.selectedLabTense)) selectedLabTense = parsed.selectedLabTense;
            }
        } catch (e) {}
    }

    function bindEvents() {
        const searchInp = document.getElementById('searchPairInput');
        if (searchInp) {
            searchInp.addEventListener('input', function () {
                handleSearch(this);
            });
        }
    }

    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    // Expose functions to global
    window.switchTab = switchTab;
    window.setCategory = setCategory;
    window.setHideMode = setHideMode;
    window.revealHiddenCell = revealHiddenCell;
    window.openPairInLab = openPairInLab;
    window.changeLabPair = changeLabPair;
    window.setLabTense = setLabTense;
    window.playVerb = playVerb;
    window.selectQuizAnswer = selectQuizAnswer;
    window.gradeQuiz = gradeQuiz;
    window.resetQuiz = resetQuiz;

    document.addEventListener('DOMContentLoaded', init);
})();
