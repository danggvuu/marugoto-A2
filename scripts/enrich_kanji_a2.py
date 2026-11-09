import json
import re

def main():
    with open('data/kanji_vocab_11_18.json', 'r', encoding='utf-8') as f:
        vocab_11_18 = json.load(f)

    with open('kanji_a2.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update mode-tabs to include 4th tab
    old_tabs = '''    <!-- Mode Tabs (Segmented Control) -->
    <div class="mode-tabs">
        <button class="mode-tab-btn active" onclick="switchTab('tab-cards')">🎴 Thẻ Học & Luyện Viết (<span id="tabCountCards">144</span>)</button>
        <button class="mode-tab-btn" onclick="switchTab('tab-exercises')">✍️ Bài Tập Từ Vựng Kanji</button>
        <button class="mode-tab-btn" onclick="switchTab('tab-rules')">📏 8 Quy Tắc Bút Thuận</button>
    </div>'''

    new_tabs = '''    <!-- Mode Tabs (Segmented Control) -->
    <div class="mode-tabs">
        <button class="mode-tab-btn active" onclick="switchTab('tab-cards')">🎴 Thẻ Học & Luyện Viết (<span id="tabCountCards">144</span>)</button>
        <button class="mode-tab-btn" onclick="switchTab('tab-exercises')">✍️ Bài Tập Từ Vựng Kanji</button>
        <button class="mode-tab-btn" onclick="switchTab('tab-rules')">📏 8 Quy Tắc Bút Thuận</button>
        <button class="mode-tab-btn" onclick="switchTab('tab-vocab-11-18')">🎴 121 Từ Ghép Kanji (L11-18)</button>
    </div>'''

    if old_tabs in html:
        html = html.replace(old_tabs, new_tabs, 1)
        print('✅ Updated mode-tabs!')
    else:
        print('⚠️ Could not find old_tabs')

    # 2. Add TAB 4 panel after TAB 3
    tab4_html = '''    <!-- TAB 4: 121 KANJI COMPOUND VOCABULARY (LESSONS 11 - 18) -->
    <div id="tab-vocab-11-18" class="tab-panel">
        <div class="rules-card" style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
                <div>
                    <h2 style="color: var(--primary); font-size: 1.45rem; margin-bottom: 4px;">🎴 121 Từ Ghép Chữ Hán Trọng Tâm (Bài 11 ➔ 18)</h2>
                    <p style="color: var(--gray); font-size: 0.95rem; margin: 0;">Trọn bộ 121 từ vựng ghép Kanji cốt lõi thường xuyên xuất hiện trong bài thi Marugoto A2-2 và hội thoại thực tế.</p>
                </div>
                <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                    <button type="button" class="btn btn-success" onclick="copyAll121Quizlet()" title="Sao chép toàn bộ định dạng Tab để nạp vào Quizlet Pro">📋 Copy Quizlet (Tab)</button>
                    <button type="button" class="btn btn-secondary" onclick="copyAll121Colon()" title="Sao chép dạng: 車、xe ô tô, XA: くるま">📋 Copy Dạng Dấu Phẩy</button>
                    <a href="tests/On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html" target="_blank" class="btn btn-outline" style="text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">⚡ Đấu Trường Cấp Tốc Đêm Nay ↗️</a>
                </div>
            </div>

            <!-- Filter by Lesson Bar -->
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;">
                <button type="button" class="filter-121-btn active" onclick="filter121Vocab('ALL', this)">🌟 Tất Cả (121)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(11, this)">Bài 11 (15)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(12, this)">Bài 12 (18)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(13, this)">Bài 13 (22)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(14, this)">Bài 14 (16)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(15, this)">Bài 15 (15)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(16, this)">Bài 16 (14)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(17, this)">Bài 17 (10)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(18, this)">Bài 18 (11)</button>
            </div>

            <!-- Search box -->
            <div style="margin-bottom: 18px;">
                <input type="text" id="search121Input" placeholder="🔍 Tìm kiếm từ ghép Kanji, cách đọc Hiragana, hoặc nghĩa tiếng Việt..." style="width: 100%; padding: 10px 16px; border: 1.5px solid var(--border); border-radius: 10px; font-size: 0.95rem;" oninput="onSearch121Change()">
            </div>

            <!-- Table of 121 Kanji Compound Words -->
            <div class="ex-table-container">
                <table class="ex-table">
                    <thead>
                        <tr>
                            <th style="width: 60px; text-align: center;">STT</th>
                            <th style="width: 80px; text-align: center;">Bài</th>
                            <th style="width: 220px;">Từ Ghép Kanji</th>
                            <th style="width: 200px;">Cách Đọc (Hiragana)</th>
                            <th>Ý Nghĩa Tiếng Việt</th>
                            <th style="width: 130px; text-align: center;">Chủ Đề</th>
                            <th style="width: 90px; text-align: center;">Thao Tác</th>
                        </tr>
                    </thead>
                    <tbody id="table121Body">
                        <!-- Populated by JS -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>'''

    rules_end = '        </div>\n    </div>\n\n    <footer>'
    if rules_end in html:
        html = html.replace(rules_end, '        </div>\n    </div>\n\n' + tab4_html + '\n\n    <footer>', 1)
        print('✅ Inserted TAB 4 markup!')
    else:
        print('⚠️ Could not find rules_end')

    # 3. Add CSS for filter-121-btn
    css_to_add = '''
        .filter-121-btn {
            padding: 7px 16px;
            border-radius: 9999px;
            border: 1.5px solid var(--border);
            background: #ffffff;
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--gray);
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .filter-121-btn:hover {
            border-color: var(--primary);
            color: var(--primary);
            background: #f0fdf4;
        }
        .filter-121-btn.active {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 2px 8px rgba(5, 150, 105, 0.3);
        }
    '''
    if '</style>' in html:
        html = html.replace('</style>', css_to_add + '\n    </style>', 1)
        print('✅ Added CSS for filter-121-btn!')

    # 4. Add JS logic and embedded 121 vocab data
    vocab_json_str = json.dumps(vocab_11_18, ensure_ascii=False)
    js_code = f'''
    // 121 Kanji Compound Vocab Data (Lessons 11-18)
    const VOCAB_121_DATA = {vocab_json_str};
    let current121Filtered = [...VOCAB_121_DATA];
    let current121Lesson = 'ALL';

    function render121Table() {{
        const tbody = document.getElementById('table121Body');
        if (!tbody) return;
        tbody.innerHTML = '';

        if (current121Filtered.length === 0) {{
            tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--gray); padding: 30px;">Không tìm thấy từ vựng nào phù hợp!</td></tr>`;
            return;
        }}

        current121Filtered.forEach((item, idx) => {{
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td style="text-align: center; font-weight: 700; color: var(--gray);">#${{idx + 1}}</td>
                <td style="text-align: center;"><span style="background: #e0e7ff; color: #4338ca; padding: 3px 8px; border-radius: 6px; font-weight: 700; font-size: 0.82rem;">Bài ${{item.lesson}}</span></td>
                <td><strong style="font-size: 1.15rem; color: #1e293b;">${{item.kanji}}</strong></td>
                <td><span style="font-size: 1.05rem; color: var(--primary-dark); font-weight: 600;">${{item.kana}}</span></td>
                <td><span style="color: #334155; font-size: 0.95rem;">${{item.vi}}</span></td>
                <td style="text-align: center;"><span style="background: #f1f5f9; color: #475569; padding: 3px 8px; border-radius: 6px; font-size: 0.8rem; font-weight: 600;">${{item.group || 'Từ vựng'}}</span></td>
                <td style="text-align: center;">
                    <button type="button" class="btn-sound-small" onclick="speakText('${{item.kana}}')" title="Nghe phát âm" style="background: #f8fafc; border: 1px solid var(--border); padding: 4px 8px; border-radius: 6px; cursor: pointer;">🔊</button>
                </td>
            `;
            tbody.appendChild(tr);
        }});
    }}

    function filter121Vocab(lesson, btn) {{
        current121Lesson = lesson;
        document.querySelectorAll('.filter-121-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        apply121Filter();
    }}

    function onSearch121Change() {{
        apply121Filter();
    }}

    function apply121Filter() {{
        const q = (document.getElementById('search121Input')?.value || '').trim().toLowerCase();
        current121Filtered = VOCAB_121_DATA.filter(item => {{
            const matchLesson = (current121Lesson === 'ALL' || item.lesson == current121Lesson);
            const matchQuery = !q || item.kanji.toLowerCase().includes(q) || item.kana.toLowerCase().includes(q) || item.vi.toLowerCase().includes(q);
            return matchLesson && matchQuery;
        }});
        render121Table();
    }}

    function copyAll121Quizlet() {{
        const text = current121Filtered.map(item => `${{item.kanji}}\\t[${{item.kana}}] ${{item.vi}}`).join('\\n');
        navigator.clipboard.writeText(text).then(() => {{
            alert(`✅ Đã sao chép ${{current121Filtered.length}} từ chuẩn định dạng Tab cho Quizlet Pro!`);
        }});
    }}

    function copyAll121Colon() {{
        const text = current121Filtered.map(item => `${{item.kanji}}、${{item.vi}}: ${{item.kana}}`).join('\\n');
        navigator.clipboard.writeText(text).then(() => {{
            alert(`✅ Đã sao chép ${{current121Filtered.length}} từ định dạng: Từ、Nghĩa: Kana!`);
        }});
    }}
    '''

    # Inject into switchTab
    old_switch = '''        if (tabId === 'tab-exercises') {
            renderTypingExercise();
            generateQuiz();
        }'''
    new_switch = '''        if (tabId === 'tab-exercises') {
            renderTypingExercise();
            generateQuiz();
        } else if (tabId === 'tab-vocab-11-18') {
            render121Table();
        }'''
    if old_switch in html:
        html = html.replace(old_switch, new_switch, 1)
        print('✅ Hooked into switchTab!')

    # Append JS code before closing </script>
    if '</script>' in html:
        html = html.replace('</script>', js_code + '\n</script>', 1)
        print('✅ Injected JS logic for 121 Kanji compound vocab!')

    with open('kanji_a2.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('🎉 Successfully updated kanji_a2.html!')

if __name__ == '__main__':
    main()
