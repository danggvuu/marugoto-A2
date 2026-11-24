/* Modular Quiz & Checkpoint Engine for On_Tap_Mini_Test_A2_2_1_4 (Marugoto A2.2 Lessons 1-4) */
const {
    rawVocab,
    rawKanji,
    part1Data,
    part2Data,
    part3Data,
    part4Data,
    part5Data,
    part6Data
} = window.MINI_A2_2_1_4_DATA;

const MINI_A2_2_1_4_CP_KEY = 'marugoto_mini_a2_2_1_4_cp_v1';
window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;
window.__MARUGOTO_CP_EXTRA_KEYS__ = [MINI_A2_2_1_4_CP_KEY];
window.__MARUGOTO_ON_RESET__ = function () {
    try { localStorage.removeItem(MINI_A2_2_1_4_CP_KEY); } catch (e) {}
    window.location.reload();
};

let currentTab = 'tab-quiz';
let isRestoringMini = false;
let currentVocabFilter = 'ALL';
let currentKanjiFilter = 'ALL';
let isMeaningHidden = false;
let currentFilteredVocab = [...rawVocab];
let currentFilteredKanji = [...rawKanji];

// State Tracking for Score
let p1Answers = {};      // qId -> chosen option index
let p2Selected = {};     // qId -> array of chosen chip indices
let p2Graded = {};       // qId -> boolean (correct/incorrect)
let p3Graded = {};       // qId -> boolean
let p4Selected = {};     // qId -> chosen option index
let p4Graded = {};       // qId -> boolean
let p5Answers = {};      // qId -> chosen option index
let p6SelfScores = {};   // qId -> numeric score (up to 3.75)

// Timer Variables (45:00)
let totalSeconds = 45 * 60;
let timerInterval = null;
let isTimerRunning = true;

function saveMiniCheckpoint() {
    if (isRestoringMini) return;
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
            const mb = document.getElementById(`p6_model_${item.id}`);
            if (mb && mb.style.display === 'block') p6ModelsOpen[item.id] = true;
        });
        const payload = {
            t: Date.now(),
            currentTab: currentTab || 'tab-quiz',
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
        localStorage.setItem(MINI_A2_2_1_4_CP_KEY, JSON.stringify(payload));
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
            if (totalSeconds % 5 === 0) saveMiniCheckpoint();
        } else if (totalSeconds <= 0) {
            clearInterval(timerInterval);
            saveMiniCheckpoint();
            alert("⏱️ Đã hết thời gian 45 phút làm bài! Hãy bấm 'Nộp Bài & Chấm Điểm' để xem kết quả.");
        }
    }, 1000);
}

function updateTimerDisplay() {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    const str = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    const el1 = document.getElementById('timerDisplay');
    if (el1) el1.innerText = str;
    const el2 = document.getElementById('timerText');
    if (el2) el2.innerText = str;
}

function toggleTimer() {
    isTimerRunning = !isTimerRunning;
    const btn = document.getElementById('timerToggleBtn');
    if (btn) {
        btn.innerHTML = isTimerRunning ? '⏸️ Tạm dừng' : '▶️ Tiếp tục';
    }
    saveMiniCheckpoint();
}

function switchTab(tabId, btn) {
    currentTab = tabId;
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));

    const target = document.getElementById(tabId);
    if (target) target.classList.add('active');

    if (btn) {
        btn.classList.add('active');
    } else {
        const found = document.querySelector(`.tab-btn[onclick*="${tabId}"]`);
        if (found) found.classList.add('active');
    }

    saveMiniCheckpoint();
}

// ==========================================
// RENDER PART 1: TRẮC NGHIỆM (10 CÂU - 25Đ)
// ==========================================
function renderPart1() {
    const container = document.getElementById('part1Container');
    container.innerHTML = part1Data.map(item => `
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
            <div class="q-explain" id="p1_exp_${item.id}">
                💡 <strong>Giải thích chi tiết:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function selectPart1Answer(qId, oIdx) {
    p1Answers[qId] = oIdx;
    const item = part1Data.find(q => q.id === qId);
    if (!item) return;

    item.options.forEach((_, idx) => {
        const b = document.getElementById(`optBtn_p1_${qId}_${idx}`);
        if (!b) return;
        b.classList.remove('selected', 'correct', 'wrong');
        if (idx === oIdx) {
            b.classList.add('selected');
            if (oIdx === item.correct) b.classList.add('correct');
            else b.classList.add('wrong');
        } else if (idx === item.correct) {
            b.classList.add('correct');
        }
    });

    const exp = document.getElementById(`p1_exp_${qId}`);
    if (exp) exp.style.display = 'block';

    calculateTotalScore();
    saveMiniCheckpoint();
}

// ==========================================
// RENDER PART 2: SẮP XẾP TỪ ★ (5 CÂU - 15Đ)
// ==========================================
function renderPart2() {
    const container = document.getElementById('part2Container');
    container.innerHTML = part2Data.map(item => `
        <div class="question-card" id="qCard_p2_${item.id}">
            <div class="q-header">
                <div>
                    <span class="q-num">Câu ${item.id}</span>
                    <span class="q-category">${item.category}</span>
                </div>
                <span class="q-points">3.0 Điểm</span>
            </div>
            <div style="font-size: 0.93rem; color: var(--gray-700); margin-bottom: 8px;">${item.prompt}</div>
            
            <div class="arrange-display-box jp-text">
                <span>${item.pre}</span>
                <span class="arrange-slot" id="p2_slot_${item.id}_0">___</span>
                <span class="arrange-slot" id="p2_slot_${item.id}_1">___</span>
                <span class="arrange-slot star" id="p2_slot_${item.id}_2">★</span>
                <span class="arrange-slot" id="p2_slot_${item.id}_3">___</span>
                <span>${item.post}</span>
            </div>

            <div class="chips-container" id="p2_pool_${item.id}">
                ${item.chips.map((chip, cIdx) => `
                    <button class="word-chip jp-text" id="p2_chip_${item.id}_${cIdx}" onclick="handlePart2ChipClick(${item.id}, ${cIdx})">
                        ${chip}
                    </button>
                `).join('')}
            </div>

            <div class="arrange-ctrl-row">
                <button class="btn-check-arrange" onclick="checkPart2Explicit(${item.id})">🎯 Kiểm Tra Thứ Tự</button>
                <button class="btn-reset-arrange" onclick="resetPart2Question(${item.id})">↩️ Chọn Lại Câu Này</button>
            </div>

            <div class="q-explain" id="p2_exp_${item.id}">
                🎯 <strong>Câu hoàn chỉnh:</strong> <span class="jp-text" style="font-weight: 700; color: #166534;">${item.fullSentence}</span><br>
                ⭐ <strong>Từ tại vị trí ngôi sao [★]:</strong> <span class="jp-text" style="font-weight: 800; color: #92400e;">${item.starChip}</span><br>
                💡 <strong>Giải thích:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function handlePart2ChipClick(qId, cIdx) {
    if (!p2Selected[qId]) p2Selected[qId] = [];
    const arr = p2Selected[qId];

    if (arr.includes(cIdx)) {
        p2Selected[qId] = arr.filter(idx => idx !== cIdx);
    } else {
        if (arr.length < 4) arr.push(cIdx);
    }

    updatePart2UI(qId);
    checkPart2Complete(qId);
    calculateTotalScore();
    saveMiniCheckpoint();
}

function updatePart2UI(qId) {
    const item = part2Data.find(q => q.id === qId);
    if (!item) return;

    const chosen = p2Selected[qId] || [];

    // Update slots
    for (let i = 0; i < 4; i++) {
        const slotEl = document.getElementById(`p2_slot_${qId}_${i}`);
        if (!slotEl) continue;
        if (chosen[i] !== undefined) {
            slotEl.innerText = item.chips[chosen[i]];
            slotEl.classList.add('filled');
        } else {
            slotEl.innerText = (i === 2) ? '★' : '___';
            slotEl.classList.remove('filled');
        }
    }

    // Update chips in pool
    item.chips.forEach((_, idx) => {
        const chipEl = document.getElementById(`p2_chip_${qId}_${idx}`);
        if (!chipEl) return;
        if (chosen.includes(idx)) chipEl.classList.add('selected');
        else chipEl.classList.remove('selected');
    });
}

function checkPart2Complete(qId) {
    const item = part2Data.find(q => q.id === qId);
    if (!item) return;
    const chosen = p2Selected[qId] || [];

    if (chosen.length === 4) {
        const isMatch = JSON.stringify(chosen) === JSON.stringify(item.correctOrder);
        p2Graded[qId] = isMatch;

        const exp = document.getElementById(`p2_exp_${qId}`);
        if (exp) exp.style.display = 'block';

        for (let i = 0; i < 4; i++) {
            const slotEl = document.getElementById(`p2_slot_${qId}_${i}`);
            if (slotEl) {
                if (isMatch) {
                    slotEl.style.borderColor = '#10b981';
                    slotEl.style.background = '#d1fae5';
                    slotEl.style.color = '#065f46';
                } else {
                    slotEl.style.borderColor = '#ef4444';
                    slotEl.style.background = '#fee2e2';
                    slotEl.style.color = '#991b1b';
                }
            }
        }
    } else {
        delete p2Graded[qId];
        const exp = document.getElementById(`p2_exp_${qId}`);
        if (exp) exp.style.display = 'none';

        for (let i = 0; i < 4; i++) {
            const slotEl = document.getElementById(`p2_slot_${qId}_${i}`);
            if (slotEl) {
                slotEl.style.borderColor = '';
                slotEl.style.background = '';
                slotEl.style.color = '';
            }
        }
    }
}

function checkPart2Explicit(qId) {
    const chosen = p2Selected[qId] || [];
    if (chosen.length < 4) {
        alert("Vui lòng chọn đủ 4 từ khóa vào các ô trống trước khi kiểm tra!");
        return;
    }
    checkPart2Complete(qId);
    calculateTotalScore();
    saveMiniCheckpoint();
}

function resetPart2Question(qId) {
    p2Selected[qId] = [];
    delete p2Graded[qId];
    updatePart2UI(qId);
    checkPart2Complete(qId);
    calculateTotalScore();
    saveMiniCheckpoint();
}

// ==========================================
// RENDER PART 3: CHIA DẠNG ĐÚNG (5 CÂU - 15Đ)
// ==========================================
function renderPart3() {
    const container = document.getElementById('part3Container');
    container.innerHTML = part3Data.map(item => `
        <div class="question-card" id="qCard_p3_${item.id}">
            <div class="q-header">
                <div>
                    <span class="q-num">Câu ${item.id}</span>
                    <span class="q-category">${item.category}</span>
                </div>
                <span class="q-points">3.0 Điểm</span>
            </div>
            
            <div class="q-text jp-text" style="font-size: 1.05rem;">
                ${item.sentence}
            </div>

            <div class="conjugate-input-wrap">
                <input type="text" id="p3_input_${item.id}" class="conjugate-input jp-text" placeholder="Nhập đáp án..." oninput="handlePart3Input(${item.id})" onkeydown="if(event.key==='Enter') gradePart3Question(${item.id})">
                <button class="btn-check-answer" id="p3_btn_${item.id}" onclick="gradePart3Question(${item.id})">Kiểm Tra</button>
            </div>

            <div class="q-explain" id="p3_exp_${item.id}">
                🎯 <strong>Đáp án chuẩn:</strong> <span class="jp-text" style="font-weight:800; color: #166534;">${item.displayAnswer}</span><br>
                💡 <strong>Giải thích:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function handlePart3Input(qId) {
    saveMiniCheckpoint();
}

function gradePart3Question(qId) {
    const item = part3Data.find(q => q.id === qId);
    if (!item) return;

    const inp = document.getElementById(`p3_input_${qId}`);
    if (!inp) return;
    const val = inp.value.trim().toLowerCase().replace(/\s+/g, '');

    if (!val) {
        alert("Vui lòng gõ đáp án vào ô trước khi kiểm tra!");
        return;
    }

    const isCorrect = item.accepted.some(acc => {
        const cleanAcc = acc.toLowerCase().replace(/\s+/g, '');
        return cleanAcc === val;
    });

    p3Graded[qId] = isCorrect;
    inp.classList.remove('correct', 'wrong');
    if (isCorrect) inp.classList.add('correct');
    else inp.classList.add('wrong');

    const exp = document.getElementById(`p3_exp_${qId}`);
    if (exp) exp.style.display = 'block';

    calculateTotalScore();
    saveMiniCheckpoint();
}

// ==========================================
// RENDER PART 4: NỐI CỘT TÌNH HUỐNG (4 CÂU - 10Đ)
// ==========================================
function renderPart4() {
    const container = document.getElementById('part4Container');
    container.innerHTML = part4Data.map(item => `
        <div class="question-card" id="qCard_p4_${item.id}">
            <div class="q-header">
                <div>
                    <span class="q-num">Câu ${item.id}</span>
                    <span class="q-category">${item.category}</span>
                </div>
                <span class="q-points">2.5 Điểm</span>
            </div>

            <div class="matching-container">
                <div class="matching-box">
                    <div class="matching-label">💬 Lời Thoại Tình Huống</div>
                    <div class="jp-text" style="font-size: 1.05rem; font-weight: 700; color: #1e1b4b; margin-bottom: 6px;">
                        ${item.situation}
                    </div>
                    <div style="font-size: 0.88rem; color: var(--gray-600); font-style: italic;">
                        ${item.context}
                    </div>
                </div>

                <div class="matching-box">
                    <div class="matching-label">👉 Chọn Câu Đáp Lại Lịch Sự & Phù Hợp</div>
                    <div class="options-list">
                        ${item.options.map((opt, oIdx) => `
                            <button class="opt-btn" id="optBtn_p4_${item.id}_${oIdx}" onclick="selectPart4Answer(${item.id}, ${oIdx})">
                                <span class="opt-key">${['A', 'B', 'C', 'D'][oIdx]}</span>
                                <span class="jp-text">${opt}</span>
                            </button>
                        `).join('')}
                    </div>
                </div>
            </div>

            <div class="q-explain" id="p4_exp_${item.id}">
                💡 <strong>Giải thích tình huống:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function selectPart4Answer(qId, oIdx) {
    p4Selected[qId] = oIdx;
    const item = part4Data.find(q => q.id === qId);
    if (!item) return;

    const isCorrect = (oIdx === item.correct);
    p4Graded[qId] = isCorrect;

    item.options.forEach((_, idx) => {
        const b = document.getElementById(`optBtn_p4_${qId}_${idx}`);
        if (!b) return;
        b.classList.remove('selected', 'correct', 'wrong');
        if (idx === oIdx) {
            b.classList.add('selected');
            if (isCorrect) b.classList.add('correct');
            else b.classList.add('wrong');
        } else if (idx === item.correct) {
            b.classList.add('correct');
        }
    });

    const exp = document.getElementById(`p4_exp_${qId}`);
    if (exp) exp.style.display = 'block';

    calculateTotalScore();
    saveMiniCheckpoint();
}

// ==========================================
// RENDER PART 5: ĐỌC HIỂU (4 CÂU / 2 BÀI - 20Đ)
// ==========================================
function renderPart5() {
    const container = document.getElementById('part5Container');
    container.innerHTML = part5Data.map(pass => `
        <div style="margin-bottom: 24px;">
            <div class="reading-box passage-card">
                <div class="reading-title passage-title">${pass.title}</div>
                <div class="reading-text passage-text jp-text">${pass.text}</div>
            </div>

            ${pass.questions.map(q => `
                <div class="question-card" id="qCard_p5_${q.id}" style="margin-top: 12px;">
                    <div class="q-header">
                        <div>
                            <span class="q-num">Câu ${q.id}</span>
                            <span class="q-category">Đọc Hiểu Đoạn Văn</span>
                        </div>
                        <span class="q-points">5.0 Điểm</span>
                    </div>

                    <div class="q-text jp-text" style="font-weight: 700;">
                        ${q.q}
                    </div>

                    <div class="options-list">
                        ${q.options.map((opt, oIdx) => `
                            <button class="opt-btn" id="optBtn_p5_${q.id}_${oIdx}" onclick="selectPart5Answer(${q.id}, ${oIdx})">
                                <span class="opt-key">${['A', 'B', 'C', 'D'][oIdx]}</span>
                                <span class="jp-text">${opt}</span>
                            </button>
                        `).join('')}
                    </div>

                    <div class="q-explain" id="p5_exp_${q.id}">
                        💡 <strong>Căn cứ đoạn văn:</strong> ${q.explain}
                    </div>
                </div>
            `).join('')}
        </div>
    `).join('');
}

function selectPart5Answer(qId, oIdx) {
    p5Answers[qId] = oIdx;
    
    let targetQ = null;
    part5Data.forEach(p => {
        const found = p.questions.find(q => q.id === qId);
        if (found) targetQ = found;
    });
    if (!targetQ) return;

    targetQ.options.forEach((_, idx) => {
        const b = document.getElementById(`optBtn_p5_${qId}_${idx}`);
        if (!b) return;
        b.classList.remove('selected', 'correct', 'wrong');
        if (idx === oIdx) {
            b.classList.add('selected');
            if (oIdx === targetQ.correct) b.classList.add('correct');
            else b.classList.add('wrong');
        } else if (idx === targetQ.correct) {
            b.classList.add('correct');
        }
    });

    const exp = document.getElementById(`p5_exp_${qId}`);
    if (exp) exp.style.display = 'block';

    calculateTotalScore();
    saveMiniCheckpoint();
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

            <div class="trans-viet-box">
                🇻🇳 <strong>Tiếng Việt:</strong> ${item.vi}
            </div>

            <div style="font-size: 0.88rem; color: var(--gray-600); margin: 8px 0;">
                💡 <strong>Từ khóa & Gợi ý:</strong> <span class="jp-text">${item.hint}</span>
            </div>

            <textarea id="trans_input_${item.id}" class="trans-textarea jp-text" placeholder="Gõ câu dịch tiếng Nhật của bạn vào đây..." oninput="handleTransInput(${item.id})"></textarea>

            <div style="margin-top: 10px; display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
                <button class="btn-check-arrange" onclick="toggleModelAnswer(${item.id})" style="background: #e0e7ff; color: #3730a3; border-color: #c7d2fe; font-weight:700;">
                    👁️ Hiện / Ẩn Đáp Án Mẫu & Phân Tích
                </button>
                <div style="font-size: 0.85rem; color: var(--gray-600);">Sau khi so sánh, tự chọn mức điểm đạt được:</div>
                <div style="display: flex; gap: 6px;">
                    <button class="word-chip" id="p6_score_0_${item.id}" onclick="setPart6Score(${item.id}, 0)" style="font-size:0.85rem; padding:4px 12px;">0đ</button>
                    <button class="word-chip" id="p6_score_15_${item.id}" onclick="setPart6Score(${item.id}, 1.5)" style="font-size:0.85rem; padding:4px 12px;">1.5đ</button>
                    <button class="word-chip" id="p6_score_25_${item.id}" onclick="setPart6Score(${item.id}, 2.5)" style="font-size:0.85rem; padding:4px 12px;">2.5đ</button>
                    <button class="word-chip" id="p6_score_375_${item.id}" onclick="setPart6Score(${item.id}, 3.75)" style="font-size:0.85rem; padding:4px 12px;">3.75đ</button>
                </div>
            </div>

            <div class="trans-model-box" id="p6_model_${item.id}">
                <div style="font-weight: 800; color: #1e1b4b; margin-bottom: 6px;">🎯 Đáp Án Mẫu Chuẩn:</div>
                <div class="jp-text" style="font-size: 1.15rem; font-weight: 700; color: #166534; margin-bottom: 4px;">
                    ${item.modelSentence}
                </div>
                <div class="jp-text" style="font-size: 0.95rem; color: var(--gray-600); margin-bottom: 10px;">
                    Cách đọc Kana: ${item.modelKana}
                </div>

                <div style="font-size: 0.88rem; font-weight: 700; color: #1e1b4b; margin-bottom: 4px;">🔍 Bóc Tách Thành Phần Ngữ Pháp:</div>
                <ul class="breakdown-list">
                    ${item.breakdown.map(b => `
                        <li class="breakdown-item">
                            <span class="breakdown-part jp-text">${b.part}</span>: <span>${b.role}</span>
                        </li>
                    `).join('')}
                </ul>
            </div>
        </div>
    `).join('');
}

function handleTransInput(qId) {
    saveMiniCheckpoint();
}

function toggleModelAnswer(qId) {
    const box = document.getElementById(`p6_model_${qId}`);
    if (!box) return;
    box.style.display = (box.style.display === 'block') ? 'none' : 'block';
    saveMiniCheckpoint();
}

function setPart6Score(qId, score) {
    p6SelfScores[qId] = score;

    [0, 1.5, 2.5, 3.75].forEach(val => {
        const strVal = String(val).replace('.', '');
        const b = document.getElementById(`p6_score_${strVal}_${qId}`);
        if (!b) return;
        b.classList.remove('selected');
        b.style.background = '';
        b.style.color = '';
        b.style.borderColor = '';
        if (val === score) {
            b.classList.add('selected');
            b.style.background = '#4f46e5';
            b.style.color = '#ffffff';
            b.style.borderColor = '#4f46e5';
        }
    });

    calculateTotalScore();
    saveMiniCheckpoint();
}

// ==========================================
// SCORING ENGINE & MODAL
// ==========================================
function calculateTotalScore() {
    let score = 0;

    // Part 1: 10 questions * 2.5 = 25 pts
    part1Data.forEach(item => {
        if (p1Answers[item.id] !== undefined && p1Answers[item.id] === item.correct) {
            score += 2.5;
        }
    });

    // Part 2: 5 questions * 3 = 15 pts
    part2Data.forEach(item => {
        if (p2Graded[item.id] === true) {
            score += 3.0;
        }
    });

    // Part 3: 5 questions * 3 = 15 pts
    part3Data.forEach(item => {
        if (p3Graded[item.id] === true) {
            score += 3.0;
        }
    });

    // Part 4: 4 questions * 2.5 = 10 pts
    part4Data.forEach(item => {
        if (p4Graded[item.id] === true) {
            score += 2.5;
        }
    });

    // Part 5: 4 questions * 5 = 20 pts
    part5Data.forEach(p => {
        p.questions.forEach(q => {
            if (p5Answers[q.id] !== undefined && p5Answers[q.id] === q.correct) {
                score += 5.0;
            }
        });
    });

    // Part 6: 4 questions * up to 3.75 = 15 pts
    part6Data.forEach(item => {
        if (p6SelfScores[item.id] !== undefined) {
            score += Number(p6SelfScores[item.id]);
        }
    });

    const totalRounded = Math.round(score * 10) / 10;
    const scoreDisplay = document.getElementById('totalScoreDisplay');
    if (scoreDisplay) scoreDisplay.innerText = totalRounded;

    const p1Count = Object.keys(p1Answers).length;
    const p2Count = Object.keys(p2Graded).length;
    const p3Count = Object.keys(p3Graded).length;
    const p4Count = Object.keys(p4Selected).length;
    const p5Count = Object.keys(p5Answers).length;
    const p6Count = Object.keys(p6SelfScores).length;
    const answeredTotal = p1Count + p2Count + p3Count + p4Count + p5Count + p6Count;
    const progEl = document.getElementById('quizProgressText');
    if (progEl) {
        progEl.innerText = `Hoàn thành: ${answeredTotal}/32 câu • Tổng điểm hiện tại: ${totalRounded} / 100đ`;
    }

    return totalRounded;
}

function submitAndGradeExam() {
    const finalScore = calculateTotalScore();
    let title = "Kết Quả Bài Thi Thử A2.2 Bài 1–4";
    let emoji = "🎉";
    let feedback = "";

    if (finalScore >= 90) {
        emoji = "🥇";
        title = "Xuất Sắc! Năng Lực A2.2 Rất Vững Vàng";
        feedback = `Chúc mừng bạn! Đạt ${finalScore}/100 điểm. Bạn đã nắm rất chắc các cấu trúc Nという意味, bổ nghĩa danh từ, phán đoán 〜そう, 〜ので và 〜てはいけません. Tự tin bước vào kỳ thi Mini Test sắp tới nhé!`;
    } else if (finalScore >= 75) {
        emoji = "🥈";
        title = "Khá Giỏi! Nắm Vững Kiến Thức Cốt Lõi";
        feedback = `Bạn đạt ${finalScore}/100 điểm. Hãy kiểm tra lại các câu sai ở phần Chia thể, Sắp xếp câu hoặc Cẩm nang bỏ túi để tránh các bẫy nhỏ về tính từ な nhé.`;
    } else if (finalScore >= 50) {
        emoji = "🥉";
        title = "Đạt Yêu Cầu - Cần Ôn Luyện Thêm";
        feedback = `Bạn đạt ${finalScore}/100 điểm. Nên đọc lại Tab 1 Lý Thuyết và Tab 5 Cẩm Nang Bỏ Túi, đặc biệt là các dạng chuyển đổi phó từ (〜く／〜に) và cấm đoán Vてはいけません.`;
    } else {
        emoji = "💪";
        title = "Cần Nỗ Lực Ôn Lại Trọng Tâm";
        feedback = `Bạn đạt ${finalScore}/100 điểm. Hãy dành thời gian xem lại lý thuyết từng bài, ôn lại từ vựng qua Quizlet ở Tab 2 rồi thử sức làm lại bài thi nhé!`;
    }

    document.getElementById('modalEmoji').innerText = emoji;
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalScoreDisplay').innerText = `${finalScore} / 100 Điểm`;
    document.getElementById('modalFeedback').innerText = feedback;
    document.getElementById('scoreModal').style.display = 'flex';
}

function closeScoreModal() {
    document.getElementById('scoreModal').style.display = 'none';
}

function resetExamSuite() {
    if (!confirm("Bạn có chắc chắn muốn làm lại toàn bộ đề thi từ đầu không?")) return;
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

    // Reset UI
    renderPart1();
    renderPart2();
    renderPart3();
    renderPart4();
    renderPart5();
    renderPart6();

    const scoreDisplay = document.getElementById('totalScoreDisplay');
    if (scoreDisplay) scoreDisplay.innerText = '0';
    const progEl = document.getElementById('quizProgressText');
    if (progEl) progEl.innerText = 'Hoàn thành: 0/32 câu • Tổng điểm hiện tại: 0 / 100đ';

    try { localStorage.removeItem(MINI_A2_2_1_4_CP_KEY); } catch (e) {}
    showToast("Đã làm mới toàn bộ bài thi!");
}

// ==========================================
// VOCABULARY TAB LOGIC
// ==========================================
function renderVocab(list) {
    const container = document.getElementById('vocabContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy từ vựng phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map(item => `
        <div class="vocab-card">
            <div class="vocab-top">
                <div>
                    <span class="vocab-badge">${item.lessonName}</span>
                    <div class="vocab-jp jp-text" style="margin-top: 4px;">${item.kanji || item.kana}</div>
                    ${item.kanji && item.kanji !== item.kana ? `<div class="vocab-sub jp-text">${item.kana}</div>` : ''}
                    <div class="vocab-sub">${item.romaji}</div>
                </div>
                <button class="sound-btn" onclick="speakText('${(item.kana || item.jp || item.kanji || '').replace(/'/g, "\\'")}')" title="Nghe cách đọc Kana">🔊</button>
            </div>
            <div class="vocab-vi ${isMeaningHidden ? 'hidden-meaning' : ''}" onclick="this.classList.toggle('hidden-meaning')">
                ${item.vi}
            </div>
        </div>
    `).join('');
}

function filterVocab(lesson, btn) {
    currentVocabFilter = lesson;
    const allBtns = document.querySelectorAll('#vocabFilterGroup .filter-btn');
    allBtns.forEach(b => b.classList.remove('active'));
    if (btn) {
        btn.classList.add('active');
    } else {
        const found = Array.from(allBtns).find(b => {
            const oc = b.getAttribute('onclick') || '';
            return oc.includes(`'${lesson}'`) || oc.includes(`"${lesson}"`);
        });
        if (found) found.classList.add('active');
    }
    applyVocabFilter();
    saveMiniCheckpoint();
}

function handleVocabSearch() {
    applyVocabFilter();
}

function applyVocabFilter() {
    const keyword = (document.getElementById('vocabSearchInput').value || '').trim().toLowerCase();
    let filtered = rawVocab;
    if (currentVocabFilter !== 'ALL') {
        filtered = filtered.filter(w => w.l === currentVocabFilter);
    }
    if (keyword) {
        filtered = filtered.filter(w => 
            (w.kanji && w.kanji.toLowerCase().includes(keyword)) ||
            (w.kana && w.kana.toLowerCase().includes(keyword)) ||
            (w.romaji && w.romaji.toLowerCase().includes(keyword)) ||
            (w.vi && w.vi.toLowerCase().includes(keyword))
        );
    }
    currentFilteredVocab = filtered;
    const countEl = document.getElementById('quizletVocabCount');
    if (countEl) countEl.innerText = filtered.length;
    renderVocab(filtered);
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
    saveMiniCheckpoint();
}

function cleanJpTermForQuizlet(str) {
    if (!str) return "";
    let s = str;
    s = s.replace(/[~～…\.]/g, "");
    s = s.replace(/^[nN]が/g, "");
    s = s.replace(/^[nNpPvV][をにへとがで]/g, "");
    s = s.replace(/てください$/g, "");
    s = s.replace(/\([^)]*を\)/g, "").replace(/（[^）]*を）/g, "");
    s = s.replace(/\(お\)/g, "お").replace(/（お）/g, "お");
    s = s.replace(/\(します\)/g, "します").replace(/（します）/g, "します");
    s = s.replace(/[\(\)（）]/g, "");
    if (s.includes("/") || s.includes("／")) {
        s = s.split(/[\/／]/)[0];
    }
    s = s.replace(/[。、,，\?？！!]/g, "");
    s = s.replace(/[\s　]+/g, "");
    return s.trim();
}

function formatQuizletVocabLine(item, delimiter = '\t', formatType = 'kana') {
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
        const term = cleanJpTermForQuizlet(item.kana || item.kanji);
        return `${term}${delimiter}${def}`;
    }
}

function copyVocabQuizletFormat() {
    copyFilteredQuizlet('\t', 'kana');
}

function copyVocabColonFormat() {
    copyFilteredQuizlet(' : ', 'kana');
}

function copyVocabCombinedFormat() {
    copyFilteredQuizlet('\t', 'combined');
}

function copyVocabKanjiOnlyFormat() {
    copyFilteredQuizlet('\t', 'kanji');
}

function copyFullVocabAllFormat() {
    const text = rawVocab.map(item => formatQuizletVocabLine(item, '\t', 'kana')).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy toàn bộ 81 từ chuẩn Quizlet Tab!`);
    }).catch(() => {
        fallbackCopyText(text, 81, 'Quizlet Tab');
    });
}

function copyFilteredQuizlet(delimiter = '\t', formatType = 'kana') {
    if (!currentFilteredVocab || currentFilteredVocab.length === 0) {
        showToast("Không có từ vựng nào để sao chép!");
        return;
    }
    const text = currentFilteredVocab.map(item => formatQuizletVocabLine(item, delimiter, formatType)).join('\n');
    let label = 'Quizlet Tab (Kana [Tab] Nghĩa)';
    if (delimiter.includes(':')) label = 'Dấu hai chấm (Kana : Nghĩa)';
    else if (formatType === 'combined') label = 'Kèm Kanji & Kana';
    else if (formatType === 'kanji') label = 'Kanji';

    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredVocab.length} từ chuẩn ${label}!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredVocab.length, label);
    });
}

// ==========================================
// KANJI TAB LOGIC
// ==========================================
function renderKanji(list) {
    const container = document.getElementById('kanjiContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy chữ Hán phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map(item => {
        const rawChar = item.char || '';
        const charLen = rawChar.length;
        let lenClass = 'char-len-1';
        let charBoxHtml = rawChar;

        if (rawChar.includes('（') && rawChar.includes('）')) {
            lenClass = 'char-len-long';
            const parts = rawChar.split('（');
            const mainWord = parts[0];
            const subWord = parts[1].replace('）', '');
            charBoxHtml = `<span class="char-main">${mainWord}</span><span class="char-sub">（${subWord}）</span>`;
        } else if (charLen >= 4) {
            lenClass = 'char-len-4';
        } else if (charLen === 3) {
            lenClass = 'char-len-3';
        } else if (charLen === 2) {
            lenClass = 'char-len-2';
        }

        const safeChar = rawChar.replace(/'/g, "\\'");
        const hiraganaText = item.hiragana || '';

        return `
        <div class="kanji-card">
            <div class="kanji-header">
                <div class="kanji-char-box jp-text ${lenClass}">${charBoxHtml}</div>
                <div class="kanji-meta">
                    <div class="kanji-title-row">
                        <div class="kanji-hv">
                            <span class="hv-name">${item.hv}</span>
                            ${hiraganaText ? `<span class="kanji-reading-pill jp-text">(${hiraganaText})</span>` : ''}
                        </div>
                        <button type="button" class="kanji-copy-btn" onclick="copySingleKanji('${safeChar}')" title="Sao chép chữ Hán này">
                            📋 Copy
                        </button>
                    </div>
                    <div class="kanji-meaning">${item.meaning}</div>
                    <div class="kanji-sub-row">
                        <span class="kanji-tag">${item.lessonName}</span>
                        <span class="kanji-tag">${item.strokes} nét</span>
                        <span class="kanji-tag kanji-tag-reading">Đọc: ${hiraganaText}</span>
                    </div>
                </div>
            </div>

            <div class="kanji-detail-box">
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
        `;
    }).join('');
}

function filterKanji(lesson, btn) {
    currentKanjiFilter = lesson;
    const allBtns = document.querySelectorAll('#kanjiFilterGroup .filter-btn');
    allBtns.forEach(b => b.classList.remove('active'));
    if (btn) {
        btn.classList.add('active');
    } else {
        const found = Array.from(allBtns).find(b => {
            const oc = b.getAttribute('onclick') || '';
            return oc.includes(`'${lesson}'`) || oc.includes(`"${lesson}"`);
        });
        if (found) found.classList.add('active');
    }
    applyKanjiFilter();
    saveMiniCheckpoint();
}

function handleKanjiSearch() {
    applyKanjiFilter();
}

function applyKanjiFilter() {
    const keyword = (document.getElementById('kanjiSearchInput').value || '').trim().toLowerCase();
    let filtered = rawKanji;
    if (currentKanjiFilter !== 'ALL') {
        filtered = filtered.filter(k => k.lesson === currentKanjiFilter);
    }
    if (keyword) {
        filtered = filtered.filter(k => 
            k.char.includes(keyword) ||
            k.hv.toLowerCase().includes(keyword) ||
            k.meaning.toLowerCase().includes(keyword) ||
            (k.hiragana && k.hiragana.includes(keyword))
        );
    }
    currentFilteredKanji = filtered;
    const countEl = document.getElementById('quizletKanjiCount');
    if (countEl) countEl.innerText = filtered.length;
    renderKanji(filtered);
}

function formatKanjiLine(item, delimiter = ' : ') {
    const ch = item.char;
    const mean = item.shortMeaning || item.meaning;
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
    const text = currentFilteredKanji.map(k => formatKanjiLine(k, ' : ')).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredKanji.length} chữ Hán (Dấu hai chấm)!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredKanji.length, 'Dấu hai chấm');
    });
}

function copyKanjiQuizletTabFormat() {
    if (!currentFilteredKanji || currentFilteredKanji.length === 0) {
        showToast("Không có chữ Hán nào để sao chép!");
        return;
    }
    const text = currentFilteredKanji.map(k => formatKanjiLine(k, '\t')).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredKanji.length} chữ Hán chuẩn Quizlet Tab!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredKanji.length, 'Quizlet Tab');
    });
}

function copySingleKanji(char) {
    const item = rawKanji.find(k => k.char === char);
    if (!item) return;
    const line = formatKanjiLine(item, ' : ');
    navigator.clipboard.writeText(line).then(() => {
        showToast(`✅ Đã copy: ${line}`);
    }).catch(() => {
        fallbackCopyText(line, 1, line);
    });
}

// ==========================================
// UTILITIES & CHECKPOINT RESTORATION
// ==========================================
function fallbackCopyText(text, count, label) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast(`✅ Đã copy ${count} mục (${label})!`);
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
    setTimeout(() => { toast.style.display = 'none'; }, 2600);
}

function restoreMiniCheckpoint() {
    try {
        const raw = localStorage.getItem(MINI_A2_2_1_4_CP_KEY);
        if (!raw) return;
        const data = JSON.parse(raw);
        if (!data) return;

        isRestoringMini = true;

        if (data.currentTab) {
            currentTab = data.currentTab;
            switchTab(data.currentTab);
        }
        if (data.isMeaningHidden !== undefined) {
            isMeaningHidden = !data.isMeaningHidden;
            toggleHideMeaning();
        }
        if (data.totalSeconds !== undefined) {
            totalSeconds = data.totalSeconds;
            updateTimerDisplay();
        }
        if (data.isTimerRunning !== undefined) {
            isTimerRunning = data.isTimerRunning;
            const btn = document.getElementById('timerToggleBtn');
            if (btn) btn.innerHTML = isTimerRunning ? '⏸️ Tạm dừng' : '▶️ Tiếp tục';
        }
        if (data.currentVocabFilter) {
            filterVocab(data.currentVocabFilter);
        }
        if (data.currentKanjiFilter) {
            filterKanji(data.currentKanjiFilter);
        }

        // Restore Part 1
        if (data.p1Answers) {
            p1Answers = data.p1Answers;
            Object.keys(p1Answers).forEach(qId => {
                selectPart1Answer(Number(qId), p1Answers[qId]);
            });
        }

        // Restore Part 2
        if (data.p2Selected) {
            p2Selected = data.p2Selected;
            Object.keys(p2Selected).forEach(qId => {
                updatePart2UI(Number(qId));
                checkPart2Complete(Number(qId));
            });
        }

        // Restore Part 3
        if (data.p3Inputs) {
            Object.keys(data.p3Inputs).forEach(qId => {
                const inp = document.getElementById(`p3_input_${qId}`);
                if (inp) {
                    inp.value = data.p3Inputs[qId];
                    if (data.p3Graded && data.p3Graded[qId] !== undefined) {
                        gradePart3Question(Number(qId));
                    }
                }
            });
        }

        // Restore Part 4
        if (data.p4Selected) {
            p4Selected = data.p4Selected;
            Object.keys(p4Selected).forEach(qId => {
                selectPart4Answer(Number(qId), p4Selected[qId]);
            });
        }

        // Restore Part 5
        if (data.p5Answers) {
            p5Answers = data.p5Answers;
            Object.keys(p5Answers).forEach(qId => {
                selectPart5Answer(Number(qId), p5Answers[qId]);
            });
        }

        // Restore Part 6
        if (data.p6Drafts) {
            Object.keys(data.p6Drafts).forEach(qId => {
                const ta = document.getElementById(`trans_input_${qId}`);
                if (ta) ta.value = data.p6Drafts[qId];
            });
        }
        if (data.p6ModelsOpen) {
            Object.keys(data.p6ModelsOpen).forEach(qId => {
                const mb = document.getElementById(`p6_model_${qId}`);
                if (mb && data.p6ModelsOpen[qId]) mb.style.display = 'block';
            });
        }
        if (data.p6SelfScores) {
            p6SelfScores = data.p6SelfScores;
            Object.keys(p6SelfScores).forEach(qId => {
                setPart6Score(Number(qId), p6SelfScores[qId]);
            });
        }

        calculateTotalScore();
    } catch (e) {
    } finally {
        isRestoringMini = false;
    }
}

// Initial Boot
document.addEventListener('DOMContentLoaded', () => {
    renderPart1();
    renderPart2();
    renderPart3();
    renderPart4();
    renderPart5();
    renderPart6();

    renderVocab(rawVocab);
    renderKanji(rawKanji);

    startTimer();
    restoreMiniCheckpoint();
});
