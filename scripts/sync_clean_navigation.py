# -*- coding: utf-8 -*-
"""
sync_clean_navigation.py
Restores clean, non-sticky, non-overlapping global hub navigation across all pages.
Eliminates the bloated sticky dock that was cutting off pills and covering content.
"""

import re
import os

PAGES = [
    ("index.html", "te"),
    ("the_ru.html", "ru"),
    ("kanji_a2.html", "kanji"),
    ("Tu_Vung_Marugoto_A1_16_A2_1_10.html", "vocab"),
    ("Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html", "grammar"),
    ("On_Tap_Mini_Test_A2_1_4.html", "ontap14"),
    ("On_Tap_Mini_Test_A2_5_8.html", "ontap58"),
    ("De_Thi_Thu_Marugoto_A2_5_8.html", "dethi"),
    ("Marugoto_A2_Lesson_10.html", "l10"),
    ("Marugoto_A2_Lesson_11.html", "l11"),
    ("Marugoto_A2_Lesson_12.html", "l12"),
    ("Marugoto_A2_Lesson_13.html", "l13"),
    ("Marugoto_A2_Lesson_14.html", "l14"),
    ("Marugoto_A2_Lesson_15.html", "l15"),
    ("Marugoto_A2_Lesson_16.html", "l16"),
    ("Marugoto_A2_Lesson_17.html", "l17"),
    ("Marugoto_A2_Lesson_18.html", "l18"),
]

HUB_NAV_CSS = """
        /* ==========================================
           GLOBAL HUB NAVIGATION (CLEAN & NON-STICKY)
           ========================================== */
        .global-hub-nav {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 10px 0 24px 0;
            flex-wrap: wrap;
        }
        .hub-nav-item {
            text-decoration: none;
            background: #ffffff;
            color: #475569;
            padding: 9px 18px;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 700;
            border: 1.5px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            font-family: inherit;
        }
        .hub-nav-item:hover {
            border-color: #4f46e5;
            color: #4f46e5;
            transform: translateY(-2px);
        }
        .hub-nav-item.active-hub {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff !important;
            border-color: transparent;
            box-shadow: 0 4px 15px rgba(79, 70, 229, 0.35);
        }
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
            border: 1.5px solid #e2e8f0;
            border-radius: 14px;
            box-shadow: 0 12px 28px rgba(0,0,0,0.12);
            padding: 8px;
            min-width: 260px;
            z-index: 9999;
        }
        .hub-dropdown-menu.show {
            display: block;
        }
        .hub-drop-link {
            display: block;
            padding: 8px 14px;
            color: #334155;
            font-size: 0.88rem;
            font-weight: 700;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.15s ease;
        }
        .hub-drop-link:hover {
            background: #eef2ff;
            color: #4f46e5;
        }
        .hub-drop-link.active {
            background: #4f46e5;
            color: #ffffff !important;
        }
        @media (max-width: 768px) {
            .global-hub-nav {
                display: flex;
                flex-wrap: nowrap;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                justify-content: flex-start;
                gap: 8px;
                margin-bottom: 15px;
                padding: 2px 2px 8px 2px;
                scrollbar-width: none;
            }
            .global-hub-nav::-webkit-scrollbar {
                display: none;
            }
            .hub-nav-item {
                flex-shrink: 0;
                padding: 7px 14px;
                font-size: 0.84rem;
            }
        }
"""

HUB_NAV_JS = """
    function toggleLessonsDropdown(e) {
        if (e) e.stopPropagation();
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) m.classList.toggle('show');
    }
    window.addEventListener('click', () => {
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) m.classList.remove('show');
    });
"""

def generate_hub_markup(active_page):
    c_te = " active-hub" if active_page == "te" else ""
    c_ru = " active-hub" if active_page == "ru" else ""
    c_kanji = " active-hub" if active_page == "kanji" else ""
    c_vocab = " active-hub" if active_page == "vocab" else ""
    c_grammar = " active-hub" if active_page == "grammar" else ""
    c_ontap14 = " active-hub" if active_page == "ontap14" else ""
    c_ontap58 = " active-hub" if active_page == "ontap58" else ""
    c_dethi = " active-hub" if active_page == "dethi" else ""
    
    is_lesson = active_page.startswith("l")
    c_lesson_btn = " active-hub" if is_lesson else ""

    lesson_links = []
    for num, name, icon in [
        (10, "外国文化", "🌟"),
        (11, "そとで食べる", "🍱"),
        (12, "特別な日の料理", "🍜"),
        (13, "出張", "✈️"),
        (14, "職場のマナー", "💻"),
        (15, "健康な生活", "🏥"),
        (16, "体にいいこと", "🏃"),
        (17, "お祝い", "🎁"),
        (18, "お祭りやイベント", "👘")
    ]:
        act = " active" if active_page == f"l{num}" else ""
        lesson_links.append(f'                <a href="Marugoto_A2_Lesson_{num}.html" class="hub-drop-link{act}">{icon} Bài {num}: {name}</a>')

    lessons_html = "\n".join(lesson_links)

    markup = f"""    <!-- Global Hub Navigation -->
    <div class="global-hub-nav">
        <a href="index.html" class="hub-nav-item{c_te}">🌸 Thể TE (～て)</a>
        <a href="the_ru.html" class="hub-nav-item{c_ru}">📘 Thể RU (Từ Điển)</a>
        <a href="kanji_a2.html" class="hub-nav-item{c_kanji}">⛩️ Học Kanji & Nét Viết</a>
        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item{c_vocab}">📖 Kho Từ Vựng A1-A2</a>
        <a href="Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item{c_grammar}">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
        <a href="On_Tap_Mini_Test_A2_1_4.html" class="hub-nav-item{c_ontap14}">🎯 Ôn Tập Bài 1-4</a>
        <a href="On_Tap_Mini_Test_A2_5_8.html" class="hub-nav-item{c_ontap58}">🎯 Ôn Tập Bài 5-8</a>
        <a href="De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-nav-item{c_dethi}">📝 5 Mã Đề Thi Thử</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item{c_lesson_btn}" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học 10-18 ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
{lessons_html}
            </div>
        </div>
    </div>"""
    return markup

def clean_and_update_page(filename, active_page):
    if not os.path.exists(filename):
        print(f"Skipping {filename}: not found")
        return

    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Remove dock CSS block
    dock_css_pattern = r'/\* ===================================================\s*GLOBAL STICKY DOCK & QUICK DRAWER[\s\S]*?(?=\n</style>)'
    html = re.sub(dock_css_pattern, '', html)
    html = html.replace('\\n</style>', '</style>')

    # 2. Cleanly strip all old hub nav CSS and insert single canonical HUB_NAV_CSS
    html = re.sub(r'/\*\s*=+[\s\S]*?GLOBAL HUB NAVIGATION[\s\S]*?(?=\n\s*/\*\s*[A-Z]|\n\s*</style>)', '', html)
    html = re.sub(r'/\*\s*Hub Dropdown Menu\s*\*[\s\S]*?(?=\n\s*/\*\s*[A-Z]|\n\s*</style>)', '', html)
    html = re.sub(r'\.global-hub-nav\s*\{[\s\S]*?\.hub-drop-link\.active\s*\{[^}]*\}', '', html)
    html = re.sub(r'\.global-hub-nav\s*\{[\s\S]*?font-size:\s*0\.84rem;\s*\}\s*\}', '', html)
    html = html.replace('</style>', HUB_NAV_CSS + '\n    </style>', 1)

    # 3. Remove dock markup (global-sticky-dock-wrapper and global-mega-sheet)
    # Case A: Dock wrapper before hero or container
    html = re.sub(r'<div class="global-sticky-dock-wrapper"[\s\S]*?</div>\s*</div>\s*</div>', '', html)
    html = re.sub(r'<div class="global-mega-sheet"[\s\S]*?</div>\s*</div>\s*</div>', '', html)
    html = re.sub(r'<!-- MEGA DRAWER SHEET -->[\s\S]*?</div>\s*</div>\s*</div>', '', html)
    html = re.sub(r'<!-- GLOBAL STICKY FLOATING DOCK \(OPTION 1\) -->[\s\S]*?</div>\s*</div>\s*</div>', '', html)

    # 4. Remove any existing global-hub-nav
    html = re.sub(r'<!-- Global Hub Navigation -->\s*<div class="global-hub-nav">[\s\S]*?</div>\s*</div>\s*</div>', '', html)
    html = re.sub(r'<!-- Global Hub Navigation -->\s*<div class="global-hub-nav">[\s\S]*?</div>', '', html)

    # 5. Insert new clean hub nav
    new_nav = generate_hub_markup(active_page)

    # If page has <div class="container">, insert right after
    if '<div class="container">' in html:
        html = html.replace('<div class="container">', '<div class="container">\n' + new_nav, 1)
    elif '<header' in html:
        html = html.replace('<header', new_nav + '\n    <header', 1)
    elif '<main' in html:
        html = html.replace('<main', new_nav + '\n    <main', 1)
    elif '<body>' in html:
        html = html.replace('<body>', '<body>\n' + new_nav, 1)

    # 6. Ensure HUB_NAV_JS is present
    if 'function toggleLessonsDropdown' not in html:
        if '</script>' in html:
            # Insert before last </script>
            pos = html.rfind('</script>')
            html = html[:pos] + HUB_NAV_JS + '\n' + html[pos:]
        else:
            html = html.replace('</body>', f'<script>{HUB_NAV_JS}</script>\n</body>')

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Cleaned and updated {filename} successfully!")

def main():
    for fn, page_key in PAGES:
        clean_and_update_page(fn, page_key)

if __name__ == "__main__":
    main()
