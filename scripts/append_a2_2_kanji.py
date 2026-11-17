# -*- coding: utf-8 -*-
"""
Append A2-2 Lesson 1 and Lesson 2 Kanji compound words to assets/data/kanji_a2_data.js
and update kanji_a2.html filter buttons.
"""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# 31 items
A2_2_KANJI_ITEMS = [
    # Lesson 1 (15 items)
    {"lesson": "A2-2 L1", "kanji": "紹介", "kana": "しょうかい", "vi": "Giới thiệu", "group": "Giao tiếp"},
    {"lesson": "A2-2 L1", "kanji": "自己紹介", "kana": "じこしょうかい", "vi": "Giới thiệu bản thân", "group": "Giao tiếp"},
    {"lesson": "A2-2 L1", "kanji": "名前", "kana": "なまえ", "vi": "Tên", "group": "Danh xưng"},
    {"lesson": "A2-2 L1", "kanji": "有名", "kana": "ゆうめい", "vi": "Nổi tiếng", "group": "Tính chất"},
    {"lesson": "A2-2 L1", "kanji": "意味", "kana": "いみ", "vi": "Ý nghĩa", "group": "Tư duy"},
    {"lesson": "A2-2 L1", "kanji": "部屋", "kana": "へや", "vi": "Căn phòng", "group": "Nơi ở"},
    {"lesson": "A2-2 L1", "kanji": "本屋", "kana": "ほんや", "vi": "Tiệm sách", "group": "Địa điểm"},
    {"lesson": "A2-2 L1", "kanji": "近い", "kana": "ちかい", "vi": "Gần", "group": "Vị trí"},
    {"lesson": "A2-2 L1", "kanji": "最近", "kana": "さいきん", "vi": "Gần đây", "group": "Thời gian"},
    {"lesson": "A2-2 L1", "kanji": "近所", "kana": "きんじょ", "vi": "Hàng xóm, lân cận", "group": "Đời sống"},
    {"lesson": "A2-2 L1", "kanji": "住みます", "kana": "すみます", "vi": "Sống", "group": "Đời sống"},
    {"lesson": "A2-2 L1", "kanji": "住所", "kana": "じゅうしょ", "vi": "Địa chỉ", "group": "Thông tin"},
    {"lesson": "A2-2 L1", "kanji": "働きます", "kana": "はたらきます", "vi": "Làm việc", "group": "Công việc"},
    {"lesson": "A2-2 L1", "kanji": "一番", "kana": "いちばん", "vi": "Nhất, số một", "group": "Số lượng"},
    {"lesson": "A2-2 L1", "kanji": "一番目", "kana": "いちばんめ", "vi": "Thứ nhất", "group": "Số lượng"},
    # Lesson 2 (16 items)
    {"lesson": "A2-2 L2", "kanji": "兄", "kana": "あに", "vi": "Anh trai mình", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "お兄さん", "kana": "おにいさん", "vi": "Anh trai (người khác)", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "姉", "kana": "あね", "vi": "Chị gái mình", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "お姉さん", "kana": "おねえさん", "vi": "Chị gái (người khác)", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "弟", "kana": "おとうと", "vi": "Em trai", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "兄弟", "kana": "きょうだい", "vi": "Anh em", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "妹", "kana": "いもうと", "vi": "Em gái", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "姉妹", "kana": "しまい", "vi": "Chị em", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "家族", "kana": "かぞく", "vi": "Gia đình", "group": "Gia đình"},
    {"lesson": "A2-2 L2", "kanji": "水族館", "kana": "すいぞくかん", "vi": "Thủy cung", "group": "Địa điểm"},
    {"lesson": "A2-2 L2", "kanji": "長い", "kana": "ながい", "vi": "Dài", "group": "Tính chất"},
    {"lesson": "A2-2 L2", "kanji": "成長", "kana": "せいちょう", "vi": "Trưởng thành, phát triển", "group": "Trạng thái"},
    {"lesson": "A2-2 L2", "kanji": "短い", "kana": "みじかい", "vi": "Ngắn", "group": "Tính chất"},
    {"lesson": "A2-2 L2", "kanji": "低い", "kana": "ひくい", "vi": "Thấp", "group": "Tính chất"},
    {"lesson": "A2-2 L2", "kanji": "歌", "kana": "うた", "vi": "Bài hát", "group": "Nghệ thuật"},
    {"lesson": "A2-2 L2", "kanji": "歌手", "kana": "かしゅ", "vi": "Ca sĩ", "group": "Nghề nghiệp"}
]

def update_kanji_data_js():
    js_path = ROOT / "assets/data/kanji_a2_data.js"
    content = js_path.read_text(encoding="utf-8")
    
    match = re.search(r"var VOCAB_121_DATA = (\[.*?\]);", content)
    if not match:
        raise ValueError("Could not find VOCAB_121_DATA in kanji_a2_data.js")
    
    current_data = json.loads(match.group(1))
    
    # Filter out any existing A2-2 items to avoid duplicate if rerun
    cleaned_data = [item for item in current_data if not str(item.get("lesson", "")).startswith("A2-2")]
    
    # Read the generated source rather than maintaining a second copy of words.
    source = json.loads((ROOT / "data/kanji_vocab_a2_2.json").read_text(encoding="utf-8"))
    groups = {(item["lesson"], item["kanji"]): item["group"] for item in A2_2_KANJI_ITEMS}
    new_items = []
    for lesson in (1, 2):
        label = f"A2-2 L{lesson}"
        for item in source[f"lesson_{lesson}"]:
            new_items.append({
                "lesson": label, "kanji": item["word"], "kana": item["kana"],
                "vi": item["mean"], "group": groups.get((label, item["word"]), "Từ vựng"),
            })
    total_data = cleaned_data + new_items
    
    new_declaration = f"var VOCAB_121_DATA = {json.dumps(total_data, ensure_ascii=False)};"
    updated_content = content[:match.start()] + new_declaration + content[match.end():]
    js_path.write_text(updated_content, encoding="utf-8")
    print(f"Updated {js_path} with total {len(total_data)} items (121 original + 31 A2-2)!")

def update_kanji_html():
    html_path = ROOT / "kanji_a2.html"
    content = html_path.read_text(encoding="utf-8")
    
    old_buttons = '''            <!-- Filter by Lesson Bar -->
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;">
                <button type="button" class="filter-121-btn active" onclick="filter121Vocab('ALL', this)">🌟 Tất Cả (121)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(11, this)">Bài 11 (15)</button>'''
                
    new_buttons = '''            <!-- Filter by Lesson Bar -->
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;">
                <button type="button" class="filter-121-btn active" onclick="filter121Vocab('ALL', this)">🌟 Tất Cả (152)</button>
                <button type="button" class="filter-121-btn" style="background: #eef2ff; color: #4338ca; border-color: #818cf8; font-weight: 700;" onclick="filter121Vocab('A2-2 L1', this)">🌸 A2-2 Bài 1 (15)</button>
                <button type="button" class="filter-121-btn" style="background: #fdf2f8; color: #be185d; border-color: #f472b6; font-weight: 700;" onclick="filter121Vocab('A2-2 L2', this)">👓 A2-2 Bài 2 (16)</button>
                <button type="button" class="filter-121-btn" onclick="filter121Vocab(11, this)">Bài 11 (15)</button>'''

    if old_buttons in content:
        content = content.replace(old_buttons, new_buttons)
        html_path.write_text(content, encoding="utf-8")
        print(f"Updated {html_path} with A2-2 filter buttons!")
    else:
        print("Buttons already updated or pattern not found in kanji_a2.html")

if __name__ == "__main__":
    update_kanji_data_js()
    update_kanji_html()
