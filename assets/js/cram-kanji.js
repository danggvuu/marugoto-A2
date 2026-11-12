/* Cram Kanji 11-18 & NPBS Engine */
const CRAM_CP_KEY = 'marugoto_cram_11_18_cp_v1';
window.__MARUGOTO_NATIVE_DOM_DISABLED__ = true;
window.__MARUGOTO_CP_EXTRA_KEYS__ = [CRAM_CP_KEY];
window.__MARUGOTO_ON_RESET__ = function () {
    try { localStorage.removeItem(CRAM_CP_KEY); } catch (e) {}
    window.location.reload();
};

const rawVocab = window.CRAM_11_18_VOCAB || [];
let currentTab = 'tab-vocab';
let isRestoringCram = false;
let currentFilteredVocab = [...rawVocab];
let currentLessonFilter = 'ALL';
let isMeaningHidden = false;
let speedTestFinished = false;

// Cram Flashcard state
let cramIndex = 0;
let cramList = [...rawVocab];

function saveCramCheckpoint() {
    if (isRestoringCram) return;
    try {
        const searchEl = document.getElementById('vocabSearchInput');
        const cardEl = document.getElementById('mainFlashcard');
        const payload = {
            t: Date.now(),
            currentTab,
            currentLessonFilter,
            searchQuery: searchEl ? searchEl.value : '',
            isMeaningHidden,
            cramIndex,
            cramFlipped: cardEl ? cardEl.classList.contains('is-flipped') : false,
            cramOrder: cramList.map(c => `${c.lesson}|${c.kanji}|${c.kana}`),
            npbsUserAnswers,
            speedTestAnswers,
            speedTestFinished
        };
        localStorage.setItem(CRAM_CP_KEY, JSON.stringify(payload));
        if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
            window.MarugotoCheckpoint.notifySaved();
        }
    } catch (e) {}
}

// Navigation
function switchMainTab(tabId, opts) {
    currentTab = tabId;
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('onclick').includes(tabId));
    });
    document.querySelectorAll('.tab-panel').forEach(panel => {
        panel.classList.toggle('active', panel.id === tabId);
    });
    if (!(opts && opts.skipScroll)) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    if (!(opts && opts.skipSave)) {
        saveCramCheckpoint();
    }
}

// Render Vocab
function renderVocab(list) {
    const container = document.getElementById('vocabContainer');
    if (!container) return;
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 50px; color: var(--gray-400);">Không tìm thấy từ vựng nào phù hợp.</div>';
        return;
    }
    container.innerHTML = list.map(item => `
        <div class="vocab-card">
            <div>
                <div class="vc-header">
                    <div class="vc-kanji jp-text">${item.kanji}</div>
                    <button type="button" class="btn-card-action" onclick="audioEngine.speak('${item.kana}')" title="Phát âm">🔊</button>
                </div>
                <div class="vc-kana jp-text">${item.kana}</div>
                <div class="vc-vi ${isMeaningHidden ? 'style="filter: blur(5px); transition: filter 0.2s;" onclick="this.style.filter=\'none\'"' : ''}">${item.vi}</div>
            </div>
            <div class="vc-footer">
                <div style="display:flex; gap:6px;">
                    <span class="badge-lesson">Bài ${item.lesson}</span>
                    <span class="badge-group">${item.group || 'Từ vựng'}</span>
                </div>
                <div class="card-btns">
                    <button type="button" class="btn-card-action" onclick="copySingleItem('${item.kanji}')" title="Copy định dạng Quizlet">📋</button>
                </div>
            </div>
        </div>
    `).join('');
}

function filterVocabByLesson(lesson, btn) {
    currentLessonFilter = lesson;
    if (btn) {
        btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    applyFilter();
}

function handleSearch() {
    applyFilter();
}

function applyFilter() {
    const keyword = document.getElementById('vocabSearchInput').value.trim().toLowerCase();
    let filtered = rawVocab;
    if (currentLessonFilter !== 'ALL') {
        filtered = filtered.filter(v => v.lesson === parseInt(currentLessonFilter));
    }
    if (keyword) {
        filtered = filtered.filter(v => 
            v.kanji.toLowerCase().includes(keyword) ||
            v.kana.toLowerCase().includes(keyword) ||
            v.vi.toLowerCase().includes(keyword)
        );
    }
    currentFilteredVocab = filtered;
    document.getElementById('currentFilteredCount').innerText = filtered.length;
    renderVocab(filtered);
    saveCramCheckpoint();
}

function toggleHideMeaning() {
    isMeaningHidden = !isMeaningHidden;
    const btn = document.getElementById('btnHideMeaning');
    if (isMeaningHidden) {
        btn.innerText = '👁️ Hiện lại nghĩa';
        btn.style.background = '#e11d48';
    } else {
        btn.innerText = '👁️ Ẩn nghĩa (Tự dò)';
        btn.style.background = '';
    }
    renderVocab(currentFilteredVocab);
    saveCramCheckpoint();
}

// Copy Handlers
function formatQuizletLine(item, delimiter = '\t') {
    return `${item.kanji}${delimiter}[${item.kana}] ${item.vi}`;
}

function formatColonLine(item) {
    return `${item.kanji}、${item.vi}: ${item.kana}`;
}

function copyAllQuizletTab() {
    const text = rawVocab.map(v => formatQuizletLine(v, '\t')).join('\n');
    copyTextToClipboard(text, `toàn bộ ${rawVocab.length} từ dạng Quizlet Tab!`);
}

function copyAllColonFormat() {
    const text = rawVocab.map(v => formatColonLine(v)).join('\n');
    copyTextToClipboard(text, `toàn bộ ${rawVocab.length} từ dạng Dấu hai chấm (車、xe ô tô: くるま)!`);
}

function copyCurrentFilteredQuizlet() {
    if (!currentFilteredVocab.length) return showToast("Không có từ nào để copy!");
    const text = currentFilteredVocab.map(v => formatQuizletLine(v, '\t')).join('\n');
    copyTextToClipboard(text, `${currentFilteredVocab.length} từ chuẩn Quizlet Tab!`);
}

function copyCurrentFilteredColon() {
    if (!currentFilteredVocab.length) return showToast("Không có từ nào để copy!");
    const text = currentFilteredVocab.map(v => formatColonLine(v)).join('\n');
    copyTextToClipboard(text, `${currentFilteredVocab.length} từ dạng Dấu hai chấm!`);
}

function copySingleItem(kanji) {
    const item = rawVocab.find(v => v.kanji === kanji);
    if (!item) return;
    const line = formatQuizletLine(item, '\t');
    copyTextToClipboard(line, `từ ${item.kanji} chuẩn Quizlet!`);
}

function copyTextToClipboard(text, successMsg) {
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã sao chép ${successMsg}`);
    }).catch(() => {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast(`✅ Đã sao chép ${successMsg}`);
    });
}

function showToast(msg) {
    const t = document.getElementById('toast');
    t.innerText = msg;
    t.style.display = 'block';
    setTimeout(() => { t.style.display = 'none'; }, 2800);
}

// Cram Flashcard Logic
function updateCramCard() {
    if (cramList.length === 0) return;
    const item = cramList[cramIndex];
    const card = document.getElementById('mainFlashcard');
    card.classList.remove('is-flipped');

    document.getElementById('cramLessonBadge').innerText = `Bài ${item.lesson}`;
    document.getElementById('cramGroupBadge').innerText = item.group || 'Từ vựng';
    document.getElementById('cramProgressText').innerText = `${cramIndex + 1} / ${cramList.length}`;

    document.getElementById('cramFrontKanji').innerText = item.kanji;
    document.getElementById('cramBackKana').innerText = item.kana;
    document.getElementById('cramBackVi').innerText = item.vi;
}

function flipCurrentCard() {
    const card = document.getElementById('mainFlashcard');
    card.classList.toggle('is-flipped');
    if (card.classList.contains('is-flipped')) {
        speakCramWord();
    }
    saveCramCheckpoint();
}

function nextCramCard() {
    cramIndex = (cramIndex + 1) % cramList.length;
    updateCramCard();
    saveCramCheckpoint();
}

function prevCramCard() {
    cramIndex = (cramIndex - 1 + cramList.length) % cramList.length;
    updateCramCard();
    saveCramCheckpoint();
}

function speakCramWord() {
    const item = cramList[cramIndex];
    if (!item) return;
    if (window.AudioEngine && typeof window.AudioEngine.speak === 'function') {
        window.AudioEngine.speak(item.kana);
    } else if (typeof audioEngine !== 'undefined' && audioEngine && typeof audioEngine.speak === 'function') {
        audioEngine.speak(item.kana);
    } else if (typeof window.speakJapanese === 'function') {
        window.speakJapanese(item.kana);
    } else if ('speechSynthesis' in window) {
        const u = new SpeechSynthesisUtterance(item.kana);
        u.lang = 'ja-JP';
        window.speechSynthesis.speak(u);
    }
}

// Keyboard support for Flashcard
window.addEventListener('keydown', (e) => {
    if (document.getElementById('tab-cram').classList.contains('active')) {
        if (e.code === 'Space') {
            e.preventDefault();
            flipCurrentCard();
        } else if (e.code === 'ArrowRight') {
            nextCramCard();
        } else if (e.code === 'ArrowLeft') {
            prevCramCard();
        }
    }
});

// 10 Câu Thử Thách NPBS
const NPBS_CHALLENGES = [
    {
        id: 1,
        q: "この 会社に（　　）、10年に なります。",
        options: ["入ります", "入って", "入る", "入った"],
        correct: 1,
        explain: "Cấu trúc mốc thời gian: <strong>V-て + [Thời gian] + に なります</strong>. Động từ chia thể Te: <code>入って</code>."
    },
    {
        id: 2,
        q: "日本語の 勉強を はじめて 3か月（　　）なります。",
        options: ["で", "を", "に", "が"],
        correct: 2,
        explain: "Trợ từ đi với <code>なります</code> để chỉ mốc thời gian là <strong>に</strong>."
    },
    {
        id: 3,
        q: "「すみません。ペンを（　　）も いいですか。」――「はい、どうぞ。」",
        options: ["借りる", "借ります", "借りて", "借りた"],
        correct: 2,
        explain: "Mẫu câu xin phép: <strong>V-て + もいいですか</strong>. <code>借ります</code> chia thể Te là <code>借りて</code>."
    },
    {
        id: 4,
        q: "「先生、テストの とき、辞書を 使っても いいですか。」Khi từ chối không cho phép, Sensei sẽ nói gì?",
        options: ["はい、使ってください。", "いいえ、使ってはいけません。", "すみません、どうぞ。", "いいえ、使ってもいいです。"],
        correct: 1,
        explain: "Quy định cấm đoán nghiêm cẩn trong thi cử: <strong>V-てはいけません</strong> (Không được dùng)."
    },
    {
        id: 5,
        q: "日本に 来て 2年に なります。Câu này có nghĩa là gì?",
        options: ["Tôi sẽ ở Nhật thêm 2 năm nữa.", "Đã 2 năm kể từ khi tôi sang Nhật.", "Tôi muốn đến Nhật trong 2 năm.", "Tôi mới sang Nhật được 2 tuần."],
        correct: 1,
        explain: "Mẫu câu <code>Vて～年に なります</code> chỉ khoảng thời gian tính từ lúc bắt đầu sang Nhật đến nay."
    },
    {
        id: 6,
        q: "「エアコンを つけても いいですか。」――「（　　）」(Chọn câu trả lời đồng ý tự nhiên)",
        options: ["ええ、いいですよ。", "だめです。", "すみません、使います。", "いいえ、どうぞ。"],
        correct: 0,
        explain: "Đồng ý cho phép: <strong>「ええ、いいですよ。」</strong> hoặc <strong>「はい、どうぞ。」</strong>."
    },
    {
        id: 7,
        q: "結婚し（　　）5年に なります。(Đã kết hôn được 5 năm rồi)",
        options: ["て", "た", "る", "ます"],
        correct: 0,
        explain: "<code>結婚します</code> chia thể Te là <code>結婚して</code>."
    },
    {
        id: 8,
        q: "「ここで 写真を とっても いいですか。」―― Từ chối lịch sự văn phòng:",
        options: ["だめ！", "すみません、ここは 写真は ちょっと…", "はい、いいですよ。", "撮ってはいけません！(quát to)"],
        correct: 1,
        explain: "Từ chối khéo léo trong văn hóa Nhật dùng <code>すみません、～は ちょっと…</code>."
    },
    {
        id: 9,
        q: "「荷物を ここに 置いても いいですか。」―「ええ、（　　）いいですよ。」",
        options: ["置いて", "置いた", "置く", "置きます"],
        correct: 0,
        explain: "Mẫu cho phép: <strong>V-ても いいです</strong> ➔ <code>置いても いいですよ</code>."
    },
    {
        id: 10,
        q: "Điền trợ từ: この パソコン（　）、使っても いいですか。",
        options: ["を", "は", "に", "で"],
        correct: 0,
        explain: "Đồ vật chịu tác động của hành động <code>使います</code> đi với trợ từ <strong>を</strong> (hoặc đưa lên làm chủ đề với は: このパソコンは...)."
    }
];

let npbsUserAnswers = {};

function renderNpbsChallenge() {
    const container = document.getElementById('npbsChallengeList');
    if (!container) return;
    container.innerHTML = NPBS_CHALLENGES.map(q => `
        <div style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 12px; padding: 16px; margin-bottom: 14px;" id="npbsQ_${q.id}">
            <div style="font-size: 0.85rem; font-weight: 700; opacity: 0.85; margin-bottom: 6px;">CÂU ${q.id} / 10</div>
            <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 10px;" class="jp-text">${q.q}</div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 8px;">
                ${q.options.map((opt, idx) => `
                    <button type="button" onclick="answerNpbsChallenge(${q.id}, ${idx}, this)" style="background: #ffffff; color: #1e1b4b; border: none; padding: 10px 14px; border-radius: 8px; font-weight: 700; font-size: 0.92rem; cursor: pointer; text-align: left; transition: all 0.2s;">
                        ${['A', 'B', 'C', 'D'][idx]}. ${opt}
                    </button>
                `).join('')}
            </div>
            <div id="npbsFb_${q.id}" style="display: none; margin-top: 10px; padding: 10px 14px; border-radius: 8px; font-size: 0.92rem; font-weight: 600;"></div>
        </div>
    `).join('');
}

function answerNpbsChallenge(qId, selectedIdx, btn) {
    if (npbsUserAnswers[qId] !== undefined) return;
    npbsUserAnswers[qId] = selectedIdx;
    const q = NPBS_CHALLENGES.find(item => item.id === qId);
    const card = document.getElementById(`npbsQ_${qId}`);
    const buttons = card.querySelectorAll('button');
    const fb = document.getElementById(`npbsFb_${qId}`);

    buttons.forEach((b, idx) => {
        b.disabled = true;
        if (idx === q.correct) {
            b.style.background = '#10b981';
            b.style.color = '#ffffff';
        } else if (idx === selectedIdx) {
            b.style.background = '#ef4444';
            b.style.color = '#ffffff';
        } else {
            b.style.opacity = '0.5';
        }
    });

    fb.style.display = 'block';
    if (selectedIdx === q.correct) {
        fb.style.background = 'rgba(16, 185, 129, 0.3)';
        fb.style.border = '1px solid #34d399';
        fb.innerHTML = `✓ <strong>Chính xác!</strong> ${q.explain}`;
    } else {
        fb.style.background = 'rgba(239, 68, 68, 0.3)';
        fb.style.border = '1px solid #f87171';
        fb.innerHTML = `✕ <strong>Chưa đúng!</strong> ${q.explain}`;
    }
    saveCramCheckpoint();
}

// 20 CÂU SPEED TEST
const SPEED_TEST_QUESTIONS = [
    { q: "Chữ Hán: 料理 có cách đọc Hiragana là gì?", opts: ["りょうり", "りょうきん", "りゆう", "むりょう"], ans: 0, exp: "料理 (りょうり): món ăn." },
    { q: "Chữ Hán: 無料 có nghĩa là gì?", opts: ["Tài liệu", "Miễn phí", "Lý do", "Vô lý"], ans: 1, exp: "無料 (むりょう): miễn phí." },
    { q: "Chữ Hán: 出張 có cách đọc là gì?", opts: ["しゅっぱつ", "しゅっちょう", "とうちゃく", "かいしゃ"], ans: 1, exp: "出張 (しゅっちょう): đi công tác." },
    { q: "Chữ Hán: 喫茶店 có nghĩa là gì?", opts: ["Nhà hàng", "Quán giải khát, quán cà phê", "Công ty", "Sân bay"], ans: 1, exp: "喫茶店 (きっさてん): quán cà phê, giải khát." },
    { q: "Chữ Hán: 自転車 có cách đọc là gì?", opts: ["じどうしゃ", "じてんしゃ", "でんしゃ", "くるま"], ans: 1, exp: "自転車 (じてんしゃ): xe đạp." },
    { q: "Chữ Hán: 運転手 có nghĩa là gì?", opts: ["Ca sĩ", "Lái xe", "Người giỏi", "Người kém"], ans: 1, exp: "運転手 (うんてんしゅ): người lái xe." },
    { q: "Chữ Hán: 週末 có cách đọc là gì?", opts: ["まいつき", "まいあさ", "しゅうまつ", "まいしゅう"], ans: 2, exp: "週末 (しゅうまつ): cuối tuần." },
    { q: "Chữ Hán: 時計 có nghĩa là gì?", opts: ["Kế toán", "Đồng hồ", "Bức ảnh", "Bức tranh"], ans: 1, exp: "時計 (とけい): đồng hồ." },
    { q: "Chữ Hán: 去年 có cách đọc là gì?", opts: ["ことし", "らいねん", "きょねん", "せんしゅう"], ans: 2, exp: "去年 (きょねん): năm ngoái." },
    { q: "Chữ Hán: 家族 có nghĩa là gì?", opts: ["Tác giả", "Họa sĩ", "Gia đình", "Bạn bè"], ans: 2, exp: "家族 (かぞく): gia đình." },
    { q: "Chữ Hán: 作文 có cách đọc là gì?", opts: ["さっか", "さくぶん", "しょるい", "てがみ"], ans: 1, exp: "作文 (さくぶん): bài văn." },
    { q: "Chữ Hán: 荷物 có nghĩa là gì?", opts: ["Đồ uống", "Đồ ăn", "Hành lý, đồ đạc", "Phương tiện"], ans: 2, exp: "荷物 (にもつ): hành lý, đồ đạc." },
    { q: "Chữ Hán: 到着 có nghĩa là gì?", opts: ["Xuất phát", "Đến nơi", "Ra ngoài", "Vào công ty"], ans: 1, exp: "到着 (とうちゃく): đến nơi." },
    { q: "Chữ Hán: 空気 có cách đọc là gì?", opts: ["くうき", "くうこう", "みなと", "そら"], ans: 0, exp: "空気 (くうき): không khí." },
    { q: "Chữ Hán: 大使館 có nghĩa là gì?", opts: ["Thư viện", "Bảo tàng", "Đại sứ quán", "Bệnh viện"], ans: 2, exp: "大使館 (たいしかん): đại sứ quán." },
    { q: "NPBS 14: この会社に入って 10年（　）なります。", opts: ["を", "に", "で", "が"], ans: 1, exp: "Cấu trúc: Vて ～年に なります." },
    { q: "NPBS 14: ペンを（　）も いいですか。", opts: ["借りて", "借りる", "借ります", "借りた"], ans: 0, exp: "Mẫu câu xin phép: V-てもいいですか ➔ 借りても." },
    { q: "Chữ Hán: 真面目 có nghĩa là gì?", opts: ["Đẹp trai", "Nghiêm túc, chăm chỉ", "Vui tính", "Giản dị"], ans: 1, exp: "真面目 (まじめ): nghiêm túc, chăm chỉ." },
    { q: "Chữ Hán: 一年中 có cách đọc là gì?", opts: ["いちねんかん", "いちねんじゅう", "しごとちゅう", "まいとし"], ans: 1, exp: "一年中 (いちねんじゅう): cả một năm." },
    { q: "NPBS 14: Khi đồng ý cho người khác mượn đồ, ta đáp lịch sự là:", opts: ["だめです。", "はい、どうぞ。", "いいえ、いいですよ。", "すみません。"], ans: 1, exp: "はい、どうぞ (Xin mời)." }
];

let speedTestAnswers = {};

function renderSpeedTest() {
    const container = document.getElementById('speedTestContainer');
    if (!container) return;
    container.innerHTML = SPEED_TEST_QUESTIONS.map((q, idx) => `
        <div style="background: #ffffff; border: 1px solid var(--gray-200); border-radius: var(--radius-md); padding: 16px; margin-bottom: 14px;" id="stCard_${idx}">
            <div style="font-size: 0.85rem; font-weight: 800; color: var(--primary); margin-bottom: 6px;">CÂU ${idx + 1} / 20</div>
            <div style="font-size: 1.02rem; font-weight: 700; margin-bottom: 12px;" class="jp-text">${q.q}</div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 8px;">
                ${q.opts.map((opt, optIdx) => `
                    <button type="button" onclick="selectSpeedTestAnswer(${idx}, ${optIdx}, this)" style="background: #f8fafc; border: 1.5px solid var(--gray-200); padding: 10px 14px; border-radius: 8px; font-weight: 700; cursor: pointer; text-align: left; transition: all 0.2s;">
                        ${['A', 'B', 'C', 'D'][optIdx]}. ${opt}
                    </button>
                `).join('')}
            </div>
            <div id="stFb_${idx}" style="display: none; margin-top: 10px; padding: 10px 14px; border-radius: 8px; font-size: 0.9rem; font-weight: 600;"></div>
        </div>
    `).join('');
}

function selectSpeedTestAnswer(qIdx, optIdx, btn) {
    speedTestAnswers[qIdx] = optIdx;
    const card = document.getElementById(`stCard_${qIdx}`);
    card.querySelectorAll('button').forEach((b, idx) => {
        if (idx === optIdx) {
            b.style.background = '#e0e7ff';
            b.style.borderColor = '#4f46e5';
            b.style.color = '#3730a3';
        } else {
            b.style.background = '#f8fafc';
            b.style.borderColor = 'var(--gray-200)';
            b.style.color = 'var(--gray-800)';
        }
    });
    saveCramCheckpoint();
}

function finishSpeedTest(opts) {
    speedTestFinished = true;
    let score = 0;
    SPEED_TEST_QUESTIONS.forEach((q, idx) => {
        const chosen = speedTestAnswers[idx];
        const card = document.getElementById(`stCard_${idx}`);
        const fb = document.getElementById(`stFb_${idx}`);
        const buttons = card.querySelectorAll('button');

        buttons.forEach((b, bIdx) => {
            b.disabled = true;
            if (bIdx === q.ans) {
                b.style.background = '#10b981';
                b.style.color = '#ffffff';
                b.style.borderColor = '#10b981';
            } else if (bIdx === chosen) {
                b.style.background = '#ef4444';
                b.style.color = '#ffffff';
                b.style.borderColor = '#ef4444';
            }
        });

        fb.style.display = 'block';
        if (chosen === q.ans) {
            score += 5;
            fb.style.background = '#d1fae5';
            fb.style.color = '#065f46';
            fb.innerHTML = `✓ <strong>Đúng!</strong> ${q.exp}`;
        } else {
            fb.style.background = '#fee2e2';
            fb.style.color = '#991b1b';
            fb.innerHTML = `✕ <strong>Sai!</strong> ${q.exp}`;
        }
    });

    document.getElementById('speedTestScore').innerText = score;
    if (!(opts && opts.skipToast)) {
        showToast(`🎉 Bạn đạt ${score} / 100 điểm! Đêm nay đã nạp đầy đủ kiến thức!`);
    }
    if (!(opts && opts.skipScroll)) {
        window.scrollTo({ top: document.getElementById('tab-test').offsetTop, behavior: 'smooth' });
    }
    if (!(opts && opts.skipSave)) {
        saveCramCheckpoint();
    }
}

function restoreCramCheckpoint() {
    try {
        const raw = localStorage.getItem(CRAM_CP_KEY);
        if (!raw) return false;
        const saved = JSON.parse(raw);
        if (!saved || typeof saved !== 'object') return false;
        isRestoringCram = true;

        if (saved.currentLessonFilter !== undefined) {
            currentLessonFilter = saved.currentLessonFilter;
            document.querySelectorAll('button[onclick*="filterVocabByLesson"]').forEach(btn => {
                const oc = btn.getAttribute('onclick') || '';
                const isAll = currentLessonFilter === 'ALL' && oc.includes("'ALL'");
                const isNum = currentLessonFilter !== 'ALL' && new RegExp(`filterVocabByLesson\(['"]?${currentLessonFilter}['"]?`).test(oc);
                btn.classList.toggle('active', isAll || isNum);
            });
        }

        const searchEl = document.getElementById('vocabSearchInput');
        if (searchEl && typeof saved.searchQuery === 'string') {
            searchEl.value = saved.searchQuery;
        }

        if (typeof saved.isMeaningHidden === 'boolean') {
            isMeaningHidden = saved.isMeaningHidden;
            const hideBtn = document.getElementById('btnHideMeaning');
            if (hideBtn) {
                hideBtn.innerText = isMeaningHidden ? '👁️ Hiện lại nghĩa' : '👁️ Ẩn nghĩa (Tự dò)';
                hideBtn.style.background = isMeaningHidden ? '#e11d48' : '';
            }
        }

        if (Array.isArray(saved.cramOrder) && saved.cramOrder.length > 0) {
            const pool = [...rawVocab];
            const ordered = [];
            saved.cramOrder.forEach(k => {
                const idx = pool.findIndex(c => `${c.lesson}|${c.kanji}|${c.kana}` === k);
                if (idx !== -1) ordered.push(pool.splice(idx, 1)[0]);
            });
            cramList = ordered.concat(pool);
        }
        if (Number.isInteger(saved.cramIndex) && saved.cramIndex >= 0 && saved.cramIndex < cramList.length) {
            cramIndex = saved.cramIndex;
        }

        if (saved.npbsUserAnswers && typeof saved.npbsUserAnswers === 'object') {
            npbsUserAnswers = saved.npbsUserAnswers;
        }
        if (saved.speedTestAnswers && typeof saved.speedTestAnswers === 'object') {
            speedTestAnswers = saved.speedTestAnswers;
        }
        speedTestFinished = Boolean(saved.speedTestFinished);

        applyFilter();
        updateCramCard();
        if (saved.cramFlipped) {
            const card = document.getElementById('mainFlashcard');
            if (card) card.classList.add('is-flipped');
        }

        renderNpbsChallenge();
        Object.keys(npbsUserAnswers).forEach(qIdKey => {
            const qId = parseInt(qIdKey, 10);
            const selectedIdx = npbsUserAnswers[qIdKey];
            const q = NPBS_CHALLENGES.find(item => item.id === qId);
            const card = document.getElementById(`npbsQ_${qId}`);
            const fb = document.getElementById(`npbsFb_${qId}`);
            if (!q || !card || !fb) return;
            card.querySelectorAll('button').forEach((b, idx) => {
                b.disabled = true;
                if (idx === q.correct) {
                    b.style.background = '#10b981';
                    b.style.color = '#ffffff';
                } else if (idx === selectedIdx) {
                    b.style.background = '#ef4444';
                    b.style.color = '#ffffff';
                } else {
                    b.style.opacity = '0.5';
                }
            });
            fb.style.display = 'block';
            if (selectedIdx === q.correct) {
                fb.style.background = 'rgba(16, 185, 129, 0.3)';
                fb.style.border = '1px solid #34d399';
                fb.innerHTML = `✓ <strong>Chính xác!</strong> ${q.explain}`;
            } else {
                fb.style.background = 'rgba(239, 68, 68, 0.3)';
                fb.style.border = '1px solid #f87171';
                fb.innerHTML = `✕ <strong>Chưa đúng!</strong> ${q.explain}`;
            }
        });

        renderSpeedTest();
        if (speedTestFinished) {
            finishSpeedTest({ skipScroll: true, skipToast: true, skipSave: true });
        } else {
            Object.keys(speedTestAnswers).forEach(qIdxKey => {
                const qIdx = parseInt(qIdxKey, 10);
                const optIdx = speedTestAnswers[qIdxKey];
                const card = document.getElementById(`stCard_${qIdx}`);
                if (!card) return;
                card.querySelectorAll('button').forEach((b, idx) => {
                    if (idx === optIdx) {
                        b.style.background = '#e0e7ff';
                        b.style.borderColor = '#4f46e5';
                        b.style.color = '#3730a3';
                    }
                });
            });
        }

        if (saved.currentTab) {
            switchMainTab(saved.currentTab, { skipScroll: true, skipSave: true });
        }
        isRestoringCram = false;
        return true;
    } catch (e) {
        isRestoringCram = false;
        return false;
    }
}

// Init All
document.addEventListener('DOMContentLoaded', () => {
    const restored = restoreCramCheckpoint();
    if (!restored) {
        renderVocab(rawVocab);
        updateCramCard();
        renderNpbsChallenge();
        renderSpeedTest();
    }
});
