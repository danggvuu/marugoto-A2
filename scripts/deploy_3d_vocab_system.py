import re
import json
import os
import glob

# Rich gradient palettes by semantic theme
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
    'nature': ('#059669', '#047857', '#064e3b'),
    'family': ('#ec4899', '#db2777', '#9d174d'),
    'default': ('#4f46e5', '#3730a3', '#1e1b4b')
}

def get_color_palette(text):
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
    if any(k in t for k in ['bay', 'tàu', 'xe', 'chuyến', 'travel', 'khách sạn', 'vé', 'sân bay', 'hành lý', 'vali', 'xuất phát', 'đến nơi', 'hạ cánh']):
        return PALETTES['travel']
    if any(k in t for k in ['văn phòng', 'máy tính', 'điện thoại', 'tài liệu', 'công việc', 'họp', 'office', 'báo cáo', 'fax', 'photo', 'giám đốc', 'thư ký', 'chi nhánh', 'trụ sở']):
        return PALETTES['office']
    if any(k in t for k in ['khỏe', 'thuốc', 'chạy', 'thể dục', 'bệnh', 'nghỉ', 'health', 'tập', 'đầu', 'bụng', 'chân', 'tai', 'mắt', 'mũi', 'miệng', 'răng', 'cảm', 'sốt', 'bơi', 'gym']):
        return PALETTES['health']
    if any(k in t for k in ['cưới', 'kết hôn', 'sinh', 'em bé', 'gia đình', 'mẹ', 'bố', 'quà', 'áo', 'váy', 'nhẫn', 'yêu']):
        return PALETTES['family']
    if any(k in t for k in ['lễ', 'hội', 'chúc', 'quà', 'đền', 'văn hóa', 'culture', 'tết', 'daruma', 'kimono', 'yukata', 'tập quán']):
        return PALETTES['culture']
    return PALETTES['default']

EMOJI_EXACT_MAP = {
    # Lesson 10
    '日本に 興味が あります': '🗾',
    '宿題を 手伝います': '🤝',
    '日本に 留学します': '🎓',
    '日本に 出張します': '💼',
    '通訳します': '🗣️',
    '翻訳します': '📖',
    '日本語を 教えます': '👨‍🏫',
    '日本語を 習います': '🧑‍🎓',
    '文化': '⛩️',
    '将来': '🚀',
    'ウェブサイト': '🌐',
    '言葉': '💬',
    '生活': '🏠',
    '歌': '🎵',
    '踊り': '💃',
    '観光客': '🧳',
    'どうしたんですか': '❓',
    '毎月': '📅',
    '毎年': '🎆',
    '～回': '🔢',
    '一週間 / 週': '📆',
    '一か月 / 月': '🌙',
    '一年 / 年': '🌟',
    'ガイド': '🚩',
    
    # Lesson 11
    'ポテトチップス': '🥔',
    'シート': '🧺',
    'ごみ袋': '🗑️',
    '皿': '🍽️',
    'フォーク': '🍴',
    'スプーン': '🥄',
    'ナイフ': '🔪',
    'コップ': '🥤',
    'はし': '🥢',
    '連絡します': '📞',
    '持って行きます': '🎒',
    '何でも': '👌',
    'どっちでも': '⚖️',
    '返事': '✉️',
    'バーベキュー': '🍖',
    'スープ': '🍲',
    '相談（します）': '👥',
    'Nについて': '💡',
    
    # Lesson 12
    '漬物': '🥒',
    'ピクルス': '🥒',
    '海老': '🦐',
    'ツナ': '🐟',
    '鮭': '🍣',
    '昆布': '🌿',
    'チーズ': '🧀',
    'マヨネーズ': '🍶',
    'チリ': '🌶️',
    '美味しい': '😋',
    '不味い': '😣',
    '甘い': '🍰',
    '辛い': '🌶️',
    '酸っぱい': '🍋',
    '塩っぱい': '🧂',
    '苦い': '☕',
    '気持ちがいい': '😌',
    '人気があります': '⭐',
    '違います': '❌',
    '似ています': '👥',
    'お腹がいっぱいです': '🤰',
    'お腹が空きました': '🤤',
    
    # Lesson 14
    'オフィス': '🏢',
    'コピー機': '📠',
    'ファックス': '📠',
    '国際電話': '🌐',
    '社長': '👔',
    '秘書': '💼',
    '事務スタッフ': '🧑‍💼',
    'ドライバー': '🚖',
    'ドア': '🚪',
    '窓': '🪟',
    '（ドアを）開けます': '🚪',
    '（ドアを）閉めます': '🔒',
    '勉強中': '📚',
    'ぺらぺら': '🗣️',
    '始めます': '▶️',
    'メモ': '📝',
    '事務所': '🏢',
    'プリントアウト': '🖨️',
    '紹介します': '🤝',
    '（パソコンが）こわれる': '💻',
    
    # Lesson 15
    '頭': '🧠',
    '顔': '😊',
    '目': '👁️',
    '鼻': '👃',
    '口': '👄',
    '歯': '🦷',
    '耳': '👂',
    '首': '🧣',
    'のど': '🗣️',
    '手': '✋',
    '指': '👆',
    'お腹': '🤰',
    '足': '🦵',
    '痛い': '😣',
    'マッサージ': '💆',
    'リラックス': '🧘',
    'エレベーター': '🛗',
    '眠い': '🥱',
    '熱があります': '🤒',
    '風邪（をひきます）': '🤧',
    '無理をします': '⚠️',
    'できるだけ': '🎯',
    
    # Lesson 16
    'ウォーキングをします': '🚶',
    '歩きます': '🚶‍♂️',
    'キロメートル': '📏',
    'キログラム': '⚖️',
    '泳ぎます': '🏊',
    '水泳をします': '🏊‍♂️',
    'プール': '🏊‍♀️',
    '体操をします': '🤸',
    'エアロビクスをします': '💃',
    'トレーニングをします': '🏋️',
    'ジム': '🏋️‍♂️',
    'ヨガをします': '🧘‍♀️',
    '健康にいい': '🥗',
    '体にいい': '💪',
    '健康に悪い': '🍔',
    '体に悪い': '🚬',
    '健康のために': '❤️',
    'リラックスをします': '☕',
    'アンケート': '📋',
    'ストレッチをします': '🧘',
    'トレーナー': '🏋️',
    '初めて': '🔰',
    'マシン': '⚙️',
    'ラウンジ': '🛋️',
    
    # Lesson 17
    '入学': '🎒',
    '卒業': '🎓',
    '就職': '💼',
    '出産': '👶',
    '赤ちゃん': '👶',
    '生まれます': '🍼',
    '結婚': '💒',
    'ネックレス': '📿',
    'セーター': '🧶',
    'おもちゃ': '🧸',
    '編み物': '🧶',
    '人形': '🎎',
    '（シャツを）着ます': '👔',
    '（シャツを）脱ぎます': '👕',
    '部屋に飾ります': '🖼️',
    '仕事で使います': '💼',
    '似合います': '👗',
    '遊びます': '🎮',
    '気に入ります': '💖',
    '～とか～とか': '📑',
    '母の日': '💐',
    '父の日': '👔',
    'クリスマス': '🎄',
    
    # Lesson 18
    '名刺入れ': '📇',
    'ペア': '👫',
    '同じ': '👯',
    '例えば': '💡',
    '習慣': '⛩️',
    '引っ越し': '📦',
    '喜びます': '🎉',
    '幸せ（な）': '🍀',
    '必要（な）': '🔑',
    'Nが必要です': '🔑',
    '赤ちゃんの物が必要です': '🍼',
    'カードを書きます': '💌',
    'お礼を言います': '🙏',
    '写真立て': '🖼️',
    '花瓶': '🏺',
    '指輪': '💍',
    'きっと': '🤞',
    'スーツ': '🤵',
    '大切（な）': '💎',
    '大切にします': '💝'
}

def clean_kanji_pedestal(kanji_str):
    if not kanji_str:
        return '日本語'
    # Strip parentheses with content
    clean = re.sub(r'^[（\(][^）\)]*[）\)]', '', kanji_str).strip()
    clean = re.sub(r'[（\(][^）\)]*[）\)]$', '', clean).strip()
    clean = re.sub(r'[（\(\)）]', '', clean).strip()
    if not clean:
        clean = kanji_str
    if len(clean) > 8:
        clean = clean[:7] + '…'
    return clean

def extract_emoji_and_title(item):
    jp = item.get('jp', '').strip()
    kanji = item.get('kanji', '').strip()
    badge = item.get('badge', '').strip()
    vi = item.get('vi', '').strip()

    # 1. Exact map check
    for key in [kanji, jp, kanji.replace(' ', ''), jp.replace(' ', '')]:
        if key in EMOJI_EXACT_MAP:
            em = EMOJI_EXACT_MAP[key]
            title = badge or vi.split(',')[0].strip() or 'TỪ VỰNG'
            title = re.sub(r'^[\U00010000-\U0010ffff\u2600-\u27bf\ud83c-\ud83e\ud83d-\ud83d\s]+', '', title).strip()
            if len(title) > 16: title = title[:15] + '…'
            return em, title.upper()

    # 2. Badge leading emoji
    m_badge = re.match(r'^([\U00010000-\U0010ffff\u2600-\u27bf\ud83c-\ud83e\ud83d-\ud83d][\ufe0f\u200d\U00010000-\U0010ffff\ud83c-\ud83e]*)\s*(.*)', badge)
    if m_badge:
        em = m_badge.group(1).strip()
        rem_badge = m_badge.group(2).strip()
        title = rem_badge or vi.split(',')[0].strip() or 'TỪ VỰNG'
        if len(title) > 16: title = title[:15] + '…'
        return em, title.upper()

    # 3. Existing non-sparkle svg
    svg = item.get('svg', '')
    m_svg = re.search(r'>([^<]+)</text>\s*<text[^>]*>([^<]+)</text>', svg)
    if m_svg:
        candidate_em = m_svg.group(1).strip()
        candidate_title = m_svg.group(2).strip()
        if candidate_em and candidate_em != '✨' and len(candidate_em) <= 3:
            return candidate_em, candidate_title.upper()

    title = badge or vi.split(',')[0].strip() or 'TỪ VỰNG'
    if len(title) > 16: title = title[:15] + '…'
    return '🌟', title.upper()

def generate_3d_isometric_svg(item, item_id):
    em, title = extract_emoji_and_title(item)
    kanji = clean_kanji_pedestal(item.get('kanji') or item.get('jp', '日本語'))
    
    col1, col2, col3 = get_color_palette(f"{item.get('cat','')} {item.get('vi','')} {title} {kanji}")
    clean_id = f"iso_{item_id}_{abs(hash(title + kanji)) % 100000}"

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
  <text x="120" y="91" text-anchor="middle" font-size="13" font-weight="900" fill="rgba(255,255,255,0.55)" font-family="sans-serif">{kanji}</text>
  <ellipse cx="120" cy="80" rx="20" ry="5" fill="rgba(0,0,0,0.35)"/>
  <g transform="translate(120, 46)">
    <circle cx="0" cy="0" r="24" fill="rgba(255,255,255,0.25)"/>
    <text x="0" y="11" text-anchor="middle" font-size="32">{em}</text>
  </g>
  <rect x="50" y="8" width="140" height="18" rx="9" fill="rgba(0, 0, 0, 0.35)" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
  <text x="120" y="21" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="800" letter-spacing="1">{title}</text>
</svg>'''

def update_lesson(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Find VOCAB_DATA
    m = re.search(r'const VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)
    if not m:
        m = re.search(r'var VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)
    if not m:
        m = re.search(r'let VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)

    if not m:
        print(f"Skipping {fn}: no VOCAB_DATA found")
        return

    data = json.loads(m.group(1))
    
    # Standardize Suru-verbs across all lessons if needed
    for idx, item in enumerate(data):
        kanji = item.get('kanji', '')
        jp = item.get('jp', '')
        vi = item.get('vi', '')
        badge = item.get('badge', '')
        
        # Check if item is a Suru-verb (Danh động từ)
        if any(w in kanji or w in jp for w in ['（します）', 'します', '（をひきます）']):
            # If badge was generic 'Động từ', clarify it
            if badge in ['Động từ', 'Cụm từ']:
                if '（します）' in kanji or 'します' in kanji:
                    item['badge'] = 'Danh động từ (N・V3)'
                    if not vi.startswith('(N)'):
                        item['vi'] = f"(N) {vi} • (V) {vi} (します)"

        item['svg'] = generate_3d_isometric_svg(item, idx + 1)

    new_vocab_json = json.dumps(data, ensure_ascii=False)
    c = c[:m.start(1)] + new_vocab_json + c[m.end(1):]

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Updated {fn}: {len(data)} items processed.")

def main():
    lessons = sorted(glob.glob('lessons/Marugoto_A2_Lesson_*.html'))
    for l in lessons:
        update_lesson(l)

if __name__ == '__main__':
    main()
