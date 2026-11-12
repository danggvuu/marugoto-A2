/**
 * MARUGOTO A1-A2 GLOBAL CHECKPOINT SYNC ENGINE (assets/js/checkpoint-sync.js)
 * Đồng bộ hóa tự động lưu & khôi phục tiến độ (checkpoint) qua localStorage cho toàn bộ dự án:
 * - Cung cấp API chuẩn window.MarugotoCheckpoint cho các trang có engine phức tạp.
 * - Tự động lưu & khôi phục Tab đang mở, Input/Textarea/Select/Radio/Checkbox, kết quả Chấm điểm,
 *   lựa chọn Quiz/Hội thoại/Từ đã thuộc trên các trang tĩnh & bán tĩnh.
 * - Hiển thị thanh trạng thái nhỏ gọn (góc dưới trái) + nút "Xóa checkpoint trang" khi muốn làm lại từ đầu.
 */
(function () {
    'use strict';

    if (window.__MARUGOTO_CHECKPOINT_LOADED__) return;
    window.__MARUGOTO_CHECKPOINT_LOADED__ = true;

    // 1. TÍNH KHÓA CHUẨN HÓA THEO ĐƯỜNG DẪN TRANG
    function resolvePageId() {
        const pathname = window.location.pathname || '';
        const href = window.location.href || '';
        const parts = pathname.split('/').filter(Boolean);
        let file = parts[parts.length - 1] || 'index.html';
        if (!file.includes('.html')) file = 'index.html';

        if (pathname.includes('/lessons/') || href.includes('/lessons/')) {
            return 'lessons/' + file;
        }
        if (pathname.includes('/tests/') || href.includes('/tests/')) {
            return 'tests/' + file;
        }
        return file;
    }

    const PAGE_ID = resolvePageId();
    const CP_PREFIX = 'marugoto_cp_v1::' + PAGE_ID;

    function getKey(slot) {
        return CP_PREFIX + '::' + slot;
    }

    function safeSave(slot, data) {
        try {
            localStorage.setItem(getKey(slot), JSON.stringify({ t: Date.now(), d: data }));
            notifySaved();
            return true;
        } catch (e) {
            return false;
        }
    }

    function safeLoad(slot, fallback) {
        try {
            const raw = localStorage.getItem(getKey(slot));
            if (!raw) return fallback;
            const parsed = JSON.parse(raw);
            return parsed && 'd' in parsed ? parsed.d : fallback;
        } catch (e) {
            return fallback;
        }
    }

    function safeRemove(slot) {
        try {
            localStorage.removeItem(getKey(slot));
        } catch (e) {}
    }

    // 2. THANH TRẠNG THÁI CHECKPOINT TOÀN CỤC (#mrgCheckpointBar)
    let pillEl = null;
    let statusTextEl = null;
    let lastSaveTimer = null;

    function injectStyles() {
        if (document.getElementById('mrgCheckpointStyles')) return;
        const st = document.createElement('style');
        st.id = 'mrgCheckpointStyles';
        st.textContent = `
            #mrgCheckpointBar {
                position: fixed;
                bottom: 14px;
                left: 14px;
                z-index: 985;
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: rgba(15, 23, 42, 0.92);
                backdrop-filter: blur(8px);
                color: #f8fafc;
                padding: 6px 10px 6px 12px;
                border-radius: 999px;
                font-family: system-ui, -apple-system, sans-serif;
                font-size: 0.78rem;
                font-weight: 600;
                box-shadow: 0 6px 20px rgba(15, 23, 42, 0.25);
                border: 1px solid rgba(255, 255, 255, 0.14);
                transition: transform 0.2s ease, opacity 0.2s ease;
            }
            #mrgCheckpointBar .mrg-cp-dot {
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: #34d399;
                flex-shrink: 0;
            }
            #mrgCheckpointBar.is-flashing .mrg-cp-dot {
                background: #a7f3d0;
                box-shadow: 0 0 8px #34d399;
            }
            #mrgCheckpointBar .mrg-cp-reset {
                border: 1px solid rgba(255, 255, 255, 0.22);
                background: rgba(255, 255, 255, 0.1);
                color: #fda4af;
                padding: 2px 8px;
                border-radius: 999px;
                font-size: 0.73rem;
                font-weight: 700;
                cursor: pointer;
                transition: background 0.15s;
            }
            #mrgCheckpointBar .mrg-cp-reset:hover {
                background: rgba(225, 29, 72, 0.35);
                color: #ffffff;
            }
            @media (max-width: 640px) {
                #mrgCheckpointBar {
                    bottom: 10px;
                    left: 10px;
                    font-size: 0.72rem;
                    padding: 5px 8px 5px 10px;
                }
            }
            @media print {
                #mrgCheckpointBar { display: none !important; }
            }
        `;
        document.head.appendChild(st);
    }

    function ensurePill() {
        if (pillEl && document.body && document.body.contains(pillEl)) return pillEl;
        if (!document.body) return null;
        injectStyles();

        pillEl = document.createElement('div');
        pillEl.id = 'mrgCheckpointBar';
        pillEl.innerHTML = `
            <span class="mrg-cp-dot" aria-hidden="true"></span>
            <span id="mrgCpText">💾 Đã bật lưu tiến độ</span>
            <button type="button" class="mrg-cp-reset" id="mrgCpResetBtn" title="Xóa toàn bộ tiến độ đã lưu trên trang này để làm lại từ đầu">🔄 Xóa checkpoint</button>
        `;
        document.body.appendChild(pillEl);
        statusTextEl = pillEl.querySelector('#mrgCpText');

        const resetBtn = pillEl.querySelector('#mrgCpResetBtn');
        if (resetBtn) {
            resetBtn.addEventListener('click', function () {
                clearPageCheckpoint(true);
            });
        }
        return pillEl;
    }

    function formatTime(ts) {
        const d = ts ? new Date(ts) : new Date();
        const pad = n => String(n).padStart(2, '0');
        return `${pad(d.getHours())}:${pad(d.getMinutes())}`;
    }

    function notifySaved(customLabel) {
        ensurePill();
        if (!statusTextEl) return;
        statusTextEl.textContent = customLabel || `💾 Đã lưu (${formatTime()})`;
        if (pillEl) {
            pillEl.classList.add('is-flashing');
            clearTimeout(lastSaveTimer);
            lastSaveTimer = setTimeout(() => {
                if (pillEl) pillEl.classList.remove('is-flashing');
            }, 900);
        }
    }

    function clearPageCheckpoint(askConfirm) {
        if (askConfirm && !window.confirm('Bạn có chắc muốn xóa checkpoint tiến độ đã lưu trên trang này và làm lại từ đầu không?')) {
            return;
        }
        try {
            const toRemove = [];
            for (let i = 0; i < localStorage.length; i++) {
                const k = localStorage.key(i);
                if (k && k.startsWith(CP_PREFIX + '::')) {
                    toRemove.push(k);
                }
            }
            if (Array.isArray(window.__MARUGOTO_CP_EXTRA_KEYS__)) {
                window.__MARUGOTO_CP_EXTRA_KEYS__.forEach(k => toRemove.push(k));
            }
            toRemove.forEach(k => localStorage.removeItem(k));
        } catch (e) {}

        if (typeof window.__MARUGOTO_ON_RESET__ === 'function') {
            window.__MARUGOTO_ON_RESET__();
        } else {
            window.location.reload();
        }
    }

    // Công khai API dùng chung
    window.MarugotoCheckpoint = {
        pageId: PAGE_ID,
        prefix: CP_PREFIX,
        getKey,
        save: safeSave,
        load: safeLoad,
        remove: safeRemove,
        notifySaved,
        clearPage: () => clearPageCheckpoint(true),
        silentClearPage: () => clearPageCheckpoint(false)
    };

    // 3. TỰ ĐỘNG ĐỒNG BỘ HÓA DOM (NẾU TRANG KHÔNG TẮT CHẾ ĐỘ AUTO DOM)
    let isRestoring = false;
    const restoredInputKeys = new Set();

    function withSilentUI(fn) {
        const origSpeak = window.speechSynthesis ? window.speechSynthesis.speak.bind(window.speechSynthesis) : null;
        const origSpeakText = window.speakText;
        const origSpeakJp = window.speakJapanese;
        const origAudioSpeak = window.audioEngine && window.audioEngine.speak;
        const origAudioCap = window.AudioEngine && window.AudioEngine.speak;
        const origScrollTo = window.scrollTo;
        const origScrollIntoView = Element.prototype.scrollIntoView;
        const origAlert = window.alert;

        try {
            if (window.speechSynthesis) window.speechSynthesis.speak = function () {};
            if (typeof window.speakText === 'function') window.speakText = function () {};
            if (typeof window.speakJapanese === 'function') window.speakJapanese = function () {};
            if (window.audioEngine && typeof window.audioEngine.speak === 'function') window.audioEngine.speak = function () {};
            if (window.AudioEngine && typeof window.AudioEngine.speak === 'function') window.AudioEngine.speak = function () {};
            window.scrollTo = function () {};
            Element.prototype.scrollIntoView = function () {};
            window.alert = function () {};
            return fn();
        } finally {
            setTimeout(() => {
                if (window.speechSynthesis && origSpeak) window.speechSynthesis.speak = origSpeak;
                if (origSpeakText) window.speakText = origSpeakText;
                if (origSpeakJp) window.speakJapanese = origSpeakJp;
                if (window.audioEngine && origAudioSpeak) window.audioEngine.speak = origAudioSpeak;
                if (window.AudioEngine && origAudioCap) window.AudioEngine.speak = origAudioCap;
                window.scrollTo = origScrollTo;
                Element.prototype.scrollIntoView = origScrollIntoView;
                window.alert = origAlert;
            }, 60);
        }
    }

    function getFieldStorageKey(el, domIdx) {
        if (!el) return null;
        if (el.hasAttribute('data-cp-ignore')) return null;
        if (el.closest('[data-cp-ignore]')) return null;
        if (el.id === 'tpCardInput' || el.classList.contains('tp-table-input')) return null;
        if (el.classList.contains('search-input') || el.type === 'search') return null;
        const ph = (el.getAttribute('placeholder') || '').toLowerCase();
        if (ph.includes('tìm kiếm') || ph.includes('tim kiem')) return null;

        if (el.type === 'radio' && el.name) {
            return 'radio::' + el.name;
        }
        if (el.id) return 'id::' + el.id;
        if (el.name) return 'name::' + el.name + '::' + domIdx;
        return 'idx::' + el.tagName + '::' + domIdx;
    }

    function collectAndSaveInputs() {
        if (isRestoring || window.__MARUGOTO_NATIVE_DOM_DISABLED__ || window.__MARUGOTO_DISABLE_AUTO_INPUTS__) return;
        const fields = Array.from(document.querySelectorAll('input, textarea, select'));
        const existing = safeLoad('inputs', {});
        let changed = false;
        fields.forEach((el, idx) => {
            const key = getFieldStorageKey(el, idx);
            if (!key) return;
            if (el.type === 'radio') {
                if (el.checked) {
                    if (existing[key] !== el.value) {
                        existing[key] = el.value;
                        changed = true;
                    }
                }
            } else if (el.type === 'checkbox') {
                if (existing[key] !== el.checked) {
                    existing[key] = el.checked;
                    changed = true;
                }
            } else {
                if (existing[key] !== el.value) {
                    existing[key] = el.value;
                    changed = true;
                }
            }
        });
        if (changed) {
            safeSave('inputs', existing);
        }
    }

    function restoreInputs() {
        if (window.__MARUGOTO_NATIVE_DOM_DISABLED__ || window.__MARUGOTO_DISABLE_AUTO_INPUTS__) return false;
        const saved = safeLoad('inputs', null);
        if (!saved || typeof saved !== 'object') return false;
        const fields = Array.from(document.querySelectorAll('input, textarea, select'));
        let didRestore = false;

        isRestoring = true;
        try {
            fields.forEach((el, idx) => {
                const key = getFieldStorageKey(el, idx);
                if (!key || !(key in saved) || restoredInputKeys.has(key + ':' + idx)) return;
                const val = saved[key];

                if (el.type === 'radio') {
                    if (el.value === val && !el.checked) {
                        el.checked = true;
                        didRestore = true;
                    }
                    restoredInputKeys.add(key + ':' + idx);
                } else if (el.type === 'checkbox') {
                    if (typeof val === 'boolean' && el.checked !== val) {
                        el.checked = val;
                        el.dispatchEvent(new Event('change', { bubbles: true }));
                        didRestore = true;
                    }
                    restoredInputKeys.add(key + ':' + idx);
                } else if (typeof val === 'string' && val !== '' && el.value !== val) {
                    el.value = val;
                    if (el.id && el.id.startsWith('input_') && typeof window.checkVerbInput === 'function') {
                        const vid = Number(el.id.replace('input_', '')) || el.id.replace('input_', '');
                        window.checkVerbInput(vid);
                    }
                    didRestore = true;
                    restoredInputKeys.add(key + ':' + idx);
                } else if (typeof val === 'string' && el.value === val && val !== '') {
                    restoredInputKeys.add(key + ':' + idx);
                }
            });
        } finally {
            isRestoring = false;
        }
        return didRestore;
    }

    function saveTabChoice(btn) {
        if (isRestoring || window.__MARUGOTO_NATIVE_DOM_DISABLED__ || window.__MARUGOTO_DISABLE_AUTO_TABS__) return;
        const allTabs = Array.from(document.querySelectorAll('.tab-btn, .nav-tab-btn, .mode-tab-btn, .tab-nav button, [role="tab"]'));
        const idx = allTabs.indexOf(btn);
        const oc = (btn.getAttribute('onclick') || '').trim();
        safeSave('tab', { oc, idx, text: (btn.textContent || '').trim().slice(0, 40) });
    }

    function restoreTabChoice() {
        if (window.__MARUGOTO_NATIVE_DOM_DISABLED__ || window.__MARUGOTO_DISABLE_AUTO_TABS__) return false;
        // Nếu URL hash chỉ định tab rõ ràng thì ưu tiên URL
        if (window.location.hash && window.location.hash.length > 1) return false;
        const saved = safeLoad('tab', null);
        if (!saved) return false;

        const allTabs = Array.from(document.querySelectorAll('.tab-btn, .nav-tab-btn, .mode-tab-btn, .tab-nav button, [role="tab"]'));
        let targetBtn = null;
        if (saved.oc) {
            targetBtn = allTabs.find(b => (b.getAttribute('onclick') || '').trim() === saved.oc);
        }
        if (!targetBtn && typeof saved.idx === 'number' && allTabs[saved.idx]) {
            targetBtn = allTabs[saved.idx];
        }
        if (!targetBtn || targetBtn.classList.contains('active')) return false;

        isRestoring = true;
        try {
            withSilentUI(() => {
                targetBtn.click();
            });
            return true;
        } finally {
            isRestoring = false;
        }
    }

    const CLICK_QUIZ_SELECTOR = [
        'button.quiz-opt',
        'button.quiz-opt-btn',
        '[onclick*="selectAnswer("]',
        '[onclick*="selectQuizAnswer("]',
        '[onclick*="checkMiniQuiz("]',
        '[onclick*="answerNpbsChallenge("]',
        '[onclick*="selectSpeedTestAnswer("]',
        '[onclick*="toggleLearned("]'
    ].join(', ');

    function getClickSig(btn) {
        const oc = (btn.getAttribute('onclick') || '').replace(/\s+/g, '');
        if (oc) return 'oc::' + oc;
        const all = Array.from(document.querySelectorAll(CLICK_QUIZ_SELECTOR));
        return 'qidx::' + all.indexOf(btn);
    }

    function recordQuizClick(btn) {
        if (isRestoring || window.__MARUGOTO_NATIVE_DOM_DISABLED__) return;
        const sig = getClickSig(btn);
        const list = safeLoad('clicks', []);
        if (!list.includes(sig)) {
            list.push(sig);
            safeSave('clicks', list);
        } else if (sig.includes('toggleLearned(')) {
            // toggleLearned can toggle ON/OFF cleanly
            const nextList = list.filter(x => x !== sig);
            safeSave('clicks', nextList);
        }
    }

    function recordDialogueClick(btn) {
        if (isRestoring || window.__MARUGOTO_NATIVE_DOM_DISABLED__) return;
        const oc = (btn.getAttribute('onclick') || '').replace(/\s+/g, '');
        if (!oc) return;
        const list = safeLoad('dialogue', []);
        if (!list.includes(oc)) {
            list.push(oc);
            safeSave('dialogue', list);
        }
    }

    function restoreQuizAndDialogue() {
        if (window.__MARUGOTO_NATIVE_DOM_DISABLED__) return false;
        let didAny = false;

        const clicks = safeLoad('clicks', []);
        if (Array.isArray(clicks) && clicks.length) {
            isRestoring = true;
            try {
                withSilentUI(() => {
                    const all = Array.from(document.querySelectorAll(CLICK_QUIZ_SELECTOR));
                    clicks.forEach(sig => {
                        let btn = null;
                        if (sig.startsWith('oc::')) {
                            const targetOc = sig.slice(4);
                            btn = all.find(b => (b.getAttribute('onclick') || '').replace(/\s+/g, '') === targetOc);
                        } else if (sig.startsWith('qidx::')) {
                            btn = all[Number(sig.slice(6))];
                        }
                        if (btn && !btn.disabled) {
                            const isLearnedToggle = sig.includes('toggleLearned(');
                            if (isLearnedToggle && btn.classList.contains('active')) return;
                            if (!isLearnedToggle && (btn.classList.contains('correct') || btn.classList.contains('wrong'))) return;
                            btn.click();
                            didAny = true;
                        }
                    });
                });
            } finally {
                isRestoring = false;
            }
        }

        // Graded form banner replay (index.html, the_ru.html, the_ta.html, the_nai.html, L6-7-8, kanji_a2)
        const gradedFn = safeLoad('graded', null);
        if (gradedFn && typeof window[gradedFn] === 'function') {
            isRestoring = true;
            try {
                withSilentUI(() => {
                    window[gradedFn]();
                });
                didAny = true;
            } finally {
                isRestoring = false;
            }
        }

        // Sequential dialogue replay via #chatOptionsGrid if present
        const dialogueQueue = safeLoad('dialogue', []);
        if (Array.isArray(dialogueQueue) && dialogueQueue.length) {
            const grid = document.getElementById('chatOptionsGrid');
            if (grid) {
                let dIdx = 0;
                const replayNextDialogue = () => {
                    if (dIdx >= dialogueQueue.length) return;
                    const want = dialogueQueue[dIdx];
                    const btn = Array.from(grid.querySelectorAll('[onclick*="chooseDialogue("]'))
                        .find(b => (b.getAttribute('onclick') || '').replace(/\s+/g, '') === want);
                    if (btn) {
                        dIdx++;
                        isRestoring = true;
                        try {
                            withSilentUI(() => {
                                btn.click();
                            });
                        } finally {
                            isRestoring = false;
                        }
                        didAny = true;
                    }
                };
                const obs = new MutationObserver(() => {
                    if (dIdx >= dialogueQueue.length) {
                        obs.disconnect();
                        return;
                    }
                    replayNextDialogue();
                });
                obs.observe(grid, { childList: true, subtree: true });
                replayNextDialogue();
                setTimeout(() => obs.disconnect(), 8000);
            }
        }
        return didAny;
    }

    function attachGlobalListeners() {
        // Save inputs live (capture phase so dynamic rows are covered)
        let inputDebounce = null;
        const scheduleInputSave = () => {
            if (isRestoring) return;
            clearTimeout(inputDebounce);
            inputDebounce = setTimeout(collectAndSaveInputs, 120);
        };
        document.addEventListener('input', scheduleInputSave, true);
        document.addEventListener('change', scheduleInputSave, true);

        // Save clicks on tabs, quizzes, grade buttons, reset buttons
        document.addEventListener('click', function (e) {
            if (isRestoring) return;
            const target = e.target && e.target.closest ? e.target.closest('button, a, [role="tab"]') : null;
            if (!target) return;

            if (target.closest('#mrgCheckpointBar') || target.closest('.global-hub-nav-wrapper')) return;

            const oc = (target.getAttribute('onclick') || '');

            // Reset buttons should clear saved state cleanly
            if (/resetQuiz|resetExercise|resetAllInputs|resetTypingExercise|resetAllExam/i.test(oc)) {
                if (/resetQuiz/i.test(oc)) {
                    safeRemove('clicks');
                } else if (/resetExercise|resetAllInputs|resetTypingExercise/i.test(oc)) {
                    safeRemove('inputs');
                    safeRemove('graded');
                    safeRemove('clicks');
                }
                notifySaved('🔄 Đã làm mới phần vừa reset');
                return;
            }

            if (/^(gradeAll|gradeAllInputs|gradeTest|gradeTypingExercise)\s*\(/i.test(oc.trim())) {
                const fnName = oc.trim().split('(')[0].trim();
                collectAndSaveInputs();
                safeSave('graded', fnName);
                return;
            }

            if (target.matches('.tab-btn, .nav-tab-btn, .mode-tab-btn, .tab-nav button, [role="tab"]')) {
                saveTabChoice(target);
                return;
            }

            if (target.matches(CLICK_QUIZ_SELECTOR)) {
                recordQuizClick(target);
                return;
            }

            if (target.matches('[onclick*="chooseDialogue("]')) {
                recordDialogueClick(target);
                return;
            }
        }, true);
    }

    function bootCheckpointSync() {
        ensurePill();
        attachGlobalListeners();

        // Kiểm tra xem trang đã có dữ liệu lưu trước đó chưa
        let hasSavedState = false;
        try {
            for (let i = 0; i < localStorage.length; i++) {
                const k = localStorage.key(i);
                if (k && (k.startsWith(CP_PREFIX + '::') || (Array.isArray(window.__MARUGOTO_CP_EXTRA_KEYS__) && window.__MARUGOTO_CP_EXTRA_KEYS__.includes(k)))) {
                    hasSavedState = true;
                    break;
                }
            }
        } catch (e) {}

        if (window.__MARUGOTO_NATIVE_DOM_DISABLED__) {
            if (hasSavedState) {
                notifySaved('✅ Đã khôi phục tiến độ');
            }
            return;
        }

        // Trì hoãn nhẹ để script trang kịp render table/quiz trước khi khôi phục
        setTimeout(() => {
            const tabOk = restoreTabChoice();
            const inpOk = restoreInputs();
            const quizOk = restoreQuizAndDialogue();
            // Lần quét bổ sung cho bảng render chậm (hoặc tab vừa mở)
            setTimeout(() => {
                const inpOk2 = restoreInputs();
                const quizOk2 = restoreQuizAndDialogue();
                if (tabOk || inpOk || quizOk || inpOk2 || quizOk2 || hasSavedState) {
                    notifySaved('✅ Đã khôi phục tiến độ');
                }
            }, 140);
        }, 50);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', bootCheckpointSync);
    } else {
        bootCheckpointSync();
    }
})();
