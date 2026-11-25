/* Marugoto A2-2 Bài 16 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "フリーマーケット",
    "kana": "フリーマーケット",
    "kanji": "フリーマーケット",
    "romaji": "furi-ma-ketto",
    "vi": "Hội chợ (đồ cũ)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_33731b41f9ce8cae\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_33731b41f9ce8cae)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎪</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "レンタルショップ",
    "kana": "レンタルショップ",
    "kanji": "レンタルショップ",
    "romaji": "rentaru shoppu",
    "vi": "Cửa hàng đồ cho thuê",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fad190c647409f80\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fad190c647409f80)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏬</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "クッション",
    "kana": "クッション",
    "kanji": "クッション",
    "romaji": "kusshon",
    "vi": "Gối",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f572a3240ef9bf17\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f572a3240ef9bf17)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛋️</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "ふとん",
    "kana": "ふとん",
    "kanji": "布団",
    "romaji": "futon",
    "vi": "Chăn, nệm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c1fb72b996d2bcb4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c1fb72b996d2bcb4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛏️</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "エコバッグ",
    "kana": "エコバッグ",
    "kanji": "エコバッグ",
    "romaji": "ekobaggu",
    "vi": "Túi thân thiện môi trường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_eab7cda53911c994\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_eab7cda53911c994)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛍️</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "ベビーベッド",
    "kana": "ベビーベッド",
    "kanji": "ベビーベッド",
    "romaji": "bebi-beddo",
    "vi": "Giường em bé",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_13772ae749bf8205\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_13772ae749bf8205)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👶</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "ベビーカー",
    "kana": "ベビーカー",
    "kanji": "ベビーカー",
    "romaji": "bebi-ka-",
    "vi": "Xe đẩy em bé",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_639208922811e5dd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_639208922811e5dd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛒</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "飽きます",
    "kana": "あきます",
    "kanji": "飽きます",
    "romaji": "akimasu",
    "vi": "Chán (ngấy)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8c43a7d2ddfa6708\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8c43a7d2ddfa6708)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥱</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "変わります",
    "kana": "かわります",
    "kanji": "変わります",
    "romaji": "kawarimasu",
    "vi": "(N) Thay đổi (Nが変わります)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9c4e592c54b965ad\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9c4e592c54b965ad)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "要ります／必要（な）",
    "kana": "いります／ひつよう（な）",
    "kanji": "要ります／必要（な）",
    "romaji": "irimasu / hitsuyou(na)",
    "vi": "Cần thiết (V)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_99e470fc4bace657\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_99e470fc4bace657)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✅</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "要りません",
    "kana": "いりません",
    "kanji": "要りません",
    "romaji": "irimasen",
    "vi": "Không cần thiết (V)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_813df1c71d206a49\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_813df1c71d206a49)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">❌</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "スーツケースを借ります",
    "kana": "スーツケースをかります",
    "kanji": "スーツケースを借ります",
    "romaji": "su-tsuke-su o karimasu",
    "vi": "Mượn vali ở cửa hàng thuê đồ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bffac48df125f131\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bffac48df125f131)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧳</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "増えます",
    "kana": "ふえます",
    "kanji": "増えます",
    "romaji": "fuemasu",
    "vi": "N tăng lên (Nが増えます)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_65386391e2271231\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_65386391e2271231)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📈</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "破れます／破ります",
    "kana": "やぶれます／やぶります",
    "kanji": "破れます／破ります",
    "romaji": "yaburemasu / yaburimasu",
    "vi": "Rách",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4dc70aae91036619\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4dc70aae91036619)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📃</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "汚れます／汚します",
    "kana": "よごれます／よごします",
    "kanji": "汚れます／汚します",
    "romaji": "yogoremasu / yogoshimasu",
    "vi": "Bị bẩn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cdf71eb8db077c80\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cdf71eb8db077c80)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧼</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "修理します／直します",
    "kana": "しゅうりします／なおします",
    "kanji": "修理します／直します",
    "romaji": "shuuri shimasu / naoshimasu",
    "vi": "Sửa chữa N",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_562760e20d91d734\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_562760e20d91d734)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔧</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "穴が開きます",
    "kana": "あながあきます",
    "kanji": "穴が開きます",
    "romaji": "ana ga akimasu",
    "vi": "Thủng lỗ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_55284dbf395711d9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_55284dbf395711d9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕳️</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 16 (A2-2)",
    "jp": "ごみを拾います",
    "kana": "ごみをひろいます",
    "kanji": "ごみを拾います",
    "romaji": "gomi o hiroimasu",
    "vi": "Nhặt rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_490794dcebde9454\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_490794dcebde9454)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧹</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "せつやくします",
    "vi": "Tiết kiệm",
    "te": "せつやくして",
    "form1": "せつやくするようにしています (cố gắng tiết kiệm)",
    "form2": "せつやくした",
    "form3": "せつやくする",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "けします",
    "vi": "Tắt điện",
    "te": "けして",
    "form1": "けすようにしています (luôn nhớ tắt)",
    "form2": "けした",
    "form3": "けす",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "とめます",
    "vi": "Khóa vòi nước",
    "te": "とめて",
    "form1": "こまめにとめましょう",
    "form2": "とめた",
    "form3": "とめる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "つづけます",
    "vi": "Tiếp tục duy trì",
    "te": "つづけて",
    "form1": "まいにちつづける (duy trì mỗi ngày)",
    "form2": "つづけた",
    "form3": "つづける",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "つかいます",
    "vi": "Dùng",
    "te": "つかって",
    "form1": "つかわない日 (ngày không dùng)",
    "form2": "つかった",
    "form3": "つかう",
    "form2Label": "Thể quá khứ ngắn: Vた"
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
