#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_mini_test_15_18.py
Tạo trang web chuyên đề Ôn Tập Mini Test Bài 15 - 18 (Marugoto A2-2 Final Review):
- Tab 1: 📖 Lý Thuyết Trọng Tâm 4 Bài (Bài 15 ➔ 18)
- Tab 2: 🎴 135 Từ Vựng Chuẩn Kèm Nút Copy Quizlet Sạch & Ẩn Nghĩa & Lọc Theo Bài
- Tab 3: ⛩️ 34 Chữ Hán Kanji (Chiết tự, Mẹo nhớ & Từ ghép & Copy Quizlet)
- Tab 4: 🎯 ĐỀ THI THỬ ĐA DẠNG NĂNG LỰC (6 Dạng Bài • 32 Câu Chuẩn Sư Phạm 100 Điểm):
    + PHẦN I: Trắc Nghiệm Tổng Hợp Ngữ Pháp & Trợ Từ (10 Câu - 25 Điểm)
    + PHẦN II: Sắp Xếp Từ Thành Câu Hoàn Chỉnh ★ (5 Câu - 15 Điểm)
    + PHẦN III: Chia Dạng Đúng Của Từ Trong Ngoặc (5 Câu - 15 Điểm)
    + PHẦN IV: Nối Cột Tình Huống & Phản Xạ Đời Sống (4 Câu - 10 Điểm)
    + PHẦN V: Đọc Hiểu Đoạn Văn Thực Tế (4 Câu / 2 Bài Đọc - 20 Điểm)
    + PHẦN VI: Luyện Dịch Câu Thực Chiến 2 Chiều (4 Câu - 15 Điểm)
- Tab 5: ⌨️ LUYỆN GÕ PHẢN XẠ NHẬT - VIỆT (Flash Typing Practice L15-18)
- Tab 6: ⚡ Cẩm Nang Bỏ Túi (Cheat Sheet Tránh Bẫy Sư Phạm)
"""

import json
import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from mini_test_15_18_exams import (
    EXAM_152,
    EXAM_153,
    EXAM_154,
    EXAM_155,
    validate_exam_suite,
)

WORKSPACE = os.path.abspath(os.path.dirname(SCRIPT_DIR))

# 1. Load Vocab
with open(os.path.join(WORKSPACE, 'data/master_vocab_official.json'), 'r', encoding='utf-8') as f:
    all_vocab = json.load(f)

vocab_15_18 = [w for w in all_vocab if w.get('l') in ['A2-15', 'A2-16', 'A2-17', 'A2-18']]

# 2. Load Kanji
with open(os.path.join(WORKSPACE, 'data/kanji_extracted.json'), 'r', encoding='utf-8') as f:
    all_kanji = json.load(f)

kanji_15_18 = [k for k in all_kanji if k.get('lesson') in ['L15', 'L16', 'L17', 'L18'] or k.get('lessonName') in ['Bài 15', 'Bài 16', 'Bài 17', 'Bài 18']]

KANJI_READINGS = {
    '体': 'からだ',
    '頭': 'あたま',
    '目': 'め',
    '口': 'くち',
    '耳': 'みみ',
    '手': 'て',
    '足': 'あし',
    '上': 'うえ',
    '下': 'した',
    '毎': 'まい',
    '末': 'すえ',
    '元': 'げん',
    '外': 'そと',
    '起': 'おきる',
    '歩': 'あるく',
    '走': 'はしる',
    '泳': 'およぐ',
    '朝': 'あさ',
    '気': 'き',
    '祝': 'いわう',
    '誕': 'たん',
    '結': 'けつ',
    '婚': 'こん',
    '絵': 'え',
    '写': 'しゃ',
    '真': 'しん',
    '計': 'けい',
    '先': 'せん',
    '今': 'いま',
    '来': 'らい',
    '年': 'とし',
    '去': 'きょ',
    '家': 'いえ',
    '思': 'おもう'
}

KANJI_SHORT_MEANINGS = {
    '体': 'thân thể, cơ thể',
    '頭': 'cái đầu, đầu óc',
    '目': 'con mắt, mục tiêu',
    '口': 'cái miệng, cửa',
    '耳': 'cái tai, lắng nghe',
    '手': 'bàn tay, người làm',
    '足': 'bàn chân, cẳng chân, đủ',
    '上': 'bên trên, phía trên',
    '下': 'bên dưới, phía dưới',
    '毎': 'mỗi, từng, hàng ngày',
    '末': 'ngọn, cuối cùng (cuối tuần)',
    '元': 'gốc gác, nguyên khí (khỏe mạnh)',
    '外': 'bên ngoài, ngoại quốc',
    '起': 'thức dậy, khởi đầu',
    '歩': 'đi bộ, từng bước',
    '走': 'chạy, tẩu thoát',
    '泳': 'bơi lội',
    '朝': 'buổi sáng, ban mai',
    '気': 'không khí, khí sắc, tinh thần',
    '祝': 'chúc mừng, lễ mừng',
    '誕': 'đản sinh, sinh ra',
    '結': 'buộc lại, kết hôn, kết quả',
    '婚': 'hôn nhân, cưới hỏi',
    '絵': 'bức tranh, hội họa',
    '写': 'chụp ảnh, sao chép',
    '真': 'chân thực, sự thật',
    '計': 'tính toán, kế hoạch, đồng hồ',
    '先': 'trước, đi đầu (tuần trước)',
    '今': 'hiện tại, bây giờ (hôm nay)',
    '来': 'đến, tương lai (năm sau)',
    '年': 'năm, tuổi tác',
    '去': 'quá khứ, đã qua (năm ngoái)',
    '家': 'ngôi nhà, gia đình',
    '思': 'suy nghĩ, ý nghĩ'
}

for k in kanji_15_18:
    ch = k['char']
    k['hiragana'] = KANJI_READINGS.get(ch, (k.get('kun') or '').split('、')[0].replace('-', '').strip() or (k.get('on') or '').split('、')[0].replace('-', '').strip())
    k['shortMeaning'] = KANJI_SHORT_MEANINGS.get(ch, k.get('meaning', '').split(',')[0].strip())

# 3. Data for Part I: Multiple Choice (10 Questions - 25 pts)
PART1_MC = [
    {
        "id": 1,
        "category": "Bài 15 • Hỏi thăm & Giải thích triệu chứng (～んです)",
        "q": "「どうしたんですか。」――「きのうから 頭が [____]。」",
        "options": ["いたいです", "いたいんです", "いたいんですか", "いたかったなんです"],
        "correct": 1,
        "explain": "Khi đối phương hỏi thăm hoàn cảnh 「どうしたんですか」(Bạn bị làm sao vậy?), ta dùng tính từ đuôi い + 「んです」 (いたいんです) để giải thích triệu chứng cơ thể đang gặp phải."
    },
    {
        "id": 2,
        "category": "Bài 15 • Lời khuyên nhẹ nhàng (V-る ＋ と いいですよ)",
        "q": "「おなかが いたくて、ねられません。」――「ねる まえに、この くすりを [____] と いいですよ。」",
        "options": ["飲んだ", "飲んで", "飲む", "飲みます"],
        "correct": 2,
        "explain": "Đưa ra lời khuyên hữu ích cho sức khỏe: 「Động từ thể Từ điển (V-る) ＋ と いいですよ」 (Làm ... thì tốt đấy nhé!)."
    },
    {
        "id": 3,
        "category": "Bài 15 • Dặn dò đừng làm (V-ない ＋ で ください)",
        "q": "「ねつが ありますから、きょうは お酒を [____] ください。」",
        "options": ["飲まないで", "飲まない", "飲まなくて", "飲むないで"],
        "correct": 0,
        "explain": "Đề nghị, dặn dò ai đó đừng làm hành động gì: 「V(thể ない) ＋ で ください」 (Xin đừng uống rượu)."
    },
    {
        "id": 4,
        "category": "Bài 16 • Liệt kê hành động tiêu biểu (V1-たり、V2-たり)",
        "q": "週末は 外を [____]、プールで 泳いだり しています。",
        "options": ["走って", "走るたり", "走った", "走ったり"],
        "correct": 3,
        "explain": "Cấu trúc liệt kê hành động tiêu biểu: 「V1-たり、V2-たり します / しています」. Động từ 走る nhóm 1 ➔ 走った ➔ 走ったり."
    },
    {
        "id": 5,
        "category": "Bài 16 • Mệnh đề bổ nghĩa cho danh từ (V〈ふつうけい〉＋ 人)",
        "q": "私の 会社で、毎朝 コーヒーを [____] 人は 10人です。",
        "options": ["飲みません", "飲まない", "飲まなくて", "飲まなかったです"],
        "correct": 1,
        "explain": "Động từ đứng trước bổ nghĩa cho danh từ 「人」 phải chia về thể thông thường (ふつうけい). Phủ định hiện tại 「飲みません」 ➔ 「飲まない」."
    },
    {
        "id": 6,
        "category": "Bài 16 • Hỏi mục đích (何 の ために)",
        "q": "「[____] の ために、毎日 歩いて いるんですか。」――「けんこうの ためです。」",
        "options": ["何", "だれ", "どこ", "いつ"],
        "correct": 0,
        "explain": "Hỏi mục đích làm một việc gì đó: 「何 (なん) の ために [Hành động]」 (Để làm gì / Vì mục đích gì?)."
    },
    {
        "id": 7,
        "category": "Bài 17 • Trợ từ nhận quà (～に もらいました)",
        "q": "「すてきな 時計ですね。」――「ええ、去年の 誕生日に 父 [____] もらったんです。」",
        "options": ["を", "で", "に", "へ"],
        "correct": 2,
        "explain": "Nhận quà từ ai đó dùng trợ từ 「に」 (hoặc 「から」): 「[Người tặng] に [Món quà] を もらいました / もらったんです」."
    },
    {
        "id": 8,
        "category": "Bài 17 • Thể thông thường + んです (Biến đổi だ ➔ な)",
        "q": "「どうして おくれたんですか。」――「すみません、道が [____]。」",
        "options": ["じゅうたいだんです", "じゅうたいなんです", "じゅうたいのです", "じゅうたいなです"],
        "correct": 1,
        "explain": "Danh từ và Tính từ đuôi な trước 「んです」 phải biến đổi 「だ ➔ な」: 「じゅうたいだ」 ➔ 「じゅうたいなんです」."
    },
    {
        "id": 9,
        "category": "Bài 17 • Liệt kê đại diện danh từ (とか／とか)",
        "q": "結婚の お祝いに、絵 [____] 時計 [____] を あげます。",
        "options": ["と／と", "や／など", "たり／たり", "とか／とか"],
        "correct": 3,
        "explain": "Liệt kê các món quà mang tính đại diện, ví dụ tiêu biểu: 「N1 とか N2 とか」 (như là tranh hay là đồng hồ...)."
    },
    {
        "id": 10,
        "category": "Bài 18 • Bày tỏ quan điểm với Tính từ đuôi な (～と 思います)",
        "q": "「あべさんの 結婚の お祝いに 花びんは どうですか。」――「ええ、とても [____] と 思います。」",
        "options": ["きれい", "きれいな", "きれいだ", "きれいです"],
        "correct": 2,
        "explain": "Trước 「と 思います」 dùng thể thông thường. Tính từ đuôi な ở hiện tại khẳng định BẮT BUỘC phải thêm 「だ」: 「きれいだ と 思います」."
    }
]

# 4. Data for Part II: Sentence Ordering (5 Questions - 15 pts)
PART2_ARRANGE = [
    {
        "id": 11,
        "category": "Bài 15 • Khuyên nhủ khi đau bụng (V-る といいですよ)",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "おなかが",
        "post": "いいですよ。",
        "chips": ["この", "飲むと", "いたい とき、", "くすりを"],
        "correctOrder": [2, 0, 3, 1],
        "starIndex": 2,
        "starChip": "くすりを",
        "fullSentence": "おなかが いたい とき、この くすりを 飲むと いいですよ。",
        "simplifiedSentence": "おなかが いたいとき、この くすりを 飲むと いいですよ。",
        "explain": "Điều kiện thời gian 「いたい とき」 + tân ngữ 「この くすりを」 + lời khuyên 「飲むと いいですよ」. Vị trí ngôi sao là [くすりを]."
    },
    {
        "id": 12,
        "category": "Bài 16 • Mệnh đề bổ nghĩa cho người (V〈ふつうけい〉＋ 人)",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "よく",
        "post": "いいです。",
        "chips": ["読む", "頭が", "本を", "人は"],
        "correctOrder": [2, 0, 3, 1],
        "starIndex": 2,
        "starChip": "人は",
        "fullSentence": "よく 本を 読む 人は 頭が いいです。",
        "simplifiedSentence": "よく 本を 読む 人は 頭が いいです。",
        "explain": "Mệnh đề động từ thể thường bổ nghĩa đứng trước danh từ 「よく 本を 読む 人は」 + vị ngữ 「頭が いいです」. Vị trí ngôi sao là [人は]."
    },
    {
        "id": 13,
        "category": "Bài 16 • Nêu hành động tiêu biểu (V-たり しました)",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "きのう",
        "post": "しました。",
        "chips": ["えいがを", "友だちと", "見たり", "おもしろい"],
        "correctOrder": [1, 3, 0, 2],
        "starIndex": 2,
        "starChip": "えいがを",
        "fullSentence": "きのう 友だちと おもしろい えいがを 見たり しました。",
        "simplifiedSentence": "きのう 友だちと おもしろい えいがを 見たり しました。",
        "explain": "Cùng ai 「友だちと」 + danh từ có tính từ bổ nghĩa 「おもしろい えいがを」 + động từ thể 「見たり しました」. Vị trí ngôi sao là [えいがを]."
    },
    {
        "id": 14,
        "category": "Bài 17 • Tặng quà Ngày của Mẹ (N1 に N2 を あげました)",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "母の 日に、",
        "post": "あげました。",
        "chips": ["母に", "花を", "わたしは", "きれいな"],
        "correctOrder": [2, 0, 3, 1],
        "starIndex": 2,
        "starChip": "きれいな",
        "fullSentence": "母の 日に、わたしは 母に きれいな 花を あげました。",
        "simplifiedSentence": "母の 日に、わたしは 母に きれいな 花を あげました。",
        "explain": "Chủ ngữ 「わたしは」 + người nhận 「母に」 + tính từ bổ nghĩa 「きれいな」 + món quà 「花を」 + 「あげました」. Vị trí ngôi sao là [きれいな]."
    },
    {
        "id": 15,
        "category": "Bài 18 • Trích dẫn lời người khác (～と 言っていました)",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "あべさんは",
        "post": "言っていました。",
        "chips": ["パーティーは", "楽しかったと", "きのうの", "とても"],
        "correctOrder": [2, 0, 3, 1],
        "starIndex": 2,
        "starChip": "とても",
        "fullSentence": "あべさんは きのうの パーティーは とても 楽しかったと 言っていました。",
        "simplifiedSentence": "あべさんは きのうの パーティーは とても 楽しかったと 言っていました。",
        "explain": "Nội dung trích dẫn ở thể thông thường quá khứ: 「きのうの パーティーは とても 楽しかったと」 + 「言っていました」. Vị trí ngôi sao là [とても]."
    }
]

# 5. Data for Part III: Fill in Correct Conjugated Form (5 Questions - 15 pts)
PART3_CONJUGATE = [
    {
        "id": 16,
        "category": "Bài 15 • Động từ thể Phủ định dặn dò (V-ないで ください)",
        "sentence": "ねつが ある ときは、無理を (します) [_______] で ください。",
        "baseWord": "します",
        "accepted": ["しない", "shinai"],
        "displayAnswer": "しない (shinai)",
        "explain": "Động từ nhóm 3 「します」 chuyển sang thể Phủ định ngắn (Nai) là 「しない」. Cấu trúc: 「V-ないで ください」 (Xin đừng làm quá sức)."
    },
    {
        "id": 17,
        "category": "Bài 15 • Động từ thể Từ điển đưa lời khuyên (V-る といいですよ)",
        "sentence": "ねる まえに、おふろに (入ります) [_______] と いいですよ。",
        "baseWord": "入ります (はいります)",
        "accepted": ["はいる", "入る", "hairu"],
        "displayAnswer": "入る / はいる (hairu)",
        "explain": "Đưa ra lời khuyên: 「V(thể từ điển) ＋ と いいですよ」. Động từ 「入ります」 nhóm 1 chuyển về thể từ điển là 「入る (はいる)」."
    },
    {
        "id": 18,
        "category": "Bài 16 • Động từ liệt kê hành động (V-たり、V-たり します)",
        "sentence": "週末は よく 外を (歩きます) [_______]、水泳を したり しています。",
        "baseWord": "歩きます (あるきます)",
        "accepted": ["あるいたり", "歩いたり", "aruitari"],
        "displayAnswer": "歩いたり / あるいたり (aruitari)",
        "explain": "Động từ 「歩きます」 nhóm 1 đuôi き ➔ thể Ta là 「歩いた」 ➔ ghép 「り」 thành 「歩いたり (あるいたり)」."
    },
    {
        "id": 19,
        "category": "Bài 17 • Mệnh đề bổ nghĩa nhận quà (V-た ＋ N)",
        "sentence": "これは 誕生日に 父に (もらいます) [_______] 時計です。",
        "baseWord": "もらいます",
        "accepted": ["もらった", "moratta"],
        "displayAnswer": "もらった (moratta)",
        "explain": "Bổ nghĩa cho danh từ 「時計」 ở thì quá khứ: Động từ 「もらいます」 chia về thể thông thường quá khứ là 「もらった」."
    },
    {
        "id": 20,
        "category": "Bài 18 • Tính từ đuôi な trước と思います (Na ＋ だ ＋ と思います)",
        "sentence": "この 着物は とても (きれいです) [_______] と 思います。",
        "baseWord": "きれいです",
        "accepted": ["きれいだ", "kireida"],
        "displayAnswer": "きれいだ (kireida)",
        "explain": "Trước 「と 思います」 phải chia về thể thông thường. Tính từ đuôi な ở hiện tại khẳng định thêm 「だ」: 「きれいです」 ➔ 「きれいだ」."
    }
]

# 6. Data for Part IV: Matching Situation & Response (4 Questions - 10 pts)
PART4_MATCH = [
    {
        "id": 21,
        "category": "Bài 15 • Kể triệu chứng & Dặn dò nghỉ ngơi",
        "promptA": "「さいきん、ちょっと こしが いたいんです。」",
        "correctBId": "B1",
        "promptB": "「それは たいへんですね。あまり 無理を しないで ください。おふろに 入ると いいですよ。」",
        "explain": "Khi đối phương nói bị đau lưng/eo 「こしが いたいんです」, ta đồng cảm 「たいへんですね」 và dặn dò 「無理を しないで ください」「おふろに 入ると いいですよ」."
    },
    {
        "id": 22,
        "category": "Bài 16 • Hỏi thăm thói quen rèn luyện sức khỏe",
        "promptA": "「けんこうの ために、なにか して いますか。」",
        "correctBId": "B2",
        "promptB": "「はい、毎朝 外を 歩いたり、週末に 泳いだり して います。」",
        "explain": "Trả lời câu hỏi về hoạt động rèn luyện vì sức khỏe bằng cấu trúc liệt kê 「〜たり、〜たり しています」."
    },
    {
        "id": 23,
        "category": "Bài 17 • Khen đồ vật & Chia sẻ nguồn gốc quà tặng",
        "promptA": "「その 時計、すてきですね。どこで 買ったんですか。」",
        "correctBId": "B3",
        "promptB": "「これですか。そつぎょうの お祝いに 父に もらったんです。」",
        "explain": "Khi được khen chiếc đồng hồ đẹp, ta giải thích nguồn gốc món quà được tặng bằng cấu trúc 「〜の お祝いに 〜に もらったんです」."
    },
    {
        "id": 24,
        "category": "Bài 18 • Bàn bạc quà mừng kết hôn",
        "promptA": "「あべさんの 結婚の お祝い、何が いいと 思いますか。」",
        "correctBId": "B4",
        "promptB": "「あべさんは 写真が 好きだと 言っていましたから、すてきな 写真たてが いいと 思います。」",
        "explain": "Kết hợp trích dẫn sở thích của người khác 「〜と言っていました」 và đưa ra ý kiến đề xuất quà tặng 「〜がいいと思います」."
    }
]

# 7. Data for Part V: Reading Comprehension (4 Questions - 20 pts)
PART5_READING = [
    {
        "passageId": 1,
        "title": "BÀI ĐỌC 1: けんこうの ための アドバイス (Giữ Gìn Sức Khỏe - Bài 15 & 16)",
        "text": "みなさん、毎日 元気に すごして いますか。わたしは 先月、頭が いたかった とき、あまり 無理を しないで はやく ねました。ねる まえに おふろに 入ったり、くすりを 飲んだり すると いいですよ。<br>また、けんこうの ために、毎日 すこし うんどうする ことが たいせつです。毎朝 外を 歩いたり、週末に プールで 泳いだり して います。よく うんどうを する 人は 元気だと 思います。みなさんも、野菜を たくさん 食べて、お酒を あまり 飲まないで くださいね。",
        "questions": [
            {
                "id": 25,
                "q": "頭が いたかった とき、この 人は どう しましたか。",
                "options": [
                    "たくさん お酒を 飲みました",
                    "くすりを 飲まないで しごとを しました",
                    "あまり 無理を しないで、はやく ねました",
                    "毎日 プールで 泳ぎました"
                ],
                "correct": 2,
                "explain": "Trong bài viết nêu rõ: 「頭が いたかった とき、あまり 無理を しないで はやく ねました」."
            },
            {
                "id": 26,
                "q": "けんこうの ために、この 人は いつも 何を して いますか。",
                "options": [
                    "毎朝 外を 歩いたり、週末に 泳いだり して います",
                    "おふろに 入らないで います",
                    "野菜を あまり 食べません",
                    "毎日 うんどうを しません"
                ],
                "correct": 0,
                "explain": "Trong bài viết nêu rõ: 「毎朝 外を 歩いたり、週末に プールで 泳いだり して います」."
            }
        ]
    },
    {
        "passageId": 2,
        "title": "BÀI ĐỌC 2: あべさんの 結婚の お祝い (Bàn Bạc Mừng Kết Hôn - Bài 17 & 18)",
        "text": "来週の 日よう日、会社の 友だちと いっしょに あべさんの 結婚の お祝いを します。あべさんは 先月、新しい 家に ひっこしました。<br>きのう、キムさんに「お祝いの プレゼントは 何が いいですか」と 聞きました。キムさんは「あべさんは 料理が 好きですから、料理の ときに 使う ものとか 花びんとかが いいと 思います」と 言っていました。ですから、みんなで きれいな 花びんを あげます。あべさんは きっと よろこぶと 思います。",
        "questions": [
            {
                "id": 27,
                "q": "キムさんは お祝いの プレゼントについて 何と 言っていましたか。",
                "options": [
                    "時計とか 絵とかが いいと 言っていました",
                    "おもちゃとか にんぎょうとかが いいと 言っていました",
                    "セーターを あげないと 言っていました",
                    "料理の ときに 使う ものとか 花びんとかが いいと 言っていました"
                ],
                "correct": 3,
                "explain": "Trong bài viết: 「キムさんは『あべさんは 料理が 好きですから、料理の ときに 使う ものとか 花びんとかが いいと 思います』と 言っていました」."
            },
            {
                "id": 28,
                "q": "あべさんの 結婚の お祝いに、みんなで 何を あげますか。",
                "options": [
                    "時計を あげます",
                    "きれいな 花びんを あげます",
                    "シャツと セーターを あげます",
                    "カメラと 写真を あげます"
                ],
                "correct": 1,
                "explain": "Trong bài viết kết luận: 「ですから、みんなで きれいな 花びんを あげます」."
            }
        ]
    }
]

# 8. Data for Part VI: Sentence Translation (4 Questions - 15 pts)
PART6_TRANSLATION = [
    {
        "id": 29,
        "category": "Bài 15 • Giải thích triệu chứng (～んです)",
        "vi": "Gần đây, cổ của tôi hơi bị đau một chút.",
        "hint": "さいきん, ちょっと, くび, いたい (～んです)",
        "modelSentence": "さいきん、ちょっと くびが いたいんです。",
        "modelKana": "さいきん、ちょっと くびが いたいんです。",
        "keywords": ["さいきん", "くびが", "いたいんです"],
        "breakdown": [
            {"part": "さいきん", "role": "Thời gian gần đây"},
            {"part": "ちょっと くびが", "role": "Bộ phận cơ thể bị đau (cổ)"},
            {"part": "いたいんです", "role": "Tính từ đuôi い + んです giải thích tình trạng cho đối phương"}
        ]
    },
    {
        "id": 30,
        "category": "Bài 16 • Mệnh đề bổ nghĩa cho người (V〈ふつうけい〉＋ 人)",
        "vi": "Người hay đọc sách thì thông minh (đầu óc tốt).",
        "hint": "よく, 本を 読みます (➔ 読む), 人 (ひと), 頭が いいです (あたまが いいです)",
        "modelSentence": "よく 本を 読む 人は 頭が いいです。",
        "modelKana": "よく 本を よむ ひとは あたまが いいです。",
        "keywords": ["よく", "本を", "読む", "人は", "頭が", "いいです"],
        "breakdown": [
            {"part": "よく 本を 読む", "role": "Động từ thể thường (ふつうけい) bổ nghĩa đứng trước danh từ"},
            {"part": "人は", "role": "Danh từ được bổ nghĩa làm chủ đề câu (người mà...)"},
            {"part": "頭が いいです", "role": "Nhận xét tính chất (thông minh / đầu óc tốt)"}
        ]
    },
    {
        "id": 31,
        "category": "Bài 17 • Nhận quà & Giải thích hoàn cảnh (～んです)",
        "vi": "Chiếc đồng hồ này là món quà tôi đã nhận từ bố nhân dịp mừng tốt nghiệp.",
        "hint": "この 時計 (この とけい), そつぎょうの お祝い (そつぎょうの おいわい), 父に, もらったんです",
        "modelSentence": "この 時計は そつぎょうの お祝いに 父に もらったんです。",
        "modelKana": "この とけいは そつぎょうの おいわいに ちちに もらったんです。",
        "keywords": ["時計", "そつぎょう", "お祝い", "父に", "もらったんです"],
        "breakdown": [
            {"part": "この 時計は", "role": "Chủ ngữ được đưa lên làm đề tài (chiếc đồng hồ này)"},
            {"part": "そつぎょうの お祝いに", "role": "Dịp kỷ niệm chúc mừng tốt nghiệp"},
            {"part": "父に", "role": "Đối tượng trao quà (nhận từ ai đó: [Người] に)"},
            {"part": "もらったんです", "role": "Động từ nhận quà ở thì quá khứ + んです giải thích hoàn cảnh"}
        ]
    },
    {
        "id": 32,
        "category": "Bài 18 • Quan điểm cá nhân (～と 思います)",
        "vi": "Tôi nghĩ rằng tiệc mừng kết hôn của anh Abe thì bữa tiệc là hay nhất, chắc chắn anh ấy sẽ vui.",
        "hint": "あべさんの 結婚の お祝い, パーティーが いい, きっと よろこぶ, 思います (おもいます)",
        "modelSentence": "あべさんの 結婚の お祝いは パーティーが いいと 思います。きっと よろこぶと 思います。",
        "modelKana": "あべさんの けっこんの おいわいは パーティーが いいと おもいます。きっと よろこぶと おもいます。",
        "keywords": ["結婚", "お祝い", "パーティーが", "いいと", "よろこぶと", "思います"],
        "breakdown": [
            {"part": "あべさんの 結婚の お祝いは", "role": "Chủ đề tiệc chúc mừng kết hôn của anh Abe"},
            {"part": "パーティーが いいと 思います", "role": "Nêu quan điểm đề xuất tổ chức tiệc là hay"},
            {"part": "きっと よろこぶと 思います", "role": "Dự đoán suy nghĩ dùng thể từ điển 「よろこぶ」 + 「と 思います」"}
        ]
    }
]

EXAM_151 = {
    "id": "151",
    "code": "151",
    "shortTitle": "Tổng Hợp Chuẩn",
    "fullTitle": "MÃ ĐỀ 151 • TỔNG HỢP CHUẨN MARUGOTO A2-1 (BÀI 15 - 18)",
    "subtitle": "Bao phủ cân đối toàn bộ Bài 15–18 & NPBS: ～んです, といい, ないで, たり, ために, bổ nghĩa V+N, もらう/あげる, と思う/と言う.",
    "badge": "🎯 Chuẩn Toàn Diện",
    "p1": PART1_MC,
    "p2": PART2_ARRANGE,
    "p3": PART3_CONJUGATE,
    "p4": PART4_MATCH,
    "p5": PART5_READING,
    "p6": PART6_TRANSLATION,
}

EXAMS_SUITE = [EXAM_151, EXAM_152, EXAM_153, EXAM_154, EXAM_155]
_validation = validate_exam_suite(EXAMS_SUITE)
assert not _validation["structure_errors"], f"Structure errors: {_validation['structure_errors']}"
assert not _validation["banned_hits"], f"Banned grammar/vocab hits: {_validation['banned_hits']}"
assert not _validation["unlearned_hits"], f"Unlearned Kanji hits: {_validation['unlearned_hits']}"

# Build JSON Data Strings
vocab_json_str = json.dumps(vocab_15_18, ensure_ascii=False)
kanji_json_str = json.dumps(kanji_15_18, ensure_ascii=False)
exams_json_str = json.dumps(EXAMS_SUITE, ensure_ascii=False)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Cẩm Nang Toàn Diện & Đề Thi Thử Đa Dạng Bài 15 - 18 (Marugoto A2-2 Final)</title>
    <meta name="description" content="Chuyên đề ôn tập và đề thi thử đa dạng 6 phần: Trắc nghiệm, Sắp xếp câu, Chia thể, Nối cột hội thoại, Đọc hiểu đoạn văn và Luyện dịch câu 100 điểm kèm Luyện gõ phản xạ.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="../assets/js/audio-engine.js"></script>
    <style>
        :root {
            --primary: #4f46e5;
            --primary-light: #e0e7ff;
            --primary-dark: #3730a3;
            --secondary: #0ea5e9;
            --secondary-light: #e0f2fe;
            --accent: #f43f5e;
            --accent-light: #ffe4e6;
            --success: #10b981;
            --success-light: #d1fae5;
            --warning: #f59e0b;
            --warning-light: #fef3c7;
            --purple: #8b5cf6;
            --purple-light: #ede9fe;
            --dark: #0f172a;
            --gray-900: #0f172a;
            --gray-800: #1e293b;
            --gray-700: #334155;
            --gray-600: #475569;
            --gray-500: #64748b;
            --gray-400: #94a3b8;
            --gray-300: #cbd5e1;
            --gray-200: #e2e8f0;
            --gray-100: #f1f5f9;
            --gray-50: #f8fafc;
            --white: #ffffff;
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 18px;
            --radius-full: 9999px;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -2px rgba(0,0,0,0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1);
            --shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.12), 0 8px 10px -6px rgba(0,0,0,0.08);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #f1f5f9;
            color: var(--gray-800);
            line-height: 1.6;
            padding: 20px 12px 80px 12px;
        }

        .jp-text {
            font-family: 'Noto Sans JP', sans-serif;
        }

        /* Container */
        .container {
            max-width: 1240px;
            margin: 0 auto;
        }

        /* Hero Header */
        .hero-banner {
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4f46e5 100%);
            border-radius: var(--radius-xl);
            padding: 38px 28px;
            color: #ffffff;
            margin-bottom: 24px;
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
            text-align: center;
        }

        .hero-banner::after {
            content: "満点";
            position: absolute;
            right: 20px;
            bottom: -30px;
            font-size: 160px;
            font-family: 'Noto Sans JP', sans-serif;
            font-weight: 900;
            color: rgba(255, 255, 255, 0.04);
            pointer-events: none;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.18);
            backdrop-filter: blur(8px);
            padding: 6px 16px;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 14px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #c7d2fe;
        }

        .hero-title {
            font-size: clamp(1.8rem, 4vw, 2.7rem);
            font-weight: 800;
            letter-spacing: -0.5px;
            line-height: 1.25;
            margin-bottom: 12px;
            background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-desc {
            font-size: clamp(0.95rem, 2vw, 1.1rem);
            color: #c7d2fe;
            max-width: 820px;
            margin: 0 auto 24px auto;
        }

        .hero-stats {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 16px;
            max-width: 900px;
            margin: 0 auto;
        }

        .hero-stat-pill {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 8px 18px;
            border-radius: var(--radius-full);
            font-size: 0.88rem;
            font-weight: 600;
            color: #e2e8f0;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        /* Tab Navigation Bar */
        .tab-nav-wrapper {
            position: sticky;
            top: 10px;
            z-index: 100;
            margin-bottom: 24px;
        }

        /* Tab Navigation Bar (Capsule Pill Standard) */
        .tab-nav-wrapper {
            position: sticky;
            top: 10px;
            z-index: 500;
            margin-bottom: 24px;
        }

        .tab-nav {
            display: flex;
            gap: 6px;
            background: #ffffff;
            padding: 6px 10px;
            border-radius: 9999px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
            border: 1.5px solid var(--gray-200);
            overflow-x: auto;
            scrollbar-width: none;
            justify-content: center;
            align-items: center;
            flex-wrap: nowrap;
        }

        .tab-nav::-webkit-scrollbar {
            display: none;
        }

        .tab-btn {
            flex: 1 1 auto;
            white-space: nowrap;
            padding: 8px 14px;
            border: 1.5px solid transparent;
            background: transparent;
            color: var(--gray-600);
            font-size: 0.84rem;
            font-weight: 800;
            border-radius: 9999px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
        }

        /* Distinct Colors for each tab */
        .tab-btn-theory:hover, [onclick*="theory"]:hover { color: #2563eb; background: #eff6ff; border-color: #bfdbfe; }
        .tab-btn-theory.active, [onclick*="theory"].active { background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important; color: #fff !important; border-color: #2563eb !important; box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35) !important; }

        .tab-btn-vocab:hover, [onclick*="vocab"]:hover { color: #059669; background: #ecfdf5; border-color: #a7f3d0; }
        .tab-btn-vocab.active, [onclick*="vocab"].active { background: linear-gradient(135deg, #10b981, #047857) !important; color: #fff !important; border-color: #059669 !important; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35) !important; }

        .tab-btn-kanji:hover, [onclick*="kanji"]:hover { color: #d97706; background: #fffbeb; border-color: #fde68a; }
        .tab-btn-kanji.active, [onclick*="kanji"].active { background: linear-gradient(135deg, #f59e0b, #d97706) !important; color: #fff !important; border-color: #d97706 !important; box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35) !important; }

        .tab-btn-quiz:hover, [onclick*="quiz"]:hover { color: #e11d48; background: #fff1f2; border-color: #fecdd3; }
        .tab-btn-quiz.active, [onclick*="quiz"].active { background: linear-gradient(135deg, #e11d48, #be123c) !important; color: #fff !important; border-color: #e11d48 !important; box-shadow: 0 4px 14px rgba(225, 29, 72, 0.35) !important; }

        .tab-btn-typing:hover, [onclick*="typing"]:hover { color: #0284c7; background: #f0f9ff; border-color: #bae6fd; }
        .tab-btn-typing.active, [onclick*="typing"].active { background: linear-gradient(135deg, #0284c7, #0369a1) !important; color: #fff !important; border-color: #0284c7 !important; box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35) !important; }

        .tab-btn-cheatsheet:hover, [onclick*="cheatsheet"]:hover { color: #7c3aed; background: #faf5ff; border-color: #ddd6fe; }
        .tab-btn-cheatsheet.active, [onclick*="cheatsheet"].active { background: linear-gradient(135deg, #8b5cf6, #6d28d9) !important; color: #fff !important; border-color: #7c3aed !important; box-shadow: 0 4px 14px rgba(139, 92, 246, 0.35) !important; }

        /* Tab Content Panels */
        .tab-panel {
            display: none;
            animation: fadeIn 0.25s ease;
        }
        .tab-panel.active {
            display: block;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Card Common */
        .content-card {
            background: var(--white);
            border-radius: var(--radius-lg);
            border: 1px solid var(--gray-200);
            padding: 28px;
            box-shadow: var(--shadow-sm);
            margin-bottom: 25px;
        }
        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--gray-100);
            flex-wrap: wrap;
            gap: 12px;
        }
        .section-title {
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--gray-900);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .section-badge {
            font-size: 0.8rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: var(--radius-full);
            background: var(--primary-light);
            color: var(--primary);
        }

        /* Grammar Styles */
        .theory-quicknav {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
            margin-bottom: 24px;
        }
        .quicknav-pill {
            padding: 9px 18px;
            border-radius: var(--radius-full);
            font-size: 0.88rem;
            font-weight: 800;
            text-decoration: none;
            white-space: nowrap;
            transition: all 0.2s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .qn-b15 { background: #eff6ff; color: #1d4ed8; border: 1.5px solid #bfdbfe; }
        .qn-b15:hover { background: #2563eb; color: #ffffff; border-color: #2563eb; transform: translateY(-2px); }
        .qn-b16 { background: #ecfdf5; color: #047857; border: 1.5px solid #a7f3d0; }
        .qn-b16:hover { background: #059669; color: #ffffff; border-color: #059669; transform: translateY(-2px); }
        .qn-b17 { background: #faf5ff; color: #6d28d9; border: 1.5px solid #ddd6fe; }
        .qn-b17:hover { background: #7c3aed; color: #ffffff; border-color: #7c3aed; transform: translateY(-2px); }
        .qn-b18 { background: #fff1f2; color: #be123c; border: 1.5px solid #fecdd3; }
        .qn-b18:hover { background: #e11d48; color: #ffffff; border-color: #e11d48; transform: translateY(-2px); }

        .grammar-card, [id^="grammar-"] {
            scroll-margin-top: 100px;
        }
        .grammar-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-lg);
            margin-bottom: 24px;
            overflow: hidden;
            box-shadow: var(--shadow-sm);
        }
        .grammar-header {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            padding: 20px 24px;
            border-bottom: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }
        .grammar-tag {
            font-size: 0.75rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--primary);
            background: var(--primary-light);
            padding: 4px 10px;
            border-radius: var(--radius-sm);
            display: inline-block;
            margin-bottom: 6px;
        }
        .grammar-title {
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--gray-900);
        }
        .grammar-body {
            padding: 24px;
        }
        .formula-box {
            background: #f0fdf4;
            border-left: 4px solid var(--success);
            padding: 14px 18px;
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            font-weight: 700;
            color: #166534;
            margin-bottom: 16px;
            font-size: 1.02rem;
        }
        .grammar-explain {
            color: var(--gray-700);
            margin-bottom: 18px;
            font-size: 0.95rem;
        }
        .example-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .example-item {
            background: var(--gray-50);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 14px 18px;
        }
        .ex-jp {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--gray-900);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
        }
        .ex-vi {
            font-size: 0.9rem;
            color: var(--gray-600);
        }
        .trap-box {
            background: #fffbeb;
            border-left: 4px solid var(--warning);
            padding: 14px 18px;
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            margin-top: 18px;
            font-size: 0.92rem;
            color: #92400e;
        }

        /* Vocab Styles */
        .vocab-controls {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .vocab-filter-group {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }
        .v-filter-btn {
            padding: 6px 14px;
            border-radius: var(--radius-full);
            border: 1px solid var(--gray-300);
            background: var(--white);
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--gray-700);
            cursor: pointer;
            transition: all 0.2s;
        }
        .v-filter-btn.active {
            background: var(--primary);
            color: var(--white);
            border-color: var(--primary);
        }
        .search-input {
            padding: 8px 16px;
            border-radius: var(--radius-full);
            border: 1px solid var(--gray-300);
            font-size: 0.9rem;
            outline: none;
            min-width: 240px;
        }
        .search-input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
        }
        .vocab-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 16px;
        }
        .vocab-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 16px;
            transition: all 0.2s;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .vocab-card:hover {
            border-color: var(--primary);
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }
        .vocab-card-header {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 8px;
        }
        .vocab-jp {
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--gray-900);
        }
        .vocab-kana {
            font-size: 0.88rem;
            color: var(--primary);
            font-weight: 600;
        }
        .vocab-badge {
            font-size: 0.72rem;
            padding: 2px 8px;
            border-radius: var(--radius-full);
            background: var(--gray-100);
            color: var(--gray-600);
            font-weight: 700;
        }
        .vocab-vi {
            font-size: 0.95rem;
            color: var(--gray-700);
            margin-top: 8px;
            padding-top: 8px;
            border-top: 1px dashed var(--gray-200);
        }
        .vocab-vi.hidden-meaning {
            filter: blur(5px);
            user-select: none;
            transition: filter 0.2s;
        }
        .vocab-vi.hidden-meaning:hover {
            filter: none;
        }
        .audio-btn {
            background: var(--primary-light);
            color: var(--primary);
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 0.9rem;
            flex-shrink: 0;
        }
        .audio-btn:hover {
            background: var(--primary);
            color: var(--white);
        }

        /* Kanji Styles */
        .kanji-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
            gap: 18px;
        }
        .kanji-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 18px;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .kanji-main {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .kanji-char {
            width: 60px;
            height: 60px;
            border-radius: var(--radius-md);
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border: 2px solid #bbf7d0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
            font-weight: 900;
            color: #166534;
        }
        .kanji-info {
            flex: 1;
        }
        .kanji-hv {
            font-size: 1.1rem;
            font-weight: 800;
            color: var(--gray-900);
        }
        .kanji-meaning {
            font-size: 0.88rem;
            color: var(--gray-600);
        }
        .kanji-readings {
            font-size: 0.85rem;
            background: var(--gray-50);
            padding: 8px 12px;
            border-radius: var(--radius-sm);
        }
        .kanji-mnemonic {
            font-size: 0.82rem;
            color: #475569;
            background: #fffbeb;
            padding: 8px 12px;
            border-radius: var(--radius-sm);
            border-left: 3px solid var(--warning);
        }

        /* Quiz & Exam Section */
        .exam-switcher-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-lg);
            padding: 18px 20px;
            margin-bottom: 18px;
            box-shadow: var(--shadow-sm);
        }
        .exam-switcher-grid {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 10px;
        }
        @media (max-width: 1024px) {
            .exam-switcher-grid {
                grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            }
        }
        .exam-switch-btn {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 4px;
            padding: 12px 14px;
            border-radius: var(--radius-md);
            border: 2px solid var(--gray-200);
            background: var(--gray-50);
            cursor: pointer;
            text-align: left;
            transition: all 0.2s ease;
        }
        .exam-switch-btn:hover {
            border-color: var(--primary);
            background: var(--white);
            transform: translateY(-1px);
        }
        .exam-switch-btn.active {
            border-color: var(--primary);
            background: var(--primary-light);
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.14);
        }
        .exam-switch-top {
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 6px;
        }
        .exam-switch-code {
            font-size: 0.78rem;
            font-weight: 800;
            color: var(--primary-dark);
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }
        .exam-switch-score {
            font-size: 0.74rem;
            font-weight: 800;
            padding: 2px 7px;
            border-radius: var(--radius-full);
            background: var(--gray-200);
            color: var(--gray-700);
        }
        .exam-switch-score.has-score {
            background: var(--success-light);
            color: #065f46;
        }
        .exam-switch-name {
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--gray-900);
            line-height: 1.3;
        }
        .exam-timer-box {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
            color: var(--white);
            padding: 16px 24px;
            border-radius: var(--radius-lg);
            margin-bottom: 24px;
            flex-wrap: wrap;
            gap: 14px;
        }
        .exam-score-display {
            font-size: 1.3rem;
            font-weight: 800;
            color: #a5b4fc;
        }
        .exam-part-header {
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            padding: 14px 20px;
            border-radius: var(--radius-md);
            margin: 30px 0 18px 0;
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--gray-900);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .question-item {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: var(--shadow-sm);
        }
        .q-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--gray-900);
            margin-bottom: 12px;
            display: flex;
            align-items: baseline;
            gap: 8px;
        }
        .q-badge {
            font-size: 0.75rem;
            padding: 3px 8px;
            border-radius: var(--radius-full);
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 800;
        }
        .options-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 10px;
            margin-bottom: 12px;
        }
        .opt-btn {
            padding: 12px 16px;
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-md);
            background: var(--white);
            text-align: left;
            font-size: 0.98rem;
            font-weight: 600;
            color: var(--gray-800);
            cursor: pointer;
            transition: all 0.2s;
        }
        .opt-btn:hover {
            border-color: var(--primary);
            background: var(--gray-50);
        }
        .opt-btn.is-correct {
            background: #dcfce7 !important;
            border-color: #22c55e !important;
            color: #15803d !important;
            font-weight: 800;
        }
        .opt-btn.is-wrong {
            background: #fee2e2 !important;
            border-color: #ef4444 !important;
            color: #b91c1c !important;
        }
        .explain-box {
            display: none;
            background: #eff6ff;
            border-left: 4px solid var(--secondary);
            padding: 12px 16px;
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            font-size: 0.92rem;
            color: #1e40af;
            margin-top: 10px;
        }

        /* Sentence Arrange Chips */
        .arrange-slot-box {
            min-height: 48px;
            border: 2px dashed var(--gray-300);
            border-radius: var(--radius-md);
            padding: 8px 12px;
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
            background: var(--gray-50);
            margin: 12px 0;
        }
        .chip-btn {
            padding: 8px 14px;
            background: var(--white);
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-full);
            font-weight: 700;
            font-size: 0.95rem;
            color: var(--gray-800);
            cursor: pointer;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s;
        }
        .chip-btn:hover {
            background: var(--primary-light);
            color: var(--primary);
            border-color: var(--primary);
        }
        .chip-btn.in-slot {
            background: var(--primary);
            color: var(--white);
            border-color: var(--primary);
        }

        /* Conjugation Input */
        .conjugate-input {
            padding: 8px 14px;
            border: 2px solid var(--gray-300);
            border-radius: var(--radius-md);
            font-size: 1rem;
            font-weight: 700;
            outline: none;
            width: 180px;
            transition: border-color 0.2s;
        }
        .conjugate-input:focus {
            border-color: var(--primary);
        }
        .conjugate-input.is-correct {
            border-color: var(--success);
            background: #f0fdf4;
            color: #166534;
        }
        .conjugate-input.is-wrong {
            border-color: var(--accent);
            background: #fff1f2;
            color: #be123c;
        }

        /* Matching Grid */
        .matching-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 16px 0;
        }
        @media (max-width: 768px) {
            .matching-grid {
                grid-template-columns: 1fr;
            }
        }
        .match-card {
            padding: 14px 18px;
            background: var(--white);
            border: 2px solid var(--gray-300);
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: all 0.2s;
            margin-bottom: 10px;
            font-size: 0.98rem;
        }
        .match-card:hover {
            border-color: var(--primary);
        }
        .match-card.selected {
            border-color: var(--primary);
            background: var(--primary-light);
            font-weight: 700;
        }
        .match-card.matched {
            border-color: var(--success);
            background: #dcfce7;
            cursor: default;
        }

        /* Reading Passage Box */
        .reading-box {
            background: #f8fafc;
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-md);
            padding: 20px 24px;
            margin-bottom: 18px;
            line-height: 1.85;
            font-size: 1.05rem;
            color: var(--gray-900);
        }

        /* Buttons & Actions */
        .btn-primary {
            padding: 10px 20px;
            border-radius: var(--radius-md);
            background: var(--primary);
            color: var(--white);
            font-weight: 700;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .btn-primary:hover {
            background: var(--primary-dark);
            transform: translateY(-1px);
        }
        .btn-quizlet {
            background: linear-gradient(135deg, #0284c7, #06b6d4);
            color: var(--white);
            padding: 8px 16px;
            border-radius: var(--radius-md);
            font-weight: 700;
            border: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.88rem;
        }
        .btn-quizlet:hover {
            opacity: 0.95;
            transform: translateY(-1px);
        }

        /* Typing Practice Styles */
        .typing-container {
            background: var(--white);
            border-radius: var(--radius-lg);
            border: 1px solid var(--gray-200);
            padding: 30px;
            box-shadow: var(--shadow-sm);
        }
        .typing-card-view {
            max-width: 680px;
            margin: 0 auto;
            text-align: center;
        }
        .typing-prompt {
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--gray-900);
            margin: 20px 0;
            min-height: 50px;
        }
        .typing-input-large {
            width: 100%;
            max-width: 520px;
            padding: 16px 20px;
            font-size: 1.3rem;
            font-weight: 700;
            border: 3px solid var(--gray-300);
            border-radius: var(--radius-lg);
            text-align: center;
            outline: none;
            transition: all 0.2s;
            margin-bottom: 16px;
        }
        .typing-input-large:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.15);
        }
        .typing-input-large.correct {
            border-color: var(--success);
            background: #f0fdf4;
            color: #166534;
        }
        .typing-input-large.wrong {
            border-color: var(--accent);
            background: #fff1f2;
            color: #be123c;
        }
        .typing-streak {
            font-size: 1.1rem;
            font-weight: 800;
            color: #ea580c;
            margin-bottom: 12px;
        }
        .typing-actions {
            display: flex;
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 14px;
        }
        .tp-mode-switch {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin: 14px 0 18px 0;
            padding: 6px;
            background: var(--gray-100);
            border-radius: var(--radius-md);
        }
        .tp-mode-pill {
            flex: 1;
            min-width: 190px;
            padding: 11px 16px;
            border: 2px solid transparent;
            border-radius: var(--radius-sm);
            background: transparent;
            color: var(--gray-700);
            font-weight: 800;
            font-size: 0.92rem;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }
        .tp-mode-pill:hover {
            background: rgba(255, 255, 255, 0.8);
            color: var(--primary);
        }
        .tp-mode-pill.active {
            background: var(--white);
            color: var(--primary);
            border-color: var(--primary);
            box-shadow: var(--shadow-sm);
        }
        .tp-toolbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px dashed var(--gray-200);
        }
        .tp-toggles {
            display: flex;
            gap: 14px;
            align-items: center;
            flex-wrap: wrap;
            font-size: 0.85rem;
            color: var(--gray-700);
            font-weight: 600;
        }
        .tp-toggles label {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            user-select: none;
        }
        .tp-kanji-hero {
            font-size: 3.1rem;
            font-weight: 900;
            color: var(--primary-dark);
            letter-spacing: 0.04em;
            line-height: 1.3;
            margin: 12px 0;
        }
        .tp-vi-hero {
            font-size: 1.45rem;
            font-weight: 800;
            color: var(--gray-900);
            line-height: 1.45;
            margin: 12px 0 8px 0;
        }
        .tp-pattern-badge {
            display: inline-block;
            background: #fef3c7;
            color: #b45309;
            font-weight: 800;
            font-size: 0.8rem;
            padding: 4px 12px;
            border-radius: var(--radius-full);
            margin-top: 4px;
        }
        .tp-detail-panel {
            margin-top: 20px;
            text-align: left;
            border-radius: var(--radius-md);
            padding: 20px 22px;
            border: 2px solid var(--gray-200);
            background: var(--gray-50);
            display: none;
        }
        .tp-detail-panel.show {
            display: block;
        }
        .tp-detail-panel.is-ok {
            background: #f0fdf4;
            border-color: #86efac;
        }
        .tp-detail-panel.is-err {
            background: #fff1f2;
            border-color: #fda4af;
        }
        .tp-detail-panel.is-reveal {
            background: #fffbeb;
            border-color: #fcd34d;
        }
        .tp-why-box {
            background: rgba(255, 255, 255, 0.9);
            border-left: 4px solid var(--accent);
            padding: 12px 15px;
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            margin: 12px 0;
            font-size: 0.94rem;
            color: #9f1239;
            line-height: 1.65;
        }
        .tp-meaning-box {
            background: rgba(255, 255, 255, 0.95);
            border-left: 4px solid var(--primary);
            padding: 12px 15px;
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            margin-top: 10px;
            font-size: 0.93rem;
            color: var(--gray-800);
            line-height: 1.65;
        }
        .tp-diff-row {
            display: grid;
            grid-template-columns: 1fr;
            gap: 8px;
            margin: 10px 0;
            padding: 12px;
            background: var(--white);
            border-radius: var(--radius-sm);
            border: 1px solid var(--gray-200);
        }
        .diff-bad {
            background: #fecdd3;
            color: #9f1239;
            text-decoration: underline wavy #e11d48;
            padding: 0 2px;
            border-radius: 3px;
            font-weight: 800;
        }
        .diff-good {
            background: #bbf7d0;
            color: #166534;
            padding: 0 2px;
            border-radius: 3px;
            font-weight: 800;
        }
        .tp-overview-drawer {
            display: none;
            margin: 14px 0 22px 0;
            padding: 16px;
            background: var(--gray-50);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-md);
            max-height: 300px;
            overflow-y: auto;
        }
        .tp-overview-drawer.show {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
            gap: 8px;
        }
        .tp-overview-item {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 10px;
            border-radius: var(--radius-sm);
            background: var(--white);
            border: 1px solid var(--gray-200);
            cursor: pointer;
            font-size: 0.82rem;
            text-align: left;
            transition: all 0.15s;
        }
        .tp-overview-item:hover {
            border-color: var(--primary);
        }
        .tp-overview-item.active {
            border-color: var(--primary);
            background: var(--primary-light);
            font-weight: 700;
        }
        .tp-overview-item.done-ok {
            border-left: 4px solid var(--success);
        }
        .tp-overview-item.done-err {
            border-left: 4px solid var(--accent);
        }

        /* Toast */
        #toast {
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #0f172a;
            color: #ffffff;
            padding: 12px 24px;
            border-radius: var(--radius-full);
            font-weight: 700;
            font-size: 0.95rem;
            box-shadow: var(--shadow-lg);
            z-index: 1000;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            pointer-events: none;
        }
        #toast.show {
            opacity: 1;
            transform: translateY(0);
        }

        @media (max-width: 768px) {
            .hero-header {
                padding: 30px 16px 24px 16px;
            }
            .main-container {
                padding: 16px 12px 60px 12px;
            }
            .content-card {
                padding: 20px 16px;
            }
            .options-list {
                grid-template-columns: 1fr;
            }
            .vocab-grid, .kanji-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    <link rel="stylesheet" href="../assets/css/site-theme.css?v=6">
</head>
<body>

<div class="container">

    <!-- Global Hub Navigation Placeholder -->
    <div id="navbar-placeholder"></div>

    <!-- Hero Header -->
    <header class="hero-banner">
        <div class="hero-badge">🎓 MARUGOTO A2-1 • BỘ 5 MÃ ĐỀ BÀI 15 - 18</div>
        <h1 class="hero-title">Bộ 5 Đề Thi Thử & Cẩm Nang Ôn Tập Bài 15 - 18</h1>
        <p class="hero-desc">Hệ thống tổng hợp toàn diện 4 bài (L15–L18): Lý thuyết chuyên sâu, 135 từ vựng Quizlet sạch, 34 chữ Hán chiết tự, Bộ 5 Mã Đề (160 câu chuẩn 100 điểm/đề) & Luyện gõ phản xạ Nhật - Việt.</p>
        <div class="hero-stats">
            <span class="hero-stat-pill">📖 4 Bài Học (L15 ➔ L18)</span>
            <span class="hero-stat-pill">🎴 135 Từ Vựng Cốt Lõi</span>
            <span class="hero-stat-pill">⛩️ 34 Chữ Hán Kanji</span>
            <span class="hero-stat-pill">🎯 Bộ 5 Mã Đề 100đ (160 Câu)</span>
            <span class="hero-stat-pill">⌨️ Flash Typing Gõ Nhật - Việt</span>
        </div>
    </header>

    <!-- Sticky Tab Navigation -->
    <div class="tab-nav-wrapper">
        <nav class="tab-nav">
            <button class="tab-btn tab-btn-theory active" onclick="switchMainTab('tab-theory')">📖 Lý Thuyết (L15-18)</button>
            <button class="tab-btn tab-btn-vocab" onclick="switchMainTab('tab-vocab')">🎴 135 Từ Vựng</button>
            <button class="tab-btn tab-btn-kanji" onclick="switchMainTab('tab-kanji')">⛩️ 34 Chữ Hán</button>
            <button class="tab-btn tab-btn-quiz" onclick="switchMainTab('tab-quiz')">🎯 Bộ 5 Mã Đề (160 Câu)</button>
            <button class="tab-btn tab-btn-typing" onclick="switchMainTab('tab-typing')">⌨️ Luyện Gõ Câu & Kanji ➔ Hira</button>
            <button class="tab-btn tab-btn-cheatsheet" onclick="switchMainTab('tab-cheatsheet')">⚡ Cẩm Nang Bỏ Túi</button>
        </nav>
    </div>

        <!-- ========================================== -->
        <!-- TAB 1: LÝ THUYẾT NGỮ PHÁP (BÀI 15 - 18)    -->
        <!-- ========================================== -->
        <div id="tab-theory" class="tab-panel active">
            <!-- Quick Jump Bar -->
            <div class="theory-quicknav">
                <a href="#grammar-l15" class="quicknav-pill qn-b15">🏥 Bài 15 (～んです／といい／ないで)</a>
                <a href="#grammar-l16" class="quicknav-pill qn-b16">🏃 Bài 16 (～たり／ために／V thường+N)</a>
                <a href="#grammar-l17" class="quicknav-pill qn-b17">🎁 Bài 17 (もらう／あげる／とか／んです)</a>
                <a href="#grammar-l18" class="quicknav-pill qn-b18">💐 Bài 18 (～と思う／と言う／お祝い)</a>
            </div>

            <!-- BÀI 15 -->
            <div class="grammar-card" id="grammar-l15">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 15 (A2-1 • SỨC KHỎE)</span>
                        <h2 class="grammar-title">たいそうすると いいですよ (Sức Khỏe & Triệu Chứng • Giải Thích & Lời Khuyên)</h2>
                    </div>
                    <span class="section-badge">Chuẩn Giáo Trình</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Hỏi & giải thích triệu chứng, lý do: <code>どうしたんですか。</code> ➔ <code>[Thể thông thường] ＋ んです</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Động từ / Tính từ い: <code>ねられないんです</code> / <code>頭が いたいんです</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Tính từ な / Danh từ (<code>だ ➔ な</code>): <code>びょうきなんです</code> / <code>たいへんなんです</code><br>
                        2. Lời khuyên gợi ý nhẹ nhàng: <code>V(thể từ điển V-る) ＋ と いいですよ</code> (Làm V thì tốt đấy)<br>
                        3. Đề nghị đừng làm V: <code>V(thể Phủ định ngắn V-ない) ＋ で ください</code> (Xin đừng làm V)
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <code>〜んですか / 〜んです</code>: Dùng khi thấy người khác có vẻ mệt mỏi để hỏi thăm tình hình <em>(どうしたんですか)</em> và để người nói giải thích lý do, hoàn cảnh của mình.<br>
                        • <code>〜と いいですよ</code>: Đưa ra lời khuyên gợi ý nhẹ nhàng tốt cho sức khỏe.<br>
                        • <code>〜ないで ください</code>: Dặn dò đừng làm hành động quá sức hoặc không tốt cho cơ thể.
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">「どうしたんですか。」――「さいきん、ちょっと こしが <span style="color: var(--primary);">いたいんです</span>。」
                                <button type="button" class="audio-btn" onclick="speakText('どうしたんですか。さいきん、ちょっとこしがいたいんです。')">🔊</button>
                            </div>
                            <div class="ex-vi">"Bạn bị làm sao thế?" ―― "Gần đây eo/lưng của tôi hơi bị đau một chút."</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">ねる まえに、おふろに <span style="color: var(--primary);">入ると いいですよ</span>。
                                <button type="button" class="audio-btn" onclick="speakText('ねるまえに、おふろにはいるといいですよ。')">🔊</button>
                            </div>
                            <div class="ex-vi">Trước khi đi ngủ, bạn nên tắm bồn thì rất tốt đấy!</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">あまり <span style="color: var(--primary);">無理を しないで ください</span>。お酒を <span style="color: var(--primary);">飲まないで ください</span>。
                                <button type="button" class="audio-btn" onclick="speakText('あまりむりをしないでください。おさけをのまないでください。')">🔊</button>
                            </div>
                            <div class="ex-vi">Xin đừng làm quá sức quá nhé. Đừng uống rượu nhé.</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Trước <code>といいですよ</code> luôn là <strong>V-る (thể từ điển)</strong>, KHÔNG chia quá khứ V-た. Trước <code>でください</code> là <strong>V-ない</strong>!
                    </div>
                </div>
            </div>

            <!-- BÀI 16 -->
            <div class="grammar-card" id="grammar-l16">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 16 (A2-1 • VẬN ĐỘNG & BỔ NGHĨA)</span>
                        <h2 class="grammar-title">走ったり、泳いだりしています & Mệnh Đề Bổ Nghĩa V〈ふつうけい〉＋ 人 / N</h2>
                    </div>
                    <span class="section-badge">Trọng tâm NPBS 16</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Nêu hành động tiêu biểu: <code>V1-たり、V2-たり します / しています</code> (Có thể nêu 1 hoặc 2 hành động tiêu biểu)<br>
                        2. Hỏi & nói mục đích: <code>何の ために 〜ていますか</code> ➔ <code>[Danh từ] の ために 〜ています</code><br>
                        3. <strong>Mệnh đề bổ nghĩa cho danh từ:</strong> <code>V〈ふつうけい (Thể thường)〉＋ 人 / Danh từ (N)</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• <code>Vます ➔ Vる</code> | <code>Vません ➔ Vない</code> | <code>Vました ➔ Vた</code> | <code>Vていません ➔ Vていない</code>
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <code>〜たり、〜たり します</code>: Đuôi <code>します</code> ở cuối câu chia linh hoạt theo các ngữ pháp đã học (quá khứ <code>しました</code>, thói quen <code>しています</code>).<br>
                        • <code>V〈ふつうけい〉＋ 人 / N</code>: Dùng động từ chia thể thông thường đặt <strong>ngay trước danh từ</strong> để bổ nghĩa ("Người mà...", "Cái mà...").
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">毎日 さんぽしたり、ヨガを <span style="color: var(--primary);">したり して います</span>。
                                <button type="button" class="audio-btn" onclick="speakText('まいにちさんぽしたり、ヨガをしたりしています。')">🔊</button>
                            </div>
                            <div class="ex-vi">Hằng ngày tôi đi dạo, tập yoga v.v...</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">よく 本を <span style="color: var(--primary);">読む 人</span>は 頭が いいです。コーヒーを <span style="color: var(--primary);">飲まない 人</span>は 10人です。
                                <button type="button" class="audio-btn" onclick="speakText('よくほんをよむひとはあたまがいいです。コーヒーをのまないひとはじゅうにんです。')">🔊</button>
                            </div>
                            <div class="ex-vi">Người hay đọc sách thì thông minh. Số người không uống cà phê là 10 người.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">たばこを <span style="color: var(--primary);">すわない 人</span>は かっこいいです。野菜を <span style="color: var(--primary);">食べない 子ども</span>は あまり 元気じゃないです。
                                <button type="button" class="audio-btn" onclick="speakText('たばこをすわないひとはかっこいいです。やさいをたべないこどもはあまりげんきじゃないです。')">🔊</button>
                            </div>
                            <div class="ex-vi">Người không hút thuốc lá thì thật ngầu. Đứa trẻ không ăn rau thì không khỏe lắm.</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Trước danh từ <code>人 / N</code> TUYỆT ĐỐI không được dùng đuôi lịch sự <code>ます / ません / ました</code>! Phải chuyển sang thể thông thường (<code>Vる / Vない / Vた / Vている</code>).
                    </div>
                </div>
            </div>

            <!-- BÀI 17 -->
            <div class="grammar-card" id="grammar-l17">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 17 (A2-1 • QUÀ TẶNG & ～んです)</span>
                        <h2 class="grammar-title">誕生日に かれに もらったんです (Cho-Nhận, とか, V thường+N & Thể thường+んです)</h2>
                    </div>
                    <span class="section-badge">Trọng tâm NPBS 17</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Nhận quà: <code>[Người tặng] に [Vật] を もらいました / もらったんです</code><br>
                        2. Tặng quà: <code>[Người nhận] に [Vật] を あげます / あげました</code><br>
                        3. Liệt kê đại diện: <code>N1 とか N2 とか</code> | Đồ vật dùng để làm gì: <code>V〈ふつうけい〉＋ もの / N</code><br>
                        4. Tổng hợp <code>Thể thông thường ＋ んです（だ ➔ な）</code>: Mở đầu nhờ vả <code>～んですが</code>, hỏi thăm <code>どうしたんですか</code>, hỏi lý do <code>どうして～んですか</code>.
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <strong>Biến đổi だ ➔ な:</strong> Danh từ & Tính từ đuôi な đổi <code>だ</code> thành <code>な</code> trước <code>んです</code> (<em>きらいなんです, しずかなんです, びょうきなんです, たいへんなんです</em>).<br>
                        • <strong>Định ngữ bổ nghĩa cho danh từ (V thể thường + N):</strong> <em>きのう 買った 本, 日本で はたらいている 人, 母が 作った 料理, 毎日 使う パソコン, あかちゃんが 着る もの</em>.
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">この 時計は そつぎょうの お祝いに <span style="color: var(--primary);">父に もらったんです</span>。
                                <button type="button" class="audio-btn" onclick="speakText('このとけいはそつぎょうのおいわいに、ちちにもらったんです。')">🔊</button>
                            </div>
                            <div class="ex-vi">Chiếc đồng hồ này là tôi nhận được từ bố nhân dịp chúc mừng tốt nghiệp đấy.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">日本語が よく <span style="color: var(--primary);">分からないんですが</span>、おしえて くださいませんか。
                                <button type="button" class="audio-btn" onclick="speakText('にほんごがよくわからないんですが、おしえてくださいませんか。')">🔊</button>
                            </div>
                            <div class="ex-vi">Tôi không hiểu tiếng Nhật lắm, bạn có thể chỉ cho tôi được không ạ? (～んですが mở đầu nhờ vả)</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">「どうして おくれたんですか。」――「道が <span style="color: var(--primary);">じゅうたいなんです</span>。」
                                <button type="button" class="audio-btn" onclick="speakText('どうしておくれたんですか。みちがじゅうたいなんです。')">🔊</button>
                            </div>
                            <div class="ex-vi">"Tại sao bạn đến muộn vậy?" ―― "Vì đường bị tắc nghẽn đấy ạ."</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Trợ từ đứng trước động từ cho-nhận: <code>もらいます</code> ➔ đứng trước <code>に</code> là NGƯỜI TẶNG. <code>あげます</code> ➔ đứng trước <code>に</code> là NGƯỜI NHẬN!
                    </div>
                </div>
            </div>

            <!-- BÀI 18 -->
            <div class="grammar-card" id="grammar-l18">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 18 (A2-1 • CHÚC MỪNG & Ý KIẾN)</span>
                        <h2 class="grammar-title">パーティーが いいと 思います (Bày Tỏ Ý Kiến, Trích Dẫn & Chúc Mừng)</h2>
                    </div>
                    <span class="section-badge">Chuẩn Giáo Trình</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Bày tỏ suy nghĩ, ý kiến cá nhân: <code>[Thể thông thường (Futsuukei)] ＋ と 思います</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Động từ / Tính từ đuôi い: <code>よろこぶ と 思います</code> / <code>パーティーが いい と 思います</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• <strong>Danh từ / Tính từ đuôi な (Hiện tại khẳng định):</strong> <code>[N / Na] ＋ だ ＋ と 思います</code><br>
                        2. Trích dẫn lại lời người khác đã nói: <code>[Thể thông thường] ＋ と 言っていました</code><br>
                        3. Giao tiếp chúc mừng & cảm ơn quà: <code>ご結婚 おめでとう ございます</code> / <code>おれいを 言います</code> / <code>たいせつに します</code>
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <code>〜と 思います</code>: Bày tỏ nhận xét, đề xuất ý kiến của bản thân khi bàn bạc tổ chức lễ chúc mừng hoặc chọn quà tặng.<br>
                        • <code>〜と 言っていました</code>: Truyền đạt lại lời nói, mong muốn của một người thứ ba (<em>あべさんは みんなと 話したいと 言っていました</em>).
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">お祝いは パーティーが <span style="color: var(--primary);">いいと 思います</span>。着物が <span style="color: var(--primary);">きれいだと 思います</span>。
                                <button type="button" class="audio-btn" onclick="speakText('おいわいはパーティーがいいとおもいます。きものがきれいだとおもいます。')">🔊</button>
                            </div>
                            <div class="ex-vi">Tôi nghĩ buổi chúc mừng tổ chức tiệc là hay. Tôi nghĩ bộ Kimono rất đẹp.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">あべさんは みんなと <span style="color: var(--primary);">話したいと 言っていました</span>。
                                <button type="button" class="audio-btn" onclick="speakText('あべさんはみんなとはなしたいといっていました。')">🔊</button>
                            </div>
                            <div class="ex-vi">Anh Abe đã nói là muốn trò chuyện với tất cả mọi người.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">たなかさんは パーティーが <span style="color: var(--primary);">楽しかったと 言っていました</span>。
                                <button type="button" class="audio-btn" onclick="speakText('たなかさんはパーティーがたのしかったといっていました。')">🔊</button>
                            </div>
                            <div class="ex-vi">Anh Tanaka đã nói là buổi tiệc rất vui.</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Trước <code>と 思います / と 言っていました</code>, nếu là Tính từ đuôi な hoặc Danh từ ở thì hiện tại khẳng định, BẮT BUỘC phải có <code>だ</code>: <em>「きれい【だ】と 思います」「しあわせ【だ】と 言っていました」</em>. Thiếu <code>だ</code> là sai!
                    </div>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 2: TỪ VỰNG CỐT LÕI (BÀI 15 - 18)       -->
        <!-- ========================================== -->
        <div id="tab-vocab" class="tab-panel">
            <div class="content-card">
                <div class="section-header">
                    <div>
                        <h2 class="section-title">🎴 135 Từ Vựng Cốt Lõi Bài 15 ➔ 18</h2>
                        <p style="color: var(--gray-600); font-size: 0.92rem; margin-top: 4px;">Toàn bộ từ vựng chính thức kèm phát âm chuẩn Tokyo, lọc theo bài học và nút sao chép Quizlet Tab siêu tốc.</p>
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <button type="button" class="btn-quizlet" onclick="copyVocabQuizletFormat()" title="Copy định dạng Tab sạch 100% cho Quizlet: [Từ Nhật] [Tab] [Nghĩa Việt]">📋 Copy Quizlet (Tab)</button>
                        <button type="button" class="btn-primary" onclick="toggleHideMeaning()" style="background: var(--gray-800);">👁️ Ẩn/Hiện Nghĩa</button>
                    </div>
                </div>

                <div class="vocab-controls">
                    <div class="vocab-filter-group" id="vocabFilterGroup">
                        <button type="button" class="v-filter-btn active" onclick="filterVocab('all')">Tất cả (135)</button>
                        <button type="button" class="v-filter-btn" onclick="filterVocab('A2-15')">Bài 15: Sức khỏe (57)</button>
                        <button type="button" class="v-filter-btn" onclick="filterVocab('A2-16')">Bài 16: Vận động (30)</button>
                        <button type="button" class="v-filter-btn" onclick="filterVocab('A2-17')">Bài 17: Quà tặng (29)</button>
                        <button type="button" class="v-filter-btn" onclick="filterVocab('A2-18')">Bài 18: Sự kiện (19)</button>
                    </div>
                    <input type="text" id="vocabSearchInput" class="search-input" placeholder="🔍 Tìm kiếm từ vựng (Nhật, Việt, Romaji)..." oninput="handleVocabSearch()">
                </div>

                <div class="vocab-grid" id="vocabGridContainer">
                    <!-- Rendered by JS -->
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 3: 34 CHỮ HÁN KANJI (BÀI 15 - 18)      -->
        <!-- ========================================== -->
        <div id="tab-kanji" class="tab-panel">
            <div class="content-card">
                <div class="section-header">
                    <div>
                        <h2 class="section-title">⛩️ 34 Chữ Hán Kanji Trọng Tâm Bài 15 ➔ 18</h2>
                        <p style="color: var(--gray-600); font-size: 0.92rem; margin-top: 4px;">Chiết tự nhớ lâu, mẹo ghi nhớ thú vị, âm Hán Việt, cách đọc On/Kun và các từ ghép thực tế trong bài thi.</p>
                    </div>
                    <button type="button" class="btn-quizlet" onclick="copyKanjiQuizletTabFormat()" title="Copy Kanji định dạng Tab cho Quizlet">📋 Copy Quizlet Kanji</button>
                </div>

                <div class="kanji-grid" id="kanjiGridContainer">
                    <!-- Rendered by JS -->
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 4: ĐỀ THI THỬ ĐA DẠNG NĂNG LỰC (100Đ)   -->
        <!-- ========================================== -->
        <div id="tab-quiz" class="tab-panel">
            <!-- Exam Switcher Card -->
            <div class="exam-switcher-card">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
                    <div>
                        <div style="font-size: 0.8rem; font-weight: 800; color: var(--primary); letter-spacing: 0.04em;">CHỌN MÃ ĐỀ LUYỆN TẬP (MỖI ĐỀ 32 CÂU • 100 ĐIỂM)</div>
                        <div id="activeExamSubtitle" style="font-size: 0.92rem; color: var(--gray-600); margin-top: 2px;"></div>
                    </div>
                    <div id="overallProgressSummary" style="font-size: 0.84rem; font-weight: 700; color: var(--gray-700); background: var(--gray-100); padding: 6px 14px; border-radius: var(--radius-full);">
                        Đã làm: 0 / 5 mã đề
                    </div>
                </div>
                <div class="exam-switcher-grid" id="examSwitcherGrid"></div>
            </div>

            <!-- Exam Timer & Score Bar -->
            <div class="exam-timer-box">
                <div>
                    <div id="examTimerHeaderTitle" style="font-size: 0.85rem; color: #c7d2fe; font-weight: 700;">MÃ ĐỀ 151 • TỔNG HỢP CHUẨN MARUGOTO A2-1 (BÀI 15 - 18)</div>
                    <div id="examTimerHeaderMeta" style="font-size: 1.3rem; font-weight: 800; margin-top: 2px;">6 Dạng Bài Chuẩn Sư Phạm • 32 Câu Hỏi</div>
                </div>
                <div style="display: flex; align-items: center; gap: 18px; flex-wrap: wrap;">
                    <div style="text-align: right;">
                        <div style="font-size: 0.82rem; color: #cbd5e1;">ĐIỂM SỐ MÃ ĐỀ NÀY</div>
                        <div class="exam-score-display" id="totalScoreText">0 / 100 Điểm</div>
                    </div>
                    <button type="button" class="btn-primary" onclick="resetAllExam()" style="background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25);">🔄 Làm Lại Đề Này</button>
                </div>
            </div>

            <!-- PHẦN I: TRẮC NGHIỆM TỔNG HỢP (10 CÂU - 25Đ) -->
            <div class="exam-part-header">
                <span>📌 PHẦN I: TRẮC NGHIỆM TỔNG HỢP NGỮ PHÁP & TRỢ TỪ (10 Câu • 25 Điểm)</span>
                <span style="font-size: 0.85rem; color: var(--primary);">2.5đ / câu</span>
            </div>
            <div id="part1Container"></div>

            <!-- PHẦN II: SẮP XẾP TỪ THÀNH CÂU HOÀN CHỈNH ★ (5 CÂU - 15Đ) -->
            <div class="exam-part-header">
                <span>⭐ PHẦN II: SẮP XẾP TỪ THÀNH CÂU HOÀN CHỈNH (並べ替え - 5 Câu • 15 Điểm)</span>
                <span style="font-size: 0.85rem; color: var(--primary);">3.0đ / câu</span>
            </div>
            <div id="part2Container"></div>

            <!-- PHẦN III: CHIA DẠNG ĐÚNG CỦA TỪ TRONG NGOẶC (5 CÂU - 15Đ) -->
            <div class="exam-part-header">
                <span>✍️ PHẦN III: CHIA DẠNG ĐÚNG CỦA TỪ TRONG NGOẶC (活用形 - 5 Câu • 15 Điểm)</span>
                <span style="font-size: 0.85rem; color: var(--primary);">3.0đ / câu</span>
            </div>
            <div id="part3Container"></div>

            <!-- PHẦN IV: NỐI CỘT TÌNH HUỐNG & HỘI THOẠI (4 CÂU - 10Đ) -->
            <div class="exam-part-header">
                <span>🔄 PHẦN IV: NỐI CỘT TÌNH HUỐNG & PHẢN XẠ THỰC TẾ (マッチング - 4 Câu • 10 Điểm)</span>
                <span style="font-size: 0.85rem; color: var(--primary);">2.5đ / câu</span>
            </div>
            <div id="part4Container"></div>

            <!-- PHẦN V: ĐỌC HIỂU ĐOẠN VĂN THỰC TẾ (4 CÂU - 20Đ) -->
            <div class="exam-part-header">
                <span>📖 PHẦN V: ĐỌC HIỂU ĐOẠN VĂN THỰC TẾ (読解 - 4 Câu / 2 Bài Đọc • 20 Điểm)</span>
                <span style="font-size: 0.85rem; color: var(--primary);">5.0đ / câu</span>
            </div>
            <div id="part5Container"></div>

            <!-- PHẦN VI: LUYỆN DỊCH CÂU THỰC CHIẾN (4 CÂU - 15Đ) -->
            <div class="exam-part-header">
                <span>🌐 PHẦN VI: LUYỆN DỊCH CÂU THỰC CHIẾN 2 CHIỀU (翻訳 - 4 Câu • 15 Điểm)</span>
                <span style="font-size: 0.85rem; color: var(--primary);">Tự đối chiếu & Chấm điểm</span>
            </div>
            <div id="part6Container"></div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 5: LUYỆN GÕ CÂU & CHỮ HÁN ➔ HIRAGANA  -->
        <!-- ========================================== -->
        <div id="tab-typing" class="tab-panel">
            <div class="typing-container">
                <div class="section-header">
                    <div>
                        <h2 class="section-title">⌨️ Luyện Gõ Ôn Tập Bài 11–18: Dịch Câu & Đọc Chữ Hán ➔ Hiragana</h2>
                        <p style="color: var(--gray-600); font-size: 0.92rem; margin-top: 4px;">
                            Luyện gõ theo bộ tài liệu cô gửi (<strong>PDF Tổng hợp ngữ pháp L11–L18</strong>, Kaiwa Mid 2 &amp; 2 file PDF Kanji 11–18). Chấm chi tiết <strong>nghĩa + công thức + giải thích vì sao sai</strong> và <strong>tự động lưu checkpoint</strong> từng câu!
                        </p>
                    </div>
                </div>

                <!-- Chọn chế độ luyện gõ -->
                <div class="tp-mode-switch" role="tablist" aria-label="Chế độ luyện gõ">
                    <button type="button" class="tp-mode-pill active" id="tpModeBtn_sentence" onclick="switchTypingMode('sentence')">🇻🇳 Câu Tiếng Việt ➔ Gõ Hiragana</button>
                    <button type="button" class="tp-mode-pill" id="tpModeBtn_kanji" onclick="switchTypingMode('kanji')">⛩️ Chữ Hán (Kanji) ➔ Gõ Hiragana</button>
                    <button type="button" class="tp-mode-pill" id="tpModeBtn_vocab" onclick="switchTypingMode('vocab')">🗂️ Từ Vựng A2 (135 từ)</button>
                </div>

                <!-- Bộ lọc bài học + Công cụ -->
                <div class="tp-toolbar">
                    <div class="vocab-filter-group" id="typingFilterGroup"></div>
                    <div class="tp-toggles">
                        <label id="tpKanjiAllowWrap" title="Nếu quên tắt bộ gõ Kanji vẫn chấp nhận nếu khớp mặt chữ chuẩn">
                            <input type="checkbox" id="tpAllowKanjiToggle" onchange="toggleTypingOption('allowKanji', this.checked)"> Cho phép kèm Kanji
                        </label>
                        <label title="Tắt mặc định để bạn đọc kỹ nghĩa và giải thích trước khi sang câu tiếp theo">
                            <input type="checkbox" id="tpAutoAdvToggle" onchange="toggleTypingOption('autoAdvance', this.checked)"> Tự nhảy câu khi đúng
                        </label>
                        <button type="button" class="vocab-action-btn" onclick="toggleTypingOverview()" id="tpOverviewBtn">📋 Danh Sách Câu</button>
                        <button type="button" class="vocab-action-btn" onclick="shuffleTypingPool()">🔀 Xáo Trộn</button>
                    </div>
                </div>

                <!-- Danh sách câu thu gọn -->
                <div class="tp-overview-drawer" id="tpOverviewDrawer"></div>

                <!-- Khung thẻ luyện gõ chính -->
                <div class="typing-card-view">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; gap:8px; flex-wrap:wrap;">
                        <span style="font-size:0.84rem; font-weight:800; color:var(--primary); background:var(--primary-light); padding:4px 12px; border-radius:var(--radius-full);" id="tpCardBadge">Câu 1 / --</span>
                        <span class="tp-pattern-badge" id="tpPatternBadge">Mẫu câu</span>
                        <div class="typing-streak" id="tpStreakBadge" style="margin:0;">🔥 Chuỗi: 0</div>
                    </div>

                    <div id="tpPromptArea" style="background:linear-gradient(135deg,#f8fafc 0%,#eef2ff 100%); border:1px solid #c7d2fe; border-radius:var(--radius-md); padding:20px 18px; margin:12px 0 18px 0;">
                        <div style="font-size:0.8rem; font-weight:700; color:var(--gray-500); text-transform:uppercase; letter-spacing:0.04em;" id="tpPromptSubtitle">ĐỀ BÀI TIẾNG VIỆT</div>
                        <div class="tp-vi-hero" id="tpPromptVi">Đang tải...</div>
                        <div id="tpHintPreview" style="display:none; margin-top:10px; padding:8px 12px; background:#ffffff; border-radius:8px; font-size:0.88rem; color:var(--primary-dark); border:1px dashed #a5b4fc;"></div>
                    </div>

                    <div style="font-size:0.86rem; font-weight:700; color:var(--gray-600); margin-bottom:8px;" id="tpInputDirective">
                        ⬇️ Nhập câu tiếng Nhật bằng <strong>Hiragana</strong> rồi nhấn Enter (hoặc Kiểm Tra):
                    </div>

                    <textarea class="typing-input-large jp-text" id="tpCardInput" rows="2" style="resize:vertical; min-height:66px; max-width:100%;" placeholder="Ví dụ: ねる まえに、よく ほんを よみます。" autocomplete="off" autocapitalize="off" spellcheck="false"></textarea>

                    <div class="typing-actions">
                        <button type="button" class="btn-primary" style="background:var(--gray-500);" onclick="prevTypingItem()">⬅️ Trước</button>
                        <button type="button" class="btn-primary" id="tpCardCheckBtn" onclick="handleTypingPrimaryBtn()">Kiểm Tra Đáp Án ⏎</button>
                        <button type="button" class="btn-primary" style="background:#0ea5e9;" onclick="speakCurrentTypingWord()">🔊 Nghe Mẫu</button>
                        <button type="button" class="btn-primary" style="background:var(--purple);" onclick="showTypingHint()">💡 Gợi Ý</button>
                        <button type="button" class="btn-primary" style="background:var(--warning);" onclick="revealTypingAnswer()">👁️ Xem Đáp Án</button>
                        <button type="button" class="btn-primary" style="background:var(--gray-600);" onclick="skipTypingWord()">Tiếp Theo ➔</button>
                        <button type="button" class="btn-primary" style="background:#be123c;" onclick="resetCurrentTypingMode()">🔄 Làm Lại Chế Độ Này</button>
                    </div>

                    <!-- Bảng giải thích chi tiết (Nghĩa + So sánh + Vì sao sai) -->
                    <div id="tpDetailPanel" class="tp-detail-panel"></div>

                    <div style="width:100%; height:10px; background:var(--gray-200); border-radius:10px; overflow:hidden; margin: 22px 0 12px 0;">
                        <div id="tpProgressBar" style="width:0%; height:100%; background:linear-gradient(90deg, var(--primary), var(--secondary)); transition:width 0.3s;"></div>
                    </div>

                    <div style="display:flex; justify-content:space-around; flex-wrap:wrap; gap:10px; font-size:0.95rem; font-weight:700; color:var(--gray-700);">
                        <span>✅ Đã làm đúng: <strong style="color:var(--success);" id="tpStatCorrect">0</strong></span>
                        <span>❌ Đang sai / cần ôn: <strong style="color:var(--accent);" id="tpStatWrong">0</strong></span>
                        <span>🎯 Đã chạm / tổng: <strong style="color:var(--primary);" id="tpStatPercent">0%</strong></span>
                    </div>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 6: CẨM NANG BỎ TÚI (CHEAT SHEET)       -->
        <!-- ========================================== -->
        <div id="tab-cheatsheet" class="tab-panel">
            <div class="content-card">
                <div class="section-header">
                    <div>
                        <h2 class="section-title">⚡ Cẩm Nang Bỏ Túi • Bí Kíp Tránh Bẫy Bài 15 ➔ 18</h2>
                        <p style="color: var(--gray-600); font-size: 0.92rem; margin-top: 4px;">Tổng hợp đúng 4 bẫy ngữ pháp trọng tâm của Bài 15-18 & Kiến Thức Bổ Sung trên lớp.</p>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
                    <!-- Cheatsheet 1 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">1. Khuyên Nhủ & Bối Cảnh ～んです (Bài 15 & 17)</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • <code>V-る ＋ と いいですよ</code>: Khuyên nhẹ nhàng nên làm gì (luôn dùng thể từ điển V-る!).<br>
                            • <code>V-ない ＋ で ください</code>: Dặn dò đừng làm gì (dùng thể Phủ định ngắn V-ない!).<br>
                            • <code>Thể thông thường ＋ んです</code>: Danh từ & Tính từ đuôi な phải đổi <strong>だ ➔ な</strong> (<em>びょうきなんです, しずかなんです, じゅうたいなんです</em>).
                        </p>
                    </div>

                    <!-- Cheatsheet 2 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">2. Mệnh Đề Bổ Nghĩa V〈ふつうけい〉＋ 人 / N (Bài 16 & 17)</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • Động từ bổ nghĩa luôn đặt <strong>TRƯỚC danh từ</strong> và phải chia về thể thông thường:<br>
                            &nbsp;&nbsp;<code>Vます ➔ Vる</code> | <code>Vません ➔ Vない</code> | <code>Vました ➔ Vた</code> | <code>Vています ➔ Vている</code>.<br>
                            • Ví dụ chuẩn: <em>よく 本を 読む 人</em>, <em>コーヒーを 飲まない 人</em>, <em>きのう 買った 本</em>, <em>母が 作った 料理</em>.
                        </p>
                    </div>

                    <!-- Cheatsheet 3 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">3. Ma Trận Cho - Nhận Quà Tặng (Bài 17)</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • <code>[Người tặng] に [Vật] を もらいました / もらったんです</code>: Nhận quà từ ai.<br>
                            • <code>[Người nhận] に [Vật] を あげます / あげました</code>: Tặng quà cho ai.<br>
                            • <strong>Mẹo phân biệt:</strong> Nhìn động từ cuối câu để biết người đứng trước trợ từ <code>に</code> là người tặng hay người nhận!<br>
                            • Liệt kê gợi ý quà tặng: <code>N1 とか N2 とか</code> (<em>絵とか 時計とか</em>).
                        </p>
                    </div>

                    <!-- Cheatsheet 4 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">4. Bẫy 「だ」 Trước と思います & と言っていました (Bài 18)</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • Động từ: <code>よろこぶ / 来られない / 楽しかった</code> + <code>と思います / と言っていました</code>.<br>
                            • Tính từ đuôi い: <code>いい / おもしろい</code> + <code>と思います</code>.<br>
                            • <strong>BẪY LỚN:</strong> Tính từ đuôi な và Danh từ ở thì hiện tại khẳng định BẮT BUỘC phải thêm <code>だ</code>:<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;➔ <em>きれい<strong>だ</strong>と思います</em> (Không nói: きれいと思います)<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;➔ <em>しあわせ<strong>だ</strong>と言っていました</em>.
                        </p>
                    </div>

                    <!-- Cheatsheet 5: PDF L11-L18 Bảng Ôn Nhanh & 6 Điểm Dễ Nhầm -->
                    <div style="grid-column: 1 / -1; background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border: 1px solid #fcd34d; border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.12rem; font-weight: 800; color: #b45309; margin-bottom: 10px;">5. Bảng Ôn Nhanh &amp; 6 Điểm Dễ Nhầm Toàn Tập L11–L18 (Theo PDF Cô Gửi)</h3>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 14px; font-size: 0.9rem; color: #78350f; line-height: 1.68;">
                            <div style="background: rgba(255,255,255,0.82); padding: 12px 14px; border-radius: 10px; border: 1px solid #fde68a;">
                                <strong style="color:#92400e;">📌 Ôn nhanh nền tảng L11–L14:</strong><br>
                                • <strong>L11:</strong> <code>Vて いきます / きます</code> (mua mang đi / mang tới); <code>いつでも・どこでも・なんでも いいです</code>; <code>N1と N2と、どちらが いいですか</code>.<br>
                                • <strong>L12:</strong> Bỏ <code>い/な</code> + <code>そうです</code> (trông có vẻ); <code>いAくて / なAで / Nで</code> (nguyên nhân).<br>
                                • <strong>L13:</strong> <code>Vた ことが あります</code> (đã từng); <code>すぎます</code> (quá); <code>S1 ですが、S2</code>.<br>
                                • <strong>L14:</strong> <code>Vて、3年に なります</code> (được 3 năm); <code>Vても いいですか</code> (xin phép) &amp; <code>すみません、ちょっと…</code> (từ chối khéo).
                            </div>
                            <div style="background: rgba(255,255,255,0.82); padding: 12px 14px; border-radius: 10px; border: 1px solid #fde68a;">
                                <strong style="color:#92400e;">🚨 6 Điểm dễ nhầm PDF Trang 19:</strong><br>
                                1. <strong>Mệnh đề bổ ngữ V + N:</strong> TUYỆT ĐỐI KHÔNG chen <code>の</code> (<s>とったのしゃしん</s> ❌ ➔ <code>とった しゃしん</code> ✅).<br>
                                2. <strong>Ngoại lệ 「そうです」:</strong> <code>いい</code> ➔ <code>よさそうです</code> ✅ (KHÔNG dùng <s>いいそう</s> ❌).<br>
                                3. <strong>Chủ ngữ mệnh đề phụ:</strong> Phải dùng <code>が</code> thay <code>は</code> (<code>母<strong>が</strong>作った料理</code> ✅).<br>
                                4. <strong>ナA / N + と思います / 言っていました:</strong> Phải thêm <code>だ</code> ở hiện tại khẳng định (<code>元気<strong>だ</strong>と思います</code> ✅).<br>
                                5. <strong>Trước 「まえに」 dù câu quá khứ:</strong> Vẫn chia <code>Vる</code> (<code>日本に 行く まえに、勉強しました</code> ✅).<br>
                                6. <strong>Khoảng thời gian + まえに:</strong> Không thêm <code>の</code> (<code>3年前に</code> / <code>10分前に</code> ✅; danh từ sự kiện mới thêm <code>の</code>).
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div> <!-- end .container -->

    <!-- Toast Notification -->
    <div id="toast"></div>

    <!-- Scripts -->
    <script>
        // DỮ LIỆU TỪ BACKEND PYTHON
        const VOCAB_DATA = __VOCAB_JSON__;
        const KANJI_DATA = __KANJI_JSON__;
        const EXAMS_LIST = __EXAMS_JSON__;
        const KANJI_15_18_DATA = __KANJI_15_18_JSON__;
        const KANJI_11_14_DATA = __KANJI_11_14_JSON__;
        const SENTENCE_TYPING_DATA = __SENTENCES_JSON__;
        const MINI15_18_CP_KEY = 'marugoto_mini15_18_cp_v2';
        window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;

        // TRẠNG THÁI TOÀN CỤC
        let currentTab = 'tab-theory';
        let currentVocabFilter = 'all';
        let isMeaningHidden = false;

        // Quản lý 5 Mã Đề & Trạng thái riêng từng Mã Đề
        let currentExamId = EXAMS_LIST[0].id;
        const examStates = {};

        let P1_DATA = EXAMS_LIST[0].p1;
        let P2_DATA = EXAMS_LIST[0].p2;
        let P3_DATA = EXAMS_LIST[0].p3;
        let P4_DATA = EXAMS_LIST[0].p4;
        let P5_DATA = EXAMS_LIST[0].p5;
        let P6_DATA = EXAMS_LIST[0].p6;
        let scoreState = { p1: {}, p2: {}, p3: {}, p4: {}, p5: {}, p6: {} };
        let arrangeState = {};
        let selectedA = null;
        let matchedPairs = {};

        function getExamById(examId) {
            return EXAMS_LIST.find(e => e.id === examId) || EXAMS_LIST[0];
        }

        function createEmptyExamState(exam) {
            return {
                scoreState: { p1: {}, p2: {}, p3: {}, p4: {}, p5: {}, p6: {} },
                p1Chosen: {},
                arrangeState: {},
                arrangeChecked: {},
                p3Answers: {},
                p4Order: exam.p4.slice().sort(() => Math.random() - 0.5),
                matchedPairs: {},
                p5Chosen: {},
                p6Draft: {},
                p6ModelOpen: {},
                p6StatusPts: {}
            };
        }

        function getActiveExamState() {
            const exam = getExamById(currentExamId);
            if (!examStates[currentExamId]) {
                examStates[currentExamId] = createEmptyExamState(exam);
            }
            return examStates[currentExamId];
        }

        function bindActiveExamAliases() {
            const exam = getExamById(currentExamId);
            const st = getActiveExamState();
            P1_DATA = exam.p1;
            P2_DATA = exam.p2;
            P3_DATA = exam.p3;
            P4_DATA = exam.p4;
            P5_DATA = exam.p5;
            P6_DATA = exam.p6;
            scoreState = st.scoreState;
            arrangeState = st.arrangeState;
            matchedPairs = st.matchedPairs;
            selectedA = null;
        }

        function computeExamScore(examId) {
            const st = examStates[examId];
            if (!st) return 0;
            let total = 0;
            ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'].forEach(p => {
                Object.values(st.scoreState[p]).forEach(val => {
                    total += Number(val) || 0;
                });
            });
            return Math.round(total * 10) / 10;
        }

        function hasExamProgress(examId) {
            const st = examStates[examId];
            if (!st) return false;
            return (
                Object.keys(st.p1Chosen).length > 0 ||
                Object.keys(st.arrangeChecked).length > 0 ||
                Object.keys(st.p3Answers).some(k => st.p3Answers[k] && st.p3Answers[k].locked) ||
                Object.keys(st.matchedPairs).length > 0 ||
                Object.keys(st.p5Chosen).length > 0 ||
                Object.keys(st.p6StatusPts).length > 0
            );
        }

        function saveCurrentExamDrafts() {
            const st = examStates[currentExamId];
            if (!st) return;
            P3_DATA.forEach(item => {
                const inp = document.getElementById(`p3_input_${item.id}`);
                if (inp) {
                    const prev = st.p3Answers[item.id] || { value: '', locked: false, isCorrect: false };
                    st.p3Answers[item.id] = { ...prev, value: inp.value };
                }
            });
            P6_DATA.forEach(item => {
                const txt = document.getElementById(`p6_txt_${item.id}`);
                if (txt) st.p6Draft[item.id] = txt.value;
            });
        }

        function updateExamHeaderBanner() {
            const exam = getExamById(currentExamId);
            const titleEl = document.getElementById('examTimerHeaderTitle');
            const metaEl = document.getElementById('examTimerHeaderMeta');
            const subEl = document.getElementById('activeExamSubtitle');
            if (titleEl) titleEl.innerText = exam.fullTitle;
            if (metaEl) metaEl.innerText = `${exam.badge} • 6 Dạng Bài Chuẩn Sư Phạm • 32 Câu Hỏi`;
            if (subEl) subEl.innerText = exam.subtitle;
        }

        function renderExamSwitcher() {
            const grid = document.getElementById('examSwitcherGrid');
            if (grid) {
                grid.innerHTML = EXAMS_LIST.map(ex => {
                    const sc = computeExamScore(ex.id);
                    const touched = hasExamProgress(ex.id);
                    const activeCls = ex.id === currentExamId ? ' active' : '';
                    const scoreCls = (touched || sc > 0) ? ' has-score' : '';
                    const scoreText = (touched || sc > 0) ? `${sc}/100đ` : 'Mới';
                    return `
                        <button type="button" class="exam-switch-btn${activeCls}" id="examSwitch_${ex.id}" onclick="switchExamSet('${ex.id}')">
                            <div class="exam-switch-top">
                                <span class="exam-switch-code">Mã Đề ${ex.code}</span>
                                <span class="exam-switch-score${scoreCls}">${scoreText}</span>
                            </div>
                            <span class="exam-switch-name">${ex.shortTitle}</span>
                        </button>
                    `;
                }).join('');
            }
            const summaryEl = document.getElementById('overallProgressSummary');
            if (summaryEl) {
                const startedCount = EXAMS_LIST.filter(ex => hasExamProgress(ex.id)).length;
                summaryEl.innerText = `Đang mở: Đề ${currentExamId} • Đã làm: ${startedCount} / ${EXAMS_LIST.length} mã đề`;
            }
        }

        function switchExamSet(examId) {
            if (examId === currentExamId) return;
            saveCurrentExamDrafts();
            currentExamId = examId;
            bindActiveExamAliases();
            updateExamHeaderBanner();
            renderPart1();
            renderPart2();
            renderPart3();
            renderPart4();
            renderPart5();
            renderPart6();
            updateTotalScore();
            renderExamSwitcher();
            saveMini15_18Checkpoint();
            showToast(`Đã chuyển sang Mã Đề ${examId} (${getExamById(examId).shortTitle})!`);
        }

        // Chuyển tab chính
        function switchMainTab(tabId, skipSave) {
            currentTab = tabId;
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            const activeBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => (b.getAttribute('onclick') || '').includes(tabId));
            if (activeBtn) activeBtn.classList.add('active');

            const targetPanel = document.getElementById(tabId);
            if (targetPanel) targetPanel.classList.add('active');

            if (tabId === 'tab-typing') {
                initTypingPractice();
            }
            if (!skipSave) {
                const curHash = (window.location.hash || '').toLowerCase();
                if (tabId !== 'tab-typing' && (curHash === '#typing' || curHash === '#tab-typing') && window.history && window.history.replaceState) {
                    window.history.replaceState(null, '', window.location.pathname + window.location.search);
                }
                saveMini15_18Checkpoint();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        // Phát âm TTS
        function speakText(text) {
            if (window.AudioEngine && typeof window.AudioEngine.speak === 'function') {
                window.AudioEngine.speak(text);
            } else if ('speechSynthesis' in window) {
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'ja-JP';
                u.rate = 0.95;
                window.speechSynthesis.speak(u);
            }
        }

        // Toast
        function showToast(msg) {
            const t = document.getElementById('toast');
            if (!t) return;
            t.innerText = msg;
            t.classList.add('show');
            setTimeout(() => {
                t.classList.remove('show');
            }, 2200);
        }

        // ==========================================
        // RENDER TỪ VỰNG
        // ==========================================
        function renderVocab(list) {
            const c = document.getElementById('vocabGridContainer');
            if (!c) return;
            c.innerHTML = list.map(item => `
                <div class="vocab-card">
                    <div>
                        <div class="vocab-card-header">
                            <div>
                                <div class="vocab-jp jp-text">${item.jp}</div>
                                <div class="vocab-kana jp-text">${item.kana || ''} ${item.hv ? `<span style="color:#64748b; font-size:0.8rem;">${item.hv}</span>` : ''}</div>
                            </div>
                            <button type="button" class="audio-btn" onclick="speakText('${item.jp}')" title="Phát âm">🔊</button>
                        </div>
                        <div class="vocab-badge">${item.l || 'A2'} • #${item.num || ''}</div>
                    </div>
                    <div class="vocab-vi ${isMeaningHidden ? 'hidden-meaning' : ''}">${item.vi}</div>
                </div>
            `).join('');
        }

        function filterVocab(lesson) {
            currentVocabFilter = lesson;
            document.querySelectorAll('#vocabFilterGroup .v-filter-btn').forEach(b => b.classList.remove('active'));
            const activeBtn = Array.from(document.querySelectorAll('#vocabFilterGroup .v-filter-btn')).find(b => b.getAttribute('onclick').includes(lesson));
            if (activeBtn) activeBtn.classList.add('active');

            const filtered = lesson === 'all' ? VOCAB_DATA : VOCAB_DATA.filter(w => w.l === lesson);
            renderVocab(filtered);
        }

        function handleVocabSearch() {
            const q = (document.getElementById('vocabSearchInput').value || '').toLowerCase().trim();
            let base = currentVocabFilter === 'all' ? VOCAB_DATA : VOCAB_DATA.filter(w => w.l === currentVocabFilter);
            if (q) {
                base = base.filter(w => 
                    (w.jp && w.jp.toLowerCase().includes(q)) ||
                    (w.kana && w.kana.toLowerCase().includes(q)) ||
                    (w.vi && w.vi.toLowerCase().includes(q)) ||
                    (w.romaji && w.romaji.toLowerCase().includes(q))
                );
            }
            renderVocab(base);
        }

        function toggleHideMeaning() {
            isMeaningHidden = !isMeaningHidden;
            document.querySelectorAll('.vocab-vi').forEach(el => {
                if (isMeaningHidden) el.classList.add('hidden-meaning');
                else el.classList.remove('hidden-meaning');
            });
            showToast(isMeaningHidden ? 'Đã ẩn nghĩa tiếng Việt (rê chuột để xem)' : 'Đã hiện nghĩa tiếng Việt');
        }

        function copyVocabQuizletFormat() {
            let targetList = currentVocabFilter === 'all' ? VOCAB_DATA : VOCAB_DATA.filter(w => w.l === currentVocabFilter);
            const lines = targetList.map(w => `${w.jp}\\t${w.vi} (${w.kana || ''})`).join('\\n');
            navigator.clipboard.writeText(lines).then(() => {
                showToast(`Đã copy ${targetList.length} từ vựng theo chuẩn Quizlet Tab!`);
            }).catch(() => {
                showToast('Không thể sao chép, vui lòng thử lại');
            });
        }

        // ==========================================
        // RENDER KANJI
        // ==========================================
        function renderKanji(list) {
            const c = document.getElementById('kanjiGridContainer');
            if (!c) return;
            c.innerHTML = list.map(k => `
                <div class="kanji-card">
                    <div class="kanji-main">
                        <div class="kanji-char jp-text">${k.char}</div>
                        <div class="kanji-info">
                            <div class="kanji-hv">${k.hv} <span style="font-size:0.8rem; color:#64748b;">(${k.strokes} nét)</span></div>
                            <div class="kanji-meaning">${k.meaning}</div>
                        </div>
                        <button type="button" class="audio-btn" onclick="speakText('${k.hiragana || k.char}')" title="Phát âm">🔊</button>
                    </div>
                    <div class="kanji-readings">
                        <div><strong>Âm Kun:</strong> <span class="jp-text" style="color:var(--primary); font-weight:700;">${k.kun || '—'}</span></div>
                        <div><strong>Âm On:</strong> <span class="jp-text" style="color:#d97706; font-weight:700;">${k.on || '—'}</span></div>
                    </div>
                    ${k.mnemonic ? `<div class="kanji-mnemonic">💡 <strong>Mẹo nhớ:</strong> ${k.mnemonic}</div>` : ''}
                </div>
            `).join('');
        }

        function copyKanjiQuizletTabFormat() {
            const lines = KANJI_DATA.map(k => `${k.char}\\t${k.hv} - ${k.meaning} [${k.hiragana || ''}]`).join('\\n');
            navigator.clipboard.writeText(lines).then(() => {
                showToast(`Đã copy ${KANJI_DATA.length} chữ Hán theo chuẩn Quizlet Tab!`);
            }).catch(() => {
                showToast('Không thể sao chép, vui lòng thử lại');
            });
        }

        // ==========================================
        // RENDER ĐỀ THI (PARTS 1 -> 6)
        // ==========================================
        function renderPart1() {
            const c = document.getElementById('part1Container');
            if (!c) return;
            const st = getActiveExamState();
            c.innerHTML = P1_DATA.map(item => {
                const chosenIdx = st.p1Chosen[item.id];
                const answered = chosenIdx !== undefined;
                return `
                    <div class="question-item" id="p1_item_${item.id}">
                        <div class="q-title">
                            <span class="q-badge">Câu ${item.id}</span>
                            <span class="jp-text" style="font-size:1.1rem;">${item.q}</span>
                        </div>
                        <div class="options-list">
                            ${item.options.map((opt, oIdx) => {
                                let cls = 'opt-btn jp-text';
                                if (answered) {
                                    if (oIdx === item.correct) cls += ' is-correct';
                                    else if (oIdx === chosenIdx) cls += ' is-wrong';
                                }
                                return `
                                    <button type="button" class="${cls}" id="p1_opt_${item.id}_${oIdx}" onclick="selectPart1Answer(${item.id}, ${oIdx})" ${answered ? 'disabled' : ''}>
                                        ${['A', 'B', 'C', 'D'][oIdx]}. ${opt}
                                    </button>
                                `;
                            }).join('')}
                        </div>
                        <div class="explain-box" id="p1_exp_${item.id}" style="display:${answered ? 'block' : 'none'};">
                            <strong>💡 Giải thích:</strong> ${item.explain}
                        </div>
                    </div>
                `;
            }).join('');
        }

        function selectPart1Answer(qId, oIdx) {
            const item = P1_DATA.find(q => q.id === qId);
            if (!item) return;
            const st = getActiveExamState();
            st.p1Chosen[qId] = oIdx;

            item.options.forEach((_, idx) => {
                const btn = document.getElementById(`p1_opt_${qId}_${idx}`);
                if (btn) {
                    btn.classList.remove('is-correct', 'is-wrong');
                    btn.disabled = true;
                }
            });

            const chosenBtn = document.getElementById(`p1_opt_${qId}_${oIdx}`);
            const correctBtn = document.getElementById(`p1_opt_${qId}_${item.correct}`);

            if (oIdx === item.correct) {
                if (chosenBtn) chosenBtn.classList.add('is-correct');
                scoreState.p1[qId] = 2.5;
            } else {
                if (chosenBtn) chosenBtn.classList.add('is-wrong');
                if (correctBtn) correctBtn.classList.add('is-correct');
                scoreState.p1[qId] = 0;
            }

            const exp = document.getElementById(`p1_exp_${qId}`);
            if (exp) exp.style.display = 'block';

            updateTotalScore();
        }

        // PART 2: ARRANGE
        function renderPart2() {
            const c = document.getElementById('part2Container');
            if (!c) return;
            const st = getActiveExamState();
            c.innerHTML = P2_DATA.map(item => {
                if (!st.arrangeState[item.id]) {
                    st.arrangeState[item.id] = {
                        placed: [],
                        available: item.chips.map((chip, idx) => ({ text: chip, origIdx: idx }))
                    };
                }
                const qSt = st.arrangeState[item.id];
                const chk = st.arrangeChecked[item.id];
                const statusHtml = chk
                    ? (chk.ok
                        ? '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>'
                        : '<span style="color:var(--accent);">✗ Chưa chính xác (0 điểm)</span>')
                    : '';
                return `
                    <div class="question-item" id="p2_item_${item.id}">
                        <div class="q-title">
                            <span class="q-badge">Câu ${item.id}</span>
                            <span>${item.prompt}</span>
                        </div>
                        <div style="font-size:1.1rem; font-weight:700; margin: 8px 0; color:var(--gray-900);">
                            <span class="jp-text">${item.pre}</span>
                            <span style="color:var(--primary); font-weight:800;"> [ 1 ] [ 2 ] [ ★ ] [ 4 ] </span>
                            <span class="jp-text">${item.post}</span>
                        </div>
                        <div class="arrange-slot-box" id="p2_slot_${item.id}">
                            ${qSt.placed.length === 0
                                ? '<span style="color:var(--gray-400); font-size:0.9rem;">(Click các mảnh ghép bên dưới để sắp xếp vào đây)</span>'
                                : qSt.placed.map((ch, pos) => `
                                    <button type="button" class="chip-btn in-slot jp-text" onclick="removeArrangeChip(${item.id}, ${ch.origIdx})" title="Click để gỡ ra">
                                        ${pos === 2 ? '★ ' : ''}${ch.text}
                                    </button>
                                `).join('')}
                        </div>
                        <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:12px;" id="p2_pool_${item.id}">
                            ${qSt.available.map(ch => `
                                <button type="button" class="chip-btn jp-text" id="p2_chip_${item.id}_${ch.origIdx}" onclick="clickArrangeChip(${item.id}, ${ch.origIdx})">${ch.text}</button>
                            `).join('')}
                        </div>
                        <div style="display:flex; gap:10px; align-items:center;">
                            <button type="button" class="btn-primary" onclick="checkArrangeAnswer(${item.id})" style="padding:6px 14px; font-size:0.88rem;">Kiểm Tra</button>
                            <button type="button" class="btn-primary" onclick="resetSingleArrange(${item.id})" style="padding:6px 14px; font-size:0.88rem; background:var(--gray-600);">Đặt Lại</button>
                            <span id="p2_status_${item.id}" style="font-weight:700; font-size:0.92rem;">${statusHtml}</span>
                        </div>
                        <div class="explain-box" id="p2_exp_${item.id}" style="display:${chk ? 'block' : 'none'};">
                            <strong>💡 Câu hoàn chỉnh:</strong> <span class="jp-text">${item.fullSentence}</span><br>
                            <strong>Giải thích:</strong> ${item.explain}
                        </div>
                    </div>
                `;
            }).join('');
        }

        function clickArrangeChip(qId, origIdx) {
            const st = arrangeState[qId];
            if (!st) return;
            const chipData = st.available.find(c => c.origIdx === origIdx);
            if (!chipData) return;

            st.available = st.available.filter(c => c.origIdx !== origIdx);
            st.placed.push(chipData);
            updateArrangeUI(qId);
            saveMini15_18Checkpoint();
        }

        function removeArrangeChip(qId, origIdx) {
            const st = arrangeState[qId];
            if (!st) return;
            const chipData = st.placed.find(c => c.origIdx === origIdx);
            if (!chipData) return;

            st.placed = st.placed.filter(c => c.origIdx !== origIdx);
            st.available.push(chipData);
            updateArrangeUI(qId);
            saveMini15_18Checkpoint();
        }

        function updateArrangeUI(qId) {
            const st = arrangeState[qId];
            const slotBox = document.getElementById(`p2_slot_${qId}`);
            const poolBox = document.getElementById(`p2_pool_${qId}`);

            if (st.placed.length === 0) {
                slotBox.innerHTML = '<span style="color:var(--gray-400); font-size:0.9rem;">(Click các mảnh ghép bên dưới để sắp xếp vào đây)</span>';
            } else {
                slotBox.innerHTML = st.placed.map((c, pos) => `
                    <button type="button" class="chip-btn in-slot jp-text" onclick="removeArrangeChip(${qId}, ${c.origIdx})" title="Click để gỡ ra">
                        ${pos === 2 ? '★ ' : ''}${c.text}
                    </button>
                `).join('');
            }

            poolBox.innerHTML = st.available.map(c => `
                <button type="button" class="chip-btn jp-text" id="p2_chip_${qId}_${c.origIdx}" onclick="clickArrangeChip(${qId}, ${c.origIdx})">${c.text}</button>
            `).join('');
        }

        function resetSingleArrange(qId) {
            const item = P2_DATA.find(q => q.id === qId);
            if (!item) return;
            const exSt = getActiveExamState();
            arrangeState[qId] = {
                placed: [],
                available: item.chips.map((chip, idx) => ({ text: chip, origIdx: idx }))
            };
            delete exSt.arrangeChecked[qId];
            delete scoreState.p2[qId];
            updateArrangeUI(qId);
            document.getElementById(`p2_status_${qId}`).innerText = '';
            document.getElementById(`p2_exp_${qId}`).style.display = 'none';
            updateTotalScore();
        }

        function checkArrangeAnswer(qId) {
            const item = P2_DATA.find(q => q.id === qId);
            const st = arrangeState[qId];
            const exSt = getActiveExamState();
            const statusEl = document.getElementById(`p2_status_${qId}`);
            const expEl = document.getElementById(`p2_exp_${qId}`);

            if (st.placed.length < 4) {
                statusEl.innerHTML = '<span style="color:var(--warning);">⚠️ Vui lòng xếp đủ cả 4 mảnh ghép!</span>';
                return;
            }

            const isStarCorrect = (st.placed[item.starIndex] && st.placed[item.starIndex].origIdx === item.correctOrder[item.starIndex]);
            const isFullCorrect = st.placed.every((c, idx) => c.origIdx === item.correctOrder[idx]);

            if (isFullCorrect || isStarCorrect) {
                statusEl.innerHTML = '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>';
                scoreState.p2[qId] = 3.0;
                exSt.arrangeChecked[qId] = { ok: true };
            } else {
                statusEl.innerHTML = '<span style="color:var(--accent);">✗ Chưa chính xác (0 điểm)</span>';
                scoreState.p2[qId] = 0;
                exSt.arrangeChecked[qId] = { ok: false };
            }

            expEl.style.display = 'block';
            updateTotalScore();
        }

        // PART 3: CONJUGATION
        function renderPart3() {
            const c = document.getElementById('part3Container');
            if (!c) return;
            const st = getActiveExamState();
            c.innerHTML = P3_DATA.map(item => {
                const ans = st.p3Answers[item.id] || { value: '', locked: false, isCorrect: false };
                const inputCls = ans.locked
                    ? `conjugate-input jp-text ${ans.isCorrect ? 'is-correct' : 'is-wrong'}`
                    : 'conjugate-input jp-text';
                const statusHtml = ans.locked
                    ? (ans.isCorrect
                        ? '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>'
                        : '<span style="color:var(--accent);">✗ Chưa đúng!</span>')
                    : '';
                return `
                    <div class="question-item" id="p3_item_${item.id}">
                        <div class="q-title">
                            <span class="q-badge">Câu ${item.id}</span>
                            <span class="jp-text" style="font-size:1.05rem;">${item.sentence}</span>
                        </div>
                        <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin:12px 0;">
                            <input type="text" class="${inputCls}" id="p3_input_${item.id}" placeholder="Nhập đáp án..." ${ans.locked ? 'disabled' : ''}>
                            <button type="button" class="btn-primary" onclick="checkConjugateAnswer(${item.id})" style="padding:7px 16px; font-size:0.9rem;">Kiểm Tra</button>
                            <span id="p3_status_${item.id}" style="font-weight:700; font-size:0.92rem;">${statusHtml}</span>
                        </div>
                        <div class="explain-box" id="p3_exp_${item.id}" style="display:${ans.locked ? 'block' : 'none'};">
                            <strong>💡 Đáp án đúng:</strong> <span class="jp-text" style="color:var(--success); font-weight:800;">${item.displayAnswer}</span><br>
                            <strong>Giải thích:</strong> ${item.explain}
                        </div>
                    </div>
                `;
            }).join('');
            P3_DATA.forEach(item => {
                const inp = document.getElementById(`p3_input_${item.id}`);
                const ans = st.p3Answers[item.id];
                if (inp && ans && ans.value) inp.value = ans.value;
            });
        }

        function checkConjugateAnswer(qId) {
            const item = P3_DATA.find(q => q.id === qId);
            const st = getActiveExamState();
            const input = document.getElementById(`p3_input_${qId}`);
            const statusEl = document.getElementById(`p3_status_${qId}`);
            const expEl = document.getElementById(`p3_exp_${qId}`);
            const val = (input.value || '').trim().toLowerCase();

            if (!val) {
                statusEl.innerHTML = '<span style="color:var(--warning);">Vui lòng nhập đáp án!</span>';
                return;
            }

            const isOk = item.accepted.some(acc => acc.toLowerCase() === val);
            input.disabled = true;
            st.p3Answers[qId] = { value: input.value.trim(), locked: true, isCorrect: isOk };

            if (isOk) {
                input.classList.add('is-correct');
                statusEl.innerHTML = '<span style="color:var(--success);">✓ Chính xác! (+3.0 điểm)</span>';
                scoreState.p3[qId] = 3.0;
            } else {
                input.classList.add('is-wrong');
                statusEl.innerHTML = '<span style="color:var(--accent);">✗ Chưa đúng!</span>';
                scoreState.p3[qId] = 0;
            }

            expEl.style.display = 'block';
            updateTotalScore();
        }

        // PART 4: MATCHING
        function renderPart4() {
            const c = document.getElementById('part4Container');
            if (!c) return;
            const st = getActiveExamState();
            const matchedBSet = new Set(Object.values(matchedPairs));
            const allMatched = Object.keys(matchedPairs).length === P4_DATA.length;
            c.innerHTML = `
                <div class="question-item">
                    <div style="font-size:0.95rem; color:var(--gray-600); margin-bottom:14px;">
                        👉 <em>Click chọn một câu ở Cột A (Tình huống), sau đó click chọn câu đối đáp tương ứng ở Cột B.</em>
                    </div>
                    <div class="matching-grid">
                        <div id="colAContainer">
                            ${P4_DATA.map(item => `
                                <div class="match-card jp-text${matchedPairs[item.id] ? ' matched' : ''}" id="match_A_${item.id}" onclick="clickMatchA(${item.id})">
                                    <strong>A${item.id - 20}:</strong> ${item.promptA}
                                </div>
                            `).join('')}
                        </div>
                        <div id="colBContainer">
                            ${st.p4Order.map(item => `
                                <div class="match-card jp-text${matchedBSet.has(item.correctBId) ? ' matched' : ''}" id="match_B_${item.correctBId}" onclick="clickMatchB('${item.correctBId}')">
                                    <strong>${item.correctBId}:</strong> ${item.promptB}
                                </div>
                            `).join('')}
                        </div>
                    </div>
                    <div style="display:flex; gap:12px; align-items:center;">
                        <button type="button" class="btn-primary" onclick="resetMatching()" style="background:var(--gray-600); padding:6px 14px; font-size:0.88rem;">Đặt Lại Cột Nối</button>
                        <span id="matchScoreText" style="font-weight:700;">${allMatched ? '<span style="color:var(--success);">🎉 Đã nối chuẩn xác toàn bộ 4 cặp câu! (+10 Điểm)</span>' : ''}</span>
                    </div>
                    <div class="explain-box" id="p4_exp_all" style="display:${allMatched ? 'block' : 'none'};">
                        <strong>💡 Phân tích các cặp hội thoại chuẩn:</strong><br>
                        ${P4_DATA.map(p => `• <strong>${p.correctBId}</strong>: ${p.explain}`).join('<br>')}
                    </div>
                </div>
            `;
        }

        function clickMatchA(id) {
            if (matchedPairs[id]) return;
            document.querySelectorAll('#colAContainer .match-card').forEach(el => el.classList.remove('selected'));
            selectedA = id;
            const el = document.getElementById(`match_A_${id}`);
            if (el) el.classList.add('selected');
        }

        function clickMatchB(bId) {
            if (!selectedA) {
                showToast('Vui lòng chọn 1 câu ở Cột A trước!');
                return;
            }
            const item = P4_DATA.find(q => q.id === selectedA);
            if (!item) return;

            const elA = document.getElementById(`match_A_${selectedA}`);
            const elB = document.getElementById(`match_B_${bId}`);

            if (item.correctBId === bId) {
                elA.classList.remove('selected');
                elA.classList.add('matched');
                elB.classList.add('matched');
                matchedPairs[selectedA] = bId;
                scoreState.p4[selectedA] = 2.5;
                showToast('✓ Nối thành công cặp câu!');
            } else {
                elA.classList.remove('selected');
                showToast('✗ Chưa đúng cặp hội thoại, hãy thử lại!');
            }
            selectedA = null;

            if (Object.keys(matchedPairs).length === P4_DATA.length) {
                document.getElementById('p4_exp_all').style.display = 'block';
                document.getElementById('matchScoreText').innerHTML = '<span style="color:var(--success);">🎉 Đã nối chuẩn xác toàn bộ 4 cặp câu! (+10 Điểm)</span>';
            }
            updateTotalScore();
        }

        function resetMatching() {
            const st = getActiveExamState();
            selectedA = null;
            st.matchedPairs = {};
            matchedPairs = st.matchedPairs;
            P4_DATA.forEach(q => {
                scoreState.p4[q.id] = 0;
            });
            renderPart4();
            updateTotalScore();
        }

        // PART 5: READING
        function renderPart5() {
            const c = document.getElementById('part5Container');
            if (!c) return;
            const st = getActiveExamState();
            c.innerHTML = P5_DATA.map(passage => `
                <div class="question-item">
                    <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary); margin-bottom:12px;">${passage.title}</h3>
                    <div class="reading-box jp-text">${passage.text}</div>
                    <div>
                        ${passage.questions.map(q => {
                            const chosenIdx = st.p5Chosen[q.id];
                            const answered = chosenIdx !== undefined;
                            return `
                                <div style="margin-bottom:18px; padding-bottom:14px; border-bottom:1px dashed var(--gray-200);">
                                    <div class="q-title">
                                        <span class="q-badge">Câu ${q.id}</span>
                                        <span class="jp-text">${q.q}</span>
                                    </div>
                                    <div class="options-list">
                                        ${q.options.map((opt, oIdx) => {
                                            let cls = 'opt-btn jp-text';
                                            if (answered) {
                                                if (oIdx === q.correct) cls += ' is-correct';
                                                else if (oIdx === chosenIdx) cls += ' is-wrong';
                                            }
                                            return `
                                                <button type="button" class="${cls}" id="p5_opt_${q.id}_${oIdx}" onclick="selectPart5Answer(${q.id}, ${oIdx}, ${passage.passageId})" ${answered ? 'disabled' : ''}>
                                                    ${['A', 'B', 'C', 'D'][oIdx]}. ${opt}
                                                </button>
                                            `;
                                        }).join('')}
                                    </div>
                                    <div class="explain-box" id="p5_exp_${q.id}" style="display:${answered ? 'block' : 'none'};">
                                        <strong>💡 Giải thích:</strong> ${q.explain}
                                    </div>
                                </div>
                            `;
                        }).join('')}
                    </div>
                </div>
            `).join('');
        }

        function selectPart5Answer(qId, oIdx, pId) {
            const passage = P5_DATA.find(p => p.passageId === pId);
            if (!passage) return;
            const item = passage.questions.find(q => q.id === qId);
            if (!item) return;
            const st = getActiveExamState();
            st.p5Chosen[qId] = oIdx;

            item.options.forEach((_, idx) => {
                const btn = document.getElementById(`p5_opt_${qId}_${idx}`);
                if (btn) {
                    btn.classList.remove('is-correct', 'is-wrong');
                    btn.disabled = true;
                }
            });

            const chosenBtn = document.getElementById(`p5_opt_${qId}_${oIdx}`);
            const correctBtn = document.getElementById(`p5_opt_${qId}_${item.correct}`);

            if (oIdx === item.correct) {
                if (chosenBtn) chosenBtn.classList.add('is-correct');
                scoreState.p5[qId] = 5.0;
            } else {
                if (chosenBtn) chosenBtn.classList.add('is-wrong');
                if (correctBtn) correctBtn.classList.add('is-correct');
                scoreState.p5[qId] = 0;
            }

            const exp = document.getElementById(`p5_exp_${qId}`);
            if (exp) exp.style.display = 'block';

            updateTotalScore();
        }

        // PART 6: TRANSLATION
        function renderPart6() {
            const c = document.getElementById('part6Container');
            if (!c) return;
            const st = getActiveExamState();
            c.innerHTML = P6_DATA.map(item => {
                const pts = st.p6StatusPts[item.id];
                const modelOpen = Boolean(st.p6ModelOpen[item.id]);
                const statusHtml = pts !== undefined
                    ? (pts > 0
                        ? `<span style="color:var(--success);">✓ Đã cộng ${pts} điểm</span>`
                        : `<span style="color:var(--accent);">✗ 0 điểm</span>`)
                    : '';
                return `
                    <div class="question-item" id="p6_item_${item.id}">
                        <div class="q-title">
                            <span class="q-badge">Câu ${item.id} • ${item.category}</span>
                            <span>${item.vi}</span>
                        </div>
                        <div style="font-size:0.88rem; color:#475569; margin-bottom:10px;">
                            💡 <strong>Từ khóa gợi ý:</strong> ${item.hint}
                        </div>
                        <textarea class="conjugate-input jp-text" id="p6_txt_${item.id}" rows="2" style="width:100%; font-size:1rem; margin-bottom:10px;" placeholder="Gõ câu dịch tiếng Nhật của bạn vào đây..."></textarea>
                        <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
                            <button type="button" class="btn-primary" onclick="toggleTranslationModel(${item.id})" style="padding:6px 14px; font-size:0.88rem;">👁️ Xem Đáp Án Mẫu</button>
                            <button type="button" class="btn-primary" onclick="selfGradeTranslation(${item.id}, 3.75)" style="background:var(--success); padding:6px 14px; font-size:0.88rem;">✓ Tự Chấm Đúng (+3.75đ)</button>
                            <button type="button" class="btn-primary" onclick="selfGradeTranslation(${item.id}, 0)" style="background:var(--gray-600); padding:6px 14px; font-size:0.88rem;">✗ Tự Chấm Sai (0đ)</button>
                            <span id="p6_status_${item.id}" style="font-weight:700;">${statusHtml}</span>
                        </div>
                        <div class="explain-box" id="p6_model_${item.id}" style="display:${modelOpen ? 'block' : 'none'};">
                            <div style="font-size:1.1rem; font-weight:800; color:var(--primary); margin-bottom:6px;" class="jp-text">
                                ${item.modelSentence}
                                <button type="button" class="audio-btn" onclick="speakP6Model(${item.id})" style="vertical-align:middle; margin-left:6px;">🔊</button>
                            </div>
                            <div style="color:var(--gray-600); font-size:0.9rem; margin-bottom:8px;">${item.modelKana}</div>
                            <strong>Phân tích ngữ pháp:</strong>
                            <ul style="margin-left:20px; font-size:0.92rem; color:var(--gray-700);">
                                ${item.breakdown.map(b => `<li><strong>${b.part}</strong>: ${b.role}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                `;
            }).join('');
            P6_DATA.forEach(item => {
                const txt = document.getElementById(`p6_txt_${item.id}`);
                if (txt && st.p6Draft[item.id]) txt.value = st.p6Draft[item.id];
            });
        }

        function speakP6Model(qId) {
            const item = P6_DATA.find(q => q.id === qId);
            if (item) speakText(item.modelSentence);
        }

        function toggleTranslationModel(qId) {
            const el = document.getElementById(`p6_model_${qId}`);
            const st = getActiveExamState();
            if (el) {
                const nextOpen = el.style.display !== 'block';
                el.style.display = nextOpen ? 'block' : 'none';
                st.p6ModelOpen[qId] = nextOpen;
                saveMini15_18Checkpoint();
            }
        }

        function selfGradeTranslation(qId, pts) {
            const st = getActiveExamState();
            scoreState.p6[qId] = pts;
            st.p6StatusPts[qId] = pts;
            st.p6ModelOpen[qId] = true;
            const statusEl = document.getElementById(`p6_status_${qId}`);
            if (pts > 0) {
                statusEl.innerHTML = `<span style="color:var(--success);">✓ Đã cộng ${pts} điểm</span>`;
            } else {
                statusEl.innerHTML = `<span style="color:var(--accent);">✗ 0 điểm</span>`;
            }
            document.getElementById(`p6_model_${qId}`).style.display = 'block';
            updateTotalScore();
        }

        // TOTAL SCORE
        function updateTotalScore() {
            const total = computeExamScore(currentExamId);
            const disp = document.getElementById('totalScoreText');
            if (disp) {
                disp.innerText = `${total} / 100 Điểm`;
            }
            renderExamSwitcher();
            if (typeof saveMini15_18Checkpoint === 'function') saveMini15_18Checkpoint();
        }

        function resetAllExam() {
            if (!confirm(`Bạn có chắc chắn muốn làm lại toàn bộ Mã Đề ${currentExamId} không?`)) return;
            examStates[currentExamId] = createEmptyExamState(getExamById(currentExamId));
            bindActiveExamAliases();
            renderPart1();
            renderPart2();
            renderPart3();
            renderPart4();
            renderPart5();
            renderPart6();
            updateTotalScore();
            saveMini15_18Checkpoint();
            showToast(`Đã đặt lại toàn bộ Mã Đề ${currentExamId}!`);
        }

        // ==========================================
        // TYPING STUDIO ENGINE (SENTENCE / KANJI / VOCAB) + CHECKPOINT
        // ==========================================
        let tpInitialized = false;
        let tpState = {
            mode: 'sentence', // 'sentence' | 'kanji' | 'vocab'
            filterByMode: { sentence: 'all', kanji: '15-18', vocab: 'all' },
            idxByBucket: {},
            orderByBucket: {},
            history: {}, // id -> { status: 'ok'|'err'|'reveal', lastInput, whyWrong, isKanjiMatch }
            drafts: {}, // id -> raw unsaved input text
            allowKanji: false,
            autoAdvance: false,
            showOverview: false,
            streak: 0,
            gradedCurrent: false
        };

        function escapeHtml(str) {
            return String(str || '')
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
        }

        function toHiragana(str) {
            if (!str) return '';
            let out = '';
            for (const ch of String(str)) {
                const code = ch.charCodeAt(0);
                if (code >= 0x30A1 && code <= 0x30F6) {
                    out += String.fromCharCode(code - 0x60);
                } else if (code >= 0xFF01 && code <= 0xFF5E) {
                    out += String.fromCharCode(code - 0xFEE0);
                } else {
                    out += ch;
                }
            }
            return out.toLowerCase();
        }

        function cleanJpCompare(s, convertKata) {
            if (!s) return '';
            const base = convertKata ? toHiragana(s) : String(s).toLowerCase();
            return base
                .trim()
                .replace(/[()（）「」『』""''…・~～/／、,。.,?!？！\\s\\-_\\t　]/g, '');
        }

        function containsKanji(s) {
            return /[\\u4E00-\\u9FAF\\u3400-\\u4DBF]/.test(s || '');
        }

        function stripDakutenChar(ch) {
            const map = {
                'が':'か','ぎ':'き','ぐ':'く','げ':'け','ご':'こ',
                'ざ':'さ','じ':'し','ず':'す','ぜ':'せ','ぞ':'そ',
                'だ':'た','ぢ':'ち','づ':'つ','で':'て','ど':'と',
                'ば':'は','び':'ひ','ぶ':'ふ','べ':'へ','ぼ':'ほ',
                'ぱ':'は','ぴ':'ひ','ぷ':'ふ','ぺ':'へ','ぽ':'ほ',
                'ゔ':'う'
            };
            return map[ch] || ch;
        }

        function stripDakutenStr(s) {
            return Array.from(s || '').map(stripDakutenChar).join('');
        }

        function collapseLongVowels(s) {
            return (s || '')
                .replace(/ー/g, '')
                .replace(/([おこそとのほもよろをごぞどぼぽうくすつぬふむゆるぐずづぶぷ])う/g, '$1')
                .replace(/([えけせてねへめれげぜでべぺい])い/g, '$1')
                .replace(/([あかさたなはまやらわがざだばぱ])あ/g, '$1');
        }

        function bigSmallKana(s) {
            return (s || '')
                .replace(/ゃ/g, 'や').replace(/ゅ/g, 'ゆ').replace(/ょ/g, 'よ')
                .replace(/っ/g, 'つ').replace(/ぁ/g, 'あ').replace(/ぃ/g, 'い')
                .replace(/ぅ/g, 'う').replace(/ぇ/g, 'え').replace(/ぉ/g, 'お');
        }

        function buildCharDiffHtml(typedRaw, targetRaw) {
            const a = Array.from(cleanJpCompare(typedRaw, true));
            const b = Array.from(cleanJpCompare(targetRaw, true));
            let typedHtml = '';
            let targetHtml = '';
            let prefix = 0;
            while (prefix < a.length && prefix < b.length && a[prefix] === b[prefix]) prefix++;
            let suffix = 0;
            while (
                suffix < (a.length - prefix) &&
                suffix < (b.length - prefix) &&
                a[a.length - 1 - suffix] === b[b.length - 1 - suffix]
            ) suffix++;

            for (let i = 0; i < prefix; i++) {
                typedHtml += `<span class="diff-good">${escapeHtml(a[i])}</span>`;
                targetHtml += `<span class="diff-good">${escapeHtml(b[i])}</span>`;
            }
            const midA = a.slice(prefix, a.length - suffix);
            const midB = b.slice(prefix, b.length - suffix);
            if (midA.length) typedHtml += `<span class="diff-bad">${escapeHtml(midA.join(''))}</span>`;
            if (midB.length) targetHtml += `<span class="diff-good" style="background:#fde68a;color:#92400e;">${escapeHtml(midB.join(''))}</span>`;
            for (let i = a.length - suffix; i < a.length; i++) {
                typedHtml += `<span class="diff-good">${escapeHtml(a[i])}</span>`;
            }
            for (let i = b.length - suffix; i < b.length; i++) {
                targetHtml += `<span class="diff-good">${escapeHtml(b[i])}</span>`;
            }
            return {
                typedHtml: typedHtml || '<em style="color:var(--gray-400);">(trống)</em>',
                targetHtml,
                expectedChunk: midB.join(''),
                gotChunk: midA.join('')
            };
        }

        function diagnoseTypingMistake(rawUser, item, mode) {
            const reasons = [];
            const normUserHira = cleanJpCompare(rawUser, true);
            const targetSample = mode === 'sentence' ? item.hira : (mode === 'kanji' ? item.kana : (item.kana || item.jp));
            const acceptedList = mode === 'sentence'
                ? (item.acceptedHira || [item.hira])
                : (mode === 'kanji' ? (item.accepted || [item.kana]) : [item.jp, item.kana, item.romaji].filter(Boolean));
            const normTarget = cleanJpCompare(targetSample, true);

            // 1. Item-specific targeted grammar / reading traps
            if (item.traps && Array.isArray(item.traps)) {
                for (const t of item.traps) {
                    if (t.regex) {
                        const re = new RegExp(t.regex, 'i');
                        if (re.test(normUserHira) || re.test(rawUser)) {
                            reasons.push(`🎯 <strong>Bẫy hay sai ở câu/từ này:</strong> ${t.why}`);
                        }
                    } else if (t.wrong && Array.isArray(t.wrong)) {
                        if (t.wrong.some(w => cleanJpCompare(w, true) === normUserHira)) {
                            reasons.push(`🎯 <strong>Lỗi nhầm cách đọc phổ biến:</strong> ${t.why}`);
                        }
                    }
                }
            }

            // 2. Typed Kanji check
            if (containsKanji(rawUser)) {
                if (mode === 'kanji') {
                    reasons.push('⛩️ <strong>Bạn vừa nhập lại mặt chữ Kanji!</strong> Chế độ này yêu cầu nhập <strong>cách đọc Hiragana</strong> (không giữ chữ Hán).');
                } else if (mode === 'sentence') {
                    const kanjiMatches = (item.kanjiAccepted || []).some(k => cleanJpCompare(k, true) === normUserHira);
                    if (kanjiMatches) {
                        reasons.push('⛩️ Câu bạn gõ khớp bản có chữ Hán nhưng chế độ hiện đang chấm <strong>thuần Hiragana</strong>. Hãy tắt chuyển chữ Kanji hoặc bật mục <em>"Cho phép kèm Kanji"</em> ở phía trên!');
                    } else {
                        reasons.push('⛩️ Trong bài gõ có dính ký tự <strong>Kanji</strong> — hãy chuyển IME sang thuần <strong>Hiragana</strong> rồi kiểm tra lại cách chia ngữ pháp bên dưới.');
                    }
                }
            }

            // 3. Forgot IME (ASCII letters typed in Hiragana modes)
            const asciiLettersOnly = (rawUser || '').replace(/fpt|youtube/ig, '');
            if (mode !== 'vocab' && /[a-zA-Z]{2,}/.test(asciiLettersOnly)) {
                reasons.push('⌨️ <strong>Có chữ cái Latinh (Romaji):</strong> Có vẻ bạn quên bật bộ gõ Hiragana tiếng Nhật (chế độ này yêu cầu nhập bằng Hiragana chứ không để Romaji thô).');
            }

            // 4. Phonological spelling diagnostics
            for (const acc of acceptedList) {
                const nt = cleanJpCompare(acc, true);
                if (!nt || !normUserHira) continue;
                if (normUserHira.replace(/っ/g, '') === nt.replace(/っ/g, '') && normUserHira !== nt) {
                    reasons.push('✂️ <strong>Thiếu hoặc thừa âm ngắt chữ 「っ」 nhỏ:</strong> Hãy kiểm tra lại các chữ có ngắt âm đôi (như <code>さっか, けっこん, いった, かった, とった, まって, きっさてん, しゅっぱつ</code>).');
                    break;
                }
                if (collapseLongVowels(normUserHira) === collapseLongVowels(nt) && normUserHira !== nt) {
                    reasons.push('🔊 <strong>Sai / thiếu trường âm (<code>う, い, ー</code>):</strong> Ví dụ <code>せんしゅう</code> (có う), <code>たんじょうび</code> (có う), <code>とけい / かいけい</code> (có い), hoặc <code>セーター</code> (có ー).');
                    break;
                }
                if (stripDakutenStr(normUserHira) === stripDakutenStr(nt) && normUserHira !== nt) {
                    reasons.push('゛ <strong>Nhầm âm đục / bán đục (tenten <code>゛</code> hoặc maru <code>゜</code>):</strong> Ví dụ <code>が/か, ぎ/き, ぐ/く, ざ/さ, じ/し, ぞ/そ, だ/た, で/て, ば/は, ぱ/は</code>.');
                    break;
                }
                if (bigSmallKana(normUserHira) === bigSmallKana(nt) && normUserHira !== nt) {
                    reasons.push('🔡 <strong>Nhầm chữ nhỏ với chữ thường:</strong> Cần dùng <code>ゃ, ゅ, ょ, っ</code> nhỏ chứ không phải <code>や, ゆ, よ, つ</code> lớn (ví dụ <code>しゃ / きょ / しゅ</code>).');
                    break;
                }
            }

            // 5. General comparison fallback & global PDF trap checks
            if (mode === 'sentence' && !reasons.length) {
                const isRelClause = (item.pattern || '').includes('＋ N') || (item.pattern || '').includes('＋ 人') || (item.category || '').includes('Bổ nghĩa');
                const relNoFix = normUserHira.replace(/([ただいるうくぐすつぬぶむ])の/g, '$1');
                if (isRelClause && relNoFix !== normUserHira && acceptedList.some(acc => cleanJpCompare(acc, true) === relNoFix)) {
                    reasons.push('🚫 <strong>BẪY PDF L16–17 (Thừa trợ từ 「の」 trong mệnh đề bổ nghĩa):</strong> Sau động từ thể thông thường đứng trước Danh từ, TUYỆT ĐỐI KHÔNG chen 「の」 (ví dụ <em>とった しゃしん ✅</em>, không dùng <s>とったのしゃしん</s> ❌)!');
                } else {
                    const diff = buildCharDiffHtml(rawUser, targetSample);
                    if (normUserHira.includes('わ') && normTarget.includes('は') && normUserHira.replace(/わ/g, 'は') === normTarget.replace(/わ/g, 'は')) {
                        reasons.push('📌 <strong>Nhầm trợ từ 「は」 thành 「わ」:</strong> Trợ từ chủ đề câu phát âm là <em>wa</em> nhưng viết bằng chữ <strong>「は」</strong>!');
                    } else if (diff.expectedChunk || diff.gotChunk) {
                        reasons.push(`🔎 <strong>Lệch tại cụm ký tự:</strong> Bạn gõ <code>${escapeHtml(diff.gotChunk || '(thiếu)')}</code> trong khi đáp án chuẩn cần <code>${escapeHtml(diff.expectedChunk || '(không có)')}</code>.`);
                    }
                }
            } else if (mode === 'kanji' && !reasons.length) {
                const diff = buildCharDiffHtml(rawUser, targetSample);
                reasons.push(`🔎 <strong>Đối chiếu mặt âm đọc:</strong> Bạn gõ <code>${escapeHtml(normUserHira)}</code>, phần khác biệt so với cách đọc chuẩn nằm ở <code>${escapeHtml(diff.expectedChunk || normTarget)}</code>.`);
            }

            if (!reasons.length) {
                reasons.push('💡 Hãy kiểm tra lại trợ từ (<code>は, が, を, に, で, と</code>), cách chia thể thông thường (<code>Vる / Vない / Vた / ている / だ</code>) và đối chiếu từng vế câu bên dưới.');
            }
            return reasons;
        }

        function getModeItems(mode) {
            if (mode === 'sentence') return SENTENCE_TYPING_DATA;
            if (mode === 'kanji') return [...KANJI_15_18_DATA, ...KANJI_11_14_DATA];
            return VOCAB_DATA.map((v, i) => ({
                id: 'v_' + i + '_' + (v.jp || ''),
                lesson: v.l || 'A2',
                vi: v.vi,
                jp: v.jp,
                kana: v.kana,
                romaji: v.romaji,
                kanji: v.kanji
            }));
        }

        function getFilterDefs(mode) {
            const wrongIds = new Set(Object.keys(tpState.history).filter(id => tpState.history[id] && tpState.history[id].status === 'err'));
            const items = getModeItems(mode);
            if (mode === 'sentence') {
                return [
                    { key: 'all', label: `Tất cả L11-18 (${items.length})` },
                    { key: 'focus-15-18', label: `Trọng tâm L15-18 (${items.filter(x => !/^A2-1[1-4]$/.test(x.lesson)).length})` },
                    { key: 'A2-15', label: `Bài 15 (${items.filter(x => x.lesson === 'A2-15').length})` },
                    { key: 'A2-16', label: `Bài 16 (${items.filter(x => x.lesson === 'A2-16').length})` },
                    { key: 'Kaiwa Mid 2', label: `Kaiwa Mid 2 (${items.filter(x => x.lesson === 'Kaiwa Mid 2').length})` },
                    { key: 'A2-17', label: `Bài 17 (${items.filter(x => x.lesson === 'A2-17').length})` },
                    { key: 'A2-18', label: `Bài 18 (${items.filter(x => x.lesson === 'A2-18').length})` },
                    { key: 'review-11-14', label: `Ôn thêm L11-14 (${items.filter(x => /^A2-1[1-4]$/.test(x.lesson)).length})` },
                    { key: 'wrong', label: `🔁 Câu sai (${items.filter(x => wrongIds.has(x.id)).length})` }
                ];
            }
            if (mode === 'kanji') {
                return [
                    { key: '15-18', label: `Kanji L15-18 (${KANJI_15_18_DATA.length})` },
                    { key: '11-14', label: `Kanji L11-14 (${KANJI_11_14_DATA.length})` },
                    { key: 'all', label: `Tất cả (${items.length})` },
                    { key: 'wrong', label: `🔁 Chữ hay sai (${items.filter(x => wrongIds.has(x.id)).length})` }
                ];
            }
            return [
                { key: 'all', label: `Tất cả (${items.length})` },
                { key: 'A2-15', label: 'Bài 15' },
                { key: 'A2-16', label: 'Bài 16' },
                { key: 'A2-17', label: 'Bài 17' },
                { key: 'A2-18', label: 'Bài 18' },
                { key: 'wrong', label: `🔁 Từ sai (${items.filter(x => wrongIds.has(x.id)).length})` }
            ];
        }

        function getActiveBucketKey() {
            const m = tpState.mode;
            const f = tpState.filterByMode[m] || (m === 'kanji' ? '15-18' : 'all');
            return `${m}::${f}`;
        }

        function getFilteredTypingPool() {
            const m = tpState.mode;
            const f = tpState.filterByMode[m] || (m === 'kanji' ? '15-18' : 'all');
            const all = getModeItems(m);
            let base;
            if (f === 'wrong') {
                base = all.filter(x => tpState.history[x.id] && tpState.history[x.id].status === 'err');
            } else if (f === 'all') {
                base = [...all];
            } else if (m === 'sentence' && f === 'focus-15-18') {
                base = all.filter(x => !/^A2-1[1-4]$/.test(x.lesson));
            } else if (m === 'sentence' && f === 'review-11-14') {
                base = all.filter(x => /^A2-1[1-4]$/.test(x.lesson));
            } else if (m === 'kanji') {
                base = all.filter(x => x.group === f);
            } else {
                base = all.filter(x => x.lesson === f);
            }
            const bucket = getActiveBucketKey();
            const savedOrder = tpState.orderByBucket[bucket];
            if (Array.isArray(savedOrder) && savedOrder.length > 0 && f !== 'wrong') {
                const mapById = new Map(base.map(it => [it.id, it]));
                const ordered = savedOrder.map(id => mapById.get(id)).filter(Boolean);
                const missing = base.filter(it => !savedOrder.includes(it.id));
                return [...ordered, ...missing];
            }
            return base;
        }

        function initTypingPractice() {
            tpInitialized = true;
            updateTypingModeButtons();
            renderTypingFilters();
            renderTypingControlsState();
            renderTypingCard(false);
        }

        function updateTypingModeButtons() {
            ['sentence', 'kanji', 'vocab'].forEach(m => {
                const btn = document.getElementById(`tpModeBtn_${m}`);
                if (btn) btn.classList.toggle('active', tpState.mode === m);
            });
            const kWrap = document.getElementById('tpKanjiAllowWrap');
            if (kWrap) kWrap.style.display = tpState.mode === 'sentence' ? 'inline-flex' : 'none';
        }

        function renderTypingControlsState() {
            const kTog = document.getElementById('tpAllowKanjiToggle');
            const aTog = document.getElementById('tpAutoAdvToggle');
            if (kTog) kTog.checked = Boolean(tpState.allowKanji);
            if (aTog) aTog.checked = Boolean(tpState.autoAdvance);
            const drawer = document.getElementById('tpOverviewDrawer');
            const oBtn = document.getElementById('tpOverviewBtn');
            if (drawer) drawer.classList.toggle('show', Boolean(tpState.showOverview));
            if (oBtn) oBtn.classList.toggle('active', Boolean(tpState.showOverview));
        }

        function renderTypingFilters() {
            const grp = document.getElementById('typingFilterGroup');
            if (!grp) return;
            const m = tpState.mode;
            const curF = tpState.filterByMode[m] || (m === 'kanji' ? '15-18' : 'all');
            const defs = getFilterDefs(m);
            grp.innerHTML = defs.map(d => `
                <button type="button" class="v-filter-btn ${d.key === curF ? 'active' : ''}" onclick="switchTypingLesson('${d.key}')">${d.label}</button>
            `).join('');
        }

        function switchTypingMode(mode) {
            tpState.mode = mode;
            tpState.gradedCurrent = false;
            updateTypingModeButtons();
            renderTypingFilters();
            renderTypingCard(true);
            saveMini15_18Checkpoint();
        }

        function switchTypingLesson(lessonKey) {
            tpState.filterByMode[tpState.mode] = lessonKey;
            tpState.gradedCurrent = false;
            renderTypingFilters();
            renderTypingCard(true);
            saveMini15_18Checkpoint();
        }

        function toggleTypingOption(optName, val) {
            if (optName === 'allowKanji') tpState.allowKanji = Boolean(val);
            if (optName === 'autoAdvance') tpState.autoAdvance = Boolean(val);
            saveMini15_18Checkpoint();
        }

        function toggleTypingOverview() {
            tpState.showOverview = !tpState.showOverview;
            renderTypingControlsState();
            renderTypingOverview();
            saveMini15_18Checkpoint();
        }

        function renderTypingOverview() {
            const drawer = document.getElementById('tpOverviewDrawer');
            if (!drawer || !tpState.showOverview) return;
            const pool = getFilteredTypingPool();
            const bucket = getActiveBucketKey();
            const curIdx = tpState.idxByBucket[bucket] || 0;
            if (!pool.length) {
                drawer.innerHTML = '<div style="grid-column:1/-1; color:var(--gray-500); font-size:0.9rem;">Chưa có mục nào trong bộ lọc này.</div>';
                return;
            }
            drawer.innerHTML = pool.map((it, idx) => {
                const hist = tpState.history[it.id];
                const stCls = hist ? (hist.status === 'ok' ? 'done-ok' : (hist.status === 'err' ? 'done-err' : '')) : '';
                const icon = hist ? (hist.status === 'ok' ? '✅' : (hist.status === 'err' ? '❌' : '👁️')) : `${idx + 1}.`;
                const title = tpState.mode === 'kanji' ? `${it.kanji} (${it.vi})` : (tpState.mode === 'sentence' ? it.vi : `${it.vi} (${it.jp})`);
                return `
                    <button type="button" class="tp-overview-item ${idx === curIdx ? 'active' : ''} ${stCls}" onclick="jumpToTypingItem(${idx})">
                        <span>${icon}</span>
                        <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${escapeHtml(title)}</span>
                    </button>
                `;
            }).join('');
        }

        function jumpToTypingItem(idx) {
            const bucket = getActiveBucketKey();
            tpState.idxByBucket[bucket] = idx;
            tpState.gradedCurrent = false;
            renderTypingCard(true);
            saveMini15_18Checkpoint();
        }

        function shuffleTypingPool() {
            const pool = getFilteredTypingPool();
            if (!pool.length) return;
            const shuffled = pool.map(x => x.id).sort(() => Math.random() - 0.5);
            const bucket = getActiveBucketKey();
            tpState.orderByBucket[bucket] = shuffled;
            tpState.idxByBucket[bucket] = 0;
            tpState.gradedCurrent = false;
            renderTypingCard(true);
            saveMini15_18Checkpoint();
            showToast('Đã xáo trộn thứ tự các thẻ!');
        }

        function renderTypingCard(shouldFocus) {
            const pool = getFilteredTypingPool();
            const bucket = getActiveBucketKey();
            let idx = tpState.idxByBucket[bucket] || 0;
            if (idx >= pool.length) idx = Math.max(0, pool.length - 1);
            if (idx < 0) idx = 0;
            tpState.idxByBucket[bucket] = idx;

            const badge = document.getElementById('tpCardBadge');
            const patBadge = document.getElementById('tpPatternBadge');
            const subEl = document.getElementById('tpPromptSubtitle');
            const promptEl = document.getElementById('tpPromptVi');
            const dirEl = document.getElementById('tpInputDirective');
            const hintPrev = document.getElementById('tpHintPreview');
            const inp = document.getElementById('tpCardInput');
            const checkBtn = document.getElementById('tpCardCheckBtn');
            const detailPanel = document.getElementById('tpDetailPanel');
            document.getElementById('tpStreakBadge').innerText = `🔥 Chuỗi: ${tpState.streak}`;

            if (!pool.length) {
                if (badge) badge.innerText = '0 / 0';
                if (patBadge) patBadge.innerText = 'Bộ lọc trống';
                if (subEl) subEl.innerText = 'TRẠNG THÁI';
                if (promptEl) {
                    promptEl.className = 'tp-vi-hero';
                    promptEl.innerText = '🎉 Tuyệt vời! Không có câu/chữ nào đang sai trong bộ lọc này.';
                }
                if (inp) {
                    inp.value = '';
                    inp.disabled = true;
                }
                if (detailPanel) { detailPanel.className = 'tp-detail-panel'; detailPanel.innerHTML = ''; }
                updateTypingStats(pool);
                renderTypingOverview();
                return;
            }

            const item = pool[idx];
            if (hintPrev) { hintPrev.style.display = 'none'; hintPrev.innerHTML = ''; }

            if (tpState.mode === 'sentence') {
                badge.innerText = `Câu ${idx + 1} / ${pool.length} • ${item.lesson}`;
                patBadge.innerText = item.category || item.pattern || 'Bài 15-18';
                subEl.innerText = 'ĐỀ BÀI TIẾNG VIỆT — DỊCH & GÕ HIRAGANA';
                promptEl.className = 'tp-vi-hero';
                promptEl.innerText = item.vi;
                dirEl.innerHTML = '⬇️ Nhập câu tiếng Nhật bằng <strong>Hiragana</strong> rồi nhấn <strong>Enter</strong>:';
                inp.placeholder = 'Ví dụ: ねる まえに、よく ほんを よみます。';
                inp.rows = 2;
            } else if (tpState.mode === 'kanji') {
                badge.innerText = `Chữ Hán ${idx + 1} / ${pool.length} • PDF Kanji ${item.group} (#${item.stt})`;
                patBadge.innerText = `Kanji Lesson ${item.group}`;
                subEl.innerText = 'NHÌN CHỮ HÁN (KANJI) — GÕ CÁCH ĐỌC HIRAGANA';
                promptEl.className = 'tp-kanji-hero jp-text';
                promptEl.innerText = item.kanji;
                dirEl.innerHTML = '⬇️ Nhập <strong>cách đọc Hiragana</strong> của chữ Hán trên rồi nhấn <strong>Enter</strong>:';
                inp.placeholder = 'Gõ cách đọc bằng Hiragana (ví dụ: らいねん)...';
                inp.rows = 1;
            } else {
                badge.innerText = `Từ ${idx + 1} / ${pool.length} • ${item.lesson}`;
                patBadge.innerText = 'Từ Vựng A2';
                subEl.innerText = 'Ý NGHĨA TIẾNG VIỆT — GÕ PHẢN XẠ';
                promptEl.className = 'tp-vi-hero';
                promptEl.innerText = item.vi;
                dirEl.innerHTML = '⬇️ Gõ <strong>Hiragana, Kanji hoặc Romaji</strong> rồi nhấn <strong>Enter</strong>:';
                inp.placeholder = 'Gõ Hiragana / Kanji / Romaji...';
                inp.rows = 1;
            }

            const hist = tpState.history[item.id];
            const draftVal = tpState.drafts[item.id];
            inp.disabled = false;
            inp.className = 'typing-input-large jp-text';

            if (hist && tpState.gradedCurrent) {
                inp.value = hist.lastInput || draftVal || '';
                if (hist.status === 'ok') inp.classList.add('correct');
                else if (hist.status === 'err') inp.classList.add('wrong');
                renderTypingDetailBox(item, hist);
                checkBtn.innerText = 'Câu Tiếp Theo ➔ (Enter)';
                checkBtn.style.background = 'var(--secondary)';
            } else if (hist && hist.status && (draftVal === undefined || draftVal === hist.lastInput)) {
                inp.value = hist.lastInput || '';
                if (hist.status === 'ok') inp.classList.add('correct');
                else if (hist.status === 'err') inp.classList.add('wrong');
                renderTypingDetailBox(item, hist);
                tpState.gradedCurrent = true;
                checkBtn.innerText = 'Câu Tiếp Theo ➔ (Enter)';
                checkBtn.style.background = 'var(--secondary)';
            } else {
                inp.value = draftVal || '';
                detailPanel.className = 'tp-detail-panel';
                detailPanel.innerHTML = '';
                tpState.gradedCurrent = false;
                checkBtn.innerText = 'Kiểm Tra Đáp Án ⏎';
                checkBtn.style.background = 'var(--primary)';
            }

            updateTypingStats(pool);
            renderTypingOverview();
            if (shouldFocus) inp.focus();
        }

        function renderTypingDetailBox(item, hist) {
            const detailPanel = document.getElementById('tpDetailPanel');
            if (!detailPanel) return;

            let headerHtml = '';
            let panelCls = 'tp-detail-panel show ';
            if (hist.status === 'ok') {
                panelCls += 'is-ok';
                headerHtml = `<div style="font-size:1.08rem; font-weight:800; color:#15803d; margin-bottom:10px;">
                    ✅ CHÍNH XÁC! ${hist.isKanjiMatch ? '<span style="font-size:0.84rem; color:#0369a1; font-weight:700;">(Chấp nhận dạng kèm Kanji)</span>' : ''}
                </div>`;
            } else if (hist.status === 'reveal') {
                panelCls += 'is-reveal';
                headerHtml = `<div style="font-size:1.08rem; font-weight:800; color:#b45309; margin-bottom:10px;">👁️ XEM ĐÁP ÁN CHUẨN</div>`;
            } else {
                panelCls += 'is-err';
                headerHtml = `<div style="font-size:1.08rem; font-weight:800; color:#be123c; margin-bottom:10px;">❌ CHƯA ĐÚNG — CÙNG XEM VÌ SAO SAI NHÉ!</div>`;
            }

            let compareHtml = '';
            const primaryReading = tpState.mode === 'sentence' ? item.hira : (tpState.mode === 'kanji' ? item.kana : (item.kana || item.jp));
            if (hist.status === 'err' && hist.lastInput !== undefined) {
                const diff = buildCharDiffHtml(hist.lastInput, primaryReading);
                compareHtml = `
                    <div class="tp-diff-row">
                        <div><strong style="color:#be123c;">Bạn đã gõ:</strong> <span class="jp-text" style="font-size:1.06rem;">${diff.typedHtml}</span></div>
                        <div><strong style="color:#15803d;">Đáp án đúng:</strong> <span class="jp-text" style="font-size:1.06rem;">${diff.targetHtml}</span></div>
                    </div>
                `;
            }

            let whyHtml = '';
            if (hist.status === 'err' && hist.whyWrong && hist.whyWrong.length) {
                whyHtml = `
                    <div class="tp-why-box">
                        <div style="font-weight:800; margin-bottom:6px;">🚨 Phân tích vì sao sai:</div>
                        <ul style="margin:0 0 0 18px; padding:0;">
                            ${hist.whyWrong.map(r => `<li style="margin-bottom:4px;">${r}</li>`).join('')}
                        </ul>
                    </div>
                `;
            }

            let meaningHtml = '';
            if (tpState.mode === 'sentence') {
                const alts = (item.acceptedHira || []).slice(1, 4);
                meaningHtml = `
                    <div class="tp-meaning-box">
                        <div style="margin-bottom:6px;">
                            <strong>🔊 Câu Hiragana chuẩn:</strong>
                            <span class="jp-text" style="font-size:1.12rem; font-weight:800; color:var(--primary-dark);">${escapeHtml(item.hira)}</span>
                            <button type="button" class="audio-btn" onclick="speakCurrentTypingWord()" style="vertical-align:middle; margin-left:6px;" title="Nghe phát âm">🔊</button>
                        </div>
                        <div style="margin-bottom:6px;"><strong>⛩️ Tham khảo kèm Kanji:</strong> <span class="jp-text" style="font-weight:700; color:#334155;">${escapeHtml(item.kanjiModel)}</span></div>
                        <div style="margin-bottom:6px;"><strong>🇻🇳 Nghĩa tiếng Việt:</strong> ${escapeHtml(item.vi)}</div>
                        <div style="margin-bottom:6px;"><strong>📐 Ngữ pháp (${escapeHtml(item.pattern)}):</strong> ${item.grammarRule}</div>
                        <div><strong>🧩 Bóc tách câu:</strong> ${item.breakdown}</div>
                        ${alts.length ? `<div style="margin-top:6px; font-size:0.84rem; color:#475569;"><strong>✔️ Biến thể cô cũng chấp nhận:</strong> ${alts.map(a => `<code class="jp-text">${escapeHtml(a)}</code>`).join(' • ')}</div>` : ''}
                    </div>
                `;
            } else if (tpState.mode === 'kanji') {
                meaningHtml = `
                    <div class="tp-meaning-box">
                        <div style="margin-bottom:6px; display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                            <span><strong>⛩️ Kanji:</strong> <span class="jp-text" style="font-size:1.35rem; font-weight:900; color:var(--primary-dark);">${escapeHtml(item.kanji)}</span></span>
                            <span><strong>🔤 Hiragana chuẩn:</strong> <span class="jp-text" style="font-size:1.2rem; font-weight:800; color:#15803d;">${escapeHtml(item.kana)}</span></span>
                            <button type="button" class="audio-btn" onclick="speakCurrentTypingWord()" title="Nghe phát âm">🔊</button>
                        </div>
                        <div style="margin-bottom:6px;"><strong>🏮 Âm Hán Việt:</strong> <span style="font-weight:800; color:#b45309; background:#fef3c7; padding:2px 8px; border-radius:6px;">${escapeHtml(item.hv)}</span></div>
                        <div style="margin-bottom:6px;"><strong>🇻🇳 Ý nghĩa:</strong> <strong>${escapeHtml(item.vi)}</strong></div>
                        <div><strong>🧠 Mẹo nhớ &amp; Phân biệt:</strong> ${item.note}</div>
                    </div>
                `;
            } else {
                meaningHtml = `
                    <div class="tp-meaning-box">
                        <div style="margin-bottom:6px;">
                            <strong>🇯🇵 Tiếng Nhật:</strong> <span class="jp-text" style="font-size:1.15rem; font-weight:800; color:var(--primary-dark);">${escapeHtml(item.jp)}</span>
                            ${item.kana ? `<span class="jp-text" style="color:var(--primary);">【${escapeHtml(item.kana)}】</span>` : ''}
                            <button type="button" class="audio-btn" onclick="speakCurrentTypingWord()" style="vertical-align:middle; margin-left:6px;">🔊</button>
                        </div>
                        <div style="margin-bottom:6px;"><strong>🔤 Romaji:</strong> ${escapeHtml(item.romaji || '')}</div>
                        <div><strong>🇻🇳 Nghĩa tiếng Việt:</strong> ${escapeHtml(item.vi)}</div>
                    </div>
                `;
            }

            detailPanel.className = panelCls;
            detailPanel.innerHTML = headerHtml + compareHtml + whyHtml + meaningHtml + `
                <div style="margin-top:12px; display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
                    <button type="button" class="btn-primary" style="padding:7px 14px; font-size:0.86rem; background:var(--secondary);" onclick="skipTypingWord()">➔ Sang câu tiếp theo (Enter)</button>
                    ${hist.status === 'err' ? `<button type="button" class="btn-primary" style="padding:7px 14px; font-size:0.86rem; background:var(--gray-600);" onclick="retryCurrentTypingCard()">🔄 Thử gõ lại câu này</button>` : ''}
                </div>
            `;
        }

        function handleTypingPrimaryBtn() {
            if (tpState.gradedCurrent) {
                skipTypingWord();
            } else {
                handleTypingSubmit();
            }
        }

        function retryCurrentTypingCard() {
            const pool = getFilteredTypingPool();
            const bucket = getActiveBucketKey();
            const item = pool[tpState.idxByBucket[bucket] || 0];
            if (!item) return;
            tpState.gradedCurrent = false;
            tpState.drafts[item.id] = '';
            delete tpState.history[item.id];
            renderTypingFilters();
            renderTypingCard(true);
            saveMini15_18Checkpoint();
        }

        function handleTypingSubmit() {
            const pool = getFilteredTypingPool();
            const bucket = getActiveBucketKey();
            const idx = tpState.idxByBucket[bucket] || 0;
            if (!pool.length || idx >= pool.length) return;

            const item = pool[idx];
            const inp = document.getElementById('tpCardInput');
            const rawVal = (inp.value || '').trim();
            if (!rawVal) {
                showToast('Vui lòng gõ đáp án trước khi kiểm tra!');
                inp.focus();
                return;
            }

            const normUser = cleanJpCompare(rawVal, true);
            let isCorrect = false;
            let isKanjiMatch = false;

            if (tpState.mode === 'sentence') {
                const normAcceptedHira = (item.acceptedHira || [item.hira]).map(x => cleanJpCompare(x, true));
                const hiraMatchNoKanji = normAcceptedHira.includes(normUser) && !containsKanji(rawVal);
                if (hiraMatchNoKanji) {
                    isCorrect = true;
                } else if (tpState.allowKanji) {
                    const normKanjiAcc = (item.kanjiAccepted || [item.kanjiModel]).map(x => cleanJpCompare(x, true));
                    if (normKanjiAcc.includes(normUser) || normAcceptedHira.includes(normUser)) {
                        isCorrect = true;
                        isKanjiMatch = containsKanji(rawVal);
                    }
                }
            } else if (tpState.mode === 'kanji') {
                if (!containsKanji(rawVal)) {
                    const normAccepted = (item.accepted || [item.kana]).map(x => cleanJpCompare(x, true));
                    isCorrect = normAccepted.includes(normUser);
                }
            } else {
                const accepted = new Set([cleanJpCompare(item.jp, true), cleanJpCompare(item.kana, true), cleanJpCompare(item.romaji, true)].filter(Boolean));
                isCorrect = accepted.has(normUser);
            }

            if (isCorrect) {
                tpState.streak++;
                tpState.history[item.id] = { status: 'ok', lastInput: rawVal, whyWrong: [], isKanjiMatch };
                delete tpState.drafts[item.id];
                tpState.gradedCurrent = true;
                const audioTxt = tpState.mode === 'sentence' ? item.hira : (item.jp || item.kanji || item.kana);
                speakText(audioTxt);
                renderTypingFilters();
                renderTypingCard(false);
                saveMini15_18Checkpoint();
                if (tpState.autoAdvance) {
                    setTimeout(() => {
                        skipTypingWord();
                    }, 900);
                }
            } else {
                tpState.streak = 0;
                const whyWrong = diagnoseTypingMistake(rawVal, item, tpState.mode);
                tpState.history[item.id] = { status: 'err', lastInput: rawVal, whyWrong, isKanjiMatch: false };
                tpState.drafts[item.id] = rawVal;
                tpState.gradedCurrent = true;
                const audioTxt = tpState.mode === 'sentence' ? item.hira : (item.jp || item.kanji || item.kana);
                speakText(audioTxt);
                renderTypingFilters();
                renderTypingCard(false);
                saveMini15_18Checkpoint();
            }
        }

        function updateTypingStats(pool) {
            const items = pool && pool.length ? pool : getModeItems(tpState.mode);
            let ok = 0, err = 0;
            items.forEach(it => {
                const h = tpState.history[it.id];
                if (h && h.status === 'ok') ok++;
                else if (h && h.status === 'err') err++;
            });
            document.getElementById('tpStatCorrect').innerText = ok;
            document.getElementById('tpStatWrong').innerText = err;
            const touched = ok + err;
            const pct = items.length === 0 ? 0 : Math.round((ok / items.length) * 100);
            document.getElementById('tpStatPercent').innerText = `${pct}% (${touched}/${items.length})`;
            const bar = document.getElementById('tpProgressBar');
            if (bar) bar.style.width = `${pct}%`;
        }

        function speakCurrentTypingWord() {
            const pool = getFilteredTypingPool();
            const bucket = getActiveBucketKey();
            const idx = tpState.idxByBucket[bucket] || 0;
            if (pool[idx]) {
                const it = pool[idx];
                speakText(tpState.mode === 'sentence' ? it.hira : (it.kanji || it.jp || it.kana));
            }
        }

        function showTypingHint() {
            const pool = getFilteredTypingPool();
            const bucket = getActiveBucketKey();
            const idx = tpState.idxByBucket[bucket] || 0;
            const item = pool[idx];
            const box = document.getElementById('tpHintPreview');
            if (!item || !box) return;

            if (tpState.mode === 'sentence') {
                const words = item.hira.split(/\\s+/);
                box.innerHTML = `💡 <strong>Gợi ý công thức:</strong> <code>${escapeHtml(item.pattern)}</code> • <strong>Bắt đầu bằng:</strong> <span class="jp-text">${escapeHtml(words.slice(0, 2).join(' '))}...</span>`;
            } else if (tpState.mode === 'kanji') {
                box.innerHTML = `💡 <strong>Gợi ý Hán Việt &amp; Nghĩa:</strong> <span style="color:#b45309;font-weight:800;">${escapeHtml(item.hv)}</span> (${escapeHtml(item.vi)}) • Chữ đầu: <strong class="jp-text">${escapeHtml((item.kana || '').charAt(0))}...</strong>`;
            } else {
                box.innerHTML = `💡 <strong>Gợi ý chữ cái đầu:</strong> <strong class="jp-text">${escapeHtml((item.kana || item.jp).charAt(0))}...</strong>`;
            }
            box.style.display = 'block';
            document.getElementById('tpCardInput').focus();
        }

        function revealTypingAnswer() {
            const pool = getFilteredTypingPool();
            const bucket = getActiveBucketKey();
            const idx = tpState.idxByBucket[bucket] || 0;
            const item = pool[idx];
            if (!item) return;

            tpState.streak = 0;
            const ans = tpState.mode === 'sentence' ? item.hira : (tpState.mode === 'kanji' ? item.kana : (item.kana || item.jp));
            tpState.history[item.id] = { status: 'reveal', lastInput: ans, whyWrong: [] };
            delete tpState.drafts[item.id];
            tpState.gradedCurrent = true;
            speakText(tpState.mode === 'sentence' ? item.hira : (item.kanji || item.jp));
            renderTypingCard(false);
            saveMini15_18Checkpoint();
        }

        function prevTypingItem() {
            const pool = getFilteredTypingPool();
            if (!pool.length) return;
            const bucket = getActiveBucketKey();
            const cur = tpState.idxByBucket[bucket] || 0;
            tpState.idxByBucket[bucket] = (cur - 1 + pool.length) % pool.length;
            tpState.gradedCurrent = false;
            renderTypingCard(true);
            saveMini15_18Checkpoint();
        }

        function skipTypingWord() {
            const pool = getFilteredTypingPool();
            if (!pool.length) return;
            const bucket = getActiveBucketKey();
            const cur = tpState.idxByBucket[bucket] || 0;
            tpState.idxByBucket[bucket] = (cur + 1) % pool.length;
            tpState.gradedCurrent = false;
            renderTypingCard(true);
            saveMini15_18Checkpoint();
        }

        function resetCurrentTypingMode() {
            const label = tpState.mode === 'sentence' ? 'Câu Tiếng Việt ➔ Hiragana' : (tpState.mode === 'kanji' ? 'Chữ Hán ➔ Hiragana' : 'Từ Vựng A2');
            if (!confirm(`Đặt lại tiến độ luyện gõ chế độ "${label}"?`)) return;
            getModeItems(tpState.mode).forEach(it => {
                delete tpState.history[it.id];
                delete tpState.drafts[it.id];
            });
            const bucket = getActiveBucketKey();
            tpState.idxByBucket[bucket] = 0;
            delete tpState.orderByBucket[bucket];
            tpState.streak = 0;
            tpState.gradedCurrent = false;
            renderTypingFilters();
            renderTypingCard(true);
            saveMini15_18Checkpoint();
            showToast(`Đã làm mới chế độ ${label}!`);
        }

        // ==========================================
        // CHECKPOINT LƯU / KHÔI PHỤC TOÀN BỘ TRẠNG THÁI (LOCALSTORAGE)
        // ==========================================
        function saveMini15_18Checkpoint() {
            try {
                saveCurrentExamDrafts();
                const payload = {
                    version: 2,
                    updatedAt: Date.now(),
                    currentTab,
                    currentExamId,
                    currentVocabFilter,
                    isMeaningHidden,
                    examStates,
                    tpState
                };
                localStorage.setItem(MINI15_18_CP_KEY, JSON.stringify(payload));
                if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
                    window.MarugotoCheckpoint.notifySaved();
                }
            } catch (e) {
                console.warn('Could not save checkpoint:', e);
            }
        }

        function restoreMini15_18Checkpoint() {
            try {
                const raw = localStorage.getItem(MINI15_18_CP_KEY);
                if (!raw) return false;
                const saved = JSON.parse(raw);
                if (!saved || saved.version !== 2) return false;

                if (saved.examStates && typeof saved.examStates === 'object') {
                    Object.keys(saved.examStates).forEach(k => {
                        if (EXAMS_LIST.some(e => e.id === k)) {
                            examStates[k] = saved.examStates[k];
                        }
                    });
                }
                if (saved.currentExamId && EXAMS_LIST.some(e => e.id === saved.currentExamId)) {
                    currentExamId = saved.currentExamId;
                }
                if (typeof saved.isMeaningHidden === 'boolean') isMeaningHidden = saved.isMeaningHidden;
                if (typeof saved.currentVocabFilter === 'string') currentVocabFilter = saved.currentVocabFilter;
                if (saved.tpState && typeof saved.tpState === 'object') {
                    tpState = Object.assign({}, tpState, saved.tpState);
                }
                if (typeof saved.currentTab === 'string') {
                    currentTab = saved.currentTab;
                }
                return true;
            } catch (e) {
                console.warn('Could not restore checkpoint:', e);
                return false;
            }
        }

        window.__MARUGOTO_CP_EXTRA_KEYS__ = [MINI15_18_CP_KEY];
        window.__MARUGOTO_ON_RESET__ = function () {
            localStorage.removeItem(MINI15_18_CP_KEY);
            window.location.reload();
        };

        document.addEventListener('DOMContentLoaded', () => {
            const restored = restoreMini15_18Checkpoint();

            const inp = document.getElementById('tpCardInput');
            if (inp) {
                inp.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter' && !e.shiftKey && !e.isComposing && e.keyCode !== 229) {
                        e.preventDefault();
                        handleTypingPrimaryBtn();
                    }
                });
                inp.addEventListener('input', () => {
                    const pool = getFilteredTypingPool();
                    const bucket = getActiveBucketKey();
                    const item = pool[tpState.idxByBucket[bucket] || 0];
                    if (item) {
                        tpState.drafts[item.id] = inp.value;
                        if (tpState.gradedCurrent) {
                            tpState.gradedCurrent = false;
                            const btn = document.getElementById('tpCardCheckBtn');
                            if (btn) {
                                btn.innerText = 'Kiểm Tra Đáp Án ⏎';
                                btn.style.background = 'var(--primary)';
                            }
                        }
                        saveMini15_18Checkpoint();
                    }
                });
            }

            const p3Wrap = document.getElementById('part3Container');
            if (p3Wrap) {
                p3Wrap.addEventListener('input', (e) => {
                    if (e.target && e.target.id && e.target.id.startsWith('p3_input_')) {
                        saveMini15_18Checkpoint();
                    }
                });
            }
            const p6Wrap = document.getElementById('part6Container');
            if (p6Wrap) {
                p6Wrap.addEventListener('input', (e) => {
                    if (e.target && e.target.id && e.target.id.startsWith('p6_txt_')) {
                        saveMini15_18Checkpoint();
                    }
                });
            }

            bindActiveExamAliases();
            updateExamHeaderBanner();
            renderExamSwitcher();
            renderVocab(VOCAB_DATA);
            renderKanji(KANJI_DATA);
            renderPart1();
            renderPart2();
            renderPart3();
            renderPart4();
            renderPart5();
            renderPart6();
            const total = computeExamScore(currentExamId);
            const disp = document.getElementById('totalScoreText');
            if (disp) disp.innerText = `${total} / 100 Điểm`;

            const h = (window.location.hash || '').toLowerCase();
            if (h === '#typing' || h === '#tab-typing') {
                switchMainTab('tab-typing', true);
            } else if (restored && currentTab && document.getElementById(currentTab)) {
                switchMainTab(currentTab, true);
            }
            if (restored) {
                showToast('💾 Đã khôi phục checkpoint bài làm trước đó!');
            }
        });
    </script>
    <script src="../assets/nav.js?v=6" defer></script>
</body>
</html>
"""

from l15_18_typing_data import KANJI_15_18_ITEMS, KANJI_11_14_ITEMS, SENTENCE_TYPING_DATA
kanji_15_18_json_str = json.dumps(KANJI_15_18_ITEMS, ensure_ascii=False)
kanji_11_14_json_str = json.dumps(KANJI_11_14_ITEMS, ensure_ascii=False)
sentences_json_str = json.dumps(SENTENCE_TYPING_DATA, ensure_ascii=False)

html_content = (
    HTML_TEMPLATE.replace('__VOCAB_JSON__', vocab_json_str)
    .replace('__KANJI_JSON__', kanji_json_str)
    .replace('__EXAMS_JSON__', exams_json_str)
    .replace('__KANJI_15_18_JSON__', kanji_15_18_json_str)
    .replace('__KANJI_11_14_JSON__', kanji_11_14_json_str)
    .replace('__SENTENCES_JSON__', sentences_json_str)
)

output_path = os.path.join(WORKSPACE, 'tests/On_Tap_Mini_Test_A2_15_18.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated {output_path} (size: {len(html_content)} chars)")
