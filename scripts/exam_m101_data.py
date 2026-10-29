#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/exam_m101_data.py
Mã đề M101: Đề Tổng Hợp Toàn Diện Marugoto A2-1 (Bài 1 - 10)
Chuẩn Can-do giáo viên 10 năm kinh nghiệm - Tuyệt đối không dùng chữ Hán chưa học.
"""

import re

PERMITTED_KANJI = set(
    '私父母子男女'          # L1
    '国外国語本読好何'      # L2
    '秋冬春夏今花海山川'    # L3
    '天気晴雨雪雲風空'      # L4
    '町店多少高安広'        # L5
    '道通右左赤青黒白'      # L6
    '時間場所駅出待止'      # L7
    '食事仕前後朝昼夜乗'    # L8
    '学校先生勉強'          # L9
    '文化音楽留旅行友達週回' # L10
    '人'                    # L1 (Nhân)
    '日月'                  # Ngày tháng (日本, ～月)
    '一二三四五六七八九十'  # Số đếm
)

def v(text, label=""):
    cjk = set(re.findall(r'[\u4e00-\u9faf]', text))
    out = cjk - PERMITTED_KANJI
    if out:
        raise ValueError(f"UNLEARNED KANJI at [{label}]: {out} in '{text}'")
    return text

def build_m101():
    return {
        "code": "M101",
        "name": "Mã Đề M101 (Đề Tổng Hợp Toàn Diện A2-1)",
        "tag": "📘 Tổng Hợp Bài 1 - 10 • Chuẩn Marugoto A2-1 Can-do",
        "desc": "Đề khảo sát năng lực toàn diện Marugoto A2-1 (Bài 1 - 10): 100% bám sát 40 câu ôn tập trọng điểm, kiểm soát nghiêm ngặt chỉ dùng 86 chữ Hán đã học.",
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
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": v("あねは ちゅうごくの ペキンに (   ) います。", "M101.Q1.p"),
                                "promptVi": "Chị gái tôi đang sống ở Bắc Kinh, Trung Quốc. (Câu 16 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("すんで", "M101.Q1.o0"),
                                    v("あそんで", "M101.Q1.o1"),
                                    v("やすんで", "M101.Q1.o2"),
                                    v("まって", "M101.Q1.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Động từ chỉ nơi cư trú (Bài 1):</strong><br>• ～に <strong>すんで います</strong>: Đang sinh sống ở... (Đúng theo Câu 16 ôn tập: Chị gái tôi đang sống ở Bắc Kinh).<br>• あそんで: Chơi.<br>• やすんで: Nghỉ ngơi.<br>• まって: Chờ đợi."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": v("一ねんの なかで、(   ) が いちばん 好きです。", "M101.Q2.p"),
                                "promptVi": "Trong một năm, tôi thích mùa hè nhất vì tôi thích ăn kem. (Câu 24 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("夏", "M101.Q2.o0"),
                                    v("雨", "M101.Q2.o1"),
                                    v("雪", "M101.Q2.o2"),
                                    v("雲", "M101.Q2.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng 4 mùa (Bài 3):</strong><br>• <strong>夏 (なつ)</strong>: Mùa hè (Đúng theo Câu 24 ôn tập: Trong 1 năm, bạn thích mùa nào nhất? - Tôi thích mùa hè nhất).<br>• 雨 (あめ): Mưa.<br>• 雪 (ゆき): Tuyết.<br>• 雲 (くも): Mây."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": v("スーパーは 駅の (   )に あります。", "M101.Q3.p"),
                                "promptVi": "Siêu thị ở gần nhà ga. (Câu 4 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ちかく", "M101.Q3.o0"),
                                    v("とおく", "M101.Q3.o1"),
                                    v("なか", "M101.Q3.o2"),
                                    v("うえ", "M101.Q3.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng chỉ vị trí (Bài 5):</strong><br>• 駅の <strong>ちかく (近く)</strong>: Gần nhà ga (Đúng theo Câu 4 ôn tập: Siêu thị ở gần nhà ga).<br>• とおく: Xa.<br>• なか: Bên trong.<br>• うえ: Phía trên."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": v("えいがを みる 前に、カフェへ 行って (   )を かいたいです。", "M101.Q4.p"),
                                "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê mua đồ uống. (Câu 13 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("のみもの", "M101.Q4.o0"),
                                    v("きっぷ", "M101.Q4.o1"),
                                    v("本", "M101.Q4.o2"),
                                    v("シャツ", "M101.Q4.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng sinh hoạt (Bài 7-8):</strong><br>• <strong>のみもの (飲み物)</strong>: Đồ uống / nước uống (Đúng theo Câu 13 ôn tập: Trước khi xem phim, tôi muốn đi quán cà phê mua đồ uống).<br>• きっぷ: Vé xe/tàu.<br>• 本: Sách.<br>• シャツ: Áo sơ mi."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": v("うえのこうえんは とても (   ) ゆうめいです。なかに どうぶつえんが あります。", "M101.Q5.p"),
                                "promptVi": "Công viên Ueno rất rộng và nổi tiếng. Bên trong có sở thú. (Câu 1 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("広くて", "M101.Q5.o0"),
                                    v("せまくて", "M101.Q5.o1"),
                                    v("高くて", "M101.Q5.o2"),
                                    v("安くて", "M101.Q5.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Nối tính từ đuôi い:</strong><br>• <strong>広い ➔ 広くて</strong>: Rộng và... (Đúng theo câu 1 ôn tập: Công viên Ueno rất rộng và nổi tiếng).<br>• せまい: Hẹp. 高い: Cao/đắt. 安い: Rẻ."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa gần nhất với câu gạch chân",
                        "groupInstruction": "Chọn câu có cách diễn đạt đồng nghĩa chuẩn xác nhất:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": v("あきはばらは でんきやが たくさん ありますから、とても べんりです。", "M101.Q6.p"),
                                "promptVi": "Akihabara có nhiều cửa hàng điện tử nên rất tiện lợi. (Câu 2 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("あきはばらは でんきやが 多くて、べんりな まちです。", "M101.Q6.o0"),
                                    v("あきはばらは でんきやが 少なくて、ふべんな まちです。", "M101.Q6.o1"),
                                    v("あきはばらは 人が 少なくて、しずかな まちです。", "M101.Q6.o2"),
                                    v("あきはばらは 店が なくて、何も かえません。", "M101.Q6.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ đồng nghĩa:</strong> たくさん あります ＝ 多くて (nhiều); べんりです ＝ べんりな まち (khu phố tiện lợi)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": v("この へんには かわいらしい ふくやが たくさん あります。", "M101.Q7.p"),
                                "promptVi": "Ở khu vực này có nhiều cửa hàng thời trang dễ thương. (Câu 3 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("この ちかくには いい ふくの 店が たくさん あります。", "M101.Q7.o0"),
                                    v("この へんには ふくの 店が ぜんぜん ありません。", "M101.Q7.o1"),
                                    v("この へんは 人が 多くて、ふくが 高いです。", "M101.Q7.o2"),
                                    v("この へんには 食べものの 店だけ あります。", "M101.Q7.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Ý nghĩa tương đương:</strong> このへん (khu vực này) ＝ このちかく; ふくや ＝ ふくの店."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": v("あさひはくぶつかんへ 行きたいんですが、どうやって 行きますか。", "M101.Q8.p"),
                                "promptVi": "Tôi muốn đi đến viện bảo tàng Asahi, đi như thế nào? (Câu 6 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("あさひはくぶつかんへの 行きかたを おしえて ください。", "M101.Q8.o0"),
                                    v("あさひはくぶつかんに 何時に 行きますか。", "M101.Q8.o1"),
                                    v("だれと あさひはくぶつかんへ 行きますか。", "M101.Q8.o2"),
                                    v("あさひはくぶつかんは どこに ありますか。", "M101.Q8.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Hỏi đường Can-do:</strong> どうやって行きますか (đi như thế nào?) đồng nghĩa với 行きかたをおしえてください (xin hãy chỉ cách đi)."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": v("やくそくの 時間を まちがえて しまいました。", "M101.Q9.p"),
                                "promptVi": "Mình bị nhầm thời gian cuộc hẹn mất rồi... (Câu 10 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("やくそくの 時間とは ちがう 時間に 行きました。", "M101.Q9.o0"),
                                    v("やくそくの 時間より はやく 行きました。", "M101.Q9.o1"),
                                    v("やくそくの 時間に ちょうど つきました。", "M101.Q9.o2"),
                                    v("やくそくの 時間を わすれませんでした。", "M101.Q9.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>まちがえる:</strong> Nhầm lẫn, sai khác ＝ ちがう時間に 行きました (đến vào thời gian khác với giờ hẹn)."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": v("わたしの しゅみは まんがを 読む ことです。", "M101.Q10.p"),
                                "promptVi": "Sở thích của tôi là đọc truyện tranh. (Câu 40 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("わたしは 日本の まんがを 読む のが 好きです。", "M101.Q10.o0"),
                                    v("わたしは まんがを ぜんぜん 読みません。", "M101.Q10.o1"),
                                    v("わたしは まんがを かく ことが 好きです。", "M101.Q10.o2"),
                                    v("わたしは まんがより アニメの ほうが 好きです。", "M101.Q10.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu sở thích:</strong> しゅみは ～ことです ＝ ～のが 好きです."
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
                                "prompt": v("学校で いろいろな 【外国語】を 勉強して います。", "M101.Q11.p"),
                                "promptVi": "Tôi đang học nhiều thứ tiếng nước ngoài ở trường học.",
                                "options": [
                                    v("がいこくご", "M101.Q11.o0"),
                                    v("そとくにこ", "M101.Q11.o1"),
                                    v("がいごくご", "M101.Q11.o2"),
                                    v("がいこくこと", "M101.Q11.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 2]: 外 (NGOẠI) + 国 (QUỐC) + 語 (NGỮ)</strong>.<br>• Ghép lại đọc âm On-yomi là <strong>がいこくご</strong>."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": v("きょうは いい 天気で、きれいな 【青空】が 広がって います。", "M101.Q12.p"),
                                "promptVi": "Hôm nay thời tiết đẹp, bầu trời xanh ngắt trải rộng.",
                                "options": [
                                    v("あおぞら", "M101.Q12.o0"),
                                    v("せいくう", "M101.Q12.o1"),
                                    v("あおそら", "M101.Q12.o2"),
                                    v("しろぞら", "M101.Q12.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 4 & 6]: 青 (THANH) + 空 (KHÔNG)</strong>.<br>• Biến âm Renkaku: 空 (そら) ➔ <strong>ぞら</strong> ➔ Đọc đúng là <strong>あおぞら</strong>."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": v("あしたの まちあわせの 【場所】は どこですか。", "M101.Q13.p"),
                                "promptVi": "Địa điểm hẹn gặp ngày mai là ở đâu thế?",
                                "options": [
                                    v("ばしょ", "M101.Q13.o0"),
                                    v("はしょ", "M101.Q13.o1"),
                                    v("じょうしょ", "M101.Q13.o2"),
                                    v("ばところ", "M101.Q13.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 場 (TRƯỜNG) + 所 (SỞ)</strong>.<br>• Ghép lại đọc là <strong>ばしょ</strong> (có âm đục ば)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": v("父と 母と いっしょに レストランで 【食事】を しました。", "M101.Q14.p"),
                                "promptVi": "Tôi đã cùng bố và mẹ dùng bữa ở nhà hàng.",
                                "options": [
                                    v("しょくじ", "M101.Q14.o0"),
                                    v("たべこと", "M101.Q14.o1"),
                                    v("しょくし", "M101.Q14.o2"),
                                    v("じきじ", "M101.Q14.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 食 (THỰC) + 事 (SỰ)</strong>.<br>• Ghép lại đọc âm On là <strong>しょくじ</strong> (có âm đục じ)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": v("にちようびに ベトナムの 【友達】と こうえんへ 行きました。", "M101.Q15.p"),
                                "promptVi": "Chủ nhật tôi đã đi công viên cùng người bạn Việt Nam.",
                                "options": [
                                    v("ともだち", "M101.Q15.o0"),
                                    v("ゆうだち", "M101.Q15.o1"),
                                    v("ともたち", "M101.Q15.o2"),
                                    v("ゆうたち", "M101.Q15.o3")
                                ],
                                "correct": 0,
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
                                "prompt": v("わたしの へやは 【ひろい】ですから、とても いいです。", "M101.Q16.p"),
                                "promptVi": "Phòng của tôi rộng rãi nên rất thoải mái.",
                                "options": [
                                    v("広い", "M101.Q16.o0"),
                                    v("店い", "M101.Q16.o1"),
                                    v("高い", "M101.Q16.o2"),
                                    v("安い", "M101.Q16.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 5]: 広 (QUẢNG)</strong> ➔ <strong>広い (ひろい)</strong>. Phân biệt: 店 (tiệm), 高 (cao), 安 (an: rẻ)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": v("えきの ロビーで 十ぷんぐらい 【まって】 ください。", "M101.Q17.p"),
                                "promptVi": "Xin vui lòng đợi khoảng 10 phút ở sảnh nhà ga.",
                                "options": [
                                    v("待って", "M101.Q17.o0"),
                                    v("止って", "M101.Q17.o1"),
                                    v("出って", "M101.Q17.o2"),
                                    v("行って", "M101.Q17.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 待 (ĐÃI)</strong> ➔ <strong>待つ (まつ)</strong> có bộ Xích (彳). Phân biệt: 止 (chỉ: dừng), 持 (trì: cầm, bộ Thủ 扌)."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": v("きょうは 【てんき】が いいですから、山が よく みえます。", "M101.Q18.p"),
                                "promptVi": "Hôm nay thời tiết đẹp nên có thể nhìn thấy rõ núi.",
                                "options": [
                                    v("天気", "M101.Q18.o0"),
                                    v("雨気", "M101.Q18.o1"),
                                    v("風気", "M101.Q18.o2"),
                                    v("空気", "M101.Q18.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 4]: 天 (THIÊN) + 気 (KHÍ)</strong> ➔ <strong>天気 (てんき)</strong>."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": v("すみません、えきへ 行く 【みち】を おしえて ください。", "M101.Q19.p"),
                                "promptVi": "Xin lỗi, xin hãy chỉ cho tôi đường đi đến nhà ga.",
                                "options": [
                                    v("道", "M101.Q19.o0"),
                                    v("通", "M101.Q19.o1"),
                                    v("右", "M101.Q19.o2"),
                                    v("左", "M101.Q19.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: 道 (ĐẠO)</strong> ➔ <strong>道 (みち)</strong>: Con đường."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": v("まいばん、日本語の ぶんぽうを 一時間 【べんきょう】します。", "M101.Q20.p"),
                                "promptVi": "Mỗi tối tôi học ngữ pháp tiếng Nhật 1 tiếng.",
                                "options": [
                                    v("勉強", "M101.Q20.o0"),
                                    v("学強", "M101.Q20.o1"),
                                    v("強勉", "M101.Q20.o2"),
                                    v("生勉", "M101.Q20.o3")
                                ],
                                "correct": 0,
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
                                "prompt": v("この 道を まっすぐ 行って、ひとつめの かど (   ) 右に まがって ください。", "M101.Q21.p"),
                                "promptVi": "Đi thẳng con đường này, rồi hãy rẽ phải ở góc đường thứ nhất. (Câu 6 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("を", "M101.Q21.o0"),
                                    v("に", "M101.Q21.o1"),
                                    v("で", "M101.Q21.o2"),
                                    v("へ", "M101.Q21.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Trợ từ chỉ hành động rẽ:</strong> Đi qua hoặc quẹo ở một địa điểm cụ thể (かど, こうさてん) dùng trợ từ <strong>を</strong> (かどを まがる)."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": v("あした 九時 (   ) しんじゅく駅の にしぐちで あいましょう。", "M101.Q22.p"),
                                "promptVi": "Ngày mai chúng ta hẹn gặp nhau vào lúc 9 giờ tại cổng tây ga Shinjuku nhé. (Câu 7 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("に", "M101.Q22.o0"),
                                    v("で", "M101.Q22.o1"),
                                    v("を", "M101.Q22.o2"),
                                    v("へ", "M101.Q22.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Trợ từ thời gian xác định:</strong> Mốc giờ cụ thể (九時, 十時) luôn đi kèm trợ từ <strong>に</strong>."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": v("えいがを みる (   )、カフェで コーヒーを のみたいです。", "M101.Q23.p"),
                                "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê uống nước. (Câu 13 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("前に", "M101.Q23.o0"),
                                    v("後で", "M101.Q23.o1"),
                                    v("から", "M101.Q23.o2"),
                                    v("ので", "M101.Q23.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc: Động từ thể từ điển (Vる) ＋ 前に:</strong> Trước khi làm việc gì (みる前に)."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": v("すみません、その じしょを (   )も いいですか。", "M101.Q24.p"),
                                "promptVi": "Xin lỗi, có thể cho tôi mượn quyển từ điển đó được không? (Câu 14 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("かりて", "M101.Q24.o0"),
                                    v("かり", "M101.Q24.o1"),
                                    v("かりる", "M101.Q24.o2"),
                                    v("かりた", "M101.Q24.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc xin phép: Động từ thể て ＋ もいいですか:</strong> かりる (Nhóm 2) ➔ <strong>かりても いいですか</strong>."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": v("とうきょうは おきなわ (   ) 人が 多いです。", "M101.Q25.p"),
                                "promptVi": "Tokyo thì đông người hơn Okinawa. (Câu 28 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("より", "M101.Q25.o0"),
                                    v("ほど", "M101.Q25.o1"),
                                    v("のほうが", "M101.Q25.o2"),
                                    v("いちばん", "M101.Q25.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc so sánh hơn: A は B より ～:</strong> Tokyo thì đông người hơn Okinawa ➔ dùng <strong>より</strong>."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": v("道に まよった (   )、日本語の テストが できませんでした。", "M101.Q26.p"),
                                "promptVi": "Vì lạc đường, nên tôi đã không thể làm được bài kiểm tra tiếng Nhật. (Câu 34 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ので", "M101.Q26.o0"),
                                    v("のに", "M101.Q26.o1"),
                                    v("ても", "M101.Q26.o2"),
                                    v("たら", "M101.Q26.o3")
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
                                "prompt": v("日本語は　＿＿＿　＿＿＿　★　＿＿＿　のが にがてです。", "M101.Q27.p"),
                                "promptVi": "Tiếng Nhật thì từ vựng nhiều. Và tôi kém việc đọc câu văn. (Câu 39 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ことばが", "M101.Q27.o0"),
                                    v("多いですから、", "M101.Q27.o1"),
                                    v("ぶんしょうを", "M101.Q27.o2"),
                                    v("読む", "M101.Q27.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Thứ tự sắp xếp đúng:</strong><br>ことばが (1) ➔ 多いですから、 (2) ➔ <strong>ぶんしょうを (3 - ★)</strong> ➔ 読む (4).<br>➔ Câu hoàn chỉnh: 日本語は ことばが 多いですから、ぶんしょうを 読む のが にがてです."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "prompt": v("ドラえもんの　＿＿＿　＿＿＿　★　＿＿＿　ありますから。", "M101.Q28.p"),
                                "promptVi": "Mình thích Doraemon hơn. Vì Doremon có chiếc túi thần kỳ. (Câu 30 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ほうが", "M101.Q28.o0"),
                                    v("好きです。", "M101.Q28.o1"),
                                    v("ふしぎな", "M101.Q28.o2"),
                                    v("ポケットが", "M101.Q28.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Thứ tự sắp xếp đúng:</strong><br>ほうが (1) ➔ 好きです。 (2) ➔ <strong>ふしぎな (3 - ★)</strong> ➔ ポケットが (4).<br>➔ Câu hoàn chỉnh: ドラえもんの ほうが 好きです。ふしぎな ポケットが ありますから。"
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "prompt": v("はくぶつかんは　＿＿＿　＿＿＿　★　＿＿＿　あります。", "M101.Q29.p"),
                                "promptVi": "Bảo tàng thì đi thẳng đường này, ở bên tay trái. (Câu 6 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("この", "M101.Q29.o0"),
                                    v("道を", "M101.Q29.o1"),
                                    v("まっすぐ行くと、", "M101.Q29.o2"),
                                    v("左がわに", "M101.Q29.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Thứ tự sắp xếp đúng:</strong><br>この (1) ➔ 道を (2) ➔ <strong>まっすぐ行くと、 (3 - ★)</strong> ➔ 左がわに (4).<br>➔ はくぶつかんは この 道を まっすぐ行くと、左がわに あります."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "prompt": v("わたしは　＿＿＿　＿＿＿　★　＿＿＿　勉強して います。", "M101.Q30.p"),
                                "promptVi": "Tôi đang học tiếng Nhật 1 tuần 3 lần ở trung tâm. (Câu 32 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("センターで", "M101.Q30.o0"),
                                    v("週に", "M101.Q30.o1"),
                                    v("三回", "M101.Q30.o2"),
                                    v("日本語を", "M101.Q30.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Thứ tự sắp xếp đúng:</strong><br>センターで (1) ➔ 週に (2) ➔ <strong>三回 (3 - ★)</strong> ➔ 日本語を (4).<br>➔ わたしは センターで 週に 三回 日本語を 勉強して います."
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
                                "reference": v("わたしは 夏が いちばん 好きです。アイスクリームが 好きですから。 tissue", "M101.Q31.ref") if False else v("わたしは 夏が いちばん 好きです。アイスクリームが 好きですから。そして、さむいのが にがてですから。", "M101.Q31.ref"),
                                "acceptAnswers": [
                                    v("わたしは 夏が いちばん 好きです。アイスクリームが 好きですから。そして、さむいのが にがてですから。", "M101.Q31.ans0"),
                                    v("夏が いちばん 好きです。アイスクリームが 好きですから。さむいのが にがてですから。", "M101.Q31.ans1"),
                                    v("夏が いちばん 好きです。アイスクリームが 好きですから。そして さむいのが にがてですから。", "M101.Q31.ans2")
                                ],
                                "hints": ["夏が いちばん 好きです", "アイスクリームが 好きですから", "さむいのが にがてですから"]
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "prompt": "Vì bão, nên tàu điện và xe bus dừng chạy.",
                                "promptVi": "Câu 35 trong bộ 40 câu ôn tập",
                                "reference": v("たいふうで、でんしゃと バスが 止まりました。", "M101.Q32.ref"),
                                "acceptAnswers": [
                                    v("たいふうで、でんしゃと バスが 止まりました。", "M101.Q32.ans0"),
                                    v("たいふうで でんしゃと バスが 止まりました。", "M101.Q32.ans1"),
                                    v("たいふうですから、でんしゃと バスが 止まりました。", "M101.Q32.ans2")
                                ],
                                "hints": ["たいふうで (do bão)", "でんしゃと バスが (tàu điện và xe bus)", "止まりました (đã dừng lại)"]
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
                "passage": v("アンさんへ。\nあしたの やくそくの 時間は 朝 十時です。\nしんじゅく駅の にしぐちで 待って います。\nえきの 前の 道を まっすぐ 行って、右がわに ある 日本りょうりの 店で 食事を しましょう。\nもし 時間に おくれたら、でんわを して ください。\nたなかより", "M101.passage"),
                "passageVi": "Gửi bạn An.\nThời gian hẹn ngày mai là 10 giờ sáng.\nMình sẽ đợi bạn ở cổng Tây ga Shinjuku nhé.\nĐi thẳng con đường phía trước nhà ga, chúng mình sẽ cùng dùng bữa ở quán món ăn Nhật Bản nằm ở phía bên tay phải.\nNếu bị muộn giờ thì hãy gọi điện thoại cho mình nhé.\nTừ Tanaka",
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": v("たなかさんと アンさんは どこで あいますか。", "M101.Q33.p"),
                        "promptVi": "Tanaka và An sẽ gặp nhau ở đâu?",
                        "options": [
                            v("しんじゅく駅の にしぐち", "M101.Q33.o0"),
                            v("えきの なかの 店", "M101.Q33.o1"),
                            v("日本りょうりの 店の なか", "M101.Q33.o2"),
                            v("あさひはくぶつかん", "M101.Q33.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài:</strong> 「しんじゅく駅の にしぐちで 待って います」 ➔ Hai người hẹn gặp ở cổng Tây ga Shinjuku."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": v("ふたりは あった 後で、何を しますか。", "M101.Q34.p"),
                        "promptVi": "Sau khi gặp nhau, hai người sẽ làm gì?",
                        "options": [
                            v("日本りょうりの 店で 食事を します。", "M101.Q34.o0"),
                            v("えきで でんわを します。", "M101.Q34.o1"),
                            v("はくぶつかんへ 行きます。", "M101.Q34.o2"),
                            v("バスに 乗って かえります。", "M101.Q34.o3")
                        ],
                        "correct": 0,
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
                        "modelAnswer": v("わたしの まちは とても 広くて、べんりな まちです。えきの ちかくには たくさんの 店が あって、いつも 人が 多いです。わたしは えきの 前の カフェで 音楽を きく ことが 好きです。こうえんも あって、春には きれいな 花が たくさん さきます。とても すみやすい まちですから、ぜひ あそびに きて ください。", "M101.Q35.ans"),
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
                        "modelAnswer": v("わたしは いま、学校で 日本語を 勉強して います。日本語は かんじを かく ことが とても おもしろいです。でも、ことばが 多くて、ぶんしょうを 読む のが 少し むずかしいです。ですから、まい朝 三十ぷん 日本語を はなす れんしゅうを して います。そして、日本の まんがを たくさん 読んで います。これからも いっしょうけんめい がんばりたいです。", "M101.Q36.ans"),
                        "modelVi": "Bây giờ tôi đang học tiếng Nhật ở trường học. Tiếng Nhật thì việc viết chữ Hán rất thú vị. Nhưng từ vựng nhiều và việc đọc câu văn hơi khó một chút. Vì vậy, mỗi sáng tôi đều luyện nói tiếng Nhật 30 phút. Và tôi đọc rất nhiều truyện tranh Nhật Bản. Sau này tôi cũng sẽ cố gắng hết mình.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; nêu rõ cảm nhận về việc học tiếng Nhật, phương pháp rèn luyện tích cực."
                    }
                ]
            }
        ]
    }
