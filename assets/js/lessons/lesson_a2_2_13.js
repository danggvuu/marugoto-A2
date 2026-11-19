/* Marugoto A2-2 Bài 13 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "地下鉄",
    "kana": "ちかてつ",
    "kanji": "地下鉄",
    "romaji": "chikatetsu",
    "vi": "Tàu điện ngầm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dd146603a2670dbe\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dd146603a2670dbe)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚇</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "バス",
    "kana": "バス",
    "kanji": "バス",
    "romaji": "basu",
    "vi": "Xe buýt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7c9a54af008f71d2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7c9a54af008f71d2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚌</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "電車",
    "kana": "でんしゃ",
    "kanji": "電車",
    "romaji": "densha",
    "vi": "Tàu điện",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e7e49c1c5165e874\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e7e49c1c5165e874)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚃</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "新幹線",
    "kana": "しんかんせん",
    "kanji": "新幹線",
    "romaji": "shinkansen",
    "vi": "Tàu siêu tốc Shinkansen",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_551be8f12532fb85\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_551be8f12532fb85)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚅</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "切符",
    "kana": "きっぷ",
    "kanji": "切符",
    "romaji": "kippu",
    "vi": "Vé tàu, vé xe",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_08420e293e004adc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_08420e293e004adc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎫</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "ICカード",
    "kana": "アイシーカード",
    "kanji": "ICカード",
    "romaji": "aishiikaado",
    "vi": "Thẻ giao thông thông minh (Suica/Pasmo)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ee05fed65e1a4f09\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ee05fed65e1a4f09)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💳</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "改札口",
    "kana": "かいさつぐち",
    "kanji": "改札口",
    "romaji": "kaisatsuguchi",
    "vi": "Cổng soát vé tự động",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_74d8cdc434d9fd45\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_74d8cdc434d9fd45)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚪</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "乗り換え",
    "kana": "のりかえ",
    "kanji": "乗り換え",
    "romaji": "norikae",
    "vi": "Sự chuyển tuyến, đổi tàu xe",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3d68a656a19f78f6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3d68a656a19f78f6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔀</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "乗る",
    "kana": "のる",
    "kanji": "乗る",
    "romaji": "noru",
    "vi": "Lên xe, đi tàu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9df35d6c99dc4b88\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9df35d6c99dc4b88)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚶‍♂️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "降りる",
    "kana": "おりる",
    "kanji": "降りる",
    "romaji": "oriru",
    "vi": "Xuống tàu xe",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7029192eaf9e4ac0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7029192eaf9e4ac0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏃</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "徒歩",
    "kana": "とほ",
    "kanji": "徒歩",
    "romaji": "toho",
    "vi": "Đi bộ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e9ec8e9dde76ee9b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e9ec8e9dde76ee9b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚶</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "路線図",
    "kana": "ろせんず",
    "kanji": "路線図",
    "romaji": "rosenzu",
    "vi": "Bản đồ tuyến đường tàu xe",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fb100b0f027b8165\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fb100b0f027b8165)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗺️</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "案内所",
    "kana": "あんないじょ",
    "kanji": "案内所",
    "romaji": "annaijo",
    "vi": "Quầy hướng dẫn thông tin",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b762a5264503b844\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b762a5264503b844)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">ℹ️</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "迷う",
    "kana": "まよう",
    "kanji": "迷う",
    "romaji": "mayou",
    "vi": "Lạc đường",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2dfe3babbd609e04\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2dfe3babbd609e04)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧭</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "到着する",
    "kana": "とうちゃくする",
    "kanji": "到着する",
    "romaji": "touchakusuru",
    "vi": "Đến nơi, cập bến",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_64c7dcb7876e7887\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_64c7dcb7876e7887)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏁</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "出発する",
    "kana": "しゅっぱつする",
    "kanji": "出発する",
    "romaji": "shuppatsusuru",
    "vi": "Xuất phát, khởi hành",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b81423fde98daff4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b81423fde98daff4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛫</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "遠い",
    "kana": "とおい",
    "kanji": "遠い",
    "romaji": "tooi",
    "vi": "Xa xôi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0c36c9a9605f87dd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0c36c9a9605f87dd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗾</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "近い",
    "kana": "ちかい",
    "kanji": "近い",
    "romaji": "chikai",
    "vi": "Gần",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a93e4da81177bfb9\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a93e4da81177bfb9)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📍</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "運賃",
    "kana": "うんちん",
    "kanji": "運賃",
    "romaji": "unchin",
    "vi": "Cước phí đi lại, tiền vé xe tàu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_07f860e1ebb6875f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_07f860e1ebb6875f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💴</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 13 (A2-2)",
    "jp": "どのくらい",
    "kana": "どのくらい",
    "kanji": "どのくらい",
    "romaji": "dono kurai",
    "vi": "Khoảng bao lâu / chừng nào",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b39374250157ccf6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b39374250157ccf6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏱️</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "のります",
    "vi": "Lên xe / đi tàu",
    "te": "のって",
    "form1": "のってから (sau khi lên xe)",
    "form2": "のった (đã đi)",
    "form3": "のる"
  },
  {
    "masu": "おります",
    "vi": "Xuống xe tàu",
    "te": "おりて",
    "form1": "おりてください (xin hãy xuống ở)",
    "form2": "おりた",
    "form3": "おりる"
  },
  {
    "masu": "のりかえます",
    "vi": "Đổi tàu xe",
    "te": "のりかえて",
    "form1": "のりかえてください",
    "form2": "のりかえた",
    "form3": "のりかえる"
  },
  {
    "masu": "まよいます",
    "vi": "Lạc đường",
    "te": "まよって",
    "form1": "みちに まよってしまいました (lỡ lạc đường)",
    "form2": "まよった",
    "form3": "まよう"
  },
  {
    "masu": "つきます",
    "vi": "Tới nơi",
    "te": "ついて",
    "form1": "ついたら (khi tới nơi)",
    "form2": "ついた",
    "form3": "つく"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "ここから バス [____] 乗って、市役所前で 降りてください。",
    "options": [
      "を",
      "で",
      "に",
      "が"
    ],
    "correct": 2,
    "explain": "Lên xe buýt dùng trợ từ に: 『バスに 乗る』."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "次の 駅で 地下鉄 [____] 乗り換えます。",
    "options": [
      "を",
      "へ",
      "で",
      "に"
    ],
    "correct": 3,
    "explain": "Đổi sang phương tiện mới dùng trợ từ に: 『地下鉄に 乗り換える』."
  },
  {
    "id": 3,
    "category": "Hội thoại",
    "q": "「お寺まで どのくらい [____] か。」 ―― 「歩いて 15分です。」",
    "options": [
      "します",
      "いきます",
      "かかります",
      "のります"
    ],
    "correct": 2,
    "explain": "Hỏi mất bao lâu: 「どのくらい かかりますか」."
  },
  {
    "id": 4,
    "category": "Từ vựng",
    "q": "地下を 走る 電車を [____] と 言います。",
    "options": [
      "新幹線",
      "バス",
      "ちかてつ",
      "タクシー"
    ],
    "correct": 2,
    "explain": "Tàu điện ngầm chạy dưới lòng đất là 「地下鉄 (ちかてつ)」."
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「切符」 có cách đọc chuẩn là gì?",
    "options": [
      "きりふ",
      "きっぷ",
      "せっぷ",
      "きっふ"
    ],
    "correct": 1,
    "explain": "切符 đọc là 「きっぷ」 (vé tàu xe)."
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "駅で 切符や ICカードを タッチして 通る 改札口は [____] です。",
    "options": [
      "あんないじょ",
      "ろせんず",
      "のりかえ",
      "かいさつぐち"
    ],
    "correct": 3,
    "explain": "Cổng soát vé nhà ga là 「改札口 (かいさつぐち)」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ 「降ります」 đối nghĩa với từ nào?",
    "options": [
      "行きます",
      "来ます",
      "乗ります (のります)",
      "帰ります"
    ],
    "correct": 2,
    "explain": "降ります (xuống xe) đối nghĩa với 乗ります (lên xe)."
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "道が 分からなくなって、[____] しまいました。交番で 聞きましょう。",
    "options": [
      "迷って",
      "止まって",
      "始まって",
      "終わって"
    ],
    "correct": 0,
    "explain": "Bị lạc đường: 迷います ➔ 「迷ってしまいました (まよって)」."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「遠い」 đọc là gì?",
    "options": [
      "ちかい",
      "とおい",
      "おそい",
      "はやい"
    ],
    "correct": 1,
    "explain": "遠い đọc là 「とおい」 (VIỄN - xa xôi)."
  },
  {
    "id": 10,
    "category": "Từ vựng",
    "q": "電車や バスの 乗り方や 行き先が 描かれている 地図は [____] です。",
    "options": [
      "ろせんず",
      "ガイドブック",
      "手紙",
      "メニュー"
    ],
    "correct": 0,
    "explain": "Sơ đồ các tuyến đường tàu xe là 「路線図 (ろせんず)」."
  },
  {
    "id": 11,
    "category": "Ngữ pháp",
    "q": "電車を [____] とき、足元に 気をつけて ください。",
    "options": [
      "降りた",
      "降りる",
      "降りて",
      "降ります"
    ],
    "correct": 1,
    "explain": "Khi xuống khỏi tàu: 『[V thể từ điển] + とき』 ➔ 「降りるとき」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「出発」 có âm Hán Việt là gì?",
    "options": [
      "XUẤT PHÁP",
      "XUẤT HÀNH",
      "NHẬP PHÁT",
      "XUẤT PHÁT"
    ],
    "correct": 3,
    "explain": "出発 có âm Hán Việt là XUẤT PHÁT (khởi hành)."
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "車や 電車を 使わずに、自分の 足で 歩いて いくことを [____] と 言います。",
    "options": [
      "とほ",
      "のりかえ",
      "うんちん",
      "とうちゃく"
    ],
    "correct": 0,
    "explain": "Đi bộ bằng chân là 「徒歩 (とほ)」 (ví dụ: 徒歩5分)."
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "駅員に 「すみません、京都寺へは [____] 行きますか」 と 尋ねました。",
    "options": [
      "だれと",
      "どうやって",
      "何時に",
      "なぜ"
    ],
    "correct": 1,
    "explain": "Hỏi cách đi tới địa điểm: 「どうやって 行きますか」."
  },
  {
    "id": 15,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「乗」 trong 「乗車」 có âm On là gì?",
    "options": [
      "じょう",
      "とう",
      "のり",
      "しょう"
    ],
    "correct": 0,
    "explain": "乗 có âm On là 「じょう」 (trong 乗車 - じょうしゃ, 乗客 - じょうきゃく)."
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
