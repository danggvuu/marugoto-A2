/* Content and deployment dependencies for all 18 Marugoto A2-2 lessons. */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const root = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const source = JSON.parse(read('data/kanji_vocab_a2_2.json'));
const officialKanji = JSON.parse(read('data/kanji_vocab_a2_2_official.json'));
const context = { window: {} };
vm.runInNewContext(read('assets/data/kanji_a2_data.js'), context);

let totalVocab = 0;
let totalQuiz = 0;
let totalKanji = 0;

const curriculumChecks = {
    3: ['ので', 'のは', 'なら', 'ずつ'],
    4: ['てはいけません', 'てから', 'ないで', 'Vる ＋ と'],
    6: ['見られます', 'し、'],
    9: ['会えて、よかったです', 'しか', 'だけ'],
    10: ['楽しめるように', '願い事を書いたり', 'ように願います'],
    11: ['動かなくなりました', '動かなくなってしまいました', '買い物できます', '届くまで'],
    12: ['重すぎます', '使いやすいです', 'どちらが安いですか'],
    13: ['いつ来ても', '二人で', '天皇によって'],
    14: ['だそうです', 'ために', 'おいてあります'],
    15: ['ついたまま', '使うようにしています', 'へらすのにいい'],
    16: ['着られなくなりました', '着られなくなったら', 'バッグにしました'],
    17: ['するそうです', 'なってから', 'なくなるまで', 'かもしれません'],
    18: ['しかられました', '起きるようになりました', '見なくなりました', '食べられるようになりました'],
};

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

    const officialRows = officialKanji[`lesson_${lesson}`];
    assert(officialRows, `Missing official Kanji list for Lesson ${lesson}`);
    const officialWords = new Set(officialRows.map(item => item.word));
    assert.deepStrictEqual(
        officialRows.map(item => [item.word, item.kana]),
        source[`lesson_${lesson}`].map(item => [item.word, item.kana]),
        `Generated Kanji source differs from official list in Lesson ${lesson}`
    );
    officialRows.forEach(item => {
        assert(html.includes(item.word), `Official Kanji word ${item.word} missing from Lesson ${lesson} HTML`);
        assert(html.includes(item.kana), `Official Kanji reading ${item.kana} missing from Lesson ${lesson} HTML`);
    });

    const rows = context.VOCAB_121_DATA.filter(item => item.lesson === `A2-2 L${lesson}`);
    assert.strictEqual(rows.length, source[`lesson_${lesson}`].length, `Kanji vocab count mismatch in Lesson ${lesson}`);
    rows.forEach((row, i) => {
        const item = source[`lesson_${lesson}`][i];
        assert.strictEqual(row.kanji, item.word);
        assert.strictEqual(row.kana, item.kana);
        assert.strictEqual(row.vi, item.mean);
    });

    const expectedGrammar = curriculumChecks[lesson] || [];
    expectedGrammar.forEach(pattern => {
        assert(html.includes(pattern), `Official grammar item "${pattern}" missing from Lesson ${lesson}`);
    });
    quiz.filter(q => q.category === 'Chữ Hán').forEach(q => {
        assert(q.scopeKanji && officialWords.has(q.scopeKanji), `Lesson ${lesson} Kanji quiz target is outside its official list: ${q.scopeKanji}`);
        const target = officialRows.find(item => item.word === q.scopeKanji);
        assert(target, `Missing official target ${q.scopeKanji} in Lesson ${lesson}`);
        assert([target.kana, target.mean].includes(q.options[q.correct]),
            `Lesson ${lesson} Kanji answer doesn't match ${q.scopeKanji}`);
    });
    quiz.filter(q => q.category === 'Ngữ pháp').forEach(q => {
        assert.strictEqual(q.grammarScope, 'official', `Lesson ${lesson} grammar quiz isn't mapped to a confirmed pattern: ${q.q}`);
    });
    const grammarPrompts = quiz.filter(q => q.category === 'Ngữ pháp').map(q => q.q.replace(/\[[^\]]+\]/g, ''));
    assert.strictEqual(new Set(grammarPrompts).size, grammarPrompts.length, `Duplicate grammar quiz prompt in Lesson ${lesson}`);
    if (lesson === 6) {
        const answer = quiz.find(q => q.q.includes('沖縄旅行はどうでしたか'));
        assert.strictEqual(answer.options[answer.correct], 'きれいでした', 'Lesson 6 must use the correct polite past form');
    }
    if (lesson === 13) {
        assert(!quiz.some(q => q.q.includes('京都寺')), 'Lesson 13 contains an invalid place name');
    }

    totalVocab += vocab.length;
    totalQuiz += quiz.length;
    totalKanji += rows.length;
}

assert.strictEqual(totalKanji, 170, 'Official A2-2 Kanji word list should contain 170 entries');
console.log(`✅ A2-2 curriculum checked: ${totalVocab} vocabulary cards, ${totalQuiz} quiz questions and ${totalKanji} official Kanji words across all 18 lessons.`);
