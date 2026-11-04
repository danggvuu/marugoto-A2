#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_mini_test_11_14.py
Tạo trang web chuyên đề Ôn Tập Mini Test Bài 11 - 14 (Marugoto A2-1 & A2-2):
- Tab 1: 📖 Lý Thuyết Toàn Diện 4 Bài (Bài 11 ➔ 14)
- Tab 2: 🎴 118 Từ Vựng Chuẩn Kèm Nút Copy Quizlet Sạch & Ẩn Nghĩa
- Tab 3: ⛩️ 30 Chữ Hán Kanji (Chiết tự, Mẹo nhớ & Từ ghép)
- Tab 4: 🎯 Đề Thi Thử Mini Test 30 Câu Trắc Nghiệm Có Bấm Giờ & Chấm Điểm Tức Thì
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

# 3. 30 Questions with well-balanced correct options (A, B, C, D)
QUIZ_DATA = [
    {
        "id": 1,
        "category": "Ngữ pháp & Rủ rê",
        "lesson": "A2-11",
        "q": "いい てんきですね。いっしょに こうえんへ [____]。",
        "options": ["行きます", "行きましょう", "行かない", "行った"],
        "correct": 1,
        "explain": "Đưa ra lời rủ rê, đề xuất cùng làm gì ta dùng thể ý chí 「V-ましょう」 (Chúng ta cùng đi nhé)."
    },
    {
        "id": 2,
        "category": "Trợ từ mang theo",
        "lesson": "A2-11",
        "q": "バーベキューの とき、肉や やさい [____] 持って行きます。",
        "options": ["を", "に", "で", "へ"],
        "correct": 0,
        "explain": "Đồ vật mang theo là tân ngữ trực tiếp của động từ 「持っていきます」, dùng trợ từ 「を」."
    },
    {
        "id": 3,
        "category": "Đề nghị giúp đỡ",
        "lesson": "A2-11",
        "q": "荷物が 重そうですね。[____]か。",
        "options": ["持ちました", "持ってください", "持ちましょう", "持っています"],
        "correct": 2,
        "explain": "Khi ngỏ ý muốn làm giúp đối phương việc gì đó, ta dùng cấu trúc 「V-ましょうか」 (Để tôi xách giúp bạn nhé?)."
    },
    {
        "id": 4,
        "category": "Chọn lựa / Quyết định",
        "lesson": "A2-11",
        "q": "A: 「何に しますか。」ー B: 「わたしは ラーメン [____] します。」",
        "options": ["を", "で", "が", "に"],
        "correct": 3,
        "explain": "Cấu trúc chọn món ăn, đồ uống hoặc đưa ra quyết định: 「N に します」 (Tôi chọn món N)."
    },
    {
        "id": 5,
        "category": "Phán đoán diện mạo",
        "lesson": "A2-12",
        "q": "この ケーキは とても [____] そうですね。",
        "options": ["おいし", "おいしい", "おいしくて", "おいしかった"],
        "correct": 0,
        "explain": "Cấu trúc phán đoán bề ngoài với Tính từ đuôi い: Bỏ đuôi 「い」 + 「そうですね」 (おいしい ➔ おいしそう)."
    },
    {
        "id": 6,
        "category": "Biến đổi tính từ",
        "lesson": "A2-12",
        "q": "レモンを 入れたので、スープが ちょっと [____] なりました。",
        "options": ["すっぱい", "すっぱく", "すっぱくて", "すっぱいに"],
        "correct": 1,
        "explain": "Tính từ đuôi い kết hợp với động từ biến đổi 「なります」: Bỏ 「い」 thay bằng 「く」 ➔ 「すっぱくなります」 (trở nên chua)."
    },
    {
        "id": 7,
        "category": "Phạm vi so sánh nhất",
        "lesson": "A2-12",
        "q": "日本の 料理の [____]で、天ぷらが いちばん 好きです。",
        "options": ["上 (うえ)", "外 (そと)", "中 (なか)", "前 (まえ)"],
        "correct": 2,
        "explain": "So sánh trong một nhóm/phạm vi: 「[Nhóm] の 中で、[A] が いちばん Adj です」 (Trong số các món ăn Nhật thì tôi thích nhất Tempura)."
    },
    {
        "id": 8,
        "category": "Phán đoán tính từ đuôi na",
        "lesson": "A2-12",
        "q": "あの レストランは いつも [____] そうですね。",
        "options": ["にぎやかな", "にぎやかに", "にぎやかだ", "にぎやか"],
        "correct": 3,
        "explain": "Tính từ đuôi な kết hợp với 「そう」: Bỏ chữ 「な」 đi trực tiếp với 「そう」 ➔ 「にぎやかそう」 (trông có vẻ nhộn nhịp)."
    },
    {
        "id": 9,
        "category": "Thể kinh nghiệm",
        "lesson": "A2-13",
        "q": "今までに 飛行機に [____] ことが ありますか。",
        "options": ["乗った", "乗る", "乗って", "乗ります"],
        "correct": 0,
        "explain": "Cấu trúc nói về trải nghiệm / kinh nghiệm trong quá khứ bắt buộc dùng động từ thể Ta: 「V-た ことが あります」."
    },
    {
        "id": 10,
        "category": "Đáp lại thể kinh nghiệm",
        "lesson": "A2-13",
        "q": "すしを 食べたことが ありますか。ー いいえ、[____]。",
        "options": ["まだ あります", "一度も ありません", "もう 食べました", "一度 あります"],
        "correct": 1,
        "explain": "Khi trả lời phủ định chưa từng làm bao giờ: 「いいえ、一度も ありません」 (Chưa từng làm một lần nào cả)."
    },
    {
        "id": 11,
        "category": "Mức độ quá đà",
        "lesson": "A2-13",
        "q": "きのうの パーティーで ビールを [____] すぎました。",
        "options": ["飲んで", "飲んだ", "飲み", "飲む"],
        "correct": 2,
        "explain": "Cấu trúc làm việc gì đó quá đà với động từ: Động từ bỏ 「ます」 + 「すぎます」 (飲みます ➔ 飲みすぎました)."
    },
    {
        "id": 12,
        "category": "Quá mức (Tính từ đuôi i)",
        "lesson": "A2-13",
        "q": "この スーツは [____]、買うことが できません。",
        "options": ["高いすぎて", "高くて", "高だすぎて", "高すぎて"],
        "correct": 3,
        "explain": "Tính từ đuôi い bỏ đuôi 「い」 ghép với すぎて (dạng nối câu): 「高すぎて」 (đắt quá nên không thể mua)."
    },
    {
        "id": 13,
        "category": "Quá mức (Tính từ đuôi na)",
        "lesson": "A2-13",
        "q": "この 部屋は [____] すぎて、ちょっと こわいです。",
        "options": ["静か", "静かな", "静かに", "静かだ"],
        "correct": 0,
        "explain": "Tính từ đuôi な kết hợp với すぎます: Bỏ hẳn chữ 「な」 ➔ 「静かすぎて」 (Quá yên tĩnh nên hơi đáng sợ)."
    },
    {
        "id": 14,
        "category": "Trợ từ công tác & Gặp gỡ",
        "lesson": "A2-13",
        "q": "来週、東京へ 出張します。そして、田中さん [____] 会います。",
        "options": ["を", "に", "で", "と"],
        "correct": 1,
        "explain": "Gặp gỡ ai đó bắt buộc đi với trợ từ 「に」: 「田中さんに 会います」."
    },
    {
        "id": 15,
        "category": "Xin phép hành động",
        "lesson": "A2-14",
        "q": "すみません、この パソコンを [____] いいですか。",
        "options": ["使って", "使うと", "使っても", "使ったら"],
        "correct": 2,
        "explain": "Cấu trúc xin phép lịch sự: 「V-ても いいですか」 (Tôi dùng cái này có được không?)."
    },
    {
        "id": 16,
        "category": "Cấm đoán & Quy tắc",
        "lesson": "A2-14",
        "q": "ここで たばこを 吸っても いいですか。ー すみません、ここでは [____]。",
        "options": ["吸ってもいいです", "吸ってください", "吸いました", "吸ってはいけません"],
        "correct": 3,
        "explain": "Khi từ chối và nêu rõ quy tắc cấm đoán: 「V-ては いけません」 (Không được phép hút thuốc)."
    },
    {
        "id": 17,
        "category": "Quy tắc nơi làm việc",
        "lesson": "A2-14",
        "q": "会議室の 中で 大声で 話し[____] いけません。",
        "options": ["ては", "ても", "たら", "れば"],
        "correct": 0,
        "explain": "Cấu trúc cấm đoán: 「V-ては いけません」."
    },
    {
        "id": 18,
        "category": "Cách sử dụng máy móc",
        "lesson": "A2-14",
        "q": "すみません、この コピー機の [____]を 教えてください。",
        "options": ["使います", "使い方 (つかいかた)", "使うこと", "使って"],
        "correct": 1,
        "explain": "Cách làm việc gì đó: Động từ bỏ ます + 「方 (かた)」 ➔ 「使い方」 (cách sử dụng, cách dùng)."
    },
    {
        "id": 19,
        "category": "Từ vựng dã ngoại",
        "lesson": "A2-11",
        "q": "ピクニックで 食べる おにぎりや おかずを 箱に 入れた ものは 何ですか。",
        "options": ["サンドイッチ", "サラダ", "お弁当 (おべんとう)", "デザート"],
        "correct": 2,
        "explain": "Cơm hộp đựng đồ ăn mang đi dã ngoại hoặc đi làm gọi là 「お弁当 (おべんとう)」."
    },
    {
        "id": 20,
        "category": "Từ vựng vị giác",
        "lesson": "A2-12",
        "q": "砂糖 (さとう)を たくさん 入れた 料理は [____] です。",
        "options": ["辛い (からい)", "苦い (にがい)", "酸っぱい (すっぱい)", "甘い (あまい)"],
        "correct": 3,
        "explain": "Đồ ăn cho nhiều đường thì có vị ngọt: 「甘い (あまい)」."
    },
    {
        "id": 21,
        "category": "Từ vựng công tác",
        "lesson": "A2-13",
        "q": "飛行機が 空港に つく ことを [____] と 言います。",
        "options": ["到着 (とうちゃく)", "出発 (しゅっぱつ)", "出張 (しゅっちょう)", "準備 (じゅんび)"],
        "correct": 0,
        "explain": "Máy bay hoặc tàu xe đến nơi an toàn gọi là 「到着 (とうちゃく)」."
    },
    {
        "id": 22,
        "category": "Từ vựng công sở",
        "lesson": "A2-14",
        "q": "書類を コピーしたり 印刷したりする 機械は [____] です。",
        "options": ["パソコン", "コピー機 (コピーき)", "キャビネット", "ファックス"],
        "correct": 1,
        "explain": "Máy photocopy trong văn phòng gọi là 「コピー機 (コピーき)」."
    },
    {
        "id": 23,
        "category": "Mượn đồ & Phép tắc",
        "lesson": "A2-14",
        "q": "ペンを 忘れましたから、同僚に ペンを [____]。",
        "options": ["貸しました (かしました)", "買いました", "借りました (かりました)", "捨てました"],
        "correct": 2,
        "explain": "Mình đi mượn của người khác dùng động từ 「借ります (かります)」. Cho mượn mới là 「貸します (かします)」."
    },
    {
        "id": 24,
        "category": "Kanji Bài 11",
        "lesson": "A2-11",
        "q": "Chữ Hán 「持」 trong 「持っていきます」 có âm Hán Việt là gì?",
        "options": ["Đặc", "Đợi", "Thời", "Trì"],
        "correct": 3,
        "explain": "Chữ 持 có âm Hán Việt là 「Trì」 (cầm, giữ, duy trì). Chiết tự: Tay 扌 nắm giữ ngôi chùa 寺."
    },
    {
        "id": 25,
        "category": "Kanji Bài 12",
        "lesson": "A2-12",
        "q": "Từ 「料理 (りょうり)」 được ghép từ 2 chữ Hán nào?",
        "options": ["Liệu (料) + Lý (理)", "Khoa (科) + Lý (理)", "Liệu (料) + Dã (野)", "Vị (味) + Lý (理)"],
        "correct": 0,
        "explain": "「料理」 ghép từ chữ 料 (Liệu - nguyên liệu) và 理 (Lý - xử lý, lý lẽ)."
    },
    {
        "id": 26,
        "category": "Kanji Bài 12",
        "lesson": "A2-12",
        "q": "Chữ Hán 「野」 trong 「野菜 (やさい - rau xanh)」 có âm Hán Việt là gì?",
        "options": ["Thái", "Dã", "Lý", "Lâm"],
        "correct": 1,
        "explain": "Chữ 野 có âm Hán Việt là 「Dã」 (đồng dã, hoang dã, dã ngoại)."
    },
    {
        "id": 27,
        "category": "Kanji Bài 13",
        "lesson": "A2-13",
        "q": "Từ 「出発」 (Khởi hành) có cách đọc Hiragana là gì?",
        "options": ["しゅつはつ", "とうちゃく", "しゅっぱつ", "はっしゃ"],
        "correct": 2,
        "explain": "「出発」 ghép từ 出 (Xuất - しゅつ) và 発 (Phát - はつ) biến âm ngắt thành 「しゅっぱつ」."
    },
    {
        "id": 28,
        "category": "Kanji Bài 14",
        "lesson": "A2-14",
        "q": "Chữ Hán 「使」 trong 「使います (つかいます - dùng, sử dụng)」 có âm Hán Việt là gì?",
        "options": ["Tiện", "Lại", "Trừ", "Sử / Sứ"],
        "correct": 3,
        "explain": "Chữ 使 có âm Hán Việt là 「Sử / Sứ」 (sử dụng, sứ giả). Chiết tự: Người 亻 gánh vác việc quan 吏."
    },
    {
        "id": 29,
        "category": "Đọc hiểu hội thoại",
        "lesson": "A2-14",
        "q": "A: 「課長、この 資料を 見ても いいですか。」ー B: 「ええ、[____]。」",
        "options": ["どうぞ", "だめです", "すみません", "失礼します"],
        "correct": 0,
        "explain": "Khi cấp dưới hỏi xin phép xem tài liệu, cấp trên đồng ý một cách lịch sự sẽ đáp: 「ええ、どうぞ」 (Vâng, xin mời cứ xem)."
    },
    {
        "id": 30,
        "category": "Văn hóa & Đời sống",
        "lesson": "A2-13",
        "q": "Khi đi công tác hoặc đi du lịch về, người Nhật thường mua quà gì tặng đồng nghiệp trong công ty?",
        "options": ["手土産 (てみやげ)", "お土産 (おみやげ)", "お祝い (おいわい)", "プレゼント"],
        "correct": 1,
        "explain": "Món quà đặc sản địa phương mua về sau chuyến công tác hay du lịch để chia cho mọi người trong cơ quan được gọi là 「お土産 (おみやげ)」."
    }
]

# Build JSON Data Strings
vocab_json_str = json.dumps(vocab_11_14, ensure_ascii=False)
kanji_json_str = json.dumps(kanji_11_14, ensure_ascii=False)
quiz_json_str = json.dumps(QUIZ_DATA, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Cẩm Nang Toàn Diện & Mini Test Bài 11 - 14 (Marugoto A2-1 & A2-2)</title>
    <meta name="description" content="Hệ thống toàn diện Lý thuyết chuyên sâu Bài 11 - 14, 118 Từ vựng chuẩn Marugoto kèm Quizlet, 30 Chữ Hán Kanji, 30 Câu trắc nghiệm thi thử có giải thích & Cẩm nang bỏ túi.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="../assets/js/audio-engine.js"></script>
    <style>
        :root {{
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
            --shadow-md: 0 4px 12px rgba(0,0,0,0.07);
            --shadow-lg: 0 12px 28px rgba(0,0,0,0.09);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}

        body {{
            background-color: #f8fafc;
            color: var(--gray-800);
            line-height: 1.6;
            padding: 20px 12px 60px 12px;
        }}

        .jp-text {{
            font-family: 'Noto Sans JP', sans-serif;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        /* Global Hub Nav */
        .global-hub-nav {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 16px;
            background: #ffffff;
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-md);
            margin-bottom: 20px;
            box-shadow: var(--shadow-sm);
            overflow-x: auto;
            scrollbar-width: none;
        }}
        .global-hub-nav::-webkit-scrollbar {{
            display: none;
        }}
        .hub-nav-item {{
            text-decoration: none;
            color: var(--gray-600);
            font-size: 0.88rem;
            font-weight: 700;
            padding: 6px 14px;
            border-radius: var(--radius-full);
            white-space: nowrap;
            background: transparent;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .hub-nav-item:hover {{
            background: var(--gray-100);
            color: var(--primary);
        }}
        .hub-nav-item.active-hub {{
            background: var(--primary-light);
            color: var(--primary);
        }}
        .hub-dropdown {{
            position: relative;
            display: inline-block;
        }}
        .hub-dropdown-menu {{
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            z-index: 1000;
            background: #ffffff;
            min-width: 280px;
            max-height: 480px;
            overflow-y: auto;
            box-shadow: var(--shadow-lg);
            border-radius: var(--radius-md);
            border: 1px solid var(--gray-200);
            padding: 8px 0;
            margin-top: 6px;
        }}
        .hub-dropdown-menu.show {{
            display: block;
        }}
        .hub-drop-link {{
            display: block;
            padding: 9px 18px;
            color: var(--gray-700);
            text-decoration: none;
            font-size: 0.88rem;
            font-weight: 600;
            transition: all 0.15s;
        }}
        .hub-drop-link:hover {{
            background: var(--gray-50);
            color: var(--primary);
        }}
        .hub-drop-link.active {{
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 700;
        }}

        /* Hero Header */
        .hero-header {{
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
            color: var(--white);
            padding: 36px 24px;
            border-radius: var(--radius-lg);
            text-align: center;
            margin-bottom: 24px;
            box-shadow: 0 10px 30px rgba(49, 46, 129, 0.25);
            position: relative;
            overflow: hidden;
        }}
        .hero-header::before {{
            content: "合格";
            position: absolute;
            right: -20px;
            bottom: -30px;
            font-size: 8rem;
            font-weight: 900;
            color: rgba(255, 255, 255, 0.05);
            font-family: 'Noto Sans JP', sans-serif;
            pointer-events: none;
        }}
        .hero-badge {{
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
            text-transform: uppercase;
            margin-bottom: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .hero-title {{
            font-size: 2.1rem;
            font-weight: 800;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
        }}
        .hero-desc {{
            font-size: 1.05rem;
            color: #c7d2fe;
            max-width: 820px;
            margin: 0 auto 20px auto;
        }}
        .hero-stats {{
            display: flex;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
        }}
        .stat-pill {{
            background: rgba(255, 255, 255, 0.12);
            padding: 8px 18px;
            border-radius: var(--radius-full);
            font-size: 0.88rem;
            font-weight: 600;
            border: 1px solid rgba(255, 255, 255, 0.18);
        }}

        /* Tab Navigation Bar */
        .tab-nav-wrapper {{
            position: sticky;
            top: 12px;
            z-index: 100;
            background: rgba(255, 255, 255, 0.94);
            backdrop-filter: blur(12px);
            padding: 8px;
            border-radius: var(--radius-lg);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(226, 232, 240, 0.8);
            margin-bottom: 25px;
        }}
        .tab-nav {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            scrollbar-width: none;
        }}
        .tab-nav::-webkit-scrollbar {{
            display: none;
        }}
        .tab-btn {{
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
        }}
        .tab-btn:hover {{
            color: var(--primary);
            background: var(--gray-100);
        }}
        .tab-btn.active {{
            background: var(--primary);
            color: var(--white);
            box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3);
        }}

        /* Tab Content Panels */
        .tab-panel {{
            display: none;
            animation: fadeIn 0.25s ease;
        }}
        .tab-panel.active {{
            display: block;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Card Common */
        .content-card {{
            background: var(--white);
            border-radius: var(--radius-lg);
            border: 1px solid var(--gray-200);
            padding: 28px;
            box-shadow: var(--shadow-sm);
            margin-bottom: 25px;
        }}
        .section-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--gray-100);
            flex-wrap: wrap;
            gap: 12px;
        }}
        .section-title {{
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--gray-900);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .section-badge {{
            font-size: 0.8rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: var(--radius-full);
            background: var(--primary-light);
            color: var(--primary);
        }}

        /* Grammar Styles */
        .theory-quicknav {{
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding: 4px 4px 18px 4px;
            margin-bottom: 22px;
            border-bottom: 1px dashed var(--gray-200);
            -webkit-overflow-scrolling: touch;
        }}
        .quicknav-pill {{
            padding: 6px 14px;
            border-radius: var(--radius-full);
            background: #f1f5f9;
            color: var(--gray-700);
            text-decoration: none;
            font-weight: 700;
            font-size: 0.85rem;
            white-space: nowrap;
            transition: all 0.2s ease;
            border: 1px solid var(--gray-200);
            display: inline-block;
        }}
        .quicknav-pill:hover, .quicknav-pill:active {{
            background: var(--primary);
            color: var(--white);
            border-color: var(--primary);
            transform: translateY(-1px);
        }}
        .grammar-card {{
            background: var(--white);
            border-radius: var(--radius-lg);
            border: 1px solid var(--gray-200);
            margin-bottom: 24px;
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s;
        }}
        .grammar-header {{
            background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%);
            padding: 18px 24px;
            border-bottom: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }}
        .grammar-tag {{
            background: var(--primary);
            color: var(--white);
            padding: 4px 10px;
            border-radius: var(--radius-sm);
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
        }}
        .grammar-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--gray-900);
            margin: 0;
        }}
        .grammar-body {{
            padding: 24px;
        }}
        .formula-box {{
            background: #f0fdf4;
            border-left: 5px solid var(--success);
            padding: 14px 18px;
            border-radius: var(--radius-sm);
            margin-bottom: 18px;
            font-weight: 700;
            color: #166534;
            font-size: 1.05rem;
        }}
        .grammar-explain {{
            color: var(--gray-700);
            margin-bottom: 16px;
            line-height: 1.7;
        }}
        .example-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .example-item {{
            background: var(--gray-50);
            padding: 12px 16px;
            border-radius: var(--radius-sm);
            border-left: 3px solid var(--secondary);
        }}
        .ex-jp {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--gray-900);
            margin-bottom: 4px;
        }}
        .ex-vi {{
            font-size: 0.92rem;
            color: var(--gray-600);
        }}
        .trap-box {{
            background: #fff1f2;
            border-left: 5px solid var(--accent);
            padding: 14px 18px;
            border-radius: var(--radius-sm);
            margin-top: 16px;
            color: #9f1239;
            font-size: 0.95rem;
        }}
        .trap-box strong {{
            display: block;
            margin-bottom: 4px;
            font-size: 1rem;
        }}

        /* Toolbar Filter & Search */
        .toolbar-card {{
            background: var(--white);
            border-radius: var(--radius-lg);
            border: 1px solid var(--gray-200);
            padding: 18px 22px;
            box-shadow: var(--shadow-sm);
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }}
        .filter-row {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            align-items: center;
        }}
        .filter-btn {{
            background: var(--gray-100);
            border: 1.5px solid transparent;
            color: var(--gray-700);
            padding: 7px 16px;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .filter-btn:hover {{
            border-color: var(--primary);
            color: var(--primary);
        }}
        .filter-btn.active {{
            background: var(--primary);
            color: var(--white);
            box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
        }}
        .action-row {{
            display: flex;
            gap: 12px;
            align-items: center;
            flex-wrap: wrap;
        }}
        .search-input-box {{
            flex: 1;
            min-width: 240px;
            position: relative;
        }}
        .search-input-box input {{
            width: 100%;
            padding: 10px 16px 10px 38px;
            border: 1.5px solid var(--gray-200);
            border-radius: var(--radius-md);
            font-size: 0.95rem;
            transition: all 0.2s;
            outline: none;
        }}
        .search-input-box input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
        }}
        .search-icon {{
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--gray-400);
            font-size: 1rem;
        }}
        .tool-toggle-btn {{
            background: var(--white);
            border: 1.5px solid var(--gray-200);
            padding: 9px 16px;
            border-radius: var(--radius-md);
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--gray-700);
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .tool-toggle-btn:hover {{
            border-color: var(--primary);
            color: var(--primary);
        }}
        .tool-toggle-btn.active {{
            background: #ede9fe;
            border-color: var(--primary);
            color: var(--primary);
        }}

        .btn-quizlet {{
            background: linear-gradient(135deg, #4257b2, #3ccfcf);
            color: var(--white);
            border: none;
            padding: 9px 18px;
            border-radius: var(--radius-md);
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
            box-shadow: 0 2px 8px rgba(66, 87, 178, 0.25);
        }}
        .btn-quizlet:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 14px rgba(66, 87, 178, 0.35);
            opacity: 0.95;
        }}

        .toast {{
            position: fixed;
            bottom: 25px;
            right: 25px;
            background: #1e293b;
            color: white;
            padding: 12px 22px;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.25);
            font-size: 0.95rem;
            font-weight: 600;
            display: none;
            z-index: 9999;
        }}

        /* Vocab Grid */
        .vocab-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 14px;
        }}
        .vocab-card {{
            background: var(--white);
            border-radius: var(--radius-md);
            border: 1px solid var(--gray-200);
            padding: 16px;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 10px;
            transition: all 0.2s ease;
        }}
        .vocab-card:hover {{
            border-color: var(--primary-light);
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }}
        .vocab-top {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 8px;
        }}
        .vocab-badge {{
            font-size: 0.72rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 4px;
            background: #eef2ff;
            color: #4338ca;
        }}
        .vocab-jp {{
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--gray-900);
            line-height: 1.3;
        }}
        .vocab-sub {{
            font-size: 0.85rem;
            color: var(--gray-500);
            margin-top: 2px;
        }}
        .vocab-vi {{
            font-size: 0.95rem;
            color: var(--gray-600);
            padding-top: 6px;
            border-top: 1px dashed var(--gray-200);
            transition: all 0.2s;
        }}
        .vocab-vi.hidden-meaning {{
            filter: blur(5px);
            user-select: none;
            cursor: pointer;
        }}
        .vocab-vi.hidden-meaning:hover {{
            filter: blur(0);
        }}
        .sound-btn {{
            background: #f1f5f9;
            border: none;
            width: 32px;
            height: 32px;
            border-radius: var(--radius-full);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: var(--gray-600);
            font-size: 0.85rem;
            transition: all 0.15s;
            flex-shrink: 0;
        }}
        .sound-btn:hover {{
            background: var(--primary-light);
            color: var(--primary);
            transform: scale(1.1);
        }}

        /* Kanji Cards */
        .kanji-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 18px;
        }}
        .kanji-card {{
            background: var(--white);
            border-radius: var(--radius-lg);
            border: 1px solid var(--gray-200);
            padding: 20px;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            gap: 14px;
            transition: all 0.2s;
        }}
        .kanji-card:hover {{
            border-color: var(--secondary);
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }}
        .kanji-header {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}
        .kanji-char-box {{
            width: 72px;
            height: 72px;
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border: 2px solid #86efac;
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: 900;
            color: #15803d;
            flex-shrink: 0;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
        }}
        .kanji-meta {{
            flex: 1;
        }}
        .kanji-hv {{
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--gray-900);
            line-height: 1.2;
        }}
        .kanji-meaning {{
            font-size: 0.95rem;
            color: var(--gray-600);
            margin-top: 3px;
        }}
        .kanji-sub-row {{
            display: flex;
            gap: 6px;
            margin-top: 6px;
        }}
        .kanji-tag {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 4px;
            background: #f1f5f9;
            color: var(--gray-600);
        }}
        .kanji-detail-box {{
            background: var(--gray-50);
            border-radius: var(--radius-sm);
            padding: 10px 14px;
            font-size: 0.88rem;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .kanji-reading-item strong {{
            color: var(--gray-700);
            font-size: 0.8rem;
            text-transform: uppercase;
            margin-right: 4px;
        }}
        .kanji-mnemonic {{
            background: #fffbeb;
            border-left: 3px solid var(--warning);
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 0.86rem;
            color: #92400e;
        }}
        .kanji-words {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 5px;
            border-top: 1px dashed var(--gray-200);
            padding-top: 10px;
        }}
        .kanji-word-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.88rem;
        }}
        .kw-jp {{
            font-weight: 700;
            color: var(--gray-900);
        }}
        .kw-vi {{
            color: var(--gray-600);
        }}

        /* Quiz Styles */
        .quiz-stats-card {{
            background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 100%);
            border-radius: var(--radius-lg);
            padding: 20px 24px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
            border: 1px solid #c7d2fe;
        }}
        .quiz-score-box {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .score-circle {{
            width: 58px;
            height: 58px;
            border-radius: var(--radius-full);
            background: var(--primary);
            color: var(--white);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            font-weight: 800;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.35);
        }}
        .score-info h4 {{
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--gray-900);
        }}
        .score-info p {{
            font-size: 0.88rem;
            color: var(--gray-600);
        }}
        .quiz-action-btns {{
            display: flex;
            gap: 10px;
            align-items: center;
        }}
        .timer-badge {{
            background: #ffffff;
            color: var(--primary-dark);
            border: 1.5px solid var(--primary);
            padding: 8px 16px;
            border-radius: var(--radius-md);
            font-weight: 800;
            font-size: 0.95rem;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .quiz-btn {{
            background: var(--white);
            color: var(--primary);
            border: 1.5px solid var(--primary);
            padding: 9px 18px;
            border-radius: var(--radius-md);
            font-size: 0.9rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .quiz-btn:hover {{
            background: var(--primary);
            color: var(--white);
        }}
        .quiz-btn.primary {{
            background: var(--primary);
            color: var(--white);
        }}

        .question-card {{
            background: var(--white);
            border-radius: var(--radius-md);
            border: 1px solid var(--gray-200);
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s;
        }}
        .q-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            margin-bottom: 12px;
        }}
        .q-num {{
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--primary);
            background: #eef2ff;
            padding: 3px 10px;
            border-radius: var(--radius-full);
        }}
        .q-category {{
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--gray-500);
            background: var(--gray-100);
            padding: 2px 8px;
            border-radius: 4px;
        }}
        .q-text {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--gray-900);
            margin-bottom: 16px;
            line-height: 1.4;
        }}
        .options-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 10px;
        }}
        .opt-btn {{
            background: var(--gray-50);
            border: 1.5px solid var(--gray-200);
            border-radius: var(--radius-sm);
            padding: 12px 16px;
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--gray-800);
            cursor: pointer;
            text-align: left;
            transition: all 0.15s;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .opt-btn:hover:not(:disabled) {{
            border-color: var(--primary);
            background: #fafcfe;
        }}
        .opt-key {{
            width: 24px;
            height: 24px;
            border-radius: var(--radius-full);
            background: var(--white);
            border: 1px solid var(--gray-300);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--gray-600);
            flex-shrink: 0;
        }}
        .opt-btn.correct {{
            background: #ecfdf5 !important;
            border-color: #10b981 !important;
            color: #065f46 !important;
        }}
        .opt-btn.correct .opt-key {{
            background: #10b981;
            color: white;
            border-color: #10b981;
        }}
        .opt-btn.wrong {{
            background: #fff1f2 !important;
            border-color: #f43f5e !important;
            color: #9f1239 !important;
        }}
        .opt-btn.wrong .opt-key {{
            background: #f43f5e;
            color: white;
            border-color: #f43f5e;
        }}
        .q-explain {{
            margin-top: 14px;
            padding: 12px 16px;
            background: #f0f9ff;
            border-left: 4px solid var(--secondary);
            border-radius: var(--radius-sm);
            font-size: 0.9rem;
            color: #0369a1;
            display: none;
            animation: fadeIn 0.2s ease;
        }}

        /* Cheat Sheet */
        .cheatsheet-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 18px;
        }}
        .cheat-card {{
            background: var(--white);
            border-radius: var(--radius-md);
            border: 1px solid var(--gray-200);
            padding: 20px;
            box-shadow: var(--shadow-sm);
        }}
        .cheat-badge {{
            display: inline-block;
            background: #fee2e2;
            color: #b91c1c;
            padding: 3px 9px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 800;
            margin-bottom: 8px;
        }}
        .cheat-title {{
            font-size: 1.1rem;
            font-weight: 800;
            color: var(--gray-900);
            margin-bottom: 10px;
        }}
        .cheat-content {{
            font-size: 0.92rem;
            color: var(--gray-700);
            line-height: 1.6;
        }}

        /* Responsive Mobile */
        @media (max-width: 768px) {{
            body {{
                padding: 12px 8px 40px 8px;
            }}
            .hero-header {{
                padding: 24px 16px;
                border-radius: var(--radius-md);
            }}
            .hero-title {{
                font-size: 1.5rem;
            }}
            .hero-desc {{
                font-size: 0.92rem;
            }}
            .tab-nav {{
                display: flex;
                gap: 4px;
            }}
            .tab-btn {{
                padding: 10px 12px;
                font-size: 0.85rem;
            }}
            .content-card {{
                padding: 16px;
            }}
        }}
    </style>
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
        <div class="hero-badge">⚡ Chuyên Đề Trọng Tâm • Marugoto A2-1 & A2-2</div>
        <h1 class="hero-title">🎯 Cẩm Nang & Mini Test Bài 11 - 14</h1>
        <p class="hero-desc">Tổng hợp kiến thức toàn diện 4 bài: Dã ngoại & Đề xuất (L11), Ẩm thực & Phán đoán (L12), Công tác & Kinh nghiệm (L13), Quy tắc công sở & Xin phép (L14). Hệ thống hóa từ vựng, chữ Hán chiết tự và đề thi thử 30 câu trắc nghiệm chuẩn sư phạm.</p>
        <div class="hero-stats">
            <div class="stat-pill">📚 4 Bài Học Trọng Tâm (11 ➔ 14)</div>
            <div class="stat-pill">🎴 118 Từ Vựng Chuẩn Kèm Quizlet</div>
            <div class="stat-pill">⛩️ 30 Chữ Hán Kanji Đầy Đủ Chiết Tự</div>
            <div class="stat-pill">🎯 30 Câu Trắc Nghiệm Chấm Điểm Tự Động</div>
        </div>
        <div style="margin-top: 18px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
            <button type="button" class="btn-quizlet" onclick="copyFullQuizletFormat()" style="padding: 10px 22px; font-size: 0.92rem;">
                📋 Copy Trọn Bộ 118 Từ Cho Quizlet (Bài 11 - 14)
            </button>
        </div>
    </header>

    <!-- Sticky Tab Navigation -->
    <div class="tab-nav-wrapper">
        <nav class="tab-nav">
            <button class="tab-btn active" onclick="switchMainTab('tab-theory')">📖 Lý Thuyết (Bài 11 - 14)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-vocab')">🎴 118 Từ Vựng</button>
            <button class="tab-btn" onclick="switchMainTab('tab-kanji')">⛩️ 30 Chữ Hán</button>
            <button class="tab-btn" onclick="switchMainTab('tab-quiz')">🎯 Đề Thi Thử (30 Câu)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-cheatsheet')">⚡ Cẩm Nang Bỏ Túi</button>
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
                    1. Rủ rê / Đề xuất: Động từ thể ý chí: <code>V(bỏ ます) ＋ ましょう</code><br>
                    2. Đề nghị giúp đỡ đối phương: <code>V(bỏ ます) ＋ ましょうか</code><br>
                    3. Mang theo đồ đạc: <code>[Danh từ] を 持って行きます / 持って来ます</code><br>
                    4. Đưa ra lựa chọn, quyết định: <code>[Danh từ] に します</code>
                </div>
                <p class="grammar-explain">
                    <strong>Phân tích chi tiết:</strong><br>
                    • <code>〜ましょう</code>: Khác với câu hỏi lịch sự thăm dò <code>〜ませんか</code>, cấu trúc <code>〜ましょう</code> biểu đạt sự chủ động, quả quyết khi cùng đưa ra lời kêu gọi hành động chung.<br>
                    • <code>〜ましょうか</code>: Dùng khi ta thấy đối phương đang gặp khó khăn (vác nặng, trời nóng, cần chụp ảnh) và mình chủ động ngỏ lời làm hộ.<br>
                    • <code>〜に します</code>: Mẫu câu kinh điển dùng trong nhà hàng khi nhân viên hỏi <em>「ご注文は？」</em> hoặc khi ta chốt hạ một phương án.
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
                    • <code>V-た ことがある</code>: Dùng động từ thể TA để kể về một trải nghiệm đặc biệt đã từng kinh qua trong đời, không dùng cho các thói quen hàng ngày như đánh răng, ăn sáng.<br>
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
                    • <code>V-かた</code>: Động từ bỏ ます kết hợp với chữ Hán 方 (Hán Việt: Phương) để biến thành danh từ chỉ cách thức thao tác. Trợ từ tân ngữ <code>を</code> biến thành <code>の</code>: <em>コピー機<span style="color:red">の</span> 使い方</em>.
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
                <button type="button" class="btn-quizlet" id="btnQuizletCopy" onclick="copyVocabQuizletFormat()" title="Định dạng Tab sạch 100%, không dấu cách, không ~, cực dễ gõ từ trên Quizlet">
                    📋 Copy Format Quizlet (<span id="quizletVocabCount">118</span> từ)
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
            </div>
        </div>

        <div class="kanji-grid" id="kanjiContainer">
            <!-- Render via JS -->
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: ĐỀ THI THỬ MINI TEST (30 CÂU)       -->
    <!-- ========================================== -->
    <div id="tab-quiz" class="tab-panel">

        <div class="quiz-stats-card">
            <div class="quiz-score-box">
                <div class="score-circle" id="scoreDisplay">0</div>
                <div class="score-info">
                    <h4 id="quizStatusTitle">Đề Mini Test Trọng Tâm Bài 11 - 14 (30 Câu Chuẩn Sư Phạm)</h4>
                    <p id="quizProgressText">Đã làm: 0/30 câu • Điểm số: 0%</p>
                </div>
            </div>
            <div class="quiz-action-btns">
                <div class="timer-badge">
                    ⏱️ <span id="timerText">35:00</span>
                </div>
                <button class="quiz-btn" onclick="toggleTimer()">⏸️ Tạm Dừng</button>
                <button class="quiz-btn primary" onclick="resetQuiz()">🔄 Làm Lại Đề Thi</button>
            </div>
        </div>

        <div id="questionsContainer">
            <!-- Render questions via JS -->
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

<script>
    // Data Injected from Python
    const rawVocab = {vocab_json_str};
    const rawKanji = {kanji_json_str};
    const quizData = {quiz_json_str};

    let currentVocabFilter = 'ALL';
    let currentKanjiFilter = 'ALL';
    let isMeaningHidden = false;
    let currentFilteredVocab = [...rawVocab];
    let userAnswers = {{}};

    // Timer Variables
    let totalSeconds = 35 * 60;
    let timerInterval = null;
    let isTimerRunning = true;

    // Start Timer
    function startTimer() {{
        if (timerInterval) clearInterval(timerInterval);
        timerInterval = setInterval(() => {{
            if (isTimerRunning && totalSeconds > 0) {{
                totalSeconds--;
                updateTimerDisplay();
            }} else if (totalSeconds <= 0) {{
                clearInterval(timerInterval);
                alert("⏱️ Hết thời gian làm bài! Hãy kiểm tra lại kết quả của bạn nhé.");
            }}
        }}, 1000);
    }}

    function updateTimerDisplay() {{
        const mins = Math.floor(totalSeconds / 60);
        const secs = totalSeconds % 60;
        const el = document.getElementById('timerText');
        if (el) {{
            el.innerText = `${{mins.toString().padStart(2, '0')}}:${{secs.toString().padStart(2, '0')}}`;
        }}
    }}

    function toggleTimer() {{
        isTimerRunning = !isTimerRunning;
        const btn = event.target;
        if (isTimerRunning) {{
            btn.innerText = "⏸️ Tạm Dừng";
        }} else {{
            btn.innerText = "▶️ Tiếp Tục";
        }}
    }}

    // Switch Tab
    function switchMainTab(tabId) {{
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

        const targetBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => 
            b.getAttribute('onclick') && b.getAttribute('onclick').includes(tabId)
        );
        if (targetBtn) targetBtn.classList.add('active');

        const targetPanel = document.getElementById(tabId);
        if (targetPanel) targetPanel.classList.add('active');
        window.scrollTo({{ top: 180, behavior: 'smooth' }});
    }}

    // Speak text
    function speakText(text) {{
        if (window.speakJapanese) {{
            window.speakJapanese(text);
        }} else if ('speechSynthesis' in window) {{
            const u = new SpeechSynthesisUtterance(text);
            u.lang = 'ja-JP';
            window.speechSynthesis.speak(u);
        }}
    }}

    // Render Vocab
    function renderVocab(list) {{
        const container = document.getElementById('vocabContainer');
        if (!list || list.length === 0) {{
            container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy từ vựng nào phù hợp.</div>';
            return;
        }}

        container.innerHTML = list.map(item => `
            <div class="vocab-card">
                <div class="vocab-top">
                    <div>
                        <span class="vocab-badge">${{item.l}}</span>
                        <div class="vocab-jp jp-text" style="margin-top: 4px;">${{item.kanji || item.kana}}</div>
                        ${{item.kanji && item.kanji !== item.kana ? `<div class="vocab-sub jp-text">${{item.kana}}</div>` : ''}}
                        <div class="vocab-sub">${{item.romaji}} ${{item.hv ? `• <span style="font-weight:700;">${{item.hv}}</span>` : ''}}</div>
                    </div>
                    <button class="sound-btn" onclick="speakText('${{item.kanji || item.kana}}')" title="Nghe phát âm">🔊</button>
                </div>
                <div class="vocab-vi ${{isMeaningHidden ? 'hidden-meaning' : ''}}" onclick="this.classList.toggle('hidden-meaning')">
                    ${{item.vi}}
                </div>
            </div>
        `).join('');
    }}

    function filterVocab(lesson, btn) {{
        currentVocabFilter = lesson;
        if (btn) {{
            btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        }}
        applyVocabFilter();
    }}

    function handleVocabSearch() {{
        applyVocabFilter();
    }}

    function applyVocabFilter() {{
        const keyword = document.getElementById('vocabSearchInput').value.trim().toLowerCase();
        let filtered = rawVocab;
        if (currentVocabFilter !== 'ALL') {{
            filtered = filtered.filter(w => w.l === currentVocabFilter);
        }}
        if (keyword) {{
            filtered = filtered.filter(w => 
                (w.kanji && w.kanji.toLowerCase().includes(keyword)) ||
                (w.kana && w.kana.toLowerCase().includes(keyword)) ||
                (w.romaji && w.romaji.toLowerCase().includes(keyword)) ||
                (w.hv && w.hv.toLowerCase().includes(keyword)) ||
                (w.vi && w.vi.toLowerCase().includes(keyword))
            );
        }}
        currentFilteredVocab = filtered;
        const countEl = document.getElementById('quizletVocabCount');
        if (countEl) countEl.innerText = filtered.length;
        renderVocab(filtered);
    }}

    function cleanJpTermForQuizlet(str) {{
        if (!str) return "";
        let s = str;
        s = s.replace(/[~～…\\.]/g, "");
        s = s.replace(/^[nN]が/g, "");
        s = s.replace(/^[nNpPvV][をにへとがで]/g, "");
        s = s.replace(/[vV]ましょう/g, "ましょう");
        s = s.replace(/[vV]ました/g, "");
        s = s.replace(/[vV]$/g, "");
        s = s.replace(/てください$/g, "");
        s = s.replace(/\\([^)]*を\\)/g, "").replace(/（[^）]*を）/g, "");
        s = s.replace(/\\(お\\)/g, "お").replace(/（お）/g, "お");
        s = s.replace(/\\(します\\)/g, "します").replace(/（します）/g, "します");
        s = s.replace(/\\(さん\\)/g, "").replace(/（さん）/g, "");
        s = s.replace(/\\(な\\)/g, "").replace(/（な）/g, "");
        s = s.replace(/[\\(\\)（）]/g, "");
        if (s.includes("/") || s.includes("／")) {{
            s = s.split(/[\\/／]/)[0];
        }}
        s = s.replace(/[NPVnvp]/g, "");
        s = s.replace(/[。、,，\\?？！!]/g, "");
        s = s.replace(/[\\s　]+/g, "");
        return s.trim();
    }}

    function formatQuizletVocabLine(item) {{
        const term = cleanJpTermForQuizlet(item.kanji || item.kana);
        let def = item.vi;
        if (item.kana && item.kanji && item.kanji !== item.kana) {{
            def = `[${{item.kana}}] ${{item.vi}}`;
        }}
        return `${{term}}\\t${{def}}`;
    }}

    function copyVocabQuizletFormat() {{
        if (!currentFilteredVocab || currentFilteredVocab.length === 0) {{
            showToast("Không có từ vựng nào để sao chép!");
            return;
        }}
        const text = currentFilteredVocab.map(formatQuizletVocabLine).join('\\n');
        navigator.clipboard.writeText(text).then(() => {{
            showToast(`✅ Đã copy ${{currentFilteredVocab.length}} từ vựng chuẩn Quizlet (Gõ mượt, không khoảng trắng, không ~)!`);
        }}).catch(() => {{
            fallbackCopyText(text, currentFilteredVocab.length);
        }});
    }}

    function copyFullQuizletFormat() {{
        const text = rawVocab.map(formatQuizletVocabLine).join('\\n');
        navigator.clipboard.writeText(text).then(() => {{
            showToast(`✅ Đã copy trọn bộ ${{rawVocab.length}} từ vựng (Bài 11 - 14) chuẩn Quizlet!`);
        }}).catch(() => {{
            fallbackCopyText(text, rawVocab.length);
        }});
    }}

    function fallbackCopyText(text, count) {{
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast(`✅ Đã copy ${{count}} từ vựng chuẩn Quizlet!`);
    }}

    function showToast(msg) {{
        let toast = document.getElementById('toast');
        if (!toast) {{
            toast = document.createElement('div');
            toast.id = 'toast';
            toast.className = 'toast';
            document.body.appendChild(toast);
        }}
        toast.innerText = msg;
        toast.style.display = 'block';
        setTimeout(() => {{ toast.style.display = 'none'; }}, 2800);
    }}

    function toggleHideMeaning() {{
        isMeaningHidden = !isMeaningHidden;
        const btn = document.getElementById('hideMeaningBtn');
        if (isMeaningHidden) {{
            btn.classList.add('active');
            btn.innerHTML = '👁️ Đang ẩn nghĩa (Chạm vào thẻ để xem)';
        }} else {{
            btn.classList.remove('active');
            btn.innerHTML = '👁️ Ẩn nghĩa tiếng Việt (Tự dò)';
        }}
        document.querySelectorAll('.vocab-vi').forEach(el => {{
            if (isMeaningHidden) el.classList.add('hidden-meaning');
            else el.classList.remove('hidden-meaning');
        }});
    }}

    // Render Kanji
    function renderKanji(list) {{
        const container = document.getElementById('kanjiContainer');
        if (!list || list.length === 0) {{
            container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy chữ Hán phù hợp.</div>';
            return;
        }}

        container.innerHTML = list.map(item => `
            <div class="kanji-card">
                <div class="kanji-header">
                    <div class="kanji-char-box jp-text">${{item.char}}</div>
                    <div class="kanji-meta">
                        <div class="kanji-hv">${{item.hv}}</div>
                        <div class="kanji-meaning">${{item.meaning}}</div>
                        <div class="kanji-sub-row">
                            <span class="kanji-tag">${{item.lessonName}}</span>
                            <span class="kanji-tag">${{item.strokes}} nét</span>
                        </div>
                    </div>
                </div>

                <div class="kanji-detail-box">
                    <div class="kanji-reading-item">
                        <strong>KUN:</strong> <span class="jp-text">${{item.kun || '—'}}</span>
                    </div>
                    <div class="kanji-reading-item">
                        <strong>ON:</strong> <span class="jp-text">${{item.on || '—'}}</span>
                    </div>
                    <div class="kanji-reading-item">
                        <strong>Chiết tự:</strong> <span>${{item.formula || '—'}}</span>
                    </div>
                </div>

                <div class="kanji-mnemonic">
                    💡 <strong>Mẹo nhớ:</strong> ${{item.mnemonic || '—'}}
                </div>

                <ul class="kanji-words">
                    ${{(item.examples || []).map(ex => `
                        <li class="kanji-word-item">
                            <span class="kw-jp jp-text">${{ex.word}} (${{ex.reading}})</span>
                            <span class="kw-vi">${{ex.vi}}</span>
                        </li>
                    `).join('')}}
                </ul>
            </div>
        `).join('');
    }}

    function filterKanji(lesson, btn) {{
        currentKanjiFilter = lesson;
        if (btn) {{
            btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        }}
        applyKanjiFilter();
    }}

    function handleKanjiSearch() {{
        applyKanjiFilter();
    }}

    function applyKanjiFilter() {{
        const keyword = document.getElementById('kanjiSearchInput').value.trim().toLowerCase();
        let filtered = rawKanji;
        if (currentKanjiFilter !== 'ALL') {{
            filtered = filtered.filter(k => k.lesson === currentKanjiFilter);
        }}
        if (keyword) {{
            filtered = filtered.filter(k => 
                k.char.includes(keyword) ||
                k.hv.toLowerCase().includes(keyword) ||
                k.meaning.toLowerCase().includes(keyword) ||
                (k.kun && k.kun.toLowerCase().includes(keyword)) ||
                (k.on && k.on.toLowerCase().includes(keyword))
            );
        }}
        renderKanji(filtered);
    }}

    // Render Quiz
    function renderQuiz() {{
        const container = document.getElementById('questionsContainer');
        container.innerHTML = quizData.map((item, idx) => `
            <div class="question-card" id="qCard_${{item.id}}">
                <div class="q-header">
                    <span class="q-num">Câu ${{idx + 1}} / ${{quizData.length}}</span>
                    <span class="q-category">${{item.lesson}} • ${{item.category}}</span>
                </div>
                <div class="q-text jp-text">${{item.q}}</div>
                <div class="options-list">
                    ${{item.options.map((opt, oIdx) => `
                        <button class="opt-btn" id="optBtn_${{item.id}}_${{oIdx}}" onclick="selectAnswer(${{item.id}}, ${{oIdx}})">
                            <span class="opt-key">${{['A', 'B', 'C', 'D'][oIdx]}}</span>
                            <span class="jp-text">${{opt}}</span>
                        </button>
                    `).join('')}}
                </div>
                <div class="q-explain" id="explain_${{item.id}}">
                    💡 <strong>Giải thích chi tiết:</strong> ${{item.explain}}
                </div>
            </div>
        `).join('');
    }}

    function selectAnswer(qId, selectedIdx) {{
        if (userAnswers[qId] !== undefined) return;

        userAnswers[qId] = selectedIdx;
        const qItem = quizData.find(q => q.id === qId);
        const correctIdx = qItem.correct;

        qItem.options.forEach((_, idx) => {{
            const btn = document.getElementById(`optBtn_${{qId}}_${{idx}}`);
            btn.disabled = true;
            if (idx === correctIdx) {{
                btn.classList.add('correct');
            }} else if (idx === selectedIdx) {{
                btn.classList.add('wrong');
            }}
        }});

        const explainEl = document.getElementById(`explain_${{qId}}`);
        explainEl.style.display = 'block';

        updateScore();
    }}

    function updateScore() {{
        let correctCount = 0;
        let answeredCount = Object.keys(userAnswers).length;

        quizData.forEach(q => {{
            if (userAnswers[q.id] === q.correct) {{
                correctCount++;
            }}
        }});

        const percent = Math.round((correctCount / quizData.length) * 100);
        document.getElementById('scoreDisplay').innerText = correctCount;
        document.getElementById('quizProgressText').innerText = 
            `Đã làm: ${{answeredCount}}/${{quizData.length}} câu • Tỷ lệ đúng: ${{percent}}%`;

        if (answeredCount === quizData.length) {{
            let rank = "🏆 XUẤT SẮC!";
            if (percent < 60) rank = "⚠️ CẦN ÔN TẬP THÊM!";
            else if (percent < 80) rank = "👍 KHÁ TỐT!";
            else if (percent < 90) rank = "🌟 RẤT GIỎI!";
            
            document.getElementById('quizStatusTitle').innerText = 
                `HOÀN THÀNH: ${{correctCount}}/${{quizData.length}} ĐIỂM (${{percent}}%) - ${{rank}}`;
        }}
    }}

    function resetQuiz() {{
        userAnswers = {{}};
        document.getElementById('scoreDisplay').innerText = '0';
        document.getElementById('quizStatusTitle').innerText = 'Đề Mini Test Trọng Tâm Bài 11 - 14 (30 Câu Chuẩn Sư Phạm)';
        document.getElementById('quizProgressText').innerText = `Đã làm: 0/${{quizData.length}} câu • Điểm số: 0%`;
        totalSeconds = 35 * 60;
        isTimerRunning = true;
        updateTimerDisplay();
        renderQuiz();
        window.scrollTo({{ top: document.getElementById('tab-quiz').offsetTop - 60, behavior: 'smooth' }});
    }}

    document.addEventListener('DOMContentLoaded', () => {{
        applyVocabFilter();
        renderKanji(rawKanji);
        renderQuiz();
        startTimer();
    }});
</script>
<script src="../assets/js/nav-dropdown.js"></script>
</body>
</html>
"""

output_path = os.path.join(WORKSPACE, 'tests/On_Tap_Mini_Test_A2_11_14.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated {output_path} ({len(html_content)} bytes).")
