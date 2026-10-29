import subprocess
import json
import re
import glob

PALETTES = {
    'food': ('#ef4444', '#b91c1c'),
    'drink': ('#8b5cf6', '#6d28d9'),
    'vegetable': ('#10b981', '#047857'),
    'meat': ('#f97316', '#c2410c'),
    'dessert': ('#ec4899', '#be185d'),
    'travel': ('#0ea5e9', '#0284c7'),
    'office': ('#6366f1', '#4338ca'),
    'health': ('#14b8a6', '#0f766e'),
    'culture': ('#dc2626', '#991b1b'),
    'gold': ('#f59e0b', '#d97706'),
    'nature': ('#059669', '#047857'),
    'family': ('#ec4899', '#db2777'),
    'blue': ('#3b82f6', '#1d4ed8'),
    'default': ('#4f46e5', '#3730a3')
}

def get_color(text):
    t = text.lower()
    if any(k in t for k in ['rượu', 'uống', 'drink', 'bia', 'trà', 'cà phê', 'nước', 'đồ uống', 'cốc', 'ly']):
        return PALETTES['drink']
    if any(k in t for k in ['hoa quả', 'dâu', 'táo', 'trái cây', 'fruit', 'ngọt', 'bánh', 'kem']):
        return PALETTES['dessert']
    if any(k in t for k in ['rau', 'salad', 'vegetable', 'củ', 'dưa chua', 'muối chua', 'tảo']):
        return PALETTES['vegetable']
    if any(k in t for k in ['thịt', 'gà', 'bò', 'heo', 'nướng', 'bbq', 'rán', 'meat', 'tôm', 'cá']):
        return PALETTES['meat']
    if any(k in t for k in ['món', 'ăn', 'cơm', 'đĩa', 'thìa', 'muỗng', 'dĩa', 'nĩa', 'dao', 'đũa', 'súp', 'trứng', 'ngon']):
        return PALETTES['food']
    if any(k in t for k in ['bay', 'chuyến', 'travel', 'khách sạn', 'vé', 'sân bay', 'hành lý', 'vali', 'xuất phát', 'đến nơi', 'hạ cánh', 'đón', 'tiễn']):
        return PALETTES['travel']
    if any(k in t for k in ['văn phòng', 'máy tính', 'điện thoại', 'tài liệu', 'công việc', 'họp', 'office', 'báo cáo', 'fax', 'photo', 'giám đốc', 'thư ký', 'chi nhánh', 'trụ sở']):
        return PALETTES['office']
    if any(k in t for k in ['khỏe', 'thuốc', 'chạy', 'thể dục', 'bệnh', 'nghỉ', 'health', 'tập', 'đầu', 'bụng', 'chân', 'tai', 'mắt', 'mũi', 'miệng', 'răng', 'cảm', 'sốt', 'bơi', 'gym']):
        return PALETTES['health']
    if any(k in t for k in ['cưới', 'kết hôn', 'sinh', 'em bé', 'gia đình', 'mẹ', 'bố', 'quà', 'áo', 'váy', 'nhẫn']):
        return PALETTES['family']
    if any(k in t for k in ['lễ', 'hội', 'chúc', 'quà', 'đền', 'văn hóa', 'culture', 'tết', 'daruma', 'kimono', 'yukata', 'tập quán']):
        return PALETTES['culture']
    return PALETTES['default']

def clean_pedestal_kanji(kanji_str):
    if not kanji_str:
        return '日本語'
    clean = re.sub(r'^[～~]', '', kanji_str)
    clean = re.sub(r'^[（\(][^）\)]*[）\)]', '', clean).strip()
    clean = re.sub(r'[（\(][^）\)]*[）\)]$', '', clean).strip()
    clean = re.sub(r'[（\(\)）]', '', clean).strip()
    # Clean phrases
    if 'フライト' in clean: return 'フライト'
    if '便' in clean: return '便'
    if 'お湯' in clean: return 'お湯'
    if 'スケジュール' in clean: return '予定'
    if 'チェック' in clean: return '点検'
    if 'ようこそ' in clean: return '歓迎'
    if 'お疲れ様' in clean: return '労い'
    if 'お待たせ' in clean: return '待機'
    if 'いかが' in clean: return '勧奨'
    if '送りに行きます' in clean: return '見送り'
    if '迎えに行きます' in clean: return '出迎え'
    if '送ります' in clean: return '送る'
    if '貰います' in clean: return '貰う'
    if '空きます' in clean: return '空く'
    if '混みます' in clean: return '混む'
    if len(clean) > 6:
        clean = clean[:5]
    return clean

FALLBACK_RESOLVE = {
    '一年 / 年': '🗓️',
    '何でも': '👌',
    '人気があります': '🔥',
    '初めて': '🔰',
    '似合います': '👗',
    'きっと': '🤞'
}

def make_3d_svg(item_id, pedestal_kanji, emoji, title, col1, col2):
    clean_id = f"iso_{item_id}_{abs(hash(title + pedestal_kanji)) % 100000}"
    return f'''<svg viewBox="0 0 240 135" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg_g_{clean_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{col1}"/>
      <stop offset="100%" stop-color="{col2}"/>
    </linearGradient>
    <linearGradient id="ped_top_{clean_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.4)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0.12)"/>
    </linearGradient>
  </defs>
  <rect width="240" height="135" rx="14" fill="url(#bg_g_{clean_id})"/>
  <circle cx="120" cy="72" r="50" fill="rgba(255,255,255,0.08)"/>
  <ellipse cx="120" cy="116" rx="60" ry="8" fill="rgba(0, 0, 0, 0.3)"/>
  <polygon points="55,88 120,110 120,118 55,96" fill="rgba(0,0,0,0.35)"/>
  <polygon points="120,110 185,88 185,96 120,118" fill="rgba(0,0,0,0.5)"/>
  <polygon points="120,66 185,88 120,110 55,88" fill="url(#ped_top_{clean_id})"/>
  <polygon points="120,68 181,88 120,108 59,88" fill="none" stroke="rgba(255,255,255,0.55)" stroke-width="1.2"/>
  <text x="120" y="91" text-anchor="middle" font-size="13" font-weight="900" fill="rgba(255,255,255,0.65)" font-family="sans-serif">{pedestal_kanji}</text>
  <ellipse cx="120" cy="80" rx="20" ry="5" fill="rgba(0,0,0,0.35)"/>
  <g transform="translate(120, 46)">
    <circle cx="0" cy="0" r="24" fill="rgba(255,255,255,0.25)"/>
    <text x="0" y="11" text-anchor="middle" font-size="32">{emoji}</text>
  </g>
  <rect x="45" y="8" width="150" height="18" rx="9" fill="rgba(0, 0, 0, 0.35)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
  <text x="120" y="21" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="800" letter-spacing="1">{title}</text>
</svg>'''

def process_all_lessons():
    for lesson in range(10, 19):
        # 1. Get original data from git
        cmd = ['git', 'show', f'f391a3a~1:lessons/Marugoto_A2_Lesson_{lesson}.html']
        out = subprocess.run(cmd, capture_output=True, text=True).stdout
        m_orig = re.search(r'const VOCAB_DATA\s*=\s*(\[.*?\]);', out, flags=re.DOTALL)
        if not m_orig:
            m_orig = re.search(r'var VOCAB_DATA\s*=\s*(\[.*?\]);', out, flags=re.DOTALL)
        orig_data = json.loads(m_orig.group(1))

        orig_map = {}
        for it in orig_data:
            s = it.get('svg', '')
            m_em = re.search(r'font-size=\"34\">([^<]+)</text>', s)
            if not m_em:
                m_em = re.search(r'>([\U00010000-\U0010ffff\u2600-\u27bf\ud83c-\ud83e\ud83d-\ud83d][\ufe0f\u200d\U00010000-\U0010ffff\ud83c-\ud83e]*)<', s)
            em = m_em.group(1) if m_em else None
            
            # Badge leading emoji fallback
            if not em or em in ['✨', '🌟', '⭐']:
                badge = it.get('badge', '')
                m_b = re.search(r'([\U00010000-\U0010ffff\u2600-\u27bf\ud83c-\ud83e\ud83d-\ud83d][\ufe0f\u200d\U00010000-\U0010ffff\ud83c-\ud83e]*)', badge)
                if m_b:
                    em = m_b.group(1)

            # Fallback dict
            kanji_key = it.get('kanji') or it.get('jp')
            if kanji_key in FALLBACK_RESOLVE:
                em = FALLBACK_RESOLVE[kanji_key]

            # Title extraction
            m_t = re.findall(r'>([^<]+)</text>', s)
            title = 'TỪ VỰNG'
            if len(m_t) > 1:
                title = m_t[1]
            elif it.get('badge'):
                title = it.get('badge')
            else:
                title = it.get('vi', '').split(',')[0].strip()
            
            # Clean title
            title = re.sub(r'[\U00010000-\U0010ffff\u2600-\u27bf\ud83c-\ud83e\ud83d-\ud83d\ufe0f\u200d]', '', title).strip().upper()
            if len(title) > 16:
                title = title[:15] + '…'
            
            orig_map[it['id']] = (em or '🌟', title)

        # 2. Update current lesson file
        curr_fn = f'lessons/Marugoto_A2_Lesson_{lesson}.html'
        with open(curr_fn, 'r', encoding='utf-8') as f:
            c = f.read()

        m_curr = re.search(r'const VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)
        if not m_curr:
            m_curr = re.search(r'var VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)

        curr_data = json.loads(m_curr.group(1))
        for it in curr_data:
            item_id = it['id']
            emoji, title = orig_map.get(item_id, ('🌟', 'TỪ VỰNG'))
            
            # Guarantee no star unless truly intentional
            kanji_key = it.get('kanji') or it.get('jp')
            if emoji in ['✨', '🌟', '⭐'] and kanji_key in FALLBACK_RESOLVE:
                emoji = FALLBACK_RESOLVE[kanji_key]

            pedestal_kanji = clean_pedestal_kanji(it.get('kanji') or it.get('jp'))
            col1, col2 = get_color(f"{it.get('cat','')} {it.get('vi','')} {title}")
            
            it['svg'] = make_3d_svg(item_id, pedestal_kanji, emoji, title, col1, col2)

        new_json = json.dumps(curr_data, ensure_ascii=False)
        c = c[:m_curr.start(1)] + new_json + c[m_curr.end(1):]

        with open(curr_fn, 'w', encoding='utf-8') as f:
            f.write(c)

        print(f"Restored Lesson {lesson}: {len(curr_data)} items.")

if __name__ == '__main__':
    process_all_lessons()
