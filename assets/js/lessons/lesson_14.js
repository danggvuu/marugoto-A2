/* Extracted data & interactive logic for Marugoto A2 Lesson 14 */
const VOCAB_DATA = [{"id": 1, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Nơi chốn", "jp": "オフィス", "kana": "オフィス", "kanji": "オフィス", "romaji": "ofisu", "vi": "Văn phòng", "exJp": "あかるくて ひろい オフィスです。", "exVi": "Văn phòng làm việc sáng sủa và rộng rãi.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_1_67860\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_1_67860\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_1_67860)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_1_67860)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">オフィス</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🏢</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">VĂN PHÒNG</text>\n</svg>"}, {"id": 2, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "キャビネット", "kana": "キャビネット", "kanji": "キャビネット", "romaji": "kyabinetto", "vi": "Tủ đựng (tài liệu, ...)", "exJp": "<ruby>資料<rt>しりょう</rt></ruby>は キャビネットの <ruby>中<rt>なか</rt></ruby>に あります。", "exVi": "Tài liệu nằm ở bên trong tủ đựng hồ sơ.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_2_2875\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_2_2875\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_2_2875)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_2_2875)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">キャビネット</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🗄️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">TỦ TÀI LIỆU</text>\n</svg>"}, {"id": 3, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "コピーき", "kana": "コピーき", "kanji": "コピー機", "romaji": "kopiiki", "vi": "Máy photo", "exJp": "コピー<ruby>機<rt>き</rt></ruby>の <ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>を <ruby>教<rt>おし</rt></ruby>えてください。", "exVi": "Xin hãy chỉ cho tôi cách sử dụng máy photo.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_3_54239\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_3_54239\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_3_54239)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_3_54239)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">コピー機</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🖨️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">MÁY PHOTO</text>\n</svg>"}, {"id": 4, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "ファックス", "kana": "ファックス", "kanji": "ファックス", "romaji": "fakkusu", "vi": "Máy fax", "exJp": "ファックスで <ruby>書類<rt>しょるい</rt></ruby>を <ruby>送<rt>おく</rt></ruby>ります。", "exVi": "Gửi giấy tờ qua đường máy fax.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_4_43645\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_4_43645\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_4_43645)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_4_43645)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">ファックス</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">📠</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">MÁY FAX</text>\n</svg>"}, {"id": 5, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thiết bị", "jp": "こくさいでんわ", "kana": "こくさいでんわ", "kanji": "国際電話", "romaji": "kokusaidenwa", "vi": "Điện thoại quốc tế", "exJp": "<ruby>会社<rt>かいしゃ</rt></ruby>から <ruby>国際電話<rt>こくさいでんわ</rt></ruby>を かけます。", "exVi": "Gọi điện thoại quốc tế từ công ty.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_5_98509\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_5_98509\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_5_98509)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_5_98509)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">国際電話</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🌐</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">GỌI QUỐC TẾ</text>\n</svg>"}, {"id": 6, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Chức vụ", "jp": "しゃちょう", "kana": "しゃちょう", "kanji": "社長", "romaji": "shachou", "vi": "Giám đốc", "exJp": "<ruby>社長<rt>しゃちょう</rt></ruby>に あいさつを します。", "exVi": "Chào hỏi giám đốc công ty.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_6_33194\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_6_33194\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_6_33194)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_6_33194)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">社長</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">👔</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">GIÁM ĐỐC</text>\n</svg>"}, {"id": 7, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Chức vụ", "jp": "ひしょ", "kana": "ひしょ", "kanji": "秘書", "romaji": "hisho", "vi": "Thư ký", "exJp": "<ruby>秘書<rt>ひしょ</rt></ruby>に スケジュールを <ruby>聞<rt>き</rt></ruby>きます。", "exVi": "Hỏi thư ký về lịch làm việc.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_7_51400\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_7_51400\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_7_51400)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_7_51400)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">秘書</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">👩‍💼</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">THƯ KÝ</text>\n</svg>"}, {"id": 8, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Nơi chốn", "jp": "うけつけ", "kana": "うけつけ", "kanji": "受付", "romaji": "uketsuke", "vi": "Lễ tân", "exJp": "1<ruby>階<rt>かい</rt></ruby>の <ruby>受付<rt>うけつけ</rt></ruby>で <ruby>待<rt>ま</rt></ruby>っています。", "exVi": "Tôi đang đợi ở quầy lễ tân tầng 1.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_8_82532\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0284c7\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_8_82532\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_8_82532)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_8_82532)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">受付</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">💁‍♀️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">LỄ TÂN</text>\n</svg>"}, {"id": 9, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Nhân sự", "jp": "じむスタッフ", "kana": "じむスタッフ", "kanji": "事務スタッフ", "romaji": "jimu sutaffu", "vi": "Nhân viên văn phòng", "exJp": "<ruby>事務<rt>じむ</rt></ruby>スタッフが <ruby>手伝<rt>てつだ</rt></ruby>って くれました。", "exVi": "Nhân viên văn phòng đã giúp đỡ tôi.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_9_99358\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_9_99358\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_9_99358)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_9_99358)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">事務スタッフ</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">👥</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">NHÂN VIÊN</text>\n</svg>"}, {"id": 10, "cat": "people", "catName": "Nhân sự & Chức vụ", "badge": "Nghề nghiệp", "jp": "ドライバー", "kana": "ドライバー", "kanji": "ドライバー", "romaji": "doraibaa", "vi": "Lái xe", "exJp": "ドライバーが <ruby>来<rt>く</rt></ruby>るまで <ruby>待<rt>ま</rt></ruby>っています。", "exVi": "Bác tài xế đang đợi sẵn ở ô tô.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_10_26739\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_10_26739\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_10_26739)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_10_26739)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">ドライバー</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🚗</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">TÀI XẾ</text>\n</svg>"}, {"id": 11, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Cơ sở vật chất", "jp": "ドア", "kana": "ドア", "kanji": "ドア", "romaji": "doa", "vi": "Cửa ra vào", "exJp": "ドアを ノックしてから <ruby>入<rt>はい</rt></ruby>ります。", "exVi": "Gõ cửa trước khi bước vào phòng.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_11_8875\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_11_8875\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_11_8875)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_11_8875)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">ドア</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🚪</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">CỬA RA VÀO</text>\n</svg>"}, {"id": 12, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Cơ sở vật chất", "jp": "まど", "kana": "まど", "kanji": "窓", "romaji": "mado", "vi": "Cửa sổ", "exJp": "<ruby>窓<rt>まど</rt></ruby>を <ruby>開<rt>あ</rt></ruby>けて、<ruby>風<rt>かぜ</rt></ruby>を <ruby>入<rt>い</rt></ruby>れます。", "exVi": "Mở cửa sổ cho gió thoáng vào.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_12_10354\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_12_10354\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_12_10354)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_12_10354)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">窓</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🪟</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">CỬA SỔ</text>\n</svg>"}, {"id": 13, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（ドアを）あけます", "kana": "（ドアを）あけます", "kanji": "（ドアを）開けます", "romaji": "akemasu", "vi": "Mở (cửa)", "exJp": "ドアを <ruby>開<rt>あ</rt></ruby>けても いいですか。", "exVi": "Tôi mở cửa có được không ạ?", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_13_8189\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_13_8189\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_13_8189)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_13_8189)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">開けます</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🚪</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">MỞ CỬA</text>\n</svg>"}, {"id": 14, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（ドアを）しめます", "kana": "（ドアを）しめます", "kanji": "（ドアを）閉めます", "romaji": "shimemasu", "vi": "Đóng (cửa)", "exJp": "<ruby>寒<rt>さむ</rt></ruby>iので、ドアを <ruby>閉<rt>し</rt></ruby>めます。", "exVi": "Trời lạnh nên tôi đóng cửa lại.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_14_90792\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#0ea5e9\"/>\n      <stop offset=\"100%\" stop-color=\"#0284c7\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_14_90792\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_14_90792)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_14_90792)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">閉めます</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🔒</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">ĐÓNG CỬA</text>\n</svg>"}, {"id": 15, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（でんきを）つけます", "kana": "（でんきを）つけます", "kanji": "（電気を）点けます", "romaji": "tsukemasu", "vi": "Bật (đèn)", "exJp": "<ruby>暗<rt>くら</rt></ruby>いので <ruby>電気<rt>でんき</rt></ruby>を <ruby>点<rt>つ</rt></ruby>けます。", "exVi": "Phòng tối nên tôi bật đèn lên.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_15_89848\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_15_89848\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_15_89848)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_15_89848)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">点けます</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">💡</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">BẬT ĐÈN</text>\n</svg>"}, {"id": 16, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Danh động từ (N・V3)", "jp": "（でんきを）けします", "kana": "（でんきを）けします", "kanji": "（電気を）消します", "romaji": "keshimasu", "vi": "Tắt (đèn)", "exJp": "<ruby>帰<rt>かえ</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>に <ruby>電気<rt>でんき</rt></ruby>を <ruby>消<rt>け</rt></ruby>してください。", "exVi": "Trước khi về nhớ tắt điện nhé.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_16_40705\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_16_40705\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_16_40705)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_16_40705)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">消します</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🌑</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">TẮT ĐÈN</text>\n</svg>"}, {"id": 17, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "（パソコンが）こわれます", "kana": "（パソコンが）こわれます", "kanji": "（パソコンが）壊れます", "romaji": "kowaremasu", "vi": "(Máy tính) Hỏng", "exJp": "パソコンが <ruby>壊<rt>こわ</rt></ruby>れて、<ruby>動<rt>うご</rt></ruby>きません。", "exVi": "Máy tính bị hỏng nên không hoạt động.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_17_13690\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_17_13690\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_17_13690)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_17_13690)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">壊れます</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">⚠️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">BỊ HỎNG</text>\n</svg>"}, {"id": 18, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Trạng thái", "jp": "べんきょうちゅう", "kana": "べんきょうちゅう", "kanji": "勉強中", "romaji": "benkyouchuu", "vi": "Đang học", "exJp": "<ruby>今<rt>いま</rt></ruby> <ruby>日本語<rt>にほんご</rt></ruby>を <ruby>勉強中<rt>べんきょうちゅう</rt></ruby>です。", "exVi": "Tôi đang trong giờ học tiếng Nhật.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_18_19561\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#14b8a6\"/>\n      <stop offset=\"100%\" stop-color=\"#0f766e\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_18_19561\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_18_19561)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_18_19561)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">勉強中</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">📖</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">ĐANG HỌC</text>\n</svg>"}, {"id": 19, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Phó từ", "jp": "ぺらぺら", "kana": "ぺらぺら", "kanji": "ぺらぺら", "romaji": "perapera", "vi": "Lưu loát (nói, ...)", "exJp": "<ruby>彼<rt>かれ</rt></ruby>は <ruby>英語<rt>えいご</rt></ruby>が ぺらぺらです。", "exVi": "Anh ấy nói tiếng Anh cực kỳ lưu loát.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_19_6690\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_19_6690\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_19_6690)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_19_6690)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">ぺらぺら</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🗣️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">LƯU LOÁT</text>\n</svg>"}, {"id": 20, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Động từ", "jp": "はじめます", "kana": "はじめます", "kanji": "始めます", "romaji": "hajimemasu", "vi": "Bắt đầu", "exJp": "では、<ruby>会議<rt>かいぎ</rt></ruby>を <ruby>始<rt>はじ</rt></ruby>めましょう。", "exVi": "Nào, chúng ta bắt đầu cuộc họp nhé.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_20_79063\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_20_79063\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_20_79063)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_20_79063)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">始めます</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">▶️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">BẮT ĐẦU</text>\n</svg>"}, {"id": 21, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Đồ dùng", "jp": "ファイル", "kana": "ファイル", "kanji": "ファイル", "romaji": "fairu", "vi": "File", "exJp": "このファイルを <ruby>見<rt>み</rt></ruby>てください。", "exVi": "Hãy xem tập tài liệu này.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_21_28033\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_21_28033\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_21_28033)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_21_28033)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">ファイル</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">📁</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">FILE TÀI LIỆU</text>\n</svg>"}, {"id": 22, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Đồ dùng", "jp": "メモ", "kana": "メモ", "kanji": "メモ", "romaji": "memo", "vi": "Ghi chú", "exJp": "<ruby>大事<rt>だいじ</rt></ruby>なことを メモに <ruby>書<rt>か</rt></ruby>きます。", "exVi": "Viết việc quan trọng vào giấy ghi chú.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_22_91161\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_22_91161\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_22_91161)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_22_91161)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">メモ</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">📝</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">GHI CHÚ</text>\n</svg>"}, {"id": 23, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Nơi chốn", "jp": "オフィス／じむしょ", "kana": "オフィス／じむしょ", "kanji": "事務所", "romaji": "ofisu / jimusho", "vi": "Văn phòng", "exJp": "<ruby>事務所<rt>じむしょ</rt></ruby>に <ruby>資料<rt>しりょう</rt></ruby>を <ruby>取<rt>と</rt></ruby>りに <ruby>行<rt>い</rt></ruby>きます。", "exVi": "Đi đến văn phòng để lấy tài liệu.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_23_40461\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#ef4444\"/>\n      <stop offset=\"100%\" stop-color=\"#b91c1c\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_23_40461\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_23_40461)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_23_40461)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">事務所</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🏢</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">VĂN PHÒNG</text>\n</svg>"}, {"id": 24, "cat": "office", "catName": "Văn phòng & Thiết bị", "badge": "Thao tác", "jp": "プリントアウト", "kana": "プリントアウト", "kanji": "プリントアウト", "romaji": "purintoauto", "vi": "In", "exJp": "このメールを プリントアウトしてください。", "exVi": "Hãy in email này ra giúp tôi nhé.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_24_43060\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#6366f1\"/>\n      <stop offset=\"100%\" stop-color=\"#4338ca\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_24_43060\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_24_43060)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_24_43060)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">プリントア</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🖨️</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">IN RA GIẤY</text>\n</svg>"}, {"id": 25, "cat": "action", "catName": "Thao tác & Động từ", "badge": "Danh động từ (N・V3)", "jp": "しょうかいします", "kana": "しょうかいします", "kanji": "紹介します", "romaji": "shoukaishimasu", "vi": "Giới thiệu", "exJp": "<ruby>新<rt>あたら</rt></ruby>しい スタッフを <ruby>紹介<rt>しょうかい</rt></ruby>します。", "exVi": "Tôi xin phép giới thiệu nhân viên mới.", "svg": "<svg viewBox=\"0 0 240 135\" width=\"100%\" height=\"100%\" xmlns=\"http://www.w3.org/2000/svg\">\n  <defs>\n    <linearGradient id=\"bg_g_iso_25_97635\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"#4f46e5\"/>\n      <stop offset=\"100%\" stop-color=\"#3730a3\"/>\n    </linearGradient>\n    <linearGradient id=\"ped_top_iso_25_97635\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">\n      <stop offset=\"0%\" stop-color=\"rgba(255,255,255,0.4)\"/>\n      <stop offset=\"100%\" stop-color=\"rgba(255,255,255,0.12)\"/>\n    </linearGradient>\n  </defs>\n  <rect width=\"240\" height=\"135\" rx=\"14\" fill=\"url(#bg_g_iso_25_97635)\"/>\n  <circle cx=\"120\" cy=\"72\" r=\"50\" fill=\"rgba(255,255,255,0.08)\"/>\n  <ellipse cx=\"120\" cy=\"116\" rx=\"60\" ry=\"8\" fill=\"rgba(0, 0, 0, 0.3)\"/>\n  <polygon points=\"55,88 120,110 120,118 55,96\" fill=\"rgba(0,0,0,0.35)\"/>\n  <polygon points=\"120,110 185,88 185,96 120,118\" fill=\"rgba(0,0,0,0.5)\"/>\n  <polygon points=\"120,66 185,88 120,110 55,88\" fill=\"url(#ped_top_iso_25_97635)\"/>\n  <polygon points=\"120,68 181,88 120,108 59,88\" fill=\"none\" stroke=\"rgba(255,255,255,0.55)\" stroke-width=\"1.2\"/>\n  <text x=\"120\" y=\"91\" text-anchor=\"middle\" font-size=\"13\" font-weight=\"900\" fill=\"rgba(255,255,255,0.65)\" font-family=\"sans-serif\">紹介します</text>\n  <ellipse cx=\"120\" cy=\"80\" rx=\"20\" ry=\"5\" fill=\"rgba(0,0,0,0.35)\"/>\n  <g transform=\"translate(120, 46)\">\n    <circle cx=\"0\" cy=\"0\" r=\"24\" fill=\"rgba(255,255,255,0.25)\"/>\n    <text x=\"0\" y=\"11\" text-anchor=\"middle\" font-size=\"32\">🤝</text>\n  </g>\n  <rect x=\"45\" y=\"8\" width=\"150\" height=\"18\" rx=\"9\" fill=\"rgba(0, 0, 0, 0.35)\" stroke=\"rgba(255,255,255,0.25)\" stroke-width=\"1\"/>\n  <text x=\"120\" y=\"21\" text-anchor=\"middle\" fill=\"#ffffff\" font-size=\"9\" font-weight=\"800\" letter-spacing=\"1\">GIỚI THIỆU</text>\n</svg>"}];
window.VOCAB_DATA = VOCAB_DATA;
const VERB_MORPH_DATA = [{"kanji": "<ruby>使<rt>つか</rt></ruby>います", "masu": "つかいます", "vi": "Sử dụng", "col2": "<ruby>使<rt>つか</rt></ruby>って", "col3": "<ruby>使<rt>つか</rt></ruby>ってもいいですか", "col4": "<ruby>使<rt>つか</rt></ruby>ってはいけません", "col5": "どうぞ<ruby>使<rt>つか</rt></ruby>ってください", "ex": "このパソコンを<ruby>使<rt>つか</rt></ruby>ってもいいですか。―― はい、どうぞ。"}, {"kanji": "<ruby>借<rt>か</rt></ruby>ります", "masu": "かります", "vi": "Vay mượn", "col2": "<ruby>借<rt>か</rt></ruby>りて", "col3": "<ruby>借<rt>か</rt></ruby>りてもいいですか", "col4": "<ruby>借<rt>か</rt></ruby>りてはいけません", "col5": "どうぞ<ruby>借<rt>か</rt></ruby>りてください", "ex": "ペンを<ruby>借<rt>か</rt></ruby>りてもいいですか。―― ええ、いいですよ。"}, {"kanji": "<ruby>開<rt>あ</rt></ruby>けます", "masu": "あけます", "vi": "Mở cửa", "col2": "<ruby>開<rt>あ</rt></ruby>けて", "col3": "<ruby>開<rt>あ</rt></ruby>けてもいいですか", "col4": "<ruby>開<rt>あ</rt></ruby>けてはいけません", "col5": "どうぞ<ruby>開<rt>あ</rt></ruby>けてください", "ex": "<ruby>少<rt>すこ</rt></ruby>し<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてもいいですか。―― どうぞ。"}, {"kanji": "つけます", "masu": "つけます", "vi": "Bật (đèn/điều hòa)", "col2": "つけて", "col3": "つけてもいいですか", "col4": "つけてはいけません", "col5": "どうぞつけてください", "ex": "<ruby>暗<rt>くら</rt></ruby>いので<ruby>電気<rt>でんき</rt></ruby>をつけてもいいですか。"}, {"kanji": "<ruby>入<rt>はい</rt></ruby>ります", "masu": "はいります", "vi": "Đi vào phòng", "col2": "<ruby>入<rt>はい</rt></ruby>って", "col3": "<ruby>入<rt>はい</rt></ruby>ってもいいですか", "col4": "<ruby>入<rt>はい</rt></ruby>ってはいけません", "col5": "どうぞお<ruby>入<rt>はい</rt></ruby>りください", "ex": "<ruby>失礼<rt>しつれい</rt></ruby>します。<ruby>入<rt>はい</rt></ruby>ってもいいですか。"}];
const QUIZ_QUESTIONS = [{"id": 1, "category": "Ngữ pháp: V-てもいいですか", "q": "この コンピューター、[____] も いいですか。", "options": ["<ruby>使<rt>つか</rt></ruby>って", "<ruby>使<rt>つか</rt></ruby>いた", "<ruby>使<rt>つか</rt></ruby>います", "<ruby>使<rt>つか</rt></ruby>う"], "correct": 0, "explain": "Cấu trúc xin phép lịch sự: V-て + もいいですか ➔ 「<ruby>使<rt>つか</rt></ruby>ってもいいですか」 (Tôi dùng có được không?)."}, {"id": 2, "category": "Ngữ pháp: V-てもいいですか", "q": "ペンを [____] も いいですか (<ruby>借<rt>か</rt></ruby>りる)。", "options": ["<ruby>借<rt>か</rt></ruby>りて", "<ruby>借<rt>か</rt></ruby>って", "<ruby>借<rt>か</rt></ruby>りた", "<ruby>借<rt>か</rt></ruby>る"], "correct": 0, "explain": "Động từ nhóm 2: <ruby>借<rt>か</rt></ruby>ります ➔ chia thể Te là 「<ruby>借<rt>か</rt></ruby>りて」 + もいいですか."}, {"id": 3, "category": "Ngữ pháp: Phản hồi xin phép", "q": "「<ruby>使<rt>つか</rt></ruby>ってもいいですか。」――「[____]、どうぞ。」", "options": ["はい", "いいえ", "だめ", "ごめん"], "correct": 0, "explain": "Khi đồng ý cho phép ai đó sử dụng đồ vật: 「はい、どうぞ」 (Vâng, xin mời)."}, {"id": 4, "category": "Ngữ pháp: Từ chối khéo", "q": "Khi đang bận dùng đồ mà người khác muốn mượn, cách từ chối khéo léo nhất là:", "options": ["すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っているんです", "<ruby>絶対<rt>ぜったい</rt></ruby>に だめです", "<ruby>嫌<rt>いや</rt></ruby>です", "<ruby>使<rt>つか</rt></ruby>わないでください"], "correct": 0, "explain": "Cách từ chối lịch sự trong văn hóa Nhật: 「すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っているんです」 (Xin lỗi, hiện tại tôi đang dùng mất rồi)."}, {"id": 5, "category": "Ngữ pháp: V-てはいけません", "q": "ここで <ruby>写真<rt>しゃしん</rt></ruby>を [____] は いけません。", "options": ["<ruby>撮<rt>と</rt></ruby>って", "<ruby>撮<rt>と</rt></ruby>り", "<ruby>撮<rt>と</rt></ruby>る", "<ruby>撮<rt>と</rt></ruby>った"], "correct": 0, "explain": "Mẫu câu cấm đoán: V-て + はいけません ➔ 「<ruby>撮<rt>と</rt></ruby>っては いけません」 (Không được chụp ảnh)."}, {"id": 6, "category": "Từ vựng: Thiết bị văn phòng", "q": "<ruby>書類<rt>しょるい</rt></ruby>を たくさん <ruby>紙<rt>かみ</rt></ruby>に コピーする <ruby>機械<rt>きかい</rt></ruby>は [____] です。", "options": ["コピー<ruby>機<rt>き</rt></ruby>", "エアコン", "キャビネット", "テレビ"], "correct": 0, "explain": "Máy in và sao chép tài liệu là 「コピー<ruby>機<rt>き</rt></ruby>」 (コピーき - Máy photocopy)."}, {"id": 7, "category": "Từ vựng: Văn phòng", "q": "パソコンを <ruby>開<rt>ひら</rt></ruby>く ときに <ruby>入力<rt>にゅうりょく</rt></ruby>する <ruby>秘密<rt>ひみつ</rt></ruby>の <ruby>文字<rt>もじ</rt></ruby>は [____] です。", "options": ["パスワード", "チケット", "スケジュール", "フライト"], "correct": 0, "explain": "Mật khẩu máy tính là 「パスワード」 (Password)."}, {"id": 8, "category": "Từ vựng: Nhân sự", "q": "<ruby>社長<rt>しゃちょう</rt></ruby>の <ruby>身<rt>み</rt></ruby>の<ruby>回<rt>まわ</rt></ruby>りの <ruby>仕事<rt>しごと</rt></ruby>を <ruby>手伝<rt>てつだ</rt></ruby>う <ruby>人<rt>ひと</rt></ruby>は [____] です。", "options": ["<ruby>秘書<rt>ひしょ</rt></ruby>", "ドライバー", "<ruby>受付<rt>うけつけ</rt></ruby>", "<ruby>学生<rt>がくせい</rt></ruby>"], "correct": 0, "explain": "Người làm trợ lý, thư ký hỗ trợ giám đốc là 「<ruby>秘書<rt>ひしょ</rt></ruby>」 (ひしょ)."}, {"id": 9, "category": "Giao tiếp: Kết thúc công tác", "q": "Khi chào tạm biệt chi nhánh sau chuyến công tác, câu nói cảm ơn chuẩn là:", "options": ["<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました", "ごちそうさまでした", "いただきます", "お<ruby>大事<rt>だいじ</rt></ruby>に"], "correct": 0, "explain": "「<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました」 (Cảm ơn anh chị đã hết lòng giúp đỡ tôi)."}, {"id": 10, "category": "Giao tiếp: Nhờ chuyển lời", "q": "「<ruby>本社<rt>ほんしゃ</rt></ruby>の <ruby>皆<rt>みな</rt></ruby>さんに よろしく [____] ください。」", "options": ["お<ruby>伝<rt>つた</rt></ruby>え", "<ruby>言<rt>い</rt></ruby>って", "<ruby>話<rt>はな</rt></ruby>して", "<ruby>書<rt>か</rt></ruby>いて"], "correct": 0, "explain": "Nhờ chuyển lời thăm hỏi lịch sự: 「よろしくお<ruby>伝<rt>つた</rt></ruby>えください」 (おつたえください)."}, {"id": 11, "category": "Chữ Hán Bài 14: 自 & 分", "q": "Từ 「じぶん」 (Bản thân mình) viết Hán tự là:", "options": ["自分", "白分", "自刀", "目分"], "correct": 0, "explain": "「じぶん」 viết chữ Hán là 「自分」 (TỰ PHÂN: <ruby>自<rt>じ</rt></ruby><ruby>分<rt>ぶん</rt></ruby>)."}, {"id": 12, "category": "Chữ Hán Bài 14: 電 & 話", "q": "Từ 「でんわ」 (Điện thoại) gồm 2 chữ Hán nào?", "options": ["電話", "電気", "電車", "電送"], "correct": 0, "explain": "「でんわ」 là 「電話」 (<ruby>電<rt>でん</rt></ruby><ruby>話<rt>わ</rt></ruby> - cả 2 chữ đều có 13 nét)."}, {"id": 13, "category": "Chữ Hán Bài 14: 使 (Sử)", "q": "Động từ 「つかいます」 (Sử dụng) có chữ Hán là:", "options": ["使います", "借ります", "送ります", "作ります"], "correct": 0, "explain": "「つかいます」 là 「使います」 (<ruby>使<rt>つか</rt></ruby>います - SỬ, 8 nét)."}, {"id": 14, "category": "Chữ Hán Bài 14: 借 (Tá)", "q": "Động từ 「かります」 (Vay mượn) có chữ Hán là:", "options": ["借ります", "使います", "送ります", "働きます"], "correct": 0, "explain": "「かります」 là 「借ります」 (<ruby>借<rt>か</rt></ruby>ります - TÁ, 10 nét, bộ Nhân đứng 亻 + chữ Tích 昔)."}, {"id": 15, "category": "Chữ Hán Bài 14: 送 (Tống)", "q": "Động từ 「おくります」 trong 「メールを 送ります」 có chữ Hán là:", "options": ["送ります", "通ります", "連ります", "返ります"], "correct": 0, "explain": "「おくります」 viết chữ Hán là 「送ります」 (<ruby>送<rt>おく</rt></ruby>ります - TỐNG, 9 nét)."}];
const DIALOGUE_STEPS = [{"options": [{"text": "すみません、このパソコンをお<ruby>借<rt>か</rt></ruby>りしてもいいですか。", "vi": "Xin lỗi cô, tôi mượn chiếc máy tính này một chút có được không ạ?", "replyAvatar": "👩‍💼", "replyNpc": "Kathy", "replyText": "はい、どうぞ！パスワードは<ruby>画面<rt>がめん</rt></ruby>の<ruby>横<rt>よこ</rt></ruby>にメモしてありますよ。", "replyVi": "Vâng, xin mời anh cứ tự nhiên dùng! Mật khẩu được ghi chú ngay bên cạnh màn hình đó ạ."}, {"text": "<ruby>資料<rt>しりょう</rt></ruby>を<ruby>印刷<rt>いんさつ</rt></ruby>したいのですが、プリンターを<ruby>使<rt>つか</rt></ruby>ってもいいですか。", "vi": "Tôi muốn in một số tài liệu, tôi dùng máy in có được không ạ?", "replyAvatar": "👩‍💼", "replyNpc": "Kathy", "replyText": "ええ、<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>です。あちらのコピー<ruby>機<rt>き</rt></ruby>に<ruby>繋<rt>つな</rt></ruby>がっていますよ。", "replyVi": "Vâng, được chứ ạ. Máy tính đã được kết nối với chiếc máy in đằng kia rồi đó."}]}, {"npcName": "Kathy", "avatar": "👩‍💼", "npcText": "<ruby>出張<rt>しゅっちょう</rt></ruby>のお<ruby>仕事<rt>しごと</rt></ruby>は<ruby>順調<rt>じゅんちょう</rt></ruby>に<ruby>進<rt>すす</rt></ruby>みましたか。もうすぐ<ruby>空港<rt>くうこう</rt></ruby>へ<ruby>向<rt>む</rt></ruby>かいますね。", "npcVi": "Công việc trong chuyến công tác diễn ra thuận lợi chứ ạ? Anh sắp sửa ra sân bay rồi nhỉ.", "options": [{"text": "はい、<ruby>大変<rt>たいへん</rt></ruby>お<ruby>世話<rt>せわ</rt></ruby>になりました！<ruby>本社<rt>ほんしゃ</rt></ruby>の<ruby>皆<rt>みな</rt></ruby>さんによろしくお<ruby>伝<rt>つた</rt></ruby>えください。", "vi": "Vâng, cảm ơn mọi người đã hết lòng giúp đỡ tôi! Cho tôi gửi lời chào hỏi thăm tới mọi người ở trụ sở chính nhé.", "replyAvatar": "👩‍💼", "replyNpc": "Kathy", "replyText": "はい、<ruby>必<rt>かなら</rt></ruby>ず<ruby>伝<rt>つた</rt></ruby>えます！お<ruby>気<rt>き</rt></ruby>をつけてお<ruby>帰<rt>かえ</rt></ruby>りくださいね。", "replyVi": "Vâng, tôi nhất định sẽ chuyển lời ạ! Chúc anh thượng lộ bình an nhé."}, {"text": "おかげさまで<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>終<rt>お</rt></ruby>わりました。また<ruby>東京<rt>とうきょう</rt></ruby>で<ruby>会<rt>あ</rt></ruby>いましょう！", "vi": "Nhờ có mọi người mà công việc đã hoàn thành tốt đẹp. Hẹn sớm gặp lại cô tại Tokyo nhé!", "replyAvatar": "👩‍💼", "replyNpc": "Kathy", "replyText": "こちらこそ！またのお<ruby>越<rt>こ</rt></ruby>しを<ruby>心<rt>こころ</rt></ruby>よりお<ruby>待<rt>ま</rt></ruby>ちしております。", "replyVi": "Chúng tôi cũng rất vinh hạnh! Rất mong được đón tiếp anh trong những lần tới."}]}];


// Furigana Toggle Logic
function toggleFurigana() {
    document.body.classList.toggle('hide-furigana');
    const isHidden = document.body.classList.contains('hide-furigana');
    const btn = document.getElementById('btnFuriganaToggle');
    const label = document.getElementById('furiganaBtnLabel');
    if (btn && label) {
        if (isHidden) {
            btn.classList.add('off');
            label.textContent = 'Furigana: TẮT';
        } else {
            btn.classList.remove('off');
            label.textContent = 'Furigana: BẬT';
        }
    }
    try { localStorage.setItem('marugoto_furigana', isHidden ? 'off' : 'on'); } catch(e) {}
}

(function initFuriganaPref() {
    try {
        const pref = localStorage.getItem('marugoto_furigana');
        if (pref === 'off') {
            document.body.classList.add('hide-furigana');
            window.addEventListener('DOMContentLoaded', () => {
                const btn = document.getElementById('btnFuriganaToggle');
                const label = document.getElementById('furiganaBtnLabel');
                if (btn && label) {
                    btn.classList.add('off');
                    label.textContent = 'Furigana: TẮT';
                }
            });
        }
    } catch(e) {}
})();

// Tokyo Audio Speech Synthesis (Dual Engine via audio-engine.js)
function speakText(text) {
    if (window.speakJapanese) {
        window.speakJapanese(text);
    }
}

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
    document.getElementById('morphTe').innerHTML = v.col2;
    document.getElementById('morphTeIki').innerHTML = v.col3;
    document.getElementById('morphTeKi').innerHTML = v.col4;
    document.getElementById('morphMashou').innerHTML = v.col5;
    document.getElementById('morphExText').innerHTML = v.ex;
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
                🎉 Hoàn thành xuất sắc đoạn hội thoại tình huống Bài 14!
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

    const userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble user';
    userBubble.innerHTML = `
        <div class="chat-avatar">🧑</div>
        <div class="chat-msg">
            <div class="chat-name">Bạn (Tôi)</div>
            <div class="chat-jp">${opt.text}</div>
            <div class="chat-vi">${opt.vi}</div>
        </div>
    `;
    chat.appendChild(userBubble);
    chat.scrollTop = chat.scrollHeight;
    speakText(opt.text);

    setTimeout(() => {
        const npcBubble = document.createElement('div');
        npcBubble.className = 'chat-bubble bot';
        npcBubble.innerHTML = `
            <div class="chat-avatar">${opt.replyAvatar || '👩'}</div>
            <div class="chat-msg">
                <div class="chat-name">${opt.replyNpc}</div>
                <div class="chat-jp">${opt.replyText}</div>
                <div class="chat-vi">${opt.replyVi}</div>
            </div>
        `;
        chat.appendChild(npcBubble);
        chat.scrollTop = chat.scrollHeight;
        speakText(opt.replyText);

        if (stepIdx + 1 < DIALOGUE_STEPS.length) {
            setTimeout(() => {
                const nextPrompt = DIALOGUE_STEPS[stepIdx + 1];
                const promptBubble = document.createElement('div');
                promptBubble.className = 'chat-bubble bot';
                promptBubble.innerHTML = `
                    <div class="chat-avatar">${nextPrompt.avatar || '👨'}</div>
                    <div class="chat-msg">
                        <div class="chat-name">${nextPrompt.npcName}</div>
                        <div class="chat-jp">${nextPrompt.npcText}</div>
                        <div class="chat-vi">${nextPrompt.npcVi}</div>
                    </div>
                `;
                chat.appendChild(promptBubble);
                chat.scrollTop = chat.scrollHeight;
                speakText(nextPrompt.npcText);
                renderDialogueOptions(stepIdx + 1);
            }, 1000);
        } else {
            renderDialogueOptions(stepIdx + 1);
        }
    }, 600);
}

// NPBS Quiz Logic
const NPBS_QUESTIONS = [
    {
        id: 1,
        q: "この 会社に（　　）、10年に なります。",
        options: ["入ります", "入って", "入る", "入った"],
        correct: 1,
        explain: "Cấu trúc diễn tả mốc thời gian trôi qua kể từ khi bắt đầu làm V: <strong>V-て + [Khoảng thời gian] + に なります</strong>. Động từ chia thể Te: <code>入って</code>."
    },
    {
        id: 2,
        q: "日本語の 勉強を はじめて 3か月（　　）なります。",
        options: ["で", "を", "に", "が"],
        correct: 2,
        explain: "Trợ từ đi trước <code>なります</code> để chỉ mốc thời gian tích lũy là <strong>に</strong> (<code>3か月に なります</code>)."
    },
    {
        id: 3,
        q: "「すみません。ペンを かりても いいですか。」――「（　　）」",
        options: ["はい、だめです。", "はい、どうぞ。", "いいえ、いいですよ。", "すみません、どうぞ。"],
        correct: 1,
        explain: "Đáp lại lời xin phép một cách đồng ý, tự nhiên và lịch sự: <strong>「はい、どうぞ。」</strong> hoặc <strong>「はい、いいですよ。」</strong>."
    },
    {
        id: 4,
        q: "「先生、テストの とき、辞書を（　　）も いいですか。」",
        options: ["使う", "使って", "使います", "使った"],
        correct: 1,
        explain: "Mẫu câu xin phép: <strong>V-て + もいいですか</strong>. Động từ <code>使います</code> (Nhóm 1) chia thể Te là <code>使って</code>."
    },
    {
        id: 5,
        q: "日本に 来て 2年に なります。Câu này mang ý nghĩa gì?",
        options: ["Tôi sẽ đến Nhật trong 2 năm nữa.", "Đã 2 năm kể từ khi tôi sang Nhật.", "Tôi ở Nhật được 2 ngày.", "Tôi muốn sang Nhật 2 năm."],
        correct: 1,
        explain: "<code>Vて ～年に なります</code> diễn tả khoảng thời gian kể từ thời điểm V bắt đầu xảy ra: <em>'Đã 2 năm kể từ khi tôi sang Nhật'</em>."
    }
];

let npbsAnswers = {};

function renderNpbsQuiz() {
    const container = document.getElementById('npbsQuizBox');
    if (!container) return;
    container.innerHTML = NPBS_QUESTIONS.map(q => `
        <div style="background: rgba(255,255,255,0.12); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.25); border-radius: 14px; padding: 18px; margin-bottom: 14px;" id="npbsCard_${q.id}">
            <div style="font-size: 0.85rem; font-weight: 700; opacity: 0.85; margin-bottom: 6px;">CÂU ${q.id} / ${NPBS_QUESTIONS.length} • THỬ THÁCH NPBS</div>
            <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 12px;" class="jp-text">${q.q}</div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 8px;">
                ${q.options.map((opt, idx) => `
                    <button type="button" onclick="answerNpbs(${q.id}, ${idx}, this)" style="background: rgba(255,255,255,0.9); color: #1e1b4b; border: none; padding: 10px 14px; border-radius: 8px; font-weight: 700; font-size: 0.95rem; cursor: pointer; text-align: left; transition: all 0.2s;" onmouseover="this.style.background='#ffffff'" onmouseout="this.style.background='rgba(255,255,255,0.9)'">
                        ${['A', 'B', 'C', 'D'][idx]}. ${opt}
                    </button>
                `).join('')}
            </div>
            <div id="npbsFb_${q.id}" style="display: none; margin-top: 10px; padding: 10px 14px; border-radius: 8px; font-size: 0.92rem; font-weight: 600;"></div>
        </div>
    `).join('');
}

function answerNpbs(qId, selectedIdx, btn) {
    if (npbsAnswers[qId] !== undefined) return;
    npbsAnswers[qId] = selectedIdx;
    const q = NPBS_QUESTIONS.find(item => item.id === qId);
    const card = document.getElementById(`npbsCard_${qId}`);
    const buttons = card.querySelectorAll('button');
    const fb = document.getElementById(`npbsFb_${qId}`);

    buttons.forEach((b, idx) => {
        b.disabled = true;
        if (idx === q.correct) {
            b.style.background = '#10b981';
            b.style.color = '#ffffff';
        } else if (idx === selectedIdx) {
            b.style.background = '#ef4444';
            b.style.color = '#ffffff';
        } else {
            b.style.opacity = '0.5';
        }
    });

    fb.style.display = 'block';
    if (selectedIdx === q.correct) {
        fb.style.background = 'rgba(16, 185, 129, 0.25)';
        fb.style.border = '1px solid #34d399';
        fb.innerHTML = `✓ <strong>Chính xác!</strong> ${q.explain}`;
    } else {
        fb.style.background = 'rgba(239, 68, 68, 0.25)';
        fb.style.border = '1px solid #f87171';
        fb.innerHTML = `✕ <strong>Chưa chính xác!</strong> ${q.explain}`;
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
            scoreMsg.textContent = "🌟 Tuyệt vời! Bạn đã thành thạo toàn bộ kiến thức Bài 14!";
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
    renderNpbsQuiz();
});
