import re
import os
import glob

# -------------------------------------------------------------
# 1. UNIFY CONTAINER WIDTH TO 1200px ACROSS ALL HTML FILES
# -------------------------------------------------------------
def unify_container_widths():
    files = glob.glob('*.html') + glob.glob('lessons/*.html') + glob.glob('tests/*.html')
    for fn in files:
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()

        # Update .container, .main-container, .app-container to max-width: 1200px
        c = re.sub(r'(\.container\s*\{[^}]*max-width:\s*)(?:1050px|1140px|1150px|1240px|1300px|960px|800px)', r'\g<1>1200px', c)
        c = re.sub(r'(\.main-container\s*\{[^}]*max-width:\s*)(?:1050px|1100px|1140px|1150px|1240px|1300px|960px|800px)', r'\g<1>1200px', c)
        c = re.sub(r'(\.app-container\s*\{[^}]*max-width:\s*)(?:1050px|1100px|1140px|1150px|1240px|1300px|960px|800px)', r'\g<1>1200px', c)
        c = re.sub(r'(\.hero-section\s*\{[^}]*max-width:\s*)(?:1050px|1100px|1140px|1150px|1240px|1300px|960px|800px)', r'\g<1>1200px', c)

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)

    print("Completed container width unification to 1200px across all files!")

# -------------------------------------------------------------
# 2. LESSONS 12 - 18 HERO & SUB-NAV DATA
# -------------------------------------------------------------
LESSON_DATA = {
    12: {
        'badge': '🍜 MARUGOTO A2-1 • TOPIC 6: 特別な日の料理 (Món Ăn Ngày Đặc Biệt)',
        'title': 'CHINH PHỤC TOÀN DIỆN BÀI 12',
        'quote': '「この料理、とても おいしそうですね！」',
        'quote_audio': 'この料理、とてもおいしそうですね',
        'subtitle': 'Học trọn vẹn ngữ pháp phán đoán thị giác <strong>「～そう」</strong>, cách nối tính từ miêu tả món ăn <strong>「A-くて / Na-で」</strong>, so sánh hương vị <strong>「～と似ています」</strong>, kèm Flashcard 3D và Mini Test 15 câu có giải thích chi tiết.',
        'stats': [
            ('24', 'Từ vựng Flashcard'),
            ('3', 'Mẫu câu trọng tâm'),
            ('8', 'Động/Tính từ vị giác'),
            ('7', 'Chữ Hán cốt lõi'),
            ('15', 'Câu Mini Test')
        ],
        'nav': [
            ('#sec-grammar1', '① Phán đoán (~そう)'),
            ('#sec-grammar2', '② Nối tính từ (くて/で)'),
            ('#sec-grammar3', '③ So sánh & Mời ăn'),
            ('#sec-verb-lab', '🔬 Thí Nghiệm Vị Giác'),
            ('#sec-dialogue', '💬 Đối Thoại Bàn Tiệc'),
            ('#sec-vocab', '🎴 24 Từ Vựng 3D'),
            ('#sec-kanji', '⛩️ 7 Chữ Hán Bài 12'),
            ('#sec-quiz', '📝 Mini Test 15 Câu'),
        ]
    },
    13: {
        'badge': '✈️ MARUGOTO A2-1 • TOPIC 7: 出張 (Đi Công Tác)',
        'title': 'CHINH PHỤC TOÀN DIỆN BÀI 13',
        'quote': '「田中さんに 会ったことが あります」',
        'quote_audio': '田中さんに会ったことがあります',
        'subtitle': 'Học trọn vẹn ngữ pháp nói về kinh nghiệm <strong>「V-たことがあります」</strong>, báo cáo lịch trình và thời gian <strong>「～時に着きます」</strong>, nghi thức đón khách sân bay, kèm Flashcard 3D và Mini Test 15 câu.',
        'stats': [
            ('25', 'Từ vựng Flashcard'),
            ('3', 'Mẫu câu trọng tâm'),
            ('10', 'Động từ thể Ta'),
            ('9', 'Chữ Hán cốt lõi'),
            ('15', 'Câu Mini Test')
        ],
        'nav': [
            ('#sec-grammar1', '① Kinh nghiệm (V-たことがある)'),
            ('#sec-grammar2', '② Lịch trình & Giờ giấc'),
            ('#sec-grammar3', '③ Nghi thức đón tiếp'),
            ('#sec-verb-lab', '🔬 Thể Ta & Lịch Trình'),
            ('#sec-dialogue', '💬 Đón Khách Sân Bay'),
            ('#sec-vocab', '🎴 25 Từ Vựng 3D'),
            ('#sec-kanji', '⛩️ 9 Chữ Hán Bài 13'),
            ('#sec-quiz', '📝 Mini Test 15 Câu'),
        ]
    },
    14: {
        'badge': '💻 MARUGOTO A2-1 • TOPIC 7: 職場のマナー (Quy Tắc Nơi Làm Việc)',
        'title': 'CHINH PHỤC TOÀN DIỆN BÀI 14',
        'quote': '「これ、使っても いいですか」',
        'quote_audio': 'これ、使ってもいいですか',
        'subtitle': 'Học trọn vẹn ngữ pháp xin phép lịch sự trong công việc <strong>「V-てもいいですか」</strong>, quy tắc và cấm đoán <strong>「V-てはいけません」</strong>, lời chào tạm biệt đồng nghiệp, kèm Flashcard 3D và Mini Test 15 câu.',
        'stats': [
            ('26', 'Từ vựng Flashcard'),
            ('3', 'Mẫu câu trọng tâm'),
            ('10', 'Động từ thể Te'),
            ('8', 'Chữ Hán cốt lõi'),
            ('15', 'Câu Mini Test')
        ],
        'nav': [
            ('#sec-grammar1', '① Xin phép (V-てもいいですか)'),
            ('#sec-grammar2', '② Cấm đoán (V-てはいけません)'),
            ('#sec-grammar3', '③ Lời chào tạm biệt'),
            ('#sec-verb-lab', '🔬 Thể Te & Xin Phép'),
            ('#sec-dialogue', '💬 Giao Tiếp Văn Phòng'),
            ('#sec-vocab', '🎴 26 Từ Vựng 3D'),
            ('#sec-kanji', '⛩️ 8 Chữ Hán Bài 14'),
            ('#sec-quiz', '📝 Mini Test 15 Câu'),
        ]
    },
    15: {
        'badge': '🏥 MARUGOTO A2-1 • TOPIC 8: 健康な生活 (Cuộc Sống Khỏe Mạnh)',
        'title': 'CHINH PHỤC TOÀN DIỆN BÀI 15',
        'quote': '「ラジオ体操を すると いいですよ」',
        'quote_audio': 'ラジオ体操をするといいですよ',
        'subtitle': 'Học trọn vẹn ngữ pháp giải thích triệu chứng sức khỏe <strong>「～んです」</strong>, đưa ra lời khuyên hữu ích <strong>「V-るといいですよ」</strong>, dặn dò kiêng cữ <strong>「V-ないでください」</strong>, kèm Flashcard 3D và Mini Test 15 câu.',
        'stats': [
            ('25', 'Từ vựng Flashcard'),
            ('3', 'Mẫu câu trọng tâm'),
            ('10', 'Động từ thể Nai'),
            ('9', 'Chữ Hán cốt lõi'),
            ('15', 'Câu Mini Test')
        ],
        'nav': [
            ('#sec-grammar1', '① Triệu chứng (~んです)'),
            ('#sec-grammar2', '② Lời khuyên (V-るといい)'),
            ('#sec-grammar3', '③ Khuyên can (V-ないで)'),
            ('#sec-verb-lab', '🔬 Thể Nai & Sức Khỏe'),
            ('#sec-dialogue', '💬 Khám Bệnh Tại Phòng Khám'),
            ('#sec-vocab', '🎴 25 Từ Vựng 3D'),
            ('#sec-kanji', '⛩️ 9 Chữ Hán Bài 15'),
            ('#sec-quiz', '📝 Mini Test 15 Câu'),
        ]
    },
    16: {
        'badge': '🏃 MARUGOTO A2-1 • TOPIC 8: 体にいいこと (Điều Tốt Cho Sức Khỏe)',
        'title': 'CHINH PHỤC TOÀN DIỆN BÀI 16',
        'quote': '「走ったり、泳いだり しています」',
        'quote_audio': '走ったり、泳いだりしています',
        'subtitle': 'Học trọn vẹn ngữ pháp liệt kê thói quen tiêu biểu <strong>「V-たり V-たりします」</strong>, biểu đạt mục đích vì sức khỏe <strong>「N の ために」</strong>, lời khuyên nên/không nên <strong>「V-たほうがいい」</strong>, kèm Flashcard 3D và Mini Test 15 câu.',
        'stats': [
            ('25', 'Từ vựng Flashcard'),
            ('3', 'Mẫu câu trọng tâm'),
            ('10', 'Động từ thể Tari'),
            ('10', 'Chữ Hán cốt lõi'),
            ('15', 'Câu Mini Test')
        ],
        'nav': [
            ('#sec-grammar1', '① Liệt kê (V-たり V-たり)'),
            ('#sec-grammar2', '② Mục đích (N の ために)'),
            ('#sec-grammar3', '③ Lời khuyên (V-たほうがいい)'),
            ('#sec-verb-lab', '🔬 Biến Thể Thể Tari'),
            ('#sec-dialogue', '💬 Tư Vấn Chế Độ Luyện Tập'),
            ('#sec-vocab', '🎴 25 Từ Vựng 3D'),
            ('#sec-kanji', '⛩️ 10 Chữ Hán Bài 16'),
            ('#sec-quiz', '📝 Mini Test 15 Câu'),
        ]
    },
    17: {
        'badge': '🎁 MARUGOTO A2-1 • TOPIC 9: お祝い (Chúc Mừng & Kỷ Niệm)',
        'title': 'CHINH PHỤC TOÀN DIỆN BÀI 17',
        'quote': '「誕生日に 彼に もらったんです」',
        'quote_audio': '誕生日に彼にもらったんです',
        'subtitle': 'Học trọn vẹn cấu trúc cho nhận quà tặng <strong>「あげる / もらう」</strong>, liệt kê đại diện quà mừng <strong>「とか」</strong>, định ngữ hóa hành động <strong>「V-る + もの」</strong>, kèm Flashcard 3D và Mini Test 15 câu.',
        'stats': [
            ('25', 'Từ vựng Flashcard'),
            ('3', 'Mẫu câu trọng tâm'),
            ('10', 'Động từ Cho - Nhận'),
            ('8', 'Chữ Hán cốt lõi'),
            ('15', 'Câu Mini Test')
        ],
        'nav': [
            ('#sec-grammar1', '① Nhận quà (もらう)'),
            ('#sec-grammar2', '② Tặng quà (あげる)'),
            ('#sec-grammar3', '③ Liệt kê đại diện (とか)'),
            ('#sec-verb-lab', '🔬 Động Từ Cho - Nhận'),
            ('#sec-dialogue', '💬 Khoe Quà Kỷ Niệm'),
            ('#sec-vocab', '🎴 25 Từ Vựng 3D'),
            ('#sec-kanji', '⛩️ 8 Chữ Hán Bài 17'),
            ('#sec-quiz', '📝 Mini Test 15 Câu'),
        ]
    },
    18: {
        'badge': '👘 MARUGOTO A2-1 • TOPIC 9: お祭りやイベント (Lễ Hội & Sự Kiện)',
        'title': 'CHINH PHỤC TOÀN DIỆN BÀI 18',
        'quote': '「浴衣を 着て、パーティーが いいと思います」',
        'quote_audio': '浴衣を着て、パーティーがいいと思います',
        'subtitle': 'Học trọn vẹn mẫu câu bày tỏ suy nghĩ <strong>「～と思います」</strong>, trích dẫn lời nói <strong>「～と言っていました」</strong>, hệ thống động từ mặc trang phục thể <strong>「V-ています」</strong>, kèm Flashcard 3D và Mini Test 15 câu.',
        'stats': [
            ('25', 'Từ vựng Flashcard'),
            ('3', 'Mẫu câu trọng tâm'),
            ('10', 'Động từ Trang Phục'),
            ('7', 'Chữ Hán cốt lõi'),
            ('15', 'Câu Mini Test')
        ],
        'nav': [
            ('#sec-grammar1', '① Bày tỏ ý kiến (~と思います)'),
            ('#sec-grammar2', '② Trích dẫn (~と言っていました)'),
            ('#sec-grammar3', '③ Mặc trang phục (V-ています)'),
            ('#sec-verb-lab', '🔬 Động Từ Mặc Đồ'),
            ('#sec-dialogue', '💬 Rủ Đi Lễ Hội Mùa Hè'),
            ('#sec-vocab', '🎴 25 Từ Vựng 3D'),
            ('#sec-kanji', '⛩️ 7 Chữ Hán Bài 18'),
            ('#sec-quiz', '📝 Mini Test 15 Câu'),
        ]
    }
}

# -------------------------------------------------------------
# 3. APPLY HERO & SUB-NAV TO LESSONS 12 - 18
# -------------------------------------------------------------
def apply_lessons_12_18_hero():
    for lid, data in LESSON_DATA.items():
        fn = f'lessons/Marugoto_A2_Lesson_{lid}.html'
        if not os.path.exists(fn): continue

        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()

        # Build Nav HTML
        nav_links = ''.join([f'<a href="{href}" class="sec-link">{label}</a>\n        ' for href, label in data['nav']])
        
        # Build Stats HTML
        stats_html = ''.join([f'''<div class="stat-card">
                    <div class="stat-number">{num}</div>
                    <div class="stat-label">{lbl}</div>
                </div>\n                ''' for num, lbl in data['stats']])

        hero_and_nav_html = f'''    <!-- STICKY SECTION SUB-NAV -->
    <div class="section-nav">
        {nav_links}
    </div>

    <!-- MAIN WRAPPER -->
    <div class="main-container">

        <!-- HERO BANNER -->
        <div class="hero-banner">
            <div class="hero-badge">{data['badge']}</div>
            <h1 class="hero-title">{data['title']}</h1>
            <div class="hero-jp-quote">
                <span>{data['quote']}</span>
                <button type="button" class="btn-speak" style="background:rgba(255,255,255,0.2); border-color:#6ee7b7; color:#fff;" onclick="speakText('{data['quote_audio']}')">🔊</button>
            </div>
            <p class="hero-subtitle">
                {data['subtitle']}
            </p>
            <div class="hero-stats-row">
                {stats_html}
            </div>
        </div>
'''

        # Target in lessons 12-18: between global-hub-nav close and <section class="content-section" id="sec-grammar1">
        pattern = r'(</div>\s*</div>\s*</div>\s*(?:<!--\s*GLOBAL FLOATING DOCK\s*-->)?\s*(?:</div>\s*</div>\s*</div>\s*)?)(<!--\s*GRAMMAR SECTIONS\s*-->\s*<section class="content-section" id="sec-grammar1">)'
        m = re.search(pattern, c)
        if m:
            c = c[:m.start(2)] + hero_and_nav_html + '\n        ' + c[m.start(2):]
            # Also close .main-container before <footer> or <script>
            if '</div>\n\n    <!-- FLASHCARD SCRIPT' in c:
                c = c.replace('</div>\n\n    <!-- FLASHCARD SCRIPT', '</div>\n    </div>\n\n    <!-- FLASHCARD SCRIPT', 1)
            elif '<!-- FLASHCARD SCRIPT' in c:
                c = c.replace('<!-- FLASHCARD SCRIPT', '</div>\n\n    <!-- FLASHCARD SCRIPT', 1)
            elif '<footer' in c:
                c = c.replace('<footer', '</div>\n\n    <footer', 1)
            print(f"Applied hero & subnav to Lesson {lid}!")
        else:
            # Fallback pattern
            m2 = re.search(r'(<div class="global-hub-nav">.*?</div>\s*</div>\s*</div>\s*)(.*?)(\s*<section class="content-section" id="sec-grammar1">)', c, re.DOTALL)
            if m2:
                c = c[:m2.start(3)] + '\n' + hero_and_nav_html + c[m2.start(3):]
                c = c.replace('<!-- FLASHCARD SCRIPT', '</div>\n\n    <!-- FLASHCARD SCRIPT', 1)
                print(f"Applied hero & subnav to Lesson {lid} (pattern 2)!")
            else:
                print(f"Warning: target not matched for Lesson {lid}")

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)

# -------------------------------------------------------------
# 4. RESTORE LESSON 10 HERO, SUBNAV & SECTION 1
# -------------------------------------------------------------
def restore_lesson_10():
    fn = 'lessons/Marugoto_A2_Lesson_10.html'
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # The missing block right after global-hub-nav and before Demo 2
    l10_block = '''    <div class="container">
        <!-- Hero Header -->
        <header class="hero-banner">
            <span class="hero-badge">MARUGOTO A2-1 • LESSON 10</span>
            <h1 class="hero-title">CHINH PHỤC TOÀN DIỆN BÀI 10</h1>
            <div class="hero-jp-quote" style="display:flex; justify-content:center; align-items:center; gap:10px; margin-bottom:12px;">
                <span style="font-size:1.35rem; color:#fef08a; font-family:var(--font-jp);">「日本で 一番 高い山は 富士山です」</span>
                <button type="button" class="btn-speak" style="background:rgba(255,255,255,0.2); border:1px solid #e0e7ff; color:#fff; border-radius:50%; width:32px; height:32px; cursor:pointer;" onclick="speakText('日本で一番高い山は富士山です')">🔊</button>
            </div>
            <p class="hero-subtitle">Bí kíp làm chủ 3 mẫu ngữ pháp trọng tâm (V-たい, Tần suất ～に～回, V-てみる), bảng đếm số lần chuẩn và trọn bộ 27 từ mới kèm hình ảnh minh họa sinh động!</p>
            <div class="hero-stats" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(160px, 1fr)); gap:12px; margin-top:20px;">
                <div class="hero-stat-card" style="background:rgba(255,255,255,0.1); padding:10px 14px; border-radius:12px; border:1px solid rgba(255,255,255,0.2); color:#fff; font-weight:700;">🎯 3 Điểm Ngữ Pháp</div>
                <div class="hero-stat-card" style="background:rgba(255,255,255,0.1); padding:10px 14px; border-radius:12px; border:1px solid rgba(255,255,255,0.2); color:#fff; font-weight:700;">🎴 27 Flashcards 3D</div>
                <div class="hero-stat-card" style="background:rgba(255,255,255,0.1); padding:10px 14px; border-radius:12px; border:1px solid rgba(255,255,255,0.2); color:#fff; font-weight:700;">🔬 Máy Biến Thể Động Từ</div>
                <div class="hero-stat-card" style="background:rgba(255,255,255,0.1); padding:10px 14px; border-radius:12px; border:1px solid rgba(255,255,255,0.2); color:#fff; font-weight:700;">⛩️ 6 Chữ Hán Cốt Lõi</div>
                <div class="hero-stat-card" style="background:rgba(255,255,255,0.1); padding:10px 14px; border-radius:12px; border:1px solid rgba(255,255,255,0.2); color:#fff; font-weight:700;">🏆 15 Câu Mini Test</div>
            </div>
        </header>

        <!-- Navigation Tabs -->
        <div class="section-nav" style="display:flex; gap:8px; overflow-x:auto; margin-bottom:24px; padding-bottom:4px;">
            <a href="#sec-grammar-1" class="tab-btn" style="text-decoration:none;">① Nguyện Vọng (V-たい)</a>
            <a href="#sec-grammar-2" class="tab-btn" style="text-decoration:none;">② Tần Suất (～に～回)</a>
            <a href="#sec-grammar-3" class="tab-btn" style="text-decoration:none;">③ Trải Nghiệm (V-てみる)</a>
            <a href="#sec-morph" class="tab-btn" style="text-decoration:none;">🔬 Máy Luyện Chia Thể</a>
            <a href="#sec-vocab" class="tab-btn" style="text-decoration:none;">🎴 27 Từ Mới Flashcard</a>
            <a href="#sec-quiz" class="tab-btn" style="text-decoration:none;">🏆 Mini Test 15 Câu</a>
        </div>

        <!-- ==================== PHẦN 1: NGỮ PHÁP 1 (V-たいです / V-たくないです) ==================== -->
        <section class="section-card" id="sec-grammar-1">
            <div class="section-header">
                <div class="section-title-wrap">
                    <div class="section-icon">🌟</div>
                    <div>
                        <h2 class="section-title">1. Mẫu Câu Bày Tỏ Nguyện Vọng: V-たいです / V-たくないです</h2>
                        <p style="color:var(--gray); font-size:0.9rem;">Diễn tả mong muốn hoặc không muốn làm một việc gì đó của bản thân người nói.</p>
                    </div>
                </div>
                <span class="section-badge">Ngữ Pháp Trọng Tâm #1</span>
            </div>

            <!-- Formula Box -->
            <div class="formula-box">
                <div class="formula-title">CÔNG THỨC BIẾN ĐỔI CHUẨN</div>
                <div class="formula-text">
                    [Động từ thể ます] <span style="color:#ef4444; text-decoration:line-through;">bỏ ます</span> ＋ <span class="formula-highlight">たいです</span> (Muốn làm) / <span class="formula-highlight">たくないです</span> (Không muốn làm)
                </div>
            </div>

            <!-- Demo Graphics & Visual Cards -->
            <div class="visual-demo-grid">
                <!-- Demo 1: Muốn đi Nhật -->
                <div class="demo-card">
                    <div class="demo-svg-wrap">
                        <svg width="220" height="130" viewBox="0 0 220 130" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <rect width="220" height="130" rx="12" fill="#e0f2fe"/>
                            <circle cx="110" cy="45" r="30" fill="#f87171" opacity="0.8"/>
                            <polygon points="40,110 110,35 180,110" fill="#3b82f6"/>
                            <polygon points="85,62 110,35 135,62 125,70 118,65 110,72 102,65 95,70" fill="#ffffff"/>
                            <path d="M165,30 L185,25 L180,33 L195,35 L175,42 L165,37 Z" fill="#6366f1"/>
                            <rect x="25" y="85" width="4" height="25" fill="#ef4444"/>
                            <rect x="50" y="85" width="4" height="25" fill="#ef4444"/>
                            <rect x="20" y="82" width="39" height="5" rx="2" fill="#ef4444"/>
                            <rect x="23" y="90" width="33" height="3" fill="#ef4444"/>
                        </svg>
                    </div>
                    <div class="demo-body">
                        <div class="demo-tag">Ví dụ 1: Đi du lịch / Ước mơ</div>
                        <div class="demo-jp jp-text"><span>日本に 行きたいです。</span><button class="sound-btn" onclick="speakText('日本に 行きたいです。')" title="Nghe phát âm">🔊</button></div>
                        <div class="demo-vi">Tôi muốn đi Nhật Bản.</div>
                        <div class="demo-notes"><b>行きます</b> (Đi) ➔ bỏ ます ➔ <b>行きたいです</b>.</div>
                    </div>
                </div>
'''

    # Look for the transition from global-hub-nav to Demo 2
    target_match = re.search(r'(<!--\s*Global Hub Navigation\s*-->\s*<div class="global-hub-nav">.*?</div>\s*</div>\s*</div>\s*)(.*?)(<!--\s*Demo 2:\s*Muốn làm biên dịch\s*-->)', c, re.DOTALL)
    if target_match:
        c = c[:target_match.start(2)] + '\n' + l10_block + '\n                ' + c[target_match.start(3):]
        # Ensure container closing tag at the end
        if '</div>\n\n    <!-- JavaScript Logic' not in c:
            c = c.replace('<!-- JavaScript Logic', '</div>\n\n    <!-- JavaScript Logic', 1)
        print("Restored Lesson 10 Hero, Subnav & Section 1!")
    else:
        print("Warning: target not matched in Lesson 10")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

if __name__ == '__main__':
    unify_container_widths()
    apply_lessons_12_18_hero()
    restore_lesson_10()
