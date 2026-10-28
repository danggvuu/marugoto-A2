# -*- coding: utf-8 -*-
"""
update_kanji_a2.py
Updates kanji_a2.html with complete Kanji data for Lessons 12 to 18,
and updates UI navigation, presets, and lesson order.
"""

import json
import re

NEW_KANJI = [
    # LESSON 12 (7 chữ)
    {
        "char": "料", "hv": "Liệu", "lesson": "L12", "lessonName": "Bài 12", "strokes": 10,
        "meaning": "Nguyên liệu, tiền cước, tiền phí", "kun": "-", "on": "りょう",
        "examples": [
            {"word": "料理", "reading": "りょうり", "vi": "Món ăn, sự nấu nướng"},
            {"word": "料金", "reading": "りょうきん", "vi": "Tiền cước, chi phí, lệ phí"},
            {"word": "給料", "reading": "きゅうりょう", "vi": "Tiền lương"},
            {"word": "無料", "reading": "むりょう", "vi": "Miễn phí"}
        ],
        "formula": "米 (Mễ - gạo) ＋ 斗 (Đấu - cái đong lường)",
        "strokeGuide": "Bộ Mễ (米 - 6 nét) bên trái ➔ bộ Đấu (斗 - 4 nét: chấm, ngang, ngang, sổ dài) bên phải.",
        "mnemonic": "Lúa gạo (米) đem vào cái đấu (斗) để đong đo nguyên Liệu (料)."
    },
    {
        "char": "理", "hv": "Lý", "lesson": "L12", "lessonName": "Bài 12", "strokes": 11,
        "meaning": "Đạo lý, lý do, xử lý, nấu nướng", "kun": "-", "on": "り",
        "examples": [
            {"word": "料理", "reading": "りょうり", "vi": "Món ăn, nấu nướng"},
            {"word": "理由", "reading": "りゆう", "vi": "Lý do, nguyên nhân"},
            {"word": "無理", "reading": "むり", "vi": "Quá sức, vô lý"},
            {"word": "地理", "reading": "ちり", "vi": "Địa lý"}
        ],
        "formula": "王 (Vương - ngọc) ＋ 里 (Lý - làng xóm)",
        "strokeGuide": "Bộ Vương (王 - 4 nét) bên trái ➔ chữ Lý (里 - 7 nét: bộ Điền 田 + bộ Thổ 土) bên phải.",
        "mnemonic": "Vị vua (王) đem viên ngọc quý về giảng giải đạo Lý (理) cho dân làng (里)."
    },
    {
        "char": "味", "hv": "Vị", "lesson": "L12", "lessonName": "Bài 12", "strokes": 8,
        "meaning": "Mùi vị, hương vị, ý nghĩa", "kun": "あじ", "on": "み",
        "examples": [
            {"word": "味", "reading": "あじ", "vi": "Mùi vị, hương vị"},
            {"word": "意味", "reading": "いみ", "vi": "Ý nghĩa"},
            {"word": "興味", "reading": "きょうみ", "vi": "Hứng thú, quan tâm"},
            {"word": "味噌汁", "reading": "みそしる", "vi": "Canh súp tương Miso"}
        ],
        "formula": "口 (Khẩu) ＋ 未 (Vị - chưa trổ)",
        "strokeGuide": "Bộ Khẩu (口 - 3 nét) bên trái ➔ chữ Vị (未 - 5 nét: ngang ngắn, ngang dài, sổ, phẩy, mác) bên phải.",
        "mnemonic": "Cái miệng (口) nếm thử quả non chưa chín (未) để biết Vị (味)."
    },
    {
        "char": "色", "hv": "Sắc", "lesson": "L12", "lessonName": "Bài 12", "strokes": 6,
        "meaning": "Màu sắc, sắc mặt, vẻ ngoài", "kun": "いろ", "on": "しょく、しき",
        "examples": [
            {"word": "色", "reading": "いろ", "vi": "Màu sắc"},
            {"word": "茶色", "reading": "ちゃいろ", "vi": "Màu nâu (màu nước trà)"},
            {"word": "景色", "reading": "けしき", "vi": "Phong cảnh, cảnh sắc"},
            {"word": "色々", "reading": "いろいろ", "vi": "Đa dạng, nhiều loại"}
        ],
        "formula": "⺈ ＋ 巳 (Ba)",
        "strokeGuide": "Bộ Đao cách điệu (⺈ - 2 nét trên) ➔ nét ngang gập và nét sổ cong móc (巳 - 4 nét dưới).",
        "mnemonic": "Con người bộc lộ cảm xúc và sắc mặt rực rỡ muôn màu Sắc (色)."
    },
    {
        "char": "野", "hv": "Dã", "lesson": "L12", "lessonName": "Bài 12", "strokes": 11,
        "meaning": "Đồng nội, hoang dã, lĩnh vực", "kun": "の", "on": "や",
        "examples": [
            {"word": "野菜", "reading": "やさい", "vi": "Rau xanh, rau củ"},
            {"word": "野球", "reading": "やきゅう", "vi": "Môn bóng chày"},
            {"word": "分野", "reading": "ぶんや", "vi": "Lĩnh vực chuyên môn"},
            {"word": "長野", "reading": "ながの", "vi": "Tỉnh Nagano (Nhật Bản)"}
        ],
        "formula": "里 (Lý) ＋ 予 (Dự)",
        "strokeGuide": "Chữ Lý (里 - 7 nét) bên trái ➔ chữ Dự (予 - 4 nét: phẩy ngang, sổ móc, 2 chấm) bên phải.",
        "mnemonic": "Nơi thôn dã (里) đem lại những dự báo (予) diệu kỳ về mùa màng Dã (野)."
    },
    {
        "char": "菜", "hv": "Thái", "lesson": "L12", "lessonName": "Bài 12", "strokes": 11,
        "meaning": "Rau xanh, món ăn thức ăn", "kun": "-", "on": "さい",
        "examples": [
            {"word": "野菜", "reading": "やさい", "vi": "Rau củ, rau xanh"},
            {"word": "白菜", "reading": "はくさい", "vi": "Cải thảo"},
            {"word": "菜食", "reading": "さいしょく", "vi": "Ăn chay, chế độ ăn rau củ"},
            {"word": "惣菜", "reading": "そうざい", "vi": "Đồ ăn kèm, món chế biến sẵn"}
        ],
        "formula": "艹 (Thảo) ＋ 采 (Thải - hái lượm)",
        "strokeGuide": "Bộ Thảo (艹 - 3 nét) bên trên ➔ chữ Thải (采 - 8 nét: trảo 爫 + mộc 木) bên dưới.",
        "mnemonic": "Hái ngọn cỏ cây (艹) dùng bàn tay hái (采) về làm món rau Thái (菜)."
    },
    {
        "char": "少", "hv": "Thiểu", "lesson": "L12", "lessonName": "Bài 12", "strokes": 4,
        "meaning": "Ít ỏi, một chút, thiếu niên", "kun": "すく-ない、すこ-し", "on": "しょう",
        "examples": [
            {"word": "少し", "reading": "すこし", "vi": "Một chút, một ít"},
            {"word": "少ない", "reading": "すくない", "vi": "Ít ỏi, hiếm hoi"},
            {"word": "少年", "reading": "しょうねん", "vi": "Thiếu niên"},
            {"word": "少女", "reading": "しょうじょ", "vi": "Thiếu nữ"}
        ],
        "formula": "小 (Tiểu) ＋ 丿 (Phiệt)",
        "strokeGuide": "Sổ móc giữa ➔ chấm trái ➔ phẩy phải ➔ nét phẩy dài chéo xuống dưới trái.",
        "mnemonic": "Đã nhỏ bé (小) lại thêm một nét phẩy tức là càng ít Thiểu (少) hơn nữa."
    },

    # LESSON 13 (9 chữ)
    {
        "char": "会", "hv": "Hội", "lesson": "L13", "lessonName": "Bài 13", "strokes": 6,
        "meaning": "Gặp gỡ, tụ họp, hội thảo", "kun": "あ-う", "on": "かい",
        "examples": [
            {"word": "会います", "reading": "あいます", "vi": "Gặp gỡ"},
            {"word": "会社", "reading": "かいしゃ", "vi": "Công ty"},
            {"word": "会議", "reading": "かいぎ", "vi": "Cuộc họp"},
            {"word": "会話", "reading": "かいわ", "vi": "Hội thoại"}
        ],
        "formula": "人 (Nhân) ＋ 一 ＋ ム",
        "strokeGuide": "Nét phẩy và nét mác (bộ Nhân) trên cùng ➔ nét ngang giữa ➔ chữ Khư (厶 - 2 nét) bên dưới.",
        "mnemonic": "Mọi người (人) cùng tề tựu dưới một mái nhà sum Hội (会)."
    },
    {
        "char": "社", "hv": "Xã", "lesson": "L13", "lessonName": "Bài 13", "strokes": 7,
        "meaning": "Công ty, đền miếu, xã hội", "kun": "-", "on": "しゃ",
        "examples": [
            {"word": "会社", "reading": "かいしゃ", "vi": "Công ty"},
            {"word": "本社", "reading": "ほんしゃ", "vi": "Trụ sở chính"},
            {"word": "支社", "reading": "ししゃ", "vi": "Chi nhánh công ty"},
            {"word": "社会", "reading": "しゃかい", "vi": "Xã hội"}
        ],
        "formula": "礻 (Kỳ - thần linh) ＋ 土 (Thổ - đất đai)",
        "strokeGuide": "Bộ Kỳ (礻 - 4 nét) bên trái ➔ chữ Thổ (土 - 3 nét: ngang, sổ, ngang đáy) bên phải.",
        "mnemonic": "Thần linh (礻) bảo vệ đất đai thôn làng thành Xã (社) tắc."
    },
    {
        "char": "支", "hv": "Chi", "lesson": "L13", "lessonName": "Bài 13", "strokes": 4,
        "meaning": "Cành nhánh, chi nhánh, chống đỡ, chi viện", "kun": "-", "on": "し",
        "examples": [
            {"word": "支社", "reading": "ししゃ", "vi": "Chi nhánh công ty"},
            {"word": "支店", "reading": "してん", "vi": "Cửa hàng chi nhánh"},
            {"word": "支配", "reading": "しはい", "vi": "Chi phối, thống trị"},
            {"word": "支援", "reading": "しえん", "vi": "Chi viện, viện trợ"}
        ],
        "formula": "十 ＋ 又",
        "strokeGuide": "Chữ Thập (十 - 2 nét trên) ➔ chữ Hựu (又 - 2 nét dưới: ngang gập, mác dài).",
        "mnemonic": "Bàn tay nắm lấy cành cây chống đỡ phân Chi (支)."
    },
    {
        "char": "張", "hv": "Trương", "lesson": "L13", "lessonName": "Bài 13", "strokes": 11,
        "meaning": "Kéo căng, giương cung, phồng to", "kun": "は-る", "on": "ちょう",
        "examples": [
            {"word": "出張", "reading": "しゅっちょう", "vi": "Chuyến công tác"},
            {"word": "主張", "reading": "しゅちょう", "vi": "Chủ trương"},
            {"word": "緊張", "reading": "きんちょう", "vi": "Căng thẳng, hồi hộp"},
            {"word": "引っ張る", "reading": "ひっぱる", "vi": "Lôi kéo, kéo giật"}
        ],
        "formula": "弓 (Cung) ＋ 長 (Trường - dài)",
        "strokeGuide": "Bộ Cung (弓 - 3 nét) bên trái ➔ chữ Trường (長 - 8 nét) bên phải.",
        "mnemonic": "Cây cung (弓) kéo căng dài (長) gọi là Trương (張)."
    },
    {
        "char": "空", "hv": "Không", "lesson": "L13", "lessonName": "Bài 13", "strokes": 8,
        "meaning": "Bầu trời, khoảng không, trống rỗng", "kun": "そら、あ-く", "on": "くう",
        "examples": [
            {"word": "空港", "reading": "くうこう", "vi": "Sân bay, phi trường"},
            {"word": "空", "reading": "そら", "vi": "Bầu trời"},
            {"word": "空気", "reading": "くうき", "vi": "Không khí"},
            {"word": "空手", "reading": "からて", "vi": "Môn võ Karate (Không thủ)"}
        ],
        "formula": "穴 (Huyệt) ＋ 工 (Công)",
        "strokeGuide": "Bộ Huyệt (穴 - 5 nét trên) ➔ chữ Công (工 - 3 nét dưới: ngang, sổ, ngang đáy).",
        "mnemonic": "Dưới mái hang sâu (穴) người thợ (工) ngước nhìn khoảng Không (空) vô tận."
    },
    {
        "char": "港", "hv": "Cảng", "lesson": "L13", "lessonName": "Bài 13", "strokes": 12,
        "meaning": "Bến cảng, sân bay, hải cảng", "kun": "みなと", "on": "こう",
        "examples": [
            {"word": "空港", "reading": "くうこう", "vi": "Sân bay, phi cảng"},
            {"word": "港", "reading": "みなと", "vi": "Bến cảng, hải cảng"},
            {"word": "港町", "reading": "みなとまち", "vi": "Phố cảng ven biển"},
            {"word": "寄港", "reading": "きこう", "vi": "Ghé cảng, cập cảng"}
        ],
        "formula": "氵 (Thủy) ＋ 巷 (Hạng - ngõ hẻm)",
        "strokeGuide": "Bộ Thủy (氵 - 3 nét) bên trái ➔ chữ Hạng (巷 - 9 nét: Cộng 共 + Tỵ 巳) bên phải.",
        "mnemonic": "Nơi dòng nước (氵) tụ hội muôn ngả thuyền bè là bến Cảng (港)."
    },
    {
        "char": "発", "hv": "Phát", "lesson": "L13", "lessonName": "Bài 13", "strokes": 9,
        "meaning": "Khởi hành, phát ra, phát triển", "kun": "-", "on": "はつ、ほつ",
        "examples": [
            {"word": "出発", "reading": "しゅっぱつ", "vi": "Khởi hành, xuất phát"},
            {"word": "発見", "reading": "はっけん", "vi": "Phát hiện, tìm thấy"},
            {"word": "発音", "reading": "はつおん", "vi": "Phát âm"},
            {"word": "発表", "reading": "はっぴょう", "vi": "Phát biểu, công bố"}
        ],
        "formula": "癶 (Bát - hai chân) ＋ 弓 ＋ 殳",
        "strokeGuide": "Bộ Bát (癶 - 5 nét trên) ➔ hai nét uốn và nét phẩy mác phía dưới.",
        "mnemonic": "Hai chân bước ra bắn tên vút đi Phát (発) động hành trình."
    },
    {
        "char": "着", "hv": "Trước", "lesson": "L13", "lessonName": "Bài 13", "strokes": 12,
        "meaning": "Đến nơi, cập bến, mặc trang phục", "kun": "つ-く、き-る", "on": "ちゃく",
        "examples": [
            {"word": "到着", "reading": "とうちゃく", "vi": "Đến nơi, cập bến"},
            {"word": "着きます", "reading": "つきます", "vi": "Đến, tới nơi"},
            {"word": "着ます", "reading": "きます", "vi": "Mặc (áo, kimono)"},
            {"word": "上着", "reading": "うわぎ", "vi": "Áo khoác ngoài"}
        ],
        "formula": "羊 (Dương - cừu) ＋ 目 (Mục - mắt)",
        "strokeGuide": "Bộ Dương biến thể (羊 - 7 nét trên với nét phẩy dài) ➔ chữ Mục (目 - 5 nét dưới).",
        "mnemonic": "Đàn cừu (羊) mở to mắt (目) mừng rỡ khi tàu cập bến Trước (着)."
    },
    {
        "char": "午", "hv": "Ngọ", "lesson": "L13", "lessonName": "Bài 13", "strokes": 4,
        "meaning": "Giờ ngọ (12 giờ trưa), phương nam", "kun": "-", "on": "ご",
        "examples": [
            {"word": "午前", "reading": "ごぜん", "vi": "Buổi sáng (trước 12h trưa)"},
            {"word": "午後", "reading": "ごご", "vi": "Buổi chiều (sau 12h trưa)"},
            {"word": "正午", "reading": "しょうご", "vi": "Chính ngọ (đúng 12h trưa)"}
        ],
        "formula": "丿 ＋ 一 ＋ 十",
        "strokeGuide": "Nét phẩy trên ➔ nét ngang ngắn ➔ nét ngang dài ➔ nét sổ thẳng giữa.",
        "mnemonic": "Chiếc chày thẳng đứng lúc bóng nắng tròn 12 giờ trưa chính Ngọ (午)."
    },

    # LESSON 14 (8 chữ)
    {
        "char": "自", "hv": "Tự", "lesson": "L14", "lessonName": "Bài 14", "strokes": 6,
        "meaning": "Tự mình, tự thân, tự do", "kun": "みずか-ら", "on": "じ、し",
        "examples": [
            {"word": "自分", "reading": "じぶん", "vi": "Bản thân mình"},
            {"word": "自動車", "reading": "じどうしゃ", "vi": "Xe ô tô"},
            {"word": "自由", "reading": "じゆう", "vi": "Tự do"},
            {"word": "自転車", "reading": "じてんしゃ", "vi": "Xe đạp"}
        ],
        "formula": "丿 ＋ 目 (Mục)",
        "strokeGuide": "Nét phẩy ngắn trên đỉnh ➔ chữ Mục (目 - 5 nét bên dưới).",
        "mnemonic": "Chỉ tay vào mũi chính giữa khuôn mặt tức là nói về Tự (自) mình."
    },
    {
        "char": "分", "hv": "Phân", "lesson": "L14", "lessonName": "Bài 14", "strokes": 4,
        "meaning": "Phân chia, thấu hiểu, phút", "kun": "わ-かる、わ-ける", "on": "ぶん、ふん、ぷん",
        "examples": [
            {"word": "自分", "reading": "じぶん", "vi": "Bản thân mình"},
            {"word": "分かります", "reading": "わかります", "vi": "Hiểu, nắm rõ"},
            {"word": "5分", "reading": "ごふん", "vi": "5 phút"},
            {"word": "半分", "reading": "はんぶん", "vi": "Một nửa"}
        ],
        "formula": "八 (Bát) ＋ 刀 (Đao)",
        "strokeGuide": "Nét phẩy trái và mác phải (bộ Bát - 2 nét trên) ➔ chữ Đao (刀 - 2 nét dưới).",
        "mnemonic": "Dùng con dao (刀) rạch đôi chia thành từng Phân (分) phần rõ ràng."
    },
    {
        "char": "電", "hv": "Điện", "lesson": "L14", "lessonName": "Bài 14", "strokes": 13,
        "meaning": "Điện lực, ánh sáng, tia chớp", "kun": "-", "on": "でん",
        "examples": [
            {"word": "電話", "reading": "でんわ", "vi": "Điện thoại"},
            {"word": "電気", "reading": "でんき", "vi": "Đèn điện, ánh sáng"},
            {"word": "電車", "reading": "でんしゃ", "vi": "Tàu điện"},
            {"word": "電力", "reading": "でんりょく", "vi": "Điện lực"}
        ],
        "formula": "雨 (Vũ) ＋ 申 (Thân)",
        "strokeGuide": "Bộ Vũ (雨 - 8 nét trên) ➔ chữ Thân (申 - 5 nét dưới: khung vuông và nét sổ thẳng).",
        "mnemonic": "Trong cơn mưa (雨) sấm chớp giáng xuống phát ra dòng Điện (電)."
    },
    {
        "char": "話", "hv": "Thoại", "lesson": "L14", "lessonName": "Bài 14", "strokes": 13,
        "meaning": "Nói chuyện, câu chuyện, đối thoại", "kun": "はな-す、はなし", "on": "わ",
        "examples": [
            {"word": "電話", "reading": "でんわ", "vi": "Điện thoại"},
            {"word": "話します", "reading": "はなします", "vi": "Nói chuyện"},
            {"word": "会話", "reading": "かいわ", "vi": "Hội thoại"},
            {"word": "世話", "reading": "せわ", "vi": "Chăm sóc, giúp đỡ"}
        ],
        "formula": "言 (Ngôn) ＋ 舌 (Thiệt - cái lưỡi)",
        "strokeGuide": "Bộ Ngôn (言 - 7 nét trái) ➔ chữ Thiệt (舌 - 6 nét phải).",
        "mnemonic": "Cái lưỡi (舌) cất thành lời nói (言) để chuyện trò đối Thoại (話)."
    },
    {
        "char": "車", "hv": "Xa", "lesson": "L14", "lessonName": "Bài 14", "strokes": 7,
        "meaning": "Xe cộ, bánh xe", "kun": "くるま", "on": "しゃ",
        "examples": [
            {"word": "車", "reading": "くるま", "vi": "Xe ô tô"},
            {"word": "電車", "reading": "でんしゃ", "vi": "Tàu điện"},
            {"word": "自転車", "reading": "じてんしゃ", "vi": "Xe đạp"},
            {"word": "駐車場", "reading": "ちゅうしゃじょう", "vi": "Bãi đỗ xe"}
        ],
        "formula": "一 ＋ 囗 ＋ 十",
        "strokeGuide": "Nét ngang trên ➔ nét sổ trái ➔ gập ngang ➔ 2 nét ngang trong ➔ ngang dài đáy ➔ sổ thẳng xuyên qua.",
        "mnemonic": "Hình cỗ Xa (車) xe có trục và bánh lăn tròn đều."
    },
    {
        "char": "送", "hv": "Tống", "lesson": "L14", "lessonName": "Bài 14", "strokes": 9,
        "meaning": "Gửi đi, tiễn đưa, chuyển phát", "kun": "おく-る", "on": "そう",
        "examples": [
            {"word": "送ります", "reading": "おくります", "vi": "Gửi (email, bưu phẩm) / Tiễn khách"},
            {"word": "郵送", "reading": "ゆうそう", "vi": "Gửi qua đường bưu điện"},
            {"word": "見送る", "reading": "みおくる", "vi": "Tiễn biệt, đưa tiễn"},
            {"word": "転送", "reading": "てんそう", "vi": "Chuyển tiếp thư từ"}
        ],
        "formula": "关 (Quan) ＋ 辶 (Quai xước)",
        "strokeGuide": "Chữ Quan (关 - 6 nét trong: 2 chấm, 2 ngang, phẩy, mác) ➔ bộ Quai xước (辶 - 3 nét ngoài).",
        "mnemonic": "Dõi theo bước chân (辶) tiễn Tống (送) người đi xa."
    },
    {
        "char": "使", "hv": "Sử", "lesson": "L14", "lessonName": "Bài 14", "strokes": 8,
        "meaning": "Sử dụng, sai khiến, đại sứ", "kun": "つか-う", "on": "し",
        "examples": [
            {"word": "使います", "reading": "つかいます", "vi": "Sử dụng, dùng"},
            {"word": "使い方", "reading": "つかいかた", "vi": "Cách sử dụng"},
            {"word": "大使館", "reading": "たいしかん", "vi": "Đại sứ quán"},
            {"word": "使用", "reading": "しよう", "vi": "Sử dụng"}
        ],
        "formula": "亻 (Nhân đứng) ＋ 吏 (Lại - quan lại)",
        "strokeGuide": "Bộ Nhân đứng (亻 - 2 nét trái) ➔ chữ Lại (吏 - 6 nét phải: ngang, khẩu 口, phẩy, mác).",
        "mnemonic": "Con người (亻) được quan sai phái ra ngoài Sử (使) dụng tài trí."
    },
    {
        "char": "借", "hv": "Tá", "lesson": "L14", "lessonName": "Bài 14", "strokes": 10,
        "meaning": "Vay mượn đồ đạc, nợ nần", "kun": "か-りる", "on": "しゃく",
        "examples": [
            {"word": "借ります", "reading": "かります", "vi": "Vay mượn"},
            {"word": "借用書", "reading": "しゃくようしょ", "vi": "Giấy vay nợ"},
            {"word": "借金", "reading": "しゃっきん", "vi": "Khoản nợ, tiền vay"}
        ],
        "formula": "亻 (Nhân đứng) ＋ 昔 (Tích - ngày xưa)",
        "strokeGuide": "Bộ Nhân đứng (亻 - 2 nét trái) ➔ chữ Tích (昔 - 8 nét phải: Thảo cách điệu + Nhật 日).",
        "mnemonic": "Người (亻) từ ngày xưa (昔) vẫn thường tìm đến vay mượn Tá (借) của nhau."
    },

    # LESSON 15 (9 chữ)
    {
        "char": "体", "hv": "Thể", "lesson": "L15", "lessonName": "Bài 15", "strokes": 7,
        "meaning": "Thân thể, cơ thể, thể dục", "kun": "からだ", "on": "たい、てい",
        "examples": [
            {"word": "体", "reading": "からだ", "vi": "Thân thể, cơ thể"},
            {"word": "体操", "reading": "たいそう", "vi": "Tập thể dục"},
            {"word": "体調", "reading": "たいちょう", "vi": "Tình trạng sức khỏe"},
            {"word": "体重", "reading": "たいじゅう", "vi": "Cân nặng, thể trọng"}
        ],
        "formula": "亻 (Nhân đứng) ＋ 本 (Bổn - cội gốc)",
        "strokeGuide": "Bộ Nhân đứng (亻 - 2 nét trái) ➔ chữ Bổn (本 - 5 nét phải: Mộc 木 + nét ngang đáy).",
        "mnemonic": "Cội gốc (本) quý giá nhất của con người (亻) chính là Thân Thể (体)."
    },
    {
        "char": "頭", "hv": "Đầu", "lesson": "L15", "lessonName": "Bài 15", "strokes": 16,
        "meaning": "Cái đầu, đầu óc, đứng đầu", "kun": "あたま", "on": "とう、ず",
        "examples": [
            {"word": "頭", "reading": "あたま", "vi": "Cái đầu"},
            {"word": "頭痛", "reading": "ずつう", "vi": "Đau đầu"},
            {"word": "頭角", "reading": "とうかく", "vi": "Xuất đầu lộ diện, nổi bật"},
            {"word": "先頭", "reading": "せんとう", "vi": "Dẫn đầu, đi đầu"}
        ],
        "formula": "豆 (Đậu) ＋ 頁 (Hiệt - đầu)",
        "strokeGuide": "Chữ Đậu (豆 - 7 nét trái) ➔ bộ Hiệt (頁 - 9 nét phải).",
        "mnemonic": "Hạt đậu (豆) nhỏ đặt trên đỉnh đầu (頁) biểu trưng cho Đầu (頭) não."
    },
    {
        "char": "目", "hv": "Mục", "lesson": "L15", "lessonName": "Bài 15", "strokes": 5,
        "meaning": "Con mắt, mục lục, mục tiêu", "kun": "め", "on": "もく",
        "examples": [
            {"word": "目", "reading": "め", "vi": "Con mắt"},
            {"word": "目薬", "reading": "めぐすり", "vi": "Thuốc nhỏ mắt"},
            {"word": "目的", "reading": "もくてき", "vi": "Mục đích"},
            {"word": "注目", "reading": "ちゅうもく", "vi": "Chú ý, để mắt tới"}
        ],
        "formula": "Khung hình chữ nhật ＋ 2 nét ngang trong",
        "strokeGuide": "Sổ trái ➔ gập ngang sổ xuống ➔ 2 nét ngang trong ➔ đóng đáy ngang.",
        "mnemonic": "Hình vẽ tròng mắt có con ngươi tinh anh sáng Mục (目)."
    },
    {
        "char": "口", "hv": "Khẩu", "lesson": "L15", "lessonName": "Bài 15", "strokes": 3,
        "meaning": "Cái miệng, cửa ra vào, nhân khẩu", "kun": "くち", "on": "こう、く",
        "examples": [
            {"word": "口", "reading": "くち", "vi": "Cái miệng"},
            {"word": "入口", "reading": "いりぐち", "vi": "Lối vào, cửa vào"},
            {"word": "出口", "reading": "でぐち", "vi": "Lối ra, cửa ra"},
            {"word": "人口", "reading": "じんこう", "vi": "Dân số, nhân khẩu"}
        ],
        "formula": "Hình vuông ba nét",
        "strokeGuide": "Sổ trái ➔ gập ngang sổ xuống ➔ đóng đáy ngang.",
        "mnemonic": "Hình vẽ cái miệng vuông vức mở ra nói lời hay Khẩu (口)."
    },
    {
        "char": "耳", "hv": "Nhĩ", "lesson": "L15", "lessonName": "Bài 15", "strokes": 6,
        "meaning": "Cái tai, lắng nghe", "kun": "みみ", "on": "じ",
        "examples": [
            {"word": "耳", "reading": "みみ", "vi": "Cái tai"},
            {"word": "初耳", "reading": "はつみみ", "vi": "Lần đầu nghe thấy"},
            {"word": "耳鼻科", "reading": "じびか", "vi": "Khoa tai mũi họng"}
        ],
        "formula": "Một nét ngang ＋ 2 sổ ＋ 2 ngang trong ➔ ngang dài chéo",
        "strokeGuide": "Ngang trên ➔ 2 sổ dọc ➔ 2 ngang giữa ➔ nét ngang dài chéo đáy.",
        "mnemonic": "Hình vẽ vành tai hứng trọn âm thanh bốn phương Nhĩ (耳)."
    },
    {
        "char": "手", "hv": "Thủ", "lesson": "L15", "lessonName": "Bài 15", "strokes": 4,
        "meaning": "Bàn tay, thủ thuật, người làm", "kun": "て", "on": "しゅ",
        "examples": [
            {"word": "手", "reading": "て", "vi": "Bàn tay"},
            {"word": "手紙", "reading": "てがみ", "vi": "Bức thư"},
            {"word": "上手", "reading": "じょうず", "vi": "Giỏi giang"},
            {"word": "下手", "reading": "へた", "vi": "Vụng về, kém cỏi"}
        ],
        "formula": "Nét phẩy ＋ 2 nét ngang ＋ sổ cong móc",
        "strokeGuide": "Phẩy ngắn trên ➔ ngang ngắn ➔ ngang dài ➔ sổ cong móc giữa.",
        "mnemonic": "Hình bàn tay xòe ra năm ngón làm nên cơ nghiệp Thủ (手)."
    },
    {
        "char": "足", "hv": "Túc", "lesson": "L15", "lessonName": "Bài 15", "strokes": 7,
        "meaning": "Bàn chân, cẳng chân, đầy đủ", "kun": "あし、た-りる", "on": "そく",
        "examples": [
            {"word": "足", "reading": "あし", "vi": "Bàn chân, cẳng chân"},
            {"word": "足ります", "reading": "たります", "vi": "Đầy đủ"},
            {"word": "遠足", "reading": "えんそく", "vi": "Dã ngoại, chuyến đi bộ đường dài"},
            {"word": "不足", "reading": "ふそく", "vi": "Không đủ, thiếu thốn"}
        ],
        "formula": "口 (Khẩu) ＋ 止 (Chỉ)",
        "strokeGuide": "Chữ Khẩu (口 - 3 nét trên) ➔ sổ giữa, ngang, sổ trái, mác dài đáy (4 nét dưới).",
        "mnemonic": "Đôi chân vững vàng bước đi mang lại ấm no sung Túc (足)."
    },
    {
        "char": "上", "hv": "Thượng", "lesson": "L15", "lessonName": "Bài 15", "strokes": 3,
        "meaning": "Bên trên, tiến lên, thượng đẳng", "kun": "うえ、あ-がる", "on": "じょう",
        "examples": [
            {"word": "上", "reading": "うえ", "vi": "Phía trên, bên trên"},
            {"word": "上手", "reading": "じょうず", "vi": "Giỏi giang"},
            {"word": "屋上", "reading": "おくじょう", "vi": "Sân thượng"},
            {"word": "上着", "reading": "うわぎ", "vi": "Áo khoác ngoài"}
        ],
        "formula": "Sổ ngắn ＋ ngang ngắn ＋ ngang dài đáy",
        "strokeGuide": "Nét sổ đứng ➔ nét ngang ngắn bên phải ➔ nét ngang dài bên dưới.",
        "mnemonic": "Nét sổ vươn cao phía TRÊN đường ngang chỉ vị trí Thượng (上)."
    },
    {
        "char": "下", "hv": "Hạ", "lesson": "L15", "lessonName": "Bài 15", "strokes": 3,
        "meaning": "Bên dưới, hạ thấp, hạ đẳng", "kun": "した、さ-がる", "on": "か、げ",
        "examples": [
            {"word": "下", "reading": "した", "vi": "Phía dưới, bên dưới"},
            {"word": "下手", "reading": "へた", "vi": "Vụng về, kém cỏi"},
            {"word": "地下", "reading": "ちか", "vi": "Dưới lòng đất"},
            {"word": "靴下", "reading": "くつした", "vi": "Đôi tất chân"}
        ],
        "formula": "Ngang dài đỉnh ➔ sổ ngắn ➔ chấm phải",
        "strokeGuide": "Nét ngang dài trên cùng ➔ nét sổ ngắn xuống ➔ nét chấm/phẩy bên phải.",
        "mnemonic": "Nét sổ chúc xuống phía DƯỚI đường ngang chỉ vị trí Hạ (下)."
    },

    # LESSON 16 (10 chữ)
    {
        "char": "毎", "hv": "Mỗi", "lesson": "L16", "lessonName": "Bài 16", "strokes": 6,
        "meaning": "Mỗi một, từng, hàng ngày", "kun": "ごと", "on": "まい",
        "examples": [
            {"word": "毎日", "reading": "まいにち", "vi": "Mỗi ngày, hàng ngày"},
            {"word": "毎朝", "reading": "まいあさ", "vi": "Mỗi sáng"},
            {"word": "毎週", "reading": "まいしゅう", "vi": "Mỗi tuần"},
            {"word": "毎年", "reading": "まいとし", "vi": "Mỗi năm"}
        ],
        "formula": "𠂉 (Nhân cách điệu) ＋ 母 (Mẫu - người mẹ)",
        "strokeGuide": "Phẩy và ngang (2 nét trên) ➔ nét sổ gập, ngang trong, 2 chấm, ngang đáy (4 nét dưới).",
        "mnemonic": "Hình người mẹ (母) tần tảo chăm sóc gia đình Mỗi (毎) ngày."
    },
    {
        "char": "末", "hv": "Mạt", "lesson": "L16", "lessonName": "Bài 16", "strokes": 5,
        "meaning": "Ngọn cây, cuối cùng, kết thúc", "kun": "すえ", "on": "まつ",
        "examples": [
            {"word": "週末", "reading": "しゅうまつ", "vi": "Cuối tuần"},
            {"word": "年末", "reading": "ねんまつ", "vi": "Cuối năm"},
            {"word": "月末", "reading": "げつまつ", "vi": "Cuối tháng"},
            {"word": "期末", "reading": "きまつ", "vi": "Cuối kỳ"}
        ],
        "formula": "一 (Ngang dài) ＋ 木 (Mộc với ngang ngắn)",
        "strokeGuide": "Ngang dài trên ➔ ngang ngắn dưới ➔ sổ thẳng giữa ➔ phẩy trái ➔ mác phải.",
        "mnemonic": "Cành cây trên dài hơn cành dưới chỉ phần ngọn, cuối Mạt (末)."
    },
    {
        "char": "元", "hv": "Nguyên", "lesson": "L16", "lessonName": "Bài 16", "strokes": 4,
        "meaning": "Nguồn gốc, căn nguyên, nguyên khí", "kun": "もと", "on": "げん、がん",
        "examples": [
            {"word": "元気", "reading": "げんき", "vi": "Khỏe mạnh, tràn đầy sinh lực"},
            {"word": "元日", "reading": "がんじつ", "vi": "Ngày mồng một Tết"},
            {"word": "元々", "reading": "もともと", "vi": "Vốn dĩ, ban đầu"}
        ],
        "formula": "二 (Nhị) ＋ 儿 (Nhân)",
        "strokeGuide": "Ngang ngắn trên ➔ ngang dài dưới ➔ phẩy trái ➔ cong móc phải.",
        "mnemonic": "Trời đất (二) sinh ra con người (儿) là cội nguồn Nguyên (元) thủy."
    },
    {
        "char": "外", "hv": "Ngoại", "lesson": "L16", "lessonName": "Bài 16", "strokes": 5,
        "meaning": "Bên ngoài, ngoại quốc", "kun": "そと、はず-す", "on": "がい、げ",
        "examples": [
            {"word": "外", "reading": "そと", "vi": "Bên ngoài"},
            {"word": "外国", "reading": "がいこく", "vi": "Nước ngoài"},
            {"word": "外出", "reading": "がいしゅつ", "vi": "Đi ra ngoài"},
            {"word": "海外", "reading": "かいがい", "vi": "Hải ngoại"}
        ],
        "formula": "夕 (Tịch - buổi chiều) ＋ 卜 (Bốc - bói toán)",
        "strokeGuide": "Bộ Tịch (夕 - 3 nét trái) ➔ bộ Bốc (卜 - 2 nét phải: sổ dọc và chấm phải).",
        "mnemonic": "Buổi chiều tà (夕) gieo quẻ bói (卜) đoán chuyện bên Ngoại (外)."
    },
    {
        "char": "起", "hv": "Khởi", "lesson": "L16", "lessonName": "Bài 16", "strokes": 10,
        "meaning": "Thức dậy, đứng lên, khởi đầu", "kun": "お-きる、お-こす", "on": "き",
        "examples": [
            {"word": "起きます", "reading": "おきます", "vi": "Thức dậy"},
            {"word": "早起き", "reading": "はやおき", "vi": "Dậy sớm"},
            {"word": "起立", "reading": "きりつ", "vi": "Đứng dậy (hiệu lệnh)"}
        ],
        "formula": "走 (Tẩu - chạy) ＋ 己 (Kỷ - bản thân)",
        "strokeGuide": "Bộ Tẩu (走 - 7 nét trái) ➔ chữ Kỷ (己 - 3 nét phải: ngang gập, ngang, cong móc).",
        "mnemonic": "Chạy bộ (走) đưa bản thân mình (己) đứng dậy Khởi (起) sắc ngày mới."
    },
    {
        "char": "歩", "hv": "Bộ", "lesson": "L16", "lessonName": "Bài 16", "strokes": 8,
        "meaning": "Đi bộ, từng bước, tản bộ", "kun": "ある-く、あゆ-む", "on": "ほ、ぽ",
        "examples": [
            {"word": "歩きます", "reading": "あるきます", "vi": "Đi bộ"},
            {"word": "散歩", "reading": "さんぽ", "vi": "Tản bộ, đi dạo"},
            {"word": "歩道", "reading": "ほどう", "vi": "Lối đi bộ, vỉa hè"}
        ],
        "formula": "止 (Chỉ) ＋ 少 (Thiếu biến thể)",
        "strokeGuide": "Bộ Chỉ (止 - 4 nét trên) ➔ nét phẩy, sổ gập, chấm (4 nét dưới).",
        "mnemonic": "Dừng lại (止) rồi bước tiếp từng bước chân đi Bộ (歩)."
    },
    {
        "char": "走", "hv": "Tẩu", "lesson": "L16", "lessonName": "Bài 16", "strokes": 7,
        "meaning": "Chạy, tẩu thoát, di chuyển nhanh", "kun": "はし-る", "on": "そう",
        "examples": [
            {"word": "走ります", "reading": "はしります", "vi": "Chạy bộ"},
            {"word": "ご馳走", "reading": "ごちそう", "vi": "Bữa tiệc chiêu đãi"},
            {"word": "走行", "reading": "そうこう", "vi": "Chạy xe, lưu thông"}
        ],
        "formula": "土 (Thổ) ＋ 疋 (Sơ biến thể)",
        "strokeGuide": "Chữ Thổ (土 - 3 nét trên) ➔ nét sổ giữa, ngang ngắn, phẩy dài, mác dài (4 nét dưới).",
        "mnemonic": "Người vung chân lao qua lớp đất cát (土) Tẩu (走) chạy thật mau."
    },
    {
        "char": "泳", "hv": "Vịnh", "lesson": "L16", "lessonName": "Bài 16", "strokes": 8,
        "meaning": "Bơi lội dưới nước", "kun": "およ-ぐ", "on": "えい",
        "examples": [
            {"word": "泳ぎます", "reading": "およぎます", "vi": "Bơi lội"},
            {"word": "水泳", "reading": "すいえい", "vi": "Môn bơi lội"},
            {"word": "平泳ぎ", "reading": "ひらおよぎ", "vi": "Bơi ếch"}
        ],
        "formula": "氵 (Thủy) ＋ 永 (Vĩnh - vĩnh cửu)",
        "strokeGuide": "Bộ Thủy (氵 - 3 nét trái) ➔ chữ Vĩnh (永 - 5 nét phải: chấm, ngang gập móc, phẩy, mác).",
        "mnemonic": "Làn nước (氵) trong xanh vĩnh hằng (永) là nơi thỏa sức bơi lội Vịnh (泳)."
    },
    {
        "char": "朝", "hv": "Triều", "lesson": "L16", "lessonName": "Bài 16", "strokes": 12,
        "meaning": "Buổi sáng, ban mai, triều đình", "kun": "あさ", "on": "ちょう",
        "examples": [
            {"word": "朝", "reading": "あさ", "vi": "Buổi sáng"},
            {"word": "毎朝", "reading": "まいあさ", "vi": "Mỗi sáng"},
            {"word": "朝食", "reading": "ちょうしょく", "vi": "Bữa ăn sáng"},
            {"word": "今朝", "reading": "けさ", "vi": "Sáng nay"}
        ],
        "formula": "十 ＋ 日 ＋ 十 ＋ 月 (Nguyệt)",
        "strokeGuide": "Ngang, sổ (Thập) ➔ Nhật 日 ➔ Thập 十 (8 nét trái) ➔ chữ Nguyệt (月 - 4 nét phải).",
        "mnemonic": "Mặt trời (日) mọc trên ngọn cỏ cùng vầng trăng (月) còn lấp lánh ban Triều (朝)."
    },
    {
        "char": "気", "hv": "Khí", "lesson": "L16", "lessonName": "Bài 16", "strokes": 6,
        "meaning": "Không khí, khí sắc, tinh thần", "kun": "-", "on": "き、け",
        "examples": [
            {"word": "元気", "reading": "げんき", "vi": "Khỏe mạnh"},
            {"word": "天気", "reading": "てんき", "vi": "Thời tiết"},
            {"word": "気持ち", "reading": "きもち", "vi": "Cảm giác, tâm trạng"},
            {"word": "気に入る", "reading": "きにいる", "vi": "Ưa thích, vừa ý"}
        ],
        "formula": "气 (Khí) ＋ 乂",
        "strokeGuide": "Phẩy ngắn trên ➔ ngang ➔ ngang dài gập cong móc ➔ 2 nét chéo (乂) bên trong.",
        "mnemonic": "Luồng hơi nước bốc lên từ nồi cơm tỏa ra nguyên Khí (気) đất trời."
    },

    # LESSON 17 (8 chữ)
    {
        "char": "祝", "hv": "Chúc", "lesson": "L17", "lessonName": "Bài 17", "strokes": 9,
        "meaning": "Chúc mừng, cầu phúc, lễ mừng", "kun": "いわ-う", "on": "しゅく",
        "examples": [
            {"word": "お祝い", "reading": "おいわい", "vi": "Quà mừng, sự chúc mừng"},
            {"word": "祝日", "reading": "しゅくじつ", "vi": "Ngày lễ tết"},
            {"word": "祝福", "reading": "しゅくふく", "vi": "Chúc phúc, ban phước"}
        ],
        "formula": "礻 (Kỳ - thần) ＋ 兄 (Huynh - anh trai)",
        "strokeGuide": "Bộ Kỳ (礻 - 4 nét trái) ➔ chữ Huynh (兄 - 5 nét phải: Khẩu 口 + Nhi 儿).",
        "mnemonic": "Người anh trai (兄) thay mặt gia đình dâng lễ lên Thần linh (礻) cầu Chúc (祝)."
    },
    {
        "char": "誕", "hv": "Đản", "lesson": "L17", "lessonName": "Bài 17", "strokes": 15,
        "meaning": "Sinh ra, giáng sinh, đản sinh", "kun": "-", "on": "たん",
        "examples": [
            {"word": "誕生日", "reading": "たんじょうび", "vi": "Ngày sinh nhật"},
            {"word": "生誕", "reading": "せいたん", "vi": "Sinh đẻ, giáng sinh"},
            {"word": "誕生", "reading": "たんじょう", "vi": "Sự ra đời, chào đời"}
        ],
        "formula": "言 (Ngôn) ＋ 延 (Duyên - kéo dài)",
        "strokeGuide": "Bộ Ngôn (言 - 7 nét trái) ➔ chữ Duyên (延 - 8 nét phải).",
        "mnemonic": "Dùng muôn lời ca tụng (言) kéo dài (延) mãi ngày chào đời Đản (誕) sinh."
    },
    {
        "char": "結", "hv": "Kết", "lesson": "L17", "lessonName": "Bài 17", "strokes": 12,
        "meaning": "Buộc lại, gắn kết, kết quả, kết hôn", "kun": "むす-ぶ", "on": "けつ、けっ",
        "examples": [
            {"word": "結婚", "reading": "けっこん", "vi": "Kết hôn, cưới xin"},
            {"word": "結びます", "reading": "むすびます", "vi": "Thắt nút, buộc lại"},
            {"word": "結果", "reading": "けっか", "vi": "Kết quả"},
            {"word": "結論", "reading": "けつろん", "vi": "Kết luận"}
        ],
        "formula": "糸 (Mịch - sợi chỉ) ＋ 吉 (Cát - tốt lành)",
        "strokeGuide": "Bộ Mịch (糸 - 6 nét trái) ➔ chữ Cát (吉 - 6 nét phải: Thổ 土 + Khẩu 口).",
        "mnemonic": "Sợi tơ hồng (糸) mang lại điều cát tường (吉) Kết (結) duyên đôi lứa."
    },
    {
        "char": "婚", "hv": "Hôn", "lesson": "L17", "lessonName": "Bài 17", "strokes": 11,
        "meaning": "Hôn nhân, đám cưới", "kun": "-", "on": "こん",
        "examples": [
            {"word": "結婚", "reading": "けっこん", "vi": "Kết hôn"},
            {"word": "婚約", "reading": "こんやく", "vi": "Đính hôn, hứa hôn"},
            {"word": "新婚", "reading": "しんこん", "vi": "Tân hôn, mới cưới"},
            {"word": "離婚", "reading": "りこん", "vi": "Ly hôn"}
        ],
        "formula": "女 (Nữ) ＋ 昏 (Hôn - chiều tà)",
        "strokeGuide": "Bộ Nữ (女 - 3 nét trái) ➔ chữ Hôn (昏 - 8 nét phải: Thị 氏 + Nhật 日).",
        "mnemonic": "Người con gái (女) bước lên kiệu hoa trong buổi hoàng Hôn (婚) lễ."
    },
    {
        "char": "絵", "hv": "Hội", "lesson": "L17", "lessonName": "Bài 17", "strokes": 12,
        "meaning": "Bức tranh vẽ, hội họa", "kun": "-", "on": "え、かい",
        "examples": [
            {"word": "絵", "reading": "え", "vi": "Bức tranh vẽ"},
            {"word": "絵本", "reading": "えほん", "vi": "Sách tranh thiếu nhi"},
            {"word": "絵画", "reading": "かいが", "vi": "Tranh hội họa nghệ thuật"},
            {"word": "油絵", "reading": "あぶらえ", "vi": "Tranh sơn dầu"}
        ],
        "formula": "糸 (Mịch) ＋ 会 (Hội)",
        "strokeGuide": "Bộ Mịch (糸 - 6 nét trái) ➔ chữ Hội (会 - 6 nét phải).",
        "mnemonic": "Sợi chỉ màu (糸) hội tụ (会) trên khung vải dệt nên bức Hội (絵) họa."
    },
    {
        "char": "写", "hv": "Tả", "lesson": "L17", "lessonName": "Bài 17", "strokes": 5,
        "meaning": "Chụp ảnh, sao chép, miêu tả", "kun": "うつ-す", "on": "しゃ",
        "examples": [
            {"word": "写真", "reading": "しゃしん", "vi": "Bức ảnh chụp"},
            {"word": "写します", "reading": "うつします", "vi": "Chụp (ảnh), chép lại"},
            {"word": "描写", "reading": "びょうしゃ", "vi": "Miêu tả, khắc họa"}
        ],
        "formula": "冖 (Mịch - mái che) ＋ 与 (Dữ)",
        "strokeGuide": "Bộ Mịch (冖 - 2 nét trên) ➔ nét sổ gập, ngang, cong móc (3 nét dưới).",
        "mnemonic": "Đặt máy dưới mái che (冖) chụp lại bức hình miêu Tả (写) chân dung."
    },
    {
        "char": "真", "hv": "Chân", "lesson": "L17", "lessonName": "Bài 17", "strokes": 10,
        "meaning": "Chân thực, đúng đắn, sự thật", "kun": "ま", "on": "しん",
        "examples": [
            {"word": "写真", "reading": "しゃしん", "vi": "Bức ảnh"},
            {"word": "真実", "reading": "しんじつ", "vi": "Chân thực, sự thật"},
            {"word": "真ん中", "reading": "まんなか", "vi": "Chính giữa"},
            {"word": "真面目", "reading": "まじめ", "vi": "Chăm chỉ, nghiêm túc"}
        ],
        "formula": "十 ＋ 目 ＋ 八",
        "strokeGuide": "Thập 十 trên cùng ➔ Mục 目 giữa ➔ nét ngang dài ➔ 2 nét chấm chéo chân đáy.",
        "mnemonic": "Mười (十) con mắt (目) cùng nhìn thấu Chân (真) tướng sự thật."
    },
    {
        "char": "計", "hv": "Kế", "lesson": "L17", "lessonName": "Bài 17", "strokes": 9,
        "meaning": "Kế hoạch, đo đạc, tính toán, đồng hồ", "kun": "はか-る", "on": "けい",
        "examples": [
            {"word": "時計", "reading": "とけい", "vi": "Đồng hồ"},
            {"word": "計画", "reading": "けいかく", "vi": "Kế hoạch"},
            {"word": "合計", "reading": "ごうけい", "vi": "Tổng cộng"},
            {"word": "体温計", "reading": "たいおんけい", "vi": "Nhiệt kế đo thân nhiệt"}
        ],
        "formula": "言 (Ngôn) ＋ 十 (Thập)",
        "strokeGuide": "Bộ Ngôn (言 - 7 nét trái) ➔ chữ Thập (十 - 2 nét phải: ngang, sổ).",
        "mnemonic": "Dùng lời nói (言) đếm đủ mười (十) điều lập nên mưu Kế (計) đo đạc."
    },

    # LESSON 18 (7 chữ)
    {
        "char": "先", "hv": "Tiên", "lesson": "L18", "lessonName": "Bài 18", "strokes": 6,
        "meaning": "Trước, đi đầu, quá khứ, giáo viên", "kun": "さき", "on": "せん",
        "examples": [
            {"word": "先週", "reading": "せんしゅう", "vi": "Tuần trước"},
            {"word": "先生", "reading": "せんせい", "vi": "Giáo viên, thầy cô"},
            {"word": "先月", "reading": "せんげつ", "vi": "Tháng trước"},
            {"word": "先輩", "reading": "せんぱい", "vi": "Tiền bối, đàn anh"}
        ],
        "formula": "牛 biến thể ＋ 儿 (Nhân)",
        "strokeGuide": "Phẩy, ngang, sổ, ngang dài (4 nét trên) ➔ phẩy trái, cong móc phải (2 nét chân).",
        "mnemonic": "Đôi chân bước vội về phía trước dẫn đầu Tiên (先) phong."
    },
    {
        "char": "今", "hv": "Kim", "lesson": "L18", "lessonName": "Bài 18", "strokes": 4,
        "meaning": "Hiện tại, bây giờ, nay", "kun": "いま", "on": "こん、きん",
        "examples": [
            {"word": "今月", "reading": "こんげつ", "vi": "Tháng này"},
            {"word": "今年", "reading": "ことし", "vi": "Năm nay"},
            {"word": "今日", "reading": "きょう", "vi": "Hôm nay"},
            {"word": "今週", "reading": "こんしゅう", "vi": "Tuần này"}
        ],
        "formula": "人 (Nhân) ＋ 一 ＋ フ",
        "strokeGuide": "Phẩy và mác (bộ Nhân) ➔ nét chấm/ngang ➔ nét gập cong bên dưới.",
        "mnemonic": "Cái nón úp ngay khoảnh khắc hiện tại lúc này là Kim (今)."
    },
    {
        "char": "来", "hv": "Lai", "lesson": "L18", "lessonName": "Bài 18", "strokes": 7,
        "meaning": "Đến, tương lai, năm sau", "kun": "く-る、き-ます", "on": "らい",
        "examples": [
            {"word": "来年", "reading": "らいねん", "vi": "Năm sau"},
            {"word": "来月", "reading": "らいげつ", "vi": "Tháng sau"},
            {"word": "来週", "reading": "らいしゅう", "vi": "Tuần sau"},
            {"word": "来ます", "reading": "きます", "vi": "Đến, tới nơi"}
        ],
        "formula": "木 (Mộc) ＋ 2 nét chấm hai bên",
        "strokeGuide": "Ngang trên ➔ 2 chấm trái phải ➔ ngang giữa ➔ sổ thẳng giữa ➔ phẩy trái ➔ mác phải.",
        "mnemonic": "Cây lúa trĩu bông mang mùa màng tương Lai (来) đến gần."
    },
    {
        "char": "年", "hv": "Niên", "lesson": "L18", "lessonName": "Bài 18", "strokes": 6,
        "meaning": "Năm tháng, tuổi tác, niên hạn", "kun": "とし", "on": "ねん",
        "examples": [
            {"word": "今年", "reading": "ことし", "vi": "Năm nay"},
            {"word": "来年", "reading": "らいねん", "vi": "Năm sau"},
            {"word": "去年", "reading": "きょねん", "vi": "Năm ngoái"},
            {"word": "年齢", "reading": "ねんれい", "vi": "Tuổi tác, niên kỷ"}
        ],
        "formula": "Phẩy ➔ ngang ➔ sổ ngắn ➔ ngang ➔ ngang dài ➔ sổ dài",
        "strokeGuide": "Phẩy trên ➔ ngang ➔ sổ ngắn ➔ ngang giữa ➔ ngang dài ➔ sổ thẳng đứng xuyên qua.",
        "mnemonic": "Bó lúa vàng gặt hái sau một Niên (年) năm ròng rã cần lao."
    },
    {
        "char": "去", "hv": "Khứ", "lesson": "L18", "lessonName": "Bài 18", "strokes": 5,
        "meaning": "Đã qua, rời đi, quá khứ", "kun": "さ-る", "on": "きょ、こ",
        "examples": [
            {"word": "去年", "reading": "きょねん", "vi": "Năm ngoái"},
            {"word": "過去", "reading": "かこ", "vi": "Quá khứ"},
            {"word": "去る", "reading": "さる", "vi": "Rời đi, lùi vào dĩ vãng"}
        ],
        "formula": "土 (Thổ) ＋ 厶 (Khư)",
        "strokeGuide": "Chữ Thổ (土 - 3 nét trên) ➔ bộ Khư (厶 - 2 nét dưới: gập chéo và chấm).",
        "mnemonic": "Vùi lấp xuống lòng đất (土) những gì đã qua trong quá Khứ (去)."
    },
    {
        "char": "家", "hv": "Gia", "lesson": "L18", "lessonName": "Bài 18", "strokes": 10,
        "meaning": "Ngôi nhà, gia đình, chuyên gia", "kun": "いえ、や", "on": "か、け",
        "examples": [
            {"word": "家", "reading": "いえ", "vi": "Ngôi nhà"},
            {"word": "家族", "reading": "かぞく", "vi": "Gia đình"},
            {"word": "家内", "reading": "かない", "vi": "Vợ tôi (nói khiêm tốn)"},
            {"word": "画家", "reading": "がか", "vi": "Họa sĩ"}
        ],
        "formula": "宀 (Miên - mái nhà) ＋ 豕 (Thỉ - con lợn)",
        "strokeGuide": "Bộ Miên (宀 - 3 nét nóc nhà) ➔ chữ Thỉ (豕 - 7 nét dưới: ngang, phẩy, cong móc, 4 phẩy nhỏ).",
        "mnemonic": "Dưới mái nhà (宀) chăn nuôi đàn lợn (豕) ấm cúng tổ ấm Gia (家) đình."
    },
    {
        "char": "思", "hv": "Tư", "lesson": "L18", "lessonName": "Bài 18", "strokes": 9,
        "meaning": "Suy nghĩ, ý nghĩ, hoài niệm", "kun": "おも-う", "on": "し",
        "examples": [
            {"word": "思います", "reading": "おもいます", "vi": "Suy nghĩ, cho là"},
            {"word": "思い出", "reading": "おもいで", "vi": "Kỷ niệm, hồi ức đẹp"},
            {"word": "思考", "reading": "しこう", "vi": "Tư duy, suy nghĩ"}
        ],
        "formula": "田 (Điền - ruộng) ＋ 心 (Tâm - trái tim)",
        "strokeGuide": "Chữ Điền (田 - 5 nét trên) ➔ bộ Tâm (心 - 4 nét dưới: chấm trái, nằm móc, 2 chấm trong).",
        "mnemonic": "Hình bóng đồng ruộng (田) quê hương luôn in đậm trong trái tim (心) người mang nỗi niềm Tư (思) hương."
    }
]

def main():
    with open("kanji_a2.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update kanjiData
    # Find the end of L11 in kanjiData: char: "願" ... }
    # Then append NEW_KANJI JSON
    new_kanji_js_items = []
    current_lesson = ""
    for item in NEW_KANJI:
        if item["lesson"] != current_lesson:
            current_lesson = item["lesson"]
            new_kanji_js_items.append(f"\n        // LESSON {current_lesson.replace('L', '')}: {item['lessonName'].upper()}")
        
        ex_str = ",\n                ".join(
            f'{{ word: "{ex["word"]}", reading: "{ex["reading"]}", vi: "{ex["vi"]}" }}'
            for ex in item["examples"]
        )
        item_str = f"""        {{
            char: "{item["char"]}", hv: "{item["hv"]}", lesson: "{item["lesson"]}", lessonName: "{item["lessonName"]}", strokes: {item["strokes"]},
            meaning: "{item["meaning"]}", kun: "{item["kun"]}", on: "{item["on"]}",
            examples: [
                {ex_str}
            ],
            formula: "{item["formula"]}",
            strokeGuide: "{item["strokeGuide"]}",
            mnemonic: "{item["mnemonic"]}"
        }}"""
        new_kanji_js_items.append(item_str)

    new_kanji_js = ",\n" + ",\n".join(new_kanji_js_items)

    # Insert before "    ];\n\n    let filteredKanji = [];"
    target_split = "    ];\n\n    let filteredKanji = [];"
    if target_split in html:
        html = html.replace(target_split, new_kanji_js + "\n    ];\n\n    let filteredKanji = [];")
        print("Inserted new Kanji items successfully into kanjiData!")
    else:
        print("ERROR: target_split not found!")
        return

    # 2. Update KANJI_LESSON_ORDER
    old_order = "const KANJI_LESSON_ORDER = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11'];"
    new_order = "const KANJI_LESSON_ORDER = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18'];"
    html = html.replace(old_order, new_order)

    # 3. Update KANJI_LESSON_TITLES
    old_titles = "'L11': 'Bài 11: Ẩm thực & Quán ăn'\n    };"
    new_titles = """'L11': 'Bài 11: Ẩm thực & Quán ăn',
        'L12': 'Bài 12: Món ăn & Hương vị',
        'L13': 'Bài 13: Lịch trình công tác',
        'L14': 'Bài 14: Nơi làm việc & Xin phép',
        'L15': 'Bài 15: Cơ thể & Bệnh tật',
        'L16': 'Bài 16: Giữ gìn sức khỏe',
        'L17': 'Bài 17: Quà tặng & Kỷ niệm',
        'L18': 'Bài 18: Lễ hội & Trang phục'
    };"""
    html = html.replace(old_titles, new_titles)

    # 4. Update selectPreset in JS
    old_preset_code = """        } else if (type === 'L10_11') {
            ['L10', 'L11'].forEach(l => selectedLessons.add(l));
        } else if (type === 'L11') {
            selectedLessons.add('L11');"""

    new_preset_code = """        } else if (type === 'L10_11') {
            ['L10', 'L11'].forEach(l => selectedLessons.add(l));
        } else if (type === 'L11_18') {
            ['L11', 'L12', 'L13', 'L14', 'L15', 'L16', 'L17', 'L18'].forEach(l => selectedLessons.add(l));
        } else if (type === 'L11') {
            selectedLessons.add('L11');"""
    html = html.replace(old_preset_code, new_preset_code)

    # 5. Update HTML Presets
    old_presets_html = """                <div class="quick-presets">
                    <button class="preset-pill active" id="preset-all" onclick="selectPreset('ALL')">🌟 Tất cả (1-11)</button>
                    <button class="preset-pill" id="preset-l1-5" onclick="selectPreset('L1_5')">Bài 1-5</button>
                    <button class="preset-pill" id="preset-l6-10" onclick="selectPreset('L6_10')">Bài 6-10</button>
                    <button class="preset-pill" id="preset-l10-11" onclick="selectPreset('L10_11')">Bài 10-11 (Mới ✨)</button>
                    <button class="preset-pill preset-clear" id="preset-none" onclick="selectPreset('NONE')">Bỏ chọn</button>
                </div>"""

    new_presets_html = """                <div class="quick-presets">
                    <button class="preset-pill active" id="preset-all" onclick="selectPreset('ALL')">🌟 Tất cả (1-18)</button>
                    <button class="preset-pill" id="preset-l1-5" onclick="selectPreset('L1_5')">Bài 1-5</button>
                    <button class="preset-pill" id="preset-l6-10" onclick="selectPreset('L6_10')">Bài 6-10</button>
                    <button class="preset-pill" id="preset-l11-18" onclick="selectPreset('L11_18')">Bài 11-18 (Mới ✨)</button>
                    <button class="preset-pill preset-clear" id="preset-none" onclick="selectPreset('NONE')">Bỏ chọn</button>
                </div>"""
    html = html.replace(old_presets_html, new_presets_html)

    # Update title in picker
    html = html.replace("DANH SÁCH BÀI HỌC (1-11):", "DANH SÁCH BÀI HỌC (1-18):")
    html = html.replace("Đang chọn: Tất cả 11 bài (86 chữ Hán)", "Đang chọn: Tất cả 18 bài (144 chữ Hán)")

    # 6. Update Dock Pills in kanji_a2.html
    old_pills = """            <a href="Marugoto_A2_Lesson_10.html" class="dock-pill" data-lesson="10"><span class="pill-ico">🌟</span> Bài 10 (Chuyên Sâu)</a>
            <a href="Marugoto_A2_Lesson_11.html" class="dock-pill" data-lesson="11"><span class="pill-ico">🍱</span> Bài 11 (Chuyên Sâu)</a>"""

    new_pills = """            <a href="Marugoto_A2_Lesson_10.html" class="dock-pill" data-lesson="10"><span class="pill-ico">🌟</span> Bài 10</a>
            <a href="Marugoto_A2_Lesson_11.html" class="dock-pill" data-lesson="11"><span class="pill-ico">🍱</span> Bài 11</a>
            <a href="Marugoto_A2_Lesson_12.html" class="dock-pill" data-lesson="12"><span class="pill-ico">🍜</span> Bài 12</a>
            <a href="Marugoto_A2_Lesson_13.html" class="dock-pill" data-lesson="13"><span class="pill-ico">✈️</span> Bài 13</a>
            <a href="Marugoto_A2_Lesson_14.html" class="dock-pill" data-lesson="14"><span class="pill-ico">💻</span> Bài 14</a>
            <a href="Marugoto_A2_Lesson_15.html" class="dock-pill" data-lesson="15"><span class="pill-ico">🏥</span> Bài 15</a>
            <a href="Marugoto_A2_Lesson_16.html" class="dock-pill" data-lesson="16"><span class="pill-ico">🏃</span> Bài 16</a>
            <a href="Marugoto_A2_Lesson_17.html" class="dock-pill" data-lesson="17"><span class="pill-ico">🎁</span> Bài 17</a>
            <a href="Marugoto_A2_Lesson_18.html" class="dock-pill" data-lesson="18"><span class="pill-ico">👘</span> Bài 18</a>"""
    html = html.replace(old_pills, new_pills)

    # 7. Update Tools Menu in kanji_a2.html
    old_tool_item = '<a href="Marugoto_A2_Lesson_11.html" class="dock-tool-item">🍱 Web Chuyên Sâu Bài 11 ✨</a>'
    new_tools = """<a href="Marugoto_A2_Lesson_11.html" class="dock-tool-item">🍱 Web Chuyên Sâu Bài 11 ✨</a>
                    <a href="Marugoto_A2_Lesson_12.html" class="dock-tool-item">🍜 Web Chuyên Sâu Bài 12 ✨</a>
                    <a href="Marugoto_A2_Lesson_13.html" class="dock-tool-item">✈️ Web Chuyên Sâu Bài 13 ✨</a>
                    <a href="Marugoto_A2_Lesson_14.html" class="dock-tool-item">💻 Web Chuyên Sâu Bài 14 ✨</a>
                    <a href="Marugoto_A2_Lesson_15.html" class="dock-tool-item">🏥 Web Chuyên Sâu Bài 15 ✨</a>
                    <a href="Marugoto_A2_Lesson_16.html" class="dock-tool-item">🏃 Web Chuyên Sâu Bài 16 ✨</a>
                    <a href="Marugoto_A2_Lesson_17.html" class="dock-tool-item">🎁 Web Chuyên Sâu Bài 17 ✨</a>
                    <a href="Marugoto_A2_Lesson_18.html" class="dock-tool-item">👘 Web Chuyên Sâu Bài 18 ✨</a>"""
    html = html.replace(old_tool_item, new_tools)

    with open("kanji_a2.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("kanji_a2.html updated successfully!")

if __name__ == "__main__":
    main()
