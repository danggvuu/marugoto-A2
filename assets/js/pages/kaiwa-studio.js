/**
 * MARUGOTO A2.1 KAIWA INTERVIEW STUDIO CONTROLLER (assets/js/pages/kaiwa-studio.js)
 * Điều khiển toàn bộ phòng luyện Kaiwa 5 phút:
 *  - 3 chủ đề câu hỏi bám sát đề thi cô giáo (Bảo vệ sức khỏe, Thăm hỏi sức khỏe, Tiệc chúc mừng)
 *  - Đồng hồ đếm ngược 5:00 mô phỏng thời gian thi vấn đáp
 *  - Tích hợp Tokyo Speech TTS tự động phát âm câu hỏi của Sensei & câu trả lời mẫu
 *  - 4 chế độ: Thi thử 5p (Simulator), Flashcard phản xạ, Kịch bản song ngữ (Roleplay), 5 Mẹo ghi điểm
 */

(function (window, document) {
    'use strict';

    const TOPICS = window.KAIWA_TOPICS_DATA || [];
    const TIPS = window.KAIWA_TIPS || [];

    // State
    let currentTopicId = getInitialTopic();
    let currentMode = 'simulator'; // 'simulator' | 'flashcard' | 'dialogue' | 'tips'
    let currentQuestionIdx = 0;
    let timerTotalSeconds = 5 * 60; // 5 phút chuẩn phòng thi
    let timerRemaining = timerTotalSeconds;
    let timerInterval = null;
    let isTimerRunning = false;
    let isFlipped = false;

    // View options
    let showVi = true;
    let showMindmap = true;
    let showAnswers = true;

    function getInitialTopic() {
        const hash = (window.location.hash || '').replace('#', '').trim();
        if (hash && TOPICS.some(t => t.id === hash)) {
            return hash;
        }
        return 'topic1';
    }

    function getCurrentTopic() {
        return TOPICS.find(t => t.id === currentTopicId) || TOPICS[0];
    }

    // ==========================================================================
    // AUDIO ENGINE HELPER
    // ==========================================================================
    function playAudio(text, btn) {
        if (!text) return;
        if (typeof window.speakJapanese === 'function') {
            window.speakJapanese(text, btn);
        } else if (typeof window.speakText === 'function') {
            window.speakText(text, btn);
        } else if (window.AudioEngine && typeof window.AudioEngine.speak === 'function') {
            window.AudioEngine.speak(text, btn);
        }
    }

    // ==========================================================================
    // TIMER ENGINE
    // ==========================================================================
    function updateTimerUI() {
        const clockEl = document.getElementById('kaiwaTimerClock');
        const fillEl = document.getElementById('kaiwaTimerFill');
        if (!clockEl || !fillEl) return;

        const m = Math.floor(timerRemaining / 60);
        const s = timerRemaining % 60;
        clockEl.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;

        const pct = (timerRemaining / timerTotalSeconds) * 100;
        fillEl.style.width = `${pct}%`;

        if (timerRemaining <= 60) {
            clockEl.style.color = '#dc2626';
            clockEl.style.animation = 'pulse 1s infinite alternate';
        } else {
            clockEl.style.color = '#dc2626';
            clockEl.style.animation = 'none';
        }
    }

    function startTimer() {
        if (isTimerRunning) return;
        isTimerRunning = true;
        const btn = document.getElementById('btnTimerToggle');
        if (btn) btn.innerHTML = '⏸️ Tạm Dừng';

        timerInterval = setInterval(() => {
            if (timerRemaining > 0) {
                timerRemaining--;
                updateTimerUI();
            } else {
                stopTimer();
                alert('⏰ Hết thời gian 5 phút thi vấn đáp! Bạn đã hoàn thành lượt luyện tập xuất sắc.');
            }
        }, 1000);
    }

    function stopTimer() {
        isTimerRunning = false;
        if (timerInterval) clearInterval(timerInterval);
        timerInterval = null;
        const btn = document.getElementById('btnTimerToggle');
        if (btn) btn.innerHTML = '▶️ Tiếp Tục';
    }

    function toggleTimer() {
        if (isTimerRunning) {
            stopTimer();
        } else {
            startTimer();
        }
    }

    function resetTimer() {
        stopTimer();
        timerRemaining = timerTotalSeconds;
        updateTimerUI();
        const btn = document.getElementById('btnTimerToggle');
        if (btn) btn.innerHTML = '▶️ Bắt Đầu 5 Phút';
    }

    // ==========================================================================
    // TOPIC SWITCHING
    // ==========================================================================
    function switchTopic(topicId) {
        if (!TOPICS.some(t => t.id === topicId)) return;
        currentTopicId = topicId;
        currentQuestionIdx = 0;
        isFlipped = false;
        try {
            window.location.hash = topicId;
        } catch (e) {}

        renderTopicTabs();
        renderCurrentMode();
    }

    function renderTopicTabs() {
        const container = document.getElementById('topicGridContainer');
        if (!container) return;

        container.innerHTML = TOPICS.map(topic => {
            const isActive = (topic.id === currentTopicId);
            return `
                <div class="topic-card-btn ${isActive ? 'active' : ''}" onclick="window.KaiwaStudio.switchTopic('${topic.id}')">
                    <div>
                        <span class="topic-card-badge">${topic.badge}</span>
                        <div class="topic-card-title">${topic.title}</div>
                        <div class="topic-card-jp">${topic.titleJp}</div>
                    </div>
                    <div class="topic-card-meta">
                        <span>📋 ${topic.coreQuestions.length} câu hỏi trọng tâm</span>
                        <span>•</span>
                        <span>⏱️ 5 phút</span>
                    </div>
                </div>
            `;
        }).join('');
    }

    // ==========================================================================
    // MODE SWITCHING
    // ==========================================================================
    function switchMode(mode) {
        currentMode = mode;
        document.querySelectorAll('.mode-tab-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });

        document.getElementById('viewSimulator').style.display = (mode === 'simulator') ? 'block' : 'none';
        document.getElementById('viewFlashcard').style.display = (mode === 'flashcard') ? 'block' : 'none';
        document.getElementById('viewDialogue').style.display = (mode === 'dialogue') ? 'block' : 'none';
        document.getElementById('viewTips').style.display = (mode === 'tips') ? 'block' : 'none';

        renderCurrentMode();
    }

    function renderCurrentMode() {
        if (currentMode === 'simulator') {
            renderSimulator();
        } else if (currentMode === 'flashcard') {
            renderFlashcard();
        } else if (currentMode === 'dialogue') {
            renderDialogue();
        } else if (currentMode === 'tips') {
            renderTips();
        }
    }

    // ==========================================================================
    // 1. RENDER SIMULATOR (CHẾ ĐỘ THI THỬ 5 PHÚT)
    // ==========================================================================
    function renderSimulator() {
        const topic = getCurrentTopic();
        const q = topic.coreQuestions[currentQuestionIdx];
        if (!q) return;

        // Prompt sheet thumbnail banner
        const sheetCard = document.getElementById('promptSheetCallout');
        if (sheetCard) {
            sheetCard.innerHTML = `
                <div class="prompt-sheet-left">
                    <img src="${topic.image}" alt="Đề cô giáo" class="prompt-sheet-thumb" onclick="window.KaiwaStudio.openImageModal('${topic.image}', '${topic.title}')" title="Bấm để xem ảnh đề cô giáo phóng to">
                    <div class="prompt-sheet-info">
                        <h3>📄 Đề Gốc Của Cô Giáo: ${topic.title}</h3>
                        <p>${topic.desc}</p>
                    </div>
                </div>
                <button type="button" class="btn-view-sheet" onclick="window.KaiwaStudio.openImageModal('${topic.image}', '${topic.title}')">
                    🔍 Xem Ảnh Đề Gốc
                </button>
            `;
        }

        // Question Stage
        const qBadge = document.getElementById('stageQBadge');
        if (qBadge) qBadge.textContent = `CÂU HỎI ${currentQuestionIdx + 1} / ${topic.coreQuestions.length}`;

        const qTextEl = document.getElementById('senseiQText');
        if (qTextEl) qTextEl.textContent = q.qJp;

        const qViEl = document.getElementById('senseiQVi');
        if (qViEl) {
            qViEl.textContent = q.qVi;
            qViEl.style.display = showVi ? 'block' : 'none';
        }

        const intentEl = document.getElementById('senseiIntentNote');
        if (intentEl) {
            intentEl.innerHTML = `<span>🎯 <strong>Mục đích cô giáo hỏi:</strong> ${q.intent}</span>`;
            intentEl.style.display = showVi ? 'flex' : 'none';
        }

        // Mindmap
        const mmBox = document.getElementById('mindmapBox');
        if (mmBox) {
            mmBox.style.display = showMindmap ? 'block' : 'none';
            const chipsEl = document.getElementById('mindmapChips');
            if (chipsEl) {
                chipsEl.innerHTML = q.mindmap.map(idea => `<span class="mindmap-chip">💡 ${idea}</span>`).join('');
            }
        }

        // Sample answers
        const ansWrap = document.getElementById('sampleAnswersWrap');
        if (ansWrap) {
            ansWrap.style.display = showAnswers ? 'block' : 'none';
            const listEl = document.getElementById('answersListContainer');
            if (listEl) {
                listEl.innerHTML = q.sampleAnswers.map(ans => {
                    const isAdv = (ans.level === 'advanced');
                    const cleanJp = ans.jp.replace(/'/g, "\\'");
                    return `
                        <div class="answer-card ${isAdv ? 'is-advanced' : 'is-basic'}">
                            <div class="answer-header">
                                <span class="answer-level-badge ${isAdv ? 'badge-advanced' : 'badge-basic'}">${ans.tag}</span>
                                <button type="button" class="btn-speak-ans" onclick="window.KaiwaStudio.playAudio('${cleanJp}', this)">
                                    🔊 Nghe mẫu
                                </button>
                            </div>
                            <div class="answer-jp jp-font">${ans.jp}</div>
                            <div class="answer-vi" style="display: ${showVi ? 'block' : 'none'}">${ans.vi}</div>
                            <div class="answer-tip">
                                <strong>💡 Mẹo dùng:</strong> ${ans.keyPoints}
                            </div>
                        </div>
                    `;
                }).join('');
            }
        }

        // Question dots
        const dotsEl = document.getElementById('qDotsStrip');
        if (dotsEl) {
            dotsEl.innerHTML = topic.coreQuestions.map((item, idx) => {
                const isActive = (idx === currentQuestionIdx);
                return `
                    <button type="button" class="q-dot-btn ${isActive ? 'active' : ''}" onclick="window.KaiwaStudio.goToQuestion(${idx})">
                        ${idx + 1}
                    </button>
                `;
            }).join('');
        }

        // Nav buttons
        const prevBtn = document.getElementById('btnPrevQ');
        if (prevBtn) prevBtn.disabled = (currentQuestionIdx === 0);

        const nextBtn = document.getElementById('btnNextQ');
        if (nextBtn) {
            if (currentQuestionIdx === topic.coreQuestions.length - 1) {
                nextBtn.innerHTML = '🎉 Đã Hết Bộ Câu Hỏi';
            } else {
                nextBtn.innerHTML = 'Câu Tiếp Theo (Sensei Hỏi) ➡️';
            }
        }
    }

    function goToQuestion(idx) {
        const topic = getCurrentTopic();
        if (idx < 0 || idx >= topic.coreQuestions.length) return;
        currentQuestionIdx = idx;
        renderSimulator();
        // Tự động đọc câu hỏi mới bằng giọng Sensei Tokyo
        const q = topic.coreQuestions[currentQuestionIdx];
        if (q && isTimerRunning) {
            playAudio(q.qJp, document.getElementById('btnSpeakSensei'));
        }
    }

    function prevQuestion() {
        if (currentQuestionIdx > 0) {
            goToQuestion(currentQuestionIdx - 1);
        }
    }

    function nextQuestion() {
        const topic = getCurrentTopic();
        if (currentQuestionIdx < topic.coreQuestions.length - 1) {
            goToQuestion(currentQuestionIdx + 1);
        } else {
            // Loop back or finish
            goToQuestion(0);
        }
    }

    function playSenseiQuestion() {
        const topic = getCurrentTopic();
        const q = topic.coreQuestions[currentQuestionIdx];
        if (!q) return;
        playAudio(q.qJp, document.getElementById('btnSpeakSensei'));
    }

    function toggleViewOption(opt) {
        if (opt === 'vi') {
            showVi = !showVi;
        } else if (opt === 'mindmap') {
            showMindmap = !showMindmap;
        } else if (opt === 'answers') {
            showAnswers = !showAnswers;
        }
        renderSimulator();
    }

    // ==========================================================================
    // 2. RENDER FLASHCARD (CHẾ ĐỘ THẺ PHẢN XẠ NHANH)
    // ==========================================================================
    function renderFlashcard() {
        const topic = getCurrentTopic();
        const q = topic.coreQuestions[currentQuestionIdx];
        if (!q) return;

        const container = document.getElementById('flashcardContainer');
        if (!container) return;

        const bestAnswer = q.sampleAnswers[0];
        const advAnswer = q.sampleAnswers[1] || q.sampleAnswers[0];

        container.innerHTML = `
            <div class="fc-card-container" onclick="window.KaiwaStudio.toggleFlipCard()">
                <div class="fc-card-inner ${isFlipped ? 'flipped' : ''}" id="fcCardInner">
                    <!-- Front Side (Question) -->
                    <div class="fc-front">
                        <div class="fc-top-badge">
                            <span class="topic-card-badge">${topic.title}</span>
                            <span style="color: #64748b;">Câu ${currentQuestionIdx + 1} / ${topic.coreQuestions.length}</span>
                        </div>
                        <div>
                            <div class="fc-front-title">${q.qJp}</div>
                            <div class="fc-front-hint">❓ ${q.qVi}</div>
                        </div>
                        <div class="fc-bottom-tap">
                            👆 Bấm vào thẻ để lật xem đáp án mẫu & từ vựng
                        </div>
                    </div>

                    <!-- Back Side (Answer) -->
                    <div class="fc-back">
                        <div class="fc-top-badge">
                            <span style="color: #047857; font-weight:800;">✓ ĐÁP ÁN GỢI Ý</span>
                            <button type="button" class="btn-speak-ans" onclick="event.stopPropagation(); window.KaiwaStudio.playAudio('${bestAnswer.jp.replace(/'/g, "\\'")}', this)">
                                🔊 Nghe
                            </button>
                        </div>
                        <div style="margin: 12px 0;">
                            <div class="answer-jp" style="font-size: 1.15rem; color:#065f46;">${bestAnswer.jp}</div>
                            <div class="answer-vi" style="font-size: 0.92rem; color:#475569;">${bestAnswer.vi}</div>
                        </div>
                        <div class="mindmap-box" style="margin-bottom: 8px; padding: 10px;">
                            <div class="mindmap-title" style="font-size: 0.78rem;">💡 Từ vựng then chốt:</div>
                            <div class="mindmap-chips">
                                ${q.vocab.map(v => `<span class="mindmap-chip" style="font-size:0.75rem;">${v.jp}: ${v.vi}</span>`).join('')}
                            </div>
                        </div>
                        <div class="fc-bottom-tap">
                            👆 Bấm để lật lại câu hỏi
                        </div>
                    </div>
                </div>
            </div>

            <div class="fc-controls-bar">
                <button type="button" class="btn-stage-nav" onclick="window.KaiwaStudio.prevQuestion()" ${currentQuestionIdx === 0 ? 'disabled' : ''}>
                    ⬅️ Câu trước
                </button>
                <button type="button" class="btn-stage-nav" onclick="window.KaiwaStudio.playAudio('${q.qJp.replace(/'/g, "\\'")}', this)">
                    🔊 Nghe câu hỏi
                </button>
                <button type="button" class="btn-stage-nav btn-stage-next" onclick="window.KaiwaStudio.nextQuestion()">
                    Câu tiếp theo ➡️
                </button>
            </div>
        `;
    }

    function toggleFlipCard() {
        isFlipped = !isFlipped;
        const inner = document.getElementById('fcCardInner');
        if (inner) inner.classList.toggle('flipped', isFlipped);
    }

    // ==========================================================================
    // 3. RENDER DIALOGUE (CHẾ ĐỘ KỊCH BẢN ĐỐI THOẠI SONG NGỮ)
    // ==========================================================================
    function renderDialogue() {
        const topic = getCurrentTopic();
        const container = document.getElementById('dialogueChatContainer');
        if (!container) return;

        container.innerHTML = topic.fullDialogue.map((line, idx) => {
            const isSensei = (line.speaker === 'sensei');
            const cleanJp = line.jp.replace(/'/g, "\\'");
            return `
                <div class="chat-bubble-row ${isSensei ? 'is-sensei' : 'is-gakusei'}">
                    ${isSensei ? `
                        <div class="chat-avatar avatar-sensei" title="Sensei">👩‍🏫</div>
                    ` : ''}
                    <div class="chat-bubble ${isSensei ? 'bubble-sensei' : 'bubble-gakusei'}">
                        <div class="chat-speaker-name ${isSensei ? 'name-sensei' : 'name-gakusei'}">
                            <span>${line.name}</span>
                            <button type="button" class="btn-speak-ans" style="padding: 2px 8px; font-size: 0.75rem;" onclick="window.KaiwaStudio.playAudio('${cleanJp}', this)">
                                🔊 Nghe
                            </button>
                        </div>
                        <div class="chat-jp-text">${line.jp}</div>
                        <div class="chat-vi-text">${line.vi}</div>
                    </div>
                    ${!isSensei ? `
                        <div class="chat-avatar avatar-gakusei" title="Bạn (Học sinh)">🙋‍♂️</div>
                    ` : ''}
                </div>
            `;
        }).join('');
    }

    // ==========================================================================
    // 4. RENDER TIPS (CHẾ ĐỘ 5 MẸO GHI ĐIỂM KAIWA)
    // ==========================================================================
    function renderTips() {
        const container = document.getElementById('tipsGridContainer');
        if (!container) return;

        container.innerHTML = TIPS.map(tip => {
            return `
                <div class="tip-card">
                    <h3>${tip.title}</h3>
                    <p>${tip.desc}</p>
                    ${tip.formula ? `
                        <div style="background: #eef2ff; border: 1px solid #c7d2fe; padding: 10px 14px; border-radius: 8px; font-weight: 700; color: #3730a3; margin-bottom: 10px;">
                            ${tip.formula}
                        </div>
                    ` : ''}
                    ${tip.example ? `
                        <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 10px 14px; border-radius: 8px; color: #047857; margin-bottom: 10px; font-family: 'Noto Sans JP', sans-serif;">
                            ${tip.example}
                        </div>
                    ` : ''}
                    ${tip.phrases ? `
                        <div class="tip-phrase-grid">
                            ${tip.phrases.map(p => `
                                <div class="tip-phrase-item">
                                    <div class="tip-phrase-jp">${p.jp}</div>
                                    <div class="tip-phrase-vi">${p.vi}</div>
                                </div>
                            `).join('')}
                        </div>
                    ` : ''}
                </div>
            `;
        }).join('');
    }

    // ==========================================================================
    // MODAL IMAGE VIEWER
    // ==========================================================================
    function openImageModal(src, title) {
        const modal = document.getElementById('kaiwaImageModal');
        const img = document.getElementById('modalPreviewImage');
        const titleEl = document.getElementById('modalImageTitle');
        if (!modal || !img) return;

        img.src = src;
        if (titleEl) titleEl.textContent = title || 'Đề gốc cô giáo';
        modal.classList.add('show');
    }

    function closeImageModal() {
        const modal = document.getElementById('kaiwaImageModal');
        if (modal) modal.classList.remove('show');
    }

    // ==========================================================================
    // INITIALIZATION
    // ==========================================================================
    function init() {
        renderTopicTabs();
        updateTimerUI();
        switchMode('simulator');

        // Close modal on Escape
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') closeImageModal();
        });

        // Hash change
        window.addEventListener('hashchange', () => {
            const h = (window.location.hash || '').replace('#', '').trim();
            if (h && TOPICS.some(t => t.id === h) && h !== currentTopicId) {
                switchTopic(h);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Public API for HTML interactions
    window.KaiwaStudio = {
        switchTopic,
        switchMode,
        goToQuestion,
        prevQuestion,
        nextQuestion,
        toggleTimer,
        resetTimer,
        playSenseiQuestion,
        toggleViewOption,
        toggleFlipCard,
        playAudio,
        openImageModal,
        closeImageModal
    };

})(window, document);
