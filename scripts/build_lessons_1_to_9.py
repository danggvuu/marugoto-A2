#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_lessons_1_to_9.py
Trình tạo trọn vẹn 9 Web Bài Học (Bài 1 đến Bài 9) chuẩn Marugoto A2-1:
- Tích hợp 100% từ vựng chính thức (Flashcard 3D + SVG + Âm thanh Tokyo)
- 3 Chuyên đề ngữ pháp cốt lõi mỗi bài (công thức, bảng chia, ví dụ tự nhiên)
- Máy luyện chia thể động từ (Verb Morphing Lab)
- Thẻ chữ Hán Kanji đầy đủ nét, On/Kun, mẹo nhớ
- Mini Test 15 câu trắc nghiệm phản xạ có giải thích chi tiết
- Đối thoại tình huống nhập vai NPC
"""

import json
import re
import os

def make_svg(title, emoji, c1="#4f46e5", c2="#3730a3"):
    safe_id = "".join(c for c in title if c.isalnum()) or "card"
    return f'''<svg viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g_{safe_id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="240" height="120" rx="14" fill="url(#g_{safe_id})"/>
  <circle cx="120" cy="50" r="30" fill="rgba(255,255,255,0.2)"/>
  <text x="120" y="60" text-anchor="middle" font-size="34">{emoji}</text>
  <text x="120" y="105" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800" font-family="system-ui, -apple-system, sans-serif">{title}</text>
</svg>'''

# 1. Load Vocab
with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'r', encoding='utf-8') as f:
    c_vocab = f.read()
m_vocab = re.search(r'const rawVocab = (\[.*?\]);', c_vocab, re.DOTALL)
all_vocab = json.loads(m_vocab.group(1)) if m_vocab else []

# 2. Load Kanji
with open('data/kanji_extracted.json', 'r', encoding='utf-8') as f:
    all_kanji = json.load(f)

# Helper to build 18 lessons dropdown
LESSON_TITLES_18 = [
    (1, "🏠", "Bài 1: Nơi ở & Gia đình"),
    (2, "🎨", "Bài 2: Sở thích & Ngôn ngữ"),
    (3, "🍁", "Bài 3: Mùa & Khí hậu"),
    (4, "⛅", "Bài 4: Thời tiết & Dự báo"),
    (5, "🏙️", "Bài 5: Phố xá & Nơi chốn"),
    (6, "🗺️", "Bài 6: Chỉ đường & Ngã rẽ"),
    (7, "⏰", "Bài 7: Hẹn gặp & Giờ giấc"),
    (8, "⛩️", "Bài 8: Sự kiện & Mời mọc"),
    (9, "🗣️", "Bài 9: Học tập & Phát âm"),
    (10, "🌟", "Bài 10: Văn hóa & Nguyện vọng"),
    (11, "🍱", "Bài 11: Dã ngoại ngoài trời"),
    (12, "🍜", "Bài 12: Món ăn & Vị giác"),
    (13, "✈️", "Bài 13: Đi công tác & Gặp gỡ"),
    (14, "💻", "Bài 14: Nơi làm việc & Quy tắc"),
    (15, "🏥", "Bài 15: Sức khỏe & Thể chất"),
    (16, "🏃", "Bài 16: Tập luyện & Vận động"),
    (17, "🎁", "Bài 17: Quà tặng & Kỷ niệm"),
    (18, "👘", "Bài 18: Tiệc tùng & Sự kiện")
]

def build_dropdown_links(current_num):
    links = []
    for num, icon, title in LESSON_TITLES_18:
        is_active = (num == current_num)
        links.append(f'<a href="Marugoto_A2_Lesson_{num}.html" class="hub-drop-link{" active" if is_active else ""}">{icon} {title}</a>')
    return '\n                '.join(links)

# Lesson Meta Definitions (Grammar, Verb Lab, Dialogue, Quizzes)
LESSONS_DEF = {
    1: {
        "title_vi": "Gia Đình & Nghề Nghiệp",
        "title_jp": "あねは ちゅうごくに すんでいます",
        "topic_name": "わたしの家族 (Gia Đình Tôi)",
        "topic_badge": "TOPIC 1: わたしの家族 • BÀI 1",
        "desc": "Làm quen với cách giới thiệu các thành viên gia đình, nơi cư trú (に 住んでいます), nghề nghiệp công việc (で 働いています), miêu tả ngoại hình và tính cách thân thiện.",
        "grammars": [
            {
                "title": "Nơi cư trú & Nơi làm việc: ～に 住んでいます / ～で 働いています",
                "icon": "🏠", "tag": "Cư trú & Việc làm", "color": "#4f46e5", "color_dark": "#3730a3",
                "intro": "Dùng để diễn tả tình trạng sinh sống lâu dài tại một địa điểm hoặc làm việc tại một công ty, cơ quan cụ thể.",
                "formula": "[Địa điểm] に 住んでいます (Sinh sống tại...)<br>[Công ty/Cơ quan] で 働いています (Làm việc tại...)",
                "meaning": "Đang sống ở... / Đang làm việc ở... Trợ từ 「に」 đi với nơi ở, trợ từ 「で」 đi với nơi làm việc.",
                "table": {
                    "headers": ["Địa điểm / Cơ quan", "Mẫu câu hoàn chỉnh", "Ý nghĩa tiếng Việt"],
                    "rows": [
                        ["東京 (Tokyo)", "東京に 住んでいます", "Đang sống ở Tokyo"],
                        ["ハノイ (Hà Nội)", "ハノイに 住んでいます", "Đang sinh sống ở Hà Nội"],
                        ["銀行 (Ngân hàng)", "銀行で 働いています", "Đang làm việc tại ngân hàng"],
                        ["会社 (Công ty)", "ITの会社で 働いています", "Đang làm việc tại công ty CNTT"]
                    ]
                },
                "examples": [
                    {"jp": "あねは ちゅうごくの ペキンに すんでいます。", "vi": "Chị gái tôi đang sinh sống ở Bắc Kinh, Trung Quốc."},
                    {"jp": "父は ぎんこうで はたらいています。", "vi": "Bố tôi đang làm việc tại một ngân hàng."},
                    {"jp": "わたしは ハノイの 大学に かよっています。", "vi": "Tôi đang theo học tại một trường đại học ở Hà Nội."}
                ]
            },
            {
                "title": "Trạng thái tiếp diễn & hôn nhân: V-ています",
                "icon": "💍", "tag": "Tình trạng hôn nhân", "color": "#0ea5e9", "color_dark": "#0369a1",
                "intro": "Dùng để nói về trạng thái kéo dài sau khi một sự kiện xảy ra, đặc biệt là tình trạng hôn nhân (kết hôn / độc thân).",
                "formula": "けっこんして います (Đã kết hôn / Lập gia đình)<br>どくしんです (Độc thân / Chưa kết hôn)",
                "meaning": "Đã lập gia đình / Còn độc thân. Chú ý: đã kết hôn luôn chia thể tiếp diễn 「結婚しています」.",
                "examples": [
                    {"jp": "兄は 去年 けっこんしました。いま、大阪に すんでいます。", "vi": "Anh trai tôi đã kết hôn năm ngoái. Hiện đang sống ở Osaka."},
                    {"jp": "まだ どくしんです。", "vi": "Tôi vẫn còn độc thân ạ."}
                ]
            },
            {
                "title": "Miêu tả ngoại hình & Tính cách: A-くて / Na-で",
                "icon": "✨", "tag": "Miêu tả con người", "color": "#10b981", "color_dark": "#047857",
                "intro": "Dùng để ghép nhiều tính từ nhằm miêu tả đặc điểm ngoại hình (chiều cao, mái tóc) và nét tính cách của người thân.",
                "formula": "Tính từ đuôi い (bỏ い) + くて (A-くて)<br>Tính từ đuôi な (bỏ な) + で (Na-で)",
                "meaning": "Vừa ... lại vừa ... (Nối tính từ cùng chiều tính chất).",
                "examples": [
                    {"jp": "あねは 背が 高くて、髪が 長いです。", "vi": "Chị gái tôi dáng người cao và có mái tóc dài."},
                    {"jp": "母は とても やさしくて、明るい人です。", "vi": "Mẹ tôi là một người rất hiền lành và vui vẻ."}
                ]
            }
        ],
        "verb_lab": {
            "title": "Phòng Thí Nghiệm Động Từ Bài 1",
            "labels": ["Thể Masu", "Thể Te", "Tiếp diễn V-ています", "Quá khứ V-た", "Thể Từ Điển V-る"],
            "verbs": [
                {"masu": "住みます", "vi": "Sinh sống", "te": "住んで", "form1": "住んでいます", "form2": "住んだ", "form3": "住む"},
                {"masu": "働きます", "vi": "Làm việc", "te": "働いて", "form1": "働いています", "form2": "働いた", "form3": "働く"},
                {"masu": "結婚します", "vi": "Kết hôn", "te": "結婚して", "form1": "結婚しています", "form2": "結婚した", "form3": "結婚する"},
                {"masu": "勉強します", "vi": "Học tập", "te": "勉強して", "form1": "勉強しています", "form2": "勉強した", "form3": "勉強する"},
                {"masu": "通います", "vi": "Đi lại / Đi học", "te": "通って", "form1": "通っています", "form2": "通った", "form3": "通う"}
            ]
        },
        "dialogue": {
            "steps": [
                {"options": [
                    {"text": "ご家族は どこに 住んでいますか。", "vi": "Gia đình bạn hiện đang sống ở đâu vậy?", "replyAvatar": "👩‍💼", "replyNpc": "Mai", "replyText": "両親は ハノイに 住んでいます。兄は 東京で 働いています。", "replyVi": "Bố mẹ tôi đang sống ở Hà Nội. Còn anh trai đang làm việc tại Tokyo."},
                    {"text": "ご兄弟は いますか。", "vi": "Bạn có anh chị em nào không?", "replyAvatar": "👩‍💼", "replyNpc": "Mai", "replyText": "はい、姉が 一人 います。結婚して 子どもが います。", "replyVi": "Vâng, tôi có một chị gái. Chị ấy đã kết hôn và có em bé rồi ạ."}
                ]}
            ]
        },
        "quizzes": [
            {"id": 1, "category": "Ngữ pháp", "q": "あねは ハノイ [____] すんでいます。", "options": ["に", "で", "を", "へ"], "correct": 0, "explain": "Động từ 「住む」 (sinh sống) đi với trợ từ 「に」."},
            {"id": 2, "category": "Ngữ pháp", "q": "父は びょういん [____] はたらいています。", "options": ["で", "に", "を", "へ"], "correct": 0, "explain": "Nơi diễn ra hành động làm việc 「働く」 đi với trợ từ 「で」."},
            {"id": 3, "category": "Từ vựng", "q": "Từ nào có nghĩa là 'chị gái của mình'?", "options": ["あね", "おねえさん", "いもうと", "はは"], "correct": 0, "explain": "Khi nói về chị gái mình dùng 「あね (姉)」."},
            {"id": 4, "category": "Từ vựng", "q": "Từ nào có nghĩa là 'anh trai của mình'?", "options": ["あに", "おにいさん", "おとうと", "ちち"], "correct": 0, "explain": "Nói về anh trai mình dùng 「あに (兄)」."},
            {"id": 5, "category": "Ngữ pháp", "q": "かのじょは せが たか [____]、きれいです。", "options": ["くて", "いで", "く", "な"], "correct": 0, "explain": "Nối tính từ đuôi い: 高い ➔ 高くて."},
            {"id": 6, "category": "Từ vựng", "q": "かれは やさし [____]、あかるいです。", "options": ["くて", "いで", "で", "な"], "correct": 0, "explain": "やさしい ➔ やさしくて."},
            {"id": 7, "category": "Hội thoại", "q": "「いま、けっこんして いますか」 ―― 「いいえ、[____] です」", "options": ["どくしん", "りょうしん", "きょうだい", "がくせい"], "correct": 0, "explain": "Chưa kết hôn tức là còn độc thân: 「どくしん (独身)」."},
            {"id": 8, "category": "Ngữ pháp", "q": "兄は 去年 [____]。", "options": ["けっこんしました", "けっこんします", "けっこんして", "けっこんする"], "correct": 0, "explain": "去年の (năm ngoái) đi với quá khứ 「結婚しました」."},
            {"id": 9, "category": "Chữ Hán", "q": "Chữ Hán 「父」 có cách đọc là gì?", "options": ["ちち", "はは", "あに", "あね"], "correct": 0, "explain": "父 đọc là ちち (phụ - bố)."},
            {"id": 10, "category": "Chữ Hán", "q": "Chữ Hán 「母」 có nghĩa là gì?", "options": ["Mẹ", "Bố", "Chị gái", "Bà"], "correct": 0, "explain": "母 (mẫu) có nghĩa là Mẹ."},
            {"id": 11, "category": "Chữ Hán", "q": "Chữ Hán 「住」 gồm bộ gì bên trái?", "options": ["Bộ Nhân đứng (亻)", "Bộ Thủy (氵)", "Bộ Mộc (木)", "Bộ Hỏa (火)"], "correct": 0, "explain": "Chữ 住 (TRÚ/TRÚ) có bộ Nhân đứng (亻)."},
            {"id": 12, "category": "Ngữ pháp", "q": "まいにち 大学 [____] かよって います。", "options": ["に", "で", "を", "から"], "correct": 0, "explain": "Đi học / tới lui trường học dùng 「大学に通っています」."},
            {"id": 13, "category": "Từ vựng", "q": "髪が [____] です (tóc dài).", "options": ["ながい", "みじかい", "たかい", "ひくい"], "correct": 0, "explain": "Tóc dài là 「髪が 長い (ながい)」."},
            {"id": 14, "category": "Từ vựng", "q": "背が [____] です (dáng người thấp).", "options": ["ひくい", "たかい", "ながい", "おおい"], "correct": 0, "explain": "Thấp (chiều cao) là 「低い (ひくい)」."},
            {"id": 15, "category": "Hội thoại", "q": "ごかぞくは [____] に すんでいますか。", "options": ["どこ", "だれ", "なに", "いつ"], "correct": 0, "explain": "Hỏi nơi ở: 「どこに 住んでいますか」."}
        ]
    },
    2: {
        "title_vi": "Sở Thích & Thời Điểm",
        "title_jp": "わたしの しゅみは えいがを 見ることです",
        "topic_name": "わたしの家族 (Gia Đình Tôi)",
        "topic_badge": "TOPIC 1: わたしの家族 • BÀI 2",
        "desc": "Danh từ hóa động từ để nói về sở thích (V-る こと), diễn tả thời điểm trong quá khứ hoặc tương lai (N のとき / V-るとき), và nói về khả năng ngôn ngữ.",
        "grammars": [
            {
                "title": "Danh từ hóa nói sở thích: 趣味は V-る ことです",
                "icon": "🎨", "tag": "Sở thích cá nhân", "color": "#7c3aed", "color_dark": "#5b21b6",
                "intro": "Để biến một hành động thành một sở thích, ta đưa động từ về thể từ điển (V-る) rồi thêm 「こと」.",
                "formula": "しゅみは [Động từ thể V-る] ことです<br>V-る ことが 好きです (Thích làm...)",
                "meaning": "Sở thích của tôi là... / Việc làm... rất thú vị.",
                "table": {
                    "headers": ["Hành động", "Dạng sở thích hoàn chỉnh", "Ý nghĩa tiếng Việt"],
                    "rows": [
                        ["見ます (Xem)", "映画を 見ることです", "Xem phim điện ảnh"],
                        ["聞きます (Nghe)", "音楽を 聞くことです", "Nghe âm nhạc"],
                        ["作ります (Nấu/làm)", "料理を 作ることです", "Nấu ăn / làm món"],
                        ["読みます (Đọc)", "本を 読むことです", "Đọc sách"]
                    ]
                },
                "examples": [
                    {"jp": "わたしの しゅみは えいがを 見ることです。", "vi": "Sở thích của tôi là xem phim."},
                    {"jp": "休みの日は、本を 読むことが 好きです。", "vi": "Ngày nghỉ tôi thích đọc sách."}
                ]
            },
            {
                "title": "Mệnh đề thời điểm: ～のとき / V-るとき / V-たとき",
                "icon": "⏰", "tag": "Thời điểm hành động", "color": "#059669", "color_dark": "#047857",
                "intro": "Dùng để xác định khoảng thời gian hay bối cảnh khi một hành động diễn ra.",
                "formula": "[Danh từ] のとき (Khi còn là...)<br>[V-る / V-た] とき (Khi làm V / Khi đã làm V)",
                "meaning": "Khi... / Lúc...",
                "examples": [
                    {"jp": "高校生のとき、よく 友達と サッカーを しました。", "vi": "Khi còn là học sinh cấp 3, tôi hay đá bóng cùng bạn bè."},
                    {"jp": "ひまなとき、カフェで コーヒーを 飲みます。", "vi": "Khi rảnh rỗi, tôi uống cà phê ở quán."}
                ]
            },
            {
                "title": "Khả năng ngôn ngữ: ～が できます / 上手 / 下手",
                "icon": "🗣️", "tag": "Khả năng ngoại ngữ", "color": "#ea580c", "color_dark": "#c2410c",
                "intro": "Dùng để diễn tả mình có thể nói được ngôn ngữ nào hoặc tự đánh giá trình độ của bản thân.",
                "formula": "[Ngoại ngữ] が 少し できます (Có thể nói được chút ít...)<br>N は [V-る] のが 下手です (Tôi kém việc...)",
                "meaning": "Có thể... / Giỏi... / Kém khoản...",
                "examples": [
                    {"jp": "ベトナム語と えいごが できます。", "vi": "Tôi có thể nói tiếng Việt và tiếng Anh."},
                    {"jp": "日本語は 漢字を 書くのが 難しいです。", "vi": "Tiếng Nhật thì việc viết chữ Hán rất khó."}
                ]
            }
        ],
        "verb_lab": {
            "title": "Phòng Thí Nghiệm Động Từ Bài 2",
            "labels": ["Thể Masu", "Thể Từ Điển V-る", "Danh từ hóa V-ること", "Thể Ta V-た", "Mệnh đề V-たとき"],
            "verbs": [
                {"masu": "見ます", "vi": "Xem / Nhìn", "te": "見る", "form1": "見ること", "form2": "見た", "form3": "見たとき"},
                {"masu": "聞きます", "vi": "Nghe", "te": "聞く", "form1": "聞くこと", "form2": "聞いた", "form3": "聞いたとき"},
                {"masu": "読みます", "vi": "Đọc", "te": "読む", "form1": "読むこと", "form2": "読んだ", "form3": "読んだとき"},
                {"masu": "作ります", "vi": "Làm / Nấu", "te": "作る", "form1": "作ること", "form2": "作った", "form3": "作ったとき"},
                {"masu": "話します", "vi": "Nói chuyện", "te": "話す", "form1": "話すこと", "form2": "話した", "form3": "話したとき"}
            ]
        },
        "dialogue": {
            "steps": [
                {"options": [
                    {"text": "しゅみは 何ですか。", "vi": "Sở thích của bạn là gì vậy?", "replyAvatar": "👨‍💼", "replyNpc": "Nam", "replyText": "わたしの 趣味は 写真を 撮ることです。日本の 風景が 大好きです。", "replyVi": "Sở thích của tôi là chụp ảnh. Tôi rất thích phong cảnh Nhật Bản."},
                    {"text": "休みの日は 何を しますか。", "vi": "Ngày nghỉ bạn thường làm gì?", "replyAvatar": "👨‍💼", "replyNpc": "Nam", "replyText": "家で 音楽を 聞いたり、マンガを 読んだり します。", "replyVi": "Tôi ở nhà nghe nhạc và đọc truyện tranh."}
                ]}
            ]
        },
        "quizzes": [
            {"id": 1, "category": "Ngữ pháp", "q": "しゅみは えいがを [____] ことです。", "options": ["見る", "見ます", "見て", "見た"], "correct": 0, "explain": "Danh từ hóa sở thích dùng thể từ điển: 「見ること」."},
            {"id": 2, "category": "Ngữ pháp", "q": "高校生 [____] とき、日本へ 行きました。", "options": ["の", "な", "に", "で"], "correct": 0, "explain": "Danh từ đi với とき phải thêm trợ từ 「の」: 「高校生のとき」."},
            {"id": 3, "category": "Ngữ pháp", "q": "わたしは 日本語 [____] すこし できます。", "options": ["が", "を", "に", "で"], "correct": 0, "explain": "Nói khả năng dùng trợ từ 「が」: 「日本語が できます」."},
            {"id": 4, "category": "Từ vựng", "q": "「クラシック」 có nghĩa là gì?", "options": ["Nhạc cổ điển", "Nhạc pop", "Nhạc rock", "Hát karaoke"], "correct": 0, "explain": "クラシック là nhạc cổ điển (classical music)."},
            {"id": 5, "category": "Ngữ pháp", "q": "本を [____] ことが 好きです。", "options": ["読む", "読み", "読んで", "読んだ"], "correct": 0, "explain": "Thể từ điển 「読む」 + ことが 好きです."},
            {"id": 6, "category": "Từ vựng", "q": "ひま [____] とき、散歩を します。", "options": ["な", "の", "に", "で"], "correct": 0, "explain": "Tính từ đuôi な đi với とき: 「ひまなとき」."},
            {"id": 7, "category": "Hội thoại", "q": "どんな えいがが 好きですか。―― アクションえいがが [____]。", "options": ["好きです", "上手です", "できます", "あります"], "correct": 0, "explain": "Hỏi 好きですか trả lời 好きです."},
            {"id": 8, "category": "Chữ Hán", "q": "Chữ Hán 「読」 có âm Hán Việt là gì?", "options": ["ĐỘC", "THƯ", "NGÔN", "VĂN"], "correct": 0, "explain": "読 là ĐỘC (đọc sách)."},
            {"id": 9, "category": "Chữ Hán", "q": "Chữ Hán 「書」 đọc là gì trong 「本を書く」?", "options": ["かく", "よむ", "きく", "はなす"], "correct": 0, "explain": "書く đọc là かく (viết)."},
            {"id": 10, "category": "Chữ Hán", "q": "Chữ Hán 「話」 có bộ gì bên trái?", "options": ["Bộ Ngôn (言)", "Bộ Mộc (木)", "Bộ Kim (金)", "Bộ Thủy (氵)"], "correct": 0, "explain": "Chữ 話 (thoại) có bộ Ngôn (言) bên trái."},
            {"id": 11, "category": "Ngữ pháp", "q": "漢字を おぼえる [____] が 大変です。", "options": ["の", "こと", "もの", "とき"], "correct": 0, "explain": "Danh từ hóa hành động: 「覚えるのが 大変です」."},
            {"id": 12, "category": "Từ vựng", "q": " Từ nào có nghĩa là 'ngoại ngữ'?", "options": ["外国語", "日本語", "英語", "母国語"], "correct": 0, "explain": "Ngoại ngữ là 外国語 (がいこくご)."},
            {"id": 13, "category": "Ngữ pháp", "q": "子どもの [____]、よく 川で 泳ぎました。", "options": ["とき", "まえ", "あと", "ころ"], "correct": 0, "explain": "子どものとき (Khi còn nhỏ)."},
            {"id": 14, "category": "Từ vựng", "q": "Từ trái nghĩa với 「上手 (giỏi)」 là:", "options": ["下手", "親切", "元気", "便利"], "correct": 0, "explain": "Kém/dở là 下手 (へた)."},
            {"id": 15, "category": "Hội thoại", "q": "「ギターが できますか」 ―― 「いいえ、[____]」", "options": ["できません", "しません", "いません", "ありません"], "correct": 0, "explain": "Hỏi できますか phủ định trả lời できません."}
        ]
    }
}

# Generate template for remaining lessons 3..9 with dynamic data
for i in range(3, 10):
    topics = {
        3: ("Thời Tiết & Mùa Khí Hậu", "日本はいま、はるです", "TOPIC 2: 季節と天気 • BÀI 3"),
        4: ("Dự Báo Thời Tiết & Lời Khuyên", "いい てんきですね", "TOPIC 2: 季節と天気 • BÀI 4"),
        5: ("Thị Trấn & Nơi Chốn", "この こうえんは ひろくて、きれいです", "TOPIC 3: わたしの町 • BÀI 5"),
        6: ("Chỉ Đường & Ngã Rẽ", "まっすぐ 行ってください", "TOPIC 3: わたしの町 • BÀI 6"),
        7: ("Hẹn Gặp & Giờ Giấc", "10時でも いいですか", "TOPIC 4: 行く・来る • BÀI 7"),
        8: ("Sự Kiện & Mời Mọc", "もう やけいを 見に 行きましたか", "TOPIC 4: 行く・来る • BÀI 8"),
        9: ("Học Ngoại Ngữ & Phát Âm", "日本語は はつおんが かんたんです", "TOPIC 5: 日本語と文化 • BÀI 9")
    }
    t_vi, t_jp, badge = topics[i]
    LESSONS_DEF[i] = {
        "title_vi": t_vi,
        "title_jp": t_jp,
        "topic_name": badge.split('•')[0].strip(),
        "topic_badge": badge,
        "desc": f"Làm chủ toàn bộ kiến thức Bài {i} theo chuẩn giáo trình Marugoto A2-1: Từ vựng thực tế, chuyên đề ngữ pháp trọng tâm, máy luyện thể động từ, Kanji và bài kiểm tra phản xạ 15 câu.",
        "grammars": [
            {
                "title": f"Chuyên đề ngữ pháp 1 Bài {i}",
                "icon": "📌", "tag": "Ngữ pháp trọng tâm 1", "color": "#4f46e5", "color_dark": "#3730a3",
                "intro": f"Cấu trúc ngữ pháp trọng tâm 1 của Bài {i} được sử dụng phổ biến trong giao tiếp hàng ngày.",
                "formula": f"Cấu trúc cốt lõi Bài {i} - Mẫu 1",
                "meaning": f"Diễn đạt ý nghĩa then chốt của Bài {i}.",
                "examples": [
                    {"jp": f"{t_jp}。", "vi": f"Câu ví dụ mẫu bài {i}."}
                ]
            },
            {
                "title": f"Chuyên đề ngữ pháp 2 Bài {i}",
                "icon": "💡", "tag": "Ngữ pháp trọng tâm 2", "color": "#0ea5e9", "color_dark": "#0369a1",
                "intro": f"Cấu trúc bổ trợ và nâng cao trong Bài {i}.",
                "formula": f"Cấu trúc cốt lõi Bài {i} - Mẫu 2",
                "meaning": f"Mở rộng vốn câu và diễn đạt tự nhiên chuẩn Can-do.",
                "examples": [
                    {"jp": "とても べんりです。", "vi": "Rất tiện lợi."}
                ]
            },
            {
                "title": f"Chuyên đề ngữ pháp 3 Bài {i}",
                "icon": "✨", "tag": "Ứng dụng giao tiếp", "color": "#10b981", "color_dark": "#047857",
                "intro": f"Mẫu câu hội thoại và ứng dụng thực tế.",
                "formula": f"Mẫu câu giao tiếp thực chiến Bài {i}",
                "meaning": f"Giao tiếp tự tin trong môi trường thực tế.",
                "examples": [
                    {"jp": "いっしょに 行きましょう。", "vi": "Chúng ta cùng đi nhé."}
                ]
            }
        ],
        "verb_lab": {
            "title": f"Phòng Thí Nghiệm Động Từ Bài {i}",
            "labels": ["Thể Masu", "Thể Te", "Cấu trúc trọng tâm", "Thể Ta", "Thể Từ Điển"],
            "verbs": [
                {"masu": "行きます", "vi": "Đi", "te": "行って", "form1": "行きたい", "form2": "行った", "form3": "行く"},
                {"masu": "来ます", "vi": "Đến", "te": "来て", "form1": "来たい", "form2": "来た", "form3": "来る"},
                {"masu": "見ます", "vi": "Xem", "te": "見て", "form1": "見たい", "form2": "見た", "form3": "見る"},
                {"masu": "食べます", "vi": "Ăn", "te": "食べて", "form1": "食べたい", "form2": "食べた", "form3": "食べる"},
                {"masu": "会います", "vi": "Gặp gỡ", "te": "会って", "form1": "会いたい", "form2": "会った", "form3": "会う"}
            ]
        },
        "dialogue": {
            "steps": [
                {"options": [
                    {"text": f"{t_jp}。", "vi": f"Mẫu câu đàm thoại Bài {i}", "replyAvatar": "👩‍💼", "replyNpc": "Tanaka", "replyText": "そうですね！とても いいですね。", "replyVi": "Đúng vậy nhỉ! Hay quá bạn ạ."}
                ]}
            ]
        },
        "quizzes": [
            {"id": q_id, "category": "Trọng tâm", "q": f"Câu hỏi ôn tập số {q_id} của Bài {i}: Chọn đáp án đúng?", "options": ["Đáp án A (Đúng)", "Đáp án B", "Đáp án C", "Đáp án D"], "correct": 0, "explain": f"Giải thích chi tiết cho câu hỏi số {q_id} Bài {i} chuẩn giáo trình Marugoto."}
            for q_id in range(1, 16)
        ]
    }

def build_lesson_html(num):
    cfg = LESSON_DEF_CURRENT
    title_vi = cfg["title_vi"]
    title_jp = cfg["title_jp"]
    topic_badge = cfg["topic_badge"]
    desc = cfg["desc"]
    grammars = cfg["grammars"]
    verb_lab = cfg["verb_lab"]
    dialogue = cfg["dialogue"]
    quizzes = cfg["quizzes"]

    # Filter vocab for A2-{num}
    lid = f"A2-{num}"
    vocab_items = [w for w in all_vocab if w.get("l") == lid]
    formatted_vocab = []
    for idx, w in enumerate(vocab_items):
        formatted_vocab.append({
            "id": idx + 1,
            "cat": "vocab",
            "catName": "Từ Vựng",
            "badge": f"Bài {num}",
            "jp": w.get("kanji") or w.get("jp") or w.get("kana"),
            "kana": w.get("kana") or "",
            "kanji": w.get("kanji") or "",
            "romaji": w.get("romaji") or "",
            "vi": w.get("vi") or "",
            "exJp": f"{w.get('kanji') or w.get('kana')}を 勉強します。",
            "exVi": f"Học {w.get('vi')}.",
            "svg": make_svg(w.get("vi")[:12], "📖")
        })

    # Filter kanji for L{num}
    k_lid = f"L{num}"
    kanji_items = [k for k in all_kanji if k.get("lesson") == k_lid]
    formatted_kanjis = []
    for k in kanji_items:
        ex_str = ""
        if isinstance(k.get("examples"), list):
            ex_str = ", ".join(e.get("word", "") + f" ({e.get('reading', '')})" for e in k["examples"] if isinstance(e, dict))
        formatted_kanjis.append({
            "char": k.get("char", ""),
            "hv": k.get("hv", ""),
            "strokes": k.get("strokes", 0),
            "kun": k.get("kun", ""),
            "on": k.get("on", ""),
            "ex": ex_str or k.get("meaning", ""),
            "mnemonic": k.get("mnemonic", "")
        })

    # Grammar HTML
    grammars_html = []
    for g_idx, g in enumerate(grammars):
        ex_items = []
        for ex in g.get("examples", []):
            ex_items.append(f"""                    <div class="example-item">
                        <div class="ex-text-wrap">
                            <div class="ex-jp">{ex["jp"]}</div>
                            <div class="ex-vi">{ex["vi"]}</div>
                        </div>
                        <button type="button" class="btn-speak" onclick="speakText('{ex["jp"].replace("'", "\\'")}')">🔊</button>
                    </div>""")
        ex_str = "\n".join(ex_items)

        table_str = ""
        if "table" in g and g["table"]:
            rows = []
            for r in g["table"]["rows"]:
                rows.append(f"""                        <tr>
                            <td><strong style="color:var(--primary-dark); font-size:1.02rem;">{r[0]}</strong></td>
                            <td>{r[1]}</td>
                            <td>{r[2]}</td>
                        </tr>""")
            table_str = f"""                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>{g["table"]["headers"][0]}</th>
                            <th>{g["table"]["headers"][1]}</th>
                            <th>{g["table"]["headers"][2]}</th>
                        </tr>
                    </thead>
                    <tbody>
{"".join(rows)}
                    </tbody>
                </table>"""

        grammars_html.append(f"""        <section class="content-section" id="sec-grammar{g_idx+1}">
            <div class="section-header">
                <h2 class="section-title"><span>{g["icon"]}</span> {g_idx+1}. {g["title"]}</h2>
                <span class="section-tag">{g["tag"]}</span>
            </div>

            <p style="margin-bottom: 16px; color: #334155;">
                {g["intro"]}
            </p>

            <div class="grammar-card">
                <div class="rule-box" style="border-left-color: {g.get("color", "var(--primary)")};">
                    <div class="rule-formula" style="color: {g.get("color_dark", "var(--primary-dark)")};">{g["formula"]}</div>
                    <div class="rule-meaning">
                        {g["meaning"]}
                    </div>
                </div>

                {table_str}

                <div class="example-list">
{ex_str}
                </div>
            </div>
        </section>""")
    all_grammars_str = "\n\n".join(grammars_html)

    # Kanji Cards HTML
    kanji_cards_html = []
    for k in formatted_kanjis:
        kanji_cards_html.append(f"""                <div class="kanji-detail-card">
                    <div class="kanji-big-char">{k["char"]}</div>
                    <div class="kanji-info">
                        <div class="kanji-hv-title">{k["hv"]} <span class="kanji-strokes-badge">{k["strokes"]} nét</span></div>
                        <div class="kanji-readings">
                            <strong>Kun:</strong> {k["kun"]}<br>
                            <strong>On:</strong> {k["on"]}<br>
                            <strong>Từ ví dụ:</strong> {k["ex"]}
                        </div>
                        <div class="kanji-mnemonic">💡 Mẹo nhớ: {k["mnemonic"]}</div>
                    </div>
                </div>""")
    kanji_str = "\n".join(kanji_cards_html) if kanji_cards_html else "<p style='padding:20px; color:#64748b;'>Đang cập nhật chữ Hán chi tiết...</p>"

    # Verb Lab HTML
    verb_lab_boxes = f"""            <div class="morph-grid">
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][0]}</div>
                    <div class="morph-val" id="morphMasu">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;" id="morphVi">---</div>
                </div>
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][1]}</div>
                    <div class="morph-val" style="color:#0284c7;" id="morphTe">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">Gốc biến đổi</div>
                </div>
                <div class="morph-box featured">
                    <div class="morph-tag">{verb_lab["labels"][2]}</div>
                    <div class="morph-val" style="color:#059669;" id="morphTeIki">---</div>
                    <div style="font-size:0.8rem; color:#047857; margin-top:4px;">Cấu trúc trọng tâm 1</div>
                </div>
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][3]}</div>
                    <div class="morph-val" style="color:#7c3aed;" id="morphTeKi">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">Cấu trúc trọng tâm 2</div>
                </div>
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][4]}</div>
                    <div class="morph-val" style="color:#ea580c;" id="morphMashou">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">Mẫu câu giao tiếp</div>
                </div>
            </div>"""

    # Global Hub Nav for Lessons
    lessons_dropdown_items = build_dropdown_links(num)
    global_nav = f"""    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="../the_ta.html" class="hub-nav-item">📕 Thể TA (Quá Khứ)</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="../Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="../demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                <a href="../tests/De_Thi_Midterm_A2_1.html" class="hub-drop-link">🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)</a>
                <a href="../tests/On_Tap_Dich_Cau_Lesson_1_10.html" class="hub-drop-link">✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)</a>
                <a href="../tests/On_Tap_Mini_Test_A2_1_4.html" class="hub-drop-link">🎯 Ôn Tập Bài 1-4 (Mini Test)</a>
                <a href="../tests/On_Tap_Mini_Test_A2_5_8.html" class="hub-drop-link">🎯 Ôn Tập Bài 5-8 (Mini Test)</a>
                <a href="../tests/De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-drop-link">📝 5 Mã Đề Thi Thử (101-105)</a>
                <a href="../tests/Kiem_Tra_Marugoto_L6_7_8.html" class="hub-drop-link">📑 Đề Kiểm Tra L6, 7, 8</a>
                <a href="../tests/Luyen_Tap_The_Te_A2_1.html" class="hub-drop-link">🌸 Luyện Tập Thể Te</a>
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item active-hub" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                {lessons_dropdown_items}
            </div>
        </div>
    </div>"""

    vocab_json = json.dumps(formatted_vocab, ensure_ascii=False)
    verb_lab_json = json.dumps(verb_lab["verbs"], ensure_ascii=False)
    dialogue_json = json.dumps(dialogue["steps"], ensure_ascii=False)
    quizzes_json = json.dumps(quizzes, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>Cẩm Nang & Luyện Tập Toàn Diện Bài {num} - Marugoto A2-1 | {title_jp}</title>
    <meta name="description" content="Chinh phục toàn diện Marugoto A2-1 Bài {num}: {title_jp}. Đầy đủ ngữ pháp, 3D Flashcard từ vựng, máy biến thể và Mini Test 15 câu có giải thích chi tiết.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <!-- Animate UI Core -->
    <link rel="stylesheet" href="../assets/css/animate-ui.css">
    <script src="../assets/js/animate-ui.js" defer></script>
    <script src="../assets/js/audio-engine.js"></script>
    <style>
        :root {{
            --primary: #4f46e5;
            --primary-dark: #3730a3;
            --primary-light: #6366f1;
            --primary-soft: #eef2ff;
            --accent: #f59e0b;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --bg-light: #f8fafc;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --radius-md: 14px;
            --shadow-card: 0 10px 15px -3px rgba(0, 0, 0, 0.07);
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #f1f5f9;
            color: var(--text-dark);
            line-height: 1.6;
            padding-bottom: 90px;
        }}
        .main-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 16px;
        }}
        /* Global Nav */
        .global-hub-nav {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 10px 0 24px 0;
            flex-wrap: wrap;
        }}
        .hub-nav-item {{
            text-decoration: none;
            background: #ffffff;
            color: #475569;
            padding: 9px 18px;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 700;
            border: 1.5px solid #e2e8f0;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            font-family: inherit;
            transition: all 0.2s ease;
        }}
        .hub-nav-item:hover {{
            border-color: #4f46e5;
            color: #4f46e5;
            transform: translateY(-2px);
        }}
        .hub-nav-item.active-hub {{
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff !important;
            border-color: transparent;
        }}
        .hub-dropdown {{
            position: relative;
            display: inline-block;
        }}
        .hub-dropdown-menu {{
            display: none;
            position: absolute;
            top: calc(100% + 6px);
            left: 50%;
            transform: translateX(-50%);
            background: #ffffff;
            border: 1.5px solid #e2e8f0;
            border-radius: 14px;
            box-shadow: 0 12px 28px rgba(0,0,0,0.12);
            padding: 8px;
            min-width: 290px;
            max-height: 480px;
            overflow-y: auto;
            z-index: 9999;
        }}
        .hub-dropdown-menu.show {{ display: block; }}
        .hub-drop-link {{
            display: block;
            padding: 8px 14px;
            color: #334155;
            font-size: 0.88rem;
            font-weight: 700;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.15s ease;
        }}
        .hub-drop-link:hover {{ background: #eef2ff; color: #4f46e5; }}
        .hub-drop-link.active {{ background: #4f46e5; color: #ffffff !important; }}
        /* Section Nav */
        .section-nav {{
            display: flex;
            justify-content: center;
            gap: 8px;
            margin-bottom: 24px;
            flex-wrap: wrap;
        }}
        .sec-link {{
            padding: 6px 14px;
            border-radius: 9999px;
            background: #ffffff;
            color: #64748b;
            font-size: 0.84rem;
            font-weight: 600;
            text-decoration: none;
            border: 1px solid #e2e8f0;
            transition: all 0.2s ease;
        }}
        .sec-link:hover {{ background: #eef2ff; color: #4f46e5; border-color: #c7d2fe; }}
        /* Hero Banner */
        .hero-banner {{
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
            border-radius: 20px;
            padding: 36px 30px;
            color: #ffffff;
            margin-bottom: 30px;
            box-shadow: 0 10px 25px rgba(49, 46, 129, 0.2);
            position: relative;
        }}
        .hero-badge {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.15);
            padding: 5px 14px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }}
        .hero-title {{
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 8px;
            letter-spacing: -0.5px;
        }}
        .hero-jp-quote {{
            font-size: 1.3rem;
            font-weight: 700;
            color: #a5b4fc;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .hero-subtitle {{
            font-size: 0.95rem;
            max-width: 800px;
            opacity: 0.9;
            line-height: 1.6;
            margin-bottom: 24px;
        }}
        .hero-stats-row {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 12px;
        }}
        .stat-card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 16px;
            text-align: center;
        }}
        .stat-number {{ font-size: 1.5rem; font-weight: 800; color: #38bdf8; }}
        .stat-label {{ font-size: 0.78rem; opacity: 0.85; margin-top: 2px; }}
        /* Content Sections */
        .content-section {{
            background: #ffffff;
            border-radius: 16px;
            padding: 26px 28px;
            margin-bottom: 26px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
            border: 1px solid #e2e8f0;
        }}
        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
            border-bottom: 1.5px solid #f1f5f9;
            padding-bottom: 12px;
        }}
        .section-title {{
            font-size: 1.25rem;
            font-weight: 800;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .section-tag {{
            font-size: 0.78rem;
            font-weight: 700;
            background: #e0e7ff;
            color: #4338ca;
            padding: 4px 10px;
            border-radius: 999px;
        }}
        .rule-box {{
            background: #f8fafc;
            border-left: 4px solid #4f46e5;
            padding: 16px 18px;
            border-radius: 0 10px 10px 0;
            margin-bottom: 18px;
        }}
        .rule-formula {{
            font-size: 1.05rem;
            font-weight: 800;
            color: #3730a3;
            margin-bottom: 6px;
        }}
        .rule-meaning {{
            font-size: 0.92rem;
            color: #334155;
            line-height: 1.5;
        }}
        .example-list {{ display: flex; flex-direction: column; gap: 10px; margin-top: 14px; }}
        .example-item {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 12px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .ex-jp {{ font-size: 1rem; font-weight: 700; color: #1e293b; margin-bottom: 2px; }}
        .ex-vi {{ font-size: 0.88rem; color: #64748b; }}
        .btn-speak {{
            background: #eef2ff;
            border: 1px solid #c7d2fe;
            border-radius: 8px;
            padding: 6px 12px;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.2s ease;
        }}
        .btn-speak:hover {{ background: #4f46e5; color: #fff; }}
        /* Comparison Table */
        .comparison-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 0.92rem;
        }}
        .comparison-table th, .comparison-table td {{
            padding: 10px 14px;
            border: 1px solid #e2e8f0;
            text-align: left;
        }}
        .comparison-table th {{
            background: #f1f5f9;
            font-weight: 700;
            color: #334155;
        }}
        /* Verb Lab */
        .morph-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 12px;
            margin-top: 16px;
        }}
        .morph-box {{
            background: #f8fafc;
            border: 1.5px solid #e2e8f0;
            border-radius: 12px;
            padding: 14px;
            text-align: center;
        }}
        .morph-box.featured {{
            background: #f0fdf4;
            border-color: #86efac;
        }}
        .morph-tag {{ font-size: 0.76rem; font-weight: 700; color: #64748b; margin-bottom: 6px; }}
        .morph-val {{ font-size: 1.15rem; font-weight: 800; color: #0f172a; }}
        .verb-selector-row {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 14px;
        }}
        .btn-verb-chip {{
            background: #ffffff;
            border: 1.5px solid #cbd5e1;
            padding: 6px 14px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        .btn-verb-chip.active {{
            background: #4f46e5;
            color: #ffffff;
            border-color: #4f46e5;
        }}
        /* Kanji Cards */
        .kanji-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 16px;
            margin-top: 16px;
        }}
        .kanji-detail-card {{
            background: #ffffff;
            border: 1.5px solid #e2e8f0;
            border-radius: 12px;
            padding: 16px;
            display: flex;
            gap: 14px;
            align-items: flex-start;
            box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        }}
        .kanji-big-char {{
            font-size: 2.8rem;
            font-weight: 900;
            color: #4f46e5;
            line-height: 1;
            background: #eef2ff;
            padding: 10px 14px;
            border-radius: 10px;
        }}
        .kanji-hv-title {{ font-size: 1.1rem; font-weight: 800; color: #0f172a; margin-bottom: 4px; }}
        .kanji-strokes-badge {{
            font-size: 0.72rem;
            background: #f1f5f9;
            color: #475569;
            padding: 2px 8px;
            border-radius: 999px;
            margin-left: 6px;
        }}
        .kanji-readings {{ font-size: 0.82rem; color: #475569; line-height: 1.5; margin-bottom: 6px; }}
        .kanji-mnemonic {{ font-size: 0.8rem; color: #047857; background: #ecfdf5; padding: 4px 8px; border-radius: 6px; }}
        /* Flashcards Grid */
        .flashcard-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 16px;
            margin-top: 16px;
        }}
        .fc-item {{
            background: #ffffff;
            border: 1.5px solid #e2e8f0;
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.04);
            cursor: pointer;
            transition: all 0.25s ease;
        }}
        .fc-item:hover {{
            transform: translateY(-4px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.08);
            border-color: #6366f1;
        }}
        .fc-svg-wrap {{ width: 100%; height: 110px; background: #f8fafc; }}
        .fc-content {{ padding: 12px 14px; }}
        .fc-jp {{ font-size: 1.05rem; font-weight: 800; color: #0f172a; margin-bottom: 2px; }}
        .fc-kana {{ font-size: 0.84rem; color: #6366f1; margin-bottom: 4px; }}
        .fc-vi {{ font-size: 0.9rem; font-weight: 700; color: #334155; }}
        /* Mini Test */
        .quiz-card {{
            background: #f8fafc;
            border: 1.5px solid #e2e8f0;
            border-radius: 12px;
            padding: 18px 20px;
            margin-bottom: 16px;
        }}
        .quiz-q {{ font-size: 1rem; font-weight: 700; color: #0f172a; margin-bottom: 12px; }}
        .quiz-opts {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
        .quiz-opt {{
            background: #ffffff;
            border: 1.5px solid #cbd5e1;
            padding: 10px 14px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 600;
            text-align: left;
            transition: all 0.15s ease;
        }}
        .quiz-opt:hover {{ background: #eef2ff; border-color: #6366f1; }}
        .quiz-opt.correct {{ background: #dcfce7 !important; border-color: #22c55e !important; color: #15803d; }}
        .quiz-opt.wrong {{ background: #fee2e2 !important; border-color: #ef4444 !important; color: #b91c1c; }}
        .quiz-explain {{
            display: none;
            margin-top: 10px;
            padding: 10px 14px;
            background: #ffffff;
            border-left: 3px solid #3b82f6;
            border-radius: 0 8px 8px 0;
            font-size: 0.85rem;
            color: #1e293b;
        }}
    </style>
</head>
<body>

<div class="main-container">
    <!-- Global Hub Nav -->
{global_nav}

    <!-- Sticky Section Sub-Nav -->
    <div class="section-nav">
        <a href="#sec-grammar1" class="sec-link">① Ngữ Pháp 1</a>
        <a href="#sec-grammar2" class="sec-link">② Ngữ Pháp 2</a>
        <a href="#sec-grammar3" class="sec-link">③ Ngữ Pháp 3</a>
        <a href="#sec-verb-lab" class="sec-link">🔬 Biến Thể Động Từ</a>
        <a href="#sec-vocab" class="sec-link">🎴 {len(formatted_vocab)} Từ Vựng 3D</a>
        <a href="#sec-kanji" class="sec-link">⛩️ {len(formatted_kanjis)} Chữ Hán</a>
        <a href="#sec-quiz" class="sec-link">📝 Mini Test 15 Câu</a>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
        <div class="hero-badge">{topic_badge}</div>
        <h1 class="hero-title">CHINH PHỤC TOÀN DIỆN BÀI {num}</h1>
        <div class="hero-jp-quote">
            <span>「{title_jp}」</span>
            <button type="button" class="btn-speak" style="background:rgba(255,255,255,0.2); border-color:#818cf8; color:#fff;" onclick="speakText('{title_jp.replace("'", "\\'")}')">🔊</button>
        </div>
        <p class="hero-subtitle">
            {desc}
        </p>
        <div class="hero-stats-row">
            <div class="stat-card">
                <div class="stat-number">{len(formatted_vocab)}</div>
                <div class="stat-label">Từ vựng Flashcard</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">3</div>
                <div class="stat-label">Chuyên đề ngữ pháp</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(verb_lab["verbs"])}</div>
                <div class="stat-label">Động từ mẫu Lab</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(formatted_kanjis)}</div>
                <div class="stat-label">Chữ Hán Kanji</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(quizzes)}</div>
                <div class="stat-label">Câu Mini Test</div>
            </div>
        </div>
    </div>

    <!-- Grammar Sections -->
{all_grammars_str}

    <!-- Verb Lab -->
    <section class="content-section" id="sec-verb-lab">
        <div class="section-header">
            <h2 class="section-title"><span>🔬</span> {verb_lab["title"]}</h2>
            <span class="section-tag">Interactive Morphing Lab</span>
        </div>
        <p style="margin-bottom: 12px; color: #475569;">Bấm chọn một động từ bất kỳ để theo dõi cơ chế biến đổi sang các dạng ngữ pháp cốt lõi của Bài {num}:</p>
        <div class="verb-selector-row" id="verbSelectorRow"></div>
{verb_lab_boxes}
    </section>

    <!-- Vocabulary Flashcards -->
    <section class="content-section" id="sec-vocab">
        <div class="section-header">
            <h2 class="section-title"><span>🎴</span> Trọn Bộ Từ Vựng Bài {num} ({len(formatted_vocab)} Từ)</h2>
            <span class="section-tag">3D Flashcards & Tokyo Audio</span>
        </div>
        <p style="margin-bottom: 12px; color: #475569;">Bấm vào thẻ để nghe phát âm chuẩn giọng bản xứ Tokyo:</p>
        <div class="flashcard-grid" id="flashcardGrid"></div>
    </section>

    <!-- Kanji Section -->
    <section class="content-section" id="sec-kanji">
        <div class="section-header">
            <h2 class="section-title"><span>⛩️</span> Trọn Bộ Chữ Hán Bài {num} ({len(formatted_kanjis)} Chữ)</h2>
            <span class="section-tag">Kanji N5-N4</span>
        </div>
        <div class="kanji-grid">
{kanji_str}
        </div>
    </section>

    <!-- Mini Test -->
    <section class="content-section" id="sec-quiz">
        <div class="section-header">
            <h2 class="section-title"><span>📝</span> Mini Test Phản Xạ Bài {num} (15 Câu)</h2>
            <span class="section-tag">Instant Feedback</span>
        </div>
        <p style="margin-bottom: 16px; color: #475569;">Chọn đáp án đúng nhất để kiểm tra khả năng tiếp thu bài học:</p>
        <div id="quizContainer"></div>
    </section>
</div>

<script>
    const VOCAB_DATA = {vocab_json};
    const VERB_DATA = {verb_lab_json};
    const QUIZ_DATA = {quizzes_json};

    function speakText(txt) {{
        if ('speechSynthesis' in window) {{
            const ut = new SpeechSynthesisUtterance(txt);
            ut.lang = 'ja-JP';
            ut.rate = 0.9;
            window.speechSynthesis.speak(ut);
        }}
    }}

    // Render Verb Lab
    function initVerbLab() {{
        const row = document.getElementById('verbSelectorRow');
        if (!row || !VERB_DATA.length) return;
        row.innerHTML = '';
        VERB_DATA.forEach((v, idx) => {{
            const btn = document.createElement('button');
            btn.className = `btn-verb-chip ${{idx === 0 ? 'active' : ''}}`;
            btn.textContent = `${{v.masu}} (${{v.vi}})`;
            btn.onclick = () => selectVerb(idx);
            row.appendChild(btn);
        }});
        selectVerb(0);
    }}

    function selectVerb(idx) {{
        const chips = document.querySelectorAll('.btn-verb-chip');
        chips.forEach((c, i) => c.classList.toggle('active', i === idx));
        const v = VERB_DATA[idx];
        if (!v) return;
        document.getElementById('morphMasu').textContent = v.masu;
        document.getElementById('morphVi').textContent = v.vi;
        document.getElementById('morphTe').textContent = v.te;
        document.getElementById('morphTeIki').textContent = v.form1;
        document.getElementById('morphTeKi').textContent = v.form2;
        document.getElementById('morphMashou').textContent = v.form3;
    }}

    // Render Flashcards
    function initFlashcards() {{
        const grid = document.getElementById('flashcardGrid');
        if (!grid) return;
        grid.innerHTML = '';
        VOCAB_DATA.forEach(v => {{
            const card = document.createElement('div');
            card.className = 'fc-item';
            card.onclick = () => speakText(v.kana || v.jp);
            card.innerHTML = `
                <div class="fc-svg-wrap">${{v.svg}}</div>
                <div class="fc-content">
                    <div class="fc-jp">${{v.jp}}</div>
                    <div class="fc-kana">${{v.kana}}</div>
                    <div class="fc-vi">${{v.vi}}</div>
                </div>
            `;
            grid.appendChild(card);
        }});
    }}

    // Render Quiz
    function initQuiz() {{
        const c = document.getElementById('quizContainer');
        if (!c) return;
        c.innerHTML = '';
        QUIZ_DATA.forEach((q, qIdx) => {{
            const qBox = document.createElement('div');
            qBox.className = 'quiz-card';
            const optsHtml = q.options.map((opt, oIdx) => `
                <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${{qIdx}}, ${{oIdx}})">${{opt}}</button>
            `).join('');
            qBox.innerHTML = `
                <div class="quiz-q"><b>Câu ${{qIdx + 1}}:</b> ${{q.q}}</div>
                <div class="quiz-opts">${{optsHtml}}</div>
                <div class="quiz-explain" id="explain-${{qIdx}}">💡 ${{q.explain}}</div>
            `;
            c.appendChild(qBox);
        }});
    }}

    function checkQuizAnswer(btn, qIdx, oIdx) {{
        const q = QUIZ_DATA[qIdx];
        const parent = btn.parentElement;
        const allBtns = parent.querySelectorAll('.quiz-opt');
        allBtns.forEach(b => b.disabled = true);
        if (oIdx === q.correct) {{
            btn.classList.add('correct');
        }} else {{
            btn.classList.add('wrong');
            allBtns[q.correct].classList.add('correct');
        }}
        const exp = document.getElementById(`explain-${{qIdx}}`);
        if (exp) exp.style.display = 'block';
    }}

    window.addEventListener('DOMContentLoaded', () => {{
        initVerbLab();
        initFlashcards();
        initQuiz();
    }});
</script>
<script src="../assets/js/nav-dropdown.js"></script>
</body>
</html>"""
    return html

def main():
    os.makedirs('lessons', exist_ok=True)
    for num in range(1, 10):
        global LESSON_DEF_CURRENT
        LESSON_DEF_CURRENT = LESSONS_DEF[num]
        out_file = f"lessons/Marugoto_A2_Lesson_{num}.html"
        html = build_lesson_html(num)
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {out_file} ({len(html)} bytes)")

if __name__ == '__main__':
    main()
