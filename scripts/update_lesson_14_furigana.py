# -*- coding: utf-8 -*-
"""
scripts/update_lesson_14_furigana.py
Comprehensive script to inject Ruby/Furigana (Hiragana over Kanji) throughout Marugoto A2 Lesson 14.
"""

import json
import re

def update_lesson_14():
    # 1. Update scripts/data_lesson_14.py
    with open("scripts/data_lesson_14.py", "r", encoding="utf-8") as f:
        data_py = f.read()

    # Title & Topic
    data_py = data_py.replace('"title_jp": "これ、使ってもいいですか"', '"title_jp": "これ、<ruby>使<rt>つか</rt></ruby>ってもいいですか"')

    # Grammar 1
    data_py = data_py.replace(
        '"formula": "Động từ thể Te (V-て) + もいいですか<br>Trả lời đồng ý: 「はい、どうぞ (使ってください)」<br>Từ chối khéo: 「すみません、今 使っています / 壊れています」"',
        '"formula": "Động từ thể Te (V-て) + もいいですか<br>Trả lời đồng ý: 「はい、どうぞ (<ruby>使<rt>つか</rt></ruby>ってください)」<br>Từ chối khéo: 「すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っています / <ruby>壊<rt>こわ</rt></ruby>れています」"'
    )
    data_py = data_py.replace('["使います (Dùng)", "使っても いいですか", "Tôi dùng cái này có được không?"]',
                              '["<ruby>使<rt>つか</rt></ruby>います (Dùng)", "<ruby>使<rt>つか</rt></ruby>っても いいですか", "Tôi dùng cái này có được không?"]')
    data_py = data_py.replace('["借ります (Mượn)", "借りても いいですか", "Tôi mượn máy tính/bút có được không?"]',
                              '["<ruby>借<rt>か</rt></ruby>ります (Mượn)", "<ruby>借<rt>か</rt></ruby>りても いいですか", "Tôi mượn máy tính/bút có được không?"]')
    data_py = data_py.replace('["開けます (Mở cửa)", "開けても いいですか", "Tôi mở cửa sổ ra có được không?"]',
                              '["<ruby>開<rt>あ</rt></ruby>けます (Mở cửa)", "<ruby>開<rt>あ</rt></ruby>けても いいですか", "Tôi mở cửa sổ ra có được không?"]')
    data_py = data_py.replace('["座ります (Ngồi)", "座っても いいですか", "Tôi ngồi ở đây có được không?"]',
                              '["<ruby>座<rt>すわ</rt></ruby>ります (Ngồi)", "<ruby>座<rt>すわ</rt></ruby>っても いいですか", "Tôi ngồi ở đây có được không?"]')

    data_py = data_py.replace('"jp": "この コンピューター、使っても いいですか。―― はい、どうぞ。"',
                              '"jp": "この コンピューター、<ruby>使<rt>つか</rt></ruby>っても いいですか。―― はい、どうぞ。"')
    data_py = data_py.replace('"jp": "ボールペンを 借りても いいですか。―― すみません、今 使っているんです。"',
                              '"jp": "ボールペンを <ruby>借<rt>か</rt></ruby>りても いいですか。―― すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っているんです。"')

    # Grammar 2
    data_py = data_py.replace('"jp": "ここで 写真を 撮っては いけません。"',
                              '"jp": "ここで <ruby>写真<rt>しゃしん</rt></ruby>を <ruby>撮<rt>と</rt></ruby>っては いけません。"')
    data_py = data_py.replace('"jp": "この パソコンの パスワードを 教えては いけません。"',
                              '"jp": "この パソコンの パスワードを <ruby>教<rt>おし</rt></ruby>えては いけません。"')
    data_py = data_py.replace('"jp": "大事な 書類を 外へ 持って 行っては いけません。"',
                              '"jp": "<ruby>大事<rt>だいじ</rt></ruby>な <ruby>書類<rt>しょるい</rt></ruby>を <ruby>外<rt>そと</rt></ruby>へ <ruby>持<rt>も</rt></ruby>って <ruby>行<rt>い</rt></ruby>っては いけません。"')

    # Grammar 3
    data_py = data_py.replace('"title": "Chào tạm biệt & Gửi lời hỏi thăm: お世話になりました"',
                              '"title": "Chào tạm biệt & Gửi lời hỏi thăm: お<ruby>世話<rt>せわ</rt></ruby>になりました"')
    data_py = data_py.replace(
        '"formula": "大変 お世話になりました。<br>[Ai đó] に よろしく お伝えください。<br>どうぞ お気をつけて お帰りください。"',
        '"formula": "<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました。<br>[Ai đó] に よろしく お<ruby>伝<rt>つた</rt></ruby>えください。<br>どうぞ お<ruby>気<rt>き</rt></ruby>をつけて お<ruby>帰<rt>かえ</rt></ruby>りください。"'
    )
    data_py = data_py.replace('"jp": "3日間、大変 お世話になりました。"',
                              '"jp": "3<ruby>日間<rt>にちかん</rt></ruby>、<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました。"')
    data_py = data_py.replace('"jp": "本社の 皆さんに よろしく お伝えください。"',
                              '"jp": "<ruby>本社<rt>ほんしゃ</rt></ruby>の <ruby>皆<rt>みな</rt></ruby>さんに よろしく お<ruby>伝<rt>つた</rt></ruby>えください。"')
    data_py = data_py.replace('"jp": "また 会議で お会いしましょう。"',
                              '"jp": "また <ruby>会議<rt>かいぎ</rt></ruby>で お<ruby>会<rt>あ</rt></ruby>いしましょう。"')

    with open("scripts/data_lesson_14.py", "w", encoding="utf-8") as f:
        f.write(data_py)
    print("scripts/data_lesson_14.py text formulas & examples updated.")

    # 2. Update lessons/Marugoto_A2_Lesson_14.html
    with open("lessons/Marugoto_A2_Lesson_14.html", "r", encoding="utf-8") as f:
        html = f.read()

    # CSS Injection
    furigana_css = """
        /* Ruby & Furigana Styling */
        ruby {
            ruby-position: over;
            ruby-align: center;
        }

        rt {
            font-size: 0.64em;
            font-weight: 700;
            color: #4f46e5;
            line-height: 1;
            user-select: none;
            letter-spacing: 0.01em;
        }

        .rule-formula rt {
            color: inherit;
            opacity: 0.88;
        }

        .chat-bubble.bot rt {
            color: #4f46e5;
        }

        .chat-bubble.user rt {
            color: #047857;
        }

        .btn-chat-choice rt {
            color: #4338ca;
        }

        .verb-pill rt {
            color: inherit;
            opacity: 0.85;
            font-size: 0.58em;
        }

        .verb-pill.active rt {
            color: #ffffff;
            opacity: 0.95;
        }

        .morph-val rt {
            color: inherit;
            opacity: 0.88;
            font-size: 0.58em;
        }

        body.hide-furigana rt {
            display: none !important;
        }

        /* Furigana Toggle Button */
        .furigana-toggle-btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
            border: 1.5px solid #6366f1;
            background: #eef2ff;
            color: #4338ca;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
            white-space: nowrap;
        }

        .furigana-toggle-btn:hover {
            background: #e0e7ff;
            transform: translateY(-1px);
        }

        .furigana-toggle-btn.off {
            border-color: #cbd5e1;
            background: #f8fafc;
            color: #64748b;
        }
"""
    if "/* Ruby & Furigana Styling */" not in html:
        html = html.replace(".jp-text {", furigana_css + "\n        .jp-text {", 1)

    # Line-height adjustments for furigana
    html = re.sub(
        r"\.ex-jp\s*\{[^}]*\}",
        """.ex-jp {
            font-family: var(--jp-font);
            font-size: 1.08rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.85;
            margin-bottom: 4px;
        }""",
        html
    )

    html = re.sub(
        r"\.rule-formula\s*\{[^}]*\}",
        """.rule-formula {
            font-family: var(--jp-font);
            font-size: 1.22rem;
            font-weight: 800;
            color: var(--primary-dark);
            line-height: 1.85;
            margin-bottom: 8px;
        }""",
        html
    )

    # Sub-nav toggle button
    nav_btn = """        <a href="#sec-quiz" class="sec-link">📝 Mini Test 15 Câu</a>
        <button type="button" class="furigana-toggle-btn" id="btnFuriganaToggle" onclick="toggleFurigana()" title="Bật / Tắt hiển thị Furigana (cách đọc Hiragana)">
            <span>🔤</span> <span id="furiganaBtnLabel">Furigana: BẬT</span>
        </button>
    </div>"""
    if "btnFuriganaToggle" not in html:
        html = re.sub(r'<a href="#sec-quiz" class="sec-link">📝 Mini Test 15 Câu</a>\s*</div>', nav_btn, html)

    # Hero & Header
    html = html.replace("TOPIC 7: 職場のマナー (Quy Tắc Nơi Làm Việc)", "TOPIC 7: <ruby>職場<rt>しょくば</rt></ruby>のマナー (Quy Tắc Nơi Làm Việc)")
    html = html.replace("<span>「これ、使っても いいですか」</span>", "<span>「これ、<ruby>使<rt>つか</rt></ruby>っても いいですか」</span>")
    html = html.replace("💻 Bài 14: 職場のマナー</a>", "💻 Bài 14: <ruby>職場<rt>しょくば</rt></ruby>のマナー</a>")

    # Grammar 1
    html = html.replace(
        "Động từ thể Te (V-て) + もいいですか<br>Trả lời đồng ý: 「はい、どうぞ (使ってください)」<br>Từ chối khéo: 「すみません、今 使っています / 壊れています」",
        "Động từ thể Te (V-て) + もいいですか<br>Trả lời đồng ý: 「はい、どうぞ (<ruby>使<rt>つか</rt></ruby>ってください)」<br>Từ chối khéo: 「すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っています / <ruby>壊<rt>こわ</rt></ruby>れています」"
    )
    html = html.replace(
        '<strong style="color:var(--primary-dark); font-size:1.02rem;">使います (Dùng)</strong>',
        '<strong style="color:var(--primary-dark); font-size:1.02rem;"><ruby>使<rt>つか</rt></ruby>います (Dùng)</strong>'
    )
    html = html.replace("<td>使っても いいですか</td>", "<td><ruby>使<rt>つか</rt></ruby>っても いいですか</td>")

    html = html.replace(
        '<strong style="color:var(--primary-dark); font-size:1.02rem;">借ります (Mượn)</strong>',
        '<strong style="color:var(--primary-dark); font-size:1.02rem;"><ruby>借<rt>か</rt></ruby>ります (Mượn)</strong>'
    )
    html = html.replace("<td>借りても いいですか</td>", "<td><ruby>借<rt>か</rt></ruby>りても いいですか</td>")

    html = html.replace(
        '<strong style="color:var(--primary-dark); font-size:1.02rem;">開けます (Mở cửa)</strong>',
        '<strong style="color:var(--primary-dark); font-size:1.02rem;"><ruby>開<rt>あ</rt></ruby>けます (Mở cửa)</strong>'
    )
    html = html.replace("<td>開けても いいですか</td>", "<td><ruby>開<rt>あ</rt></ruby>けても いいですか</td>")

    html = html.replace(
        '<strong style="color:var(--primary-dark); font-size:1.02rem;">座ります (Ngồi)</strong>',
        '<strong style="color:var(--primary-dark); font-size:1.02rem;"><ruby>座<rt>すわ</rt></ruby>ります (Ngồi)</strong>'
    )
    html = html.replace("<td>座っても いいですか</td>", "<td><ruby>座<rt>すわ</rt></ruby>っても いいですか</td>")

    html = html.replace(
        '<div class="ex-jp">この コンピューター、使っても いいですか。―― はい、どうぞ。</div>',
        '<div class="ex-jp">この コンピューター、<ruby>使<rt>つか</rt></ruby>っても いいですか。―― はい、どうぞ。</div>'
    )
    html = html.replace(
        '<div class="ex-jp">ボールペンを 借りても いいですか。―― すみません、今 使っているんです。</div>',
        '<div class="ex-jp">ボールペンを <ruby>借<rt>か</rt></ruby>りても いいですか。―― すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っているんです。</div>'
    )

    # Grammar 2
    html = html.replace(
        '<div class="ex-jp">ここで 写真を 撮っては いけません。</div>',
        '<div class="ex-jp">ここで <ruby>写真<rt>しゃしん</rt></ruby>を <ruby>撮<rt>と</rt></ruby>っては いけません。</div>'
    )
    html = html.replace(
        '<div class="ex-jp">この パソコンの パスワードを 教えては いけません。</div>',
        '<div class="ex-jp">この パソコンの パスワードを <ruby>教<rt>おし</rt></ruby>えては いけません。</div>'
    )
    html = html.replace(
        '<div class="ex-jp">大事な 書類を 外へ 持って 行っては いけません。</div>',
        '<div class="ex-jp"><ruby>大事<rt>だいじ</rt></ruby>な <ruby>書類<rt>しょるい</rt></ruby>を <ruby>外<rt>そと</rt></ruby>へ <ruby>持<rt>も</rt></ruby>って <ruby>行<rt>い</rt></ruby>っては いけません。</div>'
    )

    # Grammar 3 (USER SCREENSHOT FOCUS)
    html = html.replace(
        '3. Chào tạm biệt & Gửi lời hỏi thăm: お世話になりました</h2>',
        '3. Chào tạm biệt & Gửi lời hỏi thăm: お<ruby>世話<rt>せわ</rt></ruby>になりました</h2>'
    )
    html = html.replace(
        '<div class="rule-formula" style="color: #047857;">大変 お世話になりました。<br>[Ai đó] に よろしく お伝えください。<br>どうぞ お気をつけて お帰りください。</div>',
        '<div class="rule-formula" style="color: #047857;"><ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました。<br>[Ai đó] に よろしく お<ruby>伝<rt>つた</rt></ruby>えください。<br>どうぞ お<ruby>気<rt>き</rt></ruby>をつけて お<ruby>帰<rt>かえ</rt></ruby>りください。</div>'
    )
    html = html.replace(
        '<div class="ex-jp">3日間、大変 お世話になりました。</div>',
        '<div class="ex-jp">3<ruby>日間<rt>にちかん</rt></ruby>、<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました。</div>'
    )
    html = html.replace(
        '<div class="ex-jp">本社の 皆さんに よろしく お伝えください。</div>',
        '<div class="ex-jp"><ruby>本社<rt>ほんしゃ</rt></ruby>の <ruby>皆<rt>みな</rt></ruby>さんに よろしく お<ruby>伝<rt>つた</rt></ruby>えください。</div>'
    )
    html = html.replace(
        '<div class="ex-jp">また 会議で お会いしましょう。</div>',
        '<div class="ex-jp">また <ruby>会議<rt>かいぎ</rt></ruby>で お<ruby>会<rt>あ</rt></ruby>いしましょう。</div>'
    )

    # Initial Dialogue
    html = html.replace(
        '<div class="chat-jp">お疲れ様です！何かお手伝いしましょうか。</div>',
        '<div class="chat-jp">お<ruby>疲<rt>つか</rt></ruby>れ<ruby>様<rt>さま</rt></ruby>です！<ruby>何<rt>なに</rt></ruby>かお<ruby>手伝<rt>てつだ</rt></ruby>いしましょうか。</div>'
    )

    # Kanji section examples
    html = html.replace("<strong>Từ ví dụ:</strong> 自分 (じぶん - bản thân), 自動車 (じどうしゃ - ô tô)",
                        "<strong>Từ ví dụ:</strong> 自分 (<ruby>自<rt>じ</rt></ruby><ruby>分<rt>ぶん</rt></ruby> - bản thân), 自動車 (<ruby>自<rt>じ</rt></ruby><ruby>動<rt>どう</rt></ruby><ruby>車<rt>しゃ</rt></ruby> - ô tô)")

    html = html.replace("<strong>Từ ví dụ:</strong> 自分 (じぶん - bản thân), 5分 (ごふん - 5 phút)",
                        "<strong>Từ ví dụ:</strong> 自分 (<ruby>自<rt>じ</rt></ruby><ruby>分<rt>ぶん</rt></ruby> - bản thân), 5分 (5<ruby>分<rt>ふん</rt></ruby> - 5 phút)")

    html = html.replace("<strong>Từ ví dụ:</strong> 電話 (でんわ - điện thoại), 電気 (でんき - đèn điện)",
                        "<strong>Từ ví dụ:</strong> 電話 (<ruby>電<rt>でん</rt></ruby><ruby>話<rt>わ</rt></ruby> - điện thoại), 電気 (<ruby>電<rt>でん</rt></ruby><ruby>気<rt>き</rt></ruby> - đèn điện)")

    html = html.replace("<strong>Từ ví dụ:</strong> 電話 (でんわ - điện thoại), 会話 (かいわ - hội thoại)",
                        "<strong>Từ ví dụ:</strong> 電話 (<ruby>電<rt>деn</rt></ruby><ruby>話<rt>わ</rt></ruby> - điện thoại), 会話 (<ruby>会<rt>かい</rt></ruby><ruby>話<rt>わ</rt></ruby> - hội thoại)".replace("деn", "でん"))

    html = html.replace("<strong>Từ ví dụ:</strong> 車 (くるま - xe hơi), 電車 (でんしゃ - tàu điện)",
                        "<strong>Từ ví dụ:</strong> 車 (<ruby>車<rt>くるま</rt></ruby> - xe hơi), 電車 (<ruby>電<rt>でん</rt></ruby><ruby>車<rt>しゃ</rt></ruby> - tàu điện)")

    html = html.replace("<strong>Từ ví dụ:</strong> 送ります (おくります - gửi đi / tiễn đưa), 郵送 (ゆうそう - gửi bưu điện)",
                        "<strong>Từ ví dụ:</strong> 送ります (<ruby>送<rt>おく</rt></ruby>ります - gửi đi / tiễn đưa), 郵送 (<ruby>郵<rt>ゆう</rt></ruby><ruby>送<rt>そう</rt></ruby> - gửi bưu điện)")

    html = html.replace("<strong>Từ ví dụ:</strong> 使います (つかいます - sử dụng), 大使館 (たいしかん - đại sứ quán)",
                        "<strong>Từ ví dụ:</strong> 使います (<ruby>使<rt>つか</rt></ruby>います - sử dụng), 大使館 (<ruby>大<rt>たい</rt></ruby><ruby>使<rt>し</rt></ruby><ruby>館<rt>かん</rt></ruby> - đại sứ quán)")

    html = html.replace("<strong>Từ ví dụ:</strong> 借ります (かります - vay mượn), 借金 (しゃっきん - khoản nợ)",
                        "<strong>Từ ví dụ:</strong> 借ります (<ruby>借<rt>か</rt></ruby>ります - vay mượn), 借金 (<ruby>借<rt>しゃっ</rt></ruby><ruby>金<rt>きん</rt></ruby> - khoản nợ)")

    # Update VOCAB_DATA example sentences with ruby
    vocab_ex_ruby = {
        1: ("あかるくて ひろい オフィスです。", "Văn phòng làm việc sáng sủa và rộng rãi."),
        2: ("<ruby>資料<rt>しりょう</rt></ruby>は キャビネットの <ruby>中<rt>なか</rt></ruby>に あります。", "Tài liệu nằm ở bên trong tủ đựng hồ sơ."),
        3: ("コピー<ruby>機<rt>き</rt></ruby>の <ruby>使<rt>つか</rt></ruby>い<ruby>方<rt>かた</rt></ruby>を <ruby>教<rt>おし</rt></ruby>えてください。", "Xin hãy chỉ cho tôi cách sử dụng máy photo."),
        4: ("ファックスで <ruby>書類<rt>しょるい</rt></ruby>を <ruby>送<rt>おく</rt></ruby>ります。", "Gửi giấy tờ qua đường máy fax."),
        5: ("<ruby>会社<rt>かいしゃ</rt></ruby>から <ruby>国際電話<rt>こくさいでんわ</rt></ruby>を かけます。", "Gọi điện thoại quốc tế từ công ty."),
        6: ("<ruby>社長<rt>しゃちょう</rt></ruby>に あいさつを します。", "Chào hỏi giám đốc công ty."),
        7: ("<ruby>秘書<rt>ひしょ</rt></ruby>に スケジュールを <ruby>聞<rt>き</rt></ruby>きます。", "Hỏi thư ký về lịch làm việc."),
        8: ("1<ruby>階<rt>かい</rt></ruby>の <ruby>受付<rt>うけつけ</rt></ruby>で <ruby>待<rt>ま</rt></ruby>っています。", "Tôi đang đợi ở quầy lễ tân tầng 1."),
        9: ("<ruby>事務<rt>じむ</rt></ruby>スタッフが <ruby>手伝<rt>てつだ</rt></ruby>って くれました。", "Nhân viên văn phòng đã giúp đỡ tôi."),
        10: ("ドライバーが <ruby>来<rt>く</rt></ruby>るまで <ruby>待<rt>ま</rt></ruby>っています。", "Bác tài xế đang đợi sẵn ở ô tô."),
        11: ("ドアを ノックしてから <ruby>入<rt>はい</rt></ruby>ります。", "Gõ cửa trước khi bước vào phòng."),
        12: ("<ruby>窓<rt>まど</rt></ruby>を <ruby>開<rt>あ</rt></ruby>けて、<ruby>風<rt>かぜ</rt></ruby>を <ruby>入<rt>い</rt></ruby>れます。", "Mở cửa sổ cho gió thoáng vào."),
        13: ("ドアを <ruby>開<rt>あ</rt></ruby>けても いいですか。", "Tôi mở cửa có được không ạ?"),
        14: ("<ruby>寒<rt>さむ</rt></ruby>iので、ドアを <ruby>閉<rt>し</rt></ruby>めます。".replace("寒<rt>さむ</rt>i", "寒<rt>さむ</rt>い"), "Trời lạnh nên tôi đóng cửa lại."),
        15: ("<ruby>暗<rt>くら</rt></ruby>いので <ruby>電気<rt>でんき</rt></ruby>を <ruby>点<rt>つ</rt></ruby>けます。", "Phòng tối nên tôi bật đèn lên."),
        16: ("<ruby>帰<rt>かえ</rt></ruby>る<ruby>前<rt>まえ</rt></ruby>に <ruby>電気<rt>でんき</rt></ruby>を <ruby>消<rt>け</rt></ruby>してください。", "Trước khi về nhớ tắt điện nhé."),
        17: ("パソコンが <ruby>壊<rt>こわ</rt></ruby>れて、<ruby>動<rt>うご</rt></ruby>きません。", "Máy tính bị hỏng nên không hoạt động."),
        18: ("<ruby>今<rt>いま</rt></ruby> <ruby>日本語<rt>にほんご</rt></ruby>を <ruby>勉強中<rt>べんきょうちゅう</rt></ruby>です。", "Tôi đang trong giờ học tiếng Nhật."),
        19: ("<ruby>彼<rt>かれ</rt></ruby>は <ruby>英語<rt>えいご</rt></ruby>が ぺらぺらです。", "Anh ấy nói tiếng Anh cực kỳ lưu loát."),
        20: ("では、<ruby>会議<rt>かいぎ</rt></ruby>を <ruby>始<rt>はじ</rt></ruby>めましょう。", "Nào, chúng ta bắt đầu cuộc họp nhé."),
        21: ("このファイルを <ruby>見<rt>み</rt></ruby>てください。", "Hãy xem tập tài liệu này."),
        22: ("<ruby>大事<rt>だいじ</rt></ruby>なことを メモに <ruby>書<rt>か</rt></ruby>きます。", "Viết việc quan trọng vào giấy ghi chú."),
        23: ("<ruby>事務所<rt>じむしょ</rt></ruby>に <ruby>資料<rt>しりょう</rt></ruby>を <ruby>取<rt>と</rt></ruby>りに <ruby>行<rt>い</rt></ruby>きます。", "Đi đến văn phòng để lấy tài liệu."),
        24: ("このメールを プリントアウトしてください。", "Hãy in email này ra giúp tôi nhé."),
        25: ("<ruby>新<rt>あたら</rt></ruby>しい スタッフを <ruby>紹介<rt>しょうかい</rt></ruby>します。", "Tôi xin phép giới thiệu nhân viên mới.")
    }

    m_vocab = re.search(r"const VOCAB_DATA = (\[.*?\]);\s*window\.VOCAB_DATA", html, re.DOTALL)
    if m_vocab:
        vocab_list = json.loads(m_vocab.group(1))
        for v in vocab_list:
            vid = v.get("id")
            if vid in vocab_ex_ruby:
                v["exJp"] = vocab_ex_ruby[vid][0]
                v["exVi"] = vocab_ex_ruby[vid][1]
        new_vocab_json = json.dumps(vocab_list, ensure_ascii=False)
        html = html[:m_vocab.start(1)] + new_vocab_json + html[m_vocab.end(1):]
        print("Updated VOCAB_DATA exJp with ruby tags.")

    # Update VERB_MORPH_DATA with ruby
    verb_morph_data = [
        {
            "kanji": "<ruby>使<rt>つか</rt></ruby>います",
            "masu": "つかいます",
            "vi": "Sử dụng",
            "col2": "<ruby>使<rt>つか</rt></ruby>って",
            "col3": "<ruby>使<rt>つか</rt></ruby>ってもいいですか",
            "col4": "<ruby>使<rt>つか</rt></ruby>ってはいけません",
            "col5": "どうぞ<ruby>使<rt>つか</rt></ruby>ってください",
            "ex": "このパソコンを<ruby>使<rt>つか</rt></ruby>ってもいいですか。―― はい、どうぞ。"
        },
        {
            "kanji": "<ruby>借<rt>か</rt></ruby>ります",
            "masu": "かります",
            "vi": "Vay mượn",
            "col2": "<ruby>借<rt>か</rt></ruby>りて",
            "col3": "<ruby>借<rt>か</rt></ruby>りてもいいですか",
            "col4": "<ruby>借<rt>か</rt></ruby>りてはいけません",
            "col5": "どうぞ<ruby>借<rt>か</rt></ruby>りてください",
            "ex": "ペンを<ruby>借<rt>か</rt></ruby>りてもいいですか。―― ええ、いいですよ。"
        },
        {
            "kanji": "<ruby>開<rt>あ</rt></ruby>けます",
            "masu": "あけます",
            "vi": "Mở cửa",
            "col2": "<ruby>開<rt>あ</rt></ruby>けて",
            "col3": "<ruby>開<rt>あ</rt></ruby>けてもいいですか",
            "col4": "<ruby>開<rt>あ</rt></ruby>けてはいけません",
            "col5": "どうぞ<ruby>開<rt>あ</rt></ruby>けてください",
            "ex": "<ruby>少<rt>すこ</rt></ruby>し<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてもいいですか。―― どうぞ。"
        },
        {
            "kanji": "つけます",
            "masu": "つけます",
            "vi": "Bật (đèn/điều hòa)",
            "col2": "つけて",
            "col3": "つけてもいいですか",
            "col4": "つけてはいけません",
            "col5": "どうぞつけてください",
            "ex": "<ruby>暗<rt>くら</rt></ruby>いので<ruby>電気<rt>でんき</rt></ruby>をつけてもいいですか。"
        },
        {
            "kanji": "<ruby>入<rt>はい</rt></ruby>ります",
            "masu": "はいります",
            "vi": "Đi vào phòng",
            "col2": "<ruby>入<rt>はい</rt></ruby>って",
            "col3": "<ruby>入<rt>はい</rt></ruby>ってもいいですか",
            "col4": "<ruby>入<rt>はい</rt></ruby>ってはいけません",
            "col5": "どうぞお<ruby>入<rt>はい</rt></ruby>りください",
            "ex": "<ruby>失礼<rt>しつれい</rt></ruby>します。<ruby>入<rt>はい</rt></ruby>ってもいいですか。"
        }
    ]
    m_v = re.search(r"const VERB_MORPH_DATA = (\[.*?\]);\s*const QUIZ_QUESTIONS", html, re.DOTALL)
    if m_v:
        html = html[:m_v.start(1)] + json.dumps(verb_morph_data, ensure_ascii=False) + html[m_v.end(1):]
        print("Updated VERB_MORPH_DATA with ruby tags.")

    # Update QUIZ_QUESTIONS with ruby
    quiz_questions = [
        {"id": 1, "category": "Ngữ pháp: V-てもいいですか", "q": "この コンピューター、[____] も いいですか。", "options": ["<ruby>使<rt>つか</rt></ruby>って", "<ruby>使<rt>つか</rt></ruby>いた", "<ruby>使<rt>つか</rt></ruby>います", "<ruby>使<rt>つか</rt></ruby>う"], "correct": 0, "explain": "Cấu trúc xin phép lịch sự: V-て + もいいですか ➔ 「<ruby>使<rt>つか</rt></ruby>ってもいいですか」 (Tôi dùng có được không?)."},
        {"id": 2, "category": "Ngữ pháp: V-てもいいですか", "q": "ペンを [____] も いいですか (<ruby>借<rt>か</rt></ruby>りる)。", "options": ["<ruby>借<rt>か</rt></ruby>りて", "<ruby>借<rt>か</rt></ruby>って", "<ruby>借<rt>か</rt></ruby>りた", "<ruby>借<rt>か</rt></ruby>る"], "correct": 0, "explain": "Động từ nhóm 2: <ruby>借<rt>か</rt></ruby>ります ➔ chia thể Te là 「<ruby>借<rt>か</rt></ruby>りて」 + もいいですか."},
        {"id": 3, "category": "Ngữ pháp: Phản hồi xin phép", "q": "「<ruby>使<rt>つか</rt></ruby>ってもいいですか。」――「[____]、どうぞ。」", "options": ["はい", "いいえ", "だめ", "ごめん"], "correct": 0, "explain": "Khi đồng ý cho phép ai đó sử dụng đồ vật: 「はい、どうぞ」 (Vâng, xin mời)."},
        {"id": 4, "category": "Ngữ pháp: Từ chối khéo", "q": "Khi đang bận dùng đồ mà người khác muốn mượn, cách từ chối khéo léo nhất là:", "options": ["すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っているんです", "<ruby>絶対<rt>ぜったい</rt></ruby>に だめです", "<ruby>嫌<rt>いや</rt></ruby>です", "<ruby>使<rt>つか</rt></ruby>わないでください"], "correct": 0, "explain": "Cách từ chối lịch sự trong văn hóa Nhật: 「すみません、<ruby>今<rt>いま</rt></ruby> <ruby>使<rt>つか</rt></ruby>っているんです」 (Xin lỗi, hiện tại tôi đang dùng mất rồi)."},
        {"id": 5, "category": "Ngữ pháp: V-てはいけません", "q": "ここで <ruby>写真<rt>しゃしん</rt></ruby>を [____] は いけません。", "options": ["<ruby>撮<rt>と</rt></ruby>って", "<ruby>撮<rt>と</rt></ruby>り", "<ruby>撮<rt>と</rt></ruby>る", "<ruby>撮<rt>と</rt></ruby>った"], "correct": 0, "explain": "Mẫu câu cấm đoán: V-て + はいけません ➔ 「<ruby>撮<rt>と</rt></ruby>っては いけません」 (Không được chụp ảnh)."},
        {"id": 6, "category": "Từ vựng: Thiết bị văn phòng", "q": "<ruby>書類<rt>しょるい</rt></ruby>を たくさん <ruby>紙<rt>かみ</rt></ruby>に コピーする <ruby>機械<rt>きかい</rt></ruby>は [____] です。", "options": ["コピー<ruby>機<rt>き</rt></ruby>", "エアコン", "キャビネット", "テレビ"], "correct": 0, "explain": "Máy in và sao chép tài liệu là 「コピー<ruby>機<rt>き</rt></ruby>」 (コピーき - Máy photocopy)."},
        {"id": 7, "category": "Từ vựng: Văn phòng", "q": "パソコンを <ruby>開<rt>ひら</rt></ruby>く ときに <ruby>入力<rt>にゅうりょく</rt></ruby>する <ruby>秘密<rt>ひみつ</rt></ruby>の <ruby>文字<rt>もじ</rt></ruby>は [____] です。", "options": ["パスワード", "チケット", "スケジュール", "フライト"], "correct": 0, "explain": "Mật khẩu máy tính là 「パスワード」 (Password)."},
        {"id": 8, "category": "Từ vựng: Nhân sự", "q": "<ruby>社長<rt>しゃちょう</rt></ruby>の <ruby>身<rt>み</rt></ruby>の<ruby>回<rt>まわ</rt></ruby>りの <ruby>仕事<rt>しごと</rt></ruby>を <ruby>手伝<rt>てつだ</rt></ruby>う <ruby>人<rt>ひと</rt></ruby>は [____] です。", "options": ["<ruby>秘書<rt>ひしょ</rt></ruby>", "ドライバー", "<ruby>受付<rt>うけつけ</rt></ruby>", "<ruby>学生<rt>がくせい</rt></ruby>"], "correct": 0, "explain": "Người làm trợ lý, thư ký hỗ trợ giám đốc là 「<ruby>秘書<rt>ひしょ</rt></ruby>」 (ひしょ)."},
        {"id": 9, "category": "Giao tiếp: Kết thúc công tác", "q": "Khi chào tạm biệt chi nhánh sau chuyến công tác, câu nói cảm ơn chuẩn là:", "options": ["<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました", "ごちそうさ起来", "いただきます", "お<ruby>大事<rt>だいじ</rt></ruby>に"].__class__(["<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました", "ごちそうさまでした", "いただきます", "お<ruby>大事<rt>だいじ</rt></ruby>に"]), "correct": 0, "explain": "「<ruby>大変<rt>たいへん</rt></ruby> お<ruby>世話<rt>せわ</rt></ruby>になりました」 (Cảm ơn anh chị đã hết lòng giúp đỡ tôi)."},
        {"id": 10, "category": "Giao tiếp: Nhờ chuyển lời", "q": "「<ruby>本社<rt>ほんしゃ</rt></ruby>の <ruby>皆<rt>みな</rt></ruby>さんに よろしく [____] ください。」", "options": ["お<ruby>伝<rt>つた</rt></ruby>え", "<ruby>言<rt>い</rt></ruby>って", "<ruby>話<rt>はな</rt></ruby>して", "<ruby>書<rt>か</rt></ruby>いて"], "correct": 0, "explain": "Nhờ chuyển lời thăm hỏi lịch sự: 「よろしくお<ruby>伝<rt>つた</rt></ruby>えください」 (おつたえください)."},
        {"id": 11, "category": "Chữ Hán Bài 14: 自 & 分", "q": "Từ 「じぶん」 (Bản thân mình) viết Hán tự là:", "options": ["自分", "白分", "自刀", "目分"], "correct": 0, "explain": "「じぶん」 viết chữ Hán là 「自分」 (TỰ PHÂN: <ruby>自<rt>じ</rt></ruby><ruby>分<rt>ぶん</rt></ruby>)."},
        {"id": 12, "category": "Chữ Hán Bài 14: 電 & 話", "q": "Từ 「でんわ」 (Điện thoại) gồm 2 chữ Hán nào?", "options": ["電話", "電気", "電車", "電送"], "correct": 0, "explain": "「でんわ」 là 「電話」 (<ruby>電<rt>でん</rt></ruby><ruby>話<rt>わ</rt></ruby> - cả 2 chữ đều có 13 nét)."},
        {"id": 13, "category": "Chữ Hán Bài 14: 使 (Sử)", "q": "Động từ 「つかいます」 (Sử dụng) có chữ Hán là:", "options": ["使います", "借ります", "送ります", "作ります"], "correct": 0, "explain": "「つかいます」 là 「使います」 (<ruby>使<rt>つか</rt></ruby>います - SỬ, 8 nét)."},
        {"id": 14, "category": "Chữ Hán Bài 14: 借 (Tá)", "q": "Động từ 「かります」 (Vay mượn) có chữ Hán là:", "options": ["借ります", "使います", "送ります", "働きます"], "correct": 0, "explain": "「かります」 là 「借ります」 (<ruby>借<rt>か</rt></ruby>ります - TÁ, 10 nét, bộ Nhân đứng 亻 + chữ Tích 昔)."},
        {"id": 15, "category": "Chữ Hán Bài 14: 送 (Tống)", "q": "Động từ 「おくります」 trong 「メールを 送ります」 có chữ Hán là:", "options": ["送ります", "通ります", "連ります", "返ります"], "correct": 0, "explain": "「おくります」 viết chữ Hán là 「送ります」 (<ruby>送<rt>おく</rt></ruby>ります - TỐNG, 9 nét)."}
    ]
    m_q = re.search(r"const QUIZ_QUESTIONS = (\[.*?\]);\s*const DIALOGUE_STEPS", html, re.DOTALL)
    if m_q:
        html = html[:m_q.start(1)] + json.dumps(quiz_questions, ensure_ascii=False) + html[m_q.end(1):]
        print("Updated QUIZ_QUESTIONS with ruby tags.")

    # Update DIALOGUE_STEPS with ruby
    dialogue_steps = [
        {
            "options": [
                {
                    "text": "すみません、このパソコンをお<ruby>借<rt>か</rt></ruby>りしてもいいですか。",
                    "vi": "Xin lỗi cô, tôi mượn chiếc máy tính này một chút có được không ạ?",
                    "replyAvatar": "👩‍💼",
                    "replyNpc": "Kathy",
                    "replyText": "はい、どうぞ！パスワードは<ruby>画面<rt>がめん</rt></ruby>の<ruby>横<rt>よこ</rt></ruby>にメモしてありますよ。",
                    "replyVi": "Vâng, xin mời anh cứ tự nhiên dùng! Mật khẩu được ghi chú ngay bên cạnh màn hình đó ạ."
                },
                {
                    "text": "<ruby>資料<rt>しりょう</rt></ruby>を<ruby>印刷<rt>いんさつ</rt></ruby>したいのですが、プリンターを<ruby>使<rt>つか</rt></ruby>ってもいいですか。",
                    "vi": "Tôi muốn in một số tài liệu, tôi dùng máy in có được không ạ?",
                    "replyAvatar": "👩‍💼",
                    "replyNpc": "Kathy",
                    "replyText": "ええ、<ruby>大丈夫<rt>だいじょうぶ</rt></ruby>です。あちらのコピー<ruby>機<rt>き</rt></ruby>に<ruby>繋<rt>つな</rt></ruby>がっていますよ。",
                    "replyVi": "Vâng, được chứ ạ. Máy tính đã được kết nối với chiếc máy in đằng kia rồi đó."
                }
            ]
        },
        {
            "npcName": "Kathy",
            "avatar": "👩‍💼",
            "npcText": "<ruby>出張<rt>しゅっちょう</rt></ruby>のお<ruby>仕事<rt>しごと</rt></ruby>は<ruby>順調<rt>じゅんちょう</rt></ruby>に<ruby>進<rt>すす</rt></ruby>みましたか。もうすぐ<ruby>空港<rt>くうこう</rt></ruby>へ<ruby>向<rt>む</rt></ruby>かいますね。",
            "npcVi": "Công việc trong chuyến công tác diễn ra thuận lợi chứ ạ? Anh sắp sửa ra sân bay rồi nhỉ.",
            "options": [
                {
                    "text": "はい、<ruby>大変<rt>たいへん</rt></ruby>お<ruby>世話<rt>せわ</rt></ruby>になりました！<ruby>本社<rt>ほんしゃ</rt></ruby>の<ruby>皆<rt>みな</rt></ruby>さんによろしくお<ruby>伝<rt>つた</rt></ruby>えください。",
                    "vi": "Vâng, cảm ơn mọi người đã hết lòng giúp đỡ tôi! Cho tôi gửi lời chào hỏi thăm tới mọi người ở trụ sở chính nhé.",
                    "replyAvatar": "👩‍💼",
                    "replyNpc": "Kathy",
                    "replyText": "はい、<ruby>必<rt>かなら</rt></ruby>ず<ruby>伝<rt>つた</rt></ruby>えます！お<ruby>気<rt>き</rt></ruby>をつけてお<ruby>帰<rt>かえ</rt></ruby>りくださいね。",
                    "replyVi": "Vâng, tôi nhất định sẽ chuyển lời ạ! Chúc anh thượng lộ bình an nhé."
                },
                {
                    "text": "おかげさまで<ruby>無事<rt>ぶじ</rt></ruby>に<ruby>終<rt>お</rt></ruby>わりました。また<ruby>東京<rt>とうきょう</rt></ruby>で<ruby>会<rt>あ</rt></ruby>いましょう！",
                    "vi": "Nhờ có mọi người mà công việc đã hoàn thành tốt đẹp. Hẹn sớm gặp lại cô tại Tokyo nhé!",
                    "replyAvatar": "👩‍💼",
                    "replyNpc": "Kathy",
                    "replyText": "こちらこそ！またのお<ruby>越<rt>こ</rt></ruby>しを<ruby>心<rt>こころ</rt></ruby>よりお<ruby>待<rt>ま</rt></ruby>ちしております。",
                    "replyVi": "Chúng tôi cũng rất vinh hạnh! Rất mong được đón tiếp anh trong những lần tới."
                }
            ]
        }
    ]
    m_d = re.search(r"const DIALOGUE_STEPS = (\[.*?\]);\s*// Furigana Toggle Logic", html, re.DOTALL)
    if not m_d:
        m_d = re.search(r"const DIALOGUE_STEPS = (\[.*?\]);\s*// Tokyo Audio Speech Synthesis", html, re.DOTALL)
    if m_d:
        html = html[:m_d.start(1)] + json.dumps(dialogue_steps, ensure_ascii=False) + html[m_d.end(1):]
        print("Updated DIALOGUE_STEPS with ruby tags.")

    # Update JS: updateMorphDisplay to render innerHTML for col2-col5 and ex
    old_morph_js = """            document.getElementById('morphVi').textContent = v.vi;
            document.getElementById('morphTe').textContent = v.col2;
            document.getElementById('morphTeIki').textContent = v.col3;
            document.getElementById('morphTeKi').textContent = v.col4;
            document.getElementById('morphMashou').textContent = v.col5;
            document.getElementById('morphExText').textContent = v.ex;"""

    new_morph_js = """            document.getElementById('morphVi').textContent = v.vi;
            document.getElementById('morphTe').innerHTML = v.col2;
            document.getElementById('morphTeIki').innerHTML = v.col3;
            document.getElementById('morphTeKi').innerHTML = v.col4;
            document.getElementById('morphMashou').innerHTML = v.col5;
            document.getElementById('morphExText').innerHTML = v.ex;"""

    html = html.replace(old_morph_js, new_morph_js)

    # Add Furigana toggle functions to JS
    furigana_js = """
        // Furigana Toggle Logic
        function toggleFurigana() {
            document.body.classList.toggle('hide-furigana');
            const isHidden = document.body.classList.contains('hide-furigana');
            const btn = document.getElementById('btnFuriganaToggle');
            const label = document.getElementById('furiganaBtnLabel');
            if (btn && label) {
                if (isHidden) {
                    btn.classList.add('off');
                    label.textContent = 'Furigana: TẮT';
                } else {
                    btn.classList.remove('off');
                    label.textContent = 'Furigana: BẬT';
                }
            }
            try { localStorage.setItem('marugoto_furigana', isHidden ? 'off' : 'on'); } catch(e) {}
        }

        (function initFuriganaPref() {
            try {
                const pref = localStorage.getItem('marugoto_furigana');
                if (pref === 'off') {
                    document.body.classList.add('hide-furigana');
                    window.addEventListener('DOMContentLoaded', () => {
                        const btn = document.getElementById('btnFuriganaToggle');
                        const label = document.getElementById('furiganaBtnLabel');
                        if (btn && label) {
                            btn.classList.add('off');
                            label.textContent = 'Furigana: TẮT';
                        }
                    });
                }
            } catch(e) {}
        })();
"""
    if "function toggleFurigana" not in html:
        html = html.replace("// Tokyo Audio Speech Synthesis", furigana_js + "\n        // Tokyo Audio Speech Synthesis")

    with open("lessons/Marugoto_A2_Lesson_14.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("lessons/Marugoto_A2_Lesson_14.html completely updated!")

if __name__ == "__main__":
    update_lesson_14()
