# -*- coding: utf-8 -*-
"""
master_grammar_data.py
Comprehensive database of all grammar points across 26 lessons of Marugoto:
- Marugoto Starter A1: Lessons 11 to 18
- Marugoto Elementary 1 A2-1: Lessons 1 to 10
- Marugoto Elementary 2 A2-2: Lessons 11 to 18
"""

ALL_GRAMMAR_ITEMS = [
    # =========================================================================
    # MARUGOTO A1: BÀI 11 ĐẾN BÀI 18 (SƠ CẤP)
    # =========================================================================
    {
        "id": 1,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 11,
        "lessonTitle": "Bài 11: Sở Thích & Khả Năng (A1)",
        "title": "Bày tỏ sở thích: ～が 好きです / 好きじゃないです",
        "tag": "Sở thích",
        "cat": "hobby",
        "formula": "N が 好きです (Thích N)<br>N が 大好きです (Rất thích N)<br>N は 好きじゃないです (Không thích N)",
        "meaning": "Dùng để nói về sở thích cá nhân hoặc hỏi đối phương thích cái gì / thể loại nào (どんな N が 好きですか).",
        "notes": "Trợ từ đi kèm trước 好き (Tính từ đuôi な) là 「が」. Khi nhấn mạnh hoặc phủ định có thể thay bằng 「は」. Để hỏi loại yêu thích: 「どんな N が 好きですか」.",
        "examples": [
            {"jp": "わたしは 読書が 好きです。", "vi": "Tôi thích đọc sách."},
            {"jp": "どんな 映画が 好きですか。―― アクション映画が 好きです。", "vi": "Bạn thích thể loại phim nào? ―― Tôi thích phim hành động."},
            {"jp": "ホラー映画は 好きじゃないです。", "vi": "Phim kinh dị thì tôi không thích lắm."}
        ],
        "quiz": {
            "q": "どんな スポーツ [____] 好きですか。",
            "options": ["が", "を", "で", "に"],
            "correct": 0,
            "explain": "Đi trước tính từ 「好き」 để chỉ đối tượng được yêu thích luôn dùng trợ từ 「が」."
        }
    },
    {
        "id": 2,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 11,
        "lessonTitle": "Bài 11: Sở Thích & Khả Năng (A1)",
        "title": "Bày tỏ khả năng: ～が できます / できません",
        "tag": "Khả năng",
        "cat": "ability",
        "formula": "N (Môn thể thao / Nhạc cụ / Ngôn ngữ) が できます<br>N は できません (Không thể)",
        "meaning": "Dùng để nói mình có thể chơi được môn thể thao nào, sử dụng được ngoại ngữ nào hoặc chơi được loại nhạc cụ nào.",
        "notes": "Chỉ dùng với danh từ chỉ kỹ năng, ngôn ngữ hoặc môn thể thao (テニス, ピアノ, 日本語, 料理...).",
        "examples": [
            {"jp": "わたしは テニスが できます。", "vi": "Tôi có thể chơi quần vợt (tennis)."},
            {"jp": "韓国語が 少し できます。", "vi": "Tôi có thể nói được một chút tiếng Hàn."},
            {"jp": "ピアノは できませんが、ギターが できます。", "vi": "Piano thì tôi không chơi được nhưng guitar thì tôi biết chơi."}
        ],
        "quiz": {
            "q": "アリさんは ギター [____] できますか。",
            "options": ["が", "を", "に", "で"],
            "correct": 0,
            "explain": "Cấu trúc khả năng với danh từ: 「N が できます」."
        }
    },
    {
        "id": 3,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 11,
        "lessonTitle": "Bài 11: Sở Thích & Khả Năng (A1)",
        "title": "Địa điểm diễn ra hành động & Tần suất: N(Địa điểm) で Vます / よく・ときどき",
        "tag": "Địa điểm & Tần suất",
        "cat": "habit",
        "formula": "N(Địa điểm) で Vます<br>Phó từ: よく (Thường xuyên) / ときどき (Thỉnh thoảng) + Vます<br>あまり (Không hay...) / ぜんぜん (Hoàn toàn không...) + Vません",
        "meaning": "Chỉ nơi chốn diễn ra hành động và mức độ thường xuyên thực hiện hành động đó.",
        "notes": "Phó từ 「あまり」 và 「ぜんぜん」 bắt buộc phải đi với đuôi phủ định 「～ません」.",
        "examples": [
            {"jp": "うちで 本を 読みます。", "vi": "Tôi đọc sách tại nhà."},
            {"jp": "休みの日に よく 公園で 写真を 撮ります。", "vi": "Vào ngày nghỉ tôi thường chụp ảnh ở công viên."},
            {"jp": "お酒は あまり 飲みません。", "vi": "Rượu bia thì tôi không hay uống lắm."}
        ],
        "quiz": {
            "q": "わたしは ぜんぜん 映画を [____]。",
            "options": ["見ません", "見ます", "見ました", "見ています"],
            "correct": 0,
            "explain": "Phó từ 「ぜんぜん」 (hoàn toàn không) luôn đi với thể phủ định: 「見ません」."
        }
    },

    # A1 LESSON 12
    {
        "id": 4,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 12,
        "lessonTitle": "Bài 12: Sự Kiện & Lời Rủ Rê (A1)",
        "title": "Thời gian & Địa điểm có sự kiện: ～に / ～で [Sự kiện] が あります",
        "tag": "Sự kiện",
        "cat": "event",
        "formula": "[Thời gian] に [Sự kiện] が あります (Có sự kiện vào lúc...)<br>[Địa điểm] で [Sự kiện] が あります (Có sự kiện diễn ra tại...)",
        "meaning": "Dùng để thông báo lịch trình tổ chức lễ hội, buổi hòa nhạc, hội thảo, triển lãm.",
        "notes": "Phân biệt trợ từ: Thời gian dùng 「に」; Nơi chốn diễn ra sự kiện dùng 「で」 (không dùng に). Các từ chỉ thời gian tương đối như 今日, あした, らいしゅう không thêm に.",
        "examples": [
            {"jp": "土曜日に コンサートが あります。", "vi": "Vào thứ bảy sẽ có một buổi hòa nhạc."},
            {"jp": "国際ホールで 映画が あります。", "vi": "Tại Hội trường Quốc tế sẽ có buổi chiếu phim."},
            {"jp": "明日 公園で お祭りが あります。", "vi": "Ngày mai ở công viên sẽ có lễ hội."}
        ],
        "quiz": {
            "q": "市民ホール [____] コンサートが あります。",
            "options": ["で", "に", "を", "へ"],
            "correct": 0,
            "explain": "Nơi chốn tổ chức sự kiện/hoạt động dùng trợ từ 「で」."
        }
    },
    {
        "id": 5,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 12,
        "lessonTitle": "Bài 12: Sự Kiện & Lời Rủ Rê (A1)",
        "title": "Đi để làm gì & Rủ rê: V(bỏ ます) に 行きます / V-ませんか / V-ましょう",
        "tag": "Mục đích & Rủ rê",
        "cat": "invitation",
        "formula": "[Địa điểm] へ [Sự kiện / V(bỏ ます)] に 行きます (Đi để làm gì)<br>いっしょに V-ませんか (Bạn có muốn cùng làm... với tôi không?)<br>V-ましょう (Chúng ta cùng làm... nhé!)",
        "meaning": "Chỉ mục đích đi tới đâu, đồng thời rủ rê người khác tham gia cùng mình một cách lịch sự.",
        "notes": "「～ませんか」 là lời mời mở, thể hiện sự tôn trọng đối phương. Người nghe nếu đồng ý thường đáp: 「いいですね。～ましょう」.",
        "examples": [
            {"jp": "わたしは 盆栽展を 見に 行きます。", "vi": "Tôi đi xem triển lãm cây cảnh Bonsai."},
            {"jp": "あした 一緒に 映画を 見に 行きませんか。―― いいですね。行きましょう！", "vi": "Ngày mai bạn cùng tôi đi xem phim nhé? ―― Ý hay đấy, đi thôi!"},
            {"jp": "ちょっと 休みましょう。", "vi": "Chúng ta cùng nghỉ ngơi một chút nhé."}
        ],
        "quiz": {
            "q": "美術館へ 絵を [____] に 行きます。",
            "options": ["見", "見て", "見ます", "見る"],
            "correct": 0,
            "explain": "Động từ chỉ mục đích trước 「に行きます」 phải bỏ ます: 見ます ➔ 「見に行きます」."
        }
    },

    # A1 LESSON 13
    {
        "id": 6,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 13,
        "lessonTitle": "Bài 13: Đi Lại & Phương Tiện (A1)",
        "title": "Chặng đường di chuyển: [Từ] から [Đến] まで [Phương tiện] で 行きます",
        "tag": "Đi lại & Di chuyển",
        "cat": "transport",
        "formula": "[Nơi xuất phát] から [Nơi đến] まで [Phương tiện] で 行きます / 来ます<br>[Phương tiện] に 乗ります (Lên xe) / を 降ります (Xuống xe)",
        "meaning": "Diễn tả hành trình từ điểm khởi hành tới đích đến và phương tiện giao thông sử dụng.",
        "notes": "Đi bộ thì dùng 「歩いて (あるいて)」 và không thêm trợ từ で. Lên tàu xe dùng 「に 乗る」, xuống tàu xe dùng 「を 降りる」.",
        "examples": [
            {"jp": "うちから 駅まで バスで 行きます。", "vi": "Từ nhà đến nhà ga tôi đi bằng xe buýt."},
            {"jp": "東京から 京都まで 新幹線で 行きます。", "vi": "Từ Tokyo đến Kyoto tôi đi bằng tàu Shinkansen."},
            {"jp": "駅で 電車に 乗ります。次の駅で 電車を 降ります。", "vi": "Lên tàu điện ở nhà ga. Xuống tàu ở ga tiếp theo."}
        ],
        "quiz": {
            "q": "新宿駅で 電車 [____] 降ります。",
            "options": ["を", "に", "で", "から"],
            "correct": 0,
            "explain": "Rời khỏi/xuống phương tiện giao thông dùng trợ từ 「を」: 「電車を降ります」."
        }
    },

    # A1 LESSON 14
    {
        "id": 7,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 14,
        "lessonTitle": "Bài 14: Thị Trấn & Vị Trí Địa Lý (A1)",
        "title": "Vị trí & Sự tồn tại: [Địa điểm] に N が あります/います / [Vị trí] に あります",
        "tag": "Vị trí & Nơi chốn",
        "cat": "location",
        "formula": "[Địa điểm] に N が あります (Đồ vật/công trình)<br>[Địa điểm] に N が います (Người/động vật)<br>N1 は N2 の [前/後ろ/中/隣/近く] に あります",
        "meaning": "Xác định nơi chốn tồn tại của người hoặc vật, vị trí tương đối giữa các công trình.",
        "notes": "Đồ vật không tự chuyển động (nhà, cây cối, xe) dùng 「あります」. Người và động vật sống dùng 「います」.",
        "examples": [
            {"jp": "公園に きれいな 花が あります。", "vi": "Trong công viên có những bông hoa đẹp."},
            {"jp": "ロビーに 案内人が います。", "vi": "Ở sảnh chờ có người hướng dẫn."},
            {"jp": "銀行は デパートの 隣に あります。", "vi": "Ngân hàng nằm ở ngay bên cạnh trung tâm thương mại."}
        ],
        "quiz": {
            "q": "あそこに 犬が [____]。",
            "options": ["います", "あります", "します", "行きます"],
            "correct": 0,
            "explain": "Động vật sống (chó 犬) dùng động từ tồn tại là 「います」."
        }
    },

    # A1 LESSON 15
    {
        "id": 8,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 15,
        "lessonTitle": "Bài 15: Mong Muốn & Tặng Quà (A1)",
        "title": "Muốn có đồ vật & Cho - Nhận: ～が ほしいです / あげます / もらいました",
        "tag": "Mong muốn & Tặng quà",
        "cat": "gift",
        "formula": "N が ほしいです (Tôi muốn có N)<br>N1(người nhận) に N2(vật) を あげます (Tặng cho ai cái gì)<br>N1(người tặng) に N2(vật) を もらいました (Nhận từ ai cái gì)",
        "meaning": "Bày tỏ mong muốn sở hữu đồ vật và cách nói về hành động tặng quà, nhận quà giữa người với người.",
        "notes": "ほしい chỉ dùng cho ngôi thứ nhất (tôi muốn). Đi trước ほしい luôn dùng trợ từ 「が」.",
        "examples": [
            {"jp": "わたしは 新しい スマホが ほしいです。", "vi": "Tôi muốn có một chiếc điện thoại thông minh mới."},
            {"jp": "カーラさんに 花を あげます。", "vi": "Tôi tặng hoa cho Carla."},
            {"jp": "誕生日に 友達に 時計を もらいました。", "vi": "Vào ngày sinh nhật tôi đã nhận được chiếc đồng hồ từ bạn tôi."}
        ],
        "quiz": {
            "q": "誕生日に 父 [____] カメラを もらいました。",
            "options": ["に", "を", "で", "へ"],
            "correct": 0,
            "explain": "Nhận quà từ ai: [Người tặng] + に もらいました."
        }
    },

    # A1 LESSON 16
    {
        "id": 9,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 16,
        "lessonTitle": "Bài 16: Mua Sắm & Giá Cả (A1)",
        "title": "Mua sắm & Quá khứ: V-ました / ～は いくらですか / これを ください",
        "tag": "Mua sắm & Giá cả",
        "cat": "shopping",
        "formula": "V-ました (Đã làm...) / V-ませんでした (Đã không làm...)<br>N は いくらですか ―― [Số tiền] 円です<br>N を ください (Xin hãy lấy cho tôi N) / N に します (Tôi chọn N)",
        "meaning": "Hỏi giá cả, đưa ra yêu cầu mua sắm tại quầy hàng và diễn tả hành vi mua bán trong quá khứ.",
        "notes": "Khi chọn món trong menu hoặc chọn sản phẩm mua: 「これに します」 (Tôi chốt lấy cái này).",
        "examples": [
            {"jp": "去年 日本で かわいい 服を 買いました。", "vi": "Năm ngoái tôi đã mua quần áo đáng yêu tại Nhật."},
            {"jp": "すみません、この 傘は いくらですか。―― 1,500円です。", "vi": "Xin lỗi, chiếc ô này giá bao nhiêu? ―― Dạ 1.500 Yên ạ."},
            {"jp": "この シャツを ください。", "vi": "Xin hãy lấy cho tôi chiếc áo sơ mi này."}
        ],
        "quiz": {
            "q": "きのう デパートで 靴を [____]。",
            "options": ["買いました", "買います", "買う", "買って"],
            "correct": 0,
            "explain": "Hành động đã hoàn thành trong quá khứ (きのう - hôm qua) chia về 「V-ました」."
        }
    },

    # A1 LESSON 17 & 18
    {
        "id": 10,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 17,
        "lessonTitle": "Bài 17: Tính Từ Quá Khứ & Thể Te (A1)",
        "title": "Tính từ quá khứ & Nối hành động: A-かったです / Na-でした / V1-て V2-ます",
        "tag": "Quá khứ & Thể Te",
        "cat": "te_form",
        "formula": "Tính từ đuôi い: Bỏ い + かったです (Đã...) / くなかったです (Đã không...)<br>Tính từ đuôi な / Danh từ: + でした / じゃありませんでした<br>V1-て、V2-ます (Làm V1 rồi làm V2 theo chuỗi thời gian)",
        "meaning": "Kể lại cảm nhận, trạng thái của sự việc đã qua và liên kết chuỗi hành động diễn ra theo trình tự thời gian.",
        "notes": "いい ➔ Quá khứ là 「よかったです」 (Bất quy tắc). Chuỗi hành động thể Te luôn tuân theo thứ tự trước sau.",
        "examples": [
            {"jp": "昨日の 旅行は とても 楽しかったです。", "vi": "Chuyến du lịch hôm qua đã rất là vui."},
            {"jp": "京都は 静かでした。", "vi": "Kyoto đã rất yên tĩnh."},
            {"jp": "朝 起きて、顔を 洗って、朝ごはんを 食べます。", "vi": "Buổi sáng thức dậy, rửa mặt rồi ăn bữa sáng."}
        ],
        "quiz": {
            "q": "きのうの 天気は とても [____] です (いい)。",
            "options": ["よかった", "いいかった", "いくなかった", "よいでした"],
            "correct": 0,
            "explain": "Tính từ 「いい」 chia quá khứ bất quy tắc là 「よかったです」."
        }
    },
    {
        "id": 11,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 18,
        "lessonTitle": "Bài 18: Trải Nghiệm Hoàn Thành (A1)",
        "title": "Đã làm / Chưa làm: もう V-ました / まだ V-ていません",
        "tag": "Hoàn tất hành động",
        "cat": "experience",
        "formula": "もう V-ました (Đã làm... rồi)<br>まだ V-ていません (Vẫn chưa làm...)<br>いいえ、まだです (Chưa, tôi vẫn chưa)",
        "meaning": "Dùng để hỏi hoặc trả lời một hành động dự định đã được thực hiện hay vẫn chưa.",
        "notes": "Khi trả lời phủ định cho câu hỏi 「もう～ましたか」, không dùng V-ませんでした mà phải dùng 「いいえ、まだです」 hoặc 「まだ V-ていません」.",
        "examples": [
            {"jp": "もう 東京タワーを 見ましたか。―― はい、もう 見ました。", "vi": "Bạn đã ngắm tháp Tokyo chưa? ―― Vâng, tôi đã ngắm rồi."},
            {"jp": "富士山は まだ 見ていません。", "vi": "Núi Phú Sĩ thì tôi vẫn chưa ngắm được."},
            {"jp": "もう 昼ごはんを 食べましたか。―― いいえ、まだです。", "vi": "Bạn đã ăn trưa chưa? ―― Dạ chưa, tôi vẫn chưa ăn."}
        ],
        "quiz": {
            "q": "「もう 宿題を しましたか。」――「いいえ、[____]。」",
            "options": ["まだです", "しませんでした", "もうです", "しません"],
            "correct": 0,
            "explain": "Đáp lại câu hỏi 「もう～ましたか」 ở dạng phủ định chuẩn ngữ pháp là 「いいえ、まだです」."
        }
    },

    # =========================================================================
    # MARUGOTO A2-1: BÀI 1 ĐẾN BÀI 10 (TRUNG CẤP 1)
    # =========================================================================
    {
        "id": 12,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 1,
        "lessonTitle": "Bài 1: Nơi Ở & Gia Đình",
        "title": "Trạng thái tiếp diễn & Nghề nghiệp: V-ています / に住んでいます / で働いています",
        "tag": "Tiếp diễn & Nơi chốn",
        "cat": "habit",
        "formula": "V-て + います (Duy trì thói quen / Trạng thái kết quả kéo dài)<br>[Nơi ở] に 住んでいます (Đang sống tại...)<br>[Nơi làm việc] で 働いています (Đang làm việc tại...)",
        "meaning": "Diễn tả nơi chốn cư trú hiện tại, công việc nghề nghiệp đang làm hoặc thói quen duy trì hàng ngày.",
        "notes": "Sống ở đâu dùng trợ từ 「に」 (kết quả nơi chốn); Làm việc ở đâu dùng trợ từ 「で」 (nơi diễn ra hành động).",
        "examples": [
            {"jp": "わたしは 東京に 住んでいます。", "vi": "Tôi hiện đang sống ở Tokyo."},
            {"jp": "父は 電車の会社で 働いています。", "vi": "Bố tôi đang làm việc tại một công ty đường sắt."},
            {"jp": "毎週水曜日に 友達に 英語を 教えています。", "vi": "Tôi dạy tiếng Anh cho bạn vào mỗi thứ Tư."}
        ],
        "quiz": {
            "q": "わたしは ホテル [____] 働いています。",
            "options": ["で", "に", "を", "へ"],
            "correct": 0,
            "explain": "Nơi làm việc diễn ra hành động lao động đi với trợ từ 「で」: 「ホテルで働いています」."
        }
    },
    {
        "id": 13,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 2,
        "lessonTitle": "Bài 2: Sở Thích & Thời Điểm",
        "title": "Danh từ hóa sở thích & Mệnh đề thời điểm: V-る こと / ～のとき / V-るとき",
        "tag": "Sở thích & Thời điểm",
        "cat": "hobby",
        "formula": "私の趣味は [V thể Từ điển (RU)] ことです (Sở thích là việc...)<br>N の とき / A-い とき / Na-な とき / V-る とき (Khi...)",
        "meaning": "Biến động từ thành danh từ để nói về sở thích, và xác định mốc thời gian khi còn nhỏ, khi rảnh rỗi hoặc khi làm gì.",
        "notes": "Danh từ đi với とき phải có 「の」 (子供のとき, 暇なとき, 若いとき).",
        "examples": [
            {"jp": "私の 趣味は クラシック音楽を 聴くことです。", "vi": "Sở thích của tôi là nghe nhạc cổ điển."},
            {"jp": "子供のとき、よく アニメを 見ました。", "vi": "Khi còn nhỏ, tôi rất hay xem phim hoạt hình."},
            {"jp": "暇なとき、料理を 作ります。", "vi": "Những khi rảnh rỗi, tôi thường tự nấu ăn."}
        ],
        "quiz": {
            "q": "学生 [____] とき、よく 旅行しました。",
            "options": ["の", "な", "に", "で"],
            "correct": 0,
            "explain": "Danh từ khi bổ nghĩa cho 「とき」 phải có trợ từ 「の」: 「学生のとき」."
        }
    },
    {
        "id": 14,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 3,
        "lessonTitle": "Bài 3: Mùa & Thay Đổi Trạng Thái",
        "title": "Thay đổi trạng thái & Lý do: ～くなる / ～になる / V-るのが好き / ～から",
        "tag": "Trạng thái & Lý do",
        "cat": "change",
        "formula": "Tính từ đuôi い: Bỏ い + くなります (Trở nên...)<br>Tính từ đuôi な / Danh từ: + になります (Trở thành...)<br>V-る / A-い のが 好きです (Thích điều gì - danh từ hóa bằng の)<br>S1 から、S2 (Vì S1 nên S2)",
        "meaning": "Miêu tả sự biến đổi tự nhiên của thời tiết, khí hậu và đưa ra lý do giải thích nguyên nhân.",
        "notes": "Phân biệt くなる (tính từ đuôi い: あたたかくなる) và になる (danh từ/đuôi な: 春になる).",
        "examples": [
            {"jp": "3月ごろ、だんだん 暖かく なります。", "vi": "Khoảng tháng 3, thời tiết dần dần trở nên ấm áp."},
            {"jp": "秋が 好きです。涼しいのが 好きですから。", "vi": "Tôi thích mùa thu. Vì tôi thích sự mát mẻ."},
            {"jp": "スキーが できますから、冬が 一番 好きです。", "vi": "Vì có thể trượt tuyết nên tôi thích mùa đông nhất."}
        ],
        "quiz": {
            "q": "春になると、花が [____] なります (きれい)。",
            "options": ["きれいに", "きれいく", "きれいだ", "きれいで"],
            "correct": 0,
            "explain": "Tính từ đuôi な biến đổi với なる thành 「Na + になります」: 「きれいになります」."
        }
    },
    {
        "id": 15,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 4,
        "lessonTitle": "Bài 4: Dự Báo Thời Tiết",
        "title": "Phán đoán khả năng: ～でしょう (Chắc là) / ～かもしれません (Có lẽ)",
        "tag": "Phán đoán",
        "cat": "weather",
        "formula": "Thể thông thường (Bỏ だ với N/Na) + でしょう (Xác suất cao ~80%)<br>Thể thông thường (Bỏ だ với N/Na) + かもしれません (Xác suất ~50%)",
        "meaning": "Đưa ra phán đoán, dự báo về thời tiết hoặc sự việc tương lai dựa trên thông tin quan sát được.",
        "notes": "Trong bản tin thời tiết thường dùng 「でしょう」. Danh từ và tính từ đuôi な bỏ だ rồi ghép trực tiếp (雨でしょう, 雨かもしれません).",
        "examples": [
            {"jp": "明日は 晴れでしょう。", "vi": "Ngày mai chắc là trời sẽ nắng ráo."},
            {"jp": "午後は 雨が 降るかもしれません。", "vi": "Buổi chiều có thể trời sẽ đổ mưa."},
            {"jp": "今夜は 寒くなるかもしれませんから、コートを 着てください。", "vi": "Tối nay có lẽ trời sẽ trở lạnh đấy, bạn hãy mặc áo khoác vào nhé."}
        ],
        "quiz": {
            "q": "明日は 雪が [____] かもしれません。",
            "options": ["降る", "降ります", "降って", "降り"],
            "correct": 0,
            "explain": "Trước 「かもしれません」 là động từ thể thông thường (thể từ điển): 「降る」."
        }
    },
    {
        "id": 16,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 5,
        "lessonTitle": "Bài 5: Thị Trấn & Nơi Chốn",
        "title": "Nối tính từ đa tầng & Quan hệ tương phản: A-くて / Na-で / ～けど・～が",
        "tag": "Miêu tả & Tương phản",
        "cat": "description",
        "formula": "Tính từ đuôi い: Bỏ い + くて<br>Tính từ đuôi な: Bỏ な + で<br>Mệnh đề 1 + けど / が、Mệnh đề 2 (Tuy... nhưng...)",
        "meaning": "Ghép nhiều đặc điểm phong cảnh, kiến trúc vào một câu và diễn tả sự đối lập nhẹ nhàng.",
        "notes": "「けど」 thường dùng trong văn nói thân mật; 「が」 dùng trong văn viết hoặc giao tiếp lịch sự.",
        "examples": [
            {"jp": "この 公園は 広くて、きれいです。", "vi": "Công viên này vừa rộng lớn lại vừa đẹp đẽ."},
            {"jp": "この 町は 静かで、住みやすいです。", "vi": "Thị trấn này yên bình và rất đáng sống."},
            {"jp": "この アパートは 駅から 近いけど、家賃が 高いです。", "vi": "Căn hộ này tuy gần nhà ga nhưng tiền thuê lại đắt."}
        ],
        "quiz": {
            "q": "この町は にぎやか [____]、ちょっと 危ないです。",
            "options": ["だけど", "くて", "な", "で"],
            "correct": 0,
            "explain": "Tính từ đuôi な khi nối với mệnh đề tương phản 「けど」 ở văn nói dùng 「だけど」."
        }
    },
    {
        "id": 17,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 6,
        "lessonTitle": "Bài 6: Chỉ Đường & Xác Nhận",
        "title": "Chỉ đường & Phủ định thông tin: V-て (Chỉ dẫn) / N1 じゃなくて N2 / V-たいんですが",
        "tag": "Chỉ đường & Yêu cầu",
        "cat": "direction",
        "formula": "まっすぐ 行って、[Địa điểm] を 右/左に 曲がってください (Đi thẳng rồi rẽ...)<br>N1 じゃなくて、N2 です (Không phải N1 mà là N2)<br>[Địa điểm] に 行きたいんですが... (Tôi muốn đi tới... mở lời hỏi đường)",
        "meaning": "Hướng dẫn lộ trình di chuyển, đính chính thông tin hiểu nhầm và mở lời hỏi đường tế nhị.",
        "notes": "Đuôi 「～んですが」 dùng để tạo cớ, mở lời gợi mở để đối phương sẵn lòng hướng dẫn mình.",
        "examples": [
            {"jp": "二つ目の 角を 右に 曲がってください。", "vi": "Xin hãy rẽ phải ở góc ngã rẽ thứ hai."},
            {"jp": "一つ目 じゃなくて、二つ目ですよ。", "vi": "Không phải ngã rẽ thứ nhất đâu, mà là cái thứ hai đấy."},
            {"jp": "すみません。博物館に 行きたいんですが、どこですか。", "vi": "Xin lỗi. Tôi muốn đến viện bảo tàng, nó nằm ở đâu vậy ạ?"}
        ],
        "quiz": {
            "q": "交差点を 左 [____] 曲がってください。",
            "options": ["に", "を", "で", "へ"],
            "correct": 0,
            "explain": "Rẽ sang hướng nào dùng trợ từ 「に」: 「左に曲がってください」."
        }
    },
    {
        "id": 18,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 7,
        "lessonTitle": "Bài 7: Hẹn Giờ & Xin Lỗi Muộn",
        "title": "Hẹn giờ & Lý do muộn: N で(も) いいですか / N で / V-て すみません",
        "tag": "Hẹn gặp & Xin lỗi",
        "cat": "appointment",
        "formula": "[Thời gian] で(も) いいですか (Mấy giờ có được không?)<br>N で / V-て、遅くなって すみません (Vì... nên tôi đến muộn xin lỗi)",
        "meaning": "Thương lượng điều chỉnh giờ hẹn và giải thích lý do đến muộn (tắc đường, lạc đường, tàu trễ).",
        "notes": "Cấu trúc xin lỗi vì sự bất tiện: 「V-て + すみません」 (Ví dụ: 道に迷ってすみません).",
        "examples": [
            {"jp": "10時半でも いいですか。―― ええ、大丈夫ですよ。", "vi": "10 giờ rưỡi có được không? ―― Vâng, hoàn toàn được ạ."},
            {"jp": "遅くなって すみません。道に 迷って...", "vi": "Xin lỗi vì tôi đến muộn. Tại tôi bị lạc đường..."},
            {"jp": "大雨で 電車が 止まって しまいました。", "vi": "Vì mưa to dữ dội nên tàu điện đã bị dừng mất."}
        ],
        "quiz": {
            "q": "渋滞 [____] 遅くなって すみません。",
            "options": ["で", "に", "を", "から"],
            "correct": 0,
            "explain": "Danh từ chỉ nguyên nhân sự cố (渋滞 - tắc đường) đi với trợ từ 「で」."
        }
    },
    {
        "id": 19,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 8,
        "lessonTitle": "Bài 8: Bữa Ăn & Thứ Tự Trước Sau",
        "title": "Mời mọc & Thứ tự hành động: V-に行きませんか / V-た後で / V-る前に",
        "tag": "Thời gian & Lời mời",
        "cat": "order",
        "formula": "[Địa điểm] を 見に 行きませんか (Cùng đi ngắm... không?)<br>V-た 後で、～ (Sau khi đã làm... thì...)<br>N の 前に / V-る 前に、～ (Trước khi làm... thì...)",
        "meaning": "Rủ bạn bè đi thăm thú danh lam thắng cảnh và sắp xếp thứ tự thực hiện các hành động trong ngày.",
        "notes": "Sau khi thì dùng thể Quá khứ 「V-た 後で」; Trước khi thì dùng thể Từ điển 「V-る 前に」.",
        "examples": [
            {"jp": "夜景を 見に 行きませんか。―― いいですね。行きましょう！", "vi": "Chúng mình cùng đi ngắm cảnh đêm nhé? ―― Hay quá, đi thôi!"},
            {"jp": "食事の 後で、お土産を 買いに 行きましょう。", "vi": "Sau khi dùng bữa xong, chúng ta hãy cùng đi mua quà lưu niệm nhé."},
            {"jp": "寝る 前に、本を 読みます。", "vi": "Trước khi đi ngủ, tôi đọc sách."}
        ],
        "quiz": {
            "q": "ご飯を [____] 後で、散歩しましょう。",
            "options": ["食べた", "食べる", "食べて", "食べ"],
            "correct": 0,
            "explain": "Đứng trước 「後で」 động từ phải chia về thể Quá khứ ngắn: 「食べた後で」."
        }
    },
    {
        "id": 20,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 9,
        "lessonTitle": "Bài 9: Học Tập & Đánh Giá Ngôn Ngữ",
        "title": "Đánh giá ngôn ngữ & Nhờ vả lịch sự: N は V-る のが A / V-てくださいませんか",
        "tag": "Ngôn ngữ & Yêu cầu",
        "cat": "language",
        "formula": "N(Ngôn ngữ) は [V thể Từ điển] のが [簡単/難しい/面白い] です<br>V-て くださいませんか (Làm ơn có thể vui lòng... giúp tôi được không?)<br>[Khoảng thời gian] に [Số lần] 回 (Tần suất học tập)",
        "meaning": "Bình luận về độ khó, độ thú vị khi phát âm/viết chữ/học ngoại ngữ và cách nhờ vả thầy cô, người bản xứ giúp đỡ.",
        "notes": "「～てくださいませんか」 là mức độ nhờ vả lịch thiệp và tôn trọng hơn nhiều so với 「～てください」.",
        "examples": [
            {"jp": "日本語は 発音は 簡単ですが、漢字を 書くのが 難しいです。", "vi": "Tiếng Nhật phát âm thì đơn giản nhưng việc viết chữ Hán thì rất khó."},
            {"jp": "この 漢字の 読み方を 教えて くださいませんか。", "vi": "Làm ơn có thể vui lòng chỉ giúp tôi cách đọc chữ Hán này được không ạ?"},
            {"jp": "週に 2回 日本語の 授業が あります。", "vi": "Mỗi tuần tôi có 2 buổi học tiếng Nhật."}
        ],
        "quiz": {
            "q": "もう一度 [____] くださいませんか。",
            "options": ["言って", "言う", "言います", "言いた"],
            "correct": 0,
            "explain": "Trước mẫu câu nhờ vả lịch sự 「くださいませんか」 động từ phải chia thể Te: 「言って」."
        }
    },
    {
        "id": 21,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 10,
        "lessonTitle": "Bài 10: Nguyện Vọng & Đề Nghị Giúp Đỡ",
        "title": "Nguyện vọng tương lai & Giúp đỡ: V-たいです / V-ましょうか / V-てみます",
        "tag": "Nguyện vọng & Giúp đỡ",
        "cat": "wish",
        "formula": "いつか [Địa điểm] に 行きたいです (Ước muốn một ngày nào đó sẽ đi...)<br>V(bỏ ます) + たいです (Muốn làm gì)<br>V-ましょうか (Để tôi làm giúp bạn nhé?)<br>V-て みます (Thử làm điều gì)",
        "meaning": "Bày tỏ ước mơ, hoài bão trong tương lai, ngỏ lời đề nghị hỗ trợ người khác và tâm thế sẵn sàng trải nghiệm cái mới.",
        "notes": "Để hỏi đối phương muốn làm gì: 「何が したいですか」.",
        "examples": [
            {"jp": "いつか 日本へ 留学に 行きたいです。", "vi": "Một ngày nào đó tôi muốn được đi du học Nhật Bản."},
            {"jp": "荷物が 重そうですね。手伝いましょうか。", "vi": "Hành lý trông có vẻ nặng quá. Để tôi xách giúp bạn nhé?"},
            {"jp": "日本料理を 自分で 作って みます。", "vi": "Tôi sẽ thử tự tay nấu món ăn Nhật Bản xem sao."}
        ],
        "quiz": {
            "q": "駅まで 一緒に [____] ましょうか。",
            "options": ["行き", "行く", "行って", "行った"],
            "correct": 0,
            "explain": "Mẫu câu đề nghị giúp đỡ 「V-ましょうか」: bỏ ます thêm ましょうか ➔ 「行きましょうか」."
        }
    },

    # =========================================================================
    # MARUGOTO A2-2: BÀI 11 ĐẾN BÀI 18 (TRUNG CẤP 2)
    # =========================================================================
    {
        "id": 22,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 11,
        "lessonTitle": "Bài 11: Dã Ngoại & BBQ",
        "title": "Mang đi/mang lại & Bất định từ: V-ていきます/きます / 何でもいい / どちらがいい",
        "tag": "Dã ngoại & Lựa chọn",
        "cat": "picnic",
        "formula": "V-て 行きます (Làm rồi mang đi theo) / V-て きます (Mua/làm rồi đem lại đây)<br>[Nghi vấn từ] でも いいです (Bất kỳ cái gì / ai / đâu cũng được)<br>A と B、どちら/どっちが いいですか ―― A に します",
        "meaning": "Phân công đồ đạc mang đi dã ngoại, thể hiện sự thoải mái dễ tính khi chọn món.",
        "notes": "何でもいい (Cái gì cũng được), どこでもいい (Đâu cũng được), 誰でもいい (Ai cũng được).",
        "examples": [
            {"jp": "私は おにぎりを 作って 行きます。", "vi": "Tôi sẽ tự làm cơm nắm mang đi dã ngoại."},
            {"jp": "飲み物は 何が いいですか。―― お茶が いいです。何でも いいですよ。", "vi": "Đồ uống bạn thích gì? ―― Trà thì tốt, mà cái gì cũng được bạn nhé."},
            {"jp": "赤ワインと 白ワイン、どちらが いいですか。―― 白ワインに します。", "vi": "Vang đỏ hay vang trắng bạn thích loại nào hơn? ―― Tôi chọn vang trắng."}
        ],
        "quiz": {
            "q": "飲み物は [____] でも いいですよ。",
            "options": ["なん", "だれ", "どこ", "いつ"],
            "correct": 0,
            "explain": "Đồ uống nên dùng từ để hỏi vật 「何 (なん)」 ➔ 「何でもいい」 (cái gì cũng được)."
        }
    },
    {
        "id": 23,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 12,
        "lessonTitle": "Bài 12: Món Ăn & Hương Vị",
        "title": "Phán đoán thị giác & Miêu tả món ăn: ～そう / A-くて / ～と似ています",
        "tag": "Ẩm thực & Vị giác",
        "cat": "taste",
        "formula": "Tính từ đuôi い (Bỏ い) + そうです (Trông có vẻ... / おいしそう)<br>A-くて (Nối tính từ vị giác: からくて おいしい)<br>N1 は N2 と 似ています (Món này giống món kia) / 違います (Khác nhau)",
        "meaning": "Đưa ra lời khen ngợi cảm quan khi nhìn món ăn, nhận xét hương vị đa tầng và so sánh với món ăn quê hương.",
        "notes": "Ngoại lệ: いい ➔ よさそう (Trông có vẻ được đấy). Khi mời ăn lịch sự: 「よかったら、どうぞ」.",
        "examples": [
            {"jp": "その ケーキ、とても おいしそうですね！", "vi": "Chiếc bánh ngọt đó trông ngon lành quá chừng!"},
            {"jp": "この サラダは ちょっと からくて、おいしいです。", "vi": "Món salad này hơi cay một chút mà ngon thật đấy."},
            {"jp": "これは 韓国の キンパと 似ていますが、味は 違います。", "vi": "Món này trông khá giống Kimbap Hàn Quốc nhưng mùi vị thì khác."}
        ],
        "quiz": {
            "q": "スープが 赤いですから、ちょっと [____] ですね。",
            "options": ["からそう", "からいそう", "からくそう", "からだそう"],
            "correct": 0,
            "explain": "Tính từ đuôi い khi kết hợp với ～そう sẽ bỏ い: からい ➔ 「からそう」."
        }
    },
    {
        "id": 24,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 13,
        "lessonTitle": "Bài 13: Lịch Trình Công Tác",
        "title": "Kinh nghiệm cuộc đời & Lịch trình: V-たことがあります / ～時に着きます",
        "tag": "Kinh nghiệm & Đón tiếp",
        "cat": "experience",
        "formula": "Động từ thể Quá khứ (V-た) + ことがあります / ありません (Đã từng / Chưa từng)<br>[Thời gian] に [Địa điểm] に 着きます / 出発します<br>お疲れ様でした。ようこそ [Địa điểm] へ！",
        "meaning": "Hỏi và nói về trải nghiệm đã từng gặp ai, từng đi đâu trong quá khứ và cách báo cáo lịch trình, đón khách sân bay.",
        "notes": "Chia thể Quá khứ ngắn (Thể た) tương tự như quy tắc chia thể Te (会います ➔ 会った, 行きます ➔ 行った).",
        "examples": [
            {"jp": "わたしは 田中さんに 会ったことが あります。", "vi": "Tôi đã từng gặp anh Tanaka trước đây rồi."},
            {"jp": "飛行機は 午後3時に 成田空港に 着きます。", "vi": "Máy bay sẽ hạ cánh xuống sân bay Narita lúc 3 giờ chiều."},
            {"jp": "田中さん、お疲れ様でした。ようこそ 東京へ！フライトは いかがでしたか。", "vi": "Chào anh Tanaka, anh đã vất vả rồi. Chào mừng anh đến Tokyo! Chuyến bay của anh thế nào ạ?"}
        ],
        "quiz": {
            "q": "日本へ 出張に [____] ことがありますか。",
            "options": ["行った", "行きます", "行かない", "行くて"],
            "correct": 0,
            "explain": "Cấu trúc kinh nghiệm: V-た ことがありますか: 行きます ➔ 「行ったことがありますか」."
        }
    },
    {
        "id": 25,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 14,
        "lessonTitle": "Bài 14: Nơi Làm Việc & Mượn Đồ",
        "title": "Xin phép & Quy tắc công sở: V-てもいいですか / V-てはいけません / お世話になりました",
        "tag": "Xin phép & Lễ nghi",
        "cat": "permission",
        "formula": "V-て + もいいですか (Tôi làm... có được không?)<br>V-て + はいけません (Không được phép làm...)<br>大変 お世話になりました (Cảm ơn anh chị đã giúp đỡ hết lòng)",
        "meaning": "Xin phép mượn máy tính, sử dụng đồ đạc nơi công sở, hiểu các quy tắc cấm đoán và nói lời chào tạm biệt đầy trân trọng.",
        "notes": "Từ chối khéo khi người khác xin mượn đồ: 「すみません、今 使っているんです」.",
        "examples": [
            {"jp": "この コンピューターを 使っても いいですか。―― はい、どうぞ。", "vi": "Tôi dùng chiếc máy tính này có được không? ―― Vâng, xin mời anh cứ dùng."},
            {"jp": "ここで 写真を 撮っては いけません。", "vi": "Không được chụp ảnh tại khu vực này."},
            {"jp": "3日間、大変 お世話になりました。本社の 皆さんによろしく お伝えください。", "vi": "Trong 3 ngày qua, cảm ơn mọi người đã hết lòng giúp đỡ. Cho tôi gửi lời hỏi thăm tới mọi người ở trụ sở chính nhé."}
        ],
        "quiz": {
            "q": "ペンを [____] も いいですか (借ります)。",
            "options": ["借りて", "借って", "借りた", "借る"],
            "correct": 0,
            "explain": "Động từ nhóm 2: かります ➔ chia thể Te là 「借りて」 + もいいですか."
        }
    },
    {
        "id": 26,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 15,
        "lessonTitle": "Bài 15: Cơ Thể & Bệnh Tật",
        "title": "Giải thích bệnh trạng & Lời khuyên: ～んです / V-るといいですよ / V-ないでください",
        "tag": "Sức khỏe & Khuyên can",
        "cat": "health",
        "formula": "[Thể thông thường / Tính từ] + んです (Giải thích triệu chứng: 頭が痛いんです)<br>V(thể Từ điển) + といいですよ (Khuyên nên làm gì)<br>V-ない + でください (Dặn dò đừng làm quá sức)",
        "meaning": "Trình bày tình trạng đau ốm, mệt mỏi với cấp trên, đồng nghiệp và trao nhau những lời khuyên, dặn dò dưỡng bệnh chu đáo.",
        "notes": "Khi nghe người khác ốm đau, câu chúc quen thuộc nhất là: 「お大事に (どうぞ)」.",
        "examples": [
            {"jp": "どうしたんですか。―― ちょっと 頭が 痛いんです。", "vi": "Bạn bị làm sao thế? ―― Tôi bị đau đầu một chút."},
            {"jp": "寝る 前に、この 薬を 飲むと いいですよ。", "vi": "Trước khi đi ngủ, bạn uống viên thuốc này thì tốt đấy nhé."},
            {"jp": "熱が ありますから、あまり 無理を しないでくださいね。", "vi": "Vẫn còn sốt nên bạn đừng làm việc quá sức nhé."}
        ],
        "quiz": {
            "q": "熱が ありますから、無理を [____] ください。",
            "options": ["しないで", "しなくて", "するな", "しない"],
            "correct": 0,
            "explain": "Dặn dò không nên làm điều có hại: V-ない + でください ➔ 「しないでください」."
        }
    },
    {
        "id": 27,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 16,
        "lessonTitle": "Bài 16: Giữ Gìn Sức Khỏe",
        "title": "Liệt kê thói quen & Lời khuyên lối sống: V1-たり V2-たりします / N のために / V-たほうがいい",
        "tag": "Lối sống & Thói quen",
        "cat": "lifestyle",
        "formula": "V1-た + り、V2-た + り します / しています (Lúc làm việc này, lúc làm việc kia)<br>N の ために (Vì mục đích duy trì sức khỏe)<br>V-た ほうがいいです (Nên làm) / V-ない ほうがいいです (Không nên làm)",
        "meaning": "Liệt kê các hoạt động thể thao, thói quen sinh hoạt không theo thứ tự thời gian và đưa ra lời khuyên khoa học về lối sống.",
        "notes": "Khác với thể Te (V1-て V2), cấu trúc 「～たり～たり」 chỉ liệt kê đại diện vài việc trong rất nhiều hoạt động.",
        "examples": [
            {"jp": "週末は 公園を 走ったり、プールで 泳いだり しています。", "vi": "Cuối tuần tôi lúc thì chạy bộ ở công viên, lúc thì đi bơi ở hồ bơi."},
            {"jp": "健康の ために 何か していますか。", "vi": "Để duy trì sức khỏe, bạn có làm hoạt động gì không?"},
            {"jp": "夜遅くまで 起きていないで、早く 寝た ほうが いいですよ。", "vi": "Đừng thức quá khuya, bạn nên đi ngủ sớm thì tốt hơn đấy."}
        ],
        "quiz": {
            "q": "休みの 日は 本を [____]、映画を 見たり します。",
            "options": ["読んだり", "読んで", "読んだ", "読みたり"],
            "correct": 0,
            "explain": "Động từ thể Quá khứ ngắn (Thể た) + り: 読みます ➔ 読んだ ➔ 「読んだり」."
        }
    },
    {
        "id": 28,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 17,
        "lessonTitle": "Bài 17: Quà Tặng & Kỷ Niệm",
        "title": "Trao gửi quà tặng & Định ngữ: あげます / もらったんです / ～とか / V-る + もの",
        "tag": "Quà tặng & Định ngữ",
        "cat": "gift",
        "formula": "Watashi wa [Người nhận] に [Món quà] を あげます (Tặng ai cái gì)<br>Watashi wa [Người tặng] に [Món quà] を もらったんです (Được ai tặng)<br>N1 とか N2 とか (Liệt kê đại diện như là...)<br>[V thể Từ điển] + もの (Đồ vật để làm gì: 部屋に飾るもの)",
        "meaning": "Tặng quà vào các dịp lễ kỷ niệm, giải thích nguồn gốc kỷ vật đáng trân trọng và dùng mệnh đề định ngữ miêu tả công năng của quà tặng.",
        "notes": "Dùng 「もらったんです」 khi giải thích lý do vì sao mình sở hữu món đồ xinh xắn đối phương vừa khen ngợi.",
        "examples": [
            {"jp": "その ネックレス、とても 素敵ですね。―― 誕生日に 彼に もらったんです。", "vi": "Sợi dây chuyền đó đẹp quá nhỉ! ―― Tôi được bạn trai tặng vào ngày sinh nhật đấy."},
            {"jp": "母の日に きれいな 花を あげました。", "vi": "Vào Ngày của Mẹ tôi đã tặng một bó hoa tươi cho mẹ."},
            {"jp": "結婚の お祝いに 絵とか 時計を あげます。部屋に 飾る ものが いいですね。", "vi": "Mừng đám cưới thường tặng những thứ như tranh hay đồng hồ. Đồ trang trí phòng thì rất hay."}
        ],
        "quiz": {
            "q": "新居の 部屋に [____] ものを プレゼントしたいです。",
            "options": ["飾る", "飾って", "飾った", "飾り"],
            "correct": 0,
            "explain": "Động từ bổ nghĩa cho danh từ chỉ vật 「もの」 ở thể Từ điển: 「飾るもの」 (đồ trang trí)."
        }
    },
    {
        "id": 29,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 18,
        "lessonTitle": "Bài 18: Lễ Hội & Trang Phục",
        "title": "Ý kiến, trích dẫn & Trang phục: ～と思います / ～と言っていました / 4 động từ mặc đồ",
        "tag": "Ý kiến & Trang phục",
        "cat": "clothing",
        "formula": "[Thể thông thường] + と 思います (Tôi nghĩ là...)<br>[Thể thông thường] + と 言っていました (Ai đó nói rằng...)<br>Phân loại động từ mặc trang phục thể V-ています:<br>• 着ています: Thân trên / Toàn thân (Áo, váy, vest, kimono)<br>• 履いています: Thân dưới / Chân (Quần, váy ngắn, tất, giày)<br>• 被っています: Đầu (Mũ, nón)<br>• 掛けています: Mắt / Phụ kiện (Kính mắt)",
        "meaning": "Bày tỏ quan điểm cá nhân, thuật lại lời nói của người khác và phân loại chính xác các hành động diện trang phục dự tiệc.",
        "notes": "Trong đám cưới, lời chúc mừng chuẩn mực nhất là: 「ご結婚、おめでとうございます！」.",
        "examples": [
            {"jp": "阿部さんの お祝いは パーティーが いいと 思います。", "vi": "Mừng cho anh Abe thì tôi nghĩ tổ chức một bữa tiệc là tuyệt nhất."},
            {"jp": "阿部さんは みんなと 話したいと 言っていましたよ。", "vi": "Anh Abe nói là rất muốn được trò chuyện cùng mọi người đấy."},
            {"jp": "パーティーで 素敵な 着物を 着て、眼鏡を 掛けている 人が います。", "vi": "Ở bữa tiệc có một người đang mặc bộ Kimono tuyệt đẹp và đeo kính mắt."}
        ],
        "quiz": {
            "q": "パーティーで 新しい スーツを [____] います。",
            "options": ["着て", "履いて", "被って", "掛けて"],
            "correct": 0,
            "explain": "Bộ com-lê/vest (スーツ) là âu phục mặc trên thân người, dùng động từ 「着ます」 ➔ 「着ています」."
        }
    }
]

print(f"Loaded {len(ALL_GRAMMAR_ITEMS)} core grammar master points covering 26 lessons.")
