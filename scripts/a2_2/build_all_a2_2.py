# -*- coding: utf-8 -*-
"""
Master Builder for Marugoto A2-2 (All 9 Topics, Lessons 1 through 18):
- Builds lessons/Marugoto_A2_2_Lesson_{1..18}.html
- Builds assets/js/lessons/lesson_a2_2_{01..18}.js
- Syncs data/kanji_vocab_a2_2.json
- Updates assets/data/kanji_a2_data.js
- Updates assets/nav.js with ALL_LESSONS_A2_2
"""

import json
from pathlib import Path
import re
import sys

# Ensure repository root is on sys.path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.a2_2.generator_core import build_js_file, build_lesson_html
import scripts.a2_2.topic_01 as t1
import scripts.a2_2.topic_02 as t2
import scripts.a2_2.topic_03 as t3
import scripts.a2_2.topic_04 as t4
import scripts.a2_2.topic_05 as t5
import scripts.a2_2.topic_06 as t6
import scripts.a2_2.topic_07 as t7
import scripts.a2_2.topic_08 as t8
import scripts.a2_2.topic_09 as t9


LESSONS_CONFIG = [
    # Topic 1
    {
        "num": 1, "topic_num": 1, "topic_name_jp": "新しい友だち",
        "title": "いいなまえですね", "quote": "いいなまえですね",
        "subtitle": "Học cách giới thiệu bản thân chi tiết: giải thích ý nghĩa nguồn gốc tên mình (N という意味), gọi tên người/vật chưa biết (N1 という N2), bổ nghĩa cho danh từ (普通形 ＋ N), quê quán (で 生まれました) và bày tỏ hứng thú (に 興味があります).",
        "vocab": t1.L1_VOCAB, "verbs": t1.L1_VERBS, "kanji_list": t1.L1_KANJI_LIST, "kanji_cards": t1.L1_KANJI_CARDS,
        "grammar": t1.L1_GRAMMAR_BLOCKS, "quiz": t1.L1_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① N という意味</a>',
            '<a href="#sec-grammar2" class="sec-link">② N1 という N2</a>',
            '<a href="#sec-grammar3" class="sec-link">③ 普通形 ＋ N</a>',
            '<a href="#sec-grammar4" class="sec-link">④ Mở Rộng Giới Thiệu</a>',
        ]
    },
    {
        "num": 2, "topic_num": 1, "topic_name_jp": "新しい友だち",
        "title": "めがねをかけている人です", "quote": "めがねを かけて いる人です",
        "subtitle": "Làm chủ đại cẩm nang 5 động từ mang mặc trang phục (着る, 履く, 被る, 掛ける, する), mẫu câu miêu tả trạng thái (～を 着ています) và mệnh đề định ngữ nhận diện người trong đám đông (V-ている 人).",
        "vocab": t1.L2_VOCAB, "verbs": t1.L2_VERBS, "kanji_list": t1.L2_KANJI_LIST, "kanji_cards": t1.L2_KANJI_CARDS,
        "grammar": t1.L2_GRAMMAR_BLOCKS, "quiz": t1.L2_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① 5 Động Từ Mặc</a>',
            '<a href="#sec-grammar2" class="sec-link">② V-ています Trạng Thái</a>',
            '<a href="#sec-grammar3" class="sec-link">③ Mệnh Đề Định Ngữ</a>',
        ]
    },
    # Topic 2
    {
        "num": 3, "topic_num": 2, "topic_name_jp": "店で食べる",
        "title": "おすすめは何ですか", "quote": "おすすめは何ですか",
        "subtitle": "Khám phá thế giới ẩm thực và quán ăn Nhật Bản (居酒屋, 定食), hỏi món gợi ý ngon nhất, diễn đạt các cung bậc hương vị (甘い, 辛い, 苦い, 酸っぱい, しょっぱい) và thử nghiệm món mới với 『V-てみます』 & 『V-たことがあります』.",
        "vocab": t2.L3_VOCAB, "verbs": t2.L3_VERBS, "kanji_list": t2.L3_KANJI_LIST, "kanji_cards": t2.L3_KANJI_CARDS,
        "grammar": t2.L3_GRAMMAR_BLOCKS, "quiz": t2.L3_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Thử món: V-てみます</a>',
            '<a href="#sec-grammar2" class="sec-link">② Trải nghiệm: V-たことがあります</a>',
            '<a href="#sec-grammar3" class="sec-link">③ Hỏi gợi ý: おすすめは何ですか</a>',
        ],
        "morph_labels": {
            "form1": "Dạng V-てみます (làm thử)",
            "form2": "Dạng V-たことがある (đã từng)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 4, "topic_num": 2, "topic_name_jp": "店で食べる",
        "title": "どうやって食べますか", "quote": "どうやって食べますか",
        "subtitle": "Bí kíp ăn uống chuẩn chỉ khi du lịch Nhật: yêu cầu không lấy nguyên liệu do dị ứng hoặc khẩu vị 『V-ないでください』 & 『N-抜きで』, cùng cẩm nang thưởng thức đúng điệu 『どうやって食べますか (chấm つける vs rưới かける)』.",
        "vocab": t2.L4_VOCAB, "verbs": t2.L4_VERBS, "kanji_list": t2.L4_KANJI_LIST, "kanji_cards": t2.L4_KANJI_CARDS,
        "grammar": t2.L4_GRAMMAR_BLOCKS, "quiz": t2.L4_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Bỏ nguyên liệu: V-ないで / N-抜きで</a>',
            '<a href="#sec-grammar2" class="sec-link">② Cách ăn: どうやって食べますか</a>',
        ],
        "morph_labels": {
            "form1": "Dạng V-ないで (xin đừng)",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    # Topic 3
    {
        "num": 5, "topic_num": 3, "topic_name_jp": "沖縄旅行",
        "title": "ぼうしを持っていったほうがいいです", "quote": "ぼうしを持っていったほうがいいです",
        "subtitle": "Lên kế hoạch và chuẩn bị hành lý cho chuyến du lịch phương nam Okinawa: đưa ra lời khuyên thiết thực 『V-たほうがいい / V-ないほうがいい』 và xin gợi ý hành trình từ người bản xứ 『V-たらいいですか』.",
        "vocab": t3.L5_VOCAB, "verbs": t3.L5_VERBS, "kanji_list": t3.L5_KANJI_LIST, "kanji_cards": t3.L5_KANJI_CARDS,
        "grammar": t3.L5_GRAMMAR_BLOCKS, "quiz": t3.L5_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Lời khuyên: V-た / ない ほうがいい</a>',
            '<a href="#sec-grammar2" class="sec-link">② Xin ý kiến: V-たらいいですか</a>',
        ],
        "morph_labels": {
            "form1": "Khuyên nên: V-たほうがいい",
            "form2": "Khuyên không nên: V-ないほうがいい",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 6, "topic_num": 3, "topic_name_jp": "沖縄旅行",
        "title": "海で泳いだり、写真を撮ったりしました", "quote": "海で泳いだり、写真を撮ったりしました",
        "subtitle": "Kể lại kỳ nghỉ rực rỡ sắc màu: liệt kê các hoạt động tiêu biểu 『V1-たり、V2-たりします/しました』, khám phá khả năng tự tay làm đồ thủ công thủy tinh Ryukyu 『V-ることができます』 và chia sẻ kỷ niệm đáng nhớ.",
        "vocab": t3.L6_VOCAB, "verbs": t3.L6_VERBS, "kanji_list": t3.L6_KANJI_LIST, "kanji_cards": t3.L6_KANJI_CARDS,
        "grammar": t3.L6_GRAMMAR_BLOCKS, "quiz": t3.L6_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Liệt kê hoạt động: V-たり V-たり</a>',
            '<a href="#sec-grammar2" class="sec-link">② Khả năng trải nghiệm: V-ることができる</a>',
        ],
        "morph_labels": {
            "form1": "Dạng V-たり (khi thì...)",
            "form2": "Khả năng: V-ることができる",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    # Topic 4
    {
        "num": 7, "topic_num": 4, "topic_name_jp": "日本まつり",
        "title": "雨がふったら、どうしますか", "quote": "雨がふったら、どうしますか",
        "subtitle": "Hòa mình vào không khí sôi động của Lễ hội truyền thống Nhật Bản: xử lý tình huống giả định thời tiết 『V-たら (Nếu trời mưa...)』, rủ bạn bè mặc Yukata cùng tham gia 『V-ませんか & V-ましょう』 và hẹn điểm tập trung.",
        "vocab": t4.L7_VOCAB, "verbs": t4.L7_VERBS, "kanji_list": t4.L7_KANJI_LIST, "kanji_cards": t4.L7_KANJI_CARDS,
        "grammar": t4.L7_GRAMMAR_BLOCKS, "quiz": t4.L7_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Câu điều kiện: V-たら</a>',
            '<a href="#sec-grammar2" class="sec-link">② Rủ rê tham gia: V-ませんか / ましょう</a>',
        ],
        "morph_labels": {
            "form1": "Dạng V-たら (nếu... / sau khi...)",
            "form2": "Rủ rê: V-ましょう",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 8, "topic_num": 4, "topic_name_jp": "日本まつり",
        "title": "コンサートはもう始まりましたか", "quote": "コンサートはもう始まりましたか",
        "subtitle": "Nắm bắt tiến độ sự kiện lễ hội: hỏi việc đã diễn ra chưa với 『もう V-ましたか ➔ いいえ、まだ V-ていません』, thiết lập trình tự thưởng thức ẩm thực quầy Yatai rồi xem pháo hoa 『V-てから』.",
        "vocab": t4.L8_VOCAB, "verbs": t4.L8_VERBS, "kanji_list": t4.L8_KANJI_LIST, "kanji_cards": t4.L8_KANJI_CARDS,
        "grammar": t4.L8_GRAMMAR_BLOCKS, "quiz": t4.L8_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Tiến độ: もう V-ました / まだ V-ていません</a>',
            '<a href="#sec-grammar2" class="sec-link">② Trình tự: V-てから</a>',
        ],
        "morph_labels": {
            "form1": "Đã làm rồi: もう V-ました",
            "form2": "Vẫn chưa: まだ V-ていません",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    # Topic 5
    {
        "num": 9, "topic_num": 5, "topic_name_jp": "とくべつな日",
        "title": "来週、お祝いをしましょう", "quote": "来週、お祝いをしましょう",
        "subtitle": "Cẩm nang trao đổi và lên kế hoạch tổ chức tiệc mừng kỷ niệm (kết hôn, sinh nhật, thăng chức, tốt nghiệp): làm chủ bộ 3 động từ cho nhận 『あげる / もらう / くれる』 và 5 câu hỏi bàn bạc kinh điển.",
        "vocab": t5.L9_VOCAB, "verbs": t5.L9_VERBS, "kanji_list": t5.L9_KANJI_LIST, "kanji_cards": t5.L9_KANJI_CARDS,
        "grammar": t5.L9_GRAMMAR_BLOCKS, "quiz": t5.L9_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Cho nhận: あげる / もらう / くれる</a>',
            '<a href="#sec-grammar2" class="sec-link">② Bàn kế hoạch tiệc mừng</a>',
        ],
        "morph_labels": {
            "form1": "Dạng cho nhận: V-てあげる / もらう / くれる",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 10, "topic_num": 5, "topic_name_jp": "とくべつな日",
        "title": "どんなケーキがいいですか", "quote": "どんなケーキがいいですか",
        "subtitle": "Lên thực đơn bánh kem và quà tặng cho ngày đặc biệt: hỏi sở thích chi tiết 『どんな N がいいですか』, quyết định dứt khoát 『N にします』 và gửi gắm lời cảm ơn chân thành 『V-てくれてありがとう』.",
        "vocab": t5.L10_VOCAB, "verbs": t5.L10_VERBS, "kanji_list": t5.L10_KANJI_LIST, "kanji_cards": t5.L10_KANJI_CARDS,
        "grammar": t5.L10_GRAMMAR_BLOCKS, "quiz": t5.L10_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Cảm ơn: V-てくれてありがとう</a>',
            '<a href="#sec-grammar2" class="sec-link">② Quyết định chọn: N にします</a>',
        ],
        "morph_labels": {
            "form1": "Cảm ơn: V-てくれてありがとう",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    # Topic 6
    {
        "num": 11, "topic_num": 6, "topic_name_jp": "ネットショッピング",
        "title": "掃除機がこわれてしまったんです", "quote": "掃除機がこわれてしまったんです",
        "subtitle": "Xử lý sự cố máy móc gia dụng bị hỏng hóc: diễn tả hoàn cảnh và sự cố đáng tiếc 『V-てしまいました ＋ ～んです』, yêu cầu hỗ trợ sửa chữa và đổi trả sản phẩm trực tuyến.",
        "vocab": t6.L11_VOCAB, "verbs": t6.L11_VERBS, "kanji_list": t6.L11_KANJI_LIST, "kanji_cards": t6.L11_KANJI_CARDS,
        "grammar": t6.L11_GRAMMAR_BLOCKS, "quiz": t6.L11_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Sự cố tiếc nuối: V-てしまいました / んです</a>',
            '<a href="#sec-grammar2" class="sec-link">② Sửa chữa & Đổi trả bảo hành</a>',
        ],
        "morph_labels": {
            "form1": "Sự cố tiếc nuối: V-てしまった",
            "form2": "Giãi bày lý do: V-たんです",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 12, "topic_num": 6, "topic_name_jp": "ネットショッピング",
        "title": "こっちの方が安いです", "quote": "こっちの方が安いです",
        "subtitle": "Nghệ thuật săn sale và mua hàng thông thái qua mạng: so sánh hai sản phẩm 『N1 の方が N2 より A です』, hỏi phân vân 『どちらが A ですか』, đọc hiểu review đánh giá sao và chính sách freeship.",
        "vocab": t6.L12_VOCAB, "verbs": t6.L12_VERBS, "kanji_list": t6.L12_KANJI_LIST, "kanji_cards": t6.L12_KANJI_CARDS,
        "grammar": t6.L12_GRAMMAR_BLOCKS, "quiz": t6.L12_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① So sánh hơn: N1 の方が N2 より A</a>',
            '<a href="#sec-grammar2" class="sec-link">② Hỏi chọn lựa: どちらが A ですか</a>',
        ],
        "morph_labels": {
            "form1": "Dễ/khó dùng: V-やすい / にくい",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    # Topic 7
    {
        "num": 13, "topic_num": 7, "topic_name_jp": "れきしと文化の町",
        "title": "どうやって行きますか", "quote": "どうやって行きますか",
        "subtitle": "Chinh phục hệ thống giao thông công cộng Nhật Bản: chỉ đường và đổi tuyến tàu điện / xe buýt 『～に乗って、～で降ります』, hỏi chi phí & thời gian 『どのくらいかかりますか』.",
        "vocab": t7.L13_VOCAB, "verbs": t7.L13_VERBS, "kanji_list": t7.L13_KANJI_LIST, "kanji_cards": t7.L13_KANJI_CARDS,
        "grammar": t7.L13_GRAMMAR_BLOCKS, "quiz": t7.L13_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Chỉ đường & Chuyển tuyến</a>',
            '<a href="#sec-grammar2" class="sec-link">② Thời gian & Chi phí: どのくらい</a>',
        ],
        "morph_labels": {
            "form1": "Trình tự: V-てから",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 14, "topic_num": 7, "topic_name_jp": "れきしと文化の町",
        "title": "有名なお寺です", "quote": "有名なお寺です",
        "subtitle": "Khám phá chiều sâu cố đô và di tích lịch sử: mệnh đề định ngữ nâng cao miêu tả di sản 『[Câu định ngữ] ＋ N (建てられたお寺)』 và chia sẻ truyền thuyết tâm linh 『～と言われています』.",
        "vocab": t7.L14_VOCAB, "verbs": t7.L14_VERBS, "kanji_list": t7.L14_KANJI_LIST, "kanji_cards": t7.L14_KANJI_CARDS,
        "grammar": t7.L14_GRAMMAR_BLOCKS, "quiz": t7.L14_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Mệnh đề định ngữ di tích lịch sử</a>',
            '<a href="#sec-grammar2" class="sec-link">② Tương truyền rằng: ～と言われています</a>',
        ],
        "morph_labels": {
            "form1": "Bị động/di sản: V-られた (được xây)",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    # Topic 8
    {
        "num": 15, "topic_num": 8, "topic_name_jp": "せいかつとエコ",
        "title": "ごみはビニール袋に入れます", "quote": "ごみはビニール袋に入れます",
        "subtitle": "Sống văn minh tại xứ sở hoa anh đào: làm chủ quy tắc phân loại rác bắt buộc 『V-なければなりません / なくてもいいです』, nhận diện rác cháy được, không cháy được và rác tài nguyên tái chế.",
        "vocab": t8.L15_VOCAB, "verbs": t8.L15_VERBS, "kanji_list": t8.L15_KANJI_LIST, "kanji_cards": t8.L15_KANJI_CARDS,
        "grammar": t8.L15_GRAMMAR_BLOCKS, "quiz": t8.L15_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Quy tắc bắt buộc: V-なければなりません</a>',
            '<a href="#sec-grammar2" class="sec-link">② Quy trình phân loại rác tái chế</a>',
        ],
        "morph_labels": {
            "form1": "Bắt buộc: V-なければならない",
            "form2": "Không cần: V-なくてもいい",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 16, "topic_num": 8, "topic_name_jp": "せいかつとエコ",
        "title": "毎日、水を使わない日があります", "quote": "毎日、水を使わない日があります",
        "subtitle": "Chiến dịch bảo vệ môi trường và thói quen sống xanh: nỗ lực duy trì hành động tích cực 『V-る / ない ようにしています (luôn tắt điện, khóa nước)』 và mệnh đề định ngữ 『[V] ＋ 日 (ngày không dùng nước)』.",
        "vocab": t8.L16_VOCAB, "verbs": t8.L16_VERBS, "kanji_list": t8.L16_KANJI_LIST, "kanji_cards": t8.L16_KANJI_CARDS,
        "grammar": t8.L16_GRAMMAR_BLOCKS, "quiz": t8.L16_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Thói quen sống xanh: V-ようにしています</a>',
            '<a href="#sec-grammar2" class="sec-link">② Định ngữ chỉ ngày: [V] ＋ 日</a>',
        ],
        "morph_labels": {
            "form1": "Thói quen: V-ようにしている",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    # Topic 9
    {
        "num": 17, "topic_num": 9, "topic_name_jp": "じんせい",
        "title": "この人、知っていますか", "quote": "この人、知っていますか",
        "subtitle": "Kể chuyện về những con người truyền cảm hứng: tóm tắt tiểu sử cuộc đời danh nhân 『～で生まれ、～で育ちました』, các bước ngoặt 『V-たあとで』 và sự ghi nhận trên toàn cầu 『～に愛されています』.",
        "vocab": t9.L17_VOCAB, "verbs": t9.L17_VERBS, "kanji_list": t9.L17_KANJI_LIST, "kanji_cards": t9.L17_KANJI_CARDS,
        "grammar": t9.L17_GRAMMAR_BLOCKS, "quiz": t9.L17_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Tiểu sử cuộc đời: Sinh ra & Lớn lên</a>',
            '<a href="#sec-grammar2" class="sec-link">② Yêu mến toàn cầu: V-られている</a>',
        ],
        "morph_labels": {
            "form1": "Bị động tôn vinh: V-られている",
            "form2": "Sau khi: V-たあとで",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    },
    {
        "num": 18, "topic_num": 9, "topic_name_jp": "じんせい",
        "title": "どんな子どもでしたか", "quote": "どんな子どもでしたか",
        "subtitle": "Hồi tưởng ký ức tuổi thơ 『子どもの頃、よく V-ました』 và hạ quyết tâm cho hành trình tương lai rực rỡ với Thể Ý Chí 『V-ようと思っています』. Tổng kết toàn diện và tốt nghiệp Marugoto A2-2!",
        "vocab": t9.L18_VOCAB, "verbs": t9.L18_VERBS, "kanji_list": t9.L18_KANJI_LIST, "kanji_cards": t9.L18_KANJI_CARDS,
        "grammar": t9.L18_GRAMMAR_BLOCKS, "quiz": t9.L18_QUIZ,
        "section_links": [
            '<a href="#sec-grammar1" class="sec-link">① Kỷ niệm tuổi thơ: 子どものとき</a>',
            '<a href="#sec-grammar2" class="sec-link">② Thể Ý Chí: V-ようと思っています</a>',
        ],
        "morph_labels": {
            "form1": "Thể Ý Chí: V-ようと思っている",
            "form2": "Thay đổi: V-るようになった",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }
    }
]


def update_nav_js():
    nav_path = ROOT / "assets/nav.js"
    content = nav_path.read_text(encoding="utf-8")

    all_a2_2_items = []
    icons = ["🌸", "👓", "🍲", "🥢", "✈️", "🏖️", "🏮", "🎆", "🎉", "🎂", "🧹", "🏷️", "🚇", "🛕", "♻️", "🌱", "🏆", "🚀"]

    for cfg in LESSONS_CONFIG:
        num_str = f"{cfg['num']:02d}"
        icon = icons[cfg["num"] - 1]
        desc_short = cfg["subtitle"][:55].rstrip() + "..."
        all_a2_2_items.append({
            "file": f"Marugoto_A2_2_Lesson_{cfg['num']}.html",
            "num": num_str,
            "title": f"Bài {cfg['num']}: {cfg['title']}",
            "desc": f"{cfg['quote']} • {desc_short}",
            "icon": icon,
            "tag": "A2-2 Mới"
        })

    # Find ALL_LESSONS_A2_2 in nav.js
    pattern = r"const ALL_LESSONS_A2_2 = \[\s*[\s\S]*?\s*\];"
    new_decl = f"const ALL_LESSONS_A2_2 = {json.dumps(all_a2_2_items, ensure_ascii=False, indent=8)};"
    updated = re.sub(pattern, new_decl, content)
    nav_path.write_text(updated, encoding="utf-8")
    print(f"Updated {nav_path} with all 18 lessons in ALL_LESSONS_A2_2!")


def sync_kanji_data():
    all_kanji_vocab = {}
    for cfg in LESSONS_CONFIG:
        all_kanji_vocab[f"lesson_{cfg['num']}"] = cfg["kanji_list"]

    json_path = ROOT / "data/kanji_vocab_a2_2.json"
    json_path.write_text(
        json.dumps(all_kanji_vocab, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(f"Synced {json_path} for all 18 lessons!")

    # Update assets/data/kanji_a2_data.js
    js_path = ROOT / "assets/data/kanji_a2_data.js"
    content = js_path.read_text(encoding="utf-8")
    match = re.search(r"var VOCAB_121_DATA = (\[.*?\]);", content)
    if not match:
        raise ValueError("Could not find VOCAB_121_DATA in kanji_a2_data.js")

    current_data = json.loads(match.group(1))
    cleaned_data = [item for item in current_data if not str(item.get("lesson", "")).startswith("A2-2")]

    new_items = []
    for cfg in LESSONS_CONFIG:
        label = f"A2-2 L{cfg['num']}"
        for item in cfg["kanji_list"]:
            new_items.append({
                "lesson": label,
                "kanji": item["word"],
                "kana": item["kana"],
                "vi": item["mean"],
                "group": "A2-2 Trọng tâm"
            })

    total_data = cleaned_data + new_items
    new_decl = f"var VOCAB_121_DATA = {json.dumps(total_data, ensure_ascii=False)};"
    updated_content = content[:match.start()] + new_decl + content[match.end():]
    js_path.write_text(updated_content, encoding="utf-8")
    print(f"Updated {js_path} with total {len(total_data)} Kanji entries!")


def main():
    print(f"=== BUILDING ALL 18 LESSONS OF MARUGOTO A2-2 ===")
    for cfg in LESSONS_CONFIG:
        num = cfg["num"]
        js_file = f"lesson_a2_2_{num:02d}.js"
        html_file = f"Marugoto_A2_2_Lesson_{num}.html"

        # 1. Build JS file
        build_js_file(
            dest_path=ROOT / f"assets/js/lessons/{js_file}",
            vocab_list=cfg["vocab"],
            verb_list=cfg["verbs"],
            quiz_list=cfg["quiz"],
            badge_name=f"Bài {num} (A2-2)"
        )

        # 2. Build HTML file
        build_lesson_html(
            dest_path=ROOT / f"lessons/{html_file}",
            topic_num=cfg["topic_num"],
            topic_name_jp=cfg["topic_name_jp"],
            lesson_num=num,
            lesson_title=cfg["title"],
            quote=cfg["quote"],
            subtitle=cfg["subtitle"],
            vocab_count=len(cfg["vocab"]),
            grammar_count=len(cfg["grammar"]),
            verb_count=len(cfg["verbs"]),
            kanji_count=len(cfg["kanji_cards"]),
            grammar_blocks=cfg["grammar"],
            kanji_cards=cfg["kanji_cards"],
            js_filename=js_file,
            section_links=cfg.get("section_links"),
            morph_labels=cfg.get("morph_labels")
        )

    # 3. Update master data and nav
    sync_kanji_data()
    update_nav_js()
    print("=== MARUGOTO A2-2 FULL BUILD COMPLETED SUCCESSFULLY! ===")


if __name__ == "__main__":
    main()
