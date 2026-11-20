# -*- coding: utf-8 -*-
"""
Topic 2: 店で食べる (Dining Out / Ở quán ăn)
- Lesson 3: おすすめは何ですか (What do you recommend?)
- Lesson 4: どうやって食べますか (How do you eat this?)
"""

# =============================================================================
# LESSON 3 DATA
# =============================================================================
L3_VOCAB = [
    {
        "jp": "カウンター",
        "kana": "カウンター",
        "kanji": "カウンター",
        "romaji": "kaunta-",
        "vi": "Chỗ ngồi quầy",
        "icon": "🍸"
    },
    {
        "jp": "テーブル",
        "kana": "テーブル",
        "kanji": "テーブル",
        "romaji": "te-buru",
        "vi": "Bàn (ngồi cùng ghế)",
        "icon": "🪑"
    },
    {
        "jp": "ざしき",
        "kana": "ざしき",
        "kanji": "座敷",
        "romaji": "zashiki",
        "vi": "Bàn (ngồi bệt)",
        "icon": "🎎"
    },
    {
        "jp": "きつえんせき",
        "kana": "きつえんせき",
        "kanji": "喫煙席",
        "romaji": "kitsuenseki",
        "vi": "Ghế hút thuốc",
        "icon": "🚬"
    },
    {
        "jp": "きんえんせき",
        "kana": "きんえんせき",
        "kanji": "禁煙席",
        "romaji": "kin'enseki",
        "vi": "Ghế cấm hút thuốc",
        "icon": "🚭"
    },
    {
        "jp": "予約する",
        "kana": "よやくする",
        "kanji": "予約する",
        "romaji": "yoyaku suru",
        "vi": "Đặt trước, hẹn lịch",
        "icon": "📅"
    },
    {
        "jp": "注文する",
        "kana": "ちゅうもんする",
        "kanji": "注文する",
        "romaji": "chuumon suru",
        "vi": "Đặt món, gọi món",
        "icon": "📝"
    },
    {
        "jp": "寄せ鍋",
        "kana": "よせなべ",
        "kanji": "寄せ鍋",
        "romaji": "yosenabe",
        "vi": "Lẩu hải sản",
        "icon": "🍲"
    },
    {
        "jp": "和食",
        "kana": "わしょく",
        "kanji": "和食",
        "romaji": "washoku",
        "vi": "Món ăn kiểu Nhật",
        "icon": "🍱"
    },
    {
        "jp": "すき焼き",
        "kana": "すきやき",
        "kanji": "すき焼き",
        "romaji": "sukiyaki",
        "vi": "Món lẩu kiểu Nhật",
        "icon": "🥩"
    },
    {
        "jp": "栄養",
        "kana": "えいよう",
        "kanji": "栄養",
        "romaji": "eiyou",
        "vi": "Dinh dưỡng",
        "icon": "🥗"
    },
    {
        "jp": "ベジタリアン",
        "kana": "ベジタリアン",
        "kanji": "ベジタリアン",
        "romaji": "bejitarian",
        "vi": "Ăn chay",
        "icon": "🥦"
    },
    {
        "jp": "かに",
        "kana": "かに",
        "kanji": "蟹",
        "romaji": "kani",
        "vi": "Cua",
        "icon": "🦀"
    },
    {
        "jp": "えび",
        "kana": "えび",
        "kanji": "海老",
        "romaji": "ebi",
        "vi": "Tôm",
        "icon": "🦐"
    },
    {
        "jp": "ソフトドリンク",
        "kana": "ソフトドリンク",
        "kanji": "ソフトドリンク",
        "romaji": "sofuto dorinku",
        "vi": "Đồ uống nhẹ, nước ngọt",
        "icon": "🥤"
    },
    {
        "jp": "ウーロン茶",
        "kana": "ウーロンちゃ",
        "kanji": "ウーロン茶",
        "romaji": "u-roncha",
        "vi": "Trà Ô long",
        "icon": "🍵"
    },
    {
        "jp": "新鮮（な）",
        "kana": "しんせん（な）",
        "kanji": "新鮮（な）",
        "romaji": "shinsen(na)",
        "vi": "Tươi",
        "icon": "🐟"
    },
    {
        "jp": "おすすめ（の N）",
        "kana": "おすすめ",
        "kanji": "おすすめ（の N）",
        "romaji": "osusume (no N)",
        "vi": "Gợi ý, khuyến khích",
        "icon": "👍"
    },
    {
        "jp": "何名様ですか",
        "kana": "なんめいさまですか",
        "kanji": "何名様ですか",
        "romaji": "nanmei-sama desu ka",
        "vi": "Mấy vị (người) vậy ạ?",
        "icon": "👥"
    },
    {
        "jp": "お決まりですか",
        "kana": "おきまりですか",
        "kanji": "お決まりですか",
        "romaji": "okimari desu ka",
        "vi": "Quý vị quyết định chưa ạ?",
        "icon": "🛎️"
    },
    {
        "jp": "苦手（な）",
        "kana": "にがて（な）",
        "kanji": "苦手（な）",
        "romaji": "nigate(na)",
        "vi": "Kém, sợ...",
        "icon": "🙅"
    }
]

L3_VERBS = [
    {"masu": "たべます", "vi": "Ăn", "te": "たべて", "form1": "たべてみます (ăn thử)", "form2": "たべたことがある (đã từng ăn)", "form3": "たべる (thể từ điển)"},
    {"masu": "のみます", "vi": "Uống", "te": "のんで", "form1": "のんでみます (uống thử)", "form2": "のんだことがある (đã từng uống)", "form3": "のむ"},
    {"masu": "ちゅうもんします", "vi": "Gọi món", "te": "ちゅうもんして", "form1": "ちゅうもんしてみます (thử gọi món)", "form2": "ちゅうもんしたことがある", "form3": "ちゅうもんする"},
    {"masu": "えらびます", "vi": "Chọn lựa", "te": "えらんで", "form1": "えらんでみます (thử chọn)", "form2": "えらんだことがある", "form3": "えらぶ"},
    {"masu": "たのみます", "vi": "Nhờ / gọi món", "te": "たのんで", "form1": "たのんでみます (thử gọi)", "form2": "たのんだことがある", "form3": "たのむ"}
]

L3_KANJI_LIST = [
    {"stt": 1, "word": "料理", "kana": "りょうり", "hv": "LIỆU LÝ", "mean": "Món ăn, nấu nướng"},
    {"stt": 2, "word": "味", "kana": "あじ", "hv": "VỊ", "mean": "Mùi vị, hương vị"},
    {"stt": 3, "word": "意味", "kana": "いみ", "hv": "Ý VỊ", "mean": "Ý nghĩa"},
    {"stt": 4, "word": "甘い", "kana": "あまい", "hv": "CAM", "mean": "Ngọt"},
    {"stt": 5, "word": "辛い", "kana": "からい", "hv": "TÂN", "mean": "Cay"},
    {"stt": 6, "word": "苦い", "kana": "にがい", "hv": "KHỔ", "mean": "Đắng"},
    {"stt": 7, "word": "店員", "kana": "てんいん", "hv": "ĐIẾM VIÊN", "mean": "Nhân viên cửa hàng"},
    {"stt": 8, "word": "定食", "kana": "ていしょく", "hv": "ĐỊNH THỰC", "mean": "Cơm phần, suất ăn"},
    {"stt": 9, "word": "注文", "kana": "ちゅうもん", "hv": "CHÚ VĂN", "mean": "Gọi món, đặt hàng"},
    {"stt": 10, "word": "人気", "kana": "にんき", "hv": "NHÂN KHÍ", "mean": "Được mến mộ, hút khách"},
    {"stt": 11, "word": "乾杯", "kana": "かんぱい", "hv": "CAN BÔI", "mean": "Cạn ly"}
]

L3_KANJI_CARDS = [
    {"char": "味", "hv": "Vị", "strokes": 8, "kun": "あじ、あじ・わう", "on": "み", "ex": "味 (あじ - hương vị), 意味 (いみ - ý nghĩa), 興味 (きょうみ - hứng thú)", "mnemonic": "Cái miệng (口) nếm những quả còn non chưa chín (未 - vị) để cảm nhận Mùi vị."},
    {"char": "甘", "hv": "Cam", "strokes": 5, "kun": "あま・い、あま・やかす", "on": "かん", "ex": "甘い (あまい - ngọt), 甘味料 (かんみりょう - chất tạo ngọt)", "mnemonic": "Hình ảnh ngậm miếng đồ ngọt thơm ngon trong miệng (Cam = ngọt)."},
    {"char": "辛", "hv": "Tân", "strokes": 7, "kun": "から・い", "on": "しん", "ex": "辛い (からい - cay), 辛口 (からくち - vị cay / gay gắt), 辛苦 (しんく - gian khổ)", "mnemonic": "Một nét đứng đâm nhói vào đầu lưỡi tạo cảm giác cay sè xé họng (Tân)."},
    {"char": "苦", "hv": "Khổ", "strokes": 8, "kun": "にが・い", "on": "く", "ex": "苦い (にがい - đắng), 苦手 (にがて - kém/không thích), 苦労 (くろう - gian khổ)", "mnemonic": "Cây cỏ (艹) xưa cũ (古) tích tụ lâu ngày sắc thuốc uống rất Đắng (Khổ)."},
    {"char": "料", "hv": "Liệu", "strokes": 10, "kun": "ー", "on": "りょう", "ex": "料理 (りょうり - món ăn), 料金 (りょうきん - tiền cước phí), 無料 (むりょう - miễn phí)", "mnemonic": "Cân đong hạt gạo (米) bằng cái đấu (斗) để chuẩn bị Nguyên liệu."},
    {"char": "理", "hv": "Lý", "strokes": 11, "kun": "ー", "on": "り", "ex": "料理 (りょうり - món ăn), 理由 (りゆう - lý do), 地理 (ちり - địa lý)", "mnemonic": "Dùng ngọc quý (王) mài giũa thành từng đường nét có Quy lý rõ ràng."},
    {"char": "員", "hv": "Viên", "strokes": 7, "kun": "ー", "on": "いん", "ex": "店員 (てんいん - nhân viên quán), 会員 (かいいん - hội viên), 会社員 (かいしゃいん - nhân viên công ty)", "mnemonic": "Cái miệng (口) gắn với tiền bạc (貝 - vỏ sò bối) là Nhân viên phục vụ nhận lương."},
    {"char": "定", "hv": "Định", "strokes": 8, "kun": "さだ・める", "on": "てい、じょう", "ex": "定食 (ていしょく - cơm phần), 予定 (よてい - dự định), 定休日 (ていきゅうび - ngày nghỉ cố định)", "mnemonic": "Dưới mái nhà (宀) mọi người bước chân (疋) vững vàng, tâm trí Bình định."},
    {"char": "注", "hv": "Chú", "strokes": 8, "kun": "そそ・ぐ", "on": "ちゅう", "ex": "注文 (ちゅうもん - gọi món), 注意 (ちゅうい - chú ý), 注目 (ちゅうもく - chú mục)", "mnemonic": "Dòng nước (氵) rót ngay ngắn vào cây đèn cầy (主) để Chú tâm quan sát."}
]

L3_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🍵</span> 1. Thử Làm Điều Gì Đó: V-てみます (Làm thử V)</h2>
            <span class="section-tag">Trải nghiệm & Thử nghiệm</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng khi muốn thử ăn, thử uống, thử trải nghiệm một món ăn hoặc hành động mới để biết hương vị hay cảm giác ra sao.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">[Động từ thể TE] ＋ みます / みて ください / みませんか</div>
                <div class="rule-meaning">
                    • <strong>食べてみます:</strong> Tôi sẽ ăn thử xem sao.<br>
                    • <strong>飲んでみます:</strong> Tôi sẽ uống thử.<br>
                    • <strong>ぜひ 食べてみてください:</strong> Nhất định hãy ăn thử nhé (khuyên khách).
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">この ラーメンは とても 有名ですから、食べてみます。</div>
                        <div class="ex-vi">Món mì ramen này rất nổi tiếng nên tôi sẽ ăn thử xem sao.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('このラーメンはとても有名ですから、食べてみます')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">すこし 辛いですが、おいしいですよ。飲んでみませんか。</div>
                        <div class="ex-vi">Hơi cay một chút nhưng ngon lắm đấy. Bạn uống thử không?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('すこし辛いですが、おいしいですよ。飲んでみませんか')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>✨</span> 2. Nói Về Trải Nghiệm: V-た ことがあります (Đã từng / Chưa từng)</h2>
            <span class="section-tag">Kinh nghiệm quá khứ</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để hỏi hoặc kể về trải nghiệm đã từng hoặc chưa từng nếm thử một món ăn nào đó trong đời.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • [Động từ thể TA] ＋ ことがあります (Đã từng...)<br>
                    • [Động từ thể TA] ＋ ことが ありません / 一度もありません (Chưa từng...)
                </div>
                <div class="rule-meaning">
                    ⭐ Khi hỏi: <code>V-た ことがありますか</code> ➔ Trả lời: 「はい、あります」 hoặc 「いいえ、一度も ありません」.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">納豆（なっとう）を 食べたことが ありますか。</div>
                        <div class="ex-vi">Bạn đã từng ăn món đậu tương lên men Natto chưa?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('納豆を食べたことがありますか')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">いいえ、まだ 一度も 食べたことが ありません。</div>
                        <div class="ex-vi">Chưa, tôi chưa từng ăn món đó lần nào cả.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('いいえ、まだ一度も食べたことがありません')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar3">
        <div class="section-header">
            <h2 class="section-title"><span>🍽️</span> 3. Hỏi Gợi Ý Món Ăn: おすすめは 何ですか</h2>
            <span class="section-tag">Hội thoại quán ăn</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #d97706;">
                <div class="rule-formula" style="color: #92400e;">
                    • すみません、この 店の おすすめは 何ですか。<br>
                    • ～は どんな 味（あじ）ですか。
                </div>
                <div class="rule-meaning">
                    Nhân viên thường gợi ý món đặc sản: 「～が 人気ですよ」「さっぱりしていて おいしいですよ」.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">すみません、今日のおすすめは 何ですか。</div>
                        <div class="ex-vi">Xin lỗi, hôm nay quán có món gì gợi ý ngon nhất ạ?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('すみません、今日のおすすめは何ですか')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">こちらの 刺身定食が 一番 人気がありますよ。</div>
                        <div class="ex-vi">Suất cơm cá sống Sashimi này là món được ưa chuộng nhất đấy ạ.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('こちらの刺身定食が一番人気がありますよ')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L3_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "この 日本酒（おさけ）は 初めてですから、すこし [____] みます。",
        "options": ["のんで", "のんだ", "のむ", "のみ"],
        "correct": 0,
        "explain": "Cấu trúc 'thử làm gì' là V-てみます. 飲みます chuyển sang thể TE là 「のんで」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "「馬刺し（ばさし）を [____] ことがありますか。」 ―― 「いいえ、ありません。」",
        "options": ["食べた", "食べて", "食べる", "食べ"],
        "correct": 0,
        "explain": "Hỏi về kinh nghiệm trong đời dùng cấu trúc 『V-たことがありますか』: 食べました ➔ 食べた."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "レモンは とても [____] ですが、体によいです。",
        "options": ["すっぱい", "あまい", "からい", "にがい"],
        "correct": 0,
        "explain": "Chanh (レモン) có vị chua, tiếng Nhật là 「酸っぱい (すっぱい)」."
    },
    {
        "id": 4,
        "category": "Hội thoại",
        "q": "初めての 居酒屋で、何を 頼むか 迷ったときは 店員に 「[____]」 と 聞きます。",
        "options": ["おすすめは 何ですか", "会計を お願いします", "席は どこですか", "乾杯しましょう"],
        "correct": 0,
        "explain": "Khi muốn hỏi quán có món gì ngon/đặc sắc, ta hỏi: 「おすすめは 何ですか」."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "ビールや ジュースを 持って、みんなで 「[____]！」 と 言って グラスを 合わせます。",
        "options": ["かんぱい", "ごちそうさま", "いただきます", "いらっしゃいませ"],
        "correct": 0,
        "explain": "Trước khi bắt đầu uống trong tiệc, mọi người cùng hô cạn ly: 「乾杯 (かんぱい)」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「料理」 có âm Hán Việt là gì?",
        "options": ["LIỆU LÝ", "KHOA HỌC", "VẬT LÝ", "ĐỊNH THỰC"],
        "correct": 0,
        "explain": "料理 có âm Hán Việt là LIỆU LÝ (món ăn, nấu nướng)."
    },
    {
        "id": 7,
        "category": "Từ vựng",
        "q": "この スープは 塩が 多すぎて、とても [____] です。",
        "options": ["しょっぱい", "あまい", "にがい", "すっぱい"],
        "correct": 0,
        "explain": "Nhiều muối (塩) quá thì vị mặn chát: 「しょっぱい」."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Từ 「定食」 đọc là gì?",
        "options": ["ていしょく", "じょうしょく", "だいしょく", "ていじき"],
        "correct": 0,
        "explain": "定食 đọc là 「ていしょく」 (ĐỊNH THỰC - suất cơm phần theo set)."
    },
    {
        "id": 9,
        "category": "Ngữ pháp",
        "q": "京都の お寺で 抹茶（まっちゃ）を [____] みました。すこし 苦かったです。",
        "options": ["のんで", "のむ", "のんだ", "のみ"],
        "correct": 0,
        "explain": "Thử uống nước trà: 飲んでみます, quá khứ là 飲んでみました (thể TE + みました)."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「味」 trong 「意味」 có cách đọc Onyomi là gì?",
        "options": ["み", "あじ", "まい", "び"],
        "correct": 0,
        "explain": "味 có âm On là 「み」 (trong 意味 - いみ, 興味 - きょうみ)."
    },
    {
        "id": 11,
        "category": "Từ vựng",
        "q": "ごはん、みそ汁、魚、小鉢が セットに なっている 料理を [____] と 言います。",
        "options": ["ていしょく", "デザート", "ちゅうもん", "かいけい"],
        "correct": 0,
        "explain": "Bữa ăn kèm đầy đủ cơm, canh miso, thức ăn thành phần trọn gói gọi là 「定食 (ていしょく)」."
    },
    {
        "id": 12,
        "category": "Từ vựng",
        "q": "食事が 終わったあとで、甘い アイスクリームなどの [____] を 食べます。",
        "options": ["デザート", "さしみ", "メニュー", "いざかや"],
        "correct": 0,
        "explain": "Món ngọt tráng miệng sau bữa ăn gọi là 「デザート (dessert)」."
    },
    {
        "id": 13,
        "category": "Chữ Hán",
        "q": "Từ trái nghĩa với 「甘い (あまい - ngọt)」 khi nói về vị cay nóng là chữ nào?",
        "options": ["辛い (からい)", "苦い (にがい)", "酸っぱい (すっぱい)", "塩辛い (しおからい)"],
        "correct": 0,
        "explain": "甘い (ngọt) thường được đặt đối lập với 辛い (cay / mặn nồng trong ẩm thực)."
    },
    {
        "id": 14,
        "category": "Hội thoại",
        "q": "食事代を 支払うときに、店員に 「お[____]、お願いします」 と 言います。",
        "options": ["かいけい", "ちゅうもん", "せき", "にんき"],
        "correct": 0,
        "explain": "Khi muốn thanh toán tính tiền ở quán Nhật: 「お会計（かいけい）、お願いします」."
    },
    {
        "id": 15,
        "category": "Ngữ pháp",
        "q": "富士山に [____] ことがありますか。一度 登ってみたいです。",
        "options": ["登った", "登って", "登る", "登り"],
        "correct": 0,
        "explain": "Đã từng leo núi Phú Sĩ: 登りました (のぼりました) ➔ Thể TA: 「登った」 ＋ ことがありますか."
    }
]


# =============================================================================
# LESSON 4 DATA
# =============================================================================
L4_VOCAB = [
    {
        "jp": "かけます",
        "kana": "かけます",
        "kanji": "かけます",
        "romaji": "kakemasu",
        "vi": "Rưới, chan",
        "icon": "🥣"
    },
    {
        "jp": "つけます",
        "kana": "つけます",
        "kanji": "つけます",
        "romaji": "tsukemasu",
        "vi": "Chấm",
        "icon": "🥢"
    },
    {
        "jp": "いれます",
        "kana": "いれます",
        "kanji": "入れます",
        "romaji": "iremasu",
        "vi": "Thêm vào, cho vào",
        "icon": "🫗"
    },
    {
        "jp": "ぬります",
        "kana": "ぬります",
        "kanji": "塗ります",
        "romaji": "nurimasu",
        "vi": "Bôi, sơn, phết",
        "icon": "🧈"
    },
    {
        "jp": "やきます",
        "kana": "やきます",
        "kanji": "焼きます",
        "romaji": "yakimasu",
        "vi": "Nướng",
        "icon": "🍳"
    },
    {
        "jp": "いいにおい",
        "kana": "いいにおい",
        "kanji": "いいにおい",
        "romaji": "ii nioi",
        "vi": "Mùi thơm",
        "icon": "👃"
    },
    {
        "jp": "ふた",
        "kana": "ふた",
        "kanji": "蓋",
        "romaji": "futa",
        "vi": "Nắp, vung",
        "icon": "🍲"
    },
    {
        "jp": "さら",
        "kana": "さら",
        "kanji": "皿",
        "romaji": "sara",
        "vi": "Đĩa",
        "icon": "🍽️"
    },
    {
        "jp": "ちゃわん",
        "kana": "ちゃわん",
        "kanji": "茶碗",
        "romaji": "chawan",
        "vi": "Bát",
        "icon": "🍚"
    },
    {
        "jp": "たれ／ソース",
        "kana": "たれ／ソース",
        "kanji": "たれ／ソース",
        "romaji": "tare / so-su",
        "vi": "Nước sốt",
        "icon": "🫙"
    },
    {
        "jp": "しょうゆ",
        "kana": "しょうゆ",
        "kanji": "醤油",
        "romaji": "shouyu",
        "vi": "Xì dầu",
        "icon": "🍶"
    },
    {
        "jp": "とうがらし",
        "kana": "とうがらし",
        "kanji": "唐辛子",
        "romaji": "tougarashi",
        "vi": "Ớt",
        "icon": "🌶️"
    },
    {
        "jp": "こしょう",
        "kana": "こしょう",
        "kanji": "胡椒",
        "romaji": "koshou",
        "vi": "Hạt tiêu",
        "icon": "🧂"
    },
    {
        "jp": "バター",
        "kana": "バター",
        "kanji": "バター",
        "romaji": "bata-",
        "vi": "Bơ",
        "icon": "🧈"
    },
    {
        "jp": "おなかがすきました",
        "kana": "おなかがすきました",
        "kanji": "お腹が空きました",
        "romaji": "onaka ga sukimashita",
        "vi": "Đói",
        "icon": "🤤"
    },
    {
        "jp": "のどがかわきました",
        "kana": "のどがかわきました",
        "kanji": "喉が渇きました",
        "romaji": "nodo ga kawakimashita",
        "vi": "Khát",
        "icon": "🥤"
    },
    {
        "jp": "かんぱい",
        "kana": "かんぱい",
        "kanji": "乾杯",
        "romaji": "kanpai",
        "vi": "Cạn ly",
        "icon": "🍻"
    },
    {
        "jp": "いろがかわります",
        "kana": "いろがかわります",
        "kanji": "色が変わります",
        "romaji": "iro ga kawarimasu",
        "vi": "Màu thay đổi",
        "icon": "🎨"
    },
    {
        "jp": "がまんする",
        "kana": "がまんする",
        "kanji": "我慢する",
        "romaji": "gaman suru",
        "vi": "Chịu đựng",
        "icon": "😣"
    },
    {
        "jp": "料理を残します",
        "kana": "りょうりをのこします",
        "kanji": "料理を残します",
        "romaji": "ryouri o nokoshimasu",
        "vi": "Bỏ thừa đồ ăn",
        "icon": "🍱"
    },
    {
        "jp": "音を立てます",
        "kana": "おとをたてます",
        "kanji": "音を立てます",
        "romaji": "oto o tatemasu",
        "vi": "Tạo ra âm thanh, tiếng",
        "icon": "🔊"
    },
    {
        "jp": "かゆい",
        "kana": "かゆい",
        "kanji": "痒い",
        "romaji": "kayui",
        "vi": "Ngứa",
        "icon": "😖"
    },
    {
        "jp": "汗が出ます",
        "kana": "あせがでます",
        "kanji": "汗が出ます",
        "romaji": "ase ga demasu",
        "vi": "Toát mồ hôi",
        "icon": "💦"
    }
]

L4_VERBS = [
    {"masu": "つけます", "vi": "Chấm (nước sốt)", "te": "つけて", "form1": "つけないで (xin đừng chấm)", "form2": "つけた (đã chấm)", "form3": "つける (thể từ điển)"},
    {"masu": "やきます", "vi": "Nướng", "te": "やいて", "form1": "やかないで (đừng nướng quá chín)", "form2": "やいた (đã nướng)", "form3": "やく"},
    {"masu": "にます", "vi": "Ninh / hầm", "te": "にて", "form1": "にないで", "form2": "にた", "form3": "にる"},
    {"masu": "かけます", "vi": "Rưới lên", "te": "かけて", "form1": "かけないで (đừng rưới lên)", "form2": "かけた", "form3": "かける"},
    {"masu": "のこします", "vi": "Để thừa", "te": "のこして", "form1": "のこさないで (xin đừng để thừa)", "form2": "のこした", "form3": "のこす"}
]

L4_KANJI_LIST = [
    {"stt": 1, "word": "豚肉", "kana": "ぶたにく", "hv": "ĐỒN NHỤC", "mean": "Thịt lợn"},
    {"stt": 2, "word": "牛肉", "kana": "ぎゅうにく", "hv": "NGƯU NHỤC", "mean": "Thịt bò"},
    {"stt": 3, "word": "鶏肉", "kana": "とりにく", "hv": "KÊ NHỤC", "mean": "Thịt gà"},
    {"stt": 4, "word": "魚", "kana": "さかな", "hv": "NGƯ", "mean": "Cá"},
    {"stt": 5, "word": "卵", "kana": "たまご", "hv": "NOÃN", "mean": "Trứng"},
    {"stt": 6, "word": "野菜", "kana": "やさい", "hv": "DÃ THÁI", "mean": "Rau xanh"},
    {"stt": 7, "word": "焼き鳥", "kana": "やきとり", "hv": "THIÊU ĐIỂU", "mean": "Gà nướng xiên"},
    {"stt": 8, "word": "お願い", "kana": "おねがい", "hv": "NGUYỆN", "mean": "Yêu cầu, nhờ cậy"},
    {"stt": 9, "word": "残します", "kana": "のこします", "hv": "TÀN", "mean": "Để lại, chừa lại"}
]

L4_KANJI_CARDS = [
    {"char": "肉", "hv": "Nhục", "strokes": 6, "kun": "ー", "on": "にく", "ex": "豚肉 (ぶたにく - thịt heo), 牛肉 (ぎゅうにく - thịt bò), 肉屋 (にくや - tiệm bán thịt)", "mnemonic": "Hình miếng thịt với các đường thớ gân mỡ đan chéo bên trong (Nhục)."},
    {"char": "豚", "hv": "Đồn", "strokes": 11, "kun": "ぶた", "on": "とん", "ex": "豚肉 (ぶたにく - thịt lợn), 豚骨 (とんこつ - xương heo), 子豚 (こぶた - lợn con)", "mnemonic": "Con vật ăn nhiều thịt mỡ (月 - nhục) mang hình hài loài lợn (豕 - thỉ) là Con lợn (Đồn)."},
    {"char": "牛", "hv": "Ngưu", "strokes": 4, "kun": "うし", "on": "ぎゅう", "ex": "牛肉 (ぎゅうにく - thịt bò), 牛乳 (ぎゅうにゅう - sữa bò), 子牛 (こうし - con bê)", "mnemonic": "Hình ảnh đầu con bò với hai cái sừng cong vểnh lên (Ngưu)."},
    {"char": "鳥", "hv": "Điểu", "strokes": 11, "kun": "とり", "on": "ちょう", "ex": "鳥肉 (とりにく - thịt gà/thịt chim), 焼き鳥 (やきとり - gà nướng), 小鳥 (ことり - chim nhỏ)", "mnemonic": "Hình ảnh chú chim đậu trên cành có mỏ, mắt, cánh và 4 đốm lông đuôi (Điểu)."},
    {"char": "魚", "hv": "Ngư", "strokes": 11, "kun": "さかな、うお", "on": "ぎょ", "ex": "魚 (さかな - con cá), 魚屋 (さかなや - tiệm cá), 金魚 (きんぎょ - cá vàng)", "mnemonic": "Hình ảnh con cá có đầu nhọn, thân vảy và chiếc đuôi vẫy dưới nước (Ngư)."},
    {"char": "卵", "hv": "Noãn", "strokes": 7, "kun": "たまご", "on": "らん", "ex": "卵 (たまご - quả trứng), 産卵 (さんらん - đẻ trứng)", "mnemonic": "Hai mảnh vỏ trứng đối xứng ôm lấy phôi noãn ở giữa (Noãn = trứng)."},
    {"char": "野", "hv": "Dã", "strokes": 11, "kun": "の", "on": "や", "ex": "野菜 (やさい - rau xanh), 野球 (やきゅう - bóng chày), 分野 (ぶんや - lĩnh vực)", "mnemonic": "Khu đất hoang ở thôn quê (里) nơi có thể phóng tầm mắt quan sát (予) là Đồng dã."},
    {"char": "菜", "hv": "Thái", "strokes": 11, "kun": "ー", "on": "さい", "ex": "野菜 (やさい - rau), 白菜 (はくさい - cải thảo), 総菜 (そうざい - món ăn kèm)", "mnemonic": "Cây cỏ (艹) hái bằng bàn tay (爪) từ trên cây (木) là Rau cỏ (Thái)."},
    {"char": "焼", "hv": "Thiêu", "strokes": 12, "kun": "や・く、や・ける", "on": "しょう", "ex": "焼く (やく - nướng), 焼き鳥 (やきとり - gà nướng), 夕焼け (ゆうやけ - ráng chiều đỏ rực)", "mnemonic": "Dùng ngọn lửa (火) nung đốt đất đai trên gò cao (尧) là Nướng, Thiêu đốt."}
]

L4_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🚫</span> 1. Yêu Cầu Đừng Cho Nguyên Liệu: V-ないで ください & N-抜きで</h2>
            <span class="section-tag">Dị ứng & Khẩu vị</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Khi ăn ở quán Nhật, nếu bạn bị dị ứng hoặc không ăn được nguyên liệu nào (thịt lợn, hành, wasabi), hãy dùng 2 mẫu câu chuẩn sau:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #ef4444;">
                <div class="rule-formula" style="color: #991b1b;">
                    • [Động từ thể NAI] ＋ で ください (Xin đừng...)<br>
                    • [Danh từ nguyên liệu] ＋ 抜きで お願いします (Làm ơn bỏ N ra / Không lấy N)
                </div>
                <div class="rule-meaning">
                    • <strong>豚肉（ぶたにく）抜きで お願いします:</strong> Xin đừng cho thịt lợn.<br>
                    • <strong>わさびを 入れないで ください:</strong> Xin đừng cho mù tạt vào.<br>
                    • <strong>ネギ抜きで お願いします:</strong> Cho tôi một bát không hành.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">豚肉のアレルギーが ありますから、豚肉抜きで お願いします。</div>
                        <div class="ex-vi">Tôi bị dị ứng thịt lợn, xin làm ơn làm món không có thịt lợn.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('豚肉のアレルギーがありますから、豚肉抜きでお願いします')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">辛いのが 苦手なので、唐辛子（とうがらし）を 入れないでください。</div>
                        <div class="ex-vi">Tôi ăn cay kém nên xin vui lòng đừng cho ớt vào.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('辛いのが苦手なので、唐辛子を入れないでください')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🥢</span> 2. Hỏi Và Hướng Dẫn Cách Ăn: どうやって 食べますか</h2>
            <span class="section-tag">Hướng dẫn thưởng thức</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Nhiều món ăn Nhật Bản (như mì Soba, Sushi, Lẩu Sukiyaki) có quy trình thưởng thức riêng biệt. Dùng câu này để hỏi người phục vụ hoặc bạn bè.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #0284c7;">
                <div class="rule-formula" style="color: #0369a1;">
                    • これは どうやって 食べますか。<br>
                    • [Nước sốt / Gia vị] に つけて 食べます。(Chấm vào... rồi ăn)<br>
                    • [Sốt] を かけて 食べます。(Rưới sốt lên rồi ăn)
                </div>
                <div class="rule-meaning">
                    ⭐ <strong>Phân biệt つける vs かける:</strong><br>
                    - <strong>つける (Chấm):</strong> Nhúng món ăn vào bát nước chấm nhỏ (như chấm sushi vào xì dầu).<br>
                    - <strong>かける (Rưới / chan):</strong> Đổ nước sốt trực tiếp phủ lên bề mặt món ăn.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">この 天ぷらは、こちらの つゆに つけて 食べてください。</div>
                        <div class="ex-vi">Món tempura này, xin hãy chấm vào nước chấm ở đây rồi ăn nhé.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('この天ぷらは、こちらのつゆにつけて食べてください')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">お肉を 生卵（なまたまご）に つけて 食べると、とても おいしいですよ。</div>
                        <div class="ex-vi">Thịt mà chấm vào trứng sống rồi ăn thì ngon tuyệt hảo đấy.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('お肉を生卵につけて食べると、とてもおいしいですよ')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L4_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "私は 辛いものが だめですから、わさびを [____] ください。",
        "options": ["入れないで", "入れて", "入れた", "入る"],
        "correct": 0,
        "explain": "Yêu cầu đừng cho thêm nguyên liệu vào: V-ないでください ➔ 「入れないで」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "すみません、ラーメンを ネギ [____] で お願いできますか。",
        "options": ["ぬき", "だけ", "から", "まで"],
        "correct": 0,
        "explain": "Mẫu câu yêu cầu không lấy một nguyên liệu: 『N-抜きで (ぬきで)』 ➔ ネギ抜き (không hành)."
    },
    {
        "id": 3,
        "category": "Hội thoại",
        "q": "初めて 食べる 日本料理について、食べ方の 手順を 尋ねるとき 「[____]」 と 聞きます。",
        "options": ["どうやって 食べますか", "だれと 食べますか", "いつ 食べますか", "どこで 食べますか"],
        "correct": 0,
        "explain": "Hỏi cách thức ăn một món mới: 「どうやって 食べますか」."
    },
    {
        "id": 4,
        "category": "Từ vựng",
        "q": "イスラム教（ハラール）の 友達は [____] を 食べることが できません。",
        "options": ["ぶたにく", "やさい", "たまご", "くだもの"],
        "correct": 0,
        "explain": "Người theo đạo Hồi kiêng thịt lợn: 「豚肉 (ぶたにく)」."
    },
    {
        "id": 5,
        "category": "Ngữ pháp",
        "q": "刺身（さしみ）は しょうゆに [____] 食べてください。",
        "options": ["つけて", "ついて", "かけて", "のせて"],
        "correct": 0,
        "explain": "Chấm sashimi vào nước tương xì dầu dùng động từ 「つける」 ➔ thể TE là 「つけて」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「牛肉」 đọc là gì?",
        "options": ["ぎゅうにく", "うしにく", "うまにく", "とりにく"],
        "correct": 0,
        "explain": "牛肉 đọc là 「ぎゅうにく」 (thịt bò)."
    },
    {
        "id": 7,
        "category": "Từ vựng",
        "q": "甲殻類（こうかくるい）の [____] が あるので、エビや カニは 食べられません。",
        "options": ["アレルギー", "メニュー", "デザート", "スプーン"],
        "correct": 0,
        "explain": "Dị ứng với tôm cua: 「アレルギー (dị ứng)」."
    },
    {
        "id": 8,
        "category": "Hội thoại",
        "q": "ごはんが とても おいしくて、もう 一杯 ほしいときに 「ごはんの [____]、お願いします」 と 言います。",
        "options": ["おかわり", "おかいけい", "おみやげ", "おちゅうもん"],
        "correct": 0,
        "explain": "Yêu cầu thêm một bát cơm nữa: 「おかわり」 (xới thêm / phần nữa)."
    },
    {
        "id": 9,
        "category": "Chữ Hán",
        "q": "Từ 「野菜」 có âm Hán Việt là gì?",
        "options": ["DÃ THÁI", "DÃ NGUYÊN", "ĐIỀN THÁI", "DÃ THỦY"],
        "correct": 0,
        "explain": "野菜 có âm Hán Việt là DÃ THÁI (rau củ)."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「鳥」 trong 「焼き鳥」 đọc là gì?",
        "options": ["とり", "からす", "うお", "ねこ"],
        "correct": 0,
        "explain": "鳥 đọc là 「とり」 trong 焼き鳥 (やきとり)."
    },
    {
        "id": 11,
        "category": "Từ vựng",
        "q": "スープを 飲むときは、はしではなく [____] を 使います。",
        "options": ["スプーン", "ナイフ", "フォーク", "おさら"],
        "correct": 0,
        "explain": "Uống canh, húp súp dùng muỗng/thìa: 「スプーン (spoon)」."
    },
    {
        "id": 12,
        "category": "Ngữ pháp",
        "q": "ごはんを [____] で、全部 きれいに 食べてくださいね。",
        "options": ["残さない", "残した", "残す", "残して"],
        "correct": 0,
        "explain": "Xin đừng để thừa đồ ăn: 残しません ➔ thể NAI là 「残さない」 ＋ で."
    },
    {
        "id": 13,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「卵」 có nghĩa là gì?",
        "options": ["Quả trứng", "Con gà", "Thịt lợn", "Hạt đậu"],
        "correct": 0,
        "explain": "卵 (tamago - NOÃN) có nghĩa là quả trứng."
    },
    {
        "id": 14,
        "category": "Từ vựng",
        "q": "たくさん 食べて、もう これ以上 食べられない 状態を 「お腹が [____]」 と 言います。",
        "options": ["いっぱい", "すいた", "いたい", "あいた"],
        "correct": 0,
        "explain": "No căng bụng: 「お腹がいっぱい」."
    },
    {
        "id": 15,
        "category": "Ngữ pháp",
        "q": "ソースは 上から [____] 食べても いいですか。",
        "options": ["かけて", "かって", "かつて", "かきて"],
        "correct": 0,
        "explain": "Rưới nước sốt từ trên xuống: かけます ➔ thể TE là 「かけて」."
    }
]
