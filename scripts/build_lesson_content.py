"""Apply curated content to the existing lesson shell, preserving IDs and features.

Reviewed overrides live in lesson_content_review.py. Other lesson data remain in
their existing JS files. This build is deterministic; unchanged questions retain
their answer semantics even when the displayed answer positions are balanced.
"""
from collections import Counter
from html import escape
import json
from pathlib import Path
import random
import re

from lesson_content_review import GRAMMAR, QUIZZES, VOCAB_EXAMPLES, CORRECTIONS, EXPLANATIONS

ROOT = Path(__file__).resolve().parents[1]
REVISION = "content-2026-11-16"
READINGS = json.loads((ROOT / "data/kanji_reference_checks.json").read_text(encoding="utf-8"))["readingCorrections"]


def fix_kanji_entries(entries):
    for item in entries:
        if item.get("char") in READINGS:
            item.update(READINGS[item["char"]])


def build_kanji_corrections():
    path = ROOT / "data/kanji_extracted.json"
    entries = json.loads(path.read_text(encoding="utf-8"))
    fix_kanji_entries(entries)
    path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Preserve the separately maintained mnemonics and examples in the runtime file.
    path = ROOT / "assets/data/kanji_a2_data.js"
    source = path.read_text(encoding="utf-8")
    for char, fields in READINGS.items():
        pattern = rf'(char:\s*"{char}".*?)(?=examples:)'
        def correct(match):
            block = match[0]
            for field, value in fields.items():
                block = re.sub(rf'({field}:\s*)"[^"]*"', lambda m: m[1] + json.dumps(value, ensure_ascii=False), block)
            return block
        source = re.sub(pattern, correct, source, flags=re.S)
    path.write_text(source, encoding="utf-8")


def array_match(source, name):
    match = re.search(rf"^const {name} = (\[.*?\]);+", source, re.M | re.S)
    if not match:
        raise ValueError(f"Missing data declaration: {name}")
    return match, json.loads(match[1])


def put_array(source, name, value):
    match, _ = array_match(source, name)
    return source[:match.start()] + f"const {name} = " + json.dumps(value, ensure_ascii=False) + ";" + source[match.end():]


def new_question(qid, row):
    prompt, options, explanation = row
    return dict(id=qid, category="Ngữ pháp & giao tiếp", q=prompt, options=list(options),
                correct=0, explain=explanation)


def theory_section(index, row):
    title, formula, explanation, jp, vi, pitfall = row
    # Text is escaped; only the fixed HTML shell supplies markup.
    speech = escape(json.dumps(jp, ensure_ascii=False), quote=True)
    return f'''<section class="content-section" id="sec-grammar{index}">
            <div class="section-header">
                <h2 class="section-title">{index}. {escape(title)}</h2>
                <span class="section-tag">Ngữ pháp &amp; cách dùng</span>
            </div>
            <p>{escape(explanation)}</p>
            <div class="grammar-card">
                <div class="rule-box">
                    <div class="rule-formula">{escape(formula)}</div>
                    <div class="rule-meaning">{escape(pitfall)}</div>
                </div>
                <div class="example-list"><div class="example-item">
                    <div class="ex-text-wrap">
                        <div class="ex-jp">{escape(jp)}</div>
                        <div class="ex-vi">{escape(vi)}</div>
                    </div>
                    <button type="button" class="btn-speak" onclick="speakText({speech})" aria-label="Nghe câu ví dụ">🔊</button>
                </div></div>
            </div>
            <p class="content-source">Chủ điểm: Marugoto A2-1, mục lục Rikai/Katsudoo.
                Giải thích và ví dụ do dự án biên soạn.
                <a href="../docs/pdf/R_contents_eng.pdf">Rikai</a> ·
                <a href="../docs/pdf/K_contents_eng.pdf">Katsudoo</a>
            </p>
        </section>'''


def build():
    build_kanji_corrections()
    for n in range(1, 19):
        file = ROOT / f"assets/js/lessons/lesson_{n:02}.js"
        source = file.read_text(encoding="utf-8")
        name = "QUIZ_DATA" if n < 10 else "QUIZ_QUESTIONS"
        _, questions = array_match(source, name)
        _, vocab = array_match(source, "VOCAB_DATA")
        for item in vocab:
            # The old generic "Xを勉強します" template was not an example of usage.
            if item.get("exJp") == item.get("jp", "") + "を 勉強します。":
                item.pop("exJp", None)
                item.pop("exVi", None)
        for item, example in zip(vocab, VOCAB_EXAMPLES.get(n, [])):
            item["exJp"], item["exVi"] = example
        source = put_array(source, "VOCAB_DATA", vocab)
        if re.search(r"^const KANJI_DATA = ", source, re.M):
            _, kanji = array_match(source, "KANJI_DATA")
            fix_kanji_entries(kanji)
            source = put_array(source, "KANJI_DATA", kanji)

        if n in GRAMMAR:
            questions = []
            for i, item in enumerate(vocab[:8]):
                alternatives = list(dict.fromkeys(x["vi"] for x in vocab if x["vi"] != item["vi"]))[:3]
                questions.append(dict(
                    id=i+1, category="Từ vựng", q=f'「{item["kana"]}」 có nghĩa là gì?',
                    options=[item["vi"]] + alternatives, correct=0,
                    explain=f'「{item["jp"]}」 nghĩa là {item["vi"]}. Ví dụ: {item["exJp"]} — {item["exVi"]}'
                ))
            questions.extend(new_question(i+9, row) for i, row in enumerate(QUIZZES[n]))
            html_file = ROOT / f"lessons/Marugoto_A2_Lesson_{n}.html"
            html = html_file.read_text(encoding="utf-8")
            for i, row in enumerate(GRAMMAR[n], 1):
                html, count = re.subn(
                    rf'<section class="content-section" id="sec-grammar{i}">.*?</section>',
                    lambda _: theory_section(i, row), html, count=1, flags=re.S)
                if count != 1:
                    raise ValueError(f"Missing grammar section {n}:{i}")
                html = re.sub(
                    rf'(<a href="#sec-grammar{i}" class="sec-link">).*?(</a>)',
                    lambda m: m[1] + escape(row[0].split(":")[0]) + m[2], html)
            html = html.replace(f"theo dõi cơ chế biến đổi sang các dạng ngữ pháp cốt lõi của Bài {n}:",
                                "ôn thêm thể て, ～たい, thể た và thể từ điển (phần bổ trợ, không phải toàn bộ trọng tâm bài):")
            html = html.replace('<div class="morph-tag">Cấu trúc trọng tâm</div>', '<div class="morph-tag">Mong muốn: ～たい</div>')
            html = html.replace("Cấu trúc trọng tâm 1", "Gốc ます + たい")
            html = html.replace("Cấu trúc trọng tâm 2", "Quá khứ ngắn")
            html = html.replace(f"Làm chủ toàn bộ kiến thức Bài {n} theo chuẩn giáo trình Marugoto A2-1:",
                                f"Ôn tập theo chủ đề Bài {n} Marugoto A2-1:")
            html_file.write_text(html, encoding="utf-8")

        for i, q in enumerate(questions):
            key = (n, q["id"])
            if key in CORRECTIONS:
                questions[i] = q = new_question(q["id"], CORRECTIONS[key])
            if key in EXPLANATIONS:
                q["explain"] = EXPLANATIONS[key]
            if q.get("reviewVersion") != REVISION:
                answer = q["options"][q["correct"]]
                distractors = [option for j, option in enumerate(q["options"]) if j != q["correct"]]
                # Stable balanced positions, not a reshuffle on each page load.
                positions = list(range(4)) * 4
                random.Random(20261116 + n).shuffle(positions)
                correct = positions[i]
                distractors.insert(correct, answer)
                q["options"] = distractors
                q["correct"] = correct
            q["reviewVersion"] = REVISION
            q["origin"] = "project-authored"
        if len(questions) != 15 or len({q["id"] for q in questions}) != 15:
            raise ValueError(f"Lesson {n}: inconsistent questions")
        for q in questions:
            if len(set(q["options"])) != 4 or not 0 <= q["correct"] < 4:
                raise ValueError(f"Lesson {n} Q{q['id']}: invalid choices")
        if len(Counter(q["correct"] for q in questions)) != 4:
            raise ValueError(f"Lesson {n}: unbalanced answer positions")
        source = put_array(source, name, questions)
        # Old recorded clicks must not be replayed onto revised content/positions.
        # Version only the quiz signature; vocabulary and typing checkpoints stay intact.
        for call in [
            "checkQuizAnswer(this, ${qIdx}, ${oIdx})",
            "selectQuizOption(${q.id}, ${oIdx})",
            "answerQuiz(${q.id}, ${optIdx}, this)",
        ]:
            source = source.replace('onclick="' + call + '"',
                                    'onclick="' + call[:-1] + ", '" + REVISION + "')\"")
        source = re.sub(r"Bạn đã thành thạo toàn bộ kiến thức Bài (\d+)!",
                        r"Bạn đã làm tốt quiz Bài \1. Hãy thử vận dụng mẫu câu vào hội thoại!", source)
        file.write_text(source, encoding="utf-8")
        # Match the two erroneous Kun labels embedded in static lesson cards.
        html_file = ROOT / f"lessons/Marugoto_A2_Lesson_{n}.html"
        html = html_file.read_text(encoding="utf-8")
        html = html.replace('Kun:</strong> えき', 'Kun:</strong> —')
        html = html.replace('Kun:</strong> さき、ま<', 'Kun:</strong> さき、まず<')
        html_file.write_text(html, encoding="utf-8")
        print(f"Lesson {n:02}: 15 reviewed practice items")


if __name__ == "__main__":
    build()
