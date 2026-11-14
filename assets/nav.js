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
        { file: 'index.html', title: '🌸 Thể TE (～て)', desc: 'Cẩm nang & Bảng luyện tập chia thể TE (56 từ)', tag: 'Cốt lõi' },
        { file: 'the_ru.html', title: '📘 Thể RU (Từ Điển)', desc: 'Thể nguyên mẫu Từ điển & Quy tắc chia Jisho', tag: 'Jisho' },
        { file: 'the_ta.html', title: '📕 Thể TA (Quá Khứ)', desc: 'Thể quá khứ ngắn Ta-kei & Mẫu câu kinh nghiệm', tag: 'Ta-kei' },
        { file: 'the_nai.html', title: '📗 Thể NAI (Phủ Định)', desc: 'Thể phủ định ngắn Nai-kei & Mẫu câu khuyên cấm', tag: 'Nai-kei' },
        { file: 'Luyen_Tap_The_Te_A2_1.html', title: '⚡ Đấu Trường Luyện Thể TE', desc: 'Mini test phản xạ chia thể TE tốc độ cao', isTestFile: true, tag: 'Đấu trường' },
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

    // 3. ĐẢM BẢO CSS SITE-THEME & CHECKPOINT SYNC & NAV STYLES ĐƯỢC NẠP
    (function injectStyles() {
        // Nạp site-theme.css nếu chưa có
        const existingLink = document.querySelector('link[href*="site-theme.css"]');
        if (!existingLink) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = rootPrefix + 'assets/css/site-theme.css?v=6';
            document.head.appendChild(link);
        }

        // Nạp checkpoint-sync.js nếu chưa có
        if (!window.__MARUGOTO_CHECKPOINT_LOADED__ && !document.querySelector('script[src*="checkpoint-sync.js"]')) {
            const cpScript = document.createElement('script');
            cpScript.src = rootPrefix + 'assets/js/checkpoint-sync.js?v=1';
            cpScript.defer = true;
            document.head.appendChild(cpScript);
        }

        // Nạp dedicated style cho navbar capsule glassmorphic (chống bị đè bởi legacy page css)
        if (!document.getElementById('mrg-global-nav-styles')) {
            const style = document.createElement('style');
            style.id = 'mrg-global-nav-styles';
            style.textContent = `
                /* ==========================================================
                   MRG GLOBAL NAVBAR CAPSULE & DROPDOWN DESIGN SYSTEM
                   ========================================================== */
                html body #navbar-placeholder {
                    position: sticky !important;
                    top: 10px !important;
                    z-index: 999999 !important;
                    display: block !important;
                }

                html body .global-hub-nav-wrapper {
                    position: sticky !important;
                    top: 10px !important;
                    z-index: 999999 !important;
                    width: 100% !important;
                    max-width: 1200px !important;
                    margin: 0 auto 20px auto !important;
                    padding: 0 12px !important;
                    box-sizing: border-box !important;
                    pointer-events: none !important;
                    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
                }

                html body .global-hub-nav {
                    pointer-events: auto !important;
                    display: flex !important;
                    align-items: center !important;
                    justify-content: center !important;
                    flex-wrap: nowrap !important;
                    gap: 6px !important;
                    background: rgba(255, 255, 255, 0.86) !important;
                    backdrop-filter: blur(20px) saturate(180%) !important;
                    -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
                    border: 1px solid rgba(226, 232, 240, 0.9) !important;
                    border-radius: 9999px !important;
                    padding: 6px 10px !important;
                    box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.08),
                                0 4px 12px -2px rgba(15, 23, 42, 0.04),
                                inset 0 1px 0 rgba(255, 255, 255, 0.95) !important;
                    position: relative !important;
                    margin: 0 auto !important;
                    width: fit-content !important;
                    max-width: 100% !important;
                    box-sizing: border-box !important;
                    overflow: visible !important;
                }

                html body .hub-nav-item {
                    display: inline-flex !important;
                    align-items: center !important;
                    justify-content: center !important;
                    gap: 5px !important;
                    padding: 8px 14px !important;
                    min-height: 38px !important;
                    border-radius: 9999px !important;
                    background: transparent !important;
                    color: #334155 !important;
                    font-size: 0.86rem !important;
                    font-weight: 700 !important;
                    line-height: 1.4 !important;
                    text-decoration: none !important;
                    border: 1px solid transparent !important;
                    box-shadow: none !important;
                    cursor: pointer !important;
                    font-family: inherit !important;
                    white-space: nowrap !important;
                    flex-shrink: 0 !important;
                    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
                    -webkit-tap-highlight-color: transparent !important;
                    user-select: none !important;
                    outline: none !important;
                }

                html body .hub-nav-item:hover {
                    background: rgba(241, 245, 249, 0.9) !important;
                    color: #e11d48 !important;
                    border-color: rgba(225, 29, 72, 0.2) !important;
                    transform: translateY(-1.5px) !important;
                    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06) !important;
                }

                html body .hub-nav-item:active {
                    transform: translateY(0.5px) scale(0.98) !important;
                    transition-duration: 0.08s !important;
                }

                html body .hub-nav-item:focus-visible {
                    box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.3) !important;
                }

                html body .hub-nav-item.active-hub {
                    background: linear-gradient(135deg, #e11d48 0%, #be123c 100%) !important;
                    color: #ffffff !important;
                    border-color: rgba(225, 29, 72, 0.85) !important;
                    box-shadow: 0 4px 16px rgba(225, 29, 72, 0.38),
                                inset 0 1px 0 rgba(255, 255, 255, 0.25) !important;
                    font-weight: 800 !important;
                }

                html body .hub-nav-item.active-hub:hover {
                    background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%) !important;
                    color: #ffffff !important;
                    transform: translateY(-1px) !important;
                    box-shadow: 0 6px 20px rgba(225, 29, 72, 0.45) !important;
                }

                html body .hub-chevron {
                    display: inline-block !important;
                    font-size: 0.68rem !important;
                    margin-left: 2px !important;
                    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
                    opacity: 0.75 !important;
                }

                html body .hub-nav-item.active-hub .hub-chevron {
                    opacity: 0.95 !important;
                }

                html body .hub-nav-item[aria-expanded="true"] .hub-chevron {
                    transform: rotate(180deg) !important;
                }

                /* --- Dropdown Menus (Desktop Floating Card) --- */
                html body .hub-dropdown-menu {
                    display: none;
                    position: absolute !important;
                    background: rgba(255, 255, 255, 0.97) !important;
                    backdrop-filter: blur(24px) saturate(180%) !important;
                    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
                    border: 1px solid rgba(226, 232, 240, 0.9) !important;
                    border-radius: 20px !important;
                    box-shadow: 0 20px 45px -10px rgba(15, 23, 42, 0.16),
                                0 8px 18px -4px rgba(15, 23, 42, 0.06),
                                inset 0 1px 0 rgba(255, 255, 255, 0.8) !important;
                    padding: 12px !important;
                    min-width: 330px !important;
                    max-width: 480px !important;
                    max-height: 520px !important;
                    overflow-y: auto !important;
                    scrollbar-width: thin !important;
                    scrollbar-color: #cbd5e1 transparent !important;
                    z-index: 1000000 !important;
                    pointer-events: auto !important;
                    box-sizing: border-box !important;
                }

                html body .hub-dropdown-menu.menu-wide {
                    min-width: 580px !important;
                    max-width: 680px !important;
                }

                html body .hub-dropdown-menu.show {
                    display: block !important;
                    animation: hubDropDesktopIn 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
                }

                @keyframes hubDropDesktopIn {
                    from {
                        opacity: 0;
                        transform: translate(-50%, -10px) scale(0.97);
                    }
                    to {
                        opacity: 1;
                        transform: translate(-50%, 0) scale(1);
                    }
                }

                html body .hub-sheet-handle {
                    display: none !important;
                }

                html body .hub-drop-header {
                    display: flex !important;
                    align-items: center !important;
                    justify-content: space-between !important;
                    padding: 8px 10px 10px 10px !important;
                    margin-bottom: 6px !important;
                    border-bottom: 1px solid #f1f5f9 !important;
                }

                html body .hub-drop-header-left {
                    display: flex !important;
                    flex-direction: column !important;
                    gap: 2px !important;
                    text-align: left !important;
                }

                html body .hub-drop-title {
                    font-size: 0.95rem !important;
                    font-weight: 800 !important;
                    color: #0f172a !important;
                    letter-spacing: -0.2px !important;
                }

                html body .hub-drop-subtitle {
                    font-size: 0.74rem !important;
                    font-weight: 500 !important;
                    color: #64748b !important;
                }

                html body .hub-drop-close {
                    display: none !important;
                    width: 32px !important;
                    height: 32px !important;
                    border-radius: 50% !important;
                    border: 1px solid #e2e8f0 !important;
                    background: #f8fafc !important;
                    color: #475569 !important;
                    font-size: 1rem !important;
                    cursor: pointer !important;
                    align-items: center !important;
                    justify-content: center !important;
                    transition: all 0.15s ease !important;
                }

                html body .hub-drop-close:hover {
                    background: #e2e8f0 !important;
                    color: #0f172a !important;
                }

                html body .hub-drop-body {
                    display: flex !important;
                    flex-direction: column !important;
                    gap: 5px !important;
                }

                html body .hub-drop-grid-2col {
                    display: grid !important;
                    grid-template-columns: repeat(2, 1fr) !important;
                    gap: 6px !important;
                }

                html body .hub-drop-link {
                    display: flex !important;
                    align-items: center !important;
                    justify-content: space-between !important;
                    padding: 9px 12px !important;
                    color: #1e293b !important;
                    font-size: 0.86rem !important;
                    font-weight: 600 !important;
                    line-height: 1.35 !important;
                    text-decoration: none !important;
                    border-radius: 12px !important;
                    border: 1px solid transparent !important;
                    background: transparent !important;
                    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1) !important;
                    gap: 12px !important;
                    box-sizing: border-box !important;
                }

                html body .hub-drop-link:hover {
                    background: #fff1f2 !important;
                    color: #e11d48 !important;
                    border-color: rgba(225, 29, 72, 0.15) !important;
                    transform: translateX(3px) !important;
                }

                html body .hub-drop-link.active {
                    background: linear-gradient(135deg, #e11d48 0%, #be123c 100%) !important;
                    color: #ffffff !important;
                    box-shadow: 0 4px 14px rgba(225, 29, 72, 0.28) !important;
                }

                html body .hub-drop-info {
                    display: flex !important;
                    flex-direction: column !important;
                    gap: 2px !important;
                    text-align: left !important;
                    flex: 1 !important;
                }

                html body .hub-drop-text {
                    font-weight: 750 !important;
                    color: inherit !important;
                    font-size: 0.88rem !important;
                }

                html body .hub-drop-desc {
                    font-size: 0.74rem !important;
                    font-weight: 500 !important;
                    color: #64748b !important;
                    line-height: 1.3 !important;
                }

                html body .hub-drop-link:hover .hub-drop-desc {
                    color: #be123c !important;
                    opacity: 0.9 !important;
                }

                html body .hub-drop-link.active .hub-drop-desc {
                    color: rgba(255, 255, 255, 0.88) !important;
                }

                html body .hub-drop-tag {
                    font-size: 0.7rem !important;
                    font-weight: 750 !important;
                    padding: 3px 8px !important;
                    border-radius: 9999px !important;
                    background: #f1f5f9 !important;
                    color: #475569 !important;
                    white-space: nowrap !important;
                    flex-shrink: 0 !important;
                }

                html body .hub-drop-link:hover .hub-drop-tag {
                    background: rgba(225, 29, 72, 0.12) !important;
                    color: #be123c !important;
                }

                html body .hub-drop-link.active .hub-drop-tag {
                    background: rgba(255, 255, 255, 0.25) !important;
                    color: #ffffff !important;
                }

                html body .hub-backdrop {
                    display: none;
                    position: fixed !important;
                    top: 0 !important;
                    left: 0 !important;
                    right: 0 !important;
                    bottom: 0 !important;
                    width: 100vw !important;
                    height: 100vh !important;
                    background: rgba(15, 23, 42, 0.5) !important;
                    backdrop-filter: blur(6px) !important;
                    -webkit-backdrop-filter: blur(6px) !important;
                    z-index: 999998 !important;
                    opacity: 0;
                    transition: opacity 0.25s ease !important;
                    pointer-events: auto !important;
                }

                html body .hub-backdrop.show {
                    display: block !important;
                    opacity: 1 !important;
                }

                /* --- Mobile Responsiveness (< 768px) --- */
                @media (max-width: 768px) {
                    html body .global-hub-nav-wrapper {
                        top: 6px !important;
                        margin-bottom: 14px !important;
                        padding: 0 8px !important;
                    }

                    html body .global-hub-nav {
                        width: 100% !important;
                        display: flex !important;
                        flex-wrap: nowrap !important;
                        overflow-x: auto !important;
                        white-space: nowrap !important;
                        padding: 6px 8px !important;
                        -webkit-overflow-scrolling: touch !important;
                        scrollbar-width: none !important;
                        gap: 5px !important;
                        border-radius: 9999px !important;
                        justify-content: flex-start !important;
                    }

                    html body .global-hub-nav::-webkit-scrollbar {
                        display: none !important;
                    }

                    html body .hub-nav-item {
                        padding: 7px 12px !important;
                        font-size: 0.82rem !important;
                        min-height: 36px !important;
                        line-height: 1.4 !important;
                        border-radius: 9999px !important;
                    }

                    html body .hub-dropdown-menu {
                        position: fixed !important;
                        bottom: 0 !important;
                        left: 0 !important;
                        right: 0 !important;
                        top: auto !important;
                        transform: translateY(100%) !important;
                        max-height: 82vh !important;
                        width: 100% !important;
                        max-width: 100% !important;
                        border-radius: 24px 24px 0 0 !important;
                        box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.35) !important;
                        background: #ffffff !important;
                        border: none !important;
                        border-top: 1px solid #e2e8f0 !important;
                        z-index: 9999999 !important;
                        display: flex !important;
                        flex-direction: column !important;
                        padding: 0 0 max(16px, env(safe-area-inset-bottom)) 0 !important;
                        transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1) !important;
                        visibility: hidden !important;
                        animation: none !important;
                        overscroll-behavior: contain !important;
                    }

                    html body .hub-dropdown-menu.menu-wide {
                        min-width: 100% !important;
                        max-width: 100% !important;
                    }

                    html body .hub-dropdown-menu.show {
                        transform: translateY(0) !important;
                        visibility: visible !important;
                    }

                    html body .hub-sheet-handle {
                        display: block !important;
                        width: 40px !important;
                        height: 5px !important;
                        border-radius: 9999px !important;
                        background: #cbd5e1 !important;
                        margin: 10px auto 4px auto !important;
                        flex-shrink: 0 !important;
                    }

                    html body .hub-drop-header {
                        display: flex !important;
                        align-items: center !important;
                        justify-content: space-between !important;
                        padding: 12px 18px !important;
                        border-bottom: 1px solid #f1f5f9 !important;
                        position: sticky !important;
                        top: 0 !important;
                        background: #ffffff !important;
                        z-index: 10 !important;
                        border-radius: 24px 24px 0 0 !important;
                    }

                    html body .hub-drop-close {
                        display: flex !important;
                    }

                    html body .hub-drop-body {
                        padding: 10px 14px !important;
                        overflow-y: auto !important;
                        -webkit-overflow-scrolling: touch !important;
                        gap: 6px !important;
                    }

                    html body .hub-drop-grid-2col {
                        grid-template-columns: 1fr !important;
                    }

                    html body .hub-drop-link {
                        padding: 11px 14px !important;
                        border-radius: 14px !important;
                        background: #f8fafc !important;
                    }

                    html body .hub-drop-link:active {
                        transform: scale(0.98) !important;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    })();

    // 4. TÍNH TOÁN TRẠNG THÁI ACTIVE
    const isFormsActive = (!isLessons && !isTests && ['index.html', '', 'the_ru.html', 'the_ta.html', 'the_nai.html'].includes(currentFileName)) ||
                          (isTests && currentFileName === 'Luyen_Tap_The_Te_A2_1.html');
    const isKanjiActive = (!isLessons && !isTests && currentFileName === 'kanji_a2.html');
    const isVocabActive = (!isLessons && !isTests && currentFileName === 'Tu_Vung_Marugoto_A1_16_A2_1_10.html');
    const isGrammarActive = (!isLessons && !isTests && (currentFileName === 'Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html' || currentFileName === 'kien_thuc_bo_sung.html'));
    const isTestsActive = isTests;
    const isLessonsActive = isLessons;
    const is3dActive = (!isLessons && !isTests && currentFileName === 'demo_3d.html');

    // 5. SINH HTML CHO CÁC MỤC DROPDOWN
    function renderDropdownItems(items, type) {
        return items.map(item => {
            let linkHref = '';
            if (item.isTestFile || type === 'test') {
                linkHref = `${testsPrefix}${item.file}`;
            } else if (item.isLessonFile || type === 'lesson') {
                linkHref = `${lessonsPrefix}${item.file}`;
            } else {
                linkHref = `${rootPrefix}${item.file}`;
            }

            const baseFile = (item.file || '').split('#')[0];
            let isCurrent = false;

            if (item.isTestFile || type === 'test') {
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

    const lessonsDropdownHtml = ALL_LESSONS.map(l => {
        const isCurrent = isLessons && currentFileName === l.file;
        return `<a href="${lessonsPrefix}${l.file}" class="hub-drop-link${isCurrent ? ' active' : ''}">
            <div class="hub-drop-info">
                <span class="hub-drop-text">${l.icon} ${l.title}</span>
            </div>
            ${isCurrent ? '<span class="hub-drop-tag">Đang học</span>' : ''}
        </a>`;
    }).join('\n                ');

    // 6. TỔNG HỢP HTML TOÀN BỘ THANH NAVBAR VÀ BOTTOM SHEET/DROPDOWN
    const navbarHtml = `
    <div class="global-hub-nav-wrapper">
        <nav class="global-hub-nav" aria-label="Thanh điều hướng chính Marugoto">
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
                    <span class="hub-drop-title">🚀 Toàn Bộ Bài Học Marugoto A2-1 (18 Bài)</span>
                    <span class="hub-drop-subtitle">Trọn bộ 18 chủ đề từ vựng, hội thoại & ngữ cảnh thực tế</span>
                </div>
                <button type="button" class="hub-drop-close" onclick="window.closeAllHubDropdowns()" aria-label="Đóng">✕</button>
            </div>
            <div class="hub-drop-body hub-drop-grid-2col">
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

    function closeAllHubDropdowns() {
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
            positionDesktopMenu(btn, menu);
            menu.classList.add('show');
            if (btn) btn.setAttribute('aria-expanded', 'true');
            if (bd) bd.classList.add('show');
            if (window.innerWidth <= 768) {
                document.body.classList.add('hub-menu-open');
                document.body.style.overflow = 'hidden';
            }
        } else {
            menu.classList.remove('show');
            if (btn) btn.setAttribute('aria-expanded', 'false');
            if (bd) bd.classList.remove('show');
            document.body.classList.remove('hub-menu-open');
            document.body.style.overflow = '';
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

    // Đóng khi nhấn phím Escape
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            closeAllHubDropdowns();
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
