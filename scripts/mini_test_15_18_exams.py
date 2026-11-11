#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/mini_test_15_18_exams.py
Chứa 4 Mã Đề chuyên sâu mới (152, 153, 154, 155) nối tiếp Đề 151 trong
tests/On_Tap_Mini_Test_A2_15_18.html, bám sát 100% Marugoto A2-1 Bài 15-18 + NPBS
và đảm bảo 0 chữ Hán (Kanji) chưa học, không lẫn ngữ pháp ngoài bài.
"""

import re

# Tập 204 chữ Kanji đã học qua Marugoto Starter (A1) + Elementary 1 (A2-1 L1-18) + Bảng Kanji L11-18
LEARNED_KANJI = set(
    "一七万三上下中乗九事二五京人今仕休会体何作使借元先入全八六円写冬出分到前勉動化"
    "北十千午半南卵去友口古右味員喫四回国土地場夏外多夜大天女好婚子字学安家小少山川"
    "左年広店張強待後思所手持支文料新旅族日春昼時晴書月朝木末本来東校楽歌止歩母毎気"
    "水泳海港漢火無然父物理生由男町画留病発白百的目真着社祝神私秋空結絵耳聞肉自色花"
    "英茶荷菜行西見言計話誕語読買資赤走起足車転送通週運道酒野金門間雨雪雲電青面音頭"
    "願風食飲館駅高魚黒"
)

BANNED_REGEXES = [
    r"ほうがいい",
    r"ほうが\s*いい",
    r"(?<!ひつ)ようです",
    r"履く|履き",
    r"被る|被り",
    r"掛ける|掛け",
    r"眼鏡|めがね|マフラー|ぼうし|スニーカー",
]


def _iter_strings(obj, path=""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from _iter_strings(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _iter_strings(v, f"{path}[{i}]")


def validate_exam_suite(exams_list):
    """Kiểm tra toàn bộ đề thi: đủ 32 câu/đề, 0 Kanji chưa học, 0 mẫu câu ngoài bài."""
    unlearned_hits = []
    banned_hits = []
    structure_errors = []

    for ex in exams_list:
        code = ex.get("code", "?")
        p1, p2, p3, p4, p5, p6 = (
            ex.get("p1", []),
            ex.get("p2", []),
            ex.get("p3", []),
            ex.get("p4", []),
            ex.get("p5", []),
            ex.get("p6", []),
        )
        p5_q_count = sum(len(pas.get("questions", [])) for pas in p5)
        if (len(p1), len(p2), len(p3), len(p4), p5_q_count, len(p6)) != (10, 5, 5, 4, 4, 4):
            structure_errors.append(
                f"Exam {code} count mismatch: p1={len(p1)}, p2={len(p2)}, p3={len(p3)}, p4={len(p4)}, p5_q={p5_q_count}, p6={len(p6)}"
            )

        # Kiểm tra Part II chip không được xếp sẵn [0,1,2,3] và đủ 4 chip khác nhau
        for item in p2:
            if item.get("correctOrder") == [0, 1, 2, 3]:
                structure_errors.append(f"Exam {code} Q{item['id']} chưa xáo trộn chip [0,1,2,3]")
            if len(set(item.get("chips", []))) != 4:
                structure_errors.append(f"Exam {code} Q{item['id']} chips bị trùng lặp")

        for path, text in _iter_strings(ex, f"Exam[{code}]"):
            bad_kanji = sorted({ch for ch in text if "\u4e00" <= ch <= "\u9fff" and ch not in LEARNED_KANJI})
            if bad_kanji:
                unlearned_hits.append((path, bad_kanji, text))
            for pat in BANNED_REGEXES:
                if re.search(pat, text):
                    banned_hits.append((path, pat, text))

    return {
        "structure_errors": structure_errors,
        "unlearned_hits": unlearned_hits,
        "banned_hits": banned_hits,
    }


# ==============================================================================
# MÃ ĐỀ 152: SỨC KHỎE, VẬN ĐỘNG & MỆNH ĐỀ BỔ NGHĨA (TRỌNG TÂM BÀI 15-16 + NPBS)
# ==============================================================================
EXAM_152 = {
    "id": "152",
    "code": "152",
    "shortTitle": "Sức Khỏe & Bổ Nghĩa",
    "fullTitle": "MÃ ĐỀ 152 • CHUYÊN SÂU BÀI 15 - 16 (SỨC KHỎE, THỂ DỤC & BỔ NGHĨA V+N)",
    "subtitle": "Luyện kỹ mẫu hỏi thăm/khuyên nhủ Bài 15, động từ thể dục, mục đích ために và 6 dạng mệnh đề bổ nghĩa V〈ふつうけい〉＋ 人/N.",
    "badge": "🏥 Chuyên sâu L15–16",
    "p1": [
        {
            "id": 1,
            "category": "Bài 15 • Trình bày trạng thái cơ thể (～んです)",
            "q": "「げんきが ありませんね。どうしたんですか。」――「きょうは たいちょうが [____]。」",
            "options": ["わるいです", "わるいんです", "わるくんです", "わるかったんですか"],
            "correct": 1,
            "explain": "Khi trả lời câu hỏi thăm tình trạng 「どうしたんですか」(Bạn bị sao thế?), dùng tính từ đuôi い nguyên dạng + 「んです」 ➔ 「わるいんです」 để giải thích tình trạng hiện tại."
        },
        {
            "id": 2,
            "category": "Bài 15 • Lời khuyên tập thể dục nhẹ nhàng (V-る といいですよ)",
            "q": "「かたが いたいんです。」――「ときどき、うでを 上に [____] と いいですよ。」",
            "options": ["あげて", "あげた", "あげる", "あげます"],
            "correct": 2,
            "explain": "Khuyên nhủ động tác giãn cơ: 「Động từ thể Từ điển (V-る) ＋ と いいですよ」. Động từ 「あげます」 (nhóm 2) chia về thể từ điển là 「あげる」."
        },
        {
            "id": 3,
            "category": "Bài 15 • Khuyên can bảo vệ mắt (V-ない ＋ で ください)",
            "q": "「目が つかれて いますから、きょうは あまり テレビを [____] ください。」",
            "options": ["見ない", "見なくて", "見るないで", "見ないで"],
            "correct": 3,
            "explain": "Dặn dò ai đó đừng làm hành động gì: 「V(thể ない) ＋ で ください」. 「見ます」 nhóm 2 bỏ ます thêm ない ➔ 「見ない」 ➔ 「見ないで ください」."
        },
        {
            "id": 4,
            "category": "Bài 15 • Thư giãn trước khi kiểm tra (V-る といいですよ)",
            "q": "「きんちょうして います。」――「ゆっくり しんこきゅうを [____] と いいですよ。」",
            "options": ["する", "して", "した", "します"],
            "correct": 0,
            "explain": "Động từ nhóm 3 「します」 chuyển sang thể Từ điển là 「する」 để kết hợp trong mẫu lời khuyên 「すると いいですよ」 (Hít thở sâu thì tốt đấy)."
        },
        {
            "id": 5,
            "category": "Bài 16 • Liệt kê hoạt động thư giãn (V1-たり、V2-たり)",
            "q": "やすみの 日は うちで ストレッチを [____]、音楽を 聞いたり します。",
            "options": ["して", "したり", "するたり", "した"],
            "correct": 1,
            "explain": "Cấu trúc liệt kê hành động tiêu biểu: 「V1-たり、V2-たり します」. 「します」 ➔ thể Ta 「した」 + 「り」 ➔ 「したり」."
        },
        {
            "id": 6,
            "category": "Bài 16 • Biểu đạt mục đích (N の ために)",
            "q": "[____] の ために、毎日 野菜を たくさん 食べて、8時間 ねます。",
            "options": ["けんこうな", "けんこうだ", "けんこう", "けんこうに"],
            "correct": 2,
            "explain": "Mẫu câu chỉ mục đích: 「Danh từ (N) ＋ の ために」. 「けんこう」 là danh từ nên ghép trực tiếp với 「の ために」 (Vì sức khỏe...)."
        },
        {
            "id": 7,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa đang tiếp diễn (V-ている ＋ 人)",
            "q": "あそこで ストレッチを [____] 人は やまださんの おとうとです。",
            "options": ["して います", "します", "した いる", "して いる"],
            "correct": 3,
            "explain": "Động từ bổ nghĩa cho danh từ 「人」 ở thì hiện tại tiếp diễn phải chuyển 「ています」 về thể thông thường là 「ている」: 「ストレッチを して いる 人」."
        },
        {
            "id": 8,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa phủ định (V-ない ＋ 子ども)",
            "q": "野菜を [____] 子どもは あまり 元気じゃないです。",
            "options": ["食べない", "食べません", "食べなくて", "食べなかったです"],
            "correct": 0,
            "explain": "Phủ định hiện tại 「食べません」 đứng trước danh từ 「子ども」 phải chuyển sang thể thông thường (ふつうけい) là 「食べない」."
        },
        {
            "id": 9,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa quá khứ (V-た ＋ N)",
            "q": "きのう 友だちと [____] えいがは とても おもしろかったです。",
            "options": ["見ます", "見た", "見て", "見ました"],
            "correct": 1,
            "explain": "Bổ nghĩa cho danh từ 「えいが」 với hành động đã diễn ra hôm qua (きのう): chia 「見ました」 về thể thông thường quá khứ 「見た」."
        },
        {
            "id": 10,
            "category": "Bài 16 • Đánh giá thói quen tốt/xấu cho cơ thể",
            "q": "「毎日 1時間 歩くのは どうですか。」――「ええ、とても [____]。」",
            "options": ["体に わるいです", "けんこうに いいですよ", "けんこうを いいですよ", "体で いいですよ"],
            "correct": 1,
            "explain": "Cụm từ chuẩn trong Bài 16: 「けんこうに いい / 体に いい」 (Tốt cho sức khỏe / Tốt cho cơ thể), dùng trợ từ 「に」."
        }
    ],
    "p2": [
        {
            "id": 11,
            "category": "Bài 15 • Giải thích lý do mất ngủ (～んです)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "さいきん、",
            "post": "ねられないんです。",
            "chips": ["よく", "仕事が", "とても", "いそがしくて"],
            "correctOrder": [1, 2, 3, 0],
            "starIndex": 2,
            "starChip": "いそがしくて",
            "fullSentence": "さいきん、仕事が とても いそがしくて よく ねられないんです。",
            "simplifiedSentence": "さいきん、仕事が とても いそがしくて よく ねられないんです。",
            "explain": "Chủ ngữ 「仕事が」 + mức độ 「とても いそがしくて」 (vì bận) + 「よく ねられないんです」. Vị trí ngôi sao là [いそがしくて]."
        },
        {
            "id": 12,
            "category": "Bài 15 • Lời khuyên khi mỏi mắt (V-る といいですよ)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "目が",
            "post": "いいですよ。",
            "chips": ["食べると", "とき、", "つかれた", "ブルーベリーを"],
            "correctOrder": [2, 1, 3, 0],
            "starIndex": 2,
            "starChip": "ブルーベリーを",
            "fullSentence": "目が つかれた とき、ブルーベリーを 食べると いいですよ。",
            "simplifiedSentence": "目が つかれたとき、ブルーベリーを 食べると いいですよ。",
            "explain": "Mệnh đề chỉ thời điểm 「目が つかれた とき」 + tân ngữ 「ブルーベリーを」 + lời khuyên 「食べると いいですよ」. Vị trí ngôi sao là [ブルーベリーを]."
        },
        {
            "id": 13,
            "category": "Bài 16 • Rèn luyện ở phòng tập & hồ bơi (V-たり)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "毎日",
            "post": "して います。",
            "chips": ["プールで", "トレーニングしたり", "泳いだり", "ジムで"],
            "correctOrder": [3, 1, 0, 2],
            "starIndex": 2,
            "starChip": "プールで",
            "fullSentence": "毎日 ジムで トレーニングしたり プールで 泳いだり して います。",
            "simplifiedSentence": "毎日 ジムで トレーニングしたり プールで 泳いだり しています。",
            "explain": "Nơi chốn thực hiện hành động đi với trợ từ 「で」: 「ジムで トレーニングしたり」 + 「プールで 泳いだり」. Vị trí ngôi sao là [プールで]."
        },
        {
            "id": 14,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa đang đọc sách (V-ている ＋ 人)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "いま",
            "post": "人は わたしの 先生です。",
            "chips": ["いる", "本を", "あそこで", "読んで"],
            "correctOrder": [2, 1, 3, 0],
            "starIndex": 2,
            "starChip": "読んで",
            "fullSentence": "いま あそこで 本を 読んで いる 人は わたしの 先生です。",
            "simplifiedSentence": "いま あそこで 本を 読んでいる 人は わたしの 先生です。",
            "explain": "Mệnh đề bổ nghĩa: 「あそこで 本を 読んで いる」 đứng ngay trước danh từ 「人」. Vị trí ngôi sao là [読んで]."
        },
        {
            "id": 15,
            "category": "Bài 16 • Chạy bộ vì sức khỏe (N の ために)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "わたしは 毎朝",
            "post": "います。",
            "chips": ["こうえんを", "ために、", "けんこうの", "走って"],
            "correctOrder": [2, 1, 0, 3],
            "starIndex": 2,
            "starChip": "こうえんを",
            "fullSentence": "わたしは 毎朝 けんこうの ために、こうえんを 走って います。",
            "simplifiedSentence": "わたしは 毎朝 けんこうのために、こうえんを 走っています。",
            "explain": "Mục đích 「けんこうの ために」 đứng trước cụm hành động 「こうえんを 走って います」. Vị trí ngôi sao là [こうえんを]."
        }
    ],
    "p3": [
        {
            "id": 16,
            "category": "Bài 15 • Động từ thể Từ điển (V-る といいですよ)",
            "sentence": "かたが いたい ときは、すこし うでを (まわします) [_______] と いいですよ。",
            "baseWord": "まわします",
            "accepted": ["まわす", "mawasu"],
            "displayAnswer": "まわす (mawasu)",
            "explain": "Đưa lời khuyên nhẹ nhàng dùng thể Từ điển (V-る). 「まわします」 (nhóm 1) bỏ ます đổi し thành す ➔ 「まわす」."
        },
        {
            "id": 17,
            "category": "Bài 15 • Động từ thể Nai dặn dò (V-ないで ください)",
            "sentence": "かぜを ひいて いますから、きょうは あまり 外へ (出かけます) [_______] で ください。",
            "baseWord": "出かけます (でかけます)",
            "accepted": ["出かけない", "でかけない", "dekakenai"],
            "displayAnswer": "出かけない / でかけない (dekakenai)",
            "explain": "Dặn đừng làm gì dùng 「V-ないで ください」. 「出かけます」 (nhóm 2) bỏ ます thêm ない ➔ 「出かけない」."
        },
        {
            "id": 18,
            "category": "Bài 16 • Liệt kê hoạt động (V-たり、V-たり します)",
            "sentence": "週末は いつも こうえんを (走ります) [_______]、うちで ヨガを したり します。",
            "baseWord": "走ります (はしります)",
            "accepted": ["走ったり", "はしったり", "hashittari"],
            "displayAnswer": "走ったり / はしったり (hashittari)",
            "explain": "「走ります」 là động từ nhóm 1 (kết thúc bằng り trước ます) ➔ thể Ta là 「走った」 ➔ ghép 「り」 thành 「走ったり」."
        },
        {
            "id": 19,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa tiếp diễn (V-ている ＋ 人)",
            "sentence": "あそこで 本を (読んで います) [_______] 人は やまださんです。",
            "baseWord": "読んで います (よんで います)",
            "accepted": ["読んでいる", "読んで いる", "よんでいる", "よんで いる", "yondeiru", "yonde iru"],
            "displayAnswer": "読んでいる / よんでいる (yonde iru)",
            "explain": "Động từ đứng trước danh từ 「人」 phải bỏ 「ます」 chuyển sang thể thông thường 「読んでいる」."
        },
        {
            "id": 20,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa phủ định (V-ない ＋ 人)",
            "sentence": "わたしは たばこを (すいません) [_______] 人が 好きです。",
            "baseWord": "すいません",
            "accepted": ["すわない", "suwanai"],
            "displayAnswer": "すわない (suwanai)",
            "explain": "Chú ý đặc biệt động từ nhóm 1 có đuôi い trước ます: 「すいます」 đổi い ➔ わ + ない thành 「すわない」 (KHÔNG phải すあない!)."
        }
    ],
    "p4": [
        {
            "id": 21,
            "category": "Bài 15 • Mất ngủ do mệt mỏi",
            "promptA": "「きのうの よる、あまり ねられなかったんです。」",
            "correctBId": "B1",
            "promptB": "「それは たいへんですね。きょうは はやく うちへ かえって、やすむと いいですよ。」",
            "explain": "Đối phương than phiền không ngủ được ➔ hỏi thăm đồng cảm 「それは たいへんですね」 và khuyên về sớm nghỉ ngơi 「やすむと いいですよ」."
        },
        {
            "id": 22,
            "category": "Bài 15 • Đau cổ vai gáy & Bài tập giãn cơ",
            "promptA": "「さいきん、くびや かたが いたいんです。」",
            "correctBId": "B2",
            "promptB": "「じゃあ、まず しんこきゅうを して、ゆっくり くびを まげると いいですよ。」",
            "explain": "Gặp tình trạng đau cổ/vai ➔ dùng từ nối trình tự Bài 15 「まず…」 kèm động tác 「しんこきゅう」「くびを まげる」 để tư vấn."
        },
        {
            "id": 23,
            "category": "Bài 16 • Hoạt động tại câu lạc bộ thể thao",
            "promptA": "「すてきな スポーツクラブですね。いつも 何を して いますか。」",
            "correctBId": "B3",
            "promptB": "「トレーナーと マシンで トレーニングしたり、プールで 泳いだり して います。」",
            "explain": "Trả lời về thói quen tập luyện trong CLB thể thao bằng 「V1-たり、V2-たり しています」."
        },
        {
            "id": 24,
            "category": "Bài 16 NPBS • Hỏi người đang tập giãn cơ",
            "promptA": "「あそこで ストレッチを して いる 人は だれですか。」",
            "correctBId": "B4",
            "promptB": "「ああ、あれは 新しい スポーツクラブの 先生ですよ。」",
            "explain": "Câu hỏi dùng mệnh đề bổ nghĩa 「ストレッチを している 人」 được đáp lại bằng danh tính người đó."
        }
    ],
    "p5": [
        {
            "passageId": 1,
            "title": "BÀI ĐỌC 1: スポーツクラブの アンケート (Khảo Sát Rèn Luyện Sức Khỏe - Bài 16)",
            "text": "スポーツクラブの けんこう アンケートの けっかです。<br>やまださんは けんこうの ために、毎朝 30分 ウォーキングを しています。そして、週末は ジムで トレーニングを したり、プールで 泳いだり しています。やまださんは「たばこを すわない 人は 元気だと 思います」と 言っていました。<br>キムさんは とても いそがしいですから、スポーツクラブへ あまり 行けません。でも、エレベーターを 使わないで、いつも 会社で 歩いて います。",
            "questions": [
                {
                    "id": 25,
                    "q": "やまださんは 毎朝 けんこうの ために 何を して いますか。",
                    "options": [
                        "プールで 泳いで います",
                        "30分 ウォーキングを して います",
                        "ジムで トレーニングを して います",
                        "エレベーターを 使って います"
                    ],
                    "correct": 1,
                    "explain": "Bài đọc viết: 「やまださんは けんこうの ために、毎朝 30分 ウォーキングを しています」 (Còn gym và bơi là vào cuối tuần 週末)."
                },
                {
                    "id": 26,
                    "q": "キムさんは どうして スポーツクラブへ あまり 行けませんか。",
                    "options": [
                        "スポーツが きらいですから",
                        "プールが ありませんから",
                        "たいちょうが わるいですから",
                        "とても いそがしいですから"
                    ],
                    "correct": 3,
                    "explain": "Bài đọc nêu lý do: 「キムさんは とても いそがしいですから、スポーツクラブへ あまり 行けません」."
                }
            ]
        },
        {
            "passageId": 2,
            "title": "BÀI ĐỌC 2: 会社の 中の たいそう アドバイス (Bài Tập Giữa Giờ - Bài 15)",
            "text": "毎日 ながい 時間 パソコンを 見る 人は、目や かたが つかれますね。たいちょうが わるい ときは、まず 仕事を すこし 休んで ください。<br>それから、こうやって うでを 上に あげたり、かたを ゆっくり まわしたり すると いいですよ。さいごに、目をつむって しんこきゅうを しましょう。あまり 無理を しないで、体と 気もちを リラックスして くださいね。",
            "questions": [
                {
                    "id": 27,
                    "q": "目や かたが つかれて たいちょうが わるい とき、まず 何を しますか。",
                    "options": [
                        "仕事を すこし 休みます",
                        "パソコンを もっと 見ます",
                        "外を 走ります",
                        "くすりを 2つ 飲みます"
                    ],
                    "correct": 0,
                    "explain": "Bài đọc hướng dẫn trình tự: 「たいちょうが わるい ときは、まず 仕事を すこし 休んで ください」."
                },
                {
                    "id": 28,
                    "q": "この ぶんしょうの アドバイスに あって いるのは どれですか。",
                    "options": [
                        "かたが つかれた とき、無理を して 仕事を します",
                        "さいごに お酒を 飲むと いいです",
                        "うでを あげたり、かたを まわしたり すると いいです",
                        "しんこきゅうを しないで ください"
                    ],
                    "correct": 2,
                    "explain": "Bài đọc khuyên: 「うでを 上に あげたり、かたを ゆっくり まわしたり すると いいですよ」."
                }
            ]
        }
    ],
    "p6": [
        {
            "id": 29,
            "category": "Bài 15 • Kết hợp lời khuyên & dặn dò",
            "vi": "Khi bị cảm, bạn nên uống thuốc và xin đừng làm quá sức nhé.",
            "hint": "かぜを ひいた とき, くすりを 飲む といいですよ, 無理を しないで ください",
            "modelSentence": "かぜを ひいた とき、くすりを 飲むと いいですよ。あまり 無理を しないで ください。",
            "modelKana": "かぜを ひいた とき、くすりを のむと いいですよ。あまり むりを しないで ください。",
            "keywords": ["かぜを", "くすりを", "飲むと", "無理を", "しないで"],
            "breakdown": [
                {"part": "かぜを ひいた とき", "role": "Bối cảnh thời điểm (khi bị cảm)"},
                {"part": "くすりを 飲むと いいですよ", "role": "Lời khuyên V-る + といいですよ"},
                {"part": "あまり 無理を しないで ください", "role": "Dặn dò đừng làm quá sức (V-ないで ください)"}
            ]
        },
        {
            "id": 30,
            "category": "Bài 16 • Mục đích sống khỏe (N の ために + V-たり)",
            "vi": "Vì sức khỏe, mỗi sáng tôi đi bộ hoặc tập yoga.",
            "hint": "けんこうの ために, 毎朝 (まいあさ), 歩く (あるく ➔ 歩いたり), ヨガを したり しています",
            "modelSentence": "けんこうの ために、毎朝 歩いたり、ヨガを したり して います。",
            "modelKana": "けんこうの ために、まいあさ あるいたり、ヨガを したり して います。",
            "keywords": ["けんこうの", "ために", "毎朝", "歩いたり", "ヨガを"],
            "breakdown": [
                {"part": "けんこうの ために", "role": "Cụm chỉ mục đích (Vì sức khỏe)"},
                {"part": "毎朝 歩いたり、ヨガを したり しています", "role": "Liệt kê thói quen lặp lại hằng ngày"}
            ]
        },
        {
            "id": 31,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa phủ định",
            "vi": "Những đứa trẻ không ăn rau thì không được khỏe lắm.",
            "hint": "野菜を 食べない 子ども, あまり 元気じゃないです",
            "modelSentence": "野菜を 食べない 子どもは あまり 元気じゃないです。",
            "modelKana": "やさいを たべない こどもは あまり げんきじゃないです。",
            "keywords": ["野菜を", "食べない", "子どもは", "あまり", "元気じゃないです"],
            "breakdown": [
                {"part": "野菜を 食べない 子ども", "role": "Thể phủ định thường 「食べない」 bổ nghĩa cho 「子ども」"},
                {"part": "あまり 元気じゃないです", "role": "Phủ định của tính từ đuôi な (không khỏe lắm)"}
            ]
        },
        {
            "id": 32,
            "category": "Bài 16 NPBS • Mệnh đề bổ nghĩa thì quá khứ",
            "vi": "Bánh mì mà tôi đã mua hôm qua rất ngon.",
            "hint": "きのう 買った パン (買います ➔ 買った), とても おいしかったです",
            "modelSentence": "きのう 買った パンは とても おいしかったです。",
            "modelKana": "きのう かった パンは とても おいしかったです。",
            "keywords": ["きのう", "買った", "パンは", "おいしい", "おいしかったです"],
            "breakdown": [
                {"part": "きのう 買った パン", "role": "Động từ quá khứ thông thường 「買った」 đứng trước danh từ 「パン」"},
                {"part": "とても おいしかったです", "role": "Nhận xét ở thì quá khứ của tính từ đuôi い"}
            ]
        }
    ]
}


# ==============================================================================
# MÃ ĐỀ 153: QUÀ TẶNG, DỊP KỶ NIỆM & BẪY ～んです / と思います (TRỌNG TÂM BÀI 17-18)
# ==============================================================================
EXAM_153 = {
    "id": "153",
    "code": "153",
    "shortTitle": "Quà Tặng & ～んです",
    "fullTitle": "MÃ ĐỀ 153 • CHUYÊN SÂU BÀI 17 - 18 (QUÀ TẶNG, ～んです (だ➔な) & ～と思います)",
    "subtitle": "Luyện chắc các dịp chúc mừng, cặp あげる/もらう, とか～とか, NPBS mở đầu câu với ～んですが và bẫy N/Na + だ.",
    "badge": "🎁 Chuyên sâu L17–18",
    "p1": [
        {
            "id": 1,
            "category": "Bài 17 NPBS • Mở đầu nhờ vả làm mềm câu (～んですが)",
            "q": "すみません、にほんごが よく 分からない [____]、おしえて くださいませんか。",
            "options": ["んですか", "んですが", "のですが", "だんですが"],
            "correct": 1,
            "explain": "Cấu trúc giao tiếp quan trọng NPBS Bài 17: dùng 「Thể thông thường ＋ んですが、…」 để nêu hoàn cảnh mở đầu trước khi nhờ vả."
        },
        {
            "id": 2,
            "category": "Bài 17 NPBS • Quy tắc だ ➔ な với tính từ đuôi な",
            "q": "「この へやは とても しずかで いいですね。」――「ええ、とても [____]。」",
            "options": ["しずかだんです", "しずかなです", "しずかんです", "しずかなんです"],
            "correct": 3,
            "explain": "Tính từ đuôi な trước 「んです」 bắt buộc biến đổi 「だ ➔ な」: 「しずかだ」 ➔ 「しずかなんです」."
        },
        {
            "id": 3,
            "category": "Bài 17 • Tặng quà cho ai (N(người) に N(vật) を あげます)",
            "q": "母の 日に、わたしは 母 [____] きれいな 花と カードを あげました。",
            "options": ["に", "から", "を", "で"],
            "correct": 0,
            "explain": "Tặng quà CHO ai đó dùng trợ từ 「に」 (không dùng から): 「母に 花を あげました」."
        },
        {
            "id": 4,
            "category": "Bài 17 • Nhận quà từ ai (N(người) に もらいました)",
            "q": "「その すてきな ネックレス、だれ [____] もらったんですか。」",
            "options": ["を", "へ", "に", "で"],
            "correct": 2,
            "explain": "Hỏi nhận quà từ ai dùng trợ từ 「に」 (hoặc 「から」): 「だれに もらったんですか」."
        },
        {
            "id": 5,
            "category": "Bài 17 • Mệnh đề định ngữ chọn quà (V-る ＋ もの)",
            "q": "あべさんは 料理が 好きですから、料理の ときに [____] ものが いいと 思います。",
            "options": ["使って", "使った", "使います", "使う"],
            "correct": 3,
            "explain": "Diễn tả công dụng tổng quát của món quà 「Đồ vật dùng khi nấu ăn」: dùng V(thể từ điển) + 「もの」 ➔ 「使う もの」."
        },
        {
            "id": 6,
            "category": "Bài 17 • Liệt kê gợi ý quà tặng (N1 とか N2 とか)",
            "q": "友だちの しゅっさんの お祝いに、おもちゃ [____] あかちゃんの もの [____] を あげます。",
            "options": ["や／と", "とか／とか", "たり／たり", "も／や"],
            "correct": 1,
            "explain": "Liệt kê các gợi ý tiêu biểu về đồ vật dùng 「N1 とか N2 とか」 (như là đồ chơi hay đồ cho em bé...)."
        },
        {
            "id": 7,
            "category": "Bài 18 • Bẫy だ với tính từ đuôi な trước と思います",
            "q": "お祝いの ときは、気もちが いちばん [____] と 思います。",
            "options": ["たいせつ", "たいせつな", "たいせつだ", "たいせつです"],
            "correct": 2,
            "explain": "Tính từ đuôi な 「たいせつ(な)」 ở hiện tại khẳng định khi đứng trước 「と 思います」 bắt buộc thêm 「だ」: 「たいせつだと 思います」."
        },
        {
            "id": 8,
            "category": "Bài 18 • Trích dẫn lời nhận xét quá khứ (～と 言っていました)",
            "q": "さっき カルロスさんは「きのうの パーティーは [____]」と 言っていました。",
            "options": ["とても 楽しかった", "とても 楽しいだ", "とても 楽しかったです", "とても 楽しいな"],
            "correct": 0,
            "explain": "Trích dẫn gián tiếp trước 「と 言っていました」 dùng thể thông thường (ふつうけい). 「楽しかったです」 ➔ 「楽しかった」."
        },
        {
            "id": 9,
            "category": "Bài 18 • Từ vựng bối cảnh sinh con (N が ひつようです)",
            "q": "あかちゃんが 生まれた ときは、あかちゃんの ものが たくさん [____]。",
            "options": ["にあいます", "ひつようです", "よろこびます", "きに いります"],
            "correct": 1,
            "explain": "Mẫu từ vựng Bài 18: 「あかちゃんの ものが ひつようです」 (Đồ dùng của em bé rất cần thiết)."
        },
        {
            "id": 10,
            "category": "Bài 17 NPBS • Định ngữ quá khứ cho vật (V-た ＋ N)",
            "q": "これは 誕生日に あねが [____] セーターです。とても あたたかいです。",
            "options": ["作ります", "作って", "作りました", "作った"],
            "correct": 3,
            "explain": "Động từ bổ nghĩa đứng trước danh từ 「セーター」 diễn tả việc chị gái ĐÃ làm trong quá khứ: 「作りました」 ➔ 「作った セーター」."
        }
    ],
    "p2": [
        {
            "id": 11,
            "category": "Bài 17 NPBS • Mở đầu nhờ tư vấn mua hàng (～んですが)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "パソコンを",
            "post": "いいですか。",
            "chips": ["どれが", "んですが、", "買いたい", "とても"],
            "correctOrder": [2, 1, 0, 3],
            "starIndex": 2,
            "starChip": "どれが",
            "fullSentence": "パソコンを 買いたい んですが、どれが とても いいですか。",
            "simplifiedSentence": "パソコンを 買いたいんですが、どれが とても いいですか。",
            "explain": "Mở đầu bằng ý muốn 「買いたい んですが、」 rồi đặt câu hỏi nhờ tư vấn 「どれが … いいですか」. Vị trí ngôi sao là [どれが]."
        },
        {
            "id": 12,
            "category": "Bài 17 • Liệt kê gợi ý quà mừng đi làm (とか～とか)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "しゅうしょくの お祝いに、",
            "post": "あげたいと 思います。",
            "chips": ["とかを", "時計とか", "めいしいれ", "友だちに"],
            "correctOrder": [3, 1, 2, 0],
            "starIndex": 2,
            "starChip": "めいしいれ",
            "fullSentence": "しゅうしょくの お祝いに、友だちに 時計とか めいしいれ とかを あげたいと 思います。",
            "simplifiedSentence": "しゅうしょくの お祝いに、友だちに 時計とか めいしいれとかを あげたいと 思います。",
            "explain": "Người nhận 「友だちに」 + cụm liệt kê 「時計とか めいしいれ とかを」 + 「あげたいと 思います」. Vị trí ngôi sao là [めいしいれ]."
        },
        {
            "id": 13,
            "category": "Bài 17 NPBS • Định ngữ động từ tiếp diễn (V-ている ＋ N)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "これは",
            "post": "いる めいしいれです。",
            "chips": ["会社で", "使って", "わたしが", "いつも"],
            "correctOrder": [2, 0, 3, 1],
            "starIndex": 2,
            "starChip": "いつも",
            "fullSentence": "これは わたしが 会社で いつも 使って いる めいしいれです。",
            "simplifiedSentence": "これは わたしが 会社で いつも 使っている めいしいれです。",
            "explain": "Chủ thể hành động trong mệnh đề bổ nghĩa dùng trợ từ 「が」 (わたしが), đi qua 「会社で いつも 使って いる」. Vị trí ngôi sao là [いつも]."
        },
        {
            "id": 14,
            "category": "Bài 18 • Đề xuất quà cưới (～と 思います)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "結婚の",
            "post": "思います。",
            "chips": ["いいと", "とても", "この 花びんが", "お祝いに"],
            "correctOrder": [3, 2, 1, 0],
            "starIndex": 2,
            "starChip": "とても",
            "fullSentence": "結婚の お祝いに この 花びんが とても いいと 思います。",
            "simplifiedSentence": "結婚の お祝いに この 花びんが とても いいと 思います。",
            "explain": "Dịp lễ 「結婚の お祝いに」 + đối tượng đề xuất 「この 花びんが」 + nhận xét 「とても いいと 思います」. Vị trí ngôi sao là [とても]."
        },
        {
            "id": 15,
            "category": "Bài 18 • Trích dẫn nhận xét văn hóa (～と 言っていました)",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "キムさんは",
            "post": "言っていました。",
            "chips": ["おもしろいと", "日本の", "とても", "しゅうかんは"],
            "correctOrder": [1, 3, 2, 0],
            "starIndex": 2,
            "starChip": "とても",
            "fullSentence": "キムさんは 日本の しゅうかんは とても おもしろいと 言っていました。",
            "simplifiedSentence": "キムさんは 日本の しゅうかんは とても おもしろいと 言っていました。",
            "explain": "Chủ đề trong câu trích dẫn 「日本の しゅうかんは」 + 「とても おもしろいと 言っていました」. Vị trí ngôi sao là [とても]."
        }
    ],
    "p3": [
        {
            "id": 16,
            "category": "Bài 17 NPBS • Biến đổi だ ➔ な trước んです",
            "sentence": "「どうして この まちが 好きなんですか。」――「とても (しずかです) [_______] んです。」",
            "baseWord": "しずかです",
            "accepted": ["しずかな", "shizukana"],
            "displayAnswer": "しずかな (shizukana)",
            "explain": "Tính từ đuôi な 「しずかだ」 đứng trước 「んです」 phải đổi 「だ ➔ な」 thành 「しずかなんです」."
        },
        {
            "id": 17,
            "category": "Bài 17 • Mệnh đề định ngữ V-る もの",
            "sentence": "あたらしい へやに (かざります) [_______] ものを 買いたいです。",
            "baseWord": "かざります",
            "accepted": ["かざる", "kazaru"],
            "displayAnswer": "かざる (kazaru)",
            "explain": "「Đồ vật để trang trí」: động từ 「かざります」 (nhóm 1) chuyển về thể Từ điển là 「かざる」."
        },
        {
            "id": 18,
            "category": "Bài 17 NPBS • Định ngữ quá khứ V-た",
            "sentence": "これは きのう 母が (作りました) [_______] 料理です。",
            "baseWord": "作りました (つくりました)",
            "accepted": ["作った", "つくった", "tsukutta"],
            "displayAnswer": "作った / つくった (tsukutta)",
            "explain": "Bổ nghĩa cho danh từ 「料理」 ở thì quá khứ: 「作りました」 ➔ thể thông thường quá khứ 「作った」."
        },
        {
            "id": 19,
            "category": "Bài 18 • Bẫy だ với tính từ đuôi な trước と思います",
            "sentence": "この 写真たては とても (すてきです) [_______] と 思います。",
            "baseWord": "すてきです",
            "accepted": ["すてきだ", "sutekida"],
            "displayAnswer": "すてきだ (sutekida)",
            "explain": "「すてき(な)」 là tính từ đuôi な, trước 「と 思います」 ở hiện tại khẳng định PHẢI thêm 「だ」: 「すてきだ」."
        },
        {
            "id": 20,
            "category": "Bài 18 • Động từ thể thông thường trước と言っていました",
            "sentence": "やまださんは「あしたの パーティーに (行きます) [_______]」と 言っていました。",
            "baseWord": "行きます (いきます)",
            "accepted": ["行く", "いく", "iku"],
            "displayAnswer": "行く / いく (iku)",
            "explain": "Trích dẫn lời người khác dùng thể thông thường trước 「と 言っていました」. 「行きます」 ➔ 「行く (いく)」."
        }
    ],
    "p4": [
        {
            "id": 21,
            "category": "Bài 17 NPBS • Mở đầu nhờ vả",
            "promptA": "「すみません、ちょっと お願いが あるんですが…。」",
            "correctBId": "B1",
            "promptB": "「はい、何ですか。どんな お願いですか。」",
            "explain": "「ちょっと お願いが あるんですが…」 là câu mở đầu kinh điển để nhờ ai giúp việc gì; đối phương đáp lại sẵn sàng lắng nghe."
        },
        {
            "id": 22,
            "category": "Bài 17 • Khen đồ mặc & Kể người tặng",
            "promptA": "「その セーター、とても よく にあって いますね。」",
            "correctBId": "B2",
            "promptB": "「ありがとうございます。去年の クリスマスに あねに もらったんです。」",
            "explain": "Khi được khen áo len hợp dáng, đáp lại bằng lời cảm ơn và giải thích nguồn gốc món quà với 「～に もらったんです」."
        },
        {
            "id": 23,
            "category": "Bài 17 & 18 • Hỏi ý kiến quà mừng đi làm",
            "promptA": "「おとうとさんの しゅうしょくの お祝い、何を あげますか。」",
            "correctBId": "B3",
            "promptB": "「会社で 毎日 使う ものとか、めいしいれとかが いいと 思います。」",
            "explain": "Tư vấn quà mừng đi làm kết hợp định ngữ 「会社で 毎日 使う もの」 và liệt kê 「～とか～とか」."
        },
        {
            "id": 24,
            "category": "Bài 18 • Cảm ơn sau khi nhận quà",
            "promptA": "「結婚の お祝いの 花びん、ありがとうございました。たいせつに します。」",
            "correctBId": "B4",
            "promptB": "「いいえ、どういたしまして。ぜひ へやに かざって くださいね。」",
            "explain": "Đáp lại lời cảm ơn nhận quà bình hoa một cách lịch sự và gợi ý đặt trang trí trong phòng."
        }
    ],
    "p5": [
        {
            "passageId": 1,
            "title": "BÀI ĐỌC 1: お祝いの しゅうかん (Thói Quen Tặng Quà - Bài 17)",
            "text": "わたしの 国では、母の 日や 父の 日に 家族で 外食を したり、カードを 書いたり します。でも、日本では バレンタイン・デーに 友だちや 会社の人にも チョコレートを あげる しゅうかんが あります。<br>きのう、日本語学校の 友だちの トムさんに「母の 日に 何を あげますか」と 聞きました。トムさんは「母は お茶が 好きですから、日本のお茶とか きっさてんの おかしとかを あげようと 思います」と 言っていました。",
            "questions": [
                {
                    "id": 25,
                    "q": "この 人の 国では、母の 日に よく 何を しますか。",
                    "options": [
                        "会社の人へ チョコレートを あげます",
                        "日本のお茶を あげます",
                        "家族で 外食を したり、カードを 書いたり します",
                        "おもちゃを あげます"
                    ],
                    "correct": 2,
                    "explain": "Đoạn đầu viết: 「わたしの 国では、母の 日や 父の 日に 家族で 外食を したり、カードを 書いたり します」."
                },
                {
                    "id": 26,
                    "q": "トムさんは 母の 日に 何を あげると 言っていましたか。",
                    "options": [
                        "日本のお茶とか おかしとか",
                        "セーターと ネックレス",
                        "花と 絵",
                        "時計と めいしいれ"
                    ],
                    "correct": 0,
                    "explain": "Tom nói: 「母は お茶が 好きですから、日本のお茶とか きっさてんの おかしとかを あげようと 思います」."
                }
            ]
        },
        {
            "passageId": 2,
            "title": "BÀI ĐỌC 2: しゅっさんの おれいの カード (Thiệp Cảm Ơn Mừng Sinh Em Bé - Bài 18)",
            "text": "会社の みなさんへ<br>先月、わたしたちの 家に 元気な あかちゃんが 生まれました。みなさんに いただいた すてきな お祝いの カードと おもちゃ、どうも ありがとうございました。あかちゃんの ものは たくさん ひつようですから、とても うれしかったです。<br>あかちゃんは 毎日 元気に よく ねたり、ミルクを 飲んだり しています。みんなで いただいた おもちゃを たいせつに 使います。また こんど、あかちゃんの 写真を 見せますね。",
            "questions": [
                {
                    "id": 27,
                    "q": "会社の みなさんは お祝いに 何を あげましたか。",
                    "options": [
                        "花びんと ゆびわ",
                        "めいしいれと スーツ",
                        "時計と えいがの チケット",
                        "お祝いの カードと おもちゃ"
                    ],
                    "correct": 3,
                    "explain": "Trong thiệp cảm ơn ghi rõ: 「みなさんに いただいた すてきな お祝いの カードと おもちゃ、どうも ありがとうございました」."
                },
                {
                    "id": 28,
                    "q": "この 人たちは もらった おもちゃを どう しますか。",
                    "options": [
                        "へやに かざりません",
                        "たいせつに 使います",
                        "友だちに あげます",
                        "会社へ 持って 行きます"
                    ],
                    "correct": 1,
                    "explain": "Trong thiệp viết: 「みんなで いただいた おもちゃを たいせつに 使います」."
                }
            ]
        }
    ],
    "p6": [
        {
            "id": 29,
            "category": "Bài 17 NPBS • Mở đầu hỏi xin tư vấn (～んですが)",
            "vi": "Tôi muốn mua đồng hồ, không biết cái nào thì tốt ạ?",
            "hint": "時計を (とけいを), 買いたい んですが, どれが いいですか",
            "modelSentence": "時計を 買いたい んですが、どれが いいですか。",
            "modelKana": "とけいを かいたい んですが、どれが いいですか。",
            "keywords": ["時計を", "買いたい", "んですが", "どれが", "いいですか"],
            "breakdown": [
                {"part": "時計を 買いたい んですが", "role": "Nêu mong muốn làm bối cảnh mở đầu (từ vựng Bài 17 & NPBS)"},
                {"part": "どれが いいですか", "role": "Hỏi xin lời khuyên chọn lựa trong nhiều đồ vật"}
            ]
        },
        {
            "id": 30,
            "category": "Bài 17 • Liệt kê quà tặng đại diện (とか～とか)",
            "vi": "Vào dịp mừng kết hôn, tôi tặng những thứ như bình hoa hay khung ảnh.",
            "hint": "結婚の お祝いに, 花びん (かびん), 写真たて (しゃしんたて), とか, あげます",
            "modelSentence": "結婚の お祝いに、花びんとか 写真たてとかを あげます。",
            "modelKana": "けっこんの おいわいに、かびんとか しゃしんたてとかを あげます。",
            "keywords": ["結婚の", "お祝いに", "花びんとか", "写真たてとか", "あげます"],
            "breakdown": [
                {"part": "結婚の お祝いに", "role": "Dịp kỷ niệm kết hôn + trợ từ 「に」"},
                {"part": "花びんとか 写真たてとかを あげます", "role": "Liệt kê các món quà tiêu biểu bằng 「とか～とか」"}
            ]
        },
        {
            "id": 31,
            "category": "Bài 18 • Bẫy だ trước と思います",
            "vi": "Tôi nghĩ rằng chiếc vòng cổ này rất tuyệt vời cho sinh nhật của mẹ.",
            "hint": "この ネックレスは, 母の 誕生日に, とても すてきだと, 思います",
            "modelSentence": "この ネックレスは 母の 誕生日に とても すてきだと 思います。",
            "modelKana": "この ネックレスは ははの たんじょうびに とても すてきだと おもいます。",
            "keywords": ["ネックレスは", "誕生日に", "すてきだと", "思います"],
            "breakdown": [
                {"part": "母の 誕生日に", "role": "Mục đích/dịp sinh nhật của mẹ"},
                {"part": "とても すてきだと 思います", "role": "Tính từ đuôi な phải có 「だ」 trước 「と 思います」"}
            ]
        },
        {
            "id": 32,
            "category": "Bài 18 • Trích dẫn nhận xét (～と言っていました)",
            "vi": "Anh Tanaka đã nói rằng bộ vest đó chắc chắn sẽ hợp với bạn.",
            "hint": "たなかさんは, その スーツは, きっと にあうと, 言っていました",
            "modelSentence": "たなかさんは その スーツは きっと にあうと 言っていました。",
            "modelKana": "たなかさんは その スーツは きっと にあうと いっていました。",
            "keywords": ["たなかさんは", "スーツ", "きっと", "にあうと", "言っていました"],
            "breakdown": [
                {"part": "その スーツは きっと にあう", "role": "Lời trích dẫn chia về thể từ điển thông thường 「にあう」"},
                {"part": "と 言っていました", "role": "Tường thuật lại điều anh Tanaka đã nói"}
            ]
        }
    ]
}


# ==============================================================================
# MÃ ĐỀ 154: THỰC CHIẾN CHIA THỂ, TRỢ TỪ & ĐỌC KANJI BÀI 15–18
# ==============================================================================
EXAM_154 = {
    "id": "154",
    "code": "154",
    "shortTitle": "Chia Thể & Kanji 15–18",
    "fullTitle": "MÃ ĐỀ 154 • THỰC CHIẾN CHIA THỂ, TRỢ TỪ & KANJI BÀI 15 - 18",
    "subtitle": "Kiểm tra phản xạ đọc-hiểu 34 chữ Hán Bài 15–18 trong ngữ cảnh thật, tránh nhầm lẫn nhóm động từ 1/2/3 và trợ từ đi kèm.",
    "badge": "⛩️ Chia Thể & Kanji",
    "p1": [
        {
            "id": 1,
            "category": "Kanji Bài 16 • Cách đọc Kanji 【週末】",
            "q": "【週末】は いつも プールで 泳いだり、外を 走ったり しています。",
            "options": ["まいしゅう", "しゅうまつ", "せんしゅう", "こんしゅう"],
            "correct": 1,
            "explain": "週 (TUẦN) + 末 (MẠT/CUỐI) đọc là 「しゅうまつ」 (cuối tuần). Cẩn thận nhầm với 毎週 (まいしゅう), 先週 (せんしゅう)."
        },
        {
            "id": 2,
            "category": "Kanji Bài 16 • Cách đọc Kanji 【水泳】",
            "q": "けんこうの ために、毎日 ジムで 【水泳】を しています。",
            "options": ["すいえい", "みずおよぎ", "すいえ", "みずえい"],
            "correct": 0,
            "explain": "水 (THỦY) + 泳 (VỊNH) ghép âm On đọc là 「すいえい」 (môn bơi lội). Nếu chia động từ mới đọc 「泳ぎます (およぎます)」."
        },
        {
            "id": 3,
            "category": "Kanji Bài 17 • Chọn Kanji đúng cho 【たんじょうび】",
            "q": "来週の 日よう日は 父の 【たんじょうび】ですから、時計を あげます。",
            "options": ["誕生", "誕生物", "誕生日", "お祝い"],
            "correct": 2,
            "explain": "「たんじょうび」 viết bằng Hán tự Bài 17 là 「誕生日」 (ĐẢN SINH NHẬT)."
        },
        {
            "id": 4,
            "category": "Kanji Bài 18 • Chọn Kanji đúng cho 【きょねん】",
            "q": "【きょねん】、家族と いっしょに 日本へ 旅行に 行きました。",
            "options": ["先年", "今年", "来年", "去年"],
            "correct": 3,
            "explain": "「きょねん」 (năm ngoái) là 「去年」 (KHỨ NIÊN). 今年 (ことし - năm nay), 来年 (らいねん - năm sau)."
        },
        {
            "id": 5,
            "category": "Bài 16 • Trợ từ đánh giá tốt/xấu cho sức khỏe",
            "q": "毎日 8時間 ねるのは 体 [____] とても いいです。",
            "options": ["を", "で", "へ", "に"],
            "correct": 3,
            "explain": "Cụm cố định: 「体 に いい / けんこう に いい」 (tốt cho cơ thể / sức khỏe), bắt buộc dùng trợ từ 「に」."
        },
        {
            "id": 6,
            "category": "Bài 15 • Bẫy chia động từ nhóm 2 【起きます】 trước といいですよ",
            "q": "「朝 なかなか 起きられないんです。」――「よる、はやく ねて、おなじ 時間に [____] と いいですよ。」",
            "options": ["起きる", "起きた", "起きます", "起きて"],
            "correct": 0,
            "explain": "「起きます (おきます)」 là động từ nhóm 2 (đuôi -きます nhưng có âm い trước ます) ➔ thể Từ điển là 「起きる (おきる)」."
        },
        {
            "id": 7,
            "category": "Bài 15 • Bẫy chia động từ 【泳ぎます】 trước ないでください",
            "q": "「ちょっと ねつが あります。」――「じゃあ、きょうは プールで [____] ください。」",
            "options": ["泳がない", "泳がないで", "泳ぎないで", "泳ぐないで"],
            "correct": 1,
            "explain": "「泳ぎます」 nhóm 1 đổi ぎ ➔ が + ない ➔ 「泳がない」, ghép 「で ください」 thành 「泳がないで ください」."
        },
        {
            "id": 8,
            "category": "Kanji Bài 18 • Phân biệt thời gian 先月 / 今月 / 来月",
            "q": "あべさんは「【らいげつ】 新しい 家に ひっこします」と 言っていました。",
            "options": ["先月", "今月", "来月", "毎月"],
            "correct": 2,
            "explain": "「らいげつ」 (tháng sau) viết là 「来月」. 先月 (せんげつ - tháng trước), 今月 (こんげつ - tháng này)."
        },
        {
            "id": 9,
            "category": "Kanji Bài 15 • Phân biệt 【足】 và 【頭】",
            "q": "きのう こうえんを 10キロ 走りましたから、きょうは 【あし】が いたいです。",
            "options": ["頭", "耳", "手", "足"],
            "correct": 3,
            "explain": "Chạy bộ 10 km khiến chân (あし) bị đau ➔ chữ Hán 「足」. 頭 (あたま - đầu), 耳 (みみ - tai), 手 (て - tay)."
        },
        {
            "id": 10,
            "category": "Bài 18 • Đọc hiểu nghĩa câu với 【来年・結婚】",
            "q": "おとうとは 「【来年】、かのじょと 結婚 [____]」と 言っていました。",
            "options": ["する", "します", "しただ", "するだ"],
            "correct": 0,
            "explain": "Trước 「と 言っていました」 dùng thể thông thường! Hành động tương lai năm sau (来年) chia về thể Từ điển: 「結婚する」."
        }
    ],
    "p2": [
        {
            "id": 11,
            "category": "Kanji L18 • Chuyến du lịch gia đình năm ngoái",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "去年、",
            "post": "とりました。",
            "chips": ["きれいな", "山で", "家族と", "写真を"],
            "correctOrder": [2, 1, 0, 3],
            "starIndex": 2,
            "starChip": "きれいな",
            "fullSentence": "去年、家族と 山で きれいな 写真を とりました。",
            "simplifiedSentence": "去年、家族と 山で きれいな 写真を とりました。",
            "explain": "Cùng gia đình 「家族と」 tại núi 「山で」 chụp ảnh đẹp 「きれいな 写真を」. Vị trí ngôi sao là [きれいな]."
        },
        {
            "id": 12,
            "category": "Kanji L16 • Thói quen đi bộ mỗi sáng",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "今朝は",
            "post": "歩きました。",
            "chips": ["元気に", "はやく", "6時に", "起きて、"],
            "correctOrder": [2, 1, 3, 0],
            "starIndex": 2,
            "starChip": "起きて、",
            "fullSentence": "今朝は 6時に はやく 起きて、元気に 歩きました。",
            "simplifiedSentence": "今朝は 6時に はやく 起きて、元気に 歩きました。",
            "explain": "Lưu ý thứ tự: 「6時に はやく 起きて、」 (dậy sớm lúc 6 giờ) + 「元気に 歩きました」. Vị trí ngôi sao là [起きて、]."
        },
        {
            "id": 13,
            "category": "Kanji L15 • Bị đau tai sau khi bơi",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "きのう",
            "post": "いたいんです。",
            "chips": ["今朝", "泳いで、", "耳が", "プールで"],
            "correctOrder": [3, 1, 0, 2],
            "starIndex": 2,
            "starChip": "今朝",
            "fullSentence": "きのう プールで 泳いで、今朝 耳が いたいんです。",
            "simplifiedSentence": "きのう プールで 泳いで、今朝 耳が いたいんです。",
            "explain": "Hành động hôm qua 「プールで 泳いで、」 ➔ kết quả sáng nay 「今朝 耳が いたいんです」. Vị trí ngôi sao là [今朝]."
        },
        {
            "id": 14,
            "category": "Kanji L17 • Bức tranh đã nhận dịp sinh nhật",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "これは",
            "post": "絵です。",
            "chips": ["もらった", "誕生日に", "わたしが", "母に"],
            "correctOrder": [1, 2, 3, 0],
            "starIndex": 2,
            "starChip": "母に",
            "fullSentence": "これは 誕生日に わたしが 母に もらった 絵です。",
            "simplifiedSentence": "これは 誕生日に わたしが 母に もらった 絵です。",
            "explain": "Dịp 「誕生日に」 + người nhận 「わたしが」 + người tặng 「母に」 + 「もらった 絵です」. Vị trí ngôi sao là [母に]."
        },
        {
            "id": 15,
            "category": "Kanji L18 • Dự định năm sau",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "あねは",
            "post": "言っていました。",
            "chips": ["家へ", "来月", "ひっこすと", "大きい"],
            "correctOrder": [1, 3, 0, 2],
            "starIndex": 2,
            "starChip": "家へ",
            "fullSentence": "あねは 来月 大きい 家へ ひっこすと 言っていました。",
            "simplifiedSentence": "あねは 来月 大きい 家へ ひっこすと 言っていました。",
            "explain": "Thời gian 「来月」 + tính từ 「大きい」 bổ nghĩa 「家へ」 + 「ひっこすと」. Vị trí ngôi sao là [家へ]."
        }
    ],
    "p3": [
        {
            "id": 16,
            "category": "Bẫy động từ nhóm 1 đuôi -ります 【入ります】",
            "sentence": "かぜの ときは、おふろに (入ります) [_______] で ください。",
            "baseWord": "入ります (はいります)",
            "accepted": ["入らない", "はいらない", "hairanai"],
            "displayAnswer": "入らない / はいらない (hairanai)",
            "explain": "「入ります」 nhìn giống nhóm 2 nhưng thực chất là ĐỘNG TỪ NHÓM 1 ➔ đổi り thành ら + ない ➔ 「入らない」 (Cẩn thận bẫy 入りない!)."
        },
        {
            "id": 17,
            "category": "Bẫy động từ nhóm 1 đuôi -ります 【走ります】",
            "sentence": "足が いたい ときは、あまり 外を (走ります) [_______] で ください。",
            "baseWord": "走ります (はしります)",
            "accepted": ["走らない", "はしらない", "hashiranai"],
            "displayAnswer": "走らない / はしらない (hashiranai)",
            "explain": "「走ります」 là ĐỘNG TỪ NHÓM 1 ➔ đổi り thành ら + ない ➔ 「走らない」 (Không phải 走りない!)."
        },
        {
            "id": 18,
            "category": "Biến âm nhóm 1 đuôi ぎ 【泳ぎます ➔ 泳いだり】",
            "sentence": "夏は よく 海で (泳ぎます) [_______]、おいしい 料理を 食べたり します。",
            "baseWord": "泳ぎます (およぎます)",
            "accepted": ["泳いだり", "およいだり", "oyoidari"],
            "displayAnswer": "泳いだり / およいだり (oyoidari)",
            "explain": "Động từ nhóm 1 kết thúc bằng 「ぎ」: 泳ぎます ➔ thể Ta là 「泳いだ」 (biến âm đục だ!) ➔ 「泳いだり」."
        },
        {
            "id": 19,
            "category": "Động từ nhóm 2 【起きます ➔ 起きる】",
            "sentence": "まいにち 6時に (起きます) [_______] 人は 元気だと 思います。",
            "baseWord": "起きます (おきます)",
            "accepted": ["起きる", "おきる", "okiru"],
            "displayAnswer": "起きる / おきる (okiru)",
            "explain": "「起きます」 là động từ nhóm 2, bỏ ます thêm る ➔ 「起きる」 đứng trước bổ nghĩa cho 「人」."
        },
        {
            "id": 20,
            "category": "Bẫy nhóm 2 một âm tiết 【着ます ➔ 着ない】",
            "sentence": "わたしは 会社で あまり スーツを (着ます) [_______] 人です。",
            "baseWord": "着ます (きます)",
            "accepted": ["着ない", "きない", "kinai"],
            "displayAnswer": "着ない / きない (kinai)",
            "explain": "「着ます (きます - mặc)」 là nhóm 2 đặc biệt ➔ thể Nai là 「着ない」 (Cẩn thận không nhầm với 「来ます ➔ こない」!)."
        }
    ],
    "p4": [
        {
            "id": 21,
            "category": "Kanji L15–16 • Thói quen buổi sáng",
            "promptA": "「毎朝 何時に 起きますか。」",
            "correctBId": "B1",
            "promptB": "「6時に 起きて、30分 外を 歩きます。体に とても いいですよ。」",
            "explain": "Hỏi giờ dậy mỗi sáng (毎朝) và chia sẻ thói quen đi bộ 30 phút."
        },
        {
            "id": 22,
            "category": "Kanji L15 • Hỏi thăm triệu chứng sáng nay",
            "promptA": "「今朝は 頭が いたいんですか。」",
            "correctBId": "B2",
            "promptB": "「いいえ、きのう たくさん 歩きましたから、足が いたいんです。」",
            "explain": "Đính chính bộ phận bị đau từ 頭 (đầu) sang 足 (chân) do hôm qua đi bộ nhiều."
        },
        {
            "id": 23,
            "category": "Kanji L17 • Ảnh kỷ niệm gia đình",
            "promptA": "「いい 写真ですね。どこで とったんですか。」",
            "correctBId": "B3",
            "promptB": "「先月、家族と 海へ 行った ときに とりました。」",
            "explain": "Hỏi về bức ảnh đẹp (写真) và trả lời bằng kỷ niệm đi biển cùng gia đình tháng trước (先月・家族)."
        },
        {
            "id": 24,
            "category": "Kanji L18 • Kế hoạch năm sau",
            "promptA": "「来年は どこへ 旅行に 行くんですか。」",
            "correctBId": "B4",
            "promptB": "「今年 たくさん 仕事をして、来年は 北海道（ほっかいどう）へ 行きたいと 思います。」",
            "explain": "Khớp đúng cặp thời gian 今年 (năm nay) và 来年 (năm sau) cùng mẫu câu 「～と 思います」."
        }
    ],
    "p5": [
        {
            "passageId": 1,
            "title": "BÀI ĐỌC 1: 今朝の メモ (Nhật Ký Sức Khỏe Của Chị Hoa - Bài 15 & 16)",
            "text": "わたしは 先週まで あまり 元気じゃありませんでした。まいにち 夜 おそくまで 仕事をして いましたから、目と 頭が いたかったんです。<br>でも、今週から 毎日 6時に 起きて、30分 こうえんを 歩いたり 走ったり しています。そして、週末は 家族と プールで 泳ぎます。今朝は 体も 気もちも とても 元気です。",
            "questions": [
                {
                    "id": 25,
                    "q": "先週まで、どうして この 人は 元気じゃありませんでしたか。",
                    "options": [
                        "夜 おそくまで 仕事をして、目と 頭が いたかったからです",
                        "週末に 泳ぎましたから",
                        "毎日 6時に 起きましたから",
                        "こうえんを 走りませんでしたから"
                    ],
                    "correct": 0,
                    "explain": "Bài đọc nêu: 「まいにち 夜 おそくまで 仕事をして いましたから、目と 頭が いたかったんです」."
                },
                {
                    "id": 26,
                    "q": "今週から 毎日 何を して いますか。",
                    "options": [
                        "夜 おそくまで 仕事を しています",
                        "会社を 休んで います",
                        "くすりを 飲んで ねています",
                        "6時に 起きて、こうえんを 歩いたり 走ったり しています"
                    ],
                    "correct": 3,
                    "explain": "Bài đọc viết: 「今週から 毎日 6時に 起きて、30分 こうえんを 歩いたり 走ったり しています」."
                }
            ]
        },
        {
            "passageId": 2,
            "title": "BÀI ĐỌC 2: 先月の お祝いパーティー (Tiệc Mừng Tháng Trước - Bài 17 & 18)",
            "text": "先月、あねが 結婚しました。来月、あたらしい 家へ ひっこします。<br>先週の 土よう日、家族 みんなで お祝いの パーティーを しました。父は 花と お金を あげました。わたしは「あねは 写真が 好きだ」と 思いましたから、すてきな 写真たてを あげました。あねは「ありがとう！とても いい 写真たてですね。たいせつに します」と 言っていました。来年も また 家族で 楽しく 会いたいと 思います。",
            "questions": [
                {
                    "id": 27,
                    "q": "あねは いつ あたらしい 家へ ひっこしますか。",
                    "options": [
                        "先月",
                        "来月",
                        "先週",
                        "来年"
                    ],
                    "correct": 1,
                    "explain": "Bài đọc viết ngay câu thứ hai: 「来月、あたらしい 家へ ひっこします」."
                },
                {
                    "id": 28,
                    "q": "この 人は あねに 何を あげましたか。",
                    "options": [
                        "花と お金",
                        "時計",
                        "写真たて",
                        "絵"
                    ],
                    "correct": 2,
                    "explain": "Bài đọc viết: 「わたしは『あねは 写真が 好きだ』と 思いましたから、すてきな 写真たてを あげました」 (Hoa và tiền là bố 父 tặng)."
                }
            ]
        }
    ],
    "p6": [
        {
            "id": 29,
            "category": "Kanji L16 • Mỗi sáng dậy lúc 6h & đi bộ",
            "vi": "Mỗi sáng tôi thức dậy lúc 6 giờ và đi bộ bên ngoài.",
            "hint": "毎朝 (まいあさ), 6時に 起きます (おきます), 外を 歩きます (そとを あるきます)",
            "modelSentence": "毎朝 6時に 起きて、外を 歩きます。",
            "modelKana": "まいあさ 6じに おきて、そとを あるきます。",
            "keywords": ["毎朝", "起きて", "外を", "歩きます"],
            "breakdown": [
                {"part": "毎朝 6時に 起きて", "role": "Kanji Bài 16: 毎朝 (まいあさ), 起きます (おきます)"},
                {"part": "外を 歩きます", "role": "Đi bộ qua địa điểm dùng trợ từ 「を」: 外を 歩きます"}
            ]
        },
        {
            "id": 30,
            "category": "Kanji L15 & L18 • Sáng nay tay không đau",
            "vi": "Sáng nay tôi thấy khỏe, tay và chân đều không đau.",
            "hint": "今朝 (けさ), 元気です (げんきです), 手 (て), 足 (あし), いたくないです",
            "modelSentence": "今朝は 元気です。手も 足も いたくないです。",
            "modelKana": "けさは げんきです。ても あしも いたくないです。",
            "keywords": ["今朝", "元気", "手も", "足も", "いたくないです"],
            "breakdown": [
                {"part": "今朝は 元気です", "role": "今朝 (けさ - sáng nay) thuộc Kanji Bài 18"},
                {"part": "手も 足も いたくないです", "role": "Dùng cặp trợ từ 「も…も」 phủ định cả hai bộ phận"}
            ]
        },
        {
            "id": 31,
            "category": "Kanji L17 • Chúc mừng sinh nhật bằng bức tranh",
            "vi": "Vào ngày sinh nhật tuần trước, tôi đã nhận được bức tranh từ gia đình.",
            "hint": "先週の 誕生日 (せんしゅうの たんじょうび), 家族に (かぞくに), 絵を (えを), もらいました",
            "modelSentence": "先週の 誕生日に 家族に 絵を もらいました。",
            "modelKana": "せんしゅうの たんじょうびに かぞくに えを もらいました。",
            "keywords": ["先週", "誕生日", "家族に", "絵を", "もらいました"],
            "breakdown": [
                {"part": "先週の 誕生日に", "role": "Thời gian & dịp (Kanji L17–18)"},
                {"part": "家族に 絵を もらいました", "role": "Nhận từ gia đình 「家族に」 + bức tranh 「絵」"}
            ]
        },
        {
            "id": 32,
            "category": "Kanji L18 • Năm sau nghĩ sẽ đến Nhật cùng gia đình",
            "vi": "Tôi nghĩ năm sau sẽ đi Nhật Bản cùng với gia đình.",
            "hint": "来年 (らいねん), 家族と (かぞくと), 日本へ 行く, 思います (おもいます)",
            "modelSentence": "来年、家族と 日本へ 行くと 思います。",
            "modelKana": "らいねん、かぞくと にほんへ いくと おもいます。",
            "keywords": ["来年", "家族と", "日本へ", "行くと", "思います"],
            "breakdown": [
                {"part": "来年、家族と 日本へ 行く", "role": "Dự định năm sau chia thể Từ điển thông thường 「行く」"},
                {"part": "と 思います", "role": "Thể hiện suy nghĩ bản thân (Kanji Bài 18: 思います)"}
            ]
        }
    ]
}


# ==============================================================================
# MÃ ĐỀ 155: TỔNG HỢP NÂNG CAO • BẪY SƯ PHẠM TOÀN PHẦN (BÀI 15–18)
# ==============================================================================
EXAM_155 = {
    "id": "155",
    "code": "155",
    "shortTitle": "Bẫy Tổng Hợp",
    "fullTitle": "MÃ ĐỀ 155 • TỔNG HỢP NÂNG CAO & BẪY SƯ PHẠM TOÀN PHẦN (L15–L18)",
    "subtitle": "Phối hợp đa cấu trúc trong cùng 1 câu (bệnh lý + lời khuyên, định ngữ + と思う, ～んです だ➔な) để rà soát mọi lỗi hay mất điểm.",
    "badge": "🔥 Đề Chống Bẫy Toàn Phần",
    "p1": [
        {
            "id": 1,
            "category": "Tổng hợp Bẫy L15 & L17 • Phân biệt だ ➔ な vs tính từ い",
            "q": "「きのう、どうして パーティーに 来なかったんですか。」――「すみません、ちょっと びょうき [____]。」",
            "options": ["だんです", "なんです", "のです", "だったです"],
            "correct": 1,
            "explain": "Danh từ 「びょうき」 đứng trước 「んです」 phải biến 「だ ➔ な」: 「びょうきなんです」. (Nếu đã qua hẳn dùng 「びょうきだったんです」)."
        },
        {
            "id": 2,
            "category": "Bẫy L15 • V-る といいですよ vs V-て ください vs V-ないで ください",
            "q": "ストレスが ある ときは、好きな 音楽を 聞いて、ゆっくり [____] と いいですよ。",
            "options": ["リラックスして", "リラックスした", "リラックスする", "リラックスしない"],
            "correct": 2,
            "explain": "Ngay trước 「と いいですよ」 LUÔN là động từ thể Từ điển (V-る). 「リラックスします」 ➔ 「リラックスする」."
        },
        {
            "id": 3,
            "category": "Bẫy L16 NPBS • Cấm dùng ます/ません trong mệnh đề bổ nghĩa",
            "q": "会社で いちばん お酒を [____] 人は たなかさんです。",
            "options": ["飲みません", "飲まない", "飲まなくて", "飲まないで"],
            "correct": 1,
            "explain": "Mệnh đề bổ nghĩa đứng trước danh từ 「人」 KHÔNG BAO GIỜ dùng thể lịch sự 「飲みません」 mà phải chia 「飲まない」."
        },
        {
            "id": 4,
            "category": "Bẫy L17 • Phân biệt trợ từ người tặng vs người nhận",
            "q": "これは わたしが 去年 母 [____] あげた ネックレスです。",
            "options": ["から", "を", "で", "に"],
            "correct": 3,
            "explain": "Đọc kỹ động từ cuối mệnh đề là 「あげた」 (tặng CHO mẹ): người nhận luôn đi với trợ từ 「に」 (TUYỆT ĐỐI không dùng から cho あげます!)."
        },
        {
            "id": 5,
            "category": "Bẫy L17 & L16 • Định ngữ danh từ chỉ vật 【V-た もの】",
            "q": "この 写真たては、友だちが わたしの 誕生日に [____] ものです。",
            "options": ["作った", "作ります", "作って", "作りました"],
            "correct": 0,
            "explain": "Bổ nghĩa cho 「もの」 (món đồ bạn đã làm tặng vào sinh nhật): chia 「作りました」 ➔ thể thông thường quá khứ 「作った」."
        },
        {
            "id": 6,
            "category": "Bẫy L18 • Danh từ + だ + と思います",
            "q": "あしたの お祝いは きっと にぎやかな [____] と 思います。",
            "options": ["パーティー", "パーティーな", "パーティーだ", "パーティーです"],
            "correct": 2,
            "explain": "Danh từ 「パーティー」 ở thì hiện tại khẳng định khi đứng trước 「と 思います」 BẮT BUỘC thêm 「だ」: 「パーティーだと 思います」."
        },
        {
            "id": 7,
            "category": "Bẫy L18 • Tính từ đuôi い trước と言っていました (KHÔNG thêm だ)",
            "q": "トムさんは「母に あげた セーターは とても [____]」と 言っていました。",
            "options": ["あたたかいだ", "あたたかいです", "あたたかいな", "あたたかい"],
            "correct": 3,
            "explain": "Tính từ đuôi い đứng trước 「と 言っていました」 giữ nguyên 「あたたかい」 (TUYỆT ĐỐI không thêm 「だ」 như tính từ đuôi な!)."
        },
        {
            "id": 8,
            "category": "Tổng hợp L15 • Thứ tự động tác thể dục (まず / つぎに / さいごに)",
            "q": "まず うでを 上に あげます。[____]、かたを ゆっくり まわします。",
            "options": ["つぎに", "さいきん", "きゅうに", "きっと"],
            "correct": 0,
            "explain": "Chuỗi chỉ dẫn trình tự trong Bài 15: 「まず」 (đầu tiên) ➔ 「つぎに」 (tiếp theo) ➔ 「さいごに」 (cuối cùng)."
        },
        {
            "id": 9,
            "category": "Tổng hợp L17 & L18 • Liệt kê V-たり và N-とか đúng ngữ cảnh",
            "q": "パーティーの じゅんびに、花を [____]、カードの メッセージを 書いたり しました。",
            "options": ["買って", "買ったり", "買うとか", "買った"],
            "correct": 1,
            "explain": "Liệt kê các hành động (Động từ) dùng 「V1-たり、V2-たり します」: 「買って」 sai dạng ➔ phải là 「買ったり」. (Đừng nhầm với 「とか」 dùng cho danh từ!)."
        },
        {
            "id": 10,
            "category": "Tổng hợp L17 NPBS • Bẫy hỏi ngược tình huống ～んですが",
            "q": "「その 本、おもしろそうですね。」――「ええ、友だちに [____]。」",
            "options": ["かりたんです", "かりるだんです", "かりましたんです", "かりたなんです"],
            "correct": 0,
            "explain": "Động từ quá khứ 「かりました」 + 「んです」 ➔ bỏ ます chia thể thông thường quá khứ 「かりた」 + 「んです」 ➔ 「かりたんです」."
        }
    ],
    "p2": [
        {
            "id": 11,
            "category": "Tổng hợp L15 • Thư giãn với thể V-たり + といいですよ",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "つかれた",
            "post": "いいですよ。",
            "chips": ["音楽を", "とき、", "聞いたりすると", "マッサージを したり"],
            "correctOrder": [1, 3, 0, 2],
            "starIndex": 2,
            "starChip": "音楽を",
            "fullSentence": "つかれた とき、マッサージを したり 音楽を 聞いたりすると いいですよ。",
            "simplifiedSentence": "つかれたとき、マッサージを したり 音楽を 聞いたりすると いいですよ。",
            "explain": "Khi mệt 「つかれた とき、」 làm V1-たり 「マッサージを したり」 và V2-たりする 「音楽を 聞いたりする」 + 「と いいですよ」. Vị trí ngôi sao là [音楽を]."
        },
        {
            "id": 12,
            "category": "Tổng hợp L16 • Mệnh đề bổ nghĩa dài cho N",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "あそこで",
            "post": "あねの 友だちです。",
            "chips": ["話している", "着物を", "人は", "着て"],
            "correctOrder": [1, 3, 0, 2],
            "starIndex": 2,
            "starChip": "話している",
            "fullSentence": "あそこで 着物を 着て 話している 人は あねの 友だちです。",
            "simplifiedSentence": "あそこで 着物を 着て 話している 人は あねの 友だちです。",
            "explain": "Cụm mô tả người 「着物を 着て」 (mặc kimono) + 「話している」 (đang nói chuyện) đứng trước 「人は」. Vị trí ngôi sao là [話している]."
        },
        {
            "id": 13,
            "category": "Tổng hợp L17 • Mệnh đề định ngữ kết hợp nhận quà",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "わたしは",
            "post": "たいせつに 使って います。",
            "chips": ["時計を", "もらった", "誕生日に", "あねに"],
            "correctOrder": [3, 2, 1, 0],
            "starIndex": 2,
            "starChip": "もらった",
            "fullSentence": "わたしは あねに 誕生日に もらった 時計を たいせつに 使って います。",
            "simplifiedSentence": "わたしは あねに 誕生日に もらった 時計を たいせつに 使っています。",
            "explain": "Định ngữ quá khứ 「あねに 誕生日に もらった」 đứng ngay trước danh từ 「時計を」 (chiếc đồng hồ đã nhận từ chị vào ngày sinh nhật). Vị trí ngôi sao là [もらった]."
        },
        {
            "id": 14,
            "category": "Tổng hợp L18 • Trích dẫn có tính từ đuôi な + だ",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "あべさんは",
            "post": "言っていました。",
            "chips": ["今、", "とても", "しあわせだと", "友だちに"],
            "correctOrder": [3, 0, 1, 2],
            "starIndex": 2,
            "starChip": "とても",
            "fullSentence": "あべさんは 友だちに 今、とても しあわせだと 言っていました。",
            "simplifiedSentence": "あべさんは 友だちに 今、とても しあわせだと 言っていました。",
            "explain": "Nói với bạn 「友だちに」 + nội dung trích dẫn 「今、とても しあわせだと」 (lưu ý 「だ」 sau tính từ な 「しあわせ」) + 「言っていました」. Vị trí ngôi sao là [とても]."
        },
        {
            "id": 15,
            "category": "Tổng hợp L15 & L16 • Khuyên không nên dùng thang máy",
            "prompt": "Sắp xếp các cụm từ sau thành câu hoàn chỉnh và tìm từ ở vị trí ngôi sao [ ★ ]:",
            "pre": "けんこうの ために、",
            "post": "歩くと いいですよ。",
            "chips": ["エレベーターを", "会社でも", "かいだんを", "使わないで、"],
            "correctOrder": [1, 0, 3, 2],
            "starIndex": 2,
            "starChip": "使わないで、",
            "fullSentence": "けんこうの ために、会社でも エレベーターを 使わないで、かいだんを 歩くと いいですよ。",
            "simplifiedSentence": "けんこうのために、会社でも エレベーターを 使わないで、かいだんを 歩くと いいですよ。",
            "explain": "Ở công ty cũng 「会社でも」 + không dùng thang máy 「エレベーターを 使わないで、」 + đi cầu thang bộ 「かいだんを 歩くと いいですよ」. Vị trí ngôi sao là [使わないで、]."
        }
    ],
    "p3": [
        {
            "id": 16,
            "category": "Bẫy L17 NPBS • Danh từ trước んです (だ ➔ な)",
            "sentence": "「きのう どうして 会社を 休んだんですか。」――「ねつが あって、(かぜです) [_______] んです。」",
            "baseWord": "かぜです",
            "accepted": ["かぜな", "kazena"],
            "displayAnswer": "かぜな (kazena)",
            "explain": "Danh từ 「かぜ」 đứng trước 「んです」 phải đổi 「だ ➔ な」 thành 「かぜなんです」."
        },
        {
            "id": 17,
            "category": "Bẫy L15 • Chia thể ない động từ nhóm 1 【飲みます】",
            "sentence": "おなかが いたい ときは、つめたい 飲み物を (飲みます) [_______] で ください。",
            "baseWord": "飲みます (のみます)",
            "accepted": ["飲まない", "のまない", "nomanai"],
            "displayAnswer": "飲まない / のまない (nomanai)",
            "explain": "Dặn đừng uống đồ lạnh: 「飲みます」 (nhóm 1) đổi み ➔ ま + ない thành 「飲まない」."
        },
        {
            "id": 18,
            "category": "Bẫy L16 NPBS • Chia phủ định thông thường 【すいます】",
            "sentence": "ここは たばこを (すいます) [_______] 人が 多い 会社です。",
            "baseWord": "すいます",
            "accepted": ["すわない", "suwanai"],
            "displayAnswer": "すわない (suwanai)",
            "explain": "Bổ nghĩa cho danh từ 「人」 cần thể thông thường. Phủ định của 「すいます」 là 「すわない」 (đổi い ➔ わ + ない)."
        },
        {
            "id": 19,
            "category": "Bẫy L18 • Danh từ + だ trước と思います",
            "sentence": "あしたは とても いそがしい (一日です) [_______] と 思います。",
            "baseWord": "一日です (いちにちです)",
            "accepted": ["一日だ", "いちにちだ", "ichinichida"],
            "displayAnswer": "一日だ / いちにちだ (ichinichida)",
            "explain": "Danh từ 「一日」 đứng trước 「と 思います」 ở hiện tại khẳng định bắt buộc dùng 「だ」 ➔ 「一日だと 思います」."
        },
        {
            "id": 20,
            "category": "Bẫy L18 • Động từ nhóm 3 thể Từ điển trước と思います",
            "sentence": "この おもちゃを あげたら、あかちゃんは きっと (よろこびます) [_______] と 思います。",
            "baseWord": "よろこびます",
            "accepted": ["よろこぶ", "yorokobu"],
            "displayAnswer": "よろこぶ (yorokobu)",
            "explain": "Động từ 「よろこびます」 (nhóm 1) chuyển về thể Từ điển thông thường trước 「と 思います」 là 「よろこぶ」."
        }
    ],
    "p4": [
        {
            "id": 21,
            "category": "L15 + L17 • Hỏi han khi đồng nghiệp trông mệt",
            "promptA": "「かおに 元気が ないですね。どうしたんですか。」",
            "correctBId": "B1",
            "promptB": "「すみません。きのうから こしが いたくて、よく ねられないんです。」",
            "explain": "Đối phương hỏi thăm 「どうしたんですか」 ➔ giải thích tình trạng đau lưng khó ngủ bằng 「～んです」."
        },
        {
            "id": 22,
            "category": "L16 + L18 • Nhận xét về thói quen tập gym",
            "promptA": "「週末は ジムで トレーニングを して いるんですか。」",
            "correctBId": "B2",
            "promptB": "「ええ。けんこうの ために、走ったり ストレッチを したり して います。」",
            "explain": "Đáp lại câu hỏi về thói quen tập luyện cuối tuần bằng mục đích 「けんこうの ために」 và cấu trúc 「V-たり、V-たり して います」."
        },
        {
            "id": 23,
            "category": "L17 NPBS • Mở đầu nhờ chọn quà cho mẹ",
            "promptA": "「来週 母の 誕生日なんですが、何が いいと 思いますか。」",
            "correctBId": "B3",
            "promptB": "「そうですね。きれいな 花とか すてきな ネックレスとかが いいと 思います。」",
            "explain": "Đáp lại lời nhờ tư vấn 「～んですが」 bằng gợi ý quà dùng 「～とか～とかが いいと 思います」."
        },
        {
            "id": 24,
            "category": "L18 • Kể lại nhận xét của người được tặng quà",
            "promptA": "「あべさんは お祝いの 絵を きに いりましたか。」",
            "correctBId": "B4",
            "promptB": "「はい！『とても すてきだ。毎日 へやに かざる』と 言っていましたよ。」",
            "explain": "Tường thuật lại câu nói của anh Abe dùng thể thông thường (tính từ な + だ và động từ V-る) trước 「と 言っていました」."
        }
    ],
    "p5": [
        {
            "passageId": 1,
            "title": "BÀI ĐỌC 1: 会社での リラックスの しかた (Cách Giữ Sức Khỏe Khi Làm Việc - Bài 15 & 16)",
            "text": "わたしは まいにち 会社で パソコンを 使って います。先週は 仕事が とても いそがしかったですから、ストレスが たまって たいちょうが わるかったんです。<br>それで、この スポーツクラブの トレーナーに ききました。トレーナーは「けんこうの ために、夜 おそくまで 仕事を しないで ください。まず 1時間ごとに うでを あげたり、くびを まわしたり すると いいですよ」と 言っていました。それから、会社でも エレベーターを 使わないで 歩いて います。今は とても 気もちが いいです。",
            "questions": [
                {
                    "id": 25,
                    "q": "先週、どうして この 人は たいちょうが わるかったんですか。",
                    "options": [
                        "スポーツクラブへ 行きましたから",
                        "エレベーターを 使いましたから",
                        "うでを 上に あげましたから",
                        "仕事が いそがしくて、ストレスが ありましたから"
                    ],
                    "correct": 3,
                    "explain": "Đoạn đầu viết: 「先週は 仕事が とても いそがしかったですから、ストレスが たまって たいちょうが わるかったんです」."
                },
                {
                    "id": 26,
                    "q": "トレーナーは 何と 言っていましたか。",
                    "options": [
                        "毎日 10時間 パソコンを 見ると いい",
                        "夜 おそくまで 仕事を しないで、うでを あげたり くびを まわしたり すると いい",
                        "会社で エレベーターに 乗ると いい",
                        "たばこを すうと リラックスできる"
                    ],
                    "correct": 1,
                    "explain": "Bài đọc trích dẫn: 「夜 おそくまで 仕事を しないで ください。まず … うでを あげたり、くびを まわしたり すると いいですよ」."
                }
            ]
        },
        {
            "passageId": 2,
            "title": "BÀI ĐỌC 2: 友だちの そつぎょうの お祝い (Tiệc Chia Tay Tốt Nghiệp - Bài 17 & 18)",
            "text": "来月、大学の 友だちの ミンさんが そつぎょうします。わたしたちは こんどの日よう日、みんなで お祝いの パーティーを しようと 思っています。<br>きのう 友だちと プレゼントに ついて 話しました。ミンさんは 4月から 日本の 会社で はたらきます。ですから、わたしは「毎日 会社で 使う ものが いい。めいしいれとか スーツに にあう 時計とかが いい」と 思いました。みんなも「そうだね。いい カードも 書いて、お祝いに あげよう」と 言っていました。",
            "questions": [
                {
                    "id": 27,
                    "q": "ミンさんは 4月から 何を しますか。",
                    "options": [
                        "家族と 旅行に 行きます",
                        "スポーツクラブで 泳ぎます",
                        "日本の 会社で はたらきます",
                        "大きい 家へ ひっこします"
                    ],
                    "correct": 2,
                    "explain": "Bài đọc viết rõ: 「ミンさんは 4月から 日本の 会社で はたらきます」."
                },
                {
                    "id": 28,
                    "q": "どうして めいしいれとか 時計とかを あげようと 思いましたか。",
                    "options": [
                        "毎日 会社で 使う ものだからです",
                        "ミンさんが 料理が 好きですから",
                        "へやに かざる ものですから",
                        "あかちゃんに ひつようですから"
                    ],
                    "correct": 0,
                    "explain": "Lý do được nêu trực tiếp: 「毎日 会社で 使う ものが いい。めいしいれとか … が いい」."
                }
            ]
        }
    ],
    "p6": [
        {
            "id": 29,
            "category": "Tổng hợp L15 & L17 • Giải thích hoàn cảnh với N + なんです",
            "vi": "Hôm nay là ngày sinh nhật của mẹ đấy, nên tôi muốn mua hoa và đồng hồ.",
            "hint": "きょうは 母の 誕生日 (たんじょうび), ～んです (だ➔な), 花と 時計を 買いたいんです",
            "modelSentence": "きょうは 母の 誕生日なんです。花と 時計を 買いたいんです。",
            "modelKana": "きょうは ははの たんじょうびなんです。はなと とけいを かいたいんです。",
            "keywords": ["誕生日", "なんです", "花と", "時計を", "買いたいんです"],
            "breakdown": [
                {"part": "きょうは 母の 誕生日なんです", "role": "Danh từ 「誕生日」 + 「だ ➔ な」 + 「んです」 giải thích hoàn cảnh cho người nghe"},
                {"part": "花と 時計を 買いたいんです", "role": "Trình bày ý định mua quà bằng 「V-たい ＋ んです」"}
            ]
        },
        {
            "id": 30,
            "category": "Tổng hợp L16 NPBS • Mệnh đề bổ nghĩa phủ định + と思います",
            "vi": "Tôi nghĩ người không làm quá sức thì luôn khỏe mạnh.",
            "hint": "無理を しない 人 (むりを しない ひと), いつも 元気だと (げんきだと), 思います",
            "modelSentence": "無理を しない 人は いつも 元気だと 思います。",
            "modelKana": "むりを しない ひとは いつも げんきだと おもいます。",
            "keywords": ["無理を", "しない", "人は", "元気だと", "思います"],
            "breakdown": [
                {"part": "無理を しない 人", "role": "Động từ phủ định thể thường 「しない」 bổ nghĩa đứng trước 「人」"},
                {"part": "いつも 元気だと 思います", "role": "Tính từ đuôi な 「元気」 bắt buộc thêm 「だ」 trước 「と 思います」"}
            ]
        },
        {
            "id": 31,
            "category": "Tổng hợp L17 • Đồ vật sử dụng trong công việc",
            "vi": "Chiếc hộp đựng danh thiếp mà tôi nhận từ bố, tôi đang dùng nó trong công việc mỗi ngày.",
            "hint": "父に もらった めいしいれ, 仕事で (しごとで), 毎日 使って います",
            "modelSentence": "父に もらった めいしいれは、毎日 仕事で 使って います。",
            "modelKana": "ちちに もらった めいしいれは、まいにち しごとで つかって います。",
            "keywords": ["父に", "もらった", "めいしいれ", "仕事で", "使って"],
            "breakdown": [
                {"part": "父に もらった めいしいれ", "role": "Định ngữ quá khứ 「もらった」 đứng trước danh từ 「めいしいれ」"},
                {"part": "毎日 仕事で 使って います", "role": "Nơi/phương tiện làm việc đi với trợ từ 「で」"}
            ]
        },
        {
            "id": 32,
            "category": "Tổng hợp L18 • Trích dẫn đa thông tin (～と言っていました)",
            "vi": "Anh Yamada đã nói rằng ngày mai không khỏe lắm nên sẽ nghỉ ở nhà.",
            "hint": "やまださんは, あした あまり 元気じゃない, うちで 休む, 言っていました",
            "modelSentence": "やまださんは「あしたは あまり 元気じゃないから、うちで 休む」と 言っていました。",
            "modelKana": "やまださんは「あしたは あまり げんきじゃないから、うちで やすむ」と いっていました。",
            "keywords": ["やまださん", "元気じゃない", "休む", "言っていました"],
            "breakdown": [
                {"part": "あまり 元気じゃないから、うちで 休む", "role": "Cả hai vế trong trích dẫn đều chia về thể thông thường"},
                {"part": "と 言っていました", "role": "Tường thuật gián tiếp lời của anh Yamada"}
            ]
        }
    ]
}
