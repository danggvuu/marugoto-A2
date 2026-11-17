# -*- coding: utf-8 -*-
"""
Generator for Marugoto A2-2 Lesson 1 and Lesson 2:
- lessons/Marugoto_A2_2_Lesson_1.html
- lessons/Marugoto_A2_2_Lesson_2.html
- assets/js/lessons/lesson_a2_2_01.js
- assets/js/lessons/lesson_a2_2_02.js
- data/kanji_vocab_a2_2.json
"""

import json
import hashlib
from html import escape
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]

# -------------------------------------------------------------
# LESSON 1 DATA
# -------------------------------------------------------------
L1_VOCAB = [
    {"jp": "自己紹介", "kana": "じこしょうかい", "kanji": "自己紹介", "romaji": "jikoshoukai", "vi": "Giới thiệu bản thân", "icon": "🤝"},
    {"jp": "秘密", "kana": "ひみつ", "kanji": "秘密", "romaji": "himitsu", "vi": "Bí mật", "icon": "🤫"},
    {"jp": "国際交流", "kana": "こくさいこうりゅう", "kanji": "国際交流", "romaji": "kokusaikouryuu", "vi": "Giao lưu quốc tế", "icon": "🌐"},
    {"jp": "電気店", "kana": "でんきてん", "kanji": "電気店", "romaji": "denkiten", "vi": "Cửa hàng điện", "icon": "💡"},
    {"jp": "電気製品", "kana": "でんきせいひん", "kanji": "電気製品", "romaji": "denkiseihin", "vi": "Sản phẩm điện tử", "icon": "📱"},
    {"jp": "読書", "kana": "どくしょ", "kanji": "読書", "romaji": "dokusho", "vi": "Đọc sách", "icon": "📚"},
    {"jp": "店をやります", "kana": "みせを やります", "kanji": "店をやります", "romaji": "mise o yarimasu", "vi": "Làm, mở nhà hàng / cửa tiệm", "icon": "🏪"},
    {"jp": "翻訳をします", "kana": "ほんやくを します", "kanji": "翻訳をします", "romaji": "honyaku o shimasu", "vi": "Biên dịch (dịch viết)", "icon": "📝"},
    {"jp": "興味", "kana": "きょうみ", "kanji": "興味", "romaji": "kyoumi", "vi": "Hứng thú", "icon": "✨"},
    {"jp": "村", "kana": "むら", "kanji": "村", "romaji": "mura", "vi": "Làng", "icon": "🏡"},
    {"jp": "島", "kana": "しま", "kanji": "島", "romaji": "shima", "vi": "Đảo", "icon": "🏝️"},
    {"jp": "年", "kana": "とし", "kanji": "年", "romaji": "toshi", "vi": "Tuổi", "icon": "🎂"},
    {"jp": "生まれます", "kana": "うまれます", "kanji": "生まれます", "romaji": "umaremasu", "vi": "Được sinh ra", "icon": "👶"},
    {"jp": "優しい", "kana": "やさしい", "kanji": "優しい", "romaji": "yasashii", "vi": "Hiền lành, tốt bụng", "icon": "😊"},
    {"jp": "健康（な）", "kana": "けんこう（な）", "kanji": "健康（な）", "romaji": "kenkou(na)", "vi": "Khỏe mạnh, lành mạnh", "icon": "💪"},
    {"jp": "真面目（な）", "kana": "まじめ（な）", "kanji": "真面目（な）", "romaji": "majime(na)", "vi": "Nghiêm túc, chăm chỉ", "icon": "👔"},
    {"jp": "明るい", "kana": "あかるい", "kanji": "明るい", "romaji": "akarui", "vi": "Sáng sủa, tươi vui", "icon": "☀️"},
    {"jp": "意味", "kana": "いみ", "kanji": "意味", "romaji": "imi", "vi": "Ý nghĩa", "icon": "💡"},
    {"jp": "作家", "kana": "さっか", "kanji": "作家", "romaji": "sakka", "vi": "Nhà văn, tác giả", "icon": "🖋️"},
    {"jp": "住んでいるところ", "kana": "すんでいるところ", "kanji": "住んでいるところ", "romaji": "sunde iru tokoro", "vi": "Nơi đang sinh sống", "icon": "🏘️"}
]

L1_VERBS = [
    {"masu": "やります", "vi": "Làm / mở (tiệm)", "te": "やって", "form1": "やっています", "form2": "やった", "form3": "やる"},
    {"masu": "ほんやくします", "vi": "Biên dịch", "te": "ほんやくして", "form1": "ほんやくしています", "form2": "ほんやくした", "form3": "ほんやくする"},
    {"masu": "うまれます", "vi": "Được sinh ra", "te": "うまれて", "form1": "うまれています", "form2": "うまれた", "form3": "うまれる"},
    {"masu": "そだちます", "vi": "Lớn lên", "te": "そだって", "form1": "そだっています", "form2": "そだった", "form3": "そだつ"},
    {"masu": "すみます", "vi": "Sinh sống", "te": "すんで", "form1": "すんでいます", "form2": "すんだ", "form3": "すむ"}
]

L1_KANJI_LIST = [
    {"stt": 1, "word": "紹介", "kana": "しょうかい", "hv": "THIỆU GIỚI", "mean": "Giới thiệu"},
    {"stt": 2, "word": "自己紹介", "kana": "じこしょうかい", "hv": "TỰ KỶ THIỆU GIỚI", "mean": "Giới thiệu bản thân"},
    {"stt": 3, "word": "名前", "kana": "なまえ", "hv": "DANH TIỀN", "mean": "Tên"},
    {"stt": 4, "word": "有名", "kana": "ゆうめい", "hv": "HỮU DANH", "mean": "Nổi tiếng"},
    {"stt": 5, "word": "意味", "kana": "いみ", "hv": "Ý VỊ", "mean": "Ý nghĩa"},
    {"stt": 6, "word": "部屋", "kana": "へや", "hv": "BỘ ỐC", "mean": "Căn phòng"},
    {"stt": 7, "word": "本屋", "kana": "ほんや", "hv": "BỔN ỐC", "mean": "Tiệm sách"},
    {"stt": 8, "word": "近い", "kana": "ちかい", "hv": "CẬN", "mean": "Gần"},
    {"stt": 9, "word": "最近", "kana": "さいきん", "hv": "TỐI CẬN", "mean": "Gần đây"},
    {"stt": 10, "word": "近所", "kana": "きんじょ", "hv": "CẬN SỞ", "mean": "Hàng xóm, lân cận"},
    {"stt": 11, "word": "住みます", "kana": "すみます", "hv": "TRÚ", "mean": "Sống"},
    {"stt": 12, "word": "住所", "kana": "じゅうしょ", "hv": "TRÚ SỞ", "mean": "Địa chỉ"},
    {"stt": 13, "word": "働きます", "kana": "はたらきます", "hv": "ĐỘNG", "mean": "Làm việc"},
    {"stt": 14, "word": "一番", "kana": "いちばん", "hv": "NHẤT PHIÊN", "mean": "Nhất, số một"},
    {"stt": 15, "word": "一番目", "kana": "いちばんめ", "hv": "NHẤT PHIÊN MỤC", "mean": "Thứ nhất"}
]

L1_KANJI_CARDS = [
    {"char": "己", "hv": "Kỉ (Kỷ)", "strokes": 3, "kun": "おのれ", "on": "こ、き", "ex": "自己紹介 (じこしょうかい - giới thiệu bản thân), 利己 (りこ - ích kỷ)", "mnemonic": "Hình dáng uốn cong của dải lụa hoặc bản thân con người đang cúi mình tự soi chiếu KỶ niệm."},
    {"char": "自", "hv": "Tự", "strokes": 6, "kun": "みずか・ら", "on": "じ、し", "ex": "自己紹介 (じこしょうかい), 自分 (じぶん - bản thân), 自由 (じゆう - tự do)", "mnemonic": "Chiếc mũi (Tự) chỉ vào chính bản thân mình (Tự mình)."},
    {"char": "紹", "hv": "Thiệu", "strokes": 11, "kun": "ー", "on": "しょう", "ex": "紹介 (しょうかい - giới thiệu), 自己紹介 (じこしょうかい)", "mnemonic": "Dùng sợi tơ (糸) kết nối và chiêu (召) mời người mới đến làm quen (Thiệu)."},
    {"char": "介", "hv": "Giới", "strokes": 4, "kun": "ー", "on": "かい", "ex": "紹介 (しょうかい), 自己紹介 (じこしょうかい), 魚介 (ぎょかい)", "mnemonic": "Hình người (人) đứng ở giữa làm cầu nối hai bên (Giới)."},
    {"char": "名", "hv": "Danh", "strokes": 6, "kun": "な", "on": "めい、みょう", "ex": "名前 (なまえ - tên), 有名 (ゆうめい - nổi tiếng), 名字 (みょうじ - họ)", "mnemonic": "Buổi tối (夕) không thấy rõ nhau phải dùng miệng (口) gọi TÊN (Danh)."},
    {"char": "前", "hv": "Tiền", "strokes": 9, "kun": "まえ", "on": "ぜん", "ex": "名前 (なまえ - tên), 前 (まえ - phía trước), 午前 (ごぜん - buổi sáng)", "mnemonic": "Cắt tóc bằng dao (刂) trước trăng (月) sáng hướng về phía TRƯỚC (Tiền)."},
    {"char": "有", "hv": "Hữu", "strokes": 6, "kun": "あ・る", "on": "ゆう、う", "ex": "有名 (ゆうめい - nổi tiếng), 有料 (ゆうりょう - có phí), 有力 (ゆうりょく)", "mnemonic": "Bàn tay cầm miếng thịt (nguyệt) tức là CÓ (Hữu)."},
    {"char": "意", "hv": "Ý", "strokes": 13, "kun": "ー", "on": "い", "ex": "意味 (いみ - ý nghĩa), 意見 (いけん - ý kiến), 用意 (ようい - chuẩn bị)", "mnemonic": "Âm thanh (音) phát ra từ trái tim (心) chính là Ý niệm."},
    {"char": "味", "hv": "Vị", "strokes": 8, "kun": "あじ、あじ・わう", "on": "み", "ex": "意味 (いみ - ý nghĩa), 興味 (きょうみ - hứng thú), 味 (あじ - mùi vị)", "mnemonic": "Cái miệng (口) nếm thử quả trên cây chưa (未) chín là nếm VỊ."},
    {"char": "部", "hv": "Bộ", "strokes": 11, "kun": "ー", "on": "ぶ", "ex": "部屋 (へや - căn phòng), 全部 (ぜんぶ - toàn bộ), 部長 (ぶちょう - trưởng phòng)", "mnemonic": "Đứng (立) nói (口) tại ấp (阝) phân chia thành từng BỘ phận / căn phòng."},
    {"char": "屋", "hv": "Ốc", "strokes": 9, "kun": "や", "on": "おく", "ex": "部屋 (へや - căn phòng), 本屋 (ほんや - tiệm sách), 屋上 (おくじょう - sân thượng)", "mnemonic": "Ngôi nhà có mái che (尸) nơi người ta đến (至) để ở hoặc buôn bán (Ốc)."},
    {"char": "本", "hv": "Bản / Bổn", "strokes": 5, "kun": "もと", "on": "ほん", "ex": "本屋 (ほんや - tiệm sách), 日本 (にほん - Nhật Bản), 本 (ほん - quyển sách)", "mnemonic": "Cây cối (木) có thêm một vạch ở gốc là CĂN BẢN, gỗ làm ra SÁCH."},
    {"char": "近", "hv": "Cận", "strokes": 7, "kun": "ちか・い", "on": "きん", "ex": "近い (ちかい - gần), 最近 (さいきん - gần đây), 近所 (きんじょ - hàng xóm)", "mnemonic": "Chiếc rìu (斤) đang đi (辶) tới rất GẦN (Cận)."},
    {"char": "最", "hv": "Tối", "strokes": 12, "kun": "もっと・も", "on": "さい", "ex": "最近 (さいきん - gần đây), 最初 (さいしょ - đầu tiên), 最高 (さいこう - tuyệt nhất)", "mnemonic": "Mặt trời (日) cầm giữ (取) lấy vị trí CAO NHẤT (Tối)."},
    {"char": "所", "hv": "Sở", "strokes": 8, "kun": "ところ", "on": "しょ", "ex": "近所 (きんじょ - hàng xóm), 住所 (じゅうしょ - địa chỉ), 場所 (ばしょ - địa điểm)", "mnemonic": "Cánh cửa (戶) có chiếc rìu (斤) đánh dấu NƠI CHỐN (Sở)."},
    {"char": "住", "hv": "Trú", "strokes": 7, "kun": "す・む", "on": "じゅう", "ex": "住みます (すみます - sống), 住所 (じゅうしょ - địa chỉ), 住民 (じゅうみん - cư dân)", "mnemonic": "Người (亻) làm chủ (主) nơi mình SINH SỐNG (Trú)."},
    {"char": "働", "hv": "Động", "strokes": 13, "kun": "はたら・く", "on": "どう", "ex": "働きます (はたらきます - làm việc), 労働 (ろうどう - lao động)", "mnemonic": "Người (亻) dùng sức lực (力) chuyển động (動) để LÀM VIỆC (Động)."},
    {"char": "番", "hv": "Phiên", "strokes": 12, "kun": "ー", "on": "ばん", "ex": "一番 (いちばん - nhất, số một), 一番目 (いちばんめ - thứ nhất), 番号 (ばんごう - số hiệu)", "mnemonic": "Phân chia (釆) từng thửa ruộng (田) theo số thứ tự (Phiên)."},
    {"char": "目", "hv": "Mục", "strokes": 5, "kun": "め", "on": "もく", "ex": "一番目 (いちばんめ - thứ nhất), 目的 (もくてき - mục đích), 目 (め - mắt)", "mnemonic": "Hình vẽ con mắt người (Mục) dùng để nhìn ngắm và chỉ số thứ tự."}
]

L1_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "「ハノイ」というのは、「川の内側」[____] いう意味です。",
        "options": ["と", "で", "に", "を"],
        "correct": 0,
        "explain": "Mẫu câu giải thích định nghĩa, ý nghĩa: 『～というのは、...という意味です』. Chữ 「と」 làm trợ từ trích dẫn nội dung ý nghĩa."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "わたしは ベトナムの ダナン [____] うまれました。",
        "options": ["で", "に", "を", "へ"],
        "correct": 0,
        "explain": "Nơi diễn ra hành động/sự kiện sinh ra 『生まれます』 dùng trợ từ 「で」 (ở tại đâu). Khác với nơi cư trú lâu dài 『住んでいます』 dùng 「に」."
    },
    {
        "id": 3,
        "category": "Ngữ pháp",
        "q": "日本の 歴史や 文学 [____] きょうみが あります。",
        "options": ["に", "で", "を", "が"],
        "correct": 0,
        "explain": "Cấu trúc có hứng thú với điều gì: 『[Danh từ] に 興味 (きょうみ) が あります』. Trợ từ đi kèm đối tượng hứng thú là 「に」."
    },
    {
        "id": 4,
        "category": "Từ vựng",
        "q": "山田さんは いつも えがおで、とても [____] 人です。",
        "options": ["あかるい", "ひみつ", "むら", "とし"],
        "correct": 0,
        "explain": "Người luôn tươi cười, vui vẻ, hoạt bát được miêu tả bằng tính từ 「明るい (あかるい)」 (tươi sáng, tươi vui)."
    },
    {
        "id": 5,
        "category": "Từ vựng",
        "q": "だれにも 言わないでください。これは 二人の [____] です。",
        "options": ["ひみつ", "どくしょ", "きょうみ", "いみ"],
        "correct": 0,
        "explain": "Không được nói cho ai biết vì đây là 'bí mật' giữa hai người: 「秘密 (ひみつ)」."
    },
    {
        "id": 6,
        "category": "Ngữ pháp",
        "q": "わたしの 友だちは まじめ [____]、とても 親切です。",
        "options": ["で", "くて", "な", "に"],
        "correct": 0,
        "explain": "Nối hai tính từ, trong đó 「真面目 (まじめ)」 là tính từ đuôi な, khi liên kết đổi thành 「まじめで」."
    },
    {
        "id": 7,
        "category": "Từ vựng",
        "q": "週末は 家で [____] を します。小説が 大好きです。",
        "options": ["どくしょ", "ほんやく", "じこしょうかい", "さっか"],
        "correct": 0,
        "explain": "Thích đọc tiểu thuyết nên cuối tuần hay đọc sách: 「読書 (どくしょ) を します」."
    },
    {
        "id": 8,
        "category": "Hội thoại",
        "q": "「はじめまして。ナムです。どうぞ よろしく。」 ―― 「[____]」",
        "options": ["ナムさんですね。いい 名前ですね。", "どういたしまして。", "こちらこそ、お元気ですか。", "ごめんください。"],
        "correct": 0,
        "explain": "Trong tình huống gặp gỡ lần đầu, khi đối phương giới thiệu tên, người Nhật thường khen tên thân thiện: 『...さんですね。いいお名前ですね』."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "将来、自分で 日本料理の [____] を やりたいです。",
        "options": ["みせ", "むら", "しま", "とし"],
        "correct": 0,
        "explain": "Kinh doanh, mở quán ăn/nhà hàng dùng cụm từ 「店 (みせ) を やります」."
    },
    {
        "id": 10,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「紹介」 có cách đọc chuẩn là gì?",
        "options": ["しょうかい", "じこかい", "そくかい", "しょうけい"],
        "correct": 0,
        "explain": "紹介 đọc là 「しょうかい」 (THIỆU GIỚI - Giới thiệu)."
    },
    {
        "id": 11,
        "category": "Chữ Hán",
        "q": "Từ 「有名」 (HỮU DANH) có nghĩa là gì?",
        "options": ["Nổi tiếng", "Tên tuổi", "Ý nghĩa", "Hàng xóm"],
        "correct": 0,
        "explain": "有名 (ゆうめい) nghĩa là nổi tiếng, có tiếng tăm."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Cách đọc của chữ Hán 「近所」 là gì?",
        "options": ["きんじょ", "ちかじょ", "きんしょ", "ちかところ"],
        "correct": 0,
        "explain": "近所 đọc là 「きんじょ」 (CẬN SỞ - Hàng xóm, khu vực lân cận)."
    },
    {
        "id": 13,
        "category": "Ngữ pháp",
        "q": "父は 毎日 スポーツジムへ 行って、とても [____] です。",
        "options": ["けんこう", "さっか", "しま", "こくさい"],
        "correct": 0,
        "explain": "Đi tập gym hàng ngày để rèn luyện nên cơ thể rất 'khỏe mạnh': 「健康 (けんこう) です」."
    },
    {
        "id": 14,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「屋」 trong từ 「本屋 (ほんや)」 có âm Hán Việt là gì?",
        "options": ["Ốc", "Phòng", "Điếm", "Thất"],
        "correct": 0,
        "explain": "屋 có âm Hán Việt là ỐC (căn nhà, tiệm). 本屋 là Bổn Ốc (tiệm sách)."
    },
    {
        "id": 15,
        "category": "Từ vựng",
        "q": "村上春樹さんは 世界中で とても 読まれている [____] です。",
        "options": ["さっか", "いみ", "とし", "むら"],
        "correct": 0,
        "explain": "Haruki Murakami là một nhà văn/tác giả nổi tiếng thế giới: 「作家 (さっか)」."
    }
]

# -------------------------------------------------------------
# LESSON 2 DATA
# -------------------------------------------------------------
L2_VOCAB = [
    {"jp": "ホームパーティー", "kana": "ホームパーティー", "kanji": "ホームパーティー", "romaji": "ho-mupa-ti-", "vi": "Tiệc gia đình, tiệc tại gia", "icon": "🎉"},
    {"jp": "スーツ", "kana": "スーツ", "kanji": "スーツ", "romaji": "su-tsu", "vi": "Bộ vest, âu phục", "icon": "🤵"},
    {"jp": "サリー", "kana": "サリー", "kanji": "サリー", "romaji": "sari-", "vi": "Sari (trang phục truyền thống Ấn Độ)", "icon": "🥻"},
    {"jp": "セーター", "kana": "セーター", "kanji": "セーター", "romaji": "se-ta-", "vi": "Áo len", "icon": "🧶"},
    {"jp": "ネクタイをします", "kana": "ネクタイを します", "kanji": "ネクタイをします", "romaji": "nekutai o shimasu", "vi": "Thắt cà vạt", "icon": "👔"},
    {"jp": "スーツを着ます", "kana": "スーツを きます", "kanji": "スーツを着ます", "romaji": "su-tsu o kimasu", "vi": "Mặc vest (áo, thân trên)", "icon": "🧥"},
    {"jp": "めがねをかけます", "kana": "めがねを かけます", "kanji": "めがねをかけます", "romaji": "megane o kakemasu", "vi": "Đeo kính", "icon": "👓"},
    {"jp": "ぼうしをかぶります", "kana": "ぼうしを かぶります", "kanji": "ぼうしをかぶります", "romaji": "boushi o kaburimasu", "vi": "Đội mũ", "icon": "🧢"},
    {"jp": "スカートをはきます", "kana": "スカートを はきます", "kanji": "スカートをはきます", "romaji": "suka-to o hakimasu", "vi": "Mặc váy (phần dưới)", "icon": "👗"},
    {"jp": "くつをはきます", "kana": "くつを はきます", "kanji": "くつをはきます", "romaji": "kutsu o hakimasu", "vi": "Đi giày", "icon": "👟"},
    {"jp": "座ります", "kana": "すわります", "kanji": "座ります", "romaji": "suwarimasu", "vi": "Ngồi", "icon": "🪑"},
    {"jp": "立ちます", "kana": "たちます", "kanji": "立ちます", "romaji": "tachimasu", "vi": "Đứng", "icon": "🧍"},
    {"jp": "笑います", "kana": "わらいます", "kanji": "笑います", "romaji": "waraimasu", "vi": "Cười", "icon": "😄"},
    {"jp": "泣きます", "kana": "なきます", "kanji": "泣きます", "romaji": "nakimasu", "vi": "Khóc", "icon": "😢"},
    {"jp": "厳しい", "kana": "きびしい", "kanji": "厳しい", "romaji": "kibishii", "vi": "Nghiêm khắc, khắt khe", "icon": "🧐"},
    {"jp": "ご主人", "kana": "ごしゅじん", "kanji": "ご主人", "romaji": "goshujin", "vi": "Chồng (người khác)", "icon": "👨"},
    {"jp": "頭がいい", "kana": "あたまが いい", "kanji": "頭がいい", "romaji": "atama ga ii", "vi": "Thông minh, sáng dạ", "icon": "🧠"}
]

L2_VERBS = [
    {"masu": "着ます", "vi": "Mặc (áo, vest)", "te": "着て", "form1": "着ています", "form2": "着た", "form3": "着る"},
    {"masu": "履きます", "vi": "Mặc váy/đi giày", "te": "履いて", "form1": "履いています", "form2": "履いた", "form3": "履く"},
    {"masu": "被ります", "vi": "Đội mũ", "te": "被って", "form1": "被っています", "form2": "被った", "form3": "被る"},
    {"masu": "掛けます", "vi": "Đeo kính", "te": "掛けて", "form1": "掛けています", "form2": "掛けた", "form3": "掛ける"},
    {"masu": "します", "vi": "Thắt cà vạt / đeo phụ kiện", "te": "して", "form1": "しています", "form2": "した", "form3": "する"},
    {"masu": "座ります", "vi": "Ngồi", "te": "座って", "form1": "座っています", "form2": "座った", "form3": "座る"}
]

L2_KANJI_LIST = [
    {"stt": 1, "word": "兄", "kana": "あに", "hv": "HUYNH", "mean": "Anh trai mình"},
    {"stt": 2, "word": "お兄さん", "kana": "おにいさん", "hv": "HUYNH", "mean": "Anh trai (người khác)"},
    {"stt": 3, "word": "姉", "kana": "あね", "hv": "TỶ", "mean": "Chị gái mình"},
    {"stt": 4, "word": "お姉さん", "kana": "おねえさん", "hv": "TỶ", "mean": "Chị gái (người khác)"},
    {"stt": 5, "word": "弟", "kana": "おとうと", "hv": "ĐỆ", "mean": "Em trai"},
    {"stt": 6, "word": "兄弟", "kana": "きょうだい", "hv": "HUYNH ĐỆ", "mean": "Anh em"},
    {"stt": 7, "word": "妹", "kana": "いもうと", "hv": "MUỘI", "mean": "Em gái"},
    {"stt": 8, "word": "姉妹", "kana": "しまい", "hv": "TỶ MUỘI", "mean": "Chị em"},
    {"stt": 9, "word": "家族", "kana": "かぞく", "hv": "GIA TỘC", "mean": "Gia đình"},
    {"stt": 10, "word": "水族館", "kana": "すいぞくかん", "hv": "THỦY TỘC QUÁN", "mean": "Thủy cung"},
    {"stt": 11, "word": "長い", "kana": "ながい", "hv": "TRƯỜNG", "mean": "Dài"},
    {"stt": 12, "word": "成長", "kana": "せいちょう", "hv": "THÀNH TRƯỜNG", "mean": "Trưởng thành, phát triển"},
    {"stt": 13, "word": "短い", "kana": "みじかい", "hv": "ĐOẢN", "mean": "Ngắn"},
    {"stt": 14, "word": "低い", "kana": "ひくい", "hv": "ĐÊ", "mean": "Thấp"},
    {"stt": 15, "word": "歌", "kana": "うた", "hv": "CA", "mean": "Bài hát"},
    {"stt": 16, "word": "歌手", "kana": "かしゅ", "hv": "CA THỦ", "mean": "Ca sĩ"}
]

L2_KANJI_CARDS = [
    {"char": "兄", "hv": "Huynh", "strokes": 5, "kun": "あに", "on": "きょう、けい", "ex": "兄 (あに - anh trai mình), お兄さん (おにいさん - anh trai), 兄弟 (きょうだい - anh em)", "mnemonic": "Đứa trẻ có cái miệng to (口) biết nói điều hay và đôi chân (儿) vững chãi là người Anh."},
    {"char": "姉", "hv": "Tỷ", "strokes": 8, "kun": "あね", "on": "し", "ex": "姉 (あね - chị gái mình), お姉さん (おねえさん - chị gái), 姉妹 (しまい - chị em gái)", "mnemonic": "Người phụ nữ (女) quản lý việc chợ búa thành thị (市) là Chị gái."},
    {"char": "弟", "hv": "Đệ", "strokes": 7, "kun": "おとうと", "on": "だい、で", "ex": "弟 (おとうと - em trai), 兄弟 (きょうだい - anh em), 弟子 (でし - đệ tử)", "mnemonic": "Dây quấn quanh cây cung (弓) của người Em trai."},
    {"char": "妹", "hv": "Muội", "strokes": 8, "kun": "いもうと", "on": "まい", "ex": "妹 (いもうと - em gái), 姉妹 (しまい - chị em gái)", "mnemonic": "Người con gái (女) còn non nớt chưa trưởng thành (未 - vị) là Em gái."},
    {"char": "家", "hv": "Gia", "strokes": 10, "kun": "いえ、や", "on": "か、け", "ex": "家族 (かぞく - gia đình), 家 (いえ - ngôi nhà), 作家 (さっか - tác giả/nhà văn)", "mnemonic": "Dưới mái nhà (宀) nuôi con lợn (豕) là Gia đình, mái ấm sum vầy."},
    {"char": "族", "hv": "Tộc", "strokes": 11, "kun": "ー", "on": "ぞく", "ex": "家族 (かぞく - gia đình), 水族館 (すいぞくかん - thủy cung), 民族 (みんぞく - dân tộc)", "mnemonic": "Dưới lá cờ (方) tập hợp những người cầm mũi tên (矢) cùng chung một Gia tộc."},
    {"char": "水", "hv": "Thủy", "strokes": 4, "kun": "みず", "on": "すい", "ex": "水族館 (すいぞくかん - thủy cung), 水 (みず - nước), 水泳 (すいえい - bơi lội)", "mnemonic": "Dòng nước chảy róc rách uốn lượn qua các khe đá (Thủy)."},
    {"char": "館", "hv": "Quán", "strokes": 16, "kun": "ー", "on": "かん", "ex": "水族館 (すいぞくかん - thủy cung), 図書館 (としょかん - thư viện), 映画館 (えいがかん - rạp phim)", "mnemonic": "Nơi người ta ăn uống (飠 - thực) và nghỉ ngơi tại quan phủ (官) là Hội quán."},
    {"char": "長", "hv": "Trường", "strokes": 8, "kun": "なが・い", "on": "ちょう", "ex": "長い (ながい - dài), 成長 (せいちょう - trưởng thành), 社長 (しゃちょう - giám đốc)", "mnemonic": "Hình ảnh mái tóc dài phủ xuống và chiếc gậy chống của người lớn tuổi (Trường)."},
    {"char": "成", "hv": "Thành", "strokes": 6, "kun": "な・る", "on": "せい、じょう", "ex": "成長 (せいちょう - trưởng thành), 成功 (せいこう - thành công), 完成 (かんせい - hoàn thành)", "mnemonic": "Dùng vũ khí (qua) rèn giũa để Hoàn thành việc lớn (Thành)."},
    {"char": "短", "hv": "Đoản", "strokes": 12, "kun": "みじか・い", "on": "たん", "ex": "短い (みじかい - ngắn), 短所 (たんしょ - khuyết điểm), 短期 (たんき - ngắn hạn)", "mnemonic": "Mũi tên (矢) đem so với chiếc đĩa hạt đậu (豆) thấy ngắn ngủi (Đoản)."},
    {"char": "低", "hv": "Đê", "strokes": 7, "kun": "ひく・い", "on": "てい", "ex": "低い (ひくい - thấp), 最低 (さいてい - thấp nhất / tệ nhất), 低下 (ていか - sụt giảm)", "mnemonic": "Người (亻) cúi đầu xuống đến tận đáy (氐) là người Thấp bé hoặc khiêm nhường."},
    {"char": "歌", "hv": "Ca", "strokes": 14, "kun": "うた、うた・う", "on": "か", "ex": "歌 (うた - bài hát), 歌手 (かしゅ - ca sĩ), 国歌 (こっか - quốc ca)", "mnemonic": "Người ta mở miệng liên hồi (哥) thở ra hơi (欠) để cất tiếng Hát (Ca)."},
    {"char": "手", "hv": "Thủ", "strokes": 4, "kun": "て", "on": "しゅ", "ex": "歌手 (かしゅ - ca sĩ), 手 (て - bàn tay), 上手 (じょうず - giỏi)", "mnemonic": "Hình vẽ bàn tay người xòe ra các ngón khéo léo (Thủ)."}
]

L2_QUIZ = [
    {
        "id": 1,
        "category": "Ngữ pháp",
        "q": "あそこで めがねを [____] いる 人は 田中さんです。",
        "options": ["かけて", "きて", "はいて", "かぶって"],
        "correct": 0,
        "explain": "Động từ đi với kính mắt 「めがね」 là 「掛けます (かけます)」. Khi bổ nghĩa miêu tả trạng thái: 「めがねをかけている人」 (người đang đeo kính)."
    },
    {
        "id": 2,
        "category": "Ngữ pháp",
        "q": "山田さんは きょう 黒いスーツを [____] います。",
        "options": ["着て", "履いて", "掛けて", "被って"],
        "correct": 0,
        "explain": "Bộ vest 「スーツ」 là trang phục mặc ở phần thân trên, dùng động từ 「着ます (きます)」 ➔ 「着ています」."
    },
    {
        "id": 3,
        "category": "Ngữ pháp",
        "q": "あのかわいい ぼうしを [____] いる 子どもは だれですか。",
        "options": ["かぶって", "はいて", "きて", "して"],
        "correct": 0,
        "explain": "Mũ 「ぼうし」 là vật đội lên đầu, dùng động từ 「被ります (かぶります)」 ➔ 「被っている (かぶっている)」."
    },
    {
        "id": 4,
        "category": "Từ vựng",
        "q": "きょうは 寒いですね。あたたかい [____] を 着ましょう。",
        "options": ["セーター", "ネクタイ", "くつ", "めがね"],
        "correct": 0,
        "explain": "Trời lạnh thì mặc áo len ấm áp: 「セーター」."
    },
    {
        "id": 5,
        "category": "Ngữ pháp",
        "q": "新しい くつを [____] 出かけました。",
        "options": ["はいて", "きて", "かぶって", "かけて"],
        "correct": 0,
        "explain": "Giày dép 「くつ」 mặc/xỏ từ thắt lưng trở xuống, dùng động từ 「履きます (はきます)」."
    },
    {
        "id": 6,
        "category": "Ngữ pháp",
        "q": "会社へ 行くとき、いつも ネクタイを [____]。",
        "options": ["します", "きます", "はきます", "かぶります"],
        "correct": 0,
        "explain": "Cà vạt 「ネクタイ」 thuộc nhóm phụ kiện thắt/đeo, động từ chuẩn là 「します」 (hoặc 締めます)."
    },
    {
        "id": 7,
        "category": "Hội thoại",
        "q": "「鈴木さんは どの人ですか。」 ―― 「窓のそばに [____] 人です。」",
        "options": ["立っている", "着ている", "履いている", "歌っている"],
        "correct": 0,
        "explain": "Chỉ vị trí tư thế: 「窓のそばに立っている人」 (Là người đang đứng cạnh cửa sổ)."
    },
    {
        "id": 8,
        "category": "Từ vựng",
        "q": "あの 先生は いつも 真面目で、とても [____] です。",
        "options": ["きびしい", "ひくい", "みじかい", "ながい"],
        "correct": 0,
        "explain": "Thầy giáo luôn nghiêm túc và 'nghiêm khắc': 「厳しい (きびしい)」."
    },
    {
        "id": 9,
        "category": "Từ vựng",
        "q": "Từ 「ご主人」 dùng để nói về ai trong các lựa chọn sau?",
        "options": ["Chồng của người khác", "Vợ của người khác", "Em gái của mình", "Anh trai của mình"],
        "correct": 0,
        "explain": "ご主人 (ごしゅじん) là cách gọi chồng của người khác. Khi nói về chồng mình thường dùng 夫 (おっと)."
    },
    {
        "id": 10,
        "category": "Từ vựng",
        "q": "赤ちゃんが えがおで [____] います。かわいいですね。",
        "options": ["笑って", "泣いて", "怒って", "歌って"],
        "correct": 0,
        "explain": "Khuôn mặt cười tươi (えがお) thì hành động tương ứng là cười: 「笑っています (わらっています)」."
    },
    {
        "id": 11,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「兄弟」 có cách đọc chuẩn là gì?",
        "options": ["きょうだい", "あにてい", "けいてい", "おとうとあに"],
        "correct": 0,
        "explain": "兄弟 đọc là 「きょうだい」 (HUYNH ĐỆ - Anh em)."
    },
    {
        "id": 12,
        "category": "Chữ Hán",
        "q": "Từ 「水族館」 có nghĩa là gì?",
        "options": ["Thủy cung (viện hải dương)", "Hồ bơi", "Công viên nước", "Bến thuyền"],
        "correct": 0,
        "explain": "水族館 (すいぞくかん) là viện bảo tàng/thủy cung trưng bày sinh vật dưới nước."
    },
    {
        "id": 13,
        "category": "Chữ Hán",
        "q": "Từ trái nghĩa với 「長い (ながい)」 là từ nào?",
        "options": ["短い (みじかい)", "低い (ひくい)", "高い (たかい)", "近い (ちかい)"],
        "correct": 0,
        "explain": "長い (dài) đối nghĩa với 短い (ngắn)."
    },
    {
        "id": 14,
        "category": "Chữ Hán",
        "q": "Chữ Hán 「歌手」 gồm hai chữ nào ghép lại?",
        "options": ["CA + THỦ", "HOA + THỦ", "CA + NHÂN", "HOA + NHÂN"],
        "correct": 0,
        "explain": "歌手 gồm chữ 歌 (CA - bài hát) và 手 (THỦ - bàn tay / người chuyên làm việc gì) ➔ ca sĩ."
    },
    {
        "id": 15,
        "category": "Ngữ pháp",
        "q": "あの ソファーに [____] いる 人は どなたですか。",
        "options": ["すわって", "たって", "はいて", "かぶって"],
        "correct": 0,
        "explain": "Đi với ghế sofa 「ソファーに」 là hành động ngồi: 「座っている (すわっている)」."
    }
]

def make_svg(label, icon, color1="#4f46e5", color2="#7c3aed"):
    gradient_id = "g_" + hashlib.sha256(label.encode("utf-8")).hexdigest()[:16]
    return f'''<svg viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="{gradient_id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{color1}"/>
      <stop offset="100%" stop-color="{color2}"/>
    </linearGradient>
  </defs>
  <rect width="240" height="120" rx="14" fill="url(#{gradient_id})"/>
  <circle cx="120" cy="50" r="30" fill="rgba(255,255,255,0.2)"/>
  <text x="120" y="60" text-anchor="middle" font-size="32">{icon}</text>
</svg>'''

def build_js_file(dest_path, vocab_list, verb_list, quiz_list, badge_name):
    # Stable, balanced answer positions keep saved attempts reproducible.
    positions = [i % 4 for i in range(len(quiz_list))]
    random.Random(badge_name).shuffle(positions)
    processed_quiz = []
    for q, position in zip(quiz_list, positions):
        answer = q["options"][q["correct"]]
        options = [option for i, option in enumerate(q["options"]) if i != q["correct"]]
        options.insert(position, answer)
        processed_quiz.append({**q, "options": options, "correct": position})
    # Prepare vocab objects
    processed_vocab = []
    for idx, v in enumerate(vocab_list, 1):
        processed_vocab.append({
            "id": idx,
            "cat": "vocab",
            "catName": "Từ Vựng",
            "badge": badge_name,
            "jp": v["jp"],
            "kana": v["kana"],
            "kanji": v["kanji"],
            "romaji": v["romaji"],
            "vi": v["vi"],
            "svg": make_svg(v["vi"], v.get("icon", "📖"))
        })

    js_content = f'''/* Marugoto A2-2 {badge_name} - Extracted Data & Logic */
const VOCAB_DATA = {json.dumps(processed_vocab, ensure_ascii=False, indent=2)};

const VERB_DATA = {json.dumps(verb_list, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(processed_quiz, ensure_ascii=False, indent=2)};

function escapeLessonText(value) {{
    return String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}}

// Audio TTS handled globally via assets/js/audio-engine.js

// Render Verb Lab
function initVerbLab() {{
    const row = document.getElementById('verbSelectorRow');
    if (!row || !VERB_DATA.length) return;
    row.innerHTML = '';
    VERB_DATA.forEach((v, idx) => {{
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `btn-verb-chip ${{idx === 0 ? 'active' : ''}}`;
        btn.textContent = `${{v.masu}} (${{v.vi}})`;
        btn.onclick = () => selectVerb(idx);
        row.appendChild(btn);
    }});
    selectVerb(0);
}}

function selectVerb(idx) {{
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
    if (elMasu) elMasu.textContent = v.masu;
    if (elVi) elVi.textContent = v.vi;
    if (elTe) elTe.textContent = v.te;
    if (elForm1) elForm1.textContent = v.form1;
    if (elForm2) elForm2.textContent = v.form2;
    if (elForm3) elForm3.textContent = v.form3;
}}

// Render Flashcards
function initFlashcards() {{
    const grid = document.getElementById('flashcardGrid');
    if (!grid) return;
    grid.innerHTML = '';
    VOCAB_DATA.forEach(v => {{
        const card = document.createElement('button');
        card.type = 'button';
        card.className = 'fc-item';
        card.setAttribute('aria-label', `Nghe ${{v.jp}}`);
        card.onclick = () => {{
            if (typeof speakText === 'function') speakText(v.kana || v.jp);
        }};
        card.innerHTML = `
            <span class="fc-svg-wrap" aria-hidden="true">${{v.svg}}</span>
            <span class="fc-content">
                <span class="fc-jp" lang="ja">${{escapeLessonText(v.jp)}}</span>
                <span class="fc-kana" lang="ja">${{escapeLessonText(v.kana)}}</span>
                <span class="fc-romaji">${{escapeLessonText(v.romaji)}}</span>
                <span class="fc-vi">${{escapeLessonText(v.vi)}}</span>
                <span class="fc-listen">🔊 Nghe phát âm</span>
            </span>
        `;
        grid.appendChild(card);
    }});
}}

// Render Quiz
function initQuiz() {{
    const c = document.getElementById('quizContainer');
    if (!c) return;
    c.innerHTML = '';
    QUIZ_DATA.forEach((q, qIdx) => {{
        const qBox = document.createElement('div');
        qBox.className = 'quiz-card';
        const optsHtml = q.options.map((opt, oIdx) => `
            <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${{qIdx}}, ${{oIdx}}, 'a22-reviewed-v2')">${{escapeLessonText(opt)}}</button>
        `).join('');
        qBox.innerHTML = `
            <div class="quiz-q"><b>Câu ${{qIdx + 1}}:</b> ${{escapeLessonText(q.q)}}</div>
            <div class="quiz-opts">${{optsHtml}}</div>
            <div class="quiz-explain" id="explain-${{qIdx}}">💡 ${{escapeLessonText(q.explain)}}</div>
        `;
        c.appendChild(qBox);
    }});
}}

function checkQuizAnswer(btn, qIdx, oIdx, revision) {{
    if (revision !== 'a22-reviewed-v2' || btn.disabled) return;
    const q = QUIZ_DATA[qIdx];
    const parent = btn.parentElement;
    const allBtns = parent.querySelectorAll('.quiz-opt');
    allBtns.forEach(b => b.disabled = true);
    if (oIdx === q.correct) {{
        btn.classList.add('correct');
    }} else {{
        btn.classList.add('wrong');
        allBtns[q.correct].classList.add('correct');
    }}
    const exp = document.getElementById(`explain-${{qIdx}}`);
    if (exp) exp.style.display = 'block';
}}

function initLessonInteractive() {{
    initVerbLab();
    initFlashcards();
    initQuiz();
}}

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initLessonInteractive);
}} else {{
    initLessonInteractive();
}}

if (typeof VOCAB_DATA !== "undefined") window.VOCAB_DATA = VOCAB_DATA;
'''
    dest_path.write_text(js_content, encoding="utf-8")
    print(f"Created {dest_path}")

def build_lesson_html(
    dest_path,
    lesson_num,
    lesson_title,
    quote,
    subtitle,
    vocab_count,
    grammar_count,
    verb_count,
    kanji_count,
    grammar_blocks,
    kanji_cards,
    js_filename
):
    grammar_html = "\n".join(grammar_blocks)
    
    kanji_cards_html = []
    for k in kanji_cards:
        kanji_cards_html.append(f'''        <div class="kanji-detail-card">
            <div class="kanji-big-char">{k["char"]}</div>
            <div class="kanji-info">
                <div class="kanji-hv-title">{k["hv"]} <span class="kanji-strokes-badge">{k["strokes"]} nét</span></div>
                <div class="kanji-readings">
                    <strong>Kun:</strong> {k["kun"]}<br>
                    <strong>On:</strong> {k["on"]}<br>
                    <strong>Từ ví dụ:</strong> {k["ex"]}
                </div>
                <div class="kanji-mnemonic">💡 Mẹo nhớ: {k["mnemonic"]}</div>
            </div>
        </div>''')
    kanji_html = "\n".join(kanji_cards_html)

    html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>Cẩm Nang & Luyện Tập Toàn Diện Bài {lesson_num} (A2-2) | {quote}</title>
    <meta name="description" content="Chinh phục toàn diện Marugoto A2-2 Bài {lesson_num}: {quote}. Đầy đủ ngữ pháp, 3D Flashcard từ vựng, máy biến thể và Mini Test 15 câu có giải thích chi tiết.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <!-- Animate UI Core -->
    <link rel="stylesheet" href="../assets/css/animate-ui.css">
    <script src="../assets/js/animate-ui.js" defer></script>
    <script src="../assets/js/audio-engine.js?v=2"></script>
    <link rel="stylesheet" href="../assets/css/lesson-a2-core.css?v=1">
    <link rel="stylesheet" href="../assets/css/site-theme.css?v=7">
    <link rel="stylesheet" href="../assets/css/lesson-a2-2.css?v=1">
</head>
<body class="lesson-a2-2">

<div class="main-container">
    <!-- Global Hub Navigation Placeholder -->
    <div id="navbar-placeholder"></div>

    <!-- Sticky Section Sub-Nav -->
    <div class="section-nav">
        <a href="#sec-grammar1" class="sec-link">① Ngữ Pháp 1</a>
        <a href="#sec-grammar2" class="sec-link">② Ngữ Pháp 2</a>
        <a href="#sec-grammar3" class="sec-link">③ Ngữ Pháp 3</a>
        <a href="#sec-verb-lab" class="sec-link">🔬 Biến Thể Động Từ</a>
        <a href="#sec-vocab" class="sec-link">🎴 {vocab_count} Từ Vựng</a>
        <a href="#sec-typing-practice" class="sec-link">⌨️ Luyện Gõ Từ Vựng</a>
        <a href="#sec-kanji" class="sec-link">⛩️ {kanji_count} Chữ Hán</a>
        <a href="#sec-quiz" class="sec-link">📝 Mini Test 15 Câu</a>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
        <div class="hero-badge">TOPIC 1: 新しい友だち • BÀI {lesson_num} (MARUGOTO A2-2)</div>
        <h1 class="hero-title">CHINH PHỤC TOÀN DIỆN BÀI {lesson_num} (A2-2)</h1>
        <div class="hero-jp-quote">
            <span>「{quote}」</span>
            <button type="button" class="btn-speak" style="background:rgba(255,255,255,0.2); border-color:#818cf8; color:#fff;" onclick="speakText('{quote}')">🔊</button>
        </div>
        <p class="hero-subtitle">
            {subtitle}
        </p>
        <div class="hero-stats-row">
            <div class="stat-card">
                <div class="stat-number">{vocab_count}</div>
                <div class="stat-label">Từ vựng Flashcard</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{grammar_count}</div>
                <div class="stat-label">Chuyên đề ngữ pháp</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{verb_count}</div>
                <div class="stat-label">Động từ mẫu Lab</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{kanji_count}</div>
                <div class="stat-label">Chữ Hán Kanji</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">15</div>
                <div class="stat-label">Câu Mini Test</div>
            </div>
        </div>
    </div>

    <!-- Grammar Sections -->
{grammar_html}

    <!-- Verb Lab Section -->
    <section class="content-section" id="sec-verb-lab">
        <div class="section-header">
            <h2 class="section-title"><span>🔬</span> Phòng Thí Nghiệm Biến Thể Động Từ</h2>
            <span class="section-tag">Interactive Verb Morph</span>
        </div>
        <p style="margin-bottom: 16px; color: #475569;">Chọn động từ bên dưới để quan sát tức thì cách biến đổi sang các thể giao tiếp quan trọng:</p>
        
        <div class="verb-selector-row" id="verbSelectorRow"></div>

        <div class="morph-display-box">
            <div class="morph-grid">
                <div class="morph-cell">
                    <span class="morph-label">Thể Lịch Sự (~masu)</span>
                    <span class="morph-val" id="morphMasu">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">Ý Nghĩa Tiếng Việt</span>
                    <span class="morph-val" id="morphVi" style="color: #6366f1;">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">Thể TE (~te)</span>
                    <span class="morph-val" id="morphTe">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">Dạng ～ています (hành động / trạng thái)</span>
                    <span class="morph-val" id="morphTeIki">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">Thể Quá Khứ Ngắn (~ta)</span>
                    <span class="morph-val" id="morphTeKi">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">Thể Từ Điển (~ru / jisho)</span>
                    <span class="morph-val" id="morphMashou">---</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Vocab 3D Flashcard Section -->
    <section class="content-section" id="sec-vocab">
        <div class="section-header">
            <h2 class="section-title"><span>🎴</span> Hệ Thống Flashcard Từ Vựng Trọng Tâm ({vocab_count} Từ)</h2>
            <span class="section-tag">Audio + Visual</span>
        </div>
        <p style="margin-bottom: 16px; color: #475569;">Bấm thẻ hoặc nhấn Enter để nghe tiếng Nhật. Giọng đọc phụ thuộc dịch vụ và thiết bị.</p>
        <div class="flashcard-grid" id="flashcardGrid"></div>
    </section>

    <!-- Typing Practice Section -->
    <section class="content-section" id="sec-typing-practice"></section>

    <!-- Kanji Section -->
    <section class="content-section" id="sec-kanji">
        <div class="section-header">
            <h2 class="section-title"><span>⛩️</span> Trọn Bộ Chữ Hán Cốt Lõi Bài {lesson_num} ({kanji_count} Chữ)</h2>
            <span class="section-tag">Kanji N4-N3</span>
        </div>
        <div class="kanji-grid">
{kanji_html}
        </div>
    </section>

    <!-- Mini Test -->
    <section class="content-section" id="sec-quiz">
        <div class="section-header">
            <h2 class="section-title"><span>📝</span> Mini Test Phản Xạ Bài {lesson_num} (15 Câu)</h2>
            <span class="section-tag">Instant Feedback</span>
        </div>
        <p style="margin-bottom: 16px; color: #475569;">Chọn đáp án đúng nhất để kiểm tra khả năng tiếp thu bài học:</p>
        <div id="quizContainer"></div>
    </section>
</div>

<!-- Scripts -->
<script src="../assets/js/lessons/{js_filename}?v=2"></script>
<script src="../assets/js/nav-dropdown.js"></script>
<script src="../assets/nav.js?v=7" defer></script>
<script src="../assets/js/jp-typing-grader.js?v=1" defer></script>
<script src="../assets/js/typing-practice.js" defer></script>
</body>
</html>
'''
    dest_path.write_text(html_content, encoding="utf-8")
    print(f"Created {dest_path}")


# -------------------------------------------------------------
# GRAMMAR SECTIONS BUILDER
# -------------------------------------------------------------
L1_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>💡</span> 1. Giải Thích Tên & Từ Ngữ: ～というのは、～という意味です</h2>
            <span class="section-tag">Định nghĩa & Ý nghĩa</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Mẫu câu dùng để giới thiệu ý nghĩa, nguồn gốc của tên người, địa danh hoặc một từ ngữ tiếng Nhật/tiếng nước ngoài.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #4f46e5;">
                <div class="rule-formula" style="color: #3730a3;">[Từ / Tên] というのは、[Giải thích / Nội dung] という 意味 (いみ) です。</div>
                <div class="rule-meaning">
                    "[Từ / Tên] có nghĩa là..." Trợ từ 「というのは」 nêu lên chủ đề cần định nghĩa, và 「という意味です」 đóng khung phần giải thích ý nghĩa.
                </div>
            </div>
            <table class="comparison-table">
                <thead>
                    <tr>
                        <th>Tên / Từ ngữ</th>
                        <th>Mẫu câu hoàn chỉnh</th>
                        <th>Ý nghĩa tiếng Việt</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>ハノイ</strong></td>
                        <td>「ハノイ」というのは、「川の内側」という意味です。</td>
                        <td>"Hà Nội" có nghĩa là "bên trong những dòng sông".</td>
                    </tr>
                    <tr>
                        <td><strong>さくら</strong></td>
                        <td>「さくら」というのは、日本の花の名前という意味です。</td>
                        <td>"Sakura" có nghĩa là tên một loài hoa của Nhật Bản.</td>
                    </tr>
                    <tr>
                        <td><strong>ひみつ</strong></td>
                        <td>「ひみつ」というのは、だれにも言わないことという意味です。</td>
                        <td>"Bí mật" có nghĩa là điều không được nói cho bất kỳ ai.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>🏡</span> 2. Nơi Sinh Ra & Quê Quán: ～で 生まれました / 育ちました</h2>
            <span class="section-tag">Nơi sinh & Lớn lên</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Khi nói về nơi chốn mình sinh ra hoặc lớn lên, hành động sinh ra/lớn lên là một sự kiện diễn ra tại một địa điểm nên dùng trợ từ <strong>「で」</strong>.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">[Địa điểm] で 生まれました (Sinh ra ở...)<br>[Địa điểm] で 育ちました (Lớn lên ở...)</div>
                <div class="rule-meaning">
                    ⚠️ <strong>Lưu ý phân biệt trợ từ:</strong><br>
                    • <strong>Địa điểm + で 生まれました:</strong> Sinh ra tại đâu (dùng で).<br>
                    • <strong>Địa điểm + に 住んでいます:</strong> Hiện đang sinh sống lâu dài tại đâu (dùng に).<br>
                    • <strong>Địa điểm + の 近くの [村 / 町 / 島]:</strong> Ngôi làng / thị trấn / hòn đảo ở gần...
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">わたしは ベトナムの ダナンで 生まれました。</div>
                        <div class="ex-vi">Tôi được sinh ra ở Đà Nẵng, Việt Nam.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('わたしは ベトナムの ダナンで 生まれました')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">ハノイの 近くの 村で 育ちました。</div>
                        <div class="ex-vi">Tôi lớn lên ở một ngôi làng gần Hà Nội.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('ハノイの 近くの 村で 育ちました')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar3">
        <div class="section-header">
            <h2 class="section-title"><span>✨</span> 3. Bày Tỏ Hứng Thú & Miêu Tả Tính Cách: ～に 興味があります</h2>
            <span class="section-tag">Hứng thú & Tính cách</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để chia sẻ sở thích cá nhân, các lĩnh vực bản thân quan tâm và cách nối các tính từ miêu tả tính cách con người.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #d97706;">
                <div class="rule-formula" style="color: #92400e;">[Danh từ] に 興味 (きょうみ) が あります (Có hứng thú với...)<br>Tính từ い ➔ ～くて、... / Tính từ な ➔ ～で、...</div>
                <div class="rule-meaning">
                    • <strong>興味がある:</strong> Đối tượng mà bạn hứng thú luôn đi với trợ từ 「に」.<br>
                    • <strong>Nối tính từ tính cách:</strong><br>
                    &nbsp;&nbsp;+ 優しい (Hiền lành) ➔ 優しくて、明るいです (Vừa hiền lành vừa vui vẻ tươi sáng).<br>
                    &nbsp;&nbsp;+ 真面目な (Chăm chỉ, nghiêm túc) ➔ 真面目で、親切です (Nghiêm túc và rất tốt bụng).
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">わたしは 日本の 歴史や 文化に 興味が あります。</div>
                        <div class="ex-vi">Tôi có hứng thú với lịch sử và văn hóa Nhật Bản.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('わたしは 日本の 歴史や 文化に 興味が あります')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">兄は とても 真面目で、健康な 人です。</div>
                        <div class="ex-vi">Anh trai tôi là người rất nghiêm túc và khỏe mạnh.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('兄は とても 真面目で、健康な 人です')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]


L2_GRAMMAR_BLOCKS = [
    '''    <section class="content-section" id="sec-grammar1">
        <div class="section-header">
            <h2 class="section-title"><span>👔</span> 1. Đại Cẩm Nang 5 Động Từ Mang Mặc Trang Phục Tiếng Nhật</h2>
            <span class="section-tag">Động từ mang mặc</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Trong tiếng Việt, ta có thể dùng từ "mặc" cho mọi trang phục, nhưng tiếng Nhật phân biệt rất chặt chẽ theo vị trí trên cơ thể:
        </p>
        <div class="grammar-card">
            <table class="comparison-table">
                <thead>
                    <tr>
                        <th>Động từ</th>
                        <th>Vị trí cơ thể</th>
                        <th>Trang phục tiêu biểu</th>
                        <th>Ví dụ</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>着る (きる)</strong></td>
                        <td>Từ vai xuống thân trên</td>
                        <td>スーツ (vest), セーター (áo len), シャツ (áo sơ mi), 着物</td>
                        <td>スーツを着ます</td>
                    </tr>
                    <tr>
                        <td><strong>履く (はく)</strong></td>
                        <td>Từ thắt lưng trở xuống chân</td>
                        <td>スカート (váy), ズボン (quần), くつ (giày), くつした (tất)</td>
                        <td>くつを履きます</td>
                    </tr>
                    <tr>
                        <td><strong>被る (かぶる)</strong></td>
                        <td>Trùm lên đầu</td>
                        <td>ぼうし (mũ), ヘルメット (mũ bảo hiểm)</td>
                        <td>ぼうしを被ります</td>
                    </tr>
                    <tr>
                        <td><strong>掛ける (かける)</strong></td>
                        <td>Gài lên mắt / mặt</td>
                        <td>めがね (kính), サングラス (kính râm)</td>
                        <td>めがねを掛けます</td>
                    </tr>
                    <tr>
                        <td><strong>する</strong></td>
                        <td>Phụ kiện, trang sức</td>
                        <td>ネクタイ (cà vạt), 時計 (đồng hồ), 指輪 (nhẫn), マフラー</td>
                        <td>ネクタイをします</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar2">
        <div class="section-header">
            <h2 class="section-title"><span>👓</span> 2. Miêu Tả Trạng Thái Đang Mang Mặc: ～を [V-ている]</h2>
            <span class="section-tag">Trạng thái hiện tại</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Khi miêu tả một người đang mặc đồ gì trên người ở thời điểm hiện tại, tiếng Nhật <strong>bắt buộc phải chia sang thể ～ています</strong> (chỉ kết quả của hành động mang mặc vẫn đang tồn tại).
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #059669;">
                <div class="rule-formula" style="color: #065f46;">[Người] は [Trang phục] を [着て / 履いて / かぶって / かけて / して] います。</div>
                <div class="rule-meaning">
                    • <strong>Không dùng thể từ điển/thể -masu</strong> để tả đồ đang mặc trên người vì nó chỉ thói quen hoặc hành động sắp làm.<br>
                    • <strong>Ví dụ:</strong><br>
                    &nbsp;&nbsp;+ 田中さんは 黒いスーツを <strong>着ています</strong> (Anh Tanaka đang mặc bộ vest đen).<br>
                    &nbsp;&nbsp;+ あの人は めがねを <strong>かけています</strong> (Người kia đang đeo kính).
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">アンナさんは 赤いサリーを 着ています。</div>
                        <div class="ex-vi">Chị Anna đang mặc bộ trang phục Sari màu đỏ.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('アンナさんは 赤いサリーを 着ています')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">父は 白いぼうしを かぶっています。</div>
                        <div class="ex-vi">Bố tôi đang đội một chiếc mũ màu trắng.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('父は 白いぼうしを かぶっています')">🔊</button>
                </div>
            </div>
        </div>
    </section>''',

    '''    <section class="content-section" id="sec-grammar3">
        <div class="section-header">
            <h2 class="section-title"><span>👥</span> 3. Mệnh Đề Định Ngữ Miêu Tả Người: [Mệnh đề V-ている] + 人</h2>
            <span class="section-tag">Bổ ngữ cho danh từ</span>
        </div>
        <p style="margin-bottom: 16px; color: #334155;">
            Dùng để chỉ ra hoặc nhận diện một người nào đó trong bữa tiệc hay đám đông bằng hành động, tư thế hoặc trang phục họ đang mang.
        </p>
        <div class="grammar-card">
            <div class="rule-box" style="border-left-color: #d97706;">
                <div class="rule-formula" style="color: #92400e;">[Hành động / Trang phục + ている] + 人 (Người mà đang...)</div>
                <div class="rule-meaning">
                    • <strong>めがねを かけている 人:</strong> Người đang đeo kính.<br>
                    • <strong>ソファーに すわっている 人:</strong> Người đang ngồi ở ghế sofa.<br>
                    • <strong>あそこで 笑っている 人:</strong> Người đang cười ở đằng kia.<br>
                    • <strong>Cấu trúc nhận diện:</strong> 『[Mệnh đề] 人は [Tên] さんです』 hoặc 『[Tên] さんは [Mệnh đề] 人です』.
                </div>
            </div>
            <div class="example-list">
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">めがねを かけている 人は だれですか。</div>
                        <div class="ex-vi">Người đang đeo kính kia là ai thế?</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('めがねを かけている 人は だれですか')">🔊</button>
                </div>
                <div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">窓の そばに たっている 人は 山田さんです。</div>
                        <div class="ex-vi">Người đang đứng bên cạnh cửa sổ là anh Yamada.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText('窓の そばに たっている 人は 山田さんです')">🔊</button>
                </div>
            </div>
        </div>
    </section>'''
]


def main():
    # 1. Build JS files
    build_js_file(
        ROOT / "assets/js/lessons/lesson_a2_2_01.js",
        L1_VOCAB,
        L1_VERBS,
        L1_QUIZ,
        "Bài 1 (A2-2)"
    )

    build_js_file(
        ROOT / "assets/js/lessons/lesson_a2_2_02.js",
        L2_VOCAB,
        L2_VERBS,
        L2_QUIZ,
        "Bài 2 (A2-2)"
    )

    # 2. Build HTML files
    build_lesson_html(
        dest_path=ROOT / "lessons/Marugoto_A2_2_Lesson_1.html",
        lesson_num=1,
        lesson_title="いいなまえですね",
        quote="いいなまえですね",
        subtitle="Học cách giới thiệu bản thân chi tiết: giải thích ý nghĩa nguồn gốc tên mình (というのは、という意味です), quê quán nơi sinh ra (で 生まれました) và diễn đạt hứng thú, sở thích cá nhân.",
        vocab_count=len(L1_VOCAB),
        grammar_count=3,
        verb_count=len(L1_VERBS),
        kanji_count=len(L1_KANJI_CARDS),
        grammar_blocks=L1_GRAMMAR_BLOCKS,
        kanji_cards=L1_KANJI_CARDS,
        js_filename="lesson_a2_2_01.js"
    )

    build_lesson_html(
        dest_path=ROOT / "lessons/Marugoto_A2_2_Lesson_2.html",
        lesson_num=2,
        lesson_title="めがねをかけている人です",
        quote="めがねを かけて いる人です",
        subtitle="Làm chủ đại cẩm nang 5 động từ mang mặc trang phục (着る, 履く, 被る, 掛ける, する), mẫu câu miêu tả trạng thái (～を 着ています) và mệnh đề định ngữ nhận diện người trong đám đông (V-ている 人).",
        vocab_count=len(L2_VOCAB),
        grammar_count=3,
        verb_count=len(L2_VERBS),
        kanji_count=len(L2_KANJI_CARDS),
        grammar_blocks=L2_GRAMMAR_BLOCKS,
        kanji_cards=L2_KANJI_CARDS,
        js_filename="lesson_a2_2_02.js"
    )

    # 3. Build data/kanji_vocab_a2_2.json for 31 Kanji words
    all_kanji_vocab = {
        "lesson_1": L1_KANJI_LIST,
        "lesson_2": L2_KANJI_LIST
    }
    (ROOT / "data/kanji_vocab_a2_2.json").write_text(
        json.dumps(all_kanji_vocab, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print("Created data/kanji_vocab_a2_2.json with 31 Kanji compound words!")

if __name__ == "__main__":
    main()
