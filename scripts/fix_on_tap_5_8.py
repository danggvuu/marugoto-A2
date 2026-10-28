# -*- coding: utf-8 -*-
"""
fix_on_tap_5_8.py
Restores On_Tap_Mini_Test_A2_5_8.html to its clean, authentic, intended design.
"""

import re

def fix_page():
    path = "On_Tap_Mini_Test_A2_5_8.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Remove the dock CSS block (between /* === GLOBAL STICKY DOCK ... and </style>)
    dock_css_pattern = r'/\* ===================================================\s*GLOBAL STICKY DOCK & QUICK DRAWER \(OPTION 1\)[\s\S]*?(?=\n</style>)'
    html = re.sub(dock_css_pattern, '', html)
    html = html.replace('\\n</style>', '</style>')

    # 2. Add hub dropdown CSS if not present
    if '.hub-dropdown' not in html:
        hub_dropdown_css = """
        /* Hub Dropdown Menu */
        .hub-dropdown {
            position: relative;
            display: inline-block;
        }
        .hub-dropdown-menu {
            display: none;
            position: absolute;
            top: calc(100% + 6px);
            left: 50%;
            transform: translateX(-50%);
            background: #ffffff;
            border: 1.5px solid var(--gray-200);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-lg);
            padding: 8px;
            min-width: 260px;
            z-index: 1000;
        }
        .hub-dropdown-menu.show {
            display: block;
        }
        .hub-drop-link {
            display: block;
            padding: 8px 14px;
            color: var(--gray-700);
            font-size: 0.88rem;
            font-weight: 700;
            text-decoration: none;
            border-radius: var(--radius-sm);
            transition: all 0.15s ease;
        }
        .hub-drop-link:hover {
            background: var(--primary-light);
            color: var(--primary);
        }
        """
        html = html.replace('/* Hero Header */', hub_dropdown_css + '\n        /* Hero Header */')

    # 3. Replace the dock markup with clean global-hub-nav
    clean_hub_nav = """    <!-- Global Hub Navigation -->
    <div class="global-hub-nav">
        <a href="index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
        <a href="On_Tap_Mini_Test_A2_1_4.html" class="hub-nav-item">🎯 Ôn Tập Bài 1-4</a>
        <a href="On_Tap_Mini_Test_A2_5_8.html" class="hub-nav-item active-hub">🎯 Ôn Tập Bài 5-8</a>
        <a href="De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-nav-item">📝 5 Mã Đề Thi Thử</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học 10-18 ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                <a href="Marugoto_A2_Lesson_10.html" class="hub-drop-link">🌟 Bài 10: 外国文化</a>
                <a href="Marugoto_A2_Lesson_11.html" class="hub-drop-link">🍱 Bài 11: そとで食べる</a>
                <a href="Marugoto_A2_Lesson_12.html" class="hub-drop-link">🍜 Bài 12: 特別な日の料理</a>
                <a href="Marugoto_A2_Lesson_13.html" class="hub-drop-link">✈️ Bài 13: 出張</a>
                <a href="Marugoto_A2_Lesson_14.html" class="hub-drop-link">💻 Bài 14: 職場のマナー</a>
                <a href="Marugoto_A2_Lesson_15.html" class="hub-drop-link">🏥 Bài 15: 健康な生活</a>
                <a href="Marugoto_A2_Lesson_16.html" class="hub-drop-link">🏃 Bài 16: 体にいいこと</a>
                <a href="Marugoto_A2_Lesson_17.html" class="hub-drop-link">🎁 Bài 17: お祝い</a>
                <a href="Marugoto_A2_Lesson_18.html" class="hub-drop-link">👘 Bài 18: お祭りやイベント</a>
            </div>
        </div>
    </div>"""

    # Dock markup removal pattern: from <!-- GLOBAL STICKY FLOATING DOCK ... to before <!-- Hero Header -->
    dock_html_pattern = r'<!-- GLOBAL STICKY FLOATING DOCK \(OPTION 1\) -->[\s\S]*?(?=\s*<!-- Hero Header -->)'
    html = re.sub(dock_html_pattern, clean_hub_nav, html)

    # 4. Fix tab-nav-wrapper sticky top
    html = html.replace('top: 56px;', 'top: 12px;')

    # 5. Fix theory-quicknav to show Bài 5-8 and review 1-4
    clean_theory_quicknav = """        <!-- Quick Jump Bar for Bài 5-8 -->
        <div class="theory-quicknav">
            <a href="#grammar-l5" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">⭐ Bài 5: わたしの町 (～くて／で)</a>
            <a href="#grammar-l6" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">⭐ Bài 6: 道案内 (～てください)</a>
            <a href="#grammar-l7" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">⭐ Bài 7: 約束 (～でもいいですか)</a>
            <a href="#grammar-l8" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">⭐ Bài 8: 週末 (～に行きます)</a>
            <a href="#grammar-l9" class="quicknav-pill">Bài 9: 外国語 (～のが好き)</a>
            <a href="#grammar-l10" class="quicknav-pill">Bài 10: 外国文化 (～たい／てみる)</a>
            <a href="#grammar-review-14" class="quicknav-pill" style="background: #e2e8f0; color: #475569;">📂 Xem Lại Bài 1 - 4</a>
        </div>"""

    quicknav_pattern = r'<!-- Quick Jump Bar for all 10 lessons -->\s*<div class="theory-quicknav">[\s\S]*?</div>'
    html = re.sub(quicknav_pattern, clean_theory_quicknav, html)

    # 6. Extract Bài 1-4 cards from top of tab-theory
    # Find block from <!-- BÀI 1 --> to before <!-- BÀI 5 -->
    b1_4_pattern = r'<!-- BÀI 1 -->[\s\S]*?(?=(\\n\\n\s*)?<!-- BÀI 5 -->)'
    m = re.search(b1_4_pattern, html)
    if m:
        b1_4_content = m.group(0).strip()
        # Remove from top
        html = html[:m.start()] + html[m.end():]
        # Clean any literal \n\n <!-- BÀI 5 -->\n
        html = re.sub(r'(\\n\\n\s*)?<!-- BÀI 5 -->(\\n)?', '<!-- BÀI 5 -->', html)

        # Place into <details id="grammar-review-14"> at the end of tab-theory
        review_details = f"""
        <!-- COLLAPSIBLE SECTION: REVIEW LESSONS 1 TO 4 -->
        <details id="grammar-review-14" style="background: white; border-radius: 16px; border: 2px dashed var(--gray-300); padding: 18px 24px; margin-top: 24px; box-shadow: var(--shadow-sm);">
            <summary style="font-weight: 800; font-size: 1.15rem; color: var(--gray-800); cursor: pointer; padding: 6px 0; user-select: none;">
                📂 Bấm Để Xem Lại Lý Thuyết Nền Tảng (Bài 1 - 4 đã thi xong)
            </summary>
            <div style="margin-top: 20px;">
                {b1_4_content}
            </div>
        </details>"""

        # Replace empty review section
        empty_review_pattern = r'<!-- COLLAPSIBLE SECTION: REVIEW LESSONS 1 TO 4 -->\s*</div>'
        html = re.sub(empty_review_pattern, review_details + '\n    </div>', html)

    # 7. Add toggleLessonsDropdown JS if not present
    if 'toggleLessonsDropdown' not in html:
        js_func = """
    function toggleLessonsDropdown(e) {
        e.stopPropagation();
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) m.classList.toggle('show');
    }
    window.addEventListener('click', () => {
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) m.classList.remove('show');
    });
    """
        html = html.replace('</script>', js_func + '\n</script>')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Fixed On_Tap_Mini_Test_A2_5_8.html successfully!")

if __name__ == "__main__":
    fix_page()
