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
    "form3": "つける (thể từ điển)"
  },
  {
    "masu": "やきます",
    "vi": "Nướng",
    "te": "やいて",
    "form1": "やかないで (đừng nướng quá chín)",
    "form2": "やいた (đã nướng)",
    "form3": "やく"
  },
  {
    "masu": "にます",
    "vi": "Ninh / hầm",
    "te": "にて",
    "form1": "にないで",
    "form2": "にた",
    "form3": "にる"
  },
  {
    "masu": "かけます",
    "vi": "Rưới lên",
    "te": "かけて",
    "form1": "かけないで (đừng rưới lên)",
    "form2": "かけた",
    "form3": "かける"
  },
  {
    "masu": "のこします",
    "vi": "Để thừa",
    "te": "のこして",
    "form1": "のこさないで (xin đừng để thừa)",
    "form2": "のこした",
    "form3": "のこす"
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
      "ぜんぶ",
      "ごはん",
      "あんぜん"
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
      "Tất cả, toàn bộ",
      "An toàn",
      "Nóng"
    ],
    "correct": 0,
    "explain": "塩 nghĩa là Muối.",
    "scopeKanji": "塩"
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「全部」 có cách đọc nào?",
    "options": [
      "すべて",
      "ぜんぜん",
      "ぜんぶ",
      "あつい"
    ],
    "correct": 2,
    "explain": "全部 đọc là 「ぜんぶ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "全部"
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
    "q": "Từ Kanji 「苦手」 có nghĩa là gì?",
    "options": [
      "Muối",
      "An toàn",
      "Nóng",
      "Kém, yếu, không hợp, sợ"
    ],
    "correct": 3,
    "explain": "苦手 nghĩa là Kém, yếu, không hợp, sợ.",
    "scopeKanji": "苦手"
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
