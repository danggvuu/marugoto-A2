/* Extracted page script for tests/On_Tap_Mini_Test_A2_5_8.html */
function handleHashNavigation() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#grammar-l')) {
        if (typeof switchMainTab === 'function') {
            switchMainTab('tab-theory');
        }
        setTimeout(() => {
            const target = document.querySelector(hash);
            if (target) {
                const dockHeight = 75;
                const pos = target.getBoundingClientRect().top + window.pageYOffset - dockHeight;
                window.scrollTo({ top: pos, behavior: 'smooth' });

                // Highlight active pill
                const lessonNum = hash.replace('#grammar-l', '');
                document.querySelectorAll('.dock-pill').forEach(p => {
                    if (p.getAttribute('data-lesson') === lessonNum) {
                        p.classList.add('active');
                    } else {
                        p.classList.remove('active');
                    }
                });
            }
        }, 150);
    }
}
window.addEventListener('load', handleHashNavigation);
window.addEventListener('hashchange', handleHashNavigation);
