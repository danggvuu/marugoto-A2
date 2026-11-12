/**
 * MARUGOTO VOCABULARY TYPING PRACTICE ENGINE (assets/js/typing-practice.js)
 * Chuyên mục luyện gõ Tiếng Nhật phản xạ từ Tiếng Việt cho trọn bộ Bài 1 - Bài 18:
 * - Chế độ 1: Flash Typing (Luyện phản xạ từng thẻ, tự động chuyển từ khi đúng, âm thanh Tokyo)
 * - Chế độ 2: Full Table (Bảng gõ toàn bộ danh sách, Enter tự nhảy sang dòng tiếp theo)
 * - Tự động nhận diện VOCAB_DATA trên trang bài học.
 */

(function () {
    'use strict';

    // 1. CHUẨN HÓA VÀ SO KHỚP ĐÁP ÁN THÔNG MINH
    function cleanStr(s) {
        if (!s) return '';
        return s.toString()
            .toLowerCase()
            .trim()
            .replace(/[()（）~～/／、,。.\s\-_\t]/g, '');
    }

    function getAcceptedAnswers(item) {
        const answers = new Set();
        
        function addVariant(raw) {
            if (!raw) return;
            const cleaned = cleanStr(raw);
            if (cleaned) answers.add(cleaned);

            // Tách theo dấu gạch chéo / hoặc ／
            const parts = raw.split(/[/／]/);
            if (parts.length > 1) {
                parts.forEach(p => {
                    const c = cleanStr(p);
                    if (c) answers.add(c);
                });
            }

            // Tách phần trước dấu ngoặc đơn () hoặc （）
            // Ví dụ: 結婚（します） -> 結婚 và 結婚します
            const noParen = raw.replace(/[()（）]/g, '');
            answers.add(cleanStr(noParen));

            const beforeParen = raw.replace(/[（(].*?[）)]/g, '');
            answers.add(cleanStr(beforeParen));
        }

        addVariant(item.jp);
        addVariant(item.kana);
        addVariant(item.kanji);
        addVariant(item.romaji);

        // Hỗ trợ trường hợp trường romaji có ký tự đặc biệt (ou -> o, uu -> u)
        if (item.romaji) {
            const r = item.romaji.toLowerCase();
            answers.add(cleanStr(r.replace(/ou/g, 'o')));
            answers.add(cleanStr(r.replace(/uu/g, 'u')));
        }

        return Array.from(answers);
    }

    function checkAnswer(userInput, item) {
        const cleanedInput = cleanStr(userInput);
        if (!cleanedInput) return false;
        const accepted = getAcceptedAnswers(item);
        return accepted.includes(cleanedInput);
    }

    function escapeHtml(str) {
        return String(str || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function resolveTpPageId() {
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

    function getTpStorageKey() {
        if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.getKey === 'function') {
            return window.MarugotoCheckpoint.getKey('typing_practice');
        }
        return 'marugoto_cp_v1::' + resolveTpPageId() + '::typing_practice';
    }

    function loadTpState() {
        try {
            const raw = localStorage.getItem(getTpStorageKey());
            if (!raw) return null;
            const parsed = JSON.parse(raw);
            return parsed && typeof parsed === 'object' && 'd' in parsed ? parsed.d : parsed;
        } catch (e) {
            return null;
        }
    }

    function saveTpState(stateObj) {
        try {
            localStorage.setItem(getTpStorageKey(), JSON.stringify({ t: Date.now(), d: stateObj }));
            if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
                window.MarugotoCheckpoint.notifySaved();
            }
        } catch (e) {}
    }

    function analyzeTypingMistake(rawInput, item) {
        const cleaned = cleanStr(rawInput);
        const targetKana = cleanStr(item.kana || item.jp || '');
        const targetKanji = cleanStr(item.kanji || item.jp || '');
        const targetRomaji = cleanStr(item.romaji || '');
        const isAscii = /^[a-z0-9\s\-]+$/i.test(rawInput.trim());

        let reason = '';
        if (!cleaned) {
            reason = 'Bạn mới nhập khoảng trắng hoặc ký tự ngăn cách.';
        } else if (isAscii && targetRomaji) {
            if (cleaned.includes('ou') !== targetRomaji.includes('ou') || cleaned.includes('uu') !== targetRomaji.includes('uu')) {
                reason = 'Kiểm tra lại trường âm (ou / uu / aa) khi gõ Romaji.';
            } else if (/([bcdfghjklmpqrstvwxyz])\1/.test(targetRomaji) && !/([bcdfghjklmpqrstvwxyz])\1/.test(cleaned)) {
                reason = 'Có thể bạn bị thiếu xúc âm (gấp đôi phụ âm / っ).';
            } else {
                reason = 'Chính tả Romaji chưa khớp hoàn toàn với phiên âm chuẩn.';
            }
        } else {
            const compareTarget = /[\u4e00-\u9faf]/.test(rawInput) && targetKanji ? targetKanji : targetKana;
            let diffIdx = 0;
            while (diffIdx < cleaned.length && diffIdx < compareTarget.length && cleaned[diffIdx] === compareTarget[diffIdx]) {
                diffIdx++;
            }
            if (compareTarget.includes('っ') && !cleaned.includes('っ')) {
                reason = 'Thiếu xúc âm nhỏ 「っ」.';
            } else if ((compareTarget.includes('ゃ') || compareTarget.includes('ゅ') || compareTarget.includes('ょ')) &&
                       !(cleaned.includes('ゃ') || cleaned.includes('ゅ') || cleaned.includes('ょ'))) {
                reason = 'Kiểm tra âm ghép nhỏ 「ゃ / ゅ / ょ」.';
            } else if (compareTarget.includes('ー') && !cleaned.includes('ー')) {
                reason = 'Thiếu dấu trường âm Katakana 「ー」.';
            } else if (cleaned.length < compareTarget.length && compareTarget.startsWith(cleaned)) {
                reason = `Bạn gõ đúng phần đầu (${cleaned.length}/${compareTarget.length} ký tự), còn thiếu phần đuôi.`;
            } else if (cleaned.length > compareTarget.length && cleaned.startsWith(compareTarget)) {
                reason = 'Bạn gõ dư ký tự hoặc dư trợ từ ở cuối.';
            } else if (diffIdx > 0) {
                reason = `Đúng ${diffIdx} ký tự đầu, bắt đầu lệch từ ký tự thứ ${diffIdx + 1} (bạn gõ "${cleaned[diffIdx] || '∅'}").`;
            } else {
                reason = 'Cách đọc / mặt chữ Kana hoặc Kanji chưa khớp với nghĩa đang hỏi.';
            }
        }

        const displayTarget = item.kana ? item.kana : item.jp;
        const firstChar = displayTarget ? displayTarget.charAt(0) : '';
        const kanaLen = cleanStr(item.kana || '').length || cleanStr(item.jp || '').length;
        const hasKanjiDiff = item.kanji && item.kanji !== item.kana;
        const comparisonHint = hasKanjiDiff
            ? `Độ dài Kana: ${kanaLen} ký tự (bắt đầu bằng 「${escapeHtml(firstChar)}…」) · Có cả dạng Kanji/Kana.`
            : `Độ dài chuẩn: ${kanaLen} ký tự (bắt đầu bằng 「${escapeHtml(firstChar)}…」).`;

        return {
            reason,
            comparisonHint,
            firstChar
        };
    }

    // 2. PHÁT ÂM AUDIO GIỌNG TOKYO
    function playAudio(text) {
        if (!text) return;
        if (typeof window.speakText === 'function') {
            window.speakText(text);
        } else if ('speechSynthesis' in window) {
            const u = new SpeechSynthesisUtterance(text);
            u.lang = 'ja-JP';
            u.rate = 0.9;
            window.speechSynthesis.speak(u);
        }
    }

    // 3. KHỞI TẠO VÀ RENDER GIAO DIỆN
    function initTypingPractice() {
        const vocabList = window.VOCAB_DATA || (typeof VOCAB_DATA !== 'undefined' ? VOCAB_DATA : null);
        if (!vocabList || !Array.isArray(vocabList) || vocabList.length === 0) {
            return;
        }

        // Tìm hoặc tự tạo container section
        let sec = document.getElementById('sec-typing-practice');
        if (!sec) {
            const vocabSec = document.getElementById('sec-vocab');
            sec = document.createElement('section');
            sec.className = 'content-section';
            sec.id = 'sec-typing-practice';

            if (vocabSec && vocabSec.parentNode) {
                vocabSec.parentNode.insertBefore(sec, vocabSec.nextSibling);
            } else {
                const quizSec = document.getElementById('sec-quiz');
                if (quizSec && quizSec.parentNode) {
                    quizSec.parentNode.insertBefore(sec, quizSec);
                } else {
                    const mc = document.querySelector('.main-container') || document.querySelector('.container') || document.body;
                    mc.appendChild(sec);
                }
            }
        }

        // Thêm liên kết vào sticky section nav nếu chưa có
        const sectionNav = document.querySelector('.section-nav');
        if (sectionNav && !sectionNav.querySelector('a[href="#sec-typing-practice"]')) {
            const link = document.createElement('a');
            link.href = '#sec-typing-practice';
            link.className = sectionNav.querySelector('.sec-link') ? 'sec-link' : (sectionNav.querySelector('.tab-btn') ? 'tab-btn' : 'sec-link');
            link.style.textDecoration = 'none';
            link.innerHTML = '⌨️ Luyện Gõ Từ Vựng';
            
            // Chèn sau link #sec-vocab nếu có
            const vocabLink = sectionNav.querySelector('a[href="#sec-vocab"]');
            if (vocabLink && vocabLink.nextSibling) {
                sectionNav.insertBefore(link, vocabLink.nextSibling);
            } else {
                sectionNav.appendChild(link);
            }
        }

        // Tạo khung HTML
        sec.innerHTML = `
            <div class="section-header">
                <h2 class="section-title"><span>⌨️</span> Đấu Trường Luyện Gõ Từ Vựng (Việt ➔ Nhật)</h2>
                <span class="section-tag">Interactive Flash Typing</span>
            </div>
            <p style="margin-bottom: 16px; color: #475569;">
                Luyện phản xạ nhập liệu: Nhìn nghĩa tiếng Việt, gõ từ vựng tiếng Nhật tương ứng (hỗ trợ cả <strong>Hiragana</strong>, <strong>Kanji</strong> hoặc <strong>Romaji</strong>).
            </p>

            <div class="typing-practice-container">
                <!-- Chuyển đổi chế độ -->
                <div class="tp-mode-switch">
                    <button type="button" class="tp-mode-btn active" id="tpBtnModeCard">🎴 Thẻ Luyện Phản Xạ (Flash Typing)</button>
                    <button type="button" class="tp-mode-btn" id="tpBtnModeTable">📋 Bảng Danh Sách Toàn Bộ</button>
                </div>

                <!-- CHẾ ĐỘ 1: THẺ FLASHCARD -->
                <div id="tpCardModeView" class="tp-card-arena">
                    <div class="tp-card">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                            <span style="font-size:0.82rem; font-weight:800; color:#6366f1; background:#e0e7ff; padding:3px 10px; border-radius:999px;" id="tpCardBadge">Từ 1 / ${vocabList.length}</span>
                            <span style="font-size:0.84rem; font-weight:700; color:#ea580c;" id="tpStreakBadge">🔥 Chuỗi: 0</span>
                        </div>

                        <div class="tp-prompt-vi" id="tpPromptVi">---</div>
                        <div class="tp-prompt-hint">Gõ từ vựng tiếng Nhật rồi nhấn Enter để kiểm tra:</div>

                        <div class="tp-input-wrap">
                            <input type="text" class="tp-input" id="tpCardInput" placeholder="Nhập Hiragana, Kanji hoặc Romaji..." autocomplete="off" autocapitalize="off" spellcheck="false">
                            <button type="button" class="tp-btn-check" id="tpCardCheckBtn">Kiểm Tra ⏎</button>
                        </div>

                        <div class="tp-actions-row">
                            <button type="button" class="tp-btn-sub" id="tpBtnSpeakWord">🔊 Nghe Gợi Ý</button>
                            <button type="button" class="tp-btn-sub" id="tpBtnHintWord">💡 Gợi Ý Chữ Đầu</button>
                            <button type="button" class="tp-btn-sub" id="tpBtnShowAnswer">👁️ Xem Đáp Án</button>
                            <button type="button" class="tp-btn-sub" id="tpBtnSkipWord">Bỏ Qua ➔</button>
                            <button type="button" class="tp-btn-sub" id="tpBtnShuffleCards">🔀 Xáo Trộn</button>
                            <button type="button" class="tp-btn-sub" id="tpBtnCardReset">🔄 Làm Lại</button>
                        </div>

                        <div class="tp-feedback" id="tpCardFeedback"></div>

                        <div class="tp-progress-track">
                            <div class="tp-progress-fill" id="tpProgressBar"></div>
                        </div>

                        <div class="tp-stats-bar">
                            <span>✅ Đã thuộc: <strong style="color:#059669;" id="tpStatCorrect">0</strong></span>
                            <span>⏳ Cần luyện lại: <strong style="color:#dc2626;" id="tpStatWrong">0</strong></span>
                            <span>🎯 Tiến độ: <strong style="color:#4f46e5;" id="tpStatPercent">0%</strong></span>
                        </div>
                    </div>
                </div>

                <!-- CHẾ ĐỘ 2: BẢNG TOÀN BỘ -->
                <div id="tpTableModeView" class="tp-table-wrap" style="display:none;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
                        <span style="font-size:0.9rem; font-weight:700; color:#334155;">Nhập đáp án và bấm Enter để tự động nhảy dòng:</span>
                        <div style="display:flex; gap:8px;">
                            <button type="button" class="tp-btn-sub" id="tpBtnTableShowAll">👁️ Hiện Toàn Bộ Đáp Án</button>
                            <button type="button" class="tp-btn-sub" id="tpBtnTableReset">🔄 Làm Lại Từ Đầu</button>
                        </div>
                    </div>
                    <table class="tp-table">
                        <thead>
                            <tr>
                                <th style="width: 50px; text-align:center;">STT</th>
                                <th style="width: 240px;">Tiếng Việt (Gợi Ý)</th>
                                <th>Tiếng Nhật (Gõ Hiragana / Kanji / Romaji)</th>
                                <th style="width: 220px;">Đáp Án Chuẩn</th>
                                <th style="width: 60px; text-align:center;">Nghe</th>
                                <th style="width: 100px; text-align:center;">Trạng Thái</th>
                            </tr>
                        </thead>
                        <tbody id="tpTableBody"></tbody>
                    </table>
                </div>
            </div>
        `;

        // 4. LOGIC ĐIỀU KHIỂN CHẾ ĐỘ CARD FLASH TYPING & CHECKPOINT
        const savedTp = loadTpState() || {};
        function rebuildWordsFromOrder(order) {
            if (!Array.isArray(order) || order.length === 0) return [...vocabList];
            const pool = [...vocabList];
            const ordered = [];
            order.forEach(jpKey => {
                const foundIdx = pool.findIndex(item => item.jp === jpKey);
                if (foundIdx !== -1) {
                    ordered.push(pool.splice(foundIdx, 1)[0]);
                }
            });
            return ordered.concat(pool);
        }

        let activeMode = savedTp.mode === 'table' ? 'table' : 'card';
        let words = rebuildWordsFromOrder(savedTp.wordOrder);
        let currentIndex = Number.isInteger(savedTp.currentIndex) && savedTp.currentIndex >= 0
            ? Math.min(savedTp.currentIndex, words.length)
            : 0;
        let streak = Number.isFinite(savedTp.streak) ? savedTp.streak : 0;
        let correctCount = Number.isFinite(savedTp.correctCount) ? savedTp.correctCount : 0;
        let wrongCount = Number.isFinite(savedTp.wrongCount) ? savedTp.wrongCount : 0;
        let cardFeedbackState = savedTp.cardFeedbackState || null;
        let showTableAnswers = Boolean(savedTp.showTableAnswers);
        let tableState = (savedTp.tableState && typeof savedTp.tableState === 'object') ? { ...savedTp.tableState } : {};
        let advanceTimer = null;
        let isCardComposing = false;

        function persistTpState(extra = {}) {
            saveTpState({
                mode: activeMode,
                wordOrder: words.map(w => w.jp),
                currentIndex,
                streak,
                correctCount,
                wrongCount,
                cardDraft: cardInput ? cardInput.value : '',
                cardFeedbackState,
                showTableAnswers,
                tableState,
                ...extra
            });
        }

        const cardInput = document.getElementById('tpCardInput');
        const promptVi = document.getElementById('tpPromptVi');
        const feedback = document.getElementById('tpCardFeedback');
        const cardBadge = document.getElementById('tpCardBadge');
        const streakBadge = document.getElementById('tpStreakBadge');
        const progressBar = document.getElementById('tpProgressBar');
        const statCorrect = document.getElementById('tpStatCorrect');
        const statWrong = document.getElementById('tpStatWrong');
        const statPercent = document.getElementById('tpStatPercent');

        function renderFeedbackFromState(st, current) {
            if (!st || !current) {
                feedback.innerHTML = '';
                return;
            }
            if (st.type === 'correct') {
                feedback.innerHTML = `
                    <span style="color:#059669;">✓ <strong>Chính xác!</strong> ${escapeHtml(current.jp)} 【${escapeHtml(current.kana || '')}】 (${escapeHtml(current.romaji || '')})</span>
                `;
            } else if (st.type === 'wrong') {
                const diag = analyzeTypingMistake(st.attempt || '', current);
                feedback.innerHTML = `
                    <div style="text-align:left; background:#fff1f2; border:1px solid #fecdd3; border-radius:10px; padding:10px 12px; color:#9f1239; font-size:0.9rem; line-height:1.5;">
                        <div><strong>✕ Chưa chính xác</strong> — Bạn gõ: <code>${escapeHtml(st.attempt || '')}</code></div>
                        <div>• <strong>Nghĩa:</strong> ${escapeHtml(current.vi)}</div>
                        <div>• <strong>Vì sao sai / Gợi ý:</strong> ${escapeHtml(diag.reason)}</div>
                        <div>• <strong>Đối chiếu:</strong> ${diag.comparisonHint}</div>
                    </div>
                `;
            } else if (st.type === 'revealed') {
                feedback.innerHTML = `
                    <div style="text-align:left; background:#fffbeb; border:1px solid #fde68a; border-radius:10px; padding:10px 12px; color:#92400e; font-size:0.9rem; line-height:1.5;">
                        <div>📖 <strong>Đáp án chuẩn:</strong> <strong>${escapeHtml(current.jp)}</strong> 【${escapeHtml(current.kana || '')}】 (${escapeHtml(current.romaji || '')})</div>
                        <div>• <strong>Nghĩa:</strong> ${escapeHtml(current.vi)}</div>
                    </div>
                `;
            } else if (st.type === 'hint') {
                const hint = current.kana ? current.kana.charAt(0) : current.jp.charAt(0);
                feedback.innerHTML = `<span style="color:#4f46e5;">💡 Gợi ý chữ cái đầu: <strong>${escapeHtml(hint)}...</strong></span>`;
            } else {
                feedback.innerHTML = '';
            }
        }

        function loadCard(index, shouldFocus = true, preserveDraft = false) {
            if (advanceTimer) {
                clearTimeout(advanceTimer);
                advanceTimer = null;
            }
            if (index < 0 || index >= words.length) {
                // Đã hoàn thành hết
                promptVi.innerHTML = `🎉 Chúc mừng bạn đã hoàn thành trọn bộ ${words.length} từ vựng!`;
                feedback.innerHTML = `<span style="color:#059669;">Bạn đã nhớ được ${correctCount}/${words.length} từ. Xuất sắc!</span>`;
                cardInput.value = '';
                cardInput.disabled = true;
                cardInput.className = 'tp-input';
                cardBadge.innerText = `Hoàn tất ${words.length} / ${words.length}`;
                streakBadge.innerText = `🔥 Chuỗi: ${streak}`;
                progressBar.style.width = '100%';
                statPercent.innerText = '100%';
                statCorrect.innerText = correctCount;
                statWrong.innerText = wrongCount;
                return;
            }

            const current = words[index];
            promptVi.innerText = current.vi;
            if (!preserveDraft) {
                cardInput.value = '';
                cardFeedbackState = null;
            }
            cardInput.disabled = false;
            cardInput.className = 'tp-input';
            renderFeedbackFromState(cardFeedbackState, current);
            cardBadge.innerText = `Từ ${index + 1} / ${words.length}`;
            streakBadge.innerText = `🔥 Chuỗi: ${streak}`;

            const pct = Math.round((index / words.length) * 100);
            progressBar.style.width = `${pct}%`;
            statPercent.innerText = `${pct}%`;
            statCorrect.innerText = correctCount;
            statWrong.innerText = wrongCount;

            if (shouldFocus) {
                cardInput.focus();
            }
        }

        function handleCardSubmit() {
            if (currentIndex >= words.length || advanceTimer) return;
            const current = words[currentIndex];
            const val = cardInput.value.trim();

            if (!val) {
                cardInput.focus();
                return;
            }

            const ok = checkAnswer(val, current);
            if (ok) {
                streak++;
                correctCount++;
                cardInput.className = 'tp-input is-correct';
                cardFeedbackState = { type: 'correct' };
                renderFeedbackFromState(cardFeedbackState, current);
                statCorrect.innerText = correctCount;
                streakBadge.innerText = `🔥 Chuỗi: ${streak}`;
                playAudio(current.jp);
                persistTpState();

                // Tự động chuyển sau 1 giây
                advanceTimer = setTimeout(() => {
                    advanceTimer = null;
                    currentIndex++;
                    loadCard(currentIndex, true);
                    persistTpState();
                }, 1000);
            } else {
                streak = 0;
                streakBadge.innerText = `🔥 Chuỗi: 0`;
                wrongCount++;
                statWrong.innerText = wrongCount;
                cardInput.className = 'tp-input is-wrong';
                cardFeedbackState = { type: 'wrong', attempt: val };
                renderFeedbackFromState(cardFeedbackState, current);
                persistTpState();
                setTimeout(() => {
                    cardInput.classList.remove('is-wrong');
                }, 500);
            }
        }

        // Bắt sự kiện bàn phím + IME Guard trên ô input Card
        cardInput.addEventListener('compositionstart', () => { isCardComposing = true; });
        cardInput.addEventListener('compositionend', () => { isCardComposing = false; });
        cardInput.addEventListener('input', () => {
            if (advanceTimer) return;
            persistTpState();
        });
        cardInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.isComposing && !isCardComposing && e.keyCode !== 229) {
                e.preventDefault();
                handleCardSubmit();
            }
        });

        document.getElementById('tpCardCheckBtn').addEventListener('click', handleCardSubmit);

        document.getElementById('tpBtnSpeakWord').addEventListener('click', () => {
            if (currentIndex < words.length) {
                playAudio(words[currentIndex].jp);
            }
        });

        document.getElementById('tpBtnHintWord').addEventListener('click', () => {
            if (currentIndex < words.length) {
                const current = words[currentIndex];
                cardFeedbackState = { type: 'hint' };
                renderFeedbackFromState(cardFeedbackState, current);
                persistTpState();
                cardInput.focus();
            }
        });

        document.getElementById('tpBtnShowAnswer').addEventListener('click', () => {
            if (currentIndex < words.length) {
                if (advanceTimer) {
                    clearTimeout(advanceTimer);
                    advanceTimer = null;
                }
                const current = words[currentIndex];
                streak = 0;
                streakBadge.innerText = `🔥 Chuỗi: 0`;
                cardInput.value = current.jp;
                cardFeedbackState = { type: 'revealed' };
                renderFeedbackFromState(cardFeedbackState, current);
                playAudio(current.jp);
                persistTpState();
            }
        });

        document.getElementById('tpBtnSkipWord').addEventListener('click', () => {
            if (currentIndex < words.length) {
                currentIndex++;
            }
            loadCard(currentIndex, true);
            persistTpState();
        });

        document.getElementById('tpBtnShuffleCards').addEventListener('click', () => {
            words.sort(() => Math.random() - 0.5);
            currentIndex = 0;
            streak = 0;
            correctCount = 0;
            wrongCount = 0;
            loadCard(0, true);
            persistTpState();
        });

        document.getElementById('tpBtnCardReset').addEventListener('click', () => {
            words = [...vocabList];
            currentIndex = 0;
            streak = 0;
            correctCount = 0;
            wrongCount = 0;
            loadCard(0, true);
            persistTpState();
        });

        // 5. LOGIC ĐIỀU KHIỂN CHẾ ĐỘ BẢNG (TABLE MODE)
        const tableBody = document.getElementById('tpTableBody');
        function applyTableRowUi(idx, item, st) {
            const inp = document.getElementById(`tpTblInput_${idx}`);
            const statusBadge = document.getElementById(`tpTblStatus_${idx}`);
            const ansSpan = document.getElementById(`tpTblAns_${idx}`);
            const tipEl = document.getElementById(`tpRowTip_${idx}`);
            if (!inp || !statusBadge || !ansSpan) return;

            const status = st && st.status ? st.status : 'pending';
            const val = st && typeof st.val === 'string' ? st.val : '';
            inp.value = val;

            if (status === 'ok') {
                inp.className = 'tp-table-input is-correct';
                statusBadge.className = 'tp-badge-status tp-status-ok';
                statusBadge.innerText = '✓ Đúng';
                ansSpan.style.display = 'inline';
                if (tipEl) tipEl.innerHTML = '';
            } else if (status === 'err') {
                inp.className = 'tp-table-input is-wrong';
                statusBadge.className = 'tp-badge-status tp-status-err';
                statusBadge.innerText = '✕ Sai';
                ansSpan.style.display = showTableAnswers ? 'inline' : 'none';
                if (tipEl) {
                    const diag = analyzeTypingMistake(val, item);
                    tipEl.innerHTML = `<div style="margin-top:4px; font-size:0.78rem; color:#be123c; line-height:1.4;">💡 <strong>Vì sao sai:</strong> ${escapeHtml(diag.reason)} <span style="color:#64748b;">(${diag.comparisonHint})</span></div>`;
                }
            } else {
                inp.className = 'tp-table-input';
                statusBadge.className = 'tp-badge-status tp-status-pending';
                statusBadge.innerText = 'Chờ gõ';
                ansSpan.style.display = showTableAnswers ? 'inline' : 'none';
                if (tipEl) tipEl.innerHTML = '';
            }
        }

        function renderTableRows() {
            tableBody.innerHTML = vocabList.map((item, idx) => `
                <tr id="tpRow_${idx}">
                    <td style="text-align:center; font-weight:700; color:#64748b;">${idx + 1}</td>
                    <td><strong style="color:#0f172a; font-size:1.02rem;">${escapeHtml(item.vi)}</strong></td>
                    <td>
                        <input type="text" class="tp-table-input" id="tpTblInput_${idx}" placeholder="Gõ tiếng Nhật..." data-idx="${idx}" autocomplete="off" autocapitalize="off" spellcheck="false">
                        <div id="tpRowTip_${idx}"></div>
                    </td>
                    <td>
                        <span id="tpTblAns_${idx}" style="display:${showTableAnswers ? 'inline' : 'none'}; font-weight:700; color:#4f46e5;">
                            ${escapeHtml(item.jp)} <span style="font-size:0.85rem; color:#64748b;">【${escapeHtml(item.kana || '')}】</span>
                        </span>
                    </td>
                    <td style="text-align:center;">
                        <button type="button" class="sound-btn" data-tp-speak="${idx}">🔊</button>
                    </td>
                    <td style="text-align:center;">
                        <span class="tp-badge-status tp-status-pending" id="tpTblStatus_${idx}">Chờ gõ</span>
                    </td>
                </tr>
            `).join('');

            tableBody.querySelectorAll('button[data-tp-speak]').forEach(btn => {
                btn.addEventListener('click', () => {
                    const idx = Number(btn.getAttribute('data-tp-speak'));
                    if (vocabList[idx]) playAudio(vocabList[idx].jp);
                });
            });

            // Gán sự kiện IME Guard + Enter + Input checkpoint cho từng dòng
            const inputs = tableBody.querySelectorAll('.tp-table-input');
            inputs.forEach((inp, idx) => {
                const item = vocabList[idx];
                if (tableState[idx]) {
                    applyTableRowUi(idx, item, tableState[idx]);
                }

                let isRowComposing = false;
                inp.addEventListener('compositionstart', () => { isRowComposing = true; });
                inp.addEventListener('compositionend', () => { isRowComposing = false; });

                inp.addEventListener('input', () => {
                    const prev = tableState[idx] || {};
                    tableState[idx] = { val: inp.value, status: prev.status === 'ok' ? 'pending' : (prev.status || 'pending') };
                    if (prev.status === 'ok') {
                        applyTableRowUi(idx, item, tableState[idx]);
                        inp.value = tableState[idx].val;
                    }
                    persistTpState();
                });

                inp.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter' && !e.isComposing && !isRowComposing && e.keyCode !== 229) {
                        e.preventDefault();
                        const rawVal = inp.value;
                        const val = rawVal.trim();

                        if (checkAnswer(val, item)) {
                            tableState[idx] = { val: rawVal, status: 'ok' };
                            applyTableRowUi(idx, item, tableState[idx]);
                            playAudio(item.jp);
                            persistTpState();

                            // Tự động nhảy con trỏ sang dòng tiếp theo
                            if (idx + 1 < inputs.length) {
                                inputs[idx + 1].focus();
                            }
                        } else {
                            tableState[idx] = { val: rawVal, status: 'err' };
                            applyTableRowUi(idx, item, tableState[idx]);
                            persistTpState();
                        }
                    }
                });
            });
        }

        document.getElementById('tpBtnTableShowAll').addEventListener('click', () => {
            showTableAnswers = true;
            vocabList.forEach((_, idx) => {
                const ans = document.getElementById(`tpTblAns_${idx}`);
                if (ans) ans.style.display = 'inline';
            });
            persistTpState();
        });

        document.getElementById('tpBtnTableReset').addEventListener('click', () => {
            showTableAnswers = false;
            tableState = {};
            renderTableRows();
            persistTpState();
        });

        // 6. CHUYỂN ĐỔI CHẾ ĐỘ CARD VS TABLE
        const btnModeCard = document.getElementById('tpBtnModeCard');
        const btnModeTable = document.getElementById('tpBtnModeTable');
        const cardView = document.getElementById('tpCardModeView');
        const tableView = document.getElementById('tpTableModeView');

        function applyMode(mode, focusInput) {
            activeMode = mode === 'table' ? 'table' : 'card';
            if (activeMode === 'table') {
                btnModeTable.classList.add('active');
                btnModeCard.classList.remove('active');
                cardView.style.display = 'none';
                tableView.style.display = 'block';
                if (!tableBody.hasChildNodes()) {
                    renderTableRows();
                }
            } else {
                btnModeCard.classList.add('active');
                btnModeTable.classList.remove('active');
                cardView.style.display = 'block';
                tableView.style.display = 'none';
                if (focusInput && !cardInput.disabled) {
                    cardInput.focus();
                }
            }
        }

        btnModeCard.addEventListener('click', () => {
            applyMode('card', true);
            persistTpState();
        });

        btnModeTable.addEventListener('click', () => {
            applyMode('table', false);
            persistTpState();
        });

        // Khởi động + Khôi phục checkpoint không cuộn trang
        if (cardFeedbackState && cardFeedbackState.type === 'correct' && currentIndex < words.length) {
            currentIndex++;
            cardFeedbackState = null;
            savedTp.cardDraft = '';
        }
        const hasCardSnapshot = Boolean((savedTp.cardDraft && savedTp.cardDraft.length > 0) || cardFeedbackState);
        if (hasCardSnapshot && currentIndex < words.length) {
            cardInput.value = savedTp.cardDraft || '';
        }
        loadCard(currentIndex, false, hasCardSnapshot);
        renderTableRows();
        applyMode(activeMode, false);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTypingPractice);
    } else {
        initTypingPractice();
    }
})();
