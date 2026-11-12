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
    <script src="../assets/js/audio-engine.js?v=2"></script>
    <link rel="stylesheet" href="../assets/css/mini-test-15-18.css?v=1">
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
                        <button type="button" class="btn-primary" id="tpCardSpeakBtn" style="background:#0ea5e9;" onclick="speakCurrentTypingWord(this)">🔊 Nghe Mẫu</button>
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
    <script src="../assets/data/mini_15_18_data.js?v=1"></script>
    <script src="../assets/js/jp-typing-grader.js?v=1"></script>
    <script src="../assets/js/typing-studio.js?v=2"></script>
    <script src="../assets/js/mini-test-15-18.js?v=2"></script>
    <script src="../assets/nav.js?v=6" defer></script>
</body>
</html>
"""

from l15_18_typing_data import KANJI_15_18_ITEMS, KANJI_11_14_ITEMS, SENTENCE_TYPING_DATA

os.makedirs(os.path.join(WORKSPACE, "assets/data"), exist_ok=True)
data_payload = {
    "VOCAB_DATA": vocab_15_18,
    "KANJI_DATA": kanji_15_18,
    "EXAMS_LIST": EXAMS_SUITE,
    "KANJI_15_18_DATA": KANJI_15_18_ITEMS,
    "KANJI_11_14_DATA": KANJI_11_14_ITEMS,
    "SENTENCE_TYPING_DATA": SENTENCE_TYPING_DATA,
}
data_js_path = os.path.join(WORKSPACE, "assets/data/mini_15_18_data.js")
with open(data_js_path, "w", encoding="utf-8") as df:
    df.write("window.MINI_15_18_DATA = ")
    json.dump(data_payload, df, ensure_ascii=False, separators=(",", ":"))
    df.write(";\n")

output_path = os.path.join(WORKSPACE, "tests/On_Tap_Mini_Test_A2_15_18.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE)

print(f"Successfully generated {output_path} ({len(HTML_TEMPLATE)} chars) and {data_js_path}")
