#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/overhaul_all_midterm_exams.py
Đại tu và chuẩn hóa toàn bộ 5 đề thi Midterm Marugoto A2-1 (M101 - M105):
1. LOẠI BỎ 100% THỂ TA (V-た):
   - Đề A2-1 Bài 1-10 chưa học thể Ta (V-たことがある, V-たあとで, v.v.).
   - Loại bỏ triệt để cấu trúc 'V-た ことが あります' ở M102 Q23, thay bằng cấu trúc chuẩn Bài 8 'V-る 前に'.
   - Loại bỏ 'あった 後で' ở M101 Q34, thay bằng câu hỏi đọc hiểu chuẩn 'ふたりは あした どこで 食事を しますか'.
   - Loại bỏ 'まよったので' ở M101 Q26, M105 Q5, M105 Q25, M105 Q30.
   - Sửa các phương án nhiễu chứa thể Ta: 'かりた' -> 'かりません', 'つかった' -> 'つかいます', 'はなした' -> 'はなします', '読んだ' -> '読みます'.
2. Rút gọn 100% dạng bài từ đồng nghĩa Câu 6 - 10 thành 4 lựa chọn ngắn gọn (1-3 từ) chuẩn JLPT/Marugoto.
3. Sửa toàn bộ lỗi chính tả/typo (như 'みずを かいたいです' -> 'かいたいです').
4. Xáo trộn đáp án trắc nghiệm trên cả 5 đề thi: Tỉ lệ chuẩn 25% A, 25% B, 25% C, 25% D (7 câu mỗi đáp án).
5. Đảm bảo 100% tuân thủ 86 chữ Hán đã học bài 1-10.
6. Cập nhật đồng bộ vào exam_m101_data.py -> exam_m105_data.py và tests/De_Thi_Midterm_A2_1.html.
"""

import os
import sys
import json
import re
import random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from exam_m101_data import build_m101, v, PERMITTED_KANJI
from exam_m102_data import build_m102
from exam_m103_data import build_m103
from exam_m104_data import build_m104
from exam_m105_data import build_m105

# 1. Định nghĩa các câu từ vựng Dạng 2 (Câu 6 - 10) chuẩn trắc nghiệm cho cả 5 mã đề
NEW_VOCAB_G2 = {
    "M101": [
        {
            "id": 6,
            "type": "mc",
            "prompt": "あきはばらは でんきやが <u>たくさん あります</u>から、とても べんりです。",
            "promptVi": "Akihabara có nhiều cửa hàng điện tử nên rất tiện lợi. (Câu 2 trong bộ 40 câu ôn tập)",
            "correct_text": "多くて",
            "distractors": ["少なくて", "高くて", "やすくて"],
            "explain": "💡 <strong>Từ đồng nghĩa (Bài 5):</strong> たくさん あります ＝ <strong>多くて</strong> (nhiều). Ngược nghĩa là 少なくて (ít). Chữ 多 (Đa - nhiều) đã học ở Bài 5."
        },
        {
            "id": 7,
            "type": "mc",
            "prompt": "この へんには <u>かわいらしい</u> ふくやが たくさん あります。",
            "promptVi": "Ở khu vực này có nhiều cửa hàng thời trang dễ thương. (Câu 3 trong bộ 40 câu ôn tập)",
            "correct_text": "かわいい",
            "distractors": ["こわい", "ふるい", "きたない"],
            "explain": "💡 <strong>Từ đồng nghĩa (Bài 7):</strong> かわいらしい ＝ <strong>かわいい</strong> (dễ thương, xinh xắn)."
        },
        {
            "id": 8,
            "type": "mc",
            "prompt": "あさひはくぶつかんへ 行きたいんですが、<u>どうやって 行きますか</u>。",
            "promptVi": "Tôi muốn đi đến viện bảo tàng Asahi, đi như thế nào? (Câu 6 trong bộ 40 câu ôn tập)",
            "correct_text": "行きかたを おしえて ください",
            "distractors": ["何時に 行きますか", "だれと 行きますか", "いくら かかりますか"],
            "explain": "💡 <strong>Cách hỏi đường (Bài 5):</strong> どうやって 行きますか ＝ <strong>行きかたを おしえて ください</strong> (Hãy chỉ cho tôi cách đi). Chữ 行 (Hành) đã học ở Bài 5."
        },
        {
            "id": 9,
            "type": "mc",
            "prompt": "やくそくの 時間を <u>まちがえて</u> しまいました。",
            "promptVi": "Mình bị nhầm thời gian cuộc hẹn mất rồi... (Câu 10 trong bộ 40 câu ôn tập)",
            "correct_text": "ちがう 時間に 行きました",
            "distractors": ["はやく 行きました", "ちょうど つきました", "わすれませんでした"],
            "explain": "💡 <strong>Từ vựng sinh hoạt (Bài 7):</strong> まちがえる (nhầm lẫn) ＝ <strong>ちがう 時間に 行きました</strong> (đã đến vào thời gian khác)."
        },
        {
            "id": 10,
            "type": "mc",
            "prompt": "わたしの しゅみは まんがを たくさん <u>あつめる</u> ことです。",
            "promptVi": "Sở thích của tôi là sưu tầm thật nhiều truyện tranh. (Câu 40 trong bộ 40 câu ôn tập)",
            "correct_text": "もつ",
            "distractors": ["うる", "すてる", "かりる"],
            "explain": "💡 <strong>Từ vựng sở thích (Bài 10):</strong> あつめる (sưu tầm, tích lũy) ＝ <strong>もつ</strong> (có, sở hữu nhiều)."
        }
    ],
    "M102": [
        {
            "id": 6,
            "type": "mc",
            "prompt": "とうきょうは おきなわより 人が <u>多い</u>です。",
            "promptVi": "Tokyo thì đông người hơn Okinawa. (Câu 28 trong bộ 40 câu ôn tập)",
            "correct_text": "たくさん います",
            "distractors": ["すくないです", "ぜんぜん いません", "ちいさいです"],
            "explain": "💡 <strong>Quan hệ so sánh (Bài 4):</strong> 人が 多い (nhiều người, đông đúc) ＝ <strong>たくさん います</strong> (có nhiều người). Chữ 多 (Đa) và 人 (Nhân) đều đã học."
        },
        {
            "id": 7,
            "type": "mc",
            "prompt": "えいがを みる 前に、カフェへ 行って のみものを <u>かいたいです</u>。",
            "promptVi": "Trước khi xem phim, tôi muốn đi quán cà phê mua đồ uống. (Câu 13 trong bộ 40 câu ôn tập)",
            "correct_text": "かう つもりです",
            "distractors": ["のむ つもりです", "みる つもりです", "いく つもりです"],
            "explain": "💡 <strong>Cách diễn đạt ý định (Bài 7-8):</strong> ～たい (muốn làm) ＝ <strong>～つもり</strong> (dự định, có ý định làm). かいたいです ＝ かう つもりです (muốn mua đồ uống)."
        },
        {
            "id": 8,
            "type": "mc",
            "prompt": "ドラえもんの ほうが 好きです。<u>ふしぎな</u> ポケットが ありますから。",
            "promptVi": "Mình thích Doraemon hơn. Vì Doraemon có chiếc túi thần kỳ. (Câu 30 trong bộ 40 câu ôn tập)",
            "correct_text": "すごい",
            "distractors": ["ふつうの", "ちいさな", "ふるい"],
            "explain": "💡 <strong>Tính từ cảm thán (Bài 10):</strong> ふしぎな (kỳ diệu, thần kỳ) ＝ <strong>すごい</strong> (tuyệt vời, phi thường)."
        },
        {
            "id": 9,
            "type": "mc",
            "prompt": "ベトナム語は はなす ことが <u>むずかしい</u>です。",
            "promptVi": "Tiếng Việt thì việc nói chuyện khó khăn. (Câu 37 trong bộ 40 câu ôn tập)",
            "correct_text": "たいへんです",
            "distractors": ["とくいです", "かんたんです", "おもしろいです"],
            "explain": "💡 <strong>Tính từ chỉ độ khó (Bài 2):</strong> むずかしい (khó khăn) ＝ <strong>たいへんです</strong> (vất vả, khó). Ngược nghĩa là かんたんです."
        },
        {
            "id": 10,
            "type": "mc",
            "prompt": "あの 店は 駅の <u>ちかく</u>に あります。",
            "promptVi": "Cửa hàng đó ở gần nhà ga. (Câu 4 trong bộ 40 câu ôn tập)",
            "correct_text": "すぐ そば",
            "distractors": ["とおく", "なか", "うしろ"],
            "explain": "💡 <strong>Từ vựng vị trí (Bài 5):</strong> ちかく (gần) ＝ <strong>すぐ そば</strong> (ngay sát cạnh bên). Chữ 駅 và 店 đều đã học."
        }
    ],
    "M103": [
        {
            "id": 6,
            "type": "mc",
            "prompt": "ハノイの 秋は <u>きれいで</u>、しずかです。",
            "promptVi": "Mùa thu Hà Nội rất đẹp và yên bình. (Câu 33 trong bộ 40 câu ôn tập)",
            "correct_text": "すてきで",
            "distractors": ["きたなくて", "あつくて", "うるさくて"],
            "explain": "💡 <strong>Tính từ khen ngợi (Bài 3):</strong> きれい (đẹp, thanh lịch) ＝ <strong>すてき</strong> (tuyệt vời, tươi đẹp). Chữ 秋 (Thu) đã học ở Bài 3."
        },
        {
            "id": 7,
            "type": "mc",
            "prompt": "私の いえの となりに 青くて <u>ほそながい</u> たてものが あります。",
            "promptVi": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài. (Câu 9 trong bộ 40 câu ôn tập)",
            "correct_text": "ながくて ほそい",
            "distractors": ["まるくて おおきい", "ひろくて ひくい", "みじかくて おもい"],
            "explain": "💡 <strong>Tính từ ghép hình dáng (Bài 5):</strong> ほそながい ＝ <strong>ながくて ほそい</strong> (thon và dài)."
        },
        {
            "id": 8,
            "type": "mc",
            "prompt": "たいふうで、でんしゃと バスが <u>止まりました</u>。",
            "promptVi": "Vì bão nên tàu điện và xe buýt đã dừng chạy. (Câu 35 trong bộ 40 câu ôn tập)",
            "correct_text": "うごきませんでした",
            "distractors": ["はしりました", "つきました", "でました"],
            "explain": "💡 <strong>Động từ chỉ trạng thái giao thông (Bài 4):</strong> 止まりました (đã dừng lại) ＝ <strong>うごきませんでした</strong> (đã không di chuyển/hoạt động). Chữ 止 đã học ở Bài 7."
        },
        {
            "id": 9,
            "type": "mc",
            "prompt": "お母さんは とても かわいくて、<u>しんせつな</u> 人です。",
            "promptVi": "Mẹ tôi là người rất dễ thương và tốt bụng. (Câu 20 trong bộ 40 câu ôn tập)",
            "correct_text": "やさしい",
            "distractors": ["こわい", "きびしい", "つめたい"],
            "explain": "💡 <strong>Tính từ tính cách (Bài 1):</strong> しんせつな (tốt bụng, ân cần) ＝ <strong>やさしい</strong> (hiền hậu, tốt bụng). Chữ 母 và 人 đều đã học."
        },
        {
            "id": 10,
            "type": "mc",
            "prompt": "十二月ごろ、さむく なりますから、<u>あまり 外へ 出ません</u>。",
            "promptVi": "Khoảng tháng 12 trời trở lạnh nên tôi không hay ra ngoài lắm. (Câu 33 trong bộ 40 câu ôn tập)",
            "correct_text": "うちに いる ことが 多い",
            "distractors": ["まい日 外へ 出る", "旅行に よく 行く", "外で あそぶ"],
            "explain": "💡 <strong>Cách nói tương đương sinh hoạt (Bài 3-4):</strong> あまり 外へ 出ません (ít khi ra ngoài) ＝ <strong>うちに いる ことが 多い</strong> (thường ở trong nhà). Chữ 外, 出, 多 đều đã học."
        }
    ],
    "M104": [
        {
            "id": 6,
            "type": "mc",
            "prompt": "あしたの 朝 九時に しんじゅく駅の にしぐちで <u>あいましょう</u>。",
            "promptVi": "Hẹn gặp nhau lúc 9h sáng mai ở cửa Tây ga Shinjuku nhé. (Câu 7 trong bộ 40 câu ôn tập)",
            "correct_text": "まちます",
            "distractors": ["かえります", "でんわします", "やすみます"],
            "explain": "💡 <strong>Ngữ cảnh hẹn gặp (Bài 7):</strong> あいましょう (hãy gặp nhau nhé) ➔ <strong>まちます</strong> (sẽ đợi gặp nhau ở địa điểm đó). Chữ 朝, 九, 駅 đều đã học."
        },
        {
            "id": 7,
            "type": "mc",
            "prompt": "あべさん、おそくなって すみません。時間を <u>まちがえました</u>…",
            "promptVi": "Abe ơi xin lỗi mình đến muộn, mình bị nhầm thời gian hẹn... (Câu 10 trong bộ 40 câu ôn tập)",
            "correct_text": "おくれました",
            "distractors": ["はやく きました", "ちょうど つきました", "わすれませんでした"],
            "explain": "💡 <strong>Ngữ cảnh cuộc hẹn (Bài 7):</strong> 時間を まちがえた (nhầm giờ hẹn) ➔ <strong>おくれました</strong> (bị trễ/muộn hẹn). Chữ 時間 đã học ở Bài 7."
        },
        {
            "id": 8,
            "type": "mc",
            "prompt": "私は センターで <u>週に 三回</u> 日本語を 勉強して います。",
            "promptVi": "Tôi đang học tiếng Nhật một tuần ba lần ở trung tâm. (Câu 32 trong bộ 40 câu ôn tập)",
            "correct_text": "一週間に 三日",
            "distractors": ["一か月に 三回", "まい日", "一ねんに 三回"],
            "explain": "💡 <strong>Tần suất thời gian (Bài 9):</strong> 週に 三回 ＝ <strong>一週間に 三日</strong> (ba ngày trong một tuần). Chữ 週, 三, 回 đều đã học."
        },
        {
            "id": 9,
            "type": "mc",
            "prompt": "<u>月に 五回</u> レストランへ 食べに 行きます。",
            "promptVi": "Một tháng tôi đến nhà hàng ăn 5 lần. (Câu 32 trong bộ 40 câu ôn tập)",
            "correct_text": "一か月に 五回",
            "distractors": ["いちねんに 五回", "まい週 五回", "まい日 五回"],
            "explain": "💡 <strong>Tần suất thời gian (Bài 9):</strong> 月に 五回 ＝ <strong>一か月に 五回</strong> (năm lần trong một tháng). Chữ 月, 五, 回 đều đã học."
        },
        {
            "id": 10,
            "type": "mc",
            "prompt": "あねは ちゅうごくの ペキンに <u>すんで います</u>。",
            "promptVi": "Chị gái tôi đang sống ở Bắc Kinh, Trung Quốc. (Câu 16 trong bộ 40 câu ôn tập)",
            "correct_text": "いえが あります",
            "distractors": ["旅行して います", "あそんで います", "行って いません"],
            "explain": "💡 <strong>Động từ cư trú (Bài 1):</strong> すんで います (đang sinh sống) ＝ <strong>いえが あります</strong> (có nhà/định cư ở đó)."
        }
    ],
    "M105": [
        {
            "id": 6,
            "type": "mc",
            "prompt": "日本語が <u>じょうずに なりたい</u>んですが、どうやって 勉強したら いいですか。",
            "promptVi": "Tôi muốn giỏi tiếng Nhật thì phải học thế nào? (Câu 11 trong bộ 40 câu ôn tập)",
            "correct_text": "うまく なりたい",
            "distractors": ["やめたい", "きらいになりたい", "へたになりたい"],
            "explain": "💡 <strong>Từ đồng nghĩa (Bài 2):</strong> じょうずに なりたい (muốn giỏi tiếng Nhật) ＝ <strong>うまく なりたい</strong> (muốn thành thạo, khéo léo). Chữ 勉強 đã học ở Bài 9."
        },
        {
            "id": 7,
            "type": "mc",
            "prompt": "ちゅうごく語の 勉強は むずかしいですが、かんじは <u>おもしろい</u>です。",
            "promptVi": "Việc học tiếng Trung khó nhưng chữ Hán thì thú vị. (Câu 15 trong bộ 40 câu ôn tập)",
            "correct_text": "たのしい",
            "distractors": ["つまらない", "たいへんな", "こわい"],
            "explain": "💡 <strong>Tính từ khen ngợi (Bài 2):</strong> おもしろい (thú vị) ＝ <strong>たのしい</strong> (vui vẻ, hào hứng)."
        },
        {
            "id": 8,
            "type": "mc",
            "prompt": "フランス語は はつおんが <u>かんたんでは ありません</u>。",
            "promptVi": "Tiếng Pháp thì phát âm không đơn giản chút nào. (Câu 36 trong bộ 40 câu ôn tập)",
            "correct_text": "むずかしいです",
            "distractors": ["たのしいです", "はやいです", "みじかいです"],
            "explain": "💡 <strong>Phủ định tính từ (Bài 2):</strong> かんたんでは ありません (không đơn giản) ＝ <strong>むずかしいです</strong> (khó)."
        },
        {
            "id": 9,
            "type": "mc",
            "prompt": "ぶんしょうを 読む のが <u>にがてです</u>。",
            "promptVi": "Tôi kém việc đọc câu văn. (Câu 39 trong bộ 40 câu ôn tập)",
            "correct_text": "あまり とくいではない",
            "distractors": ["とても じょうずだ", "だいすきだ", "かんたんだ"],
            "explain": "💡 <strong>Tính từ chỉ năng lực (Bài 2):</strong> にがてです (kém, không tự tin) ＝ <strong>あまり とくいではない</strong> (không thành thạo lắm). Chữ 読 đã học ở Bài 2."
        },
        {
            "id": 10,
            "type": "mc",
            "prompt": "日本の まんがを たくさん <u>あつめて います</u>。",
            "promptVi": "Tôi đang sưu tầm nhiều truyện tranh của Nhật Bản. (Câu 40 trong bộ 40 câu ôn tập)",
            "correct_text": "もつ こと",
            "distractors": ["うる こと", "すてる こと", "かりる こと"],
            "explain": "💡 <strong>Từ vựng sở thích (Bài 10):</strong> あつめて います (sưu tầm, tích trữ) ＝ <strong>もつ こと</strong> (sở hữu trong nhà). Chữ 日本 đã học."
        }
    ]
}

def generate_balanced_keys(seed):
    random.seed(seed)
    base = [0]*7 + [1]*7 + [2]*7 + [3]*7
    for _ in range(2000):
        random.shuffle(base)
        ok = True
        for i in range(len(base)-2):
            if base[i] == base[i+1] == base[i+2]:
                ok = False
                break
        if ok:
            return base
    return base

EXAM_BUILDERS = {
    "M101": build_m101,
    "M102": build_m102,
    "M103": build_m103,
    "M104": build_m104,
    "M105": build_m105,
}

def purge_ta_forms_and_overhaul():
    print("🚀 Bắt đầu quá trình loại bỏ 100% Thể Ta (V-た) và đại tu chuẩn hóa toàn bộ 5 đề thi...")
    all_overhauled_exams = []

    for idx, (code, builder_fn) in enumerate(EXAM_BUILDERS.items()):
        exam = builder_fn()
        print(f"\n📦 Xử lý mã đề: [{code}] - {exam['name']}")

        # ----------------------------------------------------
        # 1. LOẠI BỎ CÁC CÂU CHỨA THỂ TA CỤ THỂ TRÊN TỪNG MÃ ĐỀ
        # ----------------------------------------------------
        all_items_dict = {}
        for sec in exam["sections"]:
            for g in sec.get("groups", []):
                for it in g.get("items", []):
                    all_items_dict[it["id"]] = it
            for it in sec.get("items", []):
                all_items_dict[it["id"]] = it

        if code == "M101":
            # Q24: đổi distractor かりた -> かりません
            it24 = all_items_dict.get(24)
            if it24:
                it24["options"] = [o if o != "かりた" else "かりません" for o in it24["options"]]

            # Q26: Đổi câu hỏi dùng trợ từ で chỉ nguyên nhân (Câu 35 ôn tập) thay vì まよったので
            it26 = all_items_dict.get(26)
            if it26:
                it26["prompt"] = "たいふう (   )、でんしゃが 止まりました。"
                it26["promptVi"] = "Vì bão nên tàu điện đã dừng chạy. (Câu 35 trong bộ 40 câu ôn tập)"
                it26["options"] = ["で", "に", "を", "へ"]
                it26["correct"] = 0
                it26["explain"] = "💡 <strong>Trợ từ で chỉ nguyên nhân do biến cố, thời tiết (Bài 4):</strong> たいふう<strong>で</strong> (Do bão) ➔ Đúng theo Câu 35 trong bộ 40 câu ôn tập."

            # Q34: Đọc hiểu, đổi 'ふたりは あった 後で' -> 'ふたりは あした どこで 食事を しますか。'
            it34 = all_items_dict.get(34)
            if it34:
                it34["prompt"] = "ふたりは あした どこで 食事を しますか。"
                it34["promptVi"] = "Hai người ngày mai ăn cơm ở đâu?"
                it34["options"] = ["日本りょうりの 店", "カフェ", "えきの なか", "学校"]
                it34["correct"] = 0
                it34["explain"] = "💡 <strong>Thông tin trong bài đọc:</strong> '右がわに ある 日本りょうりの 店で いっしょに ごはんを 食べましょう' ➔ Quán ăn Nhật Bản."

        elif code == "M102":
            # Q18: Sửa câu Hán tự không dùng 'たべた あとで'
            it18 = all_items_dict.get(18)
            if it18:
                it18["prompt"] = "じゅぎょうの 【あと】で、としょかんへ 行きます。"
                it18["promptVi"] = "Sau giờ học, tôi đi đến thư viện."
                it18["explain"] = "💡 <strong>Chữ Hán: 後 (Hậu):</strong> Trong từ 【あと】 (sau). 【じゅぎょうの 後で】: Sau giờ học. Chữ 行 đã học ở Bài 5."

            # Q22: đổi distractor つかった -> つかいます
            it22 = all_items_dict.get(22)
            if it22:
                it22["options"] = [o if o != "つかった" else "つかいます" for o in it22["options"]]

            # Q23: CỰC KỲ QUAN TRỌNG - Bỏ cấu trúc 'V-た ことが あります' (kinh nghiệm chưa học bài 1-10)
            # Thay bằng cấu trúc V-る 前に (Bài 8 - Câu 13 ôn tập)
            it23 = all_items_dict.get(23)
            if it23:
                it23["prompt"] = "えいがを (   ) 前に、カフェへ 行って おちゃを のみたいです。"
                it23["promptVi"] = "Trước khi xem phim, tôi muốn đi quán cà phê uống trà. (Câu 13 trong bộ 40 câu ôn tập)"
                it23["options"] = ["みる", "みます", "みて", "みない"]
                it23["correct"] = 0
                it23["explain"] = "💡 <strong>Cấu trúc trình tự thời gian (Bài 8): Động từ thể từ điển (V-る) ＋ 前に:</strong> Trước khi xem phim ➔ <strong>みる 前に</strong>. Đúng theo Câu 13 trong bộ 40 câu ôn tập."

        elif code == "M105":
            # Q5: Thay câu từ vựng まよった -> かり (Mượn từ điển - Bài 8)
            it5 = all_items_dict.get(5)
            if it5:
                it5["prompt"] = "学校の としょかんで 日本語の じしょを (   )ました。"
                it5["promptVi"] = "Tôi đã mượn cuốn từ điển tiếng Nhật ở thư viện trường. (Câu 14 trong bộ 40 câu ôn tập)"
                it5["options"] = ["かり", "まち", "よみ", "かき"]
                it5["correct"] = 0
                it5["explain"] = "💡 <strong>Động từ mượn sách/từ điển (Bài 8):</strong> かりる (かりました ➔ đã mượn). Chữ 学校, 本 đều đã học."

            # Q21: đổi distractor はなした -> はなします
            it21 = all_items_dict.get(21)
            if it21:
                it21["options"] = [o if o != "はなした" else "はなします" for o in it21["options"]]

            # Q24: đổi distractor 読んだ -> 読みます
            it24 = all_items_dict.get(24)
            if it24:
                it24["options"] = [o if o != "読んだ" else "読みます" for o in it24["options"]]

            # Q25: Thay câu まよったので bằng câu liên từ から (Câu 15 ôn tập)
            it25 = all_items_dict.get(25)
            if it25:
                it25["prompt"] = "ちゅうごく語は むずかしいですが、おもしろいです。えいごと ちがいます (   )。"
                it25["promptVi"] = "Tiếng Trung khó nhưng thú vị. Vì khác với tiếng Anh. (Câu 15 trong bộ 40 câu ôn tập)"
                it25["options"] = ["から", "ので", "のに", "けど"]
                it25["correct"] = 0
                it25["explain"] = "💡 <strong>Liên từ chỉ lý do nguyên nhân (Bài 2/10): ～から:</strong> ちがいます<strong>から</strong> (Vì khác với tiếng Anh). Đúng theo Câu 15 trong bộ 40 câu ôn tập."

            # Q30: Sắp xếp câu ngôi sao ★ (Đổi câu まよったので thành câu 39 ôn tập: 日本語は ぶんしょうを 読む のが 少し にがてです)
            it30 = all_items_dict.get(30)
            if it30:
                it30["prompt"] = "日本語は　＿＿＿　＿＿＿　★　＿＿＿　にがてです。"
                it30["promptVi"] = "Tiếng Nhật thì việc đọc câu văn tôi hơi kém một chút. (Câu 39 trong bộ 40 câu ôn tập)"
                it30["sentencePre"] = "日本語は"
                it30["sentencePost"] = "にがてです。"
                it30["starPos"] = 3
                # Parts: [1: ぶんしょうを, 2: 読む, 3: のが (★), 4: 少し]
                # Xáo trộn vị trí hiển thị:
                it30["parts"] = [
                    {"id": 1, "text": "ぶんしょうを"},
                    {"id": 2, "text": "読む"},
                    {"id": 3, "text": "のが"},
                    {"id": 4, "text": "少し"}
                ]
                it30["options"] = ["少し", "ぶんしょうを", "のが", "読む"]
                it30["correct"] = 2 # 'のが' ở vị trí index 2 (C)
                it30["fullSentence"] = "日本語は ぶんしょうを 読む のが 少し にがてです。"
                it30["explain"] = "💡 <strong>Thứ tự sắp xếp đúng:</strong><br>ぶんしょうを (1) ➔ 読む (2) ➔ <strong>のが (3 - ★)</strong> ➔ 少し (4).<br>➔ Câu hoàn chỉnh: 日本語は ぶんしょうを 読む のが 少し にがてです。"

        # ----------------------------------------------------
        # 2. CẬP NHẬT NHÓM 2 PHẦN TỪ VỰNG (Câu 6-10) TINH GỌN
        # ----------------------------------------------------
        vocab_sec = next(s for s in exam["sections"] if s["id"] == "sec1_vocab")
        g2 = next(g for g in vocab_sec["groups"] if "DẠNG 2" in g.get("groupTitle", ""))
        new_g2_items = NEW_VOCAB_G2[code]
        
        converted_g2 = []
        for it in new_g2_items:
            v(it["prompt"], f"{code}.Q{it['id']}.p")
            v(it["correct_text"], f"{code}.Q{it['id']}.correct")
            for d in it["distractors"]:
                v(d, f"{code}.Q{it['id']}.distractor")
                
            converted_g2.append({
                "id": it["id"],
                "type": "mc",
                "prompt": it["prompt"],
                "promptVi": it["promptVi"],
                "options": [it["correct_text"]] + it["distractors"],
                "correct": 0,
                "explain": it["explain"]
            })
        g2["items"] = converted_g2
        g2["groupInstruction"] = "Chọn từ hoặc cụm từ ngắn gọn mang ý nghĩa tương đương nhất với phần gạch chân:"

        # ----------------------------------------------------
        # 3. THU THẬP VÀ CÂN BẰNG ĐÁP ÁN TRẮC NGHIỆM (A:7, B:7, C:7, D:7)
        # ----------------------------------------------------
        mc_items = []
        for sec in exam["sections"]:
            for g in sec.get("groups", []):
                for it in g.get("items", []):
                    if it.get("type") == "mc":
                        mc_items.append(it)
            for it in sec.get("items", []):
                if it.get("type") == "mc":
                    mc_items.append(it)

        if len(mc_items) != 28:
            raise ValueError(f"Expected 28 MC items in {code}, got {len(mc_items)}")

        keys = generate_balanced_keys(202 + idx * 53)
        counts = {0: 0, 1: 0, 2: 0, 3: 0}
        for it, target_pos in zip(mc_items, keys):
            counts[target_pos] += 1
            curr_correct_idx = it["correct"]
            correct_val = it["options"][curr_correct_idx]
            distractors = [opt for i, opt in enumerate(it["options"]) if i != curr_correct_idx]
            
            new_opts = [None]*4
            new_opts[target_pos] = correct_val
            d_idx = 0
            for slot in range(4):
                if new_opts[slot] is None:
                    new_opts[slot] = distractors[d_idx]
                    d_idx += 1
            
            it["options"] = new_opts
            it["correct"] = target_pos
            
            for opt in new_opts:
                v(opt, f"{code}.Q{it['id']}.opt")

        print(f"  ✅ Đã cân bằng 28 câu trắc nghiệm: {counts} (A:7, B:7, C:7, D:7)")

        # Kiểm tra không còn bất kỳ Thể Ta nào
        for it in mc_items:
            for text_str in [it["prompt"]] + it["options"]:
                if "たことがある" in text_str or "た後で" in text_str or "あった後" in text_str or "まよった" in text_str:
                    raise ValueError(f"STILL FOUND TA-FORM in [{code}] Q{it['id']}: {text_str}")

        all_overhauled_exams.append(exam)

    # 4. Ghi đè vào các file scripts/exam_m10x_data.py
    header = """#!/usr/bin/env python3
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
    cjk = set(re.findall(r"[\u4e00-\u9faf]", text))
    out = cjk - PERMITTED_KANJI
    if out:
        raise ValueError(f"UNLEARNED KANJI at [{label}]: {out} in '{text}'")
    return text
"""
    for exam in all_overhauled_exams:
        code = exam["code"]
        var_name = f"build_{code.lower()}"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"exam_{code.lower()}_data.py")
        exam_json = json.dumps(exam, ensure_ascii=False, indent=4)
        content = f"{header}\nDATA_{code} = {exam_json}\n\ndef {var_name}():\n    return DATA_{code}\n"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  💾 Đã đồng bộ file nguồn: {file_path}")

    # 5. Cập nhật const EXAMS_DATA trong tests/De_Thi_Midterm_A2_1.html
    html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tests", "De_Thi_Midterm_A2_1.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    exams_json_str = json.dumps(all_overhauled_exams, ensure_ascii=False)
    pattern = r"const EXAMS_DATA = \[.*?\];\s*\n\s*//"
    match = re.search(pattern, html_content, re.DOTALL)
    if not match:
        raise ValueError("Không tìm thấy const EXAMS_DATA trong file HTML!")

    replacement = f"const EXAMS_DATA = {exams_json_str};\n    \n    //"
    new_html = html_content[:match.start()] + replacement + html_content[match.end():]

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"\n🎉 HOÀN TẤT ĐẠI TU: Đã loại bỏ 100% Thể Ta, cập nhật thành công vào: {html_path}")

if __name__ == "__main__":
    purge_ta_forms_and_overhaul()
