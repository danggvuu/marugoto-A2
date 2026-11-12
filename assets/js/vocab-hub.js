/* Vocab Hub Table, 3D Integration & Checkpoint Engine */

const TV_CP_KEY = 'marugoto_tuvung_portal_cp_v1';
window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;
window.__MARUGOTO_CP_EXTRA_KEYS__ = [TV_CP_KEY];
window.__MARUGOTO_ON_RESET__ = function () {
    try { localStorage.removeItem(TV_CP_KEY); } catch (e) {}
    window.location.reload();
};

let currentView = 'view-table';
let isRestoringTv = false;
let currentFiltered = [...rawVocab];
let currentCardIndex = 0;
let cardFlipped = false;

function saveTvCheckpoint() {
    if (isRestoringTv) return;
    try {
        const searchEl = document.getElementById('searchInput');
        const activePanel = document.querySelector('.view-panel.active');
        const payload = {
            t: Date.now(),
            currentView: currentView || (activePanel ? activePanel.id : 'view-table'),
            selectedLessons: Array.from(selectedLessons),
            currentLevelScope,
            isMultiSelectMode,
            searchQuery: searchEl ? searchEl.value : '',
            currentCardIndex,
            cardFlipped,
            cardSidePrompt,
            cardOrder: currentFiltered.map(x => `${x.l}|${x.kanji}|${x.kana}`),
            quizSettings,
            quizSession: quizSession && Array.isArray(quizSession.questions) && quizSession.questions.length > 0 ? quizSession : null
        };
        localStorage.setItem(TV_CP_KEY, JSON.stringify(payload));
        if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
            window.MarugotoCheckpoint.notifySaved();
        }
    } catch (e) {}
}

// View Switching
function switchView(viewId, opts) {
    currentView = viewId;
    document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
    const target = document.getElementById(viewId);
    if (target) target.classList.add('active');
    const activeBtn = Array.from(document.querySelectorAll('.mode-btn')).find(b => b.getAttribute('onclick')?.includes(viewId));
    if (activeBtn) activeBtn.classList.add('active');

    if (viewId === 'view-flashcard') {
        if (!(opts && opts.isRestore)) {
            currentCardIndex = 0;
            cardFlipped = false;
        }
        renderCard();
    } else if (viewId === 'view-quiz') {
        if (!(opts && opts.isRestore) || !quizSession.questions || quizSession.questions.length === 0) {
            startNewQuizTest();
        }
    }
    if (!(opts && opts.skipSave)) {
        saveTvCheckpoint();
    }
}

// ==========================================
// ==========================================
// MULTI-LESSON SELECTION & FILTER LOGIC
// ==========================================
const LESSON_ORDER = [
    "A1-3",
    "A1-4",
    "A1-5",
    "A1-6",
    "A1-7",
    "A1-8",
    "A1-9",
    "A1-10",
    "A1-11",
    "A1-12",
    "A1-13",
    "A1-14",
    "A1-15",
    "A1-16",
    "A1-17",
    "A1-18",
    "A2-1",
    "A2-2",
    "A2-3",
    "A2-4",
    "A2-5",
    "A2-6",
    "A2-7",
    "A2-8",
    "A2-9",
    "A2-10",
    "A2-11",
    "A2-12",
    "A2-13",
    "A2-14",
    "A2-15",
    "A2-16",
    "A2-17",
    "A2-18"
];

const LESSON_TITLES = {
    "A1-3": "Bài 3: Gia đình tôi có 4 người (かぞくは よにんです。)",
    "A1-4": "Bài 4: Gia đình tôi có 4 người (かぞくは よにんです。)",
    "A1-5": "Bài 5: Bạn thích gì? (なにがすきですか。)",
    "A1-6": "Bài 6: Bạn ăn ở đâu? (どこで たべますか。)",
    "A1-7": "Bài 7: Có 3 phòng (へやが みっつ あります。)",
    "A1-8": "Bài 8: Phòng đẹp nhỉ (いい へやですね。)",
    "A1-9": "Bài 9: Mấy giờ thức dậy? (なんじに おきますか。)",
    "A1-10": "Bài 10: Khi nào thì được? (いつが いいですか。)",
    "A1-11": "Bài 11: Sở thích của bạn là gì? (しゅみは なんですか。)",
    "A1-12": "Bài 12: Cùng đi không? (いっしょに いきませんか。)",
    "A1-13": "Bài 13: Đi bằng phương tiện gì? (どうやって いきますか。)",
    "A1-14": "Bài 14: Ngôi chùa nổi tiếng (ゆうめいな おてらです。)",
    "A1-15": "Bài 15: Dễ thương quá! (かわいい！)",
    "A1-16": "Bài 16: Mua sắm (これ、ください。)",
    "A1-17": "Bài 17: Trải nghiệm (たのしかったです。)",
    "A1-18": "Bài 18: Du lịch (つぎは きょうとに いきたいです。)",
    "A2-1": "Bài 1: Nơi ở (東京に すんでいます。)",
    "A2-2": "Bài 2: Sở thích (しゅみは クラシックを 聞くことです。)",
    "A2-3": "Bài 3: Mùa & Khí hậu (日本はいま、はるです。)",
    "A2-4": "Bài 4: Thời tiết (いい てんきですね。)",
    "A2-5": "Bài 5: Phố xá & Công viên (この こうえんは ひろくて、きれいです。)",
    "A2-6": "Bài 6: Chỉ đường (まっすぐ 行ってください。)",
    "A2-7": "Bài 7: Hẹn gặp (10時でも いいですか。)",
    "A2-8": "Bài 8: Cảnh đêm (もう やけいを 見に 行きましたか。)",
    "A2-9": "Bài 9: Ngôn ngữ & Phát âm (日本語は はつおんが かんたんです。)",
    "A2-10": "Bài 10: Tiếng Nhật (日本語は はつおんが かんたんです。)",
    "A2-11": "Bài 11: Mang theo cái gì dã ngoại (何を 持っていきますか。)",
    "A2-12": "Bài 12: Món ăn ngon & Vị giác (おいしそうですね。)",
    "A2-13": "Bài 13: Gặp gỡ & Chuyến công tác (たなかさんに 会ったことが ありますか。)",
    "A2-14": "Bài 14: Văn phòng & Quy tắc (これ、つかっても いいですか。)",
    "A2-15": "Bài 15: Sức khỏe & Thể dục (たいそうすると いいですよ。)",
    "A2-16": "Bài 16: Tập luyện & Vận động (はしったり およいだり しています。)",
    "A2-17": "Bài 17: Quà tặng sinh nhật (誕生日に もらったんです。)",
    "A2-18": "Bài 18: Tiệc tùng & Sự kiện (パーティーが いいと おもいます。)"
};

let selectedLessons = new Set(LESSON_ORDER); // Mặc định chọn tất cả
let currentLevelScope = 'ALL';
let isMultiSelectMode = false;
let isAdvancedDrawerOpen = false;

// Đếm số từ vựng từng bài
const lessonCounts = {};
rawVocab.forEach(item => {
    lessonCounts[item.l] = (lessonCounts[item.l] || 0) + 1;
});

// Khởi tạo các Dropdown, Level Tabs & Chips
function initLessonChips() {
    const optA1 = document.getElementById('optGroupA1');
    const optA2_1 = document.getElementById('optGroupA2_1');
    const optA2_2 = document.getElementById('optGroupA2_2');
    const rangeStart = document.getElementById('rangeStart');
    const rangeEnd = document.getElementById('rangeEnd');

    const drawerA1 = document.getElementById('drawerChipsA1');
    const drawerA2_1 = document.getElementById('drawerChipsA2_1');
    const drawerA2_2 = document.getElementById('drawerChipsA2_2');

    if (optA1) optA1.innerHTML = '';
    if (optA2_1) optA2_1.innerHTML = '';
    if (optA2_2) optA2_2.innerHTML = '';
    if (rangeStart) rangeStart.innerHTML = '';
    if (rangeEnd) rangeEnd.innerHTML = '';
    if (drawerA1) drawerA1.innerHTML = '';
    if (drawerA2_1) drawerA2_1.innerHTML = '';
    if (drawerA2_2) drawerA2_2.innerHTML = '';

    LESSON_ORDER.forEach((lid, idx) => {
        const count = lessonCounts[lid] || 0;
        const fullTitle = LESSON_TITLES[lid] || lid;
        const shortTitle = fullTitle.split('(')[0].trim();

        // 1. Điền vào 1-Click Dropdown
        const opt = document.createElement('option');
        opt.value = lid;
        opt.textContent = `${lid}: ${shortTitle} (${count} từ)`;

        if (lid.startsWith('A1')) {
            if (optA1) optA1.appendChild(opt);
        } else {
            const num = parseInt(lid.split('-')[1], 10);
            if (num <= 10) {
                if (optA2_1) optA2_1.appendChild(opt);
            } else {
                if (optA2_2) optA2_2.appendChild(opt);
            }
        }

        // 2. Điền vào Range Dropdowns
        if (rangeStart && rangeEnd) {
            const rOpt1 = document.createElement('option');
            rOpt1.value = lid;
            rOpt1.textContent = `${lid} - ${shortTitle}`;
            rangeStart.appendChild(rOpt1);

            const rOpt2 = document.createElement('option');
            rOpt2.value = lid;
            rOpt2.textContent = `${lid} - ${shortTitle}`;
            rangeEnd.appendChild(rOpt2);
        }

        // 3. Điền vào Drawer Chips Grid
        let targetDrawer = drawerA1;
        if (!lid.startsWith('A1')) {
            const num = parseInt(lid.split('-')[1], 10);
            targetDrawer = num <= 10 ? drawerA2_1 : drawerA2_2;
        }
        if (targetDrawer) {
            const chip = document.createElement('button');
            chip.type = 'button';
            chip.className = `lesson-chip ${selectedLessons.has(lid) ? 'active' : ''}`;
            chip.id = `drawer-chip-${lid}`;
            chip.title = `${fullTitle} (${count} từ)`;
            chip.innerHTML = `<span>${lid}</span><span class="chip-count">${count}</span>`;
            chip.onclick = (e) => onChipClick(lid, e);
            targetDrawer.appendChild(chip);
        }
    });

    if (rangeStart && rangeEnd) {
        rangeStart.value = "A1-3";
        rangeEnd.value = "A2-18";
    }

    renderActiveChipsBar();
    updateLessonUIState();
}

// Hiển thị thanh bài học tương ứng với nhóm đang chọn (Gọn gàng 1 dòng ngang)
function renderActiveChipsBar() {
    const bar = document.getElementById('activeChipsBar');
    if (!bar) return;
    bar.innerHTML = '';

    let targetLessons = LESSON_ORDER;
    if (currentLevelScope === 'A1') {
        targetLessons = LESSON_ORDER.filter(l => l.startsWith('A1'));
    } else if (currentLevelScope === 'A2_1') {
        targetLessons = ["A2-1", "A2-2", "A2-3", "A2-4", "A2-5", "A2-6", "A2-7", "A2-8", "A2-9", "A2-10"];
    } else if (currentLevelScope === 'A2_2') {
        targetLessons = ["A2-11", "A2-12", "A2-13", "A2-14", "A2-15", "A2-16", "A2-17", "A2-18"];
    }

    targetLessons.forEach(lid => {
        const count = lessonCounts[lid] || 0;
        const fullTitle = LESSON_TITLES[lid] || lid;
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = `lesson-chip ${selectedLessons.has(lid) ? 'active' : ''}`;
        chip.id = `active-chip-${lid}`;
        chip.title = `${fullTitle} (${count} từ) - Bấm để xem bài này`;
        chip.innerHTML = `<span>${lid}</span><span class="chip-count">${count}</span>`;
        chip.onclick = (e) => onChipClick(lid, e);
        bar.appendChild(chip);
    });
}

// Xử lý khi click vào 1 Chip bài học:
// - Mặc định (Single-select): Chuyển thẳng sang xem bài đó (1-click ăn ngay!)
// - Khi bật multi-select (hoặc giữ Shift): Bật / tắt thêm bài đó vào danh sách
function onChipClick(lid, e) {
    if (!isMultiSelectMode && !(e && (e.shiftKey || e.ctrlKey || e.metaKey))) {
        // Xem duy nhất bài này
        selectedLessons.clear();
        selectedLessons.add(lid);

        // Tự động định vị nhóm cấp độ tương ứng
        if (lid.startsWith('A1')) currentLevelScope = 'A1';
        else {
            const num = parseInt(lid.split('-')[1], 10);
            currentLevelScope = num <= 10 ? 'A2_1' : 'A2_2';
        }
        renderActiveChipsBar();
        showToast(`📖 Đang xem: ${lid} (${lessonCounts[lid] || 0} từ vựng)`);
    } else {
        // Chế độ chọn nhiều bài
        if (selectedLessons.has(lid)) {
            selectedLessons.delete(lid);
        } else {
            selectedLessons.add(lid);
        }
    }

    updateLessonUIState();
    applyFilter();
}

// Xử lý khi chọn từ Dropdown chọn nhanh
function onQuickLessonChange(value) {
    if (value === 'ALL') {
        selectLevelScope('ALL');
        return;
    }

    selectedLessons.clear();
    selectedLessons.add(value);

    if (value.startsWith('A1')) currentLevelScope = 'A1';
    else {
        const num = parseInt(value.split('-')[1], 10);
        currentLevelScope = num <= 10 ? 'A2_1' : 'A2_2';
    }

    renderActiveChipsBar();
    updateLessonUIState();
    applyFilter();
    showToast(`📖 Đang xem bài: ${value} (${lessonCounts[value] || 0} từ)`);
}

// Chọn nhanh theo nhóm Cấp độ
function selectLevelScope(scope) {
    currentLevelScope = scope;

    if (scope === 'ALL') {
        selectedLessons = new Set(LESSON_ORDER);
        showToast(`🌟 Đang chọn: Toàn bộ 34 bài (1.200+ từ)`);
    } else if (scope === 'A1') {
        selectedLessons = new Set(LESSON_ORDER.filter(l => l.startsWith('A1')));
        showToast(`📗 Đang chọn: Toàn bộ nhóm A1 (Bài 3 - 18)`);
    } else if (scope === 'A2_1') {
        selectedLessons = new Set(["A2-1", "A2-2", "A2-3", "A2-4", "A2-5", "A2-6", "A2-7", "A2-8", "A2-9", "A2-10"]);
        showToast(`📘 Đang chọn: Nhóm A2-1 (Bài 1 - 10)`);
    } else if (scope === 'A2_2') {
        selectedLessons = new Set(["A2-11", "A2-12", "A2-13", "A2-14", "A2-15", "A2-16", "A2-17", "A2-18"]);
        showToast(`💻 Đang chọn: Nhóm A2-1 (Bài 11 - 18 Mới ✨)`);
    }

    renderActiveChipsBar();
    updateLessonUIState();
    applyFilter();
}

// Bật/tắt Drawer Nâng cao & Chọn nhiều bài
function toggleAdvancedDrawer() {
    isAdvancedDrawerOpen = !isAdvancedDrawerOpen;
    const drawer = document.getElementById('advancedDrawer');
    const btn = document.getElementById('btnAdvExpand');
    if (drawer) drawer.style.display = isAdvancedDrawerOpen ? 'flex' : 'none';
    if (btn) {
        btn.classList.toggle('active', isAdvancedDrawerOpen);
        btn.innerHTML = isAdvancedDrawerOpen ? '⚙️ Thu gọn ▴' : '⚙️ Chọn nhiều bài ▾';
    }
}

// Bật/tắt chế độ multi-select
function toggleMultiSelectMode(enabled) {
    isMultiSelectMode = enabled;
    showToast(enabled ? '✅ Đã BẬT chế độ chọn nhiều bài!' : '⚡ Đã TẮT (Click bài nào xem ngay bài đó)!');
}

// Preset All / None từ Drawer
function selectPreset(type) {
    if (type === 'ALL') {
        selectedLessons = new Set(LESSON_ORDER);
        currentLevelScope = 'ALL';
        renderActiveChipsBar();
    } else if (type === 'NONE') {
        selectedLessons.clear();
    }

    updateLessonUIState();
    applyFilter();
}

// Áp dụng chọn dải bài liên tục
function applyRangeSelection() {
    const startId = document.getElementById('rangeStart').value;
    const endId = document.getElementById('rangeEnd').value;
    const sIdx = LESSON_ORDER.indexOf(startId);
    const eIdx = LESSON_ORDER.indexOf(endId);

    if (sIdx === -1 || eIdx === -1) return;
    const start = Math.min(sIdx, eIdx);
    const end = Math.max(sIdx, eIdx);

    selectedLessons.clear();
    for (let i = start; i <= end; i++) {
        selectedLessons.add(LESSON_ORDER[i]);
    }

    updateLessonUIState();
    applyFilter();
    showToast(`🎯 Đã chọn dải bài: ${LESSON_ORDER[start]} ➔ ${LESSON_ORDER[end]} (${end - start + 1} bài)!`);
}

// Cập nhật giao diện đồng bộ tất cả controls
function updateLessonUIState() {
    // 1. Cập nhật Level Pills
    document.querySelectorAll('.level-pill').forEach(btn => btn.classList.remove('active'));
    if (selectedLessons.size === LESSON_ORDER.length) {
        document.getElementById('pill-all')?.classList.add('active');
    } else if (currentLevelScope === 'A1' && Array.from(selectedLessons).every(l => l.startsWith('A1')) && selectedLessons.size === 16) {
        document.getElementById('pill-a1')?.classList.add('active');
    } else if (currentLevelScope === 'A2_1' && selectedLessons.size === 10) {
        document.getElementById('pill-a2-1')?.classList.add('active');
    } else if (currentLevelScope === 'A2_2' && selectedLessons.size === 8) {
        document.getElementById('pill-a2-2')?.classList.add('active');
    }

    // 2. Cập nhật Active Chips & Drawer Chips
    LESSON_ORDER.forEach(lid => {
        const isSel = selectedLessons.has(lid);
        const activeChip = document.getElementById(`active-chip-${lid}`);
        if (activeChip) activeChip.classList.toggle('active', isSel);

        const drawerChip = document.getElementById(`drawer-chip-${lid}`);
        if (drawerChip) drawerChip.classList.toggle('active', isSel);
    });

    // 3. Cập nhật Dropdown chọn nhanh
    const dropdown = document.getElementById('quickLessonDropdown');
    if (dropdown) {
        if (selectedLessons.size === 1) {
            dropdown.value = Array.from(selectedLessons)[0];
        } else if (selectedLessons.size === LESSON_ORDER.length) {
            dropdown.value = 'ALL';
        } else {
            dropdown.value = 'ALL';
        }
    }

    // 4. Cập nhật Summary Badge
    const summary = document.getElementById('selectionSummary');
    if (summary) {
        if (selectedLessons.size === LESSON_ORDER.length) {
            summary.textContent = `Toàn bộ 34 bài (${rawVocab.length} từ)`;
        } else if (selectedLessons.size === 0) {
            summary.textContent = `Chưa chọn bài nào`;
        } else if (selectedLessons.size === 1) {
            const only = Array.from(selectedLessons)[0];
            summary.textContent = `Đang xem: ${only} (${lessonCounts[only] || 0} từ)`;
        } else {
            summary.textContent = `Đang chọn: ${selectedLessons.size} bài (${currentFiltered ? currentFiltered.length : 0} từ)`;
        }
    }
}

function closeMiniMotion() {
    const widget = document.getElementById('miniMotionWidget');
    if (widget) {
        widget.style.display = 'none';
    }
}

let vocabSearchDebounceTimer = null;
function onSearchChange() {
    const query = document.getElementById('searchInput').value;
    const clearBtn = document.getElementById('searchClearBtn');
    if (clearBtn) clearBtn.style.display = query ? 'block' : 'none';
    clearTimeout(vocabSearchDebounceTimer);
    vocabSearchDebounceTimer = setTimeout(applyFilter, 120);
}

function clearSearch() {
    const input = document.getElementById('searchInput');
    input.value = '';
    const clearBtn = document.getElementById('searchClearBtn');
    if (clearBtn) clearBtn.style.display = 'none';
    applyFilter();
}

// ==========================================
// FILTER LOGIC (Kanji, Kana, Han-Viet, Romaji, Vietnamese)
// ==========================================
function applyFilter(opts) {
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
    if (!(opts && opts.isRestore)) {
        currentCardIndex = 0;
        cardFlipped = false;
        if (document.getElementById('view-flashcard').classList.contains('active')) {
            renderCard();
        }
        if (document.getElementById('view-quiz').classList.contains('active')) {
            startNewQuizTest();
        }
    }
    if (!(opts && opts.skipSave)) {
        saveTvCheckpoint();
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
        const safeKana = (item.kana || item.jp).replace(/'/g, "\\'");
        const safeKanji = (item.kanji || item.jp).replace(/'/g, "\\'");
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
                <div class="sub-kana-mobile">${item.kana !== item.kanji ? item.kana : ''} ${item.hv ? `<span class="badge-hv-mobile">${item.hv}</span>` : ''}</div>
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
// AUDIO HELPER (Unified via audio-engine.js)
// ==========================================

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

function flipCard() {
    cardFlipped = !cardFlipped;
    const cardInner = document.getElementById('fcCardInner');
    if (cardInner) {
        cardInner.classList.toggle('is-flipped', cardFlipped);
    }
    saveTvCheckpoint();
}

function nextCard() {
    if (currentFiltered.length === 0) return;
    currentCardIndex = (currentCardIndex + 1) % currentFiltered.length;
    cardFlipped = false;
    renderCard();
    saveTvCheckpoint();
}

function prevCard() {
    if (currentFiltered.length === 0) return;
    currentCardIndex = (currentCardIndex - 1 + currentFiltered.length) % currentFiltered.length;
    cardFlipped = false;
    renderCard();
    saveTvCheckpoint();
}

function shuffleCards() {
    if (currentFiltered.length === 0) return;
    for (let i = currentFiltered.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [currentFiltered[i], currentFiltered[j]] = [currentFiltered[j], currentFiltered[i]];
    }
    currentCardIndex = 0;
    cardFlipped = false;
    renderCard();
    showToast("🔀 Đã xáo trộn danh sách thẻ!");
    saveTvCheckpoint();
}

function toggleCardSidePrompt() {
    cardSidePrompt = (cardSidePrompt === 'jp') ? 'vi' : 'jp';
    cardFlipped = false;
    const label = document.getElementById('lblToggleSide');
    if (label) {
        label.textContent = cardSidePrompt === 'jp' ? "Mặt trước: Tiếng Nhật" : "Mặt trước: Tiếng Việt";
    }
    renderCard();
    showToast(cardSidePrompt === 'jp' ? "Đã chuyển: Mặt trước là Tiếng Nhật" : "Đã chuyển: Mặt trước là Tiếng Việt");
    saveTvCheckpoint();
}

// ==========================================
// QUIZ LOGIC (QUIZLET TEST SETTINGS & ENGINE)
// ==========================================
let quizSettings = {
    answerWith: 'vi', // 'vi' (Đề Nhật -> Chọn Việt), 'jp' (Đề Việt -> Chọn Nhật), 'both'
    count: 20,       // 10, 20, 30, 'all'
    mode: 'instant',  // 'instant' (báo đúng/sai ngay), 'test' (làm hết rồi nộp bài)
    autoSpeak: false  // Tắt mặc định để không gây ồn ào giật mình
};

let quizSession = {
    questions: [],
    currentIndex: 0,
    correctCount: 0,
    wrongCount: 0,
    answered: false,
    wrongItems: []
};

function toggleQuizSettings() {
    const panel = document.getElementById('quizSettingsPanel');
    if (panel) panel.classList.toggle('open');
}

function applyQuizSettingsAndRestart() {
    const selAnswer = document.getElementById('qsettingAnswerWith');
    const selCount = document.getElementById('qsettingCount');
    const selMode = document.getElementById('qsettingMode');
    const chkSpeak = document.getElementById('qsettingAutoSpeak');

    if (selAnswer) quizSettings.answerWith = selAnswer.value;
    if (selCount) quizSettings.count = selCount.value === 'all' ? 'all' : parseInt(selCount.value, 10);
    if (selMode) quizSettings.mode = selMode.value;
    if (chkSpeak) quizSettings.autoSpeak = chkSpeak.checked;

    toggleQuizSettings();
    startNewQuizTest();
    showToast("⚡ Đã áp dụng cài đặt Quizlet mới!");
}

function startNewQuizTest(customPool = null) {
    if (currentFiltered.length === 0) {
        showToast("Chưa có từ vựng nào được chọn!");
        return;
    }

    // Tạo pool từ vựng
    const basePool = customPool ? [...customPool] : [...currentFiltered];
    // Shuffle base pool
    for (let i = basePool.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [basePool[i], basePool[j]] = [basePool[j], basePool[i]];
    }

    // Xác định số lượng câu
    let totalQ = basePool.length;
    if (quizSettings.count !== 'all') {
        totalQ = Math.min(totalQ, parseInt(quizSettings.count, 10));
    }
    const selectedItems = basePool.slice(0, totalQ);

    // Tạo câu hỏi
    const questions = selectedItems.map(item => {
        let direction = quizSettings.answerWith;
        if (direction === 'both') {
            direction = Math.random() > 0.5 ? 'vi' : 'jp';
        }

        const promptText = (direction === 'vi') ? item.jp : item.vi;
        const correctAnswer = (direction === 'vi') ? item.vi : item.jp;
        const promptType = (direction === 'vi') ? 'Tiếng Nhật ➔ Chọn Tiếng Việt' : 'Tiếng Việt ➔ Chọn Tiếng Nhật';
        const instruction = (direction === 'vi') ? 'Chọn nghĩa tiếng Việt chính xác nhất:' : 'Chọn từ tiếng Nhật tương ứng:';

        // 3 đáp án sai: CHỈ lấy từ vựng trong các bài ĐANG CHỌN (tuyệt đối không lấy từ bài cao hơn chưa học)
        let distractorPool = basePool.filter(x => (direction === 'vi' ? x.vi !== item.vi : x.jp !== item.jp));

        // Nếu bài đang chọn có quá ít từ, chỉ được phép lấy thêm từ các bài CŨ HƠN (không bao giờ lấy bài tương lai)
        if (distractorPool.length < 3) {
            const maxSelectedIdx = Math.max(...Array.from(selectedLessons).map(l => LESSON_ORDER.indexOf(l)), 0);
            const allowedLessons = rawVocab.filter(x => LESSON_ORDER.indexOf(x.l) <= maxSelectedIdx);
            distractorPool = allowedLessons.filter(x => (direction === 'vi' ? x.vi !== item.vi : x.jp !== item.jp));
        }

        const shuffledWrong = distractorPool.sort(() => 0.5 - Math.random());
        const wrongOptions = [];
        for (let w of shuffledWrong) {
            const val = (direction === 'vi') ? w.vi : w.jp;
            if (!wrongOptions.includes(val) && val !== correctAnswer) {
                wrongOptions.push(val);
            }
            if (wrongOptions.length === 3) break;
        }

        const allOpts = [correctAnswer, ...wrongOptions].sort(() => 0.5 - Math.random());

        return {
            rawItem: item,
            direction,
            promptText,
            correctAnswer,
            promptType,
            instruction,
            options: allOpts
        };
    });

    quizSession = {
        questions,
        currentIndex: 0,
        correctCount: 0,
        wrongCount: 0,
        answered: false,
        lastSelectedOpt: null,
        wrongItems: []
    };

    const activeBox = document.getElementById('quizActiveBox');
    const resView = document.getElementById('quizResultView');
    if (activeBox) activeBox.style.display = 'block';
    if (resView) resView.style.display = 'none';

    renderQuizQuestion();
    saveTvCheckpoint();
}

function renderQuizQuestion(opts) {
    if (quizSession.questions.length === 0) return;
    const q = quizSession.questions[quizSession.currentIndex];
    if (!(opts && opts.preserveAnswered)) {
        quizSession.answered = false;
        quizSession.lastSelectedOpt = null;
    }

    const totalQ = quizSession.questions.length;
    const curIdx = quizSession.currentIndex + 1;
    const pct = Math.round((curIdx / totalQ) * 100);

    // Top Toolbar Stats
    document.getElementById('quizCurrentProgress').innerText = `${curIdx} / ${totalQ}`;
    document.getElementById('quizCorrectCount').innerText = quizSession.correctCount;
    document.getElementById('quizWrongCount').innerText = quizSession.wrongCount;
    document.getElementById('quizProgressFill').style.width = `${pct}%`;

    // Card Content
    document.getElementById('quizLesson').innerText = q.rawItem.l;
    document.getElementById('quizPromptType').innerText = q.promptType;
    document.getElementById('quizQuestion').innerText = q.promptText;
    document.getElementById('quizInstruction').innerText = q.instruction;

    // Sound Button
    const soundBtn = document.getElementById('quizSoundBtn');
    if (soundBtn) {
        soundBtn.style.display = (q.direction === 'vi') ? 'flex' : 'none';
    }

    // Tự động phát âm tiếng Nhật nếu bật
    if (quizSettings.autoSpeak && q.direction === 'vi') {
        speakJapanese(q.rawItem.jp);
    }

    // Reset feedback banner
    const feedbackBanner = document.getElementById('quizFeedbackBanner');
    if (feedbackBanner) {
        feedbackBanner.className = 'quiz-feedback-banner';
        feedbackBanner.style.display = 'none';
    }

    // Options
    const optContainer = document.getElementById('quizOptions');
    optContainer.innerHTML = '';

    const keyLabels = ['1', '2', '3', '4'];
    q.options.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-opt-btn';
        btn.id = `quiz-opt-${idx}`;
        btn.innerHTML = `
        <span class="opt-key-badge">${keyLabels[idx] || idx + 1}</span>
        <span class="opt-text">${opt}</span>
    `;
        btn.onclick = () => handleQuizOptionClick(opt, btn, q);
        optContainer.appendChild(btn);
    });
}

function speakQuizWord() {
    if (quizSession.questions.length === 0) return;
    const q = quizSession.questions[quizSession.currentIndex];
    speakJapanese(q.rawItem.jp);
}

function handleQuizOptionClick(selectedOpt, btnEl, questionObj) {
    if (quizSession.answered) return;
    quizSession.answered = true;
    quizSession.lastSelectedOpt = selectedOpt;

    const isCorrect = (selectedOpt === questionObj.correctAnswer);
    const optContainer = document.getElementById('quizOptions');
    const allBtns = optContainer.querySelectorAll('.quiz-opt-btn');
    allBtns.forEach(b => b.disabled = true);

    if (isCorrect) {
        quizSession.correctCount++;
        btnEl.classList.add('correct');
    } else {
        quizSession.wrongCount++;
        btnEl.classList.add('wrong');
        quizSession.wrongItems.push(questionObj.rawItem);
        // Highlight the correct one
        allBtns.forEach(b => {
            const text = b.querySelector('.opt-text')?.innerText;
            if (text === questionObj.correctAnswer) {
                b.classList.add('correct');
            }
        });
    }

    // Update counts
    document.getElementById('quizCorrectCount').innerText = quizSession.correctCount;
    document.getElementById('quizWrongCount').innerText = quizSession.wrongCount;

    if (quizSettings.mode === 'instant') {
        // Luyện tập tức thì: hiển thị banner phản hồi
        const banner = document.getElementById('quizFeedbackBanner');
        const feedbackText = document.getElementById('quizFeedbackText');
        if (banner && feedbackText) {
            if (isCorrect) {
                banner.className = 'quiz-feedback-banner feedback-correct';
                feedbackText.innerHTML = `✓ Chính xác! Rất tốt.`;
            } else {
                banner.className = 'quiz-feedback-banner feedback-wrong';
                feedbackText.innerHTML = `✕ Chưa đúng! Đáp án đúng: <strong>${questionObj.correctAnswer}</strong> (${questionObj.rawItem.jp} : ${questionObj.rawItem.vi}) <button type="button" class="fc-audio-btn" style="position:static; width:32px; height:32px; font-size:0.9rem; display:inline-flex;" onclick="speakJapanese('${questionObj.rawItem.jp.replace(/'/g, "\\'")}')" title="Nghe đọc">🔊</button>`;
            }
            banner.style.display = 'flex';
        }
        saveTvCheckpoint();
    } else {
        saveTvCheckpoint();
        // Chế độ Thi thử (Test): Tự động chuyển câu sau 0.45s
        setTimeout(() => {
            advanceQuiz();
        }, 450);
    }
}

function onNextQuizClick() {
    advanceQuiz();
}

function advanceQuiz() {
    quizSession.currentIndex++;
    if (quizSession.currentIndex < quizSession.questions.length) {
        renderQuizQuestion();
    } else {
        showQuizResults();
    }
    saveTvCheckpoint();
}

function showQuizResults() {
    const activeBox = document.getElementById('quizActiveBox');
    const resView = document.getElementById('quizResultView');
    if (activeBox) activeBox.style.display = 'none';
    if (resView) resView.style.display = 'block';

    const total = quizSession.questions.length;
    const correct = quizSession.correctCount;
    const wrong = quizSession.wrongCount;
    const pct = Math.round((correct / total) * 100);

    document.getElementById('resultScorePct').innerText = `${pct}%`;
    document.getElementById('resultScoreFraction').innerText = `${correct} / ${total} câu đúng`;
    document.getElementById('resultCorrectCount').innerText = correct;
    document.getElementById('resultWrongCount').innerText = wrong;

    const resTitle = document.getElementById('resultTitle');
    const resDesc = document.getElementById('resultDesc');
    if (pct >= 90) {
        resTitle.innerText = "Xuất sắc! 🏆";
        resDesc.innerText = "Bạn đã nắm vững toàn bộ các từ vựng này rồi!";
    } else if (pct >= 70) {
        resTitle.innerText = "Làm tốt lắm! 🎉";
        resDesc.innerText = "Kết quả rất tốt, chỉ cần chú ý vài từ còn nhầm lẫn thôi.";
    } else {
        resTitle.innerText = "Cần cố gắng thêm! 💪";
        resDesc.innerText = "Hãy ôn lại các từ chưa thuộc và làm lại bài kiểm tra nhé.";
    }

    // Wrong items list
    const wrongCont = document.getElementById('wrongItemsContainer');
    const wrongList = document.getElementById('wrongItemsList');
    const btnReviewWrong = document.getElementById('btnReviewWrongOnly');

    if (quizSession.wrongItems.length > 0) {
        if (wrongCont) wrongCont.style.display = 'block';
        if (btnReviewWrong) btnReviewWrong.style.display = 'inline-flex';
        if (wrongList) {
            wrongList.innerHTML = '';
            const seen = new Set();
            const uniqueWrong = [];
            for (let it of quizSession.wrongItems) {
                if (!seen.has(it.jp)) {
                    seen.add(it.jp);
                    uniqueWrong.push(it);
                }
            }

            uniqueWrong.forEach(item => {
                const row = document.createElement('div');
                row.className = 'wrong-item-row';
                row.innerHTML = `
                <span class="wrong-item-jp"><strong>${item.jp}</strong> (${item.l})</span>
                <span class="wrong-item-vi">${item.vi}</span>
            `;
                wrongList.appendChild(row);
            });
        }
    } else {
        if (wrongCont) wrongCont.style.display = 'none';
        if (btnReviewWrong) btnReviewWrong.style.display = 'none';
    }
}

function startQuizWithWrongItems() {
    if (quizSession.wrongItems.length === 0) return;
    const seen = new Set();
    const uniqueWrong = [];
    for (let it of quizSession.wrongItems) {
        if (!seen.has(it.jp)) {
            seen.add(it.jp);
            uniqueWrong.push(it);
        }
    }
    startNewQuizTest(uniqueWrong);
    showToast(`🎯 Đang ôn lại ${uniqueWrong.length} từ đã làm sai!`);
}

// ==========================================
// KEYBOARD SHORTCUTS (Quizlet Standard)
// ==========================================
window.addEventListener('keydown', (e) => {
    // Không nhận phím tắt nếu người dùng đang nhập vào input/select
    if (['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

    const isFlashcard = document.getElementById('view-flashcard')?.classList.contains('active');
    const isQuiz = document.getElementById('view-quiz')?.classList.contains('active');

    if (isFlashcard) {
        if (e.code === 'Space') {
            e.preventDefault();
            flipCard();
        } else if (e.code === 'ArrowLeft') {
            e.preventDefault();
            prevCard();
        } else if (e.code === 'ArrowRight') {
            e.preventDefault();
            nextCard();
        } else if (e.key === 's' || e.key === 'S') {
            shuffleCards();
        } else if (e.key === 'r' || e.key === 'R') {
            speakCurrent();
        }
    } else if (isQuiz) {
        // Keys 1, 2, 3, 4
        if (['1', '2', '3', '4'].includes(e.key)) {
            const idx = parseInt(e.key, 10) - 1;
            const btn = document.getElementById(`quiz-opt-${idx}`);
            if (btn && !btn.disabled) {
                btn.click();
            }
        } else if (e.code === 'Space' || e.code === 'Enter') {
            const nextBtn = document.getElementById('nextQuizBtn');
            const banner = document.getElementById('quizFeedbackBanner');
            if (banner && banner.style.display === 'flex' && nextBtn) {
                e.preventDefault();
                onNextQuizClick();
            }
        }
    }
});

// Clean Japanese term for Quizlet typing (removes spaces, tildes, brackets, placeholders)
function cleanJpTermForQuizlet(str) {
    if (!str) return "";
    let s = str;
    if (s === "まいつき、まいげつ") return "まいつき";
    if (s === "まいとし、まいねん") return "まいとし";
    s = s.replace(/[~～…\.]/g, "");
    s = s.replace(/めの[nN]/g, "め");
    s = s.replace(/^[nN]が/g, "");
    s = s.replace(/^[nNpPvV][をにへとがで]/g, "");
    s = s.replace(/^[pPnN]に/g, "");
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
    s = s.replace(/[。、,，\?？!！]/g, "");
    s = s.replace(/[\s　]+/g, "");
    return s.trim();
}

// Copy format for Quizlet (Support both clean Kana and clean Kanji)
function copyQuizletFormat(mode = 'kana') {
    if (currentFiltered.length === 0) {
        showToast("Không có từ nào để copy!");
        return;
    }

    const text = currentFiltered.map(item => {
        const cleanKana = cleanJpTermForQuizlet(item.kana);
        const cleanKanji = cleanJpTermForQuizlet(item.kanji);
        const hv = item.hv ? ` ${item.hv}` : '';

        if (mode === 'kanji') {
            const term = cleanKanji || cleanKana;
            const readingNote = cleanKana && cleanKana !== term ? ` [${cleanKana}]` : '';
            return `${term}\t${item.vi}${readingNote}${hv}`;
        } else {
            const term = cleanKana || cleanKanji;
            const kanjiNote = cleanKanji && cleanKanji !== term ? ` 【${cleanKanji}】` : '';
            return `${term}\t${item.vi}${kanjiNote}${hv}`;
        }
    }).join('\n');

    const modeLabel = mode === 'kanji' ? 'Kanji chuẩn' : 'Kana gõ siêu mượt';
    const successMsg = `✅ Đã copy ${currentFiltered.length} từ format Quizlet (${modeLabel}, không dấu cách, không ~)!`;

    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            showToast(successMsg);
        }).catch(() => {
            fallbackCopyQuizletText(text, successMsg);
        });
    } else {
        fallbackCopyQuizletText(text, successMsg);
    }
}

function fallbackCopyQuizletText(text, msg) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast(msg);
}

function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => { toast.style.display = 'none'; }, 2500);
}

function restoreTvCheckpoint() {
    try {
        const raw = localStorage.getItem(TV_CP_KEY);
        if (!raw) return false;
        const saved = JSON.parse(raw);
        if (!saved || typeof saved !== 'object') return false;
        isRestoringTv = true;

        if (Array.isArray(saved.selectedLessons)) {
            selectedLessons = new Set(saved.selectedLessons);
        }
        if (saved.currentLevelScope) currentLevelScope = saved.currentLevelScope;
        if (typeof saved.isMultiSelectMode === 'boolean') {
            isMultiSelectMode = saved.isMultiSelectMode;
            const msChk = document.getElementById('chkMultiSelect');
            if (msChk) msChk.checked = isMultiSelectMode;
        }
        if (saved.cardSidePrompt === 'vi' || saved.cardSidePrompt === 'jp') {
            cardSidePrompt = saved.cardSidePrompt;
            const label = document.getElementById('lblToggleSide');
            if (label) {
                label.textContent = cardSidePrompt === 'jp' ? "Mặt trước: Tiếng Nhật" : "Mặt trước: Tiếng Việt";
            }
        }
        if (saved.quizSettings && typeof saved.quizSettings === 'object') {
            quizSettings = { ...quizSettings, ...saved.quizSettings };
            const selAnswer = document.getElementById('qsettingAnswerWith');
            const selCount = document.getElementById('qsettingCount');
            const selMode = document.getElementById('qsettingMode');
            const chkSpeak = document.getElementById('qsettingAutoSpeak');
            if (selAnswer) selAnswer.value = quizSettings.answerWith;
            if (selCount) selCount.value = String(quizSettings.count);
            if (selMode) selMode.value = quizSettings.mode;
            if (chkSpeak) chkSpeak.checked = Boolean(quizSettings.autoSpeak);
        }
        const searchEl = document.getElementById('searchInput');
        if (searchEl && typeof saved.searchQuery === 'string') {
            searchEl.value = saved.searchQuery;
        }

        initLessonChips();
        applyFilter({ isRestore: true, skipSave: true });

        if (Array.isArray(saved.cardOrder) && saved.cardOrder.length > 0 && currentFiltered.length > 0) {
            const pool = [...currentFiltered];
            const ordered = [];
            saved.cardOrder.forEach(k => {
                const idx = pool.findIndex(x => `${x.l}|${x.kanji}|${x.kana}` === k);
                if (idx !== -1) ordered.push(pool.splice(idx, 1)[0]);
            });
            currentFiltered = ordered.concat(pool);
        }
        if (Number.isInteger(saved.currentCardIndex) && currentFiltered.length > 0) {
            currentCardIndex = Math.max(0, Math.min(saved.currentCardIndex, currentFiltered.length - 1));
        }
        cardFlipped = Boolean(saved.cardFlipped);

        if (saved.quizSession && Array.isArray(saved.quizSession.questions) && saved.quizSession.questions.length > 0) {
            quizSession = saved.quizSession;
        }

        const targetView = saved.currentView || 'view-table';
        switchView(targetView, { isRestore: true, skipSave: true });

        if (targetView === 'view-quiz' && quizSession.questions && quizSession.questions.length > 0) {
            const activeBox = document.getElementById('quizActiveBox');
            const resView = document.getElementById('quizResultView');
            if (quizSession.currentIndex >= quizSession.questions.length) {
                showQuizResults();
            } else {
                if (activeBox) activeBox.style.display = 'block';
                if (resView) resView.style.display = 'none';
                renderQuizQuestion({ preserveAnswered: true });
                if (quizSession.answered) {
                    const q = quizSession.questions[quizSession.currentIndex];
                    const allBtns = document.querySelectorAll('#quizOptions .quiz-opt-btn');
                    allBtns.forEach(b => {
                        b.disabled = true;
                        const text = b.querySelector('.opt-text')?.innerText;
                        if (text === q.correctAnswer) b.classList.add('correct');
                        else if (text === quizSession.lastSelectedOpt) b.classList.add('wrong');
                    });
                    if (quizSettings.mode === 'instant') {
                        const isCorrect = quizSession.lastSelectedOpt === q.correctAnswer;
                        const banner = document.getElementById('quizFeedbackBanner');
                        const feedbackText = document.getElementById('quizFeedbackText');
                        if (banner && feedbackText) {
                            banner.className = isCorrect ? 'quiz-feedback-banner feedback-correct' : 'quiz-feedback-banner feedback-wrong';
                            feedbackText.innerHTML = isCorrect
                                ? `✓ Chính xác! Rất tốt.`
                                : `✕ Chưa đúng! Đáp án đúng: <strong>${q.correctAnswer}</strong> (${q.rawItem.jp} : ${q.rawItem.vi})`;
                            banner.style.display = 'flex';
                        }
                    }
                }
            }
        }

        isRestoringTv = false;
        return true;
    } catch (e) {
        isRestoringTv = false;
        return false;
    }
}

// Initial render
window.addEventListener('DOMContentLoaded', () => {
    if (!restoreTvCheckpoint()) {
        initLessonChips();
        applyFilter({ skipSave: true });
    }
});
