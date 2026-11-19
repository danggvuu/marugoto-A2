/* Marugoto A2-2 Bài 10 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "ケーキ",
    "kana": "ケーキ",
    "kanji": "ケーキ",
    "romaji": "keeki",
    "vi": "Bánh gato, bánh kem sinh nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c8ec8e5c9fed181f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c8ec8e5c9fed181f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎂</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "チョコレート",
    "kana": "チョコレート",
    "kanji": "チョコレート",
    "romaji": "chokoreeto",
    "vi": "Sô-cô-la",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bba532a9d5074188\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bba532a9d5074188)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍫</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "フルーツ",
    "kana": "フルーツ",
    "kanji": "フルーツ",
    "romaji": "furuutsu",
    "vi": "Trái cây hoa quả",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c234ac35001d17f0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c234ac35001d17f0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍓</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "いちご",
    "kana": "いちご",
    "kanji": "いちご",
    "romaji": "ichigo",
    "vi": "Quả dâu tây",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6eaebaebc2b71d88\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6eaebaebc2b71d88)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍓</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "クリーム",
    "kana": "クリーム",
    "kanji": "クリーム",
    "romaji": "kuriimu",
    "vi": "Kem tươi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_44737e228901a782\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_44737e228901a782)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧁</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "メッセージ",
    "kana": "メッセージ",
    "kanji": "メッセージ",
    "romaji": "messeoji",
    "vi": "Lời nhắn chúc mừng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1c03f351e9ed2306\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1c03f351e9ed2306)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💌</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "キャンドル",
    "kana": "キャンドル",
    "kanji": "キャンドル",
    "romaji": "kyandoru",
    "vi": "Cây nến sinh nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d0243641aad8bbc7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d0243641aad8bbc7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕯️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "人数",
    "kana": "にんずう",
    "kanji": "人数",
    "romaji": "ninzuu",
    "vi": "Số lượng người",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_469915b1e7f66be2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_469915b1e7f66be2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👨‍👩‍👧‍👦</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "大きさ",
    "kana": "おおきさ",
    "kanji": "大きさ",
    "romaji": "ookisa",
    "vi": "Kích cỡ, độ lớn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5c1ad18e12112101\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5c1ad18e12112101)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📏</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "配達",
    "kana": "はいたつ",
    "kanji": "配達",
    "romaji": "haitatsu",
    "vi": "Giao hàng tận nơi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2bcd814c6444d270\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2bcd814c6444d270)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚚</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "感謝",
    "kana": "かんしゃ",
    "kanji": "感謝",
    "romaji": "kansha",
    "vi": "Biết ơn, lòng cảm tạ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_898ac1cb5e851ce7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_898ac1cb5e851ce7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙏</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "お礼",
    "kana": "おれい",
    "kanji": "お礼",
    "romaji": "orei",
    "vi": "Lời cảm ơn, quà đáp lễ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_502d54a0110c227f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_502d54a0110c227f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙇</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "手紙",
    "kana": "てがみ",
    "kanji": "手紙",
    "romaji": "tegami",
    "vi": "Bức thư",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b93da57048feb23d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b93da57048feb23d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✉️</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "サプライズ",
    "kana": "サプライズ",
    "kanji": "サプライズ",
    "romaji": "sapuraizu",
    "vi": "Bất ngờ (bữa tiệc bí mật)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a7846af91af6d62f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a7846af91af6d62f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "びっくりする",
    "kana": "びっくりする",
    "kanji": "びっくりする",
    "romaji": "bikkurisuru",
    "vi": "Giật mình ngạc nhiên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5e5582eb36753ca8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5e5582eb36753ca8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😲</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "笑顔",
    "kana": "えがお",
    "kanji": "笑顔",
    "romaji": "egao",
    "vi": "Nụ cười rạng rỡ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8048f1e2678e5e36\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8048f1e2678e5e36)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😄</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "迎える",
    "kana": "むかえる",
    "kanji": "迎える",
    "romaji": "mukaeru",
    "vi": "Đón nhận, chào đón",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_255866473ae7b99b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_255866473ae7b99b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤗</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "決める",
    "kana": "きめる",
    "kanji": "決める",
    "romaji": "kimeru",
    "vi": "Quyết định chọn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5d2d8ce513992ae7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5d2d8ce513992ae7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✔️</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "届ける",
    "kana": "とどける",
    "kanji": "届ける",
    "romaji": "todokeru",
    "vi": "Giao tới, chuyển đến",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e58fb9b4e9935d19\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e58fb9b4e9935d19)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 10 (A2-2)",
    "jp": "喜ぶ",
    "kana": "よろこぶ",
    "kanji": "喜ぶ",
    "romaji": "yorokobu",
    "vi": "Hân hoan đón mừng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bfc26564203da1c3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bfc26564203da1c3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✨</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "きめます",
    "vi": "Quyết định",
    "te": "きめて",
    "form1": "にきめました (đã quyết định chọn N)",
    "form2": "きめてください",
    "form3": "きめる"
  },
  {
    "masu": "とどけます",
    "vi": "Giao đến nơi",
    "te": "とどけて",
    "form1": "とどけてくれます (giao tới cho mình)",
    "form2": "とどけた",
    "form3": "とどける"
  },
  {
    "masu": "きてくれます",
    "vi": "Đến vì mình",
    "te": "きてくれて",
    "form1": "きてくれてありがとう (cảm ơn bạn đã đến)",
    "form2": "きてくれた",
    "form3": "きてくれる"
  },
  {
    "masu": "てつだいます",
    "vi": "Giúp đỡ",
    "te": "てつだって",
    "form1": "てつだってくれてありがとう (cảm ơn đã giúp)",
    "form2": "てつだった",
    "form3": "てつだう"
  },
  {
    "masu": "かんしゃします",
    "vi": "Biết ơn",
    "te": "かんしゃして",
    "form1": "かんしゃしています",
    "form2": "かんしゃした",
    "form3": "かんしゃする"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "パーティーに [____] くれて、本当に ありがとうございました。",
    "options": [
      "行きて",
      "来て",
      "来たら",
      "来る"
    ],
    "correct": 1,
    "explain": "Cảm ơn vì đã đến tham gia: 来ます ➔ thể TE là 「来て (きて)」 ＋ くれてありがとう."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "いろいろ 準備を [____] くれて ありがとう。とても 助かったよ。",
    "options": [
      "手伝う",
      "手伝った",
      "手伝い",
      "手伝って"
    ],
    "correct": 3,
    "explain": "Cảm ơn vì đã giúp đỡ: 手伝います ➔ thể TE là 「手伝って」."
  },
  {
    "id": 3,
    "category": "Ngữ pháp",
    "q": "ケーキの 種類は いちごの ショートケーキ [____] します。",
    "options": [
      "を",
      "で",
      "に",
      "が"
    ],
    "correct": 2,
    "explain": "Mẫu câu quyết định lựa chọn: 『N に します』."
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
    "q": "Chữ Hán 「手紙」 có nghĩa là gì?",
    "options": [
      "Tờ giấy",
      "Bàn tay",
      "Bức thư",
      "Quyển sách"
    ],
    "correct": 2,
    "explain": "手紙 (てがみ - THỦ CHỈ) có nghĩa là bức thư."
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
    "q": "Từ 「配達」 có âm Hán Việt là gì?",
    "options": [
      "PHỐI HỢP",
      "XUẤT ĐẠT",
      "THÔNG ĐẠT",
      "PHỐI ĐẠT"
    ],
    "correct": 3,
    "explain": "配達 có âm Hán Việt là PHỐI ĐẠT (giao hàng tận nơi)."
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
    "q": "Chữ Hán 「お礼」 đọc là gì?",
    "options": [
      "おらい",
      "おさつ",
      "おれい",
      "おぎ"
    ],
    "correct": 2,
    "explain": "お礼 đọc là 「おれい」 (lời cảm ơn / quà đáp lễ)."
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
    "q": "Từ 「感謝」 gồm 2 chữ nào ghép lại?",
    "options": [
      "CẢM + TÌNH",
      "CẢM + TẠ",
      "CẢM + TÂM",
      "ÁI + TẠ"
    ],
    "correct": 1,
    "explain": "感謝 gồm CẢM (感) và TẠ (謝) ➔ cảm tạ, lòng biết ơn."
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
    "q": "すてきな プレゼントを [____] くれて、本当に うれしいです。",
    "options": [
      "えらんで",
      "えらんだ",
      "えらぶ",
      "えらび"
    ],
    "correct": 0,
    "explain": "Đã cất công chọn quà tặng mình: 選んでくれて (thể TE ＋ くれて)."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「人数」 đọc là gì?",
    "options": [
      "ひとすう",
      "にんずう",
      "じんずう",
      "にんすう"
    ],
    "correct": 1,
    "explain": "人数 đọc là 「にんずう」."
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
