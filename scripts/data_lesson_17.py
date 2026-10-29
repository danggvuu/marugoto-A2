# -*- coding: utf-8 -*-
"""
Data for Marugoto A2-2 Lesson 17:
Topic 9: お祝い (Chúc mừng & Kỷ niệm)
Bài 17: Quà Tặng & Dịp Kỷ Niệm (誕生日に彼にもらったんです)
"""

def make_svg(title, emoji, c1="#ec4899", c2="#be185d"):
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

CFG_17 = {
    "num": 17,
    "title_vi": "Quà Tặng & Kỷ Niệm",
    "title_jp": "誕生日に彼にもらったんです",
    "topic_name": "Chúc Mừng & Kỷ Niệm (お祝い)",
    "topic_badge": "TOPIC 9: お祝い • BÀI 17",
    "desc": "Làm chủ cặp động từ Cho - Nhận quà tặng kinh điển (あげます / もらいます), cách chia sẻ về nguồn gốc kỷ vật với cấu trúc ～んです, kỹ năng liệt kê gợi ý quà tặng với ～とか, mệnh đề định ngữ miêu tả đồ vật (部屋に飾るもの) và hiểu sâu văn hóa tặng quà của người Nhật.",

    "grammars": [
        {
            "title": "Nhận quà từ ai đó: N(người) に N(vật) を もらいました",
            "icon": "🎁",
            "tag": "Nhận quà & Kỷ vật",
            "color": "#ec4899",
            "color_dark": "#be185d",
            "intro": "Dùng khi người nói nhận được một món quà ý nghĩa hoặc kỷ vật từ người khác vào các dịp đặc biệt (sinh nhật, tốt nghiệp, kết hôn).",
            "formula": "Watashi wa [Người tặng] に [Món quà] を もらいました / もらったんです",
            "meaning": "Tôi đã nhận được món quà này từ... (khi được khen ngợi đồ đạc, dùng もらったんです để giải thích nguồn gốc).",
            "examples": [
                {"jp": "その ネックレス、とても 素敵ですね。―― 誕生日に 彼に もらったんです。", "vi": "Sợi dây chuyền đó đẹp quá nhỉ! ―― Tôi được bạn trai tặng vào ngày sinh nhật đấy."},
                {"jp": "卒業の お祝いに、両親に 時計を もらいました。", "vi": "Vào dịp mừng tốt nghiệp, tôi được bố mẹ tặng cho một chiếc đồng hồ."},
                {"jp": "この 本は 日本の 先生に もらった 大切な 本です。", "vi": "Cuốn sách này là cuốn sách quý tôi được một giáo viên Nhật Bản tặng."}
            ]
        },
        {
            "title": "Tặng quà cho ai đó: N(người) に N(vật) を あげます",
            "icon": "💐",
            "tag": "Trao tặng quà mừng",
            "color": "#059669",
            "color_dark": "#047857",
            "intro": "Dùng khi người nói tặng quà hoặc làm điều gì chúc mừng người khác.",
            "formula": "Watashi wa [Người nhận] に [Món quà] を あげます / あげました",
            "meaning": "Tôi tặng... cho ai đó.",
            "table": {
                "headers": ["Dịp kỷ niệm", "Người nhận quà", "Câu hoàn chỉnh với あげます"],
                "rows": [
                    ["母の日 (Ngày của Mẹ)", "母に", "母の日に きれいな 花を あげます。"],
                    ["誕生日 (Sinh nhật)", "友達に", "友達の 誕生日に ケーキを あげました。"],
                    ["結婚祝い (Mừng cưới)", "先輩に", "結婚の お祝いに コーヒーカップを あげます。"],
                    ["子どもの日 (Tết thiếu nhi)", "子どもに", "おもちゃを あげます。"]
                ]
            },
            "examples": [
                {"jp": "結婚の お祝いに 何を あげますか。", "vi": "Vào dịp mừng đám cưới bạn sẽ tặng quà gì?"},
                {"jp": "父の日に ネクタイを あげました。", "vi": "Vào Ngày của Cha tôi đã tặng cà vạt cho bố."},
                {"jp": "子どもたちの 入学祝いに 新しい かばんを あげます。", "vi": "Tôi tặng cặp sách mới làm quà mừng các con vào năm học mới."}
            ]
        },
        {
            "title": "Liệt kê đại diện とか & Định ngữ: V-る + もの",
            "icon": "🖼️",
            "tag": "Gợi ý quà tặng",
            "color": "#7c3aed",
            "color_dark": "#5b21b6",
            "intro": "Dùng để gợi ý vài món quà tiêu biểu (như là A hay B gì đó...) hoặc dùng động từ bổ nghĩa cho danh từ chỉ vật để diễn tả loại quà muốn tặng.",
            "formula": "N1 とか N2 とか (như là... hay là...)<br>[Động từ thể Từ điển] + もの (đồ để làm gì đó)",
            "meaning": "Tặng những thứ như tranh hay đồng hồ; những đồ vật trang trí trong phòng.",
            "examples": [
                {"jp": "日本では 結婚の お祝いに 絵とか 時計を あげます。", "vi": "Ở Nhật Bản vào dịp đám cưới người ta thường tặng những thứ như tranh hoặc đồng hồ."},
                {"jp": "部屋に 飾る ものが いいと 思いますよ。", "vi": "Tôi nghĩ đồ dùng để trang trí trong phòng thì sẽ rất hay đấy."},
                {"jp": "料理のときに 使う ものを プレゼントしました。", "vi": "Tôi đã tặng những món đồ dùng khi nấu nướng."}
            ]
        }
    ],

    "vocab": [
        {
                "id": 1,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Quà chúc mừng",
                "jp": "おいわい",
                "kana": "おいわい",
                "kanji": "お祝い",
                "romaji": "oiwai",
                "vi": "Chúc mừng",
                "exJp": "結婚の お祝いを あげました。",
                "exVi": "Tôi đã tặng quà chúc mừng đám cưới.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_509465\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_509465)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎉</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHÚC MỪNG</text>\n</svg>"
        },
        {
                "id": 2,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Nhập học",
                "jp": "にゅうがく",
                "kana": "にゅうがく",
                "kanji": "入学",
                "romaji": "nyuugaku",
                "vi": "Nhập học",
                "exJp": "大学の 入学式に 出席しました。",
                "exVi": "Tham dự lễ nhập học đại học.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_537589\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_537589)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎓</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NHẬP HỌC</text>\n</svg>"
        },
        {
                "id": 3,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Tốt nghiệp ra trường",
                "jp": "そつぎょう",
                "kana": "そつぎょう",
                "kanji": "卒業",
                "romaji": "sotsugyou",
                "vi": "Tốt nghiệp",
                "exJp": "高校を 卒業しました。",
                "exVi": "Tôi đã tốt nghiệp trường cấp ba.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_248631\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_248631)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📜</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TỐT NGHIỆP</text>\n</svg>"
        },
        {
                "id": 4,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Bắt đầu đi làm",
                "jp": "しゅうしょく",
                "kana": "しゅうしょく",
                "kanji": "就職",
                "romaji": "shuushoku",
                "vi": "Bắt đầu đi làm",
                "exJp": "会社に 就職が 決まりました。",
                "exVi": "Tôi đã xin được việc làm tại công ty.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_931918\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_931918)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💼</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐI LÀM</text>\n</svg>"
        },
        {
                "id": 5,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Sinh em bé",
                "jp": "しゅっさん",
                "kana": "しゅっさん",
                "kanji": "出産",
                "romaji": "shussan",
                "vi": "Sinh con",
                "exJp": "出産の お祝いを えらびます。",
                "exVi": "Chọn quà chúc mừng bạn sinh em bé.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_356176\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_356176)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">SINH CON</text>\n</svg>"
        },
        {
                "id": 6,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Em bé sơ sinh",
                "jp": "あかちゃん",
                "kana": "あかちゃん",
                "kanji": "赤ちゃん",
                "romaji": "akachan",
                "vi": "Em bé",
                "exJp": "かわいい 赤ちゃんが 生まれました。",
                "exVi": "Một em bé kháu khỉnh vừa chào đời.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_752284\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_752284)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">EM BÉ</text>\n</svg>"
        },
        {
                "id": 7,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Được sinh ra",
                "jp": "うまれます",
                "kana": "うまれます",
                "kanji": "生まれます",
                "romaji": "umaremasu",
                "vi": "Được sinh ra",
                "exJp": "先月 子どもが 生まれました。",
                "exVi": "Tháng trước con tôi đã chào đời.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_640263\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_640263)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🐣</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">SINH RA</text>\n</svg>"
        },
        {
                "id": 8,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Kết hôn",
                "jp": "けっこん",
                "kana": "けっこん",
                "kanji": "結婚",
                "romaji": "kekkon",
                "vi": "Kết hôn",
                "exJp": "ふたりは 来年 結婚します。",
                "exVi": "Hai người họ sẽ kết hôn vào năm tới.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_636456\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_636456)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💍</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KẾT HÔN</text>\n</svg>"
        },
        {
                "id": 9,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Ngày của Mẹ (CN tuần 2 tháng 5)",
                "jp": "ははの ひ",
                "kana": "ははの ひ",
                "kanji": "母の日",
                "romaji": "haha no hi",
                "vi": "Ngày của mẹ (Chủ nhật thứ 2 của tháng 5)",
                "exJp": "母の日に カーネーションを 贈ります。",
                "exVi": "Tặng hoa cẩm chướng vào Ngày của Mẹ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_293873\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_293873)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👩</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NGÀY CỦA MẸ</text>\n</svg>"
        },
        {
                "id": 10,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Ngày của Bố (CN tuần 3 tháng 6)",
                "jp": "ちちの ひ",
                "kana": "ちちの ひ",
                "kanji": "父の日",
                "romaji": "chichi no hi",
                "vi": "Ngày của bố (Chủ nhật thứ 3 của tháng 6)",
                "exJp": "父の日に ネクタイを プレゼントします。",
                "exVi": "Tặng cà vạt cho bố nhân Ngày của Cha.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_32517\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_32517)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👨</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NGÀY CỦA BỐ</text>\n</svg>"
        },
        {
                "id": 11,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Lễ Giáng sinh (Christmas)",
                "jp": "クリスマス",
                "kana": "クリスマス",
                "kanji": "クリスマス",
                "romaji": "kurisumasu",
                "vi": "Giáng sinh",
                "exJp": "クリスマスに ケーキを 食べます。",
                "exVi": "Ăn bánh kem vào dịp Giáng sinh.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_245874\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_245874)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎄</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GIÁNG SINH</text>\n</svg>"
        },
        {
                "id": 12,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Ngày lễ tình nhân Valentine",
                "jp": "バレンタイン・デー",
                "kana": "バレンタイン・デー",
                "kanji": "バレンタインデー",
                "romaji": "barentain dee",
                "vi": "Ngày Valentine",
                "exJp": "バレンタインデーに チョコを あげます。",
                "exVi": "Tặng sô-cô-la vào ngày Valentine.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_188241\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_188241)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍫</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VALENTINE</text>\n</svg>"
        },
        {
                "id": 13,
                "cat": "gift",
                "catName": "Quà tặng & Đồ dùng",
                "badge": "Vòng cổ",
                "jp": "ネックレス",
                "kana": "ネックレス",
                "kanji": "ネックレス",
                "romaji": "nekkuresu",
                "vi": "Vòng cổ",
                "exJp": "きれいな ネックレスを もらいました。",
                "exVi": "Tôi nhận được sợi dây chuyền rất đẹp.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_41906\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_41906)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📿</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VÒNG CỔ</text>\n</svg>"
        },
        {
                "id": 14,
                "cat": "gift",
                "catName": "Quà tặng & Đồ dùng",
                "badge": "Áo len ấm mùa đông (Sweater)",
                "jp": "セーター",
                "kana": "セーター",
                "kanji": "セーター",
                "romaji": "seetaa",
                "vi": "Áo len",
                "exJp": "あたたかい セーターを 着ています。",
                "exVi": "Đang mặc một chiếc áo len ấm áp.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_220382\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_220382)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🧶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ÁO LEN</text>\n</svg>"
        },
        {
                "id": 15,
                "cat": "gift",
                "catName": "Quà tặng & Đồ dùng",
                "badge": "Đồ chơi trẻ em",
                "jp": "おもちゃ",
                "kana": "おもちゃ",
                "kanji": "おもちゃ",
                "romaji": "omocha",
                "vi": "Đồ chơi",
                "exJp": "子どもに おもちゃを 買いました。",
                "exVi": "Mua đồ chơi tặng cho con.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_854000\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_854000)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🧸</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐỒ CHƠI</text>\n</svg>"
        },
        {
                "id": 16,
                "cat": "gift",
                "catName": "Quà tặng & Đồ dùng",
                "badge": "Đồ đan len thủ công",
                "jp": "あみもの",
                "kana": "あみもの",
                "kanji": "編み物",
                "romaji": "amimono",
                "vi": "Đồ đan len",
                "exJp": "母の 手編みの 編み物です。",
                "exVi": "Đây là đồ đan len bằng tay của mẹ tôi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_361822\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_361822)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🧶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐỒ ĐAN LEN</text>\n</svg>"
        },
        {
                "id": 17,
                "cat": "gift",
                "catName": "Quà tặng & Đồ dùng",
                "badge": "Búp bê trang trí",
                "jp": "にんぎょう",
                "kana": "にんぎょう",
                "kanji": "人形",
                "romaji": "ningyou",
                "vi": "Búp bê",
                "exJp": "日本の 伝統的な 人形です。",
                "exVi": "Đây là búp bê truyền thống của Nhật Bản.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_919561\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_919561)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎎</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BÚP BÊ</text>\n</svg>"
        },
        {
                "id": 18,
                "cat": "action",
                "catName": "Hành động & Sử dụng",
                "badge": "Mặc (áo sơ mi",
                "jp": "（シャツを）きます",
                "kana": "（シャツを）きます",
                "kanji": "（シャツを）着ます",
                "romaji": "kimasu",
                "vi": "Mặc (áo)",
                "exJp": "新しい シャツを 着て 行きます。",
                "exVi": "Mặc chiếc áo mới rồi đi dự tiệc.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_329686\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_329686)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👔</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MẶC ÁO</text>\n</svg>"
        },
        {
                "id": 19,
                "cat": "action",
                "catName": "Hành động & Sử dụng",
                "badge": "Trang trí trong phòng",
                "jp": "へやに かざります",
                "kana": "へやに かざります",
                "kanji": "部屋に飾ります",
                "romaji": "heya ni kazarimasu",
                "vi": "Trang trí trong phòng",
                "exJp": "絵を 部屋に 飾ります。",
                "exVi": "Treo tranh trang trí trong phòng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_536289\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_536289)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🖼️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TRANG TRÍ</text>\n</svg>"
        },
        {
                "id": 20,
                "cat": "action",
                "catName": "Hành động & Sử dụng",
                "badge": "Sử dụng trong công việc",
                "jp": "しごとで つかいます",
                "kana": "しごとで つかいます",
                "kanji": "仕事で使います",
                "romaji": "shigoto de tsukaimasu",
                "vi": "Sử dụng trong công việc",
                "exJp": "このペンは 仕事で 使います。",
                "exVi": "Cây bút này tôi sử dụng trong công việc.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_507532\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_507532)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🖋️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">DÙNG ĐI LÀM</text>\n</svg>"
        },
        {
                "id": 21,
                "cat": "action",
                "catName": "Hành động & Sử dụng",
                "badge": "Rất hợp",
                "jp": "にあいます",
                "kana": "にあいます",
                "kanji": "似合います",
                "romaji": "niaimasu",
                "vi": "~ hợp",
                "exJp": "その色の 服が よく 似合いますね。",
                "exVi": "Bộ quần áo màu đó rất hợp với bạn đấy.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_677214\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_677214)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">✨</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">RẤT HỢP</text>\n</svg>"
        },
        {
                "id": 22,
                "cat": "action",
                "catName": "Hành động & Sử dụng",
                "badge": "Vui chơi giải trí",
                "jp": "あそびます",
                "kana": "あそびます",
                "kanji": "遊びます",
                "romaji": "asobimasu",
                "vi": "Chơi",
                "exJp": "休みの日は 友だちと 遊びます。",
                "exVi": "Ngày nghỉ tôi đi chơi cùng bạn bè.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_536741\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_536741)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎮</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VUI CHƠI</text>\n</svg>"
        },
        {
                "id": 23,
                "cat": "action",
                "catName": "Hành động & Sử dụng",
                "badge": "Ưa thích",
                "jp": "きに いります",
                "kana": "きに いります",
                "kanji": "気に入ります",
                "romaji": "kini irimasu",
                "vi": "Thích",
                "exJp": "このプレゼント、とても 気に入りました。",
                "exVi": "Món quà này tôi ưng ý vô cùng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_372567\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_372567)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💖</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ƯA THÍCH</text>\n</svg>"
        },
        {
                "id": 24,
                "cat": "expr",
                "catName": "Cụm từ liên kết",
                "badge": "Chẳng hạn như ~ như là ~",
                "jp": "～とか～とか",
                "kana": "～とか～とか",
                "kanji": "～とか～とか",
                "romaji": "~toka ~toka",
                "vi": "Chẳng hạn như ~ như ~",
                "exJp": "花とか お菓子とかを 買いました。",
                "exVi": "Tôi đã mua chẳng hạn như hoa tươi và bánh kẹo.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_701445\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_701445)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🔗</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHẲNG HẠN NHƯ</text>\n</svg>"
        },
        {
                "id": 25,
                "cat": "gift",
                "catName": "Quà tặng & Đồ dùng",
                "badge": "Hộp đựng danh thiếp lịch sự",
                "jp": "めいしいれ",
                "kana": "めいしいれ",
                "kanji": "名刺入れ",
                "romaji": "meishiire",
                "vi": "Hộp đựng danh thiếp",
                "exJp": "革の 名刺入れを 贈りました。",
                "exVi": "Tôi đã tặng hộp đựng danh thiếp bằng da.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_715881\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_715881)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💳</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">HỘP DANH THIẾP</text>\n</svg>"
        },
        {
                "id": 26,
                "cat": "gift",
                "catName": "Quà tặng & Đồ dùng",
                "badge": "Đồ đôi",
                "jp": "ペア",
                "kana": "ペア",
                "kanji": "ペア",
                "romaji": "pea",
                "vi": "Cặp, đôi",
                "exJp": "ペアの マグカップを プレゼントします。",
                "exVi": "Tặng cặp cốc uống nước đôi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_549980\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_549980)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">☕☕</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CẶP ĐÔI</text>\n</svg>"
        },
        {
                "id": 27,
                "cat": "expr",
                "catName": "Cụm từ liên kết",
                "badge": "Giống nhau y hệt",
                "jp": "おなじ",
                "kana": "おなじ",
                "kanji": "同じ",
                "romaji": "onaji",
                "vi": "Giống",
                "exJp": "彼と 同じ時計を 持っています。",
                "exVi": "Tôi đeo đồng hồ giống y hệt anh ấy.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_734368\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_734368)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👥</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GIỐNG NHAU</text>\n</svg>"
        },
        {
                "id": 28,
                "cat": "expr",
                "catName": "Cụm từ liên kết",
                "badge": "Ví dụ như là...",
                "jp": "たとえば",
                "kana": "たとえば",
                "kanji": "例えば",
                "romaji": "tatoeba",
                "vi": "Ví dụ",
                "exJp": "例えば 写真立てなど どうですか。",
                "exVi": "Ví dụ như khung ảnh thì bạn thấy sao?",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_862107\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_862107)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💡</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VÍ DỤ</text>\n</svg>"
        },
        {
                "id": 29,
                "cat": "event",
                "catName": "Sự kiện & Dịp lễ",
                "badge": "Tập quán",
                "jp": "しゅうかん",
                "kana": "しゅうかん",
                "kanji": "習慣",
                "romaji": "shuukan",
                "vi": "Thói quen",
                "exJp": "日本の 贈り物の 習慣を 学びます。",
                "exVi": "Học hỏi về phong tục tặng quà của người Nhật.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_928341\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_928341)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎎</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">PHONG TỤC</text>\n</svg>"
        }
],

    "verb_lab": {
        "title": "Phòng Thí Nghiệm Động Từ Cho - Nhận & Kỷ Niệm",
        "desc": "Thực hành chuyển đổi các động từ Cho - Nhận (あげます - もらいます - くれます) và các động từ đi kèm trong các dịp lễ kỷ niệm:",
        "labels": ["Động từ thể Từ điển", "Thể MASU", "あげます (Tặng ai)", "もらいました (Nhận từ ai)", "Dịp kỷ niệm"],
        "verbs": [
            {
                "kanji": "あげる",
                "masu": "あげます",
                "vi": "Tặng cho người khác",
                "col2": "友達にあげます",
                "col3": "花をあげました",
                "col4": "先生にもらいました",
                "col5": "誕生日にあげます",
                "ex": "母の日にきれいなカーネーションをあげました。"
            },
            {
                "kanji": "もらう",
                "masu": "もらいます",
                "vi": "Nhận từ người khác",
                "col2": "彼にもらいました",
                "col3": "プレゼントをもらった",
                "col4": "家族にあげます",
                "col5": "結婚祝いにもらいました",
                "ex": "誕生日に彼に素敵なネックレスをもらったんです。"
            },
            {
                "kanji": "贈る",
                "masu": "おくります",
                "vi": "Trao tặng trang trọng",
                "col2": "時計を贈ります",
                "col3": "お祝いを贈りました",
                "col4": "本を贈られました",
                "col5": "卒業のお祝いに贈ります",
                "ex": "結婚のお祝いに素敵な絵を贈ります。"
            },
            {
                "kanji": "飾る",
                "masu": "かざります",
                "vi": "Trang trí trong phòng",
                "col2": "部屋に飾ります",
                "col3": "絵を飾りました",
                "col4": "飾るものをもらいました",
                "col5": "新居に飾る絵",
                "ex": "新築祝いに部屋に飾る絵をもらいました。"
            },
            {
                "kanji": "祝う",
                "masu": "いわいます",
                "vi": "Chúc mừng, ăn mừng",
                "col2": "誕生日を祝います",
                "col3": "お祝いをあげます",
                "col4": "みんなに祝われました",
                "col5": "ご結婚のお祝い",
                "ex": "友達の結婚をみんなで心から祝います。"
            }
        ]
    },

    "dialogue": {
        "title": "Hỏi Nguồn Gốc Món Quà & Tư Vấn Quà Cưới",
        "desc": "Thực hành đối thoại khi đồng nghiệp trầm trồ khen ngợi món phụ kiện bạn đang đeo và xin lời khuyên về món quà cưới phù hợp văn hóa Nhật:",
        "initial": {
            "avatar": "👩‍💼",
            "name": "Kobayashi (Đồng nghiệp)",
            "jp": "その腕時計、すごくおしゃれですね！どこで買ったんですか。",
            "vi": "Chiếc đồng hồ đeo tay đó sành điệu và đẹp quá! Bạn mua ở đâu thế?"
        },
        "steps": [
            {
                "options": [
                    {
                        "text": "ありがとうございます！実は、先週の誕生日に彼にもらったんです。",
                        "vi": "Cảm ơn bạn! Thực ra là tôi được bạn trai tặng vào ngày sinh nhật tuần trước đấy.",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kobayashi",
                        "replyText": "彼からのプレゼントですか！とても似合っていますよ。羨ましいです。",
                        "replyVi": "Quà bạn trai tặng ư! Trông hợp với bạn lắm luôn. Ghen tị thật đấy."
                    },
                    {
                        "text": "自分で買ったんじゃなくて、大学の卒業祝いに両親にもらったんです。",
                        "vi": "Không phải tôi tự mua đâu, mà tôi được bố mẹ tặng làm quà mừng tốt nghiệp đại học đấy.",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kobayashi",
                        "replyText": "ご両親からの記念の品なんですね。ずっと大切に使えますね！",
                        "replyVi": "Kỷ vật từ bố mẹ tặng ý nghĩa quá. Bạn có thể giữ gìn và dùng suốt đời được đấy!"
                    }
                ]
            },
            {
                "npcName": "Kobayashi",
                "avatar": "👩‍💼",
                "npcText": "来月、佐藤先輩の結婚式があるんですが、日本のお祝いには何をあげればいいでしょうか。",
                "npcVi": "Tháng sau có đám cưới của tiền bối Sato, theo phong tục Nhật thì nên tặng quà gì thì hợp lý nhỉ?",
                "options": [
                    {
                        "text": "そうですね、おしゃれなペアのコーヒーカップとか、部屋に飾る絵がいいと思いますよ。",
                        "vi": "Theo tôi thì một bộ tách cà phê đôi xinh xắn hoặc bức tranh trang trí trong phòng sẽ rất tuyệt đấy.",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kobayashi",
                        "replyText": "ペアカップ！素敵ですね。二人で毎日使ってもらえそうです。探してみます！",
                        "replyVi": "Cốc đôi ư! Hay quá. Hai vợ chồng có thể dùng cùng nhau mỗi ngày. Tôi sẽ đi tìm thử!"
                    },
                    {
                        "text": "料理が好きな先輩ですから、料理のときに使う上質な鍋や食器はどうですか。",
                        "vi": "Vì chị Sato thích nấu ăn, nên những đồ dùng khi nấu nướng như bộ nồi hay chén đĩa cao cấp thì sao?",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kobayashi",
                        "replyText": "さすが！実用的で絶対に喜んでくれますね。アドバイスありがとう！",
                        "replyVi": "Quả đúng là bạn! Rất thiết thực và chị ấy chắc chắn sẽ thích mê. Cảm ơn bạn nhiều nhé!"
                    }
                ]
            }
        ]
    },

    "kanjis": [
        {"char": "祝", "hv": "CHÚC", "strokes": 9, "kun": "いわ-う", "on": "SHUKU", "ex": "お祝い (おいわい - chúc mừng/quà mừng), 祝日 (しゅくじつ - ngày lễ)", "mnemonic": "Thần linh (礻) lắng nghe người anh trai (兄) cất lời CHÚC phúc."},
        {"char": "誕", "hv": "ĐẢN", "strokes": 15, "kun": "-", "on": "TAN", "ex": "誕生日 (たんじょうび - ngày sinh nhật)", "mnemonic": "Dùng lời nói (言) kéo dài (延) lời ca ngợi ngày sinh ĐẢN."},
        {"char": "結", "hv": "KẾT", "strokes": 12, "kun": "むす-ぶ", "on": "KEK", "ex": "結婚 (けっこん - kết hôn), 結果 (けっか - kết quả)", "mnemonic": "Sợi chỉ (糸) kết thành sợi dây cát tường (吉) KẾT nối lương duyên."},
        {"char": "婚", "hv": "HÔN", "strokes": 11, "kun": "-", "on": "KON", "ex": "結婚 (けっこん - kết hôn), 新婚 (しんこん - tân hôn)", "mnemonic": "Người phụ nữ (女) trong buổi chiều tà (昏) bước vào ngày HÔN lễ."},
        {"char": "絵", "hv": "HỘI", "strokes": 12, "kun": "-", "on": "E, KAI", "ex": "絵 (え - bức tranh), 絵画 (かいが - hội họa)", "mnemonic": "Sợi tơ lụa (糸) được hội họp (会) muôn màu sắc vẽ nên bức HỘI họa."},
        {"char": "写", "hv": "TẢ", "strokes": 5, "kun": "うつ-す", "on": "SHA", "ex": "写真 (しゃしん - bức ảnh), 描写 (びょうしゃ - miêu tả)", "mnemonic": "Dưới mái che (冖) chụp một nét ngang đứng miêu TẢ chân dung."},
        {"char": "真", "hv": "CHÂN", "strokes": 10, "kun": "ま", "on": "SHIN", "ex": "写真 (しゃしん - bức ảnh), 真実 (しんじつ - sự thật)", "mnemonic": "Mười (十) con mắt (目) cùng nhìn thấu CHÂN tướng sự thật."},
        {"char": "計", "hv": "KẾ", "strokes": 9, "kun": "はか-る", "on": "KEI", "ex": "時計 (とけい - đồng hồ), 計画 (けいかく - kế hoạch)", "mnemonic": "Lời nói (言) đếm đủ mười (十) điều lập nên KẾ sách, đồng hồ đo đạc."}
    ],

    "quizzes": [
        {"id": 1, "category": "Ngữ pháp: もらいました", "q": "誕生日に 彼 [____] 素敵な ネックレスを もらいました。", "options": ["に", "を", "で", "が"], "correct": 0, "explain": "Nhận cái gì từ ai: [Người tặng] + に もらいました (Nhận từ bạn trai)."},
        {"id": 2, "category": "Ngữ pháp: あげます", "q": "母の日に お母さん [____] きれいな 花を あげます。", "options": ["に", "を", "と", "から"], "correct": 0, "explain": "Tặng quà cho ai: [Người nhận] + に あげます (Tặng cho mẹ)."},
        {"id": 3, "category": "Ngữ pháp: ～んです giải thích nguồn gốc", "q": "「その 時計、素敵ですね。」――「父に [____] んです。」", "options": ["もらった", "もらう", "もらって", "あげた"], "correct": 0, "explain": "Động từ thể Quá khứ ngắn (Thể た) + んです: もらった ➔ 「もらったんです」 (Tôi được bố tặng đấy)."},
        {"id": 4, "category": "Ngữ pháp: Liệt kê ～とか", "q": "結婚の お祝いに 絵 [____] 時計 [____] あげます。", "options": ["とか / とか", "ても / ても", "たり / たり", "など / など"], "correct": 0, "explain": "Liệt kê các danh từ đại diện: 「N1 とか N2 とか」 (Như là tranh, như là đồng hồ)."},
        {"id": 5, "category": "Ngữ pháp: Định ngữ V-る + もの", "q": "新居の 部屋に [____] ものを プレゼントしたいです。", "options": ["飾る", "飾って", "飾った", "飾り"], "correct": 0, "explain": "Mệnh đề bổ nghĩa cho danh từ chỉ vật: V thể Từ điển + もの ➔ 「飾るもの」 (Đồ dùng để trang trí)."},
        {"id": 6, "category": "Từ vựng: Lễ hội & Kỷ niệm", "q": "12月25日の お祝いは [____] です。", "options": ["クリスマス", "バレンタイン・デー", "母の日", "父の日"], "correct": 0, "explain": "Ngày lễ 25 tháng 12 là Giáng sinh: 「クリスマス」 (Christmas)."},
        {"id": 7, "category": "Từ vựng: Lễ hội", "q": "2月14日に チョコレートを あげる 日は [____] です。", "options": ["バレンタイン・デー", "クリスマス", "誕生日", "入学"], "correct": 0, "explain": "Ngày 14 tháng 2 tặng sô-cô-la là Valentine: 「バレンタイン・デー」."},
        {"id": 8, "category": "Từ vựng: Sự kiện", "q": "学校の 勉強を 全部 終えて 出る ことを [____] と 言います。", "options": ["卒業 (そつぎょう)", "入学 (にゅうがく)", "就職 (しゅうしょく)", "結婚 (けっこん)"], "correct": 0, "explain": "Hoàn thành việc học và ra trường là 「卒業」 (そつぎょう - Tốt nghiệp)."},
        {"id": 9, "category": "Từ vựng: Quà tặng", "q": "時間を 知る ための 道具は [____] です。", "options": ["時計 (とけい)", "写真 (しゃしん)", "絵 (え)", "おもちゃ"], "correct": 0, "explain": "Dụng cụ để xem giờ là đồng hồ: 「時計」 (とけい)."},
        {"id": 10, "category": "Từ vựng: Sự kiện", "q": "赤ちゃんが 生まれる ことを [____] と 言います。", "options": ["出産 (しゅっさん)", "就職", "引越し", "入学"], "correct": 0, "explain": "Sinh em bé là 「出産」 (しゅっさん - Xuất sản)."},
        {"id": 11, "category": "Chữ Hán Bài 17: 祝 (Chúc)", "q": "Chữ Hán 「祝」 trong 「お祝い (おいわい)」 có âm Hán Việt là:", "options": ["CHÚC", "ĐẢN", "KẾT", "HÔN"], "correct": 0, "explain": "Chữ 祝 có âm Hán Việt là CHÚC (9 nét, bộ Kỳ 礻 + chữ Huynh 兄)."},
        {"id": 12, "category": "Chữ Hán Bài 17: 誕 (Đản)", "q": "Từ 「たんじょうび」 (Sinh nhật) có chữ Hán đầu tiên là:", "options": ["誕", "祝", "結", "計"], "correct": 0, "explain": "「たんじょうび」 viết là 「誕生日」 (ĐẢN SINH NHẬT - chữ 誕 có 15 nét)."},
        {"id": 13, "category": "Chữ Hán Bài 17: 結婚", "q": "Từ 「けっこん」 (Kết hôn) được viết bằng cặp chữ Hán nào?", "options": ["結婚", "結絵", "婚誕", "祝婚"], "correct": 0, "explain": "「けっこん」 viết là 「結婚」 (KẾT HÔN - chữ 結 12 nét, chữ 婚 11 nét)."},
        {"id": 14, "category": "Chữ Hán Bài 17: 写真", "q": "Từ 「しゃしん」 (Bức ảnh) gồm 2 chữ Hán nào?", "options": ["写真", "画真", "絵真", "写計"], "correct": 0, "explain": "「しゃしん」 là 「写真」 (TẢ CHÂN - chữ 写 5 nét, chữ 真 10 nét)."},
        {"id": 15, "category": "Chữ Hán Bài 17: 時計", "q": "Từ 「とけい」 (Đồng hồ) viết bằng chữ Hán là:", "options": ["時計", "時真", "時写", "時結"], "correct": 0, "explain": "「とけい」 viết là 「時計」 (THỜI KẾ - chữ 時 10 nét, chữ 計 9 nét)."}
    ]
}
