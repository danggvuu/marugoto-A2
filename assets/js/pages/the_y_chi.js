/* Explicit verb groups distinguish ambiguous kana such as きる. */
(() => {
    'use strict';
    const verbs = [
        { id: 'iku', ru: 'いく', kanji: '行く', vi: 'Đi', group: 1 },
        { id: 'kau', ru: 'かう', kanji: '買う', vi: 'Mua', group: 1 },
        { id: 'kaku', ru: 'かく', kanji: '書く', vi: 'Viết', group: 1 },
        { id: 'oyogu', ru: 'およぐ', kanji: '泳ぐ', vi: 'Bơi', group: 1 },
        { id: 'hanasu', ru: 'はなす', kanji: '話す', vi: 'Nói chuyện', group: 1 },
        { id: 'matsu', ru: 'まつ', kanji: '待つ', vi: 'Chờ', group: 1 },
        { id: 'asobu', ru: 'あそぶ', kanji: '遊ぶ', vi: 'Chơi', group: 1 },
        { id: 'nomu', ru: 'のむ', kanji: '飲む', vi: 'Uống', group: 1 },
        { id: 'yomu', ru: 'よむ', kanji: '読む', vi: 'Đọc', group: 1 },
        { id: 'kaeru', ru: 'かえる', kanji: '帰る', vi: 'Về nhà (nhóm 1)', group: 1 },
        { id: 'hairu', ru: 'はいる', kanji: '入る', vi: 'Vào (nhóm 1)', group: 1 },
        { id: 'hashiru', ru: 'はしる', kanji: '走る', vi: 'Chạy (nhóm 1)', group: 1 },
        { id: 'kiru-cut', ru: 'きる', kanji: '切る', vi: 'Cắt (nhóm 1)', group: 1 },
        { id: 'tsukuru', ru: 'つくる', kanji: '作る', vi: 'Làm, chế biến', group: 1 },
        { id: 'au', ru: 'あう', kanji: '会う', vi: 'Gặp', group: 1 },
        { id: 'taberu', ru: 'たべる', kanji: '食べる', vi: 'Ăn', group: 2 },
        { id: 'miru', ru: 'みる', kanji: '見る', vi: 'Xem', group: 2 },
        { id: 'neru', ru: 'ねる', kanji: '寝る', vi: 'Ngủ', group: 2 },
        { id: 'okiru', ru: 'おきる', kanji: '起きる', vi: 'Thức dậy', group: 2 },
        { id: 'kariru', ru: 'かりる', kanji: '借りる', vi: 'Mượn (nhóm 2)', group: 2 },
        { id: 'oriru', ru: 'おりる', kanji: '降りる', vi: 'Xuống xe (nhóm 2)', group: 2 },
        { id: 'kiru-wear', ru: 'きる', kanji: '着る', vi: 'Mặc áo (nhóm 2)', group: 2 },
        { id: 'kuru', ru: 'くる', kanji: '来る', vi: 'Đến', group: 3 },
        { id: 'suru', ru: 'する', kanji: 'する', vi: 'Làm', group: 3 },
        { id: 'benkyou', ru: 'べんきょうする', kanji: '勉強する', vi: 'Học', group: 3 },
        { id: 'motte-kuru', ru: 'もってくる', kanji: '持って来る', vi: 'Mang đến', group: 3 }
    ];
    const endings = { 'う': 'おう', 'く': 'こう', 'ぐ': 'ごう', 'す': 'そう', 'つ': 'とう', 'ぬ': 'のう', 'ぶ': 'ぼう', 'む': 'もう', 'る': 'ろう' };
    const storageKey = 'marugoto_volitional_v1';
    let state = { tab: 'vol-rules', group: 'all', current: verbs[0].id, answers: {} };
    window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;
    window.__MARUGOTO_CP_EXTRA_KEYS__ = [storageKey];
    const el = id => document.getElementById(id);
    const normalize = value => String(value || '').normalize('NFKC').replace(/[\s\u3000]+/g, '');

    function conjugate(verb) {
        if (verb.group === 2) return verb.ru.slice(0, -1) + 'よう';
        if (verb.group === 3) return verb.ru.endsWith('する') ? verb.ru.slice(0, -2) + 'しよう' : verb.ru.slice(0, -2) + 'こよう';
        return verb.ru.slice(0, -1) + endings[verb.ru.slice(-1)];
    }

    function save() {
        try { localStorage.setItem(storageKey, JSON.stringify(state)); } catch (error) {}
    }

    function setTab(tab) {
        if (!['vol-rules', 'vol-usage', 'vol-practice'].includes(tab)) return;
        state.tab = tab;
        document.querySelectorAll('[data-vol-tab]').forEach(button => {
            const active = button.dataset.volTab === tab;
            button.setAttribute('aria-selected', String(active));
            button.tabIndex = active ? 0 : -1;
            el(button.dataset.volTab).hidden = !active;
        });
        save();
    }

    function pool() {
        return verbs.filter(verb => state.group === 'all' || String(verb.group) === state.group);
    }

    function currentVerb() {
        return pool().find(verb => verb.id === state.current) || pool()[0];
    }

    function render(focus = false) {
        const list = pool();
        const verb = currentVerb();
        state.current = verb.id;
        const index = list.indexOf(verb);
        const answer = state.answers[verb.id] || {};
        const draft = typeof answer.draft === 'string' ? answer.draft : '';
        const value = normalize(draft);
        const correct = Boolean(answer.checked && value === conjugate(verb));
        const ready = Boolean((answer.checked && value) || answer.revealed);
        el('volVerb').textContent = verb.kanji;
        el('volReading').textContent = verb.ru;
        el('volMeaning').textContent = verb.vi;
        el('volPosition').textContent = `Câu ${index + 1} / ${list.length}`;
        el('volQuestionGroup').textContent = `NHÓM ${verb.group}`;
        if (el('volAnswer').value !== draft) el('volAnswer').value = draft;
        el('volAnswer').setAttribute('aria-invalid', String(Boolean(answer.checked && !correct)));
        el('volPracticeCard').classList.toggle('is-correct', correct);
        el('volPracticeCard').classList.toggle('is-wrong', Boolean(answer.checked && !correct));
        let feedback = 'Enter: chấm / câu tiếp.';
        if (answer.checked) {
            if (!value) feedback = 'Chưa có đáp án. Hãy nhập thể ý chí bằng hiragana.';
            else if (!/^[\u3041-\u3096ー]+$/u.test(value)) feedback = 'Hãy nhập hiragana, không dùng Kanji, katakana hoặc romaji.';
            else feedback = correct ? 'Đúng. Bạn đã chia đúng thể ý chí.' : 'Chưa đúng. Sửa đáp án hoặc xem quy tắc rồi thử lại.';
        } else if (answer.revealed) feedback = 'Đang xem đáp án; câu này chưa được tính đúng.';
        el('volFeedback').textContent = feedback;
        el('volCheck').textContent = ready ? (index === list.length - 1 ? 'Về câu đầu' : 'Câu tiếp') : 'Kiểm tra';
        el('volReveal').textContent = answer.revealed ? 'Ẩn đáp án' : 'Xem đáp án';
        el('volReveal').setAttribute('aria-expanded', String(Boolean(answer.revealed)));
        el('volExplanation').hidden = !answer.revealed;
        el('volExpected').textContent = `${verb.ru} → ${conjugate(verb)}`;
        el('volRuleHint').textContent = verb.group === 1
            ? `Nhóm 1: ${verb.ru.slice(-1)} → ${endings[verb.ru.slice(-1)]}. Đổi sang hàng お rồi thêm う.`
            : verb.group === 2 ? 'Nhóm 2: bỏ る, thêm よう.' : verb.ru.endsWith('する') ? 'Nhóm 3: する → しよう; giữ nguyên phần đứng trước する.' : 'Nhóm 3: くる → こよう; giữ nguyên phần đứng trước くる.';
        const checked = list.filter(item => state.answers[item.id]?.checked && normalize(state.answers[item.id].draft));
        const score = checked.filter(item => normalize(state.answers[item.id].draft) === conjugate(item)).length;
        el('volProgress').textContent = `Đã chấm ${checked.length}/${list.length} · Đúng ${score}/${list.length}`;
        el('volPrevious').disabled = index === 0;
        el('volNext').disabled = index === list.length - 1;
        if (focus) el('volAnswer').focus({ preventScroll: true });
    }

    function move(offset) {
        const list = pool();
        const index = list.indexOf(currentVerb());
        state.current = list[Math.max(0, Math.min(list.length - 1, index + offset))].id;
        render(true);
        save();
    }

    function check() {
        const verb = currentVerb();
        const answer = state.answers[verb.id] || {};
        if ((answer.checked && normalize(answer.draft)) || answer.revealed) {
            const index = pool().indexOf(verb);
            move(index === pool().length - 1 ? -index : 1);
            return;
        }
        state.answers[verb.id] = { draft: el('volAnswer').value, checked: true, revealed: false };
        render();
        save();
    }

    function init() {
        try {
            const saved = JSON.parse(localStorage.getItem(storageKey));
            if (saved && typeof saved === 'object') {
                if (['all', '1', '2', '3'].includes(saved.group)) state.group = saved.group;
                if (verbs.some(verb => verb.id === saved.current)) state.current = saved.current;
                if (['vol-rules', 'vol-usage', 'vol-practice'].includes(saved.tab)) state.tab = saved.tab;
                for (const verb of verbs) {
                    const answer = saved.answers?.[verb.id];
                    if (answer && typeof answer.draft === 'string') state.answers[verb.id] = { draft: answer.draft, checked: answer.checked === true, revealed: answer.revealed === true };
                }
            }
        } catch (error) {}
        document.querySelectorAll('[data-vol-tab]').forEach(button => {
            button.addEventListener('click', () => setTab(button.dataset.volTab));
            button.addEventListener('keydown', event => {
                const tabs = [...document.querySelectorAll('[data-vol-tab]')];
                let index = tabs.indexOf(button);
                if (event.key === 'ArrowRight') index = (index + 1) % tabs.length;
                else if (event.key === 'ArrowLeft') index = (index + tabs.length - 1) % tabs.length;
                else if (event.key === 'Home') index = 0;
                else if (event.key === 'End') index = tabs.length - 1;
                else return;
                event.preventDefault();
                setTab(tabs[index].dataset.volTab);
                tabs[index].focus({ preventScroll: true });
            });
        });
        document.querySelectorAll('[data-vol-audio]').forEach(button => button.addEventListener('click', () => window.speakJapanese?.(button.dataset.volAudio, button)));
        el('volGroupFilter').value = state.group;
        el('volGroupFilter').addEventListener('change', event => {
            state.group = event.target.value;
            state.current = pool()[0].id;
            render();
            save();
        });
        el('volAnswer').addEventListener('input', () => {
            state.answers[currentVerb().id] = { draft: el('volAnswer').value, checked: false, revealed: false };
            render();
            save();
        });
        el('volAnswer').addEventListener('keydown', event => {
            if (event.key === 'Enter' && !event.shiftKey && !event.isComposing && event.keyCode !== 229) {
                event.preventDefault();
                check();
            }
        });
        el('volCheck').addEventListener('click', check);
        el('volReveal').addEventListener('click', () => {
            const verb = currentVerb();
            const answer = state.answers[verb.id] || { draft: el('volAnswer').value };
            state.answers[verb.id] = { ...answer, revealed: !answer.revealed };
            render();
            save();
        });
        el('volListen').addEventListener('click', () => window.speakJapanese?.(conjugate(currentVerb()), el('volListen')));
        el('volPrevious').addEventListener('click', () => move(-1));
        el('volNext').addEventListener('click', () => move(1));
        el('volReset').addEventListener('click', () => {
            if (!window.confirm('Xóa toàn bộ đáp án luyện thể ý chí? Các bài học khác được giữ nguyên.')) return;
            state.answers = {};
            state.current = pool()[0].id;
            render();
            save();
        });
        render();
        setTab(state.tab);
    }

    document.addEventListener('DOMContentLoaded', init);
})();
