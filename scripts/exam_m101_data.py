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


DATA_M101 = {
    "code": "M101",
    "name": "Mã Đề M101 (Đề Tổng Hợp Toàn Diện A2-1)",
    "tag": "📘 Tổng Hợp Bài 1 - 10 • Chuẩn Marugoto A2-1 Can-do",
    "desc": "Đề khảo sát năng lực toàn diện Marugoto A2-1 (Bài 1 - 10): 100% bám sát 40 câu ôn tập trọng điểm, kiểm soát nghiêm ngặt chỉ dùng 86 chữ Hán đã học.",
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
                    "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                    "items": [
                        {
                            "id": 1,
                            "type": "mc",
                            "prompt": "あねは ちゅうごくの ペキンに (   ) います。",
                            "promptVi": "Chị gái tôi đang sống ở Bắc Kinh, Trung Quốc. (Câu 16 trong bộ 40 câu ôn tập)",
                            "options": [
                                "すんで",
                                "あそんで",
                                "やすんで",
                                "まって"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Động từ chỉ nơi cư trú (Bài 1):</strong><br>• ～に <strong>すんで います</strong>: Đang sinh sống ở... (Đúng theo Câu 16 ôn tập: Chị gái tôi đang sống ở Bắc Kinh).<br>• あそんで: Chơi.<br>• やすんで: Nghỉ ngơi.<br>• まって: Chờ đợi."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "一ねんの なかで、(   ) が いちばん 好きです。",
                            "promptVi": "Trong một năm, tôi thích mùa hè nhất vì tôi thích ăn kem. (Câu 24 trong bộ 40 câu ôn tập)",
                            "options": [
                                "雨",
                                "雪",
                                "雲",
                                "夏"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng 4 mùa (Bài 3):</strong><br>• <strong>夏 (なつ)</strong>: Mùa hè (Đúng theo Câu 24 ôn tập: Trong 1 năm, bạn thích mùa nào nhất? - Tôi thích mùa hè nhất).<br>• 雨 (あめ): Mưa.<br>• 雪 (ゆき): Tuyết.<br>• 雲 (くも): Mây."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "スーパーは 駅の (   )に あります。",
                            "promptVi": "Siêu thị ở gần nhà ga. (Câu 4 trong bộ 40 câu ôn tập)",
                            "options": [
                                "とおく",
                                "なか",
                                "ちかく",
                                "うえ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Từ vựng chỉ vị trí (Bài 5):</strong><br>• 駅の <strong>ちかく (近く)</strong>: Gần nhà ga (Đúng theo Câu 4 ôn tập: Siêu thị ở gần nhà ga).<br>• とおく: Xa.<br>• なか: Bên trong.<br>• うえ: Phía trên."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "えいがを みる 前に、カフェへ 行って (   )を かいたいです。",
                            "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê mua đồ uống. (Câu 13 trong bộ 40 câu ôn tập)",
                            "options": [
                                "きっぷ",
                                "本",
                                "のみもの",
                                "シャツ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Từ vựng sinh hoạt (Bài 7-8):</strong><br>• <strong>のみもの (飲み物)</strong>: Đồ uống / nước uống (Đúng theo Câu 13 ôn tập: Trước khi xem phim, tôi muốn đi quán cà phê mua đồ uống).<br>• きっぷ: Vé xe/tàu.<br>• 本: Sách.<br>• シャツ: Áo sơ mi."
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "うえのこうえんは とても (   ) ゆうめいです。なかに どうぶつえんが あります。",
                            "promptVi": "Công viên Ueno rất rộng và nổi tiếng. Bên trong có sở thú. (Câu 1 trong bộ 40 câu ôn tập)",
                            "options": [
                                "せまくて",
                                "高くて",
                                "安くて",
                                "広くて"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Nối tính từ đuôi い:</strong><br>• <strong>広い ➔ 広くて</strong>: Rộng và... (Đúng theo câu 1 ôn tập: Công viên Ueno rất rộng và nổi tiếng).<br>• せまい: Hẹp. 高い: Cao/đắt. 安い: Rẻ."
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
                            "prompt": "あきはばらは でんきやが <u>たくさん あります</u>から、とても べんりです。",
                            "promptVi": "Akihabara có nhiều cửa hàng điện tử nên rất tiện lợi. (Câu 2 trong bộ 40 câu ôn tập)",
                            "options": [
                                "少なくて",
                                "多くて",
                                "高くて",
                                "やすくて"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Từ đồng nghĩa (Bài 5):</strong> たくさん あります ＝ <strong>多くて</strong> (nhiều). Ngược nghĩa là 少なくて (ít). Chữ 多 (Đa - nhiều) đã học ở Bài 5."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "この へんには <u>かわいらしい</u> ふくやが たくさん あります。",
                            "promptVi": "Ở khu vực này có nhiều cửa hàng thời trang dễ thương. (Câu 3 trong bộ 40 câu ôn tập)",
                            "options": [
                                "こわい",
                                "ふるい",
                                "きたない",
                                "かわいい"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ đồng nghĩa (Bài 7):</strong> かわいらしい ＝ <strong>かわいい</strong> (dễ thương, xinh xắn)."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "あさひはくぶつかんへ 行きたいんですが、<u>どうやって 行きますか</u>。",
                            "promptVi": "Tôi muốn đi đến viện bảo tàng Asahi, đi như thế nào? (Câu 6 trong bộ 40 câu ôn tập)",
                            "options": [
                                "行きかたを おしえて ください",
                                "何時に 行きますか",
                                "だれと 行きますか",
                                "いくら かかりますか"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cách hỏi đường (Bài 5):</strong> どうやって 行きますか ＝ <strong>行きかたを おしえて ください</strong> (Hãy chỉ cho tôi cách đi). Chữ 行 (Hành) đã học ở Bài 5."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "やくそくの 時間を <u>まちがえて</u> しまいました。",
                            "promptVi": "Mình bị nhầm thời gian cuộc hẹn mất rồi... (Câu 10 trong bộ 40 câu ôn tập)",
                            "options": [
                                "はやく 行きました",
                                "ちょうど つきました",
                                "わすれませんでした",
                                "ちがう 時間に 行きました"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng sinh hoạt (Bài 7):</strong> まちがえる (nhầm lẫn) ＝ <strong>ちがう 時間に 行きました</strong> (đã đến vào thời gian khác)."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "わたしの しゅみは まんがを たくさん <u>あつめる</u> ことです。",
                            "promptVi": "Sở thích của tôi là sưu tầm thật nhiều truyện tranh. (Câu 40 trong bộ 40 câu ôn tập)",
                            "options": [
                                "うる",
                                "もつ",
                                "すてる",
                                "かりる"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Từ vựng sở thích (Bài 10):</strong> あつめる (sưu tầm, tích lũy) ＝ <strong>もつ</strong> (có, sở hữu nhiều)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec2_kanji",
            "partNumber": "II",
            "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
            "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán thành Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20) chuẩn 100% chữ Hán Bài 1-10.",
            "badge": "20 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                    "groupInstruction": "Chọn cách đọc Hiragana chính xác nhất cho chữ Hán được gạch chân (Chữ Hán Bài 1-10):",
                    "items": [
                        {
                            "id": 11,
                            "type": "mc",
                            "prompt": "学校で いろいろな 【外国語】を 勉強して います。",
                            "promptVi": "Tôi đang học nhiều thứ tiếng nước ngoài ở trường học.",
                            "options": [
                                "そとくにこ",
                                "がいごくご",
                                "がいこくご",
                                "がいこくこと"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ Hán [Bài 2]: 外 (NGOẠI) + 国 (QUỐC) + 語 (NGỮ)</strong>.<br>• Ghép lại đọc âm On-yomi là <strong>がいこくご</strong>."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "きょうは いい 天気で、きれいな 【青空】が 広がって います。",
                            "promptVi": "Hôm nay thời tiết đẹp, bầu trời xanh ngắt trải rộng.",
                            "options": [
                                "せいくう",
                                "あおぞら",
                                "あおそら",
                                "しろぞら"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ Hán [Bài 4 & 6]: 青 (THANH) + 空 (KHÔNG)</strong>.<br>• Biến âm Renkaku: 空 (そら) ➔ <strong>ぞら</strong> ➔ Đọc đúng là <strong>あおぞら</strong>."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "あしたの まちあわせの 【場所】は どこですか。",
                            "promptVi": "Địa điểm hẹn gặp ngày mai là ở đâu thế?",
                            "options": [
                                "ばしょ",
                                "はしょ",
                                "じょうしょ",
                                "ばところ"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ Hán [Bài 7]: 場 (TRƯỜNG) + 所 (SỞ)</strong>.<br>• Ghép lại đọc là <strong>ばしょ</strong> (có âm đục ば)."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "父と 母と いっしょに レストランで 【食事】を しました。",
                            "promptVi": "Tôi đã cùng bố và mẹ dùng bữa ở nhà hàng.",
                            "options": [
                                "たべこと",
                                "しょくじ",
                                "しょくし",
                                "じきじ"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ Hán [Bài 8]: 食 (THỰC) + 事 (SỰ)</strong>.<br>• Ghép lại đọc âm On là <strong>しょくじ</strong> (có âm đục じ)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "にちようびに ベトナムの 【友達】と こうえんへ 行きました。",
                            "promptVi": "Chủ nhật tôi đã đi công viên cùng người bạn Việt Nam.",
                            "options": [
                                "ゆうだち",
                                "ともだち",
                                "ともたち",
                                "ゆうたち"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ Hán [Bài 10]: 友 (HỮU) + 達 (ĐẠT)</strong>.<br>• Biến âm đục: 達 (たち) ➔ <strong>だち</strong> ➔ Đọc đúng là <strong>ともだち</strong>."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Chọn chữ Hán đúng cho từ Hiragana trong ngoặc 【 】",
                    "groupInstruction": "Chọn chữ Hán viết đúng nhất cho từ Hiragana trong câu (Chữ Hán Bài 1-10):",
                    "items": [
                        {
                            "id": 16,
                            "type": "mc",
                            "prompt": "わたしの へやは 【ひろい】ですから、とても いいです。",
                            "promptVi": "Phòng của tôi rộng rãi nên rất thoải mái.",
                            "options": [
                                "広い",
                                "店い",
                                "高い",
                                "安い"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ Hán [Bài 5]: 広 (QUẢNG)</strong> ➔ <strong>広い (ひろい)</strong>. Phân biệt: 店 (tiệm), 高 (cao), 安 (an: rẻ)."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "えきの ロビーで 十ぷんぐらい 【まって】 ください。",
                            "promptVi": "Xin vui lòng đợi khoảng 10 phút ở sảnh nhà ga.",
                            "options": [
                                "止って",
                                "出って",
                                "行って",
                                "待って"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ Hán [Bài 7]: 待 (ĐÃI)</strong> ➔ <strong>待つ (まつ)</strong> có bộ Xích (彳). Phân biệt: 止 (chỉ: dừng), 持 (trì: cầm, bộ Thủ 扌)."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "きょうは 【てんき】が いいですから、山が よく みえます。",
                            "promptVi": "Hôm nay thời tiết đẹp nên có thể nhìn thấy rõ núi.",
                            "options": [
                                "天気",
                                "雨気",
                                "風気",
                                "空気"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ Hán [Bài 4]: 天 (THIÊN) + 気 (KHÍ)</strong> ➔ <strong>天気 (てんき)</strong>."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "すみません、えきへ 行く 【みち】を おしえて ください。",
                            "promptVi": "Xin lỗi, xin hãy chỉ cho tôi đường đi đến nhà ga.",
                            "options": [
                                "通",
                                "右",
                                "道",
                                "左"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ Hán [Bài 6]: 道 (ĐẠO)</strong> ➔ <strong>道 (みち)</strong>: Con đường."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "まいばん、日本語の ぶんぽうを 一時間 【べんきょう】します。",
                            "promptVi": "Mỗi tối tôi học ngữ pháp tiếng Nhật 1 tiếng.",
                            "options": [
                                "学強",
                                "強勉",
                                "勉強",
                                "生勉"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ Hán [Bài 9]: 勉 (MIỄN) + 強 (CƯỜNG)</strong> ➔ <strong>勉強 (べんきょう)</strong>."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec3_grammar",
            "partNumber": "III",
            "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
            "partDesc": "Gồm 3 dạng bài: Trắc nghiệm trợ từ & cấu trúc (21-26), Sắp xếp câu Hái sao ☆ (27-30) và Dịch câu tự luận (31-32).",
            "badge": "30 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Chọn phương án đúng nhất điền vào chỗ trống",
                    "groupInstruction": "Chọn từ / trợ từ thích hợp nhất để hoàn thành câu:",
                    "items": [
                        {
                            "id": 21,
                            "type": "mc",
                            "prompt": "この 道を まっすぐ 行って、ひとつめの かど (   ) 右に まがって ください。",
                            "promptVi": "Đi thẳng con đường này, rồi hãy rẽ phải ở góc đường thứ nhất. (Câu 6 trong bộ 40 câu ôn tập)",
                            "options": [
                                "を",
                                "に",
                                "で",
                                "へ"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Trợ từ chỉ hành động rẽ:</strong> Đi qua hoặc quẹo ở một địa điểm cụ thể (かど, こうさてん) dùng trợ từ <strong>を</strong> (かどを まがる)."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "あした 九時 (   ) しんじゅく駅の にしぐちで あいましょう。",
                            "promptVi": "Ngày mai chúng ta hẹn gặp nhau vào lúc 9 giờ tại cổng tây ga Shinjuku nhé. (Câu 7 trong bộ 40 câu ôn tập)",
                            "options": [
                                "で",
                                "を",
                                "に",
                                "へ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Trợ từ thời gian xác định:</strong> Mốc giờ cụ thể (九時, 十時) luôn đi kèm trợ từ <strong>に</strong>."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "えいがを みる (   )、カフェで コーヒーを のみたいです。",
                            "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê uống nước. (Câu 13 trong bộ 40 câu ôn tập)",
                            "options": [
                                "後で",
                                "から",
                                "ので",
                                "前に"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Cấu trúc: Động từ thể từ điển (Vる) ＋ 前に:</strong> Trước khi làm việc gì (みる前に)."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "すみません、その じしょを (   )も いいですか。",
                            "promptVi": "Xin lỗi, có thể cho tôi mượn quyển từ điển đó được không? (Câu 14 trong bộ 40 câu ôn tập)",
                            "options": [
                                "かり",
                                "かりて",
                                "かりる",
                                "かりた"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Cấu trúc xin phép: Động từ thể て ＋ もいいですか:</strong> かりる (Nhóm 2) ➔ <strong>かりても いいですか</strong>."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "とうきょうは おきなわ (   ) 人が 多いです。",
                            "promptVi": "Tokyo thì đông người hơn Okinawa. (Câu 28 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ほど",
                                "より",
                                "のほうが",
                                "いちばん"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Cấu trúc so sánh hơn: A は B より ～:</strong> Tokyo thì đông người hơn Okinawa ➔ dùng <strong>より</strong>."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "道に まよった (   )、日本語の テストが できませんでした。",
                            "promptVi": "Vì lạc đường, nên tôi đã không thể làm được bài kiểm tra tiếng Nhật. (Câu 34 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ので",
                                "のに",
                                "ても",
                                "たら"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cấu trúc nguyên nhân khách quan: ～ので:</strong> Vì lạc đường (まよったので) nên không làm được bài thi."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Sắp xếp câu tìm từ tại vị trí ngôi sao (★)",
                    "groupInstruction": "Sắp xếp 4 từ/cụm từ theo thứ tự đúng và chọn từ nằm ở vị trí ngôi sao (★):",
                    "items": [
                        {
                            "id": 27,
                            "type": "star",
                            "prompt": "日本語は　＿＿＿　＿＿＿　★　＿＿＿　のが にがてです。",
                            "promptVi": "Tiếng Nhật thì từ vựng nhiều. Và tôi kém việc đọc câu văn. (Câu 39 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ぶんしょうを",
                                "ことばが",
                                "読む",
                                "多いですから、"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[2] ことばが ➔ [4] 多いですから、 ➔ <strong>★ [1] ぶんしょうを (Vị trí số 3)</strong> ➔ [3] 読む<br>➔ Câu hoàn chỉnh: 日本語は ことばが 多いですから、ぶんしょうを 読む のが にがてです。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[1] ぶんしょうを</strong>."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "prompt": "ドラえもんの　＿＿＿　＿＿＿　★　＿＿＿　ありますから。",
                            "promptVi": "Mình thích Doraemon hơn. Vì Doremon có chiếc túi thần kỳ. (Câu 30 trong bộ 40 câu ôn tập)",
                            "options": [
                                "好きです。",
                                "ポケットが",
                                "ほうが",
                                "ふしぎな"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] ほうが ➔ [1] 好きです。 ➔ <strong>★ [4] ふしぎな (Vị trí số 3)</strong> ➔ [2] ポケットが<br>➔ Câu hoàn chỉnh: ドラえもんの ほうが 好きです。ふしぎな ポケットが ありますから。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[4] ふしぎな</strong>."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "prompt": "はくぶつかんは　＿＿＿　＿＿＿　★　＿＿＿　あります。",
                            "promptVi": "Bảo tàng thì đi thẳng đường này, ở bên tay trái. (Câu 6 trong bộ 40 câu ôn tập)",
                            "options": [
                                "左がわに",
                                "まっすぐ行くと、",
                                "この",
                                "道を"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] この ➔ [4] 道を ➔ <strong>★ [2] まっすぐ行くと、 (Vị trí số 3)</strong> ➔ [1] 左がわに<br>➔ Câu hoàn chỉnh: はくぶつかんは この 道を まっすぐ行くと、左がわに あります。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[2] まっすぐ行くと、</strong>."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "prompt": "わたしは　＿＿＿　＿＿＿　★　＿＿＿　勉強して います。",
                            "promptVi": "Tôi đang học tiếng Nhật 1 tuần 3 lần ở trung tâm. (Câu 32 trong bộ 40 câu ôn tập)",
                            "options": [
                                "日本語を",
                                "週に",
                                "三回",
                                "センターで"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[4] センターで ➔ [2] 週に ➔ <strong>★ [3] 三回 (Vị trí số 3)</strong> ➔ [1] 日本語を<br>➔ Câu hoàn chỉnh: わたしは センターで 週に 三回 日本語を 勉強して います。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[3] 三回</strong>."
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
                            "prompt": "Trong 1 năm, tôi thích mùa hè nhất vì tôi thích kem. Và tôi sợ lạnh.",
                            "promptVi": "Câu 24 trong bộ 40 câu ôn tập",
                            "reference": "わたしは 夏が いちばん 好きです。アイスクリームが 好きですから。そして、さむいのが にがてですから。",
                            "acceptAnswers": [
                                "わたしは 夏が いちばん 好きです。アイスクリームが 好きですから。そして、さむいのが にがてですから。",
                                "夏が いちばん 好きです。アイスクリームが 好きですから。さむいのが にがてですから。",
                                "夏が いちばん 好きです。アイスクリームが 好きですから。そして さむいのが にがてですから。",
                                "夏が いちばん 好きです。アイスが 好きですから。そして、さむいのが にがてです。",
                                "夏が いちばん 好きです。アイスクリームが 好きですから。それから、さむいのが にがてです。",
                                "一ねんの なかで、夏が いちばん 好きです。アイスクリームが 好きですから。そして、さむいのが にがてです。",
                                "一ねんで 夏が いちばん 好きです。アイスが 好きですから。そして さむいのが にがてです。",
                                "わたしは なつが いちばん すきです。あいすくりーむが すきですから。そして、さむいのが にがてですから。",
                                "なつが いちばん すきです。あいすくりーむが すきですから。そして、さむいのが にがてですから。",
                                "なつが いちばん すきです。あいすが すきですから。それから、さむいのが にがてです。",
                                "いちねん、なつがいちばんすきですから、クリームがすきです。それから、さむいが にがてです。",
                                "いちねんのなかで なつが いちばん すきです。あいすが すきですから。そして、さむいのが にがてです。",
                                "なつが いちばん すきです。あいすくりーむが すきですから。さむいのが にがてです。"
                            ],
                            "hints": [
                                "夏が いちばん 好きです",
                                "アイスクリームが 好きですから",
                                "さむいのが にがてですから"
                            ]
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "prompt": "Vì bão, nên tàu điện và xe bus dừng chạy.",
                            "promptVi": "Câu 35 trong bộ 40 câu ôn tập",
                            "reference": "たいふうで、でんしゃと バスが 止まりました。",
                            "acceptAnswers": [
                                "たいふうで、でんしゃと バスが 止まりました。",
                                "たいふうで でんしゃと バスが 止まりました。",
                                "たいふうですから、でんしゃと バスが 止まりました。",
                                "たいふうだから、でんしゃと バスが 止まりました。",
                                "たいふうなので、でんしゃと バスが 止まりました。",
                                "たいふうで、バスと でんしゃが 止まりました。",
                                "たいふうで、でんしゃと バスが とまりました。",
                                "たいふうですから、でんしゃと ばすが とまりました。"
                            ],
                            "hints": [
                                "たいふうで (do bão)",
                                "でんしゃと バスが (tàu điện và xe bus)",
                                "止まりました (đã dừng lại)"
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
            "partDesc": "Đọc tin nhắn đời sống chân thực và chọn đáp án đúng nhất (Câu 33-34).",
            "badge": "10 Điểm",
            "passage": "アンさんへ。\nあしたの やくそくの 時間は 朝 十時です。\nしんじゅく駅の にしぐちで 待って います。\nえきの 前の 道を まっすぐ 行って、右がわに ある 日本りょうりの 店で 食事を しましょう。\nもし 時間に おくれたら、でんわを して ください。\nたなかより",
            "passageVi": "Gửi bạn An.\nThời gian hẹn ngày mai là 10 giờ sáng.\nMình sẽ đợi bạn ở cổng Tây ga Shinjuku nhé.\nĐi thẳng con đường phía trước nhà ga, chúng mình sẽ cùng dùng bữa ở quán món ăn Nhật Bản nằm ở phía bên tay phải.\nNếu bị muộn giờ thì hãy gọi điện thoại cho mình nhé.\nTừ Tanaka",
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "たなかさんと アンさんは どこで あいますか。",
                    "promptVi": "Tanaka và An sẽ gặp nhau ở đâu?",
                    "options": [
                        "えきの なかの 店",
                        "日本りょうりの 店の なか",
                        "あさひはくぶつかん",
                        "しんじゅく駅の にしぐち"
                    ],
                    "correct": 3,
                    "explain": "💡 <strong>Thông tin trong bài:</strong> 「しんじゅく駅の にしぐちで 待って います」 ➔ Hai người hẹn gặp ở cổng Tây ga Shinjuku."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "ふたりは あった 後で、何を しますか。",
                    "promptVi": "Sau khi gặp nhau, hai người sẽ làm gì?",
                    "options": [
                        "えきで でんわを します。",
                        "はくぶつかんへ 行きます。",
                        "日本りょうりの 店で 食事を します。",
                        "バスに 乗って かえります。"
                    ],
                    "correct": 2,
                    "explain": "💡 <strong>Thông tin trong bài:</strong> 「日本りょうりの 店で 食事を しましょう」 ➔ Cùng nhau đi ăn ở quán đồ Nhật."
                }
            ]
        },
        {
            "id": "sec5_essay",
            "partNumber": "V",
            "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
            "partDesc": "Viết đoạn văn tối thiểu 50 từ/ký tự theo chủ đề Can-do đời sống Nhật Bản (Câu 35-36).",
            "badge": "15 Điểm",
            "items": [
                {
                    "id": 35,
                    "type": "essay",
                    "prompt": "あなたが すんで いる まちについて かいて ください。（とくちょう、すきな 場所、店など、五十じ いじょう）",
                    "promptVi": "Hãy viết đoạn văn giới thiệu về thành phố nơi bạn đang sống (đặc điểm, nơi bạn thích, cửa hàng... tối thiểu 50 chữ/ký tự).",
                    "minWords": 50,
                    "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしの まちは とても 広くて、べんりな まちです...",
                    "hints": [
                        "Đặc điểm thành phố: わたしの まちは ～て、～な まちです (広くて べんり / しずかで きれい)",
                        "Có những gì: えきの ちかくに ～が たくさん あります (店 / こうえん)",
                        "Nơi bạn thích: わたしは ～へ 行く ことが 好きです",
                        "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                    ],
                    "modelAnswer": "わたしの まちは とても 広くて、べんりな まちです。えきの ちかくには たくさんの 店が あって、いつも 人が 多いです。わたしは えきの 前の カフェで 音楽を きく ことが 好きです。こうえんも あって、春には きれいな 花が たくさん さきます。とても すみやすい まちですから、ぜひ あそびに きて ください。",
                    "modelVi": "Thành phố của tôi rất rộng và tiện lợi. Gần nhà ga có rất nhiều cửa hàng và lúc nào cũng đông người. Tôi thích nghe nhạc ở quán cà phê trước ga. Thành phố cũng có công viên, mùa xuân có rất nhiều hoa đẹp nở rộ. Đây là một thành phố rất đáng sống, bạn hãy ghé chơi nhé.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; miêu tả rõ ràng đặc điểm thành phố, sử dụng đúng tính từ nối (広くて) và cấu trúc sở thích (～ことが好き)."
                },
                {
                    "id": 36,
                    "type": "essay",
                    "prompt": "あなたの 日本語の 勉強について おしえて ください。（おもしろい こと、むずかしい こと、れんしゅうの ほうほうなど、五十じ いじょう）",
                    "promptVi": "Hãy viết đoạn văn chia sẻ về việc học tiếng Nhật của bạn (điều thú vị, điều khó khăn, cách luyện tập... tối thiểu 50 chữ/ký tự).",
                    "minWords": 50,
                    "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは 学校で 日本語を 勉強して います...",
                    "hints": [
                        "Bạn đang học ở đâu: わたしは 学校 / センターで 日本語を 勉強して います",
                        "Điều thú vị / khó: かん字を かく ことが おもしろい / ぶんしょうを 読む のが むずかしい",
                        "Cách bạn luyện tập: まい日 ～を れんしゅうして います (はなす / まんがを 読む)",
                        "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                    ],
                    "modelAnswer": "わたしは いま、学校で 日本語を 勉強して います。日本語は かんじを かく ことが とても おもしろいです。でも、ことばが 多くて、ぶんしょうを 読む のが 少し むずかしいです。ですから、まい朝 三十ぷん 日本語を はなす れんしゅうを して います。そして、日本の まんがを たくさん 読んで います。これからも いっしょうけんめい がんばりたいです。",
                    "modelVi": "Bây giờ tôi đang học tiếng Nhật ở trường học. Tiếng Nhật thì việc viết chữ Hán rất thú vị. Nhưng từ vựng nhiều và việc đọc câu văn hơi khó một chút. Vì vậy, mỗi sáng tôi đều luyện nói tiếng Nhật 30 phút. Và tôi đọc rất nhiều truyện tranh Nhật Bản. Sau này tôi cũng sẽ cố gắng hết mình.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; nêu rõ cảm nhận về việc học tiếng Nhật, phương pháp rèn luyện tích cực."
                }
            ]
        }
    ]
}

def build_m101():
    return DATA_M101
