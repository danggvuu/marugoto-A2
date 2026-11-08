/**
 * GLOBAL HUB NAVIGATION CONTROLLER (assets/js/nav-dropdown.js)
 * Cầu nối tương thích ngược hỗ trợ gọi toggle dropdown mượt mà cho cả Desktop & Mobile.
 */
(function () {
    'use strict';

    if (!window.toggleTestsDropdown) {
        window.toggleTestsDropdown = function (e) {
            if (e) {
                e.preventDefault();
                e.stopPropagation();
            }
            const m = document.getElementById('testsDropdownMenu');
            if (m) m.classList.toggle('show');
            const lm = document.getElementById('lessonsDropdownMenu');
            if (lm) lm.classList.remove('show');
        };
    }

    if (!window.toggleLessonsDropdown) {
        window.toggleLessonsDropdown = function (e) {
            if (e) {
                e.preventDefault();
                e.stopPropagation();
            }
            const m = document.getElementById('lessonsDropdownMenu');
            if (m) m.classList.toggle('show');
            const tm = document.getElementById('testsDropdownMenu');
            if (tm) tm.classList.remove('show');
        };
    }
})();
