/* Marugoto A2-2 Bài 16 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "節約する",
    "kana": "せつやくする",
    "kanji": "節約する",
    "romaji": "setsuyakusuru",
    "vi": "Tiết kiệm (điện, nước, tiền bạc)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_73292284a11694b7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_73292284a11694b7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "電気",
    "kana": "でんき",
    "kanji": "電気",
    "romaji": "denki",
    "vi": "Điện năng, ánh sáng đèn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_814ace009ee44f90\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_814ace009ee44f90)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚡</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "水道",
    "kana": "すいどう",
    "kanji": "水道",
    "romaji": "suidou",
    "vi": "Nước máy sinh hoạt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4286cbf76500c2bc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4286cbf76500c2bc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚰</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "ガス",
    "kana": "ガス",
    "kanji": "ガス",
    "romaji": "gasu",
    "vi": "Khí gas đun nấu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f0c29c5d8b2dd11f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f0c29c5d8b2dd11f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔥</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "止める",
    "kana": "とめる",
    "kanji": "止める",
    "romaji": "tomeru",
    "vi": "Tắt nước, dừng lại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_79cfacbb3606f227\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_79cfacbb3606f227)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛑</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "消す",
    "kana": "けす",
    "kanji": "消す",
    "romaji": "kesu",
    "vi": "Tắt điện, dập lửa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_97ac081e7df0a222\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_97ac081e7df0a222)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📴</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "習慣",
    "kana": "しゅうかん",
    "kanji": "習慣",
    "romaji": "shuukan",
    "vi": "Thói quen tốt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_93180a7716d4fa09\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_93180a7716d4fa09)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "気をつける",
    "kana": "きをつける",
    "kanji": "気をつける",
    "romaji": "ki o tsukeru",
    "vi": "Để ý, chú tâm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a9d0f9b39a5e33e3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a9d0f9b39a5e33e3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👀</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "環境",
    "kana": "かんきょう",
    "kanji": "環境",
    "romaji": "kankyou",
    "vi": "Môi trường sống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9ccec9d590f86a43\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9ccec9d590f86a43)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌍</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "自然",
    "kana": "しぜん",
    "kanji": "自然",
    "romaji": "shizen",
    "vi": "Tự nhiên, thiên nhiên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cc9b9d74c73b854d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cc9b9d74c73b854d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌲</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "地球",
    "kana": "ちきゅう",
    "kanji": "地球",
    "romaji": "chikyuu",
    "vi": "Trái đất",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3d38d7a45f3cc493\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3d38d7a45f3cc493)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌏</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "温暖化",
    "kana": "おんだんか",
    "kanji": "温暖化",
    "romaji": "ondanka",
    "vi": "Hiện tượng ấm lên toàn cầu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7e31082db3d8626e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7e31082db3d8626e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌡️</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "マイボトル",
    "kana": "マイボトル",
    "kanji": "マイボトル",
    "romaji": "mai botoru",
    "vi": "Bình nước cá nhân mang theo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_992421acd3083782\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_992421acd3083782)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍶</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "階段",
    "kana": "かいだん",
    "kanji": "階段",
    "romaji": "kaidan",
    "vi": "Cầu thang bộ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3e99e5d1de976bcf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3e99e5d1de976bcf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪜</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "食べ残し",
    "kana": "たべのこし",
    "kanji": "食べ残し",
    "romaji": "tabenokoshi",
    "vi": "Thức ăn thừa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_67336e4f4758d409\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_67336e4f4758d409)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍱</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "むだ",
    "kana": "むだ",
    "kanji": "無駄",
    "romaji": "muda",
    "vi": "Sự lãng phí vô ích",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e3c21e9021cab976\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e3c21e9021cab976)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚫</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "大切（な）",
    "kana": "たいせつ（な）",
    "kanji": "大切（な）",
    "romaji": "taisetsu(na)",
    "vi": "Quan trọng, quý giá",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a88bd8a8aab18f56\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a88bd8a8aab18f56)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💎</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "続ける",
    "kana": "つづける",
    "kanji": "続ける",
    "romaji": "tsuzukeru",
    "vi": "Duy trì, kiên trì tiếp tục",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f6a2bc95a9f847f3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f6a2bc95a9f847f3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏃‍♂️</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "工夫する",
    "kana": "くふうする",
    "kanji": "工夫する",
    "romaji": "kufuusuru",
    "vi": "Tìm tòi sáng kiến, cải tiến cách làm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3403135fb07d99f9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3403135fb07d99f9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "毎日",
    "kana": "まいにち",
    "kanji": "毎日",
    "romaji": "mainichi",
    "vi": "Mỗi ngày, hàng ngày",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0ac33762330d1e8c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0ac33762330d1e8c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "せつやくします",
    "vi": "Tiết kiệm",
    "te": "せつやくして",
    "form1": "せつやくするようにしています (cố gắng tiết kiệm)",
    "form2": "せつやくした",
    "form3": "せつやくする"
  },
  {
    "masu": "けします",
    "vi": "Tắt điện",
    "te": "けして",
    "form1": "けすようにしています (luôn nhớ tắt)",
    "form2": "けした",
    "form3": "けす"
  },
  {
    "masu": "とめます",
    "vi": "Khóa vòi nước",
    "te": "とめて",
    "form1": "こまめにとめましょう",
    "form2": "とめた",
    "form3": "とめる"
  },
  {
    "masu": "つづけます",
    "vi": "Tiếp tục duy trì",
    "te": "つづけて",
    "form1": "まいにちつづける (duy trì mỗi ngày)",
    "form2": "つづけた",
    "form3": "つづける"
  },
  {
    "masu": "つかいます",
    "vi": "Dùng",
    "te": "つかって",
    "form1": "つかわない日 (ngày không dùng)",
    "form2": "つかった",
    "form3": "つかう"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "服が着られなく [____]。",
    "options": [
      "しました",
      "あります",
      "いました",
      "なりました"
    ],
    "correct": 3,
    "explain": "Thể khả năng phủ định + なる: không còn mặc được nữa.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "服が着られなくなった [____]、どうしますか。",
    "options": [
      "ので",
      "まで",
      "ら",
      "そう"
    ],
    "correct": 2,
    "explain": "Vたら nêu điều kiện: nếu không mặc được nữa thì làm gì?",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "ゆうこさんはネクタイをバッグ [____] しました。",
    "options": [
      "に",
      "で",
      "を",
      "が"
    ],
    "correct": 0,
    "explain": "NをNにする diễn tả biến vật này thành vật khác.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「服」 có cách đọc nào?",
    "options": [
      "じてんしゃ",
      "ふく",
      "じどうしゃ",
      "うります"
    ],
    "correct": 1,
    "explain": "服 đọc là 「ふく」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "服"
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "私たちが 住んでいる 青い 星は [____] です。",
    "options": [
      "かいだん",
      "すいどう",
      "ちきゅう",
      "ガス"
    ],
    "correct": 2,
    "explain": "Trái đất hành tinh xanh là 「地球 (ちきゅう)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「自転車」 có cách đọc nào?",
    "options": [
      "じどうしゃ",
      "じてんしゃ",
      "うります",
      "かします"
    ],
    "correct": 1,
    "explain": "自転車 đọc là 「じてんしゃ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "自転車"
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "「マイボトルを 持ち歩くのは なぜですか。」 ―― 「プラスチックごみを [____] ためです。」",
    "options": [
      "増やす",
      "残す",
      "減らす",
      "買う"
    ],
    "correct": 2,
    "explain": "Để cắt giảm rác thải: 「減らす (へらす) ためです」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「自動車」 có cách đọc nào?",
    "options": [
      "うります",
      "かします",
      "かえします",
      "じどうしゃ"
    ],
    "correct": 3,
    "explain": "自動車 đọc là 「じどうしゃ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "自動車"
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "地球全体の 気温が 徐々に 上がってしまう 環境問題は 地球[____] です。",
    "options": [
      "しゅうかん",
      "おんだんか",
      "せつやく",
      "かいだん"
    ],
    "correct": 1,
    "explain": "Ấm lên toàn cầu: 「地球温暖化 (ちきゅうおんだんか)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「売ります」 có cách đọc nào?",
    "options": [
      "うります",
      "かします",
      "かえします",
      "かわります"
    ],
    "correct": 0,
    "explain": "売ります đọc là 「うります」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "売ります"
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "服が着られなくなった [____]、フリーマーケットで売ります。",
    "options": [
      "ので",
      "まで",
      "ら",
      "そう"
    ],
    "correct": 2,
    "explain": "Vたら nêu điều kiện: nếu không mặc được nữa thì bán.",
    "grammarScope": "official"
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「貸します」 có cách đọc nào?",
    "options": [
      "かえします",
      "かします",
      "かわります",
      "～よう"
    ],
    "correct": 1,
    "explain": "貸します đọc là 「かします」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "貸します"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "毎日 繰り返し 行う 行動の 決まりを [____] と 呼びます。",
    "options": [
      "しゅうかん",
      "ちきゅう",
      "おんだんか",
      "ざんしょく"
    ],
    "correct": 0,
    "explain": "Thói quen hàng ngày là 「習慣 (しゅうかん)」."
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "食べ残し（たべのこし）を 出さないように、食べられる 分だけ [____] ように しています。",
    "options": [
      "注文する",
      "注文しない",
      "注文して",
      "注文した"
    ],
    "correct": 0,
    "explain": "Cố gắng chỉ gọi đủ phần ăn: 「注文するようにしています」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「返します」 có nghĩa là gì?",
    "options": [
      "Thay đổi",
      "Dành cho ～, dùng cho ～",
      "Dành cho trẻ em",
      "Trả lại"
    ],
    "correct": 3,
    "explain": "返します nghĩa là Trả lại.",
    "scopeKanji": "返します"
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
