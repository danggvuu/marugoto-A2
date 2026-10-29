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

DATA_M103 = {
    "code": "M103",
    "name": "Mã Đề M103 (Chỉ Đường, Không Gian & Thời Tiết 4 Mùa)",
    "tag": "🗺️ Phương Hướng • Màu Sắc • Khí Hậu 4 Mùa • Chuẩn A2-1",
    "desc": "Đề chuyên sâu về chỉ dẫn đường đi (まっすぐ, 右, 左, かどを曲がる), miêu tả màu sắc hình dáng tòa nhà (赤, 青, 白, 黒), và thời tiết các mùa (春, 夏, 秋, 冬, 天気, 雨, 雪, 風, 雲).",
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
                            "prompt": "あそこに (   ) はしが みえますか。",
                            "promptVi": "Bạn có nhìn thấy cây cầu màu đỏ ở đằng kia không? (Câu 5 trong bộ 40 câu ôn tập)",
                            "options": [
                                "青い",
                                "白い",
                                "黒い",
                                "赤い"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng màu sắc (Bài 6):</strong> Cây cầu màu đỏ ➔ <strong>赤い</strong> (あかい). Các màu khác: 青い (xanh), 白い (trắng), 黒い (đen)."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "この 道を (   ) 行って ください。はくぶつかんは 左がわに あります。",
                            "promptVi": "Hãy đi thẳng con đường này. Bảo tàng ở bên tay trái. (Câu 6 trong bộ 40 câu ôn tập)",
                            "options": [
                                "まっすぐ",
                                "ゆっくり",
                                "たくさん",
                                "あまり"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Phó từ chỉ phương hướng (Bài 6):</strong> <strong>まっすぐ</strong> (thẳng, đi thẳng: まっすぐ行く)."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "あそこに まるくて (   ) たてものが みえますか。",
                            "promptVi": "Bạn có nhìn thấy tòa nhà hình tròn, thú vị ở đằng kia không? (Câu 8 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ふるい",
                                "たかい",
                                "すくない",
                                "おもしろい"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng tính từ (Bài 6):</strong> まるくて (tròn và) ＋ <strong>おもしろい</strong> (thú vị, lạ mắt)."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "私の いえの となりに 青くて (   ) たてものが あります。",
                            "promptVi": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài. (Câu 9 trong bộ 40 câu ôn tập)",
                            "options": [
                                "まるい",
                                "ひろい",
                                "やすい",
                                "ほそながい"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng hình dáng (Bài 6):</strong> <strong>ほそながい</strong> (thon dài, mảnh khảnh). 青くて ほそながい: màu xanh và thon dài."
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "うえのこうえんは とても 広くて (   ) です。なかに どうぶつえんが あります。",
                            "promptVi": "Công viên Ueno rất rộng và nổi tiếng. Bên trong có sở thú. (Câu 1 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ゆうめい",
                                "べんり",
                                "しずか",
                                "すき"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Từ vựng miêu tả thành phố (Bài 5):</strong> 広くて <strong>ゆうめい</strong> (rộng rãi và nổi tiếng)."
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
                            "prompt": "ハノイの 秋は <u>きれいで</u>、しずかです。",
                            "promptVi": "Mùa thu Hà Nội rất đẹp và yên bình. (Câu 33 trong bộ 40 câu ôn tập)",
                            "options": [
                                "きたなくて",
                                "あつくて",
                                "すてきで",
                                "うるさくて"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Tính từ khen ngợi (Bài 3):</strong> きれい (đẹp, thanh lịch) ＝ <strong>すてき</strong> (tuyệt vời, tươi đẹp). Chữ 秋 (Thu) đã học ở Bài 3."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "私の いえの となりに 青くて <u>ほそながい</u> たてものが あります。",
                            "promptVi": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài. (Câu 9 trong bộ 40 câu ôn tập)",
                            "options": [
                                "まるくて おおきい",
                                "ひろくて ひくい",
                                "ながくて ほそい",
                                "みじかくて おもい"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Tính từ ghép hình dáng (Bài 5):</strong> ほそながい ＝ <strong>ながくて ほそい</strong> (thon và dài)."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "たいふうで、でんしゃと バスが <u>止まりました</u>。",
                            "promptVi": "Vì bão nên tàu điện và xe buýt đã dừng chạy. (Câu 35 trong bộ 40 câu ôn tập)",
                            "options": [
                                "はしりました",
                                "うごきませんでした",
                                "つきました",
                                "でました"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Động từ chỉ trạng thái giao thông (Bài 4):</strong> 止まりました (đã dừng lại) ＝ <strong>うごきませんでした</strong> (đã không di chuyển/hoạt động). Chữ 止 đã học ở Bài 7."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "お母さんは とても かわいくて、<u>しんせつな</u> 人です。",
                            "promptVi": "Mẹ tôi là người rất dễ thương và tốt bụng. (Câu 20 trong bộ 40 câu ôn tập)",
                            "options": [
                                "やさしい",
                                "こわい",
                                "きびしい",
                                "つめたい"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Tính từ tính cách (Bài 1):</strong> しんせつな (tốt bụng, ân cần) ＝ <strong>やさしい</strong> (hiền hậu, tốt bụng). Chữ 母 và 人 đều đã học."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "十二月ごろ、さむく なりますから、<u>あまり 外へ 出ません</u>。",
                            "promptVi": "Khoảng tháng 12 trời trở lạnh nên tôi không hay ra ngoài lắm. (Câu 33 trong bộ 40 câu ôn tập)",
                            "options": [
                                "まい日 外へ 出る",
                                "旅行に よく 行く",
                                "うちに いる ことが 多い",
                                "外で あそぶ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Cách nói tương đương sinh hoạt (Bài 3-4):</strong> あまり 外へ 出ません (ít khi ra ngoài) ＝ <strong>うちに いる ことが 多い</strong> (thường ở trong nhà). Chữ 外, 出, 多 đều đã học."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec2_kanji",
            "partNumber": "II",
            "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
            "partDesc": "Kiểm tra nhận diện âm Hiragana và chữ Hán chủ đề thiên nhiên, thời tiết, phương hướng (Bài 1 - 10).",
            "badge": "25 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                    "groupInstruction": "Chọn âm đọc chính xác của chữ Hán trong câu:",
                    "items": [
                        {
                            "id": 11,
                            "type": "mc",
                            "prompt": "ハノイは 九月ごろ 【秋】に なります。",
                            "promptVi": "Hà Nội khoảng tháng 9 sang mùa thu.",
                            "options": [
                                "はる",
                                "なつ",
                                "ふゆ",
                                "あき"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ 秋 (THU - Bài 3):</strong> Đọc là <strong>あき</strong> (mùa thu). Phân biệt: 春 (はる - xuân), 夏 (なつ - hạ), 冬 (ふゆ - đông)."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "きょうは 【天気】が とても いいです。",
                            "promptVi": "Hôm nay thời tiết rất đẹp.",
                            "options": [
                                "てんき",
                                "でんき",
                                "げんき",
                                "くうき"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ 天気 (THIÊN KHÍ - Bài 4):</strong> Đọc là <strong>てんき</strong> (thời tiết)."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "きのう、白い 【雪】が ふりました。",
                            "promptVi": "Hôm qua tuyết trắng đã rơi.",
                            "options": [
                                "あめ",
                                "くも",
                                "かぜ",
                                "ゆき"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ 雪 (TUYẾT - Bài 4):</strong> Đọc là <strong>ゆき</strong> (tuyết). Phân biệt: 雨 (あめ - mưa), 雲 (くも - mây), 風 (かぜ - gió)."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "その かどを 【右】に まがって ください。",
                            "promptVi": "Hãy rẽ phải ở góc đường đó.",
                            "options": [
                                "ひだり",
                                "まえ",
                                "みぎ",
                                "うしろ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 右 (HỮU - Bài 6):</strong> Đọc là <strong>みぎ</strong> (bên phải). Chữ 左 (TẢ - Bài 6) đọc là ひだり (bên trái)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "はくぶつかんは 【左】がわに あります。",
                            "promptVi": "Bảo tàng nằm ở phía bên trái.",
                            "options": [
                                "ひだり",
                                "みぎ",
                                "きた",
                                "みなみ"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ 左 (TẢ - Bài 6):</strong> Đọc là <strong>ひだり</strong> (bên trái)."
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
                            "prompt": "春には きれいな 【はな】が さきます。",
                            "promptVi": "Vào mùa xuân có hoa đẹp nở rộ.",
                            "options": [
                                "海",
                                "花",
                                "山",
                                "川"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 花 (HOA - Bài 3):</strong> Đọc là <strong>はな</strong> (bông hoa). Phân biệt: 海 (うみ - biển), 山 (やま - núi), 川 (かわ - sông)."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "きょうは 【あめ】が ふって います。",
                            "promptVi": "Hôm nay trời đang mưa.",
                            "options": [
                                "雪",
                                "雲",
                                "雨",
                                "風"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 雨 (VŨ - Bài 4):</strong> Đọc là <strong>あめ</strong> (cơn mưa)."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "つよい 【かぜ】が ふいて います。",
                            "promptVi": "Gió mạnh đang thổi.",
                            "options": [
                                "雨",
                                "空",
                                "風",
                                "気"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 風 (PHONG - Bài 4):</strong> Đọc là <strong>かぜ</strong> (ngọn gió)."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "青い 【そら】が ひろがって います。",
                            "promptVi": "Bầu trời xanh trải rộng bao la.",
                            "options": [
                                "晴",
                                "空",
                                "雲",
                                "海"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 空 (KHÔNG - Bài 4):</strong> Đọc là <strong>そら</strong> (bầu trời)."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "この 【まち】には 外国人が 多いです。",
                            "promptVi": "Ở thị trấn này có nhiều người nước ngoài.",
                            "options": [
                                "店",
                                "町",
                                "道",
                                "駅"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 町 (ĐINH - Bài 5):</strong> Đọc là <strong>まち</strong> (thị trấn, phố xá). 店 (みせ), 道 (みち), 駅 (えき)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec3_grammar",
            "partNumber": "III",
            "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
            "partDesc": "Kiểm tra ngữ pháp phương hướng, tính từ nối, trợ từ nguyên nhân và so sánh.",
            "badge": "25 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Chọn phương án đúng nhất điền vào chỗ trống",
                    "groupInstruction": "Chọn từ/thể ngữ pháp chính xác nhất điền vào chỗ trống trong ngoặc (   ):",
                    "items": [
                        {
                            "id": 21,
                            "type": "mc",
                            "prompt": "一ばんめの かどを 右 (   ) まがって ください。",
                            "promptVi": "Hãy rẽ phải ở góc đường thứ nhất. (Câu 6 trong bộ 40 câu ôn tập)",
                            "options": [
                                "を",
                                "で",
                                "へ",
                                "に"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Cấu trúc rẽ hướng: [Hướng] に まがる:</strong> Rẽ sang bên phải ➔ <strong>右に まがる</strong>. Lưu ý góc đường dùng trợ từ を (かどを)."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "ハノイの 秋は きれい (   )、しずかです。",
                            "promptVi": "Mùa thu của Hà Nội thì đẹp và yên bình. (Câu 33 trong bộ 40 câu ôn tập)",
                            "options": [
                                "くて",
                                "で",
                                "くては",
                                "な"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Cấu trúc nối Tính từ đuôi な: Tính từ (bỏ な) + で:</strong> きれい (Tính từ đuôi な) ➔ <strong>きれいで</strong>, しずかです."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "十二月ごろ、さむく (   ) から、あまり 外へ 出ません。",
                            "promptVi": "Khoảng tháng 12 trời trở lạnh nên tôi không hay ra ngoài lắm. (Câu 33 trong bộ 40 câu ôn tập)",
                            "options": [
                                "します",
                                "あります",
                                "なります",
                                "行きます"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Cấu trúc biến đổi trạng thái tự nhiên: Tính từ đuôi い (bỏ い) + く なります:</strong> さむい ➔ <strong>さむく なります</strong> (trở nên lạnh)."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "夜は、道も しずかに (   )。",
                            "promptVi": "Buổi đêm, đường phố cũng trở nên yên tĩnh hơn. (Câu 33 trong bộ 40 câu ôn tập)",
                            "options": [
                                "します",
                                "できます",
                                "きます",
                                "なります"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Cấu trúc biến đổi tính từ đuôi な: Tính từ (bỏ な) + に なります:</strong> しずか ➔ <strong>しずかに なります</strong> (trở nên yên tĩnh)."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "あさひはくぶつかんへ 行きたいんですが、(   ) 行きますか。",
                            "promptVi": "Tôi muốn đi đến viện bảo tàng Asahi, đi như thế nào? (Câu 6 trong bộ 40 câu ôn tập)",
                            "options": [
                                "いくらで",
                                "どうやって",
                                "だれと",
                                "なぜ"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Từ để hỏi cách thức/đường đi: どうやって:</strong> 'Đi như thế nào / bằng cách nào?' ➔ <strong>どうやって 行きますか</strong>."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "この ところには かわいい ふくやが (   ) あります。",
                            "promptVi": "Ở khu vực này có nhiều cửa hàng thời trang dễ thương. (Câu 3 trong bộ 40 câu ôn tập)",
                            "options": [
                                "すこし",
                                "たくさん",
                                "あまり",
                                "ぜんぜん"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Phó từ chỉ số lượng nhiều: たくさん:</strong> Có rất nhiều tiệm quần áo dễ thương."
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
                            "prompt": "あさひはくぶつかんは [  ] [  ] [ ★ ] [  ] あります。",
                            "promptVi": "Bảo tàng Asahi ở bên tay trái. (Câu 6)",
                            "options": [
                                "の",
                                "左がわ",
                                "に",
                                "道"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[4] 道 ➔ [1] の ➔ <strong>★ [2] 左がわ (Vị trí số 3)</strong> ➔ [3] に<br>➔ Câu hoàn chỉnh: あさひはくぶつかんは 道の 左がわに あります。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[2] 左がわ</strong>."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "prompt": "私の [  ] [  ] [ ★ ] [  ] たてものが あります。",
                            "promptVi": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài. (Câu 9 trong bộ 40 câu ôn tập)",
                            "options": [
                                "青くて",
                                "ほそながい",
                                "いえの",
                                "となりに"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] いえの ➔ [4] となりに ➔ <strong>★ [1] 青くて (Vị trí số 3)</strong> ➔ [2] ほそながい<br>➔ Câu hoàn chỉnh: 私の いえの となりに 青くて ほそながい たてものが あります。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[1] 青くて</strong>."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "prompt": "ハノイは [  ] [  ] [ ★ ] [  ] なります。",
                            "promptVi": "Hà Nội thì khoảng tháng 9 sẽ chuyển sang mùa thu. (Câu 33)",
                            "options": [
                                "に",
                                "きれいな",
                                "九月ごろ",
                                "秋"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] 九月ごろ ➔ [2] きれいな ➔ <strong>★ [4] 秋 (Vị trí số 3)</strong> ➔ [1] に<br>➔ Câu hoàn chỉnh: ハノイは 九月ごろ きれいな 秋に なります。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[4] 秋</strong>."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "prompt": "あそこに [  ] [  ] [ ★ ] [  ] みえますか。",
                            "promptVi": "Bạn có nhìn thấy cây cầu màu đỏ ở đằng kia không? (Câu 5)",
                            "options": [
                                "よく",
                                "赤い",
                                "が",
                                "はし"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[2] 赤い ➔ [4] はし ➔ <strong>★ [3] が (Vị trí số 3)</strong> ➔ [1] よく<br>➔ Câu hoàn chỉnh: あそこに 赤い はしが よく みえますか。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[3] が</strong>."
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
                            "prompt": "Bạn có nhìn thấy cây cầu màu đỏ ở đằng kia không?",
                            "promptVi": "Câu 5 trong bộ 40 câu ôn tập",
                            "reference": "あそこに 赤い はしが みえますか。",
                            "acceptAnswers": [
                                "あそこに 赤い はしが みえますか。",
                                "あそこの 赤い はしが みえますか。",
                                "あそこに 赤いはしが みえますか。",
                                "あそこに あかい はしが みえますか。",
                                "あちらに 赤い はしが みえますか。",
                                "あそこに 赤い はしが ありますか。"
                            ],
                            "hints": [
                                "あそこに / あそこの",
                                "赤い (あかい) はしが",
                                "みえますか"
                            ]
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "prompt": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài.",
                            "promptVi": "Câu 9 trong bộ 40 câu ôn tập",
                            "reference": "私の いえの となりに 青くて ほそながい たてものが あります。",
                            "acceptAnswers": [
                                "私の いえの となりに 青くて ほそながい たてものが あります。",
                                "わたしの いえの となりに 青くて ほそながい たてものが あります。",
                                "いえの となりに 青くて ほそながい たてものが あります。",
                                "私の いえの ちかくに 青くて ほそながい たてものが あります。",
                                "わたしの いえの となりに あおくて ほそながい たてものが あります。",
                                "私の いえの となりに 青くて ながくて ほそい たてものが あります。",
                                "私の うちの となりに 青くて ほそながい たてものが あります。"
                            ],
                            "hints": [
                                "私の いえの となりに",
                                "青くて ほそながい",
                                "たてものが あります"
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
            "partDesc": "Đọc bài viết về khí hậu mùa thu Hà Nội và mùa đông và chọn đáp án đúng nhất (Câu 33-34).",
            "badge": "10 Điểm",
            "passage": "ハノイは 九月ごろ 秋に なります。ハノイの 秋は きれいで、しずかです。\n私は よく ふるい まちへ しゃしんを とりに 行きます。\nでも、十二月ごろに なると、とても さむく なりますから、あまり 外へ 出ません。\n夜は、道も しずかに なります。\n日本は 十二月から 二月まで 冬です。雪が たくさん ふりますから、白い 山が とても きれいです。\nわたしは いつか 冬の 日本へ 行って、雪を みてみたいです。",
            "passageVi": "Hà Nội khoảng tháng 9 sang mùa thu. Mùa thu Hà Nội rất đẹp và yên bình.\nTôi thường đến khu phố cổ chụp ảnh.\nNhưng đến khoảng tháng 12, trời trở nên rất lạnh nên tôi không hay ra ngoài lắm.\nBuổi đêm, đường phố cũng trở nên vắng lặng hơn.\nỞ Nhật Bản, từ tháng 12 đến tháng 2 là mùa đông. Tuyết rơi rất nhiều nên những ngọn núi phủ tuyết trắng rất đẹp.\nMột ngày nào đó tôi muốn đến Nhật Bản vào mùa đông để ngắm tuyết.",
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "この 人は なぜ 十二月に あまり 外へ 出ませんか。",
                    "promptVi": "Tại sao vào tháng 12 người này lại không hay ra ngoài?",
                    "options": [
                        "とても さむく なりますから。",
                        "雨が たくさん ふりますから。",
                        "学校の テストが ありますから。",
                        "まちが にぎやかですから。"
                    ],
                    "correct": 0,
                    "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「とても さむく なりますから、あまり 外へ 出ません」 ➔ Vì trời trở nên rất lạnh."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "この 人は 日本の 冬の 何を みてみたいと いって いますか。",
                    "promptVi": "Người này muốn ngắm điều gì ở mùa đông Nhật Bản?",
                    "options": [
                        "雪",
                        "花",
                        "海",
                        "川"
                    ],
                    "correct": 0,
                    "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「雪を みてみたいです」 ➔ Muốn ngắm tuyết (chữ 雪 - Tuyết học ở Bài 4)."
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
                    "prompt": "あなたの いえの ちかくには どんな たてものが ありますか。（いろや かたちを おしえて ください）",
                    "promptVi": "Gần nhà bạn có những tòa nhà như thế nào? Hãy miêu tả màu sắc và hình dáng của chúng.",
                    "minWords": 30,
                    "placeholder": "Gõ câu trả lời tiếng Nhật tại đây... Ví dụ: 私の いえの ちかくに 青くて たかい たてものが あります...",
                    "hints": [
                        "Vị trí: 私の いえの ちかくに / となりに...",
                        "Màu sắc & Hình dáng: 赤くて / 青くて / 白くて / まるくて / ほそながい たてもの",
                        "Tên tòa nhà: スーパー / 駅 / カフェ / 店"
                    ],
                    "modelAnswer": "私の いえの ちかくには、青くて ほそながい たてものが あります。そして、駅の 前に 白くて おおきい スーパーも あります。とても べんりで、きれいな まちです。",
                    "modelVi": "Gần nhà tôi có một tòa nhà màu xanh và thon dài. Và trước ga cũng có một siêu thị màu trắng rất to. Đây là một khu phố rất tiện lợi và sạch đẹp.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Vận dụng đúng các từ vựng chỉ màu sắc (青くて, 白くて) và phương hướng vị trí (ちかく, 前)."
                },
                {
                    "id": 36,
                    "type": "essay",
                    "prompt": "あなたの 国の きせつと 天気について おしえて ください。（すきな きせつ、てんき、その とき することなど、五十じ いじょう）",
                    "promptVi": "Hãy viết đoạn văn giới thiệu về các mùa và thời tiết ở đất nước của bạn (mùa bạn thích, thời tiết, hoạt động thường làm... tối thiểu 50 chữ/ký tự).",
                    "minWords": 50,
                    "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: ベトナムの ハノイは 九月ごろ 秋に なります...",
                    "hints": [
                        "Giới thiệu mùa: ベトナムは 九月ごろ 秋に なります / 私の くには 四つの 季節が あります",
                        "Miêu tả thời tiết: 秋は 天気が よくて、すずしいです / 冬は さむいです",
                        "Hoạt động: 私は よく まちへ 行って しゃしんを とります / 友だちと お茶を 飲みます",
                        "Độ dài: Tối thiểu 50 chữ/ký tự"
                    ],
                    "modelAnswer": "ベトナムの ハノイは 九月ごろ 秋に なります。ハノイの 秋は 天気が よくて、とても すずしいです。まちの 道には きれいな 花が たくさん さきます。わたしは 秋が いちばん 好きですから、やすみの 日に 友達と まちへ 行って、しゃしんを たくさん とります。夜も しずかで、とても すみやすいです。",
                    "modelVi": "Hà Nội ở Việt Nam khoảng tháng 9 thì sang thu. Mùa thu Hà Nội thời tiết đẹp và rất mát mẻ. Trên các con đường trong phố có nhiều hoa đẹp nở rộ. Tôi thích mùa thu nhất, nên vào ngày nghỉ tôi thường cùng bạn bè lên phố chụp nhiều ảnh. Buổi đêm cũng yên tĩnh, rất dễ chịu.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; miêu tả rõ ràng thời tiết (天気がいい, すずしい), mùa (秋), hoạt động cá nhân và cảm nhận."
                }
            ]
        }
    ]
}

def build_m103():
    return DATA_M103
