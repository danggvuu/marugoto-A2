/* Extracted data & interactive logic for Marugoto A2 Lesson 18 */
const VOCAB_DATA = [{"id": 1, "cat": "event", "catName": "Sự kiện đời người", "badge": "Kết hôn", "jp": "けっこん", "kana": "けっこん", "kanji": "結婚", "romaji": "kekkon", "vi": "Kết hôn", "exJp": "友だちの 結婚式に 参加します。", "exVi": "Tham dự lễ cưới của bạn thân.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_1_74178\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#db2777\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_1_74178\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_1_74178)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_1_74178)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">結婚</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">💍</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">KẾT HÔN</text>\n</svg>"}, {"id": 2, "cat": "event", "catName": "Sự kiện đời người", "badge": "Chuyển nhà", "jp": "ひっこし", "kana": "ひっこし", "kanji": "引っ越し", "romaji": "hikkoshi", "vi": "Chuyển nhà", "exJp": "来月 新しいアパートに 引っ越しします。", "exVi": "Tháng sau tôi sẽ chuyển sang căn hộ mới.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_2_47568\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_2_47568\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_2_47568)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_2_47568)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">引っ越し</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">📦</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">CHUYỂN NHÀ</text>\n</svg>"}, {"id": 3, "cat": "event", "catName": "Sự kiện đời người", "badge": "Bắt đầu đi làm", "jp": "しゅうしょく", "kana": "しゅうしょく", "kanji": "就職", "romaji": "shuushoku", "vi": "Bắt đầu đi làm, có việc làm", "exJp": "息子の 就職が 決まりました。", "exVi": "Con trai tôi đã nhận được việc làm ổn định.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_3_78335\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#14b8a6\"/>\n      <stop offset=\"100%\" stop-color=\"#0f766e\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_3_78335\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_3_78335)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_3_78335)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">就職</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">💼</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">ĐI LÀM</text>\n</svg>"}, {"id": 4, "cat": "event", "catName": "Sự kiện đời người", "badge": "Sinh con", "jp": "しゅっさん", "kana": "しゅっさん", "kanji": "出産", "romaji": "shussan", "vi": "Sinh con", "exJp": "出産の お祝いを 届けます。", "exVi": "Gửi quà chúc mừng bạn sinh em bé.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_4_44086\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0284c7\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_4_44086\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_4_44086)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_4_44086)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">出産</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">👶</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">SINH CON</text>\n</svg>"}, {"id": 5, "cat": "feeling", "catName": "Cảm xúc & Tâm trạng", "badge": "Vui mừng", "jp": "よろこびます", "kana": "よろこびます", "kanji": "喜びます", "romaji": "yorokobimasu", "vi": "Vui mừng, hạnh phúc", "exJp": "プレゼントを とても 喜んでくれました。", "exVi": "Bạn ấy đã vô cùng vui mừng khi nhận món quà.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_5_56939\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_5_56939\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_5_56939)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_5_56939)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">喜びます</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🥳</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">VUI MỪNG</text>\n</svg>"}, {"id": 6, "cat": "feeling", "catName": "Cảm xúc & Tâm trạng", "badge": "Hạnh phúc ngập tràn", "jp": "しあわせ（な）", "kana": "しあわせ（な）", "kanji": "幸せ（な）", "romaji": "shiawase(na)", "vi": "Hạnh phúc", "exJp": "いつまでも お幸せに！", "exVi": "Chúc hai bạn mãi mãi hạnh phúc bên nhau nhé!", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_6_22787\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#8b5cf6\"/>\n      <stop offset=\"100%\" stop-color=\"#6d28d9\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_6_22787\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_6_22787)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_6_22787)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">幸せ</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🥰</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">HẠNH PHÚC</text>\n</svg>"}, {"id": 7, "cat": "necessity", "catName": "Nhu cầu & Đồ dùng", "badge": "Cần thiết", "jp": "ひつよう（な）", "kana": "ひつよう（な）", "kanji": "必要（な）", "romaji": "hitsuyou(na)", "vi": "Cần thiết", "exJp": "パスポートが 必要です。", "exVi": "Hộ chiếu là giấy tờ cần thiết.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_7_98162\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_7_98162\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_7_98162)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_7_98162)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">必要</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">❗</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">CẦN THIẾT</text>\n</svg>"}, {"id": 8, "cat": "necessity", "catName": "Nhu cầu & Đồ dùng", "badge": "Cần có N cho cuộc sống", "jp": "N が ひつようです", "kana": "N が ひつようです", "kanji": "Nが必要です", "romaji": "N ga hitsuyou desu", "vi": "Cần N", "exJp": "新しい 生活に 家具が 必要です。", "exVi": "Cuộc sống mới cần có đồ nội thất.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_8_23427\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_8_23427\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_8_23427)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_8_23427)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">Nが必要です</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🛋️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">CẦN CÓ N</text>\n</svg>"}, {"id": 9, "cat": "necessity", "catName": "Nhu cầu & Đồ dùng", "badge": "Đồ dùng của em bé là rất cần thiết", "jp": "あかちゃんの ものが ひつようです", "kana": "あかちゃんの ものが ひつようです", "kanji": "赤ちゃんの物が必要です", "romaji": "akachan no mono ga hitsuyou desu", "vi": "Đồ dùng của em bé là cần thiết", "exJp": "出産祝には 赤ちゃんの物が 必要です。", "exVi": "Quà mừng sinh em bé thì các đồ dùng trẻ sơ sinh là rất cần thiết.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_9_38407\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#10b981\"/>\n      <stop offset=\"100%\" stop-color=\"#047857\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_9_38407\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_9_38407)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_9_38407)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">赤ちゃんの</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🍼</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">ĐỒ EM BÉ CẦN</text>\n</svg>"}, {"id": 10, "cat": "gift", "catName": "Quà tặng & Lễ nghi", "badge": "Viết thiệp chúc mừng", "jp": "カードを かきます", "kana": "カードを かきます", "kanji": "カードを書きます", "romaji": "kaado wo kakimasu", "vi": "Viết thiệp", "exJp": "お祝いの メッセージカードを 書きます。", "exVi": "Viết thiệp gửi gắm thông điệp chúc phúc.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_10_71165\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#dc2626\"/>\n      <stop offset=\"100%\" stop-color=\"#991b1b\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_10_71165\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_10_71165)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_10_71165)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">カードを書</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">💌</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">VIẾT THIỆP</text>\n</svg>"}, {"id": 11, "cat": "gift", "catName": "Quà tặng & Lễ nghi", "badge": "Lời cảm ơn", "jp": "おれい", "kana": "おれい", "kanji": "お礼", "romaji": "orei", "vi": "Lời cảm ơn", "exJp": "お世話になった方に お礼を します。", "exVi": "Tặng quà đáp lễ người đã giúp đỡ mình.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_11_63770\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#14b8a6\"/>\n      <stop offset=\"100%\" stop-color=\"#0f766e\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_11_63770\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_11_63770)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_11_63770)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">お礼</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🙇‍♂️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">LỜI CẢM ƠN</text>\n</svg>"}, {"id": 12, "cat": "gift", "catName": "Quà tặng & Lễ nghi", "badge": "Nói lời cảm ơn chân thành", "jp": "おれいを いいます", "kana": "おれいを いいます", "kanji": "お礼を言います", "romaji": "orei wo iimasu", "vi": "Nói lời cảm ơn", "exJp": "先生に 直接 お礼を 言いました。", "exVi": "Tôi đã trực tiếp nói lời cảm ơn tới thầy giáo.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_12_51596\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#14b8a6\"/>\n      <stop offset=\"100%\" stop-color=\"#0f766e\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_12_51596\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_12_51596)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_12_51596)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">お礼を言い</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🗣️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">NÓI CẢM ƠN</text>\n</svg>"}, {"id": 13, "cat": "gift", "catName": "Quà tặng & Lễ nghi", "badge": "Khung ảnh kỷ niệm", "jp": "しゃしんたて", "kana": "しゃしんたて", "kanji": "写真立て", "romaji": "shashintate", "vi": "Khung ảnh", "exJp": "結婚祝いに 写真立てを あげます。", "exVi": "Tặng khung ảnh làm quà mừng cưới.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_13_60251\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_13_60251\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_13_60251)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_13_60251)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">写真立て</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🖼️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">KHUNG ẢNH</text>\n</svg>"}, {"id": 14, "cat": "gift", "catName": "Quà tặng & Lễ nghi", "badge": "Bình hoa", "jp": "かびん", "kana": "かびん", "kanji": "花瓶", "romaji": "kabin", "vi": "Bình hoa", "exJp": "きれいな 花瓶に 花を かざります。", "exVi": "Cắm hoa tươi vào chiếc bình hoa tuyệt đẹp.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_14_35830\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_14_35830\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_14_35830)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_14_35830)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">花瓶</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🏺</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">BÌNH HOA</text>\n</svg>"}, {"id": 15, "cat": "gift", "catName": "Quà tặng & Lễ nghi", "badge": "Nhẫn đeo tay (nhẫn cưới)", "jp": "ゆびわ", "kana": "ゆびわ", "kanji": "指輪", "romaji": "yubiwa", "vi": "Nhẫn", "exJp": "結婚指輪を 買いました。", "exVi": "Chúng tôi đã mua nhẫn cưới.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_15_77898\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#ec4899\"/>\n      <stop offset=\"100%\" stop-color=\"#db2777\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_15_77898\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_15_77898)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_15_77898)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">指輪</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">💍</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">NHẪN ĐEO TAY</text>\n</svg>"}, {"id": 16, "cat": "feeling", "catName": "Cảm xúc & Tâm trạng", "badge": "Chắc chắn là", "jp": "きっと", "kana": "きっと", "kanji": "きっと", "romaji": "kitto", "vi": "Chắc chắn là, nhất định là", "exJp": "きっと 喜んでくれると 思います。", "exVi": "Tôi tin chắc chắn bạn ấy sẽ rất thích.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_16_38210\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_16_38210\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_16_38210)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_16_38210)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">きっと</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🤞</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">CHẮC CHẮN</text>\n</svg>"}, {"id": 17, "cat": "gift", "catName": "Quà tặng & Lễ nghi", "badge": "Bộ âu phục", "jp": "スーツ", "kana": "スーツ", "kanji": "スーツ", "romaji": "suutsu", "vi": "Bộ vest", "exJp": "パーティーに 新しいスーツを 着て行きます。", "exVi": "Mặc bộ com-lê mới đi dự tiệc.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_17_11491\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_17_11491\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_17_11491)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_17_11491)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">スーツ</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🤵</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">ÂU PHỤC</text>\n</svg>"}, {"id": 18, "cat": "feeling", "catName": "Cảm xúc & Tâm trạng", "badge": "Quan trọng", "jp": "たいせつ（な）", "kana": "たいせつ（な）", "kanji": "大切（な）", "romaji": "taisetsu(na)", "vi": "Quan trọng, đáng quý, trân trọng", "exJp": "友だちは 私の 大切な 宝物です。", "exVi": "Bạn bè là báu vật vô cùng quý giá của tôi.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_18_86496\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_18_86496\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_18_86496)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_18_86496)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">大切</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">💎</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">QUÝ GIÁ</text>\n</svg>"}, {"id": 19, "cat": "feeling", "catName": "Cảm xúc & Tâm trạng", "badge": "Trân trọng", "jp": "たいせつに します", "kana": "たいせつに します", "kanji": "大切にします", "romaji": "taisetsu ni shimasu", "vi": "Trân trọng, giữ gìn cẩn thận", "exJp": "いただいた プレゼントを 大切にします。", "exVi": "Tôi sẽ trân trọng và giữ gìn cẩn thận món quà này.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_19_8699\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_19_8699\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_19_8699)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_19_8699)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">大切にします</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🤲</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">TRÂN TRỌNG</text>\n</svg>"}];
window.VOCAB_DATA = VOCAB_DATA;
const VERB_MORPH_DATA = [{"kanji": "着る", "masu": "きます", "vi": "Mặc (thân trên: áo/kimono/vest)", "col2": "着物を着ています", "col3": "とても似合うと思います", "col4": "着たいと言っていました", "col5": "パーティーに着ていきます", "ex": "パーティーで素敵な着物を着ている人がいます。"}, {"kanji": "履く", "masu": "はきます", "vi": "Mặc/đi (thân dưới: quần/giày)", "col2": "黒い靴を履いています", "col3": "スニーカーがいいと思います", "col4": "新しいのを履くと言っていました", "col5": "歩きやすい靴を履きます", "ex": "歩きやすいスニーカーを履いたほうがいいですよ。"}, {"kanji": "被る", "masu": "かぶります", "vi": "Đội (mũ, nón)", "col2": "帽子を被っています", "col3": "かっこいいと思います", "col4": "被りたくないと言っていました", "col5": "日傘や帽子を被ります", "ex": "日差しが強いので帽子を被ったほうがいいです。"}, {"kanji": "掛ける", "masu": "かけます", "vi": "Đeo (kính mắt)", "col2": "眼鏡を掛けています", "col3": "よく似合うと思います", "col4": "眼鏡を掛けると言っていました", "col5": "サングラスを掛けます", "ex": "あの眼鏡を掛けている男性は誰ですか。"}, {"kanji": "思う", "masu": "おもいます", "vi": "Nghĩ là, cho là", "col2": "そう思っています", "col3": "いい考えだと思います", "col4": "阿部さんもそう言っていました", "col5": "パーティーがいいと思います", "ex": "お祝いはみんなでパーティーをするのがいいと思います。"}];
const QUIZ_QUESTIONS = [{"id": 1, "category": "Ngữ pháp: ～と思います", "q": "お祝いは パーティーが [____] と 思います。", "options": ["いい", "よく", "いいだ", "よかったに"], "correct": 0, "explain": "Tính từ đuôi い ở thể Thông thường (Futsuukei): いい ➔ 「いいと思います」 (Tôi nghĩ là hay nhất)."}, {"id": 2, "category": "Ngữ pháp: ～と思います", "q": "プレゼントを あげたら、きっと [____] と 思います。", "options": ["喜ぶ", "喜び", "喜んで", "喜ばないで"], "correct": 0, "explain": "Động từ thể Từ điển (Thể thông thường) + と思います ➔ 「喜ぶと思います」 (Tôi nghĩ bạn ấy sẽ vui)."}, {"id": 3, "category": "Ngữ pháp: ～と言っていました", "q": "阿部さんは みんなと [____] と 言っていました。", "options": ["話したい", "話します", "話して", "話したかったに"], "correct": 0, "explain": "Trích dẫn lời nói thể thông thường: 話したい ➔ 「話したいと言っていました」 (Nói rằng muốn trò chuyện)."}, {"id": 4, "category": "Từ vựng: Động từ mặc trang phục", "q": "田中さんは きれいな 着物を [____] います。", "options": ["着て (きて)", "履いて (はいて)", "被って (かぶって)", "掛けて (かけて)"], "correct": 0, "explain": "Kimono mặc trên thân người dùng động từ 「着ます」 ➔ 「着ています」."}, {"id": 5, "category": "Từ vựng: Động từ đi giày/quần", "q": "新しい スニーカーを [____] います。", "options": ["履いて (はいて)", "着て (きて)", "被って (かぶって)", "掛けて (かけて)"], "correct": 0, "explain": "Giày dép, quần tất ở phần thân dưới dùng động từ 「履きます」 ➔ 「履いています」."}, {"id": 6, "category": "Từ vựng: Đội mũ", "q": "白い 帽子を [____] います。", "options": ["被って (かぶって)", "着て (きて)", "履いて (はいて)", "掛けて (かけて)"], "correct": 0, "explain": "Mũ nón trên đầu dùng động từ 「被ります」 (かぶります) ➔ 「被っています」."}, {"id": 7, "category": "Từ vựng: Đeo kính", "q": "黒い 眼鏡を [____] います。", "options": ["掛けて (かけて)", "着て (きて)", "履いて (はいて)", "被って (かぶって)"], "correct": 0, "explain": "Kính mắt dùng động từ 「掛けます」 (かけます) ➔ 「掛けています」."}, {"id": 8, "category": "Giao tiếp: Chúc mừng đám cưới", "q": "Lời chúc mừng đám cưới trang trọng nhất trong tiếng Nhật là:", "options": ["ご結婚、おめでとうございます！", "お大事に！", "いってらっしゃい！", "ごちそうさまでした！"], "correct": 0, "explain": "「ご結婚、おめでとうございます！」 nghĩa là Xin chúc mừng đám cưới của bạn!"}, {"id": 9, "category": "Từ vựng: Thời gian", "q": "「きょねん」 (Năm ngoái) được viết bằng cặp chữ Hán nào?", "options": ["去年", "今年", "来年", "先年"], "correct": 0, "explain": "Năm ngoái là 「去年」 (KHỨ NIÊN)."}, {"id": 10, "category": "Từ vựng: Thời gian", "q": "「らいねん」 (Năm sau) được viết bằng cặp chữ Hán nào?", "options": ["来年", "今年", "去年", "先年"], "correct": 0, "explain": "Năm sau là 「来年」 (LAI NIÊN)."}, {"id": 11, "category": "Chữ Hán Bài 18: 思 (Tư)", "q": "Động từ 「おもいます」 (Suy nghĩ, cho là) có chữ Hán là:", "options": ["思います", "言います", "行きます", "話します"], "correct": 0, "explain": "「おもいます」 viết là 「思います」 (chữ TƯ - 9 nét, bộ Điền 田 + bộ Tâm 心)."}, {"id": 12, "category": "Chữ Hán Bài 18: 先 (Tiên)", "q": "Từ 「せんしゅう」 (Tuần trước) có chữ Hán đầu tiên là:", "options": ["先", "今", "来", "去"], "correct": 0, "explain": "「せんしゅう」 là 「先週」 (TIÊN CHU - chữ 先 có 6 nét)."}, {"id": 13, "category": "Chữ Hán Bài 18: 今 (Kim)", "q": "Từ 「ことし」 (Năm nay) có chữ Hán đầu tiên là:", "options": ["今", "先", "来", "去"], "correct": 0, "explain": "「ことし」 viết là 「今年」 (KIM NIÊN - chữ 今 có 4 nét)."}, {"id": 14, "category": "Chữ Hán Bài 18: 家 (Gia)", "q": "Từ 「かぞく」 (Gia đình) có chữ Hán đầu tiên là:", "options": ["家", "思", "先", "来"], "correct": 0, "explain": "「かぞく」 viết là 「家族」 (GIA TỘC - chữ 家 có 10 nét)."}, {"id": 15, "category": "Chữ Hán Bài 18: 着 (Trước)", "q": "Từ 「きもの」 (Trang phục truyền thống Kimono) viết chữ Hán là:", "options": ["着物", "履物", "被物", "掛物"], "correct": 0, "explain": "Kimono viết chữ Hán là 「着物」 (TRƯỚC VẬT - chữ 着 12 nét và chữ 物 8 nét)."}];
const DIALOGUE_STEPS = [{"options": [{"text": "みんなでレストランに集まって、サプライズパーティーをするのがいいと思います。", "vi": "Tôi nghĩ tụi mình tập hợp mọi người ở nhà hàng và làm một bữa tiệc bất ngờ là hay nhất.", "replyAvatar": "👨‍💼", "replyNpc": "Tanaka", "replyText": "いいですね！阿部さんもみんなとゆっくり話したいと言っていましたよ。", "replyVi": "Ý hay đấy! Anh Abe cũng nói là muốn được ngồi trò chuyện thong thả cùng mọi người mà."}, {"text": "お祝いに、みんなで寄せ書きした色紙とプレゼントを渡すのがいいと思います。", "vi": "Tôi nghĩ tụi mình cùng nhau viết thiệp mừng lưu bút và tặng một món quà kỷ niệm là tuyệt nhất.", "replyAvatar": "👨‍💼", "replyNpc": "Tanaka", "replyText": "温かいアイデアですね！記念に残るものをあげると喜ばれますね。", "replyVi": "Ý tưởng ấm áp quá! Tặng món đồ lưu lại kỷ niệm chắc chắn anh ấy sẽ thích lắm."}]}, {"npcName": "Abe", "avatar": "🤵", "npcText": "皆さん、今日は私のために素敵なパーティーを開いてくれて本当にありがとうございます！", "npcVi": "Tất cả mọi người, hôm nay đã vì tôi mà tổ chức bữa tiệc tuyệt vời thế này, thật lòng cảm ơn mọi người!", "options": [{"text": "ご結婚、本当におめでとうございます！末永くお幸せに！", "vi": "Chúc mừng đám cưới của anh! Chúc anh chị trăm năm hạnh phúc!", "replyAvatar": "🤵", "replyNpc": "Abe", "replyText": "ありがとうございます！これからもどうぞよろしくお願いします。", "replyVi": "Cảm ơn bạn rất nhiều! Từ nay về sau cũng mong được mọi người tiếp tục giúp đỡ."}, {"text": "スーツ姿がとてもかっこいいですね！奥様といつまでも仲良くお過ごしください。", "vi": "Bộ vest hôm nay trông anh bảnh bao lắm! Chúc anh và chị nhà luôn mãi mặn nồng bên nhau nhé.", "replyAvatar": "🤵", "replyNpc": "Abe", "replyText": "褒めてくれて嬉しいです！最高の思い出になりました。", "replyVi": "Được bạn khen tôi mừng quá! Đây thực sự là kỷ niệm tuyệt vời nhất của đời tôi."}]}];

// Tokyo Audio Speech Synthesis handled globally via assets/js/audio-engine.js

// Verb Morphing Laboratory
let currentVerbIdx = 0;

function renderVerbPicker() {
    const container = document.getElementById('verbPickerRow');
    if (!container || !VERB_MORPH_DATA.length) return;
    container.innerHTML = VERB_MORPH_DATA.map((v, i) => `
        <button type="button" class="verb-pill ${i === 0 ? 'active' : ''}" onclick="selectVerb(${i}, this)">
            <span class="pill-kanji">${v.kanji}</span>
            <span class="pill-meaning">(${v.vi})</span>
        </button>
    `).join('');
    updateMorphDisplay(0);
}

function selectVerb(idx, btn) {
    document.querySelectorAll('.verb-pill').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentVerbIdx = idx;
    updateMorphDisplay(idx);
}

function updateMorphDisplay(idx) {
    const v = VERB_MORPH_DATA[idx];
    if (!v) return;
    const morphMasuEl = document.getElementById('morphMasu');
    if (morphMasuEl) {
        morphMasuEl.innerHTML = `
            <div style="font-size:1.35rem; font-weight:800; color:#0f172a; line-height:1.2;">${v.kanji}</div>
            <div style="font-size:0.86rem; font-weight:700; color:#059669; margin-top:4px; font-family:var(--jp-font);">${v.masu}</div>
        `;
    }
    document.getElementById('morphVi').textContent = v.vi;
    document.getElementById('morphTe').textContent = v.col2;
    document.getElementById('morphTeIki').textContent = v.col3;
    document.getElementById('morphTeKi').textContent = v.col4;
    document.getElementById('morphMashou').textContent = v.col5;
    document.getElementById('morphExText').textContent = v.ex;
}

function speakCurrentMorph() {
    const v = VERB_MORPH_DATA[currentVerbIdx];
    if (v) speakText(v.ex);
}

// Flashcards Logic
let activeVocabFilter = 'all';
let learnedCards = new Set();

function initVocabFilters() {
    const bar = document.getElementById('vocabFilterBar');
    const cats = Array.from(new Set(VOCAB_DATA.map(v => v.cat)));
    const catNames = {};
    VOCAB_DATA.forEach(v => catNames[v.cat] = v.catName);

    let filterBtns = `<button class="vocab-filter-btn active" onclick="filterVocab('all', this)">🌟 Tất cả (${VOCAB_DATA.length})</button>`;
    cats.forEach(c => {
        filterBtns += `<button class="vocab-filter-btn" onclick="filterVocab('${c}', this)">${catNames[c] || c}</button>`;
    });
    filterBtns += `<div class="vocab-stats-badge" id="vocabStats">Đã thuộc: 0 / ${VOCAB_DATA.length} từ</div>`;
    bar.innerHTML = filterBtns;
}

function renderFlashcards() {
    const container = document.getElementById('flashcardsGrid');
    const filtered = activeVocabFilter === 'all' 
        ? VOCAB_DATA 
        : VOCAB_DATA.filter(v => v.cat === activeVocabFilter);

    container.innerHTML = filtered.map(v => `
        <div class="flashcard" onclick="flipCard(this, event)">
            <div class="fc-inner">
                <div class="fc-front">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="fc-badge">${v.badge || v.catName}</span>
                        <button type="button" class="btn-speak" style="width:28px; height:28px; font-size:0.75rem;" onclick="event.stopPropagation(); speakText('${v.jp}')">🔊</button>
                    </div>
                    <div class="fc-3d-stage" onclick="event.stopPropagation(); openVocab3D(VOCAB_DATA.indexOf(v))" title="Bấm để mở Mô Hình 3D 360° tương tác">
                        <div class="fc-3d-model-wrapper">
                            <div class="fc-3d-floating-obj">
                                ${v.svg}
                            </div>
                            <div class="fc-3d-shadow-blob"></div>
                        </div>
                        <div class="btn-launch-3d-badge">
                            <span>🧊</span>
                            <span>Mô hình 3D (360°)</span>
                        </div>
                    </div>
                    <div>
                        <div class="fc-jp jp-text">${v.kanji || v.jp}</div>
                        <div class="fc-kana jp-text">${v.kana}</div>
                        <div class="fc-romaji">${v.romaji}</div>
                    </div>
                    <div class="fc-hint">💡 Bấm thẻ để lật xem nghĩa & ví dụ</div>
                </div>

                <div class="fc-back">
                    <div>
                        <div class="fc-back-meaning">${v.vi}</div>
                        <div style="font-size:0.75rem; font-weight:800; color:#047857; text-transform:uppercase; margin-bottom:4px;">Ví dụ thực tế:</div>
                        <div class="fc-back-ex-jp jp-text">${v.exJp}</div>
                        <div class="fc-back-ex-vi">${v.exVi}</div>
                    </div>
                    <div class="fc-back-actions">
                        <button type="button" class="btn-speak" style="width:32px; height:32px; font-size:0.8rem;" onclick="event.stopPropagation(); speakText('${v.exJp}')">🔊</button>
                        <button type="button" class="btn-learned ${learnedCards.has(v.id) ? 'active' : ''}" onclick="event.stopPropagation(); toggleLearned(${v.id}, this)">
                            ${learnedCards.has(v.id) ? '✓ Đã thuộc' : '+ Đánh dấu thuộc'}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
    updateLearnedStats();
}

function flipCard(card, event) {
    if (event.target.closest('button')) return;
    card.classList.toggle('flipped');
}

function filterVocab(cat, btn) {
    activeVocabFilter = cat;
    document.querySelectorAll('.vocab-filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderFlashcards();
}

function toggleLearned(id, btn) {
    if (learnedCards.has(id)) {
        learnedCards.delete(id);
        btn.classList.remove('active');
        btn.textContent = '+ Đánh dấu thuộc';
    } else {
        learnedCards.add(id);
        btn.classList.add('active');
        btn.textContent = '✓ Đã thuộc';
    }
    updateLearnedStats();
}

function updateLearnedStats() {
    const badge = document.getElementById('vocabStats');
    if (badge) badge.textContent = `Đã thuộc: ${learnedCards.size} / ${VOCAB_DATA.length} từ`;
}

// Dialogue Simulator
let currentStepIdx = 0;

function initDialogue() {
    currentStepIdx = 0;
    renderDialogueOptions(0);
}

function renderDialogueOptions(stepIdx) {
    const container = document.getElementById('chatOptionsGrid');
    const step = DIALOGUE_STEPS[stepIdx];
    if (!step) {
        container.innerHTML = `
            <div style="grid-column: 1/-1; text-align:center; padding:12px; color:#059669; font-weight:700;">
                🎉 Hoàn thành xuất sắc đoạn hội thoại tình huống Bài 18!
            </div>
        `;
        return;
    }

    container.innerHTML = step.options.map((opt, i) => `
        <button type="button" class="btn-chat-choice" onclick="chooseDialogue(${stepIdx}, ${i})">
            <div style="font-family:var(--jp-font);">${opt.text}</div>
            <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">${opt.vi}</div>
        </button>
    `).join('');
}

function chooseDialogue(stepIdx, optIdx) {
    const step = DIALOGUE_STEPS[stepIdx];
    const opt = step.options[optIdx];
    const chat = document.getElementById('chatContainer');
    const optBox = document.getElementById('chatOptionsGrid');
    if (optBox) optBox.innerHTML = '';

    const appendBubble = (isUser, avatar, name, jp, vi) => {
        const bubble = document.createElement('div');
        bubble.className = 'chat-bubble ' + (isUser ? 'user' : 'bot');
        bubble.innerHTML = `
            <div class="chat-avatar">${avatar}</div>
            <div class="chat-msg">
                <div class="chat-name">${name}</div>
                <div class="chat-jp">${jp}</div>
                <div class="chat-vi">${vi}</div>
            </div>
        `;
        chat.appendChild(bubble);
        chat.scrollTop = chat.scrollHeight;
    };

    appendBubble(true, '🧑', 'Bạn (Tôi)', opt.text, opt.vi);

    const queueItems = [
        { text: opt.text },
        {
            text: opt.replyText,
            onStart: () => appendBubble(false, opt.replyAvatar || '👩', opt.replyNpc, opt.replyText, opt.replyVi)
        }
    ];

    if (stepIdx + 1 < DIALOGUE_STEPS.length) {
        const nextPrompt = DIALOGUE_STEPS[stepIdx + 1];
        queueItems.push({
            text: nextPrompt.npcText,
            onStart: () => {
                appendBubble(false, nextPrompt.avatar || '👨', nextPrompt.npcName, nextPrompt.npcText, nextPrompt.npcVi);
                renderDialogueOptions(stepIdx + 1);
            }
        });
    } else {
        queueItems.push({
            text: '',
            onStart: () => renderDialogueOptions(stepIdx + 1)
        });
    }

    if (window.AudioEngine && typeof window.AudioEngine.queue === 'function') {
        window.AudioEngine.queue(queueItems);
    } else {
        queueItems.forEach(item => { if (item.onStart) item.onStart(); });
    }
}

// Quiz Logic
let quizAnswers = {};

function renderQuiz() {
    const container = document.getElementById('quizContainer');
    container.innerHTML = QUIZ_QUESTIONS.map(q => `
        <div class="quiz-card" id="quizCard_${q.id}">
            <div class="quiz-q-num">Câu ${q.id} / 15 • ${q.category}</div>
            <div class="quiz-question-text jp-text">${q.q}</div>
            <div class="quiz-options-grid">
                ${q.options.map((opt, optIdx) => `
                    <button type="button" class="quiz-opt-btn jp-text" onclick="answerQuiz(${q.id}, ${optIdx}, this)">
                        ${opt}
                    </button>
                `).join('')}
            </div>
            <div class="quiz-feedback" id="quizFeedback_${q.id}">
                ${q.explain}
            </div>
        </div>
    `).join('');
    updateQuizProgress();
}

function answerQuiz(qId, selectedIdx, btn) {
    if (quizAnswers[qId] !== undefined) return;
    quizAnswers[qId] = selectedIdx;

    const q = QUIZ_QUESTIONS.find(item => item.id === qId);
    const card = document.getElementById(`quizCard_${qId}`);
    const buttons = card.querySelectorAll('.quiz-opt-btn');
    const feedback = document.getElementById(`quizFeedback_${qId}`);

    buttons.forEach((b, idx) => {
        b.disabled = true;
        if (idx === q.correct) {
            b.classList.add('correct');
        } else if (idx === selectedIdx) {
            b.classList.add('wrong');
        }
    });

    feedback.classList.add('show');
    if (selectedIdx === q.correct) {
        feedback.classList.add('correct');
        feedback.innerHTML = `✓ <strong>Chính xác!</strong> ${q.explain}`;
    } else {
        feedback.classList.add('wrong');
        feedback.innerHTML = `✕ <strong>Chưa chính xác!</strong> ${q.explain}`;
    }

    updateQuizProgress();
    checkQuizFinish();
}

function updateQuizProgress() {
    const answeredCount = Object.keys(quizAnswers).length;
    const pct = (answeredCount / QUIZ_QUESTIONS.length) * 100;
    document.getElementById('quizProgressBar').style.width = `${pct}%`;
}

function checkQuizFinish() {
    if (Object.keys(quizAnswers).length === QUIZ_QUESTIONS.length) {
        let score = 0;
        QUIZ_QUESTIONS.forEach(q => {
            if (quizAnswers[q.id] === q.correct) score++;
        });

        const scoreBox = document.getElementById('scoreBox');
        const scoreVal = document.getElementById('scoreVal');
        const scoreMsg = document.getElementById('scoreMsg');

        scoreVal.textContent = `${score} / 15`;
        if (score >= 13) {
            scoreMsg.textContent = "🌟 Tuyệt vời! Bạn đã thành thạo toàn bộ kiến thức Bài 18!";
        } else if (score >= 9) {
            scoreMsg.textContent = "👍 Khá tốt! Hãy ôn lại các câu chưa chính xác nhé.";
        } else {
            scoreMsg.textContent = "💪 Cố lên! Hãy xem lại phần giải thích và thử làm lại nhé.";
        }
        scoreBox.classList.add('show');
        scoreBox.scrollIntoView({ behavior: 'smooth' });
    }
}

function resetQuiz() {
    quizAnswers = {};
    document.getElementById('scoreBox').classList.remove('show');
    renderQuiz();
    document.getElementById('sec-quiz').scrollIntoView({ behavior: 'smooth' });
}

// Global Nav






document.addEventListener('click', (e) => {
    const menu = document.getElementById('globalToolsMenu');
    if (menu && !menu.contains(e.target)) {
        menu.classList.remove('show');
    }
});

// Init
window.addEventListener('DOMContentLoaded', () => {
    renderVerbPicker();
    initVocabFilters();
    renderFlashcards();
    initDialogue();
    renderQuiz();
});
