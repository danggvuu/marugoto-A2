#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/sync_all_nav_8_items.py
Đồng bộ thanh điều hướng 8 mục toàn hệ thống (Global Hub Nav)
- Dùng độc quyền assets/js/nav-dropdown.js (không inject script inline trùng lặp)
- An toàn tuyệt đối với mọi thẻ <script> và dữ liệu nội dung
"""

import re
import os
import glob

def clean_file_artifacts(content):
    # Dọn dẹp dock cũ (nếu còn)
    content = re.sub(r'<!-- GLOBAL FLOATING DOCK -->\s*(?:</div>\s*)+', '', content)
    # Dọn dẹp các khối dropdown js inline cũ
    content = re.sub(r'<script>\s*function toggleTestsDropdown\(.*?window\.toggleLessonsDropdown = toggleLessonsDropdown;\s*</script>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// Dropdown Toggles for Hub Nav.*?</script>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<script\s+src="[^"]*assets/js/nav-dropdown\.js"></script>\s*', '', content)
    content = re.sub(r'\\n<script>\s*</script>\s*', '', content)
    content = re.sub(r'<script>\s*</script>\s*', '', content)
    return content

def sync_lessons():
    lesson_files = sorted(glob.glob('lessons/Marugoto_A2_Lesson_*.html'))
    for fn in lesson_files:
        current_l = os.path.basename(fn)
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()

        c = clean_file_artifacts(c)

        lessons_drop = []
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
            is_active = (l_file == current_l)
            lessons_drop.append(f'<a href="{l_file}" class="hub-drop-link{" active" if is_active else ""}">{l_title}</a>')

        lessons_drop_html = '\n                '.join(lessons_drop)

        nav_html = f'''    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="../Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="../Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
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
            <button type="button" class="hub-nav-item active-hub" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học 10-18 ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                {lessons_drop_html}
            </div>
        </div>
    </div>'''

        # Replace existing global-hub-nav in lesson
        c = re.sub(r'<div class="global-hub-nav">.*?</div>\s*</div>\s*</div>', nav_html, c, flags=re.DOTALL)

        # Inject script before </body>
        script_block = '<script src="../assets/js/nav-dropdown.js"></script>'
        if '</body>' in c:
            c = c.replace('</body>', f'{script_block}\n</body>', 1)

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated Lesson: {fn}")

def sync_tests():
    test_files = sorted(glob.glob('tests/*.html'))
    for fn in test_files:
        if 'mockup' in fn:
            continue
        current_t = os.path.basename(fn)
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()

        c = clean_file_artifacts(c)

        tests_drop = []
        for t_file, t_title in [
            ('De_Thi_Midterm_A2_1.html', '🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)'),
            ('On_Tap_Dich_Cau_Lesson_1_10.html', '✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)'),
            ('On_Tap_Mini_Test_A2_1_4.html', '🎯 Ôn Tập Bài 1-4 (Mini Test)'),
            ('On_Tap_Mini_Test_A2_5_8.html', '🎯 Ôn Tập Bài 5-8 (Mini Test)'),
            ('De_Thi_Thu_Marugoto_A2_5_8.html', '📝 5 Mã Đề Thi Thử (101-105)'),
            ('Kiem_Tra_Marugoto_L6_7_8.html', '📑 Đề Kiểm Tra L6, 7, 8'),
            ('Luyen_Tap_The_Te_A2_1.html', '🌸 Luyện Tập Thể Te')
        ]:
            is_active = (t_file == current_t)
            tests_drop.append(f'<a href="{t_file}" class="hub-drop-link{" active" if is_active else ""}">{t_title}</a>')

        tests_drop_html = '\n                '.join(tests_drop)

        nav_html = f'''    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="../Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="../Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
        <a href="../demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item active-hub" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                {tests_drop_html}
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học 10-18 ▾</button>
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

        # Replace existing global-hub-nav in test
        c = re.sub(r'<div class="global-hub-nav">.*?</div>\s*</div>\s*</div>', nav_html, c, flags=re.DOTALL)

        # Inject script before </body>
        script_block = '<script src="../assets/js/nav-dropdown.js"></script>'
        if '</body>' in c:
            c = c.replace('</body>', f'{script_block}\n</body>', 1)

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated Test: {fn}")

def sync_roots():
    root_files = [
        'index.html',
        'the_ru.html',
        'kanji_a2.html',
        'Tu_Vung_Marugoto_A1_16_A2_1_10.html',
        'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html'
    ]
    for fn in root_files:
        current_r = fn
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()

        c = clean_file_artifacts(c)

        is_te = (current_r == 'index.html')
        is_ru = (current_r == 'the_ru.html')
        is_kanji = (current_r == 'kanji_a2.html')
        is_vocab = (current_r == 'Tu_Vung_Marugoto_A1_16_A2_1_10.html')
        is_grammar = (current_r == 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html')

        nav_html = f'''    <div class="global-hub-nav">
        <a href="index.html" class="hub-nav-item{" active-hub" if is_te else ""}">🌸 Thể TE (～て)</a>
        <a href="the_ru.html" class="hub-nav-item{" active-hub" if is_ru else ""}">📘 Thể RU (Từ Điển)</a>
        <a href="kanji_a2.html" class="hub-nav-item{" active-hub" if is_kanji else ""}">⛩️ Học Kanji & Nét Viết</a>
        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item{" active-hub" if is_vocab else ""}">📖 Kho Từ Vựng A1-A2</a>
        <a href="Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item{" active-hub" if is_grammar else ""}">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
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
    </div>'''

        # Replace or inject nav
        if '<div class="global-hub-nav">' in c:
            c = re.sub(r'<div class="global-hub-nav">.*?</div>\s*</div>\s*</div>', nav_html, c, flags=re.DOTALL)
        else:
            if '<body>' in c:
                c = c.replace('<body>', f'<body>\n{nav_html}', 1)

        # Inject script before </body>
        script_block = '<script src="assets/js/nav-dropdown.js"></script>'
        if '</body>' in c:
            c = c.replace('</body>', f'{script_block}\n</body>', 1)

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated Root: {fn}")

if __name__ == '__main__':
    sync_lessons()
    sync_tests()
    sync_roots()
    print("All navigation bars and dropdown scripts successfully synchronized without leaks!")
