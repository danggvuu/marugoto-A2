/**
 * Comprehensive Automated Regression Test Suite for Marugoto Japanese
 * Verifies fixes for R1 through R11 from docs/CODE_REVIEW.md
 */

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const vmContent = require('vm');

const ROOT = path.resolve(__dirname, '../..');
let passed = 0;
let failed = 0;

function test(name, fn) {
    try {
        fn();
        console.log(`  ✅ PASS: ${name}`);
        passed++;
    } catch (err) {
        console.error(`  ❌ FAIL: ${name}`);
        console.error(`     ${err.message}`);
        failed++;
    }
}

console.log('=== RUNNING MARUGOTO REGRESSION TESTS (R1 - R11) ===\n');

console.log('--- Content integrity ---');
const lessonFiles = fs.readdirSync(path.join(ROOT, 'assets/js/lessons'))
    .filter(name => /^lesson_(?:\d+|a2_2_0[12])\.js$/.test(name));
for (const lessonFile of lessonFiles) {
    const content = fs.readFileSync(path.join(ROOT, 'assets/js/lessons', lessonFile), 'utf8');
    test(`${lessonFile}: no placeholder quiz content`, () => {
        assert.ok(!content.includes('Câu hỏi ôn tập số'), 'placeholder quiz prompt remains');
        assert.ok(!content.includes('Đáp án A (Đúng)'), 'placeholder answer remains');
    });
    test(`${lessonFile}: quiz answer choices are unique`, () => {
        new vmContent.Script(content, { filename: lessonFile });
        const match = content.match(/const (?:QUIZ_DATA|QUIZ_QUESTIONS) = (\[[\s\S]*?\]);/);
        assert.ok(match, 'quiz declaration missing or malformed');
        const quiz = JSON.parse(match[1]);
        quiz.forEach((question, index) => {
            assert.strictEqual(new Set(question.options).size, question.options.length,
                `duplicate options in question ${index + 1}`);
            assert.ok(Number.isInteger(question.correct) && question.correct >= 0 &&
                question.correct < question.options.length, `invalid answer index in question ${index + 1}`);
        });
    });
}

// -----------------------------------------------------------------------------
// R10: Unicode Normalization (NFKC, NFD, Half-width Katakana)
// -----------------------------------------------------------------------------
console.log('--- R10: Unicode Normalization ---');
const Grader = require(path.join(ROOT, 'assets/js/jp-typing-grader.js'));

test('R10.1: NFD decomposed Hiragana is recognized', () => {
    const nfc = 'がっこうにいきます';
    const nfd = nfc.normalize('NFD');
    assert.notStrictEqual(nfc, nfd, 'NFD must be different bytes from NFC');
    const res = Grader.grade(nfd, { hira: nfc }, 'sentence', {});
    assert.strictEqual(res.ok, true, 'Decomposed NFD input must grade as OK');
});

test('R10.2: Half-width Katakana is recognized', () => {
    const halfWidth = 'ｶﾞｯｺｳﾆｲｷﾏｽ';
    const target = 'がっこうにいきます';
    const res = Grader.grade(halfWidth, { hira: target }, 'sentence', {});
    assert.strictEqual(res.ok, true, 'Half-width Katakana must grade as OK');
});

// -----------------------------------------------------------------------------
// R1: Translation Grading Rejects Incomplete/Punctuation Inputs
// -----------------------------------------------------------------------------
console.log('\n--- R1: Translation Grading Accuracy ---');
const DichCauCode = fs.readFileSync(path.join(ROOT, 'assets/js/pages/dich_cau_1_10.js'), 'utf8');
const dcContext = {};
const dcFn = new Function('context', `
    let window = { addEventListener: () => {} };
    let document = { querySelectorAll: () => [], getElementById: () => null, addEventListener: () => {} };
    ${DichCauCode}
    context.isTextFuzzyMatch = isTextFuzzyMatch;
    context.evaluateAnswer = evaluateAnswer;
    context.normalizeJp = normalizeJp;
`);
dcFn(dcContext);

test('R1.1: dich_cau_1_10 rejects single particle "は"', () => {
    const q = {
        id: 1,
        type: 'sentence',
        acceptable: ['日本語で話しましょう', 'にほんごではなしましょう'],
        keywords: ['日本語', '話しましょう'],
        keywordsHira: ['にほんご', 'はなしましょう']
    };
    const score = dcContext.evaluateAnswer(q, { text: 'は' });
    assert.strictEqual(score, 0, `Expected 0% for "は", got ${score}%`);
});

test('R1.2: dich_cau_1_10 rejects punctuation "。"', () => {
    const q = {
        id: 1,
        type: 'sentence',
        acceptable: ['日本語で話しましょう', 'にほんごではなしましょう'],
        keywords: ['日本語', '話しましょう']
    };
    const score = dcContext.evaluateAnswer(q, { text: '。' });
    assert.strictEqual(score, 0, `Expected 0% for "。", got ${score}%`);
});

test('R1.3: dich_cau_1_10 accepts full correct sentence', () => {
    const q = {
        id: 1,
        type: 'sentence',
        acceptable: ['日本語で話しましょう', 'にほんごではなしましょう'],
        keywords: ['日本語', '話しましょう']
    };
    const score = dcContext.evaluateAnswer(q, { text: 'にほんごではなしましょう。' });
    assert.strictEqual(score, 100, `Expected 100% for full sentence, got ${score}%`);
});

const MidtermCode = fs.readFileSync(path.join(ROOT, 'assets/js/pages/de_thi_midterm_a2_1.js'), 'utf8');
const mtContext = {};
const mtFn = new Function('context', `
    let window = { addEventListener: () => {}, location: { hash: '' } };
    let document = { querySelectorAll: () => [], getElementById: () => null, addEventListener: () => {} };
    ${MidtermCode}
    context.evaluateTranslation = evaluateTranslation;
    context.EXAMS_DATA = EXAMS_DATA;
`);
mtFn(mtContext);

test('R1.4: de_thi_midterm_a2_1 rejects punctuation "。"', () => {
    const m101 = mtContext.EXAMS_DATA.find(e => e.code === 'M101');
    const sec3 = m101.sections.find(s => s.id === 'sec3_grammar');
    const group3 = sec3.groups.find(g => g.items && g.items.some(x => x.id === 31));
    const item = group3.items.find(x => x.id === 31);
    const isOk = mtContext.evaluateTranslation(item, '。');
    assert.strictEqual(isOk, false, 'Expected false for punctuation "。" in midterm');
});

test('R1.5: de_thi_midterm_a2_1 accepts correct answer', () => {
    const m101 = mtContext.EXAMS_DATA.find(e => e.code === 'M101');
    const sec3 = m101.sections.find(s => s.id === 'sec3_grammar');
    const group3 = sec3.groups.find(g => g.items && g.items.some(x => x.id === 31));
    const item = group3.items.find(x => x.id === 31);
    const isOk = mtContext.evaluateTranslation(item, item.reference);
    assert.strictEqual(isOk, true, 'Expected true for reference answer in midterm');
});

// -----------------------------------------------------------------------------
// R2: Verb Lab Conjugation Accuracy
// -----------------------------------------------------------------------------
console.log('\n--- R2: Verb Conjugation Accuracy (the_ta.js) ---');
const TheTaCode = fs.readFileSync(path.join(ROOT, 'assets/js/pages/the_ta.js'), 'utf8');
const taContext = {};
const taFn = new Function('context', `
    let window = { addEventListener: () => {} };
    let document = { querySelectorAll: () => [], getElementById: () => null, addEventListener: () => {} };
    ${TheTaCode}
    context.transformJapaneseVerb = transformJapaneseVerb;
    context.userVerbAnswers = userVerbAnswers;
    context.saveCurrentInputs = saveCurrentInputs;
`);
taFn(taContext);

test('R2.1: かう conjugates to かいました / かった (Group 1)', () => {
    const res = taContext.transformJapaneseVerb('かう');
    assert.strictEqual(res.group, 1);
    assert.strictEqual(res.ta, 'かった');
    assert.strictEqual(res.masu, 'かいます');
    assert.strictEqual(res.nai, 'かわない');
});

test('R2.2: はなす conjugates to はなして / はなした (Group 1)', () => {
    const res = taContext.transformJapaneseVerb('はなす');
    assert.strictEqual(res.group, 1);
    assert.strictEqual(res.ta, 'はなした');
    assert.strictEqual(res.masu, 'はなします');
    assert.strictEqual(res.nai, 'はなさない');
});

test('R2.3: およぐ conjugates to およいだ (Group 1)', () => {
    const res = taContext.transformJapaneseVerb('およぐ');
    assert.strictEqual(res.group, 1);
    assert.strictEqual(res.ta, 'およいだ');
    assert.strictEqual(res.masu, 'およぎます');
});

test('R2.4: かします is recognized as Group 1 (not Group 3)', () => {
    const res = taContext.transformJapaneseVerb('かします');
    assert.strictEqual(res.group, 1, `Expected Group 1 for かします, got Group ${res.group}`);
    assert.strictEqual(res.ru, 'かす');
    assert.strictEqual(res.ta, 'かした');
    assert.strictEqual(res.nai, 'かさない');
});

test('R2.5: べんきょうする is recognized as Group 3 suru compound', () => {
    const res = taContext.transformJapaneseVerb('べんきょうする');
    assert.strictEqual(res.group, 3);
    assert.strictEqual(res.ta, 'べんきょうした');
    assert.strictEqual(res.masu, 'べんきょうします');
});

test('R2.6: いく exception conjugates to いった (Group 1)', () => {
    const res = taContext.transformJapaneseVerb('いく');
    assert.strictEqual(res.group, 1);
    assert.strictEqual(res.ta, 'いった');
});

// -----------------------------------------------------------------------------
// R3: Checkpoint Restoration withSilentUI
// -----------------------------------------------------------------------------
console.log('\n--- R3: Checkpoint Restoration withSilentUI Non-Destructive ---');
const CpCode = fs.readFileSync(path.join(ROOT, 'assets/js/checkpoint-sync.js'), 'utf8');
test('R3.1: checkpoint-sync tracks silentDepth and restoreGlobalsTimer', () => {
    assert.ok(CpCode.includes('silentDepth'), 'checkpoint-sync.js must track re-entrant silentDepth');
    assert.ok(CpCode.includes('restoreGlobalsTimer'), 'checkpoint-sync.js must debounce global restoration');
});

// -----------------------------------------------------------------------------
// R4: Typing Studio Reset on Clear Checkpoint
// -----------------------------------------------------------------------------
console.log('\n--- R4: Typing Studio Reset Registration ---');
test('R4.1: checkpoint-sync only clears studio history on a mounted studio page', () => {
    assert.match(CpCode, /if \(typeof window\.resetTypingStudio === 'function'\) \{\s*toRemove\.push\(window\.REVIEW_11_18_TYPING_CONFIG\?\.storageKey \|\| 'marugoto_typing_studio_v2'\)/);
});

const TypingCode = fs.readFileSync(path.join(ROOT, 'assets/js/typing-studio.js'), 'utf8');
test('R4.2: typing-studio registers keys and exports reset function', () => {
    assert.ok(TypingCode.includes('window.resetTypingStudio ='), 'typing-studio.js must export window.resetTypingStudio');
    assert.ok(TypingCode.includes('window.__MARUGOTO_CP_EXTRA_KEYS__'), 'typing-studio.js must register key in __MARUGOTO_CP_EXTRA_KEYS__');
});

// -----------------------------------------------------------------------------
// R5: Filter Input State Preservation in Verb Tables
// -----------------------------------------------------------------------------
console.log('\n--- R5: Verb Table Filter Input Preservation ---');
test('R5.1: the_ta.js preserves userVerbAnswers across renders', () => {
    assert.ok(TheTaCode.includes('userVerbAnswers'), 'the_ta.js must store user answers across filter passes');
});
const TheNaiCode = fs.readFileSync(path.join(ROOT, 'assets/js/pages/the_nai.js'), 'utf8');
test('R5.2: the_nai.js preserves userNaiInputs across renders', () => {
    assert.ok(TheNaiCode.includes('userNaiInputs'), 'the_nai.js must store user answers across filter passes');
});

// -----------------------------------------------------------------------------
// R6: No Double Skip on Auto-Advance
// -----------------------------------------------------------------------------
console.log('\n--- R6: Auto-Advance Timer Cancel Management ---');
test('R6.1: typing-studio manages autoAdvanceTimer with cancellation', () => {
    assert.ok(TypingCode.includes('autoAdvanceTimer'), 'typing-studio.js must track autoAdvanceTimer');
    assert.ok(TypingCode.includes('clearAutoAdvanceTimer'), 'typing-studio.js must define clearAutoAdvanceTimer');
});

// -----------------------------------------------------------------------------
// R7: End of Round Summary Modal & Review Queue Consistency
// -----------------------------------------------------------------------------
console.log('\n--- R7: Round Summary & Review Queue Consistency ---');
test('R7.1: typing-studio calculates true review count and includes reveals in review queue', () => {
    assert.ok(TypingCode.includes('needsReviewCount'), 'typing-studio.js must calculate true review count');
    assert.ok(TypingCode.includes("h.status === 'err' || h.status === 'reveal'"), 'review queue must include both err and reveal');
});

// -----------------------------------------------------------------------------
// R8: 3D Engine Animation Loop Control & Geometry Disposal
// -----------------------------------------------------------------------------
console.log('\n--- R8: 3D Resource Disposal and Loop Control ---');
const Engine3DCode = fs.readFileSync(path.join(ROOT, 'assets/js/vocab-3d-engine.js'), 'utf8');
test('R8.1: vocab-3d-engine disposes geometry and stops render loop on close/hidden', () => {
    assert.ok(Engine3DCode.includes('disposeHierarchy'), 'vocab-3d-engine.js must define disposeHierarchy');
    assert.ok(Engine3DCode.includes('stopAnimateLoop'), 'vocab-3d-engine.js must define stopAnimateLoop');
    assert.ok(Engine3DCode.includes('visibilitychange'), 'vocab-3d-engine.js must pause rendering when tab is hidden');
});

// -----------------------------------------------------------------------------
// R9: Vocabulary Test Mode Does Not Reveal Answers Immediately
// -----------------------------------------------------------------------------
console.log('\n--- R9: Vocab Test Mode Answer Suppression ---');
const VocabHubCode = fs.readFileSync(path.join(ROOT, 'assets/js/vocab-hub.js'), 'utf8');
test('R9.1: vocab-hub suppresses immediate answers in test mode', () => {
    assert.ok(VocabHubCode.includes("quizSettings.mode === 'test'"), 'vocab-hub.js must branch behavior on test mode');
    assert.ok(VocabHubCode.includes("btnEl.classList.add('selected')"), 'test mode must mark selected button without revealing correct/wrong');
});

// -----------------------------------------------------------------------------
// R11: Generator Relative Path
// -----------------------------------------------------------------------------
console.log('\n--- R11: Build Generator Relative Workspace ---');
const CramBuildCode = fs.readFileSync(path.join(ROOT, 'scripts/build_cram_kanji_11_18.py'), 'utf8');
test('R11.1: build_cram_kanji_11_18.py resolves workspace dynamically', () => {
    assert.ok(!CramBuildCode.includes("WORKSPACE = '/Users/"), 'build_cram_kanji_11_18.py must not hardcode user path');
    assert.ok(CramBuildCode.includes('os.path.abspath(os.path.dirname(os.path.dirname(__file__)))'), 'build_cram_kanji_11_18.py must resolve workspace dynamically');
});

// -----------------------------------------------------------------------------
// Polish: Navigation & Accessibility
// -----------------------------------------------------------------------------
console.log('\n--- Polish: Nav & Accessibility ---');
const NavCode = fs.readFileSync(path.join(ROOT, 'assets/nav.js'), 'utf8');
test('Polish.1: nav.js Te-form links directly to Luyen_Tap_The_Te_A2_1.html', () => {
    assert.ok(!NavCode.includes("{ file: 'index.html', title: '🌸 Thể TE"), 'nav.js must not point Te-form to index.html');
});
test('Polish.2: Tab key is preserved for accessibility in Typing Studio', () => {
    assert.ok(TypingCode.includes("altKey && (e.key.toLowerCase() === 's' || e.key.toLowerCase() === 'n')"), 'typing-studio.js must use Alt+S/Alt+N and not block Tab');
});

// -----------------------------------------------------------------------------
// R12: Grammar Formula Box Contrast & Stylesheet Ordering
// -----------------------------------------------------------------------------
console.log('\n--- R12: Grammar Formula Box High-Contrast Legibility ---');
const GrammarHtml = fs.readFileSync(path.join(ROOT, 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html'), 'utf8');
const GrammarCss = fs.readFileSync(path.join(ROOT, 'assets/css/pages/tong_hop_ngu_phap.css'), 'utf8');
const SiteThemeCss = fs.readFileSync(path.join(ROOT, 'assets/css/site-theme.css'), 'utf8');

test('R12.1: Tong_Hop_Ngu_Phap loads site-theme.css BEFORE page css', () => {
    const siteThemeIdx = GrammarHtml.indexOf('assets/css/site-theme.css');
    const pageCssIdx = GrammarHtml.indexOf('assets/css/pages/tong_hop_ngu_phap.css');
    assert.ok(siteThemeIdx !== -1, 'site-theme.css must be present');
    assert.ok(pageCssIdx !== -1, 'tong_hop_ngu_phap.css must be present');
    assert.ok(siteThemeIdx < pageCssIdx, 'site-theme.css must be loaded BEFORE tong_hop_ngu_phap.css');
});

test('R12.2: tong_hop_ngu_phap.css enforces deep midnight indigo formula box with crisp white text', () => {
    assert.ok(GrammarCss.includes('linear-gradient(135deg, #0f172a 0%, #1e293b 100%) !important'), 'formula-box must have dark gradient background');
    assert.ok(GrammarCss.includes('color: #ffffff !important'), 'formula-box .jp-text must have pure white text');
});

test('R12.3: site-theme.css does not override generic .formula-box with white background', () => {
    assert.ok(!SiteThemeCss.match(/\.rule-box,\s*\.formula-box\s*,\s*\.grammar-explain/), 'site-theme.css must not have bare .formula-box grouped with .rule-box');
});

console.log(`\n========================================`);
console.log(`SUMMARY: ${passed} PASSED, ${failed} FAILED`);
console.log(`========================================`);

if (failed > 0) {
    process.exit(1);
}
