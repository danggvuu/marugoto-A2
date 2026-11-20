/* Study companion; the exam and quick-check controllers keep their own state. */
(function (window, document) {
    'use strict';
    const data = window.REVIEW_11_18_DATA;
    if (!data) return;
    const KEY = 'marugoto_review_11_18_ui_v1';
    const views = ['theory', 'vocab', 'kanji', 'typing', 'cheatsheet'];
    let state = { view: 'exam', vocabLesson: 'all', vocabSearch: '', vocabPage: 1,
        hideMeaning: false, kanjiLesson: 'all', kanjiSearch: '' };
    let currentVocab = [];
    let currentKanji = [];
    const escape = value => String(value ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    const normalize = value => String(value).normalize('NFKC').toLowerCase().trim();
    const titles = { theory: '📖 Lý thuyết bài 11–18', vocab: '🎴 Từ vựng bài 11–18',
        kanji: '⛩️ Chữ Hán bài 11–18', typing: '⌨️ Phòng luyện gõ', cheatsheet: '⚡ Cẩm nang bỏ túi' };
    window.REVIEW_11_18_TYPING_CONFIG = {
        storageKey: 'marugoto_review_11_18_typing_v1', data,
        lessons: Array.from({ length: 8 }, (_, i) => `A2-${i + 11}`)
    };
    window.__MARUGOTO_CP_EXTRA_KEYS__ = [...new Set([...(window.__MARUGOTO_CP_EXTRA_KEYS__ || []), KEY])];

    function save() {
        try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (error) {}
    }

    function renderVocab() {
        const query = normalize(state.vocabSearch);
        currentVocab = data.VOCAB_DATA.filter(item =>
            (state.vocabLesson === 'all' || item.l === state.vocabLesson) &&
            (!query || normalize([item.kana, item.romaji, item.vi].join(' ')).includes(query)));
        const pages = Math.max(1, Math.ceil(currentVocab.length / 40));
        state.vocabPage = Math.max(1, Math.min(state.vocabPage, pages));
        const start = (state.vocabPage - 1) * 40;
        document.getElementById('reviewVocabCount').textContent =
            `${currentVocab.length} từ · Trang ${state.vocabPage}/${pages}`;
        document.getElementById('reviewVocabBody').innerHTML = currentVocab.slice(start, start + 40).map((item, i) => `
            <tr><td>${escape(item.l.replace('A2-', 'Bài '))}</td>
            <td lang="ja">${escape(item.kana)}</td><td>${escape(item.romaji)}</td>
            <td>${state.hideMeaning ? '<span class="review-masked">••••••</span>' : escape(item.vi)}</td>
            <td><button type="button" data-review-audio="${start + i}" aria-label="Nghe ${escape(item.kana)}">🔊</button></td></tr>
        `).join('') || '<tr><td colspan="5">Không có từ phù hợp. Hãy đổi bộ lọc hoặc xóa tìm kiếm.</td></tr>';
        document.getElementById('reviewVocabBody').querySelectorAll('[data-review-audio]').forEach(button => {
            button.addEventListener('click', () => window.speakText?.(currentVocab[Number(button.dataset.reviewAudio)].kana));
        });
        document.getElementById('reviewHideMeaning').textContent = state.hideMeaning ? 'Hiện nghĩa' : 'Ẩn nghĩa';
        const pagination = document.getElementById('reviewVocabPagination');
        pagination.innerHTML = `<button type="button" data-page="${state.vocabPage - 1}" ${state.vocabPage === 1 ? 'disabled' : ''}>← Trước</button>
            <span>${state.vocabPage} / ${pages}</span>
            <button type="button" data-page="${state.vocabPage + 1}" ${state.vocabPage === pages ? 'disabled' : ''}>Tiếp →</button>`;
        pagination.querySelectorAll('button').forEach(button => button.addEventListener('click', () => {
            state.vocabPage = Number(button.dataset.page);
            renderVocab();
            save();
        }));
    }

    function renderKanji() {
        const query = normalize(state.kanjiSearch);
        currentKanji = data.KANJI_DATA.filter(item =>
            (state.kanjiLesson === 'all' || item.lesson === state.kanjiLesson) &&
            (!query || normalize([item.char, item.hv, item.meaning, item.on, item.kun].join(' ')).includes(query)));
        document.getElementById('reviewKanjiCount').textContent = `${currentKanji.length} chữ phù hợp`;
        const compounds = [...data.KANJI_11_14_DATA, ...data.KANJI_15_18_DATA];
        document.getElementById('reviewKanjiGrid').innerHTML = currentKanji.map(item => {
            const examples = compounds.filter(word => word.kanji.includes(item.char)).slice(0, 3);
            return `<article class="review-kanji-card">
                <div class="review-kanji-top"><strong lang="ja">${escape(item.char)}</strong>
                <div><h3>${escape(item.hv)}</h3><p>${escape(item.lessonName)} · ${item.strokes} nét</p></div></div>
                <p>${escape(item.meaning)}</p><dl><dt>On</dt><dd lang="ja">${escape(item.on || '—')}</dd>
                <dt>Kun</dt><dd lang="ja">${escape(item.kun || '—')}</dd></dl>
                <p class="review-mnemonic">💡 ${escape(item.mnemonic)}</p>
                <div class="review-kanji-examples">${examples.map(word => `<button type="button" data-kana="${escape(word.kana)}">
                    <span lang="ja">${escape(word.kanji)} · ${escape(word.kana)}</span><small>${escape(word.vi)} · 🔊</small></button>`).join('') ||
                    '<p>Chưa có từ ghép đạt bộ lọc chữ; xem âm On/Kun phía trên.</p>'}</div>
                </article>`;
        }).join('') || '<p>Không có chữ phù hợp.</p>';
        document.getElementById('reviewKanjiGrid').querySelectorAll('[data-kana]').forEach(button => {
            button.addEventListener('click', () => window.speakText?.(button.dataset.kana));
        });
    }

    async function copy(text) {
        const status = document.getElementById('reviewCopyStatus');
        try {
            if (!text) { status.textContent = 'Không có dữ liệu trong bộ lọc hiện tại.'; return; }
            await navigator.clipboard.writeText(text);
            status.textContent = `Đã copy ${text.split('\n').length} mục. Dán vào Quizlet để nhập bộ từ.`;
        } catch (error) {
            status.textContent = 'Trình duyệt không cho copy. Hãy cấp quyền clipboard hoặc dùng HTTPS.';
        }
    }

    function requestedView() {
        const hash = location.hash.slice(1);
        if (hash === 'typing' || hash === 'kanji-typing') return 'typing';
        if (hash.startsWith('review-') && views.includes(hash.slice(7))) return hash.slice(7);
        if (/^(grammar-l|cheat)/.test(hash)) return /cheat/.test(hash) ? 'cheatsheet' : 'theory';
        if (hash === 'vocab-kanji-check') return 'quick';
        if (hash) return 'exam';
        return views.includes(state.view) ? state.view : 'exam';
    }

    function selectView(view, updateHash = false) {
        if (!views.includes(view) && view !== 'quick') view = 'exam';
        const study = views.includes(view);
        const exam = document.getElementById('fullExamPanel');
        const wasExamVisible = !exam.hidden;
        window.setFullReviewBasePanel?.(view !== 'exam');
        // The base controller owns timer pause/resume; non-exam study views
        // borrow its paused state without revealing the quick-check panel.
        if (study) {
            document.getElementById('vocabKanjiCheck').hidden = true;
            exam.hidden = true;
        }
        document.getElementById('reviewStudyPanel').hidden = !study;
        document.querySelectorAll('.review-study-view').forEach(panel => {
            panel.hidden = panel.id !== `review-${view}`;
        });
        document.querySelectorAll('[data-review-view]').forEach(button => {
            button.setAttribute('aria-pressed', String(button.dataset.reviewView === view));
        });
        document.getElementById('showFullExam').setAttribute('aria-pressed', String(view === 'exam'));
        document.getElementById('showVocabCheck').setAttribute('aria-pressed', String(view === 'quick'));
        if (study) document.getElementById('reviewPanelTitle').textContent = titles[view];
        if (view === 'typing') window.initTypingPractice();
        if (study && wasExamVisible) window.AudioEngine?.stop();
        state.view = view;
        save();
        if (updateHash) history.replaceState(null, '', location.pathname + location.search +
            (view === 'exam' ? '#' + currentExamCode : view === 'quick' ? '#vocab-kanji-check' : '#review-' + view));
    }

    function init() {
        try {
            const saved = JSON.parse(localStorage.getItem(KEY) || 'null');
            if (saved && typeof saved === 'object') {
                if (views.includes(saved.view)) state.view = saved.view;
                for (const key of ['vocabLesson', 'kanjiLesson']) {
                    const select = document.getElementById(key === 'vocabLesson' ? 'reviewVocabLesson' : 'reviewKanjiLesson');
                    if ([...select.options].some(option => option.value === saved[key])) state[key] = saved[key];
                }
                for (const key of ['vocabSearch', 'kanjiSearch']) if (typeof saved[key] === 'string') state[key] = saved[key];
                state.hideMeaning = saved.hideMeaning === true;
                if (Number.isInteger(saved.vocabPage)) state.vocabPage = saved.vocabPage;
            }
        } catch (error) {}
        for (const [id, key] of [['reviewVocabLesson', 'vocabLesson'], ['reviewKanjiLesson', 'kanjiLesson'],
            ['reviewVocabSearch', 'vocabSearch'], ['reviewKanjiSearch', 'kanjiSearch']]) {
            const input = document.getElementById(id);
            input.value = state[key];
            input.addEventListener(input.tagName === 'SELECT' ? 'change' : 'input', () => {
                state[key] = input.value;
                if (key.startsWith('vocab')) { state.vocabPage = 1; renderVocab(); } else renderKanji();
                save();
            });
        }
        renderVocab();
        renderKanji();
        document.getElementById('reviewHideMeaning').addEventListener('click', () => {
            state.hideMeaning = !state.hideMeaning; renderVocab(); save();
        });
        document.getElementById('reviewCopyVocab').addEventListener('click', () =>
            copy(currentVocab.map(item => `${item.kana}\t${item.vi}`).join('\n')));
        document.getElementById('reviewCopyKanji').addEventListener('click', () =>
            copy(currentKanji.map(item => `${item.char}\t${item.hv} · ${item.meaning} · On: ${item.on} / Kun: ${item.kun}`).join('\n')));
        document.querySelectorAll('[data-review-view]').forEach(button => {
            button.addEventListener('click', () => selectView(button.dataset.reviewView, true));
        });
        document.getElementById('showFullExam').addEventListener('click', () => selectView('exam', true));
        document.getElementById('showVocabCheck').addEventListener('click', () => selectView('quick', true));
        document.querySelector('.exam-start-link').addEventListener('click', () => selectView('exam'));
        window.addEventListener('hashchange', () => {
            selectView(requestedView());
            if (/^#grammar-l/.test(location.hash)) document.getElementById(location.hash.slice(1))?.scrollIntoView();
        });
        selectView(requestedView());
    }

    // Base panel init registers later; wait until all DOMContentLoaded handlers run.
    document.addEventListener('DOMContentLoaded', () => queueMicrotask(init));
})(window, document);
