# -*- coding: utf-8 -*-
"""
Sync all 18 A2-2 lessons' Kanji compound words to assets/data/kanji_a2_data.js
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
    groups.update({(item["lesson"], item["kanji"]): item["group"]
                   for item in current_data if item.get("group")})
    new_items = []
    # Require the complete source before replacing anything in the runtime file.
    for lesson in range(1, 19):
        label = f"A2-2 L{lesson}"
        for item in source[f"lesson_{lesson}"]:
            new_items.append({
                "lesson": label, "kanji": item["word"], "kana": item["kana"],
                "vi": item["mean"], "group": groups.get((label, item["word"]), "A2-2 Trọng tâm"),
            })
    total_data = cleaned_data + new_items
    
    new_declaration = f"var VOCAB_121_DATA = {json.dumps(total_data, ensure_ascii=False)};"
    updated_content = content[:match.start()] + new_declaration + content[match.end():]
    js_path.write_text(updated_content, encoding="utf-8")
    print(f"Updated {js_path} with {len(total_data)} items ({len(new_items)} A2-2, all 18 lessons)!")

def update_kanji_html():
    html_path = ROOT / "kanji_a2.html"
    content = html_path.read_text(encoding="utf-8")
    
    source = json.loads((ROOT / "data/kanji_vocab_a2_2.json").read_text(encoding="utf-8"))
    counts = {lesson: len(source[f"lesson_{lesson}"]) for lesson in range(1, 19)}
    runtime = (ROOT / "assets/data/kanji_a2_data.js").read_text(encoding="utf-8")
    items = json.loads(re.search(r"var VOCAB_121_DATA = (\[.*?\]);", runtime)[1])
    total_count = len(items)
    a2_2_count = sum(counts.values())
    content = re.sub(r">🎴 \d+ Mục Từ Kanji · A2-1 &amp; A2-2<",
                     f">🎴 {total_count} Mục Từ Kanji · A2-1 &amp; A2-2<", content)
    content = re.sub(r"\d+ mục (?:Kanji )?A2-2 bài \d+–\d+\.",
                     f"{a2_2_count} mục Kanji A2-2 bài 1–18.", content)
    content = re.sub(r"Tất Cả \(\d+\)", f"Tất Cả ({total_count})", content)
    content = re.sub(r"Trọn Bộ A2-2 \(\d+\)", f"Trọn Bộ A2-2 ({a2_2_count})", content)
    for lesson, count in counts.items():
        pattern = rf"(onclick=\"filter121Vocab\('A2-2 L{lesson}', this\)\">Bài {lesson} )\(\d+\)"
        content = re.sub(pattern, lambda match: match[1] + f"({count})", content)
    html_path.write_text(content, encoding="utf-8")
    print(f"Updated {html_path} with counts for all 18 A2-2 lessons!")

if __name__ == "__main__":
    update_kanji_data_js()
    update_kanji_html()
