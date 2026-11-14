/**
 * MARUGOTO JAPANESE INTERACTIVE HUB - CLIENT CONTROLLER
 * File: assets/js/pages/index_hub.js
 * Handles:
 * 1. Category filtering (Tabs/Pills)
 * 2. Real-time fast search (Keyboard shortcut '/', clear button, empty state)
 * 3. Dynamic badge counts
 * 4. Filter state persistence with localStorage
 */

(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', () => {
        initHubApp();
    });

    function initHubApp() {
        const searchInput = document.getElementById('hubSearchInput');
        const searchClear = document.getElementById('hubSearchClear');
        const filterPills = document.querySelectorAll('.hub-pill');
        const cardsGrid = document.getElementById('hubCardsGrid');
        const cards = Array.from(document.querySelectorAll('.hub-card'));
        const visibleCountEl = document.getElementById('hubVisibleCount');
        const lessonsSection = document.getElementById('hubLessonsSection');

        let currentCategory = 'all';
        let searchQuery = '';

        // 1. Calculate & display initial category counts
        updateCategoryCounts();

        // 2. Restore saved category if any
        try {
            const savedFilter = localStorage.getItem('marugoto_hub_active_filter');
            if (savedFilter && document.querySelector(`.hub-pill[data-filter="${savedFilter}"]`)) {
                currentCategory = savedFilter;
                filterPills.forEach(pill => {
                    const isActive = pill.getAttribute('data-filter') === currentCategory;
                    pill.classList.toggle('active', isActive);
                    pill.setAttribute('aria-selected', isActive ? 'true' : 'false');
                });
            }
        } catch (e) {
            // Ignore localStorage errors
        }

        // Apply initial filter
        applyFilter();

        // 3. Category Pill Click Handler
        filterPills.forEach(pill => {
            pill.addEventListener('click', () => {
                const filter = pill.getAttribute('data-filter');
                if (!filter) return;

                currentCategory = filter;
                filterPills.forEach(p => {
                    p.classList.remove('active');
                    p.setAttribute('aria-selected', 'false');
                });
                pill.classList.add('active');
                pill.setAttribute('aria-selected', 'true');

                try {
                    localStorage.setItem('marugoto_hub_active_filter', currentCategory);
                } catch (e) {}

                applyFilter();

                // If user clicks lessons pill, smoothly scroll to lessons section
                if (filter === 'lessons' && lessonsSection) {
                    lessonsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // 4. Search Input Handler
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                searchQuery = (e.target.value || '').trim().toLowerCase();
                if (searchClear) {
                    searchClear.style.display = searchQuery.length > 0 ? 'flex' : 'none';
                }
                applyFilter();
            });

            // Keyboard shortcut: '/' to focus search, 'Esc' to clear & blur
            document.addEventListener('keydown', (e) => {
                if (e.key === '/' && document.activeElement !== searchInput) {
                    const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
                    if (activeTag !== 'input' && activeTag !== 'textarea') {
                        e.preventDefault();
                        searchInput.focus();
                        searchInput.select();
                    }
                } else if (e.key === 'Escape' && document.activeElement === searchInput) {
                    if (searchInput.value.length > 0) {
                        searchInput.value = '';
                        searchQuery = '';
                        if (searchClear) searchClear.style.display = 'none';
                        applyFilter();
                    }
                    searchInput.blur();
                }
            });
        }

        // 5. Search Clear Button Handler
        if (searchClear) {
            searchClear.addEventListener('click', () => {
                if (searchInput) {
                    searchInput.value = '';
                    searchInput.focus();
                }
                searchQuery = '';
                searchClear.style.display = 'none';
                applyFilter();
            });
        }

        // 6. Reset Filters (Called by Empty State button)
        window.resetHubFilters = function () {
            currentCategory = 'all';
            searchQuery = '';
            if (searchInput) {
                searchInput.value = '';
            }
            if (searchClear) {
                searchClear.style.display = 'none';
            }
            filterPills.forEach(p => {
                const isAll = p.getAttribute('data-filter') === 'all';
                p.classList.toggle('active', isAll);
                p.setAttribute('aria-selected', isAll ? 'true' : 'false');
            });
            try {
                localStorage.removeItem('marugoto_hub_active_filter');
            } catch (e) {}
            applyFilter();
        };

        // 7. Core filter & search logic
        function applyFilter() {
            let visibleCount = 0;

            // Filter Feature Cards
            cards.forEach(card => {
                const category = card.getAttribute('data-category') || '';
                const title = (card.querySelector('.hub-card-title')?.textContent || '').toLowerCase();
                const subtitle = (card.querySelector('.hub-card-subtitle')?.textContent || '').toLowerCase();
                const desc = (card.querySelector('.hub-card-desc')?.textContent || '').toLowerCase();
                const keywords = (card.getAttribute('data-keywords') || '').toLowerCase();
                const allCardText = `${title} ${subtitle} ${desc} ${keywords}`;

                const matchesCategory = (currentCategory === 'all' || category === currentCategory);
                const matchesSearch = searchQuery === '' || allCardText.includes(searchQuery);

                if (matchesCategory && matchesSearch) {
                    card.style.display = 'flex';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });

            // Filter Lessons Section
            if (lessonsSection) {
                const lessonItems = Array.from(lessonsSection.querySelectorAll('.hub-lesson-item'));
                let visibleLessonItems = 0;

                lessonItems.forEach(item => {
                    const text = (item.textContent || '').toLowerCase();
                    const matchesSearch = searchQuery === '' || text.includes(searchQuery);
                    if (matchesSearch) {
                        item.style.display = 'flex';
                        visibleLessonItems++;
                    } else {
                        item.style.display = 'none';
                    }
                });

                const shouldShowLessonsSection = (currentCategory === 'all' || currentCategory === 'lessons') && (visibleLessonItems > 0 || searchQuery === '');
                lessonsSection.style.display = shouldShowLessonsSection ? 'block' : 'none';

                if (shouldShowLessonsSection && (currentCategory === 'lessons' || searchQuery !== '')) {
                    visibleCount += visibleLessonItems;
                }
            }

            // Update visible counter
            if (visibleCountEl) {
                visibleCountEl.textContent = String(visibleCount);
            }

            // Handle Empty State
            let emptyState = document.getElementById('hubEmptyState');
            if (visibleCount === 0) {
                if (!emptyState && cardsGrid) {
                    emptyState = document.createElement('div');
                    emptyState.id = 'hubEmptyState';
                    emptyState.className = 'hub-empty-state';
                    emptyState.innerHTML = `
                        <div class="hub-empty-icon">🔍</div>
                        <h3 class="hub-empty-title">Không tìm thấy tài nguyên phù hợp</h3>
                        <p class="hub-empty-desc">Không có kết quả nào khớp với từ khóa "${escapeHtml(searchQuery)}" hoặc danh mục đã chọn.</p>
                        <button type="button" class="hub-empty-reset-btn" onclick="window.resetHubFilters()">Đặt lại bộ lọc</button>
                    `;
                    cardsGrid.appendChild(emptyState);
                }
                if (emptyState) emptyState.style.display = 'block';
            } else if (emptyState) {
                emptyState.style.display = 'none';
            }
        }

        // 8. Dynamic count calculations
        function updateCategoryCounts() {
            const counts = {
                all: cards.length,
                grammar: 0,
                'vocab-kanji': 0,
                typing: 0,
                exams: 0,
                lessons: 18,
                'culture-3d': 0
            };

            cards.forEach(card => {
                const cat = card.getAttribute('data-category');
                if (counts[cat] !== undefined) {
                    counts[cat]++;
                }
            });

            // Set badge texts
            for (const key of Object.keys(counts)) {
                const badge = document.getElementById(`count-${key}`);
                if (badge) {
                    badge.textContent = String(counts[key]);
                }
            }
        }

        function escapeHtml(str) {
            const div = document.createElement('div');
            div.textContent = str;
            return div.innerHTML;
        }
    }
})();
