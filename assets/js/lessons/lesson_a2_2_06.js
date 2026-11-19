/* Marugoto A2-2 Bài 6 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "海",
    "kana": "うみ",
    "kanji": "海",
    "romaji": "umi",
    "vi": "Biển, đại dương",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_db1d1dffd4c54b0d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_db1d1dffd4c54b0d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌊</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "砂浜",
    "kana": "すなはま",
    "kanji": "砂浜",
    "romaji": "sunahama",
    "vi": "Bãi cát trắng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fcbbbd809a0564b0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fcbbbd809a0564b0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏖️</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "泳ぐ",
    "kana": "およぐ",
    "kanji": "泳ぐ",
    "romaji": "oyogu",
    "vi": "Bơi lội",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d69adfa185563b3c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d69adfa185563b3c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏊</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "ダイビング",
    "kana": "ダイビング",
    "kanji": "ダイビング",
    "romaji": "daibingu",
    "vi": "Lặn biển",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d826a9fd17699bc0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d826a9fd17699bc0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤿</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "写真",
    "kana": "しゃしん",
    "kanji": "写真",
    "romaji": "shashin",
    "vi": "Bức ảnh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d61271a973b7d40e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d61271a973b7d40e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📷</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "撮る",
    "kana": "とる",
    "kanji": "撮る",
    "romaji": "toru",
    "vi": "Chụp (ảnh)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b1e6c39fbebf0589\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b1e6c39fbebf0589)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📸</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "お土産",
    "kana": "おみやげ",
    "kanji": "お土産",
    "romaji": "omiyage",
    "vi": "Quà lưu niệm, đặc sản",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_de846ec88aa16c9b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_de846ec88aa16c9b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎁</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "シーサー",
    "kana": "シーサー",
    "kanji": "シーサー",
    "romaji": "shiisaa",
    "vi": "Tượng sư tử Shisa thần hộ mệnh Okinawa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c0488b647e84f757\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c0488b647e84f757)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🦁</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "ガラス",
    "kana": "ガラス",
    "kanji": "ガラス",
    "romaji": "garasu",
    "vi": "Thủy tinh, kính",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ddb5f8c61960445c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ddb5f8c61960445c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥛</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "コップ",
    "kana": "コップ",
    "kanji": "コップ",
    "romaji": "koppu",
    "vi": "Cái cốc, ly",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3371a8e62644d68f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3371a8e62644d68f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥃</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "工芸",
    "kana": "こうげい",
    "kanji": "工芸",
    "romaji": "kougei",
    "vi": "Thủ công mỹ nghệ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5bb16bc627876977\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5bb16bc627876977)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏺</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "体験",
    "kana": "たいけん",
    "kanji": "体験",
    "romaji": "taiken",
    "vi": "Trải nghiệm thực tế",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4c1aaabcaef736f2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4c1aaabcaef736f2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "水族館",
    "kana": "すいぞくかん",
    "kanji": "水族館",
    "romaji": "suizokukan",
    "vi": "Thủy cung",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f4606ef470d731e6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f4606ef470d731e6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐬</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "青い",
    "kana": "あおい",
    "kanji": "青い",
    "romaji": "aoi",
    "vi": "Xanh da trời / xanh lam biếc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cb0bff1cc3bcb811\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cb0bff1cc3bcb811)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔷</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "綺麗（な）",
    "kana": "きれい（な）",
    "kanji": "綺麗（な）",
    "romaji": "kirei(na)",
    "vi": "Đẹp, sạch sẽ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b4bc66b1af51b62a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b4bc66b1af51b62a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "感動する",
    "kana": "かんどうする",
    "kanji": "感動する",
    "romaji": "kandousuru",
    "vi": "Cảm động, xúc động bồi hồi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fac5065dbd5c53f6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fac5065dbd5c53f6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥹</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "思い出",
    "kana": "おもいで",
    "kanji": "思い出",
    "romaji": "omoide",
    "vi": "Kỷ niệm đẹp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f08e7ebe819fffbf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f08e7ebe819fffbf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💭</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "初めて",
    "kana": "はじめて",
    "kanji": "初めて",
    "romaji": "hajimete",
    "vi": "Lần đầu tiên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b4b3aecf297d67f3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b4b3aecf297d67f3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌱</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "また",
    "kana": "また",
    "kanji": "また",
    "romaji": "mata",
    "vi": "Lại nữa, lần nữa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5b5806d8cbc58cda\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5b5806d8cbc58cda)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 6 (A2-2)",
    "jp": "案内する",
    "kana": "あんないする",
    "kanji": "案内する",
    "romaji": "annaisuru",
    "vi": "Hướng dẫn, dẫn đường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_95f19728bc2ff7c9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_95f19728bc2ff7c9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💁</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "およぎます",
    "vi": "Bơi",
    "te": "およいで",
    "form1": "およいだり (khi thì bơi...)",
    "form2": "およぐことができる (có thể bơi)",
    "form3": "およぐ"
  },
  {
    "masu": "とります",
    "vi": "Chụp (ảnh)",
    "te": "とって",
    "form1": "とったり (khi thì chụp ảnh...)",
    "form2": "とることができる (có thể chụp)",
    "form3": "とる"
  },
  {
    "masu": "つくります",
    "vi": "Làm ra",
    "te": "つくって",
    "form1": "つくったり (làm cái này cái kia...)",
    "form2": "つくることができる (có thể tự làm)",
    "form3": "つくる"
  },
  {
    "masu": "たいけんします",
    "vi": "Trải nghiệm",
    "te": "たいけんして",
    "form1": "たいけんしたり",
    "form2": "たいけんすることができる",
    "form3": "たいけんする"
  },
  {
    "masu": "あんないします",
    "vi": "Hướng dẫn",
    "te": "あんないして",
    "form1": "あんないしたり",
    "form2": "あんないすることができる",
    "form3": "あんないする"
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
