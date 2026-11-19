# -*- coding: utf-8 -*-
"""
Topic 3: 沖縄旅行 (Okinawa Trip / Chuyến du lịch Okinawa)
- Lesson 5: ぼうしを持っていったほうがいいです (You'd better take a hat with you)
- Lesson 6: 海で泳いだり、写真を撮ったりしました (I swam in the sea and took pictures)
"""

# =============================================================================
# LESSON 5 DATA
# =============================================================================
L5_VOCAB = [
    {"jp": "沖縄", "kana": "おきなわ", "kanji": "沖縄", "romaji": "okinawa", "vi": "Okinawa (quần đảo phương nam Nhật Bản)", "icon": "🏝️"},
    {"jp": "旅行", "kana": "りょこう", "kanji": "旅行", "romaji": "ryokou", "vi": "Du lịch, chuyến đi", "icon": "✈️"},
    {"jp": "準備", "kana": "じゅんび", "kanji": "準備", "romaji": "junbi", "vi": "Chuẩn bị", "icon": "🧳"},
    {"jp": "荷物", "kana": "にもつ", "kanji": "荷物", "romaji": "nimotsu", "vi": "Hành lý", "icon": "🎒"},
    {"jp": "ぼうし", "kana": "ぼうし", "kanji": "ぼうし", "romaji": "boushi", "vi": "Mũ, nón", "icon": "👒"},
    {"jp": "日焼け止め", "kana": "ひやけどめ", "kanji": "日焼け止め", "romaji": "hiyakedome", "vi": "Kem chống nắng", "icon": "🧴"},
    {"jp": "水着", "kana": "みずぎ", "kanji": "水着", "romaji": "mizugi", "vi": "Đồ bơi", "icon": "🩱"},
    {"jp": "薬", "kana": "くすり", "kanji": "薬", "romaji": "kusuri", "vi": "Thuốc", "icon": "💊"},
    {"jp": "予約", "kana": "よやく", "kanji": "予約", "romaji": "yoyaku", "vi": "Đặt trước, hẹn trước", "icon": "📅"},
    {"jp": "飛行機", "kana": "ひこうき", "kanji": "飛行機", "romaji": "hikouki", "vi": "Máy bay", "icon": "🛫"},
    {"jp": "空港", "kana": "くうこう", "kanji": "空港", "romaji": "kuukou", "vi": "Sân bay", "icon": "🏢"},
    {"jp": "ホテル", "kana": "ホテル", "kanji": "ホテル", "romaji": "hoteru", "vi": "Khách sạn", "icon": "🏨"},
    {"jp": "ガイドブック", "kana": "ガイドブック", "kanji": "ガイドブック", "romaji": "gaidobukku", "vi": "Sách hướng dẫn du lịch", "icon": "📖"},
    {"jp": "観光", "kana": "かんこう", "kanji": "観光", "romaji": "kankou", "vi": "Tham quan, du lịch ngắm cảnh", "icon": "📸"},
    {"jp": "景色", "kana": "けしき", "kanji": "景色", "romaji": "keshiki", "vi": "Phong cảnh, cảnh sắc", "icon": "🌅"},
    {"jp": "気候", "kana": "きこう", "kanji": "気候", "romaji": "kikou", "vi": "Khí hậu", "icon": "🌤️"},
    {"jp": "暑い", "kana": "あつい", "kanji": "暑い", "romaji": "atsui", "vi": "Nóng (thời tiết)", "icon": "☀️"},
    {"jp": "涼しい", "kana": "すずしい", "kanji": "涼しい", "romaji": "suzushii", "vi": "Mát mẻ", "icon": "🍃"},
    {"jp": "忘れ物", "kana": "わすれもの", "kanji": "忘れ物", "romaji": "wasuremono", "vi": "Đồ để quên", "icon": "⚠️"},
    {"jp": "気をつける", "kana": "きをつける", "kanji": "気をつける", "romaji": "ki o tsukeru", "vi": "Cẩn thận, chú ý", "icon": "👀"}
]

L5_VERBS = [
    {"masu": "もっていきます", "vi": "Mang theo đi", "te": "もっていって", "form1": "もっていったほうがいい (nên mang theo)", "form2": "もっていかないほうがいい (không nên mang)", "form3": "もっていく"},
    {"masu": "よやくします", "vi": "Đặt trước", "te": "よやくして", "form1": "よやくしたほうがいい (nên đặt trước)", "form2": "よやくしないほうがいい", "form3": "よやくする"},
    {"masu": "しらべます", "vi": "Tra cứu, tìm hiểu", "te": "しらべて", "form1": "しらべたほうがいい (nên tra trước)", "form2": "しらべないほうがいい", "form3": "しらべる"},
    {"masu": "とまります", "vi": "Trọ lại khách sạn", "te": "とまって", "form1": "とまったほうがいい (nên trọ ở)", "form2": "とまらないほうがいい", "form3": "とまる"},
    {"masu": "わすれます", "vi": "Quên", "te": "わすれて", "form1": "わすれないほうがいい (không nên quên)", "form2": "わすれた (đã quên)", "form3": "わすれる"}
]

L5_KANJI_LIST = [
    {"stt": 1, "word": "旅行", "kana": "りょこう", "hv": "LỮ HÀNH", "mean": "Du lịch"},
    {"stt": 2, "word": "旅館", "kana": "りょかん", "hv": "LỮ QUÁN", "mean": "Quán trọ kiểu Nhật"},
    {"stt": 3, "word": "予約", "kana": "よやく", "hv": "DỰ ƯỚC", "mean": "Đặt trước"},
    {"stt": 4, "word": "予定", "kana": "よてい", "hv": "DỰ ĐỊNH", "mean": "Dự định"},
    {"stt": 5, "word": "空港", "kana": "くうこう", "hv": "KHÔNG CẢNG", "mean": "Sân bay"},
    {"stt": 6, "word": "空気", "kana": "くうき", "hv": "KHÔNG KHÍ", "mean": "Không khí"},
    {"stt": 7, "word": "港", "kana": "みなと", "hv": "CẢNG", "mean": "Bến cảng"},
    {"stt": 8, "word": "暑い", "kana": "あつい", "hv": "THỬ", "mean": "Nóng bức (thời tiết)"},
    {"stt": 9, "word": "涼しい", "kana": "すずしい", "hv": "LƯƠNG", "mean": "Mát mẻ"},
    {"stt": 10, "word": "忘れ物", "kana": "わすれもの", "hv": "VONG VẬT", "mean": "Đồ bỏ quên"}
]

L5_KANJI_CARDS = [
    {"char": "旅", "hv": "Lữ", "strokes": 10, "kun": "たび", "on": "りょ", "ex": "旅行 (りょこう - du lịch), 旅館 (りょかん - nhà trọ Nhật), 旅人 (たびびと - lữ khách)", "mnemonic": "Dưới lá cờ (方) mọi người cất bước theo đoàn đi Lữ hành viễn du."},
    {"char": "予", "hv": "Dự", "strokes": 4, "kun": "あらかじ・め", "on": "よ", "ex": "予約 (よやく - đặt trước), 予定 (よてい - dự định), 予習 (よしゅう - chuẩn bị bài trước)", "mnemonic": "Hình ảnh con thoi đưa đi đưa lại chuẩn bị Dự liệu trước khi dệt."},
    {"char": "約", "hv": "Ước", "strokes": 9, "kun": "ー", "on": "やく", "ex": "予約 (よやく - hẹn trước), 約束 (やくそく - lời hứa), 約 (やく - khoảng chừng)", "mnemonic": "Dùng sợi tơ (糸) buộc chặt cái thìa (勺) làm bằng chứng cho Giao ước."},
    {"char": "空", "hv": "Không", "strokes": 8, "kun": "そら、あ・く", "on": "くう", "ex": "空港 (くうこう - sân bay), 空気 (くうき - không khí), 青空 (あおぞら - trời xanh)", "mnemonic": "Dưới mái hang (穴) thợ thủ công (工) ngước nhìn khoảng Bầu trời trống không."},
    {"char": "港", "hv": "Cảng", "strokes": 12, "kun": "みなと", "on": "こう", "ex": "空港 (くうこう - sân bay), 港 (みなと - bến cảng), 港町 (みなとまち - phố cảng)", "mnemonic": "Nơi có dòng nước (氵) chung nhau (共) thuyền bè ra vào tấp nập là Bến cảng."},
    {"char": "暑", "hv": "Thử", "strokes": 12, "kun": "あつ・い", "on": "しょ", "ex": "暑い (あつい - nóng nực), 猛暑 (もうしょ - nắng nóng gay gắt), 避暑 (ひしょ - tránh nóng)", "mnemonic": "Mặt trời (日) chiếu thẳng lên người (者) đốt cháy da thịt là Nóng bức."},
    {"char": "涼", "hv": "Lương", "strokes": 11, "kun": "すず・しい", "on": "りょう", "ex": "涼しい (すずしい - mát mẻ), 清涼 (せいりょう - mát lành)", "mnemonic": "Dòng nước (氵) tại kinh đô (京) mang lại cảm giác Mát mẻ khoan khoái."},
    {"char": "忘", "hv": "Vong", "strokes": 7, "kun": "わす・れる", "on": "ぼう", "ex": "忘れる (わすれる - quên), 忘れ物 (わすれもの - đồ bỏ quên), 忘年会 (ぼうねんかい - tiệc tất niên)", "mnemonic": "Tâm trí (心) chết đi hoặc mất hút (亡) khiến ta Quên lãng mọi sự."}
]

L5_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>💡</span> 1. Đưa Ra Lời Khuyên: V-た ほうがいい / V-ない ほうがいい</h2>
            <span class="section-tag">Khuyên nhủ du lịch</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để đưa ra lời khuyên chân thành và hữu ích cho ai đó: "Nên làm V" hoặc "Không nên làm V".
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • [Động từ thể TA] ＋ ほうがいいです (Nên...)<br>
                    • [Động từ thể NAI] ＋ ほうがいいです (Không nên...)
                </div>
                <div class="rule-meaning">
                    • <strong>ぼうしを 持っていった ほうがいいです:</strong> Bạn nên mang theo nón/mũ.<br>
                    • <strong>ホテルを 早く 予約した ほうがいいです:</strong> Nên đặt phòng khách sạn sớm.<br>
                    • <strong>無理を しない ほうがいいです:</strong> Không nên gắng sức quá.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">沖縄の日差しは 強いですから、日焼け止めを 塗った（ぬった）ほうがいいですよ。</div>
                        <div class="ex-vi">Nắng ở Okinawa gay gắt lắm nên bạn nên bôi kem chống nắng vào nhé.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('沖縄の日差しは強いですから、日焼け止めを塗ったほうがいいですよ')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">台風のときは 海で 泳がない ほうがいいです。</div>
                        <div class="ex-vi">Khi có bão thì không nên tắm biển đâu.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('台風のときは海で泳がないほうがいいです')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>❓</span> 2. Xin Lời Khuyên Hành Trình: V-たら いいですか</h2>
            <span class="section-tag">Hỏi ý kiến người bản xứ</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • どこに 行ったら いいですか。(Tôi nên đi đâu thì tốt?)<br>
                    • 何を 持っていったら いいですか。(Tôi nên mang theo những gì?)
                </div>
                <div class="rule-meaning">
                    Cấu trúc <code>Từ để hỏi + V-たらいいですか</code> là mẫu câu vàng khi lập kế hoạch du lịch để người có kinh nghiệm mách nước.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">初めて 沖縄へ 行くんですが、どこを 観光したら いいですか。</div>
                        <div class="ex-vi">Tôi sắp đi Okinawa lần đầu, nên đi tham quan những đâu thì tốt ạ?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('初めて沖縄へ行くんですが、どこを観光したらいいですか')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L5_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "沖縄の 夏は 日差しが 強いですから、ぼうしを [____] ほうがいいですよ。",
        "options": ["持っていった", "持っていく", "持っていかない", "持っていって"],
        "correct": 0,
        "explain": "Đưa ra lời khuyên nên làm gì: V-たほうがいい ➔ 「持っていったほうがいい」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "人気のある ホテルですから、早く [____] ほうがいいです。",
        "options": ["予約した", "予約して", "予約する", "予約しない"],
        "correct": 0,
        "explain": "Nên đặt phòng sớm: 予約しました ➔ thể TA: 「予約した」 ＋ ほうがいい."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "飛行機に 乗るために、時間に 余裕を もって [____] へ 行きます。",
        "options": ["くうこう", "みなと", "りょかん", "おてら"],
        "correct": 0,
        "explain": "Đi máy bay phải đến sân bay: 「空港 (くうこう)」."
    },
    {
        "id": 4,
        "category": "Ngữ pháp",
        "q": "沖縄へ 旅行に 行くんですが、何を 着て [____] いいですか。",
        "options": ["行ったら", "行けば", "行くと", "行くなら"],
        "correct": 0,
        "explain": "Xin lời khuyên nên mặc gì đi: V-たらいいですか ➔ 「行ったらいいですか」."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "海で 泳ぐときに 着る 服を [____] と 言います。",
        "options": ["みずぎ", "ゆかた", "ぼうし", "にもつ"],
        "correct": 0,
        "explain": "Đồ bơi tiếng Nhật là 「水着 (みずぎ)」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「旅行」 có âm Hán Việt là gì?",
        "options": ["LỮ HÀNH", "LỮ QUÁN", "HÀNH LÝ", "DỰ ĐỊNH"],
        "correct": 0,
        "explain": "旅行 có âm Hán Việt là LỮ HÀNH (du lịch)."
    },
    {
        "id": 7,
        "category": "Từ vựng",
        "q": "日焼けを 防ぐために 肌に 塗る クリームは [____] です。",
        "options": ["ひやけどめ", "くすり", "ぼうし", "ガイドブック"],
        "correct": 0,
        "explain": "Kem chống nắng là 「日焼け止め (ひやけどめ)」."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Từ 「予約」 đọc là gì?",
        "options": ["よやく", "よてい", "やくそく", "よき"],
        "correct": 0,
        "explain": "予約 đọc là 「よやく」 (DỰ ƯỚC - Đặt chỗ trước)."
    },
    {
        "id": 9,
        "category": "Ngữ pháp",
        "q": "あしたは 朝 早く 出発しますから、今夜は 夜更かしを [____] ほうがいいです。",
        "options": ["しない", "した", "して", "する"],
        "correct": 0,
        "explain": "Khuyên không nên làm gì: V-ないほうがいい ➔ 「しないほうがいい」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「暑い」 dùng để miêu tả cái gì nóng?",
        "options": ["Thời tiết, khí hậu nóng nực", "Nước trà nóng", "Đồ vật nóng bỏng", "Đồ ăn cay nóng"],
        "correct": 0,
        "explain": "暑い (THỬ) chuyên dùng chỉ thời tiết khí hậu nóng nực (khác với 熱い dùng cho vật chất/nước nóng)."
    },
    {
        "id": 11,
        "category": "Từ vựng",
        "q": "観光地や おいしい レストランの 情報が のっている 本は [____] です。",
        "options": ["ガイドブック", "メニュー", "手紙", "辞書"],
        "correct": 0,
        "explain": "Sách cẩm nang chỉ dẫn du lịch: 「ガイドブック (guidebook)」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「涼しい」 đọc là gì?",
        "options": ["すずしい", "あたたかい", "さむい", "あつい"],
        "correct": 0,
        "explain": "涼しい đọc là 「すずしい」 (LƯƠNG - Mát mẻ)."
    },
    {
        "id": 13,
        "category": "Hội thoại",
        "q": "「沖縄旅行、楽しんできてね！」 ―― 「[____]」",
        "options": ["ありがとう、行ってきます！", "どういたしまして。", "こちらこそ、すみません。", "ただいま。"],
        "correct": 0,
        "explain": "Khi được bạn chúc chuyến đi vui vẻ, ta đáp: 「ありがとう、行ってきます！」 (Cảm ơn, tớ lên đường đây!)."
    },
    {
        "id": 14,
        "category": "Chữ Hán",
        "q": "Từ 「忘れ物」 nghĩa là gì?",
        "options": ["Đồ bị để quên", "Hành lý mang theo", "Quà lưu niệm", "Sách hướng dẫn"],
        "correct": 0,
        "explain": "忘れ物 (わすれもの) là đồ bỏ quên."
    },
    {
        "id": 15,
        "category": "Từ vựng",
        "q": "旅行の 前の 日に、スーツケースに 必要な ものを 入れて [____] を します。",
        "options": ["じゅんび", "かんこう", "よやく", "りょこう"],
        "correct": 0,
        "explain": "Soạn hành lý trước chuyến đi là công tác chuẩn bị: 「準備 (じゅんび) を します」."
    }
]


# =============================================================================
# LESSON 6 DATA
# =============================================================================
L6_VOCAB = [
    {"jp": "海", "kana": "うみ", "kanji": "海", "romaji": "umi", "vi": "Biển, đại dương", "icon": "🌊"},
    {"jp": "砂浜", "kana": "すなはま", "kanji": "砂浜", "romaji": "sunahama", "vi": "Bãi cát trắng", "icon": "🏖️"},
    {"jp": "泳ぐ", "kana": "およぐ", "kanji": "泳ぐ", "romaji": "oyogu", "vi": "Bơi lội", "icon": "🏊"},
    {"jp": "ダイビング", "kana": "ダイビング", "kanji": "ダイビング", "romaji": "daibingu", "vi": "Lặn biển", "icon": "🤿"},
    {"jp": "写真", "kana": "しゃしん", "kanji": "写真", "romaji": "shashin", "vi": "Bức ảnh", "icon": "📷"},
    {"jp": "撮る", "kana": "とる", "kanji": "撮る", "romaji": "toru", "vi": "Chụp (ảnh)", "icon": "📸"},
    {"jp": "お土産", "kana": "おみやげ", "kanji": "お土産", "romaji": "omiyage", "vi": "Quà lưu niệm, đặc sản", "icon": "🎁"},
    {"jp": "シーサー", "kana": "シーサー", "kanji": "シーサー", "romaji": "shiisaa", "vi": "Tượng sư tử Shisa thần hộ mệnh Okinawa", "icon": "🦁"},
    {"jp": "ガラス", "kana": "ガラス", "kanji": "ガラス", "romaji": "garasu", "vi": "Thủy tinh, kính", "icon": "🥛"},
    {"jp": "コップ", "kana": "コップ", "kanji": "コップ", "romaji": "koppu", "vi": "Cái cốc, ly", "icon": "🥃"},
    {"jp": "工芸", "kana": "こうげい", "kanji": "工芸", "romaji": "kougei", "vi": "Thủ công mỹ nghệ", "icon": "🏺"},
    {"jp": "体験", "kana": "たいけん", "kanji": "体験", "romaji": "taiken", "vi": "Trải nghiệm thực tế", "icon": "✨"},
    {"jp": "水族館", "kana": "すいぞくかん", "kanji": "水族館", "romaji": "suizokukan", "vi": "Thủy cung", "icon": "🐬"},
    {"jp": "青い", "kana": "あおい", "kanji": "青い", "romaji": "aoi", "vi": "Xanh da trời / xanh lam biếc", "icon": "🔷"},
    {"jp": "綺麗（な）", "kana": "きれい（な）", "kanji": "綺麗（な）", "romaji": "kirei(na)", "vi": "Đẹp, sạch sẽ", "icon": "✨"},
    {"jp": "感動する", "kana": "かんどうする", "kanji": "感動する", "romaji": "kandousuru", "vi": "Cảm động, xúc động bồi hồi", "icon": "🥹"},
    {"jp": "思い出", "kana": "おもいで", "kanji": "思い出", "romaji": "omoide", "vi": "Kỷ niệm đẹp", "icon": "💭"},
    {"jp": "初めて", "kana": "はじめて", "kanji": "初めて", "romaji": "hajimete", "vi": "Lần đầu tiên", "icon": "🌱"},
    {"jp": "また", "kana": "また", "kanji": "また", "romaji": "mata", "vi": "Lại nữa, lần nữa", "icon": "🔄"},
    {"jp": "案内する", "kana": "あんないする", "kanji": "案内する", "romaji": "annaisuru", "vi": "Hướng dẫn, dẫn đường", "icon": "💁"}
]

L6_VERBS = [
    {"masu": "およぎます", "vi": "Bơi", "te": "およいで", "form1": "およいだり (khi thì bơi...)", "form2": "およぐことができる (có thể bơi)", "form3": "およぐ"},
    {"masu": "とります", "vi": "Chụp (ảnh)", "te": "とって", "form1": "とったり (khi thì chụp ảnh...)", "form2": "とることができる (có thể chụp)", "form3": "とる"},
    {"masu": "つくります", "vi": "Làm ra", "te": "つくって", "form1": "つくったり (làm cái này cái kia...)", "form2": "つくることができる (có thể tự làm)", "form3": "つくる"},
    {"masu": "たいけんします", "vi": "Trải nghiệm", "te": "たいけんして", "form1": "たいけんしたり", "form2": "たいけんすることができる", "form3": "たいけんする"},
    {"masu": "あんないします", "vi": "Hướng dẫn", "te": "あんないして", "form1": "あんないしたり", "form2": "あんないすることができる", "form3": "あんないする"}
]

L6_KANJI_LIST = [
    {"stt": 1, "word": "海", "kana": "うみ", "hv": "HẢI", "mean": "Biển"},
    {"stt": 2, "word": "海外", "kana": "かいがい", "hv": "HẢI NGOẠI", "mean": "Nước ngoài"},
    {"stt": 3, "word": "写真", "kana": "しゃしん", "hv": "TẢ CHÂN", "mean": "Bức ảnh"},
    {"stt": 4, "word": "真ん中", "kana": "まんなか", "hv": "CHÂN TRUNG", "mean": "Chính giữa"},
    {"stt": 5, "word": "撮ります", "kana": "とります", "hv": "TOÁT", "mean": "Chụp (ảnh)"},
    {"stt": 6, "word": "泳ぎます", "kana": "およぎます", "hv": "VỊNH", "mean": "Bơi lội"},
    {"stt": 7, "word": "体験", "kana": "たいけん", "hv": "THỂ NGHIỆM", "mean": "Trải nghiệm"},
    {"stt": 8, "word": "楽しい", "kana": "たのしい", "hv": "LẠC / NHẠC", "mean": "Vui vẻ"},
    {"stt": 9, "word": "思い出", "kana": "おもいで", "hv": "TƯ XUẤT", "mean": "Kỷ niệm"}
]

L6_KANJI_CARDS = [
    {"char": "海", "hv": "Hải", "strokes": 9, "kun": "うみ", "on": "かい", "ex": "海 (うみ - biển), 海外 (かいがい - nước ngoài), 海水浴 (かいすいよく - tắm biển)", "mnemonic": "Nơi gom tụ mọi dòng nước (氵) của mỗi (毎) nhánh sông đổ về là Biển cả."},
    {"char": "写", "hv": "Tả", "strokes": 5, "kun": "うつ・す", "on": "しゃ", "ex": "写真 (しゃしん - bức ảnh), 描写 (びょうしゃ - miêu tả)", "mnemonic": "Dưới mái hiên (冖) đặt một khung tranh vẽ sao chép hình dáng sự vật (Tả)."},
    {"char": "真", "hv": "Chân", "strokes": 10, "kun": "ま、まこと", "on": "しん", "ex": "写真 (しゃしん - ảnh chụp chân thật), 真ん中 (まんなか - chính giữa), 真面目 (まじめ - nghiêm túc)", "mnemonic": "Mười (十) con mắt (目) cùng soi vào cái đế cân thì mới thấy được Chân lý."},
    {"char": "撮", "hv": "Toát", "strokes": 15, "kun": "と・る", "on": "さつ", "ex": "撮る (とる - chụp ảnh), 撮影 (さつえい - quay phim/chụp hình)", "mnemonic": "Bàn tay (扌) bấm máy nhanh thoăn thoắt để thâu tóm (最) khoảnh khắc đẹp."},
    {"char": "泳", "hv": "Vịnh", "strokes": 8, "kun": "およ・ぐ", "on": "えい", "ex": "泳ぐ (およぐ - bơi lội), 水泳 (すいえい - môn bơi)", "mnemonic": "Dòng nước (氵) chảy vĩnh viễn (永) nơi con người tung tăng Bơi lội."},
    {"char": "体", "hv": "Thể", "strokes": 7, "kun": "からだ", "on": "たい、てい", "ex": "体験 (たいけん - trải nghiệm), 体 (からだ - cơ thể), 体重 (たいじゅう - thể trọng/cân nặng)", "mnemonic": "Con người (亻) gắn liền với gốc rễ (本) tạo nên Cơ thể vững vàng."},
    {"char": "験", "hv": "Nghiệm", "strokes": 18, "kun": "ー", "on": "けん", "ex": "体験 (たいけん - trải nghiệm), 試験 (しけん - kỳ thi), 経験 (けいけん - kinh nghiệm)", "mnemonic": "Dùng ngựa tốt (馬) phối hợp với sự kiểm tra nghiêm cẩn (佥) để Thí nghiệm."},
    {"char": "楽", "hv": "Lạc / Nhạc", "strokes": 13, "kun": "たの・しい、たの・しむ", "on": "がく、らく", "ex": "楽しい (たのしい - vui vẻ), 音楽 (おんがく - âm nhạc), 楽（な） (らく - nhàn nhã)", "mnemonic": "Cây đàn bằng gỗ (木) gảy lên những nốt nhạc khiến lòng người An lạc, hân hoan."}
]

L6_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🏖️</span> 1. Liệt Kê Hành Động Tiêu Biểu: V1-たり、V2-たり します / しました</h2>
            <span class="section-tag">Kể lại kỳ nghỉ</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để liệt kê 2 hoặc 3 hành động tiêu biểu đại diện trong nhiều hành động đã làm hoặc dự định làm trong chuyến đi.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">[V1 thể TA] ＋ り、[V2 thể TA] ＋ り します / しました</div>
                <div class="rule-meaning">
                    • <strong>海で 泳いだり、写真を 撮ったりしました:</strong> Tôi đã tắm biển, chụp ảnh (và làm nhiều điều thú vị khác).<br>
                    • <strong>お土産を 買ったり、おいしいものを 食べたりしたいです:</strong> Muốn mua quà, ăn ngon...
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">沖縄では、青い海で 泳いだり、美ら海水族館へ 行ったりしました。</div>
                        <div class="ex-vi">Ở Okinawa, tôi đã tắm ở biển xanh ngắt, rồi đi thủy cung Churaumi.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('沖縄では、青い海で泳いだり、美ら海水族館へ行ったりしました')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">休みの 日は、本を 読んだり 音楽を 聞いたりして のんびり過ごします。</div>
                        <div class="ex-vi">Ngày nghỉ tôi thong thả đọc sách, nghe nhạc...</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('休みの日は、本を読んだり音楽を聞いたりしてのんびり過ごします')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🏺</span> 2. Khả Năng Thực Hiện: V-る ことが できます</h2>
            <span class="section-tag">Trải nghiệm làng nghề & Du lịch</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">[Động từ thể Từ điển] ＋ ことが できます (Có thể làm V)</div>
                <div class="rule-meaning">
                    Diễn đạt năng lực bản thân hoặc cơ hội trải nghiệm tại địa điểm du lịch: "Ở đây có thể tự tay làm cốc thủy tinh..."
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">ここでは、自分で 琉球ガラスの コップを 作ることが できます。</div>
                        <div class="ex-vi">Tại đây, bạn có thể tự tay làm ra chiếc cốc thủy tinh Ryukyu.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('ここでは、自分で琉球ガラスのコップを作ることができます')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L6_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "沖縄の 海で [____]、写真を 撮ったりしました。",
        "options": ["泳いだり", "泳いで", "泳ぐ", "泳ぎ"],
        "correct": 0,
        "explain": "Cấu trúc liệt kê hành động tiêu biểu: 『V1-たり、V2-たりしました』: 泳ぎました ➔ 「泳いだり」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "琉球ガラスの 工房で、きれいな コップを [____] ことが できます。",
        "options": ["作る", "作って", "作った", "作り"],
        "correct": 0,
        "explain": "Cấu trúc chỉ khả năng 『V-ることが できます』: động từ đứng trước phải ở thể từ điển ➔ 「作る」."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "旅行から 帰ったあと、家族や 友達に 配る お菓子などの プレゼントを [____] と 言います。",
        "options": ["おみやげ", "しゃしん", "シーサー", "にもつ"],
        "correct": 0,
        "explain": "Quà lưu niệm, đặc sản mua về tặng người thân: 「お土産 (おみやげ)」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「写真」 gồm 2 chữ nào ghép lại?",
        "options": ["TẢ + CHÂN", "HỌA + CHÂN", "TẢ + THẦN", "QUANG + CHÂN"],
        "correct": 0,
        "explain": "写真 gồm chữ TẢ (写) và CHÂN (真) ➔ miêu tả lại chân thật hình ảnh (bức ảnh)."
    },
    {
        "id": 5,
        "category": "Ngữ pháp",
        "q": "週末は 買い物に [____]、部屋を 掃除したりしました。",
        "options": ["行ったり", "行って", "行った", "行く"],
        "correct": 0,
        "explain": "Đi mua sắm: 行きました ➔ thể たり là 「行ったり」."
    },
    {
        "id": 6,
        "category": "Từ vựng",
        "q": "沖縄の 家の 屋根や 門に 置かれている 獅子（しし）の 像は [____] です。",
        "options": ["シーサー", "コップ", "ガラス", "ダイビング"],
        "correct": 0,
        "explain": "Tượng thần hộ mệnh trừ tà truyền thống ở Okinawa là 「シーサー (Shisa)」."
    },
    {
        "id": 7,
        "category": "Chữ Hán",
        "q": "Động từ 「撮る (とる)」 dùng với danh từ nào?",
        "options": ["写真 (しゃしん)", "海 (うみ)", "お土産 (おみやげ)", "コップ"],
        "correct": 0,
        "explain": "写真を撮る (chụp ảnh)."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Từ 「体験」 có cách đọc chuẩn là gì?",
        "options": ["たいけん", "たいげん", "からだけん", "しけん"],
        "correct": 0,
        "explain": "体験 đọc là 「たいけん」 (THỂ NGHIỆM - trải nghiệm thực tế)."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "海の中に もぐって カラフルな 魚を 見る スポーツは [____] です。",
        "options": ["ダイビング", "サッカー", "ジョギング", "テニス"],
        "correct": 0,
        "explain": "Lặn biển ngắm cá: 「ダイビング (scuba diving)」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Từ 「海」 có âm On là gì trong từ 「海外 (nước ngoài)」?",
        "options": ["かい", "うみ", "まい", "し"],
        "correct": 0,
        "explain": "海 trong 海外 (かいがい) đọc âm On là 「かい」."
    },
    {
        "id": 11,
        "category": "Hội thoại",
        "q": "「沖縄旅行は どうでしたか。」 ―― 「海が 青くて、とても [____] です。」",
        "options": ["きれいだった", "きれいくない", "きれいに", "きれい"],
        "correct": 0,
        "explain": "Khen phong cảnh biển trong chuyến đi đã qua: tính từ đuôi な ở quá khứ là 「きれいだった」."
    },
    {
        "id": 12,
        "category": "Từ vựng",
        "q": "心に 深く 残る 忘れられない 楽しい 記憶を [____] と 言います。",
        "options": ["おもいで", "おみやげ", "けしき", "じゅんび"],
        "correct": 0,
        "explain": "Kỷ niệm đẹp đáng nhớ là 「思い出 (おもいで)」."
    },
    {
        "id": 13,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「楽しい」 có nghĩa là gì?",
        "options": ["Vui vẻ", "Khó khăn", "Bận rộn", "Yên tĩnh"],
        "correct": 0,
        "explain": "楽しい (たのしい - LẠC) có nghĩa là vui vẻ."
    },
    {
        "id": 14,
        "category": "Ngữ pháp",
        "q": "巨大な ジンベエザメ（cá mập voi）を 近くで [____] ことが できました。",
        "options": ["見る", "見て", "見た", "見"],
        "correct": 0,
        "explain": "Có thể nhìn thấy tận mắt: V-る ことが できました ➔ 「見ることが できました」."
    },
    {
        "id": 15,
        "category": "Từ vựng",
        "q": "「沖縄へ 行くのは 今回が [____] ですか。」 ―― 「はい、初めてです。」",
        "options": ["何回目", "何人", "何時", "何分"],
        "correct": 0,
        "explain": "Hỏi lần thứ mấy: 「何回目 (なんかいめ)」."
    }
]
