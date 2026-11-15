/* CONTROLLER FOR TONG HOP JLPT A2.1 (BAI 11 - 18) EXAMS */

const STORAGE_KEY_PREFIX = "marugoto_tonghop_11_18_draft_";
const HISTORY_STORAGE_KEY = "marugoto_tonghop_11_18_history_v1";
const ACTIVE_EXAM_STORAGE_KEY = "marugoto_tonghop_11_18_active_code_v1";

function getInitialExamCode() {
    const hash = (window.location.hash || "").replace("#", "").trim().toUpperCase();
    if (hash && typeof window.DE_THI_TONG_HOP_DATA !== 'undefined' && window.DE_THI_TONG_HOP_DATA.some(e => e.code === hash)) {
        return hash;
    }
    try {
        const saved = localStorage.getItem(ACTIVE_EXAM_STORAGE_KEY);
        if (saved && typeof window.DE_THI_TONG_HOP_DATA !== 'undefined' && window.DE_THI_TONG_HOP_DATA.some(e => e.code === saved)) {
            return saved;
        }
    } catch (e) {}
    return "DEGOC";
}

let currentExamCode = getInitialExamCode();
let userAnswers = {}; // { [qId]: { value, starOrder, isCorrect, checked } }
let timerSeconds = 45 * 60;
let timerInterval = null;
let isTimerRunning = false;
let isImmediateMode = true; // Mặc định mở chế độ ôn luyện (hiện giải thích tức thì)
let isExamSubmitted = false;
let currentPaletteFilter = 'all';

// Audio pronunciation helper
function speakAudio(text) {
    if (!text) return;
    const cleanText = text.replace(/<[^>]*>/g, '').replace(/[（(].*?[)）]/g, '').trim();
    if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
        const utter = new SpeechSynthesisUtterance(cleanText);
        utter.lang = 'ja-JP';
        utter.rate = 0.88;
        window.speechSynthesis.speak(utter);
    }
}

// 1. DOM Ready
document.addEventListener("DOMContentLoaded", () => {
    currentExamCode = getInitialExamCode();
    initExamTabs();
    loadExam(currentExamCode);
});

window.addEventListener("hashchange", () => {
    const hash = (window.location.hash || "").replace("#", "").trim().toUpperCase();
    if (hash && hash !== currentExamCode && typeof window.DE_THI_TONG_HOP_DATA !== 'undefined' && window.DE_THI_TONG_HOP_DATA.some(e => e.code === hash)) {
        switchExam(hash);
    }
});

// 2. Tabs Initialization
function initExamTabs() {
    const container = document.getElementById("examCodeTabsContainer");
    if (!container || !window.DE_THI_TONG_HOP_DATA) return;

    container.innerHTML = window.DE_THI_TONG_HOP_DATA.map(exam => {
        const isActive = (exam.code === currentExamCode);
        const isDeGoc = (exam.code === "DEGOC");
        const activeClass = isDeGoc ? "active-degoc" : "active";
        return `
            <button type="button" class="code-tab-btn ${isActive ? activeClass : ''}" id="tab_btn_${exam.code}" onclick="switchExam('${exam.code}')">
                <span class="code-tab-title">${isDeGoc ? '📑 ĐỀ GỐC PDF' : exam.code}</span>
                <span class="code-tab-sub">${isDeGoc ? 'Bản Chuẩn 11-18' : exam.name.split('(')[0].replace('Mã Đề', 'Đề')}</span>
            </button>
        `;
    }).join("");
}

function switchExam(code) {
    if (code === currentExamCode) return;
    saveCurrentDraft();
    currentExamCode = code;
    try {
        localStorage.setItem(ACTIVE_EXAM_STORAGE_KEY, code);
    } catch(e) {}
    window.location.hash = code;

    // Update active tab buttons
    document.querySelectorAll(".code-tab-btn").forEach(btn => {
        btn.classList.remove("active");
        btn.classList.remove("active-degoc");
    });
    const targetBtn = document.getElementById(`tab_btn_${code}`);
    if (targetBtn) {
        targetBtn.classList.add(code === "DEGOC" ? "active-degoc" : "active");
    }

    loadExam(code);
    window.scrollTo({ top: 380, behavior: 'smooth' });
}

// 3. Load Exam
function getCurrentExam() {
    return (window.DE_THI_TONG_HOP_DATA || []).find(e => e.code === currentExamCode) || window.DE_THI_TONG_HOP_DATA[0];
}

function loadExam(code) {
    const exam = getCurrentExam();
    if (!exam) return;

    // Header info
    const tagEl = document.getElementById("currentExamTag");
    if (tagEl) tagEl.innerText = exam.tag || exam.code;
    const nameEl = document.getElementById("currentExamName");
    if (nameEl) nameEl.innerText = exam.name;
    const descEl = document.getElementById("currentExamDesc");
    if (descEl) descEl.innerText = exam.desc;

    // Restore answers
    isExamSubmitted = false;
    userAnswers = {};
    try {
        const saved = localStorage.getItem(STORAGE_KEY_PREFIX + code);
        if (saved) {
            userAnswers = JSON.parse(saved);
        }
    } catch (e) {}

    renderExamDOM(exam);
    renderPalette(exam);
    updateProgressCounter();

    // Reset Timer
    resetTimer();
}

function saveCurrentDraft() {
    try {
        localStorage.setItem(STORAGE_KEY_PREFIX + currentExamCode, JSON.stringify(userAnswers));
    } catch (e) {}
}

// 4. Render Exam DOM
function renderExamDOM(exam) {
    const container = document.getElementById("examSectionsContainer");
    if (!container) return;

    let html = "";
    exam.sections.forEach(sec => {
        html += `
            <div class="exam-section-card" id="${sec.id}">
                <div class="section-card-header">
                    <div>
                        <span class="section-badge">${sec.badge || ''}</span>
                        <h3 class="section-title">${sec.partTitle}</h3>
                        <p class="section-desc">${sec.partDesc}</p>
                    </div>
                </div>
        `;

        sec.groups.forEach((grp, gIdx) => {
            html += `
                <div class="group-card">
                    <div class="group-header">
                        <h4 class="group-title">${grp.groupTitle}</h4>
                        <div class="group-instruction">${grp.groupInstruction}</div>
                    </div>
            `;

            if (grp.passage) {
                html += `
                    <div class="reading-passage-box">
                        <div class="reading-passage-header">
                            <span class="reading-passage-tag">📖 BÀI ĐỌC HIỂU</span>
                            <button type="button" class="btn-toggle-passage-vi" onclick="togglePassageVi('${sec.id}_${gIdx}')">
                                👁️ Xem Dịch Nghĩa Đoạn Văn
                            </button>
                        </div>
                        <div class="reading-passage-content jp-text">${grp.passage.replace(/\n/g, '<br>')}</div>
                        <div class="reading-passage-vi" id="passage_vi_${sec.id}_${gIdx}" style="display:none;">
                            ${(grp.passageVi || '').replace(/\n/g, '<br>')}
                        </div>
                    </div>
                `;
            }

            html += `<div class="questions-list">`;
            grp.items.forEach(item => {
                html += renderQuestionItem(item);
            });
            html += `</div></div>`;
        });

        html += `</div>`;
    });

    container.innerHTML = html;

    // Apply saved answers states
    exam.sections.forEach(sec => {
        sec.groups.forEach(grp => {
            grp.items.forEach(item => {
                restoreItemState(item);
            });
        });
    });
}

function renderQuestionItem(item) {
    const ans = userAnswers[item.id] || {};
    let qHtml = `
        <div class="q-item-card" id="q_card_${item.id}">
            <div class="q-meta-row">
                <span class="q-number-badge">CÂU ${item.id}</span>
                <div style="display:flex; align-items:center; gap:6px;">
                    ${item.promptVi ? `
                        <button type="button" class="btn-hint-vi" id="btn_hint_${item.id}" onclick="toggleSingleVi(${item.id})">
                            👁️ Dịch
                        </button>
                    ` : ''}
                    <button type="button" class="btn-speak" onclick="speakAudio('${item.prompt.replace(/'/g, "\\'")}')">
                        🔊 Phát âm
                    </button>
                </div>
            </div>
    `;

    if (item.type === "mc") {
        qHtml += `
            <div class="q-prompt-jp jp-text">${item.prompt}</div>
            <div class="q-prompt-vi" id="q_prompt_vi_${item.id}" style="display:none;">${item.promptVi || ''}</div>
            <div class="options-grid">
                ${item.options.map((opt, oIdx) => `
                    <label class="option-label" id="opt_lbl_${item.id}_${oIdx}" onclick="handleSelectOption(${item.id}, ${oIdx})">
                        <input type="radio" name="opt_${item.id}" value="${oIdx}">
                        <div class="option-radio-mark">${oIdx + 1}</div>
                        <span class="option-text-jp jp-text">${opt}</span>
                    </label>
                `).join("")}
            </div>
        `;
    } else if (item.type === "star") {
        const parts = item.parts || item.options || [];
        qHtml += `
            <div class="q-prompt-jp jp-text">${item.prompt}</div>
            <div class="q-prompt-vi" id="q_prompt_vi_${item.id}" style="display:none;">${item.promptVi || ''}</div>
            <div class="star-container">
                <div class="star-slots-row">
                    ${[0, 1, 2, 3].map(slotIdx => {
                        const isStar = (slotIdx === 2); // 3rd slot is star in standard test
                        return `
                            <div class="star-slot ${isStar ? 'slot-star' : ''}" id="star_slot_${item.id}_${slotIdx}" onclick="removeStarSlot(${item.id}, ${slotIdx})">
                                ${isStar ? '★ ' : ''}Vị trí ${slotIdx + 1}
                            </div>
                        `;
                    }).join("")}
                </div>
                <div style="font-size:0.82rem; font-weight:700; color:#92400e; margin: 8px 0 6px 0;">
                    👉 Bấm lần lượt 4 cụm từ dưới đây để điền vào 4 vị trí:
                </div>
                <div class="star-pool-box" id="star_pool_${item.id}">
                    ${parts.map((p, pIdx) => `
                        <button type="button" class="star-pill jp-text" id="star_pill_${item.id}_${pIdx}" onclick="placeStarPart(${item.id}, ${pIdx})">
                            <strong>[${pIdx + 1}]</strong> ${p}
                        </button>
                    `).join("")}
                </div>
                <div class="star-actions" style="margin-top: 6px;">
                    <button type="button" class="btn-reset-star" onclick="resetStarOrder(${item.id})">
                        🔄 Xếp lại từ đầu
                    </button>
                </div>
            </div>
        `;
    }

    qHtml += `
        <div class="explain-box" id="explain_box_${item.id}" style="display:none;">
            <div class="explain-header">
                <span>💡 GIẢI THÍCH CHI TIẾT CÂU ${item.id}</span>
                <span class="badge-rule">ĐÁP ÁN: ${item.type === 'star' ? ('Vị trí ★ là [' + (item.correct + 1) + ']') : ('Đáp án ' + (item.correct + 1))}</span>
            </div>
            <div class="explain-body">
                ${item.explain || 'Đang cập nhật giải thích...'}
            </div>
        </div>
    </div>`;

    return qHtml;
}

// 5. User Selection & Interaction
function handleSelectOption(qId, oIdx) {
    if (isExamSubmitted) return;

    const exam = getCurrentExam();
    let qItem = null;
    exam.sections.forEach(s => s.groups.forEach(g => g.items.forEach(it => {
        if (it.id === qId) qItem = it;
    })));
    if (!qItem) return;

    const isCorrect = (oIdx === qItem.correct);
    userAnswers[qId] = {
        value: oIdx,
        isCorrect: isCorrect,
        checked: true
    };

    saveCurrentDraft();
    updateOptionUI(qItem, oIdx, isCorrect);
    updateProgressCounter();
    updatePaletteCell(qId);
}

function updateOptionUI(qItem, selectedIdx, isCorrect) {
    const qId = qItem.id;
    // Highlight labels
    qItem.options.forEach((opt, idx) => {
        const lbl = document.getElementById(`opt_lbl_${qId}_${idx}`);
        if (!lbl) return;
        lbl.classList.remove("selected", "opt-correct", "opt-wrong");

        if (idx === selectedIdx) {
            lbl.classList.add("selected");
            const radio = lbl.querySelector("input[type=radio]");
            if (radio) radio.checked = true;
        }

        if (isImmediateMode || isExamSubmitted) {
            if (idx === qItem.correct) {
                lbl.classList.add("opt-correct");
            } else if (idx === selectedIdx && !isCorrect) {
                lbl.classList.add("opt-wrong");
            }
        }
    });

    // Reveal explanation in immediate mode
    const expBox = document.getElementById(`explain_box_${qId}`);
    if (expBox) {
        if (isImmediateMode || isExamSubmitted) {
            expBox.style.display = "block";
        }
    }
}

// Star Order Handlers
function placeStarPart(qId, partIdx) {
    if (isExamSubmitted) return;
    const ans = userAnswers[qId] || { starOrder: [] };
    const order = ans.starOrder ? ans.starOrder.slice() : [];
    if (order.includes(partIdx)) return;
    if (order.length >= 4) return;

    order.push(partIdx);
    updateStarUI(qId, order);
}

function removeStarSlot(qId, slotIdx) {
    if (isExamSubmitted) return;
    const ans = userAnswers[qId];
    if (!ans || !ans.starOrder) return;
    const order = ans.starOrder.slice();
    if (slotIdx < order.length) {
        order.splice(slotIdx, 1);
        updateStarUI(qId, order);
    }
}

function resetStarOrder(qId) {
    if (isExamSubmitted) return;
    updateStarUI(qId, []);
}

function updateStarUI(qId, order) {
    const exam = getCurrentExam();
    let qItem = null;
    exam.sections.forEach(s => s.groups.forEach(g => g.items.forEach(it => {
        if (it.id === qId) qItem = it;
    })));
    if (!qItem) return;

    const parts = qItem.parts || qItem.options || [];

    // Update slots
    [0, 1, 2, 3].map(slotIdx => {
        const slotEl = document.getElementById(`star_slot_${qId}_${slotIdx}`);
        if (!slotEl) return;
        if (slotIdx < order.length) {
            const pIdx = order[slotIdx];
            slotEl.innerHTML = `<span class="slot-filled jp-text"><strong>[${pIdx + 1}]</strong> ${parts[pIdx]}</span>`;
            slotEl.classList.add("filled");
        } else {
            const isStar = (slotIdx === 2);
            slotEl.innerHTML = `${isStar ? '★ ' : ''}Vị trí ${slotIdx + 1}`;
            slotEl.classList.remove("filled");
        }
    });

    // Update pool pills
    parts.forEach((p, pIdx) => {
        const pill = document.getElementById(`star_pill_${qId}_${pIdx}`);
        if (!pill) return;
        if (order.includes(pIdx)) {
            pill.classList.add("used");
            pill.disabled = true;
        } else {
            pill.classList.remove("used");
            pill.disabled = false;
        }
    });

    // Check completion
    if (order.length === 4) {
        const starSelectedPart = order[2]; // position 3 is star
        const isCorrect = (starSelectedPart === qItem.correct);
        userAnswers[qId] = {
            starOrder: order,
            value: starSelectedPart,
            isCorrect: isCorrect,
            checked: true
        };
        const expBox = document.getElementById(`explain_box_${qId}`);
        if (expBox && (isImmediateMode || isExamSubmitted)) {
            expBox.style.display = "block";
        }
    } else {
        delete userAnswers[qId];
        const expBox = document.getElementById(`explain_box_${qId}`);
        if (expBox && !isExamSubmitted) {
            expBox.style.display = "none";
        }
    }

    saveCurrentDraft();
    updateProgressCounter();
    updatePaletteCell(qId);
}

function restoreItemState(item) {
    const ans = userAnswers[item.id];
    if (!ans) return;

    if (item.type === "mc") {
        updateOptionUI(item, ans.value, ans.isCorrect);
    } else if (item.type === "star" && ans.starOrder) {
        updateStarUI(item.id, ans.starOrder);
    }
}

// 6. Navigation Palette
function renderPalette(exam) {
    const container = document.getElementById("paletteGridContainer");
    if (!container) return;

    let totalQ = 0;
    let buttonsHtml = "";
    exam.sections.forEach(s => s.groups.forEach(g => g.items.forEach(it => {
        totalQ++;
        const ans = userAnswers[it.id];
        let statusClass = "pal-unanswered";
        if (ans && ans.checked) {
            if (isImmediateMode || isExamSubmitted) {
                statusClass = ans.isCorrect ? "pal-correct" : "pal-wrong";
            } else {
                statusClass = "pal-answered";
            }
        }
        buttonsHtml += `
            <button type="button" class="pal-btn ${statusClass}" id="pal_btn_${it.id}" onclick="jumpToQuestion(${it.id})">
                ${it.id}
            </button>
        `;
    })));

    container.innerHTML = buttonsHtml;
}

function updatePaletteCell(qId) {
    const btn = document.getElementById(`pal_btn_${qId}`);
    if (!btn) return;
    const ans = userAnswers[qId];
    btn.className = "pal-btn";
    if (ans && ans.checked) {
        if (isImmediateMode || isExamSubmitted) {
            btn.classList.add(ans.isCorrect ? "pal-correct" : "pal-wrong");
        } else {
            btn.classList.add("pal-answered");
        }
    } else {
        btn.classList.add("pal-unanswered");
    }
    updatePaletteFilterCounts();
}

function jumpToQuestion(qId) {
    const el = document.getElementById(`q_card_${qId}`);
    if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.classList.add("highlight-card");
        setTimeout(() => el.classList.remove("highlight-card"), 1500);
    }
}

function filterPalette(type) {
    currentPaletteFilter = type;
    document.querySelectorAll(".btn-filter-tag").forEach(b => b.classList.remove("active"));
    const activeBtn = document.getElementById(`filterBtn${type.charAt(0).toUpperCase() + type.slice(1)}`);
    if (activeBtn) activeBtn.classList.add("active");

    const exam = getCurrentExam();
    exam.sections.forEach(s => s.groups.forEach(g => g.items.forEach(it => {
        const btn = document.getElementById(`pal_btn_${it.id}`);
        const card = document.getElementById(`q_card_${it.id}`);
        const ans = userAnswers[it.id];
        let show = true;

        if (type === 'wrong') {
            show = (ans && ans.checked && !ans.isCorrect);
        } else if (type === 'unanswered') {
            show = (!ans || !ans.checked);
        }

        if (btn) btn.style.display = show ? "flex" : "none";
        if (card) card.style.display = show ? "block" : "none";
    })));
}

function updatePaletteFilterCounts() {
    let wrongCount = 0;
    let answeredCount = 0;
    const exam = getCurrentExam();
    let total = 71;

    exam.sections.forEach(s => s.groups.forEach(g => g.items.forEach(it => {
        const ans = userAnswers[it.id];
        if (ans && ans.checked) {
            answeredCount++;
            if (!ans.isCorrect) wrongCount++;
        }
    })));

    const wBtn = document.getElementById("filterBtnWrong");
    if (wBtn) wBtn.innerText = `Câu sai (${wrongCount})`;
}

// 7. Counter & Progress
function updateProgressCounter() {
    const exam = getCurrentExam();
    let answered = 0;
    let total = 0;
    exam.sections.forEach(s => s.groups.forEach(g => g.items.forEach(it => {
        total++;
        if (userAnswers[it.id] && userAnswers[it.id].checked) {
            answered++;
        }
    })));

    const countEl = document.getElementById("bottomAnswerCount");
    if (countEl) countEl.innerText = `Đã làm: ${answered}/${total} câu`;

    const barEl = document.getElementById("bottomProgressBar");
    if (barEl) {
        const pct = total > 0 ? (answered / total * 100) : 0;
        barEl.style.width = `${pct}%`;
    }
}

// 8. Mode Toggle
function toggleExamMode() {
    isImmediateMode = !isImmediateMode;
    const titleEl = document.getElementById("modeTitle");
    const descEl = document.getElementById("modeDesc");
    const iconEl = document.getElementById("modeIndicatorIcon");
    const btnEl = document.getElementById("btnToggleMode");
    const timerStrip = document.getElementById("timerStrip");

    if (isImmediateMode) {
        iconEl.innerText = "🎯";
        titleEl.innerText = "Chế Độ Ôn Luyện (Hiện Lời Giải Tức Thì)";
        descEl.innerText = "Bấm chọn đáp án sẽ biết ngay đúng/sai và tự động mở khung phân tích, dịch nghĩa chi tiết.";
        btnEl.innerText = "⏱️ Chuyển Sang Thi Thử (Tính Giờ 45p)";
        if (timerStrip) timerStrip.style.display = "none";
        stopTimer();
    } else {
        iconEl.innerText = "⏱️";
        titleEl.innerText = "Chế Độ Thi Thử Tính Giờ (45 Phút)";
        descEl.innerText = "Ẩn toàn bộ đáp án và lời giải. Đồng hồ đếm ngược 45 phút đang chạy. Hãy nộp bài để xem điểm.";
        btnEl.innerText = "🎯 Chuyển Sang Ôn Luyện (Tức Thì)";
        if (timerStrip) timerStrip.style.display = "block";
        startTimer();
    }

    const exam = getCurrentExam();
    renderExamDOM(exam);
    renderPalette(exam);
}

// 9. Timer
function startTimer() {
    if (isTimerRunning) return;
    isTimerRunning = true;
    timerInterval = setInterval(() => {
        if (timerSeconds > 0) {
            timerSeconds--;
            updateTimerDisplay();
        } else {
            clearInterval(timerInterval);
            isTimerRunning = false;
            alert("⏰ Đã hết thời gian làm bài 45 phút! Hệ thống sẽ tự động nộp bài và chấm điểm.");
            submitExam();
        }
    }, 1000);
}

function stopTimer() {
    isTimerRunning = false;
    if (timerInterval) clearInterval(timerInterval);
}

function resetTimer() {
    stopTimer();
    timerSeconds = 45 * 60;
    updateTimerDisplay();
    if (!isImmediateMode) startTimer();
}

function toggleTimerPause() {
    const btn = document.getElementById("btnTimerPause");
    if (isTimerRunning) {
        stopTimer();
        if (btn) btn.innerText = "▶️ Tiếp Tục";
    } else {
        startTimer();
        if (btn) btn.innerText = "⏸️ Tạm Dừng";
    }
}

function updateTimerDisplay() {
    const clock = document.getElementById("timerClock");
    if (!clock) return;
    const m = Math.floor(timerSeconds / 60);
    const s = timerSeconds % 60;
    clock.innerText = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

// 10. Toggle Translations & Explanations
function toggleSingleVi(qId) {
    const el = document.getElementById(`q_prompt_vi_${qId}`);
    if (!el) return;
    el.style.display = (el.style.display === "none") ? "block" : "none";
}

function togglePassageVi(key) {
    const el = document.getElementById(`passage_vi_${key}`);
    if (!el) return;
    el.style.display = (el.style.display === "none") ? "block" : "none";
}

let allExplained = false;
function toggleAllExplanations() {
    allExplained = !allExplained;
    const exam = getCurrentExam();
    exam.sections.forEach(s => s.groups.forEach(g => g.items.forEach(it => {
        const box = document.getElementById(`explain_box_${it.id}`);
        const vi = document.getElementById(`q_prompt_vi_${it.id}`);
        if (box) box.style.display = allExplained ? "block" : "none";
        if (vi) vi.style.display = allExplained ? "block" : "none";
    })));
    const textEl = document.getElementById("toggleExplainText");
    if (textEl) textEl.innerText = allExplained ? "Ẩn Tất Cả Lời Giải" : "Hiện Tất Cả Lời Giải";
}

// 11. Submit Exam & Scoring
function submitExam() {
    isExamSubmitted = true;
    stopTimer();

    const exam = getCurrentExam();
    let scoreSec1 = 0; // max 25
    let scoreSec2 = 0; // max 40
    let scoreSec3 = 0; // max 20
    let scoreSec4 = 0; // max 15

    let countSec1 = 0, countSec2 = 0, countSec3 = 0, countSec4 = 0;

    exam.sections.forEach((s, sIdx) => {
        s.groups.forEach(g => {
            g.items.forEach(it => {
                const ans = userAnswers[it.id];
                const isCorr = (ans && ans.isCorrect);

                if (sIdx === 0) { // Sec 1 (22 q)
                    if (isCorr) countSec1++;
                } else if (sIdx === 1) { // Sec 2 (35 q)
                    if (isCorr) countSec2++;
                } else if (sIdx === 2) { // Sec 3 (8 q)
                    if (isCorr) countSec3++;
                } else if (sIdx === 3) { // Sec 4 (6 q)
                    if (isCorr) countSec4++;
                }
            });
        });
    });

    scoreSec1 = Math.round((countSec1 / 22) * 25);
    scoreSec2 = Math.round((countSec2 / 35) * 40);
    scoreSec3 = Math.round((countSec3 / 8) * 20);
    scoreSec4 = Math.round((countSec4 / 6) * 15);
    const totalScore = scoreSec1 + scoreSec2 + scoreSec3 + scoreSec4;

    // Show modal
    showScoreModal({
        totalScore,
        scoreSec1, countSec1,
        scoreSec2, countSec2,
        scoreSec3, countSec3,
        scoreSec4, countSec4
    });

    // Save history
    saveHistory(totalScore);

    // Refresh UI to show all answers
    renderExamDOM(exam);
    renderPalette(exam);
}

function showScoreModal(data) {
    const modal = document.getElementById("scoreModal");
    if (!modal) return;

    document.getElementById("modalScoreNumber").innerText = data.totalScore;
    document.getElementById("modalTimestamp").innerText = new Date().toLocaleString('vi-VN');

    const pill = document.getElementById("modalRatingPill");
    const msg = document.getElementById("modalFeedbackMsg");
    if (data.totalScore >= 85) {
        pill.className = "modal-rating-pill rating-green";
        pill.innerText = "XUẤT SẮC • ĐẠT CHUẨN JLPT A2.1";
        msg.innerText = "Xin chúc mừng! Bạn đã nắm vững toàn diện từ vựng, ngữ pháp và kỹ năng đọc hiểu từ Bài 11 đến Bài 18. Bạn hoàn toàn sẵn sàng cho kỳ thi chính thức.";
    } else if (data.totalScore >= 70) {
        pill.className = "modal-rating-pill rating-yellow";
        pill.innerText = "KHÁ GIỎI • CẦN ÔN THÊM CÂU SAI";
        msg.innerText = "Kết quả rất tốt! Hãy bấm nút 'Xem lại bài làm' bên dưới, sau đó lọc xem các câu làm sai để ghi chú lại ngữ pháp trọng tâm nhé.";
    } else {
        pill.className = "modal-rating-pill rating-red";
        pill.innerText = "CẦN CỐ GẮNG • ÔN LẠI NGỮ PHÁP 11-18";
        msg.innerText = "Bạn cần củng cố thêm các mẫu câu V-て, V-る/V-た và đọc kỹ bài khóa. Hãy xem lời giải chi tiết bên dưới để làm lại đạt điểm cao hơn nhé.";
    }

    const grid = document.getElementById("modalBreakdownGrid");
    grid.innerHTML = `
        <div class="score-card-item">
            <div class="score-card-title">Chữ Hán & Từ Vựng</div>
            <div class="score-card-val">${data.scoreSec1}/25đ</div>
            <div class="score-card-sub">Đúng: ${data.countSec1}/22 câu</div>
        </div>
        <div class="score-card-item">
            <div class="score-card-title">Ngữ Pháp 11 - 18</div>
            <div class="score-card-val">${data.scoreSec2}/40đ</div>
            <div class="score-card-sub">Đúng: ${data.countSec2}/35 câu</div>
        </div>
        <div class="score-card-item">
            <div class="score-card-title">Đọc Hiểu 3 Đoạn</div>
            <div class="score-card-val">${data.scoreSec3}/20đ</div>
            <div class="score-card-sub">Đúng: ${data.countSec3}/8 câu</div>
        </div>
        <div class="score-card-item">
            <div class="score-card-title">Sắp Xếp Câu ★</div>
            <div class="score-card-val">${data.scoreSec4}/15đ</div>
            <div class="score-card-sub">Đúng: ${data.countSec4}/6 câu</div>
        </div>
    `;

    modal.classList.add("show");
}

function closeScoreModal() {
    const modal = document.getElementById("scoreModal");
    if (modal) modal.classList.remove("show");
}

function enterReviewMode() {
    closeScoreModal();
    allExplained = true;
    toggleAllExplanations();
    window.scrollTo({ top: 500, behavior: 'smooth' });
}

function confirmResetExam() {
    if (confirm("Bạn có chắc chắn muốn làm lại mã đề này từ đầu không? Dữ liệu đã chọn sẽ được xóa trắng.")) {
        userAnswers = {};
        saveCurrentDraft();
        isExamSubmitted = false;
        closeScoreModal();
        const exam = getCurrentExam();
        renderExamDOM(exam);
        renderPalette(exam);
        updateProgressCounter();
        resetTimer();
        window.scrollTo({ top: 380, behavior: 'smooth' });
    }
}

// 12. History Persistence
function saveHistory(score) {
    try {
        let history = JSON.parse(localStorage.getItem(HISTORY_STORAGE_KEY) || "[]");
        history.unshift({
            examCode: currentExamCode,
            examName: getCurrentExam().name,
            score: score,
            timestamp: new Date().toLocaleString('vi-VN')
        });
        if (history.length > 20) history = history.slice(0, 20);
        localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(history));
    } catch(e) {}
}

function openHistoryModal() {
    const modal = document.getElementById("historyModal");
    const container = document.getElementById("historyListContainer");
    if (!modal || !container) return;

    let history = [];
    try {
        history = JSON.parse(localStorage.getItem(HISTORY_STORAGE_KEY) || "[]");
    } catch(e) {}

    if (history.length === 0) {
        container.innerHTML = `<div style="text-align:center; padding:24px; color:#94a3b8;">Chưa có lịch sử làm bài nào. Hãy nộp bài thi để lưu điểm số!</div>`;
    } else {
        container.innerHTML = history.map(item => `
            <div class="history-item">
                <div>
                    <span class="history-code-badge">${item.examCode}</span>
                    <div style="font-weight:700; color:#1e1b4b; margin-top:4px;">${item.examName}</div>
                    <div style="font-size:0.78rem; color:#64748b;">${item.timestamp}</div>
                </div>
                <div style="font-size:1.4rem; font-weight:900; color:#4f46e5;">
                    ${item.score}<span style="font-size:0.8rem; color:#64748b;">/100đ</span>
                </div>
            </div>
        `).join("");
    }

    modal.classList.add("show");
}

function closeHistoryModal() {
    const modal = document.getElementById("historyModal");
    if (modal) modal.classList.remove("show");
}

function clearAllHistory() {
    if (confirm("Bạn có chắc muốn xóa sạch toàn bộ lịch sử thi trên trình duyệt này không?")) {
        localStorage.removeItem(HISTORY_STORAGE_KEY);
        openHistoryModal();
    }
}
