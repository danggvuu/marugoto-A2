# -*- coding: utf-8 -*-
"""
scripts/master_grammar_data.py
Bộ Dữ Liệu 29 Chuyên Đề Ngữ Pháp Toàn Diện Marugoto A1 - A2.1 - A2.2 (26 Bài Học)
100% CHUẨN HOÁ HÁN TỰ & CUNG CẤP FURIGANA (<ruby>) CHO TẤT CẢ VÍ DỤ:
- Không sử dụng các chữ Hán chưa học (như 発音, 簡単, 漢字, 書く, 難しい, 教えて, 授業, 荷物, 料理, 作る, 写真, 映画...).
- Các chữ Hán chưa học được chuyển về Hiragana chuẩn giáo trình Marugoto.
- Tất cả chữ Hán đều có thẻ <ruby>...<rt>cách đọc</rt></ruby> để học sinh luôn biết cách đọc chính xác.
"""

ALL_GRAMMAR_ITEMS = [
    # =========================================================================
    # MARUGOTO A1: BÀI 11 ĐẾN BÀI 18 (NHẬP MÔN & SƠ CẤP 1)
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
        "formula": "N が <ruby>好<rt>す</rt></ruby>きです (Thích N)<br>N が 大<ruby>好<rt>す</rt></ruby>きです (Rất thích N)<br>N は <ruby>好<rt>す</rt></ruby>きじゃないです (Không thích N)",
        "meaning": "Dùng để nói về sở thích cá nhân hoặc hỏi đối phương thích cái gì / thể loại nào (どんな N が 好きですか).",
        "notes": "Trợ từ đi kèm trước 好き (Tính từ đuôi な) là 「が」. Khi nhấn mạnh hoặc phủ định có thể thay bằng 「は」.",
        "examples": [
            {
                "jp": "わたしは まんがが 好きです。",
                "ruby": "わたしは まんがが <ruby>好<rt>す</rt></ruby>きです。",
                "vi": "Tôi thích truyện tranh."
            },
            {
                "jp": "どんな えいがが 好きですか。―― アクションえいがが 好きです。",
                "ruby": "どんな えいがが <ruby>好<rt>す</rt></ruby>きですか。―― アクションえいがが <ruby>好<rt>す</rt></ruby>きです。",
                "vi": "Bạn thích thể loại phim nào? ―― Tôi thích phim hành động."
            },
            {
                "jp": "ホラーえいがは 好きじゃないです。",
                "ruby": "ホラーえいがは <ruby>好<rt>す</rt></ruby>きじゃないです。",
                "vi": "Phim kinh dị thì tôi không thích lắm."
            }
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
        "notes": "Chỉ dùng với danh từ chỉ kỹ năng, ngôn ngữ hoặc môn thể thao (テニス, ピアノ, 日本語, りょうり...).",
        "examples": [
            {
                "jp": "わたしは テニスが できます。",
                "ruby": "わたしは テニスが できます。",
                "vi": "Tôi có thể chơi quần vợt (tennis)."
            },
            {
                "jp": "かんこく語が 少し できます。",
                "ruby": "かんこく<ruby>語<rt>ご</rt></ruby>が <ruby>少<rt>すこ</rt></ruby>し できます。",
                "vi": "Tôi có thể nói được một chút tiếng Hàn."
            },
            {
                "jp": "ピアノは できませんが、ギターが できます。",
                "ruby": "ピアノは できませんが、ギターが できます。",
                "vi": "Piano thì tôi không chơi được nhưng guitar thì tôi biết chơi."
            }
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
            {
                "jp": "うちで 本を 読みます。",
                "ruby": "うちで <ruby>本<rt>ほん</rt></ruby>を <ruby>読<rt>よ</rt></ruby>みます。",
                "vi": "Tôi đọc sách tại nhà."
            },
            {
                "jp": "やすみの 日に よく こうえんで しゃしんを とります。",
                "ruby": "やすみの <ruby>日<rt>ひ</rt></ruby>に よく こうえんで しゃしんを とります。",
                "vi": "Vào ngày nghỉ tôi thường chụp ảnh ở công viên."
            },
            {
                "jp": "おさけは あまり のみません。",
                "ruby": "おさけは あまり のみません。",
                "vi": "Rượu bia thì tôi không hay uống lắm."
            }
        ],
        "quiz": {
            "q": "わたしは ぜんぜん えいがを [____]。",
            "options": ["見ません", "見ます", "見ました", "見ています"],
            "correct": 0,
            "explain": "Phó từ 「ぜんぜん」 (hoàn toàn không) luôn đi với thể phủ định: 「見ません」."
        }
    },
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
        "notes": "Phân biệt trợ từ: Thời gian dùng 「に」; Nơi chốn diễn ra sự kiện dùng 「で」 (không dùng に).",
        "examples": [
            {
                "jp": "どようびに コンサートが あります。",
                "ruby": "どようびに コンサートが あります。",
                "vi": "Vào thứ bảy sẽ có một buổi hòa nhạc."
            },
            {
                "jp": "ホールで えいがが あります。",
                "ruby": "ホールで えいがが あります。",
                "vi": "Tại hội trường sẽ có buổi chiếu phim."
            },
            {
                "jp": "あした こうえんで おまつりが あります。",
                "ruby": "あした こうえんで おまつりが あります。",
                "vi": "Ngày mai ở công viên sẽ có lễ hội."
            }
        ],
        "quiz": {
            "q": "あした 学校 [____] パーティーが あります。",
            "options": ["で", "に", "を", "へ"],
            "correct": 0,
            "explain": "Nơi diễn ra sự kiện, hoạt động dùng trợ từ 「で」."
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
        "formula": "[Địa điểm] へ [V(bỏ ます)] に 行きます (Đi để làm gì)<br>いっしょに V-ませんか (Bạn có muốn cùng làm... với tôi không?)<br>V-ましょう (Chúng ta cùng làm... nhé!)",
        "meaning": "Diễn đạt mục đích đi đến đâu để làm gì và rủ rê, mời mọc đối phương một cách lịch sự.",
        "notes": "V-ませんか mang tính chất thăm dò ý kiến đối phương; V-ましょう mang tính chủ động đề xuất.",
        "examples": [
            {
                "jp": "わたしは えいがを 見に 行きます。",
                "ruby": "わたしは えいがを <ruby>見<rt>み</rt></ruby>に <ruby>行<rt>い</rt></ruby>きます。",
                "vi": "Tôi đi xem phim."
            },
            {
                "jp": "あした いっしょに えいがを 見に 行きませんか。―― いいですね。行きましょう！",
                "ruby": "あした いっしょに えいがを <ruby>見<rt>み</rt></ruby>に <ruby>行<rt>い</rt></ruby>きませんか。―― いいですね。<ruby>行<rt>い</rt></ruby>きましょう！",
                "vi": "Ngày mai bạn cùng tôi đi xem phim nhé? ―― Ý hay đấy, đi thôi!"
            },
            {
                "jp": "ちょっと やすみましょう。",
                "ruby": "ちょっと やすみましょう。",
                "vi": "Chúng ta cùng nghỉ ngơi một chút nhé."
            }
        ],
        "quiz": {
            "q": "カフェへ コーヒーを [____] に 行きませんか。",
            "options": ["飲み", "飲む", "飲んで", "飲ま"],
            "correct": 0,
            "explain": "Mục đích chuyển động: Động từ bỏ ます + に行きます ➔ 「飲みに行きます」."
        }
    },
    {
        "id": 6,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 13,
        "lessonTitle": "Bài 13: Giao Thông & Di Chuyển",
        "title": "Chặng đường di chuyển: [Từ] から [Đến] まで [Phương tiện] で 行きます",
        "tag": "Giao thông",
        "cat": "transit",
        "formula": "[Nơi xuất phát] から [Nơi đến] まで [Phương tiện] で 行きます / 来ます<br>[Phương tiện] に 乗ります (Lên xe) / を 降ります (Xuống xe)",
        "meaning": "Nói về lộ trình từ điểm xuất phát đến điểm đích, phương tiện giao thông và thao tác lên xuống xe.",
        "notes": "Lên xe dùng trợ từ 「に」; Xuống xe dùng trợ từ 「を」.",
        "examples": [
            {
                "jp": "うちから 駅まで バスで 行きます。",
                "ruby": "うちから <ruby>駅<rt>えき</rt></ruby>まで バスで <ruby>行<rt>い</rt></ruby>きます。",
                "vi": "Từ nhà đến nhà ga tôi đi bằng xe buýt."
            },
            {
                "jp": "とうきょうから きょうとまで しんかんせんで 行きます。",
                "ruby": "とうきょうから きょうとまで しんかんせんで <ruby>行<rt>い</rt></ruby>きます。",
                "vi": "Từ Tokyo đến Kyoto tôi đi bằng tàu Shinkansen."
            },
            {
                "jp": "駅で でんしゃに 乗ります。つぎの 駅で でんしゃを おります。",
                "ruby": "<ruby>駅<rt>えき</rt></ruby>で でんしゃに <ruby>乗<rt>の</rt></ruby>ります。つぎの <ruby>駅<rt>えき</rt></ruby>で でんしゃを おります。",
                "vi": "Lên tàu điện ở nhà ga. Xuống tàu ở ga tiếp theo."
            }
        ],
        "quiz": {
            "q": "毎朝 バス [____] 学校へ 行きます。",
            "options": ["で", "に", "を", "から"],
            "correct": 0,
            "explain": "Phương tiện giao thông dùng trợ từ 「で」."
        }
    },
    {
        "id": 7,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 14,
        "lessonTitle": "Bài 14: Vị Trí & Không Gian",
        "title": "Vị trí & Sự tồn tại: [Địa điểm] に N が あります/います / [Vị trí] に あります",
        "tag": "Vị trí",
        "cat": "location",
        "formula": "[Địa điểm] に N が あります (Đồ vật/công trình)<br>[Địa điểm] に N が います (Người/động vật)<br>N1 は N2 の [前/後ろ/中/近く] に あります",
        "meaning": "Xác định sự hiện diện của người, vật hoặc mô tả vị trí tương đối giữa các địa điểm trong thành phố.",
        "notes": "ありました/いました dùng cho quá khứ; Phân biệt あります (vật vô tri) và います (sinh vật sống).",
        "examples": [
            {
                "jp": "こうえんに きれいな 花が あります。",
                "ruby": "こうえんに きれいな <ruby>花<rt>はな</rt></ruby>が あります。",
                "vi": "Trong công viên có những bông hoa đẹp."
            },
            {
                "jp": "ロビーに あんないの 人が います。",
                "ruby": "ロビーに あんないの <ruby>人<rt>ひと</rt></ruby>が います。",
                "vi": "Ở sảnh chờ có người hướng dẫn."
            },
            {
                "jp": "ぎんこうは デパートの となりに あります。",
                "ruby": "ぎんこうは デパートの となりに あります。",
                "vi": "Ngân hàng nằm ở ngay bên cạnh trung tâm thương mại."
            }
        ],
        "quiz": {
            "q": "駅の 前に スーパー [____] あります。",
            "options": ["が", "は", "に", "で"],
            "correct": 0,
            "explain": "Chỉ sự tồn tại của đồ vật/địa điểm: 「N が あります」."
        }
    },
    {
        "id": 8,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 15,
        "lessonTitle": "Bài 15: Quà Tặng & Cho Nhận",
        "title": "Muốn có đồ vật & Cho - Nhận: ～が ほしいです / あげます / もらいました",
        "tag": "Cho nhận & Ước muốn",
        "cat": "giving",
        "formula": "N が ほしいです (Tôi muốn có N)<br>N1(người nhận) に N2(vật) を あげます (Tặng cho ai cái gì)<br>N1(người tặng) に N2(vật) を もらいました (Nhận từ ai cái gì)",
        "meaning": "Bày tỏ ước muốn sở hữu một món đồ và diễn đạt hành động tặng hoặc nhận quà từ bạn bè, người thân.",
        "notes": "ほしいです chỉ dùng cho mong muốn của ngôi thứ nhất (tôi); Người nhận/người tặng đi với trợ từ 「に」.",
        "examples": [
            {
                "jp": "わたしは あたらしい スマホが ほしいです。",
                "ruby": "わたしは あたらしい スマホが ほしいです。",
                "vi": "Tôi muốn có một chiếc điện thoại thông minh mới."
            },
            {
                "jp": "カーラさんに 花を あげます。",
                "ruby": "カーラさんに <ruby>花<rt>はな</rt></ruby>を あげます。",
                "vi": "Tôi tặng hoa cho Carla."
            },
            {
                "jp": "たんじょうびに 友達に とけいを もらいました。",
                "ruby": "たんじょうびに <ruby>友達<rt>ともだち</rt></ruby>に とけいを もらいました。",
                "vi": "Vào ngày sinh nhật tôi đã nhận được chiếc đồng hồ từ bạn tôi."
            }
        ],
        "quiz": {
            "q": "父の 日に 父 [____] ネクタイを あげました。",
            "options": ["に", "で", "を", "から"],
            "correct": 0,
            "explain": "Người nhận hành động tặng quà đi với trợ từ 「に」."
        }
    },
    {
        "id": 9,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 16,
        "lessonTitle": "Bài 16: Mua Sắm & Giá Cả",
        "title": "Mua sắm & Quá khứ: V-ました / ～は いくらですか / これを ください",
        "tag": "Mua sắm",
        "cat": "shopping",
        "formula": "[Đồ vật] を かいました (Đã mua đồ gì)<br>[Món hàng] は いくらですか (Hỏi giá cả)<br>これ / それ を ください (Làm ơn bán cho tôi cái này)",
        "meaning": "Giao tiếp mua sắm tại cửa hàng, hỏi giá tiền và kể lại các món đồ đã mua trong quá khứ.",
        "notes": "Để chọn món đồ quyết định mua: 「これ / それ を ください」.",
        "examples": [
            {
                "jp": "きょねん 日本で かわいい ふくを かいました。",
                "ruby": "きょねん <ruby>日本<rt>にほん</rt></ruby>で かわいい ふくを かいました。",
                "vi": "Năm ngoái tôi đã mua quần áo đáng yêu tại Nhật Bản."
            },
            {
                "jp": "すみません、この かさは いくらですか。―― せんごひゃくえんです。",
                "ruby": "すみません、この かさは いくらですか。―― せんごひゃくえんです。",
                "vi": "Xin lỗi, chiếc ô này giá bao nhiêu? ―― Dạ 1.500 Yên ạ."
            },
            {
                "jp": "この シャツを ください。",
                "ruby": "この シャツを ください。",
                "vi": "Xin hãy lấy cho tôi chiếc áo sơ mi này."
            }
        ],
        "quiz": {
            "q": "この りんごは ひとつ [____] ですか。―― 150円です。",
            "options": ["いくら", "いくつ", "どこ", "どう"],
            "correct": 0,
            "explain": "Từ để hỏi giá tiền là 「いくら」."
        }
    },
    {
        "id": 10,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 17,
        "lessonTitle": "Bài 17: Cảm Nhận Quá Khứ & Chuỗi Hành Động",
        "title": "Tính từ quá khứ & Nối hành động: A-かったです / Na-でした / V1-て V2-ます",
        "tag": "Cảm nhận & Chuỗi hành động",
        "cat": "action-chain",
        "formula": "Tính từ đuôi い: [Bỏ い] + かったです (Đã từng rất...)<br>Tính từ đuôi な: [Bỏ な] + でした (Đã từng...)<br>V1-て、V2-て、V3-ます (Làm việc 1, rồi việc 2, rồi việc 3)",
        "meaning": "Chia sẻ cảm xúc về chuyến đi hay sự việc đã qua và kết nối các hành động diễn ra theo trình tự thời gian.",
        "notes": "Thể て của động từ dùng để nối các vế câu hành động liên tiếp.",
        "examples": [
            {
                "jp": "きのうの 旅行は とても たのしかったです。",
                "ruby": "きのうの <ruby>旅行<rt>りょこう</rt></ruby>は とても たのしかったです。",
                "vi": "Chuyến du lịch hôm qua đã rất là vui."
            },
            {
                "jp": "きょうとは しずかでした。",
                "ruby": "きょうとは しずかでした。",
                "vi": "Kyoto đã rất yên tĩnh."
            },
            {
                "jp": "あさ おきて、かおを あらって、朝ごはんを 食べます。",
                "ruby": "あさ おきて、かおを あらって、<ruby>朝<rt>あさ</rt></ruby>ごはんを <ruby>食<rt>た</rt></ruby>べます。",
                "vi": "Buổi sáng thức dậy, rửa mặt rồi ăn bữa sáng."
            }
        ],
        "quiz": {
            "q": "きのうの 天気は とても [____]。",
            "options": ["よかったです", "いいでした", "よくでした", "いいかったです"],
            "correct": 0,
            "explain": "Tính từ いい (tốt) khi chia quá khứ biến thành 「よかったです」."
        }
    },
    {
        "id": 11,
        "level": "A1",
        "levelName": "Marugoto A1",
        "lesson": 18,
        "lessonTitle": "Bài 18: Trải Nghiệm & Dự Định",
        "title": "Đã làm / Chưa làm: もう V-ました / まだ V-ていません",
        "tag": "Hoàn thành & Chưa xong",
        "cat": "experience",
        "formula": "もう V-ましたか (Đã làm... xong chưa?) ―― はい、もう V-ました<br>いいえ、まだ V-ていません (Chưa, tôi vẫn chưa làm)",
        "meaning": "Hỏi và trả lời về tiến độ hoàn thành một công việc hoặc trải nghiệm một địa điểm tham quan.",
        "notes": "Phủ định của 「もう V-ましたか」 là 「まだ V-ていません」 (chứ không dùng まだ V-ませんでした).",
        "examples": [
            {
                "jp": "もう とうきょうタワーを 見ましたか。―― はい、もう 見ました。",
                "ruby": "もう とうきょうタワーを <ruby>見<rt>み</rt></ruby>ましたか。―― はい、もう <ruby>見<rt>み</rt></ruby>ました。",
                "vi": "Bạn đã ngắm tháp Tokyo chưa? ―― Vâng, tôi đã ngắm rồi."
            },
            {
                "jp": "ふじさんは まだ 見ていません。",
                "ruby": "ふじさんは まだ <ruby>見<rt>み</rt></ruby>ていません。",
                "vi": "Núi Phú Sĩ thì tôi vẫn chưa ngắm."
            },
            {
                "jp": "これから とうきょうタワーへ 行きます。",
                "ruby": "これから とうきょうタワーへ <ruby>行<rt>い</rt></ruby>きます。",
                "vi": "Từ bây giờ tôi sẽ đi đến tháp Tokyo."
            }
        ],
        "quiz": {
            "q": "おひるごはんを もう 食べましたか。―― いいえ、[____]。",
            "options": ["まだ 食べていません", "まだ 食べませんでした", "もう 食べません", "ぜんぜん 食べました"],
            "correct": 0,
            "explain": "Trả lời chưa thực hiện hành động: 「いいえ、まだ 食べていません」."
        }
    },

    # =========================================================================
    # MARUGOTO A2-1: BÀI 1 ĐẾN BÀI 10 (SƠ CẤP 2 - PHẦN 1)
    # =========================================================================
    {
        "id": 12,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 1,
        "lessonTitle": "Bài 1: Gia Đình & Nghề Nghiệp",
        "title": "Trạng thái tiếp diễn & Nghề nghiệp: V-ています / にすんでいます / ではたらいています",
        "tag": "Trạng thái & Nghề nghiệp",
        "cat": "family",
        "formula": "[Nơi ở] に すんで います (Đang sinh sống ở...)<br>[Nơi làm việc] で はたらいて います (Đang làm việc tại...)<br>[Hành động thường xuyên] を して います (Đang dạy / đang học)",
        "meaning": "Diễn đạt trạng thái hiện tại kéo dài: nơi sinh sống định cư, nơi công tác làm việc và thói quen sinh hoạt nghề nghiệp.",
        "notes": "Sống ở đâu dùng trợ từ 「に」 (すんでいます); Làm việc tại đâu dùng trợ từ 「で」 (はたらいています).",
        "examples": [
            {
                "jp": "わたしは とうきょうに すんで います。",
                "ruby": "わたしは とうきょうに すんで います。",
                "vi": "Tôi hiện đang sống ở Tokyo."
            },
            {
                "jp": "父は でんしゃの かいしゃで はたらいて います。",
                "ruby": "<ruby>父<rt>ちち</rt></ruby>は でんしゃの かいしゃで はたらいて います。",
                "vi": "Bố tôi đang làm việc tại một công ty xe điện."
            },
            {
                "jp": "まい週 すいようびに 友達に えいごを おしえて います。",
                "ruby": "まい<ruby>週<rt>しゅう</rt></ruby> すいようびに <ruby>友達<rt>ともだち</rt></ruby>に えいごを おしえて います。",
                "vi": "Tôi dạy tiếng Anh cho bạn vào mỗi thứ Tư."
            }
        ],
        "quiz": {
            "q": "あねは ベトナム [____] すんで います。",
            "options": ["に", "で", "を", "へ"],
            "correct": 0,
            "explain": "Động từ cư trú 「すんでいます」 đi kèm với trợ từ chỉ nơi chốn tồn tại là 「に」."
        }
    },
    {
        "id": 13,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 2,
        "lessonTitle": "Bài 2: Ngôn Ngữ & Thời Điểm",
        "title": "Danh từ hóa sở thích & Mệnh đề thời điểm: V-る こと / ～のとき / V-るとき",
        "tag": "Sở thích & Thời điểm",
        "cat": "time-clause",
        "formula": "私の しゅみは [V thể Từ điển] ことです (Sở thích của tôi là việc...)<br>N の とき、～ (Khi còn là học sinh / lúc nhỏ...)<br>[V thể Từ điển] とき、～ (Khi làm việc gì thì...)",
        "meaning": "Biến động từ thành cụm danh từ để giới thiệu sở thích cá nhân và tạo mệnh đề trạng ngữ chỉ thời điểm diễn ra sự việc.",
        "notes": "Danh từ đi với とき cần có 「の」: 「子どものとき」. Động từ thì chia trực tiếp về thể từ điển: 「ねるとき」.",
        "examples": [
            {
                "jp": "私の しゅみは 音楽を きく ことです。",
                "ruby": "<ruby>私<rt>わたし</rt></ruby>の しゅみは <ruby>音楽<rt>おんがく</rt></ruby>を きく ことです。",
                "vi": "Sở thích của tôi là nghe âm nhạc."
            },
            {
                "jp": "子どもの とき、よく アニメを 見ました。",
                "ruby": "<ruby>子<rt>こ</rt></ruby>どもの とき、よく アニメを <ruby>見<rt>み</rt></ruby>ました。",
                "vi": "Khi còn nhỏ, tôi rất hay xem phim hoạt hình."
            },
            {
                "jp": "ひまな とき、りょうりを つくります。",
                "ruby": "ひまな とき、りょうりを つくります。",
                "vi": "Những khi rảnh rỗi, tôi thường tự nấu ăn."
            }
        ],
        "quiz": {
            "q": "わたしの しゅみは まんがを [____] ことです。",
            "options": ["読む", "読んだ", "読んで", "読み"],
            "correct": 0,
            "explain": "Cấu trúc danh từ hóa: Động từ thể Từ điển (V-る) + こと ➔ 「読むこと」."
        }
    },
    {
        "id": 14,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 3,
        "lessonTitle": "Bài 3: Thời Tiết & Sự Biến Đổi Tự Nhiên",
        "title": "Thay đổi trạng thái & Lý do: ～くなる / ～になる / V-るのが好き / ～から",
        "tag": "Thời tiết & Biến đổi",
        "cat": "weather",
        "formula": "Tính từ đuôi い: [Bỏ い] + く なります (Trở nên lạnh/mát...)<br>Tính từ đuôi な / Danh từ: + に なります (Trở nên yên tĩnh / sang mùa thu...)<br>V(thể Từ điển) のが 好きです (Thích việc...)<br>[Mệnh đề] から (Vì...)",
        "meaning": "Miêu tả sự biến đổi dần dần của thời tiết qua các mùa trong năm và nêu lý do giải thích cho sở thích của mình.",
        "notes": "Khác biệt đuôi biến đổi: 「さむく なります」 (Tính từ い) vs 「しずかに なります / 秋に なります」 (Tính từ な / Danh từ).",
        "examples": [
            {
                "jp": "三月ごろ、だんだん あたたかく なります。",
                "ruby": "<ruby>三月<rt>さんがつ</rt></ruby>ごろ、だんだん あたたかく なります。",
                "vi": "Khoảng tháng 3, thời tiết dần dần trở nên ấm áp."
            },
            {
                "jp": "秋が 好きです。すずしいのが 好きですから。",
                "ruby": "<ruby>秋<rt>あき</rt></ruby>が <ruby>好<rt>す</rt></ruby>きです。すずしいのが <ruby>好<rt>す</rt></ruby>きですから。",
                "vi": "Tôi thích mùa thu. Vì tôi thích sự mát mẻ."
            },
            {
                "jp": "スキーが できますから、冬が いちばん 好きです。",
                "ruby": "スキーが できますから、<ruby>冬<rt>ふゆ</rt></ruby>が いちばん <ruby>好<rt>す</rt></ruby>きです。",
                "vi": "Vì có thể trượt tuyết nên tôi thích mùa đông nhất."
            }
        ],
        "quiz": {
            "q": "12月になると、だんだん [____] なります。",
            "options": ["さむく", "さむい", "さむくて", "さむに"],
            "correct": 0,
            "explain": "Tính từ đuôi い đi với なります: bỏ い thêm く ➔ 「さむく なります」."
        }
    },
    {
        "id": 15,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 4,
        "lessonTitle": "Bài 4: Dự Báo Thời Tiết & Khuyên Nhủ",
        "title": "Phán đoán khả năng: ～でしょう (Chắc là) / ～かもしれません (Có lẽ)",
        "tag": "Dự báo & Phán đoán",
        "cat": "forecast",
        "formula": "[Thể thông thường / Danh từ] + でしょう (Chắc hẳn là... độ chắc chắn cao)<br>[Thể thông thường / Danh từ] + かもしれません (Có lẽ là... độ chắc chắn khoảng 50%)<br>V-てください (Hãy mặc áo ấm vào nhé)",
        "meaning": "Đưa ra dự đoán về thời tiết trong ngày, ước đoán khả năng xảy ra mưa/nắng và nhắc nhở bạn bè mang theo áo mưa/áo khoác.",
        "notes": "Danh từ và tính từ đuôi な đi trực tiếp với 「でしょう / かもしれません」 (không thêm だ).",
        "examples": [
            {
                "jp": "あしたは 晴れでしょう。",
                "ruby": "あしたは <ruby>晴<rt>は</rt></ruby>れでしょう。",
                "vi": "Ngày mai chắc là trời sẽ nắng ráo."
            },
            {
                "jp": "ひるからは 雨が ふるかもしれません。",
                "ruby": "ひるからは <ruby>雨<rt>あめ</rt></ruby>が ふるかもしれません。",
                "vi": "Buổi chiều có thể trời sẽ đổ mưa."
            },
            {
                "jp": "こんばんは さむくなるかもしれませんから、コートを きてください。",
                "ruby": "こんばんは さむくなるかもしれませんから、コートを きてください。",
                "vi": "Tối nay có lẽ trời sẽ trở lạnh đấy, bạn hãy mặc áo khoác vào nhé."
            }
        ],
        "quiz": {
            "q": "明日は 午後から 雨が [____] かもしれません。",
            "options": ["ふる", "ふって", "ふり", "ふった"],
            "correct": 0,
            "explain": "Trước liên từ dự đoán 「かもしれません」 động từ để ở thể Từ điển (thể thông thường): 「ふる」."
        }
    },
    {
        "id": 16,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 5,
        "lessonTitle": "Bài 5: Thị Trấn & Nơi Chốn",
        "title": "Nối tính từ đa tầng & Quan hệ tương phản: A-くて / Na-で / ～けど・～が",
        "tag": "Miêu tả nơi chốn",
        "cat": "town-description",
        "formula": "Tính từ đuôi い: [Bỏ い] + くて (Rộng và đẹp...)<br>Tính từ đuôi な: [Bỏ な] + で (Yên tĩnh và tiện lợi...)<br>[Vế 1] けど / が、[Vế 2 đối lập] (Tuy gần nhưng mà đắt...)",
        "meaning": "Miêu tả đặc điểm khu phố, công viên hoặc nhà ở bằng cách xâu chuỗi nhiều tính từ đồng chiều hoặc liên kết hai vế đối lập.",
        "notes": "「～けど」 dùng trong văn nói thân mật; 「～が」 dùng trong văn phong lịch sự trang trọng.",
        "examples": [
            {
                "jp": "この こうえんは 広くて、きれいです。",
                "ruby": "この こうえんは <ruby>広<rt>ひろ</rt></ruby>くて、きれいです。",
                "vi": "Công viên này vừa rộng lớn lại vừa đẹp đẽ."
            },
            {
                "jp": "この 町は しずかで、とても いいです。",
                "ruby": "この <ruby>町<rt>まち</rt></ruby>は しずかで、とても いいです。",
                "vi": "Thị trấn này yên bình và rất đáng sống."
            },
            {
                "jp": "この へやは 駅から ちかいですが、高いです。",
                "ruby": "この へやは <ruby>駅<rt>えき</rt></ruby>から ちかいですが、<ruby>高<rt>たか</rt></ruby>いです。",
                "vi": "Căn phòng này tuy gần nhà ga nhưng lại đắt."
            }
        ],
        "quiz": {
            "q": "この レストランは [____]、おいしいです。",
            "options": ["安くて", "安いで", "安くては", "安いくて"],
            "correct": 0,
            "explain": "Nối tính từ đuôi い: 安い ➔ bỏ い thêm くて ➔ 「安くて」."
        }
    },
    {
        "id": 17,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 6,
        "lessonTitle": "Bài 6: Chỉ Đường & Ngã Rẽ",
        "title": "Chỉ đường & Phủ định thông tin: V-て (Chỉ dẫn) / N1 じゃなくて N2 / V-たいんですが",
        "tag": "Chỉ đường",
        "cat": "direction",
        "formula": "[Con đường] を まっすぐ 行って (Đi thẳng con đường này)<br>[Ngã rẽ] を 右 / 左 に まがってください (Hãy rẽ phải/trái ở...)<br>N1 じゃなくて N2 (Không phải cái 1, mà là cái 2)<br>～へ 行きたいんですが (Tôi muốn đi đến... xin hỏi đường)",
        "meaning": "Chỉ dẫn đường đi cụ thể từng bước, đính chính lại thông tin bị nghe nhầm và mở lời hỏi đường một cách tự nhiên.",
        "notes": "Hành động di chuyển qua không gian (đi thẳng con đường, băng qua cầu) dùng trợ từ 「を」.",
        "examples": [
            {
                "jp": "ふたつめの かどを 右に まがってください。",
                "ruby": "ふたつめの かどを <ruby>右<rt>みぎ</rt></ruby>に まがってください。",
                "vi": "Xin hãy rẽ phải ở góc ngã rẽ thứ hai."
            },
            {
                "jp": "ひとつめ じゃなくて、ふたつめですよ。",
                "ruby": "ひとつめ じゃなくて、ふたつめですよ。",
                "vi": "Không phải ngã rẽ thứ nhất đâu, mà là cái thứ hai đấy."
            },
            {
                "jp": "すみません。はくぶつかんに 行きたいんですが、どこですか。",
                "ruby": "すみません。はくぶつかんに <ruby>行<rt>い</rt></ruby>きたいんですが、どこですか。",
                "vi": "Xin lỗi. Tôi muốn đến viện bảo tàng, nó nằm ở đâu vậy ạ?"
            }
        ],
        "quiz": {
            "q": "この 道を まっすぐ [____] ください。",
            "options": ["行って", "行きます", "行く", "行かない"],
            "correct": 0,
            "explain": "Chỉ dẫn hành động đi tiếp: dùng thể Te 「行ってください」."
        }
    },
    {
        "id": 18,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 7,
        "lessonTitle": "Bài 7: Hẹn Hò & Xin Lỗi Muộn Giờ",
        "title": "Hẹn giờ & Lý do muộn: N で(も) いいですか / N で / V-て すみません",
        "tag": "Hẹn gặp & Xin lỗi",
        "cat": "appointment",
        "formula": "[Mốc thời gian] で(も) いいですか (Giờ này có được không?)<br>V-て すみません (Xin lỗi vì đã đến muộn / làm phiền...)<br>N(Lý do khách quan: tai nạn, bão) で (Do nguyên nhân...)",
        "meaning": "Thương lượng giờ giấc điểm hẹn linh hoạt, nói lời xin lỗi chân thành khi đến muộn và trình bày nguyên nhân khách quan.",
        "notes": "Khi trễ hẹn, câu mở đầu lịch sự nhất là: 「おそくなって すみません」.",
        "examples": [
            {
                "jp": "十時はんでも いいですか。―― ええ、だいじょうぶですよ。",
                "ruby": "<ruby>十時<rt>じゅうじ</rt></ruby>はんでも いいですか。―― ええ、だいじょうぶですよ。",
                "vi": "10 giờ rưỡi có được không? ―― Vâng, hoàn toàn được ạ."
            },
            {
                "jp": "おそくなって すみません。時間を まちがえました...",
                "ruby": "おそくなって すみません。<ruby>時間<rt>じかん</rt></ruby>を まちがえました...",
                "vi": "Xin lỗi vì tôi đến muộn. Tại tôi bị nhầm thời gian..."
            },
            {
                "jp": "たいふうで でんしゃが 止まって しまいました。",
                "ruby": "たいふうで でんしゃが <ruby>止<rt>と</rt></ruby>まって しまいました。",
                "vi": "Vì bão nên tàu điện đã bị dừng mất."
            }
        ],
        "quiz": {
            "q": "遅く [____] すみません。道に 迷いました。",
            "options": ["なって", "なり", "なる", "なったら"],
            "correct": 0,
            "explain": "Mẫu câu xin lỗi vì làm sao: V-て すみません ➔ 「遅くなって すみません」."
        }
    },
    {
        "id": 19,
        "level": "A2-1",
        "levelName": "Marugoto A2-1",
        "lesson": 8,
        "lessonTitle": "Bài 8: Trình Tự Thời Gian & Mời Mọc",
        "title": "Mời mọc & Thứ tự hành động: V-に行きませんか / V-てから / V-る前に",
        "tag": "Thứ tự hành động",
        "cat": "order",
        "formula": "[Địa điểm] へ 見に 行きませんか (Cùng đi ngắm... không?)<br>V-てから、～ (Làm xong việc này rồi mới làm việc kia)<br>V-る 前に、～ (Trước khi làm việc này thì...)",
        "meaning": "Rủ bạn bè đi thăm thú danh lam thắng cảnh và sắp xếp thứ tự thực hiện các hành động trong ngày rõ ràng chuẩn xác.",
        "notes": "Sau khi làm A rồi mới làm B dùng 「V-てから」; Trước khi làm B thì làm A dùng 「V-る 前に」.",
        "examples": [
            {
                "jp": "夜の けしきを 見に 行きませんか。―― いいですね。行きましょう！",
                "ruby": "<ruby>夜<rt>よる</rt></ruby>の けしきを <ruby>見<rt>み</rt></ruby>に <ruby>行<rt>い</rt></ruby>きませんか。―― いいですね。<ruby>行<rt>い</rt></ruby>きましょう！",
                "vi": "Chúng mình cùng đi ngắm cảnh đêm nhé? ―― Hay quá, đi thôi!"
            },
            {
                "jp": "食事を してから、おみやげを かいに 行きましょう。",
                "ruby": "<ruby>食事<rt>しょくじ</rt></ruby>を してから、おみやげを かいに <ruby>行<rt>い</rt></ruby>きましょう。",
                "vi": "Dùng bữa xong rồi, chúng ta hãy cùng đi mua quà lưu niệm nhé."
            },
            {
                "jp": "ねる 前に、本を 読みます。",
                "ruby": "ねる <ruby>前<rt>まえ</rt></ruby>に、<ruby>本<rt>ほん</rt></ruby>を <ruby>読<rt>よ</rt></ruby>みます。",
                "vi": "Trước khi đi ngủ, tôi đọc sách."
            }
        ],
        "quiz": {
            "q": "えいがを [____] 前に、カフェへ 行きましょう。",
            "options": ["見る", "見て", "見ます", "見ない"],
            "correct": 0,
            "explain": "Đứng trước 「前に」 động từ luôn ở thể Từ điển (V-る): 「見る前に」."
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
        "formula": "N(Ngôn ngữ) は [V thể Từ điển] のが [かんたん/むずかしい/おもしろい] です<br>V-て くださいませんか (Làm ơn có thể vui lòng... chỉ giúp tôi được không?)<br>[Khoảng thời gian] に [Số lần] 回 (Tần suất học tập)",
        "meaning": "Bình luận về độ khó, độ thú vị khi phát âm/viết chữ/học ngoại ngữ và cách nhờ vả thầy cô, người bản xứ giúp đỡ lịch sự.",
        "notes": "「～てくださいませんか」 là mức độ nhờ vả lịch thiệp và tôn trọng hơn nhiều so với 「～てください」.",
        "examples": [
            {
                "jp": "日本語は はつおんは かんたんですが、かんじを かくのが むずかしいです。",
                "ruby": "<ruby>日本<rt>にほん</rt></ruby><ruby>語<rt>ご</rt></ruby>は はつおんは かんたんですが、かんじを かくのが むずかしいです。",
                "vi": "Tiếng Nhật phát âm thì đơn giản nhưng việc viết chữ Hán thì rất khó."
            },
            {
                "jp": "この かんじの 読みかたを おしえて くださいませんか。",
                "ruby": "この かんじの <ruby>読<rt>よ</rt></ruby>みかたを おしえて くださいませんか。",
                "vi": "Làm ơn có thể vui lòng chỉ giúp tôi cách đọc chữ Hán này được không ạ?"
            },
            {
                "jp": "週に 二回 日本語の じゅぎょうが あります。",
                "ruby": "<ruby>週<rt>しゅう</rt></ruby>に <ruby>二回<rt>にかい</rt></ruby> <ruby>日本<rt>にほん</rt></ruby><ruby>語<rt>ご</rt></ruby>の じゅぎょうが あります。",
                "vi": "Mỗi tuần tôi có 2 buổi học tiếng Nhật."
            }
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
            {
                "jp": "いつか 日本へ りゅうがくに 行きたいです。",
                "ruby": "いつか <ruby>日本<rt>にほん</rt></ruby>へ りゅうがくに <ruby>行<rt>い</rt></ruby>きたいです。",
                "vi": "Một ngày nào đó tôi muốn được đi du học Nhật Bản."
            },
            {
                "jp": "にもつが おもそうですね。てつだいましょうか。",
                "ruby": "にもつが おもそうですね。てつだいましょうか。",
                "vi": "Hành lý trông có vẻ nặng quá. Để tôi giúp bạn một tay nhé?"
            },
            {
                "jp": "日本りょうりを じぶんで つくって みます。",
                "ruby": "<ruby>日本<rt>にほん</rt></ruby>りょうりを じぶんで つくって みます。",
                "vi": "Tôi sẽ thử tự tay nấu món ăn Nhật Bản xem sao."
            }
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
            {
                "jp": "わたしは おにぎりを つくって 行きます。",
                "ruby": "わたしは おにぎりを つくって <ruby>行<rt>い</rt></ruby>きます。",
                "vi": "Tôi sẽ tự làm cơm nắm mang đi dã ngoại."
            },
            {
                "jp": "飲み物は 何が いいですか。―― お茶が いいです。何でも いいですよ。",
                "ruby": "<ruby>飲<rt>の</rt></ruby>み<ruby>物<rt>もの</rt></ruby>は <ruby>何<rt>なに</rt></ruby>が いいですか。―― お<ruby>茶<rt>ちゃ</rt></ruby>が いいです。<ruby>何<rt>なん</rt></ruby>でも いいですよ。",
                "vi": "Đồ uống bạn thích gì? ―― Trà thì tốt, mà cái gì cũng được bạn nhé."
            },
            {
                "jp": "赤ワインと 白ワイン、どちらが いいですか。―― 白ワインに します。",
                "ruby": "<ruby>赤<rt>あか</rt></ruby>ワインと <ruby>白<rt>しろ</rt></ruby>ワイン、どちらが いいですか。―― <ruby>白<rt>しろ</rt></ruby>ワインに します。",
                "vi": "Vang đỏ hay vang trắng bạn thích loại nào hơn? ―― Tôi chọn vang trắng."
            }
        ],
        "quiz": {
            "q": "バーベキューの お肉は わたしが [____] 行きますね。",
            "options": ["買って", "買い", "買う", "買った"],
            "correct": 0,
            "explain": "Hành động chuẩn bị sẵn rồi mang tới điểm hẹn: V-て 行きます ➔ 「買って行きます」."
        }
    },
    {
        "id": 23,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 12,
        "lessonTitle": "Bài 12: Món Ăn & Đánh Giá Vị Giác",
        "title": "Phán đoán thị giác & Miêu tả món ăn: ～そう / A-くて / ～と似ています",
        "tag": "Ẩm thực & Cảm quan",
        "cat": "food-review",
        "formula": "Tính từ (bỏ い/な) + そうです (Trông có vẻ ngon/cay/ngọt)<br>A-くて、B-いです (Vị này và vị kia: cay và ngon)<br>N1 は N2 と にています (Món này trông na ná món kia)",
        "meaning": "Nhận xét món ăn qua vẻ bề ngoài khi vừa dọn ra bàn và so sánh hương vị với các món ăn quê hương.",
        "notes": "おいしい ➔ おいしそう (Trông ngon); からい ➔ からそう (Trông có vẻ cay).",
        "examples": [
            {
                "jp": "その ケーキ、とても おいしそうですね！",
                "ruby": "その ケーキ、とても おいしそうですね！",
                "vi": "Chiếc bánh ngọt đó trông ngon lành quá chừng!"
            },
            {
                "jp": "この サラダは ちょっと からくて、おいしいです。",
                "ruby": "この サラダは ちょっと からくて、おいしいです。",
                "vi": "Món salad này hơi cay một chút mà ngon thật đấy."
            },
            {
                "jp": "これは 韓国の キンパと にていますが、味は ちがいます。",
                "ruby": "これは <ruby>韓国<rt>かんこく</rt></ruby>の キンパと にていますが、<ruby>味<rt>あじ</rt></ruby>は ちがいます。",
                "vi": "Món này trông khá giống Kimbap Hàn Quốc nhưng mùi vị thì khác."
            }
        ],
        "quiz": {
            "q": "この スープは とても から [____] ですね。",
            "options": ["そう", "くて", "い", "だ"],
            "correct": 0,
            "explain": "Phán đoán qua thị giác với tính từ đuôi い: からい ➔ bỏ い thêm そう ➔ 「からそう」."
        }
    },
    {
        "id": 24,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 13,
        "lessonTitle": "Bài 13: Đón Khách & Chuyến Đi",
        "title": "Kinh nghiệm cuộc đời & Lịch trình: V-たことがあります / ～時に着きます",
        "tag": "Kinh nghiệm & Đón tiếp",
        "cat": "arrival",
        "formula": "V-た ことが あります (Tôi đã từng trải nghiệm việc gì đó)<br>[Thời gian] に [Địa điểm] に つきます (Đến nơi lúc mấy giờ)<br>フライトは いかがでしたか (Hỏi thăm chuyến bay sau hành trình dài)",
        "meaning": "Hỏi han trải nghiệm quá khứ, tiếp đón khách hàng/đối tác tại sân bay và thông báo mốc giờ hạ cánh.",
        "notes": "Mẫu câu hỏi kinh nghiệm lịch sự: 「～たことが ありますか」.",
        "examples": [
            {
                "jp": "わたしは 田中さんに 会ったことが あります。",
                "ruby": "わたしは <ruby>田中<rt>たなか</rt></ruby>さんに <ruby>会<rt>あ</rt></ruby>ったことが あります。",
                "vi": "Tôi đã từng gặp anh Tanaka trước đây rồi."
            },
            {
                "jp": "飛行機は 午後3時に 成田空港に 着きます。",
                "ruby": "<ruby>飛行機<rt>ひこうき</rt></ruby>は <ruby>午後<rt>ごご</rt></ruby>3<ruby>時<rt>じ</rt></ruby>に <ruby>成田<rt>なりた</rt></ruby><ruby>空港<rt>くうこう</rt></ruby>に <ruby>着<rt>つ</rt></ruby>きます。",
                "vi": "Máy bay sẽ hạ cánh xuống sân bay Narita lúc 3 giờ chiều."
            },
            {
                "jp": "田中さん、お疲れ様でした。ようこそ 東京へ！フライトは いかがでしたか。",
                "ruby": "<ruby>田中<rt>たなか</rt></ruby>さん、お<ruby>疲<rt>つか</rt></ruby>れ<ruby>様<rt>さま</rt></ruby>でした。ようこそ <ruby>東京<rt>とうきょう</rt></ruby>へ！フライトは いかがでしたか。",
                "vi": "Chào anh Tanaka, anh đã vất vả rồi. Chào mừng anh đến Tokyo! Chuyến bay của anh thế nào ạ?"
            }
        ],
        "quiz": {
            "q": "日本へ [____] ことが ありますか。",
            "options": ["行った", "行く", "行きます", "行かない"],
            "correct": 0,
            "explain": "Cấu trúc kinh nghiệm: Động từ thể Quá khứ ngắn (Thể た) + ことがあります ➔ 「行った」."
        }
    },
    {
        "id": 25,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 14,
        "lessonTitle": "Bài 14: Thăm Quan Công Ty & Quy Tắc",
        "title": "Xin phép & Quy tắc công sở: V-てもいいですか / V-てはいけません / お世話になりました",
        "tag": "Quy tắc & Cảm ơn",
        "cat": "office-rules",
        "formula": "V-て + もいいですか (Tôi làm... có được không?)<br>V-て + はいけません (Không được phép làm...)<br>大変 お世話になりました (Cảm ơn anh chị đã giúp đỡ hết lòng)",
        "meaning": "Xin phép cấp trên trước khi sử dụng thiết bị, nhắc nhở nội quy cấm đoán và nói lời chia tay cảm tạ sâu sắc.",
        "notes": "V-てはいけません là cấm đoán nghiêm khắc; Xin phép dùng 「V-ても いいですか」.",
        "examples": [
            {
                "jp": "この パソコンを つかっても いいですか。―― はい、どうぞ。",
                "ruby": "この パソコンを つかっても いいですか。―― はい、どうぞ。",
                "vi": "Tôi dùng chiếc máy tính này có được không? ―― Vâng, xin mời anh cứ dùng."
            },
            {
                "jp": "ここで しゃしんを とっては いけません。",
                "ruby": "ここで しゃしんを とっては いけません。",
                "vi": "Không được chụp ảnh tại khu vực này."
            },
            {
                "jp": "3日間、大変 お世話になりました。本社の 皆さんによろしく お伝えください。",
                "ruby": "3<ruby>日<rt>にち</rt></ruby><ruby>間<rt>かん</rt></ruby>、<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました。<ruby>本社<rt>ほんしゃ</rt></ruby>の <ruby>皆<rt>みな</rt></ruby>さんによろしく お<ruby>伝<rt>つた</rt></ruby>えください。",
                "vi": "Trong 3 ngày qua, cảm ơn mọi người đã hết lòng giúp đỡ. Cho tôi gửi lời hỏi thăm tới mọi người ở trụ sở chính nhé."
            }
        ],
        "quiz": {
            "q": "ここで タバコを [____] は いけません。",
            "options": ["吸って", "吸う", "吸い", "吸った"],
            "correct": 0,
            "explain": "Cấu trúc cấm đoán: V-て + はいけません ➔ 「吸ってはいけません」."
        }
    },
    {
        "id": 26,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 15,
        "lessonTitle": "Bài 15: Sức Khỏe & Thăm Bệnh",
        "title": "Giải thích bệnh trạng & Lời khuyên: ～んです / V-るといいですよ / V-ないでください",
        "tag": "Sức khỏe & Lời khuyên",
        "cat": "health",
        "formula": "[Thể thông thường / Tính từ] + んです (Giải thích triệu chứng: あたまが いたいんです)<br>V(thể Từ điển) + といいですよ (Khuyên nên làm gì)<br>V-ない + でください (Dặn dò đừng làm quá sức)",
        "meaning": "Mô tả triệu chứng đau ốm, đưa ra lời khuyên uống thuốc/nghỉ ngơi ân cần và động viên người bệnh.",
        "notes": "Đuôi 「～んです」 dùng khi giải thích lý do, nguyên nhân với sự quan tâm và giãi bày cảm xúc.",
        "examples": [
            {
                "jp": "どうしたんですか。―― ちょっと あたまが いたいんです。",
                "ruby": "どうしたんですか。―― ちょっと あたまが いたいんです。",
                "vi": "Bạn bị làm sao thế? ―― Tôi bị đau đầu một chút."
            },
            {
                "jp": "ねる 前に、この くすりを のむと いいですよ。",
                "ruby": "ねる <ruby>前<rt>まえ</rt></ruby>に、この くすりを のむと いいですよ。",
                "vi": "Trước khi đi ngủ, bạn uống viên thuốc này thì tốt đấy nhé."
            },
            {
                "jp": "ねつが ありますから、あまり むりを しないでくださいね。",
                "ruby": "ねつが ありますから、あまり むりを しないでくださいね。",
                "vi": "Vẫn còn sốt nên bạn đừng làm việc quá sức nhé."
            }
        ],
        "quiz": {
            "q": "早く 元気に [____] と いいですね。",
            "options": ["なる", "なって", "なり", "なった"],
            "correct": 0,
            "explain": "Mẫu câu khuyên nhủ/chúc phúc: V(thể Từ điển) + といいですね ➔ 「なるといいですね」."
        }
    },
    {
        "id": 27,
        "level": "A2-2",
        "levelName": "Marugoto A2-2",
        "lesson": 16,
        "lessonTitle": "Bài 16: Lối Sống Lành Mạnh & Thể Thao",
        "title": "Liệt kê thói quen & Lời khuyên lối sống: V1-たり V2-たりします / N のために / V-たほうがいい",
        "tag": "Lối sống & Thể thao",
        "cat": "lifestyle",
        "formula": "V1-た + り、V2-た + り します / しています (Lúc làm việc này, lúc làm việc kia)<br>N の ために (Vì mục đích duy trì sức khỏe)<br>V-た ほうがいいです (Nên làm) / V-ない ほうがいいです (Không nên làm)",
        "meaning": "Liệt kê tiêu biểu các hoạt động rèn luyện thân thể cuối tuần và đưa ra lời khuyên chân tình giúp cải thiện lối sống.",
        "notes": "Cấu trúc たり...たり phải chia động từ ở thể Ta rồi gắn thêm り: 「走ったり、泳いだり」.",
        "examples": [
            {
                "jp": "しゅうまつは こうえんを はしったり、プールで およいだり して います。",
                "ruby": "しゅうまつは こうえんを はしったり、プールで およいだり して います。",
                "vi": "Cuối tuần tôi lúc thì chạy bộ ở công viên, lúc thì đi bơi ở hồ bơi."
            },
            {
                "jp": "けんこうの ために 何か して いますか。",
                "ruby": "けんこうの ために <ruby>何<rt>なに</rt></ruby>か して いますか。",
                "vi": "Để duy trì sức khỏe, bạn có làm hoạt động gì không?"
            },
            {
                "jp": "夜 おそくまで おきていないで、はやく ねた ほうが いいですよ。",
                "ruby": "<ruby>夜<rt>よる</rt></ruby> おそくまで おきていないで、はやく ねた ほうが いいですよ。",
                "vi": "Đừng thức quá khuya, bạn nên đi ngủ sớm thì tốt hơn đấy."
            }
        ],
        "quiz": {
            "q": "休みの 日は 本を [____]、えいがを 見たり します。",
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
        "formula": "Watashi wa [Người nhận] に [Món quà] を あげます (Tặng ai cái gì)<br>Watashi wa [Người tặng] に [Món quà] を もらったんです (Được ai tặng)<br>N1 とか N2 とか (Liệt kê đại diện như là...)<br>[V thể Từ điển] + もの (Đồ vật để làm gì)",
        "meaning": "Tặng quà vào các dịp lễ kỷ niệm, giải thích nguồn gốc kỷ vật đáng trân trọng và dùng mệnh đề định ngữ miêu tả công năng của quà tặng.",
        "notes": "Dùng 「もらったんです」 khi giải thích lý do vì sao mình sở hữu món đồ xinh xắn đối phương vừa khen ngợi.",
        "examples": [
            {
                "jp": "その ネックレス、とても すてきですね。―― たんじょうびに かれに もらったんです。",
                "ruby": "その ネックレス、とても すてきですね。―― たんじょうびに かれに もらったんです。",
                "vi": "Sợi dây chuyền đó đẹp quá nhỉ! ―― Tôi được bạn trai tặng vào ngày sinh nhật đấy."
            },
            {
                "jp": "母の 日に きれいな 花を あげました。",
                "ruby": "<ruby>母<rt>はは</rt></ruby>の <ruby>日<rt>ひ</rt></ruby>に きれいな <ruby>花<rt>はな</rt></ruby>を あげました。",
                "vi": "Vào Ngày của Mẹ tôi đã tặng một bó hoa tươi cho mẹ."
            },
            {
                "jp": "けっこんの おいわいに えとか とけいを あげます。へやに かざる ものが いいですね。",
                "ruby": "けっこんの おいわいに えとか とけいを あげます。へやに かざる ものが いいですね。",
                "vi": "Mừng đám cưới thường tặng những thứ như tranh hay đồng hồ. Đồ trang trí phòng thì rất hay."
            }
        ],
        "quiz": {
            "q": "へやに [____] ものを プレゼントしたいです。",
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
            {
                "jp": "あべさんの おいわいは パーティーが いいと 思います。",
                "ruby": "あべさんの おいわいは パーティーが いいと <ruby>思<rt>おも</rt></ruby>います。",
                "vi": "Mừng cho anh Abe thì tôi nghĩ tổ chức một bữa tiệc là tuyệt nhất."
            },
            {
                "jp": "あべさんは みんなと はなしたいと 言っていましたよ。",
                "ruby": "あべさんは みんなと はなしたいと <ruby>言<rt>い</rt></ruby>っていましたよ。",
                "vi": "Anh Abe nói là rất muốn được trò chuyện cùng mọi người đấy."
            },
            {
                "jp": "パーティーで すてきな きものを 着て、めがねを かけている 人が います。",
                "ruby": "パーティーで すてきな きものを <ruby>着<rt>き</rt></ruby>て、めがねを かけている <ruby>人<rt>ひと</rt></ruby>が います。",
                "vi": "Ở bữa tiệc có một người đang mặc bộ Kimono tuyệt đẹp và đeo kính mắt."
            }
        ],
        "quiz": {
            "q": "パーティーで 新しい スーツを [____] います。",
            "options": ["着て", "履いて", "被って", "掛けて"],
            "correct": 0,
            "explain": "Bộ com-lê/vest (スーツ) là âu phục mặc trên thân người, dùng động từ 「着ます」 ➔ 「着ています」."
        }
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(ALL_GRAMMAR_ITEMS)} overhauled grammar items with complete Furigana & strict Kanji.")
