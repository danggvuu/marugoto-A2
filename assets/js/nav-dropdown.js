/**
 * GLOBAL HUB NAVIGATION DROPDOWN CONTROLLER
 * Toggles for:
 * - testsDropdownMenu (🎯 Ôn Tập & Đề Thi ▾)
 * - lessonsDropdownMenu (🚀 Web Bài Học 10-18 ▾)
 */
(function() {
    'use strict';

    function toggleTestsDropdown(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const m = document.getElementById('testsDropdownMenu');
        if (m) {
            m.classList.toggle('show');
        }
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) {
            lm.classList.remove('show');
        }
    }

    function toggleLessonsDropdown(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) {
            m.classList.toggle('show');
        }
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) {
            tm.classList.remove('show');
        }
    }

    // Close when clicking anywhere outside
    window.addEventListener('click', function(e) {
        if (e && e.target && e.target.closest && e.target.closest('.hub-dropdown')) {
            return;
        }
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    });

    // Close on Escape key
    window.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const lm = document.getElementById('lessonsDropdownMenu');
            if (lm) lm.classList.remove('show');
            const tm = document.getElementById('testsDropdownMenu');
            if (tm) tm.classList.remove('show');
        }
    });

    // Expose globally
    window.toggleTestsDropdown = toggleTestsDropdown;
    window.toggleLessonsDropdown = toggleLessonsDropdown;
})();
