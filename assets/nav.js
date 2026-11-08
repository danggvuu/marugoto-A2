/**
 * MARUGOTO A1-A2 GLOBAL NAVBAR COMPONENT (assets/nav.js)
 * Tự động render thanh điều hướng (navbar/dropdown) chuẩn dùng chung cho toàn bộ website.
 * Tự động nhận diện thư mục gốc hay thư mục con (lessons/, tests/) để sinh đường dẫn chuẩn xác.
 */

(function () {
    'use strict';

    // 1. DỮ LIỆU BÀI HỌC VÀ ĐỀ THI
    const ALL_LESSONS = [
        { file: 'Marugoto_A2_Lesson_1.html', title: '🌸 Bài 1: Nơi ở & Gia đình' },
        { file: 'Marugoto_A2_Lesson_2.html', title: '🎨 Bài 2: Sở thích & Ngôn ngữ' },
        { file: 'Marugoto_A2_Lesson_3.html', title: '🍁 Bài 3: Mùa & Khí hậu' },
        { file: 'Marugoto_A2_Lesson_4.html', title: '⛅ Bài 4: Thời tiết & Dự báo' },
        { file: 'Marugoto_A2_Lesson_5.html', title: '🏙️ Bài 5: Phố xá & Nơi chốn' },
        { file: 'Marugoto_A2_Lesson_6.html', title: '🗺️ Bài 6: Chỉ đường & Ngã rẽ' },
        { file: 'Marugoto_A2_Lesson_7.html', title: '⏰ Bài 7: Hẹn gặp & Giờ giấc' },
        { file: 'Marugoto_A2_Lesson_8.html', title: '⛩️ Bài 8: Sự kiện & Mời mọc' },
        { file: 'Marugoto_A2_Lesson_9.html', title: '🗣️ Bài 9: Học tập & Phát âm' },
        { file: 'Marugoto_A2_Lesson_10.html', title: '🌟 Bài 10: Ngoại ngữ & Văn hóa' },
        { file: 'Marugoto_A2_Lesson_11.html', title: '🍱 Bài 11: Dã ngoại & Ăn uống' },
        { file: 'Marugoto_A2_Lesson_12.html', title: '🍜 Bài 12: Món ăn ngày đặc biệt' },
        { file: 'Marugoto_A2_Lesson_13.html', title: '✈️ Bài 13: Đi công tác & Gặp gỡ' },
        { file: 'Marugoto_A2_Lesson_14.html', title: '💻 Bài 14: Quy tắc nơi làm việc' },
        { file: 'Marugoto_A2_Lesson_15.html', title: '🏥 Bài 15: Sức khỏe & Thể dục' },
        { file: 'Marugoto_A2_Lesson_16.html', title: '🏃 Bài 16: Tập luyện & Vận động' },
        { file: 'Marugoto_A2_Lesson_17.html', title: '🎁 Bài 17: Quà tặng & Kỷ niệm' },
        { file: 'Marugoto_A2_Lesson_18.html', title: '👘 Bài 18: Tiệc tùng & Sự kiện' }
    ];

    const ALL_TESTS = [
        { file: 'On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html', title: '⚡ Cấp Tốc Đêm Nay: Kanji 11-18 & NPBS 14' },
        { file: 'De_Thi_Midterm_A2_1.html', title: '🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)' },
        { file: 'On_Tap_Dich_Cau_Lesson_1_10.html', title: '✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)' },
        { file: 'On_Tap_Mini_Test_A2_1_4.html', title: '🎯 Ôn Tập Bài 1-4 (Mini Test)' },
        { file: 'On_Tap_Mini_Test_A2_5_8.html', title: '🎯 Ôn Tập Bài 5-8 (Mini Test)' },
        { file: 'On_Tap_Mini_Test_A2_11_14.html', title: '🎯 Ôn Tập Bài 11-14 (Mini Test)' },
        { file: 'On_Tap_Mini_Test_A2_15_18.html', title: '🎯 Ôn Tập Bài 15-18 (Mini Test Final)' },
        { file: 'De_Thi_Thu_Marugoto_A2_5_8.html', title: '📝 5 Mã Đề Thi Thử (101-105)' },
        { file: 'Kiem_Tra_Marugoto_L6_7_8.html', title: '📑 Đề Kiểm Tra L6, 7, 8' },
        { file: 'Luyen_Tap_The_Te_A2_1.html', title: '🌸 Luyện Tập Thể Te' }
    ];

    // 2. NHẬN DIỆN VỊ TRÍ FILE HIỆN TẠI (URL PATH DETECTION)
    const href = window.location.href;
    const pathname = window.location.pathname;
    const isLessons = pathname.includes('/lessons/') || href.includes('/lessons/');
    const isTests = pathname.includes('/tests/') || href.includes('/tests/');

    const rootPrefix = (isLessons || isTests) ? '../' : '';
    const lessonsPrefix = isLessons ? '' : ((isTests ? '../lessons/' : 'lessons/'));
    const testsPrefix = isTests ? '' : ((isLessons ? '../tests/' : 'tests/'));

    // Tên file hiện tại
    let currentFileName = pathname.split('/').pop() || 'index.html';
    if (!currentFileName || currentFileName.trim() === '') currentFileName = 'index.html';

    // 3. ĐẢM BẢO CSS SITE-THEME ĐƯỢC NẠP
    (function ensureThemeCSS() {
        const existingLink = document.querySelector('link[href*="site-theme.css"]');
        if (!existingLink) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = rootPrefix + 'assets/css/site-theme.css';
            document.head.appendChild(link);
        }
    })();

    // 4. TÍNH TOÁN TRẠNG THÁI ACTIVE
    const isTeActive = (!isLessons && !isTests && (currentFileName === 'index.html' || currentFileName === ''));
    const isRuActive = (!isLessons && !isTests && currentFileName === 'the_ru.html');
    const isTaActive = (!isLessons && !isTests && currentFileName === 'the_ta.html');
    const isNaiActive = (!isLessons && !isTests && currentFileName === 'the_nai.html');
    const isKanjiActive = (!isLessons && !isTests && currentFileName === 'kanji_a2.html');
    const isVocabActive = (!isLessons && !isTests && currentFileName === 'Tu_Vung_Marugoto_A1_16_A2_1_10.html');
    const isGrammarActive = (!isLessons && !isTests && currentFileName === 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html');
    const isKtbsActive = (!isLessons && !isTests && currentFileName === 'kien_thuc_bo_sung.html');
    const is3dActive = (!isLessons && !isTests && currentFileName === 'demo_3d.html');

    // 5. SINH HTML CHO CÁC MỤC DROPDOWN
    const testsDropdownHtml = ALL_TESTS.map(t => {
        const isCurrent = isTests && currentFileName === t.file;
        return `<a href="${testsPrefix}${t.file}" class="hub-drop-link${isCurrent ? ' active' : ''}">${t.title}</a>`;
    }).join('\n                ');

    const lessonsDropdownHtml = ALL_LESSONS.map(l => {
        const isCurrent = isLessons && currentFileName === l.file;
        return `<a href="${lessonsPrefix}${l.file}" class="hub-drop-link${isCurrent ? ' active' : ''}">${l.title}</a>`;
    }).join('\n                ');

    // 6. TỔNG HỢP HTML TOÀN BỘ THANH NAVBAR
    const navbarHtml = `
    <div class="global-hub-nav">
        <a href="${rootPrefix}index.html" class="hub-nav-item${isTeActive ? ' active-hub' : ''}">🌸 Thể TE (～て)</a>
        <a href="${rootPrefix}the_ru.html" class="hub-nav-item${isRuActive ? ' active-hub' : ''}">📘 Thể RU (Từ Điển)</a>
        <a href="${rootPrefix}the_ta.html" class="hub-nav-item${isTaActive ? ' active-hub' : ''}">📕 Thể TA (Quá Khứ)</a>
        <a href="${rootPrefix}the_nai.html" class="hub-nav-item${isNaiActive ? ' active-hub' : ''}">📗 Thể NAI (Phủ Định)</a>
        <a href="${rootPrefix}kanji_a2.html" class="hub-nav-item${isKanjiActive ? ' active-hub' : ''}">⛩️ Học Kanji & Nét Viết</a>
        <a href="${rootPrefix}Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item${isVocabActive ? ' active-hub' : ''}">📖 Kho Từ Vựng A1-A2</a>
        <a href="${rootPrefix}Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item${isGrammarActive ? ' active-hub' : ''}">📗 Ngữ Pháp A1-A2</a>
        <a href="${rootPrefix}kien_thuc_bo_sung.html" class="hub-nav-item${isKtbsActive ? ' active-hub' : ''}">💡 Kiến Thức Bổ Sung</a>
        <a href="${rootPrefix}demo_3d.html" class="hub-nav-item${is3dActive ? ' active-hub' : ''}">⛩️ Không Gian 3D</a>
        
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item${isTests ? ' active-hub' : ''}" onclick="window.toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                ${testsDropdownHtml}
            </div>
        </div>

        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item${isLessons ? ' active-hub' : ''}" onclick="window.toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                ${lessonsDropdownHtml}
            </div>
        </div>
    </div>`;

    // 7. HÀM TOGGLE DROPDOWN
    function toggleTestsDropdown(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const m = document.getElementById('testsDropdownMenu');
        if (m) m.classList.toggle('show');
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
    }

    function toggleLessonsDropdown(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) m.classList.toggle('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    }

    // Đóng dropdown khi click ra ngoài
    document.addEventListener('click', function (e) {
        if (e && e.target && e.target.closest && e.target.closest('.hub-dropdown')) {
            return;
        }
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    });

    // Đóng khi nhấn phím Escape
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            const lm = document.getElementById('lessonsDropdownMenu');
            if (lm) lm.classList.remove('show');
            const tm = document.getElementById('testsDropdownMenu');
            if (tm) tm.classList.remove('show');
        }
    });

    // Phơi ra global để onclick gọi được
    window.toggleTestsDropdown = toggleTestsDropdown;
    window.toggleLessonsDropdown = toggleLessonsDropdown;

    // 8. RENDER VÀO DOM (Tìm #navbar-placeholder hoặc thay thế .global-hub-nav)
    function renderNavbar() {
        const placeholder = document.getElementById('navbar-placeholder');
        if (placeholder) {
            placeholder.innerHTML = navbarHtml;
            return;
        }

        const existingNav = document.querySelector('.global-hub-nav');
        if (existingNav) {
            const temp = document.createElement('div');
            temp.innerHTML = navbarHtml;
            const newNav = temp.firstElementChild;
            existingNav.parentNode.replaceChild(newNav, existingNav);
            return;
        }

        // Nếu chưa có chỗ, chèn vào đầu container hoặc đầu body
        const container = document.querySelector('.container');
        if (container) {
            const temp = document.createElement('div');
            temp.innerHTML = navbarHtml;
            container.insertBefore(temp.firstElementChild, container.firstChild);
        } else {
            const temp = document.createElement('div');
            temp.innerHTML = navbarHtml;
            document.body.insertBefore(temp.firstElementChild, document.body.firstChild);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', renderNavbar);
    } else {
        renderNavbar();
    }
})();
