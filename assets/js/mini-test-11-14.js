/* Modular Quiz & Checkpoint Engine for On_Tap_Mini_Test_A2_11_14 */
// Dữ liệu từ assets/data/mini_11_14_data.js
const {
    rawVocab,
    rawKanji,
    part1Data,
    part2Data,
    part3Data,
    part4Data,
    part5Data,
    part6Data
} = window.MINI_11_14_DATA;

const MINI11_14_CP_KEY = 'marugoto_mini11_14_cp_v1';
window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;
window.__MARUGOTO_CP_EXTRA_KEYS__ = [MINI11_14_CP_KEY];
window.__MARUGOTO_ON_RESET__ = function () {
    try { localStorage.removeItem(MINI11_14_CP_KEY); } catch (e) {}
    window.location.reload();
};

let currentTab = null;
let isRestoringMini11_14 = false;
let currentVocabFilter = 'ALL';
let currentKanjiFilter = 'ALL';
let isMeaningHidden = false;
let currentFilteredVocab = [...rawVocab];

// State Tracking for Score
let p1Answers = {};
let p2Selected = {}; // qId -> array of chosen chip indices
let p2Graded = {};
let p3Graded = {};
let p4Selected = {};
let p4Graded = {};
let p5Answers = {};
let p6SelfScores = {};

// Timer Variables (45:00)
let totalSeconds = 45 * 60;
let timerInterval = null;
let isTimerRunning = true;

function saveMini11_14Checkpoint() {
    if (isRestoringMini11_14) return;
    try {
        const p3Inputs = {};
        part3Data.forEach(item => {
            const inp = document.getElementById(`p3_input_${item.id}`);
            if (inp && inp.value) p3Inputs[item.id] = inp.value;
        });
        const p6Drafts = {};
        const p6ModelsOpen = {};
        part6Data.forEach(item => {
            const ta = document.getElementById(`trans_input_${item.id}`);
            if (ta && ta.value) p6Drafts[item.id] = ta.value;
            const mb = document.getElementById(`trans_model_${item.id}`);
            if (mb && mb.style.display === 'block') p6ModelsOpen[item.id] = true;
        });
        const payload = {
            t: Date.now(),
            currentTab: currentTab || (document.querySelector('.tab-panel.active') ? document.querySelector('.tab-panel.active').id : 'tab-quiz'),
            currentVocabFilter,
            currentKanjiFilter,
            isMeaningHidden,
            p1Answers,
            p2Selected,
            p2Graded,
            p3Graded,
            p3Inputs,
            p4Selected,
            p4Graded,
            p5Answers,
            p6SelfScores,
            p6Drafts,
            p6ModelsOpen,
            totalSeconds,
            isTimerRunning
        };
        localStorage.setItem(MINI11_14_CP_KEY, JSON.stringify(payload));
        if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
            window.MarugotoCheckpoint.notifySaved();
        }
    } catch (e) {}
}

function startTimer() {
    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(() => {
        if (isTimerRunning && totalSeconds > 0) {
            totalSeconds--;
            updateTimerDisplay();
            if (totalSeconds % 5 === 0) saveMini11_14Checkpoint();
        } else if (totalSeconds <= 0) {
            clearInterval(timerInterval);
            saveMini11_14Checkpoint();
            alert("⏱️ Hết thời gian 45 phút làm bài! Hãy xem lại kết quả tổng điểm của bạn.");
        }
    }, 1000);
}

function updateTimerDisplay() {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    const el = document.getElementById('timerText');
    if (el) {
        el.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }
}

function toggleTimer() {
    isTimerRunning = !isTimerRunning;
    const btn = (typeof event !== 'undefined' && event && event.target) ? event.target : null;
    if (btn) {
        btn.innerText = isTimerRunning ? "⏸️ Tạm Dừng" : "▶️ Tiếp Tục";
    }
    saveMini11_14Checkpoint();
}

function switchMainTab(tabId, opts) {
    currentTab = tabId;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

    const targetBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => 
        b.getAttribute('onclick') && b.getAttribute('onclick').includes(tabId)
    );
    if (targetBtn) targetBtn.classList.add('active');

    const targetPanel = document.getElementById(tabId);
    if (targetPanel) targetPanel.classList.add('active');
    if (!(opts && opts.skipScroll)) {
        window.scrollTo({ top: 180, behavior: 'smooth' });
    }
    if (!(opts && opts.skipSave)) {
        saveMini11_14Checkpoint();
    }
}

function speakText(text) {
    if (window.speakJapanese) {
        window.speakJapanese(text);
    } else if ('speechSynthesis' in window) {
        const u = new SpeechSynthesisUtterance(text);
        u.lang = 'ja-JP';
        window.speechSynthesis.speak(u);
    }
}

// ==========================================
// RENDER PART 1: TRẮC NGHIỆM (10 CÂU - 25Đ)
// ==========================================
function renderPart1() {
    const container = document.getElementById('part1Container');
    container.innerHTML = part1Data.map((item, idx) => `
        <div class="question-card" id="qCard_p1_${item.id}">
            <div class="q-header">
                <div>
                    <span class="q-num">Câu ${item.id}</span>
                    <span class="q-category">${item.category}</span>
                </div>
                <span class="q-points">2.5 Điểm</span>
            </div>
            <div class="q-text jp-text">${item.q}</div>
            <div class="options-list">
                ${item.options.map((opt, oIdx) => `
                    <button class="opt-btn" id="optBtn_p1_${item.id}_${oIdx}" onclick="selectPart1Answer(${item.id}, ${oIdx})">
                        <span class="opt-key">${['A', 'B', 'C', 'D'][oIdx]}</span>
                        <span class="jp-text">${opt}</span>
                    </button>
                `).join('')}
            </div>
            <div class="q-explain" id="explain_p1_${item.id}">
                💡 <strong>Giải thích chi tiết:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function selectPart1Answer(qId, selectedIdx) {
    if (p1Answers[qId] !== undefined) return;
    p1Answers[qId] = selectedIdx;
    const qItem = part1Data.find(q => q.id === qId);
    const correctIdx = qItem.correct;

    qItem.options.forEach((_, idx) => {
        const btn = document.getElementById(`optBtn_p1_${qId}_${idx}`);
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.add('correct');
        } else if (idx === selectedIdx) {
            btn.classList.add('wrong');
        }
    });

    const explainEl = document.getElementById(`explain_p1_${qId}`);
    if (explainEl) explainEl.style.display = 'block';

    updateTotalScore();
}

// ==========================================
// RENDER PART 2: SẮP XẾP TỪ ★ (5 CÂU - 15Đ)
// ==========================================
function renderPart2() {
    const container = document.getElementById('part2Container');
    container.innerHTML = part2Data.map((item, idx) => {
        p2Selected[item.id] = p2Selected[item.id] || [];
        return `
            <div class="question-card" id="qCard_p2_${item.id}">
                <div class="q-header">
                    <div>
                        <span class="q-num">Câu ${item.id}</span>
                        <span class="q-category">${item.category}</span>
                    </div>
                    <span class="q-points">3.0 Điểm</span>
                </div>
                <div style="font-size: 0.95rem; color: var(--gray-600); margin-bottom: 8px;">${item.prompt}</div>

                <div class="arrange-display-box jp-text">
                    <span>${item.pre}</span>
                    <span class="arrange-slot" id="p2_slot_${item.id}_0">${p2Selected[item.id][0] !== undefined ? item.chips[p2Selected[item.id][0]] : '[ 1 ]'}</span>
                    <span class="arrange-slot" id="p2_slot_${item.id}_1">${p2Selected[item.id][1] !== undefined ? item.chips[p2Selected[item.id][1]] : '[ 2 ]'}</span>
                    <span class="arrange-slot star" id="p2_slot_${item.id}_2">${p2Selected[item.id][2] !== undefined ? item.chips[p2Selected[item.id][2]] : '★ [ 3 ]'}</span>
                    <span class="arrange-slot" id="p2_slot_${item.id}_3">${p2Selected[item.id][3] !== undefined ? item.chips[p2Selected[item.id][3]] : '[ 4 ]'}</span>
                    <span>${item.post}</span>
                </div>

                <div class="chips-container" id="p2_chips_${item.id}">
                    ${item.chips.map((chip, cIdx) => `
                        <button type="button" class="word-chip jp-text" id="p2_chip_btn_${item.id}_${cIdx}" onclick="clickArrangeChip(${item.id}, ${cIdx})">
                            <strong>${cIdx + 1}.</strong> ${chip}
                        </button>
                    `).join('')}
                </div>

                <div class="arrange-ctrl-row">
                    <button type="button" class="btn-check-arrange" id="p2_check_btn_${item.id}" onclick="checkArrangeAnswer(${item.id})">
                        ✔️ Xác Nhận Thứ Tự & Kiểm Tra
                    </button>
                    <button type="button" class="btn-reset-arrange" onclick="resetSingleArrange(${item.id})">
                        🔄 Xếp Lại
                    </button>
                </div>

                <div class="q-explain" id="explain_p2_${item.id}">
                    💡 <strong>Câu hoàn chỉnh:</strong> <span class="jp-text" style="font-weight:700;">${item.fullSentence}</span><br>
                    ⭐ <strong>Từ ở vị trí ngôi sao [ ★ ]:</strong> <span style="font-weight:700; color: #b45309;">${item.starChip}</span><br>
                    ${item.explain}
                </div>
            </div>
        `;
    }).join('');
}

function clickArrangeChip(qId, chipIdx) {
    if (p2Graded[qId]) return;
    let chosen = p2Selected[qId] || [];
    if (chosen.includes(chipIdx)) return;
    if (chosen.length >= 4) return;

    chosen.push(chipIdx);
    p2Selected[qId] = chosen;

    // Mark chip as used
    const chipBtn = document.getElementById(`p2_chip_btn_${qId}_${chipIdx}`);
    if (chipBtn) chipBtn.classList.add('used');

    // Update slots
    const qItem = part2Data.find(q => q.id === qId);
    chosen.forEach((cIdx, pos) => {
        const slot = document.getElementById(`p2_slot_${qId}_${pos}`);
        if (slot) slot.innerText = qItem.chips[cIdx];
    });
    saveMini11_14Checkpoint();
}

function resetSingleArrange(qId) {
    if (p2Graded[qId]) return;
    p2Selected[qId] = [];
    for (let i = 0; i < 4; i++) {
        const slot = document.getElementById(`p2_slot_${qId}_${i}`);
        if (slot) {
            slot.innerText = (i === 2) ? '★ [ 3 ]' : `[ ${i + 1} ]`;
        }
        const chipBtn = document.getElementById(`p2_chip_btn_${qId}_${i}`);
        if (chipBtn) chipBtn.classList.remove('used');
    }
    saveMini11_14Checkpoint();
}

function checkArrangeAnswer(qId) {
    if (p2Graded[qId]) return;
    const chosen = p2Selected[qId] || [];
    if (chosen.length < 4) {
        alert("Vui lòng bấm chọn đủ cả 4 từ trước khi kiểm tra nhé!");
        return;
    }

    const qItem = part2Data.find(q => q.id === qId);
    // Correct if starIndex matched OR entire order matched
    const isStarCorrect = (chosen[qItem.starIndex] === qItem.correctOrder[qItem.starIndex]);
    const isEntireCorrect = (JSON.stringify(chosen) === JSON.stringify(qItem.correctOrder));

    const isCorrect = isStarCorrect || isEntireCorrect;
    p2Graded[qId] = isCorrect ? 3.0 : 0.0;

    const checkBtn = document.getElementById(`p2_check_btn_${qId}`);
    if (checkBtn) {
        checkBtn.disabled = true;
        if (isCorrect) {
            checkBtn.style.background = '#10b981';
            checkBtn.innerText = "✅ Chính Xác (+3.0đ)";
        } else {
            checkBtn.style.background = '#f43f5e';
            checkBtn.innerText = "❌ Chưa Đúng (0đ)";
        }
    }

    const explainEl = document.getElementById(`explain_p2_${qId}`);
    if (explainEl) explainEl.style.display = 'block';

    updateTotalScore();
}

// ==========================================
// RENDER PART 3: CHIA DẠNG ĐÚNG (5 CÂU - 15Đ)
// ==========================================
function renderPart3() {
    const container = document.getElementById('part3Container');
    container.innerHTML = part3Data.map((item, idx) => `
        <div class="question-card" id="qCard_p3_${item.id}">
            <div class="q-header">
                <div>
                    <span class="q-num">Câu ${item.id}</span>
                    <span class="q-category">${item.category}</span>
                </div>
                <span class="q-points">3.0 Điểm</span>
            </div>
            <div class="q-text jp-text">${item.sentence}</div>
            <div class="conjugate-row">
                <input type="text" class="conj-input jp-text" id="p3_input_${item.id}" placeholder="Nhập dạng chia đúng..." oninput="saveMini11_14Checkpoint()" onkeydown="if(event.key==='Enter' && !event.isComposing && event.keyCode!==229) checkConjugateAnswer(${item.id})">
                <button type="button" class="btn-check-arrange" id="p3_btn_${item.id}" onclick="checkConjugateAnswer(${item.id})">
                    Kiểm Tra
                </button>
                <span style="font-size: 0.88rem; color: var(--gray-500);">Từ gốc: <strong>${item.baseWord}</strong></span>
            </div>
            <div class="q-explain" id="explain_p3_${item.id}">
                🎯 <strong>Đáp án chuẩn:</strong> <span class="jp-text" style="font-weight:800; color: #166534;">${item.displayAnswer}</span><br>
                💡 <strong>Quy tắc ngữ pháp:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function checkConjugateAnswer(qId) {
    if (p3Graded[qId] !== undefined) return;
    const inputEl = document.getElementById(`p3_input_${qId}`);
    const userVal = inputEl.value.trim().toLowerCase();
    if (!userVal) {
        alert("Hãy nhập câu trả lời trước khi kiểm tra nhé!");
        return;
    }

    const qItem = part3Data.find(q => q.id === qId);
    const isMatched = qItem.accepted.some(acc => userVal === acc.toLowerCase());

    inputEl.disabled = true;
    const btn = document.getElementById(`p3_btn_${qId}`);
    btn.disabled = true;

    if (isMatched) {
        inputEl.classList.add('correct');
        btn.style.background = '#10b981';
        btn.innerText = "✅ Đúng (+3.0đ)";
        p3Graded[qId] = 3.0;
    } else {
        inputEl.classList.add('wrong');
        btn.style.background = '#f43f5e';
        btn.innerText = "❌ Sai (0đ)";
        p3Graded[qId] = 0.0;
    }

    const explainEl = document.getElementById(`explain_p3_${qId}`);
    if (explainEl) explainEl.style.display = 'block';

    updateTotalScore();
}

// ==========================================
// RENDER PART 4: NỐI CỘT TÌNH HUỐNG (4 CÂU - 10Đ)
// ==========================================
function renderPart4() {
    const container = document.getElementById('part4Container');
    container.innerHTML = `
        <div class="question-card">
            <div class="matching-grid">
                ${part4Data.map((item, idx) => `
                    <div class="match-card-a" id="matchCard_${item.id}">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span class="q-num">Tình Huống ${idx + 1} (Câu ${item.id})</span>
                            <span class="q-points">2.5đ</span>
                        </div>
                        <div class="jp-text" style="font-weight:700; color: var(--gray-900); font-size: 1rem; margin-top: 4px;">
                            ${item.situation}
                        </div>
                        <div style="font-size: 0.85rem; color: var(--gray-600); margin-bottom: 6px;">
                            ${item.context}
                        </div>
                        <select class="match-select jp-text" id="matchSelect_${item.id}" onchange="onSelectMatchAnswer(${item.id})">
                            <option value="">-- Chọn câu đối đáp phù hợp --</option>
                            ${item.options.map((opt, oIdx) => `
                                <option value="${oIdx}">${opt}</option>
                            `).join('')}
                        </select>
                        <div class="q-explain" id="explain_p4_${item.id}">
                            💡 <strong>Giải thích:</strong> ${item.explain}
                        </div>
                    </div>
                `).join('')}
            </div>
            <div style="margin-top: 18px; text-align: right;">
                <button type="button" class="quiz-btn primary" id="btnCheckMatchAll" onclick="checkAllMatching()">
                    ✔️ Chấm Điểm Toàn Bộ Phần Nối Thẻ
                </button>
            </div>
        </div>
    `;
}

function onSelectMatchAnswer(qId) {
    const sel = document.getElementById(`matchSelect_${qId}`);
    p4Selected[qId] = sel.value;
    saveMini11_14Checkpoint();
}

function checkAllMatching() {
    part4Data.forEach(item => {
        const sel = document.getElementById(`matchSelect_${item.id}`);
        const chosen = p4Selected[item.id];
        sel.disabled = true;

        const card = document.getElementById(`matchCard_${item.id}`);
        if (chosen !== undefined && parseInt(chosen) === item.correct) {
            card.style.borderColor = '#10b981';
            card.style.background = '#f0fdf4';
            p4Graded[item.id] = 2.5;
        } else {
            card.style.borderColor = '#f43f5e';
            card.style.background = '#fff1f2';
            p4Graded[item.id] = 0.0;
        }

        const explainEl = document.getElementById(`explain_p4_${item.id}`);
        if (explainEl) explainEl.style.display = 'block';
    });

    const btn = document.getElementById('btnCheckMatchAll');
    btn.disabled = true;
    btn.innerText = "Đã Hoàn Thành Chấm Điểm";
    updateTotalScore();
}

// ==========================================
// RENDER PART 5: ĐỌC HIỂU ĐOẠN VĂN (4 CÂU - 20Đ)
// ==========================================
function renderPart5() {
    const container = document.getElementById('part5Container');
    container.innerHTML = part5Data.map(pass => `
        <div class="passage-card">
            <div class="passage-title">${pass.title}</div>
            <div class="passage-text jp-text">${pass.text}</div>
        </div>
        ${pass.questions.map(q => `
            <div class="question-card" id="qCard_p5_${q.id}">
                <div class="q-header">
                    <div>
                        <span class="q-num">Câu ${q.id}</span>
                        <span class="q-category">Đọc hiểu chi tiết</span>
                    </div>
                    <span class="q-points">5.0 Điểm</span>
                </div>
                <div class="q-text jp-text">${q.q}</div>
                <div class="options-list">
                    ${q.options.map((opt, oIdx) => `
                        <button class="opt-btn" id="optBtn_p5_${q.id}_${oIdx}" onclick="selectPart5Answer(${q.id}, ${oIdx})">
                            <span class="opt-key">${['A', 'B', 'C', 'D'][oIdx]}</span>
                            <span class="jp-text">${opt}</span>
                        </button>
                    `).join('')}
                </div>
                <div class="q-explain" id="explain_p5_${q.id}">
                    💡 <strong>Giải thích trích dẫn:</strong> ${q.explain}
                </div>
            </div>
        `).join('')}
    `).join('');
}

function selectPart5Answer(qId, selectedIdx) {
    if (p5Answers[qId] !== undefined) return;
    p5Answers[qId] = selectedIdx;

    let foundQ = null;
    for (const p of part5Data) {
        const f = p.questions.find(q => q.id === qId);
        if (f) { foundQ = f; break; }
    }

    const correctIdx = foundQ.correct;
    foundQ.options.forEach((_, idx) => {
        const btn = document.getElementById(`optBtn_p5_${qId}_${idx}`);
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.add('correct');
        } else if (idx === selectedIdx) {
            btn.classList.add('wrong');
        }
    });

    const explainEl = document.getElementById(`explain_p5_${qId}`);
    if (explainEl) explainEl.style.display = 'block';

    updateTotalScore();
}

// ==========================================
// RENDER PART 6: LUYỆN DỊCH CÂU (4 CÂU - 15Đ)
// ==========================================
function renderPart6() {
    const container = document.getElementById('part6Container');
    container.innerHTML = part6Data.map(item => `
        <div class="question-card" id="qCard_p6_${item.id}">
            <div class="q-header">
                <div>
                    <span class="q-num">Câu ${item.id}</span>
                    <span class="q-category">${item.category}</span>
                </div>
                <span class="q-points">3.75 Điểm</span>
            </div>
            <div style="font-size: 1.15rem; font-weight: 800; color: #1e1b4b; margin-bottom: 6px;">
                🇻🇳 ${item.vi}
            </div>
            <div style="font-size: 0.88rem; color: var(--gray-600); margin-bottom: 8px;">
                💡 <em>Gợi ý từ vựng:</em> ${item.hint}
            </div>
            <textarea class="trans-input-box jp-text" id="trans_input_${item.id}" placeholder="Nhập bản dịch tiếng Nhật của bạn vào đây..." oninput="saveMini11_14Checkpoint()"></textarea>

            <div style="margin-top: 10px; display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
                <button type="button" class="btn-check-arrange" onclick="toggleTranslationModel(${item.id})">
                    👁️ Đối Chiếu Đáp Án Chuẩn
                </button>
                <button type="button" class="tool-toggle-btn" id="btnSelfGrade_${item.id}" onclick="selfGradeTranslation(${item.id})">
                    ⭐ Tự Đánh Giá Đạt (+3.75đ)
                </button>
            </div>

            <div class="trans-model-box" id="trans_model_${item.id}">
                <div style="font-size: 0.85rem; font-weight: 800; color: #15803d; text-transform: uppercase;">
                    Câu Mẫu Chuẩn Marugoto:
                </div>
                <div class="jp-text" style="font-size: 1.25rem; font-weight: 800; color: #14532d; margin: 4px 0 2px 0;">
                    ${item.modelSentence}
                </div>
                <div class="jp-text" style="font-size: 0.95rem; color: #166534; margin-bottom: 10px;">
                    (${item.modelKana})
                </div>
                <div style="font-size: 0.88rem; font-weight: 700; color: #166534; margin-bottom: 4px;">
                    Phân tích thành phần cấu trúc:
                </div>
                <ul class="trans-breakdown-list">
                    ${item.breakdown.map(b => `
                        <li>• <strong class="jp-text">${b.part}:</strong> ${b.role}</li>
                    `).join('')}
                </ul>
            </div>
        </div>
    `).join('');
}

function toggleTranslationModel(qId) {
    const box = document.getElementById(`trans_model_${qId}`);
    if (box) {
        box.style.display = (box.style.display === 'block') ? 'none' : 'block';
        saveMini11_14Checkpoint();
    }
}

function selfGradeTranslation(qId) {
    if (p6SelfScores[qId]) {
        p6SelfScores[qId] = 0;
        const btn = document.getElementById(`btnSelfGrade_${qId}`);
        btn.classList.remove('active');
        btn.innerText = "⭐ Tự Đánh Giá Đạt (+3.75đ)";
    } else {
        p6SelfScores[qId] = 3.75;
        const btn = document.getElementById(`btnSelfGrade_${qId}`);
        btn.classList.add('active');
        btn.innerText = "✅ Đã Tính Điểm (+3.75đ)";
    }
    updateTotalScore();
}

// ==========================================
// TOTAL SCORE CALCULATION (100 PTS)
// ==========================================
function updateTotalScore() {
    let total = 0;
    let answeredQuestions = 0;

    // P1: 10 Qs * 2.5 = 25 pts
    part1Data.forEach(q => {
        if (p1Answers[q.id] !== undefined) {
            answeredQuestions++;
            if (p1Answers[q.id] === q.correct) total += 2.5;
        }
    });

    // P2: 5 Qs * 3.0 = 15 pts
    Object.keys(p2Graded).forEach(qId => {
        answeredQuestions++;
        total += p2Graded[qId];
    });

    // P3: 5 Qs * 3.0 = 15 pts
    Object.keys(p3Graded).forEach(qId => {
        answeredQuestions++;
        total += p3Graded[qId];
    });

    // P4: 4 Qs * 2.5 = 10 pts
    Object.keys(p4Graded).forEach(qId => {
        answeredQuestions++;
        total += p4Graded[qId];
    });

    // P5: 4 Qs * 5.0 = 20 pts
    for (const p of part5Data) {
        for (const q of p.questions) {
            if (p5Answers[q.id] !== undefined) {
                answeredQuestions++;
                if (p5Answers[q.id] === q.correct) total += 5.0;
            }
        }
    }

    // P6: 4 Qs * 3.75 = 15 pts
    Object.keys(p6SelfScores).forEach(qId => {
        if (p6SelfScores[qId] > 0) {
            answeredQuestions++;
            total += p6SelfScores[qId];
        }
    });

    const totalRounded = Math.round(total * 10) / 10;
    document.getElementById('totalScoreDisplay').innerText = totalRounded;
    document.getElementById('quizProgressText').innerText = 
        `Đã làm: ${answeredQuestions}/32 câu • Tổng điểm hiện tại: ${totalRounded} / 100đ`;

    if (answeredQuestions >= 32) {
        let rank = "🏆 XUẤT SẮC!";
        if (totalRounded < 50) rank = "⚠️ CẦN ÔN TẬP THÊM!";
        else if (totalRounded < 70) rank = "👍 KHÁ TỐT!";
        else if (totalRounded < 85) rank = "🌟 GIỎI!";

        document.getElementById('quizStatusTitle').innerText = 
            `HOÀN THÀNH BÀI THI: ${totalRounded} / 100 ĐIỂM - ${rank}`;
    }
    saveMini11_14Checkpoint();
}

function resetAllExam() {
    p1Answers = {};
    p2Selected = {};
    p2Graded = {};
    p3Graded = {};
    p4Selected = {};
    p4Graded = {};
    p5Answers = {};
    p6SelfScores = {};

    totalSeconds = 45 * 60;
    isTimerRunning = true;
    updateTimerDisplay();

    renderPart1();
    renderPart2();
    renderPart3();
    renderPart4();
    renderPart5();
    renderPart6();

    document.getElementById('totalScoreDisplay').innerText = '0';
    document.getElementById('quizStatusTitle').innerText = 'Đề Khảo Sát Năng Lực Toàn Diện Bài 11 - 14';
    document.getElementById('quizProgressText').innerText = 'Hoàn thành: 0/32 câu • Tổng điểm hiện tại: 0 / 100đ';

    localStorage.removeItem(MINI11_14_CP_KEY);
    window.scrollTo({ top: document.getElementById('tab-quiz').offsetTop - 60, behavior: 'smooth' });
}

// ==========================================
// VOCAB & KANJI SCRIPTS
// ==========================================
function renderVocab(list) {
    const container = document.getElementById('vocabContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy từ vựng nào phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map(item => `
        <div class="vocab-card">
            <div class="vocab-top">
                <div>
                    <span class="vocab-badge">${item.l}</span>
                    <div class="vocab-jp jp-text" style="margin-top: 4px;">${item.kanji || item.kana}</div>
                    ${item.kanji && item.kanji !== item.kana ? `<div class="vocab-sub jp-text">${item.kana}</div>` : ''}
                    <div class="vocab-sub">${item.romaji} ${item.hv ? `• <span style="font-weight:700;">${item.hv}</span>` : ''}</div>
                </div>
                <button class="sound-btn" onclick="speakText('${item.kanji || item.kana}')" title="Nghe phát âm">🔊</button>
            </div>
            <div class="vocab-vi ${isMeaningHidden ? 'hidden-meaning' : ''}" onclick="this.classList.toggle('hidden-meaning')">
                ${item.vi}
            </div>
        </div>
    `).join('');
}

function filterVocab(lesson, btn) {
    currentVocabFilter = lesson;
    if (btn) {
        btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    applyVocabFilter();
    saveMini11_14Checkpoint();
}

function handleVocabSearch() {
    applyVocabFilter();
}

function applyVocabFilter() {
    const keyword = document.getElementById('vocabSearchInput').value.trim().toLowerCase();
    let filtered = rawVocab;
    if (currentVocabFilter !== 'ALL') {
        filtered = filtered.filter(w => w.l === currentVocabFilter);
    }
    if (keyword) {
        filtered = filtered.filter(w => 
            (w.kanji && w.kanji.toLowerCase().includes(keyword)) ||
            (w.kana && w.kana.toLowerCase().includes(keyword)) ||
            (w.romaji && w.romaji.toLowerCase().includes(keyword)) ||
            (w.hv && w.hv.toLowerCase().includes(keyword)) ||
            (w.vi && w.vi.toLowerCase().includes(keyword))
        );
    }
    currentFilteredVocab = filtered;
    const countEl = document.getElementById('quizletVocabCount');
    if (countEl) countEl.innerText = filtered.length;
    renderVocab(filtered);
}

function cleanJpTermForQuizlet(str) {
    if (!str) return "";
    let s = str;
    s = s.replace(/[~～…\.]/g, "");
    s = s.replace(/^[nN]が/g, "");
    s = s.replace(/^[nNpPvV][をにへとがで]/g, "");
    s = s.replace(/[vV]ましょう/g, "ましょう");
    s = s.replace(/[vV]ました/g, "");
    s = s.replace(/[vV]$/g, "");
    s = s.replace(/てください$/g, "");
    s = s.replace(/\([^)]*を\)/g, "").replace(/（[^）]*を）/g, "");
    s = s.replace(/\(お\)/g, "お").replace(/（お）/g, "お");
    s = s.replace(/\(します\)/g, "します").replace(/（します）/g, "します");
    s = s.replace(/\(さん\)/g, "").replace(/（さん）/g, "");
    s = s.replace(/\(な\)/g, "").replace(/（な）/g, "");
    s = s.replace(/[\(\)（）]/g, "");
    if (s.includes("/") || s.includes("／")) {
        s = s.split(/[\/／]/)[0];
    }
    s = s.replace(/[NPVnvp]/g, "");
    s = s.replace(/[。、,，\?？！!]/g, "");
    s = s.replace(/[\s　]+/g, "");
    return s.trim();
}

function formatQuizletVocabLine(item, delimiter = '	', formatType = 'kana') {
    const def = (item.vi || '').trim();
    if (formatType === 'combined') {
        const kanji = cleanJpTermForQuizlet(item.kanji || item.kana);
        const kana = cleanJpTermForQuizlet(item.kana || '');
        if (kana && kana !== kanji) {
            return `${kanji}${delimiter}[${kana}] ${def}`;
        } else {
            return `${kanji}${delimiter}${def}`;
        }
    } else if (formatType === 'kanji') {
        const term = cleanJpTermForQuizlet(item.kanji || item.kana);
        return `${term}${delimiter}${def}`;
    } else {
        // Ưu tiên KANA sạch 100% để gõ siêu mượt: くだもの [Tab] Hoa quả
        const term = cleanJpTermForQuizlet(item.kana || item.kanji);
        return `${term}${delimiter}${def}`;
    }
}

// 1. Copy chuẩn Quizlet Tab (mặc định): くだもの [Tab] Hoa quả
function copyVocabQuizletFormat() {
    copyFilteredQuizlet('	', 'kana');
}

// 2. Copy chuẩn Dấu Hai Chấm (：): くだもの：Hoa quả
function copyVocabColonFormat() {
    copyFilteredQuizlet('：', 'kana');
}

// 3. Copy kèm Kanji & Kana (như Quizlet Pro): 果物 [Tab] [くだもの] Hoa quả
function copyVocabCombinedFormat() {
    copyFilteredQuizlet('	', 'combined');
}

// 4. Copy trọn bộ 118 từ Tab: くだもの [Tab] Hoa quả
function copyFullQuizletFormat() {
    copyFullQuizlet('	', 'kana');
}

// 5. Copy trọn bộ 118 từ Dấu Hai Chấm (：): くだもの：Hoa quả
function copyFullColonFormat() {
    copyFullQuizlet('：', 'kana');
}

// 6. Copy trọn bộ kèm Kanji & Kana: 果物 [Tab] [くだもの] Hoa quả
function copyFullCombinedFormat() {
    copyFullQuizlet('	', 'combined');
}

// 7. Copy Kanji Tab
function copyFullKanjiFormat() {
    copyFullQuizlet('	', 'kanji');
}

function copyFilteredQuizlet(delimiter = '	', formatType = 'kana') {
    if (!currentFilteredVocab || currentFilteredVocab.length === 0) {
        showToast("Không có từ vựng nào để sao chép!");
        return;
    }
    const text = currentFilteredVocab.map(item => formatQuizletVocabLine(item, delimiter, formatType)).join('\n');
    let label = 'Kana gõ Quizlet (くだもの [Tab] Hoa quả)';
    if (delimiter === '：') label = 'Dấu hai chấm (くだもの：Hoa quả)';
    else if (formatType === 'combined') label = 'Kèm Kanji & Kana (果物 [Tab] [くだもの] Hoa quả)';
    else if (formatType === 'kanji') label = 'Kanji';

    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredVocab.length} từ chuẩn ${label}!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredVocab.length, label);
    });
}

function copyFullQuizlet(delimiter = '	', formatType = 'kana') {
    const text = rawVocab.map(item => formatQuizletVocabLine(item, delimiter, formatType)).join('\n');
    let label = 'Kana gõ Quizlet (くだもの [Tab] Hoa quả)';
    if (delimiter === '：') label = 'Dấu hai chấm (くだもの：Hoa quả)';
    else if (formatType === 'combined') label = 'Kèm Kanji & Kana (果物 [Tab] [くだもの] Hoa quả)';
    else if (formatType === 'kanji') label = 'Kanji';

    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy toàn bộ ${rawVocab.length} từ chuẩn ${label}!`);
    }).catch(() => {
        fallbackCopyText(text, rawVocab.length, label);
    });
}

function fallbackCopyText(text, count, label) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast(`✅ Đã copy ${count} từ chuẩn ${label}!`);
}

function showToast(msg) {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => { toast.style.display = 'none'; }, 2800);
}

function toggleHideMeaning() {
    isMeaningHidden = !isMeaningHidden;
    const btn = document.getElementById('hideMeaningBtn');
    if (isMeaningHidden) {
        btn.classList.add('active');
        btn.innerHTML = '👁️ Đang ẩn nghĩa (Chạm vào thẻ để xem)';
    } else {
        btn.classList.remove('active');
        btn.innerHTML = '👁️ Ẩn nghĩa tiếng Việt (Tự dò)';
    }
    document.querySelectorAll('.vocab-vi').forEach(el => {
        if (isMeaningHidden) el.classList.add('hidden-meaning');
        else el.classList.remove('hidden-meaning');
    });
    saveMini11_14Checkpoint();
}

let currentFilteredKanji = [...rawKanji];

function formatKanjiLine(item, delimiter = ': ') {
    const ch = item.char;
    const mean = item.shortMeaning || (item.meaning ? item.meaning.split(',')[0].trim() : '');
    const hv = (item.hv || '').toUpperCase();
    const rd = item.hiragana || '';
    if (delimiter === '\t') {
        return `${ch}、${mean}, ${hv}\t${rd}`;
    }
    return `${ch}、${mean}, ${hv}: ${rd}`;
}

function copyKanjiColonFormat() {
    if (!currentFilteredKanji || currentFilteredKanji.length === 0) {
        showToast("Không có chữ Hán nào để sao chép!");
        return;
    }
    const text = currentFilteredKanji.map(k => formatKanjiLine(k, ': ')).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredKanji.length} chữ Hán (Dạng: 車、xe ô tô, XA: くるま)!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredKanji.length, 'Dạng: 車、xe ô tô, XA: くるま');
    });
}

function copyKanjiQuizletTabFormat() {
    if (!currentFilteredKanji || currentFilteredKanji.length === 0) {
        showToast("Không có chữ Hán nào để sao chép!");
        return;
    }
    const text = currentFilteredKanji.map(k => formatKanjiLine(k, '\t')).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredKanji.length} chữ Hán chuẩn Quizlet (Tab)!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredKanji.length, 'Quizlet Tab');
    });
}

function copySingleKanji(char) {
    const item = rawKanji.find(k => k.char === char);
    if (!item) return;
    const line = formatKanjiLine(item, ': ');
    navigator.clipboard.writeText(line).then(() => {
        showToast(`✅ Đã copy: ${line}`);
    }).catch(() => {
        fallbackCopyText(line, 1, line);
    });
}

function renderKanji(list) {
    const container = document.getElementById('kanjiContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy chữ Hán phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map(item => `
        <div class="kanji-card">
            <div class="kanji-header">
                <div class="kanji-char-box jp-text">${item.char}</div>
                <div class="kanji-meta">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 8px;">
                        <div class="kanji-hv">${item.hv} <span style="font-size: 0.92rem; font-weight: 700; color: #166534;">(${item.hiragana || ''})</span></div>
                        <button type="button" class="sound-btn" onclick="copySingleKanji('${item.char}')" title="Copy: ${item.char}、${item.shortMeaning || item.meaning.split(',')[0]}, ${item.hv.toUpperCase()}: ${item.hiragana}" style="width: auto; height: 26px; padding: 0 10px; border-radius: 6px; font-size: 0.76rem; font-weight: 700; background: #e0f2fe; color: #0369a1;">
                            📋 Copy
                        </button>
                    </div>
                    <div class="kanji-meaning">${item.meaning}</div>
                    <div class="kanji-sub-row">
                        <span class="kanji-tag">${item.lessonName}</span>
                        <span class="kanji-tag">${item.strokes} nét</span>
                        <span class="kanji-tag" style="background:#fef3c7; color:#92400e; font-weight:800;">Đọc: ${item.hiragana}</span>
                    </div>
                </div>
            </div>

            <div class="kanji-detail-box">
                <div class="kanji-reading-item">
                    <strong>KUN:</strong> <span class="jp-text">${item.kun || '—'}</span>
                </div>
                <div class="kanji-reading-item">
                    <strong>ON:</strong> <span class="jp-text">${item.on || '—'}</span>
                </div>
                <div class="kanji-reading-item">
                    <strong>Chiết tự:</strong> <span>${item.formula || '—'}</span>
                </div>
            </div>

            <div class="kanji-mnemonic">
                💡 <strong>Mẹo nhớ:</strong> ${item.mnemonic || '—'}
            </div>

            <ul class="kanji-words">
                ${(item.examples || []).map(ex => `
                    <li class="kanji-word-item">
                        <span class="kw-jp jp-text">${ex.word} (${ex.reading})</span>
                        <span class="kw-vi">${ex.vi}</span>
                    </li>
                `).join('')}
            </ul>
        </div>
    `).join('');
}

function filterKanji(lesson, btn) {
    currentKanjiFilter = lesson;
    if (btn) {
        btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    applyKanjiFilter();
    saveMini11_14Checkpoint();
}

function handleKanjiSearch() {
    applyKanjiFilter();
}

function applyKanjiFilter() {
    const keyword = document.getElementById('kanjiSearchInput').value.trim().toLowerCase();
    let filtered = rawKanji;
    if (currentKanjiFilter !== 'ALL') {
        filtered = filtered.filter(k => k.lesson === currentKanjiFilter);
    }
    if (keyword) {
        filtered = filtered.filter(k => 
            k.char.includes(keyword) ||
            k.hv.toLowerCase().includes(keyword) ||
            k.meaning.toLowerCase().includes(keyword) ||
            (k.kun && k.kun.toLowerCase().includes(keyword)) ||
            (k.on && k.on.toLowerCase().includes(keyword)) ||
            (k.hiragana && k.hiragana.includes(keyword))
        );
    }
    currentFilteredKanji = filtered;
    renderKanji(filtered);
}

function restoreMini11_14Checkpoint() {
    try {
        const raw = localStorage.getItem(MINI11_14_CP_KEY);
        if (!raw) return false;
        const saved = JSON.parse(raw);
        if (!saved || typeof saved !== 'object') return false;
        isRestoringMini11_14 = true;

        if (saved.currentVocabFilter) {
            currentVocabFilter = saved.currentVocabFilter;
            document.querySelectorAll('button[onclick*="filterVocab("]').forEach(b => {
                const oc = b.getAttribute('onclick') || '';
                b.classList.toggle('active', oc.includes(`'${currentVocabFilter}'`));
            });
        }
        if (saved.currentKanjiFilter) {
            currentKanjiFilter = saved.currentKanjiFilter;
            document.querySelectorAll('button[onclick*="filterKanji("]').forEach(b => {
                const oc = b.getAttribute('onclick') || '';
                b.classList.toggle('active', oc.includes(`'${currentKanjiFilter}'`));
            });
        }
        if (typeof saved.isMeaningHidden === 'boolean') {
            isMeaningHidden = saved.isMeaningHidden;
            const hideBtn = document.getElementById('hideMeaningBtn');
            if (hideBtn) {
                hideBtn.classList.toggle('active', isMeaningHidden);
                hideBtn.innerHTML = isMeaningHidden
                    ? '👁️ Đang ẩn nghĩa (Chạm vào thẻ để xem)'
                    : '👁️ Ẩn nghĩa tiếng Việt (Tự dò)';
            }
        }
        if (saved.p1Answers && typeof saved.p1Answers === 'object') p1Answers = saved.p1Answers;
        if (saved.p2Selected && typeof saved.p2Selected === 'object') p2Selected = saved.p2Selected;
        if (saved.p2Graded && typeof saved.p2Graded === 'object') p2Graded = saved.p2Graded;
        if (saved.p3Graded && typeof saved.p3Graded === 'object') p3Graded = saved.p3Graded;
        if (saved.p4Selected && typeof saved.p4Selected === 'object') p4Selected = saved.p4Selected;
        if (saved.p4Graded && typeof saved.p4Graded === 'object') p4Graded = saved.p4Graded;
        if (saved.p5Answers && typeof saved.p5Answers === 'object') p5Answers = saved.p5Answers;
        if (saved.p6SelfScores && typeof saved.p6SelfScores === 'object') p6SelfScores = saved.p6SelfScores;
        if (Number.isFinite(saved.totalSeconds)) {
            totalSeconds = saved.totalSeconds;
            updateTimerDisplay();
        }
        if (typeof saved.isTimerRunning === 'boolean') {
            isTimerRunning = saved.isTimerRunning;
            const tBtn = document.querySelector('button[onclick*="toggleTimer("]');
            if (tBtn) tBtn.innerText = isTimerRunning ? "⏸️ Tạm Dừng" : "▶️ Tiếp Tục";
        }

        applyVocabFilter();
        applyKanjiFilter();
        renderPart1();
        renderPart2();
        renderPart3();
        renderPart4();
        renderPart5();
        renderPart6();

        // Khôi phục UI Part 1
        part1Data.forEach(item => {
            const chosen = p1Answers[item.id];
            if (chosen === undefined) return;
            item.options.forEach((_, idx) => {
                const btn = document.getElementById(`optBtn_p1_${item.id}_${idx}`);
                if (!btn) return;
                btn.disabled = true;
                if (idx === item.correct) btn.classList.add('correct');
                else if (idx === chosen) btn.classList.add('wrong');
            });
            const ex = document.getElementById(`explain_p1_${item.id}`);
            if (ex) ex.style.display = 'block';
        });

        // Khôi phục UI Part 2
        part2Data.forEach(item => {
            const chosen = p2Selected[item.id] || [];
            chosen.forEach(cIdx => {
                const chipBtn = document.getElementById(`p2_chip_btn_${item.id}_${cIdx}`);
                if (chipBtn) chipBtn.classList.add('used');
            });
            if (p2Graded[item.id] !== undefined) {
                const isCorrect = p2Graded[item.id] > 0;
                const checkBtn = document.getElementById(`p2_check_btn_${item.id}`);
                if (checkBtn) {
                    checkBtn.disabled = true;
                    checkBtn.style.background = isCorrect ? '#10b981' : '#f43f5e';
                    checkBtn.innerText = isCorrect ? "✅ Chính Xác (+3.0đ)" : "❌ Chưa Đúng (0đ)";
                }
                const ex = document.getElementById(`explain_p2_${item.id}`);
                if (ex) ex.style.display = 'block';
            }
        });

        // Khôi phục UI Part 3
        const p3Inputs = saved.p3Inputs || {};
        part3Data.forEach(item => {
            const inp = document.getElementById(`p3_input_${item.id}`);
            const btn = document.getElementById(`p3_btn_${item.id}`);
            if (inp && typeof p3Inputs[item.id] === 'string') inp.value = p3Inputs[item.id];
            if (p3Graded[item.id] !== undefined) {
                const isMatched = p3Graded[item.id] > 0;
                if (inp) {
                    inp.disabled = true;
                    inp.classList.add(isMatched ? 'correct' : 'wrong');
                }
                if (btn) {
                    btn.disabled = true;
                    btn.style.background = isMatched ? '#10b981' : '#f43f5e';
                    btn.innerText = isMatched ? "✅ Đúng (+3.0đ)" : "❌ Sai (0đ)";
                }
                const ex = document.getElementById(`explain_p3_${item.id}`);
                if (ex) ex.style.display = 'block';
            }
        });

        // Khôi phục UI Part 4
        const p4GradedAny = Object.keys(p4Graded).length > 0;
        part4Data.forEach(item => {
            const sel = document.getElementById(`matchSelect_${item.id}`);
            if (sel && p4Selected[item.id] !== undefined) sel.value = String(p4Selected[item.id]);
            if (p4Graded[item.id] !== undefined) {
                if (sel) sel.disabled = true;
                const card = document.getElementById(`matchCard_${item.id}`);
                if (card) {
                    const ok = p4Graded[item.id] > 0;
                    card.style.borderColor = ok ? '#10b981' : '#f43f5e';
                    card.style.background = ok ? '#f0fdf4' : '#fff1f2';
                }
                const ex = document.getElementById(`explain_p4_${item.id}`);
                if (ex) ex.style.display = 'block';
            }
        });
        if (p4GradedAny) {
            const btnAll = document.getElementById('btnCheckMatchAll');
            if (btnAll) {
                btnAll.disabled = true;
                btnAll.innerText = "Đã Hoàn Thành Chấm Điểm";
            }
        }

        // Khôi phục UI Part 5
        part5Data.forEach(pass => {
            pass.questions.forEach(q => {
                const chosen = p5Answers[q.id];
                if (chosen === undefined) return;
                q.options.forEach((_, idx) => {
                    const btn = document.getElementById(`optBtn_p5_${q.id}_${idx}`);
                    if (!btn) return;
                    btn.disabled = true;
                    if (idx === q.correct) btn.classList.add('correct');
                    else if (idx === chosen) btn.classList.add('wrong');
                });
                const ex = document.getElementById(`explain_p5_${q.id}`);
                if (ex) ex.style.display = 'block';
            });
        });

        // Khôi phục UI Part 6
        const p6Drafts = saved.p6Drafts || {};
        const p6ModelsOpen = saved.p6ModelsOpen || {};
        part6Data.forEach(item => {
            const ta = document.getElementById(`trans_input_${item.id}`);
            if (ta && typeof p6Drafts[item.id] === 'string') ta.value = p6Drafts[item.id];
            const mb = document.getElementById(`trans_model_${item.id}`);
            if (mb && p6ModelsOpen[item.id]) mb.style.display = 'block';
            if (p6SelfScores[item.id] > 0) {
                const btn = document.getElementById(`btnSelfGrade_${item.id}`);
                if (btn) {
                    btn.classList.add('active');
                    btn.innerText = "✅ Đã Tính Điểm (+3.75đ)";
                }
            }
        });

        updateTotalScore();
        if (saved.currentTab) {
            switchMainTab(saved.currentTab, { skipScroll: true, skipSave: true });
        }
        isRestoringMini11_14 = false;
        return true;
    } catch (e) {
        isRestoringMini11_14 = false;
        return false;
    }
}

// Initialize All Components on Load
document.addEventListener('DOMContentLoaded', () => {
    const restored = restoreMini11_14Checkpoint();
    if (!restored) {
        applyVocabFilter();
        renderKanji(rawKanji);
        renderPart1();
        renderPart2();
        renderPart3();
        renderPart4();
        renderPart5();
        renderPart6();
    }
    startTimer();
});
