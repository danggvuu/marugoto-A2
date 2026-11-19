/* Marugoto A2-2 Bài 3 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "おすすめ",
    "kana": "おすすめ",
    "kanji": "おすすめ",
    "romaji": "osusume",
    "vi": "Món gợi ý, khuyến cử",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_85622667d40a9497\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_85622667d40a9497)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👍</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "味",
    "kana": "あじ",
    "kanji": "味",
    "romaji": "aji",
    "vi": "Mùi vị, hương vị",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dacee5166379b8ee\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dacee5166379b8ee)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👅</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "甘い",
    "kana": "あまい",
    "kanji": "甘い",
    "romaji": "amai",
    "vi": "Ngọt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_810486b7310a0311\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_810486b7310a0311)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍰</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "辛い",
    "kana": "からい",
    "kanji": "辛い",
    "romaji": "karai",
    "vi": "Cay",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_21dd471f683fa1bc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_21dd471f683fa1bc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌶️</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "苦い",
    "kana": "にがい",
    "kanji": "苦い",
    "romaji": "nigai",
    "vi": "Đắng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b8af154e42998657\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b8af154e42998657)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">☕</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "酸っぱい",
    "kana": "すっぱい",
    "kanji": "酸っぱい",
    "romaji": "suppai",
    "vi": "Chua",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1fc0f6a1315e3d6a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1fc0f6a1315e3d6a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍋</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "しょっぱい",
    "kana": "しょっぱい",
    "kanji": "しょっぱい",
    "romaji": "shoppai",
    "vi": "Mặn (vị muối)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_475438493adff985\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_475438493adff985)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧂</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "さっぱりした",
    "kana": "さっぱりした",
    "kanji": "さっぱりした",
    "romaji": "sappari shita",
    "vi": "Thanh đạm, mát lành, không ngấy",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_541134b9dd412484\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_541134b9dd412484)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥗</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "居酒屋",
    "kana": "いざかや",
    "kanji": "居酒屋",
    "romaji": "izakaya",
    "vi": "Quán nhậu kiểu Nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b5a2e750adb98b9e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b5a2e750adb98b9e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏮</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "定食",
    "kana": "ていしょく",
    "kanji": "定食",
    "romaji": "teishoku",
    "vi": "Cơm phần, suất ăn trọn gói",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f8db67ec238cf5a5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f8db67ec238cf5a5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍱</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "注文",
    "kana": "ちゅうもん",
    "kanji": "注文",
    "romaji": "chuumon",
    "vi": "Sự gọi món, đặt hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_85c1d20b7555241c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_85c1d20b7555241c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📋</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "刺身",
    "kana": "さしみ",
    "kanji": "刺身",
    "romaji": "sashimi",
    "vi": "Gỏi cá sống sashimi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6b1d4b5dd31af0a4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6b1d4b5dd31af0a4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐟</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "乾杯",
    "kana": "かんぱい",
    "kanji": "乾杯",
    "romaji": "kanpai",
    "vi": "Cạn ly! Nâng ly chúc mừng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2e8f47c4b960fc31\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2e8f47c4b960fc31)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍻</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "デザート",
    "kana": "デザート",
    "kanji": "デザート",
    "romaji": "dezaato",
    "vi": "Món tráng miệng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8be1b8410e7ce6ac\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8be1b8410e7ce6ac)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍨</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "メニュー",
    "kana": "メニュー",
    "kanji": "メニュー",
    "romaji": "menyuu",
    "vi": "Thực đơn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_01c50d77c03cb530\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_01c50d77c03cb530)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "店員",
    "kana": "てんいん",
    "kanji": "店員",
    "romaji": "ten'in",
    "vi": "Nhân viên quán, phục vụ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fc55f9a33efc8315\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fc55f9a33efc8315)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧑‍🍳</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "席",
    "kana": "せき",
    "kanji": "席",
    "romaji": "seki",
    "vi": "Chỗ ngồi, bàn ăn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b5e71d83b99ee09c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b5e71d83b99ee09c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪑</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "会計",
    "kana": "かいけい",
    "kanji": "会計",
    "romaji": "kaikei",
    "vi": "Tính tiền, thanh toán",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1a7000afbc4a4acf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1a7000afbc4a4acf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💳</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "人気",
    "kana": "にんき",
    "kanji": "人気",
    "romaji": "ninki",
    "vi": "Được yêu thích, phổ biến",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e265066c35e69217\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e265066c35e69217)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⭐</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "料理",
    "kana": "りょうり",
    "kanji": "料理",
    "romaji": "ryouri",
    "vi": "Món ăn, nấu nướng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f63027c26ea06866\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f63027c26ea06866)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍲</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "たべます",
    "vi": "Ăn",
    "te": "たべて",
    "form1": "たべてみます (ăn thử)",
    "form2": "たべたことがある (đã từng ăn)",
    "form3": "たべる (thể từ điển)"
  },
  {
    "masu": "のみます",
    "vi": "Uống",
    "te": "のんで",
    "form1": "のんでみます (uống thử)",
    "form2": "のんだことがある (đã từng uống)",
    "form3": "のむ"
  },
  {
    "masu": "ちゅうもんします",
    "vi": "Gọi món",
    "te": "ちゅうもんして",
    "form1": "ちゅうもんしてみます (thử gọi món)",
    "form2": "ちゅうもんしたことがある",
    "form3": "ちゅうもんする"
  },
  {
    "masu": "えらびます",
    "vi": "Chọn lựa",
    "te": "えらんで",
    "form1": "えらんでみます (thử chọn)",
    "form2": "えらんだことがある",
    "form3": "えらぶ"
  },
  {
    "masu": "たのみます",
    "vi": "Nhờ / gọi món",
    "te": "たのんで",
    "form1": "たのんでみます (thử gọi)",
    "form2": "たのんだことがある",
    "form3": "たのむ"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "この店はおいしい [____]、よく来ます。",
    "options": [
      "のは",
      "なら",
      "ずつ",
      "ので"
    ],
    "correct": 3,
    "explain": "ので nối lý do với kết quả: ngon nên thường đến.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "私が好きな [____]、ステーキです。",
    "options": [
      "ので",
      "なら",
      "のは",
      "ずつ"
    ],
    "correct": 2,
    "explain": "のは danh từ hóa mệnh đề làm chủ đề câu.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "レモンは とても [____] ですが、体によいです。",
    "options": [
      "あまい",
      "すっぱい",
      "からい",
      "にがい"
    ],
    "correct": 1,
    "explain": "Chanh (レモン) có vị chua, tiếng Nhật là 「酸っぱい (すっぱい)」."
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "野菜 [____]、このサラダがいいですよ。",
    "options": [
      "なら",
      "ので",
      "のは",
      "ずつ"
    ],
    "correct": 0,
    "explain": "なら nêu gợi ý theo chủ đề được nhắc tới.",
    "grammarScope": "official"
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "ビールや ジュースを 持って、みんなで 「[____]！」 と 言って グラスを 合わせます。",
    "options": [
      "ごちそうさま",
      "かんぱい",
      "いただきます",
      "いらっしゃいませ"
    ],
    "correct": 1,
    "explain": "Trước khi bắt đầu uống trong tiệc, mọi người cùng hô cạn ly: 「乾杯 (かんぱい)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「客」 có cách đọc nào?",
    "options": [
      "きゃく",
      "ちゅうもん",
      "ようしょく",
      "わしょく"
    ],
    "correct": 0,
    "explain": "客 đọc là 「きゃく」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "客"
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "この スープは 塩が 多すぎて、とても [____] です。",
    "options": [
      "あまい",
      "しょっぱい",
      "にがい",
      "すっぱい"
    ],
    "correct": 1,
    "explain": "Nhiều muối (塩) quá thì vị mặn chát: 「しょっぱい」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「注文」 có cách đọc nào?",
    "options": [
      "ようしょく",
      "わしょく",
      "ぎゅうにく",
      "ちゅうもん"
    ],
    "correct": 3,
    "explain": "注文 đọc là 「ちゅうもん」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "注文"
  },
  {
    "id": 9,
    "category": "Ngữ pháp",
    "q": "コーヒーを二つ [____] お願いします。",
    "options": [
      "ので",
      "なら",
      "のは",
      "ずつ"
    ],
    "correct": 3,
    "explain": "ずつ diễn tả phân chia theo từng đơn vị.",
    "grammarScope": "official"
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「洋食」 có cách đọc nào?",
    "options": [
      "ようしょく",
      "わしょく",
      "ぎゅうにく",
      "ちほう"
    ],
    "correct": 0,
    "explain": "洋食 đọc là 「ようしょく」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "洋食"
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "ごはん、みそ汁、魚、小鉢が セットに なっている 料理を [____] と 言います。",
    "options": [
      "デザート",
      "ちゅうもん",
      "ていしょく",
      "かいけい"
    ],
    "correct": 2,
    "explain": "Bữa ăn kèm đầy đủ cơm, canh miso, thức ăn thành phần trọn gói gọi là 「定食 (ていしょく)」."
  },
  {
    "id": 12,
    "category": "Từ vựng",
    "q": "食事が 終わったあとで、甘い アイスクリームなどの [____] を 食べます。",
    "options": [
      "さしみ",
      "メニュー",
      "デザート",
      "いざかや"
    ],
    "correct": 2,
    "explain": "Món ngọt tráng miệng sau bữa ăn gọi là 「デザート (dessert)」."
  },
  {
    "id": 13,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「和食」 có nghĩa là gì?",
    "options": [
      "Thịt bò",
      "Món ăn Nhật",
      "Vùng, miền",
      "Nổi tiếng"
    ],
    "correct": 1,
    "explain": "和食 nghĩa là Món ăn Nhật.",
    "scopeKanji": "和食"
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "食事代を 支払うときに、店員に 「お[____]、お願いします」 と 言います。",
    "options": [
      "かいけい",
      "ちゅうもん",
      "せき",
      "にんき"
    ],
    "correct": 0,
    "explain": "Khi muốn thanh toán tính tiền ở quán Nhật: 「お会計（かいけい）、お願いします」."
  },
  {
    "id": 15,
    "category": "Ngữ pháp",
    "q": "一つ [____] お願いします。",
    "options": [
      "ので",
      "なら",
      "ずつ",
      "のは"
    ],
    "correct": 2,
    "explain": "ずつ diễn tả phân chia theo từng đơn vị.",
    "grammarScope": "official"
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
