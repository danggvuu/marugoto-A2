#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/sync_clean_nav.py
Đồng bộ thanh navigation trên toàn bộ 22 file HTML:
- Xóa bỏ nút Ngữ Pháp: '📚 Ngữ Pháp A1-A2 (26 Bài)'
- Đổi nút '🚀 Web Bài Học 10-18 ▾' thành '🚀 Web Bài Học ▾' trên tất cả các trang
- Dọn dẹp trùng lặp 'Thể TA' nếu có
- Giữ nguyên active-hub và dropdown scripts hoàn hảo
"""

import os
import re
import glob

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
                <a href="tests/De_Thi_Midterm_A2_1.html" class="hub-drop-link">🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)</a>
                <a href="tests/On_Tap_Dich_Cau_Lesson_1_10.html" class="hub-drop-link">✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)</a>
                <a href="tests/On_Tap_Mini_Test_A2_1_4.html" class="hub-drop-link">🎯 Ôn Tập Bài 1-4 (Mini Test)</a>
                <a href="tests/On_Tap_Mini_Test_A2_5_8.html" class="hub-drop-link">🎯 Ôn Tập Bài 5-8 (Mini Test)</a>
                <a href="tests/De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-drop-link">📝 5 Mã Đề Thi Thử (101-105)</a>
                <a href="tests/Kiem_Tra_Marugoto_L6_7_8.html" class="hub-drop-link">📑 Đề Kiểm Tra L6, 7, 8</a>
                <a href="tests/Luyen_Tap_The_Te_A2_1.html" class="hub-drop-link">🌸 Luyện Tập Thể Te</a>
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
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
    </div>'''

def build_lessons_nav(current_lesson_file):
    lesson_links = []
    for l_num, l_title in [
        (10, '🌟 Bài 10: 外国文化'),
        (11, '🍱 Bài 11: そとで食べる'),
        (12, '🍜 Bài 12: 特別な日の料理'),
        (13, '✈️ Bài 13: 出張'),
        (14, '💻 Bài 14: 職場のマナー'),
        (15, '🏥 Bài 15: 健康な生活'),
        (16, '🏃 Bài 16: 体にいいこと'),
        (17, '🎁 Bài 17: お祝い'),
        (18, '👘 Bài 18: お祭りやイベント')
    ]:
        l_file = f'Marugoto_A2_Lesson_{l_num}.html'
        is_active = (l_file == current_lesson_file)
        lesson_links.append(f'<a href="{l_file}" class="hub-drop-link{" active" if is_active else ""}">{l_title}</a>')

    lessons_drop_html = '\n                '.join(lesson_links)

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
                <a href="../tests/De_Thi_Midterm_A2_1.html" class="hub-drop-link">🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)</a>
                <a href="../tests/On_Tap_Dich_Cau_Lesson_1_10.html" class="hub-drop-link">✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)</a>
                <a href="../tests/On_Tap_Mini_Test_A2_1_4.html" class="hub-drop-link">🎯 Ôn Tập Bài 1-4 (Mini Test)</a>
                <a href="../tests/On_Tap_Mini_Test_A2_5_8.html" class="hub-drop-link">🎯 Ôn Tập Bài 5-8 (Mini Test)</a>
                <a href="../tests/De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-drop-link">📝 5 Mã Đề Thi Thử (101-105)</a>
                <a href="../tests/Kiem_Tra_Marugoto_L6_7_8.html" class="hub-drop-link">📑 Đề Kiểm Tra L6, 7, 8</a>
                <a href="../tests/Luyen_Tap_The_Te_A2_1.html" class="hub-drop-link">🌸 Luyện Tập Thể Te</a>
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
    for t_file, t_title in [
        ('De_Thi_Midterm_A2_1.html', '🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)'),
        ('On_Tap_Dich_Cau_Lesson_1_10.html', '✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)'),
        ('On_Tap_Mini_Test_A2_1_4.html', '🎯 Ôn Tập Bài 1-4 (Mini Test)'),
        ('On_Tap_Mini_Test_A2_5_8.html', '🎯 Ôn Tập Bài 5-8 (Mini Test)'),
        ('De_Thi_Thu_Marugoto_A2_5_8.html', '📝 5 Mã Đề Thi Thử (101-105)'),
        ('Kiem_Tra_Marugoto_L6_7_8.html', '📑 Đề Kiểm Tra L6, 7, 8'),
        ('Luyen_Tap_The_Te_A2_1.html', '🌸 Luyện Tập Thể Te')
    ]:
        is_active = (t_file == current_test_file)
        test_links.append(f'<a href="{t_file}" class="hub-drop-link{" active" if is_active else ""}">{t_title}</a>')

    tests_drop_html = '\n                '.join(test_links)

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
                <a href="../lessons/Marugoto_A2_Lesson_10.html" class="hub-drop-link">🌟 Bài 10: 外国文化</a>
                <a href="../lessons/Marugoto_A2_Lesson_11.html" class="hub-drop-link">🍱 Bài 11: そとで食べる</a>
                <a href="../lessons/Marugoto_A2_Lesson_12.html" class="hub-drop-link">🍜 Bài 12: 特別な日の料理</a>
                <a href="../lessons/Marugoto_A2_Lesson_13.html" class="hub-drop-link">✈️ Bài 13: 出張</a>
                <a href="../lessons/Marugoto_A2_Lesson_14.html" class="hub-drop-link">💻 Bài 14: 職場のマナー</a>
                <a href="../lessons/Marugoto_A2_Lesson_15.html" class="hub-drop-link">🏥 Bài 15: 健康な生活</a>
                <a href="../lessons/Marugoto_A2_Lesson_16.html" class="hub-drop-link">🏃 Bài 16: 体にいいこと</a>
                <a href="../lessons/Marugoto_A2_Lesson_17.html" class="hub-drop-link">🎁 Bài 17: お祝い</a>
                <a href="../lessons/Marugoto_A2_Lesson_18.html" class="hub-drop-link">👘 Bài 18: お祭りやイベント</a>
            </div>
        </div>
    </div>'''

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
