import os
from build_review_11_18 import build as build_review

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 1. GENERATE HTML
html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tổng ôn Marugoto A2.1 bài 11–18 · Lý thuyết, từ vựng, Kanji &amp; đề thi</title>
    <meta name="description" content="Đề ôn tập tổng hợp toàn diện Marugoto A2.1 (Bài 11–18) bám sát cấu trúc chuẩn 4 phần: Từ vựng, Hán tự Kanji, Ngữ pháp bẫy trợ từ, Đọc hiểu đời sống và Sắp xếp câu tìm dấu sao ★ kèm Audio Tokyo và giải thích chi tiết.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/css/mini-test-15-18.css?v=8">
    <link rel="stylesheet" href="../assets/css/mini-test-11-14.css?v=1">
    <link rel="stylesheet" href="../assets/css/pages/de_thi_midterm_a2_1.css?v=2">
    <link rel="stylesheet" href="../assets/css/site-theme.css?v=7">
    <link rel="stylesheet" href="../assets/css/full-exam.css?v=3">
    <link rel="stylesheet" href="../assets/css/vocab-kanji-check-11-18.css?v=2">
    <link rel="stylesheet" href="../assets/css/review-11-18.css?v=1">
    <style>
        .badge-degoc {
            background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
            color: #fff;
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.5px;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }
        .code-tab-btn.active-degoc {
            background: #b91c1c !important;
            color: #fff !important;
            border-color: #991b1b !important;
            box-shadow: 0 4px 12px rgba(185, 28, 28, 0.35) !important;
        }
    </style>
</head>
<body class="full-exam-page">

    <!-- Global Hub Navigation Placeholder -->
    <div id="navbar-placeholder"></div>

    <div class="main-container">
        <!-- Hero Banner -->
        <header class="hero-banner">
            <span class="hero-badge">MARUGOTO A2.1 · TỔNG ÔN BÀI 11–18</span>
            <h1>
                Cẩm nang &amp; Tổng ôn Marugoto A2.1 <span class="exam-hero-lessons">Bài 11–18</span>
            </h1>
            <p class="hero-desc">
                Học lý thuyết, tra từ vựng, ôn Kanji, luyện gõ và làm đề trong cùng một trang — như bộ ôn 15–18, mở rộng đủ bài 11–18. Bài tự luyện không quy đổi thành cấp độ JLPT.
            </p>
            <div class="hero-features">
                <span class="feature-pill">⏱️ Thời gian: 45 Phút</span>
                <span class="feature-pill">💯 Thang điểm: 100 (71 Câu)</span>
                <span class="feature-pill">🎯 6 Bộ Mã Đề Toàn Diện</span>
                <span class="feature-pill">🔊 Audio Phát Âm Tokyo</span>
                <span class="feature-pill">💾 Tự Động Lưu Nháp Chống Mất Bài</span>
                <a class="exam-start-link" href="#examSectionsContainer">Vào câu hỏi <span aria-hidden="true">↓</span></a>
            </div>
        </header>

        <!-- Workspace Layout with macOS-style Left Sidebar -->
        <div class="exam-workspace-layout">
            <!-- macOS Style Sidebar -->
            <aside class="exam-sidebar" aria-label="Thanh điều hướng chuyên mục">
                <div class="macos-sidebar-box">
                    <div class="macos-sidebar-header">
                        <div class="macos-traffic-dots" aria-hidden="true">
                            <span class="macos-dot macos-dot-red"></span>
                            <span class="macos-dot macos-dot-yellow"></span>
                            <span class="macos-dot macos-dot-green"></span>
                        </div>
                        <span class="macos-sidebar-title">DANH MỤC ÔN TẬP</span>
                    </div>
                    <nav class="vkc-panels" aria-label="Chọn phần ôn tập">
                        <button type="button" data-review-view="theory" aria-controls="review-theory" aria-pressed="false">
                            <span class="macos-nav-icon">📖</span><span class="macos-nav-label">Lý thuyết 11–18</span>
                        </button>
                        <button type="button" data-review-view="vocab" aria-controls="review-vocab" aria-pressed="false">
                            <span class="macos-nav-icon">🎴</span><span class="macos-nav-label">Từ vựng</span>
                        </button>
                        <button type="button" data-review-view="kanji" aria-controls="review-kanji" aria-pressed="false">
                            <span class="macos-nav-icon">⛩️</span><span class="macos-nav-label">Kanji</span>
                        </button>
                        <button type="button" id="showFullExam" aria-controls="fullExamPanel" aria-pressed="true">
                            <span class="macos-nav-icon">📝</span><span class="macos-nav-label">Đề thi · 71 câu</span>
                        </button>
                        <button type="button" id="showVocabCheck" aria-controls="vocabKanjiCheck" aria-pressed="false">
                            <span class="macos-nav-icon">⚡</span><span class="macos-nav-label">Kiểm tra nhanh</span>
                        </button>
                        <button type="button" data-review-view="typing" aria-controls="review-typing" aria-pressed="false">
                            <span class="macos-nav-icon">⌨️</span><span class="macos-nav-label">Luyện gõ câu &amp; Kanji</span>
                        </button>
                        <button type="button" data-review-view="cheatsheet" aria-controls="review-cheatsheet" aria-pressed="false">
                            <span class="macos-nav-icon">⚡</span><span class="macos-nav-label">Cẩm nang bỏ túi</span>
                        </button>
                    </nav>
                    <div class="macos-sidebar-footer" aria-hidden="true">
                        <span class="macos-status-pill"> Marugoto A2.1</span>
                        <span class="macos-badge-count">7 Mục</span>
                    </div>
                </div>
            </aside>

            <!-- Main Content Area -->
            <div class="exam-main-content">
                <!-- REVIEW_STUDY_PANEL -->
                <section class="vocab-kanji-check" id="vocabKanjiCheck" hidden aria-label="Kiểm tra Từ vựng và Kanji bài 11 đến 18">
                    <p>Đang tải bộ câu hỏi…</p>
                </section>

                <div id="fullExamPanel">
            <!-- Whiteboard Specification Card -->
            <div class="wb-spec-card">
                <div class="wb-spec-left">
                    <div class="wb-spec-icon">📋</div>
                    <div>
                        <div class="wb-spec-title">Cấu Trúc 4 Phần Chuẩn Bám Sát Giáo Trình (Bài 11 - 18)</div>
                        <div class="wb-spec-sub">
                            Bao gồm 1 Đề gốc chuyển từ tài liệu PDF chính thức và 5 mã đề tự luyện mở rộng.
                            <a href="../docs/pdf/De_on_tap_JLPT_A2_Bai_11-18.pdf" target="_blank" class="pdf-link-btn">📄 Tải / Mở File PDF Đề Gốc</a>
                        </div>
                    </div>
                </div>
                <div class="wb-spec-tags">
                    <span class="wb-part-tag tag-vocab">1. 文字・語彙: Đọc Kanji (1-10) &amp; Điền từ vựng (11-25) [25đ]</span>
                    <span class="wb-part-tag tag-grammar">2. 文法: 35 mẫu ngữ pháp cốt lõi L11 - L18 (26-60) [40đ]</span>
                    <span class="wb-part-tag tag-reading">3. 読解: 3 bài đọc hiểu đời sống &amp; công việc (8 câu) [20đ]</span>
                    <span class="wb-part-tag tag-star">4. Sắp xếp câu: Bài tập tìm dấu sao ★ (6 câu) [15đ]</span>
                </div>
            </div>

            <!-- Exam Code Selector -->
            <div class="code-selector-card">
                <span class="selector-label">CHỌN MÃ ĐỀ THI BÀI 11 - 18:</span>
                <div class="code-tab-grid" id="examCodeTabsContainer">
                    <!-- Rendered dynamically -->
                </div>
            </div>

            <!-- Exam Info Card -->
            <div class="exam-info-card" id="examInfoCard">
                <div class="exam-info-header">
                    <div>
                        <span class="exam-tag-pill" id="currentExamTag">ĐỀ GỐC</span>
                        <h2 class="exam-title-text" id="currentExamName">Ôn tập Marugoto A2.1 (Bài 11–18)</h2>
                    </div>
                    <div class="exam-actions-group">
                        <button type="button" class="btn-top-action" onclick="toggleAllExplanations()">
                            💡 <span id="toggleExplainText">Hiện Tất Cả Lời Giải</span>
                        </button>
                        <button type="button" class="btn-top-action" onclick="confirmResetExam()">
                            🔄 Làm Lại Đề Này
                        </button>
                        <button type="button" class="btn-top-action" onclick="openHistoryModal()">
                            📜 Xem Lịch Sử
                        </button>
                    </div>
                </div>
                <p class="exam-desc-text" id="currentExamDesc">
                    Mô tả đề thi...
                </p>
            </div>

            <!-- Mode Toggle Switch Bar -->
            <div class="mode-switch-card">
                <div class="mode-switch-left">
                    <span class="mode-indicator" id="modeIndicatorIcon">🎯</span>
                    <div>
                        <div class="mode-title-text" id="modeTitle">
                            Chế Độ Ôn Luyện (Hiện Lời Giải Tức Thì)
                        </div>
                        <div class="mode-desc-text" id="modeDesc">
                            Bấm chọn đáp án sẽ biết ngay đúng/sai và tự động mở khung phân tích, dịch nghĩa chi tiết.
                        </div>
                    </div>
                </div>
                <div class="mode-switch-actions">
                    <button type="button" class="btn-mode-toggle" id="btnToggleMode" onclick="toggleExamMode()">
                        ⏱️ Chuyển Sang Thi Thử (Tính Giờ 45p)
                    </button>
                </div>
            </div>

            <!-- Timer Floating Top Strip (Only visible in exam mode) -->
            <div class="timer-top-strip" id="timerStrip" style="display: none;">
                <div class="timer-strip-inner">
                    <div class="timer-display">
                        ⏱️ Thời Gian Còn Lại: <span id="timerClock">45:00</span>
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <button type="button" class="btn-timer-ctrl" id="btnTimerPause" onclick="toggleTimerPause()">
                            ⏸️ Tạm Dừng
                        </button>
                        <button type="button" class="btn-submit-quick" onclick="submitExam()">
                            📝 Nộp Bài Ngay
                        </button>
                    </div>
                </div>
            </div>

            <!-- Filter Question Palette Bar -->
            <details class="palette-card">
                <summary>📍 Bảng điều hướng 71 câu hỏi / Lọc bài làm</summary>
                <div class="palette-header">
                    <span style="font-weight: 800; font-size: 0.88rem; color: #334155;">📍 BẢNG ĐIỀU HƯỚNG 71 CÂU HỎI:</span>
                    <div class="palette-legend">
                        <span class="legend-item"><span class="legend-dot dot-unanswered"></span> Chưa làm</span>
                        <span class="legend-item"><span class="legend-dot dot-answered"></span> Đã chọn</span>
                        <span class="legend-item"><span class="legend-dot dot-correct"></span> Đúng</span>
                        <span class="legend-item"><span class="legend-dot dot-wrong"></span> Sai</span>
                    </div>
                </div>
                <div class="palette-filter-row">
                    <button type="button" class="btn-filter-tag active" id="filterBtnAll" onclick="filterPalette('all')">Tất cả (71)</button>
                    <button type="button" class="btn-filter-tag" id="filterBtnWrong" onclick="filterPalette('wrong')">Câu sai (0)</button>
                    <button type="button" class="btn-filter-tag" id="filterBtnUnanswered" onclick="filterPalette('unanswered')">Chưa làm</button>
                </div>
                <div class="palette-grid" id="paletteGridContainer">
                    <!-- Rendered dynamically -->
                </div>
            </details>

            <!-- SECTIONS CONTAINER -->
            <div id="examSectionsContainer" tabindex="-1">
                <!-- Rendered dynamically -->
            </div>

            <!-- BOTTOM FLOATING ACTION BAR -->
            <div class="bottom-action-bar">
                <div class="bottom-inner">
                    <div class="bottom-progress-info">
                        <span style="font-weight: 800; color: #1e1b4b;" id="bottomAnswerCount">Đã làm: 0/71 câu</span>
                        <div class="bottom-progress-track">
                            <div class="bottom-progress-bar" id="bottomProgressBar" style="width: 0%;"></div>
                        </div>
                    </div>
                    <div class="bottom-buttons">
                        <button type="button" class="btn-bottom-scrolltop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
                            ⬆️ Lên Đầu Trang
                        </button>
                        <button type="button" class="btn-bottom-submit" onclick="submitExam()">
                            🏁 Nộp Bài &amp; Chấm Điểm
                        </button>
                    </div>
                </div>
            </div>
        </div><!-- /fullExamPanel -->
        </div><!-- /exam-main-content -->
    </div><!-- /exam-workspace-layout -->
    </div><!-- /main-container -->

    <!-- SCORE RESULT MODAL -->
    <div class="modal-overlay" id="scoreModal" role="dialog" aria-modal="true" aria-labelledby="modalExamTitle">
        <div class="modal-card" tabindex="-1">
            <button type="button" class="modal-close-btn" onclick="closeScoreModal()">✕</button>
            
            <div class="modal-badge-row">
                <span class="modal-tag" id="modalExamTag">KẾT QUẢ THI</span>
            </div>

            <h3 style="font-size: 1.5rem; font-weight: 800; color: #1e1b4b; margin-bottom: 4px;" id="modalExamTitle">
                Kết Quả Khảo Sát Năng Lực A2.1
            </h3>
            <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 20px;">
                Hoàn thành lúc: <span id="modalTimestamp">--:--</span>
            </p>

            <div class="score-circle-container">
                <div class="score-circle-outer">
                    <div class="score-circle-inner">
                        <div class="score-big-number" id="modalScoreNumber">0</div>
                        <div class="score-max-label">/ 100 ĐIỂM</div>
                    </div>
                </div>
            </div>

            <div id="modalRatingContainer">
                <span class="modal-rating-pill rating-green" id="modalRatingPill">XUẤT SẮC</span>
            </div>

            <div class="score-breakdown-grid" id="modalBreakdownGrid">
                <!-- Breakdown cards rendered dynamically -->
            </div>

            <p style="font-size: 0.92rem; color: #475569; margin-bottom: 24px; line-height: 1.6;" id="modalFeedbackMsg">
                Chúc mừng bạn đã hoàn thành bài thi! Toàn bộ câu hỏi đã được mở khóa lời giải thích và đáp án chi tiết.
            </p>

            <div class="modal-actions">
                <button type="button" class="btn-modal-action btn-modal-review" onclick="enterReviewMode()">
                    🔍 Xem Lại Toàn Bộ Bài Làm &amp; Lời Giải
                </button>
                <button type="button" class="btn-modal-action btn-modal-retry" onclick="confirmResetExam()">
                    🔄 Làm Lại Mã Đề Này
                </button>
            </div>
        </div>
    </div>

    <!-- HISTORY MODAL -->
    <div class="modal-overlay" id="historyModal" role="dialog" aria-modal="true" aria-labelledby="historyTitle">
        <div class="modal-card" tabindex="-1">
            <button type="button" class="modal-close-btn" onclick="closeHistoryModal()">✕</button>
            <h3 id="historyTitle" style="font-size: 1.3rem; font-weight: 800; color: #1e1b4b; margin-bottom: 6px;">📜 Lịch Sử Làm Bài Thi Bài 11 - 18</h3>
            <p style="font-size: 0.86rem; color: #64748b; margin-bottom: 16px;">Danh sách kết quả các lần thi của bạn trên trình duyệt này:</p>
            
            <div class="history-list" id="historyListContainer">
                <!-- Rendered dynamically -->
            </div>

            <div class="modal-actions" style="margin-top: 16px;">
                <button type="button" class="btn-modal-action btn-modal-retry" onclick="clearAllHistory()">
                    🗑️ Xóa Lịch Sử
                </button>
                <button type="button" class="btn-modal-action btn-modal-review" onclick="closeHistoryModal()">
                    Đóng
                </button>
            </div>
        </div>
    </div>

    <!-- TOAST NOTIFICATION -->
    <div class="toast-notify" id="toastNotify" role="status" aria-live="polite">
        <span id="toastIcon">💾</span>
        <span id="toastMsg">Đã tự động lưu nháp bài làm</span>
    </div>

    <!-- AUDIO ENGINE (Dual Tokyo Speech) -->
    <script src="../assets/js/audio-engine.js?v=2"></script>

    <!-- EXAMS DATA & CONTROLLER JS -->
    <script src="../assets/data/de_thi_tong_hop_11_18_data.js?v=1"></script>
    <script src="../assets/data/vocab_kanji_check_11_18_data.js?v=1"></script>
    <script src="../assets/js/pages/de_thi_tong_hop_11_18.js?v=2"></script>
    <script src="../assets/data/review_11_18_data.js?v=1"></script>
    <script src="../assets/js/pages/review-11-18.js?v=1"></script>
    <script src="../assets/js/jp-typing-grader.js?v=2"></script>
    <script src="../assets/js/typing-studio.js?v=9"></script>
    <script src="../assets/js/pages/vocab-kanji-check-11-18.js?v=4"></script>
    <script src="../assets/nav.js?v=7" defer></script>
</body>
</html>
"""

html_path = os.path.join(WORKSPACE, "tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html")
html_content = html_content.replace("<!-- REVIEW_STUDY_PANEL -->", build_review())
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated HTML at:", html_path)
