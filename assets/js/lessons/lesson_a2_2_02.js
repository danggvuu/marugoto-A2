/* Marugoto A2-2 Bài 2 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "ホームパーティー",
    "kana": "ホームパーティー",
    "kanji": "ホームパーティー",
    "romaji": "ho-mupa-ti-",
    "vi": "Tiệc gia đình, tiệc tại gia",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7572\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7572)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Tiệc gia đìn</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "スーツ",
    "kana": "スーツ",
    "kanji": "スーツ",
    "romaji": "su-tsu",
    "vi": "Bộ vest, âu phục",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9695\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9695)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤵</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Bộ vest, âu </text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "サリー",
    "kana": "サリー",
    "kanji": "サリー",
    "romaji": "sari-",
    "vi": "Sari (trang phục truyền thống Ấn Độ)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2197\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2197)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥻</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Sari (trang </text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "セーター",
    "kana": "セーター",
    "kanji": "セーター",
    "romaji": "se-ta-",
    "vi": "Áo len",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4339\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4339)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Áo len</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "ネクタイをします",
    "kana": "ネクタイを します",
    "kanji": "ネクタイをします",
    "romaji": "nekutai o shimasu",
    "vi": "Thắt cà vạt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6827\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6827)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Thắt cà vạt</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "スーツを着ます",
    "kana": "スーツを きます",
    "kanji": "スーツを着ます",
    "romaji": "su-tsu o kimasu",
    "vi": "Mặc vest (áo, thân trên)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4011\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4011)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧥</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Mặc vest (áo</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "めがねをかけます",
    "kana": "めがねを かけます",
    "kanji": "めがねをかけます",
    "romaji": "megane o kakemasu",
    "vi": "Đeo kính",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6912\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6912)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👓</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Đeo kính</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "ぼうしをかぶります",
    "kana": "ぼうしを かぶります",
    "kanji": "ぼうしをかぶります",
    "romaji": "boushi o kaburimasu",
    "vi": "Đội mũ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7791\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7791)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧢</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Đội mũ</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "スカートをはきます",
    "kana": "スカートを はきます",
    "kanji": "スカートをはきます",
    "romaji": "suka-to o hakimasu",
    "vi": "Mặc váy (phần dưới)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1827\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1827)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👗</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Mặc váy (phầ</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "くつをはきます",
    "kana": "くつを はきます",
    "kanji": "くつをはきます",
    "romaji": "kutsu o hakimasu",
    "vi": "Đi giày",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1436\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1436)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👟</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Đi giày</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "Pにすわります",
    "kana": "Pに すわります",
    "kanji": "Pに座ります",
    "romaji": "P ni suwarimasu",
    "vi": "Ngồi ở vị trí P",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5447\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5447)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪑</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Ngồi ở vị tr</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "Pにたちます",
    "kana": "Pに たちます",
    "kanji": "Pに立ちます",
    "romaji": "P ni tachimasu",
    "vi": "Đứng ở vị trí P",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7926\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7926)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧍</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Đứng ở vị tr</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "笑います",
    "kana": "わらいます",
    "kanji": "笑います",
    "romaji": "waraimasu",
    "vi": "Cười",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5180\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5180)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😄</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Cười</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "泣きます",
    "kana": "なきます",
    "kanji": "泣きます",
    "romaji": "nakimasu",
    "vi": "Khóc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_381\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_381)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😢</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Khóc</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "厳しい",
    "kana": "きびしい",
    "kanji": "厳しい",
    "romaji": "kibishii",
    "vi": "Nghiêm khắc, khắt khe",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_826\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_826)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧐</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Nghiêm khắc,</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "ご主人",
    "kana": "ごしゅじん",
    "kanji": "ご主人",
    "romaji": "goshujin",
    "vi": "Chồng (người khác)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2206\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2206)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👨</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Chồng (người</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 2 (A2-2)",
    "jp": "頭がいい",
    "kana": "あたまが いい",
    "kanji": "頭がいい",
    "romaji": "atama ga ii",
    "vi": "Thông minh, sáng dạ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9853\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9853)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧠</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Thông minh, </text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "着ます",
    "vi": "Mặc (áo, vest)",
    "te": "着て",
    "form1": "着ています",
    "form2": "着た",
    "form3": "着る"
  },
  {
    "masu": "履きます",
    "vi": "Mặc váy/đi giày",
    "te": "履いて",
    "form1": "履いています",
    "form2": "履いた",
    "form3": "履く"
  },
  {
    "masu": "被ります",
    "vi": "Đội mũ",
    "te": "被って",
    "form1": "被っています",
    "form2": "被った",
    "form3": "被る"
  },
  {
    "masu": "掛けます",
    "vi": "Đeo kính",
    "te": "掛けて",
    "form1": "掛けています",
    "form2": "掛けた",
    "form3": "掛ける"
  },
  {
    "masu": "します",
    "vi": "Thắt cà vạt / đeo phụ kiện",
    "te": "して",
    "form1": "しています",
    "form2": "した",
    "form3": "する"
  },
  {
    "masu": "座ります",
    "vi": "Ngồi",
    "te": "座って",
    "form1": "座っています",
    "form2": "座った",
    "form3": "座る"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "あそこで めがねを [____] いる 人は 田中さんです。",
    "options": [
      "かけて",
      "きて",
      "はいて",
      "かぶって"
    ],
    "correct": 0,
    "explain": "Động từ đi với kính mắt 「めがね」 là 「掛けます (かけます)」. Khi bổ nghĩa miêu tả trạng thái: 「めがねをかけている人」 (người đang đeo kính)."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "山田さんは きょう 黒いスーツを [____] います。",
    "options": [
      "着て",
      "履いて",
      "掛けて",
      "被って"
    ],
    "correct": 0,
    "explain": "Bộ vest 「スーツ」 là trang phục mặc ở phần thân trên, dùng động từ 「着ます (きます)」 ➔ 「着ています」."
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "あのかわいい ぼうしを [____] いる 子どもは だれですか。",
    "options": [
      "かぶって",
      "はいて",
      "きて",
      "して"
    ],
    "correct": 0,
    "explain": "Mũ 「ぼうし」 là vật đội lên đầu, dùng động từ 「被ります (かぶります)」 ➔ 「被っている (かぶっている)」."
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "きょうは 寒いですね。あたたかい [____] を 着ましょう。",
    "options": [
      "セーター",
      "ネクタイ",
      "サリー",
      "めがね"
    ],
    "correct": 0,
    "explain": "Trời lạnh thì mặc áo len ấm áp: 「セーター」."
  },
  {
    "id": 5,
    "category": "Ngữ pháp",
    "q": "新しい くつを [____] 出かけました。",
    "options": [
      "はいて",
      "きて",
      "かぶって",
      "かけて"
    ],
    "correct": 0,
    "explain": "Giày dép 「くつ」 mặc/xỏ từ thắt lưng trở xuống, dùng động từ 「履きます (はきます)」."
  },
  {
    "id": 6,
    "category": "Ngữ pháp",
    "q": "会社へ 行くとき、いつも ネクタイを [____]。",
    "options": [
      "します",
      "きます",
      "はきます",
      "かぶります"
    ],
    "correct": 0,
    "explain": "Cà vạt 「ネクタイ」 thuộc nhóm phụ kiện thắt/đeo, động từ chuẩn là 「します」 (hoặc 締めます)."
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "「鈴木さんは どの人ですか。」 ―― 「窓のそばに [____] 人です。」",
    "options": [
      "立っている",
      "着ている",
      "履いている",
      "歌っている"
    ],
    "correct": 0,
    "explain": "Chỉ vị trí tư thế: 「窓のそばに立っている人」 (Là người đang đứng cạnh cửa sổ)."
  },
  {
    "id": 8,
    "category": "Từ vựng",
    "q": "あの 先生は いつも 真面目で、とても [____] です。",
    "options": [
      "きびしい",
      "ひくい",
      "みじかい",
      "ながい"
    ],
    "correct": 0,
    "explain": "Thầy giáo luôn nghiêm túc và 'nghiêm khắc': 「厳しい (きびしい)」."
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "「あの [____] は だれの ご主人ですか。」 ―― 「佐藤さんの夫ですよ。」",
    "options": [
      "男の人",
      "女の子",
      "歌手",
      "妹"
    ],
    "correct": 0,
    "explain": "ご主人 là chồng của người khác (phái nam) ➔ 「男の人 (người đàn ông đó)」."
  },
  {
    "id": 10,
    "category": "Từ vựng",
    "q": "赤ちゃんが えがおで [____] います。かわいいですね。",
    "options": [
      "笑って",
      "泣いて",
      "怒って",
      "歌って"
    ],
    "correct": 0,
    "explain": "Khuôn mặt cười tươi (えがお) thì hành động tương ứng là cười: 「笑っています (わらっています)」."
  },
  {
    "id": 11,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「兄弟」 có cách đọc chuẩn là gì?",
    "options": [
      "きょうだい",
      "あにてい",
      "けいてい",
      "おとうとあに"
    ],
    "correct": 0,
    "explain": "兄弟 đọc là 「きょうだい」 (HUYNH ĐỆ - Anh em)."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ 「水族館」 có nghĩa là gì?",
    "options": [
      "Thủy cung (viện hải dương)",
      "Hồ bơi",
      "Công viên nước",
      "Bến thuyền"
    ],
    "correct": 0,
    "explain": "水族館 (すいぞくかん) là viện bảo tàng/thủy cung trưng bày sinh vật dưới nước."
  },
  {
    "id": 13,
    "category": "Chữ Hán",
    "q": "Từ trái nghĩa với 「長い (ながい)」 là từ nào?",
    "options": [
      "短い (みじかい)",
      "低い (ひくい)",
      "高い (たかい)",
      "近い (ちかい)"
    ],
    "correct": 0,
    "explain": "長い (dài) đối nghĩa với 短い (ngắn)."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「歌手」 gồm hai chữ nào ghép lại?",
    "options": [
      "CA + THỦ",
      "HOA + THỦ",
      "CA + NHÂN",
      "HOA + NHÂN"
    ],
    "correct": 0,
    "explain": "歌手 gồm chữ 歌 (CA - bài hát) và 手 (THỦ - bàn tay / người chuyên làm việc gì) ➔ ca sĩ."
  },
  {
    "id": 15,
    "category": "Ngữ pháp",
    "q": "あの ソファーに [____] いる 人は どなたですか。",
    "options": [
      "すわって",
      "たって",
      "はいて",
      "かぶって"
    ],
    "correct": 0,
    "explain": "Đi với ghế sofa 「ソファーに」 là hành động ngồi: 「座っている (すわっている)」."
  }
];

// Audio TTS handled globally via assets/js/audio-engine.js

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
    const elForm3 = document.getElementById('morphMashou');
    if (elMasu) elMasu.textContent = v.masu;
    if (elVi) elVi.textContent = v.vi;
    if (elTe) elTe.textContent = v.te;
    if (elForm1) elForm1.textContent = v.form1;
    if (elForm2) elForm2.textContent = v.form2;
    if (elForm3) elForm3.textContent = v.form3;
}

// Render Flashcards
function initFlashcards() {
    const grid = document.getElementById('flashcardGrid');
    if (!grid) return;
    grid.innerHTML = '';
    VOCAB_DATA.forEach(v => {
        const card = document.createElement('div');
        card.className = 'fc-item';
        card.onclick = () => {
            if (typeof speakText === 'function') speakText(v.kana || v.jp);
        };
        card.innerHTML = `
            <div class="fc-svg-wrap">${v.svg}</div>
            <div class="fc-content">
                <div class="fc-jp">${v.jp}</div>
                <div class="fc-kana">${v.kana}</div>
                <div class="fc-vi">${v.vi}</div>
            </div>
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
        const optsHtml = q.options.map((opt, oIdx) => `
            <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${qIdx}, ${oIdx})">${opt}</button>
        `).join('');
        qBox.innerHTML = `
            <div class="quiz-q"><b>Câu ${qIdx + 1}:</b> ${q.q}</div>
            <div class="quiz-opts">${optsHtml}</div>
            <div class="quiz-explain" id="explain-${qIdx}">💡 ${q.explain}</div>
        `;
        c.appendChild(qBox);
    });
}

function checkQuizAnswer(btn, qIdx, oIdx) {
    const q = QUIZ_DATA[qIdx];
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
