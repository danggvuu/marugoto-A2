/**
 * MACOS-STYLE COMPACT FLOATING SECTION RAIL, KEYBOARD SHORTCUTS & SMART LESSON SUITE
 * (assets/js/lesson-sidebar-rail.js)
 * 
 * 1. Bố cục bài học CĂN GIỮA HOÀN HẢO 100% - Không di dời DOM gây lệch trang
 * 2. Cố định nổi bên cạnh (position: fixed), tự động bám theo cuộn trang (Sticky ScrollSpy)
 * 3. Đồng bộ trạng thái active hai chiều giữa thanh capsule trên và thanh rail bên cạnh
 * 4. Hỗ trợ thu gọn/mở rộng, ghi nhớ trạng thái bằng localStorage
 * 5. Bộ phím tắt học thần tốc: J/K (lướt mục), 1-4 (chọn trắc nghiệm), Space/A (lật/nghe từ vựng)
 * 6. Cụm điều hướng Bài trước/Bài tiếp theo ở cuối trang kèm prefetch siêu tốc
 * 7. Tự động ghi nhớ vị trí đang học dở và cuộn êm ái khi mở lại
 */
(function () {
    'use strict';

    // Danh mục chuẩn 36 bài học phục vụ chuyển bài và prefetch
    const A2_1_LESSONS = [
        { file: 'Marugoto_A2_Lesson_1.html', num: '01', title: 'Bài 1: Nơi ở & Gia đình', icon: '🌸', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_2.html', num: '02', title: 'Bài 2: Sở thích & Ngôn ngữ', icon: '🎨', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_3.html', num: '03', title: 'Bài 3: Mùa & Khí hậu', icon: '🍁', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_4.html', num: '04', title: 'Bài 4: Thời tiết & Dự báo', icon: '⛅', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_5.html', num: '05', title: 'Bài 5: Phố xá & Nơi chốn', icon: '🏙️', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_6.html', num: '06', title: 'Bài 6: Chỉ đường & Ngã rẽ', icon: '🗺️', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_7.html', num: '07', title: 'Bài 7: Hẹn gặp & Giờ giấc', icon: '⏰', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_8.html', num: '08', title: 'Bài 8: Sự kiện & Mời mọc', icon: '⛩️', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_9.html', num: '09', title: 'Bài 9: Học tập & Phát âm', icon: '🗣️', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_10.html', num: '10', title: 'Bài 10: Ngoại ngữ & Văn hóa', icon: '🌟', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_11.html', num: '11', title: 'Bài 11: Dã ngoại & Ăn uống', icon: '🍱', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_12.html', num: '12', title: 'Bài 12: Món ăn ngày đặc biệt', icon: '🍜', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_13.html', num: '13', title: 'Bài 13: Đi công tác & Gặp gỡ', icon: '✈️', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_14.html', num: '14', title: 'Bài 14: Quy tắc nơi làm việc', icon: '💻', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_15.html', num: '15', title: 'Bài 15: Sức khỏe & Thể dục', icon: '🏥', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_16.html', num: '16', title: 'Bài 16: Tập luyện & Vận động', icon: '🏃', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_17.html', num: '17', title: 'Bài 17: Quà tặng & Kỷ niệm', icon: '🎁', level: 'A2-1' },
        { file: 'Marugoto_A2_Lesson_18.html', num: '18', title: 'Bài 18: Tiệc tùng & Sự kiện', icon: '👘', level: 'A2-1' }
    ];

    const A2_2_LESSONS = [
        { file: 'Marugoto_A2_2_Lesson_1.html', num: '01', title: 'Bài 1: Tên gọi', icon: '🌸', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_2.html', num: '02', title: 'Bài 2: Miêu tả người', icon: '👓', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_3.html', num: '03', title: 'Bài 3: Món ăn gợi ý', icon: '🍲', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_4.html', num: '04', title: 'Bài 4: Cách ăn', icon: '🥢', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_5.html', num: '05', title: 'Bài 5: Đi du lịch', icon: '✈️', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_6.html', num: '06', title: 'Bài 6: Hoạt động trải nghiệm', icon: '📸', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_7.html', num: '07', title: 'Bài 7: Lên kế hoạch trời mưa', icon: '🌧️', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_8.html', num: '08', title: 'Bài 8: Tham gia sự kiện', icon: '🎫', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_9.html', num: '09', title: 'Bài 9: Hướng dẫn đường đi', icon: '🗺️', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_10.html', num: '10', title: 'Bài 10: Giúp đỡ & Chỉ dẫn', icon: '🧭', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_11.html', num: '11', title: 'Bài 11: Đổi hàng & Trả đồ', icon: '🛍️', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_12.html', num: '12', title: 'Bài 12: Mua sắm & Hỏi giá', icon: '🛒', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_13.html', num: '13', title: 'Bài 13: Đồ vật quan trọng', icon: '⌚', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_14.html', num: '14', title: 'Bài 14: Kể về đồ vật yêu thích', icon: '📷', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_15.html', num: '15', title: 'Bài 15: Văn hóa trà đạo & Thư pháp', icon: '🍵', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_16.html', num: '16', title: 'Bài 16: Thử trải nghiệm truyền thống', icon: '👘', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_17.html', num: '17', title: 'Bài 17: Cuộc sống & Thói quen', icon: '🏠', level: 'A2-2' },
        { file: 'Marugoto_A2_2_Lesson_18.html', num: '18', title: 'Bài 18: Lời chúc & Tương lai', icon: '🎆', level: 'A2-2' }
    ];

    const ALL_LESSONS = [...A2_1_LESSONS, ...A2_2_LESSONS];

    function getCurrentFileName() {
        let name = window.location.pathname.split('/').pop() || 'index.html';
        return name.split('#')[0].split('?')[0];
    }

    function initLessonSidebarRail() {
        if (document.getElementById('lessonSidebarRail')) return;

        const mainContainer = document.querySelector('.main-container');
        if (!mainContainer) return;

        const sectionNav = mainContainer.querySelector('.section-nav');
        if (!sectionNav) return;

        const originalLinks = Array.from(sectionNav.querySelectorAll('a[href^="#sec-"]'));
        if (originalLinks.length < 2) return;

        document.body.classList.add('has-lesson-rail');
        const currentFileName = getCurrentFileName();

        // 1. Phân tích các mục điều hướng với nhãn ngắn gọn, đẹp mắt
        const railItems = originalLinks.map((link, idx) => {
            const href = link.getAttribute('href');
            const rawText = link.textContent.trim();
            const targetEl = document.querySelector(href);

            let icon = '●';
            let label = rawText;

            // Nhận diện chuẩn hóa nhãn theo ngữ cảnh học tập
            if (href === '#sec-grammar1') {
                icon = '①';
                label = 'Ngữ Pháp 1';
            } else if (href === '#sec-grammar2') {
                icon = '②';
                label = 'Ngữ Pháp 2';
            } else if (href === '#sec-grammar3') {
                icon = '③';
                label = 'Ngữ Pháp 3';
            } else if (href === '#sec-grammar4') {
                icon = '④';
                label = 'Ngữ Pháp 4';
            } else if (href === '#sec-grammar5') {
                icon = '⑤';
                label = 'Ngữ Pháp 5';
            } else if (href === '#sec-verb-lab') {
                icon = '🔬';
                label = 'Biến Thể ĐT';
            } else if (href === '#sec-vocab') {
                icon = '🎴';
                label = 'Từ Vựng 3D';
            } else if (href === '#sec-typing-practice') {
                icon = '⌨️';
                label = 'Luyện Gõ';
            } else if (href === '#sec-kanji') {
                icon = '⛩️';
                label = 'Chữ Hán';
            } else if (href === '#sec-quiz') {
                icon = '📝';
                label = 'Mini Test';
            } else if (href === '#sec-dialogue') {
                icon = '💬';
                label = 'Hội Thoại';
            } else {
                const iconRegex = /^([①-⑳0-9\.\-\u{1F000}-\u{1FAFF}\u{2300}-\u{27BF}\u{FE00}-\u{FE0F}]+)\s*(.*)$/u;
                const match = rawText.match(iconRegex);
                if (match && match[1].trim()) {
                    icon = match[1].trim();
                    label = match[2].trim();
                }
                label = label
                    .replace(/^Biến Thể Động Từ.*$/i, 'Biến Thể ĐT')
                    .replace(/^Luyện Gõ.*$/i, 'Luyện Gõ')
                    .replace(/^\d+\s*Từ Vựng.*$/i, 'Từ Vựng 3D')
                    .replace(/^\d+\s*Flashcard.*$/i, 'Từ Vựng 3D')
                    .replace(/^\d+\s*Chữ Hán.*$/i, 'Chữ Hán')
                    .replace(/^\d+\s*Từ Kanji.*$/i, 'Chữ Hán')
                    .replace(/^Mini Test.*$/i, 'Mini Test');
            }

            return { href, targetEl, icon, label, fullTitle: rawText };
        }).filter(item => item.targetEl !== null);

        if (railItems.length === 0) return;

        // 2. Tạo thanh sidebar macOS nổi fixed bên cạnh (Right Dock kiểu 1MS Taekwondo)
        const rail = document.createElement('aside');
        rail.id = 'lessonSidebarRail';
        rail.className = 'lesson-sidebar-rail';
        rail.setAttribute('aria-label', 'Mục lục bài học');

        rail.innerHTML = `
            <div class="macos-sidebar-box">
                <div class="macos-sidebar-header">
                    <div class="macos-traffic-dots" aria-hidden="true">
                        <span class="macos-dot macos-dot-red"></span>
                        <span class="macos-dot macos-dot-yellow"></span>
                        <span class="macos-dot macos-dot-green"></span>
                    </div>
                </div>

                <!-- Nút cuộn về đầu trang tròn kèm vòng tròn tiến độ cuộn SVG -->
                <div class="dock-progress-wrapper" title="Cuộn lên đầu trang">
                    <svg class="dock-progress-svg" viewBox="0 0 48 48">
                        <circle class="dock-progress-bg" cx="24" cy="24" r="20"></circle>
                        <circle class="dock-progress-bar" id="dockProgressBar" cx="24" cy="24" r="20"></circle>
                    </svg>
                    <button type="button" class="dock-btn-top" id="railBtnScrollTop" aria-label="Cuộn lên đầu trang">
                        <span>↑</span>
                    </button>
                </div>

                <nav class="lesson-rail-links" aria-label="Các phần trong bài">
                    ${railItems.map((item, idx) => `
                        <a href="${item.href}" class="lesson-rail-link ${idx === 0 ? 'active' : ''}" data-href="${item.href}" title="${item.fullTitle} (${item.label})">
                            <span class="rail-icon">${item.icon}</span>
                            <span class="rail-label">${item.label}</span>
                        </a>
                    `).join('')}
                </nav>

                <div class="macos-sidebar-footer">
                    <button type="button" class="dock-btn-shortcut" id="railBtnShortcuts" title="Xem bảng phím tắt học thần tốc (phím ?)">
                        <span>⌨️</span>
                    </button>
                </div>
            </div>
        `;

        document.body.appendChild(rail);

        // Tạo phần tử morphing glider lướt mượt mà giữa Top Capsule và Right Dock
        let glider = document.getElementById('lessonMorphGlider');
        if (!glider) {
            glider = document.createElement('div');
            glider.id = 'lessonMorphGlider';
            glider.className = 'lesson-morph-glider';
            glider.setAttribute('aria-hidden', 'true');
            document.body.appendChild(glider);
        }

        const macosBox = rail.querySelector('.macos-sidebar-box');
        const railLinks = Array.from(rail.querySelectorAll('.lesson-rail-link'));

        // Cài đặt độ trễ xuất hiện tầng bậc (stagger) cho các mục trên thanh dock
        railLinks.forEach((link, idx) => {
            link.style.transitionDelay = `${0.06 + idx * 0.035}s`;
        });
        const headerDots = rail.querySelector('.macos-sidebar-header');
        if (headerDots) headerDots.style.transitionDelay = '0.02s';
        const progressWrap = rail.querySelector('.dock-progress-wrapper');
        if (progressWrap) progressWrap.style.transitionDelay = '0.04s';
        const footerBtn = rail.querySelector('.macos-sidebar-footer');
        if (footerBtn) footerBtn.style.transitionDelay = `${0.06 + railLinks.length * 0.035}s`;

        // 3. Khôi phục trạng thái thu gọn từ localStorage
        const isCollapsedSaved = localStorage.getItem('marugoto_rail_collapsed') === 'true';
        if (isCollapsedSaved) {
            rail.classList.add('is-collapsed');
            document.body.classList.add('rail-collapsed');
        }

        // Sự kiện nút thu gọn / mở rộng (nút riêng hoặc chấm đỏ macOS)
        const toggleBtn = rail.querySelector('#btnToggleSidebarRail') || rail.querySelector('.macos-dot-red');
        if (toggleBtn) {
            toggleBtn.style.cursor = 'pointer';
            toggleBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const isCollapsed = rail.classList.toggle('is-collapsed');
                document.body.classList.toggle('rail-collapsed', isCollapsed);
                localStorage.setItem('marugoto_rail_collapsed', String(isCollapsed));
            });
        }

        // Tự động mở rộng khi hover trên laptop nếu đang thu gọn
        rail.addEventListener('mouseenter', () => {
            if (rail.classList.contains('is-collapsed')) {
                rail.classList.add('is-expanded');
            }
        });
        rail.addEventListener('mouseleave', () => {
            rail.classList.remove('is-expanded');
        });

        // Hàm cuộn mượt đến mục được chọn
        function scrollToSection(targetHref) {
            const target = document.querySelector(targetHref);
            if (target) {
                const offset = 75;
                const topPos = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({
                    top: Math.max(0, topPos),
                    behavior: 'smooth'
                });
                try { history.replaceState(null, '', targetHref); } catch (err) {}
                setActive(targetHref);
            }
        }

        // 4. Đồng bộ click cuộn mượt và highlight
        railLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('data-href');
                scrollToSection(href);
            });
        });

        // Nút cuộn lên đầu trang
        const scrollTopBtn = rail.querySelector('#railBtnScrollTop');
        if (scrollTopBtn) {
            scrollTopBtn.addEventListener('click', (e) => {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
                try { history.replaceState(null, '', window.location.pathname); } catch (err) {}
                const firstHref = railItems[0]?.href;
                if (firstHref) setActive(firstHref);
            });
        }

        // Nút mở bảng phím tắt
        const shortcutsBtn = rail.querySelector('#railBtnShortcuts');
        if (shortcutsBtn) {
            shortcutsBtn.addEventListener('click', (e) => {
                e.preventDefault();
                toggleShortcutsModal(true);
            });
        }

        // Hàm cập nhật trạng thái active cho cả 2 nơi (Top Capsule Nav + Side Rail)
        let currentActiveHref = railItems[0].href;
        function setActive(activeHref) {
            currentActiveHref = activeHref;
            railLinks.forEach(l => {
                if (l.getAttribute('data-href') === activeHref) {
                    l.classList.add('active');
                } else {
                    l.classList.remove('active');
                }
            });

            originalLinks.forEach(origLink => {
                const href = origLink.getAttribute('href');
                if (href === activeHref) {
                    origLink.classList.add('active');
                } else {
                    origLink.classList.remove('active');
                }
            });
        }

        // 5. CƠ CHẾ BIẾN ĐỔI CHUYỂN ĐỘNG LIÊN TỤC (1MS Taekwondo FLIP Spring Morphing)
        // Thông số vật lý Framer Motion thu được từ phân tích kỹ nghệ đảo ngược:
        // Spring: stiffness = 170, damping = 24, mass = 1 (zeta = 0.9204, settling ~650ms)
        const SPRING_LINEAR_EASE = 'linear(0.0000, 0.0290, 0.0991, 0.1908, 0.2911, 0.3911, 0.4858, 0.5719, 0.6483, 0.7144, 0.7706, 0.8177, 0.8567, 0.8885, 0.9141, 0.9346, 0.9508, 0.9635, 0.9733, 0.9808, 0.9864, 0.9907, 0.9938, 0.9961, 0.9977, 0.9988, 0.9996, 1.0001, 1.0004, 1.0005, 1.0006)';
        const SPRING_BEZIER_FALLBACK = 'cubic-bezier(0.16, 1, 0.3, 1)';

        let activeSpringEase = SPRING_BEZIER_FALLBACK;
        try {
            const testEl = document.createElement('div');
            const testAnim = testEl.animate([], { easing: SPRING_LINEAR_EASE });
            if (testAnim) activeSpringEase = SPRING_LINEAR_EASE;
        } catch (e) {
            activeSpringEase = SPRING_BEZIER_FALLBACK;
        }

        let activeAnimation = null;
        let isDockedState = false;
        let isInitialized = false;

        function triggerMorph(toDock, immediate) {
            if (immediate) {
                if (activeAnimation) {
                    activeAnimation.cancel();
                    activeAnimation = null;
                }
                document.body.classList.remove('is-morphing-dock', 'is-morphing-top');
                glider.classList.remove('is-active');
                glider.style.transform = 'none';
                if (toDock) {
                    document.body.classList.add('is-scrolled-dock');
                } else {
                    document.body.classList.remove('is-scrolled-dock');
                }
                return;
            }

            const isDesktop = window.innerWidth >= 1100;
            if (!isDesktop) return;

            const navRect = sectionNav.getBoundingClientRect();
            const dockRect = macosBox.getBoundingClientRect();

            let fromRect, targetRect, fromRadius, targetRadius;

            if (toDock) {
                // Top Capsule -> Right Dock
                if (activeAnimation) {
                    fromRect = glider.getBoundingClientRect();
                    fromRadius = getComputedStyle(glider).borderRadius || '9999px';
                    activeAnimation.cancel();
                    activeAnimation = null;
                } else {
                    fromRect = navRect;
                    fromRadius = '9999px';
                }
                targetRect = dockRect;
                targetRadius = '28px';

                document.body.classList.add('is-scrolled-dock');
                document.body.classList.add('is-morphing-dock');
                document.body.classList.remove('is-morphing-top');
            } else {
                // Right Dock -> Top Capsule
                if (activeAnimation) {
                    fromRect = glider.getBoundingClientRect();
                    fromRadius = getComputedStyle(glider).borderRadius || '28px';
                    activeAnimation.cancel();
                    activeAnimation = null;
                } else {
                    fromRect = dockRect;
                    fromRadius = '28px';
                }
                targetRect = navRect;
                targetRadius = '9999px';

                document.body.classList.remove('is-scrolled-dock');
                document.body.classList.add('is-morphing-top');
                document.body.classList.remove('is-morphing-dock');
            }

            // Thiết lập vị trí ban đầu của phần tử morphing glider
            glider.style.left = fromRect.left + 'px';
            glider.style.top = fromRect.top + 'px';
            glider.style.width = fromRect.width + 'px';
            glider.style.height = fromRect.height + 'px';
            glider.style.borderRadius = fromRadius;
            glider.style.transform = 'translate3d(0, 0, 0)';
            glider.classList.add('is-active');

            const deltaX = targetRect.left - fromRect.left;
            const deltaY = targetRect.top - fromRect.top;

            const keyframes = [
                {
                    transform: 'translate3d(0, 0, 0)',
                    width: `${fromRect.width}px`,
                    height: `${fromRect.height}px`,
                    borderRadius: fromRadius,
                    opacity: 1
                },
                {
                    transform: `translate3d(${deltaX}px, ${deltaY}px, 0)`,
                    width: `${targetRect.width}px`,
                    height: `${targetRect.height}px`,
                    borderRadius: targetRadius,
                    opacity: 1
                }
            ];

            try {
                activeAnimation = glider.animate(keyframes, {
                    duration: 650,
                    easing: activeSpringEase,
                    fill: 'forwards'
                });

                activeAnimation.onfinish = () => {
                    activeAnimation = null;
                    document.body.classList.remove('is-morphing-dock', 'is-morphing-top');
                    glider.classList.remove('is-active');
                    glider.style.transform = 'none';
                };
            } catch (err) {
                activeAnimation = null;
                document.body.classList.remove('is-morphing-dock', 'is-morphing-top');
                glider.classList.remove('is-active');
                glider.style.transform = 'none';
            }
        }

        // 6. ScrollSpy thông minh theo vị trí cuộn trang & Morphing Dock
        const DOCK_THRESHOLD = 140;
        const UNDOCK_THRESHOLD = 100;
        let isTicking = false;

        function updateScrollSpy() {
            const scrollPos = window.scrollY + 110;
            const docHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
            const winHeight = window.innerHeight;
            const isDesktop = window.innerWidth >= 1100;

            // Xử lý chuyển đổi giữa Top Capsule và Right Dock với ngưỡng trễ (Hysteresis)
            if (isDesktop) {
                if (!isInitialized) {
                    isInitialized = true;
                    isDockedState = window.scrollY > DOCK_THRESHOLD;
                    triggerMorph(isDockedState, true);
                } else {
                    if (!isDockedState && window.scrollY > DOCK_THRESHOLD) {
                        isDockedState = true;
                        triggerMorph(true);
                    } else if (isDockedState && window.scrollY < UNDOCK_THRESHOLD) {
                        isDockedState = false;
                        triggerMorph(false);
                    }
                }
            } else {
                if (isDockedState || document.body.classList.contains('is-scrolled-dock')) {
                    isDockedState = false;
                    triggerMorph(false, true);
                }
            }

            // Cập nhật vòng tròn tiến độ cuộn (Circular Scroll Progress)
            const maxScroll = docHeight - winHeight;
            const scrollFraction = maxScroll > 0 ? Math.min(1, Math.max(0, window.scrollY / maxScroll)) : 0;
            const progressBar = document.getElementById('dockProgressBar');
            if (progressBar) {
                const circumference = 125.66;
                progressBar.style.strokeDashoffset = circumference * (1 - scrollFraction);
            }

            // Ở đáy trang thì kích hoạt mục cuối
            if (window.scrollY + winHeight >= docHeight - 60) {
                const lastItem = railItems[railItems.length - 1];
                if (lastItem) {
                    setActive(lastItem.href);
                    savePosition(lastItem.href);
                }
                return;
            }

            // Ở đỉnh trang thì kích hoạt mục đầu tiên
            if (window.scrollY < 160) {
                const firstItem = railItems[0];
                if (firstItem) {
                    setActive(firstItem.href);
                    savePosition(firstItem.href);
                }
                return;
            }

            let currentHref = railItems[0].href;
            for (let i = 0; i < railItems.length; i++) {
                const sec = railItems[i].targetEl;
                if (!sec) continue;
                const top = sec.offsetTop;
                const height = sec.offsetHeight;
                if (scrollPos >= top && scrollPos < top + height) {
                    currentHref = railItems[i].href;
                    break;
                } else if (scrollPos >= top) {
                    currentHref = railItems[i].href;
                }
            }

            setActive(currentHref);
            savePosition(currentHref);
        }

        window.addEventListener('resize', () => {
            const isDesktop = window.innerWidth >= 1100;
            if (!isDesktop && isDockedState) {
                isDockedState = false;
                triggerMorph(false, true);
            }
        }, { passive: true });

        function savePosition(href) {
            if (!href || !href.startsWith('#sec-')) return;
            try {
                localStorage.setItem('marugoto_resume_' + currentFileName, href);
                localStorage.setItem('marugoto_last_lesson_url', window.location.href);
            } catch (e) {}
        }

        window.addEventListener('scroll', () => {
            if (!isTicking) {
                requestAnimationFrame(() => {
                    updateScrollSpy();
                    isTicking = false;
                });
                isTicking = true;
            }
        }, { passive: true });

        setTimeout(updateScrollSpy, 150);

        // Hỗ trợ cả khi click các pill ở thanh section-nav
        originalLinks.forEach(origLink => {
            origLink.addEventListener('click', (e) => {
                const href = origLink.getAttribute('href');
                if (href && href.startsWith('#sec-')) {
                    setActive(href);
                }
            });
        });

        // 6. KHỞI TẠO CÁC NÂNG CẤP ĐỘ MƯỢT VÀ ĐỘ TIỆN DỤNG
        const navData = getLessonNavigation(currentFileName);
        initBottomLessonNav(mainContainer, navData);
        initSmoothKeyboardEngine(railItems, scrollToSection, navData);
        initAutoScrollResume(currentFileName, railItems, scrollToSection);
        initAutoSpeakToolbar();
        initShortcutsModal();
        if (navData && navData.next) {
            initPrefetchEngine(navData.next.file);
        }
    }

    // --- HELPER CHUYỂN BÀI HỌC VÀ PREFETCH ---
    function getLessonNavigation(currentFileName) {
        const idx = ALL_LESSONS.findIndex(l => l.file === currentFileName);
        if (idx === -1) return null;
        return {
            current: ALL_LESSONS[idx],
            prev: idx > 0 ? ALL_LESSONS[idx - 1] : null,
            next: idx < ALL_LESSONS.length - 1 ? ALL_LESSONS[idx + 1] : null,
            index: idx,
            total: ALL_LESSONS.length
        };
    }

    // 7. CỤM ĐIỀU HƯỚNG BÀI TRƯỚC / BÀI TIẾP THEO Ở CUỐI TRANG
    function initBottomLessonNav(mainContainer, navData) {
        if (!navData || document.querySelector('.lesson-bottom-nav')) return;

        const bottomNav = document.createElement('nav');
        bottomNav.className = 'lesson-bottom-nav';
        bottomNav.setAttribute('aria-label', 'Chuyển bài học tiếp theo');

        const prev = navData.prev;
        const next = navData.next;

        bottomNav.innerHTML = `
            <div class="bottom-nav-inner">
                <a href="${prev ? prev.file : '#'}" class="bottom-nav-btn prev-btn ${prev ? '' : 'disabled'}" title="${prev ? prev.title : 'Đang ở bài đầu tiên'}">
                    <span class="nav-arrow">←</span>
                    <div class="nav-info">
                        <span class="nav-sub">BÀI TRƯỚC</span>
                        <span class="nav-title">${prev ? prev.icon + ' ' + prev.title : 'Đang ở bài đầu tiên'}</span>
                    </div>
                </a>

                <a href="../index.html" class="bottom-nav-btn center-hub-btn" title="Về trang chủ giáo trình 36 bài">
                    <span class="hub-icon">📚</span>
                    <div class="nav-info">
                        <span class="nav-sub">GIÁO TRÌNH MARUGOTO</span>
                        <span class="nav-title">Bài ${navData.index + 1} / ${navData.total}</span>
                    </div>
                </a>

                <a href="${next ? next.file : '#'}" class="bottom-nav-btn next-btn ${next ? '' : 'disabled'}" title="${next ? next.title : 'Đã hoàn thành toàn bộ 36 bài'}">
                    <div class="nav-info">
                        <span class="nav-sub">BÀI TIẾP THEO</span>
                        <span class="nav-title">${next ? next.icon + ' ' + next.title : 'Đã hết bài học'}</span>
                    </div>
                    <span class="nav-arrow">→</span>
                </a>
            </div>
        `;

        mainContainer.appendChild(bottomNav);
    }

    // 8. TẢI TRƯỚC NGẦM SIÊU TỐC (PREFETCH ENGINE)
    function initPrefetchEngine(nextLessonFile) {
        function prefetchUrl(url) {
            if (!url || document.querySelector(`link[rel="prefetch"][href="${url}"]`)) return;
            const link = document.createElement('link');
            link.rel = 'prefetch';
            link.href = url;
            document.head.appendChild(link);
        }

        // Tự động tải trước bài tiếp theo sau 1 giây
        if (nextLessonFile) {
            setTimeout(() => prefetchUrl(nextLessonFile), 1000);
        }

        // Tự động tải trước bất kỳ liên kết bài nào khi di chuột qua quá 100ms
        let hoverTimer = null;
        document.addEventListener('mouseover', (e) => {
            const anchor = e.target.closest('a[href$=".html"]');
            if (anchor && anchor.href && !anchor.href.includes('#')) {
                clearTimeout(hoverTimer);
                hoverTimer = setTimeout(() => {
                    prefetchUrl(anchor.getAttribute('href'));
                }, 100);
            }
        }, { passive: true });
    }

    // 9. HỆ THỐNG PHÍM TẮT HỌC THẦN TỐC
    function initSmoothKeyboardEngine(railItems, scrollToSection, navData) {
        let selectedCardIdx = -1;

        window.addEventListener('keydown', (e) => {
            // Không can thiệp nếu đang gõ trong input, textarea hoặc phòng luyện gõ
            const tag = (e.target.tagName || '').toLowerCase();
            if (tag === 'input' || tag === 'textarea' || e.target.isContentEditable) return;
            if (document.body.classList.contains('typing-active')) return;

            // Phím ? : Mở / đóng bảng hướng dẫn phím tắt
            if (e.key === '?' || (e.key === '/' && e.shiftKey)) {
                e.preventDefault();
                toggleShortcutsModal();
                return;
            }

            // Phím ESC : Đóng modal
            if (e.key === 'Escape') {
                toggleShortcutsModal(false);
                return;
            }

            // Phím Alt + Mũi tên phải hoặc Shift + N: Sang bài tiếp theo
            if ((e.altKey && e.key === 'ArrowRight') || (e.shiftKey && (e.key === 'N' || e.key === 'n'))) {
                if (navData && navData.next) {
                    e.preventDefault();
                    window.location.href = navData.next.file;
                    return;
                }
            }

            // Phím Alt + Mũi tên trái hoặc Shift + P: Về bài trước
            if ((e.altKey && e.key === 'ArrowLeft') || (e.shiftKey && (e.key === 'P' || e.key === 'p'))) {
                if (navData && navData.prev) {
                    e.preventDefault();
                    window.location.href = navData.prev.file;
                    return;
                }
            }

            // Phím J : Lướt xuống chuyên đề tiếp theo
            if (e.key === 'j' || e.key === 'J') {
                e.preventDefault();
                const activeLink = document.querySelector('.lesson-rail-link.active');
                const currHref = activeLink ? activeLink.getAttribute('data-href') : railItems[0].href;
                const idx = railItems.findIndex(i => i.href === currHref);
                const nextIdx = Math.min(railItems.length - 1, (idx >= 0 ? idx : 0) + 1);
                scrollToSection(railItems[nextIdx].href);
                return;
            }

            // Phím K : Lướt lên chuyên đề phía trước
            if (e.key === 'k' || e.key === 'K') {
                e.preventDefault();
                const activeLink = document.querySelector('.lesson-rail-link.active');
                const currHref = activeLink ? activeLink.getAttribute('data-href') : railItems[0].href;
                const idx = railItems.findIndex(i => i.href === currHref);
                const prevIdx = Math.max(0, (idx >= 0 ? idx : 0) - 1);
                scrollToSection(railItems[prevIdx].href);
                return;
            }

            // Phím 1, 2, 3, 4: Chọn phương án trắc nghiệm Mini Test đang nhìn thấy
            if (['1', '2', '3', '4'].includes(e.key)) {
                const quizCards = Array.from(document.querySelectorAll('.quiz-card'));
                if (quizCards.length > 0) {
                    const centerY = window.innerHeight / 2;
                    let closestCard = null;
                    let minDistance = Infinity;

                    quizCards.forEach(card => {
                        const rect = card.getBoundingClientRect();
                        if (rect.bottom > 80 && rect.top < window.innerHeight - 80) {
                            const dist = Math.abs((rect.top + rect.bottom) / 2 - centerY);
                            if (dist < minDistance) {
                                minDistance = dist;
                                closestCard = card;
                            }
                        }
                    });

                    if (closestCard) {
                        const opts = closestCard.querySelectorAll('.quiz-opt');
                        const optIndex = parseInt(e.key, 10) - 1;
                        if (opts[optIndex] && !opts[optIndex].disabled) {
                            e.preventDefault();
                            opts[optIndex].click();
                            opts[optIndex].classList.add('key-pressed');
                            setTimeout(() => opts[optIndex].classList.remove('key-pressed'), 200);
                        }
                    }
                }
                return;
            }

            // Phím Space và Mũi tên Trái / Phải khi đang học từ vựng
            const cards = Array.from(document.querySelectorAll('.fc-item'));
            if (cards.length > 0) {
                // Kiểm tra xem phần từ vựng có đang ở trong tầm mắt không
                const vocabSec = document.getElementById('sec-vocab');
                const isVocabInView = vocabSec ? (vocabSec.getBoundingClientRect().top < window.innerHeight && vocabSec.getBoundingClientRect().bottom > 0) : false;

                if (isVocabInView) {
                    if (e.key === 'ArrowRight') {
                        e.preventDefault();
                        selectedCardIdx = (selectedCardIdx + 1) % cards.length;
                        activateCard(cards[selectedCardIdx]);
                        return;
                    }
                    if (e.key === 'ArrowLeft') {
                        e.preventDefault();
                        selectedCardIdx = (selectedCardIdx - 1 + cards.length) % cards.length;
                        activateCard(cards[selectedCardIdx]);
                        return;
                    }
                    if (e.key === ' ' || e.key === 'a' || e.key === 'A') {
                        e.preventDefault();
                        if (selectedCardIdx < 0 || selectedCardIdx >= cards.length) selectedCardIdx = 0;
                        activateCard(cards[selectedCardIdx]);
                        return;
                    }
                }
            }
        });

        function activateCard(cardEl) {
            if (!cardEl) return;
            cardEl.focus();
            cardEl.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            cardEl.click();
        }
    }

    // 10. GHI NHỚ VỊ TRÍ ĐANG HỌC DỞ VÀ TỰ ĐỘNG TIẾP TỤC
    function initAutoScrollResume(currentFileName, railItems, scrollToSection) {
        if (window.location.hash) return; // Nếu có sẵn hash do người dùng bấm thì ưu tiên hash đó

        try {
            const savedSection = localStorage.getItem('marugoto_resume_' + currentFileName);
            if (savedSection && savedSection !== railItems[0].href) {
                const targetEl = document.querySelector(savedSection);
                if (!targetEl) return;

                const matchItem = railItems.find(i => i.href === savedSection);
                const sectionName = matchItem ? matchItem.label : 'vị trí trước';

                // Tạo toast thông báo tiếp tục
                const toast = document.createElement('div');
                toast.className = 'lesson-resume-toast';
                toast.innerHTML = `
                    <span>📍 Đang tiếp tục tại <b>${sectionName}</b></span>
                    <button type="button" class="resume-toast-btn" id="btnResumeTop">Về đầu trang</button>
                `;
                document.body.appendChild(toast);

                toast.querySelector('#btnResumeTop')?.addEventListener('click', () => {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                    toast.classList.add('is-hiding');
                    setTimeout(() => toast.remove(), 350);
                });

                // Tự động cuộn êm đến mục đang học sau 350ms
                setTimeout(() => {
                    scrollToSection(savedSection);
                }, 350);

                // Tự biến mất sau 4 giây
                setTimeout(() => {
                    if (toast.parentNode) {
                        toast.classList.add('is-hiding');
                        setTimeout(() => toast.remove(), 350);
                    }
                }, 4000);
            }
        } catch (e) {}
    }

    // 11. THANH TIỆN ÍCH TỰ ĐỘNG ĐỌC TỪ VỰNG FLASHCARD
    function initAutoSpeakToolbar() {
        const vocabSec = document.getElementById('sec-vocab');
        if (!vocabSec) return;

        const grid = vocabSec.querySelector('.flashcard-grid');
        if (!grid || vocabSec.querySelector('.vocab-quick-toolbar')) return;

        const toolbar = document.createElement('div');
        toolbar.className = 'vocab-quick-toolbar';

        const isAutoSpeakOn = localStorage.getItem('marugoto_auto_speak') === 'true';

        toolbar.innerHTML = `
            <label class="auto-speak-toggle" title="Tự động phát âm thanh giọng Tokyo khi đổi từ">
                <input type="checkbox" id="chkAutoSpeakVocab" ${isAutoSpeakOn ? 'checked' : ''}>
                <span class="toggle-slider"></span>
                <span class="toggle-label">🔊 Tự động đọc từ khi lướt</span>
            </label>
            <span class="keyboard-tip-badge" id="btnVocabShortcutTip" title="Bấm để xem tất cả phím tắt học thần tốc">
                ⌨️ Phím tắt: [Space] Nghe • [←/→] Đổi từ • [?] Hướng dẫn
            </span>
        `;

        vocabSec.insertBefore(toolbar, grid);

        const chk = toolbar.querySelector('#chkAutoSpeakVocab');
        if (chk) {
            chk.addEventListener('change', () => {
                localStorage.setItem('marugoto_auto_speak', String(chk.checked));
            });
        }

        toolbar.querySelector('#btnVocabShortcutTip')?.addEventListener('click', () => {
            toggleShortcutsModal(true);
        });
    }

    // 12. BẢNG HƯỚNG DẪN PHÍM TẮT MODAL
    let shortcutsModal = null;
    function initShortcutsModal() {
        if (shortcutsModal) return;

        shortcutsModal = document.createElement('div');
        shortcutsModal.className = 'lesson-shortcuts-modal';
        shortcutsModal.innerHTML = `
            <div class="shortcuts-modal-card" role="dialog" aria-modal="true" aria-label="Bảng phím tắt học tiếng Nhật">
                <div class="shortcuts-modal-header">
                    <div class="shortcuts-modal-title">⌨️ Phím tắt học thần tốc</div>
                    <button type="button" class="shortcuts-modal-close" id="btnCloseShortcuts" aria-label="Đóng">✕</button>
                </div>
                <div class="shortcuts-list">
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Chuyển sang chuyên đề tiếp theo</span>
                        <div class="shortcut-keys"><kbd class="key-cap">J</kbd></div>
                    </div>
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Quay lại chuyên đề phía trước</span>
                        <div class="shortcut-keys"><kbd class="key-cap">K</kbd></div>
                    </div>
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Chọn nhanh đáp án Mini Test</span>
                        <div class="shortcut-keys">
                            <kbd class="key-cap">1</kbd>
                            <kbd class="key-cap">2</kbd>
                            <kbd class="key-cap">3</kbd>
                            <kbd class="key-cap">4</kbd>
                        </div>
                    </div>
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Lật thẻ từ vựng & Nghe phát âm</span>
                        <div class="shortcut-keys"><kbd class="key-cap">Space</kbd> hoặc <kbd class="key-cap">A</kbd></div>
                    </div>
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Chuyển từ vựng trước hoặc sau</span>
                        <div class="shortcut-keys"><kbd class="key-cap">←</kbd> <kbd class="key-cap">→</kbd></div>
                    </div>
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Chuyển sang bài học tiếp theo</span>
                        <div class="shortcut-keys"><kbd class="key-cap">Alt</kbd> + <kbd class="key-cap">→</kbd> hoặc <kbd class="key-cap">Shift</kbd> + <kbd class="key-cap">N</kbd></div>
                    </div>
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Quay về bài học trước đó</span>
                        <div class="shortcut-keys"><kbd class="key-cap">Alt</kbd> + <kbd class="key-cap">←</kbd> hoặc <kbd class="key-cap">Shift</kbd> + <kbd class="key-cap">P</kbd></div>
                    </div>
                    <div class="shortcut-item">
                        <span class="shortcut-desc">Đóng bảng phím tắt này</span>
                        <div class="shortcut-keys"><kbd class="key-cap">Esc</kbd></div>
                    </div>
                </div>
            </div>
        `;

        document.body.appendChild(shortcutsModal);

        shortcutsModal.querySelector('#btnCloseShortcuts')?.addEventListener('click', () => {
            toggleShortcutsModal(false);
        });

        shortcutsModal.addEventListener('click', (e) => {
            if (e.target === shortcutsModal) {
                toggleShortcutsModal(false);
            }
        });
    }

    function toggleShortcutsModal(forceState) {
        if (!shortcutsModal) initShortcutsModal();
        const isOpen = shortcutsModal.classList.contains('is-open');
        const nextState = typeof forceState === 'boolean' ? forceState : !isOpen;
        if (nextState) {
            shortcutsModal.classList.add('is-open');
        } else {
            shortcutsModal.classList.remove('is-open');
        }
    }

    window.initLessonSidebarRail = initLessonSidebarRail;
    window.toggleShortcutsModal = toggleShortcutsModal;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLessonSidebarRail);
    } else {
        initLessonSidebarRail();
    }
})();
