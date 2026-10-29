#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/exam_m104_data.py
Mã đề M104: Đề Chuyên Sâu Giao Tiếp, Mua Sắm & Tần Suất Đời Sống (Bài 1 - 10)
Chuẩn Can-do giáo viên 10 năm kinh nghiệm - Tuyệt đối không dùng chữ Hán chưa học.
"""

import re
try:
    from scripts.exam_m101_data import PERMITTED_KANJI, v
except ImportError:
    from exam_m101_data import PERMITTED_KANJI, v

def build_m104():
    return {
        "code": "M104",
        "name": "Mã Đề M104 (Giao Tiếp, Mua Sắm & Tần Suất Đời Sống)",
        "tag": "🛍️ Mua Sắm • Hẹn Gặp • Tần Suất • Nhờ Vả Lịch Sự • Chuẩn A2-1",
        "desc": "Đề chuyên sâu về các tình huống giao tiếp đời sống thực tế: lời xin lỗi vì đến muộn, cách hỏi và chỉ cách làm món ăn (～かたを おしえて くださいませんか), tần suất hành động (週に三回, 月に五回), mua sắm và tặng quà.",
        "timeLimit": 45 * 60,
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ vựng chính xác nhất điền vào khoảng trống câu sau:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": v("あきはばらは でんきやが 多くて、とても (   ) です。", "M104.Q1.p"),
                                "promptVi": "Akihabara có nhiều cửa hàng điện tử nên rất tiện lợi. (Câu 2 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("べんり", "M104.Q1.o0"),
                                    v("ゆうめい", "M104.Q1.o1"),
                                    v("しずか", "M104.Q1.o2"),
                                    v("さむい", "M104.Q1.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng tính từ (Bài 5):</strong> Có nhiều cửa hàng nên rất thuận tiện, tiện lợi ➔ <strong>べんり</strong> (tiện lợi)."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": v("あした 十時に ホテルの (   ) で あいましょう。", "M104.Q2.p"),
                                "promptVi": "Ngày mai chúng ta hẹn gặp nhau vào lúc 10h tại sảnh khách sạn nhé. (Câu 17 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ロビー", "M104.Q2.o0"),
                                    v("トイレ", "M104.Q2.o1"),
                                    v("シャワー", "M104.Q2.o2"),
                                    v("エレベーター", "M104.Q2.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng nơi chốn khách sạn (Bài 7):</strong> Sảnh đợi khách sạn là <strong>ロビー</strong> (lobby)."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": v("きょねんの たんじょうびに かわいい (   ) を もらいました。", "M104.Q3.p"),
                                "promptVi": "Dịp sinh nhật năm ngoái, tôi đã nhận được chiếc áo phông rất dễ thương. (Câu 19 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("Tシャツ", "M104.Q3.o0"),
                                    v("コーヒー", "M104.Q3.o1"),
                                    v("みず", "M104.Q3.o2"),
                                    v("おちゃ", "M104.Q3.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng quà tặng trang phục (Bài 6):</strong> Áo phông là <strong>Tシャツ</strong>."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": v("わあ、きれいな (   ) ですね。だれに もらいましたか。", "M104.Q4.p"),
                                "promptVi": "Ôi, đồng hồ đẹp quá. Bạn nhận được từ ai vậy? (Câu 20 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("とけい", "M104.Q4.o0"),
                                    v("じしょ", "M104.Q4.o1"),
                                    v("まんが", "M104.Q4.o2"),
                                    v("てがみ", "M104.Q4.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng đồ dùng cá nhân (Bài 7):</strong> Chiếc đồng hồ là <strong>とけい</strong>."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": v("あねは いま、ゲームの かいしゃで (   ) を して います。", "M104.Q5.p"),
                                "promptVi": "Chị gái tôi bây giờ đang làm việc tại một công ty trò chơi. (Câu 16 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("仕事", "M104.Q5.o0"),
                                    v("食事", "M104.Q5.o1"),
                                    v("勉強", "M104.Q5.o2"),
                                    v("旅行", "M104.Q5.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng nghề nghiệp (Bài 8):</strong> Làm việc tại công ty ➔ <strong>仕事</strong>を して います (しごとを して います). Chữ 仕 và 事 đều học ở Bài 8."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa gần nhất với câu gạch chân",
                        "groupInstruction": "Chọn câu tiếng Nhật mang ý nghĩa tương đương với câu đã cho:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": v("<u>あしたの 朝 九時に しんじゅく駅の にしぐちで あいましょう。</u>", "M104.Q6.p"),
                                "promptVi": "9h sáng mai chúng mình gặp nhau ở cổng tây ga Shinjuku nhé. (Câu 7)",
                                "options": [
                                    v("あしたの 朝 九時に しんじゅく駅の にしぐちで まちます。", "M104.Q6.o0"),
                                    v("あしたの 夜 九時に しんじゅく駅へ 行きます。", "M104.Q6.o1"),
                                    v("しんじゅく駅ではなく、とうきょう駅で あいましょう。", "M104.Q6.o2"),
                                    v("あさっての 朝 九時に あいましょう。", "M104.Q6.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Đồng nghĩa giao tiếp hẹn gặp:</strong> Gặp nhau ở cổng Tây lúc 9h sáng."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": v("<u>あべさん、おそくなって すみません。時間を まちがえました…</u>", "M104.Q7.p"),
                                "promptVi": "Anh Abe ơi, mình xin lỗi vì đến muộn nhé. Mình bị nhầm thời gian... (Câu 10)",
                                "options": [
                                    v("時間を まちがえたので、やくそくの 時間に おくれました。もうしわけありません。", "M104.Q7.o0"),
                                    v("時間が ありましたから、はやく きました。", "M104.Q7.o1"),
                                    v("道が すいて いたので、すぐに つきました。", "M104.Q7.o2"),
                                    v("あべさんに あいたく なかったです。", "M104.Q7.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Ý nghĩa lời xin lỗi:</strong> Nhầm thời gian nên bị muộn cuộc hẹn (おくれました)."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": v("<u>私は センターで 週に 三回 日本語を 勉強して います。</u>", "M104.Q8.p"),
                                "promptVi": "Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. (Câu 32)",
                                "options": [
                                    v("一週間に 三日、センターへ 日本語を ならいに 行きます。", "M104.Q8.o0"),
                                    v("一か月に 三回だけ 日本語を 勉強します。", "M104.Q8.o1"),
                                    v("まい日 センターで 日本語を 勉強して います。", "M104.Q8.o2"),
                                    v("週に 一回だけ 日本語の 勉強を します。", "M104.Q8.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tương đương tần suất: 週に三回 = 一週間に三日 (3 ngày một tuần).</strong> Chữ 週 (Chu - tuần) và 回 (Hồi - lần) học ở Bài 10."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": v("<u>月に 五回 レストランへ 食べに 行きます。</u>", "M104.Q9.p"),
                                "promptVi": "Một tháng tôi đến nhà hàng ăn 5 lần. (Câu 32)",
                                "options": [
                                    v("一か月の あいだに、五回 レストランで 食事を します。", "M104.Q9.o0"),
                                    v("いちねんに 五回しか レストランへ 行きません。", "M104.Q9.o1"),
                                    v("まい週 五回 レストランへ 行きます。", "M104.Q9.o2"),
                                    v("うちで まい日 ごはんを 食べます。", "M104.Q9.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tương đương cách nói: 月に五回 = 一か月に五回 (5 lần trong một tháng).</strong>"
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": v("<u>あねは ちゅうごくの ペキンに すんで います。</u>", "M104.Q10.p"),
                                "promptVi": "Chị gái tôi đang sống ở Bắc Kinh, Trung Quốc. (Câu 16)",
                                "options": [
                                    v("私の あねの いえは ちゅうごくの ペキンに あります。", "M104.Q10.o0"),
                                    v("あねは 日本の とうきょうに すんで います。", "M104.Q10.o1"),
                                    v("あねは まだ ちゅうごくへ 行った ことが ありません。", "M104.Q10.o2"),
                                    v("あねは どこにも すんで いません。", "M104.Q10.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tương đương cư trú: Đang sống ở Bắc Kinh = Nhà của chị ở Bắc Kinh.</strong>"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Kiểm tra chữ Hán chủ đề gia đình, quốc gia, thời gian, trường học (Bài 1 - 10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn âm đọc chính xác của chữ Hán trong câu:",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": v("わたしの 【母】は とても しんせつです。", "M104.Q11.p"),
                                "promptVi": "Mẹ tôi rất tốt bụng.",
                                "options": [
                                    v("はは", "M104.Q11.o0"),
                                    v("ちち", "M104.Q11.o1"),
                                    v("あね", "M104.Q11.o2"),
                                    v("いもうと", "M104.Q11.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 母 (MẪU - Bài 1):</strong> Đọc là <strong>はは</strong> (mẹ mình). Chữ 父 (PHỤ - Bài 1) đọc là ちち (bố mình)."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": v("わたしの 【父】は まい朝 さんぽを します。", "M104.Q12.p"),
                                "promptVi": "Bố tôi mỗi sáng đều đi dạo.",
                                "options": [
                                    v("ちち", "M104.Q12.o0"),
                                    v("はは", "M104.Q12.o1"),
                                    v("あに", "M104.Q12.o2"),
                                    v("おとうと", "M104.Q12.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 父 (PHỤ - Bài 1):</strong> Đọc là <strong>ちち</strong> (bố mình)."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": v("あの 【男】の 人は だれですか。", "M104.Q13.p"),
                                "promptVi": "Người đàn ông đằng kia là ai thế?",
                                "options": [
                                    v("おとこ", "M104.Q13.o0"),
                                    v("おんな", "M104.Q13.o1"),
                                    v("ひと", "M104.Q13.o2"),
                                    v("こども", "M104.Q13.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 男 (NAM - Bài 1):</strong> Đọc là <strong>おとこ</strong>. 男の人: おとこのひと (người đàn ông)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": v("あそこで 【女】の 子が あそんで います。", "M104.Q14.p"),
                                "promptVi": "Đằng kia có bé gái đang chơi đùa.",
                                "options": [
                                    v("おんな", "M104.Q14.o0"),
                                    v("おとこ", "M104.Q14.o1"),
                                    v("はは", "M104.Q14.o2"),
                                    v("ちち", "M104.Q14.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 女 (NỮ - Bài 1):</strong> Đọc là <strong>おんな</strong>. 女の子: おんなのこ (bé gái)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": v("センターで 【週】に 三回 勉強します。", "M104.Q15.p"),
                                "promptVi": "Tôi học 3 lần một tuần ở trung tâm.",
                                "options": [
                                    v("しゅう", "M104.Q15.o0"),
                                    v("かい", "M104.Q15.o1"),
                                    v("つき", "M104.Q15.o2"),
                                    v("ねん", "M104.Q15.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 週 (CHU - Bài 10):</strong> Đọc là <strong>しゅう</strong> (tuần). 週に三回: しゅうにさんかい."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn chữ Hán đúng cho từ Hiragana trong ngoặc 【 】",
                        "groupInstruction": "Chọn chữ Hán chính xác trong 4 phương án cho từ được gạch dưới:",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": v("月に 五【かい】 レストランへ 行きます。", "M104.Q16.p"),
                                "promptVi": "Mỗi tháng tôi đến nhà hàng 5 lần.",
                                "options": [
                                    v("回", "M104.Q16.o0"),
                                    v("週", "M104.Q16.o1"),
                                    v("時", "M104.Q16.o2"),
                                    v("間", "M104.Q16.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 回 (HỒI - Bài 10):</strong> Đọc là <strong>かい</strong> (số lần: 一回, 二回, 三回, 五回)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": v("日本の 【ぶんか】を まなびたいです。", "M104.Q17.p"),
                                "promptVi": "Tôi muốn học hỏi văn hóa Nhật Bản.",
                                "options": [
                                    v("文化", "M104.Q17.o0"),
                                    v("音楽", "M104.Q17.o1"),
                                    v("旅行", "M104.Q17.o2"),
                                    v("友達", "M104.Q17.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 文化 (VĂN HÓA - Bài 10):</strong> Đọc là <strong>ぶんか</strong>. Cả 2 chữ 文 và 化 đều học ở Bài 10."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": v("へやで 【おんがく】を ききます。", "M104.Q18.p"),
                                "promptVi": "Tôi nghe nhạc ở trong phòng.",
                                "options": [
                                    v("音楽", "M104.Q18.o0"),
                                    v("文化", "M104.Q18.o1"),
                                    v("外国", "M104.Q18.o2"),
                                    v("日本語", "M104.Q18.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 音楽 (ÂM NHẠC - Bài 10):</strong> Đọc là <strong>おんがく</strong>. Chữ 音 (Âm) và 楽 (Nhạc/Lạc) học ở Bài 10."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": v("夏やすみに 【りょこう】を します。", "M104.Q19.p"),
                                "promptVi": "Nghỉ hè tôi đi du lịch.",
                                "options": [
                                    v("旅行", "M104.Q19.o0"),
                                    v("留学", "M104.Q19.o1"),
                                    v("食事", "M104.Q19.o2"),
                                    v("仕事", "M104.Q19.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 旅行 (LỮ HÀNH - Bài 10):</strong> Đọc là <strong>りょこう</strong> (chuyến du lịch)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": v("あしたは 【がっこう】が やすみです。", "M104.Q20.p"),
                                "promptVi": "Ngày mai trường học được nghỉ.",
                                "options": [
                                    v("学校", "M104.Q20.o0"),
                                    v("先生", "M104.Q20.o1"),
                                    v("友達", "M104.Q20.o2"),
                                    v("留学生", "M104.Q20.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 学校 (HỌC HIỆU - Bài 9):</strong> Đọc là <strong>がっこう</strong> (trường học)."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Kiểm tra cách nói lịch sự, tần suất hành động, cách làm (～かた), và liên từ chỉ lý do.",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn phương án đúng nhất điền vào chỗ trống",
                        "groupInstruction": "Chọn từ/thể ngữ pháp chính xác nhất điền vào chỗ trống trong ngoặc (   ):",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": v("ベトナムりょうりの つくりかたを おしえて (   )。", "M104.Q21.p"),
                                "promptVi": "Bạn có thể chỉ cho tôi cách làm món ăn Việt Nam được không? (Câu 31 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("くださいませんか", "M104.Q21.o0"),
                                    v("くださいました", "M104.Q21.o1"),
                                    v("くれますか", "M104.Q21.o2"),
                                    v("あげますか", "M104.Q21.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc nhờ vả lịch sự: V-て くださいませんか:</strong> Nhờ người khác chỉ bảo cho mình một cách tôn trọng, lịch sự."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": v("私は センターで 週 (   ) 三回 日本語を 勉強して います。", "M104.Q22.p"),
                                "promptVi": "Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. (Câu 32 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("に", "M104.Q22.o0"),
                                    v("で", "M104.Q22.o1"),
                                    v("を", "M104.Q22.o2"),
                                    v("へ", "M104.Q22.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc chỉ tần suất: [Đơn vị thời gian] に [Số lần] 回:</strong> 週に三回 (3 lần một tuần), 月に五回 (5 lần một tháng)."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": v("きれいな とけいですね。(   ) に もらいましたか。", "M104.Q23.p"),
                                "promptVi": "Đồng hồ đẹp quá, bạn nhận được từ ai vậy? (Câu 20 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("だれ", "M104.Q23.o0"),
                                    v("どこ", "M104.Q23.o1"),
                                    v("いつ", "M104.Q23.o2"),
                                    v("なに", "M104.Q23.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc nhận từ ai: [Người] に もらう:</strong> Từ để hỏi người nhận là <strong>だれに</strong> もらいましたか."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": v("あした、何時に (   ) か。", "M104.Q24.p"),
                                "promptVi": "Ngày mai mấy giờ chúng ta gặp nhau thế? (Câu 7 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("あいます", "M104.Q24.o0"),
                                    v("あいまし", "M104.Q24.o1"),
                                    v("あう", "M104.Q24.o2"),
                                    v("あって", "M104.Q24.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Hỏi giờ gặp nhau: 何時に あいますか:</strong> Thể lịch sự ます đi với trợ từ nghi vấn か."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": v("あべさん、おそくなって すみません。時間を (   )…", "M104.Q25.p"),
                                "promptVi": "Anh Abe ơi, mình xin lỗi vì đến muộn nhé. Mình bị nhầm thời gian hẹn... (Câu 10)",
                                "options": [
                                    v("まちがえました", "M104.Q25.o0"),
                                    v("まちがえます", "M104.Q25.o1"),
                                    v("わすれました", "M104.Q25.o2"),
                                    v("なくしました", "M104.Q25.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng nhầm lẫn: じかんを まちがえました:</strong> Tôi đã nhầm giờ hẹn."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": v("いつか、日本へ (   ) したいです。", "M104.Q26.p"),
                                "promptVi": "Một ngày nào đó, tôi muốn đi du học ở Nhật Bản. (Câu 32 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("りゅうがく", "M104.Q26.o0"),
                                    v("りょこう", "M104.Q26.o1"),
                                    v("かいもの", "M104.Q26.o2"),
                                    v("さんぽ", "M104.Q26.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc nguyện vọng du học: 日本へ りゅうがくしたいです (Muốn đi du học Nhật Bản).</strong>"
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Sắp xếp câu tìm từ tại vị trí ngôi sao (★)",
                        "groupInstruction": "Sắp xếp 4 cụm từ theo đúng ngữ pháp và chọn từ nằm ở vị trí ngôi sao (★):",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "prompt": v("あしたの 朝 九時に [  ] [  ] [ ★ ] [  ] あいましょう。", "M104.Q27.p"),
                                "promptVi": "9h sáng mai tại cổng tây ga Shinjuku nhé. (Câu 7)",
                                "options": [
                                    v("しんじゅく駅", "M104.Q27.o0"),
                                    v("の", "M104.Q27.o1"),
                                    v("にしぐち", "M104.Q27.o2"),
                                    v("で", "M104.Q27.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> あしたの 朝 九時に [しんじゅく駅] [の] [★ にしぐち] [で] あいましょう。<br>Vị trí ngôi sao là <strong>にしぐち</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "prompt": v("ベトナムりょうりの [  ] [  ] [ ★ ] [  ] くださいませんか。", "M104.Q28.p"),
                                "promptVi": "Bạn có thể chỉ cho tôi cách làm món ăn Việt Nam không? (Câu 31)",
                                "options": [
                                    v("つくりかた", "M104.Q28.o0"),
                                    v("を", "M104.Q28.o1"),
                                    v("私に", "M104.Q28.o2"),
                                    v("おしえて", "M104.Q28.o3")
                                ],
                                "correct": 3,
                                "explain": "💡 <strong>Trật tự câu:</strong> ベトナムりょうりの [つくりかた] [を] [私に] [★ おしえて] くださいませんか。<br>Vị trí ngôi sao là <strong>おしえて</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "prompt": v("私は センターで [  ] [  ] [ ★ ] [  ] 勉強して います。", "M104.Q29.p"),
                                "promptVi": "Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. (Câu 32)",
                                "options": [
                                    v("週に", "M104.Q29.o0"),
                                    v("三回", "M104.Q29.o1"),
                                    v("日本語", "M104.Q29.o2"),
                                    v("を", "M104.Q29.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> 私は センターで [週に] [三回] [★ 日本語] [を] 勉強して います。<br>Vị trí ngôi sao là <strong>日本語</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "prompt": v("あねは いま、[  ] [  ] [ ★ ] [  ] して います。", "M104.Q30.p"),
                                "promptVi": "Chị tôi đang làm việc tại công ty trò chơi. (Câu 16)",
                                "options": [
                                    v("ゲームの", "M104.Q30.o0"),
                                    v("かいしゃで", "M104.Q30.o1"),
                                    v("仕事", "M104.Q30.o2"),
                                    v("を", "M104.Q30.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> あねは いま、[ゲームの] [かいしゃで] [★ 仕事] [を] して います。<br>Vị trí ngôi sao là <strong>仕事</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu tự luận (Việt ➔ Nhật)",
                        "groupInstruction": "Nhập bản dịch tiếng Nhật chính xác cho các câu sau:",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "prompt": "Ngày mai chúng ta hẹn gặp nhau vào lúc 10h tại sảnh khách sạn nhé.",
                                "promptVi": "Câu 17 trong bộ 40 câu ôn tập",
                                "reference": v("あした 十時に ホテルの ロビーで あいましょう。", "M104.Q31.ref"),
                                "acceptAnswers": [
                                    v("あした 十時に ホテルの ロビーで あいましょう。", "M104.Q31.ans0"),
                                    v("あした 十時に ホテルの ロビーで あいましょう。", "M104.Q31.ans1"),
                                    v("あした 10時に ホテルの ロビーで あいましょう。", "M104.Q31.ans2")
                                ],
                                "hints": ["あした 十時に", "ホテルの ロビーで", "あいましょう (あいましょう)"]
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "prompt": "Bạn có thể chỉ cho tôi cách làm món ăn Việt Nam không?",
                                "promptVi": "Câu 31 trong bộ 40 câu ôn tập",
                                "reference": v("ベトナムりょうりの つくりかたを おしえて くださいませんか。", "M104.Q32.ref"),
                                "acceptAnswers": [
                                    v("ベトナムりょうりの つくりかたを おしえて くださいませんか。", "M104.Q32.ans0"),
                                    v("ベトナムりょうりの つくりかたを おしえて ください。", "M104.Q32.ans1"),
                                    v("ベトナムりょうりの つくりかたを おしえてくださいませんか。", "M104.Q32.ans2")
                                ],
                                "hints": ["ベトナムりょうりの", "つくりかたを", "おしえて くださいませんか"]
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc tin nhắn hẹn gặp và chọn đáp án chính xác nhất (Câu 33-34).",
                "badge": "10 Điểm",
                "passage": v("ナムさんへ。\nメッセージを ありがとうございます。\nあしたの 日曜日、十時に ホテルの ロビーで あいましょう。\nあきはばらは でんきやが 多くて、とても べんりですから、いっしょに 行って 新しい でんしじしょを みませんか。\n買い物の 後で、おいしい 日本りょうりを 食べましょう。\nもし 時間に おくれたら、メッセージを 送って くださいね。\nさとうより", "M104.passage") if False else v("ナムさんへ。\nメッセージを ありがとうございます。\nあしたの 日曜日、十時に ホテルの ロビーで あいましょう。\nあきはばらは でんきやが 多くて、とても べんりですから、いっしょに 行って でんしじしょを みませんか。\n買い物の 後で、おいしい 日本りょうりを 食べましょう。\nもし 時間に おくれたら、メッセージを 送って くださいね。\nさとうより", "M104.passage") if False else v("ナムさんへ。\nメッセージを ありがとうございます。\nあしたの にちようび、十時に ホテルの ロビーで あいましょう。\nあきはばらは でんきやが 多くて、とても べんりですから、いっしょに 行って でんしじしょを みませんか。\nかいものの 後で、おいしい 日本りょうりを たべましょう。\nもし 時間に おくれたら、れんらくを して くださいね。\nさとうより", "M104.passage"),
                "passageVi": "Gửi bạn Nam.\nCảm ơn tin nhắn của bạn.\nChủ nhật ngày mai chúng ta gặp nhau lúc 10 giờ ở sảnh khách sạn nhé.\nAkihabara có nhiều tiệm điện tử và rất tiện lợi, bạn cùng đi xem kim từ điển với mình nhé.\nSau khi mua sắm, chúng mình cùng đi ăn món Nhật ngon lành nhé.\nNếu bị muộn giờ thì hãy liên lạc cho mình nhé.\nTừ Sato",
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": v("さとうさんと ナムさんは あした 何時に あいますか。", "M104.Q33.p"),
                        "promptVi": "Sato và Nam ngày mai sẽ gặp nhau lúc mấy giờ?",
                        "options": [
                            v("十時", "M104.Q33.o0"),
                            v("九時", "M104.Q33.o1"),
                            v("七時", "M104.Q33.o2"),
                            v("十二時", "M104.Q33.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「十時に ホテルの ロビーで あいましょう」 ➔ Hẹn gặp lúc 10 giờ."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": v("ふたりは あきはばらで 何を しますか。", "M104.Q34.p"),
                        "promptVi": "Hai người họ sẽ làm gì ở Akihabara?",
                        "options": [
                            v("でんしじしょを みて、日本りょうりを たべます。", "M104.Q34.o0"),
                            v("ホテルに とまります。", "M104.Q34.o1"),
                            v("学校で 勉強します。", "M104.Q34.o2"),
                            v("でんしゃの きっぷを かいます。", "M104.Q34.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài đọc:</strong> Xem kim từ điển và sau đó đi ăn món ăn Nhật."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Viết đoạn văn ngắn trả lời câu hỏi và bài luận theo chủ đề (tối thiểu 50 chữ/ký tự).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "あなたの たんじょうびに どんな プレゼントを もらいましたか。（だれに、何を もらったか かいて ください）",
                        "promptVi": "Vào dịp sinh nhật, bạn đã nhận được món quà gì? (Hãy viết rõ bạn nhận từ ai và nhận món gì).",
                        "minWords": 30,
                        "placeholder": "Gõ câu trả lời tiếng Nhật tại đây... Ví dụ: きょねんの たんじょうびに 友達に かわいい Tシャツを もらいました...",
                        "hints": [
                            "Bối cảnh: きょねんの たんじょうびに...",
                            "Người tặng: 母に / 友達に / 父に...",
                            "Món quà: かわいい Tシャツ / 白い シャツ / とけいを もらいました",
                            "Cảm xúc: とても うれしかったです"
                        ],
                        "modelAnswer": v("きょねんの たんじょうびに、友達に 白い かわいい シャツを もらいました。そして、父と 母に きれいな とけいを もらいました。とても うれしかったです。", "M104.Q35.ans"),
                        "modelVi": "Vào dịp sinh nhật năm ngoái, bạn bè đã tặng tôi một chiếc áo sơ mi trắng rất dễ thương. Và bố mẹ đã tặng tôi một chiếc đồng hồ rất đẹp. Tôi đã rất vui mừng.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Sử dụng đúng cấu trúc nhận quà (N(người) に N(vật) を もらいました), tính từ miêu tả đồ vật."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "あなたの まちの 日本文化センターや 好きな 日本りょうりについて かいて ください。（週や 月の かいすう、すきな りゆう、しょうらいの ゆめなど、五十じ いじょう）",
                        "promptVi": "Hãy viết đoạn văn chia sẻ về hoạt động học tập tại trung tâm văn hóa Nhật Bản hoặc món ăn Nhật yêu thích của bạn (tần suất theo tuần/tháng, lý do thích, ước mơ du học... tối thiểu 50 chữ/ký tự).",
                        "minWords": 50,
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: 私の まちには 日本の 文化センターが あります...",
                        "hints": [
                            "Giới thiệu nơi học: 私の まちには 日本の 文化センターが あります",
                            "Tần suất học & ăn: 私は センターで 週に 三回 勉強して います / 月に 五回 レストランへ 行きます",
                            "Lý do thích: 日本りょうりが 好きですから / とても おいしいですから",
                            "Ước mơ tương lai: いつか、日本へ 留学したいです",
                            "Độ dài: Tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": v("私の 町には 外国人が たくさん います。町の なかに、日本の 文化センターが あります。私は センターで 週に 三回 日本語を 勉強して います。そして、日本りょうりが 好きですから、月に 五回 レストランへ 食べに 行きます。いつか、日本へ 留学したいです。", "M104.Q36.ans") if False else v("私の 町には 外国人が たくさん います。町の なかに、日本の 文化センターが あります。私は センターで 週に 三回 日本語を 勉強して います。そして、日本りょうりが 好きですから、月に 五回 レストランへ たべに 行きます。いつか、日本へ 留学生として 行きたいです。", "M104.Q36.ans"),
                        "modelVi": "Thành phố của tôi có nhiều người nước ngoài. Trong thành phố có trung tâm văn hóa Nhật Bản. Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. Và tôi thích món ăn Nhật nên một tháng tôi đến nhà hàng ăn năm lần. Một ngày nào đó, tôi muốn đến Nhật Bản với tư cách là một lưu học sinh.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; bám sát câu 32 bộ ôn tập, vận dụng chính xác cấu trúc tần suất (週に三回, 月に五回) và nguyện vọng tương lai (～たいです)."
                    }
                ]
            }
        ]
    }

if __name__ == "__main__":
    exam = build_m104()
    print("M104 built successfully!")
    print("Code:", exam["code"])
    print("Sections:", len(exam["sections"]))
