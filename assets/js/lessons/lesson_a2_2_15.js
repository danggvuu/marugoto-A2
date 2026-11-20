/* Marugoto A2-2 Bài 15 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "環境",
    "kana": "かんきょう",
    "kanji": "環境",
    "romaji": "kankyou",
    "vi": "Môi trường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e16f1ec37c00f235\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e16f1ec37c00f235)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌍</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "エコ活動",
    "kana": "エコかつどう",
    "kanji": "エコ活動",
    "romaji": "eko katsudou",
    "vi": "Hoạt động bảo vệ môi trường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_345dbcfc1a0a797d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_345dbcfc1a0a797d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌱</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "省エネ",
    "kana": "しょうエネ",
    "kanji": "省エネ",
    "romaji": "shouene",
    "vi": "Tiết kiệm năng lượng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e5b9d6ad4b144c09\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e5b9d6ad4b144c09)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "温度を上げます",
    "kana": "おんどをあげます",
    "kanji": "温度を上げます",
    "romaji": "ondo o agemasu",
    "vi": "Tăng nhiệt độ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_675a0f2eee654766\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_675a0f2eee654766)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌡️</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "温度を下げます",
    "kana": "おんどをさげます",
    "kanji": "温度を下げます",
    "romaji": "ondo o sagemasu",
    "vi": "Giảm nhiệt độ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c28056f056992ee3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c28056f056992ee3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">❄️</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "むだにします",
    "kana": "むだにします",
    "kanji": "むだにします",
    "romaji": "muda ni shimasu",
    "vi": "Làm lãng phí",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_22a7fb0e03c7058c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_22a7fb0e03c7058c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚠️</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "リサイクル",
    "kana": "リサイクル",
    "kanji": "リサイクル",
    "romaji": "risaikuru",
    "vi": "Tái chế",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e7a257822fcd73e8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e7a257822fcd73e8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">♻️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ごみを分けます",
    "kana": "ごみをわけます",
    "kanji": "ごみを分けます",
    "romaji": "gomi o wakemasu",
    "vi": "Phân loại rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8667105953dab0de\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8667105953dab0de)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗂️</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ごみを減らします",
    "kana": "ごみをへらします",
    "kanji": "ごみを減らします",
    "romaji": "gomi o herashimasu",
    "vi": "Giảm bớt rác thải",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fc3b6fa348ab707d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fc3b6fa348ab707d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📉</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "空気を汚します",
    "kana": "くうきをよごします",
    "kanji": "空気を汚します",
    "romaji": "kuuki o yogoshimasu",
    "vi": "Làm bẩn, ô nhiễm không khí",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4863c09fa4630033\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4863c09fa4630033)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏭</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "油を流します",
    "kana": "あぶらをながします",
    "kanji": "油を流します",
    "romaji": "abura o nagashimasu",
    "vi": "Xả dầu mỡ xuống cống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_81e897c694631836\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_81e897c694631836)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛢️</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "空気をきれいにします",
    "kana": "くうきをきれいにします",
    "kanji": "空気をきれいにします",
    "romaji": "kuuki o kirei ni shimasu",
    "vi": "Làm sạch không khí",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d4aeb12cff68eb7d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d4aeb12cff68eb7d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍃</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "役に立ちます",
    "kana": "やくにたちます",
    "kanji": "役に立ちます",
    "romaji": "yaku ni tachimasu",
    "vi": "Có ích, hữu ích",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c46651fb0a598ea1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c46651fb0a598ea1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👍</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "料理を残します",
    "kana": "りょうりをのこします",
    "kanji": "料理を残します",
    "romaji": "ryouri o nokoshimasu",
    "vi": "Bỏ lại, chừa lại thức ăn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_734fff338fe89829\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_734fff338fe89829)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍱</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ごみを捨てます",
    "kana": "ごみをすてます",
    "kanji": "ごみを捨てます",
    "romaji": "gomi o sutemasu",
    "vi": "Vứt rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_70fc1ed58d62485a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_70fc1ed58d62485a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗑️</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ごみ箱",
    "kana": "ごみばこ",
    "kanji": "ごみ箱",
    "romaji": "gomibako",
    "vi": "Thùng rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6e434dfc9783add2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6e434dfc9783add2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪣</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "もったいない",
    "kana": "もったいない",
    "kanji": "もったいない",
    "romaji": "mottainai",
    "vi": "Lãng phí quá!",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c3ccaa9f85ad15f6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c3ccaa9f85ad15f6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😣</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "新聞紙",
    "kana": "しんぶんし",
    "kanji": "新聞紙",
    "romaji": "shinbunshi",
    "vi": "Giấy báo cũ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_37aea34db795da00\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_37aea34db795da00)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📰</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "紙",
    "kana": "かみ",
    "kanji": "紙",
    "romaji": "kami",
    "vi": "Giấy",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_702e14de8aa8972d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_702e14de8aa8972d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📄</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "すてます",
    "vi": "Vứt rác",
    "te": "すてて",
    "form1": "すてなければならない (phải vứt đúng nơi)",
    "form2": "すててはいけない (không được vứt)",
    "form3": "すてる"
  },
  {
    "masu": "わけます",
    "vi": "Phân chia",
    "te": "わけて",
    "form1": "わけてから出します",
    "form2": "わけなければならない (phải phân loại)",
    "form3": "わける"
  },
  {
    "masu": "だします",
    "vi": "Đem ra",
    "te": "だして",
    "form1": "朝8時までに出してください",
    "form2": "ださなくてもいい (không cần đem ra)",
    "form3": "だす"
  },
  {
    "masu": "まもります",
    "vi": "Tuân thủ",
    "te": "まもって",
    "form1": "ルールをまもってください",
    "form2": "まもった",
    "form3": "まもる"
  },
  {
    "masu": "へらします",
    "vi": "Cắt giảm",
    "te": "へらして",
    "form1": "ごみをへらしましょう",
    "form2": "へらした",
    "form3": "へらす"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "会議室の電気が [____] ままです。",
    "options": [
      "つけて",
      "ついた",
      "つく",
      "ついて"
    ],
    "correct": 1,
    "explain": "Vたまま diễn tả trạng thái tiếp tục giữ nguyên.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "私は自分のはしを使う [____] しています。",
    "options": [
      "ように",
      "ために",
      "ので",
      "まで"
    ],
    "correct": 0,
    "explain": "Vるようにしています nói về thói quen mình cố gắng duy trì.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "生ごみや 紙くずなどの 燃やすことが できる ごみは [____] です。",
    "options": [
      "もえないごみ",
      "もえるごみ",
      "しげんごみ",
      "そだいごみ"
    ],
    "correct": 1,
    "explain": "Rác cháy được là 「燃えるごみ (もえるごみ)」."
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「油」 có cách đọc nào?",
    "options": [
      "かみ",
      "あぶら",
      "おんど",
      "かつどう"
    ],
    "correct": 1,
    "explain": "油 đọc là 「あぶら」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "油"
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "清涼飲料水や お茶が 入っている プラスチックの ボトルは [____] です。",
    "options": [
      "ペットボトル",
      "ビニール袋",
      "かん",
      "びん"
    ],
    "correct": 0,
    "explain": "Chai nhựa đựng trà/nước là 「ペットボトル (PET bottle)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「紙」 có cách đọc nào?",
    "options": [
      "おんど",
      "かつどう",
      "かみ",
      "かいぎしつ"
    ],
    "correct": 2,
    "explain": "紙 đọc là 「かみ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "紙"
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "まだ 使える 物を 簡単に 捨ててしまうのは [____] です。",
    "options": [
      "すばらしい",
      "にぎやか",
      "しずか",
      "もったいない"
    ],
    "correct": 3,
    "explain": "Lãng phí tiếc của: 「もったいない」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「温度」 có cách đọc nào?",
    "options": [
      "かつどう",
      "おんど",
      "かいぎしつ",
      "さむい"
    ],
    "correct": 1,
    "explain": "温度 đọc là 「おんど」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "温度"
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "スーパーの レジ袋を もらわないで、自分の [____] を 使います。",
    "options": [
      "エコバッグ",
      "ペットボトル",
      "メニュー",
      "ガイドブック"
    ],
    "correct": 0,
    "explain": "Túi vải dùng nhiều lần để bảo vệ môi trường: 「エコバッグ (eco-bag)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「活動」 có cách đọc nào?",
    "options": [
      "かつどう",
      "かいぎしつ",
      "さむい",
      "だします"
    ],
    "correct": 0,
    "explain": "活動 đọc là 「かつどう」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "活動"
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "会議室の電気を消す [____] しています。",
    "options": [
      "ために",
      "ので",
      "まで",
      "ように"
    ],
    "correct": 3,
    "explain": "Vるようにしています diễn tả thói quen được duy trì.",
    "grammarScope": "official"
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「会議室」 có cách đọc nào?",
    "options": [
      "さむい",
      "だします",
      "かいぎしつ",
      "～ど（にじゅうはちど）"
    ],
    "correct": 2,
    "explain": "会議室 đọc là 「かいぎしつ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "会議室"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "一度 使った 物を もう一度 使えるように 加工することを [____] と 言います。",
    "options": [
      "アレルギー",
      "サプライズ",
      "リサイクル",
      "メッセージ"
    ],
    "correct": 2,
    "explain": "Tái chế đồ phế liệu: 「リサイクル (recycle)」."
  },
  {
    "id": 14,
    "category": "Ngữ pháp",
    "q": "自分のはしは、ごみをへらす [____] いいです。",
    "options": [
      "ので",
      "なら",
      "のに",
      "まで"
    ],
    "correct": 2,
    "explain": "Vるのにいい nêu công dụng phù hợp.",
    "grammarScope": "official"
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「寒い」 có nghĩa là gì?",
    "options": [
      "Đưa ra, lấy ra",
      "～ độ (28 độ)",
      "～ điểm (100 điểm)",
      "Lạnh (thời tiết)"
    ],
    "correct": 3,
    "explain": "寒い nghĩa là Lạnh (thời tiết).",
    "scopeKanji": "寒い"
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
