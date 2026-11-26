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
    4: ['てはいけません', 'てから', 'ないで', 'V thể từ điển ＋ と'],
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

    assert(vocab.length >= 16 && vocab.length <= 50, `Lesson ${lesson} vocab count ${vocab.length} out of range`);
    assert.strictEqual(quiz.length, lesson <= 4 ? 20 : 15, `Lesson ${lesson} quiz count mismatch`);
    if (lesson <= 4) {
        assert.deepStrictEqual(quiz.slice(0, 15).map(q => q.id), Array.from({ length: 15 }, (_, i) => i + 1),
            `Lesson ${lesson} must retain its original quiz order`);
        assert.deepStrictEqual(quiz.slice(15).map(q => [q.id, q.reviewVersion]),
            Array.from({ length: 5 }, (_, i) => [i + 16, 'a22-practice20-v1']),
            `Lesson ${lesson} must append the five versioned practice questions`);
    }
    assert(vocab.every(item => item.jp && item.kana && item.romaji && item.vi), `Missing fields in Lesson ${lesson} vocab`);
    assert(vocab.every(item => !/[A-Za-z]/.test(item.kana)), `Kana must not include template placeholders in Lesson ${lesson}`);
    if (lesson === 4) {
        const grill = array('VERB_DATA').find(item => item.masu === 'やきます');
        assert.strictEqual(grill?.form1, 'やかないで (đừng nướng)', 'Lesson 4 negative verb gloss must match やかないで');
    }

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
    if (lesson <= 4) {
        const sentences = array('SENTENCE_PRACTICE_DATA');
        const kanjiPractice = array('KANJI_PRACTICE_DATA');
        assert.strictEqual(sentences.length, 40, `Lesson ${lesson} must have exactly 40 typing prompts`);
        assert.deepStrictEqual(sentences.map(item => item.id), Array.from({ length: 40 }, (_, i) => i + 1));
        assert(sentences.every(item => item.vi && item.jp && item.requireKanji === true));
        assert(kanjiPractice.every(item => item.id && item.word && item.mean));
        const officialPractice = kanjiPractice.filter(item => item.id.startsWith('official-'));
        assert.deepStrictEqual(officialPractice.map(item => [item.word, item.mean]),
            officialKanji[`lesson_${lesson}`].map(item => [item.word, item.mean]),
            `Lesson ${lesson} Kanji drill must contain its official vocabulary without modification`);
        if (lesson === 1 || lesson === 2) {
            const expectedSupplement = lesson === 1
                ? ['紹介', '一番目', '住所', '近所', '近い', '一番', '最近', '部屋']
                : ['姉妹', '水族館', '成長', '兄弟', '歌手'];
            assert.deepStrictEqual(kanjiPractice.filter(item => item.id.startsWith('supplement-'))
                .map(item => item.word).sort(), expectedSupplement.sort());
        }
        assert(html.includes('typing-sentence-practice.js?v=3'));
        assert(html.includes('Luyện Gõ 40 Câu'));
    }

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

assert.strictEqual(totalVocab, 439, 'Official A2-2 vocabulary should contain 439 entries');
assert.strictEqual(totalQuiz, 290, 'A2-2 should have 290 quiz items after the four lesson expansions');
assert.strictEqual(totalKanji, 181, 'Official A2-2 Kanji word list should contain 181 entries');

const reviewContext = { window: {} };
vm.runInNewContext(read('assets/data/mini_a2_2_1_4_data.js'), reviewContext);
const reviewData = JSON.parse(JSON.stringify(reviewContext.window.MINI_A2_2_1_4_DATA));
const reviewHtml = read('tests/On_Tap_Mini_Test_A2_2_1_4.html');
const reviewKanjiSource = [1, 2, 3, 4].flatMap(n => source[`lesson_${n}`]);
const supplementWords = [
    '紹介', '一番目', '住所', '姉妹', '水族館', '成長', '近所', '兄弟', '近い', '一番', '最近', '部屋', '歌手'
];
const expectedGrammar = [
    'S は N という意味です', 'N1 という N2: tên gọi', 'Thể thông thường + danh từ',
    'Miêu tả tính chất: A は B が', 'N đang làm V: Vている + N', 'Trông có vẻ: ～そうです／～そうな N', 'Làm V một cách ADJ: ～く／～に／～そうに',
    'Vì: ～ので', 'Nhấn mạnh danh từ: ～のは N です', 'Nếu là N thì: Nなら', 'Mỗi thứ / mỗi lượt: ～ずつ',
    'Không được làm V: ～ては／ではいけません', 'Làm V1 xong rồi làm V2: ～てから', 'Trạng thái / cách thức: Vて／Vないで V2', 'Cứ hễ làm V thì: ～と'
];
const expectedGrammarCounts = [3, 4, 4, 4];
expectedGrammarCounts.forEach((count, index) => {
    const lessonHtml = read(`lessons/Marugoto_A2_2_Lesson_${index + 1}.html`);
    assert.strictEqual(
        (lessonHtml.match(/<section class="content-section" id="sec-grammar\d+">/g) || []).length,
        count,
        `Lesson ${index + 1} must render its canonical grammar section count`
    );
});
assert.strictEqual(reviewData.rawKanji.length, 62, 'Review Kanji cards must total 62');
assert.deepStrictEqual(
    reviewData.rawKanji.slice(0, 49).map(item => [item.word, item.kana]),
    reviewKanjiSource.map(item => [item.word, item.kana]),
    'The original 49 review Kanji must retain their order and content'
);
assert.deepStrictEqual(
    reviewData.rawKanji.slice(49).map(item => item.word),
    supplementWords,
    'The 13 worksheet terms must be appended as supplemental cards'
);
reviewData.rawKanji.slice(49).forEach(item => {
    assert.strictEqual(item.lesson, 'SUPPLEMENT');
    assert(item.kana && item.meaning && item.hv && item.strokes > 0 && item.formula && item.mnemonic,
        `Supplemental Kanji metadata is incomplete: ${item.word}`);
});
assert.strictEqual((reviewHtml.match(/class="content-section review-grammar-section"/g) || []).length, 15,
    'Review theory must render all 15 canonical grammar sections');
expectedGrammar.forEach((title, i) => {
    assert(reviewHtml.includes(title), `Review theory is missing grammar section ${i + 1}: ${title}`);
});
assert(reviewHtml.includes('Câu luyện dịch • Đáp án tham khảo'));
assert(reviewHtml.includes("filterKanji('SUPPLEMENT', this)"));
assert(reviewHtml.includes('Tất cả (62 mục)'));
assert(reviewHtml.includes('Bổ sung từ phiếu (13 mục)'));
assert(reviewHtml.includes('49 mục đầu giữ nguyên thứ tự'));
assert(!reviewHtml.includes('__KANJI_COUNT__') && !reviewHtml.includes('__SUPPLEMENT_COUNT__'));
assert.strictEqual((reviewHtml.match(/class="contraction-table"/g) || []).length, 1);
assert.strictEqual((reviewHtml.match(/<tr><td>/g) || []).length, 10, 'Review contraction table must have 10 verb rows');
const lesson4Html = read('lessons/Marugoto_A2_2_Lesson_4.html');
assert(lesson4Html.includes('class="contraction-table"'), 'Lesson 4 must render the canonical contraction data');
assert.strictEqual((lesson4Html.match(/<tr><td>/g) || []).length, 10, 'Lesson 4 contraction table must have 10 rows');
assert(reviewHtml.includes('mini-test-a2-2-1-4.js?v=2'));
assert(reviewHtml.includes('mini_a2_2_1_4_data.js?v=2'));
assert.strictEqual(reviewData.part1Data.length, 10);
assert.strictEqual(reviewData.part2Data.length, 5);
assert.strictEqual(reviewData.part3Data.length, 5);
assert.strictEqual(reviewData.part4Data.length, 4);
assert.strictEqual(reviewData.part5Data.reduce((count, passage) => count + passage.questions.length, 0), 4);
assert.strictEqual(reviewData.part6Data.length, 4);
assert.strictEqual(reviewData.part1Data[4].options[2], '着ます', 'Ambiguous completed-clothing distractor must be removed without moving its slot');
assert(reviewData.part1Data[7].q.includes('現在・肯定の普通形'));
assert(reviewData.part1Data[9].q.includes('V-ては いけません'));
assert(reviewData.part3Data.find(item => item.id === 19).sentence.includes('現在・肯定の普通形'));
assert.strictEqual(reviewData.part6Data.find(item => item.id === 30).vi, 'Đứa bé đang ăn bánh kem một cách ngon lành.');

const curriculumSource = read('scripts/a2_2/official_curriculum.py');
for (const name of ['QUIZ_OVERRIDES', 'GRAMMAR_OVERRIDE_IDS']) {
    const match = curriculumSource.match(new RegExp(`${name}\\s*=\\s*\\{([\\s\\S]*?)\\n\\}`));
    assert(match, `Missing ${name} declaration`);
    const keys = [...match[1].matchAll(/\((\d+),\s*(\d+)\)\s*(?=[:,])/g)]
        .map(([, lesson, question]) => `${lesson}:${question}`);
    assert.strictEqual(new Set(keys).size, keys.length, `${name} contains duplicate lesson/question keys`);
}

console.log(`✅ A2-2 curriculum checked: ${totalVocab} vocabulary cards, ${totalQuiz} quiz questions and ${totalKanji} official Kanji words across all 18 lessons.`);
