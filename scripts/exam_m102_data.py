#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/exam_m102_data.py
Mã đề M102: Đề Chuyên Sâu Động Từ, Thể て & So Sánh (Bài 1 - 10)
Chuẩn Can-do giáo viên 10 năm kinh nghiệm - Tuyệt đối không dùng chữ Hán chưa học.
"""

import re
try:
    from scripts.exam_m101_data import PERMITTED_KANJI, v
except ImportError:
    from exam_m101_data import PERMITTED_KANJI, v

def build_m102():
    return {
        "code": "M102",
        "name": "Mã Đề M102 (Chuyên Sâu Động Từ & So Sánh)",
        "tag": "⚡ Thể て • Thể Từ Điển • So Sánh hơn/nhất • Chuẩn A2-1",
        "desc": "Đề chuyên sâu về Thể liên kết (～てから, ～てもいい, ～てください), Thể từ điển (～まえに, ～ことができる, ～こと), và So sánh (より, どちら, ほう, いちばん) bám sát 40 câu ôn tập.",
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
                                "prompt": v("わたしは つめたい (   ) を のみたいです。", "M102.Q1.p"),
                                "promptVi": "Tôi muốn uống cà phê lạnh. (Câu 22 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("コーヒー", "M102.Q1.o0"),
                                    v("シャツ", "M102.Q1.o1"),
                                    v("ぼうし", "M102.Q1.o2"),
                                    v("くつ", "M102.Q1.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng đồ uống:</strong> Đi với động từ 飲む (のみたい - muốn uống) và tính từ つめたい (lạnh) chỉ có thể là <strong>コーヒー</strong> (cà phê). Các từ còn lại là đồ trang phục: シャツ (áo sơ mi), ぼうし (mũ), くつ (giày)."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": v("白い (   ) が ほしいです。", "M102.Q2.p"),
                                "promptVi": "Tớ muốn có chiếc áo sơ mi trắng. (Câu 21 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("シャツ", "M102.Q2.o0"),
                                    v("おちゃ", "M102.Q2.o1"),
                                    v("みず", "M102.Q2.o2"),
                                    v("あめ", "M102.Q2.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng trang phục & màu sắc:</strong> 白い (trắng) bổ nghĩa cho danh từ chỉ quần áo: <strong>シャツ</strong> (áo sơ mi). Chữ Hán 白 (Bạch) đã học ở Bài 6."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": v("わたしの しゅみは まんがを (   ) ことです。", "M102.Q3.p"),
                                "promptVi": "Sở thích của tôi là đọc truyện tranh. (Câu 40 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("読む", "M102.Q3.o0"),
                                    v("食べる", "M102.Q3.o1"),
                                    v("のむ", "M102.Q3.o2"),
                                    v("行く", "M102.Q3.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc sở thích: N / V-る ＋ ことです:</strong> まんが (truyện tranh) đi với động từ <strong>読む</strong> (đọc - chữ Hán 読 học ở Bài 2). まんがを 読む こと: Việc đọc truyện tranh."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": v("フランス語は (   ) が かんたんでは ありません。", "M102.Q4.p"),
                                "promptVi": "Tiếng Pháp thì phát âm không đơn giản. (Câu 36 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("はつおん", "M102.Q4.o0"),
                                    v("ことば", "M102.Q4.o1"),
                                    v("ぶんぽう", "M102.Q4.o2"),
                                    v("かんじ", "M102.Q4.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng học ngoại ngữ (Bài 2):</strong> <strong>はつおん</strong> (phát âm). Câu 36 ôn tập: 'Tiếng Pháp thì phát âm không đơn giản' ➔ フランス語は はつおんが かんたんでは ありません。"
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": v("あした、いっしょに とうきょうタワーを (   )。夜の けしきが きれいですよ。", "M102.Q5.p"),
                                "promptVi": "Mai bạn ngắm tháp Tokyo với tôi không? Cảnh đêm đẹp lắm đó. (Câu 27 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("みませんか", "M102.Q5.o0") if False else v("みませんか", "M102.Q5.o0"),
                                    v("みました", "M102.Q5.o1"),
                                    v("みて", "M102.Q5.o2"),
                                    v("みないで", "M102.Q5.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc rủ rê lịch sự: ～ませんか:</strong> 'Cùng ngắm tháp Tokyo với tôi không?' ➔ <strong>みませんか</strong>. Chữ 夜 (Dạ - đêm) đã học ở Bài 8."
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
                                "prompt": v("<u>とうきょうは おきなわより 人が 多いです。</u>", "M102.Q6.p"),
                                "promptVi": "Tokyo thì đông người hơn Okinawa. (Câu 28 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("おきなわは とうきょうより 人が すくないです。", "M102.Q6.o0"),
                                    v("おきなわの ほうが 人が 多いです。", "M102.Q6.o1"),
                                    v("とうきょうも おきなわも 人が おなじです。", "M102.Q6.o2") if False else v("とうきょうも おきなわも 人が おなじです。", "M102.Q6.o2"),
                                    v("とうきょうは 人が あまり いません。", "M102.Q6.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Quan hệ so sánh đảo ngược:</strong> 'Tokyo đông người hơn Okinawa' đồng nghĩa với 'Okinawa ít người hơn Tokyo' (<strong>おきなわは とうきょうより 人が すくないです</strong>)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": v("<u>えいがを みる 前に、カフェへ 行って みずを かいたいです。</u>", "M102.Q7.p"),
                                "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê mua nước. (Câu 13 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("カフェで みずを かってから、えいがを みます。", "M102.Q7.o0"),
                                    v("えいがを みた 後で、カフェへ 行きます。", "M102.Q7.o1"),
                                    v("えいがの なかで カフェの みずを のみます。", "M102.Q7.o2"),
                                    v("みずが ないですから、えいがを みません。", "M102.Q7.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tương đương trình tự thời gian:</strong> 'Trước khi làm B thì làm A' (Bの 前に A) = 'Làm A xong rồi mới làm B' (<strong>Aてから B</strong>)."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": v("<u>ドラえもんの ほうが 好きです。ふしぎな ポケットが ありますから。</u>", "M102.Q8.p"),
                                "promptVi": "Mình thích Doraemon hơn. Vì Doraemon có chiếc túi thần kỳ. (Câu 30 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ふしぎな ポケットが あるので、ドラえもんが 好きです。", "M102.Q8.o0"),
                                    v("ポケモンも ドラえもんも おなじくらい 好きです。", "M102.Q8.o1"),
                                    v("ポケットが 好きではないので、ドラえもんを えらびません。", "M102.Q8.o2"),
                                    v("ドラえもんより ポケモンの ほうが 好きです。", "M102.Q8.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chuyển đổi liên từ chỉ nguyên nhân: ～から ➔ ～ので:</strong> 'Vì có túi thần kỳ nên thích Doraemon'."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": v("<u>ベトナム語は はなす ことが むずかしいです。</u>", "M102.Q9.p"),
                                "promptVi": "Tiếng Việt thì việc nói chuyện khó. (Câu 37 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ベトナム語で はなす のは たいへんです。", "M102.Q9.o0"),
                                    v("ベトナム語を はなす ことが とても とくいです。", "M102.Q9.o1"),
                                    v("ベトナム語の かんじを かく のが むずかしいです。", "M102.Q9.o2"),
                                    v("ベトナム語は だれでも かんたんに はなせます。", "M102.Q9.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ đồng nghĩa: むずかしい = たいへん (khó khăn, vất vả):</strong> Việc nói tiếng Việt khó ➔ Nói tiếng Việt thì vất vả/khó khăn."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": v("<u>あの 店は えきの ちかくに あります。</u>", "M102.Q10.p"),
                                "promptVi": "Cửa hàng đó ở gần nhà ga. (Câu 4 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("あの 店は 駅の すぐ そばに あります。", "M102.Q10.o0"),
                                    v("あの 店は 駅から とても とおいです。", "M102.Q10.o1"),
                                    v("あの 店は 駅の なかに あります。", "M102.Q10.o2"),
                                    v("あの 店の 前には 駅が ありません。", "M102.Q10.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ đồng nghĩa chỉ khoảng cách: ちかく = すぐ そば (ngay bên cạnh, rất gần):</strong> Cửa hàng ở gần ga ➔ Ở ngay bên cạnh ga. Chữ 駅 (Dịch - ga) và 店 (Điếm - tiệm) đều thuộc 86 chữ Hán đã học."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Kiểm tra năng lực nhận diện âm đọc và chữ viết Hán tự đã học (Bài 1 - 10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn âm đọc chính xác của chữ Hán trong câu:",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": v("まい朝、七時に えきを 【出】ます。", "M102.Q11.p"),
                                "promptVi": "Mỗi sáng, tôi ra khỏi ga lúc 7 giờ.",
                                "options": [
                                    v("で", "M102.Q11.o0"),
                                    v("ま", "M102.Q11.o1"),
                                    v("と", "M102.Q11.o2"),
                                    v("い", "M102.Q11.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 出 (XUẤT - Bài 7):</strong> Âm Kun là <strong>で (る)</strong>. 出ます đọc là <strong>でます</strong> (đi ra, rời khỏi)."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": v("駅で 友だちを 【待】ちます。", "M102.Q12.p"),
                                "promptVi": "Tôi đợi bạn ở nhà ga.",
                                "options": [
                                    v("ま", "M102.Q12.o0"),
                                    v("も", "M102.Q12.o1"),
                                    v("と", "M102.Q12.o2"),
                                    v("た", "M102.Q12.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 待 (ĐÃI - Bài 7):</strong> Âm Kun là <strong>ま (つ)</strong>. 待ちます đọc là <strong>まちます</strong> (chờ, đợi)."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": v("バスが 【止】まりました。", "M102.Q13.p"),
                                "promptVi": "Xe buýt đã dừng lại.",
                                "options": [
                                    v("と", "M102.Q13.o0"),
                                    v("とま", "M102.Q13.o1"),
                                    v("の", "M102.Q13.o2"),
                                    v("で", "M102.Q13.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 止 (CHỈ - Bài 7):</strong> Âm Kun là <strong>と (まる)</strong>. 止まりました đọc là <strong>とまりました</strong> (đã dừng)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": v("この 【道】を まっすぐ 行って ください。", "M102.Q14.p"),
                                "promptVi": "Xin hãy đi thẳng con đường này. (Câu 6 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("みち", "M102.Q14.o0"),
                                    v("まち", "M102.Q14.o1"),
                                    v("かわ", "M102.Q14.o2"),
                                    v("やま", "M102.Q14.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 道 (ĐẠO - Bài 6):</strong> Âm Kun là <strong>みち</strong> (con đường). Tránh nhầm với 町 (まち - thị trấn), 川 (かわ - con sông), 山 (やま - ngọn núi)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": v("スーパーは 【駅】の ちかくに あります。", "M102.Q15.p") if False else v("スーパーは 【駅】の ちかくに あります。", "M102.Q15.p"),
                                "promptVi": "Siêu thị ở gần nhà ga. (Câu 4 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("えき", "M102.Q15.o0"),
                                    v("みち", "M102.Q15.o1"),
                                    v("まち", "M102.Q15.o2"),
                                    v("みせ", "M102.Q15.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 駅 (DỊCH - Bài 7):</strong> Đọc là <strong>えき</strong> (nhà ga)."
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
                                "prompt": v("あしたの 【あさ】 九時に あいましょう。", "M102.Q16.p"),
                                "promptVi": "9h sáng mai chúng ta gặp nhau nhé. (Câu 7 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("朝", "M102.Q16.o0"),
                                    v("昼", "M102.Q16.o1"),
                                    v("夜", "M102.Q16.o2"),
                                    v("今", "M102.Q16.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 朝 (TRIÊU - Bài 8):</strong> Đọc là <strong>あさ</strong> (buổi sáng). Các chữ phân biệt: 昼 (ひる - trưa), 夜 (よる - đêm), 今 (いま - bây giờ)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": v("ごはんの 【まえ】に、てを あらいます。", "M102.Q17.p") if False else v("ごはんの 【まえ】に、てを あらいます。", "M102.Q17.p"),
                                "promptVi": "Trước bữa ăn, tôi rửa tay.",
                                "options": [
                                    v("前", "M102.Q17.o0"),
                                    v("後", "M102.Q17.o1"),
                                    v("右", "M102.Q17.o2"),
                                    v("左", "M102.Q17.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 前 (TIỀN - Bài 8):</strong> Đọc là <strong>まえ</strong> (phía trước, trước khi). Chữ 後 (HẬU - Bài 8) đọc là あと/うしろ."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": v("ごはんを たべた 【あと】で、おちゃを のみます。", "M102.Q18.p") if False else v("ごはんを たべた 【あと】で、おちゃを のみます。", "M102.Q18.p"),
                                "promptVi": "Sau khi ăn cơm xong, tôi uống trà.",
                                "options": [
                                    v("後", "M102.Q18.o0"),
                                    v("前", "M102.Q18.o1"),
                                    v("待", "M102.Q18.o2"),
                                    v("止", "M102.Q18.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 後 (HẬU - Bài 8):</strong> Đọc là <strong>あと</strong> trong mẫu câu V-た後で (sau khi làm gì)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": v("あそこで バスに 【の】ります。", "M102.Q19.p"),
                                "promptVi": "Tôi lên xe buýt ở đằng kia.",
                                "options": [
                                    v("乗", "M102.Q19.o0"),
                                    v("出", "M102.Q19.o1"),
                                    v("待", "M102.Q19.o2"),
                                    v("行", "M102.Q19.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 乗 (THỪA - Bài 8):</strong> Âm Kun là <strong>の (る)</strong> (lên xe, đi tàu xe: 乗ります - のります)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": v("にちようびに 【ともだち】と あそびます。", "M102.Q20.p"),
                                "promptVi": "Chủ nhật tôi đi chơi cùng bạn bè.",
                                "options": [
                                    v("友達", "M102.Q20.o0"),
                                    v("先生", "M102.Q20.o1"),
                                    v("学校", "M102.Q20.o2"),
                                    v("留学生", "M102.Q20.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 友達 (HỮU ĐẠT - Bài 10):</strong> Đọc là <strong>ともだち</strong> (bạn bè). Cả 2 chữ 友 và 達 đều được học ở Bài 10."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Kiểm tra thể liên kết, thể từ điển, cấu trúc xin phép, so sánh và sắp xếp câu sao (★).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn phương án đúng nhất điền vào chỗ trống",
                        "groupInstruction": "Chọn từ/thể ngữ pháp chính xác nhất điền vào chỗ trống trong ngoặc (   ):",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": v("すみません、その じしょを かり (   ) も いいですか。", "M102.Q21.p"),
                                "promptVi": "Xin lỗi, có thể cho tôi mượn quyển từ điển đó được không? (Câu 14 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ても", "M102.Q21.o0"),
                                    v("たら", "M102.Q21.o1"),
                                    v("ては", "M102.Q21.o2"),
                                    v("のに", "M102.Q21.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc xin phép lịch sự: V-てもいいですか:</strong> かりる (Nhóm 2) ➔ かりて ＋ もいいですか (Tôi mượn có được không?)."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": v("ええ、どうぞ (   ) ください。", "M102.Q22.p"),
                                "promptVi": "Được chứ, bạn hãy dùng đi. (Câu 14 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("つかって", "M102.Q22.o0"),
                                    v("つかい", "M102.Q22.o1"),
                                    v("つかう", "M102.Q22.o2"),
                                    v("つかった", "M102.Q22.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc yêu cầu / khuyến khích nhẹ nhàng: V-てください:</strong> つかう ➔ thể て là <strong>つかって</strong>."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": v("ベトナムへ 行った ことが (   )。", "M102.Q23.p"),
                                "promptVi": "Anh đã từng đến Việt Nam chưa? - Chưa, tôi chưa từng. (Câu 26 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ありますか", "M102.Q23.o0"),
                                    v("いますか", "M102.Q23.o1"),
                                    v("しますか", "M102.Q23.o2"),
                                    v("いきますか", "M102.Q23.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc kinh nghiệm: V-た ことが あります (đã từng làm gì):</strong> Hỏi kinh nghiệm ➔ 行った ことが <strong>ありますか</strong>."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": v("ポケモンと ドラえもんと、(   ) が 好きですか。", "M102.Q24.p"),
                                "promptVi": "Giữa Pokemon và Doraemon, bạn thích cái nào hơn? (Câu 30 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("どちら", "M102.Q24.o0"),
                                    v("どこ", "M102.Q24.o1"),
                                    v("だれ", "M102.Q24.o2"),
                                    v("いくら", "M102.Q24.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc so sánh chọn 1 trong 2: Aと Bと どちらが ～:</strong> Khi so sánh giữa 2 đối tượng, bắt buộc dùng từ để hỏi <strong>どちら</strong> (bên nào, cái nào)."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": v("日本で どこが (   ) さむいですか。", "M102.Q25.p"),
                                "promptVi": "Ở Nhật Bản, ở đâu là lạnh nhất? (Câu 29 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("いちばん", "M102.Q25.o0"),
                                    v("もっと", "M102.Q25.o1"),
                                    v("あまり", "M102.Q25.o2"),
                                    v("ぜんぜん", "M102.Q25.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc so sánh nhất trong phạm vi: [Phạm vi] で [Từ để hỏi] が いちばん ～:</strong> Ở Nhật thì ở đâu lạnh nhất ➔ dùng <strong>いちばん</strong>."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": v("たいふう (   )、でんしゃと バスが 止まりました。", "M102.Q26.p"),
                                "promptVi": "Vì bão, nên tàu điện và xe buýt dừng chạy. (Câu 35 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("で", "M102.Q26.o0"),
                                    v("に", "M102.Q26.o1"),
                                    v("を", "M102.Q26.o2"),
                                    v("へ", "M102.Q26.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Trợ từ で chỉ nguyên nhân do thiên tai, biến cố: N(thiên tai) + で:</strong> たいふうで (Do bão) nên tàu xe dừng lại."
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
                                "prompt": v("えいがを [  ] [  ] [ ★ ] [  ] みずを かいたいです。", "M102.Q27.p"),
                                "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê mua nước. (Câu 13)",
                                "options": [
                                    v("前に、", "M102.Q27.o0"),
                                    v("行って", "M102.Q27.o1"),
                                    v("みる", "M102.Q27.o2"),
                                    v("カフェへ", "M102.Q27.o3")
                                ],
                                "correct": 3,
                                "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] みる ➔ [1] 前に、 ➔ <strong>★ [4] カフェへ (Vị trí số 3)</strong> ➔ [2] 行って<br>➔ Câu hoàn chỉnh: えいがを みる 前に、カフェへ 行って みずを かいたいです。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[4] カフェへ</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "prompt": v("ポケモンと [  ] [  ] [ ★ ] [  ] 好きですか。", "M102.Q28.p"),
                                "promptVi": "Giữa Pokemon và Doraemon, bạn thích cái nào hơn? (Câu 30)",
                                "options": [
                                    v("が", "M102.Q28.o0"),
                                    v("ドラえもんと、", "M102.Q28.o1"),
                                    v("いちばん", "M102.Q28.o2"),
                                    v("どちら", "M102.Q28.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[2] ドラえもんと、 ➔ [4] どちら ➔ <strong>★ [1] が (Vị trí số 3)</strong> ➔ [3] いちばん<br>➔ Câu hoàn chỉnh: ポケモンと ドラえもんと、どちらが いちばん 好きですか。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[1] が</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "prompt": v("とうきょうは [  ] [  ] [ ★ ] [  ] 多いです。", "M102.Q29.p"),
                                "promptVi": "Tokyo thì đông người hơn Okinawa. (Câu 28)",
                                "options": [
                                    v("より", "M102.Q29.o0"),
                                    v("とても", "M102.Q29.o1"),
                                    v("人が", "M102.Q29.o2"),
                                    v("おきなわ", "M102.Q29.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[4] おきなわ ➔ [1] より ➔ <strong>★ [3] 人が (Vị trí số 3)</strong> ➔ [2] とても<br>➔ Câu hoàn chỉnh: とうきょうは おきなわより 人が とても 多いです。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[3] 人が</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "prompt": v("私の しゅみは [  ] [  ] [ ★ ] [  ] ことです。", "M102.Q30.p"),
                                "promptVi": "Sở thích của tôi là đọc truyện tranh. (Câu 40)",
                                "options": [
                                    v("まんがを", "M102.Q30.o0"),
                                    v("たくさん", "M102.Q30.o1"),
                                    v("読む", "M102.Q30.o2"),
                                    v("日本の", "M102.Q30.o3")
                                ],
                                "correct": 1,
                                "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[4] 日本の ➔ [1] まんがを ➔ <strong>★ [2] たくさん (Vị trí số 3)</strong> ➔ [3] 読む<br>➔ Câu hoàn chỉnh: 私の しゅみは 日本の まんがを たくさん 読む ことです。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[2] たくさん</strong>."
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
                                "prompt": "Tiếng Việt thì việc nói chuyện khó.",
                                "promptVi": "Câu 37 trong bộ 40 câu ôn tập",
                                "reference": v("ベトナム語は はなす ことが むずかしいです。", "M102.Q31.ref"),
                                "acceptAnswers": [
                                    v("ベトナム語は はなす ことが むずかしいです。", "M102.Q31.ans0"),
                                    v("ベトナム語は はなす のが むずかしいです。", "M102.Q31.ans1"),
                                    v("ベトナム語は はなす ことが たいへんです。", "M102.Q31.ans2")
                                ],
                                "hints": ["ベトナム語は", "はなす ことが / のが", "むずかしいです"]
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "prompt": "Tôi muốn có chiếc áo sơ mi trắng.",
                                "promptVi": "Câu 21 trong bộ 40 câu ôn tập",
                                "reference": v("白い シャツが ほしいです。", "M102.Q32.ref"),
                                "acceptAnswers": [
                                    v("白い シャツが ほしいです。", "M102.Q32.ans0"),
                                    v("わたしは 白い シャツが ほしいです。", "M102.Q32.ans1"),
                                    v("白いシャツが ほしいです。", "M102.Q32.ans2")
                                ],
                                "hints": ["白い (しろい)", "シャツが", "ほしいです"]
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc bài viết chia sẻ về sở thích, việc học và chọn đáp án chính xác nhất (Câu 33-34).",
                "badge": "10 Điểm",
                "passage": v("わたしは いま、学校で 日本語を 勉強して います。\n日本語は かんじを かく ことが とても おもしろいです。でも、ことばが 多くて、ぶんしょうを 読む のが 少し むずかしいです。\nわたしの しゅみは まんがを 読む ことです。日本の まんがが 好きですから、いえに たくさん あります。\nえいがを みる 前に、カフェへ 行って つめたい コーヒーを のむ のも 好きです。\nらいねん、日本へ 友達と 旅行に 行ってみたいです。", "M102.passage"),
                "passageVi": "Bây giờ tôi đang học tiếng Nhật ở trường học.\nTiếng Nhật thì việc viết chữ Hán rất thú vị. Nhưng từ vựng nhiều và việc đọc câu văn hơi khó một chút.\nSở thích của tôi là đọc truyện tranh. Vì tôi thích truyện tranh Nhật Bản nên ở nhà có rất nhiều.\nTrước khi xem phim, tôi cũng thích ghé quán cà phê để uống cà phê lạnh.\nNăm sau, tôi rất muốn đi du lịch Nhật Bản cùng bạn bè.",
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": v("この 人は 日本語の 何が おもしろいですか。", "M102.Q33.p"),
                        "promptVi": "Người này thấy điều gì ở tiếng Nhật thú vị?",
                        "options": [
                            v("かんじを かく こと", "M102.Q33.o0"),
                            v("ぶんしょうを 読む こと", "M102.Q33.o1"),
                            v("ことばを おぼえる こと", "M102.Q33.o2"),
                            v("テストを うける こと", "M102.Q33.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「日本語は かんじを かく ことが とても おもしろいです」 ➔ Việc viết chữ Hán rất thú vị."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": v("この 人は えいがを みる 前に 何を しますか。", "M102.Q34.p"),
                        "promptVi": "Người này làm gì trước khi xem phim?",
                        "options": [
                            v("カフェで つめたい コーヒーを のみます。", "M102.Q34.o0"),
                            v("まんがを 読みます。", "M102.Q34.o1"),
                            v("日本へ 旅行に 行きます。", "M102.Q34.o2"),
                            v("学校で 勉強します。", "M102.Q34.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「えいがを みる 前に、カフェへ 行って つめたい コーヒーを のむ のも 好きです」 ➔ Đi quán cà phê uống cà phê lạnh."
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
                        "prompt": "あなたの しゅみは 何ですか。（すきな こと、よく することなどを かいて ください）",
                        "promptVi": "Sở thích của bạn là gì? Hãy chia sẻ về điều bạn thích làm khi rảnh rỗi.",
                        "minWords": 30,
                        "placeholder": "Gõ câu trả lời tiếng Nhật tại đây... Ví dụ: わたしの しゅみは まんがを 読む ことです...",
                        "hints": [
                            "Cấu trúc sở thích: わたしの しゅみは ～ ことです (まんがを 読む / おんがくを きく)",
                            "Nêu tần suất / nơi làm: やすみの 日に うちで / 週に 三回...",
                            "Cảm xúc: とても おもしろい / たのしいです"
                        ],
                        "modelAnswer": v("わたしの しゅみは まんがを 読む ことです。日本の まんがが 好きですから、いえに たくさん あります。やすみの 日に、へやで 音楽を ききながら 読みます。とても たのしい 時間です。", "M102.Q35.ans"),
                        "modelVi": "Sở thích của tôi là đọc truyện tranh. Vì tôi thích truyện tranh Nhật Bản nên ở nhà có rất nhiều. Vào ngày nghỉ, tôi vừa nghe nhạc trong phòng vừa đọc. Đó là khoảng thời gian rất vui vẻ.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Sử dụng đúng cấu trúc sở thích (～ことです), nêu rõ cảm xúc và bối cảnh thực hiện."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "一ねんの なかで どの きせつが いちばん 好きですか。その りゆうも おしえて ください。（五十じ いじょう）",
                        "promptVi": "Trong 4 mùa của năm, bạn thích nhất mùa nào? Hãy giải thích rõ lý do tại sao (Viết đoạn văn tối thiểu 50 chữ/ký tự).",
                        "minWords": 50,
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは 夏が いちばん 好きです...",
                        "hints": [
                            "Mùa yêu thích nhất: わたしは [春 / 夏 / 秋 / 冬] が いちばん 好きです",
                            "Lý do thời tiết: 天気が いいですから / さむくないですから",
                            "Hoạt động / Đồ ăn: アイスクリームを たべる / 花を みる / 旅行に 行く",
                            "Độ dài: Tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": v("わたしは 夏が いちばん 好きです。夏は 天気が よくて、海へ 行く ことが できますから。そして、つめたい アイスクリームを たべる のが 好きです。冬は とても さむくて、外へ 出る のが にがてですから、あたたかい 夏の ほうが 好きです。", "M102.Q36.ans"),
                        "modelVi": "Tôi thích mùa hè nhất. Vì mùa hè thời tiết đẹp và tôi có thể đi biển. Và tôi thích ăn kem lạnh. Mùa đông thì rất lạnh, tôi rất ngại đi ra ngoài nên tôi thích mùa hè ấm áp hơn.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; nêu rõ mùa ưa thích bằng cấu trúc so sánh nhất (いちばん好き), sử dụng cấu trúc chỉ lý do (～から) và so sánh hơn (～のほうが好き)."
                    }
                ]
            }
        ]
    }

if __name__ == "__main__":
    exam = build_m102()
    print("M102 built successfully!")
    print("Code:", exam["code"])
    print("Sections:", len(exam["sections"]))
