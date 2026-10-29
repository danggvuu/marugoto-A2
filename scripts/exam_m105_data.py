#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/exam_m105_data.py
Mã đề M105: Đề Chuyên Sâu Học Tập, Ngoại Ngữ & Ước Mơ (Bài 1 - 10)
Chuẩn Can-do giáo viên 10 năm kinh nghiệm - Tuyệt đối không dùng chữ Hán chưa học.
"""

import re
try:
    from scripts.exam_m101_data import PERMITTED_KANJI, v
except ImportError:
    from exam_m101_data import PERMITTED_KANJI, v

def build_m105():
    return {
        "code": "M105",
        "name": "Mã Đề M105 (Phương Pháp Học Ngoại Ngữ & Ước Mơ)",
        "tag": "🎓 Ngoại Ngữ • Kỹ Năng Nghe Nói Đọc • Ước Mơ Du Học • Chuẩn A2-1",
        "desc": "Đề chuyên sâu về phương pháp học tiếng Nhật (ことば, ぶんぽう, かんじ, まんがを 読む), so sánh độ khó các ngoại ngữ (ベトナム語, フランス語, えいご, ちゅうごく語), và mục tiêu du học.",
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
                                "prompt": v("日本語は (   ) を かく ことが とても おもしろいです。", "M105.Q1.p"),
                                "promptVi": "Tiếng Nhật thì việc viết chữ Hán rất thú vị. (Câu 38 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("かんじ", "M105.Q1.o0"),
                                    v("みず", "M105.Q1.o1"),
                                    v("えき", "M105.Q1.o2"),
                                    v("まち", "M105.Q1.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng kỹ năng học tiếng Nhật (Bài 2):</strong> Viết chữ Hán ➔ <strong>かんじ</strong>を かく こと."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": v("いままで どんな (   ) を 勉強しましたか。", "M105.Q2.p"),
                                "promptVi": "Cho đến bây giờ bạn đã học ngoại ngữ nào rồi? (Câu 12 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("外国語", "M105.Q2.o0"),
                                    v("天気", "M105.Q2.o1"),
                                    v("場所", "M105.Q2.o2"),
                                    v("時間", "M105.Q2.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán ghép (Bài 2):</strong> Ngoại ngữ là <strong>外国語</strong> (がいこくご). Cả 外, 国, 語 đều học ở Bài 2."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": v("すみません、この (   ) の つかいかたを おしえて くださいませんか。", "M105.Q3.p"),
                                "promptVi": "Xin lỗi, bạn có thể chỉ cho tôi cách sử dụng kim từ điển này không? (Câu 18 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("でんしじしょ", "M105.Q3.o0"),
                                    v("コーヒー", "M105.Q3.o1"),
                                    v("シャツ", "M105.Q3.o2"),
                                    v("くつ", "M105.Q3.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng công cụ học tập (Bài 2):</strong> Kim từ điển là <strong>でんしじしょ</strong>."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": v("日本語は ことばが 多いです。そして、(   ) を 読む のが にがてです。", "M105.Q4.p"),
                                "promptVi": "Tiếng Nhật thì từ vựng nhiều. Và tôi kém việc đọc câu văn. (Câu 39 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ぶんしょう", "M105.Q4.o0"),
                                    v("みず", "M105.Q4.o1"),
                                    v("やま", "M105.Q4.o2"),
                                    v("かわ", "M105.Q4.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng đọc hiểu (Bài 2):</strong> Đọc đoạn văn, câu văn là <strong>ぶんしょう</strong>を 読む."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": v("道に (   ) ので、日本語の テストが できませんでした。", "M105.Q5.p"),
                                "promptVi": "Vì lạc đường nên tôi đã không thể làm bài kiểm tra tiếng Nhật. (Câu 34 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("まよった", "M105.Q5.o0"),
                                    v("のぼった", "M105.Q5.o1"),
                                    v("おわった", "M105.Q5.o2"),
                                    v("はじまった", "M105.Q5.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cụm từ cố định (Bài 6):</strong> 道に まよう (Lạc đường) ➔ Quá khứ: <strong>まよった</strong>."
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
                                "prompt": v("<u>日本語が じょうずに なりたいんですが、どうやって 勉強したら いいですか。</u>", "M105.Q6.p"),
                                "promptVi": "Tôi muốn giỏi tiếng Nhật thì phải học thế nào? (Câu 11 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("日本語が うまく なる ほうほうを おしえて ください。", "M105.Q6.o0"),
                                    v("日本語を ぜんぜん 勉強したく ありません。", "M105.Q6.o1"),
                                    v("日本語は とても かんたんだと 思います。", "M105.Q6.o2") if False else v("日本語は とても かんたんです。", "M105.Q6.o2"),
                                    v("日本語の 先生に なりたくないです。", "M105.Q6.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Đồng nghĩa giao tiếp: じょうずに なりたい = うまく なる (muốn trở nên giỏi giang, thành thạo).</strong>"
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": v("<u>ちゅうごく語の 勉強は むずかしいですが、かんじは おもしろいです。</u>", "M105.Q7.p"),
                                "promptVi": "Việc học tiếng Trung khó nhưng chữ Hán thú vị. (Câu 15 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ちゅうごく語は たいへんですが、かんじを まなぶ のは たのしいです。", "M105.Q7.o0"),
                                    v("ちゅうごく語は かんじも ぜんぶ つまらないです。", "M105.Q7.o1"),
                                    v("ちゅうごく語は えいごと まったく 同じです。", "M105.Q7.o2") if False else v("ちゅうごく語は えいごと まったく おなじです。", "M105.Q7.o2"),
                                    v("ちゅうごく語は だれでも すぐに わかります。", "M105.Q7.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ đồng nghĩa: むずかしい = たいへん, おもしろい = たのしい.</strong>"
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": v("<u>フランス語は はつおんが かんたんでは ありません。</u>", "M105.Q8.p"),
                                "promptVi": "Tiếng Pháp thì phát âm không đơn giản. (Câu 36 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("フランス語の はつおんは 少し むずかしいです。", "M105.Q8.o0"),
                                    v("フランス語の はつおんは とても かんたんです。", "M105.Q8.o1"),
                                    v("フランス語には はつおんが ありません。", "M105.Q8.o2"),
                                    v("フランス語を はなす 人は いません。", "M105.Q8.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tương đương phủ định: かんたんではありません (không đơn giản) = 少しむずかしい (hơi khó).</strong>"
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": v("<u>ぶんしょうを 読む のが にがてです。</u>", "M105.Q9.p"),
                                "promptVi": "Tôi kém việc đọc câu văn. (Câu 39 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("長い ぶんしょうを 読む ことが あまり とくいでは ありません。", "M105.Q9.o0") if False else v("ぶんしょうを 読む ことが あまり とくいでは ありません。", "M105.Q9.o0"),
                                    v("ぶんしょうを 読む ことが とても じょうずです。", "M105.Q9.o1"),
                                    v("本を 読む ことが いちばん 好きです。", "M105.Q9.o2"),
                                    v("まい日 たくさん ぶんしょうを 書きます。", "M105.Q9.o3") if False else v("まい日 たくさん ぶんしょうを かきます。", "M105.Q9.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ trái nghĩa tương đương: にがて (kém/ngại) = あまり とくいではない (không giỏi lắm).</strong>"
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": v("<u>日本の まんがを たくさん あつめて います。</u>", "M105.Q10.p"),
                                "promptVi": "Tôi đang sưu tầm nhiều truyện tranh của Nhật Bản. (Câu 40 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("へやに 日本の まんがが たくさん あります。", "M105.Q10.o0"),
                                    v("日本の まんがを ぜんぜん もって いません。", "M105.Q10.o1"),
                                    v("まんがを 一さつも 読んだ ことが ありません。", "M105.Q10.o2"),
                                    v("日本の まんがが きらいです。", "M105.Q10.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Ý nghĩa thực tế: Sưu tầm nhiều truyện tranh = Trong phòng có rất nhiều truyện tranh.</strong>"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Kiểm tra nhận diện chữ Hán chủ đề học tập, trường học, ngôn ngữ (Bài 1 - 10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn âm đọc chính xác của chữ Hán trong câu:",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": v("まい日、学校で 【勉強】します。", "M105.Q11.p"),
                                "promptVi": "Mỗi ngày tôi đều học ở trường.",
                                "options": [
                                    v("べんきょう", "M105.Q11.o0"),
                                    v("ぶんきょう", "M105.Q11.o1"),
                                    v("べんきょうう", "M105.Q11.o2"),
                                    v("めんきょう", "M105.Q11.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 勉強 (MIỄN CƯỜNG - Bài 9):</strong> Đọc là <strong>べんきょう</strong> (học tập)."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": v("あの 人は わたしの 【先生】です。", "M105.Q12.p"),
                                "promptVi": "Người đó là giáo viên của tôi.",
                                "options": [
                                    v("せんせい", "M105.Q12.o0"),
                                    v("がくせい", "M105.Q12.o1"),
                                    v("ともだち", "M105.Q12.o2"),
                                    v("りゅうがくせい", "M105.Q12.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 先生 (TIÊN SINH - Bài 9):</strong> Đọc là <strong>せんせい</strong> (thầy cô giáo)."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": v("休みの 日に 本を 【読】みます。", "M105.Q13.p") if False else v("やすみの 日に 本を 【読】みます。", "M105.Q13.p"),
                                "promptVi": "Vào ngày nghỉ tôi đọc sách.",
                                "options": [
                                    v("よ", "M105.Q13.o0"),
                                    v("の", "M105.Q13.o1"),
                                    v("み", "M105.Q13.o2"),
                                    v("か", "M105.Q13.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 読 (ĐỘC - Bài 2):</strong> Âm Kun là <strong>よ (む)</strong>. 読みます đọc là <strong>よみます</strong>."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": v("わたしは まんがが 【好】きです。", "M105.Q14.p"),
                                "promptVi": "Tôi thích truyện tranh.",
                                "options": [
                                    v("す", "M105.Q14.o0"),
                                    v("たの", "M105.Q14.o1"),
                                    v("おもしろ", "M105.Q14.o2"),
                                    v("やす", "M105.Q14.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 好 (HẢO - Bài 2):</strong> Đọc là <strong>す (き)</strong> (thích)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": v("これは 【何】ですか。", "M105.Q15.p"),
                                "promptVi": "Cái này là cái gì thế?",
                                "options": [
                                    v("なん", "M105.Q15.o0"),
                                    v("どこ", "M105.Q15.o1"),
                                    v("だれ", "M105.Q15.o2"),
                                    v("いつ", "M105.Q15.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 何 (HÀ - Bài 2):</strong> Đọc là <strong>なん / なに</strong> (cái gì)."
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
                                "prompt": v("いろいろな 【がいこくご】を 勉強したいです。", "M105.Q16.p"),
                                "promptVi": "Tôi muốn học nhiều ngoại ngữ khác nhau.",
                                "options": [
                                    v("外国語", "M105.Q16.o0"),
                                    v("日本語", "M105.Q16.o1"),
                                    v("中国語", "M105.Q16.o2") if False else v("文化語", "M105.Q16.o2"),
                                    v("旅行語", "M105.Q16.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 外国語 (NGOẠI QUỐC NGỮ - Bài 2):</strong> Đọc là <strong>がいこくご</strong>."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": v("学校に 【りゅうがくせい】が たくさん います。", "M105.Q17.p"),
                                "promptVi": "Ở trường học có rất nhiều lưu học sinh.",
                                "options": [
                                    v("留学生", "M105.Q17.o0"),
                                    v("先生", "M105.Q17.o1"),
                                    v("友達", "M105.Q17.o2"),
                                    v("外国人", "M105.Q17.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 留学生 (LƯU HỌC SINH - Bài 9, 10):</strong> Đọc là <strong>りゅうがくせい</strong>."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": v("この 【ほん】は とても おもしろいです。", "M105.Q18.p"),
                                "promptVi": "Quyển sách này rất thú vị.",
                                "options": [
                                    v("本", "M105.Q18.o0"),
                                    v("国", "M105.Q18.o1"),
                                    v("語", "M105.Q18.o2"),
                                    v("何", "M105.Q18.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 本 (BỔN/BẢN - Bài 2):</strong> Đọc là <strong>ほん</strong> (quyển sách)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": v("【いま】、日本語の じゅぎょう中 (ちゅう) です。", "M105.Q19.p") if False else v("【いま】、日本語を 勉強して います。", "M105.Q19.p"),
                                "promptVi": "Bây giờ tôi đang học tiếng Nhật.",
                                "options": [
                                    v("今", "M105.Q19.o0"),
                                    v("朝", "M105.Q19.o1"),
                                    v("昼", "M105.Q19.o2"),
                                    v("夜", "M105.Q19.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 今 (KIM - Bài 3):</strong> Đọc là <strong>いま</strong> (bây giờ)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": v("あした、どこへ 【い】きますか。", "M105.Q20.p"),
                                "promptVi": "Ngày mai bạn đi đâu thế?",
                                "options": [
                                    v("行", "M105.Q20.o0"),
                                    v("出", "M105.Q20.o1"),
                                    v("待", "M105.Q20.o2"),
                                    v("止", "M105.Q20.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ 行 (HÀNH - Bài 10):</strong> Đọc là <strong>い (きます)</strong> (đi)."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Kiểm tra cấu trúc lời khuyên, danh từ hóa V-ること, liên từ nối và trợ từ so sánh.",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn phương án đúng nhất điền vào chỗ trống",
                        "groupInstruction": "Chọn từ/thể ngữ pháp chính xác nhất điền vào chỗ trống trong ngoặc (   ):",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": v("いつも 日本語を (   ) ください。そして、ことばを たくさん おぼえて ください。", "M105.Q21.p"),
                                "promptVi": "Hãy thường xuyên nói tiếng Nhật. Và hãy nhớ nhiều từ vựng nhé. (Câu 11 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("はなして", "M105.Q21.o0"),
                                    v("はなす", "M105.Q21.o1"),
                                    v("はなした", "M105.Q21.o2"),
                                    v("はなし", "M105.Q21.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc lời khuyên/yêu cầu lịch sự: V-てください:</strong> はなす (Nhóm 1) ➔ Thể て là <strong>はなして</strong>."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": v("むずかしいですが、かんじは おもしろいです。えいご (   ) ちがいますから。", "M105.Q22.p"),
                                "promptVi": "Khó nhưng chữ Hán thú vị. Vì khác với tiếng Anh. (Câu 15 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("と", "M105.Q22.o0"),
                                    v("に", "M105.Q22.o1"),
                                    v("を", "M105.Q22.o2"),
                                    v("で", "M105.Q22.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc so sánh khác biệt: A と ちがう:</strong> Khác với tiếng Anh ➔ <strong>えいごと ちがいます</strong>."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": v("日本語は かんじを かく (   ) が おもしろいです。", "M105.Q23.p"),
                                "promptVi": "Tiếng Nhật thì việc viết chữ Hán thú vị. (Câu 38 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("こと", "M105.Q23.o0"),
                                    v("もの", "M105.Q23.o1"),
                                    v("ひと", "M105.Q23.o2"),
                                    v("ところ", "M105.Q23.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Danh từ hóa động từ: V-る ＋ こと (việc làm gì):</strong> かく こと (việc viết)."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": v("私の しゅみは まんがを (   ) ことです。", "M105.Q24.p"),
                                "promptVi": "Sở thích của tôi là đọc truyện tranh. (Câu 40 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("読む", "M105.Q24.o0"),
                                    v("読んだ", "M105.Q24.o1"),
                                    v("読んで", "M105.Q24.o2"),
                                    v("読み", "M105.Q24.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc sở thích: Nの しゅみは [Động từ thể từ điển (V-る)] ことです:</strong> まんがを <strong>読む</strong> ことです."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": v("道に まよった (   )、テストが できませんでした。", "M105.Q25.p"),
                                "promptVi": "Vì lạc đường nên tôi đã không thể làm được bài kiểm tra. (Câu 34 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("ので", "M105.Q25.o0"),
                                    v("のに", "M105.Q25.o1"),
                                    v("たら", "M105.Q25.o2"),
                                    v("ても", "M105.Q25.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Liên từ chỉ lý do nguyên nhân khách quan: V-thể thông thường + ので:</strong> まよったので (vì bị lạc đường)."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": v("らいねん、日本へ 行って (   ) です。", "M105.Q26.p"),
                                "promptVi": "Năm sau tôi rất muốn đi thử đến Nhật Bản. (Câu 26 trong bộ 40 câu ôn tập)",
                                "options": [
                                    v("みたい", "M105.Q26.o0"),
                                    v("ほしい", "M105.Q26.o1"),
                                    v("たくない", "M105.Q26.o2"),
                                    v("にくい", "M105.Q26.o3")
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc làm thử việc gì: V-て みたい (muốn thử làm gì):</strong> 行ってみたいです (muốn đi thử)."
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
                                "prompt": v("いつも 日本語を [  ] [  ] [ ★ ] [  ] おぼえて ください。", "M105.Q27.p"),
                                "promptVi": "Hãy thường xuyên nói tiếng Nhật. Và hãy nhớ nhiều từ vựng. (Câu 11)",
                                "options": [
                                    v("はなして", "M105.Q27.o0"),
                                    v("ください。そして、", "M105.Q27.o1"),
                                    v("ことばを", "M105.Q27.o2"),
                                    v("たくさん", "M105.Q27.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> いつも 日本語を [はなして] [ください。そして、] [★ ことばを] [たくさん] おぼえて ください。<br>Vị trí ngôi sao là <strong>ことばを</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "prompt": v("かんじは [  ] [  ] [ ★ ] [  ] ちがいますから。", "M105.Q28.p"),
                                "promptVi": "Chữ Hán thú vị vì khác với tiếng Anh. (Câu 15)",
                                "options": [
                                    v("おもしろいです。", "M105.Q28.o0"),
                                    v("えいご", "M105.Q28.o1"),
                                    v("と", "M105.Q28.o2"),
                                    v("ぜんぜん", "M105.Q28.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> かんじは [おもしろいです。] [えいご] [★ と] [ぜんぜん] ちがいますから。<br>Vị trí ngôi sao là <strong>と</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "prompt": v("日本語は [  ] [  ] [ ★ ] [  ] おもしろいです。", "M105.Q29.p"),
                                "promptVi": "Tiếng Nhật thì việc viết chữ Hán rất thú vị. (Câu 38)",
                                "options": [
                                    v("かんじを", "M105.Q29.o0"),
                                    v("かく", "M105.Q29.o1"),
                                    v("ことが", "M105.Q29.o2"),
                                    v("とても", "M105.Q29.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> 日本語は [かんじを] [かく] [★ ことが] [とても] おもしろいです。<br>Vị trí ngôi sao là <strong>ことが</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "prompt": v("道に [  ] [  ] [ ★ ] [  ] できませんでした。", "M105.Q30.p"),
                                "promptVi": "Vì lạc đường nên tôi đã không thể làm bài kiểm tra tiếng Nhật. (Câu 34)",
                                "options": [
                                    v("まよったので、", "M105.Q30.o0"),
                                    v("日本語の", "M105.Q30.o1"),
                                    v("テストが", "M105.Q30.o2"),
                                    v("ぜんぜん", "M105.Q30.o3")
                                ],
                                "correct": 2,
                                "explain": "💡 <strong>Trật tự câu:</strong> 道に [まよったので、] [日本語の] [★ テストが] [ぜんぜん] できませんでした。<br>Vị trí ngôi sao là <strong>テストが</strong>."
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
                                "prompt": "Tiếng Nhật thì việc viết chữ Hán thú vị.",
                                "promptVi": "Câu 38 trong bộ 40 câu ôn tập",
                                "reference": v("日本語は かんじを かく ことが おもしろいです。", "M105.Q31.ref"),
                                "acceptAnswers": [
                                    v("日本語は かんじを かく ことが おもしろいです。", "M105.Q31.ans0"),
                                    v("日本語は かんじを かく のが おもしろいです。", "M105.Q31.ans1"),
                                    v("日本語は かんじを かく ことが とても おもしろいです。", "M105.Q31.ans2")
                                ],
                                "hints": ["日本語は", "かんじを かく ことが / のが", "おもしろいです"]
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "prompt": "Vì lạc đường, nên tôi đã không thể làm được bài kiểm tra tiếng Nhật.",
                                "promptVi": "Câu 34 trong bộ 40 câu ôn tập",
                                "reference": v("道に まよったので、日本語の テストが できませんでした。", "M105.Q32.ref"),
                                "acceptAnswers": [
                                    v("道に まよったので、日本語の テストが できませんでした。", "M105.Q32.ans0"),
                                    v("道に まよいましたから、日本語の テストが できませんでした。", "M105.Q32.ans1"),
                                    v("道に まよったから、日本語の テストが できませんでした。", "M105.Q32.ans2")
                                ],
                                "hints": ["道に まよったので / まよいましたから", "日本語の テストが", "できませんでした"]
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc bài chia sẻ về việc học ngoại ngữ và chọn đáp án chính xác nhất (Câu 33-34).",
                "badge": "10 Điểm",
                "passage": v("わたしは 学校で 外国語を 勉強する ことが 大好きです。\nいままで えいごと フランス語を 勉強しました。\nフランス語は はつおんが 少し むずかしいですが、とても きれいな ことばです。\nいまは、学校で 日本語を 勉強して います。\n日本語は かんじを かく ことが とても おもしろいです。\nでも、ことばが 多くて、ぶんしょうを 読む のが 少し にがてですから、まい朝 三十ぷん 読む れんしゅうを して います。\nしょうらい、日本へ 留学生として 行って、たくさんの 友達を つくりたいです。", "M105.passage") if False else v("わたしは 学校で 外国語を 勉強する ことが 好きです。\nいままで えいごと フランス語を 勉強しました。\nフランス語は はつおんが 少し むずかしいですが、とても きれいな ことばです。\nいまは、学校で 日本語を 勉強して います。\n日本語は かんじを かく ことが とても おもしろいです。\nでも、ことばが 多くて、ぶんしょうを 読む のが 少し にがてですから、まい朝 三十ぷん 読む れんしゅうを して います。\nしょうらい、日本へ 留学生として 行って、たくさんの 友達を つくりたいです。", "M105.passage"),
                "passageVi": "Tôi rất thích việc học ngoại ngữ ở trường học.\nCho đến nay tôi đã học tiếng Anh và tiếng Pháp.\nTiếng Pháp thì phát âm hơi khó một chút nhưng là một ngôn ngữ rất đẹp.\nHiện tại, tôi đang học tiếng Nhật ở trường.\nTiếng Nhật thì việc viết chữ Hán rất thú vị.\nTuy nhiên từ vựng nhiều và việc đọc câu văn tôi hơi kém một chút, nên mỗi sáng tôi luyện đọc 30 phút.\nTrong tương lai, tôi muốn sang Nhật Bản với tư cách là lưu học sinh và kết thật nhiều bạn bè.",
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": v("この 人は なぜ まい朝 三十ぷん 読む れんしゅうを して いますか。", "M105.Q33.p"),
                        "promptVi": "Tại sao mỗi sáng người này lại luyện đọc 30 phút?",
                        "options": [
                            v("ぶんしょうを 読む のが 少し にがてですから。", "M105.Q33.o0"),
                            v("かんじを かく のが きらいですから。", "M105.Q33.o1"),
                            v("フランス語を はなしたいですから。", "M105.Q33.o2"),
                            v("テストが ぜんぜん ありませんから。", "M105.Q33.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「ぶんしょうを 読む のが 少し にがてですから、まい朝 三十ぷん 読む れんしゅうを して います」 ➔ Vì việc đọc văn bản hơi kém một chút."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": v("この 人の しょうらいの ゆめは 何ですか。", "M105.Q34.p"),
                        "promptVi": "Ước mơ trong tương lai của người này là gì?",
                        "options": [
                            v("日本へ 留学生として 行く こと。", "M105.Q34.o0"),
                            v("フランスで 先生に なる こと。", "M105.Q34.o1"),
                            v("えいごの 本を 書く こと。", "M105.Q34.o2") if False else v("えいごの 本を かく こと。", "M105.Q34.o2"),
                            v("学校を やめる こと。", "M105.Q34.o3")
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「しょうらい、日本へ 留学生として 行って、たくさんの 友達を つくりたいです」 ➔ Đi du học Nhật Bản."
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
                        "prompt": "あなたにとって、日本語の 勉強で 何が おもしろいですか。何が むずかしいですか。",
                        "promptVi": "Đối với bạn, trong việc học tiếng Nhật điều gì thú vị và điều gì khó khăn? Hãy chia sẻ ngắn gọn.",
                        "minWords": 30,
                        "placeholder": "Gõ câu trả lời tiếng Nhật tại đây... Ví dụ: 日本語は かんじを かく ことが おもしろいです...",
                        "hints": [
                            "Điều thú vị: かんじを かく ことが おもしろい / はなす のが たのしい",
                            "Điều khó khăn: ことばが 多い / ぶんしょうを 読む のが にがて",
                            "Cảm xúc: これからも いっしょうけんめい 勉強したいです"
                        ],
                        "modelAnswer": v("日本語は かんじを かく ことが とても おもしろいです。でも、ことばが 多くて、ぶんしょうを 読む のが 少し にがてです。これからも いっしょうけんめい がんばります。", "M105.Q35.ans"),
                        "modelVi": "Tiếng Nhật thì việc viết chữ Hán rất thú vị. Nhưng từ vựng nhiều và việc đọc văn bản tôi hơi kém một chút. Sau này tôi sẽ cố gắng hết mình.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Sử dụng đúng cấu trúc danh từ hóa (V-ること / V-るの), nêu bật cả điểm thú vị và điểm khó khăn."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "あなたの しょうらいの ゆめや、これから 勉強したい 外国語について かいて ください。（りゆう、もくひょうなど、五十じ いじょう）",
                        "promptVi": "Hãy viết đoạn văn chia sẻ về ước mơ tương lai hoặc ngoại ngữ bạn muốn học tiếp theo (lý do, mục tiêu học tập... tối thiểu 50 chữ/ký tự).",
                        "minWords": 50,
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは しょうらい、日本へ 留学生として 行きたいです...",
                        "hints": [
                            "Ước mơ: わたしは しょうらい、日本へ 留学生として 行きたいです",
                            "Ngoại ngữ muốn học: 日本語や えいごを もっと じょうずに はなしたいです",
                            "Kế hoạch rèn luyện: まい日、三十ぷん 日本語を 勉強して、日本の 友達を つくります",
                            "Độ dài: Tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": v("わたしは しょうらい、日本へ 留学生として 行きたいです。日本の 文化や 音楽が 好きですから、学校で もっと 日本語を 勉強します。そして、まい日 三十ぷん 日本語を はなす れんしゅうを して、日本の 友達を たくさん つくりたいです。これからも いっしょうけんめい がんばります。", "M105.Q36.ans"),
                        "modelVi": "Trong tương lai, tôi muốn đến Nhật Bản với tư cách là một lưu học sinh. Vì tôi thích văn hóa và âm nhạc Nhật Bản nên tôi sẽ học tiếng Nhật nhiều hơn ở trường. Mỗi ngày tôi sẽ luyện nói tiếng Nhật 30 phút và kết thật nhiều bạn bè người Nhật. Sau này tôi sẽ cố gắng hết mình.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; nêu rõ ước mơ (留学生として行きたい), sử dụng đúng liên từ lý do (～から) và từ vựng Bài 1 - 10."
                    }
                ]
            }
        ]
    }

if __name__ == "__main__":
    exam = build_m105()
    print("M105 built successfully!")
    print("Code:", exam["code"])
    print("Sections:", len(exam["sections"]))
