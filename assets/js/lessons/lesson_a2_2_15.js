/* Marugoto A2-2 Bài 15 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ごみ",
    "kana": "ごみ",
    "kanji": "ごみ",
    "romaji": "gomi",
    "vi": "Rác thải",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7a847009af2f1e2e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7a847009af2f1e2e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗑️</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "分別",
    "kana": "ぶんべつ",
    "kanji": "分別",
    "romaji": "bunbetsu",
    "vi": "Sự phân loại rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e155cdf58d2273dd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e155cdf58d2273dd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">♻️</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "燃えるごみ",
    "kana": "もえるごみ",
    "kanji": "燃えるごみ",
    "romaji": "moeru gomi",
    "vi": "Rác cháy được (rác hữu cơ, giấy)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6cba2051452310f2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6cba2051452310f2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔥</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "燃えないごみ",
    "kana": "もえないごみ",
    "kanji": "燃えないごみ",
    "romaji": "moenai gomi",
    "vi": "Rác không cháy được (kim loại, thủy tinh)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7d2c79510b128d39\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7d2c79510b128d39)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚫</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "資源ごみ",
    "kana": "しげんごみ",
    "kanji": "資源ごみ",
    "romaji": "shigen gomi",
    "vi": "Rác tái chế (giấy báo, vỏ lon)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3827d8f30e6582c9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3827d8f30e6582c9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ペットボトル",
    "kana": "ペットボトル",
    "kanji": "ペットボトル",
    "romaji": "petto botoru",
    "vi": "Chai nhựa PET",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1939065eba4aaf50\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1939065eba4aaf50)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧴</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "缶",
    "kana": "かん",
    "kanji": "缶",
    "romaji": "kan",
    "vi": "Vỏ lon kim loại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_264c8187e43ce028\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_264c8187e43ce028)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥫</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "瓶",
    "kana": "びん",
    "kanji": "瓶",
    "romaji": "bin",
    "vi": "Chai lọ thủy tinh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_52b489105c81e5de\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_52b489105c81e5de)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍾</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ビニール袋",
    "kana": "ビニールぶくろ",
    "kanji": "ビニール袋",
    "romaji": "biniiru bukuro",
    "vi": "Túi nilon",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_362ffcd224173632\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_362ffcd224173632)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛍️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "捨てる",
    "kana": "すてる",
    "kanji": "捨てる",
    "romaji": "suteru",
    "vi": "Vứt rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_70fc1ed58d62485a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_70fc1ed58d62485a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚮</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "回収する",
    "kana": "かいしゅうする",
    "kanji": "回収する",
    "romaji": "kaishuusuru",
    "vi": "Thu gom rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1ecb647afbfb1038\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1ecb647afbfb1038)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚛</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "曜日",
    "kana": "ようび",
    "kanji": "曜日",
    "romaji": "youbi",
    "vi": "Thứ trong tuần (lịch thu rác)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6dd4bd2bd81b1b24\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6dd4bd2bd81b1b24)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "ルール",
    "kana": "ルール",
    "kanji": "ルール",
    "romaji": "ruuru",
    "vi": "Quy tắc, luật lệ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_34047efc283cbef1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_34047efc283cbef1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "守る",
    "kana": "まもる",
    "kanji": "守る",
    "romaji": "mamoru",
    "vi": "Tuân thủ quy định",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bd5edfd3f8a66b13\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bd5edfd3f8a66b13)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✅</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "リサイクル",
    "kana": "リサイクル",
    "kanji": "リサイクル",
    "romaji": "risaikuru",
    "vi": "Tái chế",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e7a257822fcd73e8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e7a257822fcd73e8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "もったいない",
    "kana": "もったいない",
    "kanji": "もったいない",
    "romaji": "mottainai",
    "vi": "Lãng phí quá, tiếc của",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8bcd93630b3ae49d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8bcd93630b3ae49d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😢</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "減らす",
    "kana": "へらす",
    "kanji": "減らす",
    "romaji": "herasu",
    "vi": "Cắt giảm (lượng rác)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_479d5a3db26c29d7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_479d5a3db26c29d7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📉</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "エコバッグ",
    "kana": "エコバッグ",
    "kanji": "エコバッグ",
    "romaji": "ekobaggu",
    "vi": "Túi vải dùng nhiều lần",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a5f2ea9508fdd746\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a5f2ea9508fdd746)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👜</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "分ける",
    "kana": "わける",
    "kanji": "分ける",
    "romaji": "wakeru",
    "vi": "Chia ra, phân loại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_05bcab5e35fc31c5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_05bcab5e35fc31c5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔀</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 15 (A2-2)",
    "jp": "出す",
    "kana": "だす",
    "kanji": "出す",
    "romaji": "dasu",
    "vi": "Đem rác ra nơi tập kết",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b621e5405b989c92\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b621e5405b989c92)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚪</text>\n</svg>"
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
    "q": "ごみは ルールに 従って、きちんと 分別 [____] なりません。",
    "options": [
      "しないで",
      "しなければ",
      "したら",
      "しては"
    ],
    "correct": 1,
    "explain": "Bắt buộc phải làm: V-なければなりません ➔ しません ➔ 「しなければ」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "この日は 瓶（びん）の 日ですから、缶は [____] いいです。",
    "options": [
      "出さなくても",
      "出さなければ",
      "出さないで",
      "出して"
    ],
    "correct": 0,
    "explain": "Không cần làm cũng được: V-なくてもいいです ➔ 「出さなくても」."
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
    "q": "Chữ Hán 「分別」 có cách đọc chuẩn là gì?",
    "options": [
      "ふんべつ",
      "ぶんべつ",
      "わけべつ",
      "ぶんわけ"
    ],
    "correct": 1,
    "explain": "分別 đọc là 「ぶんべつ」 (PHÂN BIỆT - phân loại rác)."
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
    "q": "Từ 「捨てます (すてます)」 có nghĩa là gì?",
    "options": [
      "Nhặt rác lên",
      "Mua đồ",
      "Vứt rác đi",
      "Đổi hàng"
    ],
    "correct": 2,
    "explain": "捨てる (すてる - XẢ) có nghĩa là vứt bỏ."
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
    "q": "Từ 「資源」 có âm Hán Việt là gì?",
    "options": [
      "TƯ LIỆU",
      "TƯ NGUYÊN",
      "TỰ NGUYÊN",
      "TƯ BẢN"
    ],
    "correct": 1,
    "explain": "資源 có âm Hán Việt là TƯ NGUYÊN (tài nguyên)."
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
    "q": "Chữ Hán 「守る」 đọc là gì?",
    "options": [
      "まもる",
      "すてる",
      "わける",
      "へらす"
    ],
    "correct": 0,
    "explain": "守る đọc là 「まもる」 (THỦ - tuân thủ quy tắc)."
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "ペットボトルを 捨てるときは、キャップを [____] から 捨ててください。",
    "options": [
      "はずす",
      "はずした",
      "はずし",
      "はずして"
    ],
    "correct": 3,
    "explain": "Trình tự: tháo nắp ra xong rồi mới vứt ➔ V-てから: 「はずして」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「袋」 trong 「ビニール袋」 có nghĩa là gì?",
    "options": [
      "Cái chai",
      "Cái hộp",
      "Cái túi",
      "Tờ giấy"
    ],
    "correct": 2,
    "explain": "袋 (ふくろ - ĐẠI) nghĩa là cái bao, cái túi."
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
    "category": "Hội thoại",
    "q": "「ごみは どこに [____] いいですか。」 ―― 「あそこの 集積場ですよ。」",
    "options": [
      "出せば",
      "出したらば",
      "出したら",
      "出すなら"
    ],
    "correct": 2,
    "explain": "Nên đem rác ra đâu thì tốt: V-たらいいですか ➔ 「出したらいいですか」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「燃える」 có âm Hán Việt là gì?",
    "options": [
      "HỎA",
      "TIÊU",
      "THIÊU",
      "NHIÊN"
    ],
    "correct": 3,
    "explain": "燃える có âm Hán Việt là NHIÊN (bùng cháy)."
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
