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
    const icons = {
        arrow: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
        sound: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m11 5-6 4H2v6h3l6 4V5Z"/><path d="M15 8a6 6 0 0 1 0 8m3-11a10 10 0 0 1 0 14"/></svg>',
        settings: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 7h16M4 17h16"/><circle cx="9" cy="7" r="3" fill="white"/><circle cx="15" cy="17" r="3" fill="white"/></svg>'
    };
    const lessonName = lesson => lesson === 'all' ? 'Bài 11–18' : `Bài ${lesson.slice(3)}`;
    const modeName = mode => ({ mixed: 'Từ vựng + Kanji', vocab: 'Từ vựng', kanji: 'Kanji' })[mode];

    function updateDirectionLabels() {
        const mode = root.querySelector('#vkcMode').value;
        const labels = mode === 'kanji' ? ['Kanji → Kana', 'Kana → Kanji']
            : mode === 'vocab' ? ['Nghĩa Việt → Kana', 'Kana → Nghĩa Việt']
                : ['Nghĩa / Kanji → Kana', 'Kana → Nghĩa / Kanji'];
        root.querySelectorAll('#vkcDirection option').forEach((option, i) => { option.textContent = labels[i]; });
    }

    function focusQuestion() {
        const area = root.querySelector('.vkc-practice');
        area.querySelector('[tabindex="-1"]')?.focus({ preventScroll: true });
        const rect = area.getBoundingClientRect();
        if (rect.top < 80 || rect.bottom > window.innerHeight) {
            area.scrollIntoView({ block: 'start', behavior: 'instant' });
        }
    }

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
            root.querySelector('#vkcSaveStatus').textContent = 'Đã lưu tiến độ';
            root.querySelector('#vkcSaveStatus').classList.remove('vkc-save-error');
        } catch (error) {
            root.querySelector('#vkcSaveStatus').textContent = 'Chưa lưu được phiên. Bạn vẫn có thể tiếp tục trong trang hiện tại.';
            root.querySelector('#vkcSaveStatus').classList.add('vkc-save-error');
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
        root.querySelector('#vkcSettings').open = false;
        focusQuestion();
    }

    function score() {
        return session.questions.filter(q => q.selected !== null &&
            q.options[q.selected] === fields(byId.get(q.id), session.settings.direction).answer).length;
    }

    function renderQuestion() {
        const card = root.querySelector('#vkcCard');
        const status = root.querySelector('#vkcStatus');
        const summary = root.querySelector('#vkcSettingsSummary');
        summary.textContent = session
            ? `${lessonName(session.settings.lesson)} · ${modeName(session.settings.mode)} · ${session.questions.length} câu`
            : 'Chọn nội dung bạn muốn ôn hôm nay';
        root.querySelector('#vkcSettingsTitle').textContent = session ? 'Thiết lập lượt mới' : 'Thiết lập lượt kiểm tra';
        root.querySelector('.vkc-start').innerHTML = `${session ? 'Bắt đầu lượt mới' : 'Bắt đầu kiểm tra'} ${icons.arrow}`;
        if (!session) {
            status.textContent = '';
            root.querySelector('#vkcSettings').open = true;
            card.innerHTML = `<div class="vkc-empty">
                <span class="vkc-empty-mark" aria-hidden="true">Aa</span>
                <h3>Sẵn sàng ôn một chút?</h3>
                <p>Chọn thiết lập phía trên rồi bấm <strong>Bắt đầu kiểm tra</strong>.</p>
                <ul><li>4 lựa chọn mỗi câu</li><li>Xem đáp án ngay</li><li>Ôn lại câu sai</li></ul>
                </div>`;
            return;
        }
        const total = session.questions.length;
        const correct = score();
        const answeredCount = session.questions.filter(q => q.selected !== null).length;
        status.innerHTML = `<div class="vkc-progress-heading">
            <span>${session.index === total ? 'Đã hoàn thành' : `Câu <strong>${session.index + 1}</strong> <span class="vkc-muted">/ ${total}</span>`}</span>
            <span class="vkc-score"><span aria-hidden="true">✓</span> ${correct} đúng</span>
            </div><progress class="vkc-progress" value="${answeredCount}" max="${total}" aria-label="Số câu đã trả lời">${answeredCount}/${total}</progress>`;
        if (session.index === total) {
            const percent = Math.round(correct / total * 100);
            card.innerHTML = `<div class="vkc-finished">
                <div class="vkc-result-ring" style="--vkc-result:${percent}%"><span><strong>${percent}%</strong>chính xác</span></div>
                <span class="vkc-eyebrow">HOÀN THÀNH LƯỢT KIỂM TRA</span>
                <h3 tabindex="-1">${correct === total ? 'Bạn đã làm đúng tất cả!' : 'Thêm một lượt, nhớ thêm một chút.'}</h3>
                <p>Đúng <strong>${correct}/${total}</strong> câu${correct === total ? '.' : ` · Còn ${total - correct} câu cần ôn lại.`}</p>
                <div class="vkc-result-actions">
                    <button type="button" id="vkcRetryWrong" class="vkc-primary" ${correct === total ? 'disabled' : ''}>Ôn lại câu sai ${icons.arrow}</button>
                    <button type="button" id="vkcRestart" class="vkc-secondary">Làm lượt mới</button>
                </div>
                <p class="vkc-result-note">Kết quả này được lưu riêng với đề tổng hợp.</p>
                </div>`;
            card.querySelector('#vkcRetryWrong').addEventListener('click', () => start(true));
            card.querySelector('#vkcRestart').addEventListener('click', () => {
                root.querySelector('#vkcSettings').open = true;
                root.querySelector('#vkcLesson').focus();
            });
            return;
        }
        const q = session.questions[session.index];
        const item = byId.get(q.id);
        const f = fields(item, session.settings.direction);
        const answered = q.selected !== null;
        const isCorrect = answered && q.options[q.selected] === f.answer;
        const instruction = f.kanji
            ? session.settings.direction === 'forward' ? 'Chọn cách đọc đúng' : 'Chọn từ Kanji tương ứng'
            : session.settings.direction === 'forward' ? 'Chọn từ có nghĩa sau' : 'Chọn nghĩa đúng của từ';
        card.innerHTML = `<div class="vkc-question-meta"><span class="vkc-type">${f.kanji ? 'KANJI' : 'TỪ VỰNG'}</span><span>${escape(lessonName(item.lesson))}</span></div>
            <div class="vkc-question-content">
            <p class="vkc-prompt-label">${instruction}</p>
            <h3 tabindex="-1" class="vkc-prompt ${f.kanji ? 'is-kanji' : ''}" ${f.kanji || session.settings.direction === 'reverse' ? 'lang="ja"' : ''}>${escape(f.prompt)}</h3>
            ${f.kanji ? `<p class="vkc-meaning">${escape(item.vi)}</p>` : ''}
            </div>
            <div class="vkc-options">${q.options.map((option, index) => {
                const cls = answered ? (option === f.answer ? ' is-correct' : index === q.selected ? ' is-wrong' : '') : '';
                const mark = answered && option === f.answer ? '✓' : answered && index === q.selected ? '✕' : '';
                const label = mark === '✓' ? 'Đáp án đúng' : mark === '✕' ? 'Bạn đã chọn · Chưa đúng' : '';
                return `<button type="button" class="vkc-option${cls}" data-index="${index}" ${answered ? 'disabled' : ''}>
                    <span class="vkc-option-letter" aria-hidden="true">${'ABCD'[index]}</span>
                    <span class="vkc-option-copy">${escape(option)}${label ? `<small>${label}</small>` : ''}</span>
                    ${mark ? `<span class="vkc-option-mark" aria-hidden="true">${mark}</span>` : ''}
                    </button>`;
            }).join('')}</div>
            <div class="vkc-feedback ${answered ? isCorrect ? 'is-correct' : 'is-wrong' : ''}" role="status" ${answered ? '' : 'hidden'}>
                ${answered ? `<div><span class="vkc-feedback-label">${isCorrect ? '✓ Chính xác!' : 'Ôn lại từ này nhé'}</span>
                    <strong>${escape(f.answer)}</strong><p>${escape(f.answer === item.vi ? item.kana : item.vi)}</p></div>
                    <button type="button" class="vkc-speak" aria-label="Nghe cách đọc đáp án">${icons.sound} Nghe</button>` : ''}
            </div>
            <div class="vkc-question-footer"><span>${answered ? 'Đã lưu câu trả lời' : 'Chọn một đáp án để kiểm tra'}</span>
            <button type="button" class="vkc-next vkc-primary" ${answered ? '' : 'hidden'}>${session.index === total - 1 ? 'Xem kết quả' : 'Câu tiếp theo'} ${icons.arrow}</button></div>`;
        card.querySelectorAll('.vkc-option').forEach(button => button.addEventListener('click', () => {
            if (q.selected !== null) return;
            q.selected = Number(button.dataset.index);
            save();
            renderQuestion();
            card.querySelector('.vkc-next').focus({ preventScroll: true });
        }));
        card.querySelector('.vkc-speak')?.addEventListener('click', () => window.speakText?.(item.kana));
        card.querySelector('.vkc-next').addEventListener('click', () => {
            if (q.selected === null) return;
            session.index++;
            save();
            renderQuestion();
            focusQuestion();
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
        root.innerHTML = `<div class="vkc-header">
            <div><span class="vkc-eyebrow">LUYỆN NHỚ MỖI NGÀY</span>
            <h2>Từ vựng <span>&</span> Kanji</h2>
            <p>Ôn từng chút, nhớ lâu hơn. Chọn đáp án và nhận phản hồi ngay.</p></div>
            <span class="vkc-scope-badge">A2.1 <span aria-hidden="true">/</span> Bài 11–18</span>
            </div><div class="vkc-body">
            <details id="vkcSettings" class="vkc-setup" open>
            <summary><span class="vkc-settings-icon">${icons.settings}</span><span class="vkc-settings-copy">
                <strong id="vkcSettingsTitle">Thiết lập lượt kiểm tra</strong><span id="vkcSettingsSummary"></span>
                </span><span class="vkc-setup-chevron" aria-hidden="true">⌄</span></summary>
            <div class="vkc-setup-content"><div class="vkc-settings">
            <label>Bài học<select id="vkcLesson"><option value="all">Bài 11–18</option>${DATA.lessons.map(l => `<option value="${l}">Bài ${l.slice(3)}</option>`).join('')}</select></label>
            <label>Loại câu<select id="vkcMode"><option value="mixed">Trộn cả hai</option><option value="vocab">Từ vựng</option><option value="kanji">Kanji</option></select></label>
            <label>Hướng hỏi<select id="vkcDirection"><option value="forward"></option><option value="reverse"></option></select></label>
            <label>Độ dài lượt<select id="vkcCount"><option value="10">10 câu · Ôn nhanh</option><option value="20">20 câu · Luyện tập</option><option value="all">Toàn bộ câu phù hợp</option></select></label>
            </div><div class="vkc-setup-actions"><p>Số câu thực tế tùy bộ lọc, không lặp câu hỏi.</p>
            <button type="button" class="vkc-start vkc-primary">Bắt đầu kiểm tra ${icons.arrow}</button></div></div></details>
            <div class="vkc-practice"><div id="vkcStatus" class="vkc-status"></div><div id="vkcCard" class="vkc-card"></div>
            <div class="vkc-session-note"><span>Không tính giờ · Điểm riêng với đề tổng hợp</span><span id="vkcSaveStatus" role="status"></span></div></div>
            <details class="vkc-about" open><summary>Phạm vi nội dung &amp; lưu tiến độ</summary>
                <div><p><strong>Chỉ Marugoto A2 bài 11–18.</strong> ${DATA.vocab.length} mục từ vựng viết bằng Kana,
                ${DATA.kanji.length} mục từ ghép Kanji từ danh sách ${DATA.allowedKanji.length} chữ.
                Mọi chữ trong câu hỏi và đáp án Kanji đều được giới hạn trong danh sách này.</p>
                <p>Tiến độ tự lưu trên trình duyệt này. Điểm không cộng vào đề 71 câu.
                Đồng hồ đề tổng hợp tạm dừng khi mở phần này và tiếp tục khi quay lại trong cùng trang.</p></div>
            </details></div>`;
        restore();
        for (const [id, key] of [['vkcLesson', 'lesson'], ['vkcMode', 'mode'], ['vkcDirection', 'direction'], ['vkcCount', 'count']]) {
            root.querySelector('#' + id).value = String(settings[key]);
        }
        updateDirectionLabels();
        root.querySelector('#vkcMode').addEventListener('change', updateDirectionLabels);
        root.querySelector('#vkcSettings').open = !session;
        if (session) root.querySelector('#vkcSaveStatus').textContent = 'Đã khôi phục tiến độ';
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
