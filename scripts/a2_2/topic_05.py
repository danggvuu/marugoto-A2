# -*- coding: utf-8 -*-
"""
Topic 5: とくべつな日 (Special Days / Những ngày đặc biệt)
- Lesson 9: 来週、お祝いをしましょう (Let's celebrate next week)
- Lesson 10: どんなケーキがいいですか (What kind of cake would you like?)
"""

# =============================================================================
# LESSON 9 DATA
# =============================================================================
L9_VOCAB = [
    {"jp": "お祝い", "kana": "おいわい", "kanji": "お祝い", "romaji": "oiwai", "vi": "Lời chúc mừng, quà mừng, tiệc mừng", "icon": "🎉"},
    {"jp": "結婚", "kana": "けっこん", "kanji": "結婚", "romaji": "kekkon", "vi": "Kết hôn, cưới hỏi", "icon": "💍"},
    {"jp": "婚約", "kana": "こんやく", "kanji": "婚約", "romaji": "konyaku", "vi": "Đính hôn", "icon": "🕊️"},
    {"jp": "出産", "kana": "しゅっさん", "kanji": "出産", "romaji": "shussan", "vi": "Sinh nở, sinh em bé", "icon": "👶"},
    {"jp": "昇進", "kana": "しょうしん", "kanji": "昇進", "romaji": "shoushin", "vi": "Thăng chức, thăng tiến", "icon": "📈"},
    {"jp": "卒業", "kana": "そつぎょう", "kanji": "卒業", "romaji": "sotsugyou", "vi": "Tốt nghiệp ra trường", "icon": "🎓"},
    {"jp": "誕生日", "kana": "たんじょうび", "kanji": "誕生日", "romaji": "tanjoubi", "vi": "Ngày sinh nhật", "icon": "🎂"},
    {"jp": "プレゼント", "kana": "プレゼント", "kanji": "プレゼント", "romaji": "purezento", "vi": "Món quà tặng", "icon": "🎁"},
    {"jp": "花束", "kana": "はなたば", "kanji": "花束", "romaji": "hanataba", "vi": "Bó hoa tươi", "icon": "💐"},
    {"jp": "ネクタイ", "kana": "ネクタイ", "kanji": "ネクタイ", "romaji": "nekutai", "vi": "Cà vạt", "icon": "👔"},
    {"jp": "時計", "kana": "とけい", "kanji": "時計", "romaji": "tokei", "vi": "Đồng hồ", "icon": "⌚"},
    {"jp": "選ぶ", "kana": "えらぶ", "kanji": "選ぶ", "romaji": "erabu", "vi": "Lựa chọn, tuyển chọn", "icon": "✨"},
    {"jp": "あげる", "kana": "あげる", "kanji": "あげる", "romaji": "ageru", "vi": "Tặng, biếu (cho người khác)", "icon": "🤲"},
    {"jp": "もらう", "kana": "もらう", "kanji": "もらう", "romaji": "morau", "vi": "Nhận được từ ai", "icon": "🤝"},
    {"jp": "くれる", "kana": "くれる", "kanji": "くれる", "romaji": "kureru", "vi": "(Ai đó) tặng/cho mình", "icon": "💖"},
    {"jp": "喜ぶ", "kana": "よろこぶ", "kanji": "喜ぶ", "romaji": "yorokobu", "vi": "Vui mừng, sung sướng", "icon": "😊"},
    {"jp": "相談する", "kana": "そうだんする", "kanji": "相談する", "romaji": "soudansuru", "vi": "Thảo luận, trao đổi ý kiến", "icon": "🗣️"},
    {"jp": "参加する", "kana": "さんかする", "kanji": "参加する", "romaji": "sankasuru", "vi": "Tham gia (bữa tiệc)", "icon": "🙋‍♂️"},
    {"jp": "招待する", "kana": "しょうたいする", "kanji": "招待する", "romaji": "shoutaisuru", "vi": "Mời mọc, chiêu đãi", "icon": "💌"},
    {"jp": "乾杯する", "kana": "かんぱいする", "kanji": "乾杯する", "romaji": "kanpaisuru", "vi": "Cạn ly chúc mừng", "icon": "🥂"}
]

L9_VERBS = [
    {"masu": "あげます", "vi": "Tặng / cho", "te": "あげて", "form1": "てあげます (làm cho ai)", "form2": "あげた (đã tặng)", "form3": "あげる"},
    {"masu": "もらいます", "vi": "Nhận được", "te": "もらって", "form1": "てもらいます (được ai làm cho)", "form2": "もらった (đã nhận)", "form3": "もらう"},
    {"masu": "くれます", "vi": "(Ai) cho mình", "te": "くれて", "form1": "てくれます (ai làm giúp mình)", "form2": "くれた (đã cho mình)", "form3": "くれる"},
    {"masu": "いわいます", "vi": "Chúc mừng", "te": "いわって", "form1": "いわいましょう (cùng chúc mừng)", "form2": "いわった (đã chúc mừng)", "form3": "いわう"},
    {"masu": "よろこびます", "vi": "Vui vẻ đón nhận", "te": "よろこんで", "form1": "よろこぶでしょう (chắc sẽ vui lắm)", "form2": "よろこんだ", "form3": "よろこぶ"}
]

L9_KANJI_LIST = [
    {"stt": 1, "word": "お祝い", "kana": "おいわい", "hv": "CHÚC", "mean": "Lời chúc mừng, quà mừng"},
    {"stt": 2, "word": "結婚", "kana": "けっこん", "hv": "KẾT HÔN", "mean": "Kết hôn"},
    {"stt": 3, "word": "誕生日", "kana": "たんじょうび", "hv": "ĐẢN SINH NHẬT", "mean": "Sinh nhật"},
    {"stt": 4, "word": "出産", "kana": "しゅっさん", "hv": "XUẤT SẢN", "mean": "Sinh đẻ"},
    {"stt": 5, "word": "卒業", "kana": "そつぎょう", "hv": "TỐT NGHIỆP", "mean": "Tốt nghiệp"},
    {"stt": 6, "word": "時計", "kana": "とけい", "hv": "THỜI KẾ", "mean": "Đồng hồ"},
    {"stt": 7, "word": "参加", "kana": "さんか", "hv": "THAM GIA", "mean": "Tham gia"},
    {"stt": 8, "word": "相談", "kana": "そうだん", "hv": "TƯƠNG ĐÀM", "mean": "Bàn bạc, thảo luận"},
    {"stt": 9, "word": "花束", "kana": "はなたば", "hv": "HOA THÚC", "mean": "Bó hoa"}
]

L9_KANJI_CARDS = [
    {"char": "祝", "hv": "Chúc", "strokes": 9, "kun": "いわ・う", "on": "しゅく、しゅう", "ex": "お祝い (おいわい - chúc mừng), 祝日 (しゅくじつ - ngày quốc lễ), 祝福 (しゅくふく - chúc phúc)", "mnemonic": "Thầy tế đứng trước bàn thờ thần linh (礻) cất tiếng cầu Chúc điều lành."},
    {"char": "結", "hv": "Kết", "strokes": 12, "kun": "むす・ぶ", "on": "けつ", "ex": "結婚 (けっこん - kết hôn), 結ぶ (むすぶ - buộc lại/kết duyên), 結果 (けっか - kết quả)", "mnemonic": "Dùng sợi chỉ (糸) đan kết các điều tốt lành (吉) lại với nhau là Kết duyên."},
    {"char": "婚", "hv": "Hôn", "strokes": 11, "kun": "ー", "on": "こん", "ex": "結婚 (けっこん - kết hôn), 婚約 (こんやく - đính hôn), 新婚 (しんこん - tân hôn)", "mnemonic": "Người phụ nữ (女) đón hoàng hôn buông xuống (昏) về nhà chồng làm lễ Hôn nhân."},
    {"char": "誕", "hv": "Đản", "strokes": 15, "kun": "ー", "on": "たん", "ex": "誕生日 (たんじょうび - ngày sinh nhật), 生誕 (せいたん - giáng sinh/chào đời)", "mnemonic": "Cất lời chúc tụng (言) kéo dài trải rộng (延) chào đón em bé Đản sinh."},
    {"char": "産", "hv": "Sản", "strokes": 11, "kun": "う・む、う・まれる", "on": "さん", "ex": "出産 (しゅっさん - sinh con), お土産 (おみやげ - quà lưu niệm), 産業 (さんぎょう - ngành công nghiệp)", "mnemonic": "Đứng trên vách đá (广) trông coi việc sinh sôi mầm sống mới (Sản)."},
    {"char": "卒", "hv": "Tốt", "strokes": 8, "kun": "ー", "on": "そつ", "ex": "卒業 (そつぎょう - tốt nghiệp), 卒業生 (そつぎょうせい - cựu học sinh)", "mnemonic": "Người mặc áo lễ đính mười chữ thập tròn vẹn (十) hoàn tất việc học (Tốt)."},
    {"char": "業", "hv": "Nghiệp", "strokes": 13, "kun": "ー", "on": "ぎょう、ごう", "ex": "卒業 (そつぎょう - tốt nghiệp), 授業 (じゅぎょう - giờ học), 工業 (こうぎょう - công nghiệp)", "mnemonic": "Khung gỗ chạm trổ hình ngọn lửa treo các nhạc cụ lớn dùng làm đại Nghiệp."},
    {"char": "参", "hv": "Tham", "strokes": 8, "kun": "まい・る", "on": "さん", "ex": "参加 (さんか - tham gia), 参考 (さんこう - tham khảo)", "mnemonic": "Ba ngôi sao lấp lánh (厶) tụ hội cùng những vệt sáng là Tham gia."},
    {"char": "束", "hv": "Thúc", "strokes": 7, "kun": "たば", "on": "そく", "ex": "花束 (はなたば - bó hoa), 約束 (やくそく - lời hứa), 結束 (けっそく - đoàn kết)", "mnemonic": "Buộc chặt một sợi dây quanh khúc gỗ (木) lại thành từng Bó, từng Thúc."}
]

L9_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🎁</span> 1. Cho Nhận Trong Ngày Vui: あげる / もらう / くれる</h2>
            <span class="section-tag">Quà tặng & Ân nghĩa</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Trọn bộ 3 động từ cho nhận nền tảng trong tiếng Nhật khi tặng và nhận quà mừng:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • [Người nhận] に [Quà] を あげます (Tôi / ai đó tặng cho người khác)<br>
                    • [Người tặng] に / から [Quà] を もらいます (Tôi nhận được từ ai)<br>
                    • [Người khác] が 私に [Quà] を くれます (Ai đó tặng/cho tôi)
                </div>
                <div class="rule-meaning">
                    ⭐ <strong>Tuyệt chiêu ghi nhớ:</strong><br>
                    - <strong>あげる:</strong> Hướng từ tôi ra người ngoài.<br>
                    - <strong>くれる:</strong> Hướng từ người khác vào lòng tôi.<br>
                    - <strong>もらう:</strong> Tôi là chủ thể nhận lấy ân huệ/món quà từ người khác.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">レーさんの 結婚のお祝いに、何を あげますか。</div>
                        <div class="ex-vi">Để mừng đám cưới anh Lê, chúng mình sẽ tặng gì nhỉ?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('レーさんの結婚のお祝いに、何をあげますか')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">誕生日に 友達が すてきな 時計を くれました。</div>
                        <div class="ex-vi">Vào ngày sinh nhật, bạn bè đã tặng cho tôi một chiếc đồng hồ rất đẹp.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('誕生日に友達がすてきな時計をくれました')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🥂</span> 2. Trao Đổi Lên Kế Hoạch Tiệc Mừng (Thực Hành Slide Lớp Học)</h2>
            <span class="section-tag">Giao tiếp thực tế</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">5 Câu Hỏi Thảo Luận Lễ Kỷ Niệm Chuẩn Marugoto</div>
                <div class="rule-meaning">
                    1. <strong>レーさんの 結婚の お祝いパーティー、どうしますか。</strong> (Tiệc mừng cưới anh Lê tính sao đây?)<br>
                    2. <strong>プレゼントは 何を あげますか。</strong> (Quà tặng thì mình tặng gì?)<br>
                    3. <strong>何人 参加しますか。</strong> (Có bao nhiêu người sẽ tham gia?)<br>
                    4. <strong>どこで しますか。</strong> (Sẽ tổ chức ở đâu?)<br>
                    5. <strong>レーさんに 言いましたか。</strong> (Đã nói cho anh Lê biết chưa?)
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">来週、レーさんの 結婚のお祝いを しましょう！</div>
                        <div class="ex-vi">Tuần tới, chúng mình hãy cùng tổ chức chúc mừng đám cưới anh Lê nhé!</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('来週、レーさんの結婚のお祝いをしましょう')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L9_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "レーさんの 結婚の [____] に、みんなで 花束を あげました。",
        "options": ["お祝い", "おみやげ", "おれい", "おねがい"],
        "correct": 0,
        "explain": "Tặng quà chúc mừng nhân dịp đám cưới: 「お祝い (おいわい)」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "私は 田中さんの 誕生日に ネクタイを [____]。",
        "options": ["あげました", "くれました", "いただきました", "くださった"],
        "correct": 0,
        "explain": "Tôi tặng cho người khác: 『私 ➔ 他人: あげます』 ➔ 「あげました」."
    },
    {
        "id": 3,
        "category": "Ngữ pháp",
        "q": "誕生日に 先生が すてきな 辞書を [____]。",
        "options": ["くれました", "あげました", "やりました", "もらいました"],
        "correct": 0,
        "explain": "Người khác tặng cho tôi dùng 『くれます』: 先生が私に ➔ 「くれました」."
    },
    {
        "id": 4,
        "category": "Hội thoại",
        "q": "「パーティーには 何人 [____] か。」 ―― 「全部で 8人です。」",
        "options": ["参加します", "案内します", "見学します", "練習します"],
        "correct": 0,
        "explain": "Có bao nhiêu người tham gia tiệc: 「参加します (さんかします)」."
    },
    {
        "id": 5,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「結婚」 có cách đọc chuẩn là gì?",
        "options": ["けっこん", "けつこん", "けつほん", "けっこお"],
        "correct": 0,
        "explain": "結婚 đọc là 「けっこん」 (KẾT HÔN)."
    },
    {
        "id": 6,
        "category": "Từ vựng",
        "q": "きれいな バラや チューリップを まとめた ものを [____] と 言います。",
        "options": ["はなたば", "ネクタイ", "とけい", "プレゼント"],
        "correct": 0,
        "explain": "Bó hoa tươi gom lại là 「花束 (はなたば)」."
    },
    {
        "id": 7,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「祝」 trong 「お祝い」 đọc Kunyomi là gì?",
        "options": ["いわい", "しゅくい", "のろい", "ことほぎ"],
        "correct": 0,
        "explain": "祝 có âm Kun là いわ・う, danh từ là 「お祝い (おいわい)」."
    },
    {
        "id": 8,
        "category": "Hội thoại",
        "q": "「プレゼントは 何が いいでしょうか。」 ―― 「山田さんに [____] みましょう。」",
        "options": ["相談して", "予約して", "見学して", "勉強して"],
        "correct": 0,
        "explain": "Hỏi ý kiến, bàn bạc với ai: 相談します (そうだんします) ➔ 「相談してみましょう」."
    },
    {
        "id": 9,
        "category": "Chữ Hán",
        "q": "Từ 「卒業」 có nghĩa là gì?",
        "options": ["Tốt nghiệp ra trường", "Nhập học", "Đi làm việc", "Nghỉ hưu"],
        "correct": 0,
        "explain": "卒業 (そつぎょう - TỐT NGHIỆP) nghĩa là hoàn thành khóa học, ra trường."
    },
    {
        "id": 10,
        "category": "Từ vựng",
        "q": "会社で 役職が 上がる おめでたい 出来事は [____] です。",
        "options": ["しょうしん", "しゅっさん", "けっこん", "そつぎょう"],
        "correct": 0,
        "explain": "Thăng chức lên chức vụ cao hơn: 「昇進 (しょうしん)」."
    },
    {
        "id": 11,
        "category": "Ngữ pháp",
        "q": "私は 母に きれいな スカーフを [____]。(Tôi nhận được từ mẹ)",
        "options": ["もらいました", "あげました", "やりました", "貸しました"],
        "correct": 0,
        "explain": "Tôi nhận được quà từ mẹ: 『[Người tặng] に/から もらいました』."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「時計」 gồm 2 chữ nào?",
        "options": ["THỜI + KẾ", "THỜI + KIM", "THỜI + ĐỘ", "ĐỒNG + KẾ"],
        "correct": 0,
        "explain": "時計 gồm THỜI (時) và KẾ (計) ➔ dụng cụ đo đếm thời gian (đồng hồ)."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "赤ちゃんが 無事に 生まれた お祝いは [____] 祝いです。",
        "options": ["しゅっさん", "しょうしん", "けっこん", "そつぎょう"],
        "correct": 0,
        "explain": "Mừng sinh em bé là mừng xuất sản: 「出産祝い (しゅっさんいわい)」."
    },
    {
        "id": 14,
        "category": "Hội thoại",
        "q": "プレゼントを あげたとき、相手が とても [____] くれました。",
        "options": ["よろこんで", "こまって", "つかれて", "いそいで"],
        "correct": 0,
        "explain": "Đối phương vui mừng khôn xiết: 喜ぶ (よろこぶ) ➔ 「喜んでくれました」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「誕」 trong 「誕生日」 có âm Hán Việt là gì?",
        "options": ["ĐẢN", "DIÊN", "SINH", "ĐẠI"],
        "correct": 0,
        "explain": "誕 có âm Hán Việt là ĐẢN (chào đời, sinh nở)."
    }
]


# =============================================================================
# LESSON 10 DATA
# =============================================================================
L10_VOCAB = [
    {"jp": "ケーキ", "kana": "ケーキ", "kanji": "ケーキ", "romaji": "keeki", "vi": "Bánh gato, bánh kem sinh nhật", "icon": "🎂"},
    {"jp": "チョコレート", "kana": "チョコレート", "kanji": "チョコレート", "romaji": "chokoreeto", "vi": "Sô-cô-la", "icon": "🍫"},
    {"jp": "フルーツ", "kana": "フルーツ", "kanji": "フルーツ", "romaji": "furuutsu", "vi": "Trái cây hoa quả", "icon": "🍓"},
    {"jp": "いちご", "kana": "いちご", "kanji": "いちご", "romaji": "ichigo", "vi": "Quả dâu tây", "icon": "🍓"},
    {"jp": "クリーム", "kana": "クリーム", "kanji": "クリーム", "romaji": "kuriimu", "vi": "Kem tươi", "icon": "🧁"},
    {"jp": "メッセージ", "kana": "メッセージ", "kanji": "メッセージ", "romaji": "messeoji", "vi": "Lời nhắn chúc mừng", "icon": "💌"},
    {"jp": "キャンドル", "kana": "キャンドル", "kanji": "キャンドル", "romaji": "kyandoru", "vi": "Cây nến sinh nhật", "icon": "🕯️"},
    {"jp": "人数", "kana": "にんずう", "kanji": "人数", "romaji": "ninzuu", "vi": "Số lượng người", "icon": "👨‍👩‍👧‍👦"},
    {"jp": "大きさ", "kana": "おおきさ", "kanji": "大きさ", "romaji": "ookisa", "vi": "Kích cỡ, độ lớn", "icon": "📏"},
    {"jp": "配達", "kana": "はいたつ", "kanji": "配達", "romaji": "haitatsu", "vi": "Giao hàng tận nơi", "icon": "🚚"},
    {"jp": "感謝", "kana": "かんしゃ", "kanji": "感謝", "romaji": "kansha", "vi": "Biết ơn, lòng cảm tạ", "icon": "🙏"},
    {"jp": "お礼", "kana": "おれい", "kanji": "お礼", "romaji": "orei", "vi": "Lời cảm ơn, quà đáp lễ", "icon": "🙇"},
    {"jp": "手紙", "kana": "てがみ", "kanji": "手紙", "romaji": "tegami", "vi": "Bức thư", "icon": "✉️"},
    {"jp": "サプライズ", "kana": "サプライズ", "kanji": "サプライズ", "romaji": "sapuraizu", "vi": "Bất ngờ (bữa tiệc bí mật)", "icon": "🎉"},
    {"jp": "びっくりする", "kana": "びっくりする", "kanji": "びっくりする", "romaji": "bikkurisuru", "vi": "Giật mình ngạc nhiên", "icon": "😲"},
    {"jp": "笑顔", "kana": "えがお", "kanji": "笑顔", "romaji": "egao", "vi": "Nụ cười rạng rỡ", "icon": "😄"},
    {"jp": "迎える", "kana": "むかえる", "kanji": "迎える", "romaji": "mukaeru", "vi": "Đón nhận, chào đón", "icon": "🤗"},
    {"jp": "決める", "kana": "きめる", "kanji": "決める", "romaji": "kimeru", "vi": "Quyết định chọn", "icon": "✔️"},
    {"jp": "届ける", "kana": "とどける", "kanji": "届ける", "romaji": "todokeru", "vi": "Giao tới, chuyển đến", "icon": "📦"},
    {"jp": "喜ぶ", "kana": "よろこぶ", "kanji": "喜ぶ", "romaji": "yorokobu", "vi": "Hân hoan đón mừng", "icon": "✨"}
]

L10_VERBS = [
    {"masu": "きめます", "vi": "Quyết định", "te": "きめて", "form1": "にきめました (đã quyết định chọn N)", "form2": "きめてください", "form3": "きめる"},
    {"masu": "とどけます", "vi": "Giao đến nơi", "te": "とどけて", "form1": "とどけてくれます (giao tới cho mình)", "form2": "とどけた", "form3": "とどける"},
    {"masu": "きてくれます", "vi": "Đến vì mình", "te": "きてくれて", "form1": "きてくれてありがとう (cảm ơn bạn đã đến)", "form2": "きてくれた", "form3": "きてくれる"},
    {"masu": "てつだいます", "vi": "Giúp đỡ", "te": "てつだって", "form1": "てつだってくれてありがとう (cảm ơn đã giúp)", "form2": "てつだった", "form3": "てつだう"},
    {"masu": "かんしゃします", "vi": "Biết ơn", "te": "かんしゃして", "form1": "かんしゃしています", "form2": "かんしゃした", "form3": "かんしゃする"}
]

L10_KANJI_LIST = [
    {"stt": 1, "word": "手紙", "kana": "てがみ", "hv": "THỦ CHỈ", "mean": "Lá thư"},
    {"stt": 2, "word": "お礼", "kana": "おれい", "hv": "LỄ", "mean": "Lời cảm ơn, quà cảm ơn"},
    {"stt": 3, "word": "感謝", "kana": "かんしゃ", "hv": "CẢM TẠ", "mean": "Biết ơn, cảm tạ"},
    {"stt": 4, "word": "配達", "kana": "はいたつ", "hv": "PHỐI ĐẠT", "mean": "Giao hàng"},
    {"stt": 5, "word": "人数", "kana": "にんずう", "hv": "NHÂN SỐ", "mean": "Số người"},
    {"stt": 6, "word": "笑顔", "kana": "えがお", "hv": "TIẾU NHAN", "mean": "Khuôn mặt cười"},
    {"stt": 7, "word": "決めます", "kana": "きめます", "hv": "QUYẾT", "mean": "Quyết định"}
]

L10_KANJI_CARDS = [
    {"char": "手", "hv": "Thủ", "strokes": 4, "kun": "て", "on": "しゅ", "ex": "手紙 (てがみ - bức thư), 歌手 (かしゅ - ca sĩ), 上手 (じょうず - giỏi giang)", "mnemonic": "Hình ảnh bàn tay với 5 ngón mở rộng (Thủ = bàn tay)."},
    {"char": "紙", "hv": "Chỉ", "strokes": 10, "kun": "かみ", "on": "し", "ex": "手紙 (てがみ - bức thư), 紙 (かみ - tờ giấy), 新聞紙 (しんぶんし - giấy báo)", "mnemonic": "Dùng sợi tơ (糸) giã thành bột trải phẳng trên họ thị (氏) để tạo nên Trang giấy."},
    {"char": "礼", "hv": "Lễ", "strokes": 5, "kun": "ー", "on": "れい、らい", "ex": "お礼 (おれい - lời cảm ơn), 礼儀 (れいぎ - lễ nghi), 失礼 (しつれい - thất lễ)", "mnemonic": "Đứng trước bàn thờ thần (礻) cúi mình thi lễ uốn cong hình móc (乚) là Lễ độ."},
    {"char": "謝", "hv": "Tạ", "strokes": 17, "kun": "あやま・る", "on": "しゃ", "ex": "感謝 (かんしゃ - cảm tạ/biết ơn), 謝る (あやまる - xin lỗi), 謝礼 (しゃれい - tiền thù lao)", "mnemonic": "Dùng lời nói (言) bắn đi mũi tên (射 - xạ) để bày tỏ tấm lòng Cảm tạ."},
    {"char": "配", "hv": "Phối", "strokes": 10, "kun": "くば・る", "on": "はい", "ex": "配達 (はいたつ - giao hàng), 心配 (しんぱい - lo lắng), 配布 (はいふ - phát tài liệu)", "mnemonic": "Đem hũ rượu ngon (酉) chia đều cho từng người ngồi quỳ gối (己) là Phân phối."},
    {"char": "達", "hv": "Đạt", "strokes": 12, "kun": "ー", "on": "たつ", "ex": "配達 (はいたつ - giao hàng), 友達 (ともだち - bạn bè), 達成 (たっせい - đạt thành)", "mnemonic": "Bước chân đi nhanh (辶) mang con dê nhỏ (羍) đến đích trọn vẹn là Thông đạt."},
    {"char": "数", "hv": "Số", "strokes": 13, "kun": "かず、かぞ・える", "on": "すう", "ex": "人数 (にんずう - số người), 数学 (すうがく - toán học), 数字 (すうじ - con số)", "mnemonic": "Đếm từng hạt gạo (米) rồi dùng roi (攵) gõ nhịp kiểm kê là Số lượng."}
]

L10_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>💖</span> 1. Bày Tỏ Lòng Biết Ơn: V-て くれて ありがとう</h2>
            <span class="section-tag">Lời cảm ơn chân thành</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để cảm ơn ai đó đã cất công làm một hành động tốt đẹp giúp đỡ hoặc đem lại niềm vui cho mình.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • [Động từ thể TE] ＋ くれて ありがとう（ございます）<br>
                    • 今日は 来てくれて ありがとう。(Cảm ơn vì hôm nay đã đến dự)
                </div>
                <div class="rule-meaning">
                    • <strong>手伝ってくれて ありがとう:</strong> Cảm ơn bạn đã phụ giúp mình.<br>
                    • <strong>教えてくれて ありがとうございます:</strong> Cảm ơn vì đã chỉ bảo cho tôi.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">私の 結婚パーティーに 来てくれて、本当に ありがとう！</div>
                        <div class="ex-vi">Thực sự cảm ơn các bạn rất nhiều vì đã đến dự bữa tiệc cưới của mình!</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('私の結婚パーティーに来てくれて、本当にありがとう')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🎂</span> 2. Quyết Định Lựa Chọn: N に します</h2>
            <span class="section-tag">Đặt bánh kem & Gọi món</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • どんな ケーキが いいですか。(Bạn thích bánh kem loại nào?)<br>
                    • いちごの ケーキに します。(Tôi quyết định chọn bánh kem dâu tây)
                </div>
                <div class="rule-meaning">
                    Cấu trúc <code>N に します</code> biểu thị sự quyết định dứt khoát khi gọi món ăn hoặc chọn quà trong số nhiều phương án.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">フルーツケーキと チョコレートケーキ、どちらに しますか。</div>
                        <div class="ex-vi">Bánh hoa quả và bánh sô-cô-la, bạn quyết định chọn loại nào?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('フルーツケーキとチョコレートケーキ、どちらにしますか')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L10_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "パーティーに [____] くれて、本当に ありがとうございました。",
        "options": ["来て", "行きて", "来たら", "来る"],
        "correct": 0,
        "explain": "Cảm ơn vì đã đến tham gia: 来ます ➔ thể TE là 「来て (きて)」 ＋ くれてありがとう."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "いろいろ 準備を [____] くれて ありがとう。とても 助かったよ。",
        "options": ["手伝って", "手伝う", "手伝った", "手伝い"],
        "correct": 0,
        "explain": "Cảm ơn vì đã giúp đỡ: 手伝います ➔ thể TE là 「手伝って」."
    },
    {
        "id": 3,
        "category": "Ngữ pháp",
        "q": "ケーキの 種類は いちごの ショートケーキ [____] します。",
        "options": ["に", "を", "で", "が"],
        "correct": 0,
        "explain": "Mẫu câu quyết định lựa chọn: 『N に します』."
    },
    {
        "id": 4,
        "category": "Từ vựng",
        "q": "ケーキの 上に のせる 赤くて 甘酸っぱい 果物は [____] です。",
        "options": ["いちご", "チョコレート", "キャンドル", "メッセージ"],
        "correct": 0,
        "explain": "Quả dâu tây phủ trên bánh kem là 「いちご」."
    },
    {
        "id": 5,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「手紙」 có nghĩa là gì?",
        "options": ["Bức thư", "Tờ giấy", "Bàn tay", "Quyển sách"],
        "correct": 0,
        "explain": "手紙 (てがみ - THỦ CHỈ) có nghĩa là bức thư."
    },
    {
        "id": 6,
        "category": "Hội thoại",
        "q": "内緒（ないしょ）で 準備して 相手を 驚かせる 計画を 「[____] パーティー」 と 言います。",
        "options": ["サプライズ", "メッセージ", "キャンドル", "チョコレート"],
        "correct": 0,
        "explain": "Bữa tiệc bất ngờ tạo ngạc nhiên là 「サプライズ (surprise)」."
    },
    {
        "id": 7,
        "category": "Chữ Hán",
        "q": "Từ 「配達」 có âm Hán Việt là gì?",
        "options": ["PHỐI ĐẠT", "PHỐI HỢP", "XUẤT ĐẠT", "THÔNG ĐẠT"],
        "correct": 0,
        "explain": "配達 có âm Hán Việt là PHỐI ĐẠT (giao hàng tận nơi)."
    },
    {
        "id": 8,
        "category": "Từ vựng",
        "q": "誕生日ケーキの 上に 立てて 火を つける ろうそくは [____] です。",
        "options": ["キャンドル", "クリーム", "フルーツ", "ケーキ"],
        "correct": 0,
        "explain": "Nến cắm bánh sinh nhật là 「キャンドル (candle)」."
    },
    {
        "id": 9,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「お礼」 đọc là gì?",
        "options": ["おれい", "おらい", "おさつ", "おぎ"],
        "correct": 0,
        "explain": "お礼 đọc là 「おれい」 (lời cảm ơn / quà đáp lễ)."
    },
    {
        "id": 10,
        "category": "Hội thoại",
        "q": "「どんな ケーキが いいですか。」 ―― 「チョコレートの ケーキが [____] です。」",
        "options": ["いい", "よくない", "いく", "よく"],
        "correct": 0,
        "explain": "Bày tỏ loại mình thích: 「～がいいです」 (loại đó được/thích loại đó)."
    },
    {
        "id": 11,
        "category": "Từ vựng",
        "q": "ケーキの プレートに 「お誕生日 おめでとう」 と チョコペンで [____] を 書きます。",
        "options": ["メッセージ", "てがみ", "にんずう", "えがお"],
        "correct": 0,
        "explain": "Lời nhắn chúc mừng ghi trên socola là 「メッセージ (message)」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Từ 「感謝」 gồm 2 chữ nào ghép lại?",
        "options": ["CẢM + TẠ", "CẢM + TÌNH", "CẢM + TÂM", "ÁI + TẠ"],
        "correct": 0,
        "explain": "感謝 gồm CẢM (感) và TẠ (謝) ➔ cảm tạ, lòng biết ơn."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "パーティーの 参加者の [____] は 何人ですか。",
        "options": ["にんずう", "おおきさ", "えがお", "おれい"],
        "correct": 0,
        "explain": "Số lượng người tham gia: 「人数 (にんずう)」."
    },
    {
        "id": 14,
        "category": "Ngữ pháp",
        "q": "すてきな プレゼントを [____] くれて、本当に うれしいです。",
        "options": ["えらんで", "えらんだ", "えらぶ", "えらび"],
        "correct": 0,
        "explain": "Đã cất công chọn quà tặng mình: 選んでくれて (thể TE ＋ くれて)."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「人数」 đọc là gì?",
        "options": ["にんずう", "ひとすう", "じんずう", "にんすう"],
        "correct": 0,
        "explain": "人数 đọc là 「にんずう」."
    }
]
