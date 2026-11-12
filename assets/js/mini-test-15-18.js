/* Modular Quiz & Exam Coordinator for On_Tap_Mini_Test_A2_15_18 */
// DỮ LIỆU TỪ assets/data/mini_15_18_data.js
const {
    VOCAB_DATA,
    KANJI_DATA,
    EXAMS_LIST,
    KANJI_15_18_DATA,
    KANJI_11_14_DATA,
    SENTENCE_TYPING_DATA
} = window.MINI_15_18_DATA;
const MINI15_18_CP_KEY = 'marugoto_mini15_18_cp_v2';
window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;

// TRẠNG THÁI TOÀN CỤC
let currentTab = 'tab-theory';
let currentVocabFilter = 'all';
let isMeaningHidden = false;

// Quản lý 5 Mã Đề & Trạng thái riêng từng Mã Đề
let currentExamId = EXAMS_LIST[0].id;
const examStates = {};

let P1_DATA = EXAMS_LIST[0].p1;
let P2_DATA = EXAMS_LIST[0].p2;
let P3_DATA = EXAMS_LIST[0].p3;
let P4_DATA = EXAMS_LIST[0].p4;
let P5_DATA = EXAMS_LIST[0].p5;
let P6_DATA = EXAMS_LIST[0].p6;
let scoreState = { p1: {}, p2: {}, p3: {}, p4: {}, p5: {}, p6: {} };
let arrangeState = {};
let selectedA = null;
let matchedPairs = {};

function getExamById(examId) {
    return EXAMS_LIST.find(e => e.id === examId) || EXAMS_LIST[0];
}

function createEmptyExamState(exam) {
    return {
        scoreState: { p1: {}, p2: {}, p3: {}, p4: {}, p5: {}, p6: {} },
        p1Chosen: {},
        arrangeState: {},
        arrangeChecked: {},
        p3Answers: {},
        p4Order: exam.p4.slice().sort(() => Math.random() - 0.5),
        matchedPairs: {},
        p5Chosen: {},
        p6Draft: {},
        p6ModelOpen: {},
        p6StatusPts: {}
    };
}

function getActiveExamState() {
    const exam = getExamById(currentExamId);
    if (!examStates[currentExamId]) {
        examStates[currentExamId] = createEmptyExamState(exam);
    }
    return examStates[currentExamId];
}

function bindActiveExamAliases() {
    const exam = getExamById(currentExamId);
    const st = getActiveExamState();
    P1_DATA = exam.p1;
    P2_DATA = exam.p2;
    P3_DATA = exam.p3;
    P4_DATA = exam.p4;
    P5_DATA = exam.p5;
    P6_DATA = exam.p6;
    scoreState = st.scoreState;
    arrangeState = st.arrangeState;
    matchedPairs = st.matchedPairs;
    selectedA = null;
}

function computeExamScore(examId) {
    const st = examStates[examId];
    if (!st) return 0;
    let total = 0;
    ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'].forEach(p => {
        Object.values(st.scoreState[p]).forEach(val => {
            total += Number(val) || 0;
        });
    });
    return Math.round(total * 10) / 10;
}

function hasExamProgress(examId) {
    const st = examStates[examId];
    if (!st) return false;
    return (
        Object.keys(st.p1Chosen).length > 0 ||
        Object.keys(st.arrangeChecked).length > 0 ||
        Object.keys(st.p3Answers).some(k => st.p3Answers[k] && st.p3Answers[k].locked) ||
        Object.keys(st.matchedPairs).length > 0 ||
        Object.keys(st.p5Chosen).length > 0 ||
        Object.keys(st.p6StatusPts).length > 0
    );
}

function saveCurrentExamDrafts() {
    const st = examStates[currentExamId];
    if (!st) return;
    P3_DATA.forEach(item => {
        const inp = document.getElementById(`p3_input_${item.id}`);
        if (inp) {
            const prev = st.p3Answers[item.id] || { value: '', locked: false, isCorrect: false };
            st.p3Answers[item.id] = { ...prev, value: inp.value };
        }
    });
    P6_DATA.forEach(item => {
        const txt = document.getElementById(`p6_txt_${item.id}`);
        if (txt) st.p6Draft[item.id] = txt.value;
    });
}

function updateExamHeaderBanner() {
    const exam = getExamById(currentExamId);
    const titleEl = document.getElementById('examTimerHeaderTitle');
    const metaEl = document.getElementById('examTimerHeaderMeta');
    const subEl = document.getElementById('activeExamSubtitle');
    if (titleEl) titleEl.innerText = exam.fullTitle;
    if (metaEl) metaEl.innerText = `${exam.badge} • 6 Dạng Bài Chuẩn Sư Phạm • 32 Câu Hỏi`;
    if (subEl) subEl.innerText = exam.subtitle;
}

function renderExamSwitcher() {
    const grid = document.getElementById('examSwitcherGrid');
    if (grid) {
        grid.innerHTML = EXAMS_LIST.map(ex => {
            const sc = computeExamScore(ex.id);
            const touched = hasExamProgress(ex.id);
            const activeCls = ex.id === currentExamId ? ' active' : '';
            const scoreCls = (touched || sc > 0) ? ' has-score' : '';
            const scoreText = (touched || sc > 0) ? `${sc}/100đ` : 'Mới';
            return `
                <button type="button" class="exam-switch-btn${activeCls}" id="examSwitch_${ex.id}" onclick="switchExamSet('${ex.id}')">
                    <div class="exam-switch-top">
                        <span class="exam-switch-code">Mã Đề ${ex.code}</span>
                        <span class="exam-switch-score${scoreCls}">${scoreText}</span>
                    </div>
                    <span class="exam-switch-name">${ex.shortTitle}</span>
                </button>
            `;
        }).join('');
    }
    const summaryEl = document.getElementById('overallProgressSummary');
    if (summaryEl) {
        const startedCount = EXAMS_LIST.filter(ex => hasExamProgress(ex.id)).length;
        summaryEl.innerText = `Đang mở: Đề ${currentExamId} • Đã làm: ${startedCount} / ${EXAMS_LIST.length} mã đề`;
    }
}

function switchExamSet(examId) {
    if (examId === currentExamId) return;
    saveCurrentExamDrafts();
    currentExamId = examId;
    bindActiveExamAliases();
    updateExamHeaderBanner();
    renderPart1();
    renderPart2();
    renderPart3();
    renderPart4();
    renderPart5();
    renderPart6();
    updateTotalScore();
    renderExamSwitcher();
    saveMini15_18Checkpoint();
    showToast(`Đã chuyển sang Mã Đề ${examId} (${getExamById(examId).shortTitle})!`);
}

// Chuyển tab chính
function switchMainTab(tabId, skipSave) {
    currentTab = tabId;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

    const activeBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => (b.getAttribute('onclick') || '').includes(tabId));
    if (activeBtn) activeBtn.classList.add('active');

    const targetPanel = document.getElementById(tabId);
    if (targetPanel) targetPanel.classList.add('active');

    if (tabId === 'tab-typing') {
        initTypingPractice();
    }
    if (!skipSave) {
        const curHash = (window.location.hash || '').toLowerCase();
        if (tabId !== 'tab-typing' && (curHash === '#typing' || curHash === '#tab-typing') && window.history && window.history.replaceState) {
            window.history.replaceState(null, '', window.location.pathname + window.location.search);
        }
        saveMini15_18Checkpoint();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// Phát âm TTS
function speakText(text) {
    if (window.AudioEngine && typeof window.AudioEngine.speak === 'function') {
        window.AudioEngine.speak(text);
    } else if ('speechSynthesis' in window) {
        const u = new SpeechSynthesisUtterance(text);
        u.lang = 'ja-JP';
        u.rate = 0.95;
        window.speechSynthesis.speak(u);
    }
}

// Toast
function showToast(msg) {
    const t = document.getElementById('toast');
    if (!t) return;
    t.innerText = msg;
    t.classList.add('show');
    setTimeout(() => {
        t.classList.remove('show');
    }, 2200);
}

// ==========================================
// RENDER TỪ VỰNG
// ==========================================
function renderVocab(list) {
    const c = document.getElementById('vocabGridContainer');
    if (!c) return;
    c.innerHTML = list.map(item => `
        <div class="vocab-card">
            <div>
                <div class="vocab-card-header">
                    <div>
                        <div class="vocab-jp jp-text">${item.jp}</div>
                        <div class="vocab-kana jp-text">${item.kana || ''} ${item.hv ? `<span style="color:#64748b; font-size:0.8rem;">${item.hv}</span>` : ''}</div>
                    </div>
                    <button type="button" class="audio-btn" onclick="speakText('${item.jp}')" title="Phát âm">🔊</button>
                </div>
                <div class="vocab-badge">${item.l || 'A2'} • #${item.num || ''}</div>
            </div>
            <div class="vocab-vi ${isMeaningHidden ? 'hidden-meaning' : ''}">${item.vi}</div>
        </div>
    `).join('');
}

function filterVocab(lesson) {
    currentVocabFilter = lesson;
    document.querySelectorAll('#vocabFilterGroup .v-filter-btn').forEach(b => b.classList.remove('active'));
    const activeBtn = Array.from(document.querySelectorAll('#vocabFilterGroup .v-filter-btn')).find(b => b.getAttribute('onclick').includes(lesson));
    if (activeBtn) activeBtn.classList.add('active');

    const filtered = lesson === 'all' ? VOCAB_DATA : VOCAB_DATA.filter(w => w.l === lesson);
    renderVocab(filtered);
}

function handleVocabSearch() {
    const q = (document.getElementById('vocabSearchInput').value || '').toLowerCase().trim();
    let base = currentVocabFilter === 'all' ? VOCAB_DATA : VOCAB_DATA.filter(w => w.l === currentVocabFilter);
    if (q) {
        base = base.filter(w => 
            (w.jp && w.jp.toLowerCase().includes(q)) ||
            (w.kana && w.kana.toLowerCase().includes(q)) ||
            (w.vi && w.vi.toLowerCase().includes(q)) ||
            (w.romaji && w.romaji.toLowerCase().includes(q))
        );
    }
    renderVocab(base);
}

function toggleHideMeaning() {
    isMeaningHidden = !isMeaningHidden;
    document.querySelectorAll('.vocab-vi').forEach(el => {
        if (isMeaningHidden) el.classList.add('hidden-meaning');
        else el.classList.remove('hidden-meaning');
    });
    showToast(isMeaningHidden ? 'Đã ẩn nghĩa tiếng Việt (rê chuột để xem)' : 'Đã hiện nghĩa tiếng Việt');
}

function copyVocabQuizletFormat() {
    let targetList = currentVocabFilter === 'all' ? VOCAB_DATA : VOCAB_DATA.filter(w => w.l === currentVocabFilter);
    const lines = targetList.map(w => `${w.jp}\t${w.vi} (${w.kana || ''})`).join('\n');
    navigator.clipboard.writeText(lines).then(() => {
        showToast(`Đã copy ${targetList.length} từ vựng theo chuẩn Quizlet Tab!`);
    }).catch(() => {
        showToast('Không thể sao chép, vui lòng thử lại');
    });
}

// ==========================================
// RENDER KANJI
// ==========================================
function renderKanji(list) {
    const c = document.getElementById('kanjiGridContainer');
    if (!c) return;
    c.innerHTML = list.map(k => `
        <div class="kanji-card">
            <div class="kanji-main">
                <div class="kanji-char jp-text">${k.char}</div>
                <div class="kanji-info">
                    <div class="kanji-hv">${k.hv} <span style="font-size:0.8rem; color:#64748b;">(${k.strokes} nét)</span></div>
                    <div class="kanji-meaning">${k.meaning}</div>
                </div>
                <button type="button" class="audio-btn" onclick="speakText('${k.hiragana || k.char}')" title="Phát âm">🔊</button>
            </div>
            <div class="kanji-readings">
                <div><strong>Âm Kun:</strong> <span class="jp-text" style="color:var(--primary); font-weight:700;">${k.kun || '—'}</span></div>
                <div><strong>Âm On:</strong> <span class="jp-text" style="color:#d97706; font-weight:700;">${k.on || '—'}</span></div>
            </div>
            ${k.mnemonic ? `<div class="kanji-mnemonic">💡 <strong>Mẹo nhớ:</strong> ${k.mnemonic}</div>` : ''}
        </div>
    `).join('');
}

function copyKanjiQuizletTabFormat() {
    const lines = KANJI_DATA.map(k => `${k.char}\t${k.hv} - ${k.meaning} [${k.hiragana || ''}]`).join('\n');
    navigator.clipboard.writeText(lines).then(() => {
        showToast(`Đã copy ${KANJI_DATA.length} chữ Hán theo chuẩn Quizlet Tab!`);
    }).catch(() => {
        showToast('Không thể sao chép, vui lòng thử lại');
    });
}

// ==========================================
// RENDER ĐỀ THI (PARTS 1 -> 6)
// ==========================================
function renderPart1() {
    const c = document.getElementById('part1Container');
    if (!c) return;
    const st = getActiveExamState();
    c.innerHTML = P1_DATA.map(item => {
        const chosenIdx = st.p1Chosen[item.id];
        const answered = chosenIdx !== undefined;
        return `
            <div class="question-item" id="p1_item_${item.id}">
                <div class="q-title">
                    <span class="q-badge">Câu ${item.id}</span>
                    <span class="jp-text" style="font-size:1.1rem;">${item.q}</span>
                </div>
                <div class="options-list">
                    ${item.options.map((opt, oIdx) => {
                        let cls = 'opt-btn jp-text';
                        if (answered) {
                            if (oIdx === item.correct) cls += ' is-correct';
                            else if (oIdx === chosenIdx) cls += ' is-wrong';
                        }
                        return `
                            <button type="button" class="${cls}" id="p1_opt_${item.id}_${oIdx}" onclick="selectPart1Answer(${item.id}, ${oIdx})" ${answered ? 'disabled' : ''}>
                                ${['A', 'B', 'C', 'D'][oIdx]}. ${opt}
                            </button>
                        `;
                    }).join('')}
                </div>
                <div class="explain-box" id="p1_exp_${item.id}" style="display:${answered ? 'block' : 'none'};">
                    <strong>💡 Giải thích:</strong> ${item.explain}
                </div>
            </div>
        `;
    }).join('');
}

function selectPart1Answer(qId, oIdx) {
    const item = P1_DATA.find(q => q.id === qId);
    if (!item) return;
    const st = getActiveExamState();
    st.p1Chosen[qId] = oIdx;

    item.options.forEach((_, idx) => {
        const btn = document.getElementById(`p1_opt_${qId}_${idx}`);
        if (btn) {
            btn.classList.remove('is-correct', 'is-wrong');
            btn.disabled = true;
        }
    });

    const chosenBtn = document.getElementById(`p1_opt_${qId}_${oIdx}`);
    const correctBtn = document.getElementById(`p1_opt_${qId}_${item.correct}`);

    if (oIdx === item.correct) {
        if (chosenBtn) chosenBtn.classList.add('is-correct');
        scoreState.p1[qId] = 2.5;
    } else {
        if (chosenBtn) chosenBtn.classList.add('is-wrong');
        if (correctBtn) correctBtn.classList.add('is-correct');
        scoreState.p1[qId] = 0;
    }

    const exp = document.getElementById(`p1_exp_${qId}`);
    if (exp) exp.style.display = 'block';

    updateTotalScore();
}

// PART 2: ARRANGE
function renderPart2() {
    const c = document.getElementById('part2Container');
    if (!c) return;
    const st = getActiveExamState();
    c.innerHTML = P2_DATA.map(item => {
        if (!st.arrangeState[item.id]) {
            st.arrangeState[item.id] = {
                placed: [],
                available: item.chips.map((chip, idx) => ({ text: chip, origIdx: idx }))
            };
        }
        const qSt = st.arrangeState[item.id];
        const chk = st.arrangeChecked[item.id];
        const statusHtml = chk
            ? (chk.ok
                ? '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>'
                : '<span style="color:var(--accent);">✗ Chưa chính xác (0 điểm)</span>')
            : '';
        return `
            <div class="question-item" id="p2_item_${item.id}">
                <div class="q-title">
                    <span class="q-badge">Câu ${item.id}</span>
                    <span>${item.prompt}</span>
                </div>
                <div style="font-size:1.1rem; font-weight:700; margin: 8px 0; color:var(--gray-900);">
                    <span class="jp-text">${item.pre}</span>
                    <span style="color:var(--primary); font-weight:800;"> [ 1 ] [ 2 ] [ ★ ] [ 4 ] </span>
                    <span class="jp-text">${item.post}</span>
                </div>
                <div class="arrange-slot-box" id="p2_slot_${item.id}">
                    ${qSt.placed.length === 0
                        ? '<span style="color:var(--gray-400); font-size:0.9rem;">(Click các mảnh ghép bên dưới để sắp xếp vào đây)</span>'
                        : qSt.placed.map((ch, pos) => `
                            <button type="button" class="chip-btn in-slot jp-text" onclick="removeArrangeChip(${item.id}, ${ch.origIdx})" title="Click để gỡ ra">
                                ${pos === 2 ? '★ ' : ''}${ch.text}
                            </button>
                        `).join('')}
                </div>
                <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:12px;" id="p2_pool_${item.id}">
                    ${qSt.available.map(ch => `
                        <button type="button" class="chip-btn jp-text" id="p2_chip_${item.id}_${ch.origIdx}" onclick="clickArrangeChip(${item.id}, ${ch.origIdx})">${ch.text}</button>
                    `).join('')}
                </div>
                <div style="display:flex; gap:10px; align-items:center;">
                    <button type="button" class="btn-primary" onclick="checkArrangeAnswer(${item.id})" style="padding:6px 14px; font-size:0.88rem;">Kiểm Tra</button>
                    <button type="button" class="btn-primary" onclick="resetSingleArrange(${item.id})" style="padding:6px 14px; font-size:0.88rem; background:var(--gray-600);">Đặt Lại</button>
                    <span id="p2_status_${item.id}" style="font-weight:700; font-size:0.92rem;">${statusHtml}</span>
                </div>
                <div class="explain-box" id="p2_exp_${item.id}" style="display:${chk ? 'block' : 'none'};">
                    <strong>💡 Câu hoàn chỉnh:</strong> <span class="jp-text">${item.fullSentence}</span><br>
                    <strong>Giải thích:</strong> ${item.explain}
                </div>
            </div>
        `;
    }).join('');
}

function clickArrangeChip(qId, origIdx) {
    const st = arrangeState[qId];
    if (!st) return;
    const chipData = st.available.find(c => c.origIdx === origIdx);
    if (!chipData) return;

    st.available = st.available.filter(c => c.origIdx !== origIdx);
    st.placed.push(chipData);
    updateArrangeUI(qId);
    saveMini15_18Checkpoint();
}

function removeArrangeChip(qId, origIdx) {
    const st = arrangeState[qId];
    if (!st) return;
    const chipData = st.placed.find(c => c.origIdx === origIdx);
    if (!chipData) return;

    st.placed = st.placed.filter(c => c.origIdx !== origIdx);
    st.available.push(chipData);
    updateArrangeUI(qId);
    saveMini15_18Checkpoint();
}

function updateArrangeUI(qId) {
    const st = arrangeState[qId];
    const slotBox = document.getElementById(`p2_slot_${qId}`);
    const poolBox = document.getElementById(`p2_pool_${qId}`);

    if (st.placed.length === 0) {
        slotBox.innerHTML = '<span style="color:var(--gray-400); font-size:0.9rem;">(Click các mảnh ghép bên dưới để sắp xếp vào đây)</span>';
    } else {
        slotBox.innerHTML = st.placed.map((c, pos) => `
            <button type="button" class="chip-btn in-slot jp-text" onclick="removeArrangeChip(${qId}, ${c.origIdx})" title="Click để gỡ ra">
                ${pos === 2 ? '★ ' : ''}${c.text}
            </button>
        `).join('');
    }

    poolBox.innerHTML = st.available.map(c => `
        <button type="button" class="chip-btn jp-text" id="p2_chip_${qId}_${c.origIdx}" onclick="clickArrangeChip(${qId}, ${c.origIdx})">${c.text}</button>
    `).join('');
}

function resetSingleArrange(qId) {
    const item = P2_DATA.find(q => q.id === qId);
    if (!item) return;
    const exSt = getActiveExamState();
    arrangeState[qId] = {
        placed: [],
        available: item.chips.map((chip, idx) => ({ text: chip, origIdx: idx }))
    };
    delete exSt.arrangeChecked[qId];
    delete scoreState.p2[qId];
    updateArrangeUI(qId);
    document.getElementById(`p2_status_${qId}`).innerText = '';
    document.getElementById(`p2_exp_${qId}`).style.display = 'none';
    updateTotalScore();
}

function checkArrangeAnswer(qId) {
    const item = P2_DATA.find(q => q.id === qId);
    const st = arrangeState[qId];
    const exSt = getActiveExamState();
    const statusEl = document.getElementById(`p2_status_${qId}`);
    const expEl = document.getElementById(`p2_exp_${qId}`);

    if (st.placed.length < 4) {
        statusEl.innerHTML = '<span style="color:var(--warning);">⚠️ Vui lòng xếp đủ cả 4 mảnh ghép!</span>';
        return;
    }

    const isStarCorrect = (st.placed[item.starIndex] && st.placed[item.starIndex].origIdx === item.correctOrder[item.starIndex]);
    const isFullCorrect = st.placed.every((c, idx) => c.origIdx === item.correctOrder[idx]);

    if (isFullCorrect || isStarCorrect) {
        statusEl.innerHTML = '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>';
        scoreState.p2[qId] = 3.0;
        exSt.arrangeChecked[qId] = { ok: true };
    } else {
        statusEl.innerHTML = '<span style="color:var(--accent);">✗ Chưa chính xác (0 điểm)</span>';
        scoreState.p2[qId] = 0;
        exSt.arrangeChecked[qId] = { ok: false };
    }

    expEl.style.display = 'block';
    updateTotalScore();
}

// PART 3: CONJUGATION
function renderPart3() {
    const c = document.getElementById('part3Container');
    if (!c) return;
    const st = getActiveExamState();
    c.innerHTML = P3_DATA.map(item => {
        const ans = st.p3Answers[item.id] || { value: '', locked: false, isCorrect: false };
        const inputCls = ans.locked
            ? `conjugate-input jp-text ${ans.isCorrect ? 'is-correct' : 'is-wrong'}`
            : 'conjugate-input jp-text';
        const statusHtml = ans.locked
            ? (ans.isCorrect
                ? '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>'
                : '<span style="color:var(--accent);">✗ Chưa đúng!</span>')
            : '';
        return `
            <div class="question-item" id="p3_item_${item.id}">
                <div class="q-title">
                    <span class="q-badge">Câu ${item.id}</span>
                    <span class="jp-text" style="font-size:1.05rem;">${item.sentence}</span>
                </div>
                <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin:12px 0;">
                    <input type="text" class="${inputCls}" id="p3_input_${item.id}" placeholder="Nhập đáp án..." ${ans.locked ? 'disabled' : ''}>
                    <button type="button" class="btn-primary" onclick="checkConjugateAnswer(${item.id})" style="padding:7px 16px; font-size:0.9rem;">Kiểm Tra</button>
                    <span id="p3_status_${item.id}" style="font-weight:700; font-size:0.92rem;">${statusHtml}</span>
                </div>
                <div class="explain-box" id="p3_exp_${item.id}" style="display:${ans.locked ? 'block' : 'none'};">
                    <strong>💡 Đáp án đúng:</strong> <span class="jp-text" style="color:var(--success); font-weight:800;">${item.displayAnswer}</span><br>
                    <strong>Giải thích:</strong> ${item.explain}
                </div>
            </div>
        `;
    }).join('');
    P3_DATA.forEach(item => {
        const inp = document.getElementById(`p3_input_${item.id}`);
        const ans = st.p3Answers[item.id];
        if (inp && ans && ans.value) inp.value = ans.value;
    });
}

function checkConjugateAnswer(qId) {
    const item = P3_DATA.find(q => q.id === qId);
    const st = getActiveExamState();
    const input = document.getElementById(`p3_input_${qId}`);
    const statusEl = document.getElementById(`p3_status_${qId}`);
    const expEl = document.getElementById(`p3_exp_${qId}`);
    const val = (input.value || '').trim().toLowerCase();

    if (!val) {
        statusEl.innerHTML = '<span style="color:var(--warning);">Vui lòng nhập đáp án!</span>';
        return;
    }

    const isOk = item.accepted.some(acc => acc.toLowerCase() === val);
    input.disabled = true;
    st.p3Answers[qId] = { value: input.value.trim(), locked: true, isCorrect: isOk };

    if (isOk) {
        input.classList.add('is-correct');
        statusEl.innerHTML = '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>';
        scoreState.p3[qId] = 3.0;
    } else {
        input.classList.add('is-wrong');
        statusEl.innerHTML = '<span style="color:var(--accent);">✗ Chưa đúng!</span>';
        scoreState.p3[qId] = 0;
    }

    expEl.style.display = 'block';
    updateTotalScore();
}

// PART 4: MATCHING
function renderPart4() {
    const c = document.getElementById('part4Container');
    if (!c) return;
    const st = getActiveExamState();
    const matchedBSet = new Set(Object.values(matchedPairs));
    const allMatched = Object.keys(matchedPairs).length === P4_DATA.length;
    c.innerHTML = `
        <div class="question-item">
            <div style="font-size:0.95rem; color:var(--gray-600); margin-bottom:14px;">
                👉 <em>Click chọn một câu ở Cột A (Tình huống), sau đó click chọn câu đối đáp tương ứng ở Cột B.</em>
            </div>
            <div class="matching-grid">
                <div id="colAContainer">
                    ${P4_DATA.map(item => `
                        <div class="match-card jp-text${matchedPairs[item.id] ? ' matched' : ''}" id="match_A_${item.id}" onclick="clickMatchA(${item.id})">
                            <strong>A${item.id - 20}:</strong> ${item.promptA}
                        </div>
                    `).join('')}
                </div>
                <div id="colBContainer">
                    ${st.p4Order.map(item => `
                        <div class="match-card jp-text${matchedBSet.has(item.correctBId) ? ' matched' : ''}" id="match_B_${item.correctBId}" onclick="clickMatchB('${item.correctBId}')">
                            <strong>${item.correctBId}:</strong> ${item.promptB}
                        </div>
                    `).join('')}
                </div>
            </div>
            <div style="display:flex; gap:12px; align-items:center;">
                <button type="button" class="btn-primary" onclick="resetMatching()" style="background:var(--gray-600); padding:6px 14px; font-size:0.88rem;">Đặt Lại Cột Nối</button>
                <span id="matchScoreText" style="font-weight:700;">${allMatched ? '<span style="color:var(--success);">🎉 Đã nối chuẩn xác toàn bộ 4 cặp câu! (+10 Điểm)</span>' : ''}</span>
            </div>
            <div class="explain-box" id="p4_exp_all" style="display:${allMatched ? 'block' : 'none'};">
                <strong>💡 Phân tích các cặp hội thoại chuẩn:</strong><br>
                ${P4_DATA.map(p => `• <strong>${p.correctBId}</strong>: ${p.explain}`).join('<br>')}
            </div>
        </div>
    `;
}

function clickMatchA(id) {
    if (matchedPairs[id]) return;
    document.querySelectorAll('#colAContainer .match-card').forEach(el => el.classList.remove('selected'));
    selectedA = id;
    const el = document.getElementById(`match_A_${id}`);
    if (el) el.classList.add('selected');
}

function clickMatchB(bId) {
    if (!selectedA) {
        showToast('Vui lòng chọn 1 câu ở Cột A trước!');
        return;
    }
    const item = P4_DATA.find(q => q.id === selectedA);
    if (!item) return;

    const elA = document.getElementById(`match_A_${selectedA}`);
    const elB = document.getElementById(`match_B_${bId}`);

    if (item.correctBId === bId) {
        elA.classList.remove('selected');
        elA.classList.add('matched');
        elB.classList.add('matched');
        matchedPairs[selectedA] = bId;
        scoreState.p4[selectedA] = 2.5;
        showToast('✓ Nối thành công cặp câu!');
    } else {
        elA.classList.remove('selected');
        showToast('✗ Chưa đúng cặp hội thoại, hãy thử lại!');
    }
    selectedA = null;

    if (Object.keys(matchedPairs).length === P4_DATA.length) {
        document.getElementById('p4_exp_all').style.display = 'block';
        document.getElementById('matchScoreText').innerHTML = '<span style="color:var(--success);">🎉 Đã nối chuẩn xác toàn bộ 4 cặp câu! (+10 Điểm)</span>';
    }
    updateTotalScore();
}

function resetMatching() {
    const st = getActiveExamState();
    selectedA = null;
    st.matchedPairs = {};
    matchedPairs = st.matchedPairs;
    P4_DATA.forEach(q => {
        scoreState.p4[q.id] = 0;
    });
    renderPart4();
    updateTotalScore();
}

// PART 5: READING
function renderPart5() {
    const c = document.getElementById('part5Container');
    if (!c) return;
    const st = getActiveExamState();
    c.innerHTML = P5_DATA.map(passage => `
        <div class="question-item">
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary); margin-bottom:12px;">${passage.title}</h3>
            <div class="reading-box jp-text">${passage.text}</div>
            <div>
                ${passage.questions.map(q => {
                    const chosenIdx = st.p5Chosen[q.id];
                    const answered = chosenIdx !== undefined;
                    return `
                        <div style="margin-bottom:18px; padding-bottom:14px; border-bottom:1px dashed var(--gray-200);">
                            <div class="q-title">
                                <span class="q-badge">Câu ${q.id}</span>
                                <span class="jp-text">${q.q}</span>
                            </div>
                            <div class="options-list">
                                ${q.options.map((opt, oIdx) => {
                                    let cls = 'opt-btn jp-text';
                                    if (answered) {
                                        if (oIdx === q.correct) cls += ' is-correct';
                                        else if (oIdx === chosenIdx) cls += ' is-wrong';
                                    }
                                    return `
                                        <button type="button" class="${cls}" id="p5_opt_${q.id}_${oIdx}" onclick="selectPart5Answer(${q.id}, ${oIdx}, ${passage.passageId})" ${answered ? 'disabled' : ''}>
                                            ${['A', 'B', 'C', 'D'][oIdx]}. ${opt}
                                        </button>
                                    `;
                                }).join('')}
                            </div>
                            <div class="explain-box" id="p5_exp_${q.id}" style="display:${answered ? 'block' : 'none'};">
                                <strong>💡 Giải thích:</strong> ${q.explain}
                            </div>
                        </div>
                    `;
                }).join('')}
            </div>
        </div>
    `).join('');
}

function selectPart5Answer(qId, oIdx, pId) {
    const passage = P5_DATA.find(p => p.passageId === pId);
    if (!passage) return;
    const item = passage.questions.find(q => q.id === qId);
    if (!item) return;
    const st = getActiveExamState();
    st.p5Chosen[qId] = oIdx;

    item.options.forEach((_, idx) => {
        const btn = document.getElementById(`p5_opt_${qId}_${idx}`);
        if (btn) {
            btn.classList.remove('is-correct', 'is-wrong');
            btn.disabled = true;
        }
    });

    const chosenBtn = document.getElementById(`p5_opt_${qId}_${oIdx}`);
    const correctBtn = document.getElementById(`p5_opt_${qId}_${item.correct}`);

    if (oIdx === item.correct) {
        if (chosenBtn) chosenBtn.classList.add('is-correct');
        scoreState.p5[qId] = 5.0;
    } else {
        if (chosenBtn) chosenBtn.classList.add('is-wrong');
        if (correctBtn) correctBtn.classList.add('is-correct');
        scoreState.p5[qId] = 0;
    }

    const exp = document.getElementById(`p5_exp_${qId}`);
    if (exp) exp.style.display = 'block';

    updateTotalScore();
}

// PART 6: TRANSLATION
function renderPart6() {
    const c = document.getElementById('part6Container');
    if (!c) return;
    const st = getActiveExamState();
    c.innerHTML = P6_DATA.map(item => {
        const pts = st.p6StatusPts[item.id];
        const modelOpen = Boolean(st.p6ModelOpen[item.id]);
        const statusHtml = pts !== undefined
            ? (pts > 0
                ? `<span style="color:var(--success);">✓ Đã cộng ${pts} điểm</span>`
                : `<span style="color:var(--accent);">✗ 0 điểm</span>`)
            : '';
        return `
            <div class="question-item" id="p6_item_${item.id}">
                <div class="q-title">
                    <span class="q-badge">Câu ${item.id} • ${item.category}</span>
                    <span>${item.vi}</span>
                </div>
                <div style="font-size:0.88rem; color:#475569; margin-bottom:10px;">
                    💡 <strong>Từ khóa gợi ý:</strong> ${item.hint}
                </div>
                <textarea class="conjugate-input jp-text" id="p6_txt_${item.id}" rows="2" style="width:100%; font-size:1rem; margin-bottom:10px;" placeholder="Gõ câu dịch tiếng Nhật của bạn vào đây..."></textarea>
                <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
                    <button type="button" class="btn-primary" onclick="toggleTranslationModel(${item.id})" style="padding:6px 14px; font-size:0.88rem;">👁️ Xem Đáp Án Mẫu</button>
                    <button type="button" class="btn-primary" onclick="selfGradeTranslation(${item.id}, 3.75)" style="background:var(--success); padding:6px 14px; font-size:0.88rem;">✓ Tự Chấm Đúng (+3.75đ)</button>
                    <button type="button" class="btn-primary" onclick="selfGradeTranslation(${item.id}, 0)" style="background:var(--gray-600); padding:6px 14px; font-size:0.88rem;">✗ Tự Chấm Sai (0đ)</button>
                    <span id="p6_status_${item.id}" style="font-weight:700;">${statusHtml}</span>
                </div>
                <div class="explain-box" id="p6_model_${item.id}" style="display:${modelOpen ? 'block' : 'none'};">
                    <div style="font-size:1.1rem; font-weight:800; color:var(--primary); margin-bottom:6px;" class="jp-text">
                        ${item.modelSentence}
                        <button type="button" class="audio-btn" onclick="speakP6Model(${item.id})" style="vertical-align:middle; margin-left:6px;">🔊</button>
                    </div>
                    <div style="color:var(--gray-600); font-size:0.9rem; margin-bottom:8px;">${item.modelKana}</div>
                    <strong>Phân tích ngữ pháp:</strong>
                    <ul style="margin-left:20px; font-size:0.92rem; color:var(--gray-700);">
                        ${item.breakdown.map(b => `<li><strong>${b.part}</strong>: ${b.role}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
    }).join('');
    P6_DATA.forEach(item => {
        const txt = document.getElementById(`p6_txt_${item.id}`);
        if (txt && st.p6Draft[item.id]) txt.value = st.p6Draft[item.id];
    });
}

function speakP6Model(qId) {
    const item = P6_DATA.find(q => q.id === qId);
    if (item) speakText(item.modelSentence);
}

function toggleTranslationModel(qId) {
    const el = document.getElementById(`p6_model_${qId}`);
    const st = getActiveExamState();
    if (el) {
        const nextOpen = el.style.display !== 'block';
        el.style.display = nextOpen ? 'block' : 'none';
        st.p6ModelOpen[qId] = nextOpen;
        saveMini15_18Checkpoint();
    }
}

function selfGradeTranslation(qId, pts) {
    const st = getActiveExamState();
    scoreState.p6[qId] = pts;
    st.p6StatusPts[qId] = pts;
    st.p6ModelOpen[qId] = true;
    const statusEl = document.getElementById(`p6_status_${qId}`);
    if (pts > 0) {
        statusEl.innerHTML = `<span style="color:var(--success);">✓ Đã cộng ${pts} điểm</span>`;
    } else {
        statusEl.innerHTML = `<span style="color:var(--accent);">✗ 0 điểm</span>`;
    }
    document.getElementById(`p6_model_${qId}`).style.display = 'block';
    updateTotalScore();
}

// TOTAL SCORE
function updateTotalScore() {
    const total = computeExamScore(currentExamId);
    const disp = document.getElementById('totalScoreText');
    if (disp) {
        disp.innerText = `${total} / 100 Điểm`;
    }
    renderExamSwitcher();
    if (typeof saveMini15_18Checkpoint === 'function') saveMini15_18Checkpoint();
}

function resetAllExam() {
    if (!confirm(`Bạn có chắc chắn muốn làm lại toàn bộ Mã Đề ${currentExamId} không?`)) return;
    examStates[currentExamId] = createEmptyExamState(getExamById(currentExamId));
    bindActiveExamAliases();
    renderPart1();
    renderPart2();
    renderPart3();
    renderPart4();
    renderPart5();
    renderPart6();
    updateTotalScore();
    saveMini15_18Checkpoint();
    showToast(`Đã đặt lại toàn bộ Mã Đề ${currentExamId}!`);
}


// ==========================================
// CHECKPOINT LƯU / KHÔI PHỤC TOÀN BỘ TRẠNG THÁI (LOCALSTORAGE)
// ==========================================
function saveMini15_18Checkpoint() {
    try {
        saveCurrentExamDrafts();
        const payload = {
            version: 2,
            updatedAt: Date.now(),
            currentTab,
            currentExamId,
            currentVocabFilter,
            isMeaningHidden,
            examStates,
            tpState
        };
        localStorage.setItem(MINI15_18_CP_KEY, JSON.stringify(payload));
        if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
            window.MarugotoCheckpoint.notifySaved();
        }
    } catch (e) {
        console.warn('Could not save checkpoint:', e);
    }
}

function restoreMini15_18Checkpoint() {
    try {
        const raw = localStorage.getItem(MINI15_18_CP_KEY);
        if (!raw) return false;
        const saved = JSON.parse(raw);
        if (!saved || saved.version !== 2) return false;

        if (saved.examStates && typeof saved.examStates === 'object') {
            Object.keys(saved.examStates).forEach(k => {
                if (EXAMS_LIST.some(e => e.id === k)) {
                    examStates[k] = saved.examStates[k];
                }
            });
        }
        if (saved.currentExamId && EXAMS_LIST.some(e => e.id === saved.currentExamId)) {
            currentExamId = saved.currentExamId;
        }
        if (typeof saved.isMeaningHidden === 'boolean') isMeaningHidden = saved.isMeaningHidden;
        if (typeof saved.currentVocabFilter === 'string') currentVocabFilter = saved.currentVocabFilter;
        if (saved.tpState && typeof saved.tpState === 'object') {
            tpState = Object.assign({}, tpState, saved.tpState);
        }
        if (typeof saved.currentTab === 'string') {
            currentTab = saved.currentTab;
        }
        return true;
    } catch (e) {
        console.warn('Could not restore checkpoint:', e);
        return false;
    }
}

window.__MARUGOTO_CP_EXTRA_KEYS__ = [MINI15_18_CP_KEY];
window.__MARUGOTO_ON_RESET__ = function () {
    localStorage.removeItem(MINI15_18_CP_KEY);
    window.location.reload();
};

document.addEventListener('DOMContentLoaded', () => {
    const restored = restoreMini15_18Checkpoint();

    if (typeof window.bindTypingInputEvents === 'function') {
        window.bindTypingInputEvents();
    }

    const p3Wrap = document.getElementById('part3Container');
    if (p3Wrap) {
        p3Wrap.addEventListener('input', (e) => {
            if (e.target && e.target.id && e.target.id.startsWith('p3_input_')) {
                saveMini15_18Checkpoint();
            }
        });
    }
    const p6Wrap = document.getElementById('part6Container');
    if (p6Wrap) {
        p6Wrap.addEventListener('input', (e) => {
            if (e.target && e.target.id && e.target.id.startsWith('p6_txt_')) {
                saveMini15_18Checkpoint();
            }
        });
    }

    bindActiveExamAliases();
    updateExamHeaderBanner();
    renderExamSwitcher();
    renderVocab(VOCAB_DATA);
    renderKanji(KANJI_DATA);
    renderPart1();
    renderPart2();
    renderPart3();
    renderPart4();
    renderPart5();
    renderPart6();
    const total = computeExamScore(currentExamId);
    const disp = document.getElementById('totalScoreText');
    if (disp) disp.innerText = `${total} / 100 Điểm`;

    const h = (window.location.hash || '').toLowerCase();
    if (h === '#typing' || h === '#tab-typing') {
        switchMainTab('tab-typing', true);
    } else if (restored && currentTab && document.getElementById(currentTab)) {
        switchMainTab(currentTab, true);
    }
    if (restored) {
        showToast('💾 Đã khôi phục checkpoint bài làm trước đó!');
    }
});
