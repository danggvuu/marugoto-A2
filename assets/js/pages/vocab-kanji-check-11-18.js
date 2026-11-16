/* Independent, strictly scoped A2.1 lesson 11–18 vocabulary/Kanji practice. */
(function (window, document) {
    'use strict';
    const DATA = window.VOCAB_KANJI_CHECK_DATA;
    const root = document.getElementById('vocabKanjiCheck');
    if (!DATA || !root) return;
    const KEY = 'marugoto_vocab_kanji_check_11_18_v1';
    window.__MARUGOTO_CP_EXTRA_KEYS__ = [...new Set([...(window.__MARUGOTO_CP_EXTRA_KEYS__ || []), KEY])];
    const items = [...DATA.vocab, ...DATA.kanji];
    const byId = new Map(items.map(item => [item.id, item]));
    const normal = value => String(value).normalize('NFKC').replace(/\s+/g, '').toLowerCase();
    const escape = value => String(value ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;')
        .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    const defaults = { lesson: 'all', mode: 'mixed', count: '20', direction: 'forward' };
    let settings = { ...defaults };
    let session = null;
    let previousExamRunning = false;

    function shuffled(array) {
        const result = [...array];
        for (let i = result.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [result[i], result[j]] = [result[j], result[i]];
        }
        return result;
    }

    function validSettings(value) {
        return value && (value.lesson === 'all' || DATA.lessons.includes(value.lesson)) &&
            ['mixed', 'kanji', 'vocab'].includes(value.mode) &&
            ['10', '20', 'all'].includes(String(value.count)) &&
            ['forward', 'reverse'].includes(value.direction);
    }

    function belongs(item, config) {
        return (config.lesson === 'all' || item.lesson === config.lesson) &&
            (config.mode === 'mixed' || item.id.startsWith(config.mode + ':'));
    }

    function fields(item, direction) {
        const kanji = item.id.startsWith('kanji:');
        if (kanji) return direction === 'forward'
            ? { prompt: item.jp, answer: item.kana, label: 'Kanji → chọn cách đọc Kana', kanji: true }
            : { prompt: item.kana, answer: item.jp, label: 'Kana → chọn từ viết bằng Kanji', kanji: true };
        return direction === 'forward'
            ? { prompt: item.vi, answer: item.kana, label: 'Nghĩa Việt → chọn từ bằng Kana', kanji: false }
            : { prompt: item.kana, answer: item.vi, label: 'Kana → chọn nghĩa Việt', kanji: false };
    }

    function questionFor(item, pool, config) {
        const target = fields(item, config.direction);
        const used = new Set([normal(target.answer)]);
        const wrong = [];
        for (const other of shuffled(pool)) {
            // Exclude readings, spellings and meanings equivalent to the target:
            // they must not become plausible "wrong" answers.
            if (other.id === item.id || ['kana', 'jp', 'vi'].some(key => normal(other[key]) === normal(item[key]))) continue;
            const candidate = fields(other, config.direction);
            if (normal(candidate.prompt) === normal(target.prompt) || used.has(normal(candidate.answer))) continue;
            used.add(normal(candidate.answer));
            wrong.push(candidate.answer);
            if (wrong.length === 3) break;
        }
        if (wrong.length !== 3) return null;
        return { id: item.id, options: shuffled([target.answer, ...wrong]), selected: null };
    }

    function save() {
        try {
            localStorage.setItem(KEY, JSON.stringify({ version: DATA.version, settings, session, updatedAt: Date.now() }));
            root.querySelector('#vkcSaveStatus').textContent = 'Đã lưu phiên kiểm tra trên trình duyệt này.';
        } catch (error) {
            root.querySelector('#vkcSaveStatus').textContent = 'Chưa lưu được phiên. Bạn vẫn có thể tiếp tục trong trang hiện tại.';
        }
    }

    function restore() {
        try {
            const saved = JSON.parse(localStorage.getItem(KEY) || 'null');
            if (!saved || saved.version !== DATA.version || !validSettings(saved.settings)) return;
            settings = { ...saved.settings, count: String(saved.settings.count) };
            const value = saved.session;
            if (!value || !validSettings(value.settings) || !Array.isArray(value.questions) || !value.questions.length) return;
            const config = value.settings;
            const allowedOptions = type => new Set(items.filter(item => belongs(item, config) && item.id.startsWith(type + ':'))
                .map(item => fields(item, config.direction).answer));
            const optionsByType = { kanji: allowedOptions('kanji'), vocab: allowedOptions('vocab') };
            const ids = new Set();
            for (const q of value.questions) {
                const item = byId.get(q.id);
                if (!item || !belongs(item, config) || ids.has(q.id)) return;
                ids.add(q.id);
                const type = q.id.split(':')[0];
                if (!Array.isArray(q.options) || q.options.length !== 4 ||
                    new Set(q.options.map(normal)).size !== 4 ||
                    !q.options.includes(fields(item, config.direction).answer) ||
                    q.options.some(option => !optionsByType[type].has(option)) ||
                    !(q.selected === null || (Number.isInteger(q.selected) && q.selected >= 0 && q.selected < 4))) return;
            }
            if (!Number.isInteger(value.index) || value.index < 0 || value.index > value.questions.length) return;
            if (value.questions.some((q, i) => i < value.index ? q.selected === null : i > value.index && q.selected !== null)) return;
            session = value;
        } catch (error) { /* An invalid snapshot must not inject out-of-scope items. */ }
    }

    function start(reviewOnly = false) {
        const pending = session && session.index < session.questions.length && session.questions.some(q => q.selected !== null);
        if (pending && !window.confirm('Bắt đầu lượt mới? Phiên kiểm tra từ vựng/Kanji hiện tại sẽ được thay thế.')) return;
        const config = reviewOnly && session ? { ...session.settings } : {
            lesson: root.querySelector('#vkcLesson').value,
            mode: root.querySelector('#vkcMode').value,
            count: root.querySelector('#vkcCount').value,
            direction: root.querySelector('#vkcDirection').value
        };
        const wrongIds = reviewOnly ? new Set(session.questions.filter(q =>
            q.options[q.selected] !== fields(byId.get(q.id), session.settings.direction).answer).map(q => q.id)) : null;
        const pools = {};
        for (const type of ['vocab', 'kanji']) {
            const pool = items.filter(item => belongs(item, config) && item.id.startsWith(type + ':'));
            const unique = new Set();
            pools[type] = shuffled(pool).filter(item => {
                if (wrongIds && !wrongIds.has(item.id)) return false;
                const key = normal(fields(item, config.direction).prompt);
                if (unique.has(key)) return false;
                unique.add(key);
                return true;
            }).map(item => questionFor(item, pool, config)).filter(Boolean);
        }
        // Interleave the two banks so a mixed 10/20-question round covers both.
        const combined = [];
        for (let i = 0; i < Math.max(pools.vocab.length, pools.kanji.length); i++) {
            if (pools.vocab[i]) combined.push(pools.vocab[i]);
            if (pools.kanji[i]) combined.push(pools.kanji[i]);
        }
        const limit = reviewOnly || config.count === 'all' ? combined.length : Number(config.count);
        settings = config;
        session = combined.length ? { settings: config, questions: shuffled(combined.slice(0, limit)), index: 0 } : null;
        save();
        renderQuestion();
    }

    function score() {
        return session.questions.filter(q => q.selected !== null &&
            q.options[q.selected] === fields(byId.get(q.id), session.settings.direction).answer).length;
    }

    function renderQuestion() {
        const card = root.querySelector('#vkcCard');
        const status = root.querySelector('#vkcStatus');
        if (!session) {
            status.textContent = '';
            card.innerHTML = '<p>Chọn bài, loại câu và hướng hỏi rồi bấm “Bắt đầu”. Số câu thực tế phụ thuộc bộ lọc; mỗi câu có bốn lựa chọn khác nhau.</p>';
            return;
        }
        const total = session.questions.length;
        const correct = score();
        if (session.index === total) {
            status.textContent = `Hoàn thành ${total} câu`;
            card.innerHTML = `<div class="vkc-finished"><h3>Kết quả: ${correct}/${total} (${Math.round(correct / total * 100)}%)</h3>
                <p>${total - correct} câu cần ôn lại. Điểm này độc lập với đề tổng hợp 71 câu.</p>
                <button type="button" id="vkcRetryWrong" ${correct === total ? 'disabled' : ''}>Ôn lại câu sai</button>
                <button type="button" id="vkcRestart">Làm lượt mới</button></div>`;
            card.querySelector('#vkcRetryWrong').addEventListener('click', () => start(true));
            card.querySelector('#vkcRestart').addEventListener('click', () => start());
            return;
        }
        const q = session.questions[session.index];
        const item = byId.get(q.id);
        const f = fields(item, session.settings.direction);
        const answered = q.selected !== null;
        status.textContent = `Câu ${session.index + 1}/${total} · Đúng ${correct} · ${session.settings.lesson === 'all' ? 'Bài 11–18' : session.settings.lesson}`;
        card.innerHTML = `<div class="vkc-question-meta"><span>${escape(item.lesson)}</span><span>${f.kanji ? 'Kanji' : 'Từ vựng'}</span></div>
            <div class="vkc-prompt-label">${escape(f.label)}</div>
            <div class="vkc-prompt ${f.kanji ? 'is-kanji' : ''}">${escape(f.prompt)}</div>
            ${f.kanji ? `<p class="vkc-meaning">Nghĩa: ${escape(item.vi)}</p>` : ''}
            <div class="vkc-options">${q.options.map((option, index) => {
                const cls = answered ? (option === f.answer ? ' is-correct' : index === q.selected ? ' is-wrong' : '') : '';
                return `<button type="button" class="vkc-option${cls}" data-index="${index}" ${answered ? 'disabled' : ''}>${index + 1}. ${escape(option)}</button>`;
            }).join('')}</div>
            <div class="vkc-feedback" aria-live="polite">${answered
                ? `${q.options[q.selected] === f.answer ? '✓ Đúng' : '✗ Chưa đúng'} — Đáp án: <strong>${escape(f.answer)}</strong><br>
                    ${escape(item.kana)} · ${escape(item.vi)} <button type="button" class="vkc-speak" aria-label="Nghe cách đọc đáp án">🔊 Nghe</button>` : ''}</div>
            <button type="button" class="vkc-next" ${answered ? '' : 'hidden'}>${session.index === total - 1 ? 'Xem kết quả' : 'Câu tiếp theo →'}</button>`;
        card.querySelectorAll('.vkc-option').forEach(button => button.addEventListener('click', () => {
            if (q.selected !== null) return;
            q.selected = Number(button.dataset.index);
            save();
            renderQuestion();
        }));
        card.querySelector('.vkc-speak')?.addEventListener('click', () => window.speakText?.(item.kana));
        card.querySelector('.vkc-next').addEventListener('click', () => {
            if (q.selected === null) return;
            session.index++;
            save();
            renderQuestion();
        });
    }

    function selectPanel(practice) {
        const panel = document.getElementById('fullExamPanel');
        if (practice && !panel.hidden) {
            previousExamRunning = typeof isTimerRunning !== 'undefined' && isTimerRunning;
            if (typeof stopTimer === 'function') stopTimer();
            if (typeof saveCurrentDraft === 'function') saveCurrentDraft();
            if (typeof updateModeUI === 'function') updateModeUI();
        }
        panel.hidden = practice;
        root.hidden = !practice;
        document.getElementById('showFullExam').setAttribute('aria-pressed', String(!practice));
        document.getElementById('showVocabCheck').setAttribute('aria-pressed', String(practice));
        if (!practice && previousExamRunning) {
            previousExamRunning = false;
            if (typeof startTimer === 'function') startTimer();
        }
        window.AudioEngine?.stop();
    }

    function init() {
        root.innerHTML = `<div class="vkc-header"><div><span class="vkc-eyebrow">A2.1 · BÀI 11–18</span>
            <h2>Kiểm tra Từ vựng & Kanji</h2>
            <p>Từ vựng chỉ A2-11–18 và viết bằng Kana. Phần Kanji chỉ dùng từ ghép có mọi chữ thuộc danh sách Kanji bài 11–18 (kể cả đáp án nhiễu).</p>
            <p>${DATA.vocab.length} mục từ vựng · ${DATA.kanji.length} mục Kanji hợp lệ · ${DATA.allowedKanji.length} chữ trong danh sách.</p>
            </div></div><div class="vkc-body">
            <p>Điểm riêng, không cộng vào đề tổng hợp. Đồng hồ đề tổng hợp tạm dừng khi mở phần này và tiếp tục khi quay lại.</p>
            <div class="vkc-settings">
            <label>Bài học<select id="vkcLesson"><option value="all">Tất cả bài 11–18</option>${DATA.lessons.map(l => `<option value="${l}">Bài ${l.slice(3)}</option>`).join('')}</select></label>
            <label>Loại câu<select id="vkcMode"><option value="mixed">Từ vựng + Kanji</option><option value="vocab">Từ vựng</option><option value="kanji">Kanji</option></select></label>
            <label>Hướng hỏi<select id="vkcDirection"><option value="forward">Việt → Kana / Kanji → Kana</option><option value="reverse">Kana → Việt / Kana → Kanji</option></select></label>
            <label>Số câu<select id="vkcCount"><option value="10">10 câu</option><option value="20">20 câu</option><option value="all">Tất cả phù hợp</option></select></label>
            <button type="button" class="vkc-start">Bắt đầu / Làm lượt mới</button></div>
            <p id="vkcSaveStatus" role="status"></p><div id="vkcStatus" class="vkc-status"></div><div id="vkcCard" class="vkc-card"></div></div>`;
        restore();
        for (const [id, key] of [['vkcLesson', 'lesson'], ['vkcMode', 'mode'], ['vkcDirection', 'direction'], ['vkcCount', 'count']]) {
            root.querySelector('#' + id).value = String(settings[key]);
        }
        root.querySelector('.vkc-start').addEventListener('click', () => start());
        // Reveal the anchor target before the browser performs its native scroll.
        document.querySelector('.exam-start-link')?.addEventListener('click', () => selectPanel(false));
        document.getElementById('showFullExam').addEventListener('click', () => {
            history.replaceState(null, '', location.pathname + location.search + '#' + currentExamCode);
            selectPanel(false);
        });
        document.getElementById('showVocabCheck').addEventListener('click', () => {
            history.replaceState(null, '', location.pathname + location.search + '#vocab-kanji-check');
            selectPanel(true);
        });
        window.addEventListener('hashchange', () => selectPanel(location.hash === '#vocab-kanji-check'));
        selectPanel(location.hash === '#vocab-kanji-check');
        renderQuestion();
    }

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();
})(window, document);
