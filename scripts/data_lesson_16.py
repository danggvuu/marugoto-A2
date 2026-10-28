# -*- coding: utf-8 -*-
"""
Data for Marugoto A2-2 Lesson 16:
Topic 8: けんこう (Sức khỏe)
Bài 16: Giữ Gìn Sức Khỏe & Thói Quen Sống (走ったり、泳いだりしています)
"""

def make_svg(title, emoji, c1="#10b981", c2="#047857"):
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

CFG_16 = {
    "num": 16,
    "title_vi": "Giữ Gìn Sức Khỏe & Lối Sống",
    "title_jp": "走ったり、泳いだりしています",
    "topic_name": "Sức Khỏe (けんこう)",
    "topic_badge": "TOPIC 8: けんこう • BÀI 16",
    "desc": "Làm chủ cách liệt kê các hoạt động thể thao và thói quen sinh hoạt tiêu biểu với cấu trúc V1-たり V2-たりします, biểu đạt mục đích duy trì thể lực (N のために), đưa ra lời khuyên khoa học nên hoặc không nên làm gì (V-たほうがいい / V-ないほうがいい).",

    "grammars": [
        {
            "title": "Liệt kê hành động tiêu biểu: V1-たり、V2-たりします",
            "icon": "🏃",
            "tag": "Liệt kê thói quen",
            "color": "#10b981",
            "color_dark": "#047857",
            "intro": "Dùng để chọn ra vài hành động tiêu biểu đại diện trong số nhiều việc mình làm (không cần tuân theo thứ tự trước sau như thể Te).",
            "formula": "Động từ thể Quá khứ (V-た) + り、V-た + り します / しています",
            "meaning": "Lúc thì làm V1, lúc thì làm V2... (ví dụ: ngày nghỉ tôi lúc thì chạy bộ, lúc thì bơi lội).",
            "table": {
                "headers": ["Động từ 1", "Động từ 2", "Câu hoàn chỉnh V-たり V-たりします"],
                "rows": [
                    ["走ります (Chạy)", "泳ぎます (Bơi)", "週末は 走ったり、泳いだり しています。"],
                    ["本を読みます (Đọc)", "映画を見ます (Xem)", "休みの日は 本を読んだり、映画を見たり します。"],
                    ["散歩します (Tản bộ)", "買い物をします (Mua sắm)", "公園を 散歩したり、買い物をしたり します。"],
                    ["ヨガをします (Yoga)", "たいそうをします (Thể dục)", "ヨガをしたり、体操をしたり しています。"]
                ]
            },
            "examples": [
                {"jp": "週末は 公園を 走ったり、プールで 泳いだり しています。", "vi": "Cuối tuần tôi lúc thì chạy bộ ở công viên, lúc thì đi bơi ở hồ bơi."},
                {"jp": "休みの日は 音楽を 聞いたり、掃除を したり します。", "vi": "Vào ngày nghỉ tôi nghe nhạc rồi lúc thì dọn dẹp phòng ốc."},
                {"jp": "健康の ために、歩いたり 野菜を たくさん 食べたり しています。", "vi": "Để giữ gìn sức khỏe, tôi đi bộ và ăn nhiều rau xanh."}
            ]
        },
        {
            "title": "Biểu đạt mục đích: N の ために (Để... / Vì...)",
            "icon": "🎯",
            "tag": "Mục tiêu & Động lực",
            "color": "#0284c7",
            "color_dark": "#0369a1",
            "intro": "Dùng để nêu rõ mục đích của một chuỗi hành vi hoặc câu hỏi tìm hiểu lối sống của người khác.",
            "formula": "[Danh từ] の ために [Hành động / Câu hỏi]",
            "meaning": "Vì... / Để phục vụ cho... (ví dụ: Vì sức khỏe, Vì gia đình, Vì kỳ thi).",
            "examples": [
                {"jp": "健康の ために 何か していますか。", "vi": "Để duy trì sức khỏe, bạn có làm hoạt động gì không?"},
                {"jp": "健康の ために、毎朝 ヨーグルトを 食べて います。", "vi": "Vì sức khỏe, mỗi sáng tôi đều ăn sữa chua."},
                {"jp": "家族の ために 一生懸命 働いています。", "vi": "Tôi làm việc chăm chỉ hết mình vì gia đình."}
            ]
        },
        {
            "title": "Lời khuyên nên / không nên làm: V-たほうがいい / V-ないほうがいい",
            "icon": "💡",
            "tag": "Lời khuyên sức khỏe",
            "color": "#ea580c",
            "color_dark": "#c2410c",
            "intro": "Dùng khi người nói muốn đưa ra lời khuyên cụ thể, trực diện về lối sống tốt cho người nghe.",
            "formula": "Động từ thể Quá khứ (V-た) + ほうがいいです (Nên làm)<br>Động từ thể Phủ định (V-ない) + ほうがいいです (Không nên làm)",
            "meaning": "Nên... thì tốt hơn / Không nên... thì tốt hơn (so sánh giữa hai sự lựa chọn).",
            "examples": [
                {"jp": "毎日 野菜を たくさん 食べた ほうが いいですよ。", "vi": "Mỗi ngày bạn nên ăn nhiều rau xanh thì tốt hơn đấy."},
                {"jp": "夜遅くまで 起きていないで、早く 寝た ほうが いいです。", "vi": "Đừng thức quá khuya, bạn nên đi ngủ sớm thì tốt hơn."},
                {"jp": "お酒を 飲みすぎない ほうが いいですよ。", "vi": "Bạn không nên uống rượu bia quá nhiều đâu nhé."}
            ]
        }
    ],

    "vocab": [
        {
                "id": 1,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Chạy bộ thể dục (Jogging)",
                "jp": "ジョギング（を）します",
                "kana": "ジョギング（を）します",
                "kanji": "ジョギングをします",
                "romaji": "jogingu (wo) shimasu",
                "vi": "Chạy bộ thể dục (Jogging)",
                "exJp": "毎朝 公園で ジョギングをします。",
                "exVi": "Mỗi sáng đều chạy bộ ở công viên.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_102856\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_102856)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏃</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHẠY BỘ</text>\n</svg>"
        },
        {
                "id": 2,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Chạy nhanh",
                "jp": "はしります",
                "kana": "はしります",
                "kanji": "走ります",
                "romaji": "hashirimasu",
                "vi": "Chạy nhanh",
                "exJp": "駅まで 急いで 走りました。",
                "exVi": "Chạy vội vã ra ga.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_263711\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_263711)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏃‍♂️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CHẠY NHANH</text>\n</svg>"
        },
        {
                "id": 3,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Đi bộ rèn luyện sức khỏe",
                "jp": "ウォーキング（を）します",
                "kana": "ウォーキング（を）します",
                "kanji": "ウォーキングをします",
                "romaji": "uookingu (wo) shimasu",
                "vi": "Đi bộ rèn luyện sức khỏe",
                "exJp": "夜 ウォーキングを しています。",
                "exVi": "Buổi tối tôi thường đi bộ thể dục.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_405087\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_405087)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐI BỘ</text>\n</svg>"
        },
        {
                "id": 4,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Đi bộ bình thường",
                "jp": "あるきます",
                "kana": "あるきます",
                "kanji": "歩きます",
                "romaji": "arukimasu",
                "vi": "Đi bộ bình thường",
                "exJp": "毎日 30分 歩きます。",
                "exVi": "Mỗi ngày đi bộ 30 phút.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_405087\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_405087)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚶‍♂️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">ĐI BỘ</text>\n</svg>"
        },
        {
                "id": 5,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Kilomet (km)",
                "jp": "キロメートル",
                "kana": "キロメートル",
                "kanji": "キロメートル",
                "romaji": "kiromeetoru",
                "vi": "Kilomet (km)",
                "exJp": "毎日 5キロメートル 走ります。",
                "exVi": "Mỗi ngày chạy 5 km.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_452816\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_452816)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📏</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KILOMET</text>\n</svg>"
        },
        {
                "id": 6,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Kilogram (kg)",
                "jp": "キログラム",
                "kana": "キログラム",
                "kanji": "キログラム",
                "romaji": "kiroguramu",
                "vi": "Kilogram (kg)",
                "exJp": "体重が 2キログラム へりました。",
                "exVi": "Cân nặng đã giảm được 2 kg.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_683650\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_683650)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">⚖️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KILOGRAM</text>\n</svg>"
        },
        {
                "id": 7,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Bơi dưới nước",
                "jp": "およぎます",
                "kana": "およぎます",
                "kanji": "泳ぎます",
                "romaji": "oyogimasu",
                "vi": "Bơi dưới nước",
                "exJp": "夏は 海で 泳ぎます。",
                "exVi": "Mùa hè đi bơi ở biển.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_313518\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_313518)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏊</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BƠI</text>\n</svg>"
        },
        {
                "id": 8,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Môn bơi lội",
                "jp": "すいえい（を）します",
                "kana": "すいえい（を）します",
                "kanji": "水泳をします",
                "romaji": "suiei (wo) shimasu",
                "vi": "Môn bơi lội",
                "exJp": "週末に 水泳を 習っています。",
                "exVi": "Cuối tuần tôi đi học bơi lội.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_145572\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_145572)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏊‍♂️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BƠI LỘI</text>\n</svg>"
        },
        {
                "id": 9,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Bể bơi",
                "jp": "プール",
                "kana": "プール",
                "kanji": "プール",
                "romaji": "puuru",
                "vi": "Bể bơi, hồ bơi",
                "exJp": "近くの プールへ 行きます。",
                "exVi": "Đi đến bể bơi gần nhà.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_522024\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_522024)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏊</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BỂ BƠI</text>\n</svg>"
        },
        {
                "id": 10,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Tập bài thể dục",
                "jp": "たいそう（を）します",
                "kana": "たいそう（を）します",
                "kanji": "体操をします",
                "romaji": "taisou (wo) shimasu",
                "vi": "Tập bài thể dục",
                "exJp": "運動の前に 体操をします。",
                "exVi": "Tập thể dục trước khi vận động.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_800977\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_800977)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤸</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TẬP THỂ DỤC</text>\n</svg>"
        },
        {
                "id": 11,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Tập aerobic nhịp điệu",
                "jp": "エアロビクス（を）します",
                "kana": "エアロビクス（を）します",
                "kanji": "エアロビクスをします",
                "romaji": "earobikusu (wo) shimasu",
                "vi": "Tập aerobic nhịp điệu",
                "exJp": "ジムで エアロビクスを します。",
                "exVi": "Tập aerobic ở phòng gym.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_988192\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_988192)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💃</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">AEROBIC</text>\n</svg>"
        },
        {
                "id": 12,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Tập thể hình",
                "jp": "トレーニング（を）します",
                "kana": "トレーニング（を）します",
                "kanji": "トレーニングをします",
                "romaji": "toreeningu (wo) shimasu",
                "vi": "Tập thể hình, rèn luyện thể lực",
                "exJp": "筋力 トレーニングを します。",
                "exVi": "Tập luyện rèn cơ bắp.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_627270\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_627270)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏋️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TẬP GYM</text>\n</svg>"
        },
        {
                "id": 13,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Phòng tập thể hình gym",
                "jp": "ジム",
                "kana": "ジム",
                "kanji": "ジム",
                "romaji": "jimu",
                "vi": "Phòng tập thể hình gym",
                "exJp": "週に3回 ジムに 通っています。",
                "exVi": "Đi tập gym 3 buổi một tuần.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_82838\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_82838)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏋️‍♂️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">PHÒNG GYM</text>\n</svg>"
        },
        {
                "id": 14,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Tập yoga thiền định",
                "jp": "ヨガ（を）します",
                "kana": "ヨガ（を）します",
                "kanji": "ヨガをします",
                "romaji": "yoga (wo) shimasu",
                "vi": "Tập yoga thiền định",
                "exJp": "朝起きて ヨガを します。",
                "exVi": "Thức dậy buổi sáng rồi tập yoga.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_392463\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_392463)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🧘</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TẬP YOGA</text>\n</svg>"
        },
        {
                "id": 15,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Hút thuốc lá",
                "jp": "たばこを すいます",
                "kana": "たばこを すいます",
                "kanji": "煙草を吸います",
                "romaji": "tabako wo suimasu",
                "vi": "Hút thuốc lá",
                "exJp": "たばこを 吸うのを やめました。",
                "exVi": "Tôi đã bỏ hẳn hút thuốc lá.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_207421\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_207421)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🚭</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">HÚT THUỐC</text>\n</svg>"
        },
        {
                "id": 16,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Sức khỏe tốt",
                "jp": "けんこう",
                "kana": "けんこう",
                "kanji": "健康",
                "romaji": "kenkou",
                "vi": "Sức khỏe tốt",
                "exJp": "健康が いちばん 大切です。",
                "exVi": "Sức khỏe là điều quý giá nhất.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_839422\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_839422)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">💪</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">SỨC KHỎE</text>\n</svg>"
        },
        {
                "id": 17,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Tốt cho sức khỏe",
                "jp": "けんこうに いい",
                "kana": "けんこうに いい",
                "kanji": "健康にいい",
                "romaji": "kenkou ni ii",
                "vi": "Tốt cho sức khỏe",
                "exJp": "野菜は 健康にいいです。",
                "exVi": "Rau xanh rất tốt cho sức khỏe.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_16817\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_16817)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🥗</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TỐT SỨC KHỎE</text>\n</svg>"
        },
        {
                "id": 18,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Tốt cho cơ thể",
                "jp": "からだに いい",
                "kana": "からだに いい",
                "kanji": "体にいい",
                "romaji": "karada ni ii",
                "vi": "Tốt cho cơ thể",
                "exJp": "お茶は 体にいい 飲み物です。",
                "exVi": "Trà là thức uống tốt cho cơ thể.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_110909\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_110909)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🍵</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">TỐT CƠ THỂ</text>\n</svg>"
        },
        {
                "id": 19,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Có hại cho sức khỏe",
                "jp": "けんこうに わるい",
                "kana": "けんこうに わるい",
                "kanji": "健康に悪い",
                "romaji": "kenkou ni warui",
                "vi": "Có hại cho sức khỏe",
                "exJp": "お酒の 飲みすぎは 健康に悪いです。",
                "exVi": "Uống quá nhiều rượu có hại sức khỏe.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_117454\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_117454)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">⚠️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">HẠI SỨC KHỎE</text>\n</svg>"
        },
        {
                "id": 20,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Có hại cho cơ thể",
                "jp": "からだに わるい",
                "kana": "からだに わるい",
                "kanji": "体に悪い",
                "romaji": "karada ni warui",
                "vi": "Có hại cho cơ thể",
                "exJp": "夜更かしは 体に悪いです。",
                "exVi": "Thức khuya rất có hại cho cơ thể.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_647711\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_647711)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">❌</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">HẠI CƠ THỂ</text>\n</svg>"
        },
        {
                "id": 21,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Vì sức khỏe bản thân",
                "jp": "けんこうの ために",
                "kana": "けんこうの ために",
                "kanji": "健康のために",
                "romaji": "kenkou no tameni",
                "vi": "Vì sức khỏe bản thân",
                "exJp": "健康のために 毎日走っています。",
                "exVi": "Tôi chạy mỗi ngày vì sức khỏe.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_600941\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_600941)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏃</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">VÌ SỨC KHỎE</text>\n</svg>"
        },
        {
                "id": 22,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Thư giãn",
                "jp": "リラックス（を）します",
                "kana": "リラックス（を）します",
                "kanji": "リラックスをします",
                "romaji": "rirakkusu (wo) shimasu",
                "vi": "Thư giãn, xả stress",
                "exJp": "お風呂に入って リラックスします。",
                "exVi": "Ngâm bồn tắm để thư giãn.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_751884\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_751884)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🛀</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">THƯ GIÃN</text>\n</svg>"
        },
        {
                "id": 23,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Bản khảo sát câu hỏi",
                "jp": "アンケート",
                "kana": "アンケート",
                "kanji": "アンケート",
                "romaji": "ankeeto",
                "vi": "Bản khảo sát câu hỏi",
                "exJp": "健康についての アンケートに 答えます。",
                "exVi": "Trả lời bản khảo sát về sức khỏe.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_150546\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_150546)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📋</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">BẢN KHẢO SÁT</text>\n</svg>"
        },
        {
                "id": 24,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Kết quả khảo sát/kiểm tra",
                "jp": "けっか",
                "kana": "けっか",
                "kanji": "結果",
                "romaji": "kekka",
                "vi": "Kết quả khảo sát/kiểm tra",
                "exJp": "健康診断の 結果が よかったです。",
                "exVi": "Kết quả khám sức khỏe định kỳ rất tốt.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_860552\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_860552)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">📊</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">KẾT QUẢ</text>\n</svg>"
        },
        {
                "id": 25,
                "cat": "exercise",
                "catName": "Môn thể thao & Tập luyện",
                "badge": "Tập giãn cơ",
                "jp": "ストレッチ（を）します",
                "kana": "ストレッチ（を）します",
                "kanji": "ストレッチをします",
                "romaji": "sutorecchi (wo) shimasu",
                "vi": "Tập giãn cơ, khởi động",
                "exJp": "お風呂の後に ストレッチをします。",
                "exVi": "Giãn cơ sau khi tắm xong.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_355376\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_355376)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🤸‍♀️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">GIÃN CƠ</text>\n</svg>"
        },
        {
                "id": 26,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Câu lạc bộ thể thao",
                "jp": "スポーツクラブ",
                "kana": "スポーツクラブ",
                "kanji": "スポーツクラブ",
                "romaji": "supootsu kurabu",
                "vi": "Câu lạc bộ thể thao",
                "exJp": "スポーツクラブに 入会しました。",
                "exVi": "Tôi đã đăng ký câu lạc bộ thể thao.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_767451\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_767451)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🏟️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">CLB THỂ THAO</text>\n</svg>"
        },
        {
                "id": 27,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Huấn luyện viên",
                "jp": "トレーナー",
                "kana": "トレーナー",
                "kanji": "トレーナー",
                "romaji": "toreenaa",
                "vi": "Huấn luyện viên, PT",
                "exJp": "トレーナーに 運動を 教わります。",
                "exVi": "Được huấn luyện viên hướng dẫn bài tập.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_140074\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_140074)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">👨‍🏫</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">HLV THỂ HÌNH</text>\n</svg>"
        },
        {
                "id": 28,
                "cat": "health",
                "catName": "Sức khỏe & Thói quen",
                "badge": "Lần đầu tiên",
                "jp": "はじめて",
                "kana": "はじめて",
                "kanji": "初めて",
                "romaji": "hajimete",
                "vi": "Lần đầu tiên",
                "exJp": "初めて マラソンに 参加しました。",
                "exVi": "Lần đầu tiên tôi tham gia chạy marathon.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_183185\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_183185)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🌟</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">LẦN ĐẦU TIÊN</text>\n</svg>"
        },
        {
                "id": 29,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Máy móc tập luyện gym",
                "jp": "マシン",
                "kana": "マシン",
                "kanji": "マシン",
                "romaji": "mashin",
                "vi": "Máy móc tập luyện gym",
                "exJp": "新しい トレーニングマシンです。",
                "exVi": "Đây là máy tập gym đời mới.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_124890\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_124890)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">⚙️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">MÁY TẬP</text>\n</svg>"
        },
        {
                "id": 30,
                "cat": "measure",
                "catName": "Đo lường & Cơ sở vật chất",
                "badge": "Phòng chờ",
                "jp": "ラウンジ",
                "kana": "ラウンジ",
                "kanji": "ラウンジ",
                "romaji": "raunji",
                "vi": "Phòng chờ, sảnh nghỉ ngơi",
                "exJp": "運動の後に ラウンジで 休みます。",
                "exVi": "Nghỉ ngơi ở sảnh chờ sau khi tập.",
                "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_854531\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_854531)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"34\">🛋️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">PHÒNG CHỜ</text>\n</svg>"
        }
],

    "verb_lab": {
        "title": "Phòng Thí Nghiệm Động Từ Thể Tari & Lời Khuyên (Morphing Lab)",
        "desc": "Thực hành biến đổi động từ sang thể Tari (Liệt kê thói quen sống) và mẫu câu khuyên bảo nên/không nên (V-たほうがいい / V-ないほうがいい):",
        "labels": ["Thể MASU", "Thể TARI (Liệt kê)", "V1-たり V2-たり (Đang làm)", "V-たほうがいい (Nên)", "V-ないほうがいい (Không nên)"],
        "verbs": [
            {
                "kanji": "走ります",
                "masu": "はしります",
                "vi": "Chạy bộ",
                "col2": "走ったり",
                "col3": "走ったり泳いだりしています",
                "col4": "走ったほうがいいです",
                "col5": "走りすぎないほうがいいです",
                "ex": "週末は公園を走ったり歩いたりしています。"
            },
            {
                "kanji": "泳ぎます",
                "masu": "およぎます",
                "vi": "Bơi lội",
                "col2": "泳いだり",
                "col3": "泳いだり走ったりしています",
                "col4": "泳いだほうがいいです",
                "col5": "無理に泳がないほうがいいです",
                "ex": "夏は海やプールで泳いだりします。"
            },
            {
                "kanji": "起きます",
                "masu": "おきます",
                "vi": "Thức dậy",
                "col2": "起きたり",
                "col3": "早く起きたり運動したりします",
                "col4": "早く起きたほうがいいです",
                "col5": "遅く起きないほうがいいです",
                "ex": "朝早く起きて散歩したほうがいいですよ。"
            },
            {
                "kanji": "食べます",
                "masu": "たべます",
                "vi": "Ăn uống",
                "col2": "食べたり",
                "col3": "野菜を食べたり牛乳を飲んだり",
                "col4": "野菜を食べたほうがいいです",
                "col5": "食べすぎないほうがいいです",
                "ex": "毎朝くだものや野菜を食べたほうがいいです。"
            },
            {
                "kanji": "飲みます",
                "masu": "のみます",
                "vi": "Uống",
                "col2": "飲んだり",
                "col3": "お茶を飲んだり音楽を聞いたり",
                "col4": "お水を飲んだほうがいいです",
                "col5": "お酒を飲みすぎないほうがいい",
                "ex": "お酒を飲みすぎないほうが体にいいですよ。"
            }
        ]
    },

    "dialogue": {
        "title": "Chia Sẻ Bí Quyết Rèn Luyện Sức Khỏe",
        "desc": "Thảo luận về các thói quen vận động thể thao cuối tuần và trao đổi những lời khuyên hữu ích để nâng cao thể lực:",
        "initial": {
            "avatar": "👨‍💼",
            "name": "Kato (Đồng nghiệp)",
            "jp": "いつも元気ですね！健康のために何かしているんですか。",
            "vi": "Lúc nào trông bạn cũng tràn đầy năng lượng! Để giữ sức khỏe bạn có tập tành gì không?"
        },
        "steps": [
            {
                "options": [
                    {
                        "text": "はい、休みの日はジョギングをしたり、ジムで泳いだりしています。",
                        "vi": "Vâng, vào ngày nghỉ tôi lúc thì chạy bộ, lúc thì đi bơi ở phòng gym.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Kato",
                        "replyText": "素晴らしいですね！どのくらいのペースで続けているんですか。",
                        "replyVi": "Tuyệt vời quá! Bạn duy trì với tần suất như thế nào vậy?"
                    },
                    {
                        "text": "朝早く起きて、30分くらい近所をウォーキングしています。",
                        "vi": "Tôi thức dậy sớm vào buổi sáng rồi đi bộ khoảng 30 phút quanh khu phố.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Kato",
                        "replyText": "朝のウォーキングは気持ちがいいですね！見習いたいです。",
                        "replyVi": "Đi bộ buổi sáng không khí trong lành dễ chịu lắm nhỉ! Tôi phải học tập bạn mới được."
                    }
                ]
            },
            {
                "npcName": "Kato",
                "avatar": "👨‍💼",
                "npcText": "実は最近、仕事で疲れて運動不足なんです。どうすればいいでしょうか。",
                "npcVi": "Thực ra dạo này công việc bận rộn nên tôi ít vận động quá. Tôi nên làm thế nào bây giờ nhỉ?",
                "options": [
                    {
                        "text": "まずは無理をしないで、エスカレーターを使わずに階段を歩いたほうがいいですよ。",
                        "vi": "Trước tiên đừng quá gượng ép, thay vì đi thang cuốn bạn nên đi cầu thang bộ thì tốt hơn đấy.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Kato",
                        "replyText": "なるほど！駅の階段を使うことから始めてみます。アドバイスありがとう！",
                        "replyVi": "Ra là vậy! Tôi sẽ bắt đầu từ việc leo cầu thang ở nhà ga. Cảm ơn lời khuyên của bạn nhé!"
                    },
                    {
                        "text": "夜はスマホを見ないで早く寝て、休日に散歩から始めたほうがいいですよ。",
                        "vi": "Ban đêm không nên xem điện thoại mà hãy ngủ sớm, cuối tuần bắt đầu bằng việc đi dạo thì tốt hơn đấy.",
                        "replyAvatar": "👨‍💼",
                        "replyNpc": "Kato",
                        "replyText": "いいアドバイスですね！今夜から実践してみます。",
                        "replyVi": "Lời khuyên hay quá! Tối nay tôi sẽ thực hiện luôn."
                    }
                ]
            }
        ]
    },

    "kanjis": [
        {"char": "毎", "hv": "MỖI", "strokes": 6, "kun": "ごと", "on": "MAI", "ex": "毎日 (まいにち - mỗi ngày), 毎朝 (まいあさ - mỗi sáng)", "mnemonic": "Hình người mẹ (母) đội nón tần tảo MỖI ngày nuôi con."},
        {"char": "末", "hv": "MẠT", "strokes": 5, "kun": "すえ", "on": "MATSU", "ex": "週末 (しゅうまつ - cuối tuần), 年末 (ねんまつ - cuối năm)", "mnemonic": "Ngọn cây có cành trên dài hơn cành dưới chỉ phần ngọn, cuối MẠT."},
        {"char": "元", "hv": "NGUYÊN", "strokes": 4, "kun": "もと", "on": "GEN, GAN", "ex": "元気 (げんき - khỏe mạnh), 元日 (がんじつ - mùng 1 tết)", "mnemonic": "Hai nét ngang trên người (儿) tượng trưng cho nguồn gốc NGUYÊN thủy."},
        {"char": "外", "hv": "NGOẠI", "strokes": 5, "kun": "そと、はず-す", "on": "GAI", "ex": "外 (そと - bên ngoài), 外国 (がいこく - nước ngoài)", "mnemonic": "Buổi chiều (夕) bói quẻ bốc bằng dao (卜) để xem chuyện bên NGOẠI."},
        {"char": "起", "hv": "KHỞI", "strokes": 10, "kun": "お-きる、お-こす", "on": "KI", "ex": "起きます (おきます - thức dậy), 早起 (はやおき - dậy sớm)", "mnemonic": "Chạy bộ (走) đưa bản thân mình (己) đứng dậy KHỞI hành ngày mới."},
        {"char": "歩", "hv": "BỘ", "strokes": 8, "kun": "ある-く、あゆ-む", "on": "HO, PO", "ex": "歩きます (あるきます - đi bộ), 散歩 (さんぽ - tản bộ)", "mnemonic": "Hai bàn chân trước sau bước đi thong dong từng BỘ."},
        {"char": "走", "hv": "TẨU", "strokes": 7, "kun": "はし-る", "on": "SOO", "ex": "走ります (はしります - chạy), ご馳走 (ごちそう - bữa tiệc)", "mnemonic": "Người uốn mình vung tay vọt qua đất đai (土) TẨU thoát thật nhanh."},
        {"char": "泳", "hv": "VỊNH", "strokes": 8, "kun": "およ-ぐ", "on": "EI", "ex": "泳ぎます (およぎます - bơi lội), 水泳 (すいえい - môn bơi lội)", "mnemonic": "Dòng nước (氵) vĩnh cửu (永) là nơi thỏa sức bơi lội VỊNH mình."},
        {"char": "朝", "hv": "TRIỀU", "strokes": 12, "kun": "あさ", "on": "CHOO", "ex": "朝 (あさ - buổi sáng), 毎朝 (まいあさ - mỗi sáng)", "mnemonic": "Mặt trời mọc giữa đồng cỏ mười phương cùng vầng trăng buổi sáng sớm (TRIỀU)."},
        {"char": "気", "hv": "KHÍ", "strokes": 6, "kun": "-", "on": "KI", "ex": "元気 (げんき - khỏe mạnh), 天気 (てんき - thời tiết)", "mnemonic": "Luồng hơi nước bốc lên từ nồi cơm tỏa ra nguyên KHÍ trời đất."}
    ],

    "quizzes": [
        {"id": 1, "category": "Ngữ pháp: V-たり V-たりします", "q": "休みの 日は 本を [____]、映画を 見たり します。", "options": ["読んだり", "読んで", "読んだ", "読みたり"], "correct": 0, "explain": "Động từ thể Quá khứ ngắn (Thể た) + り: 読みます ➔ 読んだ ➔ 「読んだり」 (Lúc đọc sách, lúc xem phim)."},
        {"id": 2, "category": "Ngữ pháp: V-たり V-たりします", "q": "週末は プールで [____]、公園を 走ったり しています。", "options": ["泳いだり", "泳ぎたり", "泳いで", "泳いだ"], "correct": 0, "explain": "泳ぎます chia thể Quá khứ là 泳いだ ➔ Thêm り thành 「泳いだり」."},
        {"id": 3, "category": "Ngữ pháp: N のために", "q": "健康 [____] ために、毎朝 ウォーキングを しています。", "options": ["の", "に", "を", "で"], "correct": 0, "explain": "Cấu trúc chỉ mục đích với danh từ: 「Danh từ + の ために」 (Vì sức khỏe)."},
        {"id": 4, "category": "Ngữ pháp: V-たほうがいい", "q": "夜遅くまで 起きていないで、早く [____] ほうが いいですよ。", "options": ["寝た", "寝る", "寝て", "寝ない"], "correct": 0, "explain": "Khuyên nên làm gì: V-た + ほうがいい ➔ 「寝たほうがいい」 (Nên đi ngủ sớm)."},
        {"id": 5, "category": "Ngữ pháp: V-ないほうがいい", "q": "お酒を 飲み [____] ほうが いいですよ。", "options": ["すぎない", "すぎた", "すぎる", "すぎて"], "correct": 0, "explain": "Khuyên không nên làm gì: V-ない + ほうがいい ➔ 飲みすぎない ほうがいい (Không nên uống quá nhiều)."},
        {"id": 6, "category": "Từ vựng: Thể thao", "q": "プールで 手足を 動かして 進む 運動は [____] です。", "options": ["すいえい (水泳)", "ジョギング", "ヨガ", "たいそう"], "correct": 0, "explain": "Bơi lội trong hồ bơi là 「水泳」 (すいえい) / 泳ぎます."},
        {"id": 7, "category": "Từ vựng: Rèn luyện", "q": "道を 一歩一歩 足で 進む 運動は [____] です。", "options": ["ウォーキング (歩く)", "ドライブ", "フライト", "スキー"], "correct": 0, "explain": "Đi bộ thể dục là 「ウォーキング」 (Walking) / 歩きます."},
        {"id": 8, "category": "Từ vựng: Thói quen", "q": "「あさはやく おきます」 có nghĩa tiếng Việt là gì?", "options": ["Dậy sớm vào buổi sáng", "Đi ngủ sớm", "Ăn sáng sớm", "Đi làm sớm"], "correct": 0, "explain": "「朝早く起きます」 nghĩa là thức dậy sớm vào buổi sáng."},
        {"id": 9, "category": "Từ vựng: Cảnh báo", "q": "自分の 体力以上に 無理をして 働く ことを [____] と 言います。", "options": ["働きすぎます", "休みます", "走ります", "歩きます"], "correct": 0, "explain": "Lao động quá độ quá sức gọi là 「働きすぎます」 (はたらきすぎます)."},
        {"id": 10, "category": "Từ vựng: Sức khỏe", "q": "病気が なくて 体が 丈夫な 状態を 表す 言葉は [____] です。", "options": ["元気 (げんき)", "気持ちが悪い", "疲れている", "眠い"], "correct": 0, "explain": "Khỏe khoắn, dồi dào sinh lực là 「元気」 (げんき)."},
        {"id": 11, "category": "Chữ Hán Bài 16: 毎 (Mỗi)", "q": "Chữ Hán 「毎」 trong 「毎日 / 毎朝」 có bao nhiêu nét?", "options": ["6 nét", "5 nét", "7 nét", "8 nét"], "correct": 0, "explain": "Chữ 毎 (MỖI) có 6 nét viết."},
        {"id": 12, "category": "Chữ Hán Bài 16: 週末", "q": "Từ 「しゅうまつ」 (Cuối tuần) viết bằng cặp chữ Hán nào?", "options": ["週末", "週未", "週末", "週本"], "correct": 0, "explain": "「しゅうまつ」 là 「週末」 (CHU MẠT - chữ 末 có nét ngang trên dài hơn nét dưới)."},
        {"id": 13, "category": "Chữ Hán Bài 16: 歩 & 走", "q": "Cặp động từ 「あるきます」 (Đi bộ) và 「はしります」 (Chạy) viết là:", "options": ["歩きます và 走ります", "足きます và 走きます", "止きます và 走ります", "行きます và 来ます"], "correct": 0, "explain": "Đi bộ là 「歩きます」 (BỘ - 8 nét); chạy là 「走ります」 (TẨU - 7 nét)."},
        {"id": 14, "category": "Chữ Hán Bài 16: 泳 (Vịnh)", "q": "Động từ 「およぎます」 (Bơi lội) chứa bộ thủ nào?", "options": ["Bộ Thủy (氵)", "Bộ Hỏa (灬)", "Bộ Mộc (木)", "Bộ Kim (金)"], "correct": 0, "explain": "Bơi lội dưới nước nên chữ 泳 (VỊNH) có bộ Thủy (氵 - 3 nét chấm thủy)."},
        {"id": 15, "category": "Chữ Hán Bài 16: 起 (Khởi)", "q": "Động từ 「おきます」 trong 「朝早く起きます」 có chữ Hán là:", "options": ["起きます", "走きます", "歩きます", "行きます"], "correct": 0, "explain": "Thức dậy là 「起きます」 (KHỞI - 10 nét, bộ Tẩu 走 + chữ Kỷ 己)."}
    ]
}
