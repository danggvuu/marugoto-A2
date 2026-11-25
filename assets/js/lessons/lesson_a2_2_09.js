/* Marugoto A2-2 Bài 9 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "お正月",
    "kana": "おしょうがつ",
    "kanji": "お正月",
    "romaji": "oshougatsu",
    "vi": "Tết Nguyên Đán",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3732d9f324a4f20b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3732d9f324a4f20b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎍</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "大晦日",
    "kana": "おおみそか",
    "kanji": "大晦日",
    "romaji": "oomisoka",
    "vi": "Đêm giao thừa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e70994303aa7dd79\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e70994303aa7dd79)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔔</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "元日",
    "kana": "がんじつ",
    "kanji": "元日",
    "romaji": "ganjitsu",
    "vi": "Ngày mùng 1 Tết, ngày đầu năm mới",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fb7f7c041f18aa7f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fb7f7c041f18aa7f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌅</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "かるた",
    "kana": "かるた",
    "kanji": "かるた",
    "romaji": "karuta",
    "vi": "Bài lá truyền thống của Nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0faf272482422ccd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0faf272482422ccd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎴</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "挨拶",
    "kana": "あいさつ",
    "kanji": "挨拶",
    "romaji": "aisatsu",
    "vi": "Chào hỏi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f6f61a0f1c03e4b4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f6f61a0f1c03e4b4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙇</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "ごちそう",
    "kana": "ごちそう",
    "kanji": "ごちそう",
    "romaji": "gochisou",
    "vi": "Món ăn ngon đãi khách",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7128e6a3310d677f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7128e6a3310d677f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍱</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "おせち料理",
    "kana": "おせちりょうり",
    "kanji": "おせち料理",
    "romaji": "osechi ryouri",
    "vi": "Món ăn ngày Tết của người Nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4a67ddedac79a582\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4a67ddedac79a582)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍱</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "お年玉",
    "kana": "おとしだま",
    "kanji": "お年玉",
    "romaji": "otoshidama",
    "vi": "Tiền lì xì, tiền mừng tuổi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cab69049fd196e8f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cab69049fd196e8f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧧</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "年賀状",
    "kana": "ねんがじょう",
    "kanji": "年賀状",
    "romaji": "nengajou",
    "vi": "Thiệp chúc mừng năm mới",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_aa45b82271290771\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_aa45b82271290771)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✉️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "大掃除",
    "kana": "おおそうじ",
    "kanji": "大掃除",
    "romaji": "oosouji",
    "vi": "Tổng vệ sinh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b6dad9828e301d8b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b6dad9828e301d8b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧹</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "初詣",
    "kana": "はつもうで",
    "kanji": "初詣",
    "romaji": "hatsumoude",
    "vi": "Đi lễ chùa đầu năm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_239f504c74bd4e9d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_239f504c74bd4e9d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⛩️</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "親",
    "kana": "おや",
    "kanji": "親",
    "romaji": "oya",
    "vi": "Bố mẹ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_aef71d6ddffdb0f4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_aef71d6ddffdb0f4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👪</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "親戚",
    "kana": "しんせき",
    "kanji": "親戚",
    "romaji": "shinseki",
    "vi": "Họ hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d7a00e2881a9e996\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d7a00e2881a9e996)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "飾ります",
    "kana": "かざります",
    "kanji": "飾ります",
    "romaji": "kazarimasu",
    "vi": "Trang trí",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d48231a7b623520d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d48231a7b623520d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎋</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "ごろごろします",
    "kana": "ごろごろします",
    "kanji": "ごろごろします",
    "romaji": "gorogoro shimasu",
    "vi": "Nằm lười, thư giãn không làm gì cả",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a965e7daab56e4b7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a965e7daab56e4b7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛋️</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "過ごします",
    "kana": "すごします",
    "kanji": "過ごします",
    "romaji": "sugoshimasu",
    "vi": "Trải qua",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_90944889b2f968e1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_90944889b2f968e1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "つまらない",
    "kana": "つまらない",
    "kanji": "つまらない",
    "romaji": "tsumaranai",
    "vi": "Nhàm chán (nội dung)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c62694fcad76a75a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c62694fcad76a75a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥱</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "退屈（な）",
    "kana": "たいくつ（な）",
    "kanji": "退屈（な）",
    "romaji": "taikutsu(na)",
    "vi": "Buồn chán (cảm giác)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_763ca83b4cebfb3b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_763ca83b4cebfb3b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😑</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "特別（な）",
    "kana": "とくべつ（な）",
    "kanji": "特別（な）",
    "romaji": "tokubetsu(na)",
    "vi": "Đặc biệt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dd9ef1dc9aca290e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dd9ef1dc9aca290e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "面倒（な）",
    "kana": "めんどう（な）",
    "kanji": "面倒（な）",
    "romaji": "mendou(na)",
    "vi": "Phiền toái, phiền phức",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ce3953481e7da873\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ce3953481e7da873)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😫</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "あけましておめでとうございます",
    "kana": "あけましておめでとうございます",
    "kanji": "あけましておめでとうございます",
    "romaji": "akemashite omedetou gozaimasu",
    "vi": "Chúc mừng năm mới",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_de7577ad6555eadc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_de7577ad6555eadc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "久しぶり",
    "kana": "ひさしぶり",
    "kanji": "久しぶり",
    "romaji": "hisashiburi",
    "vi": "Lâu lắm không gặp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_269f85c76ee313ee\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_269f85c76ee313ee)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙋</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "戻ります",
    "kana": "もどります",
    "kanji": "戻ります",
    "romaji": "modorimasu",
    "vi": "Quay trở lại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1cfe6274b1cbad41\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1cfe6274b1cbad41)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "あげます",
    "vi": "Tặng / cho",
    "te": "あげて",
    "form1": "てあげます (làm cho ai)",
    "form2": "あげた (đã tặng)",
    "form3": "あげる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "もらいます",
    "vi": "Nhận được",
    "te": "もらって",
    "form1": "てもらいます (được ai làm cho)",
    "form2": "もらった (đã nhận)",
    "form3": "もらう",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "くれます",
    "vi": "(Ai) cho mình",
    "te": "くれて",
    "form1": "てくれます (ai làm giúp mình)",
    "form2": "くれた (đã cho mình)",
    "form3": "くれる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "いわいます",
    "vi": "Chúc mừng",
    "te": "いわって",
    "form1": "いわいましょう (cùng chúc mừng)",
    "form2": "いわった (đã chúc mừng)",
    "form3": "いわう",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "よろこびます",
    "vi": "Vui vẻ đón nhận",
    "te": "よろこんで",
    "form1": "よろこぶでしょう (chắc sẽ vui lắm)",
    "form2": "よろこんだ",
    "form3": "よろこぶ",
    "form2Label": "Thể quá khứ ngắn: Vた"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "休みはメキシコに [____]。",
    "options": [
      "帰りました",
      "帰って",
      "帰っていました",
      "帰ります"
    ],
    "correct": 2,
    "explain": "Vていました diễn tả việc đã ở/đang làm trong một khoảng thời gian đã qua.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "親に [____]、よかったです。",
    "options": [
      "会えて",
      "会って",
      "会う",
      "会った"
    ],
    "correct": 0,
    "explain": "会える là thể khả năng; 会えてよかった diễn tả vui vì gặp được.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "友だちに [____]、残念でした。",
    "options": [
      "会えなくて",
      "会わないで",
      "会って",
      "会うので"
    ],
    "correct": 0,
    "explain": "会えなくて残念 diễn tả tiếc vì không gặp được.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "私の休みは3日間 [____] でした。",
    "options": [
      "しか",
      "だけ",
      "でも",
      "ので"
    ],
    "correct": 1,
    "explain": "だけ đi với vị ngữ khẳng định để nói chỉ có.",
    "grammarScope": "official"
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「正月」 có nghĩa là gì?",
    "options": [
      "Cuối năm",
      "Đầu năm",
      "Cha mẹ",
      "Tết, dịp đầu năm mới"
    ],
    "correct": 3,
    "explain": "正月 nghĩa là Tết, dịp đầu năm mới.",
    "scopeKanji": "正月"
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "きれいな バラや チューリップを まとめた ものを [____] と 言います。",
    "options": [
      "ネクタイ",
      "とけい",
      "はなたば",
      "プレゼント"
    ],
    "correct": 2,
    "explain": "Bó hoa tươi gom lại là 「花束 (はなたば)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「年末」 có nghĩa là gì?",
    "options": [
      "Đầu năm",
      "Cha mẹ",
      "Cuối năm",
      "Bận rộn"
    ],
    "correct": 2,
    "explain": "年末 nghĩa là Cuối năm.",
    "scopeKanji": "年末"
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "「プレゼントは 何が いいでしょうか。」 ―― 「山田さんに [____] みましょう。」",
    "options": [
      "予約して",
      "見学して",
      "相談して",
      "勉強して"
    ],
    "correct": 2,
    "explain": "Hỏi ý kiến, bàn bạc với ai: 相談します (そうだんします) ➔ 「相談してみましょう」."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「年始」 có nghĩa là gì?",
    "options": [
      "Cha mẹ",
      "Đầu năm",
      "Bận rộn",
      "Đặc biệt"
    ],
    "correct": 1,
    "explain": "年始 nghĩa là Đầu năm.",
    "scopeKanji": "年始"
  },
  {
    "id": 10,
    "category": "Từ vựng",
    "q": "会社で 役職が 上がる おめでたい 出来事は [____] です。",
    "options": [
      "しゅっさん",
      "けっこん",
      "そつぎょう",
      "しょうしん"
    ],
    "correct": 3,
    "explain": "Thăng chức lên chức vụ cao hơn: 「昇進 (しょうしん)」."
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "今年は休みが3日 [____] ありませんでした。",
    "options": [
      "だけ",
      "でも",
      "ので",
      "しか"
    ],
    "correct": 3,
    "explain": "しか đi cùng vị ngữ phủ định để nói chỉ có.",
    "grammarScope": "official"
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「親」 có cách đọc nào?",
    "options": [
      "おや",
      "いそがしい",
      "とくべつ",
      "きこく"
    ],
    "correct": 0,
    "explain": "親 đọc là 「おや」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "親"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "赤ちゃんが 無事に 生まれた お祝いは [____] 祝いです。",
    "options": [
      "しょうしん",
      "しゅっさん",
      "けっこん",
      "そつぎょう"
    ],
    "correct": 1,
    "explain": "Mừng sinh em bé là mừng xuất sản: 「出産祝い (しゅっさんいわい)」."
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "プレゼントを あげたとき、相手が とても [____] くれました。",
    "options": [
      "こまって",
      "よろこんで",
      "つかれて",
      "いそいで"
    ],
    "correct": 1,
    "explain": "Đối phương vui mừng khôn xiết: 喜ぶ (よろこぶ) ➔ 「喜んでくれました」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「忙しい」 có nghĩa là gì?",
    "options": [
      "Bận rộn",
      "Đặc biệt",
      "Về nước",
      "Vui mừng"
    ],
    "correct": 0,
    "explain": "忙しい nghĩa là Bận rộn.",
    "scopeKanji": "忙しい"
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
