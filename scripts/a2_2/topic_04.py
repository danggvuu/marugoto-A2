# -*- coding: utf-8 -*-
"""
Topic 4: 日本まつり (Japan Festival / Lễ hội Nhật Bản)
- Lesson 7: 雨がふったら、どうしますか (What will you do if it rains?)
- Lesson 8: コンサートはもう始まりましたか (Has the concert already started?)
"""

# =============================================================================
# LESSON 7 DATA
# =============================================================================
L7_VOCAB = [
    {
        "jp": "ボランティア",
        "kana": "ボランティア",
        "kanji": "ボランティア",
        "romaji": "borantia",
        "vi": "Tình nguyện",
        "icon": "🤝"
    },
    {
        "jp": "スタッフ",
        "kana": "スタッフ",
        "kanji": "スタッフ",
        "romaji": "sutaffu",
        "vi": "Staff",
        "icon": "👔"
    },
    {
        "jp": "ボランティアスタッフ",
        "kana": "ボランティアスタッフ",
        "kanji": "ボランティアスタッフ",
        "romaji": "borantia sutaffu",
        "vi": "Tình nguyện viên",
        "icon": "🤝"
    },
    {
        "jp": "祭り",
        "kana": "まつり",
        "kanji": "祭り",
        "romaji": "matsuri",
        "vi": "Lễ hội",
        "icon": "🏮"
    },
    {
        "jp": "イベント",
        "kana": "イベント",
        "kanji": "イベント",
        "romaji": "ibento",
        "vi": "Sự kiện",
        "icon": "🎪"
    },
    {
        "jp": "会場",
        "kana": "かいじょう",
        "kanji": "会場",
        "romaji": "kaijou",
        "vi": "Hội trường, địa điểm tổ chức",
        "icon": "🏛️"
    },
    {
        "jp": "ホール",
        "kana": "ホール",
        "kanji": "ホール",
        "romaji": "ho-ru",
        "vi": "Hội trường (Hall)",
        "icon": "🎭"
    },
    {
        "jp": "広場",
        "kana": "ひろば",
        "kanji": "広場",
        "romaji": "hiroba",
        "vi": "Quảng trường",
        "icon": "🏟️"
    },
    {
        "jp": "ロビー",
        "kana": "ロビー",
        "kanji": "ロビー",
        "romaji": "robi-",
        "vi": "Đại sảnh",
        "icon": "🏨"
    },
    {
        "jp": "踊り／踊ります",
        "kana": "おどり／おどります",
        "kanji": "踊り／踊ります",
        "romaji": "odori / odorimasu",
        "vi": "Nhảy múa",
        "icon": "💃"
    },
    {
        "jp": "準備（します）",
        "kana": "じゅんび（します）",
        "kanji": "準備（します）",
        "romaji": "junbi(shimasu)",
        "vi": "Chuẩn bị",
        "icon": "📦"
    },
    {
        "jp": "片付け",
        "kana": "かたづけ",
        "kanji": "片付け",
        "romaji": "katadzuke",
        "vi": "Sắp xếp, dọn dẹp",
        "icon": "🧹"
    },
    {
        "jp": "案内（します）",
        "kana": "あんない（します）",
        "kanji": "案内（します）",
        "romaji": "annai(shimasu)",
        "vi": "Hướng dẫn",
        "icon": "💁"
    },
    {
        "jp": "撮影（します）",
        "kana": "さつえい（します）",
        "kanji": "撮影（します）",
        "romaji": "satsuei(shimasu)",
        "vi": "Quay chụp",
        "icon": "📸"
    },
    {
        "jp": "受付",
        "kana": "うけつけ",
        "kanji": "受付",
        "romaji": "uketsuke",
        "vi": "Lễ tân",
        "icon": "🛎️"
    },
    {
        "jp": "通訳",
        "kana": "つうやく",
        "kanji": "通訳",
        "romaji": "tsuuyaku",
        "vi": "Phiên, thông dịch",
        "icon": "🗣️"
    },
    {
        "jp": "司会",
        "kana": "しかい",
        "kanji": "司会",
        "romaji": "shikai",
        "vi": "MC",
        "icon": "🎤"
    },
    {
        "jp": "連絡します",
        "kana": "れんらくします",
        "kanji": "連絡します",
        "romaji": "renraku shimasu",
        "vi": "Liên lạc (người)",
        "icon": "📞"
    },
    {
        "jp": "連絡先",
        "kana": "れんらくさき",
        "kanji": "連絡先",
        "romaji": "renrakusaki",
        "vi": "Địa chỉ liên lạc",
        "icon": "📋"
    },
    {
        "jp": "担当（します）",
        "kana": "たんとう（します）",
        "kanji": "担当（します）",
        "romaji": "tantou(shimasu)",
        "vi": "Đảm nhận, phụ trách",
        "icon": "👔"
    },
    {
        "jp": "探します",
        "kana": "さがします",
        "kanji": "探します",
        "romaji": "sagashimasu",
        "vi": "Tìm kiếm (Nを探します)",
        "icon": "🔍"
    },
    {
        "jp": "始まります／始めます",
        "kana": "はじまります／はじめます",
        "kanji": "始まります／始めます",
        "romaji": "hajimarimasu / hajimemasu",
        "vi": "Bắt đầu",
        "icon": "🚀"
    },
    {
        "jp": "中止（します）",
        "kana": "ちゅうし（します）",
        "kanji": "中止（します）",
        "romaji": "chuushi(shimasu)",
        "vi": "Hủy, dừng lại",
        "icon": "🛑"
    },
    {
        "jp": "集まります",
        "kana": "あつまります",
        "kanji": "集まります",
        "romaji": "atsumarimasu",
        "vi": "Tập trung, tụ họp",
        "icon": "👥"
    },
    {
        "jp": "スピーチコンテスト",
        "kana": "スピーチコンテスト",
        "kanji": "スピーチコンテスト",
        "romaji": "supi-chi kontesuto",
        "vi": "Cuộc thi hùng biện",
        "icon": "🎙️"
    },
    {
        "jp": "頼みます",
        "kana": "たのみます",
        "kanji": "頼みます",
        "romaji": "tanomimasu",
        "vi": "Nhờ vả (Nを頼みます)",
        "icon": "🙇"
    },
    {
        "jp": "習います",
        "kana": "ならいます",
        "kanji": "習います",
        "romaji": "naraimasu",
        "vi": "Học (có người dạy, năng khiếu...)",
        "icon": "📖"
    },
    {
        "jp": "並べます",
        "kana": "ならべます",
        "kanji": "並べます",
        "romaji": "narabemasu",
        "vi": "Sắp xếp, xếp thành hàng",
        "icon": "🧱"
    },
    {
        "jp": "都合がいい",
        "kana": "つごうがいい",
        "kanji": "都合がいい",
        "romaji": "tsugou ga ii",
        "vi": "Thời gian thuận tiện, phù hợp, tiện lợi",
        "icon": "📆"
    },
    {
        "jp": "自信",
        "kana": "じしん",
        "kanji": "自信",
        "romaji": "jishin",
        "vi": "Tự tin",
        "icon": "💪"
    }
]

L7_VERBS = [
    {"masu": "ふります", "vi": "Rơi (mưa)", "te": "ふって", "form1": "ふったら (nếu mưa rơi)", "form2": "ふらない (không mưa)", "form3": "ふる"},
    {"masu": "あつまります", "vi": "Tập hợp lại", "te": "あつまって", "form1": "あつまったら (khi tập hợp xong)", "form2": "あつまりましょう (hãy tập trung lại)", "form3": "あつまる"},
    {"masu": "さそいます", "vi": "Rủ rê", "te": "さそって", "form1": "さそったら", "form2": "さそいませんか (sao không rủ...)", "form3": "さそう"},
    {"masu": "ちゅうしします", "vi": "Hủy bỏ", "te": "ちゅうしして", "form1": "ちゅうしになったら (nếu bị hủy)", "form2": "ちゅうしした", "form3": "ちゅうしする"},
    {"masu": "れんらくします", "vi": "Liên lạc", "te": "れんらくして", "form1": "れんらくしたら", "form2": "れんらくしてください (hãy liên lạc)", "form3": "れんらくする"}
]

L7_KANJI_LIST = [
    {"stt": 1, "word": "祭り", "kana": "まつり", "hv": "TẾ", "mean": "Lễ hội"},
    {"stt": 2, "word": "雨", "kana": "あめ", "hv": "VŨ", "mean": "Mưa"},
    {"stt": 3, "word": "花火", "kana": "はなび", "hv": "HOA HỎA", "mean": "Pháo hoa"},
    {"stt": 4, "word": "中止", "kana": "ちゅうし", "hv": "TRUNG CHỈ", "mean": "Hủy bỏ"},
    {"stt": 5, "word": "集合", "kana": "しゅうごう", "hv": "TẬP HỢP", "mean": "Tập trung lại"},
    {"stt": 6, "word": "場所", "kana": "ばしょ", "hv": "TRƯỜNG SỞ", "mean": "Địa điểm, nơi chốn"},
    {"stt": 7, "word": "始まる", "kana": "はじまる", "hv": "THỦY", "mean": "Bắt đầu"},
    {"stt": 8, "word": "終わる", "kana": "おわる", "hv": "CHUNG", "mean": "Kết thúc"},
    {"stt": 9, "word": "時間", "kana": "じかん", "hv": "THỜI GIAN", "mean": "Thời gian"}
]

L7_KANJI_CARDS = [
    {"char": "祭", "hv": "Tế", "strokes": 11, "kun": "まつ・る、まつり", "on": "さい", "ex": "祭り (まつり - lễ hội), 文化祭 (ぶんかさい - lễ hội văn hóa), 祭日 (さいじつ - ngày lễ)", "mnemonic": "Bàn tay (爫) dâng thịt tế (月 - nhục) lên bàn thờ thần linh (示) trong ngày Tế lễ."},
    {"char": "雨", "hv": "Vũ", "strokes": 8, "kun": "あめ、あま", "on": "う", "ex": "雨 (あめ - mưa), 大雨 (おおあめ - mưa to), 雨天 (うてん - trời mưa)", "mnemonic": "Bầu trời giăng mây che phủ, từng hạt Mưa rớt xuống tí tách (Vũ)."},
    {"char": "花", "hv": "Hoa", "strokes": 7, "kun": "はな", "on": "か、け", "ex": "花火 (はなび - pháo hoa), 花 (はな - bông hoa), 花見 (はなみ - ngắm hoa)", "mnemonic": "Cây cỏ (艹) biến hóa (化) muôn màu sắc tươi thắm thành những đóa Hoa."},
    {"char": "火", "hv": "Hỏa", "strokes": 4, "kun": "ひ", "on": "か", "ex": "花火 (はなび - pháo hoa), 火曜日 (かようび - thứ Ba), 火事 (かじ - hỏa hoạn)", "mnemonic": "Ngọn lửa bốc cháy với hai đốm than hồng bắn sang hai bên (Hỏa)."},
    {"char": "止", "hv": "Chỉ", "strokes": 4, "kun": "と・まる、と・める", "on": "し", "ex": "中止 (ちゅうし - hủy bỏ), 止まる (とまる - dừng lại), 通行止め (つうこうどめ - cấm đường)", "mnemonic": "Bàn chân bước tới vạch giới hạn thì dừng chân đứng lại (Chỉ = dừng)."},
    {"char": "集", "hv": "Tập", "strokes": 12, "kun": "あつ・まる、あつ・める", "on": "しゅう", "ex": "集合 (しゅうごう - tập hợp), 集まる (あつまる - tụ tập), 集中 (しゅうちゅう - tập trung)", "mnemonic": "Ba con chim (隹) cùng bay về đậu trên cành cây (木) là Tụ tập, Tập hợp."},
    {"char": "場", "hv": "Trường", "strokes": 12, "kun": "ば", "on": "じょう", "ex": "場所 (ばしょ - nơi chốn), 会場 (かいじょう - hội trường), 広場 (ひろば - quảng trường)", "mnemonic": "Khu đất đai (土) dưới ánh nắng chan hòa (昜 - dương) là Nơi chốn, Chiến trường."},
    {"char": "始", "hv": "Thủy", "strokes": 8, "kun": "はじ・まる、はじ・める", "on": "し", "ex": "始まる (はじまる - bắt đầu), 始発 (しはつ - chuyến tàu đầu tiên), 開始 (かいし - khai mạc)", "mnemonic": "Người phụ nữ (女) lần đầu cất tiếng (台 - thai) sinh con là Khởi đầu sự sống."},
    {"char": "終", "hv": "Chung", "strokes": 11, "kun": "お・わる、お・える", "on": "しゅう", "ex": "終わる (おわる - kết thúc), 終点 (しゅうてん - trạm cuối), 最終 (さいしゅう - sau cùng)", "mnemonic": "Dùng sợi chỉ (糸) thắt nút lại vào mùa đông lạnh giá (冬) là Kết thúc một năm."}
]

L7_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🌧️</span> 1. Câu Điều Kiện: V-たら (Nếu... / Sau khi...)</h2>
            <span class="section-tag">Dự phòng tình huống</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để giả định một tình huống có thể xảy ra trong tương lai: "Nếu trời mưa thì...?", hoặc "Sau khi đến nơi thì...".
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">[Động từ thể TA] ＋ ら、～ (Nếu... thì...)</div>
                <div class="rule-meaning">
                    • <strong>雨が ふったら:</strong> Nếu trời mưa rơi.<br>
                    • <strong>駅に 着いたら:</strong> Sau khi tới ga (hãy gọi cho tôi).<br>
                    • <strong>安かったら:</strong> Nếu rẻ (Tính từ đuôi い ➔ ～かったら).
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">雨が ふったら、花火大会は 中止に なります。</div>
                        <div class="ex-vi">Nếu trời đổ mưa thì đại hội pháo hoa sẽ bị hủy bỏ.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('雨がふったら、花火大会は中止になります')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">駅に ついたら、電話を してください。</div>
                        <div class="ex-vi">Sau khi tới nhà ga, hãy gọi điện cho tôi nhé.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('駅についたら、電話をしてください')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🎆</span> 2. Rủ Rê & Đề Xuất Đi Lễ Hội: V-ませんか & V-ましょう</h2>
            <span class="section-tag">Giao tiếp thân thiện</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • 一緒に まつりに 行きませんか。(Cùng đi lễ hội không?)<br>
                    • 浴衣を 着て 行きましょう。(Cùng mặc yukata đi nhé!)
                </div>
                <div class="rule-meaning">
                    <code>～ませんか</code>: Lời mời lịch sự, tôn trọng ý kiến đối phương.<br>
                    <code>～ましょう</code>: Lời rủ rê hào hứng hoặc đồng thuận: 「ええ、行きましょう！」.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">今週末、浅草の まつりに 一緒に 行きませんか。</div>
                        <div class="ex-vi">Cuối tuần này, cùng đi lễ hội ở Asakusa với mình không?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('今週末、浅草のまつりに一緒に行きませんか')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L7_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "あした 雨が [____]、まつりは 延期（えんき）に なります。",
        "options": ["ふったら", "ふれば", "ふると", "ふって"],
        "correct": 0,
        "explain": "Câu điều kiện nếu trời mưa: ふりました ➔ thể TA là 「ふったら」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "「土曜日の 花火大会、一緒に [____]。」 ―― 「ええ、ぜひ！」",
        "options": ["行きませんか", "行きましょう", "行った", "行かない"],
        "correct": 0,
        "explain": "Mời rủ lịch sự: V-ませんか ➔ 「行きませんか」."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "日本の 夏まつりで 夜空に 打ち上げられる 美しい 光は [____] です。",
        "options": ["はなび", "たいこ", "ゆかた", "やたい"],
        "correct": 0,
        "explain": "Pháo hoa rực rỡ bắn trên bầu trời đêm mùa hè là 「花火 (はなび)」."
    },
    {
        "id": 4,
        "category": "Ngữ pháp",
        "q": "駅の 改札口に [____]、メッセージを 送ってください。",
        "options": ["ついたら", "ついて", "つくなら", "つく"],
        "correct": 0,
        "explain": "Sau khi đến nơi (V-たら): 着きました ➔ 「着いたら (ついたら)」."
    },
    {
        "id": 5,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「祭り」 có âm Hán Việt là gì?",
        "options": ["TẾ", "SÁI", "HỢP", "TRƯỜNG"],
        "correct": 0,
        "explain": "祭り có âm Hán Việt là TẾ (lễ hội tế thần)."
    },
    {
        "id": 6,
        "category": "Từ vựng",
        "q": "夏まつりで 着る 涼しい 木綿の 着物は [____] です。",
        "options": ["ゆかた", "みずぎ", "スーツ", "コート"],
        "correct": 0,
        "explain": "Kimono mỏng mặc mùa hè đi hội là 「浴衣 (ゆかた)」."
    },
    {
        "id": 7,
        "category": "Hội thoại",
        "q": "「何時に どこで [____] か。」 ―― 「ハチ公前で 6時に しましょう。」",
        "options": ["待ち合わせます", "泊まります", "泳ぎます", "買います"],
        "correct": 0,
        "explain": "Hẹn gặp mặt ở đâu: 「待ち合わせます (まちあわせます)」."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Từ 「中止」 có nghĩa là gì?",
        "options": ["Hủy bỏ sự kiện", "Tạm dừng nghỉ ngơi", "Bắt đầu làm", "Thay đổi địa điểm"],
        "correct": 0,
        "explain": "中止 (ちゅうし - TRUNG CHỈ) nghĩa là hủy bỏ."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "大雨の ため、花火は [____] に なりました。来週 行われます。",
        "options": ["えんき", "ちゅうし", "しゅうごう", "こんざつ"],
        "correct": 0,
        "explain": "Dời sang tuần sau tức là bị hoãn lại: 「延期 (えんき)」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「集合」 đọc là gì?",
        "options": ["しゅうごう", "じゅうごう", "しゅうあい", "しゅうかい"],
        "correct": 0,
        "explain": "集合 đọc là 「しゅうごう」 (TẬP HỢP - tập trung lại một chỗ)."
    },
    {
        "id": 11,
        "category": "Từ vựng",
        "q": "まつりの 会場は 人が たくさん いて、とても [____] していました。",
        "options": ["こんざつ", "しゅうごう", "よやく", "たいけん"],
        "correct": 0,
        "explain": "Đông nghẹt người, chen chúc nhau: 「混雑 (こんざつ) していました」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「場所」 gồm 2 chữ nào?",
        "options": ["TRƯỜNG + SỞ", "ĐỊA + SỞ", "TRƯỜNG + ĐỊA", "THỊ + SỞ"],
        "correct": 0,
        "explain": "場所 gồm chữ TRƯỜNG (場) và SỞ (所) ➔ nơi chốn, vị trí."
    },
    {
        "id": 13,
        "category": "Ngữ pháp",
        "q": "時間が [____]、屋台で たこ焼きを 買いましょう。",
        "options": ["あったら", "あって", "あると", "あれば"],
        "correct": 0,
        "explain": "Nếu có thời gian: あります ➔ thể TA là 「あったら」."
    },
    {
        "id": 14,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「始まる」 có âm Hán Việt là gì?",
        "options": ["THỦY", "CHUNG", "KAI", "NGUYÊN"],
        "correct": 0,
        "explain": "始まる có âm Hán Việt là THỦY (khởi đầu, bắt đầu)."
    },
    {
        "id": 15,
        "category": "Hội thoại",
        "q": "「まつり、とても 楽しかったですね。」 ―― 「[____]」",
        "options": ["ええ、本当に よかったですね！", "いいえ、どういたしまして。", "こちらこそ、ごめんなさい。", "はじめまして。"],
        "correct": 0,
        "explain": "Đồng tình chia sẻ cảm xúc vui vẻ sau sự kiện: 「ええ、本当によかったですね！」."
    }
]


# =============================================================================
# LESSON 8 DATA
# =============================================================================
L8_VOCAB = [
    {
        "jp": "日時",
        "kana": "にちじ",
        "kanji": "日時",
        "romaji": "nichiji",
        "vi": "Ngày giờ",
        "icon": "🕒"
    },
    {
        "jp": "会場",
        "kana": "かいじょう",
        "kanji": "会場",
        "romaji": "kaijou",
        "vi": "Hội trường, địa điểm tổ chức",
        "icon": "🏛️"
    },
    {
        "jp": "入場料",
        "kana": "にゅうじょうりょう",
        "kanji": "入場料",
        "romaji": "nyuujouryou",
        "vi": "Phí vào cửa",
        "icon": "🎟️"
    },
    {
        "jp": "入場無料",
        "kana": "にゅうじょうむりょう",
        "kanji": "入場無料",
        "romaji": "nyuujou muryou",
        "vi": "Miễn phí vào",
        "icon": "🆓"
    },
    {
        "jp": "参加費",
        "kana": "さんかひ",
        "kanji": "参加費",
        "romaji": "sankahi",
        "vi": "Phí tham gia",
        "icon": "💵"
    },
    {
        "jp": "始めます／始まります",
        "kana": "はじめます／はじまります",
        "kanji": "始めます／始まります",
        "romaji": "hajimemasu / hajimarimasu",
        "vi": "Bắt đầu",
        "icon": "🚀"
    },
    {
        "jp": "終わります",
        "kana": "おわります",
        "kanji": "終わります",
        "romaji": "owarimasu",
        "vi": "Kết thúc",
        "icon": "🏁"
    },
    {
        "jp": "やります",
        "kana": "やります",
        "kanji": "やります",
        "romaji": "yarimasu",
        "vi": "Tổ chức, diễn ra",
        "icon": "🎪"
    },
    {
        "jp": "プログラム",
        "kana": "プログラム",
        "kanji": "プログラム",
        "romaji": "puroguramu",
        "vi": "Lịch trình chương trình",
        "icon": "📑"
    },
    {
        "jp": "うちわ",
        "kana": "うちわ",
        "kanji": "団扇",
        "romaji": "uchiwa",
        "vi": "Quạt giấy",
        "icon": "🪭"
    },
    {
        "jp": "広場",
        "kana": "ひろば",
        "kanji": "広場",
        "romaji": "hiroba",
        "vi": "Quảng trường",
        "icon": "🏟️"
    },
    {
        "jp": "ホール",
        "kana": "ホール",
        "kanji": "ホール",
        "romaji": "ho-ru",
        "vi": "Hội trường",
        "icon": "🎭"
    },
    {
        "jp": "デモンストレーション",
        "kana": "デモンストレーション",
        "kanji": "デモンストレーション",
        "romaji": "demonsutore-shon",
        "vi": "Biểu diễn mẫu",
        "icon": "🥋"
    },
    {
        "jp": "お願い",
        "kana": "おねがい",
        "kanji": "お願い",
        "romaji": "onegai",
        "vi": "Yêu cầu, lời nhờ vả",
        "icon": "🙏"
    },
    {
        "jp": "飲食",
        "kana": "いんしょく",
        "kanji": "飲食",
        "romaji": "inshoku",
        "vi": "Việc ăn uống",
        "icon": "🍱"
    },
    {
        "jp": "ご遠慮ください",
        "kana": "ごえんりょください",
        "kanji": "ご遠慮ください",
        "romaji": "go-enryo kudasai",
        "vi": "Xin vui lòng không N",
        "icon": "⛔"
    },
    {
        "jp": "大人",
        "kana": "おとな",
        "kanji": "大人",
        "romaji": "otona",
        "vi": "Người lớn",
        "icon": "🧑"
    },
    {
        "jp": "連絡先",
        "kana": "れんらくさき",
        "kanji": "連絡先",
        "romaji": "renrakusaki",
        "vi": "Thông tin liên lạc (SĐT, mail…)",
        "icon": "📋"
    },
    {
        "jp": "情報",
        "kana": "じょうほう",
        "kanji": "情報",
        "romaji": "jouhou",
        "vi": "Thông tin",
        "icon": "ℹ️"
    },
    {
        "jp": "本日",
        "kana": "ほんじつ",
        "kanji": "本日",
        "romaji": "honjitsu",
        "vi": "Hôm nay (trang trọng)",
        "icon": "☀️"
    },
    {
        "jp": "お忙しい中",
        "kana": "おいそがしいなか",
        "kanji": "お忙しい中",
        "romaji": "oisogashii naka",
        "vi": "Trong lúc các bạn bận rộn",
        "icon": "⌛"
    },
    {
        "jp": "おいでくださって、ありがとうございます",
        "kana": "おいでくださって、ありがとうございます",
        "kanji": "おいでくださって、ありがとうございます",
        "romaji": "oide kudasatte arigatou gozaimasu",
        "vi": "Cảm ơn các bạn đã đến sự kiện",
        "icon": "🙇"
    }
]

L8_VERBS = [
    {"masu": "ならびます", "vi": "Xếp hàng", "te": "ならんで", "form1": "もうならびました (đã xếp hàng rồi)", "form2": "まだならんでいません (chưa xếp hàng)", "form3": "ならぶ"},
    {"masu": "はじまります", "vi": "Bắt đầu", "te": "はじまって", "form1": "もうはじまりました (đã bắt đầu rồi)", "form2": "まだはじまっていません (vẫn chưa)", "form3": "はじまる"},
    {"masu": "おわります", "vi": "Kết thúc", "te": "おわって", "form1": "もうおわりました", "form2": "まだおわっていません", "form3": "おわる"},
    {"masu": "つかれます", "vi": "Mệt", "te": "つかれて", "form1": "すこしつかれました (hơi mệt)", "form2": "つかれてから (sau khi mệt)", "form3": "つかれる"},
    {"masu": "かいます", "vi": "Mua", "te": "かって", "form1": "かってから (sau khi mua xong thì...)", "form2": "もうかいました", "form3": "かう"}
]

L8_KANJI_LIST = [
    {"stt": 1, "word": "夜", "kana": "よる", "hv": "DẠ", "mean": "Ban đêm"},
    {"stt": 2, "word": "今夜", "kana": "こんや", "hv": "KIM DẠ", "mean": "Tối nay"},
    {"stt": 3, "word": "音", "kana": "おと", "hv": "ÂM", "mean": "Âm thanh"},
    {"stt": 4, "word": "音楽", "kana": "おんがく", "hv": "ÂM NHẠC", "mean": "Âm nhạc"},
    {"stt": 5, "word": "並びます", "kana": "ならびます", "hv": "TỊNH", "mean": "Xếp hàng"},
    {"stt": 6, "word": "金魚", "kana": "きんぎょ", "hv": "KIM NGƯ", "mean": "Cá vàng"},
    {"stt": 7, "word": "疲れます", "kana": "つかれます", "hv": "BÌ", "mean": "Mệt mỏi"},
    {"stt": 8, "word": "屋台", "kana": "やたい", "hv": "ỐC ĐÀI", "mean": "Quầy hàng ăn"}
]

L8_KANJI_CARDS = [
    {"char": "夜", "hv": "Dạ", "strokes": 8, "kun": "よ、よる", "on": "や", "ex": "夜 (よる - ban đêm), 今夜 (こんや - tối nay), 夜中 (よなか - nửa đêm)", "mnemonic": "Con người (亻) bước đi dưới vầng trăng khuyết và làn sương buông là Đêm tối."},
    {"char": "音", "hv": "Âm", "strokes": 9, "kun": "おと、ね", "on": "おん、いん", "ex": "音 (おと - âm thanh), 音楽 (おんがく - âm nhạc), 本音 (ほんね - thật lòng)", "mnemonic": "Cái miệng (口) cất lời (言) phát ra luồng hơi tạo thành Âm thanh."},
    {"char": "並", "hv": "Tịnh", "strokes": 8, "kun": "なら・ぶ、なら・べる", "on": "へい", "ex": "並ぶ (ならぶ - xếp hàng), 並木 (なみき - hàng cây hai bên đường)", "mnemonic": "Hai người đứng sát nhau ngay ngắn thẳng hàng (Tịnh = xếp hàng)."},
    {"char": "金", "hv": "Kim", "strokes": 8, "kun": "かね", "on": "きん、こん", "ex": "金魚 (きんぎょ - cá vàng), お金 (おかね - tiền), 金曜日 (きんようび - thứ Sáu)", "mnemonic": "Dưới mái nhà (人) chôn giấu hai thỏi vàng óng ánh trong lòng đất (土) là Kim loại."},
    {"char": "疲", "hv": "Bì", "strokes": 10, "kun": "つか・れる", "on": "ひ", "ex": "疲れる (つかれる - mệt mỏi), 疲労 (ひろう - kiệt sức/mệt mỏi)", "mnemonic": "Căn bệnh (疒 - nạch) làm da thịt (皮 - bì) xám xịt rã rời là Mệt mỏi."},
    {"char": "台", "hv": "Đài", "strokes": 5, "kun": "ー", "on": "だい、たい", "ex": "屋台 (やたい - quầy hàng), 台所 (だいどころ - gian bếp), 一台 (いちだい - một chiếc xe/máy)", "mnemonic": "Cái bục dựng bằng đá phẳng có cửa miệng (口) đặt cao lên là Lôi đài."}
]

L8_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>⏳</span> 1. Đã Làm Xong vs. Vẫn Chưa Làm: もう V-ました & まだ V-ていません</h2>
            <span class="section-tag">Tiến độ sự việc</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để hỏi xem một sự việc tại lễ hội đã bắt đầu/hoàn thành hay chưa:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • もう [Động từ thể MASTA] か。(Đã... rồi phải không?)<br>
                    ➔ はい、もう [V-ました]。<br>
                    ➔ いいえ、まだ [V-ていません]。(Vẫn chưa...)
                </div>
                <div class="rule-meaning">
                    ⭐ <strong>Lưu ý vàng:</strong> Khi trả lời phủ định cho câu hỏi 「もう～ましたか」, <strong>KHÔNG</strong> dùng 「～ませんでした」 mà phải dùng <code>「いいえ、まだ ～ていません」</code>.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">コンサートは もう 始まりましたか。</div>
                        <div class="ex-vi">Buổi hòa nhạc đã bắt đầu chưa?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('コンサートはもう始まりましたか')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">いいえ、まだ 始まっていません。あと 10分で 始まりますよ。</div>
                        <div class="ex-vi">Chưa, vẫn chưa bắt đầu đâu. Khoảng 10 phút nữa mới bắt đầu.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('いいえ、まだ始まっていません。あと10分で始まりますよ')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🐙</span> 2. Trình Tự Hành Động: V1-てから V2 (Sau khi làm V1 thì làm V2)</h2>
            <span class="section-tag">Thứ tự ưu tiên</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">[V1 thể TE] ＋ から、V2 (Làm xong V1 rồi mới làm tiếp V2)</div>
                <div class="rule-meaning">
                    Nhấn mạnh hành động 1 phải được hoàn tất xong xuôi thì hành động 2 mới diễn ra.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">たこ焼きを 買ってから、花火を 見に行きましょう。</div>
                        <div class="ex-vi">Mua bánh takoyaki xong rồi chúng mình cùng đi xem pháo hoa nhé.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('たこ焼きを買ってから、花火を見に行きましょう')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L8_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "「コンサートは もう [____] か。」 ―― 「はい、10分前に 始まりました。」",
        "options": ["始まりました", "始まります", "始まって", "始まった"],
        "correct": 0,
        "explain": "Đã bắt đầu chưa: もう ＋ V-ましたか ➔ 「始まりましたか」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "「お昼ごはんは もう 食べましたか。」 ―― 「いいえ、まだ [____]。」",
        "options": ["食べていません", "食べませんでした", "食べます", "食べた"],
        "correct": 0,
        "explain": "Trả lời 'vẫn chưa': 『いいえ、まだ V-ていません』 ➔ 「食べていません」."
    },
    {
        "id": 3,
        "category": "Ngữ pháp",
        "q": "チケットを [____] から、会場に 入ってください。",
        "options": ["買って", "買ったら", "買い", "買う"],
        "correct": 0,
        "explain": "Trình tự sau khi làm V1: V-てから ➔ 買います chuyển sang thể TE là 「買って」."
    },
    {
        "id": 4,
        "category": "Từ vựng",
        "q": "たこ焼きを 買うために、長い [____] に 並びました。",
        "options": ["ぎょうれつ", "まつり", "えんそう", "コンサート"],
        "correct": 0,
        "explain": "Xếp hàng trong hàng người đông đúc: 「行列 (ぎょうれつ)」."
    },
    {
        "id": 5,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「夜」 trong 「今夜」 đọc là gì?",
        "options": ["や", "よる", "ゆう", "ばん"],
        "correct": 0,
        "explain": "今夜 đọc là 「こんや」 (KIM DẠ - Tối nay)."
    },
    {
        "id": 6,
        "category": "Từ vựng",
        "q": "水槽の 中の 赤い 魚を 紙の ポイですくう 遊びは [____] です。",
        "options": ["きんぎょすくい", "たこやき", "やきそば", "おめん"],
        "correct": 0,
        "explain": "Trò chơi vớt cá vàng ngày hội là 「金魚すくい (きんぎょすくい)」."
    },
    {
        "id": 7,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「並ぶ」 có cách đọc Kunyomi là gì?",
        "options": ["ならぶ", "はらぶ", "えらぶ", "よらぶ"],
        "correct": 0,
        "explain": "並ぶ đọc là 「ならぶ」 (TỊNH - Xếp hàng)."
    },
    {
        "id": 8,
        "category": "Hội thoại",
        "q": "太鼓の かっこいい [____] が 遠くから 聞こえてきます。",
        "options": ["おと", "みず", "いろ", "あじ"],
        "correct": 0,
        "explain": "Tiếng trống rền vang: 「太鼓の音 (おと)」."
    },
    {
        "id": 9,
        "category": "Chữ Hán",
        "q": "Từ 「音楽」 gồm 2 chữ nào?",
        "options": ["ÂM + NHẠC", "Ý + NHẠC", "ÂM + KHẢ", "HOA + NHẠC"],
        "correct": 0,
        "explain": "音楽 gồm ÂM (音) và NHẠC/LẠC (楽) ➔ âm nhạc."
    },
    {
        "id": 10,
        "category": "Từ vựng",
        "q": "ずっと 歩いて いたので、足が [____] しまいました。",
        "options": ["つかれて", "ついた", "ならんで", "おわって"],
        "correct": 0,
        "explain": "Mỏi mệt đôi chân: 疲れます ➔ thể TE: 「つかれて」."
    },
    {
        "id": 11,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「金魚」 đọc là gì?",
        "options": ["きんぎょ", "きんさかな", "かねうお", "こんぎょ"],
        "correct": 0,
        "explain": "金魚 đọc là 「きんぎょ」 (cá vàng)."
    },
    {
        "id": 12,
        "category": "Ngữ pháp",
        "q": "太鼓の 演奏が [____] から、帰ることに しました。",
        "options": ["終わって", "終わる", "終わった", "終わりに"],
        "correct": 0,
        "explain": "Sau khi buổi diễn kết thúc: V-てから ➔ 終わります ➔ 「終わって」."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "きつねや ひょっとこの 顔の 形を した かぶり物は [____] です。",
        "options": ["おめん", "ぼうし", "ゆかた", "めがね"],
        "correct": 0,
        "explain": "Mặt nạ cáo đeo trong hội là 「お面 (おめん)」."
    },
    {
        "id": 14,
        "category": "Hội thoại",
        "q": "「ちょうど 今、花火が [____] よ！ 見て！」",
        "options": ["始まったところだ", "終わってしまった", "始まらない", "始める"],
        "correct": 0,
        "explain": "Vừa đúng lúc pháo hoa khai màn: 「始まったところだ / 始まりましたよ」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「疲」 có âm Hán Việt là gì?",
        "options": ["BÌ", "PHÁ", "BI", "THIỀM"],
        "correct": 0,
        "explain": "疲 có âm Hán Việt là BÌ (mệt mỏi, bì quyện)."
    }
]
