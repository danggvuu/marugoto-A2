/* Focused lesson fixes. Python generators write only to in-memory sinks here.
 * Run: node qa/regression/review_lesson_fixes.js
 * After the main build, add --check-generated to verify shipped A2.2 parity.
 */
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { execFileSync } = require('child_process');
const root = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const plain = value => JSON.parse(JSON.stringify(value));
const array = (code, name) => JSON.parse(code.match(new RegExp(`^const ${name} = (\\[[\\s\\S]*?\\]);`, 'm'))[1]);

const generated = JSON.parse(execFileSync('python3', ['-B', '-c', String.raw`
import contextlib
import io
import json
from pathlib import Path
import sys

root = Path.cwd()
sys.path.insert(0, str(root / "scripts"))
from build_lesson_content import correct_runtime_kanji_readings
from scripts.a2_2.build_all_a2_2 import LESSONS_CONFIG
from scripts.a2_2.generator_core import build_js_file, build_lesson_html
from scripts.a2_2.official_curriculum import _verb_form2_label

class MemoryFile:
    def write_text(self, text, encoding=None):
        self.text = text

result = {"lessons": []}
with contextlib.redirect_stdout(io.StringIO()):
    for cfg in LESSONS_CONFIG:
        number = cfg["num"]
        js, html = MemoryFile(), MemoryFile()
        build_js_file(
            js, cfg["vocab"], cfg["verbs"], cfg["quiz"], f"Bài {number} (A2-2)",
            typing_list=cfg.get("typing_data"), kanji_practice_list=cfg.get("kanji_practice_data")
        )
        build_lesson_html(
            dest_path=html, topic_num=cfg["topic_num"], topic_name_jp=cfg["topic_name_jp"],
            lesson_num=number, lesson_title=cfg["title"], quote=cfg["quote"],
            subtitle=cfg["subtitle"], vocab_count=len(cfg["vocab"]),
            grammar_count=len(cfg["grammar"]), verb_count=len(cfg["verbs"]),
            kanji_count=len(cfg["kanji_list"]), grammar_blocks=cfg["grammar"],
            kanji_cards=cfg["kanji_cards"], js_filename=f"lesson_a2_2_{number:02}.js",
            section_links=cfg["section_links"], morph_labels=cfg["morph_labels"],
            quiz_count=len(cfg["quiz"]), sentence_practice_count=len(cfg.get("typing_data", [])))
        result["lessons"].append({"number": number, "code": js.text, "html": html.text})

runtime = (root / "assets/data/kanji_a2_data.js").read_text(encoding="utf-8")
result["kanji"] = correct_runtime_kanji_readings(runtime)
assert correct_runtime_kanji_readings(result["kanji"]) == result["kanji"]
fixture = '''var kanjiData = [
    {char: "駅", lesson: "L7", lessonName: "Bài 7", kun: "bad", on: "bad", examples: [{on: "keep"}]},
    {char: "先", lesson: "L9", lessonName: "Bài 9", kun: "bad", on: "bad", examples: []},
    {char: "歩", lesson: "L16", lessonName: "Bài 16", on: "bad", examples: []},
    {char: "結", lesson: "L17", lessonName: "Bài 17", on: "bad", examples: []},
    {char: "先", lesson: "L18", lessonName: "Bài 18", kun: "bad", on: "bad", examples: []}
];'''
result["kanjiFixture"] = correct_runtime_kanji_readings(fixture)
try:
    _verb_form2_label("unreviewed form")
except ValueError:
    pass
else:
    raise AssertionError("Unknown supplementary forms must not silently receive a past label")
print(json.dumps(result, ensure_ascii=False))
`], { cwd: root, encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 }));

function classList() {
    const values = new Set();
    return {
        add: value => values.add(value),
        remove: value => values.delete(value),
        contains: value => values.has(value),
        toggle(value, force) {
            const add = force === undefined ? !values.has(value) : force;
            if (add) values.add(value); else values.delete(value);
            return add;
        },
    };
}

function element() {
    return {
        innerHTML: '', textContent: '', style: {}, children: [], disabled: false,
        classList: classList(),
        appendChild(child) { this.children.push(child); },
    };
}

function lessonContext(code) {
    const elements = new Map();
    const context = {
        document: {
            readyState: 'loading',
            addEventListener() {},
            querySelectorAll: () => [],
            createElement: () => element(),
            getElementById(id) {
                if (!elements.has(id)) elements.set(id, element());
                return elements.get(id);
            },
        },
        window: { addEventListener() {} },
        localStorage: { getItem: () => null },
    };
    vm.createContext(context);
    vm.runInContext(code, context);
    return { context, elements };
}

// Reading updates must preserve metadata, including duplicate characters' lessons.
const kanjiContext = { window: {} };
vm.runInNewContext(generated.kanji, kanjiContext);
assert.strictEqual(generated.kanji, read('assets/data/kanji_a2_data.js'), 'Reading corrections must be idempotent');
const canonical = JSON.parse(read('data/kanji_extracted.json'));
const occurrences = new Map();
const byChar = new Map();
canonical.forEach(item => {
    if (!byChar.has(item.char)) byChar.set(item.char, []);
    byChar.get(item.char).push(item);
});
const kanji = plain(kanjiContext.kanjiData);
assert.strictEqual(kanji.length, canonical.length);
kanji.forEach(item => {
    const index = occurrences.get(item.char) || 0;
    const source = byChar.get(item.char)?.[index];
    assert(source, `Missing canonical occurrence ${item.char}:${index}`);
    assert.strictEqual(item.lesson, source.lesson, `${item.char}:${index} lesson drift`);
    assert.strictEqual(item.lessonName, source.lessonName, `${item.char}:${index} lesson-name drift`);
    occurrences.set(item.char, index + 1);
});
assert.deepStrictEqual(kanji.filter(item => item.char === '先').map(item => item.lesson), ['L9', 'L18']);
const selected = new Set(Array.from({ length: 18 }, (_, i) => `L${i + 1}`));
assert.strictEqual(kanji.filter(item => selected.has(item.lesson)).length, 144, 'All-lesson filter must retain all 144 entries');
const fixtureContext = {};
vm.runInNewContext(generated.kanjiFixture, fixtureContext);
const fixture = plain(fixtureContext.kanjiData);
assert.deepStrictEqual(fixture.map(item => item.lesson), ['L7', 'L9', 'L16', 'L17', 'L18']);
assert.deepStrictEqual(fixture.map(item => item.on), ['えき', 'せん', 'ほ、ぶ、ふ', 'けつ、けち', 'せん']);
assert.strictEqual(fixture[0].kun, '—');
assert.strictEqual(fixture[1].kun, 'さき、まず');
assert.strictEqual(fixture[0].examples[0].on, 'keep', 'Example fields must remain untouched');

// Execute every rendered 3D handler, also after filtering. No global `v` exists.
let launches = 0;
for (let number = 10; number <= 18; number++) {
    const code = read(`assets/js/lessons/lesson_${number}.js`);
    const { context, elements } = lessonContext(code);
    const vocab = array(code, 'VOCAB_DATA');
    const calls = [];
    let stopped = 0;
    context.openVocab3D = index => calls.push(index);
    context.event = { stopPropagation() { stopped++; } };
    assert.strictEqual(vm.runInContext('typeof v', context), 'undefined');
    for (const category of ['all', ...new Set(vocab.map(item => item.cat))]) {
        calls.length = 0;
        if (number === 10) {
            context.renderFlashcards(category);
        } else {
            vm.runInContext(`activeVocabFilter = ${JSON.stringify(category)}; renderFlashcards();`, context);
        }
        const html = elements.get(number === 10 ? 'flashcardGrid' : 'flashcardsGrid').innerHTML;
        const handlers = [...html.matchAll(/class="fc-3d-stage" onclick="([^"]+)"/g)].map(match => match[1]);
        const expected = vocab.map((item, index) => ({ item, index }))
            .filter(({ item }) => category === 'all' || item.cat === category)
            .map(({ index }) => index);
        assert.strictEqual(handlers.length, expected.length, `L${number}:${category} missing 3D controls`);
        handlers.forEach(handler => vm.runInContext(handler, context));
        assert.deepStrictEqual(calls, expected, `L${number}:${category} must launch original vocabulary indices`);
        launches += handlers.length;
    }
    assert(stopped > 0, `L${number} click must stop propagation`);
}

// Independently reviewed expected labels for every verb, not just each lesson's first.
const labels = {
    past: 'Thể quá khứ ngắn: Vた', experience: 'Trải nghiệm: Vたことがある',
    advice: 'Khuyên không nên: Vないほうがいい', ability: 'Khả năng: Vることができる',
    negative: 'Thể phủ định ngắn: Vない', suggestion: 'Rủ rê: Vましょう', invitation: 'Lời mời: Vませんか',
    request: 'Yêu cầu: Vてください', unfinished: 'Vẫn chưa: まだVていません', sequence: 'Trình tự: Vてから',
    politePast: 'Quá khứ lịch sự: Vました', explanation: 'Giải thích: thể thông thường + んです',
    difficult: 'Khó làm: gốc ます + にくい', prohibition: 'Cấm: Vてはいけない',
    obligation: 'Bắt buộc: Vなければならない', optional: 'Không cần: Vなくてもいい',
    after: 'Sau khi: Vたあとで', place: 'Địa điểm: Vた + ところ', until: 'Mốc kết thúc: Vるまで',
    nominal: 'Điều đã xảy ra: Vた + こと',
};
const repeat = (value, count = 5) => Array(count).fill(value);
const expectedLabels = [
    repeat('past'), repeat('past', 6), repeat('experience'), repeat('past'),
    [...repeat('advice', 4), 'past'], repeat('ability'),
    ['negative', 'suggestion', 'invitation', 'past', 'request'],
    [...repeat('unfinished', 3), 'sequence', 'politePast'], repeat('past'),
    ['request', ...repeat('past', 4)], ['explanation', 'explanation', 'past', 'unfinished', 'past'],
    [...repeat('past', 4), 'difficult'], repeat('past'), repeat('past'),
    ['prohibition', 'obligation', 'optional', 'past', 'past'], repeat('past'),
    ['after', 'place', 'until', 'past', 'past'], ['past', 'past', 'nominal', 'past', 'past'],
];
let verbsChecked = 0;
let unchangedSignatures = 0;
let newQuizSignatures = 0;
for (const lesson of generated.lessons) {
    const { number, code, html } = lesson;
    const verbs = array(code, 'VERB_DATA');
    const quiz = array(code, 'QUIZ_DATA');
    const file = `assets/js/lessons/lesson_a2_2_${String(number).padStart(2, '0')}.js`;
    const shippedVerbs = array(read(file), 'VERB_DATA');
    const stripLabel = ({ form2Label, ...verb }) => verb;
    assert.deepStrictEqual(verbs.map(stripLabel), shippedVerbs.map(stripLabel), `L${number} authored verb values must not change`);
    assert.deepStrictEqual(verbs.map(verb => verb.form2Label), expectedLabels[number - 1].map(key => labels[key]));
    assert(html.includes(`id="morphForm2Label">${verbs[0].form2Label}</span>`), `L${number} initial label must match its first verb`);
    const { context, elements } = lessonContext(code);
    for (let index = verbs.length - 1; index >= 0; index--) {
        context.selectVerb(index);
        assert.strictEqual(elements.get('morphForm2Label').textContent, verbs[index].form2Label);
        assert.strictEqual(elements.get('morphTeKi').textContent, verbs[index].form2);
        assert.strictEqual(elements.get('morphTeIki').textContent, verbs[index].form1);
        assert.strictEqual(elements.get('morphMashou').textContent, verbs[index].form3);
        verbsChecked++;
    }
    context.initQuiz();
    const cards = elements.get('quizContainer').children;
    quiz.forEach((question, index) => {
        const handlers = [...cards[index].innerHTML.matchAll(/onclick="([^"]+)"/g)].map(match => match[1].replace(/\s+/g, ''));
        if (question.reviewVersion === 'a22-practice20-v1') {
            assert(number >= 1 && number <= 4);
            assert(handlers.every(handler => handler.includes("'a22-practice20-v1'")));
            const buttons = question.options.map(() => element());
            buttons.forEach(button => { button.parentElement = { querySelectorAll: () => buttons }; });
            context.checkQuizAnswer(buttons[question.correct], index, question.correct, 'a22-reviewed-v2');
            assert(buttons.every(button => !button.disabled), 'Legacy signature must not grade new quiz items');
            context.checkQuizAnswer(buttons[question.correct], index, question.correct, question.reviewVersion);
            assert(buttons.every(button => button.disabled));
            assert(buttons[question.correct].classList.contains('correct'));
            newQuizSignatures++;
        } else if (number === 14 && question.id === 7) {
            assert.strictEqual(question.reviewVersion, 'a22-l14-q7-past-v3');
            assert(question.q.includes('Chọn dạng quá khứ'));
            const completed = question.q.replace('[____]', question.options[question.correct]);
            assert(completed.includes('すばらしかった です。'));
            assert(!completed.includes('すばらしかった でした'));
            assert(handlers.every(handler => handler.includes("'a22-l14-q7-past-v3'")));
            const oldHandler = `checkQuizAnswer(this,${index},${question.correct},'a22-reviewed-v2')`;
            assert(!handlers.includes(oldHandler), 'Old L14Q7 checkpoint signature must not match a new button');
            const buttons = question.options.map(() => element());
            buttons.forEach(button => { button.parentElement = { querySelectorAll: () => buttons }; });
            context.checkQuizAnswer(buttons[question.correct], index, question.correct, 'a22-reviewed-v2');
            assert(buttons.every(button => !button.disabled), 'Stale direct calls must not grade corrected Q7');
            context.checkQuizAnswer(buttons[question.correct], index, question.correct, question.reviewVersion);
            assert(buttons.every(button => button.disabled));
            assert(buttons[question.correct].classList.contains('correct'));
            context.checkQuizAnswer(buttons[question.correct], index, question.correct, question.reviewVersion);
            assert.strictEqual(elements.get(`explain-${index}`).style.display, 'block');
        } else {
            question.options.forEach((_, optionIndex) => {
                assert.strictEqual(handlers[optionIndex], `checkQuizAnswer(this,${index},${optionIndex},'a22-reviewed-v2')`);
            });
            const buttons = question.options.map(() => element());
            buttons.forEach(button => { button.parentElement = { querySelectorAll: () => buttons }; });
            context.checkQuizAnswer(buttons[question.correct], index, question.correct, 'a22-reviewed-v2');
            assert(buttons[question.correct].classList.contains('correct'), `L${number} Q${question.id} valid old revision must still grade`);
            unchangedSignatures++;
        }
    });
    if (process.argv.includes('--check-generated')) {
        assert.strictEqual(read(file), code, `${file} is stale; run the main build`);
        assert.strictEqual(read(`lessons/Marugoto_A2_2_Lesson_${number}.html`), html, `L${number} HTML is stale`);
    }
}
assert.strictEqual(unchangedSignatures, 269);
assert.strictEqual(newQuizSignatures, 20);
assert.strictEqual(verbsChecked, 91);
console.log(`✅ Lesson fixes: 144 Kanji lesson assignments, ${launches} rendered 3D launches, ${verbsChecked} verb/label selections, corrected Q7, ${unchangedSignatures} preserved and ${newQuizSignatures} new quiz signatures.`);
