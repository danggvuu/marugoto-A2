/* Marugoto A2-2 Bài 12 (A2-2) - Extracted Data & Logic */
const VOCAB_DATA = [
  {
    "id": 1,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "モデル",
    "kana": "モデル",
    "kanji": "モデル",
    "romaji": "moderu",
    "vi": "Mẫu mã, kiểu loại",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_edc5c199fa8d3976\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_edc5c199fa8d3976)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📱</text>\n</svg>"
  },
  {
    "id": 2,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "重さ",
    "kana": "おもさ",
    "kanji": "重さ",
    "romaji": "omosa",
    "vi": "Cân nặng, khối lượng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_26c1cc0fee5b4e4a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_26c1cc0fee5b4e4a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚖️</text>\n</svg>"
  },
  {
    "id": 3,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "大きさ",
    "kana": "おおきさ",
    "kanji": "大きさ",
    "romaji": "ookisa",
    "vi": "Độ lớn, kích thước",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_3e5800100a7238ca\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_3e5800100a7238ca)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📐</text>\n</svg>"
  },
  {
    "id": 4,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "機能",
    "kana": "きのう",
    "kanji": "機能",
    "romaji": "kinou",
    "vi": "Chức năng, tính năng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_ebe64c2688843d9e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_ebe64c2688843d9e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⚙️</text>\n</svg>"
  },
  {
    "id": 5,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "値段",
    "kana": "ねだん",
    "kanji": "値段",
    "romaji": "nedan",
    "vi": "Giá cả",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a8d99322c004c529\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a8d99322c004c529)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏷️</text>\n</svg>"
  },
  {
    "id": 6,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "税込",
    "kana": "ぜいこみ",
    "kanji": "税込",
    "romaji": "zeikomi",
    "vi": "Đã bao gồm thuế",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_61cde9e68f186c92\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_61cde9e68f186c92)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧾</text>\n</svg>"
  },
  {
    "id": 7,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "翌日",
    "kana": "よくじつ",
    "kanji": "翌日",
    "romaji": "yokujitsu",
    "vi": "Ngày hôm sau",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_618d596755a35b01\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_618d596755a35b01)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📆</text>\n</svg>"
  },
  {
    "id": 8,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "送料無料",
    "kana": "そうりょうむりょう",
    "kanji": "送料無料",
    "romaji": "souryou muryou",
    "vi": "Miễn phí vận chuyển",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_5fd8a314e65e92b0\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_5fd8a314e65e92b0)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🚚</text>\n</svg>"
  },
  {
    "id": 9,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "届きます",
    "kana": "とどきます",
    "kanji": "届きます",
    "romaji": "todokimasu",
    "vi": "Được giao đến",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_fd0d6843bd5db8f2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_fd0d6843bd5db8f2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n</svg>"
  },
  {
    "id": 10,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "省エネ",
    "kana": "しょうエネ",
    "kanji": "省エネ",
    "romaji": "shouene",
    "vi": "Tiết kiệm năng lượng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_e5b9d6ad4b144c09\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_e5b9d6ad4b144c09)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌱</text>\n</svg>"
  },
  {
    "id": 11,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "デザイン",
    "kana": "デザイン",
    "kanji": "デザイン",
    "romaji": "dezain",
    "vi": "Thiết kế, kiểu dáng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_a0167384afbacd6f\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_a0167384afbacd6f)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🎨</text>\n</svg>"
  },
  {
    "id": 12,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "カラー",
    "kana": "カラー",
    "kanji": "カラー",
    "romaji": "kara-",
    "vi": "Màu sắc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_bd938d6bcff0b351\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_bd938d6bcff0b351)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🌈</text>\n</svg>"
  },
  {
    "id": 13,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "レビュー",
    "kana": "レビュー",
    "kanji": "レビュー",
    "romaji": "rebyu-",
    "vi": "Đánh giá, nhận xét (review)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_53502d535c2950c8\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_53502d535c2950c8)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">⭐</text>\n</svg>"
  },
  {
    "id": 14,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "重い",
    "kana": "おもい",
    "kanji": "重い",
    "romaji": "omoi",
    "vi": "Nặng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_1467c839eb65b59b\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_1467c839eb65b59b)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🏋️</text>\n</svg>"
  },
  {
    "id": 15,
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
    "id": 16,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "複雑（な）",
    "kana": "ふくざつ（な）",
    "kanji": "複雑（な）",
    "romaji": "fukuzatsu(na)",
    "vi": "Phức tạp",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6e3ddbf767910672\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6e3ddbf767910672)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🧩</text>\n</svg>"
  },
  {
    "id": 17,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "気に入ります",
    "kana": "きにいります",
    "kanji": "気に入ります",
    "romaji": "ki ni irimasu",
    "vi": "Yêu thích, ưng ý",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_d95927451b83cb8e\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_d95927451b83cb8e)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">💖</text>\n</svg>"
  },
  {
    "id": 18,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "満足（します）",
    "kana": "まんぞく（します）",
    "kanji": "満足（します）",
    "romaji": "manzoku(shimasu)",
    "vi": "Hài lòng, thỏa mãn",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_8cdb82b1887c67d6\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_8cdb82b1887c67d6)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😊</text>\n</svg>"
  },
  {
    "id": 19,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "ごみを捨てます",
    "kana": "ごみをすてます",
    "kanji": "ごみを捨てます",
    "romaji": "gomi o sutemasu",
    "vi": "Vứt rác",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_70fc1ed58d62485a\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_70fc1ed58d62485a)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🗑️</text>\n</svg>"
  },
  {
    "id": 20,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "びっくり（します）",
    "kana": "びっくり（します）",
    "kanji": "びっくり（します）",
    "romaji": "bikkuri(shimasu)",
    "vi": "Bất ngờ, kinh ngạc",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_0011cee271757080\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_0011cee271757080)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">😲</text>\n</svg>"
  },
  {
    "id": 21,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "ユーザー",
    "kana": "ユーザー",
    "kanji": "ユーザー",
    "romaji": "yu-za-",
    "vi": "Người dùng, khách hàng",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_6d3256a76aabcc45\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_6d3256a76aabcc45)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">👤</text>\n</svg>"
  },
  {
    "id": 22,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "モード",
    "kana": "モード",
    "kanji": "モード",
    "romaji": "mo-do",
    "vi": "Chế độ (hoạt động)",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_05503948df1839fd\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_05503948df1839fd)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">🔄</text>\n</svg>"
  },
  {
    "id": 23,
    "cat": "vocab",
    "catName": "Từ Vựng",
    "badge": "Bài 12 (A2-2)",
    "jp": "うるさい",
    "kana": "うるさい",
    "kanji": "うるさい",
    "romaji": "urusai",
    "vi": "Ồn ào",
    "svg": "<svg viewBox=\"0 0 240 120\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"g_7e426c4c36516bd2\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#7c3aed\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"120\" rx=\"14\" fill=\"url(#g_7e426c4c36516bd2)\"/>\n  <circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"rgba(255,255,255,0.2)\"/>\n  <text x=\"120\" y=\"60\" text-anchor=\"middle\" font-size=\"32\">📢</text>\n</svg>"
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
    "explain": "Cấu trúc so sánh hơn: 『N1 の ほうが N2 より A』 ➔ 「ほう」.",
    "grammarScope": "official"
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
    "explain": "Hỏi so sánh giữa 2 đối tượng dùng từ để hỏi: 『どちら (どっち)』.",
    "grammarScope": "official"
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
    "category": "Ngữ pháp",
    "q": "このアイロンは重 [____]、使いにくいです。",
    "options": [
      "やすくて",
      "にくくて",
      "すぎる",
      "すぎて"
    ],
    "correct": 3,
    "explain": "い形容詞 bỏ い + すぎて: 重すぎて.",
    "grammarScope": "official"
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
    "q": "Từ Kanji 「機能」 có cách đọc nào?",
    "options": [
      "きのう",
      "しょうエネ",
      "にほんせい",
      "おもい"
    ],
    "correct": 0,
    "explain": "機能 đọc là 「きのう」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "機能"
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
    "category": "Ngữ pháp",
    "q": "このアイロンは軽くて、[____] やすいです。",
    "options": [
      "使って",
      "使う",
      "使った",
      "使い"
    ],
    "correct": 3,
    "explain": "Vます bỏ ます + やすい: 使いやすい.",
    "grammarScope": "official"
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
    "explain": "Tàu điện thì đúng giờ hơn xe buýt: 電車のほうが.",
    "grammarScope": "official"
  },
  {
    "id": 10,
    "category": "Chữ Hán",
    "q": "Từ Kanji 「省エネ」 có cách đọc nào?",
    "options": [
      "にほんせい",
      "おもい",
      "しょうエネ",
      "かるい"
    ],
    "correct": 2,
    "explain": "省エネ đọc là 「しょうエネ」 theo danh sách Kanji chính thức của bài học này.",
    "scopeKanji": "省エネ"
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
    "q": "Từ Kanji 「日本製」 có nghĩa là gì?",
    "options": [
      "Nặng",
      "Nhẹ",
      "Yên tĩnh, êm",
      "Sản xuất tại Nhật"
    ],
    "correct": 3,
    "explain": "日本製 nghĩa là Sản xuất tại Nhật.",
    "scopeKanji": "日本製"
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
    "q": "Từ Kanji 「重い」 có nghĩa là gì?",
    "options": [
      "Nặng",
      "Nhẹ",
      "Yên tĩnh, êm",
      "Nhanh, sớm"
    ],
    "correct": 0,
    "explain": "重い nghĩa là Nặng.",
    "scopeKanji": "重い"
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
