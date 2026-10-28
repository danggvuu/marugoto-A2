import re

def update_kanji_layout():
    with open('kanji_a2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS for hero header, mode tabs, toolbar, drawer, tips
    new_css_block = '''
        /* Page Hero Banner */
        .page-hero-banner {
            background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #0284c7 100%);
            color: white;
            padding: 22px 24px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(37, 99, 235, 0.22);
            margin-bottom: 18px;
        }

        .page-hero-banner h1 {
            font-size: 1.75rem;
            font-weight: 800;
            margin-bottom: 6px;
            letter-spacing: -0.5px;
        }

        .page-hero-banner p {
            font-size: 0.95rem;
            opacity: 0.93;
            max-width: 820px;
            margin: 0 auto;
        }

        /* Mode Switcher Segmented Tabs */
        .mode-tabs {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 18px;
            flex-wrap: wrap;
        }

        .mode-tab-btn {
            background: white;
            border: 1.5px solid #e2e8f0;
            padding: 9px 20px;
            border-radius: 30px;
            font-size: 0.92rem;
            font-weight: 700;
            cursor: pointer;
            color: #334155;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            display: inline-flex;
            align-items: center;
            gap: 7px;
        }

        .mode-tab-btn:hover {
            border-color: #93c5fd;
            color: #2563eb;
            transform: translateY(-1px);
        }

        .mode-tab-btn.active {
            background: #2563eb;
            color: white;
            border-color: #2563eb;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
        }

        .tab-panel {
            display: none;
            animation: fadeIn 0.25s ease;
        }

        .tab-panel.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* High-Efficiency Controls & Filter Card */
        .controls-card {
            background: white;
            border-radius: 16px;
            box-shadow: 0 4px 18px rgba(0,0,0,0.04);
            border: 1px solid #e2e8f0;
            padding: 14px 18px;
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        /* Primary Toolbar Row (Search + Presets + Actions) */
        .toolbar-primary-row {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .search-input-wrap {
            position: relative;
            flex: 1 1 260px;
            min-width: 220px;
        }

        .search-input-wrap input {
            width: 100%;
            padding: 10px 34px 10px 14px;
            border: 1.5px solid #cbd5e1;
            border-radius: 12px;
            font-size: 0.92rem;
            outline: none;
            transition: all 0.2s;
            background: #f8fafc;
        }
        .search-input-wrap input:focus {
            border-color: #2563eb;
            background: white;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
        }

        .search-clear-btn {
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: #94a3b8;
            font-size: 1rem;
            cursor: pointer;
            padding: 2px 6px;
            display: none;
        }

        .quick-presets-group {
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }

        .preset-pill {
            background: #f8fafc;
            border: 1.5px solid #e2e8f0;
            color: #475569;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
        }

        .preset-pill:hover {
            border-color: #93c5fd;
            color: #2563eb;
            background: #eff6ff;
            transform: translateY(-1px);
        }

        .preset-pill.active {
            background: #2563eb;
            border-color: #2563eb;
            color: white;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
        }

        .preset-clear {
            color: #ef4444;
            border-color: #fecaca;
        }
        .preset-clear:hover {
            background: #fef2f2;
            border-color: #ef4444;
            color: #dc2626;
        }

        .toolbar-actions {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-left: auto;
        }

        .btn-drawer-toggle {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #f1f5f9;
            border: 1.5px solid #cbd5e1;
            color: #334155;
            padding: 7px 14px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
        }
        .btn-drawer-toggle:hover {
            background: #e2e8f0;
            border-color: #94a3b8;
        }
        .btn-drawer-toggle.active {
            background: #e0f2fe;
            border-color: #38bdf8;
            color: #0284c7;
        }

        .badge-counter {
            background: #2563eb;
            color: white;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 1px 7px;
            border-radius: 10px;
        }
        .btn-drawer-toggle.active .badge-counter {
            background: #0284c7;
        }

        .btn-print {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: white;
            border: 1.5px solid #cbd5e1;
            color: #475569;
            padding: 7px 13px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
        }
        .btn-print:hover {
            border-color: #2563eb;
            color: #2563eb;
            background: #eff6ff;
        }

        /* Collapsible Lesson Filter Drawer */
        .lesson-filter-drawer {
            display: none;
            flex-direction: column;
            gap: 12px;
            padding-top: 12px;
            border-top: 1px dashed #e2e8f0;
            animation: drawerSlide 0.22s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .lesson-filter-drawer.open {
            display: flex;
        }

        @keyframes drawerSlide {
            from { opacity: 0; transform: translateY(-6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .range-selector-strip {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            flex-wrap: wrap;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 8px 12px;
            font-size: 0.85rem;
        }

        .range-inputs-group {
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }

        .range-label {
            font-weight: 700;
            color: #1e293b;
        }

        .range-dropdown {
            padding: 5px 8px;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            background: white;
            color: #1e293b;
            outline: none;
            max-width: 220px;
        }
        .range-dropdown:focus {
            border-color: #2563eb;
        }

        .btn-range-apply {
            background: #2563eb;
            color: white;
            border: none;
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s;
        }
        .btn-range-apply:hover {
            background: #1d4ed8;
        }

        .range-tip {
            font-size: 0.76rem;
            color: #64748b;
        }

        .chips-rack {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .chips-rack-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
        }

        .chips-title {
            font-size: 0.82rem;
            font-weight: 700;
            color: #475569;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .selection-badge {
            background: #eff6ff;
            color: #2563eb;
            border: 1px solid #bfdbfe;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 2px 10px;
            border-radius: 12px;
        }

        .chips-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .lesson-chip {
            background: white;
            border: 1.5px solid #e2e8f0;
            padding: 5px 10px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            color: #334155;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.15s ease;
            user-select: none;
        }
        .lesson-chip:hover {
            border-color: #93c5fd;
            background: #f8fafc;
            transform: translateY(-1px);
        }
        .lesson-chip.active {
            background: #2563eb;
            border-color: #2563eb;
            color: white;
            box-shadow: 0 2px 6px rgba(37, 99, 235, 0.25);
        }
        .lesson-chip.active .chip-count {
            background: rgba(255, 255, 255, 0.25);
            color: white;
        }
        .chip-check {
            font-size: 0.75rem;
            font-weight: bold;
        }
        .chip-count {
            font-size: 0.72rem;
            opacity: 0.9;
            background: rgba(0,0,0,0.06);
            padding: 0 5px;
            border-radius: 6px;
        }

        /* Writing Tip Pill Banner */
        .writing-tip-pill {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1e40af;
            padding: 8px 14px;
            border-radius: 10px;
            font-size: 0.86rem;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }
        .tip-close-btn {
            background: none;
            border: none;
            color: #60a5fa;
            font-size: 0.95rem;
            cursor: pointer;
            padding: 2px 6px;
            border-radius: 4px;
            line-height: 1;
        }
        .tip-close-btn:hover {
            color: #1e40af;
            background: rgba(255,255,255,0.6);
        }
    '''

    # Replace old CSS around lines 65-144
    css_target = re.search(r'/\* Header \*/.*?/\* Multi-Lesson Selection & Filter Component \*/.*?\.controls-card\s*\{[^}]*\}', content, re.DOTALL)
    if css_target:
        content = content[:css_target.start()] + new_css_block + content[css_target.end():]
        print("Replaced CSS header and controls-card successfully")
    else:
        print("Warning: CSS target 1 not matched")

    # 2. Update the HTML structure between container open and cards container
    html_target_pattern = r'<div class="container">.*?<!-- TAB 1: KANJI CARDS & INTERACTIVE WRITING -->\s*<div id="tab-cards" class="tab-panel active">.*?<div class="cards-list" id="cardsContainer"></div>'
    
    new_html_block = '''<div class="container">
    <!-- Global Hub Navigation (Compact & Organized) -->
    <div class="global-hub-nav">
        <a href="index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="kanji_a2.html" class="hub-nav-item active-hub">⛩️ Học Kanji & Nét Viết</a>
        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
        <a href="demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                <a href="tests/On_Tap_Mini_Test_A2_1_4.html" class="hub-drop-link">🎯 Ôn Tập Bài 1-4 (Mini Test)</a>
                <a href="tests/On_Tap_Mini_Test_A2_5_8.html" class="hub-drop-link">🎯 Ôn Tập Bài 5-8 (Mini Test)</a>
                <a href="tests/De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-drop-link">📝 5 Mã Đề Thi Thử (101-105)</a>
                <a href="tests/Kiem_Tra_Marugoto_L6_7_8.html" class="hub-drop-link">📑 Đề Kiểm Tra L6, 7, 8</a>
                <a href="tests/Luyen_Tap_The_Te_A2_1.html" class="hub-drop-link">🌸 Luyện Tập Thể Te</a>
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học 10-18 ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                <a href="lessons/Marugoto_A2_Lesson_10.html" class="hub-drop-link">🌟 Bài 10: 外国文化</a>
                <a href="lessons/Marugoto_A2_Lesson_11.html" class="hub-drop-link">🍱 Bài 11: そとで食べる</a>
                <a href="lessons/Marugoto_A2_Lesson_12.html" class="hub-drop-link">🍜 Bài 12: 特別な日の料理</a>
                <a href="lessons/Marugoto_A2_Lesson_13.html" class="hub-drop-link">✈️ Bài 13: 出張</a>
                <a href="lessons/Marugoto_A2_Lesson_14.html" class="hub-drop-link">💻 Bài 14: 職場のマナー</a>
                <a href="lessons/Marugoto_A2_Lesson_15.html" class="hub-drop-link">🏥 Bài 15: 健康な生活</a>
                <a href="lessons/Marugoto_A2_Lesson_16.html" class="hub-drop-link">🏃 Bài 16: 体にいいこと</a>
                <a href="lessons/Marugoto_A2_Lesson_17.html" class="hub-drop-link">🎁 Bài 17: お祝い</a>
                <a href="lessons/Marugoto_A2_Lesson_18.html" class="hub-drop-link">👘 Bài 18: お祭りやイベント</a>
            </div>
        </div>
    </div>

    <!-- Header Hero Banner -->
    <header class="page-hero-banner">
        <h1>⛩️ THẺ HỌC, TẬP VIẾT & BÀI TẬP KANJI MARUGOTO A2-1</h1>
        <p>144 chữ Hán chuẩn giáo trình Minato Bài 1-18 • Nét bút hoạt họa SVG • Bảng tập vẽ trực tiếp • Trắc nghiệm phản xạ</p>
    </header>

    <!-- Mode Tabs (Segmented Control) -->
    <div class="mode-tabs">
        <button class="mode-tab-btn active" onclick="switchTab('tab-cards')">🎴 Thẻ Học & Luyện Viết (<span id="tabCountCards">144</span>)</button>
        <button class="mode-tab-btn" onclick="switchTab('tab-exercises')">✍️ Bài Tập Từ Vựng Kanji</button>
        <button class="mode-tab-btn" onclick="switchTab('tab-rules')">📏 8 Quy Tắc Bút Thuận</button>
    </div>

    <!-- High-Efficiency Compact Toolbar & Filter Card -->
    <div class="controls-card">
        <!-- Row 1: Search, Quick Presets & Actions -->
        <div class="toolbar-primary-row">
            <div class="search-input-wrap">
                <input type="text" id="searchInput" placeholder="🔍 Tìm chữ Hán, Hán Việt (Thu, Đông...), Kun, On, nghĩa..." oninput="onSearchChange()">
                <button class="search-clear-btn" id="searchClearBtn" onclick="clearSearch()" title="Xóa tìm kiếm">✕</button>
            </div>

            <div class="quick-presets-group">
                <button class="preset-pill active" id="preset-all" onclick="selectPreset('ALL')" title="Xem toàn bộ 18 bài">🌟 Tất cả (1-18)</button>
                <button class="preset-pill" id="preset-l1-5" onclick="selectPreset('L1_5')">Bài 1-5</button>
                <button class="preset-pill" id="preset-l6-10" onclick="selectPreset('L6_10')">Bài 6-10</button>
                <button class="preset-pill" id="preset-l11-18" onclick="selectPreset('L11_18')">Bài 11-18 ✨</button>
                <button class="preset-pill preset-clear" id="preset-none" onclick="selectPreset('NONE')">Bỏ chọn</button>
            </div>

            <div class="toolbar-actions">
                <button type="button" class="btn-drawer-toggle" id="btnToggleDrawer" onclick="toggleLessonFilterDrawer()" title="Mở rộng để chọn từng bài lẻ hoặc chọn dải liên tục">
                    <span>⚙️ Lọc 18 bài</span>
                    <span class="badge-counter" id="activeFilterBadge">18 bài</span>
                    <span id="drawerArrow">▾</span>
                </button>
                <button type="button" class="btn-print" onclick="window.print()" title="In thẻ học Kanji dạng Flashcard">🖨️ In Thẻ</button>
            </div>
        </div>

        <!-- Row 2: Collapsible Filter Drawer -->
        <div class="lesson-filter-drawer" id="lessonFilterDrawer">
            <div class="range-selector-strip">
                <div class="range-inputs-group">
                    <span class="range-label">🎯 Chọn dải bài liên tục:</span>
                    <span>Từ</span>
                    <select class="range-dropdown" id="rangeStartBar"></select>
                    <span>đến</span>
                    <select class="range-dropdown" id="rangeEndBar"></select>
                    <button class="btn-range-apply" onclick="applyRangeSelection(true)">Áp dụng</button>
                </div>
                <span class="range-tip">💡 Mẹo: Giữ <strong>Shift + Click</strong> vào 2 bài bất kỳ để chọn dải liên tục!</span>
            </div>

            <div class="chips-rack">
                <div class="chips-rack-header">
                    <span class="chips-title">Chọn từng bài riêng lẻ:</span>
                    <span class="selection-badge" id="selectionSummary">Đang chọn: Tất cả 18 bài (144 chữ Hán)</span>
                </div>
                <div class="chips-grid" id="chipsContainerKanji"></div>
            </div>
        </div>
    </div>

    <!-- TAB 1: KANJI CARDS & INTERACTIVE WRITING -->
    <div id="tab-cards" class="tab-panel active">
        <div class="writing-tip-pill" id="writingTipPill">
            <span>💡 <strong>Mẹo luyện viết:</strong> Dùng chuột hoặc ngón tay vẽ trực tiếp vào ô chữ Hán bên phải thẻ để luyện nhớ nét! Bấm nút <em>"Làm mờ mẫu"</em> để tự viết.</span>
            <button class="tip-close-btn" onclick="document.getElementById('writingTipPill').style.display='none'" title="Đóng mẹo">✕</button>
        </div>
        <div class="cards-list" id="cardsContainer"></div>'''

    html_match = re.search(html_target_pattern, content, re.DOTALL)
    if html_match:
        content = content[:html_match.start()] + new_html_block + content[html_match.end():]
        print("Replaced HTML header, tabs, toolbar, drawer, cards container successfully")
    else:
        print("Warning: HTML target pattern not matched")

    # 3. Add JS functions for drawer and dropdowns
    new_js_block = '''
    function toggleLessonFilterDrawer() {
        const drawer = document.getElementById('lessonFilterDrawer');
        const arrow = document.getElementById('drawerArrow');
        const btn = document.getElementById('btnToggleDrawer');
        if (!drawer) return;
        const isOpen = drawer.classList.toggle('open');
        if (arrow) arrow.textContent = isOpen ? '▴' : '▾';
        if (btn) btn.classList.toggle('active', isOpen);
    }

    function toggleTestsDropdown(e) {
        if (e) e.stopPropagation();
        const m = document.getElementById('testsDropdownMenu');
        if (m) m.classList.toggle('show');
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
    }

    function toggleLessonsDropdown(e) {
        if (e) e.stopPropagation();
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) m.classList.toggle('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    }

    window.addEventListener('click', () => {
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    });
'''
    # Replace existing toggleLessonsDropdown
    content = re.sub(r'function toggleLessonsDropdown\(e\)\s*\{.*?window\.addEventListener\(\'click\',\s*\(\)\s*=>\s*\{.*?\}\);', new_js_block.strip(), content, flags=re.DOTALL)

    # 4. Update applyLessonFilter to update tabCountCards and activeFilterBadge
    old_apply_summary = "const summary = document.getElementById('selectionSummary');"
    new_apply_summary = """const summary = document.getElementById('selectionSummary');
        const tabCount = document.getElementById('tabCountCards');
        if (tabCount) tabCount.textContent = filteredKanji.length;
        const filterBadge = document.getElementById('activeFilterBadge');
        if (filterBadge) {
            filterBadge.textContent = selectedLessons.size === KANJI_LESSON_ORDER.length ? '18 bài' : `${selectedLessons.size} bài`;
        }"""
    content = content.replace(old_apply_summary, new_apply_summary, 1)

    with open('kanji_a2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("All updates written to kanji_a2.html")

if __name__ == '__main__':
    update_kanji_layout()
