/* Marugoto A2-2 Bài 9 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "お祝い",
    "kana": "おいわい",
    "kanji": "お祝い",
    "romaji": "oiwai",
    "vi": "Lời chúc mừng, quà mừng, tiệc mừng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_74ed248eb29cbda9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_74ed248eb29cbda9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "結婚",
    "kana": "けっこん",
    "kanji": "結婚",
    "romaji": "kekkon",
    "vi": "Kết hôn, cưới hỏi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_04fb2d7ff29dbf0b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_04fb2d7ff29dbf0b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💍</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "婚約",
    "kana": "こんやく",
    "kanji": "婚約",
    "romaji": "konyaku",
    "vi": "Đính hôn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7580bcaa3fd939d1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7580bcaa3fd939d1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕊️</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "出産",
    "kana": "しゅっさん",
    "kanji": "出産",
    "romaji": "shussan",
    "vi": "Sinh nở, sinh em bé",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2a2383f62614d840\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2a2383f62614d840)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👶</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "昇進",
    "kana": "しょうしん",
    "kanji": "昇進",
    "romaji": "shoushin",
    "vi": "Thăng chức, thăng tiến",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_16e254e72a46e096\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_16e254e72a46e096)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📈</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "卒業",
    "kana": "そつぎょう",
    "kanji": "卒業",
    "romaji": "sotsugyou",
    "vi": "Tốt nghiệp ra trường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9e2d42d3cbd4fd1a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9e2d42d3cbd4fd1a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎓</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "誕生日",
    "kana": "たんじょうび",
    "kanji": "誕生日",
    "romaji": "tanjoubi",
    "vi": "Ngày sinh nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_481b88a17ddec884\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_481b88a17ddec884)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎂</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "プレゼント",
    "kana": "プレゼント",
    "kanji": "プレゼント",
    "romaji": "purezento",
    "vi": "Món quà tặng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ea5270c7ae089793\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ea5270c7ae089793)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎁</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "花束",
    "kana": "はなたば",
    "kanji": "花束",
    "romaji": "hanataba",
    "vi": "Bó hoa tươi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f722eca7f44696f2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f722eca7f44696f2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💐</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "ネクタイ",
    "kana": "ネクタイ",
    "kanji": "ネクタイ",
    "romaji": "nekutai",
    "vi": "Cà vạt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4aa86ea0d7df2545\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4aa86ea0d7df2545)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "時計",
    "kana": "とけい",
    "kanji": "時計",
    "romaji": "tokei",
    "vi": "Đồng hồ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d3d56bbad5727946\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d3d56bbad5727946)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⌚</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "選ぶ",
    "kana": "えらぶ",
    "kanji": "選ぶ",
    "romaji": "erabu",
    "vi": "Lựa chọn, tuyển chọn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ea84faf59a522f48\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ea84faf59a522f48)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "あげる",
    "kana": "あげる",
    "kanji": "あげる",
    "romaji": "ageru",
    "vi": "Tặng, biếu (cho người khác)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_782ce55fb7cc5900\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_782ce55fb7cc5900)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤲</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "もらう",
    "kana": "もらう",
    "kanji": "もらう",
    "romaji": "morau",
    "vi": "Nhận được từ ai",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5015bbc1001b9d3e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5015bbc1001b9d3e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "くれる",
    "kana": "くれる",
    "kanji": "くれる",
    "romaji": "kureru",
    "vi": "(Ai đó) tặng/cho mình",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_62288196a767ddf1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_62288196a767ddf1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💖</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "喜ぶ",
    "kana": "よろこぶ",
    "kanji": "喜ぶ",
    "romaji": "yorokobu",
    "vi": "Vui mừng, sung sướng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_40d2de7c6bdb69cb\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_40d2de7c6bdb69cb)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😊</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "相談する",
    "kana": "そうだんする",
    "kanji": "相談する",
    "romaji": "soudansuru",
    "vi": "Thảo luận, trao đổi ý kiến",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_76867d9da8f89961\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_76867d9da8f89961)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗣️</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "参加する",
    "kana": "さんかする",
    "kanji": "参加する",
    "romaji": "sankasuru",
    "vi": "Tham gia (bữa tiệc)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_73f7f11350287913\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_73f7f11350287913)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙋‍♂️</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "招待する",
    "kana": "しょうたいする",
    "kanji": "招待する",
    "romaji": "shoutaisuru",
    "vi": "Mời mọc, chiêu đãi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_63735e7079672c8f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_63735e7079672c8f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💌</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 9 (A2-2)",
    "jp": "乾杯する",
    "kana": "かんぱいする",
    "kanji": "乾杯する",
    "romaji": "kanpaisuru",
    "vi": "Cạn ly chúc mừng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0c3f39930d5f92c4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0c3f39930d5f92c4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥂</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "あげます",
    "vi": "Tặng / cho",
    "te": "あげて",
    "form1": "てあげます (làm cho ai)",
    "form2": "あげた (đã tặng)",
    "form3": "あげる"
  },
  {
    "masu": "もらいます",
    "vi": "Nhận được",
    "te": "もらって",
    "form1": "てもらいます (được ai làm cho)",
    "form2": "もらった (đã nhận)",
    "form3": "もらう"
  },
  {
    "masu": "くれます",
    "vi": "(Ai) cho mình",
    "te": "くれて",
    "form1": "てくれます (ai làm giúp mình)",
    "form2": "くれた (đã cho mình)",
    "form3": "くれる"
  },
  {
    "masu": "いわいます",
    "vi": "Chúc mừng",
    "te": "いわって",
    "form1": "いわいましょう (cùng chúc mừng)",
    "form2": "いわった (đã chúc mừng)",
    "form3": "いわう"
  },
  {
    "masu": "よろこびます",
    "vi": "Vui vẻ đón nhận",
    "te": "よろこんで",
    "form1": "よろこぶでしょう (chắc sẽ vui lắm)",
    "form2": "よろこんだ",
    "form3": "よろこぶ"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "レーさんの 結婚の [____] に、みんなで 花束を あげました。",
    "options": [
      "おみやげ",
      "おれい",
      "お祝い",
      "おねがい"
    ],
    "correct": 2,
    "explain": "Tặng quà chúc mừng nhân dịp đám cưới: 「お祝い (おいわい)」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "私は 田中さんの 誕生日に ネクタイを [____]。",
    "options": [
      "あげました",
      "くれました",
      "いただきました",
      "くださった"
    ],
    "correct": 0,
    "explain": "Tôi tặng cho người khác: 『私 ➔ 他人: あげます』 ➔ 「あげました」."
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "誕生日に 先生が すてきな 辞書を [____]。",
    "options": [
      "くれました",
      "あげました",
      "やりました",
      "もらいました"
    ],
    "correct": 0,
    "explain": "Người khác tặng cho tôi dùng 『くれます』: 先生が私に ➔ 「くれました」."
  },
  {
    "id": 4,
    "category": "Hội thoại",
    "q": "「パーティーには 何人 [____] か。」 ―― 「全部で 8人です。」",
    "options": [
      "案内します",
      "参加します",
      "見学します",
      "練習します"
    ],
    "correct": 1,
    "explain": "Có bao nhiêu người tham gia tiệc: 「参加します (さんかします)」."
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「結婚」 có cách đọc chuẩn là gì?",
    "options": [
      "けつこん",
      "けつほん",
      "けっこお",
      "けっこん"
    ],
    "correct": 3,
    "explain": "結婚 đọc là 「けっこん」 (KẾT HÔN)."
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
    "q": "Chữ Hán 「祝」 trong 「お祝い」 đọc Kunyomi là gì?",
    "options": [
      "しゅくい",
      "のろい",
      "いわい",
      "ことほぎ"
    ],
    "correct": 2,
    "explain": "祝 có âm Kun là いわ・う, danh từ là 「お祝い (おいわい)」."
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
    "q": "Từ 「卒業」 có nghĩa là gì?",
    "options": [
      "Nhập học",
      "Tốt nghiệp ra trường",
      "Đi làm việc",
      "Nghỉ hưu"
    ],
    "correct": 1,
    "explain": "卒業 (そつぎょう - TỐT NGHIỆP) nghĩa là hoàn thành khóa học, ra trường."
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
    "q": "私は 母に きれいな スカーフを [____]。(Tôi nhận được từ mẹ)",
    "options": [
      "あげました",
      "やりました",
      "貸しました",
      "もらいました"
    ],
    "correct": 3,
    "explain": "Tôi nhận được quà từ mẹ: 『[Người tặng] に/から もらいました』."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「時計」 gồm 2 chữ nào?",
    "options": [
      "THỜI + KẾ",
      "THỜI + KIM",
      "THỜI + ĐỘ",
      "ĐỒNG + KẾ"
    ],
    "correct": 0,
    "explain": "時計 gồm THỜI (時) và KẾ (計) ➔ dụng cụ đo đếm thời gian (đồng hồ)."
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
    "q": "Chữ Hán 「誕」 trong 「誕生日」 có âm Hán Việt là gì?",
    "options": [
      "ĐẢN",
      "DIÊN",
      "SINH",
      "ĐẠI"
    ],
    "correct": 0,
    "explain": "誕 có âm Hán Việt là ĐẢN (chào đời, sinh nở)."
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
