/* Marugoto A2-2 Bài 5 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "沖縄",
    "kana": "おきなわ",
    "kanji": "沖縄",
    "romaji": "okinawa",
    "vi": "Okinawa (quần đảo phương nam Nhật Bản)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6d66e1ff64991d3c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6d66e1ff64991d3c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏝️</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "旅行",
    "kana": "りょこう",
    "kanji": "旅行",
    "romaji": "ryokou",
    "vi": "Du lịch, chuyến đi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_455328a7f2e12509\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_455328a7f2e12509)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✈️</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "準備",
    "kana": "じゅんび",
    "kanji": "準備",
    "romaji": "junbi",
    "vi": "Chuẩn bị",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e65470792f71bd21\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e65470792f71bd21)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧳</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "荷物",
    "kana": "にもつ",
    "kanji": "荷物",
    "romaji": "nimotsu",
    "vi": "Hành lý",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d02a37221c4592b3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d02a37221c4592b3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎒</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ぼうし",
    "kana": "ぼうし",
    "kanji": "ぼうし",
    "romaji": "boushi",
    "vi": "Mũ, nón",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_465310cbba005351\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_465310cbba005351)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👒</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "日焼け止め",
    "kana": "ひやけどめ",
    "kanji": "日焼け止め",
    "romaji": "hiyakedome",
    "vi": "Kem chống nắng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6d207bfb26f078b5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6d207bfb26f078b5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧴</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "水着",
    "kana": "みずぎ",
    "kanji": "水着",
    "romaji": "mizugi",
    "vi": "Đồ bơi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_aae271b53285a8a3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_aae271b53285a8a3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🩱</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "薬",
    "kana": "くすり",
    "kanji": "薬",
    "romaji": "kusuri",
    "vi": "Thuốc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_96a6d0404da8b4d8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_96a6d0404da8b4d8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💊</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "予約",
    "kana": "よやく",
    "kanji": "予約",
    "romaji": "yoyaku",
    "vi": "Đặt trước, hẹn trước",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8e8906c4544ad22b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8e8906c4544ad22b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "飛行機",
    "kana": "ひこうき",
    "kanji": "飛行機",
    "romaji": "hikouki",
    "vi": "Máy bay",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_be639f28f5888474\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_be639f28f5888474)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛫</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "空港",
    "kana": "くうこう",
    "kanji": "空港",
    "romaji": "kuukou",
    "vi": "Sân bay",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_db886fea29ed7a4c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_db886fea29ed7a4c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏢</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ホテル",
    "kana": "ホテル",
    "kanji": "ホテル",
    "romaji": "hoteru",
    "vi": "Khách sạn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3c234d8b6f44a12d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3c234d8b6f44a12d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏨</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "ガイドブック",
    "kana": "ガイドブック",
    "kanji": "ガイドブック",
    "romaji": "gaidobukku",
    "vi": "Sách hướng dẫn du lịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2622c607375e00f9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2622c607375e00f9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📖</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "観光",
    "kana": "かんこう",
    "kanji": "観光",
    "romaji": "kankou",
    "vi": "Tham quan, du lịch ngắm cảnh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_736f3fe86f4c68af\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_736f3fe86f4c68af)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📸</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "景色",
    "kana": "けしき",
    "kanji": "景色",
    "romaji": "keshiki",
    "vi": "Phong cảnh, cảnh sắc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0bba85a0cba2cba6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0bba85a0cba2cba6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌅</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "気候",
    "kana": "きこう",
    "kanji": "気候",
    "romaji": "kikou",
    "vi": "Khí hậu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e424fa30109d16f2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e424fa30109d16f2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌤️</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "暑い",
    "kana": "あつい",
    "kanji": "暑い",
    "romaji": "atsui",
    "vi": "Nóng (thời tiết)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ef78e9295f1c291a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ef78e9295f1c291a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">☀️</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "涼しい",
    "kana": "すずしい",
    "kanji": "涼しい",
    "romaji": "suzushii",
    "vi": "Mát mẻ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_987efef98c315be7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_987efef98c315be7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍃</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "忘れ物",
    "kana": "わすれもの",
    "kanji": "忘れ物",
    "romaji": "wasuremono",
    "vi": "Đồ để quên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_34e4cfa402b687fb\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_34e4cfa402b687fb)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚠️</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 5 (A2-2)",
    "jp": "気をつける",
    "kana": "きをつける",
    "kanji": "気をつける",
    "romaji": "ki o tsukeru",
    "vi": "Cẩn thận, chú ý",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7ddce50dceaade73\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7ddce50dceaade73)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👀</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "もっていきます",
    "vi": "Mang theo đi",
    "te": "もっていって",
    "form1": "もっていったほうがいい (nên mang theo)",
    "form2": "もっていかないほうがいい (không nên mang)",
    "form3": "もっていく"
  },
  {
    "masu": "よやくします",
    "vi": "Đặt trước",
    "te": "よやくして",
    "form1": "よやくしたほうがいい (nên đặt trước)",
    "form2": "よやくしないほうがいい",
    "form3": "よやくする"
  },
  {
    "masu": "しらべます",
    "vi": "Tra cứu, tìm hiểu",
    "te": "しらべて",
    "form1": "しらべたほうがいい (nên tra trước)",
    "form2": "しらべないほうがいい",
    "form3": "しらべる"
  },
  {
    "masu": "とまります",
    "vi": "Trọ lại khách sạn",
    "te": "とまって",
    "form1": "とまったほうがいい (nên trọ ở)",
    "form2": "とまらないほうがいい",
    "form3": "とまる"
  },
  {
    "masu": "わすれます",
    "vi": "Quên",
    "te": "わすれて",
    "form1": "わすれないほうがいい (không nên quên)",
    "form2": "わすれた (đã quên)",
    "form3": "わすれる"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "沖縄の 夏は 日差しが 強いですから、ぼうしを [____] ほうがいいですよ。",
    "options": [
      "持っていく",
      "持っていかない",
      "持っていって",
      "持っていった"
    ],
    "correct": 3,
    "explain": "Đưa ra lời khuyên nên làm gì: V-たほうがいい ➔ 「持っていったほうがいい」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "人気のある ホテルですから、早く [____] ほうがいいです。",
    "options": [
      "予約した",
      "予約して",
      "予約する",
      "予約しない"
    ],
    "correct": 0,
    "explain": "Nên đặt phòng sớm: 予約しました ➔ thể TA: 「予約した」 ＋ ほうがいい."
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "飛行機に 乗るために、時間に 余裕を もって [____] へ 行きます。",
    "options": [
      "みなと",
      "くうこう",
      "りょかん",
      "おてら"
    ],
    "correct": 1,
    "explain": "Đi máy bay phải đến sân bay: 「空港 (くうこう)」."
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "沖縄へ 旅行に 行くんですが、何を 着て [____] いいですか。",
    "options": [
      "行けば",
      "行ったら",
      "行くと",
      "行くなら"
    ],
    "correct": 1,
    "explain": "Xin lời khuyên nên mặc gì đi: V-たらいいですか ➔ 「行ったらいいですか」."
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "海で 泳ぐときに 着る 服を [____] と 言います。",
    "options": [
      "ゆかた",
      "ぼうし",
      "にもつ",
      "みずぎ"
    ],
    "correct": 3,
    "explain": "Đồ bơi tiếng Nhật là 「水着 (みずぎ)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「旅行」 có âm Hán Việt là gì?",
    "options": [
      "LỮ HÀNH",
      "LỮ QUÁN",
      "HÀNH LÝ",
      "DỰ ĐỊNH"
    ],
    "correct": 0,
    "explain": "旅行 có âm Hán Việt là LỮ HÀNH (du lịch)."
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "日焼けを 防ぐために 肌に 塗る クリームは [____] です。",
    "options": [
      "くすり",
      "ぼうし",
      "ひやけどめ",
      "ガイドブック"
    ],
    "correct": 2,
    "explain": "Kem chống nắng là 「日焼け止め (ひやけどめ)」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ 「予約」 đọc là gì?",
    "options": [
      "よてい",
      "やくそく",
      "よやく",
      "よき"
    ],
    "correct": 2,
    "explain": "予約 đọc là 「よやく」 (DỰ ƯỚC - Đặt chỗ trước)."
  },
  {
    "id": 9,
    "category": "Ngữ pháp",
    "q": "あしたは 朝 早く 出発しますから、今夜は 夜更かしを [____] ほうがいいです。",
    "options": [
      "した",
      "して",
      "しない",
      "する"
    ],
    "correct": 2,
    "explain": "Khuyên không nên làm gì: V-ないほうがいい ➔ 「しないほうがいい」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「暑い」 dùng để miêu tả cái gì nóng?",
    "options": [
      "Nước trà nóng",
      "Thời tiết, khí hậu nóng nực",
      "Đồ vật nóng bỏng",
      "Đồ ăn cay nóng"
    ],
    "correct": 1,
    "explain": "暑い (THỬ) chuyên dùng chỉ thời tiết khí hậu nóng nực (khác với 熱い dùng cho vật chất/nước nóng)."
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "観光地や おいしい レストランの 情報が のっている 本は [____] です。",
    "options": [
      "ガイドブック",
      "メニュー",
      "手紙",
      "辞書"
    ],
    "correct": 0,
    "explain": "Sách cẩm nang chỉ dẫn du lịch: 「ガイドブック (guidebook)」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「涼しい」 đọc là gì?",
    "options": [
      "あたたかい",
      "さむい",
      "あつい",
      "すずしい"
    ],
    "correct": 3,
    "explain": "涼しい đọc là 「すずしい」 (LƯƠNG - Mát mẻ)."
  },
  {
    "id": 13,
    "category": "Hội thoại",
    "q": "「沖縄旅行、楽しんできてね！」 ―― 「[____]」",
    "options": [
      "どういたしまして。",
      "ありがとう、行ってきます！",
      "こちらこそ、すみません。",
      "ただいま。"
    ],
    "correct": 1,
    "explain": "Khi được bạn chúc chuyến đi vui vẻ, ta đáp: 「ありがとう、行ってきます！」 (Cảm ơn, tớ lên đường đây!)."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Từ 「忘れ物」 nghĩa là gì?",
    "options": [
      "Đồ bị để quên",
      "Hành lý mang theo",
      "Quà lưu niệm",
      "Sách hướng dẫn"
    ],
    "correct": 0,
    "explain": "忘れ物 (わすれもの) là đồ bỏ quên."
  },
  {
    "id": 15,
    "category": "Từ vựng",
    "q": "旅行の 前の 日に、スーツケースに 必要な ものを 入れて [____] を します。",
    "options": [
      "かんこう",
      "よやく",
      "じゅんび",
      "りょこう"
    ],
    "correct": 2,
    "explain": "Soạn hành lý trước chuyến đi là công tác chuẩn bị: 「準備 (じゅんび) を します」."
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
