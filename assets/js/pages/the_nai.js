/* Extracted page script for the_nai.html */
const verbsData = [{ "id": 1, "masu": "あいます", "kanji": "会います", "vi": "Gặp gỡ", "group": "1", "nai": "あわない", "note": "⚠️ Bẫy i ➔ わ: あわない", "isTrap": true }, { "id": 2, "masu": "かいます", "kanji": "買います", "vi": "Mua sắm", "group": "1", "nai": "かわない", "note": "⚠️ Bẫy i ➔ わ: かわない", "isTrap": true }, { "id": 3, "masu": "すいます", "kanji": "吸います", "vi": "Hút (thuốc)", "group": "1", "nai": "すわない", "note": "⚠️ Bẫy i ➔ わ: すわない", "isTrap": true }, { "id": 4, "masu": "ならいます", "kanji": "習います", "vi": "Học tập", "group": "1", "nai": "ならわない", "note": "⚠️ Bẫy i ➔ わ: ならわない", "isTrap": true }, { "id": 5, "masu": "うたいます", "kanji": "歌います", "vi": "Hát", "group": "1", "nai": "うたわない", "note": "⚠️ Bẫy i ➔ わ: うたわない", "isTrap": true }, { "id": 6, "masu": "つかいます", "kanji": "使います", "vi": "Sử dụng, dùng", "group": "1", "nai": "つかわない", "note": "⚠️ Bẫy i ➔ わ: つかわない", "isTrap": true }, { "id": 7, "masu": "おもいます", "kanji": "思います", "vi": "Suy nghĩ", "group": "1", "nai": "おもわない", "note": "⚠️ Bẫy i ➔ わ: おもわない", "isTrap": true }, { "id": 8, "masu": "てつだいます", "kanji": "手伝います", "vi": "Giúp đỡ", "group": "1", "nai": "てつだわない", "note": "⚠️ Bẫy i ➔ わ: てつだわない", "isTrap": true }, { "id": 9, "masu": "まちます", "kanji": "待ちます", "vi": "Chờ đợi", "group": "1", "nai": "またない", "note": "chi ➔ た: またない" }, { "id": 10, "masu": "たちます", "kanji": "立ちます", "vi": "Đứng lên", "group": "1", "nai": "たたない", "note": "chi ➔ た: たたない" }, { "id": 11, "masu": "もちます", "kanji": "持ちます", "vi": "Cầm, mang", "group": "1", "nai": "もたない", "note": "chi ➔ た: もたない" }, { "id": 12, "masu": "とります", "kanji": "取ります/撮ります", "vi": "Lấy / Chụp ảnh", "group": "1", "nai": "とらない", "note": "ri ➔ ら: とらない" }, { "id": 13, "masu": "つくります", "kanji": "作ります", "vi": "Làm, chế biến", "group": "1", "nai": "つくらない", "note": "ri ➔ ら: つくらない" }, { "id": 14, "masu": "すわります", "kanji": "座ります", "vi": "Ngồi xuống", "group": "1", "nai": "すわらない", "note": "ri ➔ ら: すわらない" }, { "id": 15, "masu": "のぼります", "kanji": "登ります", "vi": "Leo núi", "group": "1", "nai": "のぼらない", "note": "ri ➔ ら: のぼらない" }, { "id": 16, "masu": "とまります", "kanji": "泊まります", "vi": "Trọ lại", "group": "1", "nai": "とまらない", "note": "ri ➔ ら: とまらない" }, { "id": 17, "masu": "まがります", "kanji": "曲がります", "vi": "Rẽ, quẹo", "group": "1", "nai": "まがらない", "note": "ri ➔ ら: まがらない" }, { "id": 18, "masu": "わたります", "kanji": "渡ります", "vi": "Băng qua", "group": "1", "nai": "わたらない", "note": "ri ➔ ら: わたらない" }, { "id": 19, "masu": "わかります", "kanji": "分かります", "vi": "Hiểu, rõ", "group": "1", "nai": "わからない", "note": "ri ➔ ら: わからない" }, { "id": 20, "masu": "おわります", "kanji": "終わります", "vi": "Kết thúc", "group": "1", "nai": "おわらない", "note": "ri ➔ ら: おわらない" }, { "id": 21, "masu": "かえります", "kanji": "帰ります", "vi": "Đi về", "group": "1", "nai": "かえらない", "note": "⚠️ Bẫy nhóm 1: ri ➔ ら (かえらない)", "isTrap": true }, { "id": 22, "masu": "はいります", "kanji": "入ります", "vi": "Đi vào", "group": "1", "nai": "はいらない", "note": "⚠️ Bẫy nhóm 1: ri ➔ ら (はいらない)", "isTrap": true }, { "id": 23, "masu": "はしります", "kanji": "走ります", "vi": "Chạy", "group": "1", "nai": "はしらない", "note": "⚠️ Bẫy nhóm 1: ri ➔ ら (はしらない)", "isTrap": true }, { "id": 24, "masu": "しります", "kanji": "知ります", "vi": "Biết", "group": "1", "nai": "しらない", "note": "⚠️ Bẫy nhóm 1: ri ➔ ら (しらない)", "isTrap": true }, { "id": 25, "masu": "きります", "kanji": "切ります", "vi": "Cắt", "group": "1", "nai": "きらない", "note": "⚠️ Bẫy nhóm 1: ri ➔ ら (きらない)", "isTrap": true }, { "id": 26, "masu": "いります", "kanji": "要ります", "vi": "Cần thiết", "group": "1", "nai": "いらない", "note": "⚠️ Bẫy nhóm 1: ri ➔ ら (いらない)", "isTrap": true }, { "id": 27, "masu": "のみます", "kanji": "飲みます", "vi": "Uống", "group": "1", "nai": "のまない", "note": "mi ➔ ま: のまない" }, { "id": 28, "masu": "よみます", "kanji": "読みます", "vi": "Đọc sách", "group": "1", "nai": "よまない", "note": "mi ➔ ま: よまない" }, { "id": 29, "masu": "やすみます", "kanji": "休みます", "vi": "Nghỉ ngơi", "group": "1", "nai": "やすまない", "note": "mi ➔ ま: やすまない" }, { "id": 30, "masu": "すみます", "kanji": "住みます", "vi": "Sinh sống", "group": "1", "nai": "すまない", "note": "mi ➔ ま: すまない" }, { "id": 31, "masu": "たのみます", "kanji": "頼みます", "vi": "Nhờ vả", "group": "1", "nai": "たのまない", "note": "mi ➔ ま: たのまない" }, { "id": 32, "masu": "あそびます", "kanji": "遊びます", "vi": "Vui chơi", "group": "1", "nai": "あそばない", "note": "bi ➔ ば: あそばない" }, { "id": 33, "masu": "えらびます", "kanji": "選びます", "vi": "Chọn lựa", "group": "1", "nai": "えらばない", "note": "bi ➔ ば: えらばない" }, { "id": 34, "masu": "よびます", "kanji": "呼びます", "vi": "Gọi, kêu", "group": "1", "nai": "よばない", "note": "bi ➔ ば: よばない" }, { "id": 35, "masu": "しにます", "kanji": "死にます", "vi": "Chết", "group": "1", "nai": "しなない", "note": "ni ➔ な: しなない" }, { "id": 36, "masu": "かきます", "kanji": "書きます", "vi": "Viết, vẽ", "group": "1", "nai": "かかない", "note": "ki ➔ か: かかない" }, { "id": 37, "masu": "ききます", "kanji": "聞きます", "vi": "Nghe, hỏi", "group": "1", "nai": "きかない", "note": "ki ➔ か: きかない" }, { "id": 38, "masu": "あるきます", "kanji": "歩きます", "vi": "Đi bộ", "group": "1", "nai": "あるかない", "note": "ki ➔ か: あるかない" }, { "id": 39, "masu": "はたらきます", "kanji": "働きます", "vi": "Làm việc", "group": "1", "nai": "はたらかない", "note": "ki ➔ か: はたらかない" }, { "id": 40, "masu": "いきます", "kanji": "行きます", "vi": "Đi tới nơi nào", "group": "1", "nai": "いかない", "note": "ki ➔ か: いかない (⚠️ Quy tắc: không phải いった)", "isTrap": true }, { "id": 41, "masu": "およぎます", "kanji": "泳ぎます", "vi": "Bơi lội", "group": "1", "nai": "およがない", "note": "gi ➔ が: およがない" }, { "id": 42, "masu": "いそぎます", "kanji": "急ぎます", "vi": "Gấp gáp, vội", "group": "1", "nai": "いそがない", "note": "gi ➔ が: いそがない" }, { "id": 43, "masu": "ぬぎます", "kanji": "脱ぎます", "vi": "Cởi đồ", "group": "1", "nai": "ぬがない", "note": "gi ➔ が: ぬがない" }, { "id": 44, "masu": "はなします", "kanji": "話します", "vi": "Nói chuyện", "group": "1", "nai": "はなさない", "note": "shi ➔ さ: はなさない" }, { "id": 45, "masu": "かします", "kanji": "貸します", "vi": "Cho mượn", "group": "1", "nai": "かさない", "note": "shi ➔ さ: かさない" }, { "id": 46, "masu": "けします", "kanji": "消します", "vi": "Tắt đèn, xóa", "group": "1", "nai": "けさない", "note": "shi ➔ さ: けさない" }, { "id": 47, "masu": "なおします", "kanji": "直します", "vi": "Sửa chữa", "group": "1", "nai": "なおさない", "note": "shi ➔ さ: なおさない" }, { "id": 48, "masu": "だします", "kanji": "出します", "vi": "Gửi, đưa ra, nộp", "group": "1", "nai": "ださない", "note": "shi ➔ さ: ださない" }, { "id": 49, "masu": "あります", "kanji": "有ります", "vi": "Có (đồ vật)", "group": "1", "nai": "ない", "note": "🚨 Bẫy số 1: あります ➔ ない (không có あらない)", "isTrap": true }, { "id": 50, "masu": "たべます", "kanji": "食べます", "vi": "Ăn", "group": "2", "nai": "たべない", "note": "Bỏ ます + ない" }, { "id": 51, "masu": "みます", "kanji": "見ます", "vi": "Xem, ngắm", "group": "2", "nai": "みない", "note": "1 âm tiết: Bỏ ます + ない", "isTrap": true }, { "id": 52, "masu": "ねます", "kanji": "寝ます", "vi": "Đi ngủ", "group": "2", "nai": "ねない", "note": "Bỏ ます + ない" }, { "id": 53, "masu": "おきます", "kanji": "起きます", "vi": "Thức dậy", "group": "2", "nai": "おきない", "note": "⚠️ Đặc biệt nhóm 2 (âm i)", "isTrap": true }, { "id": 54, "masu": "かります", "kanji": "借ります", "vi": "Vay mượn", "group": "2", "nai": "かりない", "note": "⚠️ Đặc biệt nhóm 2 (âm i)", "isTrap": true }, { "id": 55, "masu": "おります", "kanji": "降ります", "vi": "Xuống tàu/xe", "group": "2", "nai": "おりない", "note": "⚠️ Đặc biệt nhóm 2 (âm i)", "isTrap": true }, { "id": 56, "masu": "あびます", "kanji": "浴びます", "vi": "Tắm vòi sen", "group": "2", "nai": "あびない", "note": "⚠️ Đặc biệt nhóm 2 (âm i)", "isTrap": true }, { "id": 57, "masu": "きます", "kanji": "着ます", "vi": "Mặc (áo sơ mi)", "group": "2", "nai": "きない", "note": "⚠️ Đặc biệt nhóm 2: 1 âm tiết (きない)", "isTrap": true }, { "id": 58, "masu": "できます", "kanji": "出来ます", "vi": "Có thể làm được", "group": "2", "nai": "できない", "note": "⚠️ Đặc biệt nhóm 2", "isTrap": true }, { "id": 59, "masu": "おしえます", "kanji": "教えます", "vi": "Dạy học, chỉ dẫn", "group": "2", "nai": "おしえない", "note": "Bỏ ます + ない" }, { "id": 60, "masu": "みせます", "kanji": "見せます", "vi": "Cho xem", "group": "2", "nai": "みせない", "note": "Bỏ ます + ない" }, { "id": 61, "masu": "あけます", "kanji": "開けます", "vi": "Mở (cửa)", "group": "2", "nai": "あけない", "note": "Bỏ ます + ない" }, { "id": 62, "masu": "しめます", "kanji": "閉めます", "vi": "Đóng (cửa)", "group": "2", "nai": "しめない", "note": "Bỏ ます + ない" }, { "id": 63, "masu": "とめます", "kanji": "止めます", "vi": "Dừng xe", "group": "2", "nai": "とめない", "note": "Bỏ ます + ない" }, { "id": 64, "masu": "すてます", "kanji": "捨てます", "vi": "Vứt rác", "group": "2", "nai": "すてない", "note": "Bỏ ます + ない" }, { "id": 65, "masu": "あつめます", "kanji": "集めます", "vi": "Sưu tầm", "group": "2", "nai": "あつめない", "note": "Bỏ ます + ない" }, { "id": 66, "masu": "つかれます", "kanji": "疲れます", "vi": "Mệt mỏi", "group": "2", "nai": "つかれない", "note": "Bỏ ます + ない" }, { "id": 67, "masu": "わすれます", "kanji": "忘れます", "vi": "Quên mất", "group": "2", "nai": "わすれない", "note": "Bỏ ます + ない" }, { "id": 68, "masu": "おぼえます", "kanji": "覚えます", "vi": "Ghi nhớ", "group": "2", "nai": "おぼえない", "note": "Bỏ ます + ない" }, { "id": 69, "masu": "します", "kanji": "為ます", "vi": "Làm hành động", "group": "3", "nai": "しない", "note": "suru ➔ しない" }, { "id": 70, "masu": "きます", "kanji": "来ます", "vi": "Đến nơi", "group": "3", "nai": "こない", "note": "🚨 Bẫy số 2: kuru ➔ こない (来ない)", "isTrap": true }, { "id": 71, "masu": "べんきょうします", "kanji": "勉強します", "vi": "Học tập", "group": "3", "nai": "べんきょうしない", "note": "N+します ➔ しない" }, { "id": 72, "masu": "しゅっぱつします", "kanji": "出発します", "vi": "Khởi hành", "group": "3", "nai": "しゅっぱつしない", "note": "N+します ➔ しない" }, { "id": 73, "masu": "しゅっちょうします", "kanji": "出張します", "vi": "Đi công tác", "group": "3", "nai": "しゅっちょうしない", "note": "N+します ➔ しない" }, { "id": 74, "masu": "さんぽします", "kanji": "散歩します", "vi": "Đi dạo", "group": "3", "nai": "さんぽしない", "note": "N+します ➔ しない" }, { "id": 75, "masu": "うんどうします", "kanji": "運動します", "vi": "Tập thể dục", "group": "3", "nai": "うんどうしない", "note": "N+します ➔ しない" }, { "id": 76, "masu": "もってきます", "kanji": "持って来ます", "vi": "Mang đến", "group": "3", "nai": "もってこない", "note": "kuru ➔ こない", "isTrap": true }, { "id": 77, "masu": "つれてきます", "kanji": "連れて来ます", "vi": "Dẫn đến", "group": "3", "nai": "つれてこない", "note": "kuru ➔ こない", "isTrap": true }];
let currentFilter = 'all';
let showAnswersState = false;

function switchTab(tabId) {
    document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));
    document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));

    const target = document.getElementById(tabId);
    if (target) target.classList.add('active');
    const activeBtn = Array.from(document.querySelectorAll('.nav-tab-btn')).find(b => b.getAttribute('onclick')?.includes(tabId));
    if (activeBtn) activeBtn.classList.add('active');
}

function setFilter(filterType, btn) {
    currentFilter = filterType;
    document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderTable();
}

function filterVerbs() {
    renderTable();
}

function renderTable() {
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = '';
    const searchVal = (document.getElementById('searchInput')?.value || '').trim().toLowerCase();

    const filtered = verbsData.filter(item => {
        if (currentFilter === '1' && item.group !== '1') return false;
        if (currentFilter === '2' && item.group !== '2') return false;
        if (currentFilter === '3' && item.group !== '3') return false;
        if (currentFilter === 'trap' && !item.isTrap) return false;

        if (searchVal) {
            const text = `${item.masu} ${item.kanji} ${item.vi} ${item.nai} ${item.note}`.toLowerCase();
            if (!text.includes(searchVal)) return false;
        }
        return true;
    });

    filtered.forEach((item, index) => {
        const tr = document.createElement('tr');

        // Group badge
        let groupBadge = '';
        if (item.group === '1') groupBadge = '<span class="group-tag tag-g1">Nhóm ①</span>';
        else if (item.group === '2') groupBadge = '<span class="group-tag tag-g2">Nhóm ②</span>';
        else groupBadge = '<span class="group-tag tag-g3">Nhóm ③</span>';

        if (item.isTrap) {
            groupBadge += ' <span class="group-tag tag-trap">Bẫy</span>';
        }

        tr.innerHTML = `
        <td style="text-align: center; color: var(--gray); font-weight: bold;">${index + 1}</td>
        <td>
            <div style="font-weight: 800; font-size: 1.05rem;" class="jp-text">${item.kanji}</div>
            <div style="color: var(--primary); font-size: 0.9rem;" class="jp-text">${item.masu}</div>
            <div style="color: var(--gray); font-size: 0.85rem;">${item.vi}</div>
        </td>
        <td>${groupBadge}</td>
        <td>
            <div style="display: flex; gap: 8px; align-items: center;">
                <input type="text" class="input-nai" id="input_${item.id}" placeholder="Nhập thể Nai..." oninput="checkVerbInput(${item.id})" autocomplete="off">
                <button type="button" class="sound-btn" onclick="speakJapanese('${item.nai}', this)" title="Nghe phát âm thể Nai">🔊</button>
            </div>
            <div id="hint_${item.id}" style="font-size: 0.82rem; color: #047857; margin-top: 4px; display: none;">
                💡 ${item.note} ➔ <strong class="jp-text">${item.nai}</strong>
            </div>
        </td>
        <td style="text-align: center;">
            <span class="status-badge status-pending" id="status_${item.id}">Chưa nhập</span>
        </td>
    `;
        tbody.appendChild(tr);

        if (showAnswersState) {
            const input = document.getElementById(`input_${item.id}`);
            input.value = item.nai;
            checkVerbInput(item.id);
        }
    });
}

function cleanKana(str) {
    return (str || '').trim().toLowerCase().replace(/[\s　]+/g, '');
}

function checkVerbInput(id) {
    const item = verbsData.find(v => v.id === id);
    if (!item) return;
    const input = document.getElementById(`input_${id}`);
    const status = document.getElementById(`status_${id}`);
    const hint = document.getElementById(`hint_${id}`);
    const val = cleanKana(input.value);

    if (!val) {
        input.className = 'input-nai';
        status.className = 'status-badge status-pending';
        status.innerText = 'Chưa nhập';
        hint.style.display = 'none';
        return;
    }

    const expected = cleanKana(item.nai);
    if (val === expected) {
        input.className = 'input-nai correct';
        status.className = 'status-badge status-ok';
        status.innerText = '✓ Chính xác';
        hint.style.display = 'block';
    } else {
        input.className = 'input-nai wrong';
        status.className = 'status-badge status-err';
        status.innerText = '✕ Chưa đúng';
        hint.style.display = 'block';
    }
}
function gradeAllInputs() {
    let correct = 0;
    let total = 0;

    verbsData.forEach(item => {
        const input = document.getElementById(`input_${item.id}`);
        if (input && input.value.trim()) {
            total++;
            checkVerbInput(item.id);
            if (cleanKana(input.value) === cleanKana(item.nai)) {
                correct++;
            }
        }
    });

    if (total === 0) {
        showToast('⚠️ Bạn chưa nhập đáp án nào!');
    } else {
        showToast(`🎯 Kết quả: Đúng ${correct}/${total} câu đã nhập!`);
    }
}
function toggleShowAllAnswers() {
    showAnswersState = !showAnswersState;
    const btn = document.getElementById('btnToggleAnswers');
    if (showAnswersState) {
        btn.innerText = '🙈 Ẩn Toàn Bộ Đáp Án';
        verbsData.forEach(item => {
            const input = document.getElementById(`input_${item.id}`);
            if (input) {
                input.value = item.nai;
                checkVerbInput(item.id);
            }
        });
    } else {
        btn.innerText = '👁️ Hiện Toàn Bộ Đáp Án';
        resetAllInputs();
    }
}

function resetAllInputs() {
    showAnswersState = false;
    document.getElementById('btnToggleAnswers').innerText = '👁️ Hiện Toàn Bộ Đáp Án';
    verbsData.forEach(item => {
        const input = document.getElementById(`input_${item.id}`);
        if (input) {
            input.value = '';
            checkVerbInput(item.id);
        }
    });
}

function speakJapanese(text, btn) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'ja-JP';
    u.rate = 0.88;
    if (btn) {
        btn.style.transform = 'scale(1.3)';
        u.onend = () => { btn.style.transform = ''; };
    }
    window.speechSynthesis.speak(u);
}

// Lab Transformer
const VERB_TRANSFORMS = {
    'あいます': { kanji: '会います', group: 1, te: 'あって', ru: 'あう', ta: 'あった', nai: 'あわない', note: '⚠️ i ➔ わ + ない' },
    'かいます': { kanji: '買います', group: 1, te: 'かって', ru: 'かう', ta: 'かった', nai: 'かわない', note: '⚠️ i ➔ わ + ない' },
    'かえります': { kanji: '帰ります', group: 1, te: 'かえって', ru: 'かえる', ta: 'かえった', nai: 'かえらない', note: '⚠️ Bẫy nhóm 1 đuôi eru: ri ➔ ら + ない' },
    'はいります': { kanji: '入ります', group: 1, te: 'はいって', ru: 'はいる', ta: 'はいった', nai: 'はいらない', note: '⚠️ Bẫy nhóm 1 đuôi iru: ri ➔ ら + ない' },
    'あります': { kanji: '有ります', group: 1, te: 'あって', ru: 'ある', ta: 'あった', nai: 'ない', note: '🚨 Ngoại lệ tối thượng: ない (không có あらない)' },
    'いきます': { kanji: '行きます', group: 1, te: 'いって', ru: 'いく', ta: 'いった', nai: 'いかない', note: 'Thể Nai theo quy tắc: ki ➔ か + ない' },
    'のみます': { kanji: '飲みます', group: 1, te: 'のんで', ru: 'のむ', ta: 'のんだ', nai: 'のまない', note: 'mi ➔ ま + ない' },
    'かきます': { kanji: '書きます', group: 1, te: 'かいて', ru: 'かく', ta: 'かいた', nai: 'かかない', note: 'ki ➔ か + ない' },
    'はなします': { kanji: '話します', group: 1, te: 'はなして', ru: 'はなす', ta: 'はなした', nai: 'はなさない', note: 'shi ➔ さ + ない' },
    'たべます': { kanji: '食べます', group: 2, te: 'たべて', ru: 'たべる', ta: 'たべた', nai: 'たべない', note: 'Nhóm 2: Bỏ ます + ない' },
    'みます': { kanji: '見ます', group: 2, te: 'みて', ru: 'みる', ta: 'みた', nai: 'みない', note: 'Nhóm 2: 1 âm tiết bỏ ます + ない' },
    'おきます': { kanji: '起きます', group: 2, te: 'おきて', ru: 'おきる', ta: 'おきた', nai: 'おきない', note: 'Nhóm 2 đặc biệt âm i: bỏ ます + ない' },
    'きます': { kanji: '来ます', group: 3, te: 'きて', ru: 'くる', ta: 'きた', nai: 'こない', note: '🚨 Bẫy nhóm 3: kuru ➔ こない (đổi âm sang KO)' },
    'します': { kanji: '為ます', group: 3, te: 'して', ru: 'する', ta: 'した', nai: 'しない', note: 'Nhóm 3: suru ➔ しない' }
};

function setLabInput(val) {
    document.getElementById('labInput').value = val;
    transformLabVerb();
}

function transformLabVerb() {
    const raw = cleanKana(document.getElementById('labInput').value);
    const resBox = document.getElementById('labResultBox');
    if (!raw) {
        resBox.innerHTML = '<div style="color: var(--gray); font-size: 1.05rem;">Hãy gõ một động từ hoặc chọn từ mẫu bên trên để xem kết quả phân tích 4 thể!</div>';
        return;
    }

    // Check if in dictionary
    let found = VERB_TRANSFORMS[raw];
    if (!found) {
        // Check in verbsData
        const item = verbsData.find(v => cleanKana(v.masu) === raw || cleanKana(v.kanji) === raw);
        if (item) {
            found = {
                kanji: item.kanji,
                group: parseInt(item.group),
                te: '—',
                ru: '—',
                ta: '—',
                nai: item.nai,
                note: item.note
            };
        }
    }

    if (found) {
        resBox.innerHTML = `
        <div style="font-size: 1.6rem; font-weight: 900; color: #065f46; margin-bottom: 4px;" class="jp-text">${found.kanji || raw} (${raw})</div>
        <div style="display: inline-block; padding: 4px 14px; border-radius: 999px; background: #d1fae5; color: #065f46; font-weight: 800; font-size: 0.88rem; margin-bottom: 18px;">
            Nhóm ${found.group} • ${found.note || 'Quy tắc chuẩn'}
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; text-align: left;">
            <div style="background: white; border: 2px solid #a7f3d0; border-radius: 12px; padding: 14px; box-shadow: var(--shadow);">
                <div style="font-size: 0.82rem; font-weight: 800; color: #047857;">📗 THỂ NAI (ない形)</div>
                <div style="font-size: 1.4rem; font-weight: 900; color: #047857; margin: 4px 0;" class="jp-text">${found.nai}</div>
                <div style="font-size: 0.82rem; color: var(--gray);">Phủ định ngắn</div>
            </div>
            <div style="background: white; border: 2px solid #bfdbfe; border-radius: 12px; padding: 14px; box-shadow: var(--shadow);">
                <div style="font-size: 0.82rem; font-weight: 800; color: #1d4ed8;">📘 THỂ RU (辞書形)</div>
                <div style="font-size: 1.4rem; font-weight: 900; color: #1d4ed8; margin: 4px 0;" class="jp-text">${found.ru || '—'}</div>
                <div style="font-size: 0.82rem; color: var(--gray);">Thể từ điển</div>
            </div>
            <div style="background: white; border: 2px solid #fbcfe8; border-radius: 12px; padding: 14px; box-shadow: var(--shadow);">
                <div style="font-size: 0.82rem; font-weight: 800; color: #be185d;">🌸 THỂ TE (て形)</div>
                <div style="font-size: 1.4rem; font-weight: 900; color: #be185d; margin: 4px 0;" class="jp-text">${found.te || '—'}</div>
                <div style="font-size: 0.82rem; color: var(--gray);">Nối câu, xin phép</div>
            </div>
            <div style="background: white; border: 2px solid #fecdd3; border-radius: 12px; padding: 14px; box-shadow: var(--shadow);">
                <div style="font-size: 0.82rem; font-weight: 800; color: #e11d48;">📕 THỂ TA (た形)</div>
                <div style="font-size: 1.4rem; font-weight: 900; color: #e11d48; margin: 4px 0;" class="jp-text">${found.ta || '—'}</div>
                <div style="font-size: 0.82rem; color: var(--gray);">Thể quá khứ ngắn</div>
            </div>
        </div>
    `;
    } else {
        // Heuristic deduction
        resBox.innerHTML = `
        <div style="font-size: 1.3rem; font-weight: 800; color: var(--dark); margin-bottom: 8px;">Đang phân tích: <span class="jp-text">${raw}</span></div>
        <div style="color: var(--gray);">Gợi ý chuyển đổi theo quy tắc chung: Chuyển âm trước <strong>ます</strong> từ hàng <strong>「い」</strong> sang hàng <strong>「あ」</strong> rồi thêm <strong>ない</strong>!</div>
    `;
    }
}

// Quiz 15 Questions
const QUIZ_LIST = [
    { q: "Động từ 会います (あいます - Gặp) chia sang thể NAI là gì?", opts: ["あわない", "ああない", "あない", "あえあい"], ans: 0, exp: "Đuôi 'い' của nhóm 1 luôn chuyển thành 'わ' ➔ あわない." },
    { q: "Động từ あります (Có đồ vật) chia sang thể NAI là gì?", opts: ["あらない", "あない", "ない", "ありない"], ans: 2, exp: "Bẫy số 1: あります chuyển thành 'ない' (không có あらない)." },
    { q: "Động từ 来ます (きます - Đến) chia sang thể NAI là gì?", opts: ["きない", "こない", "くらない", "かない"], ans: 1, exp: "Bẫy số 2: kuru ➔ こない (chữ Hán là 来ない)." },
    { q: "Động từ 帰ります (かえります - Về) chia sang thể NAI là gì?", opts: ["かえらない", "かえない", "かえらないで", "かえりない"], ans: 0, exp: "帰ります thuộc Nhóm 1 (đuôi ri) ➔ かえらない." },
    { q: "Động từ 食べます (たべます - Ăn) chia sang thể NAI là gì?", opts: ["たべない", "たばない", "たべらない", "たべわない"], ans: 0, exp: "Nhóm 2 chỉ cần bỏ ます thêm ない ➔ たべない." },
    { q: "Động từ 行きます (いきます - Đi) chia sang thể NAI là gì?", opts: ["いかない", "いった", "いかないで", "いわない"], ans: 0, exp: "Khác với thể Te/Ta (いった), thể Nai của 行きます hoàn toàn quy tắc: ki ➔ ka ➔ いかない." },
    { q: "Động từ 待ちます (まちます - Chờ) chia sang thể NAI là gì?", opts: ["またない", "まちない", "まったない", "まつない"], ans: 0, exp: "Đuôi chi ➔ ta ➔ またない." },
    { q: "Động từ 話します (はなします - Nói) chia sang thể NAI là gì?", opts: ["はなさない", "はなしない", "はなしたない", "はなさらない"], ans: 0, exp: "Đuôi shi ➔ sa ➔ はなさない." },
    { q: "Động từ 買います (かいます - Mua) chia sang thể NAI là gì?", opts: ["かわない", "かあない", "かない", "かいらない"], ans: 0, exp: "Đuôi i ➔ wa ➔ かわない." },
    { q: "Cấu trúc: 'Xin đừng chụp ảnh ở đây' trong tiếng Nhật là:", opts: ["ここで 写真を 撮らないで ください。", "ここで 写真を 撮らなくて ください。", "ここで 写真を 撮らない ほうが いいです。", "ここで 写真を 撮って ください。"], ans: 0, exp: "Mẫu câu xin đừng làm gì: V-ないで ください." },
    { q: "Động từ 着ます (きます - Mặc áo) chia sang thể NAI là gì?", opts: ["きない", "こない", "きらない", "かかない"], ans: 0, exp: "着ます (mặc) thuộc Nhóm 2 ➔ きない. (Phân biệt với 来ます - đến ➔ こない)." },
    { q: "Động từ 起きます (おきます - Thức dậy) chia sang thể NAI là gì?", opts: ["おきない", "おかない", "おきらない", "おきわない"], ans: 0, exp: "起きます thuộc Nhóm 2 đặc biệt ➔ おきない." },
    { q: "Cấu trúc: 'Tôi phải uống thuốc' trong tiếng Nhật là:", opts: ["薬を 飲まなければ なりません。", "薬を 飲まなくても いいです。", "薬を 飲まないで ください。", "薬を 飲んだ ことが あります。"], ans: 0, exp: "Nghĩa vụ phải làm: V-なければ なりません." },
    { q: "Động từ 急ぎます (いそぎます - Vội) chia sang thể NAI là gì?", opts: ["いそがない", "いそかない", "いそぎない", "いそごない"], ans: 0, exp: "Đuôi gi ➔ ga ➔ いそがない." },
    { q: "Cấu trúc: 'Ngày mai bạn không cần đến cũng được' là:", opts: ["明日は 来なくても いいですよ。", "明日は 来ないで ください。", "明日は 来なければ なりません。", "明日は 来ない ほうが いいです。"], ans: 0, exp: "Không cần làm gì cũng được: V-なくても いいです." }
];

let quizAnswers = {};

function renderQuiz() {
    const container = document.getElementById('quizContainer');
    container.innerHTML = QUIZ_LIST.map((q, idx) => `
    <div style="background: #ffffff; border: 1.5px solid var(--border); border-radius: 12px; padding: 18px; margin-bottom: 14px;" id="qCard_${idx}">
        <div style="font-size: 0.85rem; font-weight: 800; color: var(--primary); margin-bottom: 6px;">CÂU ${idx + 1} / 15</div>
        <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 12px;" class="jp-text">${q.q}</div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 8px;">
            ${q.opts.map((opt, optIdx) => `
                <button type="button" onclick="selectQuizAnswer(${idx}, ${optIdx}, this)" style="background: #f8fafc; border: 1.5px solid var(--border); padding: 10px 14px; border-radius: 8px; font-weight: 700; cursor: pointer; text-align: left; transition: all 0.2s;">
                    ${['A', 'B', 'C', 'D'][optIdx]}. ${opt}
                </button>
            `).join('')}
        </div>
        <div id="qFb_${idx}" style="display: none; margin-top: 10px; padding: 10px 14px; border-radius: 8px; font-size: 0.92rem; font-weight: 600;"></div>
    </div>
`).join('');
}

function selectQuizAnswer(qIdx, optIdx, btn) {
    if (quizAnswers[qIdx] !== undefined) return;
    quizAnswers[qIdx] = optIdx;
    const q = QUIZ_LIST[qIdx];
    const card = document.getElementById(`qCard_${qIdx}`);
    const fb = document.getElementById(`qFb_${qIdx}`);
    const buttons = card.querySelectorAll('button');

    buttons.forEach((b, idx) => {
        b.disabled = true;
        if (idx === q.ans) {
            b.style.background = '#10b981';
            b.style.color = '#ffffff';
            b.style.borderColor = '#10b981';
        } else if (idx === optIdx) {
            b.style.background = '#ef4444';
            b.style.color = '#ffffff';
            b.style.borderColor = '#ef4444';
        } else {
            b.style.opacity = '0.5';
        }
    });

    fb.style.display = 'block';
    if (optIdx === q.ans) {
        fb.style.background = '#d1fae5';
        fb.style.color = '#065f46';
        fb.innerHTML = `✓ <strong>Chính xác!</strong> ${q.exp}`;
    } else {
        fb.style.background = '#fee2e2';
        fb.style.color = '#991b1b';
        fb.innerHTML = `✕ <strong>Chưa chính xác!</strong> ${q.exp}`;
    }

    updateScore();
}

function updateScore() {
    let score = 0;
    QUIZ_LIST.forEach((q, idx) => {
        if (quizAnswers[idx] === q.ans) score++;
    });
    document.getElementById('quizScoreText').innerText = score;
}

function copyQuizletFormat() {
    const text = verbsData.map(v => `${v.kanji}\t[${v.nai}] ${v.vi}`).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${verbsData.length} động từ thể NAI chuẩn Tab Quizlet Pro!`);
    }).catch(err => {
        alert('Không thể truy cập clipboard, vui lòng thử lại!');
    });
}

function showToast(msg) {
    let t = document.getElementById('toast');
    if (!t) return;
    t.innerText = msg;
    t.style.display = 'block';
    setTimeout(() => { t.style.display = 'none'; }, 2800);
}

// Init
document.addEventListener('DOMContentLoaded', () => {
    renderTable();
    renderQuiz();
});
