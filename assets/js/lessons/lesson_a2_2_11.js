/* Marugoto A2-2 Bài 11 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
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
    "id": 2,
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
    "id": 3,
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
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "電子レンジ",
    "kana": "でんしレンジ",
    "kanji": "電子レンジ",
    "romaji": "denshirenji",
    "vi": "Lò vi sóng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_941cac7563a4ea39\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_941cac7563a4ea39)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📻</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "パソコン",
    "kana": "パソコン",
    "kanji": "パソコン",
    "romaji": "pasokon",
    "vi": "Máy vi tính",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dbd615e26875e0b2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dbd615e26875e0b2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💻</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "壊れる",
    "kana": "こわれる",
    "kanji": "壊れる",
    "romaji": "kowareru",
    "vi": "Bị hỏng (tự động từ)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_434ed7ba3627b0cf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_434ed7ba3627b0cf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💥</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "動く",
    "kana": "うごく",
    "kanji": "動く",
    "romaji": "ugoku",
    "vi": "Hoạt động, chạy máy",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f0358490cbdbb810\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f0358490cbdbb810)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚙️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "調子",
    "kana": "ちょうし",
    "kanji": "調子",
    "romaji": "choushi",
    "vi": "Tình trạng máy móc / sức khỏe",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a7bd67ceeb3acc22\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a7bd67ceeb3acc22)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📊</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "故障",
    "kana": "こしょう",
    "kanji": "故障",
    "romaji": "koshou",
    "vi": "Sự cố, hỏng hóc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e61f226d6c6390d7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e61f226d6c6390d7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚠️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "修理",
    "kana": "しゅうり",
    "kanji": "修理",
    "romaji": "shuuri",
    "vi": "Sửa chữa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b7bf84fe7a7d65c6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b7bf84fe7a7d65c6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔧</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "保証書",
    "kana": "ほしょうしょ",
    "kanji": "保証書",
    "romaji": "hoshousho",
    "vi": "Giấy bảo hành",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4be9c45df4a0c5a2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4be9c45df4a0c5a2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "ネット通販",
    "kana": "ネットつうはん",
    "kanji": "ネット通販",
    "romaji": "netto tsuuhan",
    "vi": "Mua hàng online / thương mại điện tử",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_37a979a1cd9cfcd9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_37a979a1cd9cfcd9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛒</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "注文する",
    "kana": "ちゅうもんする",
    "kanji": "注文する",
    "romaji": "chuumonsuru",
    "vi": "Đặt hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_00f587e012696dd5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_00f587e012696dd5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "届く",
    "kana": "とどく",
    "kanji": "届く",
    "romaji": "todoku",
    "vi": "Được giao tới nơi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3e1e50dd270367bf\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3e1e50dd270367bf)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚚</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "返品",
    "kana": "へんぴん",
    "kanji": "返品",
    "romaji": "henpin",
    "vi": "Trả lại hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8c4e12470ecc7177\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8c4e12470ecc7177)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">↩️</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "交換",
    "kana": "こうかん",
    "kanji": "交換",
    "romaji": "koukan",
    "vi": "Đổi hàng khác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3070bad8c7858b1f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3070bad8c7858b1f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "不便（な）",
    "kana": "ふべん（な）",
    "kanji": "不便（な）",
    "romaji": "fuben(na)",
    "vi": "Bất tiện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b06b56a8e07d9c34\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b06b56a8e07d9c34)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😣</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "困る",
    "kana": "こまる",
    "kanji": "困る",
    "romaji": "komaru",
    "vi": "Khó xử, gặp rắc rối",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_709c8349ccf46248\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_709c8349ccf46248)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😰</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "問い合わせ",
    "kana": "といあわせ",
    "kanji": "問い合わせ",
    "romaji": "toiawase",
    "vi": "Liên hệ hỗ trợ, thắc mắc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d8671382f0c0d5be\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d8671382f0c0d5be)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📞</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 11 (A2-2)",
    "jp": "変な音",
    "kana": "へんなおと",
    "kanji": "変な音",
    "romaji": "hen na oto",
    "vi": "Tiếng kêu lạ, âm thanh bất thường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f8e0c70c81ccbe32\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f8e0c70c81ccbe32)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔊</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "こわれます",
    "vi": "Bị hỏng",
    "te": "こわれて",
    "form1": "こわれてしまった (lỡ hỏng mất rồi)",
    "form2": "こわれたんです (bị hỏng đấy ạ)",
    "form3": "こわれる"
  },
  {
    "masu": "うごきます",
    "vi": "Chạy / hoạt động",
    "te": "うごいて",
    "form1": "うごかなくなりました (không chạy nữa)",
    "form2": "うごかないんです",
    "form3": "うごく"
  },
  {
    "masu": "なおします",
    "vi": "Sửa chữa",
    "te": "なおして",
    "form1": "なおしてください (hãy sửa giúp)",
    "form2": "なおした",
    "form3": "なおす"
  },
  {
    "masu": "とどきます",
    "vi": "Hàng tới",
    "te": "とどいて",
    "form1": "もうとどきました (đã giao tới rồi)",
    "form2": "まだとどいていません",
    "form3": "とどく"
  },
  {
    "masu": "こまります",
    "vi": "Khó khăn / rắc rối",
    "te": "こまって",
    "form1": "こまっているんです (tôi đang rất khó xử)",
    "form2": "こまった",
    "form3": "こまる"
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
