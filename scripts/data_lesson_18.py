# -*- coding: utf-8 -*-
"""
Data for Marugoto A2-2 Lesson 18:
Topic 9: お祝い (Chúc mừng & Kỷ niệm)
Bài 18: Tiệc Tùng, Trang Phục & Cảm Nghĩ (パーティーがいいと思います)
"""

def make_svg(title, emoji, c1="#8b5cf6", c2="#6d28d9"):
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

CFG_18 = {
    "num": 18,
    "title_vi": "Lễ Hội & Trang Phục",
    "title_jp": "パーティーがいいと思います",
    "topic_name": "Chúc Mừng & Kỷ Niệm (お祝い)",
    "topic_badge": "TOPIC 9: お祝い • BÀI 18",
    "desc": "Làm chủ cấu trúc bày tỏ suy nghĩ, quan điểm cá nhân (～と思います), trích dẫn lời nói của người khác (～と言っていました), phân biệt chính xác 4 nhóm động từ mặc trang phục (着る, 履く, 被る, 掛ける) và gửi những lời chúc tụng trang trọng nhất trong các bữa tiệc kỷ niệm.",

    "grammars": [
        {
            "title": "Bày tỏ suy nghĩ & Quan điểm cá nhân: ～と 思います",
            "icon": "💭",
            "tag": "Ý kiến cá nhân",
            "color": "#8b5cf6",
            "color_dark": "#6d28d9",
            "intro": "Dùng để phát biểu ý kiến, quan điểm hoặc nhận xét của bản thân một cách chừng mực, lịch sự trước tập thể.",
            "formula": "[Thể thông thường (Futsuukei)] + と 思います<br>Danh từ / Tính từ đuôi な (Hiện tại khẳng định): N/Na + だ + と 思います",
            "meaning": "Tôi nghĩ rằng... / Tôi cho là... (ví dụ: Tôi nghĩ tổ chức tiệc sẽ rất vui).",
            "table": {
                "headers": ["Ý kiến", "Dạng thể thông thường + と思います", "Ý nghĩa tiếng Việt"],
                "rows": [
                    ["パーティーがいい (Tiệc rất hay)", "パーティーが いいと 思います", "Tôi nghĩ tổ chức tiệc là hay nhất"],
                    ["喜ぶ (Sẽ rất vui)", "きっと 喜ぶと 思います", "Tôi nghĩ chắc chắn bạn ấy sẽ vui"],
                    ["きれいだ (Xinh đẹp)", "着物が きれいだと 思います", "Tôi nghĩ bộ Kimono rất đẹp"],
                    ["似合う (Rất hợp)", "よく 似合うと 思います", "Tôi nghĩ là rất hợp với bạn"]
                ]
            },
            "examples": [
                {"jp": "阿部さんの お祝いは パーティーが いいと 思います。", "vi": "Mừng cho anh Abe thì tôi nghĩ tổ chức một bữa tiệc là tuyệt nhất."},
                {"jp": "この プレゼントを あげたら、きっと 喜ぶと 思いますよ。", "vi": "Tôi nghĩ nếu tặng món quà này chắc chắn cô ấy sẽ rất vui đấy."},
                {"jp": "日本の 着物は とても 素晴らしいと 思います。", "vi": "Tôi nghĩ trang phục Kimono của Nhật Bản thực sự rất tuyệt vời."}
            ]
        },
        {
            "title": "Trích dẫn lời người khác đã nói: ～と 言っていました",
            "icon": "🗣️",
            "tag": "Truyền đạt thông tin",
            "color": "#0284c7",
            "color_dark": "#0369a1",
            "intro": "Dùng để thuật lại lời nói, tâm tư hoặc nguyện vọng của một người thứ ba cho người nghe biết.",
            "formula": "[Thể thông thường (Futsuukei)] + と 言っていました",
            "meaning": "Ai đó đã nói rằng... (ví dụ: Anh Abe nói rằng muốn trò chuyện cùng mọi người).",
            "examples": [
                {"jp": "阿部さんは みんなと 話したいと 言っていました。", "vi": "Anh Abe đã nói là muốn được trò chuyện cùng với tất cả mọi người."},
                {"jp": "田中さんは 明日の パーティーに 来られないと 言っていました。", "vi": "Anh Tanaka nói là ngày mai không thể đến dự tiệc được."},
                {"jp": "先生も とても 楽しみに していると 言っていましたよ。", "vi": "Thầy giáo cũng nói là đang rất hào hứng mong chờ buổi tiệc đấy."}
            ]
        },
        {
            "title": "Động từ mặc trang phục thể V-ています: Phân loại chuẩn xác",
            "icon": "👘",
            "tag": "Trang phục & Diện mạo",
            "color": "#ec4899",
            "color_dark": "#be185d",
            "intro": "Trong tiếng Nhật, hành động mặc trang phục được phân chia rất chi tiết tùy theo vị trí trên cơ thể và sử dụng thể V-ています để miêu tả trạng thái đang mặc.",
            "formula": "Thân trên / Toàn thân: 着ます ➔ 着ています (Áo, váy, comple, kimono)<br>Thân dưới / Chân: 履きます ➔ 履いています (Quần, váy ngắn, tất, giày)<br>Đầu: 被ります ➔ 被っています (Mũ, nón)<br>Mắt / Phụ kiện: 掛けます ➔ 掛けています (Kính mắt)",
            "meaning": "Đang mặc / Đang đi / Đang đội / Đang đeo...",
            "examples": [
                {"jp": "田中さんは 素敵な 着物を 着ていますね。", "vi": "Cô Tanaka đang mặc một bộ Kimono thật lộng lẫy nhỉ."},
                {"jp": "黒い スーツを 着て、眼鏡を 掛けている 人は 社長です。", "vi": "Người đang mặc bộ comple đen và đeo kính mắt là giám đốc đấy."},
                {"jp": "白い 帽子を 被って、スニーカーを 履いています。", "vi": "Anh ấy đang đội mũ trắng và đi giày thể thao."}
            ]
        }
    ],

    "vocab": [
        {
                "id": 1,
                "cat": "event",
                "catName": "Sự kiện đời người",
                "badge": "Kết hôn",
                "jp": "けっこん",
                "kana": "けっこん",
                "kanji": "結婚",
                "romaji": "kekkon",
                "vi": "Kết hôn",
                "exJp": "友だちの 結婚式に 参加します。",
                "exVi": "Tham dự lễ cưới của bạn thân.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_636456\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_636456)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💍</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KẾT HÔN</text>\n</svg>"
        },
        {
                "id": 2,
                "cat": "event",
                "catName": "Sự kiện đời người",
                "badge": "Chuyển nhà",
                "jp": "ひっこし",
                "kana": "ひっこし",
                "kanji": "引っ越し",
                "romaji": "hikkoshi",
                "vi": "Chuyển nhà",
                "exJp": "来月 新しいアパートに 引っ越しします。",
                "exVi": "Tháng sau tôi sẽ chuyển sang căn hộ mới.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_762725\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_762725)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📦</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHUYỂN NHÀ</text>\n</svg>"
        },
        {
                "id": 3,
                "cat": "event",
                "catName": "Sự kiện đời người",
                "badge": "Bắt đầu đi làm",
                "jp": "しゅうしょく",
                "kana": "しゅうしょく",
                "kanji": "就職",
                "romaji": "shuushoku",
                "vi": "Bắt đầu đi làm, có việc làm",
                "exJp": "息子の 就職が 決まりました。",
                "exVi": "Con trai tôi đã nhận được việc làm ổn định.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_931918\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_931918)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💼</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐI LÀM</text>\n</svg>"
        },
        {
                "id": 4,
                "cat": "event",
                "catName": "Sự kiện đời người",
                "badge": "Sinh con",
                "jp": "しゅっさん",
                "kana": "しゅっさん",
                "kanji": "出産",
                "romaji": "shussan",
                "vi": "Sinh con",
                "exJp": "出産の お祝いを 届けます。",
                "exVi": "Gửi quà chúc mừng bạn sinh em bé.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_356176\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_356176)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">SINH CON</text>\n</svg>"
        },
        {
                "id": 5,
                "cat": "feeling",
                "catName": "Cảm xúc & Tâm trạng",
                "badge": "Vui mừng",
                "jp": "よろこびます",
                "kana": "よろこびます",
                "kanji": "喜びます",
                "romaji": "yorokobimasu",
                "vi": "Vui mừng, hạnh phúc",
                "exJp": "プレゼントを とても 喜んでくれました。",
                "exVi": "Bạn ấy đã vô cùng vui mừng khi nhận món quà.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_165790\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_165790)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥳</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VUI MỪNG</text>\n</svg>"
        },
        {
                "id": 6,
                "cat": "feeling",
                "catName": "Cảm xúc & Tâm trạng",
                "badge": "Hạnh phúc ngập tràn",
                "jp": "しあわせ（な）",
                "kana": "しあわせ（な）",
                "kanji": "幸せ（な）",
                "romaji": "shiawase(na)",
                "vi": "Hạnh phúc",
                "exJp": "いつまでも お幸せに！",
                "exVi": "Chúc hai bạn mãi mãi hạnh phúc bên nhau nhé!",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_700497\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_700497)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥰</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">HẠNH PHÚC</text>\n</svg>"
        },
        {
                "id": 7,
                "cat": "necessity",
                "catName": "Nhu cầu & Đồ dùng",
                "badge": "Cần thiết",
                "jp": "ひつよう（な）",
                "kana": "ひつよう（な）",
                "kanji": "必要（な）",
                "romaji": "hitsuyou(na)",
                "vi": "Cần thiết",
                "exJp": "パスポートが 必要です。",
                "exVi": "Hộ chiếu là giấy tờ cần thiết.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_241791\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_241791)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">❗</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CẦN THIẾT</text>\n</svg>"
        },
        {
                "id": 8,
                "cat": "necessity",
                "catName": "Nhu cầu & Đồ dùng",
                "badge": "Cần có N cho cuộc sống",
                "jp": "N が ひつようです",
                "kana": "N が ひつようです",
                "kanji": "Nが必要です",
                "romaji": "N ga hitsuyou desu",
                "vi": "Cần N",
                "exJp": "新しい 生活に 家具が 必要です。",
                "exVi": "Cuộc sống mới cần có đồ nội thất.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_933238\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_933238)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🛋️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CẦN CÓ N</text>\n</svg>"
        },
        {
                "id": 9,
                "cat": "necessity",
                "catName": "Nhu cầu & Đồ dùng",
                "badge": "Đồ dùng của em bé là rất cần thiết",
                "jp": "あかちゃんの ものが ひつようです",
                "kana": "あかちゃんの ものが ひつようです",
                "kanji": "赤ちゃんの物が必要です",
                "romaji": "akachan no mono ga hitsuyou desu",
                "vi": "Đồ dùng của em bé là cần thiết",
                "exJp": "出産祝には 赤ちゃんの物が 必要です。",
                "exVi": "Quà mừng sinh em bé thì các đồ dùng trẻ sơ sinh là rất cần thiết.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_121227\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_121227)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍼</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐỒ EM BÉ CẦN</text>\n</svg>"
        },
        {
                "id": 10,
                "cat": "gift",
                "catName": "Quà tặng & Lễ nghi",
                "badge": "Viết thiệp chúc mừng",
                "jp": "カードを かきます",
                "kana": "カードを かきます",
                "kanji": "カードを書きます",
                "romaji": "kaado wo kakimasu",
                "vi": "Viết thiệp",
                "exJp": "お祝いの メッセージカードを 書きます。",
                "exVi": "Viết thiệp gửi gắm thông điệp chúc phúc.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_400809\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_400809)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💌</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VIẾT THIỆP</text>\n</svg>"
        },
        {
                "id": 11,
                "cat": "gift",
                "catName": "Quà tặng & Lễ nghi",
                "badge": "Lời cảm ơn",
                "jp": "おれい",
                "kana": "おれい",
                "kanji": "お礼",
                "romaji": "orei",
                "vi": "Lời cảm ơn",
                "exJp": "お世話になった方に お礼を します。",
                "exVi": "Tặng quà đáp lễ người đã giúp đỡ mình.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_495680\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_495680)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🙇‍♂️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">LỜI CẢM ƠN</text>\n</svg>"
        },
        {
                "id": 12,
                "cat": "gift",
                "catName": "Quà tặng & Lễ nghi",
                "badge": "Nói lời cảm ơn chân thành",
                "jp": "おれいを いいます",
                "kana": "おれいを いいます",
                "kanji": "お礼を言います",
                "romaji": "orei wo iimasu",
                "vi": "Nói lời cảm ơn",
                "exJp": "先生に 直接 お礼を 言いました。",
                "exVi": "Tôi đã trực tiếp nói lời cảm ơn tới thầy giáo.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_97874\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_97874)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🗣️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NÓI CẢM ƠN</text>\n</svg>"
        },
        {
                "id": 13,
                "cat": "gift",
                "catName": "Quà tặng & Lễ nghi",
                "badge": "Khung ảnh kỷ niệm",
                "jp": "しゃしんたて",
                "kana": "しゃしんたて",
                "kanji": "写真立て",
                "romaji": "shashintate",
                "vi": "Khung ảnh",
                "exJp": "結婚祝いに 写真立てを あげます。",
                "exVi": "Tặng khung ảnh làm quà mừng cưới.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_364508\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_364508)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🖼️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KHUNG ẢNH</text>\n</svg>"
        },
        {
                "id": 14,
                "cat": "gift",
                "catName": "Quà tặng & Lễ nghi",
                "badge": "Bình hoa",
                "jp": "かびん",
                "kana": "かびん",
                "kanji": "花瓶",
                "romaji": "kabin",
                "vi": "Bình hoa",
                "exJp": "きれいな 花瓶に 花を かざります。",
                "exVi": "Cắm hoa tươi vào chiếc bình hoa tuyệt đẹp.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_717431\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_717431)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏺</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BÌNH HOA</text>\n</svg>"
        },
        {
                "id": 15,
                "cat": "gift",
                "catName": "Quà tặng & Lễ nghi",
                "badge": "Nhẫn đeo tay (nhẫn cưới)",
                "jp": "ゆびわ",
                "kana": "ゆびわ",
                "kanji": "指輪",
                "romaji": "yubiwa",
                "vi": "Nhẫn",
                "exJp": "結婚指輪を 買いました。",
                "exVi": "Chúng tôi đã mua nhẫn cưới.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_218985\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_218985)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💍</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NHẪN ĐEO TAY</text>\n</svg>"
        },
        {
                "id": 16,
                "cat": "feeling",
                "catName": "Cảm xúc & Tâm trạng",
                "badge": "Chắc chắn là",
                "jp": "きっと",
                "kana": "きっと",
                "kanji": "きっと",
                "romaji": "kitto",
                "vi": "Chắc chắn là, nhất định là",
                "exJp": "きっと 喜んでくれると 思います。",
                "exVi": "Tôi tin chắc chắn bạn ấy sẽ rất thích.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_484829\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_484829)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌟</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHẮC CHẮN</text>\n</svg>"
        },
        {
                "id": 17,
                "cat": "gift",
                "catName": "Quà tặng & Lễ nghi",
                "badge": "Bộ âu phục",
                "jp": "スーツ",
                "kana": "スーツ",
                "kanji": "スーツ",
                "romaji": "suutsu",
                "vi": "Bộ vest",
                "exJp": "パーティーに 新しいスーツを 着て行きます。",
                "exVi": "Mặc bộ com-lê mới đi dự tiệc.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_845247\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_845247)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤵</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ÂU PHỤC</text>\n</svg>"
        },
        {
                "id": 18,
                "cat": "feeling",
                "catName": "Cảm xúc & Tâm trạng",
                "badge": "Quan trọng",
                "jp": "たいせつ（な）",
                "kana": "たいせつ（な）",
                "kanji": "大切（な）",
                "romaji": "taisetsu(na)",
                "vi": "Quan trọng, đáng quý, trân trọng",
                "exJp": "友だちは 私の 大切な 宝物です。",
                "exVi": "Bạn bè là báu vật vô cùng quý giá của tôi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_892756\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_892756)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💎</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">QUÝ GIÁ</text>\n</svg>"
        },
        {
                "id": 19,
                "cat": "feeling",
                "catName": "Cảm xúc & Tâm trạng",
                "badge": "Trân trọng",
                "jp": "たいせつに します",
                "kana": "たいせつに します",
                "kanji": "大切にします",
                "romaji": "taisetsu ni shimasu",
                "vi": "Trân trọng, giữ gìn cẩn thận",
                "exJp": "いただいた プレゼントを 大切にします。",
                "exVi": "Tôi sẽ trân trọng và giữ gìn cẩn thận món quà này.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_472398\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_472398)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤲</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TRÂN TRỌNG</text>\n</svg>"
        }
],

    "verb_lab": {
        "title": "Phòng Thí Nghiệm Động Từ Trang Phục & Cảm Nghĩ",
        "desc": "Thực hành phân loại chuẩn xác 4 động từ mặc đồ và chuyển đổi câu sang dạng nêu ý kiến (～と思います) hoặc trích dẫn lời nói (～と言っていました):",
        "labels": ["Động từ thể Từ điển", "Thể MASU", "Trang phục ～ています", "Ý kiến ～と思います", "Trích dẫn ～と言っていました"],
        "verbs": [
            {
                "kanji": "着る",
                "masu": "きます",
                "vi": "Mặc (thân trên: áo/kimono/vest)",
                "col2": "着物を着ています",
                "col3": "とても似合うと思います",
                "col4": "着たいと言っていました",
                "col5": "パーティーに着ていきます",
                "ex": "パーティーで素敵な着物を着ている人がいます。"
            },
            {
                "kanji": "履く",
                "masu": "はきます",
                "vi": "Mặc/đi (thân dưới: quần/giày)",
                "col2": "黒い靴を履いています",
                "col3": "スニーカーがいいと思います",
                "col4": "新しいのを履くと言っていました",
                "col5": "歩きやすい靴を履きます",
                "ex": "歩きやすいスニーカーを履いたほうがいいですよ。"
            },
            {
                "kanji": "被る",
                "masu": "かぶります",
                "vi": "Đội (mũ, nón)",
                "col2": "帽子を被っています",
                "col3": "かっこいいと思います",
                "col4": "被りたくないと言っていました",
                "col5": "日傘や帽子を被ります",
                "ex": "日差しが強いので帽子を被ったほうがいいです。"
            },
            {
                "kanji": "掛ける",
                "masu": "かけます",
                "vi": "Đeo (kính mắt)",
                "col2": "眼鏡を掛けています",
                "col3": "よく似合うと思います",
                "col4": "眼鏡を掛けると言っていました",
                "col5": "サングラスを掛けます",
                "ex": "あの眼鏡を掛けている男性は誰ですか。"
            },
            {
                "kanji": "思う",
                "masu": "おもいます",
                "vi": "Nghĩ là, cho là",
                "col2": "そう思っています",
                "col3": "いい考えだと思います",
                "col4": "阿部さんもそう言っていました",
                "col5": "パーティーがいいと思います",
                "ex": "お祝いはみんなでパーティーをするのがいいと思います。"
            }
        ]
    },

    "dialogue": {
        "title": "Bàn Bạc Tổ Chức Tiệc Mừng & Gửi Lời Chúc Mừng",
        "desc": "Thực hành cùng đồng nghiệp lên kế hoạch tổ chức tiệc mừng đám cưới và gửi lời chúc mừng hạnh phúc chân thành nhất:",
        "initial": {
            "avatar": "👨‍💼",
            "name": "Tanaka (Đồng nghiệp)",
            "jp": "阿部さんの結婚のお祝い、どうしましょうか。",
            "vi": "Mừng đám cưới của anh Abe, chúng ta nên làm gì đây nhỉ?"
        },
        "steps": [
            {
                "options": [
                    {
                        "text": "みんなでレストランに集まって、サプライズパーティーをするのがいいと思います。",
                        "vi": "Tôi nghĩ tụi mình tập hợp mọi người ở nhà hàng và làm một bữa tiệc bất ngờ là hay nhất.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "いいですね！阿部さんもみんなとゆっくり話したいと言っていましたよ。",
                        "replyVi": "Ý hay đấy! Anh Abe cũng nói là muốn được ngồi trò chuyện thong thả cùng mọi người mà."
                    },
                    {
                        "text": "お祝いに、みんなで寄せ書きした色紙とプレゼントを渡すのがいいと思います。",
                        "vi": "Tôi nghĩ tụi mình cùng nhau viết thiệp mừng lưu bút và tặng một món quà kỷ niệm là tuyệt nhất.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "温かいアイデアですね！記念に残るものをあげると喜ばれますね。",
                        "replyVi": "Ý tưởng ấm áp quá! Tặng món đồ lưu lại kỷ niệm chắc chắn anh ấy sẽ thích lắm."
                    }
                ]
            },
            {
                "npcName": "Abe",
                "avatar": "🤵",
                "npcText": "皆さん、今日は私のために素敵なパーティーを開いてくれて本当にありがとうございます！",
                "npcVi": "Tất cả mọi người, hôm nay đã vì tôi mà tổ chức bữa tiệc tuyệt vời thế này, thật lòng cảm ơn mọi người!",
                "options": [
                    {
                        "text": "ご結婚、本当におめでとうございます！末永くお幸せに！",
                        "vi": "Chúc mừng đám cưới của anh! Chúc anh chị trăm năm hạnh phúc!",
                        "replyAvatar": "🤵",
                        "replyNpc": "Abe",
                        "replyText": "ありがとうございます！これからもどうぞよろしくお願いします。",
                        "replyVi": "Cảm ơn bạn rất nhiều! Từ nay về sau cũng mong được mọi người tiếp tục giúp đỡ."
                    },
                    {
                        "text": "スーツ姿がとてもかっこいいですね！奥様といつまでも仲良くお過ごしください。",
                        "vi": "Bộ vest hôm nay trông anh bảnh bao lắm! Chúc anh và chị nhà luôn mãi mặn nồng bên nhau nhé.",
                        "replyAvatar": "🤵",
                        "replyNpc": "Abe",
                        "replyText": "褒めてくれて嬉しいです！最高の思い出になりました。",
                        "replyVi": "Được bạn khen tôi mừng quá! Đây thực sự là kỷ niệm tuyệt vời nhất của đời tôi."
                    }
                ]
            }
        ]
    },

    "kanjis": [
        {"char": "先", "hv": "TIÊN", "strokes": 6, "kun": "さき", "on": "SEN", "ex": "先週 (せんしゅう - tuần trước), 先生 (せんせい - giáo viên)", "mnemonic": "Đôi chân bước đi phía TIÊN phong trước mọi người."},
        {"char": "今", "hv": "KIM", "strokes": 4, "kun": "いま", "on": "KON, KIN", "ex": "今月 (こんげつ - tháng này), 今年 (ことし - năm nay)", "mnemonic": "Cái nón úp ngay thời khắc KIM hiện tại này."},
        {"char": "来", "hv": "LAI", "strokes": 7, "kun": "く-る、き-ます", "on": "RAI", "ex": "来年 (らいねん - năm sau), 来月 (らいげつ - tháng sau)", "mnemonic": "Cây lúa trĩu bông từ tương LAI mang mùa màng tới."},
        {"char": "年", "hv": "NIÊN", "strokes": 6, "kun": "とし", "on": "NEN", "ex": "今年 (ことし - năm nay), 去年 (きょねん - năm ngoái)", "mnemonic": "Vác bó lúa vàng gặt hái sau một NIÊN năm ròng rã."},
        {"char": "去", "hv": "KHỨ", "strokes": 5, "kun": "さ-る", "on": "KYO, KO", "ex": "去年 (きょねん - năm ngoái), 過去 (かこ - quá khứ)", "mnemonic": "Chôn sâu xuống đất (土) những gì đã qua trong quá KHỨ."},
        {"char": "家", "hv": "GIA", "strokes": 10, "kun": "いえ、や", "on": "KA", "ex": "家族 (かぞく - gia đình), 家 (いえ - ngôi nhà)", "mnemonic": "Dưới mái nhà (宀) có nuôi chú heo (豕) ấm cúng tình GIA đình."},
        {"char": "思", "hv": "TƯ", "strokes": 9, "kun": "おも-う", "on": "SHI", "ex": "思います (おもいます - suy nghĩ), 思い出 (おもいで - kỷ niệm)", "mnemonic": "Ruộng đồng (田) luôn đọng lại trong trái tim (心) người mang TƯ tưởng hoài niệm."}
    ],

    "quizzes": [
        {"id": 1, "category": "Ngữ pháp: ～と思います", "q": "お祝いは パーティーが [____] と 思います。", "options": ["いい", "よく", "いいだ", "よかったに"], "correct": 0, "explain": "Tính từ đuôi い ở thể Thông thường (Futsuukei): いい ➔ 「いいと思います」 (Tôi nghĩ là hay nhất)."},
        {"id": 2, "category": "Ngữ pháp: ～と思います", "q": "プレゼントを あげたら、きっと [____] と 思います。", "options": ["喜ぶ", "喜び", "喜んで", "喜ばないで"], "correct": 0, "explain": "Động từ thể Từ điển (Thể thông thường) + と思います ➔ 「喜ぶと思います」 (Tôi nghĩ bạn ấy sẽ vui)."},
        {"id": 3, "category": "Ngữ pháp: ～と言っていました", "q": "阿部さんは みんなと [____] と 言っていました。", "options": ["話したい", "話します", "話して", "話したかったに"], "correct": 0, "explain": "Trích dẫn lời nói thể thông thường: 話したい ➔ 「話したいと言っていました」 (Nói rằng muốn trò chuyện)."},
        {"id": 4, "category": "Từ vựng: Động từ mặc trang phục", "q": "田中さんは きれいな 着物を [____] います。", "options": ["着て (きて)", "履いて (はいて)", "被って (かぶって)", "掛けて (かけて)"], "correct": 0, "explain": "Kimono mặc trên thân người dùng động từ 「着ます」 ➔ 「着ています」."},
        {"id": 5, "category": "Từ vựng: Động từ đi giày/quần", "q": "新しい スニーカーを [____] います。", "options": ["履いて (はいて)", "着て (きて)", "被って (かぶって)", "掛けて (かけて)"], "correct": 0, "explain": "Giày dép, quần tất ở phần thân dưới dùng động từ 「履きます」 ➔ 「履いています」."},
        {"id": 6, "category": "Từ vựng: Đội mũ", "q": "白い 帽子を [____] います。", "options": ["被って (かぶって)", "着て (きて)", "履いて (はいて)", "掛けて (かけて)"], "correct": 0, "explain": "Mũ nón trên đầu dùng động từ 「被ります」 (かぶります) ➔ 「被っています」."},
        {"id": 7, "category": "Từ vựng: Đeo kính", "q": "黒い 眼鏡を [____] います。", "options": ["掛けて (かけて)", "着て (きて)", "履いて (はいて)", "被って (かぶって)"], "correct": 0, "explain": "Kính mắt dùng động từ 「掛けます」 (かけます) ➔ 「掛けています」."},
        {"id": 8, "category": "Giao tiếp: Chúc mừng đám cưới", "q": "Lời chúc mừng đám cưới trang trọng nhất trong tiếng Nhật là:", "options": ["ご結婚、おめでとうございます！", "お大事に！", "いってらっしゃい！", "ごちそうさまでした！"], "correct": 0, "explain": "「ご結婚、おめでとうございます！」 nghĩa là Xin chúc mừng đám cưới của bạn!"},
        {"id": 9, "category": "Từ vựng: Thời gian", "q": "「きょねん」 (Năm ngoái) được viết bằng cặp chữ Hán nào?", "options": ["去年", "今年", "来年", "先年"], "correct": 0, "explain": "Năm ngoái là 「去年」 (KHỨ NIÊN)."},
        {"id": 10, "category": "Từ vựng: Thời gian", "q": "「らいねん」 (Năm sau) được viết bằng cặp chữ Hán nào?", "options": ["来年", "今年", "去年", "先年"], "correct": 0, "explain": "Năm sau là 「来年」 (LAI NIÊN)."},
        {"id": 11, "category": "Chữ Hán Bài 18: 思 (Tư)", "q": "Động từ 「おもいます」 (Suy nghĩ, cho là) có chữ Hán là:", "options": ["思います", "言います", "行きます", "話します"], "correct": 0, "explain": "「おもいます」 viết là 「思います」 (chữ TƯ - 9 nét, bộ Điền 田 + bộ Tâm 心)."},
        {"id": 12, "category": "Chữ Hán Bài 18: 先 (Tiên)", "q": "Từ 「せんしゅう」 (Tuần trước) có chữ Hán đầu tiên là:", "options": ["先", "今", "来", "去"], "correct": 0, "explain": "「せんしゅう」 là 「先週」 (TIÊN CHU - chữ 先 có 6 nét)."},
        {"id": 13, "category": "Chữ Hán Bài 18: 今 (Kim)", "q": "Từ 「ことし」 (Năm nay) có chữ Hán đầu tiên là:", "options": ["今", "先", "来", "去"], "correct": 0, "explain": "「ことし」 viết là 「今年」 (KIM NIÊN - chữ 今 có 4 nét)."},
        {"id": 14, "category": "Chữ Hán Bài 18: 家 (Gia)", "q": "Từ 「かぞく」 (Gia đình) có chữ Hán đầu tiên là:", "options": ["家", "思", "先", "来"], "correct": 0, "explain": "「かぞく」 viết là 「家族」 (GIA TỘC - chữ 家 có 10 nét)."},
        {"id": 15, "category": "Chữ Hán Bài 18: 着 (Trước)", "q": "Từ 「きもの」 (Trang phục truyền thống Kimono) viết chữ Hán là:", "options": ["着物", "履物", "被物", "掛物"], "correct": 0, "explain": "Kimono viết chữ Hán là 「着物」 (TRƯỚC VẬT - chữ 着 12 nét và chữ 物 8 nét)."}
    ]
}
