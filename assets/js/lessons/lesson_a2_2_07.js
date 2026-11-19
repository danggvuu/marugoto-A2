/* Marugoto A2-2 Bài 7 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "まつり",
    "kana": "まつり",
    "kanji": "祭り",
    "romaji": "matsuri",
    "vi": "Lễ hội truyền thống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_763c848b4e9fd487\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_763c848b4e9fd487)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏮</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "屋台",
    "kana": "やたい",
    "kanji": "屋台",
    "romaji": "yatai",
    "vi": "Quầy hàng ăn di động ngoài trời",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3a3c2cbb42528656\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3a3c2cbb42528656)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍢</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "花火",
    "kana": "はなび",
    "kanji": "花火",
    "romaji": "hanabi",
    "vi": "Pháo hoa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1c8502c91c9f8a30\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1c8502c91c9f8a30)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎆</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "浴衣",
    "kana": "ゆかた",
    "kanji": "浴衣",
    "romaji": "yukata",
    "vi": "Áo yukata (kimono mùa hè)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a406011e0216e4bb\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a406011e0216e4bb)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👘</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "太鼓",
    "kana": "たいこ",
    "kanji": "太鼓",
    "romaji": "taiko",
    "vi": "Trống Taiko Nhật Bản",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_932f11635ee5ecd4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_932f11635ee5ecd4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥁</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "盆踊り",
    "kana": "ぼんおどり",
    "kanji": "盆踊り",
    "romaji": "bon'odori",
    "vi": "Điệu múa Bon truyền thống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_23ea212062b557a2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_23ea212062b557a2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💃</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "雨",
    "kana": "あめ",
    "kanji": "雨",
    "romaji": "ame",
    "vi": "Cơn mưa",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4e342a0d811bed6f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4e342a0d811bed6f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌧️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "中止",
    "kana": "ちゅうし",
    "kanji": "中止",
    "romaji": "chuushi",
    "vi": "Hủy bỏ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_09c9e7122bb35315\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_09c9e7122bb35315)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛑</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "延期",
    "kana": "えんき",
    "kanji": "延期",
    "romaji": "enki",
    "vi": "Hoãn lại, dời ngày",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d9a035b6001d9136\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d9a035b6001d9136)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "集合",
    "kana": "しゅうごう",
    "kanji": "集合",
    "romaji": "shuugou",
    "vi": "Tập trung, tụ họp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f638c9ce9e4b638f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f638c9ce9e4b638f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "場所",
    "kana": "ばしょ",
    "kanji": "場所",
    "romaji": "basho",
    "vi": "Địa điểm, nơi chốn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d8958c03a5a7d736\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d8958c03a5a7d736)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📍</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "待ち合わせ",
    "kana": "まちあわせ",
    "kanji": "待ち合わせ",
    "romaji": "machiawase",
    "vi": "Điểm hẹn, việc hẹn gặp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5e9b3bd65c4b80e8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5e9b3bd65c4b80e8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "誘う",
    "kana": "さそう",
    "kanji": "誘う",
    "romaji": "sasou",
    "vi": "Rủ rê, mời mọc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8a4a8b1fb96ca965\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8a4a8b1fb96ca965)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👋</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "混雑",
    "kana": "こんざつ",
    "kanji": "混雑",
    "romaji": "konzatsu",
    "vi": "Đông đúc, chen chúc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f49da1f32ef22316\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f49da1f32ef22316)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚶‍♂️</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "にぎやか（な）",
    "kana": "にぎやか（な）",
    "kanji": "にぎやか（な）",
    "romaji": "nigiyaka(na)",
    "vi": "Náo nhiệt, sôi động",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a0fc8cc2bde1860a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a0fc8cc2bde1860a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "始まる",
    "kana": "はじまる",
    "kanji": "始まる",
    "romaji": "hajimaru",
    "vi": "Bắt đầu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b3cacc46a7dba138\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b3cacc46a7dba138)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">▶️</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "終わる",
    "kana": "おわる",
    "kanji": "終わる",
    "romaji": "owaru",
    "vi": "Kết thúc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_35184912fa636159\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_35184912fa636159)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏹️</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "連絡する",
    "kana": "れんらくする",
    "kanji": "連絡する",
    "romaji": "renrakusuru",
    "vi": "Liên lạc, nhắn tin",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6967bbbf98224469\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6967bbbf98224469)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📱</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "楽しみにする",
    "kana": "たのしみにする",
    "kanji": "楽しみにする",
    "romaji": "tanoshimi ni suru",
    "vi": "Háo hức mong đợi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5fde9e6fbaa5a93b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5fde9e6fbaa5a93b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥳</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 7 (A2-2)",
    "jp": "着ていく",
    "kana": "きていく",
    "kanji": "着ていく",
    "romaji": "kite iku",
    "vi": "Mặc (trang phục) đi tới",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_81c9569f41b4fbe4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_81c9569f41b4fbe4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👘</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "ふります",
    "vi": "Rơi (mưa)",
    "te": "ふって",
    "form1": "ふったら (nếu mưa rơi)",
    "form2": "ふらない (không mưa)",
    "form3": "ふる"
  },
  {
    "masu": "あつまります",
    "vi": "Tập hợp lại",
    "te": "あつまって",
    "form1": "あつまったら (khi tập hợp xong)",
    "form2": "あつまりましょう (hãy tập trung lại)",
    "form3": "あつまる"
  },
  {
    "masu": "さそいます",
    "vi": "Rủ rê",
    "te": "さそって",
    "form1": "さそったら",
    "form2": "さそいませんか (sao không rủ...)",
    "form3": "さそう"
  },
  {
    "masu": "ちゅうしします",
    "vi": "Hủy bỏ",
    "te": "ちゅうしして",
    "form1": "ちゅうしになったら (nếu bị hủy)",
    "form2": "ちゅうしした",
    "form3": "ちゅうしする"
  },
  {
    "masu": "れんらくします",
    "vi": "Liên lạc",
    "te": "れんらくして",
    "form1": "れんらくしたら",
    "form2": "れんらくしてください (hãy liên lạc)",
    "form3": "れんらくする"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "あした 雨が [____]、まつりは 延期（えんき）に なります。",
    "options": [
      "ふれば",
      "ふると",
      "ふったら",
      "ふって"
    ],
    "correct": 2,
    "explain": "Câu điều kiện nếu trời mưa: ふりました ➔ thể TA là 「ふったら」."
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "「土曜日の 花火大会、一緒に [____]。」 ―― 「ええ、ぜひ！」",
    "options": [
      "行きましょう",
      "行った",
      "行かない",
      "行きませんか"
    ],
    "correct": 3,
    "explain": "Mời rủ lịch sự: V-ませんか ➔ 「行きませんか」."
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "日本の 夏まつりで 夜空に 打ち上げられる 美しい 光は [____] です。",
    "options": [
      "たいこ",
      "はなび",
      "ゆかた",
      "やたい"
    ],
    "correct": 1,
    "explain": "Pháo hoa rực rỡ bắn trên bầu trời đêm mùa hè là 「花火 (はなび)」."
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "駅の 改札口に [____]、メッセージを 送ってください。",
    "options": [
      "ついて",
      "ついたら",
      "つくなら",
      "つく"
    ],
    "correct": 1,
    "explain": "Sau khi đến nơi (V-たら): 着きました ➔ 「着いたら (ついたら)」."
  },
  {
    "id": 5,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「祭り」 có âm Hán Việt là gì?",
    "options": [
      "SÁI",
      "TẾ",
      "HỢP",
      "TRƯỜNG"
    ],
    "correct": 1,
    "explain": "祭り có âm Hán Việt là TẾ (lễ hội tế thần)."
  },
  {
    "id": 6,
    "category": "Từ vựng",
    "q": "夏まつりで 着る 涼しい 木綿の 着物は [____] です。",
    "options": [
      "ゆかた",
      "みずぎ",
      "スーツ",
      "コート"
    ],
    "correct": 0,
    "explain": "Kimono mỏng mặc mùa hè đi hội là 「浴衣 (ゆかた)」."
  },
  {
    "id": 7,
    "category": "Hội thoại",
    "q": "「何時に どこで [____] か。」 ―― 「ハチ公前で 6時に しましょう。」",
    "options": [
      "泊まります",
      "泳ぎます",
      "待ち合わせます",
      "買います"
    ],
    "correct": 2,
    "explain": "Hẹn gặp mặt ở đâu: 「待ち合わせます (まちあわせます)」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ 「中止」 có nghĩa là gì?",
    "options": [
      "Hủy bỏ sự kiện",
      "Tạm dừng nghỉ ngơi",
      "Bắt đầu làm",
      "Thay đổi địa điểm"
    ],
    "correct": 0,
    "explain": "中止 (ちゅうし - TRUNG CHỈ) nghĩa là hủy bỏ."
  },
  {
    "id": 9,
    "category": "Từ vựng",
    "q": "大雨の ため、花火は [____] に なりました。来週 行われます。",
    "options": [
      "ちゅうし",
      "しゅうごう",
      "こんざつ",
      "えんき"
    ],
    "correct": 3,
    "explain": "Dời sang tuần sau tức là bị hoãn lại: 「延期 (えんき)」."
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「集合」 đọc là gì?",
    "options": [
      "しゅうごう",
      "じゅうごう",
      "しゅうあい",
      "しゅうかい"
    ],
    "correct": 0,
    "explain": "集合 đọc là 「しゅうごう」 (TẬP HỢP - tập trung lại một chỗ)."
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "まつりの 会場は 人が たくさん いて、とても [____] していました。",
    "options": [
      "しゅうごう",
      "こんざつ",
      "よやく",
      "たいけん"
    ],
    "correct": 1,
    "explain": "Đông nghẹt người, chen chúc nhau: 「混雑 (こんざつ) していました」."
  },
  {
    "id": 12,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「場所」 gồm 2 chữ nào?",
    "options": [
      "TRƯỜNG + SỞ",
      "ĐỊA + SỞ",
      "TRƯỜNG + ĐỊA",
      "THỊ + SỞ"
    ],
    "correct": 0,
    "explain": "場所 gồm chữ TRƯỜNG (場) và SỞ (所) ➔ nơi chốn, vị trí."
  },
  {
    "id": 13,
    "category": "Ngữ pháp",
    "q": "時間が [____]、屋台で たこ焼きを 買いましょう。",
    "options": [
      "あって",
      "あると",
      "あれば",
      "あったら"
    ],
    "correct": 3,
    "explain": "Nếu có thời gian: あります ➔ thể TA là 「あったら」."
  },
  {
    "id": 14,
    "category": "Chữ Hán",
    "q": "Chữ Hán 「始まる」 có âm Hán Việt là gì?",
    "options": [
      "CHUNG",
      "KAI",
      "THỦY",
      "NGUYÊN"
    ],
    "correct": 2,
    "explain": "始まる có âm Hán Việt là THỦY (khởi đầu, bắt đầu)."
  },
  {
    "id": 15,
    "category": "Hội thoại",
    "q": "「まつり、とても 楽しかったですね。」 ―― 「[____]」",
    "options": [
      "いいえ、どういたしまして。",
      "こちらこそ、ごめんなさい。",
      "ええ、本当に よかったですね！",
      "はじめまして。"
    ],
    "correct": 2,
    "explain": "Đồng tình chia sẻ cảm xúc vui vẻ sau sự kiện: 「ええ、本当によかったですね！」."
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
