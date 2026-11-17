/**
 * MARUGOTO A2.1 KAIWA INTERVIEW STUDIO CONTROLLER (assets/js/pages/kaiwa-studio.js)
 * Điều khiển toàn bộ phòng luyện Kaiwa 5 phút:
 *  - 4 chủ đề câu hỏi bám sát đề thi cô giáo:
 *    1. Bảo vệ sức khỏe (Bài 15)
 *    2. Thăm hỏi sức khỏe & Lời khuyên (Bài 16)
 *    3. Trao đổi tiệc chúc mừng kết hôn (Bài 17-18)
 *    4. Kinh nghiệm du lịch Nhật Bản (Đề mới - Bài 11-12)
 *  - 4 chế độ học:
 *    1. Danh Sách Hỏi - Đáp Toàn Diện (qalist) - Mặc định, cuộn xem toàn bộ câu hỏi và đáp án mẫu
 *    2. Kịch Bản Đối Thoại Song Ngữ (dialogue) - Luyện Shadowing đóng vai Sensei & Bạn
 *    3. Phòng Thi Thử 5 Phút (simulator) - Đếm ngược 5:00 và phản xạ từng câu
 *    4. 5 Bí Kíp Ghi Điểm Vấn Đáp (tips) - Chiến thuật Aizuchi, filler words
 */

(function (window, document) {
    'use strict';

    const TOPICS = window.KAIWA_TOPICS_DATA || [];
    const TIPS = window.KAIWA_TIPS || [];

    // State
    let currentTopicId = getInitialTopic();
    let currentMode = 'qalist'; // 'qalist' | 'dialogue' | 'simulator' | 'tips'
    let currentQuestionIdx = 0;
    let timerTotalSeconds = 5 * 60; // 5 phút chuẩn phòng thi
    let timerRemaining = timerTotalSeconds;
    let timerInterval = null;
    let isTimerRunning = false;

    // View options
    let showVi = true;
    let showMindmap = true;
    let showAnswers = true;
    const STORAGE_KEY = 'marugoto_kaiwa_session_v1';
    let deadline = null;
    let resetting = false;
    window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;
    window.__MARUGOTO_CP_EXTRA_KEYS__ = [...new Set([...(window.__MARUGOTO_CP_EXTRA_KEYS__ || []), STORAGE_KEY])];
    window.__MARUGOTO_ON_RESET__ = () => {
        resetting = true;
        if (timerInterval) clearInterval(timerInterval);
        window.AudioEngine?.stop();
        window.location.reload();
    };

    function saveSession() {
        if (resetting) return;
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify({
                version: 1, currentTopicId, currentMode, currentQuestionIdx,
                timerRemaining, deadline, showVi, showMindmap, showAnswers
            }));
        } catch (error) { /* Continue without persistence when storage is blocked. */ }
    }

    function restoreSession() {
        try {
            const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
            if (!saved || saved.version !== 1) return;
            const explicitTopic = location.hash.slice(1);
            const topic = TOPICS.find(t => t.id === explicitTopic) || TOPICS.find(t => t.id === saved.currentTopicId);
            if (topic) currentTopicId = topic.id;
            if (['qalist', 'dialogue', 'simulator', 'tips'].includes(saved.currentMode)) currentMode = saved.currentMode;
            if (topic && topic.id === saved.currentTopicId && Number.isInteger(saved.currentQuestionIdx) &&
                saved.currentQuestionIdx >= 0 && saved.currentQuestionIdx < topic.coreQuestions.length) {
                currentQuestionIdx = saved.currentQuestionIdx;
            }
            for (const key of ['showVi', 'showMindmap', 'showAnswers']) {
                if (typeof saved[key] !== 'boolean') continue;
                if (key === 'showVi') showVi = saved[key];
                if (key === 'showMindmap') showMindmap = saved[key];
                if (key === 'showAnswers') showAnswers = saved[key];
            }
            if (Number.isFinite(saved.timerRemaining) && saved.timerRemaining >= 0 && saved.timerRemaining <= timerTotalSeconds) {
                timerRemaining = Math.ceil(saved.timerRemaining);
            }
            if (Number.isFinite(saved.deadline) && saved.deadline > 0 && saved.deadline <= Date.now() + timerTotalSeconds * 1000) {
                timerRemaining = Math.max(0, Math.ceil((saved.deadline - Date.now()) / 1000));
                if (timerRemaining > 0) deadline = saved.deadline;
            }
        } catch (error) {}
    }

    function syncTimer() {
        if (deadline !== null) timerRemaining = Math.max(0, Math.ceil((deadline - Date.now()) / 1000));
        updateTimerUI();
        if (isTimerRunning && timerRemaining === 0) {
            stopTimer();
            const btn = document.getElementById('btnTimerToggle');
            if (btn) btn.textContent = 'Đã hết 5 phút';
            alert('⏰ Hết thời gian 5 phút thi vấn đáp!');
        }
    }

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

    function escapeHtml(text) {
        if (!text) return '';
        return String(text)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
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
        } else {
            try {
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'ja-JP';
                u.rate = 0.92;
                window.speechSynthesis.speak(u);
            } catch (e) {
                console.warn('Audio playback error:', e);
            }
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
        if (isTimerRunning || timerRemaining === 0) return;
        if (deadline === null) deadline = Date.now() + timerRemaining * 1000;
        isTimerRunning = true;
        const btn = document.getElementById('btnTimerToggle');
        if (btn) btn.innerHTML = '⏸️ Tạm Dừng';

        timerInterval = setInterval(syncTimer, 250);
        saveSession();
        syncTimer();
    }

    function stopTimer() {
        if (deadline !== null) timerRemaining = Math.max(0, Math.ceil((deadline - Date.now()) / 1000));
        deadline = null;
        isTimerRunning = false;
        if (timerInterval) clearInterval(timerInterval);
        timerInterval = null;
        const btn = document.getElementById('btnTimerToggle');
        if (btn) btn.innerHTML = '▶️ Tiếp Tục';
        saveSession();
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
        saveSession();
    }

    // ==========================================================================
    // TOPIC SWITCHING
    // ==========================================================================
    function switchTopic(topicId, updateHash = true) {
        if (!TOPICS.some(t => t.id === topicId)) return;
        if (topicId === currentTopicId) return;
        window.AudioEngine?.stop();
        currentTopicId = topicId;
        currentQuestionIdx = 0;
        try {
            if (updateHash) window.location.hash = topicId;
        } catch (e) {}

        renderTopicTabs();
        renderActiveTopicBanner();
        renderCurrentMode();
        saveSession();
    }

    function renderTopicTabs() {
        const container = document.getElementById('topicGridContainer');
        if (!container) return;

        container.innerHTML = TOPICS.map(topic => {
            const isActive = (topic.id === currentTopicId);
            let icon = '🌿';
            if (topic.id === 'topic2') icon = '💊';
            if (topic.id === 'topic3') icon = '🎁';
            if (topic.id === 'topic4') icon = '🗾';

            return `
                <button type="button" class="topic-pill-btn ${isActive ? 'active' : ''}" onclick="window.KaiwaStudio.switchTopic('${topic.id}')">
                    <span class="topic-pill-icon">${icon}</span>
                    <div class="topic-pill-text">
                        <span class="topic-pill-title">Chủ Đề ${topic.num}: ${escapeHtml(topic.title)}</span>
                        <span class="topic-pill-sub">${escapeHtml(topic.titleJp)}</span>
                    </div>
                    <span class="topic-pill-badge">${topic.coreQuestions.length} câu hỏi</span>
                </button>
            `;
        }).join('');
    }

    function renderActiveTopicBanner() {
        const banner = document.getElementById('topicActiveBanner');
        if (!banner) return;
        const topic = getCurrentTopic();

        banner.innerHTML = `
            <div class="active-banner-content">
                <img src="${topic.image}" alt="${escapeHtml(topic.title)}" class="active-banner-thumb" onclick="window.KaiwaStudio.openImageModal('${topic.image}', '${escapeHtml(topic.title)}')" title="Bấm để xem ảnh đề thi phóng to">
                <div class="active-banner-info">
                    <div class="active-banner-tags">
                        <span class="active-banner-badge">${escapeHtml(topic.badge)}</span>
                        <span class="active-banner-lesson">${escapeHtml(topic.lessonRef)}</span>
                    </div>
                    <h2 class="active-banner-title">
                        <span>Chủ Đề ${topic.num}: ${escapeHtml(topic.title)}</span>
                        <span class="active-banner-title-jp">「${escapeHtml(topic.titleJp)}」</span>
                    </h2>
                    <p class="active-banner-desc">${escapeHtml(topic.desc)}</p>
                </div>
                <button type="button" class="btn-open-sheet" onclick="window.KaiwaStudio.openImageModal('${topic.image}', '${escapeHtml(topic.title)}')">
                    🔍 Xem Ảnh Đề Gốc
                </button>
            </div>
        `;
    }

    // ==========================================================================
    // MODE SWITCHING
    // ==========================================================================
    function switchMode(mode) {
        if (!['qalist', 'dialogue', 'simulator', 'tips'].includes(mode)) return;
        currentMode = mode;
        document.querySelectorAll('.mode-tab-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });

        const vQAList = document.getElementById('viewQAList');
        const vDialogue = document.getElementById('viewDialogue');
        const vSimulator = document.getElementById('viewSimulator');
        const vTips = document.getElementById('viewTips');

        if (vQAList) vQAList.style.display = (mode === 'qalist') ? 'block' : 'none';
        if (vDialogue) vDialogue.style.display = (mode === 'dialogue') ? 'block' : 'none';
        if (vSimulator) vSimulator.style.display = (mode === 'simulator') ? 'block' : 'none';
        if (vTips) vTips.style.display = (mode === 'tips') ? 'block' : 'none';

        renderCurrentMode();
        saveSession();
    }

    function renderCurrentMode() {
        if (currentMode === 'qalist') {
            renderQAList();
        } else if (currentMode === 'dialogue') {
            renderDialogue();
        } else if (currentMode === 'simulator') {
            renderSimulator();
        } else if (currentMode === 'tips') {
            renderTips();
        }
    }

    // ==========================================================================
    // 1. RENDER QA LIST (CHẾ ĐỘ HỌC CHÍNH - XEM TOÀN BỘ CÂU HỎI TRỰC QUAN)
    // ==========================================================================
    function renderQAList() {
        const topic = getCurrentTopic();
        const container = document.getElementById('qalistContainer');
        const statsEl = document.getElementById('qalistStats');
        if (!container) return;

        if (statsEl) {
            statsEl.innerHTML = `
                <span>📋 Trọn bộ <b>${topic.coreQuestions.length} câu hỏi trọng tâm</b> kèm audio Tokyo &amp; câu trả lời mẫu 2 cấp độ</span>
            `;
        }

        // Cập nhật text trên các nút toolbar
        const lblVi = document.getElementById('lblToggleVi');
        if (lblVi) lblVi.textContent = showVi ? 'BẬT' : 'TẮT';
        const lblMm = document.getElementById('lblToggleMindmap');
        if (lblMm) lblMm.textContent = showMindmap ? 'BẬT' : 'TẮT';

        container.innerHTML = topic.coreQuestions.map((q, idx) => {
            const cleanQ = q.qJp.replace(/'/g, "\\'");
            return `
                <article class="qalist-card" id="qcard-${idx}">
                    <!-- Card Top Header -->
                    <div class="qalist-card-header">
                        <div class="qalist-num-group">
                            <span class="qalist-q-badge">CÂU HỎI ${idx + 1} / ${topic.coreQuestions.length}</span>
                            <span class="qalist-target-tag">Mục tiêu: ${escapeHtml(q.intent)}</span>
                        </div>
                        <button type="button" class="btn-speak-sensei" onclick="window.KaiwaStudio.playAudio('${cleanQ}', this)" title="Nghe giáo viên Tokyo phát âm câu hỏi">
                            🔊 Nghe Sensei Hỏi
                        </button>
                    </div>

                    <!-- Sensei Question -->
                    <div class="qalist-question-box">
                        <div class="qalist-q-jp jp-font">${escapeHtml(q.qJp)}</div>
                        <div class="qalist-q-vi" style="display: ${showVi ? 'block' : 'none'};">
                            👉 <b>Ý nghĩa:</b> ${escapeHtml(q.qVi)}
                        </div>
                    </div>

                    <!-- Mindmap Reflex Ideas -->
                    <div class="qalist-mindmap-box" style="display: ${showMindmap ? 'block' : 'none'};">
                        <div class="qalist-mindmap-title">💡 Ý tưởng phản xạ nhanh (Mindmap bật nói):</div>
                        <div class="mindmap-chips">
                            ${q.mindmap.map(idea => `<span class="mindmap-chip">✦ ${escapeHtml(idea)}</span>`).join('')}
                        </div>
                    </div>

                    <!-- Sample Answers Area -->
                    <div class="qalist-answers-section">
                        <div class="qalist-answers-title">🌟 MẪU CÂU TRẢ LỜI GỢI Ý (BẬT NÓI TỰ TIN):</div>
                        <div class="qalist-answers-grid">
                            ${q.sampleAnswers.map(ans => {
                                const isAdv = (ans.level === 'advanced');
                                const cleanAns = ans.jp.replace(/'/g, "\\'");
                                return `
                                    <div class="answer-card ${isAdv ? 'is-advanced' : 'is-basic'}">
                                        <div class="answer-header">
                                            <span class="answer-level-badge ${isAdv ? 'badge-advanced' : 'badge-basic'}">
                                                ${isAdv ? '🟣 Nâng cao / Tự nhiên (A2+)' : '🟢 Chuẩn cơ bản (A2.1)'} • ${escapeHtml(ans.tag)}
                                            </span>
                                            <button type="button" class="btn-speak-ans" onclick="window.KaiwaStudio.playAudio('${cleanAns}', this)" title="Nghe mẫu phát âm câu này">
                                                🔊 Nghe mẫu
                                            </button>
                                        </div>
                                        <div class="answer-jp jp-font">${escapeHtml(ans.jp)}</div>
                                        <div class="answer-vi" style="display: ${showVi ? 'block' : 'none'};">
                                            ${escapeHtml(ans.vi)}
                                        </div>
                                        <div class="answer-tip">
                                            <strong>💡 Mẹo dùng:</strong> ${escapeHtml(ans.keyPoints)}
                                        </div>
                                    </div>
                                `;
                            }).join('')}
                        </div>
                    </div>

                    <!-- Vocabulary Gold Footnote -->
                    ${(q.vocab && q.vocab.length) ? `
                        <div class="qalist-vocab-bar">
                            <span class="qalist-vocab-title">📖 Từ vựng then chốt:</span>
                            <div class="qalist-vocab-tags">
                                ${q.vocab.map(v => `<span class="qalist-vocab-tag"><b>${escapeHtml(v.jp)}</b>: ${escapeHtml(v.vi)}</span>`).join('')}
                            </div>
                        </div>
                    ` : ''}
                </article>
            `;
        }).join('');
    }

    // ==========================================================================
    // 2. RENDER DIALOGUE (CHẾ ĐỘ KỊCH BẢN ĐỐI THOẠI SONG NGỮ)
    // ==========================================================================
    function renderDialogue() {
        const topic = getCurrentTopic();
        const container = document.getElementById('dialogueChatContainer');
        if (!container) return;

        container.innerHTML = topic.fullDialogue.map(line => {
            const isSensei = (line.speaker === 'sensei');
            const cleanJp = line.jp.replace(/'/g, "\\'");
            return `
                <div class="chat-bubble-row ${isSensei ? 'is-sensei' : 'is-gakusei'}">
                    ${isSensei ? `
                        <div class="chat-avatar avatar-sensei" title="Sensei">👩‍🏫</div>
                    ` : ''}
                    <div class="chat-bubble ${isSensei ? 'bubble-sensei' : 'bubble-gakusei'}">
                        <div class="chat-speaker-name ${isSensei ? 'name-sensei' : 'name-gakusei'}">
                            <span>${escapeHtml(line.name)}</span>
                            <button type="button" class="btn-speak-ans" style="padding: 2px 8px; font-size: 0.75rem;" onclick="window.KaiwaStudio.playAudio('${cleanJp}', this)">
                                🔊 Nghe
                            </button>
                        </div>
                        <div class="chat-jp-text jp-font">${escapeHtml(line.jp)}</div>
                        <div class="chat-vi-text">${escapeHtml(line.vi)}</div>
                    </div>
                    ${!isSensei ? `
                        <div class="chat-avatar avatar-gakusei" title="Bạn (Học sinh)">🙋‍♂️</div>
                    ` : ''}
                </div>
            `;
        }).join('');
    }

    // ==========================================================================
    // 3. RENDER SIMULATOR (CHẾ ĐỘ THI THỬ 5 PHÚT BẤM GIỜ)
    // ==========================================================================
    function renderSimulator() {
        const topic = getCurrentTopic();
        const q = topic.coreQuestions[currentQuestionIdx];
        if (!q) return;

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
            intentEl.innerHTML = `<span>🎯 <strong>Mục đích cô giáo hỏi:</strong> ${escapeHtml(q.intent)}</span>`;
            intentEl.style.display = showVi ? 'flex' : 'none';
        }

        // Mindmap
        const mmBox = document.getElementById('mindmapBox');
        if (mmBox) {
            mmBox.style.display = showMindmap ? 'block' : 'none';
            const chipsEl = document.getElementById('mindmapChips');
            if (chipsEl) {
                chipsEl.innerHTML = q.mindmap.map(idea => `<span class="mindmap-chip">💡 ${escapeHtml(idea)}</span>`).join('');
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
                    const cleanAns = ans.jp.replace(/'/g, "\\'");
                    return `
                        <div class="answer-card ${isAdv ? 'is-advanced' : 'is-basic'}">
                            <div class="answer-header">
                                <span class="answer-level-badge ${isAdv ? 'badge-advanced' : 'badge-basic'}">${escapeHtml(ans.tag)}</span>
                                <button type="button" class="btn-speak-ans" onclick="window.KaiwaStudio.playAudio('${cleanAns}', this)">
                                    🔊 Nghe mẫu
                                </button>
                            </div>
                            <div class="answer-jp jp-font">${escapeHtml(ans.jp)}</div>
                            <div class="answer-vi" style="display: ${showVi ? 'block' : 'none'}">${escapeHtml(ans.vi)}</div>
                            <div class="answer-tip">
                                <strong>💡 Mẹo dùng:</strong> ${escapeHtml(ans.keyPoints)}
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
        saveSession();
        // Tự động đọc câu hỏi mới nếu đang bật timer
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
            const chk = document.getElementById('chkShowVi');
            if (chk) chk.checked = showVi;
        } else if (opt === 'mindmap') {
            showMindmap = !showMindmap;
            const chk = document.getElementById('chkShowMindmap');
            if (chk) chk.checked = showMindmap;
        } else if (opt === 'answers') {
            showAnswers = !showAnswers;
            const chk = document.getElementById('chkShowAnswers');
            if (chk) chk.checked = showAnswers;
        }

        if (currentMode === 'qalist') {
            renderQAList();
        } else if (currentMode === 'simulator') {
            renderSimulator();
        }
        saveSession();
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
                    <h3>${escapeHtml(tip.title)}</h3>
                    <p>${escapeHtml(tip.desc)}</p>
                    ${tip.formula ? `
                        <div style="background: #eef2ff; border: 1px solid #c7d2fe; padding: 10px 14px; border-radius: 8px; font-weight: 700; color: #3730a3; margin-bottom: 10px;">
                            ${escapeHtml(tip.formula)}
                        </div>
                    ` : ''}
                    ${tip.example ? `
                        <div style="background: #ecfdf5; border: 1px solid #a7f3d0; padding: 10px 14px; border-radius: 8px; color: #047857; margin-bottom: 10px; font-family: 'Noto Sans JP', sans-serif;">
                            ${escapeHtml(tip.example)}
                        </div>
                    ` : ''}
                    ${tip.phrases ? `
                        <div class="tip-phrase-grid">
                            ${tip.phrases.map(p => `
                                <div class="tip-phrase-item">
                                    <div class="tip-phrase-jp jp-font">${escapeHtml(p.jp)}</div>
                                    <div class="tip-phrase-vi">${escapeHtml(p.vi)}</div>
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
        if (titleEl) titleEl.textContent = `📄 Ảnh Đề Gốc Cô Giáo: ${title}`;
        modal.classList.add('show');
    }

    function closeImageModal() {
        const modal = document.getElementById('kaiwaImageModal');
        if (modal) modal.classList.remove('show');
    }

    function openCurrentTopicSheet() {
        const topic = getCurrentTopic();
        if (topic && topic.image) {
            openImageModal(topic.image, topic.title);
        }
    }

    // ==========================================================================
    // INITIALIZATION
    // ==========================================================================
    function init() {
        restoreSession();
        renderTopicTabs();
        renderActiveTopicBanner();
        switchMode(currentMode);
        updateTimerUI();
        for (const [id, checked] of [['chkShowVi', showVi], ['chkShowMindmap', showMindmap], ['chkShowAnswers', showAnswers]]) {
            const input = document.getElementById(id);
            if (input) input.checked = checked;
        }
        if (deadline !== null) startTimer();
        else if (timerRemaining < timerTotalSeconds) {
            const btn = document.getElementById('btnTimerToggle');
            if (btn) btn.textContent = timerRemaining === 0 ? 'Đã hết 5 phút' : '▶️ Tiếp Tục';
        }
        window.addEventListener('hashchange', () => {
            const topic = location.hash.slice(1);
            switchTopic(TOPICS.some(t => t.id === topic) ? topic : 'topic1', false);
        });
        document.addEventListener('visibilitychange', syncTimer);
        window.addEventListener('pagehide', saveSession);

        // Keyboard navigation
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') {
                closeImageModal();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Export to global scope
    window.KaiwaStudio = {
        switchTopic,
        switchMode,
        playAudio,
        toggleTimer,
        resetTimer,
        goToQuestion,
        prevQuestion,
        nextQuestion,
        playSenseiQuestion,
        toggleViewOption,
        openImageModal,
        closeImageModal,
        openCurrentTopicSheet
    };

})(window, document);
