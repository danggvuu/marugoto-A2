/* Marugoto A2-2 Bài 4 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "豚肉",
    "kana": "ぶたにく",
    "kanji": "豚肉",
    "romaji": "butaniku",
    "vi": "Thịt lợn (heo)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0f206ba33d6b2246\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0f206ba33d6b2246)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥩</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "牛肉",
    "kana": "ぎゅうにく",
    "kanji": "牛肉",
    "romaji": "gyuuniku",
    "vi": "Thịt bò",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_85e888d6ac0fb489\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_85e888d6ac0fb489)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥩</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "鶏肉",
    "kana": "とりにく",
    "kanji": "鶏肉",
    "romaji": "toriniku",
    "vi": "Thịt gà",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d040776882f60281\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d040776882f60281)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍗</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "卵",
    "kana": "たまご",
    "kanji": "卵",
    "romaji": "tamago",
    "vi": "Trứng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9617840231521da3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9617840231521da3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥚</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "野菜",
    "kana": "やさい",
    "kanji": "野菜",
    "romaji": "yasai",
    "vi": "Rau củ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_46bc2ab4e6361057\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_46bc2ab4e6361057)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥬</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "ネギ",
    "kana": "ネギ",
    "kanji": "ネギ",
    "romaji": "negi",
    "vi": "Hành lá",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_577f5aaaf14b03ef\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_577f5aaaf14b03ef)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧅</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "わさび",
    "kana": "わさび",
    "kanji": "わさび",
    "romaji": "wasabi",
    "vi": "Mù tạt wasabi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bfb588fd4ec0ef03\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bfb588fd4ec0ef03)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌿</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "アレルギー",
    "kana": "アレルギー",
    "kanji": "アレルギー",
    "romaji": "arerugii",
    "vi": "Dị ứng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_69cdc04177a960cd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_69cdc04177a960cd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚠️</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "豚肉抜き",
    "kana": "ぶたにくぬき",
    "kanji": "豚肉抜き",
    "romaji": "butaniku nuki",
    "vi": "Không lấy thịt lợn, bỏ thịt lợn ra",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dc3df2b403d0262c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dc3df2b403d0262c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚫</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "スープ",
    "kana": "スープ",
    "kanji": "スープ",
    "romaji": "suupu",
    "vi": "Nước súp, nước dùng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6df8e410664357e0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6df8e410664357e0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥣</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "たれ",
    "kana": "たれ",
    "kanji": "たれ",
    "romaji": "tare",
    "vi": "Nước chấm sốt tare",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_663912c6dc863756\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_663912c6dc863756)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍶</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "スプーン",
    "kana": "スプーン",
    "kanji": "スプーン",
    "romaji": "supuun",
    "vi": "Cái thìa / muỗng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3327258c33f555b7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3327258c33f555b7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥄</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "はし",
    "kana": "はし",
    "kanji": "はし",
    "romaji": "hashi",
    "vi": "Đôi đũa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6ad8ca903e0fda95\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6ad8ca903e0fda95)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥢</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "おかわり",
    "kana": "おかわり",
    "kanji": "おかわり",
    "romaji": "okawari",
    "vi": "Bát nữa / thêm một phần cơm hoặc canh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_97239761af1001ca\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_97239761af1001ca)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍚</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "お腹がいっぱい",
    "kana": "おなかが いっぱい",
    "kanji": "お腹がいっぱい",
    "romaji": "onaka ga ippai",
    "vi": "No bụng, no căng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_47c9bf74645e94e0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_47c9bf74645e94e0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😋</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "残す",
    "kana": "のこす",
    "kanji": "残す",
    "romaji": "nokosu",
    "vi": "Để lại, ăn thừa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_accc5a4a7671dbbd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_accc5a4a7671dbbd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍽️</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "焼く",
    "kana": "やく",
    "kanji": "焼く",
    "romaji": "yaku",
    "vi": "Nướng, xào rán",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_19b920bd60390336\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_19b920bd60390336)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍳</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "煮る",
    "kana": "にる",
    "kanji": "煮る",
    "romaji": "niru",
    "vi": "Ninh, hầm, kho",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7b42b24ccfb24cfe\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7b42b24ccfb24cfe)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍲</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "つける",
    "kana": "つける",
    "kanji": "つける",
    "romaji": "tsukeru",
    "vi": "Chấm (nước sốt)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7ad0fdcf48831dcd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7ad0fdcf48831dcd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥢</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 4 (A2-2)",
    "jp": "かける",
    "kana": "かける",
    "kanji": "かける",
    "romaji": "kakeru",
    "vi": "Rưới, chan (nước sốt lên món)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_35e1b0fd5145d233\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_35e1b0fd5145d233)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🫗</text>\n</svg>"
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
      "～かた"
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
      "Tất cả",
      "Cách ～",
      "Cách ăn"
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
      "～かた",
      "たべかた",
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
    "q": "Từ Kanji 「～方」 có nghĩa là gì?",
    "options": [
      "Cách ăn",
      "Nóng (đồ vật, thức ăn)",
      "Không giỏi, không thích",
      "Cách ～"
    ],
    "correct": 3,
    "explain": "～方 nghĩa là Cách ～.",
    "scopeKanji": "～方"
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
