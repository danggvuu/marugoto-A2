# -*- coding: utf-8 -*-
"""
update_all_paths.py
Updates all asset links, navigation links, and document references across:
- Root HTML portals
- lessons/*.html
- tests/*.html
- README.md
"""

import os
import glob
import re

ROOT_PORTALS = [
    'index.html',
    'the_ru.html',
    'kanji_a2.html',
    'Tu_Vung_Marugoto_A1_16_A2_1_10.html',
    'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html',
    'demo_3d.html'
]

LESSON_FILES = [f'Marugoto_A2_Lesson_{i}.html' for i in range(10, 19)]

TEST_FILES = [
    'De_Thi_Thu_Marugoto_A2_5_8.html',
    'On_Tap_Mini_Test_A2_1_4.html',
    'On_Tap_Mini_Test_A2_5_8.html',
    'Kiem_Tra_Marugoto_L6_7_8.html',
    'Luyen_Tap_The_Te_A2_1.html',
    'mockup_portal_options.html'
]

# 1. Update Root Portals
for fn in ROOT_PORTALS:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Asset paths
    content = re.sub(r'href=([\'\"])animate-ui\.css([\'\"])', r'href=\1assets/css/animate-ui.css\2', content)
    content = re.sub(r'src=([\'\"])animate-ui\.js([\'\"])', r'src=\1assets/js/animate-ui.js\2', content)
    content = re.sub(r'src=([\'\"])audio-engine\.js([\'\"])', r'src=\1assets/js/audio-engine.js\2', content)

    # Links to lessons
    for lf in LESSON_FILES:
        content = re.sub(rf'href=([\'\"]){lf}([\'\"])', rf'href=\1lessons/{lf}\2', content)

    # Links to tests
    for tf in TEST_FILES:
        content = re.sub(rf'href=([\'\"]){tf}([\'\"])', rf'href=\1tests/{tf}\2', content)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated root portal: {fn}')

# 2. Update Lessons
for lf in LESSON_FILES:
    path = os.path.join('lessons', lf)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Asset paths
    content = re.sub(r'href=([\'\"])(?:\.\./)?animate-ui\.css([\'\"])', r'href=\1../assets/css/animate-ui.css\2', content)
    content = re.sub(r'src=([\'\"])(?:\.\./)?animate-ui\.js([\'\"])', r'src=\1../assets/js/animate-ui.js\2', content)
    content = re.sub(r'src=([\'\"])(?:\.\./)?audio-engine\.js([\'\"])', r'src=\1../assets/js/audio-engine.js\2', content)

    # Links to root portals
    for rf in ROOT_PORTALS:
        content = re.sub(rf'href=([\'\"])(?:\.\./)?{rf}([\'\"])', rf'href=\1../{rf}\2', content)

    # Links to tests
    for tf in TEST_FILES:
        content = re.sub(rf'href=([\'\"])(?:\.\./)?(?:\.\./tests/)?{tf}([\'\"])', rf'href=\1../tests/{tf}\2', content)

    # Links to other lessons (remain relative inside lessons/)
    for other_lf in LESSON_FILES:
        content = re.sub(rf'href=([\'\"])(?:\.\./)?(?:lessons/)?{other_lf}([\'\"])', rf'href=\1{other_lf}\2', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated lesson: {path}')

# 3. Update Tests
for tf in TEST_FILES:
    path = os.path.join('tests', tf)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Asset paths
    content = re.sub(r'href=([\'\"])(?:\.\./)?animate-ui\.css([\'\"])', r'href=\1../assets/css/animate-ui.css\2', content)
    content = re.sub(r'src=([\'\"])(?:\.\./)?animate-ui\.js([\'\"])', r'src=\1../assets/js/animate-ui.js\2', content)
    content = re.sub(r'src=([\'\"])(?:\.\./)?audio-engine\.js([\'\"])', r'src=\1../assets/js/audio-engine.js\2', content)

    # Links to root portals
    for rf in ROOT_PORTALS:
        content = re.sub(rf'href=([\'\"])(?:\.\./)?{rf}([\'\"])', rf'href=\1../{rf}\2', content)

    # Links to lessons
    for lf in LESSON_FILES:
        content = re.sub(rf'href=([\'\"])(?:\.\./)?(?:lessons/)?{lf}([\'\"])', rf'href=\1../lessons/{lf}\2', content)

    # Links to other tests (remain relative inside tests/)
    for other_tf in TEST_FILES:
        content = re.sub(rf'href=([\'\"])(?:\.\./)?(?:tests/)?{other_tf}([\'\"])', rf'href=\1{other_tf}\2', content)

    # PDF links in On_Tap_Mini_Test_A2_5_8.html
    content = re.sub(r'href=([\'\"])(?:\.\./)?([^\'\"]+\.pdf)([\'\"])', r'href=\1../docs/pdf/\2\3', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated test: {path}')

print("All HTML files updated successfully!")
