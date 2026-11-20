/* Marugoto A2-2 Bài 17 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "人生",
    "kana": "じんせい",
    "kanji": "人生",
    "romaji": "jinsei",
    "vi": "Cuộc đời, đời người",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a33847611ce0be35\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a33847611ce0be35)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌱</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "俳優",
    "kana": "はいゆう",
    "kanji": "俳優",
    "romaji": "haiyuu",
    "vi": "Diễn viên nam",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_85ae7baf2d543dc5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_85ae7baf2d543dc5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎭</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "女優",
    "kana": "じょゆう",
    "kanji": "女優",
    "romaji": "joyuu",
    "vi": "Diễn viên nữ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_38a97d0594366086\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_38a97d0594366086)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎬</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "音楽家",
    "kana": "おんがくか",
    "kanji": "音楽家",
    "romaji": "ongakuka",
    "vi": "Nhạc sĩ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_06c3143a2ff46f23\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_06c3143a2ff46f23)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎼</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "画家",
    "kana": "がか",
    "kanji": "画家",
    "romaji": "gaka",
    "vi": "Họa sĩ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fbd4af3c12b11564\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fbd4af3c12b11564)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎨</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "作家",
    "kana": "さっか",
    "kanji": "作家",
    "romaji": "sakka",
    "vi": "Nhà văn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b9c48e128cd1960f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b9c48e128cd1960f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🖋️</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "小説家",
    "kana": "しょうせつか",
    "kanji": "小説家",
    "romaji": "shousetsuka",
    "vi": "Tiểu thuyết gia",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bfc19e0249e7cf2f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bfc19e0249e7cf2f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📚</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "スポーツ選手",
    "kana": "スポーツせんしゅ",
    "kanji": "スポーツ選手",
    "romaji": "supo-tsu senshu",
    "vi": "Tuyển thủ thể thao",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5612bcfb71f3160c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5612bcfb71f3160c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚽</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "柔道家",
    "kana": "じゅうどうか",
    "kanji": "柔道家",
    "romaji": "juudouka",
    "vi": "Võ sĩ judo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e37efcc18593078c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e37efcc18593078c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥋</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "映画監督",
    "kana": "えいがかんとく",
    "kanji": "映画監督",
    "romaji": "eiga kantoku",
    "vi": "Đạo diễn phim",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_163b7ce7f2ede070\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_163b7ce7f2ede070)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎥</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "科学者",
    "kana": "かがくしゃ",
    "kanji": "科学者",
    "romaji": "kagakusha",
    "vi": "Nhà khoa học",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c0a392c7f32889a3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c0a392c7f32889a3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔬</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "教育者",
    "kana": "きょういくしゃ",
    "kanji": "教育者",
    "romaji": "kyouikusha",
    "vi": "Nhà giáo dục học",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_494edd09bd84ee96\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_494edd09bd84ee96)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👨‍🏫</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "バイオリニスト",
    "kana": "バイオリニスト",
    "kanji": "バイオリニスト",
    "romaji": "baiorinisuto",
    "vi": "Nghệ sĩ Violin",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0448154b301f5758\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0448154b301f5758)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎻</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "大ファン",
    "kana": "だいファン",
    "kanji": "大ファン",
    "romaji": "dai fan",
    "vi": "Fan bự",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a460570ed30e4fde\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a460570ed30e4fde)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤩</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "金メダル",
    "kana": "きんメダル",
    "kanji": "金メダル",
    "romaji": "kin medaru",
    "vi": "Huy chương vàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_631d12f704fca59c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_631d12f704fca59c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥇</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "～賞",
    "kana": "～しょう",
    "kanji": "～賞",
    "romaji": "~shou",
    "vi": "Giải thưởng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_076217d5d22b01b4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_076217d5d22b01b4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏆</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "翻訳（します）",
    "kana": "ほんやく（します）",
    "kanji": "翻訳（します）",
    "romaji": "honyaku(shimasu)",
    "vi": "Biên dịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_229b130b8efd14fa\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_229b130b8efd14fa)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📝</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "活躍（します）",
    "kana": "かつやく（します）",
    "kanji": "活躍（します）",
    "romaji": "katsuyaku(shimasu)",
    "vi": "Thành công, hoạt động sôi nổi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e035903b37f9530e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e035903b37f9530e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌟</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "亡くなります",
    "kana": "なくなります",
    "kanji": "亡くなります",
    "romaji": "nakunarimasu",
    "vi": "Qua đời",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_93715fae24b615f4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_93715fae24b615f4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕊️</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "作品",
    "kana": "さくひん",
    "kanji": "作品",
    "romaji": "sakuhin",
    "vi": "Tác phẩm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ce289ffd4f39fa05\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ce289ffd4f39fa05)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🖼️</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "太陽",
    "kana": "たいよう",
    "kanji": "太陽",
    "romaji": "taiyou",
    "vi": "Mặt trời",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c8da03f3ffc7ee92\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c8da03f3ffc7ee92)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">☀️</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "呼びます",
    "kana": "よびます",
    "kanji": "呼びます",
    "romaji": "yobimasu",
    "vi": "Gọi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_605b257e75e0f054\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_605b257e75e0f054)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗣️</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "ずっと",
    "kana": "ずっと",
    "kanji": "ずっと",
    "romaji": "zutto",
    "vi": "Suốt, mãi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8fa6593707e6ba4a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8fa6593707e6ba4a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 24,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "辞めます／やめます",
    "kana": "やめます",
    "kanji": "辞めます",
    "romaji": "yamemasu",
    "vi": "Bỏ N, Từ bỏ N",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a911969faa9a5af3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a911969faa9a5af3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛑</text>\n</svg>"
  },
  {
    "id": 25,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "離婚します",
    "kana": "りこんします",
    "kanji": "離婚します",
    "romaji": "rikon shimasu",
    "vi": "Ly hôn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d92e9dfe3dee9433\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d92e9dfe3dee9433)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💔</text>\n</svg>"
  },
  {
    "id": 26,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "びっくりしました",
    "kana": "びっくりしました",
    "kanji": "びっくりしました",
    "romaji": "bikkuri shimashita",
    "vi": "Bất ngờ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c5b69ed8bc625223\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c5b69ed8bc625223)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😲</text>\n</svg>"
  },
  {
    "id": 27,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "貧しい",
    "kana": "まずしい",
    "kanji": "貧しい",
    "romaji": "mazushii",
    "vi": "Nghèo, thiếu thốn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_007d07da44dadbba\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_007d07da44dadbba)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏚️</text>\n</svg>"
  },
  {
    "id": 28,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "苦労します",
    "kana": "くろうします",
    "kanji": "苦労します",
    "romaji": "kurou shimasu",
    "vi": "Gặp khó khăn, vất vả",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bec43b86632b332c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bec43b86632b332c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧗</text>\n</svg>"
  },
  {
    "id": 29,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "首相",
    "kana": "しゅしょう",
    "kanji": "首相",
    "romaji": "shushou",
    "vi": "Thủ tướng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1fd02bc1d3942ae5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1fd02bc1d3942ae5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏛️</text>\n</svg>"
  },
  {
    "id": 30,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "大統領",
    "kana": "だいとうりょう",
    "kanji": "大統領",
    "romaji": "daitouryou",
    "vi": "Tổng thống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_711cc7786c306f3a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_711cc7786c306f3a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🇺🇸</text>\n</svg>"
  },
  {
    "id": 31,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "政治家",
    "kana": "せいじか",
    "kanji": "政治家",
    "romaji": "seijika",
    "vi": "Chính trị gia",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ee0d995f5b3bb93a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ee0d995f5b3bb93a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n</svg>"
  },
  {
    "id": 32,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "実業家",
    "kana": "じつぎょうか",
    "kanji": "実業家",
    "romaji": "jitsugyouka",
    "vi": "Doanh nhân, nhà kinh doanh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3b7f0b32a505d586\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3b7f0b32a505d586)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💼</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "うまれます",
    "vi": "Được sinh ra",
    "te": "うまれて",
    "form1": "うまれました (đã sinh ra tại)",
    "form2": "うまれたあとで",
    "form3": "うまれる"
  },
  {
    "masu": "そだちます",
    "vi": "Lớn lên",
    "te": "そだって",
    "form1": "そだちました (đã lớn lên tại)",
    "form2": "そだったところ",
    "form3": "そだつ"
  },
  {
    "masu": "せいこうします",
    "vi": "Thành công",
    "te": "せいこうして",
    "form1": "せいこうした (đã thành công)",
    "form2": "せいこうするまで",
    "form3": "せいこうする"
  },
  {
    "masu": "どりょくします",
    "vi": "Nỗ lực",
    "te": "どりょくして",
    "form1": "どりょくをつづけた (tiếp tục nỗ lực)",
    "form2": "どりょくした",
    "form3": "どりょくする"
  },
  {
    "masu": "かつやくします",
    "vi": "Hoạt động tích cực",
    "te": "かつやくして",
    "form1": "かつやくしています",
    "form2": "かつやくした",
    "form3": "かつやくする"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "この歌手は2回目の結婚をする [____] です。",
    "options": [
      "よう",
      "まで",
      "そう",
      "しか"
    ],
    "correct": 2,
    "explain": "普通形 + そうです dẫn lại thông tin nghe được.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "この人は画家になって [____]、フランスに行きました。",
    "options": [
      "から",
      "まで",
      "そう",
      "しか"
    ],
    "correct": 0,
    "explain": "Vてから nêu hành động xảy ra sau khi trở thành họa sĩ.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "画家はなくなる [____]、フランスで絵をかきました。",
    "options": [
      "から",
      "そう",
      "しか",
      "まで"
    ],
    "correct": 3,
    "explain": "まで nêu mốc cuối cùng của hành động.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "この画家は一番有名 [____] しれません。",
    "options": [
      "ので",
      "まで",
      "しか",
      "かも"
    ],
    "correct": 3,
    "explain": "かもしれません diễn tả phỏng đoán chưa chắc chắn.",
    "grammarScope": "official"
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "あきらめずに 毎日 こつこつと [____] した 結果、夢が かないました。",
    "options": [
      "しっぱい",
      "せいこう",
      "かつやく",
      "どりょく"
    ],
    "correct": 3,
    "explain": "Nỗ lực kiên trì không bỏ cuộc: 「努力 (どりょく) した」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「人生」 có cách đọc nào?",
    "options": [
      "かしゅ",
      "じんせい",
      "せんしゅ",
      "がか"
    ],
    "correct": 1,
    "explain": "人生 đọc là 「じんせい」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "人生"
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "「この 人、[____] か。」 ―― 「ええ、ノーベル賞を 取った 科学者ですね。」",
    "options": [
      "分かりました",
      "知恵があります",
      "知っています",
      "覚えます"
    ],
    "correct": 2,
    "explain": "Hỏi có biết người này không: 「知っていますか」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「歌手」 có cách đọc nào?",
    "options": [
      "せんしゅ",
      "かしゅ",
      "がか",
      "さっか"
    ],
    "correct": 1,
    "explain": "歌手 đọc là 「かしゅ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "歌手"
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "将来 やりたい ことや 目指している 希望は [____] です。",
    "options": [
      "ゆめ",
      "しっぱい",
      "えいきょう",
      "しょうがい"
    ],
    "correct": 0,
    "explain": "Giấc mơ, ước mơ tương lai: 「夢 (ゆめ)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「選手」 có cách đọc nào?",
    "options": [
      "せんしゅ",
      "がか",
      "さっか",
      "にゅうがく"
    ],
    "correct": 0,
    "explain": "選手 đọc là 「せんしゅ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "選手"
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "田中さんは 東京で [____]、京都で 育ちました。",
    "options": [
      "生まれる",
      "生まれ",
      "生まれた",
      "生まれて"
    ],
    "correct": 1,
    "explain": "Liên kết câu dạng văn viết trang trọng: 生まれます ➔ bỏ ます thành 「生まれ」.",
    "grammarScope": "official"
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「画家」 có cách đọc nào?",
    "options": [
      "さっか",
      "にゅうがく",
      "がか",
      "そつぎょう"
    ],
    "correct": 2,
    "explain": "画家 đọc là 「がか」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "画家"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "国際的な 大会で 優勝して、金メダルの [____] を もらいました。",
    "options": [
      "ゆめ",
      "じんせい",
      "しょう",
      "さくひん"
    ],
    "correct": 2,
    "explain": "Nhận phần thưởng, huy chương: 「賞 (しょう)」."
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "子どもの 頃に 読んだ 本から、とても 大きな [____] を 受けました。",
    "options": [
      "えいきょう",
      "しっぱい",
      "どりょく",
      "しょうがい"
    ],
    "correct": 0,
    "explain": "Nhận được tầm ảnh hưởng lớn lao: 「影響 (えいきょう) を受けました」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「作家」 có nghĩa là gì?",
    "options": [
      "Nhập học",
      "Nhà văn, tác giả",
      "Tốt nghiệp",
      "Bệnh, ốm"
    ],
    "correct": 1,
    "explain": "作家 nghĩa là Nhà văn, tác giả.",
    "scopeKanji": "作家"
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
