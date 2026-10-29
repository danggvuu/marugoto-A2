# -*- coding: utf-8 -*-
"""
Data for Marugoto A2-2 Lesson 14:
Topic 7: 出張 (Chuyến đi công tác)
Bài 14: Nơi Làm Việc & Xin Phép (これ、使ってもいいですか)
"""

def make_svg(title, emoji, c1="#7c3aed", c2="#5b21b6"):
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

CFG_14 = {
    "num": 14,
    "title_vi": "Nơi Làm Việc & Xin Phép",
    "title_jp": "これ、使ってもいいですか",
    "topic_name": "Chuyến Đi Công Tác (出張)",
    "topic_badge": "TOPIC 7: 出張 • BÀI 14",
    "desc": "Làm chủ mẫu câu xin phép lịch thiệp trong văn phòng (V-てもいいですか), cách phản hồi đồng ý hoặc từ chối tế nhị, làm quen với trang thiết bị văn phòng, giới thiệu đồng nghiệp và nói lời chào tạm biệt đầy trân trọng khi kết thúc chuyến công tác.",

    "grammars": [
        {
            "title": "Mẫu câu xin phép lịch sự: V-てもいいですか",
            "icon": "💻",
            "tag": "Giao tiếp nơi làm việc",
            "color": "#7c3aed",
            "color_dark": "#5b21b6",
            "intro": "Dùng khi bạn muốn xin phép cấp trên, đồng nghiệp hoặc đối tác để sử dụng đồ vật, mở/đóng cửa hay thực hiện một hành động nào đó trong văn phòng.",
            "formula": "Động từ thể Te (V-て) + もいいですか<br>Trả lời đồng ý: 「はい、どうぞ (使ってください)」<br>Từ chối khéo: 「すみません、今 使っています / 壊れています」",
            "meaning": "Tôi làm ... có được không? / Xin phép cho tôi được... Luôn thể hiện sự tôn trọng không gian làm việc chung.",
            "table": {
                "headers": ["Hành động", "Dạng xin phép V-てもいいですか", "Nghĩa tiếng Việt"],
                "rows": [
                    ["使います (Dùng)", "使っても いいですか", "Tôi dùng cái này có được không?"],
                    ["借ります (Mượn)", "借りても いいですか", "Tôi mượn máy tính/bút có được không?"],
                    ["開けます (Mở cửa)", "開けても いいですか", "Tôi mở cửa sổ ra có được không?"],
                    ["座ります (Ngồi)", "座っても いいですか", "Tôi ngồi ở đây có được không?"]
                ]
            },
            "examples": [
                {"jp": "この コンピューター、使っても いいですか。―― はい、どうぞ。", "vi": "Tôi dùng chiếc máy tính này có được không? ―― Vâng, xin mời anh cứ dùng tự nhiên."},
                {"jp": "ボールペンを 借りても いいですか。―― すみません、今 使っているんです。", "vi": "Tôi mượn chiếc bút bi có được không? ―― Xin lỗi anh, tôi hiện đang dùng mất rồi."},
                {"jp": "エアコンを つけても いいですか。―― ええ、いいですよ。", "vi": "Tôi bật điều hòa lên có được không? ―― Vâng, được chứ ạ."}
            ]
        },
        {
            "title": "Cấm đoán & Quy tắc văn phòng: V-てはいけません",
            "icon": "🚫",
            "tag": "Quy tắc & Nội quy",
            "color": "#dc2626",
            "color_dark": "#991b1b",
            "intro": "Dùng để nhắc nhở các quy định, nội quy bảo mật hoặc các điều không được phép làm tại khu vực làm việc của công ty.",
            "formula": "Động từ thể Te (V-て) + はいけません",
            "meaning": "Không được làm... / Cấm làm... (Thường dùng trong quy chế văn phòng hoặc người hướng dẫn căn dặn).",
            "examples": [
                {"jp": "ここで 写真を 撮っては いけません。", "vi": "Không được chụp ảnh tại khu vực này."},
                {"jp": "この パソコンの パスワードを 教えては いけません。", "vi": "Không được tiết lộ mật khẩu của máy tính này cho người ngoài."},
                {"jp": "大事な 書類を 外へ 持って 行っては いけません。", "vi": "Không được mang tài liệu quan trọng ra bên ngoài văn phòng."}
            ]
        },
        {
            "title": "Chào tạm biệt & Gửi lời hỏi thăm: お世話になりました",
            "icon": "🙏",
            "tag": "Lễ nghi công sở",
            "color": "#059669",
            "color_dark": "#047857",
            "intro": "Lời chào kết thúc chuyến công tác, bày tỏ lòng biết ơn sâu sắc đối với sự hỗ trợ của chi nhánh và nhờ chuyển lời thăm hỏi đến trụ sở chính.",
            "formula": "大変 お世話になりました。<br>[Ai đó] に よろしく お伝えください。<br>どうぞ お気をつけて お帰りください。",
            "meaning": "Cảm ơn anh/chị đã hết lòng giúp đỡ tôi trong suốt thời gian qua. Cho tôi gửi lời hỏi thăm tới mọi người ở trụ sở chính nhé.",
            "examples": [
                {"jp": "3日間、大変 お世話になりました。", "vi": "Trong 3 ngày qua, cảm ơn mọi người đã hết lòng giúp đỡ tôi."},
                {"jp": "本社の 皆さんに よろしく お伝えください。", "vi": "Xin vui lòng cho tôi gửi lời chào hỏi thăm tới tất cả mọi người ở trụ sở chính nhé."},
                {"jp": "また 会議で お会いしましょう。", "vi": "Hẹn sớm gặp lại anh trong cuộc họp lần tới nhé."}
            ]
        }
    ],

    "vocab": [
        {
                "id": 1,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Nơi chốn",
                "jp": "オフィス",
                "kana": "オフィス",
                "kanji": "オフィス",
                "romaji": "ofisu",
                "vi": "Văn phòng",
                "exJp": "あかるくて ひろい オフィスです。",
                "exVi": "Văn phòng làm việc sáng sủa và rộng rãi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_458197\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0284c7\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_458197)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏢</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VĂN PHÒNG</text>\n</svg>"
        },
        {
                "id": 2,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Thiết bị",
                "jp": "キャビネット",
                "kana": "キャビネット",
                "kanji": "キャビネット",
                "romaji": "kyabinetto",
                "vi": "Tủ đựng (tài liệu, ...)",
                "exJp": "しりょうは キャビネットの なかに あります。",
                "exVi": "Tài liệu nằm ở bên trong tủ đựng hồ sơ.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_683203\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#475569\"/>\n      <stop offset=\"100%\" stop-color=\"#1e293b\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_683203)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🗄️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TỦ TÀI LIỆU</text>\n</svg>"
        },
        {
                "id": 3,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Thiết bị",
                "jp": "コピーき",
                "kana": "コピーき",
                "kanji": "コピー機",
                "romaji": "kopiiki",
                "vi": "Máy photo",
                "exJp": "コピーきの つかいかたを おしえてください。",
                "exVi": "Xin hãy chỉ cho tôi cách sử dụng máy photo.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_521805\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#64748b\"/>\n      <stop offset=\"100%\" stop-color=\"#334155\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_521805)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🖨️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MÁY PHOTO</text>\n</svg>"
        },
        {
                "id": 4,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Thiết bị",
                "jp": "ファックス",
                "kana": "ファックス",
                "kanji": "ファックス",
                "romaji": "fakkusu",
                "vi": "Máy fax",
                "exJp": "ファックスで しょるいを おくります。",
                "exVi": "Gửi giấy tờ qua đường máy fax.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_218616\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0284c7\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_218616)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📠</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MÁY FAX</text>\n</svg>"
        },
        {
                "id": 5,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Thiết bị",
                "jp": "こくさいでんわ",
                "kana": "こくさいでんわ",
                "kanji": "国際電話",
                "romaji": "kokusaidenwa",
                "vi": "Điện thoại quốc tế",
                "exJp": "かいしゃから こくさいでんわを かけます。",
                "exVi": "Gọi điện thoại quốc tế từ công ty.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_511331\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#3b82f6\"/>\n      <stop offset=\"100%\" stop-color=\"#1d4ed8\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_511331)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌐</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GỌI QUỐC TẾ</text>\n</svg>"
        },
        {
                "id": 6,
                "cat": "people",
                "catName": "Nhân sự & Chức vụ",
                "badge": "Chức vụ",
                "jp": "しゃちょう",
                "kana": "しゃちょう",
                "kanji": "社長",
                "romaji": "shachou",
                "vi": "Giám đốc",
                "exJp": "しゃちょうに あいさつを します。",
                "exVi": "Chào hỏi giám đốc công ty.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_406482\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#1e293b\"/>\n      <stop offset=\"100%\" stop-color=\"#0f172a\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_406482)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👔</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GIÁM ĐỐC</text>\n</svg>"
        },
        {
                "id": 7,
                "cat": "people",
                "catName": "Nhân sự & Chức vụ",
                "badge": "Chức vụ",
                "jp": "ひしょ",
                "kana": "ひしょ",
                "kanji": "秘書",
                "romaji": "hisho",
                "vi": "Thư ký",
                "exJp": "ひしょに スケジュールを ききます。",
                "exVi": "Hỏi thư ký về lịch làm việc.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_983740\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_983740)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👩‍💼</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">THƯ KÝ</text>\n</svg>"
        },
        {
                "id": 8,
                "cat": "people",
                "catName": "Nhân sự & Chức vụ",
                "badge": "Nơi chốn",
                "jp": "うけつけ",
                "kana": "うけつけ",
                "kanji": "受付",
                "romaji": "uketsuke",
                "vi": "Lễ tân",
                "exJp": "１かいの うけつけで まっています。",
                "exVi": "Tôi đang đợi ở quầy lễ tân tầng 1.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_113847\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#be185d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_113847)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💁‍♀️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">LỄ TÂN</text>\n</svg>"
        },
        {
                "id": 9,
                "cat": "people",
                "catName": "Nhân sự & Chức vụ",
                "badge": "Nhân sự",
                "jp": "じむスタッフ",
                "kana": "じむスタッフ",
                "kanji": "事務スタッフ",
                "romaji": "jimu sutaffu",
                "vi": "Nhân viên văn phòng",
                "exJp": "じむスタッフが てつだって くれました。",
                "exVi": "Nhân viên văn phòng đã giúp đỡ tôi.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_969709\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_969709)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👥</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">NHÂN VIÊN</text>\n</svg>"
        },
        {
                "id": 10,
                "cat": "people",
                "catName": "Nhân sự & Chức vụ",
                "badge": "Nghề nghiệp",
                "jp": "ドライバー",
                "kana": "ドライバー",
                "kanji": "ドライバー",
                "romaji": "doraibaa",
                "vi": "Lái xe",
                "exJp": "ドライバーが くるまで まっています。",
                "exVi": "Bác tài xế đang đợi sẵn ở ô tô.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_120181\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f59e0b\"/>\n      <stop offset=\"100%\" stop-color=\"#d97706\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_120181)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚗</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TÀI XẾ</text>\n</svg>"
        },
        {
                "id": 11,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Cơ sở vật chất",
                "jp": "ドア",
                "kana": "ドア",
                "kanji": "ドア",
                "romaji": "doa",
                "vi": "Cửa ra vào",
                "exJp": "ドアを ノックしてから はいります。",
                "exVi": "Gõ cửa trước khi bước vào phòng.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_143025\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#78350f\"/>\n      <stop offset=\"100%\" stop-color=\"#451a03\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_143025)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚪</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CỬA RA VÀO</text>\n</svg>"
        },
        {
                "id": 12,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Cơ sở vật chất",
                "jp": "まど",
                "kana": "まど",
                "kanji": "窓",
                "romaji": "mado",
                "vi": "Cửa sổ",
                "exJp": "まどを あけて、かぜを いれます。",
                "exVi": "Mở cửa sổ cho gió thoáng vào.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_474277\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0284c7\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_474277)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🪟</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CỬA SỔ</text>\n</svg>"
        },
        {
                "id": 13,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Động từ",
                "jp": "（ドアを）あけます",
                "kana": "（ドアを）あけます",
                "kanji": "（ドアを）開けます",
                "romaji": "akemasu",
                "vi": "Mở (cửa)",
                "exJp": "ドアを あけても いいですか。",
                "exVi": "Tôi mở cửa có được không ạ?",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_519606\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#22c55e\"/>\n      <stop offset=\"100%\" stop-color=\"#15803d\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_519606)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚪</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MỞ CỬA</text>\n</svg>"
        },
        {
                "id": 14,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Động từ",
                "jp": "（ドアを）しめます",
                "kana": "（ドアを）しめます",
                "kanji": "（ドアを）閉めます",
                "romaji": "shimemasu",
                "vi": "Đóng (cửa)",
                "exJp": "さむいので、ドアを しめます。",
                "exVi": "Trời lạnh nên tôi đóng cửa lại.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_529198\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_529198)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🔒</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐÓNG CỬA</text>\n</svg>"
        },
        {
                "id": 15,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Động từ",
                "jp": "（でんきを）つけます",
                "kana": "（でんきを）つけます",
                "kanji": "（電気を）点けます",
                "romaji": "tsukemasu",
                "vi": "Bật (đèn)",
                "exJp": "くらいので でんきを つけます。",
                "exVi": "Phòng tối nên tôi bật đèn lên.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_216847\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#eab308\"/>\n      <stop offset=\"100%\" stop-color=\"#ca8a04\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_216847)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💡</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BẬT ĐÈN</text>\n</svg>"
        },
        {
                "id": 16,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Động từ",
                "jp": "（でんきを）けします",
                "kana": "（でんきを）けします",
                "kanji": "（電気を）消します",
                "romaji": "keshimasu",
                "vi": "Tắt (đèn)",
                "exJp": "かえるまえに でんきを けしてください。",
                "exVi": "Trước khi về nhớ tắt điện nhé.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_691253\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#475569\"/>\n      <stop offset=\"100%\" stop-color=\"#1e293b\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_691253)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌑</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TẮT ĐÈN</text>\n</svg>"
        },
        {
                "id": 17,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Động từ",
                "jp": "（パソコンが）こわれます",
                "kana": "（パソコンが）こわれます",
                "kanji": "（パソコンが）壊れます",
                "romaji": "kowaremasu",
                "vi": "(Máy tính) Hỏng",
                "exJp": "パソコンが こわれて、うごきません。",
                "exVi": "Máy tính bị hỏng nên không hoạt động.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_895837\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#dc2626\"/>\n      <stop offset=\"100%\" stop-color=\"#991b1b\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_895837)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">⚠️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BỊ HỎNG</text>\n</svg>"
        },
        {
                "id": 18,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Trạng thái",
                "jp": "べんきょうちゅう",
                "kana": "べんきょうちゅう",
                "kanji": "勉強中",
                "romaji": "benkyouchuu",
                "vi": "Đang học",
                "exJp": "いま にほんごを べんきょうちゅうです。",
                "exVi": "Tôi đang trong giờ học tiếng Nhật.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_819992\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_819992)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📖</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐANG HỌC</text>\n</svg>"
        },
        {
                "id": 19,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Phó từ",
                "jp": "ぺらぺら",
                "kana": "ぺらぺら",
                "kanji": "ぺらぺら",
                "romaji": "perapera",
                "vi": "Lưu loát (nói, ...)",
                "exJp": "かれは えいごが ぺらぺらです。",
                "exVi": "Anh ấy nói tiếng Anh cực kỳ lưu loát.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_257758\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0369a1\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_257758)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🗣️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">LƯU LOÁT</text>\n</svg>"
        },
        {
                "id": 20,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Động từ",
                "jp": "はじめます",
                "kana": "はじめます",
                "kanji": "始めます",
                "romaji": "hajimemasu",
                "vi": "Bắt đầu",
                "exJp": "では、かいぎを はじめましょう。",
                "exVi": "Vậy thì chúng ta bắt đầu cuộc họp nhé.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_23707\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#059669\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_23707)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">▶️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BẮT ĐẦU</text>\n</svg>"
        },
        {
                "id": 21,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Đồ dùng",
                "jp": "ファイル",
                "kana": "ファイル",
                "kanji": "ファイル",
                "romaji": "fairu",
                "vi": "File",
                "exJp": "このファイルを みてください。",
                "exVi": "Xin hãy xem tập file tài liệu này.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_365272\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#f59e0b\"/>\n      <stop offset=\"100%\" stop-color=\"#d97706\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_365272)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📁</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">FILE TÀI LIỆU</text>\n</svg>"
        },
        {
                "id": 22,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Đồ dùng",
                "jp": "メモ",
                "kana": "メモ",
                "kanji": "メモ",
                "romaji": "memo",
                "vi": "Ghi chú",
                "exJp": "だいじなことを メモに かきます。",
                "exVi": "Viết những điều quan trọng vào giấy ghi chú.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_696655\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#eab308\"/>\n      <stop offset=\"100%\" stop-color=\"#ca8a04\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_696655)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📝</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GHI CHÚ</text>\n</svg>"
        },
        {
                "id": 23,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Nơi chốn",
                "jp": "オフィス／じむしょ",
                "kana": "オフィス／じむしょ",
                "kanji": "事務所",
                "romaji": "ofisu / jimusho",
                "vi": "Văn phòng",
                "exJp": "じむしょに しりょうを とりに いきます。",
                "exVi": "Tôi đi đến văn phòng để lấy tài liệu.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_458197\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#3b82f6\"/>\n      <stop offset=\"100%\" stop-color=\"#1d4ed8\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_458197)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏢</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VĂN PHÒNG</text>\n</svg>"
        },
        {
                "id": 24,
                "cat": "office",
                "catName": "Văn phòng & Thiết bị",
                "badge": "Thao tác",
                "jp": "プリントアウト",
                "kana": "プリントアウト",
                "kanji": "プリントアウト",
                "romaji": "purintoauto",
                "vi": "In",
                "exJp": "このメールを プリントアウトしてください。",
                "exVi": "Xin hãy in bức email này ra giấy.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_824286\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#06b6d4\"/>\n      <stop offset=\"100%\" stop-color=\"#0891b2\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_824286)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🖨️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">IN RA GIẤY</text>\n</svg>"
        },
        {
                "id": 25,
                "cat": "action",
                "catName": "Thao tác & Động từ",
                "badge": "Động từ",
                "jp": "しょうかいします",
                "kana": "しょうかいします",
                "kanji": "紹介します",
                "romaji": "shoukaishimasu",
                "vi": "Giới thiệu",
                "exJp": "あたらしい スタッフを しょうかいします。",
                "exVi": "Tôi xin phép giới thiệu nhân viên mới.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_712906\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_712906)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤝</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GIỚI THIỆU</text>\n</svg>"
        }
],

    "verb_lab": {
        "title": "Phòng Thí Nghiệm Động Từ Thể Te & Xin Phép Văn Phòng",
        "desc": "Thực hành chuyển đổi động từ sang thể Te để xin phép (V-てもいいですか) hoặc nêu quy định cấm đoán (V-てはいけません):",
        "labels": ["Thể MASU", "Thể TE", "V-てもいいですか (Xin phép)", "V-てはいけません (Cấm)", "Lời đáp cho phép"],
        "verbs": [
            {
                "kanji": "使います",
                "masu": "つかいます",
                "vi": "Sử dụng",
                "col2": "使って",
                "col3": "使ってもいいですか",
                "col4": "使ってはいけません",
                "col5": "どうぞ使ってください",
                "ex": "このパソコンを使ってもいいですか。―― はい、どうぞ。"
            },
            {
                "kanji": "借ります",
                "masu": "かります",
                "vi": "Vay mượn",
                "col2": "借りて",
                "col3": "借りてもいいですか",
                "col4": "借りてはいけません",
                "col5": "どうぞ借りてください",
                "ex": "ペンを借りてもいいですか。―― ええ、いいですよ。"
            },
            {
                "kanji": "開けます",
                "masu": "あけます",
                "vi": "Mở cửa",
                "col2": "開けて",
                "col3": "開けてもいいですか",
                "col4": "開けてはいけません",
                "col5": "どうぞ開けてください",
                "ex": "少し窓を開けてもいいですか。―― どうぞ。"
            },
            {
                "kanji": "つけます",
                "masu": "つけます",
                "vi": "Bật (đèn/điều hòa)",
                "col2": "つけて",
                "col3": "つけてもいいですか",
                "col4": "つけてはいけません",
                "col5": "どうぞつけてください",
                "ex": "暗いので電気をつけてもいいですか。"
            },
            {
                "kanji": "入ります",
                "masu": "はいります",
                "vi": "Đi vào phòng",
                "col2": "入って",
                "col3": "入ってもいいですか",
                "col4": "入ってはいけません",
                "col5": "どうぞお入りください",
                "ex": "失礼します。入ってもいいですか。"
            }
        ]
    },

    "dialogue": {
        "title": "Mượn Đồ Văn Phòng & Lời Chào Tạm Biệt",
        "desc": "Thực hành giao tiếp xin mượn đồ văn phòng tại chi nhánh công ty và nói lời tạm biệt cảm ơn khi kết thúc chuyến công tác:",
        "initial": {
            "avatar": "👩‍💼",
            "name": "Kathy (Thư ký chi nhánh)",
            "jp": "お疲れ様です！何かお手伝いしましょうか。",
            "vi": "Chào anh! Tôi có thể hỗ trợ được gì cho anh không ạ?"
        },
        "steps": [
            {
                "options": [
                    {
                        "text": "すみません、このパソコンをお借りしてもいいですか。",
                        "vi": "Xin lỗi cô, tôi mượn chiếc máy tính này một chút có được không ạ?",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kathy",
                        "replyText": "はい、どうぞ！パスワードは画面の横にメモしてありますよ。",
                        "replyVi": "Vâng, xin mời anh cứ tự nhiên dùng! Mật khẩu được ghi chú ngay bên cạnh màn hình đó ạ."
                    },
                    {
                        "text": "資料を印刷したいのですが、プリンターを使ってもいいですか。",
                        "vi": "Tôi muốn in một số tài liệu, tôi dùng máy in có được không ạ?",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kathy",
                        "replyText": "ええ、大丈夫です。あちらのコピー機に繋がっていますよ。",
                        "replyVi": "Vâng, được chứ ạ. Máy tính đã được kết nối với chiếc máy in đằng kia rồi đó."
                    }
                ]
            },
            {
                "npcName": "Kathy",
                "avatar": "👩‍💼",
                "npcText": "出張のお仕事は順調に進みましたか。もうすぐ空港へ向かいますね。",
                "npcVi": "Công việc trong chuyến công tác diễn ra thuận lợi chứ ạ? Anh sắp sửa ra sân bay rồi nhỉ.",
                "options": [
                    {
                        "text": "はい、大変お世話になりました！本社の皆さんによろしくお伝えください。",
                        "vi": "Vâng, cảm ơn mọi người đã hết lòng giúp đỡ tôi! Cho tôi gửi lời chào hỏi thăm tới mọi người ở trụ sở chính nhé.",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kathy",
                        "replyText": "はい、必ず伝えます！お気をつけてお帰りくださいね。",
                        "replyVi": "Vâng, tôi nhất định sẽ chuyển lời ạ! Chúc anh thượng lộ bình an nhé."
                    },
                    {
                        "text": "おかげさまで無事に終わりました。また東京で会いましょう！",
                        "vi": "Nhờ có mọi người mà công việc đã hoàn thành tốt đẹp. Hẹn sớm gặp lại cô tại Tokyo nhé!",
                        "replyAvatar": "👩‍💼",
                        "replyNpc": "Kathy",
                        "replyText": "こちらこそ！またのお越しを心よりお待ちしております。",
                        "replyVi": "Chúng tôi cũng rất vinh hạnh! Rất mong được đón tiếp anh trong những lần tới."
                    }
                ]
            }
        ]
    },

    "kanjis": [
        {"char": "自", "hv": "TỰ", "strokes": 6, "kun": "みずか-ら", "on": "JI, SHI", "ex": "自分 (じぶん - bản thân), 自動車 (じどうしゃ - ô tô)", "mnemonic": "Hình vẽ cái mũi ở chính giữa gương mặt đại diện cho bản TỰ mình."},
        {"char": "分", "hv": "PHÂN", "strokes": 4, "kun": "わ-かる、わ-ける", "on": "BUN, FUN", "ex": "自分 (じぶん - bản thân), 5分 (ごふん - 5 phút)", "mnemonic": "Dùng con dao (刀) chia tách (八) mọi vật thành nhiều PHÂN phần."},
        {"char": "電", "hv": "ĐIỆN", "strokes": 13, "kun": "-", "on": "DEN", "ex": "電話 (でんわ - điện thoại), 電気 (でんき - đèn điện)", "mnemonic": "Những tia chớp lóe sáng dưới cơn mưa (雨) phát ra luồng ĐIỆN."},
        {"char": "話", "hv": "THOẠI", "strokes": 13, "kun": "はな-す、はなし", "on": "WA", "ex": "電話 (でんわ - điện thoại), 会話 (かいわ - hội thoại)", "mnemonic": "Dùng lời nói (言) và cái lưỡi (舌) để trò chuyện đối THOẠI."},
        {"char": "車", "hv": "XA", "strokes": 7, "kun": "くるま", "on": "SHA", "ex": "車 (くるま - xe hơi), 電車 (でんしゃ - tàu điện)", "mnemonic": "Hình ảnh cỗ XA xe có bánh và trục quay từ thời cổ đại."},
        {"char": "送", "hv": "TỐNG", "strokes": 9, "kun": "おく-る", "on": "SOO", "ex": "送ります (おくります - gửi đi / tiễn đưa), 郵送 (ゆうそう - gửi bưu điện)", "mnemonic": "Bước chân đi (辶) tiễn đưa quà cáp TỐNG tiễn phương xa."},
        {"char": "使", "hv": "SỬ", "strokes": 8, "kun": "つか-う", "on": "SHI", "ex": "使います (つかいます - sử dụng), 大使館 (たいしかん - đại sứ quán)", "mnemonic": "Con người (亻) được quan sai phái SỬ dụng tài năng."},
        {"char": "借", "hv": "TÁ", "strokes": 10, "kun": "か-りる", "on": "SHAKU", "ex": "借ります (かります - vay mượn), 借金 (しゃっきん - khoản nợ)", "mnemonic": "Con người (亻) qua ngày xưa (昔) vẫn phải đi vay mượn TÁ của nhau."}
    ],

    "quizzes": [
        {"id": 1, "category": "Ngữ pháp: V-てもいいですか", "q": "この コンピューター、[____] も いいですか。", "options": ["使って", "使いた", "使います", "使う"], "correct": 0, "explain": "Cấu trúc xin phép lịch sự: V-て + もいいですか ➔ 「使ってもいいですか」 (Tôi dùng có được không?)."},
        {"id": 2, "category": "Ngữ pháp: V-てもいいですか", "q": "ペンを [____] も いいですか (かりる)。", "options": ["借りて", "借って", "借りた", "借る"], "correct": 0, "explain": "Động từ nhóm 2: かります ➔ chia thể Te là 「借りて」 + もいいですか."},
        {"id": 3, "category": "Ngữ pháp: Phản hồi xin phép", "q": "「使ってもいいですか。」――「[____]、どうぞ。」", "options": ["はい", "いいえ", "だめ", "ごめん"], "correct": 0, "explain": "Khi đồng ý cho phép ai đó sử dụng đồ vật: 「はい、どうぞ」 (Vâng, xin mời)."},
        {"id": 4, "category": "Ngữ pháp: Từ chối khéo", "q": "Khi đang bận dùng đồ mà người khác muốn mượn, cách từ chối khéo léo nhất là:", "options": ["すみません、今 使っているんです", "絶対に だめです", "嫌です", "使わないでください"], "correct": 0, "explain": "Cách từ chối lịch sự trong văn hóa Nhật: 「すみません、今 使っているんです」 (Xin lỗi, hiện tại tôi đang dùng mất rồi)."},
        {"id": 5, "category": "Ngữ pháp: V-てはいけません", "q": "ここで 写真を [____] は いけません。", "options": ["撮って", "撮り", "撮る", "撮った"], "correct": 0, "explain": "Mẫu câu cấm đoán: V-て + はいけません ➔ 「撮ってはいけません」 (Không được chụp ảnh)."},
        {"id": 6, "category": "Từ vựng: Thiết bị văn phòng", "q": "書類を たくさん 紙に コピーする 機械は [____] です。", "options": ["コピー機", "エアコン", "キャビネット", "テレビ"], "correct": 0, "explain": "Máy in và sao chép tài liệu là 「コピー機」 (コピーき - Máy photocopy)."},
        {"id": 7, "category": "Từ vựng: Văn phòng", "q": "パソコンを 開く ときに 入力する 秘密の 文字は [____] です。", "options": ["パスワード", "チケット", "スケジュール", "フライト"], "correct": 0, "explain": "Mật khẩu máy tính là 「パスワード」 (Password)."},
        {"id": 8, "category": "Từ vựng: Nhân sự", "q": "社長の 身の回りの 仕事を 手伝う 人は [____] です。", "options": ["秘書 (ひしょ)", "ドライバー", "受付", "学生"], "correct": 0, "explain": "Người làm trợ lý, thư ký hỗ trợ giám đốc là 「秘書」 (ひしょ)."},
        {"id": 9, "category": "Giao tiếp: Kết thúc công tác", "q": "Khi chào tạm biệt chi nhánh sau chuyến công tác, câu nói cảm ơn chuẩn là:", "options": ["大変 お世話になりました", "ごちそうさまでした", "いただきます", "お大事に"], "correct": 0, "explain": "「大変 お世話になりました」 (Cảm ơn anh chị đã hết lòng giúp đỡ tôi)."},
        {"id": 10, "category": "Giao tiếp: Nhờ chuyển lời", "q": "「本社の 皆さんに よろしく [____] ください。」", "options": ["お伝え", "言って", "話して", "書いて"], "correct": 0, "explain": "Nhờ chuyển lời thăm hỏi lịch sự: 「よろしくお伝えください」 (おつたえください)."},
        {"id": 11, "category": "Chữ Hán Bài 14: 自 & 分", "q": "Từ 「じぶん」 (Bản thân mình) viết Hán tự là:", "options": ["自分", "白分", "自刀", "目分"], "correct": 0, "explain": "「じぶん」 viết chữ Hán là 「自分」 (TỰ PHÂN)."},
        {"id": 12, "category": "Chữ Hán Bài 14: 電 & 話", "q": "Từ 「でんわ」 (Điện thoại) gồm 2 chữ Hán nào?", "options": ["電話", "電気", "電車", "電送"], "correct": 0, "explain": "「でんわ」 là 「電話」 (ĐIỆN THOẠI - cả 2 chữ đều có 13 nét)."},
        {"id": 13, "category": "Chữ Hán Bài 14: 使 (Sử)", "q": "Động từ 「つかいます」 (Sử dụng) có chữ Hán là:", "options": ["使います", "借ります", "送ります", "作ります"], "correct": 0, "explain": "「つかいます」 là 「使います」 (SỬ - 8 nét)."},
        {"id": 14, "category": "Chữ Hán Bài 14: 借 (Tá)", "q": "Động từ 「かります」 (Vay mượn) có chữ Hán là:", "options": ["借ります", "使います", "送ります", "働きます"], "correct": 0, "explain": "「かります」 là 「借ります」 (TÁ - 10 nét, bộ Nhân đứng 亻 + chữ Tích 昔)."},
        {"id": 15, "category": "Chữ Hán Bài 14: 送 (Tống)", "q": "Động từ 「おくります」 trong 「メールを 送ります」 có chữ Hán là:", "options": ["送ります", "通ります", "連ります", "返ります"], "correct": 0, "explain": "「おくります」 viết chữ Hán là 「送ります」 (TỐNG - 9 nét)."}
    ]
}
