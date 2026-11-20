/**
 * MACOS-STYLE COMPACT FLOATING SECTION RAIL & SCROLLSPY SYNC
 * (assets/js/lesson-sidebar-rail.js)
 * 
 * 1. Bố cục bài học CĂN GIỮA HOÀN HẢO 100% - Không di dời DOM gây lệch trang
 * 2. Cố định nổi bên cạnh (position: fixed), tự động bám theo cuộn trang (Sticky ScrollSpy)
 * 3. Đồng bộ trạng thái active hai chiều giữa thanh capsule trên và thanh rail bên cạnh
 * 4. Hỗ trợ thu gọn/mở rộng, ghi nhớ trạng thái bằng localStorage
 */
(function () {
    'use strict';

    function initLessonSidebarRail() {
        if (document.getElementById('lessonSidebarRail')) return;

        const mainContainer = document.querySelector('.main-container');
        if (!mainContainer) return;

        const sectionNav = mainContainer.querySelector('.section-nav');
        if (!sectionNav) return;

        const originalLinks = Array.from(sectionNav.querySelectorAll('a[href^="#sec-"]'));
        if (originalLinks.length < 2) return;

        document.body.classList.add('has-lesson-rail');

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

        // 2. Tạo thanh sidebar macOS nổi fixed bên cạnh (KHÔNG di chuyển mainContainer để giữ căn giữa)
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
                    <span class="macos-sidebar-title">MỤC LỤC</span>
                    <button type="button" class="macos-sidebar-toggle" id="btnToggleSidebarRail" title="Thu gọn / Mở rộng" aria-label="Thu gọn hoặc mở rộng mục lục">
                        <span class="macos-toggle-arrow">›</span>
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
                    <button type="button" class="rail-btn-top" id="railBtnScrollTop" title="Cuộn lên đầu trang">
                        <span class="top-icon">⬆️</span>
                        <span class="top-text">Lên đầu trang</span>
                    </button>
                </div>
            </div>
        `;

        document.body.appendChild(rail);

        // 3. Khôi phục trạng thái thu gọn từ localStorage
        const isCollapsedSaved = localStorage.getItem('marugoto_rail_collapsed') === 'true';
        if (isCollapsedSaved) {
            rail.classList.add('is-collapsed');
            document.body.classList.add('rail-collapsed');
        }

        // Sự kiện nút thu gọn / mở rộng
        const toggleBtn = rail.querySelector('#btnToggleSidebarRail');
        if (toggleBtn) {
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

        // 4. Đồng bộ click cuộn mượt và highlight
        const railLinks = Array.from(rail.querySelectorAll('.lesson-rail-link'));
        railLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('data-href');
                const target = document.querySelector(href);
                if (target) {
                    const offset = 75;
                    const topPos = target.getBoundingClientRect().top + window.pageYOffset - offset;
                    window.scrollTo({
                        top: Math.max(0, topPos),
                        behavior: 'smooth'
                    });
                    try { history.replaceState(null, '', href); } catch (err) {}
                    setActive(href);
                }
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

        // Hàm cập nhật trạng thái active cho cả 2 nơi (Top Capsule Nav + Side Rail)
        function setActive(activeHref) {
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

        // 5. ScrollSpy thông minh theo vị trí cuộn trang
        let isTicking = false;
        function updateScrollSpy() {
            const scrollPos = window.scrollY + 110;
            const docHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
            const winHeight = window.innerHeight;

            // Ở đáy trang thì kích hoạt mục cuối
            if (window.scrollY + winHeight >= docHeight - 60) {
                const lastItem = railItems[railItems.length - 1];
                if (lastItem) setActive(lastItem.href);
                return;
            }

            // Ở đỉnh trang thì kích hoạt mục đầu tiên
            if (window.scrollY < 160) {
                const firstItem = railItems[0];
                if (firstItem) setActive(firstItem.href);
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
    }

    window.initLessonSidebarRail = initLessonSidebarRail;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLessonSidebarRail);
    } else {
        initLessonSidebarRail();
    }
})();
