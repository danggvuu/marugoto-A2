/* Marugoto A2-2 Bài 3 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "カウンター",
    "kana": "カウンター",
    "kanji": "カウンター",
    "romaji": "kaunta-",
    "vi": "Chỗ ngồi quầy, quầy bar",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_491dc8b3c46c42cc\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_491dc8b3c46c42cc)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍸</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "テーブル",
    "kana": "テーブル",
    "kanji": "テーブル",
    "romaji": "te-buru",
    "vi": "Bàn (ngồi cùng ghế)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ed0e5e066a7f63ac\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ed0e5e066a7f63ac)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🪑</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "ざしき",
    "kana": "ざしき",
    "kanji": "座敷",
    "romaji": "zashiki",
    "vi": "Chỗ ngồi bệt (chiếu tatami)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_760cb16f84cbae38\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_760cb16f84cbae38)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎎</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "きつえんせき",
    "kana": "きつえんせき",
    "kanji": "喫煙席",
    "romaji": "kitsuenseki",
    "vi": "Ghế/khu vực hút thuốc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_2a8177a976187984\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_2a8177a976187984)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚬</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "きんえんせき",
    "kana": "きんえんせき",
    "kanji": "禁煙席",
    "romaji": "kin'enseki",
    "vi": "Ghế/khu vực cấm hút thuốc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_349cc0e6ce50bf92\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_349cc0e6ce50bf92)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚭</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "よやくする",
    "kana": "よやくする",
    "kanji": "予約する",
    "romaji": "yoyaku suru",
    "vi": "Đặt trước, hẹn lịch",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d17022b708502931\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d17022b708502931)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📅</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "ちゅうもんする",
    "kana": "ちゅうもんする",
    "kanji": "注文する",
    "romaji": "chuumon suru",
    "vi": "Đặt món, gọi món",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7503576c870ac0f4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7503576c870ac0f4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📋</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "よせなべ",
    "kana": "よせなべ",
    "kanji": "寄せ鍋",
    "romaji": "yosenabe",
    "vi": "Lẩu hải sản thập cẩm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ef2ce9b9dd501603\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ef2ce9b9dd501603)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍲</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "わしょく",
    "kana": "わしょく",
    "kanji": "和食",
    "romaji": "washoku",
    "vi": "Món ăn kiểu Nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0823ead6a5a24a2f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0823ead6a5a24a2f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍱</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "すきやき",
    "kana": "すきやき",
    "kanji": "すき焼き",
    "romaji": "sukiyaki",
    "vi": "Món lẩu bò Sukiyaki",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_4ed715de14378e1e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_4ed715de14378e1e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥩</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "えいよう",
    "kana": "えいよう",
    "kanji": "栄養",
    "romaji": "eiyou",
    "vi": "Dinh dưỡng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3c897893af4beed4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3c897893af4beed4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥗</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "ベジタリアン",
    "kana": "ベジタリアン",
    "kanji": "ベジタリアン",
    "romaji": "bejitarian",
    "vi": "Người ăn chay, món chay",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d7dbf5cbfb3e9ca8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d7dbf5cbfb3e9ca8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥬</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "かに",
    "kana": "かに",
    "kanji": "蟹",
    "romaji": "kani",
    "vi": "Cua",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_de77879b88cab8f3\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_de77879b88cab8f3)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🦀</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "えび",
    "kana": "えび",
    "kanji": "海老",
    "romaji": "ebi",
    "vi": "Tôm",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_b7ce3cde79e0021b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_b7ce3cde79e0021b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🦐</text>\n</svg>"
  },
  {
    "id": 15,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "ソフトドリンク",
    "kana": "ソフトドリンク",
    "kanji": "ソフトドリンク",
    "romaji": "sofuto dorinku",
    "vi": "Đồ uống nhẹ, nước ngọt",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c4d849c15ea6fbe5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c4d849c15ea6fbe5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥤</text>\n</svg>"
  },
  {
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "ウーロンちゃ",
    "kana": "ウーロンちゃ",
    "kanji": "烏龍茶",
    "romaji": "u-roncha",
    "vi": "Trà Ô long",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6e3f297af0afb370\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6e3f297af0afb370)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍵</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "しんせん（な）",
    "kana": "しんせん（な）",
    "kanji": "新鮮（な）",
    "romaji": "shinsen(na)",
    "vi": "Tươi, tươi sống",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c42212a36daa3fd2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c42212a36daa3fd2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐟</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "おすすめ",
    "kana": "おすすめ",
    "kanji": "おすすめ",
    "romaji": "osusume",
    "vi": "Gợi ý, món khuyên dùng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cd9ca8922a402fee\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cd9ca8922a402fee)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👍</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "なんめいさまですか",
    "kana": "なんめいさまですか",
    "kanji": "何名様ですか",
    "romaji": "nanmeisama desu ka",
    "vi": "Mấy vị (người) vậy ạ?",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8cdd95c084f60001\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8cdd95c084f60001)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "おきまりですか",
    "kana": "おきまりですか",
    "kanji": "お決まりですか",
    "romaji": "okimari desu ka",
    "vi": "Quý khách quyết định món chưa ạ?",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e8041bcaa68f1490\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e8041bcaa68f1490)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛎️</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "にがて（な）",
    "kana": "にがて（な）",
    "kanji": "苦手（な）",
    "romaji": "nigate(na)",
    "vi": "Kém, không thích, sợ ăn...",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_67f317a3706070c6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_67f317a3706070c6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😣</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "たべます",
    "vi": "Ăn",
    "te": "たべて",
    "form1": "たべてみます (ăn thử)",
    "form2": "たべたことがある (đã từng ăn)",
    "form3": "たべる (thể từ điển)"
  },
  {
    "masu": "のみます",
    "vi": "Uống",
    "te": "のんで",
    "form1": "のんでみます (uống thử)",
    "form2": "のんだことがある (đã từng uống)",
    "form3": "のむ"
  },
  {
    "masu": "ちゅうもんします",
    "vi": "Gọi món",
    "te": "ちゅうもんして",
    "form1": "ちゅうもんしてみます (thử gọi món)",
    "form2": "ちゅうもんしたことがある",
    "form3": "ちゅうもんする"
  },
  {
    "masu": "えらびます",
    "vi": "Chọn lựa",
    "te": "えらんで",
    "form1": "えらんでみます (thử chọn)",
    "form2": "えらんだことがある",
    "form3": "えらぶ"
  },
  {
    "masu": "たのみます",
    "vi": "Nhờ / gọi món",
    "te": "たのんで",
    "form1": "たのんでみます (thử gọi)",
    "form2": "たのんだことがある",
    "form3": "たのむ"
  }
];

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Ngữ pháp",
    "q": "この店はおいしい [____]、よく来ます。",
    "options": [
      "のは",
      "なら",
      "ずつ",
      "ので"
    ],
    "correct": 3,
    "explain": "ので nối lý do với kết quả: ngon nên thường đến.",
    "grammarScope": "official"
  },
  {
    "id": 2,
    "category": "Ngữ pháp",
    "q": "私が好きな [____]、ステーキです。",
    "options": [
      "ので",
      "なら",
      "のは",
      "ずつ"
    ],
    "correct": 2,
    "explain": "のは danh từ hóa mệnh đề làm chủ đề câu.",
    "grammarScope": "official"
  },
  {
    "id": 3,
    "category": "Từ vựng",
    "q": "レモンは とても [____] ですが、体によいです。",
    "options": [
      "あまい",
      "すっぱい",
      "からい",
      "にがい"
    ],
    "correct": 1,
    "explain": "Chanh (レモン) có vị chua, tiếng Nhật là 「酸っぱい (すっぱい)」."
  },
  {
    "id": 4,
    "category": "Ngữ pháp",
    "q": "野菜 [____]、このサラダがいいですよ。",
    "options": [
      "なら",
      "ので",
      "のは",
      "ずつ"
    ],
    "correct": 0,
    "explain": "なら nêu gợi ý theo chủ đề được nhắc tới.",
    "grammarScope": "official"
  },
  {
    "id": 5,
    "category": "Từ vựng",
    "q": "ビールや ジュースを 持って、みんなで 「[____]！」 と 言って グラスを 合わせます。",
    "options": [
      "ごちそうさま",
      "かんぱい",
      "いただきます",
      "いらっしゃいませ"
    ],
    "correct": 1,
    "explain": "Trước khi bắt đầu uống trong tiệc, mọi người cùng hô cạn ly: 「乾杯 (かんぱい)」."
  },
  {
    "id": 6,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「お客さん」 có cách đọc nào?",
    "options": [
      "おきゃくさん",
      "ちゅうもん",
      "ようしょく",
      "わしょく"
    ],
    "correct": 0,
    "explain": "お客さん đọc là 「おきゃくさん」 mang nghĩa Khách hàng.",
    "scopeKanji": "お客さん"
  },
  {
    "id": 7,
    "category": "Từ vựng",
    "q": "この スープは 塩が 多すぎて、とても [____] です。",
    "options": [
      "あまい",
      "しょっぱい",
      "にがい",
      "すっぱい"
    ],
    "correct": 1,
    "explain": "Nhiều muối (塩) quá thì vị mặn chát: 「しょっぱい」."
  },
  {
    "id": 8,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「注文」 có cách đọc nào?",
    "options": [
      "ようしょく",
      "わしょく",
      "ぎゅうにく",
      "ちゅうもん"
    ],
    "correct": 3,
    "explain": "注文 đọc là 「ちゅうもん」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "注文"
  },
  {
    "id": 9,
    "category": "Ngữ pháp",
    "q": "コーヒーを二つ [____] お願いします。",
    "options": [
      "ので",
      "なら",
      "のは",
      "ずつ"
    ],
    "correct": 3,
    "explain": "ずつ diễn tả phân chia theo từng đơn vị.",
    "grammarScope": "official"
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「洋食」 có cách đọc nào?",
    "options": [
      "ようしょく",
      "わしょく",
      "ぎゅうにく",
      "ちほう"
    ],
    "correct": 0,
    "explain": "洋食 đọc là 「ようしょく」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "洋食"
  },
  {
    "id": 11,
    "category": "Từ vựng",
    "q": "ごはん、みそ汁、魚、小鉢が セットに なっている 料理を [____] と 言います。",
    "options": [
      "デザート",
      "ちゅうもん",
      "ていしょく",
      "かいけい"
    ],
    "correct": 2,
    "explain": "Bữa ăn kèm đầy đủ cơm, canh miso, thức ăn thành phần trọn gói gọi là 「定食 (ていしょく)」."
  },
  {
    "id": 12,
    "category": "Từ vựng",
    "q": "食事が 終わったあとで、甘い アイスクリームなどの [____] を 食べます。",
    "options": [
      "さしみ",
      "メニュー",
      "デザート",
      "いざかや"
    ],
    "correct": 2,
    "explain": "Món ngọt tráng miệng sau bữa ăn gọi là 「デザート (dessert)」."
  },
  {
    "id": 13,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「和食」 có nghĩa là gì?",
    "options": [
      "Thịt bò",
      "Đồ ăn kiểu Nhật",
      "Địa phương",
      "Nổi tiếng"
    ],
    "correct": 1,
    "explain": "和食 nghĩa là Đồ ăn kiểu Nhật.",
    "scopeKanji": "和食"
  },
  {
    "id": 14,
    "category": "Hội thoại",
    "q": "食事代を 支払うときに、店員に 「お[____]、お願いします」 と 言います。",
    "options": [
      "かいけい",
      "ちゅうもん",
      "せき",
      "にんき"
    ],
    "correct": 0,
    "explain": "Khi muốn thanh toán tính tiền ở quán Nhật: 「お会計（かいけい）、お願いします」."
  },
  {
    "id": 15,
    "category": "Ngữ pháp",
    "q": "一つ [____] お願いします。",
    "options": [
      "ので",
      "なら",
      "ずつ",
      "のは"
    ],
    "correct": 2,
    "explain": "ずつ diễn tả phân chia theo từng đơn vị.",
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
