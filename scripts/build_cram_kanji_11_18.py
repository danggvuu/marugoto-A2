import json
import os

WORKSPACE = '/Users/dangvu/Downloads/nhật'

with open(os.path.join(WORKSPACE, 'data/kanji_vocab_11_18.json'), 'r', encoding='utf-8') as f:
    vocab_list = json.load(f)

# Build HTML content
vocab_json_str = json.dumps(vocab_list, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ Đấu Trường Ôn Tập Cấp Tốc Đêm Nay: 121 Từ Kanji Bài 11 ➔ 18 & NPBS Bài 14</title>
    <meta name="description" content="Chuyên trang ôn luyện thần tốc: 121 hợp từ Kanji Lessons 11-18, chế độ Flashcard Cram, mẹo nhớ 6 chuỗi chữ Hán, ngữ pháp bổ sung Bài 14 và đề thi đột kích 20 câu.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <script src="../assets/js/audio-engine.js?v=2"></script>
    <link rel="stylesheet" href="../assets/css/cram-kanji.css?v=1">
</head>
<body>

<div class="container">
    <!-- Global Navigation -->
    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🏠 Trang Chủ</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể Từ Điển</a>
        <a href="../the_ta.html" class="hub-nav-item">📙 Thể Ta</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Kanji A2</a>
        <a href="../kien_thuc_bo_sung.html" class="hub-nav-item">💡 Kiến Thức Bổ Sung</a>
        <a href="On_Tap_Mini_Test_A2_11_14.html" class="hub-nav-item">🎯 Mini Test 11-14</a>
        <a href="On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html" class="hub-nav-item active-hub">⚡ Cấp Tốc Đêm Nay (L11-18)</a>
    </div>

    <!-- Hero Header -->
    <header class="hero-banner">
        <div class="hero-badge">🔥 CRAMMING STATION • HỌC CẤP TỐC ĐÊM NAY • BÀI 11 ➔ 18</div>
        <h1 class="hero-title">⚡ Đấu Trường Ôn Tập Cấp Tốc Đêm Nay:<br>121 Hợp Từ Kanji & NPBS Bài 14</h1>
        <p class="hero-desc">Trang bị toàn bộ vũ khí nhét kiến thức vào đầu trong đêm: Copy Quizlet 1-Click theo từng bài, Lật Flashcard Cram cấp tốc, 6 Chuỗi Hack não chữ Hán và Thử thách phản xạ NPBS 14 chuẩn thi cử.</p>
        
        <div class="hero-stats">
            <div class="stat-pill">🎴 121 Hợp Từ Kanji</div>
            <div class="stat-pill">📚 8 Bài Học (L11 ➔ L18)</div>
            <div class="stat-pill">⚡ 2 Mẫu NPBS Bài 14</div>
            <div class="stat-pill">🎯 20 Câu Test Đột Kích</div>
        </div>

        <div class="hero-actions">
            <button type="button" class="btn-cram-action btn-indigo" onclick="switchMainTab('tab-typing')" style="background: linear-gradient(135deg, #4f46e5, #7c3aed); color: #fff; font-weight: 800;">
                ⌨️ Luyện Gõ 121 Kanji (Theo Bài 11-18)
            </button>
            <button type="button" class="btn-cram-action btn-purple" onclick="copyAllQuizletTab()">
                📋 Copy Quizlet Toàn Bộ (121 từ)
            </button>
            <button type="button" class="btn-cram-action btn-green" onclick="copyAllColonFormat()">
                📋 Copy Dấu Hai Chấm (121 từ)
            </button>
            <button type="button" class="btn-cram-action btn-amber" onclick="switchMainTab('tab-cram')">
                ⚡ Lật Thẻ Cram Mode
            </button>
            <button type="button" class="btn-cram-action btn-sky" onclick="switchMainTab('tab-npbs')">
                🎯 Thử Thách NPBS 14
            </button>
        </div>
    </header>

    <!-- Sticky Tab Navigation -->
    <div class="tab-nav-wrapper">
        <nav class="tab-nav">
            <button class="tab-btn active" onclick="switchMainTab('tab-vocab')">🎴 121 Từ Vựng (L11-18)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-typing')">⌨️ Luyện Gõ 121 Kanji (L11-18)</button>
            <button class="tab-btn" onclick="switchMainTab('tab-cram')">⚡ Flashcard Cram Mode</button>
            <button class="tab-btn" onclick="switchMainTab('tab-hack')">🧠 Hack Não 6 Chuỗi Kanji</button>
            <button class="tab-btn" onclick="switchMainTab('tab-npbs')">⚡ NPBS Bài 14 & Thử Thách</button>
            <button class="tab-btn" onclick="switchMainTab('tab-test')">🎯 Đề Thi Đột Kích 20 Câu</button>
        </nav>
    </div>

    <!-- ========================================== -->
    <!-- TAB 1: 121 TỪ VỰNG KANJI BÀI 11-18        -->
    <!-- ========================================== -->
    <div id="tab-vocab" class="tab-panel active">
        <div class="toolbar-card">
            <div class="filter-row">
                <span style="font-size: 0.85rem; font-weight: 800; color: var(--gray-600); margin-right: 4px;">CHỌN BÀI:</span>
                <button class="filter-btn active" onclick="filterVocabByLesson('ALL', this)">🌟 Tất Cả (121 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(11, this)">Bài 11 (15 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(12, this)">Bài 12 (18 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(13, this)">Bài 13 (22 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(14, this)">Bài 14 (16 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(15, this)">Bài 15 (15 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(16, this)">Bài 16 (14 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(17, this)">Bài 17 (10 từ)</button>
                <button class="filter-btn" onclick="filterVocabByLesson(18, this)">Bài 18 (11 từ)</button>
            </div>
            <div class="action-row">
                <div class="search-box">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="vocabSearchInput" class="search-input" placeholder="Tìm theo Kanji, Hiragana, tiếng Việt (VD: 料理, りょうり, món ăn)..." oninput="handleSearch()">
                </div>
                <button type="button" class="btn-cram-action btn-purple" onclick="copyCurrentFilteredQuizlet()" style="padding: 9px 16px; font-size: 0.88rem;">
                    📋 Copy Quizlet (<span id="currentFilteredCount">121</span> từ)
                </button>
                <button type="button" class="btn-cram-action btn-green" onclick="copyCurrentFilteredColon()" style="padding: 9px 16px; font-size: 0.88rem;">
                    📋 Copy Dấu (：)
                </button>
                <button type="button" class="btn-cram-action btn-amber" onclick="toggleHideMeaning()" id="btnHideMeaning" style="padding: 9px 16px; font-size: 0.88rem;">
                    👁️ Ẩn nghĩa (Tự dò)
                </button>
            </div>
        </div>

        <div class="vocab-grid" id="vocabContainer">
            <!-- Render via JS -->
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB: LUYỆN GÕ 121 KANJI BÀI 11 - 18        -->
    <!-- ========================================== -->
    <div id="tab-typing" class="tab-panel">
        <div class="toolbar-card" style="margin-bottom: 20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
                <div>
                    <h2 style="font-size: 1.45rem; font-weight: 900; color: #1e1b4b; margin: 0 0 4px 0;">⌨️ Phòng Luyện Gõ Phản Xạ 121 Kanji Bài 11 ➔ 18</h2>
                    <p style="color: var(--gray-600); margin: 0; font-size: 0.92rem;">Nhìn mặt chữ Hán Kanji ➔ Gõ cách đọc Hiragana theo từng bài học (11-18). Tự động chấm điểm, phát âm Tokyo và hiển thị mẹo nhớ!</p>
                </div>
            </div>

            <!-- Chọn chế độ luyện gõ -->
            <div class="tp-mode-switch" role="tablist" aria-label="Chế độ luyện gõ" style="margin-top: 14px;">
                <button type="button" class="tp-mode-pill active" id="tpModeBtn_kanji" onclick="switchTypingMode('kanji')">⛩️ Chữ Hán (Kanji) ➔ Gõ Hiragana (121 từ)</button>
                <button type="button" class="tp-mode-pill" id="tpModeBtn_sentence" onclick="switchTypingMode('sentence')">🇻🇳 Câu Tiếng Việt ➔ Gõ Hiragana (112 câu)</button>
                <button type="button" class="tp-mode-pill" id="tpModeBtn_vocab" onclick="switchTypingMode('vocab')">🗂️ Từ Vựng A2 (135 từ)</button>
            </div>

            <!-- Bộ lọc bài học + Công cụ -->
            <div class="tp-toolbar" style="margin-top: 14px;">
                <div class="vocab-filter-group" id="typingFilterGroup"></div>
                <div class="tp-toggles">
                    <label id="tpKanjiAllowWrap" style="display:none;" title="Nếu quên tắt bộ gõ Kanji vẫn chấp nhận nếu khớp mặt chữ chuẩn">
                        <input type="checkbox" id="tpAllowKanjiToggle" onchange="toggleTypingOption('allowKanji', this.checked)"> Cho phép kèm Kanji
                    </label>
                    <label title="Tự động nhảy câu/chữ khi gõ đúng">
                        <input type="checkbox" id="tpAutoAdvToggle" onchange="toggleTypingOption('autoAdvance', this.checked)"> Tự nhảy khi đúng
                    </label>
                    <button type="button" class="vocab-action-btn" onclick="toggleTypingOverview()" id="tpOverviewBtn">📋 Danh Sách Chữ</button>
                    <button type="button" class="vocab-action-btn" onclick="shuffleTypingPool()">🔀 Xáo Trộn</button>
                </div>
            </div>
        </div>

        <!-- Danh sách chữ thu gọn -->
        <div class="tp-overview-drawer" id="tpOverviewDrawer"></div>

        <!-- Khung thẻ luyện gõ chính -->
        <div class="typing-card-view">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; gap:8px; flex-wrap:wrap;">
                <span style="font-size:0.84rem; font-weight:800; color:var(--primary); background:rgba(79,70,229,0.1); padding:4px 12px; border-radius:var(--radius-full);" id="tpCardBadge">Chữ Hán 1 / --</span>
                <span class="tp-pattern-badge" id="tpPatternBadge">Bài 11</span>
                <div class="typing-streak" id="tpStreakBadge" style="margin:0;">🔥 Chuỗi: 0</div>
            </div>

            <div id="tpPromptArea" style="background:linear-gradient(135deg,#f8fafc 0%,#eef2ff 100%); border:1px solid #c7d2fe; border-radius:var(--radius-md); padding:20px 18px; margin:12px 0 18px 0;">
                <div style="font-size:0.8rem; font-weight:700; color:var(--gray-500); text-transform:uppercase; letter-spacing:0.04em;" id="tpPromptSubtitle">NHÌN CHỮ HÁN (KANJI) — GÕ CÁCH ĐỌC HIRAGANA</div>
                <div class="tp-kanji-hero jp-text" id="tpPromptVi">Đang tải...</div>
                <div id="tpHintPreview" style="display:none; margin-top:10px; padding:8px 12px; background:#ffffff; border-radius:8px; font-size:0.88rem; color:var(--primary-dark); border:1px dashed #a5b4fc;"></div>
            </div>

            <div style="font-size:0.86rem; font-weight:700; color:var(--gray-600); margin-bottom:8px;" id="tpInputDirective">
                ⬇️ Nhập <strong>cách đọc Hiragana</strong> của chữ Hán trên rồi nhấn Enter:
            </div>

            <input type="text" class="typing-input-large jp-text" id="tpCardInput" placeholder="Nhập cách đọc Hiragana rồi nhấn Enter..." autocomplete="off" autocapitalize="off" spellcheck="false">

            <div class="typing-actions">
                <button type="button" class="btn-primary" style="background:var(--gray-500);" onclick="prevTypingItem()">⬅️ Trước</button>
                <button type="button" class="btn-primary" id="tpCardCheckBtn" onclick="handleTypingPrimaryBtn()">Kiểm Tra Đáp Án ⏎</button>
                <button type="button" class="btn-primary" id="tpCardRetryBtn" style="background:#0284c7; display:none;" onclick="retryCurrentTypingCard()">🔄 Gõ Lại Từ Này (Esc)</button>
                <button type="button" class="btn-primary" id="tpCardSpeakBtn" style="background:#0ea5e9;" onclick="speakCurrentTypingWord(this)">🔊 Nghe Mẫu</button>
                <button type="button" class="btn-primary" style="background:var(--purple);" onclick="showTypingHint()">💡 Gợi Ý</button>
                <button type="button" class="btn-primary" style="background:var(--warning);" onclick="revealTypingAnswer()">👁️ Xem Đáp Án</button>
                <button type="button" class="btn-primary" style="background:var(--gray-600);" onclick="skipTypingWord()">Tiếp Theo ➔</button>
                <button type="button" class="btn-primary" style="background:#be123c;" onclick="resetCurrentTypingMode()">🔄 Làm Lại Chế Độ Này</button>
            </div>

            <!-- Bảng giải thích chi tiết (Nghĩa + So sánh + Vì sao sai) -->
            <div id="tpDetailPanel" class="tp-detail-panel"></div>

            <div style="width:100%; height:10px; background:var(--gray-200); border-radius:10px; overflow:hidden; margin: 22px 0 12px 0;">
                <div id="tpProgressBar" style="width:0%; height:100%; background:linear-gradient(90deg, var(--primary), var(--secondary)); transition:width 0.3s;"></div>
            </div>

            <div style="display:flex; justify-content:space-around; flex-wrap:wrap; gap:10px; font-size:0.95rem; font-weight:700; color:var(--gray-700);">
                <span>✅ Đã làm đúng: <strong style="color:var(--success);" id="tpStatCorrect">0</strong></span>
                <span>❌ Cần luyện thêm: <strong style="color:var(--accent);" id="tpStatWrong">0</strong></span>
                <span>🎯 Đã chạm / tổng: <strong style="color:var(--primary);" id="tpStatPercent">0%</strong></span>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 2: FLASHCARD CRAM MODE                -->
    <!-- ========================================== -->
    <div id="tab-cram" class="tab-panel">
        <div class="cram-box">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <span class="badge-lesson" id="cramLessonBadge">Bài 11</span>
                <span style="font-weight: 800; color: var(--gray-600);" id="cramProgressText">1 / 121</span>
                <span class="badge-group" id="cramGroupBadge">Ẩm thực</span>
            </div>

            <div class="flashcard-scene" onclick="flipCurrentCard()">
                <div class="flashcard" id="mainFlashcard">
                    <div class="card-face card-front">
                        <div class="cram-kanji jp-text" id="cramFrontKanji">お酒</div>
                        <div class="cram-hint">👆 Chạm hoặc bấm Space để lật xem cách đọc & nghĩa</div>
                    </div>
                    <div class="card-face card-back">
                        <div class="cram-kana jp-text" id="cramBackKana">おさけ</div>
                        <div class="cram-vi" id="cramBackVi">Rượu, đồ có cồn</div>
                        <button type="button" class="btn-cram-action btn-sky" onclick="event.stopPropagation(); speakCramWord()" style="margin-top: 14px; padding: 6px 16px; font-size: 0.85rem;">
                            🔊 Nghe phát âm
                        </button>
                    </div>
                </div>
            </div>

            <div class="cram-controls">
                <button type="button" class="btn-cram-ctrl btn-prev" onclick="prevCramCard()">⬅️ Trước</button>
                <button type="button" class="btn-cram-ctrl btn-flip" onclick="flipCurrentCard()">🔄 Lật Thẻ (Space)</button>
                <button type="button" class="btn-cram-ctrl btn-next" onclick="nextCramCard()">Kế tiếp ➡️</button>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 3: HACK NÃO 6 CHUỖI KANJI THẦN THÁNH   -->
    <!-- ========================================== -->
    <div id="tab-hack" class="tab-panel">
        <div class="toolbar-card">
            <h2 style="font-size: 1.5rem; font-weight: 900; color: #1e1b4b; margin-bottom: 8px;">🧠 6 Chuỗi Kanji Xâu Chuỗi: Nhớ Trọn 121 Từ Trong 30 Phút</h2>
            <p style="color: var(--gray-600); margin-bottom: 22px;">Quy tắc vàng để nhét vào đầu trong đêm: Học theo chuỗi liên kết các từ ghép (Compounds) dùng chung gốc chữ Hán.</p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 18px;">
                <!-- Chuỗi 1 -->
                <div style="background: #faf5ff; border: 1.5px solid #d8b4fe; border-radius: 14px; padding: 18px;">
                    <h3 style="color: #6b21a8; font-size: 1.15rem; font-weight: 800; margin-bottom: 10px;">🍶 1. Chuỗi Rượu, Trà & Đồ Vật (Bài 11)</h3>
                    <ul style="padding-left: 20px; line-height: 1.8; color: #374151;">
                        <li><strong>酒 (TỬU)</strong>: お酒 (おさけ - rượu) ➔ 日本酒 (にほんしゅ - rượu Nhật)</li>
                        <li><strong>作 (TÁC)</strong>: 作ります (つくります - làm) ➔ 作文 (さくぶん - bài văn)</li>
                        <li><strong>物 (VẬT)</strong>: 食べ物 (たべもの) ➔ 飲み物 (のみもの) ➔ 乗り物 (のりもの) ➔ 荷物 (にもつ)</li>
                        <li><strong>茶 (TRÀ)</strong>: お茶 (おちゃ - trà) ➔ 喫茶店 (きっさてん - quán cà phê)</li>
                        <li><strong>持 (TRÌ)</strong>: 持ちます (もちます - cầm) ➔ 気持ち (きもち - tâm trạng)</li>
                        <li><strong>願 (NGUYỆN)</strong>: お願い (おねがい) ➔ お願いします ➔ 願い事 (ねがいごと)</li>
                    </ul>
                </div>

                <!-- Chuỗi 2 -->
                <div style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 14px; padding: 18px;">
                    <h3 style="color: #15803d; font-size: 1.15rem; font-weight: 800; margin-bottom: 10px;">🍜 2. Chuỗi Liệu, Lý, Vị & Trung (Bài 12)</h3>
                    <ul style="padding-left: 20px; line-height: 1.8; color: #374151;">
                        <li><strong>料 (LIỆU)</strong>: 料理 (りょうり - món ăn) ➔ 料金 (りょうきん - phí) ➔ 無料 (むりょう - miễn phí) ➔ 資料 (しりょう - tài liệu)</li>
                        <li><strong>理 (LÝ)</strong>: 料理 ➔ 理由 (りゆう - lý do) ➔ 無理 (むり - quá sức)</li>
                        <li><strong>味 (VỊ)</strong>: 味 (あじ - vị) ➔ 地味 (じみ - giản dị)</li>
                        <li><strong>中 (TRUNG)</strong>: 中 (なか) ➔ 仕事中 (しごとちゅう) ➔ 一年中 (いちねんじゅう) ➔ 中止 (ちゅうし)</li>
                        <li><strong>入 (NHẬP)</strong>: 入ります (はいります) ➔ 入れます (いれます) ➔ 入学 (にゅうがく)</li>
                    </ul>
                </div>

                <!-- Chuỗi 3 -->
                <div style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 18px;">
                    <h3 style="color: #1d4ed8; font-size: 1.15rem; font-weight: 800; margin-bottom: 10px;">🏢 3. Chuỗi Hội, Xã, Xuất & Trước (Bài 13)</h3>
                    <ul style="padding-left: 20px; line-height: 1.8; color: #374151;">
                        <li><strong>会・社 (HỘI - XÃ)</strong>: 会います ➔ 社会 (しゃかい) ➔ 会社員 (かいしゃいん) ➔ 本社 (ほんしゃ) ➔ 支社 (ししゃ) ➔ 入社 (にゅうしゃ) ➔ 神社 (じんじゃ)</li>
                        <li><strong>出 (XUẤT)</strong>: 出ます ➔ 出します ➔ 出かけます ➔ 出口 (でぐち) ➔ 出張 (しゅっちょう) ➔ 出発 (しゅっぱつ)</li>
                        <li><strong>着 (TRƯỚC)</strong>: 到着 (とうちゃく - đến nơi) ➔ 着きます (つきます) ➔ 着ます (きます - mặc) ➔ 着物 (きもの)</li>
                        <li><strong>空・港 (KHÔNG - CẢNG)</strong>: 空 (そら) ➔ 空気 (くうき) ➔ 港 (みなと) ➔ 空港 (くうこう)</li>
                    </ul>
                </div>

                <!-- Chuỗi 4 -->
                <div style="background: #fffbeb; border: 1.5px solid #fde68a; border-radius: 14px; padding: 18px;">
                    <h3 style="color: #b45309; font-size: 1.15rem; font-weight: 800; margin-bottom: 10px;">🚗 4. Chuỗi Tự, Xa & Điện Khí (Bài 14)</h3>
                    <ul style="padding-left: 20px; line-height: 1.8; color: #374151;">
                        <li><strong>自 (TỰ)</strong>: 自分 (じぶん) ➔ 自由 (じゆう) ➔ 自然 (しぜん) ➔ 自動車 (じどうしゃ) ➔ 自転車 (じてんしゃ)</li>
                        <li><strong>車 (XA)</strong>: 車 (くるま) ➔ 自動車 ➔ 自転車 ➔ 電車 (でんしゃ)</li>
                        <li><strong>電 (ĐIỆN)</strong>: 電話 (でんわ) ➔ 電車 (でんしゃ) ➔ 電子レンジ ➔ 電気 (でんき)</li>
                        <li><strong>気 (KHÍ)</strong>: 電気 ➔ 病気 (びょうき) ➔ 人気 (にんき) ➔ 空気 (くうき)</li>
                        <li><strong>使・借・送</strong>: 使います (つかいます) ➔ 大使館 (たいしかん) ➔ 借ります (かります) ➔ 送ります (おくります)</li>
                    </ul>
                </div>

                <!-- Chuỗi 5 -->
                <div style="background: #fdf2f8; border: 1.5px solid #fbcfe8; border-radius: 14px; padding: 18px;">
                    <h3 style="color: #be185d; font-size: 1.15rem; font-weight: 800; margin-bottom: 10px;">🏃 5. Chuỗi Thể, Thủ, Túc & Vận Động (Bài 15-16)</h3>
                    <ul style="padding-left: 20px; line-height: 1.8; color: #374151;">
                        <li><strong>体 (THỂ)</strong>: 体 (からだ) ➔ 全体 (ぜんたい)</li>
                        <li><strong>手 (THỦ)</strong>: 手 (て) ➔ 上手 (じょうず) ➔ 下手 (へた) ➔ 歌手 (かしゅ) ➔ 運転手 (うんてんしゅ)</li>
                        <li><strong>足 (TÚC)</strong>: 足 (あし - chân) ➔ 足ります (たります - đủ)</li>
                        <li><strong>毎 (MỖI)</strong>: 毎日 ➔ 毎朝 ➔ 毎週 ➔ 毎月 (まいつき/まいげつ) ➔ 週末 (しゅうまつ)</li>
                        <li><strong>外 (NGOẠI)</strong>: 外 (そと) ➔ 外国 (がいこく) ➔ 外食 (がいしょく)</li>
                        <li><strong>泳 (VỊNH)</strong>: 泳ぎます (およぎます) ➔ 水泳 (すいえい)</li>
                    </ul>
                </div>

                <!-- Chuỗi 6 -->
                <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 18px;">
                    <h3 style="color: #334155; font-size: 1.15rem; font-weight: 800; margin-bottom: 10px;">📅 6. Chuỗi Niên, Kế, Gia & Tư (Bài 17-18)</h3>
                    <ul style="padding-left: 20px; line-height: 1.8; color: #374151;">
                        <li><strong>計 (KẾ)</strong>: 計ります (はかります) ➔ 時計 (とけい) ➔ 会計 (かいけい)</li>
                        <li><strong>真 (CHÂN)</strong>: 写真 (しゃしん) ➔ 真面目 (まじめ - chăm chỉ)</li>
                        <li><strong>年 (NIÊN)</strong>: 去年 (きょねん) ➔ 今年 (ことし) ➔ 来年 (らいねん)</li>
                        <li><strong>今 (KIM)</strong>: 今朝 (けさ) ➔ 今月 (こんげつ) ➔ 今年 (ことし)</li>
                        <li><strong>家 (GIA)</strong>: 家 (いえ) ➔ 家族 (かぞく) ➔ 作家 (さっか) ➔ 画家 (がか)</li>
                        <li><strong>思 (TƯ)</strong>: 思います (おもいます - nghĩ)</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: NPBS BÀI 14 & THỬ THÁCH THỰC CHIẾN  -->
    <!-- ========================================== -->
    <div id="tab-npbs" class="tab-panel">
        <div class="toolbar-card" style="border: 2px solid #8b5cf6;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
                <h2 style="font-size: 1.5rem; font-weight: 900; color: #581c87;">⚡ Ngữ Pháp Bổ Sung Trọng Tâm Bài 14 (NPBS)</h2>
                <span class="badge-lesson" style="font-size:0.85rem; padding:6px 14px;">Trọng Điểm Thi Cử</span>
            </div>

            <!-- Cấu trúc 1 -->
            <div style="background:#f5f3ff; border: 1.5px solid #ddd6fe; border-radius: 14px; padding: 20px; margin-bottom: 20px;">
                <h3 style="color:#6d28d9; font-size:1.15rem; margin-bottom:8px;">🌸 1. Đã làm V được … (thời gian): V て　～ 年／～か月　に　なります。</h3>
                <p style="color:#374151; margin-bottom: 12px; font-size:0.95rem;">
                    <strong>Bản chất:</strong> Diễn tả khoảng thời gian kể từ khi một hành động hoặc mốc sự kiện bắt đầu diễn ra cho tới hiện tại. Động từ chia <strong>thể Te (V-て)</strong> và trợ từ đứng trước <code>なります</code> luôn là <strong>に</strong>.
                </p>
                <div style="background:#ffffff; border-radius:10px; padding:14px; border:1px solid #e9d5ff;">
                    <div style="margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span class="jp-text" style="font-size:1.05rem; font-weight:700; color:#4c1d95;">この 会社に 入って 10年 に なります。</span>
                            <div style="color:#6b7280; font-size:0.9rem;">➡ Đã 10 năm kể từ khi tôi vào công ty này. (Tôi vào công ty này được 10 năm rồi).</div>
                        </div>
                        <button type="button" class="btn-card-action" onclick="audioEngine.speak('この会社に入って10年になります')">🔊</button>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span class="jp-text" style="font-size:1.05rem; font-weight:700; color:#4c1d95;">日本語の 勉強を はじめて 3か月 に なります。</span>
                            <div style="color:#6b7280; font-size:0.9rem;">➡ Đã 3 tháng kể từ khi tớ bắt đầu học tiếng Nhật. (Tớ đã bắt đầu học tiếng Nhật được 3 tháng rồi).</div>
                        </div>
                        <button type="button" class="btn-card-action" onclick="audioEngine.speak('日本語の勉強をはじめて3か月になります')">🔊</button>
                    </div>
                </div>
            </div>

            <!-- Cấu trúc 2 -->
            <div style="background:#f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 14px; padding: 20px; margin-bottom: 24px;">
                <h3 style="color:#15803d; font-size:1.15rem; margin-bottom:8px;">🌸 2. Tôi làm V được không?: （？）V ても　いいですか。</h3>
                <p style="color:#374151; margin-bottom: 12px; font-size:0.95rem;">
                    <strong>Quy tắc đối đáp chuẩn:</strong><br>
                    • ☺ Đồng ý: <strong>「はい、いいですよ。」</strong> ／ <strong>「はい、どうぞ。」</strong><br>
                    • ☹ Từ chối khéo: <strong>「すみません…〈kèm lý do〉」</strong> (tránh dùng だめです thô lỗ)<br>
                    • ☆ Dạng khẳng định cho phép: <strong>V ても　いいです。</strong> ➡ Được phép làm V; Làm V cũng được
                </p>
                <div style="background:#ffffff; border-radius:10px; padding:14px; border:1px solid #dcfce7;">
                    <div style="margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span class="jp-text" style="font-size:1.05rem; font-weight:700; color:#166534;">すみません。ペンを 借りても いいですか。―― はい、どうぞ。</span>
                            <div style="color:#6b7280; font-size:0.9rem;">➡ Xin lỗi. Tớ có thể mượn bút được không? ―― Vâng, bạn cứ tự nhiên lấy nhé.</div>
                        </div>
                        <button type="button" class="btn-card-action" onclick="audioEngine.speak('すみません。ペンを借りてもいいですか。はい、どうぞ。')">🔊</button>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span class="jp-text" style="font-size:1.05rem; font-weight:700; color:#166534;">先生、テストの とき、辞書を 使っても いいですか。</span>
                            <div style="color:#6b7280; font-size:0.9rem;">➡ Sensei ơi, trong khi làm bài kiểm tra, em có thể sử dụng từ điển được không ạ?</div>
                        </div>
                        <button type="button" class="btn-card-action" onclick="audioEngine.speak('先生、テストのとき、辞書を使ってもいいですか。')">🔊</button>
                    </div>
                </div>
            </div>

            <!-- 10 CÂU THỬ THÁCH NPBS TƯƠNG TÁC -->
            <div style="background: linear-gradient(135deg, #4f46e5, #7c3aed); border-radius: var(--radius-lg); padding: 24px; color: #ffffff;">
                <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 4px;">🎯 10 CÂU THỬ THÁCH PHẢN XẠ NPBS BÀI 14</h3>
                <p style="font-size: 0.92rem; opacity: 0.9; margin-bottom: 18px;">Chọn đáp án chính xác để kiểm tra độ nhạy của phản xạ ngữ pháp ngay lập tức.</p>

                <div id="npbsChallengeList">
                    <!-- Populated via JS -->
                </div>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 5: ĐỀ THI ĐỘT KÍCH 20 CÂU (SPEED TEST) -->
    <!-- ========================================== -->
    <div id="tab-test" class="tab-panel">
        <div class="toolbar-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
                <div>
                    <h2 style="font-size: 1.5rem; font-weight: 900; color: #1e1b4b;">🎯 Đề Thi Đột Kích 20 Câu (100 Điểm)</h2>
                    <p style="color: var(--gray-600); margin-top: 4px;">Kiểm tra tổng hợp 121 Kanji + Ngữ pháp bổ sung Bài 14 trước khi đi ngủ.</p>
                </div>
                <div style="font-size: 1.1rem; font-weight: 800; background: #e0f2fe; color: #0369a1; padding: 8px 18px; border-radius: var(--radius-full);">
                    Điểm: <span id="speedTestScore">0</span> / 100
                </div>
            </div>

            <div id="speedTestContainer">
                <!-- Populated via JS -->
            </div>

            <div style="margin-top: 24px; text-align: center;">
                <button type="button" class="btn-cram-action btn-purple" onclick="finishSpeedTest()" style="padding: 12px 36px; font-size: 1.05rem;">
                    🚀 Chấm Điểm & Nộp Bài Đột Kích
                </button>
            </div>
        </div>
    </div>
</div>

<div id="toast" class="toast"></div>

<script src="../assets/data/mini_15_18_data.js?v=2"></script>
<script src="../assets/js/jp-typing-grader.js?v=2"></script>
<script src="../assets/js/typing-studio.js?v=5"></script>
<script src="../assets/data/cram_kanji_data.js?v=1"></script>
<script src="../assets/js/cram-kanji.js?v=2"></script>
<script src="../assets/nav.js?v=6" defer></script>
</body>
</html>
"""

os.makedirs(os.path.join(WORKSPACE, "assets/data"), exist_ok=True)
cram_data_path = os.path.join(WORKSPACE, "assets/data/cram_kanji_data.js")
with open(cram_data_path, "w", encoding="utf-8") as df:
    df.write(f"window.CRAM_11_18_VOCAB = {vocab_json_str};\n")
output_path = os.path.join(WORKSPACE, "tests/On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Generated {output_path} ({len(html)} bytes) and {cram_data_path}")
