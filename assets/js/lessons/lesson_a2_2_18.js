/* Marugoto A2-2 Bài 18 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "子ども",
    "kana": "こども",
    "kanji": "子ども",
    "romaji": "kodomo",
    "vi": "Trẻ con, đứa trẻ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ac6e95fb087cda38\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ac6e95fb087cda38)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧒</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "昔",
    "kana": "むかし",
    "kanji": "昔",
    "romaji": "mukashi",
    "vi": "Ngày xưa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5be24d7dea8c6560\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5be24d7dea8c6560)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "頃",
    "kana": "ころ",
    "kanji": "頃",
    "romaji": "koro",
    "vi": "Hồi, lúc (thời gian trước)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0717dfb43f153652\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0717dfb43f153652)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕰️</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "性格",
    "kana": "せいかく",
    "kanji": "性格",
    "romaji": "seikaku",
    "vi": "Tính cách",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_770290b6ef4da391\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_770290b6ef4da391)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧠</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "おとなしい",
    "kana": "おとなしい",
    "kanji": "おとなしい",
    "romaji": "otonashii",
    "vi": "Hiền lành, trầm tính, ngoan ngoãn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bab8e79705d161f8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bab8e79705d161f8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😌</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "元気（な）",
    "kana": "げんき（な）",
    "kanji": "元気（な）",
    "romaji": "genki(na)",
    "vi": "Khỏe mạnh, hoạt bát",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8c8ebbeacb3ed3d2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8c8ebbeacb3ed3d2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚡</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "活発（な）",
    "kana": "かっぱつ（な）",
    "kanji": "活発（な）",
    "romaji": "kappatsu(na)",
    "vi": "Năng động, sôi nổi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_98f2fd8ef731d836\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_98f2fd8ef731d836)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏃‍♂️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "いたずら（な）",
    "kana": "いたずら（な）",
    "kanji": "いたずら（な）",
    "romaji": "itazura(na)",
    "vi": "Nghịch ngợm, quậy phá",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b0947a0b798fa594\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b0947a0b798fa594)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😜</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "将来",
    "kana": "しょうらい",
    "kanji": "将来",
    "romaji": "shourai",
    "vi": "Tương lai",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d2c173401877d00e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d2c173401877d00e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔭</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "変わる",
    "kana": "かわる",
    "kanji": "変わる",
    "romaji": "kawaru",
    "vi": "Thay đổi, biến đổi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c3e4184b699be308\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c3e4184b699be308)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "思い出す",
    "kana": "おもいだす",
    "kanji": "思い出す",
    "romaji": "omoidasu",
    "vi": "Nhớ lại, hồi tưởng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3eba1cdbcbd263c3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3eba1cdbcbd263c3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💭</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "覚える",
    "kana": "おぼえる",
    "kanji": "覚える",
    "romaji": "oboeru",
    "vi": "Ghi nhớ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0a97ceddf083b363\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0a97ceddf083b363)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧠</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "家族",
    "kana": "かぞく",
    "kanji": "家族",
    "romaji": "kazoku",
    "vi": "Gia đình",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_230524693dd0a978\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_230524693dd0a978)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👨‍👩‍👧‍👦</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "目標",
    "kana": "もくひょう",
    "kanji": "目標",
    "romaji": "mokuhyou",
    "vi": "Mục tiêu phấn đấu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_021d2061ec9e48cd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_021d2061ec9e48cd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎯</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "頑張る",
    "kana": "がんばる",
    "kanji": "頑張る",
    "romaji": "ganbaru",
    "vi": "Cố gắng, nỗ lực hết sức",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4a5f964435b69744\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4a5f964435b69744)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔥</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "勉強する",
    "kana": "べんきょうする",
    "kanji": "勉強する",
    "romaji": "benkyousuru",
    "vi": "Học tập",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a5151651f0e179c5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a5151651f0e179c5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📚</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "成長する",
    "kana": "せいちょうする",
    "kanji": "成長する",
    "romaji": "seichousuru",
    "vi": "Trưởng thành, lớn lên",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a896baefd200d1cb\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a896baefd200d1cb)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📈</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "これから",
    "kana": "これから",
    "kanji": "これから",
    "romaji": "korekara",
    "vi": "Từ nay về sau",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f640d89f6ef9c277\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f640d89f6ef9c277)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">➡️</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "ずっと",
    "kana": "ずっと",
    "kanji": "ずっと",
    "romaji": "zutto",
    "vi": "Suốt, mãi mãi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_56393d1259353567\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_56393d1259353567)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">♾️</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "働く",
    "kana": "はたらく",
    "kanji": "働く",
    "romaji": "hataraku",
    "vi": "Làm việc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fa71af8566e0d7d7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fa71af8566e0d7d7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💼</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "おもいだします",
    "vi": "Nhớ lại",
    "te": "おもいだして",
    "form1": "おもいだすと (mỗi khi nhớ lại)",
    "form2": "おもいだした (đã nhớ ra)",
    "form3": "おもいだす"
  },
  {
    "masu": "がんばります",
    "vi": "Cố gắng",
    "te": "がんばって",
    "form1": "がんばろうと思っています (đang dự định sẽ cố gắng)",
    "form2": "がんばった",
    "form3": "がんばる"
  },
  {
    "masu": "かわります",
    "vi": "Thay đổi",
    "te": "かわって",
    "form1": "かわりました (đã đổi thay)",
    "form2": "かわったこと",
    "form3": "かわる"
  },
  {
    "masu": "はたらきます",
    "vi": "Làm việc",
    "te": "はたらいて",
    "form1": "はたらこうと思っています (tính sẽ làm việc)",
    "form2": "はたらいた",
    "form3": "はたらく"
  },
  {
    "masu": "つづけます",
    "vi": "Tiếp tục duy trì",
    "te": "つづけて",
    "form1": "つづけようと思います",
    "form2": "つづけた",
    "form3": "つづける"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "将来、日本で 自分の 会社を [____] と 思っています。",
    "options": [
      "作ろう",
      "作る",
      "作った",
      "作り"
    ],
    "correct": 0,
    "explain": "Cấu trúc dự định thể ý chí: 『V thể Ý chí + と思っています』: 作ります ➔ 「作ろう」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "子どもの [____] は、いつも 外で 元気に 走っていました。",
    "options": [
      "まえ",
      "ころ",
      "あと",
      "あいだ"
    ],
    "correct": 1,
    "explain": "Thời bé, hồi nhỏ: 『子どもの頃 (ころ)』."
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "あまり 騒がずに 静かで 礼儀正しい 様子は [____] です。",
    "options": [
      "いたずら",
      "おとなしい",
      "かっぱつ",
      "にぎやか"
    ],
    "correct": 1,
    "explain": "Hiền lành, ngoan ngoãn, trầm tính: 「おとなしい」."
  },
  {
    "id": 4,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「性格」 có cách đọc chuẩn là gì?",
    "options": [
      "せいかく",
      "しょうかく",
      "せいこう",
      "せいぎ"
    ],
    "correct": 0,
    "explain": "性格 đọc là 「せいかく」 (TÍNH CÁCH)."
  },
  {
    "id": 5,
    "category": "Ngữ pháp",
    "q": "これからも 毎日 日本語を [____] と 思います。",
    "options": [
      "勉強する",
      "勉強して",
      "勉強しよう",
      "勉強した"
    ],
    "correct": 2,
    "explain": "Dự định tương lai: 勉強します ➔ thể ý chí là 「勉強しよう」."
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "元気で 行動的な 人の 性格を 「[____] な 性格」 と 表現します。",
    "options": [
      "おとなしい",
      "ふべん",
      "ひくい",
      "かっぱつ"
    ],
    "correct": 3,
    "explain": "Năng động hoạt bát: 「活発 (かっぱつ) な性格」."
  },
  {
    "id": 7,
    "category": "Chữ Hán",
    "q": "Từ 「将来」 có nghĩa là gì?",
    "options": [
      "Quá khứ đã qua",
      "Hiện tại bây giờ",
      "Thời xưa",
      "Tương lai phía trước"
    ],
    "correct": 3,
    "explain": "将来 (しょうらい - TƯƠNG LAI) nghĩa là tương lai, mai sau."
  },
  {
    "id": 8,
    "category": "Hội thoại",
    "q": "昔の 写真を 見ると、当時の 楽しい 思い出を [____] ます。",
    "options": [
      "覚えます",
      "調べます",
      "思い出し",
      "変わります"
    ],
    "correct": 2,
    "explain": "Hồi tưởng, nhớ lại kỷ niệm cũ: 「思い出す (おもいだす)」."
  },
  {
    "id": 9,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「目標」 gồm 2 chữ nào?",
    "options": [
      "NHÃN + TIÊU",
      "MỤC + ĐÍCH",
      "MỤC + TIÊU",
      "ĐẦU + TIÊU"
    ],
    "correct": 2,
    "explain": "目標 gồm MỤC (目) và TIÊU (標) ➔ mục tiêu phấn đấu."
  },
  {
    "id": 10,
    "category": "Từ vựng",
    "q": "先生や 友達に 「これからも [____] ね！」 と 励まされました。",
    "options": [
      "とまって",
      "がんばって",
      "あきらめて",
      "つかれて"
    ],
    "correct": 1,
    "explain": "Lời động viên cố lên: 「これからも 頑張って (がんばって) ね！」."
  },
  {
    "id": 11,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「覚える」 đọc là gì?",
    "options": [
      "かんがえる",
      "おもえる",
      "さとる",
      "おぼえる"
    ],
    "correct": 3,
    "explain": "覚える đọc là 「おぼえる」 (GIÁC - ghi nhớ)."
  },
  {
    "id": 12,
    "category": "Ngữ pháp",
    "q": "子どもの 頃は ピーマンが 嫌いでしたが、大人に なってから 食べられるように [____]。",
    "options": [
      "します",
      "なれません",
      "なりました",
      "しています"
    ],
    "correct": 2,
    "explain": "Biến đổi trạng thái theo thời gian: 『V-る / られる ように なりました』 (đã có thể ăn được)."
  },
  {
    "id": 13,
    "category": "Từ vựng",
    "q": "自分の 目標に 向かって 心も 体も 大きく なることを [____] と 言います。",
    "options": [
      "しっぱい",
      "せいちょう",
      "へんぴん",
      "こうかん"
    ],
    "correct": 1,
    "explain": "Trưởng thành, lớn lên: 「成長 (せいちょう)」."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Từ 「勉強」 có âm Hán Việt là gì?",
    "options": [
      "MIỄN CƯỠNG",
      "MIỄN LỰC",
      "CƯỠNG LỰC",
      "HỌC TẬP"
    ],
    "correct": 0,
    "explain": "勉強 có âm Hán Việt là MIỄN CƯỠNG (nghĩa gốc là gắng sức nỗ lực học tập)."
  },
  {
    "id": 15,
    "category": "Hội thoại",
    "q": "「まるごと A2-2の 勉強、お疲れ様でした！」 ―― 「[____]」",
    "options": [
      "ありがとうございました！ 楽しかったです！",
      "どういたしまして。",
      "こちらこそ、ごめんなさい。",
      "おやすみなさい。"
    ],
    "correct": 0,
    "explain": "Lời đáp đầy hào hứng và biết ơn khi hoàn thành khóa học A2-2: 「ありがとうございました！ 楽しかったです！」."
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
