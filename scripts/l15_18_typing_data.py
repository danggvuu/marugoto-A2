# -*- coding: utf-8 -*-
"""Structured typing datasets for Marugoto A2 Lessons 11-18 Kanji (from PDFs) and Lessons 15-18 Vietnamese->Hiragana Sentences (from teacher notes)."""

# 50 items strictly verified from Kanji_Lesson_15-18.pdf
KANJI_15_18_ITEMS = [
    {
        "id": "k1518_01", "stt": 1, "group": "15-18", "lesson": "A2-18",
        "kanji": "来年", "kana": "らいねん", "accepted": ["らいねん"],
        "hv": "LAI NIÊN", "vi": "năm sau",
        "note": "来 (LAI = tới) + 年 (NIÊN = năm). Phân biệt với 今年 (ことし - năm nay) và 去年 (きょねん - năm ngoái).",
        "traps": [{"wrong": ["きょねん", "ことし"], "why": "Đây là 来年 (LAI NIÊN = năm sau ➔ らいねん). きょねん là 去年 (năm ngoái), ことし là 今年 (năm nay)."},
                  {"wrong": ["らいとし", "くるねん", "らいね"], "why": "Âm ghép On'yomi chuẩn của 来年 là らい・ねん (không đọc らいとし hay thiếu chữ ん)."}]
    },
    {
        "id": "k1518_02", "stt": 2, "group": "15-18", "lesson": "A2-16",
        "kanji": "外", "kana": "そと", "accepted": ["そと"],
        "hv": "NGOẠI", "vi": "bên ngoài",
        "note": "Đứng một mình đọc Kun'yomi là そと. Khi ghép từ Hán Việt như 外国 (がいこく), 外食 (がいしょく) mới đọc là がい.",
        "traps": [{"wrong": ["がい"], "why": "Khi chữ 外 đứng MỘT MÌNH chỉ vị trí thì đọc Kun'yomi là そと; đọc がい chỉ dùng trong từ ghép như 外国 / 外食."}]
    },
    {
        "id": "k1518_03", "stt": 3, "group": "15-18", "lesson": "A2-16",
        "kanji": "毎日", "kana": "まいにち", "accepted": ["まいにち"],
        "hv": "MỖI NHẬT", "vi": "hằng ngày, mỗi ngày",
        "note": "毎 (MỖI = まい) + 日 (NHẬT = にち). Phân biệt chuỗi 毎: 毎朝 (まいあさ), 毎週 (まいしゅう), 毎月 (まいつき/まいげつ).",
        "traps": [{"wrong": ["まいひ", "まいび"], "why": "日 trong 毎日 đọc âm On là にち ➔ まいにち (không đọc まいひ)."}]
    },
    {
        "id": "k1518_04", "stt": 4, "group": "15-18", "lesson": "A2-15",
        "kanji": "足ります", "kana": "たります", "accepted": ["たります"],
        "hv": "TÚC", "vi": "đủ",
        "note": "Cùng chữ 足 (TÚC): danh từ 'cái chân' đọc là あし (足), còn động từ 'đủ' nhóm II đọc là たります (足ります).",
        "traps": [{"wrong": ["あしります", "そくります", "たれます"], "why": "Động từ 足ります mang nghĩa 'đủ' đọc là たります (khác với danh từ 足 = あし 'chân')."}]
    },
    {
        "id": "k1518_05", "stt": 5, "group": "15-18", "lesson": "A2-15",
        "kanji": "下", "kana": "した", "accepted": ["した"],
        "hv": "HẠ", "vi": "dưới, bên dưới",
        "note": "Đứng một mình đọc là した. Chú ý khi ghép thành 下手 (へた - kém) lại đọc đặc biệt là へた!",
        "traps": [{"wrong": ["うえ", "へた", "か"], "why": "Chữ 下 đứng một mình đọc した ('bên dưới'). うえ là 上 ('bên trên'), へた là 下手 ('kém')."}]
    },
    {
        "id": "k1518_06", "stt": 6, "group": "15-18", "lesson": "A2-16",
        "kanji": "元気", "kana": "げんき", "accepted": ["げんき"],
        "hv": "NGUYÊN KHÍ", "vi": "khỏe mạnh, khỏe",
        "note": "Tính từ đuôi な (元気な / 元気です). 元 (NGUYÊN = げん) + 気 (KHÍ = き). Cẩn thận đục âm げ chứ không phải けん.",
        "traps": [{"wrong": ["けんき", "げんぎ"], "why": "Sai đục âm! 元 đọc là げん (có tenten ゛) và 気 đọc là き (không tenten) ➔ げんき."}]
    },
    {
        "id": "k1518_07", "stt": 7, "group": "15-18", "lesson": "A2-18",
        "kanji": "今年", "kana": "ことし", "accepted": ["ことし"],
        "hv": "KIM NIÊN", "vi": "năm nay",
        "note": "BẤT QUY TẮC (đọc gộp): 今年 đọc là ことし (không đọc こんねん hay いまとし!). Giống 今朝 (けさ).",
        "traps": [{"wrong": ["こんねん", "こんとし", "いまとし"], "why": "Từ đặc biệt bất quy tắc! 今年 KHÔNG ghép theo âm Hán mà đọc thuộc lòng là ことし."}]
    },
    {
        "id": "k1518_08", "stt": 8, "group": "15-18", "lesson": "A2-16",
        "kanji": "外食", "kana": "がいしょく", "accepted": ["がいしょく"],
        "hv": "NGOẠI THỰC", "vi": "ăn ngoài",
        "note": "外 (NGOẠI = がい) + 食 (THỰC = しょく). Có âm ghép ょ ở しょ! Tránh gõ nhầm しよく hay そとたべ.",
        "traps": [{"wrong": ["そとたべ", "がいしよく", "かいしょく"], "why": "外 ghép On'yomi là がい (có tenten), 食 là しょく (chữ ょ nhỏ, ghép thành しょ)."}]
    },
    {
        "id": "k1518_09", "stt": 9, "group": "15-18", "lesson": "A2-18",
        "kanji": "先週", "kana": "せんしゅう", "accepted": ["せんしゅう"],
        "hv": "TIÊN CHU", "vi": "tuần trước",
        "note": "先 (TIÊN = せん) + 週 (CHU = しゅう, có ゅ nhỏ và trường âm う!). Đừng quên trường âm う ở cuối.",
        "traps": [{"wrong": ["せんしゅ", "せんしゆう", "せんしゅん"], "why": "Chữ 週 đọc là しゅう — gồm ゅ nhỏ và trường âm う ở cuối (せんしゅう)."}]
    },
    {
        "id": "k1518_10", "stt": 10, "group": "15-18", "lesson": "A2-17",
        "kanji": "写真", "kana": "しゃしん", "accepted": ["しゃしん"],
        "hv": "TẢ CHÂN", "vi": "ảnh, hình ảnh",
        "note": "写 (TẢ = しゃ, có ゃ nhỏ) + 真 (CHÂN = しん). Lưu ý gõ đúng âm ghép しゃ.",
        "traps": [{"wrong": ["しやしん", "しゃじん", "さしん"], "why": "Chú ý しゃ có chữ ゃ nhỏ (âm ghép 'sha') và 真 là しん (không có tenten)."}]
    },
    {
        "id": "k1518_11", "stt": 11, "group": "15-18", "lesson": "A2-17",
        "kanji": "着ます", "kana": "きます", "accepted": ["きます"],
        "hv": "TRƯỚC", "vi": "mặc",
        "note": "Phân biệt cặp song sinh cực hay thi nhầm: 着ます (きます = mặc áo/váy, L17) vs 着きます (つきます = đến nơi, L13)!",
        "traps": [{"wrong": ["つきます", "ちゃくます"], "why": "Coi chừng nhầm cặp 着ます / 着きます! Không có chữ き ở giữa thì là 着ます (きます = MẶC). Còn 着きます (つきます) mới là ĐẾN NƠI."}]
    },
    {
        "id": "k1518_12", "stt": 12, "group": "15-18", "lesson": "A2-15",
        "kanji": "下手", "kana": "へた", "accepted": ["へた"],
        "hv": "HẠ THỦ", "vi": "không giỏi, kém",
        "note": "Từ đọc ĐẶC BIỆT (jukujikun): 下手 đọc là へた (không đọc したて hay かしゅ!). Đối nghĩa với 上手 (じょうず = giỏi).",
        "traps": [{"wrong": ["したて", "じょうず", "かしゅ", "げて"], "why": "Từ đặc biệt đọc thuộc lòng là へた! Không đọc したて (theo nghĩa chữ) hay じょうず (trái nghĩa: giỏi)."}]
    },
    {
        "id": "k1518_13", "stt": 13, "group": "15-18", "lesson": "A2-16",
        "kanji": "水泳", "kana": "すいえい", "accepted": ["すいえい"],
        "hv": "THỦY VỊNH", "vi": "bơi lội",
        "note": "Danh từ chỉ môn bơi lội: 水 (THỦY = すい) + 泳 (VỊNH = えい). Khi là động từ 'bơi' dùng 泳ぎます (およぎます).",
        "traps": [{"wrong": ["みずおよぎ", "すいおよ", "すいえ"], "why": "Cụm Hán Việt THỦY VỊNH đọc bằng On'yomi hết: すい + えい = すいえい."}]
    },
    {
        "id": "k1518_14", "stt": 14, "group": "15-18", "lesson": "A2-15",
        "kanji": "目", "kana": "め", "accepted": ["め"],
        "hv": "MỤC", "vi": "mắt",
        "note": "Bộ phận cơ thể Bài 15: 目 (め - mắt), 耳 (みみ - tai), 手 (て - tay), 足 (あし - chân), 頭 (あたま - đầu), 体 (からだ - cơ thể).",
        "traps": [{"wrong": ["みみ", "もく", "て"], "why": "Chữ 目 (MỤC = mắt) đọc là め (đứng một mình). Không nhầm với 耳 (みみ - tai) hay âm On もく trong 目的 (もくてき)."}]
    },
    {
        "id": "k1518_15", "stt": 15, "group": "15-18", "lesson": "A2-15",
        "kanji": "耳", "kana": "みみ", "accepted": ["みみ"],
        "hv": "NHĨ", "vi": "tai",
        "note": "耳 (NHĨ = tai) đọc là みみ. Dễ nhớ: hai vòng chữ み lặp lại như đôi tai.",
        "traps": [{"wrong": ["め", "て"], "why": "耳 (NHĨ = tai) đọc là みみ (không nhầm với 目 = め 'mắt')."}]
    },
    {
        "id": "k1518_16", "stt": 16, "group": "15-18", "lesson": "A2-18",
        "kanji": "去年", "kana": "きょねん", "accepted": ["きょねん"],
        "hv": "KHỨ NIÊN", "vi": "năm ngoái",
        "note": "去 (KHỨ = きょ, âm ghép có ょ nhỏ!) + 年 (NIÊN = ねん). Đừng gõ trường âm う thành きょうねん!",
        "traps": [{"wrong": ["きょうねん", "きよねん", "らいねん"], "why": "Bẫy kinh điển! 去 đọc ngắn là きょ (KHÔNG có trường âm う, tránh gõ thành きょうねん hay きよねん)."}]
    },
    {
        "id": "k1518_17", "stt": 17, "group": "15-18", "lesson": "A2-16",
        "kanji": "外国", "kana": "がいこく", "accepted": ["がいこく"],
        "hv": "NGOẠI QUỐC", "vi": "nước ngoài",
        "note": "外 (NGOẠI = がい) + 国 (QUỐC = こく). Để ý đục âm ở chữ đầu がい, chữ sau こく KHÔNG có đục âm.",
        "traps": [{"wrong": ["かいこく", "がいごく", "そとくに"], "why": "Đọc đúng đục âm: がい (có tenten) + こく (không tenten) ➔ がいこく."}]
    },
    {
        "id": "k1518_18", "stt": 18, "group": "15-18", "lesson": "A2-17",
        "kanji": "計ります", "kana": "はかります", "accepted": ["はかります"],
        "hv": "KẾ", "vi": "đo, cân, tính",
        "note": "Chữ 計 đứng trong 時計 (とけい), 会計 (かいけい) đọc là けい, nhưng khi làm động từ 計ります lại đọc Kun'yomi là はかります!",
        "traps": [{"wrong": ["けいります", "とけいます", "わかります"], "why": "Bẫy cực hay sai! 計 trong 時計 đọc là けい, nhưng động từ 計ります ('đo/cân') đọc bằng âm Kun là はかります."}]
    },
    {
        "id": "k1518_19", "stt": 19, "group": "15-18", "lesson": "A2-15",
        "kanji": "運転手", "kana": "うんてんしゅ", "accepted": ["うんてんしゅ"],
        "hv": "VẬN CHUYỂN THỦ", "vi": "tài xế, lái xe",
        "note": "運転 (VẬN CHUYỂN = うんてん 'lái xe') + 手 (THỦ = しゅ 'người làm nghề...'). Chú ý âm ghép しゅ, KHÔNG có trường âm う!",
        "traps": [{"wrong": ["うんてんて", "うんてんしゅう", "うんてんしゆ"], "why": "Chữ 手 chỉ nghề nghiệp đọc ngắn là しゅ (ゅ nhỏ, không kéo dài thành しゅう và không đọc て)."}]
    },
    {
        "id": "k1518_20", "stt": 20, "group": "15-18", "lesson": "A2-18",
        "kanji": "今朝", "kana": "けさ", "accepted": ["けさ"],
        "hv": "KIM TRIỀU", "vi": "sáng nay",
        "note": "Từ BẤT QUY TẮC: 今朝 đọc là けさ (không đọc こんあさ hay いまあさ!). Đối chiếu 今年 (ことし - năm nay), 今日 (きょう - hôm nay).",
        "traps": [{"wrong": ["こんあさ", "いまあさ", "こんちょう"], "why": "Bất quy tắc đặc biệt! 今朝 đọc gộp thuộc lòng là けさ (không đọc こんあさ hay いまあさ)."}]
    },
    {
        "id": "k1518_21", "stt": 21, "group": "15-18", "lesson": "A2-16",
        "kanji": "泳ぎます", "kana": "およぎます", "accepted": ["およぎます"],
        "hv": "VỊNH", "vi": "bơi",
        "note": "Chú ý đục âm ở chữ ぎ: お・よ・ぎ・ま・す (Nhóm I, thể て = およいで, thể ない = およがない).",
        "traps": [{"wrong": ["およきます", "えいぎます", "すいぎます"], "why": "Có tenten ở chữ ぎ! Đọc là およぎます (không phải およきます)."}]
    },
    {
        "id": "k1518_22", "stt": 22, "group": "15-18", "lesson": "A2-16",
        "kanji": "毎週", "kana": "まいしゅう", "accepted": ["まいしゅう"],
        "hv": "MỖI CHU", "vi": "hằng tuần, mỗi tuần",
        "note": "毎 (まい) + 週 (しゅう, có ゅ nhỏ và trường âm う).",
        "traps": [{"wrong": ["まいしゅ", "まいじゅう", "まいしゆう"], "why": "週 là しゅう (chữ ゅ nhỏ + trường âm う ➔ まいしゅう)."}]
    },
    {
        "id": "k1518_23", "stt": 23, "group": "15-18", "lesson": "A2-15",
        "kanji": "手", "kana": "て", "accepted": ["て"],
        "hv": "THỦ", "vi": "tay",
        "note": "Đứng một mình đọc là て. Khi ghép nghề nghiệp đọc là しゅ (歌手, 運転手); đặc biệt 上手 (じょうず), 下手 (へた).",
        "traps": [{"wrong": ["しゅ", "め", "あし"], "why": "手 đứng một mình chỉ bộ phận cơ thể đọc là て."}]
    },
    {
        "id": "k1518_24", "stt": 24, "group": "15-18", "lesson": "A2-18",
        "kanji": "作家", "kana": "さっか", "accepted": ["さっか"],
        "hv": "TÁC GIA", "vi": "tác giả, nhà văn",
        "note": "BIẾN ÂM NGẮT っ! さく + か biến âm thành さっか. Rất hay thiếu chữ っ nhỏ! Phân biệt với 画家 (がか - họa sĩ, không có っ).",
        "traps": [{"wrong": ["さか", "さくか", "さくいえ"], "why": "Chữ 作 (さく) gặp 家 (か) biến âm ngắt thành っ ➔ さっか (chứ không phải さか hay さくか)."}]
    },
    {
        "id": "k1518_25", "stt": 25, "group": "15-18", "lesson": "A2-17",
        "kanji": "時計", "kana": "とけい", "accepted": ["とけい"],
        "hv": "THỜI KẾ", "vi": "đồng hồ",
        "note": "Ghép Kun + On: 時 (と) + 計 (けい). Đừng nhầm thành じけい hay thiếu trường âm い ở けい.",
        "traps": [{"wrong": ["じけい", "とけ", "ときけい"], "why": "Từ đặc biệt đọc là とけい (có chữ い ở cuối けい, chữ đầu đọc と chứ không phải じ)."}]
    },
    {
        "id": "k1518_26", "stt": 26, "group": "15-18", "lesson": "A2-15",
        "kanji": "頭", "kana": "あたま", "accepted": ["あたま"],
        "hv": "ĐẦU", "vi": "đầu",
        "note": "頭 (ĐẦU = đầu) đọc là あたま. Mẫu hay gặp: 頭がいい (thông minh), 頭が痛い (đau đầu).",
        "traps": [{"wrong": ["からだ", "かお", "とう"], "why": "頭 đứng một mình đọc là あたま ('đầu'). Không nhầm với 体 (からだ - cơ thể)."}]
    },
    {
        "id": "k1518_27", "stt": 27, "group": "15-18", "lesson": "A2-16",
        "kanji": "週末", "kana": "しゅうまつ", "accepted": ["しゅうまつ"],
        "hv": "CHU MẠT", "vi": "cuối tuần",
        "note": "週 (しゅう - có trường âm う!) + 末 (まつ - âm cuối つ). Gặp thường xuyên ở các bài A2.",
        "traps": [{"wrong": ["しゅまつ", "しゅうまち", "しゆうまつ"], "why": "Chú ý 週 là しゅう (ゅ nhỏ + trường âm う) và 末 là まつ ➔ しゅうまつ."}]
    },
    {
        "id": "k1518_28", "stt": 28, "group": "15-18", "lesson": "A2-18",
        "kanji": "思います", "kana": "おもいます", "accepted": ["おもいます"],
        "hv": "TƯ", "vi": "nghĩ, cho rằng",
        "note": "Ngữ pháp trọng tâm Bài 18: 〈ふつうけい〉＋と思います. Động từ nhóm I đọc là おもいます.",
        "traps": [{"wrong": ["おもうます", "しみます", "おみます"], "why": "思います đọc là お・も・い・ま・す (Nhóm I, thể từ điển là おもう)."}]
    },
    {
        "id": "k1518_29", "stt": 29, "group": "15-18", "lesson": "A2-18",
        "kanji": "今月", "kana": "こんげつ", "accepted": ["こんげつ"],
        "hv": "KIM NGUYỆT", "vi": "tháng này",
        "note": "今 (こん) + 月 (げつ - có đục âm げ!). Không đọc こんがつ hay こんつき.",
        "traps": [{"wrong": ["こんがつ", "こんつき", "こんけつ"], "why": "月 chỉ 'tháng này' đọc là げつ (có tenten げ) ➔ こんげつ."}]
    },
    {
        "id": "k1518_30", "stt": 30, "group": "15-18", "lesson": "A2-15",
        "kanji": "全体", "kana": "ぜんたい", "accepted": ["ぜんたい"],
        "hv": "TOÀN THỂ", "vi": "toàn thể, toàn bộ",
        "note": "全 (ぜん - có đục âm ぜ!) + 体 (たい). Phân biệt 体 đứng một mình đọc からだ (cơ thể), ghép Hán đọc たい (全体 ぜんたい).",
        "traps": [{"wrong": ["せんたい", "ぜんからだ", "ぜんてい"], "why": "全 có tenten đọc là ぜん, ghép với 体 đọc âm On là たい ➔ ぜんたい."}]
    },
    {
        "id": "k1518_31", "stt": 31, "group": "15-18", "lesson": "A2-18",
        "kanji": "画家", "kana": "がか", "accepted": ["がか"],
        "hv": "HỌA GIA", "vi": "họa sĩ",
        "note": "画 (が) + 家 (か). KHÔNG có âm ngắt っ (khác với 作家 さっか!). Đứng một mình chữ 絵 là え (tranh).",
        "traps": [{"wrong": ["がっか", "えか", "かか"], "why": "Bẫy so với 作家 (さっか): 画家 KHÔNG có chữ っ nhỏ mà đọc liền がか (が có tenten, か không tenten)."}]
    },
    {
        "id": "k1518_32", "stt": 32, "group": "15-18", "lesson": "A2-16",
        "kanji": "歩きます", "kana": "あるきます", "accepted": ["あるきます"],
        "hv": "BỘ", "vi": "đi bộ",
        "note": "Động từ nhóm I: 歩きます (あるきます). Dễ nhầm với 走ります (はしります - chạy).",
        "traps": [{"wrong": ["はしります", "ほきます", "あきます"], "why": "歩きます đọc là あるきます ('đi bộ'). Đừng nhầm với 走ります (はしります - chạy)."}]
    },
    {
        "id": "k1518_33", "stt": 33, "group": "15-18", "lesson": "A2-16",
        "kanji": "毎月", "kana": "まいげつ", "accepted": ["まいげつ", "まいつき", "まいげつまいつき"],
        "hv": "MỖI NGUYỆT", "vi": "hằng tháng, mỗi tháng",
        "note": "Theo bảng PDF có 2 cách đọc đều đúng: まいげつ hoặc まいつき (hội thoại hay dùng まいつき, văn viết/hành chính hay dùng まいげつ).",
        "traps": [{"wrong": ["まいがつ", "まいけつ"], "why": "毎月 có 2 cách đọc đúng là まいげつ (có tenten げ) hoặc まいつき (không đọc まいがつ)."}]
    },
    {
        "id": "k1518_34", "stt": 34, "group": "15-18", "lesson": "A2-17",
        "kanji": "結婚", "kana": "けっこん", "accepted": ["けっこん"],
        "hv": "KẾT HÔN", "vi": "kết hôn, hôn nhân",
        "note": "ÂM NGẮT っ! 結 (けつ) + 婚 (こん) biến âm thành けっこん. Tránh thiếu chữ っ hoặc gõ nhầm けつこん.",
        "traps": [{"wrong": ["けこん", "けつこん", "けっこ"], "why": "Chữ 結 biến âm thành けっ (có っ nhỏ) và giữ ん cuối ➔ けっこん."}]
    },
    {
        "id": "k1518_35", "stt": 35, "group": "15-18", "lesson": "A2-15",
        "kanji": "目的", "kana": "もくてき", "accepted": ["もくてき"],
        "hv": "MỤC ĐÍCH", "vi": "mục đích",
        "note": "目 ghép từ Hán Việt đọc là もく (khác với 目 đứng một mình là め) + 的 (てき) ➔ もくてき.",
        "traps": [{"wrong": ["めてき", "もくでき", "もってい"], "why": "目 trong từ ghép đọc On'yomi là もく, 的 là てき (không tenten) ➔ もくてき."}]
    },
    {
        "id": "k1518_36", "stt": 36, "group": "15-18", "lesson": "A2-17",
        "kanji": "お祝い", "kana": "おいわい", "accepted": ["おいわい"],
        "hv": "CHÚC", "vi": "lời chúc, quà mừng",
        "note": "Trong ghi chú L17 có cụm そつぎょうの おいわいに (làm quà mừng tốt nghiệp). Đọc là お・い・わ・い (chú ý わ rồi い).",
        "traps": [{"wrong": ["おしゅく", "おいわ", "おゆわい"], "why": "Chữ 祝 trong danh từ お祝い đọc Kun là いわい ➔ おいわい (không đọc おゆわい hay thiếu chữ い cuối)."}]
    },
    {
        "id": "k1518_37", "stt": 37, "group": "15-18", "lesson": "A2-16",
        "kanji": "起きます", "kana": "おきます", "accepted": ["おきます"],
        "hv": "KHỞI", "vi": "thức dậy",
        "note": "Động từ nhóm II đặc biệt (đuôi i-masu nhưng thuộc nhóm II!): 起きます (おきます). Phân biệt mặt chữ 走ります (はしります) & 起きます!",
        "traps": [{"wrong": ["はしります", "ねます", "ききます"], "why": "Chữ 起 (KHỞI = thức dậy) đọc là おきます. Chú ý bộ 走 + 己 bên phải!"}]
    },
    {
        "id": "k1518_38", "stt": 38, "group": "15-18", "lesson": "A2-18",
        "kanji": "家", "kana": "いえ", "accepted": ["いえ"],
        "hv": "GIA", "vi": "nhà",
        "note": "Đứng một mình ở A2 Bài 15-18 đọc là いえ (tài liệu nhà ở: 家 = いえ). Khi ghép 家族 đọc かぞく, 作家 đọc さっか.",
        "traps": [{"wrong": ["うち", "か", "かぞく"], "why": "Trong bảng Kanji L15-18, 家 (GIA) đọc là いえ (không phải うち — từ うち thường viết bằng Kana hoặc 内)."}]
    },
    {
        "id": "k1518_39", "stt": 39, "group": "15-18", "lesson": "A2-17",
        "kanji": "会計", "kana": "かいけい", "accepted": ["かいけい"],
        "hv": "HỘI KẾ", "vi": "tính tiền, thanh toán",
        "note": "会 (かい, L13 会います) + 計 (けい, giống trong 時計 とけい) ➔ かいけい. Đừng quên hai chữ い!",
        "traps": [{"wrong": ["かいけ", "かけい", "あいけい"], "why": "Cả hai chữ đều kết thúc bằng い: かい + けい = かいけい."}]
    },
    {
        "id": "k1518_40", "stt": 40, "group": "15-18", "lesson": "A2-16",
        "kanji": "走ります", "kana": "はしります", "accepted": ["はしります"],
        "hv": "TẨU", "vi": "chạy",
        "note": "Động từ nhóm I (nhìn ngoài tưởng nhóm II vì đuôi -irimasu nhưng 走ります thuộc NHÓM I ➔ はしらない, はしって!).",
        "traps": [{"wrong": ["あるきます", "おきます", "そうります"], "why": "走ります (TẨU = chạy) đọc là はしります. Tránh nhầm mặt chữ với 起きます (おきます) hay nghĩa với 歩きます (あるきます)."}]
    },
    {
        "id": "k1518_41", "stt": 41, "group": "15-18", "lesson": "A2-15",
        "kanji": "足", "kana": "あし", "accepted": ["あし"],
        "hv": "TÚC", "vi": "chân",
        "note": "Đứng một mình đọc あし (chân). Khi chia động từ 足ります đọc là たります (đủ).",
        "traps": [{"wrong": ["たり", "そく", "て"], "why": "足 đứng một mình chỉ bộ phận cơ thể đọc là あし ('chân')."}]
    },
    {
        "id": "k1518_42", "stt": 42, "group": "15-18", "lesson": "A2-15",
        "kanji": "上手", "kana": "じょうず", "accepted": ["じょうず"],
        "hv": "THƯỢNG THỦ", "vi": "giỏi, khéo",
        "note": "Tính từ な đặc biệt: 上 (じょう - ょ nhỏ + trường âm う + じ có tenten!) + 手 (ず - có tenten!).",
        "traps": [{"wrong": ["じょうしゅ", "じょず", "うえのて", "しょうず"], "why": "Cách đọc đặc biệt rất hay sai chính tả: じょう (có tenten じ, ょ nhỏ và trường âm う) + ず (có tenten ở ず)!"}]
    },
    {
        "id": "k1518_43", "stt": 43, "group": "15-18", "lesson": "A2-15",
        "kanji": "歌手", "kana": "かしゅ", "accepted": ["かしゅ"],
        "hv": "CA THỦ", "vi": "ca sĩ",
        "note": "歌 (か) + 手 (しゅ - ゅ nhỏ, KHÔNG có trường âm う!). Giống chữ 手 trong 運転手 (うんてんしゅ).",
        "traps": [{"wrong": ["かて", "かしゅう", "うたて", "かしゆ"], "why": "Chữ 手 chỉ nghề nghiệp đọc là しゅ (ngắn, ゅ nhỏ, không có trường âm う)."}]
    },
    {
        "id": "k1518_44", "stt": 44, "group": "15-18", "lesson": "A2-18",
        "kanji": "家族", "kana": "かぞく", "accepted": ["かぞく"],
        "hv": "GIA TỘC", "vi": "gia đình",
        "note": "家 (か) + 族 (ぞく - có đục âm ở ぞ!).",
        "traps": [{"wrong": ["かそく", "いえぞく", "かずく"], "why": "族 đọc có đục âm ぞ: か・ぞ・く (không phải かそく)."}]
    },
    {
        "id": "k1518_45", "stt": 45, "group": "15-18", "lesson": "A2-17",
        "kanji": "絵", "kana": "え", "accepted": ["え"],
        "hv": "HỘI", "vi": "tranh, bức tranh",
        "note": "Chỉ có đúng 1 âm tiết え! Có mặt trong câu Kaiwa Mid 2 #10: 父が買った絵 (ちちが かった え).",
        "traps": [{"wrong": ["かい", "が", "しゃしん"], "why": "Chữ 絵 (tranh) đứng một mình đọc rất ngắn gọn là え (không đọc が như trong 画家)."}]
    },
    {
        "id": "k1518_46", "stt": 46, "group": "15-18", "lesson": "A2-15",
        "kanji": "上", "kana": "うえ", "accepted": ["うえ"],
        "hv": "THƯỢNG", "vi": "trên, bên trên",
        "note": "Đứng một mình chỉ vị trí: うえ. Ghép thành 上手 đọc じょうず.",
        "traps": [{"wrong": ["した", "じょう"], "why": "上 đứng một mình đọc là うえ ('bên trên'). Đừng nhầm với 下 (した - bên dưới)."}]
    },
    {
        "id": "k1518_47", "stt": 47, "group": "15-18", "lesson": "A2-15",
        "kanji": "体", "kana": "からだ", "accepted": ["からだ"],
        "hv": "THỂ", "vi": "cơ thể",
        "note": "Đứng một mình đọc là からだ (chữ だ có đục âm!). Ghép trong 全体 đọc là ぜんたい.",
        "traps": [{"wrong": ["からた", "たい", "あたま"], "why": "Chữ cuối là だ (có tenten!): からだ (cơ thể)."}]
    },
    {
        "id": "k1518_48", "stt": 48, "group": "15-18", "lesson": "A2-17",
        "kanji": "誕生日", "kana": "たんじょうび", "accepted": ["たんじょうび"],
        "hv": "ĐẢN SINH NHẬT", "vi": "sinh nhật",
        "note": "誕 (たん) + 生 (じょう - ょ nhỏ + trường âm う!) + 日 (び - đục âm!). Gặp trong Bài 17!",
        "traps": [{"wrong": ["たんじょうひ", "たんじょび", "たんしょうび"], "why": "Coi chừng 2 chỗ hay gõ thiếu: じょう (có じ có tenten + ょ nhỏ + う) và chữ cuối là び (có tenten)!"}]
    },
    {
        "id": "k1518_49", "stt": 49, "group": "15-18", "lesson": "A2-16",
        "kanji": "毎朝", "kana": "まいあさ", "accepted": ["まいあさ"],
        "hv": "MỖI TRIỀU", "vi": "mỗi sáng, hằng sáng",
        "note": "毎 (まい) + 朝 (あさ). Tránh nhầm với 今朝 (けさ - sáng nay!).",
        "traps": [{"wrong": ["まいけさ", "けさ", "まいちょう"], "why": "朝 đi với 毎 đọc bình thường là あさ ➔ まいあさ (chỉ có 今朝 mới đọc bất quy tắc thành けさ)."}]
    },
    {
        "id": "k1518_50", "stt": 50, "group": "15-18", "lesson": "A2-17",
        "kanji": "真面目", "kana": "まじめ", "accepted": ["まじめ"],
        "hv": "CHÂN DIỆN MỤC", "vi": "nghiêm túc, chăm chỉ",
        "note": "Tính từ đuôi な (真面目な / 真面目です). Đọc là ま・じ・め (không liên quan gì tới âm đọc thường của 目 là め đâu nhưng phần cuối vẫn giữ め!).",
        "traps": [{"wrong": ["まめ", "しんめんもく", "まもくめ"], "why": "Từ Jukujikun đọc thuộc lòng là まじめ (chú ý có じ có tenten ở giữa!)."}]
    },
]

# 69 items strictly verified from Kanji_Lesson_11-14.pdf
KANJI_11_14_ITEMS = [
    {"id": "k1114_01", "stt": 1, "group": "11-14", "lesson": "A2-14", "kanji": "電子レンジ", "kana": "でんしレンジ", "accepted": ["でんしレンジ", "でんしれんじ"], "hv": "ĐIỆN TỬ", "vi": "lò vi sóng", "note": "電 (でん) + 子 (し) + レンジ (Katakana, nhập でんしレンジ hay でんしれんじ đều được chấm đúng)."},
    {"id": "k1114_02", "stt": 2, "group": "11-14", "lesson": "A2-14", "kanji": "電車", "kana": "でんしゃ", "accepted": ["でんしゃ"], "hv": "ĐIỆN XA", "vi": "tàu điện", "note": "電 (でん) + 車 (しゃ - ゃ nhỏ). Khác với 車 đứng một mình là くるま."},
    {"id": "k1114_03", "stt": 3, "group": "11-14", "lesson": "A2-13", "kanji": "着ます", "kana": "きます", "accepted": ["きます"], "hv": "TRƯỚC", "vi": "mặc", "note": "Không có き ở thân ➔ 着ます (きます = mặc). Có き ở thân ➔ 着きます (つきます = đến nơi)."},
    {"id": "k1114_04", "stt": 4, "group": "11-14", "lesson": "A2-14", "kanji": "電話", "kana": "でんわ", "accepted": ["でんわ"], "hv": "ĐIỆN THOẠI", "vi": "điện thoại", "note": "電 (でん) + 話 (わ)."},
    {"id": "k1114_05", "stt": 5, "group": "11-14", "lesson": "A2-13", "kanji": "出かけます", "kana": "でかけます", "accepted": ["でかけます"], "hv": "XUẤT", "vi": "đi ra ngoài", "note": "Động từ nhóm II: 出かけます (でかけます). Phân biệt 出ます (でます) và 出します (だします)."},
    {"id": "k1114_06", "stt": 6, "group": "11-14", "lesson": "A2-12", "kanji": "仕事中", "kana": "しごとちゅう", "accepted": ["しごとちゅう"], "hv": "SỰ SĨ TRUNG", "vi": "đang làm việc", "note": "Cụm [N]+中 mang nghĩa 'đang trong lúc...' đọc là ちゅう (chữ ゅ nhỏ + trường âm う)."},
    {"id": "k1114_07", "stt": 7, "group": "11-14", "lesson": "A2-13", "kanji": "到着", "kana": "とうちゃく", "accepted": ["とうちゃく"], "hv": "ĐÁO TRƯỚC", "vi": "đến nơi", "note": "到 (とう - có trường âm う!) + 着 (ちゃく - ゃ nhỏ!)."},
    {"id": "k1114_08", "stt": 8, "group": "11-14", "lesson": "A2-11", "kanji": "日本酒", "kana": "にほんしゅ", "accepted": ["にほんしゅ", "にっぽんしゅ"], "hv": "NHẬT BẢN TỬU", "vi": "rượu Nhật, sake", "note": "日本 (にほん) + 酒 (しゅ - ゅ nhỏ, không trường âm う!)."},
    {"id": "k1114_09", "stt": 9, "group": "11-14", "lesson": "A2-12", "kanji": "味", "kana": "あじ", "accepted": ["あじ"], "hv": "VỊ", "vi": "vị, hương vị", "note": "Đứng một mình đọc là あじ (じ có tenten!). Ghép trong 地味 đọc là じみ."},
    {"id": "k1114_10", "stt": 10, "group": "11-14", "lesson": "A2-11", "kanji": "お茶", "kana": "おちゃ", "accepted": ["おちゃ"], "hv": "TRÀ", "vi": "trà", "note": "お + ちゃ (ゃ nhỏ)."},
    {"id": "k1114_11", "stt": 11, "group": "11-14", "lesson": "A2-11", "kanji": "お酒", "kana": "おさけ", "accepted": ["おさけ"], "hv": "TỬU", "vi": "rượu", "note": "酒 đứng sau お đọc Kun'yomi là おさけ; ghép Hán Việt như 日本酒 đọc là にほんしゅ."},
    {"id": "k1114_12", "stt": 12, "group": "11-14", "lesson": "A2-14", "kanji": "人気", "kana": "にんき", "accepted": ["にんき"], "hv": "NHÂN KHÍ", "vi": "được yêu thích, nổi tiếng", "note": "Coi chừng nhầm sang ひとき hoặc じんき! Đây là từ đặc biệt đọc にんき (Nhân = にん)."},
    {"id": "k1114_13", "stt": 13, "group": "11-14", "lesson": "A2-12", "kanji": "資料", "kana": "しりょう", "accepted": ["しりょう"], "hv": "TƯ LIỆU", "vi": "tài liệu", "note": "資 (し) + 料 (りょう - ょ nhỏ + trường âm う!). Phân biệt 料理 (りょうり)."},
    {"id": "k1114_14", "stt": 14, "group": "11-14", "lesson": "A2-11", "kanji": "喫茶店", "kana": "きっさてん", "accepted": ["きっさてん"], "hv": "KHIẾT TRÀ ĐIẾM", "vi": "quán cà phê, quán giải khát", "note": "Có âm ngắt っ nhỏ: きっさてん (gặp nhiều ở Bài 17!)."},
    {"id": "k1114_15", "stt": 15, "group": "11-14", "lesson": "A2-11", "kanji": "乗り物", "kana": "のりもの", "accepted": ["のりもの"], "hv": "THỪA VẬT", "vi": "phương tiện đi lại", "note": "Cụm [Vます bỏ ます] + 物 (もの): 乗ります ➔ のりもの."},
    {"id": "k1114_16", "stt": 16, "group": "11-14", "lesson": "A2-13", "kanji": "空港", "kana": "くうこう", "accepted": ["くうこう"], "hv": "KHÔNG CẢNG", "vi": "sân bay", "note": "Cả 2 chữ đều có trường âm う: 空 (くう) + 港 (こう) ➔ くうこう."},
    {"id": "k1114_17", "stt": 17, "group": "11-14", "lesson": "A2-13", "kanji": "会います", "kana": "あいます", "accepted": ["あいます"], "hv": "HỘI", "vi": "gặp", "note": "会います đọc là あいます (gặp trong Bài 18 ～と会わない)."},
    {"id": "k1114_18", "stt": 18, "group": "11-14", "lesson": "A2-11", "kanji": "作文", "kana": "さくぶん", "accepted": ["さくぶん"], "hv": "TÁC VĂN", "vi": "bài văn, bài viết", "note": "作 (さく) + 文 (ぶん - có tenten ở ぶ!)."},
    {"id": "k1114_19", "stt": 19, "group": "11-14", "lesson": "A2-14", "kanji": "使います", "kana": "つかいます", "accepted": ["つかいます"], "hv": "SỬ", "vi": "sử dụng", "note": "Gặp nhiều trong Bài 15-18 (使って/使う/使わないで)."},
    {"id": "k1114_20", "stt": 20, "group": "11-14", "lesson": "A2-11", "kanji": "飲み物", "kana": "のみもの", "accepted": ["のみもの"], "hv": "ẨM VẬT", "vi": "đồ uống", "note": "飲 (のみ) + 物 (もの)."},
    {"id": "k1114_21", "stt": 21, "group": "11-14", "lesson": "A2-12", "kanji": "中止", "kana": "ちゅうし", "accepted": ["ちゅうし"], "hv": "TRUNG CHỈ", "vi": "hoãn, hủy, ngừng", "note": "中 (ちゅう - có ゅ nhỏ + trường âm う!) + 止 (し)."},
    {"id": "k1114_22", "stt": 22, "group": "11-14", "lesson": "A2-12", "kanji": "一年中", "kana": "いちねんじゅう", "accepted": ["いちねんじゅう"], "hv": "NHẤT NIÊN TRUNG", "vi": "quanh năm", "note": "Biến đục âm đặc biệt ở 中: 'cả năm/quanh năm' đọc じゅう (có tenten じ!), khác với 仕事中 (ちゅう)."},
    {"id": "k1114_23", "stt": 23, "group": "11-14", "lesson": "A2-12", "kanji": "中", "kana": "なか", "accepted": ["なか"], "hv": "TRUNG", "vi": "trong, bên trong", "note": "Đứng một mình chỉ vị trí đọc là なか (có trong Bài 18: おかしの中で)."},
    {"id": "k1114_24", "stt": 24, "group": "11-14", "lesson": "A2-11", "kanji": "荷物", "kana": "にもつ", "accepted": ["にもつ"], "hv": "HÀ VẬT", "vi": "hành lý, đồ đạc", "note": "荷 (に) + 物 (もつ - khác với もの trong 食べ物/飲み物!)."},
    {"id": "k1114_25", "stt": 25, "group": "11-14", "lesson": "A2-13", "kanji": "支社", "kana": "ししゃ", "accepted": ["ししゃ"], "hv": "CHI XÃ", "vi": "chi nhánh công ty", "note": "支 (し) + 社 (しゃ - ゃ nhỏ). Đối chiếu 本社 (ほんしゃ - trụ sở chính)."},
    {"id": "k1114_26", "stt": 26, "group": "11-14", "lesson": "A2-13", "kanji": "発音", "kana": "はつおん", "accepted": ["はつおん"], "hv": "PHÁT ÂM", "vi": "phát âm", "note": "Khác với 出発 (しゅっぱつ có âm ngắt っ): 発音 KHÔNG biến âm っ mà đọc đủ はつおん."},
    {"id": "k1114_27", "stt": 27, "group": "11-14", "lesson": "A2-14", "kanji": "自由", "kana": "じゆう", "accepted": ["じゆう"], "hv": "TỰ DO", "vi": "tự do", "note": "Chú ý chữ ゆ TO (không nhỏ!) + trường âm う ➔ じ・ゆ・う!"},
    {"id": "k1114_28", "stt": 28, "group": "11-14", "lesson": "A2-13", "kanji": "空", "kana": "そら", "accepted": ["そら"], "hv": "KHÔNG", "vi": "bầu trời", "note": "Đứng một mình đọc そら ('bầu trời'). Ghép từ Hán đọc くう (空気 くうき, 空港 くうこう)."},
    {"id": "k1114_29", "stt": 29, "group": "11-14", "lesson": "A2-13", "kanji": "本社", "kana": "ほんしゃ", "accepted": ["ほんしゃ"], "hv": "BẢN XÃ", "vi": "trụ sở chính", "note": "本 (ほん) + 社 (しゃ - ゃ nhỏ)."},
    {"id": "k1114_30", "stt": 30, "group": "11-14", "lesson": "A2-12", "kanji": "料理", "kana": "りょうり", "accepted": ["りょうり"], "hv": "LIỆU LÝ", "vi": "món ăn, nấu ăn", "note": "Chú ý trường âm đầu りょう (ょ nhỏ + う), gặp nhiều trong Bài 16-18."},
    {"id": "k1114_31", "stt": 31, "group": "11-14", "lesson": "A2-14", "kanji": "電気", "kana": "でんき", "accepted": ["でんき"], "hv": "ĐIỆN KHÍ", "vi": "điện", "note": "Chú ý phân biệt với 元気 (げんき) và 病気 (びょうき)! Trong Bài 18 có cụm 電気バイク (xe máy điện)."},
    {"id": "k1114_32", "stt": 32, "group": "11-14", "lesson": "A2-13", "kanji": "出発", "kana": "しゅっぱつ", "accepted": ["しゅっぱつ"], "hv": "XUẤT PHÁT", "vi": "khởi hành", "note": "Bán đục âm + âm ngắt: しゅ・っ・ぱ・つ (ぱ có maru ゜, xuất hiện trong Bài 17 hội thoại #5!)."},
    {"id": "k1518_aux_33" if False else "k1114_33", "stt": 33, "group": "11-14", "lesson": "A2-11", "kanji": "作ります", "kana": "つくります", "accepted": ["つくります"], "hv": "TÁC", "vi": "làm, chế tạo", "note": "Động từ nhóm I: 作ります (つくります ➔ 作らない / 作った)."},
    {"id": "k1114_34", "stt": 34, "group": "11-14", "lesson": "A2-11", "kanji": "願い事", "kana": "ねがいごと", "accepted": ["ねがいごと"], "hv": "NGUYỆN SỰ", "vi": "điều ước, nguyện vọng", "note": "Biến đục âm ご: ねがい + ごと (có tenten ở ご!)."},
    {"id": "k1114_35", "stt": 35, "group": "11-14", "lesson": "A2-11", "kanji": "お願い", "kana": "おねがい", "accepted": ["おねがい"], "hv": "NGUYỆN", "vi": "lời nhờ, yêu cầu", "note": "Danh từ dùng trong Bài 17: ちょっとお願いがあるんですが…"},
    {"id": "k1114_36", "stt": 36, "group": "11-14", "lesson": "A2-14", "kanji": "送ります", "kana": "おくります", "accepted": ["おくります"], "hv": "TỐNG", "vi": "gửi", "note": "お・く・り・ま・す. Tránh nhầm với おきます (起きます - thức dậy)."},
    {"id": "k1114_37", "stt": 37, "group": "11-14", "lesson": "A2-11", "kanji": "持ちます", "kana": "もちます", "accepted": ["もちます"], "hv": "TRÌ", "vi": "cầm, mang, có", "note": "Gặp trong Bài 18 #1: 持ってこない (もってこない)."},
    {"id": "k1114_38", "stt": 38, "group": "11-14", "lesson": "A2-12", "kanji": "野菜", "kana": "やさい", "accepted": ["やさい"], "hv": "DÃ THÁI", "vi": "rau củ", "note": "Gặp rất nhiều ở Bài 16 & Bài 18 (野菜を食べない子ども / 野菜のほうが健康にいい)."},
    {"id": "k1114_39", "stt": 39, "group": "11-14", "lesson": "A2-13", "kanji": "会社員", "kana": "かいしゃいん", "accepted": ["かいしゃいん"], "hv": "HỘI XÃ VIÊN", "vi": "nhân viên công ty", "note": "かい + しゃ + いん."},
    {"id": "k1114_40", "stt": 40, "group": "11-14", "lesson": "A2-13", "kanji": "入社", "kana": "にゅうしゃ", "accepted": ["にゅうしゃ"], "hv": "NHẬP XÃ", "vi": "vào công ty, gia nhập công ty", "note": "入 (にゅう - ゅ nhỏ + trường âm う!) + 社 (しゃ - ゃ nhỏ)."},
    {"id": "k1114_41", "stt": 41, "group": "11-14", "lesson": "A2-12", "kanji": "入ります", "kana": "はいります", "accepted": ["はいります"], "hv": "NHẬP", "vi": "vào", "note": "Tự động từ NHÓM I (coi chừng bẫy: nhìn kết thúc -irimasu nhưng vẫn là Nhóm I ➔ はいらない / はいって!)."},
    {"id": "k1114_42", "stt": 42, "group": "11-14", "lesson": "A2-14", "kanji": "自然", "kana": "しぜん", "accepted": ["しぜん"], "hv": "TỰ NHIÊN", "vi": "thiên nhiên, tự nhiên", "note": "Đục âm ở ぜ: しぜん."},
    {"id": "k1114_43", "stt": 43, "group": "11-14", "lesson": "A2-13", "kanji": "社会", "kana": "しゃかい", "accepted": ["しゃかい"], "hv": "XÃ HỘI", "vi": "xã hội", "note": "Đọc ngược âm với 会社 (かいしゃ): 社会 = しゃかい."},
    {"id": "k1114_44", "stt": 44, "group": "11-14", "lesson": "A2-12", "kanji": "入学", "kana": "にゅうがく", "accepted": ["にゅうがく"], "hv": "NHẬP HỌC", "vi": "nhập học", "note": "にゅう + がく (có tenten ở が!). Dùng trong Bài 15: 大学に入学しました."},
    {"id": "k1114_45", "stt": 45, "group": "11-14", "lesson": "A2-13", "kanji": "出張", "kana": "しゅっちょう", "accepted": ["しゅっちょう"], "hv": "XUẤT TRƯƠNG", "vi": "đi công tác", "note": "Âm ngắt っ + trường âm ょう: しゅ・っ・ちょ・う!"},
    {"id": "k1114_46", "stt": 46, "group": "11-14", "lesson": "A2-14", "kanji": "大使館", "kana": "たいしかん", "accepted": ["たいしかん"], "hv": "ĐẠI SỨ QUÁN", "vi": "đại sứ quán", "note": "大 (たい) + 使 (し) + 館 (かん)."},
    {"id": "k1114_47", "stt": 47, "group": "11-14", "lesson": "A2-13", "kanji": "出口", "kana": "でぐち", "accepted": ["でぐち"], "hv": "XUẤT KHẨU", "vi": "lối ra", "note": "Biến đục âm rendaku ở ぐ: でぐち (không đọc でくち!)."},
    {"id": "k1114_48", "stt": 48, "group": "11-14", "lesson": "A2-14", "kanji": "自分", "kana": "じぶん", "accepted": ["じぶん"], "hv": "TỰ PHÂN", "vi": "bản thân, chính mình", "note": "Cả 2 chữ đều có tenten: じ + ぶん (gặp ở Bài 18 #5: 自分で)."},
    {"id": "k1114_49", "stt": 49, "group": "11-14", "lesson": "A2-14", "kanji": "車", "kana": "くるま", "accepted": ["くるま"], "hv": "XA", "vi": "xe, ô tô", "note": "Đứng một mình đọc くるま (Kun'yomi)."},
    {"id": "k1114_50", "stt": 50, "group": "11-14", "lesson": "A2-11", "kanji": "食べ物", "kana": "たべもの", "accepted": ["たべもの"], "hv": "THỰC VẬT", "vi": "đồ ăn, thức ăn", "note": "たべ + もの."},
    {"id": "k1114_51", "stt": 51, "group": "11-14", "lesson": "A2-11", "kanji": "気持ち", "kana": "きもち", "accepted": ["きもち"], "hv": "KHÍ TRÌ", "vi": "cảm giác, tâm trạng", "note": "き + もち."},
    {"id": "k1114_52", "stt": 52, "group": "11-14", "lesson": "A2-12", "kanji": "入れます", "kana": "いれます", "accepted": ["いれます"], "hv": "NHẬP", "vi": "cho vào, bỏ vào", "note": "Tha động từ NHÓM II: いれます (khác với 入ります はいります là tự động từ 'đi vào')."},
    {"id": "k1114_53", "stt": 53, "group": "11-14", "lesson": "A2-11", "kanji": "お願いします", "kana": "おねがいします", "accepted": ["おねがいします"], "hv": "NGUYỆN", "vi": "nhờ, mong, làm ơn", "note": "お + ねがい + します."},
    {"id": "k1114_54", "stt": 54, "group": "11-14", "lesson": "A2-13", "kanji": "出します", "kana": "だします", "accepted": ["だします"], "hv": "XUẤT", "vi": "lấy ra, đưa ra, nộp", "note": "Tha động từ: だします (khác với 出ます でます 'đi ra')."},
    {"id": "k1114_55", "stt": 55, "group": "11-14", "lesson": "A2-13", "kanji": "神社", "kana": "じんじゃ", "accepted": ["じんじゃ"], "hv": "THẦN XÃ", "vi": "đền Thần đạo", "note": "Cả 2 đều đục âm: じん + じゃ (ゃ nhỏ)."},
    {"id": "k1114_56", "stt": 56, "group": "11-14", "lesson": "A2-12", "kanji": "理由", "kana": "りゆう", "accepted": ["りゆう"], "hv": "LÝ DO", "vi": "lý do", "note": "Chữ ゆ TO + trường âm う: り・ゆ・う (cần thiết cho Bài 17 hỏi lý do!)."},
    {"id": "k1114_57", "stt": 57, "group": "11-14", "lesson": "A2-14", "kanji": "借ります", "kana": "かります", "accepted": ["かります"], "hv": "TÁ", "vi": "mượn, thuê", "note": "Động từ NHÓM II đặc biệt (đuôi -irimasu nhưng vẫn Nhóm II ➔ かりない / かりて!)."},
    {"id": "k1114_58", "stt": 58, "group": "11-14", "lesson": "A2-13", "kanji": "港", "kana": "みなと", "accepted": ["みなと"], "hv": "CẢNG", "vi": "cảng", "note": "Đứng một mình đọc みなと; ghép trong 空港 đọc こう."},
    {"id": "k1114_59", "stt": 59, "group": "11-14", "lesson": "A2-14", "kanji": "自転車", "kana": "じてんしゃ", "accepted": ["じてんしゃ"], "hv": "TỰ CHUYỂN XA", "vi": "xe đạp", "note": "じ (có tenten) + てん + しゃ (ゃ nhỏ)."},
    {"id": "k1114_60", "stt": 60, "group": "11-14", "lesson": "A2-13", "kanji": "出ます", "kana": "でます", "accepted": ["でます"], "hv": "XUẤT", "vi": "ra, rời khỏi", "note": "Động từ nhóm II: でます."},
    {"id": "k1114_61", "stt": 61, "group": "11-14", "lesson": "A2-12", "kanji": "色", "kana": "いろ", "accepted": ["いろ"], "hv": "SẮC", "vi": "màu sắc", "note": "Đứng một mình đọc いろ."},
    {"id": "k1114_62", "stt": 62, "group": "11-14", "lesson": "A2-13", "kanji": "空気", "kana": "くうき", "accepted": ["くうき"], "hv": "KHÔNG KHÍ", "vi": "không khí", "note": "空 có trường âm う: くう・き."},
    {"id": "k1114_63", "stt": 63, "group": "11-14", "lesson": "A2-12", "kanji": "料金", "kana": "りょうきん", "accepted": ["りょうきん"], "hv": "LIỆU KIM", "vi": "phí, cước phí", "note": "料 đọc là りょう (ょ nhỏ + trường âm う) + きん."},
    {"id": "k1114_64", "stt": 64, "group": "11-14", "lesson": "A2-13", "kanji": "着きます", "kana": "つきます", "accepted": ["つきます"], "hv": "TRƯỚC", "vi": "đến, tới nơi", "note": "Có き giữa chữ ➔ đọc là つきます (đến nơi). Không nhầm với 着ます (きます - mặc)!"},
    {"id": "k1114_65", "stt": 65, "group": "11-14", "lesson": "A2-12", "kanji": "無理", "kana": "むり", "accepted": ["むり"], "hv": "VÔ LÝ", "vi": "không thể, quá sức", "note": "Gặp trong Bài 15: むりをしないでください (đừng làm quá sức)."},
    {"id": "k1114_66", "stt": 66, "group": "11-14", "lesson": "A2-14", "kanji": "病気", "kana": "びょうき", "accepted": ["びょうき"], "hv": "BỆNH KHÍ", "vi": "bệnh, ốm", "note": "病 đọc là びょう (び có tenten + ょ nhỏ + trường âm う!)."},
    {"id": "k1114_67", "stt": 67, "group": "11-14", "lesson": "A2-12", "kanji": "色々", "kana": "いろいろ", "accepted": ["いろいろ"], "hv": "SẮC", "vi": "nhiều loại, đa dạng", "note": "Từ láy いろいろ."},
    {"id": "k1114_68", "stt": 68, "group": "11-14", "lesson": "A2-14", "kanji": "自動車", "kana": "じどうしゃ", "accepted": ["じどうしゃ"], "hv": "TỰ ĐỘNG XA", "vi": "ô tô, xe hơi", "note": "じ + どう (trường âm う!) + しゃ (ゃ nhỏ)."},
    {"id": "k1114_69", "stt": 69, "group": "11-14", "lesson": "A2-12", "kanji": "地味", "kana": "じみ", "accepted": ["じみ"], "hv": "ĐỊA VỊ", "vi": "giản dị, không nổi bật", "note": "Tính từ đuôi な (地味な): đọc là じみ (じ có tenten!)."},
    {"id": "k1114_70", "stt": 70, "group": "11-14", "lesson": "A2-12", "kanji": "無料", "kana": "むりょう", "accepted": ["むりょう"], "hv": "VÔ LIỆU", "vi": "miễn phí", "note": "無 (VÔ = không có, む) + 料 (LIỆU = phí, りょう). Phân biệt với 有料 (ゆうりょう - có phí) và 料理 (りょうり).", "traps": [{"wrong": ["むりょ", "ぶひょう", "ゆうりょう"], "why": "Âm On là む・りょう (chú ý trường âm う ở cuối, khác 有料 là có phí)."}]},
    {"id": "k1114_71", "stt": 71, "group": "11-14", "lesson": "A2-13", "kanji": "着物", "kana": "きもの", "accepted": ["きもの"], "hv": "TRƯỚC VẬT", "vi": "bộ kimono, trang phục truyền thống Nhật", "note": "着 (TRƯỚC = mặc, き) + 物 (VẬT = đồ, もの). Đọc thuần Nhật là きもの.", "traps": [{"wrong": ["ちゃくぶつ", "きぶつ"], "why": "Từ thuần Nhật quen thuộc đọc là きもの (không đọc âm On ちゃくぶつ)."}]},
]


# Full sentence database from teacher's Classroom notes & Answer keys (L15-L18 + L17 NPBS + Kaiwa Mid 2)
SENTENCE_TYPING_DATA = [
    # ================= LESSON 15 =================
    {
        "id": "s15_01", "lesson": "A2-15", "category": "ÔN TẬP L15 ① まえに",
        "pattern": "Vる ＋ まえに",
        "vi": "Trước khi ngủ, tôi thường hay đọc sách.",
        "hira": "ねる まえに、よく ほんを よみます。",
        "acceptedHira": [
            "ねるまえに、よくほんをよみます", "ねるまえに、よくほんをよんでいます",
            "ねるまえに、ほんをよくよみます", "ねるまえに、ほんをよくよんでいます",
            "ねるまえによくほんをよみます", "ねるまえにほんをよくよみます"
        ],
        "kanjiModel": "寝る前に、よく本を読みます。（／読んでいます）",
        "kanjiAccepted": [
            "寝るまえによく本を読みます", "寝る前によく本を読みます", "ねるまえによく本を読みます", "寝るまえによく本を読んでいます",
            "寝る前に本をよく読みます", "寝るまえに本をよく読みます", "ねるまえに本をよく読みます", "寝る前に本をよく読んでいます",
            "寝る前によく本を読んでいます", "寝る前によく本をよみます"
        ],
        "grammarRule": "① Công thức 'Trước khi làm V': <b>Vる（Từ điển）＋ まえに</b>. Phải đưa động từ trước まえに về thể Từ điển (ねる, KHÔNG dùng ねます hay ねて!).",
        "breakdown": "ねる (ngủ - thể từ điển) + まえに (trước khi) + よく (thường hay) + ほんを (sách) + よみます / よんでいます (đọc).",
        "traps": [
            {"regex": "ねますまえに|ねてまえに|ねたまえに|ねないまえに", "why": "Trước 「まえに」 bắt buộc chia động từ về thể Từ điển (Vる ➔ ねる), KHÔNG dùng thể ます, て hay た!"},
            {"regex": "まえで|まえを", "why": "Sau 「まえ」 phải đi với trợ từ 「に」 (まえに), không dùng で hay を."}
        ]
    },
    {
        "id": "s15_02", "lesson": "A2-15", "category": "ÔN TẬP L15 ① まえに",
        "pattern": "N ＋ の ＋ まえに",
        "vi": "Trước bữa tối, tôi thỉnh thoảng uống nước.",
        "hira": "ばんごはんの まえに、ときどき みずを のみます。",
        "acceptedHira": [
            "ばんごはんのまえに、ときどきみずをのみます", "ゆうごはんのまえに、ときどきみずをのみます",
            "ばんごはんのまえに、みずをときどきのみます", "ゆうごはんのまえに、みずをときどきのみます",
            "ばんごはんのまえにときどきみずをのみます", "ばんごはんのまえにみずをときどきのみます"
        ],
        "kanjiModel": "晩ご飯の前に、ときどき水を飲みます。",
        "kanjiAccepted": [
            "晩ご飯の前にときどき水を飲みます", "ばんごはんの前にときどき水を飲みます", "晩ご飯のまえにときどき水を飲みます",
            "晩ご飯の前に水をときどき飲みます", "ばんごはんの前に水をときどき飲みます", "晩ご飯のまえに水をときどき飲みます"
        ],
        "grammarRule": "① Công thức với Danh từ: <b>N ＋ の ＋ まえに</b>. Nhớ phải có trợ từ 「の」 nối giữa danh từ ばんごはん và まえに!",
        "breakdown": "ばんごはん (bữa tối) + の まえに (trước khi) + ときどき (thỉnh thoảng) + みずを (nước) + のみます (uống).",
        "traps": [
            {"regex": "ばんごはんまえに", "why": "Danh từ 「ばんごはん」 đứng trước 「まえに」 BẮT BUỘC phải có trợ từ 「の」 ở giữa ➔ ばんごはんの まえに!"},
            {"regex": "ときどき.*まえに", "why": "Phó từ chỉ tần suất 「ときどき」 nên đặt sau dấu phẩy, trước hành động 「みずを のみます」."}
        ]
    },
    {
        "id": "s15_03", "lesson": "A2-15", "category": "ÔN TẬP L15 ① まえに",
        "pattern": "<Khoảng thời gian> ＋ まえに",
        "vi": "3 năm trước, tôi đã vào trường đại học này.",
        "hira": "3ねん まえに、この だいがくに はいりました。",
        "acceptedHira": ["3ねんまえに、このだいがくにはいりました", "さんねんまえに、このだいがくにはいりました", "3ねんまえに、このだいがくににゅうがくしました", "さんねんまえに、このだいがくににゅうがくしました"],
        "kanjiModel": "３年前に、この大学に入りました。（＝入学しました）",
        "kanjiAccepted": ["3年前にこの大学に入りました", "３年前にこの大学に入りました", "3ねんまえにこの大学に入りました", "3年前にこの大学に入学しました", "3年まえにこの大学に入りました"],
        "grammarRule": "① Công thức khoảng thời gian: <b>&lt;Khoảng thời gian&gt; ＋ まえに</b> (KHÔNG có 「の」 trước まえに!). Lưu ý: 大学に 入ります ＝ 大学に 入学しました.",
        "breakdown": "3ねん / さんねん (3 năm) + まえに (trước, không thêm の) + この だいがくに (vào trường đại học này) + はいりました / にゅうがくしました (đã vào học - quá khứ).",
        "traps": [
            {"regex": "ねんのまえに", "why": "Khoảng thời gian (3ねん, 2しゅうかん...) đi trực tiếp với 「まえに」, KHÔNG thêm trợ từ 「の」!"},
            {"regex": "はいります$|にゅうがくします$", "why": "Câu kể chuyện '3 năm trước ĐÃ vào đại học' nên phải chia thì quá khứ 「はいりました / にゅうがくしました」."},
            {"regex": "だいがくをはいりました", "why": "Động từ đi vào một địa điểm 「入ります」 dùng trợ từ 「に」 (だいがくに はいります), không dùng 「を」!"}
        ]
    },
    {
        "id": "s15_04", "lesson": "A2-15", "category": "ÔN TẬP L15 ② Vると いいです",
        "pattern": "Vる ＋ と いいです（よ）",
        "vi": "Khi đau đầu, bạn nên uống thuốc này thì tốt.",
        "hira": "あたまが いたい とき、この くすりを のむと いいですよ。",
        "acceptedHira": ["あたまがいたいとき、このくすりをのむといいですよ", "あたまがいたいとき、このくすりをのむといいです"],
        "kanjiModel": "頭が痛いとき、この薬を飲むといいですよ。",
        "kanjiAccepted": ["頭が痛いときこの薬を飲むといいですよ", "頭が痛いときこの薬を飲むといいです", "頭がいたいときこのくすりを飲むといいですよ"],
        "grammarRule": "② Công thức khuyên nhủ nhẹ: <b>Vる（Từ điển）＋ と いいです（よ）</b> ('Làm V thì tốt đó'). Bổ nghĩa với とき: tính từ đuôi い giữ nguyên い + とき.",
        "breakdown": "あたまが いたい とき (khi đau đầu) + この くすりを (thuốc này) + のむと いいですよ (uống thì tốt đó).",
        "traps": [
            {"regex": "のみますといいです|のんでといいです|のんだといいです", "why": "Trước 「と いいです」 động từ BẮT BUỘC phải chia về thể Từ điển (のむ, KHÔNG dùng のみます/のんで/のんだ)!"},
            {"regex": "いたいなとき|いたいのとき", "why": "Tính từ đuôi い 「いたい」 đi trực tiếp trước 「とき」 ➔ あたまが いたい とき (không thêm な hay の)!"},
            {"regex": "あたまはいたい|あたまをいたい", "why": "Bộ phận cơ thể bị đau dùng trợ từ 「が」: あたまが いたい."}
        ]
    },
    {
        "id": "s15_05", "lesson": "A2-15", "category": "ÔN TẬP L15 ② Vると いいです",
        "pattern": "Nの とき、Vると いいです",
        "vi": "Khi stress, bạn nên thong thả đi dạo ở công viên thì tốt.",
        "hira": "ストレスの とき、ゆっくり こうえんを さんぽすると いいですよ。",
        "acceptedHira": [
            "ストレスのとき、ゆっくりこうえんをさんぽするといいですよ", "すとれすのとき、ゆっくりこうえんをさんぽするといいですよ",
            "ストレスのとき、ゆっくりこうえんをさんぽするといいです", "すとれすのとき、ゆっくりこうえんをさんぽするといいです",
            "ストレスのとき、こうえんをゆっくりさんぽするといいですよ", "すとれすのとき、こうえんをゆっくりさんぽするといいですよ",
            "ストレスのとき、こうえんをゆっくりさんぽするといいです", "すとれすのとき、こうえんをゆっくりさんぽするといいです"
        ],
        "kanjiModel": "ストレスのとき、ゆっくり公園を散歩するといいですよ。",
        "kanjiAccepted": [
            "ストレスのときゆっくり公園を散歩するといいですよ", "ストレスのときゆっくり公園を散歩するといいです",
            "ストレスのとき公園をゆっくり散歩するといいですよ", "ストレスのとき公園をゆっくり散歩するといいです"
        ],
        "grammarRule": "② Danh từ 「ストレス」 nối với 「とき」 qua 「の」 (<b>ストレスの とき</b>). Điểm di chuyển đi dạo dùng trợ từ <b>を</b> (こうえんを さんぽする)! Còn ゆっくり = thong thả.",
        "breakdown": "ストレスの とき (khi stress) + ゆっくり (thong thả) + こうえんを (ở/quanh công viên) + さんぽすると いいですよ (nên đi dạo thì tốt).",
        "traps": [
            {"regex": "ストレスとき", "why": "ストレス là danh từ, đứng trước 「とき」 bắt buộc phải có trợ từ 「の」 ➔ ストレスの とき."},
            {"regex": "こうえんにさんぽ|こうえんでさんぽ", "why": "Không gian di chuyển xuyên suốt như đi dạo (さんぽする), chạy bộ (はしる), đi bộ (あるく) trong tiếng Nhật dùng trợ từ 「を」 ➔ こうえんを さんぽする!"},
            {"regex": "さんぽしますと|さんぽしてと", "why": "Trước 「と いいです」 phải đưa động từ về thể Từ điển ➔ さんぽすると いいですよ."}
        ]
    },
    {
        "id": "s15_06", "lesson": "A2-15", "category": "ÔN TẬP L15 ② Vると いいです",
        "pattern": "Vる まえに、Vると いいですよ",
        "vi": "Trước khi đi ngủ, bạn nên uống nước ấm thì tốt.",
        "hira": "ねる まえに、おゆを のむと いいですよ。",
        "acceptedHira": ["ねるまえに、おゆをのむといいですよ", "ねるまえに、おゆをのむといいです", "ねるまえに、あたたかいみずをのむといいですよ", "ねるまえに、あたたかいみずをのむといいです"],
        "kanjiModel": "寝る前に、お湯（／温かい水）を飲むといいですよ。",
        "kanjiAccepted": ["寝る前にお湯を飲むといいですよ", "寝る前に温かい水を飲むといいですよ", "寝るまえにおゆを飲むといいですよ"],
        "grammarRule": "② Kết hợp ngữ pháp L15 ① + ②: 'Nước ấm / nước nóng nhẹ' trong giáo trình là <b>おゆ</b> (hoặc <b>あたたかい みず</b>).",
        "breakdown": "ねる まえに (trước khi ngủ) + おゆを / あたたかい みずを (nước ấm) + のむと いいですよ (uống thì tốt đó).",
        "traps": [
            {"regex": "あついみず", "why": "Nước ấm theo lời cô chữa là 「おゆ」 hoặc 「あたたかい みず」 (あつい là nóng bỏng)."},
            {"regex": "ねますまえに|のみますと", "why": "Cả hai vế trước 「まえに」 và trước 「と いいです」 đều phải dùng thể Từ điển (ねる / のむ)!"}
        ]
    },
    {
        "id": "s15_07", "lesson": "A2-15", "category": "ÔN TẬP L15 ② Vると いいです",
        "pattern": "Vる まえに、Vると いいですよ",
        "vi": "Trước khi bơi, bạn nên tập thể dục kỹ.",
        "hira": "およぐ まえに、よく たいそうを すると いいですよ。",
        "acceptedHira": [
            "およぐまえに、よくたいそうをするといいですよ", "およぐまえに、よくたいそうをするといいです",
            "およぐまえに、ちゃんとたいそうをするといいですよ", "およぐまえに、しっかりたいそうをするといいですよ",
            "およぐまえに、よくうんどうをするといいですよ", "およぐまえに、ちゃんとうんどうをするといいですよ", "およぐまえに、しっかりうんどうをするといいですよ",
            "およぐまえに、よくストレッチをするといいですよ", "およぐまえに、よくすとれっちをするといいですよ",
            "およぐまえに、ちゃんとストレッチをするといいですよ", "およぐまえに、しっかりストレッチをするといいですよ"
        ],
        "kanjiModel": "泳ぐ前に、よく／ちゃんと／しっかり 体操（／運動／ストレッチ）をするといいですよ。",
        "kanjiAccepted": ["泳ぐ前によく体操をするといいですよ", "泳ぐ前にちゃんと運動をするといいですよ", "泳ぐ前にしっかり体操をするといいですよ", "泳ぐ前によく運動をするといいですよ"],
        "grammarRule": "② Cô chữa đa dạng phương án đều đúng: 'kỹ' = <b>よく／ちゃんと／しっかり</b>; 'tập thể dục/khởi động' = <b>たいそう／うんどう／ストレッチ</b>.",
        "breakdown": "およぐ (bơi - thể Vる từ 泳ぎます) + まえに (trước khi) + よく/ちゃんと/しっかり (kỹ) + たいそう/うんどう/ストレッチを すると いいですよ.",
        "traps": [
            {"regex": "およぎますまえに|およいでまえに", "why": "泳ぎます (Nhóm I đuôi ぎ) đổi sang thể Từ điển là 「およぐ」 ➔ およぐ まえに."},
            {"regex": "しますと|してと", "why": "します chia về thể Từ điển là 「する」 ➔ すると いいですよ."}
        ]
    },
    {
        "id": "s15_08", "lesson": "A2-15", "category": "ÔN TẬP L15 ③ Vないで ください",
        "pattern": "Vないで ＋ ください",
        "vi": "Khi bị cảm, đừng làm quá sức.",
        "hira": "かぜの とき、むりを しないで ください。",
        "acceptedHira": ["かぜのとき、むりをしないでください"],
        "kanjiModel": "風邪のとき、無理をしないでください。",
        "kanjiAccepted": ["風邪のとき無理をしないでください", "かぜのとき無理をしないでください", "風邪のときむりをしないでください"],
        "grammarRule": "③ Công thức xin đừng làm gì: <b>Vない ＋ で ください</b>. Chú ý かぜ (bị cảm) là danh từ ➔ nối với とき bằng 「の」; むりを します (làm quá sức, nhóm III) ➔ むりを しないで ください.",
        "breakdown": "かぜの とき (khi bị cảm) + むりを (quá sức) + しないで ください (xin đừng làm).",
        "traps": [
            {"regex": "かぜとき", "why": "「かぜ」 là danh từ, cần thêm trợ từ 「の」 trước とき ➔ かぜの とき!"},
            {"regex": "むりをすない|むりをしまない|むりをさない", "why": "「します」 thuộc Nhóm III chia thể ない là 「しない」 ➔ むりを しないで ください."}
        ]
    },
    {
        "id": "s15_09", "lesson": "A2-15", "category": "ÔN TẬP L15 ③ Vないで ください",
        "pattern": "～から、Vないで ください",
        "vi": "Vì không tốt cho sức khỏe, nên đừng hút thuốc lá.",
        "hira": "けんこうに よくないですから、たばこを すわないで ください。",
        "acceptedHira": [
            "けんこうによくないですから、たばこをすわないでください",
            "けんこうによくないから、たばこをすわないでください",
            "けんこうによくないので、たばこをすわないでください",
            "けんこうにわるいですから、たばこをすわないでください",
            "けんこうにわるいから、たばこをすわないでください",
            "けんこうにわるいので、たばこをすわないでください"
        ],
        "kanjiModel": "健康に悪い／よくないですから、たばこを吸わないでください。",
        "kanjiAccepted": ["健康に悪いですからたばこを吸わないでください", "健康によくないですからたばこを吸わないでください"],
        "grammarRule": "③ Lưu ý BẪY ĐỘNG TỪ NHÓM I ĐUÔI 「～います」: すいます (hút) ➔ <b>すわない</b> (phải đổi い thành <b>わ</b>, KHÔNG phải すいない!). 'Không tốt cho sức khỏe' = けんこうに わるい／よくない.",
        "breakdown": "けんこうに (cho sức khỏe) + わるいですから / よくないですから (vì xấu/không tốt) + たばこを すわないで ください (đừng hút thuốc lá).",
        "traps": [
            {"regex": "すいないで", "why": "BẪY ĐUÔI 「～います」! すいます chia sang thể ない phải chuyển い ➔ わ: 「すわないで ください」(KHÔNG phải すいないで)!"},
            {"regex": "いいじゃない|よくじゃない|いいくない", "why": "Tính từ 「いい」 chia phủ định đặc biệt thành 「よくない」 (hoặc dùng trái nghĩa 「わるい」)!"},
            {"regex": "けんこうで|けんこうを", "why": "Tốt/xấu CHO sức khỏe dùng trợ từ 「に」: けんこうに いい／わるい."}
        ]
    },
    {
        "id": "s15_10", "lesson": "A2-15", "category": "ÔN TẬP L15 ③ Vないで ください",
        "pattern": "Vないで ください",
        "vi": "Xin đừng hút thuốc lá ở đây.",
        "hira": "ここで たばこを すわないで ください。",
        "acceptedHira": ["ここでたばこをすわないでください"],
        "kanjiModel": "ここでたばこを吸わないでください。",
        "kanjiAccepted": ["ここでたばこを吸わないでください", "ここでタバコを吸わないでください", "ここで煙草を吸わないでください"],
        "grammarRule": "③ Nơi diễn ra hành động ('tại/ở đây') dùng trợ từ <b>で</b>: ここで. Đuôi すいます ➔ <b>すわないで</b>.",
        "breakdown": "ここで (ở đây - nơi hành động) + たばこを (thuốc lá) + すわないで ください (xin đừng hút).",
        "traps": [
            {"regex": "すいないで", "why": "Bẫy Nhóm I đuôi い: すいます ➔ すわないで ください (い chuyển thành わ, không phải い➔あ hay giữ nguyên い)!"},
            {"regex": "ここに.*すわ", "why": "Hút thuốc là hành động diễn ra tại địa điểm, nên 'ở đây' dùng 「ここで」, không dùng 「ここに」!"}
        ]
    },
    {
        "id": "s15_11", "lesson": "A2-15", "category": "ÔN TẬP L15 ③ Vないで ください",
        "pattern": "Vないで ください",
        "vi": "Xin đừng sử dụng máy tính trong khi kiểm tra.",
        "hira": "テストの とき、パソコンを つかわないで ください。",
        "acceptedHira": ["テストのとき、パソコンをつかわないでください", "てすとのとき、ぱそこんをつかわないでください", "しけんのとき、パソコンをつかわないでください"],
        "kanjiModel": "テストのとき、パソコンを使わないでください。",
        "kanjiAccepted": ["テストのときパソコンを使わないでください", "テストのとき、パソコンを使わないでください"],
        "grammarRule": "③ テスト (danh từ) + の とき. Động từ 使います (nhóm I đuôi います) ➔ thể ない là <b>つかわない</b> (い ➔ わ!).",
        "breakdown": "テストの とき (trong khi/lúc kiểm tra) + パソコンを (máy tính) + つかわないで ください (xin đừng sử dụng).",
        "traps": [
            {"regex": "つかないで|つかいないで", "why": "使います kết thúc bằng い: chia thể ない chuyển い ➔ わ thành 「つかわないで ください」!"},
            {"regex": "テストとき", "why": "テスト là danh từ nên cần thêm 「の」 trước とき ➔ テストの とき."}
        ]
    },
    {
        "id": "s15_12", "lesson": "A2-15", "category": "ÔN TẬP L15 ③ Vないで ください",
        "pattern": "Vないで ください",
        "vi": "Xin đừng đột nhiên bẻ / xoay cổ.",
        "hira": "きゅうに くびを まげないで ください。",
        "acceptedHira": [
            "きゅうにくびをまげないでください",
            "くびをきゅうにまげないでください",
            "きゅうにくびをまがさないでください",
            "くびをきゅうにまがさないでください",
            "きゅうにくびをまわさないでください",
            "くびをきゅうにまわさないでください"
        ],
        "kanjiModel": "きゅうに首をまげないでください。（PDF: まがさないで）",
        "kanjiAccepted": [
            "急に首を曲げないでください", "きゅうに首を曲げないでください", "急に首をまげないでください",
            "首を急に曲げないでください", "首をきゅうに曲げないでください", "首を急にまげないでください",
            "きゅうに首をまがさないでください", "急に首をまがさないでください",
            "首を急にまがさないでください", "首をきゅうにまがさないでください",
            "急に首を回さないでください", "きゅうに首をまわさないでください",
            "首を急に回さないでください", "首をきゅうにまわさないでください"
        ],
        "grammarRule": "③ まげます (bẻ/cúi gập, Nhóm II) ➔ <b>まげない</b>. File PDF ôn tập có ghi bản <b>まがさないで</b> (Nhóm I) / <b>まわさないで</b> (xoay cổ) nên đều được chấp nhận ở đây!",
        "breakdown": "きゅうに (đột nhiên) + くびを (cổ) + まげないで ください (xin đừng bẻ).",
        "traps": [
            {"regex": "まがないで|まげらないで", "why": "まげます thuộc Nhóm II (-eます) ➔ bỏ ます + ない ➔ まげないで ください (hoặc dùng đúng thể Nhóm I まわさないで/まがさないで)."},
            {"regex": "きゅに", "why": "きゅうに có trường âm う ở chữ きゅう."}
        ]
    },
    {
        "id": "s15_13", "lesson": "A2-15", "category": "ÔN TẬP L15 ① Vる まえに",
        "pattern": "Vる ＋ まえに",
        "vi": "Trước khi đi làm, tôi tự làm cơm hộp.",
        "hira": "しごとに いく まえに、おべんとうを つくります。",
        "acceptedHira": [
            "しごとにいくまえに、おべんとうをつくります",
            "しごとにいくまえにべんとうをつくります",
            "しごとにいくまえにおべんとうをつくります"
        ],
        "kanjiModel": "仕事に行く前に、おべんとうを作ります。",
        "kanjiAccepted": ["仕事に行く前に、おべんとうを作ります", "仕事に行く前に、お弁当を作ります", "仕事に行く前にお弁当を作ります"],
        "grammarRule": "① Hành động xảy ra trước một hành động khác: Động từ đứng trước <b>まえに</b> LUÔN chia ở thể từ điển <b>Vる</b> (いきます ➔ <b>いく</b>).",
        "breakdown": "しごとに いく まえに (trước khi đi làm) + おべんとうを つくります (làm cơm hộp).",
        "traps": [
            {"regex": "いきますまえに|いったまえに|いくのまえに", "why": "Trước 「まえに」 bắt buộc chia động từ về thể từ điển Vる (いく) và KHÔNG chen thêm 「の」 hay để 「いきます」!"}
        ]
    },
    {
        "id": "s15_14", "lesson": "A2-15", "category": "ÔN TẬP L15 ① Vる まえに (Vế sau Quá khứ)",
        "pattern": "Vる ＋ まえに、～ました",
        "vi": "Trước khi sang Nhật, tôi đã học tiếng Nhật.",
        "hira": "にほんに いく まえに、にほんごを べんきょうしました。",
        "acceptedHira": [
            "にほんにいくまえに、にほんごをべんきょうしました",
            "にほんへいくまえに、にほんごをべんきょうしました",
            "にほんにいくまえににほんごをべんきょうしました"
        ],
        "kanjiModel": "日本に行く前に、日本語を勉強しました。",
        "kanjiAccepted": ["日本に行く前に、日本語を勉強しました", "日本に行く前に日本語を勉強しました", "日本へ行く前に日本語を勉強しました"],
        "grammarRule": "① BẪY KINH ĐIỂN TRONG PDF: Dù cả câu kể chuyện ĐÃ XẢY RA ở quá khứ (<b>べんきょうしました</b>), động từ trước <b>まえに</b> vẫn LUÔN là thể từ điển <b>いく</b> (TUYỆT ĐỐI không chia いった!).",
        "breakdown": "にほんに いく まえに (trước khi đi Nhật) + にほんごを べんきょうしました (đã học tiếng Nhật).",
        "traps": [
            {"regex": "いったまえに|きましたまえに|きますまえに|いくのまえに", "why": "BẪY PDF L15: Dù vế sau là quá khứ (~ました), động từ trước まえに LUÔN là Vる (にほんに いく まえに), tuyệt đối không dùng いった まえに!"}
        ]
    },
    {
        "id": "s15_15", "lesson": "A2-15", "category": "ÔN TẬP L15 ① Khoảng thời gian + まえに",
        "pattern": "〈Khoảng thời gian〉＋ まえに",
        "vi": "10 phút trước, tôi đã đến nhà ga.",
        "hira": "10ぷんまえに、えきに つきました。",
        "acceptedHira": [
            "10ぷんまえに、えきにつきました",
            "じゅっぷんまえに、えきにつきました",
            "じっぷんまえに、えきにつきました",
            "じゅうぷんまえにえきにつきました"
        ],
        "kanjiModel": "10分前に、駅に着きました。",
        "kanjiAccepted": ["10分前に、駅に着きました", "10分前に駅に着きました", "十分前に駅に着きました"],
        "grammarRule": "① Khoảng thời gian + <b>まえに</b>: Nối trực tiếp KHÔNG cần trợ từ 「の」 ở giữa (10ぷんまえに / 3ねんまえに). Chỉ có Danh từ sự kiện mới cần 「の」(食事の前に).",
        "breakdown": "10ぷん まえに (10 phút trước, không có の) + えきに つきました (đã đến nhà ga).",
        "traps": [
            {"regex": "10ぷんのまえに|じゅっぷんのまえに|じっぷんのまえに|さんねんのまえに", "why": "BẪY PDF TRANG 19: Khoảng thời gian (3ねん, 10ぷん) đứng trước まえに KHÔNG có 「の」! Chỉ danh từ sự kiện mới thêm の."}
        ]
    },

    # ================= LESSON 16 =================
    {
        "id": "s16_01", "lesson": "A2-16", "category": "ÔN TẬP L16 ① V1たり、V2たり",
        "pattern": "V1たり、V2たり します／しています",
        "vi": "Vào ngày nghỉ, tôi thường đi mua sắm và dùng bữa với gia đình v.v...",
        "hira": "やすみの ひは、よく かいものしたり、かぞくと しょくじしたり して います。",
        "acceptedHira": [
            "やすみのひは、よくかいものしたり、かぞくとしょくじしたりしています",
            "やすみのひは、よくかいものしたり、かぞくとしょくじしたりします",
            "やすみのひに、よくかいものしたり、かぞくとしょくじしたりしています",
            "やすみのひに、よくかいものしたり、かぞくとしょくじしたりします"
        ],
        "kanjiModel": "休みの日は、よく買い物したり、家族と食事したりしています。",
        "kanjiAccepted": ["休みの日はよく買い物したり家族と食事したりしています", "休みの日はよく買い物したり家族と食事したりします"],
        "grammarRule": "① Cấu trúc liệt kê hành động tiêu biểu: <b>V1た＋り、V2た＋り します（／しています）</b>. Nhớ động từ cuối câu là します/しています (chia theo thì/thói quen).",
        "breakdown": "やすみの ひは (vào ngày nghỉ) + よく (thường) + かいものしたり (mua sắm) + かぞくと しょくじしたり (dùng bữa với gia đình) + して います (làm thói quen).",
        "traps": [
            {"regex": "かいものするたり|しょくじするたり", "why": "Trước 「たり」 phải chia động từ về thể た (quá khứ ngắn), KHÔNG dùng thể Từ điển! ➔ かいものした＋り."},
            {"regex": "しょくじしたりです$", "why": "Cuối mẫu ～たり～たり bắt buộc phải có động từ 「します／しています」, không kết thúc bằng です!"}
        ]
    },
    {
        "id": "s16_02", "lesson": "A2-16", "category": "ÔN TẬP L16 ① V1たり、V2たり",
        "pattern": "Nの ために、V1たり、V2たり しています",
        "vi": "Vì sức khỏe, mỗi ngày tôi ăn hoa quả và rau xanh, chạy bộ ở công viên khoảng 30 phút v.v...",
        "hira": "けんこうの ために、まいにち くだものと やさいを たべたり、30ぷんぐらい こうえんを ジョギングしたり して います。",
        "acceptedHira": [
            "けんこうのために、まいにちくだものとやさいをたべたり、30ぷんぐらいこうえんをジョギングしたりしています",
            "けんこうのために、まいにちくだものとやさいをたべたり、30ぷんぐらいこうえんをはしったりしています",
            "けんこうのために、まいにちくだものとやさいをたべたり、さんじゅっぷんぐらいこうえんをジョギングしたりしています",
            "けんこうのために、まいにちくだものとやさいをたべたり、さんじゅっぷんぐらいこうえんをはしったりしています",
            "けんこうのために、まいにちくだものとやさいをたべたり、30ぷんくらいこうえんをジョギングしたりしています",
            "けんこうのために、まいにちくだものとやさいをたべたり、30ぷんくらいこうえんをはしったりしています",
            "けんこうのために、まいにちくだものとやさいをたべたり、30ぷんぐらいこうえんをじょぎんぐしたりしています"
        ],
        "kanjiModel": "健康のために、毎日 くだものと野菜を食べたり、30分ぐらい公園をジョギングしたり／走ったりしています。",
        "kanjiAccepted": ["健康のために毎日くだものと野菜を食べたり30分ぐらい公園をジョギングしたりしています", "健康のために毎日くだものと野菜を食べたり30分ぐらい公園を走ったりしています"],
        "grammarRule": "① 'Vì N' = <b>Nの ために</b>. Nơi chạy bộ trong công viên dùng trợ từ <b>を</b> (こうえんを ジョギングしたり／走ったり). Chú ý đếm phút: 30ぷん (さんじゅっぷん).",
        "breakdown": "けんこうの ために (vì sức khỏe) + まいにち (mỗi ngày) + くだものと やさいを たべたり + 30ぷんぐらい こうえんを ジョギングしたり/はしったり して います.",
        "traps": [
            {"regex": "けんこうために", "why": "'Vì N' cần có trợ từ 「の」: けんこうの ために!"},
            {"regex": "たべるたり|ジョギングするたり|はしるたり", "why": "Trước 「たり」 luôn chia thể た: たべた＋り, ジョギングした＋り / はしった＋り."},
            {"regex": "こうえんにジョギング|こうえんにはし", "why": "Hành động di chuyển qua không gian (chạy bộ ở công viên) dùng trợ từ 「を」 ➔ こうえんを ジョギングしたり / はしったり."}
        ]
    },
    {
        "id": "s16_03", "lesson": "A2-16", "category": "ÔN TẬP L16 ① V1たり、V2たり",
        "pattern": "V1たり、V2たり しないで ください",
        "vi": "Đừng xem điện thoại hay sử dụng máy tính v.v... ở nơi tối.",
        "hira": "くらい ところで スマホを みたり、パソコンを つかったり しないで ください。",
        "acceptedHira": [
            "くらいところでスマホをみたり、パソコンをつかったりしないでください",
            "くらいところですまほをみたり、ぱそこんをつかったりしないでください"
        ],
        "kanjiModel": "暗いところでスマホを見たり、パソコンを使ったりしないでください。",
        "kanjiAccepted": ["暗いところでスマホを見たりパソコンを使ったりしないでください", "暗いところでスマホを見たり、パソコンを使ったりしないでください"],
        "grammarRule": "① Kết hợp ～たり～たり với 「ないでください」! Động từ cuối 「します」 đổi sang thể ない ➔ <b>しないで ください</b>. Chú ý thể た của 使います: った (つかったり).",
        "breakdown": "くらい ところで (ở nơi tối) + スマホを みたり (xem điện thoại) + パソコンを つかったり (sử dụng máy tính) + しないで ください (xin đừng).",
        "traps": [
            {"regex": "つかわったり|つかいたり", "why": "使います (Nhóm I đuôi い) chia thể た biến âm thành っ ➔ つかったり!"},
            {"regex": "したくないで|しないください", "why": "Với ～たり～たり, chia động từ cuối します ➔ しないで ください (nhớ phải có chữ で sau ない)!"}
        ]
    },
    {
        "id": "s16_04", "lesson": "A2-16", "category": "ÔN TẬP L16 ① V1たり、V2たり",
        "pattern": "V1たり、V2たり すると いいですよ",
        "vi": "Trước khi ngủ, bạn nên ngâm bồn, nghe nhạc nhẹ nhàng v.v... thì tốt.",
        "hira": "ねる まえに、おふろに はいったり、しずかな おんがくを きいたり すると いいですよ。",
        "acceptedHira": [
            "ねるまえに、おふろにはいったり、しずかなおんがくをきいたりするといいですよ",
            "ねるまえに、おふろにはいったり、しずかなおんがくをきいたりするといいです"
        ],
        "kanjiModel": "寝る前に、お風呂に入ったり、静かな音楽を聴いたりするといいですよ。",
        "kanjiAccepted": ["寝る前にお風呂に入ったり静かな音楽を聞いたりするといいですよ", "寝る前にお風呂に入ったり静かな音楽を聴いたりするといいですよ"],
        "grammarRule": "① Kết hợp Bài 15 + Bài 16: Động từ cuối 「します」 chia sang thể Từ điển 「する」 để ghép với 「と いいですよ」! Nhớ しずか là tính từ đuôi な ➔ <b>しずかな</b> おんがく.",
        "breakdown": "ねる まえに (trước khi ngủ) + おふろに はいったり (ngâm bồn tắm - Nhóm I はいった) + しずかな おんがくを きいたり (nghe nhạc nhẹ) + すると いいですよ.",
        "traps": [
            {"regex": "しずかおんがく|しずかの", "why": "「しずか」 là tính từ đuôi な! Trước danh từ おんがく bắt buộc phải có 「な」 ➔ しずかな おんがく."},
            {"regex": "おふろをはい", "why": "Vào bồn tắm (お風呂に入る) dùng trợ từ 「に」 ➔ おふろに はいったり."},
            {"regex": "はいりたり", "why": "入ります (はいります) thuộc NHÓM I (ngoại lệ), chia thể た là はいった ➔ はいったり!"}
        ]
    },
    {
        "id": "s16_05", "lesson": "A2-16", "category": "ÔN TẬP L16 ② V〈ふつうけい〉＋ 人",
        "pattern": "V〈ふつうけい〉＋ 人",
        "vi": "Người hút thuốc lá thì tình trạng sức khỏe không tốt.",
        "hira": "たばこを すう ひとは たいちょうが わるいです。",
        "acceptedHira": [
            "たばこをすうひとはたいちょうがわるいです",
            "たばこをすうひとはからだのちょうしがわるいです",
            "たばこをすうひとはたいちょうがよくないです",
            "たばこをすうひとはからだのちょうしがよくないです"
        ],
        "kanjiModel": "たばこを吸う人は体調／体の調子が悪いです。",
        "kanjiAccepted": ["たばこを吸う人は体調が悪いです", "たばこを吸う人は体の調子が悪いです", "タバコを吸う人は体調が悪いです"],
        "grammarRule": "② Mệnh đề bổ ngữ cho danh từ: <b>V〈ふつうけい〉＋ 人</b>. Chú ý 'tình trạng sức khỏe' = <b>たいちょう</b> hoặc <b>からだの ちょうし</b>.",
        "breakdown": "たばこを すう ひと (người hút thuốc lá - thể từ điển bổ nghĩa cho 人) + は + たいちょう / からだの ちょうしが わるいです.",
        "traps": [
            {"regex": "すいますひと", "why": "Trước danh từ 「ひと」 không dùng thể ます! Phải chia về thể thông thường: すいます ➔ すう ひと."},
            {"regex": "の.*ひと", "why": "Không chèn 「の」 giữa động từ và danh từ! Nói thẳng là 「すう ひと」, KHÔNG nói すうのひと!"}
        ]
    },
    {
        "id": "s16_06", "lesson": "A2-16", "category": "ÔN TẬP L16 ② V〈ふつうけい〉＋ 人",
        "pattern": "Vている ＋ 人",
        "vi": "Người đang tập yoga một mình là anh trai tôi.",
        "hira": "ひとりで ヨガを して いる ひとは あにです。",
        "acceptedHira": [
            "ひとりでヨガをしているひとはあにです",
            "ひとりでよがをしているひとはあにです",
            "ひとりでヨガをしているひとはわたしのおにいさんです",
            "ひとりでヨガをしているひとはおにいさんです"
        ],
        "kanjiModel": "一人でヨガをしている人は兄です。",
        "kanjiAccepted": ["一人でヨガをしている人は兄です", "ひとりでヨガをしている人は兄です"],
        "grammarRule": "② Hành động đang tiếp diễn dùng <b>Vている ＋ 人</b> (して います ➔ して いる). 'Một mình' = <b>ひとりで</b>. Anh trai của mình = あに.",
        "breakdown": "ひとりで (một mình) + ヨガを して いる ひと (người đang tập yoga) + は + あにです (là anh trai tôi).",
        "traps": [
            {"regex": "していますひと", "why": "Trước danh từ 「ひと」 phải đưa しています về thể thông thường ➔ して いる ひと."},
            {"regex": "ひとりヨガ|ひとりにヨガ", "why": "'Làm một mình' dùng trợ từ 「で」 ➔ ひとりで!"}
        ]
    },
    {
        "id": "s16_07", "lesson": "A2-16", "category": "ÔN TẬP L16 ② V〈ふつうけい〉＋ 人",
        "pattern": "Vた ＋ 人",
        "vi": "Người đã uống rượu thì xin đừng lái xe.",
        "hira": "おさけを のんだ ひとは くるまを うんてんしないで ください。",
        "acceptedHira": [
            "おさけをのんだひとはくるまをうんてんしないでください",
            "おさけをのんだひとはうんてんしないでください"
        ],
        "kanjiModel": "お酒を飲んだ人は（車を）運転しないでください。",
        "kanjiAccepted": ["お酒を飲んだ人は車を運転しないでください", "お酒を飲んだ人は運転しないでください"],
        "grammarRule": "② 'Người ĐÃ uống rượu' ➔ dùng thể quá khứ ngắn <b>Vた ＋ 人</b> (のみました ➔ のんだ). Phần sau là L15 ③: <b>Vないで ください</b>.",
        "breakdown": "おさけを のんだ ひと (người đã uống rượu) + は + (くるまを) うんてんしないで ください (xin đừng lái xe).",
        "traps": [
            {"regex": "のみましたひと|のむひと", "why": "Câu nói 'người ĐÃ uống rượu' nên phải dùng quá khứ thông thường 「のんだ ひと」 (cũng không dùng thể ます)."},
            {"regex": "うんてんすない|うんてんしまない", "why": "うんてんします (nhóm III) chia thể ない là 「うんてんしない」 ➔ うんてんしないで ください."}
        ]
    },
    {
        "id": "s16_08", "lesson": "A2-16", "category": "ÔN TẬP L16 ② V〈ふつうけい〉＋ 人",
        "pattern": "Vない ＋ 人",
        "vi": "Người không hiểu tiếng Nhật thì xin hãy đọc cuốn sách này.",
        "hira": "にほんごが わからない ひとは、この ほんを よんで ください。",
        "acceptedHira": ["にほんごがわからないひとは、このほんをよんでください"],
        "kanjiModel": "日本語がわからない人は、この本を読んでください。",
        "kanjiAccepted": ["日本語がわからない人はこの本を読んでください", "日本語が分からない人はこの本を読んでください"],
        "grammarRule": "② Phủ định hiện tại dùng <b>Vない ＋ 人</b> (わかりません ➔ わからない). Lưu ý động từ わかります đi với trợ từ <b>が</b> (にほんごが).",
        "breakdown": "にほんごが わからない ひと (người không hiểu tiếng Nhật) + は + この ほんを よんで ください (hãy đọc sách này).",
        "traps": [
            {"regex": "わかりませんひと|わかりないひと", "why": "わかります (Nhóm I) chia thể ない là わからない (KHÔNG dùng わかりません hay わかりない)!"},
            {"regex": "にほんごをわから", "why": "Động từ 「わかります」 luôn đi với trợ từ 「が」 ➔ にほんごが わからない."}
        ]
    },
    {
        "id": "s16_n1", "lesson": "A2-16", "category": "NGỮ PHÁP L16 (Mở rộng)",
        "pattern": "V〈ふつうけい〉＋ 人",
        "vi": "Người hay đọc sách thì thông minh.",
        "hira": "よく ほんを よむ ひとは あたまが いいです。",
        "acceptedHira": ["よくほんをよむひとはあたまがいいです"],
        "kanjiModel": "よく本を読む人は頭がいいです。",
        "kanjiAccepted": ["よく本を読む人は頭がいいです"],
        "grammarRule": "② Câu luyện tập của cô L16: 'thông minh' = <b>あたまが いいです</b>.",
        "breakdown": "よく ほんを よむ ひと (người hay đọc sách) + は + あたまが いいです (thông minh).",
        "traps": [{"regex": "よみますひと", "why": "Phải chia thể Từ điển 「よむ」 trước ひと!"}]
    },
    {
        "id": "s16_n2", "lesson": "A2-16", "category": "NGỮ PHÁP L16 (Mở rộng)",
        "pattern": "V〈ふつうけい〉＋ N",
        "vi": "Tớ không thích người đàn ông hút thuốc.",
        "hira": "わたしは たばこを すう おとこのひとが すきじゃないです。",
        "acceptedHira": ["わたしはたばこをすうおとこのひとがすきじゃないです", "たばこをすうおとこのひとがすきじゃないです", "わたしはたばこをすうおとこのひとがすきではありません"],
        "kanjiModel": "わたしはたばこを吸う男の人が好きじゃないです。",
        "kanjiAccepted": ["わたしはたばこを吸う男の人が好きじゃないです", "私はたばこを吸う男の人が好きじゃないです"],
        "grammarRule": "② Ghép với cấu trúc わたしは Nが すきじゃないです! Lưu ý 'người đàn ông' = <b>おとこのひと</b>.",
        "breakdown": "わたしは + たばこを すう おとこのひと (người đàn ông hút thuốc) + が + すきじゃないです.",
        "traps": [
            {"regex": "おとこのひとをすき", "why": "Tính từ 「すき」 đi với trợ từ 「が」, KHÔNG dùng 「を」!"},
            {"regex": "すいますおとこ", "why": "Phải chia động từ về thể thông thường 「すう」 trước 「おとこのひと」."}
        ]
    },
    {
        "id": "s16_n3", "lesson": "A2-16", "category": "NGỮ PHÁP L16 (Mở rộng)",
        "pattern": "V〈ふつうけい〉＋ N",
        "vi": "Bộ phim đã xem hôm qua đã thú vị.",
        "hira": "きのう みた えいがは おもしろかったです。",
        "acceptedHira": ["きのうみたえいがはおもしろかったです"],
        "kanjiModel": "きのう見た映画はおもしろかったです。",
        "kanjiAccepted": ["きのう見た映画はおもしろかったです", "昨日見た映画はおもしろかったです"],
        "grammarRule": "② Quá khứ trong cụm bổ ngữ: みました ➔ <b>みた</b>. Quá khứ của tính từ い (おもしろい) ➔ <b>おもしろかった</b>です.",
        "breakdown": "きのう みた えいが (bộ phim đã xem hôm qua) + は + おもしろかったです (đã thú vị).",
        "traps": [{"regex": "おもしろいです$|みましたえいが", "why": "Cả hai đều là chuyện hôm qua: みた えいが ... おもしろかったです."}]
    },
    {
        "id": "s16_n4", "lesson": "A2-16", "category": "NGỮ PHÁP L16 (Mở rộng)",
        "pattern": "V1たり、V2たり します",
        "vi": "Ngày mai tôi sẽ dọn phòng, giặt giũ v.v...",
        "hira": "あした へやを そうじしたり、せんたくしたり します。",
        "acceptedHira": ["あしたへやをそうじしたり、せんたくしたりします"],
        "kanjiModel": "あした部屋を掃除したり、洗濯したりします。",
        "kanjiAccepted": ["あした部屋を掃除したり洗濯したりします"],
        "grammarRule": "① Thể quá khứ ngắn ghép ～たり: そうじします ➔ そうじした＋り, せんたくします ➔ せんたくした＋り.",
        "breakdown": "あした + へやを そうじしたり (dọn phòng) + せんたくしたり (giặt giũ) + します.",
        "traps": [{"regex": "そうじするたり|せんたくするたり", "why": "Trước 「たり」 luôn chia về thể た: そうじしたり、せんたくしたり します!"}]
    },
    {
        "id": "s16_n5", "lesson": "A2-16", "category": "NGỮ PHÁP L16 (Mở rộng)",
        "pattern": "V〈ふつうけい〉＋ N",
        "vi": "Đứa trẻ không ăn rau thì không khỏe lắm.",
        "hira": "やさいを たべない こどもは あまり げんきじゃないです。",
        "acceptedHira": ["やさいをたべないこどもはあまりげんきじゃないです", "やさいをたべないこどもはあまりげんきではありません"],
        "kanjiModel": "野菜を食べない子どもはあまり元気じゃないです。",
        "kanjiAccepted": ["野菜を食べない子どもはあまり元気じゃないです"],
        "grammarRule": "② たべます (nhóm II) ➔ たべない ＋ こども. Đi với あまり nhớ dùng thể phủ định ở cuối câu!",
        "breakdown": "やさいを たべない こども (đứa trẻ không ăn rau) + は + あまり げんきじゃないです (không khỏe lắm).",
        "traps": [{"regex": "たべらない|げんきです$", "why": "たべます thuộc Nhóm II ➔ たべない; phó từ 「あまり」 bắt buộc đi với phủ định げんきじゃないです!"}]
    },
    {
        "id": "s16_n6", "lesson": "A2-16", "category": "NGỮ PHÁP L16 (Mở rộng)",
        "pattern": "Vている ＋ N",
        "vi": "Cuốn sách tôi đang đọc là Doraemon.",
        "hira": "よんで いる ほんは ドラえもんです。",
        "acceptedHira": ["よんでいるほんはドラえもんです", "よんでいるほんはどらえもんです", "わたしがよんでいるほんはドラえもんです"],
        "kanjiModel": "読んでいる本はドラえもんです。",
        "kanjiAccepted": ["読んでいる本はドラえもんです"],
        "grammarRule": "② Bổ nghĩa Vている đứng trước danh từ ほん.",
        "breakdown": "よんで いる ほん (cuốn sách đang đọc) + は + ドラえもんです.",
        "traps": [{"regex": "よみますほん|よんでいますほん", "why": "Trước danh từ 「ほん」 phải dùng thể thông thường 「よんで いる」!"}]
    },

    # ================= KAIWA MID 2 (L16-17 V+N) =================
    {
        "id": "km2_01", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "V〈ふつうけい〉＋ N",
        "vi": "Người uống cà phê",
        "hira": "コーヒーを のむ ひと",
        "acceptedHira": ["コーヒーをのむひと", "こーひーをのむひと"],
        "kanjiModel": "コーヒーを飲む人",
        "kanjiAccepted": ["コーヒーを飲む人"],
        "grammarRule": "③ Mệnh đề bổ ngữ cơ bản: V(ふつうけい) đứng trực tiếp trước danh từ N (không thêm の).",
        "breakdown": "コーヒーを のむ (uống cà phê - Vる) + ひと (người).",
        "traps": [{"regex": "のみますひと|のむのひと", "why": "Không dùng thể ます và không thêm 「の」 trước 「ひと」! Dùng thẳng: のむ ひと."}]
    },
    {
        "id": "km2_02", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "V〈ふつうけい〉＋ N",
        "vi": "Người tập thể dục",
        "hira": "うんどうを する ひと",
        "acceptedHira": ["うんどうをするひと", "うんどうするひと"],
        "kanjiModel": "運動（を）する人",
        "kanjiAccepted": ["運動をする人", "運動する人"],
        "grammarRule": "③ 運動（を）します ➔ thể Từ điển 運動（を）する ＋ 人.",
        "breakdown": "うんどう（を）する (tập thể dục) + ひと (người).",
        "traps": [{"regex": "しますひと", "why": "Đưa します về thể Từ điển 「する」 trước danh từ ひと!"}]
    },
    {
        "id": "km2_03", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Vない ＋ N",
        "vi": "Người không đọc sách",
        "hira": "ほんを よまない ひと",
        "acceptedHira": ["ほんをよまないひと"],
        "kanjiModel": "本を読まない人",
        "kanjiAccepted": ["本を読まない人"],
        "grammarRule": "③ Phủ định bổ ngữ: よみません ➔ <b>よまない</b> ＋ ひと.",
        "breakdown": "ほんを よまない (không đọc sách) + ひと (người).",
        "traps": [{"regex": "よみませんひと|よむない", "why": "Phủ định ngắn của よみます (Nhóm I) là よまない."}]
    },
    {
        "id": "km2_04", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Vない ＋ N",
        "vi": "Người không hiểu tiếng Nhật",
        "hira": "にほんごが わからない ひと",
        "acceptedHira": ["にほんごがわからないひと"],
        "kanjiModel": "日本語がわからない人",
        "kanjiAccepted": ["日本語がわからない人", "日本語が分からない人"],
        "grammarRule": "③ Nhớ trợ từ 「が」 với わかります!",
        "breakdown": "にほんごが わからない + ひと.",
        "traps": [{"regex": "にほんごを|わかりない", "why": "わかります đi với 「が」, và thể ない là わからない."}]
    },
    {
        "id": "km2_05", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Vた ＋ N",
        "vi": "Người đã làm bài tập về nhà",
        "hira": "しゅくだいを した ひと",
        "acceptedHira": ["しゅくだいをしたひと"],
        "kanjiModel": "宿題をした人",
        "kanjiAccepted": ["宿題をした人", "しゅくだいをした人"],
        "grammarRule": "③ Thể quá khứ ngắn: しました ➔ <b>した</b> ＋ ひと.",
        "breakdown": "しゅくだいを した (đã làm bài tập) + ひと (người).",
        "traps": [{"regex": "しましたひと|するひと", "why": "'Người ĐÃ làm' dùng thể quá khứ ngắn 「した」 trước ひと."}]
    },
    {
        "id": "km2_06", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Vなかった ＋ N",
        "vi": "Người đã không làm bài tập về nhà",
        "hira": "しゅくだいを しなかった ひと",
        "acceptedHira": ["しゅくだいをしなかったひと"],
        "kanjiModel": "宿題をしなかった人",
        "kanjiAccepted": ["宿題をしなかった人", "しゅくだいをしなかった人"],
        "grammarRule": "③ Quá khứ phủ định: しませんでした ➔ <b>しなかった</b> ＋ ひと.",
        "breakdown": "しゅくだいを しなかった (đã không làm bài tập) + ひと (người).",
        "traps": [{"regex": "しませんでしたひと|しないかった|しなかったのひと", "why": "Quá khứ phủ định của します là 「しなかった」 (bỏ い ở しない rồi thêm かった)."}]
    },
    {
        "id": "km2_07", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "V〈ふつうけい〉＋ N",
        "vi": "Công việc sử dụng tiếng Nhật",
        "hira": "にほんごを つかう しごと",
        "acceptedHira": ["にほんごをつかうしごと"],
        "kanjiModel": "日本語を使う仕事",
        "kanjiAccepted": ["日本語を使う仕事"],
        "grammarRule": "③ つかいます ➔ つかう ＋ しごと.",
        "breakdown": "にほんごを つかう (sử dụng tiếng Nhật) + しごと (công việc).",
        "traps": [{"regex": "つかいますしごと", "why": "Đưa つかいます về thể Từ điển つかう!"}]
    },
    {
        "id": "km2_08", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Sが／の V〈ふつうけい〉＋ N",
        "vi": "Đồ em bé mặc",
        "hira": "あかちゃんが きる もの",
        "acceptedHira": ["あかちゃんがきるもの", "あかちゃんのきるもの"],
        "kanjiModel": "あかちゃんが／の着るもの",
        "kanjiAccepted": ["あかちゃんが着るもの", "あかちゃんの着るもの", "赤ちゃんが着るもの"],
        "grammarRule": "③ Chủ ngữ trong mệnh đề bổ ngữ dùng trợ từ <b>が</b> (hoặc <b>の</b>). 着ます (mặc, nhóm II) ➔ <b>きる</b>.",
        "breakdown": "あかちゃんが/の (em bé - chủ thể của động từ trong mệnh đề phụ) + きる (mặc) + もの (đồ).",
        "traps": [{"regex": "あかちゃんはきる|きますもの", "why": "Trong mệnh đề bổ ngữ dùng 「が」(hoặc 「の」) thay cho 「は」, và động từ là 「きる」 (着ます thuộc nhóm II)!"}]
    },
    {
        "id": "km2_09", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Sに Vた Nは ～です",
        "vi": "Món quà nhận được từ mẹ là chiếc áo len màu hồng.",
        "hira": "ははに もらった プレゼントは ピンクの セーターです。",
        "acceptedHira": [
            "ははにもらったプレゼントはピンクのセーターです",
            "ははからもらったプレゼントはピンクのセーターです",
            "ははにもらったぷれぜんとはぴんくのせーたーです"
        ],
        "kanjiModel": "母にもらったプレゼントはピンクのセーターです。",
        "kanjiAccepted": ["母にもらったプレゼントはピンクのセーターです", "母からもらったプレゼントはピンクのセーターです"],
        "grammarRule": "③ Nhận từ ai dùng 「人に/から もらう」. Quá khứ ngắn もらいました ➔ <b>もらった</b>. 'Màu hồng' = ピンクの + danh từ.",
        "breakdown": "ははに もらった プレゼント (món quà nhận được từ mẹ) + は + ピンクの セーターです (là chiếc áo len màu hồng).",
        "traps": [{"regex": "もらいました|ピンクセーター", "why": "Trong cụm bổ ngữ chia 「もらった」; 'áo len màu hồng' nối bằng 「の」 ➔ ピンクの セーター."}]
    },
    {
        "id": "km2_10", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Sが Vた Nは ～で、～です",
        "vi": "Bức tranh bố đã mua thì nổi tiếng và đắt tiền.",
        "hira": "ちちが かった えは ゆうめいで、たかいです。",
        "acceptedHira": ["ちちがかったえはゆうめいで、たかいです"],
        "kanjiModel": "父が買った絵は有名で、高いです。",
        "kanjiAccepted": ["父が買った絵はゆうめいで高いです", "父が買った絵は有名で高いです", "父が買った絵はゆうめいで、たかいです"],
        "grammarRule": "③ Chủ ngữ mệnh đề bổ ngữ dùng 「が」 (ちち<b>が</b> かった). Nối tính từ đuôi な (ゆうめい) + tính từ đuôi い ➔ <b>ゆうめいで</b>、たかいです.",
        "breakdown": "ちちが かった え (bức tranh bố đã mua) + は + ゆうめいで (nổi tiếng và) + たかいです (đắt tiền).",
        "traps": [
            {"regex": "ちちはかった", "why": "Chủ ngữ trong mệnh đề bổ ngữ phải dùng trợ từ 「が」 ➔ ちちが かった え! (Trợ từ 「は」 chỉ đánh dấu chủ đề cả câu lớn)."},
            {"regex": "ゆうめいいて|ゆうめいかった", "why": "「ゆうめい」 là tính từ đuôi な! Nối 2 tính từ dùng 「ゆうめいで、～」."}
        ]
    },
    {
        "id": "km2_11", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Vている Nは Vて ください",
        "vi": "Người đang học tiếng Pháp thì hãy sử dụng ứng dụng này.",
        "hira": "フランスごを べんきょうして いる ひとは この アプリを つかって ください。",
        "acceptedHira": ["フランスごをべんきょうしているひとはこのアプリをつかってください", "ふらんすごをべんきょうしているひとはこのあぷりをつかってください"],
        "kanjiModel": "フランス語を勉強している人はこのアプリを使ってください。",
        "kanjiAccepted": ["フランス語を勉強している人はこのアプリを使ってください"],
        "grammarRule": "③ Đang làm gì ➔ <b>Vている ＋ 人</b>. App = アプリ. Hãy dùng = つかって ください.",
        "breakdown": "フランスごを べんきょうして いる ひと (người đang học tiếng Pháp) + は + この アプリを つかって ください.",
        "traps": [{"regex": "べんきょうしたひと|つかわて", "why": "'Đang học' dùng 「べんきょうして いる」; 'Hãy sử dụng' chia thể て của 使います là 「つかって ください」."}]
    },
    {
        "id": "km2_12", "lesson": "Kaiwa Mid 2", "category": "KAIWA MID 2 ③ V + N",
        "pattern": "Vている Nは ～です",
        "vi": "Chú mèo đang chơi ở vườn là Mimi chan.",
        "hira": "にわで あそんで いる ねこは みみちゃんです。",
        "acceptedHira": ["にわであそんでいるねこはみみちゃんです", "にわであそんでいるねこはミミちゃんです"],
        "kanjiModel": "庭で遊んでいる猫はみみちゃんです。",
        "kanjiAccepted": ["庭で遊んでいる猫はみみちゃんです", "庭で遊んでいる猫はミミちゃんです"],
        "grammarRule": "③ Ở vườn (nơi diễn ra hành động chơi) dùng 「にわ<b>で</b>」. あそびます ➔ あそんで いる.",
        "breakdown": "にわで あそんで いる ねこ (chú mèo đang chơi ở vườn) + は + みみちゃんです.",
        "traps": [{"regex": "あそんでる|あそびて|にわにあそん", "why": "Nơi hành động chơi ở vườn là 「にわで」; thể て của あそびます (đuôi び) là 「あそんで」 (nếu viết chuẩn văn phong học thì nhớ chữ い trong あそんでいる)."}]
    },

    # ================= LESSON 17 =================
    {
        "id": "s17_01a", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "〈ふつうけい〉＋ んですか",
        "vi": "Wa, bộ vest đẹp quá. Bạn đã mua ở đâu vậy?",
        "hira": "わ、すてきな スーツですね。どこで かったんですか。",
        "acceptedHira": ["わ、すてきなスーツですね。どこでかったんですか", "わあ、すてきなスーツですね。どこでかったんですか", "わ、すてきなすーつですね。どこでかったんですか"],
        "kanjiModel": "わ、すてきなスーツですね。どこで買ったんですか。",
        "kanjiAccepted": ["わ、すてきなスーツですね。どこで買ったんですか"],
        "grammarRule": "① Hỏi thăm thân mật để tìm hiểu hoàn cảnh sau điều vừa thấy: <b>V〈ふつうけい〉＋ んですか</b> (かいました ➔ かったんですか). 'Đẹp/tuyệt' = すてきな (tính từ な).",
        "breakdown": "わ、すてきな スーツですね (Wa, bộ vest đẹp quá nhỉ) + どこで かったんですか (Bạn đã mua ở đâu vậy?).",
        "traps": [
            {"regex": "かいましたんですか|かうんですか", "why": "Trước 「んですか」 phải dùng Thể thông thường thì quá khứ: かいました ➔ かった ➔ かったんですか!"},
            {"regex": "すてきスーツ|すてきのスーツ", "why": "「すてき」 là tính từ đuôi な ➔ すてきな スーツ."}
        ]
    },
    {
        "id": "s17_01b", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "〈ふつうけい〉＋ んですよ",
        "vi": "Tôi đã mua ở trung tâm thương mại gần nhà đấy.",
        "hira": "うちの ちかくの デパートで かったんですよ。",
        "acceptedHira": ["うちのちかくのデパートでかったんですよ", "うちのちかくのデパートでかったんです", "うちのちかくのでぱーとでかったんですよ"],
        "kanjiModel": "うちの近くのデパートで買ったんですよ。",
        "kanjiAccepted": ["うちの近くのデパートで買ったんですよ", "家の近くのデパートで買ったんですよ", "うちの近くのデパートで買ったんです"],
        "grammarRule": "① Đáp lại câu hỏi 「～んですか」 cũng trả lời bằng <b>～んです（よ）</b> để giải thích hoàn cảnh.",
        "breakdown": "うちの ちかくの デパートで (ở TTTM gần nhà tôi) + かったんですよ (tôi đã mua đấy).",
        "traps": [{"regex": "かいましたんです|デパートにかった", "why": "Hành động mua diễn ra TẠI TTTM dùng 「デパートで」, và chia quá khứ ngắn 「かったんですよ」."}]
    },
    {
        "id": "s17_02a", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "どうして 〈ふつうけい〉＋ んですか",
        "vi": "Tại sao tối nay bạn không đến bữa tiệc của công ty?",
        "hira": "どうして こんばん かいしゃの パーティーに いかないんですか。",
        "acceptedHira": [
            "どうしてこんばんかいしゃのパーティーにいかないんですか",
            "どうしてこんばんかいしゃのパーティーにこないんですか",
            "なぜこんばんかいしゃのパーティーにいかないんですか",
            "どうしてこんばんかいしゃのぱーてぃーにいかないんですか"
        ],
        "kanjiModel": "どうしてこんばん会社のパーティーに行かないんですか。",
        "kanjiAccepted": ["どうしてこんばん会社のパーティーに行かないんですか", "どうして今晩会社のパーティーに行かないんですか"],
        "grammarRule": "① Hỏi nguyên nhân, lý do: <b>どうして ～んですか</b>. Phủ định hiện tại: いきません ➔ <b>いかない</b> ＋ んですか.",
        "breakdown": "どうして (tại sao) + こんばん (tối nay) + かいしゃの パーティーに (đến bữa tiệc của công ty) + いかないんですか / こないんですか.",
        "traps": [
            {"regex": "いきませんんですか|いきないんですか", "why": "いきます thuộc Nhóm I ➔ phủ định thông thường là 「いかない」 + んですか (không dùng いきません hay いきない)!"},
            {"regex": "きます➔きない|きないんです", "why": "Nếu dùng 来ます (đến) thì Nhóm III chia thể ない là 「こない」(không phải きない)!"}
        ]
    },
    {
        "id": "s17_02b", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "N ＋ なんです",
        "vi": "Hôm nay là sinh nhật của mẹ tôi.",
        "hira": "きょうは ははの たんじょうびなんです。",
        "acceptedHira": ["きょうはははのたんじょうびなんです", "きょうは、ははのたんじょうびなんです"],
        "kanjiModel": "今日は母の誕生日なんです。",
        "kanjiAccepted": ["今日は母の誕生日なんです", "きょうは母の誕生日なんです"],
        "grammarRule": "① BẪY QUAN TRỌNG NHẤT BÀI 17: <b>Danh từ / Tính từ đuôi な trước んです phải đổi 「だ ➔ な」</b>! Không nói たんじょうびですんです hay たんじょうびだんです, mà phải là <b>たんじょうびなんです</b>!",
        "breakdown": "きょうは (hôm nay) + ははの たんじょうび + なんです (vì là sinh nhật của mẹ).",
        "traps": [
            {"regex": "たんじょうびんです|たんじょうびだんです|たんじょうびですんです|たんじょうびです$", "why": "BẪY CỰC HAY SAI L17! Danh từ (誕生日) + んです BẮT BUỘC phải đổi だ ➔ な ➔ 「たんじょうびなんです」 (thiếu な hoặc dùng です/だ đều sai)!"}
        ]
    },
    {
        "id": "s17_03a", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "どうやって V〈ふつうけい〉＋ んですか",
        "vi": "Cái bánh này, làm như thế nào vậy ạ?",
        "hira": "この ケーキは、どうやって つくるんですか。",
        "acceptedHira": ["このケーキは、どうやってつくるんですか", "このケーキは、どうやってつくったんですか", "このけーきは、どうやってつくるんですか"],
        "kanjiModel": "このケーキは、どうやって作るんですか。（／作ったんですか）",
        "kanjiAccepted": ["このケーキはどうやって作るんですか", "このケーキは、どうやって作るんですか", "このケーキはどうやって作ったんですか"],
        "grammarRule": "① 'Làm như thế nào' = <b>どうやって</b>. Kết hợp ～んですか để hỏi cách thức làm.",
        "breakdown": "この ケーキは (cái bánh này) + どうやって (như thế nào) + つくるんですか / つくったんですか (làm vậy?).",
        "traps": [{"regex": "つくりますんです|つくってんです", "why": "Trước 「んですか」 phải dùng thể thông thường (つくる hoặc つくった), không dùng thể ます hay て."}]
    },
    {
        "id": "s17_03b", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "～んですよ。～んです。",
        "vi": "Đơn giản lắm. Tớ đã xem trên youtube đấy.",
        "hira": "かんたんですよ。ユーチューブで みたんです。",
        "acceptedHira": ["かんたんですよ。ユーチューブでみたんです", "かんたんですよ。youtubeでみたんです", "かんたんですよ。ゆーちゅーぶでみたんです"],
        "kanjiModel": "かんたんですよ。YOUTUBEで見ました／見たんです。",
        "kanjiAccepted": ["かんたんですよ。YOUTUBEで見たんです", "簡単ですよ。YOUTUBEで見たんです", "かんたんですよ。YouTubeで見たんです"],
        "grammarRule": "① Giải thích ngắn gọn + ～んです để làm rõ nguồn/lý do đã xem trên YouTube.",
        "breakdown": "かんたんですよ (đơn giản lắm) + ユーチューブで (trên YouTube) + みたんです (tớ đã xem đấy).",
        "traps": [{"regex": "みますんです|みましたんです", "why": "みました đổi sang thể thông thường là 「みた」 ➔ みたんです."}]
    },
    {
        "id": "s17_04a", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んですが",
        "pattern": "〈ふつうけい〉＋ んですが、～たら いいですか",
        "vi": "Xin lỗi, tôi muốn mua máy ảnh tốt, nên mua ở đâu thì được ạ?",
        "hira": "すみません。いい カメラを かいたいんですが、どこで かったら いいですか。",
        "acceptedHira": ["すみません。いいカメラをかいたいんですが、どこでかったらいいですか", "すみません、いいカメラをかいたいんですが、どこでかったらいいですか", "すみません。いいかめらをかいたいんですが、どこでかったらいいですか"],
        "kanjiModel": "すみません。いいカメラを買いたいんですが、どこで買ったらいいですか。",
        "kanjiAccepted": ["すみません。いいカメラを買いたいんですが、どこで買ったらいいですか"],
        "grammarRule": "① Mở đầu hoàn cảnh trước khi xin lời khuyên: <b>Vたい ＋ んですが</b>. Theo sau là câu hỏi xin lời khuyên: <b>どこで Vたら いいですか</b>.",
        "breakdown": "すみません + いい カメラを かいたいんですが (tôi muốn mua máy ảnh tốt nhưng...) + どこで かったら いいですか (nên mua ở đâu thì được ạ?).",
        "traps": [{"regex": "かいたいですんですが|かいますんですが|かうたら", "why": "「かいたいです」 là tính từ đuôi い ➔ bỏ です thành 「かいたいんです」. Còn thể た của かいます là かった ➔ かったら いいですか!"}]
    },
    {
        "id": "s17_04b", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "Vて みて ください",
        "vi": "Um... Bạn hãy thử xem trang web của FPT Shop nhé.",
        "hira": "うん…エフピーティーショップの サイトで みて みて ください。",
        "acceptedHira": [
            "うん…FPTショップのサイトでみてみてください",
            "うん、FPTショップのサイトでみてみてください",
            "うん…fptショップのサイトでみてみてください",
            "うん、fptショップのサイトでみてみてください",
            "うん…エフピーティーショップのサイトでみてみてください",
            "FPTショップのサイトでみてみてください",
            "fptショップのサイトでみてみてください",
            "うん…FPTシップのサイトでみてみてください"
        ],
        "kanjiModel": "うん…FPTショップのサイトで見てみてください。",
        "kanjiAccepted": ["うん…FPTショップのサイトで見てみてください", "FPTショップのサイトで見てみてください"],
        "grammarRule": "① Thử làm gì đó: <b>Vて ＋ みます ➔ Vて みて ください</b> (xem thử = みて みて ください).",
        "breakdown": "うん… (Um...) + FPTショップの サイトで (trên trang web của FPT Shop) + みて みて ください (hãy thử xem nhé).",
        "traps": [{"regex": "みるみてください|みてみってください", "why": "'Hãy thử xem': みます (nhóm II) chuyển みて + みます (nhóm II) chuyển みて ください ➔ みて みて ください!"}]
    },
    {
        "id": "s17_05a", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んですが",
        "pattern": "～んですが、おしえて いただけませんか",
        "vi": "Tôi không hiểu cách đọc chữ Hán này, bạn chỉ cho tôi được không?",
        "hira": "この かんじの よみかたが わからないんですが、おしえて いただけませんか。",
        "acceptedHira": [
            "このかんじのよみかたがわからないんですが、おしえていただけませんか",
            "このかんじのよみかたがわからないんですが、おしえてくださいませんか",
            "このかんじのよみかたがわからないんですが、おしえてくれませんか"
        ],
        "kanjiModel": "この漢字の読み方がわからないんですが、教えていただけませんか。",
        "kanjiAccepted": ["この漢字の読み方がわからないんですが教えていただけませんか", "この漢字の読み方がわからないんですが、教えていただけませんか", "この漢字の読み方がわからないんですが、教えてくださいませんか"],
        "grammarRule": "① Mở đầu nhờ vả lịch sự: <b>～んですが、Vて いただけませんか／くださいませんか</b>. 'Cách đọc' = <b>よみかた</b> (読みます bỏ ます thêm かた).",
        "breakdown": "この かんじの よみかたが わからないんですが (tôi không hiểu cách đọc chữ Hán này) + おしえて いただけませんか (bạn chỉ giúp tôi được không).",
        "traps": [
            {"regex": "わかりませんんですが|よみかたを", "why": "わから ＋ ないんですが (thể thông thường) và dùng trợ từ 「が」 trước わからない!"}
        ]
    },
    {
        "id": "s17_05b", "lesson": "A2-17", "category": "ÔN TẬP L17 ① ～んです",
        "pattern": "～ですよ",
        "vi": "Cái này phải không? Đây là “Xuất phát” đấy.",
        "hira": "これですか。これは しゅっぱつですよ。",
        "acceptedHira": ["これですか。これはしゅっぱつですよ", "これですか。これは「しゅっぱつ」ですよ", "これですか。これはしゅっぱつです"],
        "kanjiModel": "これですか。これは「出発（しゅっぱつ）」ですよ。",
        "kanjiAccepted": ["これですか。これは出発ですよ", "これですか。これは「出発」ですよ"],
        "grammarRule": "① Xuất phát = 出発 (<b>しゅっぱつ</b> - có âm ngắt っ và bán đục âm ぱ).",
        "breakdown": "これですか (cái này phải không?) + これは 「しゅっぱつ」ですよ (đây là 'xuất phát' đấy).",
        "traps": [{"regex": "しゅつはつ|しゅぱつ|しゅっはつ", "why": "Từ Kanji L13 出発 đọc là 「しゅっぱつ」 (nhớ âm ngắt っ nhỏ và maru ぱ!)."}]
    },
    {
        "id": "s17_np1", "lesson": "A2-17", "category": "KIẾN THỨC L17_A2.1",
        "pattern": "～んですが、Vて くださいませんか",
        "vi": "Tôi muốn mua máy tính, không biết loại nào thì tốt?",
        "hira": "パソコンを かいたいんですが、どれが いいですか。",
        "acceptedHira": ["パソコンをかいたいんですが、どれがいいですか", "ぱそこんをかいたいんですが、どれがいいですか"],
        "kanjiModel": "パソコンを買いたいんですが、どれがいいですか。",
        "kanjiAccepted": ["パソコンを買いたいんですが、どれがいいですか", "パソコンを買いたいんですがどれがいいですか"],
        "grammarRule": "① Khi dùng ～んですが để hỏi xin tư vấn lựa chọn từ nhiều loại: <b>どれが いいですか</b> (cái nào thì tốt).",
        "breakdown": "パソコンを かいたいんですが (tôi muốn mua máy tính...) + どれが いいですか (loại nào thì tốt?).",
        "traps": [{"regex": "かいたいですんですが|どれはいい", "why": "「かいたい」 không thêm です trước んです; nghi vấn từ 「どれ」 đi với trợ từ 「が」!"}]
    },
    {
        "id": "s17_np2", "lesson": "A2-17", "category": "KIẾN THỨC L17_A2.1",
        "pattern": "どうしたんですか / ～んです",
        "vi": "Trông bạn không được khỏe nhỉ. Bạn đang mệt à?",
        "hira": "げんきが ないですね。つかれて いるんですか。",
        "acceptedHira": ["げんきがないですね。つかれているんですか"],
        "kanjiModel": "元気がないですね。疲れているんですか。",
        "kanjiAccepted": ["元気がないですね。疲れているんですか"],
        "grammarRule": "① Nhìn sắc mặt đối phương rồi dùng <b>～んですか</b> để hỏi thăm tình hình. 'Đang mệt' = つかれて いる ➔ つかれて いるんですか.",
        "breakdown": "げんきが ないですね (trông không có sức sống/khỏe nhỉ) + つかれて いるんですか (bạn đang mệt à?).",
        "traps": [{"regex": "つかれるんですか|つかれていますんですか", "why": "Đang mệt là trạng thái 「つかれて いる」 ➔ đưa về thể thông thường: つかれて いるんですか."}]
    },
    {
        "id": "s17_np3", "lesson": "A2-17", "category": "KIẾN THỨC L17_A2.1",
        "pattern": "Aい ＋ んです",
        "vi": "Tôi hơi đau đầu một chút.",
        "hira": "ちょっと あたまが いたいんです。",
        "acceptedHira": ["ちょっとあたまがいたいんです"],
        "kanjiModel": "ちょっと頭が痛いんです。",
        "kanjiAccepted": ["ちょっと頭が痛いんです"],
        "grammarRule": "① Giải thích hoàn cảnh với tính từ đuôi い: bỏ です giữ nguyên い + んです (<b>いたい ＋ んです</b>).",
        "breakdown": "ちょっと (một chút) + あたまが いたいんです (tôi bị đau đầu).",
        "traps": [{"regex": "いたいなんです|いたいですんです", "why": "「いたい」 là tính từ đuôi い (KHÔNG phải đuôi な) ➔ ghép thẳng 「いたいんです」, KHÔNG thêm な!"}]
    },
    {
        "id": "s17_np4", "lesson": "A2-17", "category": "KIẾN THỨC L17_A2.1",
        "pattern": "N ＋ なんです",
        "vi": "Tại sao bạn đến muộn? — Tại đường tắc.",
        "hira": "どうして おくれたんですか。みちが じゅうたいなんです。",
        "acceptedHira": ["どうしておくれたんですか。みちがじゅうたいなんです", "みちがじゅうたいなんです"],
        "kanjiModel": "どうしておくれたんですか。道がじゅうたいなんです。",
        "kanjiAccepted": ["どうしておくれたんですか。道がじゅうたいなんです", "どうして遅れたんですか。道が渋滞なんです"],
        "grammarRule": "① 'Tắc đường' = じゅうたい (Danh từ). Khi giải thích nguyên nhân với んです ➔ phải dùng <b>な + んです</b> (じゅうたいなんです)!",
        "breakdown": "どうして おくれたんですか (tại sao đến muộn?) + みちが じゅうたいなんです (vì đường tắc).",
        "traps": [{"regex": "じゅうたいんです|おくりました|おくれたのですか", "why": "じゅうたい là danh từ nên bắt buộc thêm な trước んです: じゅうたいなんです! (おくれました ➔ おくれた)."}]
    },
    {
        "id": "s17_np5", "lesson": "A2-17", "category": "KIẾN THỨC L17_A2.1",
        "pattern": "どうして～んですか / ～んです",
        "vi": "Tại sao bạn học tiếng Nhật vậy? — Vì tôi muốn làm việc ở Nhật.",
        "hira": "どうして にほんごを べんきょうして いるんですか。にほんで はたらきたいんです。",
        "acceptedHira": ["どうしてにほんごをべんきょうしているんですか。にほんではたらきたいんです", "にほんではたらきたいんです"],
        "kanjiModel": "どうして日本語を勉強しているんですか。日本で働きたいんです。",
        "kanjiAccepted": ["どうして日本語を勉強しているんですか。日本で働きたいんです"],
        "grammarRule": "① Câu hỏi lý do trọng tâm: <b>どうして ～んですか</b>. Giải thích bằng Vたい ＋ んです (không thêm だ hay です!).",
        "breakdown": "どうして にほんごを べんきょうして いるんですか + にほんで はたらきたいんです.",
        "traps": [{"regex": "はたらきたいですんです|はたらきたいなんです", "why": "Đuôi 「～たい」 chia như tính từ đuôi い ➔ ghép thẳng んです thành 「はたらきたいんです」, không thêm な hay です!"}]
    },
    {
        "id": "s17_np6", "lesson": "A2-17", "category": "KIẾN THỨC L17_A2.1",
        "pattern": "～んですか / Nに ～んです",
        "vi": "Đồng hồ nhìn cute thế. Cậu mua ở đâu đấy? — Tôi đã nhận từ bố làm quà mừng tốt nghiệp.",
        "hira": "かわいい とけいですね。どこで かったんですか。そつぎょうの おいわいに ちちに もらったんです。",
        "acceptedHira": [
            "かわいいとけいですね。どこでかったんですか。そつぎょうのおいわいにちちにもらったんです",
            "そつぎょうのおいわいにちちにもらったんです",
            "そつぎょうのおいわいにちちからもらったんです"
        ],
        "kanjiModel": "かわいい時計ですね。どこで買ったんですか。卒業のお祝いに父にもらったんです。",
        "kanjiAccepted": ["かわいい時計ですね。どこで買ったんですか。卒業のお祝いに父にもらったんです", "卒業のお祝いに父にもらったんです"],
        "grammarRule": "① Ghi chú L17: làm quà mừng tốt nghiệp = <b>そつぎょうの おいわいに</b> (nhớ Kanji L17: お祝い = おいわい!).",
        "breakdown": "かわいい とけいですね + どこで かったんですか + そつぎょうの おいわいに ちちに もらったんです.",
        "traps": [{"regex": "おいわいでちち|もらいません|もらいましたんです", "why": "'Nhân dịp làm quà mừng' dùng trợ từ 「に」 (おいわいに); trước んです chia quá khứ ngắn 「もらったんです」!"}]
    },
    {
        "id": "s17_06", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vた ＋ N",
        "vi": "Đây là ảnh đã chụp ở Nhật.",
        "hira": "これは にほんで とった しゃしんです。",
        "acceptedHira": ["これはにほんでとったしゃしんです"],
        "kanjiModel": "これは日本で撮った写真です。",
        "kanjiAccepted": ["これは日本でとった写真です", "これは日本で撮った写真です"],
        "grammarRule": "② 'Chụp ảnh' = とります (Nhóm I) ➔ thể quá khứ ngắn là <b>とった</b>. Đừng quên âm ngắt っ!",
        "breakdown": "これは (đây là) + にほんで とった しゃしん (ảnh đã chụp ở Nhật) + です.",
        "traps": [{"regex": "とりた|とりましたしゃしん|にほんにとった", "why": "とります (Nhóm I) chia thể た biến âm thành っ ➔ とった; hành động chụp tại Nhật dùng 「にほんで」."}]
    },
    {
        "id": "s17_07", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Nに／から Vた ＋ N",
        "vi": "Đây là đồng hồ nhận được từ bố.",
        "hira": "これは ちちに もらった とけいです。",
        "acceptedHira": ["これはちちにもらったとけいです", "これはちちからもらったとけいです"],
        "kanjiModel": "これは父に／からもらった時計です。",
        "kanjiAccepted": ["これは父にもらった時計です", "これは父からもらった時計です"],
        "grammarRule": "② Nhận từ ai đó: <b>ちちに／から もらった</b> ＋ とけい.",
        "breakdown": "これは + ちちに/から もらった (đã nhận từ bố) + とけいです (là đồng hồ).",
        "traps": [{"regex": "もらいました|とけ", "why": "Trong cụm bổ ngữ phải chia 「もらった」; đồng hồ đọc là 「とけい」 (có chữ い)."}]
    },
    {
        "id": "s17_08", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vた ことが ある ＋ N",
        "vi": "Đây là bộ phim tôi đã từng xem.",
        "hira": "これは わたしが みた ことが ある えいがです。",
        "acceptedHira": ["これはわたしがみたことがあるえいがです", "これはみたことがあるえいがです"],
        "kanjiModel": "これは（私が）見たことがある映画です。",
        "kanjiAccepted": ["これは私が見たことがある映画です", "これは見たことがある映画です", "これはわたしがみたことがあるえいがです"],
        "grammarRule": "② Kết hợp ngữ pháp 'đã từng làm' (<b>Vた ことが ある</b> — đưa あります về ある!) để bổ nghĩa cho えいが.",
        "breakdown": "これは + (わたしが) みた ことが ある (mà tôi đã từng xem) + えいがです.",
        "traps": [{"regex": "ことがありますえいが|みるたこと", "why": "Trước danh từ 「えいが」, 「あります」 phải chia về thể thông thường 「ある」 ➔ みた ことが ある えいが!"}]
    },
    {
        "id": "s17_09", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vる ＋ ところ",
        "vi": "Chỗ này là nơi đọc sách.",
        "hira": "ここは ほんを よむ ところです。",
        "acceptedHira": ["ここはほんをよむところです"],
        "kanjiModel": "ここは本を読むところです。",
        "kanjiAccepted": ["ここは本を読むところです", "ここは本を読む所です"],
        "grammarRule": "② 'Nơi / chỗ để làm gì' dùng danh từ <b>ところ</b> (để Vる đứng trướcところ).",
        "breakdown": "ここは (chỗ này) + ほんを よむ (đọc sách) + ところです (là nơi).",
        "traps": [{"regex": "よみますところ|ここがほんを", "why": "Chủ ngữ chính của câu giới thiệu nơi này dùng 「ここは」; động từ trước ところ chia thể Từ điển 「よむ」."}]
    },
    {
        "id": "s17_10", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vている ＋ N",
        "vi": "Chú chó đang chơi ở vườn là Milo chan.",
        "hira": "にわで あそんで いる いぬは ミロちゃんです。",
        "acceptedHira": ["にわであそんでいるいぬはミロちゃんです", "にわであそんでいるいぬはみろちゃんです"],
        "kanjiModel": "庭で遊んでいる犬はミロちゃんです。",
        "kanjiAccepted": ["庭で遊んでいる犬はミロちゃんです", "庭で遊んでいる犬はみろちゃんです"],
        "grammarRule": "② Tương tự câu #12 Kaiwa Mid 2! 'Ở vườn' = <b>にわで</b>; 'đang chơi' = <b>あそんで いる</b>; 'chú chó' = いぬ.",
        "breakdown": "にわで あそんで いる いぬ (chú chó đang chơi ở vườn) + は + ミロちゃんです.",
        "traps": [{"regex": "にわにあそん|あそびて", "why": "Nơi hành động chơi dùng 「で」 (にわで); thể て của あそびます là 「あそんで」."}]
    },
    {
        "id": "s17_11", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Sが Vて くれた ＋ N",
        "vi": "Cơm hộp mẹ làm cho tôi là ngon nhất.",
        "hira": "ははが つくって くれた おべんとうは いちばん おいしいです。",
        "acceptedHira": ["ははがつくってくれたおべんとうはいちばんおいしいです"],
        "kanjiModel": "母が作ってくれたお弁当はいちばんおいしいです。",
        "kanjiAccepted": ["母が作ってくれたお弁当はいちばんおいしいです", "母が作ってくれたおべんとうはいちばんおいしいです"],
        "grammarRule": "② Cô chú thích mẫu <b>Sが Vて くれます ➔ Sが Vて くれた N</b> ('ai đó làm cho tôi'). Chủ ngữ người làm trong mệnh đề bổ ngữ dùng trợ từ <b>が</b> (ははが)!",
        "breakdown": "ははが (mẹ - chủ thể trong mệnh đề phụ) + つくって くれた (đã làm cho tôi) + おべんとうは (cơm hộp thì) + いちばん おいしいです.",
        "traps": [
            {"regex": "はははつくって|つくってあげた|つくってもらった", "why": "'Mẹ làm cho tôi' phải dùng 「母<b>が</b> 作って くれた」 (nếu dùng もらった thì phải là 母<b>に</b>!)."},
            {"regex": "くれましたおべんとう", "why": "Trước おべんとう phải chuyển くれました về thể thông thường 「くれた」!"}
        ]
    },
    {
        "id": "s17_12", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "V〈ふつうけい〉＋ Nを したいです",
        "vi": "Tớ muốn làm công việc sử dụng tiếng Nhật.",
        "hira": "にほんごを つかう しごとを したいです。",
        "acceptedHira": ["にほんごをつかうしごとをしたいです"],
        "kanjiModel": "日本語を使う仕事をしたいです。",
        "kanjiAccepted": ["日本語を使う仕事をしたいです"],
        "grammarRule": "② Bổ ngữ <b>にほんごを つかう しごと</b> đóng vai trò làm tân ngữ cho したいです (làm công việc...).",
        "breakdown": "にほんごを つかう しごと (công việc sử dụng tiếng Nhật) + を したいです (muốn làm).",
        "traps": [{"regex": "つかいますしごと|しごとがしたい", "why": "Chia 「つかう」 trước しごと; muốn làm công việc gì dùng 「しごとを したいです」 (hoặc が cũng gặp nhưng cô chữa を)."}]
    },
    {
        "id": "s17_13", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vた ＋ ところ",
        "vi": "Nơi tớ đã gặp chồng mình là trường cấp 3.",
        "hira": "おっとに あった ところは こうこうです。",
        "acceptedHira": ["おっとにあったところはこうこうです", "しゅじんにあったところはこうこうです"],
        "kanjiModel": "夫に会ったところは高校です。",
        "kanjiAccepted": ["夫に会ったところは高校です", "おっとに会ったところは高校です"],
        "grammarRule": "② Động từ 'gặp ai' luôn dùng trợ từ <b>に</b> (おっとに 会った)! 'Chồng mình' = おっと / しゅじん; 'trường cấp 3' = こうこう.",
        "breakdown": "おっとに あった (đã gặp chồng) + ところは (nơi mà... thì) + こうこうです (là trường cấp 3).",
        "traps": [{"regex": "おっとをあった|あいまた", "why": "会います đi với trợ từ 「に」 (người gặp), KHÔNG dùng 「を」! Thể た của 会います là 「あった」."}]
    },
    {
        "id": "s17_14", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vない ＋ 人と ～たいです",
        "vi": "Tớ muốn kết hôn với người không uống rượu.",
        "hira": "おさけを のまない ひとと けっこんしたいです。",
        "acceptedHira": ["おさけをのまないひととけっこんしたいです"],
        "kanjiModel": "お酒を飲まない人と結婚したいです。",
        "kanjiAccepted": ["お酒を飲まない人と結婚したいです"],
        "grammarRule": "② Kết hôn với ai dùng trợ từ <b>と</b>: N ＋ <b>と</b> ＋ けっこんしたいです. Nhớ Kanji 結婚 = けっこん (có っ nhỏ!).",
        "breakdown": "おさけを のまない ひと (người không uống rượu) + と (với) + けっこんしたいです (muốn kết hôn).",
        "traps": [
            {"regex": "ひとをけっこん|ひとにけっこん", "why": "Kết hôn VỚI ai dùng trợ từ 「と」 ➔ ～ひとと けっこんしたいです!"},
            {"regex": "のみない|のみませんひと|けこん", "why": "のみます chia thể ない là 「のまない」; 結婚 là 「けっこん」 (nhớ âm ngắt っ)."}
        ]
    },
    {
        "id": "s17_15", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vない ＋ N",
        "vi": "Người không hút thuốc lá thì thật ngầu!",
        "hira": "たばこを すわない ひとは かっこいいです。",
        "acceptedHira": ["たばこをすわないひとはかっこいいです"],
        "kanjiModel": "たばこを吸わない人はかっこいいです。",
        "kanjiAccepted": ["たばこを吸わない人はかっこいいです"],
        "grammarRule": "② Mẫu câu trong note L16 + ôn tập L17 #10: すいます ➔ すわない (nhớ い ➔ わ!). Ngầu/đẹp trai = <b>かっこいいです</b>.",
        "breakdown": "たばこを すわない ひと (người không hút thuốc) + は + かっこいいです (thật ngầu).",
        "traps": [{"regex": "すいないひと|かこいい", "why": "すいます ➔ すわない; かっこいい có âm ngắt っ nhỏ ở giữa!"}]
    },
    {
        "id": "s17_16", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vる ＋ もの",
        "vi": "Tôi sẽ tặng mẹ món đồ sử dụng khi du lịch.",
        "hira": "ははに りょこうの とき つかう ものを あげます。",
        "acceptedHira": ["ははにりょこうのときつかうものをあげます"],
        "kanjiModel": "母に旅行のとき使うものをあげます。",
        "kanjiAccepted": ["母に旅行のとき使うものをあげます"],
        "grammarRule": "② Tặng cho ai dùng <b>に</b> (ははに ... あげます). Cụm bổ ngữ: りょこうの とき つかう もの (món đồ dùng khi đi du lịch).",
        "breakdown": "ははに (cho mẹ) + りょこうの とき つかう ものを (món đồ sử dụng khi du lịch) + あげます (tặng).",
        "traps": [{"regex": "りょこうとき|つかわない|くれます", "why": "りょこう là danh từ cần thêm 「の」 trước とき; 'tôi tặng mẹ' dùng 「あげます」 (không phải くれます!)."}]
    },
    {
        "id": "s17_17", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Vる ＋ もの",
        "vi": "Khi chuyển nhà, tôi đã nhận được từ bạn bè món đồ trang trí phòng.",
        "hira": "ひっこしの とき、ともだちに へやに かざる ものを もらいました。",
        "acceptedHira": ["ひっこしのとき、ともだちにへやにかざるものをもらいました", "ひっこしのとき、ともだちからへやにかざるものをもらいました"],
        "kanjiModel": "引っ越しのとき、友だちに／から部屋にかざるものをもらいました。",
        "kanjiAccepted": ["引っ越しのとき友だちに部屋にかざるものをもらいました", "引っ越しのとき友だちから部屋にかざるものをもらいました", "ひっこしのときともだちにへやにかざるものをもらいました"],
        "grammarRule": "② Động từ mới L17: <b>かざります ➔ かざる</b> (trang trí). Trang trí cái gì ở đâu (đặt gắn vào chỗ đó): <b>へやに</b> かざる!",
        "breakdown": "ひっこしの とき (khi chuyển nhà) + ともだちに/から (từ bạn bè) + へやに かざる ものを (món đồ trang trí ở phòng) + もらいました (đã nhận).",
        "traps": [{"regex": "へやをかざる|かざりますもの|ひこし", "why": "ひっこし có âm ngắt っ; trang trí vào trong phòng dùng trợ từ 「に」 (へやに かざる)."}]
    },
    {
        "id": "s17_18", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Sが Vる ＋ N",
        "vi": "Sau khi sinh em bé, cần nhiều đồ em bé mặc.",
        "hira": "しゅっさんの あとで、あかちゃんが きる ものが たくさん ひつようです。",
        "acceptedHira": ["しゅっさんのあとで、あかちゃんがきるものがたくさんひつようです", "しゅっさんのあと、あかちゃんがきるものがたくさんひつようです"],
        "kanjiModel": "出産のあとで、あかちゃんが着るものがたくさんひつようです。",
        "kanjiAccepted": ["出産のあとであかちゃんが着るものがたくさん必要です", "出産のあとであかちゃんが着るものがたくさんひつようです"],
        "grammarRule": "② 'Sau khi N' = <b>Nの あとで</b>. Chủ ngữ trong mệnh đề bổ ngữ dùng 「が」 (あかちゃんが きる). 'Cần thiết' = <b>ひつようです</b> (đi với trợ từ が!).",
        "breakdown": "しゅっさんの あとで (sau khi sinh) + あかちゃんが きる ものが (đồ em bé mặc) + たくさん ひつようです (cần rất nhiều).",
        "traps": [
            {"regex": "あかちゃんはきる|しゅっさんあとで", "why": "Trong cụm bổ ngữ dùng 「あかちゃんが」 (không phải は); sau danh từ しゅっさん thêm 「の」 trước あとで!"},
            {"regex": "ものをひつよう", "why": "Tính từ 「ひつようです」 (cần) đi với trợ từ 「が」 (～ものが ひつようです)."}
        ]
    },
    {
        "id": "s17_19", "lesson": "A2-17", "category": "ÔN TẬP L17 ② Sが V〈ふつうけい〉＋ N",
        "pattern": "Aなで、V〈ふつうけい〉＋ N",
        "vi": "Tôi muốn đến quán cà phê yên tĩnh và có thể học tốt.",
        "hira": "しずかで よく べんきょうが できる きっさてんに いきたいです。",
        "acceptedHira": ["しずかでよくべんきょうができるきっさてんにいきたいです"],
        "kanjiModel": "しずかで よく勉強ができる喫茶店に行きたいです。",
        "kanjiAccepted": ["静かでよく勉強ができる喫茶店に行きたいです", "しずかでよく勉強ができる喫茶店に行きたいです"],
        "grammarRule": "② Kết hợp 2 ý bổ nghĩa cùng danh từ '喫茶店': <b>しずか（なA ➔ で）＋ よく べんきょうが できる ＋ きっさてん</b>! Lưu ý 'có thể học' dùng <b>べんきょうが できる</b> (trợ từ が!).",
        "breakdown": "しずかで (yên tĩnh và) + よく べんきょうが できる (có thể học tốt) + きっさてんに いきたいです.",
        "traps": [
            {"regex": "しずかなよく|しずかて", "why": "Nối tính từ đuôi な với mệnh đề phía sau dùng 「しずかで」!"},
            {"regex": "べんきょうができます|べんきょうをできる", "why": "Trước 「きっさてん」 phải đổi できます ➔ できる, và できる đi với trợ từ 「が」 (べんきょうが できる)."}
        ]
    },
    {
        "id": "s17_np7", "lesson": "A2-17", "category": "NGỮ PHÁP L17 Mở đầu ～んですが",
        "pattern": "～んですが、～て くださいませんか",
        "vi": "Tôi không hiểu tiếng Nhật lắm, nên anh/chị chỉ cho tôi được không?",
        "hira": "にほんごが よく わからないんですが、おしえて くださいませんか。",
        "acceptedHira": [
            "にほんごがよくわからないんですが、おしえてくださいませんか",
            "にほんごがよくわかりませんが、おしえてくださいませんか"
        ],
        "kanjiModel": "日本語がよく分からないんですが、教えてくださいませんか。",
        "kanjiAccepted": ["日本語がよく分からないんですが、教えてくださいませんか", "日本語がよくわからないんですが、教えてくださいませんか"],
        "grammarRule": "Ngữ pháp L17 (mục 1): Dùng <b>V〈ふつうけい〉＋ んですが</b> để nêu bối cảnh mềm mại trước khi nhờ vả <b>～て くださいませんか</b>.",
        "breakdown": "にほんごが よく わからないんですが (tôi không hiểu tiếng Nhật lắm nên...) + おしえて くださいませんか (xin chỉ giúp tôi được không?).",
        "traps": [
            {"regex": "わかりない|わからないだんです", "why": "わかります (Nhóm I) chia thể ない ➔ わからない + んです (không thêm だ trước ん!)."}
        ]
    },
    {
        "id": "s17_np8", "lesson": "A2-17", "category": "NGỮ PHÁP L17 Mở đầu ～んですが",
        "pattern": "ちょっと Nが あるんですが…",
        "vi": "Tôi có chút việc muốn nhờ...",
        "hira": "ちょっと おねがいが あるんですが。",
        "acceptedHira": ["ちょっとおねがいがあるんですが"],
        "kanjiModel": "ちょっとお願いがあるんですが…。",
        "kanjiAccepted": ["ちょっとお願いがあるんですが", "ちょっとお願いがあるんですが…"],
        "grammarRule": "Mẫu mở lời nhờ vả kinh điển L17: <b>ちょっと おねがいが あるんですが…</b> (「あります」 ở thể thông thường là <b>ある</b> + <b>んです</b>).",
        "breakdown": "ちょっと (một chút) + おねがいが (điều nhờ vả) + あるんですが (có đấy ạ, nhưng...).",
        "traps": [
            {"regex": "ありますんですが|あるだんです|おねがいをある", "why": "「あります」 chuyển thể thông thường là 「ある」 + んですが (không để nguyên あります, không dùng trợ từ を)."}
        ]
    },
    {
        "id": "s17_np9", "lesson": "A2-17", "category": "NGỮ PHÁP L17 Hỏi tình hình",
        "pattern": "どうしたんですか",
        "vi": "Có chuyện gì vậy?",
        "hira": "どうしたんですか。",
        "acceptedHira": ["どうしたんですか"],
        "kanjiModel": "どうしたんですか。",
        "kanjiAccepted": ["どうしたんですか"],
        "grammarRule": "Ngữ pháp L17 (mục 2): Câu hỏi thăm tình hình khi thấy ai có vẻ bất thường (mệt, lo lắng...): <b>どうしたんですか</b> (Thể た của します = した + んですか).",
        "breakdown": "どう (thế nào/sao vậy) + した (đã xảy ra/làm gì) + んですか.",
        "traps": [
            {"regex": "どうしますか|どうするんですか|どうしたですか", "why": "Hỏi chuyện vừa xảy ra với ai đó dùng cố định thì quá khứ ngắn 「どうしたんですか」 (không dùng どうしたですか)."}
        ]
    },

    # ================= LESSON 18 =================
    {
        "id": "s18_01", "lesson": "A2-18", "category": "ÔN TẬP L18 ① と おもいます",
        "pattern": "V〈ふつうけい〉＋ と おもいます",
        "vi": "Tôi nghĩ anh Yamada sẽ không mang ô đến lớp học.",
        "hira": "やまださんは きょうしつに かさを もって こないと おもいます。",
        "acceptedHira": ["やまださんはきょうしつにかさをもってこないとおもいます"],
        "kanjiModel": "山田さんは教室に傘を持ってこないと思います。",
        "kanjiAccepted": ["山田さんはきょうしつに傘を持ってこないと思います", "山田さんは教室に傘を持ってこないと思います"],
        "grammarRule": "① BẪY KINH ĐIỂN NHÓM III: 'Mang đến' là <b>持って きます ➔ phủ định thể thông thường là 持って こない</b> (KHÔNG phải きない!). Sau đó nối với 「と おもいます」.",
        "breakdown": "やまださんは + きょうしつに (đến lớp học) + かさを もって こない (sẽ không mang ô đến) + と おもいます (tôi nghĩ).",
        "traps": [
            {"regex": "もってきない|もってくらない", "why": "BẪY ĐỘNG TỪ NHÓM III! 「きます (đến)」 chia sang thể ない phải là 「こない」 ➔ もって こないと おもいます (KHÔNG phải きない)!"},
            {"regex": "こないとおもう$|こないと、", "why": "Cuối câu lịch sự là 「と おもいます」."}
        ]
    },
    {
        "id": "s18_02", "lesson": "A2-18", "category": "ÔN TẬP L18 ① と おもいます",
        "pattern": "Aな ＋ だ ＋ と おもいます",
        "vi": "Tôi nghĩ việc học tiếng Nhật vất vả.",
        "hira": "にほんごの べんきょうは たいへんだと おもいます。",
        "acceptedHira": ["にほんごのべんきょうはたいへんだとおもいます"],
        "kanjiModel": "日本語の勉強はたいへんだと思います。",
        "kanjiAccepted": ["日本語の勉強はたいへんだと思います", "日本語の勉強は大変だと思います"],
        "grammarRule": "① CỰC QUAN TRỌNG BÀI 18: <b>Tính từ đuôi な / Danh từ trước 「と おもいます」 BẮT BUỘC phải có 「だ」</b> ở thì hiện tại khẳng định (<b>たいへん ＋ だ ＋ と おもいます</b> — khác với んです là な)!",
        "breakdown": "にほんごの べんきょうは (việc học tiếng Nhật) + たいへんだ (vất vả) + と おもいます (tôi nghĩ là).",
        "traps": [
            {"regex": "たいへんと|たいへんなと|たいへんですと", "why": "BẪY LỚN NHẤT BÀI 18! Trước 「と おもいます」, tính từ đuôi な / Danh từ BẮT BUỘC phải thêm 「だ」 ➔ 「たいへんだと おもいます」 (KHÔNG dùng な hay bỏ だ hay です)!"}
        ]
    },
    {
        "id": "s18_03", "lesson": "A2-18", "category": "ÔN TẬP L18 ① と おもいます",
        "pattern": "Vた ＋ と おもいます",
        "vi": "Tôi nghĩ Sakura đã mua rất nhiều bánh kẹo ngon.",
        "hira": "さくらさんは おいしい おかしを たくさん かったと おもいます。",
        "acceptedHira": ["さくらさんはおいしいおかしをたくさんかったとおもいます"],
        "kanjiModel": "さくらさんはおいしいお菓子をたくさん買ったと思います。",
        "kanjiAccepted": ["さくらさんはおいしいお菓子をたくさん買ったと思います"],
        "grammarRule": "① Đã mua = かいました ➔ thể thông thường quá khứ là <b>かった</b> + と おもいます.",
        "breakdown": "さくらさんは + おいしい おかしを (bánh kẹo ngon) + たくさん かった (đã mua nhiều) + と おもいます.",
        "traps": [{"regex": "かいましたと|かっただと", "why": "Trước 「と おもいます」 dùng thể thông thường 「かった」, và KHÔNG thêm 「だ」 sau động từ!"}]
    },
    {
        "id": "s18_04", "lesson": "A2-18", "category": "ÔN TẬP L18 ① と おもいます",
        "pattern": "Nの ほうが ～と おもいます",
        "vi": "Tôi nghĩ rau xanh thì tốt hơn cho sức khỏe.",
        "hira": "やさいの ほうが けんこうに いいと おもいます。",
        "acceptedHira": ["やさいのほうがけんこうにいいとおもいます"],
        "kanjiModel": "野菜のほうが健康にいいと思います。",
        "kanjiAccepted": ["野菜のほうが健康にいいと思います"],
        "grammarRule": "① So sánh hơn (nhắc lại): <b>Nの ほうが ～いいです</b>. Tính từ đuôi い 「いい」 đưa trực tiếp trước 「と おもいます」 (KHÔNG thêm だ!).",
        "breakdown": "やさいの ほうが (phía rau xanh - tốt hơn) + けんこうに (cho sức khỏe) + いいと おもいます.",
        "traps": [
            {"regex": "いいだと|いいですと", "why": "Tính từ đuôi い 「いい」 đứng trực tiếp trước 「と おもいます」, KHÔNG thêm 「だ」 hay 「です」!"},
            {"regex": "けんこうでいい|けんこうをいい", "why": "'Tốt cho sức khỏe' dùng trợ từ 「に」 ➔ けんこうに いい."}
        ]
    },
    {
        "id": "s18_05", "lesson": "A2-18", "category": "ÔN TẬP L18 ① と おもいます",
        "pattern": "Vなかった ＋ と おもいます",
        "vi": "Tôi nghĩ Lyly đã không tự mình nấu ăn hôm qua.",
        "hira": "リリさんは きのう じぶんで りょうりを つくらなかったと おもいます。",
        "acceptedHira": ["リリさんはきのうじぶんでりょうりをつくらなかったとおもいます", "りりさんはきのうじぶんでりょうりをつくらなかったとおもいます"],
        "kanjiModel": "リリさんはきのう自分で料理を作らなかったと思います。",
        "kanjiAccepted": ["リリさんはきのう自分で料理を作らなかったと思います"],
        "grammarRule": "① 'Tự mình' = <b>じぶんで</b> (Kanji L14). Phủ định quá khứ của つくります (nhóm I) ➔ つくりませんでした ➔ <b>つくらなかった</b>!",
        "breakdown": "リリさんは + きのう (hôm qua) + じぶんで (tự mình) + りょうりを つくらなかった (đã không nấu ăn) + と おもいます.",
        "traps": [{"regex": "つくりませんでしたと|つくらないかった|じぶんに", "why": "つくりませんでした đổi sang thể thông thường là 「つくらなかった」 (nhóm I: り➔ら + なかった); 'tự mình' dùng trợ từ 「で」: じぶんで!"}]
    },
    {
        "id": "s18_06", "lesson": "A2-18", "category": "ÔN TẬP L18 ① Nについて、どう おもいますか",
        "pattern": "N ＋ について、どう おもいますか",
        "vi": "Bạn nghĩ như thế nào về xe máy điện của Việt Nam?",
        "hira": "ベトナムの でんきバイクについて どう おもいますか。",
        "acceptedHira": ["ベトナムのでんきバイクについてどうおもいますか", "べとなむのでんきばいくについてどうおもいますか"],
        "kanjiModel": "ベトナムの電気バイクについてどう思いますか。",
        "kanjiAccepted": ["ベトナムの電気バイクについてどう思いますか"],
        "grammarRule": "① Hỏi ý kiến về chủ đề N: <b>N ＋ について、どう おもいますか</b>.",
        "breakdown": "ベトナムの でんきバイクについて (về xe máy điện của VN) + どう おもいますか (bạn nghĩ thế nào?).",
        "traps": [{"regex": "なんだとおもいます|どうやっておもいます", "why": "'Nghĩ như thế nào về N' dùng cấu trúc cố định 「Nについて、どう おもいますか」 (không dùng どうやって)."}]
    },
    {
        "id": "s18_07", "lesson": "A2-18", "category": "ÔN TẬP L18 ② と いって いました",
        "pattern": "Sは 〈ふつうけい〉＋ と いって いました",
        "vi": "Mori san đã nói rằng, vì quá bận nên sẽ không gặp ai cả.",
        "hira": "もりさんは いそがしすぎて、だれにも あわないと いって いました。",
        "acceptedHira": ["もりさんはいそがしすぎて、だれにもあわないといっていました"],
        "kanjiModel": "もりさんはいそがしすぎて、だれにも会わないと言っていました。",
        "kanjiAccepted": ["もりさんはいそがしすぎて、だれにも会わないと言っていました", "もりさんは忙しすぎて、だれにも会わないと言っていました"],
        "grammarRule": "② Tường thuật lời nói: <b>Sは 〈ふつうけい〉＋ と いって いました</b>. Kết hợp 'quá V/A' = <b>いそがしすぎて</b> (いそがしい bỏ い + すぎて); 'không gặp ai cả' = だれにも あわない (nhớ あいます ➔ あわない!).",
        "breakdown": "もりさんは + いそがしすぎて (vì quá bận nên) + だれにも あわない (sẽ không gặp ai) + と いって いました (đã nói rằng).",
        "traps": [
            {"regex": "あいない|あいませんと", "why": "会います (nhóm I đuôi い) chia thể ない phải là 「あわない」 (い ➔ わ, KHÔNG phải あいない)!"},
            {"regex": "いそがしいすぎて|いいました$|いって います$", "why": "Quá bận là 「いそがしすぎて」 (bỏ い rồi thêm すぎて); câu tường thuật của cô dùng 「と いって いました」."}
        ]
    },
    {
        "id": "s18_08", "lesson": "A2-18", "category": "ÔN TẬP L18 ② と いって いました",
        "pattern": "Nが Aなだった ＋ と いって いました",
        "vi": "Nobita đã nói rằng, bài kiểm tra hôm qua đã đơn giản.",
        "hira": "のびたくんは、きのうの テストが かんたんだったと いって いました。",
        "acceptedHira": ["のびたくんは、きのうのテストがかんたんだったといっていました", "のびたさんは、きのうのテストがかんたんだったといっていました", "のびたくんは、きのうのてすとがかんたんだったといっていました"],
        "kanjiModel": "のび太くんは、きのうのテストがかんたんだったと言っていました。",
        "kanjiAccepted": ["のび太くんは、きのうのテストがかんたんだったと言っていました", "のび太くんはきのうのテストが簡単だったと言っていました"],
        "grammarRule": "② Tính từ đuôi な quá khứ trước 「と」: かんたんでした ➔ <b>かんたんだった</b>! Chủ ngữ trong lời trích dẫn dùng trợ từ 「が」 (テストが).",
        "breakdown": "のびたくんは + きのうの テストが (bài kiểm tra hôm qua) + かんたんだった (đã đơn giản) + と いって いました.",
        "traps": [{"regex": "かんたんでしたと|かんたんだと|かんたんなった", "why": "ĐÃ đơn giản (quá khứ của tính từ な): かんたんでした ➔ thể thông thường là 「かんたんだった」 + と いって いました!"}]
    },
    {
        "id": "s18_09", "lesson": "A2-18", "category": "ÔN TẬP L18 ② と いって いました",
        "pattern": "Gのなかで Nが いちばん ～と いって いました",
        "vi": "Doraemon đã nói rằng, trong các loại bánh kẹo, dorayaki là ngon nhất.",
        "hira": "ドラえもんは、おかしの なかで どらやきが いちばん おいしいと いって いました。",
        "acceptedHira": [
            "ドラえもんは、おかしのなかでどらやきがいちばんおいしいといっていました",
            "ドラえもんは、おかしでどらやきがいちばんおいしいといっていました",
            "どらえもんは、おかしのなかでどらやきがいちばんおいしいといっていました",
            "どらえもんは、おかしでどらやきがいちばんおいしいといっていました"
        ],
        "kanjiModel": "ドラえもんは、おかし（の中）で どらやきがいちばんおいしいと言っていました。",
        "kanjiAccepted": ["ドラえもんはおかしの中でどらやきがいちばんおいしいと言っていました", "ドラえもんはおかしでどらやきがいちばんおいしいと言っていました"],
        "grammarRule": "② So sánh nhất: <b>G(の中)で Nが いちばん ～です ➔ ふつうけい ＋ と いって いました</b>. Tính từ い 「おいしい」 bỏ です đứng thẳng trước 「と」.",
        "breakdown": "ドラえもんは + おかし(のなか)で (trong các loại bánh kẹo) + どらやきが いちばん おいしい + と いって いました.",
        "traps": [{"regex": "おいしいだと|おいしいですと", "why": "Tính từ đuôi い 「おいしい」 không thêm 「だ」 hay 「です」 trước 「と」!"}]
    },
    {
        "id": "s18_10", "lesson": "A2-18", "category": "ÔN TẬP L18 ② と いって いました",
        "pattern": "Vた ＋ と いって いました",
        "vi": "Shizuka đã nói rằng, hôm qua đã học bài cùng Dekisugi tại thư viện.",
        "hira": "しずかさんは、きのう できすぎさんと としょかんで べんきょうしたと いって いました。",
        "acceptedHira": [
            "しずかさんは、きのうできすぎさんととしょかんでべんきょうしたといっていました",
            "しずかさんは、きのうできすぎくんととしょかんでべんきょうしたといっていました"
        ],
        "kanjiModel": "しずかさんは、きのう できすぎさんと図書館で勉強したと言っていました。",
        "kanjiAccepted": ["しずかさんはきのうできすぎさんと図書館で勉強したと言っていました", "しずかさんは、きのうできすぎさんと図書館で勉強したと言っていました"],
        "grammarRule": "② Thư viện = としょかん (hành động học tại đó ➔ としょかん<b>で</b>). Quá khứ thông thường: べんきょうしました ➔ <b>べんきょうした</b> + と いって いました.",
        "breakdown": "しずかさんは + きのう できすぎさんと としょかんで (cùng Dekisugi tại thư viện) + べんきょうした (đã học) + と いって いました.",
        "traps": [{"regex": "としょかんに|べんきょうしましたと", "why": "Nơi diễn ra hành động học tập là 「としょかんで」; chia 「べんきょうした」 trước と."}]
    },
    {
        "id": "s18_11", "lesson": "A2-18", "category": "ÔN TẬP L18 ② なんと いって いましたか",
        "pattern": "Sは なんと いって いましたか",
        "vi": "Tại giờ học hôm qua, cô giáo đã nói gì?",
        "hira": "きのうの じゅぎょうで、せんせいは なんと いって いましたか。",
        "acceptedHira": ["きのうのじゅぎょうで、せんせいはなんといっていましたか"],
        "kanjiModel": "きのうの授業で、先生はなんと言っていましたか。",
        "kanjiAccepted": ["きのうの授業で先生はなんと言っていましたか", "きのうのじゅぎょうで先生はなんと言っていましたか"],
        "grammarRule": "② Hỏi người nào đó đã nói gì: <b>Sは なんと いって いましたか</b> (dùng <b>なんと</b> = gì/thế nào, kèm trợ từ 「と」 có sẵn trong なんと!).",
        "breakdown": "きのうの じゅぎょうで (tại giờ học hôm qua) + せんせいは + なんと いって いましたか (đã nói gì?).",
        "traps": [{"regex": "なにといっていましたか|なんといいましたか", "why": "'Đã nói gì' dùng cụm chuẩn 「なんと いって いましたか」 (không dùng なにと)!"}]
    },
    {
        "id": "s18_12", "lesson": "A2-18", "category": "ÔN TẬP L18 ② と いって いました",
        "pattern": "V〈ふつうけい〉＋ と いって いました",
        "vi": "Cô giáo đã nói rằng, tuần sau không có bài kiểm tra.",
        "hira": "せんせいは、らいしゅう テストが ないと いって いました。",
        "acceptedHira": [
            "せんせいは、らいしゅうテストがないといっていました",
            "せんせいは、らいしゅうてすとがないといっていました",
            "せんせいは、らいしゅうテストがふたつあるといっていました"
        ],
        "kanjiModel": "先生は、来週テストがないと言っていました。",
        "kanjiAccepted": ["先生は来週テストがないと言っていました", "先生は、来週テストがないと言っていました"],
        "grammarRule": "② BẪY ĐỘNG TỪ 「あります」: Phủ định thông thường của 「あります」 là <b>ない</b> (KHÔNG phải あらない hay ありません!). Sau 「テストが ない」 nối thẳng với 「と いって いました」.",
        "breakdown": "せんせいは + らいしゅう (tuần sau) + テストが ない (không có bài kiểm tra) + と いって いました (đã nói rằng).",
        "traps": [{"regex": "あらない|ありませんと|ないだと", "why": "BẪY CỰC QUAN TRỌNG! Phủ định ngắn của 「あります」 luôn là 「ない」 (tuyệt đối không có あらない, và không thêm だ sau ない)!"}]
    },
    {
        "id": "s18_13", "lesson": "A2-18", "category": "ÔN TẬP L18 ① Hỏi ý kiến ～について どう思いますか",
        "pattern": "Nに ついて、どう おもいますか",
        "vi": "Bạn nghĩ thế nào về cuộc sống ở Nhật?",
        "hira": "にほんの せいかつに ついて、どう おもいますか。",
        "acceptedHira": ["にほんのせいかつについて、どうおもいますか"],
        "kanjiModel": "日本の生活について、どう思いますか。",
        "kanjiAccepted": ["日本の生活について、どう思いますか", "日本の生活についてどう思いますか", "日本のせいかつについて、どう思いますか"],
        "grammarRule": "① PDF L18: Hỏi ý kiến về chủ đề N dùng <b>Nに ついて、どう おもいますか</b> (tuyệt đối KHÔNG dùng なに おもいますか!).",
        "breakdown": "にほんの せいかつ (cuộc sống ở Nhật) + について (về vấn đề...) + どう おもいますか (bạn nghĩ thế nào?).",
        "traps": [
            {"regex": "なにおもいますか|なにとおもいますか", "why": "Hỏi ý kiến về một chủ đề luôn dùng 「どう おもいますか」 (KHÔNG dùng なにおもいますか)!"}
        ]
    },

    # ================= ÔN THÊM L11-14 (THEO PDF TỔNG HỢP L11~L18) =================
    {
        "id": "s11_01", "lesson": "A2-11", "category": "BÀI 11 ① Vて いきます",
        "pattern": "Vて いきます",
        "vi": "Tôi sẽ mua cơm hộp rồi mang đi (đến chỗ hẹn/chuyến đi).",
        "hira": "おべんとうを かって いきます。",
        "acceptedHira": ["おべんとうをかっていきます", "べんとうをかっていきます"],
        "kanjiModel": "お弁当を買っていきます。",
        "kanjiAccepted": ["お弁当を買っていきます", "お弁当を買って行きます", "おべんとうを買っていきます"],
        "grammarRule": "L11 ① <b>Vて いきます</b>: Làm hành động V xong rồi <b>đi khỏi</b> vị trí hiện tại (hoặc mua sẵn rồi mang theo đi).",
        "breakdown": "おべんとうを (cơm hộp) + かって いきます (mua rồi mang đi).",
        "traps": [
            {"regex": "かていきます|かいっていきます", "why": "かいます chia thể て là 「かって」 (có âm ngắt っ nhỏ)."}
        ]
    },
    {
        "id": "s11_02", "lesson": "A2-11", "category": "BÀI 11 ① Vて きます",
        "pattern": "Vて きます",
        "vi": "Tôi sẽ mang đồ uống đến (tiệc / chỗ hẹn).",
        "hira": "のみものを もって きます。",
        "acceptedHira": ["のみものをもってきます"],
        "kanjiModel": "飲み物を持ってきます。",
        "kanjiAccepted": ["飲み物を持ってきます", "飲み物を持って来ます"],
        "grammarRule": "L11 ① <b>Vて きます</b>: Mang thứ gì đó <b>đến/tới</b> nơi hẹn hoặc chỗ người nói. Phân biệt với 「買っていきます」(mua rồi đi).",
        "breakdown": "のみものを (đồ uống) + もって きます (cầm/mang đến).",
        "traps": [
            {"regex": "もてきます|もちてきます", "why": "もちます chia thể て là 「もって」 (âm ngắt っ nhỏ)."}
        ]
    },
    {
        "id": "s11_03", "lesson": "A2-11", "category": "BÀI 11 ② Từ để hỏi + でも いいです",
        "pattern": "いつでも いいです",
        "vi": "Lúc nào cũng được.",
        "hira": "いつでも いいです。",
        "acceptedHira": ["いつでもいいです", "いつでもいいですよ"],
        "kanjiModel": "いつでもいいです。",
        "kanjiAccepted": ["いつでもいいです", "いつでも良いです"],
        "grammarRule": "L11 ② <b>Từ để hỏi ＋ でも いいです</b>: Đưa ra sự lựa chọn thoải mái không câu nệ thời gian (いつでも = lúc nào cũng được).",
        "breakdown": "いつ (bao giờ) + でも (cũng) + いいです (được/tốt).",
        "traps": [
            {"regex": "いつでもいいだ|いつもいいです", "why": "「いつも」 là 'luôn luôn'; còn 'lúc nào cũng được' là 「いつでも いいです」!"}
        ]
    },
    {
        "id": "s11_04", "lesson": "A2-11", "category": "BÀI 11 ② Từ để hỏi + でも いいです",
        "pattern": "どこでも いいです",
        "vi": "Ở đâu cũng được.",
        "hira": "どこでも いいです。",
        "acceptedHira": ["どこでもいいです", "どこでもいいですよ"],
        "kanjiModel": "どこでもいいです。",
        "kanjiAccepted": ["どこでもいいです", "何処でもいいです"],
        "grammarRule": "L11 ② <b>どこ ＋ でも いいです</b>: Địa điểm nào cũng được (chú ý どこ chứ không dùng なに hay どれ).",
        "breakdown": "どこ (ở đâu) + でも いいです (cũng được).",
        "traps": [
            {"regex": "どこもいいです|どこがいいです", "why": "Phải dùng trợ từ 「でも」 sau từ để hỏi: どこでも いいです."}
        ]
    },
    {
        "id": "s11_05", "lesson": "A2-11", "category": "BÀI 11 ② Từ để hỏi + でも いいです",
        "pattern": "なんでも いいです",
        "vi": "Cái gì cũng được.",
        "hira": "なんでも いいです。",
        "acceptedHira": ["なんでもいいです", "なんでもいいですよ"],
        "kanjiModel": "なんでもいいです。",
        "kanjiAccepted": ["なんでもいいです", "何でもいいです"],
        "grammarRule": "L11 ② BẪY ĐỌC ÂM: <b>何 + でも</b> đọc là <b>なんでも</b> (KHÔNG đọc là なにでも!).",
        "breakdown": "なん (gì) + でも いいです (cũng được).",
        "traps": [
            {"regex": "なにでもいいです", "why": "BẪY PHÁT ÂM QUAN TRỌNG: 何 + でも đọc chuẩn là 「なんでも いいです」 (không phải なにでも)!"}
        ]
    },
    {
        "id": "s11_06", "lesson": "A2-11", "category": "BÀI 11 ③ N1と N2と、どちらが いいですか",
        "pattern": "N1と N2と、どちらが いいですか",
        "vi": "Giữa cà phê và trà, bạn thích cái nào hơn?",
        "hira": "こーひーと おちゃと、どちらが いいですか。",
        "acceptedHira": [
            "こーひーとおちゃと、どちらがいいですか",
            "こーひーとおちゃ、どちらがいいですか",
            "コーヒーとおちゃと、どちらがいいですか"
        ],
        "kanjiModel": "コーヒーとお茶と、どちらがいいですか。",
        "kanjiAccepted": ["コーヒーとお茶と、どちらがいいですか", "コーヒーとお茶とどちらがいいですか"],
        "grammarRule": "L11 ③ Hỏi chọn 1 trong 2 thứ: <b>N1と N2と、どちらが いいですか</b> (trả lời: コーヒーが いいです).",
        "breakdown": "コーヒーと (cà phê và) + おちゃと (trà) + どちらが いいですか (cái nào tốt hơn/thích hơn?).",
        "traps": [
            {"regex": "どれがいいですか|なにがいいですか", "why": "So sánh giữa 2 thứ dùng 「どちらが いいですか」 (từ 3 thứ trở lên mới dùng どれ)!"}
        ]
    },
    {
        "id": "s12_01", "lesson": "A2-12", "category": "BÀI 12 ① Tính từ + そうです",
        "pattern": "いA(bỏ い) ＋ そうです",
        "vi": "Trông có vẻ ngon.",
        "hira": "おいしそうです。",
        "acceptedHira": ["おいしそうです", "おいしそうですね"],
        "kanjiModel": "おいしそうです。",
        "kanjiAccepted": ["おいしそうです", "美味しそうです"],
        "grammarRule": "L12 ① Diễn tả vẻ bề ngoài nhìn thấy bằng mắt: Tính từ đuôi い <b>bỏ い + そうです</b> (おいしい ➔ <b>おいしそうです</b>).",
        "breakdown": "おいし (bỏ い của おいしい) + そうです (trông có vẻ).",
        "traps": [
            {"regex": "おいしいそう", "why": "BẪY KINH ĐIỂN L12: Phải BỎ chữ 「い」 cuối tính từ! 「おいしいそう」 sai ➔ đúng là 「おいしそうです」!"}
        ]
    },
    {
        "id": "s12_02", "lesson": "A2-12", "category": "BÀI 12 ① Tính từ + そうです",
        "pattern": "いA(bỏ い) ＋ そうです",
        "vi": "Trông có vẻ cay.",
        "hira": "からそうです。",
        "acceptedHira": ["からそうです", "からそうですね"],
        "kanjiModel": "辛そうです。",
        "kanjiAccepted": ["辛そうです", "からそうです"],
        "grammarRule": "L12 ① Từ 「からい」 (cay) bỏ chữ 「い」 rồi cộng 「そうです」 ➔ <b>からそうです</b>.",
        "breakdown": "から (bỏ い của からい) + そうです (trông có vẻ cay).",
        "traps": [
            {"regex": "からいそう", "why": "Phải bỏ chữ 「い」 trước そうです ➔ 「からそうです」!"}
        ]
    },
    {
        "id": "s12_03", "lesson": "A2-12", "category": "BÀI 12 ① Tính từ な + そうです",
        "pattern": "なA(bỏ な) ＋ そうです",
        "vi": "Trông có vẻ khỏe.",
        "hira": "げんきそうです。",
        "acceptedHira": ["げんきそうです", "げんきそうですね"],
        "kanjiModel": "元気そうです。",
        "kanjiAccepted": ["元気そうです", "元気そうですね"],
        "grammarRule": "L12 ① Tính từ đuôi な bỏ な (không thêm な hay だ) + thẳng <b>そうです</b> ➔ <b>げんきそうです</b>.",
        "breakdown": "げんき (tính từ な bỏ な) + そうです (trông có vẻ khỏe).",
        "traps": [
            {"regex": "げんきなそう|げんきだそう", "why": "Tính từ đuôi な ghép thẳng với そうです, KHÔNG giữ 「な」 hay 「だ」 ➔ 「げんきそうです」!"}
        ]
    },
    {
        "id": "s12_04", "lesson": "A2-12", "category": "BÀI 12 ① Ngoại lệ いい ➔ よさそうです",
        "pattern": "いい ➔ よさそうです (Điểm dễ nhầm PDF p.19)",
        "vi": "Trông có vẻ tốt / hay đấy.",
        "hira": "よさそうです。",
        "acceptedHira": ["よさそうです", "よさそうですね"],
        "kanjiModel": "よさそうです。",
        "kanjiAccepted": ["よさそうです", "良さそうです"],
        "grammarRule": "L12 ① NGOẠI LỆ ĐẶC BIỆT TRONG PDF TRANG 19: Tính từ 「いい」 (tốt) khi ghép với そうです BẮT BUỘC đổi thành <b>よさそうです</b> (thêm chữ <b>さ</b>)! 「ない」 cũng thành なさそうです.",
        "breakdown": "よ (gốc của いい) + さ + そうです = よさそうです (trông có vẻ tốt).",
        "traps": [
            {"regex": "いいそう|いそう|よそう", "why": "BẪY ĐẶC BIỆT PDF: 「いい」 KHÔNG đổi thành いそう hay よそう mà bắt buộc thêm 「さ」 thành 「よさそうです」!"}
        ]
    },
    {
        "id": "s12_05", "lesson": "A2-12", "category": "BÀI 12 ② ～て / ～で (Nguyên nhân)",
        "pattern": "いA(bỏ い)くて、～",
        "vi": "Vì ngon nên tôi đã ăn quá nhiều.",
        "hira": "おいしくて、たべすぎました。",
        "acceptedHira": ["おいしくて、たべすぎました", "おいしくてたべすぎました"],
        "kanjiModel": "おいしくて、食べすぎました。",
        "kanjiAccepted": ["おいしくて、食べすぎました", "美味しくて、食べすぎました", "おいしくて食べすぎました"],
        "grammarRule": "L12 ② Tính từ đuôi い chỉ nguyên nhân: bỏ い + <b>くて</b> (おいしい ➔ <b>おいしくて</b>). Vế sau dùng mẫu Vます(bỏ ます) + すぎます = ăn quá nhiều.",
        "breakdown": "おいしくて (vì ngon nên) + たべすぎました (đã ăn quá nhiều).",
        "traps": [
            {"regex": "おいしいで|おいくて", "why": "おいしい đổi sang thể て chỉ nguyên nhân phải giữ chữ し: 「おいしくて」 (không phải おいしいで)!"}
        ]
    },
    {
        "id": "s12_06", "lesson": "A2-12", "category": "BÀI 12 ② ～くて (Phủ định いA)",
        "pattern": "いAくない ➔ いAくなくて、～",
        "vi": "Quán này không đắt nên tôi hay đi.",
        "hira": "この みせは たかくなくて、よく いきます。",
        "acceptedHira": ["このみせはたかくなくて、よくいきます", "このみせはたかくなくてよくいきます"],
        "kanjiModel": "この店は高くなくて、よく行きます。",
        "kanjiAccepted": ["この店は高くなくて、よく行きます", "この店は高くなくてよく行きます"],
        "grammarRule": "L12 ② BẪY PHỦ ĐỊNH: Đuôi 「～くない」 hoạt động như tính từ đuôi い, nên bỏ い + くて thành <b>たかくなくて</b>!",
        "breakdown": "この みせは (quán này) + たかくなくて (vì không đắt nên) + よく いきます (hay đi).",
        "traps": [
            {"regex": "たかくないで|たかくないて|たかくなくで", "why": "たかくない chia thể て là 「たかくなくて」 (KHÔNG phải たかくないて hay たかくないで)!"}
        ]
    },
    {
        "id": "s12_07", "lesson": "A2-12", "category": "BÀI 12 ② なA + で (Nguyên nhân)",
        "pattern": "なA ＋ で、～",
        "vi": "Khách sạn này tiện lợi nên tôi hay sử dụng.",
        "hira": "この ほてるは べんりで、よく つかいます。",
        "acceptedHira": [
            "このほてるはべんりで、よくつかいます",
            "このホテルはべんりで、よくつかいます",
            "このほてるはべんりでよくつかいます"
        ],
        "kanjiModel": "このホテルは便利で、よく使います。",
        "kanjiAccepted": ["このホテルは便利で、よく使います", "このホテルは便利でよく使います"],
        "grammarRule": "L12 ② Tính từ đuôi な chỉ nguyên nhân nối bằng <b>で</b>: べんり ➔ <b>べんりで</b>.",
        "breakdown": "この ホテルは (khách sạn này) + べんりで (vì tiện nên) + よく つかいます (hay dùng).",
        "traps": [
            {"regex": "べんりくて|べんりて|べんりなで", "why": "べんり là tính từ đuôi な ➔ thêm thẳng 「で」 thành 「べんりで」 (không dùng くて hay なで)!"}
        ]
    },
    {
        "id": "s12_08", "lesson": "A2-12", "category": "BÀI 12 ② なAじゃなくて (Nguyên nhân phủ định)",
        "pattern": "なAじゃなくて、～",
        "vi": "Xe buýt không tiện lắm nên mỗi ngày tôi đi làm bằng xe máy.",
        "hira": "ばすは あまり べんりじゃなくて、まいにち ばいくで かいしゃに いきます。",
        "acceptedHira": [
            "ばすはあまりべんりじゃなくて、まいにちばいくでかいしゃにいきます",
            "バスはあまりべんりじゃなくて、まいにちバイクでかいしゃにいきます"
        ],
        "kanjiModel": "バスはあまり便利じゃなくて、毎日バイクで会社に行きます。",
        "kanjiAccepted": ["バスはあまり便利じゃなくて、毎日バイクで会社に行きます", "バスはあまり便利じゃなくて毎日バイクで会社に行きます"],
        "grammarRule": "L12 ② Phủ định của Danh từ / Tính từ な chỉ nguyên nhân: <b>じゃない ➔ じゃなくて</b> (べんりじゃなくて).",
        "breakdown": "バスは あまり べんりじゃなくて (xe buýt không tiện lắm nên) + まいにち バイクで かいしゃに いきます.",
        "traps": [
            {"regex": "べんりじゃないで|べんりくなくて", "why": "べんり (なA) chia phủ định thể て là 「べんりじゃなくて」 (KHÔNG dùng べんりくなくて)!"}
        ]
    },
    {
        "id": "s12_09", "lesson": "A2-12", "category": "BÀI 12 ② Danh từ + で (Nguyên nhân)",
        "pattern": "N ＋ で、～",
        "vi": "Vì tắc đường nên tôi đã đến trường muộn.",
        "hira": "じゅうたいで、がっこうに おくれました。",
        "acceptedHira": ["じゅうたいで、がっこうにおくれました", "じゅうたいでがっこうにおくれました"],
        "kanjiModel": "じゅうたいで、学校におくれました。",
        "kanjiAccepted": ["じゅうたいで、学校におくれました", "渋滞で、学校に遅れました", "じゅうたいで学校に遅れました"],
        "grammarRule": "L12 ② Danh từ + <b>で</b> diễn tả nguyên nhân sự cố (tắc đường, ốm, bão...): じゅうたい<b>で</b>、おくれました (tắc đường nên bị muộn).",
        "breakdown": "じゅうたいで (vì tắc đường nên) + がっこうに おくれました (đã trễ học).",
        "traps": [
            {"regex": "じゅうたいから|じゅうたいくて|がっこうをおくれました", "why": "Dùng 「じゅうたいで」 để chỉ nguyên nhân danh từ, và động từ 'muộn' đi với trợ từ 「に」 (がっこうに おくれました)!"}
        ]
    },
    {
        "id": "s13_01", "lesson": "A2-13", "category": "BÀI 13 ① Vた ことが あります",
        "pattern": "Vた ＋ ことが あります",
        "vi": "Tôi đã từng đi Nhật Bản.",
        "hira": "にほんに いった ことが あります。",
        "acceptedHira": ["にほんにいったことがあります", "にほんへいったことがあります"],
        "kanjiModel": "日本に行ったことがあります。",
        "kanjiAccepted": ["日本に行ったことがあります", "日本へ行ったことがあります"],
        "grammarRule": "L13 ① Nói về trải nghiệm quá khứ ('đã từng làm gì'): <b>Vた ＋ ことが あります</b>. Bẫy: động từ phải chia thể <b>た</b> (いった), KHÔNG để Vる (いく)!",
        "breakdown": "にほんに (đến Nhật) + いった ことが あります (đã từng đi).",
        "traps": [
            {"regex": "いくことがあります|いきましたことがあります", "why": "BẪY L13: Diễn tả trải nghiệm 'đã từng' bắt buộc dùng thể 「Vた」 ➔ 「いった ことが あります」 (いく ことが あります mang nghĩa 'thỉnh thoảng đi')!"}
        ]
    },
    {
        "id": "s13_02", "lesson": "A2-13", "category": "BÀI 13 ① Vた ことが あります",
        "pattern": "Vた ＋ ことが あります",
        "vi": "Tôi đã từng nhìn thấy núi Phú Sĩ.",
        "hira": "ふじさんを みた ことが あります。",
        "acceptedHira": ["ふじさんをみたことがあります"],
        "kanjiModel": "ふじさんを見たことがあります。",
        "kanjiAccepted": ["ふじさんを見たことがあります", "富士山を見たことがあります"],
        "grammarRule": "L13 ① Động từ みます (nhìn thấy, Nhóm II) ➔ thể た là <b>みた</b> + ことが あります.",
        "breakdown": "ふじさんを (núi Phú Sĩ) + みた ことが あります (đã từng thấy).",
        "traps": [
            {"regex": "みることがあります|みましたことがあります", "why": "Trước 「ことが あります」 khi nói về trải nghiệm luôn dùng 「Vた」 ➔ 「みた ことが あります」!"}
        ]
    },
    {
        "id": "s13_03", "lesson": "A2-13", "category": "BÀI 13 ② Vます / Tính từ ＋ すぎます",
        "pattern": "いA(bỏ い) ＋ すぎます",
        "vi": "Món mì ramen này cay quá. Tôi đã uống rất nhiều nước.",
        "hira": "この らーめんは からすぎます。みずを たくさん のみました。",
        "acceptedHira": [
            "このらーめんはからすぎます。みずをたくさんのみました",
            "このラーメンはからすぎます。みずをたくさんのみました",
            "このらーめんはからすぎますみずをたくさんのみました",
            "このらーめんはからすぎます。たくさんみずをのみました",
            "このラーメンはからすぎます。たくさんみずをのみました",
            "このらーめんはからすぎますたくさんみずをのみました"
        ],
        "kanjiModel": "このラーメンはからすぎます。水をたくさん飲みました。",
        "kanjiAccepted": [
            "このラーメンはからすぎます。水をたくさん飲みました", "このラーメンは辛すぎます。水をたくさん飲みました",
            "このラーメンはからすぎます。たくさん水を飲みました", "このラーメンは辛すぎます。たくさん水を飲みました"
        ],
        "grammarRule": "L13 ② Mức độ thái quá ('quá mức'): Tính từ い bỏ い + <b>すぎます</b> (からい ➔ <b>からすぎます</b>).",
        "breakdown": "この ラーメンは (mì ramen này) + からすぎます (cay quá) + みずを たくさん のみました (uống nhiều nước).",
        "traps": [
            {"regex": "からいすぎます", "why": "Phải bỏ chữ 「い」 của からい trước すぎます ➔ 「からすぎます」!"}
        ]
    },
    {
        "id": "s13_04", "lesson": "A2-13", "category": "BÀI 13 ③ ～ですが、～",
        "pattern": "S1(đối lập) ですが、S2",
        "vi": "Khách sạn tuy cũ nhưng sạch đẹp.",
        "hira": "ほてるは ふるいですが、きれいです。",
        "acceptedHira": ["ほてるはふるいですが、きれいです", "ホテルはふるいですが、きれいです"],
        "kanjiModel": "ホテルは古いですが、きれいです。",
        "kanjiAccepted": ["ホテルは古いですが、きれいです", "ホテルは古いですが、綺麗です"],
        "grammarRule": "L13 ③ Nối hai vế tương phản ('tuy ... nhưng ...'): <b>Tính từ い + ですが</b> (ふるいですが、きれいです).",
        "breakdown": "ホテルは ふるいですが (khách sạn cũ nhưng) + きれいです (sạch đẹp).",
        "traps": [
            {"regex": "ふるいが|ふるいだですが", "why": "Khi dùng mẫu câu lịch sự với が ('nhưng'), ghép sau thể lịch sự です ➔ 「ふるいですが」!"}
        ]
    },
    {
        "id": "s13_05", "lesson": "A2-13", "category": "BÀI 13 ③ ～ですが、～",
        "pattern": "S1 ですが、S2",
        "vi": "Hơi đắt một chút nhưng tiện lợi.",
        "hira": "ちょっと たかいですが、べんりです。",
        "acceptedHira": ["ちょっとたかいですが、べんりです", "ちょっとたかいですがべんりです"],
        "kanjiModel": "ちょっと高いですが、便利です。",
        "kanjiAccepted": ["ちょっと高いですが、便利です", "ちょっと高いですが便利です"],
        "grammarRule": "L13 ③ Dùng trạng từ giảm nhẹ <b>ちょっと</b> + Tính từ + ですが + vế tích cực.",
        "breakdown": "ちょっと たかいですが (hơi đắt một chút nhưng) + べんりです (tiện lợi).",
        "traps": [
            {"regex": "たかいが", "why": "Sau tính từ câu lịch sự cần thêm です trước が ➔ 「たかいですが」!"}
        ]
    },
    {
        "id": "s14_01", "lesson": "A2-14", "category": "BÀI 14 ① Vて、〈Thời gian〉に なります",
        "pattern": "Vて、〈Thời gian〉に なります",
        "vi": "Từ khi đến Nhật đã được 3 năm rồi.",
        "hira": "にほんに きて、3ねんに なります。",
        "acceptedHira": [
            "にほんにきて、3ねんになります",
            "にほんにきて、さんねんになります",
            "にほんへきて、3ねんになります",
            "にほんへきて、さんねんになります"
        ],
        "kanjiModel": "日本に来て、3年になります。",
        "kanjiAccepted": ["日本に来て、3年になります", "日本に来て3年になります", "日本に来て、三年になります"],
        "grammarRule": "L14 ① Diễn tả mốc thời gian tích lũy kể từ một sự kiện: <b>Vて、〈Thời gian〉に なります</b>.",
        "breakdown": "にほんに きて (từ khi đến Nhật) + 3ねんに なります (đã thành/được 3 năm).",
        "traps": [
            {"regex": "くるて|きたで|3ねんなります", "why": "きます chia thể て là 「きて」; trước なります cần có trợ từ 「に」 (3ねんに なります)!"}
        ]
    },
    {
        "id": "s14_02", "lesson": "A2-14", "category": "BÀI 14 ① Vて、〈Thời gian〉に なります",
        "pattern": "Vて、〈Thời gian〉に なります",
        "vi": "Tôi làm việc ở công ty này đã được 2 năm rồi.",
        "hira": "この かいしゃで はたらいて、2ねんに なります。",
        "acceptedHira": [
            "このかいしゃではたらいて、2ねんになります",
            "このかいしゃではたらいて、にねんになります",
            "このかいしゃではたらいて2ねんになります"
        ],
        "kanjiModel": "この会社で働いて、2年になります。",
        "kanjiAccepted": ["この会社で働いて、2年になります", "この会社で働いて2年になります", "この会社で働いて、二年になります"],
        "grammarRule": "L14 ① Hành động 'làm việc' xảy ra tại công ty dùng trợ từ 「で」 (かいしゃで); động từ はたらきます ➔ thể て là <b>はたらいて</b>.",
        "breakdown": "この かいしゃで はたらいて (làm việc ở công ty này) + 2ねんに なります (đã được 2 năm).",
        "traps": [
            {"regex": "はたらきて|はたらって|かいしゃにはたらいて", "why": "はたらきます đuôi き chia thể て ➔ 「はたらいて」 (âm い, không phải っ); nơi làm việc dùng trợ từ 「で」!"}
        ]
    },
    {
        "id": "s14_03", "lesson": "A2-14", "category": "BÀI 14 ② Vても いいですか",
        "pattern": "Vても いいですか",
        "vi": "Tôi ngồi ở đây có được không?",
        "hira": "ここに すわっても いいですか。",
        "acceptedHira": ["ここにすわってもいいですか"],
        "kanjiModel": "ここに座ってもいいですか。",
        "kanjiAccepted": ["ここに座ってもいいですか"],
        "grammarRule": "L14 ② Xin phép lịch sự: <b>Vても いいですか</b>. Động từ すわります (ngồi, Nhóm I đuôi り) ➔ <b>すわって</b>; nơi đích gắn chỗ ngồi dùng 「に」 (ここに).",
        "breakdown": "ここに (ở đây) + すわっても いいですか (tôi ngồi có được không?).",
        "traps": [
            {"regex": "すわりても|すわて|ここで", "why": "すわります chia thể て là 「すわって」 (có っ nhỏ), vị trí ngồi đi với động từ đứng yên/đích 「ここに」!"}
        ]
    },
    {
        "id": "s14_04", "lesson": "A2-14", "category": "BÀI 14 ② Vても いいですか",
        "pattern": "Vても いいですか",
        "vi": "Tôi chụp ảnh có được không?",
        "hira": "しゃしんを とっても いいですか。",
        "acceptedHira": ["しゃしんをとってもいいですか"],
        "kanjiModel": "写真を撮ってもいいですか。",
        "kanjiAccepted": ["写真を撮ってもいいですか"],
        "grammarRule": "L14 ② とります (chụp ảnh, Nhóm I đuôi り) ➔ thể て là <b>とって</b> + も いいですか.",
        "breakdown": "しゃしんを (ảnh) + とっても いいですか (chụp có được không?).",
        "traps": [
            {"regex": "とりても|とて", "why": "とります (Nhóm I) chuyển り ➔ って: 「とっても いいですか」!"}
        ]
    },
    {
        "id": "s14_05", "lesson": "A2-14", "category": "BÀI 14 ③ Từ chối nhẹ nhàng",
        "pattern": "すみません、ちょっと…",
        "vi": "Xin lỗi, hơi (khó xử / không tiện)...",
        "hira": "すみません、ちょっと。",
        "acceptedHira": ["すみません、ちょっと", "すみません、ちょっと。", "すみませんちょっと"],
        "kanjiModel": "すみません、ちょっと…。",
        "kanjiAccepted": ["すみません、ちょっと", "すみません、ちょっと…"],
        "grammarRule": "L14 ③ Cách người Nhật từ chối khéo lời xin phép (khi câu trả lời là KHÔNG): nói lửng <b>すみません、ちょっと…</b> thay vì nói thẳng 'ダメです'.",
        "breakdown": "すみません (xin lỗi) + ちょっと… (hơi... [bất tiện nên không được đâu ạ]).",
        "traps": [
            {"regex": "すいません、だめ|いいえ、だめ", "why": "Văn hóa giao tiếp L14: Tránh nói 'ダメです', dùng câu lửng lịch sự 「すみません、ちょっと…」!"}
        ]
    },
]
