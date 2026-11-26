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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4f767e50279fbe64\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4f767e50279fbe64)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dac5fcdff4fccd89\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dac5fcdff4fccd89)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤫</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_842fbf72974e88c7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_842fbf72974e88c7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌐</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_416f9bc3cb63a956\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_416f9bc3cb63a956)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_61ec65f4269a2cf1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_61ec65f4269a2cf1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📱</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4bc171bc6285c4d3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4bc171bc6285c4d3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📚</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0f8826a1eceb86a1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0f8826a1eceb86a1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏪</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_11511e477db245e9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_11511e477db245e9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📝</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e178a3931fe4c447\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e178a3931fe4c447)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e1b022b1b107e617\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e1b022b1b107e617)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏡</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f0af84d99e247121\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f0af84d99e247121)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏝️</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ce65d0e85be215a5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ce65d0e85be215a5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎂</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fad634267c1e113b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fad634267c1e113b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👶</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a959a9cf89b0d1e7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a959a9cf89b0d1e7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😊</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6ca118a732f26159\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6ca118a732f26159)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💪</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_19ddf9ce6702eac0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_19ddf9ce6702eac0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_72e14c670d1e600f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_72e14c670d1e600f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">☀️</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_84da895ef3b41986\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_84da895ef3b41986)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d2e796274019fb4e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d2e796274019fb4e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🖋️</text>\n</svg>"
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
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7d7ea658d9e5ecfc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7d7ea658d9e5ecfc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏘️</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "やります",
    "vi": "Làm / mở (tiệm)",
    "te": "やって",
    "form1": "やっています",
    "form2": "やった",
    "form3": "やる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "ほんやくします",
    "vi": "Biên dịch",
    "te": "ほんやくして",
    "form1": "ほんやくしています",
    "form2": "ほんやくした",
    "form3": "ほんやくする",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "うまれます",
    "vi": "Được sinh ra",
    "te": "うまれて",
    "form1": "うまれています",
    "form2": "うまれた",
    "form3": "うまれる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "そだちます",
    "vi": "Lớn lên",
    "te": "そだって",
    "form1": "そだっています",
    "form2": "そだった",
    "form3": "そだつ",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "すみます",
    "vi": "Sinh sống",
    "te": "すんで",
    "form1": "すんでいます",
    "form2": "すんだ",
    "form3": "すむ",
    "form2Label": "Thể quá khứ ngắn: Vた"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "「ハノイ」というのは、「川の内側」[____] いう意味です。",
    "options": [
      "で",
      "と",
      "に",
      "を"
    ],
    "correct": 1,
    "explain": "Mẫu câu giải thích định nghĩa, ý nghĩa: 『～というのは、...という意味です』. Chữ 「と」 làm trợ từ trích dẫn nội dung ý nghĩa.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "さいたま [____] ところに住んでいます。",
    "options": [
      "という",
      "ので",
      "しか",
      "まで"
    ],
    "correct": 0,
    "explain": "N1 というところ giới thiệu tên địa điểm: さいたまというところ.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "私は山田さんという [____] を知っています。",
    "options": [
      "意味",
      "ところ",
      "人",
      "ため"
    ],
    "correct": 2,
    "explain": "N1というN2 giới thiệu người/vật có tên là N1.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "山田さんは いつも えがおで、とても [____] 人です。",
    "options": [
      "ひみつ",
      "むら",
      "とし",
      "あかるい"
    ],
    "correct": 3,
    "explain": "Người luôn tươi cười, vui vẻ, hoạt bát được miêu tả bằng tính từ 「明るい (あかるい)」 (tươi sáng, tươi vui)."
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "だれにも 言わないでください。これは 二人の [____] です。",
    "options": [
      "どくしょ",
      "きょうみ",
      "ひみつ",
      "いみ"
    ],
    "correct": 2,
    "explain": "Không được nói cho ai biết vì đây là 'bí mật' giữa hai người: 「秘密 (ひみつ)」."
  },
  {
    "id": 6,
    "category": "Ngữ pháp",
    "q": "あそこに 山田さん [____] 人が います。新しい 先生ですよ。",
    "options": [
      "と",
      "という",
      "ので",
      "ような"
    ],
    "correct": 1,
    "explain": "Cấu trúc giới thiệu tên gọi của người/vật/địa danh mà người nghe chưa biết: 『N1 という N2』 (N2 có tên/gọi là N1) ➔ 「山田さんという人」 (người tên là Yamada).",
    "grammarScope": "official"
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "週末は 家で [____] を します。小説が 大好きです。",
    "options": [
      "ほんやく",
      "じこしょうかい",
      "さっか",
      "どくしょ"
    ],
    "correct": 3,
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
    "q": "将来、自分で 日本料理の [____] を やりたいです。",
    "options": [
      "むら",
      "しま",
      "みせ",
      "とし"
    ],
    "correct": 2,
    "explain": "Kinh doanh, mở quán ăn/nhà hàng dùng cụm từ 「店 (みせ) を やります」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「自己紹介」 có cách đọc nào?",
    "options": [
      "なまえ",
      "じこしょうかい",
      "いみ",
      "ほんや"
    ],
    "correct": 1,
    "explain": "自己紹介 đọc là 「じこしょうかい」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "自己紹介"
  },
  {
    "id": 11,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「名前」 có nghĩa là gì?",
    "options": [
      "Ý nghĩa",
      "Hiệu sách",
      "Tên",
      "Gần, gần đây"
    ],
    "correct": 2,
    "explain": "名前 nghĩa là Tên.",
    "scopeKanji": "名前"
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「意味」 có cách đọc nào?",
    "options": [
      "いみ",
      "ほんや",
      "ちかく",
      "すみます"
    ],
    "correct": 0,
    "explain": "意味 đọc là 「いみ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "意味"
  },
  {
    "id": 13,
    "category": "Ngữ pháp",
    "q": "これは 先週 日本で [____] 本です。とても おもしろいですよ。",
    "options": [
      "買った",
      "買いました",
      "買い",
      "買いて"
    ],
    "correct": 0,
    "explain": "Mệnh đề bổ nghĩa cho danh từ 『普通形 ＋ N』: Động từ đã hoàn thành trong quá khứ đưa về thể Quá khứ thông thường (thể た): 買いました ➔ 「買った本」 (cuốn sách đã mua).",
    "grammarScope": "official"
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「本屋」 có cách đọc nào?",
    "options": [
      "ちかく",
      "ほんや",
      "すみます",
      "はたらきます"
    ],
    "correct": 1,
    "explain": "本屋 đọc là 「ほんや」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "本屋"
  },
  {
    "id": 15,
    "category": "Từ vựng",
    "q": "村上春樹さんは 世界中で とても 読まれている [____] です。",
    "options": [
      "いみ",
      "とし",
      "むら",
      "さっか"
    ],
    "correct": 3,
    "explain": "Haruki Murakami là một nhà văn/tác giả nổi tiếng thế giới: 「作家 (さっか)」."
  },
  {
    "id": 16,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "「秋子」は「秋の子ども」[____] 意味です。",
    "options": [
      "という",
      "として",
      "について",
      "によって"
    ],
    "correct": 0,
    "explain": "N という意味です giải thích ý nghĩa: 「秋の子ども」という意味です. Nghĩa này ứng với tên viết là 秋子.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 17,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "Cụm nào có nghĩa là ‘một người bạn tên là Sakura’?",
    "options": [
      "さくらをいう友だち",
      "さくらという友だち",
      "さくらにいう友だち",
      "さくらでいう友だち"
    ],
    "correct": 1,
    "explain": "Tên gọi + という + danh từ chỉ loại người/vật: さくらという友だち.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 18,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "‘Đây là cuốn sách tôi đã đọc hôm qua.’ これは昨日私が [____] 本です。",
    "options": [
      "読みます",
      "読む",
      "読んだ",
      "読んで"
    ],
    "correct": 2,
    "explain": "Hành động đã xảy ra hôm qua dùng thể thường quá khứ 読んだ trước 本; không dùng thể ます để bổ nghĩa danh từ.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 19,
    "category": "Chữ Hán",
    "scopeKanji": "住みます",
    "q": "「住みます」の読み方はどれですか。",
    "options": [
      "はたらきます",
      "うまれます",
      "やすみます",
      "すみます"
    ],
    "correct": 3,
    "explain": "住みます đọc là すみます, nghĩa là sống/cư trú.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 20,
    "category": "Chữ Hán",
    "scopeKanji": "近く",
    "q": "「近く」の読み方はどれですか。",
    "options": [
      "とおく",
      "ちかい",
      "きんく",
      "ちかく"
    ],
    "correct": 3,
    "explain": "近く đọc là ちかく, nghĩa là ở gần.",
    "reviewVersion": "a22-practice20-v1"
  }
];

const SENTENCE_PRACTICE_DATA = [
  {
    "id": 1,
    "vi": "Tôi xin tự giới thiệu bản thân.",
    "jp": "私は自己紹介をします。",
    "requireKanji": true,
    "accepted": [
      "私は自己紹介します。"
    ]
  },
  {
    "id": 2,
    "vi": "Tên tôi là Linh.",
    "jp": "私の名前はリンです。",
    "requireKanji": true,
    "accepted": [
      "私はリンといいます。"
    ]
  },
  {
    "id": 3,
    "vi": "Tên tôi là Akiko, viết là 秋子, có nghĩa là ‘đứa trẻ mùa thu’.",
    "jp": "私の名前は秋子です。「秋の子ども」という意味です。",
    "requireKanji": true,
    "accepted": [
      "私の名前は秋子で、「秋の子ども」という意味です。",
      "私の名前は秋子です。秋子は秋の子供という意味です。"
    ]
  },
  {
    "id": 4,
    "vi": "Hiệu sách ở gần nhà tôi.",
    "jp": "本屋は私の家の近くにあります。",
    "requireKanji": true,
    "accepted": [
      "私の家の近くに本屋があります。"
    ]
  },
  {
    "id": 5,
    "vi": "Tôi sống trong một ngôi làng.",
    "jp": "私は村に住んでいます。",
    "requireKanji": true,
    "accepted": [
      "私は村で暮らしています。"
    ]
  },
  {
    "id": 6,
    "vi": "Chị tôi làm việc ở cửa hàng điện.",
    "jp": "姉は電気店で働いています。",
    "requireKanji": true,
    "accepted": [
      "姉は電気店に勤めています。"
    ]
  },
  {
    "id": 7,
    "vi": "Tôi quan tâm đến các sản phẩm điện tử.",
    "jp": "私は電気製品に興味があります。",
    "requireKanji": true,
    "accepted": [
      "私は電気製品に関心があります。"
    ]
  },
  {
    "id": 8,
    "vi": "Sở thích của tôi là đọc sách.",
    "jp": "私の趣味は読書です。",
    "requireKanji": true,
    "accepted": [
      "私は読書が趣味です。"
    ]
  },
  {
    "id": 9,
    "vi": "Bố tôi đang kinh doanh một cửa tiệm.",
    "jp": "父は店をやっています。",
    "requireKanji": true,
    "accepted": [
      "父は店を経営しています。"
    ]
  },
  {
    "id": 10,
    "vi": "Anh tôi làm công việc biên dịch.",
    "jp": "兄は翻訳をしています。",
    "requireKanji": true,
    "accepted": [
      "兄は翻訳の仕事をしています。"
    ]
  },
  {
    "id": 11,
    "vi": "Tôi sẽ giới thiệu người bạn đang làm việc ở hiệu sách.",
    "jp": "本屋で働いている友だちを紹介します。",
    "requireKanji": true,
    "accepted": [
      "本屋で働いている友達を紹介します。"
    ]
  },
  {
    "id": 12,
    "vi": "Địa chỉ của nhà văn này là một bí mật.",
    "jp": "この作家の住所は秘密です。",
    "requireKanji": true,
    "accepted": [
      "この作家の住所は内緒です。"
    ]
  },
  {
    "id": 13,
    "vi": "Tuổi của tôi là một bí mật.",
    "jp": "私の年は秘密です。",
    "requireKanji": true,
    "accepted": [
      "私の年齢は秘密です。"
    ]
  },
  {
    "id": 14,
    "vi": "Người bạn đang sống ở Hà Nội rất hiền lành.",
    "jp": "ハノイに住んでいる友だちはとても優しいです。",
    "requireKanji": true,
    "accepted": [
      "ハノイに住んでいる友達はとても優しいです。"
    ]
  },
  {
    "id": 15,
    "vi": "Người bạn không uống rượu có sức khỏe tốt.",
    "jp": "お酒を飲まない友だちは健康です。",
    "requireKanji": true,
    "accepted": [
      "お酒を飲まない友達は健康です。"
    ]
  },
  {
    "id": 16,
    "vi": "Người đang học trong thư viện rất nghiêm túc.",
    "jp": "図書館で勉強している人はとても真面目です。",
    "requireKanji": true,
    "accepted": [
      "図書館で勉強している人はとてもまじめです。"
    ]
  },
  {
    "id": 17,
    "vi": "Cô giáo của tôi có tính cách rất vui vẻ.",
    "jp": "私の先生はとても明るいです。",
    "requireKanji": true,
    "accepted": [
      "私の先生は性格がとても明るいです。"
    ]
  },
  {
    "id": 18,
    "vi": "Tên Sakura có nghĩa là hoa anh đào.",
    "jp": "「さくら」という名前は「桜の花」という意味です。",
    "requireKanji": true,
    "accepted": [
      "「さくら」という名前は「さくらの花」という意味です。"
    ]
  },
  {
    "id": 19,
    "vi": "Người viết cuốn sách này là một nhà văn Nhật Bản.",
    "jp": "この本を書いた人は日本の作家です。",
    "requireKanji": true,
    "accepted": [
      "これは日本の作家が書いた本です。"
    ]
  },
  {
    "id": 20,
    "vi": "Nơi tôi đang sinh sống ở gần hiệu sách.",
    "jp": "私が住んでいるところは本屋の近くです。",
    "requireKanji": true,
    "accepted": [
      "私が住んでいる場所は本屋の近くです。"
    ]
  },
  {
    "id": 21,
    "vi": "Tôi sinh ra ở Việt Nam.",
    "jp": "私はベトナムで生まれました。",
    "requireKanji": true,
    "accepted": [
      "私はベトナム生まれです。"
    ]
  },
  {
    "id": 22,
    "vi": "Tôi đang sống trên hòn đảo tên là Phú Quý.",
    "jp": "私は「フークイ」という島に住んでいます。",
    "requireKanji": true,
    "accepted": [
      "私はフークイという島で暮らしています。"
    ]
  },
  {
    "id": 23,
    "vi": "Đây là cuốn sách tôi đã đọc hôm qua.",
    "jp": "これは昨日読んだ本です。",
    "requireKanji": true,
    "accepted": [
      "これは昨日私が読んだ本です。"
    ]
  },
  {
    "id": 24,
    "vi": "Người đang làm việc ở cửa hàng là chị tôi.",
    "jp": "店で働いている人は姉です。",
    "requireKanji": true,
    "accepted": []
  },
  {
    "id": 25,
    "vi": "Đây là người bạn tên là Sakura.",
    "jp": "この人は「さくら」という友だちです。",
    "requireKanji": true,
    "accepted": [
      "この人はさくらという友達です。"
    ]
  },
  {
    "id": 26,
    "vi": "Thủy cung tôi đã đến hôm qua ở gần hiệu sách.",
    "jp": "昨日行った水族館は本屋の近くにあります。",
    "requireKanji": true,
    "accepted": [
      "昨日行った水族館は本屋の近くです。"
    ]
  },
  {
    "id": 27,
    "vi": "Tôi rất hứng thú với giao lưu quốc tế.",
    "jp": "私は国際交流にとても興味があります。",
    "requireKanji": true,
    "accepted": [
      "私は国際交流にとても関心があります。"
    ]
  },
  {
    "id": 28,
    "vi": "Người bạn sống ở đảo làm việc tại hiệu sách.",
    "jp": "島に住んでいる友だちは本屋で働いています。",
    "requireKanji": true,
    "accepted": [
      "島に住んでいる友達は本屋で働いています。"
    ]
  },
  {
    "id": 29,
    "vi": "Hiệu sách là cửa hàng đầu tiên tính từ ga.",
    "jp": "本屋は駅から一番目の店です。",
    "requireKanji": true,
    "accepted": [
      "本屋は駅から数えて一番目の店です。"
    ]
  },
  {
    "id": 30,
    "vi": "Đồ uống tôi rất thích hồi nhỏ là nước ép táo.",
    "jp": "子どものころ大好きだった飲み物はりんごジュースです。",
    "requireKanji": true,
    "accepted": [
      "子供のころ大好きだった飲み物はりんごジュースです。",
      "子供のころ大好きだった飲み物はリンゴジュースです。",
      "子どものころ大好きだった飲み物はリンゴジュースです。"
    ]
  },
  {
    "id": 31,
    "vi": "Người nghiêm túc đang viết một cuốn sách.",
    "jp": "真面目な人が本を書いています。",
    "requireKanji": true,
    "accepted": [
      "まじめな人が本を書いています。"
    ]
  },
  {
    "id": 32,
    "vi": "Người bạn từng là giáo viên hiện đang viết sách.",
    "jp": "先生だった友だちは今、本を書いています。",
    "requireKanji": true,
    "accepted": [
      "先生だった友達は今、本を書いています。",
      "教師だった友達は今、本を書いています。"
    ]
  },
  {
    "id": 33,
    "vi": "Người đang kinh doanh cửa tiệm trong làng là bố tôi.",
    "jp": "村で店をやっている人は父です。",
    "requireKanji": true,
    "accepted": [
      "村で店を経営している人は父です。"
    ]
  },
  {
    "id": 34,
    "vi": "Cuốn sách chị tôi đã dịch rất thú vị.",
    "jp": "姉が翻訳した本はとてもおもしろいです。",
    "requireKanji": true,
    "accepted": [
      "姉が訳した本はとてもおもしろいです。",
      "姉が翻訳した本はとても面白いです。"
    ]
  },
  {
    "id": 35,
    "vi": "Tôi đã gặp nhà văn đang sống trên đảo.",
    "jp": "島に住んでいる作家に会いました。",
    "requireKanji": true,
    "accepted": [
      "島に住んでいる作家と会いました。"
    ]
  },
  {
    "id": 36,
    "vi": "Tên của người bạn đang làm ở hiệu sách là Mai.",
    "jp": "本屋で働いている友だちの名前はマイです。",
    "requireKanji": true,
    "accepted": [
      "本屋で働いている友達の名前はマイです。"
    ]
  },
  {
    "id": 37,
    "vi": "Tôi thích sản phẩm điện tử mà công ty này sản xuất.",
    "jp": "私はこの会社が作っている電気製品が好きです。",
    "requireKanji": true,
    "accepted": []
  },
  {
    "id": 38,
    "vi": "Người bạn sinh ra trong làng tôi hiện sống trong khu tôi ở.",
    "jp": "私の村で生まれた友だちは今、近所に住んでいます。",
    "requireKanji": true,
    "accepted": [
      "私の村で生まれた友達は今、近所に住んでいます。"
    ]
  },
  {
    "id": 39,
    "vi": "Tôi thường đọc sách ở quán cà phê tên là Sakura.",
    "jp": "私はよく「さくら」というカフェで読書をします。",
    "requireKanji": true,
    "accepted": [
      "私はさくらという喫茶店でよく読書をします。"
    ]
  },
  {
    "id": 40,
    "vi": "Tôi muốn sống trong ngôi làng gần biển.",
    "jp": "私は海に近い村に住みたいです。",
    "requireKanji": true,
    "accepted": [
      "私は海の近くの村に住みたいです。"
    ]
  }
];

const KANJI_PRACTICE_DATA = [
  {
    "id": "official-1-1",
    "word": "自己紹介",
    "kana": "じこしょうかい",
    "mean": "Giới thiệu bản thân",
    "accepted": []
  },
  {
    "id": "official-1-2",
    "word": "名前",
    "kana": "なまえ",
    "mean": "Tên",
    "accepted": []
  },
  {
    "id": "official-1-3",
    "word": "意味",
    "kana": "いみ",
    "mean": "Ý nghĩa",
    "accepted": []
  },
  {
    "id": "official-1-4",
    "word": "本屋",
    "kana": "ほんや",
    "mean": "Hiệu sách",
    "accepted": []
  },
  {
    "id": "official-1-5",
    "word": "近く",
    "kana": "ちかく",
    "mean": "Gần, gần đây",
    "accepted": []
  },
  {
    "id": "official-1-6",
    "word": "住みます",
    "kana": "すみます",
    "mean": "Sống, cư trú",
    "accepted": []
  },
  {
    "id": "official-1-7",
    "word": "働きます",
    "kana": "はたらきます",
    "mean": "Làm việc",
    "accepted": []
  },
  {
    "id": "official-1-8",
    "word": "～番目（１番目）",
    "kana": "～ばんめ（いちばんめ）",
    "mean": "Thứ ～ (thứ nhất)",
    "accepted": [
      "一番目",
      "1番目"
    ]
  },
  {
    "id": "supplement-1-1",
    "word": "一番",
    "kana": "いちばん",
    "mean": "Nhất, số một",
    "accepted": []
  },
  {
    "id": "supplement-1-2",
    "word": "一番目",
    "kana": "いちばんめ",
    "mean": "Thứ nhất",
    "accepted": []
  },
  {
    "id": "supplement-1-3",
    "word": "住所",
    "kana": "じゅうしょ",
    "mean": "Địa chỉ",
    "accepted": []
  },
  {
    "id": "supplement-1-4",
    "word": "最近",
    "kana": "さいきん",
    "mean": "Gần đây",
    "accepted": []
  },
  {
    "id": "supplement-1-5",
    "word": "紹介",
    "kana": "しょうかい",
    "mean": "Giới thiệu",
    "accepted": []
  },
  {
    "id": "supplement-1-6",
    "word": "近い",
    "kana": "ちかい",
    "mean": "Gần",
    "accepted": []
  },
  {
    "id": "supplement-1-7",
    "word": "近所",
    "kana": "きんじょ",
    "mean": "Hàng xóm, lân cận",
    "accepted": []
  },
  {
    "id": "supplement-1-8",
    "word": "部屋",
    "kana": "へや",
    "mean": "Căn phòng",
    "accepted": []
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
if (typeof SENTENCE_PRACTICE_DATA !== "undefined") window.SENTENCE_PRACTICE_DATA = SENTENCE_PRACTICE_DATA;
if (typeof KANJI_PRACTICE_DATA !== "undefined") window.KANJI_PRACTICE_DATA = KANJI_PRACTICE_DATA;
