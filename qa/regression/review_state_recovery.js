/* Behavior regressions for shared checkpoint recovery; Node built-ins only. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const ROOT = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(ROOT, file), 'utf8');
const plain = value => JSON.parse(JSON.stringify(value));
const STUDIO_KEY = 'marugoto_typing_studio_v2';
const CRAM_KEY = 'marugoto_cram_11_18_cp_v1';

function makeClock() {
    let now = 0;
    let nextId = 1;
    const jobs = new Map();
    return {
        setTimeout(fn, delay = 0) {
            const id = nextId++;
            jobs.set(id, { at: now + delay, fn });
            return id;
        },
        clearTimeout(id) { jobs.delete(id); },
        advance(ms) {
            const end = now + ms;
            let iterations = 0;
            while (true) {
                const next = [...jobs.entries()].filter(([, job]) => job.at <= end)
                    .sort((a, b) => a[1].at - b[1].at || a[0] - b[0])[0];
                if (!next) break;
                assert(++iterations < 1000, 'timer loop did not settle');
                jobs.delete(next[0]);
                now = next[1].at;
                next[1].fn();
            }
            now = end;
        }
    };
}

function makeBrowser(initialStorage = {}, autoNodes = false) {
    const elements = new Map();
    const queries = new Map();
    const listeners = new Map();
    const storage = new Map(Object.entries(initialStorage));
    const writes = [];
    const clock = makeClock();

    class Element {
        constructor(id = '', attributes = {}) {
            this.id = id;
            this.attributes = attributes;
            this.style = {};
            this.dataset = {};
            this.value = '';
            this.innerHTML = '';
            this.children = [];
            const classes = new Set();
            this.classList = {
                add(...names) { names.forEach(name => classes.add(name)); },
                remove(...names) { names.forEach(name => classes.delete(name)); },
                contains(name) { return classes.has(name); },
                toggle(name, force) {
                    const next = force === undefined ? !classes.has(name) : Boolean(force);
                    if (next) classes.add(name);
                    else classes.delete(name);
                    return next;
                }
            };
        }
        getAttribute(name) { return this.attributes[name] || null; }
        setAttribute(name, value) { this.attributes[name] = String(value); }
        querySelector() { return null; }
        querySelectorAll() { return []; }
        addEventListener() {}
        focus() {}
        scrollIntoView() {}
        contains(child) { return this.children.includes(child); }
        appendChild(child) {
            this.children.push(child);
            if (child.id) elements.set(child.id, child);
            return child;
        }
    }

    function addElement(id, attributes) {
        const element = new Element(id, attributes);
        elements.set(id, element);
        return element;
    }
    const document = {
        readyState: 'loading',
        head: new Element(),
        body: new Element(),
        createElement() { return new Element(); },
        getElementById(id) { return elements.get(id) || (autoNodes ? addElement(id) : null); },
        querySelector() { return null; },
        querySelectorAll(selector) { return queries.get(selector) || []; },
        addEventListener(name, fn) {
            if (!listeners.has(name)) listeners.set(name, []);
            listeners.get(name).push(fn);
        }
    };
    const context = vm.createContext({
        console, document, Element,
        innerWidth: 1200,
        location: { pathname: '/the_ru.html', href: 'https://example.test/the_ru.html', hash: '', reload() {} },
        addEventListener() {},
        scrollTo() {},
        alert() {},
        setTimeout: clock.setTimeout,
        clearTimeout: clock.clearTimeout,
        localStorage: {
            get length() { return storage.size; },
            key(index) { return [...storage.keys()][index] || null; },
            getItem(key) { return storage.get(key) || null; },
            setItem(key, value) { storage.set(key, value); writes.push({ key, value }); },
            removeItem(key) { storage.delete(key); }
        }
    });
    context.window = context;
    return {
        context, document, elements, queries, storage, writes, clock, addElement,
        run(file) { vm.runInContext(read(file), context, { filename: file }); },
        domReady() { (listeners.get('DOMContentLoaded') || []).forEach(fn => fn()); }
    };
}

function studioSnapshot() {
    return {
        version: 2, mode: 'sentence', savedAt: 123,
        filterByMode: { sentence: 'all', kanji: 'all', vocab: 'all' },
        idxByBucket: { 'sentence::all': 0, 'kanji::all': 0 },
        orderByBucket: { 'kanji::all': ['k2', 'k1'] },
        history: { s1: { status: 'ok', lastInput: 'にほんごをべんきょうします。', whyWrong: [] } },
        drafts: { k1: 'から', s2: 'draft' },
        allowKanji: true, autoAdvance: false, streak: 3
    };
}

function cramSnapshot(filter = 11) {
    return {
        currentLessonFilter: filter, currentTab: 'tab-test', searchQuery: 'Xe',
        isMeaningHidden: true, cramIndex: 1, cramFlipped: true,
        cramOrder: ['12|車|くるま', '11|日|ひ'],
        npbsUserAnswers: { 1: 1 }, speedTestAnswers: { 0: 2 }, speedTestFinished: false
    };
}

function loadCram(storage = {}) {
    const env = makeBrowser(storage, true);
    env.context.MINI_15_18_DATA = {
        SENTENCE_TYPING_DATA: [{ id: 's1', lesson: 'A2-15', hira: 'にほんごをべんきょうします。', vi: 'Học tiếng Nhật' }],
        KANJI_15_18_DATA: [
            { id: 'k1', lesson: 'A2-15', kanji: '体', kana: 'からだ', vi: 'Cơ thể', stt: 1 },
            { id: 'k2', lesson: 'A2-16', kanji: '足', kana: 'あし', vi: 'Chân', stt: 2 }
        ],
        KANJI_11_14_DATA: [], VOCAB_DATA: []
    };
    env.context.CRAM_11_18_VOCAB = [
        { lesson: 11, kanji: '日', kana: 'ひ', vi: 'Ngày' },
        { lesson: 12, kanji: '車', kana: 'くるま', vi: 'Xe' }
    ];
    env.filters = [
        ["filterVocabByLesson('ALL', this)", 'ALL'],
        ['filterVocabByLesson(11, this)', '11'],
        ['filterVocabByLesson("12", this)', '12'],
        ["filterVocabByLesson('18', this)", '18'],
        ['filterVocabByLesson(111, this)', '111']
    ].map(([onclick, lesson]) => {
        const btn = env.addElement('filter-' + lesson, { onclick });
        btn.lesson = lesson;
        return btn;
    });
    env.queries.set('button[onclick*="filterVocabByLesson"]', env.filters);
    env.queries.set('.tab-btn', ['tab-vocab', 'tab-test', 'tab-typing'].map(id =>
        env.addElement('btn-' + id, { onclick: `switchMainTab('${id}')` })));
    env.queries.set('.tab-panel', ['tab-vocab', 'tab-test', 'tab-typing'].map(id => env.addElement(id)));
    env.run('assets/js/typing-studio.js');
    env.run('assets/js/cram-kanji.js');
    return env;
}

function assertStudioPreserved(env, saved) {
    const writes = env.writes.filter(entry => entry.key === STUDIO_KEY);
    assert(writes.length > 0, 'mode switch must still persist the studio');
    for (const { value } of writes) {
        const stored = JSON.parse(value);
        for (const key of ['history', 'drafts', 'filterByMode', 'orderByBucket', 'allowKanji', 'autoAdvance', 'streak']) {
            assert.deepEqual(stored[key], saved[key], `${key} was overwritten before restoration`);
        }
        assert.equal(stored.version, 2);
        assert.equal(stored.mode, 'kanji');
    }
    assert.equal(env.context.tpInitialized, true);
    assert.deepEqual(plain(env.context.tpState.history), saved.history);
}

test('first cram typing entry restores shared history and drafts before saving', () => {
    const saved = studioSnapshot();
    const env = loadCram({ [STUDIO_KEY]: JSON.stringify(saved), unrelated: 'keep' });
    assert.equal(env.context.tpInitialized, false);
    assert.equal(env.writes.length, 0);
    env.context.switchMainTab('tab-typing');
    assertStudioPreserved(env, saved);
    assert.equal(env.storage.get('unrelated'), 'keep');
    assert(env.elements.get('tab-typing').classList.contains('active'));
    env.context.tpState.drafts.unsaved = 'still in memory';
    env.context.switchMainTab('tab-vocab');
    env.context.switchMainTab('tab-typing');
    assert.equal(env.context.tpState.drafts.unsaved, 'still in memory', 're-entry must not reload older storage');
});

test('restoring a saved cram typing tab preserves the shared studio checkpoint', () => {
    const saved = studioSnapshot();
    const cram = { ...cramSnapshot(), currentTab: 'tab-typing' };
    const env = loadCram({ [STUDIO_KEY]: JSON.stringify(saved), [CRAM_KEY]: JSON.stringify(cram) });
    assert.equal(env.context.restoreCramCheckpoint(), true);
    assertStudioPreserved(env, saved);
    assert.equal(env.storage.get(CRAM_KEY), JSON.stringify(cram), 'restoration must not overwrite the cram snapshot');
});

test('typing deep link also restores progress, and a new user can start without a checkpoint', () => {
    for (const saved of [studioSnapshot(), null]) {
        const env = loadCram(saved ? { [STUDIO_KEY]: JSON.stringify(saved) } : {});
        env.context.location.hash = '#typing';
        env.domReady();
        if (saved) assertStudioPreserved(env, saved);
        else {
            assert.equal(env.context.tpState.mode, 'kanji');
            assert.equal(env.context.tpInitialized, true);
            assert.deepEqual(JSON.parse(env.storage.get(STUDIO_KEY)).history, {});
        }
    }
});

for (const filter of [11, '11', 12, '18', 'ALL']) {
    test(`cram restores lesson ${JSON.stringify(filter)} and the rest of its saved session`, () => {
        const saved = cramSnapshot(filter);
        const env = loadCram({ [CRAM_KEY]: JSON.stringify(saved) });
        assert.equal(env.context.restoreCramCheckpoint(), true);
        assert.deepEqual(env.filters.filter(btn => btn.classList.contains('active')).map(btn => btn.lesson), [String(filter)]);
        assert.equal(env.elements.get('vocabSearchInput').value, saved.searchQuery);
        assert.equal(env.elements.get('mainFlashcard').classList.contains('is-flipped'), true);
        assert.equal(env.elements.get('cramFrontKanji').innerText, '日');
        assert(env.elements.get('tab-test').classList.contains('active'));
        const state = plain(vm.runInContext('({ currentLessonFilter, cramIndex, npbsUserAnswers, speedTestAnswers, isRestoringCram })', env.context));
        assert.equal(state.currentLessonFilter, filter);
        assert.equal(state.cramIndex, 1);
        assert.deepEqual(state.npbsUserAnswers, saved.npbsUserAnswers);
        assert.deepEqual(state.speedTestAnswers, saved.speedTestAnswers);
        assert.equal(state.isRestoringCram, false);
        assert.equal(env.writes.length, 0, 'restoration must stay read-only');
    });
}

function loadCheckpoint(storage = {}) {
    const env = makeBrowser(storage);
    const calls = {};
    function tracked(name) { calls[name] = 0; return function () { calls[name]++; }; }
    env.context.speechSynthesis = { speak: tracked('synth') };
    env.context.speakText = tracked('text');
    env.context.speakJapanese = tracked('japanese');
    env.context.audioEngine = { speak: tracked('audio') };
    env.context.AudioEngine = { speak: tracked('Audio') };
    env.context.scrollTo = tracked('scroll');
    env.context.Element.prototype.scrollIntoView = tracked('elementScroll');
    env.context.alert = tracked('alert');
    env.calls = calls;
    env.invokeGlobals = () => {
        env.context.speechSynthesis.speak('test');
        env.context.speakText('test');
        env.context.speakJapanese('test');
        env.context.audioEngine.speak('test');
        env.context.AudioEngine.speak('test');
        env.context.scrollTo(0, 100);
        new env.context.Element().scrollIntoView();
        env.context.alert('test');
    };
    // Test-only access to the private helper; execute its real implementation unchanged.
    const source = read('assets/js/checkpoint-sync.js');
    const end = source.lastIndexOf('\n})();');
    assert(end >= 0, 'checkpoint IIFE boundary not found');
    vm.runInContext(source.slice(0, end) + '\nwindow.__testSilentUI = withSilentUI;' + source.slice(end), env.context);
    return env;
}

function assertCalls(env, expected) {
    for (const [name, count] of Object.entries(env.calls)) assert.equal(count, expected, name);
}

test('sequential silent restores retain originals until the extended unmute deadline', () => {
    const env = loadCheckpoint();
    env.context.__testSilentUI(env.invokeGlobals);
    assertCalls(env, 0);
    env.clock.advance(60);
    env.context.__testSilentUI(env.invokeGlobals);
    env.clock.advance(99);
    env.invokeGlobals();
    assertCalls(env, 0);
    assert.equal(env.context.isRestoringCheckpoint, true);
    env.clock.advance(1);
    env.invokeGlobals();
    assertCalls(env, 1);
    assert.equal(env.context.isRestoringCheckpoint, false);
});

test('nested and throwing silent restores unmute correctly, including later cycles', () => {
    const env = loadCheckpoint();
    assert.equal(env.context.__testSilentUI(() => env.context.__testSilentUI(() => 42)), 42);
    assert.throws(() => env.context.__testSilentUI(() => { throw new Error('restore failed'); }), /restore failed/);
    env.clock.advance(100);
    env.invokeGlobals();
    assertCalls(env, 1);
    let replacementCalls = 0;
    env.context.speakText = () => replacementCalls++;
    env.context.__testSilentUI(env.invokeGlobals);
    assertCalls(env, 1);
    env.clock.advance(100);
    env.invokeGlobals();
    assert.equal(replacementCalls, 1, 'a later restoration must capture the current real handler');
    assert.equal(env.context.isRestoringCheckpoint, false);
});

test('real checkpoint boot restores a tab plus grading without leaving the page muted', () => {
    const prefix = 'marugoto_cp_v1::the_ru.html::';
    const env = loadCheckpoint({
        [prefix + 'tab']: JSON.stringify({ d: { oc: "switchTab('tab-theory')", idx: 1 } }),
        [prefix + 'graded']: JSON.stringify({ d: 'gradeAll' })
    });
    const practice = env.addElement('practice', { onclick: "switchTab('tab-practice')" });
    const theory = env.addElement('theory', { onclick: "switchTab('tab-theory')" });
    practice.classList.add('active');
    theory.click = () => { practice.classList.remove('active'); theory.classList.add('active'); env.invokeGlobals(); };
    env.queries.set('.tab-btn, .nav-tab-btn, .mode-tab-btn, .tab-nav button, [role="tab"]', [practice, theory]);
    let grades = 0;
    env.context.gradeAll = () => { grades++; env.invokeGlobals(); };
    env.domReady();
    env.clock.advance(300);
    assert.equal(grades, 2, 'exercise must be replayed by both real restoration passes');
    assert(theory.classList.contains('active'));
    assertCalls(env, 0);
    env.invokeGlobals();
    assertCalls(env, 1);
    assert.equal(env.context.isRestoringCheckpoint, false);
});

test('checkpoint reset stays scoped to the current page and its registered native key', () => {
    const own = 'marugoto_cp_v1::the_ru.html::inputs';
    const other = 'marugoto_cp_v1::the_ta.html::inputs';
    const env = loadCheckpoint({ [own]: '{}', [other]: '{}', [STUDIO_KEY]: 'keep', nativeKey: '{}' });
    env.context.__MARUGOTO_CP_EXTRA_KEYS__ = ['nativeKey'];
    env.context.MarugotoCheckpoint.silentClearPage();
    assert.equal(env.storage.has(own), false);
    assert.equal(env.storage.has('nativeKey'), false);
    assert.equal(env.storage.has(other), true);
    assert.equal(env.storage.get(STUDIO_KEY), 'keep');
});

function deferred() {
    let resolve;
    const promise = new Promise(done => { resolve = done; });
    return { promise, resolve };
}
const settle = () => new Promise(resolve => setImmediate(resolve));
const svg = marker => `<svg data-marker="${marker}"><path d="M0 0L1 1"/></svg>`;
const item = char => ({ char, strokes: 4 });

function loadKanji() {
    const env = makeBrowser();
    env.context.VOCAB_121_DATA = [];
    env.context.kanjiData = [];
    env.requests = [];
    env.context.fetch = url => {
        const request = { url, ...deferred() };
        env.requests.push(request);
        return request.promise;
    };
    env.run('assets/js/kanji-a2.js');
    env.applied = [];
    // Rendering/network boundaries are faked; initKanjiPlayer and fetchKanjiSvg are real.
    env.context.setupSvgPlayer = (index, text) => {
        env.applied.push({ char: vm.runInContext(`kanjiPlayers[${index}].char`, env.context), text });
        env.elements.get('kanji-svg-container-' + index).innerHTML = text;
    };
    env.mount = index => {
        env.addElement('anim-status-' + index);
        env.addElement('stroke-steps-' + index);
        return env.addElement('kanji-svg-container-' + index);
    };
    env.resolveSvg = async (request, marker) => {
        request.resolve({ ok: true, text: async () => svg(marker) });
        await settle();
    };
    return env;
}

test('out-of-order SVG fetches cannot replace the newer character at a reused index', async () => {
    const env = loadKanji();
    env.mount(0);
    env.context.initKanjiPlayer(item('日'), 0);
    const current = env.mount(0);
    env.context.initKanjiPlayer(item('月'), 0);
    await env.resolveSvg(env.requests[1], '月');
    await env.resolveSvg(env.requests[0], '日');
    assert.deepEqual(env.applied, [{ char: '月', text: svg('月') }]);
    assert.equal(current.innerHTML, svg('月'));
    assert.equal(vm.runInContext('svgCache.get("日")', env.context), svg('日'), 'obsolete display results may still populate the cache');
});

test('a replaced card rejects its old SVG even before lazy initialization of the new player', async () => {
    const env = loadKanji();
    env.mount(0);
    env.context.initKanjiPlayer(item('日'), 0);
    const replacement = env.mount(0);
    await env.resolveSvg(env.requests[0], '日');
    assert.equal(env.applied.length, 0);
    assert.equal(replacement.innerHTML, '');
});

test('retrying the same character ignores the superseded request on the same DOM node', async () => {
    const env = loadKanji();
    const container = env.mount(0);
    env.context.initKanjiPlayer(item('日'), 0);
    env.context.initKanjiPlayer(item('日'), 0);
    await env.resolveSvg(env.requests[1], 'new retry');
    await env.resolveSvg(env.requests[0], 'old request');
    assert.equal(env.applied.length, 1);
    assert.equal(container.innerHTML, svg('new retry'));
});

test('an obsolete failed SVG fetch cannot overwrite a newer player with retry UI', async () => {
    const env = loadKanji();
    env.mount(0);
    env.context.initKanjiPlayer(item('日'), 0);
    env.mount(0);
    env.context.initKanjiPlayer(item('月'), 0);
    await env.resolveSvg(env.requests[1], '月');
    env.context.fetch = async () => ({ ok: false });
    env.requests[0].resolve({ ok: false });
    await settle();
    assert.equal(env.elements.get('anim-status-0').innerHTML, '');
    assert.equal(env.elements.get('stroke-steps-0').innerHTML, '');
    assert.equal(env.applied.length, 1);
});

test('a live failed SVG fetch still shows retry UI, and cached SVGs still render', async () => {
    const env = loadKanji();
    env.mount(0);
    env.context.fetch = async () => ({ ok: false });
    env.context.initKanjiPlayer(item('日'), 0);
    await settle();
    assert.match(env.elements.get('anim-status-0').innerHTML, /Thử lại/);
    assert.match(env.elements.get('stroke-steps-0').innerHTML, /Tải lại SVG/);
    vm.runInContext('svgCache.set("月", "<svg><path/></svg>")', env.context);
    env.mount(0);
    env.context.initKanjiPlayer(item('月'), 0);
    await settle();
    assert.deepEqual(env.applied, [{ char: '月', text: '<svg><path/></svg>' }]);
});
