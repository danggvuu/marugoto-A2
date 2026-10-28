#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full 5 Midterm Exams Suite for tests/De_Thi_Midterm_A2_1.html
Gồm 5 mã đề thi thử giữa kỳ Midterm hoàn chỉnh:
- Mã Đề M101: 📘 Đề Khảo Sát Tổng Hợp Toàn Diện (Bài 1 - 8)
- Mã Đề M102: ⭐ Đề Trọng Tâm Chuẩn Bảng Lớp (Bài 5 - 8)
- Mã Đề M103: ⛩️ Đề Thực Chiến Đời Sống & Du Lịch (Bài 1 - 8)
- Mã Đề M104: 🍱 Đề Đột Phá Giao Tiếp & Ẩm Thực (Bài 1 - 8)
- Mã Đề M105: 🎯 Đề Tuyển Chọn Chuẩn Đề Thầy Cô (Bài 1 - 8)
"""

import sys
sys.path.append('scripts')
from build_midterm_exam import EXAMS_DATA as BASE_EXAMS

M103 = {
    "code": "M103",
    "name": "Mã Đề M103 (Đề Thực Chiến Đời Sống & Du Lịch)",
    "tag": "⛩️ Thực Chiến Bài 1 - 8 • Đời Sống & Du Lịch",
    "desc": "Bám sát các tình huống thực tế tại Nhật: hỏi đường, nhà ga, mua sắm ở bách hóa, sinh hoạt gia đình và lễ hội hoa anh đào.",
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
                            "prompt": "この スープは (   ) ですから、砂糖（さとう）を 入れないで ください。",
                            "promptVi": "Món súp này ngọt rồi nên xin đừng cho thêm đường.",
                            "options": ["あまい", "からい", "すっぱい", "しょっぱい"],
                            "correct": 0,
                            "explain": "あまい (ngọt) nên không cần cho thêm đường (砂糖を 入れないで ください). Từ vựng mùi vị Bài 6."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "あしたは 友だちと デパートで (   ) を します。",
                            "promptVi": "Ngày mai tôi sẽ đi mua sắm ở trung tâm thương mại cùng bạn.",
                            "options": ["かいもの", "さんぽ", "りょこう", "しょくじ"],
                            "correct": 0,
                            "explain": "デパート (trung tâm thương mại) đi với 買い物を します (mua sắm). Bài 7-8."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "改札口を 出て、(   ) へ 行くと、タクシー乗り場が あります。",
                            "promptVi": "Ra khỏi cửa soát vé, rẽ sang bên trái thì sẽ có điểm đón taxi.",
                            "options": ["ひだり", "うえ", "なか", "うしろ"],
                            "correct": 0,
                            "explain": "左 (ひだり - bên trái). Mẫu câu chỉ đường nhà ga Bài 5."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "兄は ITの 会社で (   ) を して います。",
                            "promptVi": "Anh trai tôi đang làm kỹ sư tại công ty công nghệ thông tin.",
                            "options": ["エンジニア", "いしゃ", "かんごし", "きょうし"],
                            "correct": 0,
                            "explain": "Công ty IT đi với nghề nghiệp エンジニア (kỹ sư). Từ vựng nghề nghiệp Bài 1-2."
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "お祭りで 日本の 伝統的な (   ) を 見ました。",
                            "promptVi": "Ở lễ hội tôi đã xem điệu múa truyền thống của Nhật Bản.",
                            "options": ["おどり", "うた", "え", "しゃしん"],
                            "correct": 0,
                            "explain": "おどり (điệu múa truyền thống, điệu múa lễ hội Bon Odori). Từ vựng Bài 7."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Chọn câu hoặc từ đồng nghĩa",
                    "groupInstruction": "Chọn câu (A, B, C, D) có ý nghĩa tương đương gần nhất với câu hoặc cụm từ được gạch chân:",
                    "items": [
                        {
                            "id": 6,
                            "type": "mc",
                            "prompt": "この 靴は <span class='hl-kw'>小さすぎます</span>。",
                            "promptVi": "Đôi giày này quá nhỏ.",
                            "options": [
                                "足に 合わなくて、きついです。",
                                "とても ちょうど いいです。",
                                "大きくて、脱げやすいです。",
                                "とても 安くて、軽いです。"
                            ],
                            "correct": 0,
                            "explain": "小さすぎます (quá nhỏ) = 足に 合わなくて、きついです (không vừa chân, bị chật)."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "日曜日は <span class='hl-kw'>いつも</span> 家で 映画を 見ます。",
                            "promptVi": "Chủ nhật tôi lúc nào cũng xem phim ở nhà.",
                            "options": [
                                "だいたい 毎週、かならず 見ます。",
                                "たまに 見ることが あります。",
                                "ぜんぜん 見ません。",
                                "一度だけ 見ました。"
                            ],
                            "correct": 0,
                            "explain": "いつも (luôn luôn, lúc nào cũng) = だいたい 毎週かならず (hầu như tuần nào cũng xem)."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "あの 人は とても <span class='hl-kw'>親切です</span>。",
                            "promptVi": "Người đó rất tốt bụng, nhiệt tình.",
                            "options": [
                                "困っている 人を よく 助けて くれます。",
                                "背が とても 高くて、かっこいいです。",
                                "いつも 怒って ばかり います。",
                                "お金を たくさん 持って います。"
                            ],
                            "correct": 0,
                            "explain": "親切 (しんせつ - tốt bụng, thân thiện) = sẵn lòng giúp đỡ người gặp khó khăn."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "この 店は <span class='hl-kw'>有名です</span>。",
                            "promptVi": "Cửa hàng này nổi tiếng.",
                            "options": [
                                "たくさんの 人が この 店を 知って います。",
                                "だれも この 店を 知りません。",
                                "店が 新しくて、とても きれいです。",
                                "料理が とても まずいです。"
                            ],
                            "correct": 0,
                            "explain": "有名 (ゆうめい - nổi tiếng) = rất nhiều người biết đến (たくさんの 人が 知っています)."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "父は <span class='hl-kw'>車を 運転する</span> ことが できます。",
                            "promptVi": "Bố tôi có thể lái xe hơi.",
                            "options": [
                                "自分で 車を 走らせることが できます。",
                                "車を 直すことが できます。",
                                "車を 買うことが できません。",
                                "車を 洗うことが 好きです。"
                            ],
                            "correct": 0,
                            "explain": "運転する (うんてんする - lái xe) = tự mình điều khiển xe chạy."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec2_kanji",
            "partNumber": "II",
            "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
            "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán ra Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20).",
            "badge": "20 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Kanji ➔ Hiragana (Chọn cách đọc đúng)",
                    "groupInstruction": "Chọn cách đọc Hiragana đúng cho chữ Hán gạch chân:",
                    "items": [
                        {
                            "id": 11,
                            "type": "mc",
                            "prompt": "あした <span class='hl-kw'>友達</span>と 映画を 見ます。",
                            "promptVi": "Ngày mai tôi xem phim cùng bạn bè.",
                            "options": ["ともだち", "こども", "かぞく", "きょうだい"],
                            "correct": 0,
                            "explain": "「友達」 đọc là ともだち (Bạn bè)."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "川の そばを <span class='hl-kw'>歩いて</span> 行きましょう。",
                            "promptVi": "Chúng ta hãy đi bộ dọc bờ sông nhé.",
                            "options": ["あるいて", "はしって", "およいで", "のって"],
                            "correct": 0,
                            "explain": "「歩いて」 đọc là あるいて (Đi bộ - thể Te của 歩きます)."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "この <span class='hl-kw'>花</span>は とても きれいです。",
                            "promptVi": "Bông hoa này rất đẹp.",
                            "options": ["はな", "とり", "き", "くさ"],
                            "correct": 0,
                            "explain": "「花」 đọc là はな (Bông hoa)."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "図書館で 本を <span class='hl-kw'>借りました</span>。",
                            "promptVi": "Tôi đã mượn sách ở thư viện.",
                            "options": ["かりました", "かしました", "かいました", "よみました"],
                            "correct": 0,
                            "explain": "「借りました」 đọc là かりました (Đã mượn)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "スーパーの 前で <span class='hl-kw'>待って</span> ください。",
                            "promptVi": "Xin hãy chờ ở trước siêu thị.",
                            "options": ["まって", "もって", "たって", "すわって"],
                            "correct": 0,
                            "explain": "「待って」 đọc là まって (Chờ đợi - thể Te của 待ちます)."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Hiragana ➔ Kanji (Chọn chữ Hán đúng)",
                    "groupInstruction": "Chọn chữ Hán đúng cho từ Hiragana gạch chân:",
                    "items": [
                        {
                            "id": 16,
                            "type": "mc",
                            "prompt": "朝ごはんを <span class='hl-kw'>たべました</span>。",
                            "promptVi": "Tôi đã ăn bữa sáng.",
                            "options": ["食べました", "飲みました", "作りました", "買いました"],
                            "correct": 0,
                            "explain": "たべました là chữ Hán「食」➔ 食べました."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "日本語を <span class='hl-kw'>べんきょう</span> します。",
                            "promptVi": "Tôi học tiếng Nhật.",
                            "options": ["勉強", "練習", "案内", "見学"],
                            "correct": 0,
                            "explain": "べんきょう là chữ Hán「勉強」."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "これは わたしの <span class='hl-kw'>いえ</span> です。",
                            "promptVi": "Đây là nhà của tôi.",
                            "options": ["家", "町", "部屋", "庭"],
                            "correct": 0,
                            "explain": "いえ là chữ Hán「家」."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "あの <span class='hl-kw'>ひと</span>は だれですか。",
                            "promptVi": "Người đằng kia là ai thế?",
                            "options": ["人", "大", "入", "子"],
                            "correct": 0,
                            "explain": "ひと là chữ Hán「人」."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "コンビニで ジュースを <span class='hl-kw'>かいました</span>。",
                            "promptVi": "Tôi đã mua nước trái cây ở cửa hàng tiện lợi.",
                            "options": ["買いました", "売りました", "借りました", "返しました"],
                            "correct": 0,
                            "explain": "かいました (mua) là chữ Hán「買」➔ 買いました."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec3_grammar",
            "partNumber": "III",
            "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
            "partDesc": "Gồm 3 dạng bài: Điền khuyết (21-26), Hái sao ☆ (27-30), Dịch câu (31-32).",
            "badge": "30 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Điền vào chỗ trống trong ngoặc (   )",
                    "groupInstruction": "Chọn trợ từ hoặc dạng chia ngữ pháp đúng nhất điền vào (   ):",
                    "items": [
                        {
                            "id": 21,
                            "type": "mc",
                            "prompt": "わたしは 日本語の 新聞を 読む (   ) が できません。",
                            "promptVi": "Tôi không thể đọc báo tiếng Nhật.",
                            "options": ["こと", "の", "もの", "とき"],
                            "correct": 0,
                            "explain": "Mẫu câu V-ru + ことが できます/できません (Nói về khả năng)."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "会社へ 行く (   ) に、朝ごはんを 食べます。",
                            "promptVi": "Trước khi đi làm, tôi ăn bữa sáng.",
                            "options": ["まえ", "あと", "とき", "あいだ"],
                            "correct": 0,
                            "explain": "V-ru + まえに (Trước khi làm hành động V)."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "荷物を 持ちましょうか。…ありがとうございます、(   ) ください。",
                            "promptVi": "Để tôi xách hành lý giúp bạn nhé? …Cảm ơn bạn, xin hãy giúp tôi.",
                            "options": ["おねがいして", "おねがいします", "手伝って", "もって"],
                            "correct": 2,
                            "explain": "手伝って ください (てつだってください - Xin hãy giúp tôi một tay)."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "日曜日は 部屋を 掃除 (   )、洗濯を したり しました。",
                            "promptVi": "Chủ nhật tôi vừa dọn phòng, vừa giặt đồ...",
                            "options": ["したり", "して", "した", "する"],
                            "correct": 0,
                            "explain": "Mẫu câu liệt kê hành động tiêu biểu: ～たり、～たり します."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "すみません、この 部屋に 入って (   ) いいですか。",
                            "promptVi": "Xin lỗi, tôi bước vào phòng này có được không?",
                            "options": ["も", "は", "が", "を"],
                            "correct": 0,
                            "explain": "V-te + も いいですか (Mẫu câu xin phép lịch sự)."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "バスが 来ませんでした (   )、歩いて 行きました。",
                            "promptVi": "Vì xe buýt không tới nên tôi đã đi bộ.",
                            "options": ["から", "でも", "のに", "より"],
                            "correct": 0,
                            "explain": "Mệnh đề nguyên nhân + から (vì... nên...)."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: ☆ Hái sao (Sắp xếp cụm từ vào đúng vị trí)",
                    "groupInstruction": "Sắp xếp 4 cụm từ [1, 2, 3, 4] vào 4 vị trí trống và chọn số tương ứng tại vị trí ngôi sao ★:",
                    "items": [
                        {
                            "id": 27,
                            "type": "star",
                            "sentencePre": "わたしは",
                            "sentencePost": "できます。",
                            "promptVi": "Tôi có thể viết thư bằng tiếng Nhật.",
                            "parts": [
                                {"id": 1, "text": "手紙を"},
                                {"id": 2, "text": "ことが"},
                                {"id": 3, "text": "日本語で"},
                                {"id": 4, "text": "書く"}
                            ],
                            "fullOrder": [3, 1, 4, 2],
                            "starPos": 3,
                            "correctOption": 4, # part 4 "書く"
                            "fullSentence": "わたしは 日本語で 手紙を ★書く ことが できます。",
                            "explain": "Thứ tự sắp xếp: わたしは [3. 日本語で] [1. 手紙を] ★[4. 書く] [2. ことが] できます. Vị trí ★ là động từ thể từ điển (4) 書く."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "sentencePre": "出かける",
                            "sentencePost": "ください。",
                            "promptVi": "Trước khi ra ngoài xin hãy tắt đèn.",
                            "parts": [
                                {"id": 1, "text": "消して"},
                                {"id": 2, "text": "まえに"},
                                {"id": 3, "text": "忘れずに"},
                                {"id": 4, "text": "電気を"}
                            ],
                            "fullOrder": [2, 4, 1, 3],
                            "starPos": 3,
                            "correctOption": 1, # part 1 "消して"
                            "fullSentence": "出かける まえに 電気を ★消して 忘れずに ください。",
                            "explain": "Thứ tự sắp xếp: 出かける [2. まえに] [4. 電気を] ★[1. 消して] [3. 忘れずに] ください. Vị trí ngôi sao ★ là cụm (1) 消して."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "sentencePre": "駅を",
                            "sentencePost": "あります。",
                            "promptVi": "Ra khỏi ga, rẽ phải thì sẽ có đồn cảnh sát.",
                            "parts": [
                                {"id": 1, "text": "出て"},
                                {"id": 2, "text": "交番が"},
                                {"id": 3, "text": "右へ"},
                                {"id": 4, "text": "まがると"}
                            ],
                            "fullOrder": [1, 3, 4, 2],
                            "starPos": 3,
                            "correctOption": 4, # part 4 "まがると"
                            "fullSentence": "駅を 出て 右へ ★まがると 交番が あります。",
                            "explain": "Thứ tự sắp xếp: 駅を [1. 出て] [3. 右へ] ★[4. まがると] [2. 交番が] あります. Vị trí ngôi sao ★ là động từ (4) まがると."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "sentencePre": "母の",
                            "sentencePost": "買いました。",
                            "promptVi": "Tôi đã mua một chiếc khăn quàng cổ làm quà sinh nhật cho mẹ.",
                            "parts": [
                                {"id": 1, "text": "スカーフを"},
                                {"id": 2, "text": "たんじょうびの"},
                                {"id": 3, "text": "きれいで"},
                                {"id": 4, "text": "プレゼントに"}
                            ],
                            "fullOrder": [2, 4, 1, 3],
                            "starPos": 3,
                            "correctOption": 1, # part 1 "スカーフを"
                            "fullSentence": "母の たんじょうびの プレゼントに ★スカーフを きれいで 買いました。",
                            "explain": "Thứ tự sắp xếp: 母の [2. たんじょうびの] [4. プレゼントに] ★[1. スカーフを] 買いました. Vị trí ★ là (1) スカーフを."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 3: Dịch câu (Tự luận)",
                    "groupInstruction": "Nhập bản dịch vào ô trống (chấp nhận cả Kanji lẫn Hiragana, không phân biệt dấu cách):",
                    "items": [
                        {
                            "id": 31,
                            "type": "trans",
                            "dir": "vi_to_ja",
                            "prompt": "Dịch sang tiếng Nhật: <br><strong style='color:#1e1b4b;'>「Sau khi uống thuốc, tôi đã đi ngủ.」</strong>",
                            "placeholder": "Nhập câu tiếng Nhật (Ví dụ: 薬を 飲んでから、寝ました)...",
                            "acceptable": [
                                "薬を飲んでから、寝ました",
                                "くすりをのんでから、ねました",
                                "薬を飲んでから寝ました",
                                "くすりをのんでからねました",
                                "薬を飲んでから、ねました"
                            ],
                            "standard": "薬を 飲んでから、寝ました（くすりを のんでから、ねました）。",
                            "explain": "Mẫu câu V-te + から: Sau khi làm hành động 1 thì làm hành động 2. 薬を 飲みます ➔ 薬を 飲んでから, 寝ました."
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "dir": "ja_to_vi",
                            "prompt": "Dịch sang tiếng Việt: <br><strong style='color:#1e1b4b;'>「あそこに 白くて 高い 建物が 見えますか。」</strong>",
                            "placeholder": "Nhập câu dịch tiếng Việt (Ví dụ: Bạn có nhìn thấy tòa nhà màu trắng và cao ở đằng kia không?)...",
                            "keywords": ["nhìn thấy", "màu trắng", "cao", "tòa nhà", "đằng kia"],
                            "standard": "Bạn có nhìn thấy tòa nhà màu trắng và cao ở đằng kia không?",
                            "explain": "Nối tính từ đuôi い: 白い ➔ 白くて. Động từ 見えますか (có nhìn thấy... không?)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec4_reading",
            "partNumber": "IV",
            "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
            "partDesc": "Đọc email mời đi ngắm hoa anh đào dưới đây và chọn đáp án chính xác nhất cho 2 câu hỏi (33 và 34).",
            "badge": "10 Điểm",
            "readingPassage": {
                "title": "【田中さんからの メール：お花見の お誘い】",
                "content": "ナムさん、こんにちは。\n来週の 日曜日（4月5日）、上野公園で 友だちと お花見を します。\n桜が とても きれいに 咲いて いますよ。\nみんなで お弁当を 食べたり、写真を 撮ったり して、楽しく 過ごしましょう。\n\n集合時間は 午前11時です。上野駅の 公園口（こうえんぐち）で 待ち合わせます。\n飲み物や お菓子は 近くの コンビニで 買うことが できますから、何も 持って来なくても いいですよ。\n来ることが できますか。返事を 待って いますね！",
                "translation": "【Email từ anh Tanaka: Lời mời đi ngắm hoa anh đào】\nChào bạn Nam.\nChủ nhật tuần tới (ngày 5 tháng 4), mình sẽ cùng các bạn đi ngắm hoa anh đào ở công viên Ueno.\nHoa anh đào đang nở rất là đẹp đấy.\nMọi người sẽ cùng nhau ăn cơm hộp, chụp ảnh và tận hưởng khoảng thời gian vui vẻ nhé.\n\nThời gian tập trung là 11 giờ sáng. Chúng ta hẹn gặp nhau ở Cổng Công Viên (Kouen-guchi) ga Ueno.\nĐồ uống và bánh kẹo có thể mua ở cửa hàng tiện lợi gần đó nên bạn không cần mang theo gì cũng được.\nBạn có thể đi được không? Mình chờ hồi âm của bạn nhé!"
            },
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "お花見は いつ、どこで ありますか。",
                    "promptVi": "Buổi ngắm hoa diễn ra khi nào và ở đâu?",
                    "options": [
                        "4月5日の 日曜日に、上野公園で あります。",
                        "今週の 土曜日に、新宿御苑で あります。",
                        "4月15日の 日曜日に、市民センターで あります。",
                        "来週の 日曜日の 夜に、東京タワーで あります。"
                    ],
                    "correct": 0,
                    "explain": "Trong email ghi rõ: 『来週の 日曜日（4月5日）、上野公園で 友だちと お花見を します。』 Phương án A hoàn toàn chính xác."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "ナムさんは お花見に 何を 持って 行かなければ なりませんか。",
                    "promptVi": "Bạn Nam phải mang theo thứ gì khi đi ngắm hoa?",
                    "options": [
                        "飲み物やお菓子は コンビニで 買えますから、何も 持って行かなくても いいです。",
                        "手作りのお弁当と たくさんの お酒を 持って行きます。",
                        "重い カメラと 伝統的な 服を 持って行かなければ なりません。",
                        "入場料 2000円を 事前に 払わなければ なりません。"
                    ],
                    "correct": 0,
                    "explain": "Trong thư anh Tanaka ghi: 『飲み物や お菓子は 近くの コンビニで 買うことが できますから、何も 持って来なくても いいですよ。』 Do đó phương án A đúng."
                }
            ]
        },
        {
            "id": "sec5_essay",
            "partNumber": "V",
            "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
            "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (mỗi câu viết từ 2 đến 3 câu hoàn chỉnh).",
            "badge": "15 Điểm",
            "items": [
                {
                    "id": 35,
                    "type": "essay",
                    "prompt": "あなたの 趣味について 書いてください。（どんな 趣味ですか。いつ しますか。2〜3文で 書いてください）",
                    "promptVi": "Hãy giới thiệu về sở thích của bạn (Đó là sở thích gì? Bạn thường làm khi nào? Viết 2-3 câu tiếng Nhật)",
                    "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしの 趣味は サッカーを することです...)...",
                    "hints": [
                        "Sở thích là: わたしの 趣味は ～ことです / ～が好きです",
                        "Thời gian làm: 休みの日に / 毎晩 / 週末に",
                        "Cảm nghĩ: とても 楽しいです / リラックスできます"
                    ],
                    "modelAnswer": "わたしの 趣味は 写真を 撮る ことです。休みの日は いつも カメラを 持って、公園や 古い 町へ 行きます。とても 楽しいです。",
                    "modelVi": "Sở thích của tôi là chụp ảnh. Vào ngày nghỉ tôi luôn mang máy ảnh đi công viên hoặc những khu phố cổ. Rất là vui.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Sử dụng tốt mẫu câu biểu đạt sở thích (趣味は V-ることです); nêu rõ thời gian thực hiện; có tính từ cảm nghĩ."
                },
                {
                    "id": 36,
                    "type": "essay",
                    "prompt": "あなたの 住んでいる 町について 紹介してください。（どんな 町ですか。何が ありますか。2〜3文で 書いてください）",
                    "promptVi": "Hãy giới thiệu về thị trấn/thành phố nơi bạn đang sống (Đó là nơi như thế nào? Có những gì? Viết 2-3 câu tiếng Nhật)",
                    "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしの 住んでいる 町は ハノイです...)...",
                    "hints": [
                        "Giới thiệu nơi sống: わたしは ～に 住んで います",
                        "Đặc điểm nơi chốn: とても 静かで、きれいな 町です / にぎやかです",
                        "Địa điểm có sẵn: 近くに 大きな スーパーや 公園が あります"
                    ],
                    "modelAnswer": "わたしは ベトナムの ダナンに 住んで います。海が 近くて、とても きれいな 町です。おいしい 海鮮料理の レストランが たくさん あります。",
                    "modelVi": "Tôi đang sống ở Đà Nẵng, Việt Nam. Đó là một thành phố rất đẹp và gần biển. Nơi đây có rất nhiều nhà hàng hải sản ngon miệng.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Nêu rõ tên thành phố và cấu trúc 住んでいます; dùng đúng tính từ miêu tả đặc điểm (きれいで、近くて); kể được các địa điểm tiêu biểu."
                }
            ]
        }
    ]
}

M104 = {
    "code": "M104",
    "name": "Mã Đề M104 (Đề Đột Phá Giao Tiếp & Ẩm Thực)",
    "tag": "🍱 Đột Phá Bài 1 - 8 • Ẩm Thực & Nhà Hàng",
    "desc": "Tập trung vào giao tiếp Can-do trong đời sống thường nhật: gọi món, hỏi hương vị, sở thích, mượn đồ và lời mời tham gia sự kiện.",
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
                    "groupTitle": "DẠNG 1: Điền vào chỗ trống trong ngoặc (   )",
                    "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                    "items": [
                        {
                            "id": 1,
                            "type": "mc",
                            "prompt": "この レストランの 料理は 量が とても (   ) ですから、全部 食べられません。",
                            "promptVi": "Món ăn ở nhà hàng này lượng nhiều quá nên tôi không ăn hết được.",
                            "options": ["おおい", "すくない", "ちいさい", "せまい"],
                            "correct": 0,
                            "explain": "量が多い (りょうがおおい - lượng thức ăn nhiều). Trái nghĩa với 少ない (ít). Bài 6."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "あしたの 午後、会社の 会議室で (   ) が あります。",
                            "promptVi": "Chiều mai ở phòng họp công ty có cuộc họp.",
                            "options": ["ミーティング", "チケット", "ファッション", "メニュー"],
                            "correct": 0,
                            "explain": "Phòng họp công ty đi với ミーティング (meeting - cuộc họp). Bài 1-2."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "誕生日に お父さんから すてきな (   ) を もらいました。",
                            "promptVi": "Vào dịp sinh nhật, tôi đã nhận được một món quà rất đẹp từ bố.",
                            "options": ["プレゼント", "アルバイト", "ルール", "マナー"],
                            "correct": 0,
                            "explain": "Sinh nhật đi với quà tặng プレゼント (present). Bài 8."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "道を 渡る ときは、車に (   ) を つけて ください。",
                            "promptVi": "Khi sang đường, xin hãy chú ý cẩn thận xe cộ.",
                            "options": ["気", "手", "目", "足"],
                            "correct": 0,
                            "explain": "Quán dụng ngữ: 気をつける (きをつける - chú ý, cẩn thận). Bài 5."
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "のどが かわきましたから、冷たい (   ) が 飲みたいです。",
                            "promptVi": "Khát nước quá nên tôi muốn uống nước lạnh.",
                            "options": ["みず", "ごはん", "パン", "にく"],
                            "correct": 0,
                            "explain": "のどがかわきました (khát nước) thì uống 水 (みず - nước). Bài 6."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Chọn câu hoặc từ đồng nghĩa",
                    "groupInstruction": "Chọn câu (A, B, C, D) có ý nghĩa tương đương gần nhất với câu hoặc cụm từ được gạch chân:",
                    "items": [
                        {
                            "id": 6,
                            "type": "mc",
                            "prompt": "わたしは よく 料理を <span class='hl-kw'>失敗します</span>。",
                            "promptVi": "Tôi thường nấu ăn bị thất bại (hỏng).",
                            "options": [
                                "料理を うまく 作ることが できません。",
                                "料理が とても 得意で、上手です。",
                                "いつも レストランで 食べます。",
                                "料理を まったく 作りません。"
                            ],
                            "correct": 0,
                            "explain": "失敗します (しっぱいします - thất bại) = うまく 作ることが できません (không thể nấu ngon/thành công)."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "この 部屋は <span class='hl-kw'>せまい</span> です。",
                            "promptVi": "Căn phòng này chật hẹp.",
                            "options": [
                                "部屋が ひろく ありません。",
                                "部屋が とても 明るいです。",
                                "部屋が とても 静かです。",
                                "家賃が とても 高いです。"
                            ],
                            "correct": 0,
                            "explain": "せまい (chật chội) = ひろく ありません (không rộng rãi)."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "この シャツは <span class='hl-kw'>ちょうど いい</span> です。",
                            "promptVi": "Chiếc áo này vừa vặn.",
                            "options": [
                                "サイズが ぴったりで、ちょうど 合っています。",
                                "大きすぎて、着られません。",
                                "小さくて、苦しいです。",
                                "色が とても 派手です。"
                            ],
                            "correct": 0,
                            "explain": "ちょうど いい (vừa khít, vừa vặn) = サイズが ぴったり (kích cỡ chuẩn)."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "駅の まわりは いつも <span class='hl-kw'>にぎやか</span> です。",
                            "promptVi": "Khu vực xung quanh ga lúc nào cũng nhộn nhịp, náo nhiệt.",
                            "options": [
                                "人が たくさん いて、活気が あります。",
                                "人が ぜんぜん いなくて、暗いです。",
                                "とても 静かで、落ち着きます。",
                                "危険な 場所が たくさん あります。"
                            ],
                            "correct": 0,
                            "explain": "にぎやか (nhộn nhịp, sầm uất) = có nhiều người và không khí sôi động."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "山田さんは <span class='hl-kw'>お酒に 強い</span> です。",
                            "promptVi": "Anh Yamada uống rượu rất cừ (tửu lượng tốt).",
                            "options": [
                                "お酒を たくさん 飲んでも、あまり 酔いません。",
                                "お酒が きらいで、全然 飲みません。",
                                "一杯 飲んだら、すぐ 眠くなります。",
                                "お酒の 匂いが 苦手です。"
                            ],
                            "correct": 0,
                            "explain": "お酒に強い (uống được nhiều rượu mà không dễ say)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec2_kanji",
            "partNumber": "II",
            "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
            "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán ra Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20).",
            "badge": "20 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Kanji ➔ Hiragana (Chọn cách đọc đúng)",
                    "groupInstruction": "Chọn cách đọc Hiragana đúng cho chữ Hán gạch chân:",
                    "items": [
                        {
                            "id": 11,
                            "type": "mc",
                            "prompt": "あした <span class='hl-kw'>雨</span>が 降るでしょう。",
                            "promptVi": "Ngày mai chắc là trời sẽ mưa.",
                            "options": ["あめ", "ゆき", "かぜ", "くも"],
                            "correct": 0,
                            "explain": "「雨」 đọc là あめ (Mưa)."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "毎晩 11時に <span class='hl-kw'>寝ます</span>。",
                            "promptVi": "Mỗi tối tôi đi ngủ lúc 11 giờ.",
                            "options": ["ねます", "おきます", "いきます", "きます"],
                            "correct": 0,
                            "explain": "「寝ます」 đọc là ねます (Đi ngủ)."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "日本の <span class='hl-kw'>夏</span>は とても 暑いです。",
                            "promptVi": "Mùa hè ở Nhật Bản rất nóng.",
                            "options": ["なつ", "はる", "あき", "ふゆ"],
                            "correct": 0,
                            "explain": "「夏」 đọc là なつ (Mùa hè)."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "駅で 電車を <span class='hl-kw'>降りました</span>。",
                            "promptVi": "Tôi đã xuống tàu ở nhà ga.",
                            "options": ["おりました", "のりました", "あがりました", "はいりました"],
                            "correct": 0,
                            "explain": "「降りました」 đọc là おりました (Đã xuống xe/tàu)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "あの <span class='hl-kw'>高い</span> 山は 富士山です。",
                            "promptVi": "Ngọn núi cao đằng kia là núi Phú Sĩ.",
                            "options": ["たかい", "ひくい", "ながい", "ひろい"],
                            "correct": 0,
                            "explain": "「高い」 đọc là たかい (Cao)."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Hiragana ➔ Kanji (Chọn chữ Hán đúng)",
                    "groupInstruction": "Chọn chữ Hán đúng cho từ Hiragana gạch chân:",
                    "items": [
                        {
                            "id": 16,
                            "type": "mc",
                            "prompt": "友だちと お茶を <span class='hl-kw'>のみました</span>。",
                            "promptVi": "Tôi đã uống trà cùng bạn bè.",
                            "options": ["飲みました", "食べました", "買いました", "見ました"],
                            "correct": 0,
                            "explain": "のみました (uống) là chữ Hán「飲」➔ 飲みました."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "きれいな 花を <span class='hl-kw'>みました</span>。",
                            "promptVi": "Tôi đã ngắm bông hoa đẹp.",
                            "options": ["見ました", "聞きました", "読みました", "立ちました"],
                            "correct": 0,
                            "explain": "みました (xem/ngắm) là chữ Hán「見」➔ 見ました."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "日本語の 本を <span class='hl-kw'>よみます</span>。",
                            "promptVi": "Tôi đọc sách tiếng Nhật.",
                            "options": ["読みます", "書きます", "聞きます", "話します"],
                            "correct": 0,
                            "explain": "よみます (đọc) là chữ Hán「読」➔ 読みます."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "あした 家族と <span class='hl-kw'>やま</span>へ 行きます。",
                            "promptVi": "Ngày mai tôi đi leo núi cùng gia đình.",
                            "options": ["山", "川", "海", "空"],
                            "correct": 0,
                            "explain": "やま (núi) là chữ Hán「山」."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "この <span class='hl-kw'>かわ</span>で 魚を つります。",
                            "promptVi": "Câu cá ở con sông này.",
                            "options": ["川", "海", "池", "湖"],
                            "correct": 0,
                            "explain": "かわ (dòng sông) là chữ Hán「川」."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec3_grammar",
            "partNumber": "III",
            "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
            "partDesc": "Gồm 3 dạng bài: Điền khuyết (21-26), Hái sao ☆ (27-30), Dịch câu (31-32).",
            "badge": "30 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Điền vào chỗ trống trong ngoặc (   )",
                    "groupInstruction": "Chọn trợ từ hoặc dạng chia ngữ pháp đúng nhất điền vào (   ):",
                    "items": [
                        {
                            "id": 21,
                            "type": "mc",
                            "prompt": "すみません、写真を 撮って (   ) か。",
                            "promptVi": "Xin lỗi, bạn có thể chụp ảnh giúp tôi được không?",
                            "options": ["もらえません", "あげません", "しません", "なりせん"],
                            "correct": 0,
                            "explain": "～て もらえませんか (Mẫu câu nhờ vả đối phương giúp đỡ lịch sự)."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "美術館の 中では 走って (   ) いけません。",
                            "promptVi": "Trong bảo tàng mỹ thuật không được chạy nhảy.",
                            "options": ["は", "も", "が", "を"],
                            "correct": 0,
                            "explain": "V-te + は いけません (Cấm đoán nội quy)."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "京都へ 行った (   ) が ありますか。",
                            "promptVi": "Bạn đã từng đến Kyoto bao giờ chưa?",
                            "options": ["こと", "の", "とき", "もの"],
                            "correct": 0,
                            "explain": "V-ta + ことが あります (Mẫu câu hỏi kinh nghiệm đã từng làm gì)."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "ごはんを 食べて (   )、お風呂に 入ります。",
                            "promptVi": "Sau khi ăn cơm xong, tôi đi tắm bồn.",
                            "options": ["から", "まで", "より", "ながら"],
                            "correct": 0,
                            "explain": "V-te + から (Sau khi làm V1 thì làm V2)."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "この パソコンは 軽くて、(   ) 使いやすいです。",
                            "promptVi": "Chiếc máy tính này vừa nhẹ lại vừa dễ sử dụng.",
                            "options": ["とても", "あまり", "全然", "少しも"],
                            "correct": 0,
                            "explain": "Nối ý tích cực: 軽くて (nhẹ) và とても 使いやすい (rất dễ dùng)."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "休みの日は 音楽を 聞いたり、本を (   ) しました。",
                            "promptVi": "Vào ngày nghỉ tôi vừa nghe nhạc vừa đọc sách...",
                            "options": ["読んだり", "読んで", "読んだ", "読む"],
                            "correct": 0,
                            "explain": "Mẫu V1-たり、V2-たり します: 読みます chuyển sang là 読んだり."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: ☆ Hái sao (Sắp xếp cụm từ vào đúng vị trí)",
                    "groupInstruction": "Sắp xếp 4 cụm từ [1, 2, 3, 4] vào 4 vị trí trống và chọn số tương ứng tại vị trí ngôi sao ★:",
                    "items": [
                        {
                            "id": 27,
                            "type": "star",
                            "sentencePre": "この",
                            "sentencePost": "です。",
                            "promptVi": "Chiếc máy tính này nhẹ và rất dễ sử dụng.",
                            "parts": [
                                {"id": 1, "text": "使いやすい"},
                                {"id": 2, "text": "パソコンは"},
                                {"id": 3, "text": "とても"},
                                {"id": 4, "text": "軽くて"}
                            ],
                            "fullOrder": [2, 4, 3, 1],
                            "starPos": 3,
                            "correctOption": 3, # part 3 "とても"
                            "fullSentence": "この パソコンは 軽くて ★とても 使いやすい です。",
                            "explain": "Thứ tự sắp xếp: この [2. パソコンは] [4. 軽くて] ★[3. とても] [1. 使いやすい] です. Vị trí ★ là phó từ (3) とても."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "sentencePre": "雨が",
                            "sentencePost": "持っていきます。",
                            "promptVi": "Vì trời đang mưa nên tôi sẽ mang theo ô.",
                            "parts": [
                                {"id": 1, "text": "いますから"},
                                {"id": 2, "text": "忘れずに"},
                                {"id": 3, "text": "降って"},
                                {"id": 4, "text": "傘を"}
                            ],
                            "fullOrder": [3, 1, 4, 2],
                            "starPos": 3,
                            "correctOption": 4, # part 4 "傘を"
                            "fullSentence": "雨が 降って いますから ★傘を 忘れずに 持っていきます。",
                            "explain": "Thứ tự sắp xếp: 雨が [3. 降って] [1. いますから] ★[4. 傘を] [2. 忘れずに] 持っていきます. Vị trí ngôi sao ★ là cụm (4) 傘を."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "sentencePre": "駅へ",
                            "sentencePost": "曲がってください。",
                            "promptVi": "Để đi tới nhà ga, hãy rẽ trái ở góc ngã rẽ đằng kia.",
                            "parts": [
                                {"id": 1, "text": "左へ"},
                                {"id": 2, "text": "あのかどを"},
                                {"id": 3, "text": "まっすぐ行って"},
                                {"id": 4, "text": "行くには"}
                            ],
                            "fullOrder": [4, 3, 2, 1],
                            "starPos": 3,
                            "correctOption": 2, # part 2 "あのかどを"
                            "fullSentence": "駅へ 行くには まっすぐ行って ★あのかどを 左へ 曲がってください。",
                            "explain": "Thứ tự sắp xếp: 駅へ [4. 行くには] [3. まっすぐ行って] ★[2. あのかどを] [1. 左へ] 曲がってください. Vị trí ★ là (2) あのかどを."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "sentencePre": "わたしは",
                            "sentencePost": "ありません。",
                            "promptVi": "Tôi chưa từng ăn món sashimi bao giờ.",
                            "parts": [
                                {"id": 1, "text": "刺身を"},
                                {"id": 2, "text": "一度も"},
                                {"id": 3, "text": "食べた"},
                                {"id": 4, "text": "ことが"}
                            ],
                            "fullOrder": [2, 1, 3, 4],
                            "starPos": 3,
                            "correctOption": 3, # part 3 "食べた"
                            "fullSentence": "わたしは 一度も 刺身を ★食べた ことが ありません。",
                            "explain": "Thứ tự sắp xếp: わたしは [2. 一度も] [1. 刺身を] ★[3. 食べた] [4. ことが] ありません. Vị trí ★ là động từ thể Ta (3) 食べた."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 3: Dịch câu (Tự luận)",
                    "groupInstruction": "Nhập bản dịch vào ô trống (chấp nhận cả Kanji lẫn Hiragana, không phân biệt dấu cách):",
                    "items": [
                        {
                            "id": 31,
                            "type": "trans",
                            "dir": "vi_to_ja",
                            "prompt": "Dịch sang tiếng Nhật: <br><strong style='color:#1e1b4b;'>「Xin lỗi, hãy cho tôi xem chiếc đồng hồ kia.」</strong>",
                            "placeholder": "Nhập câu tiếng Nhật (Ví dụ: すみません、あの 時計を 見せて ください)...",
                            "acceptable": [
                                "すみません、あの時計を見せてください",
                                "すみません、あのとけいをみせてください",
                                "あの時計を見せてください",
                                "あのとけいをみせてください",
                                "すみませんあの時計を見せてください"
                            ],
                            "standard": "すみません、あの 時計を 見せて ください（あの とけいを みせて ください）。",
                            "explain": "Mẫu câu nhờ xem đồ: [Vật] を 見せて ください (みせてください). あの 時計 (chiếc đồng hồ kia)."
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "dir": "ja_to_vi",
                            "prompt": "Dịch sang tiếng Việt: <br><strong style='color:#1e1b4b;'>「この 川で 泳いでは いけません。あぶないですから。」</strong>",
                            "placeholder": "Nhập câu dịch tiếng Việt (Ví dụ: Không được bơi ở con sông này vì nguy hiểm)...",
                            "keywords": ["không được bơi", "sông", "nguy hiểm"],
                            "standard": "Không được bơi ở con sông này. Vì rất nguy hiểm.",
                            "explain": "Mẫu câu cấm đoán: V-ては いけません (không được làm V). あぶない (nguy hiểm)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec4_reading",
            "partNumber": "IV",
            "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
            "partDesc": "Đọc thông báo về lớp học nấu ăn Nhật Bản dưới đây và chọn đáp án chính xác nhất cho 2 câu hỏi (33 và 34).",
            "badge": "10 Điểm",
            "readingPassage": {
                "title": "【無料の 日本料理教室の ご案内】",
                "content": "外国人の みなさん、日本の 料理を 一緒に 作りませんか。\n来月の 10日（土曜日）、中央コミュニティセンターで「日本料理教室」を 開きます。\n今回の メニューは、巻き寿司（まきずし）と みそ汁です。\nプロの 料理人が やさしく 作り方を 教えて くれますから、初めての 人でも 大丈夫です。\n\n参加費は 無料ですが、材料の 準備が ありますから、事前に 申し込みが 必要です。\n定員は 20人です。エプロンと 三角巾（さんかくきん）を 持って来て ください。\nみなさんの ご参加を お待ちして います！",
                "translation": "【Thông báo Lớp học nấu món ăn Nhật miễn phí】\nCác bạn người nước ngoài ơi, các bạn có muốn cùng nhau nấu món ăn Nhật Bản không?\nThứ Bảy ngày 10 tháng sau, tại Trung tâm cộng đồng trung tâm sẽ mở 'Lớp học nấu món ăn Nhật'.\nThực đơn lần này là món sushi cuộn (Makizushi) và canh tương Miso.\nĐầu bếp chuyên nghiệp sẽ tận tình hướng dẫn cách làm nên người mới học lần đầu cũng hoàn toàn yên tâm.\n\nPhí tham gia là miễn phí, tuy nhiên vì cần chuẩn bị nguyên liệu nên cần đăng ký trước.\nSố lượng giới hạn là 20 người. Xin hãy mang theo tạp dề và khăn trùm đầu tam giác.\nRất mong nhận được sự tham gia của tất cả các bạn!"
            },
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "この 料理教室で 何を 作りますか。",
                    "promptVi": "Ở lớp học nấu ăn này mọi người sẽ nấu món gì?",
                    "options": [
                        "巻き寿司と みそ汁を 作ります。",
                        "ラーメンと たこ焼きを 作ります。",
                        "カレーライスと サラダを 作ります。",
                        "ケーキと クッキーを 作ります。"
                    ],
                    "correct": 0,
                    "explain": "Trong thông báo ghi rõ: 『今回の メニューは、巻き寿司と みそ汁です。』 Phương án A đúng."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "料理教室に ついて、正しい ものは どれですか。",
                    "promptVi": "Câu nào dưới đây là ĐÚNG về lớp học nấu ăn?",
                    "options": [
                        "参加費は 無料ですが、事前に 申し込みが 必要です。",
                        "材料費として 3000円を 当日 払わなければ なりません。",
                        "料理の 経験が ある 人だけ 参加できます。",
                        "エプロンは 教室で 無料で 貸して もらえます。"
                    ],
                    "correct": 0,
                    "explain": "Trong bài nêu: 『参加費は 無料ですが、材料の 準備が ありますから、事前に 申し込みが 必要です。』 Phương án A hoàn toàn chính xác."
                }
            ]
        },
        {
            "id": "sec5_essay",
            "partNumber": "V",
            "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
            "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (mỗi câu viết từ 2 đến 3 câu hoàn chỉnh).",
            "badge": "15 Điểm",
            "items": [
                {
                    "id": 35,
                    "type": "essay",
                    "prompt": "日本へ 行ったら、どんな お土産を 買いたいですか。（だれに 買いますか。2〜3文で 書いてください）",
                    "promptVi": "Nếu sang Nhật, bạn muốn mua quà lưu niệm gì? Bạn mua cho ai? (Viết 2-3 câu bằng tiếng Nhật)",
                    "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしは 家族に 日本のお菓子を 買いたいです...)...",
                    "hints": [
                        "Quà lưu niệm: お菓子 / 抹茶 / 着物 / お守り",
                        "Người nhận: 家族に / 友達に / 両親に",
                        "Mục đích & Lý do: 有名ですから / きれいですから"
                    ],
                    "modelAnswer": "わたしは 家族に 日本の おいしい 抹茶のお菓子を 買いたいです。日本の お菓子は とても きれいで 有名ですから。そして、友だちには かわいい キーホルダーを あげたいです。",
                    "modelVi": "Tôi muốn mua bánh kẹo matcha ngon của Nhật cho gia đình. Vì bánh kẹo Nhật rất đẹp và nổi tiếng. Và tôi muốn tặng móc khóa dễ thương cho bạn bè.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Nêu rõ loại quà lưu niệm muốn mua (お土産) và đối tượng nhận (～に); dùng đúng mẫu câu biểu đạt mong muốn ～たいです."
                },
                {
                    "id": 36,
                    "type": "essay",
                    "prompt": "あなたの 朝の 習慣（ルーティン）について 書いてください。（起きてから 何を しますか。2〜3文で 書いてください）",
                    "promptVi": "Hãy viết về thói quen buổi sáng của bạn (Sau khi thức dậy bạn làm những gì? Viết 2-3 câu bằng tiếng Nhật)",
                    "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: 毎朝 6時に 起きます...)...",
                    "hints": [
                        "Giờ thức dậy: 毎朝 ～時に 起きます",
                        "Chuỗi hành động sau khi dậy: 起きてから ～ます",
                        "Nối hành động: ～て、～ます / ～たり、～たり します"
                    ],
                    "modelAnswer": "わたしは 毎朝 6時半に 起きます。起きてから、顔を 洗って、熱い コーヒーを 飲みます。それから、日本語の 単語を 15分 勉強します。",
                    "modelVi": "Mỗi sáng tôi thức dậy lúc 6 rưỡi. Sau khi dậy, tôi rửa mặt rồi uống một ly cà phê nóng. Sau đó, tôi học từ vựng tiếng Nhật 15 phút.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Diễn đạt mạch lạc trình tự buổi sáng bằng thể Te (～て、～ます); dùng đúng trợ từ và mốc thời gian."
                }
            ]
        }
    ]
}

M105 = {
    "code": "M105",
    "name": "Mã Đề M105 (Đề Tuyển Chọn Chuẩn Đề Thầy Cô)",
    "tag": "🎯 Chuẩn Đề Giảng Viên • Khảo Sát Năng Lực",
    "desc": "Đề tổng duyệt các bẫy thường gặp trong đề thi: phân biệt trợ từ, chia thể Te/Ru, nhận biết ngữ cảnh từ vựng và tự luận mở rộng.",
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
                    "groupTitle": "DẠNG 1: Điền vào chỗ trống trong ngoặc (   )",
                    "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                    "items": [
                        {
                            "id": 1,
                            "type": "mc",
                            "prompt": "すみません、お会計（おかいけい）を (   ) ください。",
                            "promptVi": "Xin lỗi, xin vui lòng tính tiền giúp tôi.",
                            "options": ["おねがいします", "みせて", "あけて", "わたって"],
                            "correct": 0,
                            "explain": "Khi thanh toán ở nhà hàng: お会計を お願いします (おねがいします - Xin vui lòng tính tiền). Bài 6."
                        },
                        {
                            "id": 2,
                            "type": "mc",
                            "prompt": "あしたは 朝から 晩まで 予定が いっぱいですから、とても (   ) です。",
                            "promptVi": "Ngày mai từ sáng đến tối kín lịch nên tôi rất bận.",
                            "options": ["いそがしい", "ひま", "たのしい", "さびしい"],
                            "correct": 0,
                            "explain": "予定がいっぱい (kín lịch trình) ➔ 忙しい (いそがしい - bận rộn). Bài 2-3."
                        },
                        {
                            "id": 3,
                            "type": "mc",
                            "prompt": "ベトナムから 日本まで 飛行機で 5時間 (   ) かかります。",
                            "promptVi": "Từ Việt Nam sang Nhật Bản đi máy bay mất khoảng chừng 5 tiếng.",
                            "options": ["ぐらい", "だけ", "より", "ほど"],
                            "correct": 0,
                            "explain": "Lượng thời gian + ぐらい (khoảng chừng). Bài 5."
                        },
                        {
                            "id": 4,
                            "type": "mc",
                            "prompt": "この 店は 野菜が いつも (   ) で、おいしいです。",
                            "promptVi": "Cửa hàng này rau lúc nào cũng tươi mới nên rất ngon.",
                            "options": ["しんせん", "ふるい", "からい", "にがい"],
                            "correct": 0,
                            "explain": "新鮮 (しんせん - tươi mới, tươi ngon). Từ vựng thực phẩm Bài 6."
                        },
                        {
                            "id": 5,
                            "type": "mc",
                            "prompt": "友だちの 結婚式に すてきな (   ) を 着て 行きました。",
                            "promptVi": "Tôi đã mặc chiếc váy tuyệt đẹp đi dự đám cưới của bạn.",
                            "options": ["ドレス", "くつ", "ぼうし", "かばん"],
                            "correct": 0,
                            "explain": "Mặc quần áo/váy dùng động từ 着て (きて) ➔ ドレス (dress - váy đầm dạ tiệc). Bài 8."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Chọn câu hoặc từ đồng nghĩa",
                    "groupInstruction": "Chọn câu (A, B, C, D) có ý nghĩa tương đương gần nhất với câu hoặc cụm từ được gạch chân:",
                    "items": [
                        {
                            "id": 6,
                            "type": "mc",
                            "prompt": "わたしは 毎朝 <span class='hl-kw'>ジョギングを します</span>。",
                            "promptVi": "Mỗi sáng tôi đều chạy bộ thể dục.",
                            "options": [
                                "ゆっくり 走って 運動を します。",
                                "車で ドライブを します。",
                                "家で ずっと 寝て います。",
                                "公園で 魚を つります。"
                            ],
                            "correct": 0,
                            "explain": "ジョギング (jogging - chạy bộ thể dục) = ゆっくり 走って 運動を します."
                        },
                        {
                            "id": 7,
                            "type": "mc",
                            "prompt": "この 部屋は <span class='hl-kw'>あたたかい</span> です。",
                            "promptVi": "Căn phòng này ấm áp.",
                            "options": [
                                "寒く ありません。",
                                "とても 暑くて、息が 苦しいです。",
                                "エアコンが こわれて います。",
                                "とても 暗いです。"
                            ],
                            "correct": 0,
                            "explain": "あたたかい (ấm áp) = 寒くありません (không lạnh)."
                        },
                        {
                            "id": 8,
                            "type": "mc",
                            "prompt": "あの 人は <span class='hl-kw'>英語が ペラペラです</span>。",
                            "promptVi": "Người kia nói tiếng Anh lưu loát, trôi chảy.",
                            "options": [
                                "とても 上手に すらすら 英語を 話せます。",
                                "英語が まったく 話せません。",
                                "英語を 勉強したことが ありません。",
                                "英語の 単語を すぐ 忘れます。"
                            ],
                            "correct": 0,
                            "explain": "ペラペラ (lưu loát, trôi chảy khi nói ngoại ngữ) = 上手に すらすら 話せます."
                        },
                        {
                            "id": 9,
                            "type": "mc",
                            "prompt": "この 図書館は とても <span class='hl-kw'>しずか</span> です。",
                            "promptVi": "Thư viện này rất yên tĩnh.",
                            "options": [
                                "音が なくて、うるさく ありません。",
                                "人が 大声で 叫んで います。",
                                "とても にぎやかです。",
                                "本が 一冊も ありません。"
                            ],
                            "correct": 0,
                            "explain": "しずか (静か - yên tĩnh) = không ồn ào (うるさくありません)."
                        },
                        {
                            "id": 10,
                            "type": "mc",
                            "prompt": "あしたは <span class='hl-kw'>つごうが わるい</span> です。",
                            "promptVi": "Ngày mai tôi không tiện (bận lịch, không thu xếp được).",
                            "options": [
                                "予定が あって、行くことが できません。",
                                "時間が たくさん あって、ひまです。",
                                "とても 元気です。",
                                "早く 会いたいです。"
                            ],
                            "correct": 0,
                            "explain": "都合が悪い (つごうがわるい - kẹt lịch, không tiện đi được)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec2_kanji",
            "partNumber": "II",
            "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
            "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán ra Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20).",
            "badge": "20 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Kanji ➔ Hiragana (Chọn cách đọc đúng)",
                    "groupInstruction": "Chọn cách đọc Hiragana đúng cho chữ Hán gạch chân:",
                    "items": [
                        {
                            "id": 11,
                            "type": "mc",
                            "prompt": "きのう <span class='hl-kw'>午後</span> 3時に 友達に 会いました。",
                            "promptVi": "Hôm qua lúc 3 giờ chiều tôi đã gặp bạn.",
                            "options": ["ごご", "ごぜん", "あさ", "よる"],
                            "correct": 0,
                            "explain": "「午後」 đọc là ごご (Buổi chiều / PM)."
                        },
                        {
                            "id": 12,
                            "type": "mc",
                            "prompt": "この <span class='hl-kw'>魚</span>は とても おいしいです。",
                            "promptVi": "Món cá này rất ngon.",
                            "options": ["さかな", "にく", "たまご", "やさい"],
                            "correct": 0,
                            "explain": "「魚」 đọc là さかな (Con cá)."
                        },
                        {
                            "id": 13,
                            "type": "mc",
                            "prompt": "あの 赤い <span class='hl-kw'>車</span>は 父の 車です。",
                            "promptVi": "Chiếc ô tô màu đỏ đằng kia là xe của bố tôi.",
                            "options": ["くるま", "でんしゃ", "じてんしゃ", "ふね"],
                            "correct": 0,
                            "explain": "「車」 đọc là くるま (Xe hơi)."
                        },
                        {
                            "id": 14,
                            "type": "mc",
                            "prompt": "今朝 早く <span class='hl-kw'>起きました</span>。",
                            "promptVi": "Sáng nay tôi đã thức dậy sớm.",
                            "options": ["おきました", "ねました", "でかけました", "かえりました"],
                            "correct": 0,
                            "explain": "「起きました」 đọc là おきました (Đã thức dậy)."
                        },
                        {
                            "id": 15,
                            "type": "mc",
                            "prompt": "日本語の <span class='hl-kw'>言葉</span>を たくさん 覚えました。",
                            "promptVi": "Tôi đã ghi nhớ nhiều từ vựng tiếng Nhật.",
                            "options": ["ことば", "かんじ", "ぶんぽう", "おと"],
                            "correct": 0,
                            "explain": "「言葉」 đọc là ことば (Từ vựng, lời nói)."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: Hiragana ➔ Kanji (Chọn chữ Hán đúng)",
                    "groupInstruction": "Chọn chữ Hán đúng cho từ Hiragana gạch chân:",
                    "items": [
                        {
                            "id": 16,
                            "type": "mc",
                            "prompt": "デパートで 服を <span class='hl-kw'>かいました</span>。",
                            "promptVi": "Tôi đã mua quần áo ở trung tâm thương mại.",
                            "options": ["買いました", "売りました", "着ました", "脱ぎました"],
                            "correct": 0,
                            "explain": "かいました (mua) là chữ Hán「買」➔ 買いました."
                        },
                        {
                            "id": 17,
                            "type": "mc",
                            "prompt": "公園で 写真を <span class='hl-kw'>とりました</span>。",
                            "promptVi": "Tôi đã chụp ảnh ở công viên.",
                            "options": ["撮りました", "取りました", "見ました", "書きました"],
                            "correct": 0,
                            "explain": "写真を とりました (chụp ảnh) là chữ Hán「撮」➔ 撮りました."
                        },
                        {
                            "id": 18,
                            "type": "mc",
                            "prompt": "母は 中学校の <span class='hl-kw'>せんせい</span> です。",
                            "promptVi": "Mẹ tôi là giáo viên trường cấp 2.",
                            "options": ["先生", "学生", "生徒", "校長"],
                            "correct": 0,
                            "explain": "せんせい là chữ Hán「先生」."
                        },
                        {
                            "id": 19,
                            "type": "mc",
                            "prompt": "あの <span class='hl-kw'>みせ</span>で 昼ごはんを 食べました。",
                            "promptVi": "Tôi đã ăn trưa ở cửa tiệm đằng kia.",
                            "options": ["店", "駅", "館", "室"],
                            "correct": 0,
                            "explain": "みせ là chữ Hán「店」."
                        },
                        {
                            "id": 20,
                            "type": "mc",
                            "prompt": "駅の <span class='hl-kw'>まえ</span>で 友達を 待ちました。",
                            "promptVi": "Tôi đã đợi bạn ở trước nhà ga.",
                            "options": ["前", "後", "横", "隣"],
                            "correct": 0,
                            "explain": "まえ là chữ Hán「前」."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec3_grammar",
            "partNumber": "III",
            "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
            "partDesc": "Gồm 3 dạng bài: Điền khuyết (21-26), Hái sao ☆ (27-30), Dịch câu (31-32).",
            "badge": "30 Điểm",
            "groups": [
                {
                    "groupTitle": "DẠNG 1: Điền vào chỗ trống trong ngoặc (   )",
                    "groupInstruction": "Chọn trợ từ hoặc dạng chia ngữ pháp đúng nhất điền vào (   ):",
                    "items": [
                        {
                            "id": 21,
                            "type": "mc",
                            "prompt": "わたしは 車を 運転する (   ) が できます。",
                            "promptVi": "Tôi có thể lái xe hơi.",
                            "options": ["こと", "の", "もの", "とき"],
                            "correct": 0,
                            "explain": "V-ru + ことが できます (Mẫu câu khả năng)."
                        },
                        {
                            "id": 22,
                            "type": "mc",
                            "prompt": "寝る (   ) に、歯を みがきます。",
                            "promptVi": "Trước khi đi ngủ, tôi đánh răng.",
                            "options": ["まえ", "あと", "とき", "から"],
                            "correct": 0,
                            "explain": "V-ru + まえに (Trước khi làm việc V)."
                        },
                        {
                            "id": 23,
                            "type": "mc",
                            "prompt": "ここで タバコを 吸って (   ) いけません。",
                            "promptVi": "Không được hút thuốc ở đây.",
                            "options": ["は", "も", "が", "を"],
                            "correct": 0,
                            "explain": "V-te + は いけません (Cấm đoán)."
                        },
                        {
                            "id": 24,
                            "type": "mc",
                            "prompt": "窓を 開けて (   ) いいですか。",
                            "promptVi": "Tôi mở cửa sổ có được không?",
                            "options": ["も", "は", "が", "を"],
                            "correct": 0,
                            "explain": "V-te + も いいですか (Xin phép)."
                        },
                        {
                            "id": 25,
                            "type": "mc",
                            "prompt": "雨が 降って (   )、涼しく なりました。",
                            "promptVi": "Sau khi mưa rơi thì trời trở nên mát mẻ hơn.",
                            "options": ["から", "まで", "より", "ながら"],
                            "correct": 0,
                            "explain": "V-te + から (Sau khi hành động V xảy ra)."
                        },
                        {
                            "id": 26,
                            "type": "mc",
                            "prompt": "日曜日、洗濯を したり、部屋を 掃除 (   ) しました。",
                            "promptVi": "Chủ nhật tôi giặt giũ và dọn dẹp phòng...",
                            "options": ["したり", "して", "した", "する"],
                            "correct": 0,
                            "explain": "Mẫu liệt kê: ～たり、～たり します."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 2: ☆ Hái sao (Sắp xếp cụm từ vào đúng vị trí)",
                    "groupInstruction": "Sắp xếp 4 cụm từ [1, 2, 3, 4] vào 4 vị trí trống và chọn số tương ứng tại vị trí ngôi sao ★:",
                    "items": [
                        {
                            "id": 27,
                            "type": "star",
                            "sentencePre": "あしたは",
                            "sentencePost": "です。",
                            "promptVi": "Ngày mai tôi muốn đi biển cùng bạn và bơi lội.",
                            "parts": [
                                {"id": 1, "text": "海へ"},
                                {"id": 2, "text": "泳ぎたい"},
                                {"id": 3, "text": "友だちと"},
                                {"id": 4, "text": "行って"}
                            ],
                            "fullOrder": [3, 1, 4, 2],
                            "starPos": 3,
                            "correctOption": 4, # part 4 "行って"
                            "fullSentence": "あしたは 友だちと 海へ ★行って 泳ぎたい です。",
                            "explain": "Thứ tự sắp xếp: あしたは [3. 友だちと] [1. 海へ] ★[4. 行って] [2. 泳ぎたい] です. Vị trí ★ là thể Te (4) 行って."
                        },
                        {
                            "id": 28,
                            "type": "star",
                            "sentencePre": "ごはんを",
                            "sentencePost": "洗います。",
                            "promptVi": "Trước khi ăn cơm, tôi rửa tay thật sạch.",
                            "parts": [
                                {"id": 1, "text": "手を"},
                                {"id": 2, "text": "食べる"},
                                {"id": 3, "text": "きれいに"},
                                {"id": 4, "text": "まえに"}
                            ],
                            "fullOrder": [2, 4, 1, 3],
                            "starPos": 3,
                            "correctOption": 1, # part 1 "手を"
                            "fullSentence": "ごはんを 食べる まえに ★手を きれいに 洗います。",
                            "explain": "Thứ tự sắp xếp: ごはんを [2. 食べる] [4. まえに] ★[1. 手を] [3. きれいに] 洗います. Vị trí ngôi sao ★ là tân ngữ (1) 手を."
                        },
                        {
                            "id": 29,
                            "type": "star",
                            "sentencePre": "交差点を",
                            "sentencePost": "あります。",
                            "promptVi": "Băng qua ngã tư, đi thẳng thì sẽ có bưu điện ở bên tay phải.",
                            "parts": [
                                {"id": 1, "text": "渡って"},
                                {"id": 2, "text": "行くと"},
                                {"id": 3, "text": "まっすぐ"},
                                {"id": 4, "text": "右側に"}
                            ],
                            "fullOrder": [1, 3, 2, 4],
                            "starPos": 3,
                            "correctOption": 2, # part 2 "行くと"
                            "fullSentence": "交差点を 渡って まっすぐ ★行くと 右側に あります。",
                            "explain": "Thứ tự: 交差点を [1. 渡って] [3. まっすぐ] ★[2. 行くと] [4. 右側に] あります. Vị trí ★ là (2) 行くと."
                        },
                        {
                            "id": 30,
                            "type": "star",
                            "sentencePre": "わたしは",
                            "sentencePost": "ありません。",
                            "promptVi": "Tôi chưa từng đi Nhật Bản lần nào.",
                            "parts": [
                                {"id": 1, "text": "行った"},
                                {"id": 2, "text": "一度も"},
                                {"id": 3, "text": "ことが"},
                                {"id": 4, "text": "日本へ"}
                            ],
                            "fullOrder": [2, 4, 1, 3],
                            "starPos": 3,
                            "correctOption": 1, # part 1 "行った"
                            "fullSentence": "わたしは 一度も 日本へ ★行った ことが ありません。",
                            "explain": "Thứ tự: わたしは [2. 一度も] [4. 日本へ] ★[1. 行った] [3. ことが] ありません. Vị trí ★ là động từ thể Ta (1) 行った."
                        }
                    ]
                },
                {
                    "groupTitle": "DẠNG 3: Dịch câu (Tự luận)",
                    "groupInstruction": "Nhập bản dịch vào ô trống (chấp nhận cả Kanji lẫn Hiragana, không phân biệt dấu cách):",
                    "items": [
                        {
                            "id": 31,
                            "type": "trans",
                            "dir": "vi_to_ja",
                            "prompt": "Dịch sang tiếng Nhật: <br><strong style='color:#1e1b4b;'>「Tôi có thể nói được một chút tiếng Nhật.」</strong>",
                            "placeholder": "Nhập câu tiếng Nhật (Ví dụ: わたしは 日本語が 少し 話せます / 話す ことが できます)...",
                            "acceptable": [
                                "わたしは日本語が少し話せます",
                                "私は日本語が少し話せます",
                                "わたしは日本語を少し話すことができます",
                                "私は日本語を少し話すことができます",
                                "日本語が少し話せます",
                                "日本語をすこしはなすことができます",
                                "にほんごがすこしはなせます"
                            ],
                            "standard": "わたしは 日本語が 少し 話せます（または 日本語を 少し 話す ことが できます）。",
                            "explain": "Mẫu câu khả năng: ～が 話せます hoặc ～を 話す ことが できます. 少し (すこし - một chút)."
                        },
                        {
                            "id": 32,
                            "type": "trans",
                            "dir": "ja_to_vi",
                            "prompt": "Dịch sang tiếng Việt: <br><strong style='color:#1e1b4b;'>「休みの日は たいてい 家で 音楽を 聞きながら、本を 読みます。」</strong>",
                            "placeholder": "Nhập câu dịch tiếng Việt (Ví dụ: Vào ngày nghỉ tôi thường vừa nghe nhạc vừa đọc sách ở nhà)...",
                            "keywords": ["ngày nghỉ", "ở nhà", "nghe nhạc", "đọc sách", "vừa"],
                            "standard": "Vào ngày nghỉ tôi thường vừa nghe nhạc vừa đọc sách ở nhà.",
                            "explain": "Cấu trúc hành động đồng thời: V1 (bỏ masu) + ながら V2 (vừa làm V1 vừa làm V2)."
                        }
                    ]
                }
            ]
        },
        {
            "id": "sec4_reading",
            "partNumber": "IV",
            "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
            "partDesc": "Đọc lịch trình chuyến tham quan ngắm lá đỏ ở Nikko dưới đây và chọn đáp án chính xác nhất cho 2 câu hỏi (33 và 34).",
            "badge": "10 Điểm",
            "readingPassage": {
                "title": "【日光（にっこう）の 紅葉（こうよう）日帰りツアーの ご案内】",
                "content": "秋の 美しい 自然を 楽しむ「日光 紅葉ツアー」の お知らせです。\n日時は 10月25日（日曜日）です。朝7時30分に 新宿駅 西口に 集合して、専用の バスで 出発します。\n日光東照宮（にっこうとうしょうぐう）を 見学したり、華厳の滝（けごんのたき）の 近くで きれいな 紅葉を 見たり します。\n\nお昼ごはんは 日光の 有名な ゆば料理を 食べます。\n東京への 到着予定は 午後7時ごろです。\nツアーの 費用は 1人 8,500円（昼食代と バスの 交通費を 含む）です。\n山は 風が 強くて 寒いですから、暖かい 上着を 持って来て ください。\n定員は 30名です。お早めに お申し込み ください！",
                "translation": "【Thông báo Tour tham quan ngắm lá đỏ đi về trong ngày ở Nikko】\nThông báo về 'Tour ngắm lá đỏ Nikko' để tận hưởng thiên nhiên mùa thu tươi đẹp.\nThời gian: Chủ nhật ngày 25 tháng 10. Tập trung lúc 7 giờ 30 phút sáng tại Cổng Tây ga Shinjuku và khởi hành bằng xe buýt riêng.\nĐoàn sẽ tham quan đền Nikko Toshogu và ngắm lá đỏ tuyệt đẹp gần thác Kegon.\n\nBữa trưa đoàn sẽ thưởng thức món váng đậu Yuba nổi tiếng của Nikko.\nDự kiến về đến Tokyo vào khoảng 7 giờ tối.\nChi phí tour là 8.500 yên/người (đã bao gồm bữa trưa và tiền xe buýt).\nTrên núi gió to và trời lạnh nên xin quý khách hãy mang theo áo khoác ấm.\nSố lượng giới hạn 30 người. Xin vui lòng đăng ký sớm!"
            },
            "items": [
                {
                    "id": 33,
                    "type": "mc",
                    "prompt": "この ツアーの 集合時間と 場所は どこですか。",
                    "promptVi": "Thời gian và địa điểm tập trung của tour này là ở đâu?",
                    "options": [
                        "朝7時30分に、新宿駅の 西口です。",
                        "朝8時00分に、上野駅の 公園口です。",
                        "午後12時00分に、日光東照宮の 前です。",
                        "午後7時00分に、東京駅の 丸の内口です。"
                    ],
                    "correct": 0,
                    "explain": "Trong bài ghi rõ: 『朝7時30分に 新宿駅 西口に 集合して、専用の バスで 出発します。』 Phương án A chính xác."
                },
                {
                    "id": 34,
                    "type": "mc",
                    "prompt": "ツアーに ついて、正しい ものは どれですか。",
                    "promptVi": "Câu nào dưới đây là ĐÚNG về chuyến tour này?",
                    "options": [
                        "昼ごはん代は ツアーの 費用（8,500円）に 入って います。",
                        "お昼ごはんは 自分で 準備して 持って行かなければ なりません。",
                        "日光の 山は 暑いですから、薄い 服を 着て 行きます。",
                        "ツアーは 1泊2日で、日光の ホテルに 泊まります。"
                    ],
                    "correct": 0,
                    "explain": "Trong bài ghi: 『ツアーの 費用は 1人 8,500円（昼食代と バスの 交通費を 含む）』 (Bao gồm cả tiền ăn trưa và tiền xe). Do đó phương án A đúng."
                }
            ]
        },
        {
            "id": "sec5_essay",
            "partNumber": "V",
            "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
            "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (mỗi câu viết từ 2 đến 3 câu hoàn chỉnh).",
            "badge": "15 Điểm",
            "items": [
                {
                    "id": 35,
                    "type": "essay",
                    "prompt": "あなたの 国の おすすめの 観光地（かんこうち）について 紹介してください。（どこですか。何が 有名ですか。2〜3文で 書いてください）",
                    "promptVi": "Hãy giới thiệu về một địa điểm du lịch bạn yêu thích ở đất nước bạn (Ở đâu? Có gì nổi tiếng? Viết 2-3 câu tiếng Nhật)",
                    "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしのおすすめの観光地は ハロン湾です...)...",
                    "hints": [
                        "Địa điểm: わたしのおすすめは ～です / ～にあります",
                        "Nổi tiếng về: ～が 有名です / 自然が きれいです",
                        "Lời mời: ぜひ 一度 行ってみてください"
                    ],
                    "modelAnswer": "わたしのおすすめの 観光地は ベトナムの ハロン湾です。海と 島が とても きれいで、世界遺産（せかいいさん）です。船に 乗って、おいしい 魚を 食べることが できます。",
                    "modelVi": "Địa điểm du lịch tôi muốn giới thiệu là Vịnh Hạ Long của Việt Nam. Biển và các hòn đảo rất đẹp, là di sản thế giới. Bạn có thể đi thuyền và thưởng thức cá ngon.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Nêu rõ tên địa danh du lịch; nêu được điểm nổi bật thu hút du khách; ngữ pháp và trợ từ chuẩn xác."
                },
                {
                    "id": 36,
                    "type": "essay",
                    "prompt": "日本語の 勉強で、何が 一番 難しいですか。どうしてですか。（2〜3文で 書いてください）",
                    "promptVi": "Khi học tiếng Nhật, bạn thấy điều gì khó nhất? Vì sao? (Viết 2-3 câu bằng tiếng Nhật)",
                    "placeholder": "Gõ câu trả lời tiếng Nhật tại đây (Ví dụ: わたしは 漢字を 覚える ことが 一番 難しいです...)...",
                    "hints": [
                        "Cái khó nhất: ～が 一番 難しいです (漢字 / 文法 / 発音 / 聴解)",
                        "Lý do: 覚える ことが たくさん ありますから / 違いですから",
                        "Nỗ lực: ですから、毎日 練習して います"
                    ],
                    "modelAnswer": "わたしは 漢字を 覚える ことが 一番 難しいと 思います。形や 読み方が たくさん ありますから。でも、意味を 知ると とても 面白いです。",
                    "modelVi": "Tôi nghĩ việc nhớ chữ Hán là khó nhất. Vì có rất nhiều hình thái và cách đọc. Nhưng khi hiểu được ý nghĩa thì thấy rất thú vị.",
                    "rubric": "Tiêu chí chấm điểm Can-do: Biểu đạt rõ ràng quan điểm khó nhất (一番 難しい); đưa ra nguyên nhân thuyết phục bằng ～から; kết câu tự nhiên."
                }
            ]
        }
    ]
}

# Combine all 5 exams in order: M101, M102, M103, M104, M105
# Find M101 and M102 from BASE_EXAMS
m101 = next(e for e in BASE_EXAMS if e["code"] == "M101")
m102 = next(e for e in BASE_EXAMS if e["code"] == "M102")

EXAMS_DATA_5 = [m101, m102, M103, M104, M105]

print(f"Successfully compiled all 5 Midterm Exam Sets: {[e['code'] for e in EXAMS_DATA_5]}")
