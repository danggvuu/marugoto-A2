/* Marugoto A2-2 Bài 6 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "ツアー",
    "kana": "ツアー",
    "kanji": "ツアー",
    "romaji": "tsua-",
    "vi": "Tour",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c0323ea228dc7712\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c0323ea228dc7712)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧳</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "ショー",
    "kana": "ショー",
    "kanji": "ショー",
    "romaji": "sho-",
    "vi": "Show, buổi trình diễn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_70b72a3bc1e207a5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_70b72a3bc1e207a5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎭</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "イルカ",
    "kana": "イルカ",
    "kanji": "イルカ",
    "romaji": "iruka",
    "vi": "Cá heo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_953cf3fcff82dc61\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_953cf3fcff82dc61)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐬</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "水族館",
    "kana": "すいぞくかん",
    "kanji": "水族館",
    "romaji": "suizokukan",
    "vi": "Thủy cung",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f4606ef470d731e6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f4606ef470d731e6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐠</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "パンフレット",
    "kana": "パンフレット",
    "kanji": "パンフレット",
    "romaji": "panfuretto",
    "vi": "Tờ giới thiệu, quảng cáo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3327bb9abc2879bc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3327bb9abc2879bc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📄</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "森",
    "kana": "もり",
    "kanji": "森",
    "romaji": "mori",
    "vi": "Rừng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1103afce6036c87d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1103afce6036c87d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌲</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "釣り",
    "kana": "つり",
    "kanji": "釣り",
    "romaji": "tsuri",
    "vi": "Câu cá",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6ede786e82d8b979\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6ede786e82d8b979)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎣</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "ガラス",
    "kana": "ガラス",
    "kanji": "ガラス",
    "romaji": "garasu",
    "vi": "Thủy tinh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6526372146168741\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6526372146168741)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪟</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "思い出",
    "kana": "おもいで",
    "kanji": "思い出",
    "romaji": "omoide",
    "vi": "Kỷ niệm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e3e1138600900207\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e3e1138600900207)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📸</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "珍しい動物",
    "kana": "めずらしいどうぶつ",
    "kanji": "珍しい動物",
    "romaji": "mezurashii doubutsu",
    "vi": "Động vật hiếm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ef46c28649be9937\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ef46c28649be9937)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐼</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "人気があります",
    "kana": "にんきがあります",
    "kanji": "人気があります",
    "romaji": "ninki ga arimasu",
    "vi": "Được yêu thích, ưa chuộng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_66eebabfb6a764d4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_66eebabfb6a764d4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌟</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "楽しみます",
    "kana": "たのしみます",
    "kanji": "楽しみます",
    "romaji": "tanoshimimasu",
    "vi": "Tận hưởng niềm vui (Nを楽しむ)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b631f206c9b0455f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b631f206c9b0455f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "女性",
    "kana": "じょせい",
    "kanji": "女性",
    "romaji": "josei",
    "vi": "Nữ giới",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a0d4d743e86ee111\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a0d4d743e86ee111)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👩</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "男性",
    "kana": "だんせい",
    "kanji": "男性",
    "romaji": "dansei",
    "vi": "Nam giới",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e5f74544da65e9ef\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e5f74544da65e9ef)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👨</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "アンケート",
    "kana": "アンケート",
    "kanji": "アンケート",
    "romaji": "anke-to",
    "vi": "Bảng khảo sát",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bb22939c90f650db\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bb22939c90f650db)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📋</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "参加します",
    "kana": "さんかします",
    "kanji": "参加します",
    "romaji": "sanka shimasu",
    "vi": "Tham gia (Nに参加します)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_42c0968fea412786\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_42c0968fea412786)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙋</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "およぎます",
    "vi": "Bơi",
    "te": "およいで",
    "form1": "およいだり (khi thì bơi...)",
    "form2": "およぐことができる (có thể bơi)",
    "form3": "およぐ",
    "form2Label": "Khả năng: Vることができる"
  },
  {
    "masu": "とります",
    "vi": "Chụp (ảnh)",
    "te": "とって",
    "form1": "とったり (khi thì chụp ảnh...)",
    "form2": "とることができる (có thể chụp)",
    "form3": "とる",
    "form2Label": "Khả năng: Vることができる"
  },
  {
    "masu": "つくります",
    "vi": "Làm ra",
    "te": "つくって",
    "form1": "つくったり (làm cái này cái kia...)",
    "form2": "つくることができる (có thể tự làm)",
    "form3": "つくる",
    "form2Label": "Khả năng: Vることができる"
  },
  {
    "masu": "たいけんします",
    "vi": "Trải nghiệm",
    "te": "たいけんして",
    "form1": "たいけんしたり",
    "form2": "たいけんすることができる",
    "form3": "たいけんする",
    "form2Label": "Khả năng: Vることができる"
  },
  {
    "masu": "あんないします",
    "vi": "Hướng dẫn",
    "te": "あんないして",
    "form1": "あんないしたり",
    "form2": "あんないすることができる",
    "form3": "あんないする",
    "form2Label": "Khả năng: Vることができる"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "おしろの中が [____]。",
    "options": [
      "見られます",
      "見たり",
      "見ること",
      "見たし"
    ],
    "correct": 0,
    "explain": "見られます là thể khả năng của 見る.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "今日のツアーはおどりも見た [____]、音楽も聞いたし、楽しめました。",
    "options": [
      "たり",
      "ので",
      "し",
      "なら"
    ],
    "correct": 2,
    "explain": "～し liệt kê nhiều lý do/đặc điểm; mỗi vế dùng し.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "旅行から 帰ったあと、家族や 友達に 配る お菓子などの プレゼントを [____] と 言います。",
    "options": [
      "しゃしん",
      "シーサー",
      "おみやげ",
      "にもつ"
    ],
    "correct": 2,
    "explain": "Quà lưu niệm, đặc sản mua về tặng người thân: 「お土産 (おみやげ)」."
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「観光地」 có cách đọc nào?",
    "options": [
      "じょせい",
      "だんせい",
      "かんこうち",
      "どうぶつ"
    ],
    "correct": 2,
    "explain": "観光地 đọc là 「かんこうち」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "観光地"
  },
  {
    "id": 5,
    "category": "Ngữ pháp",
    "q": "ここではイルカのショーを [____]。",
    "options": [
      "見ますこと",
      "見られます",
      "見たり",
      "見て"
    ],
    "correct": 1,
    "explain": "見られます diễn tả có thể xem.",
    "grammarScope": "official"
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "沖縄の 家の 屋根や 門に 置かれている 獅子（しし）の 像は [____] です。",
    "options": [
      "シーサー",
      "コップ",
      "ガラス",
      "ダイビング"
    ],
    "correct": 0,
    "explain": "Tượng thần hộ mệnh trừ tà truyền thống ở Okinawa là 「シーサー (Shisa)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「女性」 có nghĩa là gì?",
    "options": [
      "Nam giới",
      "Động vật",
      "Không khí",
      "Phụ nữ"
    ],
    "correct": 3,
    "explain": "女性 nghĩa là Phụ nữ.",
    "scopeKanji": "女性"
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「男性」 có cách đọc nào?",
    "options": [
      "どうぶつ",
      "だんせい",
      "くうき",
      "りょうきん"
    ],
    "correct": 1,
    "explain": "男性 đọc là 「だんせい」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "男性"
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "海の中に もぐって カラフルな 魚を 見る スポーツは [____] です。",
    "options": [
      "ダイビング",
      "サッカー",
      "ジョギング",
      "テニス"
    ],
    "correct": 0,
    "explain": "Lặn biển ngắm cá: 「ダイビング (scuba diving)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「動物」 có cách đọc nào?",
    "options": [
      "くうき",
      "どうぶつ",
      "りょうきん",
      "むりょう"
    ],
    "correct": 1,
    "explain": "動物 đọc là 「どうぶつ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "動物"
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "沖縄旅行はどうでしたか。海が青くて、とても [____]。",
    "options": [
      "きれいでした",
      "きれいだったです",
      "きれいですた",
      "きれいだでした"
    ],
    "correct": 0,
    "explain": "な形容詞 きれい quá khứ lịch sự là きれいでした.",
    "grammarScope": "official"
  },
  {
    "id": 12,
    "category": "Từ vựng",
    "q": "心に 深く 残る 忘れられない 楽しい 記憶を [____] と 言います。",
    "options": [
      "おみやげ",
      "けしき",
      "じゅんび",
      "おもいで"
    ],
    "correct": 3,
    "explain": "Kỷ niệm đẹp đáng nhớ là 「思い出 (おもいで)」."
  },
  {
    "id": 13,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「空気」 có nghĩa là gì?",
    "options": [
      "Giá, phí",
      "Không khí",
      "Miễn phí",
      "Sáng"
    ],
    "correct": 1,
    "explain": "空気 nghĩa là Không khí.",
    "scopeKanji": "空気"
  },
  {
    "id": 14,
    "category": "Ngữ pháp",
    "q": "この水族館では、イルカのショーが [____]。",
    "options": [
      "見たり",
      "見るし",
      "見られます",
      "見て"
    ],
    "correct": 2,
    "explain": "Thể khả năng của 見る là 見られる／見られます.",
    "grammarScope": "official"
  },
  {
    "id": 15,
    "category": "Từ vựng",
    "q": "「沖縄へ 行くのは 今回が [____] ですか。」 ―― 「はい、初めてです。」",
    "options": [
      "何人",
      "何時",
      "何分",
      "何回目"
    ],
    "correct": 3,
    "explain": "Hỏi lần thứ mấy: 「何回目 (なんかいめ)」."
  }
];

function escapeLessonText(value) {
    return String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// Render Verb Lab
function initVerbLab() {
    const row = document.getElementById('verbSelectorRow');
    if (!row || !VERB_DATA.length) return;
    row.innerHTML = '';
    VERB_DATA.forEach((v, idx) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `btn-verb-chip ${idx === 0 ? 'active' : ''}`;
        btn.textContent = `${v.masu} (${v.vi})`;
        btn.onclick = () => selectVerb(idx);
        row.appendChild(btn);
    });
    selectVerb(0);
}

function selectVerb(idx) {
    const chips = document.querySelectorAll('.btn-verb-chip');
    chips.forEach((c, i) => c.classList.toggle('active', i === idx));
    const v = VERB_DATA[idx];
    if (!v) return;

    const elMasu = document.getElementById('morphMasu');
    const elVi = document.getElementById('morphVi');
    const elTe = document.getElementById('morphTe');
    const elForm1 = document.getElementById('morphTeIki');
    const elForm2 = document.getElementById('morphTeKi');
    const elForm2Label = document.getElementById('morphForm2Label');
    const elForm3 = document.getElementById('morphMashou');

    if (elMasu) elMasu.textContent = v.masu || '---';
    if (elVi) elVi.textContent = v.vi || '---';
    if (elTe) elTe.textContent = v.te || '---';
    if (elForm1) elForm1.textContent = v.form1 || '---';
    if (elForm2) elForm2.textContent = v.form2 || '---';
    if (elForm2Label) elForm2Label.textContent = v.form2Label || 'Ví dụ chia thể (bổ trợ)';
    if (elForm3) elForm3.textContent = v.form3 || '---';
}

// Render Flashcards
function initFlashcards() {
    const grid = document.getElementById('flashcardGrid');
    if (!grid) return;
    grid.innerHTML = '';
    VOCAB_DATA.forEach(v => {
        const card = document.createElement('button');
        card.type = 'button';
        card.className = 'fc-item';
        card.setAttribute('aria-label', `Nghe ${v.jp}`);
        card.onclick = () => {
            if (typeof speakText === 'function') speakText(v.kana || v.jp);
        };
        card.innerHTML = `
            <span class="fc-svg-wrap" aria-hidden="true">${v.svg}</span>
            <span class="fc-content">
                <span class="fc-jp" lang="ja">${escapeLessonText(v.jp)}</span>
                <span class="fc-kana" lang="ja">${escapeLessonText(v.kana)}</span>
                <span class="fc-romaji">${escapeLessonText(v.romaji)}</span>
                <span class="fc-vi">${escapeLessonText(v.vi)}</span>
                <span class="fc-listen">🔊 Nghe phát âm</span>
            </span>
        `;
        grid.appendChild(card);
    });
}

// Render Quiz
function initQuiz() {
    const c = document.getElementById('quizContainer');
    if (!c) return;
    c.innerHTML = '';
    QUIZ_DATA.forEach((q, qIdx) => {
        const qBox = document.createElement('div');
        qBox.className = 'quiz-card';
        const revision = q.reviewVersion || 'a22-reviewed-v2';
        const optsHtml = q.options.map((opt, oIdx) => `
            <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${qIdx}, ${oIdx}, '${revision}')">${escapeLessonText(opt)}</button>
        `).join('');
        qBox.innerHTML = `
            <div class="quiz-q"><b>Câu ${qIdx + 1}:</b> ${escapeLessonText(q.q)}</div>
            <div class="quiz-opts">${optsHtml}</div>
            <div class="quiz-explain" id="explain-${qIdx}">💡 ${escapeLessonText(q.explain)}</div>
        `;
        c.appendChild(qBox);
    });
}

function checkQuizAnswer(btn, qIdx, oIdx, revision) {
    const q = QUIZ_DATA[qIdx];
    if (!q || revision !== (q.reviewVersion || 'a22-reviewed-v2') || btn.disabled) return;
    const parent = btn.parentElement;
    const allBtns = parent.querySelectorAll('.quiz-opt');
    allBtns.forEach(b => b.disabled = true);
    if (oIdx === q.correct) {
        btn.classList.add('correct');
    } else {
        btn.classList.add('wrong');
        allBtns[q.correct].classList.add('correct');
    }
    const exp = document.getElementById(`explain-${qIdx}`);
    if (exp) exp.style.display = 'block';
}

function initLessonInteractive() {
    initVerbLab();
    initFlashcards();
    initQuiz();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLessonInteractive);
} else {
    initLessonInteractive();
}

if (typeof VOCAB_DATA !== "undefined") window.VOCAB_DATA = VOCAB_DATA;
