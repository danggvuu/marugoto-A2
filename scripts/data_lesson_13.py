# -*- coding: utf-8 -*-
"""
Data for Marugoto A2-2 Lesson 13:
Topic 7: 出張 (Chuyến đi công tác)
Bài 13: Lịch Trình Công Tác & Đón Tiếp (田中さんに会ったことがあります)
"""

def make_svg(title, emoji, c1="#0284c7", c2="#0369a1"):
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

CFG_13 = {
    "num": 13,
    "title_vi": "Lịch Trình Công Tác",
    "title_jp": "田中さんに会ったことがあります",
    "topic_name": "Chuyến Đi Công Tác (出張)",
    "topic_badge": "TOPIC 7: 出張 • BÀI 13",
    "desc": "Làm chủ cách nói về kinh nghiệm và trải nghiệm trong quá khứ (V-たことがあります), đọc hiểu và trao đổi lịch trình công tác, giờ giấc bay/đến nơi, cùng các nghi thức đón tiếp khách tại sân bay chuẩn văn hóa doanh nghiệp Nhật Bản.",

    "grammars": [
        {
            "title": "Nói về kinh nghiệm, trải nghiệm: V-たことがあります",
            "icon": "✈️",
            "tag": "Trải nghiệm & Kinh nghiệm",
            "color": "#0284c7",
            "color_dark": "#0369a1",
            "intro": "Dùng để diễn tả một hành động hay sự kiện đã từng xảy ra ít nhất một lần trong đời tính đến thời điểm hiện tại.",
            "formula": "Động từ thể Quá khứ (V-た) + ことがあります (Đã từng)<br>Động từ thể Quá khứ (V-た) + ことがありません (Chưa từng)<br>Động từ thể Quá khứ (V-た) + ことがありますか (Đã từng... chưa?)",
            "meaning": "Đã từng làm gì... / Chưa từng làm gì... Trong công việc: giới thiệu đã từng gặp đối tác, đã từng đến trụ sở chính hay chưa.",
            "table": {
                "headers": ["Thể Từ điển / Masu", "Thể Ta (Quá khứ)", "Dạng kinh nghiệm hoàn chỉnh"],
                "rows": [
                    ["会います (Gặp)", "会った", "田中さんに 会ったことが あります。"],
                    ["行きます (Đi)", "行った", "東京の本社に 行ったことが あります。"],
                    ["乗ります (Đi/Lên)", "乗った", "新幹線に 乗ったことが ありません。"],
                    ["泊まります (Nghỉ trọ)", "泊まった", "あのホテルに 泊まったことが ありますか。"]
                ]
            },
            "examples": [
                {"jp": "私は 田中さんに 会ったことが あります。", "vi": "Tôi đã từng gặp anh Tanaka trước đây rồi."},
                {"jp": "日本へ 出張に 行ったことが ありません。", "vi": "Tôi chưa từng đi công tác Nhật Bản bao giờ."},
                {"jp": "そのホテルに 泊まったことが ありますか。―― はい、一度あります。", "vi": "Bạn đã từng ở khách sạn đó bao giờ chưa? ―― Vâng, tôi đã ở một lần rồi."}
            ]
        },
        {
            "title": "Báo cáo lịch trình & Giờ giấc: ～時に 着きます / 出発します",
            "icon": "⏰",
            "tag": "Lịch trình công tác",
            "color": "#059669",
            "color_dark": "#047857",
            "intro": "Dùng để thông báo chính xác mốc thời gian xuất phát, đến nơi của chuyến bay hoặc tàu xe trong lịch trình công tác.",
            "formula": "[Thời gian] に [Địa điểm] に 着きます (Đến nơi lúc mấy giờ)<br>[Thời gian] に [Địa điểm] を 出発します (Khởi hành lúc mấy giờ)",
            "meaning": "Đến lúc... / Khởi hành lúc... Giúp hai bên công ty sắp xếp xe cộ đón tiễn chu đáo.",
            "examples": [
                {"jp": "飛行機は 午後3時に 成田空港に 着きます。", "vi": "Máy bay sẽ hạ cánh xuống sân bay Narita vào lúc 3 giờ chiều."},
                {"jp": "田中さんは 12日の 朝8時に ベトナムを 出発します。", "vi": "Anh Tanaka sẽ khởi hành từ Việt Nam vào lúc 8 giờ sáng ngày 12."},
                {"jp": "何時に 空港へ 迎えに 行きますか。―― 2時半に 行きます。", "vi": "Mấy giờ bạn sẽ đi ra sân bay đón? ―― 2 giờ rưỡi tôi sẽ đi."}
            ]
        },
        {
            "title": "Nghi thức đón khách tại sân bay: ようこそ / フライトはいかがでしたか",
            "icon": "🤝",
            "tag": "Văn hóa doanh nghiệp",
            "color": "#d97706",
            "color_dark": "#b45309",
            "intro": "Các câu chào hỏi trang trọng, lịch thiệp khi đón đối tác hoặc đồng nghiệp từ xa đến thăm công ty.",
            "formula": "お疲れ様でした。ようこそ [Địa điểm] へ！<br>フライトは いかがでしたか。<br>お疲れでは ありませんか。",
            "meaning": "Chào mừng anh đã đến... Chuyến bay của anh thế nào? Anh có mệt mỏi lắm không?",
            "examples": [
                {"jp": "田中さん、お疲れ様でした。ようこそ、ハノイへ！", "vi": "Anh Tanaka, anh đã vất vả rồi. Chào mừng anh đến với Hà Nội!"},
                {"jp": "フライトは いかがでしたか。―― 少し疲れましたが、大丈夫です。", "vi": "Chuyến bay của anh thế nào ạ? ―― Có hơi mệt một chút nhưng tôi vẫn ổn ạ."},
                {"jp": "ホテルまで 車で お送りします。", "vi": "Chúng tôi sẽ đưa anh về khách sạn bằng ô tô."}
            ]
        }
    ],

    "vocab": [
        {
                "id": 1,
                "cat": "flight",
                "catName": "Chuyến bay & Sân bay",
                "badge": "Chuyến bay",
                "jp": "～時の フライト",
                "kana": "～じの フライト",
                "kanji": "～時のフライト",
                "romaji": "~ji no furaito",
                "vi": "Chuyến bay lúc … giờ",
                "exJp": "９時の フライトで とうきょうへ いきます。",
                "exVi": "Tôi sẽ đi Tokyo trên chuyến bay lúc 9 giờ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_108758\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0284c7\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_108758)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">✈️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHUYẾN BAY</text>\n</svg>"
        },
        {
                "id": 2,
                "cat": "flight",
                "catName": "Chuyến bay & Sân bay",
                "badge": "Chuyến bay",
                "jp": "～時の びん",
                "kana": "～じの びん",
                "kanji": "～時の便",
                "romaji": "~ji no bin",
                "vi": "Chuyến bay lúc … giờ",
                "exJp": "ごご２時の びんに のります。",
                "exVi": "Tôi sẽ lên chuyến bay lúc 2 giờ chiều.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_108758\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0284c7\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_108758)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🛫</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHUYẾN BAY</text>\n</svg>"
        },
        {
                "id": 3,
                "cat": "flight",
                "catName": "Chuyến bay & Sân bay",
                "badge": "Địa điểm",
                "jp": "くうこう",
                "kana": "くうこう",
                "kanji": "空港",
                "romaji": "kuukou",
                "vi": "Sân bay",
                "exJp": "ハノイの くうこうに とうちゃくしました。",
                "exVi": "Tôi đã đáp xuống sân bay Hà Nội.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_749688\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#3b82f6\"/>\n      <stop offset=\"100%\" stop-color=\"#1d4ed8\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_749688)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏬</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">SÂN BAY</text>\n</svg>"
        },
        {
                "id": 4,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Danh động từ (N・V3)",
                "jp": "しゅっぱつ（します）",
                "kana": "しゅっぱつ（します）",
                "kanji": "出発（します）",
                "romaji": "shuppatsu(shimasu)",
                "vi": "Xuất phát",
                "exJp": "ひこうきは １０時に しゅっぱつします。",
                "exVi": "Máy bay sẽ cất cánh lúc 10 giờ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_983722\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_983722)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🛫</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">XUẤT PHÁT</text>\n</svg>"
        },
        {
                "id": 5,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Danh động từ (N・V3)",
                "jp": "とうちゃく（します）",
                "kana": "とうちゃく（します）",
                "kanji": "到着（します）",
                "romaji": "touchaku(shimasu)",
                "vi": "Hạ cánh, đến nơi",
                "exJp": "とうきょうに ぶじに とうちゃくしました。",
                "exVi": "Đã hạ cánh an toàn tới Tokyo.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_414450\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#22c55e\"/>\n      <stop offset=\"100%\" stop-color=\"#15803d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_414450)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🛬</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐẾN NƠI</text>\n</svg>"
        },
        {
                "id": 6,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Danh động từ (N・V3)",
                "jp": "しゅっちょう（します）",
                "kana": "しゅっちょう（します）",
                "kanji": "出張（します）",
                "romaji": "shucchou(shimasu)",
                "vi": "Công tác",
                "exJp": "らいしゅう おおさかへ しゅっちょうします。",
                "exVi": "Tuần tới tôi sẽ đi công tác Osaka.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_635627\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_635627)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💼</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CÔNG TÁC</text>\n</svg>"
        },
        {
                "id": 7,
                "cat": "company",
                "catName": "Công ty & Cơ quan",
                "badge": "Công ty",
                "jp": "ししゃ",
                "kana": "ししゃ",
                "kanji": "支社",
                "romaji": "shisha",
                "vi": "Chi nhánh",
                "exJp": "ベトナムの ししゃで はたらいています。",
                "exVi": "Tôi đang làm việc tại chi nhánh Việt Nam.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_783444\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_783444)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏢</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHI NHÁNH</text>\n</svg>"
        },
        {
                "id": 8,
                "cat": "company",
                "catName": "Công ty & Cơ quan",
                "badge": "Công ty",
                "jp": "ほんしゃ",
                "kana": "ほんしゃ",
                "kanji": "本社",
                "romaji": "honsha",
                "vi": "Trụ sở chính",
                "exJp": "とうきょうの ほんしゃに れんらくします。",
                "exVi": "Tôi sẽ liên lạc về trụ sở chính ở Tokyo.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_906698\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_906698)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏛️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TRỤ SỞ CHÍNH</text>\n</svg>"
        },
        {
                "id": 9,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Động từ",
                "jp": "おくります",
                "kana": "おくります",
                "kanji": "送ります",
                "romaji": "okurimasu",
                "vi": "Gửi",
                "exJp": "ともだちを くうこうまで おくります。",
                "exVi": "Tôi tiễn bạn ra tận sân bay.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_356941\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f59e0b\"/>\n      <stop offset=\"100%\" stop-color=\"#d97706\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_356941)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👋</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TIỄN ĐI</text>\n</svg>"
        },
        {
                "id": 10,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Động từ",
                "jp": "もらいます",
                "kana": "もらいます",
                "kanji": "貰います",
                "romaji": "moraimasu",
                "vi": "Nhận",
                "exJp": "せんぱいから おみやげを もらいました。",
                "exVi": "Tôi đã nhận được quà lưu niệm từ tiền bối.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_336256\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#eab308\"/>\n      <stop offset=\"100%\" stop-color=\"#ca8a04\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_336256)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎁</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NHẬN ĐƯỢC</text>\n</svg>"
        },
        {
                "id": 11,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Động từ",
                "jp": "おくりに いきます",
                "kana": "おくりに いきます",
                "kanji": "送りに行きます",
                "romaji": "okurini ikimasu",
                "vi": "Đi tiễn",
                "exJp": "あした たなかさんを おくりに いきます。",
                "exVi": "Ngày mai tôi sẽ đi tiễn anh Tanaka.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_559448\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#14b8a6\"/>\n      <stop offset=\"100%\" stop-color=\"#0f766e\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_559448)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚶‍♂️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐI TIỄN</text>\n</svg>"
        },
        {
                "id": 12,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Động từ",
                "jp": "むかえに いきます",
                "kana": "むかえに いきます",
                "kanji": "迎えに行きます",
                "romaji": "mukaeni ikimasu",
                "vi": "Đi đón",
                "exJp": "えきまで くるまで むかえに いきます。",
                "exVi": "Tôi sẽ lái xe ra ga để đi đón bạn.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_966935\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0284c7\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_966935)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚗</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐI ĐÓN</text>\n</svg>"
        },
        {
                "id": 13,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Danh từ",
                "jp": "でむかえ",
                "kana": "でむかえ",
                "kanji": "出迎え",
                "romaji": "demukae",
                "vi": "Đón",
                "exJp": "くうこうで でむかえが あります。",
                "exVi": "Có người ra sân bay đón tiếp.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_122105\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#059669\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_122105)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤝</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐÓN TIẾP</text>\n</svg>"
        },
        {
                "id": 14,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Danh từ",
                "jp": "みおくり",
                "kana": "みおくり",
                "kanji": "見送り",
                "romaji": "miokuri",
                "vi": "Tiễn",
                "exJp": "おおぜいの ひとが みおくりに きました。",
                "exVi": "Rất đông người đã đến tiễn đưa.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_898034\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f97316\"/>\n      <stop offset=\"100%\" stop-color=\"#c2410c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_898034)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👋</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TIỄN BIỆT</text>\n</svg>"
        },
        {
                "id": 15,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Động từ",
                "jp": "すきます",
                "kana": "すきます",
                "kanji": "空きます",
                "romaji": "sukimasu",
                "vi": "Vắng vẻ",
                "exJp": "このじかんの でんしゃは すいています。",
                "exVi": "Tàu điện giờ này khá vắng vẻ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_497857\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#06b6d4\"/>\n      <stop offset=\"100%\" stop-color=\"#0891b2\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_497857)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🪑</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VẮNG VẺ</text>\n</svg>"
        },
        {
                "id": 16,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Động từ",
                "jp": "こみます",
                "kana": "こみます",
                "kanji": "混みます",
                "romaji": "komimasu",
                "vi": "Đông đúc",
                "exJp": "みちは くるまで こんでいます。",
                "exVi": "Đường phố đang đông nghẹt xe cộ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_51977\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_51977)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👥</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐÔNG ĐÚC</text>\n</svg>"
        },
        {
                "id": 17,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Tính từ na",
                "jp": "かいてき（な）",
                "kana": "かいてき（な）",
                "kanji": "快適（な）",
                "romaji": "kaiteki(na)",
                "vi": "Thoải mái, dễ chịu",
                "exJp": "ホテルは ひろくて とても かいてきです。",
                "exVi": "Khách sạn rộng rãi và rất tiện nghi thoải mái.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_493162\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_493162)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🛋️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TIỆN NGHI</text>\n</svg>"
        },
        {
                "id": 18,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Danh từ",
                "jp": "じさ",
                "kana": "じさ",
                "kanji": "時差",
                "romaji": "jisa",
                "vi": "Chênh lệch múi giờ",
                "exJp": "にほんと ベトナムの じさは ２じかんです。",
                "exVi": "Múi giờ giữa Nhật và Việt Nam chênh lệch 2 tiếng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_307562\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f59e0b\"/>\n      <stop offset=\"100%\" stop-color=\"#d97706\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_307562)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">⏰</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MÚI GIỜ</text>\n</svg>"
        },
        {
                "id": 19,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Cụm từ",
                "jp": "おゆが でます",
                "kana": "おゆが でます",
                "kanji": "お湯が出ます",
                "romaji": "oyu ga demasu",
                "vi": "Có nước ấm",
                "exJp": "シャワーから あたたかい おゆが でます。",
                "exVi": "Vòi hoa sen chảy ra dòng nước ấm áp.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_620569\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0284c7\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_620569)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚿</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NƯỚC NÓNG</text>\n</svg>"
        },
        {
                "id": 20,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Tính từ",
                "jp": "ぬるい",
                "kana": "ぬるい",
                "kanji": "温い",
                "romaji": "nurui",
                "vi": "Ấm ấm (nước sôi...), nguội...",
                "exJp": "おゆが ぬるくて、すこし さむいです。",
                "exVi": "Nước chỉ hơi ấm ấm nên hơi lạnh.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_96693\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#64748b\"/>\n      <stop offset=\"100%\" stop-color=\"#334155\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_96693)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌡️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">HƠI ẤM NGUỘI</text>\n</svg>"
        },
        {
                "id": 21,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Danh từ",
                "jp": "スケジュール",
                "kana": "スケジュール",
                "kanji": "スケジュール",
                "romaji": "sukejuuru",
                "vi": "Lịch trình",
                "exJp": "しゅっちょうの スケジュールを かくにんします。",
                "exVi": "Xác nhận lại lịch trình chuyến công tác.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_966274\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_966274)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📅</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">LỊCH TRÌNH</text>\n</svg>"
        },
        {
                "id": 22,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Danh từ",
                "jp": "ばんごう",
                "kana": "ばんごう",
                "kanji": "番号",
                "romaji": "bangou",
                "vi": "Số",
                "exJp": "へやの ばんごうは 302です。",
                "exVi": "Số phòng của tôi là 302.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_25137\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_25137)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🔢</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CON SỐ</text>\n</svg>"
        },
        {
                "id": 23,
                "cat": "state",
                "catName": "Trạng thái & Lịch trình",
                "badge": "Phó từ",
                "jp": "ずっと",
                "kana": "ずっと",
                "kanji": "ずっと",
                "romaji": "zutto",
                "vi": "Suốt, mãi / Hơn hẳn",
                "exJp": "きのうは ずっと ホテルに いました。",
                "exVi": "Hôm qua tôi ở suốt trong khách sạn.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_22600\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_22600)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">⏳</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">SUỐT MÃI</text>\n</svg>"
        },
        {
                "id": 24,
                "cat": "travel",
                "catName": "Di chuyển & Công tác",
                "badge": "Danh động từ (N・V3)",
                "jp": "チェック（します）",
                "kana": "チェック（します）",
                "kanji": "チェック（します）",
                "romaji": "chekku(shimasu)",
                "vi": "Kiểm tra, check",
                "exJp": "メールを チェックしてください。",
                "exVi": "Xin hãy kiểm tra hòm thư email nhé.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_523968\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#22c55e\"/>\n      <stop offset=\"100%\" stop-color=\"#15803d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_523968)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">✔️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KIỂM TRA</text>\n</svg>"
        },
        {
                "id": 25,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Danh động từ (N・V3)",
                "jp": "たんとう（します）",
                "kana": "たんとう（します）",
                "kanji": "担当（します）",
                "romaji": "tantou(shimasu)",
                "vi": "Phụ trách",
                "exJp": "ベトナムの プロジェクトを たんとうします。",
                "exVi": "Tôi phụ trách dự án Việt Nam.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_172295\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0284c7\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_172295)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📋</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">PHỤ TRÁCH</text>\n</svg>"
        },
        {
                "id": 26,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Mẫu câu",
                "jp": "～へ ようこそ。",
                "kana": "～へ ようこそ。",
                "kanji": "～へようこそ",
                "romaji": "~e youkoso",
                "vi": "Chào mừng đến với…",
                "exJp": "にほんへ ようこそ！",
                "exVi": "Chào mừng bạn đến với Nhật Bản!",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_741418\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f43f5e\"/>\n      <stop offset=\"100%\" stop-color=\"#be123c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_741418)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🎊</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHÀO MỪNG</text>\n</svg>"
        },
        {
                "id": 27,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Mẫu câu",
                "jp": "おつかれさまです。",
                "kana": "おつかれさまです。",
                "kanji": "お疲れ様です",
                "romaji": "otsukaresama desu",
                "vi": "Bạn đã vất vả rồi",
                "exJp": "きょうも おつかれさまでした。",
                "exVi": "Hôm nay bạn cũng đã vất vả rồi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_358065\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#059669\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_358065)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍵</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VẤT VẢ RỒI</text>\n</svg>"
        },
        {
                "id": 28,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Mẫu câu",
                "jp": "おまたせしました。",
                "kana": "おまたせしました。",
                "kanji": "お待たせしました",
                "romaji": "omataseshimashita",
                "vi": "Xin lỗi đã để bạn phải đợi",
                "exJp": "たいへん おまたせしました。",
                "exVi": "Vô cùng xin lỗi vì đã để quý khách phải đợi lâu.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_460158\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f59e0b\"/>\n      <stop offset=\"100%\" stop-color=\"#d97706\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_460158)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🙇</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐỂ BẠN ĐỢI</text>\n</svg>"
        },
        {
                "id": 29,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Mẫu câu",
                "jp": "～は いかがですか。",
                "kana": "～は いかがですか。",
                "kanji": "～はいかがですか",
                "romaji": "~wa ikaga desu ka",
                "vi": "＝～は どうですか。 Như thế nào (lịch sự)",
                "exJp": "おちゃは いかがですか。",
                "exVi": "Dùng thêm một tách trà nhé ạ?",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_718021\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_718021)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍵</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NHƯ THẾ NÀO</text>\n</svg>"
        },
        {
                "id": 30,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Danh từ",
                "jp": "じょうだん",
                "kana": "じょうだん",
                "kanji": "冗談",
                "romaji": "joudan",
                "vi": "Nói đùa",
                "exJp": "じょうだんを いって わらいました。",
                "exVi": "Nói đùa một câu khiến mọi người cùng cười.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_651373\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#eab308\"/>\n      <stop offset=\"100%\" stop-color=\"#ca8a04\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_651373)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">😄</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NÓI ĐÙA</text>\n</svg>"
        },
        {
                "id": 31,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Danh từ",
                "jp": "あいさつ",
                "kana": "あいさつ",
                "kanji": "挨拶",
                "romaji": "aisatsu",
                "vi": "Chào hỏi",
                "exJp": "あさの あいさつを します。",
                "exVi": "Chào hỏi nhau vào buổi sáng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_57558\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#06b6d4\"/>\n      <stop offset=\"100%\" stop-color=\"#0891b2\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_57558)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🙋‍♂️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHÀO HỎI</text>\n</svg>"
        },
        {
                "id": 32,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Danh từ",
                "jp": "ねだん",
                "kana": "ねだん",
                "kanji": "値段",
                "romaji": "nedan",
                "vi": "Giá cả",
                "exJp": "このホテルの ねだんは やすいです。",
                "exVi": "Giá phòng của khách sạn này khá rẻ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_936458\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#14b8a6\"/>\n      <stop offset=\"100%\" stop-color=\"#0f766e\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_936458)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏷️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GIÁ CẢ</text>\n</svg>"
        },
        {
                "id": 33,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Danh từ",
                "jp": "かぎ",
                "kana": "かぎ",
                "kanji": "鍵",
                "romaji": "kagi",
                "vi": "Chìa khóa",
                "exJp": "へやの かぎを うけつけに あずけます。",
                "exVi": "Gửi chìa khóa phòng ở quầy lễ tân.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_410671\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#eab308\"/>\n      <stop offset=\"100%\" stop-color=\"#a16207\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_410671)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🔑</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHÌA KHÓA</text>\n</svg>"
        },
        {
                "id": 34,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Danh từ",
                "jp": "かいぎ",
                "kana": "かいぎ",
                "kanji": "会議",
                "romaji": "kaigi",
                "vi": "Cuộc họp",
                "exJp": "ごごから ほんしゃで かいぎが あります。",
                "exVi": "Chiều nay có cuộc họp ở trụ sở chính.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_312923\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_312923)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👥</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CUỘC HỌP</text>\n</svg>"
        },
        {
                "id": 35,
                "cat": "business",
                "catName": "Giao tiếp công sở",
                "badge": "Danh từ",
                "jp": "しりょう",
                "kana": "しりょう",
                "kanji": "資料",
                "romaji": "shiryou",
                "vi": "Tài liệu",
                "exJp": "かいぎの しりょうを コピーします。",
                "exVi": "Photo tài liệu cho cuộc họp.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_626671\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#3b82f6\"/>\n      <stop offset=\"100%\" stop-color=\"#1d4ed8\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_626671)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📄</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TÀI LIỆU</text>\n</svg>"
        }
],

    "verb_lab": {
        "title": "Phòng Thí Nghiệm Động Từ Thể Ta & Lịch Trình (Morphing Lab)",
        "desc": "Thực hành biến đổi động từ sang thể Quá khứ ngắn (Thể た), tạo mẫu câu trải nghiệm kinh nghiệm và mẫu câu đi lại trong chuyến công tác:",
        "labels": ["Thể MASU", "Thể TA (Quá khứ)", "V-たことがあります (Đã từng)", "V-たことがありません (Chưa từng)", "Mẫu câu công tác"],
        "verbs": [
            {
                "kanji": "会います",
                "masu": "あいます",
                "vi": "Gặp gỡ",
                "col2": "会った",
                "col3": "会ったことがあります",
                "col4": "会ったことがありません",
                "col5": "空港で会いましょう",
                "ex": "私は田中さんに会ったことがあります。"
            },
            {
                "kanji": "行きます",
                "masu": "いきます",
                "vi": "Đi công tác",
                "col2": "行った",
                "col3": "行ったことがあります",
                "col4": "行ったことがありません",
                "col5": "出張に行きます",
                "ex": "日本へ出張に行ったことがありますか。"
            },
            {
                "kanji": "来ます",
                "masu": "きます",
                "vi": "Đến nơi",
                "col2": "来た",
                "col3": "来たことがあります",
                "col4": "来たことがありません",
                "col5": "12日に来ます",
                "ex": "田中さんは来週の月曜日に来ます。"
            },
            {
                "kanji": "乗ります",
                "masu": "のります",
                "vi": "Lên máy bay / tàu",
                "col2": "乗った",
                "col3": "乗ったことがあります",
                "col4": "乗ったことがありません",
                "col5": "飛行機に乗ります",
                "ex": "新幹線に乗ったことがありますか。"
            },
            {
                "kanji": "泊まります",
                "masu": "とまります",
                "vi": "Nghỉ trọ khách sạn",
                "col2": "泊まった",
                "col3": "泊まったことがあります",
                "col4": "泊まったことがありません",
                "col5": "ホテルに泊まります",
                "ex": "駅前のホテルに泊まったことがあります。"
            }
        ]
    },

    "dialogue": {
        "title": "Đón Khách Tại Sân Bay Quốc Tế",
        "desc": "Mô phỏng cuộc gặp gỡ đón tiếp đối tác Nhật Bản vừa hạ cánh xuống sân bay, hỏi han chuyến bay và sắp xếp di chuyển về khách sạn:",
        "initial": {
            "avatar": "👨‍💼",
            "name": "Tanaka-san (Khách công tác)",
            "jp": "こんにちは！お待たせしました。",
            "vi": "Xin chào bạn! Xin lỗi vì đã để bạn phải chờ lâu nhé."
        },
        "steps": [
            {
                "options": [
                    {
                        "text": "田中さん、お疲れ様でした。ようこそベトナムへ！",
                        "vi": "Chào anh Tanaka, anh đã vất vả rồi. Chào mừng anh đến với Việt Nam!",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "ありがとうございます。迎えに来てくれて助かりました。",
                        "replyVi": "Cảm ơn bạn rất nhiều. Bạn ra đón thế này đỡ cho tôi quá."
                    },
                    {
                        "text": "初めまして！フライトはいかがでしたか。",
                        "vi": "Rất vui được gặp anh lần đầu! Chuyến bay của anh thế nào ạ?",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "とても快適でしたよ。天気も良くてよかったです。",
                        "replyVi": "Rất thoải mái bạn ạ. Thời tiết đẹp nên chuyến bay êm lắm."
                    }
                ]
            },
            {
                "npcName": "Tanaka",
                "avatar": "👨‍💼",
                "npcText": "今からホテルへ向かいますか。車を手配してくれましたか。",
                "npcVi": "Bây giờ chúng ta di chuyển về khách sạn chứ nhỉ? Bạn đã sắp xếp xe giúp tôi chưa?",
                "options": [
                    {
                        "text": "はい、外にタクシーが待っています。荷物を持ちましょうか。",
                        "vi": "Vâng, bên ngoài có xe taxi đang đợi sẵn rồi ạ. Để tôi xách hành lý giúp anh nhé.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "すみません、ありがとうございます。よろしくお願いします。",
                        "replyVi": "Ngại quá, cảm ơn bạn nhiều nhé. Nhờ cả vào bạn."
                    },
                    {
                        "text": "会社の車を用意しました。ホテルまで約30分で着きますよ。",
                        "vi": "Chúng tôi đã chuẩn bị sẵn xe công ty rồi ạ. Về đến khách sạn mất khoảng 30 phút thôi.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Tanaka",
                        "replyText": "素晴らしいですね！とても助かります。",
                        "replyVi": "Tuyệt vời quá! Rất cảm ơn sự chu đáo của công ty bạn."
                    }
                ]
            }
        ]
    },

    "kanjis": [
        {"char": "会", "hv": "HỘI", "strokes": 6, "kun": "あ-う", "on": "KAI", "ex": "会社 (かいしゃ - công ty), 会います (あいます - gặp gỡ)", "mnemonic": "Mọi người tụ họp dưới một mái nhà (人) nói lời sum HỘI."},
        {"char": "社", "hv": "XÃ", "strokes": 7, "kun": "-", "on": "SHA", "ex": "会社 (かいしゃ - công ty), 本社 (ほんしゃ - trụ sở)", "mnemonic": "Thần linh (礻) phù hộ cho đất đai xã tắc (土) của XÃ hội."},
        {"char": "支", "hv": "CHI", "strokes": 4, "kun": "-", "on": "SHI", "ex": "支社 (ししゃ - chi nhánh), 支店 (してん - chi nhánh)", "mnemonic": "Bàn tay chống đỡ cành cây nhánh nhỏ (CHI)."},
        {"char": "張", "hv": "TRƯƠNG", "strokes": 11, "kun": "は-る", "on": "CHOO", "ex": "出張 (しゅっちょう - công tác), 主張 (しゅちょう - chủ trương)", "mnemonic": "Cây cung (弓) được kéo căng dài (長) gọi là TRƯƠNG."},
        {"char": "空", "hv": "KHÔNG", "strokes": 8, "kun": "そら", "on": "KUU", "ex": "空港 (くうこう - sân bay), 空気 (くうき - không khí)", "mnemonic": "Dưới mái nhà (穴) nhìn lên khoảng KHÔNG vũ trụ bao la."},
        {"char": "港", "hv": "CẢNG", "strokes": 12, "kun": "みなと", "on": "KOO", "ex": "空港 (くうこう - sân bay), 港 (みなと - bến cảng)", "mnemonic": "Dòng nước (氵) nơi các con hẻm thuyền bè tụ về bến CẢNG (巷)."},
        {"char": "発", "hv": "PHÁT", "strokes": 9, "kun": "-", "on": "HATSU", "ex": "出発 (しゅっぱつ - xuất phát), 発表 (はっぴょう - phát biểu)", "mnemonic": "Bắn cung phát tên vút bay ra ngoài tạo đà PHÁT động."},
        {"char": "着", "hv": "TRƯỚC", "strokes": 12, "kun": "つ-く、き-る", "on": "CHAKU", "ex": "到着 (とうちゃく - đến nơi), 着きます (つきます - cập bến)", "mnemonic": "Đàn cừu (羊) nhìn thấy mắt (目) người đã cập bến TRƯỚC."},
        {"char": "午", "hv": "NGỌ", "strokes": 4, "kun": "-", "on": "GO", "ex": "午前 (ごぜん - buổi sáng), 午後 (ごご - buổi chiều)", "mnemonic": "Cây chày giã gạo thẳng đứng lúc 12 giờ trưa (chính NGỌ)."}
    ],

    "quizzes": [
        {"id": 1, "category": "Ngữ pháp: V-たことがあります", "q": "私は 田中さんに [____] ことがあります。", "options": ["会った", "会う", "会いて", "会いまし"], "correct": 0, "explain": "Động từ thể Quá khứ ngắn (Thể た): 会います ➔ 会った + ことがあります (Đã từng gặp)."},
        {"id": 2, "category": "Ngữ pháp: V-たことがあります", "q": "日本へ 出張に [____] ことがありますか。", "options": ["行った", "行きます", "行かない", "行くて"], "correct": 0, "explain": "行きます có thể Ta bất quy tắc là 「行った」 ➔ 行ったことがありますか (Đã từng đi chưa?)."},
        {"id": 3, "category": "Ngữ pháp: Lịch trình", "q": "飛行機は 午後3時に 空港 [____] 着きます。", "options": ["に", "で", "を", "から"], "correct": 0, "explain": "Địa điểm đến nơi đi với trợ từ に: 「空港に着きます」 (Hạ cánh tại sân bay)."},
        {"id": 4, "category": "Từ vựng: Công tác", "q": "仕事で よその 土地へ 行く ことを [____] と 言います。", "options": ["出張 (しゅっちょう)", "旅行 (りょこう)", "留学 (りゅうがく)", "引越し (ひっこし)"], "correct": 0, "explain": "Chuyến đi làm việc tại nơi khác gọi là công tác: 「出張」 (しゅっちょう)."},
        {"id": 5, "category": "Từ vựng: Công ty", "q": "会社で 一番 中心に なる 建物は [____] です。", "options": ["本社 (ほんしゃ)", "支社 (ししゃ)", "空港 (くうこう)", "ホテル"], "correct": 0, "explain": "Trụ sở chính đầu não của công ty là 「本社」 (ほんしゃ)."},
        {"id": 6, "category": "Từ vựng: Sân bay", "q": "飛行機が 飛び立つ 場所は [____] です。", "options": ["空港 (くうこう)", "駅 (えき)", "港 (みなと)", "バス停"], "correct": 0, "explain": "Nơi máy bay cất cánh là sân bay: 「空港」 (くうこう)."},
        {"id": 7, "category": "Giao tiếp: Đón khách", "q": "Khi đón đối tác từ phương xa đến, câu chào hỏi lịch sự là:", "options": ["お疲れ様でした。ようこそ！", "いってらっしゃい！", "ごちそうさまでした！", "お大事に！"], "correct": 0, "explain": "「お疲れ様でした。ようこそ！」 (Anh đã vất vả rồi, chào mừng anh đã tới!)."},
        {"id": 8, "category": "Giao tiếp: Hỏi thăm", "q": "Để hỏi thăm đối tác chuyến bay có thuận lợi không, ta nói:", "options": ["フライトは いかがでしたか", "お元気ですか", "何時に起きましたか", "どこへ行きますか"], "correct": 0, "explain": "「フライトは いかがでしたか」 (Chuyến bay của anh thế nào ạ?)."},
        {"id": 9, "category": "Từ vựng: Đưa đón", "q": "空港まで 友達を [____] 行きます (Đi đón).", "options": ["むかえに", "おくりに", "かえりに", "あいに"], "correct": 0, "explain": "Đi đón ai đó là 「迎えに行きます」 (むかえにいきます)."},
        {"id": 10, "category": "Từ vựng: Xuất phát & Đến", "q": "「しゅっぱつ」 có nghĩa đối lập với từ nào?", "options": ["とうちゃく (到着)", "しゅっちょう (出張)", "よてい (予定)", "フライト"], "correct": 0, "explain": "「出発」 (Khởi hành) đối lập với 「到着」 (Đến nơi)."},
        {"id": 11, "category": "Chữ Hán Bài 13: 会 & 社", "q": "Từ 「かいしゃ」 (Công ty) gồm 2 chữ Hán nào?", "options": ["会社", "本社", "支社", "社会"], "correct": 0, "explain": "「かいしゃ」 viết chữ Hán là 「会社」 (HỘI XÃ)."},
        {"id": 12, "category": "Chữ Hán Bài 13: 支社", "q": "Từ 「ししゃ」 (Chi nhánh công ty) gồm chữ Hán nào?", "options": ["支社", "本社", "張社", "発社"], "correct": 0, "explain": "Chi nhánh là 「支社」 (CHI XÃ - 4 nét chữ 支)."},
        {"id": 13, "category": "Chữ Hán Bài 13: 出張", "q": "Từ 「しゅっちょう」 (Chuyến công tác) viết bằng chữ Hán là:", "options": ["出張", "出長", "発張", "着張"], "correct": 0, "explain": "Công tác viết chữ Hán là 「出張」 (XUẤT TRƯƠNG)."},
        {"id": 14, "category": "Chữ Hán Bài 13: 空港", "q": "Từ 「くうこう」 (Sân bay) viết Hán tự là:", "options": ["空港", "海港", "発港", "着港"], "correct": 0, "explain": "Sân bay là 「空港」 (KHÔNG CẢNG - gồm chữ 空 và 港)."},
        {"id": 15, "category": "Chữ Hán Bài 13: 午前 & 午後", "q": "Chữ Hán 「午」 trong 「午前 / 午後」 mang ý nghĩa gì?", "options": ["Giờ ngọ (12 giờ trưa)", "Buổi sáng", "Buổi tối", "Nửa đêm"], "correct": 0, "explain": "Chữ 午 (NGỌ) là mốc 12 giờ trưa; 午前 (trước trưa = sáng), 午後 (sau trưa = chiều)."}
    ]
}
