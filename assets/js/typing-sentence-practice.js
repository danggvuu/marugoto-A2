/* Marugoto A2-2 sentence and Kanji typing practice. */
(function () {
    'use strict';

    const sentences = window.SENTENCE_PRACTICE_DATA;
    const kanji = window.KANJI_PRACTICE_DATA || [];
    const section = document.getElementById('sec-sentence-practice');
    if (!section || !Array.isArray(sentences) || !sentences.length) return;
    if (sentences.length !== 40) throw new Error('Sentence practice must contain exactly 40 prompts.');

    const revision = 'a2-2-typing40-v1';
    const key = window.MarugotoCheckpoint?.getKey?.('typing_sentences_a2_2_v1')
        || `marugoto_cp_v1::lessons/${location.pathname.split('/').pop()}::typing_sentences_a2_2_v1`;
    const legacyKey = `marugoto_cp_v1::${location.pathname}::typing_sentences_a2_2_v1`;

    function contentSignature(item, isKanji = false) {
        return JSON.stringify(isKanji
            ? [item.mean, item.word, item.accepted || []]
            : [item.vi, item.jp, item.accepted || [], Boolean(item.requireKanji)]);
    }

    function restoreItems(items, saved, isKanji = false) {
        const restored = {};
        items.forEach(item => {
            const current = saved?.[item.id];
            if (!current || typeof current !== 'object') return;
            const signature = contentSignature(item, isKanji);
            if (current.signature !== signature) {
                // Legacy checkpoints have no signature; preserve only still-valid correct answers.
                const validLegacy = !current.signature && current.status === 'correct' &&
                    (isKanji ? gradeKanji(current.draft || '', item) : gradeSentence(current.draft || '', item)).correct;
                if (!validLegacy) {
                    delete current.status;
                    delete current.feedback;
                }
            }
            restored[item.id] = { ...current, signature };
        });
        return restored;
    }

    function loadState() {
        try {
            const saved = [key, legacyKey].map(storageKey => {
                try {
                    return JSON.parse(localStorage.getItem(storageKey) || 'null');
                } catch (error) {
                    return null;
                }
            }).filter(checkpoint => (checkpoint?.d || checkpoint)?.revision === revision)
                .sort((a, b) => (Number(b.t) || 0) - (Number(a.t) || 0))[0];
            const state = saved && saved.d ? saved.d : saved;
            if (state?.revision === revision && state.items && typeof state.items === 'object') {
                state.items = restoreItems(sentences, state.items);
                state.kanjiItems = restoreItems(kanji, state.kanjiItems, true);
                try {
                    localStorage.setItem(key, JSON.stringify({ t: saved.t || Date.now(), d: state }));
                    localStorage.removeItem(legacyKey);
                } catch (error) {
                    // A failed migration must not discard the state already loaded into memory.
                }
                return state;
            }
        } catch (error) {
            // Ignore an invalid practice-only checkpoint without touching other lesson progress.
        }
        return { revision, items: {}, kanjiItems: {}, showAllAnswers: false };
    }

    const state = loadState();
    const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[char]);

    // This section owns its checkpoint; generic input restore must not resurrect reset drafts.
    section.setAttribute('data-cp-ignore', '');
    section.innerHTML = `
        <div class="section-header">
            <h2 class="section-title"><span aria-hidden="true">⌨</span> Luyện gõ 40 câu Việt → Nhật</h2>
            <span class="section-tag">Tự nhập câu có Kanji • Lưu tiến độ riêng</span>
        </div>
        <p class="sentence-practice-intro">Dịch từng câu sang tiếng Nhật bằng IME. Câu mẫu không hiện trước khi bạn yêu cầu; câu trả lời phải có Kanji và có thể dùng các cách viết tương đương đã duyệt.</p>
        <div class="sentence-practice-toolbar">
            <strong>Câu đúng: <span id="sentencePracticeProgress">0 / 40</span></strong>
            <div class="sentence-practice-actions">
                <button type="button" class="tp-btn-sub" id="sentenceShowAll">Hiện đáp án</button>
                <button type="button" class="tp-btn-sub" id="sentenceReset">Làm lại</button>
            </div>
        </div>
        <div class="sentence-practice-list" id="sentencePracticeList"></div>
        ${kanji.length ? `
            <div class="sentence-practice-kanji-head">
                <div>
                    <h3>Gõ từ Kanji theo nghĩa</h3>
                    <p>${kanji.length} mục gồm danh sách chính thức của bài và từ bổ sung trong phiếu. Phải nhập chữ Kanji, không chỉ nhập cách đọc.</p>
                </div>
                <strong>Từ đúng: <span id="kanjiPracticeProgress">0 / ${kanji.length}</span></strong>
            </div>
            <div class="sentence-practice-list sentence-practice-kanji-list" id="kanjiPracticeList"></div>
        ` : ''}
    `;

    const list = section.querySelector('#sentencePracticeList');
    const kanjiList = section.querySelector('#kanjiPracticeList');
    const progress = section.querySelector('#sentencePracticeProgress');
    const kanjiProgress = section.querySelector('#kanjiPracticeProgress');
    const showAllButton = section.querySelector('#sentenceShowAll');

    function saveState() {
        try {
            localStorage.setItem(key, JSON.stringify({ t: Date.now(), d: state }));
            localStorage.removeItem(legacyKey);
            window.MarugotoCheckpoint?.notifySaved?.();
        } catch (error) {
            // Storage can be unavailable in private browsing; typing still works for this visit.
        }
    }

    function normalize(value) {
        const normalized = window.JpTypingGrader?.toHiragana
            ? window.JpTypingGrader.toHiragana(value)
            : String(value || '').normalize('NFKC').toLowerCase();
        return normalized.trim().replace(/[()（）「」『』"'…・~～/／、,。.!！?？\s\-‐‑‒–—―_　]/g, '');
    }

    function gradeSentence(value, item) {
        if (item.requireKanji && window.JpTypingGrader?.grade) {
            const result = window.JpTypingGrader.grade(value, {
                vi: item.vi,
                kanjiModel: item.jp,
                kanjiAccepted: item.accepted || []
            }, 'sentence', { allowKanji: true });
            return { correct: result.ok, missingKanji: !window.JpTypingGrader.containsKanji(value) };
        }
        const acceptable = [item.jp, ...(item.accepted || [])].map(normalize);
        return {
            correct: acceptable.includes(normalize(value)) &&
                (!item.requireKanji || window.JpTypingGrader?.containsKanji?.(value)),
            missingKanji: item.requireKanji && !window.JpTypingGrader?.containsKanji?.(value)
        };
    }

    function gradeKanji(value, item) {
        const missingKanji = !window.JpTypingGrader?.containsKanji?.(value);
        return {
            correct: !missingKanji && [item.word, ...(item.accepted || [])].some(word => normalize(value) === normalize(word)),
            missingKanji
        };
    }

    function updateProgress() {
        const sentenceCount = Object.values(state.items).filter(item => item.status === 'correct').length;
        progress.textContent = `${sentenceCount} / ${sentences.length}`;
        if (kanjiProgress) {
            const kanjiCount = Object.values(state.kanjiItems).filter(item => item.status === 'correct').length;
            kanjiProgress.textContent = `${kanjiCount} / ${kanji.length}`;
        }
        showAllButton.textContent = state.showAllAnswers ? 'Ẩn đáp án' : 'Hiện đáp án';
    }

    function updateCard(card, item, saved = {}, isKanji = false) {
        const input = card.querySelector('.sentence-practice-input');
        const status = card.querySelector('.sentence-practice-status');
        const answer = card.querySelector('.sentence-practice-answer');
        const feedback = card.querySelector('.sentence-practice-feedback');
        if (document.activeElement !== input || input.value !== (saved.draft || '')) input.value = saved.draft || '';
        const visible = state.showAllAnswers || saved.revealed;
        answer.hidden = !visible;
        answer.textContent = isKanji ? item.word : item.jp;
        card.classList.toggle('is-correct', saved.status === 'correct');
        card.classList.toggle('is-wrong', saved.status === 'wrong');
        status.textContent = saved.status === 'correct' ? 'Đúng' : saved.status === 'wrong' ? 'Chưa đúng' : 'Chưa gõ';
        status.className = `sentence-practice-status${saved.status === 'correct' ? ' is-correct' : saved.status === 'wrong' ? ' is-wrong' : ''}`;
        if (feedback) feedback.textContent = saved.feedback || '';
        updateProgress();
    }

    function makeCard(item, isKanji = false) {
        const card = document.createElement('article');
        const id = String(item.id);
        const getStore = () => isKanji ? state.kanjiItems : state.items;
        const prompt = isKanji ? item.mean : item.vi;
        card.className = `sentence-practice-card${isKanji ? ' sentence-practice-kanji-card' : ''}`;
        card.dataset.sentenceId = id;
        card.innerHTML = `
            <div class="sentence-practice-card-head">
                <span class="sentence-practice-number">${isKanji ? `Kanji ${item.id}` : `Câu ${item.id}`}</span>
                <span class="sentence-practice-status" aria-live="polite">Chưa gõ</span>
            </div>
            <p class="sentence-practice-prompt">${escapeHtml(prompt)}</p>
            <label class="sentence-practice-label" for="sentencePracticeInput${isKanji ? `K${item.id}` : item.id}">${isKanji ? 'Gõ từ bằng chữ Kanji:' : 'Gõ câu tiếng Nhật có Kanji:'}</label>
            <div class="sentence-practice-entry">
                <input class="sentence-practice-input" id="sentencePracticeInput${isKanji ? `K${item.id}` : item.id}" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="${isKanji ? '漢字を入力してください' : '日本語を入力してください'}" lang="ja">
                <button type="button" class="sentence-practice-check">Kiểm tra</button>
                <button type="button" class="sentence-practice-reveal">Đáp án</button>
                ${isKanji ? '' : '<button type="button" class="sentence-practice-speak" aria-label="Nghe câu mẫu">🔊</button>'}
            </div>
            <p class="sentence-practice-feedback" aria-live="polite"></p>
            <p class="sentence-practice-answer" lang="ja" hidden></p>
        `;
        const input = card.querySelector('.sentence-practice-input');
        const getCurrent = () => getStore()[id] || { signature: contentSignature(item, isKanji) };
        updateCard(card, item, getCurrent(), isKanji);

        function grade() {
            if (!input.value.trim()) {
                input.focus();
                return;
            }
            const current = getCurrent();
            current.draft = input.value;
            const { correct, missingKanji } = isKanji ? gradeKanji(input.value, item) : gradeSentence(input.value, item);
            current.status = correct ? 'correct' : 'wrong';
            current.feedback = missingKanji ? 'Hãy nhập ít nhất một chữ Kanji; chỉ gõ kana chưa đủ.'
                : correct ? 'Chính xác.' : 'Chưa khớp; có thể xem đáp án tham khảo.';
            getStore()[id] = current;
            updateCard(card, item, current, isKanji);
            card.querySelector('.sentence-practice-feedback').textContent = current.feedback;
            saveState();
            if (correct && !isKanji) window.speakText?.(item.jp);
        }

        card.querySelector('.sentence-practice-check').addEventListener('click', grade);
        card.querySelector('.sentence-practice-reveal').addEventListener('click', () => {
            const current = getCurrent();
            current.revealed = !current.revealed;
            getStore()[id] = current;
            updateCard(card, item, current, isKanji);
            saveState();
        });
        const speak = card.querySelector('.sentence-practice-speak');
        if (speak) speak.addEventListener('click', () => window.speakText?.(item.jp));
        input.addEventListener('input', () => {
            const current = getCurrent();
            current.draft = input.value;
            if (current.status) delete current.status;
            if (current.feedback) delete current.feedback;
            getStore()[id] = current;
            updateCard(card, item, current, isKanji);
            card.querySelector('.sentence-practice-feedback').textContent = '';
            saveState();
        });
        input.addEventListener('keydown', event => {
            if (event.key === 'Enter' && !event.isComposing && event.keyCode !== 229) {
                event.preventDefault();
                grade();
            }
        });
        return card;
    }

    sentences.forEach(item => list.appendChild(makeCard(item)));
    if (kanjiList) kanji.forEach(item => kanjiList.appendChild(makeCard(item, true)));

    showAllButton.addEventListener('click', () => {
        state.showAllAnswers = !state.showAllAnswers;
        sentences.forEach(item => updateCard(list.querySelector(`[data-sentence-id="${item.id}"]`), item, state.items[item.id] || {}));
        kanji.forEach(item => updateCard(kanjiList.querySelector(`[data-sentence-id="${item.id}"]`), item, state.kanjiItems[item.id] || {}, true));
        saveState();
    });
    section.querySelector('#sentenceReset').addEventListener('click', () => {
        state.items = {};
        state.kanjiItems = {};
        state.showAllAnswers = false;
        sentences.forEach(item => updateCard(list.querySelector(`[data-sentence-id="${item.id}"]`), item));
        kanji.forEach(item => updateCard(kanjiList.querySelector(`[data-sentence-id="${item.id}"]`), item, {}, true));
        section.querySelectorAll('.sentence-practice-feedback').forEach(el => { el.textContent = ''; });
        saveState();
    });
})();
