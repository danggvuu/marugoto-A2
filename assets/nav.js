/**
 * MARUGOTO A1-A2 GLOBAL NAVBAR COMPONENT (assets/nav.js)
 * Tự động render thanh điều hướng (navbar/dropdown/bottom sheet) chuẩn dùng chung cho toàn bộ website.
 * Tự động nhận diện thư mục gốc hay thư mục con (lessons/, tests/) để sinh đường dẫn chuẩn xác.
 * Tối ưu hóa 100% cho cả Điện thoại (Mobile Bottom Sheet) và Máy tính (Desktop Floating Dropdown).
 */

(function () {
    'use strict';

    // 1. DỮ LIỆU CÁC THỂ ĐỘNG TỪ (Được gom chung vào 1 thẻ gọn gàng)
    const ALL_VERB_FORMS = [
        { file: 'index.html', title: '🌸 Thể TE (～て)', desc: 'Cẩm nang & Bảng luyện tập chia thể TE (56 từ)' },
        { file: 'the_ru.html', title: '📘 Thể RU (Từ Điển)', desc: 'Thể nguyên mẫu Từ điển & Quy tắc chia Jisho' },
        { file: 'the_ta.html', title: '📕 Thể TA (Quá Khứ)', desc: 'Thể quá khứ ngắn Ta-kei & Hành động kinh nghiệm' },
        { file: 'the_nai.html', title: '📗 Thể NAI (Phủ Định)', desc: 'Thể phủ định ngắn Nai-kei & Mẫu câu khuyên cấm' },
        { file: 'Luyen_Tap_The_Te_A2_1.html', title: '⚡ Đấu Trường Luyện Thể TE', desc: 'Mini test phản xạ chia thể TE tốc độ cao', isTestFile: true }
    ];

    // DỮ LIỆU BÀI HỌC VÀ ĐỀ THI
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
        { file: 'On_Tap_Mini_Test_A2_15_18.html', title: '🎯 Ôn Tập Bài 15-18 (Bộ 5 Mã Đề)' },
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

    // 3. ĐẢM BẢO CSS SITE-THEME & CHECKPOINT SYNC ĐƯỢC NẠP
    (function ensureThemeCSS() {
        const existingLink = document.querySelector('link[href*="site-theme.css"]');
        if (!existingLink) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = rootPrefix + 'assets/css/site-theme.css?v=6';
            document.head.appendChild(link);
        }
        if (!window.__MARUGOTO_CHECKPOINT_LOADED__ && !document.querySelector('script[src*="checkpoint-sync.js"]')) {
            const cpScript = document.createElement('script');
            cpScript.src = rootPrefix + 'assets/js/checkpoint-sync.js?v=1';
            cpScript.defer = true;
            document.head.appendChild(cpScript);
        }
    })();

    // 4. TÍNH TOÁN TRẠNG THÁI ACTIVE
    const isTeActive = (!isLessons && !isTests && (currentFileName === 'index.html' || currentFileName === ''));
    const isRuActive = (!isLessons && !isTests && currentFileName === 'the_ru.html');
    const isTaActive = (!isLessons && !isTests && currentFileName === 'the_ta.html');
    const isNaiActive = (!isLessons && !isTests && currentFileName === 'the_nai.html');
    const isTePracticeActive = (isTests && currentFileName === 'Luyen_Tap_The_Te_A2_1.html');
    const isFormsActive = isTeActive || isRuActive || isTaActive || isNaiActive || isTePracticeActive;

    const isKanjiActive = (!isLessons && !isTests && currentFileName === 'kanji_a2.html');
    const isVocabActive = (!isLessons && !isTests && currentFileName === 'Tu_Vung_Marugoto_A1_16_A2_1_10.html');
    const isGrammarActive = (!isLessons && !isTests && currentFileName === 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html');
    const isKtbsActive = (!isLessons && !isTests && currentFileName === 'kien_thuc_bo_sung.html');
    const is3dActive = (!isLessons && !isTests && currentFileName === 'demo_3d.html');

    // 5. SINH HTML CHO CÁC MỤC DROPDOWN
    const formsDropdownHtml = ALL_VERB_FORMS.map(f => {
        const linkHref = f.isTestFile ? `${testsPrefix}${f.file}` : `${rootPrefix}${f.file}`;
        const isCurrent = f.isTestFile
            ? (isTests && currentFileName === f.file)
            : (!isLessons && !isTests && (currentFileName === f.file || (f.file === 'index.html' && (currentFileName === '' || currentFileName === 'index.html'))));
        return `<a href="${linkHref}" class="hub-drop-link${isCurrent ? ' active' : ''}">
            <div class="hub-drop-info">
                <span class="hub-drop-text">${f.title}</span>
                <span class="hub-drop-desc">${f.desc}</span>
            </div>
            ${isCurrent ? '<span class="hub-drop-tag">Đang mở</span>' : ''}
        </a>`;
    }).join('\n                ');

    const testsDropdownHtml = ALL_TESTS.map(t => {
        const isCurrent = isTests && currentFileName === t.file;
        return `<a href="${testsPrefix}${t.file}" class="hub-drop-link${isCurrent ? ' active' : ''}">
            <span class="hub-drop-text">${t.title}</span>
            ${isCurrent ? '<span class="hub-drop-tag">Đang mở</span>' : ''}
        </a>`;
    }).join('\n                ');

    const lessonsDropdownHtml = ALL_LESSONS.map(l => {
        const isCurrent = isLessons && currentFileName === l.file;
        return `<a href="${lessonsPrefix}${l.file}" class="hub-drop-link${isCurrent ? ' active' : ''}">
            <span class="hub-drop-text">${l.title}</span>
            ${isCurrent ? '<span class="hub-drop-tag">Đang mở</span>' : ''}
        </a>`;
    }).join('\n                ');

    // 6. TỔNG HỢP HTML TOÀN BỘ THANH NAVBAR VÀ BOTTOM SHEET/DROPDOWN
    const navbarHtml = `
    <div class="global-hub-nav-wrapper">
        <nav class="global-hub-nav" aria-label="Thanh điều hướng chính Marugoto">
            <!-- Thẻ gộp Các Thể Động Từ (Gọn gàng thay vì 4 nút riêng biệt) -->
            <button type="button" id="hubBtnForms" class="hub-nav-item${isFormsActive ? ' active-hub' : ''}" onclick="window.toggleFormsDropdown(event)">🎴 Các Thể Động Từ ▾</button>
            
            <a href="${rootPrefix}kanji_a2.html" class="hub-nav-item${isKanjiActive ? ' active-hub' : ''}">⛩️ Học Kanji & Nét Viết</a>
            <a href="${rootPrefix}Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item${isVocabActive ? ' active-hub' : ''}">📖 Kho Từ Vựng A1-A2</a>
            <a href="${rootPrefix}Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item${isGrammarActive ? ' active-hub' : ''}">📗 Ngữ Pháp A1-A2</a>
            <a href="${rootPrefix}kien_thuc_bo_sung.html" class="hub-nav-item${isKtbsActive ? ' active-hub' : ''}">💡 Kiến Thức Bổ Sung</a>
            <a href="${rootPrefix}demo_3d.html" class="hub-nav-item${is3dActive ? ' active-hub' : ''}">⛩️ Không Gian 3D</a>
            
            <button type="button" id="hubBtnTests" class="hub-nav-item${isTests ? ' active-hub' : ''}" onclick="window.toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <button type="button" id="hubBtnLessons" class="hub-nav-item${isLessons ? ' active-hub' : ''}" onclick="window.toggleLessonsDropdown(event)">🚀 Web Bài Học ▾</button>
        </nav>

        <!-- Lớp phủ mờ (Backdrop) cho Mobile và ngoài vùng click -->
        <div class="hub-backdrop" id="hubNavBackdrop" onclick="window.closeAllHubDropdowns()"></div>

        <!-- Menu Các Thể Động Từ (Desktop Dropdown & Mobile Bottom Sheet) -->
        <div class="hub-dropdown-menu" id="formsDropdownMenu" role="dialog" aria-modal="true">
            <div class="hub-drop-header">
                <span class="hub-drop-title">🎴 Các Thể Động Từ (TE / RU / TA / NAI)</span>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${formsDropdownHtml}
            </div>
        </div>

        <!-- Menu Ôn Tập & Đề Thi (Desktop Dropdown & Mobile Bottom Sheet) -->
        <div class="hub-dropdown-menu" id="testsDropdownMenu" role="dialog" aria-modal="true">
            <div class="hub-drop-header">
                <span class="hub-drop-title">🎯 Ôn Tập & Đề Thi Marugoto</span>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${testsDropdownHtml}
            </div>
        </div>

        <!-- Menu Web Bài Học (Desktop Dropdown & Mobile Bottom Sheet) -->
        <div class="hub-dropdown-menu" id="lessonsDropdownMenu" role="dialog" aria-modal="true">
            <div class="hub-drop-header">
                <span class="hub-drop-title">🚀 Toàn Bộ Bài Học (Bài 1 - 18)</span>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${lessonsDropdownHtml}
            </div>
        </div>
    </div>`;

    // 7. HÀM ĐỊNH VỊ VÀ ĐIỀU KHIỂN DROPDOWN
    function positionDesktopMenu(btn, menu) {
        if (!btn || !menu) return;
        if (window.innerWidth > 768) {
            const wrapper = menu.closest('.global-hub-nav-wrapper') || btn.parentElement;
            const btnRect = btn.getBoundingClientRect();
            const wrapperRect = wrapper.getBoundingClientRect();

            menu.style.top = (btnRect.bottom - wrapperRect.top + 8) + 'px';
            menu.style.left = (btnRect.left - wrapperRect.left + (btnRect.width / 2)) + 'px';
            menu.style.transform = 'translateX(-50%)';
        } else {
            menu.style.top = '';
            menu.style.left = '';
            menu.style.transform = '';
        }
    }

    function closeAllHubDropdowns() {
        const fm = document.getElementById('formsDropdownMenu');
        const tm = document.getElementById('testsDropdownMenu');
        const lm = document.getElementById('lessonsDropdownMenu');
        const bd = document.getElementById('hubNavBackdrop');
        if (fm) fm.classList.remove('show');
        if (tm) tm.classList.remove('show');
        if (lm) lm.classList.remove('show');
        if (bd) bd.classList.remove('show');
        document.body.classList.remove('hub-menu-open');
    }

    function toggleFormsDropdown(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const fm = document.getElementById('formsDropdownMenu');
        const tm = document.getElementById('testsDropdownMenu');
        const lm = document.getElementById('lessonsDropdownMenu');
        const bd = document.getElementById('hubNavBackdrop');
        const btn = document.getElementById('hubBtnForms');

        if (!fm) return;

        if (tm) tm.classList.remove('show');
        if (lm) lm.classList.remove('show');

        const willOpen = !fm.classList.contains('show');
        if (willOpen) {
            positionDesktopMenu(btn, fm);
            fm.classList.add('show');
            if (bd) bd.classList.add('show');
            if (window.innerWidth <= 768) {
                document.body.classList.add('hub-menu-open');
            }
        } else {
            fm.classList.remove('show');
            if (bd) bd.classList.remove('show');
            document.body.classList.remove('hub-menu-open');
        }
    }

    function toggleTestsDropdown(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const fm = document.getElementById('formsDropdownMenu');
        const tm = document.getElementById('testsDropdownMenu');
        const lm = document.getElementById('lessonsDropdownMenu');
        const bd = document.getElementById('hubNavBackdrop');
        const btn = document.getElementById('hubBtnTests');

        if (!tm) return;

        if (fm) fm.classList.remove('show');
        if (lm) lm.classList.remove('show');

        const willOpen = !tm.classList.contains('show');
        if (willOpen) {
            positionDesktopMenu(btn, tm);
            tm.classList.add('show');
            if (bd) bd.classList.add('show');
            if (window.innerWidth <= 768) {
                document.body.classList.add('hub-menu-open');
            }
        } else {
            tm.classList.remove('show');
            if (bd) bd.classList.remove('show');
            document.body.classList.remove('hub-menu-open');
        }
    }

    function toggleLessonsDropdown(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const fm = document.getElementById('formsDropdownMenu');
        const tm = document.getElementById('testsDropdownMenu');
        const lm = document.getElementById('lessonsDropdownMenu');
        const bd = document.getElementById('hubNavBackdrop');
        const btn = document.getElementById('hubBtnLessons');

        if (!lm) return;

        if (fm) fm.classList.remove('show');
        if (tm) tm.classList.remove('show');

        const willOpen = !lm.classList.contains('show');
        if (willOpen) {
            positionDesktopMenu(btn, lm);
            lm.classList.add('show');
            if (bd) bd.classList.add('show');
            if (window.innerWidth <= 768) {
                document.body.classList.add('hub-menu-open');
            }
        } else {
            lm.classList.remove('show');
            if (bd) bd.classList.remove('show');
            document.body.classList.remove('hub-menu-open');
        }
    }

    // Đóng dropdown khi click ra ngoài (dành cho Desktop)
    document.addEventListener('click', function (e) {
        if (e && e.target && e.target.closest && (
            e.target.closest('.hub-dropdown-menu') || 
            e.target.closest('#hubBtnForms') || 
            e.target.closest('#hubBtnTests') || 
            e.target.closest('#hubBtnLessons')
        )) {
            return;
        }
        closeAllHubDropdowns();
    });

    // Đóng khi nhấn phím Escape
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            closeAllHubDropdowns();
        }
    });

    // Tự động căn chỉnh khi resize màn hình
    window.addEventListener('resize', function () {
        const fm = document.getElementById('formsDropdownMenu');
        const tm = document.getElementById('testsDropdownMenu');
        const lm = document.getElementById('lessonsDropdownMenu');
        if (fm && fm.classList.contains('show')) {
            positionDesktopMenu(document.getElementById('hubBtnForms'), fm);
        }
        if (tm && tm.classList.contains('show')) {
            positionDesktopMenu(document.getElementById('hubBtnTests'), tm);
        }
        if (lm && lm.classList.contains('show')) {
            positionDesktopMenu(document.getElementById('hubBtnLessons'), lm);
        }
    });

    // Phơi ra global để onclick gọi được
    window.toggleFormsDropdown = toggleFormsDropdown;
    window.toggleTestsDropdown = toggleTestsDropdown;
    window.toggleLessonsDropdown = toggleLessonsDropdown;
    window.closeAllHubDropdowns = closeAllHubDropdowns;

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
        const container = document.querySelector('.container') || document.querySelector('.main-container');
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
