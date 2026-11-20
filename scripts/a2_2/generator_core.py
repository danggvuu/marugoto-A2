# -*- coding: utf-8 -*-
"""
Core Generator utilities for Marugoto A2-2 Lessons.
Provides shared SVG rendering, JS builder with quiz balancing,
and unified responsive HTML lesson page generation.
"""

import json
import hashlib
from html import escape
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[2]


def make_svg(label, icon, color1="#4f46e5", color2="#7c3aed"):
    gradient_id = "g_" + hashlib.sha256(label.encode("utf-8")).hexdigest()[:16]
    return f'''<svg viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="{gradient_id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{color1}"/>
      <stop offset="100%" stop-color="{color2}"/>
    </linearGradient>
  </defs>
  <rect width="240" height="120" rx="14" fill="url(#{gradient_id})"/>
  <circle cx="120" cy="50" r="30" fill="rgba(255,255,255,0.2)"/>
  <text x="120" y="60" text-anchor="middle" font-size="32">{icon}</text>
</svg>'''


def build_js_file(dest_path, vocab_list, verb_list, quiz_list, badge_name):
    """
    Builds the lesson JS file with balanced quiz positions (4, 4, 4, 3 distribution)
    and full flashcard / verb lab interactive handlers.
    """
    assert len(quiz_list) == 15, f"Quiz must contain exactly 15 questions, got {len(quiz_list)}"

    # Stable, balanced answer positions keep saved attempts reproducible.
    positions = [i % 4 for i in range(len(quiz_list))]
    random.Random(badge_name).shuffle(positions)

    processed_quiz = []
    for q, position in zip(quiz_list, positions):
        assert len(q["options"]) == 4, f"Each question must have 4 options: {q['q']}"
        answer = q["options"][q["correct"]]
        options = [option for i, option in enumerate(q["options"]) if i != q["correct"]]
        options.insert(position, answer)
        processed_quiz.append({**q, "options": options, "correct": position})

    # Prepare vocab objects
    processed_vocab = []
    for idx, v in enumerate(vocab_list, 1):
        processed_vocab.append({
            "id": idx,
            "cat": "vocab",
            "catName": "Từ Vựng",
            "badge": badge_name,
            "jp": v["jp"],
            "kana": v["kana"],
            "kanji": v["kanji"],
            "romaji": v["romaji"],
            "vi": v["vi"],
            "svg": make_svg(v["vi"], v.get("icon", "📖"))
        })

    js_content = f'''/* Marugoto A2-2 {badge_name} - Extracted Data & Logic */
const VOCAB_DATA = {json.dumps(processed_vocab, ensure_ascii=False, indent=2)};

const VERB_DATA = {json.dumps(verb_list, ensure_ascii=False, indent=2)};

const QUIZ_DATA = {json.dumps(processed_quiz, ensure_ascii=False, indent=2)};

function escapeLessonText(value) {{
    return String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}}

// Render Verb Lab
function initVerbLab() {{
    const row = document.getElementById('verbSelectorRow');
    if (!row || !VERB_DATA.length) return;
    row.innerHTML = '';
    VERB_DATA.forEach((v, idx) => {{
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `btn-verb-chip ${{idx === 0 ? 'active' : ''}}`;
        btn.textContent = `${{v.masu}} (${{v.vi}})`;
        btn.onclick = () => selectVerb(idx);
        row.appendChild(btn);
    }});
    selectVerb(0);
}}

function selectVerb(idx) {{
    const chips = document.querySelectorAll('.btn-verb-chip');
    chips.forEach((c, i) => c.classList.toggle('active', i === idx));
    const v = VERB_DATA[idx];
    if (!v) return;

    const elMasu = document.getElementById('morphMasu');
    const elVi = document.getElementById('morphVi');
    const elTe = document.getElementById('morphTe');
    const elForm1 = document.getElementById('morphTeIki');
    const elForm2 = document.getElementById('morphTeKi');
    const elForm3 = document.getElementById('morphMashou');

    if (elMasu) elMasu.textContent = v.masu || '---';
    if (elVi) elVi.textContent = v.vi || '---';
    if (elTe) elTe.textContent = v.te || '---';
    if (elForm1) elForm1.textContent = v.form1 || '---';
    if (elForm2) elForm2.textContent = v.form2 || '---';
    if (elForm3) elForm3.textContent = v.form3 || '---';
}}

// Render Flashcards
function initFlashcards() {{
    const grid = document.getElementById('flashcardGrid');
    if (!grid) return;
    grid.innerHTML = '';
    VOCAB_DATA.forEach(v => {{
        const card = document.createElement('button');
        card.type = 'button';
        card.className = 'fc-item';
        card.setAttribute('aria-label', `Nghe ${{v.jp}}`);
        card.onclick = () => {{
            if (typeof speakText === 'function') speakText(v.kana || v.jp);
        }};
        card.innerHTML = `
            <span class="fc-svg-wrap" aria-hidden="true">${{v.svg}}</span>
            <span class="fc-content">
                <span class="fc-jp" lang="ja">${{escapeLessonText(v.jp)}}</span>
                <span class="fc-kana" lang="ja">${{escapeLessonText(v.kana)}}</span>
                <span class="fc-romaji">${{escapeLessonText(v.romaji)}}</span>
                <span class="fc-vi">${{escapeLessonText(v.vi)}}</span>
                <span class="fc-listen">🔊 Nghe phát âm</span>
            </span>
        `;
        grid.appendChild(card);
    }});
}}

// Render Quiz
function initQuiz() {{
    const c = document.getElementById('quizContainer');
    if (!c) return;
    c.innerHTML = '';
    QUIZ_DATA.forEach((q, qIdx) => {{
        const qBox = document.createElement('div');
        qBox.className = 'quiz-card';
        const optsHtml = q.options.map((opt, oIdx) => `
            <button type="button" class="quiz-opt" onclick="checkQuizAnswer(this, ${{qIdx}}, ${{oIdx}}, 'a22-reviewed-v2')">${{escapeLessonText(opt)}}</button>
        `).join('');
        qBox.innerHTML = `
            <div class="quiz-q"><b>Câu ${{qIdx + 1}}:</b> ${{escapeLessonText(q.q)}}</div>
            <div class="quiz-opts">${{optsHtml}}</div>
            <div class="quiz-explain" id="explain-${{qIdx}}">💡 ${{escapeLessonText(q.explain)}}</div>
        `;
        c.appendChild(qBox);
    }});
}}

function checkQuizAnswer(btn, qIdx, oIdx, revision) {{
    if (revision !== 'a22-reviewed-v2' || btn.disabled) return;
    const q = QUIZ_DATA[qIdx];
    const parent = btn.parentElement;
    const allBtns = parent.querySelectorAll('.quiz-opt');
    allBtns.forEach(b => b.disabled = true);
    if (oIdx === q.correct) {{
        btn.classList.add('correct');
    }} else {{
        btn.classList.add('wrong');
        allBtns[q.correct].classList.add('correct');
    }}
    const exp = document.getElementById(`explain-${{qIdx}}`);
    if (exp) exp.style.display = 'block';
}}

function initLessonInteractive() {{
    initVerbLab();
    initFlashcards();
    initQuiz();
}}

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initLessonInteractive);
}} else {{
    initLessonInteractive();
}}

if (typeof VOCAB_DATA !== "undefined") window.VOCAB_DATA = VOCAB_DATA;
'''
    dest_path.write_text(js_content, encoding="utf-8")
    print(f"Created {dest_path}")


def build_lesson_html(
    dest_path,
    topic_num,
    topic_name_jp,
    lesson_num,
    lesson_title,
    quote,
    subtitle,
    vocab_count,
    grammar_count,
    verb_count,
    kanji_count,
    grammar_blocks,
    kanji_cards,
    js_filename,
    section_links=None,
    morph_labels=None
):
    grammar_html = "\n".join(grammar_blocks)

    kanji_cards_html = []
    for k in kanji_cards:
        if "word" in k:
            long_class = " char-long" if len(k["word"]) >= 4 else ""
            kanji_cards_html.append(f'''        <div class="kanji-detail-card">
            <div class="kanji-big-char{long_class}" lang="ja">{k["word"]}</div>
            <div class="kanji-info">
                <div class="kanji-hv-title" lang="ja">{k["kana"]}</div>
                <div class="kanji-readings">{k["mean"]}</div>
            </div>
        </div>''')
        else:
            kanji_cards_html.append(f'''        <div class="kanji-detail-card">
                <div class="kanji-big-char">{k["char"]}</div>
                <div class="kanji-info">
                    <div class="kanji-hv-title">{k["hv"]} <span class="kanji-strokes-badge">{k["strokes"]} nét</span></div>
                    <div class="kanji-readings"><strong>Kun:</strong> {k["kun"]}<br>
                        <strong>On:</strong> {k["on"]}<br><strong>Từ ví dụ:</strong> {k["ex"]}</div>
                    <div class="kanji-mnemonic">💡 Mẹo nhớ: {k["mnemonic"]}</div>
                </div>
            </div>''')
    kanji_html = "\n".join(kanji_cards_html)

    if section_links:
        sec_links_html = "\n        ".join(section_links)
    else:
        sec_links_html = '''<a href="#sec-grammar1" class="sec-link">① Ngữ Pháp 1</a>
        <a href="#sec-grammar2" class="sec-link">② Ngữ Pháp 2</a>
        <a href="#sec-grammar3" class="sec-link">③ Ngữ Pháp 3</a>'''

    if not morph_labels:
        morph_labels = {
            "form1": "Dạng ～ています (tiếp diễn / trạng thái)",
            "form2": "Thể Quá Khứ Ngắn (~ta)",
            "form3": "Thể Từ Điển (~ru / jisho)"
        }

    html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>Cẩm Nang & Luyện Tập Toàn Diện Bài {lesson_num} (A2-2) | {quote}</title>
    <meta name="description" content="Chinh phục toàn diện Marugoto A2-2 Bài {lesson_num}: {quote}. Đầy đủ ngữ pháp, 3D Flashcard từ vựng, máy biến thể và Mini Test 15 câu có giải thích chi tiết.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <!-- Animate UI Core -->
    <link rel="stylesheet" href="../assets/css/animate-ui.css">
    <script src="../assets/js/animate-ui.js" defer></script>
    <script src="../assets/js/audio-engine.js?v=2"></script>
    <link rel="stylesheet" href="../assets/css/lesson-a2-core.css?v=1">
    <link rel="stylesheet" href="../assets/css/site-theme.css?v=7">
    <link rel="stylesheet" href="../assets/css/lesson-a2-2.css?v=1">
</head>
<body class="lesson-a2-2">

<div class="main-container">
    <!-- Global Hub Navigation Placeholder -->
    <div id="navbar-placeholder"></div>

    <!-- Sticky Section Sub-Nav -->
    <div class="section-nav">
        {sec_links_html}
        <a href="#sec-verb-lab" class="sec-link">🔬 Biến Thể Động Từ</a>
        <a href="#sec-vocab" class="sec-link">🎴 {vocab_count} Flashcard</a>
        <a href="#sec-typing-practice" class="sec-link">⌨️ Luyện Gõ Từ Vựng</a>
        <a href="#sec-kanji" class="sec-link">⛩️ {kanji_count} Từ Kanji</a>
        <a href="#sec-quiz" class="sec-link">📝 Mini Test 15 Câu</a>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
        <div class="hero-badge">TOPIC {topic_num}: {topic_name_jp} • BÀI {lesson_num} (MARUGOTO A2-2)</div>
        <h1 class="hero-title">CHINH PHỤC TOÀN DIỆN BÀI {lesson_num} (A2-2)</h1>
        <div class="hero-jp-quote">
            <span>「{quote}」</span>
            <button type="button" class="btn-speak" style="background:rgba(255,255,255,0.2); border-color:#818cf8; color:#fff;" onclick="speakText('{quote}')">🔊</button>
        </div>
        <p class="hero-subtitle">
            {subtitle}
        </p>
        <div class="hero-stats-row">
            <div class="stat-card">
                <div class="stat-number">{vocab_count}</div>
                <div class="stat-label">Từ vựng Flashcard</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{grammar_count}</div>
                <div class="stat-label">Chuyên đề ngữ pháp</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{verb_count}</div>
                <div class="stat-label">Động từ mẫu Lab</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{kanji_count}</div>
                <div class="stat-label">Từ Kanji trong bài</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">15</div>
                <div class="stat-label">Câu Mini Test</div>
            </div>
        </div>
    </div>

    <!-- Grammar Sections -->
{grammar_html}

    <!-- Verb Lab Section -->
    <section class="content-section" id="sec-verb-lab">
        <div class="section-header">
            <h2 class="section-title"><span>🔬</span> Phòng Thí Nghiệm Biến Thể Động Từ</h2>
            <span class="section-tag">Interactive Verb Morph</span>
        </div>
        <p style="margin-bottom: 16px; color: #475569;">Bảng chia thể là phần luyện tập bổ trợ; các mục ngữ pháp chính thức của bài nằm ở phần trên.</p>
        
        <div class="verb-selector-row" id="verbSelectorRow"></div>

        <div class="morph-display-box">
            <div class="morph-grid">
                <div class="morph-cell">
                    <span class="morph-label">Thể Lịch Sự (~masu)</span>
                    <span class="morph-val" id="morphMasu">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">Ý Nghĩa Tiếng Việt</span>
                    <span class="morph-val" id="morphVi" style="color: #6366f1;">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">Thể TE (~te)</span>
                    <span class="morph-val" id="morphTe">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">{morph_labels['form1']}</span>
                    <span class="morph-val" id="morphTeIki">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">{morph_labels['form2']}</span>
                    <span class="morph-val" id="morphTeKi">---</span>
                </div>
                <div class="morph-cell">
                    <span class="morph-label">{morph_labels['form3']}</span>
                    <span class="morph-val" id="morphMashou">---</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Vocab 3D Flashcard Section -->
    <section class="content-section" id="sec-vocab">
        <div class="section-header">
            <h2 class="section-title"><span>🎴</span> Flashcard từ vựng theo chủ đề ({vocab_count} mục)</h2>
            <span class="section-tag">Có từ mở rộng để luyện thêm</span>
        </div>
        <p style="margin-bottom: 16px; color: #475569;">Bộ thẻ gồm từ theo chủ đề và một số từ mở rộng; không thay thế danh sách từ vựng đầy đủ trong sách. Bấm thẻ để nghe cách đọc.</p>
        <div class="flashcard-grid" id="flashcardGrid"></div>
    </section>

    <!-- Typing Practice Section -->
    <section class="content-section" id="sec-typing-practice"></section>

    <!-- Kanji Section -->
    <section class="content-section" id="sec-kanji">
        <div class="section-header">
            <h2 class="section-title"><span>⛩️</span> Từ Kanji trong Rikai Bài {lesson_num} ({kanji_count} mục)</h2>
            <span class="section-tag">Danh sách Japan Foundation</span>
        </div>
        <div class="kanji-grid">
{kanji_html}
        </div>
    </section>

    <!-- Mini Test -->
    <section class="content-section" id="sec-quiz">
        <div class="section-header">
            <h2 class="section-title"><span>📝</span> Mini Test Phản Xạ Bài {lesson_num} (15 Câu)</h2>
            <span class="section-tag">Instant Feedback</span>
        </div>
        <p style="margin-bottom: 16px; color: #475569;">Chọn đáp án đúng nhất để kiểm tra khả năng tiếp thu bài học:</p>
        <div id="quizContainer"></div>
    </section>
</div>

<!-- Scripts -->
<script src="../assets/js/lessons/{js_filename}?v=2"></script>
<script src="../assets/js/nav-dropdown.js"></script>
<script src="../assets/nav.js?v=7" defer></script>
<script src="../assets/js/jp-typing-grader.js?v=1" defer></script>
<script src="../assets/js/typing-practice.js" defer></script>
</body>
</html>
'''
    dest_path.write_text(html_content, encoding="utf-8")
    print(f"Created {dest_path}")
