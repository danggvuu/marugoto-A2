# -*- coding: utf-8 -*-
"""
build_master_grammar_app.py
Generates Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html
Comprehensive Interactive Japanese Grammar Master Learning Hub
Covering 26 Lessons: Marugoto A1 (L11-18), A2-1 (L1-10), A2-2 (L11-18)
"""

import json
import os
import master_grammar_data as mgd

VERB_LAB_DATA = [
    {
        "id": "taberu",
        "kanji": "食べる",
        "kana": "たべる",
        "group": "Nhóm 2 (Động từ đuôi る)",
        "vi": "Ăn",
        "masu": "食べます",
        "ru": "食べる",
        "te": "食べて",
        "ta": "食べた",
        "nai": "食べない",
        "tara": "食べたら",
        "tari": "食べたり",
        "ex": "日本の りょうりを 食べたことが あります。",
        "exRuby": "<ruby>日本<rt>にほん</rt></ruby>の りょうりを <ruby>食<rt>た</rt></ruby>べたことが あります。",
        "exVi": "Tôi đã từng ăn món ăn Nhật Bản."
    },
    {
        "id": "nomu",
        "kanji": "飲む",
        "kana": "のむ",
        "group": "Nhóm 1 (Đuôi む -> んで / んだ)",
        "vi": "Uống",
        "masu": "飲みます",
        "ru": "飲む",
        "te": "飲んで",
        "ta": "飲んだ",
        "nai": "飲まない",
        "tara": "飲んだら",
        "tari": "飲んだり",
        "ex": "くすりを 飲んだほうが いいですよ。",
        "exRuby": "くすりを <ruby>飲<rt>の</rt></ruby>んだほうが いいですよ。",
        "exVi": "Bạn nên uống thuốc đi nhé."
    },
    {
        "id": "iku",
        "kanji": "行く",
        "kana": "いく",
        "group": "Nhóm 1 (Đặc biệt: く -> って / った)",
        "vi": "Đi",
        "masu": "行きます",
        "ru": "行く",
        "te": "行って",
        "ta": "行った",
        "nai": "行かない",
        "tara": "行ったら",
        "tari": "行ったり",
        "ex": "しゅうまつは かいものに 行ったり、えいがを 見たりします。",
        "exRuby": "しゅうまつは かいものに <ruby>行<rt>い</rt></ruby>ったり、えいがを <ruby>見<rt>み</rt></ruby>たりします。",
        "exVi": "Cuối tuần tôi lúc thì đi mua sắm, lúc thì xem phim."
    },
    {
        "id": "kuru",
        "kanji": "来る",
        "kana": "くる",
        "group": "Nhóm 3 (Bất quy tắc: くる -> きます -> きて -> きた -> こない)",
        "vi": "Đến",
        "masu": "来ます (きます)",
        "ru": "来る (くる)",
        "te": "来て (きて)",
        "ta": "来た (きた)",
        "nai": "来ない (こない)",
        "tara": "来たら (きたら)",
        "tari": "来たり (きたり)",
        "ex": "ともだちが うちに あそびに 来ました。",
        "exRuby": "ともだちが うちに あそびに <ruby>来<rt>き</rt></ruby>ました。",
        "exVi": "Bạn tôi đã đến nhà tôi chơi."
    },
    {
        "id": "suru",
        "kanji": "する",
        "kana": "する",
        "group": "Nhóm 3 (Bất quy tắc: する -> します -> して -> した -> しない)",
        "vi": "Làm / Chơi",
        "masu": "します",
        "ru": "する",
        "te": "して",
        "ta": "した",
        "nai": "しない",
        "tara": "したら",
        "tari": "したり",
        "ex": "ここで しゃしんを とっても いいですか。",
        "exRuby": "ここで しゃしんを とっても いいですか。",
        "exVi": "Tôi chụp ảnh ở đây có được không?"
    },
    {
        "id": "kau",
        "kanji": "買う",
        "kana": "かう",
        "group": "Nhóm 1 (Đuôi う -> って / った)",
        "vi": "Mua",
        "masu": "買います",
        "ru": "買う",
        "te": "買って",
        "ta": "買った",
        "nai": "買わない",
        "tara": "買ったら",
        "tari": "買ったり",
        "ex": "おべんとうを 買って 行きましょう。",
        "exRuby": "おべんとうを <ruby>買<rt>か</rt></ruby>って <ruby>行<rt>い</rt></ruby>きましょう。",
        "exVi": "Chúng ta hãy mua cơm hộp mang đi nhé."
    },
    {
        "id": "matsu",
        "kanji": "待つ",
        "kana": "まつ",
        "group": "Nhóm 1 (Đuôi つ -> って / った)",
        "vi": "Chờ / Đợi",
        "masu": "待ちます",
        "ru": "待つ",
        "te": "待って",
        "ta": "待った",
        "nai": "待たない",
        "tara": "待ったら",
        "tari": "待ったり",
        "ex": "ちょっと まってください。",
        "exRuby": "ちょっと まってください。",
        "exVi": "Xin vui lòng đợi một chút."
    },
    {
        "id": "yomu",
        "kanji": "読む",
        "kana": "よむ",
        "group": "Nhóm 1 (Đuôi む -> んで / んだ)",
        "vi": "Đọc",
        "masu": "読みます",
        "ru": "読む",
        "te": "読んで",
        "ta": "読んだ",
        "nai": "読まない",
        "tara": "読んだら",
        "tari": "読んだり",
        "ex": "ねる まえに、本を 読みます。",
        "exRuby": "ねる まえに、<ruby>本<rt>ほん</rt></ruby>を <ruby>読<rt>よ</rt></ruby>みます。",
        "exVi": "Trước khi ngủ, tôi đọc sách."
    },
    {
        "id": "hanasu",
        "kanji": "話す",
        "kana": "はなす",
        "group": "Nhóm 1 (Đuôi す -> して / した)",
        "vi": "Nói chuyện",
        "masu": "話します",
        "ru": "話す",
        "te": "話して",
        "ta": "話した",
        "nai": "話さない",
        "tara": "話したら",
        "tari": "話したり",
        "ex": "日本語で 話してください。",
        "exRuby": "<ruby>日本<rt>にほん</rt></ruby><ruby>語<rt>ご</rt></ruby>で <ruby>話<rt>はな</rt></ruby>してください。",
        "exVi": "Xin hãy nói bằng tiếng Nhật."
    },
    {
        "id": "miru",
        "kanji": "見る",
        "kana": "みる",
        "group": "Nhóm 2 (Đuôi る trước là âm i)",
        "vi": "Xem / Nhìn",
        "masu": "見ます",
        "ru": "見る",
        "te": "見て",
        "ta": "見た",
        "nai": "見ない",
        "tara": "見たら",
        "tari": "見たり",
        "ex": "テレビを 見ながら、ごはんを 食べます。",
        "exRuby": "テレビを <ruby>見<rt>み</rt></ruby>ながら、ごはんを <ruby>食<rt>た</rt></ruby>べます。",
        "exVi": "Vừa xem tivi vừa ăn cơm."
    },
    {
        "id": "kaeru",
        "kanji": "帰る",
        "kana": "かえる",
        "group": "Nhóm 1 đặc biệt (Đuôi る đổi thành って)",
        "vi": "Về (nhà, quê)",
        "masu": "帰ります",
        "ru": "帰る",
        "te": "帰って",
        "ta": "帰った",
        "nai": "帰らない",
        "tara": "帰ったら",
        "tari": "帰ったり",
        "ex": "いえに 帰ってから、シャワーを あびます。",
        "exRuby": "いえに <ruby>帰<rt>かえ</rt></ruby>ってから、シャワーを あびます。",
        "exVi": "Sau khi về nhà thì tôi tắm vòi sen."
    },
    {
        "id": "au",
        "kanji": "会う",
        "kana": "あう",
        "group": "Nhóm 1 (Đuôi う -> って / った)",
        "vi": "Gặp gỡ",
        "masu": "会います",
        "ru": "会う",
        "te": "会って",
        "ta": "会った",
        "nai": "会わない",
        "tara": "会ったら",
        "tari": "会ったり",
        "ex": "日曜日、ともだちに 会う よていです。",
        "exRuby": "<ruby>日<rt>にち</rt></ruby><ruby>曜<rt>よう</rt></ruby><ruby>日<rt>び</rt></ruby>、ともだちに <ruby>会<rt>あ</rt></ruby>う よていです。",
        "exVi": "Chủ nhật, tôi dự định gặp bạn."
    },
    {
        "id": "tsukuru",
        "kanji": "作る",
        "kana": "つくる",
        "group": "Nhóm 1 (Đuôi る -> って / った)",
        "vi": "Làm / Nấu chế biến",
        "masu": "作ります",
        "ru": "作る",
        "te": "作って",
        "ta": "作った",
        "nai": "作らない",
        "tara": "作ったら",
        "tari": "作ったり",
        "ex": "母が ケーキを つくってくれました。",
        "exRuby": "<ruby>母<rt>はは</rt></ruby>が ケーキを つくってくれました。",
        "exVi": "Mẹ đã làm bánh ngọt cho tôi."
    },
    {
        "id": "neru",
        "kanji": "寝る",
        "kana": "ねる",
        "group": "Nhóm 2 (Đuôi る trước là âm e)",
        "vi": "Ngủ",
        "masu": "寝ます",
        "ru": "寝る",
        "te": "寝て",
        "ta": "寝た",
        "nai": "寝ない",
        "tara": "寝たら",
        "tari": "寝たり",
        "ex": "早く ねたほうが いいですよ。",
        "exRuby": "<ruby>早<rt>はや</rt></ruby>く ねたほうが いいですよ。",
        "exVi": "Bạn nên đi ngủ sớm đi nhé."
    },
    {
        "id": "okiru",
        "kanji": "起きる",
        "kana": "おきる",
        "group": "Nhóm 2 (Đuôi る trước là âm i)",
        "vi": "Thức dậy",
        "masu": "起きます",
        "ru": "起きる",
        "te": "起きて",
        "ta": "起きた",
        "nai": "起きない",
        "tara": "起きたら",
        "tari": "起きたり",
        "ex": "毎朝 6時に 起きています。",
        "exRuby": "<ruby>毎<rt>まい</rt></ruby><ruby>朝<rt>あさ</rt></ruby> 6<ruby>時<rt>じ</rt></ruby>に <ruby>起<rt>お</rt></ruby>きています。",
        "exVi": "Mỗi sáng tôi đều thức dậy lúc 6 giờ."
    }
]

def generate_html():
    grammar_items_json = json.dumps(mgd.ALL_GRAMMAR_ITEMS, ensure_ascii=False)
    verbs_json = json.dumps(VERB_LAB_DATA, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>Tổng Hợp Ngữ Pháp Marugoto A1 - A2 Toàn Diện (26 Bài Học) | JF Standard</title>
    <meta name="description" content="Cẩm nang tổng hợp ngữ pháp Marugoto A1 (L11-18), A2-1 (L1-10) và A2-2 (L11-18). Đầy đủ công thức, giải thích chi tiết, audio Tokyo chuẩn, máy biến đổi động từ và trắc nghiệm phản xạ.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <!-- Animate UI Core -->
    <link rel="stylesheet" href="animate-ui.css">
    <script src="animate-ui.js" defer></script>
    <!-- Unified Tokyo Audio Engine -->
    <script src="audio-engine.js"></script>
    <style>
        :root {{
            --primary: #4f46e5;
            --primary-dark: #3730a3;
            --primary-light: #6366f1;
            --primary-soft: #eef2ff;
            --accent: #f59e0b;
            --accent-green: #10b981;
            --accent-rose: #f43f5e;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --bg-light: #f8fafc;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --jp-font: 'Noto Sans JP', sans-serif;
            --main-font: 'Plus Jakarta Sans', sans-serif;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: var(--main-font);
            background-color: #f1f5f9;
            color: var(--text-dark);
            line-height: 1.6;
            padding-bottom: 90px;
            overflow-x: hidden;
        }}

        .jp-text {{
            font-family: var(--jp-font);
        }}

        /* -------------------------------------------------------------
           1. GLOBAL HUB NAVIGATION (CLEAN & NON-STICKY)
        ------------------------------------------------------------- */
        .global-hub-nav {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 12px auto 20px auto;
            flex-wrap: wrap;
            max-width: 1300px;
            padding: 0 10px;
        }}

        .hub-nav-item {{
            text-decoration: none;
            background: #ffffff;
            color: #475569;
            padding: 9px 18px;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 700;
            border: 1.5px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            font-family: inherit;
        }}

        .hub-nav-item:hover {{
            border-color: var(--primary);
            color: var(--primary);
            transform: translateY(-2px);
        }}

        .hub-nav-item.active-hub {{
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff !important;
            border-color: transparent;
            box-shadow: 0 4px 15px rgba(79, 70, 229, 0.35);
        }}

        /* Hub Dropdown Menu */
        .hub-dropdown {{
            position: relative;
            display: inline-block;
        }}

        .hub-dropdown-menu {{
            display: none;
            position: absolute;
            top: calc(100% + 6px);
            left: 50%;
            transform: translateX(-50%);
            background: #ffffff;
            border: 1.5px solid #e2e8f0;
            border-radius: 14px;
            box-shadow: 0 12px 28px rgba(0,0,0,0.12);
            padding: 8px;
            min-width: 260px;
            z-index: 9999;
        }}

        .hub-dropdown-menu.show {{
            display: block;
        }}

        .hub-drop-link {{
            display: block;
            padding: 8px 14px;
            color: #334155;
            font-size: 0.88rem;
            font-weight: 700;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.15s ease;
        }}

        .hub-drop-link:hover {{
            background: #eef2ff;
            color: #4f46e5;
        }}

        .hub-drop-link.active {{
            background: #4f46e5;
            color: #ffffff !important;
        }}

        @media (max-width: 768px) {{
            .global-hub-nav {{
                display: flex;
                flex-wrap: nowrap;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                justify-content: flex-start;
                gap: 8px;
                margin-bottom: 15px;
                padding: 2px 2px 8px 2px;
                scrollbar-width: none;
            }}
            .global-hub-nav::-webkit-scrollbar {{
                display: none;
            }}
            .hub-nav-item {{
                flex-shrink: 0;
                padding: 7px 14px;
                font-size: 0.84rem;
            }}
        }}

        /* -------------------------------------------------------------
           2. HERO HEADER & KPI STATS
        ------------------------------------------------------------- */
        .hero-section {{
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%);
            color: #ffffff;
            padding: 50px 20px 40px;
            position: relative;
            overflow: hidden;
        }}

        .hero-section::before {{
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 350px;
            height: 350px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.3) 0%, transparent 70%);
            border-radius: 50%;
        }}

        .hero-container {{
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }}

        .hero-badge-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: #e0e7ff;
            margin-bottom: 16px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}

        .hero-title {{
            font-size: 2.25rem;
            font-weight: 900;
            line-height: 1.25;
            margin-bottom: 14px;
            background: linear-gradient(135deg, #ffffff, #c7d2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .hero-subtitle {{
            font-size: 1.05rem;
            color: #c7d2fe;
            max-width: 850px;
            line-height: 1.6;
            margin-bottom: 28px;
        }}

        /* KPI STATS CARDS */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }}

        .kpi-card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: var(--radius-md);
            padding: 16px 20px;
            display: flex;
            align-items: center;
            gap: 14px;
            transition: transform 0.2s ease;
        }}

        .kpi-card:hover {{
            transform: translateY(-2px);
            background: rgba(255, 255, 255, 0.15);
        }}

        .kpi-icon {{
            font-size: 2rem;
        }}

        .kpi-value {{
            font-size: 1.6rem;
            font-weight: 900;
            color: #ffffff;
            line-height: 1.1;
        }}

        .kpi-label {{
            font-size: 0.8rem;
            color: #e0e7ff;
            font-weight: 600;
            margin-top: 2px;
        }}

        /* PROGRESS BAR IN HERO */
        .progress-box {{
            background: rgba(15, 23, 42, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: var(--radius-md);
            padding: 18px 22px;
        }}

        .progress-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.88rem;
            font-weight: 700;
            color: #e0e7ff;
            margin-bottom: 10px;
        }}

        .progress-track {{
            height: 10px;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 999px;
            overflow: hidden;
            position: relative;
        }}

        .progress-fill {{
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #10b981, #34d399);
            border-radius: 999px;
            transition: width 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .progress-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 10px;
            font-size: 0.8rem;
            color: #c7d2fe;
        }}

        .btn-text-action {{
            background: none;
            border: none;
            color: #a5b4fc;
            text-decoration: underline;
            cursor: pointer;
            font-size: 0.8rem;
            font-weight: 600;
        }}

        .btn-text-action:hover {{
            color: #ffffff;
        }}

        /* -------------------------------------------------------------
           3. MAIN APP LAYOUT & TABS
        ------------------------------------------------------------- */
        .app-container {{
            max-width: 1300px;
            margin: 0 auto;
            padding: 30px 20px;
        }}

        /* TOP NAVIGATION TABS (GRAMMAR EXPLORER / VERB LAB / QUIZ) */
        .top-mode-nav {{
            display: flex;
            align-items: center;
            gap: 10px;
            background: #ffffff;
            padding: 8px;
            border-radius: var(--radius-md);
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 24px;
            overflow-x: auto;
        }}

        .mode-tab-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 0.92rem;
            font-weight: 700;
            cursor: pointer;
            border: none;
            background: transparent;
            color: #64748b;
            white-space: nowrap;
            transition: all 0.2s ease;
        }}

        .mode-tab-btn:hover {{
            background: #f1f5f9;
            color: var(--text-dark);
        }}

        .mode-tab-btn.active {{
            background: var(--primary);
            color: #ffffff;
            box-shadow: 0 4px 10px rgba(79, 70, 229, 0.25);
        }}

        /* -------------------------------------------------------------
           4. SEARCH & FILTER CONTROLS
        ------------------------------------------------------------- */
        .filter-panel {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-lg);
            padding: 22px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            margin-bottom: 28px;
        }}

        .search-row {{
            display: flex;
            gap: 12px;
            margin-bottom: 18px;
        }}

        .search-input-box {{
            flex: 1;
            position: relative;
        }}

        .search-input-box input {{
            width: 100%;
            padding: 12px 18px 12px 42px;
            border-radius: var(--radius-md);
            border: 1.5px solid #cbd5e1;
            font-size: 0.95rem;
            font-family: inherit;
            color: var(--text-dark);
            outline: none;
            transition: border-color 0.2s, box-shadow 0.2s;
        }}

        .search-input-box input:focus {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
        }}

        .search-icon {{
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
            font-size: 1.1rem;
        }}

        .level-tabs-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 14px;
        }}

        .level-pill {{
            padding: 7px 16px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            border: 1px solid #e2e8f0;
            background: #f8fafc;
            color: #475569;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .level-pill:hover {{
            background: #e2e8f0;
            color: var(--text-dark);
        }}

        .level-pill.active {{
            background: var(--text-dark);
            color: #ffffff;
            border-color: var(--text-dark);
        }}

        .furigana-toggle-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            border: 1.5px solid #6366f1;
            background: #eef2ff;
            color: #4338ca;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .furigana-toggle-btn:hover {{
            background: #e0e7ff;
            transform: translateY(-1px);
        }}

        .furigana-toggle-btn.off {{
            border-color: #cbd5e1;
            background: #f8fafc;
            color: #64748b;
        }}

        /* Ruby / Furigana Styling */
        ruby {{
            ruby-position: over;
        }}

        rt {{
            font-size: 0.62em;
            font-weight: 700;
            color: #4f46e5;
            line-height: 1;
            user-select: none;
            letter-spacing: 0.02em;
        }}

        body.hide-furigana rt {{
            display: none;
        }}

        .category-scroll-row {{
            display: flex;
            align-items: center;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}

        .cat-chip {{
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 600;
            border: 1px solid #e2e8f0;
            background: #ffffff;
            color: #64748b;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.15s ease;
        }}

        .cat-chip:hover {{
            background: #f1f5f9;
            color: var(--primary);
        }}

        .cat-chip.active {{
            background: var(--primary-soft);
            color: var(--primary);
            border-color: var(--primary-light);
            font-weight: 700;
        }}

        .filter-status-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 14px;
            padding-top: 12px;
            border-top: 1px solid #f1f5f9;
            font-size: 0.84rem;
            color: #64748b;
        }}

        /* -------------------------------------------------------------
           5. GRAMMAR CARDS GRID
        ------------------------------------------------------------- */
        .grammar-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 22px;
        }}

        @media (min-width: 992px) {{
            .grammar-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}

        .grammar-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.04);
            display: flex;
            flex-direction: column;
            position: relative;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s, border-color 0.2s;
        }}

        .grammar-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 12px 20px -4px rgba(0, 0, 0, 0.08);
            border-color: #cbd5e1;
        }}

        .grammar-card.is-learned {{
            border-color: #10b981;
            background: linear-gradient(180deg, #ffffff 0%, #f0fdf4 100%);
        }}

        .grammar-card.is-learned::after {{
            content: '✓ ĐÃ THUỘC';
            position: absolute;
            top: 14px;
            right: 14px;
            font-size: 0.72rem;
            font-weight: 800;
            background: #10b981;
            color: #ffffff;
            padding: 3px 8px;
            border-radius: 999px;
            letter-spacing: 0.05em;
        }}

        .card-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 14px;
        }}

        .card-meta {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .level-badge {{
            font-size: 0.74rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 6px;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }}

        .level-a1 {{
            background: #e0f2fe;
            color: #0369a1;
        }}

        .level-a2-1 {{
            background: #dcfce7;
            color: #15803d;
        }}

        .level-a2-2 {{
            background: #f3e8ff;
            color: #7e22ce;
        }}

        .lesson-badge {{
            font-size: 0.76rem;
            font-weight: 700;
            color: #64748b;
            background: #f1f5f9;
            padding: 4px 8px;
            border-radius: 6px;
        }}

        .tag-pill {{
            font-size: 0.74rem;
            font-weight: 600;
            background: #fffbeb;
            color: #b45309;
            border: 1px solid #fef3c7;
            padding: 3px 8px;
            border-radius: 6px;
        }}

        .card-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--text-dark);
            line-height: 1.4;
            margin-bottom: 12px;
        }}

        /* FORMULA BOX */
        .formula-box {{
            background: #1e1b4b;
            color: #ffffff;
            padding: 14px 16px;
            border-radius: var(--radius-md);
            font-family: inherit;
            font-size: 0.92rem;
            line-height: 1.6;
            margin-bottom: 14px;
            border-left: 4px solid #6366f1;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
        }}

        .meaning-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 12px 14px;
            margin-bottom: 14px;
            font-size: 0.88rem;
            color: #334155;
            line-height: 1.55;
        }}

        .meaning-label {{
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 4px;
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .notes-box {{
            background: #fffdf5;
            border: 1px dashed #fde68a;
            border-radius: var(--radius-md);
            padding: 10px 14px;
            margin-bottom: 14px;
            font-size: 0.83rem;
            color: #92400e;
            line-height: 1.5;
        }}

        /* EXAMPLES CONTAINER */
        .examples-section {{
            margin-top: auto;
            border-top: 1px solid #f1f5f9;
            padding-top: 14px;
        }}

        .examples-title {{
            font-size: 0.78rem;
            font-weight: 800;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 10px;
        }}

        .example-item {{
            background: #f8fafc;
            border: 1px solid #edf2f7;
            border-radius: var(--radius-sm);
            padding: 10px 12px;
            margin-bottom: 8px;
            transition: background 0.15s ease;
        }}

        .example-item:hover {{
            background: #f1f5f9;
        }}

        .example-jp-row {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 8px;
        }}

        .example-jp {{
            font-family: var(--jp-font);
            font-size: 1.02rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.85;
        }}

        .example-vi {{
            font-size: 0.82rem;
            color: #64748b;
            margin-top: 4px;
        }}

        .btn-speak {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.85rem;
            flex-shrink: 0;
            transition: all 0.15s ease;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }}

        .btn-speak:hover {{
            background: var(--primary-soft);
            border-color: var(--primary-light);
            color: var(--primary);
            transform: scale(1.08);
        }}

        .card-actions {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 14px;
            padding-top: 12px;
            border-top: 1px solid #f1f5f9;
        }}

        .learn-toggle-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            border: 1.5px solid #cbd5e1;
            background: #ffffff;
            color: #475569;
            transition: all 0.2s ease;
        }}

        .learn-toggle-btn:hover {{
            border-color: #10b981;
            color: #10b981;
        }}

        .learn-toggle-btn.checked {{
            background: #10b981;
            color: #ffffff;
            border-color: #10b981;
        }}

        .card-quiz-btn {{
            background: none;
            border: none;
            color: var(--primary);
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .card-quiz-btn:hover {{
            text-decoration: underline;
        }}

        /* INLINE CARD QUIZ ACCORDION */
        .card-inline-quiz {{
            display: none;
            background: #f8fafc;
            border: 1.5px solid #c7d2fe;
            border-radius: var(--radius-md);
            padding: 14px;
            margin-top: 12px;
        }}

        .card-inline-quiz.show {{
            display: block;
        }}

        .inline-quiz-q {{
            font-weight: 700;
            font-size: 0.88rem;
            margin-bottom: 10px;
            color: var(--primary-dark);
        }}

        .inline-quiz-options {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 10px;
        }}

        .inline-opt-btn {{
            padding: 8px 10px;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            text-align: left;
            transition: all 0.15s ease;
        }}

        .inline-opt-btn:hover {{
            border-color: var(--primary);
            background: var(--primary-soft);
        }}

        .inline-opt-btn.correct {{
            background: #dcfce7 !important;
            border-color: #10b981 !important;
            color: #15803d !important;
            font-weight: 700;
        }}

        .inline-opt-btn.wrong {{
            background: #fee2e2 !important;
            border-color: #ef4444 !important;
            color: #b91c1c !important;
        }}

        .inline-explain {{
            display: none;
            font-size: 0.8rem;
            padding: 8px;
            border-radius: 6px;
            background: #eef2ff;
            color: #3730a3;
            line-height: 1.45;
        }}

        .inline-explain.show {{
            display: block;
        }}

        /* -------------------------------------------------------------
           6. VERB MORPHING LAB
        ------------------------------------------------------------- */
        .verb-lab-section {{
            display: none;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-lg);
            padding: 30px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
            margin-bottom: 30px;
        }}

        .verb-lab-section.active {{
            display: block;
        }}

        .lab-header {{
            margin-bottom: 24px;
        }}

        .lab-title {{
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--text-dark);
            margin-bottom: 6px;
        }}

        .lab-desc {{
            font-size: 0.9rem;
            color: var(--text-muted);
        }}

        .verb-picker-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 12px;
            margin-bottom: 24px;
        }}

        .verb-select-pill {{
            padding: 8px 16px;
            border-radius: 999px;
            border: 1px solid #cbd5e1;
            background: #ffffff;
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--text-dark);
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
        }}

        .verb-select-pill:hover {{
            background: #f1f5f9;
            border-color: var(--primary);
        }}

        .verb-select-pill.active {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
        }}

        .morph-display-card {{
            background: #f8fafc;
            border: 1.5px solid #e2e8f0;
            border-radius: var(--radius-lg);
            padding: 24px;
        }}

        .verb-main-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 1px solid #e2e8f0;
        }}

        .verb-hero-name {{
            font-size: 1.8rem;
            font-weight: 900;
            color: var(--primary-dark);
        }}

        .verb-hero-group {{
            font-size: 0.85rem;
            font-weight: 700;
            color: #64748b;
            background: #e2e8f0;
            padding: 4px 12px;
            border-radius: 999px;
        }}

        .morph-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }}

        .morph-cell {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: var(--radius-md);
            padding: 14px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.03);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .morph-cell-tag {{
            font-size: 0.72rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--primary);
            margin-bottom: 6px;
        }}

        .morph-cell-jp-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 6px;
        }}

        .morph-cell-jp {{
            font-size: 1.2rem;
            font-weight: 800;
            color: var(--text-dark);
        }}

        .morph-cell-note {{
            font-size: 0.75rem;
            color: #64748b;
            margin-top: 4px;
        }}

        .morph-ex-box {{
            background: #eef2ff;
            border-left: 4px solid var(--primary);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }}

        .morph-ex-jp {{
            font-size: 1rem;
            font-weight: 700;
            color: #1e1b4b;
        }}

        .morph-ex-vi {{
            font-size: 0.85rem;
            color: #475569;
            margin-top: 4px;
        }}

        /* -------------------------------------------------------------
           7. MASTER REFLEX QUIZ MODAL
        ------------------------------------------------------------- */
        .quiz-modal-overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(8px);
            z-index: 3000;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}

        .quiz-modal-overlay.show {{
            display: flex;
        }}

        .quiz-modal-card {{
            background: #ffffff;
            width: 100%;
            max-width: 650px;
            border-radius: var(--radius-lg);
            padding: 28px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.3);
            position: relative;
        }}

        .quiz-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 1px solid #e2e8f0;
        }}

        .quiz-step-badge {{
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--primary);
            background: var(--primary-soft);
            padding: 4px 12px;
            border-radius: 999px;
        }}

        .quiz-score-badge {{
            font-size: 0.85rem;
            font-weight: 800;
            color: #10b981;
        }}

        .quiz-close-btn {{
            background: none;
            border: none;
            font-size: 1.2rem;
            cursor: pointer;
            color: #94a3b8;
        }}

        .quiz-q-box {{
            background: #f8fafc;
            border: 1.5px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 18px;
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--text-dark);
            margin-bottom: 20px;
            line-height: 1.5;
        }}

        .quiz-options-list {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }}

        .quiz-opt-btn {{
            padding: 12px 18px;
            background: #ffffff;
            border: 1.5px solid #cbd5e1;
            border-radius: var(--radius-md);
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--text-dark);
            cursor: pointer;
            text-align: left;
            transition: all 0.15s ease;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .quiz-opt-btn:hover {{
            background: #f8fafc;
            border-color: var(--primary);
        }}

        .quiz-opt-btn.correct {{
            background: #dcfce7 !important;
            border-color: #10b981 !important;
            color: #15803d !important;
        }}

        .quiz-opt-btn.wrong {{
            background: #fee2e2 !important;
            border-color: #ef4444 !important;
            color: #b91c1c !important;
        }}

        .quiz-explain-box {{
            display: none;
            background: #eef2ff;
            border-left: 4px solid var(--primary);
            padding: 12px 16px;
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            font-size: 0.88rem;
            color: #312e81;
            margin-bottom: 20px;
            line-height: 1.5;
        }}

        .quiz-explain-box.show {{
            display: block;
        }}

        .quiz-actions {{
            display: flex;
            justify-content: flex-end;
            gap: 12px;
        }}

        .quiz-next-btn {{
            padding: 10px 24px;
            background: var(--primary);
            color: #ffffff;
            border: none;
            border-radius: 999px;
            font-size: 0.9rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .quiz-next-btn:hover {{
            background: var(--primary-dark);
            transform: translateY(-1px);
        }}

        /* CELEBRATION SUMMARY */
        .quiz-result-view {{
            text-align: center;
            padding: 20px 0;
        }}

        .quiz-result-trophy {{
            font-size: 4rem;
            margin-bottom: 12px;
        }}

        .quiz-result-title {{
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--text-dark);
            margin-bottom: 8px;
        }}

        .quiz-result-score {{
            font-size: 2.5rem;
            font-weight: 900;
            color: var(--primary);
            margin-bottom: 14px;
        }}

        .quiz-result-desc {{
            font-size: 0.92rem;
            color: var(--text-muted);
            max-width: 450px;
            margin: 0 auto 24px;
        }}

        /* -------------------------------------------------------------
           8. TOAST NOTIFICATION
        ------------------------------------------------------------- */
        .toast-bubble {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #1e1b4b;
            color: #ffffff;
            padding: 12px 20px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.25);
            z-index: 9999;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            pointer-events: none;
        }}

        .toast-bubble.show {{
            opacity: 1;
            transform: translateY(0);
        }}
    </style>
</head>
<body>

    <!-- Global Hub Navigation -->
    <div class="global-hub-nav">
        <a href="index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item active-hub">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
        <a href="On_Tap_Mini_Test_A2_1_4.html" class="hub-nav-item">🎯 Ôn Tập Bài 1-4</a>
        <a href="On_Tap_Mini_Test_A2_5_8.html" class="hub-nav-item">🎯 Ôn Tập Bài 5-8</a>
        <a href="De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-nav-item">📝 5 Mã Đề Thi Thử</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học 10-18 ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                <a href="Marugoto_A2_Lesson_10.html" class="hub-drop-link">🌟 Bài 10: 外国文化</a>
                <a href="Marugoto_A2_Lesson_11.html" class="hub-drop-link">🍱 Bài 11: そとで食べる</a>
                <a href="Marugoto_A2_Lesson_12.html" class="hub-drop-link">🍜 Bài 12: 特別な日の料理</a>
                <a href="Marugoto_A2_Lesson_13.html" class="hub-drop-link">✈️ Bài 13: 出張</a>
                <a href="Marugoto_A2_Lesson_14.html" class="hub-drop-link">💻 Bài 14: 職場のマナー</a>
                <a href="Marugoto_A2_Lesson_15.html" class="hub-drop-link">🏥 Bài 15: 健康な生活</a>
                <a href="Marugoto_A2_Lesson_16.html" class="hub-drop-link">🏃 Bài 16: 体にいいこと</a>
                <a href="Marugoto_A2_Lesson_17.html" class="hub-drop-link">🎁 Bài 17: お祝い</a>
                <a href="Marugoto_A2_Lesson_18.html" class="hub-drop-link">👘 Bài 18: お祭りやイベント</a>
            </div>
        </div>
    </div>

    <!-- 2. HERO HEADER & KPI STATS -->
    <header class="hero-section">
        <div class="hero-container">
            <div class="hero-badge-pill">
                <span>⚡</span>
                <span>HỆ THỐNG NGỮ PHÁP CHUẨN JF STANDARD (A1 • A2-1 • A2-2)</span>
            </div>
            <h1 class="hero-title">Tổng Hợp Ngữ Pháp Marugoto Toàn Diện</h1>
            <p class="hero-subtitle">
                Đầy đủ trọn vẹn 26 bài học từ 5 tài liệu chính thống: A1 (Bài 11~18), A2-1 (Bài 1~10), và A2-2 (Bài 11~18).
                Tích hợp công thức mẫu, giải thích song ngữ Nhật - Việt, audio giọng chuẩn Tokyo, phòng thực nghiệm biến thể động từ và trắc nghiệm phản xạ 20 câu.
            </p>

            <!-- KPI STATS -->
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-icon">🎓</div>
                    <div>
                        <div class="kpi-value">26</div>
                        <div class="kpi-label">Bài học chuẩn JF</div>
                    </div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-icon">📌</div>
                    <div>
                        <div class="kpi-value">29</div>
                        <div class="kpi-label">Chuyên đề ngữ pháp</div>
                    </div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-icon">💡</div>
                    <div>
                        <div class="kpi-value">75+</div>
                        <div class="kpi-label">Công thức & Mẫu câu</div>
                    </div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-icon">🔊</div>
                    <div>
                        <div class="kpi-value">85+</div>
                        <div class="kpi-label">Ví dụ Audio Tokyo</div>
                    </div>
                </div>
            </div>

            <!-- LEARNING PROGRESS BAR -->
            <div class="progress-box">
                <div class="progress-header">
                    <span>🏆 TIẾN ĐỘ THUỘC LÒNG NGỮ PHÁP</span>
                    <span id="progressStatsText">0 / 29 Đã hiểu (0%)</span>
                </div>
                <div class="progress-track">
                    <div class="progress-fill" id="progressBarFill"></div>
                </div>
                <div class="progress-footer">
                    <span>Bấm nút <strong>"Đã hiểu ✓"</strong> trên mỗi thẻ ngữ pháp để lưu tiến độ tự động vào máy.</span>
                    <div>
                        <button type="button" class="btn-text-action" onclick="markAllLearned()">Đánh dấu tất cả</button>
                        <span style="opacity:0.4; margin:0 6px;">|</span>
                        <button type="button" class="btn-text-action" onclick="resetProgress()">Làm lại từ đầu</button>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- 3. MAIN APP CONTAINER -->
    <main class="app-container">

        <!-- MODE NAVIGATION TABS -->
        <div class="top-mode-nav">
            <button type="button" class="mode-tab-btn active" id="btnTabExplorer" onclick="switchMainTab('explorer')">
                <span>📚</span>
                <span>Kho Ngữ Pháp 26 Bài (29 Chuyên Đề)</span>
            </button>
            <button type="button" class="mode-tab-btn" id="btnTabVerbLab" onclick="switchMainTab('verbLab')">
                <span>⚙️</span>
                <span>Phòng Biến Đổi Động Từ (Verb Morphing Lab)</span>
            </button>
            <button type="button" class="mode-tab-btn" id="btnTabQuiz" onclick="startMasterQuiz()">
                <span>⚡</span>
                <span>Thử Thách Phản Xạ 20 Câu (Random Quiz)</span>
            </button>
        </div>

        <!-- TAB 1: GRAMMAR EXPLORER -->
        <div id="tabExplorerView">
            
            <!-- FILTER PANEL -->
            <div class="filter-panel">
                <!-- Search input -->
                <div class="search-row">
                    <div class="search-input-box">
                        <span class="search-icon">🔍</span>
                        <input type="text" id="grammarSearchInput" placeholder="Tìm theo cấu trúc (ている, てもいい, そう...), nghĩa tiếng Việt (xin phép, thời tiết, khuyên...), hoặc bài học..." oninput="handleSearch()">
                    </div>
                </div>

                <!-- Level filters & Furigana Toggle -->
                <div class="level-tabs-row" style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
                    <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                        <span style="font-size:0.85rem; font-weight:800; color:#64748b; margin-right:4px;">Cấp độ:</span>
                        <button type="button" class="level-pill active" onclick="setLevelFilter('all', this)">Tất cả (29)</button>
                        <button type="button" class="level-pill" onclick="setLevelFilter('A1', this)">Marugoto A1 (11)</button>
                        <button type="button" class="level-pill" onclick="setLevelFilter('A2-1', this)">Marugoto A2-1 (10)</button>
                        <button type="button" class="level-pill" onclick="setLevelFilter('A2-2', this)">Marugoto A2-2 (8)</button>
                    </div>
                    <div style="display:flex; align-items:center; gap:8px;">
                        <button type="button" class="furigana-toggle-btn" id="btnFuriganaToggle" onclick="toggleFurigana()" title="Bật / Tắt hiển thị Furigana (cách đọc Hán tự)">
                            <span>🔤</span> <span id="furiganaBtnLabel">Furigana: BẬT</span>
                        </button>
                    </div>
                </div>

                <!-- Category tags -->
                <div class="category-scroll-row">
                    <span style="font-size:0.8rem; font-weight:700; color:#94a3b8; margin-right:4px; flex-shrink:0;">Thẻ:</span>
                    <button type="button" class="cat-chip active" onclick="setCategoryFilter('all', this)">Tất cả danh mục</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('hobby', this)">Sở thích & Khả năng</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('ongoing', this)">Đang diễn ra (~ている)</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('permission', this)">Xin phép & Cấm đoán</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('advice', this)">Lời khuyên & Gợi ý</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('reason', this)">Lý do & Giải thích</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('guess', this)">Dự đoán (~そう / ~でしょう)</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('experience', this)">Kinh nghiệm (~たことがある)</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('listing', this)">Liệt kê (~たり～たり)</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('giving', this)">Cho & Nhận</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('opinion', this)">Ý kiến (~とおもう)</button>
                    <button type="button" class="cat-chip" onclick="setCategoryFilter('travel', this)">Di chuyển & Nơi chốn</button>
                </div>

                <!-- Status bar -->
                <div class="filter-status-bar">
                    <span id="filterCountLabel">Đang hiển thị 29 / 29 chuyên đề ngữ pháp</span>
                    <span style="font-size:0.8rem; color:#94a3b8;">Nhấn 🔊 trên mỗi ví dụ để luyện phát âm chuẩn Tokyo</span>
                </div>
            </div>

            <!-- GRAMMAR CARDS GRID -->
            <div class="grammar-grid" id="grammarCardsGrid">
                <!-- Injected via JavaScript -->
            </div>
        </div>

        <!-- TAB 2: VERB MORPHING LAB -->
        <div class="verb-lab-section" id="tabVerbLabView">
            <div class="lab-header">
                <div class="lab-title">⚙️ Phòng Thực Nghiệm Biến Đổi Động Từ (Verb Morphing Lab)</div>
                <div class="lab-desc">
                    Quan sát trực quan toàn bộ các thể biến đổi quan trọng nhất trong Marugoto A1 & A2 (ます形, 辞書形 (RU), て形, た形, ない形, たら形, たり形).
                    Chọn nhanh các động từ tiêu biểu bên dưới để nghe phát âm và đối chiếu ngữ cảnh!
                </div>
            </div>

            <!-- Verb picker pills -->
            <div class="verb-picker-row" id="verbPickerRow">
                <!-- Injected via JavaScript -->
            </div>

            <!-- Morph Display Card -->
            <div class="morph-display-card">
                <div class="verb-main-header">
                    <div>
                        <div class="verb-hero-name jp-text" id="labHeroKanji">食べる (たべる)</div>
                        <div style="font-size:1rem; font-weight:700; color:#475569; margin-top:4px;" id="labHeroVi">Ăn</div>
                    </div>
                    <div class="verb-hero-group" id="labHeroGroup">Nhóm 2 (Động từ đuôi る)</div>
                </div>

                <div class="morph-grid">
                    <div class="morph-cell">
                        <div>
                            <div class="morph-cell-tag">1. Thể Lịch Sự (ます形)</div>
                            <div class="morph-cell-jp-row">
                                <span class="morph-cell-jp jp-text" id="mMasu">食べます</span>
                                <button type="button" class="btn-speak" onclick="speakFromElement('mMasu')">🔊</button>
                            </div>
                        </div>
                        <div class="morph-cell-note">Dùng giao tiếp lịch sự hiện tại / tương lai</div>
                    </div>

                    <div class="morph-cell">
                        <div>
                            <div class="morph-cell-tag">2. Thể Từ Điển (辞書形 - Thể RU)</div>
                            <div class="morph-cell-jp-row">
                                <span class="morph-cell-jp jp-text" id="mRu">食べる</span>
                                <button type="button" class="btn-speak" onclick="speakFromElement('mRu')">🔊</button>
                            </div>
                        </div>
                        <div class="morph-cell-note">Dùng trong: V-ること, V-るまえに, V-るとき, V-ると</div>
                    </div>

                    <div class="morph-cell">
                        <div>
                            <div class="morph-cell-tag">3. Thể Nối (て形 - Thể TE)</div>
                            <div class="morph-cell-jp-row">
                                <span class="morph-cell-jp jp-text" id="mTe">食べて</span>
                                <button type="button" class="btn-speak" onclick="speakFromElement('mTe')">🔊</button>
                            </div>
                        </div>
                        <div class="morph-cell-note">Dùng trong: V-ている, V-てください, V-てもいい, V-てから</div>
                    </div>

                    <div class="morph-cell">
                        <div>
                            <div class="morph-cell-tag">4. Thể Quá Khứ (た形 - Thể TA)</div>
                            <div class="morph-cell-jp-row">
                                <span class="morph-cell-jp jp-text" id="mTa">食べた</span>
                                <button type="button" class="btn-speak" onclick="speakFromElement('mTa')">🔊</button>
                            </div>
                        </div>
                        <div class="morph-cell-note">Dùng trong: V-たことがある (Kinh nghiệm), V-たほうがいい (Khuyên)</div>
                    </div>

                    <div class="morph-cell">
                        <div>
                            <div class="morph-cell-tag">5. Thể Phủ Định (ない形 - Thể NAI)</div>
                            <div class="morph-cell-jp-row">
                                <span class="morph-cell-jp jp-text" id="mNai">食べない</span>
                                <button type="button" class="btn-speak" onclick="speakFromElement('mNai')">🔊</button>
                            </div>
                        </div>
                        <div class="morph-cell-note">Dùng trong: V-ないでください (Xin đừng), V-ないほうがいい</div>
                    </div>

                    <div class="morph-cell">
                        <div>
                            <div class="morph-cell-tag">6. Thể Điều Kiện (たら形)</div>
                            <div class="morph-cell-jp-row">
                                <span class="morph-cell-jp jp-text" id="mTara">食べたら</span>
                                <button type="button" class="btn-speak" onclick="speakFromElement('mTara')">🔊</button>
                            </div>
                        </div>
                        <div class="morph-cell-note">Dùng trong: Nếu... thì... / V-たらどうですか (Gợi ý)</div>
                    </div>

                    <div class="morph-cell">
                        <div>
                            <div class="morph-cell-tag">7. Thể Liệt Kê (たり形)</div>
                            <div class="morph-cell-jp-row">
                                <span class="morph-cell-jp jp-text" id="mTari">食べたり</span>
                                <button type="button" class="btn-speak" onclick="speakFromElement('mTari')">🔊</button>
                            </div>
                        </div>
                        <div class="morph-cell-note">Dùng trong: V1-たり V2-たりします (Lúc thì... lúc thì...)</div>
                    </div>
                </div>

                <div class="morph-ex-box">
                    <div>
                        <div style="font-size:0.75rem; font-weight:800; color:var(--primary); text-transform:uppercase; margin-bottom:4px;">Ví dụ mẫu thực tế:</div>
                        <div class="morph-ex-jp jp-text" id="mExJp"><ruby>日本<rt>にほん</rt></ruby>の りょうりを <ruby>食<rt>た</rt></ruby>べたことが あります。</div>
                        <div class="morph-ex-vi" id="mExVi">Tôi đã từng ăn món ăn Nhật Bản.</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakFromElement('mExJp')">🔊</button>
                </div>
            </div>
        </div>

    </main>

    <!-- 4. MASTER REFLEX QUIZ MODAL -->
    <div class="quiz-modal-overlay" id="quizModalOverlay" onclick="closeQuizModal()">
        <div class="quiz-modal-card" onclick="event.stopPropagation()">
            <div class="quiz-header">
                <div style="display:flex; align-items:center; gap:10px;">
                    <span class="quiz-step-badge" id="quizStepBadge">Câu 1 / 20</span>
                    <span class="quiz-score-badge" id="quizScoreBadge">Điểm: 0</span>
                </div>
                <button type="button" class="quiz-close-btn" onclick="closeQuizModal()">✕</button>
            </div>

            <!-- Question Screen -->
            <div id="quizQuestionView">
                <div class="quiz-q-box jp-text" id="quizQuestionText">
                    <!-- Injected via JS -->
                </div>

                <div class="quiz-options-list" id="quizOptionsList">
                    <!-- Injected via JS -->
                </div>

                <div class="quiz-explain-box" id="quizExplainBox">
                    <!-- Injected via JS -->
                </div>

                <div class="quiz-actions">
                    <button type="button" class="quiz-next-btn" id="btnNextQuiz" onclick="nextQuizQuestion()" style="display:none;">Câu tiếp theo →</button>
                </div>
            </div>

            <!-- Result Screen -->
            <div class="quiz-result-view" id="quizResultView" style="display:none;">
                <div class="quiz-result-trophy" id="quizTrophy">🎉</div>
                <h3 class="quiz-result-title" id="quizResultTitle">Hoàn Thành Thử Thách!</h3>
                <div class="quiz-result-score" id="quizResultScore">18 / 20</div>
                <p class="quiz-result-desc" id="quizResultDesc">
                    Phản xạ ngữ pháp tuyệt vời! Bạn đã nắm rất chắc các mẫu câu trọng tâm từ A1 đến A2.
                </p>
                <div style="display:flex; justify-content:center; gap:12px;">
                    <button type="button" class="quiz-next-btn" onclick="startMasterQuiz()">⚡ Thử thách lại</button>
                    <button type="button" class="dock-btn" onclick="closeQuizModal()">Đóng cửa sổ</button>
                </div>
            </div>
        </div>
    </div>

    <!-- TOAST NOTIFICATION -->
    <div class="toast-bubble" id="toastBubble">Đã lưu tiến độ!</div>

    <!-- 5. JAVASCRIPT LOGIC -->
    <script>
        const GRAMMAR_DATA = {grammar_items_json};
        const VERB_DATA = {verbs_json};

        const STORAGE_KEY = 'marugoto_grammar_progress_v1';
        let learnedSet = new Set();

        // Filter states
        let currentLevel = 'all';
        let currentCat = 'all';
        let currentSearch = '';

        // Load progress from localStorage
        function loadProgress() {{
            try {{
                const saved = localStorage.getItem(STORAGE_KEY);
                if (saved) {{
                    const arr = JSON.parse(saved);
                    learnedSet = new Set(arr);
                }}
            }} catch(e) {{
                console.error(e);
            }}
            updateProgressUI();
        }}

        function saveProgress() {{
            try {{
                localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(learnedSet)));
            }} catch(e) {{
                console.error(e);
            }}
            updateProgressUI();
        }}

        function updateProgressUI() {{
            const total = GRAMMAR_DATA.length;
            const count = learnedSet.size;
            const percent = total > 0 ? Math.round((count / total) * 100) : 0;

            document.getElementById('progressStatsText').textContent = `${{count}} / ${{total}} Đã hiểu (${{percent}}%)`;
            document.getElementById('progressBarFill').style.width = `${{percent}}%`;

            // Update card badges if rendered
            GRAMMAR_DATA.forEach(item => {{
                const card = document.getElementById(`grammarCard_${{item.id}}`);
                const btn = document.getElementById(`learnToggleBtn_${{item.id}}`);
                if (card && btn) {{
                    if (learnedSet.has(item.id)) {{
                        card.classList.add('is-learned');
                        btn.classList.add('checked');
                        btn.innerHTML = '✓ Đã thuộc';
                    }} else {{
                        card.classList.remove('is-learned');
                        btn.classList.remove('checked');
                        btn.innerHTML = '○ Đánh dấu đã hiểu';
                    }}
                }}
            }});
        }}

        function toggleLearned(id, event) {{
            if (event) event.stopPropagation();
            if (learnedSet.has(id)) {{
                learnedSet.delete(id);
                showToast(`Đã bỏ đánh dấu chuyên đề #${{id}}`);
            }} else {{
                learnedSet.add(id);
                showToast(`🎉 Tuyệt vời! Đã thuộc chuyên đề #${{id}}`);
            }}
            saveProgress();
        }}

        function markAllLearned() {{
            if (confirm('Bạn có chắc chắn muốn đánh dấu ĐÃ THUỘC toàn bộ 29 chuyên đề ngữ pháp?')) {{
                GRAMMAR_DATA.forEach(item => learnedSet.add(item.id));
                saveProgress();
                showToast('🎉 Chúc mừng! Bạn đã hoàn thành 100% ngữ pháp!');
            }}
        }}

        function resetProgress() {{
            if (confirm('Bạn có chắc chắn muốn xóa tiến độ và học lại từ đầu?')) {{
                learnedSet.clear();
                saveProgress();
                showToast('Đã đặt lại tiến độ học tập.');
            }}
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toastBubble');
            toast.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2200);
        }}

        // Tokyo Audio Speech Synthesis (Dual Engine via audio-engine.js)
        function speakText(text) {{
            if (window.speakJapanese) {{
                window.speakJapanese(text);
            }}
        }}

        function speakFromElement(elId) {{
            const el = document.getElementById(elId);
            if (el) {{
                // Clone and remove <rt> so TTS does not read furigana twice
                const clone = el.cloneNode(true);
                clone.querySelectorAll('rt').forEach(rt => rt.remove());
                speakText(clone.textContent.trim());
            }}
        }}

        // RENDER GRAMMAR CARDS
        function renderGrammarCards() {{
            const container = document.getElementById('grammarCardsGrid');
            const searchLower = currentSearch.trim().toLowerCase();

            const filtered = GRAMMAR_DATA.filter(item => {{
                // Level filter
                if (currentLevel !== 'all' && item.level !== currentLevel) return false;
                
                // Category filter
                if (currentCat !== 'all' && item.cat !== currentCat) return false;

                // Search query
                if (searchLower) {{
                    const matchTitle = item.title.toLowerCase().includes(searchLower);
                    const matchFormula = item.formula.toLowerCase().includes(searchLower);
                    const matchMeaning = item.meaning.toLowerCase().includes(searchLower);
                    const matchNotes = item.notes.toLowerCase().includes(searchLower);
                    const matchLesson = `bài ${{item.lesson}}`.includes(searchLower) || `lesson ${{item.lesson}}`.includes(searchLower);
                    const matchTag = item.tag.toLowerCase().includes(searchLower);
                    const matchEx = item.examples.some(ex => ex.jp.toLowerCase().includes(searchLower) || ex.vi.toLowerCase().includes(searchLower));

                    if (!matchTitle && !matchFormula && !matchMeaning && !matchNotes && !matchLesson && !matchTag && !matchEx) {{
                        return false;
                    }}
                }}

                return true;
            }});

            document.getElementById('filterCountLabel').textContent = `Đang hiển thị ${{filtered.length}} / ${{GRAMMAR_DATA.length}} chuyên đề ngữ pháp`;

            if (filtered.length === 0) {{
                container.innerHTML = `
                    <div style="grid-column: 1 / -1; background:#ffffff; border-radius:16px; padding:50px 20px; text-align:center; border:1px dashed #cbd5e1;">
                        <div style="font-size:3rem; margin-bottom:12px;">🔍</div>
                        <h3 style="font-size:1.2rem; font-weight:800; color:#1e293b; margin-bottom:6px;">Không tìm thấy mẫu ngữ pháp nào phù hợp</h3>
                        <p style="font-size:0.9rem; color:#64748b; margin-bottom:18px;">Hãy thử tìm từ khóa khác (ví dụ: xin phép, đang làm, ている, そう, khuyên...)</p>
                        <button type="button" class="level-pill active" onclick="resetAllFilters()">Xem tất cả</button>
                    </div>
                `;
                return;
            }}

            container.innerHTML = filtered.map(item => {{
                const isLearned = learnedSet.has(item.id);
                const levelCls = item.level === 'A1' ? 'level-a1' : (item.level === 'A2-1' ? 'level-a2-1' : 'level-a2-2');

                const examplesHtml = item.examples.map(ex => `
                    <div class="example-item">
                        <div class="example-jp-row">
                            <span class="example-jp jp-text">${{ex.ruby || ex.jp}}</span>
                            <button type="button" class="btn-speak" title="Nghe phát âm" onclick="speakText('${{ex.jp.replace(/'/g, "\\\\'") }}')">🔊</button>
                        </div>
                        <div class="example-vi">${{ex.vi}}</div>
                    </div>
                `).join('');

                return `
                    <div class="grammar-card ${{isLearned ? 'is-learned' : ''}}" id="grammarCard_${{item.id}}">
                        <!-- Card Header -->
                        <div class="card-header">
                            <div>
                                <div class="card-meta">
                                    <span class="level-badge ${{levelCls}}">${{item.levelName}}</span>
                                    <span class="lesson-badge">Bài ${{item.lesson}}</span>
                                    <span class="tag-pill">${{item.tag}}</span>
                                </div>
                            </div>
                        </div>

                        <!-- Card Title -->
                        <h2 class="card-title">${{item.title}}</h2>

                        <!-- Formula -->
                        <div class="formula-box">
                            <div style="font-size:0.75rem; font-weight:800; color:#a5b4fc; text-transform:uppercase; margin-bottom:4px; letter-spacing:0.05em;">CÔNG THỨC MẪU:</div>
                            <div class="jp-text">${{item.formula}}</div>
                        </div>

                        <!-- Meaning -->
                        <div class="meaning-box">
                            <div class="meaning-label">Ý Nghĩa & Bản Chất:</div>
                            <div>${{item.meaning}}</div>
                        </div>

                        <!-- Notes -->
                        <div class="notes-box">
                            <div style="font-weight:800; margin-bottom:2px;">💡 Lưu ý cốt lõi:</div>
                            <div>${{item.notes}}</div>
                        </div>

                        <!-- Examples -->
                        <div class="examples-section">
                            <div class="examples-title">Đàm Thoại & Câu Ví Dụ Tiêu Biểu:</div>
                            ${{examplesHtml}}
                        </div>

                        <!-- Actions & In-Card Quiz Toggle -->
                        <div class="card-actions">
                            <button type="button" class="learn-toggle-btn ${{isLearned ? 'checked' : ''}}" id="learnToggleBtn_${{item.id}}" onclick="toggleLearned(${{item.id}}, event)">
                                ${{isLearned ? '✓ Đã thuộc' : '○ Đánh dấu đã hiểu'}}
                            </button>
                            <button type="button" class="card-quiz-btn" onclick="toggleCardQuiz(${{item.id}})">
                                <span>✍️ Kiểm tra nhanh</span>
                                <span>▾</span>
                            </button>
                        </div>

                        <!-- In-card Mini Quiz Accordion -->
                        <div class="card-inline-quiz" id="cardInlineQuiz_${{item.id}}">
                            <div class="inline-quiz-q jp-text">${{item.quiz.q}}</div>
                            <div class="inline-quiz-options">
                                ${{item.quiz.options.map((opt, optIdx) => `
                                    <button type="button" class="inline-opt-btn" onclick="checkCardQuiz(${{item.id}}, ${{optIdx}}, this)">
                                        ${{opt}}
                                    </button>
                                `).join('')}}
                            </div>
                            <div class="inline-explain" id="cardInlineExplain_${{item.id}}">
                                💡 <strong>Giải thích:</strong> ${{item.quiz.explain}}
                            </div>
                        </div>
                    </div>
                `;
            }}).join('');
        }}

        // IN-CARD QUIZ LOGIC
        function toggleCardQuiz(id) {{
            const el = document.getElementById(`cardInlineQuiz_${{id}}`);
            if (el) {{
                el.classList.toggle('show');
            }}
        }}

        function checkCardQuiz(itemId, optIdx, btn) {{
            const item = GRAMMAR_DATA.find(g => g.id === itemId);
            if (!item) return;

            const parent = btn.parentElement;
            const buttons = parent.querySelectorAll('.inline-opt-btn');
            buttons.forEach(b => b.disabled = true);

            const isCorrect = (optIdx === item.quiz.correct);
            if (isCorrect) {{
                btn.classList.add('correct');
                showToast('Chính xác! 🌟');
            }} else {{
                btn.classList.add('wrong');
                buttons[item.quiz.correct].classList.add('correct');
                showToast('Chưa đúng rồi! Hãy đọc giải thích bên dưới nhé.');
            }}

            const explainEl = document.getElementById(`cardInlineExplain_${{itemId}}`);
            if (explainEl) {{
                explainEl.classList.add('show');
            }}
        }}

        // FILTER HANDLERS
        function handleSearch() {{
            currentSearch = document.getElementById('grammarSearchInput').value;
            renderGrammarCards();
        }}

        function setLevelFilter(level, btn) {{
            currentLevel = level;
            document.querySelectorAll('.level-pill').forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            renderGrammarCards();
        }}

        function setCategoryFilter(cat, btn) {{
            currentCat = cat;
            document.querySelectorAll('.cat-chip').forEach(c => c.classList.remove('active'));
            btn.classList.add('active');
            renderGrammarCards();
        }}

        function resetAllFilters() {{
            currentLevel = 'all';
            currentCat = 'all';
            currentSearch = '';
            document.getElementById('grammarSearchInput').value = '';
            document.querySelectorAll('.level-pill').forEach((p, idx) => p.classList.toggle('active', idx === 0));
            document.querySelectorAll('.cat-chip').forEach((c, idx) => c.classList.toggle('active', idx === 0));
            renderGrammarCards();
        }}

        // FURIGANA TOGGLE LOGIC
        let furiganaEnabled = localStorage.getItem('marugoto_furigana_enabled') !== 'false'; // Mặc định BẬT

        function applyFuriganaState() {{
            const btn = document.getElementById('btnFuriganaToggle');
            const label = document.getElementById('furiganaBtnLabel');
            if (furiganaEnabled) {{
                document.body.classList.remove('hide-furigana');
                if (btn) btn.classList.remove('off');
                if (label) label.textContent = 'Furigana: BẬT';
            }} else {{
                document.body.classList.add('hide-furigana');
                if (btn) btn.classList.add('off');
                if (label) label.textContent = 'Furigana: TẮT';
            }}
        }}

        function toggleFurigana() {{
            furiganaEnabled = !furiganaEnabled;
            localStorage.setItem('marugoto_furigana_enabled', furiganaEnabled);
            applyFuriganaState();
        }}

        // TAB SWITCHING
        function switchMainTab(tab) {{
            const explorer = document.getElementById('tabExplorerView');
            const verbLab = document.getElementById('tabVerbLabView');
            const btnExp = document.getElementById('btnTabExplorer');
            const btnLab = document.getElementById('btnTabVerbLab');

            if (tab === 'explorer') {{
                explorer.style.display = 'block';
                verbLab.classList.remove('active');
                btnExp.classList.add('active');
                btnLab.classList.remove('active');
            }} else if (tab === 'verbLab') {{
                explorer.style.display = 'none';
                verbLab.classList.add('active');
                btnExp.classList.remove('active');
                btnLab.classList.add('active');
            }}
        }}

        // VERB MORPHING LAB LOGIC
        let activeVerbIdx = 0;

        function initVerbLab() {{
            const picker = document.getElementById('verbPickerRow');
            picker.innerHTML = VERB_DATA.map((v, i) => `
                <button type="button" class="verb-select-pill ${{i === 0 ? 'active' : ''}}" onclick="selectVerbLab(${{i}}, this)">
                    ${{v.kanji}} (${{v.vi}})
                </button>
            `).join('');
            updateVerbLabDisplay(0);
        }}

        function selectVerbLab(idx, btn) {{
            activeVerbIdx = idx;
            document.querySelectorAll('.verb-select-pill').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            updateVerbLabDisplay(idx);
        }}

        function updateVerbLabDisplay(idx) {{
            const v = VERB_DATA[idx];
            document.getElementById('labHeroKanji').textContent = `${{v.kanji}} (${{v.kana}})`;
            document.getElementById('labHeroVi').textContent = v.vi;
            document.getElementById('labHeroGroup').textContent = v.group;

            document.getElementById('mMasu').textContent = v.masu;
            document.getElementById('mRu').textContent = v.ru;
            document.getElementById('mTe').textContent = v.te;
            document.getElementById('mTa').textContent = v.ta;
            document.getElementById('mNai').textContent = v.nai;
            document.getElementById('mTara').textContent = v.tara;
            document.getElementById('mTari').textContent = v.tari;

            document.getElementById('mExJp').innerHTML = v.exRuby || v.ex;
            document.getElementById('mExVi').textContent = v.exVi;
        }}

        // MASTER REFLEX QUIZ (RANDOM 20 QUESTIONS)
        let quizQuestions = [];
        let quizCurrentIndex = 0;
        let quizScore = 0;

        function startMasterQuiz() {{
            // Shuffle all grammar quizzes and take 20
            const shuffled = [...GRAMMAR_DATA].sort(() => 0.5 - Math.random());
            quizQuestions = shuffled.slice(0, 20);
            quizCurrentIndex = 0;
            quizScore = 0;

            document.getElementById('quizModalOverlay').classList.add('show');
            document.getElementById('quizQuestionView').style.display = 'block';
            document.getElementById('quizResultView').style.display = 'none';

            loadQuizStep();
        }}

        function closeQuizModal() {{
            document.getElementById('quizModalOverlay').classList.remove('show');
        }}

        function loadQuizStep() {{
            const item = quizQuestions[quizCurrentIndex];
            document.getElementById('quizStepBadge').textContent = `Câu ${{quizCurrentIndex + 1}} / ${{quizQuestions.length}}`;
            document.getElementById('quizScoreBadge').textContent = `Điểm: ${{quizScore}}`;

            document.getElementById('quizQuestionText').innerHTML = `
                <div style="font-size:0.75rem; font-weight:800; color:#6366f1; text-transform:uppercase; margin-bottom:6px;">${{item.levelName}} • Bài ${{item.lesson}}:</div>
                <div>${{item.quiz.q}}</div>
            `;

            const list = document.getElementById('quizOptionsList');
            list.innerHTML = item.quiz.options.map((opt, idx) => `
                <button type="button" class="quiz-opt-btn" onclick="selectQuizAnswer(${{idx}}, this)">
                    <span>${{opt}}</span>
                    <span style="opacity:0.4;">○</span>
                </button>
            `).join('');

            const explain = document.getElementById('quizExplainBox');
            explain.classList.remove('show');
            explain.innerHTML = '';

            document.getElementById('btnNextQuiz').style.display = 'none';
        }}

        function selectQuizAnswer(selectedIdx, btn) {{
            const item = quizQuestions[quizCurrentIndex];
            const list = document.getElementById('quizOptionsList');
            const buttons = list.querySelectorAll('.quiz-opt-btn');
            buttons.forEach(b => b.disabled = true);

            const isCorrect = (selectedIdx === item.quiz.correct);
            if (isCorrect) {{
                btn.classList.add('correct');
                btn.querySelector('span:last-child').textContent = '✓';
                quizScore++;
                document.getElementById('quizScoreBadge').textContent = `Điểm: ${{quizScore}}`;
                speakText(item.quiz.q.replace(/\\[____\\]/g, item.quiz.options[selectedIdx]));
            }} else {{
                btn.classList.add('wrong');
                btn.querySelector('span:last-child').textContent = '✕';
                buttons[item.quiz.correct].classList.add('correct');
                buttons[item.quiz.correct].querySelector('span:last-child').textContent = '✓';
            }}

            const explain = document.getElementById('quizExplainBox');
            explain.innerHTML = `💡 <strong>Giải thích ngữ pháp:</strong> ${{item.quiz.explain}}`;
            explain.classList.add('show');

            const nextBtn = document.getElementById('btnNextQuiz');
            if (quizCurrentIndex < quizQuestions.length - 1) {{
                nextBtn.textContent = 'Câu tiếp theo →';
            }} else {{
                nextBtn.textContent = 'Xem kết quả tổng kết 🏆';
            }}
            nextBtn.style.display = 'inline-block';
        }}

        function nextQuizQuestion() {{
            quizCurrentIndex++;
            if (quizCurrentIndex < quizQuestions.length) {{
                loadQuizStep();
            }} else {{
                showQuizResult();
            }}
        }}

        function showQuizResult() {{
            document.getElementById('quizQuestionView').style.display = 'none';
            const resView = document.getElementById('quizResultView');
            resView.style.display = 'block';

            const scoreEl = document.getElementById('quizResultScore');
            const titleEl = document.getElementById('quizResultTitle');
            const descEl = document.getElementById('quizResultDesc');
            const trophyEl = document.getElementById('quizTrophy');

            scoreEl.textContent = `${{quizScore}} / ${{quizQuestions.length}}`;

            if (quizScore >= 18) {{
                trophyEl.textContent = '🏆';
                titleEl.textContent = 'Xuất Sắc Tuyệt Vời!';
                descEl.textContent = 'Bạn đã làm chủ hoàn toàn ngữ pháp Marugoto A1 & A2! Tốc độ phản xạ rất chuẩn.';
            }} else if (quizScore >= 14) {{
                trophyEl.textContent = '🌟';
                titleEl.textContent = 'Làm Rất Tốt!';
                descEl.textContent = 'Kiến thức ngữ pháp rất vững. Hãy xem lại các câu chưa đúng để đạt điểm tối đa nhé.';
            }} else {{
                trophyEl.textContent = '💡';
                titleEl.textContent = 'Tiếp Tục Ôn Luyện Nhé!';
                descEl.textContent = 'Ngữ pháp cần sự lặp lại liên tục. Hãy sử dụng các thẻ tóm tắt và nghe ví dụ audio để ghi nhớ sâu hơn.';
            }}
        }}

        // HUB DROPDOWN HELPER
        function toggleLessonsDropdown(e) {{
            if (e) e.stopPropagation();
            const m = document.getElementById('lessonsDropdownMenu');
            if (m) m.classList.toggle('show');
        }}

        window.addEventListener('click', () => {{
            const m = document.getElementById('lessonsDropdownMenu');
            if (m) m.classList.remove('show');
        }});

        // INIT ON DOM LOADED
        document.addEventListener('DOMContentLoaded', () => {{
            loadProgress();
            applyFuriganaState();
            renderGrammarCards();
            initVerbLab();
        }});
    </script>
</body>
</html>
"""
    return html

def main():
    print("Building Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html...")
    html_content = generate_html()
    output_path = "/Users/dangvu/Downloads/nhật/Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated successfully! Size: {os.path.getsize(output_path)} bytes.")

if __name__ == "__main__":
    main()
