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

DATA_M102 = {
    "code": "M102",
    "name": "Mã Đề M102 (Chuyên Sâu Động Từ & So Sánh)",
    "tag": "⚡ Thể て • Thể Từ Điển • So Sánh hơn/nhất • Chuẩn A2-1",
    "desc": "Đề chuyên sâu về Thể liên kết (～てから, ～てもいい, ～てください), Thể từ điển (～まえに, ～ことができる, ～こと), và So sánh (より, どちら, ほう, いちばん) bám sát 40 câu ôn tập.",
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
                            "prompt": "わたしは つめたい (   ) を のみたいです。",
                            "promptVi": "Tôi muốn uống cà phê lạnh. (Câu 22 trong bộ 40 câu ôn tập)",
                            "options": [
                                "コーヒー",
                                "シャツ",
                                "ぼうし",
                                "くつ"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Từ vựng đồ uống:</strong> Đi với động từ 飲む (のみたい - muốn uống) và tính từ つめたい (lạnh) chỉ có thể là <strong>コーヒー</strong> (cà phê). Các từ còn lại là đồ trang phục: シャツ (áo sơ mi), ぼうし (mũ), くつ (giày)."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "白い (   ) が ほしいです。",
                            "promptVi": "Tớ muốn có chiếc áo sơ mi trắng. (Câu 21 trong bộ 40 câu ôn tập)",
                            "options": [
                                "おちゃ",
                                "みず",
                                "あめ",
                                "シャツ"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng trang phục & màu sắc:</strong> 白い (trắng) bổ nghĩa cho danh từ chỉ quần áo: <strong>シャツ</strong> (áo sơ mi). Chữ Hán 白 (Bạch) đã học ở Bài 6."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "わたしの しゅみは まんがを (   ) ことです。",
                            "promptVi": "Sở thích của tôi là đọc truyện tranh. (Câu 40 trong bộ 40 câu ôn tập)",
                            "options": [
                                "読む",
                                "食べる",
                                "のむ",
                                "行く"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cấu trúc sở thích: N / V-る ＋ ことです:</strong> まんが (truyện tranh) đi với động từ <strong>読む</strong> (đọc - chữ Hán 読 học ở Bài 2). まんがを 読む こと: Việc đọc truyện tranh."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "フランス語は (   ) が かんたんでは ありません。",
                            "promptVi": "Tiếng Pháp thì phát âm không đơn giản. (Câu 36 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ことば",
                                "ぶんぽう",
                                "かんじ",
                                "はつおん"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng học ngoại ngữ (Bài 2):</strong> <strong>はつおん</strong> (phát âm). Câu 36 ôn tập: 'Tiếng Pháp thì phát âm không đơn giản' ➔ フランス語は はつおんが かんたんでは ありません。"
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "あした、いっしょに とうきょうタワーを (   )。夜の けしきが きれいですよ。",
                            "promptVi": "Mai bạn ngắm tháp Tokyo với tôi không? Cảnh đêm đẹp lắm đó. (Câu 27 trong bộ 40 câu ôn tập)",
                            "options": [
                                "みました",
                                "みて",
                                "みないで",
                                "みませんか"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Cấu trúc rủ rê lịch sự: ～ませんか:</strong> 'Cùng ngắm tháp Tokyo với tôi không?' ➔ <strong>みませんか</strong>. Chữ 夜 (Dạ - đêm) đã học ở Bài 8."
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
                            "prompt": "とうきょうは おきなわより 人が <u>多い</u>です。",
                            "promptVi": "Tokyo thì đông người hơn Okinawa. (Câu 28 trong bộ 40 câu ôn tập)",
                            "options": [
                                "たくさん います",
                                "すくないです",
                                "ぜんぜん いません",
                                "ちいさいです"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Quan hệ so sánh (Bài 4):</strong> 人が 多い (nhiều người, đông đúc) ＝ <strong>たくさん います</strong> (có nhiều người). Chữ 多 (Đa) và 人 (Nhân) đều đã học."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "えいがを みる 前に、カフェへ 行って のみものを <u>かいたいです</u>。",
                            "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê mua đồ uống. (Câu 13 trong bộ 40 câu ôn tập)",
                            "options": [
                                "かう つもりです",
                                "のむ つもりです",
                                "みる つもりです",
                                "いく つもりです"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cách diễn đạt ý định (Bài 7-8):</strong> ～たい (muốn làm) ＝ <strong>～つもり</strong> (dự định, có ý định làm). かいたいです ＝ かう つもりです (muốn mua đồ uống)."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "ドラえもんの ほうが 好きです。<u>ふしぎな</u> ポケットが ありますから。",
                            "promptVi": "Mình thích Doraemon hơn. Vì Doraemon có chiếc túi thần kỳ. (Câu 30 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ふつうの",
                                "すごい",
                                "ちいさな",
                                "ふるい"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Tính từ cảm thán (Bài 10):</strong> ふしぎな (kỳ diệu, thần kỳ) ＝ <strong>すごい</strong> (tuyệt vời, phi thường)."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "ベトナム語は はなす ことが <u>むずかしい</u>です。",
                            "promptVi": "Tiếng Việt thì việc nói chuyện khó khăn. (Câu 37 trong bộ 40 câu ôn tập)",
                            "options": [
                                "とくいです",
                                "かんたんです",
                                "おもしろいです",
                                "たいへんです"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Tính từ chỉ độ khó (Bài 2):</strong> むずかしい (khó khăn) ＝ <strong>たいへんです</strong> (vất vả, khó). Ngược nghĩa là かんたんです."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "あの 店は 駅の <u>ちかく</u>に あります。",
                            "promptVi": "Cửa hàng đó ở gần nhà ga. (Câu 4 trong bộ 40 câu ôn tập)",
                            "options": [
                                "とおく",
                                "なか",
                                "すぐ そば",
                                "うしろ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Từ vựng vị trí (Bài 5):</strong> ちかく (gần) ＝ <strong>すぐ そば</strong> (ngay sát cạnh bên). Chữ 駅 và 店 đều đã học."
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
                            "prompt": "まい朝、七時に えきを 【出】ます。",
                            "promptVi": "Mỗi sáng, tôi ra khỏi ga lúc 7 giờ.",
                            "options": [
                                "で",
                                "ま",
                                "と",
                                "い"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ 出 (XUẤT - Bài 7):</strong> Âm Kun là <strong>で (る)</strong>. 出ます đọc là <strong>でます</strong> (đi ra, rời khỏi)."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "駅で 友だちを 【待】ちます。",
                            "promptVi": "Tôi đợi bạn ở nhà ga.",
                            "options": [
                                "も",
                                "ま",
                                "と",
                                "た"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 待 (ĐÃI - Bài 7):</strong> Âm Kun là <strong>ま (つ)</strong>. 待ちます đọc là <strong>まちます</strong> (chờ, đợi)."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "バスが 【止】まりました。",
                            "promptVi": "Xe buýt đã dừng lại.",
                            "options": [
                                "とま",
                                "と",
                                "の",
                                "で"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 止 (CHỈ - Bài 7):</strong> Âm Kun là <strong>と (まる)</strong>. 止まりました đọc là <strong>とまりました</strong> (đã dừng)."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "この 【道】を まっすぐ 行って ください。",
                            "promptVi": "Xin hãy đi thẳng con đường này. (Câu 6 trong bộ 40 câu ôn tập)",
                            "options": [
                                "まち",
                                "かわ",
                                "やま",
                                "みち"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ 道 (ĐẠO - Bài 6):</strong> Âm Kun là <strong>みち</strong> (con đường). Tránh nhầm với 町 (まち - thị trấn), 川 (かわ - con sông), 山 (やま - ngọn núi)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "スーパーは 【駅】の ちかくに あります。",
                            "promptVi": "Siêu thị ở gần nhà ga. (Câu 4 trong bộ 40 câu ôn tập)",
                            "options": [
                                "みち",
                                "まち",
                                "えき",
                                "みせ"
                            ],
                            "correct": 2,
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
                            "prompt": "あしたの 【あさ】 九時に あいましょう。",
                            "promptVi": "9h sáng mai chúng ta gặp nhau nhé. (Câu 7 trong bộ 40 câu ôn tập)",
                            "options": [
                                "昼",
                                "朝",
                                "夜",
                                "今"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 朝 (TRIÊU - Bài 8):</strong> Đọc là <strong>あさ</strong> (buổi sáng). Các chữ phân biệt: 昼 (ひる - trưa), 夜 (よる - đêm), 今 (いま - bây giờ)."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "ごはんの 【まえ】に、てを あらいます。",
                            "promptVi": "Trước bữa ăn, tôi rửa tay.",
                            "options": [
                                "後",
                                "前",
                                "右",
                                "左"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 前 (TIỀN - Bài 8):</strong> Đọc là <strong>まえ</strong> (phía trước, trước khi). Chữ 後 (HẬU - Bài 8) đọc là あと/うしろ."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "じゅぎょうの 【あと】で、としょかんへ 行きます。",
                            "promptVi": "Sau giờ học, tôi đi đến thư viện.",
                            "options": [
                                "前",
                                "待",
                                "後",
                                "止"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ Hán: 後 (Hậu):</strong> Trong từ 【あと】 (sau). 【じゅぎょうの 後で】: Sau giờ học. Chữ 行 đã học ở Bài 5."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "あそこで バスに 【の】ります。",
                            "promptVi": "Tôi lên xe buýt ở đằng kia.",
                            "options": [
                                "出",
                                "待",
                                "乗",
                                "行"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 乗 (THỪA - Bài 8):</strong> Âm Kun là <strong>の (る)</strong> (lên xe, đi tàu xe: 乗ります - のります)."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "にちようびに 【ともだち】と あそびます。",
                            "promptVi": "Chủ nhật tôi đi chơi cùng bạn bè.",
                            "options": [
                                "友達",
                                "先生",
                                "学校",
                                "留学生"
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
                            "prompt": "すみません、その じしょを かり (   ) も いいですか。",
                            "promptVi": "Xin lỗi, có thể cho tôi mượn quyển từ điển đó được không? (Câu 14 trong bộ 40 câu ôn tập)",
                            "options": [
                                "たら",
                                "ては",
                                "ても",
                                "のに"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Cấu trúc xin phép lịch sự: V-てもいいですか:</strong> かりる (Nhóm 2) ➔ かりて ＋ もいいですか (Tôi mượn có được không?)."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "ええ、どうぞ (   ) ください。",
                            "promptVi": "Được chứ, bạn hãy dùng đi. (Câu 14 trong bộ 40 câu ôn tập)",
                            "options": [
                                "つかい",
                                "つかって",
                                "つかう",
                                "つかいます"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Cấu trúc yêu cầu / khuyến khích nhẹ nhàng: V-てください:</strong> つかう ➔ thể て là <strong>つかって</strong>."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "えいがを (   ) 前に、カフェへ 行って おちゃを のみたいです。",
                            "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê uống trà. (Câu 13 trong bộ 40 câu ôn tập)",
                            "options": [
                                "みます",
                                "みて",
                                "みない",
                                "みる"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Cấu trúc trình tự thời gian (Bài 8): Động từ thể từ điển (V-る) ＋ 前に:</strong> Trước khi xem phim ➔ <strong>みる 前に</strong>. Đúng theo Câu 13 trong bộ 40 câu ôn tập."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "ポケモンと ドラえもんと、(   ) が 好きですか。",
                            "promptVi": "Giữa Pokemon và Doraemon, bạn thích cái nào hơn? (Câu 30 trong bộ 40 câu ôn tập)",
                            "options": [
                                "どこ",
                                "だれ",
                                "どちら",
                                "いくら"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Cấu trúc so sánh chọn 1 trong 2: Aと Bと どちらが ～:</strong> Khi so sánh giữa 2 đối tượng, bắt buộc dùng từ để hỏi <strong>どちら</strong> (bên nào, cái nào)."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "日本で どこが (   ) さむいですか。",
                            "promptVi": "Ở Nhật Bản, ở đâu là lạnh nhất? (Câu 29 trong bộ 40 câu ôn tập)",
                            "options": [
                                "もっと",
                                "あまり",
                                "ぜんぜん",
                                "いちばん"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Cấu trúc so sánh nhất trong phạm vi: [Phạm vi] で [Từ để hỏi] が いちばん ～:</strong> Ở Nhật thì ở đâu lạnh nhất ➔ dùng <strong>いちばん</strong>."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "たいふう (   )、でんしゃと バスが 止まりました。",
                            "promptVi": "Vì bão, nên tàu điện và xe buýt dừng chạy. (Câu 35 trong bộ 40 câu ôn tập)",
                            "options": [
                                "に",
                                "を",
                                "で",
                                "へ"
                            ],
                            "correct": 2,
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
                            "prompt": "えいがを [  ] [  ] [ ★ ] [  ] みずを かいたいです。",
                            "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê mua nước. (Câu 13)",
                            "options": [
                                "前に、",
                                "行って",
                                "みる",
                                "カフェへ"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] みる ➔ [1] 前に、 ➔ <strong>★ [4] カフェへ (Vị trí số 3)</strong> ➔ [2] 行って<br>➔ Câu hoàn chỉnh: えいがを みる 前に、カフェへ 行って みずを かいたいです。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[4] カフェへ</strong>."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "prompt": "ポケモンと [  ] [  ] [ ★ ] [  ] 好きですか。",
                            "promptVi": "Giữa Pokemon và Doraemon, bạn thích cái nào hơn? (Câu 30)",
                            "options": [
                                "が",
                                "ドラえもんと、",
                                "いちばん",
                                "どちら"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[2] ドラえもんと、 ➔ [4] どちら ➔ <strong>★ [1] が (Vị trí số 3)</strong> ➔ [3] いちばん<br>➔ Câu hoàn chỉnh: ポケモンと ドラえもんと、どちらが いちばん 好きですか。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[1] が</strong>."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "prompt": "とうきょうは [  ] [  ] [ ★ ] [  ] 多いです。",
                            "promptVi": "Tokyo thì đông người hơn Okinawa. (Câu 28)",
                            "options": [
                                "より",
                                "とても",
                                "人が",
                                "おきなわ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[4] おきなわ ➔ [1] より ➔ <strong>★ [3] 人が (Vị trí số 3)</strong> ➔ [2] とても<br>➔ Câu hoàn chỉnh: とうきょうは おきなわより 人が とても 多いです。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[3] 人が</strong>."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "prompt": "私の しゅみは [  ] [  ] [ ★ ] [  ] ことです。",
                            "promptVi": "Sở thích của tôi là đọc truyện tranh. (Câu 40)",
                            "options": [
                                "まんがを",
                                "たくさん",
                                "読む",
                                "日本の"
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
                            "reference": "ベトナム語は はなす ことが むずかしいです。",
                            "acceptAnswers": [
                                "ベトナム語は はなす ことが むずかしいです。",
                                "ベトナム語は はなす のが むずかしいです。",
                                "ベトナム語は はなす ことが たいへんです。",
                                "ベトナム語は はなす のが たいへんです。",
                                "ベトナムごは はなす ことが むずかしいです。",
                                "ベトナムごは はなす のが むずかしいです。",
                                "べとなむごは はなす ことが むずかしいです。",
                                "べとなむごは はなす のが むずかしいです。",
                                "ベトナム語は かいわが むずかしいです。"
                            ],
                            "hints": [
                                "ベトナム語は",
                                "はなす ことが / のが",
                                "むずかしいです"
                            ]
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "prompt": "Tôi muốn có chiếc áo sơ mi trắng.",
                            "promptVi": "Câu 21 trong bộ 40 câu ôn tập",
                            "reference": "白い シャツが ほしいです。",
                            "acceptAnswers": [
                                "白い シャツが ほしいです。",
                                "わたしは 白い シャツが ほしいです。",
                                "白いシャツが ほしいです。",
                                "白い シャツを ほしいです。",
                                "しろい シャツが ほしいです。",
                                "わたしは しろい シャツが ほしいです。",
                                "しろい しゃつが ほしいです。",
                                "白い ふくが ほしいです。"
                            ],
                            "hints": [
                                "白い (しろい)",
                                "シャツが",
                                "ほしいです"
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
            "partDesc": "Đọc bài viết chia sẻ về sở thích, việc học và chọn đáp án chính xác nhất (Câu 33-34).",
            "badge": "10 Điểm",
            "passage": "わたしは いま、学校で 日本語を 勉強して います。\n日本語は かんじを かく ことが とても おもしろいです。でも、ことばが 多くて、ぶんしょうを 読む のが 少し むずかしいです。\nわたしの しゅみは まんがを 読む ことです。日本の まんがが 好きですから、いえに たくさん あります。\nえいがを みる 前に、カフェへ 行って つめたい コーヒーを のむ のも 好きです。\nらいねん、日本へ 友達と 旅行に 行ってみたいです。",
            "passageVi": "Bây giờ tôi đang học tiếng Nhật ở trường học.\nTiếng Nhật thì việc viết chữ Hán rất thú vị. Nhưng từ vựng nhiều và việc đọc câu văn hơi khó một chút.\nSở thích của tôi là đọc truyện tranh. Vì tôi thích truyện tranh Nhật Bản nên ở nhà có rất nhiều.\nTrước khi xem phim, tôi cũng thích ghé quán cà phê để uống cà phê lạnh.\nNăm sau, tôi rất muốn đi du lịch Nhật Bản cùng bạn bè.",
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "この 人は 日本語の 何が おもしろいですか。",
                    "promptVi": "Người này thấy điều gì ở tiếng Nhật thú vị?",
                    "options": [
                        "ぶんしょうを 読む こと",
                        "かんじを かく こと",
                        "ことばを おぼえる こと",
                        "テストを うける こと"
                    ],
                    "correct": 1,
                    "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「日本語は かんじを かく ことが とても おもしろいです」 ➔ Việc viết chữ Hán rất thú vị."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "この 人は えいがを みる 前に 何を しますか。",
                    "promptVi": "Người này làm gì trước khi xem phim?",
                    "options": [
                        "カフェで つめたい コーヒーを のみます。",
                        "まんがを 読みます。",
                        "日本へ 旅行に 行きます。",
                        "学校で 勉強します。"
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
                    "modelAnswer": "わたしの しゅみは まんがを 読む ことです。日本の まんがが 好きですから、いえに たくさん あります。やすみの 日に、へやで 音楽を ききながら 読みます。とても たのしい 時間です。",
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
                    "modelAnswer": "わたしは 夏が いちばん 好きです。夏は 天気が よくて、海へ 行く ことが できますから。そして、つめたい アイスクリームを たべる のが 好きです。冬は とても さむくて、外へ 出る のが にがてですから、あたたかい 夏の ほうが 好きです。",
                    "modelVi": "Tôi thích mùa hè nhất. Vì mùa hè thời tiết đẹp và tôi có thể đi biển. Và tôi thích ăn kem lạnh. Mùa đông thì rất lạnh, tôi rất ngại đi ra ngoài nên tôi thích mùa hè ấm áp hơn.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; nêu rõ mùa ưa thích bằng cấu trúc so sánh nhất (いちばん好き), sử dụng cấu trúc chỉ lý do (～から) và so sánh hơn (～のほうが好き)."
                }
            ]
        }
    ]
}

def build_m102():
    return DATA_M102
