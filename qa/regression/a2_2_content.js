/* Content and deployment dependencies for the two A2-2 lessons. */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const root = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const source = JSON.parse(read('data/kanji_vocab_a2_2.json'));
const context = { window: {} };
vm.runInNewContext(read('assets/data/kanji_a2_data.js'), context);
for (const lesson of [1, 2]) {
    const code = read(`assets/js/lessons/lesson_a2_2_0${lesson}.js`);
    const array = name => JSON.parse(code.match(new RegExp(`const ${name} = (\\[[\\s\\S]*?\\]);`))[1]);
    const vocab = array('VOCAB_DATA');
    const quiz = array('QUIZ_DATA');
    assert.strictEqual(vocab.length, lesson === 1 ? 20 : 17);
    assert.strictEqual(quiz.length, 15);
    assert(vocab.every(item => item.jp && item.kana && item.romaji && item.vi));
    assert(vocab.every(item => !/[A-Za-z]/.test(item.kana)), 'Kana must not include template placeholders');
    const counts = [0, 0, 0, 0];
    quiz.forEach(q => {
        assert.strictEqual(new Set(q.options).size, 4);
        assert(q.explain && Number.isInteger(q.correct) && q.correct >= 0 && q.correct < 4);
        counts[q.correct]++;
        assert(!q.q.includes('自分ので'));
    });
    assert(Math.max(...counts) - Math.min(...counts) <= 1, 'Unbalanced answer positions');
    if (lesson === 1) {
        const q = quiz[0];
        assert.strictEqual(q.q.replace('[____]', q.options[q.correct]), '「ハノイ」というのは、「川の内側」と いう意味です。');
    }
    const html = read(`lessons/Marugoto_A2_2_Lesson_${lesson}.html`);
    assert(html.includes('lesson-a2-2.css'));
    assert(html.includes('class="flashcard-grid"'));
    const rows = context.VOCAB_121_DATA.filter(item => item.lesson === `A2-2 L${lesson}`);
    assert.strictEqual(rows.length, source[`lesson_${lesson}`].length);
    rows.forEach((row, i) => {
        const item = source[`lesson_${lesson}`][i];
        assert.strictEqual(row.kanji, item.word);
        assert.strictEqual(row.kana, item.kana);
        assert.strictEqual(row.vi, item.mean);
    });
}
console.log('A2-2 content validated: 37 words, 30 balanced quiz items, 31 Kanji entries.');
