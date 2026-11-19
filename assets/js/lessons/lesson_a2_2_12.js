/* Marugoto A2-2 Bài 12 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "値段",
    "kana": "ねだん",
    "kanji": "値段",
    "romaji": "nedan",
    "vi": "Giá cả, mức giá",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_28bce4a127d7e5c8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_28bce4a127d7e5c8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏷️</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "性能",
    "kana": "せいのう",
    "kanji": "性能",
    "romaji": "seinou",
    "vi": "Tính năng, hiệu suất máy",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_44a3ebd85649db29\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_44a3ebd85649db29)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚡</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "サイズ",
    "kana": "サイズ",
    "kanji": "サイズ",
    "romaji": "saizu",
    "vi": "Kích cỡ size",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_86c8dbfba8121316\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_86c8dbfba8121316)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📐</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "重さ",
    "kana": "おもさ",
    "kanji": "重さ",
    "romaji": "omosa",
    "vi": "Trọng lượng, độ nặng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_73f4cc0437ce25a0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_73f4cc0437ce25a0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚖️</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "軽い",
    "kana": "かるい",
    "kanji": "軽い",
    "romaji": "karui",
    "vi": "Nhẹ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_52e76ce99b3c7d01\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_52e76ce99b3c7d01)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪶</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "重い",
    "kana": "おもい",
    "kanji": "重い",
    "romaji": "omoi",
    "vi": "Nặng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1467c839eb65b59b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1467c839eb65b59b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪨</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "安い",
    "kana": "やすい",
    "kanji": "安い",
    "romaji": "yasui",
    "vi": "Rẻ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_68dd9bdae02e5c3c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_68dd9bdae02e5c3c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💰</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "高い",
    "kana": "たかい",
    "kanji": "高い",
    "romaji": "takai",
    "vi": "Đắt, giá cao",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1e27f40fc5a8ef42\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1e27f40fc5a8ef42)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💎</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "便利（な）",
    "kana": "べんり（な）",
    "kanji": "便利（な）",
    "romaji": "benri(na)",
    "vi": "Tiện lợi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c5cbb98f4006cc92\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c5cbb98f4006cc92)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👍</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "静か（な）",
    "kana": "しずか（な）",
    "kanji": "静か（な）",
    "romaji": "shizuka(na)",
    "vi": "Yên tĩnh, chạy êm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_385a12550da85804\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_385a12550da85804)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤫</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "レビュー",
    "kana": "レビュー",
    "kanji": "レビュー",
    "romaji": "rebyuu",
    "vi": "Đánh giá, review sản phẩm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cddcec750ea2f6ac\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cddcec750ea2f6ac)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⭐</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "口コミ",
    "kana": "くちこみ",
    "kanji": "口コミ",
    "romaji": "kuchikomi",
    "vi": "Nhận xét truyền miệng, đánh giá của khách",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f4ca26333c54304e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f4ca26333c54304e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💬</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "星",
    "kana": "ほし",
    "kanji": "星",
    "romaji": "hoshi",
    "vi": "Ngôi sao xếp hạng (rating)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_debf3141f7edfcae\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_debf3141f7edfcae)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌟</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "評価",
    "kana": "ひょうか",
    "kanji": "評価",
    "romaji": "hyouka",
    "vi": "Sự đánh giá, xếp hạng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_25969063bb82640d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_25969063bb82640d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📊</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "送料無料",
    "kana": "そうりょうむりょう",
    "kanji": "送料無料",
    "romaji": "souryou muryou",
    "vi": "Miễn phí vận chuyển (Freeship)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_399d0b869c723a8e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_399d0b869c723a8e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚚</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "配達日",
    "kana": "はいたつび",
    "kanji": "配達日",
    "romaji": "haitatsubi",
    "vi": "Ngày giao hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0d2ec9507db091e3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0d2ec9507db091e3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📆</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "割引",
    "kana": "わりびき",
    "kanji": "割引",
    "romaji": "waribiki",
    "vi": "Giảm giá, chiết khấu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6e083ddfdb0f5dd0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6e083ddfdb0f5dd0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏷️</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "ポイント",
    "kana": "ポイント",
    "kanji": "ポイント",
    "romaji": "pointo",
    "vi": "Điểm tích lũy mua sắm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_07298b70678122e8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_07298b70678122e8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪙</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "比べる",
    "kana": "くらべる",
    "kanji": "比べる",
    "romaji": "kuraberu",
    "vi": "So sánh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_11591add86f95720\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_11591add86f95720)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔍</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "迷う",
    "kana": "まよう",
    "kanji": "迷う",
    "romaji": "mayou",
    "vi": "Phân vân, đắn đo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_06cf3da82e686e20\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_06cf3da82e686e20)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤔</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "くらべます",
    "vi": "So sánh",
    "te": "くらべて",
    "form1": "くらべてみると (khi thử so sánh)",
    "form2": "くらべた (đã so sánh)",
    "form3": "くらべる"
  },
  {
    "masu": "まよいます",
    "vi": "Phân vân",
    "te": "まよって",
    "form1": "まよっている (đang phân vân)",
    "form2": "まよった (đã đắn đo)",
    "form3": "まよう"
  },
  {
    "masu": "きめます",
    "vi": "Quyết định",
    "te": "きめて",
    "form1": "こちらにします (chọn cái này)",
    "form2": "きめた (đã chốt)",
    "form3": "きめる"
  },
  {
    "masu": "はらいます",
    "vi": "Thanh toán",
    "te": "はらって",
    "form1": "カードではらいます",
    "form2": "はらった",
    "form3": "はらう"
  },
  {
    "masu": "つかいます",
    "vi": "Sử dụng",
    "te": "つかって",
    "form1": "つかいやすい (dễ sử dụng)",
    "form2": "つかいにくい (khó dùng)",
    "form3": "つかう"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "こちらの 掃除機の [____] が、あちらより 軽くて 静かです。",
    "options": [
      "より",
      "ほど",
      "ほう",
      "だけ"
    ],
    "correct": 2,
    "explain": "Cấu trúc so sánh hơn: 『N1 の ほうが N2 より A』 ➔ 「ほう」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "「黒と 白と [____] が いいですか。」 ―― 「白の 方が いいです。」",
    "options": [
      "だれ",
      "どこ",
      "どちら",
      "いつ"
    ],
    "correct": 2,
    "explain": "Hỏi so sánh giữa 2 đối tượng dùng từ để hỏi: 『どちら (どっち)』."
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "実際に 買った 人の 感想や 評価を 書いた 文章は [____] です。",
    "options": [
      "サイズ",
      "ポイント",
      "レビュー",
      "メニュー"
    ],
    "correct": 2,
    "explain": "Đánh giá, bình luận của người mua là 「レビュー (review / 口コミ)」."
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「比べる」 đọc là gì?",
    "options": [
      "ならべる",
      "えらべる",
      "しらべる",
      "くらべる"
    ],
    "correct": 3,
    "explain": "比べる đọc là 「くらべる」 (TỈ - so sánh đối chiếu)."
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "送料（tiền ship）を 払わなくても いい サービスを [____] と 言います。",
    "options": [
      "そうりょうむりょう",
      "わりびき",
      "ねだん",
      "せいほう"
    ],
    "correct": 0,
    "explain": "Freeship không mất tiền vận chuyển là 「送料無料 (そうりょうむりょう)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ trái nghĩa với 「重い (おもい - nặng)」 là từ nào?",
    "options": [
      "軽い (かるい)",
      "安い (やすい)",
      "低い (ひくい)",
      "薄い (うすい)"
    ],
    "correct": 0,
    "explain": "重い (nặng) đối nghĩa với 軽い (nhẹ)."
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "20% [____] の セール中なので、いつもより 安く 買えます。",
    "options": [
      "ねだん",
      "わりびき",
      "ほし",
      "サイズ"
    ],
    "correct": 1,
    "explain": "Giảm giá 20%: 「20% 割引 (わりびき)」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「便利」 có âm Hán Việt là gì?",
    "options": [
      "TIỆN ĐỒ",
      "CÁT LỢI",
      "LỢI DỤNG",
      "TIỆN LỢI"
    ],
    "correct": 3,
    "explain": "便利 có âm Hán Việt là TIỆN LỢI."
  },
  {
    "id": 9,
    "category": "Ngữ pháp",
    "q": "バスより 電車の [____] が 時間が 正確です。",
    "options": [
      "より",
      "ほう",
      "から",
      "まで"
    ],
    "correct": 1,
    "explain": "Tàu điện thì đúng giờ hơn xe buýt: 電車のほうが."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「値段」 đọc là gì?",
    "options": [
      "ちくだん",
      "ねたん",
      "ねだん",
      "ばいだん"
    ],
    "correct": 2,
    "explain": "値段 đọc là 「ねだん」 (TRỊ ĐOẠN - giá tiền)."
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "どちらの 商品を 買うか、なかなか 決められずに [____] います。",
    "options": [
      "まよって",
      "よろこんで",
      "つかれて",
      "こわれて"
    ],
    "correct": 0,
    "explain": "Đang phân vân đắn đo: 迷います ➔ 「迷っています (まよっています)」."
  },
  {
    "id": 12,
    "category": "Hội thoại",
    "q": "「この 掃除機、星 5つの うち [____] 4.8で とても 評判が いいですよ。」",
    "options": [
      "つき",
      "ほし",
      "ひ",
      "みず"
    ],
    "correct": 1,
    "explain": "Xếp hạng đánh giá theo sao: 「星 (ほし)」."
  },
  {
    "id": 13,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「無料」 gồm 2 chữ nào?",
    "options": [
      "VÔ + LÝ",
      "HỮU + LIỆU",
      "VÔ + LƯỢNG",
      "VÔ + LIỆU"
    ],
    "correct": 3,
    "explain": "無料 gồm VÔ (無) và LIỆU (料) ➔ không mất tiền, miễn phí."
  },
  {
    "id": 14,
    "category": "Từ vựng",
    "q": "お買い物で たまった [____] を 使って、割引を 受けました。",
    "options": [
      "レビュー",
      "ポイント",
      "サイズ",
      "メッセージ"
    ],
    "correct": 1,
    "explain": "Điểm thưởng tích lũy mua sắm: 「ポイント (point)」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「割引」 gồm 2 chữ nào?",
    "options": [
      "CÁT + DẪN",
      "LỢI + DẪN",
      "CÁT + DỤNG",
      "CHI + DẪN"
    ],
    "correct": 0,
    "explain": "割引 gồm chữ CÁT (割 - chia cắt) và DẪN (引 - kéo/bớt lại) ➔ giảm giá chiết khấu."
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
