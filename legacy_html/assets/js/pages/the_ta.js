/* Extracted page script for the_ta.html */
// 70 Verbs Dataset with Groups, Thể TA, Meanings and pedagogical tips
const verbsData = [
    // Nhóm 1: i, chi, ri -> tta
    { id: 1, masu: "あいます", kanji: "会います", vi: "Gặp gỡ", group: "1", ta: "あった", note: "i ➔ った" },
    { id: 2, masu: "かいます", kanji: "買います", vi: "Mua sắm", group: "1", ta: "かった", note: "i ➔ った" },
    { id: 3, masu: "すいます", kanji: "吸います", vi: "Hút (thuốc)", group: "1", ta: "すった", note: "i ➔ った" },
    { id: 4, masu: "ならいます", kanji: "習います", vi: "Học (có người dạy)", group: "1", ta: "ならった", note: "i ➔ った" },
    { id: 5, masu: "うたいます", kanji: "歌います", vi: "Hát", group: "1", ta: "うたった", note: "i ➔ った" },
    { id: 6, masu: "つかいます", kanji: "使います", vi: "Sử dụng, dùng", group: "1", ta: "つかった", note: "i ➔ った" },
    { id: 7, masu: "まちます", kanji: "待ちます", vi: "Chờ đợi", group: "1", ta: "まった", note: "chi ➔ った" },
    { id: 8, masu: "たちます", kanji: "立ちます", vi: "Đứng lên", group: "1", ta: "たった", note: "chi ➔ った" },
    { id: 9, masu: "もちます", kanji: "持ちます", vi: "Cầm, mang theo", group: "1", ta: "もった", note: "chi ➔ った" },
    { id: 10, masu: "とります", kanji: "取ります/撮ります", vi: "Lấy / Chụp ảnh", group: "1", ta: "とった", note: "ri ➔ った" },
    { id: 11, masu: "のぼります", kanji: "登ります", vi: "Leo núi", group: "1", ta: "のぼった", note: "ri ➔ った" },
    { id: 12, masu: "つくります", kanji: "作ります", vi: "Làm, chế biến", group: "1", ta: "つくった", note: "ri ➔ った" },
    { id: 13, masu: "すわります", kanji: "座ります", vi: "Ngồi xuống", group: "1", ta: "すわった", note: "ri ➔ った" },
    { id: 14, masu: "まがります", kanji: "曲がります", vi: "Rẽ, quẹo", group: "1", ta: "まがった", note: "ri ➔ った" },
    { id: 15, masu: "とまります", kanji: "泊まります", vi: "Trọ lại khách sạn", group: "1", ta: "とまった", note: "ri ➔ った" },
    { id: 16, masu: "わたります", kanji: "渡ります", vi: "Băng qua cầu/đường", group: "1", ta: "わたった", note: "ri ➔ った" },

    // Nhóm 1 Bẫy Đuôi IRU/ERU
    { id: 17, masu: "かえります", kanji: "帰ります", vi: "Đi về", group: "1", ta: "かえった", note: "⚠️ Bẫy nhóm 1: ri ➔ った", isTrap: true },
    { id: 18, masu: "はいります", kanji: "入ります", vi: "Đi vào", group: "1", ta: "はいった", note: "⚠️ Bẫy nhóm 1: ri ➔ った", isTrap: true },
    { id: 19, masu: "はしります", kanji: "走ります", vi: "Chạy", group: "1", ta: "はしった", note: "⚠️ Bẫy nhóm 1: ri ➔ った", isTrap: true },
    { id: 20, masu: "しります", kanji: "知ります", vi: "Biết", group: "1", ta: "しった", note: "⚠️ Bẫy nhóm 1: ri ➔ った", isTrap: true },
    { id: 21, masu: "きります", kanji: "切ります", vi: "Cắt", group: "1", ta: "きった", note: "⚠️ Bẫy nhóm 1: ri ➔ った", isTrap: true },
    { id: 22, masu: "いります", kanji: "要ります", vi: "Cần thiết", group: "1", ta: "いった", note: "⚠️ Bẫy nhóm 1: ri ➔ った", isTrap: true },

    // Nhóm 1: mi, bi, ni -> nda
    { id: 23, masu: "のみます", kanji: "飲みます", vi: "Uống", group: "1", ta: "のんだ", note: "mi ➔ んだ" },
    { id: 24, masu: "よみます", kanji: "読みます", vi: "Đọc sách", group: "1", ta: "よんだ", note: "mi ➔ んだ" },
    { id: 25, masu: "やすみます", kanji: "休みます", vi: "Nghỉ ngơi", group: "1", ta: "やすんだ", note: "mi ➔ んだ" },
    { id: 26, masu: "すみます", kanji: "住みます", vi: "Sinh sống", group: "1", ta: "すんだ", note: "mi ➔ んだ" },
    { id: 27, masu: "あそびます", kanji: "遊びます", vi: "Vui chơi", group: "1", ta: "あそんだ", note: "bi ➔ んだ" },
    { id: 28, masu: "えらびます", kanji: "選びます", vi: "Chọn lựa", group: "1", ta: "えらんだ", note: "bi ➔ んだ" },
    { id: 29, masu: "しにます", kanji: "死にます", vi: "Chết", group: "1", ta: "しんだ", note: "ni ➔ んだ" },

    // Nhóm 1: ki -> ita, gi -> ida
    { id: 30, masu: "かきます", kanji: "書きます", vi: "Viết, vẽ", group: "1", ta: "かいた", note: "ki ➔ いた" },
    { id: 31, masu: "ききます", kanji: "聞きます", vi: "Nghe, hỏi", group: "1", ta: "きいた", note: "ki ➔ いた" },
    { id: 32, masu: "あるきます", kanji: "歩きます", vi: "Đi bộ", group: "1", ta: "あるいた", note: "ki ➔ いた" },
    { id: 33, masu: "はたらきます", kanji: "働きます", vi: "Làm việc", group: "1", ta: "はたらいた", note: "ki ➔ いた" },
    { id: 34, masu: "およぎます", kanji: "泳ぎます", vi: "Bơi lội", group: "1", ta: "およいだ", note: "gi ➔ いだ" },
    { id: 35, masu: "いそぎます", kanji: "急ぎます", vi: "Gấp gáp, vội", group: "1", ta: "いそいだ", note: "gi ➔ いだ" },
    { id: 36, masu: "ぬぎます", kanji: "脱ぎます", vi: "Cởi đồ", group: "1", ta: "ぬいだ", note: "gi ➔ いだ" },

    // Nhóm 1: shi -> shita
    { id: 37, masu: "はなします", kanji: "話します", vi: "Nói chuyện", group: "1", ta: "はなした", note: "shi ➔ した" },
    { id: 38, masu: "かします", kanji: "貸します", vi: "Cho mượn, cho vay", group: "1", ta: "かした", note: "shi ➔ した" },
    { id: 39, masu: "けします", kanji: "消します", vi: "Tắt đèn, xóa", group: "1", ta: "けした", note: "shi ➔ した" },
    { id: 40, masu: "なおします", kanji: "直します", vi: "Sửa chữa", group: "1", ta: "なおした", note: "shi ➔ した" },

    // Nhóm 1 Ngoại lệ Đi
    { id: 41, masu: "いきます", kanji: "行きます", vi: "Đi tới nơi nào", group: "1", ta: "いった", note: "🚨 Ngoại lệ: いった (không phải いいた)", isTrap: true },

    // Nhóm 2: bo masu them ta
    { id: 42, masu: "たべます", kanji: "食べます", vi: "Ăn", group: "2", ta: "たべた", note: "Bỏ ます + た" },
    { id: 43, masu: "みます", kanji: "見ます", vi: "Xem, ngắm", group: "2", ta: "みた", note: "1 âm tiết: Bỏ ます + た", isTrap: true },
    { id: 44, masu: "ねます", kanji: "寝ます", vi: "Đi ngủ", group: "2", ta: "ねた", note: "Bỏ ます + た" },
    { id: 45, masu: "おきます", kanji: "起きます", vi: "Thức dậy", group: "2", ta: "おきた", note: "⚠️ Đặc biệt nhóm 2", isTrap: true },
    { id: 46, masu: "かります", kanji: "借ります", vi: "Vay mượn", group: "2", ta: "かりた", note: "⚠️ Đặc biệt nhóm 2", isTrap: true },
    { id: 47, masu: "おります", kanji: "降ります", vi: "Xuống tàu/xe", group: "2", ta: "おりた", note: "⚠️ Đặc biệt nhóm 2", isTrap: true },
    { id: 48, masu: "あびます", kanji: "浴びます", vi: "Tắm vòi sen", group: "2", ta: "あびた", note: "⚠️ Đặc biệt nhóm 2", isTrap: true },
    { id: 49, masu: "シャツを きます", kanji: "着ます", vi: "Mặc áo sơ mi", group: "2", ta: "シャツを きた", note: "⚠️ Đặc biệt nhóm 2", altTa: "シャツを着た,シャツをきた", isTrap: true },
    { id: 50, masu: "できます", kanji: "出来ます", vi: "Có thể làm được", group: "2", ta: "できた", note: "⚠️ Đặc biệt nhóm 2", isTrap: true },
    { id: 51, masu: "おしえます", kanji: "教えます", vi: "Dạy học, chỉ dẫn", group: "2", ta: "おしえた", note: "Bỏ ます + た" },
    { id: 52, masu: "みせます", kanji: "見せます", vi: "Cho xem", group: "2", ta: "みせた", note: "Bỏ ます + た" },
    { id: 53, masu: "あけます", kanji: "開けます", vi: "Mở (cửa)", group: "2", ta: "あけた", note: "Bỏ ます + た" },
    { id: 54, masu: "しめます", kanji: "閉めます", vi: "Đóng (cửa)", group: "2", ta: "しめた", note: "Bỏ ます + た" },
    { id: 55, masu: "とめます", kanji: "止めます", vi: "Dừng xe", group: "2", ta: "とめた", note: "Bỏ ます + た" },
    { id: 56, masu: "すてます", kanji: "捨てます", vi: "Vứt rác", group: "2", ta: "すてた", note: "Bỏ ます + た" },
    { id: 57, masu: "あつめます", kanji: "集めます", vi: "Sưu tầm, thu gom", group: "2", ta: "あつめた", note: "Bỏ ます + た" },
    { id: 58, masu: "つかれます", kanji: "疲れます", vi: "Mệt mỏi", group: "2", ta: "つかれた", note: "Bỏ ます + た" },
    { id: 59, masu: "わすれます", kanji: "忘れます", vi: "Quên mất", group: "2", ta: "わすれた", note: "Bỏ ます + た" },
    { id: 60, masu: "おぼえます", kanji: "覚えます", vi: "Ghi nhớ", group: "2", ta: "おぼえた", note: "Bỏ ます + た" },

    // Nhóm 3: shimasu -> shita, kimasu -> kita
    { id: 61, masu: "します", kanji: "為ます", vi: "Làm hành động", group: "3", ta: "した", note: "suru ➔ した" },
    { id: 62, masu: "きます", kanji: "来ます", vi: "Đến nơi", group: "3", ta: "きた", note: "kuru ➔ きた (来ます➔来た)", isTrap: true },
    { id: 63, masu: "べんきょうします", kanji: "勉強します", vi: "Học tập", group: "3", ta: "べんきょうした", note: "N+します ➔ した" },
    { id: 64, masu: "しゅっぱつします", kanji: "出発します", vi: "Khởi hành", group: "3", ta: "しゅっぱつした", note: "N+します ➔ した" },
    { id: 65, masu: "とうちゃくします", kanji: "到着します", vi: "Đến nơi", group: "3", ta: "とうちゃくした", note: "N+します ➔ した" },
    { id: 66, masu: "しゅっちょうします", kanji: "出張します", vi: "Đi công tác", group: "3", ta: "しゅっちょうした", note: "N+します ➔ した" },
    { id: 67, masu: "さんぽします", kanji: "散歩します", vi: "Đi dạo", group: "3", ta: "さんぽした", note: "N+します ➔ した" },
    { id: 68, masu: "うんどうします", kanji: "運動します", vi: "Tập thể dục", group: "3", ta: "うんどうした", note: "N+します ➔ した" },
    { id: 69, masu: "もってきます", kanji: "持って来ます", vi: "Mang đến", group: "3", ta: "もってきた", note: "kuru ➔ きた" },
    { id: 70, masu: "つれてきます", kanji: "連れて来ます", vi: "Dẫn đến", group: "3", ta: "つれてきた", note: "kuru ➔ きた" }
];

let currentFilter = 'all';
let showAnswersState = false;
const userVerbAnswers = {}; // id -> { group: '', ta: '', isGroupCorrect: null, isTaCorrect: null }

function saveCurrentInputs() {
    verbsData.forEach(item => {
        const groupSelect = document.getElementById(`group-${item.id}`);
        const taInput = document.getElementById(`ta-${item.id}`);
        if (groupSelect && taInput) {
            if (!userVerbAnswers[item.id]) userVerbAnswers[item.id] = {};
            userVerbAnswers[item.id].group = groupSelect.value;
            userVerbAnswers[item.id].ta = taInput.value;
        }
    });
}

function switchTab(tabId) {
    document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));
    document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));

    const target = document.getElementById(tabId);
    if (target) target.classList.add('active');
    const activeBtn = Array.from(document.querySelectorAll('.nav-tab-btn')).find(b => b.getAttribute('onclick')?.includes(tabId));
    if (activeBtn) activeBtn.classList.add('active');
}

function setFilter(filterType, btn) {
    saveCurrentInputs();
    currentFilter = filterType;
    document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderTable();
}

function filterVerbs() {
    saveCurrentInputs();
    renderTable();
}

function renderTable() {
    saveCurrentInputs();
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = '';
    const searchVal = (document.getElementById('searchInput')?.value || '').trim().toLowerCase();

    const filtered = verbsData.filter(item => {
        // Group Filter
        if (currentFilter === '1' && item.group !== '1') return false;
        if (currentFilter === '2' && item.group !== '2') return false;
        if (currentFilter === '3' && item.group !== '3') return false;
        if (currentFilter === 'trap' && !item.isTrap) return false;

        // Search
        if (searchVal) {
            const text = `${item.masu} ${item.kanji} ${item.vi} ${item.ta} ${item.note}`.toLowerCase();
            if (!text.includes(searchVal)) return false;
        }
        return true;
    });

    filtered.forEach((item, index) => {
        const tr = document.createElement('tr');
        tr.id = `row-${item.id}`;
        const saved = userVerbAnswers[item.id] || { group: '', ta: '', isGroupCorrect: null, isTaCorrect: null };
        const groupClass = saved.isGroupCorrect === true ? 'is-correct' : (saved.isGroupCorrect === false ? 'is-incorrect' : '');
        const taClass = saved.isTaCorrect === true ? 'is-correct' : (saved.isTaCorrect === false ? 'is-incorrect' : '');
        const statusText = (saved.isGroupCorrect !== null && saved.isTaCorrect !== null)
            ? ((saved.isGroupCorrect && saved.isTaCorrect) ? '✅' : '❌')
            : '';

        tr.innerHTML = `
            <td><strong>${index + 1}</strong></td>
            <td>
                <span class="verb-masu">${item.masu}</span>
                <button type="button" class="fc-speaker-btn" style="margin-left:6px; vertical-align:middle; width:28px; height:28px; font-size:12px;" onclick="speakJapanese('${item.masu}', this)" title="Nghe phát âm">🔊</button>
                <span class="verb-vi">${item.kanji ? `${item.kanji} • ` : ''}${item.vi}</span>
            </td>
            <td>
                <select class="group-select ${groupClass}" id="group-${item.id}">
                    <option value="" ${!saved.group ? 'selected' : ''}>Nhóm</option>
                    <option value="1" ${saved.group === '1' ? 'selected' : ''}>Nhóm 1</option>
                    <option value="2" ${saved.group === '2' ? 'selected' : ''}>Nhóm 2</option>
                    <option value="3" ${saved.group === '3' ? 'selected' : ''}>Nhóm 3</option>
                </select>
            </td>
            <td>
                <input type="text" class="text-input ${taClass}" id="ta-${item.id}" value="${(saved.ta || '').replace(/"/g, '&quot;')}" placeholder="Chia thể TA...">
                <div class="answer-hint ${showAnswersState ? 'show' : ''}" id="hint-${item.id}">👉 Đáp án: <strong>${item.ta}</strong> <button type="button" class="fc-speaker-btn" style="margin-left:4px; vertical-align:middle; width:24px; height:24px; font-size:11px;" onclick="speakJapanese('${item.ta}', this)" title="Nghe thể TA">🔊</button> (N${item.group}) ${item.note ? `[${item.note}]` : ''}</div>
            </td>
            <td style="text-align: center;">
                <span id="status-${item.id}" class="status-icon">${statusText}</span>
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
    saveCurrentInputs();
    let correctCount = 0;
    let totalCount = verbsData.length;

    verbsData.forEach(item => {
        const saved = userVerbAnswers[item.id] || { group: '', ta: '' };
        const userGroup = saved.group;
        const userTa = normalizeStr(saved.ta);

        const isGroupCorrect = userGroup === item.group;

        const validTaAnswers = [normalizeStr(item.ta)];
        if (item.altTa) {
            item.altTa.split(',').forEach(alt => validTaAnswers.push(normalizeStr(alt)));
        }

        const userTaNoSpace = userTa.replace(/\s+/g, '');
        const isTaCorrect = validTaAnswers.some(ans => ans === userTa || ans.replace(/\s+/g, '') === userTaNoSpace);

        userVerbAnswers[item.id] = {
            group: userGroup,
            ta: saved.ta,
            isGroupCorrect: isGroupCorrect,
            isTaCorrect: isTaCorrect
        };

        const groupSelect = document.getElementById(`group-${item.id}`);
        const taInput = document.getElementById(`ta-${item.id}`);
        const statusIcon = document.getElementById(`status-${item.id}`);

        if (groupSelect) {
            if (isGroupCorrect) {
                groupSelect.classList.remove('is-incorrect');
                groupSelect.classList.add('is-correct');
            } else {
                groupSelect.classList.remove('is-correct');
                groupSelect.classList.add('is-incorrect');
            }
        }

        if (taInput) {
            if (isTaCorrect) {
                taInput.classList.remove('is-incorrect');
                taInput.classList.add('is-correct');
            } else {
                taInput.classList.remove('is-correct');
                taInput.classList.add('is-incorrect');
            }
        }

        if (isGroupCorrect && isTaCorrect) {
            correctCount++;
            if (statusIcon) statusIcon.innerHTML = '✅';
        } else {
            if (statusIcon) statusIcon.innerHTML = '❌';
        }
    });

    const banner = document.getElementById('scoreBanner');
    if (banner) {
        banner.style.display = 'block';
        const percentage = Math.round((correctCount / totalCount) * 100);
        banner.innerHTML = `🎉 Kết Quả: Bạn làm đúng ${correctCount} / ${totalCount} từ (${percentage}%). ${percentage >= 80 ? 'Xuất sắc! Bạn đã làm chủ hoàn toàn thể TA!' : 'Cố gắng lên, hãy xem lại quy tắc và luyện thêm nhé!'}`;
        banner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}

function toggleAnswers() {
    showAnswersState = !showAnswersState;
    verbsData.forEach(item => {
        const hint = document.getElementById(`hint-${item.id}`);
        if (hint) {
            if (showAnswersState) {
                hint.classList.add('show');
            } else {
                hint.classList.remove('show');
            }
        }
    });
}

function resetExercise() {
    Object.keys(userVerbAnswers).forEach(k => delete userVerbAnswers[k]);
    verbsData.forEach(item => {
        const groupSelect = document.getElementById(`group-${item.id}`);
        const taInput = document.getElementById(`ta-${item.id}`);
        const statusIcon = document.getElementById(`status-${item.id}`);
        const hint = document.getElementById(`hint-${item.id}`);

        if (groupSelect) {
            groupSelect.value = '';
            groupSelect.classList.remove('is-correct', 'is-incorrect');
        }
        if (taInput) {
            taInput.value = '';
            taInput.classList.remove('is-correct', 'is-incorrect');
        }
        if (statusIcon) statusIcon.innerHTML = '';
        if (hint) hint.classList.remove('show');
    });

    showAnswersState = false;
    const banner = document.getElementById('scoreBanner');
    if (banner) banner.style.display = 'none';
}

// Audio TTS Function handled globally via assets/js/audio-engine.js

// Interactive Verb Lab Transformer Logic
const IRREGULAR_VERBS = {
    'いく': { group: 1, masu: 'いきます', ru: 'いく', te: 'いって', ta: 'いった', nai: 'いかない', note: '🚨 Ngoại lệ nhóm 1: いく➔いった' },
    '行きます': { group: 1, masu: '行きます', ru: '行く', te: '行って', ta: '行った', nai: '行かない', note: '🚨 Ngoại lệ nhóm 1: 行く➔行った' },
    'いきます': { group: 1, masu: 'いきます', ru: 'いく', te: 'いって', ta: 'いった', nai: 'いかない', note: '🚨 Ngoại lệ nhóm 1: いきます➔いった' },
    '行く': { group: 1, masu: '行きます', ru: '行く', te: '行って', ta: '行った', nai: '行かない', note: '🚨 Ngoại lệ nhóm 1: 行く➔行った' },
    'する': { group: 3, masu: 'します', ru: 'する', te: 'して', ta: 'した', nai: 'しない', note: 'Nhóm 3 bất quy tắc (suru)' },
    'します': { group: 3, masu: 'します', ru: 'する', te: 'して', ta: 'した', nai: 'しない', note: 'Nhóm 3 bất quy tắc (suru)' },
    'くる': { group: 3, masu: 'きます', ru: 'くる', te: 'きて', ta: 'きた', nai: 'こない', note: 'Nhóm 3 bất quy tắc (kuru)' },
    'きます': { group: 3, masu: 'きます', ru: 'くる', te: 'きて', ta: 'きた', nai: 'こない', note: 'Nhóm 3 kuru (đến) hoặc 着る (mặc, nhóm 2)' },
    '来ます': { group: 3, masu: '来ます', ru: '来る', te: '来て', ta: '来た', nai: '来ない', note: 'Nhóm 3 来る' },
    '来る': { group: 3, masu: '来ます', ru: '来る', te: '来て', ta: '来た', nai: '来ない', note: 'Nhóm 3 来る' },
    'ある': { group: 1, masu: 'あります', ru: 'ある', te: 'あって', ta: 'あった', nai: 'ない', note: '🚨 Ngoại lệ: nai là ない' },
    'あります': { group: 1, masu: 'あります', ru: 'ある', te: 'あって', ta: 'あった', nai: 'ない', note: '🚨 Ngoại lệ: nai là ない' }
};

function runLabTransform() {
    const val = document.getElementById('labInput').value.trim();
    if (!val) return;

    let result = transformJapaneseVerb(val);
    if (result) {
        document.getElementById('labGroupTag').textContent = `Nhóm ${result.group}`;
        document.getElementById('labGroupTag').className = `group-tag tag-g${result.group}`;
        document.getElementById('labMasu').innerHTML = `${result.masu} <button type="button" class="fc-speaker-btn" onclick="speakJapanese('${result.masu}', this)">🔊</button>`;
        document.getElementById('labRu').innerHTML = `${result.ru} <button type="button" class="fc-speaker-btn" onclick="speakJapanese('${result.ru}', this)">🔊</button>`;
        document.getElementById('labTe').innerHTML = `${result.te} <button type="button" class="fc-speaker-btn" onclick="speakJapanese('${result.te}', this)">🔊</button>`;
        document.getElementById('labTa').innerHTML = `${result.ta} <button type="button" class="fc-speaker-btn" onclick="speakJapanese('${result.ta}', this)">🔊</button>`;
        document.getElementById('labNai').innerHTML = `${result.nai} <button type="button" class="fc-speaker-btn" onclick="speakJapanese('${result.nai}', this)">🔊</button>`;
        document.getElementById('labExplain').innerHTML = `💡 <strong>Quy tắc áp dụng:</strong> ${result.note}`;
    }
}

function setLabWord(word) {
    const inp = document.getElementById('labInput');
    inp.value = word;
    runLabTransform();
}

function speakLab(elemId) {
    const el = document.getElementById(elemId);
    if (el) {
        const txt = el.textContent.replace('🔊', '').trim();
        speakJapanese(txt);
    }
}

function transformJapaneseVerb(v) {
    if (!v) return null;
    v = v.trim();
    if (IRREGULAR_VERBS[v]) return IRREGULAR_VERBS[v];

    // Compound Kuru verbs (e.g. もってくる, つれてくる)
    if (v.endsWith('くる') || v.endsWith('きます') || v.endsWith('来る') || v.endsWith('来ます')) {
        const prefix = v.replace(/(くる|きます|来る|来ます)$/, '');
        return {
            group: 3,
            masu: prefix + 'きます',
            ru: prefix + 'くる',
            te: prefix + 'きて',
            ta: prefix + 'きた',
            nai: prefix + 'こない',
            note: 'Động từ ghép nhóm 3 (kuru)'
        };
    }

    // Specific Godan verbs ending in す / します (Nhóm 1)
    const godanSuStems = {
        'か': { ru: 'かす', masu: 'かします', te: 'かして', ta: 'かした', nai: 'かさない' },
        '貸': { ru: '貸す', masu: '貸します', te: '貸して', ta: '貸した', nai: '貸さない' },
        'はな': { ru: 'はなす', masu: 'はなします', te: 'はなして', ta: 'はなした', nai: 'はなさない' },
        '話': { ru: '話す', masu: '話します', te: '話して', ta: '話した', nai: '話さない' },
        'だ': { ru: 'だす', masu: 'だします', te: 'だして', ta: 'だした', nai: 'ださない' },
        '出': { ru: '出す', masu: '出します', te: '出して', ta: '出した', nai: '出さない' },
        'お': { ru: 'おす', masu: 'おします', te: 'おして', ta: 'おした', nai: 'おさない' },
        '押': { ru: '押す', masu: '押します', te: '押して', ta: '押した', nai: '押さない' },
        'け': { ru: 'けす', masu: 'けします', te: 'けして', ta: 'けした', nai: 'けさない' },
        '消': { ru: '消す', masu: '消します', te: '消して', ta: '消した', nai: '消さない' },
        'なお': { ru: 'なおす', masu: 'なおします', te: 'なおして', ta: 'なおした', nai: 'なおさない' },
        '直': { ru: '直す', masu: '直します', te: '直して', ta: '直した', nai: '直さない' },
        'わた': { ru: 'わたす', masu: 'わたします', te: 'わたして', ta: 'わたした', nai: 'わたさない' },
        '渡': { ru: '渡す', masu: '渡します', te: '渡して', ta: '渡した', nai: '渡さない' },
        'おと': { ru: 'おとす', masu: 'おとします', te: 'おとして', ta: 'おとした', nai: 'おとさない' },
        '落': { ru: '落とす', masu: '落とします', te: '落として', ta: '落とした', nai: '落とさない' },
        'さが': { ru: 'さがす', masu: 'さがします', te: 'さがして', ta: 'さがした', nai: 'さがさない' },
        '探': { ru: '探す', masu: '探します', te: '探して', ta: '探した', nai: '探さない' },
        'なく': { ru: 'なくす', masu: 'なくします', te: 'なくして', ta: 'なくした', nai: 'なくさない' },
        '無く': { ru: '無くす', masu: '無くします', te: '無くして', ta: '無くした', nai: '無くさない' },
        'おもいだ': { ru: 'おもいだす', masu: 'おもいだします', te: 'おもいだして', ta: 'おもいだした', nai: 'おもいださない' },
        '思い出し': { ru: '思い出す', masu: '思い出します', te: '思い出して', ta: '思い出したい', nai: '思い出さない' }
    };

    if (v.endsWith('します')) {
        const stem = v.slice(0, -3);
        if (godanSuStems[stem]) {
            const info = godanSuStems[stem];
            return {
                group: 1,
                masu: info.masu,
                ru: info.ru,
                te: info.te,
                ta: info.ta,
                nai: info.nai,
                note: 'Động từ nhóm 1 đuôi す: Bỏ ます (し) thêm <strong>した</strong>'
            };
        }
        // Suru compound (Nhóm 3)
        return {
            group: 3,
            masu: stem + 'します',
            ru: stem + 'する',
            te: stem + 'して',
            ta: stem + 'した',
            nai: stem + 'しない',
            note: 'Danh động từ nhóm 3 (N + します)'
        };
    }

    if (v.endsWith('する')) {
        const prefix = v.slice(0, -2);
        return {
            group: 3,
            masu: prefix + 'します',
            ru: prefix + 'する',
            te: prefix + 'して',
            ta: prefix + 'した',
            nai: prefix + 'しない',
            note: 'Danh động từ nhóm 3 (N + する)'
        };
    }

    // Special Group 2 verbs (Ichidan ending in -iru / -eru)
    const g2Special = [
        'おきる', 'おきます', 'みる', 'みます', 'ねる', 'ねます',
        'かりる', 'かります', 'おりる', 'おります', 'あびる', 'あびます',
        'できる', 'できます', 'たべる', 'たべます', 'おしえる', 'おしえます',
        'わすれる', 'わすれます', 'みせる', 'みせます', 'あける', 'あけます',
        'しめる', 'しめます', 'とめる', 'とめます', 'すてる', 'すてます',
        'あつめる', 'あつめます', 'つかれる', 'つかれます', 'おぼえる', 'おぼえます'
    ];
    for (let s of g2Special) {
        if (v === s || v.endsWith(s)) {
            let stem = v.replace(/ます$/, '').replace(/る$/, '');
            return {
                group: 2,
                masu: stem + 'ます',
                ru: stem + 'る',
                te: stem + 'て',
                ta: stem + 'た',
                nai: stem + 'ない',
                note: 'Động từ nhóm 2: Bỏ ます / る thêm た'
            };
        }
    }

    // Masu form input
    if (v.endsWith('ます')) {
        const base = v.slice(0, -2);
        const last = base.slice(-1);
        const root = base.slice(0, -1);

        // Group 1
        if (['い', 'ち', 'り'].includes(last)) {
            const uMap = { 'い': 'う', 'ち': 'つ', 'り': 'る' };
            const aMap = { 'い': 'わ', 'ち': 'た', 'り': 'ら' };
            return {
                group: 1,
                masu: v,
                ru: root + uMap[last],
                te: root + 'って',
                ta: root + 'った',
                nai: root + aMap[last] + 'ない',
                note: `Âm ${last} trước ます đổi thành <strong>った</strong> (âm ngắt)`
            };
        }
        if (['み', 'び', 'に'].includes(last)) {
            const uMap = { 'み': 'む', 'び': 'ぶ', 'に': 'ぬ' };
            const aMap = { 'み': 'ま', 'び': 'ば', 'に': 'な' };
            return {
                group: 1,
                masu: v,
                ru: root + uMap[last],
                te: root + 'んで',
                ta: root + 'んだ',
                nai: root + aMap[last] + 'ない',
                note: `Âm ${last} trước ます đổi thành <strong>んだ</strong> (âm mũi + đục)`
            };
        }
        if (last === 'き') {
            return {
                group: 1,
                masu: v,
                ru: root + 'く',
                te: root + 'いて',
                ta: root + 'いた',
                nai: root + 'かない',
                note: 'Âm き trước ます đổi thành <strong>いた</strong>'
            };
        }
        if (last === 'ぎ') {
            return {
                group: 1,
                masu: v,
                ru: root + 'ぐ',
                te: root + 'いで',
                ta: root + 'いだ',
                nai: root + 'がない',
                note: 'Âm ぎ trước ます đổi thành <strong>いだ</strong>'
            };
        }
        if (last === 'し') {
            return {
                group: 1,
                masu: v,
                ru: root + 'す',
                te: root + 'して',
                ta: root + 'した',
                nai: root + 'さない',
                note: 'Âm し trước ます đổi thành <strong>した</strong>'
            };
        }
        // default group 2
        return {
            group: 2,
            masu: v,
            ru: base + 'る',
            te: base + 'て',
            ta: base + 'た',
            nai: base + 'ない',
            note: 'Động từ nhóm 2: Bỏ ます thêm <strong>た</strong>'
        };
    }

    // Dictionary form (Jisho-kei) inputs
    if (v.endsWith('う')) {
        const root = v.slice(0, -1);
        return {
            group: 1,
            masu: root + 'います',
            ru: v,
            te: root + 'って',
            ta: root + 'った',
            nai: root + 'わない',
            note: 'Động từ nhóm 1 đuôi う đổi thành <strong>った</strong> (âm ngắt)'
        };
    }
    if (v.endsWith('つ')) {
        const root = v.slice(0, -1);
        return {
            group: 1,
            masu: root + 'ちます',
            ru: v,
            te: root + 'って',
            ta: root + 'った',
            nai: root + 'たない',
            note: 'Động từ nhóm 1 đuôi つ đổi thành <strong>った</strong> (âm ngắt)'
        };
    }
    if (v.endsWith('す')) {
        const root = v.slice(0, -1);
        return {
            group: 1,
            masu: root + 'します',
            ru: v,
            te: root + 'して',
            ta: root + 'した',
            nai: root + 'さない',
            note: 'Động từ nhóm 1 đuôi す đổi thành <strong>した</strong>'
        };
    }
    if (v.endsWith('く')) {
        const root = v.slice(0, -1);
        return {
            group: 1,
            masu: root + 'きます',
            ru: v,
            te: root + 'いて',
            ta: root + 'いた',
            nai: root + 'かない',
            note: 'Động từ nhóm 1 đuôi く đổi thành <strong>いた</strong>'
        };
    }
    if (v.endsWith('ぐ')) {
        const root = v.slice(0, -1);
        return {
            group: 1,
            masu: root + 'ぎます',
            ru: v,
            te: root + 'いで',
            ta: root + 'いだ',
            nai: root + 'がない',
            note: 'Động từ nhóm 1 đuôi ぐ đổi thành <strong>いだ</strong>'
        };
    }
    if (v.endsWith('む') || v.endsWith('ぶ') || v.endsWith('ぬ')) {
        const root = v.slice(0, -1);
        const lastChar = v.slice(-1);
        const iMap = { 'む': 'み', 'ぶ': 'び', 'ぬ': 'に' };
        const aMap = { 'む': 'ま', 'ぶ': 'ば', 'ぬ': 'な' };
        return {
            group: 1,
            masu: root + iMap[lastChar] + 'ます',
            ru: v,
            te: root + 'んで',
            ta: root + 'んだ',
            nai: root + aMap[lastChar] + 'ない',
            note: 'Động từ nhóm 1 đuôi む/ぶ/ぬ đổi thành <strong>んだ</strong>'
        };
    }
    if (v.endsWith('る')) {
        const g1RuTraps = ['かえる', 'はいる', 'はしる', 'しる', 'きる', 'いる', 'へる', 'しゃべる', 'すべる'];
        const isG1Trap = g1RuTraps.includes(v);
        const prevChar = v.slice(-2, -1);
        const aouKana = ['あ','か','さ','た','な','は','ま','や','ら','わ','お','こ','そ','と','の','ほ','モ','よ','ろ','う','く','す','つ','ぬ','ふ','む','ゆ','る'];
        const isClearlyG1 = aouKana.includes(prevChar);

        if (isG1Trap || isClearlyG1) {
            const root = v.slice(0, -1);
            return {
                group: 1,
                masu: root + 'ります',
                ru: v,
                te: root + 'って',
                ta: root + 'った',
                nai: root + 'らない',
                note: isG1Trap ? '⚠️ Ngoại lệ nhóm 1: đuôi る đổi thành <strong>った</strong>' : 'Động từ nhóm 1 đuôi る đổi thành <strong>った</strong>'
            };
        } else {
            const root = v.slice(0, -1);
            return {
                group: 2,
                masu: root + 'ます',
                ru: v,
                te: root + 'て',
                ta: root + 'た',
                nai: root + 'ない',
                note: 'Động từ nhóm 2: Bỏ る thêm <strong>た</strong>'
            };
        }
    }

    return {
        group: 1,
        masu: v + 'ます',
        ru: v,
        te: v + 'て',
        ta: v + 'た',
        nai: v + 'ない',
        note: 'Phân tích cơ bản'
    };
}

// Init
window.addEventListener('DOMContentLoaded', () => {
    renderTable();
    runLabTransform();
});
