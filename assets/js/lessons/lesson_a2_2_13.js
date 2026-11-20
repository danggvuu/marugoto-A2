/* Marugoto A2-2 Bài 13 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "歴史",
    "kana": "れきし",
    "kanji": "歴史",
    "romaji": "rekishi",
    "vi": "Lịch sử",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0a23570855ef4d6d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0a23570855ef4d6d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "文化",
    "kana": "ぶんか",
    "kanji": "文化",
    "romaji": "bunka",
    "vi": "Văn hóa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_137128b5243b1195\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_137128b5243b1195)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏛️</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "天皇",
    "kana": "てんのう",
    "kanji": "天皇",
    "romaji": "tennou",
    "vi": "Thiên hoàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a95dc9f10805f777\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a95dc9f10805f777)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👑</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "将軍",
    "kana": "しょうぐん",
    "kanji": "将軍",
    "romaji": "shougun",
    "vi": "Tướng quân",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2a7dd87e97dafbc2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2a7dd87e97dafbc2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏯</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "城／～城",
    "kana": "しろ／～じょう",
    "kanji": "城／～城",
    "romaji": "shiro / ~jou",
    "vi": "Thành",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_80b2de35ee1c7477\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_80b2de35ee1c7477)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏯</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "舞妓さん",
    "kana": "まいこさん",
    "kanji": "舞妓さん",
    "romaji": "maiko-san",
    "vi": "Thiếu nữ Maiko (vũ kỹ tập sự)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1fe52d39122ed774\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1fe52d39122ed774)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👘</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "約～年前",
    "kana": "やく～ねんまえ",
    "kanji": "約～年前",
    "romaji": "yaku ~nenmae",
    "vi": "Khoảng... năm trước",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_55c681bdc171870a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_55c681bdc171870a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "世紀",
    "kana": "せいき",
    "kanji": "世紀",
    "romaji": "seiki",
    "vi": "Thế kỷ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2889c5adecb97aed\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2889c5adecb97aed)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "時代",
    "kana": "じだい",
    "kanji": "時代",
    "romaji": "jidai",
    "vi": "Thời đại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e7e0ee1dc370083d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e7e0ee1dc370083d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "茶道",
    "kana": "さどう",
    "kanji": "茶道",
    "romaji": "sadou",
    "vi": "Trà đạo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bc9faedeebbfb698\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bc9faedeebbfb698)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍵</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "華道",
    "kana": "かどう",
    "kanji": "華道",
    "romaji": "kadou",
    "vi": "Nghệ thuật cắm hoa truyền thống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8bbc9115b8789295\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8bbc9115b8789295)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌸</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "建てます",
    "kana": "たてます",
    "kanji": "建てます",
    "romaji": "tatemasu",
    "vi": "Xây dựng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dc1cc385952d3d37\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dc1cc385952d3d37)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏗️</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "石",
    "kana": "いし",
    "kanji": "石",
    "romaji": "ishi",
    "vi": "Đá",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_abe7044d8eaac9ff\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_abe7044d8eaac9ff)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪨</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "仏教",
    "kana": "ぶっきょう",
    "kanji": "仏教",
    "romaji": "bukkyou",
    "vi": "Phật giáo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f8fd11d1554ccfe6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f8fd11d1554ccfe6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪷</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "観光客",
    "kana": "かんこうきゃく",
    "kanji": "観光客",
    "romaji": "kankoukyaku",
    "vi": "Khách du lịch, tham quan",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5a84d0007e171139\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5a84d0007e171139)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧳</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "本物",
    "kana": "ほんもの",
    "kanji": "本物",
    "romaji": "honmono",
    "vi": "Đồ thật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b57e2131e3b1337a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b57e2131e3b1337a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💎</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "舞台",
    "kana": "ぶたい",
    "kanji": "舞台",
    "romaji": "butai",
    "vi": "Sân khấu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1fe19412a01925a7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1fe19412a01925a7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎭</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "柱",
    "kana": "はしら",
    "kanji": "柱",
    "romaji": "hashira",
    "vi": "Cột",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_63451816b6c6e055\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_63451816b6c6e055)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏛️</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "立派",
    "kana": "りっぱ",
    "kanji": "立派",
    "romaji": "rippa",
    "vi": "Tuyệt vời, tráng lệ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a3c06c595f99cf83\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a3c06c595f99cf83)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏰</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "～以上",
    "kana": "～いじょう",
    "kanji": "～以上",
    "romaji": "~ijou",
    "vi": "Trên... hơn...",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_62ef685d85bf3546\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_62ef685d85bf3546)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📈</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "中心",
    "kana": "ちゅうしん",
    "kanji": "中心",
    "romaji": "chuushin",
    "vi": "Trung tâm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3320aa647b6621f9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3320aa647b6621f9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎯</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "のります",
    "vi": "Lên xe / đi tàu",
    "te": "のって",
    "form1": "のってから (sau khi lên xe)",
    "form2": "のった (đã đi)",
    "form3": "のる"
  },
  {
    "masu": "おります",
    "vi": "Xuống xe tàu",
    "te": "おりて",
    "form1": "おりてください (xin hãy xuống ở)",
    "form2": "おりた",
    "form3": "おりる"
  },
  {
    "masu": "のりかえます",
    "vi": "Đổi tàu xe",
    "te": "のりかえて",
    "form1": "のりかえてください",
    "form2": "のりかえた",
    "form3": "のりかえる"
  },
  {
    "masu": "まよいます",
    "vi": "Lạc đường",
    "te": "まよって",
    "form1": "みちに まよってしまいました (lỡ lạc đường)",
    "form2": "まよった",
    "form3": "まよう"
  },
  {
    "masu": "つきます",
    "vi": "Tới nơi",
    "te": "ついて",
    "form1": "ついたら (khi tới nơi)",
    "form2": "ついた",
    "form3": "つく"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "京都はいつ来て [____]、楽しめます。",
    "options": [
      "は",
      "か",
      "も",
      "まで"
    ],
    "correct": 2,
    "explain": "いつVても diễn tả dù đến lúc nào thì kết quả vẫn vậy.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "妹と [____] 京都に来ました。",
    "options": [
      "二人を",
      "二人に",
      "二人が",
      "二人で"
    ],
    "correct": 3,
    "explain": "で đánh dấu nhóm người cùng thực hiện hành động.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "京都は8世紀の終わりに天皇によって [____]。",
    "options": [
      "つくりました",
      "つくって",
      "つくられました",
      "つくる"
    ],
    "correct": 2,
    "explain": "つくられました là thể bị động: được xây dựng.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "地下を 走る 電車を [____] と 言います。",
    "options": [
      "新幹線",
      "バス",
      "ちかてつ",
      "タクシー"
    ],
    "correct": 2,
    "explain": "Tàu điện ngầm chạy dưới lòng đất là 「地下鉄 (ちかてつ)」."
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「京都」 có nghĩa là gì?",
    "options": [
      "Đền Thần đạo",
      "Kyoto",
      "Chùa",
      "Phật giáo"
    ],
    "correct": 1,
    "explain": "京都 nghĩa là Kyoto.",
    "scopeKanji": "京都"
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "駅で 切符や ICカードを タッチして 通る 改札口は [____] です。",
    "options": [
      "あんないじょ",
      "ろせんず",
      "のりかえ",
      "かいさつぐち"
    ],
    "correct": 3,
    "explain": "Cổng soát vé nhà ga là 「改札口 (かいさつぐち)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「神社」 có nghĩa là gì?",
    "options": [
      "Chùa",
      "Phật giáo",
      "Đền Thần đạo",
      "Lịch sử"
    ],
    "correct": 2,
    "explain": "神社 nghĩa là Đền Thần đạo.",
    "scopeKanji": "神社"
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "道が 分からなくなって、[____] しまいました。交番で 聞きましょう。",
    "options": [
      "迷って",
      "止まって",
      "始まって",
      "終わって"
    ],
    "correct": 0,
    "explain": "Bị lạc đường: 迷います ➔ 「迷ってしまいました (まよって)」."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「お寺」 có nghĩa là gì?",
    "options": [
      "Phật giáo",
      "Chùa",
      "Lịch sử",
      "Thế giới"
    ],
    "correct": 1,
    "explain": "お寺 nghĩa là Chùa.",
    "scopeKanji": "お寺"
  },
  {
    "id": 10,
    "category": "Từ vựng",
    "q": "電車や バスの 乗り方や 行き先が 描かれている 地図は [____] です。",
    "options": [
      "ろせんず",
      "ガイドブック",
      "手紙",
      "メニュー"
    ],
    "correct": 0,
    "explain": "Sơ đồ các tuyến đường tàu xe là 「路線図 (ろせんず)」."
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "この金閣寺は足利義満によって [____]。",
    "options": [
      "建てました",
      "建てられました",
      "建てて",
      "建てる"
    ],
    "correct": 1,
    "explain": "建てられました là thể bị động: được xây dựng.",
    "grammarScope": "official"
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「仏教」 có cách đọc nào?",
    "options": [
      "れきし",
      "せかい",
      "ちゅうしん",
      "ぶっきょう"
    ],
    "correct": 3,
    "explain": "仏教 đọc là 「ぶっきょう」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "仏教"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "車や 電車を 使わずに、自分の 足で 歩いて いくことを [____] と 言います。",
    "options": [
      "とほ",
      "のりかえ",
      "うんちん",
      "とうちゃく"
    ],
    "correct": 0,
    "explain": "Đi bộ bằng chân là 「徒歩 (とほ)」 (ví dụ: 徒歩5分)."
  },
  {
    "id": 14,
    "category": "Ngữ pháp",
    "q": "京都はいつ来ても [____]。",
    "options": [
      "楽しみます",
      "楽しめます",
      "楽しんで",
      "楽しむ"
    ],
    "correct": 1,
    "explain": "いつ来ても楽しめます diễn tả Kyoto luôn thú vị dù đến lúc nào.",
    "grammarScope": "official"
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「歴史」 có nghĩa là gì?",
    "options": [
      "Lịch sử",
      "Thế giới",
      "Trung tâm",
      "Thế kỷ ～ (thế kỷ 8)"
    ],
    "correct": 0,
    "explain": "歴史 nghĩa là Lịch sử.",
    "scopeKanji": "歴史"
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
