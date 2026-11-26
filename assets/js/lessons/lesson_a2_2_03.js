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
    "vi": "Chỗ ngồi quầy",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_9faae04446045ab4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_9faae04446045ab4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍸</text>\n</svg>"
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
    "vi": "Bàn (ngồi bệt)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8b1457f420636e24\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8b1457f420636e24)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎎</text>\n</svg>"
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
    "vi": "Ghế hút thuốc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_c67323323dbb7f3c\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_c67323323dbb7f3c)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚬</text>\n</svg>"
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
    "vi": "Ghế cấm hút thuốc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_830d1070fdf86ca0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_830d1070fdf86ca0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚭</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "予約する",
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
    "jp": "注文する",
    "kana": "ちゅうもんする",
    "kanji": "注文する",
    "romaji": "chuumon suru",
    "vi": "Đặt món, gọi món",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7503576c870ac0f4\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7503576c870ac0f4)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📝</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "寄せ鍋",
    "kana": "よせなべ",
    "kanji": "寄せ鍋",
    "romaji": "yosenabe",
    "vi": "Lẩu hải sản",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_f9d8211f0a0faf24\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_f9d8211f0a0faf24)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍲</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "和食",
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
    "jp": "すき焼き",
    "kana": "すきやき",
    "kanji": "すき焼き",
    "romaji": "sukiyaki",
    "vi": "Món lẩu kiểu Nhật",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fce24cd93725fa6f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fce24cd93725fa6f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥩</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "栄養",
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
    "vi": "Ăn chay",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_cff75605eff0f345\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_cff75605eff0f345)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🥦</text>\n</svg>"
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
    "jp": "ウーロン茶",
    "kana": "ウーロンちゃ",
    "kanji": "ウーロン茶",
    "romaji": "u-roncha",
    "vi": "Trà Ô long",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6e3f297af0afb370\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6e3f297af0afb370)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🍵</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "新鮮（な）",
    "kana": "しんせん（な）",
    "kanji": "新鮮（な）",
    "romaji": "shinsen(na)",
    "vi": "Tươi",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1200297115e82d95\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1200297115e82d95)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🐟</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "おすすめ（の N）",
    "kana": "おすすめ",
    "kanji": "おすすめ（の N）",
    "romaji": "osusume (no N)",
    "vi": "Gợi ý, khuyến khích",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8a22e30e195d73c6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8a22e30e195d73c6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👍</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "何名様ですか",
    "kana": "なんめいさまですか",
    "kanji": "何名様ですか",
    "romaji": "nanmei-sama desu ka",
    "vi": "Mấy vị (người) vậy ạ?",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8cdd95c084f60001\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8cdd95c084f60001)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "お決まりですか",
    "kana": "おきまりですか",
    "kanji": "お決まりですか",
    "romaji": "okimari desu ka",
    "vi": "Quý vị quyết định chưa ạ?",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a37c3afd13fdd0b5\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a37c3afd13fdd0b5)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🛎️</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 3 (A2-2)",
    "jp": "苦手（な）",
    "kana": "にがて（な）",
    "kanji": "苦手（な）",
    "romaji": "nigate(na)",
    "vi": "Kém, sợ...",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_19a19d1c9b2a7afb\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_19a19d1c9b2a7afb)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🙅</text>\n</svg>"
  }
];

const VERB_DATA = [
  {
    "masu": "たべます",
    "vi": "Ăn",
    "te": "たべて",
    "form1": "たべてみます (ăn thử)",
    "form2": "たべたことがある (đã từng ăn)",
    "form3": "たべる (thể từ điển)",
    "form2Label": "Trải nghiệm: Vたことがある"
  },
  {
    "masu": "のみます",
    "vi": "Uống",
    "te": "のんで",
    "form1": "のんでみます (uống thử)",
    "form2": "のんだことがある (đã từng uống)",
    "form3": "のむ",
    "form2Label": "Trải nghiệm: Vたことがある"
  },
  {
    "masu": "ちゅうもんします",
    "vi": "Gọi món",
    "te": "ちゅうもんして",
    "form1": "ちゅうもんしてみます (thử gọi món)",
    "form2": "ちゅうもんしたことがある",
    "form3": "ちゅうもんする",
    "form2Label": "Trải nghiệm: Vたことがある"
  },
  {
    "masu": "えらびます",
    "vi": "Chọn lựa",
    "te": "えらんで",
    "form1": "えらんでみます (thử chọn)",
    "form2": "えらんだことがある",
    "form3": "えらぶ",
    "form2Label": "Trải nghiệm: Vたことがある"
  },
  {
    "masu": "たのみます",
    "vi": "Nhờ / gọi món",
    "te": "たのんで",
    "form1": "たのんでみます (thử gọi)",
    "form2": "たのんだことがある",
    "form3": "たのむ",
    "form2Label": "Trải nghiệm: Vたことがある"
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
      "ちゅうい",
      "ようしょく"
    ],
    "correct": 0,
    "explain": "お客さん đọc là 「おきゃくさん」 theo danh sách Kanji chính thức của bài học này.",
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
      "ちゅうい",
      "ようしょく",
      "ようふく",
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
    "q": "Từ Kanji 「注意」 có cách đọc nào?",
    "options": [
      "ちゅうい",
      "ようしょく",
      "ようふく",
      "わしょく"
    ],
    "correct": 0,
    "explain": "注意 đọc là 「ちゅうい」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "注意"
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
    "q": "Từ Kanji 「洋食」 có nghĩa là gì?",
    "options": [
      "Quần áo kiểu Tây",
      "Đồ ăn kiểu Tây",
      "Đồ ăn kiểu Nhật",
      "Quần áo kiểu Nhật"
    ],
    "correct": 1,
    "explain": "洋食 nghĩa là Đồ ăn kiểu Tây.",
    "scopeKanji": "洋食"
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
  },
  {
    "id": 16,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "Điền mẫu chỉ lý do ので: 明日は休み [____]、ゆっくりします。",
    "options": [
      "なので",
      "だので",
      "ので",
      "なで"
    ],
    "correct": 0,
    "explain": "Danh từ ở hiện tại khẳng định nối với ので bằng な: 休みなので. Câu có nghĩa là vì mai được nghỉ nên tôi sẽ nghỉ ngơi thong thả.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 17,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "Dùng mẫu nhấn mạnh ～のは Nです: 私が一番好きな [____] 和食です。",
    "options": [
      "ので",
      "のは",
      "なら",
      "ずつ"
    ],
    "correct": 1,
    "explain": "好き là tính từ な: 好きなのは和食です. の danh từ hóa phần phía trước để xác định món ăn yêu thích nhất.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 18,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "‘Nếu là đồ ăn Nhật thì tôi gợi ý sukiyaki.’ 和食 [____]、すき焼きがおすすめです。",
    "options": [
      "なのは",
      "ずつ",
      "なら",
      "を"
    ],
    "correct": 2,
    "explain": "Nなら nhắc lại chủ đề để đưa gợi ý: 和食なら、すき焼きがおすすめです.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 19,
    "category": "Ngữ pháp",
    "grammarScope": "official",
    "q": "‘Cho tôi bia và trà Ô long, mỗi loại hai ly.’ ビールとウーロン茶を二杯 [____] ください。",
    "options": [
      "ので",
      "なら",
      "のは",
      "ずつ"
    ],
    "correct": 3,
    "explain": "二杯ずつ là mỗi loại hai ly. Đồ uống dùng lượng từ 杯; 人 đếm người, không đếm món ăn hay ly nước.",
    "reviewVersion": "a22-practice20-v1"
  },
  {
    "id": 20,
    "category": "Chữ Hán",
    "scopeKanji": "注文",
    "q": "「注文」の読み方はどれですか。",
    "options": [
      "ちゅうい",
      "ようしょく",
      "ほうほう",
      "ちゅうもん"
    ],
    "correct": 3,
    "explain": "注文 đọc là ちゅうもん, nghĩa là gọi món/đặt hàng.",
    "reviewVersion": "a22-practice20-v1"
  }
];

const SENTENCE_PRACTICE_DATA = [
  {
    "id": 1,
    "vi": "Khách đang ngồi ở quầy.",
    "jp": "お客さんはカウンターに座っています。",
    "requireKanji": true,
    "accepted": [
      "お客さんはカウンター席に座っています。"
    ]
  },
  {
    "id": 2,
    "vi": "Tôi đã đặt chiếc bàn cạnh cửa sổ.",
    "jp": "窓のそばのテーブルを予約しました。",
    "requireKanji": true,
    "accepted": [
      "窓際のテーブルを予約しました。"
    ]
  },
  {
    "id": 3,
    "vi": "Khách đang ngồi trong phòng trải chiếu tatami.",
    "jp": "お客さんは座敷に座っています。",
    "requireKanji": true,
    "accepted": [
      "お客さんはざしきに座っています。"
    ]
  },
  {
    "id": 4,
    "vi": "Ghế hút thuốc ở bên phải.",
    "jp": "喫煙席は右にあります。",
    "requireKanji": true,
    "accepted": [
      "喫煙席は右側にあります。"
    ]
  },
  {
    "id": 5,
    "vi": "Cho tôi chỗ ngồi không hút thuốc.",
    "jp": "禁煙席をお願いします。",
    "requireKanji": true,
    "accepted": [
      "禁煙席にしてください。"
    ]
  },
  {
    "id": 6,
    "vi": "Tôi đã đặt chỗ cho bốn người.",
    "jp": "四人分の席を予約しました。",
    "requireKanji": true,
    "accepted": [
      "四名分の席を予約しました。",
      "四人の席を予約しました。"
    ]
  },
  {
    "id": 7,
    "vi": "Chúng tôi đã gọi món lẩu thập cẩm.",
    "jp": "私たちは寄せ鍋を注文しました。",
    "requireKanji": true,
    "accepted": [
      "私たちはよせ鍋を注文しました。"
    ]
  },
  {
    "id": 8,
    "vi": "Món ăn kiểu Nhật ở đây rất nổi tiếng.",
    "jp": "ここの和食はとても有名です。",
    "requireKanji": true,
    "accepted": [
      "ここの日本料理はとても有名です。"
    ]
  },
  {
    "id": 9,
    "vi": "Vì tôi thích sukiyaki nên tôi sẽ gọi món đó.",
    "jp": "すき焼きが好きなので、注文します。",
    "requireKanji": true,
    "accepted": [
      "すき焼きが好きなので、それを注文します。"
    ]
  },
  {
    "id": 10,
    "vi": "Món ăn này bổ dưỡng.",
    "jp": "この料理は栄養があります。",
    "requireKanji": true,
    "accepted": [
      "この料理は栄養が豊富です。"
    ]
  },
  {
    "id": 11,
    "vi": "Nếu ăn chay thì tôi gợi ý món rau này.",
    "jp": "ベジタリアンなら、この野菜料理がおすすめです。",
    "requireKanji": true,
    "accepted": [
      "ベジタリアンなら、この野菜の料理がおすすめです。"
    ]
  },
  {
    "id": 12,
    "vi": "Vì không thích cua nên tôi không ăn.",
    "jp": "蟹が好きではないので、食べません。",
    "requireKanji": true,
    "accepted": [
      "かにが好きではないので、食べません。",
      "かにが好きじゃないので、食べません。"
    ]
  },
  {
    "id": 13,
    "vi": "Tôm của nhà hàng này rất tươi.",
    "jp": "この店の海老はとても新鮮です。",
    "requireKanji": true,
    "accepted": [
      "この店のえびはとても新鮮です。"
    ]
  },
  {
    "id": 14,
    "vi": "Tôi gọi nước ngọt.",
    "jp": "ソフトドリンクを注文します。",
    "requireKanji": true,
    "accepted": [
      "ソフトドリンクを頼みます。"
    ]
  },
  {
    "id": 15,
    "vi": "Trà Ô long ở đây rất ngon.",
    "jp": "ここのウーロン茶はとてもおいしいです。",
    "requireKanji": true,
    "accepted": [
      "ここのウーロン茶はとても美味しいです。",
      "ここの烏龍茶はとてもおいしいです。",
      "ここの烏龍茶はとても美味しいです。"
    ]
  },
  {
    "id": 16,
    "vi": "Xin hỏi quý khách có mấy vị ạ?",
    "jp": "何名様ですか。",
    "requireKanji": true,
    "accepted": [
      "何名さまですか。"
    ]
  },
  {
    "id": 17,
    "vi": "Quý khách đã chọn món xong chưa ạ?",
    "jp": "お決まりですか。",
    "requireKanji": true,
    "accepted": [
      "ご注文はお決まりですか。"
    ]
  },
  {
    "id": 18,
    "vi": "Tôi ăn cay kém.",
    "jp": "私は辛い料理が苦手です。",
    "requireKanji": true,
    "accepted": [
      "私は辛い食べ物が苦手です。",
      "私は辛いものが苦手です。"
    ]
  },
  {
    "id": 19,
    "vi": "Khách đã gọi món thịt bò.",
    "jp": "お客さんは牛肉を注文しました。",
    "requireKanji": true,
    "accepted": [
      "お客さんは牛肉を頼みました。"
    ]
  },
  {
    "id": 20,
    "vi": "Vì món ăn nguội nên tôi hâm nóng nó.",
    "jp": "料理が冷たいので、温めます。",
    "requireKanji": true,
    "accepted": [
      "料理が冷たいので、あたためます。"
    ]
  },
  {
    "id": 21,
    "vi": "Vì nhà hàng nổi tiếng nên khách rất đông.",
    "jp": "店が有名なので、お客さんがたくさんいます。",
    "requireKanji": true,
    "accepted": [
      "店が有名なので、たくさんのお客さんがいます。"
    ]
  },
  {
    "id": 22,
    "vi": "Vì hôm nay là sinh nhật nên chúng tôi ăn ở nhà hàng.",
    "jp": "今日は誕生日なので、レストランで食べます。",
    "requireKanji": true,
    "accepted": [
      "今日は誕生日なので、レストランで食事をします。"
    ]
  },
  {
    "id": 23,
    "vi": "Món ăn tôi thích nhất là đồ ăn Nhật.",
    "jp": "私が一番好きなのは和食です。",
    "requireKanji": true,
    "accepted": [
      "私が一番好きなのは日本料理です。"
    ]
  },
  {
    "id": 24,
    "vi": "Món tôi đã gọi là lẩu thập cẩm.",
    "jp": "私が注文したのは寄せ鍋です。",
    "requireKanji": true,
    "accepted": [
      "私が頼んだのは寄せ鍋です。"
    ]
  },
  {
    "id": 25,
    "vi": "Nếu là đồ ăn Tây thì tôi gợi ý món này.",
    "jp": "洋食なら、この料理がおすすめです。",
    "requireKanji": true,
    "accepted": [
      "洋食なら、この料理をおすすめします。"
    ]
  },
  {
    "id": 26,
    "vi": "Nếu là quần áo kiểu Nhật thì tôi thích kimono.",
    "jp": "和服なら、着物が好きです。",
    "requireKanji": true,
    "accepted": [
      "和服なら、きものが好きです。"
    ]
  },
  {
    "id": 27,
    "vi": "Nhà hàng này có một phòng kiểu Nhật.",
    "jp": "この店には和室があります。",
    "requireKanji": true,
    "accepted": [
      "この店には日本式の部屋があります。"
    ]
  },
  {
    "id": 28,
    "vi": "Cách gọi món ở nhà hàng này rất đơn giản.",
    "jp": "この店の注文の方法は簡単です。",
    "requireKanji": true,
    "accepted": [
      "この店での注文の方法は簡単です。",
      "この店の注文方法は簡単です。"
    ]
  },
  {
    "id": 29,
    "vi": "Vì trẻ em đang lớn nên dinh dưỡng rất quan trọng.",
    "jp": "子どもは成長しているので、栄養が大切です。",
    "requireKanji": true,
    "accepted": [
      "子供は成長しているので、栄養が大切です。"
    ]
  },
  {
    "id": 30,
    "vi": "Sữa bò lạnh nên tôi hâm nóng.",
    "jp": "牛乳が冷たいので、温めます。",
    "requireKanji": true,
    "accepted": [
      "牛乳が冷たいので、あたためます。"
    ]
  },
  {
    "id": 31,
    "vi": "Phòng kiểu Nhật ở nhà hàng này có tính phí sử dụng.",
    "jp": "この店の和室は有料です。",
    "requireKanji": true,
    "accepted": [
      "この店では和室の利用は有料です。"
    ]
  },
  {
    "id": 32,
    "vi": "Cửa hàng này bán quần áo kiểu Tây.",
    "jp": "この店では洋服を売っています。",
    "requireKanji": true,
    "accepted": [
      "この店では洋服を販売しています。"
    ]
  },
  {
    "id": 33,
    "vi": "Hãy chú ý đến cách ăn món này.",
    "jp": "この料理の食べ方に注意してください。",
    "requireKanji": true,
    "accepted": [
      "この料理の食べ方に気をつけてください。"
    ]
  },
  {
    "id": 34,
    "vi": "Tôi đã ăn món ăn của địa phương này.",
    "jp": "この地方の料理を食べました。",
    "requireKanji": true,
    "accepted": [
      "この地域の料理を食べました。"
    ]
  },
  {
    "id": 35,
    "vi": "Vì hôm qua là ngày nghỉ nên tôi đã ăn ở nhà hàng.",
    "jp": "昨日は休みだったので、レストランで食べました。",
    "requireKanji": true,
    "accepted": [
      "昨日は休日だったので、レストランで食べました。"
    ]
  },
  {
    "id": 36,
    "vi": "Món cay nhất ở nhà hàng này là cà ri.",
    "jp": "この店で一番辛いのはカレーです。",
    "requireKanji": true,
    "accepted": [
      "この店で一番辛い料理はカレーです。"
    ]
  },
  {
    "id": 37,
    "vi": "Vì sữa bò đã lạnh rồi nên tôi sẽ uống ngay.",
    "jp": "牛乳が冷えたので、すぐ飲みます。",
    "requireKanji": true,
    "accepted": [
      "牛乳が冷えたので、すぐに飲みます。"
    ]
  },
  {
    "id": 38,
    "vi": "Tôi gọi bia và nước ngọt, mỗi thứ hai ly.",
    "jp": "ビールとソフトドリンクを二杯ずつ注文します。",
    "requireKanji": true,
    "accepted": [
      "ビールとソフトドリンクを二杯ずつ頼みます。"
    ]
  },
  {
    "id": 39,
    "vi": "Tôi sẽ làm lạnh nước và sữa bò, mỗi loại một chai.",
    "jp": "水と牛乳を一本ずつ冷やします。",
    "requireKanji": true,
    "accepted": [
      "水と牛乳をそれぞれ一本ずつ冷やします。"
    ]
  },
  {
    "id": 40,
    "vi": "Nếu là lẩu sukiyaki, thịt bò tươi là ngon nhất.",
    "jp": "すき焼きなら、新鮮な牛肉が一番です。",
    "requireKanji": true,
    "accepted": [
      "すき焼きなら、新鮮な牛肉が一番おいしいです。"
    ]
  }
];

const KANJI_PRACTICE_DATA = [
  {
    "id": "official-3-1",
    "word": "お客さん",
    "kana": "おきゃくさん",
    "mean": "Khách hàng",
    "accepted": []
  },
  {
    "id": "official-3-2",
    "word": "注文",
    "kana": "ちゅうもん",
    "mean": "Order, gọi món, đặt hàng",
    "accepted": []
  },
  {
    "id": "official-3-3",
    "word": "注意",
    "kana": "ちゅうい",
    "mean": "Chú ý, nhắc nhở",
    "accepted": []
  },
  {
    "id": "official-3-4",
    "word": "洋食",
    "kana": "ようしょく",
    "mean": "Đồ ăn kiểu Tây",
    "accepted": []
  },
  {
    "id": "official-3-5",
    "word": "洋服",
    "kana": "ようふく",
    "mean": "Quần áo kiểu Tây",
    "accepted": []
  },
  {
    "id": "official-3-6",
    "word": "和食",
    "kana": "わしょく",
    "mean": "Đồ ăn kiểu Nhật",
    "accepted": []
  },
  {
    "id": "official-3-7",
    "word": "和服",
    "kana": "わふく",
    "mean": "Quần áo kiểu Nhật",
    "accepted": []
  },
  {
    "id": "official-3-8",
    "word": "和室",
    "kana": "わしつ",
    "mean": "Phòng kiểu Nhật",
    "accepted": []
  },
  {
    "id": "official-3-9",
    "word": "方",
    "kana": "かた",
    "mean": "Vị, cách làm~",
    "accepted": []
  },
  {
    "id": "official-3-10",
    "word": "地方",
    "kana": "ちほう",
    "mean": "Địa phương",
    "accepted": []
  },
  {
    "id": "official-3-11",
    "word": "方法",
    "kana": "ほうほう",
    "mean": "Phương pháp, cách thức",
    "accepted": []
  },
  {
    "id": "official-3-12",
    "word": "有名",
    "kana": "ゆうめい",
    "mean": "Nổi tiếng",
    "accepted": []
  },
  {
    "id": "official-3-13",
    "word": "有料",
    "kana": "ゆうりょう",
    "mean": "Có phí, mất phí",
    "accepted": []
  },
  {
    "id": "official-3-14",
    "word": "牛肉",
    "kana": "ぎゅうにく",
    "mean": "Thịt bò",
    "accepted": []
  },
  {
    "id": "official-3-15",
    "word": "牛乳",
    "kana": "ぎゅうにゅう",
    "mean": "Sữa bò",
    "accepted": []
  },
  {
    "id": "official-3-16",
    "word": "冷たい",
    "kana": "つめたい",
    "mean": "Lạnh (cảm giác)",
    "accepted": []
  },
  {
    "id": "official-3-17",
    "word": "冷える",
    "kana": "ひえる",
    "mean": "Lạnh, cóng",
    "accepted": []
  },
  {
    "id": "official-3-18",
    "word": "冷やす",
    "kana": "ひやす",
    "mean": "Làm lạnh",
    "accepted": []
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
    const elForm2Label = document.getElementById('morphForm2Label');
    const elForm3 = document.getElementById('morphMashou');

    if (elMasu) elMasu.textContent = v.masu || '---';
    if (elVi) elVi.textContent = v.vi || '---';
    if (elTe) elTe.textContent = v.te || '---';
    if (elForm1) elForm1.textContent = v.form1 || '---';
    if (elForm2) elForm2.textContent = v.form2 || '---';
    if (elForm2Label) elForm2Label.textContent = v.form2Label || 'Ví dụ chia thể (bổ trợ)';
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
        const revision = q.reviewVersion || 'a22-reviewed-v2';
        const optsHtml = q.options.map((opt, oIdx) => `
            <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${qIdx}, ${oIdx}, '${revision}')">${escapeLessonText(opt)}</button>
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
    const q = QUIZ_DATA[qIdx];
    if (!q || revision !== (q.reviewVersion || 'a22-reviewed-v2') || btn.disabled) return;
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
if (typeof SENTENCE_PRACTICE_DATA !== "undefined") window.SENTENCE_PRACTICE_DATA = SENTENCE_PRACTICE_DATA;
if (typeof KANJI_PRACTICE_DATA !== "undefined") window.KANJI_PRACTICE_DATA = KANJI_PRACTICE_DATA;
