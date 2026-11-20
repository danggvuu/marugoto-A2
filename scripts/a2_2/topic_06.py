# -*- coding: utf-8 -*-
"""
Topic 6: ネットショッピング (Online Shopping / Mua sắm trực tuyến)
- Lesson 11: 掃除機がこわれてしまったんです (My vacuum cleaner has broken down)
- Lesson 12: こっちの方が安いです (This one is cheaper)
"""

# =============================================================================
# LESSON 11 DATA
# =============================================================================
L11_VOCAB = [
    {
        "jp": "商品",
        "kana": "しょうひん",
        "kanji": "商品",
        "romaji": "shouhin",
        "vi": "Sản phẩm",
        "icon": "📦"
    },
    {
        "jp": "電気製品",
        "kana": "でんきせいひん",
        "kanji": "電気製品",
        "romaji": "denkiseihin",
        "vi": "Đồ điện",
        "icon": "📱"
    },
    {
        "jp": "掃除機",
        "kana": "そうじき",
        "kanji": "掃除機",
        "romaji": "soujiki",
        "vi": "Máy hút bụi",
        "icon": "🧹"
    },
    {
        "jp": "冷蔵庫",
        "kana": "れいぞうこ",
        "kanji": "冷蔵庫",
        "romaji": "reizouko",
        "vi": "Tủ lạnh",
        "icon": "🧊"
    },
    {
        "jp": "洗濯機",
        "kana": "せんたくき",
        "kanji": "洗濯機",
        "romaji": "sentakuki",
        "vi": "Máy giặt",
        "icon": "🧺"
    },
    {
        "jp": "音楽プレーヤー",
        "kana": "おんがくプレーヤー",
        "kanji": "音楽プレーヤー",
        "romaji": "ongaku pure-ya-",
        "vi": "Máy phát nhạc",
        "icon": "📻"
    },
    {
        "jp": "扇風機",
        "kana": "せんぷうき",
        "kanji": "扇風機",
        "romaji": "senpuuki",
        "vi": "Quạt",
        "icon": "🪭"
    },
    {
        "jp": "アイロン",
        "kana": "アイロン",
        "kanji": "アイロン",
        "romaji": "airon",
        "vi": "Bàn là",
        "icon": "👔"
    },
    {
        "jp": "電子レンジ",
        "kana": "でんしレンジ",
        "kanji": "電子レンジ",
        "romaji": "denshi renji",
        "vi": "Lò vi sóng",
        "icon": "🍲"
    },
    {
        "jp": "炊飯器",
        "kana": "すいはんき",
        "kanji": "炊飯器",
        "romaji": "suihanki",
        "vi": "Nồi cơm",
        "icon": "🍚"
    },
    {
        "jp": "壊れます",
        "kana": "こわれます",
        "kanji": "壊れます",
        "romaji": "kowaremasu",
        "vi": "Hỏng",
        "icon": "💥"
    },
    {
        "jp": "音が出ません",
        "kana": "おとがでません",
        "kanji": "音が出ません",
        "romaji": "oto ga demasen",
        "vi": "Không phát âm thanh",
        "icon": "🔇"
    },
    {
        "jp": "動きません",
        "kana": "うごきません",
        "kanji": "動きません",
        "romaji": "ugokimasen",
        "vi": "Không cử động",
        "icon": "🛑"
    },
    {
        "jp": "調子が悪い",
        "kana": "ちょうしがわるい",
        "kanji": "調子が悪い",
        "romaji": "choushi ga warui",
        "vi": "Tình trạng không tốt, trục trặc",
        "icon": "⚠️"
    },
    {
        "jp": "気にしません",
        "kana": "きにしません",
        "kanji": "気にしません",
        "romaji": "ki ni shimasen",
        "vi": "Không để ý, bận tâm đến N",
        "icon": "🤷"
    },
    {
        "jp": "探します",
        "kana": "さがします",
        "kanji": "探します",
        "romaji": "sagashimasu",
        "vi": "Tìm kiếm",
        "icon": "🔍"
    },
    {
        "jp": "落とします",
        "kana": "おとします",
        "kanji": "落とします",
        "romaji": "otoshimasu",
        "vi": "Đánh rơi",
        "icon": "📉"
    },
    {
        "jp": "困ります",
        "kana": "こまります",
        "kanji": "困ります",
        "romaji": "komarimasu",
        "vi": "Khó khăn, rắc rối",
        "icon": "😰"
    },
    {
        "jp": "調べます",
        "kana": "しらべます",
        "kanji": "調べます",
        "romaji": "shirabemasu",
        "vi": "Tìm hiểu, điều tra",
        "icon": "📖"
    },
    {
        "jp": "比べます",
        "kana": "くらべます",
        "kanji": "比べます",
        "romaji": "kurabemasu",
        "vi": "So sánh",
        "icon": "⚖️"
    },
    {
        "jp": "届きます",
        "kana": "とどきます",
        "kanji": "届きます",
        "romaji": "todokimasu",
        "vi": "Được giao đến, chuyển đến",
        "icon": "📦"
    },
    {
        "jp": "決めます",
        "kana": "きめます",
        "kanji": "決めます",
        "romaji": "kimemasu",
        "vi": "Quyết định",
        "icon": "✅"
    },
    {
        "jp": "注文します",
        "kana": "ちゅうもんします",
        "kanji": "注文します",
        "romaji": "chuumon shimasu",
        "vi": "Order, đặt hàng",
        "icon": "🛒"
    },
    {
        "jp": "考えます",
        "kana": "かんがえます",
        "kanji": "考えます",
        "romaji": "kangaemasu",
        "vi": "Suy nghĩ",
        "icon": "🤔"
    }
]

L11_VERBS = [
    {"masu": "こわれます", "vi": "Bị hỏng", "te": "こわれて", "form1": "こわれてしまった (lỡ hỏng mất rồi)", "form2": "こわれたんです (bị hỏng đấy ạ)", "form3": "こわれる"},
    {"masu": "うごきます", "vi": "Chạy / hoạt động", "te": "うごいて", "form1": "うごかなくなりました (không chạy nữa)", "form2": "うごかないんです", "form3": "うごく"},
    {"masu": "なおします", "vi": "Sửa chữa", "te": "なおして", "form1": "なおしてください (hãy sửa giúp)", "form2": "なおした", "form3": "なおす"},
    {"masu": "とどきます", "vi": "Hàng tới", "te": "とどいて", "form1": "もうとどきました (đã giao tới rồi)", "form2": "まだとどいていません", "form3": "とどく"},
    {"masu": "こまります", "vi": "Khó khăn / rắc rối", "te": "こまって", "form1": "こまっているんです (tôi đang rất khó xử)", "form2": "こまった", "form3": "こまる"}
]

L11_KANJI_LIST = [
    {"stt": 1, "word": "掃除機", "kana": "そうじき", "hv": "TẢO TRỪ CƠ", "mean": "Máy hút bụi"},
    {"stt": 2, "word": "洗濯機", "kana": "せんたくき", "hv": "TIỂM TRẠC CƠ", "mean": "Máy giặt"},
    {"stt": 3, "word": "冷蔵庫", "kana": "れいぞうこ", "hv": "LÃNH TÀNG KHỐ", "mean": "Tủ lạnh"},
    {"stt": 4, "word": "故障", "kana": "こしょう", "hv": "CỐ CHƯỚNG", "mean": "Hỏng hóc, sự cố"},
    {"stt": 5, "word": "修理", "kana": "しゅうり", "hv": "TU LÝ", "mean": "Sửa chữa"},
    {"stt": 6, "word": "交換", "kana": "こうかん", "hv": "GIAO HOÁN", "mean": "Đổi hàng, hoán đổi"},
    {"stt": 7, "word": "不便", "kana": "ふべん", "hv": "BẤT TIỆN", "mean": "Bất tiện"},
    {"stt": 8, "word": "壊れます", "kana": "こわれます", "hv": "HOẠI", "mean": "Bị hỏng"}
]

L11_KANJI_CARDS = [
    {"char": "掃", "hv": "Tảo", "strokes": 11, "kun": "は・く", "on": "そう", "ex": "掃除機 (そうじき - máy hút bụi), 掃除 (そうじ - dọn dẹp)", "mnemonic": "Bàn tay (扌) cầm chổi quét sạch bụi bặm trong gian nhà của người vợ (婦) là Quét dọn (Tảo)."},
    {"char": "除", "hv": "Trừ", "strokes": 10, "kun": "のぞ・く", "on": "じょ、じ", "ex": "掃除 (そうじ - lau dọn), 削除 (さくじょ - xóa bỏ), 除く (のぞく - loại trừ)", "mnemonic": "Bước lên bậc thềm (阝) gạt bỏ chiếc dư thừa (余) là Tiêu trừ."},
    {"char": "機", "hv": "Cơ", "strokes": 16, "kun": "はた", "on": "き", "ex": "掃除機 (そうじき - máy hút bụi), 飛行機 (ひこうき - máy bay), 機会 (きかい - cơ hội)", "mnemonic": "Dùng cây gỗ (木) phối hợp cùng vài bánh răng dây chuyền tạo thành Cỗ máy (Cơ)."},
    {"char": "洗", "hv": "Tiển", "strokes": 9, "kun": "あら・う", "on": "せん", "ex": "洗濯機 (せんたくき - máy giặt), 洗う (あらう - rửa), お手洗い (おてあらい - nhà vệ sinh)", "mnemonic": "Dùng nước (氵) rửa sạch bàn chân trước khi đi tiếp (Tiên = Tiển)."},
    {"char": "濯", "hv": "Trạc", "strokes": 17, "kun": "ー", "on": "たく", "ex": "洗濯機 (せんたくき - máy giặt), 洗濯物 (せんたくもの - quần áo giặt)", "mnemonic": "Dùng nước (氵) giũ sạch bùn bám trên đôi cánh chim (隹) là Giặt giũ (Trạc)."},
    {"char": "冷", "hv": "Lãnh", "strokes": 7, "kun": "つめ・たい、ひ・える", "on": "れい", "ex": "冷蔵庫 (れいぞうこ - tủ lạnh), 冷たい (つめたい - lạnh buốt), 冷静 (れいせい - điềm tĩnh)", "mnemonic": "Hai giọt băng giá (冫) rơi xuống theo hiệu lệnh (令) tạo nên cảm giác Lạnh giá."},
    {"char": "蔵", "hv": "Tàng", "strokes": 17, "kun": "くら", "on": "ぞう", "ex": "冷蔵庫 (れいぞうこ - tủ lạnh), 貯蔵 (ちょぞう - dự trữ), 蔵 (くら - kho thóc)", "mnemonic": "Cây cỏ (艹) che giấu vũ khí và binh lính (臧) cất kín trong Kho tàng."},
    {"char": "庫", "hv": "Khố", "strokes": 10, "kun": "くら", "on": "こ、く", "ex": "冷蔵庫 (れいぞうこ - tủ lạnh), 金庫 (きんこ - két sắt), 車庫 (しゃこ - nhà để xe)", "mnemonic": "Dưới mái hiên (广) cất giữ xe cộ (車) an toàn là Kho tàng (Khố)."},
    {"char": "壊", "hv": "Hoại", "strokes": 16, "kun": "こわ・れる、こわ・す", "on": "かい", "ex": "壊れる (こわれる - bị vỡ/hỏng), 崩壊 (ほうかい - sụp đổ), 破壊 (はかい - phá hoại)", "mnemonic": "Đất đá (土) bị đổ nát vùi lấp cả xiêm áo (褱) là Phá hoại, Sụp đổ."}
]

L11_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>💥</span> 1. Sự Cố Đáng Tiếc: V-て しまいました & ～んです</h2>
            <span class="section-tag">Than phiền hỏng hóc</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Khi thiết bị đồ dùng bất ngờ bị hỏng, người Nhật dùng thể <code>V-てしまいました</code> kết hợp đuôi <code>～んです</code> để giãi bày sự cố đáng tiếc và xin được hỗ trợ.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #ef4444;">
                <div class="rule-formula" style="color: #991b1b;">
                    • [Động từ thể TE] ＋ しまいました (Lỡ mất / Tiếc nuối)<br>
                    • [Thể thông thường] ＋ んです / のです (Giãi bày hoàn cảnh)
                </div>
                <div class="rule-meaning">
                    • <strong>掃除機が こわれてしまったんです:</strong> Máy hút bụi của tôi bị hỏng mất rồi ạ.<br>
                    • <strong>変な 音が して、動かないんです:</strong> Nó phát ra tiếng kêu lạ rồi không chạy nữa.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">すみません、先週 買ったばかりの 洗濯機が こわれてしまったんです。</div>
                        <div class="ex-vi">Xin lỗi, chiếc máy giặt tôi vừa mua tuần trước bị hỏng mất rồi ạ.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('すみません、先週買ったばかりの洗濯機がこわれてしまったんです')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🔧</span> 2. Yêu Cầu Bảo Hành & Sửa Chữa</h2>
            <span class="section-tag">Bảo hành & Đổi trả</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #0284c7;">
                <div class="rule-formula" style="color: #0369a1;">
                    • 保証期間（ほしょうきかん）中ですか。(Còn trong thời hạn bảo hành không?)<br>
                    • 修理（しゅうり）を お願いできますか。(Có thể sửa giúp tôi không?)<br>
                    • 新しいのと 交換（こうかん）して ください。(Xin đổi cho tôi cái mới)
                </div>
                <div class="rule-meaning">
                    Khi đi bảo hành cần mang theo giấy bảo hành (保証書) và biên lai thanh toán (レシート).
                </div>
            </div>
        </div>
    </section>'''
]

L11_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "昨日から 冷蔵庫の 調子が 悪くて、[____] しまったんです。",
        "options": ["こわれて", "こわして", "こわれた", "こわる"],
        "correct": 0,
        "explain": "Tự động từ bị hỏng: こわれます ➔ thể TE: 「こわれて」 ＋ しまいました."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "スイッチを 押しても、まったく [____] んです。どうしたら いいですか。",
        "options": ["動かない", "動いた", "動いて", "動く"],
        "correct": 0,
        "explain": "Bấm nút máy vẫn không chạy (thể phủ định thông thường + んです): 「動かないんです」."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "床の ゴミや ホコリを 吸い取る 電化製品は [____] です。",
        "options": ["そうじき", "せんたくき", "れいぞうこ", "電子レンジ"],
        "correct": 0,
        "explain": "Máy hút bụi sàn nhà là 「掃除機 (そうじき)」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「故障」 có âm Hán Việt là gì?",
        "options": ["CỐ CHƯỚNG", "CỐ HƯƠNG", "CỐ ĐỊNH", "CHƯỚNG NGẠI"],
        "correct": 0,
        "explain": "故障 có âm Hán Việt là CỐ CHƯỚNG (sự cố, hỏng hóc kỹ thuật)."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "冷たい 飲み物や 食べ物を 腐らせないように 保存する 家電は [____] です。",
        "options": ["れいぞうこ", "そうじき", "パソコン", "せんたくき"],
        "correct": 0,
        "explain": "Tủ lạnh bảo quản đồ ăn là 「冷蔵庫 (れいぞうこ)」."
    },
    {
        "id": 6,
        "category": "Hội thoại",
        "q": "無料で 修理して もらうために、商品と 一緒に [____] を 見せます。",
        "options": ["ほしょうしょ", "メニュー", "手紙", "ガイドブック"],
        "correct": 0,
        "explain": "Giấy bảo hành sản phẩm: 「保証書 (ほしょうしょ)」."
    },
    {
        "id": 7,
        "category": "Chữ Hán",
        "q": "Từ 「修理」 có cách đọc là gì?",
        "options": ["しゅうり", "しゅうじ", "しゅうれい", "すうり"],
        "correct": 0,
        "explain": "修理 đọc là 「しゅうり」 (TU LÝ - sửa chữa)."
    },
    {
        "id": 8,
        "category": "Từ vựng",
        "q": "服が 汚れたので、[____] で 洗います。",
        "options": ["せんたくき", "れいぞうこ", "そうじき", "電子レンジ"],
        "correct": 0,
        "explain": "Giặt quần áo bằng máy giặt: 「洗濯機 (せんたくき)」."
    },
    {
        "id": 9,
        "category": "Ngữ pháp",
        "q": "インターネットで 注文した 商品が まだ [____] のですが、確認して もらえますか。",
        "options": ["届かない", "届いた", "届いて", "届く"],
        "correct": 0,
        "explain": "Hàng vẫn chưa tới (giải thích hoàn cảnh): 「届かないのですが」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「不便」 đối nghĩa với từ nào?",
        "options": ["便利 (べんり)", "大切 (たいせつ)", "静か (しずか)", "簡単 (かんたん)"],
        "correct": 0,
        "explain": "不便 (bất tiện) đối nghĩa với 便利 (tiện lợi)."
    },
    {
        "id": 11,
        "category": "Từ vựng",
        "q": "買った 商品に 傷が あったので、新しい ものに [____] して ください。",
        "options": ["こうかん", "しゅうり", "へんぴん", "よやく"],
        "correct": 0,
        "explain": "Đổi sang sản phẩm mới không trầy xước: 「交換 (こうかん) してください」."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「庫」 trong 「冷蔵庫」 có âm Hán Việt là gì?",
        "options": ["KHỐ", "QUÁN", "CẢNG", "SỞ"],
        "correct": 0,
        "explain": "庫 có âm Hán Việt là KHỐ (kho chứa)."
    },
    {
        "id": 13,
        "category": "Hội thoại",
        "q": "「どうしたんですか。」 ―― 「パソコンが 急に 動かなくなって、とても [____] んです。」",
        "options": ["困っている", "喜んでいる", "楽しんでいる", "休んでいる"],
        "correct": 0,
        "explain": "Máy tính đơ rắc rối khó xử: 「困っているんです (こまっているんです)」."
    },
    {
        "id": 14,
        "category": "Từ vựng",
        "q": "電子レンジから [____] が 聞こえます。火花が 出たら 危険です。",
        "options": ["へんなおと", "あじ", "いろ", "におい"],
        "correct": 0,
        "explain": "Tiếng kêu lạ bất thường từ lò vi sóng: 「変な音 (へんなおと)」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「洗」 trong 「洗濯機」 đọc Kunyomi là gì?",
        "options": ["あらう", "あらわす", "そそぐ", "ぬぐう"],
        "correct": 0,
        "explain": "洗 có âm Kunyomi là 「あらう (洗う - rửa, giặt)」."
    }
]


# =============================================================================
# LESSON 12 DATA
# =============================================================================
L12_VOCAB = [
    {
        "jp": "モデル",
        "kana": "モデル",
        "kanji": "モデル",
        "romaji": "moderu",
        "vi": "Mẫu, kiểu",
        "icon": "📱"
    },
    {
        "jp": "重さ",
        "kana": "おもさ",
        "kanji": "重さ",
        "romaji": "omosa",
        "vi": "Cân nặng",
        "icon": "⚖️"
    },
    {
        "jp": "大きさ",
        "kana": "おおきさ",
        "kanji": "大きさ",
        "romaji": "ookisa",
        "vi": "Độ lớn",
        "icon": "📐"
    },
    {
        "jp": "機能",
        "kana": "きのう",
        "kanji": "機能",
        "romaji": "kinou",
        "vi": "Chức năng",
        "icon": "⚙️"
    },
    {
        "jp": "値段",
        "kana": "ねだん",
        "kanji": "値段",
        "romaji": "nedan",
        "vi": "Giá cả",
        "icon": "🏷️"
    },
    {
        "jp": "税込",
        "kana": "ぜいこみ",
        "kanji": "税込",
        "romaji": "zeikomi",
        "vi": "Bao gồm thuế",
        "icon": "🧾"
    },
    {
        "jp": "翌日",
        "kana": "よくじつ",
        "kanji": "翌日",
        "romaji": "yokujitsu",
        "vi": "Ngày hôm sau",
        "icon": "📅"
    },
    {
        "jp": "送料無料",
        "kana": "そうりょうむりょう",
        "kanji": "送料無料",
        "romaji": "souryou muryou",
        "vi": "Miễn phí vận chuyển",
        "icon": "🚚"
    },
    {
        "jp": "届きます",
        "kana": "とどきます",
        "kanji": "届きます",
        "romaji": "todokimasu",
        "vi": "Được giao đến (Nが届きます)",
        "icon": "📦"
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
        "jp": "デザイン",
        "kana": "デザイン",
        "kanji": "デザイン",
        "romaji": "dezain",
        "vi": "Thiết kế",
        "icon": "🎨"
    },
    {
        "jp": "カラー",
        "kana": "カラー",
        "kanji": "カラー",
        "romaji": "kara-",
        "vi": "Màu sắc",
        "icon": "🌈"
    },
    {
        "jp": "レビュー",
        "kana": "レビュー",
        "kanji": "レビュー",
        "romaji": "rebyu-",
        "vi": "Review, đánh giá",
        "icon": "⭐"
    },
    {
        "jp": "重い",
        "kana": "おもい",
        "kanji": "重い",
        "romaji": "omoi",
        "vi": "Nặng",
        "icon": "🏋️"
    },
    {
        "jp": "軽い",
        "kana": "かるい",
        "kanji": "軽い",
        "romaji": "karui",
        "vi": "Nhẹ",
        "icon": "🪶"
    },
    {
        "jp": "複雑（な）",
        "kana": "ふくざつ（な）",
        "kanji": "複雑（な）",
        "romaji": "fukuzatsu(na)",
        "vi": "Phức tạp",
        "icon": "🧩"
    },
    {
        "jp": "気に入ります",
        "kana": "きにいります",
        "kanji": "気に入ります",
        "romaji": "ki ni irimasu",
        "vi": "Thích, ưa thích",
        "icon": "❤️"
    },
    {
        "jp": "満足（します）",
        "kana": "まんぞく（します）",
        "kanji": "満足（します）",
        "romaji": "manzoku(shimasu)",
        "vi": "Hài lòng",
        "icon": "😊"
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
        "jp": "びっくり（します）",
        "kana": "びっくり（します）",
        "kanji": "びっくり（します）",
        "romaji": "bikkuri(shimasu)",
        "vi": "Bất ngờ",
        "icon": "😲"
    },
    {
        "jp": "ユーザー",
        "kana": "ユーザー",
        "kanji": "ユーザー",
        "romaji": "yu-za-",
        "vi": "Người dùng",
        "icon": "👤"
    },
    {
        "jp": "モード",
        "kana": "モード",
        "kanji": "モード",
        "romaji": "mo-do",
        "vi": "Chế độ",
        "icon": "🎛️"
    },
    {
        "jp": "うるさい",
        "kana": "うるさい",
        "kanji": "うるさい",
        "romaji": "urusai",
        "vi": "Ồn ào",
        "icon": "📢"
    }
]

L12_VERBS = [
    {"masu": "くらべます", "vi": "So sánh", "te": "くらべて", "form1": "くらべてみると (khi thử so sánh)", "form2": "くらべた (đã so sánh)", "form3": "くらべる"},
    {"masu": "まよいます", "vi": "Phân vân", "te": "まよって", "form1": "まよっている (đang phân vân)", "form2": "まよった (đã đắn đo)", "form3": "まよう"},
    {"masu": "きめます", "vi": "Quyết định", "te": "きめて", "form1": "こちらにします (chọn cái này)", "form2": "きめた (đã chốt)", "form3": "きめる"},
    {"masu": "はらいます", "vi": "Thanh toán", "te": "はらって", "form1": "カードではらいます", "form2": "はらった", "form3": "はらう"},
    {"masu": "つかいます", "vi": "Sử dụng", "te": "つかって", "form1": "つかいやすい (dễ sử dụng)", "form2": "つかいにくい (khó dùng)", "form3": "つかう"}
]

L12_KANJI_LIST = [
    {"stt": 1, "word": "値段", "kana": "ねだん", "hv": "TRỊ ĐOẠN", "mean": "Mức giá, giá tiền"},
    {"stt": 2, "word": "比べる", "kana": "くらべる", "hv": "TỈ", "mean": "So sánh"},
    {"stt": 3, "word": "便利", "kana": "べんり", "hv": "TIỆN LỢI", "mean": "Tiện lợi"},
    {"stt": 4, "word": "軽い", "kana": "かるい", "hv": "KHINH", "mean": "Nhẹ"},
    {"stt": 5, "word": "重い", "kana": "おもい", "hv": "TRỌNG", "mean": "Nặng"},
    {"stt": 6, "word": "安い", "kana": "やすい", "hv": "AN", "mean": "Rẻ"},
    {"stt": 7, "word": "高い", "kana": "たかい", "hv": "CAO", "mean": "Đắt, cao"},
    {"stt": 8, "word": "割引", "kana": "わりびき", "hv": "CÁT DẪN", "mean": "Giảm giá"},
    {"stt": 9, "word": "無料", "kana": "むりょう", "hv": "VÔ LIỆU", "mean": "Miễn phí"}
]

L12_KANJI_CARDS = [
    {"char": "比", "hv": "Tỉ", "strokes": 4, "kun": "くら・べる", "on": "ひ", "ex": "比べる (くらべる - so sánh), 比較 (ひかく - đối chiếu so sánh)", "mnemonic": "Hai người đứng sát vai nhau để So đo chiều cao (Tỉ)."},
    {"char": "便", "hv": "Tiện", "strokes": 9, "kun": "たよ・り", "on": "べん、びん", "ex": "便利 (べんり - tiện lợi), 郵便局 (ゆうびんきょく - bưu điện), 不便 (ふべん - bất tiện)", "mnemonic": "Con người (亻) làm việc gì cũng đổi mới (更) cho Thuận tiện."},
    {"char": "利", "hv": "Lợi", "strokes": 7, "kun": "き・く", "on": "り", "ex": "便利 (べんり - tiện lợi), 利用 (りよう - sử dụng), 利益 (りえき - lợi ích)", "mnemonic": "Cây lúa (禾) chín vàng dùng dao sắc (刂) gặt về là Lợi ích thu hoạch."},
    {"char": "軽", "hv": "Khinh", "strokes": 12, "kun": "かる・い", "on": "けい", "ex": "軽い (かるい - nhẹ), 手軽 (てがる - tiện tay/đơn giản)", "mnemonic": "Cỗ xe (車) lăn bon bon trên dòng sông cạn (𢀖) rất Nhẹ nhàng (Khinh)."},
    {"char": "重", "hv": "Trọng", "strokes": 9, "kun": "おも・い、かさ・なる", "on": "じゅう、ちょう", "ex": "重い (おもい - nặng), 体重 (たいじゅう - cân nặng), 重要 (じゅうよう - quan trọng)", "mnemonic": "Mang ngàn (千) bao đất (里) đè lên đôi vai nên rất Nặng nhọc (Trọng)."},
    {"char": "安", "hv": "An", "strokes": 6, "kun": "やす・い", "on": "あん", "ex": "安い (やすい - rẻ), 安心 (あんしん - an tâm), 安全 (あんぜん - an toàn)", "mnemonic": "Người phụ nữ (女) ở yên ổn dưới mái nhà (宀) thì tâm hồn Bình an."},
    {"char": "高", "hv": "Cao", "strokes": 10, "kun": "たか・い", "on": "こう", "ex": "高い (たかい - cao / đắt đỏ), 高校 (こうこう - trường cấp 3), 高級 (こうきゅう - cao cấp)", "mnemonic": "Hình tháp canh cao vút có mái che và cửa sổ nhìn ra xa (Cao)."},
    {"char": "割", "hv": "Cát", "strokes": 12, "kun": "わ・る、わり", "on": "かつ", "ex": "割引 (わりびき - giảm giá), 割合 (わりあい - tỷ lệ), 割る (わる - đập vỡ/chia ra)", "mnemonic": "Cầm con dao (刂) xẻ hại (害) đồ vật ra làm từng phần là Chia cắt."}
]

L12_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>⚖️</span> 1. So Sánh Hơn: N1 の 方が N2 より A です</h2>
            <span class="section-tag">So sánh sản phẩm</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Khi mua sắm trực tuyến, dùng mẫu so sánh này để cân nhắc các tiêu chí: giá cả, độ nặng, tính năng:
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">
                    • N1 の 方（ほう）が N2 より [Tính từ] です (N1 thì ... hơn N2)<br>
                    • こっちの 方が あっちより 安いです。(Cái bên này rẻ hơn cái đằng kia)
                </div>
                <div class="rule-meaning">
                    • <strong>この 掃除機の 方が 軽くて 静かです:</strong> Máy hút bụi này nhẹ và êm hơn.<br>
                    • <strong>A社より B社の 方が レビューが 高いです:</strong> Hãng B có đánh giá cao hơn hãng A.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">Aの パソコンは Bのより 軽くて、持ち運びに 便利ですよ。</div>
                        <div class="ex-vi">Máy tính A nhẹ hơn máy tính B nên mang đi lại rất tiện lợi.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('AのパソコンはBのより軽くて、持ち運びに便利ですよ')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>⭐</span> 2. Hỏi So Sánh: N1 と N2 と どちらが A ですか</h2>
            <span class="section-tag">Tham khảo ý kiến</span>
        </div>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">
                    • N1 と N2 と どちら（どっち）が A ですか。(Giữa N1 và N2, cái nào ... hơn?)<br>
                    ➔ [N] の 方が A です。(Cái N thì ... hơn)
                </div>
                <div class="rule-meaning">
                    Trong khẩu ngữ thân mật hàng ngày, <code>どちら</code> thường được nói thành <code>どっち</code>.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">白と 黒と どちらが 人気がありますか。</div>
                        <div class="ex-vi">Màu trắng và màu đen thì màu nào được ưa chuộng hơn ạ?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('白と黒とどちらが人気がありますか')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]

L12_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "こちらの 掃除機の [____] が、あちらより 軽くて 静かです。",
        "options": ["ほう", "より", "ほど", "だけ"],
        "correct": 0,
        "explain": "Cấu trúc so sánh hơn: 『N1 の ほうが N2 より A』 ➔ 「ほう」."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "「黒と 白と [____] が いいですか。」 ―― 「白の 方が いいです。」",
        "options": ["どちら", "だれ", "どこ", "いつ"],
        "correct": 0,
        "explain": "Hỏi so sánh giữa 2 đối tượng dùng từ để hỏi: 『どちら (どっち)』."
    },
    {
        "id": 3,
        "category": "Từ vựng",
        "q": "実際に 買った 人の 感想や 評価を 書いた 文章は [____] です。",
        "options": ["レビュー", "サイズ", "ポイント", "メニュー"],
        "correct": 0,
        "explain": "Đánh giá, bình luận của người mua là 「レビュー (review / 口コミ)」."
    },
    {
        "id": 4,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「比べる」 đọc là gì?",
        "options": ["くらべる", "ならべる", "えらべる", "しらべる"],
        "correct": 0,
        "explain": "比べる đọc là 「くらべる」 (TỈ - so sánh đối chiếu)."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "送料（tiền ship）を 払わなくても いい サービスを [____] と 言います。",
        "options": ["そうりょうむりょう", "わりびき", "ねだん", "せいほう"],
        "correct": 0,
        "explain": "Freeship không mất tiền vận chuyển là 「送料無料 (そうりょうむりょう)」."
    },
    {
        "id": 6,
        "category": "Chữ Hán",
        "q": "Từ trái nghĩa với 「重い (おもい - nặng)」 là từ nào?",
        "options": ["軽い (かるい)", "安い (やすい)", "低い (ひくい)", "薄い (うすい)"],
        "correct": 0,
        "explain": "重い (nặng) đối nghĩa với 軽い (nhẹ)."
    },
    {
        "id": 7,
        "category": "Từ vựng",
        "q": "20% [____] の セール中なので、いつもより 安く 買えます。",
        "options": ["わりびき", "ねだん", "ほし", "サイズ"],
        "correct": 0,
        "explain": "Giảm giá 20%: 「20% 割引 (わりびき)」."
    },
    {
        "id": 8,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「便利」 có âm Hán Việt là gì?",
        "options": ["TIỆN LỢI", "TIỆN ĐỒ", "CÁT LỢI", "LỢI DỤNG"],
        "correct": 0,
        "explain": "便利 có âm Hán Việt là TIỆN LỢI."
    },
    {
        "id": 9,
        "category": "Ngữ pháp",
        "q": "バスより 電車の [____] が 時間が 正確です。",
        "options": ["ほう", "より", "から", "まで"],
        "correct": 0,
        "explain": "Tàu điện thì đúng giờ hơn xe buýt: 電車のほうが."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「値段」 đọc là gì?",
        "options": ["ねだん", "ちくだん", "ねたん", "ばいだん"],
        "correct": 0,
        "explain": "値段 đọc là 「ねだん」 (TRỊ ĐOẠN - giá tiền)."
    },
    {
        "id": 11,
        "category": "Từ vựng",
        "q": "どちらの 商品を 買うか、なかなか 決められずに [____] います。",
        "options": ["まよって", "よろこんで", "つかれて", "こわれて"],
        "correct": 0,
        "explain": "Đang phân vân đắn đo: 迷います ➔ 「迷っています (まよっています)」."
    },
    {
        "id": 12,
        "category": "Hội thoại",
        "q": "「この 掃除機、星 5つの うち [____] 4.8で とても 評判が いいですよ。」",
        "options": ["ほし", "つき", "ひ", "みず"],
        "correct": 0,
        "explain": "Xếp hạng đánh giá theo sao: 「星 (ほし)」."
    },
    {
        "id": 13,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「無料」 gồm 2 chữ nào?",
        "options": ["VÔ + LIỆU", "VÔ + LÝ", "HỮU + LIỆU", "VÔ + LƯỢNG"],
        "correct": 0,
        "explain": "無料 gồm VÔ (無) và LIỆU (料) ➔ không mất tiền, miễn phí."
    },
    {
        "id": 14,
        "category": "Từ vựng",
        "q": "お買い物で たまった [____] を 使って、割引を 受けました。",
        "options": ["ポイント", "レビュー", "サイズ", "メッセージ"],
        "correct": 0,
        "explain": "Điểm thưởng tích lũy mua sắm: 「ポイント (point)」."
    },
    {
        "id": 15,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「割引」 gồm 2 chữ nào?",
        "options": ["CÁT + DẪN", "LỢI + DẪN", "CÁT + DỤNG", "CHI + DẪN"],
        "correct": 0,
        "explain": "割引 gồm chữ CÁT (割 - chia cắt) và DẪN (引 - kéo/bớt lại) ➔ giảm giá chiết khấu."
    }
]
