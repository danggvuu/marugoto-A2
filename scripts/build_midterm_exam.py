#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for tests/De_Thi_Midterm_A2_1.html
Chuẩn format đề thi giữa kỳ Midterm Marugoto A2-1 theo đúng bảng lớp học:
- Phần 1: Từ vựng (( ) & Câu đồng nghĩa)
- Phần 2: Kanji (Kanji->Hira & Hira->Kanji)
- Phần 3: Ngữ pháp (( ), Hái sao ☆, Dịch câu)
- Phần 4: Đọc hiểu (2 câu TN)
- Phần 5: Tự luận (Trả lời câu hỏi: 2 câu)
"""

import json

EXAMS_DATA = [
    {
        "code": "M102",
        "name": "Mã Đề M102 (Đề Trọng Tâm Chuẩn Bảng Lớp)",
        "tag": "⭐ Trọng Tâm Bài 5 - 8 • Đề Bảng Thầy Cô",
        "desc": "Bám sát 100% cấu trúc 5 phần trên bảng lớp học: Từ vựng (Điền từ + Đồng nghĩa), Kanji (2 chiều), Ngữ pháp (Điền từ + Hái sao ☆ + Dịch câu), Đọc hiểu thực tế (2 câu TN), Tự luận Can-do (2 câu).",
        "timeLimit": 45 * 60, # 45 minutes
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu có ý nghĩa tương đương / đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": "駅を 出て、まっすぐ 行くと、右側に 郵便局が (   )。",
                                "promptVi": "Ra khỏi ga, đi thẳng thì ở phía bên phải có bưu điện.",
                                "options": ["あります", "います", "します", "おきます"],
                                "correct": 0,
                                "explain": "郵便局 (ゆうびんきょく - bưu điện) là đồ vật vô tri vô giác, đi với động từ tồn tại あります. (いません dùng cho người/động vật). Ngữ pháp chỉ đường Bài 5."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": "この ラーメンは (   ) ですから、水が たくさん いります。",
                                "promptVi": "Món mì ramen này cay nên cần nhiều nước.",
                                "options": ["あまい", "からい", "すっぱい", "にがい"],
                                "correct": 1,
                                "explain": "からい (cay) nên mới cần uống nhiều nước (水が たくさん いります). あまい = ngọt, すっぱい = chua, にがい = đắng. Từ vựng Bài 6."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": "日曜日、公園で (   ) が ありますから、友だちと 見に 行きます。",
                                "promptVi": "Chủ nhật ở công viên có sự kiện nên tôi đi xem cùng bạn bè.",
                                "options": ["イベント", "スケジュール", "マナー", "ルール"],
                                "correct": 0,
                                "explain": "イベント (event - sự kiện, lễ hội). Ngữ cảnh đi xem cùng bạn bè thì イベント (sự kiện) là chính xác nhất. Bài 7."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": "日本へ 来てから、もう 3年 (   ) に なります。",
                                "promptVi": "Kể từ khi đến Nhật thì đã được khoảng 3 năm rồi.",
                                "options": ["だけ", "ぐらい", "より", "ほど"],
                                "correct": 1,
                                "explain": "Số từ + ぐらい (khoảng chừng). Mẫu câu nói về khoảng thời gian đã trôi qua. だけ = chỉ, より = hơn."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": "すみません、メニューを (   ) ください。",
                                "promptVi": "Xin lỗi, xin hãy cho tôi xem thực đơn.",
                                "options": ["わたって", "みせて", "まがって", "あいて"],
                                "correct": 1,
                                "explain": "見せて ください (みせてください) = hãy cho tôi xem. わたって = băng qua đường, まがって = rẽ, あいて = mở. Hội thoại gọi món Bài 6."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu hoặc từ đồng nghĩa",
                        "groupInstruction": "Chọn câu (A, B, C, D) có ý nghĩa tương đương gần nhất với câu hoặc cụm từ được gạch chân:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": "この レストランは いつも <span class='hl-kw'>こんで います</span>。",
                                "promptVi": "Nhà hàng này lúc nào cũng đông đúc.",
                                "options": [
                                    "人が たくさん います。",
                                    "人が ぜんぜん いません。",
                                    "店が とても ひろい です。",
                                    "料理が とても まずい です。"
                                ],
                                "correct": 0,
                                "explain": "こんで います (混んでいます) nghĩa là đông nghẹt, chen chúc = 人が たくさん います (có rất đông người)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": "わたしは <span class='hl-kw'>ときどき</span> 日本料理を 作ります。",
                                "promptVi": "Tôi thỉnh thoảng nấu món ăn Nhật.",
                                "options": [
                                    "毎日 いつも 作ります。",
                                    "たまに 作りますが、毎日ではありません。",
                                    "一度も 作ったことが ありません。",
                                    "これから 作る つもりです。"
                                ],
                                "correct": 1,
                                "explain": "ときどき (thỉnh thoảng, đôi khi) đồng nghĩa với たまに (thỉnh thoảng), chỉ tần suất không thường xuyên."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": "田中さんは 今 <span class='hl-kw'>手が はなせません</span>。",
                                "promptVi": "Anh Tanaka hiện tại đang không dứt tay ra được (rất bận).",
                                "options": [
                                    "手を 洗って います。",
                                    "今 とても いそがしくて、他のことが できません。",
                                    "手が 痛くて 動きません。",
                                    "手袋を ぬいで います。"
                                ],
                                "correct": 1,
                                "explain": "手が離せない (手がはなせません) là quán dụng ngữ thông dụng trong giao tiếp và công sở, mang nghĩa 'đang bận làm dở việc, không thể dứt tay làm việc khác'."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": "駅の まえに <span class='hl-kw'>こうばん</span>が あります。",
                                "promptVi": "Trước nhà ga có đồn cảnh sát.",
                                "options": [
                                    "けいさつかんが いる 所",
                                    "電車や バスを 待つ 所",
                                    "薬を 買う 所",
                                    "本を 借りる 所"
                                ],
                                "correct": 0,
                                "explain": "こうばん (交番 - Đồn cảnh sát) = けいさつかんが いる 所 (nơi có cảnh sát thường trực). Bài 5."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": "母に <span class='hl-kw'>すてきな</span> プレゼントを あげました。",
                                "promptVi": "Tôi đã tặng mẹ một món quà rất tuyệt vời.",
                                "options": [
                                    "とても いい",
                                    "とても からい",
                                    "とても おもい",
                                    "とても わるい"
                                ],
                                "correct": 0,
                                "explain": "すてきな (tuyệt vời, đẹp, đáng yêu) = とても いい (rất tốt/rất đẹp). Bài 8."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán ra Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20).",
                "badge": "20 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Kanji ➔ Hiragana (Chọn cách đọc đúng)",
                        "groupInstruction": "Chọn cách đọc Hiragana đúng cho chữ Hán được gạch chân:",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": "週末、友だちと 神社で <span class='hl-kw'>祭り</span>を 見ました。",
                                "promptVi": "Cuối tuần, tôi đã xem lễ hội ở đền thờ cùng bạn bè.",
                                "options": ["まつり", "まち", "おどり", "はなび"],
                                "correct": 0,
                                "explain": "「祭り」 đọc là まつり (Lễ hội - Bài 7). Chú ý không nhầm với 町 (まち - phố) hay 花火 (はなび - pháo hoa)."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": "デパートで <span class='hl-kw'>新しい</span> かばんを 買いました。",
                                "promptVi": "Tôi đã mua một chiếc túi xách mới ở trung tâm thương mại.",
                                "options": ["ふるい", "あたらしい", "うつくしい", "おもしろい"],
                                "correct": 1,
                                "explain": "「新しい」 đọc là あたらしい (Mới). Từ trái nghĩa là 古い (ふるい - cũ)."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": "あの 角を <span class='hl-kw'>右</span>へ まがって ください。",
                                "promptVi": "Xin hãy rẽ phải ở góc ngã tư đằng kia.",
                                "options": ["ひだり", "みぎ", "まえ", "うしろ"],
                                "correct": 1,
                                "explain": "「右」 đọc là みぎ (Bên phải - Bài 5). Bên trái là 左 (ひだり)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": "ベトナムの <span class='hl-kw'>料理</span>は とても おいしいです。",
                                "promptVi": "Món ăn Việt Nam rất ngon.",
                                "options": ["りょうり", "りょこう", "りゆう", "りょうしん"],
                                "correct": 0,
                                "explain": "「料理」 đọc là りょうり (Món ăn, ẩm thực - Bài 6). 旅行 = りょこう (du lịch), 理由 = りゆう (lý do)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": "夏休みに 家族と <span class='hl-kw'>海</span>へ 行きました。",
                                "promptVi": "Kỳ nghỉ hè tôi đã đi biển cùng gia đình.",
                                "options": ["やま", "かわ", "うみ", "いけ"],
                                "correct": 2,
                                "explain": "「海」 đọc là うみ (Biển). 山 = やま (núi), 川 = かわ (sông), 池 = いけ (ao)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Hiragana ➔ Kanji (Chọn chữ Hán đúng)",
                        "groupInstruction": "Chọn chữ Hán tương ứng chính xác với từ Hiragana gạch chân:",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": "あしたの 朝 8時に 駅で <span class='hl-kw'>あいます</span>。",
                                "promptVi": "Sáng mai lúc 8 giờ gặp nhau ở nhà ga nhé.",
                                "options": ["会います", "合います", "開きます", "見ます"],
                                "correct": 0,
                                "explain": "あいます (gặp gỡ) là chữ Hán「会」➔ 会います. 合います là vừa/hợp, 開きます là mở."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": "この 道を まっすぐ <span class='hl-kw'>いって</span> ください。",
                                "promptVi": "Xin hãy đi thẳng con đường này.",
                                "options": ["行って", "来て", "待って", "帰って"],
                                "correct": 0,
                                "explain": "いって (đi) là chữ Hán「行」➔ 行って. 来て là đến, 待って là chờ, 帰って là về."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": "あの <span class='hl-kw'>みせ</span>で おいしい パンを 売っています。",
                                "promptVi": "Ở cửa hàng đằng kia đang bán bánh mì rất ngon.",
                                "options": ["駅", "店", "車", "門"],
                                "correct": 1,
                                "explain": "みせ (cửa hàng/tiệm) là chữ Hán「店」. 駅 là nhà ga, 車 là xe hơi, 門 là cổng."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": "外国の 言葉を <span class='hl-kw'>ならって</span> います。",
                                "promptVi": "Tôi đang học ngoại ngữ.",
                                "options": ["習って", "買って", "売って", "知って"],
                                "correct": 0,
                                "explain": "ならって (học/luyện tập) là chữ Hán「習」➔ 習って (習います). 買 = mua, 売 = bán, 知 = biết."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": "ここは とても しずかな <span class='hl-kw'>まち</span> です。",
                                "promptVi": "Nơi đây là một khu phố/thị trấn rất yên tĩnh.",
                                "options": ["道", "町", "川", "寺"],
                                "correct": 1,
                                "explain": "まち (thị trấn, phố xá) là chữ Hán「町」. 道 = con đường, 川 = dòng sông, 寺 = ngôi chùa."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Gồm 3 dạng bài: Điền khuyết trợ từ/thể (21-26), Sắp xếp câu Hái sao ☆ (27-30), Dịch câu Tự luận (31-32).",
                "badge": "30 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn trợ từ hoặc dạng chia ngữ pháp đúng nhất điền vào (   ):",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": "すみません、市役所へ 行く 道を 教えて (   ) か。",
                                "promptVi": "Xin lỗi, bạn có thể chỉ giúp tôi đường đi đến ủy ban thành phố được không?",
                                "options": ["もらえません", "あげません", "しません", "なりません"],
                                "correct": 0,
                                "explain": "～て もらえませんか: Mẫu câu nhờ vả đối phương giúp đỡ một cách lịch sự (Bài 5). Không dùng あげません hay しません."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": "ここで たばこを (   ) は いけません。",
                                "promptVi": "Không được hút thuốc ở đây.",
                                "options": ["すって", "すう", "すいた", "すいます"],
                                "correct": 0,
                                "explain": "Động từ thể Te + は いけません: Mẫu câu cấm đoán quy tắc/nội quy. 吸います (nhóm 1) chuyển sang thể Te là 吸って (すって)."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": "わたしは 納豆を 食べる (   ) が できません。",
                                "promptVi": "Tôi không thể ăn được món natto.",
                                "options": ["の", "こと", "もの", "とき"],
                                "correct": 1,
                                "explain": "Động từ thể từ điển (V-ru) + ことが できます/できません: Mẫu câu biểu thị khả năng (Bài 3-4)."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": "交差点を 渡って (   )、銀行が 見えます。",
                                "promptVi": "Sau khi băng qua ngã tư thì sẽ nhìn thấy ngân hàng.",
                                "options": ["から", "まで", "より", "ながら"],
                                "correct": 0,
                                "explain": "V-te + から: Hành động sau khi làm V1 thì làm/xảy ra V2 (Bài 5: chỉ đường liên hoàn). Không dùng ながら (vừa... vừa) hay まで."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": "あの レストランの 料理は おいしい (   )、安いです。",
                                "promptVi": "Món ăn của nhà hàng kia vừa ngon lại vừa rẻ.",
                                "options": ["し", "が", "でも", "から"],
                                "correct": 0,
                                "explain": "Tính từ + し、...し: Liệt kê các tính chất tương đồng hoặc nguyên nhân song song. が và でも mang nghĩa đối lập."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": "暑いですから、窓を 開けて (   ) いいですか。",
                                "promptVi": "Vì trời nóng nên tôi mở cửa sổ có được không?",
                                "options": ["も", "は", "が", "を"],
                                "correct": 0,
                                "explain": "V-te + も いいですか: Mẫu câu xin phép làm một hành động nào đó. (Trái ngược với ては いけません)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: ☆ Hái sao (Sắp xếp cụm từ vào đúng vị trí)",
                        "groupInstruction": "Sắp xếp 4 cụm từ [1, 2, 3, 4] vào 4 vị trí trống để tạo thành câu hoàn chỉnh, sau đó chọn số tương ứng với vị trí ngôi sao ★:",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "sentencePre": "すみません、駅へ",
                                "sentencePost": "いいですか。",
                                "promptVi": "Xin lỗi, để đi đến nhà ga thì đi bằng xe buýt như thế nào thì được ạ?",
                                "parts": [
                                    {"id": 1, "text": "行けば"},
                                    {"id": 2, "text": "どうやって"},
                                    {"id": 3, "text": "行くには"},
                                    {"id": 4, "text": "バスで"}
                                ],
                                "fullOrder": [3, 4, 2, 1],
                                "starPos": 3, # 1-based position of star in the 4 slots: slot 1, slot 2, slot 3 (★), slot 4
                                "correctOption": 2, # part id at star position: part 2 "どうやって"
                                "fullSentence": "すみません、駅へ 行くには バスで ★どうやって 行けば いいですか。",
                                "explain": "Thứ tự sắp xếp chuẩn: 駅へ [3. 行くには] [4. バスで] ★[2. どうやって] [1. 行けば] いいですか。Vị trí ngôi sao ★ ở vị trí thứ 3 là cụm (2) どうやって."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "sentencePre": "この 料理は",
                                "sentencePost": "おいしいですよ。",
                                "promptVi": "Món ăn này vì hơi cay một chút nên bạn ăn thử xem, ngon lắm đấy.",
                                "parts": [
                                    {"id": 1, "text": "から"},
                                    {"id": 2, "text": "ちょっと"},
                                    {"id": 3, "text": "からい"},
                                    {"id": 4, "text": "食べてみて"}
                                ],
                                "fullOrder": [2, 3, 1, 4],
                                "starPos": 3,
                                "correctOption": 1, # part 1 "から"
                                "fullSentence": "この 料理は ちょっと からい ★から 食べてみて おいしいですよ。",
                                "explain": "Thứ tự sắp xếp chuẩn: この 料理は [2. ちょっと] [3. からい] ★[1. から] [4. 食べてみて] おいしいですよ。Cụm từ ở vị trí ★ là (1) から."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "sentencePre": "橋を",
                                "sentencePost": "あります。",
                                "promptVi": "Băng qua cây cầu, hễ đi thẳng thì sẽ có một công viên lớn.",
                                "parts": [
                                    {"id": 1, "text": "わたって"},
                                    {"id": 2, "text": "大きな"},
                                    {"id": 3, "text": "まっすぐ行くと"},
                                    {"id": 4, "text": "公園が"}
                                ],
                                "fullOrder": [1, 3, 2, 4],
                                "starPos": 3,
                                "correctOption": 2, # part 2 "大きな"
                                "fullSentence": "橋を わたって まっすぐ行くと ★大きな 公園が あります。",
                                "explain": "Thứ tự sắp xếp chuẩn: 橋を [1. わたって] [3. まっすぐ行くと] ★[2. 大きな] [4. 公園が] あります。Vị trí ngôi sao ★ chính là tính từ (2) 大きな."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "sentencePre": "休みの日は",
                                "sentencePost": "します。",
                                "promptVi": "Vào ngày nghỉ tôi thường đọc sách và nghe nhạc.",
                                "parts": [
                                    {"id": 1, "text": "本を"},
                                    {"id": 2, "text": "読んだり"},
                                    {"id": 3, "text": "音楽を"},
                                    {"id": 4, "text": "聞いたり"}
                                ],
                                "fullOrder": [1, 2, 3, 4],
                                "starPos": 3,
                                "correctOption": 3, # part 3 "音楽を"
                                "fullSentence": "休みの日は 本を 読んだり ★音楽を 聞いたり します。",
                                "explain": "Thứ tự sắp xếp chuẩn theo mẫu V1-たり、V2-たり します: 休みの日は [1. 本を] [2. 読んだり] ★[3. 音楽を] [4. 聞いたり] します。Vị trí ngôi sao ★ là cụm (3) 音楽を."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu (Tự luận)",
                        "groupInstruction": "Nhập bản dịch vào ô trống (chấp nhận cả Kanji lẫn Hiragana, không phân biệt dấu cách):",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "dir": "vi_to_ja",
                                "prompt": "Dịch sang tiếng Nhật: <br><strong style='color:#1e1b4b;'>「Hãy rẽ phải ở góc ngã tư đằng kia.」</strong>",
                                "placeholder": "Nhập câu tiếng Nhật (Ví dụ: あの かどを 右へ まがって ください)...",
                                "acceptable": [
                                    "あのかどをみぎへまがってください",
                                    "あのかどをみぎにまがってください",
                                    "あのかどを右へ曲がってください",
                                    "あのかどを右に曲がってください",
                                    "あの角を右へ曲がってください",
                                    "あの角を右に曲がってください",
                                    "あの角を右へまがってください",
                                    "あの角を右にまがってください",
                                    "あのかどを右へまがってください",
                                    "あの角をみぎへ曲がってください"
                                ],
                                "standard": "あの かどを 右へ（右に） まがって ください。",
                                "explain": "Cấu trúc chỉ đường: [Địa điểm] を [Hướng] へ/に まがってください (rẽ ở... về hướng...). あの かど (góc kia), 右 (みぎ - phải), 曲がって (まがって - thể Te của 曲がります)."
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "dir": "ja_to_vi",
                                "prompt": "Dịch sang tiếng Việt: <br><strong style='color:#1e1b4b;'>「すみません、この 部屋で 写真を 撮っても いいですか。」</strong>",
                                "placeholder": "Nhập câu dịch tiếng Việt (Ví dụ: Xin lỗi, tôi có thể chụp ảnh trong phòng này được không?)...",
                                "keywords": ["xin lỗi", "chụp ảnh", "được không", "phòng"],
                                "standard": "Xin lỗi, tôi có thể chụp ảnh trong căn phòng này được không? (hoặc: Xin phép tôi chụp ảnh ở phòng này được không?)",
                                "explain": "Cấu trúc xin phép: V-ても いいですか (làm V có được không?). 写真を 撮ります (chụp ảnh) ➔ 写真を 撮っても いいですか."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc bài viết thông báo thực tế dưới đây và chọn đáp án chính xác nhất cho 2 câu hỏi (33 và 34).",
                "badge": "10 Điểm",
                "readingPassage": {
                    "title": "【国際交流（こくさいこうりゅう）フェスティバルの お知らせ】",
                    "content": "来週の 土曜日（11月15日）、市民センターの 2階で「国際交流フェスティバル」が あります。\nいろいろな 国の 料理を 食べたり、伝統的な（でんとうてきな） 音楽を 聞いたり することが できます。\nベトナムの フォーや 日本の たこ焼きの 屋台（やたい）も ありますよ。\n\n時間は 午前10時から 午後4時までです。\n入場（にゅうじょう）は 無料（むりょう）ですが、料理を 食べる ときは チケットが いります。\nチケットは 当日（とうじつ） 受付（うけつけ）で 買うことが できます。\nみなさん、ぜひ 友だちや 家族と 一緒に 来て ください！",
                    "translation": "【Thông Báo Về Lễ Hội Giao Lưu Quốc Tế】\nThứ Bảy tuần tới (ngày 15 tháng 11), tại tầng 2 của Trung tâm giao lưu cư dân thành phố sẽ tổ chức 'Lễ hội giao lưu quốc tế'.\nCác bạn có thể thưởng thức ẩm thực của nhiều quốc gia, lắng nghe âm nhạc truyền thống.\nNgoài ra còn có cả các gian hàng ẩm thực như món Phở của Việt Nam và món bánh Takoyaki của Nhật Bản nữa đấy!\n\nThời gian diễn ra từ 10 giờ sáng đến 4 giờ chiều.\nVào cửa miễn phí, tuy nhiên khi muốn thưởng thức các món ăn thì các bạn cần có phiếu (ticket).\nPhiếu này có thể mua trực tiếp tại quầy lễ tân vào đúng ngày diễn ra sự kiện.\nMời tất cả các bạn hãy cùng gia đình và bạn bè ghé tham gia nhé!"
                },
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": "この フェスティバルで 何を することが できますか。",
                        "promptVi": "Ở lễ hội này mọi người có thể làm những hoạt động gì?",
                        "options": [
                            "いろいろな 国の 料理を 食べたり、音楽を 聞いたり できます。",
                            "無料で すべての 料理を 持ち帰ることが できます。",
                            "市民センターの 映画を 見ることが できます。",
                            "日本語の テストを 無料で 受けることが できます。"
                        ],
                        "correct": 0,
                        "explain": "Đoạn văn ghi rõ: 『いろいろな 国の 料理を 食べたり、伝統的な 音楽を 聞いたり することが できます。』(Có thể thưởng thức đồ ăn nhiều nước và nghe âm nhạc). Phương án A hoàn toàn chính xác."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": "フェスティバルに ついて、正しい ものは どれですか。",
                        "promptVi": "Câu nào dưới đây là ĐÚNG về lễ hội này?",
                        "options": [
                            "チケットは 事前に インターネットで 買わなければ なりません。",
                            "入場料（にゅうじょうりょう）は 1000円 かかります。",
                            "料理を 食べたい ときは、当日 受付で チケットを 買います。",
                            "フェスティバルは 夜の 8時まで やって います。"
                        ],
                        "correct": 2,
                        "explain": "Trong bài ghi rõ: 『入場は 無料ですが、料理を 食べる ときは チケットが いります。チケットは 当日 受付で 買うことが できます。』 (Vào cửa miễn phí, nếu ăn đồ ăn thì mua vé tại bàn lễ tân trong ngày). Do đó phương án C đúng."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (mỗi câu viết từ 2 đến 3 câu hoàn chỉnh).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "休みの日は 何を しますか。どこへ 行きますか。（2〜3文の 日本語で 書いてください）",
                        "promptVi": "Vào ngày nghỉ bạn làm gì? Bạn thường đi đâu? (Hãy viết 2 đến 3 câu bằng tiếng Nhật)",
                        "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: 休みの日は たいてい 家で 映画を 見ます...)...",
                        "hints": [
                            "Gợi ý mẫu câu: ～へ 行きます / ～と 一緒に ～ます",
                            "Mẫu liệt kê hành động: ～たり、～たり します",
                            "Tính từ cảm xúc: とても 楽しいです / 面白いです"
                        ],
                        "modelAnswer": "休みの日は たいてい 家で 映画を 見たり、音楽を 聞いたり します。天気が いい ときは、友だちと 公園へ 行きます。とても 楽しいです。",
                        "modelVi": "Vào ngày nghỉ tôi thường xem phim hoặc nghe nhạc ở nhà. Khi thời tiết đẹp, tôi cùng bạn bè đi dạo công viên. Rất là vui.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Có đủ 2-3 câu văn hoàn chỉnh; sử dụng đúng trợ từ (で, へ, を); chia đúng thể động từ (～ます / ～たりします); diễn đạt mạch lạc tự nhiên."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "あなたの 好きな 料理（日本料理 または ベトナム料理）について 紹介してください。（どんな 料理ですか。どうして 好きですか。2〜3文で 書いてください）",
                        "promptVi": "Hãy giới thiệu về món ăn yêu thích của bạn (món Nhật hoặc món Việt). Đó là món gì? Tại sao bạn thích? (Viết 2-3 câu tiếng Nhật)",
                        "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしは ベトナムの フォーが 大好きです...)...",
                        "hints": [
                            "Món yêu thích: わたしは ～が 好きです / 大好きです",
                            "Miêu tả mùi vị: スープが おいしいです / からいです / あまいです",
                            "Lý do: ～ですから / 体に いいですから"
                        ],
                        "modelAnswer": "わたしは ベトナムの フォーが 大好きです。スープが とても おいしくて、あたたかいです。牛肉や 野菜が たくさん 入って いますから、体に いいです。",
                        "modelVi": "Tôi rất thích món phở của Việt Nam. Nước dùng rất ngon và ấm nóng. Vì có nhiều thịt bò và rau nên rất tốt cho sức khỏe.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Nêu rõ tên món ăn yêu thích; có tính từ miêu tả hương vị đặc trưng; có câu nêu lý do vì sao thích (～から); ngữ pháp chuẩn xác."
                    }
                ]
            }
        ]
    },
    {
        "code": "M101",
        "name": "Mã Đề M101 (Đề Tổng Hợp Toàn Diện A2-1)",
        "tag": "📘 Tổng Hợp Bài 1 - 8 • Đề Thi Khảo Sát",
        "desc": "Bao quát toàn bộ năng lực Marugoto A2-1 từ Bài 1 đến Bài 8: Giới thiệu bản thân, thói quen sinh hoạt, nơi ở, món ăn, lễ hội, phương tiện và chỉ đường.",
        "timeLimit": 45 * 60,
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu có ý nghĩa tương đương / đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": "わたしは 毎朝 7時に (   ) を 飲んでから、会社へ 行きます。",
                                "promptVi": "Mỗi sáng tôi uống cà phê lúc 7 giờ rồi mới đến công ty.",
                                "options": ["コーヒー", "パン", "ごはん", "サンドイッチ"],
                                "correct": 0,
                                "explain": "Động từ là 飲んでから (uống rồi...). Trong 4 phương án chỉ có コーヒー (cà phê) là đồ uống."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": "休みの日は たいてい 家で ゆっくり (   ) します。",
                                "promptVi": "Vào ngày nghỉ tôi thường thong thả thư giãn ở nhà.",
                                "options": ["リラックス", "ミーティング", "スピーチ", "アルバイト"],
                                "correct": 0,
                                "explain": "ゆっくり リラックス します: thư giãn một cách thong thả, thoải mái. Từ mượn Katakana Bài 2-3."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": "この アパートは 駅から 近くて、とても (   ) です。",
                                "promptVi": "Căn hộ này gần nhà ga nên rất tiện lợi.",
                                "options": ["べんり", "ふべん", "あぶない", "うるさい"],
                                "correct": 0,
                                "explain": "駅から 近くて (gần ga) mang ý tích cực ➔ べんり (tiện lợi). ふべん = bất tiện, あぶない = nguy hiểm, うるさい = ồn ào."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": "かばんの なかに さいふや 携帯電話が (   ) います。",
                                "promptVi": "Trong túi xách có để ví tiền và điện thoại di động.",
                                "options": ["はいって", "でて", "おちて", "あがって"],
                                "correct": 0,
                                "explain": "はいって います (入っています - có chứa đựng / nằm bên trong). でて = ra ngoài, おちて = rơi."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": "すみません、この 料理の (   ) を 教えて ください。",
                                "promptVi": "Xin lỗi, hãy chỉ cho tôi cách làm món ăn này.",
                                "options": ["つくりかた", "たべかた", "のみかた", "いきかた"],
                                "correct": 0,
                                "explain": "作り方 (つくりかた) = cách làm, cách chế biến. Mẫu V-masu bỏ masu + かた (cách làm V)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu hoặc từ đồng nghĩa",
                        "groupInstruction": "Chọn câu (A, B, C, D) có ý nghĩa tương đương gần nhất với câu hoặc cụm từ được gạch chân:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": "あしたは ようじが ありませんから、<span class='hl-kw'>ひま</span> です。",
                                "promptVi": "Ngày mai tôi không có việc bận gì nên rảnh rỗi.",
                                "options": [
                                    "時間が たくさん あります。",
                                    "とても いそがしい です。",
                                    "仕事が たくさん あります。",
                                    "病院へ 行かなければ なりません。"
                                ],
                                "correct": 0,
                                "explain": "ひま (rảnh rỗi) = 時間が たくさん あります (có nhiều thời gian trống, rảnh rỗi)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": "姉は <span class='hl-kw'>けっこんして います</span>。",
                                "promptVi": "Chị gái tôi đã kết hôn.",
                                "options": [
                                    "おっと（夫）が います。",
                                    "一人で 住んで います。",
                                    "まだ 学生です。",
                                    "子どもが いません。"
                                ],
                                "correct": 0,
                                "explain": "けっこんして います (đã kết hôn/lập gia đình) = có chồng (おっとが います)."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": "わたしは 日本のアニメに <span class='hl-kw'>きょうみが あります</span>。",
                                "promptVi": "Tôi rất có hứng thú với anime Nhật Bản.",
                                "options": [
                                    "アニメが 好きで、もっと 知りたいです。",
                                    "アニメが きらいで、見たくないです。",
                                    "アニメを ぜんぜん 知りません。",
                                    "アニメを 自分で 作りたいです。"
                                ],
                                "correct": 0,
                                "explain": "きょうみが あります (có hứng thú/quan tâm) = rất thích và muốn tìm hiểu thêm."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": "スーパーで <span class='hl-kw'>たくさんの</span> 野菜を 買いました。",
                                "promptVi": "Tôi đã mua rất nhiều rau ở siêu thị.",
                                "options": [
                                    "野菜を いっぱい 買いました。",
                                    "野菜を すこしだけ 買いました。",
                                    "野菜を ぜんぜん 買いませんでした。",
                                    "高い 野菜だけ 買いました。"
                                ],
                                "correct": 0,
                                "explain": "たくさんの (rất nhiều) = いっぱい (nhiều, đầy ắp)."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": "父は 毎朝 <span class='hl-kw'>さんぽ</span>を します。",
                                "promptVi": "Bố tôi mỗi sáng đều đi dạo bộ.",
                                "options": [
                                    "歩いて 運動を します。",
                                    "車で ドライブを します。",
                                    "ベッドで ねます。",
                                    "テレビを 見ます。"
                                ],
                                "correct": 0,
                                "explain": "さんぽ (散歩 - đi dạo bộ) = 歩いて 運動を します (đi bộ thư giãn/vận động)."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán ra Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20).",
                "badge": "20 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Kanji ➔ Hiragana (Chọn cách đọc đúng)",
                        "groupInstruction": "Chọn cách đọc Hiragana đúng cho chữ Hán được gạch chân:",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": "わたしの 趣味は <span class='hl-kw'>旅行</span> です。",
                                "promptVi": "Sở thích của tôi là đi du lịch.",
                                "options": ["りょこう", "りょうり", "りゆう", "りょうしん"],
                                "correct": 0,
                                "explain": "「旅行」 đọc là りょこう (Du lịch). 料理 = món ăn, 理由 = lý do."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": "父は 病院で <span class='hl-kw'>医者</span>を して います。",
                                "promptVi": "Bố tôi đang làm bác sĩ ở bệnh viện.",
                                "options": ["いしゃ", "かんごし", "きょうし", "ぎんこういん"],
                                "correct": 0,
                                "explain": "「医者」 đọc là いしゃ (Bác sĩ). Chữ Y (医) kết hợp Giả (者)."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": "朝 6時に <span class='hl-kw'>起きて</span>、シャワーを あびます。",
                                "promptVi": "Sáng tôi thức dậy lúc 6 giờ rồi tắm vòi sen.",
                                "options": ["ねて", "おきて", "たべて", "のんで"],
                                "correct": 1,
                                "explain": "「起きて」 là thể Te của 起きます (おきます - thức dậy)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": "これは 日本の <span class='hl-kw'>有名</span>な お菓子です。",
                                "promptVi": "Đây là loại bánh kẹo nổi tiếng của Nhật Bản.",
                                "options": ["ゆうめい", "たいせつ", "べんり", "しずか"],
                                "correct": 0,
                                "explain": "「有名」 đọc là ゆうめい (Nổi tiếng). Hữu (有) + Danh (名)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": "机の 上に <span class='hl-kw'>本</span>が 3冊 あります。",
                                "promptVi": "Trên bàn có 3 quyển sách.",
                                "options": ["ほん", "ノート", "ペン", "かばん"],
                                "correct": 0,
                                "explain": "「本」 đọc là ほん (Quyển sách). Lượng từ đếm sách là 冊 (さつ)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Hiragana ➔ Kanji (Chọn chữ Hán đúng)",
                        "groupInstruction": "Chọn chữ Hán tương ứng chính xác với từ Hiragana gạch chân:",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": "日本語の 歌を <span class='hl-kw'>うたいました</span>。",
                                "promptVi": "Tôi đã hát bài hát tiếng Nhật.",
                                "options": ["歌いました", "書きました", "聞きました", "読みました"],
                                "correct": 0,
                                "explain": "うたいました (hát) là chữ Hán「歌」➔ 歌いました. 書 = viết, 聞 = nghe, 読 = đọc."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": "きのう 新しい 服を <span class='hl-kw'>かいました</span>。",
                                "promptVi": "Hôm qua tôi đã mua quần áo mới.",
                                "options": ["買いました", "売りました", "着ました", "脱ぎました"],
                                "correct": 0,
                                "explain": "かいました (mua) là chữ Hán「買」➔ 買いました. 売 = bán."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": "母は 中学校の <span class='hl-kw'>せんせい</span> です。",
                                "promptVi": "Mẹ tôi là giáo viên trường trung học cơ sở.",
                                "options": ["学生", "先生", "会社員", "店員"],
                                "correct": 1,
                                "explain": "せんせい (giáo viên) là chữ Hán「先生」. Tiên (先) + Sinh (生)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": "あの <span class='hl-kw'>くるま</span>は とても 速いです。",
                                "promptVi": "Chiếc ô tô đằng kia rất nhanh.",
                                "options": ["電車", "自転車", "車", "飛行機"],
                                "correct": 2,
                                "explain": "くるま (xe ô tô) là chữ Hán「車」."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": "天気が いいですから、<span class='hl-kw'>そと</span>で 遊びましょう。",
                                "promptVi": "Thời tiết đẹp nên chúng ta hãy chơi ở bên ngoài nhé.",
                                "options": ["中", "外", "前", "後"],
                                "correct": 1,
                                "explain": "そと (bên ngoài) là chữ Hán「外」. 中 = bên trong, 前 = phía trước, 後 = phía sau."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Gồm 3 dạng bài: Điền khuyết trợ từ/thể (21-26), Sắp xếp câu Hái sao ☆ (27-30), Dịch câu Tự luận (31-32).",
                "badge": "30 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn trợ từ hoặc dạng chia ngữ pháp đúng nhất điền vào (   ):",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": "わたしは ピアノを ひく (   ) が できます。",
                                "promptVi": "Tôi có thể chơi đàn piano.",
                                "options": ["こと", "の", "もの", "とき"],
                                "correct": 0,
                                "explain": "Động từ thể từ điển (V-ru) + ことが できます: Mẫu câu nói về khả năng."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": "朝 ごはんを (   ) まえに、手を 洗います。",
                                "promptVi": "Trước khi ăn cơm sáng tôi rửa tay.",
                                "options": ["たべる", "たべた", "たべて", "たべます"],
                                "correct": 0,
                                "explain": "V-ru + まえに (Trước khi làm việc V). Luôn luôn dùng thể từ điển trước まえに."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": "図書館の 中では 静かに (   ) ください。",
                                "promptVi": "Trong thư viện xin hãy giữ yên tĩnh.",
                                "options": ["して", "する", "した", "します"],
                                "correct": 0,
                                "explain": "V-te + ください: Mẫu câu nhờ vả, yêu cầu lịch sự. します ➔ して."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": "田中さんは 今 会議室で 話して (   )。",
                                "promptVi": "Anh Tanaka hiện đang nói chuyện trong phòng họp.",
                                "options": ["います", "あります", "おきます", "みます"],
                                "correct": 0,
                                "explain": "V-te + います: Hành động đang tiếp diễn tại thời điểm nói."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": "日曜日、映画を (   )、買い物を したり しました。",
                                "promptVi": "Chủ nhật tôi vừa xem phim, vừa đi mua sắm...",
                                "options": ["見たり", "見て", "見ると", "見ながら"],
                                "correct": 0,
                                "explain": "Mẫu câu liệt kê hành động tiêu biểu: V1-たり、V2-たり します."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": "すみません、ボールペンを 借りても (   ) ですか。",
                                "promptVi": "Xin lỗi, tôi có thể mượn chiếc bút bi được không ạ?",
                                "options": ["いい", "だめ", "わるい", "ない"],
                                "correct": 0,
                                "explain": "V-te + も いいですか: Mẫu câu xin phép lịch sự 'Làm... có được không?'"
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: ☆ Hái sao (Sắp xếp cụm từ vào đúng vị trí)",
                        "groupInstruction": "Sắp xếp 4 cụm từ [1, 2, 3, 4] vào 4 vị trí trống để tạo thành câu hoàn chỉnh, sau đó chọn số tương ứng với vị trí ngôi sao ★:",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "sentencePre": "わたしは",
                                "sentencePost": "できます。",
                                "promptVi": "Tôi có thể chơi đàn guitar.",
                                "parts": [
                                    {"id": 1, "text": "ことが"},
                                    {"id": 2, "text": "ギターを"},
                                    {"id": 3, "text": "ひく"},
                                    {"id": 4, "text": "じょうずに"}
                                ],
                                "fullOrder": [2, 4, 3, 1],
                                "starPos": 3,
                                "correctOption": 3, # part 3 "ひく"
                                "fullSentence": "わたしは ギターを じょうずに ★ひく ことが できます。",
                                "explain": "Thứ tự sắp xếp: わたしは [2. ギターを] [4. じょうずに] ★[3. ひく] [1. ことが] できます。Vị trí ngôi sao ★ là động từ thể từ điển (3) ひく."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "sentencePre": "寝る",
                                "sentencePost": "います。",
                                "promptVi": "Trước khi đi ngủ, tôi thường viết nhật ký.",
                                "parts": [
                                    {"id": 1, "text": "日記を"},
                                    {"id": 2, "text": "まえに"},
                                    {"id": 3, "text": "書いて"},
                                    {"id": 4, "text": "いつも"}
                                ],
                                "fullOrder": [2, 4, 1, 3],
                                "starPos": 3,
                                "correctOption": 1, # part 1 "日記を"
                                "fullSentence": "寝る まえに いつも ★日記を 書いて います。",
                                "explain": "Thứ tự sắp xếp: 寝る [2. まえに] [4. いつも] ★[1. 日記を] [3. 書いて] います。Vị trí ngôi sao ★ là tân ngữ (1) 日記を."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "sentencePre": "休みの日は",
                                "sentencePost": "します。",
                                "promptVi": "Vào ngày nghỉ tôi thường xem TV hoặc đi dạo.",
                                "parts": [
                                    {"id": 1, "text": "見たり"},
                                    {"id": 2, "text": "テレビを"},
                                    {"id": 3, "text": "散歩を"},
                                    {"id": 4, "text": "したり"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 3,
                                "correctOption": 3, # part 3 "散歩を"
                                "fullSentence": "休みの日は テレビを 見たり ★散歩を したり します。",
                                "explain": "Thứ tự sắp xếp: 休みの日は [2. テレビを] [1. 見たり] ★[3. 散歩を] [4. したり] します。Cụm ở vị trí ★ là (3) 散歩を."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "sentencePre": "この 部屋には",
                                "sentencePost": "よ。",
                                "promptVi": "Căn phòng này thì ai cũng không được bước vào đâu đấy.",
                                "parts": [
                                    {"id": 1, "text": "入っては"},
                                    {"id": 2, "text": "いけません"},
                                    {"id": 3, "text": "だれも"},
                                    {"id": 4, "text": "勝手に"}
                                ],
                                "fullOrder": [3, 4, 1, 2],
                                "starPos": 3,
                                "correctOption": 1, # part 1 "入っては"
                                "fullSentence": "この 部屋には だれも 勝手に ★入っては いけません よ。",
                                "explain": "Thứ tự: この 部屋には [3. だれも] [4. 勝手に] ★[1. 入っては] [2. いけません] よ。Vị trí ★ là (1) 入っては."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu (Tự luận)",
                        "groupInstruction": "Nhập bản dịch vào ô trống (chấp nhận cả Kanji lẫn Hiragana, không phân biệt dấu cách):",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "dir": "vi_to_ja",
                                "prompt": "Dịch sang tiếng Nhật: <br><strong style='color:#1e1b4b;'>「Trước khi đi ngủ, tôi luôn uống một cốc nước.」</strong>",
                                "placeholder": "Nhập câu tiếng Nhật (Ví dụ: 寝る まえに、いつも 水を 飲みます)...",
                                "acceptable": [
                                    "ねるまえにいつも水をのみます",
                                    "寝るまえにいつも水をのみます",
                                    "寝る前にいつも水を飲みます",
                                    "ねる前にいつも水を飲みます",
                                    "ねるまえにいつもみずをのみます",
                                    "寝る前にいつもみずを飲みます",
                                    "ねるまえにいつもみずを飲みます",
                                    "ねるまえにいつも水をいっぱいのみます",
                                    "寝る前にいつも水を一杯飲みます"
                                ],
                                "standard": "寝る まえに、いつも 水を 飲みます（または 水を 一杯 飲みます）。",
                                "explain": "Mẫu câu V-ru + まえに (Trước khi làm V): 寝る まえに (ねるまえに), 水を 飲みます (みずを のみます)."
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "dir": "ja_to_vi",
                                "prompt": "Dịch sang tiếng Việt: <br><strong style='color:#1e1b4b;'>「休みの日は 家で 本を 読んだり、音楽を 聞いたり します。」</strong>",
                                "placeholder": "Nhập câu dịch tiếng Việt (Ví dụ: Vào ngày nghỉ tôi thường đọc sách và nghe nhạc ở nhà)...",
                                "keywords": ["ngày nghỉ", "ở nhà", "đọc sách", "nghe nhạc"],
                                "standard": "Vào ngày nghỉ tôi đọc sách và nghe nhạc ở nhà (hoặc: Ngày nghỉ tôi thường ở nhà đọc sách, nghe nhạc).",
                                "explain": "Mẫu V-たり、V-たり します: Liệt kê các hành động tiêu biểu diễn ra trong ngày nghỉ."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc bài viết chia sẻ thực tế dưới đây và chọn đáp án chính xác nhất cho 2 câu hỏi (33 và 34).",
                "badge": "10 Điểm",
                "readingPassage": {
                    "title": "【わたしの 東京での 生活（ナム）】",
                    "content": "みなさん、こんにちは。ベトナムから 来た ナムです。\n東京に 住んでから 6か月に なりました。\n平日は 日本語学校へ 行って、一生懸命 勉強して います。\n学校が 終わってから、スーパーで 買い物を して、家で 自分で 料理を 作ります。\nベトナムの 料理も 作りますが、最近は 日本の みそ汁や 卵焼きを 作る ことが 好きです。\n週末は 日本人の 友だちと 一緒に 公園を 散歩したり、カフェで 日本語を 話したり します。\n日本の 生活は とても 忙しいですが、毎日 新しい ことが たくさん あって、とても 楽しいです。",
                    "translation": "【Cuộc Sống Ở Tokyo Của Tôi (Nam)】\nXin chào tất cả mọi người. Tôi là Nam, đến từ Việt Nam.\nKể từ khi sống ở Tokyo đến nay đã được 6 tháng rồi.\nCác ngày trong tuần tôi đến trường tiếng Nhật và chăm chỉ học tập.\nSau khi tan học, tôi đi siêu thị mua đồ rồi tự nấu ăn tại nhà.\nTôi cũng nấu cả món ăn Việt Nam, nhưng dạo gần đây tôi rất thích nấu canh miso và trứng cuộn tamagoyaki của Nhật.\nCuối tuần, tôi cùng những người bạn Nhật đi dạo công viên hoặc trò chuyện bằng tiếng Nhật ở quán cà phê.\nCuộc sống ở Nhật rất bận rộn nhưng mỗi ngày đều có rất nhiều điều mới mẻ, thực sự rất vui vẻ."
                },
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": "ナムさんは 学校が 終わってから 何を しますか。",
                        "promptVi": "Bạn Nam làm gì sau khi tan trường?",
                        "options": [
                            "スーパーで 買い物を して、自分で 料理を 作ります。",
                            "友だちと カフェへ 行って、ずっと 話します。",
                            "公園で サッカーの 練習を します。",
                            "アルバイト先へ 行って、夜まで 働きます。"
                        ],
                        "correct": 0,
                        "explain": "Trong bài viết ghi rõ: 『学校が 終わってから、スーパーで 買い物を して、家で 自分で 料理を 作ります。』 Do đó phương án A chính xác."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": "ナムさんの 生活について、正しい ものは どれですか。",
                        "promptVi": "Câu nào dưới đây là ĐÚNG về cuộc sống của bạn Nam?",
                        "options": [
                            "日本料理は 一度も 作ったことが ありません。",
                            "平日は 勉強して、週末は 友だちと 散歩や カフェに 行きます。",
                            "東京に 住んでから もう 3年に なりました。",
                            "日本の 生活は つまらなくて、毎日 寂しいです。"
                        ],
                        "correct": 1,
                        "explain": "Đoạn văn miêu tả: 평 nhật (平日は) học tập, cuối tuần (週末は) đi dạo công viên và quán cà phê cùng bạn bè người Nhật. Phương án B chính xác."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (mỗi câu viết từ 2 đến 3 câu hoàn chỉnh).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "あなたの 家族について 紹介してください。（何人 家族ですか。家族は どこに 住んで いますか。2〜3文で 書いてください）",
                        "promptVi": "Hãy giới thiệu về gia đình bạn. Gia đình bạn có mấy người? Gia đình đang sống ở đâu? (Viết 2-3 câu tiếng Nhật)",
                        "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしの 家族は 4人です...)...",
                        "hints": [
                            "Số người trong gia đình: わたしの 家族は ～人です",
                            "Thành viên: 父と、母と、兄と、わたしです",
                            "Nơi sống: 家族は ハノイに 住んで います"
                        ],
                        "modelAnswer": "わたしの 家族は 4人です。父、母、姉と わたしです。家族は ベトナムの ハノイに 住んで います。みんな とても 元気です。",
                        "modelVi": "Gia đình tôi có 4 người: bố, mẹ, chị gái và tôi. Gia đình đang sống ở Hà Nội, Việt Nam. Mọi người đều rất khỏe mạnh.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Nói đúng số lượng người và thành viên gia đình; dùng đúng trợ từ に với 住んでいます; câu văn tự nhiên, đủ 2-3 câu."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "日本で どんな ことを してみたいですか。りゆうも 書いてください。（2〜3文で 書いてください）",
                        "promptVi": "Bạn muốn làm những điều gì ở Nhật Bản? Hãy viết cả lý do nữa nhé! (Viết 2-3 câu tiếng Nhật)",
                        "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしは 富士山に 登ってみたいです...)...",
                        "hints": [
                            "Muốn làm gì: ～てみたいです / ～たいです",
                            "Địa điểm / Hoạt động: 京都のお寺 / 富士山 / 桜を見る / 温泉に入る",
                            "Lý do: ～ですから / 有名ですから"
                        ],
                        "modelAnswer": "わたしは 日本の 京都へ 行って、古い お寺や 桜を 見てみたいです。写真で 見て、とても きれいでしたから。そして、本物の 抹茶を 飲みたいです。",
                        "modelVi": "Tôi muốn đến Kyoto của Nhật để ngắm những ngôi chùa cổ và hoa anh đào. Vì xem qua ảnh tôi thấy rất đẹp. Và tôi cũng muốn uống matcha chính gốc nữa.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Sử dụng tốt mẫu câu biểu đạt mong muốn ～たいです hoặc trải nghiệm ～てみたいです; có đưa ra nguyên nhân lý do; từ vựng phong phú."
                    }
                ]
            }
        ]
    }
]

print(f"Loaded {len(EXAMS_DATA)} exams with {len(EXAMS_DATA[0]['sections'])} sections each.")
