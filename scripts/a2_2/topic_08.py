# -*- coding: utf-8 -*-
"""
Topic 8: せいかつとエコ (Life and Eco-friendly Activities)
- Lesson 15: ごみはビニール袋に入れます (We put garbage in plastic bags)
- Lesson 16: 毎日、水を使わない日があります (There are days when we don't use water every day)
"""

# =============================================================================
# LESSON 15 DATA
# =============================================================================
L15_VOCAB = [
    {
        "jp": "環境",
        "kana": "かんきょう",
        "kanji": "環境",
        "romaji": "kankyou",
        "vi": "Môi trường",
        "icon": "🌍"
    },
    {
        "jp": "エコ活動",
        "kana": "エコかつどう",
        "kanji": "エコ活動",
        "romaji": "eko katsudou",
        "vi": "Hoạt động thân thiện với môi trường",
        "icon": "🌱"
    },
    {
        "jp": "省エネ",
        "kana": "しょうエネ",
        "kanji": "省エネ",
        "romaji": "shouene",
        "vi": "Tiết kiệm năng lượng",
        "icon": "💡"
    },
    {
        "jp": "温度を上げます",
        "kana": "おんどをあげます",
        "kanji": "温度を上げます",
        "romaji": "ondo o agemasu",
        "vi": "Tăng nhiệt độ",
        "icon": "🌡️"
    },
    {
        "jp": "温度を下げます",
        "kana": "おんどをさげます",
        "kanji": "温度を下げます",
        "romaji": "ondo o sagemasu",
        "vi": "Giảm nhiệt độ",
        "icon": "❄️"
    },
    {
        "jp": "無駄にします",
        "kana": "むだにします",
        "kanji": "無駄にします",
        "romaji": "muda ni shimasu",
        "vi": "Làm lãng phí",
        "icon": "⚠️"
    },
    {
        "jp": "リサイクル",
        "kana": "リサイクル",
        "kanji": "リサイクル",
        "romaji": "risaikuru",
        "vi": "Tái chế",
        "icon": "♻️"
    },
    {
        "jp": "ごみを分けます",
        "kana": "ごみをわけます",
        "kanji": "ごみを分けます",
        "romaji": "gomi o wakemasu",
        "vi": "Phân loại rác",
        "icon": "🗂️"
    },
    {
        "jp": "ごみを減らします",
        "kana": "ごみをへらします",
        "kanji": "ごみを減らします",
        "romaji": "gomi o herashimasu",
        "vi": "Giảm bớt rác thải",
        "icon": "📉"
    },
    {
        "jp": "空気を汚します",
        "kana": "くうきをよごします",
        "kanji": "空気を汚します",
        "romaji": "kuuki o yogoshimasu",
        "vi": "Làm bẩn không khí",
        "icon": "🏭"
    },
    {
        "jp": "油を流します",
        "kana": "あぶらをながします",
        "kanji": "油を流します",
        "romaji": "abura o nagashimasu",
        "vi": "Xả dầu ăn từ nhà bếp",
        "icon": "🛢️"
    },
    {
        "jp": "空気をきれいにします",
        "kana": "くうきをきれいにします",
        "kanji": "空気をきれいにします",
        "romaji": "kuuki o kirei ni shimasu",
        "vi": "Làm sạch không khí",
        "icon": "🍃"
    },
    {
        "jp": "役に立ちます",
        "kana": "やくにたちます",
        "kanji": "役に立ちます",
        "romaji": "yaku ni tachimasu",
        "vi": "Có ích cho N (Nに役に立ちます)",
        "icon": "👍"
    },
    {
        "jp": "料理を残します",
        "kana": "りょうりをのこします",
        "kanji": "料理を残します",
        "romaji": "ryouri o nokoshimasu",
        "vi": "Bỏ lại, chừa lại thức ăn",
        "icon": "🍱"
    },
    {
        "jp": "ごみを捨てます",
        "kana": "ごみをすてます",
        "kanji": "ごみを捨てます",
        "romaji": "gomi o sutemasu",
        "vi": "Vứt rác",
        "icon": "🗑️"
    },
    {
        "jp": "ごみ箱",
        "kana": "ごみばこ",
        "kanji": "ごみ箱",
        "romaji": "gomibako",
        "vi": "Thùng rác",
        "icon": "🪣"
    },
    {
        "jp": "もったいない",
        "kana": "もったいない",
        "kanji": "もったいない",
        "romaji": "mottainai",
        "vi": "Lãng phí",
        "icon": "😣"
    },
    {
        "jp": "新聞紙",
        "kana": "しんぶんし",
        "kanji": "新聞紙",
        "romaji": "shinbunshi",
        "vi": "Giấy báo",
        "icon": "📰"
    },
    {
        "jp": "紙",
        "kana": "かみ",
        "kanji": "紙",
        "romaji": "kami",
        "vi": "Giấy",
        "icon": "📄"
    }
]

L15_VERBS = [
    {"masu": "すてます", "vi": "Vứt rác", "te": "すてて", "form1": "すてなければならない (phải vứt đúng nơi)", "form2": "すててはいけない (không được vứt)", "form3": "すてる"},
    {"masu": "わけます", "vi": "Phân chia", "te": "わけて", "form1": "わけてから出します", "form2": "わけなければならない (phải phân loại)", "form3": "わける"},
    {"masu": "だします", "vi": "Đem ra", "te": "だして", "form1": "朝8時までに出してください", "form2": "ださなくてもいい (không cần đem ra)", "form3": "だす"},
    {"masu": "まもります", "vi": "Tuân thủ", "te": "まもって", "form1": "ルールをまもってください", "form2": "まもった", "form3": "まもる"},
    {"masu": "へらします", "vi": "Cắt giảm", "te": "へらして", "form1": "ごみをへらしましょう", "form2": "へらした", "form3": "へらす"}
]

L15_KANJI_LIST = [
    {"stt": 1, "word": "分別", "kana": "ぶんべつ", "hv": "PHÂN BIỆT", "mean": "Phân loại"},
    {"stt": 2, "word": "燃える", "kana": "もえる", "hv": "NHIÊN", "mean": "Cháy được"},
    {"stt": 3, "word": "資源", "kana": "しげん", "hv": "TƯ NGUYÊN", "mean": "Tài nguyên"},
    {"stt": 4, "word": "捨てます", "kana": "すてます", "hv": "XẢ", "mean": "Vứt đi"},
    {"stt": 5, "word": "袋", "kana": "ふくろ", "hv": "ĐẠI", "mean": "Túi, bao"},
    {"stt": 6, "word": "曜日", "kana": "ようび", "hv": "DIỆU NHẬT", "mean": "Thứ trong tuần"},
    {"stt": 7, "word": "守ります", "kana": "まもります", "hv": "THỦ", "mean": "Bảo vệ, tuân thủ"},
    {"stt": 8, "word": "出します", "kana": "だします", "hv": "XUẤT", "mean": "Đem ra, nộp"}
]

L15_KANJI_CARDS = [
    {"char": "分", "hv": "Phân", "strokes": 4, "kun": "わ・ける、わ・かる", "on": "ぶん、ふん、ぶ", "ex": "分別 (ぶんべつ - phân loại), 分ける (わける - chia ra), 十分 (じゅうぶん - đầy đủ)", "mnemonic": "Cầm con dao (刀) bổ tám (八) phần chia đều là Phân chia."},
    {"char": "別", "hv": "Biệt", "strokes": 7, "kun": "わか・れる", "on": "べつ", "ex": "分別 (ぶんべつ - phân loại), 特別 (とくべつ - đặc biệt), 別の (べつの - cái khác)", "mnemonic": "Dùng dao (刂) rạch mở hộp xương (另) chia tách rạch ròi là Phân biệt."},
    {"char": "燃", "hv": "Nhiên", "strokes": 16, "kun": "も・える、も・やす", "on": "ねん", "ex": "燃える (もえる - cháy), 燃料 (ねんりょう - nhiên liệu)", "mnemonic": "Ngọn lửa (火) bén vào thịt nướng (然) bốc cháy rừng rực là Bốc cháy (Nhiên)."},
    {"char": "資", "hv": "Tư", "strokes": 13, "kun": "ー", "on": "し", "ex": "資源 (しげん - tài nguyên), 資料 (しりょう - tài liệu), 資本 (しほん - tư bản/vốn)", "mnemonic": "Tiền tài bảo vật (貝) dùng để trang trải thứ tiếp theo (次) là Tư bản, Tài nguyên."},
    {"char": "源", "hv": "Nguyên", "strokes": 13, "kun": "みなもと", "on": "げん", "ex": "資源 (しげん - tài nguyên), 語源 (ごげん - nguồn gốc từ), 電源 (でんげん - nguồn điện)", "mnemonic": "Dòng nước (氵) tuôn chảy ra từ cánh đồng trên cao (原) là Ngọn nguồn (Nguyên)."},
    {"char": "捨", "hv": "Xả", "strokes": 11, "kun": "す・てる", "on": "しゃ", "ex": "捨てる (すてる - vứt đi), 四捨五入 (ししゃごにゅう - làm tròn số)", "mnemonic": "Bàn tay (扌) buông bỏ đồ đạc trong gian nhà trọ (舍) là Xả bỏ, Vứt đi."},
    {"char": "袋", "hv": "Đại", "strokes": 11, "kun": "ふくろ", "on": "たい", "ex": "袋 (ふくろ - cái túi), 手袋 (てぶくろ - găng tay), ごみ袋 (ごみぶくろ - túi rác)", "mnemonic": "Tấm vải áo (衣) may thay thế (代) thành cái Túi đựng đồ (Đại)."},
    {"char": "守", "hv": "Thủ", "strokes": 6, "kun": "まも・る", "on": "しゅ、す", "ex": "守る (まもる - bảo vệ/tuân thủ), お守り (おまもり - bùa hộ mệnh), 留守 (るす - vắng nhà)", "mnemonic": "Dưới mái nhà (宀) bàn tay (寸) cẩn trọng trông coi gìn giữ là Canh thủ."}
]

L15_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>📜</span> 1. Quy Định Đời Sống: V-なければ なりません (Bắt buộc phải làm)</h2>
            <span class="section-tag">Luật phân loại rác</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Tại Nhật Bản, việc phân loại rác là nghĩa vụ bắt buộc của mọi cư dân trong khu phố:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #ef4444;">
                <div class="rule-formula" style="color: #991b1b;">
                    • [Động từ thể NAI (bỏ い)] ＋ なければ なりません (Phải làm V)<br>
                    • [Động từ thể NAI (bỏ い)] ＋ なくても いいです (Không cần làm V cũng được)
                </div>
                <div class="rule-meaning">
                    • <strong>ごみは ちゃんと 分別しなければ なりません:</strong> Phải phân loại rác cẩn thận.<br>
                    • <strong>指定の ごみ袋に 入れて 出さなければ なりません:</strong> Phải cho vào túi rác quy định rồi mới đem ra.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">燃えるごみは、火曜日と 金曜日の 朝8時までに 出さなければなりません。</div>
                        <div class="ex-vi">Rác cháy được thì phải đem ra trước 8 giờ sáng ngày thứ Ba và thứ Sáu.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('燃えるごみは、火曜日と金曜日の朝8時までに出さなければなりません')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🗑️</span> 2. Hướng Dẫn Vứt Rác Đúng Cách: N に 入れます / 出します</h2>
            <span class="section-tag">Quy trình rác tái chế</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • ペットボトルは ラベルと キャップを 取ってから 捨てます。<br>
                    • 中を 水で 洗ってから、資源ごみの 箱に 入れてください。
                </div>
            </div>
        </div>
    </section>'''
]

L15_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "ごみは ルールに 従って、きちんと 分別 [____] なりません。",
        "options": ["しなければ", "しないで", "したら", "しては"],
        "correct": 0,
        "explain": "Bắt buộc phải làm: V-なければなりません ➔ しません ➔ 「しなければ」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "この日は 瓶（びん）の 日ですから、缶は [____] いいです。",
        "options": ["出さなくても", "出さなければ", "出さないで", "出して"],
        "correct": 0,
        "explain": "Không cần làm cũng được: V-なくてもいいです ➔ 「出さなくても」."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "生ごみや 紙くずなどの 燃やすことが できる ごみは [____] です。",
        "options": ["もえるごみ", "もえないごみ", "しげんごみ", "そだいごみ"],
        "correct": 0,
        "explain": "Rác cháy được là 「燃えるごみ (もえるごみ)」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「分別」 có cách đọc chuẩn là gì?",
        "options": ["ぶんべつ", "ふんべつ", "わけべつ", "ぶんわけ"],
        "correct": 0,
        "explain": "分別 đọc là 「ぶんべつ」 (PHÂN BIỆT - phân loại rác)."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "清涼飲料水や お茶が 入っている プラスチックの ボトルは [____] です。",
        "options": ["ペットボトル", "ビニール袋", "かん", "びん"],
        "correct": 0,
        "explain": "Chai nhựa đựng trà/nước là 「ペットボトル (PET bottle)」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Từ 「捨てます (すてます)」 có nghĩa là gì?",
        "options": ["Vứt rác đi", "Nhặt rác lên", "Mua đồ", "Đổi hàng"],
        "correct": 0,
        "explain": "捨てる (すてる - XẢ) có nghĩa là vứt bỏ."
    },
    {
        "id": 7,
        "category": "Hội thoại",
        "q": "まだ 使える 物を 簡単に 捨ててしまうのは [____] です。",
        "options": ["もったいない", "すばらしい", "にぎやか", "しずか"],
        "correct": 0,
        "explain": "Lãng phí tiếc của: 「もったいない」."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Từ 「資源」 có âm Hán Việt là gì?",
        "options": ["TƯ NGUYÊN", "TƯ LIỆU", "TỰ NGUYÊN", "TƯ BẢN"],
        "correct": 0,
        "explain": "資源 có âm Hán Việt là TƯ NGUYÊN (tài nguyên)."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "スーパーの レジ袋を もらわないで、自分の [____] を 使います。",
        "options": ["エコバッグ", "ペットボトル", "メニュー", "ガイドブック"],
        "correct": 0,
        "explain": "Túi vải dùng nhiều lần để bảo vệ môi trường: 「エコバッグ (eco-bag)」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「守る」 đọc là gì?",
        "options": ["まもる", "すてる", "わける", "へらす"],
        "correct": 0,
        "explain": "守る đọc là 「まもる」 (THỦ - tuân thủ quy tắc)."
    },
    {
        "id": 11,
        "category": "Ngữ pháp",
        "q": "ペットボトルを 捨てるときは、キャップを [____] から 捨ててください。",
        "options": ["はずして", "はずす", "はずした", "はずし"],
        "correct": 0,
        "explain": "Trình tự: tháo nắp ra xong rồi mới vứt ➔ V-てから: 「はずして」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「袋」 trong 「ビニール袋」 có nghĩa là gì?",
        "options": ["Cái túi", "Cái chai", "Cái hộp", "Tờ giấy"],
        "correct": 0,
        "explain": "袋 (ふくろ - ĐẠI) nghĩa là cái bao, cái túi."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "一度 使った 物を もう一度 使えるように 加工することを [____] と 言います。",
        "options": ["リサイクル", "アレルギー", "サプライズ", "メッセージ"],
        "correct": 0,
        "explain": "Tái chế đồ phế liệu: 「リサイクル (recycle)」."
    },
    {
        "id": 14,
        "category": "Hội thoại",
        "q": "「ごみは どこに [____] いいですか。」 ―― 「あそこの 集積場ですよ。」",
        "options": ["出したら", "出せば", "出したらば", "出すなら"],
        "correct": 0,
        "explain": "Nên đem rác ra đâu thì tốt: V-たらいいですか ➔ 「出したらいいですか」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「燃える」 có âm Hán Việt là gì?",
        "options": ["NHIÊN", "HỎA", "TIÊU", "THIÊU"],
        "correct": 0,
        "explain": "燃える có âm Hán Việt là NHIÊN (bùng cháy)."
    }
]


# =============================================================================
# LESSON 16 DATA
# =============================================================================
L16_VOCAB = [
    {
        "jp": "フリーマーケット",
        "kana": "フリーマーケット",
        "kanji": "フリーマーケット",
        "romaji": "furi-ma-ketto",
        "vi": "Hội chợ (đồ cũ)",
        "icon": "🎪"
    },
    {
        "jp": "レンタルショップ",
        "kana": "レンタルショップ",
        "kanji": "レンタルショップ",
        "romaji": "rentaru shoppu",
        "vi": "Cửa hàng đồ cho thuê",
        "icon": "🏬"
    },
    {
        "jp": "クッション",
        "kana": "クッション",
        "kanji": "クッション",
        "romaji": "kusshon",
        "vi": "Gối",
        "icon": "🛋️"
    },
    {
        "jp": "ふとん",
        "kana": "ふとん",
        "kanji": "布団",
        "romaji": "futon",
        "vi": "Chăn, nệm",
        "icon": "🛏️"
    },
    {
        "jp": "エコバッグ",
        "kana": "エコバッグ",
        "kanji": "エコバッグ",
        "romaji": "ekobaggu",
        "vi": "Túi thân thiện môi trường",
        "icon": "🛍️"
    },
    {
        "jp": "ベビーベッド",
        "kana": "ベビーベッド",
        "kanji": "ベビーベッド",
        "romaji": "bebi-beddo",
        "vi": "Giường em bé",
        "icon": "👶"
    },
    {
        "jp": "ベビーカー",
        "kana": "ベビーカー",
        "kanji": "ベビーカー",
        "romaji": "bebi-ka-",
        "vi": "Xe đẩy em bé",
        "icon": "🛒"
    },
    {
        "jp": "飽きます",
        "kana": "あきます",
        "kanji": "飽きます",
        "romaji": "akimasu",
        "vi": "Chán (ngấy)",
        "icon": "🥱"
    },
    {
        "jp": "変わります",
        "kana": "かわります",
        "kanji": "変わります",
        "romaji": "kawarimasu",
        "vi": "(N) Thay đổi (Nが変わります)",
        "icon": "🔄"
    },
    {
        "jp": "要ります／必要（な）",
        "kana": "いります／ひつよう（な）",
        "kanji": "要ります／必要（な）",
        "romaji": "irimasu / hitsuyou(na)",
        "vi": "Cần thiết (V)",
        "icon": "✅"
    },
    {
        "jp": "要りません",
        "kana": "いりません",
        "kanji": "要りません",
        "romaji": "irimasen",
        "vi": "Không cần thiết (V)",
        "icon": "❌"
    },
    {
        "jp": "スーツケースを借ります",
        "kana": "スーツケースをかります",
        "kanji": "スーツケースを借ります",
        "romaji": "su-tsuke-su o karimasu",
        "vi": "Mượn vali ở cửa hàng thuê đồ",
        "icon": "🧳"
    },
    {
        "jp": "増えます",
        "kana": "ふえます",
        "kanji": "増えます",
        "romaji": "fuemasu",
        "vi": "N tăng lên (Nが増えます)",
        "icon": "📈"
    },
    {
        "jp": "破れます／破ります",
        "kana": "やぶれます／やぶります",
        "kanji": "破れます／破ります",
        "romaji": "yaburemasu / yaburimasu",
        "vi": "Rách",
        "icon": "📃"
    },
    {
        "jp": "汚れます／汚します",
        "kana": "よごれます／よごします",
        "kanji": "汚れます／汚します",
        "romaji": "yogoremasu / yogoshimasu",
        "vi": "Bị bẩn",
        "icon": "🧼"
    },
    {
        "jp": "修理します／直します",
        "kana": "しゅうりします／なおします",
        "kanji": "修理します／直します",
        "romaji": "shuuri shimasu / naoshimasu",
        "vi": "Sửa chữa N",
        "icon": "🔧"
    },
    {
        "jp": "穴が開きます",
        "kana": "あながあきます",
        "kanji": "穴が開きます",
        "romaji": "ana ga akimasu",
        "vi": "Thủng lỗ",
        "icon": "🕳️"
    },
    {
        "jp": "ごみを拾います",
        "kana": "ごみをひろいます",
        "kanji": "ごみを拾います",
        "romaji": "gomi o hiroimasu",
        "vi": "Nhặt rác",
        "icon": "🧹"
    }
]

L16_VERBS = [
    {"masu": "せつやくします", "vi": "Tiết kiệm", "te": "せつやくして", "form1": "せつやくするようにしています (cố gắng tiết kiệm)", "form2": "せつやくした", "form3": "せつやくする"},
    {"masu": "けします", "vi": "Tắt điện", "te": "けして", "form1": "けすようにしています (luôn nhớ tắt)", "form2": "けした", "form3": "けす"},
    {"masu": "とめます", "vi": "Khóa vòi nước", "te": "とめて", "form1": "こまめにとめましょう", "form2": "とめた", "form3": "とめる"},
    {"masu": "つづけます", "vi": "Tiếp tục duy trì", "te": "つづけて", "form1": "まいにちつづける (duy trì mỗi ngày)", "form2": "つづけた", "form3": "つづける"},
    {"masu": "つかいます", "vi": "Dùng", "te": "つかって", "form1": "つかわない日 (ngày không dùng)", "form2": "つかった", "form3": "つかう"}
]

L16_KANJI_LIST = [
    {"stt": 1, "word": "節約", "kana": "せつやく", "hv": "TIẾT ƯỚC", "mean": "Tiết kiệm"},
    {"stt": 2, "word": "水道", "kana": "すいどう", "hv": "THỦY ĐẠO", "mean": "Nước máy"},
    {"stt": 3, "word": "環境", "kana": "かんきょう", "hv": "HOÀN CẢNH", "mean": "Môi trường"},
    {"stt": 4, "word": "自然", "kana": "しぜん", "hv": "TỰ NHIÊN", "mean": "Thiên nhiên"},
    {"stt": 5, "word": "地球", "kana": "ちきゅう", "hv": "ĐỊA CẦU", "mean": "Trái đất"},
    {"stt": 6, "word": "習慣", "kana": "しゅうかん", "hv": "TẬP QUÁN", "mean": "Thói quen"},
    {"stt": 7, "word": "大切", "kana": "たいせつ", "hv": "ĐẠI THIẾT", "mean": "Quan trọng"},
    {"stt": 8, "word": "階段", "kana": "かいだん", "hv": "GIAI ĐOẠN", "mean": "Cầu thang bộ"}
]

L16_KANJI_CARDS = [
    {"char": "節", "hv": "Tiết", "strokes": 13, "kun": "ふし", "on": "せつ", "ex": "節約 (せつやく - tiết kiệm), 季節 (きせつ - mùa trong năm), 調節 (ちょうせつ - điều tiết)", "mnemonic": "Đốt tre (竹) ngay ngắn có chừng mực ước chế (即) là Tiết độ, Tiết kiệm."},
    {"char": "道", "hv": "Đạo", "strokes": 12, "kun": "みち", "on": "どう、とう", "ex": "水道 (すいどう - nước máy), 道路 (どうろ - con đường), 書道 (しょどう - thư đạo)", "mnemonic": "Bước chân đi (辶) theo sự dẫn đường của khối óc lãnh đạo (首) là Con đường (Đạo)."},
    {"char": "環", "hv": "Hoàn", "strokes": 17, "kun": "ー", "on": "かん", "ex": "環境 (かんきょう - môi trường), 循環 (じゅんかん - tuần hoàn)", "mnemonic": "Chiếc vòng ngọc quý (王) bao quanh nhìn ngắm say sưa là Tuần hoàn."},
    {"char": "境", "hv": "Cảnh", "strokes": 14, "kun": "さかい", "on": "きょう、けい", "ex": "環境 (かんきょう - môi trường), 国境 (こっきょう - biên giới), 境 (さかい - ranh giới)", "mnemonic": "Vùng đất đai (土) có ánh sáng (竟) phân định rõ bờ cõi là Ranh giới, Địa cảnh."},
    {"char": "然", "hv": "Nhiên", "strokes": 12, "kun": "ー", "on": "ぜん、ねん", "ex": "自然 (しぜん - tự nhiên), 当然 (とうぜん - đương nhiên), 全然 (ぜんぜん - hoàn toàn)", "mnemonic": "Thịt thú (⺼) đem nướng trên than lửa (灬) chín tự nhiên như bản chất vốn có (Nhiên)."},
    {"char": "球", "hv": "Cầu", "strokes": 11, "kun": "たま", "on": "きゅう", "ex": "地球 (ちきゅう - trái đất), 野球 (やきゅう - bóng chày), 電球 (でんきゅう - bóng đèn)", "mnemonic": "Viên ngọc quý (王) hình tròn cầu để cầu cứu (求) là Quả cầu."},
    {"char": "習", "hv": "Tập", "strokes": 11, "kun": "なら・う", "on": "しゅう", "ex": "習慣 (しゅうかん - thói quen), 練習 (れんしゅう - luyện tập), 復習 (ふくしゅう - ôn tập)", "mnemonic": "Đôi cánh chim non (羽) trắng muốt (白) tập vỗ nhiều lần để bay lượn là Học tập."},
    {"char": "段", "hv": "Đoạn", "strokes": 9, "kun": "ー", "on": "だん", "ex": "階段 (かいだん - cầu thang), 段階 (だんかい - giai đoạn), 手段 (しゅだん - thủ đoạn/phương tiện)", "mnemonic": "Dùng búa rìu (殳) đẽo từng tấc đá trên vách đứng tạo nên từng Bậc thang (Đoạn)."}
]

L16_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>🌱</span> 1. Thói Quen Tiết Kiệm: V-る / V-ない ように しています</h2>
            <span class="section-tag">Thói quen sống xanh</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để diễn tả sự nỗ lực duy trì một thói quen tốt hàng ngày bảo vệ môi trường và tiết kiệm năng lượng:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • [V thể Từ điển] ＋ ように しています (Cố gắng tạo thói quen làm V)<br>
                    • [V thể NAI] ＋ ように しています (Cố gắng không làm V)
                </div>
                <div class="rule-meaning">
                    • <strong>部屋を 出るときは、電気を 消すように しています:</strong> Tôi luôn cố gắng tắt đèn mỗi khi ra khỏi phòng.<br>
                    • <strong>歯を みがくときは、水を 出しっぱなしに しないように しています:</strong> Cố gắng không xả nước lãng phí khi đánh răng.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">ペットボトルの ゴミを 減らすために、マイボトルを 持っていくように しています。</div>
                        <div class="ex-vi">Để cắt giảm rác chai nhựa, tôi luôn duy trì thói quen mang theo bình nước cá nhân.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('ペットボトルのゴミを減らすために、マイボトルを持っていくようにしています')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>💧</span> 2. Mệnh Đề Định Ngữ Chỉ Ngày Đặc Biệt: [V-thể thông thường] ＋ 日</h2>
            <span class="section-tag">Lối sống Eco</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • 水を 使わない 日 (Ngày không dùng nước)<br>
                    • 車を 運転しない 日 (Ngày không lái xe - đi bộ hoặc xe bus)
                </div>
            </div>
        </div>
    </section>'''
]

L16_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "部屋を 出るときは、必ず 電気を [____] ように しています。",
        "options": ["消す", "消して", "消した", "消し"],
        "correct": 0,
        "explain": "Cố gắng duy trì thói quen làm gì: 『V thể từ điển + ようにしています』 ➔ 「消す」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "健康と 節電の ために、エレベーターを [____] で 階段を 使っています。",
        "options": ["使わない", "使った", "使う", "使って"],
        "correct": 0,
        "explain": "Không dùng thang máy: 『使わないで』 (thể NAI + で)."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "電気や 水を むだに 使わないで 大切に 使うことを [____] と 言います。",
        "options": ["せつやく", "しゅうかん", "かんきょう", "しぜん"],
        "correct": 0,
        "explain": "Tiết kiệm năng lượng: 「節約 (せつやく)」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「環境」 có âm Hán Việt là gì?",
        "options": ["HOÀN CẢNH", "HOÀN THÀNH", "ĐỊA CẢNH", "HOÀN ĐỊA"],
        "correct": 0,
        "explain": "環境 có âm Hán Việt là HOÀN CẢNH (môi trường)."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "私たちが 住んでいる 青い 星は [____] です。",
        "options": ["ちきゅう", "かいだん", "すいどう", "ガス"],
        "correct": 0,
        "explain": "Trái đất hành tinh xanh là 「地球 (ちきゅう)」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Từ 「自然」 có cách đọc chuẩn là gì?",
        "options": ["しぜん", "じぜん", "しねん", "じねん"],
        "correct": 0,
        "explain": "自然 đọc là 「しぜん」 (TỰ NHIÊN)."
    },
    {
        "id": 7,
        "category": "Hội thoại",
        "q": "「マイボトルを 持ち歩くのは なぜですか。」 ―― 「プラスチックごみを [____] ためです。」",
        "options": ["減らす", "増やす", "残す", "買う"],
        "correct": 0,
        "explain": "Để cắt giảm rác thải: 「減らす (へらす) ためです」."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「水道」 gồm 2 chữ nào?",
        "options": ["THỦY + ĐẠO", "THỦY + ĐƯỜNG", "HẢI + ĐẠO", "THỦY + THIỆN"],
        "correct": 0,
        "explain": "水道 gồm THỦY (水) và ĐẠO (道) ➔ hệ thống nước máy."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "地球全体の 気温が 徐々に 上がってしまう 環境問題は 地球[____] です。",
        "options": ["おんだんか", "しゅうかん", "せつやく", "かいだん"],
        "correct": 0,
        "explain": "Ấm lên toàn cầu: 「地球温暖化 (ちきゅうおんだんか)」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「階段」 đọc là gì?",
        "options": ["かいだん", "かいどう", "はしご", "けいだん"],
        "correct": 0,
        "explain": "階段 đọc là 「かいだん」 (GIAI ĐOẠN - cầu thang)."
    },
    {
        "id": 11,
        "category": "Ngữ pháp",
        "q": "歯を みがいている 間は、水道の 水を [____] ください。",
        "options": ["止めて", "止めてから", "止めたら", "止める"],
        "correct": 0,
        "explain": "Hãy khóa vòi nước: 止めます ➔ thể TE: 「止めてください」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「大切」 có nghĩa là gì?",
        "options": ["Quan trọng, trân quý", "Rất to lớn", "Rất nguy hiểm", "Cắt rời ra"],
        "correct": 0,
        "explain": "大切 (たいせつ) nghĩa là quan trọng, trân quý."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "毎日 繰り返し 行う 行動の 決まりを [____] と 呼びます。",
        "options": ["しゅうかん", "ちきゅう", "おんだんか", "ざんしょく"],
        "correct": 0,
        "explain": "Thói quen hàng ngày là 「習慣 (しゅうかん)」."
    },
    {
        "id": 14,
        "category": "Hội thoại",
        "q": "食べ残し（たべのこし）を 出さないように、食べられる 分だけ [____] ように しています。",
        "options": ["注文する", "注文しない", "注文して", "注文した"],
        "correct": 0,
        "explain": "Cố gắng chỉ gọi đủ phần ăn: 「注文するようにしています」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「節」 trong 「節約」 có âm Hán Việt là gì?",
        "options": ["TIẾT", "TRÚC", "TỨC", "KẾT"],
        "correct": 0,
        "explain": "節 có âm Hán Việt là TIẾT (tiết chế, tiết kiệm)."
    }
]
