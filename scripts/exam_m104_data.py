#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

PERMITTED_KANJI = set(
    "私父母子男女"
    "国外国語本読好何"
    "秋冬春夏今花海山川"
    "天気晴雨雪雲風空"
    "町店多少高安広"
    "道通右左赤青黒白"
    "時間場所駅出待止"
    "食事仕前後朝昼夜乗"
    "学校先生勉強"
    "文化音楽留旅行友達週回"
    "人"
    "日月"
    "一二三四五六七八九十"
)

def v(text, label=""):
    cjk = set(re.findall(r"[一-龯]", text))
    out = cjk - PERMITTED_KANJI
    if out:
        raise ValueError(f"UNLEARNED KANJI at [{label}]: {out} in '{text}'")
    return text

DATA_M104 = {
    "code": "M104",
    "name": "Mã Đề M104 (Giao Tiếp, Mua Sắm & Tần Suất Đời Sống)",
    "tag": "🛍️ Mua Sắm • Hẹn Gặp • Tần Suất • Nhờ Vả Lịch Sự • Chuẩn A2-1",
    "desc": "Đề chuyên sâu về các tình huống giao tiếp đời sống thực tế: lời xin lỗi vì đến muộn, cách hỏi và chỉ cách làm món ăn (～かたを おしえて くださいませんか), tần suất hành động (週に三回, 月に五回), mua sắm và tặng quà.",
    "timeLimit": 2700,
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
                            "prompt": "あきはばらは でんきやが 多くて、とても (   ) です。",
                            "promptVi": "Akihabara có nhiều cửa hàng điện tử nên rất tiện lợi. (Câu 2 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ゆうめい",
                                "しずか",
                                "べんり",
                                "さむい"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Từ vựng tính từ (Bài 5):</strong> Có nhiều cửa hàng nên rất thuận tiện, tiện lợi ➔ <strong>べんり</strong> (tiện lợi)."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "あした 十時に ホテルの (   ) で あいましょう。",
                            "promptVi": "Ngày mai chúng ta hẹn gặp nhau vào lúc 10h tại sảnh khách sạn nhé. (Câu 17 trong bộ 40 câu ôn tập)",
                            "options": [
                                "トイレ",
                                "シャワー",
                                "ロビー",
                                "エレベーター"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Từ vựng nơi chốn khách sạn (Bài 7):</strong> Sảnh đợi khách sạn là <strong>ロビー</strong> (lobby)."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "きょねんの たんじょうびに かわいい (   ) を もらいました。",
                            "promptVi": "Dịp sinh nhật năm ngoái, tôi đã nhận được chiếc áo phông rất dễ thương. (Câu 19 trong bộ 40 câu ôn tập)",
                            "options": [
                                "コーヒー",
                                "みず",
                                "おちゃ",
                                "Tシャツ"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng quà tặng trang phục (Bài 6):</strong> Áo phông là <strong>Tシャツ</strong>."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "わあ、きれいな (   ) ですね。だれに もらいましたか。",
                            "promptVi": "Ôi, đồng hồ đẹp quá. Bạn nhận được từ ai vậy? (Câu 20 trong bộ 40 câu ôn tập)",
                            "options": [
                                "じしょ",
                                "まんが",
                                "てがみ",
                                "とけい"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng đồ dùng cá nhân (Bài 7):</strong> Chiếc đồng hồ là <strong>とけい</strong>."
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "あねは いま、ゲームの かいしゃで (   ) を して います。",
                            "promptVi": "Chị gái tôi bây giờ đang làm việc tại một công ty trò chơi. (Câu 16 trong bộ 40 câu ôn tập)",
                            "options": [
                                "仕事",
                                "食事",
                                "勉強",
                                "旅行"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Từ vựng nghề nghiệp (Bài 8):</strong> Làm việc tại công ty ➔ <strong>仕事</strong>を して います (しごとを して います). Chữ 仕 và 事 đều học ở Bài 8."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa gần nhất với câu gạch chân",
                    "groupInstruction": "Chọn từ hoặc cụm từ ngắn gọn mang ý nghĩa tương đương nhất với phần gạch chân:",
                    "items": [
                        {
                            "id": 6,
                            "type": "mc",
                            "prompt": "あしたの 朝 九時に しんじゅく駅の にしぐちで <u>あいましょう</u>。",
                            "promptVi": "Hẹn gặp nhau lúc 9h sáng mai ở cửa Tây ga Shinjuku nhé. (Câu 7 trong bộ 40 câu ôn tập)",
                            "options": [
                                "かえります",
                                "まちます",
                                "でんわします",
                                "やすみます"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Ngữ cảnh hẹn gặp (Bài 7):</strong> あいましょう (hãy gặp nhau nhé) ➔ <strong>まちます</strong> (sẽ đợi gặp nhau ở địa điểm đó). Chữ 朝, 九, 駅 đều đã học."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "あべさん、おそくなって すみません。時間を <u>まちがえました</u>…",
                            "promptVi": "Abe ơi xin lỗi mình đến muộn, mình bị nhầm thời gian hẹn... (Câu 10 trong bộ 40 câu ôn tập)",
                            "options": [
                                "おくれました",
                                "はやく きました",
                                "ちょうど つきました",
                                "わすれませんでした"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Ngữ cảnh cuộc hẹn (Bài 7):</strong> 時間を まちがえた (nhầm giờ hẹn) ➔ <strong>おくれました</strong> (bị trễ/muộn hẹn). Chữ 時間 đã học ở Bài 7."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "私は センターで <u>週に 三回</u> 日本語を 勉強して います。",
                            "promptVi": "Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. (Câu 32 trong bộ 40 câu ôn tập)",
                            "options": [
                                "一か月に 三回",
                                "まい日",
                                "一ねんに 三回",
                                "一週間に 三日"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Tần suất thời gian (Bài 9):</strong> 週に 三回 ＝ <strong>一週間に 三日</strong> (ba ngày trong một tuần). Chữ 週, 三, 回 đều đã học."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "<u>月に 五回</u> レストランへ 食べに 行きます。",
                            "promptVi": "Một tháng tôi đến nhà hàng ăn 5 lần. (Câu 32 trong bộ 40 câu ôn tập)",
                            "options": [
                                "一か月に 五回",
                                "いちねんに 五回",
                                "まい週 五回",
                                "まい日 五回"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Tần suất thời gian (Bài 9):</strong> 月に 五回 ＝ <strong>一か月に 五回</strong> (năm lần trong một tháng). Chữ 月, 五, 回 đều đã học."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "あねは ちゅうごくの ペキンに <u>すんで います</u>。",
                            "promptVi": "Chị gái tôi đang sống ở Bắc Kinh, Trung Quốc. (Câu 16 trong bộ 40 câu ôn tập)",
                            "options": [
                                "旅行して います",
                                "いえが あります",
                                "あそんで います",
                                "行って いません"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Động từ cư trú (Bài 1):</strong> すんで います (đang sinh sống) ＝ <strong>いえが あります</strong> (có nhà/định cư ở đó)."
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
                            "prompt": "わたしの 【母】は とても しんせつです。",
                            "promptVi": "Mẹ tôi rất tốt bụng.",
                            "options": [
                                "ちち",
                                "はは",
                                "あね",
                                "いもうと"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 母 (MẪU - Bài 1):</strong> Đọc là <strong>はは</strong> (mẹ mình). Chữ 父 (PHỤ - Bài 1) đọc là ちち (bố mình)."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "わたしの 【父】は まい朝 さんぽを します。",
                            "promptVi": "Bố tôi mỗi sáng đều đi dạo.",
                            "options": [
                                "はは",
                                "あに",
                                "おとうと",
                                "ちち"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ 父 (PHỤ - Bài 1):</strong> Đọc là <strong>ちち</strong> (bố mình)."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "あの 【男】の 人は だれですか。",
                            "promptVi": "Người đàn ông đằng kia là ai thế?",
                            "options": [
                                "おんな",
                                "ひと",
                                "おとこ",
                                "こども"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 男 (NAM - Bài 1):</strong> Đọc là <strong>おとこ</strong>. 男の人: おとこのひと (người đàn ông)."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "あそこで 【女】の 子が あそんで います。",
                            "promptVi": "Đằng kia có bé gái đang chơi đùa.",
                            "options": [
                                "おとこ",
                                "おんな",
                                "はは",
                                "ちち"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 女 (NỮ - Bài 1):</strong> Đọc là <strong>おんな</strong>. 女の子: おんなのこ (bé gái)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "センターで 【週】に 三回 勉強します。",
                            "promptVi": "Tôi học 3 lần một tuần ở trung tâm.",
                            "options": [
                                "かい",
                                "つき",
                                "しゅう",
                                "ねん"
                            ],
                            "correct": 2,
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
                            "prompt": "月に 五【かい】 レストランへ 行きます。",
                            "promptVi": "Mỗi tháng tôi đến nhà hàng 5 lần.",
                            "options": [
                                "週",
                                "回",
                                "時",
                                "間"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 回 (HỒI - Bài 10):</strong> Đọc là <strong>かい</strong> (số lần: 一回, 二回, 三回, 五回)."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "日本の 【ぶんか】を まなびたいです。",
                            "promptVi": "Tôi muốn học hỏi văn hóa Nhật Bản.",
                            "options": [
                                "音楽",
                                "文化",
                                "旅行",
                                "友達"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 文化 (VĂN HÓA - Bài 10):</strong> Đọc là <strong>ぶんか</strong>. Cả 2 chữ 文 và 化 đều học ở Bài 10."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "へやで 【おんがく】を ききます。",
                            "promptVi": "Tôi nghe nhạc ở trong phòng.",
                            "options": [
                                "文化",
                                "外国",
                                "日本語",
                                "音楽"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ 音楽 (ÂM NHẠC - Bài 10):</strong> Đọc là <strong>おんがく</strong>. Chữ 音 (Âm) và 楽 (Nhạc/Lạc) học ở Bài 10."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "夏やすみに 【りょこう】を します。",
                            "promptVi": "Nghỉ hè tôi đi du lịch.",
                            "options": [
                                "旅行",
                                "留学",
                                "食事",
                                "仕事"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ 旅行 (LỮ HÀNH - Bài 10):</strong> Đọc là <strong>りょこう</strong> (chuyến du lịch)."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "あしたは 【がっこう】が やすみです。",
                            "promptVi": "Ngày mai trường học được nghỉ.",
                            "options": [
                                "先生",
                                "友達",
                                "学校",
                                "留学生"
                            ],
                            "correct": 2,
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
                            "prompt": "ベトナムりょうりの つくりかたを おしえて (   )。",
                            "promptVi": "Bạn có thể chỉ cho tôi cách làm món ăn Việt Nam được không? (Câu 31 trong bộ 40 câu ôn tập)",
                            "options": [
                                "くださいませんか",
                                "くださいました",
                                "くれますか",
                                "あげますか"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cấu trúc nhờ vả lịch sự: V-て くださいませんか:</strong> Nhờ người khác chỉ bảo cho mình một cách tôn trọng, lịch sự."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "私は センターで 週 (   ) 三回 日本語を 勉強して います。",
                            "promptVi": "Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. (Câu 32 trong bộ 40 câu ôn tập)",
                            "options": [
                                "で",
                                "を",
                                "に",
                                "へ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Cấu trúc chỉ tần suất: [Đơn vị thời gian] に [Số lần] 回:</strong> 週に三回 (3 lần một tuần), 月に五回 (5 lần một tháng)."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "きれいな とけいですね。(   ) に もらいましたか。",
                            "promptVi": "Đồng hồ đẹp quá, bạn nhận được từ ai vậy? (Câu 20 trong bộ 40 câu ôn tập)",
                            "options": [
                                "だれ",
                                "どこ",
                                "いつ",
                                "なに"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cấu trúc nhận từ ai: [Người] に もらう:</strong> Từ để hỏi người nhận là <strong>だれに</strong> もらいましたか."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "あした、何時に (   ) か。",
                            "promptVi": "Ngày mai mấy giờ chúng ta gặp nhau thế? (Câu 7 trong bộ 40 câu ôn tập)",
                            "options": [
                                "あいまし",
                                "あう",
                                "あって",
                                "あいます"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Hỏi giờ gặp nhau: 何時に あいますか:</strong> Thể lịch sự ます đi với trợ từ nghi vấn か."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "あべさん、おそくなって すみません。時間を (   )…",
                            "promptVi": "Anh Abe ơi, mình xin lỗi vì đến muộn nhé. Mình bị nhầm thời gian hẹn... (Câu 10)",
                            "options": [
                                "まちがえます",
                                "わすれました",
                                "なくしました",
                                "まちがえました"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng nhầm lẫn: じかんを まちがえました:</strong> Tôi đã nhầm giờ hẹn."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "いつか、日本へ (   ) したいです。",
                            "promptVi": "Một ngày nào đó, tôi muốn đi du học ở Nhật Bản. (Câu 32 trong bộ 40 câu ôn tập)",
                            "options": [
                                "りゅうがく",
                                "りょこう",
                                "かいもの",
                                "さんぽ"
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
                            "prompt": "あしたの 朝 九時に [  ] [  ] [ ★ ] [  ] あいましょう。",
                            "promptVi": "9h sáng mai tại cổng tây ga Shinjuku nhé. (Câu 7)",
                            "options": [
                                "で",
                                "しんじゅく駅",
                                "にしぐち",
                                "の"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[2] しんじゅく駅 ➔ [4] の ➔ <strong>★ [3] にしぐち (Vị trí số 3)</strong> ➔ [1] で<br>➔ Câu hoàn chỉnh: あしたの 朝 九時に しんじゅく駅の にしぐちで あいましょう。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[3] にしぐち</strong>."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "prompt": "ベトナムりょうりの [  ] [  ] [ ★ ] [  ] くださいませんか。",
                            "promptVi": "Bạn có thể chỉ cho tôi cách làm món ăn Việt Nam không? (Câu 31)",
                            "options": [
                                "私に",
                                "つくりかた",
                                "おしえて",
                                "を"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[2] つくりかた ➔ [4] を ➔ <strong>★ [1] 私に (Vị trí số 3)</strong> ➔ [3] おしえて<br>➔ Câu hoàn chỉnh: ベトナムりょうりの つくりかたを 私に おしえて くださいませんか。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[1] 私に</strong>."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "prompt": "私は センターで [  ] [  ] [ ★ ] [  ] 勉強して います。",
                            "promptVi": "Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. (Câu 32)",
                            "options": [
                                "三回",
                                "を",
                                "週に",
                                "日本語"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] 週に ➔ [1] 三回 ➔ <strong>★ [4] 日本語 (Vị trí số 3)</strong> ➔ [2] を<br>➔ Câu hoàn chỉnh: 私は センターで 週に 三回 日本語を 勉強して います。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[4] 日本語</strong>."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "prompt": "あねは いま、[  ] [  ] [ ★ ] [  ] して います。",
                            "promptVi": "Chị tôi đang làm việc tại công ty trò chơi. (Câu 16)",
                            "options": [
                                "かいしゃで",
                                "仕事",
                                "ゲームの",
                                "を"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] ゲームの ➔ [1] かいしゃで ➔ <strong>★ [2] 仕事 (Vị trí số 3)</strong> ➔ [4] を<br>➔ Câu hoàn chỉnh: あねは いま、ゲームの かいしゃで 仕事を して います。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[2] 仕事</strong>."
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
                            "reference": "あした 十時に ホテルの ロビーで あいましょう。",
                            "acceptAnswers": [
                                "あした 十時に ホテルの ロビーで あいましょう。",
                                "あした 10時に ホテルの ロビーで あいましょう。",
                                "あした 10じに ホテルの ロビーで あいましょう。",
                                "あした 10時に ホテルの ロビーで あいましょうね。",
                                "あした 十時に ホテルロビーで あいましょう。",
                                "あした 10時に ほてるの ろびーで あいましょう。"
                            ],
                            "hints": [
                                "あした 十時に",
                                "ホテルの ロビーで",
                                "あいましょう (あいましょう)"
                            ]
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "prompt": "Bạn có thể chỉ cho tôi cách làm món ăn Việt Nam không?",
                            "promptVi": "Câu 31 trong bộ 40 câu ôn tập",
                            "reference": "ベトナムりょうりの つくりかたを おしえて くださいませんか。",
                            "acceptAnswers": [
                                "ベトナムりょうりの つくりかたを おしえて くださいませんか。",
                                "ベトナムりょうりの つくりかたを おしえて ください。",
                                "ベトナムりょうりの つくりかたを おしえてくださいませんか。",
                                "ベトナムりょうりの つくりかたを おしえて もらえませんか。",
                                "ベトナムりょうりの つくりかたを おしえて くれませんか。",
                                "ベトナムの りょうりの つくりかたを おしえて ください。",
                                "べとなむりょうりの つくりかたを おしえて くださいませんか。"
                            ],
                            "hints": [
                                "ベトナムりょうりの",
                                "つくりかたを",
                                "おしえて くださいませんか"
                            ]
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
            "passage": "ナムさんへ。\nメッセージを ありがとうございます。\nあしたの にちようび、十時に ホテルの ロビーで あいましょう。\nあきはばらは でんきやが 多くて、とても べんりですから、いっしょに 行って でんしじしょを みませんか。\nかいものの 後で、おいしい 日本りょうりを たべましょう。\nもし 時間に おくれたら、れんらくを して くださいね。\nさとうより",
            "passageVi": "Gửi bạn Nam.\nCảm ơn tin nhắn của bạn.\nChủ nhật ngày mai chúng ta gặp nhau lúc 10 giờ ở sảnh khách sạn nhé.\nAkihabara có nhiều tiệm điện tử và rất tiện lợi, bạn cùng đi xem kim từ điển với mình nhé.\nSau khi mua sắm, chúng mình cùng đi ăn món Nhật ngon lành nhé.\nNếu bị muộn giờ thì hãy liên lạc cho mình nhé.\nTừ Sato",
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "さとうさんと ナムさんは あした 何時に あいますか。",
                    "promptVi": "Sato và Nam ngày mai sẽ gặp nhau lúc mấy giờ?",
                    "options": [
                        "九時",
                        "七時",
                        "十時",
                        "十二時"
                    ],
                    "correct": 2,
                    "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「十時に ホテルの ロビーで あいましょう」 ➔ Hẹn gặp lúc 10 giờ."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "ふたりは あきはばらで 何を しますか。",
                    "promptVi": "Hai người họ sẽ làm gì ở Akihabara?",
                    "options": [
                        "ホテルに とまります。",
                        "でんしじしょを みて、日本りょうりを たべます。",
                        "学校で 勉強します。",
                        "でんしゃの きっぷを かいます。"
                    ],
                    "correct": 1,
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
                    "modelAnswer": "きょねんの たんじょうびに、友達に 白い かわいい シャツを もらいました。そして、父と 母に きれいな とけいを もらいました。とても うれしかったです。",
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
                    "modelAnswer": "私の 町には 外国人が たくさん います。町の なかに、日本の 文化センターが あります。私は センターで 週に 三回 日本語を 勉強して います。そして、日本りょうりが 好きですから、月に 五回 レストランへ たべに 行きます。いつか、日本へ 留学生として 行きたいです。",
                    "modelVi": "Thành phố của tôi có nhiều người nước ngoài. Trong thành phố có trung tâm văn hóa Nhật Bản. Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. Và tôi thích món ăn Nhật nên một tháng tôi đến nhà hàng ăn năm lần. Một ngày nào đó, tôi muốn đến Nhật Bản với tư cách là một lưu học sinh.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; bám sát câu 32 bộ ôn tập, vận dụng chính xác cấu trúc tần suất (週に三回, 月に五回) và nguyện vọng tương lai (～たいです)."
                }
            ]
        }
    ]
}

def build_m104():
    return DATA_M104
