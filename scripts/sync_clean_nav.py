#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/sync_clean_nav.py
Đồng bộ thanh navigation trên toàn bộ 31 file HTML:
- Xóa bỏ nút Ngữ Pháp: '📚 Ngữ Pháp A1-A2 (26 Bài)' (đã thay bằng menu Web Bài Học)
- Menu '🚀 Web Bài Học ▾' chứa ĐẦY ĐỦ TRỌN BỘ 18 BÀI (Bài 1 -> Bài 18)
- Đảm bảo CSS .hub-dropdown-menu có max-height: 480px và overflow-y: auto
- Đảm bảo hàm toggleLessonsDropdown & toggleTestsDropdown hoạt động hoàn hảo
"""

import os
import re
import glob

ALL_18_LESSONS = [
    (1, 'Marugoto_A2_Lesson_1.html', '🌸 Bài 1: Nơi ở & Gia đình'),
    (2, 'Marugoto_A2_Lesson_2.html', '🎨 Bài 2: Sở thích & Ngôn ngữ'),
    (3, 'Marugoto_A2_Lesson_3.html', '🍁 Bài 3: Mùa & Khí hậu'),
    (4, 'Marugoto_A2_Lesson_4.html', '⛅ Bài 4: Thời tiết & Dự báo'),
    (5, 'Marugoto_A2_Lesson_5.html', '🏙️ Bài 5: Phố xá & Nơi chốn'),
    (6, 'Marugoto_A2_Lesson_6.html', '🗺️ Bài 6: Chỉ đường & Ngã rẽ'),
    (7, 'Marugoto_A2_Lesson_7.html', '⏰ Bài 7: Hẹn gặp & Giờ giấc'),
    (8, 'Marugoto_A2_Lesson_8.html', '⛩️ Bài 8: Sự kiện & Mời mọc'),
    (9, 'Marugoto_A2_Lesson_9.html', '🗣️ Bài 9: Học tập & Phát âm'),
    (10, 'Marugoto_A2_Lesson_10.html', '🌟 Bài 10: Ngoại ngữ & Văn hóa'),
    (11, 'Marugoto_A2_Lesson_11.html', '🍱 Bài 11: Dã ngoại & Ăn uống'),
    (12, 'Marugoto_A2_Lesson_12.html', '🍜 Bài 12: Món ăn ngày đặc biệt'),
    (13, 'Marugoto_A2_Lesson_13.html', '✈️ Bài 13: Đi công tác & Gặp gỡ'),
    (14, 'Marugoto_A2_Lesson_14.html', '💻 Bài 14: Quy tắc nơi làm việc'),
    (15, 'Marugoto_A2_Lesson_15.html', '🏥 Bài 15: Sức khỏe & Thể dục'),
    (16, 'Marugoto_A2_Lesson_16.html', '🏃 Bài 16: Tập luyện & Vận động'),
    (17, 'Marugoto_A2_Lesson_17.html', '🎁 Bài 17: Quà tặng & Kỷ niệm'),
    (18, 'Marugoto_A2_Lesson_18.html', '👘 Bài 18: Tiệc tùng & Sự kiện'),
]

TEST_LINKS = [
    ('De_Thi_Midterm_A2_1.html', '🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)'),
    ('On_Tap_Dich_Cau_Lesson_1_10.html', '✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)'),
    ('On_Tap_Mini_Test_A2_1_4.html', '🎯 Ôn Tập Bài 1-4 (Mini Test)'),
    ('On_Tap_Mini_Test_A2_5_8.html', '🎯 Ôn Tập Bài 5-8 (Mini Test)'),
    ('De_Thi_Thu_Marugoto_A2_5_8.html', '📝 5 Mã Đề Thi Thử (101-105)'),
    ('Kiem_Tra_Marugoto_L6_7_8.html', '📑 Đề Kiểm Tra L6, 7, 8'),
    ('Luyen_Tap_The_Te_A2_1.html', '🌸 Luyện Tập Thể Te')
]

def find_global_nav_range(content):
    m = re.search(r'<div class="global-hub-nav"[^>]*>', content)
    if not m:
        return None, None
    start = m.start()
    depth = 0
    i = start
    while i < len(content):
        if content[i:i+4] == '<div':
            depth += 1
            i += 4
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return start, i + 6
            i += 6
        else:
            i += 1
    return None, None

def build_root_nav(current_file):
    is_te = (current_file == 'index.html')
    is_ru = (current_file == 'the_ru.html')
    is_ta = (current_file == 'the_ta.html')
    is_kanji = (current_file == 'kanji_a2.html')
    is_vocab = (current_file == 'Tu_Vung_Marugoto_A1_16_A2_1_10.html')

    tests_html = '\n                '.join([f'<a href="tests/{f}" class="hub-drop-link">{t}</a>' for f, t in TEST_LINKS])
    lessons_html = '\n                '.join([f'<a href="lessons/{f}" class="hub-drop-link">{t}</a>' for _, f, t in ALL_18_LESSONS])

    return f'''    <div class="global-hub-nav">
        <a href="index.html" class="hub-nav-item{" active-hub" if is_te else ""}">🌸 Thể TE (～て)</a>
        <a href="the_ru.html" class="hub-nav-item{" active-hub" if is_ru else ""}">📘 Thể RU (Từ Điển)</a>
        <a href="the_ta.html" class="hub-nav-item{" active-hub" if is_ta else ""}">📕 Thể TA (Quá Khứ)</a>
        <a href="kanji_a2.html" class="hub-nav-item{" active-hub" if is_kanji else ""}">⛩️ Học Kanji & Nét Viết</a>
        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item{" active-hub" if is_vocab else ""}">📖 Kho Từ Vựng A1-A2</a>
        <a href="demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                {tests_html}
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                {lessons_html}
            </div>
        </div>
    </div>'''

def build_lessons_nav(current_lesson_file):
    lesson_links = []
    for num, l_file, l_title in ALL_18_LESSONS:
        is_active = (l_file == current_lesson_file)
        lesson_links.append(f'<a href="{l_file}" class="hub-drop-link{" active" if is_active else ""}">{l_title}</a>')

    lessons_drop_html = '\n                '.join(lesson_links)
    tests_html = '\n                '.join([f'<a href="../tests/{f}" class="hub-drop-link">{t}</a>' for f, t in TEST_LINKS])

    return f'''    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="../the_ta.html" class="hub-nav-item">📕 Thể TA (Quá Khứ)</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="../Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="../demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                {tests_html}
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item active-hub" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                {lessons_drop_html}
            </div>
        </div>
    </div>'''

def build_tests_nav(current_test_file):
    test_links = []
    for t_file, t_title in TEST_LINKS:
        is_active = (t_file == current_test_file)
        test_links.append(f'<a href="{t_file}" class="hub-drop-link{" active" if is_active else ""}">{t_title}</a>')

    tests_drop_html = '\n                '.join(test_links)
    lessons_html = '\n                '.join([f'<a href="../lessons/{f}" class="hub-drop-link">{t}</a>' for _, f, t in ALL_18_LESSONS])

    return f'''    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="../the_ta.html" class="hub-nav-item">📕 Thể TA (Quá Khứ)</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="../Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="../demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item active-hub" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                {tests_drop_html}
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                {lessons_html}
            </div>
        </div>
    </div>'''

def ensure_dropdown_css(content):
    # Ensure .hub-dropdown-menu has max-height: 480px; overflow-y: auto;
    pattern = r'(\.hub-dropdown-menu\s*\{[^}]*?)(min-width:\s*2[0-9]{2}px;)'
    if re.search(pattern, content):
        if 'overflow-y:' not in content[re.search(pattern, content).start():re.search(pattern, content).end() + 100]:
            content = re.sub(
                r'(\.hub-dropdown-menu\s*\{[^}]*?min-width:\s*2[0-9]{2}px;)',
                r'\1\n            max-height: 480px;\n            overflow-y: auto;\n            scrollbar-width: thin;',
                content,
                count=1
            )
    return content

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start, end = find_global_nav_range(content)
    if start is None:
        print(f"Skipping {file_path}: No global nav found")
        return False

    base_name = os.path.basename(file_path)
    if file_path.startswith('lessons/'):
        new_nav = build_lessons_nav(base_name)
    elif file_path.startswith('tests/'):
        new_nav = build_tests_nav(base_name)
    else:
        new_nav = build_root_nav(base_name)

    updated_content = content[:start] + new_nav + content[end:]
    updated_content = ensure_dropdown_css(updated_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Successfully updated: {file_path}")
    return True

def main():
    root_files = [
        'index.html',
        'the_ru.html',
        'the_ta.html',
        'kanji_a2.html',
        'Tu_Vung_Marugoto_A1_16_A2_1_10.html',
        'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html'
    ]
    lesson_files = sorted(glob.glob('lessons/Marugoto_A2_Lesson_*.html'))
    test_files = sorted([f for f in glob.glob('tests/*.html') if 'mockup' not in f])

    all_files = root_files + lesson_files + test_files
    print(f"Starting update on {len(all_files)} files...")
    success_count = 0
    for f in all_files:
        if process_file(f):
            success_count += 1

    print(f"DONE! Successfully synchronized {success_count}/{len(all_files)} files.")

if __name__ == '__main__':
    main()
