/* Optional section-by-section reading without changing lesson content or checkpoints. */
(function () {
    'use strict';
    function init() {
        const sections = Array.from(document.querySelectorAll('section.content-section[id]'));
        if (sections.length < 2 || document.getElementById('lessonOutline')) return;
        document.body.classList.add('lesson-page');
        const outline = document.createElement('details');
        outline.id = 'lessonOutline';
        outline.className = 'lesson-outline';
        const summary = document.createElement('summary');
        summary.textContent = 'Mục lục & học theo từng phần';
        const controls = document.createElement('div');
        controls.className = 'lesson-outline-controls';
        const label = document.createElement('label');
        label.htmlFor = 'lessonSectionSelect';
        label.textContent = 'Phần đang học';
        const select = document.createElement('select');
        select.id = 'lessonSectionSelect';
        sections.forEach((section, index) => {
            const option = document.createElement('option');
            option.value = section.id;
            option.textContent = section.querySelector('h2')?.textContent.trim() || `Phần ${index + 1}`;
            select.appendChild(option);
        });
        const focusBtn = document.createElement('button');
        focusBtn.type = 'button';
        focusBtn.textContent = 'Học từng phần';
        focusBtn.setAttribute('aria-pressed', 'false');
        const previous = document.createElement('button');
        previous.type = 'button';
        previous.textContent = '← Phần trước';
        const next = document.createElement('button');
        next.type = 'button';
        next.textContent = 'Phần tiếp →';
        let focused = false;
        function apply(scroll) {
            sections.forEach(section => section.classList.toggle('lesson-focus-hidden', focused && section.id !== select.value));
            previous.disabled = select.selectedIndex === 0;
            next.disabled = select.selectedIndex === sections.length - 1;
            focusBtn.setAttribute('aria-pressed', String(focused));
            focusBtn.textContent = focused ? 'Xem toàn bộ bài' : 'Học từng phần';
            if (scroll) sections[select.selectedIndex].scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        select.addEventListener('change', () => apply(true));
        focusBtn.addEventListener('click', () => { focused = !focused; apply(true); });
        previous.addEventListener('click', () => { select.selectedIndex--; apply(true); });
        next.addEventListener('click', () => { select.selectedIndex++; apply(true); });
        function followHash(hash) {
            const index = sections.findIndex(section => '#' + section.id === hash);
            if (index < 0) return;
            select.selectedIndex = index;
            apply(false);
        }
        document.addEventListener('click', event => {
            const anchor = event.target.closest('a[href^="#sec-"]');
            if (anchor) followHash(anchor.getAttribute('href'));
        }, true);
        window.addEventListener('hashchange', () => followHash(window.location.hash));
        controls.append(label, select, focusBtn, previous, next);
        outline.append(summary, controls);
        sections[0].before(outline);
        followHash(window.location.hash);
        apply(false);
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();
})();
