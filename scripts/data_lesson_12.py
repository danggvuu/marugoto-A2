# -*- coding: utf-8 -*-
"""
Data for Marugoto A2-2 Lesson 12:
Topic 6: そとで食べる (Ăn ngoài trời)
Bài 12: Món Ăn & Hương Vị (おいしそうですね - Trông ngon quá nhỉ!)
"""

def make_svg(title, emoji, c1="#059669", c2="#047857"):
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

CFG_12 = {
    "num": 12,
    "title_vi": "Món Ăn & Hương Vị",
    "title_jp": "おいしそうですね",
    "topic_name": "Ăn Ngoài Trời (そとで食べる)",
    "topic_badge": "TOPIC 6: そとで食べる • BÀI 12",
    "desc": "Chinh phục toàn diện cách miêu tả món ăn, nhận xét hương vị (cay, ngọt, chua, mặn, đắng), phán đoán vẻ bề ngoài với cấu trúc ～そう, so sánh với các món ăn quen thuộc và tự tin mời mọc, phản hồi trong bữa tiệc ẩm thực.",
    
    "grammars": [
        {
            "title": "Phán đoán qua thị giác: ～そう (Trông có vẻ...)",
            "icon": "🍜",
            "tag": "Thị giác & Đánh giá",
            "color": "#059669",
            "color_dark": "#047857",
            "intro": "Dùng khi người nói nhìn vào bề ngoài của món ăn hoặc sự vật và đưa ra cảm nhận, phán đoán trực tiếp trước khi thử hoặc trước khi sự việc diễn ra.",
            "formula": "Tính từ đuôi い (Bỏ い) + そうです<br>Tính từ đuôi な (Bỏ な) + そうです<br>Động từ thể ます (Bỏ ます) + そうです",
            "meaning": "Trông có vẻ... / Dường như sắp... (Đặc biệt: いい ➔ よさそう). Khi khen ngợi món ăn người khác mang tới: 「おいしそうですね！」 (Trông ngon quá nhỉ!).",
            "table": {
                "headers": ["Dạng gốc", "Cách biến đổi sang ～そう", "Ý nghĩa tiếng Việt"],
                "rows": [
                    ["おいしい (Ngon)", "おいしそう (です)", "Trông có vẻ ngon"],
                    ["からい (Cay)", "からそう (です)", "Trông có vẻ cay"],
                    ["あつい (Nóng sốt)", "あつそう (です)", "Trông có vẻ nóng sốt"],
                    ["あまい (Ngọt)", "あまそう (です)", "Trông có vẻ ngọt đậm"],
                    ["いい (Tốt/ngon)", "よさそう (です)", "Trông có vẻ ổn/hay đấy"]
                ]
            },
            "examples": [
                {"jp": "そのケーキ、とても おいしそうですね。", "vi": "Chiếc bánh ngọt đó trông ngon lành quá nhỉ!"},
                {"jp": "赤いですから、ちょっと からそうですね。", "vi": "Vì màu đỏ nên trông có vẻ hơi cay đấy nhỉ."},
                {"jp": "このスープは あつそうだから、気をつけてください。", "vi": "Món canh súp này trông nóng lắm, bạn cẩn thận nhé."}
            ]
        },
        {
            "title": "Nối tính từ miêu tả món ăn: A-くて / Na-で",
            "icon": "🌶️",
            "tag": "Miêu tả hương vị đa tầng",
            "color": "#ea580c",
            "color_dark": "#c2410c",
            "intro": "Dùng để liên kết hai hay nhiều tính chất, hương vị của món ăn trong cùng một câu nói mạch lạc, mượt mà.",
            "formula": "Tính từ đuôi い ➔ Bỏ い + くて<br>Tính từ đuôi な ➔ Bỏ な + で",
            "meaning": "Vừa... vừa... / ... và... (ví dụ: vừa cay vừa ngon, vừa rẻ vừa bổ dưỡng).",
            "table": {
                "headers": ["Tính từ 1", "Dạng liên kết", "Câu ví dụ hoàn chỉnh"],
                "rows": [
                    ["からい (Cay)", "からくて", "このサラダは ちょっと からくて、おいしいです。"],
                    ["あまい (Ngọt)", "あまくて", "このイチゴは あまくて、おいしいですよ。"],
                    ["やすい (Rẻ)", "やすくて", "あの店のラーメンは やすくて、おいしいです。"],
                    ["しんせん（な）", "しんせんで", "魚が しんせんで、とても おいしいです。"]
                ]
            },
            "examples": [
                {"jp": "このサラダ、ちょっと からくて おいしいですね。", "vi": "Món salad này hơi cay một chút mà ngon thật đấy."},
                {"jp": "日本の うどんは あたたかくて、おいしいです。", "vi": "Mì Udon của Nhật ấm nóng và rất ngon."},
                {"jp": "このフルーツは つめたくて、あまいです。", "vi": "Trái cây này mát lạnh và ngọt ngào."}
            ]
        },
        {
            "title": "So sánh & Mời ăn: ～と 似ています / よかったらどうぞ",
            "icon": "🍱",
            "tag": "Giao tiếp ẩm thực",
            "color": "#0284c7",
            "color_dark": "#0369a1",
            "intro": "Mẫu câu so sánh một món ăn mới với món quen thuộc của đất nước mình, và các câu khẩu ngữ lịch thiệp khi mời mọc hay đón nhận đồ ăn.",
            "formula": "N1 は N2 と 似ています (Món 1 giống món 2)<br>N1 は N2 と 違います (Món 1 khác món 2)<br>よかったら、どうぞ (Nếu được xin mời bạn dùng thử)<br>いただきます (Tôi xin phép dùng bữa)",
            "meaning": "Dùng để giới thiệu món ăn quê hương, giúp đối phương dễ hình dung hương vị, đồng thời thể hiện sự hiếu khách, văn minh trên bàn tiệc.",
            "examples": [
                {"jp": "これは 韓国のキンパと 似ていますね。", "vi": "Món này trông khá giống với món Kimbap của Hàn Quốc nhỉ."},
                {"jp": "見た目は 似ていますが、味は ちょっと 違います。", "vi": "Bề ngoài thì giống nhau nhưng mùi vị thì hơi khác một chút."},
                {"jp": "よかったら、サラダを どうぞ。―― ありがとうございます。いただきます。", "vi": "Nếu được thì xin mời bạn dùng món salad nhé. ―― Cảm ơn bạn, tôi xin phép dùng thử ạ."}
            ]
        }
    ],

    "vocab": [
        {
                "id": 1,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Món ăn",
                "jp": "つけもの",
                "kana": "つけもの",
                "kanji": "漬物",
                "romaji": "tsukemono",
                "vi": "Đồ muối chua kiểu Nhật",
                "exJp": "きゅうりの つけものが おいしいです。",
                "exVi": "Món dưa chuột muối chua rất ngon.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_785997\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_785997)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥒</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐỒ MUỐI CHUA</text>\n</svg>"
        },
        {
                "id": 2,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Món ăn",
                "jp": "ピクルス",
                "kana": "ピクルス",
                "kanji": "ピクルス",
                "romaji": "pikurusu",
                "vi": "Các loại dưa chua tây (Pickles)",
                "exJp": "ハンバーガーに ピクルスを いれます。",
                "exVi": "Cho dưa chuột bao tử muối vào hamburger.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_792100\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#22c55e\"/>\n      <stop offset=\"100%\" stop-color=\"#15803d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_792100)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥒</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">DƯA CHUA</text>\n</svg>"
        },
        {
                "id": 3,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Rau củ",
                "jp": "レタス",
                "kana": "レタス",
                "kanji": "レタス",
                "romaji": "retasu",
                "vi": "Rau xà lách tươi",
                "exJp": "しんせんな レタスを つかった サラダです。",
                "exVi": "Món salad sử dụng rau xà lách tươi giòn.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_608640\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#16a34a\"/>\n      <stop offset=\"100%\" stop-color=\"#14532d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_608640)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥬</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">XÀ LÁCH</text>\n</svg>"
        },
        {
                "id": 4,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Hoa quả",
                "jp": "レモン",
                "kana": "レモン",
                "kanji": "レモン",
                "romaji": "remon",
                "vi": "Quả chanh vàng",
                "exJp": "からあげに レモンを かけます。",
                "exVi": "Vắt chanh lên món gà rán.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_62332\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#eab308\"/>\n      <stop offset=\"100%\" stop-color=\"#ca8a04\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_62332)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍋</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHANH</text>\n</svg>"
        },
        {
                "id": 5,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Rau củ",
                "jp": "きゅうり",
                "kana": "きゅうり",
                "kanji": "胡瓜",
                "romaji": "kyuuri",
                "vi": "Dưa chuột, dưa leo",
                "exJp": "なつは つめたい きゅうりが おいしいです。",
                "exVi": "Mùa hè ăn dưa leo ướp lạnh rất ngon.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_720377\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#15803d\"/>\n      <stop offset=\"100%\" stop-color=\"#14532d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_720377)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥒</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">DƯA CHUỘT</text>\n</svg>"
        },
        {
                "id": 6,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Hải sản",
                "jp": "えび",
                "kana": "えび",
                "kanji": "海老",
                "romaji": "ebi",
                "vi": "Tôm tươi",
                "exJp": "えびの てんぷらを ちゅうもんしました。",
                "exVi": "Tôi đã gọi món tempura tôm.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_581831\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f97316\"/>\n      <stop offset=\"100%\" stop-color=\"#c2410c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_581831)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🦐</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TÔM TƯƠI</text>\n</svg>"
        },
        {
                "id": 7,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Hải sản",
                "jp": "ツナ",
                "kana": "ツナ",
                "kanji": "ツナ",
                "romaji": "tsuna",
                "vi": "Cá ngừ đại dương (Tuna)",
                "exJp": "ツナマヨの おにぎりが いちばん にんきです。",
                "exVi": "Cơm nắm cá ngừ sốt mayo là được yêu thích nhất.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_352454\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0284c7\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_352454)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🐟</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CÁ NGỪ</text>\n</svg>"
        },
        {
                "id": 8,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Hải sản",
                "jp": "しゃけ／さけ",
                "kana": "しゃけ／さけ",
                "kanji": "鮭",
                "romaji": "shake / sake",
                "vi": "Cá hồi nướng / làm sushi",
                "exJp": "あさごはんに やきざけを たべます。",
                "exVi": "Ăn cá hồi nướng vào bữa sáng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_138941\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#fb923c\"/>\n      <stop offset=\"100%\" stop-color=\"#ea580c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_138941)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍣</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CÁ HỒI</text>\n</svg>"
        },
        {
                "id": 9,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Thực phẩm",
                "jp": "こんぶ",
                "kana": "こんぶ",
                "kanji": "昆布",
                "romaji": "konbu",
                "vi": "Tảo bẹ kombu nấu nước dùng dashi",
                "exJp": "こんぶで だしを とります。",
                "exVi": "Nấu lấy nước dùng từ tảo bẹ kombu.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_365456\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#15803d\"/>\n      <stop offset=\"100%\" stop-color=\"#064e3b\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_365456)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌿</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TẢO BẸ</text>\n</svg>"
        },
        {
                "id": 10,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Món ăn",
                "jp": "うめぼし",
                "kana": "うめぼし",
                "kanji": "梅干し",
                "romaji": "umeboshi",
                "vi": "Quả mơ muối Nhật Bản",
                "exJp": "うめぼしは すっぱくて しょっぱいです。",
                "exVi": "Mơ muối vừa chua vừa mặn.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_79427\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#e11d48\"/>\n      <stop offset=\"100%\" stop-color=\"#9f1239\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_79427)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🔴</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MƠ MUỐI</text>\n</svg>"
        },
        {
                "id": 11,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Thực phẩm",
                "jp": "チーズ",
                "kana": "チーズ",
                "kanji": "チーズ",
                "romaji": "chiizu",
                "vi": "Phô mai (Cheese)",
                "exJp": "ピザに チーズが たっぷり のっています。",
                "exVi": "Bánh pizza có ngập tràn phô mai thơm ngon.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_28506\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f59e0b\"/>\n      <stop offset=\"100%\" stop-color=\"#b45309\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_28506)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🧀</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">PHÔ MAI</text>\n</svg>"
        },
        {
                "id": 12,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Thực phẩm",
                "jp": "ハム",
                "kana": "ハム",
                "kanji": "ハム",
                "romaji": "hamu",
                "vi": "Thịt heo xông khói / dăm bông",
                "exJp": "パンに ハムと チーズを はさみます。",
                "exVi": "Kẹp thịt nguội và phô mai vào bánh mì.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_449210\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f43f5e\"/>\n      <stop offset=\"100%\" stop-color=\"#be123c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_449210)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥓</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">DĂM BÔNG</text>\n</svg>"
        },
        {
                "id": 13,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Gia vị",
                "jp": "マヨネーズ",
                "kana": "マヨネーズ",
                "kanji": "マヨネーズ",
                "romaji": "mayoneezu",
                "vi": "Sốt sốt kem Mayonnaise",
                "exJp": "サラダに マヨネーズを かけます。",
                "exVi": "Rưới sốt mayone lên salad.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_793357\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#fef08a\"/>\n      <stop offset=\"100%\" stop-color=\"#ca8a04\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_793357)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MAYONNAISE</text>\n</svg>"
        },
        {
                "id": 14,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Gia vị",
                "jp": "チリ",
                "kana": "チリ",
                "kanji": "チリ",
                "romaji": "chiri",
                "vi": "Ớt cay (Chili)",
                "exJp": "このソースは チリが はいっていて からいです。",
                "exVi": "Nước sốt này có ớt nên khá cay.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_899243\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#dc2626\"/>\n      <stop offset=\"100%\" stop-color=\"#991b1b\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_899243)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌶️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ỚT CAY</text>\n</svg>"
        },
        {
                "id": 15,
                "cat": "food",
                "catName": "Món ăn & Thực phẩm",
                "badge": "Bánh kẹo",
                "jp": "センベイ",
                "kana": "センベイ",
                "kanji": "煎餅",
                "romaji": "senbei",
                "vi": "Bánh gạo truyền thống Senbei",
                "exJp": "おちゃと センベイを たべました。",
                "exVi": "Tôi đã uống trà xanh và ăn bánh gạo senbei.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_235727\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#d97706\"/>\n      <stop offset=\"100%\" stop-color=\"#78350f\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_235727)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍘</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BÁNH GẠO</text>\n</svg>"
        },
        {
                "id": 16,
                "cat": "adj",
                "catName": "Vị giác & Tính chất",
                "badge": "Tính từ",
                "jp": "あたたかい",
                "kana": "あたたかい",
                "kanji": "温かい",
                "romaji": "atatakai",
                "vi": "Ấm áp, ấm nóng (đồ ăn/thức uống)",
                "exJp": "あたたかい おちゃを どうぞ。",
                "exVi": "Xin mời dùng chén trà ấm nóng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_812902\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f97316\"/>\n      <stop offset=\"100%\" stop-color=\"#c2410c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_812902)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">♨️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ẤM NÓNG</text>\n</svg>"
        },
        {
                "id": 17,
                "cat": "adj",
                "catName": "Vị giác & Tính chất",
                "badge": "Tính từ",
                "jp": "つめたい",
                "kana": "つめたい",
                "kanji": "冷たい",
                "romaji": "tsumetai",
                "vi": "Lạnh, buốt (nhiệt độ đồ uống/vật)",
                "exJp": "つめたい ビールを のみたいです。",
                "exVi": "Tôi muốn uống một cốc bia thật lạnh.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_848277\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#38bdf8\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_848277)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🧊</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">LẠNH BUỐT</text>\n</svg>"
        },
        {
                "id": 18,
                "cat": "adj",
                "catName": "Vị giác & Tính chất",
                "badge": "Tính từ",
                "jp": "おいしい",
                "kana": "おいしい",
                "kanji": "美味しい",
                "romaji": "oishii",
                "vi": "Ngon miệng",
                "exJp": "この てんぷらは とても おいしいです。",
                "exVi": "Món tempura này thực sự rất ngon.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_515274\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_515274)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">😋</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NGON MIỆNG</text>\n</svg>"
        },
        {
                "id": 19,
                "cat": "adj",
                "catName": "Vị giác & Tính chất",
                "badge": "Tính từ",
                "jp": "まずい",
                "kana": "まずい",
                "kanji": "不味い",
                "romaji": "mazui",
                "vi": "Dở, không ngon",
                "exJp": "まずい りょうりは たべたくないです。",
                "exVi": "Tôi không muốn ăn đồ ăn dở tệ đâu.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_364763\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#64748b\"/>\n      <stop offset=\"100%\" stop-color=\"#334155\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_364763)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">😖</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">DỞ KHÔNG NGON</text>\n</svg>"
        },
        {
                "id": 20,
                "cat": "taste",
                "catName": "Vị giác & Tính chất",
                "badge": "Vị giác",
                "jp": "あまい",
                "kana": "あまい",
                "kanji": "甘い",
                "romaji": "amai",
                "vi": "Vị ngọt",
                "exJp": "この くだものは とても あまいです。",
                "exVi": "Trái cây này có vị rất ngọt.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_910582\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f59e0b\"/>\n      <stop offset=\"100%\" stop-color=\"#d97706\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_910582)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍯</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VỊ NGỌT</text>\n</svg>"
        },
        {
                "id": 21,
                "cat": "taste",
                "catName": "Vị giác & Tính chất",
                "badge": "Vị giác",
                "jp": "からい",
                "kana": "からい",
                "kanji": "辛い",
                "romaji": "karai",
                "vi": "Vị cay nóng",
                "exJp": "タイりょうりは からいですが、すきです。",
                "exVi": "Món Thái tuy cay nhưng tôi lại rất thích.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_819903\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_819903)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌶️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VỊ CAY</text>\n</svg>"
        },
        {
                "id": 22,
                "cat": "taste",
                "catName": "Vị giác & Tính chất",
                "badge": "Vị giác",
                "jp": "すっぱい",
                "kana": "すっぱい",
                "kanji": "酸っぱい",
                "romaji": "suppai",
                "vi": "Vị chua",
                "exJp": "レモンは すっぱいです。",
                "exVi": "Chanh thì có vị chua gắt.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_48195\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#84cc16\"/>\n      <stop offset=\"100%\" stop-color=\"#4d7c0f\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_48195)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍋</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VỊ CHUA</text>\n</svg>"
        },
        {
                "id": 23,
                "cat": "taste",
                "catName": "Vị giác & Tính chất",
                "badge": "Vị giác",
                "jp": "しょっぱい",
                "kana": "しょっぱい",
                "kanji": "塩っぱい",
                "romaji": "shoppai",
                "vi": "Vị mặn",
                "exJp": "スープに しおが おおくて、しょっぱいです。",
                "exVi": "Nước súp nhiều muối quá nên bị mặn.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_687916\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#06b6d4\"/>\n      <stop offset=\"100%\" stop-color=\"#0e7490\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_687916)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🧂</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VỊ MẶN</text>\n</svg>"
        },
        {
                "id": 24,
                "cat": "taste",
                "catName": "Vị giác & Tính chất",
                "badge": "Vị giác",
                "jp": "にがい",
                "kana": "にがい",
                "kanji": "苦い",
                "romaji": "nigai",
                "vi": "Vị đắng",
                "exJp": "この くすりは とても にがいです。",
                "exVi": "Thuốc này đắng nghét.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_376005\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#78350f\"/>\n      <stop offset=\"100%\" stop-color=\"#451a03\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_376005)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">☕</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VỊ ĐẮNG</text>\n</svg>"
        },
        {
                "id": 25,
                "cat": "expr",
                "catName": "Trạng thái & Cảm nhận",
                "badge": "Cụm từ",
                "jp": "きもちが いい",
                "kana": "きもちが いい",
                "kanji": "気持ちがいい",
                "romaji": "kimochi ga ii",
                "vi": "Thoải mái, dễ chịu, sảng khoái",
                "exJp": "かぜが ふいて、きもちが いいですね。",
                "exVi": "Gió thổi mát mẻ dễ chịu quá nhỉ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_60319\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#059669\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_60319)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍃</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">THOẢI MÁI</text>\n</svg>"
        },
        {
                "id": 26,
                "cat": "adj",
                "catName": "Vị giác & Tính chất",
                "badge": "Tính từ na",
                "jp": "しんせん（な）",
                "kana": "しんせん（な）",
                "kanji": "新鮮（な）",
                "romaji": "shinsen(na)",
                "vi": "Tươi, tươi mới (hải sản, rau)",
                "exJp": "しんせんな さかなで すしを つくります。",
                "exVi": "Làm sushi từ cá tươi ngon.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_905908\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0284c7\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_905908)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🐟</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TƯƠI MỚI</text>\n</svg>"
        },
        {
                "id": 27,
                "cat": "expr",
                "catName": "Trạng thái & Cảm nhận",
                "badge": "Cụm từ",
                "jp": "にんきが あります",
                "kana": "にんきが あります",
                "kanji": "人気があります",
                "romaji": "ninki ga arimasu",
                "vi": "Được mọi người ưa chuộng, nổi tiếng",
                "exJp": "このみせの ラーメンは にんきが あります。",
                "exVi": "Mì ramen của quán này rất được ưa chuộng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_95388\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#eab308\"/>\n      <stop offset=\"100%\" stop-color=\"#a16207\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_95388)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">⭐</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐƯỢC ƯA CHUỘNG</text>\n</svg>"
        },
        {
                "id": 28,
                "cat": "verb",
                "catName": "Trạng thái & Cảm nhận",
                "badge": "Động từ",
                "jp": "ちがいます",
                "kana": "ちがいます",
                "kanji": "違います",
                "romaji": "chigaimasu",
                "vi": "Khác nhau / Không phải",
                "exJp": "ベトナムと にほんの たべものは ちがいます。",
                "exVi": "Ẩm thực Việt Nam và Nhật Bản khác nhau.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_849695\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_849695)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">≠</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KHÁC NHAU</text>\n</svg>"
        },
        {
                "id": 29,
                "cat": "verb",
                "catName": "Trạng thái & Cảm nhận",
                "badge": "Động từ",
                "jp": "にています",
                "kana": "にています",
                "kanji": "似ています",
                "romaji": "niteimasu",
                "vi": "Giống nhau, tương tự",
                "exJp": "このふたつは あじが よく にています。",
                "exVi": "Hai món này hương vị rất giống nhau.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_734368\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_734368)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">≒</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GIỐNG NHAU</text>\n</svg>"
        },
        {
                "id": 30,
                "cat": "expr",
                "catName": "Trạng thái & Cảm nhận",
                "badge": "Cụm từ",
                "jp": "おなかが いっぱいです",
                "kana": "おなかが いっぱいです",
                "kanji": "お腹がいっぱいです",
                "romaji": "onaka ga ippai desu",
                "vi": "No bụng rồi",
                "exJp": "たくさん たべて、おなかが いっぱいです。",
                "exVi": "Ăn nhiều quá, no căng bụng rồi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_462852\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#22c55e\"/>\n      <stop offset=\"100%\" stop-color=\"#15803d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_462852)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤰</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NO BỤNG</text>\n</svg>"
        },
        {
                "id": 31,
                "cat": "expr",
                "catName": "Trạng thái & Cảm nhận",
                "badge": "Cụm từ",
                "jp": "おなかが すきました",
                "kana": "おなかが すきました",
                "kanji": "お腹が空きました",
                "romaji": "onaka ga sukimashita",
                "vi": "Đói bụng rồi",
                "exJp": "おなかが すいたので、ごはんを たべましょう。",
                "exVi": "Đói bụng rồi nên cùng đi ăn cơm thôi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_820680\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f97316\"/>\n      <stop offset=\"100%\" stop-color=\"#ea580c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_820680)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤤</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐÓI BỤNG</text>\n</svg>"
        }
],

    "verb_lab": {
        "title": "Phòng Thí Nghiệm Động/Tính Từ Vị Giác (Morphing Lab)",
        "desc": "Thực hành chuyển đổi tính từ miêu tả hương vị sang dạng phán đoán ～そう (Trông có vẻ), liên kết ～くて và mẫu câu kinh nghiệm 食べたことがあります:",
        "labels": ["Gốc từ", "Dạng liên kết", "Phán đoán thị giác", "Mẫu câu kinh nghiệm", "Mẫu câu giao tiếp"],
        "verbs": [
            {
                "kanji": "美味しい",
                "masu": "おいしい",
                "vi": "Ngon miệng",
                "col2": "おいしくて",
                "col3": "おいしそう",
                "col4": "食べたことがある",
                "col5": "どうぞ食べてみて",
                "ex": "このケーキはとてもおいしそうですね。"
            },
            {
                "kanji": "辛い",
                "masu": "からい",
                "vi": "Cay",
                "col2": "からくて",
                "col3": "からそう",
                "col4": "からいのが好き",
                "col5": "ちょっとからいですよ",
                "ex": "この料理は赤くて、ちょっとからそうですね。"
            },
            {
                "kanji": "甘い",
                "masu": "あまい",
                "vi": "Ngọt ngào",
                "col2": "あまくて",
                "col3": "あまそう",
                "col4": "あまくておいしい",
                "col5": "あまい物が好きです",
                "ex": "このイチゴはあまくておいしいです。"
            },
            {
                "kanji": "温かい",
                "masu": "あたたかい",
                "vi": "Ấm áp, nóng sốt",
                "col2": "あたたかくて",
                "col3": "あたたかそう",
                "col4": "あたたかいスープ",
                "col5": "あたたかい内にどうぞ",
                "ex": "あたたかいスープをどうぞ飲んでください。"
            },
            {
                "kanji": "冷たい",
                "masu": "つめたい",
                "vi": "Mát lạnh",
                "col2": "つめたくて",
                "col3": "つめたそう",
                "col4": "つめたいビール",
                "col5": "つめたいうどんが好き",
                "ex": "暑い日にはつめたい麦茶が一番です。"
            }
        ]
    },

    "dialogue": {
        "title": "Thưởng Thức Hương Vị Trong Bữa Tiệc Picnic",
        "desc": "Đóng vai người tham gia bữa tiệc ngoài trời, giao lưu và nhận xét hương vị món ăn với bạn bè Nhật Bản:",
        "initial": {
            "avatar": "👩‍🦰",
            "name": "Emi (Bạn học Nhật)",
            "jp": "これ、私が作ったお弁当です。どうぞ！",
            "vi": "Đây là hộp cơm bento do chính tay mình tự làm đấy. Mời các bạn cùng ăn nhé!"
        },
        "steps": [
            {
                "options": [
                    {
                        "text": "わあ、とても おいしそうですね！いただきます。",
                        "vi": "Oa, trông ngon mắt quá chừng! Mình xin phép ăn nhé.",
                        "replyAvatar": "👩‍🦰",
                        "replyNpc": "Emi",
                        "replyText": "どうぞ！卵焼きと唐揚げが入っていますよ。",
                        "replyVi": "Cứ tự nhiên nhé! Có trứng cuộn và gà rán bên trong đó."
                    },
                    {
                        "text": "きれいですね！韓国のキンパと似ていますね。",
                        "vi": "Đẹp mắt quá! Trông khá giống món Kimbap của Hàn Quốc nhỉ.",
                        "replyAvatar": "👩‍🦰",
                        "replyNpc": "Emi",
                        "replyText": "そうですね！でも海苔巻きの味は少し違いますよ。",
                        "replyVi": "Đúng thế thật! Nhưng vị của cơm cuộn rong biển Nhật thì hơi khác một chút đấy."
                    }
                ]
            },
            {
                "npcName": "Tanaka",
                "avatar": "👨‍💼",
                "npcText": "こちらのサラダも どうですか。ちょっと からいですよ。",
                "npcVi": "Thử thêm món salad này nữa xem sao? Có vị hơi cay một chút đấy.",
                "options": [
                    {
                        "text": "辛いのは 大好きですから、ぜひ いただきます！",
                        "vi": "Mình cực kỳ thích ăn cay nên nhất định sẽ thử ạ!",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "本当ですか！口に合ってよかったです。",
                        "replyVi": "Thật ư! Rất mừng vì món ăn hợp khẩu vị của bạn nhé."
                    },
                    {
                        "text": "ありがとうございます。辛くて シャキシャキして おいしいです！",
                        "vi": "Cảm ơn bạn. Rau vừa cay vừa giòn sần sật, ngon tuyệt vời!",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "たくさん 食べてくださいね！",
                        "replyVi": "Bạn hãy ăn thật nhiều vào nhé!"
                    }
                ]
            }
        ]
    },

    "kanjis": [
        {"char": "料", "hv": "LIỆU", "strokes": 10, "kun": "-", "on": "RYOO", "ex": "料理 (りょうり - món ăn), 料金 (りょうきん - cước phí)", "mnemonic": "Lúa gạo (米) được đem đi cân đong (斗) để tính nguyên LIỆU."},
        {"char": "理", "hv": "LÝ", "strokes": 11, "kun": "-", "on": "RI", "ex": "料理 (りょうり - nấu nướng), 理由 (りゆう - lý do)", "mnemonic": "Vua (王) dùng ngọc quý giải thích đạo LÝ trong thôn làng (里)."},
        {"char": "味", "hv": "VỊ", "strokes": 8, "kun": "あじ", "on": "MI", "ex": "味 (あじ - mùi vị), 意味 (いみ - ý nghĩa)", "mnemonic": "Cái miệng (口) nếm thử ngọn cây non chưa trổ (未) để biết VỊ."},
        {"char": "色", "hv": "SẮC", "strokes": 6, "kun": "いろ", "on": "SHOKU, SHIKI", "ex": "色 (いろ - màu sắc), 茶色 (ちゃいろ - màu nâu)", "mnemonic": "Con người thể hiện sắc mặt và màu SẮC rực rỡ."},
        {"char": "野", "hv": "DÃ", "strokes": 11, "kun": "の", "on": "YA", "ex": "野菜 (やさい - rau xanh), 野球 (やきゅう - bóng chày)", "mnemonic": "Thôn dã (里) đem lại cho ta nhiều điều mầu nhiệm (予)."},
        {"char": "菜", "hv": "THÁI", "strokes": 11, "kun": "-", "on": "SAI", "ex": "野菜 (やさい - rau củ), 菜食 (さいしょく - ăn chay)", "mnemonic": "Cỏ cây (艹) dùng tay hái (采) về làm món rau THÁI tươi ngon."},
        {"char": "少", "hv": "THIỂU", "strokes": 4, "kun": "すく-ない、すこ-し", "on": "SHOO", "ex": "少し (すこし - một chút), 少ない (すくない - ít ỏi)", "mnemonic": "Chữ Tiểu (小) có thêm một nét phẩy tức là ít THIỂU hơn nữa."}
    ],

    "quizzes": [
        {"id": 1, "category": "Ngữ pháp: ～そう", "q": "この ラーメンは とても [____] ですね。", "options": ["おいしそう", "おいしいそう", "おいしくそう", "おいしかったそう"], "correct": 0, "explain": "Tính từ đuôi い khi kết hợp với ～そう sẽ bỏ い: おいしい ➔ おいしそう (Trông có vẻ ngon)."},
        {"id": 2, "category": "Ngữ pháp: ～そう", "q": "スープが 赤いですから、ちょっと [____] ですね。", "options": ["からそう", "からいそう", "からくそう", "からだそう"], "correct": 0, "explain": "からい ➔ bỏ い thêm そう thành 「からそう」 (Trông có vẻ cay)."},
        {"id": 3, "category": "Ngữ pháp: Nối tính từ A-くて", "q": "この サラダは ちょっと [____]、おいしいです。", "options": ["からくて", "からいで", "からいから", "からくても"], "correct": 0, "explain": "Nối 2 tính từ: からい ➔ からくて (Hơi cay một chút mà ngon)."},
        {"id": 4, "category": "Từ vựng: Vị giác", "q": "レモンは どんな 味ですか。―― とても [____] です。", "options": ["すっぱい", "あまい", "にがい", "しょっぱい"], "correct": 0, "explain": "Quả chanh (レモン) thì có vị chua là 「すっぱい」."},
        {"id": 5, "category": "Từ vựng: Vị giác", "q": "ケーキや チョコレートは [____] です。", "options": ["あまい", "からい", "すっぱい", "まずい"], "correct": 0, "explain": "Bánh ngọt và sô-cô-la có vị ngọt là 「あまい」."},
        {"id": 6, "category": "Từ vựng: Vị giác", "q": "しおが たくさん 入っていますから、とても [____] です。", "options": ["しょっぱい", "すっぱい", "にがい", "あまい"], "correct": 0, "explain": "Cho nhiều muối (しお) thì món ăn sẽ bị mặn muối là 「しょっぱい」."},
        {"id": 7, "category": "Ngữ pháp: So sánh ～と似ています", "q": "日本の すしは 韓国の キンパ [____] 似ています。", "options": ["と", "に", "を", "で"], "correct": 0, "explain": "Cấu trúc so sánh giống với cái gì: 「N と 似ています」 (Giống với N)."},
        {"id": 8, "category": "Ngữ pháp: Mẫu câu kinh nghiệm", "q": "あなたは 納豆を [____] ことがありますか。", "options": ["食べた", "食べる", "食べ", "食べて"], "correct": 0, "explain": "Cấu trúc hỏi trải nghiệm kinh nghiệm trong quá khứ là: V-た ことがありますか ➔ 「食べたことがありますか」."},
        {"id": 9, "category": "Giao tiếp: Mời ăn", "q": "Khi muốn lịch sự mời bạn bè dùng thử món ăn của mình, ta nói:", "options": ["よかったら、どうぞ", "ごちそうさまでした", "お邪魔します", "失礼します"], "correct": 0, "explain": "「よかったら、どうぞ」 nghĩa là 'Nếu được xin mời bạn cứ tự nhiên dùng'."},
        {"id": 10, "category": "Giao tiếp: Đáp lại lời mời", "q": "Khi nhận món ăn người khác mời, câu chào trước khi ăn là:", "options": ["いただきます", "ごちそうさま", "お疲れ様", "どういたしまして"], "correct": 0, "explain": "Câu nói bắt buộc khi bắt đầu ăn là 「いただきます」."},
        {"id": 11, "category": "Chữ Hán Bài 12: 料 (Liệu)", "q": "Chữ Hán 「料」 trong từ 「料理 (りょうり)」 có âm Hán Việt là:", "options": ["LIỆU", "LÝ", "KHOA", "VỊ"], "correct": 0, "explain": "Chữ 料 có âm Hán Việt là LIỆU (10 nét), mang nghĩa nguyên liệu, vật liệu."},
        {"id": 12, "category": "Chữ Hán Bài 12: 理 (Lý)", "q": "Chữ Hán nào kết hợp với 「料」 để tạo thành từ 「りょうり」 (Món ăn)?", "options": ["理", "野", "菜", "味"], "correct": 0, "explain": "「料理」 gồm chữ LIỆU (料) và chữ LÝ (理 - 11 nét)."},
        {"id": 13, "category": "Chữ Hán Bài 12: 味 (Vị)", "q": "Từ 「あじ」 (Mùi vị) được viết bằng chữ Hán là:", "options": ["味", "色", "少", "菜"], "correct": 0, "explain": "「あじ」 viết bằng chữ Hán là 「味」 (VỊ - 8 nét, gồm bộ Khẩu 口 và chữ Mùi 未)."},
        {"id": 14, "category": "Chữ Hán Bài 12: 野 & 菜", "q": "Từ 「やさい」 (Rau xanh, rau củ) được viết bằng cặp chữ Hán nào?", "options": ["野菜", "料理", "風味", "少色"], "correct": 0, "explain": "「やさい」 viết Hán tự là 「野菜」 (DÃ THÁI)."},
        {"id": 15, "category": "Chữ Hán Bài 12: 少 (Thiểu)", "q": "Từ 「すこし」 (Một chút, một ít) có chữ Hán là:", "options": ["少し", "多し", "小さし", "高し"], "correct": 0, "explain": "「すこし」 viết chữ Hán là 「少し」 (chữ THIỂU - 4 nét)."}
    ]
}
