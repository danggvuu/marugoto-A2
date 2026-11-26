/* Marugoto A2-2 Bài 4 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "かけます",
    "kana": "かけます",
    "kanji": "かけます",
    "romaji": "kakemasu",
    "vi": "Rưới, chan",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ea40f26be5ddcd70\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ea40f26be5ddcd70)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥣</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "つけます",
    "kana": "つけます",
    "kanji": "つけます",
    "romaji": "tsukemasu",
    "vi": "Chấm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0e002d730a716277\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0e002d730a716277)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥢</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "いれます",
    "kana": "いれます",
    "kanji": "入れます",
    "romaji": "iremasu",
    "vi": "Thêm vào, cho vào",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5a68c569760c1fad\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5a68c569760c1fad)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🫗</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "ぬります",
    "kana": "ぬります",
    "kanji": "塗ります",
    "romaji": "nurimasu",
    "vi": "Bôi, sơn, phết",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ebfbcd53f4229e3d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ebfbcd53f4229e3d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧈</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "やきます",
    "kana": "やきます",
    "kanji": "焼きます",
    "romaji": "yakimasu",
    "vi": "Nướng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4294911d5e17c260\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4294911d5e17c260)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍳</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "いいにおい",
    "kana": "いいにおい",
    "kanji": "いいにおい",
    "romaji": "ii nioi",
    "vi": "Mùi thơm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b08f51c00f08bd06\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b08f51c00f08bd06)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👃</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "ふた",
    "kana": "ふた",
    "kanji": "蓋",
    "romaji": "futa",
    "vi": "Nắp, vung",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d61275d30518c8aa\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d61275d30518c8aa)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍲</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "さら",
    "kana": "さら",
    "kanji": "皿",
    "romaji": "sara",
    "vi": "Đĩa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_592bb98ae8759b14\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_592bb98ae8759b14)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍽️</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "ちゃわん",
    "kana": "ちゃわん",
    "kanji": "茶碗",
    "romaji": "chawan",
    "vi": "Bát",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9d6e81a74cd3e447\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9d6e81a74cd3e447)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍚</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "たれ／ソース",
    "kana": "たれ／ソース",
    "kanji": "たれ／ソース",
    "romaji": "tare / so-su",
    "vi": "Nước sốt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b7df2960dcae1928\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b7df2960dcae1928)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🫙</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "しょうゆ",
    "kana": "しょうゆ",
    "kanji": "醤油",
    "romaji": "shouyu",
    "vi": "Xì dầu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5635d8a97fb10035\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5635d8a97fb10035)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍶</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "とうがらし",
    "kana": "とうがらし",
    "kanji": "唐辛子",
    "romaji": "tougarashi",
    "vi": "Ớt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a5c861f4511ab8b3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a5c861f4511ab8b3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌶️</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "こしょう",
    "kana": "こしょう",
    "kanji": "胡椒",
    "romaji": "koshou",
    "vi": "Hạt tiêu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1b19a372ed7955b8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1b19a372ed7955b8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧂</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "バター",
    "kana": "バター",
    "kanji": "バター",
    "romaji": "bata-",
    "vi": "Bơ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_84591945136c13fc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_84591945136c13fc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧈</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "おなかがすきました",
    "kana": "おなかがすきました",
    "kanji": "お腹が空きました",
    "romaji": "onaka ga sukimashita",
    "vi": "Đói",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fda4340b2ab3a408\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fda4340b2ab3a408)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤤</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "のどがかわきました",
    "kana": "のどがかわきました",
    "kanji": "喉が渇きました",
    "romaji": "nodo ga kawakimashita",
    "vi": "Khát",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6525276c8d32fc52\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6525276c8d32fc52)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥤</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "かんぱい",
    "kana": "かんぱい",
    "kanji": "乾杯",
    "romaji": "kanpai",
    "vi": "Cạn ly",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9c8f65a2be728ae3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9c8f65a2be728ae3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍻</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "いろがかわります",
    "kana": "いろがかわります",
    "kanji": "色が変わります",
    "romaji": "iro ga kawarimasu",
    "vi": "Màu thay đổi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a37431fa02100c22\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a37431fa02100c22)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎨</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "がまんする",
    "kana": "がまんする",
    "kanji": "我慢する",
    "romaji": "gaman suru",
    "vi": "Chịu đựng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5d8204b48ad7d87c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5d8204b48ad7d87c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😣</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "料理を残します",
    "kana": "りょうりをのこします",
    "kanji": "料理を残します",
    "romaji": "ryouri o nokoshimasu",
    "vi": "Bỏ thừa đồ ăn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a964e1be5608f4a2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a964e1be5608f4a2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍱</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "音を立てます",
    "kana": "おとをたてます",
    "kanji": "音を立てます",
    "romaji": "oto o tatemasu",
    "vi": "Tạo ra âm thanh, tiếng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d0befd71c0c559d7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d0befd71c0c559d7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔊</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "かゆい",
    "kana": "かゆい",
    "kanji": "痒い",
    "romaji": "kayui",
    "vi": "Ngứa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d3369431471d013d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d3369431471d013d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😖</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "汗が出ます",
    "kana": "あせがでます",
    "kanji": "汗が出ます",
    "romaji": "ase ga demasu",
    "vi": "Toát mồ hôi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2d399344f75090b2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2d399344f75090b2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💦</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "つけます",
    "vi": "Chấm (nước sốt)",
    "te": "つけて",
    "form1": "つけないで (xin đừng chấm)",
    "form2": "つけた (đã chấm)",
    "form3": "つける (thể từ điển)",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "やきます",
    "vi": "Nướng",
    "te": "やいて",
    "form1": "やかないで (đừng nướng)",
    "form2": "やいた (đã nướng)",
    "form3": "やく",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "にます",
    "vi": "Ninh / hầm",
    "te": "にて",
    "form1": "にないで",
    "form2": "にた",
    "form3": "にる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "かけます",
    "vi": "Rưới lên",
    "te": "かけて",
    "form1": "かけないで (đừng rưới lên)",
    "form2": "かけた",
    "form3": "かける",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "のこします",
    "vi": "Để thừa",
    "te": "のこして",
    "form1": "のこさないで (xin đừng để thừa)",
    "form2": "のこした",
    "form3": "のこす",
    "form2Label": "Thể quá khứ ngắn: Vた"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "ここで写真を [____] いけません。",
    "options": [
      "撮らないで",
      "撮っては",
      "撮ってから",
      "撮ると"
    ],
    "correct": 1,
    "explain": "Vてはいけません diễn tả điều bị cấm.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "飲み物は乾杯 [____]、飲みましょう。",
    "options": [
      "しないで",
      "してから",
      "しては",
      "すると"
    ],
    "correct": 1,
    "explain": "Vてから nối hai hành động theo thứ tự.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "何も [____] 食べます。",
    "options": [
      "つけては",
      "つけると",
      "つけてから",
      "つけないで"
    ],
    "correct": 3,
    "explain": "Vないで diễn tả làm việc khác mà không thực hiện hành động V.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "イスラム教（ハラール）の 友達は [____] を 食べることが できません。",
    "options": [
      "やさい",
      "ぶたにく",
      "たまご",
      "くだもの"
    ],
    "correct": 1,
    "explain": "Người theo đạo Hồi kiêng thịt lợn: 「豚肉 (ぶたにく)」."
  },
  {
    "id": 5,
    "category": "Ngữ pháp",
    "q": "刺身（さしみ）は しょうゆに [____] 食べてください。",
    "options": [
      "つけて",
      "ついて",
      "かけて",
      "のせて"
    ],
    "correct": 0,
    "explain": "Chấm sashimi vào nước tương xì dầu dùng động từ 「つける」 ➔ thể TE là 「つけて」.",
    "grammarScope": "official"
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「ご飯」 có cách đọc nào?",
    "options": [
      "しお",
      "すべて",
      "ごはん",
      "ぜんぜん"
    ],
    "correct": 2,
    "explain": "ご飯 đọc là 「ごはん」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "ご飯"
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "甲殻類（こうかくるい）の [____] が あるので、エビや カニは 食べられません。",
    "options": [
      "メニュー",
      "デザート",
      "アレルギー",
      "スプーン"
    ],
    "correct": 2,
    "explain": "Dị ứng với tôm cua: 「アレルギー (dị ứng)」."
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "ごはんが とても おいしくて、もう 一杯 ほしいときに 「ごはんの [____]、お願いします」 と 言います。",
    "options": [
      "おかいけい",
      "おみやげ",
      "おちゅうもん",
      "おかわり"
    ],
    "correct": 3,
    "explain": "Yêu cầu thêm một bát cơm nữa: 「おかわり」 (xới thêm / phần nữa)."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「塩」 có nghĩa là gì?",
    "options": [
      "Muối",
      "Tất cả (lịch sự)",
      "Hoàn toàn (không)",
      "Tất cả, toàn bộ"
    ],
    "correct": 0,
    "explain": "塩 nghĩa là Muối.",
    "scopeKanji": "塩"
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「全て」 có cách đọc nào?",
    "options": [
      "ぜんぜん",
      "ぜんぶ",
      "すべて",
      "あんぜん"
    ],
    "correct": 2,
    "explain": "全て đọc là 「すべて」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "全て"
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "スープを 飲むときは、はしではなく [____] を 使います。",
    "options": [
      "スプーン",
      "ナイフ",
      "フォーク",
      "おさら"
    ],
    "correct": 0,
    "explain": "Uống canh, húp súp dùng muỗng/thìa: 「スプーン (spoon)」."
  },
  {
    "id": 12,
    "category": "Ngữ pháp",
    "q": "ここでは魚を [____] はいけません。",
    "options": [
      "食べて",
      "食べないで",
      "食べると",
      "食べてから"
    ],
    "correct": 0,
    "explain": "食べてはいけません nghĩa là không được ăn.",
    "grammarScope": "official"
  },
  {
    "id": 13,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「全然」 có nghĩa là gì?",
    "options": [
      "Tất cả, toàn bộ",
      "An toàn",
      "Nóng",
      "Hoàn toàn (không)"
    ],
    "correct": 3,
    "explain": "全然 nghĩa là Hoàn toàn (không).",
    "scopeKanji": "全然"
  },
  {
    "id": 14,
    "category": "Từ vựng",
    "q": "たくさん 食べて、もう これ以上 食べられない 状態を 「お腹が [____]」 と 言います。",
    "options": [
      "すいた",
      "いたい",
      "いっぱい",
      "あいた"
    ],
    "correct": 2,
    "explain": "No căng bụng: 「お腹がいっぱい」."
  },
  {
    "id": 15,
    "category": "Ngữ pháp",
    "q": "しょうゆをつけて食べる [____]、おいしいです。",
    "options": [
      "まで",
      "と",
      "しか",
      "ので"
    ],
    "correct": 1,
    "explain": "Vると nêu kết quả thường xảy ra.",
    "grammarScope": "official"
  },
  {
    "id": 16,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "Đổi 食べる sang đúng mẫu cấm Vてはいけません.",
    "options": [
      "食べてはいけません",
      "食べないでください",
      "食べてから",
      "食べると"
    ],
    "correct": 0,
    "explain": "食べる → 食べて → 食べてはいけません. 食べないでください là lời yêu cầu đừng ăn, không phải mẫu Vてはいけません được hỏi.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 17,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "「飲んではだめです」の短い形はどれですか。",
    "options": [
      "飲んちゃだめです",
      "飲んじゃだめです",
      "飲みじゃだめです",
      "飲まじゃだめです"
    ],
    "correct": 1,
    "explain": "飲んでは → 飲んじゃ: giữ 飲ん, đổi では thành じゃ. Với ては thì rút thành ちゃ, như 食べては → 食べちゃ.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 18,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "Dùng てから để nói ‘Rửa tay xong rồi ăn cơm’: 手を洗って [____]、ご飯を食べます。",
    "options": [
      "と",
      "ないで",
      "から",
      "では"
    ],
    "correct": 2,
    "explain": "洗う → 洗ってから: rửa tay xong rồi mới ăn. てから nhấn mạnh trình tự hoàn tất hành động.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 19,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "‘Hãy ăn mà không chấm xì dầu.’ しょうゆを [____] 食べてください。",
    "options": [
      "つけてから",
      "つけると",
      "つけちゃ",
      "つけないで"
    ],
    "correct": 3,
    "explain": "つけないで食べる là ăn mà không chấm xì dầu. つけてから lại có nghĩa là chấm xong rồi mới ăn, trái với yêu cầu.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 20,
    "category": "Chữ Hán",
    "scopeKanji": "ご飯",
    "q": "「ご飯」の読み方はどれですか。",
    "options": [
      "ごばん",
      "ごめし",
      "ごぱん",
      "ごはん"
    ],
    "correct": 3,
    "explain": "ご飯 đọc là ごはん, nghĩa là cơm/bữa ăn.",
    "reviewVersion": "a22-practice20-v1"
  }
];

const SENTENCE_PRACTICE_DATA = [
  {
    "id": 1,
    "vi": "Tôi cho muối vào cơm.",
    "jp": "ご飯に塩を入れます。",
    "requireKanji": true,
    "accepted": [
      "ご飯に塩を加えます。"
    ]
  },
  {
    "id": 2,
    "vi": "Hãy cho tất cả nguyên liệu vào nồi.",
    "jp": "材料を全て鍋に入れてください。",
    "requireKanji": true,
    "accepted": [
      "全ての材料を鍋に入れてください。"
    ]
  },
  {
    "id": 3,
    "vi": "Tôi hoàn toàn không ăn món cay.",
    "jp": "私は辛い料理を全然食べません。",
    "requireKanji": true,
    "accepted": [
      "私は辛い料理をまったく食べません。"
    ]
  },
  {
    "id": 4,
    "vi": "Tôi đã ăn hết tất cả cơm.",
    "jp": "ご飯を全部食べました。",
    "requireKanji": true,
    "accepted": [
      "ご飯を全て食べました。"
    ]
  },
  {
    "id": 5,
    "vi": "Phòng này an toàn.",
    "jp": "この部屋は安全です。",
    "requireKanji": true,
    "accepted": []
  },
  {
    "id": 6,
    "vi": "Món ăn nóng nên hãy cẩn thận.",
    "jp": "料理が熱いので、気をつけてください。",
    "requireKanji": true,
    "accepted": [
      "料理が熱いので、注意してください。"
    ]
  },
  {
    "id": 7,
    "vi": "Cà phê này đắng.",
    "jp": "このコーヒーは苦いです。",
    "requireKanji": true,
    "accepted": [
      "これは苦いコーヒーです。"
    ]
  },
  {
    "id": 8,
    "vi": "Tôi thấy căng tức bụng vì đã ăn nhiều.",
    "jp": "たくさん食べたので、お腹が苦しいです。",
    "requireKanji": true,
    "accepted": [
      "たくさん食べたので、おなかが苦しいです。"
    ]
  },
  {
    "id": 9,
    "vi": "Tôi ngại ăn ớt.",
    "jp": "私は唐辛子が苦手です。",
    "requireKanji": true,
    "accepted": [
      "私はとうがらしが苦手です。"
    ]
  },
  {
    "id": 10,
    "vi": "Hãy chan nước sốt lên cơm.",
    "jp": "ご飯にソースをかけてください。",
    "requireKanji": true,
    "accepted": [
      "ご飯にたれをかけてください。"
    ]
  },
  {
    "id": 11,
    "vi": "Hãy chấm thức ăn vào xì dầu rồi ăn.",
    "jp": "料理を醤油につけて食べてください。",
    "requireKanji": true,
    "accepted": [
      "料理をしょうゆにつけて食べてください。"
    ]
  },
  {
    "id": 12,
    "vi": "Tôi cho hạt tiêu vào súp.",
    "jp": "スープに胡椒を入れます。",
    "requireKanji": true,
    "accepted": [
      "スープにこしょうを入れます。"
    ]
  },
  {
    "id": 13,
    "vi": "Tôi phết bơ lên bánh mì rồi ăn.",
    "jp": "パンにバターを塗って食べます。",
    "requireKanji": true,
    "accepted": [
      "パンにバターをぬって食べます。"
    ]
  },
  {
    "id": 14,
    "vi": "Tôi nướng cá trước bữa tối.",
    "jp": "晩ご飯の前に魚を焼きます。",
    "requireKanji": true,
    "accepted": [
      "夕ご飯の前に魚を焼きます。",
      "夕食の前に魚を焼きます。"
    ]
  },
  {
    "id": 15,
    "vi": "Từ trong nồi có mùi thơm bay ra.",
    "jp": "鍋からいいにおいがします。",
    "requireKanji": true,
    "accepted": [
      "鍋からいい匂いがします。",
      "鍋から良い匂いがします。"
    ]
  },
  {
    "id": 16,
    "vi": "Hãy đậy nắp nồi.",
    "jp": "鍋に蓋をしてください。",
    "requireKanji": true,
    "accepted": [
      "鍋にふたをしてください。",
      "鍋の蓋を閉めてください。"
    ]
  },
  {
    "id": 17,
    "vi": "Hãy đặt bát và đĩa lên bàn.",
    "jp": "茶碗と皿をテーブルに置いてください。",
    "requireKanji": true,
    "accepted": [
      "お茶碗とお皿をテーブルに置いてください。"
    ]
  },
  {
    "id": 18,
    "vi": "Món này cay nhưng tôi vẫn chịu.",
    "jp": "この料理は辛いですが、我慢します。",
    "requireKanji": true,
    "accepted": [
      "この料理は辛いですけど、我慢します。"
    ]
  },
  {
    "id": 19,
    "vi": "Tôi đang đói bụng.",
    "jp": "お腹が空きました。",
    "requireKanji": true,
    "accepted": [
      "おなかが空きました。",
      "お腹がすきました。"
    ]
  },
  {
    "id": 20,
    "vi": "Vì khát nước nên tôi đã uống trà.",
    "jp": "喉が渇いたので、お茶を飲みました。",
    "requireKanji": true,
    "accepted": [
      "のどが渇いたので、お茶を飲みました。",
      "喉がかわいたので、お茶を飲みました。"
    ]
  },
  {
    "id": 21,
    "vi": "Sau khi rửa tay, tôi ăn cơm.",
    "jp": "手を洗ってから、ご飯を食べます。",
    "requireKanji": true,
    "accepted": [
      "手を洗ってから、食事をします。"
    ]
  },
  {
    "id": 22,
    "vi": "Sau khi nướng cá, hãy đặt nó lên đĩa.",
    "jp": "魚を焼いてから、皿にのせてください。",
    "requireKanji": true,
    "accepted": [
      "魚を焼いてから、皿に載せてください。",
      "魚を焼いてから、お皿にのせてください。"
    ]
  },
  {
    "id": 23,
    "vi": "Hãy ăn mà không chấm xì dầu.",
    "jp": "醤油をつけないで食べてください。",
    "requireKanji": true,
    "accepted": [
      "しょうゆをつけないで食べてください。",
      "醤油につけないで食べてください。"
    ]
  },
  {
    "id": 24,
    "vi": "Hãy ăn mà không để thừa đồ ăn.",
    "jp": "料理を残さないで食べてください。",
    "requireKanji": true,
    "accepted": [
      "料理を全部食べてください。"
    ]
  },
  {
    "id": 25,
    "vi": "Không được gây tiếng động lớn trong phòng này.",
    "jp": "この部屋で大きな音を立ててはいけません。",
    "requireKanji": true,
    "accepted": [
      "この部屋で大きな音を立ててはだめです。",
      "この部屋で大きな音を立てちゃだめです。"
    ]
  },
  {
    "id": 26,
    "vi": "Khi nướng thịt bò, màu của thịt sẽ thay đổi.",
    "jp": "牛肉を焼くと、色が変わります。",
    "requireKanji": true,
    "accepted": [
      "牛肉を焼くと、牛肉の色が変わります。"
    ]
  },
  {
    "id": 27,
    "vi": "Cứ mở nắp ra thì mùi thơm sẽ bay ra.",
    "jp": "蓋を開けると、いいにおいがします。",
    "requireKanji": true,
    "accepted": [
      "ふたを開けると、いいにおいがします。",
      "蓋を開けると、いい匂いがします。"
    ]
  },
  {
    "id": 28,
    "vi": "Không được chạm vào món ăn nóng.",
    "jp": "熱い料理に触ってはいけません。",
    "requireKanji": true,
    "accepted": [
      "熱い料理に触ってはだめです。",
      "熱い料理に触っちゃだめです。"
    ]
  },
  {
    "id": 29,
    "vi": "Hãy uống trà mà không cho đường.",
    "jp": "砂糖を入れないで、お茶を飲んでください。",
    "requireKanji": true,
    "accepted": [
      "お茶は砂糖を入れないで飲んでください。"
    ]
  },
  {
    "id": 30,
    "vi": "Đừng cho hạt tiêu vào súp.",
    "jp": "スープに胡椒を入れないでください。",
    "requireKanji": true,
    "accepted": [
      "スープにこしょうを入れないでください。"
    ]
  },
  {
    "id": 31,
    "vi": "Sau khi cho bơ vào, hãy khuấy đều.",
    "jp": "バターを入れてから、よく混ぜてください。",
    "requireKanji": true,
    "accepted": [
      "バターを入れてから、よくかき混ぜてください。"
    ]
  },
  {
    "id": 32,
    "vi": "Hãy chấm rau vào nước sốt rồi ăn.",
    "jp": "野菜をたれにつけて食べてください。",
    "requireKanji": true,
    "accepted": [
      "野菜をソースにつけて食べてください。"
    ]
  },
  {
    "id": 33,
    "vi": "Cứ nướng thịt thì mùi thơm sẽ lan ra.",
    "jp": "肉を焼くと、いいにおいがします。",
    "requireKanji": true,
    "accepted": [
      "肉を焼くと、いい匂いがします。"
    ]
  },
  {
    "id": 34,
    "vi": "Đừng ăn nhiều ớt nhé.",
    "jp": "唐辛子をたくさん食べちゃだめです。",
    "requireKanji": true,
    "accepted": [
      "とうがらしをたくさん食べちゃだめです。",
      "唐辛子をたくさん食べてはいけません。"
    ]
  },
  {
    "id": 35,
    "vi": "Không được uống nước này.",
    "jp": "この水を飲んではいけません。",
    "requireKanji": true,
    "accepted": [
      "この水を飲んではだめです。",
      "この水を飲んじゃだめです。"
    ]
  },
  {
    "id": 36,
    "vi": "Sau khi nâng cốc chúc mừng, mọi người cùng dùng bữa.",
    "jp": "乾杯してから、みんなで食事をします。",
    "requireKanji": true,
    "accepted": [
      "乾杯してから、みんなでご飯を食べます。"
    ]
  },
  {
    "id": 37,
    "vi": "Đừng gây tiếng động trong bữa ăn.",
    "jp": "食事中、音を立てないでください。",
    "requireKanji": true,
    "accepted": [
      "食事中は、音を立てないでください。"
    ]
  },
  {
    "id": 38,
    "vi": "Sau khi thịt bò đổi màu, hãy cho rau vào nồi.",
    "jp": "牛肉の色が変わってから、野菜を鍋に入れてください。",
    "requireKanji": true,
    "accepted": [
      "牛肉の色が変わってから、鍋に野菜を入れてください。"
    ]
  },
  {
    "id": 39,
    "vi": "Cứ ăn món này là tôi lại ngứa người và toát mồ hôi.",
    "jp": "この料理を食べると、体が痒くなって汗が出ます。",
    "requireKanji": true,
    "accepted": [
      "この料理を食べると、体がかゆくなって汗が出ます。"
    ]
  },
  {
    "id": 40,
    "vi": "Không được uống rượu trong phòng này nhé.",
    "jp": "この部屋でお酒を飲んじゃだめです。",
    "requireKanji": true,
    "accepted": [
      "この部屋でお酒を飲んではいけません。",
      "この部屋でお酒を飲んではだめです。",
      "この部屋で酒を飲んじゃだめです。"
    ]
  }
];

const KANJI_PRACTICE_DATA = [
  {
    "id": "official-4-1",
    "word": "ご飯",
    "kana": "ごはん",
    "mean": "Cơm, bữa cơm",
    "accepted": []
  },
  {
    "id": "official-4-2",
    "word": "塩",
    "kana": "しお",
    "mean": "Muối",
    "accepted": []
  },
  {
    "id": "official-4-3",
    "word": "全て",
    "kana": "すべて",
    "mean": "Tất cả (lịch sự)",
    "accepted": []
  },
  {
    "id": "official-4-4",
    "word": "全然",
    "kana": "ぜんぜん",
    "mean": "Hoàn toàn (không)",
    "accepted": []
  },
  {
    "id": "official-4-5",
    "word": "全部",
    "kana": "ぜんぶ",
    "mean": "Tất cả, toàn bộ",
    "accepted": []
  },
  {
    "id": "official-4-6",
    "word": "安全",
    "kana": "あんぜん",
    "mean": "An toàn",
    "accepted": []
  },
  {
    "id": "official-4-7",
    "word": "熱い",
    "kana": "あつい",
    "mean": "Nóng",
    "accepted": []
  },
  {
    "id": "official-4-8",
    "word": "苦い",
    "kana": "にがい",
    "mean": "Đắng",
    "accepted": []
  },
  {
    "id": "official-4-9",
    "word": "苦しい",
    "kana": "くるしい",
    "mean": "Đau khổ, khó khăn",
    "accepted": []
  },
  {
    "id": "official-4-10",
    "word": "苦手",
    "kana": "にがて",
    "mean": "Kém, yếu, không hợp, sợ",
    "accepted": []
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
if (typeof SENTENCE_PRACTICE_DATA !== "undefined") window.SENTENCE_PRACTICE_DATA = SENTENCE_PRACTICE_DATA;
if (typeof KANJI_PRACTICE_DATA !== "undefined") window.KANJI_PRACTICE_DATA = KANJI_PRACTICE_DATA;
