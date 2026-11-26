/* Marugoto A2-2 sentence typing practice: 40 Vietnamese prompts per lesson. */
(function () {
    'use strict';

    const items = window.SENTENCE_PRACTICE_DATA;
    const section = document.getElementById('sec-sentence-practice');
    if (!section || !Array.isArray(items) || !items.length) return;
    if (items.length !== 40) throw new Error('Sentence practice must contain exactly 40 prompts.');

    const revision = 'a2-2-typing40-v1';
    const key = window.MarugotoCheckpoint?.getKey?.('typing_sentences_a2_2_v1')
        || `marugoto_cp_v1::${location.pathname}::typing_sentences_a2_2_v1`;

    function loadState() {
        try {
            const saved = JSON.parse(localStorage.getItem(key) || 'null');
            const state = saved && saved.d ? saved.d : saved;
            if (state?.revision === revision && state.items && typeof state.items === 'object') return state;
        } catch (error) {
            // Ignore an invalid practice-only checkpoint without touching other lesson progress.
        }
        return { revision, items: {}, showAllAnswers: false };
    }

    const state = loadState();
    const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({
        '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[char]);

    section.innerHTML = `
        <div class="section-header">
            <h2 class="section-title"><span>⌨️</span> Luyện gõ 40 câu Việt → Nhật</h2>
            <span class="section-tag">Có đáp án Kanji • Lưu tiến độ riêng</span>
        </div>
        <p class="sentence-practice-intro">Đọc câu tiếng Việt rồi tự gõ câu tiếng Nhật bằng IME. Đáp án yêu cầu đúng mặt chữ Kanji được học; Hiragana/Katakana, khoảng trắng và dấu câu được chuẩn hóa. Câu mẫu chỉ hiện khi bấm xem đáp án.</p>
        <div class="sentence-practice-toolbar">
            <strong>Đã đúng: <span id="sentencePracticeProgress">0 / 40</span></strong>
            <div class="sentence-practice-actions">
                <button type="button" class="tp-btn-sub" id="sentenceShowAll">Hiện đáp án</button>
                <button type="button" class="tp-btn-sub" id="sentenceReset">Làm lại 40 câu</button>
            </div>
        </div>
        <div class="sentence-practice-list" id="sentencePracticeList"></div>
    `;

    const list = section.querySelector('#sentencePracticeList');
    const progress = section.querySelector('#sentencePracticeProgress');
    const showAllButton = section.querySelector('#sentenceShowAll');

    function saveState() {
        try {
            localStorage.setItem(key, JSON.stringify({ t: Date.now(), d: state }));
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

    function updateProgress() {
        const count = Object.values(state.items).filter(item => item.status === 'correct').length;
        progress.textContent = `${count} / ${items.length}`;
        showAllButton.textContent = state.showAllAnswers ? 'Ẩn đáp án' : 'Hiện đáp án';
    }

    function updateCard(card, item, saved = {}) {
        const input = card.querySelector('.sentence-practice-input');
        const status = card.querySelector('.sentence-practice-status');
        const answer = card.querySelector('.sentence-practice-answer');
        if (document.activeElement !== input || input.value !== (saved.draft || '')) input.value = saved.draft || '';
        const visible = state.showAllAnswers || saved.revealed;
        answer.hidden = !visible;
        answer.textContent = item.jp;
        card.classList.toggle('is-correct', saved.status === 'correct');
        card.classList.toggle('is-wrong', saved.status === 'wrong');
        status.textContent = saved.status === 'correct' ? '✓ Đúng' : saved.status === 'wrong' ? 'Chưa đúng' : 'Chưa gõ';
        status.className = `sentence-practice-status${saved.status === 'correct' ? ' is-correct' : saved.status === 'wrong' ? ' is-wrong' : ''}`;
        updateProgress();
    }

    function grade(item, card) {
        const input = card.querySelector('.sentence-practice-input');
        const current = state.items[item.id] || {};
        if (!input.value.trim()) {
            input.focus();
            return;
        }
        current.draft = input.value;
        current.status = normalize(input.value) === normalize(item.jp) ? 'correct' : 'wrong';
        state.items[item.id] = current;
        updateCard(card, item, current);
        saveState();
        if (current.status === 'correct') window.speakText?.(item.jp);
    }

    items.forEach(item => {
        const card = document.createElement('article');
        card.className = 'sentence-practice-card';
        card.dataset.sentenceId = String(item.id);
        card.innerHTML = `
            <div class="sentence-practice-card-head">
                <span class="sentence-practice-number">Câu ${item.id}</span>
                <span class="sentence-practice-status">Chưa gõ</span>
            </div>
            <p class="sentence-practice-prompt">${escapeHtml(item.vi)}</p>
            <label class="sentence-practice-label" for="sentencePracticeInput${item.id}">Gõ câu tiếng Nhật có Kanji:</label>
            <div class="sentence-practice-entry">
                <input class="sentence-practice-input" id="sentencePracticeInput${item.id}" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="日本語を入力してください" lang="ja">
                <button type="button" class="sentence-practice-check">Kiểm tra</button>
                <button type="button" class="sentence-practice-reveal">Đáp án</button>
                <button type="button" class="sentence-practice-speak" aria-label="Nghe câu mẫu">🔊</button>
            </div>
            <p class="sentence-practice-answer" hidden></p>
        `;
        const input = card.querySelector('.sentence-practice-input');
        const saved = state.items[item.id] || {};
        updateCard(card, item, saved);
        card.querySelector('.sentence-practice-check').addEventListener('click', () => grade(item, card));
        card.querySelector('.sentence-practice-reveal').addEventListener('click', () => {
            saved.revealed = !saved.revealed;
            state.items[item.id] = saved;
            updateCard(card, item, saved);
            saveState();
        });
        card.querySelector('.sentence-practice-speak').addEventListener('click', () => window.speakText?.(item.jp));
        input.addEventListener('input', () => {
            const current = state.items[item.id] || {};
            current.draft = input.value;
            if (current.status) delete current.status;
            state.items[item.id] = current;
            updateCard(card, item, current);
            saveState();
        });
        input.addEventListener('keydown', event => {
            if (event.key === 'Enter' && !event.isComposing && event.keyCode !== 229) {
                event.preventDefault();
                grade(item, card);
            }
        });
        list.appendChild(card);
    });

    section.querySelector('#sentenceShowAll').addEventListener('click', () => {
        state.showAllAnswers = !state.showAllAnswers;
        items.forEach(item => updateCard(list.querySelector(`[data-sentence-id="${item.id}"]`), item, state.items[item.id] || {}));
        saveState();
    });
    section.querySelector('#sentenceReset').addEventListener('click', () => {
        state.items = {};
        state.showAllAnswers = false;
        items.forEach(item => updateCard(list.querySelector(`[data-sentence-id="${item.id}"]`), item));
        saveState();
    });
})();
