import re
import os
import glob

def fix_css_mismatched_braces():
    # Lessons 12-18 have orphan:
    #             padding: 16px;
    #             text-align: center;
    #             transition: all 0.25s;
    #         }
    orphan_block = re.compile(
        r'(\.morph-val\s*\{[^}]*\}\s*)\n\s*padding:\s*16px;\s*\n\s*text-align:\s*center;\s*\n\s*transition:\s*all\s*0\.25s;\s*\n\s*\}\s*\n',
        re.MULTILINE
    )
    for fn in glob.glob('lessons/Marugoto_A2_Lesson_*.html'):
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        if orphan_block.search(c):
            c = orphan_block.sub(r'\1\n', c)
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"[CSS Fix] Removed orphan CSS block in {fn}")

def fix_duplicate_vocab_stats():
    # In lessons 12-18:
    # <div class="vocab-filter-bar" id="vocabFilterBar">
    #     <!-- Filters rendered via JS -->
    #     <div class="vocab-stats-badge" id="vocabStats">Đã thuộc: 0 / 31 từ</div>
    # </div>
    pattern = re.compile(
        r'(<div class="vocab-filter-bar" id="vocabFilterBar">\s*<!-- Filters rendered via JS -->)\s*<div class="vocab-stats-badge" id="vocabStats">[^<]*</div>',
        re.DOTALL
    )
    for fn in glob.glob('lessons/Marugoto_A2_Lesson_*.html'):
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        if pattern.search(c):
            c = pattern.sub(r'\1', c)
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"[DOM Fix] Removed static duplicate vocabStats in {fn}")

def fix_de_thi_thu_container():
    fn = 'tests/De_Thi_Thu_Marugoto_A2_5_8.html'
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Find after global-hub-nav and before code-selector-card
    target = '<!-- Exam Code Selector Card -->'
    if '<div class="container">' not in c and target in c:
        hero_markup = '''    <div class="container">
        <!-- Hero Banner -->
        <div class="hero-banner">
            <span class="hero-badge">MARUGOTO A2-1 • TIÊU CHUẨN JF</span>
            <h1>📝 BỘ 5 ĐỀ THI THỬ TOÀN DIỆN (BÀI 5 - 8)</h1>
            <p style="color: rgba(255, 255, 255, 0.85); font-size: 0.95rem; margin-top: 6px;">Luyện thi cấp tốc các mã đề 101, 102, 103, 104, 105 với đồng hồ đếm ngược 40 phút, tự động lưu tiến trình, chấm điểm chuẩn xác và lời giải chi tiết.</p>
        </div>

        '''
        c = c.replace(target, hero_markup + target, 1)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"[Layout Fix] Restored <div class=\"container\"> and Hero Banner in {fn}")

def fix_css_variables():
    # 1. Tu_Vung_Marugoto_A1_16_A2_1_10.html -> add --secondary
    tv_fn = 'Tu_Vung_Marugoto_A1_16_A2_1_10.html'
    with open(tv_fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if '--secondary:' not in c and '--primary-light:' in c:
        c = c.replace('--primary-light: #a29bfe;', '--primary-light: #a29bfe;\n            --secondary: #a29bfe;', 1)
        with open(tv_fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"[CSS Var Fix] Added --secondary to {tv_fn}")

    # 2. tests/De_Thi_Thu_Marugoto_A2_5_8.html -> add --gray-400
    dtt_fn = 'tests/De_Thi_Thu_Marugoto_A2_5_8.html'
    with open(dtt_fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if '--gray-400:' not in c and '--gray-300: #cbd5e1;' in c:
        c = c.replace('--gray-300: #cbd5e1;', '--gray-300: #cbd5e1;\n            --gray-400: #94a3b8;', 1)
        with open(dtt_fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"[CSS Var Fix] Added --gray-400 to {dtt_fn}")

    # 3. tests/On_Tap_Mini_Test_A2_1_4.html & tests/On_Tap_Mini_Test_A2_5_8.html -> add --gray-300
    for ot_fn in ['tests/On_Tap_Mini_Test_A2_1_4.html', 'tests/On_Tap_Mini_Test_A2_5_8.html']:
        with open(ot_fn, 'r', encoding='utf-8') as f:
            c = f.read()
        if '--gray-300:' not in c and '--gray-400: #94a3b8;' in c:
            c = c.replace('--gray-400: #94a3b8;', '--gray-400: #94a3b8;\n            --gray-300: #cbd5e1;', 1)
            with open(ot_fn, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"[CSS Var Fix] Added --gray-300 to {ot_fn}")

def fix_confetti_lesson_10():
    fn = 'lessons/Marugoto_A2_Lesson_10.html'
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    old_confetti = "const canvas = document.getElementById('confettiCanvas');\n            const ctx = canvas.getContext('2d');"
    safe_confetti = """let canvas = document.getElementById('confettiCanvas');
            if (!canvas) {
                canvas = document.createElement('canvas');
                canvas.id = 'confettiCanvas';
                document.body.appendChild(canvas);
            }
            const ctx = canvas.getContext('2d');"""
    if old_confetti in c:
        c = c.replace(old_confetti, safe_confetti, 1)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"[JS Fix] Safe confetti canvas injection in {fn}")

def clean_dead_dock_functions():
    # Remove toggleGlobalMegaSheet, closeGlobalMegaSheet, toggleGlobalToolsDropdown across all files
    dead_code_regex = re.compile(
        r'// Global Navigation Dropdowns\s*function toggleGlobalMegaSheet\([^)]*\)\s*\{[^}]*\}\s*'
        r'function closeGlobalMegaSheet\([^)]*\)\s*\{[^}]*\}\s*'
        r'function toggleGlobalToolsDropdown\([^)]*\)\s*\{[^}]*\}\s*'
        r'document\.addEventListener\(\'click\',\s*\(e\)\s*=>\s*\{[^}]*globalToolsMenu[^}]*\}\);',
        re.DOTALL
    )
    # Also individual functions
    func_regexes = [
        re.compile(r'function toggleGlobalMegaSheet\([^)]*\)\s*\{[^}]*\}'),
        re.compile(r'function closeGlobalMegaSheet\([^)]*\)\s*\{[^}]*\}'),
        re.compile(r'function toggleGlobalToolsDropdown\([^)]*\)\s*\{[^}]*\}'),
        re.compile(r'document\.addEventListener\(\'click\',\s*\(e\)\s*=>\s*\{[^}]*globalToolsMenu[^}]*\}\);')
    ]
    all_files = sorted(glob.glob('*.html')) + sorted(glob.glob('lessons/*.html')) + sorted(glob.glob('tests/*.html'))
    for fn in all_files:
        if 'mockup' in fn: continue
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        orig = c
        c = dead_code_regex.sub('', c)
        for r in func_regexes:
            c = r.sub('', c)
        if c != orig:
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"[Cleanup] Removed dead floating dock functions in {fn}")

if __name__ == '__main__':
    fix_css_mismatched_braces()
    fix_duplicate_vocab_stats()
    fix_de_thi_thu_container()
    fix_css_variables()
    fix_confetti_lesson_10()
    clean_dead_dock_functions()
    print("All frontend fixes applied!")
