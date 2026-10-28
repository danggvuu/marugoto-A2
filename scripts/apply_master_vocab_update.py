# -*- coding: utf-8 -*-
import json
import re

with open('master_vocab_official.json', 'r', encoding='utf-8') as f:
    vocab_data = json.load(f)

# 1. Format rawVocab
raw_vocab_lines = ['    // Master Vocabulary Data\n    const rawVocab = [']
current_l = None
for item in vocab_data:
    if item['l'] != current_l:
        current_l = item['l']
        raw_vocab_lines.append(f'        // {current_l}')
    raw_vocab_lines.append(f'        {{ l: {json.dumps(item["l"], ensure_ascii=False)}, jp: {json.dumps(item["jp"], ensure_ascii=False)}, vi: {json.dumps(item["vi"], ensure_ascii=False)} }},')
raw_vocab_lines.append('    ];\n')
new_raw_vocab_str = '\n'.join(raw_vocab_lines)

# 2. LESSON_ORDER and LESSON_TITLES
LESSON_ORDER = [
    'A1-3', 'A1-4', 'A1-5', 'A1-6', 'A1-7', 'A1-8', 'A1-9', 'A1-10',
    'A1-11', 'A1-12', 'A1-13', 'A1-14', 'A1-15', 'A1-16', 'A1-17', 'A1-18',
    'A2-1', 'A2-2', 'A2-3', 'A2-4', 'A2-5', 'A2-6', 'A2-7', 'A2-8',
    'A2-9', 'A2-10', 'A2-11', 'A2-12', 'A2-13', 'A2-14', 'A2-15', 'A2-16',
    'A2-17', 'A2-18'
]

LESSON_TITLES = {
    'A1-3': 'Bài 3: Gia đình tôi có 4 người (かぞくは よにんです。)',
    'A1-4': 'Bài 4: Gia đình tôi có 4 người (かぞくは よにんです。)',
    'A1-5': 'Bài 5: Bạn thích gì? (なにがすきですか。)',
    'A1-6': 'Bài 6: Bạn ăn ở đâu? (どこで たべますか。)',
    'A1-7': 'Bài 7: Có 3 phòng (へやが みっつ あります。)',
    'A1-8': 'Bài 8: Phòng đẹp nhỉ (いい へやですね。)',
    'A1-9': 'Bài 9: Mấy giờ thức dậy? (なんじに おきますか。)',
    'A1-10': 'Bài 10: Khi nào thì được? (いつが いいですか。)',
    'A1-11': 'Bài 11: Sở thích của bạn là gì? (しゅみは なんですか。)',
    'A1-12': 'Bài 12: Cùng đi không? (いっしょに いきませんか。)',
    'A1-13': 'Bài 13: Đi bằng phương tiện gì? (どうやって いきますか。)',
    'A1-14': 'Bài 14: Ngôi chùa nổi tiếng (ゆうめいな おてらです。)',
    'A1-15': 'Bài 15: Dễ thương quá! (かわいい！)',
    'A1-16': 'Bài 16: Mua sắm (これ、ください。)',
    'A1-17': 'Bài 17: Trải nghiệm (たのしかったです。)',
    'A1-18': 'Bài 18: Du lịch (つぎは きょうとに いきたいです。)',
    'A2-1':  'Bài 1: Nơi ở (東京に すんでいます。)',
    'A2-2':  'Bài 2: Sở thích (しゅみは クラシックを 聞くことです。)',
    'A2-3':  'Bài 3: Mùa & Khí hậu (日本はいま、はるです。)',
    'A2-4':  'Bài 4: Thời tiết (いい てんきですね。)',
    'A2-5':  'Bài 5: Phố xá & Công viên (この こうえんは ひろくて、きれいです。)',
    'A2-6':  'Bài 6: Chỉ đường (まっすぐ 行ってください。)',
    'A2-7':  'Bài 7: Hẹn gặp (10時でも いいですか。)',
    'A2-8':  'Bài 8: Cảnh đêm (もう やけいを 見に 行きましたか。)',
    'A2-9':  'Bài 9: Ngôn ngữ & Phát âm (日本語は はつおんが かんたんです。)',
    'A2-10': 'Bài 10: Tiếng Nhật (日本語は はつおんが かんたんです。)',
    'A2-11': 'Bài 11: Mang theo cái gì dã ngoại (何を 持っていきますか。)',
    'A2-12': 'Bài 12: Món ăn ngon & Vị giác (おいしそうですね。)',
    'A2-13': 'Bài 13: Gặp gỡ & Chuyến công tác (たなかさんに 会ったことが ありますか。)',
    'A2-14': 'Bài 14: Văn phòng & Quy tắc (これ、つかっても いいですか。)',
    'A2-15': 'Bài 15: Sức khỏe & Thể dục (たいそうすると いいですよ。)',
    'A2-16': 'Bài 16: Tập luyện & Vận động (はしったり およいだり しています。)',
    'A2-17': 'Bài 17: Quà tặng sinh nhật (誕生日に もらったんです。)',
    'A2-18': 'Bài 18: Tiệc tùng & Sự kiện (パーティーが いいと おもいます。)'
}

new_order_titles = f'''    // ==========================================
    // MULTI-LESSON SELECTION & FILTER LOGIC
    // ==========================================
    const LESSON_ORDER = {json.dumps(LESSON_ORDER, ensure_ascii=False, indent=8)};

    const LESSON_TITLES = {json.dumps(LESSON_TITLES, ensure_ascii=False, indent=8)};
'''

with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <title>
html = re.sub(
    r'<title>.*?</title>',
    '<title>📖 Kho Từ Vựng Toàn Diện Marugoto A1 (L3-18) + A2-1 (L1-18) - 1,200+ Từ Chuẩn Giáo Trình</title>',
    html
)

# Replace rawVocab
start_marker = '    // Master Vocabulary Data\n    const rawVocab = ['
end_marker = '    let currentFiltered = [...rawVocab];'

s_idx = html.find(start_marker)
e_idx = html.find(end_marker)
if s_idx != -1 and e_idx != -1:
    html = html[:s_idx] + new_raw_vocab_str + '\n' + html[e_idx:]
else:
    print('Error finding rawVocab bounds!')

# Replace LESSON_ORDER & LESSON_TITLES
s2 = html.find('    // MULTI-LESSON SELECTION & FILTER LOGIC\n    // ==========================================\n    const LESSON_ORDER = [')
e2 = html.find('    let selectedLessons = new Set(LESSON_ORDER);')
if s2 != -1 and e2 != -1:
    html = html[:s2] + new_order_titles + '\n' + html[e2:]
else:
    print('Error finding LESSON_ORDER bounds!')

# Update Preset Buttons in HTML
old_presets = '''                <div class="quick-presets">
                    <button class="preset-pill active" id="preset-all" onclick="selectPreset('ALL')">🌟 Tất cả (21 bài)</button>
                    <button class="preset-pill" id="preset-a1" onclick="selectPreset('A1')">A1 (16-18)</button>
                    <button class="preset-pill" id="preset-a2-1-10" onclick="selectPreset('A2_1_10')">A2-1 (1-10)</button>
                    <button class="preset-pill" id="preset-a2-11-18" onclick="selectPreset('A2_11_18')">A2-2 (11-18) ✨</button>
                    <button class="preset-pill" id="preset-a2-all" onclick="selectPreset('A2_ALL')">Trọn bộ A2 (1-18)</button>
                    <button class="preset-pill preset-clear" onclick="selectPreset('NONE')">🗑️ Bỏ chọn hết</button>
                </div>'''

new_presets = '''                <div class="quick-presets">
                    <button class="preset-pill active" id="preset-all" onclick="selectPreset('ALL')">🌟 Tất cả (34 bài / 1,200+ từ)</button>
                    <button class="preset-pill" id="preset-a1" onclick="selectPreset('A1')">A1 (Bài 3 - 18)</button>
                    <button class="preset-pill" id="preset-a2-1-10" onclick="selectPreset('A2_1_10')">A2-1 (Bài 1 - 10)</button>
                    <button class="preset-pill" id="preset-a2-11-18" onclick="selectPreset('A2_11_18')">A2-1 (Bài 11 - 18) ✨</button>
                    <button class="preset-pill" id="preset-a2-all" onclick="selectPreset('A2_ALL')">Trọn bộ A2 (Bài 1 - 18)</button>
                    <button class="preset-pill preset-clear" onclick="selectPreset('NONE')">🗑️ Bỏ chọn hết</button>
                </div>'''

if old_presets in html:
    html = html.replace(old_presets, new_presets)
else:
    print('Note: old_presets exact match not found, checking regex replacement')

# Update Chips groups titles
html = html.replace('Marugoto A1 (Bài 16 - 18):', 'Marugoto A1 (Bài 3 - 18):')
html = html.replace('Marugoto A2-1 (Bài 1 - 10):', 'Marugoto A2-1 (Bài 1 - 10):')
html = html.replace('Marugoto A2-2 (Bài 11 - 18 Mới ✨):', 'Marugoto A2-1 (Bài 11 - 18 Mới ✨):')

# Update initLessonChips()
old_init_chips_sub = '''        // 1. Tạo nhóm A1 trong Dropdown
        if (msList) {
            const grpA1 = document.createElement('div');
            grpA1.className = 'ms-group-header';
            grpA1.innerHTML = `
                <span>Marugoto A1 (Bài 16 - 18)</span>
                <button type="button" class="ms-group-btn" onclick="toggleGroup('A1')">Chọn nhóm A1</button>
            `;
            msList.appendChild(grpA1);
        }

        LESSON_ORDER.forEach((lid, idx) => {
            const isA1 = lid.startsWith('A1');
            const targetCont = isA1 ? containerA1 : containerA2;
            const count = lessonCounts[lid] || 0;
            const title = LESSON_TITLES[lid] || lid;

            // Chèn Header nhóm A2 khi bắt đầu bài A2-1
            if (msList && lid === 'A2-1') {
                const grpA2 = document.createElement('div');
                grpA2.className = 'ms-group-header';
                grpA2.innerHTML = `
                    <span>Marugoto A2-1 (Bài 1 - 10)</span>
                    <button type="button" class="ms-group-btn" onclick="toggleGroup('A2')">Chọn nhóm A2-1</button>
                `;
                msList.appendChild(grpA2);
            }'''

new_init_chips_sub = '''        const containerA2_2 = document.getElementById('chipsContainerA2_2');
        if (containerA2_2) containerA2_2.innerHTML = '';

        // 1. Tạo nhóm A1 trong Dropdown
        if (msList) {
            const grpA1 = document.createElement('div');
            grpA1.className = 'ms-group-header';
            grpA1.innerHTML = `
                <span>Marugoto A1 (Bài 3 - 18)</span>
                <button type="button" class="ms-group-btn" onclick="toggleGroup('A1')">Chọn nhóm A1 (3-18)</button>
            `;
            msList.appendChild(grpA1);
        }

        LESSON_ORDER.forEach((lid, idx) => {
            let targetCont = containerA1;
            if (lid.startsWith('A1')) {
                targetCont = containerA1;
            } else {
                const num = parseInt(lid.split('-')[1], 10);
                if (num <= 10) {
                    targetCont = containerA2;
                } else {
                    targetCont = containerA2_2;
                }
            }
            const count = lessonCounts[lid] || 0;
            const title = LESSON_TITLES[lid] || lid;

            // Chèn Header nhóm A2 khi bắt đầu bài A2-1
            if (msList && lid === 'A2-1') {
                const grpA2 = document.createElement('div');
                grpA2.className = 'ms-group-header';
                grpA2.innerHTML = `
                    <span>Marugoto A2-1 (Bài 1 - 10)</span>
                    <button type="button" class="ms-group-btn" onclick="toggleGroup('A2_1')">Chọn nhóm A2-1 (1-10)</button>
                `;
                msList.appendChild(grpA2);
            }

            // Chèn Header nhóm A2 (11-18) khi bắt đầu bài A2-11
            if (msList && lid === 'A2-11') {
                const grpA2_2 = document.createElement('div');
                grpA2_2.className = 'ms-group-header';
                grpA2_2.innerHTML = `
                    <span>Marugoto A2-1 (Bài 11 - 18 Mới ✨)</span>
                    <button type="button" class="ms-group-btn" onclick="toggleGroup('A2_2')">Chọn nhóm A2-1 (11-18)</button>
                `;
                msList.appendChild(grpA2_2);
            }'''

if old_init_chips_sub in html:
    html = html.replace(old_init_chips_sub, new_init_chips_sub)
else:
    print('Note: old_init_chips_sub exact match not found!')

# Update range default
html = html.replace('rangeStart.value = "A2-1";', 'rangeStart.value = "A1-3";')
html = html.replace('rangeEnd.value = "A2-5";', 'rangeEnd.value = "A2-18";')

# Update toggleGroup
old_toggle_group = '''    // Chọn nhanh cả nhóm A1 hoặc A2
    function toggleGroup(groupName) {
        let targets = [];
        if (groupName === 'A1') {
            targets = ["A1-16", "A1-17", "A1-18"];
        } else if (groupName === 'A2_1' || groupName === 'A2') {
            targets = ["A2-1", "A2-2", "A2-3", "A2-4", "A2-5", "A2-6", "A2-7", "A2-8", "A2-9", "A2-10"];
        } else if (groupName === 'A2_2') {
            targets = ["A2-11", "A2-12", "A2-13", "A2-14", "A2-15", "A2-16", "A2-17", "A2-18"];
        }'''

new_toggle_group = '''    // Chọn nhanh cả nhóm A1 hoặc A2
    function toggleGroup(groupName) {
        let targets = [];
        if (groupName === 'A1') {
            targets = LESSON_ORDER.filter(l => l.startsWith('A1'));
        } else if (groupName === 'A2_1') {
            targets = ["A2-1", "A2-2", "A2-3", "A2-4", "A2-5", "A2-6", "A2-7", "A2-8", "A2-9", "A2-10"];
        } else if (groupName === 'A2_2') {
            targets = ["A2-11", "A2-12", "A2-13", "A2-14", "A2-15", "A2-16", "A2-17", "A2-18"];
        } else if (groupName === 'A2') {
            targets = LESSON_ORDER.filter(l => l.startsWith('A2'));
        }'''

if old_toggle_group in html:
    html = html.replace(old_toggle_group, new_toggle_group)
else:
    print('Note: old_toggle_group exact match not found!')

# Update selectPreset
old_select_preset = '''    // Chọn nhanh theo các Preset
    function selectPreset(type) {
        selectedLessons.clear();

        if (type === 'ALL') {
            LESSON_ORDER.forEach(l => selectedLessons.add(l));
        } else if (type === 'A1') {
            ["A1-16", "A1-17", "A1-18"].forEach(l => selectedLessons.add(l));
        } else if (type === 'A2_1_10') {
            ["A2-1", "A2-2", "A2-3", "A2-4", "A2-5", "A2-6", "A2-7", "A2-8", "A2-9", "A2-10"].forEach(l => selectedLessons.add(l));
        } else if (type === 'A2_11_18') {
            ["A2-11", "A2-12", "A2-13", "A2-14", "A2-15", "A2-16", "A2-17", "A2-18"].forEach(l => selectedLessons.add(l));
        } else if (type === 'A2_ALL') {
            LESSON_ORDER.filter(l => l.startsWith('A2')).forEach(l => selectedLessons.add(l));
        } else if (type === 'NONE') {
            // Bỏ chọn hết
        }'''

new_select_preset = '''    // Chọn nhanh theo các Preset
    function selectPreset(type) {
        selectedLessons.clear();

        if (type === 'ALL') {
            LESSON_ORDER.forEach(l => selectedLessons.add(l));
        } else if (type === 'A1') {
            LESSON_ORDER.filter(l => l.startsWith('A1')).forEach(l => selectedLessons.add(l));
        } else if (type === 'A2_1_10') {
            ["A2-1", "A2-2", "A2-3", "A2-4", "A2-5", "A2-6", "A2-7", "A2-8", "A2-9", "A2-10"].forEach(l => selectedLessons.add(l));
        } else if (type === 'A2_11_18') {
            ["A2-11", "A2-12", "A2-13", "A2-14", "A2-15", "A2-16", "A2-17", "A2-18"].forEach(l => selectedLessons.add(l));
        } else if (type === 'A2_ALL') {
            LESSON_ORDER.filter(l => l.startsWith('A2')).forEach(l => selectedLessons.add(l));
        } else if (type === 'NONE') {
            // Bỏ chọn hết
        }'''

if old_select_preset in html:
    html = html.replace(old_select_preset, new_select_preset)
else:
    print('Note: old_select_preset exact match not found!')

# Update triggerText in updateChipsUI
html = html.replace('🌟 Tất Cả Các Bài (A1-16 ➔ A2-18)', '🌟 Tất Cả Các Bài (A1-3 ➔ A2-18)')

# Update renderTable speaker button
old_render_table = '''        currentFiltered.forEach((item, idx) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td class="col-stt"><strong>${idx + 1}</strong></td>
                <td class="col-lesson"><span class="tag-lesson">${item.l}</span></td>
                <td class="col-jp"><span class="jp-word">${item.jp}</span></td>
                <td class="col-vi"><span class="vi-word">${item.vi}</span></td>
            `;
            tbody.appendChild(tr);
        });'''

new_render_table = '''        currentFiltered.forEach((item, idx) => {
            const tr = document.createElement('tr');
            const safeJp = item.jp.replace(/'/g, "\\\\'");
            tr.innerHTML = `
                <td class="col-stt"><strong>${idx + 1}</strong></td>
                <td class="col-lesson"><span class="tag-lesson">${item.l}</span></td>
                <td class="col-jp">
                    <span class="jp-word">${item.jp}</span>
                    <button type="button" class="btn-speak-inline" onclick="speakJapanese('${safeJp}')" title="Nghe phát âm chuẩn Tokyo">🔊</button>
                </td>
                <td class="col-vi"><span class="vi-word">${item.vi}</span></td>
            `;
            tbody.appendChild(tr);
        });'''

if old_render_table in html:
    html = html.replace(old_render_table, new_render_table)
else:
    print('Note: old_render_table exact match not found!')

# Style for btn-speak-inline if not present
if '.btn-speak-inline' not in html:
    btn_style = '''
    .btn-speak-inline {
        background: #f0fdf4;
        border: 1px solid #86efac;
        color: #166534;
        border-radius: 50%;
        width: 26px;
        height: 26px;
        cursor: pointer;
        font-size: 0.75rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-left: 6px;
        transition: all 0.2s;
        vertical-align: middle;
    }
    .btn-speak-inline:hover {
        background: #22c55e;
        color: #fff;
        transform: scale(1.1);
    }
    '''
    html = html.replace('</style>', btn_style + '\n</style>')

with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated Tu_Vung_Marugoto_A1_16_A2_1_10.html successfully!')
