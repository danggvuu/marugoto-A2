/* Marugoto A2-2 Bài 14 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "お寺",
    "kana": "おてら",
    "kanji": "お寺",
    "romaji": "otera",
    "vi": "Chùa chiền Phật giáo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dff54d45b4bd384a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dff54d45b4bd384a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛕</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "神社",
    "kana": "じんじゃ",
    "kanji": "神社",
    "romaji": "jinja",
    "vi": "Đền thần đạo Shinto",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9f210cb29937fc72\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9f210cb29937fc72)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⛩️</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "城",
    "kana": "しろ",
    "kanji": "城",
    "romaji": "shiro",
    "vi": "Lâu đài, thành cổ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bab0e8fe52d84f6b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bab0e8fe52d84f6b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏯</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "歴史",
    "kana": "れきし",
    "kanji": "歴史",
    "romaji": "rekishi",
    "vi": "Lịch sử",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0a23570855ef4d6d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0a23570855ef4d6d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "伝統",
    "kana": "でんとう",
    "kanji": "伝統",
    "romaji": "dentou",
    "vi": "Truyền thống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6e40584bc1e46434\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6e40584bc1e46434)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎎</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "建物",
    "kana": "たてもの",
    "kanji": "建物",
    "romaji": "tatemono",
    "vi": "Tòa nhà, công trình kiến trúc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_15161893b13e8669\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_15161893b13e8669)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏛️</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "国宝",
    "kana": "こくほう",
    "kanji": "国宝",
    "romaji": "kokuhou",
    "vi": "Bảo vật quốc gia",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b0c34c8baf42d7a4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b0c34c8baf42d7a4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👑</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "庭園",
    "kana": "ていえん",
    "kanji": "庭園",
    "romaji": "teien",
    "vi": "Khu vườn cảnh kiểu Nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b2e4e16f290aba52\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b2e4e16f290aba52)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌳</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "桜",
    "kana": "さくら",
    "kanji": "桜",
    "romaji": "sakura",
    "vi": "Hoa anh đào",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2887716b833f2968\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2887716b833f2968)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌸</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "紅葉",
    "kana": "こうよう",
    "kanji": "紅葉",
    "romaji": "kouyou",
    "vi": "Lá đỏ mùa thu (momiji)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6bde2b4f08fadfec\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6bde2b4f08fadfec)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍁</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "観光客",
    "kana": "かんこうきゃく",
    "kanji": "観光客",
    "romaji": "kankoukyaku",
    "vi": "Khách du lịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ef7ca9d1296ea0d1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ef7ca9d1296ea0d1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎒</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "ガイド",
    "kana": "ガイド",
    "kanji": "ガイド",
    "romaji": "gaido",
    "vi": "Hướng dẫn viên du lịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_159ca30cf1cf2dde\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_159ca30cf1cf2dde)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚩</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "昔",
    "kana": "むかし",
    "kanji": "昔",
    "romaji": "mukashi",
    "vi": "Ngày xưa, thời xưa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_35a12272d8803247\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_35a12272d8803247)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "時代",
    "kana": "じだい",
    "kanji": "時代",
    "romaji": "jidai",
    "vi": "Thời đại, triều đại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8bd3be56867bf2f2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8bd3be56867bf2f2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗡️</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "建てる",
    "kana": "たてる",
    "kanji": "建てる",
    "romaji": "tateru",
    "vi": "Xây dựng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dc1cc385952d3d37\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dc1cc385952d3d37)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏗️</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "残る",
    "kana": "のこる",
    "kanji": "残る",
    "romaji": "nokoru",
    "vi": "Còn sót lại, lưu giữ đến nay",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c299b23f975813c4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c299b23f975813c4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛡️</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "訪れる",
    "kana": "おとずれる",
    "kanji": "訪れる",
    "romaji": "otozureru",
    "vi": "Ghé thăm, viếng thăm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_715bacb33fa3166a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_715bacb33fa3166a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚶‍♂️</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "素晴らしい",
    "kana": "すばらしい",
    "kanji": "素晴らしい",
    "romaji": "subarashii",
    "vi": "Tuyệt vời, tráng lệ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a3c06c595f99cf83\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a3c06c595f99cf83)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌟</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "静か（な）",
    "kana": "しずか（な）",
    "kanji": "静か（な）",
    "romaji": "shizuka(na)",
    "vi": "Thanh tịnh, yên bình",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c9c89dfe43663a18\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c9c89dfe43663a18)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕊️</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "案内する",
    "kana": "あんないする",
    "kanji": "案内する",
    "romaji": "annaisuru",
    "vi": "Dẫn đường, thuyết minh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2b70350aebeb929a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2b70350aebeb929a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗣️</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "たてます",
    "vi": "Xây dựng",
    "te": "たてて",
    "form1": "たてられた (được xây dựng)",
    "form2": "たてた (đã xây)",
    "form3": "たてる"
  },
  {
    "masu": "のこります",
    "vi": "Còn lưu giữ",
    "te": "のこって",
    "form1": "のこっている (đang còn lưu lại)",
    "form2": "のこった",
    "form3": "のこる"
  },
  {
    "masu": "おとずれます",
    "vi": "Ghé thăm",
    "te": "おとずれて",
    "form1": "おとずれるひと (người ghé thăm)",
    "form2": "おとずれた",
    "form3": "おとずれる"
  },
  {
    "masu": "まもります",
    "vi": "Gìn giữ, bảo vệ",
    "te": "まもって",
    "form1": "まもられている (được bảo tồn)",
    "form2": "まもった",
    "form3": "まもる"
  },
  {
    "masu": "つたえます",
    "vi": "Truyền lại",
    "te": "つたえて",
    "form1": "つたえられている (được tương truyền)",
    "form2": "つたえた",
    "form3": "つたえる"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "これは 400年前に [____] 古い お城です。",
    "options": [
      "建てた",
      "建てる",
      "建てられた",
      "建ち"
    ],
    "correct": 2,
    "explain": "Được xây dựng từ 400 năm trước (thể bị động bổ nghĩa danh từ): 「建てられたお城」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "京都には、昔の 伝統が たくさん [____] 町が あります。",
    "options": [
      "残っている",
      "残った",
      "残る",
      "残して"
    ],
    "correct": 0,
    "explain": "Thành phố đang còn lưu giữ lại nhiều truyền thống: 「残っている町」."
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "赤い 鳥居（とりい）が たくさん 並んでいる 神道の 施設は [____] です。",
    "options": [
      "おてら",
      "しろ",
      "ていえん",
      "じんじゃ"
    ],
    "correct": 3,
    "explain": "Đền thần đạo với cổng Torii màu đỏ là 「神社 (じんじゃ)」."
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「歴史」 có cách đọc là gì?",
    "options": [
      "れきじ",
      "りきし",
      "れっし",
      "れきし"
    ],
    "correct": 3,
    "explain": "歴史 đọc là 「れきし」 (LỊCH SỬ)."
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "秋に なると 木の 葉が 赤や 黄色に 変わる 現象を [____] と 言います。",
    "options": [
      "こうよう",
      "さくら",
      "まつり",
      "ていえん"
    ],
    "correct": 0,
    "explain": "Lá đỏ mùa thu là 「紅葉 (こうよう / もみじ)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「お寺」 có âm Hán Việt là gì?",
    "options": [
      "TỰ",
      "XÃ",
      "THÀNH",
      "ĐÌNH"
    ],
    "correct": 0,
    "explain": "お寺 có âm Hán Việt là TỰ (chùa chiền)."
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "「京都の 街は どうでしたか。」 ―― 「古い 建物が たくさん あって、とても [____] でした。」",
    "options": [
      "すばらしい",
      "すばらしくない",
      "すばらしかった",
      "すばらしく"
    ],
    "correct": 2,
    "explain": "Khen chuyến đi trong quá khứ: tính từ đuôi い ở quá khứ là 「すばらしかった」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ 「建物」 gồm 2 chữ nào ghép lại?",
    "options": [
      "THIẾT + VẬT",
      "KIẾN + VẬT",
      "TẠO + VẬT",
      "KIẾN + THÀNH"
    ],
    "correct": 1,
    "explain": "建物 gồm KIẾN (建) và VẬT (物) ➔ công trình xây dựng, tòa nhà."
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "国にとって 非常に 価値が 高い 貴重な 宝物は [____] に 指定されます。",
    "options": [
      "おみやげ",
      "しゃしん",
      "こくほう",
      "ガイド"
    ],
    "correct": 2,
    "explain": "Bảo vật quốc gia là 「国宝 (こくほう)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「城」 đọc là gì?",
    "options": [
      "しろ",
      "まち",
      "むら",
      "いえ"
    ],
    "correct": 0,
    "explain": "城 đọc là 「しろ」 (hoặc âm On là じょう trong 大阪城)."
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "この 神社は 平安時代に [____] と 言われています。",
    "options": [
      "できる",
      "できた",
      "できて",
      "できたら"
    ],
    "correct": 1,
    "explain": "Tương truyền rằng đã được tạo dựng: 『V-た と言われています』 ➔ 「できたと言われています」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ 「伝統」 có âm Hán Việt là gì?",
    "options": [
      "TRUYỀN TỔNG",
      "TRUYỀN THỐNG",
      "TRUYỀN HỆ",
      "QUAN TRUYỀN"
    ],
    "correct": 1,
    "explain": "伝統 có âm Hán Việt là TRUYỀN THỐNG."
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "観光地を 案内して 説明して くれる 人を [____] と 呼びます。",
    "options": [
      "てんいん",
      "いしゃ",
      "さっか",
      "ガイド"
    ],
    "correct": 3,
    "explain": "Hướng dẫn viên du lịch là 「ガイド (tour guide)」."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「昔」 đọc là gì?",
    "options": [
      "いま",
      "まえ",
      "むかし",
      "あした"
    ],
    "correct": 2,
    "explain": "昔 đọc là 「むかし」 (TÍCH - ngày xưa)."
  },
  {
    "id": 15,
    "category": "Hội thoại",
    "q": "「お寺の 庭は [____] で、心が 落ち着きました。」",
    "options": [
      "にぎやか",
      "しずか",
      "べんり",
      "ふべん"
    ],
    "correct": 1,
    "explain": "Khu vườn chùa thanh tịnh yên ả: 「静か (しずか) で」."
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
    const elForm3 = document.getElementById('morphMashou');

    if (elMasu) elMasu.textContent = v.masu || '---';
    if (elVi) elVi.textContent = v.vi || '---';
    if (elTe) elTe.textContent = v.te || '---';
    if (elForm1) elForm1.textContent = v.form1 || '---';
    if (elForm2) elForm2.textContent = v.form2 || '---';
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
        const optsHtml = q.options.map((opt, oIdx) => `
            <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${qIdx}, ${oIdx}, 'a22-reviewed-v2')">${escapeLessonText(opt)}</button>
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
    if (revision !== 'a22-reviewed-v2' || btn.disabled) return;
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
