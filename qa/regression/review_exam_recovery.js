/* Focused controller behavior tests. Run: node qa/regression/review_exam_recovery.js */
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const root = path.resolve(__dirname, '../..');
const MIDTERM = 'assets/js/pages/de_thi_midterm_a2_1.js';
const DRAFT = 'marugoto_midterm_draft_';
const HISTORY = 'marugoto_midterm_history_v1';
let passed = 0;

function test(name, run) {
    run();
    passed++;
    console.log(`PASS: ${name}`);
}

// Only browser services are mocked: all grading, recovery, reset and timer
// functions below execute the actual shipped controllers, without replacements.
function harness(file = MIDTERM, options = {}) {
    const storage = options.storage || new Map();
    const blocked = options.blocked || {};
    const elements = new Map();
    function element(id) {
        if (elements.has(id)) return elements.get(id);
        const classes = new Set();
        const node = { value: '', checked: false, disabled: false, style: {},
            innerHTML: '', innerText: '', textContent: '', offsetTop: 100, dataset: {}, children: [],
            scrollIntoView() {}, addEventListener() {}, getAttribute() { return ''; }, setAttribute() {},
            appendChild(child) { this.children.push(child); },
            querySelectorAll() { return []; }, querySelector() { return element(id + '_input'); } };
        Object.defineProperty(node, 'className', {
            get: () => [...classes].join(' '),
            set: value => { classes.clear(); String(value).split(/\s+/).filter(Boolean).forEach(x => classes.add(x)); }
        });
        node.classList = {
            add: (...names) => names.forEach(name => classes.add(name)),
            remove: (...names) => names.forEach(name => classes.delete(name)),
            contains: name => classes.has(name),
            toggle(name, force) {
                const add = force === undefined ? !classes.has(name) : force;
                if (add) classes.add(name); else classes.delete(name);
                return add;
            }
        };
        elements.set(id, node);
        return node;
    }
    const windowEvents = new Map();
    const documentEvents = new Map();
    const listen = events => (name, callback) => {
        if (!events.has(name)) events.set(name, []);
        events.get(name).push(callback);
    };
    const emit = (events, name) => (events.get(name) || []).forEach(callback => callback());
    let now = options.now || 1700000000000;
    let nextId = 1;
    const intervals = new Map();
    class ClockDate extends Date {
        constructor(...args) { super(...(args.length ? args : [now])); }
        static now() { return now; }
    }
    const context = {
        console, Date: ClockDate, confirm: () => true, alert() {}, scrollTo() {},
        addEventListener: listen(windowEvents),
        location: { hash: options.hash || '', reload() { emit(windowEvents, 'pagehide'); } },
        history: { replaceState(_, __, url) { context.location.hash = url.includes('#') ? url.slice(url.indexOf('#')) : ''; } },
        localStorage: {
            getItem(key) { if (blocked.read) throw Error('blocked read'); return storage.get(key) ?? null; },
            setItem(key, value) { if (blocked.write) throw Error('blocked write'); storage.set(key, String(value)); },
            removeItem(key) { if (blocked.remove) throw Error('blocked remove'); storage.delete(key); }
        },
        document: {
            body: element('body'), visibilityState: 'visible', addEventListener: listen(documentEvents),
            createElement: tag => element(`${tag}_${nextId++}`),
            getElementById: element,
            querySelector: selector => selector.includes('toggleTimer(') ? element('timerToggleBtn') : null,
            querySelectorAll: selector => selector.includes('#examContentContainer input')
                ? ['trans_input_31', 'essay_input_35', 'btnToggleTimer', 'btnResetTimer', 'submit'].map(element) : []
        },
        setTimeout: () => nextId++, clearTimeout() {},
        setInterval(callback, delay) {
            const id = nextId++;
            intervals.set(id, { callback, delay, next: now + delay });
            return id;
        },
        clearInterval: id => intervals.delete(id)
    };
    context.window = context;
    vm.createContext(context);
    for (const source of [...(options.data || []), file]) {
        vm.runInContext(fs.readFileSync(path.join(root, source), 'utf8'), context, { filename: source });
    }
    emit(documentEvents, 'DOMContentLoaded');
    const run = code => vm.runInContext(code, context);
    return {
        run, storage, blocked, element, intervals, context,
        snapshot: code => JSON.parse(JSON.stringify(run(code))),
        now: () => now,
        pagehide: () => emit(windowEvents, 'pagehide'),
        advance(milliseconds) {
            const target = now + milliseconds;
            while (true) {
                const next = [...intervals.values()].sort((a, b) => a.next - b.next)[0];
                if (!next || next.next > target) break;
                now = next.next;
                next.next += next.delay;
                next.callback();
            }
            now = target;
        },
        reload(elapsed = 0) {
            emit(windowEvents, 'pagehide');
            return harness(file, { ...options, storage, blocked, now: now + elapsed, hash: context.location.hash });
        }
    };
}

for (const initiallyCorrect of [false, true]) {
    test(`Midterm regrades ${initiallyCorrect ? 'right → wrong' : 'wrong → right'} translations`, () => {
        const h = harness();
        h.run(`handleTransInput(31, ${initiallyCorrect ? 'getAllItems(EXAMS_DATA[0]).find(q => q.id === 31).reference' : "'。'"}); checkTranslationSingle(31);`);
        assert.strictEqual(h.run('userAnswers[31].isCorrect'), initiallyCorrect);
        h.run(`handleTransInput(31, ${initiallyCorrect ? "'。'" : 'getAllItems(EXAMS_DATA[0]).find(q => q.id === 31).reference'});`);
        assert.strictEqual(h.run('userAnswers[31].checked'), undefined);
        assert.strictEqual(h.run('userAnswers[31].isCorrect'), undefined);
        h.run('submitExam(true)');
        assert.strictEqual(h.element('modalScoreBig').textContent, initiallyCorrect ? '0 / 100' : '2.5 / 100');
    });
}

test('Midterm recomputes legacy cached grades without losing saved answers', () => {
    for (const correct of [false, true]) {
        const h = harness();
        const value = correct ? h.run('getAllItems(EXAMS_DATA[0]).find(q => q.id === 31).reference') : '。';
        h.storage.set(DRAFT + 'M101', JSON.stringify({ userAnswers: { 31: { value, checked: true, isCorrect: !correct } }, timerSeconds: 1234 }));
        const restored = harness(MIDTERM, { storage: h.storage, now: h.now() });
        assert.strictEqual(restored.run('timerSeconds'), 1234);
        assert.strictEqual(restored.run('userAnswers[31].value'), value);
        restored.run('submitExam(true)');
        assert.strictEqual(restored.run('userAnswers[31].isCorrect'), correct);
    }
});

test('Midterm keeps explicit self-grades across reload but revokes them on edits', () => {
    for (const edit of [false, true]) {
        let h = harness();
        h.run("handleTransInput(31, 'câu khác'); overrideTransCorrect(31)");
        h = h.reload();
        assert.strictEqual(h.run('userAnswers[31].selfApproved'), true);
        if (edit) h.run("handleTransInput(31, '。')");
        h.run('submitExam(true)');
        assert.strictEqual(h.run('userAnswers[31].isCorrect'), !edit);
    }
});

test('Midterm pause survives immediate reload and resumes one timer', () => {
    let h = harness();
    h.advance(3500);
    h.run('toggleTimer()');
    const remaining = h.run('timerSeconds');
    const saved = JSON.parse(h.storage.get(DRAFT + 'M101'));
    assert.strictEqual(saved.isTimerRunning, false);
    assert.strictEqual(saved.timerDeadline, null);
    h = h.reload(60000);
    assert.strictEqual(h.run('isTimerRunning'), false);
    assert.strictEqual(h.intervals.size, 0);
    h.advance(10000);
    assert.strictEqual(h.run('timerSeconds'), remaining);
    h.run('toggleTimer()');
    assert.strictEqual(h.intervals.size, 1);
    h.advance(1000);
    assert.strictEqual(h.run('timerSeconds'), remaining - 1);
});

test('Midterm running checkpoints account for elapsed time and expired reloads', () => {
    let h = harness();
    h = h.reload(5000);
    assert.strictEqual(h.run('timerSeconds'), 2695);
    assert.strictEqual(h.intervals.size, 1);
    h = h.reload(2700000);
    assert.strictEqual(h.run('timerSeconds'), 0);
    assert.strictEqual(h.run('isExamSubmitted'), true);
    assert.strictEqual(h.intervals.size, 0);
    h = h.reload();
    assert.strictEqual(JSON.parse(h.storage.get(HISTORY)).length, 1);
});

test('Midterm legacy zero-second checkpoints submit instead of resetting time', () => {
    const storage = new Map([[DRAFT + 'M101', JSON.stringify({ userAnswers: {}, timerSeconds: 0 })]]);
    const h = harness(MIDTERM, { storage });
    assert.strictEqual(h.run('timerSeconds'), 0);
    assert.strictEqual(h.run('isExamSubmitted'), true);
});

test('Midterm submitted reloads stay read-only without duplicating history', () => {
    let h = harness();
    h.run('handleSelectOption(1, 2); submitExam(true)');
    const answers = h.snapshot('userAnswers');
    h = h.reload();
    assert.strictEqual(h.run('isExamSubmitted'), true);
    assert.strictEqual(h.run('isTimerRunning'), false);
    assert.strictEqual(h.element('trans_input_31').disabled, true);
    assert.strictEqual(h.element('essay_input_35').disabled, true);
    assert.strictEqual(h.element('btnToggleTimer').disabled, true);
    h.run("handleSelectOption(1, 0); handleTransInput(31, '。'); handleEssayInput(35, 'new essay'); overrideTransCorrect(31); checkTranslationSingle(31); toggleTimer(); startTimer(); submitExam(true)");
    assert.deepStrictEqual(h.snapshot('userAnswers'), answers);
    assert.strictEqual(h.intervals.size, 0);
    assert.strictEqual(JSON.parse(h.storage.get(HISTORY)).length, 1);
});

test('Midterm switch flushes the active code and restores each timer independently', () => {
    const h = harness();
    h.advance(2500);
    h.run('handleSelectOption(1, 2); toggleTimer(); switchExam("M102")');
    assert.strictEqual(h.run('isTimerRunning'), true);
    assert.deepStrictEqual(h.snapshot('userAnswers'), {});
    assert.deepStrictEqual(h.snapshot('window.__MARUGOTO_CP_EXTRA_KEYS__'), [DRAFT + 'M102']);
    h.run('handleSelectOption(1, 1); switchExam("M101")');
    assert.strictEqual(h.run('userAnswers[1].value'), 2);
    assert.strictEqual(h.run('timerSeconds'), 2698);
    assert.strictEqual(h.run('isTimerRunning'), false);
    assert.strictEqual(JSON.parse(h.storage.get(DRAFT + 'M102')).userAnswers[1].value, 1);
    assert.strictEqual(h.run('window.__MARUGOTO_NATIVE_DOM_DISABLED__'), true);
});

test('Midterm shared checkpoint reset clears only the active code and cannot resurrect it on pagehide', () => {
    let h = harness();
    const otherDraft = JSON.stringify({ userAnswers: { 1: { value: 1 } }, timerSeconds: 1200 });
    const history = JSON.stringify([{ code: 'M102', totalScore: 80 }]);
    h.storage.set(DRAFT + 'M102', otherDraft);
    h.storage.set(HISTORY, history);
    h.storage.set('unrelated-progress', 'preserve');
    h.run('switchExam("M103"); handleSelectOption(1, 0)');
    assert.deepStrictEqual(h.snapshot('window.__MARUGOTO_CP_EXTRA_KEYS__'), [DRAFT + 'M103']);
    // The shared toolbar removes registered keys, then calls the native reset hook.
    h.snapshot('window.__MARUGOTO_CP_EXTRA_KEYS__').forEach(key => h.context.localStorage.removeItem(key));
    h.run('window.__MARUGOTO_ON_RESET__()');
    h.pagehide();
    assert.strictEqual(h.storage.has(DRAFT + 'M103'), false);
    assert.strictEqual(h.storage.get(DRAFT + 'M102'), otherDraft);
    assert.strictEqual(h.storage.get(HISTORY), history);
    assert.strictEqual(h.storage.get('unrelated-progress'), 'preserve');
    h = h.reload();
    assert.strictEqual(h.run('currentExamCode'), 'M103');
    assert.deepStrictEqual(h.snapshot('userAnswers'), {});
});

test('Midterm timer and native reset restart once without clearing other codes/history', () => {
    const h = harness();
    h.storage.set(DRAFT + 'M102', 'preserve');
    h.storage.set(HISTORY, '[]');
    h.advance(10000);
    h.run('resetTimer()');
    assert.strictEqual(h.run('timerSeconds'), 2700);
    assert.strictEqual(h.intervals.size, 1);
    h.run('handleSelectOption(1, 2); resetCurrentExam()');
    assert.deepStrictEqual(h.snapshot('userAnswers'), {});
    assert.strictEqual(h.intervals.size, 1);
    assert.strictEqual(h.storage.get(DRAFT + 'M102'), 'preserve');
    assert.strictEqual(h.storage.get(HISTORY), '[]');
});

test('Midterm grading, pause and reset remain usable with unavailable storage', () => {
    const h = harness(MIDTERM, { blocked: { read: true, write: true, remove: true } });
    h.run('toggleTimer(); handleTransInput(31, getAllItems(EXAMS_DATA[0]).find(q => q.id === 31).reference); submitExam(true)');
    assert.strictEqual(h.element('modalScoreBig').textContent, '2.5 / 100');
    assert.strictEqual(h.run('isTimerRunning'), false);
    h.run('resetCurrentExam()');
    assert.strictEqual(h.run('isExamSubmitted'), false);
    assert.strictEqual(h.intervals.size, 1);
    h.run('window.__MARUGOTO_ON_RESET__()');
    assert.strictEqual(h.intervals.size, 0);
});

for (const [name, file, data, reset, key] of [
    ['11–14', 'assets/js/mini-test-11-14.js', 'assets/data/mini_11_14_data.js', 'resetAllExam', 'marugoto_mini11_14_cp_v1'],
    ['A2.2 1–4', 'assets/js/mini-test-a2-2-1-4.js', 'assets/data/mini_a2_2_1_4_data.js', 'resetExamSuite', 'marugoto_mini_a2_2_1_4_cp_v1']
]) {
    test(`Mini ${name} restarts after expiry, pause and repeated resets`, () => {
        const h = harness(file, { data: [data] });
        h.run(name === '11–14' ? "switchMainTab('tab-quiz')" : "switchTab('tab-quiz')");
        h.storage.set('other-exam', 'preserve');
        h.run('timerStarted = true; isTimerRunning = true; totalSeconds = 1');
        h.advance(2000);
        assert.strictEqual(h.intervals.size, 0);
        h.run(`${reset}()`);
        assert.strictEqual(h.run('totalSeconds'), 2700);
        assert.strictEqual(h.intervals.size, 1);
        h.advance(5000);
        assert.strictEqual(h.run('totalSeconds'), 2695);
        assert.strictEqual(JSON.parse(h.storage.get(key)).totalSeconds, 2695);
        h.run(`toggleTimer(); ${reset}(); ${reset}()`);
        assert.strictEqual(h.run('isTimerRunning'), true);
        assert.strictEqual(h.intervals.size, 1);
        assert.match(h.element('timerToggleBtn').innerText + h.element('timerToggleBtn').innerHTML, /⏸️/);
        h.advance(1000);
        assert.strictEqual(h.run('totalSeconds'), 2699);
        assert.strictEqual(h.storage.get('other-exam'), 'preserve');
    });

    test(`Mini ${name} reset still restarts when storage removal/writes fail`, () => {
        const h = harness(file, { data: [data] });
        h.run(name === '11–14' ? "switchMainTab('tab-quiz'); timerStarted = true; isTimerRunning = true; totalSeconds = 1" : "switchTab('tab-quiz'); timerStarted = true; isTimerRunning = true; totalSeconds = 1");
        h.advance(2000);
        h.blocked.remove = h.blocked.write = true;
        h.run(`${reset}()`);
        h.advance(1000);
        assert.strictEqual(h.run('totalSeconds'), 2699);
        assert.strictEqual(h.intervals.size, 1);
    });
}

test('Mini A2.2 restores answers, drafts, self-score, tab, supplement filter and paused timer', () => {
    const file = 'assets/js/mini-test-a2-2-1-4.js';
    const data = 'assets/data/mini_a2_2_1_4_data.js';
    let h = harness(file, { data: [data] });
    h.run('selectPart1Answer(1, 0)');
    [2, 3, 0, 1].forEach(index => h.run(`handlePart2ChipClick(11, ${index})`));
    h.element('p3_input_16').value = '買った';
    h.run('gradePart3Question(16)');
    h.run('selectPart4Answer(21, 0); selectPart5Answer(25, 0)');
    h.element('trans_input_29').value = 'あそこで先生と話している人です。';
    h.run('handleTransInput(29); toggleModelAnswer(29); setPart6Score(29, 2.5)');
    h.run("filterKanji('SUPPLEMENT'); switchTab('tab-quiz'); toggleTimer()");
    h.advance(2300);
    h.run("switchTab('tab-kanji')");
    const saved = JSON.parse(h.storage.get('marugoto_mini_a2_2_1_4_cp_v1'));
    assert.strictEqual(saved.currentKanjiFilter, 'SUPPLEMENT');
    assert.strictEqual(saved.isTimerRunning, false);

    h = h.reload();
    assert.strictEqual(h.run('currentTab'), 'tab-kanji');
    assert.strictEqual(h.run('currentKanjiFilter'), 'SUPPLEMENT');
    assert.strictEqual(h.run('p1Answers[1]'), 0);
    assert.deepStrictEqual(h.snapshot('p2Selected[11]'), [2, 3, 0, 1]);
    assert.strictEqual(h.run('p2Graded[11]'), true);
    assert.strictEqual(h.element('p3_input_16').value, '買った');
    assert.strictEqual(h.run('p3Graded[16]'), true);
    assert.strictEqual(h.run('p4Selected[21]'), 0);
    assert.strictEqual(h.run('p5Answers[25]'), 0);
    assert.strictEqual(h.element('trans_input_29').value, 'あそこで先生と話している人です。');
    assert.strictEqual(h.element('p6_model_29').style.display, 'block');
    assert.strictEqual(h.run('p6SelfScores[29]'), 2.5);
    assert.strictEqual(h.run('isTimerRunning'), false);
    assert.strictEqual(h.run('totalSeconds'), saved.totalSeconds);
    assert.strictEqual(h.intervals.size, 0);
    h.run("switchTab('tab-quiz'); toggleTimer()");
    assert.strictEqual(h.intervals.size, 1);
});

test('Mini A2.2 editing a conjugation draft clears its old grade', () => {
    const h = harness('assets/js/mini-test-a2-2-1-4.js', {
        data: ['assets/data/mini_a2_2_1_4_data.js']
    });
    h.element('p3_input_16').value = '買った';
    h.run('gradePart3Question(16)');
    assert.strictEqual(h.run('p3Graded[16]'), true);
    h.element('p3_input_16').value = '買います';
    h.run('handlePart3Input(16)');
    assert.strictEqual(h.run('p3Graded[16]'), undefined);
    assert.strictEqual(h.element('p3_exp_16').style.display, 'none');
    assert.strictEqual(h.element('p3_input_16').classList.contains('correct'), false);
    assert.strictEqual(h.element('p3_input_16').classList.contains('wrong'), false);
    assert.strictEqual(JSON.parse(h.storage.get('marugoto_mini_a2_2_1_4_cp_v1')).p3Inputs[16], '買います');
});

test('Mini A2.2 accepts valid alternate word orders without changing chip indices', () => {
    const h = harness('assets/js/mini-test-a2-2-1-4.js', {
        data: ['assets/data/mini_a2_2_1_4_data.js']
    });
    const answers = [
        [11, [3, 0, 1, 2], '名前を'],
        [12, [1, 3, 0, 2], '笑っている'],
        [13, [3, 2, 0, 1], 'もっと'],
        [14, [0, 1, 2, 3], 'のは'],
        [15, [2, 3, 0, 1], 'しょうゆを']
    ];
    answers.forEach(([id, order, starChip]) => {
        h.run(`p2Selected[${id}] = ${JSON.stringify(order)}; checkPart2Complete(${id})`);
        assert.strictEqual(h.run(`p2Graded[${id}]`), true, `Alternate order for ${id} should be accepted`);
        assert.strictEqual(h.element(`p2_answer_star_${id}`).innerText, starChip);
    });
    const data = h.snapshot('part2Data');
    data.forEach((item, index) => {
        assert.strictEqual(item.correctOrder.join(','), [[2, 3, 0, 1], [3, 0, 1, 2], [3, 0, 1, 2], [3, 0, 1, 2], [0, 1, 2, 3]][index].join(','));
        assert.strictEqual(item.chips.length, 4);
    });
});

test('Mini A2.2 kana grading keeps katakana and rejects Kanji, romaji and empty answers', () => {
    const h = harness('assets/js/mini-test-a2-2-1-4.js', {
        data: ['assets/data/mini_a2_2_1_4_data.js']
    });
    h.run("const kanaFixture = {jp:'わたしはスーツをきています。', accepted:['スーツをきています。']};");
    for (const answer of ['わたしはスーツをきています。', 'スーツをきています。', ' わたしは ｽｰﾂをきています ']) {
        assert.strictEqual(h.run(`gradeKanaValue(${JSON.stringify(answer)}, kanaFixture).correct`), true);
    }
    for (const answer of ['わたしはすーつをきています。', '私はスーツを着ています。', 'watashi wa suutsu o kiteimasu', '。', '']) {
        assert.strictEqual(h.run(`gradeKanaValue(${JSON.stringify(answer)}, kanaFixture).correct`), false);
    }
});

console.log(`Exam recovery: ${passed} targeted behavior checks passed.`);
