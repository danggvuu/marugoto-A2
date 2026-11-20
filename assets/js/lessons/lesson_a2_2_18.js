/* Marugoto A2-2 Bài 18 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "けんかします",
    "kana": "けんかします",
    "kanji": "けんかします",
    "romaji": "kenka shimasu",
    "vi": "Cãi cọ, đánh nhau",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ee226570914fdc37\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ee226570914fdc37)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥊</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "褒めます",
    "kana": "ほめます",
    "kanji": "褒めます",
    "romaji": "homemasu",
    "vi": "Khen ngợi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_89d32ac8a54bd453\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_89d32ac8a54bd453)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👏</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "叱ります",
    "kana": "しかります",
    "kanji": "叱ります",
    "romaji": "shikarimasu",
    "vi": "Mắng, quở trách",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1157558deca6a9ad\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1157558deca6a9ad)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😠</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "おしゃれします",
    "kana": "おしゃれします",
    "kanji": "おしゃれします",
    "romaji": "oshare shimasu",
    "vi": "Làm đỏm, diện đồ đẹp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_070fe97e2bb67f72\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_070fe97e2bb67f72)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👗</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "誘います",
    "kana": "さそいます",
    "kanji": "誘います",
    "romaji": "sasoimasu",
    "vi": "Rủ bạn bè, mời",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3bf93f4cab3cc71f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3bf93f4cab3cc71f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "就職します",
    "kana": "しゅうしょくします",
    "kanji": "就職します",
    "romaji": "shuushoku shimasu",
    "vi": "Vào làm tại công ty",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b876438dc2e651bd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b876438dc2e651bd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💼</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "デートします",
    "kana": "デートします",
    "kanji": "デートします",
    "romaji": "de-to shimasu",
    "vi": "Hẹn hò với người yêu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_34e72a3ca77b36d7\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_34e72a3ca77b36d7)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💑</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "転勤します",
    "kana": "てんきんします",
    "kanji": "転勤します",
    "romaji": "tenkin shimasu",
    "vi": "Chuyển công tác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ed0d90a3d266f8c3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ed0d90a3d266f8c3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">✈️</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "退職します",
    "kana": "たいしょくします",
    "kanji": "退職します",
    "romaji": "taishoku shimasu",
    "vi": "Nghỉ việc, về hưu",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9c53feddf4e6ec77\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9c53feddf4e6ec77)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏖️</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "ひどい",
    "kana": "ひどい",
    "kanji": "ひどい",
    "romaji": "hidoi",
    "vi": "Tồi tệ, quá đáng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1fb2e69d34bc2229\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1fb2e69d34bc2229)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😣</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "悲しい",
    "kana": "かなしい",
    "kanji": "悲しい",
    "romaji": "kanashii",
    "vi": "Buồn rầu, đau lòng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1729b5817314f865\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1729b5817314f865)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😢</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "甘えます",
    "kana": "あまえます",
    "kanji": "甘えます",
    "romaji": "amaemasu",
    "vi": "Nũng nịu, nhõng nhẽo",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b15dee67a52273f2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b15dee67a52273f2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥰</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "大人しい",
    "kana": "おとなしい",
    "kanji": "大人しい",
    "romaji": "otonashii",
    "vi": "Điềm đạm, dễ bảo, ngoan",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7d1774010d877ebd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7d1774010d877ebd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😌</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "成績",
    "kana": "せいせき",
    "kanji": "成績",
    "romaji": "seiseki",
    "vi": "Thành tích, kết quả học tập",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e485534ca3813790\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e485534ca3813790)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📊</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "恥ずかしい",
    "kana": "はずかしい",
    "kanji": "恥ずかしい",
    "romaji": "hazukashii",
    "vi": "Xấu hổ, ngượng ngùng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b9b6700679face62\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b9b6700679face62)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😳</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "きっかけ",
    "kana": "きっかけ",
    "kanji": "きっかけ",
    "romaji": "kikkake",
    "vi": "Cơ duyên, duyên cớ",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_69c6f43f91deca89\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_69c6f43f91deca89)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔑</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "夕食",
    "kana": "ゆうしょく",
    "kanji": "夕食",
    "romaji": "yuushoku",
    "vi": "Bữa cơm tối",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_847e755b80215593\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_847e755b80215593)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍲</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "仲がいい",
    "kana": "なかがいい",
    "kanji": "仲がいい",
    "romaji": "naka ga ii",
    "vi": "Thân thiết, mối quan hệ tốt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6c53d93d25a46f01\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6c53d93d25a46f01)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👫</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "勧めます",
    "kana": "すすめます",
    "kanji": "勧めます",
    "romaji": "susumemasu",
    "vi": "Đề xuất, gợi ý",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a7b6323e6a103541\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a7b6323e6a103541)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "社会人",
    "kana": "しゃかいじん",
    "kanji": "社会人",
    "romaji": "shakaijin",
    "vi": "Người đi làm, người ngoài xã hội",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_12661e1e4fd87e40\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_12661e1e4fd87e40)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "やっと",
    "kana": "やっと",
    "kanji": "やっと",
    "romaji": "yatto",
    "vi": "Cuối cùng thì (kết quả tốt)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_551554ae88fc9aa6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_551554ae88fc9aa6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎉</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 18 (A2-2)",
    "jp": "心配します",
    "kana": "しんぱいします",
    "kanji": "心配します",
    "romaji": "shinpai shimasu",
    "vi": "Lo lắng, bận tâm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c99ff7b0fcae0b20\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c99ff7b0fcae0b20)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😟</text>\n</svg>"
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
    "q": "私は母に [____]。",
    "options": [
      "しかられました",
      "しからせました",
      "しかりました",
      "しかって"
    ],
    "correct": 0,
    "explain": "しかられました là thể bị động: bị mẹ mắng.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "朝早く起きるように [____]。",
    "options": [
      "しました",
      "なりました",
      "あります",
      "いました"
    ],
    "correct": 1,
    "explain": "Vるようになりました diễn tả thói quen mới hình thành.",
    "grammarScope": "official"
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
    "q": "Từ Kanji 「思い出」 có cách đọc nào?",
    "options": [
      "おもいで",
      "せいかつ",
      "えいが",
      "おっと"
    ],
    "correct": 0,
    "explain": "思い出 đọc là 「おもいで」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "思い出"
  },
  {
    "id": 5,
    "category": "Ngữ pháp",
    "q": "夜テレビを見 [____] なりました。",
    "options": [
      "ないで",
      "なくて",
      "なく",
      "ない"
    ],
    "correct": 2,
    "explain": "Vなくなりました diễn tả một việc không còn xảy ra.",
    "grammarScope": "official"
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
    "q": "Từ Kanji 「生活」 có nghĩa là gì?",
    "options": [
      "Phim",
      "Chồng (của mình)",
      "Vợ (của mình)",
      "Cuộc sống, sinh hoạt"
    ],
    "correct": 3,
    "explain": "生活 nghĩa là Cuộc sống, sinh hoạt.",
    "scopeKanji": "生活"
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
    "q": "Từ Kanji 「映画」 có nghĩa là gì?",
    "options": [
      "Chồng (của mình)",
      "Vợ (của mình)",
      "Phim",
      "Cha mẹ"
    ],
    "correct": 2,
    "explain": "映画 nghĩa là Phim.",
    "scopeKanji": "映画"
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
    "q": "Từ Kanji 「夫」 có nghĩa là gì?",
    "options": [
      "Vợ (của mình)",
      "Cha mẹ",
      "Bất tiện",
      "Chồng (của mình)"
    ],
    "correct": 3,
    "explain": "夫 nghĩa là Chồng (của mình).",
    "scopeKanji": "夫"
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
    "explain": "Biến đổi trạng thái theo thời gian: 『V-る / られる ように なりました』 (đã có thể ăn được).",
    "grammarScope": "official"
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
    "q": "Từ Kanji 「妻」 có cách đọc nào?",
    "options": [
      "つま",
      "りょうしん",
      "ふべん",
      "えらびます"
    ],
    "correct": 0,
    "explain": "妻 đọc là 「つま」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "妻"
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
