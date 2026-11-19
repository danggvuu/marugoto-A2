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
    "vi": "Cuộc đời, nhân sinh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6d8b914ab2d6e9de\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6d8b914ab2d6e9de)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌱</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "生涯",
    "kana": "しょうがい",
    "kanji": "生涯",
    "romaji": "shougai",
    "vi": "Cả cuộc đời, suốt đời",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3ab4d2eba4b7039a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3ab4d2eba4b7039a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📜</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "生まれる",
    "kana": "うまれる",
    "kanji": "生まれる",
    "romaji": "umareru",
    "vi": "Sinh ra",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e489f6124f901d08\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e489f6124f901d08)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👶</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "育つ",
    "kana": "そだつ",
    "kanji": "育つ",
    "romaji": "sodatsu",
    "vi": "Lớn lên, trưởng thành",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3676c80698f1123a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3676c80698f1123a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪴</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "時代",
    "kana": "じだい",
    "kanji": "時代",
    "romaji": "jidai",
    "vi": "Thời đại, thế hệ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e65b8e75d6ede63b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e65b8e75d6ede63b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⏳</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "成功する",
    "kana": "せいこうする",
    "kanji": "成功する",
    "romaji": "seikousuru",
    "vi": "Thành công",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_310313b64942b0a3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_310313b64942b0a3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏆</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "失敗する",
    "kana": "しっぱいする",
    "kanji": "失敗する",
    "romaji": "shippaisuru",
    "vi": "Thất bại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_710b8dc0a898001d\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_710b8dc0a898001d)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌧️</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "努力する",
    "kana": "どりょくする",
    "kanji": "努力する",
    "romaji": "doryokusuru",
    "vi": "Nỗ lực, cố gắng hết mình",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f246a9ab359fc94c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f246a9ab359fc94c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💪</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "夢",
    "kana": "ゆめ",
    "kanji": "夢",
    "romaji": "yume",
    "vi": "Ước mơ, hoài bão",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6c0826e1a54bac5f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6c0826e1a54bac5f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⭐</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "作家",
    "kana": "さっか",
    "kanji": "作家",
    "romaji": "sakka",
    "vi": "Nhà văn, tác giả",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d2e796274019fb4e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d2e796274019fb4e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🖋️</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "漫画家",
    "kana": "まんがか",
    "kanji": "漫画家",
    "romaji": "mangaka",
    "vi": "Họa sĩ truyện tranh",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7409c1738b26326f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7409c1738b26326f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎨</text>\n</svg>"
  },
  {
    "id": 12,
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
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "作品",
    "kana": "さくひん",
    "kanji": "作品",
    "romaji": "sakuhin",
    "vi": "Tác phẩm nghệ thuật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ec2c28bde37161be\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ec2c28bde37161be)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🖼️</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "有名（な）",
    "kana": "ゆうめい（な）",
    "kanji": "有名（な）",
    "romaji": "yuumei(na)",
    "vi": "Nổi tiếng khắp nơi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f79be5c1088266f8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f79be5c1088266f8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌟</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "世界的（な）",
    "kana": "せかいてき（な）",
    "kanji": "世界的（な）",
    "romaji": "sekaiteki(na)",
    "vi": "Tầm cỡ thế giới",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6dcebb61cb53b96c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6dcebb61cb53b96c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌐</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "影響",
    "kana": "えいきょう",
    "kanji": "影響",
    "romaji": "eikyou",
    "vi": "Ảnh hưởng, tác động",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_00556dde2c6edeb0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_00556dde2c6edeb0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌊</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "受ける",
    "kana": "うける",
    "kanji": "受ける",
    "romaji": "ukeru",
    "vi": "Nhận được (ảnh hưởng/giải thưởng)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_dd7c75a5644a07db\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_dd7c75a5644a07db)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤲</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "賞",
    "kana": "しょう",
    "kanji": "賞",
    "romaji": "shou",
    "vi": "Giải thưởng danh giá",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4d6c4eddd5e4a483\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4d6c4eddd5e4a483)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥇</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "活躍する",
    "kana": "かつやくする",
    "kanji": "活躍する",
    "romaji": "katsuyakusuru",
    "vi": "Hoạt động sôi nổi, gặt hái thành tựu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_75518ab18f2bbf80\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_75518ab18f2bbf80)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚀</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 17 (A2-2)",
    "jp": "亡くなる",
    "kana": "なくなる",
    "kanji": "亡くなる",
    "romaji": "nakunaru",
    "vi": "Qua đời, mất",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6cfc9fe0b7947466\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6cfc9fe0b7947466)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🕊️</text>\n</svg>"
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
