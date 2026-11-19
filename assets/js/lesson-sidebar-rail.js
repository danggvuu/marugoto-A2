/**
 * MACOS-STYLE COMPACT FLOATING SECTION RAIL (assets/js/lesson-sidebar-rail.js)
 * Tự động chuyển đổi thanh điều hướng bài học thành thanh sidebar nổi nhỏ gọn kiểu macOS
 * Cố định bên cạnh, tự động bám theo cuộn trang (ScrollSpy), hỗ trợ thu gọn/mở rộng.
 */
(function () {
    'use strict';

    function initLessonSidebarRail() {
        // Tránh khởi tạo lặp lại
        if (document.getElementById('lessonSidebarRail')) return;

        const sectionNav = document.querySelector('.section-nav');
        if (!sectionNav) return;

        const originalLinks = Array.from(sectionNav.querySelectorAll('a[href^="#sec-"]'));
        if (originalLinks.length < 2) return;

        // Đánh dấu body
        document.body.classList.add('has-lesson-rail');

        // Phân tích các mục điều hướng
        const railItems = originalLinks.map((link, idx) => {
            const href = link.getAttribute('href');
            const rawText = link.textContent.trim();
            const targetEl = document.querySelector(href);

            let icon = '●';
            let label = rawText;

            // Tách biểu tượng (emoji, biểu tượng số tròn, hoặc ký tự đầu)
            const iconRegex = /^([①-⑳0-9\.\-\u{1F000}-\u{1FAFF}\u{2300}-\u{27BF}\u{FE00}-\u{FE0F}]+)\s*(.*)$/u;
            const match = rawText.match(iconRegex);
            if (match && match[1].trim()) {
                icon = match[1].trim();
                label = match[2].trim();
            }

            // Rút gọn các nhãn dài để vừa vặn khung nhỏ gọn
            label = label
                .replace(/^Biến Thể Động Từ.*$/i, 'Biến Thể ĐT')
                .replace(/^Luyện Gõ.*$/i, 'Luyện Gõ')
                .replace(/^\d+\s*Từ Vựng.*$/i, 'Từ Vựng')
                .replace(/^\d+\s*Chữ Hán.*$/i, 'Chữ Hán')
                .replace(/^Mini Test.*$/i, 'Mini Test')
                .replace(/^Máy Luyện Chia Thể.*$/i, 'Luyện Chia Thể');

            return {
                href,
                targetEl,
                icon,
                label,
                fullTitle: rawText
            };
        }).filter(item => item.targetEl !== null);

        if (railItems.length === 0) return;

        // Tạo phần tử Aside thanh bên macOS
        const rail = document.createElement('aside');
        rail.id = 'lessonSidebarRail';
        rail.className = 'lesson-sidebar-rail';
        rail.setAttribute('aria-label', 'Thanh mục lục bài học');

        // Tạo cấu trúc HTML chuẩn macOS
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
                        <a href="${item.href}" class="lesson-rail-link ${idx === 0 ? 'active' : ''}" data-href="${item.href}" title="${item.fullTitle}">
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

        // Khôi phục trạng thái thu gọn đã lưu
        const isCollapsedSaved = localStorage.getItem('marugoto_rail_collapsed') === 'true';
        if (isCollapsedSaved) {
            rail.classList.add('is-collapsed');
            document.body.classList.add('rail-collapsed');
        }

        // Bắt sự kiện nút thu gọn
        const toggleBtn = rail.querySelector('#btnToggleSidebarRail');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const isCollapsed = rail.classList.toggle('is-collapsed');
                document.body.classList.toggle('rail-collapsed', isCollapsed);
                localStorage.setItem('marugoto_rail_collapsed', String(isCollapsed));
            });
        }

        // Bắt sự kiện cuộn mượt khi click vào từng link
        const railLinks = Array.from(rail.querySelectorAll('.lesson-rail-link'));
        railLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const href = link.getAttribute('data-href');
                const target = document.querySelector(href);
                if (target) {
                    const offset = 80;
                    const topPos = target.getBoundingClientRect().top + window.pageYOffset - offset;
                    window.scrollTo({
                        top: Math.max(0, topPos),
                        behavior: 'smooth'
                    });
                    try {
                        history.replaceState(null, '', href);
                    } catch (err) {}
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
                try {
                    history.replaceState(null, '', window.location.pathname);
                } catch (err) {}
            });
        }

        // Đặt active cho link
        function setActive(activeHref) {
            railLinks.forEach(l => {
                if (l.getAttribute('data-href') === activeHref) {
                    l.classList.add('active');
                } else {
                    l.classList.remove('active');
                }
            });
        }

        // ScrollSpy thông minh tự động nhận diện phần đang đọc
        let isTicking = false;
        function updateScrollSpy() {
            const scrollPos = window.scrollY + 120;
            const docHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
            const winHeight = window.innerHeight;

            // Nếu chạm sát đáy trang -> active mục cuối cùng (thường là Mini Test)
            if (window.scrollY + winHeight >= docHeight - 60) {
                const lastItem = railItems[railItems.length - 1];
                if (lastItem) setActive(lastItem.href);
                return;
            }

            // Nếu đang ở đầu trang
            if (window.scrollY < 180) {
                const firstItem = railItems[0];
                if (firstItem) setActive(firstItem.href);
                return;
            }

            // Tìm section đang nằm trong tầm nhìn
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

        // Cập nhật khi mới load xong
        setTimeout(updateScrollSpy, 150);

        // Hỗ trợ cả các link trong top nav cũ khi click
        originalLinks.forEach(origLink => {
            origLink.addEventListener('click', (e) => {
                const href = origLink.getAttribute('href');
                if (href && href.startsWith('#sec-')) {
                    setActive(href);
                }
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLessonSidebarRail);
    } else {
        initLessonSidebarRail();
    }
})();
