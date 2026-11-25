/* Marugoto A2-2 Bài 10 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "秋祭り",
    "kana": "あきまつり",
    "kanji": "秋祭り",
    "romaji": "akimatsuri",
    "vi": "Lễ hội mùa thu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b6bb4617a8c55a67\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b6bb4617a8c55a67)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍁</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "行事",
    "kana": "ぎょうじ",
    "kanji": "行事",
    "romaji": "gyouji",
    "vi": "Sự kiện, hội",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2a65f107a766ed10\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2a65f107a766ed10)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎏</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "豆まき（します）",
    "kana": "まめまき（します）",
    "kanji": "豆まき（します）",
    "romaji": "mamemaki(shimasu)",
    "vi": "Lễ hội ném đậu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ba9adb6f0baab664\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ba9adb6f0baab664)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👹</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "ひな祭り",
    "kana": "ひなまつり",
    "kanji": "ひな祭り",
    "romaji": "hinamatsuri",
    "vi": "Lễ hội dành cho bé gái ở Nhật Bản",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_49601586b851ee36\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_49601586b851ee36)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎎</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "こいのぼり",
    "kana": "こいのぼり",
    "kanji": "鯉のぼり",
    "romaji": "koinobori",
    "vi": "Cờ cá chép",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_151a36c3977cc19a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_151a36c3977cc19a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎏</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "七夕飾り",
    "kana": "たなばたかざり",
    "kanji": "七夕飾り",
    "romaji": "tanabata kazari",
    "vi": "Ngày lễ Thất tịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_59497610686b8607\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_59497610686b8607)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎋</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "千歳飴",
    "kana": "ちとせあめ",
    "kanji": "千歳飴",
    "romaji": "chitoseame",
    "vi": "Kẹo dùng trong lễ hội Shichi-Go-San cho trẻ em",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dd8e9b4b6a767002\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dd8e9b4b6a767002)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍬</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "飴",
    "kana": "あめ",
    "kanji": "飴",
    "romaji": "ame",
    "vi": "Kẹo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8cf225db87063848\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8cf225db87063848)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍬</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "豆",
    "kana": "まめ",
    "kanji": "豆",
    "romaji": "mame",
    "vi": "Đậu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b7ef4256491352c1\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b7ef4256491352c1)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🫘</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "星",
    "kana": "ほし",
    "kanji": "星",
    "romaji": "hoshi",
    "vi": "Sao",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2c58bff1638b77ce\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2c58bff1638b77ce)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⭐</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "鬼",
    "kana": "おに",
    "kanji": "鬼",
    "romaji": "oni",
    "vi": "Quỷ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_861c66fbc28ebdaf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_861c66fbc28ebdaf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👹</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "豊作",
    "kana": "ほうさく",
    "kanji": "豊作",
    "romaji": "housaku",
    "vi": "Mùa màng bội thu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fc67818eb58427a3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fc67818eb58427a3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌾</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "長生き",
    "kana": "ながいき",
    "kanji": "長生き",
    "romaji": "nagaiki",
    "vi": "Sống lâu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c0bd41dfbe8bc10f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c0bd41dfbe8bc10f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👴</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "幸せ",
    "kana": "しあわせ",
    "kanji": "幸せ",
    "romaji": "shiawase",
    "vi": "Hạnh phúc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8866b7cf3467876b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8866b7cf3467876b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍀</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "願い事",
    "kana": "ねがいごと",
    "kanji": "願い事",
    "romaji": "negaigoto",
    "vi": "Điều mong muốn, mong ước, điều ước",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_76e54eeb666e43c5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_76e54eeb666e43c5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌟</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "けが（をします）",
    "kana": "けが（をします）",
    "kanji": "怪我（をします）",
    "romaji": "kega(o shimasu)",
    "vi": "Vết thương (Bị thương)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e0f8980304dfb278\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e0f8980304dfb278)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🩹</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "投げます",
    "kana": "なげます",
    "kanji": "投げます",
    "romaji": "nagemasu",
    "vi": "Ném",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7c9fc31a29f9a645\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7c9fc31a29f9a645)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎯</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "祈ります",
    "kana": "いのります",
    "kanji": "祈ります",
    "romaji": "inorimasu",
    "vi": "Chúc, cầu nguyện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_35a003f7232a03fc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_35a003f7232a03fc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙏</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "祝います",
    "kana": "いわいます",
    "kanji": "祝います",
    "romaji": "iwaimasu",
    "vi": "Chúc mừng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d5aaf3eb5a0fd696\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d5aaf3eb5a0fd696)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "成長します",
    "kana": "せいちょうします",
    "kanji": "成長します",
    "romaji": "seichou shimasu",
    "vi": "Trưởng thành",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8c14d769e0ecd141\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8c14d769e0ecd141)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌱</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "感謝します",
    "kana": "かんしゃします",
    "kanji": "感謝します",
    "romaji": "kansha shimasu",
    "vi": "Cảm ơn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dda1b23e1220e69f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dda1b23e1220e69f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💐</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "収穫します",
    "kana": "しゅうかくします",
    "kanji": "収穫します",
    "romaji": "shuukaku shimasu",
    "vi": "Thu hoạch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cd6d3bfe6226b8b8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cd6d3bfe6226b8b8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍇</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "うまく行きます",
    "kana": "うまく・いきます",
    "kanji": "うまく行きます",
    "romaji": "umaku ikimasu",
    "vi": "Thuận lợi, suôn sẻ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d1a7200d6369e6c3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d1a7200d6369e6c3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  },
  {
    "id": 24,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "起こります",
    "kana": "おこります",
    "kanji": "起こります",
    "romaji": "okorimasu",
    "vi": "N xảy ra (Nが起こります)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bcf3946563834181\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bcf3946563834181)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚡</text>\n</svg>"
  },
  {
    "id": 25,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "出会います",
    "kana": "であいます",
    "kanji": "出会います",
    "romaji": "deaimasu",
    "vi": "Gặp gỡ (tình cờ, định mệnh)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ca5b7e19f9ef331f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ca5b7e19f9ef331f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👫</text>\n</svg>"
  },
  {
    "id": 26,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "困ります",
    "kana": "こまります",
    "kanji": "困ります",
    "romaji": "komarimasu",
    "vi": "Gặp khó khăn, vất vả, khó xử...",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6b540d4bcb176b00\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6b540d4bcb176b00)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😰</text>\n</svg>"
  },
  {
    "id": 27,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "合格します",
    "kana": "ごうかくします",
    "kanji": "合格します",
    "romaji": "goukaku shimasu",
    "vi": "Thi đỗ kỳ thi (試験に合格します)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b02b8cb0b97bd63d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b02b8cb0b97bd63d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💮</text>\n</svg>"
  },
  {
    "id": 28,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "落ちます",
    "kana": "おちます",
    "kanji": "落ちます",
    "romaji": "ochimasu",
    "vi": "Thi trượt (試験に落ちます)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d3f4164e4d5e4733\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d3f4164e4d5e4733)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍂</text>\n</svg>"
  },
  {
    "id": 29,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "給料",
    "kana": "きゅうりょう",
    "kanji": "給料",
    "romaji": "kyuuryou",
    "vi": "Lương",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_33e4acef55a92c83\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_33e4acef55a92c83)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💵</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "きめます",
    "vi": "Quyết định",
    "te": "きめて",
    "form1": "にきめました (đã quyết định chọn N)",
    "form2": "きめてください",
    "form3": "きめる",
    "form2Label": "Yêu cầu: Vてください"
  },
  {
    "masu": "とどけます",
    "vi": "Giao đến nơi",
    "te": "とどけて",
    "form1": "とどけてくれます (giao tới cho mình)",
    "form2": "とどけた",
    "form3": "とどける",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "きてくれます",
    "vi": "Đến vì mình",
    "te": "きてくれて",
    "form1": "きてくれてありがとう (cảm ơn bạn đã đến)",
    "form2": "きてくれた",
    "form3": "きてくれる",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "てつだいます",
    "vi": "Giúp đỡ",
    "te": "てつだって",
    "form1": "てつだってくれてありがとう (cảm ơn đã giúp)",
    "form2": "てつだった",
    "form3": "てつだう",
    "form2Label": "Thể quá khứ ngắn: Vた"
  },
  {
    "masu": "かんしゃします",
    "vi": "Biết ơn",
    "te": "かんしゃして",
    "form1": "かんしゃしています",
    "form2": "かんしゃした",
    "form3": "かんしゃする",
    "form2Label": "Thể quá khứ ngắn: Vた"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "若い人が楽しめる [____]、イベントがあります。",
    "options": [
      "ので",
      "ように",
      "なら",
      "まで"
    ],
    "correct": 1,
    "explain": "V khả năng + ように nêu mục đích/kết quả mong muốn.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "七夕のとき、願い事を書いたり [____]、楽しみます。",
    "options": [
      "する",
      "した",
      "しない",
      "して"
    ],
    "correct": 3,
    "explain": "Liệt kê ví dụ: Vたりして楽しみます.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "いいことがある [____] 願います。",
    "options": [
      "ので",
      "しか",
      "ように",
      "まで"
    ],
    "correct": 2,
    "explain": "Vるように願う diễn tả điều mong ước.",
    "grammarScope": "official"
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "ケーキの 上に のせる 赤くて 甘酸っぱい 果物は [____] です。",
    "options": [
      "いちご",
      "チョコレート",
      "キャンドル",
      "メッセージ"
    ],
    "correct": 0,
    "explain": "Quả dâu tây phủ trên bánh kem là 「いちご」."
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「幸せ」 có nghĩa là gì?",
    "options": [
      "Sự trưởng thành, phát triển",
      "Sống lâu",
      "Hạnh phúc",
      "Điều ước"
    ],
    "correct": 2,
    "explain": "幸せ nghĩa là Hạnh phúc.",
    "scopeKanji": "幸せ"
  },
  {
    "id": 6,
    "category": "Hội thoại",
    "q": "内緒（ないしょ）で 準備して 相手を 驚かせる 計画を 「[____] パーティー」 と 言います。",
    "options": [
      "メッセージ",
      "キャンドル",
      "サプライズ",
      "チョコレート"
    ],
    "correct": 2,
    "explain": "Bữa tiệc bất ngờ tạo ngạc nhiên là 「サプライズ (surprise)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「成長」 có nghĩa là gì?",
    "options": [
      "Sống lâu",
      "Điều ước",
      "Thi đỗ",
      "Sự trưởng thành, phát triển"
    ],
    "correct": 3,
    "explain": "成長 nghĩa là Sự trưởng thành, phát triển.",
    "scopeKanji": "成長"
  },
  {
    "id": 8,
    "category": "Từ vựng",
    "q": "誕生日ケーキの 上に 立てて 火を つける ろうそくは [____] です。",
    "options": [
      "キャンドル",
      "クリーム",
      "フルーツ",
      "ケーキ"
    ],
    "correct": 0,
    "explain": "Nến cắm bánh sinh nhật là 「キャンドル (candle)」."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「長生き」 có nghĩa là gì?",
    "options": [
      "Điều ước",
      "Thi đỗ",
      "Sống lâu",
      "Kỳ thi"
    ],
    "correct": 2,
    "explain": "長生き nghĩa là Sống lâu.",
    "scopeKanji": "長生き"
  },
  {
    "id": 10,
    "category": "Hội thoại",
    "q": "「どんな ケーキが いいですか。」 ―― 「チョコレートの ケーキが [____] です。」",
    "options": [
      "いい",
      "よくない",
      "いく",
      "よく"
    ],
    "correct": 0,
    "explain": "Bày tỏ loại mình thích: 「～がいいです」 (loại đó được/thích loại đó)."
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "ケーキの プレートに 「お誕生日 おめでとう」 と チョコペンで [____] を 書きます。",
    "options": [
      "てがみ",
      "メッセージ",
      "にんずう",
      "えがお"
    ],
    "correct": 1,
    "explain": "Lời nhắn chúc mừng ghi trên socola là 「メッセージ (message)」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「願い事」 có cách đọc nào?",
    "options": [
      "ごうかく",
      "ねがいごと",
      "しけん",
      "おとな"
    ],
    "correct": 1,
    "explain": "願い事 đọc là 「ねがいごと」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "願い事"
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "パーティーの 参加者の [____] は 何人ですか。",
    "options": [
      "おおきさ",
      "えがお",
      "おれい",
      "にんずう"
    ],
    "correct": 3,
    "explain": "Số lượng người tham gia: 「人数 (にんずう)」."
  },
  {
    "id": 14,
    "category": "Ngữ pháp",
    "q": "パーティーの時間におくれない [____]、早く行きましょう。",
    "options": [
      "ように",
      "ので",
      "なら",
      "まで"
    ],
    "correct": 0,
    "explain": "Vないように nêu điều cần tránh để đạt mục đích.",
    "grammarScope": "official"
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「合格」 có nghĩa là gì?",
    "options": [
      "Kỳ thi",
      "Thi đỗ",
      "Người lớn",
      "Lễ ～ (lễ trưởng thành)"
    ],
    "correct": 1,
    "explain": "合格 nghĩa là Thi đỗ.",
    "scopeKanji": "合格"
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
