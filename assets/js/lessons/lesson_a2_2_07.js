/* Marugoto A2-2 Bài 7 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "ボランティア",
    "kana": "ボランティア",
    "kanji": "ボランティア",
    "romaji": "borantia",
    "vi": "Tình nguyện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a9a8b3a5697bb08f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a9a8b3a5697bb08f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "スタッフ",
    "kana": "スタッフ",
    "kanji": "スタッフ",
    "romaji": "sutaffu",
    "vi": "Nhân viên, staff",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_88f774290d2cd012\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_88f774290d2cd012)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧑‍💼</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "ボランティアスタッフ",
    "kana": "ボランティアスタッフ",
    "kanji": "ボランティアスタッフ",
    "romaji": "borantia sutaffu",
    "vi": "Tình nguyện viên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_53ac9a9d5793f94a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_53ac9a9d5793f94a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙋‍♂️</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "まつり",
    "kana": "まつり",
    "kanji": "祭り",
    "romaji": "matsuri",
    "vi": "Lễ hội",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_239b035788d5b3e8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_239b035788d5b3e8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏮</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "イベント",
    "kana": "イベント",
    "kanji": "イベント",
    "romaji": "ibento",
    "vi": "Sự kiện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bdcc1fe570854227\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bdcc1fe570854227)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎪</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "かいじょう",
    "kana": "かいじょう",
    "kanji": "会場",
    "romaji": "kaijou",
    "vi": "Hội trường, địa điểm tổ chức",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_68f5c16bf3de16e0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_68f5c16bf3de16e0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏛️</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "ホール",
    "kana": "ホール",
    "kanji": "ホール",
    "romaji": "ho-ru",
    "vi": "Hội trường (hall)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cf41c1f6df0ab67a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cf41c1f6df0ab67a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏢</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "ひろば",
    "kana": "ひろば",
    "kanji": "広場",
    "romaji": "hiroba",
    "vi": "Quảng trường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_34bca7a8b6186f52\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_34bca7a8b6186f52)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏞️</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "ロビー",
    "kana": "ロビー",
    "kanji": "ロビー",
    "romaji": "robi-",
    "vi": "Đại sảnh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_09abfaa4b0282447\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_09abfaa4b0282447)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛋️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "おどり／おどります",
    "kana": "おどり／おどります",
    "kanji": "踊り／踊ります",
    "romaji": "odori / odorimasu",
    "vi": "Điệu nhảy / Nhảy múa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_126dfd07e10880bc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_126dfd07e10880bc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💃</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "じゅんび（します）",
    "kana": "じゅんび（します）",
    "kanji": "準備（します）",
    "romaji": "junbi(shimasu)",
    "vi": "Chuẩn bị",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e65470792f71bd21\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e65470792f71bd21)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "かたづけ",
    "kana": "かたづけ",
    "kanji": "片づけ",
    "romaji": "katazuke",
    "vi": "Sắp xếp, dọn dẹp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f224863c4dae4e93\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f224863c4dae4e93)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧹</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "あんない（します）",
    "kana": "あんない（します）",
    "kanji": "案内（します）",
    "romaji": "annai(shimasu)",
    "vi": "Hướng dẫn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_986946214dd5bb9e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_986946214dd5bb9e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💁</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "さつえい（します）",
    "kana": "さつえい（します）",
    "kanji": "撮影（します）",
    "romaji": "satsuei(shimasu)",
    "vi": "Quay phim, chụp ảnh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_36169846ae587508\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_36169846ae587508)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📷</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "うけつけ",
    "kana": "うけつけ",
    "kanji": "受付",
    "romaji": "uketsuke",
    "vi": "Quầy lễ tân",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3fc52b416f05f6eb\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3fc52b416f05f6eb)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛎️</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "つうやく",
    "kana": "つうやく",
    "kanji": "通訳",
    "romaji": "tsuuyaku",
    "vi": "Phiên dịch, thông dịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_086e2217db83257e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_086e2217db83257e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗣️</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "しかい",
    "kana": "しかい",
    "kanji": "司会",
    "romaji": "shikai",
    "vi": "MC, người dẫn chương trình",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8703caccc9a10b25\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8703caccc9a10b25)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎤</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "れんらく（します）",
    "kana": "れんらく（します）",
    "kanji": "連絡（します）",
    "romaji": "renraku(shimasu)",
    "vi": "Liên lạc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_419370b1c3eeebb2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_419370b1c3eeebb2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📞</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "れんらくさき",
    "kana": "れんらくさき",
    "kanji": "連絡先",
    "romaji": "renrakusaki",
    "vi": "Địa chỉ liên lạc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_08bbe8d91d081fce\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_08bbe8d91d081fce)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📝</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "たんとう（します）",
    "kana": "たんとう（します）",
    "kanji": "担当（します）",
    "romaji": "tantou(shimasu)",
    "vi": "Đảm nhận, phụ trách",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_554b3109c98d5e4f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_554b3109c98d5e4f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💼</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "ちゅうし（します）",
    "kana": "ちゅうし（します）",
    "kanji": "中止（します）",
    "romaji": "chuushi(shimasu)",
    "vi": "Hủy, dừng lại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_33c77facae47f82f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_33c77facae47f82f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛑</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "あつまります",
    "kana": "あつまります",
    "kanji": "集まります",
    "romaji": "atsumarimasu",
    "vi": "Tập trung, tụ họp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f638c9ce9e4b638f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f638c9ce9e4b638f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "ふります",
    "vi": "Rơi (mưa)",
    "te": "ふって",
    "form1": "ふったら (nếu mưa rơi)",
    "form2": "ふらない (không mưa)",
    "form3": "ふる"
  },
  {
    "masu": "あつまります",
    "vi": "Tập hợp lại",
    "te": "あつまって",
    "form1": "あつまったら (khi tập hợp xong)",
    "form2": "あつまりましょう (hãy tập trung lại)",
    "form3": "あつまる"
  },
  {
    "masu": "さそいます",
    "vi": "Rủ rê",
    "te": "さそって",
    "form1": "さそったら",
    "form2": "さそいませんか (sao không rủ...)",
    "form3": "さそう"
  },
  {
    "masu": "ちゅうしします",
    "vi": "Hủy bỏ",
    "te": "ちゅうしして",
    "form1": "ちゅうしになったら (nếu bị hủy)",
    "form2": "ちゅうしした",
    "form3": "ちゅうしする"
  },
  {
    "masu": "れんらくします",
    "vi": "Liên lạc",
    "te": "れんらくして",
    "form1": "れんらくしたら",
    "form2": "れんらくしてください (hãy liên lạc)",
    "form3": "れんらくする"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "あした 雨が [____]、まつりは 延期（えんき）に なります。",
    "options": [
      "ふれば",
      "ふると",
      "ふったら",
      "ふって"
    ],
    "correct": 2,
    "explain": "Câu điều kiện nếu trời mưa: ふりました ➔ thể TA là 「ふったら」.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "日本語が [____] 人と話しました。",
    "options": [
      "話したら",
      "話して",
      "話すと",
      "話せる"
    ],
    "correct": 3,
    "explain": "話す có thể dạng khả năng là 話せる.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "日本の 夏まつりで 夜空に 打ち上げられる 美しい 光は [____] です。",
    "options": [
      "たいこ",
      "はなび",
      "ゆかた",
      "やたい"
    ],
    "correct": 1,
    "explain": "Pháo hoa rực rỡ bắn trên bầu trời đêm mùa hè là 「花火 (はなび)」."
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "駅の 改札口に [____]、メッセージを 送ってください。",
    "options": [
      "ついて",
      "ついたら",
      "つくなら",
      "つく"
    ],
    "correct": 1,
    "explain": "Sau khi đến nơi (V-たら): 着きました ➔ 「着いたら (ついたら)」.",
    "grammarScope": "official"
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「受付」 có nghĩa là gì?",
    "options": [
      "Quảng trường",
      "Quầy lễ tân, tiếp tân",
      "Vấn đề",
      "Giống nhau"
    ],
    "correct": 1,
    "explain": "受付 nghĩa là Quầy lễ tân, tiếp tân.",
    "scopeKanji": "受付"
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "夏まつりで 着る 涼しい 木綿の 着物は [____] です。",
    "options": [
      "ゆかた",
      "みずぎ",
      "スーツ",
      "コート"
    ],
    "correct": 0,
    "explain": "Kimono mỏng mặc mùa hè đi hội là 「浴衣 (ゆかた)」."
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "「何時に どこで [____] か。」 ―― 「ハチ公前で 6時に しましょう。」",
    "options": [
      "泊まります",
      "泳ぎます",
      "待ち合わせます",
      "買います"
    ],
    "correct": 2,
    "explain": "Hẹn gặp mặt ở đâu: 「待ち合わせます (まちあわせます)」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「広場」 có cách đọc nào?",
    "options": [
      "ひろば",
      "もんだい",
      "おなじ",
      "あつまります"
    ],
    "correct": 0,
    "explain": "広場 đọc là 「ひろば」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "広場"
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "大雨の ため、花火は [____] に なりました。来週 行われます。",
    "options": [
      "ちゅうし",
      "しゅうごう",
      "こんざつ",
      "えんき"
    ],
    "correct": 3,
    "explain": "Dời sang tuần sau tức là bị hoãn lại: 「延期 (えんき)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「問題」 có cách đọc nào?",
    "options": [
      "もんだい",
      "おなじ",
      "あつまります",
      "はじまります"
    ],
    "correct": 0,
    "explain": "問題 đọc là 「もんだい」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "問題"
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "まつりの 会場は 人が たくさん いて、とても [____] していました。",
    "options": [
      "しゅうごう",
      "こんざつ",
      "よやく",
      "たいけん"
    ],
    "correct": 1,
    "explain": "Đông nghẹt người, chen chúc nhau: 「混雑 (こんざつ) していました」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「同じ」 có cách đọc nào?",
    "options": [
      "おなじ",
      "あつまります",
      "はじまります",
      "おわります"
    ],
    "correct": 0,
    "explain": "同じ đọc là 「おなじ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "同じ"
  },
  {
    "id": 13,
    "category": "Ngữ pháp",
    "q": "時間が [____]、屋台で たこ焼きを 買いましょう。",
    "options": [
      "あって",
      "あると",
      "あれば",
      "あったら"
    ],
    "correct": 3,
    "explain": "Nếu có thời gian: あります ➔ thể TA là 「あったら」.",
    "grammarScope": "official"
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「集まります」 có cách đọc nào?",
    "options": [
      "はじまります",
      "おわります",
      "あつまります",
      "ちゅうしします"
    ],
    "correct": 2,
    "explain": "集まります đọc là 「あつまります」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "集まります"
  },
  {
    "id": 15,
    "category": "Hội thoại",
    "q": "「まつり、とても 楽しかったですね。」 ―― 「[____]」",
    "options": [
      "いいえ、どういたしまして。",
      "こちらこそ、ごめんなさい。",
      "ええ、本当に よかったですね！",
      "はじめまして。"
    ],
    "correct": 2,
    "explain": "Đồng tình chia sẻ cảm xúc vui vẻ sau sự kiện: 「ええ、本当によかったですね！」."
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
