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
    let lastSavedTimeStr = '--:--';

    function injectStyles() {
        if (document.getElementById('mrgCheckpointStyles')) return;
        const st = document.createElement('style');
        st.id = 'mrgCheckpointStyles';
        st.textContent = `
            #mrgCheckpointBar {
                position: fixed;
                bottom: max(12px, env(safe-area-inset-bottom));
                left: max(12px, env(safe-area-inset-left));
                z-index: 985;
                display: inline-flex;
                align-items: center;
                gap: 7px;
                background: rgba(15, 23, 42, 0.88);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                color: #f8fafc;
                padding: 5px 10px 5px 10px;
                border-radius: 999px;
                font-family: system-ui, -apple-system, sans-serif;
                font-size: 0.74rem;
                font-weight: 600;
                box-shadow: 0 4px 14px rgba(15, 23, 42, 0.18);
                border: 1px solid rgba(255, 255, 255, 0.12);
                transition: transform 0.2s ease, opacity 0.2s ease, background 0.2s ease;
                cursor: pointer;
                user-select: none;
            }
            #mrgCheckpointBar:hover {
                background: rgba(15, 23, 42, 0.96);
                transform: translateY(-1px);
            }
            #mrgCheckpointBar .mrg-cp-dot {
                width: 7px;
                height: 7px;
                border-radius: 50%;
                background: #10b981;
                flex-shrink: 0;
                transition: background-color 0.2s ease;
            }
            #mrgCheckpointBar.is-saving .mrg-cp-dot {
                background: #f59e0b;
                box-shadow: 0 0 6px #f59e0b;
            }
            #mrgCheckpointBar.is-error .mrg-cp-dot {
                background: #ef4444;
                box-shadow: 0 0 6px #ef4444;
            }
            #mrgCheckpointBar .mrg-cp-menu-btn {
                background: transparent;
                border: none;
                color: #94a3b8;
                font-size: 0.75rem;
                cursor: pointer;
                padding: 1px 3px;
                line-height: 1;
                border-radius: 4px;
                transition: color 0.15s ease;
            }
            #mrgCheckpointBar:hover .mrg-cp-menu-btn {
                color: #ffffff;
            }
            /* Checkpoint Reset Modal */
            .mrg-cp-modal-backdrop {
                position: fixed;
                top: 0; left: 0; right: 0; bottom: 0;
                background: rgba(15, 23, 42, 0.5);
                backdrop-filter: blur(4px);
                z-index: 999998;
            }
            .mrg-cp-modal-card {
                position: fixed;
                top: 50%; left: 50%;
                transform: translate(-50%, -50%);
                background: #ffffff;
                color: #0f172a;
                border-radius: 16px;
                padding: 22px 24px;
                width: 90%;
                max-width: 400px;
                box-shadow: 0 20px 45px rgba(0, 0, 0, 0.22);
                border: 1px solid #e2e8f0;
                z-index: 999999;
                font-family: system-ui, -apple-system, sans-serif;
            }
            .mrg-cp-modal-card h3 {
                margin: 0 0 10px 0;
                font-size: 1.05rem;
                font-weight: 800;
                color: #0f172a;
            }
            .mrg-cp-modal-card p {
                margin: 0 0 14px 0;
                font-size: 0.86rem;
                color: #475569;
                line-height: 1.5;
            }
            .mrg-cp-modal-actions {
                display: flex;
                flex-direction: column;
                gap: 8px;
                margin-top: 18px;
            }
            .mrg-cp-btn-danger {
                background: #fee2e2;
                color: #b91c1c;
                border: 1px solid #fca5a5;
                padding: 10px 14px;
                border-radius: 10px;
                font-size: 0.86rem;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.15s ease;
            }
            .mrg-cp-btn-danger:hover {
                background: #ef4444;
                color: #ffffff;
            }
            .mrg-cp-btn-cancel {
                background: #f1f5f9;
                color: #334155;
                border: 1px solid #cbd5e1;
                padding: 8px 14px;
                border-radius: 10px;
                font-size: 0.86rem;
                font-weight: 600;
                cursor: pointer;
            }
            @media (max-width: 640px) {
                #mrgCheckpointBar {
                    bottom: max(8px, env(safe-area-inset-bottom));
                    left: max(8px, env(safe-area-inset-left));
                    font-size: 0.7rem;
                    padding: 4px 8px;
                }
            }
            @media print {
                #mrgCheckpointBar, .mrg-cp-modal-backdrop, .mrg-cp-modal-card { display: none !important; }
            }
        `;
        document.head.appendChild(st);
    }

    function openCheckpointModal() {
        let modal = document.getElementById('mrgCpModal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'mrgCpModal';
            modal.innerHTML = `
                <div class="mrg-cp-modal-backdrop" onclick="window.MarugotoCheckpoint.closeModal()"></div>
                <div class="mrg-cp-modal-card" role="dialog" aria-modal="true" aria-labelledby="mrgCpModalTitle">
                    <h3 id="mrgCpModalTitle">💾 Lưu Tiến Độ Học Tập</h3>
                    <p>Tiến độ làm bài, các ô đã nhập và kết quả chấm điểm trên trang này đang được tự động lưu vào bộ nhớ máy.</p>
                    <p style="font-size:0.8rem; color:#64748b; background:#f8fafc; padding:8px 10px; border-radius:8px; border:1px solid #e2e8f0;">
                        ⏱️ Lần lưu gần nhất: <strong id="mrgCpModalTime" style="color:#0f172a;">${lastSavedTimeStr}</strong>
                    </p>
                    <div class="mrg-cp-modal-actions">
                        <button type="button" class="mrg-cp-btn-danger" id="mrgCpResetBtnModal">🔄 Làm lại từ đầu (Xóa tiến độ trang này)</button>
                        <button type="button" class="mrg-cp-btn-cancel" onclick="window.MarugotoCheckpoint.closeModal()">Đóng cửa sổ</button>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);
            const btnReset = modal.querySelector('#mrgCpResetBtnModal');
            if (btnReset) {
                btnReset.addEventListener('click', function () {
                    closeCheckpointModal();
                    clearPageCheckpoint(true);
                });
            }
        }
        const timeEl = document.getElementById('mrgCpModalTime');
        if (timeEl) timeEl.textContent = lastSavedTimeStr;
        modal.style.display = 'block';
    }

    function closeCheckpointModal() {
        const modal = document.getElementById('mrgCpModal');
        if (modal) modal.style.display = 'none';
    }

    function ensurePill() {
        if (pillEl && document.body && document.body.contains(pillEl)) return pillEl;
        if (!document.body) return null;
        injectStyles();

        pillEl = document.createElement('div');
        pillEl.id = 'mrgCheckpointBar';
        pillEl.title = 'Bấm để xem thông tin lưu tiến độ hoặc đặt lại bài học';
        pillEl.innerHTML = `
            <span class="mrg-cp-dot" aria-hidden="true"></span>
            <span id="mrgCpText">Đã bật lưu tiến độ</span>
            <button type="button" class="mrg-cp-menu-btn" id="mrgCpResetBtn" aria-label="Cài đặt tiến độ">⚙️</button>
        `;
        document.body.appendChild(pillEl);
        statusTextEl = pillEl.querySelector('#mrgCpText');

        pillEl.addEventListener('click', function (e) {
            openCheckpointModal();
        });
        return pillEl;
    }

    function formatTime(ts) {
        const d = ts ? new Date(ts) : new Date();
        const pad = n => String(n).padStart(2, '0');
        return `${pad(d.getHours())}:${pad(d.getMinutes())}`;
    }

    function notifySaved(customLabel) {
        ensurePill();
        lastSavedTimeStr = formatTime();
        if (!statusTextEl) return;
        statusTextEl.textContent = customLabel || `Đã lưu (${lastSavedTimeStr})`;
        if (pillEl) {
            pillEl.classList.remove('is-saving', 'is-error');
            pillEl.classList.add('is-flashing');
            clearTimeout(lastSaveTimer);
            lastSaveTimer = setTimeout(() => {
                if (pillEl) pillEl.classList.remove('is-flashing');
            }, 800);
        }
    }

    function notifySaving() {
        ensurePill();
        if (!statusTextEl) return;
        statusTextEl.textContent = 'Đang lưu...';
        if (pillEl) {
            pillEl.classList.remove('is-error');
            pillEl.classList.add('is-saving');
        }
    }

    function notifyError(msg) {
        ensurePill();
        if (!statusTextEl) return;
        statusTextEl.textContent = msg || 'Lỗi lưu bộ nhớ!';
        if (pillEl) {
            pillEl.classList.remove('is-saving');
            pillEl.classList.add('is-error');
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
            // Only reset a studio mounted on this page, never another page's history.
            if (typeof window.resetTypingStudio === 'function') {
                toRemove.push('marugoto_typing_studio_v2');
            }
            toRemove.forEach(k => {
                try { localStorage.removeItem(k); } catch (e) {}
            });
            if (typeof window.resetTypingStudio === 'function') {
                window.resetTypingStudio();
            }
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
        notifySaving,
        notifyError,
        openModal: openCheckpointModal,
        closeModal: closeCheckpointModal,
        clearPage: () => clearPageCheckpoint(true),
        silentClearPage: () => clearPageCheckpoint(false)
    };

    // 3. TỰ ĐỘNG ĐỒNG BỘ HÓA DOM (NẾU TRANG KHÔNG TẮT CHẾ ĐỘ AUTO DOM)
    let isRestoring = false;
    const restoredInputKeys = new Set();

    let silentDepth = 0;
    let trueGlobals = null;
    let restoreGlobalsTimer = null;

    function withSilentUI(fn) {
        if (restoreGlobalsTimer) {
            clearTimeout(restoreGlobalsTimer);
            restoreGlobalsTimer = null;
        }

        if (silentDepth === 0) {
            trueGlobals = {
                synthSpeak: window.speechSynthesis ? window.speechSynthesis.speak.bind(window.speechSynthesis) : null,
                speakText: typeof window.speakText === 'function' ? window.speakText : null,
                speakJapanese: typeof window.speakJapanese === 'function' ? window.speakJapanese : null,
                audioSpeak: window.audioEngine && typeof window.audioEngine.speak === 'function' ? window.audioEngine.speak : null,
                audioCapSpeak: window.AudioEngine && typeof window.AudioEngine.speak === 'function' ? window.AudioEngine.speak : null,
                scrollTo: typeof window.scrollTo === 'function' ? window.scrollTo.bind(window) : null,
                scrollIntoView: Element.prototype.scrollIntoView,
                alert: typeof window.alert === 'function' ? window.alert.bind(window) : null
            };
        }

        silentDepth++;
        window.isRestoringCheckpoint = true;

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
            silentDepth = Math.max(0, silentDepth - 1);
            if (silentDepth === 0) {
                restoreGlobalsTimer = setTimeout(() => {
                    if (silentDepth === 0 && trueGlobals) {
                        window.isRestoringCheckpoint = false;
                        if (window.speechSynthesis && trueGlobals.synthSpeak) window.speechSynthesis.speak = trueGlobals.synthSpeak;
                        if (trueGlobals.speakText) window.speakText = trueGlobals.speakText;
                        if (trueGlobals.speakJapanese) window.speakJapanese = trueGlobals.speakJapanese;
                        if (window.audioEngine && trueGlobals.audioSpeak) window.audioEngine.speak = trueGlobals.audioSpeak;
                        if (window.AudioEngine && trueGlobals.audioCapSpeak) window.AudioEngine.speak = trueGlobals.audioCapSpeak;
                        if (trueGlobals.scrollTo) window.scrollTo = trueGlobals.scrollTo;
                        if (trueGlobals.scrollIntoView) Element.prototype.scrollIntoView = trueGlobals.scrollIntoView;
                        if (trueGlobals.alert) window.alert = trueGlobals.alert;
                        trueGlobals = null;
                    }
                }, 100);
            }
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
