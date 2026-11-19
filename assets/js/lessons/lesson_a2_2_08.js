/* Marugoto A2-2 Bài 8 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "コンサート",
    "kana": "コンサート",
    "kanji": "コンサート",
    "romaji": "konsaato",
    "vi": "Buổi hòa nhạc, ca nhạc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d55d0bb2b56b956e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d55d0bb2b56b956e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎵</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "演奏",
    "kana": "えんそう",
    "kanji": "演奏",
    "romaji": "ensou",
    "vi": "Biểu diễn nhạc cụ, trình diễn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5130d9ed93253df1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5130d9ed93253df1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎻</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "たこ焼き",
    "kana": "たこやき",
    "kanji": "たこ焼き",
    "romaji": "takoyaki",
    "vi": "Bánh bạch tuộc nướng Takoyaki",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8ff140b541043f8a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8ff140b541043f8a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐙</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "焼きそば",
    "kana": "やきそば",
    "kanji": "焼きそば",
    "romaji": "yakisoba",
    "vi": "Mì xào Yakisoba",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bd2b9700e718d933\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bd2b9700e718d933)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍜</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "お面",
    "kana": "おめん",
    "kanji": "お面",
    "romaji": "omen",
    "vi": "Mặt nạ truyền thống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f5b77abd841825dc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f5b77abd841825dc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👺</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "金魚すくい",
    "kana": "きんぎょすくい",
    "kanji": "金魚すくい",
    "romaji": "kingyosukui",
    "vi": "Trò chơi vớt cá vàng bằng vợt giấy",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_02f10f5f33a6cab3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_02f10f5f33a6cab3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐠</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "行列",
    "kana": "ぎょうれつ",
    "kanji": "行列",
    "romaji": "gyouretsu",
    "vi": "Hàng người xếp hàng dài",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a381eb197327a4b7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a381eb197327a4b7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚶‍♂️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "並ぶ",
    "kana": "ならぶ",
    "kanji": "並ぶ",
    "romaji": "narabu",
    "vi": "Xếp hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d1ce7111a9a09f63\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d1ce7111a9a09f63)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧍</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "もう",
    "kana": "もう",
    "kanji": "もう",
    "romaji": "mou",
    "vi": "Đã... rồi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_15af3a54dfe6eb5c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_15af3a54dfe6eb5c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✔️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "まだ",
    "kana": "まだ",
    "kanji": "まだ",
    "romaji": "mada",
    "vi": "Vẫn chưa...",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1e505bb130e78c2c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1e505bb130e78c2c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "ちょうど",
    "kana": "ちょうど",
    "kanji": "ちょうど",
    "romaji": "choudo",
    "vi": "Vừa vặn, vừa đúng lúc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_23317dbb74517277\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_23317dbb74517277)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎯</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "疲れる",
    "kana": "つかれる",
    "kanji": "疲れる",
    "romaji": "tsukareru",
    "vi": "Mệt mỏi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_304a36cf8f805439\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_304a36cf8f805439)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😫</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "にぎやか（な）",
    "kana": "にぎやか（な）",
    "kanji": "にぎやか（な）",
    "romaji": "nigiyaka(na)",
    "vi": "Náo nhiệt, rộn ràng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f4341c09bb41dc75\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f4341c09bb41dc75)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎊</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "音",
    "kana": "おと",
    "kanji": "音",
    "romaji": "oto",
    "vi": "Âm thanh, tiếng động",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dfa59eba3c6c998f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dfa59eba3c6c998f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔊</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "夜",
    "kana": "よる",
    "kanji": "夜",
    "romaji": "yoru",
    "vi": "Ban đêm, buổi tối",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ec19c90e016b7343\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ec19c90e016b7343)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌙</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "楽しむ",
    "kana": "たのしむ",
    "kanji": "楽しむ",
    "romaji": "tanoshimu",
    "vi": "Tận hưởng, thưởng thức",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_07916d7224ce183d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_07916d7224ce183d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😃</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "買う",
    "kana": "かう",
    "kanji": "買う",
    "romaji": "kau",
    "vi": "Mua",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c86bcdaa94c7ddd4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c86bcdaa94c7ddd4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛍️</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "帰る",
    "kana": "かえる",
    "kanji": "帰る",
    "romaji": "kaeru",
    "vi": "Về nhà",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bf8f53d8e295133b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bf8f53d8e295133b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏠</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "案内板",
    "kana": "あんないばん",
    "kanji": "案内板",
    "romaji": "annaiban",
    "vi": "Bảng chỉ dẫn, sơ đồ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c5ab51117c103248\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c5ab51117c103248)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📋</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 8 (A2-2)",
    "jp": "お腹がすく",
    "kana": "おなかが すく",
    "kanji": "お腹がすく",
    "romaji": "onaka ga suku",
    "vi": "Đói bụng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2711513b564e91b1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2711513b564e91b1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😋</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "ならびます",
    "vi": "Xếp hàng",
    "te": "ならんで",
    "form1": "もうならびました (đã xếp hàng rồi)",
    "form2": "まだならんでいません (chưa xếp hàng)",
    "form3": "ならぶ"
  },
  {
    "masu": "はじまります",
    "vi": "Bắt đầu",
    "te": "はじまって",
    "form1": "もうはじまりました (đã bắt đầu rồi)",
    "form2": "まだはじまっていません (vẫn chưa)",
    "form3": "はじまる"
  },
  {
    "masu": "おわります",
    "vi": "Kết thúc",
    "te": "おわって",
    "form1": "もうおわりました",
    "form2": "まだおわっていません",
    "form3": "おわる"
  },
  {
    "masu": "つかれます",
    "vi": "Mệt",
    "te": "つかれて",
    "form1": "すこしつかれました (hơi mệt)",
    "form2": "つかれてから (sau khi mệt)",
    "form3": "つかれる"
  },
  {
    "masu": "かいます",
    "vi": "Mua",
    "te": "かって",
    "form1": "かってから (sau khi mua xong thì...)",
    "form2": "もうかいました",
    "form3": "かう"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "「コンサートは もう [____] か。」 ―― 「はい、10分前に 始まりました。」",
    "options": [
      "始まります",
      "始まって",
      "始まりました",
      "始まった"
    ],
    "correct": 2,
    "explain": "Đã bắt đầu chưa: もう ＋ V-ましたか ➔ 「始まりましたか」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "「お昼ごはんは もう 食べましたか。」 ―― 「いいえ、まだ [____]。」",
    "options": [
      "食べていません",
      "食べませんでした",
      "食べます",
      "食べた"
    ],
    "correct": 0,
    "explain": "Trả lời 'vẫn chưa': 『いいえ、まだ V-ていません』 ➔ 「食べていません」."
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "チケットを [____] から、会場に 入ってください。",
    "options": [
      "買ったら",
      "買って",
      "買い",
      "買う"
    ],
    "correct": 1,
    "explain": "Trình tự sau khi làm V1: V-てから ➔ 買います chuyển sang thể TE là 「買って」."
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "たこ焼きを 買うために、長い [____] に 並びました。",
    "options": [
      "まつり",
      "えんそう",
      "コンサート",
      "ぎょうれつ"
    ],
    "correct": 3,
    "explain": "Xếp hàng trong hàng người đông đúc: 「行列 (ぎょうれつ)」."
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「夜」 trong 「今夜」 đọc là gì?",
    "options": [
      "よる",
      "ゆう",
      "や",
      "ばん"
    ],
    "correct": 2,
    "explain": "今夜 đọc là 「こんや」 (KIM DẠ - Tối nay)."
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "水槽の 中の 赤い 魚を 紙の ポイですくう 遊びは [____] です。",
    "options": [
      "たこやき",
      "きんぎょすくい",
      "やきそば",
      "おめん"
    ],
    "correct": 1,
    "explain": "Trò chơi vớt cá vàng ngày hội là 「金魚すくい (きんぎょすくい)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「並ぶ」 có cách đọc Kunyomi là gì?",
    "options": [
      "ならぶ",
      "はらぶ",
      "えらぶ",
      "よらぶ"
    ],
    "correct": 0,
    "explain": "並ぶ đọc là 「ならぶ」 (TỊNH - Xếp hàng)."
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "太鼓の かっこいい [____] が 遠くから 聞こえてきます。",
    "options": [
      "みず",
      "いろ",
      "あじ",
      "おと"
    ],
    "correct": 3,
    "explain": "Tiếng trống rền vang: 「太鼓の音 (おと)」."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Từ 「音楽」 gồm 2 chữ nào?",
    "options": [
      "Ý + NHẠC",
      "ÂM + KHẢ",
      "HOA + NHẠC",
      "ÂM + NHẠC"
    ],
    "correct": 3,
    "explain": "音楽 gồm ÂM (音) và NHẠC/LẠC (楽) ➔ âm nhạc."
  },
  {
    "id": 10,
    "category": "Từ vựng",
    "q": "ずっと 歩いて いたので、足が [____] しまいました。",
    "options": [
      "ついた",
      "つかれて",
      "ならんで",
      "おわって"
    ],
    "correct": 1,
    "explain": "Mỏi mệt đôi chân: 疲れます ➔ thể TE: 「つかれて」."
  },
  {
    "id": 11,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「金魚」 đọc là gì?",
    "options": [
      "きんさかな",
      "かねうお",
      "きんぎょ",
      "こんぎょ"
    ],
    "correct": 2,
    "explain": "金魚 đọc là 「きんぎょ」 (cá vàng)."
  },
  {
    "id": 12,
    "category": "Ngữ pháp",
    "q": "太鼓の 演奏が [____] から、帰ることに しました。",
    "options": [
      "終わる",
      "終わった",
      "終わって",
      "終わりに"
    ],
    "correct": 2,
    "explain": "Sau khi buổi diễn kết thúc: V-てから ➔ 終わります ➔ 「終わって」."
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "きつねや ひょっとこの 顔の 形を した かぶり物は [____] です。",
    "options": [
      "ぼうし",
      "おめん",
      "ゆかた",
      "めがね"
    ],
    "correct": 1,
    "explain": "Mặt nạ cáo đeo trong hội là 「お面 (おめん)」."
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "「ちょうど 今、花火が [____] よ！ 見て！」",
    "options": [
      "始まったところだ",
      "終わってしまった",
      "始まらない",
      "始める"
    ],
    "correct": 0,
    "explain": "Vừa đúng lúc pháo hoa khai màn: 「始まったところだ / 始まりましたよ」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「疲」 có âm Hán Việt là gì?",
    "options": [
      "BÌ",
      "PHÁ",
      "BI",
      "THIỀM"
    ],
    "correct": 0,
    "explain": "疲 có âm Hán Việt là BÌ (mệt mỏi, bì quyện)."
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
