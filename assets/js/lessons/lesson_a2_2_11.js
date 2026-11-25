/* Marugoto A2-2 Bài 11 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "商品",
    "kana": "しょうひん",
    "kanji": "商品",
    "romaji": "shouhin",
    "vi": "Sản phẩm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_48f85a5f891fa1fe\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_48f85a5f891fa1fe)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "電気製品",
    "kana": "でんきせいひん",
    "kanji": "電気製品",
    "romaji": "denkiseihin",
    "vi": "Đồ điện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b9babffd85cdb423\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b9babffd85cdb423)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📱</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "掃除機",
    "kana": "そうじき",
    "kanji": "掃除機",
    "romaji": "soujiki",
    "vi": "Máy hút bụi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5828c803ce1c4aaf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5828c803ce1c4aaf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧹</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "冷蔵庫",
    "kana": "れいぞうこ",
    "kanji": "冷蔵庫",
    "romaji": "reizouko",
    "vi": "Tủ lạnh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1d5b57d755b214c2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1d5b57d755b214c2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧊</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "洗濯機",
    "kana": "せんたくき",
    "kanji": "洗濯機",
    "romaji": "sentakuki",
    "vi": "Máy giặt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9eb9780b47a9f18f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9eb9780b47a9f18f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧺</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "音楽プレーヤー",
    "kana": "おんがくプレーヤー",
    "kanji": "音楽プレーヤー",
    "romaji": "ongaku pure-ya-",
    "vi": "Máy phát nhạc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_da203e596d1c5f80\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_da203e596d1c5f80)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📻</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "扇風機",
    "kana": "せんぷうき",
    "kanji": "扇風機",
    "romaji": "senpuuki",
    "vi": "Quạt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b9d3e42384561eb9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b9d3e42384561eb9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪭</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "アイロン",
    "kana": "アイロン",
    "kanji": "アイロン",
    "romaji": "airon",
    "vi": "Bàn là",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3228808ce4032fe9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3228808ce4032fe9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "電子レンジ",
    "kana": "でんしレンジ",
    "kanji": "電子レンジ",
    "romaji": "denshi renji",
    "vi": "Lò vi sóng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_941cac7563a4ea39\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_941cac7563a4ea39)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍲</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "炊飯器",
    "kana": "すいはんき",
    "kanji": "炊飯器",
    "romaji": "suihanki",
    "vi": "Nồi cơm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_48f0d3e4cf8ed7db\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_48f0d3e4cf8ed7db)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍚</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "壊れます",
    "kana": "こわれます",
    "kanji": "壊れます",
    "romaji": "kowaremasu",
    "vi": "Hỏng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fd69bba6b58f8147\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fd69bba6b58f8147)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💥</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "音が出ません",
    "kana": "おとがでません",
    "kanji": "音が出ません",
    "romaji": "oto ga demasen",
    "vi": "Không phát âm thanh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0c5fbf0f8a6a44ed\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0c5fbf0f8a6a44ed)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔇</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "動きません",
    "kana": "うごきません",
    "kanji": "動きません",
    "romaji": "ugokimasen",
    "vi": "Không cử động",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_25fbdf771529e10e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_25fbdf771529e10e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛑</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "調子が悪い",
    "kana": "ちょうしがわるい",
    "kanji": "調子が悪い",
    "romaji": "choushi ga warui",
    "vi": "Tình trạng không tốt, trục trặc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0f5ecec79b27260c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0f5ecec79b27260c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚠️</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "気にしません",
    "kana": "きにしません",
    "kanji": "気にしません",
    "romaji": "ki ni shimasen",
    "vi": "Không để ý, bận tâm đến N",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7e9491f8dcdfe1b0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7e9491f8dcdfe1b0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤷</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "探します",
    "kana": "さがします",
    "kanji": "探します",
    "romaji": "sagashimasu",
    "vi": "Tìm kiếm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_87ae432c9f654c1e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_87ae432c9f654c1e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔍</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "落とします",
    "kana": "おとします",
    "kanji": "落とします",
    "romaji": "otoshimasu",
    "vi": "Đánh rơi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_40d764613812f732\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_40d764613812f732)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📉</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "困ります",
    "kana": "こまります",
    "kanji": "困ります",
    "romaji": "komarimasu",
    "vi": "Khó khăn, rắc rối",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8b01129f3fc81714\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8b01129f3fc81714)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😰</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "調べます",
    "kana": "しらべます",
    "kanji": "調べます",
    "romaji": "shirabemasu",
    "vi": "Tìm hiểu, điều tra",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a058ca75b57e41ba\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a058ca75b57e41ba)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📖</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "比べます",
    "kana": "くらべます",
    "kanji": "比べます",
    "romaji": "kurabemasu",
    "vi": "So sánh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_11591add86f95720\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_11591add86f95720)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚖️</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "届きます",
    "kana": "とどきます",
    "kanji": "届きます",
    "romaji": "todokimasu",
    "vi": "Được giao đến, chuyển đến",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d74ad9c6655cffde\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d74ad9c6655cffde)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "決めます",
    "kana": "きめます",
    "kanji": "決めます",
    "romaji": "kimemasu",
    "vi": "Quyết định",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e1c4eaaac22e9f16\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e1c4eaaac22e9f16)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✅</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "注文します",
    "kana": "ちゅうもんします",
    "kanji": "注文します",
    "romaji": "chuumon shimasu",
    "vi": "Order, đặt hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ea8a53c1d2362166\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ea8a53c1d2362166)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛒</text>\n</svg>"
  },
  {
    "id": 24,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "考えます",
    "kana": "かんがえます",
    "kanji": "考えます",
    "romaji": "kangaemasu",
    "vi": "Suy nghĩ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cb71922a7427a6cd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cb71922a7427a6cd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤔</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "こわれます",
    "vi": "Bị hỏng",
    "te": "こわれて",
    "form1": "こわれてしまった (lỡ hỏng mất rồi)",
    "form2": "こわれたんです (bị hỏng đấy ạ)",
    "form3": "こわれる",
    "form2Label": "Giải thích: thể thông thường + んです"
  },
  {
    "masu": "うごきます",
    "vi": "Chạy / hoạt động",
    "te": "うごいて",
    "form1": "うごかなくなりました (không chạy nữa)",
    "form2": "うごかないんです",
    "form3": "うごく",
    "form2Label": "Giải thích: thể thông thường + んです"
  },
  {
    "masu": "なおします",
    "vi": "Sửa chữa",
    "te": "なおして",
    "form1": "なおしてください (hãy sửa giúp)",
    "form2": "なおした",
    "form3": "なおす",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "とどきます",
    "vi": "Hàng tới",
    "te": "とどいて",
    "form1": "もうとどきました (đã giao tới rồi)",
    "form2": "まだとどいていません",
    "form3": "とどく",
    "form2Label": "Vẫn chưa: まだVていません"
  },
  {
    "masu": "こまります",
    "vi": "Khó khăn / rắc rối",
    "te": "こまって",
    "form1": "こまっているんです (tôi đang rất khó xử)",
    "form2": "こまった",
    "form3": "こまる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "昨日から 冷蔵庫の 調子が 悪くて、[____] しまったんです。",
    "options": [
      "こわれて",
      "こわして",
      "こわれた",
      "こわる"
    ],
    "correct": 0,
    "explain": "Tự động từ bị hỏng: こわれます ➔ thể TE: 「こわれて」 ＋ しまいました.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "ネットショッピングは時間を気に [____] 買い物できます。",
    "options": [
      "しなくて",
      "しない",
      "しなかった",
      "しないで"
    ],
    "correct": 3,
    "explain": "Vないで買い物できます: có thể mua sắm mà không bận tâm thời gian.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "床の ゴミや ホコリを 吸い取る 電化製品は [____] です。",
    "options": [
      "そうじき",
      "せんたくき",
      "れいぞうこ",
      "電子レンジ"
    ],
    "correct": 0,
    "explain": "Máy hút bụi sàn nhà là 「掃除機 (そうじき)」."
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「商品」 có cách đọc nào?",
    "options": [
      "でんきせいひん",
      "しょうひん",
      "でんしレンジ",
      "～き"
    ],
    "correct": 1,
    "explain": "商品 đọc là 「しょうひん」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "商品"
  },
  {
    "id": 5,
    "category": "Ngữ pháp",
    "q": "せんぷう機が [____] なりました。",
    "options": [
      "動かなく",
      "動かないで",
      "動いて",
      "動くまで"
    ],
    "correct": 0,
    "explain": "Vなくなる diễn tả trạng thái không còn hoạt động.",
    "grammarScope": "official"
  },
  {
    "id": 6,
    "category": "Hội thoại",
    "q": "無料で 修理して もらうために、商品と 一緒に [____] を 見せます。",
    "options": [
      "メニュー",
      "ほしょうしょ",
      "手紙",
      "ガイドブック"
    ],
    "correct": 1,
    "explain": "Giấy bảo hành sản phẩm: 「保証書 (ほしょうしょ)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「電気製品」 có nghĩa là gì?",
    "options": [
      "Lò vi sóng",
      "Máy ～ (máy hút bụi)",
      "Nhân viên cửa hàng",
      "Đồ điện, thiết bị điện"
    ],
    "correct": 3,
    "explain": "電気製品 nghĩa là Đồ điện, thiết bị điện.",
    "scopeKanji": "電気製品"
  },
  {
    "id": 8,
    "category": "Từ vựng",
    "q": "服が 汚れたので、[____] で 洗います。",
    "options": [
      "れいぞうこ",
      "そうじき",
      "せんたくき",
      "電子レンジ"
    ],
    "correct": 2,
    "explain": "Giặt quần áo bằng máy giặt: 「洗濯機 (せんたくき)」."
  },
  {
    "id": 9,
    "category": "Ngữ pháp",
    "q": "電子レンジがとどく [____]、1週間かかりました。",
    "options": [
      "しか",
      "そう",
      "なら",
      "まで"
    ],
    "correct": 3,
    "explain": "まで nêu mốc thời gian cho đến khi hàng được giao.",
    "grammarScope": "official"
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「電子レンジ」 có cách đọc nào?",
    "options": [
      "でんしレンジ",
      "～き",
      "てんいん",
      "ちょうし"
    ],
    "correct": 0,
    "explain": "電子レンジ đọc là 「でんしレンジ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "電子レンジ"
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "買った 商品に 傷が あったので、新しい ものに [____] して ください。",
    "options": [
      "しゅうり",
      "へんぴん",
      "こうかん",
      "よやく"
    ],
    "correct": 2,
    "explain": "Đổi sang sản phẩm mới không trầy xước: 「交換 (こうかん) してください」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「～機（そうじ機）」 có cách đọc nào?",
    "options": [
      "てんいん",
      "ちょうし",
      "～き",
      "わるい"
    ],
    "correct": 2,
    "explain": "～機（そうじ機） đọc là 「～き」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "～機（そうじ機）"
  },
  {
    "id": 13,
    "category": "Hội thoại",
    "q": "「どうしたんですか。」 ―― 「パソコンが 急に 動かなくなって、とても [____] んです。」",
    "options": [
      "喜んでいる",
      "困っている",
      "楽しんでいる",
      "休んでいる"
    ],
    "correct": 1,
    "explain": "Máy tính đơ rắc rối khó xử: 「困っているんです (こまっているんです)」."
  },
  {
    "id": 14,
    "category": "Từ vựng",
    "q": "電子レンジから [____] が 聞こえます。火花が 出たら 危険です。",
    "options": [
      "あじ",
      "いろ",
      "へんなおと",
      "におい"
    ],
    "correct": 2,
    "explain": "Tiếng kêu lạ bất thường từ lò vi sóng: 「変な音 (へんなおと)」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「店員」 có nghĩa là gì?",
    "options": [
      "Tình trạng",
      "Nhân viên cửa hàng",
      "Xấu, không tốt",
      "Hoạt động, chạy (máy móc)"
    ],
    "correct": 1,
    "explain": "店員 nghĩa là Nhân viên cửa hàng.",
    "scopeKanji": "店員"
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
