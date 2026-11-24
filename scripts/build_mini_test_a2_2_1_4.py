#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_mini_test_a2_2_1_4.py
Tạo trang web chuyên đề Ôn Tập Mini Test Bài 1 - 4 (Marugoto A2-2):
- Tab 1: 📖 Lý Thuyết Toàn Diện 4 Bài (Bài 1 ➔ 4)
- Tab 2: 🎴 81 Từ Vựng Chuẩn Kèm Nút Copy Quizlet Sạch & Ẩn Nghĩa (Bài 1 - 4)
- Tab 3: ⛩️ 49 Chữ Hán Kanji (Từ ghép, Nghĩa, Hán Việt, Mẹo nhớ & Copy Quizlet)
- Tab 4: 🎯 ĐỀ THI THỬ ĐA DẠNG NĂNG LỰC (6 Dạng Bài • 32 Câu Chuẩn Sư Phạm 100 Điểm):
    + PHẦN I: Trắc Nghiệm Tổng Hợp Ngữ Pháp & Trợ Từ (10 Câu - 25 Điểm)
    + PHẦN II: Sắp Xếp Từ Thành Câu Hoàn Chỉnh ★ (5 Câu - 15 Điểm)
    + PHẦN III: Chia Dạng Đúng Của Từ Trong Ngoặc (5 Câu - 15 Điểm)
    + PHẦN IV: Nối Cột Tình Huống & Phản Xạ Đời Sống (4 Câu - 10 Điểm)
    + PHẦN V: Đọc Hiểu Đoạn Văn Thực Tế (4 Câu / 2 Bài Đọc - 20 Điểm)
    + PHẦN VI: Luyện Dịch Câu Thực Chiến 2 Chiều (4 Câu - 15 Điểm)
- Tab 5: ⚡ Cẩm Nang Bỏ Túi (Cheat Sheet Tránh Bẫy Sư Phạm)
"""

import json
import os
import re

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 1. Load Official Vocab for Lessons 1 - 4
with open(os.path.join(WORKSPACE, 'data/vocab_a2_2_official.json'), 'r', encoding='utf-8') as f:
    vocab_raw_dict = json.load(f)

vocab_a2_2_1_4 = []
for l_key, l_label, l_num in [
    ('lesson_1', 'Bài 1', 'L1'),
    ('lesson_2', 'Bài 2', 'L2'),
    ('lesson_3', 'Bài 3', 'L3'),
    ('lesson_4', 'Bài 4', 'L4')
]:
    for item in vocab_raw_dict.get(l_key, []):
        vocab_a2_2_1_4.append({
            'l': l_num,
            'lessonName': l_label,
            'jp': item.get('jp', ''),
            'kanji': item.get('kanji', ''),
            'kana': item.get('kana', ''),
            'romaji': item.get('romaji', ''),
            'vi': item.get('vi', ''),
            'icon': item.get('icon', '📝')
        })

# 2. Load Official Kanji for Lessons 1 - 4
with open(os.path.join(WORKSPACE, 'data/kanji_vocab_a2_2.json'), 'r', encoding='utf-8') as f:
    kanji_raw_dict = json.load(f)

# Sino-Vietnamese (Hán Việt) and Mnemonics Map for the 49 Kanji Compounds
KANJI_META = {
    # Lesson 1
    '自己紹介': {'hv': 'TỰ KỶ THIỆU GIỚI', 'strokes': 26, 'formula': '自 (Tự thân) ＋ 己 (Bản thân) ＋ 紹 (Giới thiệu) ＋ 介 (Ở giữa)', 'mnemonic': 'Tự bản thân (自己) đứng ra giới thiệu (紹介) kết nối với mọi người.'},
    '名前': {'hv': 'DANH TIỀN', 'strokes': 15, 'formula': '名 (Tịch 夕 + Khẩu 口) ＋ 前 (Tiền)', 'mnemonic': 'Tối đến (夕) cất tiếng gọi (口) tên (名) người đi ở phía trước (前).'},
    '意味': {'hv': 'Ý VỊ', 'strokes': 21, 'formula': '意 (Âm 音 + Tâm 心) ＋ 味 (Khẩu 口 + Mùi 未)', 'mnemonic': 'Ý nghĩ phát ra từ trái tim (意) có phong vị, hương sắc riêng (味).'},
    '本屋': {'hv': 'BẢN ỐC', 'strokes': 14, 'formula': '本 (Gốc rễ, sách) ＋ 屋 (Nhà, mái nhà)', 'mnemonic': 'Mái nhà (屋) chuyên chứa đựng các pho sách quý (本) chính là hiệu sách.'},
    '近く': {'hv': 'CẬN', 'strokes': 7, 'formula': '斤 (Cái rìu) ＋ 辶 (Bước đi)', 'mnemonic': 'Vác rìu (斤) bước đi (辶) một đoạn ngắn là đến nơi rất gần (近く).'},
    '住みます': {'hv': 'TRÚ', 'strokes': 7, 'formula': '亻 (Nhân đứng) ＋ 主 (Chủ nhân)', 'mnemonic': 'Con người (亻) làm chủ (主) một mảnh đất để sinh sống định cư (住).'},
    '働きます': {'hv': 'ĐỘNG', 'strokes': 13, 'formula': '亻 (Nhân đứng) ＋ 動 (Chuyển động)', 'mnemonic': 'Con người (亻) không ngừng vận động, làm việc siêng năng (働).'},
    '～番目（１番目）': {'hv': 'PHIÊN MỤC', 'strokes': 17, 'formula': '番 (Thứ tự) ＋ 目 (Mắt, số thứ tự)', 'mnemonic': 'Đôi mắt (目) chăm chú theo dõi từng số thứ tự (番) được xướng tên.'},

    # Lesson 2
    '兄': {'hv': 'HUYNH', 'strokes': 5, 'formula': '口 (Miệng) ＋ 儿 (Chân người)', 'mnemonic': 'Người anh cả trong nhà có tiếng nói lớn (口) chỉ bảo các em (儿).'},
    'お兄さん': {'hv': 'HUYNH', 'strokes': 5, 'formula': 'お ＋ 兄 ＋ さん', 'mnemonic': 'Cách gọi anh trai của người khác hoặc xưng hô kính trọng với anh trai.'},
    '姉': {'hv': 'TỶ', 'strokes': 8, 'formula': '女 (Phụ nữ) ＋ 市 (Chợ)', 'mnemonic': 'Người phụ nữ (女) đảm đang thường ra chợ (市) mua đồ cho cả nhà là chị gái.'},
    'お姉さん': {'hv': 'TỶ', 'strokes': 8, 'formula': 'お ＋ 姉 ＋ さん', 'mnemonic': 'Cách gọi chị gái của người khác một cách lịch sự, kính cẩn.'},
    '弟': {'hv': 'ĐỆ', 'strokes': 7, 'formula': 'Tượng hình sợi dây quấn quanh cọc tre', 'mnemonic': 'Người em trai nhỏ tuổi luôn được gia đình bảo bọc, gắn kết chặt chẽ.'},
    '妹': {'hv': 'MUỘI', 'strokes': 8, 'formula': '女 (Phụ nữ) ＋ 未 (Chưa đến)', 'mnemonic': 'Người con gái (女) còn nhỏ tuổi, tương lai chưa tới (未) là em gái.'},
    '家族': {'hv': 'GIA TỘC', 'strokes': 21, 'formula': '家 (Mái nhà 宀 + Lợn 豕) ＋ 族 (Cờ 方 + Mũi tên 矢)', 'mnemonic': 'Dưới cùng một mái nhà (家), các thành viên đoàn kết như một đạo quân (族).'},
    '長い': {'hv': 'TRƯỜNG', 'strokes': 8, 'formula': 'Hình ảnh mái tóc dài của vị trưởng lão', 'mnemonic': 'Mái tóc dài buông xõa biểu trưng cho thời gian dài lâu, trường thọ.'},
    '短い': {'hv': 'ĐOẢN', 'strokes': 12, 'formula': '矢 (Mũi tên) ＋ 豆 (Hạt đậu)', 'mnemonic': 'Mũi tên (矢) ngắn chỉ bằng độ dài của những hạt đậu (豆) xếp lại.'},
    '低い': {'hv': 'ĐÊ', 'strokes': 7, 'formula': '亻 (Người) ＋ 氐 (Chân đế, gốc)', 'mnemonic': 'Người (亻) cúi mình xuống tận gốc rễ (氐) diễn tả vị trí thấp bé.'},
    '上手': {'hv': 'THƯỢNG THỦ', 'strokes': 7, 'formula': '上 (Ở trên) ＋ 手 (Bàn tay)', 'mnemonic': 'Bàn tay (手) luôn giơ lên vị trí dẫn đầu (上) biểu thị sự giỏi giang, thành thạo.'},
    '歌': {'hv': 'CA', 'strokes': 14, 'formula': '哥 (Khả ＋ Khả) ＋ 欠 (Há miệng)', 'mnemonic': 'Há to miệng (欠) ngân nga từng câu hát du dương (歌).'},
    '歌います': {'hv': 'CA', 'strokes': 14, 'formula': '歌 (Bài hát) ＋ います', 'mnemonic': 'Động từ ca hát, ngân nga giai điệu âm nhạc.'},

    # Lesson 3
    'お客さん': {'hv': 'KHÁCH', 'strokes': 9, 'formula': 'お ＋ 客 (Mái nhà 宀 + Mỗi 各) ＋ さん', 'mnemonic': 'Mỗi người (各) bước vào dưới mái nhà (宀) đều là vị khách quý (客).'},
    '注文': {'hv': 'CHÚ VĂN', 'strokes': 12, 'formula': '注 (Thủy 氵+ Chủ 主) ＋ 文 (Chữ nghĩa)', 'mnemonic': 'Rót hết tâm tư (注) vào từng câu chữ (文) khi đặt hàng, gọi món.'},
    '注意': {'hv': 'CHÚ Ý', 'strokes': 16, 'formula': '注 (Rót vào) ＋ 意 (Ý nghĩ, tâm trí)', 'mnemonic': 'Rót toàn bộ sự chú ý (注) và tâm trí (意) vào việc đang làm.'},
    '洋食': {'hv': 'DƯƠNG THỰC', 'strokes': 18, 'formula': '洋 (Đại dương, phương Tây) ＋ 食 (Ăn uống)', 'mnemonic': 'Món ăn (食) bắt nguồn từ bên kia đại dương phương Tây (洋).'},
    '洋服': {'hv': 'DƯƠNG PHỤC', 'strokes': 17, 'formula': '洋 (Phương Tây) ＋ 服 (Quần áo)', 'mnemonic': 'Trang phục, quần áo (服) theo phong cách hiện đại phương Tây (洋).'},
    '和食': {'hv': 'HÒA THỰC', 'strokes': 17, 'formula': '和 (Hòa hợp, Nhật Bản) ＋ 食 (Ẩm thực)', 'mnemonic': 'Ẩm thực truyền thống Nhật Bản (和食) tinh tế và hòa hợp với thiên nhiên.'},
    '和服': {'hv': 'HÒA PHỤC', 'strokes': 16, 'formula': '和 (Nhật Bản) ＋ 服 (Trang phục)', 'mnemonic': 'Trang phục truyền thống Nhật Bản (như Kimono, Yukata).'},
    '和室': {'hv': 'HÒA THẤT', 'strokes': 17, 'formula': '和 (Nhật Bản) ＋ 室 (Căn phòng)', 'mnemonic': 'Căn phòng trải chiếu Tatami mang phong cách kiến trúc Nhật Bản.'},
    '方': {'hv': 'PHƯƠNG', 'strokes': 4, 'formula': 'Bộ Phương (Phương hướng, cách thức)', 'mnemonic': 'Vị khách quý hoặc cách thức làm một việc gì đó (〜方).'},
    '地方': {'hv': 'ĐỊA PHƯƠNG', 'strokes': 10, 'formula': '地 (Đất đai) ＋ 方 (Phương hướng)', 'mnemonic': 'Các vùng miền, khu vực địa phương trên khắp đất nước.'},
    '方法': {'hv': 'PHƯƠNG PHÁP', 'strokes': 12, 'formula': '方 (Phương thức) ＋ 法 (Pháp luật, quy tắc)', 'mnemonic': 'Quy tắc và phương pháp (方法) đúng đắn để giải quyết công việc.'},
    '有名': {'hv': 'HỮU DANH', 'strokes': 12, 'formula': '有 (Có) ＋ 名 (Tên tuổi)', 'mnemonic': 'Có (有) tên tuổi (名) lẫy lừng được thiên hạ biết đến là nổi tiếng.'},
    '有料': {'hv': 'HỮU LIỆU', 'strokes': 16, 'formula': '有 (Có) ＋ 料 (Phí tổn, tiền)', 'mnemonic': 'Dịch vụ có tính phí, phải trả tiền (有料) mới được sử dụng.'},
    '牛肉': {'hv': 'NGƯU NHỤC', 'strokes': 10, 'formula': '牛 (Con bò) ＋ 肉 (Thịt)', 'mnemonic': 'Thịt (肉) của con bò (牛) - nguyên liệu quen thuộc trong ẩm thực.'},
    '牛乳': {'hv': 'NGƯU NHŨ', 'strokes': 12, 'formula': '牛 (Con bò) ＋ 乳 (Sữa mẹ, vú)', 'mnemonic': 'Dòng sữa tươi mát (乳) lấy từ con bò cái (牛).'},
    '冷たい': {'hv': 'LÃNH', 'strokes': 7, 'formula': '冫 (Băng giá) ＋ 令 (Hiệu lệnh)', 'mnemonic': 'Những giọt nước đóng băng (冫) lạnh buốt khi chạm vào.'},
    '冷える': {'hv': 'LÃNH', 'strokes': 7, 'formula': '冷 (Lạnh) ＋ える', 'mnemonic': 'Tự bản thân thời tiết hoặc đồ vật nguội đi, lạnh cóng.'},
    '冷やす': {'hv': 'LÃNH', 'strokes': 7, 'formula': '冷 (Lạnh) ＋ やす', 'mnemonic': 'Hành động chủ động làm lạnh đồ ăn, thức uống (bỏ vào tủ lạnh).'},

    # Lesson 4
    'ご飯': {'hv': 'PHẠN', 'strokes': 12, 'formula': 'ご ＋ 飯 (Thực 食 + Phản 反)', 'mnemonic': 'Bữa cơm (飯) thơm ngon luôn là nguồn năng lượng mỗi ngày.'},
    '塩': {'hv': 'DIÊM', 'strokes': 13, 'formula': '土 (Đất) ＋ 鹵 (Muối mỏ) ＋ 皿 (Cái đĩa)', 'mnemonic': 'Những hạt muối trắng (塩) khai thác từ biển được bày trên đĩa.'},
    '全て': {'hv': 'TOÀN', 'strokes': 6, 'formula': '全 (Toàn bộ) ＋ て', 'mnemonic': 'Dưới một mái vương (王), gom góp toàn bộ tất cả mọi thứ.'},
    '全然': {'hv': 'TOÀN NHIÊN', 'strokes': 18, 'formula': '全 (Toàn bộ) ＋ 然 (Tự nhiên, vậy)', 'mnemonic': 'Hoàn toàn, tuyệt nhiên (thường đi với thể phủ định).'},
    '全部': {'hv': 'TOÀN BỘ', 'strokes': 17, 'formula': '全 (Toàn bộ) ＋ 部 (Bộ phận)', 'mnemonic': 'Gom góp tất cả các bộ phận lại thành một chỉnh thể toàn bộ.'},
    '安全': {'hv': 'AN TOÀN', 'strokes': 12, 'formula': '安 (An bình) ＋ 全 (Toàn vẹn)', 'mnemonic': 'Mọi việc yên ổn (安) và toàn vẹn (全) không gặp nguy hiểm.'},
    '熱い': {'hv': 'NHIỆT', 'strokes': 15, 'formula': '埶 (Trồng trọt) ＋ 灬 (Lửa nóng)', 'mnemonic': 'Ngọn lửa đỏ rực phía dưới (灬) tỏa ra hơi nóng bừng bừng.'},
    '苦い': {'hv': 'KHỔ', 'strokes': 8, 'formula': '艹 (Cỏ cây) ＋ 古 (Cũ kỹ)', 'mnemonic': 'Cây cỏ dại (艹) lâu năm (古) thường có vị đắng ngắt.'},
    '苦しい': {'hv': 'KHỔ', 'strokes': 8, 'formula': '苦 (Đắng cay) ＋ しい', 'mnemonic': 'Cảm giác đau đớn, khó thở hoặc khốn khổ trong cuộc sống.'},
    '苦手': {'hv': 'KHỔ THỦ', 'strokes': 12, 'formula': '苦 (Đau khổ) ＋ 手 (Bàn tay)', 'mnemonic': 'Bàn tay (手) thấy khổ sở (苦) khi phải làm việc mình yếu kém, không giỏi.'}
}

kanji_a2_2_1_4 = []
for l_key, l_label, l_num in [
    ('lesson_1', 'Bài 1', 'L1'),
    ('lesson_2', 'Bài 2', 'L2'),
    ('lesson_3', 'Bài 3', 'L3'),
    ('lesson_4', 'Bài 4', 'L4')
]:
    for item in kanji_raw_dict.get(l_key, []):
        w = item.get('word', '')
        meta = KANJI_META.get(w, {
            'hv': 'HÁN TỰ',
            'strokes': 8,
            'formula': 'Từ vựng chữ Hán Marugoto A2.2',
            'mnemonic': 'Ghi nhớ cách đọc và ý nghĩa của từ ghép trong bài.'
        })
        kanji_a2_2_1_4.append({
            'char': w,
            'word': w,
            'kana': item.get('kana', ''),
            'hiragana': item.get('kana', ''),
            'meaning': item.get('mean', ''),
            'shortMeaning': item.get('mean', '').split(',')[0].strip(),
            'hv': meta['hv'],
            'lesson': l_num,
            'lessonName': l_label,
            'strokes': meta['strokes'],
            'formula': meta['formula'],
            'mnemonic': meta['mnemonic'],
            'kun': item.get('kana', ''),
            'on': '—',
            'examples': [
                {'word': w, 'reading': item.get('kana', ''), 'vi': item.get('mean', '')}
            ]
        })

# 3. Data for Part I: Multiple Choice (10 Questions - 25 pts)
PART1_MC = [
    {
        "id": 1,
        "category": "Bài 1 • N という意味",
        "q": "「無料」は どういう 意味ですか。ー お金が かからない [____] 意味です。",
        "options": ["と いう", "の", "に", "で"],
        "correct": 0,
        "explain": "Cấu trúc giải thích ý nghĩa của từ hoặc cách nói: 「[Mệnh đề / Từ ngữ] ＋ という 意味です」 (Có ý nghĩa là...)."
    },
    {
        "id": 2,
        "category": "Bài 1 • N1 という N2",
        "q": "駅の 近くに「さくら」[____] レストランが あります。あそこで 食べましょう。",
        "options": ["という", "と", "の", "に"],
        "correct": 0,
        "explain": "Cấu trúc giới thiệu tên gọi cụ thể của một địa điểm/vật: 「N1 ＋ という ＋ N2」 (Có một nhà hàng tên là Sakura)."
    },
    {
        "id": 3,
        "category": "Bài 1 • Mệnh đề bổ nghĩa N (Động từ)",
        "q": "これは わたしが 先週 デパートで [____] 靴です。とても 軽いです。",
        "options": ["買った", "買います", "買って", "買いたい"],
        "correct": 0,
        "explain": "Mệnh đề bổ nghĩa cho danh từ trong quá khứ bắt buộc dùng thể Ta: 「先週買った靴」 (Đôi giày đã mua tuần trước)."
    },
    {
        "id": 4,
        "category": "Bài 1 • Mệnh đề bổ nghĩa N (Tính từ な)",
        "q": "京都には [____] お寺や 神社が たくさん あります。",
        "options": ["有名な", "有名だ", "有名", "有名で"],
        "correct": 0,
        "explain": "Tính từ đuôi な khi đứng trước bổ nghĩa cho danh từ bắt buộc phải giữ chữ 「な」: 「有名なお寺」 (Ngôi chùa nổi tiếng). Tuyệt đối cấm dùng 有名だ ❌."
    },
    {
        "id": 5,
        "category": "Bài 2 • Nhận diện người (Vている + N)",
        "q": "あそこで 青い シャツを [____] 人は わたしの 兄です。",
        "options": ["着ている", "着る", "着た", "着て"],
        "correct": 0,
        "explain": "Miêu tả trạng thái trang phục đang mặc để nhận diện người dùng 「V-ている ＋ 人」: 「青いシャツを着ている人」 (Người đang mặc chiếc áo màu xanh)."
    },
    {
        "id": 6,
        "category": "Bài 2 • Phán đoán diện mạo そう",
        "q": "この 料理は とても [____] そうですね。一口 食べてみても いいですか。",
        "options": ["から", "からい", "からくて", "からかった"],
        "correct": 0,
        "explain": "Tính từ đuôi い phán đoán vẻ ngoài qua thị giác: Bỏ đuôi 「い」 ＋ 「そう」 (からい ➔ からそう: trông có vẻ cay)."
    },
    {
        "id": 7,
        "category": "Bài 2 • Trạng từ hóa tính từ",
        "q": "もうすぐ 夏休みに なるので、髪を [____] 切りました。",
        "options": ["短く", "短い", "短いに", "短くて"],
        "correct": 0,
        "explain": "Biến tính từ đuôi い thành phó từ bổ nghĩa cho động từ: Bỏ đuôi 「い」 thay bằng 「く」 ＋ V (短く切る: cắt ngắn)."
    },
    {
        "id": 8,
        "category": "Bài 3 • Nguyên nhân mềm mại 〜ので",
        "q": "あしたは 試験が [____] ので、今夜は 早く 家へ 帰って 勉強します。",
        "options": ["ある", "あります", "あって", "あった"],
        "correct": 0,
        "explain": "Đứng trước 「〜ので」 là thể thông thường (普通形). Động từ thể từ điển: 「あるので」 (Vì ngày mai có bài thi...)."
    },
    {
        "id": 9,
        "category": "Bài 3 • Danh từ hóa 〜のは & Gợi ý 〜なら",
        "q": "A: 「わたしが いちばん 好きな [____] 和食です。」ー B: 「和食 [____]、この すし屋が いいですよ。」",
        "options": ["のは ／ なら", "ことは ／ なら", "のは ／ から", "ものは ／ ので"],
        "correct": 0,
        "explain": "Cấu trúc danh từ hóa mệnh đề: 「普通形 ＋ のは 〜 です」 và đưa ra gợi ý theo chủ đề: 「N ＋ なら」 (Nếu là món Nhật thì quán sushi này tuyệt lắm)."
    },
    {
        "id": 10,
        "category": "Bài 4 • Cấm đoán quy định",
        "q": "ここは 禁煙ですから、たばこを [____]。外で 吸ってください。",
        "options": ["吸っては いけません", "吸っても いいです", "吸わないで ください", "吸います"],
        "correct": 0,
        "explain": "Nêu quy định cấm đoán tuyệt đối ở nơi công cộng: 「V-ては いけません」 (Không được phép hút thuốc / cấm hút thuốc)."
    }
]

# 4. Data for Part II: Sentence Ordering (5 Questions - 15 pts)
PART2_ARRANGE = [
    {
        "id": 11,
        "category": "Bài 1 • Bổ nghĩa danh từ",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "昨日",
        "post": "忘れました。",
        "chips": ["料理の", "名前を", "レストランで", "食べた"],
        "correctOrder": [2, 3, 0, 1], # レストランで (2) -> 食べた (3) -> ★ 料理の (0) -> 名前を (1)
        "starIndex": 2, # 3rd position (0-based: 2) -> "料理の" (chip 0)
        "starChip": "料理の",
        "fullSentence": "昨日 レストランで 食べた 料理の 名前を 忘れました。",
        "explain": "Mệnh đề bổ nghĩa cho danh từ: 昨日 [レストランで] [食べた] [★ 料理の] [名前を] 忘れました. Vị trí ngôi sao là [料理の]."
    },
    {
        "id": 12,
        "category": "Bài 2 • Phán đoán diện mạo 〜そうな + N",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "あそこで",
        "post": "山田さんです。",
        "chips": ["笑っている", "やさしそうな", "人は", "楽しそうに"],
        "correctOrder": [3, 0, 1, 2], # 楽しそうに (3) -> 笑っている (0) -> ★ やさしそうな (1) -> 人は (2)
        "starIndex": 2,
        "starChip": "やさしそうな",
        "fullSentence": "あそこで 楽しそうに 笑っている やさしそうな 人は 山田さんです。",
        "explain": "Thứ tự từ: あそこで [楽しそうに] [笑っている] [★ やさしそうな] [人は] 山田さんです. Vị trí ngôi sao là [やさしそうな]."
    },
    {
        "id": 13,
        "category": "Bài 2 • Trạng từ hóa tính từ",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "大事な メモですから、",
        "post": "書いてください。",
        "chips": ["もっと", "きれいに", "字を", "ノートに"],
        "correctOrder": [3, 0, 1, 2], # ノートに (3) -> もっと (0) -> ★ きれいに (1) -> 字を (2)
        "starIndex": 2,
        "starChip": "きれいに",
        "fullSentence": "大事な メモですから、ノートに もっと きれいに 字を 書いてください。",
        "explain": "Trạng từ của tính từ な: きれいに + V. Thứ tự: [ノートに] [もっと] [★ きれいに] [字を] 書いてください. Vị trí ngôi sao là [きれいに]."
    },
    {
        "id": 14,
        "category": "Bài 3 • Danh từ hóa 〜のは 〜です",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "わたしが",
        "post": "母が 作った 料理です。",
        "chips": ["いちばん", "好きな", "のは", "日本の 食べ物で"],
        "correctOrder": [3, 0, 1, 2], # 日本の 食べ物で (3) -> いちばん (0) -> ★ 好きな (1) -> のは (2)
        "starIndex": 2,
        "starChip": "好きな",
        "fullSentence": "わたしが 日本の 食べ物で いちばん 好きな のは 母が 作った 料理です。",
        "explain": "Danh từ hóa mệnh đề: [日本の 食べ物で] [いちばん] [★ 好きな] [のは] 母が 作った 料理です. Vị trí ngôi sao là [好きな]."
    },
    {
        "id": 15,
        "category": "Bài 4 • Không làm V1 〜ないで",
        "prompt": "Sắp xếp các từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
        "pre": "この 料理は",
        "post": "食べてください。",
        "chips": ["しょうゆを", "つけないで", "塩だけ", "かけて"],
        "correctOrder": [0, 1, 2, 3], # しょうゆを (0) -> つけないで (1) -> ★ 塩だけ (2) -> かけて (3)
        "starIndex": 2,
        "starChip": "塩だけ",
        "fullSentence": "この 料理は しょうゆを つけないで 塩だけ かけて 食べてください。",
        "explain": "Làm V2 mà không làm V1: [しょうゆを] [つけないで] [★ 塩だけ] [かけて] 食べてください. Vị trí ngôi sao là [塩だけ]."
    }
]

# 5. Data for Part III: Conjugation (5 Questions - 15 pts)
PART3_CONJUGATE = [
    {
        "id": 16,
        "category": "Bài 1 • Bổ nghĩa danh từ quá khứ",
        "sentence": "これは きのう 本屋で (買う) [_______] 雑誌です。",
        "baseWord": "買う (かう)",
        "accepted": ["買った", "かった", "katta"],
        "displayAnswer": "買った (かった)",
        "explain": "Mệnh đề bổ nghĩa cho danh từ trong quá khứ bắt buộc chia thể Ta: 買う ➔ <strong>買った</strong> (quy tắc thể Ta: う、つ、る ➔ った)."
    },
    {
        "id": 17,
        "category": "Bài 2 • Phán đoán diện mạo 〜そう",
        "sentence": "この ケーキは とても (甘い) [_______] そうですね。一つ ください。",
        "baseWord": "甘い (あまい)",
        "accepted": ["甘", "あま", "ama"],
        "displayAnswer": "甘 (あま)",
        "explain": "Tính từ đuôi い phán đoán vẻ ngoài bỏ đuôi 「い」 trước そう: 甘い ➔ <strong>甘</strong>そう (trông có vẻ ngọt)."
    },
    {
        "id": 18,
        "category": "Bài 2 • Trạng từ hóa tính từ đuôi い",
        "sentence": "髪が 長くなったので、(短い) [_______] 切ってもらいました。",
        "baseWord": "短い (みじかい)",
        "accepted": ["短く", "みじかく", "mijikaku"],
        "displayAnswer": "短く (みじかく)",
        "explain": "Biến tính từ đuôi い thành phó từ bổ nghĩa cho động từ: Bỏ đuôi 「い」 thay bằng 「く」 ➔ <strong>短く</strong>切る (cắt ngắn)."
    },
    {
        "id": 19,
        "category": "Bài 3 • Nguyên nhân với tính từ đuôi な + ので",
        "sentence": "きょうは とても (暇) [_______] ので、映画を 見に 行きませんか。",
        "baseWord": "暇 (ひま)",
        "accepted": ["暇な", "ひまな", "himana"],
        "displayAnswer": "暇な (ひまな)",
        "explain": "Trước 「〜ので」, tính từ đuôi な và danh từ phải đi kèm 「な」: 暇 ➔ <strong>暇な</strong>ので. Tuyệt đối không dùng 暇だので ❌."
    },
    {
        "id": 20,
        "category": "Bài 4 • Trình tự sau khi làm xong 〜てから",
        "sentence": "手を きれいに (洗う) [_______] から、みんなで 一緒に ご飯を 食べましょう。",
        "baseWord": "洗う (あらう)",
        "accepted": ["洗って", "あらって", "aratte"],
        "displayAnswer": "洗って (あらって)",
        "explain": "Cấu trúc trình tự hành động: Sau khi làm xong V1 thì làm V2: 「V-て ＋ から」. 洗う ➔ <strong>洗って</strong>から."
    }
]

# 6. Data for Part IV: Situation Matching (4 Questions - 10 pts)
PART4_MATCH = [
    {
        "id": 21,
        "category": "Bài 1 • Hỏi ý nghĩa từ vựng",
        "situation": "A: 「すみません、『お勘定（おかんじょう）』はどういう意味ですか。」",
        "context": "(Khách nước ngoài đi ăn nhà hàng hỏi ý nghĩa từ vựng tiếng Nhật)",
        "options": [
            "「『お会計・お金を払うこと』という意味ですよ。」",
            "「めがねを かけて、青い シャツを 着ている 田中さんですよ。」",
            "「魚なら、本日のおすすめの 刺身が 新鮮で 一番ですよ。」",
            "「たれを つけないで、そのまま 塩を 少し かけて 食べてください。」"
        ],
        "correct": 0,
        "explain": "Đáp lại câu hỏi ý nghĩa 「〜はどういう意味ですか」 bằng cấu trúc giải thích: 「『...』という意味ですよ。」"
    },
    {
        "id": 22,
        "category": "Bài 2 • Nhận diện bạn bè trong tiệc",
        "situation": "A: 「あのう、あそこで 楽しそうに 話している 男の人は 誰ですか。」",
        "context": "(Hỏi nhận diện một người đang nói chuyện trong buổi tiệc gia đình)",
        "options": [
            "「『お会計・お金を払うこと』という意味ですよ。」",
            "「めがねを かけて、青い シャツを 着ている 田中さんですよ。」",
            "「魚なら、本日のおすすめの 刺身が 新鮮で 一番ですよ。」",
            "「たれを つけないで、そのまま 塩を 少し かけて 食べてください。」"
        ],
        "correct": 1,
        "explain": "Nhận diện người qua đặc điểm ngoại hình và trang phục: 「めがねをかけて、青いシャツを着ている田中さんですよ。」"
    },
    {
        "id": 23,
        "category": "Bài 3 • Hỏi xin gợi ý món ăn",
        "situation": "A: 「すみません、この 店の おすすめの 料理は 何ですか。」",
        "context": "(Khách nhờ nhân viên quán tư vấn món ăn ngon)",
        "options": [
            "「『お会計・お金を払うこと』という意味ですよ。」",
            "「めがねを かけて、青い シャツを 着ている 田中さんですよ。」",
            "「魚なら、本日のおすすめの 刺身が 新鮮で 一番ですよ。」",
            "「たれを つけないで、そのまま 塩を 少し かけて 食べてください。」"
        ],
        "correct": 2,
        "explain": "Đưa ra đề xuất gợi ý theo chủ đề người nghe quan tâm dùng 「N ＋ なら」: 「魚なら、...刺身が一番ですよ。」"
    },
    {
        "id": 24,
        "category": "Bài 4 • Hỏi cách thưởng thức món ăn",
        "situation": "A: 「この 料理は 初めて なんですが、どうやって 食べますか。」",
        "context": "(Lần đầu ăn món Nhật, hỏi người bản xứ hướng dẫn cách ăn đúng điệu)",
        "options": [
            "「『お会計・お金を払うこと』という意味ですよ。」",
            "「めがねを かけて、青い シャツを 着ている 田中さんですよ。」",
            "「魚なら、本日のおすすめの 刺身が 新鮮で 一番ですよ。」",
            "「たれを つけないで、そのまま 塩を 少し かけて 食べてください。」"
        ],
        "correct": 3,
        "explain": "Hướng dẫn cách ăn không chấm nước sốt mà rắc chút muối: 「たれをつけないで、そのまま塩を少し...」 (Cấu trúc Vないで)."
    }
]

# 7. Data for Part V: Reading Comprehension (4 Questions / 2 Passages - 20 pts)
PART5_READING = [
    {
        "passageId": 1,
        "title": "BÀI ĐỌC 1: 国際交流パーティーでの 出会い (Cuộc Gặp Gỡ Tại Bữa Tiệc Giao Lưu Quốc Tế - Bài 1 & 2)",
        "text": "先週の日曜日、わたしは 市民センターで 開かれた 国際交流パーティーに 参加しました。会場には いろいろな 国から 来た 人たちが たくさん いました。<br>会場で、めがねを かけて、青い シャツを 着ている 男の人に 会いました。「鈴木」という 名前で、大学で 日本語を 教えている 先生でした。鈴木先生は いつも にこにこしていて、とても やさしそうな 人でした。<br>鈴木先生が 好きなのは、ベトナム料理だそうです。特に 「フォー」という 料理が 大好きで、ベトナムにも 3回 行った ことが あると 言っていました。わたしは 先生と 連絡先を 交換して、来週 ベトナム料理の 店へ 一緒に 行く 約束を しました。",
        "questions": [
            {
                "id": 25,
                "q": "鈴木先生は どんな 人ですか。",
                "options": [
                    "めがねを かけて、青い シャツを 着ている やさしそうな 人",
                    "背が 高くて、黒い スーツを 着ている 厳しい 人",
                    "料理が 苦手で、あまり 話さない 人",
                    "ベトナムへ 一度も 行った ことが ない 人"
                ],
                "correct": 0,
                "explain": "Trong bài viết nêu rõ: 「めがねをかけて、青いシャツを着ている男の人...とてもやさしそうな人でした」."
            },
            {
                "id": 26,
                "q": "鈴木先生と わたしは 来週 何を しますか。",
                "options": [
                    "市民センターで 国際交流パーティーを 開きます",
                    "一緒に ベトナム料理の 店へ 行きます",
                    "大学で 日本語の 試験を 受けます",
                    "ベトナムへ 飛行機で 旅行に 行きます"
                ],
                "correct": 1,
                "explain": "Trong bài viết: 「来週 ベトナム料理の 店へ 一緒に 行く 約束を しました」."
            }
        ]
    },
    {
        "passageId": 2,
        "title": "BÀI ĐỌC 2: 日本料理屋「さくら」の おすすめと ルール (Món Ngon Và Quy Tắc Tại Nhà Hàng Sakura - Bài 3 & 4)",
        "text": "駅の 近くに「さくら」という 有名な 日本料理の 店が あります。店に入ると、まず 手を 洗ってから、席に 案内されます。<br>この店の おすすめは 天ぷらと 刺身です。刺身なら、毎朝 港から 届く 新鮮な 魚が 一番です。天ぷらを 食べるときは、つゆを つけないで、特別な 塩を 少し つけると、サクサクして とても おいしいです。<br>店の中には いくつか ルールが あります。他のお客さんの 迷惑に なりますから、大声で 話しては いけません。また、全席 禁煙ですので、店内で たばこを 吸ってはいけません。静かに おいしい 和食を 楽しむことが できます。",
        "questions": [
            {
                "id": 27,
                "q": "「さくら」で 天ぷらを 食べるとき、どうやって 食べると おいしいですか。",
                "options": [
                    "つゆを たくさん つけて 食べます",
                    "つゆを つけないで、特別な 塩を 少し つけて 食べます",
                    "マヨネーズを かけて 食べます",
                    "箸を 使わないで、手で そのまま 食べます"
                ],
                "correct": 1,
                "explain": "Trong bài viết ghi rõ: 「天ぷらを 食べるときは、つゆを つけないで、特別な 塩を 少し つけると、サクサクして とても おいしいです」."
            },
            {
                "id": 28,
                "q": "店の中の ルールについて、正しいものは どれですか。",
                "options": [
                    "店の中で 写真を 撮っては いけません",
                    "手を 洗わないで 席に 座らなければ なりません",
                    "たばこを 吸ったり、大声で 話したり しては いけません",
                    "席で たばこを 吸っても いいです"
                ],
                "correct": 2,
                "explain": "Bài viết nêu 2 quy định cấm: 「大声で話してはいけません」 và 「店内でたばこを吸ってはいけません」."
            }
        ]
    }
]

# 8. Data for Part VI: Sentence Translation (4 Questions - 15 pts)
PART6_TRANSLATION = [
    {
        "id": 29,
        "category": "Bài 1 • Bổ nghĩa danh từ",
        "vi": "Người đang nói chuyện với thầy giáo ở đằng kia là anh Tanaka.",
        "hint": "あそこ (đằng kia), 先生 (thầy giáo), 話している (đang nói chuyện), 田中さん (anh Tanaka)",
        "modelSentence": "あそこで 先生と 話している 人は 田中さんです。",
        "modelKana": "あそこで せんせいと はなしている ひとは たなかさんです。",
        "keywords": ["先生", "話している", "人", "田中さん"],
        "breakdown": [
            {"part": "あそこで", "role": "Vị trí diễn ra hành động (ở đằng kia)"},
            {"part": "先生と 話している", "role": "Mệnh đề bổ nghĩa cho danh từ (đang nói chuyện với thầy giáo)"},
            {"part": "人は", "role": "Danh từ trung tâm (người)"},
            {"part": "田中さんです", "role": "Vị ngữ xác định danh tính (là anh Tanaka)"}
        ]
    },
    {
        "id": 30,
        "category": "Bài 2 • Trạng từ hóa & Phán đoán",
        "vi": "Đứa bé đang ăn chiếc bánh kem trông có vẻ rất ngon lành.",
        "hint": "子ども (đứa bé), ケーキ (bánh kem), おいしそうに (ngon lành - trạng từ), 食べています (đang ăn)",
        "modelSentence": "子どもが ケーキを おいしそうに 食べています。",
        "modelKana": "こどもが けーきを おいしそうに たべています。",
        "keywords": ["子ども", "ケーキ", "おいしそうに", "食べています"],
        "breakdown": [
            {"part": "子どもが", "role": "Chủ ngữ thực hiện hành động (đứa bé)"},
            {"part": "ケーキを", "role": "Tân ngữ hành động (chiếc bánh kem)"},
            {"part": "おいしそうに", "role": "Tính từ đuôi い làm trạng từ: おいしい ➔ おいしそう ➔ おいしそうに (một cách ngon lành)"},
            {"part": "食べています", "role": "Hành động đang tiếp diễn (đang ăn)"}
        ]
    },
    {
        "id": 31,
        "category": "Bài 3 • Danh từ hóa 〜のは 〜です",
        "vi": "Thứ mà tôi thích nhất trong các món ăn Nhật Bản là sushi.",
        "hint": "日本の 料理 (món ăn Nhật), いちばん (nhất), 好きなのは (thứ tôi thích là - danh từ hóa), すし (sushi)",
        "modelSentence": "日本の 料理の 中で、わたしが いちばん 好きなのは すしです。",
        "modelKana": "にほんの りょうりの なかで、わたしが いちばん すきなのは すしです。",
        "keywords": ["日本", "料理", "いちばん", "好き", "のは", "すし"],
        "breakdown": [
            {"part": "日本の 料理の 中で", "role": "Phạm vi so sánh (trong số các món ăn Nhật)"},
            {"part": "わたしが いちばん 好きなのは", "role": "Danh từ hóa mệnh đề bằng trợ từ の: điều tôi thích nhất là..."},
            {"part": "すしです", "role": "Danh từ đích (là sushi)"}
        ]
    },
    {
        "id": 32,
        "category": "Bài 4 • Trình tự Vてから",
        "vi": "Sau khi rửa tay sạch sẽ, hãy cùng nhau ăn cơm nhé.",
        "hint": "手 (tay), きれいに (sạch sẽ - trạng từ), 洗ってから (sau khi rửa), 一緒に (cùng nhau), ご飯 (cơm), 食べましょう (cùng ăn nhé)",
        "modelSentence": "手を きれいに 洗ってから、みんなで 一緒に ご飯を 食べましょう。",
        "modelKana": "てを きれいに あらってから、みんなで いっしょに ごはんを たべましょう。",
        "keywords": ["手", "きれいに", "洗ってから", "一緒に", "ご飯", "食べましょう"],
        "breakdown": [
            {"part": "手を きれいに 洗ってから", "role": "Trình tự hành động V1てから (sau khi rửa tay sạch sẽ - きれいに là trạng từ của tính từ な)"},
            {"part": "みんなで 一緒に", "role": "Phương thức cùng nhau thực hiện"},
            {"part": "ご飯を 食べましょう", "role": "Đề xuất rủ rê cùng làm gì (chúng ta cùng ăn cơm nhé)"}
        ]
    }
]

# Export JSON file for Mini Test A2.2 Lessons 1-4 Data
DATA_JS_CONTENT = f"""/* Canonical Structured Data for Marugoto A2.2 Lessons 1-4 Mini Test Companion */
window.MINI_A2_2_1_4_DATA = {{
    rawVocab: {json.dumps(vocab_a2_2_1_4, ensure_ascii=False, indent=2)},
    rawKanji: {json.dumps(kanji_a2_2_1_4, ensure_ascii=False, indent=2)},
    part1Data: {json.dumps(PART1_MC, ensure_ascii=False, indent=2)},
    part2Data: {json.dumps(PART2_ARRANGE, ensure_ascii=False, indent=2)},
    part3Data: {json.dumps(PART3_CONJUGATE, ensure_ascii=False, indent=2)},
    part4Data: {json.dumps(PART4_MATCH, ensure_ascii=False, indent=2)},
    part5Data: {json.dumps(PART5_READING, ensure_ascii=False, indent=2)},
    part6Data: {json.dumps(PART6_TRANSLATION, ensure_ascii=False, indent=2)}
}};
"""

data_js_path = os.path.join(WORKSPACE, 'assets/data/mini_a2_2_1_4_data.js')
with open(data_js_path, 'w', encoding='utf-8') as f:
    f.write(DATA_JS_CONTENT)
print(f"Generated {data_js_path} ({len(vocab_a2_2_1_4)} vocab, {len(kanji_a2_2_1_4)} kanji, 32 questions)")

# 9. Generate HTML Content
HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Cẩm Nang Toàn Diện & Đề Thi Thử Đa Dạng Bài 1 - 4 (Marugoto A2.2)</title>
    <meta name="description" content="Chuyên đề ôn tập và đề thi thử đa dạng 6 phần: Trắc nghiệm, Sắp xếp câu, Chia thể, Nối cột hội thoại, Đọc hiểu đoạn văn và Luyện dịch câu 100 điểm cho Marugoto A2.2 Bài 1 - 4.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="../assets/js/audio-engine.js?v=2"></script>
    <link rel="stylesheet" href="../assets/css/mini-test-11-14.css?v=1">
</head>
<body class="mini-test-page">

<div class="container">

    <!-- Global Hub Header Navigation -->
    <nav class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🏠 Trang Chủ</a>
        <a href="../Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item">📗 Ngữ Pháp A1-A2</a>
        
        <div class="hub-dropdown">
            <button class="hub-nav-item hub-drop-btn">📚 Bài Học A2.2 ▾</button>
            <div class="hub-dropdown-menu">
                <a href="../lessons/Marugoto_A2_2_Lesson_1.html" class="hub-drop-link">🌸 Bài 1: いいなまえですね</a>
                <a href="../lessons/Marugoto_A2_2_Lesson_2.html" class="hub-drop-link">👓 Bài 2: めがねをかけている人です</a>
                <a href="../lessons/Marugoto_A2_2_Lesson_3.html" class="hub-drop-link">🍲 Bài 3: おすすめは何ですか</a>
                <a href="../lessons/Marugoto_A2_2_Lesson_4.html" class="hub-drop-link">🥢 Bài 4: どうやって食べますか</a>
            </div>
        </div>

        <div class="hub-dropdown">
            <button class="hub-nav-item hub-drop-btn active">🎯 Mini Test ▾</button>
            <div class="hub-dropdown-menu">
                <a href="On_Tap_Mini_Test_A2_2_1_4.html" class="hub-drop-link active">🎯 Ôn Tập A2.2 Bài 1-4 (Hiện tại)</a>
                <a href="On_Tap_Mini_Test_A2_15_18.html" class="hub-drop-link">🎯 Ôn Tập A2.1 Bài 15-18</a>
                <a href="On_Tap_Mini_Test_A2_11_14.html" class="hub-drop-link">🎯 Ôn Tập A2.1 Bài 11-14</a>
                <a href="On_Tap_Mini_Test_A2_5_8.html" class="hub-drop-link">🎯 Ôn Tập A2.1 Bài 5-8</a>
                <a href="On_Tap_Mini_Test_A2_1_4.html" class="hub-drop-link">🎯 Ôn Tập A2.1 Bài 1-4</a>
            </div>
        </div>
    </nav>

    <!-- Hero Header -->
    <header class="hero-header" style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 45%, #4338ca 100%);">
        <span class="hero-badge" style="background: #4f46e5; color: #ffffff;">MARUGOTO A2.2 • CHUYÊN ĐỀ BÀI 1 - 4</span>
        <h1 class="hero-title">Cẩm Nang & Đề Thi Thử Bài 1 – 4</h1>
        <p class="hero-desc">
            Nắm chắc trọn vẹn ngữ pháp Nという意味, mệnh đề bổ nghĩa N, phán đoán 〜そう, nguyên nhân 〜ので, cấm đoán 〜てはいけません cùng 81 từ vựng & 49 chữ Hán chuẩn kỳ thi Mini Test!
        </p>

        <div class="hero-stats">
            <div class="stat-pill">
                <span class="stat-pill-dot" style="background: #10b981;"></span>
                <span>⏱️ Thời gian: <strong>45 Phút</strong></span>
            </div>
            <div class="stat-pill">
                <span class="stat-pill-dot" style="background: #f59e0b;"></span>
                <span>💯 Thang điểm: <strong>100 Điểm (32 Câu)</strong></span>
            </div>
            <div class="stat-pill">
                <span class="stat-pill-dot" style="background: #3b82f6;"></span>
                <span>🎴 <strong>81 Từ Vựng & 49 Kanji</strong></span>
            </div>
            <div class="stat-pill">
                <span class="stat-pill-dot" style="background: #ec4899;"></span>
                <span>🔊 Phát Âm Tokyo & Lưu Checkpoint</span>
            </div>
        </div>
    </header>

    <!-- Tab Bar -->
    <div class="tab-nav-wrapper">
        <div class="tab-nav">
            <button class="tab-btn" onclick="switchTab('tab-theory', this)">📖 Lý Thuyết 1–4</button>
            <button class="tab-btn" onclick="switchTab('tab-vocab', this)">🎴 81 Từ Vựng</button>
            <button class="tab-btn" onclick="switchTab('tab-kanji', this)">⛩️ 49 Kanji</button>
            <button class="tab-btn active" onclick="switchTab('tab-quiz', this)">🎯 Đề Thi • 32 Câu</button>
            <button class="tab-btn" onclick="switchTab('tab-cheat', this)">⚡ Cẩm Nang Bỏ Túi</button>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 1: LÝ THUYẾT 1–4                                           -->
    <!-- ============================================================== -->
    <div id="tab-theory" class="tab-panel">
        
        <!-- Quick Nav Sub-bar -->
        <div class="theory-quicknav">
            <a href="#theory-b1" class="quicknav-pill">Bài 1: Ý nghĩa & Bổ nghĩa N</a>
            <a href="#theory-b2" class="quicknav-pill">Bài 2: Nhận diện, 〜そう & Trạng từ</a>
            <a href="#theory-b3" class="quicknav-pill">Bài 3: 〜ので, 〜のは & 〜なら</a>
            <a href="#theory-b4" class="quicknav-pill">Bài 4: 〜てはいけません, 〜てから & 〜ないで</a>
        </div>

        <!-- BÀI 1 -->
        <div class="content-card" id="theory-b1">
            <div class="section-header">
                <div>
                    <span class="section-badge">BÀI 1 • いいなまえですね</span>
                    <h2 class="section-title">1. N という意味 & Mệnh đề bổ nghĩa cho danh từ</h2>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 1</span>
                    <span class="grammar-title">N という意味 (Có nghĩa là N) & N1 という N2 (N2 có tên gọi là N1)</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Giải thích nghĩa: <code>[Từ ngữ / Cách nói] ＋ という 意味です。</code><br>
                        • Khi muốn hỏi nghĩa: <code>[Từ ngữ] は どういう 意味ですか。</code><br>
                        • Gọi tên người / vật / địa điểm: <code>N1 (Tên riêng) ＋ という ＋ N2 (Danh từ chỉ nhóm/loại)</code>
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Ý nghĩa & Cách dùng:</strong><br>
                        - <code>という意味</code>: Dùng để giải thích hoặc định nghĩa ý nghĩa của một từ, cụm từ hoặc biển báo.<br>
                        - <code>N1 という N2</code>: Dùng để giới thiệu tên gọi của người, đồ ăn, quán xá, địa danh... mà người nghe có thể chưa từng biết tới.<br><br>
                        🌟 <strong>Ví dụ thực chiến:</strong><br>
                        • 「無料（むりょう）」は <strong>お金が かからない という 意味です</strong>。(“Muryou” có nghĩa là không mất tiền).<br>
                        • これは 何と いう 意味ですか。(Cái này có nghĩa là gì vậy?).<br>
                        • わたしは <strong>山田さんという 人</strong>に 会いました。(Tôi đã gặp một người tên là Yamada).<br>
                        • 駅の 近くに <strong>「さくら」という レストラン</strong>が あります。(Ở gần ga có một nhà hàng tên là Sakura).
                    </div>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 2</span>
                    <span class="grammar-title">Mệnh đề thể thông thường bổ nghĩa cho danh từ (普通形 ＋ N)</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Động từ: <code>V (Thể thông thường - Vる / Vた / Vない) ＋ N</code><br>
                        • Tính từ đuôi い: <code>イA (Thể thông thường) ＋ N</code><br>
                        • Tính từ đuôi な: <code>ナA (Thể thông thường) ＋ な ＋ N</code> (⚠️ Chú ý: だ biến thành な)<br>
                        • Danh từ: <code>N1 ＋ の ＋ N2</code>
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Nguyên tắc vàng:</strong><br>
                        - Cả mệnh đề bổ nghĩa luôn đặt <strong>NGAY TRƯỚC</strong> danh từ được bổ nghĩa.<br>
                        - Chủ ngữ trong mệnh đề phụ bổ nghĩa phải đi với trợ từ <code>が</code> (hoặc <code>の</code>), không dùng <code>は</code>.<br><br>
                        🌟 <strong>Ví dụ thực chiến:</strong><br>
                        • これは わたしが <strong>先週 買った</strong> 本です。(Đây là cuốn sách tôi đã mua tuần trước).<br>
                        • <strong>日本で 買った</strong> お菓子は とても おいしいです。(Bánh kẹo đã mua ở Nhật rất ngon).<br>
                        • 京都には <strong>有名な</strong> お寺が たくさん あります。(Ở Kyoto có rất nhiều ngôi chùa nổi tiếng).<br>
                        • あそこで <strong>先生と 話している</strong> 人は 田中さんです。(Người đang nói chuyện với thầy giáo ở đằng kia là anh Tanaka).
                    </div>
                </div>
            </div>
        </div>

        <!-- BÀI 2 -->
        <div class="content-card" id="theory-b2">
            <div class="section-header">
                <div>
                    <span class="section-badge">BÀI 2 • めがねをかけている人です</span>
                    <h2 class="section-title">2. Nhận diện người, Phán đoán 〜そう & Trạng từ hóa</h2>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 3</span>
                    <span class="grammar-title">Nhận diện người bằng mệnh đề: Tính chất + N & Vている + N</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Đặc điểm ngoại hình: <code>[Bộ phận cơ thể] が [Tính từ] ＋ 人</code> (<em>かみが 長い 人</em>)<br>
                        • Trang phục / Hành động: <code>V-ている ＋ 人</code> (<em>めがねを かけている 人</em>, <em>青い服を 着ている 人</em>)
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Cách dùng:</strong> Dùng để xác định, miêu tả một người cụ thể trong đám đông thông qua đặc điểm diện mạo, quần áo phụ kiện đang mặc hoặc hành động họ đang làm.<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • あそこで <strong>めがねを かけている 人</strong>は 誰ですか。(Người đang đeo kính ở đằng kia là ai thế?).<br>
                        • <strong>青い シャツを 着ている 人</strong>が 田中さんです。(Người đang mặc chiếc áo sơ mi xanh là anh Tanaka).
                    </div>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 4</span>
                    <span class="grammar-title">Phán đoán diện mạo qua thị giác: 〜そうです ／ 〜そうな N</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Tính từ đuôi い: <code>Bỏ [い] ＋ そうです</code> (<em>おいしい ➔ おいしそう</em>)<br>
                        • Tính từ đuôi な: <code>Bỏ [な] ＋ そうです</code> (<em>元気な ➔ 元気そう</em>)<br>
                        • Bổ nghĩa danh từ: <code>[Tính từ bỏ い/bỏ な] ＋ そうな ＋ N</code> (<em>やさしそうな 人</em>)<br>
                        • ⚠️ Ngoại lệ đặc biệt: <code>いい ➔ よさそう</code> (Tuyệt đối không nói <code>いいそう</code> ❌)
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Ý nghĩa:</strong> Diễn tả cảm nhận, phán đoán trực quan khi nhìn vào người hoặc vật (“trông có vẻ...”, “dường như...”).<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • この ケーキは とても <strong>おいしそう</strong>ですね。(Chiếc bánh này trông có vẻ ngon nhỉ).<br>
                        • 田中さんは <strong>やさしそうな 人</strong>ですね。(Anh Tanaka trông có vẻ là người rất hiền lành, tốt bụng).
                    </div>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 5</span>
                    <span class="grammar-title">Tính từ làm trạng từ bổ nghĩa cho động từ: 〜く ／ 〜に ＋ V</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Tính từ đuôi い: <code>Bỏ [い] ＋ く ＋ V</code> (<em>短い ➔ 短く 切る</em>)<br>
                        • Tính từ đuôi な: <code>Bỏ [な] ＋ に ＋ V</code> (<em>きれいな ➔ きれいに 書く</em>)
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Ý nghĩa:</strong> Diễn tả cách thức, tính chất thực hiện một hành động (cắt ngắn, viết đẹp, nói chuyện to/nhỏ...).<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • 髪を <strong>短く</strong> 切りました。(Tôi đã cắt tóc ngắn).<br>
                        • ノートに 字を <strong>きれいに</strong> 書いてください。(Hãy viết chữ đẹp vào vở nhé).<br>
                        • 子どもが ケーキを <strong>おいしそうに</strong> 食べています。(Đứa bé đang ăn chiếc bánh một cách ngon lành).
                    </div>
                </div>
            </div>
        </div>

        <!-- BÀI 3 -->
        <div class="content-card" id="theory-b3">
            <div class="section-header">
                <div>
                    <span class="section-badge">BÀI 3 • おすすめは何ですか</span>
                    <h2 class="section-title">3. Lý do 〜ので, Danh từ hóa 〜のは, Gợi ý 〜なら & Phân phối 〜ずつ</h2>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 6</span>
                    <span class="grammar-title">Lý do nguyên nhân mềm mại, khách quan: 〜ので</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Động từ / Tính từ đuôi い: <code>Thể thông thường (普通形) ＋ ので</code><br>
                        • Tính từ đuôi な / Danh từ: <code>Từ căn ＋ な ＋ ので</code> (⚠️ Chú ý: だ biến thành な, ví dụ <em>暇なので</em>, <em>雨なので</em>)
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Bản chất sư phạm:</strong> So với <code>から</code> (mang tính chủ quan của người nói), <code>ので</code> mang sắc thái khách quan, lịch sự, mềm mại hơn, thường dùng khi xin phép, thông báo lý do một cách trang nhã.<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • あしたは 試験が <strong>あるので</strong>、早く 帰ります。(Vì ngày mai có bài thi nên tôi về sớm).<br>
                        • きょうは <strong>暇なので</strong>、映画を 見に 行きませんか。(Hôm nay rảnh rỗi nên cùng đi xem phim nhé?).
                    </div>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 7</span>
                    <span class="grammar-title">Danh từ hóa mệnh đề: 〜のは 〜です & Gợi ý: N なら</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Danh từ hóa: <code>[Mệnh đề thể thông thường] ＋ のは ＋ [N] です。</code><br>
                        • Đưa ra gợi ý: <code>N (Chủ đề người nghe hỏi) ＋ なら、〜がいいですよ／おすすめです。</code>
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Ý nghĩa:</strong><br>
                        - <code>〜のは 〜です</code>: Dùng trợ từ <code>の</code> để biến cả một câu thành cụm danh từ làm chủ ngữ nhằm nhấn mạnh vào vế sau.<br>
                        - <code>N なら</code>: Đưa ra lựa chọn, đề xuất phù hợp nhất với chủ đề mà đối phương vừa nêu ra.<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • わたしが <strong>いちばん 好きなのは</strong>、和食です。(Thứ mà tôi thích nhất chính là món ăn Nhật).<br>
                        • A: 「おすすめの 料理は 何ですか。」ー B: 「<strong>魚なら</strong>、この 刺身が 一番ですよ。」(Nếu là cá thì món sashimi này là số một).
                    </div>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 8</span>
                    <span class="grammar-title">Phân phối đều theo số lượng: Số từ ＋ ずつ</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        <code>[Số từ / Lượng từ] ＋ ずつ</code> (<em>一つずつ</em>, <em>1人ずつ</em>, <em>少しずつ</em>)
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Ý nghĩa:</strong> Diễn tả việc chia đều số lượng cho từng đối tượng hoặc thực hiện từng chút một.<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • ケーキを <strong>一つずつ</strong> 取ってください。(Mỗi người hãy lấy một chiếc bánh nhé).<br>
                        • 日本語が <strong>少しずつ</strong> 上手に なりました。(Tiếng Nhật đã tiến bộ từng chút một).
                    </div>
                </div>
            </div>
        </div>

        <!-- BÀI 4 -->
        <div class="content-card" id="theory-b4">
            <div class="section-header">
                <div>
                    <span class="section-badge">BÀI 4 • どうやって食べますか</span>
                    <h2 class="section-title">4. Cấm đoán 〜てはいけません, Trình tự 〜てから & Làm V2 mà không V1 〜ないで</h2>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 9</span>
                    <span class="grammar-title">Cấm đoán quy định: V-ては いけません (Không được phép làm V)</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Lịch sự / Quy định: <code>V-ては いけません</code> (<em>吸っては いけません</em>)<br>
                        • Thân mật trong giao tiếp: <code>V-ちゃ だめ</code> / <code>V-じゃ だめ</code> (<em>食べちゃだめ</em>, <em>飲んじゃだめ</em>)
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Ý nghĩa:</strong> Diễn tả lệnh cấm tuyệt đối, các quy định tại nơi công cộng hoặc người trên nhắc nhở người dưới.<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • ここで たばこを <strong>吸っては いけません</strong>。(Không được phép hút thuốc ở đây).<br>
                        • 試験の とき、ケータイを <strong>使っては だめです</strong>。(Trong giờ thi không được dùng điện thoại di động).
                    </div>
                </div>
            </div>

            <div class="grammar-card">
                <div class="grammar-header">
                    <span class="grammar-tag">NGỮ PHÁP 10</span>
                    <span class="grammar-title">Trình tự: V1-てから V2 & Làm V2 mà không làm V1: V-ないで V2</span>
                </div>
                <div class="grammar-body">
                    <div class="formula-box">
                        • Trình tự hành động: <code>V1-て ＋ から、V2</code> (Sau khi hoàn tất V1 thì làm V2)<br>
                        • Trạng thái không làm V1: <code>V1-ない ＋ で、V2</code> (Làm V2 mà KHÔNG làm V1)<br>
                        • Điều kiện hệ quả: <code>V(Thể từ điển) ＋ と、〜</code> (Hễ làm V thì sẽ xảy ra kết quả...)
                    </div>
                    <div class="grammar-explain">
                        👉 <strong>Phân biệt sư phạm:</strong><br>
                        - <code>Vてから</code>: Nhấn mạnh V1 phải xong xuôi trọn vẹn rồi mới chuyển sang V2.<br>
                        - <code>Vないで</code>: Diễn tả thực hiện V2 trong trạng thái không làm V1 (khác với <code>なくて</code> chỉ nguyên nhân).<br><br>
                        🌟 <strong>Ví dụ:</strong><br>
                        • 手を <strong>洗ってから</strong>、ご飯を 食べます。(Sau khi rửa tay sạch sẽ thì ăn cơm).<br>
                        • しょうゆを <strong>つけないで</strong>、そのまま 食べます。(Ăn trực tiếp mà không chấm nước tương).<br>
                        • マヨネーズを <strong>つけると</strong>、とても おいしいです。(Hễ chấm sốt mayonnaise là ngon lắm).
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 2: TỪ VỰNG (81 TỪ)                                          -->
    <!-- ============================================================== -->
    <div id="tab-vocab" class="tab-panel">
        <div class="toolbar-card">
            <div class="filter-row" id="vocabFilterGroup">
                <span style="font-size: 0.85rem; font-weight: 800; color: var(--gray-600); margin-right: 4px;">CHỌN BÀI:</span>
                <button type="button" class="filter-btn active" onclick="filterVocab('ALL', this)">🌟 Tất Cả (81 từ)</button>
                <button type="button" class="filter-btn" onclick="filterVocab('L1', this)">Bài 1 (20 từ)</button>
                <button type="button" class="filter-btn" onclick="filterVocab('L2', this)">Bài 2 (17 từ)</button>
                <button type="button" class="filter-btn" onclick="filterVocab('L3', this)">Bài 3 (21 từ)</button>
                <button type="button" class="filter-btn" onclick="filterVocab('L4', this)">Bài 4 (23 từ)</button>
            </div>
            <div class="action-row">
                <div class="search-input-box">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="vocabSearchInput" placeholder="Tìm kiếm từ vựng (Kanji, Kana, Romaji, tiếng Việt)..." oninput="handleVocabSearch()">
                </div>
                <button type="button" class="tool-toggle-btn" id="hideMeaningBtn" onclick="toggleHideMeaning()">
                    👁️ Ẩn nghĩa tiếng Việt (Tự dò)
                </button>
                <button type="button" class="btn-quizlet" id="btnQuizletCopy" onclick="copyVocabQuizletFormat()" title="Định dạng Tab sạch 100%, gõ siêu mượt trên Quizlet: かな [Tab] Nghĩa">
                    📋 Copy Gõ Kana (<span id="quizletVocabCount">81</span> từ)
                </button>
                <button type="button" class="btn-quizlet" onclick="copyVocabColonFormat()" style="background: linear-gradient(135deg, #059669, #10b981);" title="Định dạng dấu hai chấm: かな：Nghĩa">
                    📋 Copy Dấu (：)
                </button>
                <button type="button" class="btn-quizlet" onclick="copyVocabCombinedFormat()" style="background: linear-gradient(135deg, #7c3aed, #9333ea);" title="Dạng chuẩn Quizlet: Kanji [Tab] [Kana] Nghĩa">
                    🎴 Copy Kèm Kanji (Tab)
                </button>
                <button type="button" class="btn-quizlet" onclick="copyFullVocabAllFormat()" style="background: #1e1b4b;" title="Sao chép toàn bộ 81 từ">
                    ⚡ Copy Toàn Bộ (81 Từ)
                </button>
            </div>
        </div>

        <div class="vocab-grid" id="vocabContainer">
            <!-- Render via JS -->
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 3: KANJI (49 CHỮ HÁN)                                      -->
    <!-- ============================================================== -->
    <div id="tab-kanji" class="tab-panel">
        <div class="toolbar-card">
            <div class="filter-row" id="kanjiFilterGroup">
                <span style="font-size: 0.85rem; font-weight: 800; color: var(--gray-600); margin-right: 4px;">CHỌN BÀI:</span>
                <button type="button" class="filter-btn active" onclick="filterKanji('ALL', this)">⛩️ Tất Cả (49 Kanji Bài 1-4)</button>
                <button type="button" class="filter-btn" onclick="filterKanji('L1', this)">Bài 1 (8 chữ)</button>
                <button type="button" class="filter-btn" onclick="filterKanji('L2', this)">Bài 2 (13 chữ)</button>
                <button type="button" class="filter-btn" onclick="filterKanji('L3', this)">Bài 3 (18 chữ)</button>
                <button type="button" class="filter-btn" onclick="filterKanji('L4', this)">Bài 4 (10 chữ)</button>
            </div>
            <div class="action-row">
                <div class="search-input-box">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="kanjiSearchInput" placeholder="Tìm kiếm chữ Hán, Hán Việt, cách đọc hoặc ý nghĩa..." oninput="handleKanjiSearch()">
                </div>
                <button type="button" class="btn-quizlet" onclick="copyKanjiQuizletTabFormat()" title="Định dạng Tab sạch chuẩn Quizlet">
                    📋 Copy Kanji Tab (<span id="quizletKanjiCount">49</span> chữ)
                </button>
                <button type="button" class="btn-quizlet" onclick="copyKanjiColonFormat()" style="background: linear-gradient(135deg, #059669, #10b981);" title="Chữ Hán, Nghĩa, HÁN VIỆT : Cách Đọc">
                    📋 Copy Kanji Dấu (：)
                </button>
            </div>
        </div>

        <div class="kanji-grid" id="kanjiContainer">
            <!-- Render via JS -->
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 4: ĐỀ THI THỬ 6 PHẦN (100 ĐIỂM)                           -->
    <!-- ============================================================== -->
    <div id="tab-quiz" class="tab-panel active">
        
        <!-- Score Bar & Timer -->
        <div class="quiz-stats-card">
            <div class="quiz-score-box">
                <div class="score-circle">
                    <span class="score-num" id="totalScoreDisplay">0</span>
                    <span class="score-max">/100 ĐIỂM</span>
                </div>
                <div class="score-info">
                    <h4 id="quizStatusTitle">Đề Khảo Sát Năng Lực Toàn Diện Bài 1 – 4</h4>
                    <p id="quizProgressText">Hoàn thành: 0/32 câu • Tổng điểm hiện tại: 0 / 100đ</p>
                </div>
            </div>
            <div class="quiz-action-btns">
                <div class="timer-badge">
                    ⏱️ <span id="timerDisplay">45:00</span>
                </div>
                <button type="button" class="quiz-btn" onclick="toggleTimer()" id="timerToggleBtn">⏸️ Tạm Dừng</button>
                <button type="button" class="quiz-btn primary" onclick="submitAndGradeExam()">🎯 Nộp Bài & Chấm Điểm</button>
                <button type="button" class="quiz-btn" onclick="resetExamSuite()" style="background:#fee2e2; color:#991b1b; border-color:#fecaca;">🔄 Làm Lại Đề Thi</button>
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

        <!-- PHẦN I: TRẮC NGHIỆM -->
        <div id="sec-part1">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%);">
                <div class="exam-part-title">
                    <span>📌 PHẦN I: TRẮC NGHIỆM TỔNG HỢP NGỮ PHÁP & TRỢ TỪ</span>
                </div>
                <span class="part-badge-tag">10 Câu • 25 Điểm (2.5đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Chọn 1 phương án đúng nhất (A, B, C hoặc D) điền vào chỗ trống [____]. Chấm điểm tức thì kèm giải thích chi tiết.
            </p>
            <div id="part1Container"></div>
        </div>

        <!-- PHẦN II: SẮP XẾP TỪ -->
        <div id="sec-part2">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #b45309 0%, #78350f 100%);">
                <div class="exam-part-title">
                    <span>⭐ PHẦN II: SẮP XẾP TỪ THÀNH CÂU HOÀN CHỈNH (並べ替え)</span>
                </div>
                <span class="part-badge-tag">5 Câu • 15 Điểm (3đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Bấm vào các thẻ từ (Chips) theo thứ tự đúng để ghép vào câu, sau đó kiểm tra từ ở vị trí ngôi sao <strong>[ ★ ]</strong>.
            </p>
            <div id="part2Container"></div>
        </div>

        <!-- PHẦN III: CHIA DẠNG ĐÚNG -->
        <div id="sec-part3">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #047857 0%, #064e3b 100%);">
                <div class="exam-part-title">
                    <span>✍️ PHẦN III: CHIA DẠNG ĐÚNG CỦA TỪ TRONG NGOẶC (活用形・穴埋め)</span>
                </div>
                <span class="part-badge-tag">5 Câu • 15 Điểm (3đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Điền dạng biến đổi thích hợp của từ trong ngoặc đơn vào ô trống, sau đó bấm <strong>[Kiểm Tra]</strong> hoặc phím <strong>Enter</strong>.
            </p>
            <div id="part3Container"></div>
        </div>

        <!-- PHẦN IV: NỐI CỘT TÌNH HUỐNG -->
        <div id="sec-part4">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #6d28d9 0%, #4c1d95 100%);">
                <div class="exam-part-title">
                    <span>🔄 PHẦN IV: NỐI CỘT TÌNH HUỐNG & PHẢN XẠ ĐỜI SỐNG (マッチング)</span>
                </div>
                <span class="part-badge-tag">4 Câu • 10 Điểm (2.5đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Chọn câu đáp lại phù hợp và lịch sự nhất trong các tình huống giao tiếp thường ngày tại Nhật Bản.
            </p>
            <div id="part4Container"></div>
        </div>

        <!-- PHẦN V: ĐỌC HIỂU -->
        <div id="sec-part5">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #0284c7 0%, #0c4a6e 100%);">
                <div class="exam-part-title">
                    <span>📖 PHẦN V: ĐỌC HIỂU ĐOẠN VĂN THỰC TẾ (読解)</span>
                </div>
                <span class="part-badge-tag">4 Câu / 2 Bài Đọc • 20 Điểm (5đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Đọc kỹ các đoạn văn ngắn về cuộc sống, tiệc tùng và quy tắc nhà hàng Nhật Bản, sau đó trả lời các câu hỏi trắc nghiệm.
            </p>
            <div id="part5Container"></div>
        </div>

        <!-- PHẦN VI: LUYỆN DỊCH CÂU -->
        <div id="sec-part6">
            <div class="exam-part-header" style="background: linear-gradient(135deg, #b91c1c 0%, #7f1d1d 100%);">
                <div class="exam-part-title">
                    <span>✍️ PHẦN VI: LUYỆN DỊCH CÂU THỰC CHIẾN 2 CHIỀU</span>
                </div>
                <span class="part-badge-tag">4 Câu • 15 Điểm (3.75đ/câu)</span>
            </div>
            <p style="margin-bottom: 16px; color: var(--gray-600); font-size: 0.95rem;">
                👉 <strong>Hướng dẫn:</strong> Thử sức tự gõ câu dịch tiếng Nhật vào ô trống, sau đó bấm xem đáp án mẫu, từ khóa và đối chiếu tự chấm điểm.
            </p>
            <div id="part6Container"></div>
        </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 5: CẨM NANG BỎ TÚI (CHEAT SHEET)                          -->
    <!-- ============================================================== -->
    <div id="tab-cheat" class="tab-panel">
        <div class="content-card">
            <div class="section-header">
                <div>
                    <span class="section-badge">CẨM NANG PHÒNG THI MARUGOTO A2.2</span>
                    <h2 class="section-title">⚡ 8 Bẫy Sư Phạm Kinh Điển Cần Tránh Tuyệt Đối</h2>
                </div>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 1 • BỔ NGHĨA CHO DANH TỪ (BÀI 1)</span>
                <h3 class="cheat-title">Tính từ な và Danh từ khi bổ nghĩa</h3>
                <p class="cheat-content">
                    • <strong>Tính từ đuôi な:</strong> Bắt buộc giữ lại <code>な</code> khi đứng trước danh từ (<em>有名な 人</em>). Cấm nói <code>有名だ人</code> ❌!<br>
                    • <strong>Danh từ:</strong> Nối với danh từ khác bắt buộc phải dùng trợ từ <code>の</code> (<em>日本の 料理</em>, <em>友達の 車</em>).<br>
                    • <strong>Động từ:</strong> Dùng thể thông thường (<em>買った本</em> - sách đã mua, <em>買う本</em> - sách sẽ mua).
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 2 • PHÂN BIỆT HAI CẤU TRÚC TO IU (BÀI 1)</span>
                <h3 class="cheat-title">N という意味 vs N1 という N2</h3>
                <p class="cheat-content">
                    • <strong>N という意味:</strong> Dùng để GIẢI THÍCH Ý NGHĨA của từ vựng/cách nói (<em>「無料」はお金がかからないという意味です</em>).<br>
                    • <strong>N1 という N2:</strong> Dùng để GỌI TÊN cụ thể người/vật mà người nghe chưa biết (<em>「さくら」というレストラン</em>, <em>田中さんという人</em>).
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 3 • PHÁN ĐOÁN DIỆN MẠO (BÀI 2)</span>
                <h3 class="cheat-title">Quy tắc bỏ đuôi của 〜そうです & Ngoại lệ いい</h3>
                <p class="cheat-content">
                    • <strong>Tính từ đuôi い:</strong> Bỏ hẳn [い] + そうです (<em>おいしい ➔ おいしそう</em>). Cấm nói <code>おいしいそう</code> ❌!<br>
                    • <strong>Tính từ đuôi な:</strong> Bỏ [な] + そうです (<em>元気な ➔ 元気そう</em>).<br>
                    • <strong>Ngoại lệ bắt buộc nhớ:</strong> <code>いい ➔ よさそう</code> (Trông có vẻ tốt). Tuyệt đối cấm nói <code>いいそう</code> ❌!<br>
                    • <strong>Khi bổ nghĩa cho danh từ:</strong> Phải biến thành <code>〜そうな ＋ N</code> (<em>やさしそうな 人</em>).
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 4 • TRẠNG TỪ HÓA TÍNH TỪ (BÀI 2)</span>
                <h3 class="cheat-title">Tính từ đuôi い biến thành 〜く, Tính từ な biến thành 〜に</h3>
                <p class="cheat-content">
                    • <strong>Tính từ đuôi い:</strong> Bỏ [い] thay bằng <code>く</code> (<em>短い ➔ 短く 切る</em>, <em>おいしい ➔ おいしそうに 食べる</em>).<br>
                    • <strong>Tính từ đuôi な:</strong> Bỏ [な] thay bằng <code>に</code> (<em>きれいな ➔ きれいに 書く</em>, <em>静かな ➔ 静かに 話す</em>).<br>
                    👉 Ghi nhớ: Phó từ đứng trước động từ để mô tả phương thức, mức độ thực hiện hành động.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 5 • NGUYÊN NHÂN MỀM MẠI (BÀI 3)</span>
                <h3 class="cheat-title">〜ので vs 〜から & Biến đổi なので</h3>
                <p class="cheat-content">
                    • <strong>Tính từ đuôi な & Danh từ:</strong> Trước <code>ので</code> phải dùng chữ <code>な</code> (<em>暇なので</em>, <em>雨なので</em>). Cấm nói <code>暇だので</code> ❌!<br>
                    • <strong>Sắc thái:</strong> <code>ので</code> mang tính khách quan, trang nhã, thường dùng khi xin phép hoặc nêu lý do nhẹ nhàng. Không đi với câu mệnh lệnh ép buộc như <code>から</code>.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 6 • DANH TỪ HÓA & GỢI Ý (BÀI 3)</span>
                <h3 class="cheat-title">〜のは 〜です vs N ＋ なら</h3>
                <p class="cheat-content">
                    • <strong>〜のは 〜です:</strong> Dùng <code>の</code> để biến cả mệnh đề thành danh từ làm chủ ngữ: <em>わたしが 好きなのは、すしです</em>.<br>
                    • <strong>N ＋ なら:</strong> Bắt lấy chủ đề mà người nghe đang hỏi để đưa ra gợi ý tốt nhất: <em>魚なら、この刺身が おすすめです</em>.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 7 • CẤM ĐOÁN VS XIN PHÉP (BÀI 4)</span>
                <h3 class="cheat-title">V-てはいけません vs V-てもいいですか</h3>
                <p class="cheat-content">
                    • <strong>Cấm đoán:</strong> <code>V-ては いけません</code> (<em>吸っては いけません</em> - Cấm hút thuốc).<br>
                    • <strong>Xin phép:</strong> <code>V-ても いいですか</code> (<em>使っても いいですか</em> - Cho tôi dùng có được không?).<br>
                    👉 Câu thần chú: <code>ても</code> = Làm cũng ĐƯỢC; <code>ては</code> = Làm thì CẤM! Văn nói thân mật cấm đoán: <code>〜ちゃだめ / 〜じゃだめ</code>.
                </p>
            </div>

            <div class="cheat-card">
                <span class="cheat-badge">BẪY 8 • HÀNH ĐỘNG PHỤ VS NGUYÊN NHÂN (BÀI 4)</span>
                <h3 class="cheat-title">V-ないで vs V-なくて & Trình tự V-てから</h3>
                <p class="cheat-content">
                    • <strong>V-ないで:</strong> Làm hành động V2 mà KHÔNG LÀM V1 (trạng thái đồng hành: <em>何もつけないで 食べます</em>).<br>
                    • <strong>V-なくて:</strong> Chỉ NGUYÊN NHÂN dẫn đến kết quả ngoài ý muốn (<em>お金が なくて 買えません</em>).<br>
                    • <strong>V-てから:</strong> Xong hẳn V1 mới làm tiếp V2 (<em>手を 洗ってから ご飯を 食べる</em>).
                </p>
            </div>
        </div>
    </div>

</div>

<!-- Modal Kết Quả Điểm Số -->
<div id="scoreModal" class="modal-overlay" style="display:none;">
    <div class="modal-card">
        <div style="font-size: 3rem; margin-bottom: 10px;" id="modalEmoji">🎉</div>
        <h2 style="font-size: 1.5rem; font-weight: 800; color: #1e1b4b; margin-bottom: 6px;" id="modalTitle">Kết Quả Bài Thi Thử A2.2 Bài 1–4</h2>
        <div style="font-size: 2.4rem; font-weight: 900; color: var(--primary); margin: 12px 0;" id="modalScoreDisplay">0 / 100 Điểm</div>
        <p style="color: var(--gray-600); font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px;" id="modalFeedback">
            Lời nhận xét chi tiết và định hướng ôn tập.
        </p>
        <div style="display: flex; gap: 12px; justify-content: center;">
            <button class="btn-ctrl" onclick="closeScoreModal()" style="background:var(--primary); color:white; border-color:var(--primary); font-weight:800; padding:10px 24px;">
                Xem Chi Tiết Từng Câu
            </button>
            <button class="btn-ctrl" onclick="resetExamSuite(); closeScoreModal();" style="background:#fee2e2; color:#991b1b; border-color:#fecaca; padding:10px 20px;">
                Làm Lại Đề Thi
            </button>
        </div>
    </div>
</div>

<!-- Toast Notification -->
<div id="toast" class="toast">Đã sao chép vào bộ nhớ tạm!</div>

<script src="../assets/data/mini_a2_2_1_4_data.js?v=1"></script>
<script src="../assets/js/mini-test-a2-2-1-4.js?v=1"></script>
<script src="../assets/nav.js?v=6" defer></script>
</body>
</html>
"""

html_path = os.path.join(WORKSPACE, 'tests/On_Tap_Mini_Test_A2_2_1_4.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Successfully generated {html_path} ({len(HTML_CONTENT)} bytes)")

