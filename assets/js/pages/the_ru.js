/* Extracted page script for the_ru.html */
// Full 56 verbs dataset
const verbsData = [
    { id: 1, masu: "さんぽします", group: "3", ru: "さんぽする", note: "" },
    { id: 2, masu: "かえります", group: "1", ru: "かえる", note: "Nhóm 1" },
    { id: 3, masu: "まがります", group: "1", ru: "まがる", note: "" },
    { id: 4, masu: "まちます", group: "1", ru: "まつ", note: "chi ➔ tsu" },
    { id: 5, masu: "およぎます", group: "1", ru: "およぐ", note: "gi ➔ gu" },
    { id: 6, masu: "かります", group: "2", ru: "かりる", note: "Đặc biệt nhóm 2" },
    { id: 7, masu: "ねます", group: "2", ru: "ねる", note: "" },
    { id: 8, masu: "あいます", group: "1", ru: "あう", note: "i ➔ u" },
    { id: 9, masu: "はなします", group: "1", ru: "はなす", note: "shi ➔ su" },
    { id: 10, masu: "たべます", group: "2", ru: "たべる", note: "" },
    { id: 11, masu: "します", group: "3", ru: "する", note: "" },
    { id: 12, masu: "たべます", group: "2", ru: "たべる", note: "" },
    { id: 13, masu: "うんどうします", group: "3", ru: "うんどうする", note: "" },
    { id: 14, masu: "もってきます", group: "3", ru: "もってくる", note: "" },
    { id: 15, masu: "でます", group: "2", ru: "でる", note: "" },
    { id: 16, masu: "とります", group: "1", ru: "とる", note: "" },
    { id: 17, masu: "やすみます", group: "1", ru: "やすむ", note: "mi ➔ mu" },
    { id: 18, masu: "シャツを きます", group: "2", ru: "シャツを きる", note: "き(mặc): Nhóm 2", altRu: "シャツを着る,シャツをきる" },
    { id: 19, masu: "かします", group: "1", ru: "かす", note: "" },
    { id: 20, masu: "ききます", group: "1", ru: "きく", note: "ki ➔ ku" },
    { id: 21, masu: "ねます", group: "2", ru: "ねる", note: "" },
    { id: 22, masu: "けします", group: "1", ru: "けす", note: "" },
    { id: 23, masu: "いきます", group: "1", ru: "いく", note: "ki ➔ ku" },
    { id: 24, masu: "あそびます", group: "1", ru: "あそぶ", note: "bi ➔ bu" },
    { id: 25, masu: "すてます", group: "2", ru: "すてる", note: "" },
    { id: 26, masu: "はいります", group: "1", ru: "はいる", note: "Nhóm 1" },
    { id: 27, masu: "はしります", group: "1", ru: "はしる", note: "Nhóm 1" },
    { id: 28, masu: "みせます", group: "2", ru: "みせる", note: "" },
    { id: 29, masu: "かいます", group: "1", ru: "かう", note: "" },
    { id: 30, masu: "のぼります", group: "1", ru: "のぼる", note: "" },
    { id: 31, masu: "わたります", group: "1", ru: "わたる", note: "" },
    { id: 32, masu: "７時に おきます", group: "2", ru: "７時に おきる", note: "Đặc biệt nhóm 2", altRu: "7じに おきる,7時におきる,７時におきる,7じにおきる" },
    { id: 33, masu: "いります", group: "1", ru: "いる", note: "iru (cần): Nhóm 1" },
    { id: 34, masu: "とまります", group: "1", ru: "とまる", note: "" },
    { id: 35, masu: "みます", group: "2", ru: "みる", note: "" },
    { id: 36, masu: "すわります", group: "1", ru: "すわる", note: "" },
    { id: 37, masu: "あるきます", group: "1", ru: "あるく", note: "" },
    { id: 38, masu: "いそぎます", group: "1", ru: "いそぐ", note: "" },
    { id: 39, masu: "みます", group: "2", ru: "みる", note: "" },
    { id: 40, masu: "かばんを おきます", group: "1", ru: "かばんを おく", note: "おく (đặt): Nhóm 1", altRu: "かばんをおく" },
    { id: 41, masu: "たちます", group: "1", ru: "たつ", note: "chi ➔ tsu" },
    { id: 42, masu: "あんないします", group: "3", ru: "あんないする", note: "" },
    { id: 43, masu: "のみます", group: "1", ru: "のむ", note: "" },
    { id: 44, masu: "とめます", group: "2", ru: "とめる", note: "" },
    { id: 45, masu: "しにます", group: "1", ru: "しぬ", note: "ni ➔ nu" },
    { id: 46, masu: "よみます", group: "1", ru: "よむ", note: "" },
    { id: 47, masu: "はたらきます", group: "1", ru: "はたらく", note: "" },
    { id: 48, masu: "おしえます", group: "2", ru: "おしえる", note: "" },
    { id: 49, masu: "かえります", group: "1", ru: "かえる", note: "" },
    { id: 50, masu: "べんきょうします", group: "3", ru: "べんきょうする", note: "" },
    { id: 51, masu: "あつめます", group: "2", ru: "あつめる", note: "" },
    { id: 52, masu: "しります", group: "1", ru: "しる", note: "Nhóm 1" },
    { id: 53, masu: "つれてきます", group: "3", ru: "つれてくる", note: "" },
    { id: 54, masu: "きります", group: "1", ru: "きる", note: "kiru (cắt): Nhóm 1" },
    { id: 55, masu: "つかれます", group: "2", ru: "つかれる", note: "" },
    { id: 56, masu: "学校に きます", group: "3", ru: "学校に くる", note: "kuru: Nhóm 3", altRu: "がっこうに くる,学校にくる,がっこうにくる" }
];

let showAnswersState = false;

function switchTab(tabId) {
    document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));
    document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));

    const target = document.getElementById(tabId);
    if (target) target.classList.add('active');
    const activeBtn = Array.from(document.querySelectorAll('.nav-tab-btn')).find(b => b.getAttribute('onclick')?.includes(tabId));
    if (activeBtn) activeBtn.classList.add('active');
}

function renderTable() {
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = '';

    verbsData.forEach((item, index) => {
        const tr = document.createElement('tr');
        tr.id = `row-${item.id}`;
        tr.innerHTML = `
            <td><strong>${index + 1}</strong></td>
            <td>
                <span class="verb-masu">${item.masu}</span>
                <button type="button" class="fc-speaker-btn" style="margin-left:6px; vertical-align:middle; width:28px; height:28px; font-size:13px;" onclick="speakJapanese('${item.masu}', this)" title="Nghe phát âm">🔊</button>
            </td>
            <td>
                <select class="group-select" id="group-${item.id}">
                    <option value="">Nhóm</option>
                    <option value="1">Nhóm 1</option>
                    <option value="2">Nhóm 2</option>
                    <option value="3">Nhóm 3</option>
                </select>
            </td>
            <td>
                <input type="text" class="text-input" id="ru-${item.id}" placeholder="Chia thể RU...">
                <div class="answer-hint" id="hint-${item.id}">👉 Đáp án: <strong>${item.ru}</strong> <button type="button" class="fc-speaker-btn" style="margin-left:4px; vertical-align:middle; width:24px; height:24px; font-size:11px;" onclick="speakJapanese('${item.ru}', this)" title="Nghe thể RU">🔊</button> (N${item.group}) ${item.note ? `[${item.note}]` : ''}</div>
            </td>
            <td style="text-align: center;">
                <span id="status-${item.id}" class="status-icon"></span>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function normalizeStr(str) {
    if (!str) return '';
    return str.trim().toLowerCase().replace(/\s+/g, ' ');
}

function gradeAll() {
    let correctCount = 0;
    let totalCount = verbsData.length;

    verbsData.forEach(item => {
        const groupSelect = document.getElementById(`group-${item.id}`);
        const ruInput = document.getElementById(`ru-${item.id}`);
        const statusIcon = document.getElementById(`status-${item.id}`);

        const userGroup = groupSelect.value;
        const userRu = normalizeStr(ruInput.value);

        const isGroupCorrect = userGroup === item.group;

        const validRuAnswers = [normalizeStr(item.ru)];
        if (item.altRu) {
            item.altRu.split(',').forEach(alt => validRuAnswers.push(normalizeStr(alt)));
        }

        const userRuNoSpace = userRu.replace(/\s+/g, '');
        const isRuCorrect = validRuAnswers.some(ans => ans === userRu || ans.replace(/\s+/g, '') === userRuNoSpace);

        if (isGroupCorrect) {
            groupSelect.classList.remove('is-incorrect');
            groupSelect.classList.add('is-correct');
        } else {
            groupSelect.classList.remove('is-correct');
            groupSelect.classList.add('is-incorrect');
        }

        if (isRuCorrect) {
            ruInput.classList.remove('is-incorrect');
            ruInput.classList.add('is-correct');
        } else {
            ruInput.classList.remove('is-correct');
            ruInput.classList.add('is-incorrect');
        }

        if (isGroupCorrect && isRuCorrect) {
            correctCount++;
            statusIcon.innerHTML = '✅';
        } else {
            statusIcon.innerHTML = '❌';
        }
    });

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

function toggleAnswers() {
    showAnswersState = !showAnswersState;
    verbsData.forEach(item => {
        const hint = document.getElementById(`hint-${item.id}`);
        hint.style.display = showAnswersState ? 'block' : 'none';
    });
}

function resetExercise() {
    if (confirm("Bạn có muốn xóa bài làm để thực hành lại từ đầu không?")) {
        verbsData.forEach(item => {
            const groupSelect = document.getElementById(`group-${item.id}`);
            const ruInput = document.getElementById(`ru-${item.id}`);
            const statusIcon = document.getElementById(`status-${item.id}`);
            const hint = document.getElementById(`hint-${item.id}`);

            groupSelect.value = '';
            groupSelect.className = 'group-select';
            ruInput.value = '';
            ruInput.className = 'text-input';
            statusIcon.innerHTML = '';
            hint.style.display = 'none';
        });
        showAnswersState = false;
        document.getElementById('scoreBanner').style.display = 'none';
    }
}

function filterVerbs() {
    const query = normalizeStr(document.getElementById('searchInput').value);
    verbsData.forEach(item => {
        const row = document.getElementById(`row-${item.id}`);
        const textToMatch = normalizeStr(item.masu + ' ' + item.ru);
        if (textToMatch.includes(query)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

window.addEventListener('DOMContentLoaded', () => {
    renderTable();
});
