# -*- coding: utf-8 -*-
"""
Topic 7: れきしと文化の町 (A Town Rich in History and Culture)
- Lesson 13: どうやって行きますか (How do I get there?)
- Lesson 14: 有名なお寺です (It's a famous temple)
"""

# =============================================================================
# LESSON 13 DATA
# =============================================================================
L13_VOCAB = [
    {
        "jp": "歴史",
        "kana": "れきし",
        "kanji": "歴史",
        "romaji": "rekishi",
        "vi": "Lịch sử",
        "icon": "📜"
    },
    {
        "jp": "文化",
        "kana": "ぶんか",
        "kanji": "文化",
        "romaji": "bunka",
        "vi": "Văn hóa",
        "icon": "🏛️"
    },
    {
        "jp": "天皇",
        "kana": "てんのう",
        "kanji": "天皇",
        "romaji": "tennou",
        "vi": "Thiên hoàng",
        "icon": "👑"
    },
    {
        "jp": "将軍",
        "kana": "しょうぐん",
        "kanji": "将軍",
        "romaji": "shougun",
        "vi": "Tướng quân",
        "icon": "🏯"
    },
    {
        "jp": "城／～城",
        "kana": "しろ／～じょう",
        "kanji": "城／～城",
        "romaji": "shiro / ~jou",
        "vi": "Thành",
        "icon": "🏯"
    },
    {
        "jp": "舞妓さん",
        "kana": "まいこさん",
        "kanji": "舞妓さん",
        "romaji": "maiko-san",
        "vi": "Thiếu nữ Maiko (vũ kỹ tập sự)",
        "icon": "👘"
    },
    {
        "jp": "約～年前",
        "kana": "やく～ねんまえ",
        "kanji": "約～年前",
        "romaji": "yaku ~nenmae",
        "vi": "Khoảng... năm trước",
        "icon": "⏳"
    },
    {
        "jp": "世紀",
        "kana": "せいき",
        "kanji": "世紀",
        "romaji": "seiki",
        "vi": "Thế kỷ",
        "icon": "⏳"
    },
    {
        "jp": "時代",
        "kana": "じだい",
        "kanji": "時代",
        "romaji": "jidai",
        "vi": "Thời đại",
        "icon": "📜"
    },
    {
        "jp": "茶道",
        "kana": "さどう",
        "kanji": "茶道",
        "romaji": "sadou",
        "vi": "Trà đạo",
        "icon": "🍵"
    },
    {
        "jp": "華道",
        "kana": "かどう",
        "kanji": "華道",
        "romaji": "kadou",
        "vi": "Nghệ thuật cắm hoa truyền thống",
        "icon": "🌸"
    },
    {
        "jp": "建てます",
        "kana": "たてます",
        "kanji": "建てます",
        "romaji": "tatemasu",
        "vi": "Xây dựng",
        "icon": "🏗️"
    },
    {
        "jp": "石",
        "kana": "いし",
        "kanji": "石",
        "romaji": "ishi",
        "vi": "Đá",
        "icon": "🪨"
    },
    {
        "jp": "仏教",
        "kana": "ぶっきょう",
        "kanji": "仏教",
        "romaji": "bukkyou",
        "vi": "Phật giáo",
        "icon": "🪷"
    },
    {
        "jp": "観光客",
        "kana": "かんこうきゃく",
        "kanji": "観光客",
        "romaji": "kankoukyaku",
        "vi": "Khách du lịch, tham quan",
        "icon": "🧳"
    },
    {
        "jp": "本物",
        "kana": "ほんもの",
        "kanji": "本物",
        "romaji": "honmono",
        "vi": "Đồ thật",
        "icon": "💎"
    },
    {
        "jp": "舞台",
        "kana": "ぶたい",
        "kanji": "舞台",
        "romaji": "butai",
        "vi": "Sân khấu",
        "icon": "🎭"
    },
    {
        "jp": "柱",
        "kana": "はしら",
        "kanji": "柱",
        "romaji": "hashira",
        "vi": "Cột",
        "icon": "🏛️"
    },
    {
        "jp": "立派",
        "kana": "りっぱ",
        "kanji": "立派",
        "romaji": "rippa",
        "vi": "Tuyệt vời, tráng lệ",
        "icon": "🏰"
    },
    {
        "jp": "～以上",
        "kana": "～いじょう",
        "kanji": "～以上",
        "romaji": "~ijou",
        "vi": "Trên... hơn...",
        "icon": "📈"
    },
    {
        "jp": "中心",
        "kana": "ちゅうしん",
        "kanji": "中心",
        "romaji": "chuushin",
        "vi": "Trung tâm",
        "icon": "🎯"
    }
]

L13_VERBS = [
    {"masu": "のります", "vi": "Lên xe / đi tàu", "te": "のって", "form1": "のってから (sau khi lên xe)", "form2": "のった (đã đi)", "form3": "のる"},
    {"masu": "おります", "vi": "Xuống xe tàu", "te": "おりて", "form1": "おりてください (xin hãy xuống ở)", "form2": "おりた", "form3": "おりる"},
    {"masu": "のりかえます", "vi": "Đổi tàu xe", "te": "のりかえて", "form1": "のりかえてください", "form2": "のりかえた", "form3": "のりかえる"},
    {"masu": "まよいます", "vi": "Lạc đường", "te": "まよって", "form1": "みちに まよってしまいました (lỡ lạc đường)", "form2": "まよった", "form3": "まよう"},
    {"masu": "つきます", "vi": "Tới nơi", "te": "ついて", "form1": "ついたら (khi tới nơi)", "form2": "ついた", "form3": "つく"}
]

L13_KANJI_LIST = [
    {"stt": 1, "word": "地下鉄", "kana": "ちかてつ", "hv": "ĐỊA HẠ THIẾT", "mean": "Tàu điện ngầm"},
    {"stt": 2, "word": "切符", "kana": "きっぷ", "hv": "THIẾT PHÙ", "mean": "Vé tàu xe"},
    {"stt": 3, "word": "改札口", "kana": "かいさつぐち", "hv": "CẢI TRÁT KHẨU", "mean": "Cổng soát vé"},
    {"stt": 4, "word": "乗ります", "kana": "のります", "hv": "THỪA", "mean": "Lên xe tàu"},
    {"stt": 5, "word": "降ります", "kana": "おります", "hv": "GIÁNG", "mean": "Xuống xe tàu"},
    {"stt": 6, "word": "乗り換え", "kana": "のりかえ", "hv": "THỪA HOÁN", "mean": "Đổi tuyến xe"},
    {"stt": 7, "word": "出発", "kana": "しゅっぱつ", "hv": "XUẤT PHÁT", "mean": "Xuất phát"},
    {"stt": 8, "word": "到着", "kana": "とうちゃく", "hv": "ĐÁO TRƯỚC", "mean": "Đến nơi"},
    {"stt": 9, "word": "遠い", "kana": "とおい", "hv": "VIỄN", "mean": "Xa"}
]

L13_KANJI_CARDS = [
    {"char": "乗", "hv": "Thừa", "strokes": 9, "kun": "の・る、の・せる", "on": "じょう", "ex": "乗る (のる - lên xe), 乗り換え (のりかえ - chuyển tuyến), 乗車券 (じょうしゃけん - vé xe)", "mnemonic": "Con người trèo lên cây (木) cao phóng tầm mắt ngắm cảnh là Cưỡi, Thừa."},
    {"char": "降", "hv": "Giáng / Hàng", "strokes": 10, "kun": "お・りる、ふ・る", "on": "こう", "ex": "降りる (おりる - xuống xe), 降る (ふる - mưa rơi), 降車 (こうしゃ - xuống xe)", "mnemonic": "Bước chân từ bậc thềm dốc (阝) đi Xuống từng nấc thang là Hạ giáng."},
    {"char": "換", "hv": "Hoán", "strokes": 12, "kun": "か・える", "on": "かん", "ex": "乗り換え (のりかえ - đổi tàu), 交換 (こうかん - hoán đổi), 換気 (かんき - thông gió)", "mnemonic": "Bàn tay (扌) gạt bỏ ngọn lửa bùng sáng (奐) để Đổi lấy làn gió mát."},
    {"char": "切", "hv": "Thiết", "strokes": 4, "kun": "き・る", "on": "せつ、さい", "ex": "切符 (きっぷ - vé), 切る (きる - cắt), 親切 (しんせつ - thân thiện/tận tình)", "mnemonic": "Cầm con dao sắc (刀) cắt số bảy (七) làm đôi là Cắt đứt, Quyết thiết."},
    {"char": "符", "hv": "Phù", "strokes": 11, "kun": "ー", "on": "ふ", "ex": "切符 (きっぷ - vé tàu xe), 符号 (ふごう - phù hiệu/ký hiệu)", "mnemonic": "Thẻ tre (竹) khắc dấu ấn chứng nhận cho người phó thác (付) là Tấm bùa, Tấm vé."},
    {"char": "改", "hv": "Cải", "strokes": 7, "kun": "あらた・める", "on": "かい", "ex": "改札口 (かいさつぐち - cổng soát vé), 改善 (かいぜん - cải thiện), 改正 (かいせい - sửa đổi)", "mnemonic": "Đứa trẻ (己) cầm roi (攵) rèn luyện sửa đổi thói hư tật xấu là Canh cải."},
    {"char": "札", "hv": "Trát", "strokes": 5, "kun": "ふだ", "on": "さつ", "ex": "改札口 (かいさつぐち - cửa soát vé), お札 (おさつ - tiền giấy), 名札 (なふだ - bảng tên)", "mnemonic": "Thanh gỗ nhỏ (木) có móc (乚) treo ghi tên tuổi phân định là Thẻ trát."},
    {"char": "遠", "hv": "Viễn", "strokes": 13, "kun": "とお・い", "on": "えん、おん", "ex": "遠い (とおい - xa xôi), 遠慮 (えんりょ - khách sáo/ngại ngùng)", "mnemonic": "Bước chân đi đường dài (辶) qua các cánh đồng bao la (袁) là Xa xôi (Viễn)."}
]

L13_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🔀</span> 1. Chỉ Dẫn Di Chuyển Tuyến: ～に乗って、～で降ります</h2>
            <span class="section-tag">Hướng dẫn đi lại</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Khi hướng dẫn khách du lịch cách đi đến một ngôi chùa cổ hay địa danh tham quan:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • [Phương tiện] に 乗って、[Ga / Trạm] で 降ります。<br>
                    • [Ga] で [Tuyến khác] に 乗り換えます。(Đổi sang tàu khác tại ga...)
                </div>
                <div class="rule-meaning">
                    • Trợ từ <strong>「に」</strong> đi với phương tiện được lên: <code>電車に 乗る</code>.<br>
                    • Trợ từ <strong>「を / で」</strong>: <code>電車を 降りる</code> (xuống khỏi tàu) / <code>京都駅で 降りる</code> (xuống tại ga Kyoto).
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">京都駅から 205番の バスに 乗って、金閣寺道で 降りてください。</div>
                        <div class="ex-vi">Từ ga Kyoto bạn hãy lên xe buýt số 205, rồi xuống ở trạm Kinkakuji-michi nhé.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('京都駅から205番のバスに乗って、金閣寺道で降りてください')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>⏱️</span> 2. Hỏi Thời Gian & Chi Phí: どのくらい かかりますか</h2>
            <span class="section-tag">Thời gian & Chi phí</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • ここから [Địa điểm] まで どのくらい かかりますか。<br>
                    ➔ 電車で 30分くらい かかります。運賃は 240円です。
                </div>
                <div class="rule-meaning">
                    Động từ <code>かかります</code> dùng cho cả tốn thời gian lẫn tốn tiền cước phí.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">歩いて どのくらい かかりますか。 ―― 徒歩 10分くらいですよ。</div>
                        <div class="ex-vi">Đi bộ mất khoảng bao lâu? ―― Đi bộ mất khoảng 10 phút thôi.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('歩いてどのくらいかかりますか。徒歩10分くらいですよ')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L13_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "ここから バス [____] 乗って、市役所前で 降りてください。",
        "options": ["に", "を", "で", "が"],
        "correct": 0,
        "explain": "Lên xe buýt dùng trợ từ に: 『バスに 乗る』."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "次の 駅で 地下鉄 [____] 乗り換えます。",
        "options": ["に", "を", "へ", "で"],
        "correct": 0,
        "explain": "Đổi sang phương tiện mới dùng trợ từ に: 『地下鉄に 乗り換える』."
    },
    {
        "id": 3,
        "category": "Hội thoại",
        "q": "「お寺まで どのくらい [____] か。」 ―― 「歩いて 15分です。」",
        "options": ["かかります", "します", "いきます", "のります"],
        "correct": 0,
        "explain": "Hỏi mất bao lâu: 「どのくらい かかりますか」."
    },
    {
        "id": 4,
        "category": "Từ vựng",
        "q": "地下を 走る 電車を [____] と 言います。",
        "options": ["ちかてつ", "新幹線", "バス", "タクシー"],
        "correct": 0,
        "explain": "Tàu điện ngầm chạy dưới lòng đất là 「地下鉄 (ちかてつ)」."
    },
    {
        "id": 5,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「切符」 có cách đọc chuẩn là gì?",
        "options": ["きっぷ", "きりふ", "せっぷ", "きっふ"],
        "correct": 0,
        "explain": "切符 đọc là 「きっぷ」 (vé tàu xe)."
    },
    {
        "id": 6,
        "category": "Từ vựng",
        "q": "駅で 切符や ICカードを タッチして 通る 改札口は [____] です。",
        "options": ["かいさつぐち", "あんないじょ", "ろせんず", "のりかえ"],
        "correct": 0,
        "explain": "Cổng soát vé nhà ga là 「改札口 (かいさつぐち)」."
    },
    {
        "id": 7,
        "category": "Chữ Hán",
        "q": "Từ 「降ります」 đối nghĩa với từ nào?",
        "options": ["乗ります (のります)", "行きます", "来ます", "帰ります"],
        "correct": 0,
        "explain": "降ります (xuống xe) đối nghĩa với 乗ります (lên xe)."
    },
    {
        "id": 8,
        "category": "Hội thoại",
        "q": "道が 分からなくなって、[____] しまいました。交番で 聞きましょう。",
        "options": ["迷って", "止まって", "始まって", "終わって"],
        "correct": 0,
        "explain": "Bị lạc đường: 迷います ➔ 「迷ってしまいました (まよって)」."
    },
    {
        "id": 9,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「遠い」 đọc là gì?",
        "options": ["とおい", "ちかい", "おそい", "はやい"],
        "correct": 0,
        "explain": "遠い đọc là 「とおい」 (VIỄN - xa xôi)."
    },
    {
        "id": 10,
        "category": "Từ vựng",
        "q": "電車や バスの 乗り方や 行き先が 描かれている 地図は [____] です。",
        "options": ["ろせんず", "ガイドブック", "手紙", "メニュー"],
        "correct": 0,
        "explain": "Sơ đồ các tuyến đường tàu xe là 「路線図 (ろせんず)」."
    },
    {
        "id": 11,
        "category": "Ngữ pháp",
        "q": "電車を [____] とき、足元に 気をつけて ください。",
        "options": ["降りる", "降りた", "降りて", "降ります"],
        "correct": 0,
        "explain": "Khi xuống khỏi tàu: 『[V thể từ điển] + とき』 ➔ 「降りるとき」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「出発」 có âm Hán Việt là gì?",
        "options": ["XUẤT PHÁT", "XUẤT PHÁP", "XUẤT HÀNH", "NHẬP PHÁT"],
        "correct": 0,
        "explain": "出発 có âm Hán Việt là XUẤT PHÁT (khởi hành)."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "車や 電車を 使わずに、自分の 足で 歩いて いくことを [____] と 言います。",
        "options": ["とほ", "のりかえ", "うんちん", "とうちゃく"],
        "correct": 0,
        "explain": "Đi bộ bằng chân là 「徒歩 (とほ)」 (ví dụ: 徒歩5分)."
    },
    {
        "id": 14,
        "category": "Hội thoại",
        "q": "駅員に 「すみません、京都寺へは [____] 行きますか」 と 尋ねました。",
        "options": ["どうやって", "だれと", "何時に", "なぜ"],
        "correct": 0,
        "explain": "Hỏi cách đi tới địa điểm: 「どうやって 行きますか」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「乗」 trong 「乗車」 có âm On là gì?",
        "options": ["じょう", "とう", "のり", "しょう"],
        "correct": 0,
        "explain": "乗 có âm On là 「じょう」 (trong 乗車 - じょうしゃ, 乗客 - じょうきゃく)."
    }
]


# =============================================================================
# LESSON 14 DATA
# =============================================================================
L14_VOCAB = [
    {
        "jp": "文化財",
        "kana": "ぶんかざい",
        "kanji": "文化財",
        "romaji": "bunkazai",
        "vi": "Di sản văn hóa",
        "icon": "🏯"
    },
    {
        "jp": "国宝",
        "kana": "こくほう",
        "kanji": "国宝",
        "romaji": "kokuhou",
        "vi": "Quốc bảo",
        "icon": "👑"
    },
    {
        "jp": "織物",
        "kana": "おりもの",
        "kanji": "織物",
        "romaji": "orimono",
        "vi": "Vải dệt, đồ dệt",
        "icon": "🧶"
    },
    {
        "jp": "道具",
        "kana": "どうぐ",
        "kanji": "道具",
        "romaji": "dougu",
        "vi": "Dụng cụ",
        "icon": "🧰"
    },
    {
        "jp": "刀",
        "kana": "かたな",
        "kanji": "刀",
        "romaji": "katana",
        "vi": "Thanh đao",
        "icon": "⚔️"
    },
    {
        "jp": "焼き物",
        "kana": "やきもの",
        "kanji": "焼き物",
        "romaji": "yakimono",
        "vi": "Đồ gốm",
        "icon": "🏺"
    },
    {
        "jp": "昔",
        "kana": "むかし",
        "kanji": "昔",
        "romaji": "mukashi",
        "vi": "Ngày xưa",
        "icon": "🕰️"
    },
    {
        "jp": "書",
        "kana": "しょ",
        "kanji": "書",
        "romaji": "sho",
        "vi": "Sách (văn tự)",
        "icon": "📜"
    },
    {
        "jp": "字",
        "kana": "じ",
        "kanji": "字",
        "romaji": "ji",
        "vi": "Chữ viết",
        "icon": "✍️"
    },
    {
        "jp": "土の人形",
        "kana": "つちのにんぎょう",
        "kanji": "土の人形",
        "romaji": "tsuchi no ningyou",
        "vi": "Búp bê đất",
        "icon": "🎎"
    },
    {
        "jp": "楽器",
        "kana": "がっき",
        "kanji": "楽器",
        "romaji": "gakki",
        "vi": "Nhạc cụ",
        "icon": "🎸"
    },
    {
        "jp": "やっぱり",
        "kana": "やっぱり",
        "kanji": "やっぱり",
        "romaji": "yappari",
        "vi": "Quả nhiên là...",
        "icon": "💡"
    },
    {
        "jp": "墓",
        "kana": "はか",
        "kanji": "墓",
        "romaji": "haka",
        "vi": "Mộ",
        "icon": "🪦"
    },
    {
        "jp": "詩",
        "kana": "うた",
        "kanji": "詩",
        "romaji": "uta",
        "vi": "Thơ",
        "icon": "📜"
    },
    {
        "jp": "恋",
        "kana": "こい",
        "kanji": "恋",
        "romaji": "koi",
        "vi": "Tình yêu",
        "icon": "❤️"
    },
    {
        "jp": "ヨーロッパ",
        "kana": "ヨーロッパ",
        "kanji": "ヨーロッパ",
        "romaji": "yo-roppa",
        "vi": "Châu Âu",
        "icon": "🌍"
    },
    {
        "jp": "輸出",
        "kana": "ゆしゅつ",
        "kanji": "輸出",
        "romaji": "yushutsu",
        "vi": "Xuất khẩu",
        "icon": "🚢"
    },
    {
        "jp": "ペルシャ",
        "kana": "ペルシャ",
        "kanji": "ペルシャ",
        "romaji": "perusha",
        "vi": "Ba Tư",
        "icon": "🕌"
    },
    {
        "jp": "じゅうたん",
        "kana": "じゅうたん",
        "kanji": "絨毯",
        "romaji": "juutan",
        "vi": "Tấm thảm",
        "icon": "🧶"
    },
    {
        "jp": "戦争",
        "kana": "せんそう",
        "kanji": "戦争",
        "romaji": "sensou",
        "vi": "Chiến tranh",
        "icon": "🛡️"
    },
    {
        "jp": "運びます",
        "kana": "はこびます",
        "kanji": "運びます",
        "romaji": "hakobimasu",
        "vi": "Vận chuyển",
        "icon": "🚚"
    },
    {
        "jp": "使用（します）",
        "kana": "しよう（します）",
        "kanji": "使用（します）",
        "romaji": "shiyou(shimasu)",
        "vi": "Sử dụng",
        "icon": "⚙️"
    },
    {
        "jp": "触ります",
        "kana": "さわります",
        "kanji": "触ります",
        "romaji": "sawarimasu",
        "vi": "Chạm, sờ",
        "icon": "✋"
    },
    {
        "jp": "ルール／規則",
        "kana": "ルール／きそく",
        "kanji": "ルール／規則",
        "romaji": "ru-ru / kisoku",
        "vi": "Quy tắc",
        "icon": "📜"
    },
    {
        "jp": "置きます",
        "kana": "おきます",
        "kanji": "置きます",
        "romaji": "okimasu",
        "vi": "Đặt, để",
        "icon": "📦"
    },
    {
        "jp": "貼ります",
        "kana": "はります",
        "kanji": "貼ります",
        "romaji": "harimasu",
        "vi": "Dán",
        "icon": "🏷️"
    },
    {
        "jp": "知らせます",
        "kana": "しらせます",
        "kanji": "知らせます",
        "romaji": "shirasemasu",
        "vi": "Thông báo",
        "icon": "📢"
    },
    {
        "jp": "ポスター",
        "kana": "ポスター",
        "kanji": "ポスター",
        "romaji": "posuta-",
        "vi": "Poster, áp phích",
        "icon": "📰"
    },
    {
        "jp": "調べます",
        "kana": "しらべます",
        "kanji": "調べます",
        "romaji": "shirabemasu",
        "vi": "Tìm hiểu, tra cứu",
        "icon": "🔍"
    },
    {
        "jp": "ロッカー",
        "kana": "ロッカー",
        "kanji": "ロッカー",
        "romaji": "rokka-",
        "vi": "Tủ locker",
        "icon": "🗄️"
    },
    {
        "jp": "カレンダー",
        "kana": "カレンダー",
        "kanji": "カレンダー",
        "romaji": "karenda-",
        "vi": "Lịch",
        "icon": "📅"
    }
]

L14_VERBS = [
    {"masu": "たてます", "vi": "Xây dựng", "te": "たてて", "form1": "たてられた (được xây dựng)", "form2": "たてた (đã xây)", "form3": "たてる"},
    {"masu": "のこります", "vi": "Còn lưu giữ", "te": "のこって", "form1": "のこっている (đang còn lưu lại)", "form2": "のこった", "form3": "のこる"},
    {"masu": "おとずれます", "vi": "Ghé thăm", "te": "おとずれて", "form1": "おとずれるひと (người ghé thăm)", "form2": "おとずれた", "form3": "おとずれる"},
    {"masu": "まもります", "vi": "Gìn giữ, bảo vệ", "te": "まもって", "form1": "まもられている (được bảo tồn)", "form2": "まもった", "form3": "まもる"},
    {"masu": "つたえます", "vi": "Truyền lại", "te": "つたえて", "form1": "つたえられている (được tương truyền)", "form2": "つたえた", "form3": "つたえる"}
]

L14_KANJI_LIST = [
    {"stt": 1, "word": "お寺", "kana": "おてら", "hv": "TỰ", "mean": "Chùa"},
    {"stt": 2, "word": "神社", "kana": "じんじゃ", "hv": "THẦN XÃ", "mean": "Đền thần đạo"},
    {"stt": 3, "word": "城", "kana": "しろ", "hv": "THÀNH", "mean": "Thành, lâu đài"},
    {"stt": 4, "word": "歴史", "kana": "れきし", "hv": "LỊCH SỬ", "mean": "Lịch sử"},
    {"stt": 5, "word": "伝統", "kana": "でんとう", "hv": "TRUYỀN THỐNG", "mean": "Truyền thống"},
    {"stt": 6, "word": "建物", "kana": "たてもの", "hv": "KIẾN VẬT", "mean": "Tòa nhà"},
    {"stt": 7, "word": "昔", "kana": "むかし", "hv": "TÍCH", "mean": "Thời xưa"},
    {"stt": 8, "word": "時代", "kana": "じだい", "hv": "THỜI ĐẠI", "mean": "Thời đại"}
]

L14_KANJI_CARDS = [
    {"char": "寺", "hv": "Tự", "strokes": 6, "kun": "てら", "on": "じ", "ex": "お寺 (おてら - ngôi chùa), 金閣寺 (きんかくじ - chùa Vàng), 東寺 (とうじ - chùa Toji)", "mnemonic": "Khu đất đai (土) có quy củ đo đếm từng tấc (寸) thanh tịnh là Ngôi chùa."},
    {"char": "社", "hv": "Xã", "strokes": 7, "kun": "やしろ", "on": "しゃ", "ex": "神社 (じんじゃ - đền Shinto), 会社 (かいしゃ - công ty), 社会 (しゃかい - xã hội)", "mnemonic": "Bàn thờ thần linh (礻) đặt trên vùng đất (土) nơi cư dân quy tụ là Đền xã."},
    {"char": "城", "hv": "Thành", "strokes": 9, "kun": "しろ", "on": "じょう", "ex": "城 (しろ - lâu đài), 大阪城 (おおさかじょう - thành Osaka), 城壁 (じょうへき - tường thành)", "mnemonic": "Đắp đất (土) kiên cố hoàn thành (成) nên bức Lâu đài, Tường thành."},
    {"char": "歴", "hv": "Lịch", "strokes": 14, "kun": "ー", "on": "れき", "ex": "歴史 (れきし - lịch sử), 履歴書 (りれきしょ - sơ yếu lý lịch)", "mnemonic": "Dưới chân vách đá sừng sững (厂) có hai hàng cây (林) trải qua muôn ngàn bước chân (止) của Lịch sử."},
    {"char": "史", "hv": "Sử", "strokes": 5, "kun": "ー", "on": "し", "ex": "歴史 (れきし - lịch sử), 世界史 (せかいし - lịch sử thế giới)", "mnemonic": "Cái miệng (口) cất lời và bàn tay cầm bút chép lại từng trang Sử xanh."},
    {"char": "伝", "hv": "Truyền", "strokes": 6, "kun": "つた・わる、つた・える", "on": "でん", "ex": "伝統 (でんとう - truyền thống), 伝える (つたえる - truyền đạt), 伝説 (でんせつ - truyền thuyết)", "mnemonic": "Con người (亻) đem cuộn chỉ (专) truyền tay nối dài từ đời này sang đời khác."},
    {"char": "統", "hv": "Thống", "strokes": 12, "kun": "す・べる", "on": "とう", "ex": "伝統 (でんとう - truyền thống), 大統領 (だいとうりょう - tổng thống), 統一 (とういつ - thống nhất)", "mnemonic": "Dùng sợi tơ (糸) gom tụ các huyết thống (充) lại thành một Hệ thống."},
    {"char": "建", "hv": "Kiến", "strokes": 9, "kun": "た・てる、た・つ", "on": "けん", "ex": "建物 (たてもの - tòa nhà), 建築 (けんちく - kiến trúc), 建設 (けんせつ - xây dựng)", "mnemonic": "Bước chân dài (廴) vung tay cầm cây bút kẻ vẽ nên bản thiết kế Xây dựng."}
]

L14_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🛕</span> 1. Bổ Nghĩa Miêu Tả Địa Danh Lịch Sử: [Mệnh đề thể thông thường] ＋ N</h2>
            <span class="section-tag">Giới thiệu di tích</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để giới thiệu câu chuyện lịch sử, kiến trúc gắn với danh lam thắng cảnh:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • 600年前に 建てられた お寺です。(Là ngôi chùa được xây dựng từ 600 năm trước)<br>
                    • 木で 作られた 古い 建物です。(Là công trình cổ được làm bằng gỗ)<br>
                    • 歴史が ある 町です。(Là thị trấn có bề dày lịch sử)
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">これは 14世紀に 足利義満に よって 建てられた 金閣寺です。</div>
                        <div class="ex-vi">Đây là Chùa Vàng Kinkaku-ji, được xây dựng bởi tướng quân Ashikaga Yoshimitsu vào thế kỷ 14.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('これは14世紀に建てられた金閣寺です')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🌸</span> 2. Tương Truyền Rằng: ～と 言われています</h2>
            <span class="section-tag">Truyền thuyết & Di tích</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">[Thể thông thường] ＋ と 言われています (Người ta tương truyền rằng / Nói rằng...)</div>
                <div class="rule-meaning">
                    Dùng để giới thiệu các truyền thuyết, ý nghĩa phong thủy hoặc sự tích của ngôi đền/chùa cổ.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">この 水を 飲むと、病気が 治ると 言われています。</div>
                        <div class="ex-vi">Tương truyền rằng uống dòng nước này thì bệnh tật sẽ tiêu tan.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('この水を飲むと、病気が治ると言われています')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L14_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "これは 400年前に [____] 古い お城です。",
        "options": ["建てられた", "建てた", "建てる", "建ち"],
        "correct": 0,
        "explain": "Được xây dựng từ 400 năm trước (thể bị động bổ nghĩa danh từ): 「建てられたお城」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "京都には、昔の 伝統が たくさん [____] 町が あります。",
        "options": ["残っている", "残った", "残る", "残して"],
        "correct": 0,
        "explain": "Thành phố đang còn lưu giữ lại nhiều truyền thống: 「残っている町」."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "赤い 鳥居（とりい）が たくさん 並んでいる 神道の 施設は [____] です。",
        "options": ["じんじゃ", "おてら", "しろ", "ていえん"],
        "correct": 0,
        "explain": "Đền thần đạo với cổng Torii màu đỏ là 「神社 (じんじゃ)」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「歴史」 có cách đọc là gì?",
        "options": ["れきし", "れきじ", "りきし", "れっし"],
        "correct": 0,
        "explain": "歴史 đọc là 「れきし」 (LỊCH SỬ)."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "秋に なると 木の 葉が 赤や 黄色に 変わる 現象を [____] と 言います。",
        "options": ["こうよう", "さくら", "まつり", "ていえん"],
        "correct": 0,
        "explain": "Lá đỏ mùa thu là 「紅葉 (こうよう / もみじ)」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「お寺」 có âm Hán Việt là gì?",
        "options": ["TỰ", "XÃ", "THÀNH", "ĐÌNH"],
        "correct": 0,
        "explain": "お寺 có âm Hán Việt là TỰ (chùa chiền)."
    },
    {
        "id": 7,
        "category": "Hội thoại",
        "q": "Chọn dạng quá khứ của すばらしい: 「京都の 街は どうでしたか。」 ―― 「古い 建物が たくさん あって、とても [____] です。」",
        "options": ["すばらしかった", "すばらしい", "すばらしくない", "すばらしく"],
        "correct": 0,
        "explain": "Tính từ い đổi い thành かった rồi thêm です: すばらしい → すばらしかったです. Không thêm でした sau かった.",
        "reviewVersion": "a22-l14-q7-past-v3"
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Từ 「建物」 gồm 2 chữ nào ghép lại?",
        "options": ["KIẾN + VẬT", "THIẾT + VẬT", "TẠO + VẬT", "KIẾN + THÀNH"],
        "correct": 0,
        "explain": "建物 gồm KIẾN (建) và VẬT (物) ➔ công trình xây dựng, tòa nhà."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "国にとって 非常に 価値が 高い 貴重な 宝物は [____] に 指定されます。",
        "options": ["こくほう", "おみやげ", "しゃしん", "ガイド"],
        "correct": 0,
        "explain": "Bảo vật quốc gia là 「国宝 (こくほう)」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「城」 đọc là gì?",
        "options": ["しろ", "まち", "むら", "いえ"],
        "correct": 0,
        "explain": "城 đọc là 「しろ」 (hoặc âm On là じょう trong 大阪城)."
    },
    {
        "id": 11,
        "category": "Ngữ pháp",
        "q": "この 神社は 平安時代に [____] と 言われています。",
        "options": ["できた", "できる", "できて", "できたら"],
        "correct": 0,
        "explain": "Tương truyền rằng đã được tạo dựng: 『V-た と言われています』 ➔ 「できたと言われています」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Từ 「伝統」 có âm Hán Việt là gì?",
        "options": ["TRUYỀN THỐNG", "TRUYỀN TỔNG", "TRUYỀN HỆ", "QUAN TRUYỀN"],
        "correct": 0,
        "explain": "伝統 có âm Hán Việt là TRUYỀN THỐNG."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "観光地を 案内して 説明して くれる 人を [____] と 呼びます。",
        "options": ["ガイド", "てんいん", "いしゃ", "さっか"],
        "correct": 0,
        "explain": "Hướng dẫn viên du lịch là 「ガイド (tour guide)」."
    },
    {
        "id": 14,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「昔」 đọc là gì?",
        "options": ["むかし", "いま", "まえ", "あした"],
        "correct": 0,
        "explain": "昔 đọc là 「むかし」 (TÍCH - ngày xưa)."
    },
    {
        "id": 15,
        "category": "Hội thoại",
        "q": "「お寺の 庭は [____] で、心が 落ち着きました。」",
        "options": ["しずか", "にぎやか", "べんり", "ふべん"],
        "correct": 0,
        "explain": "Khu vườn chùa thanh tịnh yên ả: 「静か (しずか) で」."
    }
]
