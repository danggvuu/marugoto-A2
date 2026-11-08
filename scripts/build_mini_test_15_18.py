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

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

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
        "category": "Bài 15 • Triệu chứng & Giải thích lý do",
        "q": "「顔色が 悪いですね。どうしたんですか。」――「ちょっと お腹が [____]。」",
        "options": ["痛いんです", "痛いです", "痛くなんです", "痛かったんですか"],
        "correct": 0,
        "explain": "Khi đối phương hỏi thăm tình trạng bất thường 「どうしたんですか」, ta dùng tính từ đuôi い + 「んです」 (痛いんです) để giải thích tình trạng cơ thể khó chịu."
    },
    {
        "id": 2,
        "category": "Bài 15 • Lời khuyên nhẹ nhàng",
        "q": "「喉が 痛くて、声が 出ないんです。」――「じゃあ、温かい お茶を [____] と いいですよ。」",
        "options": ["飲む", "飲んだ", "飲んで", "飲み"],
        "correct": 0,
        "explain": "Đưa ra lời khuyên hữu ích cho sức khỏe: 「Động từ thể Từ điển (V-る) ＋ といいですよ」 (Làm ... thì tốt đấy nhé!)."
    },
    {
        "id": 3,
        "category": "Bài 15 • Dặn dò khuyên can",
        "q": "「熱が 38度も ありますから、きょうは お風呂に [____] ください。」",
        "options": ["入らないで", "入らない", "入らなくて", "入るないで"],
        "correct": 0,
        "explain": "Dặn dò, khuyên can bệnh nhân không nên làm điều gì quá sức: 「V(thể ない) ＋ でください」 (Xin đừng...)."
    },
    {
        "id": 4,
        "category": "Bài 16 • Liệt kê hành động",
        "q": "休みの日は 公園を [____]、ジムで 泳いだり しています。",
        "options": ["走ったり", "走って", "走るたり", "走った"],
        "correct": 0,
        "explain": "Cấu trúc liệt kê hành động tiêu biểu đại diện: 「V1-たり、V2-たり します / しています」. Động từ 走る nhóm 1 ➔ 走った ➔ 走ったり."
    },
    {
        "id": 5,
        "category": "Bài 16 • Mục đích hành động",
        "q": "「[____] の ために、毎日 階段を 使っているんですか。」――「健康のためです。」",
        "options": ["何", "だれ", "どこ", "いつ"],
        "correct": 0,
        "explain": "Hỏi mục đích: 「何 (なん) の ために [Hành động]」 (Để phục vụ cho điều gì / Vì cái gì?)."
    },
    {
        "id": 6,
        "category": "Bài 16 • Lời khuyên nên làm",
        "q": "「風邪を ひいたようです。」――「無理を しないで、きょうは 早く [____] ほうが いいですよ。」",
        "options": ["寝た", "寝る", "寝て", "寝ない"],
        "correct": 0,
        "explain": "Khuyên bảo dứt khoát nên làm gì: 「V-た ほうがいいです」 (Nên làm... thì tốt hơn)."
    },
    {
        "id": 7,
        "category": "Bài 17 • Trợ từ nhận quà",
        "q": "「素敵な 時計ですね。」――「ええ、誕生日に 父 [____] もらったんです。」",
        "options": ["に", "を", "で", "へ"],
        "correct": 0,
        "explain": "Nhận quà từ ai đó dùng trợ từ 「に」 (hoặc 「から」): 「[Người tặng] に [Món quà] を もらいました / もらったんです」."
    },
    {
        "id": 8,
        "category": "Bài 17 • Liệt kê đại diện とか",
        "q": "引越し祝いには、お皿 [____] グラス [____] が いいと 思います。",
        "options": ["とか／とか", "や／など", "と／と", "たり／たり"],
        "correct": 0,
        "explain": "Liệt kê danh từ tiêu biểu mang tính đại diện, tự nhiên trong hội thoại: 「N1 とか N2 とか」 (như là... hay là...)."
    },
    {
        "id": 9,
        "category": "Bài 18 • Bày tỏ quan điểm cá nhân",
        "q": "「送別会の プレゼントは 何が いいですか。」――「鈴木さんは お酒が 好きですから、ワインが [____] と 思います。」",
        "options": ["いい", "いいだ", "よく", "いいの"],
        "correct": 0,
        "explain": "Trước 「と思います」 là thể thông thường (Futsuukei). Tính từ đuôi い giữ nguyên dạng: 「いい と 思います」."
    },
    {
        "id": 10,
        "category": "Bài 18 • Động từ mặc trang phục",
        "q": "パーティーの 会場に、黒い スーツを 着て、眼鏡を [____] いる 人が います。",
        "options": ["かけて", "かぶって", "はいて", "きて"],
        "correct": 0,
        "explain": "Đeo kính dùng động từ 「掛けます (かけます)」 ➔ 「眼鏡を 掛けています」. (Đội mũ dùng 被る, mặc quần/giày dùng 履く, mặc áo dùng 着る)."
    }
]

# 4. Data for Part II: Sentence Ordering (5 Questions - 15 pts)
PART2_ARRANGE = [
    {
        "id": 11,
        "category": "Bài 15 • Trình bày lý do nghỉ làm",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "今朝から",
        "post": "休んだんです。",
        "chips": ["熱が", "あって、", "頭も痛いので", "会社を"],
        "correctOrder": [0, 1, 2, 3],
        "starIndex": 2,
        "starChip": "頭も痛いので",
        "fullSentence": "今朝から 熱が あって、頭も痛いので 会社を 休んだんです。",
        "simplifiedSentence": "今朝から 熱があって、頭も痛いので 会社を 休んだんです。",
        "explain": "Nối hai triệu chứng sức khỏe bằng thể Te 「熱があって」 + lý do 「頭も痛いので」 + kết quả 「会社を休んだんです」. Vị trí ngôi sao là [頭も痛いので]."
    },
    {
        "id": 12,
        "category": "Bài 16 • Khuyên nhủ vì sức khỏe",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "健康の",
        "post": "ほうがいいですよ。",
        "chips": ["ために、", "野菜を", "食べた", "たくさん"],
        "correctOrder": [0, 1, 3, 2],
        "starIndex": 2,
        "starChip": "たくさん",
        "fullSentence": "健康の ために、野菜を たくさん 食べた ほうがいいですよ。",
        "simplifiedSentence": "健康のために、野菜をたくさん食べたほうがいいですよ。",
        "explain": "Mục đích 「健康のために」 + bổ ngữ chỉ lượng 「野菜を たくさん」 + khuyên nhủ 「食べた ほうがいいですよ」. Vị trí ngôi sao là [たくさん]."
    },
    {
        "id": 13,
        "category": "Bài 16 • Liệt kê thói quen rèn luyện",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "休みの日は",
        "post": "しています。",
        "chips": ["公園を", "走ったり、", "プールで", "泳いだり"],
        "correctOrder": [0, 1, 2, 3],
        "starIndex": 2,
        "starChip": "プールで",
        "fullSentence": "休みの日は 公園を 走ったり、プールで 泳いだり しています。",
        "simplifiedSentence": "休みの日は 公園を走ったり、プールで泳いだりしています。",
        "explain": "Cấu trúc liệt kê: 「[Địa điểm 1] を 走ったり、[★ Địa điểm 2 で] 泳いだり しています」. Vị trí ngôi sao là [プールで]."
    },
    {
        "id": 14,
        "category": "Bài 17 • Tặng quà cưới bạn thân",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "友だちの",
        "post": "あげました。",
        "chips": ["結婚祝いに、", "二人に", "きれいな", "ペアグラスを"],
        "correctOrder": [0, 1, 2, 3],
        "starIndex": 2,
        "starChip": "きれいな",
        "fullSentence": "友だちの 結婚祝いに、二人に きれいな ペアグラスを あげました。",
        "simplifiedSentence": "友だちの 結婚祝いに、二人に きれいな ペアグラスを あげました。",
        "explain": "Dịp tặng quà 「結婚祝いに」 + đối tượng nhận 「二人に」 + tính từ bổ nghĩa 「きれいな」 + tân ngữ 「ペアグラスを」 + động từ 「あげました」. Vị trí ngôi sao là [きれいな]."
    },
    {
        "id": 15,
        "category": "Bài 18 • Trích dẫn lời người khác",
        "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "山田さんは",
        "post": "言っていました。",
        "chips": ["都合が", "悪くて", "パーティーに", "行けないと"],
        "correctOrder": [0, 1, 2, 3],
        "starIndex": 2,
        "starChip": "パーティーに",
        "fullSentence": "山田さんは 都合が 悪くて パーティーに 行けないと 言っていました。",
        "simplifiedSentence": "山田さんは 都合が悪くて パーティーに行けないと言っていました。",
        "explain": "Nguyên nhân bận việc 「都合が悪くて」 + điểm đến 「パーティーに」 + thể phủ định khả năng 「行けないと」 + trích dẫn 「言っていました」. Vị trí ngôi sao là [パーティーに]."
    }
]

# 5. Data for Part III: Fill in Correct Conjugated Form (5 Questions - 15 pts)
PART3_CONJUGATE = [
    {
        "id": 16,
        "category": "Bài 15 • Động từ thể Phủ định cấm đoán nhẹ",
        "sentence": "熱が あるときは、無理を (する) [_______] でください。",
        "baseWord": "する",
        "accepted": ["しない", "shinai"],
        "displayAnswer": "しない (shinai)",
        "explain": "Động từ bất quy tắc nhóm 3 「する」 chuyển sang thể Phủ định ngắn (Nai) là 「しない」. Cấu trúc: 「V-ないでください」 (Xin đừng...)."
    },
    {
        "id": 17,
        "category": "Bài 15 • Động từ thể Từ điển đưa lời khuyên",
        "sentence": "風邪気味の ときは、ビタミンCを たくさん (とる) [_______] と いいですよ。",
        "baseWord": "とる (取ります)",
        "accepted": ["とる", "取る", "toru"],
        "displayAnswer": "とる / 取る (toru)",
        "explain": "Cấu trúc đưa lời khuyên hữu ích cho sức khỏe: 「V(thể từ điển) ＋ といいですよ」. Động từ 取る giữ nguyên dạng từ điển."
    },
    {
        "id": 18,
        "category": "Bài 16 • Động từ thể Quá khứ khuyên nhủ nên làm",
        "sentence": "夜 遅くまで 起きていないで、早く (寝る) [_______] ほうが いいですよ。",
        "baseWord": "寝る (ねる)",
        "accepted": ["ねた", "寝た", "neta"],
        "displayAnswer": "寝た / ねた (neta)",
        "explain": "Động từ nhóm 2 「寝る (ねる)」 chuyển sang thể Quá khứ (Ta) là 「寝た (ねた)」. Cấu trúc: 「V-た ほうがいいです」."
    },
    {
        "id": 19,
        "category": "Bài 17 • Định ngữ thể Quá khứ nhận quà",
        "sentence": "これは 去年の 誕生日に 恋人に (もらう) [_______] ペアリングです。",
        "baseWord": "もらう",
        "accepted": ["もらった", "moratta"],
        "displayAnswer": "もらった (moratta)",
        "explain": "Định ngữ bổ nghĩa cho danh từ ペアリング trong quá khứ: Động từ nhóm 1 đuôi う ➔ 「もらった」."
    },
    {
        "id": 20,
        "category": "Bài 18 • Động từ thể Te diễn tả trang phục",
        "sentence": "あそこで 青い 着物を (着る) [_______] いる 人は どなたですか。",
        "baseWord": "着る (きる)",
        "accepted": ["きて", "着て", "kite"],
        "displayAnswer": "着て / きて (kite)",
        "explain": "Động từ nhóm 2 「着る (きる)」 chuyển sang thể Te là 「着て」. Cấu trúc trạng thái đang mặc trang phục: 「V-ています」."
    }
]

# 6. Data for Part IV: Matching Situation & Response (4 Questions - 10 pts)
PART4_MATCH = [
    {
        "id": 21,
        "category": "Bài 15 • Triệu chứng & Khuyên đi khám",
        "promptA": "「昨日から 熱が あって、喉も すごく 痛いんです。」",
        "correctBId": "B1",
        "promptB": "「それは 大変ですね。きょうは 無理を しないで、病院へ 行くと いいですよ。」",
        "explain": "Khi nghe đối phương kể triệu chứng bị sốt và đau họng, ta đáp lại bằng lời đồng cảm 「それは大変ですね」 kèm lời khuyên 「無理をしないで、病院へ行くといいですよ」."
    },
    {
        "id": 22,
        "category": "Bài 16 • Thói quen lười vận động & Lời khuyên",
        "promptA": "「最近、お腹が 出てきて、体が 重いんです。」",
        "correctBId": "B2",
        "promptB": "「健康のために、エレベーターを 使わないで、階段を 歩いた ほうが いいですよ。」",
        "explain": "Lời khuyên thực tế để giảm cân và rèn luyện: 「階段を歩いたほうがいいですよ」 (Nên đi bộ cầu thang bộ)."
    },
    {
        "id": 23,
        "category": "Bài 17 • Khen ngợi phụ kiện & Nguồn gốc",
        "promptA": "「その ネクタイ、とても おしゃれですね。どこで 買ったんですか。」",
        "correctBId": "B3",
        "promptB": "「これですか。就職祝いに 兄に もらったんです。」",
        "explain": "Khi được khen đồ dùng cá nhân, người Nhật thường khiêm tốn giải thích nguồn gốc được tặng bằng cấu trúc 「〜にもらったんです」."
    },
    {
        "id": 24,
        "category": "Bài 18 • Hỏi ý kiến về trang phục dự tiệc",
        "promptA": "「明日の ホームパーティー、どんな 服を 着て 行けば いいですか。」",
        "correctBId": "B4",
        "promptB": "「カジュアルな 集まりですから、スーツじゃなくて ジーンズでも いいと 思いますよ。」",
        "explain": "Tư vấn trang phục cho tiệc tại nhà: Không cần mặc comple cứng nhắc, mặc quần bò cũng được (「ジーンズでもいいと思います」)."
    }
]

# 7. Data for Part V: Reading Comprehension (4 Questions - 20 pts)
PART5_READING = [
    {
        "passageId": 1,
        "title": "BÀI ĐỌC 1: 健康な 生活の アドバイス (Lời Khuyên Giữ Gìn Sức Khỏe - Bài 15 & 16)",
        "text": "みなさん、毎日 元気に 過ごして いますか。冬は 空気が 乾燥して、風邪を ひきやすい 季節です。もし「少し 喉が 痛いな」とか「熱が あるな」と 思ったら、無理を しないで 早く 寝る ことが 大切です。お風呂に 長く 入らないで、温かい スープや お茶を 飲むと いいですよ。<br>また、病気に ならない ために、普段から 運動した ほうが いいです。毎朝 走ったり、階段を 歩いたり して、体を 動かしましょう。そして、野菜や 果物を たくさん 食べる ように してください。",
        "questions": [
            {
                "id": 25,
                "q": "風邪気味の とき、どうした ほうが いいと 書いてありますか。",
                "options": [
                    "お風呂に 長く 入った ほうがいい",
                    "無理を しないで、温かいものを 飲んで 早く 寝た ほうがいい",
                    "公園を たくさん 走った ほうがいい",
                    "冷たい 水を たくさん 飲んだ ほうがいい"
                ],
                "correct": 1,
                "explain": "Trong bài viết: 「無理を しないで 早く 寝る ことが 大切です。お風呂に 長く 入らないで、温かい スープや お茶を 飲むと いいですよ」."
            },
            {
                "id": 26,
                "q": "病気に ならない ために、普段から 何を すると いいですか。",
                "options": [
                    "階段を 使わないで エレベーターに 乗る",
                    "走ったり 階段を 歩いたり して 体を 動かす",
                    "薬を 毎日 飲む",
                    "一日中 家で 休む"
                ],
                "correct": 1,
                "explain": "Trong bài viết nêu rõ: 「病気に ならない ために、普段から 運動した ほうが いいです。毎朝 走ったり、階段を 歩いたり して、体を 動かしましょう」."
            }
        ]
    },
    {
        "passageId": 2,
        "title": "BÀI ĐỌC 2: 送別会と プレゼントの 相談 (Bàn Bạc Tiệc Chia Tay & Chọn Quà - Bài 17 & 18)",
        "text": "来週の 金曜日、会社で 田中さんの 送別会を します。田中さんは 来月から 大阪の 支社へ 引っ越します。みんなで レストランで 食事を したり、思い出の 写真を 見たり する 予定です。<br>昨日、幹事の リンさんに「プレゼントは 何が いいですか」と 聞きました。リンさんは「田中さんは コーヒーが 好きですから、おしゃれな コーヒーカップとか タンブラーが いいと 思います」と 言っていました。田中さんは いつも 青い シャツを 着て いますから、青い カップを 買う つもりです。",
        "questions": [
            {
                "id": 27,
                "q": "田中さんは 来月から どうしますか。",
                "options": [
                    "会社を やめて 外国へ 行く",
                    "大阪の 支社へ 引っ越す",
                    "東京で 新しい 会社に 入る",
                    "リンさんと いっしょに 旅行する"
                ],
                "correct": 1,
                "explain": "Trong bài viết: 「田中さんは 来月から 大阪の 支社へ 引っ越します」."
            },
            {
                "id": 28,
                "q": "リンさんは プレゼントについて 何と 言っていましたか。",
                "options": [
                    "高い スーツを あげた ほうがいいと言っていた",
                    "コーヒーカップとか タンブラーが いいと 言っていた",
                    "何も 買わないで 現金を あげると言っていた",
                    "お酒や ビールが 一番いいと言っていた"
                ],
                "correct": 1,
                "explain": "Trong bài viết: 「リンさんは『田中さんは コーヒーが 好きですから、おしゃれな コーヒーカップとか タンブラーが いいと 思います』と 言っていました」."
            }
        ]
    }
]

# 8. Data for Part VI: Sentence Translation (4 Questions - 15 pts)
PART6_TRANSLATION = [
    {
        "id": 29,
        "category": "Bài 15 • Giải thích lý do nghỉ làm",
        "vi": "Từ sáng nay tôi bị sốt nên đã xin nghỉ làm ở công ty.",
        "hint": "今朝から (けさから), 熱があります (ねつがあります), 会社 (かいしゃ), 休みました (やすみました)",
        "modelSentence": "今朝から 熱が あるので、会社を 休んだんです。",
        "modelKana": "けさから ねつが あるので、かいしゃを やすんだんです。",
        "keywords": ["今朝から", "熱が", "あるので", "会社を", "休んだ"],
        "breakdown": [
            {"part": "今朝から", "role": "Thời điểm bắt đầu (từ sáng nay)"},
            {"part": "熱が あるので / 熱があって", "role": "Nguyên nhân chỉ lý do (bị sốt)"},
            {"part": "会社を 休んだんです", "role": "Kết quả thực tế + んです phân trần giải thích"}
        ]
    },
    {
        "id": 30,
        "category": "Bài 16 • Mục đích & Liệt kê rèn luyện",
        "vi": "Để tốt cho sức khỏe, vào ngày nghỉ tôi lúc thì chạy bộ, lúc thì bơi lội.",
        "hint": "健康 (けんこう), ために, 休みの 日 (やすみのひ), 走ります (はしります ➔ はしったり), 泳ぎます (およぎます ➔ およいだり)",
        "modelSentence": "健康の ために、休みの 日は 走ったり、泳いだり しています。",
        "modelKana": "けんこうの ために、やすみの ひは はしったり、およいだり しています。",
        "keywords": ["健康", "ために", "休み", "走ったり", "泳いだり"],
        "breakdown": [
            {"part": "健康の ために", "role": "Biểu đạt mục đích: N の ために (vì sức khỏe)"},
            {"part": "休みの 日は", "role": "Chủ đề thời gian (vào ngày nghỉ)"},
            {"part": "走ったり、泳いだり しています", "role": "Liệt kê hành động tiêu biểu: V1-たり、V2-たり しています"}
        ]
    },
    {
        "id": 31,
        "category": "Bài 17 • Nhận quà từ người thân",
        "vi": "Chiếc đồng hồ này là món quà tôi đã nhận được từ bố vào ngày sinh nhật.",
        "hint": "この 時計 (この とけい), 誕生日 (たんじょうび), 父 (ちち), もらいました / もらったんです",
        "modelSentence": "この 時計は 誕生日に 父に もらったんです。",
        "modelKana": "この とけいは たんじょうびに ちちに もらったんです。",
        "keywords": ["時計", "誕生日に", "父に", "もらった"],
        "breakdown": [
            {"part": "この 時計は", "role": "Chủ ngữ được đưa lên làm đề tài (chiếc đồng hồ này)"},
            {"part": "誕生日に", "role": "Thời điểm (vào ngày sinh nhật)"},
            {"part": "父に", "role": "Đối tượng trao quà (nhận từ ai đó: [Người] に)"},
            {"part": "もらったんです", "role": "Động từ nhận quà ở thì quá khứ + んです giải thích nguồn gốc"}
        ]
    },
    {
        "id": 32,
        "category": "Bài 18 • Bày tỏ ý kiến cá nhân với Tính từ đuôi な",
        "vi": "Tôi nghĩ rằng bữa tiệc chia tay vào tuần sau sẽ rất náo nhiệt và vui vẻ.",
        "hint": "来週 (らいしゅう), 送別会 (そうべつかい), とても, にぎやか (tính từ đuôi な), 思います (おもいます)",
        "modelSentence": "来週の 送別会は とても にぎやかだと 思います。",
        "modelKana": "らいしゅうの そうべつかいは とても にぎやかだと おもいます。",
        "keywords": ["来週", "送別会", "とても", "にぎやかだ", "思います"],
        "breakdown": [
            {"part": "来週の 送別会は", "role": "Chủ ngữ (bữa tiệc chia tay tuần sau)"},
            {"part": "とても にぎやかだと", "role": "Tính từ đuôi な thể thông thường khẳng định hiện tại phải thêm だ (にぎやかだ + と)"},
            {"part": "思います", "role": "Mẫu câu nêu suy nghĩ, quan điểm cá nhân"}
        ]
    }
]

# Build JSON Data Strings
vocab_json_str = json.dumps(vocab_15_18, ensure_ascii=False)
kanji_json_str = json.dumps(kanji_15_18, ensure_ascii=False)
p1_json_str = json.dumps(PART1_MC, ensure_ascii=False)
p2_json_str = json.dumps(PART2_ARRANGE, ensure_ascii=False)
p3_json_str = json.dumps(PART3_CONJUGATE, ensure_ascii=False)
p4_json_str = json.dumps(PART4_MATCH, ensure_ascii=False)
p5_json_str = json.dumps(PART5_READING, ensure_ascii=False)
p6_json_str = json.dumps(PART6_TRANSLATION, ensure_ascii=False)

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
            background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
            color: var(--gray-800);
            line-height: 1.6;
            min-height: 100vh;
        }

        .jp-text {
            font-family: 'Noto Sans JP', sans-serif;
        }

        /* Hero Header */
        .hero-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
            color: var(--white);
            padding: 40px 20px 32px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
            border-bottom: 3px solid rgba(255, 255, 255, 0.1);
        }

        .hero-header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 60%);
            pointer-events: none;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            padding: 6px 16px;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 14px;
            border: 1px solid rgba(255, 255, 255, 0.2);
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
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 18px;
            border-radius: var(--radius-full);
            font-size: 0.88rem;
            font-weight: 600;
            color: #e2e8f0;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        /* Container */
        .main-container {
            max-width: 1240px;
            margin: 0 auto;
            padding: 24px 16px 80px 16px;
        }

        /* Tab Navigation Bar */
        .tab-nav-wrapper {
            position: sticky;
            top: 0;
            z-index: 50;
            background: rgba(248, 250, 252, 0.95);
            backdrop-filter: blur(12px);
            padding: 12px 0;
            margin-bottom: 24px;
            border-bottom: 1px solid var(--gray-200);
        }

        .tab-nav {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            scrollbar-width: thin;
            background: var(--white);
            border-radius: var(--radius-lg);
            padding: 6px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
        }

        .tab-btn {
            flex: 1;
            white-space: nowrap;
            padding: 12px 18px;
            border: none;
            background: transparent;
            color: var(--gray-600);
            font-size: 0.95rem;
            font-weight: 700;
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .tab-btn:hover {
            color: var(--primary);
            background: var(--gray-100);
        }
        .tab-btn.active {
            background: var(--primary);
            color: var(--white);
            box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3);
        }

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
            gap: 8px;
            overflow-x: auto;
            padding: 4px 4px 18px 4px;
            margin-bottom: 22px;
        }
        .quicknav-pill {
            padding: 8px 16px;
            border-radius: var(--radius-full);
            background: var(--white);
            border: 1px solid var(--gray-300);
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--gray-700);
            text-decoration: none;
            white-space: nowrap;
            transition: all 0.2s;
        }
        .quicknav-pill:hover {
            background: var(--primary);
            color: var(--white);
            border-color: var(--primary);
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
    <link rel="stylesheet" href="../assets/css/site-theme.css">
</head>
<body>

    <!-- Global Hub Navigation Placeholder -->
    <div id="navbar-placeholder"></div>

    <!-- Hero Header -->
    <header class="hero-header">
        <div class="hero-badge">🎓 MARUGOTO A2-2 • FINAL REVIEW EXAM</div>
        <h1 class="hero-title">Đề Thi Thử & Cẩm Nang Ôn Tập Bài 15 - 18</h1>
        <p class="hero-desc">Hệ thống tổng hợp toàn diện 4 bài cuối giáo trình Marugoto A2-2: Lý thuyết chuyên sâu, 135 từ vựng Quizlet sạch, 34 chữ Hán chiết tự, Đề thi chuẩn 6 dạng 100 điểm & Luyện gõ phản xạ Nhật - Việt.</p>
        <div class="hero-stats">
            <span class="hero-stat-pill">📖 4 Bài Học (L15 ➔ L18)</span>
            <span class="hero-stat-pill">🎴 135 Từ Vựng Cốt Lõi</span>
            <span class="hero-stat-pill">⛩️ 34 Chữ Hán Kanji</span>
            <span class="hero-stat-pill">🎯 Đề Thi Thử 100 Điểm (6 Dạng)</span>
            <span class="hero-stat-pill">⌨️ Flash Typing Gõ Nhật - Việt</span>
        </div>
    </header>

    <!-- Sticky Tab Navigation -->
    <div class="tab-nav-wrapper">
        <nav class="tab-nav">
            <button class="tab-btn active" onclick="switchMainTab('tab-theory')">📖 Lý Thuyết (Bài 15 - 18)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-vocab')">🎴 135 Từ Vựng</button>
            <button class="tab-btn" onclick="switchMainTab('tab-kanji')">⛩️ 34 Chữ Hán</button>
            <button class="tab-btn" onclick="switchMainTab('tab-quiz')">🎯 Đề Thi Thử (6 Dạng • 100đ)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-typing')">⌨️ Luyện Gõ Phản Xạ</button>
            <button class="tab-btn" onclick="switchMainTab('tab-cheatsheet')">⚡ Cẩm Nang Bỏ Túi</button>
        </nav>
    </div>

    <main class="main-container">

        <!-- ========================================== -->
        <!-- TAB 1: LÝ THUYẾT NGỮ PHÁP (BÀI 15 - 18)    -->
        <!-- ========================================== -->
        <div id="tab-theory" class="tab-panel active">
            <!-- Quick Jump Bar -->
            <div class="theory-quicknav">
                <a href="#grammar-l15" class="quicknav-pill" style="background: var(--primary); color: white;">🏥 Bài 15: Cơ Thể & Triệu Chứng (～んです／～といい)</a>
                <a href="#grammar-l16" class="quicknav-pill" style="background: var(--primary); color: white;">🏃 Bài 16: Rèn Luyện Sức Khỏe (～たり～たり／～たほうがいい)</a>
                <a href="#grammar-l17" class="quicknav-pill" style="background: var(--primary); color: white;">🎁 Bài 17: Quà Tặng & Kỷ Niệm (もらいました／あげます／とか)</a>
                <a href="#grammar-l18" class="quicknav-pill" style="background: var(--primary); color: white;">👘 Bài 18: Lễ Hội & Trang Phục (～と思います／着ています)</a>
            </div>

            <!-- BÀI 15 -->
            <div class="grammar-card" id="grammar-l15">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 15 (A2-2)</span>
                        <h2 class="grammar-title">体操するといいですよ (Cơ Thể & Triệu Chứng Bệnh • Giải Thích & Lời Khuyên)</h2>
                    </div>
                    <span class="section-badge">Trọng điểm A2-2</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Giải thích lý do, tình trạng sức khỏe: <code>[Thể thông thường] ＋ んです</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Động từ: <code>休むんです</code> / <code>起きられないんです</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Tính từ đuôi い: <code>痛いんです</code> / <code>だるいんです</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Tính từ đuôi な / Danh từ: <code>病気なんです</code> / <code>風邪なんです</code><br>
                        2. Lời khuyên nhẹ nhàng hữu ích: <code>V(thể từ điển) ＋ といいですよ</code><br>
                        3. Dặn dò, khuyên can cấm đoán nhẹ: <code>V(thể ない) ＋ でください</code>
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <code>〜んです</code>: Mẫu câu kinh điển khi được hỏi thăm <em>「どうしたんですか」(Bạn bị làm sao vậy?)</em> để bày tỏ và giải thích triệu chứng đang gặp phải, mong nhận được sự thông cảm hoặc tư vấn.<br>
                        • <code>〜といいですよ</code>: Lời khuyên thân thiện, mang tính chia sẻ kinh nghiệm hữu ích cho đối phương mà không hề áp đặt.<br>
                        • <code>〜ないでください</code>: Nhắc nhở người bệnh dặn dò chăm sóc bản thân, không làm quá sức (<em>あまり無理をしないでください</em>).
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">「どうしたんですか。」――「ちょっと 頭が <span style="color: var(--primary);">痛いんです</span>。」
                                <button type="button" class="audio-btn" onclick="speakText('どうしたんですか。ちょっと頭が痛いんです。')">🔊</button>
                            </div>
                            <div class="ex-vi">"Bạn bị làm sao vậy?" ―― "Tôi bị đau đầu một chút."</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">寝る 前に、温かい お茶を <span style="color: var(--primary);">飲むと いいですよ</span>。
                                <button type="button" class="audio-btn" onclick="speakText('寝る前に、温かいお茶を飲むといいですよ。')">🔊</button>
                            </div>
                            <div class="ex-vi">Trước khi đi ngủ, bạn uống một tách trà ấm thì rất tốt đấy nhé!</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">熱が ありますから、きょうは お風呂に <span style="color: var(--primary);">入らないで ください</span>。
                                <button type="button" class="audio-btn" onclick="speakText('熱がありますから、きょうはお風呂に入らないでください。')">🔊</button>
                            </div>
                            <div class="ex-vi">Vì bạn đang bị sốt nên hôm nay xin đừng ngâm bồn tắm nhé.</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Trước <code>んです</code>: Tính từ đuôi な và Danh từ thì hiện tại khẳng định bắt buộc phải chuyển thành <code>なん (病気なんです, 暇なんです)</code>, TUYỆT ĐỐI không dùng <code>だんです</code>.
                    </div>
                </div>
            </div>

            <!-- BÀI 16 -->
            <div class="grammar-card" id="grammar-l16">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 16 (A2-2)</span>
                        <h2 class="grammar-title">走ったり、泳いだりしています (Lối Sống Lành Mạnh • Liệt Kê & Lời Khuyên Nên Làm)</h2>
                    </div>
                    <span class="section-badge">Trọng điểm A2-2</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Liệt kê hành động tiêu biểu: <code>V1-たり、V2-たり します / しています</code><br>
                        2. Biểu đạt mục đích hành động: <code>[Danh từ] の ために ＋ [Hành động]</code><br>
                        3. Lời khuyên nên làm: <code>V(thể Quá khứ Ta) ＋ ほうがいいです</code><br>
                        4. Lời khuyên KHÔNG nên làm: <code>V(thể Phủ định Nai) ＋ ほうがいいです</code>
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <code>〜たり、〜たりします</code>: Liệt kê một vài hành động đại diện trong số nhiều việc mình làm (ví dụ: ngày nghỉ tôi lúc thì chạy bộ, lúc thì đọc sách). Đuôi cuối cùng chia theo thì của cả câu.<br>
                        • <code>〜のために</code>: Nêu rõ mục đích vì cái gì (<em>健康のために: vì sức khỏe; 試験のために: vì kỳ thi</em>).<br>
                        • <code>〜たほうがいい / 〜ないほうがいい</code>: Lời khuyên dứt khoát, so sánh giữa việc nên làm và không làm (ví dụ: nên ăn nhiều rau xanh, không nên thức khuya).
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">休みの日は 公園を <span style="color: var(--primary);">走ったり</span>、プールで <span style="color: var(--primary);">泳いだり しています</span>。
                                <button type="button" class="audio-btn" onclick="speakText('休みの日は公園を走ったり、プールで泳いだりしています。')">🔊</button>
                            </div>
                            <div class="ex-vi">Vào ngày nghỉ, tôi lúc thì chạy bộ ở công viên, lúc thì đi bơi ở hồ bơi.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text"><span style="color: var(--primary);">健康の ために</span>、毎朝 ジョギングを しています。
                                <button type="button" class="audio-btn" onclick="speakText('健康のために、毎朝ジョギングをしています。')">🔊</button>
                            </div>
                            <div class="ex-vi">Vì sức khỏe, mỗi buổi sáng tôi đều chạy bộ thể dục.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">野菜を たくさん <span style="color: var(--primary);">食べた ほうがいいですよ</span>。
                                <button type="button" class="audio-btn" onclick="speakText('野菜をたくさん食べたほうがいいですよ。')">🔊</button>
                            </div>
                            <div class="ex-vi">Bạn nên ăn nhiều rau xanh thì tốt hơn đấy.</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Cẩn thận nhầm lẫn giữa <code>V-た ほうがいい</code> (khuyên nên làm - dùng thể Quá khứ) và <code>V-ない ほうがいい</code> (khuyên không nên làm - dùng thể Phủ định Nai, KHÔNG dùng thể quá khứ phủ định).
                    </div>
                </div>
            </div>

            <!-- BÀI 17 -->
            <div class="grammar-card" id="grammar-l17">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 17 (A2-2)</span>
                        <h2 class="grammar-title">誕生日に彼にもらったんです (Quà Tặng & Kỷ Niệm • Trao Nhận & Liệt Kê とか)</h2>
                    </div>
                    <span class="section-badge">Trọng điểm A2-2</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Nhận quà từ ai đó: <code>Watashi wa [Người tặng] に [Vật] を もらいました / もらったんです</code><br>
                        2. Tặng quà cho ai đó: <code>Watashi wa [Người nhận] に [Vật] を あげます / あげました</code><br>
                        3. Liệt kê danh từ đại diện: <code>N1 とか N2 とか</code><br>
                        4. Định ngữ với もの (đồ vật để làm gì): <code>[V(thể từ điển)] ＋ もの</code>
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <code>〜に もらいました</code>: Diễn tả việc nhận đồ từ ai đó. Trong giao tiếp thực tế, khi đối phương khen đồ của mình, người Nhật dùng <code>〜にもらったんです</code> để chia sẻ nguồn gốc món quà ấm áp.<br>
                        • <code>〜に あげます</code>: Tặng cho ai đó món quà nhân dịp kỷ niệm (sinh nhật, ngày của Mẹ, đám cưới, thôi nôi).<br>
                        • <code>〜とか 〜とか</code>: Liệt kê danh từ nhẹ nhàng, tự nhiên trong khẩu ngữ hàng ngày (<em>スカーフとか手袋とか</em>).<br>
                        • <code>V-る ＋ もの</code>: Tạo cụm danh từ chỉ đồ vật dùng vào mục đích cụ thể (<em>書くもの: đồ để viết; 部屋に飾るもの: đồ trang trí phòng</em>).
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">この ネックレスは 誕生日に 彼<span style="color: var(--primary);">に もらったんです</span>。
                                <button type="button" class="audio-btn" onclick="speakText('このネックレスは誕生日に彼にもらったんです。')">🔊</button>
                            </div>
                            <div class="ex-vi">Chiếc dây chuyền này là tôi nhận được từ bạn trai nhân dịp sinh nhật đấy.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">母の日に 母<span style="color: var(--primary);">に 花を あげました</span>。
                                <button type="button" class="audio-btn" onclick="speakText('母の日に母に花をあげました。')">🔊</button>
                            </div>
                            <div class="ex-vi">Vào Ngày của Mẹ, tôi đã tặng hoa cho mẹ.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">冬の プレゼントは 手袋<span style="color: var(--primary);">とか</span> マフラー<span style="color: var(--primary);">とか</span>が いいですね。
                                <button type="button" class="audio-btn" onclick="speakText('冬のプレゼントは手袋とかマフラーとかがいいですね。')">🔊</button>
                            </div>
                            <div class="ex-vi">Quà tặng mùa đông thì những thứ như găng tay hay khăn quàng cổ là rất hợp nhỉ.</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Người tặng hay người nhận đều đi với trợ từ <code>に</code>. Cần nhìn động từ cuối câu: Nếu là <code>もらいました</code> thì người đứng trước <code>に</code> là NGƯỜI TẶNG; nếu là <code>あげました</code> thì người đứng trước <code>に</code> là NGƯỜI NHẬN.
                    </div>
                </div>
            </div>

            <!-- BÀI 18 -->
            <div class="grammar-card" id="grammar-l18">
                <div class="grammar-header">
                    <div>
                        <span class="grammar-tag">BÀI 18 (A2-2)</span>
                        <h2 class="grammar-title">パーティーがいいと思います (Sự Kiện & Trang Phục • Quan Điểm, Trích Dẫn & Thể V-ています)</h2>
                    </div>
                    <span class="section-badge">Trọng điểm A2-2</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        1. Bày tỏ ý kiến cá nhân: <code>[Thể thông thường (Futsuukei)] ＋ と 思います</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Tính từ đuôi な / Danh từ: <code>[N / Na] ＋ だ ＋ と 思います</code> (Lưu ý chữ だ!)<br>
                        2. Trích dẫn gián tiếp lời người khác: <code>[Thể thông thường] ＋ と 言っていました</code><br>
                        3. Động từ trang phục trạng thái đang mặc: <code>V-ています</code><br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Mặc thân trên / toàn thân: <code>着ます ➔ 着ています</code> (áo sơ mi, vest, kimono)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Mặc thân dưới / chân: <code>履きます ➔ 履いています</code> (quần, tất, giày, váy ngắn)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Đội đầu: <code>被ります ➔ 被っています</code> (mũ, nón)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Đeo mắt: <code>掛けます ➔ 掛けています</code> (kính)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;• Phụ kiện: <code>します ➔ しています</code> (cà vạt, đồng hồ, nhẫn)
                    </div>
                    <p class="grammar-explain">
                        <strong>Phân tích chi tiết:</strong><br>
                        • <code>〜と思います</code>: Bày tỏ suy nghĩ chủ quan, dự đoán khi bàn bạc tổ chức sự kiện, liên hoan.<br>
                        • <code>〜と言っていました</code>: Truyền đạt lại thông tin mà người thứ ba đã nói trước đó.<br>
                        • <code>Động từ trang phục</code>: Tiếng Nhật phân chia cực kỳ tỉ mỉ theo từng bộ phận cơ thể. Khi miêu tả ai đó đang mặc món đồ gì, bắt buộc dùng thì tiếp diễn trạng thái <code>〜ています</code>.
                    </p>
                    <ul class="example-list">
                        <li class="example-item">
                            <div class="ex-jp jp-text">明日の 送別会は とても にぎやか<span style="color: var(--primary);">だと 思います</span>。
                                <button type="button" class="audio-btn" onclick="speakText('明日の送別会はとてもにぎやかだと思います。')">🔊</button>
                            </div>
                            <div class="ex-vi">Tôi nghĩ rằng buổi tiệc chia tay ngày mai sẽ rất là náo nhiệt.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">山田さんは 来週 出張する<span style="color: var(--primary);">と 言っていました</span>。
                                <button type="button" class="audio-btn" onclick="speakText('山田さんは来週出張すると言っていました。')">🔊</button>
                            </div>
                            <div class="ex-vi">Anh Yamada đã nói rằng tuần sau anh ấy sẽ đi công tác.</div>
                        </li>
                        <li class="example-item">
                            <div class="ex-jp jp-text">白い シャツを <span style="color: var(--primary);">着て</span>、眼鏡を <span style="color: var(--primary);">掛けている</span> 人です。
                                <button type="button" class="audio-btn" onclick="speakText('白いシャツを着て、眼鏡を掛けている人です。')">🔊</button>
                            </div>
                            <div class="ex-vi">Là người đang mặc áo sơ mi trắng và đeo kính mắt.</div>
                        </li>
                    </ul>
                    <div class="trap-box">
                        <strong>⚠️ Bẫy thi cần chú ý:</strong>
                        Trước <code>と思います</code>, nếu là Danh từ hoặc Tính từ đuôi な ở dạng khẳng định hiện tại, BẮT BUỘC phải thêm <code>だ</code>: <em>「パーティーは にぎやか【だ】と 思います」</em>, <em>「あの人は 先生【だ】と 思います」</em>. Thiếu <code>だ</code> là sai ngữ pháp!
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
            <!-- Exam Timer & Score Bar -->
            <div class="exam-timer-box">
                <div>
                    <div style="font-size: 0.85rem; color: #c7d2fe; font-weight: 700;">ĐỀ THI TỔNG HỢP MARUGOTO A2-2 (BÀI 15 - 18)</div>
                    <div style="font-size: 1.3rem; font-weight: 800; margin-top: 2px;">6 Dạng Bài Chuẩn Sư Phạm • 32 Câu Hỏi</div>
                </div>
                <div style="display: flex; align-items: center; gap: 18px; flex-wrap: wrap;">
                    <div style="text-align: right;">
                        <div style="font-size: 0.82rem; color: #cbd5e1;">ĐIỂM SỐ HIỆN TẠI</div>
                        <div class="exam-score-display" id="totalScoreText">0 / 100 Điểm</div>
                    </div>
                    <button type="button" class="btn-primary" onclick="resetAllExam()" style="background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25);">🔄 Làm Lại Từ Đầu</button>
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
        <!-- TAB 5: LUYỆN GÕ PHẢN XẠ NHẬT - VIỆT         -->
        <!-- ========================================== -->
        <div id="tab-typing" class="tab-panel">
            <div class="typing-container">
                <div class="section-header">
                    <div>
                        <h2 class="section-title">⌨️ Luyện Gõ Tiếng Nhật Phản Xạ Từ Tiếng Việt</h2>
                        <p style="color: var(--gray-600); font-size: 0.92rem; margin-top: 4px;">Nhìn nghĩa tiếng Việt ➔ gõ ngay Romaji hoặc Hiragana hoặc Kanji. Tự động chấm điểm, phát âm Tokyo chuẩn!</p>
                    </div>
                    <div class="vocab-filter-group" id="typingFilterGroup">
                        <button type="button" class="v-filter-btn active" onclick="switchTypingLesson('all')">Tất cả (135)</button>
                        <button type="button" class="v-filter-btn" onclick="switchTypingLesson('A2-15')">Bài 15</button>
                        <button type="button" class="v-filter-btn" onclick="switchTypingLesson('A2-16')">Bài 16</button>
                        <button type="button" class="v-filter-btn" onclick="switchTypingLesson('A2-17')">Bài 17</button>
                        <button type="button" class="v-filter-btn" onclick="switchTypingLesson('A2-18')">Bài 18</button>
                    </div>
                </div>

                <div class="typing-card-view">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <span id="tpCardBadge" style="font-weight: 700; color: var(--gray-500); font-size: 0.9rem;">Thẻ 1 / 135</span>
                        <span id="tpStreakBadge" class="typing-streak">🔥 Chuỗi: 0</span>
                    </div>

                    <div style="background: var(--gray-50); border: 2px dashed var(--gray-300); border-radius: var(--radius-lg); padding: 30px 20px; margin-bottom: 20px;">
                        <div style="font-size: 0.85rem; color: var(--gray-500); font-weight: 700; text-transform: uppercase;">Ý NGHĨA TIẾNG VIỆT</div>
                        <div id="tpPromptVi" class="typing-prompt">Đang tải...</div>
                        <div id="tpCardFeedback" style="min-height: 24px; font-weight: 700; font-size: 0.98rem;"></div>
                    </div>

                    <input type="text" id="tpCardInput" class="typing-input-large" placeholder="Gõ Romaji hoặc Hiragana/Kanji rồi bấm Enter..." autocomplete="off" autocapitalize="off" spellcheck="false">

                    <div class="typing-actions">
                        <button type="button" class="btn-primary" id="tpCardCheckBtn" onclick="handleTypingSubmit()">Kiểm Tra (Enter)</button>
                        <button type="button" class="btn-primary" onclick="speakCurrentTypingWord()" style="background: var(--secondary);">🔊 Phát Âm</button>
                        <button type="button" class="btn-primary" onclick="showTypingHint()" style="background: var(--purple);">💡 Gợi Ý</button>
                        <button type="button" class="btn-primary" onclick="revealTypingAnswer()" style="background: var(--warning);">👁️ Đáp Án</button>
                        <button type="button" class="btn-primary" onclick="skipTypingWord()" style="background: var(--gray-600);">⏭️ Bỏ Qua</button>
                    </div>

                    <div style="margin-top: 24px; display: flex; justify-content: center; gap: 24px; font-size: 0.95rem; font-weight: 700; color: var(--gray-600);">
                        <span>Đúng: <strong id="tpStatCorrect" style="color: var(--success);">0</strong></span>
                        <span>Sai: <strong id="tpStatWrong" style="color: var(--accent);">0</strong></span>
                        <span>Tỷ lệ: <strong id="tpStatPercent" style="color: var(--primary);">0%</strong></span>
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
                        <h2 class="section-title">⚡ Cẩm Nang Bỏ Túi • Bí Kíp Tránh Bẫy Sư Phạm</h2>
                        <p style="color: var(--gray-600); font-size: 0.92rem; margin-top: 4px;">Những điểm ngữ pháp the chốt thường xuyên xuất hiện trong đề kiểm tra giữa kỳ & cuối kỳ Marugoto A2.</p>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
                    <!-- Cheatsheet 1 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">1. Phân Biệt 3 Sắc Thái Khuyên Nhủ</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • <code>V-るといいですよ</code>: Lời khuyên thân thiện, gợi ý bổ ích (ví dụ: uống trà nóng thì tốt đấy). Không mang tính ép buộc.<br>
                            • <code>V-たほうがいいですよ</code>: Khuyên dứt khoát, so sánh giữa 2 lựa chọn (nên làm A thì tốt hơn làm B, nếu không làm sẽ không tốt).<br>
                            • <code>V-ないでください</code>: Nhắc nhở dặn dò cấm đoán nhẹ (đừng cố quá sức, đừng uống bia lạnh).
                        </p>
                    </div>

                    <!-- Cheatsheet 2 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">2. Ma Trận Cho - Nhận (Trao Tặng)</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • <code>[Người nhận] に [Vật] を あげます</code>: Tặng cho ai đó (hướng hành động đi ra xa khỏi người nói).<br>
                            • <code>[Người tặng] に [Vật] を もらいました</code>: Nhận từ ai đó. (Khi khoe đồ người khác tặng dùng: <em>〜にもらったんです</em>).<br>
                            • <strong>Tuyệt chiêu nhận diện:</strong> Nhìn động từ cuối câu để biết người đứng trước trợ từ <code>に</code> là người tặng hay người nhận!
                        </p>
                    </div>

                    <!-- Cheatsheet 3 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">3. Bản Đồ Động Từ Mặc Trang Phục</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • <strong>Thân trên & Toàn thân:</strong> <code>着ます (きます)</code> ➔ áo sơ mi, áo khoác, vest, kimono, váy liền.<br>
                            • <strong>Thân dưới & Chân:</strong> <code>履きます (はきます)</code> ➔ quần dài, quần đùi, váy ngắn, giày, tất.<br>
                            • <strong>Đầu:</strong> <code>被ります (かぶります)</code> ➔ mũ len, nón bảo hiểm.<br>
                            • <strong>Mắt:</strong> <code>掛けます (かけます)</code> ➔ kính mắt, kính râm.<br>
                            • <strong>Phụ kiện:</strong> <code>します</code> ➔ cà vạt, đồng hồ đeo tay, nhẫn, vòng cổ.
                        </p>
                    </div>

                    <!-- Cheatsheet 4 -->
                    <div style="background: var(--gray-50); border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 20px;">
                        <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 10px;">4. Bẫy Thể Thông Thường Trước と思います</h3>
                        <p style="font-size: 0.92rem; color: var(--gray-700); line-height: 1.7;">
                            • Động từ: <code>行く / 行かない / 行った</code> + <code>と思います</code>.<br>
                            • Tính từ đuôi い: <code>おいしい / いい</code> + <code>と思います</code>.<br>
                            • <strong>BẪY LỚN:</strong> Tính từ đuôi な và Danh từ ở thì hiện tại khẳng định BẮT BUỘC phải thêm <code>だ</code>:<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;➔ <em>にぎやか<strong>だ</strong>と思います</em> (Không được nói: にぎやかと思います)<br>
                            &nbsp;&nbsp;&nbsp;&nbsp;➔ <em>先生<strong>だ</strong>と思います</em> (Không được nói: 先生と思います).
                        </p>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- Toast Notification -->
    <div id="toast"></div>

    <!-- Scripts -->
    <script>
        // DỮ LIỆU TỪ BACKEND PYTHON
        const VOCAB_DATA = __VOCAB_JSON__;
        const KANJI_DATA = __KANJI_JSON__;
        const P1_DATA = __P1_JSON__;
        const P2_DATA = __P2_JSON__;
        const P3_DATA = __P3_JSON__;
        const P4_DATA = __P4_JSON__;
        const P5_DATA = __P5_JSON__;
        const P6_DATA = __P6_JSON__;

        // TRẠNG THÁI TOÀN CỤC
        let currentTab = 'tab-theory';
        let currentVocabFilter = 'all';
        let isMeaningHidden = false;

        // Điểm số các phần
        let scoreState = {
            p1: {},
            p2: {},
            p3: {},
            p4: {},
            p5: {},
            p6: {}
        };

        // Chuyển tab chính
        function switchMainTab(tabId) {
            currentTab = tabId;
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            const activeBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick').includes(tabId));
            if (activeBtn) activeBtn.classList.add('active');

            const targetPanel = document.getElementById(tabId);
            if (targetPanel) targetPanel.classList.add('active');

            if (tabId === 'tab-typing') {
                initTypingPractice();
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
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
            c.innerHTML = P1_DATA.map((item, idx) => `
                <div class="question-item" id="p1_item_${item.id}">
                    <div class="q-title">
                        <span class="q-badge">Câu ${item.id}</span>
                        <span class="jp-text" style="font-size:1.1rem;">${item.q}</span>
                    </div>
                    <div class="options-list">
                        ${item.options.map((opt, oIdx) => `
                            <button type="button" class="opt-btn jp-text" id="p1_opt_${item.id}_${oIdx}" onclick="selectPart1Answer(${item.id}, ${oIdx})">
                                ${['A', 'B', 'C', 'D'][oIdx]}. ${opt}
                            </button>
                        `).join('')}
                    </div>
                    <div class="explain-box" id="p1_exp_${item.id}">
                        <strong>💡 Giải thích:</strong> ${item.explain}
                    </div>
                </div>
            `).join('');
        }

        function selectPart1Answer(qId, oIdx) {
            const item = P1_DATA.find(q => q.id === qId);
            if (!item) return;

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
        let arrangeState = {};

        function renderPart2() {
            const c = document.getElementById('part2Container');
            if (!c) return;
            c.innerHTML = P2_DATA.map(item => {
                arrangeState[item.id] = {
                    placed: [],
                    available: item.chips.map((chip, idx) => ({ text: chip, origIdx: idx }))
                };
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
                            <span style="color:var(--gray-400); font-size:0.9rem;">(Click các mảnh ghép bên dưới để sắp xếp vào đây)</span>
                        </div>
                        <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:12px;" id="p2_pool_${item.id}">
                            ${item.chips.map((chip, idx) => `
                                <button type="button" class="chip-btn jp-text" id="p2_chip_${item.id}_${idx}" onclick="clickArrangeChip(${item.id}, ${idx})">${chip}</button>
                            `).join('')}
                        </div>
                        <div style="display:flex; gap:10px; align-items:center;">
                            <button type="button" class="btn-primary" onclick="checkArrangeAnswer(${item.id})" style="padding:6px 14px; font-size:0.88rem;">Kiểm Tra</button>
                            <button type="button" class="btn-primary" onclick="resetSingleArrange(${item.id})" style="padding:6px 14px; font-size:0.88rem; background:var(--gray-600);">Đặt Lại</button>
                            <span id="p2_status_${item.id}" style="font-weight:700; font-size:0.92rem;"></span>
                        </div>
                        <div class="explain-box" id="p2_exp_${item.id}">
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
        }

        function removeArrangeChip(qId, origIdx) {
            const st = arrangeState[qId];
            if (!st) return;
            const chipData = st.placed.find(c => c.origIdx === origIdx);
            if (!chipData) return;

            st.placed = st.placed.filter(c => c.origIdx !== origIdx);
            st.available.push(chipData);
            updateArrangeUI(qId);
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
                <button type="button" class="chip-btn jp-text" onclick="clickArrangeChip(${qId}, ${c.origIdx})">${c.text}</button>
            `).join('');
        }

        function resetSingleArrange(qId) {
            const item = P2_DATA.find(q => q.id === qId);
            if (!item) return;
            arrangeState[qId] = {
                placed: [],
                available: item.chips.map((chip, idx) => ({ text: chip, origIdx: idx }))
            };
            updateArrangeUI(qId);
            document.getElementById(`p2_status_${qId}`).innerText = '';
            document.getElementById(`p2_exp_${qId}`).style.display = 'none';
        }

        function checkArrangeAnswer(qId) {
            const item = P2_DATA.find(q => q.id === qId);
            const st = arrangeState[qId];
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
            } else {
                statusEl.innerHTML = '<span style="color:var(--accent);">✗ Chưa chính xác (0 điểm)</span>';
                scoreState.p2[qId] = 0;
            }

            expEl.style.display = 'block';
            updateTotalScore();
        }

        // PART 3: CONJUGATION
        function renderPart3() {
            const c = document.getElementById('part3Container');
            if (!c) return;
            c.innerHTML = P3_DATA.map(item => `
                <div class="question-item" id="p3_item_${item.id}">
                    <div class="q-title">
                        <span class="q-badge">Câu ${item.id}</span>
                        <span class="jp-text" style="font-size:1.05rem;">${item.sentence}</span>
                    </div>
                    <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap; margin:12px 0;">
                        <input type="text" class="conjugate-input jp-text" id="p3_input_${item.id}" placeholder="Nhập đáp án...">
                        <button type="button" class="btn-primary" onclick="checkConjugateAnswer(${item.id})" style="padding:7px 16px; font-size:0.9rem;">Kiểm Tra</button>
                        <span id="p3_status_${item.id}" style="font-weight:700; font-size:0.92rem;"></span>
                    </div>
                    <div class="explain-box" id="p3_exp_${item.id}">
                        <strong>💡 Đáp án đúng:</strong> <span class="jp-text" style="color:var(--success); font-weight:800;">${item.displayAnswer}</span><br>
                        <strong>Giải thích:</strong> ${item.explain}
                    </div>
                </div>
            `).join('');
        }

        function checkConjugateAnswer(qId) {
            const item = P3_DATA.find(q => q.id === qId);
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
        let selectedA = null;
        let matchedPairs = {};

        function renderPart4() {
            const c = document.getElementById('part4Container');
            if (!c) return;
            c.innerHTML = `
                <div class="question-item">
                    <div style="font-size:0.95rem; color:var(--gray-600); margin-bottom:14px;">
                        👉 <em>Click chọn một câu ở Cột A (Tình huống), sau đó click chọn câu đối đáp tương ứng ở Cột B.</em>
                    </div>
                    <div class="matching-grid">
                        <div id="colAContainer">
                            ${P4_DATA.map(item => `
                                <div class="match-card jp-text" id="match_A_${item.id}" onclick="clickMatchA(${item.id})">
                                    <strong>A${item.id - 20}:</strong> ${item.promptA}
                                </div>
                            `).join('')}
                        </div>
                        <div id="colBContainer">
                            ${P4_DATA.slice().sort(() => Math.random() - 0.5).map(item => `
                                <div class="match-card jp-text" id="match_B_${item.correctBId}" onclick="clickMatchB('${item.correctBId}')">
                                    <strong>${item.correctBId}:</strong> ${item.promptB}
                                </div>
                            `).join('')}
                        </div>
                    </div>
                    <div style="display:flex; gap:12px; align-items:center;">
                        <button type="button" class="btn-primary" onclick="resetMatching()" style="background:var(--gray-600); padding:6px 14px; font-size:0.88rem;">Đặt Lại Cột Nối</button>
                        <span id="matchScoreText" style="font-weight:700;"></span>
                    </div>
                    <div class="explain-box" id="p4_exp_all">
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
            selectedA = null;
            matchedPairs = {};
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
            c.innerHTML = P5_DATA.map(passage => `
                <div class="question-item">
                    <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary); margin-bottom:12px;">${passage.title}</h3>
                    <div class="reading-box jp-text">${passage.text}</div>
                    <div>
                        ${passage.questions.map(q => `
                            <div style="margin-bottom:18px; padding-bottom:14px; border-bottom:1px dashed var(--gray-200);">
                                <div class="q-title">
                                    <span class="q-badge">Câu ${q.id}</span>
                                    <span class="jp-text">${q.q}</span>
                                </div>
                                <div class="options-list">
                                    ${q.options.map((opt, oIdx) => `
                                        <button type="button" class="opt-btn jp-text" id="p5_opt_${q.id}_${oIdx}" onclick="selectPart5Answer(${q.id}, ${oIdx}, ${passage.passageId})">
                                            ${['A', 'B', 'C', 'D'][oIdx]}. ${opt}
                                        </button>
                                    `).join('')}
                                </div>
                                <div class="explain-box" id="p5_exp_${q.id}">
                                    <strong>💡 Giải thích:</strong> ${q.explain}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `).join('');
        }

        function selectPart5Answer(qId, oIdx, pId) {
            const passage = P5_DATA.find(p => p.passageId === pId);
            if (!passage) return;
            const item = passage.questions.find(q => q.id === qId);
            if (!item) return;

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
            c.innerHTML = P6_DATA.map(item => `
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
                        <span id="p6_status_${item.id}" style="font-weight:700;"></span>
                    </div>
                    <div class="explain-box" id="p6_model_${item.id}">
                        <div style="font-size:1.1rem; font-weight:800; color:var(--primary); margin-bottom:6px;" class="jp-text">
                            ${item.modelSentence}
                            <button type="button" class="audio-btn" onclick="speakText('${item.modelSentence}')" style="vertical-align:middle; margin-left:6px;">🔊</button>
                        </div>
                        <div style="color:var(--gray-600); font-size:0.9rem; margin-bottom:8px;">${item.modelKana}</div>
                        <strong>Phân tích ngữ pháp:</strong>
                        <ul style="margin-left:20px; font-size:0.92rem; color:var(--gray-700);">
                            ${item.breakdown.map(b => `<li><strong>${b.part}</strong>: ${b.role}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            `).join('');
        }

        function toggleTranslationModel(qId) {
            const el = document.getElementById(`p6_model_${qId}`);
            if (el) el.style.display = el.style.display === 'block' ? 'none' : 'block';
        }

        function selfGradeTranslation(qId, pts) {
            scoreState.p6[qId] = pts;
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
            let total = 0;
            ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'].forEach(p => {
                Object.values(scoreState[p]).forEach(val => {
                    total += Number(val) || 0;
                });
            });
            const disp = document.getElementById('totalScoreText');
            if (disp) {
                disp.innerText = `${Math.round(total * 10) / 10} / 100 Điểm`;
            }
        }

        function resetAllExam() {
            if (!confirm('Bạn có chắc chắn muốn làm lại toàn bộ đề thi không?')) return;
            scoreState = { p1: {}, p2: {}, p3: {}, p4: {}, p5: {}, p6: {} };
            renderPart1();
            renderPart2();
            renderPart3();
            renderPart4();
            renderPart5();
            renderPart6();
            updateTotalScore();
            showToast('Đã đặt lại toàn bộ đề thi!');
        }

        // ==========================================
        // TYPING PRACTICE ENGINE
        // ==========================================
        let typingWords = [];
        let typingIdx = 0;
        let typingStreak = 0;
        let typingCorrect = 0;
        let typingWrong = 0;

        function initTypingPractice() {
            switchTypingLesson('all');
        }

        function switchTypingLesson(lesson) {
            document.querySelectorAll('#typingFilterGroup .v-filter-btn').forEach(b => b.classList.remove('active'));
            const activeBtn = Array.from(document.querySelectorAll('#typingFilterGroup .v-filter-btn')).find(b => b.getAttribute('onclick').includes(lesson));
            if (activeBtn) activeBtn.classList.add('active');

            typingWords = lesson === 'all' ? [...VOCAB_DATA] : VOCAB_DATA.filter(w => w.l === lesson);
            typingWords.sort(() => Math.random() - 0.5);
            typingIdx = 0;
            typingStreak = 0;
            typingCorrect = 0;
            typingWrong = 0;
            loadTypingCard();
        }

        function loadTypingCard() {
            if (typingIdx >= typingWords.length) {
                document.getElementById('tpPromptVi').innerHTML = '🎉 Chúc mừng bạn đã hoàn thành toàn bộ danh sách gõ phản xạ!';
                document.getElementById('tpCardFeedback').innerText = '';
                document.getElementById('tpCardInput').disabled = true;
                return;
            }
            const item = typingWords[typingIdx];
            document.getElementById('tpCardBadge').innerText = `Thẻ ${typingIdx + 1} / ${typingWords.length} (${item.l || ''})`;
            document.getElementById('tpStreakBadge').innerText = `🔥 Chuỗi: ${typingStreak}`;
            document.getElementById('tpPromptVi').innerText = item.vi;
            document.getElementById('tpCardFeedback').innerText = '';
            const inp = document.getElementById('tpCardInput');
            inp.disabled = false;
            inp.value = '';
            inp.className = 'typing-input-large';
            inp.focus();
            updateTypingStats();
        }

        function cleanAnswerStr(s) {
            if (!s) return '';
            return s.toString().toLowerCase().trim().replace(/[()（）~～/／、,。.\\s\\-_\\t]/g, '');
        }

        function handleTypingSubmit() {
            if (typingIdx >= typingWords.length) return;
            const item = typingWords[typingIdx];
            const inp = document.getElementById('tpCardInput');
            const feedback = document.getElementById('tpCardFeedback');
            const userVal = cleanAnswerStr(inp.value);

            if (!userVal) {
                feedback.innerHTML = '<span style="color:var(--warning);">Vui lòng gõ đáp án trước khi bấm Enter!</span>';
                return;
            }

            const accepted = new Set([
                cleanAnswerStr(item.jp),
                cleanAnswerStr(item.kana),
                cleanAnswerStr(item.romaji)
            ]);

            const isCorrect = accepted.has(userVal);

            if (isCorrect) {
                typingStreak++;
                typingCorrect++;
                inp.classList.add('correct');
                feedback.innerHTML = `<span style="color:var(--success);">✓ Chính xác! (${item.jp} • ${item.kana || ''})</span>`;
                speakText(item.jp);
                setTimeout(() => {
                    typingIdx++;
                    loadTypingCard();
                }, 700);
            } else {
                typingStreak = 0;
                typingWrong++;
                inp.classList.add('wrong');
                feedback.innerHTML = `<span style="color:var(--accent);">✗ Chưa chính xác! Đáp án đúng: <strong>${item.jp}</strong> (${item.kana || ''})</span>`;
                speakText(item.jp);
            }
            updateTypingStats();
        }

        function updateTypingStats() {
            document.getElementById('tpStatCorrect').innerText = typingCorrect;
            document.getElementById('tpStatWrong').innerText = typingWrong;
            const total = typingCorrect + typingWrong;
            const pct = total === 0 ? 0 : Math.round((typingCorrect / total) * 100);
            document.getElementById('tpStatPercent').innerText = `${pct}%`;
        }

        function speakCurrentTypingWord() {
            if (typingIdx < typingWords.length) {
                speakText(typingWords[typingIdx].jp);
            }
        }

        function showTypingHint() {
            if (typingIdx < typingWords.length) {
                const item = typingWords[typingIdx];
                const hint = (item.kana || item.jp).charAt(0);
                document.getElementById('tpCardFeedback').innerHTML = `<span style="color:var(--purple);">💡 Chữ cái đầu tiên: <strong>${hint}...</strong></span>`;
                document.getElementById('tpCardInput').focus();
            }
        }

        function revealTypingAnswer() {
            if (typingIdx < typingWords.length) {
                const item = typingWords[typingIdx];
                typingStreak = 0;
                document.getElementById('tpStreakBadge').innerText = `🔥 Chuỗi: 0`;
                document.getElementById('tpCardInput').value = item.jp;
                document.getElementById('tpCardFeedback').innerHTML = `<span style="color:var(--warning);">Đáp án: <strong>${item.jp}</strong> (${item.kana || ''} - ${item.romaji || ''})</span>`;
                speakText(item.jp);
            }
        }

        function skipTypingWord() {
            typingIdx++;
            loadTypingCard();
        }

        // Bắt phím Enter trong ô input gõ
        document.addEventListener('DOMContentLoaded', () => {
            const inp = document.getElementById('tpCardInput');
            if (inp) {
                inp.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        handleTypingSubmit();
                    }
                });
            }

            // Khởi tạo hiển thị dữ liệu
            renderVocab(VOCAB_DATA);
            renderKanji(KANJI_DATA);
            renderPart1();
            renderPart2();
            renderPart3();
            renderPart4();
            renderPart5();
            renderPart6();
            updateTotalScore();
        });
    </script>
    <script src="../assets/nav.js" defer></script>
</body>
</html>
"""

html_content = HTML_TEMPLATE.replace('__VOCAB_JSON__', vocab_json_str) \
                            .replace('__KANJI_JSON__', kanji_json_str) \
                            .replace('__P1_JSON__', p1_json_str) \
                            .replace('__P2_JSON__', p2_json_str) \
                            .replace('__P3_JSON__', p3_json_str) \
                            .replace('__P4_JSON__', p4_json_str) \
                            .replace('__P5_JSON__', p5_json_str) \
                            .replace('__P6_JSON__', p6_json_str)

output_path = os.path.join(WORKSPACE, 'tests/On_Tap_Mini_Test_A2_15_18.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated {output_path} (size: {len(html_content)} chars)")
