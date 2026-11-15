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

        // 1. Calculate & display initial category counts & resume progress
        updateCategoryCounts();
        updateResumeButton();

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

        // 9. Real-time Resume Study Button derived from localStorage
        function updateResumeButton() {
            const resumeBtn = document.getElementById('hubResumeBtn');
            if (!resumeBtn) return;

            let latestActivity = null;
            let latestTime = 0;
            const hasContent = value => {
                if (Array.isArray(value)) return value.length > 0;
                if (value && typeof value === 'object') return Object.values(value).some(hasContent);
                return value !== '' && value !== null && value !== undefined && value !== false && value !== 0;
            };
            const consider = (title, url, timestamp) => {
                const time = Number(timestamp);
                if (!Number.isFinite(time) || time <= latestTime) return;
                latestTime = time;
                latestActivity = { title, url };
            };

            // Check typing studio progress
            try {
                const tsRaw = localStorage.getItem('marugoto_typing_studio_v2');
                if (tsRaw) {
                    const ts = JSON.parse(tsRaw);
                    const histKeys = ts && ts.history ? Object.keys(ts.history) : [];
                    if (histKeys.length > 0 || hasContent(ts && ts.drafts)) {
                        const m = ts.mode || 'sentence';
                        const modeLabel = m === 'sentence' ? 'Luyện gõ câu' : (m === 'kanji' ? 'Luyện Kanji' : 'Luyện từ vựng');
                        const targetUrl = 'tests/On_Tap_Mini_Test_A2_15_18.html#typing';
                        consider(`Tiếp tục: ${modeLabel} →`, targetUrl, ts.savedAt);
                    }
                }
            } catch (e) {}

            // Check checkpoint-sync keys across pages
            try {
                for (let i = 0; i < localStorage.length; i++) {
                    const key = localStorage.key(i);
                    if (key && key.startsWith('marugoto_cp_v1::')) {
                        const val = localStorage.getItem(key);
                        if (!val) continue;
                        let parsed;
                        try { parsed = JSON.parse(val); } catch (e) { continue; }
                        const [pagePath, slot] = key.replace('marugoto_cp_v1::', '').split('::');
                        // Merely opening a menu/tab is not a study session.
                        if (!['inputs', 'clicks', 'dialogue', 'graded', 'typing_practice'].includes(slot)) continue;
                        if (!hasContent(parsed && parsed.d)) continue;
                        if (!/^(?:lessons\/|tests\/)?[\w-]+\.html$/.test(pagePath) || pagePath === 'index.html') continue;
                        if (parsed && parsed.t && parsed.t > latestTime) {
                            let friendlyName = pagePath;
                            let link = pagePath;

                            if (pagePath.includes('Marugoto_A2_Lesson_')) {
                                const num = pagePath.match(/Lesson_(\d+)/)?.[1] || '';
                                friendlyName = `Bài ${num} (A2-1)`;
                            } else if (pagePath.includes('De_Thi_Midterm')) {
                                friendlyName = 'Đề Thi Midterm A2-1';
                            } else if (pagePath.includes('Tu_Vung')) {
                                friendlyName = 'Kho Từ Vựng Toàn Diện';
                            } else if (pagePath.includes('kanji_a2')) {
                                friendlyName = 'Kanji & Bút Thuận A2';
                            } else if (pagePath.includes('Tong_Hop_Ngu_Phap')) {
                                friendlyName = 'Ngữ Pháp Marugoto A1–A2';
                            } else if (pagePath.includes('On_Tap_Mini_Test_A2_15_18')) {
                                friendlyName = 'Ôn Tập Bài 15–18';
                            } else if (pagePath.includes('Luyen_Tap_The_Te')) {
                                friendlyName = 'Luyện Chia Thể TE';
                            }

                            consider(`Tiếp tục học: ${friendlyName} →`, link, parsed.t);
                        }
                    }
                    // Native controllers own checkpoints outside the generic prefix.
                    const portals = {
                        marugoto_tuvung_portal_cp_v1: ['Kho từ vựng', 'Tu_Vung_Marugoto_A1_16_A2_1_10.html'],
                        marugoto_kanji_a2_cp_v1: ['Kanji & bút thuận', 'kanji_a2.html'],
                        marugoto_mini11_14_cp_v1: ['Ôn tập bài 11–14', 'tests/On_Tap_Mini_Test_A2_11_14.html'],
                        marugoto_cram_11_18_cp_v1: ['Ôn Kanji 11–18', 'tests/On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html']
                    };
                    if (portals[key]) {
                        try {
                            const saved = JSON.parse(localStorage.getItem(key));
                            if (saved) consider(`Tiếp tục học: ${portals[key][0]} →`, portals[key][1], saved.t);
                        } catch (e) {}
                    }
                    if (key && key.startsWith('marugoto_tonghop_11_18_draft_')) {
                        try {
                            const saved = JSON.parse(localStorage.getItem(key));
                            const code = key.slice('marugoto_tonghop_11_18_draft_'.length);
                            if (/^(DEGOC|M11[1-5])$/.test(code) && hasContent(saved && saved.userAnswers)) {
                                consider(`Tiếp tục đề ${code} →`, `tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html#${code}`, saved.updatedAt);
                            }
                        } catch (e) {}
                    }
                }
            } catch (e) {}

            if (latestActivity) {
                resumeBtn.href = latestActivity.url;
                resumeBtn.innerHTML = `<span>⚡ ${escapeHtml(latestActivity.title)}</span>`;
            } else {
                resumeBtn.href = 'lessons/Marugoto_A2_Lesson_1.html';
                resumeBtn.innerHTML = `<span>🚀 Chọn bài để bắt đầu học →</span>`;
            }
        }

        function escapeHtml(str) {
            const div = document.createElement('div');
            div.textContent = str;
            return div.innerHTML;
        }
    }
})();
