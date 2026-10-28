# -*- coding: utf-8 -*-
import json
import os

from lesson_data_12_18 import LESSON_CONFIGS

def build_lesson_html(cfg):
    num = cfg["num"]
    title_vi = cfg["title_vi"]
    title_jp = cfg["title_jp"]
    topic_name = cfg["topic_name"]
    topic_badge = cfg["topic_badge"]
    desc = cfg["desc"]
    grammars = cfg["grammars"]
    vocab = cfg["vocab"]
    kanjis = cfg["kanjis"]
    quizzes = cfg["quizzes"]
    verb_lab = cfg["verb_lab"]
    dialogue = cfg["dialogue"]

    # Generate dock pills for Lessons 1 to 18
    icons = {
        1: "🏠", 2: "🎨", 3: "🍁", 4: "⛅", 5: "🏙️", 6: "🗺️",
        7: "⏰", 8: "⛩️", 9: "🗣️", 10: "🌟", 11: "🍱", 12: "🍜",
        13: "✈️", 14: "💻", 15: "🏥", 16: "🏃", 17: "🎁", 18: "👘"
    }
    pills_html = []
    for i in range(1, 19):
        active_cls = " active" if i == num else ""
        icon = icons.get(i, "📘")
        if i in [10, 11, 12, 13, 14, 15, 16, 17, 18]:
            pills_html.append(f'                <a href="Marugoto_A2_Lesson_{i}.html" class="dock-pill{active_cls}"><span class="pill-ico">{icon}</span> Bài {i}</a>')
        else:
            pills_html.append(f'                <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l{i}" class="dock-pill{active_cls}"><span class="pill-ico">{icon}</span> Bài {i}</a>')
    dock_pills_str = "\n".join(pills_html)

    # Tools menu items
    tools_html = []
    tools_html.append('                        <a href="index.html" class="dock-tool-item">🌸 Thể TE (～て)</a>')
    tools_html.append('                        <a href="the_ru.html" class="dock-tool-item">📘 Thể RU (Từ Điển)</a>')
    tools_html.append('                        <a href="kanji_a2.html" class="dock-tool-item">⛩️ Học Kanji & Nét Viết</a>')
    tools_html.append('                        <a href="Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="dock-tool-item">📖 Kho Từ Vựng A1-A2 (600+ Từ)</a>')
    tools_html.append('                        <a href="On_Tap_Mini_Test_A2_5_8.html" class="dock-tool-item">🎯 Cẩm Nang Toàn Diện 10 Bài</a>')
    tools_html.append('                        <a href="De_Thi_Thu_Marugoto_A2_5_8.html" class="dock-tool-item">📝 5 Mã Đề Thi Thử</a>')
    for i in range(10, 19):
        active_tool = " active" if i == num else ""
        icon = icons.get(i, "📘")
        tools_html.append(f'                        <a href="Marugoto_A2_Lesson_{i}.html" class="dock-tool-item{active_tool}">{icon} Web Chuyên Sâu Bài {i} ✨</a>')
    dock_tools_str = "\n".join(tools_html)

    # Grammars HTML
    grammars_html = []
    for g_idx, g in enumerate(grammars):
        ex_items = []
        for ex in g["examples"]:
            ex_items.append(f"""                    <div class="example-item">
                        <div class="ex-text-wrap">
                            <div class="ex-jp">{ex["jp"]}</div>
                            <div class="ex-vi">{ex["vi"]}</div>
                        </div>
                        <button type="button" class="btn-speak" onclick="speakText('{ex["jp"].replace("'", "\\'")}')">🔊</button>
                    </div>""")
        ex_str = "\n".join(ex_items)

        table_str = ""
        if "table" in g and g["table"]:
            rows = []
            for r in g["table"]["rows"]:
                rows.append(f"""                        <tr>
                            <td><strong style="color:var(--primary-dark); font-size:1.02rem;">{r[0]}</strong></td>
                            <td>{r[1]}</td>
                            <td>{r[2]}</td>
                        </tr>""")
            table_str = f"""                <table class="comparison-table">
                    <thead>
                        <tr>
                            <th>{g["table"]["headers"][0]}</th>
                            <th>{g["table"]["headers"][1]}</th>
                            <th>{g["table"]["headers"][2]}</th>
                        </tr>
                    </thead>
                    <tbody>
{"".join(rows)}
                    </tbody>
                </table>"""

        grammars_html.append(f"""        <section class="content-section" id="sec-grammar{g_idx+1}">
            <div class="section-header">
                <h2 class="section-title"><span>{g["icon"]}</span> {g_idx+1}. {g["title"]}</h2>
                <span class="section-tag">{g["tag"]}</span>
            </div>

            <p style="margin-bottom: 16px; color: #334155;">
                {g["intro"]}
            </p>

            <div class="grammar-card">
                <div class="rule-box" style="border-left-color: {g.get("color", "var(--primary)")};">
                    <div class="rule-formula" style="color: {g.get("color_dark", "var(--primary-dark)")};">{g["formula"]}</div>
                    <div class="rule-meaning">
                        {g["meaning"]}
                    </div>
                </div>

                {table_str}

                <div class="example-list">
{ex_str}
                </div>
            </div>
        </section>""")

    all_grammars_str = "\n\n".join(grammars_html)

    # Kanji Cards HTML
    kanji_cards_html = []
    for k in kanjis:
        kanji_cards_html.append(f"""                <div class="kanji-detail-card">
                    <div class="kanji-big-char">{k["char"]}</div>
                    <div class="kanji-info">
                        <div class="kanji-hv-title">{k["hv"]} <span class="kanji-strokes-badge">{k["strokes"]} nét</span></div>
                        <div class="kanji-readings">
                            <strong>Kun:</strong> {k["kun"]}<br>
                            <strong>On:</strong> {k["on"]}<br>
                            <strong>Từ ví dụ:</strong> {k["ex"]}
                        </div>
                        <div class="kanji-mnemonic">💡 Mẹo nhớ: {k["mnemonic"]}</div>
                    </div>
                </div>""")
    kanji_str = "\n".join(kanji_cards_html)

    # Verb lab HTML
    verb_lab_boxes = f"""            <div class="morph-grid">
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][0]}</div>
                    <div class="morph-val" id="morphMasu">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;" id="morphVi">---</div>
                </div>
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][1]}</div>
                    <div class="morph-val" style="color:#0284c7;" id="morphTe">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">Gốc biến đổi</div>
                </div>
                <div class="morph-box featured">
                    <div class="morph-tag">{verb_lab["labels"][2]}</div>
                    <div class="morph-val" style="color:#059669;" id="morphTeIki">---</div>
                    <div style="font-size:0.8rem; color:#047857; margin-top:4px;">Cấu trúc trọng tâm 1</div>
                </div>
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][3]}</div>
                    <div class="morph-val" style="color:#7c3aed;" id="morphTeKi">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">Cấu trúc trọng tâm 2</div>
                </div>
                <div class="morph-box">
                    <div class="morph-tag">{verb_lab["labels"][4]}</div>
                    <div class="morph-val" style="color:#ea580c;" id="morphMashou">---</div>
                    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">Mẫu câu giao tiếp</div>
                </div>
            </div>"""

    # Dialogue steps data as json
    dialogue_json = json.dumps(dialogue["steps"], ensure_ascii=False)
    vocab_json = json.dumps(vocab, ensure_ascii=False)
    verb_lab_json = json.dumps(verb_lab["verbs"], ensure_ascii=False)
    quizzes_json = json.dumps(quizzes, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>Cẩm Nang & Luyện Tập Toàn Diện Bài {num} - Marugoto A2-2 | {title_jp}</title>
    <meta name="description" content="Chinh phục toàn diện Marugoto A2 Bài {num}: {title_jp}. Đầy đủ ngữ pháp, 3D Flashcard từ vựng, máy biến thể và Mini Test 15 câu có giải thích chi tiết.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <!-- Animate UI Core (Spring Physics & Micro-Interactions) -->
    <link rel="stylesheet" href="animate-ui.css">
    <script src="animate-ui.js" defer></script>
    <!-- Unified Tokyo Audio Engine -->
    <script src="audio-engine.js"></script>
    <style>
        :root {{
            --primary: #059669;
            --primary-dark: #047857;
            --primary-light: #10b981;
            --primary-soft: #ecfdf5;
            --accent: #f59e0b;
            --accent-orange: #ea580c;
            --accent-soft: #fffbeb;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --bg-light: #f8fafc;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --shadow-subtle: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            --shadow-card: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
            --shadow-hover: 0 20px 25px -5px rgba(5, 150, 105, 0.12), 0 8px 10px -6px rgba(5, 150, 105, 0.08);
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

        /* Sticky Floating Dock */
        .global-sticky-dock-wrapper {{
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(226, 232, 240, 0.85);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
        }}

        .global-sticky-dock {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 10px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }}

        .dock-brand {{
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
            color: var(--primary-dark);
            font-weight: 800;
            font-size: 1.05rem;
            flex-shrink: 0;
        }}

        .dock-pill-track {{
            display: flex;
            align-items: center;
            gap: 6px;
            overflow-x: auto;
            scrollbar-width: none;
            padding: 2px 0;
        }}

        .dock-pill-track::-webkit-scrollbar {{
            display: none;
        }}

        .dock-pill {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
            text-decoration: none;
            color: #64748b;
            background: #f1f5f9;
            border: 1px solid #e2e8f0;
            white-space: nowrap;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .dock-pill:hover {{
            color: var(--primary-dark);
            background: var(--primary-soft);
            border-color: #a7f3d0;
            transform: translateY(-1px);
        }}

        .dock-pill.active {{
            color: #ffffff;
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
            border-color: #047857;
            box-shadow: 0 2px 6px rgba(5, 150, 105, 0.35);
        }}

        .dock-actions {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-shrink: 0;
        }}

        .dock-action-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: #334155;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .dock-action-btn:hover {{
            background: #f8fafc;
            border-color: #94a3b8;
            color: #0f172a;
        }}

        .dock-dropdown-wrapper {{
            position: relative;
        }}

        .dock-tools-menu {{
            display: none;
            position: absolute;
            top: calc(100% + 8px);
            right: 0;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.12);
            padding: 8px;
            min-width: 240px;
            max-height: 480px;
            overflow-y: auto;
            z-index: 1010;
        }}

        .dock-tools-menu.show {{
            display: block;
            animation: fadeInDown 0.2s ease;
        }}

        .dock-tool-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 600;
            color: #334155;
            text-decoration: none;
            transition: all 0.15s;
        }}

        .dock-tool-item:hover, .dock-tool-item.active {{
            background: var(--primary-soft);
            color: var(--primary-dark);
        }}

        /* Mega Drawer Sheet */
        .global-mega-sheet {{
            display: none;
            position: fixed;
            top: 54px;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(8px);
            z-index: 1050;
            padding: 20px;
            overflow-y: auto;
        }}

        .global-mega-sheet.show {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
        }}

        .sheet-content {{
            background: #ffffff;
            border-radius: 20px;
            max-width: 980px;
            width: 100%;
            padding: 28px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            margin-top: 10px;
        }}

        .sheet-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 14px;
            margin-bottom: 20px;
        }}

        .sheet-header-title {{
            font-size: 1.25rem;
            font-weight: 800;
            color: #0f172a;
        }}

        .sheet-close-btn {{
            background: #f1f5f9;
            border: none;
            border-radius: 50%;
            width: 36px;
            height: 36px;
            font-size: 1.1rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #64748b;
        }}

        .sheet-topics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
        }}

        .sheet-topic-card {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 16px;
        }}

        .sheet-topic-badge {{
            font-size: 0.75rem;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--primary-dark);
            margin-bottom: 8px;
        }}

        .sheet-lesson-link {{
            display: block;
            text-decoration: none;
            padding: 8px 10px;
            border-radius: 8px;
            margin-bottom: 6px;
            transition: all 0.15s;
        }}

        .sheet-lesson-link:hover {{
            background: #ffffff;
            box-shadow: var(--shadow-subtle);
        }}

        .sheet-lesson-name {{
            font-size: 0.9rem;
            font-weight: 700;
            color: #1e293b;
        }}

        .sheet-lesson-desc {{
            font-size: 0.76rem;
            color: #64748b;
        }}

        /* Section Nav */
        .section-nav {{
            position: sticky;
            top: 54px;
            z-index: 900;
            background: #ffffff;
            border-bottom: 1px solid #e2e8f0;
            padding: 8px 16px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.03);
            display: flex;
            gap: 8px;
            overflow-x: auto;
            scrollbar-width: none;
        }}

        .section-nav::-webkit-scrollbar {{
            display: none;
        }}

        .sec-link {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            text-decoration: none;
            color: #475569;
            background: #f1f5f9;
            white-space: nowrap;
            transition: all 0.2s;
        }}

        .sec-link:hover, .sec-link.active {{
            background: var(--primary-soft);
            color: var(--primary-dark);
        }}

        /* Container & Hero */
        .main-container {{
            max-width: 1100px;
            margin: 24px auto;
            padding: 0 20px;
        }}

        .hero-banner {{
            background: linear-gradient(135deg, #064e3b 0%, #065f46 45%, #047857 100%);
            border-radius: var(--radius-lg);
            padding: 40px 32px;
            color: #ffffff;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-card);
            margin-bottom: 32px;
        }}

        .hero-banner::after {{
            content: "{cfg.get('hero_emoji', '🍱')}";
            position: absolute;
            right: 20px;
            bottom: 10px;
            font-size: 5rem;
            opacity: 0.15;
            pointer-events: none;
        }}

        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(16, 185, 129, 0.25);
            border: 1px solid rgba(52, 211, 153, 0.4);
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            color: #6ee7b7;
            margin-bottom: 14px;
        }}

        .hero-title {{
            font-size: 2.1rem;
            font-weight: 900;
            line-height: 1.25;
            margin-bottom: 12px;
            letter-spacing: -0.5px;
        }}

        .hero-jp-quote {{
            font-family: var(--jp-font);
            font-size: 1.35rem;
            font-weight: 700;
            color: #fef08a;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .hero-subtitle {{
            font-size: 1.02rem;
            color: #e2e8f0;
            max-width: 800px;
            margin-bottom: 24px;
        }}

        .hero-stats-row {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px;
        }}

        .stat-card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 16px;
            text-align: center;
        }}

        .stat-number {{
            font-size: 1.6rem;
            font-weight: 900;
            color: #a7f3d0;
            line-height: 1;
            margin-bottom: 4px;
        }}

        .stat-label {{
            font-size: 0.78rem;
            color: #e2e8f0;
            font-weight: 600;
        }}

        /* Content Sections */
        .content-section {{
            background: #ffffff;
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 32px;
            box-shadow: var(--shadow-subtle);
            border: 1px solid var(--border-color);
            scroll-margin-top: 130px;
        }}

        .section-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 16px;
        }}

        .section-title {{
            font-size: 1.4rem;
            font-weight: 800;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .section-tag {{
            font-size: 0.78rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 999px;
            background: var(--primary-soft);
            color: var(--primary-dark);
            text-transform: uppercase;
        }}

        /* Grammar Card */
        .grammar-card {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 22px;
            margin-bottom: 24px;
        }}

        .rule-box {{
            background: #ffffff;
            border-left: 5px solid var(--primary);
            border-radius: 8px;
            padding: 16px 20px;
            margin: 14px 0;
            box-shadow: var(--shadow-subtle);
        }}

        .rule-formula {{
            font-family: var(--jp-font);
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 6px;
        }}

        .rule-meaning {{
            font-size: 0.95rem;
            color: #334155;
            font-weight: 600;
        }}

        .example-list {{
            margin-top: 16px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .example-item {{
            background: #ffffff;
            border-radius: 10px;
            padding: 12px 16px;
            border: 1px solid #e2e8f0;
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 12px;
            transition: all 0.2s;
        }}

        .example-item:hover {{
            border-color: #a7f3d0;
            box-shadow: var(--shadow-subtle);
        }}

        .ex-text-wrap {{
            flex-grow: 1;
        }}

        .ex-jp {{
            font-family: var(--jp-font);
            font-size: 1.05rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 3px;
        }}

        .ex-vi {{
            font-size: 0.88rem;
            color: #475569;
        }}

        .btn-speak {{
            background: #ecfdf5;
            border: 1px solid #a7f3d0;
            color: var(--primary-dark);
            border-radius: 50%;
            width: 36px;
            height: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            flex-shrink: 0;
            transition: all 0.2s;
        }}

        .btn-speak:hover {{
            background: var(--primary);
            color: #ffffff;
            transform: scale(1.08);
        }}

        .comparison-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 0.92rem;
            background: #ffffff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: var(--shadow-subtle);
        }}

        .comparison-table th {{
            background: #065f46;
            color: #ffffff;
            padding: 12px 16px;
            text-align: left;
            font-weight: 700;
        }}

        .comparison-table td {{
            padding: 12px 16px;
            border-bottom: 1px solid #e2e8f0;
        }}

        .comparison-table tr:last-child td {{
            border-bottom: none;
        }}

        .comparison-table tr:nth-child(even) {{
            background: #f8fafc;
        }}

        /* Morph Lab */
        .verb-picker-row {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 24px;
            align-items: center;
        }}

        .verb-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 9px 18px;
            border-radius: 999px;
            font-size: 0.92rem;
            font-weight: 700;
            border: 1.5px solid #cbd5e1;
            background: #ffffff;
            color: #334155;
            cursor: pointer;
            white-space: nowrap;
            flex-shrink: 0;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }}

        .verb-pill:hover {{
            border-color: var(--primary);
            color: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(5, 150, 105, 0.15);
        }}

        .verb-pill.active {{
            background: var(--primary) !important;
            color: #ffffff !important;
            border-color: var(--primary-dark) !important;
            box-shadow: 0 4px 12px rgba(5, 150, 105, 0.35) !important;
            transform: translateY(-1px);
        }}

        .verb-pill .pill-kanji {{
            font-family: var(--jp-font);
            font-weight: 800;
            font-size: 0.95rem;
        }}

        .verb-pill .pill-meaning {{
            font-size: 0.8rem;
            font-weight: 600;
            opacity: 0.75;
        }}

        .verb-pill.active .pill-meaning {{
            opacity: 0.92;
            color: #ecfdf5;
        }}

        .morph-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 14px;
            margin-bottom: 18px;
        }}

        .morph-box {{
            background: #ffffff;
            border: 2px solid #e2e8f0;
            border-radius: 14px;
            padding: 18px 16px;
            text-align: center;
            transition: all 0.25s;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 120px;
        }}

        .morph-box:hover {{
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-card);
        }}

        .morph-box.featured {{
            border-color: var(--primary);
            background: var(--primary-soft);
        }}

        .morph-tag {{
            font-size: 0.75rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: #64748b;
            margin-bottom: 8px;
        }}

        .morph-val {{
            font-family: var(--jp-font);
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--text-dark);
            margin: 6px 0;
            word-break: keep-all;
            white-space: normal;
        }}
            padding: 16px;
            text-align: center;
            transition: all 0.25s;
        }}

        .morph-box.featured {{
            border-color: var(--primary);
            background: #ecfdf5;
        }}

        .morph-tag {{
            font-size: 0.72rem;
            font-weight: 800;
            text-transform: uppercase;
            color: #64748b;
            margin-bottom: 6px;
        }}

        .morph-box.featured .morph-tag {{
            color: var(--primary-dark);
        }}

        .morph-val {{
            font-family: var(--jp-font);
            font-size: 1.15rem;
            font-weight: 800;
            color: #0f172a;
        }}

        .morph-ex-box {{
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 10px;
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        /* Dialogue */
        .dialogue-wrap {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 24px;
        }}

        .chat-container {{
            display: flex;
            flex-direction: column;
            gap: 14px;
            margin-bottom: 20px;
        }}

        .chat-bubble {{
            display: flex;
            gap: 12px;
            max-width: 80%;
        }}

        .chat-bubble.bot {{
            align-self: flex-start;
        }}

        .chat-bubble.user {{
            align-self: flex-end;
            flex-direction: row-reverse;
        }}

        .chat-avatar {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            flex-shrink: 0;
        }}

        .chat-msg {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            padding: 12px 16px;
            box-shadow: var(--shadow-subtle);
        }}

        .chat-bubble.user .chat-msg {{
            background: #059669;
            color: #ffffff;
            border-color: #047857;
        }}

        .chat-name {{
            font-size: 0.72rem;
            font-weight: 800;
            color: #64748b;
            margin-bottom: 2px;
        }}

        .chat-bubble.user .chat-name {{
            color: #a7f3d0;
            text-align: right;
        }}

        .chat-jp {{
            font-family: var(--jp-font);
            font-size: 0.98rem;
            font-weight: 700;
        }}

        .chat-vi {{
            font-size: 0.8rem;
            color: #64748b;
            margin-top: 3px;
        }}

        .chat-bubble.user .chat-vi {{
            color: #e2e8f0;
        }}

        .chat-options-panel {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            padding: 16px;
        }}

        .chat-opt-title {{
            font-size: 0.85rem;
            font-weight: 800;
            color: #334155;
            margin-bottom: 10px;
        }}

        .chat-btn-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 10px;
        }}

        .btn-chat-choice {{
            background: #f8fafc;
            border: 1.5px solid #cbd5e1;
            border-radius: 10px;
            padding: 10px 14px;
            font-size: 0.88rem;
            font-weight: 700;
            color: #1e293b;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
        }}

        .btn-chat-choice:hover {{
            border-color: var(--primary);
            background: var(--primary-soft);
            color: var(--primary-dark);
        }}

        /* Flashcards 3D */
        .vocab-filter-bar {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 22px;
        }}

        .vocab-filter-btn {{
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: #475569;
            cursor: pointer;
            transition: all 0.15s;
        }}

        .vocab-filter-btn:hover, .vocab-filter-btn.active {{
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary-dark);
        }}

        .vocab-stats-badge {{
            margin-left: auto;
            font-size: 0.85rem;
            color: #64748b;
            font-weight: 700;
        }}

        .flashcards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 20px;
        }}

        .flashcard {{
            background: transparent;
            perspective: 1000px;
            height: 310px;
            cursor: pointer;
        }}

        .fc-inner {{
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            box-shadow: var(--shadow-subtle);
            border-radius: 16px;
        }}

        .flashcard.flipped .fc-inner {{
            transform: rotateY(180deg);
        }}

        .fc-front, .fc-back {{
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 16px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border: 1px solid #e2e8f0;
            background: #ffffff;
        }}

        .fc-back {{
            transform: rotateY(180deg);
            background: #f8fafc;
            border-color: #a7f3d0;
            text-align: left;
        }}

        .fc-badge {{
            display: inline-block;
            align-self: flex-start;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 999px;
            background: var(--primary-soft);
            color: var(--primary-dark);
        }}

        .fc-illustration {{
            width: 100%;
            height: 105px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            overflow: hidden;
        }}

        .fc-illustration svg {{
            width: 100%;
            height: 100%;
        }}

        .fc-jp {{
            font-family: var(--jp-font);
            font-size: 1.35rem;
            font-weight: 900;
            color: #0f172a;
        }}

        .fc-kana {{
            font-family: var(--jp-font);
            font-size: 0.9rem;
            color: var(--primary);
            font-weight: 700;
        }}

        .fc-romaji {{
            font-size: 0.78rem;
            color: #94a3b8;
        }}

        .fc-hint {{
            font-size: 0.72rem;
            color: #94a3b8;
            font-weight: 600;
        }}

        .fc-back-meaning {{
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 8px;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 6px;
        }}

        .fc-back-ex-jp {{
            font-family: var(--jp-font);
            font-size: 0.92rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 4px;
        }}

        .fc-back-ex-vi {{
            font-size: 0.8rem;
            color: #475569;
        }}

        .fc-back-actions {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 10px;
        }}

        .btn-learned {{
            font-size: 0.75rem;
            font-weight: 700;
            padding: 5px 10px;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            background: #ffffff;
            color: #475569;
            cursor: pointer;
        }}

        .btn-learned.active {{
            background: #10b981;
            color: #ffffff;
            border-color: #059669;
        }}

        /* Kanji Cards */
        .kanji-cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 18px;
        }}

        .kanji-detail-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 20px;
            display: flex;
            gap: 16px;
            box-shadow: var(--shadow-subtle);
            transition: all 0.2s;
        }}

        .kanji-detail-card:hover {{
            border-color: #a7f3d0;
            box-shadow: var(--shadow-card);
            transform: translateY(-2px);
        }}

        .kanji-big-char {{
            width: 72px;
            height: 72px;
            border-radius: 14px;
            background: linear-gradient(135deg, #059669 0%, #10b981 100%);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--jp-font);
            font-size: 2.5rem;
            font-weight: 900;
            flex-shrink: 0;
            box-shadow: 0 4px 10px rgba(5, 150, 105, 0.3);
        }}

        .kanji-info {{
            flex-grow: 1;
        }}

        .kanji-hv-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 2px;
        }}

        .kanji-strokes-badge {{
            font-size: 0.72rem;
            font-weight: 700;
            background: #f1f5f9;
            padding: 2px 8px;
            border-radius: 4px;
            color: #475569;
        }}

        .kanji-readings {{
            font-size: 0.82rem;
            color: #334155;
            margin: 6px 0;
            line-height: 1.4;
        }}

        .kanji-mnemonic {{
            font-size: 0.78rem;
            color: #047857;
            background: #ecfdf5;
            padding: 4px 8px;
            border-radius: 6px;
            font-weight: 600;
        }}

        /* Quiz */
        .quiz-progress-bar-wrap {{
            background: #e2e8f0;
            height: 8px;
            border-radius: 999px;
            margin-bottom: 24px;
            overflow: hidden;
        }}

        .quiz-progress-fill {{
            background: linear-gradient(90deg, #10b981, #059669);
            height: 100%;
            width: 0%;
            transition: width 0.3s ease;
        }}

        .quiz-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: var(--shadow-subtle);
        }}

        .quiz-q-num {{
            font-size: 0.78rem;
            font-weight: 800;
            color: var(--primary);
            text-transform: uppercase;
            margin-bottom: 6px;
        }}

        .quiz-question-text {{
            font-size: 1.05rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 14px;
        }}

        .quiz-options-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin-bottom: 12px;
        }}

        .quiz-opt-btn {{
            background: #f8fafc;
            border: 1.5px solid #cbd5e1;
            border-radius: 10px;
            padding: 12px 16px;
            font-size: 0.95rem;
            font-weight: 700;
            color: #334155;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .quiz-opt-btn:hover:not(:disabled) {{
            border-color: var(--primary);
            background: var(--primary-soft);
            color: var(--primary-dark);
        }}

        .quiz-opt-btn.correct {{
            background: #dcfce7 !important;
            border-color: #22c55e !important;
            color: #15803d !important;
        }}

        .quiz-opt-btn.wrong {{
            background: #fee2e2 !important;
            border-color: #ef4444 !important;
            color: #b91c1c !important;
        }}

        .quiz-feedback {{
            display: none;
            padding: 12px 16px;
            border-radius: 8px;
            font-size: 0.88rem;
            line-height: 1.5;
            margin-top: 10px;
        }}

        .quiz-feedback.show {{
            display: block;
            animation: fadeIn 0.3s;
        }}

        .quiz-feedback.correct {{
            background: #f0fdf4;
            border: 1px solid #86efac;
            color: #166534;
        }}

        .quiz-feedback.wrong {{
            background: #fef2f2;
            border: 1px solid #fca5a5;
            color: #991b1b;
        }}

        .score-box {{
            display: none;
            text-align: center;
            background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
            color: #ffffff;
            border-radius: var(--radius-lg);
            padding: 36px 20px;
            margin-top: 24px;
        }}

        .score-box.show {{
            display: block;
            animation: zoomIn 0.35s ease;
        }}

        .score-val {{
            font-size: 3.5rem;
            font-weight: 900;
            color: #a7f3d0;
            margin: 10px 0;
        }}

        .btn-retry {{
            background: #ffffff;
            color: #064e3b;
            border: none;
            padding: 12px 28px;
            border-radius: 999px;
            font-weight: 800;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 14px;
            transition: all 0.2s;
        }}

        .btn-retry:hover {{
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}

        @media (max-width: 768px) {{
            .hero-title {{
                font-size: 1.6rem;
            }}
            .hero-jp-quote {{
                font-size: 1.1rem;
            }}
            .content-section {{
                padding: 20px 16px;
            }}
            .dock-pill-track {{
                width: 100%;
                order: 3;
            }}
            .global-sticky-dock {{
                flex-wrap: wrap;
            }}
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        @keyframes zoomIn {{
            from {{ opacity: 0; transform: scale(0.92); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
    </style>
</head>
<body>

    <!-- GLOBAL FLOATING DOCK -->
    <div class="global-sticky-dock-wrapper">
        <div class="global-sticky-dock">
            <a href="index.html" class="dock-brand" title="Trang chủ Luyện tập">
                <span>⛩️</span>
                <span class="dock-brand-text">Marugoto A2</span>
            </a>

            <!-- Lesson Track Pills (1 to 18) -->
            <div class="dock-pill-track" id="dockPillTrack">
{dock_pills_str}
            </div>

            <!-- Action Controls -->
            <div class="dock-actions">
                <button type="button" class="dock-action-btn" onclick="toggleGlobalMegaSheet(event)" title="Mục lục 18 bài học">
                    <span>📑 18 Bài Học</span>
                    <span>▾</span>
                </button>
                <div class="dock-dropdown-wrapper">
                    <button type="button" class="dock-action-btn" onclick="toggleGlobalToolsDropdown(event)" title="Tiện ích học tập">
                        <span>🛠️ Tiện Ích</span>
                        <span>▾</span>
                    </button>
                    <div class="dock-tools-menu" id="globalToolsMenu">
{dock_tools_str}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- MEGA DRAWER SHEET -->
    <div class="global-mega-sheet" id="globalMegaSheet" onclick="closeGlobalMegaSheet()">
        <div class="sheet-content" onclick="event.stopPropagation()">
            <div class="sheet-header">
                <div class="sheet-header-title">📚 Mục Lục Toàn Diện 18 Bài Học (Marugoto A2-1 & A2-2)</div>
                <button type="button" class="sheet-close-btn" onclick="closeGlobalMegaSheet()">✕</button>
            </div>
            <div class="sheet-topics-grid">
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 1: Gia Đình & Bản Thân</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l1" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏠 Bài 1: Nơi ở & Gia đình</div>
                        <div class="sheet-lesson-desc">～に住んでいます / Thể ている / で働いています</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l2" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🎨 Bài 2: Sở thích của tôi</div>
                        <div class="sheet-lesson-desc">V-ること / Thể từ điển (RU) / Năng khiếu</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 2: Mùa & Thời Tiết</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l3" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🍁 Bài 3: Bốn mùa khí hậu</div>
                        <div class="sheet-lesson-desc">V-ると / になる・くなる (Thay đổi trạng thái)</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l4" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">⛅ Bài 4: Dự báo thời tiết</div>
                        <div class="sheet-lesson-desc">～でしょう / ～かもしれません (Phán đoán)</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 3: Thị Trấn Của Tôi</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l5" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏙️ Bài 5: Nơi chốn & Phố xá</div>
                        <div class="sheet-lesson-desc">Địa điểm, phong cảnh và lối sống thị trấn</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l6" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🗺️ Bài 6: Mua sắm & Phương hướng</div>
                        <div class="sheet-lesson-desc">Chỉ đường, hỏi giá cả và mua hàng hóa</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 4: Đi Lại & Ăn Uống</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l7" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">⏰ Bài 7: Ra ngoài & Đi lại</div>
                        <div class="sheet-lesson-desc">Phương tiện giao thông, hẹn giờ và xuất phát</div>
                    </a>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l8" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">⛩️ Bài 8: Bữa ăn & Thời gian</div>
                        <div class="sheet-lesson-desc">Món ăn thường ngày, thói quen ăn uống</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 5: Ngôn Ngữ & Văn Hóa</div>
                    <a href="On_Tap_Mini_Test_A2_5_8.html#grammar-l9" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🗣️ Bài 9: Giao lưu ngôn ngữ</div>
                        <div class="sheet-lesson-desc">Học ngoại ngữ, các phương pháp trau dồi</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_10.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🌟 Bài 10: Ước mơ du lịch Nhật</div>
                        <div class="sheet-lesson-desc">V-たいです / Tần suất ～回 / V-てみます</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 6: Ăn Uống Ngoài Trời</div>
                    <a href="Marugoto_A2_Lesson_11.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🍱 Bài 11: Dã ngoại picnic</div>
                        <div class="sheet-lesson-desc">V-ていきます/きます / なんでもいい / どちらがいい</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_12.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🍜 Bài 12: Món ăn & Vị giác</div>
                        <div class="sheet-lesson-desc">V-たことがあります / どちらが / Hương vị ẩm thực</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 7: Chuyến Đi Công Tác</div>
                    <a href="Marugoto_A2_Lesson_13.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">✈️ Bài 13: Lịch trình công tác</div>
                        <div class="sheet-lesson-desc">V-てください / Sân bay, đưa đón & lịch trình</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_14.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">💻 Bài 14: Nơi làm việc</div>
                        <div class="sheet-lesson-desc">V-てもいいですか (Xin phép) / V-てはいけません (Cấm)</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 8: Cuộc Sống Khỏe Mạnh</div>
                    <a href="Marugoto_A2_Lesson_15.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏥 Bài 15: Cơ thể & Bệnh tật</div>
                        <div class="sheet-lesson-desc">～んです (Giải thích) / Triệu chứng & Khám bệnh</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_16.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🏃 Bài 16: Giữ gìn sức khỏe</div>
                        <div class="sheet-lesson-desc">V-たほうがいい / V-ないほうがいい / V-すぎます</div>
                    </a>
                </div>
                <div class="sheet-topic-card">
                    <div class="sheet-topic-badge">Topic 9: Chúc Mừng & Kỷ Niệm</div>
                    <a href="Marugoto_A2_Lesson_17.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">🎁 Bài 17: Quà tặng & Kỷ niệm</div>
                        <div class="sheet-lesson-desc">あげます / もらいます / Các dịp lễ kỷ niệm</div>
                    </a>
                    <a href="Marugoto_A2_Lesson_18.html" class="sheet-lesson-link">
                        <div class="sheet-lesson-name">👘 Bài 18: Trang phục & Lễ hội</div>
                        <div class="sheet-lesson-desc">V-ています (Mặc trang phục) / ～と思います / Lời chúc</div>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- STICKY SECTION SUB-NAV -->
    <div class="section-nav">
        <a href="#sec-grammar1" class="sec-link">① Ngữ Pháp 1</a>
        <a href="#sec-grammar2" class="sec-link">② Ngữ Pháp 2</a>
        <a href="#sec-grammar3" class="sec-link">③ Ngữ Pháp 3</a>
        <a href="#sec-verb-lab" class="sec-link">🔬 Máy Biến Thể</a>
        <a href="#sec-dialogue" class="sec-link">💬 Đối Thoại Tương Tác</a>
        <a href="#sec-vocab" class="sec-link">🎴 Flashcard 3D ({len(vocab)} từ)</a>
        <a href="#sec-kanji" class="sec-link">⛩️ {len(kanjis)} Chữ Hán</a>
        <a href="#sec-quiz" class="sec-link">📝 Mini Test 15 Câu</a>
    </div>

    <!-- MAIN CONTAINER -->
    <div class="main-container">

        <!-- HERO BANNER -->
        <div class="hero-banner">
            <div class="hero-badge">{topic_badge}</div>
            <h1 class="hero-title">CHINH PHỤC TOÀN DIỆN BÀI {num}</h1>
            <div class="hero-jp-quote">
                <span>「{title_jp}」</span>
                <button type="button" class="btn-speak" style="background:rgba(255,255,255,0.2); border-color:#6ee7b7; color:#fff;" onclick="speakText('{title_jp.replace("'", "\\'")}')">🔊</button>
            </div>
            <p class="hero-subtitle">
                {desc}
            </p>
            <div class="hero-stats-row">
                <div class="stat-card">
                    <div class="stat-number">{len(vocab)}</div>
                    <div class="stat-label">Từ vựng Flashcard</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">3</div>
                    <div class="stat-label">Mẫu câu trọng tâm</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(verb_lab["verbs"])}</div>
                    <div class="stat-label">Động từ biến thể</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(kanjis)}</div>
                    <div class="stat-label">Chữ Hán cốt lõi</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">15</div>
                    <div class="stat-label">Câu Mini Test</div>
                </div>
            </div>
        </div>

        <!-- GRAMMAR SECTIONS -->
{all_grammars_str}

        <!-- INTERACTIVE LABORATORY -->
        <section class="content-section" id="sec-verb-lab">
            <div class="section-header">
                <h2 class="section-title"><span>🔬</span> {verb_lab["title"]}</h2>
                <span class="section-tag">Interactive Laboratory</span>
            </div>

            <p style="margin-bottom: 16px; color: #334155;">
                {verb_lab["desc"]}
            </p>

            <div class="verb-picker-row" id="verbPickerRow">
                <!-- Verb pills populated via JS -->
            </div>

{verb_lab_boxes}

            <div class="morph-ex-box">
                <div>
                    <div style="font-size:0.75rem; font-weight:800; color:#047857; text-transform:uppercase;">Câu ví dụ thực tế trong Bài {num}:</div>
                    <div style="font-family:var(--jp-font); font-size:1.05rem; font-weight:800; color:#0f172a; margin-top:2px;" id="morphExText">
                        ---
                    </div>
                </div>
                <button type="button" class="btn-speak" id="btnMorphSpeak" onclick="speakCurrentMorph()">🔊</button>
            </div>
        </section>

        <!-- INTERACTIVE DIALOGUE SIMULATOR -->
        <section class="content-section" id="sec-dialogue">
            <div class="section-header">
                <h2 class="section-title"><span>💬</span> {dialogue["title"]}</h2>
                <span class="section-tag">Role-play Simulator</span>
            </div>

            <p style="margin-bottom: 16px; color: #334155;">
                {dialogue["desc"]}
            </p>

            <div class="dialogue-wrap">
                <div class="chat-container" id="chatContainer">
                    <div class="chat-bubble bot">
                        <div class="chat-avatar">{dialogue["initial"]["avatar"]}</div>
                        <div class="chat-msg">
                            <div class="chat-name">{dialogue["initial"]["name"]}</div>
                            <div class="chat-jp">{dialogue["initial"]["jp"]}</div>
                            <div class="chat-vi">{dialogue["initial"]["vi"]}</div>
                        </div>
                    </div>
                </div>

                <div class="chat-options-panel">
                    <div class="chat-opt-title">🎯 Chọn lời thoại phản hồi của bạn:</div>
                    <div class="chat-btn-grid" id="chatOptionsGrid">
                        <!-- Populated dynamically via JS -->
                    </div>
                </div>
            </div>
        </section>

        <!-- FLASHCARDS 3D -->
        <section class="content-section" id="sec-vocab">
            <div class="section-header">
                <h2 class="section-title"><span>🎴</span> TRỌN BỘ {len(vocab)} TỪ VỰNG BÀI {num} (FLASHCARD 3D)</h2>
                <span class="section-tag">Flashcards 3D</span>
            </div>

            <p style="margin-bottom: 16px; color: #334155;">
                Bấm trực tiếp vào từng thẻ để lật xem nghĩa tiếng Việt và câu ví dụ. Bấm biểu tượng 🔊 để nghe phát âm chuẩn Tokyo:
            </p>

            <div class="vocab-filter-bar" id="vocabFilterBar">
                <!-- Filters rendered via JS -->
                <div class="vocab-stats-badge" id="vocabStats">Đã thuộc: 0 / {len(vocab)} từ</div>
            </div>

            <div class="flashcards-grid" id="flashcardsGrid">
                <!-- Cards rendered via JS -->
            </div>
        </section>

        <!-- KANJI SECTION -->
        <section class="content-section" id="sec-kanji">
            <div class="section-header">
                <h2 class="section-title"><span>⛩️</span> {len(kanjis)} CHỮ HÁN CỐT LÕI BÀI {num}</h2>
                <span class="section-tag">Kanji Mastery</span>
            </div>

            <p style="margin-bottom: 20px; color: #334155;">
                Các chữ Hán này đã được cập nhật hoàn chỉnh trong ứng dụng <a href="kanji_a2.html" style="color:var(--primary); font-weight:700; text-decoration:underline;">Học Kanji & Nét Viết</a>:
            </p>

            <div class="kanji-cards-grid">
{kanji_str}
            </div>

            <div style="text-align: center; margin-top: 24px;">
                <a href="kanji_a2.html" class="dock-action-btn" style="padding: 10px 24px; font-size: 0.95rem; background: var(--primary); color: #fff; border: none; display: inline-flex;">
                    ⛩️ Mở Ứng Dụng Luyện Viết Từng Nét Chữ Hán Bài Này ➔
                </a>
            </div>
        </section>

        <!-- MINI TEST SECTION -->
        <section class="content-section" id="sec-quiz">
            <div class="section-header">
                <h2 class="section-title"><span>📝</span> MINI TEST PHẢN XẠ BÀI {num} (15 CÂU)</h2>
                <span class="section-tag">Interactive Exam</span>
            </div>

            <p style="margin-bottom: 16px; color: #334155;">
                Bài test gồm 15 câu bao quát toàn bộ ngữ pháp, từ vựng và chữ Hán Bài {num}. Bấm vào đáp án để xem giải thích chi tiết ngay lập tức!
            </p>

            <div class="quiz-progress-bar-wrap">
                <div class="quiz-progress-fill" id="quizProgressBar"></div>
            </div>

            <div id="quizContainer">
                <!-- Questions rendered via JS -->
            </div>

            <div class="score-box" id="scoreBox">
                <h3>🎉 KẾT QUẢ BÀI TEST BÀI {num}</h3>
                <div class="score-val" id="scoreVal">15 / 15</div>
                <p id="scoreMsg" style="font-size: 1.1rem; color: #a7f3d0; margin-bottom: 16px;">
                    Xuất sắc! Bạn đã nắm vững toàn bộ kiến thức Bài {num}!
                </p>
                <button type="button" class="btn-retry" onclick="resetQuiz()">🔄 Làm Lại Bài Test</button>
            </div>
        </section>

    </div>

    <!-- SCRIPTS -->
    <script>
        const VOCAB_DATA = {vocab_json};
        const VERB_MORPH_DATA = {verb_lab_json};
        const QUIZ_QUESTIONS = {quizzes_json};
        const DIALOGUE_STEPS = {dialogue_json};

        // Tokyo Audio Speech Synthesis (Dual Engine via audio-engine.js)
        function speakText(text) {{
            if (window.speakJapanese) {{
                window.speakJapanese(text);
            }}
        }}

        // Verb Morphing Laboratory
        let currentVerbIdx = 0;

        function renderVerbPicker() {{
            const container = document.getElementById('verbPickerRow');
            if (!container || !VERB_MORPH_DATA.length) return;
            container.innerHTML = VERB_MORPH_DATA.map((v, i) => `
                <button type="button" class="verb-pill ${{i === 0 ? 'active' : ''}}" onclick="selectVerb(${{i}}, this)">
                    <span class="pill-kanji">${{v.kanji}}</span>
                    <span class="pill-meaning">(${{v.vi}})</span>
                </button>
            `).join('');
            updateMorphDisplay(0);
        }}

        function selectVerb(idx, btn) {{
            document.querySelectorAll('.verb-pill').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentVerbIdx = idx;
            updateMorphDisplay(idx);
        }}

        function updateMorphDisplay(idx) {{
            const v = VERB_MORPH_DATA[idx];
            if (!v) return;
            const morphMasuEl = document.getElementById('morphMasu');
            if (morphMasuEl) {{
                morphMasuEl.innerHTML = `
                    <div style="font-size:1.35rem; font-weight:800; color:#0f172a; line-height:1.2;">${{v.kanji}}</div>
                    <div style="font-size:0.86rem; font-weight:700; color:#059669; margin-top:4px; font-family:var(--jp-font);">${{v.masu}}</div>
                `;
            }}
            document.getElementById('morphVi').textContent = v.vi;
            document.getElementById('morphTe').textContent = v.col2;
            document.getElementById('morphTeIki').textContent = v.col3;
            document.getElementById('morphTeKi').textContent = v.col4;
            document.getElementById('morphMashou').textContent = v.col5;
            document.getElementById('morphExText').textContent = v.ex;
        }}

        function speakCurrentMorph() {{
            const v = VERB_MORPH_DATA[currentVerbIdx];
            if (v) speakText(v.ex);
        }}

        // Flashcards Logic
        let activeVocabFilter = 'all';
        let learnedCards = new Set();

        function initVocabFilters() {{
            const bar = document.getElementById('vocabFilterBar');
            const cats = Array.from(new Set(VOCAB_DATA.map(v => v.cat)));
            const catNames = {{}};
            VOCAB_DATA.forEach(v => catNames[v.cat] = v.catName);

            let filterBtns = `<button class="vocab-filter-btn active" onclick="filterVocab('all', this)">🌟 Tất cả (${{VOCAB_DATA.length}})</button>`;
            cats.forEach(c => {{
                filterBtns += `<button class="vocab-filter-btn" onclick="filterVocab('${{c}}', this)">${{catNames[c] || c}}</button>`;
            }});
            filterBtns += `<div class="vocab-stats-badge" id="vocabStats">Đã thuộc: 0 / ${{VOCAB_DATA.length}} từ</div>`;
            bar.innerHTML = filterBtns;
        }}

        function renderFlashcards() {{
            const container = document.getElementById('flashcardsGrid');
            const filtered = activeVocabFilter === 'all' 
                ? VOCAB_DATA 
                : VOCAB_DATA.filter(v => v.cat === activeVocabFilter);

            container.innerHTML = filtered.map(v => `
                <div class="flashcard" onclick="flipCard(this, event)">
                    <div class="fc-inner">
                        <div class="fc-front">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span class="fc-badge">${{v.badge || v.catName}}</span>
                                <button type="button" class="btn-speak" style="width:28px; height:28px; font-size:0.75rem;" onclick="event.stopPropagation(); speakText('${{v.jp}}')">🔊</button>
                            </div>
                            <div class="fc-illustration">
                                ${{v.svg || ''}}
                            </div>
                            <div>
                                <div class="fc-jp jp-text">${{v.kanji || v.jp}}</div>
                                <div class="fc-kana jp-text">${{v.kana}}</div>
                                <div class="fc-romaji">${{v.romaji}}</div>
                            </div>
                            <div class="fc-hint">💡 Bấm thẻ để lật xem nghĩa & ví dụ</div>
                        </div>

                        <div class="fc-back">
                            <div>
                                <div class="fc-back-meaning">${{v.vi}}</div>
                                <div style="font-size:0.75rem; font-weight:800; color:#047857; text-transform:uppercase; margin-bottom:4px;">Ví dụ thực tế:</div>
                                <div class="fc-back-ex-jp jp-text">${{v.exJp}}</div>
                                <div class="fc-back-ex-vi">${{v.exVi}}</div>
                            </div>
                            <div class="fc-back-actions">
                                <button type="button" class="btn-speak" style="width:32px; height:32px; font-size:0.8rem;" onclick="event.stopPropagation(); speakText('${{v.exJp}}')">🔊</button>
                                <button type="button" class="btn-learned ${{learnedCards.has(v.id) ? 'active' : ''}}" onclick="event.stopPropagation(); toggleLearned(${{v.id}}, this)">
                                    ${{learnedCards.has(v.id) ? '✓ Đã thuộc' : '+ Đánh dấu thuộc'}}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            `).join('');
            updateLearnedStats();
        }}

        function flipCard(card, event) {{
            if (event.target.closest('button')) return;
            card.classList.toggle('flipped');
        }}

        function filterVocab(cat, btn) {{
            activeVocabFilter = cat;
            document.querySelectorAll('.vocab-filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderFlashcards();
        }}

        function toggleLearned(id, btn) {{
            if (learnedCards.has(id)) {{
                learnedCards.delete(id);
                btn.classList.remove('active');
                btn.textContent = '+ Đánh dấu thuộc';
            }} else {{
                learnedCards.add(id);
                btn.classList.add('active');
                btn.textContent = '✓ Đã thuộc';
            }}
            updateLearnedStats();
        }}

        function updateLearnedStats() {{
            const badge = document.getElementById('vocabStats');
            if (badge) badge.textContent = `Đã thuộc: ${{learnedCards.size}} / ${{VOCAB_DATA.length}} từ`;
        }}

        // Dialogue Simulator
        let currentStepIdx = 0;

        function initDialogue() {{
            currentStepIdx = 0;
            renderDialogueOptions(0);
        }}

        function renderDialogueOptions(stepIdx) {{
            const container = document.getElementById('chatOptionsGrid');
            const step = DIALOGUE_STEPS[stepIdx];
            if (!step) {{
                container.innerHTML = `
                    <div style="grid-column: 1/-1; text-align:center; padding:12px; color:#059669; font-weight:700;">
                        🎉 Hoàn thành xuất sắc đoạn hội thoại tình huống Bài {num}!
                    </div>
                `;
                return;
            }}

            container.innerHTML = step.options.map((opt, i) => `
                <button type="button" class="btn-chat-choice" onclick="chooseDialogue(${{stepIdx}}, ${{i}})">
                    <div style="font-family:var(--jp-font);">${{opt.text}}</div>
                    <div style="font-size:0.75rem; color:#64748b; margin-top:2px;">${{opt.vi}}</div>
                </button>
            `).join('');
        }}

        function chooseDialogue(stepIdx, optIdx) {{
            const step = DIALOGUE_STEPS[stepIdx];
            const opt = step.options[optIdx];
            const chat = document.getElementById('chatContainer');

            const userBubble = document.createElement('div');
            userBubble.className = 'chat-bubble user';
            userBubble.innerHTML = `
                <div class="chat-avatar">🧑</div>
                <div class="chat-msg">
                    <div class="chat-name">Bạn (Tôi)</div>
                    <div class="chat-jp">${{opt.text}}</div>
                    <div class="chat-vi">${{opt.vi}}</div>
                </div>
            `;
            chat.appendChild(userBubble);
            speakText(opt.text);

            setTimeout(() => {{
                const npcBubble = document.createElement('div');
                npcBubble.className = 'chat-bubble bot';
                npcBubble.innerHTML = `
                    <div class="chat-avatar">${{opt.replyAvatar || '👩'}}</div>
                    <div class="chat-msg">
                        <div class="chat-name">${{opt.replyNpc}}</div>
                        <div class="chat-jp">${{opt.replyText}}</div>
                        <div class="chat-vi">${{opt.replyVi}}</div>
                    </div>
                `;
                chat.appendChild(npcBubble);
                speakText(opt.replyText);

                if (stepIdx + 1 < DIALOGUE_STEPS.length) {{
                    setTimeout(() => {{
                        const nextPrompt = DIALOGUE_STEPS[stepIdx + 1];
                        const promptBubble = document.createElement('div');
                        promptBubble.className = 'chat-bubble bot';
                        promptBubble.innerHTML = `
                            <div class="chat-avatar">${{nextPrompt.avatar || '👨'}}</div>
                            <div class="chat-msg">
                                <div class="chat-name">${{nextPrompt.npcName}}</div>
                                <div class="chat-jp">${{nextPrompt.npcText}}</div>
                                <div class="chat-vi">${{nextPrompt.npcVi}}</div>
                            </div>
                        `;
                        chat.appendChild(promptBubble);
                        speakText(nextPrompt.npcText);
                        renderDialogueOptions(stepIdx + 1);
                    }}, 1000);
                }} else {{
                    renderDialogueOptions(stepIdx + 1);
                }}
            }}, 600);
        }}

        // Quiz Logic
        let quizAnswers = {{}};

        function renderQuiz() {{
            const container = document.getElementById('quizContainer');
            container.innerHTML = QUIZ_QUESTIONS.map(q => `
                <div class="quiz-card" id="quizCard_${{q.id}}">
                    <div class="quiz-q-num">Câu ${{q.id}} / 15 • ${{q.category}}</div>
                    <div class="quiz-question-text jp-text">${{q.q}}</div>
                    <div class="quiz-options-grid">
                        ${{q.options.map((opt, optIdx) => `
                            <button type="button" class="quiz-opt-btn jp-text" onclick="answerQuiz(${{q.id}}, ${{optIdx}}, this)">
                                ${{opt}}
                            </button>
                        `).join('')}}
                    </div>
                    <div class="quiz-feedback" id="quizFeedback_${{q.id}}">
                        ${{q.explain}}
                    </div>
                </div>
            `).join('');
            updateQuizProgress();
        }}

        function answerQuiz(qId, selectedIdx, btn) {{
            if (quizAnswers[qId] !== undefined) return;
            quizAnswers[qId] = selectedIdx;

            const q = QUIZ_QUESTIONS.find(item => item.id === qId);
            const card = document.getElementById(`quizCard_${{qId}}`);
            const buttons = card.querySelectorAll('.quiz-opt-btn');
            const feedback = document.getElementById(`quizFeedback_${{qId}}`);

            buttons.forEach((b, idx) => {{
                b.disabled = true;
                if (idx === q.correct) {{
                    b.classList.add('correct');
                }} else if (idx === selectedIdx) {{
                    b.classList.add('wrong');
                }}
            }});

            feedback.classList.add('show');
            if (selectedIdx === q.correct) {{
                feedback.classList.add('correct');
                feedback.innerHTML = `✓ <strong>Chính xác!</strong> ${{q.explain}}`;
            }} else {{
                feedback.classList.add('wrong');
                feedback.innerHTML = `✕ <strong>Chưa chính xác!</strong> ${{q.explain}}`;
            }}

            updateQuizProgress();
            checkQuizFinish();
        }}

        function updateQuizProgress() {{
            const answeredCount = Object.keys(quizAnswers).length;
            const pct = (answeredCount / QUIZ_QUESTIONS.length) * 100;
            document.getElementById('quizProgressBar').style.width = `${{pct}}%`;
        }}

        function checkQuizFinish() {{
            if (Object.keys(quizAnswers).length === QUIZ_QUESTIONS.length) {{
                let score = 0;
                QUIZ_QUESTIONS.forEach(q => {{
                    if (quizAnswers[q.id] === q.correct) score++;
                }});

                const scoreBox = document.getElementById('scoreBox');
                const scoreVal = document.getElementById('scoreVal');
                const scoreMsg = document.getElementById('scoreMsg');

                scoreVal.textContent = `${{score}} / 15`;
                if (score >= 13) {{
                    scoreMsg.textContent = "🌟 Tuyệt vời! Bạn đã thành thạo toàn bộ kiến thức Bài {num}!";
                }} else if (score >= 9) {{
                    scoreMsg.textContent = "👍 Khá tốt! Hãy ôn lại các câu chưa chính xác nhé.";
                }} else {{
                    scoreMsg.textContent = "💪 Cố lên! Hãy xem lại phần giải thích và thử làm lại nhé.";
                }}
                scoreBox.classList.add('show');
                scoreBox.scrollIntoView({{ behavior: 'smooth' }});
            }}
        }}

        function resetQuiz() {{
            quizAnswers = {{}};
            document.getElementById('scoreBox').classList.remove('show');
            renderQuiz();
            document.getElementById('sec-quiz').scrollIntoView({{ behavior: 'smooth' }});
        }}

        // Global Nav
        function toggleGlobalMegaSheet(e) {{
            if (e) e.stopPropagation();
            document.getElementById('globalMegaSheet').classList.toggle('show');
        }}

        function closeGlobalMegaSheet() {{
            document.getElementById('globalMegaSheet').classList.remove('show');
        }}

        function toggleGlobalToolsDropdown(e) {{
            if (e) e.stopPropagation();
            document.getElementById('globalToolsMenu').classList.toggle('show');
        }}

        document.addEventListener('click', (e) => {{
            const menu = document.getElementById('globalToolsMenu');
            if (menu && !menu.contains(e.target)) {{
                menu.classList.remove('show');
            }}
        }});

        // Init
        window.addEventListener('DOMContentLoaded', () => {{
            renderVerbPicker();
            initVocabFilters();
            renderFlashcards();
            initDialogue();
            renderQuiz();
        }});
    </script>
</body>
</html>
"""
    return html

def main():
    for cfg in LESSON_CONFIGS:
        num = cfg["num"]
        filename = f"Marugoto_A2_Lesson_{num}.html"
        html = build_lesson_html(cfg)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {filename} successfully ({len(html)} bytes)!")

if __name__ == "__main__":
    main()
