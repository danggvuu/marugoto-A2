/* Interactive Kanji A2 Explorer, Stroke Player, Practice & Checkpoint Engine */
let current121Filtered = [...VOCAB_121_DATA];
let current121Lesson = 'ALL';

function render121Table() {
    const tbody = document.getElementById('table121Body');
    if (!tbody) return;
    tbody.innerHTML = '';

    if (current121Filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--gray); padding: 30px;">Không tìm thấy từ vựng nào phù hợp!</td></tr>`;
        return;
    }

    current121Filtered.forEach((item, idx) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td style="text-align: center; font-weight: 700; color: var(--gray);">#${idx + 1}</td>
            <td style="text-align: center;"><span style="background: #e0e7ff; color: #4338ca; padding: 3px 8px; border-radius: 6px; font-weight: 700; font-size: 0.82rem;">Bài ${item.lesson}</span></td>
            <td><strong style="font-size: 1.15rem; color: #1e293b;">${item.kanji}</strong></td>
            <td><span style="font-size: 1.05rem; color: var(--primary-dark); font-weight: 600;">${item.kana}</span></td>
            <td><span style="color: #334155; font-size: 0.95rem;">${item.vi}</span></td>
            <td style="text-align: center;"><span style="background: #f1f5f9; color: #475569; padding: 3px 8px; border-radius: 6px; font-size: 0.8rem; font-weight: 600;">${item.group || 'Từ vựng'}</span></td>
            <td style="text-align: center;">
                <button type="button" class="btn-sound-small" onclick="speakText('${item.kana}')" title="Nghe phát âm" style="background: #f8fafc; border: 1px solid var(--border); padding: 4px 8px; border-radius: 6px; cursor: pointer;">🔊</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function filter121Vocab(lesson, btn) {
    current121Lesson = lesson;
    document.querySelectorAll('.filter-121-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    apply121Filter();
}

function onSearch121Change() {
    apply121Filter();
}

function apply121Filter(opts) {
    const q = (document.getElementById('search121Input')?.value || '').trim().toLowerCase();
    current121Filtered = VOCAB_121_DATA.filter(item => {
        const matchLesson = (current121Lesson === 'ALL' || item.lesson == current121Lesson);
        const matchQuery = !q || item.kanji.toLowerCase().includes(q) || item.kana.toLowerCase().includes(q) || item.vi.toLowerCase().includes(q);
        return matchLesson && matchQuery;
    });
    render121Table();
    if (!(opts && opts.skipSave) && typeof saveKanjiCheckpoint === 'function') saveKanjiCheckpoint();
}

function copyAll121Quizlet() {
    const text = current121Filtered.map(item => `${item.kanji}\t[${item.kana}] ${item.vi}`).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        alert(`✅ Đã sao chép ${current121Filtered.length} từ chuẩn định dạng Tab cho Quizlet Pro!`);
    });
}

function copyAll121Colon() {
    const text = current121Filtered.map(item => `${item.kanji}、${item.vi}: ${item.kana}`).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        alert(`✅ Đã sao chép ${current121Filtered.length} từ định dạng: Từ、Nghĩa: Kana!`);
    });
}



const KANJI_CP_KEY = 'marugoto_kanji_a2_cp_v1';
window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;
window.__MARUGOTO_CP_EXTRA_KEYS__ = [KANJI_CP_KEY];
window.__MARUGOTO_ON_RESET__ = function () {
    try { localStorage.removeItem(KANJI_CP_KEY); } catch (e) {}
    window.location.reload();
};

let currentKanjiTab = 'tab-cards';
let isRestoringKanji = false;
let filteredKanji = [];
let currentVocabExercises = [];
let showHints = false;
let typingAnswers = {};
let typingGraded = false;

function saveKanjiCheckpoint() {
    if (isRestoringKanji) return;
    try {
        const searchEl = document.getElementById('searchInput');
        const search121El = document.getElementById('search121Input');
        const payload = {
            t: Date.now(),
            currentKanjiTab,
            selectedLessons: Array.from(selectedLessons),
            searchQuery: searchEl ? searchEl.value : '',
            current121Lesson: typeof current121Lesson !== 'undefined' ? current121Lesson : 'ALL',
            search121Query: search121El ? search121El.value : '',
            typingAnswers,
            typingGraded,
            showHints
        };
        localStorage.setItem(KANJI_CP_KEY, JSON.stringify(payload));
        if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
            window.MarugotoCheckpoint.notifySaved();
        }
    } catch (e) {}
}

// Switch Tabs
function switchTab(tabId, opts) {
    currentKanjiTab = tabId;
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.mode-tab-btn').forEach(b => {
        const oc = b.getAttribute('onclick') || '';
        b.classList.toggle('active', oc.includes(tabId));
    });
    const targetPanel = document.getElementById(tabId);
    if (targetPanel) targetPanel.classList.add('active');

    if (tabId === 'tab-exercises' && !(opts && opts.isRestore)) {
        renderTypingExercise();
        generateQuiz();
    } else if (tabId === 'tab-vocab-11-18') {
        render121Table();
    }
    if (!(opts && opts.skipSave)) {
        saveKanjiCheckpoint();
    }
}

// Multi-Lesson Filter System
const KANJI_LESSON_ORDER = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18'];
const KANJI_LESSON_TITLES = {
    'L1': 'Bài 1: Tôi và gia đình',
    'L2': 'Bài 2: Sở thích & Ngôn ngữ',
    'L3': 'Bài 3: Mùa & Thiên nhiên',
    'L4': 'Bài 4: Thời tiết',
    'L5': 'Bài 5: Thị trấn & Phố xá',
    'L6': 'Bài 6: Phương hướng & Màu sắc',
    'L7': 'Bài 7: Ra ngoài & Đi lại',
    'L8': 'Bài 8: Bữa ăn & Thời gian',
    'L9': 'Bài 9: Trường học & Học tập',
    'L10': 'Bài 10: Văn hóa & Du lịch',
    'L11': 'Bài 11: Ẩm thực & Quán ăn',
    'L12': 'Bài 12: Món ăn & Hương vị',
    'L13': 'Bài 13: Lịch trình công tác',
    'L14': 'Bài 14: Nơi làm việc & Xin phép',
    'L15': 'Bài 15: Cơ thể & Bệnh tật',
    'L16': 'Bài 16: Giữ gìn sức khỏe',
    'L17': 'Bài 17: Quà tặng & Kỷ niệm',
    'L18': 'Bài 18: Lễ hội & Trang phục'
};
let selectedLessons = new Set(KANJI_LESSON_ORDER); // Mặc định chọn tất cả các bài
let lastClickedLessonIdx = -1;

// Đếm số Kanji theo từng bài
const lessonCounts = {};
kanjiData.forEach(item => {
    lessonCounts[item.lesson] = (lessonCounts[item.lesson] || 0) + 1;
});

// Toast notification
function showToast(msg) {
    let toast = document.getElementById('toastMsg');
    if (!toast) {
        toast = document.createElement('div');
        toast.className = 'toast-msg';
        toast.id = 'toastMsg';
        document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2600);
}

// Khởi tạo các Chip & Dropdown dải bài & Custom Multi-Select Dropdown một lần duy nhất
function initKanjiLessonChips() {
    const container = document.getElementById('chipsContainerKanji');
    const rangeStart = document.getElementById('rangeStart');
    const rangeEnd = document.getElementById('rangeEnd');
    const rangeStartBar = document.getElementById('rangeStartBar');
    const rangeEndBar = document.getElementById('rangeEndBar');
    const msList = document.getElementById('msOptionsListKanji');

    if (container) container.innerHTML = '';
    if (rangeStart) rangeStart.innerHTML = '';
    if (rangeEnd) rangeEnd.innerHTML = '';
    if (rangeStartBar) rangeStartBar.innerHTML = '';
    if (rangeEndBar) rangeEndBar.innerHTML = '';
    if (msList) msList.innerHTML = '';

    KANJI_LESSON_ORDER.forEach((lid, idx) => {
        const count = lessonCounts[lid] || 0;
        const title = KANJI_LESSON_TITLES[lid] || lid;

        // A. Tạo Option Item trong Custom Multi-Select Dropdown
        if (msList) {
            const itemEl = document.createElement('label');
            itemEl.className = `ms-option-item ${selectedLessons.has(lid) ? 'selected' : ''}`;
            itemEl.id = `ms-item-kanji-${lid}`;
            itemEl.onclick = (e) => {
                if (e.target && e.target.type === 'checkbox') return;
                toggleLesson(lid, idx, e);
            };
            itemEl.innerHTML = `
                <input type="checkbox" class="ms-checkbox" id="ms-cb-kanji-${lid}" ${selectedLessons.has(lid) ? 'checked' : ''} onchange="toggleLesson('${lid}', ${idx}, event)">
                <span class="ms-item-tag">${lid.replace('L', 'Bài ')}</span>
                <span class="ms-item-title">${title.split(':')[1]?.trim() || title}</span>
                <span class="ms-item-count">${count} chữ</span>
            `;
            msList.appendChild(itemEl);
        }

        // B. Tạo Chip Button bên dưới
        if (container) {
            const chip = document.createElement('button');
            chip.className = `lesson-chip ${selectedLessons.has(lid) ? 'active' : ''}`;
            chip.id = `chip-${lid}`;
            chip.title = `${title} (${count} chữ Hán)`;
            chip.innerHTML = `
                <span class="chip-check">${selectedLessons.has(lid) ? '✓' : '+'}</span>
                <span>${lid.replace('L', 'Bài ')}</span>
                <span class="chip-count">${count}</span>
            `;
            chip.onclick = (e) => toggleLesson(lid, idx, e);
            container.appendChild(chip);
        }

        // C. Tạo Dropdown dải bài (cho cả 2 cặp)
        [
            { s: rangeStart, e: rangeEnd },
            { s: rangeStartBar, e: rangeEndBar }
        ].forEach(pair => {
            if (pair.s && pair.e) {
                const opt1 = document.createElement('option');
                opt1.value = lid;
                opt1.textContent = `${lid.replace('L', 'Bài ')} - ${title.split(':')[1]?.trim() || title}`;
                pair.s.appendChild(opt1);

                const opt2 = document.createElement('option');
                opt2.value = lid;
                opt2.textContent = `${lid.replace('L', 'Bài ')} - ${title.split(':')[1]?.trim() || title}`;
                pair.e.appendChild(opt2);
            }
        });
    });

    const lastLesson = KANJI_LESSON_ORDER[KANJI_LESSON_ORDER.length - 1];
    if (rangeStart && rangeEnd) {
        rangeStart.value = "L1";
        rangeEnd.value = lastLesson;
    }
    if (rangeStartBar && rangeEndBar) {
        rangeStartBar.value = "L1";
        rangeEndBar.value = lastLesson;
    }
}

// Toggle Dropdown Mở/Đóng cho Kanji
function toggleMsDropdownKanji(e) {
    if (e) e.stopPropagation();
    const container = document.getElementById('msContainerKanji');
    if (container) container.classList.toggle('open');
}

function closeMsDropdownKanji() {
    const container = document.getElementById('msContainerKanji');
    if (container) container.classList.remove('open');
}

document.addEventListener('click', (e) => {
    const container = document.getElementById('msContainerKanji');
    if (container && !container.contains(e.target)) {
        closeMsDropdownKanji();
    }
});

// Toggle một bài học (Hỗ trợ Shift + Click chọn dải bài liên tục)
function toggleLesson(lid, idx, event) {
    if (event && event.shiftKey && lastClickedLessonIdx !== -1) {
        const start = Math.min(lastClickedLessonIdx, idx);
        const end = Math.max(lastClickedLessonIdx, idx);
        for (let i = start; i <= end; i++) {
            selectedLessons.add(KANJI_LESSON_ORDER[i]);
        }
        showToast(`Đã chọn liên tục từ ${KANJI_LESSON_ORDER[start].replace('L', 'Bài ')} đến ${KANJI_LESSON_ORDER[end].replace('L', 'Bài ')}!`);
    } else {
        if (selectedLessons.has(lid)) {
            selectedLessons.delete(lid);
        } else {
            selectedLessons.add(lid);
        }
    }

    lastClickedLessonIdx = idx;
    updatePresetPillsState();
    updateChipsUI();
    applyLessonFilter();
}

// Chọn dải bài liên tục từ Range Dropdown
function applyRangeSelection(isBar = false) {
    const startEl = isBar ? document.getElementById('rangeStartBar') : document.getElementById('rangeStart');
    const endEl = isBar ? document.getElementById('rangeEndBar') : document.getElementById('rangeEnd');
    const startId = startEl ? startEl.value : 'L1';
    const endId = endEl ? endEl.value : KANJI_LESSON_ORDER[KANJI_LESSON_ORDER.length - 1];
    const sIdx = KANJI_LESSON_ORDER.indexOf(startId);
    const eIdx = KANJI_LESSON_ORDER.indexOf(endId);

    if (sIdx === -1 || eIdx === -1) return;
    const start = Math.min(sIdx, eIdx);
    const end = Math.max(sIdx, eIdx);

    selectedLessons.clear();
    for (let i = start; i <= end; i++) {
        selectedLessons.add(KANJI_LESSON_ORDER[i]);
    }

    updatePresetPillsState();
    updateChipsUI();
    applyLessonFilter();
    showToast(`Đã chọn dải bài: ${KANJI_LESSON_ORDER[start].replace('L', 'Bài ')} ➔ ${KANJI_LESSON_ORDER[end].replace('L', 'Bài ')} (${end - start + 1} bài)!`);
}

function onRangeDropdownChange() {
    // Tự động kiểm tra
}

// Chọn nhanh theo các Preset
function selectPreset(type) {
    selectedLessons.clear();

    if (type === 'ALL') {
        KANJI_LESSON_ORDER.forEach(l => selectedLessons.add(l));
    } else if (type === 'L1_5') {
        ['L1', 'L2', 'L3', 'L4', 'L5'].forEach(l => selectedLessons.add(l));
    } else if (type === 'L6_10') {
        ['L6', 'L7', 'L8', 'L9', 'L10'].forEach(l => selectedLessons.add(l));
    } else if (type === 'L10_11') {
        ['L10', 'L11'].forEach(l => selectedLessons.add(l));
    } else if (type === 'L11_18') {
        ['L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18'].forEach(l => selectedLessons.add(l));
    } else if (type === 'L11') {
        selectedLessons.add('L11');
    } else if (type === 'L3') {
        selectedLessons.add('L3');
    } else if (type === 'NONE') {
        // Rỗng
    }

    lastClickedLessonIdx = -1;
    updatePresetPillsState(type);
    updateChipsUI();
    applyLessonFilter();
}

function updatePresetPillsState(activeType) {
    document.querySelectorAll('.preset-pill').forEach(btn => btn.classList.remove('active'));
    if (activeType && activeType !== 'NONE') {
        const btn = document.getElementById(`preset-${activeType.toLowerCase().replace(/_/g, '-')}`);
        if (btn) btn.classList.add('active');
    } else if (selectedLessons.size === KANJI_LESSON_ORDER.length) {
        const btn = document.getElementById('preset-all');
        if (btn) btn.classList.add('active');
    }
}

function updateChipsUI() {
    KANJI_LESSON_ORDER.forEach(lid => {
        const isSel = selectedLessons.has(lid);

        // 1. Cập nhật Chip Button
        const chip = document.getElementById(`chip-${lid}`);
        if (chip) {
            chip.classList.toggle('active', isSel);
            const check = chip.querySelector('.chip-check');
            if (check) check.textContent = isSel ? '✓' : '+';
        }

        // 2. Cập nhật Checkbox trong Dropdown
        const itemEl = document.getElementById(`ms-item-kanji-${lid}`);
        if (itemEl) itemEl.classList.toggle('selected', isSel);
        const cb = document.getElementById(`ms-cb-kanji-${lid}`);
        if (cb) cb.checked = isSel;
    });

    // 3. Cập nhật Label & Badge trên nút Dropdown Kanji
    const triggerText = document.getElementById('msTriggerTextKanji');
    const triggerBadge = document.getElementById('msTriggerBadgeKanji');
    const footerCount = document.getElementById('msFooterCountKanji');

    if (triggerText) {
        if (selectedLessons.size === KANJI_LESSON_ORDER.length) {
            triggerText.textContent = `🌟 Tất Cả ${KANJI_LESSON_ORDER.length} Bài (${kanjiData.length} chữ Hán)`;
            if (triggerBadge) triggerBadge.textContent = `${KANJI_LESSON_ORDER.length}/${KANJI_LESSON_ORDER.length}`;
        } else if (selectedLessons.size === 0) {
            triggerText.textContent = "⚠️ Chưa chọn bài nào (vui lòng chọn)";
            if (triggerBadge) triggerBadge.textContent = `0/${KANJI_LESSON_ORDER.length}`;
        } else if (selectedLessons.size === 1) {
            const only = Array.from(selectedLessons)[0];
            const t = KANJI_LESSON_TITLES[only] || only;
            triggerText.textContent = `${only.replace('L', 'Bài ')}: ${t.split(':')[1]?.trim() || t}`;
            if (triggerBadge) triggerBadge.textContent = `1/${KANJI_LESSON_ORDER.length}`;
        } else {
            const sortedSel = KANJI_LESSON_ORDER.filter(l => selectedLessons.has(l)).map(l => l.replace('L', 'Bài '));
            triggerText.textContent = `📚 Đang chọn ${selectedLessons.size} bài (${sortedSel.join(', ')})`;
            if (triggerBadge) triggerBadge.textContent = `${selectedLessons.size}/${KANJI_LESSON_ORDER.length}`;
        }
    }

    if (footerCount) {
        footerCount.textContent = `Đang chọn: ${selectedLessons.size} bài (${filteredKanji ? filteredKanji.length : 0} chữ Hán)`;
    }
}

let kanjiSearchDebounceTimer = null;
function onSearchChange() {
    const query = document.getElementById('searchInput').value;
    const clearBtn = document.getElementById('searchClearBtn');
    if (clearBtn) clearBtn.style.display = query ? 'block' : 'none';
    clearTimeout(kanjiSearchDebounceTimer);
    kanjiSearchDebounceTimer = setTimeout(applyLessonFilter, 120);
}

function clearSearch() {
    const input = document.getElementById('searchInput');
    input.value = '';
    const clearBtn = document.getElementById('searchClearBtn');
    if (clearBtn) clearBtn.style.display = 'none';
    applyLessonFilter();
}

// Filter by Lesson & Search
function applyLessonFilter() {
    const query = document.getElementById('searchInput') ? document.getElementById('searchInput').value.trim().toLowerCase() : '';

    filteredKanji = kanjiData.filter(item => {
        const matchLesson = selectedLessons.has(item.lesson);
        const matchQuery = !query ||
            item.char.includes(query) ||
            item.hv.toLowerCase().includes(query) ||
            item.meaning.toLowerCase().includes(query) ||
            item.kun.toLowerCase().includes(query) ||
            item.on.toLowerCase().includes(query);
        return matchLesson && matchQuery;
    });

    // Cập nhật tóm tắt số lượng
    const summary = document.getElementById('selectionSummary');
    const tabCount = document.getElementById('tabCountCards');
    if (tabCount) tabCount.textContent = filteredKanji.length;
    const filterBadge = document.getElementById('activeFilterBadge');
    if (filterBadge) {
        filterBadge.textContent = selectedLessons.size === KANJI_LESSON_ORDER.length ? '18 bài' : `${selectedLessons.size} bài`;
    }
    if (summary) {
        if (selectedLessons.size === KANJI_LESSON_ORDER.length) {
            summary.textContent = `Đang chọn: Tất cả ${KANJI_LESSON_ORDER.length} bài (${filteredKanji.length} chữ Hán)`;
        } else if (selectedLessons.size === 0) {
            summary.textContent = `Chưa chọn bài nào (vui lòng bấm chọn bài)`;
        } else {
            const sortedSel = KANJI_LESSON_ORDER.filter(l => selectedLessons.has(l)).map(l => l.replace('L', 'Bài '));
            summary.textContent = `Đang chọn: ${selectedLessons.size} bài (${sortedSel.join(', ')}) • ${filteredKanji.length} chữ Hán`;
        }
    }

    renderCards(filteredKanji);
    renderTypingExercise();
    generateQuiz();
    saveKanjiCheckpoint();
}

// Render Kanji Cards with Interactive Writing Canvas & Step-by-Step Breakdown (Optimized with DocumentFragment & Lazy SVG Player)
function renderCards(data) {
    const container = document.getElementById('cardsContainer');
    container.innerHTML = '';

    if (data.length === 0) {
        container.innerHTML = '<div style="text-align: center; padding: 40px; color: #888;">Không tìm thấy chữ Hán nào phù hợp với bộ lọc hiện tại!</div>';
        return;
    }

    const fragment = document.createDocumentFragment();

    data.forEach((item, index) => {
        const card = document.createElement('div');
        card.className = 'kanji-card';
        card.dataset.index = index;

        const examplesHtml = item.examples.map(ex => 
            `<div class="example-line">• <span class="example-jp" style="cursor:pointer;" onclick="speakJapanese('${ex.word}', this)" title="Bấm để nghe phát âm">${ex.word}（${ex.reading}）</span> <button type="button" class="fc-speaker-btn" style="width:24px; height:24px; font-size:12px; margin-left:4px; vertical-align:middle;" onclick="speakJapanese('${ex.word}', this)" title="Nghe từ vựng này">🔊</button> : ${ex.vi}</div>`
        ).join('');

        card.innerHTML = `
            <div class="card-header-bar">
                <div class="kanji-badge" style="cursor:pointer;" onclick="speakJapanese('${item.char}', this)" title="Bấm để nghe phát âm chữ Hán này">${item.char}</div>
                <div class="han-viet-title">${item.hv}</div>
                <span class="stroke-badge">✍️ ${item.strokes} nét</span>
                <div class="lesson-tag">${item.lessonName}</div>
            </div>

            <div class="card-body">
                <!-- Left Info Box -->
                <div class="info-box">
                    <div>
                        <ul class="info-list">
                            <li class="info-item">
                                <span class="info-bullet">•</span>
                                <span class="info-label">Ý nghĩa:</span>
                                <span>${item.meaning}</span>
                            </li>
                            <li class="info-item">
                                <span class="info-bullet">•</span>
                                <span class="info-label">Kun:</span>
                                <span class="info-value-kun" style="cursor:pointer;" onclick="speakJapanese('${item.kun}', this)" title="Nghe âm Kun">${item.kun}</span> <button type="button" class="fc-speaker-btn" style="width:20px; height:20px; font-size:10px; margin-left:4px; vertical-align:middle;" onclick="speakJapanese('${item.kun}', this)" title="Nghe âm Kun">🔊</button>
                            </li>
                            <li class="info-item">
                                <span class="info-bullet">•</span>
                                <span class="info-label">On:</span>
                                <span class="info-value-on" style="cursor:pointer;" onclick="speakJapanese('${item.on}', this)" title="Nghe âm On">${item.on}</span> <button type="button" class="fc-speaker-btn" style="width:20px; height:20px; font-size:10px; margin-left:4px; vertical-align:middle;" onclick="speakJapanese('${item.on}', this)" title="Nghe âm On">🔊</button>
                            </li>
                        </ul>

                        <div class="examples-section">
                            ${examplesHtml}
                        </div>
                    </div>

                    <div class="guides-wrapper">
                        <div class="stroke-guide-note">
                            🖌️ <strong>Cách viết (${item.strokes} nét):</strong> ${item.strokeGuide}
                        </div>
                        <div class="mnemonic-note">
                            💡 <strong>Mẹo nhớ:</strong> ${item.mnemonic}
                        </div>
                    </div>
                </div>

                <!-- Right Column: Formula & Stroke Order Animator & Interactive Canvas -->
                <div class="visual-column">
                    <div class="mnemonic-visual-box">
                        <div class="radical-formula">${item.formula}</div>
                        <div style="font-size: 0.78rem; color: #888;">Chiết tự bộ thủ</div>
                    </div>

                    <div class="anim-status-bar" id="anim-status-${index}">
                        <span>Nét: <strong id="stroke-curr-${index}">${item.strokes}</strong> / ${item.strokes}</span>
                    </div>

                    <div class="kanji-grid-box" id="grid-box-${index}">
                        <div class="grid-line-h"></div>
                        <div class="grid-line-v"></div>
                        <div class="kanji-svg-container" id="kanji-svg-container-${index}" data-opacity="1">
                            <span class="kanji-char-large" id="kanji-fallback-${index}">${item.char}</span>
                        </div>
                        <canvas class="practice-canvas" id="canvas-${index}" width="165" height="165"></canvas>
                    </div>

                    <!-- Canvas Tools -->
                    <div class="canvas-tools-bar">
                        <button class="btn-canvas" id="btn-draw-${index}" onclick="togglePracticeMode(${index})" title="Bật chế độ tự dùng tay hoặc chuột viết chữ vào ô vuông">✍️ Tập viết</button>
                        <button class="btn-canvas" id="btn-clear-${index}" onclick="clearPracticeCanvas(${index})" title="Xóa các nét bạn đã tự vẽ">🗑️ Xóa nét</button>
                        <button class="btn-canvas" id="btn-ghost-${index}" onclick="cycleGhostOpacity(${index})" title="Thay đổi độ mờ chữ mẫu để tự nhớ cách viết">👁️ Mẫu: Rõ</button>
                    </div>

                    <!-- Animation & Step Controls -->
                    <div class="anim-controls">
                        <button class="btn-anim" id="btn-prev-${index}" onclick="stepPrevStroke(${index})" title="Lùi 1 nét">⏮️ Lùi</button>
                        <button class="btn-anim btn-anim-play" id="btn-play-${index}" onclick="togglePlayAnimation(${index})" title="Phát từng nét chuyển động">▶️ Phát nét</button>
                        <button class="btn-anim" id="btn-next-${index}" onclick="stepNextStroke(${index})" title="Tiến 1 nét">⏭️ Tiến</button>
                        <button class="btn-anim" id="btn-replay-${index}" onclick="replayAnimation(${index})" title="Xem vẽ lại từ đầu">🔄 Lại</button>
                        <button class="btn-anim active-tool" id="btn-num-${index}" onclick="toggleNumbers(${index})" title="Bật/tắt số thứ tự nét">🔢 Số nét</button>
                    </div>
                </div>
            </div>

            <!-- Step-by-Step Stroke Breakdown Strip -->
            <div class="stroke-breakdown-section">
                <div class="stroke-breakdown-header">
                    <div class="stroke-breakdown-title">
                        <span>🖌️ Bảng phân rã từng bước vẽ (${item.strokes} nét):</span>
                    </div>
                    <span class="stroke-breakdown-hint">👉 Bấm vào từng ô để xem nét đó hoặc tự luyện viết theo thứ tự</span>
                </div>
                <div class="stroke-steps-strip" id="stroke-steps-${index}">
                    <span style="font-size: 0.85rem; color: #7f8c8d; padding: 4px;">Đang tải thứ tự nét KanjiVG...</span>
                </div>
            </div>
        `;
        fragment.appendChild(card);
    });

    container.appendChild(fragment);

    // Lazy-init KanjiVG Players via IntersectionObserver for buttery-smooth 120fps scrolling
    if ('IntersectionObserver' in window) {
        if (window._kanjiObserver) window._kanjiObserver.disconnect();
        window._kanjiObserver = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const c = entry.target;
                    const idx = parseInt(c.dataset.index, 10);
                    if (!c.dataset.loaded && data[idx]) {
                        c.dataset.loaded = 'true';
                        initKanjiPlayer(data[idx], idx);
                    }
                    obs.unobserve(c);
                }
            });
        }, { rootMargin: '300px 0px' });

        container.querySelectorAll('.kanji-card').forEach(c => window._kanjiObserver.observe(c));
    } else {
        data.forEach((item, index) => initKanjiPlayer(item, index));
    }
}

// ==========================================
// KANJIVG STROKE ORDER ANIMATION & BREAKDOWN PLAYER LOGIC
// ==========================================
const svgCache = new Map();
const kanjiPlayers = {};

async function fetchKanjiSvg(char) {
    if (svgCache.has(char)) return svgCache.get(char);
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
                    svgCache.set(char, text);
                    return text;
                }
            }
        } catch (e) {
            // Thử nguồn tiếp theo
        }
    }
    return null;
}

function initKanjiPlayer(item, index) {
    if (kanjiPlayers[index] && kanjiPlayers[index].timer) {
        clearTimeout(kanjiPlayers[index].timer);
    }

    kanjiPlayers[index] = {
        char: item.char,
        totalStrokes: item.strokes,
        currentStroke: item.strokes,
        isPlaying: false,
        showNumbers: true,
        paths: [],
        ghostPaths: [],
        numbersGroup: null,
        timer: null
    };

    fetchKanjiSvg(item.char).then(svgText => {
        if (svgText) {
            setupSvgPlayer(index, svgText);
        } else {
            const status = document.getElementById(`anim-status-${index}`);
            if (status) {
                status.innerHTML = `<span style="color:#7f8c8d; font-size:0.8rem;">(Xem nét tĩnh)</span>`;
            }
            const stepsStrip = document.getElementById(`stroke-steps-${index}`);
            if (stepsStrip) {
                stepsStrip.innerHTML = `<span style="color:#7f8c8d; font-size:0.82rem; padding:4px;">Chữ này đang hiển thị phông chuẩn (${item.strokes} nét)</span>`;
            }
        }
    });
}

function setupSvgPlayer(index, svgText) {
    const player = kanjiPlayers[index];
    if (!player) return;

    const container = document.getElementById(`kanji-svg-container-${index}`);
    if (!container) return;

    const parser = new DOMParser();
    const doc = parser.parseFromString(svgText, 'image/svg+xml');
    const rawSvg = doc.querySelector('svg');
    if (!rawSvg) return;

    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 109 109');
    svg.setAttribute('class', 'kanjivg-svg');

    // Extract stroke paths
    const rawPaths = Array.from(rawSvg.querySelectorAll('path'));
    if (rawPaths.length > 0) {
        player.totalStrokes = rawPaths.length;
        player.currentStroke = rawPaths.length;
    }

    // 1. Ghost Group (light gray guide background)
    const ghostGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    ghostGroup.setAttribute('class', 'ghost-strokes');
    player.ghostPaths = [];
    rawPaths.forEach(rp => {
        const gp = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        gp.setAttribute('d', rp.getAttribute('d'));
        gp.setAttribute('fill', 'none');
        gp.setAttribute('stroke', '#e2e8f0');
        gp.setAttribute('stroke-width', '4');
        gp.setAttribute('stroke-linecap', 'round');
        gp.setAttribute('stroke-linejoin', 'round');
        ghostGroup.appendChild(gp);
        player.ghostPaths.push(gp);
    });
    svg.appendChild(ghostGroup);

    // 2. Active Animated Strokes Group
    const activeGroup = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    activeGroup.setAttribute('class', 'active-strokes');
    player.paths = [];
    rawPaths.forEach(rp => {
        const ap = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        ap.setAttribute('d', rp.getAttribute('d'));
        ap.setAttribute('fill', 'none');
        ap.setAttribute('stroke', '#2c3e50');
        ap.setAttribute('stroke-width', '4.5');
        ap.setAttribute('stroke-linecap', 'round');
        ap.setAttribute('stroke-linejoin', 'round');
        activeGroup.appendChild(ap);
        player.paths.push(ap);
    });
    svg.appendChild(activeGroup);

    // 3. Stroke Numbers Group
    const rawNumbersGroup = rawSvg.querySelector('[id*="StrokeNumbers"]');
    if (rawNumbersGroup) {
        const numbersGroup = rawNumbersGroup.cloneNode(true);
        numbersGroup.querySelectorAll('text').forEach(t => {
            t.setAttribute('fill', '#e74c3c');
            t.setAttribute('font-size', '8');
            t.setAttribute('font-weight', 'bold');
            t.setAttribute('font-family', '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif');
            t.style.transition = 'opacity 0.2s';
        });
        svg.appendChild(numbersGroup);
        player.numbersGroup = numbersGroup;
        numbersGroup.style.display = player.showNumbers ? 'inline' : 'none';
    }

    container.innerHTML = '';
    container.appendChild(svg);

    // Setup path strokeDasharray & default fully visible
    player.paths.forEach(p => {
        const len = p.getTotalLength();
        p.dataset.length = len;
        p.style.strokeDasharray = `${len} ${len}`;
        p.style.strokeDashoffset = '0';
        p.style.stroke = '#2c3e50';
    });

    // 4. TẠO BẢNG PHÂN RÃ TỪNG BƯỚC VẼ (1 -> N nét) TRỰC QUAN
    const stepsContainer = document.getElementById(`stroke-steps-${index}`);
    if (stepsContainer && rawPaths.length > 0) {
        stepsContainer.innerHTML = '';
        rawPaths.forEach((_, stepIdx) => {
            const k = stepIdx + 1;
            const stepBox = document.createElement('div');
            stepBox.className = `stroke-step-box ${k === player.currentStroke ? 'active-step' : ''}`;
            stepBox.id = `step-box-${index}-${k}`;
            stepBox.title = `Nét ${k}/${player.totalStrokes} (Bấm để nhảy tới nét này)`;
            stepBox.onclick = () => jumpToStroke(index, k);

            // Tạo mini SVG biểu diễn nét đến bước k
            let pathsHtml = '';
            for (let i = 0; i < stepIdx; i++) {
                pathsHtml += `<path d="${rawPaths[i].getAttribute('d')}" fill="none" stroke="#4a5568" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />`;
            }
            pathsHtml += `<path d="${rawPaths[stepIdx].getAttribute('d')}" fill="none" stroke="#e74c3c" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" />`;

            stepBox.innerHTML = `
                <svg viewBox="0 0 109 109" class="step-mini-svg">
                    <line x1="0" y1="54.5" x2="109" y2="54.5" stroke="#f1f5f9" stroke-width="1.5" stroke-dasharray="3 3"/>
                    <line x1="54.5" y1="0" x2="54.5" y2="109" stroke="#f1f5f9" stroke-width="1.5" stroke-dasharray="3 3"/>
                    ${pathsHtml}
                </svg>
                <div class="step-num-badge">${k}</div>
            `;
            stepsContainer.appendChild(stepBox);
        });
    }

    // 5. Khởi tạo Canvas tập viết
    initPracticeCanvas(index);

    updatePlayerUI(index);
}

function updatePlayerUI(index) {
    const player = kanjiPlayers[index];
    if (!player) return;

    const currEl = document.getElementById(`stroke-curr-${index}`);
    if (currEl) currEl.textContent = player.currentStroke;

    const statusEl = document.getElementById(`anim-status-${index}`);
    if (statusEl) {
        if (player.isPlaying) {
            statusEl.innerHTML = `<span>Đang vẽ nét: <strong style="color:#e74c3c;">${player.currentStroke + 1}</strong> / ${player.totalStrokes}</span>`;
        } else if (player.currentStroke === player.totalStrokes) {
            statusEl.innerHTML = `<span>Nét: <strong>${player.totalStrokes}</strong> / ${player.totalStrokes} <span style="color:#27ae60;">(Đầy đủ)</span></span>`;
        } else {
            statusEl.innerHTML = `<span>Nét: <strong>${player.currentStroke}</strong> / ${player.totalStrokes}</span>`;
        }
    }

    const playBtn = document.getElementById(`btn-play-${index}`);
    if (playBtn) {
        if (player.isPlaying) {
            playBtn.innerHTML = '⏸️ Tạm dừng';
            playBtn.classList.add('active-tool');
        } else {
            playBtn.innerHTML = '▶️ Phát nét';
            playBtn.classList.remove('active-tool');
        }
    }
}

function highlightStepBox(index, stepNumber) {
    const container = document.getElementById(`stroke-steps-${index}`);
    if (!container) return;
    const boxes = container.querySelectorAll('.stroke-step-box');
    boxes.forEach(b => b.classList.remove('active-step'));
    const target = document.getElementById(`step-box-${index}-${stepNumber}`);
    if (target) {
        target.classList.add('active-step');
        target.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' });
    }
}

function jumpToStroke(index, targetStroke) {
    const player = kanjiPlayers[index];
    if (!player) return;

    if (player.isPlaying) {
        player.isPlaying = false;
        if (player.timer) clearTimeout(player.timer);
    }

    targetStroke = Math.max(0, Math.min(targetStroke, player.totalStrokes));
    player.currentStroke = targetStroke;

    player.paths.forEach((p, sIdx) => {
        const len = parseFloat(p.dataset.length) || p.getTotalLength();
        p.style.transition = 'none';
        if (sIdx < targetStroke - 1) {
            p.style.strokeDashoffset = '0';
            p.style.stroke = '#2c3e50';
        } else if (sIdx === targetStroke - 1) {
            p.style.strokeDashoffset = '0';
            p.style.stroke = '#e74c3c'; // Làm nổi bật nét hiện tại
        } else {
            p.style.strokeDashoffset = len;
            p.style.stroke = '#2c3e50';
        }
    });

    if (player.numbersGroup) {
        const numTexts = player.numbersGroup.querySelectorAll('text');
        numTexts.forEach((t, sIdx) => {
            t.style.opacity = (sIdx < targetStroke && player.showNumbers) ? '1' : '0';
        });
    }

    highlightStepBox(index, targetStroke);
    updatePlayerUI(index);
}

function drawStroke(index, strokeIdx, onDone) {
    const player = kanjiPlayers[index];
    if (!player || strokeIdx < 0 || strokeIdx >= player.paths.length) {
        if (onDone) onDone();
        return;
    }

    const p = player.paths[strokeIdx];
    const len = parseFloat(p.dataset.length) || p.getTotalLength();

    // Ép reflow (Forced Reflow) để trình duyệt không bỏ qua transition cho nét đầu tiên
    p.style.transition = 'none';
    p.style.strokeDashoffset = len;
    void p.getBoundingClientRect();

    const duration = Math.min(0.55, Math.max(0.28, (len / 120) * 0.45));
    p.style.transition = `stroke-dashoffset ${duration}s ease-in-out`;
    p.style.stroke = '#e74c3c';
    p.style.strokeDashoffset = '0';

    if (player.numbersGroup) {
        const numTexts = player.numbersGroup.querySelectorAll('text');
        if (numTexts[strokeIdx]) {
            numTexts[strokeIdx].style.opacity = player.showNumbers ? '1' : '0';
        }
    }

    highlightStepBox(index, strokeIdx + 1);

    setTimeout(() => {
        p.style.stroke = '#2c3e50';
        if (onDone) onDone();
    }, duration * 1000 + 40);
}

function hideStroke(index, strokeIdx) {
    const player = kanjiPlayers[index];
    if (!player || strokeIdx < 0 || strokeIdx >= player.paths.length) return;

    const p = player.paths[strokeIdx];
    const len = parseFloat(p.dataset.length) || 100;
    p.style.transition = 'none';
    p.style.strokeDashoffset = len;
    p.style.stroke = '#2c3e50';

    if (player.numbersGroup) {
        const numTexts = player.numbersGroup.querySelectorAll('text');
        if (numTexts[strokeIdx]) {
            numTexts[strokeIdx].style.opacity = '0';
        }
    }
}

function playLoop(index) {
    const player = kanjiPlayers[index];
    if (!player || !player.isPlaying) return;

    if (player.currentStroke >= player.totalStrokes) {
        player.isPlaying = false;
        updatePlayerUI(index);
        return;
    }

    updatePlayerUI(index);
    const strokeToDraw = player.currentStroke;
    drawStroke(index, strokeToDraw, () => {
        if (!player.isPlaying) return;
        player.currentStroke = strokeToDraw + 1;
        updatePlayerUI(index);

        if (player.currentStroke < player.totalStrokes) {
            player.timer = setTimeout(() => {
                playLoop(index);
            }, 160);
        } else {
            player.isPlaying = false;
            updatePlayerUI(index);
        }
    });
}

function togglePlayAnimation(index) {
    const player = kanjiPlayers[index];
    if (!player) return;

    if (player.isPlaying) {
        player.isPlaying = false;
        if (player.timer) clearTimeout(player.timer);
        updatePlayerUI(index);
        return;
    }

    if (player.currentStroke >= player.totalStrokes) {
        player.paths.forEach((_, sIdx) => hideStroke(index, sIdx));
        player.currentStroke = 0;
    }

    player.isPlaying = true;
    playLoop(index);
}

function replayAnimation(index) {
    const player = kanjiPlayers[index];
    if (!player) return;

    if (player.timer) clearTimeout(player.timer);
    player.isPlaying = false;
    player.paths.forEach((_, sIdx) => hideStroke(index, sIdx));
    player.currentStroke = 0;
    updatePlayerUI(index);

    player.isPlaying = true;
    playLoop(index);
}

function stepNextStroke(index) {
    const player = kanjiPlayers[index];
    if (!player) return;

    if (player.isPlaying) {
        player.isPlaying = false;
        if (player.timer) clearTimeout(player.timer);
    }

    if (player.currentStroke < player.totalStrokes) {
        drawStroke(index, player.currentStroke);
        player.currentStroke++;
        updatePlayerUI(index);
    }
}

function stepPrevStroke(index) {
    const player = kanjiPlayers[index];
    if (!player) return;

    if (player.isPlaying) {
        player.isPlaying = false;
        if (player.timer) clearTimeout(player.timer);
    }

    if (player.currentStroke > 0) {
        player.currentStroke--;
        hideStroke(index, player.currentStroke);
        highlightStepBox(index, player.currentStroke);
        updatePlayerUI(index);
    }
}

function toggleNumbers(index) {
    const player = kanjiPlayers[index];
    if (!player) return;

    player.showNumbers = !player.showNumbers;
    if (player.numbersGroup) {
        player.numbersGroup.style.display = player.showNumbers ? 'inline' : 'none';
    }

    const btn = document.getElementById(`btn-num-${index}`);
    if (btn) {
        btn.classList.toggle('active-tool', player.showNumbers);
    }
}

// ==========================================
// INTERACTIVE PRACTICE CANVAS LOGIC (TẬP VIẾT)
// ==========================================
function initPracticeCanvas(index) {
    const canvas = document.getElementById(`canvas-${index}`);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let isDrawing = false;
    let lastX = 0, lastY = 0;

    function getCoords(e) {
        const rect = canvas.getBoundingClientRect();
        const clientX = e.clientX || (e.touches && e.touches[0] ? e.touches[0].clientX : 0);
        const clientY = e.clientY || (e.touches && e.touches[0] ? e.touches[0].clientY : 0);
        return {
            x: (clientX - rect.left) * (canvas.width / rect.width),
            y: (clientY - rect.top) * (canvas.height / rect.height)
        };
    }

    function startDraw(e) {
        e.preventDefault();
        isDrawing = true;
        const { x, y } = getCoords(e);
        lastX = x;
        lastY = y;
        ctx.beginPath();
        ctx.arc(x, y, 2.5, 0, Math.PI * 2);
        ctx.fillStyle = '#2980b9';
        ctx.fill();
    }

    function draw(e) {
        if (!isDrawing) return;
        e.preventDefault();
        const { x, y } = getCoords(e);
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.strokeStyle = '#2980b9';
        ctx.lineWidth = 5.5;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
        ctx.stroke();
        lastX = x;
        lastY = y;
    }

    function stopDraw(e) {
        if (!isDrawing) return;
        e.preventDefault();
        isDrawing = false;
    }

    canvas.addEventListener('pointerdown', startDraw);
    canvas.addEventListener('pointermove', draw);
    canvas.addEventListener('pointerup', stopDraw);
    canvas.addEventListener('pointercancel', stopDraw);
    canvas.addEventListener('pointerleave', stopDraw);
}

function togglePracticeMode(index) {
    const canvas = document.getElementById(`canvas-${index}`);
    const btn = document.getElementById(`btn-draw-${index}`);
    if (!canvas || !btn) return;

    const isActive = canvas.classList.toggle('active');
    btn.classList.toggle('active-tool', isActive);
    if (isActive) {
        showToast("Đã bật bảng vẽ! Hãy vẽ bằng chuột hoặc ngón tay lên ô vuông.");
    } else {
        showToast("Đã tắt bảng vẽ.");
    }
}

function clearPracticeCanvas(index) {
    const canvas = document.getElementById(`canvas-${index}`);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    showToast("Đã xóa sạch nét vẽ trên ô!");
}

function cycleGhostOpacity(index) {
    const svgCont = document.getElementById(`kanji-svg-container-${index}`);
    const btn = document.getElementById(`btn-ghost-${index}`);
    if (!svgCont || !btn) return;

    let curr = parseFloat(svgCont.dataset.opacity || "1");
    if (curr > 0.6) {
        curr = 0.25;
        btn.innerHTML = '👁️ Mẫu: Mờ';
        btn.title = 'Mẫu chữ đang mờ 25% để bạn tập nhớ nét';
        showToast("Mẫu chữ đã làm mờ 25% để bạn tập nhớ!");
    } else if (curr > 0.1) {
        curr = 0;
        btn.innerHTML = '🙈 Mẫu: Ẩn';
        btn.title = 'Mẫu chữ đã ẩn để bạn tự nhớ và viết hoàn toàn';
        showToast("Đã ẩn mẫu chữ để bạn tự nhớ viết hoàn toàn!");
    } else {
        curr = 1;
        btn.innerHTML = '👁️ Mẫu: Rõ';
        btn.title = 'Mẫu chữ hiển thị đầy đủ 100%';
        showToast("Đã hiện mẫu chữ rõ 100%!");
    }
    svgCont.dataset.opacity = curr;
    svgCont.style.opacity = curr;
}

// EXERCISE 1: TYPING READING
function renderTypingExercise() {
    const tbody = document.getElementById('exTableBody');
    tbody.innerHTML = '';
    document.getElementById('exScoreBanner').style.display = 'none';

    // Collect all unique vocabulary examples from filtered Kanji
    const map = new Map();
    filteredKanji.forEach(k => {
        k.examples.forEach(ex => {
            if (!map.has(ex.word)) {
                map.set(ex.word, ex);
            }
        });
    });

    currentVocabExercises = Array.from(map.values());

    currentVocabExercises.forEach((ex, idx) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td class="col-ex-stt"><strong>#${idx + 1}</strong></td>
            <td class="col-ex-word"><span class="ex-kanji-word">${ex.word}</span></td>
            <td class="col-ex-meaning"><span class="ex-meaning-text">${ex.vi}</span></td>
            <td class="col-ex-input">
                <input type="text" class="ex-input" id="ex-in-${idx}" placeholder="Nhập Hiragana...">
                <div class="ex-hint" id="ex-hint-${idx}" style="display:${showHints ? 'block' : 'none'}">👉 Đáp án: <strong>${ex.reading}</strong></div>
            </td>
            <td class="col-ex-status" id="ex-status-${idx}"></td>
        `;
        tbody.appendChild(tr);

        const inp = tr.querySelector(`#ex-in-${idx}`);
        if (inp) {
            if (typeof typingAnswers[ex.word] === 'string') {
                inp.value = typingAnswers[ex.word];
            }
            inp.addEventListener('input', () => {
                typingAnswers[ex.word] = inp.value;
                typingGraded = false;
                saveKanjiCheckpoint();
            });
        }
    });

    if (typingGraded && currentVocabExercises.length > 0) {
        gradeTypingExercise({ skipSave: true });
    }
}

function gradeTypingExercise(opts) {
    let correct = 0;
    const total = currentVocabExercises.length;
    if (total === 0) return;
    typingGraded = true;

    currentVocabExercises.forEach((ex, idx) => {
        const input = document.getElementById(`ex-in-${idx}`);
        const status = document.getElementById(`ex-status-${idx}`);
        const val = input.value.trim();

        if (val === ex.reading) {
            correct++;
            input.classList.remove('wrong');
            input.classList.add('correct');
            status.innerHTML = '✅';
        } else {
            input.classList.remove('correct');
            input.classList.add('wrong');
            status.innerHTML = '❌';
        }
    });

    const banner = document.getElementById('exScoreBanner');
    const percent = Math.round((correct / total) * 100);
    banner.style.display = 'block';
    banner.innerHTML = `🎉 Kết quả: Đúng ${correct}/${total} từ (${percent}%)`;
    if (!(opts && opts.skipSave)) saveKanjiCheckpoint();
}

function toggleExerciseHints() {
    showHints = !showHints;
    currentVocabExercises.forEach((_, idx) => {
        const h = document.getElementById(`ex-hint-${idx}`);
        if (h) h.style.display = showHints ? 'block' : 'none';
    });
    saveKanjiCheckpoint();
}

function resetTypingExercise() {
    typingAnswers = {};
    typingGraded = false;
    showHints = false;
    renderTypingExercise();
    saveKanjiCheckpoint();
}

// EXERCISE 2: MULTIPLE CHOICE QUIZ
function generateQuiz() {
    const pool = filteredKanji.length >= 4 ? filteredKanji : kanjiData;
    const target = pool[Math.floor(Math.random() * pool.length)];
    const ex = target.examples[0];

    // Randomly pick quiz type: 0 = Kanji -> Reading/Meaning, 1 = Reading -> Kanji
    const quizType = Math.random() > 0.5 ? 0 : 1;

    const promptEl = document.getElementById('quizPrompt');
    const subEl = document.getElementById('quizQuestionText');
    const tagEl = document.getElementById('quizTag');
    const optBox = document.getElementById('quizOptionsBox');
    const nextBtn = document.getElementById('nextQuizBtn');

    nextBtn.style.display = 'none';
    optBox.innerHTML = '';

    const wrongPool = kanjiData.filter(k => k.char !== target.char).sort(() => 0.5 - Math.random()).slice(0, 3);

    if (quizType === 0) {
        tagEl.innerText = `${target.lessonName} • Hán Việt: ${target.hv.toUpperCase()}`;
        promptEl.innerText = ex.word;
        subEl.innerText = "Chọn cách đọc và nghĩa đúng của từ Kanji trên:";

        const correctAns = `${ex.reading} (${ex.vi})`;
        const options = [
            correctAns,
            `${wrongPool[0].examples[0].reading} (${wrongPool[0].examples[0].vi})`,
            `${wrongPool[1].examples[0].reading} (${wrongPool[1].examples[0].vi})`,
            `${wrongPool[2].examples[0].reading} (${wrongPool[2].examples[0].vi})`
        ].sort(() => 0.5 - Math.random());

        renderQuizOptions(options, correctAns, optBox, nextBtn);
    } else {
        tagEl.innerText = `${target.lessonName} • Chọn Chữ Hán Đúng`;
        promptEl.innerText = `${ex.reading}`;
        subEl.innerText = `Nghĩa là "${ex.vi}". Đâu là chữ Kanji đúng?`;

        const correctAns = `${ex.word} [Hán Việt: ${target.hv}]`;
        const options = [
            correctAns,
            `${wrongPool[0].examples[0].word} [Hán Việt: ${wrongPool[0].hv}]`,
            `${wrongPool[1].examples[0].word} [Hán Việt: ${wrongPool[1].hv}]`,
            `${wrongPool[2].examples[0].word} [Hán Việt: ${wrongPool[2].hv}]`
        ].sort(() => 0.5 - Math.random());

        renderQuizOptions(options, correctAns, optBox, nextBtn);
    }
}

function renderQuizOptions(options, correctAns, optBox, nextBtn) {
    options.forEach(opt => {
        const btn = document.createElement('button');
        btn.className = 'quiz-opt';
        btn.innerText = opt;
        btn.onclick = () => {
            const all = optBox.querySelectorAll('.quiz-opt');
            all.forEach(b => b.disabled = true);
            if (opt === correctAns) {
                btn.classList.add('correct');
            } else {
                btn.classList.add('wrong');
                all.forEach(b => {
                    if (b.innerText === correctAns) b.classList.add('correct');
                });
            }
            nextBtn.style.display = 'inline-flex';
        };
        optBox.appendChild(btn);
    });
}

function restoreKanjiCheckpoint() {
    try {
        const raw = localStorage.getItem(KANJI_CP_KEY);
        if (!raw) return false;
        const saved = JSON.parse(raw);
        if (!saved || typeof saved !== 'object') return false;
        isRestoringKanji = true;

        if (Array.isArray(saved.selectedLessons)) {
            selectedLessons = new Set(saved.selectedLessons);
        }
        const searchEl = document.getElementById('searchInput');
        if (searchEl && typeof saved.searchQuery === 'string') {
            searchEl.value = saved.searchQuery;
        }
        if (saved.current121Lesson !== undefined && typeof current121Lesson !== 'undefined') {
            current121Lesson = saved.current121Lesson;
            document.querySelectorAll('.filter-121-btn').forEach(btn => {
                const oc = btn.getAttribute('onclick') || '';
                const isMatch = current121Lesson === 'ALL'
                    ? oc.includes("'ALL'")
                    : new RegExp(`filter121Vocab\\(['"]?${current121Lesson}['"]?`).test(oc);
                btn.classList.toggle('active', isMatch);
            });
        }
        const search121El = document.getElementById('search121Input');
        if (search121El && typeof saved.search121Query === 'string') {
            search121El.value = saved.search121Query;
        }
        if (saved.typingAnswers && typeof saved.typingAnswers === 'object') {
            typingAnswers = saved.typingAnswers;
        }
        typingGraded = Boolean(saved.typingGraded);
        showHints = Boolean(saved.showHints);

        initKanjiLessonChips();
        updatePresetPillsState();
        if (typeof updateChipsUI === 'function') updateChipsUI();
        applyLessonFilter();
        if (typeof apply121Filter === 'function') apply121Filter({ skipSave: true });

        if (saved.currentKanjiTab) {
            switchTab(saved.currentKanjiTab, { isRestore: true, skipSave: true });
        }

        isRestoringKanji = false;
        return true;
    } catch (e) {
        isRestoringKanji = false;
        return false;
    }
}

window.addEventListener('DOMContentLoaded', () => {
    if (!restoreKanjiCheckpoint()) {
        initKanjiLessonChips();
        isRestoringKanji = true;
        applyLessonFilter();
        isRestoringKanji = false;
    }
});









function toggleLessonFilterDrawer() {
    const drawer = document.getElementById('lessonFilterDrawer');
    const arrow = document.getElementById('drawerArrow');
    const btn = document.getElementById('btnToggleDrawer');
    if (!drawer) return;
    const isOpen = drawer.classList.toggle('open');
    if (arrow) arrow.textContent = isOpen ? '▴' : '▾';
    if (btn) btn.classList.toggle('active', isOpen);
}







