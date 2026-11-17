/* Marugoto A2-2 Bài 1 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "自己紹介",
    "kana": "じこしょうかい",
    "kanji": "自己紹介",
    "romaji": "jikoshoukai",
    "vi": "Giới thiệu bản thân",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9519\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9519)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Giới thiệu b</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "秘密",
    "kana": "ひみつ",
    "kanji": "秘密",
    "romaji": "himitsu",
    "vi": "Bí mật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6169\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6169)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤫</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Bí mật</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "国際交流",
    "kana": "こくさいこうりゅう",
    "kanji": "国際交流",
    "romaji": "kokusaikouryuu",
    "vi": "Giao lưu quốc tế",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8616\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8616)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌐</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Giao lưu quố</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "電気店",
    "kana": "でんきてん",
    "kanji": "電気店",
    "romaji": "denkiten",
    "vi": "Cửa hàng điện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2525\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2525)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Cửa hàng điệ</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "電気製品",
    "kana": "でんきせいひん",
    "kanji": "電気製品",
    "romaji": "denkiseihin",
    "vi": "Sản phẩm điện tử",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4742\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4742)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📱</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Sản phẩm điệ</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "読書",
    "kana": "どくしょ",
    "kanji": "読書",
    "romaji": "dokusho",
    "vi": "Đọc sách",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7557\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7557)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📚</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Đọc sách</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "店をやります",
    "kana": "みせを やります",
    "kanji": "店をやります",
    "romaji": "mise o yarimasu",
    "vi": "Làm, mở nhà hàng / cửa tiệm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5579\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5579)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏪</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Làm, mở nhà </text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "翻訳をします",
    "kana": "ほんやくを します",
    "kanji": "翻訳をします",
    "romaji": "honyaku o shimasu",
    "vi": "Biên dịch (dịch viết)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_407\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_407)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📝</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Biên dịch (d</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "興味",
    "kana": "きょうみ",
    "kanji": "興味",
    "romaji": "kyoumi",
    "vi": "Hứng thú",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6078\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6078)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Hứng thú</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "村",
    "kana": "むら",
    "kanji": "村",
    "romaji": "mura",
    "vi": "Làng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_289\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_289)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏡</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Làng</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "島",
    "kana": "しま",
    "kanji": "島",
    "romaji": "shima",
    "vi": "Đảo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4684\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4684)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏝️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Đảo</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "年",
    "kana": "とし",
    "kanji": "年",
    "romaji": "toshi",
    "vi": "Tuổi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7673\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7673)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎂</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Tuổi</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "生まれます",
    "kana": "うまれます",
    "kanji": "生まれます",
    "romaji": "umaremasu",
    "vi": "Được sinh ra",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5563\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5563)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👶</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Được sinh ra</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "優しい",
    "kana": "やさしい",
    "kanji": "優しい",
    "romaji": "yasashii",
    "vi": "Hiền lành, tốt bụng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7505\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7505)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😊</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Hiền lành, t</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "健康（な）",
    "kana": "けんこう（な）",
    "kanji": "健康（な）",
    "romaji": "kenkou(na)",
    "vi": "Khỏe mạnh, lành mạnh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7096\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7096)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💪</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Khỏe mạnh, l</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "真面目（な）",
    "kana": "まじめ（な）",
    "kanji": "真面目（な）",
    "romaji": "majime(na)",
    "vi": "Nghiêm túc, chăm chỉ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3734\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3734)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Nghiêm túc, </text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "明るい",
    "kana": "あかるい",
    "kanji": "明るい",
    "romaji": "akarui",
    "vi": "Sáng sủa, tươi vui",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2363\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2363)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">☀️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Sáng sủa, tư</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "意味",
    "kana": "いみ",
    "kanji": "意味",
    "romaji": "imi",
    "vi": "Ý nghĩa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3211\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3211)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Ý nghĩa</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "作家",
    "kana": "さっか",
    "kanji": "作家",
    "romaji": "sakka",
    "vi": "Nhà văn, tác giả",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7504\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7504)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🖋️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Nhà văn, tác</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 1 (A2-2)",
    "jp": "住んでいるところ",
    "kana": "すんでいるところ",
    "kanji": "住んでいるところ",
    "romaji": "sunde iru tokoro",
    "vi": "Nơi đang sinh sống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6648\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6648)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏘️</text>\n  <text x=\"120\" y=\"105\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"12\" font-weight=\"800\" font-family=\"system-ui, -apple-system, sans-serif\">Nơi đang sin</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "やります",
    "vi": "Làm / mở (tiệm)",
    "te": "やって",
    "form1": "やっています",
    "form2": "やった",
    "form3": "やる"
  },
  {
    "masu": "ほんやくします",
    "vi": "Biên dịch",
    "te": "ほんやくして",
    "form1": "ほんやくしています",
    "form2": "ほんやくした",
    "form3": "ほんやくする"
  },
  {
    "masu": "うまれます",
    "vi": "Được sinh ra",
    "te": "うまれて",
    "form1": "うまれています",
    "form2": "うまれた",
    "form3": "うまれる"
  },
  {
    "masu": "そだちます",
    "vi": "Lớn lên",
    "te": "そだって",
    "form1": "そだっています",
    "form2": "そだった",
    "form3": "そだつ"
  },
  {
    "masu": "すみます",
    "vi": "Sinh sống",
    "te": "すんで",
    "form1": "すんでいます",
    "form2": "すんだ",
    "form3": "すむ"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "「ハノイ」というのは、「川の内側」[____] という意味です。",
    "options": [
      "と",
      "で",
      "に",
      "を"
    ],
    "correct": 0,
    "explain": "Mẫu câu giải thích định nghĩa, ý nghĩa: 『～というのは、...という意味です』. Chữ 「と」 làm trợ từ trích dẫn nội dung ý nghĩa."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "わたしは ベトナムの ダナン [____] うまれました。",
    "options": [
      "で",
      "に",
      "を",
      "へ"
    ],
    "correct": 0,
    "explain": "Nơi diễn ra hành động/sự kiện sinh ra 『生まれます』 dùng trợ từ 「で」 (ở tại đâu). Khác với nơi cư trú lâu dài 『住んでいます』 dùng 「に」."
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "日本の 歴史や 文学 [____] きょうみが あります。",
    "options": [
      "に",
      "で",
      "を",
      "が"
    ],
    "correct": 0,
    "explain": "Cấu trúc có hứng thú với điều gì: 『[Danh từ] に 興味 (きょうみ) が あります』. Trợ từ đi kèm đối tượng hứng thú là 「に」."
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "山田さんは いつも えがおで、とても [____] 人です。",
    "options": [
      "あかるい",
      "ひみつ",
      "むら",
      "とし"
    ],
    "correct": 0,
    "explain": "Người luôn tươi cười, vui vẻ, hoạt bát được miêu tả bằng tính từ 「明るい (あかるい)」 (tươi sáng, tươi vui)."
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "だれにも 言わないでください。これは 二人の [____] です。",
    "options": [
      "ひみつ",
      "どくしょ",
      "きょうみ",
      "いみ"
    ],
    "correct": 0,
    "explain": "Không được nói cho ai biết vì đây là 'bí mật' giữa hai người: 「秘密 (ひみつ)」."
  },
  {
    "id": 6,
    "category": "Ngữ pháp",
    "q": "わたしの 友だちは まじめ [____]、とても 親切です。",
    "options": [
      "で",
      "くて",
      "な",
      "に"
    ],
    "correct": 0,
    "explain": "Nối hai tính từ, trong đó 「真面目 (まじめ)」 là tính từ đuôi な, khi liên kết đổi thành 「まじめで」."
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "週末は 家で [____] を します。小説が 大好きです。",
    "options": [
      "どくしょ",
      "ほんやく",
      "じこしょうかい",
      "さっか"
    ],
    "correct": 0,
    "explain": "Thích đọc tiểu thuyết nên cuối tuần hay đọc sách: 「読書 (どくしょ) を します」."
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "「はじめまして。ナムです。どうぞ よろしく。」 ―― 「[____]」",
    "options": [
      "ナムさんですね。いい 名前ですね。",
      "どういたしまして。",
      "こちらこそ、お元気ですか。",
      "ごめんください。"
    ],
    "correct": 0,
    "explain": "Trong tình huống gặp gỡ lần đầu, khi đối phương giới thiệu tên, người Nhật thường khen tên thân thiện: 『...さんですね。いいお名前ですね』."
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "将来、自分ので 日本料理の [____] を やりたいです。",
    "options": [
      "みせ",
      "むら",
      "しま",
      "とし"
    ],
    "correct": 0,
    "explain": "Kinh doanh, mở quán ăn/nhà hàng dùng cụm từ 「店 (みせ) を やります」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「紹介」 có cách đọc chuẩn là gì?",
    "options": [
      "しょうかい",
      "じこかい",
      "そくかい",
      "しょうけい"
    ],
    "correct": 0,
    "explain": "紹介 đọc là 「しょうかい」 (THIỆU GIỚI - Giới thiệu)."
  },
  {
    "id": 11,
    "category": "Chữ Hán",
    "q": "Từ 「有名」 (HỮU DANH) có nghĩa là gì?",
    "options": [
      "Nổi tiếng",
      "Tên tuổi",
      "Ý nghĩa",
      "Hàng xóm"
    ],
    "correct": 0,
    "explain": "有名 (ゆうめい) nghĩa là nổi tiếng, có tiếng tăm."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Cách đọc của chữ Hán 「近所」 là gì?",
    "options": [
      "きんじょ",
      "ちかじょ",
      "きんしょ",
      "ちかところ"
    ],
    "correct": 0,
    "explain": "近所 đọc là 「きんじょ」 (CẬN SỞ - Hàng xóm, khu vực lân cận)."
  },
  {
    "id": 13,
    "category": "Ngữ pháp",
    "q": "父は 毎日 スポーツジムへ 行って、とても [____] です。",
    "options": [
      "けんこう",
      "さっか",
      "しま",
      "こくさい"
    ],
    "correct": 0,
    "explain": "Đi tập gym hàng ngày để rèn luyện nên cơ thể rất 'khỏe mạnh': 「健康 (けんこう) です」."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「屋」 trong từ 「本屋 (ほんや)」 có âm Hán Việt là gì?",
    "options": [
      "Ốc",
      "Phòng",
      "Điếm",
      "Thất"
    ],
    "correct": 0,
    "explain": "屋 có âm Hán Việt là ỐC (căn nhà, tiệm). 本屋 là Bổn Ốc (tiệm sách)."
  },
  {
    "id": 15,
    "category": "Từ vựng",
    "q": "村上春樹さんは 世界中で とても 読まれている [____] です。",
    "options": [
      "さっか",
      "いみ",
      "とし",
      "むら"
    ],
    "correct": 0,
    "explain": "Haruki Murakami là một nhà văn/tác giả nổi tiếng thế giới: 「作家 (さっか)」."
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
