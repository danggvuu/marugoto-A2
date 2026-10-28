import re

FILES = [
    ('index.html', 'index.html'),
    ('the_ru.html', 'the_ru.html'),
    ('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'Tu_Vung_Marugoto_A1_16_A2_1_10.html'),
    ('Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html', 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html'),
]

for filename, active_url in FILES:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate the nav with active-hub on current file
    nav_html = f'''    <div class="global-hub-nav">
        <a href="index.html" class="hub-nav-item{' active-hub' if active_url == 'index.html' else ''}">🌸 Thể TE (～て)</a>
        <a href="the_ru.html" class="hub-nav-item{' active-hub' if active_url == 'the_ru.html' else ''}">📘 Thể RU (Từ Điển)</a>
        <a href="kanji_a2.html" class="hub-nav-item{' active-hub' if active_url == 'kanji_a2.html' else ''}">⛩️ Học Kanji & Nét Viết</a>
        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item{' active-hub' if active_url == 'Tu_Vung_Marugoto_A1_16_A2_1_10.html' else ''}">📖 Kho Từ Vựng A1-A2</a>
        <a href="Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item{' active-hub' if active_url == 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html' else ''}">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
        <a href="demo_3d.html" class="hub-nav-item{' active-hub' if active_url == 'demo_3d.html' else ''}">⛩️ Không Gian 3D</a>
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
    </div>'''

    pattern = r'<div class="global-hub-nav">.*?</div>\s*</div>\s*</div>'
    # Match the existing nav structure
    m = re.search(r'<div class="global-hub-nav">.*?</div>\s*</div>\s*</div>', content, re.DOTALL)
    if not m:
        # standard global-hub-nav closing
        m = re.search(r'<div class="global-hub-nav">.*?</div>\s*</div>', content, re.DOTALL)
    
    if m:
        content = content[:m.start()] + nav_html + content[m.end():]
        print(f"Updated nav in {filename}")
    else:
        # Try finding just `<div class="global-hub-nav">...</div>` with balanced closing
        # Let's find `<div class="global-hub-nav">` up to the next `<header`
        m2 = re.search(r'<div class="global-hub-nav">.*?(?=<header)', content, re.DOTALL)
        if m2:
            content = content[:m2.start()] + nav_html + '\n\n    ' + content[m2.end():]
            print(f"Updated nav in {filename} (pattern 2)")
        else:
            print(f"Could not find nav in {filename}")

    # Ensure toggleTestsDropdown function exists
    if 'function toggleTestsDropdown' not in content:
        js_func = '''
    function toggleTestsDropdown(e) {
        if (e) e.stopPropagation();
        const m = document.getElementById('testsDropdownMenu');
        if (m) m.classList.toggle('show');
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
    }
'''
        # Inject right before toggleLessonsDropdown
        if 'function toggleLessonsDropdown' in content:
            content = content.replace('function toggleLessonsDropdown', js_func + '\n    function toggleLessonsDropdown', 1)
        elif '</script>' in content:
            content = content.replace('</script>', js_func + '\n</script>', 1)

    # Ensure click listener closes testsDropdownMenu as well
    if 'testsDropdownMenu' not in content or "const tm = document.getElementById('testsDropdownMenu');" not in content:
        content = re.sub(
            r'window\.addEventListener\(\'click\',\s*\(\)\s*=>\s*\{[^}]*lessonsDropdownMenu[^}]*\}\);',
            '''window.addEventListener('click', () => {
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    });''',
            content
        )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Completed global hub nav synchronization across portals!")
