#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/overhaul_all_midterm_exams.py
Đại tu và chuẩn hóa toàn bộ 5 đề thi Midterm Marugoto A2-1 (M101 - M105):
1. Rút gọn 100% dạng bài từ đồng nghĩa Câu 6 - 10 thành 4 lựa chọn ngắn gọn (1-4 từ) chuẩn JLPT/Marugoto.
2. Sửa toàn bộ lỗi chính tả/typo (như 'みずを かいたいです' -> 'かいたいです').
3. Xáo trộn đáp án trắc nghiệm trên cả 5 đề thi: Tỉ lệ chuẩn 25% A, 25% B, 25% C, 25% D (7 câu mỗi đáp án).
4. Đảm bảo 100% tuân thủ 86 chữ Hán đã học bài 1-10.
5. Cập nhật đồng bộ vào exam_m101_data.py -> exam_m105_data.py và tests/De_Thi_Midterm_A2_1.html.
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

# Định nghĩa các câu từ vựng Dạng 2 (Câu 6 - 10) chuẩn trắc nghiệm cho cả 5 mã đề
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

def overhaul_all():
    print("🚀 Bắt đầu quá trình đại tu chuẩn hóa toàn bộ 5 đề thi Midterm...")
    all_overhauled_exams = []

    for idx, (code, builder_fn) in enumerate(EXAM_BUILDERS.items()):
        exam = builder_fn()
        print(f"\n📦 Xử lý mã đề: [{code}] - {exam['name']}")

        # 1. Cập nhật nhóm 2 phần từ vựng (Câu 6-10)
        vocab_sec = next(s for s in exam["sections"] if s["id"] == "sec1_vocab")
        g2 = next(g for g in vocab_sec["groups"] if "DẠNG 2" in g.get("groupTitle", ""))
        new_g2_items = NEW_VOCAB_G2[code]
        
        # Đưa các câu mới vào
        converted_g2 = []
        for it in new_g2_items:
            # Kiểm tra chữ Hán nghiêm ngặt
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

        # 2. Thu thập toàn bộ 28 câu trắc nghiệm (MC)
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

        # 3. Phân bổ cân bằng đáp án A, B, C, D (7 câu mỗi chữ cái)
        keys = generate_balanced_keys(101 + idx * 43)
        counts = {0: 0, 1: 0, 2: 0, 3: 0}
        for it, target_pos in zip(mc_items, keys):
            counts[target_pos] += 1
            curr_correct_idx = it["correct"]
            correct_val = it["options"][curr_correct_idx]
            distractors = [opt for i, opt in enumerate(it["options"]) if i != curr_correct_idx]
            
            # Xây dựng new options với target_pos là đáp án đúng
            new_opts = [None]*4
            new_opts[target_pos] = correct_val
            d_idx = 0
            for slot in range(4):
                if new_opts[slot] is None:
                    new_opts[slot] = distractors[d_idx]
                    d_idx += 1
            
            it["options"] = new_opts
            it["correct"] = target_pos
            
            # Kiểm tra chữ Hán
            for opt in new_opts:
                v(opt, f"{code}.Q{it['id']}.opt")

        print(f"  ✅ Đã cân bằng 28 câu trắc nghiệm: {counts} (A:7, B:7, C:7, D:7)")

        # 4. Kiểm tra câu sao ★ (Q27-Q30)
        star_items = []
        for sec in exam["sections"]:
            for g in sec.get("groups", []):
                for it in g.get("items", []):
                    if it.get("type") == "star":
                        star_items.append(it)
            for it in sec.get("items", []):
                if it.get("type") == "star":
                    star_items.append(it)
        
        star_corrects = [it["correct"] for it in star_items]
        print(f"  ⭐ Câu sao ★ ({len(star_items)} câu) có đáp án: {star_corrects}")

        all_overhauled_exams.append(exam)

    # 5. Cập nhật const EXAMS_DATA trong tests/De_Thi_Midterm_A2_1.html
    html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tests", "De_Thi_Midterm_A2_1.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    exams_json_str = json.dumps(all_overhauled_exams, ensure_ascii=False)
    
    # Tìm vùng const EXAMS_DATA = [...];
    pattern = r"const EXAMS_DATA = \[.*?\];\s*\n\s*//"
    match = re.search(pattern, html_content, re.DOTALL)
    if not match:
        raise ValueError("Không tìm thấy const EXAMS_DATA trong file HTML!")

    replacement = f"const EXAMS_DATA = {exams_json_str};\n    \n    //"
    new_html = html_content[:match.start()] + replacement + html_content[match.end():]

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"\n🎉 Đã cập nhật thành công EXAMS_DATA vào: {html_path}")
    print(f"   Dung lượng dữ liệu mới: {len(exams_json_str)} ký tự.")

if __name__ == "__main__":
    overhaul_all()
