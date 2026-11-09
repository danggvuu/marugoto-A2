/**
 * GLOBAL HUB NAVIGATION CONTROLLER (assets/js/nav-dropdown.js)
 * Cầu nối tương thích ngược hỗ trợ gọi toggle dropdown mượt mà cho cả Desktop & Mobile.
 */
(function () {
    'use strict';

    if (!window.toggleFormsDropdown) {
        window.toggleFormsDropdown = function (e) {
            if (e) {
                e.preventDefault();
                e.stopPropagation();
            }
            const fm = document.getElementById('formsDropdownMenu');
            if (fm) fm.classList.toggle('show');
            const tm = document.getElementById('testsDropdownMenu');
            if (tm) tm.classList.remove('show');
            const lm = document.getElementById('lessonsDropdownMenu');
            if (lm) lm.classList.remove('show');
        };
    }

    if (!window.toggleTestsDropdown) {
        window.toggleTestsDropdown = function (e) {
            if (e) {
                e.preventDefault();
                e.stopPropagation();
            }
            const tm = document.getElementById('testsDropdownMenu');
            if (tm) tm.classList.toggle('show');
            const fm = document.getElementById('formsDropdownMenu');
            if (fm) fm.classList.remove('show');
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
            const lm = document.getElementById('lessonsDropdownMenu');
            if (lm) lm.classList.toggle('show');
            const fm = document.getElementById('formsDropdownMenu');
            if (fm) fm.classList.remove('show');
            const tm = document.getElementById('testsDropdownMenu');
            if (tm) tm.classList.remove('show');
        };
    }
})();
