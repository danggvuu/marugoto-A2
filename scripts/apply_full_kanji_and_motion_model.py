# -*- coding: utf-8 -*-
"""
apply_full_kanji_and_motion_model.py
Injects:
1. Complete enriched vocabulary (1,217 words with kanji, kana, hv, romaji, kanji_chars)
2. Upgraded Table columns (STT | Bài | Kanji | Kana | Hán Việt | Tiếng Việt | ✍️ Nét & Phát Âm)
3. Upgraded 3D Flashcards with Kanji, Kana, Hán Việt, and quick motion model button
4. Interactive KanjiVG Stroke Animation Motion Model Modal
5. Floating Mini Stroke Motion Model Widget
6. Search debounced across Kanji, Kana, Hán Việt, Romaji, and Vietnamese
into Tu_Vung_Marugoto_A1_16_A2_1_10.html
"""

import json
import re

with open('master_vocab_enriched.json', 'r', encoding='utf-8') as f:
    master_vocab = json.load(f)

with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Table header
old_table_header = '''                <thead>
                    <tr>
                        <th class="col-stt">STT</th>
                        <th class="col-lesson">Bài</th>
                        <th class="col-jp">Tiếng Nhật</th>
                        <th class="col-vi">Ý Nghĩa Tiếng Việt</th>
                    </tr>
                </thead>'''

new_table_header = '''                <thead>
                    <tr>
                        <th class="col-stt">STT</th>
                        <th class="col-lesson">Bài</th>
                        <th class="col-kanji">Chữ Hán (Kanji)</th>
                        <th class="col-kana">Cách Đọc (Kana)</th>
                        <th class="col-hv">Âm Hán Việt</th>
                        <th class="col-vi">Ý Nghĩa Tiếng Việt</th>
                        <th class="col-actions">✍️ Nét & Âm Thanh</th>
                    </tr>
                </thead>'''

if old_table_header in html:
    html = html.replace(old_table_header, new_table_header)
    print("Replaced table header successfully!")
else:
    print("WARNING: Table header not found directly, checking regex...")
    html = re.sub(
        r'<table class="vocab-table">\s*<thead>\s*<tr>.*?</tr>\s*</thead>',
        f'<table class="vocab-table">\n{new_table_header}',
        html,
        flags=re.DOTALL
    )

# 2. Add Motion Model CSS
motion_css = '''
    /* =====================================================
       KANJI STROKE ANIMATION MOTION MODEL & ENRICHED VOCAB STYLES
       ===================================================== */
    .col-kanji {
        width: 18%;
        font-family: "Hiragino Mincho ProN", "Yu Mincho", "Noto Serif JP", serif;
        font-size: 1.15rem;
        font-weight: 700;
        color: #1e293b;
    }
    .col-kana {
        width: 18%;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Sans", sans-serif;
        font-size: 0.95rem;
        color: #475569;
    }
    .col-hv {
        width: 15%;
        font-size: 0.85rem;
        font-weight: 700;
        color: #0284c7;
    }
    .col-actions {
        width: 140px;
        text-align: center;
        white-space: nowrap;
    }
    .badge-hv {
        display: inline-block;
        padding: 2px 7px;
        font-size: 0.78rem;
        font-weight: 700;
        background: #e0f2fe;
        color: #0369a1;
        border-radius: 6px;
        letter-spacing: 0.3px;
    }
    .clickable-kanji {
        cursor: pointer;
        transition: color 0.12s ease;
        border-bottom: 2px dotted #38bdf8;
    }
    .clickable-kanji:hover {
        color: #0284c7;
    }
    .btn-stroke-model {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 4px 8px;
        font-size: 0.78rem;
        font-weight: 600;
        background: #f1f5f9;
        color: #334155;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.12s ease;
    }
    .btn-stroke-model:hover {
        background: #e2e8f0;
        color: #0284c7;
        border-color: #93c5fd;
        transform: translateY(-1px);
    }
    .btn-stroke-model:active {
        transform: scale(0.96);
    }
    .no-stroke-tag {
        font-size: 0.75rem;
        color: #94a3b8;
        padding: 3px 6px;
    }
    .action-btn-group {
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Modal Backdrop & Container */
    .motion-modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(8px);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 16px;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.2s ease;
    }
    .motion-modal-backdrop.open {
        opacity: 1;
        pointer-events: auto;
    }
    .motion-modal-card {
        background: #ffffff;
        border-radius: 18px;
        max-width: 820px;
        width: 100%;
        max-height: 92vh;
        overflow-y: auto;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
        display: flex;
        flex-direction: column;
        border: 1px solid #e2e8f0;
        animation: motionModalPop 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes motionModalPop {
        from { transform: scale(0.94); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    .motion-modal-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 18px 24px;
        border-bottom: 1px solid #e2e8f0;
        background: #f8fafc;
        border-top-left-radius: 18px;
        border-top-right-radius: 18px;
    }
    .motion-modal-title-group {
        display: flex;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
    }
    .motion-badge-lesson {
        padding: 3px 9px;
        font-size: 0.78rem;
        font-weight: 700;
        border-radius: 999px;
        background: #3b82f6;
        color: #ffffff;
    }
    .motion-title-wrap h3 {
        margin: 0;
        font-size: 1.45rem;
        font-weight: 800;
        color: #0f172a;
        font-family: "Hiragino Mincho ProN", "Yu Mincho", serif;
        display: inline-block;
    }
    .motion-kana-sub {
        font-size: 0.95rem;
        color: #64748b;
        margin-left: 8px;
        font-weight: 500;
    }
    .motion-hv-sub {
        font-size: 0.85rem;
        font-weight: 700;
        color: #0284c7;
        margin-left: 8px;
    }
    .motion-header-actions {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .btn-motion-speak {
        padding: 6px 14px;
        font-size: 0.85rem;
        font-weight: 600;
        background: #ecfdf5;
        color: #047857;
        border: 1px solid #a7f3d0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.12s ease;
    }
    .btn-motion-speak:hover {
        background: #d1fae5;
    }
    .btn-motion-close {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        border: 1px solid #cbd5e1;
        background: #ffffff;
        font-size: 1rem;
        font-weight: 700;
        color: #64748b;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.12s ease;
    }
    .btn-motion-close:hover {
        background: #f1f5f9;
        color: #ef4444;
    }

    /* Character Selector Tabs */
    .motion-char-tabs-wrap {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 12px 24px;
        background: #f1f5f9;
        border-bottom: 1px solid #e2e8f0;
        overflow-x: auto;
    }
    .char-tab-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 16px;
        font-size: 0.95rem;
        font-weight: 700;
        background: #ffffff;
        color: #334155;
        border: 1.5px solid #cbd5e1;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.12s ease;
    }
    .char-tab-btn:hover {
        border-color: #38bdf8;
        color: #0284c7;
    }
    .char-tab-btn.active {
        background: #0284c7;
        color: #ffffff;
        border-color: #0284c7;
        box-shadow: 0 4px 10px -2px rgba(2, 132, 199, 0.4);
    }

    /* Modal Body Grid */
    .motion-modal-body {
        display: grid;
        grid-template-columns: 340px 1fr;
        gap: 24px;
        padding: 24px;
    }
    @media (max-width: 768px) {
        .motion-modal-body {
            grid-template-columns: 1fr;
            padding: 16px;
        }
    }
    .motion-stage-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .kanji-grid-box {
        position: relative;
        width: 260px;
        height: 260px;
        background: #ffffff;
        border: 2px solid #cbd5e1;
        border-radius: 14px;
        box-shadow: inset 0 2px 6px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.06);
        overflow: hidden;
    }
    .grid-cross-lines {
        position: absolute;
        inset: 0;
        background:
            linear-gradient(to right, transparent 49.5%, #f1f5f9 49.5%, #f1f5f9 50.5%, transparent 50.5%),
            linear-gradient(to bottom, transparent 49.5%, #f1f5f9 49.5%, #f1f5f9 50.5%, transparent 50.5%);
        pointer-events: none;
    }
    .grid-diagonal-lines {
        position: absolute;
        inset: 0;
        background:
            linear-gradient(45deg, transparent 49.5%, #f8fafc 49.5%, #f8fafc 50.5%, transparent 50.5%),
            linear-gradient(-45deg, transparent 49.5%, #f8fafc 49.5%, #f8fafc 50.5%, transparent 50.5%);
        pointer-events: none;
    }
    .kanji-svg-player-wrap {
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .kanji-svg-player-wrap svg {
        width: 100%;
        height: 100%;
    }
    .motion-loading-spinner {
        font-size: 0.88rem;
        color: #64748b;
    }
    .motion-practice-canvas {
        position: absolute;
        inset: 0;
        z-index: 5;
        cursor: crosshair;
        touch-action: none;
        display: none;
    }
    .motion-practice-canvas.active {
        display: block;
    }

    /* Motion Controls */
    .motion-controls-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        margin-top: 14px;
        flex-wrap: wrap;
    }
    .btn-m-ctrl {
        padding: 6px 12px;
        font-size: 0.8rem;
        font-weight: 600;
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        color: #334155;
        cursor: pointer;
        transition: all 0.12s ease;
    }
    .btn-m-ctrl:hover {
        background: #e2e8f0;
        color: #0f172a;
    }
    .btn-m-ctrl:active {
        transform: scale(0.96);
    }
    .motion-subcontrols-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        margin-top: 12px;
        gap: 8px;
    }
    .motion-speed-picker {
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .ctrl-label {
        font-size: 0.78rem;
        color: #64748b;
        font-weight: 600;
    }
    .speed-btn {
        padding: 3px 7px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid #cbd5e1;
        background: #ffffff;
        color: #475569;
        border-radius: 6px;
        cursor: pointer;
    }
    .speed-btn.active {
        background: #0284c7;
        color: #ffffff;
        border-color: #0284c7;
    }
    .mode-pill-btn {
        padding: 4px 10px;
        font-size: 0.78rem;
        font-weight: 700;
        border: 1.5px solid #cbd5e1;
        background: #ffffff;
        color: #475569;
        border-radius: 999px;
        cursor: pointer;
    }
    .mode-pill-btn.active {
        background: #10b981;
        color: #ffffff;
        border-color: #10b981;
    }
    .practice-actions-row {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 10px;
        flex-wrap: wrap;
        width: 100%;
        justify-content: center;
    }
    .btn-pr-action {
        padding: 4px 10px;
        font-size: 0.75rem;
        font-weight: 600;
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        cursor: pointer;
    }
    .practice-hint {
        font-size: 0.75rem;
        color: #64748b;
        width: 100%;
        text-align: center;
        margin-top: 4px;
    }

    /* Sidebar info */
    .motion-sidebar {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    .char-details-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 16px;
    }
    .char-big-header {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .char-huge-display {
        font-size: 3.4rem;
        font-weight: 800;
        color: #0f172a;
        font-family: "Hiragino Mincho ProN", "Yu Mincho", serif;
        line-height: 1;
        min-width: 65px;
        text-align: center;
    }
    .char-meta-text {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    .meta-hv {
        font-size: 1.05rem;
        color: #0284c7;
    }
    .meta-strokes {
        font-size: 0.88rem;
        color: #475569;
    }
    .meta-vi {
        font-size: 0.9rem;
        color: #334155;
    }

    /* Breakdown Strip */
    .step-breakdown-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 14px;
    }
    .step-breakdown-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
        font-size: 0.85rem;
        font-weight: 700;
        color: #334155;
    }
    .step-hint {
        font-size: 0.75rem;
        font-weight: 500;
        color: #94a3b8;
    }
    .step-strip-scroll {
        display: flex;
        gap: 8px;
        overflow-x: auto;
        padding-bottom: 8px;
    }
    .step-thumb {
        flex: 0 0 54px;
        width: 54px;
        height: 54px;
        border: 1.5px solid #e2e8f0;
        border-radius: 8px;
        background: #f8fafc;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        transition: all 0.12s ease;
    }
    .step-thumb:hover {
        border-color: #38bdf8;
        transform: translateY(-2px);
    }
    .step-thumb.active {
        border-color: #0284c7;
        background: #e0f2fe;
    }
    .step-thumb svg {
        width: 38px;
        height: 38px;
    }
    .step-num-badge {
        position: absolute;
        bottom: 2px;
        right: 4px;
        font-size: 0.65rem;
        font-weight: 800;
        color: #e11d48;
    }

    /* Flashcard additions */
    .fc-kanji-huge {
        font-size: 2.6rem;
        font-weight: 800;
        font-family: "Hiragino Mincho ProN", "Yu Mincho", serif;
        color: #0f172a;
        margin-bottom: 4px;
    }
    .fc-kana-sub {
        font-size: 1.15rem;
        color: #64748b;
        font-weight: 500;
    }
    .fc-hv-badge {
        display: inline-block;
        padding: 3px 10px;
        font-size: 0.85rem;
        font-weight: 700;
        background: #e0f2fe;
        color: #0369a1;
        border-radius: 999px;
        margin-top: 8px;
    }
    .btn-fc-motion {
        padding: 6px 14px;
        font-size: 0.82rem;
        font-weight: 600;
        background: #ffffff;
        color: #0284c7;
        border: 1.5px solid #bae6fd;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.12s ease;
    }
    .btn-fc-motion:hover {
        background: #e0f2fe;
        border-color: #38bdf8;
    }

    /* Floating Mini Motion Widget */
    .mini-motion-widget {
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: 170px;
        background: rgba(255, 255, 255, 0.94);
        backdrop-filter: blur(14px);
        border: 1px solid #cbd5e1;
        border-radius: 14px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.18);
        z-index: 998;
        overflow: hidden;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .mini-motion-widget.minimized {
        width: 110px;
    }
    .mini-motion-widget.minimized .mini-motion-body {
        display: none;
    }
    .mini-motion-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 6px 10px;
        background: #f8fafc;
        border-bottom: 1px solid #e2e8f0;
    }
    .mini-motion-title {
        display: flex;
        align-items: center;
        gap: 5px;
        font-weight: 800;
        font-size: 0.95rem;
        color: #0f172a;
    }
    .mini-hv {
        font-size: 0.72rem;
        font-weight: 700;
        color: #0284c7;
    }
    .mini-motion-btns {
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .btn-mini-opt {
        border: none;
        background: transparent;
        font-size: 0.8rem;
        cursor: pointer;
        color: #64748b;
        padding: 2px;
    }
    .btn-mini-opt:hover {
        color: #0284c7;
    }
    .mini-motion-body {
        padding: 8px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .mini-svg-stage {
        width: 120px;
        height: 120px;
        background: #ffffff;
        border: 1px dashed #cbd5e1;
        border-radius: 8px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    .mini-svg-stage svg {
        width: 100%;
        height: 100%;
    }
    .mini-placeholder {
        font-size: 0.7rem;
        color: #94a3b8;
        text-align: center;
        padding: 6px;
    }
    .mini-word-desc {
        font-size: 0.72rem;
        color: #475569;
        text-align: center;
        margin-top: 6px;
        max-width: 150px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .motion-pulse-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #10b981;
        display: inline-block;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); opacity: 0.6; }
        50% { transform: scale(1.3); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.6; }
    }
'''

if '/* KANJI STROKE ANIMATION MOTION MODEL' not in html:
    html = html.replace('</style>', f'{motion_css}\n</style>', 1)
    print("Injected Motion Model CSS!")

# 3. Add Motion Modal & Floating Widget HTML right before </body>
modal_html = '''
<!-- KANJI STROKE ANIMATION MOTION MODEL MODAL -->
<div id="kanjiMotionModal" class="motion-modal-backdrop" onclick="closeStrokeModelOnBackdrop(event)">
    <div class="motion-modal-card" onclick="event.stopPropagation()">
        <!-- Modal Header -->
        <div class="motion-modal-header">
            <div class="motion-modal-title-group">
                <span class="motion-badge-lesson" id="motionLessonBadge">A1-3</span>
                <div class="motion-title-wrap">
                    <h3 id="motionWordKanji">自己紹介</h3>
                    <span id="motionWordKana" class="motion-kana-sub">じこしょうかい</span>
                    <span id="motionWordHv" class="motion-hv-sub">[TỰ KỶ THIỆU GIỚI]</span>
                </div>
            </div>
            <div class="motion-header-actions">
                <button type="button" class="btn-motion-speak" onclick="speakMotionWord()" title="Nghe phát âm chuẩn">🔊 Nghe</button>
                <button type="button" class="btn-motion-close" onclick="closeStrokeModel()" title="Đóng modal">✕</button>
            </div>
        </div>

        <!-- Multi-Kanji Character Tabs -->
        <div class="motion-char-tabs-wrap" id="motionCharTabs">
            <!-- Populated via JS -->
        </div>

        <!-- Main Interactive Body -->
        <div class="motion-modal-body">
            <!-- Left: Animated Vector Kanji Canvas Stage -->
            <div class="motion-stage-container">
                <div class="kanji-grid-box" id="kanjiGridBox">
                    <div class="grid-cross-lines"></div>
                    <div class="grid-diagonal-lines"></div>

                    <div id="kanjiSvgContainer" class="kanji-svg-player-wrap">
                        <div class="motion-loading-spinner" id="motionSpinner">Đang tải nét chữ...</div>
                    </div>

                    <canvas id="motionCanvas" width="260" height="260" class="motion-practice-canvas"></canvas>
                </div>

                <!-- Stage Playback Controls -->
                <div class="motion-controls-row">
                    <button type="button" class="btn-m-ctrl" id="btnMotionPlay" onclick="toggleMotionPlay()" title="Phát / Tạm dừng">▶️ Phát tiếp</button>
                    <button type="button" class="btn-m-ctrl" onclick="stepMotionPrev()" title="Lùi 1 nét">⏮️ Lùi nét</button>
                    <button type="button" class="btn-m-ctrl" onclick="stepMotionNext()" title="Tiến 1 nét">⏭️ Tiến nét</button>
                    <button type="button" class="btn-m-ctrl" onclick="replayMotion()" title="Vẽ lại từ đầu">🔄 Vẽ lại</button>
                    <button type="button" class="btn-m-ctrl" id="btnMotionNumbers" onclick="toggleMotionNumbers()" title="Bật/Tắt số thứ tự nét">🔢 Số nét</button>
                </div>

                <!-- Speed & Mode Switcher -->
                <div class="motion-subcontrols-row">
                    <div class="motion-speed-picker">
                        <span class="ctrl-label">Tốc độ:</span>
                        <button type="button" class="speed-btn" onclick="setMotionSpeed(0.6, this)">0.5x</button>
                        <button type="button" class="speed-btn active" onclick="setMotionSpeed(1.0, this)">1.0x</button>
                        <button type="button" class="speed-btn" onclick="setMotionSpeed(1.6, this)">1.5x</button>
                    </div>
                    <div class="motion-mode-toggle">
                        <button type="button" class="mode-pill-btn active" id="btnModeWatch" onclick="switchMotionMode('watch')">🎬 Xem Hoạt Họa</button>
                        <button type="button" class="mode-pill-btn" id="btnModeDraw" onclick="switchMotionMode('draw')">✍️ Tự Tập Viết</button>
                    </div>
                </div>

                <!-- Drawing Practice Actions -->
                <div class="practice-actions-row" id="practiceActionsRow" style="display: none;">
                    <button type="button" class="btn-pr-action" onclick="clearPracticeCanvas()">🧹 Xóa vẽ lại</button>
                    <button type="button" class="btn-pr-action" id="btnToggleGhost" onclick="togglePracticeGhost()">👁️ Ẩn nét mờ</button>
                    <span class="practice-hint">💡 Dùng chuột hoặc ngón tay để tô theo từng nét chữ!</span>
                </div>
            </div>

            <!-- Right: Kanji Breakdown & Info -->
            <div class="motion-sidebar">
                <div class="char-details-card">
                    <div class="char-big-header">
                        <div class="char-huge-display" id="charHugeDisplay">自</div>
                        <div class="char-meta-text">
                            <div class="meta-hv" id="charMetaHv">Hán Việt: <strong>TỰ</strong></div>
                            <div class="meta-strokes" id="charMetaStrokes">Tổng số nét: <strong id="charStrokeCountVal">6</strong> nét</div>
                            <div class="meta-vi" id="charMetaMeaning">Ý nghĩa: Tự mình, bản thân</div>
                        </div>
                    </div>
                </div>

                <!-- Step-by-Step Breakdown Strip -->
                <div class="step-breakdown-card">
                    <div class="step-breakdown-header">
                        <span>Phân rã thứ tự nét vẽ</span>
                        <span class="step-hint">Click vào bước để xem ngay</span>
                    </div>
                    <div class="step-strip-scroll" id="stepStripScroll">
                        <!-- Populated via JS -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- FLOATING MINI MOTION MODEL WIDGET (Bottom Right) -->
<div id="miniMotionWidget" class="mini-motion-widget">
    <div class="mini-motion-header">
        <div class="mini-motion-title">
            <span class="motion-pulse-dot"></span>
            <span id="miniMotionChar">自</span>
            <span id="miniMotionHv" class="mini-hv">TỰ</span>
        </div>
        <div class="mini-motion-btns">
            <button type="button" class="btn-mini-opt" onclick="expandMiniMotion()" title="Mở mô hình chi tiết">↗️</button>
            <button type="button" class="btn-mini-opt" onclick="toggleMiniMotionMinimize()" title="Thu nhỏ / Mở rộng" id="btnMiniToggle">–</button>
        </div>
    </div>
    <div class="mini-motion-body" id="miniMotionBody">
        <div class="mini-svg-stage" id="miniSvgContainer" onclick="expandMiniMotion()" title="Click để phóng to">
            <div class="mini-placeholder">✍️ Chọn một từ để xem chuyển động nét!</div>
        </div>
        <div class="mini-word-desc" id="miniWordDesc">Tự mình, bản thân</div>
    </div>
</div>
'''

if 'id="kanjiMotionModal"' not in html:
    html = html.replace('</body>', f'{modal_html}\n</body>')
    print("Injected Motion Model Modal and Widget HTML!")

# 4. Overwrite rawVocab in HTML with master_vocab
raw_vocab_json = json.dumps(master_vocab, ensure_ascii=False, indent=4)
raw_vocab_snippet = f'    // Master Vocabulary Data (Enriched with Kanji, Kana, Han-Viet, Romaji)\n    const rawVocab = {raw_vocab_json};'

pattern = r'    // Master Vocabulary Data\s*const rawVocab = \[.*?\];'
if re.search(pattern, html, flags=re.DOTALL):
    html = re.sub(pattern, raw_vocab_snippet, html, flags=re.DOTALL)
    print("Updated rawVocab in HTML successfully!")
else:
    print("WARNING: rawVocab regex pattern did not match directly, searching alternative...")
    idx_start = html.find('const rawVocab = [')
    if idx_start != -1:
        idx_end = html.find('];', idx_start)
        if idx_end != -1:
            html = html[:idx_start] + f'const rawVocab = {raw_vocab_json}' + html[idx_end+1:]
            print("Replaced rawVocab by boundary indices successfully!")

with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated Tu_Vung_Marugoto_A1_16_A2_1_10.html (Part 1)")
