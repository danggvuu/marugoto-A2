import re
import json
import os
import glob

# Palette mapping by theme
PALETTES = {
    'food': ('#ef4444', '#b91c1c', '#7f1d1d'),
    'drink': ('#8b5cf6', '#6d28d9', '#4c1d95'),
    'vegetable': ('#10b981', '#047857', '#064e3b'),
    'meat': ('#f97316', '#c2410c', '#7c2d12'),
    'dessert': ('#ec4899', '#be185d', '#831843'),
    'travel': ('#0ea5e9', '#0284c7', '#0c4a6e'),
    'office': ('#6366f1', '#4338ca', '#1e1b4b'),
    'health': ('#14b8a6', '#0f766e', '#134e4a'),
    'culture': ('#dc2626', '#991b1b', '#450a0a'),
    'gold': ('#f59e0b', '#d97706', '#78350f'),
    'default': ('#4f46e5', '#3730a3', '#1e1b4b')
}

def get_color_palette(text):
    t = text.lower()
    if any(k in t for k in ['rượu', 'uống', 'drink', 'bia', 'trà', 'cà phê', 'nước']):
        return PALETTES['drink']
    if any(k in t for k in ['hoa quả', 'dâu', 'táo', 'trái cây', 'fruit']):
        return PALETTES['dessert']
    if any(k in t for k in ['rau', 'salad', 'vegetable', 'củ']):
        return PALETTES['vegetable']
    if any(k in t for k in ['thịt', 'gà', 'bò', 'heo', 'nướng', 'bbq', 'rán']):
        return PALETTES['meat']
    if any(k in t for k in ['món', 'ăn', 'cơm', 'bánh', 'mì', 'food', 'súp']):
        return PALETTES['food']
    if any(k in t for k in ['bay', 'tàu', 'xe', 'chuyến', 'travel', 'khách sạn', 'vé', 'sân bay']):
        return PALETTES['travel']
    if any(k in t for k in ['văn phòng', 'máy tính', 'điện thoại', 'tài liệu', 'công việc', 'họp', 'office']):
        return PALETTES['office']
    if any(k in t for k in ['khỏe', 'thuốc', 'chạy', 'thể dục', 'bệnh', 'nghỉ', 'health', 'tập']):
        return PALETTES['health']
    if any(k in t for k in ['lễ', 'hội', 'chúc', 'quà', 'đền', 'văn hóa', 'culture', 'tết']):
        return PALETTES['culture']
    return PALETTES['default']

def extract_emoji_and_title(item):
    svg = item.get('svg', '')
    em = '✨'
    title = item.get('badge') or item.get('vi', '').split(',')[0].strip() or 'TỪ VỰNG'
    
    # Try extract from existing svg
    m = re.search(r'>([^<]+)</text>\s*<text[^>]*>([^<]+)</text>', svg)
    if m:
        candidate_em = m.group(1).strip()
        candidate_title = m.group(2).strip()
        if candidate_em and len(candidate_em) <= 3:
            em = candidate_em
        if candidate_title:
            title = candidate_title
    else:
        # Fallback keyword emoji
        text = f"{item.get('jp','')} {item.get('vi','')} {item.get('badge','')}".lower()
        if 'quả' in text or 'trái cây' in text: em = '🍎'
        elif 'rượu' in text or 'uống' in text: em = '🍶'
        elif 'cơm' in text: em = '🍙'
        elif 'salad' in text or 'rau' in text: em = '🥗'
        elif 'bánh' in text or 'sandwich' in text: em = '🥪'
        elif 'thịt' in text or 'gà' in text: em = '🍗'
        elif 'dâu' in text: em = '🍓'
        elif 'trứng' in text: em = '🍳'
        elif 'mì' in text or 'ramen' in text: em = '🍜'
        elif 'máy bay' in text or 'bay' in text: em = '✈️'
        elif 'vali' in text or 'hành lý' in text: em = '🧳'
        elif 'tàu' in text: em = '🚄'
        elif 'khách sạn' in text: em = '🏨'
        elif 'máy tính' in text or 'laptop' in text: em = '💻'
        elif 'điện thoại' in text: em = '📱'
        elif 'tài liệu' in text or 'hồ sơ' in text: em = '📄'
        elif 'thuốc' in text: em = '💊'
        elif 'chạy' in text or 'thể thao' in text: em = '🏃'
        elif 'quà' in text: em = '🎁'
        elif 'đèn' in text: em = '🏮'
        elif 'lễ' in text or 'hội' in text: em = '👘'

    # Shorten title if too long
    if len(title) > 16:
        title = title[:15] + '…'
    return em, title.upper()

def generate_3d_isometric_svg(item, item_id):
    em, title = extract_emoji_and_title(item)
    kanji = item.get('kanji') or item.get('jp', '日本語')
    if len(kanji) > 6:
        kanji = kanji[:5]
    
    col1, col2, col3 = get_color_palette(f"{item.get('cat','')} {item.get('vi','')} {title}")

    clean_id = f"iso_{item_id}_{abs(hash(title)) % 100000}"

    return f'''<svg viewBox="0 0 240 135" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="top_g_{clean_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{col1}"/>
      <stop offset="100%" stop-color="{col2}"/>
    </linearGradient>
    <linearGradient id="side_g_{clean_id}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{col2}"/>
      <stop offset="100%" stop-color="{col3}"/>
    </linearGradient>
  </defs>
  <ellipse cx="120" cy="122" rx="75" ry="10" fill="rgba(15, 23, 42, 0.28)"/>
  <polygon points="50,88 120,114 120,124 50,98" fill="url(#side_g_{clean_id})"/>
  <polygon points="120,114 190,88 190,98 120,124" fill="{col3}"/>
  <polygon points="120,62 190,88 120,114 50,88" fill="url(#top_g_{clean_id})"/>
  <polygon points="120,64 186,88 120,112 54,88" fill="none" stroke="rgba(255,255,255,0.45)" stroke-width="1.5"/>
  <text x="120" y="93" text-anchor="middle" font-size="13" font-weight="900" fill="rgba(255,255,255,0.35)" font-family="sans-serif">{kanji}</text>
  <ellipse cx="120" cy="82" rx="22" ry="6" fill="rgba(0,0,0,0.28)"/>
  <g transform="translate(120, 48)">
    <circle cx="0" cy="0" r="25" fill="rgba(255,255,255,0.22)"/>
    <text x="0" y="11" text-anchor="middle" font-size="32">{em}</text>
  </g>
  <rect x="65" y="5" width="110" height="18" rx="9" fill="rgba(15, 23, 42, 0.75)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
  <text x="120" y="18" text-anchor="middle" fill="#ffffff" font-size="9.5" font-weight="800" letter-spacing="1">{title}</text>
</svg>'''

def update_lesson_3d(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Inject Head 3D Assets if missing
    assets_head = '''    <!-- 3D Model Studio & Interactive WebGL Engine -->
    <link rel="stylesheet" href="../assets/css/vocab-3d.css">
    <script src="../assets/js/vendor/three.min.js"></script>
    <script src="../assets/js/vendor/OrbitControls.js"></script>
    <script src="../assets/js/vocab-3d-engine.js" defer></script>
'''
    if 'vocab-3d.css' not in c:
        c = c.replace('</head>', f'{assets_head}</head>', 1)
        print(f"[{fn}] Injected 3D Head assets")

    # 2. Upgrade VOCAB_DATA with 3D Isometric SVGs
    m = re.search(r'const VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)
    if not m:
        m = re.search(r'var VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)
    if not m:
        m = re.search(r'let VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)

    if m:
        data = json.loads(m.group(1))
        for idx, item in enumerate(data):
            item['svg'] = generate_3d_isometric_svg(item, idx + 1)
        new_vocab_json = json.dumps(data, ensure_ascii=False)
        c = c[:m.start(1)] + new_vocab_json + c[m.end(1):]
        print(f"[{fn}] Upgraded {len(data)} vocabulary items with 3D Isometric SVGs")

    # 3. Update renderFlashcards to use fc-3d-stage
    # For lessons 11-18
    old_fc_pattern = re.compile(
        r'<div class="fc-illustration">\s*\$\{v\.svg\}\s*</div>',
        re.DOTALL
    )
    new_stage = '''<div class="fc-3d-stage" onclick="event.stopPropagation(); openVocab3D(VOCAB_DATA.indexOf(v))" title="Bấm để mở Mô Hình 3D 360° tương tác">
                                <div class="fc-3d-model-wrapper">
                                    <div class="fc-3d-floating-obj">
                                        ${v.svg}
                                    </div>
                                    <div class="fc-3d-shadow-blob"></div>
                                </div>
                                <div class="btn-launch-3d-badge">
                                    <span>🧊</span>
                                    <span>Mô hình 3D (360°)</span>
                                </div>
                            </div>'''
    if old_fc_pattern.search(c):
        c = old_fc_pattern.sub(new_stage, c)
        print(f"[{fn}] Replaced fc-illustration with fc-3d-stage")

    # For Lesson 10 which has ${v.svg || ''}
    old_fc_10 = re.compile(
        r'<div class="fc-illustration">\s*\$\{v\.svg\s*\|\|\s*\'\'\}\s*</div>',
        re.DOTALL
    )
    if old_fc_10.search(c):
        c = old_fc_10.sub(new_stage, c)
        print(f"[{fn}] Replaced fc-illustration with fc-3d-stage (L10 format)")

    # Ensure window.enhanceFlashcards3D is called after renderFlashcards
    if 'enhanceFlashcards3D' not in c:
        c = re.sub(
            r'(container\.innerHTML\s*=\s*filtered\.map\([^)]*\)\.join\(\'\'\);)',
            r'\1\n            if (window.enhanceFlashcards3D) window.enhanceFlashcards3D();',
            c
        )
        c = re.sub(
            r'(grid\.innerHTML\s*=\s*items\.map\([^)]*\)\.join\(\'\'\);)',
            r'\1\n            if (window.enhanceFlashcards3D) window.enhanceFlashcards3D();',
            c
        )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

def main():
    lessons = sorted(glob.glob('lessons/Marugoto_A2_Lesson_*.html'))
    for l in lessons:
        update_lesson_3d(l)
    print("Done upgrading all lessons with the 3D Interactive Model System!")

if __name__ == '__main__':
    main()
