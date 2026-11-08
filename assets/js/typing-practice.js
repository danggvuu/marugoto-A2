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
        const vocabList = window.VOCAB_DATA;
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

        // 4. LOGIC ĐIỀU KHIỂN CHẾ ĐỘ CARD FLASH TYPING
        let words = [...vocabList];
        let currentIndex = 0;
        let streak = 0;
        let correctCount = 0;
        let wrongCount = 0;

        const cardInput = document.getElementById('tpCardInput');
        const promptVi = document.getElementById('tpPromptVi');
        const feedback = document.getElementById('tpCardFeedback');
        const cardBadge = document.getElementById('tpCardBadge');
        const streakBadge = document.getElementById('tpStreakBadge');
        const progressBar = document.getElementById('tpProgressBar');
        const statCorrect = document.getElementById('tpStatCorrect');
        const statWrong = document.getElementById('tpStatWrong');
        const statPercent = document.getElementById('tpStatPercent');

        function loadCard(index) {
            if (index < 0 || index >= words.length) {
                // Đã hoàn thành hết
                promptVi.innerHTML = `🎉 Chúc mừng bạn đã hoàn thành trọn bộ ${words.length} từ vựng!`;
                feedback.innerHTML = `<span style="color:#059669;">Bạn đã nhớ được ${correctCount}/${words.length} từ. Xuất sắc!</span>`;
                cardInput.disabled = true;
                progressBar.style.width = '100%';
                statPercent.innerText = '100%';
                return;
            }

            const current = words[index];
            promptVi.innerText = current.vi;
            cardInput.value = '';
            cardInput.disabled = false;
            cardInput.className = 'tp-input';
            feedback.innerHTML = '';
            cardBadge.innerText = `Từ ${index + 1} / ${words.length}`;
            streakBadge.innerText = `🔥 Chuỗi: ${streak}`;

            const pct = Math.round((index / words.length) * 100);
            progressBar.style.width = `${pct}%`;
            statPercent.innerText = `${pct}%`;
            statCorrect.innerText = correctCount;
            statWrong.innerText = wrongCount;

            cardInput.focus();
        }

        function handleCardSubmit() {
            if (currentIndex >= words.length) return;
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
                feedback.innerHTML = `
                    <span style="color:#059669;">✓ <strong>Chính xác!</strong> ${current.jp} 【${current.kana || ''}】 (${current.romaji || ''})</span>
                `;
                playAudio(current.jp);

                // Tự động chuyển sau 1 giây
                setTimeout(() => {
                    currentIndex++;
                    loadCard(currentIndex);
                }, 1000);
            } else {
                streak = 0;
                streakBadge.innerText = `🔥 Chuỗi: 0`;
                wrongCount++;
                cardInput.className = 'tp-input is-wrong';
                feedback.innerHTML = `
                    <span style="color:#dc2626;">✕ Chưa chính xác! Hãy thử lại hoặc bấm "Xem Đáp Án".</span>
                `;
                setTimeout(() => {
                    cardInput.classList.remove('is-wrong');
                }, 500);
            }
        }

        // Bắt sự kiện bàn phím trên ô input Card
        cardInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
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
                const hint = current.kana ? current.kana.charAt(0) : current.jp.charAt(0);
                feedback.innerHTML = `<span style="color:#4f46e5;">💡 Gợi ý chữ cái đầu: <strong>${hint}...</strong></span>`;
                cardInput.focus();
            }
        });

        document.getElementById('tpBtnShowAnswer').addEventListener('click', () => {
            if (currentIndex < words.length) {
                const current = words[currentIndex];
                streak = 0;
                streakBadge.innerText = `🔥 Chuỗi: 0`;
                cardInput.value = current.jp;
                feedback.innerHTML = `
                    <span style="color:#d97706;">📖 Đáp án: <strong>${current.jp}</strong> 【${current.kana || ''}】 (${current.romaji || ''})</span>
                `;
                playAudio(current.jp);
            }
        });

        document.getElementById('tpBtnSkipWord').addEventListener('click', () => {
            currentIndex++;
            loadCard(currentIndex);
        });

        document.getElementById('tpBtnShuffleCards').addEventListener('click', () => {
            words.sort(() => Math.random() - 0.5);
            currentIndex = 0;
            streak = 0;
            correctCount = 0;
            wrongCount = 0;
            loadCard(0);
        });

        // 5. LOGIC ĐIỀU KHIỂN CHẾ ĐỘ BẢNG (TABLE MODE)
        const tableBody = document.getElementById('tpTableBody');
        function renderTableRows() {
            tableBody.innerHTML = vocabList.map((item, idx) => `
                <tr id="tpRow_${idx}">
                    <td style="text-align:center; font-weight:700; color:#64748b;">${idx + 1}</td>
                    <td><strong style="color:#0f172a; font-size:1.02rem;">${item.vi}</strong></td>
                    <td>
                        <input type="text" class="tp-table-input" id="tpTblInput_${idx}" placeholder="Gõ tiếng Nhật..." data-idx="${idx}" autocomplete="off" autocapitalize="off" spellcheck="false">
                    </td>
                    <td>
                        <span id="tpTblAns_${idx}" style="display:none; font-weight:700; color:#4f46e5;">
                            ${item.jp} <span style="font-size:0.85rem; color:#64748b;">【${item.kana || ''}】</span>
                        </span>
                    </td>
                    <td style="text-align:center;">
                        <button type="button" class="sound-btn" onclick="window.speakText && window.speakText('${item.jp}')">🔊</button>
                    </td>
                    <td style="text-align:center;">
                        <span class="tp-badge-status tp-status-pending" id="tpTblStatus_${idx}">Chờ gõ</span>
                    </td>
                </tr>
            `).join('');

            // Gán sự kiện Enter cho từng dòng
            const inputs = tableBody.querySelectorAll('.tp-table-input');
            inputs.forEach((inp, idx) => {
                inp.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        const val = inp.value.trim();
                        const item = vocabList[idx];
                        const statusBadge = document.getElementById(`tpTblStatus_${idx}`);
                        const ansSpan = document.getElementById(`tpTblAns_${idx}`);

                        if (checkAnswer(val, item)) {
                            inp.className = 'tp-table-input is-correct';
                            statusBadge.className = 'tp-badge-status tp-status-ok';
                            statusBadge.innerText = '✓ Đúng';
                            ansSpan.style.display = 'inline';
                            playAudio(item.jp);

                            // Tự động nhảy con trỏ sang dòng tiếp theo
                            if (idx + 1 < inputs.length) {
                                inputs[idx + 1].focus();
                            }
                        } else {
                            inp.className = 'tp-table-input is-wrong';
                            statusBadge.className = 'tp-badge-status tp-status-err';
                            statusBadge.innerText = '✕ Sai';
                        }
                    }
                });
            });
        }

        document.getElementById('tpBtnTableShowAll').addEventListener('click', () => {
            vocabList.forEach((_, idx) => {
                const ans = document.getElementById(`tpTblAns_${idx}`);
                if (ans) ans.style.display = 'inline';
            });
        });

        document.getElementById('tpBtnTableReset').addEventListener('click', () => {
            renderTableRows();
        });

        // 6. CHUYỂN ĐỔI CHẾ ĐỘ CARD VS TABLE
        const btnModeCard = document.getElementById('tpBtnModeCard');
        const btnModeTable = document.getElementById('tpBtnModeTable');
        const cardView = document.getElementById('tpCardModeView');
        const tableView = document.getElementById('tpTableModeView');

        btnModeCard.addEventListener('click', () => {
            btnModeCard.classList.add('active');
            btnModeTable.classList.remove('active');
            cardView.style.display = 'block';
            tableView.style.display = 'none';
            cardInput.focus();
        });

        btnModeTable.addEventListener('click', () => {
            btnModeTable.classList.add('active');
            btnModeCard.classList.remove('active');
            cardView.style.display = 'none';
            tableView.style.display = 'block';
            if (!tableBody.hasChildNodes()) {
                renderTableRows();
            }
        });

        // Khởi động
        loadCard(0);
        renderTableRows();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTypingPractice);
    } else {
        initTypingPractice();
    }
})();
