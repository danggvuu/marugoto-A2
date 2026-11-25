/* Marugoto A2-2 Bài 5 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "観光シーズン",
    "kana": "かんこうシーズン",
    "kanji": "観光シーズン",
    "romaji": "kankou shi-zun",
    "vi": "Mùa du lịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_08e2bf64b8c7786d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_08e2bf64b8c7786d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✈️</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "台風シーズン",
    "kana": "たいふうシーズン",
    "kanji": "台風シーズン",
    "romaji": "taifuu shi-zun",
    "vi": "Mùa bão",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6c7f86bdacc1e750\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6c7f86bdacc1e750)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌀</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "自然",
    "kana": "しぜん",
    "kanji": "自然",
    "romaji": "shizen",
    "vi": "Thiên nhiên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7e1752e08949fb2c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7e1752e08949fb2c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌿</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "島",
    "kana": "しま",
    "kanji": "島",
    "romaji": "shima",
    "vi": "Đảo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f0af84d99e247121\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f0af84d99e247121)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏝️</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "グルメ",
    "kana": "グルメ",
    "kanji": "グルメ",
    "romaji": "gurume",
    "vi": "Ăn uống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e2fb5615982c1d21\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e2fb5615982c1d21)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍽️</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ダイビングの道具",
    "kana": "ダイビングのどうぐ",
    "kanji": "ダイビングの道具",
    "romaji": "daibingu no dougu",
    "vi": "Đồ lặn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0c5f64d0621a0f56\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0c5f64d0621a0f56)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤿</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "サングラス",
    "kana": "サングラス",
    "kanji": "サングラス",
    "romaji": "sangurasu",
    "vi": "Kính râm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_806edc60e8fd7bdd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_806edc60e8fd7bdd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕶️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "コート",
    "kana": "コート",
    "kanji": "コート",
    "romaji": "ko-to",
    "vi": "Áo choàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f8e2a9dfbe139bcf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f8e2a9dfbe139bcf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧥</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ジャケット",
    "kana": "ジャケット",
    "kanji": "ジャケット",
    "romaji": "jaketto",
    "vi": "Áo khoác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_68ee4fba2c004e80\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_68ee4fba2c004e80)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧥</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "料金",
    "kana": "りょうきん",
    "kanji": "料金",
    "romaji": "ryoukin",
    "vi": "Chi phí",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_aae52a04f6c327a3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_aae52a04f6c327a3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💰</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "豊か（な）",
    "kana": "ゆたか（な）",
    "kanji": "豊か（な）",
    "romaji": "yutaka(na)",
    "vi": "Phong phú",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_207f92769a0a1bdd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_207f92769a0a1bdd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌾</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "美しい",
    "kana": "うつくしい",
    "kanji": "美しい",
    "romaji": "utsukushii",
    "vi": "Đẹp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_85477490449ed90f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_85477490449ed90f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ドライブします",
    "kana": "ドライブします",
    "kanji": "ドライブします",
    "romaji": "doraibu shimasu",
    "vi": "Lái xe",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d2e73060a34ef5b4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d2e73060a34ef5b4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚗</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "レンタルします",
    "kana": "レンタルします",
    "kanji": "レンタルします",
    "romaji": "rentaru shimasu",
    "vi": "Thuê",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_812f5bbd74565939\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_812f5bbd74565939)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔑</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "予約します",
    "kana": "よやくします",
    "kanji": "予約します",
    "romaji": "yoyaku shimasu",
    "vi": "Hẹn, đặt trước",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_331051746d4d240a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_331051746d4d240a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "込みます",
    "kana": "こみます",
    "kanji": "込みます",
    "romaji": "komimasu",
    "vi": "Đông",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_67f006f019a90c7f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_67f006f019a90c7f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "揺れます",
    "kana": "ゆれます",
    "kanji": "揺れます",
    "romaji": "yuremasu",
    "vi": "Rung, lắc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ff6adfbdd2300854\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ff6adfbdd2300854)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌊</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ほっとします",
    "kana": "ほっとします",
    "kanji": "ほっとします",
    "romaji": "hotto shimasu",
    "vi": "An tâm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_202296626ae2017c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_202296626ae2017c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍵</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "おすすめのコース",
    "kana": "おすすめのコース",
    "kanji": "おすすめのコース",
    "romaji": "osusume no ko-su",
    "vi": "Khóa được khuyến khích",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9169c8e3892ea8b2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9169c8e3892ea8b2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗺️</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "持っていきます",
    "kana": "もっていきます",
    "kanji": "持っていきます",
    "romaji": "motte ikimasu",
    "vi": "Mang đi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_49c20a62d5206272\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_49c20a62d5206272)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎒</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "自然",
    "kana": "しぜん",
    "kanji": "自然",
    "romaji": "shizen",
    "vi": "Thiên nhiên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7e1752e08949fb2c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7e1752e08949fb2c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌿</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "景色",
    "kana": "けしき",
    "kanji": "景色",
    "romaji": "keshiki",
    "vi": "Phong cảnh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_89b505d64145b32f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_89b505d64145b32f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌄</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "豊か（な）",
    "kana": "ゆたか（な）",
    "kanji": "豊か（な）",
    "romaji": "yutaka(na)",
    "vi": "Phong phú, đa dạng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bd7a6e7a8224e1c3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bd7a6e7a8224e1c3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌾</text>\n</svg>"
  },
  {
    "id": 24,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "島",
    "kana": "しま",
    "kanji": "島",
    "romaji": "shima",
    "vi": "Đảo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f0af84d99e247121\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f0af84d99e247121)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏝️</text>\n</svg>"
  },
  {
    "id": 25,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "島をドライブします",
    "kana": "しまをドライブします",
    "kanji": "島をドライブします",
    "romaji": "shima o doraibu shimasu",
    "vi": "Lái xe dạo quanh đảo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8a451c1a53077fd6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8a451c1a53077fd6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚗</text>\n</svg>"
  },
  {
    "id": 26,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "美しい",
    "kana": "うつくしい",
    "kanji": "美しい",
    "romaji": "utsukushii",
    "vi": "Tuyệt đẹp, hùng vĩ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b0e51b4ecc77f26c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b0e51b4ecc77f26c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  },
  {
    "id": 27,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "おすすめ",
    "kana": "おすすめ",
    "kanji": "おすすめ",
    "romaji": "osusume",
    "vi": "Đề xuất",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3a11f9115d12039e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3a11f9115d12039e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👍</text>\n</svg>"
  },
  {
    "id": 28,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "予約します",
    "kana": "よやくします",
    "kanji": "予約します",
    "romaji": "yoyaku shimasu",
    "vi": "Đặt trước, book (Ｎを予約します)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d990c85ae28d5d8f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d990c85ae28d5d8f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  },
  {
    "id": 29,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ダイビング（します）",
    "kana": "ダイビング（します）",
    "kanji": "ダイビング（します）",
    "romaji": "daibingu(shimasu)",
    "vi": "Lặn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f77eec8d2e600b39\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f77eec8d2e600b39)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤿</text>\n</svg>"
  },
  {
    "id": 30,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "道具",
    "kana": "どうぐ",
    "kanji": "道具",
    "romaji": "dougu",
    "vi": "Dụng cụ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_913b1a44d896bd95\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_913b1a44d896bd95)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧰</text>\n</svg>"
  },
  {
    "id": 31,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "料金",
    "kana": "りょうきん",
    "kanji": "料金",
    "romaji": "ryoukin",
    "vi": "Phí, tiền phải trả…",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_79a8a1ffb1acd47a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_79a8a1ffb1acd47a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💰</text>\n</svg>"
  },
  {
    "id": 32,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "レンタル（します）",
    "kana": "レンタル（します）",
    "kanji": "レンタル（します）",
    "romaji": "rentaru(shimasu)",
    "vi": "Thuê",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_812f5bbd74565939\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_812f5bbd74565939)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔑</text>\n</svg>"
  },
  {
    "id": 33,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "込みます",
    "kana": "こみます",
    "kanji": "込みます",
    "romaji": "komimasu",
    "vi": "Đông (混んでいます)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0f2619042f3a496f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0f2619042f3a496f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n</svg>"
  },
  {
    "id": 34,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "空きます",
    "kana": "すきます",
    "kanji": "空きます",
    "romaji": "sukimasu",
    "vi": "Vắng (空いています)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_40414b9236305eb2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_40414b9236305eb2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍃</text>\n</svg>"
  },
  {
    "id": 35,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "サングラス（をかけます）",
    "kana": "サングラス（をかけます）",
    "kanji": "サングラス（をかけます）",
    "romaji": "sangurasu(o kakemasu)",
    "vi": "Kính râm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_806edc60e8fd7bdd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_806edc60e8fd7bdd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕶️</text>\n</svg>"
  },
  {
    "id": 36,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "素晴らしい",
    "kana": "すばらしい",
    "kanji": "素晴らしい",
    "romaji": "subarashii",
    "vi": "Tuyệt vời, rất tốt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_32d37116154bf13c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_32d37116154bf13c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌟</text>\n</svg>"
  },
  {
    "id": 37,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "揺れます",
    "kana": "ゆれます",
    "kanji": "揺れます",
    "romaji": "yuremasu",
    "vi": "Rung, lắc (nhà/thuyền)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_92ecf020644aaf3d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_92ecf020644aaf3d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌊</text>\n</svg>"
  },
  {
    "id": 38,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "観光シーズン",
    "kana": "かんこうシーズン",
    "kanji": "観光シーズン",
    "romaji": "kankou shi-zun",
    "vi": "Mùa du lịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_08e2bf64b8c7786d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_08e2bf64b8c7786d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✈️</text>\n</svg>"
  },
  {
    "id": 39,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "親切（な）",
    "kana": "しんせつ（な）",
    "kanji": "親切（な）",
    "romaji": "shinsetsu(na)",
    "vi": "Tốt bụng, thân thiện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c429a687c8177da3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c429a687c8177da3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n</svg>"
  },
  {
    "id": 40,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "アドバイス",
    "kana": "アドバイス",
    "kanji": "アドバイス",
    "romaji": "adobaisu",
    "vi": "Lời khuyên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3e546730d8923588\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3e546730d8923588)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
  },
  {
    "id": 41,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ほっとします",
    "kana": "ほっとします",
    "kanji": "ほっとします",
    "romaji": "hotto shimasu",
    "vi": "Nhẹ nhõm, thở phào",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f640c5a1c82bea96\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f640c5a1c82bea96)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍵</text>\n</svg>"
  },
  {
    "id": 42,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "できれば、～",
    "kana": "できれば、～",
    "kanji": "できれば、～",
    "romaji": "dekireba, ~",
    "vi": "Nếu có thể thì...",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0e6c3c3cf28ec154\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0e6c3c3cf28ec154)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙏</text>\n</svg>"
  },
  {
    "id": 43,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "海岸",
    "kana": "かいがん",
    "kanji": "海岸",
    "romaji": "kaigan",
    "vi": "Bờ biển",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_469642fd896302fc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_469642fd896302fc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏖️</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "もっていきます",
    "vi": "Mang theo đi",
    "te": "もっていって",
    "form1": "もっていったほうがいい (nên mang theo)",
    "form2": "もっていかないほうがいい (không nên mang)",
    "form3": "もっていく",
    "form2Label": "Khuyên không nên: Vないほうがいい"
  },
  {
    "masu": "よやくします",
    "vi": "Đặt trước",
    "te": "よやくして",
    "form1": "よやくしたほうがいい (nên đặt trước)",
    "form2": "よやくしないほうがいい",
    "form3": "よやくする",
    "form2Label": "Khuyên không nên: Vないほうがいい"
  },
  {
    "masu": "しらべます",
    "vi": "Tra cứu, tìm hiểu",
    "te": "しらべて",
    "form1": "しらべたほうがいい (nên tra trước)",
    "form2": "しらべないほうがいい",
    "form3": "しらべる",
    "form2Label": "Khuyên không nên: Vないほうがいい"
  },
  {
    "masu": "とまります",
    "vi": "Trọ lại khách sạn",
    "te": "とまって",
    "form1": "とまったほうがいい (nên trọ ở)",
    "form2": "とまらないほうがいい",
    "form3": "とまる",
    "form2Label": "Khuyên không nên: Vないほうがいい"
  },
  {
    "masu": "わすれます",
    "vi": "Quên",
    "te": "わすれて",
    "form1": "わすれないほうがいい (không nên quên)",
    "form2": "わすれた (đã quên)",
    "form3": "わすれる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "沖縄の 夏は 日差しが 強いですから、ぼうしを [____] ほうがいいですよ。",
    "options": [
      "持っていく",
      "持っていかない",
      "持っていって",
      "持っていった"
    ],
    "correct": 3,
    "explain": "Đưa ra lời khuyên nên làm gì: V-たほうがいい ➔ 「持っていったほうがいい」.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "人気のある ホテルですから、早く [____] ほうがいいです。",
    "options": [
      "予約した",
      "予約して",
      "予約する",
      "予約しない"
    ],
    "correct": 0,
    "explain": "Nên đặt phòng sớm: 予約しました ➔ thể TA: 「予約した」 ＋ ほうがいい.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "飛行機に 乗るために、時間に 余裕を もって [____] へ 行きます。",
    "options": [
      "みなと",
      "くうこう",
      "りょかん",
      "おてら"
    ],
    "correct": 1,
    "explain": "Đi máy bay phải đến sân bay: 「空港 (くうこう)」."
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "沖縄に [____] とき、船で行きました。",
    "options": [
      "行った",
      "行く",
      "行って",
      "行かない"
    ],
    "correct": 1,
    "explain": "Vるとき nêu thời điểm đi Okinawa.",
    "grammarScope": "official"
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "海で 泳ぐときに 着る 服を [____] と 言います。",
    "options": [
      "ゆかた",
      "ぼうし",
      "にもつ",
      "みずぎ"
    ],
    "correct": 3,
    "explain": "Đồ bơi tiếng Nhật là 「水着 (みずぎ)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「木」 có cách đọc nào?",
    "options": [
      "き",
      "もり",
      "しま",
      "しぜん"
    ],
    "correct": 0,
    "explain": "木 đọc là 「き」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "木"
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "日焼けを 防ぐために 肌に 塗る クリームは [____] です。",
    "options": [
      "くすり",
      "ぼうし",
      "ひやけどめ",
      "ガイドブック"
    ],
    "correct": 2,
    "explain": "Kem chống nắng là 「日焼け止め (ひやけどめ)」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「森」 có cách đọc nào?",
    "options": [
      "しま",
      "しぜん",
      "もり",
      "ふね"
    ],
    "correct": 2,
    "explain": "森 đọc là 「もり」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "森"
  },
  {
    "id": 9,
    "category": "Ngữ pháp",
    "q": "あしたは 朝 早く 出発しますから、今夜は 夜更かしを [____] ほうがいいです。",
    "options": [
      "した",
      "して",
      "しない",
      "する"
    ],
    "correct": 2,
    "explain": "Khuyên không nên làm gì: V-ないほうがいい ➔ 「しないほうがいい」.",
    "grammarScope": "official"
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「島」 có cách đọc nào?",
    "options": [
      "しぜん",
      "しま",
      "ふね",
      "あつい"
    ],
    "correct": 1,
    "explain": "島 đọc là 「しま」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "島"
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "観光地や おいしい レストランの 情報が のっている 本は [____] です。",
    "options": [
      "ガイドブック",
      "メニュー",
      "手紙",
      "辞書"
    ],
    "correct": 0,
    "explain": "Sách cẩm nang chỉ dẫn du lịch: 「ガイドブック (guidebook)」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「自然」 có cách đọc nào?",
    "options": [
      "ふね",
      "あつい",
      "かえります",
      "しぜん"
    ],
    "correct": 3,
    "explain": "自然 đọc là 「しぜん」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "自然"
  },
  {
    "id": 13,
    "category": "Hội thoại",
    "q": "「沖縄旅行、楽しんできてね！」 ―― 「[____]」",
    "options": [
      "どういたしまして。",
      "ありがとう、行ってきます！",
      "こちらこそ、すみません。",
      "ただいま。"
    ],
    "correct": 1,
    "explain": "Khi được bạn chúc chuyến đi vui vẻ, ta đáp: 「ありがとう、行ってきます！」 (Cảm ơn, tớ lên đường đây!)."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「船」 có cách đọc nào?",
    "options": [
      "ふね",
      "あつい",
      "かえります",
      "よやくします"
    ],
    "correct": 0,
    "explain": "船 đọc là 「ふね」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "船"
  },
  {
    "id": 15,
    "category": "Từ vựng",
    "q": "旅行の 前の 日に、スーツケースに 必要な ものを 入れて [____] を します。",
    "options": [
      "かんこう",
      "よやく",
      "じゅんび",
      "りょこう"
    ],
    "correct": 2,
    "explain": "Soạn hành lý trước chuyến đi là công tác chuẩn bị: 「準備 (じゅんび) を します」."
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
