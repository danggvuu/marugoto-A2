/**
 * MARUGOTO A1-A2 GLOBAL NAVBAR COMPONENT (assets/nav.js)
 * Tự động render thanh điều hướng dạng viên thuốc (sticky glassmorphic capsule) chuẩn cho toàn bộ website.
 * Tự động nhận diện thư mục gốc hay thư mục con (lessons/, tests/) để sinh đường dẫn chuẩn xác.
 * Hỗ trợ 6 cụm dropdown nhóm thông minh: Động Từ, Kanji, Từ Vựng, Ngữ Pháp, Đề Thi, Bài Học.
 * Tối ưu hóa 100% cho Desktop (Floating Dropdown định vị thông minh) và Mobile (Bottom Sheet Modal mượt mà).
 */

(function () {
    'use strict';

    // 1. DỮ LIỆU CÁC MỤC ĐIỀU HƯỚNG THEO NHÓM
    const ALL_VERB_FORMS = [
        { file: 'Luyen_Tap_The_Te_A2_1.html', title: '🌸 Thể TE (～て)', desc: 'Cẩm nang & Bảng luyện tập chia thể TE (56 từ)', isTestFile: true, tag: 'Cốt lõi' },
        { file: 'the_ru.html', title: '📘 Thể RU (Từ Điển)', desc: 'Thể nguyên mẫu Từ điển & Quy tắc chia Jisho', tag: 'Jisho' },
        { file: 'the_ta.html', title: '📕 Thể TA (Quá Khứ)', desc: 'Thể quá khứ ngắn Ta-kei & Mẫu câu kinh nghiệm', tag: 'Ta-kei' },
        { file: 'the_nai.html', title: '📗 Thể NAI (Phủ Định)', desc: 'Thể phủ định ngắn Nai-kei & Mẫu câu khuyên cấm', tag: 'Nai-kei' },
        { file: 'tu_tha_dong_tu.html', title: '⚖️ Tự Động Từ & Tha Động Từ', desc: '50 cặp Tự - Tha, 5 thần chú đuôi & trắc nghiệm', tag: 'Trọng tâm' },
        { file: 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html#tabVerbLabView', title: '🧪 Verb Lab: Thí Nghiệm Động Từ', desc: 'Mô phỏng biến đổi đuôi động từ trực quan tương tác', tag: 'Tương tác' }
    ];

    const ALL_KANJI_ITEMS = [
        { file: 'kanji_a2.html', title: '⛩️ Học Kanji & Bút Thuận A2', desc: 'Thẻ flashcard, 8 quy tắc viết & canvas luyện nét', tag: 'Cốt lõi' },
        { file: 'kanji_a2.html#tab-vocab-11-18', title: '🎴 121 Từ Ghép Kanji Trọng Tâm', desc: 'Hệ thống từ vựng Hán tự bài 11-18 kèm âm On/Kun', tag: 'Bài 11-18' },
        { file: 'kanji_a2.html#tab-exercises', title: '📝 Luyện Bút Thuận & Phản Xạ', desc: 'Điền Hiragana cho Kanji & trắc nghiệm 4 lựa chọn', tag: 'Bài tập' },
        { file: 'On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html', title: '⚡ Cấp Tốc Đêm Nay: Kanji 11-18 & NPBS 14', desc: 'Ôn siêu tốc 121 từ Kanji + 5 chủ điểm NPBS 14', isTestFile: true, tag: 'Cấp tốc' }
    ];

    const ALL_VOCAB_ITEMS = [
        { file: 'Tu_Vung_Marugoto_A1_16_A2_1_10.html', title: '📖 Kho Từ Vựng Toàn Diện A1-A2', desc: 'Bảng tra cứu 1000+ từ vựng A1-A2 kèm bộ lọc thông minh', tag: 'Tra cứu' },
        { file: 'Tu_Vung_Marugoto_A1_16_A2_1_10.html#view-flashcard', title: '🎴 Flashcard Ôn Nhớ Từ Vựng', desc: 'Lật thẻ luyện ghi nhớ nghĩa, từ loại & phát âm', tag: 'Flashcard' },
        { file: 'Tu_Vung_Marugoto_A1_16_A2_1_10.html#view-quiz', title: '🎯 Trắc Nghiệm Phản Xạ Nghĩa Từ', desc: 'Thử thách trắc nghiệm chọn nghĩa tiếng Việt chuẩn xác', tag: 'Quiz' },
        { file: 'On_Tap_Dich_Cau_Lesson_1_10.html', title: '✍️ Luyện Dịch Câu Bài 1 - 10', desc: '40 câu luyện dịch 2 chiều Nhật - Việt củng cố từ vựng', isTestFile: true, tag: 'Luyện dịch' }
    ];

    const ALL_GRAMMAR_ITEMS = [
        { file: 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html', title: '📗 Tổng Hợp Ngữ Pháp A1-A2', desc: 'Toàn bộ chủ điểm ngữ pháp cốt lõi Marugoto A1 và A2', tag: 'Tổng hợp' },
        { file: 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html#tabVerbLabView', title: '🧪 Verb Lab: Thí Nghiệm Động Từ', desc: 'Khảo sát chuyển đổi thể động từ trực quan tức thì', tag: 'Thực hành' },
        { file: 'kien_thuc_bo_sung.html', title: '💡 Cẩm Nang Kiến Thức Bổ Sung', desc: 'Văn hóa giao tiếp, kính ngữ & mở rộng đối thoại thực tế', tag: 'Cẩm nang' }
    ];

    const ALL_TESTS = [
        { file: 'Luyen_Kaiwa_5_Phut.html', title: '🎙️ Luyện Kaiwa Phỏng Vấn 5 Phút (4 Chủ Đề Cô Giáo)', desc: 'Mô phỏng thi vấn đáp: Sức khỏe, Thăm hỏi, Tiệc mừng & Đi Nhật', tag: 'HOT', isRootFile: true },
        { file: 'De_Thi_Tong_Hop_JLPT_A2_11_18.html', title: '🎯 Tổng Ôn Tập & Đề Thi Thử Bài 11 - 18 (Đề Gốc PDF & 5 Mã Đề)', desc: 'Chuẩn 100% De_on_tap_JLPT_A2_Bai_11-18.pdf + 5 mã đề thực chiến 71 câu', tag: 'Đề 11-18' },
        { file: 'De_Thi_Midterm_A2_1.html', title: '🎯 Bộ 5 Đề Thi Giữa Kỳ Midterm (M101 - M105)', desc: 'Bộ 5 đề thi chuẩn điểm 100 có tính giờ & chấm điểm', tag: 'Midterm' },
        { file: 'On_Tap_Mini_Test_A2_15_18.html', title: '🎯 Ôn Tập Bài 15-18 (Bộ 5 Mã Đề)', desc: 'Khảo sát năng lực chuyên sâu 4 bài cuối kỳ A2-1', tag: 'Đề 15-18' },
        { file: 'On_Tap_Mini_Test_A2_11_14.html', title: '🎯 Ôn Tập Bài 11-14 (Mini Test)', desc: '6 dạng bài thực chiến: Trắc nghiệm, xếp câu, nối cột', tag: 'Đề 11-14' },
        { file: 'On_Tap_Mini_Test_A2_5_8.html', title: '🎯 Ôn Tập Bài 5-8 (Mini Test)', desc: 'Trọng tâm giao tiếp, chỉ đường & sự kiện', tag: 'Đề 5-8' },
        { file: 'On_Tap_Mini_Test_A2_1_4.html', title: '🎯 Ôn Tập Bài 1-4 (Mini Test)', desc: 'Củng cố nền tảng nơi ở, thời tiết & sở thích', tag: 'Đề 1-4' },
        { file: 'De_Thi_Thu_Marugoto_A2_5_8.html', title: '📝 5 Mã Đề Thi Thử (101-105)', desc: 'Luyện thi thử tổng hợp Marugoto A2 bài 5-8', tag: 'Thi thử' },
        { file: 'Kiem_Tra_Marugoto_L6_7_8.html', title: '📑 Đề Kiểm Tra L6, 7, 8', desc: 'Bài kiểm tra định kỳ 3 bài L6, 7, 8', tag: 'Kiểm tra' },
        { file: 'On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html', title: '⚡ Cấp Tốc Đêm Nay: Kanji 11-18 & NPBS 14', desc: 'Ôn siêu tốc 121 từ Kanji + 5 chủ điểm NPBS 14', tag: 'Cấp tốc' },
        { file: 'On_Tap_Dich_Cau_Lesson_1_10.html', title: '✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)', desc: 'Luyện dịch 2 chiều Nhật - Việt phản xạ nhanh', tag: 'Luyện dịch' },
        { file: 'Luyen_Tap_The_Te_A2_1.html', title: '⚡ Đấu Trường Luyện Thể TE', desc: 'Mini test phản xạ chia thể TE tốc độ cao', tag: 'Động từ' }
    ];

    const ALL_LESSONS_A2_2 = [
        {
                "file": "Marugoto_A2_2_Lesson_1.html",
                "num": "01",
                "title": "Bài 1: Tên gọi & Giới thiệu",
                "icon": "🌸"
        },
        {
                "file": "Marugoto_A2_2_Lesson_2.html",
                "num": "02",
                "title": "Bài 2: Trang phục & Miêu tả người",
                "icon": "👓"
        },
        {
                "file": "Marugoto_A2_2_Lesson_3.html",
                "num": "03",
                "title": "Bài 3: Quán ăn & Món gợi ý",
                "icon": "🍲"
        },
        {
                "file": "Marugoto_A2_2_Lesson_4.html",
                "num": "04",
                "title": "Bài 4: Cách ăn & Bỏ nguyên liệu",
                "icon": "🥢"
        },
        {
                "file": "Marugoto_A2_2_Lesson_5.html",
                "num": "05",
                "title": "Bài 5: Du lịch & Chuẩn bị hành lý",
                "icon": "✈️"
        },
        {
                "file": "Marugoto_A2_2_Lesson_6.html",
                "num": "06",
                "title": "Bài 6: Tắm biển & Trải nghiệm",
                "icon": "🏖️"
        },
        {
                "file": "Marugoto_A2_2_Lesson_7.html",
                "num": "07",
                "title": "Bài 7: Lễ hội & Rủ rê tham gia",
                "icon": "🏮"
        },
        {
                "file": "Marugoto_A2_2_Lesson_8.html",
                "num": "08",
                "title": "Bài 8: Hòa nhạc & Quầy hàng Yatai",
                "icon": "🎆"
        },
        {
                "file": "Marugoto_A2_2_Lesson_9.html",
                "num": "09",
                "title": "Bài 9: Tiệc mừng & Tặng quà",
                "icon": "🎉"
        },
        {
                "file": "Marugoto_A2_2_Lesson_10.html",
                "num": "10",
                "title": "Bài 10: Bánh sinh nhật & Cảm ơn",
                "icon": "🎂"
        },
        {
                "file": "Marugoto_A2_2_Lesson_11.html",
                "num": "11",
                "title": "Bài 11: Đồ gia dụng bị hỏng",
                "icon": "🧹"
        },
        {
                "file": "Marugoto_A2_2_Lesson_12.html",
                "num": "12",
                "title": "Bài 12: So sánh & Mua sắm online",
                "icon": "🏷️"
        },
        {
                "file": "Marugoto_A2_2_Lesson_13.html",
                "num": "13",
                "title": "Bài 13: Chỉ đường & Đi tàu xe",
                "icon": "🚇"
        },
        {
                "file": "Marugoto_A2_2_Lesson_14.html",
                "num": "14",
                "title": "Bài 14: Thăm đền chùa & Di tích",
                "icon": "🛕"
        },
        {
                "file": "Marugoto_A2_2_Lesson_15.html",
                "num": "15",
                "title": "Bài 15: Quy tắc phân loại rác",
                "icon": "♻️"
        },
        {
                "file": "Marugoto_A2_2_Lesson_16.html",
                "num": "16",
                "title": "Bài 16: Thói quen tiết kiệm Eco",
                "icon": "🌱"
        },
        {
                "file": "Marugoto_A2_2_Lesson_17.html",
                "num": "17",
                "title": "Bài 17: Cuộc đời & Danh nhân",
                "icon": "🏆"
        },
        {
                "file": "Marugoto_A2_2_Lesson_18.html",
                "num": "18",
                "title": "Bài 18: Kỷ niệm & Tương lai",
                "icon": "🚀"
        }
];

    const ALL_LESSONS = [
        { file: 'Marugoto_A2_Lesson_1.html', num: '01', title: 'Bài 1: Nơi ở & Gia đình', icon: '🌸' },
        { file: 'Marugoto_A2_Lesson_2.html', num: '02', title: 'Bài 2: Sở thích & Ngôn ngữ', icon: '🎨' },
        { file: 'Marugoto_A2_Lesson_3.html', num: '03', title: 'Bài 3: Mùa & Khí hậu', icon: '🍁' },
        { file: 'Marugoto_A2_Lesson_4.html', num: '04', title: 'Bài 4: Thời tiết & Dự báo', icon: '⛅' },
        { file: 'Marugoto_A2_Lesson_5.html', num: '05', title: 'Bài 5: Phố xá & Nơi chốn', icon: '🏙️' },
        { file: 'Marugoto_A2_Lesson_6.html', num: '06', title: 'Bài 6: Chỉ đường & Ngã rẽ', icon: '🗺️' },
        { file: 'Marugoto_A2_Lesson_7.html', num: '07', title: 'Bài 7: Hẹn gặp & Giờ giấc', icon: '⏰' },
        { file: 'Marugoto_A2_Lesson_8.html', num: '08', title: 'Bài 8: Sự kiện & Mời mọc', icon: '⛩️' },
        { file: 'Marugoto_A2_Lesson_9.html', num: '09', title: 'Bài 9: Học tập & Phát âm', icon: '🗣️' },
        { file: 'Marugoto_A2_Lesson_10.html', num: '10', title: 'Bài 10: Ngoại ngữ & Văn hóa', icon: '🌟' },
        { file: 'Marugoto_A2_Lesson_11.html', num: '11', title: 'Bài 11: Dã ngoại & Ăn uống', icon: '🍱' },
        { file: 'Marugoto_A2_Lesson_12.html', num: '12', title: 'Bài 12: Món ăn ngày đặc biệt', icon: '🍜' },
        { file: 'Marugoto_A2_Lesson_13.html', num: '13', title: 'Bài 13: Đi công tác & Gặp gỡ', icon: '✈️' },
        { file: 'Marugoto_A2_Lesson_14.html', num: '14', title: 'Bài 14: Quy tắc nơi làm việc', icon: '💻' },
        { file: 'Marugoto_A2_Lesson_15.html', num: '15', title: 'Bài 15: Sức khỏe & Thể dục', icon: '🏥' },
        { file: 'Marugoto_A2_Lesson_16.html', num: '16', title: 'Bài 16: Tập luyện & Vận động', icon: '🏃' },
        { file: 'Marugoto_A2_Lesson_17.html', num: '17', title: 'Bài 17: Quà tặng & Kỷ niệm', icon: '🎁' },
        { file: 'Marugoto_A2_Lesson_18.html', num: '18', title: 'Bài 18: Tiệc tùng & Sự kiện', icon: '👘' }
    ];

    // 2. NHẬN DIỆN VỊ TRÍ FILE HIỆN TẠI (URL PATH DETECTION)
    const href = window.location.href;
    const pathname = window.location.pathname;
    const isLessons = pathname.includes('/lessons/') || href.includes('/lessons/');
    const isTests = pathname.includes('/tests/') || href.includes('/tests/');

    const rootPrefix = (isLessons || isTests) ? '../' : '';
    const lessonsPrefix = isLessons ? '' : ((isTests ? '../lessons/' : 'lessons/'));
    const testsPrefix = isTests ? '' : ((isLessons ? '../tests/' : 'tests/'));

    let currentFileName = pathname.split('/').pop() || 'index.html';
    if (!currentFileName || currentFileName.trim() === '') currentFileName = 'index.html';
    currentFileName = currentFileName.split('#')[0].split('?')[0];

    // 3. ĐẢM BẢO CSS SITE-THEME & NAV.CSS & CHECKPOINT SYNC ĐƯỢC NẠP
    (function injectStyles() {
        // Nạp site-theme.css nếu chưa có
        const existingLink = document.querySelector('link[href*="site-theme.css"]');
        if (!existingLink) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = rootPrefix + 'assets/css/site-theme.css?v=6';
            document.head.appendChild(link);
        }

        // Nạp nav.css chuyên dụng
        const existingNavCss = document.querySelector('link[href*="nav.css"]');
        if (!existingNavCss) {
            const navLink = document.createElement('link');
            navLink.rel = 'stylesheet';
            navLink.href = rootPrefix + 'assets/css/nav.css?v=2';
            document.head.appendChild(navLink);
        }

        // Nạp checkpoint-sync.js nếu chưa có
        if (!window.__MARUGOTO_CHECKPOINT_LOADED__ && !document.querySelector('script[src*="checkpoint-sync.js"]')) {
            const cpScript = document.createElement('script');
            cpScript.src = rootPrefix + 'assets/js/checkpoint-sync.js?v=3';
            cpScript.defer = true;
            document.head.appendChild(cpScript);
        }
        if (isLessons && !document.querySelector('script[src*="lesson-outline.js"]')) {
            const outlineCss = document.createElement('link');
            outlineCss.rel = 'stylesheet';
            outlineCss.href = rootPrefix + 'assets/css/lesson-outline.css?v=1';
            document.head.appendChild(outlineCss);
            const outlineScript = document.createElement('script');
            outlineScript.src = rootPrefix + 'assets/js/lesson-outline.js?v=1';
            document.head.appendChild(outlineScript);
        }
    })();

    // 4. TÍNH TOÁN TRẠNG THÁI ACTIVE
    const isHomeActive = (!isLessons && !isTests && (currentFileName === '' || currentFileName === 'index.html'));
    const isFormsActive = (!isLessons && !isTests && ['the_ru.html', 'the_ta.html', 'the_nai.html', 'tu_tha_dong_tu.html'].includes(currentFileName)) ||
                          (isTests && currentFileName === 'Luyen_Tap_The_Te_A2_1.html');
    const isKanjiActive = (!isLessons && !isTests && currentFileName === 'kanji_a2.html');
    const isVocabActive = (!isLessons && !isTests && currentFileName === 'Tu_Vung_Marugoto_A1_16_A2_1_10.html');
    const isGrammarActive = (!isLessons && !isTests && (currentFileName === 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html' || currentFileName === 'kien_thuc_bo_sung.html'));
    const isTestsActive = isTests;
    const isLessonsActive = isLessons;
    const isKaiwaActive = (!isLessons && !isTests && currentFileName === 'Luyen_Kaiwa_5_Phut.html');
    const is3dActive = (!isLessons && !isTests && currentFileName === 'demo_3d.html');

    // 5. SINH HTML CHO CÁC MỤC DROPDOWN
    function renderDropdownItems(items, type) {
        return items.map(item => {
            let linkHref = '';
            if (item.isRootFile) {
                linkHref = `${rootPrefix}${item.file}`;
            } else if (item.isTestFile || type === 'test') {
                linkHref = `${testsPrefix}${item.file}`;
            } else if (item.isLessonFile || type === 'lesson') {
                linkHref = `${lessonsPrefix}${item.file}`;
            } else {
                linkHref = `${rootPrefix}${item.file}`;
            }

            const baseFile = (item.file || '').split('#')[0];
            let isCurrent = false;

            if (item.isRootFile) {
                isCurrent = !isLessons && !isTests && currentFileName === baseFile;
            } else if (item.isTestFile || type === 'test') {
                isCurrent = isTests && currentFileName === baseFile;
            } else if (item.isLessonFile || type === 'lesson') {
                isCurrent = isLessons && currentFileName === baseFile;
            } else {
                isCurrent = !isLessons && !isTests && (
                    currentFileName === baseFile ||
                    (baseFile === 'index.html' && (currentFileName === '' || currentFileName === 'index.html'))
                );
            }

            const tagText = isCurrent ? 'Đang mở' : (item.tag || '');
            const tagHtml = tagText ? `<span class="hub-drop-tag">${tagText}</span>` : '';
            const descHtml = item.desc ? `<span class="hub-drop-desc">${item.desc}</span>` : '';

            return `<a href="${linkHref}" class="hub-drop-link${isCurrent ? ' active' : ''}">
                <div class="hub-drop-info">
                    <span class="hub-drop-text">${item.title}</span>
                    ${descHtml}
                </div>
                ${tagHtml}
            </a>`;
        }).join('\n                ');
    }

    const formsDropdownHtml = renderDropdownItems(ALL_VERB_FORMS, 'form');
    const kanjiDropdownHtml = renderDropdownItems(ALL_KANJI_ITEMS, 'kanji');
    const vocabDropdownHtml = renderDropdownItems(ALL_VOCAB_ITEMS, 'vocab');
    const grammarDropdownHtml = renderDropdownItems(ALL_GRAMMAR_ITEMS, 'grammar');
    const testsDropdownHtml = renderDropdownItems(ALL_TESTS, 'test');

    function renderLessonLinks(list) {
        return list.map(l => {
            const isCurrent = isLessons && currentFileName === l.file;
            const tag = isCurrent ? 'Đang học' : (l.tag || '');
            const tagHtml = tag ? `<span class="hub-drop-tag">${tag}</span>` : '';
            const descHtml = l.desc ? `<span class="hub-drop-desc">${l.desc}</span>` : '';
            return `<a href="${lessonsPrefix}${l.file}" class="hub-drop-link${isCurrent ? ' active' : ''}">
                <div class="hub-drop-info">
                    <span class="hub-drop-text">${l.icon} ${l.title}</span>
                    ${descHtml}
                </div>
                ${tagHtml}
            </a>`;
        }).join('\n                ');
    }

    const a2_2Html = renderLessonLinks(ALL_LESSONS_A2_2);
    const a2_1Html = renderLessonLinks(ALL_LESSONS);

    const lessonsDropdownHtml = `
        <div class="hub-drop-group-wrap" style="width: 100%; margin-bottom: 10px;">
            <div class="hub-drop-group-title" style="display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 7px 12px; font-size: 0.8rem; font-weight: 800; color: #4338ca; text-transform: uppercase; letter-spacing: 0.04em; background: #eef2ff; border-radius: 8px; margin: 2px 0 8px 0; border-left: 3px solid #6366f1;">
                <span>🌸 Marugoto A2-2 (Sơ Cấp 2 Tập 2 - Mới)</span>
                <span style="font-size: 0.7rem; background: #6366f1; color: #fff; padding: 2px 8px; border-radius: 99px; white-space: nowrap; flex-shrink: 0;">Lịch 17/11</span>
            </div>
            <div class="hub-drop-grid-2col">
                ${a2_2Html}
            </div>
        </div>
        <div class="hub-drop-group-wrap" style="width: 100%;">
            <div class="hub-drop-group-title" style="padding: 7px 12px; font-size: 0.8rem; font-weight: 800; color: #475569; text-transform: uppercase; letter-spacing: 0.04em; background: #f1f5f9; border-radius: 8px; margin: 4px 0 8px 0; border-left: 3px solid #94a3b8;">
                📚 Marugoto A2-1 (Trọn Bộ 18 Bài Tập 1)
            </div>
            <div class="hub-drop-grid-2col">
                ${a2_1Html}
            </div>
        </div>
    `;

    // 6. TỔNG HỢP HTML TOÀN BỘ THANH NAVBAR VÀ BOTTOM SHEET/DROPDOWN
    const navbarHtml = `
    <div class="global-hub-nav-wrapper">
        <nav class="global-hub-nav" aria-label="Thanh điều hướng chính Marugoto">
            <!-- 0. Trang Chủ Pill -->
            <a href="${rootPrefix}index.html" id="hubBtnHome" class="hub-nav-item${isHomeActive ? ' active-hub' : ''}" title="Trang chủ học tập Marugoto">
                <span>🏠 Trang Chủ</span>
            </a>

            <!-- 1. Động Từ Dropdown -->
            <button type="button" id="hubBtnForms" class="hub-nav-item${isFormsActive ? ' active-hub' : ''}" onclick="window.toggleFormsDropdown(event)" aria-haspopup="dialog" aria-expanded="false" aria-controls="formsDropdownMenu">
                <span>🎴 Động Từ</span><span class="hub-chevron">▾</span>
            </button>
            
            <!-- 2. Kanji Dropdown -->
            <button type="button" id="hubBtnKanji" class="hub-nav-item${isKanjiActive ? ' active-hub' : ''}" onclick="window.toggleKanjiDropdown(event)" aria-haspopup="dialog" aria-expanded="false" aria-controls="kanjiDropdownMenu">
                <span>⛩️ Kanji</span><span class="hub-chevron">▾</span>
            </button>

            <!-- 3. Từ Vựng Dropdown -->
            <button type="button" id="hubBtnVocab" class="hub-nav-item${isVocabActive ? ' active-hub' : ''}" onclick="window.toggleVocabDropdown(event)" aria-haspopup="dialog" aria-expanded="false" aria-controls="vocabDropdownMenu">
                <span>📖 Từ Vựng</span><span class="hub-chevron">▾</span>
            </button>

            <!-- 4. Ngữ Pháp Dropdown -->
            <button type="button" id="hubBtnGrammar" class="hub-nav-item${isGrammarActive ? ' active-hub' : ''}" onclick="window.toggleGrammarDropdown(event)" aria-haspopup="dialog" aria-expanded="false" aria-controls="grammarDropdownMenu">
                <span>📗 Ngữ Pháp</span><span class="hub-chevron">▾</span>
            </button>

            <!-- 5. Đề Thi Dropdown -->
            <button type="button" id="hubBtnTests" class="hub-nav-item${isTestsActive ? ' active-hub' : ''}" onclick="window.toggleTestsDropdown(event)" aria-haspopup="dialog" aria-expanded="false" aria-controls="testsDropdownMenu">
                <span>🎯 Đề Thi</span><span class="hub-chevron">▾</span>
            </button>

            <!-- 5.5 Kaiwa 5P Direct Pill -->
            <a href="${rootPrefix}Luyen_Kaiwa_5_Phut.html" class="hub-nav-item${isKaiwaActive ? ' active-hub' : ''}" title="Phòng luyện phỏng vấn Kaiwa 5 phút 4 chủ đề cô giáo">
                <span>🎙️ Kaiwa 5P</span>
            </a>

            <!-- 6. Bài Học Dropdown -->
            <button type="button" id="hubBtnLessons" class="hub-nav-item${isLessonsActive ? ' active-hub' : ''}" onclick="window.toggleLessonsDropdown(event)" aria-haspopup="dialog" aria-expanded="false" aria-controls="lessonsDropdownMenu">
                <span>🚀 Bài Học</span><span class="hub-chevron">▾</span>
            </button>

            <!-- 7. Không Gian 3D Direct Pill -->
            <a href="${rootPrefix}demo_3d.html" class="hub-nav-item${is3dActive ? ' active-hub' : ''}" title="Khám phá phòng học không gian 3D tương tác">
                <span>⛩️ 3D Lab</span>
            </a>
        </nav>

        <!-- Lớp phủ mờ (Backdrop) cho Mobile và ngoài vùng click -->
        <div class="hub-backdrop" id="hubNavBackdrop" onclick="window.closeAllHubDropdowns()"></div>

        <!-- 1. Menu Các Thể Động Từ -->
        <div class="hub-dropdown-menu" id="formsDropdownMenu" role="dialog" aria-modal="true" aria-label="Menu Các Thể Động Từ">
            <div class="hub-sheet-handle"></div>
            <div class="hub-drop-header">
                <div class="hub-drop-header-left">
                    <span class="hub-drop-title">🎴 Các Thể Động Từ Marugoto</span>
                    <span class="hub-drop-subtitle">Quy tắc chia thể, thể ngắn & đấu trường phản xạ</span>
                </div>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${formsDropdownHtml}
            </div>
        </div>

        <!-- 2. Menu Kanji & Bút Thuận -->
        <div class="hub-dropdown-menu" id="kanjiDropdownMenu" role="dialog" aria-modal="true" aria-label="Menu Học Kanji">
            <div class="hub-sheet-handle"></div>
            <div class="hub-drop-header">
                <div class="hub-drop-header-left">
                    <span class="hub-drop-title">⛩️ Chữ Hán Kanji (Marugoto A2-1)</span>
                    <span class="hub-drop-subtitle">Flashcard, 8 quy tắc bút thuận, từ ghép & bài tập</span>
                </div>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${kanjiDropdownHtml}
            </div>
        </div>

        <!-- 3. Menu Kho Từ Vựng -->
        <div class="hub-dropdown-menu" id="vocabDropdownMenu" role="dialog" aria-modal="true" aria-label="Menu Kho Từ Vựng">
            <div class="hub-sheet-handle"></div>
            <div class="hub-drop-header">
                <div class="hub-drop-header-left">
                    <span class="hub-drop-title">📖 Kho Từ Vựng Toàn Diện A1-A2</span>
                    <span class="hub-drop-subtitle">Tra cứu 1000+ từ vựng, flashcard & trắc nghiệm</span>
                </div>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${vocabDropdownHtml}
            </div>
        </div>

        <!-- 4. Menu Ngữ Pháp & Kiến Thức Bổ Sung -->
        <div class="hub-dropdown-menu" id="grammarDropdownMenu" role="dialog" aria-modal="true" aria-label="Menu Ngữ Pháp">
            <div class="hub-sheet-handle"></div>
            <div class="hub-drop-header">
                <div class="hub-drop-header-left">
                    <span class="hub-drop-title">📗 Ngữ Pháp & Cẩm Nang Bổ Trợ</span>
                    <span class="hub-drop-subtitle">Tổng hợp mẫu câu cốt lõi, Verb Lab & giao tiếp</span>
                </div>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${grammarDropdownHtml}
            </div>
        </div>

        <!-- 5. Menu Ôn Tập & Đề Thi -->
        <div class="hub-dropdown-menu" id="testsDropdownMenu" role="dialog" aria-modal="true" aria-label="Menu Ôn Tập & Đề Thi">
            <div class="hub-sheet-handle"></div>
            <div class="hub-drop-header">
                <div class="hub-drop-header-left">
                    <span class="hub-drop-title">🎯 Ôn Tập & Đề Thi Thực Chiến</span>
                    <span class="hub-drop-subtitle">Đề thi Midterm, Mini test theo bài & đề thi thử</span>
                </div>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body">
                ${testsDropdownHtml}
            </div>
        </div>

        <!-- 6. Menu Web Bài Học -->
        <div class="hub-dropdown-menu menu-wide" id="lessonsDropdownMenu" role="dialog" aria-modal="true" aria-label="Menu Bài Học">
            <div class="hub-sheet-handle"></div>
            <div class="hub-drop-header">
                <div class="hub-drop-header-left">
                    <span class="hub-drop-title">🚀 Hệ Thống Bài Học Marugoto (A2-1 & A2-2)</span>
                    <span class="hub-drop-subtitle">Đầy đủ 18 bài A2-1 và các chuyên đề mới Marugoto A2-2</span>
                </div>
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

            // Tính tâm x mong muốn của dropdown
            const btnCenter = btnRect.left - wrapperRect.left + (btnRect.width / 2);
            const menuWidth = menu.offsetWidth || 340;
            const wrapperWidth = wrapperRect.width;

            // Giới hạn để dropdown không bao giờ bị tràn lề trái/phải màn hình
            const minCenter = (menuWidth / 2) + 10;
            const maxCenter = wrapperWidth - (menuWidth / 2) - 10;
            const clampedCenter = Math.max(minCenter, Math.min(btnCenter, maxCenter));

            menu.style.top = (btnRect.bottom - wrapperRect.top + 8) + 'px';
            menu.style.left = clampedCenter + 'px';
            menu.style.transform = 'translateX(-50%)';
        } else {
            menu.style.top = '';
            menu.style.left = '';
            menu.style.transform = '';
        }
    }

    const ALL_MENU_IDS = [
        'formsDropdownMenu',
        'kanjiDropdownMenu',
        'vocabDropdownMenu',
        'grammarDropdownMenu',
        'testsDropdownMenu',
        'lessonsDropdownMenu'
    ];

    const ALL_BTN_IDS = [
        'hubBtnForms',
        'hubBtnKanji',
        'hubBtnVocab',
        'hubBtnGrammar',
        'hubBtnTests',
        'hubBtnLessons'
    ];

    let lastFocusedBtn = null;

    function closeAllHubDropdowns(restoreFocus = true) {
        ALL_MENU_IDS.forEach(id => {
            const m = document.getElementById(id);
            if (m) m.classList.remove('show');
        });
        ALL_BTN_IDS.forEach(id => {
            const b = document.getElementById(id);
            if (b) b.setAttribute('aria-expanded', 'false');
        });
        const bd = document.getElementById('hubNavBackdrop');
        if (bd) bd.classList.remove('show');
        document.body.classList.remove('hub-menu-open');
        document.body.style.overflow = '';
        if (restoreFocus && lastFocusedBtn && typeof lastFocusedBtn.focus === 'function') {
            try { lastFocusedBtn.focus(); } catch (err) {}
            lastFocusedBtn = null;
        }
    }

    function toggleHubDropdown(menuId, btnId, e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const menu = document.getElementById(menuId);
        const btn = document.getElementById(btnId);
        const bd = document.getElementById('hubNavBackdrop');

        if (!menu) return;

        const willOpen = !menu.classList.contains('show');

        // Đóng các menu khác
        ALL_MENU_IDS.forEach(id => {
            if (id !== menuId) {
                const m = document.getElementById(id);
                if (m) m.classList.remove('show');
            }
        });
        ALL_BTN_IDS.forEach(id => {
            if (id !== btnId) {
                const b = document.getElementById(id);
                if (b) b.setAttribute('aria-expanded', 'false');
            }
        });

        if (willOpen) {
            lastFocusedBtn = btn;
            positionDesktopMenu(btn, menu);
            menu.classList.add('show');
            if (btn) btn.setAttribute('aria-expanded', 'true');
            if (bd) bd.classList.add('show');
            if (window.innerWidth <= 768) {
                document.body.classList.add('hub-menu-open');
                document.body.style.overflow = 'hidden';
            }
            const firstFocusable = menu.querySelector('.hub-drop-close, .hub-drop-link');
            if (firstFocusable && typeof firstFocusable.focus === 'function') {
                setTimeout(() => { try { firstFocusable.focus(); } catch(err){} }, 50);
            }
        } else {
            closeAllHubDropdowns(true);
        }
    }

    function toggleFormsDropdown(e) { toggleHubDropdown('formsDropdownMenu', 'hubBtnForms', e); }
    function toggleKanjiDropdown(e) { toggleHubDropdown('kanjiDropdownMenu', 'hubBtnKanji', e); }
    function toggleVocabDropdown(e) { toggleHubDropdown('vocabDropdownMenu', 'hubBtnVocab', e); }
    function toggleGrammarDropdown(e) { toggleHubDropdown('grammarDropdownMenu', 'hubBtnGrammar', e); }
    function toggleTestsDropdown(e) { toggleHubDropdown('testsDropdownMenu', 'hubBtnTests', e); }
    function toggleLessonsDropdown(e) { toggleHubDropdown('lessonsDropdownMenu', 'hubBtnLessons', e); }

    // Đóng dropdown khi click ra ngoài
    document.addEventListener('click', function (e) {
        if (!e || !e.target) return;
        if (e.target.closest && (
            e.target.closest('.hub-dropdown-menu') ||
            e.target.closest('.hub-nav-item')
        )) {
            return;
        }
        closeAllHubDropdowns();
    });

    // Đóng khi nhấn phím Escape và bẫy focus (Trap Focus) cho Modal
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            closeAllHubDropdowns(true);
            return;
        }
        if (e.key === 'Tab') {
            const openMenu = document.querySelector('.hub-dropdown-menu.show');
            if (!openMenu) return;
            const focusables = Array.from(openMenu.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')).filter(el => !el.disabled && el.offsetParent !== null);
            if (!focusables.length) return;
            const first = focusables[0];
            const last = focusables[focusables.length - 1];
            if (e.shiftKey && document.activeElement === first) {
                e.preventDefault();
                last.focus();
            } else if (!e.shiftKey && document.activeElement === last) {
                e.preventDefault();
                first.focus();
            }
        }
    });

    // Tự động căn chỉnh khi resize màn hình
    window.addEventListener('resize', function () {
        const mappings = [
            ['hubBtnForms', 'formsDropdownMenu'],
            ['hubBtnKanji', 'kanjiDropdownMenu'],
            ['hubBtnVocab', 'vocabDropdownMenu'],
            ['hubBtnGrammar', 'grammarDropdownMenu'],
            ['hubBtnTests', 'testsDropdownMenu'],
            ['hubBtnLessons', 'lessonsDropdownMenu']
        ];
        mappings.forEach(([btnId, menuId]) => {
            const m = document.getElementById(menuId);
            if (m && m.classList.contains('show')) {
                positionDesktopMenu(document.getElementById(btnId), m);
            }
        });
    });

    // Tự động cuộn căn giữa active tab trên thiết bị di động
    function scrollToActiveNav() {
        if (window.innerWidth <= 768) {
            const nav = document.querySelector('.global-hub-nav');
            const active = nav ? nav.querySelector('.active-hub') : null;
            if (nav && active) {
                setTimeout(() => {
                    const navRect = nav.getBoundingClientRect();
                    const activeRect = active.getBoundingClientRect();
                    const scrollLeft = active.offsetLeft - (navRect.width / 2) + (activeRect.width / 2);
                    nav.scrollTo({ left: Math.max(0, scrollLeft), behavior: 'smooth' });
                }, 80);
            }
        }
    }

    // Phơi ra global để các script khác và inline onclick gọi được
    window.toggleFormsDropdown = toggleFormsDropdown;
    window.toggleKanjiDropdown = toggleKanjiDropdown;
    window.toggleVocabDropdown = toggleVocabDropdown;
    window.toggleGrammarDropdown = toggleGrammarDropdown;
    window.toggleTestsDropdown = toggleTestsDropdown;
    window.toggleLessonsDropdown = toggleLessonsDropdown;
    window.closeAllHubDropdowns = closeAllHubDropdowns;

    // 8. RENDER VÀO DOM
    function renderNavbar() {
        const placeholder = document.getElementById('navbar-placeholder');
        if (placeholder) {
            placeholder.innerHTML = navbarHtml;
            scrollToActiveNav();
            return;
        }

        const existingWrapper = document.querySelector('.global-hub-nav-wrapper');
        if (existingWrapper) {
            const temp = document.createElement('div');
            temp.innerHTML = navbarHtml;
            existingWrapper.parentNode.replaceChild(temp.firstElementChild, existingWrapper);
            scrollToActiveNav();
            return;
        }

        const existingNav = document.querySelector('.global-hub-nav');
        if (existingNav) {
            const temp = document.createElement('div');
            temp.innerHTML = navbarHtml;
            const newNav = temp.firstElementChild;
            existingNav.parentNode.replaceChild(newNav, existingNav);
            scrollToActiveNav();
            return;
        }

        // Chèn vào đầu container hoặc đầu body nếu chưa có placeholder
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
        scrollToActiveNav();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', renderNavbar);
    } else {
        renderNavbar();
    }
})();
