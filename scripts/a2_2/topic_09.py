# -*- coding: utf-8 -*-
"""
Topic 9: じんせい (People's Lives / Cuộc đời & Kế hoạch tương lai)
- Lesson 17: この人、知っていますか (Do you know this person?)
- Lesson 18: どんな子どもでしたか (What kind of child were you?)
"""

# =============================================================================
# LESSON 17 DATA
# =============================================================================
L17_VOCAB = [
    {
        "jp": "人生",
        "kana": "じんせい",
        "kanji": "人生",
        "romaji": "jinsei",
        "vi": "Cuộc đời, đời người",
        "icon": "🌱"
    },
    {
        "jp": "俳優",
        "kana": "はいゆう",
        "kanji": "俳優",
        "romaji": "haiyuu",
        "vi": "Diễn viên nam",
        "icon": "🎭"
    },
    {
        "jp": "女優",
        "kana": "じょゆう",
        "kanji": "女優",
        "romaji": "joyuu",
        "vi": "Diễn viên nữ",
        "icon": "🎬"
    },
    {
        "jp": "音楽家",
        "kana": "おんがくか",
        "kanji": "音楽家",
        "romaji": "ongakuka",
        "vi": "Nhạc sĩ",
        "icon": "🎼"
    },
    {
        "jp": "画家",
        "kana": "がか",
        "kanji": "画家",
        "romaji": "gaka",
        "vi": "Họa sĩ",
        "icon": "🎨"
    },
    {
        "jp": "作家",
        "kana": "さっか",
        "kanji": "作家",
        "romaji": "sakka",
        "vi": "Nhà văn",
        "icon": "🖋️"
    },
    {
        "jp": "小説家",
        "kana": "しょうせつか",
        "kanji": "小説家",
        "romaji": "shousetsuka",
        "vi": "Tiểu thuyết gia",
        "icon": "📚"
    },
    {
        "jp": "スポーツ選手",
        "kana": "スポーツせんしゅ",
        "kanji": "スポーツ選手",
        "romaji": "supo-tsu senshu",
        "vi": "Tuyển thủ thể thao",
        "icon": "⚽"
    },
    {
        "jp": "柔道家",
        "kana": "じゅうどうか",
        "kanji": "柔道家",
        "romaji": "juudouka",
        "vi": "Võ sĩ judo",
        "icon": "🥋"
    },
    {
        "jp": "映画監督",
        "kana": "えいがかんとく",
        "kanji": "映画監督",
        "romaji": "eiga kantoku",
        "vi": "Đạo diễn phim",
        "icon": "🎥"
    },
    {
        "jp": "科学者",
        "kana": "かがくしゃ",
        "kanji": "科学者",
        "romaji": "kagakusha",
        "vi": "Nhà khoa học",
        "icon": "🔬"
    },
    {
        "jp": "教育者",
        "kana": "きょういくしゃ",
        "kanji": "教育者",
        "romaji": "kyouikusha",
        "vi": "Nhà giáo dục học",
        "icon": "👨‍🏫"
    },
    {
        "jp": "バイオリニスト",
        "kana": "バイオリニスト",
        "kanji": "バイオリニスト",
        "romaji": "baiorinisuto",
        "vi": "Nghệ sĩ Violin",
        "icon": "🎻"
    },
    {
        "jp": "大ファン",
        "kana": "だいファン",
        "kanji": "大ファン",
        "romaji": "dai fan",
        "vi": "Fan bự",
        "icon": "🤩"
    },
    {
        "jp": "金メダル",
        "kana": "きんメダル",
        "kanji": "金メダル",
        "romaji": "kin medaru",
        "vi": "Huy chương vàng",
        "icon": "🥇"
    },
    {
        "jp": "～賞",
        "kana": "～しょう",
        "kanji": "～賞",
        "romaji": "~shou",
        "vi": "Giải thưởng",
        "icon": "🏆"
    },
    {
        "jp": "翻訳（します）",
        "kana": "ほんやく（します）",
        "kanji": "翻訳（します）",
        "romaji": "honyaku(shimasu)",
        "vi": "Biên dịch",
        "icon": "📝"
    },
    {
        "jp": "活躍（します）",
        "kana": "かつやく（します）",
        "kanji": "活躍（します）",
        "romaji": "katsuyaku(shimasu)",
        "vi": "Thành công, hoạt động sôi nổi",
        "icon": "🌟"
    },
    {
        "jp": "亡くなります",
        "kana": "なくなります",
        "kanji": "亡くなります",
        "romaji": "nakunarimasu",
        "vi": "Qua đời",
        "icon": "🕊️"
    },
    {
        "jp": "作品",
        "kana": "さくひん",
        "kanji": "作品",
        "romaji": "sakuhin",
        "vi": "Tác phẩm",
        "icon": "🖼️"
    },
    {
        "jp": "太陽",
        "kana": "たいよう",
        "kanji": "太陽",
        "romaji": "taiyou",
        "vi": "Mặt trời",
        "icon": "☀️"
    },
    {
        "jp": "呼びます",
        "kana": "よびます",
        "kanji": "呼びます",
        "romaji": "yobimasu",
        "vi": "Gọi",
        "icon": "🗣️"
    },
    {
        "jp": "ずっと",
        "kana": "ずっと",
        "kanji": "ずっと",
        "romaji": "zutto",
        "vi": "Suốt, mãi",
        "icon": "⏳"
    },
    {
        "jp": "辞めます／やめます",
        "kana": "やめます",
        "kanji": "辞めます",
        "romaji": "yamemasu",
        "vi": "Bỏ N, Từ bỏ N",
        "icon": "🛑"
    },
    {
        "jp": "離婚します",
        "kana": "りこんします",
        "kanji": "離婚します",
        "romaji": "rikon shimasu",
        "vi": "Ly hôn",
        "icon": "💔"
    },
    {
        "jp": "びっくりしました",
        "kana": "びっくりしました",
        "kanji": "びっくりしました",
        "romaji": "bikkuri shimashita",
        "vi": "Bất ngờ",
        "icon": "😲"
    },
    {
        "jp": "貧しい",
        "kana": "まずしい",
        "kanji": "貧しい",
        "romaji": "mazushii",
        "vi": "Nghèo, thiếu thốn",
        "icon": "🏚️"
    },
    {
        "jp": "苦労します",
        "kana": "くろうします",
        "kanji": "苦労します",
        "romaji": "kurou shimasu",
        "vi": "Gặp khó khăn, vất vả",
        "icon": "🧗"
    },
    {
        "jp": "首相",
        "kana": "しゅしょう",
        "kanji": "首相",
        "romaji": "shushou",
        "vi": "Thủ tướng",
        "icon": "🏛️"
    },
    {
        "jp": "大統領",
        "kana": "だいとうりょう",
        "kanji": "大統領",
        "romaji": "daitouryou",
        "vi": "Tổng thống",
        "icon": "🇺🇸"
    },
    {
        "jp": "政治家",
        "kana": "せいじか",
        "kanji": "政治家",
        "romaji": "seijika",
        "vi": "Chính trị gia",
        "icon": "👔"
    },
    {
        "jp": "実業家",
        "kana": "じつぎょうか",
        "kanji": "実業家",
        "romaji": "jitsugyouka",
        "vi": "Doanh nhân, nhà kinh doanh",
        "icon": "💼"
    }
]

L17_VERBS = [
    {"masu": "うまれます", "vi": "Được sinh ra", "te": "うまれて", "form1": "うまれました (đã sinh ra tại)", "form2": "うまれたあとで", "form3": "うまれる"},
    {"masu": "そだちます", "vi": "Lớn lên", "te": "そだって", "form1": "そだちました (đã lớn lên tại)", "form2": "そだったところ", "form3": "そだつ"},
    {"masu": "せいこうします", "vi": "Thành công", "te": "せいこうして", "form1": "せいこうした (đã thành công)", "form2": "せいこうするまで", "form3": "せいこうする"},
    {"masu": "どりょくします", "vi": "Nỗ lực", "te": "どりょくして", "form1": "どりょくをつづけた (tiếp tục nỗ lực)", "form2": "どりょくした", "form3": "どりょくする"},
    {"masu": "かつやくします", "vi": "Hoạt động tích cực", "te": "かつやくして", "form1": "かつやくしています", "form2": "かつやくした", "form3": "かつやくする"}
]

L17_KANJI_LIST = [
    {"stt": 1, "word": "人生", "kana": "じんせい", "hv": "NHÂN SINH", "mean": "Cuộc đời"},
    {"stt": 2, "word": "育ちます", "kana": "そだちます", "hv": "DỤC", "mean": "Lớn lên"},
    {"stt": 3, "word": "成功", "kana": "せいこう", "hv": "THÀNH CÔNG", "mean": "Thành công"},
    {"stt": 4, "word": "努力", "kana": "どりょく", "hv": "NỖ LỰC", "mean": "Nỗ lực, cố gắng"},
    {"stt": 5, "word": "夢", "kana": "ゆめ", "hv": "MỘNG", "mean": "Ước mơ"},
    {"stt": 6, "word": "科学者", "kana": "かがくしゃ", "hv": "KHOA HỌC GIẢ", "mean": "Nhà khoa học"},
    {"stt": 7, "word": "作品", "kana": "さくひん", "hv": "TÁC PHẨM", "mean": "Tác phẩm"},
    {"stt": 8, "word": "世界", "kana": "せかい", "hv": "THẾ GIỚI", "mean": "Thế giới"}
]

L17_KANJI_CARDS = [
    {"char": "生", "hv": "Sinh", "strokes": 5, "kun": "い・きる、う・まれる", "on": "せい、しょう", "ex": "人生 (じんせい - nhân sinh), 生まれる (うまれる - sinh ra), 先生 (せんせい - giáo viên)", "mnemonic": "Mầm cây xanh nhú lên từ lòng đất đâm chồi nảy lộc là Sự sống (Sinh)."},
    {"char": "育", "hv": "Dục", "strokes": 8, "kun": "そだ・つ、そだ・てる", "on": "いく", "ex": "育つ (そだつ - lớn lên), 教育 (きょういく - giáo dục), 体育 (たいいく - thể dục)", "mnemonic": "Nuôi nấng đứa trẻ sơ sinh (充) cho ăn đầy đủ thịt mỡ (月 - nhục) là Nuôi dưỡng."},
    {"char": "功", "hv": "Công", "strokes": 5, "kun": "ー", "on": "こう、く", "ex": "成功 (せいこう - thành công), 功績 (こうせき - công tích/thành quả)", "mnemonic": "Dùng sức lực (力) thực hiện công việc (工) hoàn thành mỹ mãn là Công trạng."},
    {"char": "努", "hv": "Nỗ", "strokes": 7, "kun": "つと・める", "on": "ど", "ex": "努力 (どりょく - nỗ lực), 勉める (つとめる - gắng sức)", "mnemonic": "Con người như nô bộc (奴) dốc hết toàn bộ sức lực (力) là Nỗ lực."},
    {"char": "力", "hv": "Lực", "strokes": 2, "kun": "ちから", "on": "りょく、りき", "ex": "努力 (どりょく - nỗ lực), 力 (ちから - sức mạnh), 能力 (のうりょく - năng lực)", "mnemonic": "Hình cánh tay cơ bắp gồng lên tràn đầy Sức lực."},
    {"char": "夢", "hv": "Mộng", "strokes": 13, "kun": "ゆめ", "on": "む", "ex": "夢 (ゆめ - giấc mơ/hoài bão), 悪夢 (あくむ - ác mộng)", "mnemonic": "Dưới bóng cây cỏ đêm tối (艹 + 罒) con người ngắm trăng (夕) mơ màng là Giấc mộng."},
    {"char": "界", "hv": "Giới", "strokes": 9, "kun": "ー", "on": "かい", "ex": "世界 (せかい - thế giới), 限界 (げんかい - giới hạn), 業界 (ぎょうかい - ngành nghề)", "mnemonic": "Khu ruộng (田) có cắm cọc phân định rõ ranh giới (介) là Ranh giới, Thế giới."},
    {"char": "品", "hv": "Phẩm", "strokes": 9, "kun": "しな", "on": "ひん", "ex": "作品 (さくひん - tác phẩm), 商品 (しょうひん - hàng hóa), 部品 (ぶひん - linh kiện)", "mnemonic": "Ba chiếc miệng (口) cùng ăn nếm và đánh giá chất lượng của Vật phẩm."}
]

L17_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>📜</span> 1. Kể Lại Tiểu Sử Cuộc Đời: ～で 生まれ、～で 育ちました</h2>
            <span class="section-tag">Tiểu sử danh nhân</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để tóm tắt các chặng đường quan trọng trong cuộc đời của một người nổi tiếng hoặc tác giả yêu thích:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • [Nơi chốn] で 生まれ、[Nơi chốn] で 育ちました。<br>
                    • [Động từ thể TA] ＋ あとで、～ (Sau khi...)
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">手塚治虫は 大阪で 生まれ、兵庫県で 育ちました。</div>
                        <div class="ex-vi">Tezuka Osamu (ông tổ truyện tranh Nhật) sinh ra ở Osaka và lớn lên tại tỉnh Hyogo.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('手塚治虫は大阪で生まれ、兵庫県で育ちました')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">大学を 卒業した あとで、アニメの 会社を 作りました。</div>
                        <div class="ex-vi">Sau khi tốt nghiệp đại học, ông đã thành lập công ty sản xuất phim hoạt hình.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('大学を卒業したあとで、アニメの会社を作りました')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🌟</span> 2. Tác Phẩm Được Yêu Thích Toàn Cầu: ～に 愛されています</h2>
            <span class="section-tag">Bị động mang ý nghĩa tích cực</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • 彼の 作品は 世界中の 人々に 読まれています / 愛されています。<br>
                    (Tác phẩm của ông được mọi người khắp thế giới đón đọc / yêu mến)
                </div>
            </div>
        </div>
    </section>'''
]

L17_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "宮崎駿監督の 映画は、世界中で たくさんの 人に [____] います。",
        "options": ["愛されて", "愛して", "愛した", "愛する"],
        "correct": 0,
        "explain": "Được mọi người yêu mến (thể bị động): 愛します ➔ 「愛されて」 います."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "高校を 卒業 [____] あとで、日本へ 留学しました。",
        "options": ["した", "して", "する", "したら"],
        "correct": 0,
        "explain": "Sau khi làm gì: 『V thể TA + あとで』 ➔ 「卒業したあとで」."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "ドラえもんなどの 漫画を 描く 職業の 人は [____] です。",
        "options": ["まんがか", "かがくしゃ", "さっか", "かしゅ"],
        "correct": 0,
        "explain": "Họa sĩ vẽ truyện tranh là 「漫画家 (まんがか)」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「成功」 có cách đọc là gì?",
        "options": ["せいこう", "じょうこう", "せいごう", "しょうこう"],
        "correct": 0,
        "explain": "成功 đọc là 「せいこう」 (THÀNH CÔNG)."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "あきらめずに 毎日 こつこつと [____] した 結果、夢が かないました。",
        "options": ["どりょく", "しっぱい", "せいこう", "かつやく"],
        "correct": 0,
        "explain": "Nỗ lực kiên trì không bỏ cuộc: 「努力 (どりょく) した」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Từ 「人生」 có âm Hán Việt là gì?",
        "options": ["NHÂN SINH", "NHÂN THỜI", "NHÂN ĐẠI", "DÂN SINH"],
        "correct": 0,
        "explain": "人生 có âm Hán Việt là NHÂN SINH (cuộc đời con người)."
    },
    {
        "id": 7,
        "category": "Hội thoại",
        "q": "「この 人、[____] か。」 ―― 「ええ、ノーベル賞を 取った 科学者ですね。」",
        "options": ["知っています", "分かりました", "知恵があります", "覚えます"],
        "correct": 0,
        "explain": "Hỏi có biết người này không: 「知っていますか」."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「育つ」 đọc là gì?",
        "options": ["そだつ", "たつ", "かつ", "うつ"],
        "correct": 0,
        "explain": "育つ đọc là 「そだつ」 (DỤC - lớn lên, khôn lớn)."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "将来 やりたい ことや 目指している 希望は [____] です。",
        "options": ["ゆめ", "しっぱい", "えいきょう", "しょうがい"],
        "correct": 0,
        "explain": "Giấc mơ, ước mơ tương lai: 「夢 (ゆめ)」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「世界」 gồm 2 chữ nào?",
        "options": ["THẾ + GIỚI", "THỜI + GIỚI", "THẾ + ĐỊA", "THẾ + QUỐC"],
        "correct": 0,
        "explain": "世界 gồm THẾ (世) và GIỚI (界) ➔ thế giới toàn cầu."
    },
    {
        "id": 11,
        "category": "Ngữ pháp",
        "q": "田中さんは 東京で [____]、京都で 育ちました。",
        "options": ["生まれ", "生まれる", "生まれた", "生まれて"],
        "correct": 0,
        "explain": "Liên kết câu dạng văn viết trang trọng: 生まれます ➔ bỏ ます thành 「生まれ」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Từ 「作品」 có nghĩa là gì?",
        "options": ["Tác phẩm nghệ thuật/sách", "Sản phẩm công nghiệp", "Nguyên liệu", "Vật phẩm đắt tiền"],
        "correct": 0,
        "explain": "作品 (さくひん - TÁC PHẨM) là tác phẩm nghệ thuật, văn học, hội họa."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "国際的な 大会で 優勝して、金メダルの [____] を もらいました。",
        "options": ["しょう", "ゆめ", "じんせい", "さくひん"],
        "correct": 0,
        "explain": "Nhận phần thưởng, huy chương: 「賞 (しょう)」."
    },
    {
        "id": 14,
        "category": "Hội thoại",
        "q": "子どもの 頃に 読んだ 本から、とても 大きな [____] を 受けました。",
        "options": ["えいきょう", "しっぱい", "どりょく", "しょうがい"],
        "correct": 0,
        "explain": "Nhận được tầm ảnh hưởng lớn lao: 「影響 (えいきょう) を受けました」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「努力」 gồm 2 chữ nào ghép lại?",
        "options": ["NỖ + LỰC", "NỖ + ĐỘ", "MIỄN + LỰC", "DỤC + LỰC"],
        "correct": 0,
        "explain": "努力 gồm NỖ (努) và LỰC (力) ➔ nỗ lực hết mình."
    }
]


# =============================================================================
# LESSON 18 DATA
# =============================================================================
L18_VOCAB = [
    {
        "jp": "妹とけんかします",
        "kana": "いもうととけんかします",
        "kanji": "妹とけんかします",
        "romaji": "imouto to kenka shimasu",
        "vi": "Cãi cọ với em gái",
        "icon": "🥊"
    },
    {
        "jp": "先生が褒めます",
        "kana": "せんせいがほめます",
        "kanji": "先生が褒めます",
        "romaji": "sensei ga homemasu",
        "vi": "Giáo viên khen",
        "icon": "👏"
    },
    {
        "jp": "母が叱ります",
        "kana": "ははがしかります",
        "kanji": "母が叱ります",
        "romaji": "haha ga shikarimasu",
        "vi": "Mẹ mắng",
        "icon": "😠"
    },
    {
        "jp": "おしゃれします",
        "kana": "おしゃれします",
        "kanji": "おしゃれします",
        "romaji": "oshare shimasu",
        "vi": "Làm đỏm, làm điệu",
        "icon": "👗"
    },
    {
        "jp": "友達を誘います",
        "kana": "ともだちをさそいます",
        "kanji": "友達を誘います",
        "romaji": "tomodachi o sasoimasu",
        "vi": "Rủ bạn bè",
        "icon": "🤝"
    },
    {
        "jp": "就職します",
        "kana": "しゅうしょくします",
        "kanji": "就職します",
        "romaji": "shuushoku shimasu",
        "vi": "Bắt đầu công việc tại công ty lớn",
        "icon": "💼"
    },
    {
        "jp": "恋人とデートします",
        "kana": "こいびととデートします",
        "kanji": "恋人とデートします",
        "romaji": "koibito to de-to shimasu",
        "vi": "Hẹn hò với người yêu",
        "icon": "💑"
    },
    {
        "jp": "転勤します",
        "kana": "てんきんします",
        "kanji": "転勤します",
        "romaji": "tenkin shimasu",
        "vi": "Chuyển công tác đến Pháp",
        "icon": "✈️"
    },
    {
        "jp": "退職します",
        "kana": "たいしょくします",
        "kanji": "退職します",
        "romaji": "taishoku shimasu",
        "vi": "Khi 60 tuổi, tôi sẽ nghỉ việc",
        "icon": "🏖️"
    },
    {
        "jp": "ひどい",
        "kana": "ひどい",
        "kanji": "酷い",
        "romaji": "hidoi",
        "vi": "Tệ",
        "icon": "😣"
    },
    {
        "jp": "悲しい",
        "kana": "かなしい",
        "kanji": "悲しい",
        "romaji": "kanashii",
        "vi": "Buồn rầu",
        "icon": "😢"
    },
    {
        "jp": "甘えます",
        "kana": "あまえます",
        "kanji": "甘えます",
        "romaji": "amaemasu",
        "vi": "Nuông chiều",
        "icon": "🥰"
    },
    {
        "jp": "大人しい",
        "kana": "おとなしい",
        "kanji": "大人しい",
        "romaji": "otonashii",
        "vi": "Điềm đạm, dễ bảo",
        "icon": "😌"
    },
    {
        "jp": "成績",
        "kana": "せいせき",
        "kanji": "成績",
        "romaji": "seiseki",
        "vi": "Thành tích",
        "icon": "📊"
    },
    {
        "jp": "恥ずかしい",
        "kana": "はずかしい",
        "kanji": "恥ずかしい",
        "romaji": "hazukashii",
        "vi": "Xấu hổ",
        "icon": "😳"
    },
    {
        "jp": "きっかけ",
        "kana": "きっかけ",
        "kanji": "きっかけ",
        "romaji": "kikkake",
        "vi": "Cơ duyên",
        "icon": "🔑"
    },
    {
        "jp": "夕食",
        "kana": "ゆうしょく",
        "kanji": "夕食",
        "romaji": "yuushoku",
        "vi": "Bữa tối",
        "icon": "🍲"
    },
    {
        "jp": "仲がいい",
        "kana": "なかがいい",
        "kanji": "仲がいい",
        "romaji": "naka ga ii",
        "vi": "Thân thiết, mối quan quan hệ tốt",
        "icon": "👫"
    },
    {
        "jp": "前",
        "kana": "まえ",
        "kanji": "前",
        "romaji": "mae",
        "vi": "Trước đây",
        "icon": "🕰️"
    },
    {
        "jp": "勧めます",
        "kana": "すすめます",
        "kanji": "勧めます",
        "romaji": "susumemasu",
        "vi": "Đề xuất, gợi ý",
        "icon": "💡"
    },
    {
        "jp": "興味があります",
        "kana": "きょうみがあります",
        "kanji": "興味があります",
        "romaji": "kyoumi ga arimasu",
        "vi": "Có hứng thú",
        "icon": "✨"
    },
    {
        "jp": "社会人",
        "kana": "しゃかいじん",
        "kanji": "社会人",
        "romaji": "shakaijin",
        "vi": "Người trưởng thành, người xã hội",
        "icon": "👔"
    },
    {
        "jp": "やっと",
        "kana": "やっと",
        "kanji": "やっと",
        "romaji": "yatto",
        "vi": "Cuối cùng thì (kết quả tốt)",
        "icon": "🎉"
    },
    {
        "jp": "町のサイン",
        "kana": "まちのサイン",
        "kanji": "町のサイン",
        "romaji": "machi no sain",
        "vi": "biển báo trên phố",
        "icon": "🪧"
    },
    {
        "jp": "頼みます",
        "kana": "たのみます",
        "kanji": "頼みます",
        "romaji": "tanomimasu",
        "vi": "Nhờ vả",
        "icon": "🙇"
    },
    {
        "jp": "心配します",
        "kana": "しんぱいします",
        "kanji": "心配します",
        "romaji": "shinpai shimasu",
        "vi": "Lo lắng",
        "icon": "😟"
    },
    {
        "jp": "怖い",
        "kana": "こわい",
        "kanji": "怖い",
        "romaji": "kowai",
        "vi": "Sợ",
        "icon": "😨"
    }
]

L18_VERBS = [
    {"masu": "おもいだします", "vi": "Nhớ lại", "te": "おもいだして", "form1": "おもいだすと (mỗi khi nhớ lại)", "form2": "おもいだした (đã nhớ ra)", "form3": "おもいだす"},
    {"masu": "がんばります", "vi": "Cố gắng", "te": "がんばって", "form1": "がんばろうと思っています (đang dự định sẽ cố gắng)", "form2": "がんばった", "form3": "がんばる"},
    {"masu": "かわります", "vi": "Thay đổi", "te": "かわって", "form1": "かわりました (đã đổi thay)", "form2": "かわったこと", "form3": "かわる"},
    {"masu": "はたらきます", "vi": "Làm việc", "te": "はたらいて", "form1": "はたらこうと思っています (tính sẽ làm việc)", "form2": "はたらいた", "form3": "はたらく"},
    {"masu": "つづけます", "vi": "Tiếp tục duy trì", "te": "つづけて", "form1": "つづけようと思います", "form2": "つづけた", "form3": "つづける"}
]

L18_KANJI_LIST = [
    {"stt": 1, "word": "性格", "kana": "せいかく", "hv": "TÍNH CÁCH", "mean": "Tính cách"},
    {"stt": 2, "word": "活発", "kana": "かっぱつ", "hv": "HOẠT BÁT", "mean": "Hoạt bát, năng động"},
    {"stt": 3, "word": "将来", "kana": "しょうらい", "hv": "TƯƠNG LAI", "mean": "Tương lai"},
    {"stt": 4, "word": "目標", "kana": "もくひょう", "hv": "MỤC TIÊU", "mean": "Mục tiêu"},
    {"stt": 5, "word": "覚えます", "kana": "おぼえます", "hv": "GIÁC", "mean": "Ghi nhớ"},
    {"stt": 6, "word": "思い出します", "kana": "おもいだします", "hv": "TƯ XUẤT", "mean": "Nhớ lại"},
    {"stt": 7, "word": "勉強", "kana": "べんきょう", "hv": "MIỄN CƯỠNG", "mean": "Học tập"},
    {"stt": 8, "word": "働きます", "kana": "はたらきます", "hv": "ĐỘNG", "mean": "Làm việc"}
]

L18_KANJI_CARDS = [
    {"char": "性", "hv": "Tính", "strokes": 8, "kun": "ー", "on": "せい、しょう", "ex": "性格 (せいかく - tính cách), 男性 (だんせい - nam giới), 女性 (じょせい - nữ giới)", "mnemonic": "Con tim (忄) sinh ra (生) bản chất tự nhiên là Tính tình, Tính cách."},
    {"char": "格", "hv": "Cách", "strokes": 10, "kun": "ー", "on": "かく、こう", "ex": "性格 (せいかく - tính cách), 合格 (ごうかく - đỗ đạt/thi đỗ), 資格 (しかく - bằng cấp/tư cách)", "mnemonic": "Cây gỗ (木) đặt ngay ngắn trước cổng các (各) người qua lại là Quy cách."},
    {"char": "活", "hv": "Hoạt", "strokes": 9, "kun": "い・きる", "on": "かつ", "ex": "活発 (かっぱつ - hoạt bát), 生活 (せいかつ - sinh hoạt), 活動 (かつどう - hoạt động)", "mnemonic": "Dòng nước (氵) tưới vào chiếc lưỡi (舌) hồi sinh sức sống là Linh hoạt, Hoạt bát."},
    {"char": "発", "hv": "Phát", "strokes": 9, "kun": "ー", "on": "はつ、ほつ", "ex": "活発 (かっぱつ - năng động), 出発 (しゅっぱつ - xuất phát), 発見 (はっけん - phát hiện)", "mnemonic": "Chân bước sải dài (癶) giương cung bắn mũi tên vút bay là Phát khởi."},
    {"char": "標", "hv": "Tiêu", "strokes": 15, "kun": "しるし", "on": "ひょう", "ex": "目標 (もくひょう - mục tiêu), 標準 (ひょうじゅん - tiêu chuẩn), 標識 (ひょうしき - biển báo)", "mnemonic": "Cây gỗ (木) dựng cao lên tận ngọn (票 - phiếu) làm dấu mốc định hướng là Tiêu điểm."},
    {"char": "覚", "hv": "Giác", "strokes": 12, "kun": "おぼ・える、さ・める", "on": "かく", "ex": "覚える (おぼえる - ghi nhớ), 目覚まし (めざまし - báo thức), 感覚 (かんかく - cảm giác)", "mnemonic": "Mở rộng tầm mắt (見) dưới mái trường học hỏi thấu suốt mọi điều là Nhận giác."},
    {"char": "勉", "hv": "Miễn", "strokes": 10, "kun": "つと・める", "on": "べん", "ex": "勉強 (べんきょう - học tập), 勉励 (べんれい - siêng năng)", "mnemonic": "Người thoát khỏi nguy nan (免) dùng hết sức lực (力) để Miễn cưỡng, Gắng sức."},
    {"char": "強", "hv": "Cường", "strokes": 11, "kun": "つよ・い", "on": "きょう、ごう", "ex": "勉強 (べんきょう - học tập rèn luyện), 強い (つよい - mạnh mẽ), 強調 (きょうちょう - nhấn mạnh)", "mnemonic": "Cây cung lớn (弓) bắn xuyên qua loài bọ giáp cứng (虫) là Kiên cường, Mạnh mẽ."}
]

L18_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>👦</span> 1. Kỷ Niệm Tuổi Thơ: 子どものとき、よく V-ました</h2>
            <span class="section-tag">Hồi tưởng quá khứ</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để kể về tính cách thời thơ ấu và những việc mình thường hay làm khi còn nhỏ:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • 子どもの とき、よく 外で 遊（あそ）びました。<br>
                    • 昔は おとなしかったですが、今は 活発に なりました。
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">子どもの 頃は どんな 子どもでしたか。 ―― おとなしくて、絵を 描くのが 好きでした。</div>
                        <div class="ex-vi">Hồi nhỏ bạn là đứa trẻ như thế nào? ―― Mình trầm tính và rất thích vẽ tranh.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('子どもの頃はどんな子どもでしたか。おとなしくて、絵を描くのが好きでした')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🚀</span> 2. Thể Ý Chí & Quyết Tâm Tương Lai: V-ようと 思っています</h2>
            <span class="section-tag">Kế hoạch tương lai & Tổng kết A2-2</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • [Động từ thể Ý chí (ikoukei)] ＋ と 思っています (Đang dự định / nung nấu ý định sẽ...)<br>
                    • Nhóm 1: う ➔ おう (行こう、働こう、続けよう)<br>
                    • Nhóm 2: る ➔ よう (食べよう、見よう)<br>
                    • Nhóm 3: 勉強しよう、来よう (こよう)
                </div>
                <div class="rule-meaning">
                    • <strong>将来、日本で 働こうと 思っています:</strong> Tôi dự định tương lai sẽ làm việc tại Nhật.<br>
                    • <strong>これからも 日本語の 勉強を 続けようと 思います:</strong> Từ nay tôi sẽ tiếp tục duy trì việc học tiếng Nhật.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">A2-2を 終えたあとも、N3合格を 目指して 頑張ろうと 思っています！</div>
                        <div class="ex-vi">Sau khi hoàn thành xong A2-2, mình dự định sẽ quyết tâm hướng tới mục tiêu đỗ N3!</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('A2-2を終えたあとも、N3合格を目指して頑張ろうと思っています')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L18_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "将来、日本で 自分の 会社を [____] と 思っています。",
        "options": ["作ろう", "作る", "作った", "作り"],
        "correct": 0,
        "explain": "Cấu trúc dự định thể ý chí: 『V thể Ý chí + と思っています』: 作ります ➔ 「作ろう」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "子どもの [____] は、いつも 外で 元気に 走っていました。",
        "options": ["ころ", "まえ", "あと", "あいだ"],
        "correct": 0,
        "explain": "Thời bé, hồi nhỏ: 『子どもの頃 (ころ)』."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "あまり 騒がずに 静かで 礼儀正しい 様子は [____] です。",
        "options": ["おとなしい", "いたずら", "かっぱつ", "にぎやか"],
        "correct": 0,
        "explain": "Hiền lành, ngoan ngoãn, trầm tính: 「おとなしい」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「性格」 có cách đọc chuẩn là gì?",
        "options": ["せいかく", "しょうかく", "せいこう", "せいぎ"],
        "correct": 0,
        "explain": "性格 đọc là 「せいかく」 (TÍNH CÁCH)."
    },
    {
        "id": 5,
        "category": "Ngữ pháp",
        "q": "これからも 毎日 日本語を [____] と 思います。",
        "options": ["勉強しよう", "勉強する", "勉強して", "勉強した"],
        "correct": 0,
        "explain": "Dự định tương lai: 勉強します ➔ thể ý chí là 「勉強しよう」."
    },
    {
        "id": 6,
        "category": "Từ vựng",
        "q": "元気で 行動的な 人の 性格を 「[____] な 性格」 と 表現します。",
        "options": ["かっぱつ", "おとなしい", "ふべん", "ひくい"],
        "correct": 0,
        "explain": "Năng động hoạt bát: 「活発 (かっぱつ) な性格」."
    },
    {
        "id": 7,
        "category": "Chữ Hán",
        "q": "Từ 「将来」 có nghĩa là gì?",
        "options": ["Tương lai phía trước", "Quá khứ đã qua", "Hiện tại bây giờ", "Thời xưa"],
        "correct": 0,
        "explain": "将来 (しょうらい - TƯƠNG LAI) nghĩa là tương lai, mai sau."
    },
    {
        "id": 8,
        "category": "Hội thoại",
        "q": "昔の 写真を 見ると、当時の 楽しい 思い出を [____] ます。",
        "options": ["思い出し", "覚えます", "調べます", "変わります"],
        "correct": 0,
        "explain": "Hồi tưởng, nhớ lại kỷ niệm cũ: 「思い出す (おもいだす)」."
    },
    {
        "id": 9,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「目標」 gồm 2 chữ nào?",
        "options": ["MỤC + TIÊU", "NHÃN + TIÊU", "MỤC + ĐÍCH", "ĐẦU + TIÊU"],
        "correct": 0,
        "explain": "目標 gồm MỤC (目) và TIÊU (標) ➔ mục tiêu phấn đấu."
    },
    {
        "id": 10,
        "category": "Từ vựng",
        "q": "先生や 友達に 「これからも [____] ね！」 と 励まされました。",
        "options": ["がんばって", "とまって", "あきらめて", "つかれて"],
        "correct": 0,
        "explain": "Lời động viên cố lên: 「これからも 頑張って (がんばって) ね！」."
    },
    {
        "id": 11,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「覚える」 đọc là gì?",
        "options": ["おぼえる", "かんがえる", "おもえる", "さとる"],
        "correct": 0,
        "explain": "覚える đọc là 「おぼえる」 (GIÁC - ghi nhớ)."
    },
    {
        "id": 12,
        "category": "Ngữ pháp",
        "q": "子どもの 頃は ピーマンが 嫌いでしたが、大人に なってから 食べられるように [____]。",
        "options": ["なりました", "します", "なれません", "しています"],
        "correct": 0,
        "explain": "Biến đổi trạng thái theo thời gian: 『V-る / られる ように なりました』 (đã có thể ăn được)."
    },
    {
        "id": 13,
        "category": "Từ vựng",
        "q": "自分の 目標に 向かって 心も 体も 大きく なることを [____] と 言います。",
        "options": ["せいちょう", "しっぱい", "へんぴん", "こうかん"],
        "correct": 0,
        "explain": "Trưởng thành, lớn lên: 「成長 (せいちょう)」."
    },
    {
        "id": 14,
        "category": "Chữ Hán",
        "q": "Từ 「勉強」 có âm Hán Việt là gì?",
        "options": ["MIỄN CƯỠNG", "MIỄN LỰC", "CƯỠNG LỰC", "HỌC TẬP"],
        "correct": 0,
        "explain": "勉強 có âm Hán Việt là MIỄN CƯỠNG (nghĩa gốc là gắng sức nỗ lực học tập)."
    },
    {
        "id": 15,
        "category": "Hội thoại",
        "q": "「まるごと A2-2の 勉強、お疲れ様でした！」 ―― 「[____]」",
        "options": ["ありがとうございました！ 楽しかったです！", "どういたしまして。", "こちらこそ、ごめんなさい。", "おやすみなさい。"],
        "correct": 0,
        "explain": "Lời đáp đầy hào hứng và biết ơn khi hoàn thành khóa học A2-2: 「ありがとうございました！ 楽しかったです！」."
    }
]
