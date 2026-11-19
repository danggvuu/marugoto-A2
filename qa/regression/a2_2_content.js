/* Content and deployment dependencies for all 18 Marugoto A2-2 lessons. */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const root = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const source = JSON.parse(read('data/kanji_vocab_a2_2.json'));
const context = { window: {} };
vm.runInNewContext(read('assets/data/kanji_a2_data.js'), context);

let totalVocab = 0;
let totalQuiz = 0;
let totalKanji = 0;

for (let lesson = 1; lesson <= 18; lesson++) {
    const lessonStr = String(lesson).padStart(2, '0');
    const code = read(`assets/js/lessons/lesson_a2_2_${lessonStr}.js`);
    const array = name => JSON.parse(code.match(new RegExp(`const ${name} = (\\[[\\s\\S]*?\\]);`))[1]);
    const vocab = array('VOCAB_DATA');
    const quiz = array('QUIZ_DATA');

    assert(vocab.length >= 17 && vocab.length <= 25, `Lesson ${lesson} vocab count ${vocab.length} out of range`);
    assert.strictEqual(quiz.length, 15, `Lesson ${lesson} quiz must have exactly 15 questions`);
    assert(vocab.every(item => item.jp && item.kana && item.romaji && item.vi), `Missing fields in Lesson ${lesson} vocab`);
    assert(vocab.every(item => !/[A-Za-z]/.test(item.kana)), `Kana must not include template placeholders in Lesson ${lesson}`);

    const counts = [0, 0, 0, 0];
    quiz.forEach((q, qIdx) => {
        assert.strictEqual(new Set(q.options).size, 4, `Lesson ${lesson} question ${qIdx + 1} options must be unique`);
        assert(q.explain && Number.isInteger(q.correct) && q.correct >= 0 && q.correct < 4, `Invalid quiz question in Lesson ${lesson}`);
        counts[q.correct]++;
        assert(!q.q.includes('自分ので'));
    });
    assert(Math.max(...counts) - Math.min(...counts) <= 1, `Unbalanced answer positions in Lesson ${lesson}: ${JSON.stringify(counts)}`);

    if (lesson === 1) {
        const q = quiz[0];
        assert.strictEqual(q.q.replace('[____]', q.options[q.correct]), '「ハノイ」というのは、「川の内側」と いう意味です。');
    }

    const html = read(`lessons/Marugoto_A2_2_Lesson_${lesson}.html`);
    assert(html.includes('lesson-a2-2.css'), `Missing CSS link in Lesson ${lesson} HTML`);
    assert(html.includes('class="flashcard-grid"'), `Missing flashcard grid in Lesson ${lesson} HTML`);

    const rows = context.VOCAB_121_DATA.filter(item => item.lesson === `A2-2 L${lesson}`);
    assert.strictEqual(rows.length, source[`lesson_${lesson}`].length, `Kanji vocab count mismatch in Lesson ${lesson}`);
    rows.forEach((row, i) => {
        const item = source[`lesson_${lesson}`][i];
        assert.strictEqual(row.kanji, item.word);
        assert.strictEqual(row.kana, item.kana);
        assert.strictEqual(row.vi, item.mean);
    });

    totalVocab += vocab.length;
    totalQuiz += quiz.length;
    totalKanji += rows.length;
}

console.log(`✅ All 18 A2-2 lessons validated successfully: ${totalVocab} vocabulary cards, ${totalQuiz} balanced quiz questions (15 per lesson), and ${totalKanji} Kanji vocabulary entries!`);
