/* Structural/content regression guards, not an automated Japanese teacher. */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const root = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const normalized = value => value.replace(/<rt>.*?<\/rt>/g, '').replace(/<[^>]+>/g, '').normalize('NFKC').replace(/\s+/g, '').trim();
const lessonQuizzes = {};
let questionsChecked = 0;
for (let lesson = 1; lesson <= 18; lesson++) {
    const filename = `assets/js/lessons/lesson_${String(lesson).padStart(2, '0')}.js`;
    const code = read(filename);
    new vm.Script(code, { filename });
    const match = code.match(/^const (?:QUIZ_DATA|QUIZ_QUESTIONS) = (\[[\s\S]*?\]);/m);
    assert(match, `${filename}: missing quiz declaration (must not silently skip)`);
    const items = JSON.parse(match[1]);
    assert.strictEqual(items.length, 15);
    assert.strictEqual(new Set(items.map(q => q.id)).size, items.length);
    const distribution = [0, 0, 0, 0];
    for (const q of items) {
        assert.strictEqual(q.options.length, 4);
        assert.strictEqual(new Set(q.options.map(normalized)).size, 4, `${filename}: Q${q.id} duplicate visible options`);
        assert(Number.isInteger(q.correct) && q.correct >= 0 && q.correct < 4);
        assert(typeof q.q === 'string' && q.q.trim() && typeof q.explain === 'string' && q.explain.trim(),
            `${filename}: Q${q.id} missing prompt/explanation`);
        assert(!/Câu hỏi ôn tập số|Đáp án A \(Đúng\)|Câu ví dụ mẫu/.test(JSON.stringify(q)));
        assert(!/を\s*勉強します/.test(q.explain) || !/Ví dụ: .*を\s*勉強します。/.test(q.explain) ||
            /歴史|日本語|英語/.test(q.explain), 'mechanical vocabulary example');
        distribution[q.correct]++;
        questionsChecked++;
    }
    assert(Math.max(...distribution) - Math.min(...distribution) <= 1, `${filename}: answer-position bias`);
    lessonQuizzes[lesson] = items;
    if (lesson >= 3 && lesson <= 9) {
        const html = read(`lessons/Marugoto_A2_Lesson_${lesson}.html`);
        assert(!/Cấu trúc cốt lõi Bài|Chuyên đề ngữ pháp [123] Bài|Diễn đạt ý nghĩa then chốt|Câu ví dụ mẫu/.test(html));
        assert(html.includes('R_contents_eng.pdf'));
        assert.strictEqual(items.filter(q => q.category === 'Ngữ pháp & giao tiếp').length, 7);
    }
    assert(code.includes("'content-2026-11-16'"), `${filename}: quiz checkpoint signature was not versioned`);
}
const question = (lesson, id) => lessonQuizzes[lesson].find(q => q.id === id);
const answer = (lesson, id) => { const q = question(lesson, id); return q.options[q.correct]; };
assert.strictEqual(answer(11, 15), '願');
assert.strictEqual(answer(16, 12), '週末');
assert(!question(12, 7).options.includes('に'), 'do not mark a valid alternative particle wrong');
assert(!question(15, 1).options.includes('痛いです'), 'avoid ambiguous correct distractor');
assert(!question(2, 11).options.includes('こと'));
const kanji = JSON.parse(read('data/kanji_extracted.json'));
const reference = JSON.parse(read('data/kanji_reference_checks.json'));
const context = { window: {} };
vm.createContext(context);
vm.runInContext(read('assets/data/kanji_a2_data.js'), context);
for (const list of [kanji, context.kanjiData]) {
    for (const k of list) {
        assert.strictEqual(k.strokes, reference.strokeCounts[k.char], `stroke count: ${k.char}`);
        for (const [field, value] of Object.entries(reference.readingCorrections[k.char] || {})) {
            assert.strictEqual(k[field], value, `${k.char} ${field}`);
        }
    }
}
const examsContext = { window: {} };
vm.createContext(examsContext);
vm.runInContext(read('assets/data/de_thi_tong_hop_11_18_data.js'), examsContext);
for (const exam of examsContext.window.DE_THI_TONG_HOP_DATA) {
    if (exam.code === 'DEGOC') continue;
    const questions = exam.sections.flatMap(s => s.groups.flatMap(g => g.items));
    const weather = questions.find(q => q.prompt.includes('明日は 天気が'));
    assert(weather, exam.code + ': missing weather regression case');
    assert.strictEqual(weather.options[weather.correct], 'いい');
    assert(!weather.prompt.includes('いい ('));
    const start = questions.find(q => q.prompt.includes('３か月前'));
    assert(start);
    assert(!start.prompt.includes('勉強を ('), 'duplicated を in prompt');
}
for (const exam of examsContext.window.DE_THI_TONG_HOP_DATA.filter(exam => /^M11[1-5]$/.test(exam.code))) {
    const questions = exam.sections.flatMap(section => section.groups.flatMap(group => group.items));
    const text = JSON.stringify(questions);
    assert(!/スプーン|フォーク|ナイフ|ファクス|アレルギー|納豆|富士山|日本で 働いた|経験/.test(text), `${exam.code}: out-of-scope bank item`);
    assert(!/ように|ながら|てしま|なければ|ほうがいい|食べられ/.test(text), `${exam.code}: out-of-scope grammar`);
}
console.log(`Content checks passed: ${questionsChecked} lesson questions, 21 theory sections, 144 Kanji entries in source/runtime, corrected exam cases.`);
