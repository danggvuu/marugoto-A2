/* Marugoto A2-2 Bài 14 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "文化財",
    "kana": "ぶんかざい",
    "kanji": "文化財",
    "romaji": "bunkazai",
    "vi": "Di sản văn hóa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1743179165c445f5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1743179165c445f5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏯</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "国宝",
    "kana": "こくほう",
    "kanji": "国宝",
    "romaji": "kokuhou",
    "vi": "Quốc bảo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cf1a5f4afbbf2280\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cf1a5f4afbbf2280)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👑</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "織物",
    "kana": "おりもの",
    "kanji": "織物",
    "romaji": "orimono",
    "vi": "Vải dệt, đồ dệt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d6d7bafe0a9e7274\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d6d7bafe0a9e7274)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧶</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "道具",
    "kana": "どうぐ",
    "kanji": "道具",
    "romaji": "dougu",
    "vi": "Dụng cụ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_913b1a44d896bd95\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_913b1a44d896bd95)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧰</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "刀",
    "kana": "かたな",
    "kanji": "刀",
    "romaji": "katana",
    "vi": "Thanh đao",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a6708ee1ade4c67b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a6708ee1ade4c67b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚔️</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "焼き物",
    "kana": "やきもの",
    "kanji": "焼き物",
    "romaji": "yakimono",
    "vi": "Đồ gốm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1649b865ae1b53e4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1649b865ae1b53e4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏺</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "昔",
    "kana": "むかし",
    "kanji": "昔",
    "romaji": "mukashi",
    "vi": "Ngày xưa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5be24d7dea8c6560\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5be24d7dea8c6560)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕰️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "書",
    "kana": "しょ",
    "kanji": "書",
    "romaji": "sho",
    "vi": "Sách (văn tự)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_764eb7a81cb794d3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_764eb7a81cb794d3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "字",
    "kana": "じ",
    "kanji": "字",
    "romaji": "ji",
    "vi": "Chữ viết",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_866932abd2abd7a2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_866932abd2abd7a2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✍️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "土の人形",
    "kana": "つちのにんぎょう",
    "kanji": "土の人形",
    "romaji": "tsuchi no ningyou",
    "vi": "Búp bê đất",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_75b0177b0d856bc1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_75b0177b0d856bc1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎎</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "楽器",
    "kana": "がっき",
    "kanji": "楽器",
    "romaji": "gakki",
    "vi": "Nhạc cụ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f192a5b32430f6ef\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f192a5b32430f6ef)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎸</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "やっぱり",
    "kana": "やっぱり",
    "kanji": "やっぱり",
    "romaji": "yappari",
    "vi": "Quả nhiên là...",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_105b0b9dc572a353\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_105b0b9dc572a353)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "墓",
    "kana": "はか",
    "kanji": "墓",
    "romaji": "haka",
    "vi": "Mộ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7f8cef7704335666\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7f8cef7704335666)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪦</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "詩",
    "kana": "うた",
    "kanji": "詩",
    "romaji": "uta",
    "vi": "Thơ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f10f47e11370c692\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f10f47e11370c692)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "恋",
    "kana": "こい",
    "kanji": "恋",
    "romaji": "koi",
    "vi": "Tình yêu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e94c79197f8a3b45\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e94c79197f8a3b45)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">❤️</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "ヨーロッパ",
    "kana": "ヨーロッパ",
    "kanji": "ヨーロッパ",
    "romaji": "yo-roppa",
    "vi": "Châu Âu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d5bd4c065dc14b5f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d5bd4c065dc14b5f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌍</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "輸出",
    "kana": "ゆしゅつ",
    "kanji": "輸出",
    "romaji": "yushutsu",
    "vi": "Xuất khẩu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9c23e4a7c9b28e28\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9c23e4a7c9b28e28)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚢</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "ペルシャ",
    "kana": "ペルシャ",
    "kanji": "ペルシャ",
    "romaji": "perusha",
    "vi": "Ba Tư",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f3b355978fb0c2af\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f3b355978fb0c2af)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕌</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "じゅうたん",
    "kana": "じゅうたん",
    "kanji": "絨毯",
    "romaji": "juutan",
    "vi": "Tấm thảm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_55f95a7fb9d4ebe0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_55f95a7fb9d4ebe0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧶</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "戦争",
    "kana": "せんそう",
    "kanji": "戦争",
    "romaji": "sensou",
    "vi": "Chiến tranh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_78f49e58fb58c345\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_78f49e58fb58c345)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛡️</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "運びます",
    "kana": "はこびます",
    "kanji": "運びます",
    "romaji": "hakobimasu",
    "vi": "Vận chuyển",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ea49e91e52e9e2fc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ea49e91e52e9e2fc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚚</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "使用（します）",
    "kana": "しよう（します）",
    "kanji": "使用（します）",
    "romaji": "shiyou(shimasu)",
    "vi": "Sử dụng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c016d15ccc6ae53f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c016d15ccc6ae53f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚙️</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "触ります",
    "kana": "さわります",
    "kanji": "触ります",
    "romaji": "sawarimasu",
    "vi": "Chạm, sờ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ba945173f5e7c1a3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ba945173f5e7c1a3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✋</text>\n</svg>"
  },
  {
    "id": 24,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "ルール／規則",
    "kana": "ルール／きそく",
    "kanji": "ルール／規則",
    "romaji": "ru-ru / kisoku",
    "vi": "Quy tắc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ecdad3edc880e1f6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ecdad3edc880e1f6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 25,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "置きます",
    "kana": "おきます",
    "kanji": "置きます",
    "romaji": "okimasu",
    "vi": "Đặt, để",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7861c1ab1c80398a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7861c1ab1c80398a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 26,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "貼ります",
    "kana": "はります",
    "kanji": "貼ります",
    "romaji": "harimasu",
    "vi": "Dán",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_acadb0de99bb27a3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_acadb0de99bb27a3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏷️</text>\n</svg>"
  },
  {
    "id": 27,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "知らせます",
    "kana": "しらせます",
    "kanji": "知らせます",
    "romaji": "shirasemasu",
    "vi": "Thông báo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a9b656f50b4edb64\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a9b656f50b4edb64)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📢</text>\n</svg>"
  },
  {
    "id": 28,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "ポスター",
    "kana": "ポスター",
    "kanji": "ポスター",
    "romaji": "posuta-",
    "vi": "Poster, áp phích",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2a7922e8926c7b01\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2a7922e8926c7b01)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📰</text>\n</svg>"
  },
  {
    "id": 29,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "調べます",
    "kana": "しらべます",
    "kanji": "調べます",
    "romaji": "shirabemasu",
    "vi": "Tìm hiểu, tra cứu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a0afdb13860eaf95\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a0afdb13860eaf95)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔍</text>\n</svg>"
  },
  {
    "id": 30,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "ロッカー",
    "kana": "ロッカー",
    "kanji": "ロッカー",
    "romaji": "rokka-",
    "vi": "Tủ locker",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5160770c5b6b5615\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5160770c5b6b5615)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗄️</text>\n</svg>"
  },
  {
    "id": 31,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 14 (A2-2)",
    "jp": "カレンダー",
    "kana": "カレンダー",
    "kanji": "カレンダー",
    "romaji": "karenda-",
    "vi": "Lịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_be87b3025462ef7e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_be87b3025462ef7e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "たてます",
    "vi": "Xây dựng",
    "te": "たてて",
    "form1": "たてられた (được xây dựng)",
    "form2": "たてた (đã xây)",
    "form3": "たてる"
  },
  {
    "masu": "のこります",
    "vi": "Còn lưu giữ",
    "te": "のこって",
    "form1": "のこっている (đang còn lưu lại)",
    "form2": "のこった",
    "form3": "のこる"
  },
  {
    "masu": "おとずれます",
    "vi": "Ghé thăm",
    "te": "おとずれて",
    "form1": "おとずれるひと (người ghé thăm)",
    "form2": "おとずれた",
    "form3": "おとずれる"
  },
  {
    "masu": "まもります",
    "vi": "Gìn giữ, bảo vệ",
    "te": "まもって",
    "form1": "まもられている (được bảo tồn)",
    "form2": "まもった",
    "form3": "まもる"
  },
  {
    "masu": "つたえます",
    "vi": "Truyền lại",
    "te": "つたえて",
    "form1": "つたえられている (được tương truyền)",
    "form2": "つたえた",
    "form3": "つたえる"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "この絵は日本で一番古いマンガだ [____]。",
    "options": [
      "ようです",
      "ためです",
      "そうです",
      "あります"
    ],
    "correct": 2,
    "explain": "Danh từ + だそうです dẫn lại thông tin nghe được.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "イベントを知らせる [____]、カレンダーを作ります。",
    "options": [
      "ために",
      "ように",
      "ので",
      "まで"
    ],
    "correct": 0,
    "explain": "Vるために nêu mục đích của hành động.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "赤い 鳥居（とりい）が たくさん 並んでいる 神道の 施設は [____] です。",
    "options": [
      "おてら",
      "しろ",
      "ていえん",
      "じんじゃ"
    ],
    "correct": 3,
    "explain": "Đền thần đạo với cổng Torii màu đỏ là 「神社 (じんじゃ)」."
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「飲食」 có cách đọc nào?",
    "options": [
      "きんし",
      "せつめい",
      "どうぐ",
      "いんしょく"
    ],
    "correct": 3,
    "explain": "飲食 đọc là 「いんしょく」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "飲食"
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "秋に なると 木の 葉が 赤や 黄色に 変わる 現象を [____] と 言います。",
    "options": [
      "こうよう",
      "さくら",
      "まつり",
      "ていえん"
    ],
    "correct": 0,
    "explain": "Lá đỏ mùa thu là 「紅葉 (こうよう / もみじ)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「禁止」 có cách đọc nào?",
    "options": [
      "きんし",
      "せつめい",
      "どうぐ",
      "はくぶつかん"
    ],
    "correct": 0,
    "explain": "禁止 đọc là 「きんし」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "禁止"
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "「京都の 街は どうでしたか。」 ―― 「古い 建物が たくさん あって、とても [____] でした。」",
    "options": [
      "すばらしい",
      "すばらしくない",
      "すばらしかった",
      "すばらしく"
    ],
    "correct": 2,
    "explain": "Khen chuyến đi trong quá khứ: tính từ đuôi い ở quá khứ là 「すばらしかった」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「説明」 có cách đọc nào?",
    "options": [
      "どうぐ",
      "せつめい",
      "はくぶつかん",
      "ひつよう"
    ],
    "correct": 1,
    "explain": "説明 đọc là 「せつめい」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "説明"
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "国にとって 非常に 価値が 高い 貴重な 宝物は [____] に 指定されます。",
    "options": [
      "おみやげ",
      "しゃしん",
      "こくほう",
      "ガイド"
    ],
    "correct": 2,
    "explain": "Bảo vật quốc gia là 「国宝 (こくほう)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「道具」 có cách đọc nào?",
    "options": [
      "どうぐ",
      "はくぶつかん",
      "ひつよう",
      "～かい"
    ],
    "correct": 0,
    "explain": "道具 đọc là 「どうぐ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "道具"
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "受付にイベントカレンダーがおいて [____]。",
    "options": [
      "います",
      "あります",
      "します",
      "なります"
    ],
    "correct": 1,
    "explain": "Vてあります diễn tả vật được chuẩn bị/đặt sẵn và trạng thái còn đó.",
    "grammarScope": "official"
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「博物館」 có cách đọc nào?",
    "options": [
      "ひつよう",
      "はくぶつかん",
      "～かい",
      "いんしょく"
    ],
    "correct": 1,
    "explain": "博物館 đọc là 「はくぶつかん」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "博物館"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "観光地を 案内して 説明して くれる 人を [____] と 呼びます。",
    "options": [
      "てんいん",
      "いしゃ",
      "さっか",
      "ガイド"
    ],
    "correct": 3,
    "explain": "Hướng dẫn viên du lịch là 「ガイド (tour guide)」."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「必要」 có cách đọc nào?",
    "options": [
      "～かい",
      "いんしょく",
      "ひつよう",
      "きんし"
    ],
    "correct": 2,
    "explain": "必要 đọc là 「ひつよう」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "必要"
  },
  {
    "id": 15,
    "category": "Hội thoại",
    "q": "「お寺の 庭は [____] で、心が 落ち着きました。」",
    "options": [
      "にぎやか",
      "しずか",
      "べんり",
      "ふべん"
    ],
    "correct": 1,
    "explain": "Khu vườn chùa thanh tịnh yên ả: 「静か (しずか) で」."
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
