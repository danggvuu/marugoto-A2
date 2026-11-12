#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_mini_test_11_14.py
Tạo trang web chuyên đề Ôn Tập Mini Test Bài 11 - 14 (Marugoto A2-1 & A2-2):
- Tab 1: 📖 Lý Thuyết Toàn Diện 4 Bài (Bài 11 ➔ 14)
- Tab 2: 🎴 118 Từ Vựng Chuẩn Kèm Nút Copy Quizlet Sạch & Ẩn Nghĩa
- Tab 3: ⛩️ 30 Chữ Hán Kanji (Chiết tự, Mẹo nhớ & Từ ghép)
- Tab 4: 🎯 ĐỀ THI THỬ ĐA DẠNG NĂNG LỰC (6 Dạng Bài • 32 Câu Chuẩn Sư Phạm 100 Điểm):
    + PHẦN I: Trắc Nghiệm Tổng Hợp Ngữ Pháp & Trợ Từ (10 Câu - 25 Điểm)
    + PHẦN II: Sắp Xếp Từ Thành Câu Hoàn Chỉnh ★ (5 Câu - 15 Điểm)
    + PHẦN III: Chia Dạng Đúng Của Từ Trong Ngoặc (5 Câu - 15 Điểm)
    + PHẦN IV: Nối Cột Tình Huống & Phản Xạ Công Sở (4 Câu - 10 Điểm)
    + PHẦN V: Đọc Hiểu Đoạn Văn Thực Tế (4 Câu / 2 Bài Đọc - 20 Điểm)
    + PHẦN VI: Luyện Dịch Câu Thực Chiến 2 Chiều (4 Câu - 15 Điểm)
- Tab 5: ⚡ Cẩm Nang Bỏ Túi (Cheat Sheet Tránh Bẫy Sư Phạm)
"""

import json
import os

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 1. Load Vocab
with open(os.path.join(WORKSPACE, 'data/master_vocab_official.json'), 'r', encoding='utf-8') as f:
    all_vocab = json.load(f)

vocab_11_14 = [w for w in all_vocab if w.get('l') in ['A2-11', 'A2-12', 'A2-13', 'A2-14']]

# 2. Load Kanji
with open(os.path.join(WORKSPACE, 'data/kanji_extracted.json'), 'r', encoding='utf-8') as f:
    all_kanji = json.load(f)

kanji_11_14 = [k for k in all_kanji if k.get('lesson') in ['L11', 'L12', 'L13', 'L14'] or k.get('lessonName') in ['Bài 11', 'Bài 12', 'Bài 13', 'Bài 14']]

KANJI_READINGS = {
    '酒': 'さけ',
    '作': 'つくる',
    '物': 'もの',
    '茶': 'おちゃ',
    '持': 'もつ',
    '願': 'ねがう',
    '料': 'りょう',
    '理': 'り',
    '味': 'あじ',
    '色': 'いろ',
    '野': 'の',
    '菜': 'さい',
    '少': 'すこし',
    '会': 'あう',
    '社': 'しゃ',
    '支': 'し',
    '張': 'ちょう',
    '空': 'そら',
    '港': 'みなと',
    '発': 'はつ',
    '着': 'つく',
    '午': 'ご',
    '自': 'じ',
    '分': 'ぶん',
    '電': 'でん',
    '話': 'はなす',
    '車': 'くるま',
    '送': 'おくる',
    '使': 'つかう',
    '借': 'かりる'
}

KANJI_SHORT_MEANINGS = {
    '酒': 'rượu, đồ uống có cồn',
    '作': 'làm, chế tạo, nấu nướng',
    '物': 'đồ vật, sự vật',
    '茶': 'trà, nước chè',
    '持': 'cầm, giữ, sở hữu',
    '願': 'cầu chúc, nhờ cậy',
    '料': 'nguyên liệu, tiền cước',
    '理': 'lý do, xử lý',
    '味': 'mùi vị, hương vị',
    '色': 'màu sắc',
    '野': 'cánh đồng, hoang dã',
    '菜': 'rau xanh',
    '少': 'ít ỏi, một chút',
    '会': 'gặp gỡ, tụ họp',
    '社': 'công ty, đền thờ',
    '支': 'chi nhánh, chống đỡ',
    '張': 'kéo căng, phồng to',
    '空': 'bầu trời, trống rỗng',
    '港': 'bến cảng, sân bay',
    '発': 'khởi hành, xuất phát',
    '着': 'đến nơi, mặc đồ',
    '午': 'buổi trưa, giờ ngọ',
    '自': 'tự mình, tự thân',
    '分': 'phân chia, phút',
    '電': 'điện lực, tia chớp',
    '話': 'nói chuyện, câu chuyện',
    '車': 'xe ô tô',
    '送': 'gửi đi, tiễn đưa',
    '使': 'dùng, sử dụng',
    '借': 'vay mượn'
}

for k in kanji_11_14:
    ch = k['char']
    k['hiragana'] = KANJI_READINGS.get(ch, (k.get('kun') or '').split('、')[0].replace('-', '').strip() or (k.get('on') or '').split('、')[0].replace('-', '').strip())
    k['shortMeaning'] = KANJI_SHORT_MEANINGS.get(ch, k.get('meaning', '').split(',')[0].strip())

# 3. Data for Part I: Multiple Choice (10 Questions - 25 pts)
PART1_MC = [
    {
        "id": 1,
        "category": "Bài 11 • Rủ rê",
        "q": "いい てんきですね。いっしょに こうえんへ [____]。",
        "options": ["行きます", "行きましょう", "行かない", "行った"],
        "correct": 1,
        "explain": "Rủ rê, đề xuất cùng làm gì ta dùng thể ý chí 「V-ましょう」 (Chúng ta cùng đi nhé)."
    },
    {
        "id": 2,
        "category": "Bài 11 • Trợ từ mang theo",
        "q": "バーベキューの とき、肉や やさい [____] 持って行きます。",
        "options": ["を", "に", "で", "へ"],
        "correct": 0,
        "explain": "Đồ vật mang theo là tân ngữ trực tiếp của động từ 「持っていきます」, dùng trợ từ 「を」."
    },
    {
        "id": 3,
        "category": "Bài 11 • Đề nghị giúp đỡ",
        "q": "荷物が 重そうですね。[____]か。",
        "options": ["持ちました", "持ってください", "持ちましょう", "持っています"],
        "correct": 2,
        "explain": "Khi chủ động ngỏ ý làm giúp đối phương việc gì đó, dùng 「V-ましょうか」 (Để tôi xách giúp bạn nhé?)."
    },
    {
        "id": 4,
        "category": "Bài 11 • Chọn món / Quyết định",
        "q": "A: 「何に しますか。」ー B: 「わたしは ラーメン [____] します。」",
        "options": ["を", "で", "が", "に"],
        "correct": 3,
        "explain": "Cấu trúc chọn món ăn, đồ uống hoặc đưa ra quyết định: 「N に します」."
    },
    {
        "id": 5,
        "category": "Bài 12 • Phán đoán diện mạo",
        "q": "この ケーキは とても [____] そうですね。",
        "options": ["おいし", "おいしい", "おいしくて", "おいしかった"],
        "correct": 0,
        "explain": "Tính từ đuôi い phán đoán vẻ ngoài: Bỏ đuôi 「い」 + 「そう」 (おいしい ➔ おいしそう)."
    },
    {
        "id": 6,
        "category": "Bài 12 • Biến đổi tính từ",
        "q": "レモンを 入れたので、スープが ちょっと [____] なりました。",
        "options": ["すっぱい", "すっぱく", "すっぱくて", "すっぱいに"],
        "correct": 1,
        "explain": "Tính từ đuôi い đi với なります: Bỏ 「い」 thay bằng 「く」 ➔ 「すっぱくなります」 (trở nên chua)."
    },
    {
        "id": 7,
        "category": "Bài 13 • Thể kinh nghiệm",
        "q": "今までに 飛行機に [____] ことが ありますか。",
        "options": ["乗った", "乗る", "乗って", "乗ります"],
        "correct": 0,
        "explain": "Cấu trúc nói về kinh nghiệm trong quá khứ bắt buộc dùng thể Ta: 「V-た ことが あります」."
    },
    {
        "id": 8,
        "category": "Bài 13 • Mức độ quá đà",
        "q": "この スーツは [____]、買うことが できません。",
        "options": ["高いすぎて", "高くて", "高だすぎて", "高すぎて"],
        "correct": 3,
        "explain": "Tính từ đuôi い bỏ đuôi 「い」 ghép với すぎて (dạng nối câu nguyên nhân): 「高すぎて」."
    },
    {
        "id": 9,
        "category": "Bài 14 • Xin phép lịch sự",
        "q": "すみません、この パソコンを [____] いいですか。",
        "options": ["使って", "使うと", "使っても", "使ったら"],
        "correct": 2,
        "explain": "Cấu trúc xin phép: 「V-ても いいですか」 (Tôi dùng cái này có được không?)."
    },
    {
        "id": 10,
        "category": "Bài 14 • Cấm đoán quy định",
        "q": "ここで たばこを 吸っても いいですか。ー すみません、ここでは [____]。",
        "options": ["吸ってもいいです", "吸ってください", "吸いました", "吸ってはいけません"],
        "correct": 3,
        "explain": "Quy tắc cấm đoán: 「V-ては いけません」 (Không được phép hút thuốc)."
    }
]

# 4. Data for Part II: Sentence Ordering (5 Questions - 15 pts)
PART2_ARRANGE = [
    {
        "id": 11,
        "category": "Bài 12 • So sánh phạm vi",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "日本の 料理の",
        "post": "好きです。",
        "chips": ["中で", "天ぷらが", "いちばん", "の"],
        "correctOrder": [3, 0, 1, 2], # [4, 1, 2, 3] in 1-based index: の (4) -> 中で (1) -> ★ 天ぷらが (2) -> いちばん (3)
        "starIndex": 2, # 3rd position in 4 blanks (0-based: 2) -> "天ぷらが" (index 1)
        "starChip": "天ぷらが",
        "fullSentence": "日本の 料理の の 中で、天ぷらが いちばん 好きです。",
        "simplifiedSentence": "日本の 料理の 中で、天ぷらが いちばん 好きです。",
        "explain": "Cấu trúc phạm vi: 「[Nhóm] の 中で、[A] が いちばん Adj です」. Thứ tự: [の] [中で] [★ 天ぷらが] [いちばん]."
    },
    {
        "id": 12,
        "category": "Bài 13 • Quá đà với động từ",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "きのうの パーティーで",
        "post": "すぎました。",
        "chips": ["お酒を", "ビールや", "たくさん", "飲み"],
        "correctOrder": [1, 0, 2, 3], # ビールや (2) -> お酒を (1) -> ★ たくさん (3) -> 飲み (4)
        "starIndex": 2,
        "starChip": "たくさん",
        "fullSentence": "きのうの パーティーで ビールや お酒を たくさん 飲みすぎました。",
        "explain": "Liệt kê 「A や B」 làm tân ngữ cho động từ 「飲みすぎました」. Thứ tự: [ビールや] [お酒を] [★ たくさん] [飲み] すぎました."
    },
    {
        "id": 13,
        "category": "Bài 13 • Phủ định thể kinh nghiệm",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "すしを",
        "post": "ありません。",
        "chips": ["一度も", "食べた", "ことが", "まだ"],
        "correctOrder": [1, 2, 0, 3], # 食べた (2) -> ことが (3) -> ★ 一度も (1) -> まだ (đối chiếu: 食べた ことが 一度も ありません)
        "starIndex": 2,
        "starChip": "一度も",
        "fullSentence": "すしを 食べた ことが 一度も ありません。",
        "explain": "Cấu trúc nhấn mạnh chưa từng làm bao giờ: 「V-た ことが 一度も ありません」. Vị trí ngôi sao là [一度も]."
    },
    {
        "id": 14,
        "category": "Bài 14 • Danh từ hóa cách dùng",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "すみません、この",
        "post": "教えてください。",
        "chips": ["使い方を", "コピー機の", "ちょっと", "わたしに"],
        "correctOrder": [1, 0, 2, 3], # コピー機の (2) -> 使い方を (1) -> ★ ちょっと (3) -> わたしに (hoặc ちょっと わたしに)
        "starIndex": 1,
        "starChip": "使い方を",
        "fullSentence": "すみません、この コピー機の 使い方を ちょっと 教えてください。",
        "explain": "Cụm danh từ cách làm: 「[Máy móc] の 使い方を 教えてください」. Vị trí ngôi sao là [使い方を]."
    },
    {
        "id": 15,
        "category": "Bài 14 • Mượn đồ đồng nghiệp",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "ペンを",
        "post": "借りました。",
        "chips": ["忘れたので", "同僚に", "黒い", "ペンを"],
        "correctOrder": [0, 1, 2, 3], # 忘れたので (1) -> 同僚に (2) -> ★ 黒い (3) -> ペンを (4)
        "starIndex": 2,
        "starChip": "黒い",
        "fullSentence": "ペンを 忘れたので、同僚に 黒い ペンを 借りました。",
        "explain": "Nguyên nhân 「〜ので」 + đối tượng mượn 「同僚に」 + tân ngữ 「黒い ペンを」. Vị trí ngôi sao là [黒い]."
    }
]

# 5. Data for Part III: Fill in Correct Conjugated Form (5 Questions - 15 pts)
PART3_CONJUGATE = [
    {
        "id": 16,
        "category": "Bài 13 • Động từ + すぎる",
        "sentence": "きのう ビールを (飲む) [_______] すぎて、きょう 頭が いたいです。",
        "baseWord": "飲む (のむ)",
        "accepted": ["飲み", "のみ", "nomi"],
        "displayAnswer": "飲み (のみ)",
        "explain": "Động từ kết hợp với 「すぎる」: Bỏ đuôi ます ➔ 飲みます ➔ <strong>飲み</strong>."
    },
    {
        "id": 17,
        "category": "Bài 13 • Tính từ đuôi na + すぎる",
        "sentence": "この 部屋は (静か) [_______] すぎて、ちょっと こわいです。",
        "baseWord": "静か (しずか)",
        "accepted": ["静か", "しずか", "shizuka"],
        "displayAnswer": "静か (しずか)",
        "explain": "Tính từ đuôi な kết hợp với 「すぎる」: Bỏ hẳn chữ な, tuyệt đối KHÔNG thêm だ ➔ <strong>静か</strong>すぎます."
    },
    {
        "id": 18,
        "category": "Bài 12 • Phán đoán diện mạo そう",
        "sentence": "この ケーキは とても (おいしい) [_______] そうですね。いっしょに 食べましょう。",
        "baseWord": "おいしい",
        "accepted": ["おいし", "oishi"],
        "displayAnswer": "おいし",
        "explain": "Tính từ đuôi い phán đoán vẻ ngoài: Bỏ đuôi 「い」 + そう ➔ <strong>おいし</strong>そう."
    },
    {
        "id": 19,
        "category": "Bài 13 • Thể kinh nghiệm たことがある",
        "sentence": "今までに 日本へ (行く) [_______] ことが ありますか。",
        "baseWord": "行く (いく)",
        "accepted": ["行った", "いった", "itta"],
        "displayAnswer": "行った (いった)",
        "explain": "Thể kinh nghiệm bắt buộc dùng động từ thể Ta: 行く ➔ <strong>行った</strong> ことが あります."
    },
    {
        "id": 20,
        "category": "Bài 14 • Danh từ hóa cách làm V-かた",
        "sentence": "この 漢字の (読む) [_______] 方を 教えてください。",
        "baseWord": "読む (よむ)",
        "accepted": ["読み", "よみ", "yomi"],
        "displayAnswer": "読み (よみ)",
        "explain": "Cách làm: Động từ bỏ ます + 方 (かた) ➔ 読みます ➔ <strong>読み</strong>方 (cách đọc)."
    }
]

# 6. Data for Part IV: Situation Matching (4 Questions - 10 pts)
PART4_MATCH = [
    {
        "id": 21,
        "category": "Bài 11 • Đề nghị giúp đỡ",
        "situation": "A: 「荷物が 重そうですね。持ちましょうか。」",
        "context": "(Thấy đối phương vác đồ nặng, ngỏ ý muốn xách giúp)",
        "options": [
            "「ありがとうございます。お願いします。」",
            "「ええ、どうぞ。」",
            "「すみません、ここでは 吸ってはいけません。」",
            "「いいえ、一度も ありません。」"
        ],
        "correct": 0,
        "explain": "Khi người khác đề nghị giúp đỡ, đáp lại lịch sự bằng lời cảm ơn và nhờ cậy: 「ありがとうございます。お願いします。」"
    },
    {
        "id": 22,
        "category": "Bài 14 • Xin phép cấp trên",
        "situation": "A: 「課長、この 資料を 見ても いいですか。」",
        "context": "(Cấp dưới hỏi xin phép xem tập tài liệu công ty)",
        "options": [
            "「ありがとうございます。お願いします。」",
            "「ええ、どうぞ。」",
            "「すみません、ここでは 吸ってはいけません。」",
            "「いいえ、一度も ありません。」"
        ],
        "correct": 1,
        "explain": "Khi cấp trên đồng ý cho phép cấp dưới xem tài liệu, dùng lời mời lịch sự: 「ええ、どうぞ。」 (Vâng, xin mời cứ xem)."
    },
    {
        "id": 23,
        "category": "Bài 14 • Cấm đoán quy định",
        "situation": "A: 「すみません、ここで たばこを 吸っても いいですか。」",
        "context": "(Khách hỏi xin hút thuốc lá ở nơi có biển cấm)",
        "options": [
            "「ありがとうございます。お願いします。」",
            "「ええ、どうぞ。」",
            "「すみません、ここでは 吸ってはいけません。」",
            "「いいえ、一度も ありません。」"
        ],
        "correct": 2,
        "explain": "Từ chối và nêu rõ quy định cấm hút thuốc: 「すみません、ここでは 吸っては いけません。」"
    },
    {
        "id": 24,
        "category": "Bài 13 • Hỏi về kinh nghiệm",
        "situation": "A: 「今までに 一人で 外国へ 行った ことが ありますか。」",
        "context": "(Hỏi xem bạn đã từng đi nước ngoài một mình bao giờ chưa)",
        "options": [
            "「ありがとうございます。お願いします。」",
            "「ええ、どうぞ。」",
            "「すみません、ここでは 吸ってはいけません。」",
            "「いいえ、一度も ありません。」"
        ],
        "correct": 3,
        "explain": "Phủ định thể kinh nghiệm chưa từng làm dù chỉ một lần: 「いいえ、一度も ありません。」"
    }
]

# 7. Data for Part V: Reading Comprehension (4 Questions / 2 Passages - 20 pts)
PART5_READING = [
    {
        "passageId": 1,
        "title": "BÀI ĐỌC 1: ピクニックの 計画 (Kế Hoạch Dã Ngoại Cuối Tuần - Bài 11 & 12)",
        "text": "今週の 日曜日に、クラスの みんなと こうえんへ ピクニックに 行きます。天気予報に よると、日曜日は いい 天気に なりそうです。<br>たなかさんは お弁当と おにぎりを 作って 持って行きます。スミスさんは くだものと お菓子を 買います。わたしは 飲み物を 準備します。みんなで おいしい 料理を 食べて、写真を たくさん 撮りましょう。",
        "questions": [
            {
                "id": 25,
                "q": "日曜日の 天気は どうですか。",
                "options": [
                    "雨が 降ります",
                    "いい 天気に なりそうです",
                    "とても 寒くなります",
                    "風が 強いです"
                ],
                "correct": 1,
                "explain": "Trong bài viết: 「天気予報に よると、日曜日は いい 天気に なりそうです」."
            },
            {
                "id": 26,
                "q": "たなかさんは 何を 準備して 持って行きますか。",
                "options": [
                    "くだものと お菓子",
                    "飲み物と ジュース",
                    "お弁当と おにぎり",
                    "カメラと パソコン"
                ],
                "correct": 2,
                "explain": "Trong bài viết: 「たなかさんは お弁当と おにぎりを 作って 持って行きます」."
            }
        ]
    },
    {
        "passageId": 2,
        "title": "BÀI ĐỌC 2: 初めての 東京出張 (Chuyến Đi Công Tác Tokyo Đầu Tiên - Bài 13 & 14)",
        "text": "わたしは 先週、仕事で 初めて 東京へ 出張しました。今までに 一度も 飛行機に 乗った ことが ありませんでしたから、少し きんちょうしました。<br>東京で 取引先の 山田さんに 会って、いっしょに 会議を しました。夜、山田さんと レストランへ 行って、日本料理を 食べました。天ぷらが とても おいしかったので、食べすぎて しまいました。<br>次の日は 会社で コピー機の 使い方や パソコンの ルールを 教えてもらいました。とても いい 経験に なりました。",
        "questions": [
            {
                "id": 27,
                "q": "マイさんは どうして 飛行機に 乗る とき、きんちょうしましたか。",
                "options": [
                    "飛行機が きらいだから",
                    "今までに 一度も 飛行機に 乗った ことが なかったから",
                    "荷物が 重すぎたから",
                    "時間が なかったから"
                ],
                "correct": 1,
                "explain": "Trong bài viết: 「今までに 一度も 飛行機に 乗った ことが ありませんでしたから、少し きんちょうしました」."
            },
            {
                "id": 28,
                "q": "マイさんは レストランで どうして 料理を 食べすぎて しまいましたか。",
                "options": [
                    "お腹が とても すいていたから",
                    "天ぷらが とても おいしかったから",
                    "料理が 安かったから",
                    "山田さんに たくさん もらったから"
                ],
                "correct": 1,
                "explain": "Trong bài viết: 「天ぷらが とても おいしかったので、食べすぎて しまいました」."
            }
        ]
    }
]

# 8. Data for Part VI: Sentence Translation (4 Questions - 15 pts)
PART6_TRANSLATION = [
    {
        "id": 29,
        "category": "Bài 13 • Thể kinh nghiệm quá khứ",
        "vi": "Tôi đã từng bơi một mình ở biển vào ban đêm.",
        "hint": "夜 (よる), 一人で (ひとりで), 海 (うみ), 泳ぎます (およぎます ➔ およいだ)",
        "modelSentence": "わたしは 夜、一人で 海で 泳いだ ことが あります。",
        "modelKana": "わたしは よる、ひとりで うみで およいだ ことがあります。",
        "keywords": ["夜", "一人で", "海", "泳いだ", "こと", "あります"],
        "breakdown": [
            {"part": "夜 (よる)", "role": "Thời gian (ban đêm)"},
            {"part": "一人で (ひとりで)", "role": "Phương thức (một mình)"},
            {"part": "海で (うみで)", "role": "Địa điểm hành động (ở biển - trợ từ で)"},
            {"part": "泳いだ ことが あります", "role": "Thể kinh nghiệm V-た ことが あります"}
        ]
    },
    {
        "id": 30,
        "category": "Bài 13 • Mức độ quá đà với tính từ",
        "vi": "Bộ vest này đẹp nhưng mà đắt quá đi.",
        "hint": "スーツ, きれい (tính từ đuôi な), 高い (たかい ➔ たかすぎます)",
        "modelSentence": "この スーツは きれいだけど、高すぎます。",
        "modelKana": "この すーつは きれいだけど、たかすぎます。",
        "keywords": ["スーツ", "きれい", "だけど", "高すぎ"],
        "breakdown": [
            {"part": "この スーツは", "role": "Chủ ngữ (bộ vest này)"},
            {"part": "きれいだけど", "role": "Tính từ đuôi な nối tương phản (hoặc きれいですが)"},
            {"part": "高すぎます", "role": "Tính từ đuôi い bỏ い + すぎます (đắt quá)"}
        ]
    },
    {
        "id": 31,
        "category": "Bài 13 • Quá đà chỉ nguyên nhân",
        "vi": "Vì căn phòng này quá yên tĩnh, nên hơi đáng sợ.",
        "hint": "部屋 (へや), 静か (しずか - tính từ đuôi な), こわい (đáng sợ)",
        "modelSentence": "この 部屋は 静かすぎて、ちょっと こわいです。",
        "modelKana": "この へやは しずかすぎて、ちょっと こわいです。",
        "keywords": ["部屋", "静かすぎ", "ちょっと", "こわい"],
        "breakdown": [
            {"part": "この 部屋は", "role": "Chủ ngữ (căn phòng này)"},
            {"part": "静かすぎて", "role": "Tính từ đuôi な bỏ な + すぎて chỉ nguyên nhân (quá yên tĩnh nên...)"},
            {"part": "ちょっと こわいです", "role": "Hơi đáng sợ"}
        ]
    },
    {
        "id": 32,
        "category": "Bài 13 & Bài 11 • Nấu quá nhiều đồ ăn",
        "vi": "Vì nấu quá nhiều món ăn, nên tôi đã không thể ăn hết một mình.",
        "hint": "料理 (りょうり), 作りすぎました (つくりすぎました), 一人で, 全部 (ぜんぶ)",
        "modelSentence": "料理を 作りすぎたので、一人で 全部 食べられませんでした。",
        "modelKana": "りょうりを つくりすぎたので、ひとりで ぜんぶ たべられませんでした。",
        "keywords": ["料理", "作りすぎ", "一人で", "食べられません"],
        "breakdown": [
            {"part": "料理を 作りすぎたので", "role": "Động từ bỏ ます + すぎたので (vì đã nấu quá nhiều món)"},
            {"part": "一人で", "role": "Một mình"},
            {"part": "全部 食べられませんでした", "role": "Không thể ăn hết (hoặc 食べきれませんでした)"}
        ]
    }
]

# Build JSON Data Strings
vocab_json_str = json.dumps(vocab_11_14, ensure_ascii=False)
kanji_json_str = json.dumps(kanji_11_14, ensure_ascii=False)
p1_json_str = json.dumps(PART1_MC, ensure_ascii=False)
p2_json_str = json.dumps(PART2_ARRANGE, ensure_ascii=False)
p3_json_str = json.dumps(PART3_CONJUGATE, ensure_ascii=False)
p4_json_str = json.dumps(PART4_MATCH, ensure_ascii=False)
p5_json_str = json.dumps(PART5_READING, ensure_ascii=False)
p6_json_str = json.dumps(PART6_TRANSLATION, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Cẩm Nang Toàn Diện & Đề Thi Thử Đa Dạng Bài 11 - 14 (Marugoto A2-1 & A2-2)</title>
    <meta name="description" content="Chuyên đề ôn tập và đề thi thử đa dạng 6 phần: Trắc nghiệm, Sắp xếp câu, Chia thể, Nối cột hội thoại, Đọc hiểu đoạn văn và Luyện dịch câu 100 điểm.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="../assets/js/audio-engine.js?v=2"></script>
    <link rel="stylesheet" href="../assets/css/mini-test-11-14.css?v=1">
</head>
<body>

<div class="container">

    <!-- Global Hub Navigation -->
    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="../the_ta.html" class="hub-nav-item">📕 Thể TA (Quá Khứ)</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="../Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="../kien_thuc_bo_sung.html" class="hub-nav-item">💡 Kiến Thức Bổ Sung</a>
        <a href="../demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item active-hub" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                <!-- Sync script will populate -->
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                <!-- Sync script will populate -->
            </div>
        </div>
    </div>

    <!-- Hero Header -->
    <header class="hero-header">
        <div class="hero-badge">⚡ Chuyên Đề Trọng Tâm Toàn Diện • Marugoto A2-1 & A2-2</div>
        <h1 class="hero-title">🎯 Cẩm Nang & Đề Thi Thử Đa Dạng Bài 11 - 14</h1>
        <p class="hero-desc">Hệ thống khảo sát toàn diện năng lực qua 6 dạng bài thực chiến: Trắc nghiệm lựa chọn, Sắp xếp câu ★, Chia thể & Điền khuyết, Nối cột phản xạ, Đọc hiểu đoạn văn và Luyện dịch câu 2 chiều chuẩn 100 điểm.</p>
        <div class="hero-stats">
            <div class="stat-pill">📚 4 Bài Học Trọng Tâm (11 ➔ 14)</div>
            <div class="stat-pill">🎴 118 Từ Vựng Kèm Quizlet</div>
            <div class="stat-pill">⛩️ 30 Chữ Hán Chiết Tự</div>
            <div class="stat-pill">🎯 6 Dạng Bài • 32 Câu (Thang Điểm 100)</div>
        </div>
        <div style="margin-top: 18px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
            <button type="button" class="btn-quizlet" onclick="copyFullQuizletFormat()" style="padding: 10px 18px; font-size: 0.9rem;" title="Dạng gõ siêu mượt trên Quizlet: くだもの [Tab] Hoa quả">
                📋 Copy Gõ Kana (Tab): くだもの [Tab] Hoa quả
            </button>
            <button type="button" class="btn-quizlet" onclick="copyFullColonFormat()" style="background: linear-gradient(135deg, #059669, #10b981); padding: 10px 18px; font-size: 0.9rem;" title="Dạng dấu hai chấm: くだもの：Hoa quả">
                📋 Copy Dấu (：): くだもの：Hoa quả
            </button>
            <button type="button" class="btn-quizlet" onclick="copyFullCombinedFormat()" style="background: linear-gradient(135deg, #7c3aed, #9333ea); padding: 10px 18px; font-size: 0.9rem;" title="Dạng chuẩn Quizlet Pro: 果物 [Tab] [くだもの] Hoa quả">
                🎴 Copy Kèm Kanji: 果物 [Tab] [くだもの] Hoa quả
            </button>
            <button type="button" class="btn-quizlet" onclick="copyKanjiColonFormat()" style="background: linear-gradient(135deg, #d97706, #f59e0b); padding: 10px 18px; font-size: 0.9rem;" title="Copy 30 chữ Hán định dạng: 車、xe ô tô, XA: くるま">
                ⛩️ Copy Kanji: 車、xe ô tô, XA: くるま
            </button>
            <button type="button" class="btn-quizlet" onclick="copyKanjiQuizletTabFormat()" style="background: linear-gradient(135deg, #0284c7, #06b6d4); padding: 10px 18px; font-size: 0.9rem;" title="Copy 30 chữ Hán Tab cho Quizlet: [車、xe ô tô, XA] [Tab] [くるま]">
                ⛩️ Copy Kanji Quizlet (Tab)
            </button>
        </div>
    </header>

    <!-- Sticky Tab Navigation -->
    <div class="tab-nav-wrapper">
        <nav class="tab-nav">
            <button class="tab-btn active" onclick="switchMainTab('tab-theory')">📖 Lý Thuyết (Bài 11 - 14)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-vocab')">🎴 118 Từ Vựng</button>
            <button class="tab-btn" onclick="switchMainTab('tab-kanji')">⛩️ 30 Chữ Hán</button>
            <button class="tab-btn" onclick="switchMainTab('tab-quiz')">🎯 Đề Thi Thử Đa Dạng (6 Dạng • 100đ)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-cheatsheet')">⚡ Cẩm Nang Bỏ Túi</button>
            <a href="On_Tap_Mini_Test_A2_15_18.html#typing" class="tab-btn" style="text-decoration:none; background:#fffbeb; color:#b45309; border-color:#fcd34d;">⌨️ Luyện Gõ L11–18 &amp; Kanji PDF ➔</a>
        </nav>
    </div>

    <!-- ========================================== -->
    <!-- TAB 1: LÝ THUYẾT NGỮ PHÁP (BÀI 11 - 14)    -->
    <!-- ========================================== -->
    <div id="tab-theory" class="tab-panel active">

        <!-- Quick Jump Bar -->
        <div class="theory-quicknav">
            <a href="#grammar-l11" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">🍱 Bài 11: ピクニック (～ましょう／に します)</a>
            <a href="#grammar-l12" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">🍜 Bài 12: 日本料理 (～そう／～くなる)</a>
            <a href="#grammar-l13" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">✈️ Bài 13: 出張 (～たことがある／～すぎる)</a>
            <a href="#grammar-l14" class="quicknav-pill" style="background: var(--primary); color: white; border-color: var(--primary);">💻 Bài 14: 会社で (～てもいい／～かた)</a>
        </div>

        <!-- BÀI 11 -->
        <div class="grammar-card" id="grammar-l11">
            <div class="grammar-header">
                <div>
                    <span class="grammar-tag">BÀI 11 (A2-1)</span>
                    <h2 class="grammar-title">ピクニック (Dã Ngoại • Rủ Rê, Đề Nghị Giúp & Quyết Định Chọn Món)</h2>
                </div>
                <span class="section-badge">Trọng điểm A2-1</span>
            </div>
            <div class="grammar-body">
                <div class="formula-box">
                    1. Rủ rê / Đề xuất: <code>V(bỏ ます) ＋ ましょう</code><br>
                    2. Đề nghị giúp đỡ đối phương: <code>V(bỏ ます) ＋ ましょうか</code><br>
                    3. Mang theo đồ đạc / Dẫn ai đi: <code>[Danh từ] を 持って行きます / 連れて行きます</code><br>
                    4. Đưa ra lựa chọn, quyết định: <code>[Danh từ] に します</code>
                </div>
                <p class="grammar-explain">
                    <strong>Phân tích chi tiết:</strong><br>
                    • <code>〜ましょう</code>: Lời rủ rê chủ động, quả quyết khi cùng đưa ra đề xuất hành động chung.<br>
                    • <code>〜ましょうか</code>: Dùng khi ta thấy đối phương đang gặp khó khăn (vác nặng, trời nóng, cần chụp ảnh) và mình chủ động ngỏ lời làm hộ.<br>
                    • <code>〜に します</code>: Mẫu câu kinh điển dùng trong nhà hàng khi nhân viên hỏi <em>「ご注文は？」</em> hoặc khi ta chốt hạ một lựa chọn.
                </p>
                <ul class="example-list">
                    <li class="example-item">
                        <div class="ex-jp jp-text">いい てんきですね。いっしょに こうえんへ <span style="color: var(--primary);">行きましょう</span>。</div>
                        <div class="ex-vi">Thời tiết đẹp quá nhỉ. Chúng mình cùng đi ra công viên nhé!</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">荷物が 重そうですね。<span style="color: var(--primary);">持ちましょうか</span>。</div>
                        <div class="ex-vi">Hành lý trông có vẻ nặng quá. Để tôi xách giúp bạn nhé?</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">バーベキューの とき、肉や やさい<span style="color: var(--primary);">を</span> 持って行きます。</div>
                        <div class="ex-vi">Khi đi tiệc nướng dã ngoại BBQ, tôi sẽ mang theo thịt và rau xanh.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">A: 「何に しますか。」ー B: 「わたしは ラーメン<span style="color: var(--primary);">に します</span>。」</div>
                        <div class="ex-vi">A: Bạn chọn món gì? - B: Tôi quyết định chọn món mì ramen.</div>
                    </li>
                </ul>
                <div class="trap-box">
                    <strong>⚠️ Bẫy thi cần chú ý:</strong>
                    Tránh nhầm lẫn giữa <code>〜ましょう</code> (mình và bạn cùng làm) với <code>〜ましょうか</code> (để một mình tôi làm giúp bạn). Khi người khác đề nghị giúp bằng <code>〜ましょうか</code>, nếu đồng ý hãy đáp: <em>「ありがとうございます。お願いします」</em>, nếu từ chối khéo léo đáp: <em>「いいえ、大丈夫です」</em>.
                </div>
            </div>
        </div>

        <!-- BÀI 12 -->
        <div class="grammar-card" id="grammar-l12">
            <div class="grammar-header">
                <div>
                    <span class="grammar-tag">BÀI 12 (A2-1)</span>
                    <h2 class="grammar-title">特別な日の料理 (Ẩm Thực • Phán Đoán Bề Ngoài, Biến Đổi Tính Từ & So Sánh)</h2>
                </div>
                <span class="section-badge">Trọng điểm A2-1</span>
            </div>
            <div class="grammar-body">
                <div class="formula-box">
                    1. Phán đoán diện mạo bề ngoài: <code>Adj-i (bỏ い) / Adj-na (bỏ な) ＋ そうです</code><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;⭐ Ngoại lệ đặc biệt: <code>いい ➔ よさそう</code>, <code>ない ➔ なさそう</code><br>
                    2. Biến đổi trạng thái: <code>Adj-i (bỏ い) ＋ くなります</code> / <code>Adj-na (bỏ な) ＋ になります</code><br>
                    3. So sánh trong phạm vi: <code>[Nhóm / Phạm vi] の 中で、[A] が いちばん Adj です</code>
                </div>
                <p class="grammar-explain">
                    <strong>Phân tích chi tiết:</strong><br>
                    • <code>〜そう</code>: Dùng trực giác, thị giác nhìn bề ngoài để ước lượng tính chất sự vật. Nhìn thấy món ăn bắt mắt thì thốt lên <em>「おいしそう！」</em> chứ chưa nếm thử. Nếu đã ăn rồi thì phải dùng trực tiếp tính từ <em>「おいしいです」</em>.<br>
                    • <code>〜くなります / になります</code>: Diễn tả sự biến đổi bản chất hay mùi vị theo thời gian hoặc tác động bên ngoài (thêm chanh súp chua đi, lớn lên giỏi giang hơn).<br>
                    • <code>〜の中で</code>: Luôn nhớ trợ từ <code>で</code> sau danh từ chỉ phạm vi (trong ẩm thực Nhật, trong gia đình, trong 4 mùa).
                </p>
                <ul class="example-list">
                    <li class="example-item">
                        <div class="ex-jp jp-text">この ケーキは とても <span style="color: var(--primary);">おいしそう</span>ですね。</div>
                        <div class="ex-vi">Chiếc bánh ngọt này trông có vẻ ngon mắt quá nhỉ.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">この 辞書は とても <span style="color: var(--primary);">よさそう</span>です。(いい ➔ よさそう)</div>
                        <div class="ex-vi">Quyển từ điển này trông có vẻ rất tốt và hữu ích đấy.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">レモンを 入れたので、スープが ちょっと <span style="color: var(--primary);">すっぱく なりました</span>。</div>
                        <div class="ex-vi">Vì cho thêm chanh vào nên bát súp đã trở nên hơi chua một chút.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">日本の 料理<span style="color: var(--primary);">の 中で</span>、天ぷらが いちばん 好きです。</div>
                        <div class="ex-vi">Trong số các món ăn của Nhật Bản, tôi thích nhất là món Tempura.</div>
                    </li>
                </ul>
                <div class="trap-box">
                    <strong>⚠️ Bẫy thi cần chú ý:</strong>
                    1. Tuyệt đối KHÔNG giữ lại đuôi <code>い</code>: ❌ <code>おいしいそう</code> (Sai!), chỉ dùng <code>おいしそう</code> (Đúng!).<br>
                    2. Từ <code>いい</code> biến thành <code>よさそう</code>, không bao giờ có <code>いいそう</code>!<br>
                    3. Đuôi な bỏ hẳn chữ な: <code>にぎやかそう</code> chứ không phải <code>にぎやかなそう</code>.
                </div>
            </div>
        </div>

        <!-- BÀI 13 -->
        <div class="grammar-card" id="grammar-l13">
            <div class="grammar-header">
                <div>
                    <span class="grammar-tag">BÀI 13 (A2-2)</span>
                    <h2 class="grammar-title">出張 (Chuyến Đi Công Tác • Thể Kinh Nghiệm & Mức Độ Quá Đà)</h2>
                </div>
                <span class="section-badge">Trọng điểm A2-2</span>
            </div>
            <div class="grammar-body">
                <div class="formula-box">
                    1. Thể kinh nghiệm: <code>V-た ことが あります</code> (Đã từng...)<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;Phủ định tuyệt đối: <code>いいえ、一度も ありません</code> (Chưa từng một lần nào)<br>
                    2. Mức độ quá đà: <code>V(bỏ ます) / Adj-i(bỏ い) / Adj-na(bỏ な) ＋ すぎます</code><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;Nối câu nguyên nhân: <code>〜すぎて、[kết quả tiêu cực]</code><br>
                    3. Trợ từ gặp gỡ & công tác: <code>[Người] に 会います</code>, <code>[Địa điểm] へ 出張します</code>
                </div>
                <p class="grammar-explain">
                    <strong>Phân tích chi tiết:</strong><br>
                    • <code>V-た ことがある</code>: Dùng động từ thể TA để kể về một trải nghiệm đặc biệt đã từng kinh qua trong đời, không dùng cho các thói quen hàng ngày.<br>
                    • <code>〜すぎる</code>: Mang sắc thái tiêu cực (vượt quá ngưỡng cho phép, gây hậu quả xấu). Ăn nhiều quá đau bụng, vest đắt quá không mua nổi, phòng yên tĩnh quá phát sợ.<br>
                    • Đi công tác tới đâu dùng trợ từ <code>へ / に</code>, gặp gỡ ai đó bắt buộc dùng trợ từ <code>に</code>.
                </p>
                <ul class="example-list">
                    <li class="example-item">
                        <div class="ex-jp jp-text">今までに 飛行機に <span style="color: var(--primary);">乗った ことが ありますか</span>。</div>
                        <div class="ex-vi">Từ trước tới nay bạn đã từng đi máy bay bao giờ chưa?</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">すしを 食べたことが ありますか。ー いいえ、<span style="color: var(--primary);">一度も ありません</span>。</div>
                        <div class="ex-vi">Bạn đã từng ăn sushi bao giờ chưa? - Dạ chưa, một lần cũng chưa từng ăn ạ.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">きのうの パーティーで ビールを <span style="color: var(--primary);">飲みすぎました</span>。</div>
                        <div class="ex-vi">Trong bữa tiệc tối hôm qua, tôi đã lỡ uống quá chén (uống quá nhiều bia).</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">この スーツは <span style="color: var(--primary);">高すぎて</span>、買うことが できません。</div>
                        <div class="ex-vi">Bộ vest này đắt quá đi, nên tôi không tài nào mua nổi.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">この 部屋は <span style="color: var(--primary);">静かすぎて</span>、ちょっと こわいです。</div>
                        <div class="ex-vi">Căn phòng này yên tĩnh quá mức, thành ra hơi đáng sợ.</div>
                    </li>
                </ul>
                <div class="trap-box">
                    <strong>⚠️ Bẫy thi cần chú ý:</strong>
                    1. <code>静かすぎる</code>: Tính từ đuôi な ghép với すぎる tuyệt đối BỎ CHỮ な, KHÔNG THÊM だ (Cấm viết: <code>静かだすぎる</code> ❌, <code>静かなすぎる</code> ❌).<br>
                    2. Khi trả lời "chưa từng", chọn ngay <code>一度もありません</code>, không chọn <code>まだあります</code> ❌.
                </div>
            </div>
        </div>

        <!-- BÀI 14 -->
        <div class="grammar-card" id="grammar-l14">
            <div class="grammar-header">
                <div>
                    <span class="grammar-tag">BÀI 14 (A2-2)</span>
                    <h2 class="grammar-title">職場 (Môi Trường Công Sở • Xin Phép, Cấm Đoán & Cách Sử Dụng)</h2>
                </div>
                <span class="section-badge">Trọng điểm A2-2</span>
            </div>
            <div class="grammar-body">
                <div class="formula-box">
                    1. Xin phép lịch sự: <code>V-て ＋ も いいですか</code> (Tôi làm... có được không?)<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;Đồng ý cho phép: <code>ええ、どうぞ</code> / <code>いいですよ</code><br>
                    2. Cấm đoán quy định: <code>V-て ＋ は いけません</code> (Không được phép làm...)<br>
                    3. Cách làm (Danh từ hóa): <code>V(bỏ ます) ＋ 方 (かた)</code><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;⭐ Trợ từ chuyển đổi: <code>[N] を V ➔ [N] の V-かた</code><br>
                    4. Phép tắc mượn đồ: <code>[Người] に [Đồ vật] を 借ります (mượn của ai)</code>
                </div>
                <p class="grammar-explain">
                    <strong>Phân tích chi tiết:</strong><br>
                    • <code>V-てもいいですか</code>: Cấu trúc hỏi xin ý kiến cấp trên hay đồng nghiệp trước khi dùng đồ cơ quan. Khi được đồng ý, người Nhật thường dùng phó từ <code>どうぞ</code> (xin mời).<br>
                    • <code>V-てはいけません</code>: Quy tắc bắt buộc, cấm hút thuốc, cấm chụp ảnh, cấm làm ồn nơi công cộng.<br>
                    • <code>V-かた</code>: Động từ bỏ ます kết hợp với chữ Hán 方 (Phương) để biến thành danh từ chỉ cách thức thao tác. Trợ từ tân ngữ <code>を</code> biến thành <code>の</code>: <em>コピー機<span style="color:red">の</span> 使い方</em>.
                </p>
                <ul class="example-list">
                    <li class="example-item">
                        <div class="ex-jp jp-text">すみません、この パソコンを <span style="color: var(--primary);">使っても いいですか</span>。</div>
                        <div class="ex-vi">Xin lỗi, tôi dùng chiếc máy vi tính này có được không ạ?</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">ここで たばこを 吸っては <span style="color: var(--primary);">いけません</span>。</div>
                        <div class="ex-vi">Không được phép hút thuốc lá ở khu vực này.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">すみません、この コピー機の <span style="color: var(--primary);">使い方</span>を 教えてください。</div>
                        <div class="ex-vi">Xin lỗi, hãy chỉ giúp tôi cách sử dụng chiếc máy photocopy này với ạ.</div>
                    </li>
                    <li class="example-item">
                        <div class="ex-jp jp-text">ペンを 忘れましたから、同僚に ペンを <span style="color: var(--primary);">借りました</span>。</div>
                        <div class="ex-vi">Vì để quên bút nên tôi đã mượn bút từ người đồng nghiệp.</div>
                    </li>
                </ul>
                <div class="trap-box">
                    <strong>⚠️ Bẫy thi cần chú ý:</strong>
                    Phân biệt rõ: <code>借ります (かります)</code> là mình mượn của người khác (nhận về); còn <code>貸します (かします)</code> là mình đem đồ của mình cho người khác mượn (đưa đi).
                </div>
            </div>
        </div>

    </div>

    <!-- ========================================== -->
    <!-- TAB 2: KHO TỪ VỰNG (118 TỪ BÀI 11 - 14)    -->
    <!-- ========================================== -->
    <div id="tab-vocab" class="tab-panel">
        <div class="toolbar-card">
            <div class="filter-row">
                <span style="font-size: 0.85rem; font-weight: 800; color: var(--gray-600); margin-right: 4px;">CHỌN BÀI:</span>
                <button class="filter-btn active" onclick="filterVocab('ALL', this)">🌟 Tất Cả (118 từ Bài 11-14)</button>
                <button class="filter-btn" onclick="filterVocab('A2-11', this)">Bài 11 (27 từ)</button>
                <button class="filter-btn" onclick="filterVocab('A2-12', this)">Bài 12 (31 từ)</button>
                <button class="filter-btn" onclick="filterVocab('A2-13', this)">Bài 13 (35 từ)</button>
                <button class="filter-btn" onclick="filterVocab('A2-14', this)">Bài 14 (25 từ)</button>
            </div>
            <div class="action-row">
                <div class="search-input-box">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="vocabSearchInput" placeholder="Tìm kiếm từ vựng (Nhật, Hiragana, Hán Việt, tiếng Việt)..." oninput="handleVocabSearch()">
                </div>
                <button class="tool-toggle-btn" id="hideMeaningBtn" onclick="toggleHideMeaning()">
                    👁️ Ẩn nghĩa tiếng Việt (Tự dò)
                </button>
                <button type="button" class="btn-quizlet" id="btnQuizletCopy" onclick="copyVocabQuizletFormat()" title="Định dạng Tab sạch 100%, gõ siêu mượt trên Quizlet: くだもの [Tab] Hoa quả">
                    📋 Copy Gõ Kana (<span id="quizletVocabCount">118</span> từ)
                </button>
                <button type="button" class="btn-quizlet" onclick="copyVocabColonFormat()" style="background: linear-gradient(135deg, #059669, #10b981);" title="Định dạng dấu hai chấm: くだもの：Hoa quả">
                    📋 Copy Dấu (：)
                </button>
                <button type="button" class="btn-quizlet" onclick="copyVocabCombinedFormat()" style="background: linear-gradient(135deg, #7c3aed, #9333ea);" title="Dạng chuẩn Quizlet Pro: 果物 [Tab] [くだもの] Hoa quả">
                    🎴 Copy Kèm Kanji (Tab)
                </button>
            </div>
        </div>

        <div class="vocab-grid" id="vocabContainer">
            <!-- Render via JS -->
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 3: 30 CHỮ HÁN KANJI TRỌN BỘ            -->
    <!-- ========================================== -->
    <div id="tab-kanji" class="tab-panel">
        <div class="toolbar-card">
            <div class="filter-row">
                <span style="font-size: 0.85rem; font-weight: 800; color: var(--gray-600); margin-right: 4px;">CHỌN BÀI:</span>
                <button class="filter-btn active" onclick="filterKanji('ALL', this)">⛩️ Tất Cả (30 Chữ Hán Bài 11-14)</button>
                <button class="filter-btn" onclick="filterKanji('L11', this)">Bài 11 (6 chữ)</button>
                <button class="filter-btn" onclick="filterKanji('L12', this)">Bài 12 (7 chữ)</button>
                <button class="filter-btn" onclick="filterKanji('L13', this)">Bài 13 (9 chữ)</button>
                <button class="filter-btn" onclick="filterKanji('L14', this)">Bài 14 (8 chữ)</button>
            </div>
            <div class="action-row">
                <div class="search-input-box">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="kanjiSearchInput" placeholder="Tìm theo chữ Hán, Hán Việt, cách đọc On/Kun..." oninput="handleKanjiSearch()">
                </div>
                <button type="button" class="btn-quizlet" onclick="copyKanjiColonFormat()" style="background: linear-gradient(135deg, #059669, #10b981);" title="Copy toàn bộ 30 chữ theo định dạng: 車、xe ô tô, XA: くるま">
                    📋 Copy (車、xe ô tô, XA: くるま)
                </button>
                <button type="button" class="btn-quizlet" onclick="copyKanjiQuizletTabFormat()" title="Copy định dạng Tab cho Quizlet: [車、xe ô tô, XA] [Tab] [くるま]">
                    📋 Copy Quizlet (Tab)
                </button>
            </div>
        </div>

        <div class="kanji-grid" id="kanjiContainer">
            <!-- Render via JS -->
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: ĐỀ THI THỬ ĐA DẠNG NĂNG LỰC (100Đ)  -->
    <!-- ========================================== -->
    <div id="tab-quiz" class="tab-panel">

        <div class="quiz-stats-card">
            <div class="quiz-score-box">
                <div class="score-circle">
                    <span class="score-num" id="totalScoreDisplay">0</span>
                    <span class="score-max">/100 ĐIỂM</span>
                </div>
                <div class="score-info">
                    <h4 id="quizStatusTitle">Đề Khảo Sát Năng Lực Toàn Diện Bài 11 - 14</h4>
                    <p id="quizProgressText">Hoàn thành: 0/32 câu • Tổng điểm hiện tại: 0 / 100đ</p>
                </div>
            </div>
            <div class="quiz-action-btns">
                <div class="timer-badge">
                    ⏱️ <span id="timerText">45:00</span>
                </div>
                <button class="quiz-btn" onclick="toggleTimer()">⏸️ Tạm Dừng</button>
                <button class="quiz-btn primary" onclick="resetAllExam()">🔄 Làm Lại Đề Thi</button>
            </div>
        </div>

        <!-- Quick Jump Bar Between 6 Parts -->
        <div class="theory-quicknav" style="margin-bottom: 25px;">
            <a href="#sec-part1" class="quicknav-pill" style="background: #eef2ff; color: #4338ca; border-color: #c7d2fe;">I. Trắc Nghiệm (10 Câu • 25đ)</a>
            <a href="#sec-part2" class="quicknav-pill" style="background: #fef3c7; color: #b45309; border-color: #fde68a;">II. Sắp Xếp Câu ★ (5 Câu • 15đ)</a>
            <a href="#sec-part3" class="quicknav-pill" style="background: #d1fae5; color: #047857; border-color: #a7f3d0;">III. Chia Dạng Đúng (5 Câu • 15đ)</a>
            <a href="#sec-part4" class="quicknav-pill" style="background: #ede9fe; color: #6d28d9; border-color: #ddd6fe;">IV. Nối Thẻ Hội Thoại (4 Câu • 10đ)</a>
            <a href="#sec-part5" class="quicknav-pill" style="background: #e0f2fe; color: #0369a1; border-color: #bae6fd;">V. Đọc Hiểu Đoạn Văn (4 Câu • 20đ)</a>
            <a href="#sec-part6" class="quicknav-pill" style="background: #fee2e2; color: #b91c1c; border-color: #fecaca;">VI. Luyện Dịch Câu (4 Câu • 15đ)</a>
        </div>

        <!-- ============================================== -->
        <!-- PHẦN I: TRẮC NGHIỆM TỔNG HỢP (10 CÂU - 25Đ)   -->
        <!-- ============================================== -->
        <div id="sec-part1">
            <div class="exam-part-header">
                <div class="exam-part-title">
                    <span>📌 PHẦN I: TRẮC NGHIỆM TỔNG HỢP NGỮ PHÁP & TRỢ TỪ</span>
                </div>
                <span class="part-badge-tag">10 Câu • 25 Điểm (2.5đ/câu)</span>
            </div>
            <div id="part1Container">
                <!-- Render Part 1 via JS -->
            </div>
        </div>

        <!-- ============================================== -->
        <!-- PHẦN II: SẮP XẾP TỪ THÀNH CÂU ★ (5 CÂU - 15Đ)  -->
        <!-- ============================================== -->
        <div id="sec-part2">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #78350f 0%, #b45309 100%);">
                <div class="exam-part-title">
                    <span>⭐ PHẦN II: SẮP XẾP TỪ THÀNH CÂU HOÀN CHỈNH (並べ替え)</span>
                </div>
                <span class="part-badge-tag">5 Câu • 15 Điểm (3đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Bấm vào các từ khóa (Chips) theo thứ tự đúng để ghép vào câu, sau đó bấm <strong>[Xác Nhận Thứ Tự]</strong> để kiểm tra từ ở vị trí ngôi sao <strong>[ ★ ]</strong>.
            </p>
            <div id="part2Container">
                <!-- Render Part 2 via JS -->
            </div>
        </div>

        <!-- ============================================== -->
        <!-- PHẦN III: CHIA DẠNG ĐÚNG CỦA TỪ (5 CÂU - 15Đ) -->
        <!-- ============================================== -->
        <div id="sec-part3">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #064e3b 0%, #047857 100%);">
                <div class="exam-part-title">
                    <span>✍️ PHẦN III: CHIA DẠNG ĐÚNG CỦA TỪ TRONG NGOẶC (活用形・穴埋め)</span>
                </div>
                <span class="part-badge-tag">5 Câu • 15 Điểm (3đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Điền dạng biến đổi thích hợp của từ trong ngoặc vào ô trống (chấp nhận cả Kanji lẫn Hiragana/Romaji), sau đó nhấn <strong>[Kiểm Tra]</strong> hoặc phím <strong>Enter</strong>.
            </p>
            <div id="part3Container">
                <!-- Render Part 3 via JS -->
            </div>
        </div>

        <!-- ============================================== -->
        <!-- PHẦN IV: NỐI CỘT TÌNH HUỐNG (4 CÂU - 10Đ)     -->
        <!-- ============================================== -->
        <div id="sec-part4">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 100%);">
                <div class="exam-part-title">
                    <span>🔄 PHẦN IV: NỐI CỘT TÌNH HUỐNG & PHẢN XẠ CÔNG SỞ (マッチング)</span>
                </div>
                <span class="part-badge-tag">4 Câu • 10 Điểm (2.5đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Chọn câu hồi đáp chuẩn mực của người Nhật phù hợp nhất với từng tình huống giao tiếp.
            </p>
            <div id="part4Container">
                <!-- Render Part 4 via JS -->
            </div>
        </div>

        <!-- ============================================== -->
        <!-- PHẦN V: ĐỌC HIỂU ĐOẠN VĂN (4 CÂU - 20Đ)       -->
        <!-- ============================================== -->
        <div id="sec-part5">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #0c4a6e 0%, #0284c7 100%);">
                <div class="exam-part-title">
                    <span>📖 PHẦN V: ĐỌC HIỂU ĐOẠN VĂN THỰC TẾ (読解)</span>
                </div>
                <span class="part-badge-tag">4 Câu / 2 Bài Đọc • 20 Điểm (5đ/câu)</span>
            </div>
            <div id="part5Container">
                <!-- Render Part 5 via JS -->
            </div>
        </div>

        <!-- ============================================== -->
        <!-- PHẦN VI: LUYỆN DỊCH CÂU 2 CHIỀU (4 CÂU - 15Đ) -->
        <!-- ============================================== -->
        <div id="sec-part6">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #881337 0%, #be123c 100%);">
                <div class="exam-part-title">
                    <span>🌐 PHẦN VI: LUYỆN DỊCH CÂU THỰC CHIẾN (翻訳・ライティング)</span>
                </div>
                <span class="part-badge-tag">4 Câu • 15 Điểm (3.75đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Nhập câu dịch tiếng Nhật vào ô văn bản, sau đó bấm <strong>[Đối Chiếu Đáp Án Chuẩn]</strong> để xem phân tích cấu trúc và tự đánh giá điểm.
            </p>
            <div id="part6Container">
                <!-- Render Part 6 via JS -->
            </div>
        </div>

    </div>

    <!-- ========================================== -->
    <!-- TAB 5: CẨM NANG BỎ TÚI (CHEAT SHEET)       -->
    <!-- ========================================== -->
    <div id="tab-cheatsheet" class="tab-panel">
        <div class="cheatsheet-grid">
            <div class="cheat-card">
                <span class="cheat-badge">BẪY 1 • RỦ RÊ VS ĐỀ NGHỊ GIÚP (BÀI 11)</span>
                <h3 class="cheat-title">ましょう vs ましょうか</h3>
                <p class="cheat-content">
                    • <strong>V-ましょう:</strong> Rủ rê cả 2 cùng làm (<em>いっしょに 行きましょう</em> - Chúng mình cùng đi nhé).<br>
                    • <strong>V-ましょうか:</strong> Đề nghị một mình tôi làm giúp bạn (<em>荷物を 持ちましょうか</em> - Để tôi xách hành lý giúp bạn nhé?).<br>
                    👉 Thêm chữ <code>か</code> biến thành lời đề nghị giúp đỡ ân cần, đừng nhầm lẫn!
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 2 • PHÁN ĐOÁN BỀ NGOÀI (BÀI 12)</span>
                <h3 class="cheat-title">〜そう (Bỏ い, Bỏ な & Ngoại lệ)</h3>
                <p class="cheat-content">
                    • <strong>Tính từ đuôi い:</strong> Bỏ hẳn [い] + そう (<em>おいしそう</em>).<br>
                    • <strong>Tính từ đuôi な:</strong> Bỏ hẳn [な] + そう (<em>にぎやかそう</em>).<br>
                    • <strong>Ngoại lệ sống còn:</strong> <code>いい</code> ➔ <strong><code>よさそう</code></strong> (CẤM dùng <code>いいそう</code> ❌).<br>
                    • <code>ない</code> ➔ <strong><code>なさそう</code></strong>.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 3 • BIẾN ĐỔI TÍNH TỪ (BÀI 12)</span>
                <h3 class="cheat-title">〜くなる vs 〜になる</h3>
                <p class="cheat-content">
                    • <strong>Tính từ đuôi い:</strong> Bỏ [い] + <strong>くなる</strong> (<em>甘くなります</em> - trở nên ngọt).<br>
                    • <strong>Tính từ đuôi な:</strong> Bỏ [な] + <strong>になる</strong> (<em>上手になります</em> - trở nên giỏi).<br>
                    • <strong>Danh từ:</strong> N + <strong>になる</strong> (<em>先生になります</em> - trở thành giáo viên).
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 4 • SO SÁNH PHẠM VI (BÀI 12)</span>
                <h3 class="cheat-title">〜の中で (Trong số...)</h3>
                <p class="cheat-content">
                    • So sánh nhất trong một nhóm: <code>[Phạm vi] の 中で、[A] が いちばん [Tính từ] です</code>.<br>
                    • Ví dụ: <em>日本の 料理の <mark>中で</mark>、天ぷらが いちばん 好きです</em>.<br>
                    👉 Sau chữ 「中」 luôn là trợ từ <code>で</code>, không dùng <code>に</code> hay <code>を</code>.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 5 • THỂ KINH NGHIỆM (BÀI 13)</span>
                <h3 class="cheat-title">V-たことがある & 一度もありません</h3>
                <p class="cheat-content">
                    • <strong>Kinh nghiệm:</strong> Bắt buộc dùng <strong>Thể TA</strong> (<em>乗った ことが あります</em>).<br>
                    • <strong>Phủ định tuyệt đối:</strong> <em>いいえ、一度も ありません</em> (Một lần cũng chưa từng).<br>
                    👉 Không trả lời: <code>まだ あります</code> ❌.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 6 • MỨC ĐỘ QUÁ ĐÀ (BÀI 13)</span>
                <h3 class="cheat-title">〜すぎる (V-stem, Bỏ い, Bỏ な)</h3>
                <p class="cheat-content">
                    • <strong>Động từ:</strong> V(bỏ ます) + すぎる (<em>飲みすぎる</em>).<br>
                    • <strong>Tính từ đuôi い:</strong> Bỏ [い] + すぎる (<em>高すぎる</em>).<br>
                    • <strong>Tính từ đuôi な:</strong> Bỏ [な] + すぎる (<em>静かすぎる</em>). Cấm nói <code>静かだすぎる</code> ❌!<br>
                    • <strong>Dạng nguyên nhân:</strong> <em>高すぎて 買えません</em> (Đắt quá không mua nổi).
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 7 • XIN PHÉP VS CẤM ĐOÁN (BÀI 14)</span>
                <h3 class="cheat-title">〜てもいい vs 〜てはいけない</h3>
                <p class="cheat-content">
                    • <strong>Xin phép:</strong> <code>V-ても いいですか</code> (<em>使ってもいいですか</em> ➔ Đáp: <em>ええ、どうぞ</em>).<br>
                    • <strong>Cấm đoán:</strong> <code>V-ては いけません</code> (<em>吸っては いけません</em> - Cấm hút thuốc).<br>
                    👉 Nhớ câu thần chú: <code>ても</code> = Làm cũng ĐƯỢC; <code>ては</code> = Làm thì KHÔNG ĐƯỢC.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 8 • MƯỢN ĐỒ & CÁCH LÀM (BÀI 14)</span>
                <h3 class="cheat-title">借ります vs 貸します & V-かた</h3>
                <p class="cheat-content">
                    • <strong>借ります (かります):</strong> Mình MƯỢN từ ai (nhận về mình: <em>同僚に 借りました</em>).<br>
                    • <strong>貸します (かします):</strong> Mình CHO MƯỢN (đưa sang cho người khác).<br>
                    • <strong>V-かた:</strong> Động từ bỏ ます + 方 (<em>使い方, 読み方</em>). Nhớ trợ từ <code>を</code> biến thành <code>の</code> (<em>コピー機<mark>の</mark> 使い方</em>).
                </p>
            </div>
        </div>
    </div>

</div>

<!-- Toast Notification -->
<div id="toast" class="toast">Đã copy vào bộ nhớ tạm!</div>

<script src="../assets/data/mini_11_14_data.js?v=1"></script>
<script src="../assets/js/mini-test-11-14.js?v=2"></script>
<script src="../assets/nav.js?v=6" defer></script>
</body>
</html>
"""

os.makedirs(os.path.join(WORKSPACE, "assets/data"), exist_ok=True)
data_js_path = os.path.join(WORKSPACE, "assets/data/mini_11_14_data.js")
with open(data_js_path, "w", encoding="utf-8") as df:
    df.write("window.MINI_11_14_DATA = {\n")
    df.write(f"  rawVocab: {vocab_json_str},\n")
    df.write(f"  rawKanji: {kanji_json_str},\n")
    df.write(f"  part1Data: {p1_json_str},\n")
    df.write(f"  part2Data: {p2_json_str},\n")
    df.write(f"  part3Data: {p3_json_str},\n")
    df.write(f"  part4Data: {p4_json_str},\n")
    df.write(f"  part5Data: {p5_json_str},\n")
    df.write(f"  part6Data: {p6_json_str}\n")
    df.write("};\n")

output_path = os.path.join(WORKSPACE, "tests/On_Tap_Mini_Test_A2_11_14.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {output_path} ({len(html_content)} bytes) and {data_js_path}")
