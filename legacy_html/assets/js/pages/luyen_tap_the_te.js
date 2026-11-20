/* Extracted page script for tests/Luyen_Tap_The_Te_A2_1.html */
// 56 Verbs data from the classroom assignment
const verbsData = [
    { id: 1, masu: "さんぽします", group: "3", te: "さんぽして", note: "" },
    { id: 2, masu: "かえります", group: "1", te: "かえって", note: "" },
    { id: 3, masu: "まがります", group: "1", te: "まがって", note: "" },
    { id: 4, masu: "まちます", group: "1", te: "まって", note: "" },
    { id: 5, masu: "およぎます", group: "1", te: "およいで", note: "" },
    { id: 6, masu: "かります", group: "2", te: "かりて", note: "Đặc biệt nhóm 2" },
    { id: 7, masu: "ねます", group: "2", te: "ねて", note: "" },
    { id: 8, masu: "あいます", group: "1", te: "あって", note: "" },
    { id: 9, masu: "はなします", group: "1", te: "はなして", note: "" },
    { id: 10, masu: "たべます", group: "2", te: "たべて", note: "" },
    { id: 11, masu: "します", group: "3", te: "して", note: "" },
    { id: 12, masu: "たべます", group: "2", te: "たべて", note: "" },
    { id: 13, masu: "うんどうします", group: "3", te: "うんどうして", note: "" },
    { id: 14, masu: "もってきます", group: "3", te: "もってきて", note: "" },
    { id: 15, masu: "でます", group: "2", te: "でて", note: "" },
    { id: 16, masu: "とります", group: "1", te: "とって", note: "" },
    { id: 17, masu: "やすみます", group: "1", te: "やすんで", note: "" },
    { id: 18, masu: "シャツを きます", group: "2", te: "シャツを きて", note: "き(mặc): Nhóm 2" },
    { id: 19, masu: "かします", group: "1", te: "かして", note: "" },
    { id: 20, masu: "ききます", group: "1", te: "きいて", note: "" },
    { id: 21, masu: "ねます", group: "2", te: "ねて", note: "" },
    { id: 22, masu: "けします", group: "1", te: "けして", note: "" },
    { id: 23, masu: "いきます", group: "1", te: "いって", note: "Ngoại lệ" },
    { id: 24, masu: "あそびます", group: "1", te: "あそんで", note: "" },
    { id: 25, masu: "すてます", group: "2", te: "すてて", note: "" },
    { id: 26, masu: "はいります", group: "1", te: "はいって", note: "" },
    { id: 27, masu: "はしります", group: "1", te: "はしって", note: "" },
    { id: 28, masu: "みせます", group: "2", te: "みせて", note: "" },
    { id: 29, masu: "かいます", group: "1", te: "かって", note: "" },
    { id: 30, masu: "のぼります", group: "1", te: "のぼって", note: "" },
    { id: 31, masu: "わたります", group: "1", te: "わたって", note: "" },
    { id: 32, masu: "７時に おきます", group: "2", te: "７時に おきて", note: "おきる: Nhóm 2 đặc biệt", altTe: "7じに おきて,7時に おきて,７時におきて,7時におきて" },
    { id: 33, masu: "いります", group: "1", te: "いって", note: "iru (cần): Nhóm 1" },
    { id: 34, masu: "とまります", group: "1", te: "とまって", note: "" },
    { id: 35, masu: "みます", group: "2", te: "みて", note: "" },
    { id: 36, masu: "すわります", group: "1", te: "すわって", note: "" },
    { id: 37, masu: "あるきます", group: "1", te: "あるいて", note: "" },
    { id: 38, masu: "いそぎます", group: "1", te: "いそいで", note: "" },
    { id: 39, masu: "みます", group: "2", te: "みて", note: "" },
    { id: 40, masu: "かばんを おきます", group: "1", te: "かばんを おいて", note: "おく (đặt): Nhóm 1", altTe: "かばんをおいて" },
    { id: 41, masu: "たちます", group: "1", te: "たって", note: "" },
    { id: 42, masu: "あんないします", group: "3", te: "あんないして", note: "" },
    { id: 43, masu: "のみます", group: "1", te: "のんで", note: "" },
    { id: 44, masu: "とめます", group: "2", te: "とめて", note: "" },
    { id: 45, masu: "しにます", group: "1", te: "しんで", note: "" },
    { id: 46, masu: "よみます", group: "1", te: "よんで", note: "" },
    { id: 47, masu: "はたらきます", group: "1", te: "はたらいて", note: "" },
    { id: 48, masu: "おしえます", group: "2", te: "おしえて", note: "" },
    { id: 49, masu: "かえります", group: "1", te: "かえって", note: "" },
    { id: 50, masu: "べんきょうします", group: "3", te: "べんきょうして", note: "" },
    { id: 51, masu: "あつめます", group: "2", te: "あつめて", note: "" },
    { id: 52, masu: "しります", group: "1", te: "しって", note: "" },
    { id: 53, masu: "つれてきます", group: "3", te: "つれてきて", note: "" },
    { id: 54, masu: "きります", group: "1", te: "きって", note: "kiru (cắt): Nhóm 1" },
    { id: 55, masu: "つかれます", group: "2", te: "つかれて", note: "" },
    { id: 56, masu: "学校に きます", group: "3", te: "学校に きて", note: "kuru: Nhóm 3", altTe: "がっこうに きて,学校にきて,がっこうにきて" }
];

let showAnswersState = false;

// Switch Tabs
function switchTab(tabId) {
    document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));
    document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));

    const target = document.getElementById(tabId);
    if (target) target.classList.add('active');
    const activeBtn = Array.from(document.querySelectorAll('.nav-tab-btn')).find(b => b.getAttribute('onclick')?.includes(tabId));
    if (activeBtn) activeBtn.classList.add('active');
}

// Helper: generate negative forms
function getNegativeTargets(item) {
    // Form 1: ～ていません (e.g. たべていません)
    const negTe = item.te + "いません";
    const negTeSpace = item.te + " いません";

    // Form 2: ～ません (e.g. たべません)
    const negMasu = item.masu.replace(/ます$/, 'ません');

    return { negTe, negTeSpace, negMasu };
}

// Render Table
function renderTable() {
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = '';

    verbsData.forEach((item, index) => {
        const tr = document.createElement('tr');
        tr.id = `row-${item.id}`;
        const negs = getNegativeTargets(item);

        tr.innerHTML = `
            <td><strong>${index + 1}</strong></td>
            <td>
                <span class="verb-masu">${item.masu}</span>
                <button type="button" class="fc-speaker-btn" style="margin-left:6px; vertical-align:middle; width:28px; height:28px; font-size:13px;" onclick="speakJapanese('${item.masu}', this)" title="Nghe phát âm">🔊</button>
            </td>
            <td>
                <select class="group-select" id="group-${item.id}">
                    <option value="">Chọn nhóm</option>
                    <option value="1">Nhóm 1</option>
                    <option value="2">Nhóm 2</option>
                    <option value="3">Nhóm 3</option>
                </select>
            </td>
            <td>
                <input type="text" class="text-input" id="te-${item.id}" placeholder="Ví dụ: ${item.te.slice(-2)}...">
                <div class="answer-hint" id="hint-te-${item.id}">👉 ～て: <strong>${item.te}</strong> <button type="button" class="fc-speaker-btn" style="margin-left:4px; vertical-align:middle; width:22px; height:22px; font-size:11px;" onclick="speakJapanese('${item.te}', this)" title="Nghe thể TE">🔊</button> (N${item.group}) ${item.note ? `[${item.note}]` : ''}</div>
            </td>
            <td>
                <input type="text" class="text-input" id="neg-${item.id}" placeholder="Điền ～ていません hoặc ～ません...">
                <div class="answer-hint" id="hint-neg-${item.id}">👉 Phủ định: <strong>${negs.negTe}</strong> <button type="button" class="fc-speaker-btn" style="margin-left:4px; vertical-align:middle; width:22px; height:22px; font-size:11px;" onclick="speakJapanese('${negs.negTe}', this)" title="Nghe phủ định">🔊</button> / <strong>${negs.negMasu}</strong></div>
            </td>
            <td style="text-align: center;">
                <span id="status-${item.id}" class="status-icon"></span>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// Standardize string comparison
function normalizeStr(str) {
    if (!str) return '';
    return str.trim().toLowerCase().replace(/\s+/g, ' ');
}

// Grade All Answers
function gradeAll() {
    let correctCount = 0;
    let totalCount = verbsData.length;

    verbsData.forEach(item => {
        const groupSelect = document.getElementById(`group-${item.id}`);
        const teInput = document.getElementById(`te-${item.id}`);
        const negInput = document.getElementById(`neg-${item.id}`);
        const statusIcon = document.getElementById(`status-${item.id}`);

        const userGroup = groupSelect.value;
        const userTe = normalizeStr(teInput.value);
        const userNeg = normalizeStr(negInput.value);

        // Group validation
        const isGroupCorrect = userGroup === item.group;

        // Te validation (allow alternate spellings and no space)
        const validTeAnswers = [normalizeStr(item.te)];
        if (item.altTe) {
            item.altTe.split(',').forEach(alt => validTeAnswers.push(normalizeStr(alt)));
        }
        const userTeNoSpace = userTe.replace(/\s+/g, '');
        const isTeCorrect = validTeAnswers.some(ans => ans === userTe || ans.replace(/\s+/g, '') === userTeNoSpace);

        // Negative validation (accept both ～ていません AND ～ません)
        const negs = getNegativeTargets(item);
        const validNegAnswers = [
            normalizeStr(negs.negTe),
            normalizeStr(negs.negTeSpace),
            normalizeStr(negs.negMasu)
        ];
        const userNegNoSpace = userNeg.replace(/\s+/g, '');
        const isNegCorrect = validNegAnswers.some(ans => ans === userNeg || ans.replace(/\s+/g, '') === userNegNoSpace);

        // Group styling
        if (isGroupCorrect) {
            groupSelect.classList.remove('is-incorrect');
            groupSelect.classList.add('is-correct');
        } else {
            groupSelect.classList.remove('is-correct');
            groupSelect.classList.add('is-incorrect');
        }

        // Te styling
        if (isTeCorrect) {
            teInput.classList.remove('is-incorrect');
            teInput.classList.add('is-correct');
        } else {
            teInput.classList.remove('is-correct');
            teInput.classList.add('is-incorrect');
        }

        // Negative styling
        if (isNegCorrect) {
            negInput.classList.remove('is-incorrect');
            negInput.classList.add('is-correct');
        } else {
            negInput.classList.remove('is-correct');
            negInput.classList.add('is-incorrect');
        }

        // Overall row check
        if (isGroupCorrect && isTeCorrect && isNegCorrect) {
            correctCount++;
            statusIcon.innerHTML = '✅';
        } else {
            statusIcon.innerHTML = '❌';
        }
    });

    // Show Score Banner
    const banner = document.getElementById('scoreBanner');
    banner.style.display = 'block';
    const percent = Math.round((correctCount / totalCount) * 100);
    banner.innerHTML = `🎉 Bạn làm đúng hoàn toàn: ${correctCount}/${totalCount} câu (${percent}%)`;

    if (percent >= 80) {
        banner.style.background = 'linear-gradient(135deg, #00b894 0%, #00cec9 100%)';
    } else if (percent >= 50) {
        banner.style.background = 'linear-gradient(135deg, #f39c12 0%, #e67e22 100%)';
    } else {
        banner.style.background = 'linear-gradient(135deg, #e74c3c 0%, #c0392b 100%)';
    }

    banner.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Toggle Answers
function toggleAnswers() {
    showAnswersState = !showAnswersState;
    verbsData.forEach(item => {
        const hintTe = document.getElementById(`hint-te-${item.id}`);
        const hintNeg = document.getElementById(`hint-neg-${item.id}`);
        hintTe.style.display = showAnswersState ? 'block' : 'none';
        hintNeg.style.display = showAnswersState ? 'block' : 'none';
    });
}

// Reset Table
function resetExercise() {
    if (confirm("Bạn có chắc chắn muốn xóa hết bài làm để làm lại từ đầu?")) {
        verbsData.forEach(item => {
            const groupSelect = document.getElementById(`group-${item.id}`);
            const teInput = document.getElementById(`te-${item.id}`);
            const negInput = document.getElementById(`neg-${item.id}`);
            const statusIcon = document.getElementById(`status-${item.id}`);
            const hintTe = document.getElementById(`hint-te-${item.id}`);
            const hintNeg = document.getElementById(`hint-neg-${item.id}`);

            groupSelect.value = '';
            groupSelect.className = 'group-select';
            teInput.value = '';
            teInput.className = 'text-input';
            negInput.value = '';
            negInput.className = 'text-input';
            statusIcon.innerHTML = '';
            hintTe.style.display = 'none';
            hintNeg.style.display = 'none';
        });
        showAnswersState = false;
        document.getElementById('scoreBanner').style.display = 'none';
    }
}

// Search filter
function filterVerbs() {
    const query = normalizeStr(document.getElementById('searchInput').value);
    verbsData.forEach(item => {
        const row = document.getElementById(`row-${item.id}`);
        const textToMatch = normalizeStr(item.masu + ' ' + item.te);
        if (textToMatch.includes(query)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Initialize
window.addEventListener('DOMContentLoaded', () => {
    renderTable();
});
