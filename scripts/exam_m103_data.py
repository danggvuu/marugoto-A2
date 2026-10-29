#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/exam_m103_data.py
Mã đề M103: Đề Chuyên Sâu Chỉ Đường, Mô Tả Không Gian & Thời Tiết 4 Mùa (Bài 1 - 10)
Chuẩn Can-do giáo viên 10 năm kinh nghiệm - Tuyệt đối không dùng chữ Hán chưa học.
"""

import re
try:
    from scripts.exam_m101_data import PERMITTED_KANJI, v
except ImportError:
    from exam_m101_data import PERMITTED_KANJI, v

def build_m103():
    return {
        "code": "M103",
        "name": "Mã Đề M103 (Chỉ Đường, Không Gian & Thời Tiết 4 Mùa)",
        "tag": "🗺️ Phương Hướng • Màu Sắc • Khí Hậu 4 Mùa • Chuẩn A2-1",
        "desc": "Đề chuyên sâu về chỉ dẫn đường đi (まっすぐ, 右, 左, かどを曲がる), miêu tả màu sắc hình dáng tòa nhà (赤, 青, 白, 黒), và thời tiết các mùa (春, 夏, 秋, 冬, 天気, 雨, 雪, 風, 雲).",
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
                                "prompt": v("あそこに (   ) はしが みえますか。", "M103.Q1.p"),
                                "promptVi": "Bạn có nhìn thấy cây cầu màu đỏ ở đằng kia không? (Câu 5 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("赤い", "M103.Q1.o0"),
                                    v("青い", "M103.Q1.o1"),
                                    v("白い", "M103.Q1.o2"),
                                    v("黒い", "M103.Q1.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng màu sắc (Bài 6):</strong> Cây cầu màu đỏ ➔ <strong>赤い</strong> (あかい). Các màu khác: 青い (xanh), 白い (trắng), 黒い (đen)."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": v("この 道を (   ) 行って ください。はくぶつかんは 左がわに あります。", "M103.Q2.p"),
                                "promptVi": "Hãy đi thẳng con đường này. Bảo tàng ở bên tay trái. (Câu 6 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("まっすぐ", "M103.Q2.o0"),
                                    v("ゆっくり", "M103.Q2.o1"),
                                    v("たくさん", "M103.Q2.o2"),
                                    v("あまり", "M103.Q2.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Phó từ chỉ phương hướng (Bài 6):</strong> <strong>まっすぐ</strong> (thẳng, đi thẳng: まっすぐ行く)."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": v("あそこに まるくて (   ) たてものが みえますか。", "M103.Q3.p"),
                                "promptVi": "Bạn có nhìn thấy tòa nhà hình tròn, thú vị ở đằng kia không? (Câu 8 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("おもしろい", "M103.Q3.o0"),
                                    v("ふるい", "M103.Q3.o1"),
                                    v("たかい", "M103.Q3.o2"),
                                    v("すくない", "M103.Q3.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng tính từ (Bài 6):</strong> まるくて (tròn và) ＋ <strong>おもしろい</strong> (thú vị, lạ mắt)."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": v("私の いえの となりに 青くて (   ) たてものが あります。", "M103.Q4.p"),
                                "promptVi": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài. (Câu 9 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ほそながい", "M103.Q4.o0"),
                                    v("まるい", "M103.Q4.o1"),
                                    v("ひろい", "M103.Q4.o2"),
                                    v("やすい", "M103.Q4.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng hình dáng (Bài 6):</strong> <strong>ほそながい</strong> (thon dài, mảnh khảnh). 青くて ほそながい: màu xanh và thon dài."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": v("うえのこうえんは とても 広くて (   ) です。なかに どうぶつえんが あります。", "M103.Q5.p"),
                                "promptVi": "Công viên Ueno rất rộng và nổi tiếng. Bên trong có sở thú. (Câu 1 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ゆうめい", "M103.Q5.o0"),
                                    v("べんり", "M103.Q5.o1"),
                                    v("しずか", "M103.Q5.o2"),
                                    v("すき", "M103.Q5.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng miêu tả thành phố (Bài 5):</strong> 広くて <strong>ゆうめい</strong> (rộng rãi và nổi tiếng)."
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
                                "prompt": v("<u>ハノイは 九月ごろ 秋に なります。ハノイの 秋は きれいで、しずかです。</u>", "M103.Q6.p"),
                                "promptVi": "Hà Nội khoảng tháng 9 chuyển sang mùa thu. Mùa thu Hà Nội đẹp và yên bình. (Câu 33)",
                                "options": [
                                    v("九月になると、ハノイは きれいで しずかな 秋を むかえます。", "M103.Q6.o0"),
                                    v("ハノイの 秋は いつも 雨が ふって にぎやかです。", "M103.Q6.o1"),
                                    v("ハノイには 秋が ありません。", "M103.Q6.o2"),
                                    v("九月の ハノイは とても あついです。", "M103.Q6.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Ý nghĩa tương đương:</strong> Vào khoảng tháng 9, Hà Nội bước vào mùa thu đẹp và yên bình (<strong>きれいで しずかな 秋</strong>)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": v("<u>きょうとは とても きれいで、ふるい おてらが たくさん ある 町です。</u>", "M103.Q7.p"),
                                "promptVi": "Kyoto là thành phố rất đẹp và có nhiều ngôi chùa cổ. (Câu 25 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("きょうとは きれいで、ふるい おてらが 多い 町です。", "M103.Q7.o0"),
                                    v("きょうとには おてらが ぜんぜん ありません。", "M103.Q7.o1"),
                                    v("きょうとは あたらしい たてものだけの まちです。", "M103.Q7.o2"),
                                    v("きょうとは あまり きれいでは ありません。", "M103.Q7.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ đồng nghĩa: たくさんある = 多い (nhiều):</strong> きょうとは きれいで、ふるい おてらが 多い 町です."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": v("<u>たいふうで、でんしゃと バスが 止まりました。</u>", "M103.Q8.p"),
                                "promptVi": "Vì bão, nên tàu điện và xe buýt dừng chạy. (Câu 35 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("たいふうが きたので、でんしゃも バスも うごきませんでした。", "M103.Q8.o0"),
                                    v("たいふうでも でんしゃと バスは はしりました。", "M103.Q8.o1"),
                                    v("天気は いいですが、でんしゃが 止まりました。", "M103.Q8.o2"),
                                    v("たいふうの とき、バスだけが はしりました。", "M103.Q8.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tương đương ý nghĩa: 止まりました = うごきませんでした (không chạy/không di chuyển).</strong>"
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": v("<u>お母さんは とても かわいくて、しんせつな 人です。</u>", "M103.Q9.p"),
                                "promptVi": "Mẹ tôi là người rất dễ thương và tốt bụng. (Câu 23 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("母は やさしくて、とても すてきな 人です。", "M103.Q9.o0"),
                                    v("母は こわくて、きびしい 人です。", "M103.Q9.o1"),
                                    v("母は あまり はなしません。", "M103.Q9.o2"),
                                    v("母は いつも おこって います。", "M103.Q9.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Đồng nghĩa phẩm chất: しんせつ = やさしい (tốt bụng, hiền hậu, tử tế).</strong>"
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": v("<u>十二月ごろ、さむく なりますから、あまり 外へ 出ません。</u>", "M103.Q10.p"),
                                "promptVi": "Khoảng tháng 12 trời trở lạnh nên tôi không hay ra ngoài lắm. (Câu 33)",
                                "options": [
                                    v("十二月は さむいので、うちに いる ことが 多いです。", "M103.Q10.o0"),
                                    v("十二月は あたたかいので、まい日 外へ 行きます。", "M103.Q10.o1"),
                                    v("さむいですが、よく 外で あそびます。", "M103.Q10.o2"),
                                    v("十二月は 旅行に ばかり 行きます。", "M103.Q10.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Đồng nghĩa hành động: あまり外へ出ません (ít khi ra ngoài) = うちにいることが多い (thường ở nhà).</strong>"
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
                                "prompt": v("ハノイは 九月ごろ 【秋】に なります。", "M103.Q11.p"),
                                "promptVi": "Hà Nội khoảng tháng 9 sang mùa thu.",
                                "options": [
                                    v("あき", "M103.Q11.o0"),
                                    v("はる", "M103.Q11.o1"),
                                    v("なつ", "M103.Q11.o2"),
                                    v("ふゆ", "M103.Q11.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 秋 (THU - Bài 3):</strong> Đọc là <strong>あき</strong> (mùa thu). Phân biệt: 春 (はる - xuân), 夏 (なつ - hạ), 冬 (ふゆ - đông)."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": v("きょうは 【天気】が とても いいです。", "M103.Q12.p"),
                                "promptVi": "Hôm nay thời tiết rất đẹp.",
                                "options": [
                                    v("てんき", "M103.Q12.o0"),
                                    v("でんき", "M103.Q12.o1"),
                                    v("げんき", "M103.Q12.o2"),
                                    v("くうき", "M103.Q12.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 天気 (THIÊN KHÍ - Bài 4):</strong> Đọc là <strong>てんき</strong> (thời tiết)."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": v("きのう、白い 【雪】が ふりました。", "M103.Q13.p"),
                                "promptVi": "Hôm qua tuyết trắng đã rơi.",
                                "options": [
                                    v("ゆき", "M103.Q13.o0"),
                                    v("あめ", "M103.Q13.o1"),
                                    v("くも", "M103.Q13.o2"),
                                    v("かぜ", "M103.Q13.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 雪 (TUYẾT - Bài 4):</strong> Đọc là <strong>ゆき</strong> (tuyết). Phân biệt: 雨 (あめ - mưa), 雲 (くも - mây), 風 (かぜ - gió)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": v("その かどを 【右】に まがって ください。", "M103.Q14.p"),
                                "promptVi": "Hãy rẽ phải ở góc đường đó.",
                                "options": [
                                    v("みぎ", "M103.Q14.o0"),
                                    v("ひだり", "M103.Q14.o1"),
                                    v("まえ", "M103.Q14.o2"),
                                    v("うしろ", "M103.Q14.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 右 (HỮU - Bài 6):</strong> Đọc là <strong>みぎ</strong> (bên phải). Chữ 左 (TẢ - Bài 6) đọc là ひだり (bên trái)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": v("はくぶつかんは 【左】がわに あります。", "M103.Q15.p"),
                                "promptVi": "Bảo tàng nằm ở phía bên trái.",
                                "options": [
                                    v("ひだり", "M103.Q15.o0"),
                                    v("みぎ", "M103.Q15.o1"),
                                    v("きた", "M103.Q15.o2"),
                                    v("みなみ", "M103.Q15.o3")
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
                                "prompt": v("春には きれいな 【はな】が さきます。", "M103.Q16.p"),
                                "promptVi": "Vào mùa xuân có hoa đẹp nở rộ.",
                                "options": [
                                    v("花", "M103.Q16.o0"),
                                    v("海", "M103.Q16.o1"),
                                    v("山", "M103.Q16.o2"),
                                    v("川", "M103.Q16.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 花 (HOA - Bài 3):</strong> Đọc là <strong>はな</strong> (bông hoa). Phân biệt: 海 (うみ - biển), 山 (やま - núi), 川 (かわ - sông)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": v("きょうは 【あめ】が ふって います。", "M103.Q17.p"),
                                "promptVi": "Hôm nay trời đang mưa.",
                                "options": [
                                    v("雨", "M103.Q17.o0"),
                                    v("雪", "M103.Q17.o1"),
                                    v("雲", "M103.Q17.o2"),
                                    v("風", "M103.Q17.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 雨 (VŨ - Bài 4):</strong> Đọc là <strong>あめ</strong> (cơn mưa)."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": v("つよい 【かぜ】が ふいて います。", "M103.Q18.p"),
                                "promptVi": "Gió mạnh đang thổi.",
                                "options": [
                                    v("風", "M103.Q18.o0"),
                                    v("雨", "M103.Q18.o1"),
                                    v("空", "M103.Q18.o2"),
                                    v("気", "M103.Q18.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 風 (PHONG - Bài 4):</strong> Đọc là <strong>かぜ</strong> (ngọn gió)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": v("青い 【そら】が ひろがって います。", "M103.Q19.p"),
                                "promptVi": "Bầu trời xanh trải rộng bao la.",
                                "options": [
                                    v("空", "M103.Q19.o0"),
                                    v("晴", "M103.Q19.o1"),
                                    v("雲", "M103.Q19.o2"),
                                    v("海", "M103.Q19.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 空 (KHÔNG - Bài 4):</strong> Đọc là <strong>そら</strong> (bầu trời)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": v("この 【まち】には 外国人が 多いです。", "M103.Q20.p"),
                                "promptVi": "Ở thị trấn này có nhiều người nước ngoài.",
                                "options": [
                                    v("町", "M103.Q20.o0"),
                                    v("店", "M103.Q20.o1"),
                                    v("道", "M103.Q20.o2"),
                                    v("駅", "M103.Q20.o3")
                                ],
                                "correct": 0,
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
                                "prompt": v("一ばんめの かどを 右 (   ) まがって ください。", "M103.Q21.p"),
                                "promptVi": "Hãy rẽ phải ở góc đường thứ nhất. (Câu 6 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("に", "M103.Q21.o0"),
                                    v("を", "M103.Q21.o1"),
                                    v("で", "M103.Q21.o2"),
                                    v("へ", "M103.Q21.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc rẽ hướng: [Hướng] に まがる:</strong> Rẽ sang bên phải ➔ <strong>右に まがる</strong>. Lưu ý góc đường dùng trợ từ を (かどを)."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": v("ハノイの 秋は きれい (   )、しずかです。", "M103.Q22.p"),
                                "promptVi": "Mùa thu của Hà Nội thì đẹp và yên bình. (Câu 33 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("で", "M103.Q22.o0"),
                                    v("くて", "M103.Q22.o1"),
                                    v("くては", "M103.Q22.o2"),
                                    v("な", "M103.Q22.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc nối Tính từ đuôi な: Tính từ (bỏ な) + で:</strong> きれい (Tính từ đuôi な) ➔ <strong>きれいで</strong>, しずかです."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": v("十二月ごろ、さむく (   ) から、あまり 外へ 出ません。", "M103.Q23.p"),
                                "promptVi": "Khoảng tháng 12 trời trở lạnh nên tôi không hay ra ngoài lắm. (Câu 33 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("なります", "M103.Q23.o0"),
                                    v("します", "M103.Q23.o1"),
                                    v("あります", "M103.Q23.o2"),
                                    v("行きます", "M103.Q23.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc biến đổi trạng thái tự nhiên: Tính từ đuôi い (bỏ い) + く なります:</strong> さむい ➔ <strong>さむく なります</strong> (trở nên lạnh)."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": v("夜は、道も しずかに (   )。", "M103.Q24.p"),
                                "promptVi": "Buổi đêm, đường phố cũng trở nên yên tĩnh hơn. (Câu 33 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("なります", "M103.Q24.o0"),
                                    v("します", "M103.Q24.o1"),
                                    v("できます", "M103.Q24.o2"),
                                    v("きます", "M103.Q24.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc biến đổi tính từ đuôi な: Tính từ (bỏ な) + に なります:</strong> しずか ➔ <strong>しずかに なります</strong> (trở nên yên tĩnh)."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": v("あさひはくぶつかんへ 行きたいんですが、(   ) 行きますか。", "M103.Q25.p"),
                                "promptVi": "Tôi muốn đi đến viện bảo tàng Asahi, đi như thế nào? (Câu 6 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("どうやって", "M103.Q25.o0"),
                                    v("いくらで", "M103.Q25.o1"),
                                    v("だれと", "M103.Q25.o2"),
                                    v("なぜ", "M103.Q25.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ để hỏi cách thức/đường đi: どうやって:</strong> 'Đi như thế nào / bằng cách nào?' ➔ <strong>どうやって 行きますか</strong>."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": v("この ところには かわいい ふくやが (   ) あります。", "M103.Q26.p"),
                                "promptVi": "Ở khu vực này có nhiều cửa hàng thời trang dễ thương. (Câu 3 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("たくさん", "M103.Q26.o0"),
                                    v("すこし", "M103.Q26.o1"),
                                    v("あまり", "M103.Q26.o2"),
                                    v("ぜんぜん", "M103.Q26.o3")
                                ],
                                "correct": 0,
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
                                "prompt": v("あさひはくぶつかんは [  ] [  ] [ ★ ] [  ] あります。", "M103.Q27.p"),
                                "promptVi": "Bảo tàng Asahi ở bên tay trái. (Câu 6)",
                                "options": [
                                    v("道", "M103.Q27.o0"),
                                    v("の", "M103.Q27.o1"),
                                    v("左がわ", "M103.Q27.o2"),
                                    v("に", "M103.Q27.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> あさひはくぶつかんは [道] [の] [★ 左がわ] [に] あります。<br>Vị trí ngôi sao là <strong>左がわ</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "prompt": v("私の [  ] [  ] [ ★ ] [  ] たてものが あります。", "M103.Q28.p"),
                                "promptVi": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài. (Câu 9 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("いえの", "M103.Q28.o0"),
                                    v("となりに", "M103.Q28.o1"),
                                    v("青くて", "M103.Q28.o2"),
                                    v("ほそながい", "M103.Q28.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> 私の [いえの] (1) [となりに] (2) [★ 青くて] (3) [ほそながい] (4) たてものが あります。<br>Vị trí ngôi sao là <strong>青くて</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "prompt": v("ハノイは [  ] [  ] [ ★ ] [  ] なります。", "M103.Q29.p"),
                                "promptVi": "Hà Nội thì khoảng tháng 9 sẽ chuyển sang mùa thu. (Câu 33)",
                                "options": [
                                    v("九月ごろ", "M103.Q29.o0"),
                                    v("きれいな", "M103.Q29.o1"),
                                    v("秋", "M103.Q29.o2"),
                                    v("に", "M103.Q29.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> ハノイは [九月ごろ] [──] [★ 秋] [に] なります。<br>Trật tự: [九月ごろ] (1) [きれいな] (2) [★ 秋] (3) [に] (4) なります ➔ Vị trí số 3 là <strong>秋</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "prompt": v("あそこに [  ] [  ] [ ★ ] [  ] みえますか。", "M103.Q30.p"),
                                "promptVi": "Bạn có nhìn thấy cây cầu màu đỏ ở đằng kia không? (Câu 5)",
                                "options": [
                                    v("赤い", "M103.Q30.o0"),
                                    v("はし", "M103.Q30.o1"),
                                    v("が", "M103.Q30.o2"),
                                    v("よく", "M103.Q30.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> あそこに [赤い] [はし] [★ が] [よく] みえますか。<br>Vị trí số 3 là <strong>が</strong>."
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
                                "reference": v("あそこに 赤い はしが みえますか。", "M103.Q31.ref"),
                                "acceptAnswers": [
                                    v("あそこに 赤い はしが みえますか。", "M103.Q31.ans0"),
                                    v("あそこの 赤い はしが みえますか。", "M103.Q31.ans1"),
                                    v("あそこに 赤いはしが みえますか。", "M103.Q31.ans2")
                                ],
                                "hints": ["あそこに / あそこの", "赤い (あかい) はしが", "みえますか"]
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "prompt": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài.",
                                "promptVi": "Câu 9 trong bộ 40 câu ôn tập",
                                "reference": v("私の いえの となりに 青くて ほそながい たてものが あります。", "M103.Q32.ref"),
                                "acceptAnswers": [
                                    v("私の いえの となりに 青くて ほそながい たてものが あります。", "M103.Q32.ans0"),
                                    v("わたしの いえの となりに 青くて ほそながい たてものが あります。", "M103.Q32.ans1"),
                                    v("いえの となりに 青くて ほそながい たてものが あります。", "M103.Q32.ans2")
                                ],
                                "hints": ["私の いえの となりに", "青くて ほそながい", "たてものが あります"]
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
                "passage": v("ハノイは 九月ごろ 秋に なります。ハノイの 秋は きれいで、しずかです。\n私は よく ふるい まちへ しゃしんを とりに 行きます。\nでも、十二月ごろに なると、とても さむく なりますから、あまり 外へ 出ません。\n夜は、道も しずかに なります。\n日本は 十二月から 二月まで 冬です。雪が たくさん ふりますから、白い 山が とても きれいです。\nわたしは いつか 冬の 日本へ 行って、雪を みてみたいです。", "M103.passage"),
                "passageVi": "Hà Nội khoảng tháng 9 sang mùa thu. Mùa thu Hà Nội rất đẹp và yên bình.\nTôi thường đến khu phố cổ chụp ảnh.\nNhưng đến khoảng tháng 12, trời trở nên rất lạnh nên tôi không hay ra ngoài lắm.\nBuổi đêm, đường phố cũng trở nên vắng lặng hơn.\nỞ Nhật Bản, từ tháng 12 đến tháng 2 là mùa đông. Tuyết rơi rất nhiều nên những ngọn núi phủ tuyết trắng rất đẹp.\nMột ngày nào đó tôi muốn đến Nhật Bản vào mùa đông để ngắm tuyết.",
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": v("この 人は なぜ 十二月に あまり 外へ 出ませんか。", "M103.Q33.p"),
                        "promptVi": "Tại sao vào tháng 12 người này lại không hay ra ngoài?",
                        "options": [
                            v("とても さむく なりますから。", "M103.Q33.o0"),
                            v("雨が たくさん ふりますから。", "M103.Q33.o1"),
                            v("学校の テストが ありますから。", "M103.Q33.o2"),
                            v("まちが にぎやかですから。", "M103.Q33.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「とても さむく なりますから、あまり 外へ 出ません」 ➔ Vì trời trở nên rất lạnh."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": v("この 人は 日本の 冬の 何を みてみたいと いって いますか。", "M103.Q34.p"),
                        "promptVi": "Người này muốn ngắm điều gì ở mùa đông Nhật Bản?",
                        "options": [
                            v("雪", "M103.Q34.o0"),
                            v("花", "M103.Q34.o1"),
                            v("海", "M103.Q34.o2"),
                            v("川", "M103.Q34.o3")
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
                        "modelAnswer": v("私の いえの ちかくには、青くて ほそながい たてものが あります。そして、駅の 前に 白くて おおきい スーパーも あります。とても べんりで、きれいな まちです。", "M103.Q35.ans"),
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
                        "modelAnswer": v("ベトナムの ハノイは 九月ごろ 秋に なります。ハノイの 秋は 天気が よくて、とても すずしいです。まちの 道には きれいな 花が たくさん さきます。わたしは 秋が いちばん 好きですから、やすみの 日に 友達と まちへ 行って、しゃしんを たくさん とります。夜も しずかで、とても すみやすいです。", "M103.Q36.ans"),
                        "modelVi": "Hà Nội ở Việt Nam khoảng tháng 9 thì sang thu. Mùa thu Hà Nội thời tiết đẹp và rất mát mẻ. Trên các con đường trong phố có nhiều hoa đẹp nở rộ. Tôi thích mùa thu nhất, nên vào ngày nghỉ tôi thường cùng bạn bè lên phố chụp nhiều ảnh. Buổi đêm cũng yên tĩnh, rất dễ chịu.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; miêu tả rõ ràng thời tiết (天気がいい, すずしい), mùa (秋), hoạt động cá nhân và cảm nhận."
                    }
                ]
            }
        ]
    }

if __name__ == "__main__":
    exam = build_m103()
    print("M103 built successfully!")
    print("Code:", exam["code"])
    print("Sections:", len(exam["sections"]))
