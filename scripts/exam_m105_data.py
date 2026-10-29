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

DATA_M105 = {
    "code": "M105",
    "name": "Mã Đề M105 (Phương Pháp Học Ngoại Ngữ & Ước Mơ)",
    "tag": "🎓 Ngoại Ngữ • Kỹ Năng Nghe Nói Đọc • Ước Mơ Du Học • Chuẩn A2-1",
    "desc": "Đề chuyên sâu về phương pháp học tiếng Nhật (ことば, ぶんぽう, かんじ, まんがを 読む), so sánh độ khó các ngoại ngữ (ベトナム語, フランス語, えいご, ちゅうごく語), và mục tiêu du học.",
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
                            "prompt": "日本語は (   ) を かく ことが とても おもしろいです。",
                            "promptVi": "Tiếng Nhật thì việc viết chữ Hán rất thú vị. (Câu 38 trong bộ 40 câu ôn tập)",
                            "options": [
                                "みず",
                                "かんじ",
                                "えき",
                                "まち"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Từ vựng kỹ năng học tiếng Nhật (Bài 2):</strong> Viết chữ Hán ➔ <strong>かんじ</strong>を かく こと."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "いままで どんな (   ) を 勉強しましたか。",
                            "promptVi": "Cho đến bây giờ bạn đã học ngoại ngữ nào rồi? (Câu 12 trong bộ 40 câu ôn tập)",
                            "options": [
                                "天気",
                                "場所",
                                "時間",
                                "外国語"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ Hán ghép (Bài 2):</strong> Ngoại ngữ là <strong>外国語</strong> (がいこくご). Cả 外, 国, 語 đều học ở Bài 2."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "すみません、この (   ) の つかいかたを おしえて くださいませんか。",
                            "promptVi": "Xin lỗi, bạn có thể chỉ cho tôi cách sử dụng kim từ điển này không? (Câu 18 trong bộ 40 câu ôn tập)",
                            "options": [
                                "でんしじしょ",
                                "コーヒー",
                                "シャツ",
                                "くつ"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Từ vựng công cụ học tập (Bài 2):</strong> Kim từ điển là <strong>でんしじしょ</strong>."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "日本語は ことばが 多いです。そして、(   ) を 読む のが にがてです。",
                            "promptVi": "Tiếng Nhật thì từ vựng nhiều. Và tôi kém việc đọc câu văn. (Câu 39 trong bộ 40 câu ôn tập)",
                            "options": [
                                "みず",
                                "やま",
                                "ぶんしょう",
                                "かわ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Từ vựng đọc hiểu (Bài 2):</strong> Đọc đoạn văn, câu văn là <strong>ぶんしょう</strong>を 読む."
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "学校の としょかんで 日本語の じしょを (   )ました。",
                            "promptVi": "Tôi đã mượn cuốn từ điển tiếng Nhật ở thư viện trường. (Câu 14 trong bộ 40 câu ôn tập)",
                            "options": [
                                "かり",
                                "まち",
                                "よみ",
                                "かき"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Động từ mượn sách/từ điển (Bài 8):</strong> かりる (かりました ➔ đã mượn). Chữ 学校, 本 đều đã học."
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
                            "prompt": "日本語が <u>じょうずに なりたい</u>んですが、どうやって 勉強したら いいですか。",
                            "promptVi": "Tôi muốn giỏi tiếng Nhật thì phải học thế nào? (Câu 11 trong bộ 40 câu ôn tập)",
                            "options": [
                                "うまく なりたい",
                                "やめたい",
                                "きらいになりたい",
                                "へたになりたい"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Từ đồng nghĩa (Bài 2):</strong> じょうずに なりたい (muốn giỏi tiếng Nhật) ＝ <strong>うまく なりたい</strong> (muốn thành thạo, khéo léo). Chữ 勉強 đã học ở Bài 9."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "ちゅうごく語の 勉強は むずかしいですが、かんじは <u>おもしろい</u>です。",
                            "promptVi": "Việc học tiếng Trung khó nhưng chữ Hán thì thú vị. (Câu 15 trong bộ 40 câu ôn tập)",
                            "options": [
                                "つまらない",
                                "たいへんな",
                                "たのしい",
                                "こわい"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Tính từ khen ngợi (Bài 2):</strong> おもしろい (thú vị) ＝ <strong>たのしい</strong> (vui vẻ, hào hứng)."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "フランス語は はつおんが <u>かんたんでは ありません</u>。",
                            "promptVi": "Tiếng Pháp thì phát âm không đơn giản chút nào. (Câu 36 trong bộ 40 câu ôn tập)",
                            "options": [
                                "たのしいです",
                                "はやいです",
                                "みじかいです",
                                "むずかしいです"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Phủ định tính từ (Bài 2):</strong> かんたんでは ありません (không đơn giản) ＝ <strong>むずかしいです</strong> (khó)."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "ぶんしょうを 読む のが <u>にがてです</u>。",
                            "promptVi": "Tôi kém việc đọc câu văn. (Câu 39 trong bộ 40 câu ôn tập)",
                            "options": [
                                "とても じょうずだ",
                                "だいすきだ",
                                "あまり とくいではない",
                                "かんたんだ"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Tính từ chỉ năng lực (Bài 2):</strong> にがてです (kém, không tự tin) ＝ <strong>あまり とくいではない</strong> (không thành thạo lắm). Chữ 読 đã học ở Bài 2."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "日本の まんがを たくさん <u>あつめて います</u>。",
                            "promptVi": "Tôi đang sưu tầm nhiều truyện tranh của Nhật Bản. (Câu 40 trong bộ 40 câu ôn tập)",
                            "options": [
                                "うる こと",
                                "すてる こと",
                                "かりる こと",
                                "もつ こと"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Từ vựng sở thích (Bài 10):</strong> あつめて います (sưu tầm, tích trữ) ＝ <strong>もつ こと</strong> (sở hữu trong nhà). Chữ 日本 đã học."
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
                            "prompt": "まい日、学校で 【勉強】します。",
                            "promptVi": "Mỗi ngày tôi đều học ở trường.",
                            "options": [
                                "ぶんきょう",
                                "べんきょうう",
                                "めんきょう",
                                "べんきょう"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ 勉強 (MIỄN CƯỜNG - Bài 9):</strong> Đọc là <strong>べんきょう</strong> (học tập)."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "あの 人は わたしの 【先生】です。",
                            "promptVi": "Người đó là giáo viên của tôi.",
                            "options": [
                                "がくせい",
                                "せんせい",
                                "ともだち",
                                "りゅうがくせい"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 先生 (TIÊN SINH - Bài 9):</strong> Đọc là <strong>せんせい</strong> (thầy cô giáo)."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "やすみの 日に 本を 【読】みます。",
                            "promptVi": "Vào ngày nghỉ tôi đọc sách.",
                            "options": [
                                "の",
                                "み",
                                "よ",
                                "か"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 読 (ĐỘC - Bài 2):</strong> Âm Kun là <strong>よ (む)</strong>. 読みます đọc là <strong>よみます</strong>."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "わたしは まんがが 【好】きです。",
                            "promptVi": "Tôi thích truyện tranh.",
                            "options": [
                                "たの",
                                "おもしろ",
                                "す",
                                "やす"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 好 (HẢO - Bài 2):</strong> Đọc là <strong>す (き)</strong> (thích)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "これは 【何】ですか。",
                            "promptVi": "Cái này là cái gì thế?",
                            "options": [
                                "どこ",
                                "なん",
                                "だれ",
                                "いつ"
                            ],
                            "correct": 1,
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
                            "prompt": "いろいろな 【がいこくご】を 勉強したいです。",
                            "promptVi": "Tôi muốn học nhiều ngoại ngữ khác nhau.",
                            "options": [
                                "日本語",
                                "文化語",
                                "外国語",
                                "旅行語"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Chữ 外国語 (NGOẠI QUỐC NGỮ - Bài 2):</strong> Đọc là <strong>がいこくご</strong>."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "学校に 【りゅうがくせい】が たくさん います。",
                            "promptVi": "Ở trường học có rất nhiều lưu học sinh.",
                            "options": [
                                "先生",
                                "友達",
                                "外国人",
                                "留学生"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Chữ 留学生 (LƯU HỌC SINH - Bài 9, 10):</strong> Đọc là <strong>りゅうがくせい</strong>."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "この 【ほん】は とても おもしろいです。",
                            "promptVi": "Quyển sách này rất thú vị.",
                            "options": [
                                "本",
                                "国",
                                "語",
                                "何"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Chữ 本 (BỔN/BẢN - Bài 2):</strong> Đọc là <strong>ほん</strong> (quyển sách)."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "【いま】、日本語を 勉強して います。",
                            "promptVi": "Bây giờ tôi đang học tiếng Nhật.",
                            "options": [
                                "朝",
                                "今",
                                "昼",
                                "夜"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Chữ 今 (KIM - Bài 3):</strong> Đọc là <strong>いま</strong> (bây giờ)."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "あした、どこへ 【い】きますか。",
                            "promptVi": "Ngày mai bạn đi đâu thế?",
                            "options": [
                                "出",
                                "行",
                                "待",
                                "止"
                            ],
                            "correct": 1,
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
                            "prompt": "いつも 日本語を (   ) ください。そして、ことばを たくさん おぼえて ください。",
                            "promptVi": "Hãy thường xuyên nói tiếng Nhật. Và hãy nhớ nhiều từ vựng nhé. (Câu 11 trong bộ 40 câu ôn tập)",
                            "options": [
                                "はなして",
                                "はなす",
                                "はなします",
                                "はなし"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cấu trúc lời khuyên/yêu cầu lịch sự: V-てください:</strong> はなす (Nhóm 1) ➔ Thể て là <strong>はなして</strong>."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "むずかしいですが、かんじは おもしろいです。えいご (   ) ちがいますから。",
                            "promptVi": "Khó nhưng chữ Hán thú vị. Vì khác với tiếng Anh. (Câu 15 trong bộ 40 câu ôn tập)",
                            "options": [
                                "に",
                                "と",
                                "を",
                                "で"
                            ],
                            "correct": 1,
                            "explain": "💡 <strong>Cấu trúc so sánh khác biệt: A と ちがう:</strong> Khác với tiếng Anh ➔ <strong>えいごと ちがいます</strong>."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "日本語は かんじを かく (   ) が おもしろいです。",
                            "promptVi": "Tiếng Nhật thì việc viết chữ Hán thú vị. (Câu 38 trong bộ 40 câu ôn tập)",
                            "options": [
                                "もの",
                                "ひと",
                                "ところ",
                                "こと"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Danh từ hóa động từ: V-る ＋ こと (việc làm gì):</strong> かく こと (việc viết)."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "私の しゅみは まんがを (   ) ことです。",
                            "promptVi": "Sở thích của tôi là đọc truyện tranh. (Câu 40 trong bộ 40 câu ôn tập)",
                            "options": [
                                "読む",
                                "読みます",
                                "読んで",
                                "読み"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Cấu trúc sở thích: Nの しゅみは [Động từ thể từ điển (V-る)] ことです:</strong> まんがを <strong>読む</strong> ことです."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "ちゅうごく語は むずかしいですが、おもしろいです。えいごと ちがいます (   )。",
                            "promptVi": "Tiếng Trung khó nhưng thú vị. Vì khác với tiếng Anh. (Câu 15 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ので",
                                "のに",
                                "から",
                                "けど"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Liên từ chỉ lý do nguyên nhân (Bài 2/10): ～から:</strong> ちがいます<strong>から</strong> (Vì khác với tiếng Anh). Đúng theo Câu 15 trong bộ 40 câu ôn tập."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "らいねん、日本へ 行って (   ) です。",
                            "promptVi": "Năm sau tôi rất muốn đi thử đến Nhật Bản. (Câu 26 trong bộ 40 câu ôn tập)",
                            "options": [
                                "ほしい",
                                "たくない",
                                "にくい",
                                "みたい"
                            ],
                            "correct": 3,
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
                            "prompt": "いつも 日本語を [  ] [  ] [ ★ ] [  ] おぼえて ください。",
                            "promptVi": "Hãy thường xuyên nói tiếng Nhật. Và hãy nhớ nhiều từ vựng. (Câu 11)",
                            "options": [
                                "ことばを",
                                "たくさん",
                                "はなして",
                                "ください。そして、"
                            ],
                            "correct": 0,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] はなして ➔ [4] ください。そして、 ➔ <strong>★ [1] ことばを (Vị trí số 3)</strong> ➔ [2] たくさん<br>➔ Câu hoàn chỉnh: いつも 日本語を はなして ください。そして、ことばを たくさん おぼえて ください。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[1] ことばを</strong>."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "prompt": "かんじは [  ] [  ] [ ★ ] [  ] ちがいますから。",
                            "promptVi": "Chữ Hán thú vị vì khác với tiếng Anh. (Câu 15)",
                            "options": [
                                "ぜんぜん",
                                "えいご",
                                "おもしろいです。",
                                "と"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] おもしろいです。 ➔ [2] えいご ➔ <strong>★ [4] と (Vị trí số 3)</strong> ➔ [1] ぜんぜん<br>➔ Câu hoàn chỉnh: かんじは おもしろいです。えいごと ぜんぜん ちがいますから。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[4] と</strong>."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "prompt": "日本語は [  ] [  ] [ ★ ] [  ] おもしろいです。",
                            "promptVi": "Tiếng Nhật thì việc viết chữ Hán rất thú vị. (Câu 38)",
                            "options": [
                                "かく",
                                "とても",
                                "かんじを",
                                "ことが"
                            ],
                            "correct": 3,
                            "explain": "💡 <strong>Thứ tự sắp xếp câu:</strong><br>[3] かんじを ➔ [1] かく ➔ <strong>★ [4] ことが (Vị trí số 3)</strong> ➔ [2] とても<br>➔ Câu hoàn chỉnh: 日本語は かんじを かく ことが とても おもしろいです。<br>➔ Vị trí ngôi sao (★) là phương án <strong>[4] ことが</strong>."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "prompt": "日本語は　＿＿＿　＿＿＿　★　＿＿＿　にがてです。",
                            "promptVi": "Tiếng Nhật thì việc đọc câu văn tôi hơi kém một chút. (Câu 39 trong bộ 40 câu ôn tập)",
                            "options": [
                                "少し",
                                "ぶんしょうを",
                                "のが",
                                "読む"
                            ],
                            "correct": 2,
                            "explain": "💡 <strong>Thứ tự sắp xếp đúng:</strong><br>ぶんしょうを (1) ➔ 読む (2) ➔ <strong>のが (3 - ★)</strong> ➔ 少し (4).<br>➔ Câu hoàn chỉnh: 日本語は ぶんしょうを 読む のが 少し にがてです。",
                            "sentencePre": "日本語は",
                            "sentencePost": "にがてです。",
                            "starPos": 3,
                            "parts": [
                                {
                                    "id": 1,
                                    "text": "ぶんしょうを"
                                },
                                {
                                    "id": 2,
                                    "text": "読む"
                                },
                                {
                                    "id": 3,
                                    "text": "のが"
                                },
                                {
                                    "id": 4,
                                    "text": "少し"
                                }
                            ],
                            "fullSentence": "日本語は ぶんしょうを 読む のが 少し にがてです。"
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
                            "reference": "日本語は かんじを かく ことが おもしろいです。",
                            "acceptAnswers": [
                                "日本語は かんじを かく ことが おもしろいです。",
                                "日本語は かんじを かく のが おもしろいです。",
                                "日本語は かんじを かく ことが とても おもしろいです。",
                                "にほんごは かんじを かく ことが おもしろいです。",
                                "にほんごは かんじを かく のが おもしろいです。",
                                "日本語は かんじを かく ことが たのしいです。",
                                "日本語は かんじを かく のが たのしいです。"
                            ],
                            "hints": [
                                "日本語は",
                                "かんじを かく ことが / のが",
                                "おもしろいです"
                            ]
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "prompt": "Vì lạc đường, nên tôi đã không thể làm được bài kiểm tra tiếng Nhật.",
                            "promptVi": "Câu 34 trong bộ 40 câu ôn tập",
                            "reference": "道に まよったので、日本語の テストが できませんでした。",
                            "acceptAnswers": [
                                "道に まよったので、日本語の テストが できませんでした。",
                                "道に まよいましたから、日本語の テストが できませんでした。",
                                "道に まよったから、日本語の テストが できませんでした。",
                                "みちに まよったので、にほんごの てすとが できませんでした。",
                                "みちに まよいましたから、にほんごの てすとが できませんでした。",
                                "道に まよって、日本語の テストが できませんでした。"
                            ],
                            "hints": [
                                "道に まよったので / まよいましたから",
                                "日本語の テストが",
                                "できませんでした"
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
            "partDesc": "Đọc bài chia sẻ về việc học ngoại ngữ và chọn đáp án chính xác nhất (Câu 33-34).",
            "badge": "10 Điểm",
            "passage": "わたしは 学校で 外国語を 勉強する ことが 好きです。\nいままで えいごと フランス語を 勉強しました。\nフランス語は はつおんが 少し むずかしいですが、とても きれいな ことばです。\nいまは、学校で 日本語を 勉強して います。\n日本語は かんじを かく ことが とても おもしろいです。\nでも、ことばが 多くて、ぶんしょうを 読む のが 少し にがてですから、まい朝 三十ぷん 読む れんしゅうを して います。\nしょうらい、日本へ 留学生として 行って、たくさんの 友達を つくりたいです。",
            "passageVi": "Tôi rất thích việc học ngoại ngữ ở trường học.\nCho đến nay tôi đã học tiếng Anh và tiếng Pháp.\nTiếng Pháp thì phát âm hơi khó một chút nhưng là một ngôn ngữ rất đẹp.\nHiện tại, tôi đang học tiếng Nhật ở trường.\nTiếng Nhật thì việc viết chữ Hán rất thú vị.\nTuy nhiên từ vựng nhiều và việc đọc câu văn tôi hơi kém một chút, nên mỗi sáng tôi luyện đọc 30 phút.\nTrong tương lai, tôi muốn sang Nhật Bản với tư cách là lưu học sinh và kết thật nhiều bạn bè.",
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "この 人は なぜ まい朝 三十ぷん 読む れんしゅうを して いますか。",
                    "promptVi": "Tại sao mỗi sáng người này lại luyện đọc 30 phút?",
                    "options": [
                        "かんじを かく のが きらいですから。",
                        "ぶんしょうを 読む のが 少し にがてですから。",
                        "フランス語を はなしたいですから。",
                        "テストが ぜんぜん ありませんから。"
                    ],
                    "correct": 1,
                    "explain": "💡 <strong>Thông tin trong bài đọc:</strong> 「ぶんしょうを 読む のが 少し にがてですから、まい朝 三十ぷん 読む れんしゅうを して います」 ➔ Vì việc đọc văn bản hơi kém một chút."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "この 人の しょうらいの ゆめは 何ですか。",
                    "promptVi": "Ước mơ trong tương lai của người này là gì?",
                    "options": [
                        "日本へ 留学生として 行く こと。",
                        "フランスで 先生に なる こと。",
                        "えいごの 本を かく こと。",
                        "学校を やめる こと。"
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
                    "modelAnswer": "日本語は かんじを かく ことが とても おもしろいです。でも、ことばが 多くて、ぶんしょうを 読む のが 少し にがてです。これからも いっしょうけんめい がんばります。",
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
                    "modelAnswer": "わたしは しょうらい、日本へ 留学生として 行きたいです。日本の 文化や 音楽が 好きですから、学校で もっと 日本語を 勉強します。そして、まい日 三十ぷん 日本語を はなす れんしゅうを して、日本の 友達を たくさん つくりたいです。これからも いっしょうけんめい がんばります。",
                    "modelVi": "Trong tương lai, tôi muốn đến Nhật Bản với tư cách là một lưu học sinh. Vì tôi thích văn hóa và âm nhạc Nhật Bản nên tôi sẽ học tiếng Nhật nhiều hơn ở trường. Mỗi ngày tôi sẽ luyện nói tiếng Nhật 30 phút và kết thật nhiều bạn bè người Nhật. Sau này tôi sẽ cố gắng hết mình.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; nêu rõ ước mơ (留学生として行きたい), sử dụng đúng liên từ lý do (～から) và từ vựng Bài 1 - 10."
                }
            ]
        }
    ]
}

def build_m105():
    return DATA_M105
