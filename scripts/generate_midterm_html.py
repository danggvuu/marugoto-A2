import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import EXAMS_DATA from build_5_midterm_exams
from build_5_midterm_exams import EXAMS_DATA_5 as EXAMS_DATA

print(f"Loaded {len(EXAMS_DATA)} exams.")

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Trọn Bộ 5 Mã Đề Thi Giữa Kỳ Midterm Marugoto A2-1 • Chuẩn Cấu Trúc Bảng Lớp Học (M101 - M105)</title>
    <meta name="description" content="Đề thi thử giữa kỳ Midterm Marugoto A2-1 chuẩn 100% format bảng lớp: Từ vựng (( ) & câu đồng nghĩa), Kanji (2 chiều), Ngữ pháp (( ), hái sao ☆, dịch câu), Đọc hiểu (2 câu TN), Tự luận Can-do (2 câu).">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #4f46e5;
            --primary-light: #e0e7ff;
            --primary-dark: #3730a3;
            --secondary: #0ea5e9;
            --secondary-light: #e0f2fe;
            --accent: #f43f5e;
            --accent-light: #ffe4e6;
            --success: #10b981;
            --success-light: #d1fae5;
            --warning: #f59e0b;
            --warning-light: #fef3c7;
            --gold: #d97706;
            --dark: #0f172a;
            --gray-50: #f8fafc;
            --gray-100: #f1f5f9;
            --gray-200: #e2e8f0;
            --gray-300: #cbd5e1;
            --gray-400: #94a3b8;
            --gray-500: #64748b;
            --gray-600: #475569;
            --gray-700: #334155;
            --gray-800: #1e293b;
            --radius-md: 10px;
            --radius-lg: 16px;
            --radius-full: 9999px;
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        body {
            background-color: #f1f5f9;
            color: var(--gray-800);
            line-height: 1.6;
            padding-bottom: 80px;
        }

        .jp-text {
            font-family: 'Noto Sans JP', sans-serif;
        }

        /* Top Global Hub Nav */
        .global-hub-nav {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 10px 0 24px 0;
            flex-wrap: wrap;
        }

        .hub-nav-item {
            text-decoration: none;
            background: #ffffff;
            color: #475569;
            padding: 9px 18px;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 700;
            border: 1.5px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            font-family: inherit;
        }

        .hub-nav-item:hover {
            border-color: #4f46e5;
            color: #4f46e5;
            transform: translateY(-2px);
        }

        .hub-nav-item.active-hub {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: #ffffff !important;
            border-color: transparent;
            box-shadow: 0 4px 15px rgba(79, 70, 229, 0.35);
        }

        /* Hub Dropdown Menu */
        .hub-dropdown {
            position: relative;
            display: inline-block;
        }

        .hub-dropdown-menu {
            display: none;
            position: absolute;
            top: calc(100% + 6px);
            left: 50%;
            transform: translateX(-50%);
            background: #ffffff;
            border: 1.5px solid #e2e8f0;
            border-radius: 14px;
            box-shadow: 0 12px 28px rgba(0,0,0,0.12);
            padding: 8px;
            min-width: 270px;
            z-index: 9999;
        }

        .hub-dropdown-menu.show {
            display: block;
        }

        .hub-drop-link {
            display: block;
            padding: 8px 14px;
            color: #334155;
            font-size: 0.88rem;
            font-weight: 700;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.15s ease;
        }

        .hub-drop-link:hover {
            background: #eef2ff;
            color: #4f46e5;
        }

        .hub-drop-link.active {
            background: #4f46e5;
            color: #ffffff !important;
        }

        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 16px;
        }

        /* Hero Banner */
        .hero-banner {
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 45%, #4338ca 100%);
            color: white;
            border-radius: var(--radius-lg);
            padding: 30px 26px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-md);
            position: relative;
            overflow: hidden;
        }

        .hero-banner::after {
            content: '中間試験';
            position: absolute;
            right: 20px;
            bottom: -20px;
            font-family: 'Noto Sans JP', sans-serif;
            font-size: 6.5rem;
            font-weight: 900;
            color: rgba(255, 255, 255, 0.05);
            pointer-events: none;
            line-height: 1;
        }

        .hero-banner h1 {
            font-size: 1.85rem;
            font-weight: 800;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .hero-badge {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            color: #ffffff;
            font-size: 0.82rem;
            font-weight: 800;
            padding: 4px 14px;
            border-radius: var(--radius-full);
            box-shadow: 0 2px 8px rgba(217, 119, 6, 0.4);
        }

        .hero-desc {
            font-size: 0.98rem;
            opacity: 0.94;
            max-width: 880px;
            margin-bottom: 18px;
            line-height: 1.6;
        }

        .hero-features {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .feature-pill {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 7px 15px;
            border-radius: 9999px;
            font-size: 0.84rem;
            font-weight: 600;
            backdrop-filter: blur(4px);
        }

        /* Whiteboard spec callout */
        .wb-spec-card {
            background: #ffffff;
            border-radius: var(--radius-lg);
            border: 2px dashed #6366f1;
            padding: 16px 20px;
            margin-bottom: 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.08);
        }

        .wb-spec-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .wb-spec-icon {
            font-size: 2rem;
            background: #eef2ff;
            width: 50px;
            height: 50px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .wb-spec-title {
            font-weight: 800;
            color: #1e1b4b;
            font-size: 1rem;
        }

        .wb-spec-sub {
            font-size: 0.85rem;
            color: #64748b;
        }

        .wb-spec-tags {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .wb-part-tag {
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 0.8rem;
            font-weight: 700;
            color: #334155;
        }

        /* Exam Code Selector */
        .code-selector-card {
            background: white;
            border-radius: var(--radius-lg);
            padding: 16px 20px;
            margin-bottom: 22px;
            box-shadow: var(--shadow-sm);
            border: 1.5px solid var(--gray-200);
        }

        .selector-label {
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--gray-500);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            display: block;
        }

        .code-tab-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 12px;
        }

        .code-tab-btn {
            background: var(--gray-50);
            border: 2px solid var(--gray-300);
            border-radius: 14px;
            padding: 14px 18px;
            text-align: left;
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
        }

        .code-tab-btn:hover {
            border-color: var(--primary);
            background: var(--primary-light);
            transform: translateY(-2px);
        }

        .code-tab-btn.active {
            background: white;
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.18);
        }

        .code-tab-btn .tab-code {
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .code-tab-btn .tab-badge {
            font-size: 0.75rem;
            font-weight: 700;
            background: #e0e7ff;
            color: #3730a3;
            padding: 3px 8px;
            border-radius: 9999px;
        }

        .code-tab-btn.active .tab-badge {
            background: #4f46e5;
            color: white;
        }

        .code-tab-btn .tab-desc {
            font-size: 0.82rem;
            color: var(--gray-600);
            margin-top: 6px;
            line-height: 1.4;
        }

        /* Sticky Control Bar */
        .control-bar {
            background: white;
            border-radius: var(--radius-lg);
            padding: 14px 22px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 14px;
            position: sticky;
            top: 15px;
            z-index: 90;
        }

        .timer-box {
            display: flex;
            align-items: center;
            gap: 10px;
            background: var(--gray-100);
            padding: 8px 18px;
            border-radius: var(--radius-full);
            font-weight: 800;
            font-size: 1.15rem;
            color: var(--dark);
        }

        .timer-box.warning {
            background: var(--accent-light);
            color: var(--accent);
            animation: pulseWarning 1s infinite alternate;
        }

        @keyframes pulseWarning {
            0% { transform: scale(1); }
            100% { transform: scale(1.04); }
        }

        .timer-btn {
            background: white;
            border: 1px solid var(--gray-300);
            border-radius: 50%;
            width: 32px;
            height: 32px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }

        .timer-btn:hover {
            background: var(--gray-200);
        }

        .progress-box {
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;
            min-width: 220px;
            max-width: 380px;
        }

        .progress-bar-bg {
            flex: 1;
            height: 10px;
            background: var(--gray-200);
            border-radius: 9999px;
            overflow: hidden;
        }

        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #10b981 0%, #059669 100%);
            width: 0%;
            transition: width 0.3s ease;
            border-radius: 9999px;
        }

        .progress-text {
            font-size: 0.86rem;
            font-weight: 700;
            color: var(--gray-600);
            white-space: nowrap;
        }

        .control-actions {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .toggle-switch-label {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--gray-700);
            cursor: pointer;
            user-select: none;
            background: var(--gray-100);
            padding: 8px 14px;
            border-radius: var(--radius-full);
            transition: all 0.2s ease;
        }

        .toggle-switch-label:hover {
            background: var(--gray-200);
        }

        .toggle-switch-label input {
            cursor: pointer;
            accent-color: var(--primary);
            width: 16px;
            height: 16px;
        }

        .btn-submit {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border: none;
            border-radius: var(--radius-full);
            padding: 10px 24px;
            font-size: 0.95rem;
            font-weight: 800;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(16, 185, 129, 0.45);
        }

        .btn-history {
            background: var(--gray-100);
            color: var(--gray-700);
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-full);
            padding: 10px 18px;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn-history:hover {
            background: var(--gray-200);
            color: var(--dark);
        }

        /* Question Navigation Palette */
        .q-palette-card {
            background: white;
            border-radius: var(--radius-lg);
            padding: 16px 20px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
        }

        .q-palette-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            flex-wrap: wrap;
            gap: 10px;
        }

        .q-palette-title {
            font-size: 0.9rem;
            font-weight: 800;
            color: var(--gray-700);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .palette-legend {
            display: flex;
            gap: 14px;
            font-size: 0.8rem;
            color: var(--gray-600);
            flex-wrap: wrap;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .legend-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }

        .legend-dot.unanswered { background: var(--gray-300); }
        .legend-dot.answered { background: var(--success); }
        .legend-dot.star { background: var(--gold); }
        .legend-dot.essay { background: #8b5cf6; }

        .palette-groups {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .palette-sec-row {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
            padding: 6px 0;
            border-bottom: 1px dashed var(--gray-200);
        }

        .palette-sec-row:last-child {
            border-bottom: none;
        }

        .palette-sec-name {
            font-size: 0.82rem;
            font-weight: 800;
            color: var(--primary);
            min-width: 140px;
        }

        .palette-bubbles {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }

        .q-bubble {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            background: var(--gray-100);
            border: 1.5px solid var(--gray-300);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--gray-700);
            cursor: pointer;
            text-decoration: none;
            transition: all 0.15s ease;
        }

        .q-bubble:hover {
            border-color: var(--primary);
            background: var(--primary-light);
            color: var(--primary);
            transform: translateY(-2px);
        }

        .q-bubble.answered {
            background: var(--success-light);
            border-color: var(--success);
            color: #065f46;
        }

        .q-bubble.is-star {
            border-color: var(--gold);
        }

        .q-bubble.is-essay {
            border-color: #8b5cf6;
        }

        /* Section Containers */
        .exam-section-card {
            background: white;
            border-radius: var(--radius-lg);
            margin-bottom: 28px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
            overflow: hidden;
        }

        .section-header {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            padding: 18px 24px;
            border-bottom: 2px solid var(--gray-200);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }

        .sec-title-group {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .sec-badge-num {
            background: var(--primary);
            color: white;
            font-weight: 900;
            font-size: 1.1rem;
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 6px rgba(79, 70, 229, 0.3);
        }

        .sec-title-text {
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--dark);
        }

        .sec-weight-badge {
            background: #dbeafe;
            color: #1e40af;
            font-size: 0.8rem;
            font-weight: 800;
            padding: 5px 12px;
            border-radius: 9999px;
            border: 1px solid #bfdbfe;
        }

        .sec-desc-text {
            padding: 10px 24px;
            background: #fdfdfe;
            font-size: 0.9rem;
            color: var(--gray-600);
            border-bottom: 1px solid var(--gray-200);
        }

        /* Group Dividers inside sections */
        .group-divider {
            padding: 14px 24px;
            background: #f8fafc;
            border-top: 1px solid var(--gray-200);
            border-bottom: 1px solid var(--gray-200);
        }

        .group-title {
            font-size: 0.95rem;
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .group-instruction {
            font-size: 0.86rem;
            color: var(--gray-600);
        }

        /* Question Item Card */
        .q-item-card {
            padding: 22px 24px;
            border-bottom: 1px solid var(--gray-200);
            transition: background 0.2s ease;
        }

        .q-item-card:last-child {
            border-bottom: none;
        }

        .q-item-card:hover {
            background: #fafbff;
        }

        .q-meta-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
            gap: 10px;
        }

        .q-number-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--gray-100);
            color: var(--gray-700);
            font-weight: 800;
            font-size: 0.86rem;
            padding: 4px 12px;
            border-radius: 8px;
            border: 1px solid var(--gray-300);
        }

        .btn-speak {
            background: white;
            border: 1px solid var(--gray-300);
            color: var(--primary);
            border-radius: 8px;
            padding: 4px 10px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.2s ease;
        }

        .btn-speak:hover {
            background: var(--primary-light);
            border-color: var(--primary);
        }

        .q-prompt-jp {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--dark);
            line-height: 1.7;
            margin-bottom: 6px;
        }

        .q-prompt-vi {
            font-size: 0.88rem;
            color: var(--gray-500);
            margin-bottom: 14px;
        }

        .hl-kw {
            color: var(--primary);
            background: var(--primary-light);
            padding: 1px 6px;
            border-radius: 4px;
            font-weight: 800;
            border-bottom: 2px solid var(--primary);
        }

        /* Options Grid (MC) */
        .options-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 10px;
            margin-bottom: 10px;
        }

        .option-label {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 16px;
            border-radius: 12px;
            border: 2px solid var(--gray-200);
            background: white;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }

        .option-label:hover {
            border-color: var(--primary);
            background: #fafbff;
            transform: translateY(-1px);
        }

        .option-label input[type="radio"] {
            display: none;
        }

        .option-radio-mark {
            width: 22px;
            height: 22px;
            border-radius: 50%;
            border: 2px solid var(--gray-300);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--gray-500);
            background: var(--gray-50);
            flex-shrink: 0;
            transition: all 0.2s ease;
        }

        .option-label.selected {
            border-color: var(--primary);
            background: #f5f3ff;
            box-shadow: 0 2px 8px rgba(79, 70, 229, 0.15);
        }

        .option-label.selected .option-radio-mark {
            border-color: var(--primary);
            background: var(--primary);
            color: white;
        }

        .option-text-jp {
            font-size: 1rem;
            font-weight: 600;
            color: var(--gray-800);
        }

        /* Star Ranking Interactive UI */
        .star-container {
            background: #fffbeb;
            border: 2px solid #fde68a;
            border-radius: 14px;
            padding: 16px 20px;
            margin-bottom: 16px;
        }

        .star-sentence-box {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            font-size: 1.15rem;
            font-weight: 700;
            color: #78350f;
            margin-bottom: 16px;
            padding: 12px;
            background: white;
            border-radius: 10px;
            border: 1px solid #fef3c7;
        }

        .star-slot {
            min-width: 90px;
            height: 38px;
            padding: 2px 12px;
            border-radius: 8px;
            border: 2px dashed #d97706;
            background: #fffdf5;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95rem;
            font-weight: 700;
            color: #92400e;
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
        }

        .star-slot.filled {
            border-style: solid;
            background: #fef3c7;
            border-color: #f59e0b;
        }

        .star-slot.slot-star {
            border-color: #f59e0b;
            background: #fff7ed;
            box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.25);
        }

        .star-slot.slot-star::before {
            content: '★';
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.9rem;
            color: #d97706;
        }

        .star-pool-box {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 14px;
        }

        .star-pill {
            background: white;
            border: 1.5px solid #cbd5e1;
            border-radius: 8px;
            padding: 8px 14px;
            font-size: 0.95rem;
            font-weight: 700;
            color: #1e293b;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: var(--shadow-sm);
        }

        .star-pill:hover {
            border-color: var(--gold);
            background: #fffbeb;
            transform: translateY(-2px);
        }

        .star-pill.placed {
            opacity: 0.45;
            pointer-events: none;
            background: #f1f5f9;
            border-color: #e2e8f0;
        }

        .star-actions {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }

        .btn-reset-star {
            background: white;
            border: 1px solid #cbd5e1;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
            color: #64748b;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-reset-star:hover {
            background: #fee2e2;
            border-color: #f87171;
            color: #dc2626;
        }

        /* Translation Input UI */
        .trans-input-box {
            margin-bottom: 12px;
        }

        .trans-textarea {
            width: 100%;
            padding: 12px 16px;
            border-radius: 10px;
            border: 1.5px solid var(--gray-300);
            font-size: 1rem;
            color: var(--dark);
            outline: none;
            transition: border 0.2s ease;
        }

        .trans-textarea:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
        }

        .trans-btn-row {
            display: flex;
            gap: 10px;
            margin-top: 8px;
            flex-wrap: wrap;
        }

        .btn-trans-check {
            background: var(--primary-light);
            color: var(--primary-dark);
            border: 1px solid #c7d2fe;
            border-radius: 8px;
            padding: 7px 16px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-trans-check:hover {
            background: var(--primary);
            color: white;
        }

        /* Reading Passage Card */
        .passage-card {
            background: #f8fafc;
            border: 1.5px solid #cbd5e1;
            border-radius: 14px;
            padding: 22px 24px;
            margin: 16px 24px 24px 24px;
            position: relative;
        }

        .passage-title {
            font-size: 1.2rem;
            font-weight: 800;
            color: #1e1b4b;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }

        .passage-body {
            font-size: 1.05rem;
            line-height: 1.85;
            color: #1e293b;
            white-space: pre-line;
            margin-bottom: 16px;
        }

        .passage-translation {
            background: white;
            border-radius: 10px;
            padding: 14px 18px;
            border-left: 4px solid var(--primary);
            font-size: 0.92rem;
            color: var(--gray-700);
            white-space: pre-line;
            display: none;
            margin-top: 12px;
        }

        .passage-translation.show {
            display: block;
        }

        .btn-toggle-trans {
            background: white;
            border: 1px solid var(--gray-300);
            color: var(--gray-700);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-toggle-trans:hover {
            background: var(--primary-light);
            color: var(--primary);
        }

        /* Essay Textarea & Rubric */
        .essay-box {
            margin-top: 10px;
        }

        .essay-textarea {
            width: 100%;
            min-height: 120px;
            padding: 14px 16px;
            border-radius: 12px;
            border: 1.5px solid var(--gray-300);
            font-size: 1.05rem;
            line-height: 1.6;
            color: var(--dark);
            outline: none;
            resize: vertical;
            transition: border 0.2s ease;
        }

        .essay-textarea:focus {
            border-color: #8b5cf6;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.18);
        }

        .essay-meta-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 6px;
            font-size: 0.82rem;
            color: var(--gray-500);
        }

        .hint-pills-row {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin: 10px 0 14px 0;
        }

        .hint-pill {
            background: #ede9fe;
            color: #5b21b6;
            font-size: 0.8rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 9999px;
            border: 1px solid #ddd6fe;
        }

        .essay-model-card {
            background: #faf5ff;
            border: 1.5px solid #d8b4fe;
            border-radius: 12px;
            padding: 16px 20px;
            margin-top: 14px;
            display: none;
        }

        .essay-model-card.show {
            display: block;
        }

        .model-header {
            font-weight: 800;
            color: #581c87;
            font-size: 0.95rem;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .model-text-jp {
            font-size: 1.05rem;
            font-weight: 600;
            color: #3b0764;
            margin-bottom: 6px;
            line-height: 1.7;
        }

        .model-text-vi {
            font-size: 0.88rem;
            color: #6b21a8;
            margin-bottom: 10px;
        }

        .model-rubric {
            font-size: 0.82rem;
            color: #7e22ce;
            background: white;
            padding: 8px 12px;
            border-radius: 8px;
            border-left: 3px solid #a855f7;
        }

        /* Feedback Explanation Box */
        .explain-box {
            margin-top: 14px;
            padding: 14px 18px;
            border-radius: 10px;
            background: #f8fafc;
            border-left: 4px solid var(--primary);
            font-size: 0.9rem;
            color: var(--gray-800);
            display: none;
            animation: fadeIn 0.3s ease;
        }

        .explain-box.show {
            display: block;
        }

        .explain-box.correct {
            background: #f0fdf4;
            border-left-color: var(--success);
            color: #14532d;
        }

        .explain-box.wrong {
            background: #fef2f2;
            border-left-color: var(--accent);
            color: #7f1d1d;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Review Mode Overrides */
        .review-mode .option-label.is-correct-ans {
            background: #d1fae5 !important;
            border-color: #10b981 !important;
            color: #065f46 !important;
            box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.4);
        }

        .review-mode .option-label.is-wrong-ans {
            background: #fee2e2 !important;
            border-color: #ef4444 !important;
            color: #991b1b !important;
        }

        /* Result Modal */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(5px);
            z-index: 1000;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }

        .modal-overlay.show {
            display: flex;
        }

        .modal-card {
            background: white;
            border-radius: 20px;
            max-width: 650px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.25);
            text-align: center;
            position: relative;
            animation: modalZoom 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes modalZoom {
            from { transform: scale(0.92); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }

        .modal-close-btn {
            position: absolute;
            top: 18px;
            right: 18px;
            background: var(--gray-100);
            border: none;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            font-size: 1.1rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--gray-600);
        }

        .modal-close-btn:hover {
            background: var(--gray-200);
        }

        .modal-trophy {
            font-size: 4rem;
            margin-bottom: 10px;
        }

        .modal-score-big {
            font-size: 3.5rem;
            font-weight: 900;
            color: var(--primary);
            line-height: 1;
            margin-bottom: 6px;
        }

        .modal-score-sub {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--gray-500);
            margin-bottom: 16px;
        }

        .modal-rating-pill {
            display: inline-block;
            padding: 6px 20px;
            border-radius: 9999px;
            font-weight: 800;
            font-size: 1rem;
            margin-bottom: 24px;
        }

        .rating-gold { background: #fef3c7; color: #b45309; }
        .rating-green { background: #d1fae5; color: #047857; }
        .rating-blue { background: #e0f2fe; color: #0369a1; }
        .rating-orange { background: #ffedd5; color: #c2410c; }

        .score-breakdown-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 10px;
            margin-bottom: 24px;
            text-align: left;
        }

        .breakdown-item {
            background: var(--gray-50);
            border: 1px solid var(--gray-200);
            border-radius: 12px;
            padding: 12px;
        }

        .breakdown-title {
            font-size: 0.76rem;
            font-weight: 800;
            color: var(--gray-500);
            text-transform: uppercase;
        }

        .breakdown-score {
            font-size: 1.25rem;
            font-weight: 900;
            color: var(--dark);
            margin-top: 4px;
        }

        .modal-actions {
            display: flex;
            gap: 12px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn-modal-action {
            padding: 12px 24px;
            border-radius: 9999px;
            font-weight: 800;
            font-size: 0.95rem;
            cursor: pointer;
            border: none;
            transition: all 0.2s ease;
        }

        .btn-modal-review {
            background: var(--primary);
            color: white;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.35);
        }

        .btn-modal-review:hover {
            background: var(--primary-dark);
            transform: translateY(-2px);
        }

        .btn-modal-retry {
            background: var(--gray-100);
            color: var(--gray-700);
            border: 1px solid var(--gray-300);
        }

        .btn-modal-retry:hover {
            background: var(--gray-200);
        }

        /* History Modal */
        .history-list {
            margin: 16px 0;
            max-height: 350px;
            overflow-y: auto;
            text-align: left;
        }

        .history-row {
            padding: 12px 16px;
            border-radius: 10px;
            border: 1px solid var(--gray-200);
            background: var(--gray-50);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        /* Toast notification */
        .toast-notify {
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #1e1b4b;
            color: white;
            padding: 12px 20px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.25);
            font-size: 0.9rem;
            font-weight: 700;
            z-index: 2000;
            display: flex;
            align-items: center;
            gap: 10px;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            pointer-events: none;
        }

        .toast-notify.show {
            opacity: 1;
            transform: translateY(0);
        }

        @media (max-width: 768px) {
            .hero-banner { padding: 22px 18px; }
            .hero-banner h1 { font-size: 1.45rem; }
            .control-bar { padding: 12px 14px; top: 10px; }
            .progress-box { order: 3; min-width: 100%; max-width: 100%; }
            .code-tab-grid { grid-template-columns: 1fr; }
            .q-item-card { padding: 16px 14px; }
            .section-header { padding: 14px 16px; }
            .passage-card { margin: 12px 14px 18px 14px; padding: 16px; }
            .star-sentence-box { font-size: 1rem; }
        }
    </style>
</head>
<body>

    <!-- TOP GLOBAL HUB NAV -->
    <div class="global-hub-nav">
        <a href="../index.html" class="hub-nav-item">🌸 Thể TE (～て)</a>
        <a href="../the_ru.html" class="hub-nav-item">📘 Thể RU (Từ Điển)</a>
        <a href="../kanji_a2.html" class="hub-nav-item">⛩️ Học Kanji & Nét Viết</a>
        <a href="../Tu_Vung_Marugoto_A1_16_A2_1_10.html" class="hub-nav-item">📖 Kho Từ Vựng A1-A2</a>
        <a href="../Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html" class="hub-nav-item">📚 Ngữ Pháp A1-A2 (26 Bài)</a>
        <a href="../demo_3d.html" class="hub-nav-item">⛩️ Không Gian 3D</a>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item active-hub" onclick="toggleTestsDropdown(event)">🎯 Ôn Tập & Đề Thi ▾</button>
            <div class="hub-dropdown-menu" id="testsDropdownMenu">
                <a href="De_Thi_Midterm_A2_1.html" class="hub-drop-link active">🎯 Đề Thi Giữa Kỳ Midterm (Bảng M102)</a>
                <a href="On_Tap_Mini_Test_A2_1_4.html" class="hub-drop-link">🎯 Ôn Tập Bài 1-4 (Mini Test)</a>
                <a href="On_Tap_Mini_Test_A2_5_8.html" class="hub-drop-link">🎯 Ôn Tập Bài 5-8 (Mini Test)</a>
                <a href="De_Thi_Thu_Marugoto_A2_5_8.html" class="hub-drop-link">📝 5 Mã Đề Thi Thử (101-105)</a>
                <a href="Kiem_Tra_Marugoto_L6_7_8.html" class="hub-drop-link">📑 Đề Kiểm Tra L6, 7, 8</a>
                <a href="Luyen_Tap_The_Te_A2_1.html" class="hub-drop-link">🌸 Luyện Tập Thể Te</a>
            </div>
        </div>
        <div class="hub-dropdown">
            <button type="button" class="hub-nav-item" onclick="toggleLessonsDropdown(event)">🚀 Web Bài Học 10-18 ▾</button>
            <div class="hub-dropdown-menu" id="lessonsDropdownMenu">
                <a href="../lessons/Marugoto_A2_Lesson_10.html" class="hub-drop-link">🌟 Bài 10: 外国文化</a>
                <a href="../lessons/Marugoto_A2_Lesson_11.html" class="hub-drop-link">🍱 Bài 11: そとで食べる</a>
                <a href="../lessons/Marugoto_A2_Lesson_12.html" class="hub-drop-link">🍜 Bài 12: 特別な日の料理</a>
                <a href="../lessons/Marugoto_A2_Lesson_13.html" class="hub-drop-link">✈️ Bài 13: 出張</a>
                <a href="../lessons/Marugoto_A2_Lesson_14.html" class="hub-drop-link">💻 Bài 14: 職場のマナー</a>
                <a href="../lessons/Marugoto_A2_Lesson_15.html" class="hub-drop-link">🏥 Bài 15: 健康な生活</a>
                <a href="../lessons/Marugoto_A2_Lesson_16.html" class="hub-drop-link">🏃 Bài 16: 体にいいこと</a>
                <a href="../lessons/Marugoto_A2_Lesson_17.html" class="hub-drop-link">🎁 Bài 17: お祝い</a>
                <a href="../lessons/Marugoto_A2_Lesson_18.html" class="hub-drop-link">👘 Bài 18: お祭りやイベント</a>
            </div>
        </div>
    </div>

    <div class="main-container">
        <!-- Hero Banner -->
        <header class="hero-banner">
            <span class="hero-badge">MIDTERM EXAM SIMULATOR</span>
            <h1>
                🎯 Đề Thi Giữa Kỳ Midterm Marugoto A2-1
            </h1>
            <p class="hero-desc">
                Hệ thống thi thử giữa kỳ thiết kế chuẩn 100% theo form bảng lớp học của thầy cô: Đầy đủ 5 phần trọng điểm, tự động bấm giờ, lưu bài làm, chấm điểm chi tiết kèm Tokyo Audio TTS và giải thích cặn kẽ từng câu.
            </p>
            <div class="hero-features">
                <span class="feature-pill">⏱️ Thời gian: 45 Phút</span>
                <span class="feature-pill">💯 Thang điểm 100 & Điểm 10</span>
                <span class="feature-pill">🔊 Dual Tokyo Voice TTS</span>
                <span class="feature-pill">💾 Tự động lưu nháp chống mất bài</span>
            </div>
        </header>

        <!-- Whiteboard Specification Card -->
        <div class="wb-spec-card">
            <div class="wb-spec-left">
                <div class="wb-spec-icon">📋</div>
                <div>
                    <div class="wb-spec-title">Cấu Trúc 5 Phần Chuẩn Bảng Lớp Học (Form Midterm)</div>
                    <div class="wb-spec-sub">Được chuẩn hóa trực tiếp từ sơ đồ kiểm tra giữa kỳ của giảng viên</div>
                </div>
            </div>
            <div class="wb-spec-tags">
                <span class="wb-part-tag">1. Từ vựng: ( ) & Câu đồng nghĩa</span>
                <span class="wb-part-tag">2. Kanji: Kanji ➔ Hira & Hira ➔ Kanji</span>
                <span class="wb-part-tag">3. Ngữ pháp: ( ) & Hái sao ☆ & Dịch câu</span>
                <span class="wb-part-tag">4. Đọc hiểu: 2 câu TN</span>
                <span class="wb-part-tag">5. Tự luận: Trả lời 2 câu</span>
            </div>
        </div>

        <!-- Exam Code Selector -->
        <div class="code-selector-card">
            <span class="selector-label">CHỌN MÃ ĐỀ THI MIDTERM:</span>
            <div class="code-tab-grid" id="examCodeTabsContainer">
                <!-- Rendered dynamically -->
            </div>
        </div>

        <!-- Sticky Control Bar -->
        <div class="control-bar" id="stickyControlBar">
            <div class="timer-box" id="timerBox">
                <span>⏱️</span>
                <span id="timerDisplay">45:00</span>
                <button type="button" class="timer-btn" id="btnToggleTimer" title="Tạm dừng / Tiếp tục" onclick="toggleTimer()">⏸️</button>
            </div>

            <div class="progress-box">
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" id="progressBarFill"></div>
                </div>
                <span class="progress-text" id="progressText">0 / 36 câu (0%)</span>
            </div>

            <div class="control-actions">
                <label class="toggle-switch-label" title="Xem giải thích và đáp án ngay khi chọn (phù hợp ôn luyện)">
                    <input type="checkbox" id="immediateCheckToggle" onchange="toggleImmediateMode()">
                    <span>⚡ Chế độ kiểm tra ngay</span>
                </label>
                <button type="button" class="btn-history" onclick="openHistoryModal()">
                    📜 Lịch sử (<span id="historyCountBadge">0</span>)
                </button>
                <button type="button" class="btn-submit" onclick="submitExam(false)">
                    ✅ Nộp Bài Thi
                </button>
            </div>
        </div>

        <!-- Quick Question Navigation Palette -->
        <div class="q-palette-card">
            <div class="q-palette-header">
                <span class="q-palette-title">
                    🧭 BẢNG ĐIỀU HƯỚNG CÂU HỎI (Bấm số để nhảy nhanh tới câu)
                </span>
                <div class="palette-legend">
                    <span class="legend-item"><span class="legend-dot unanswered"></span> Chưa làm</span>
                    <span class="legend-item"><span class="legend-dot answered"></span> Đã làm</span>
                    <span class="legend-item"><span class="legend-dot star"></span> Hái sao ☆</span>
                    <span class="legend-item"><span class="legend-dot essay"></span> Tự luận</span>
                </div>
            </div>
            <div class="palette-groups" id="paletteGroupsContainer">
                <!-- Rendered dynamically -->
            </div>
        </div>

        <!-- Exam Content Container -->
        <main id="examContentContainer">
            <!-- Rendered dynamically -->
        </main>
    </div>

    <!-- RESULT MODAL -->
    <div class="modal-overlay" id="resultModal">
        <div class="modal-card">
            <button type="button" class="modal-close-btn" onclick="closeResultModal()">✕</button>
            <div class="modal-trophy" id="modalTrophy">🏆</div>
            <div class="modal-score-big" id="modalScoreBig">85 / 100</div>
            <div class="modal-score-sub" id="modalScoreSub">Điểm hệ số 10: 8.5 • Thời gian: 24:15</div>
            <div id="modalRatingContainer">
                <span class="modal-rating-pill rating-green" id="modalRatingPill">XUẤT SẮC</span>
            </div>

            <div class="score-breakdown-grid" id="modalBreakdownGrid">
                <!-- Breakdown cards rendered dynamically -->
            </div>

            <p style="font-size: 0.92rem; color: #475569; margin-bottom: 24px; line-height: 1.6;" id="modalFeedbackMsg">
                Chúc mừng bạn đã hoàn thành xuất sắc bài thi giữa kỳ! Toàn bộ câu hỏi đã được mở khóa lời giải thích và đáp án chi tiết.
            </p>

            <div class="modal-actions">
                <button type="button" class="btn-modal-action btn-modal-review" onclick="enterReviewMode()">
                    🔍 Xem Lại Toàn Bộ Bài Làm & Lời Giải
                </button>
                <button type="button" class="btn-modal-action btn-modal-retry" onclick="confirmResetExam()">
                    🔄 Làm Lại Mã Đề Này
                </button>
            </div>
        </div>
    </div>

    <!-- HISTORY MODAL -->
    <div class="modal-overlay" id="historyModal">
        <div class="modal-card">
            <button type="button" class="modal-close-btn" onclick="closeHistoryModal()">✕</button>
            <h3 style="font-size: 1.3rem; font-weight: 800; color: #1e1b4b; margin-bottom: 6px;">📜 Lịch Sử Làm Bài Thi Midterm</h3>
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
    <div class="toast-notify" id="toastNotify">
        <span id="toastIcon">💾</span>
        <span id="toastMsg">Đã tự động lưu nháp bài làm</span>
    </div>

    <!-- AUDIO ENGINE (Dual Tokyo Speech) -->
    <script src="../assets/js/audio-engine.js"></script>

    <!-- EXAMS DATA & CONTROLLER JS -->
    <script>
    const EXAMS_DATA = ''' + json.dumps(EXAMS_DATA, ensure_ascii=False) + ''';
    ''' + '''
    // ==========================================
    // EXAM CONTROLLER STATE
    // ==========================================
    let currentExamCode = (typeof EXAMS_DATA !== 'undefined' && EXAMS_DATA.length > 0) ? EXAMS_DATA[0].code : "M101";
    let userAnswers = {}; // { [qId]: { value, starOrder, isCorrect, checked } }
    let timerSeconds = 45 * 60;
    let timerInterval = null;
    let isTimerRunning = false;
    let isImmediateMode = false;
    let isExamSubmitted = false;

    const STORAGE_KEY_PREFIX = "marugoto_midterm_draft_";
    const HISTORY_STORAGE_KEY = "marugoto_midterm_history_v1";

    // 1. Initialize
    document.addEventListener("DOMContentLoaded", () => {
        initExamTabs();
        loadExam(currentExamCode);
        updateHistoryBadge();
    });

    // 2. Exam Tabs
    function initExamTabs() {
        const container = document.getElementById("examCodeTabsContainer");
        if (!container) return;
        container.innerHTML = EXAMS_DATA.map(ex => `
            <div class="code-tab-btn ${ex.code === currentExamCode ? 'active' : ''}" onclick="switchExam('${ex.code}')">
                <div class="tab-code">
                    <span>${ex.name}</span>
                    <span class="tab-badge">${ex.tag}</span>
                </div>
                <div class="tab-desc">${ex.desc}</div>
            </div>
        `).join("");
    }

    function switchExam(code) {
        if (code === currentExamCode) return;
        if (!isExamSubmitted && Object.keys(userAnswers).length > 0) {
            if (!confirm("Bạn có bài làm dở ở đề hiện tại. Chuyển đề sẽ chuyển sang mã đề mới (tiến độ đề cũ vẫn được lưu). Tiếp tục?")) {
                return;
            }
        }
        currentExamCode = code;
        initExamTabs();
        loadExam(code);
    }

    // 3. Timer Engine
    function startTimer() {
        stopTimer();
        isTimerRunning = true;
        const btn = document.getElementById("btnToggleTimer");
        if (btn) btn.textContent = "⏸️";
        timerInterval = setInterval(() => {
            if (timerSeconds > 0) {
                timerSeconds--;
                updateTimerDisplay();
                if (timerSeconds % 10 === 0) {
                    saveDraft();
                }
            } else {
                stopTimer();
                alert("⏰ Hết giờ làm bài! Hệ thống đang tự động nộp bài thi của bạn.");
                submitExam(true);
            }
        }, 1000);
    }

    function stopTimer() {
        isTimerRunning = false;
        if (timerInterval) clearInterval(timerInterval);
        const btn = document.getElementById("btnToggleTimer");
        if (btn) btn.textContent = "▶️";
    }

    function toggleTimer() {
        if (isExamSubmitted) return;
        if (isTimerRunning) {
            stopTimer();
            showToast("⏸️ Đã tạm dừng đồng hồ");
        } else {
            startTimer();
            showToast("▶️ Tiếp tục tính giờ");
        }
    }

    function updateTimerDisplay() {
        const d = document.getElementById("timerDisplay");
        const b = document.getElementById("timerBox");
        if (!d) return;
        const m = Math.floor(timerSeconds / 60);
        const s = timerSeconds % 60;
        d.textContent = `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
        if (timerSeconds <= 5 * 60) {
            if (b) b.classList.add("warning");
        } else {
            if (b) b.classList.remove("warning");
        }
    }

    // 4. Load & Render Exam
    function loadExam(code) {
        const exam = EXAMS_DATA.find(e => e.code === code) || EXAMS_DATA[0];
        document.body.classList.remove("review-mode");
        isExamSubmitted = false;

        // Restore draft if exists
        const draft = loadDraft(code);
        if (draft) {
            userAnswers = draft.userAnswers || {};
            timerSeconds = (typeof draft.timerSeconds === "number") ? draft.timerSeconds : exam.timeLimit;
            showToast("💾 Đã khôi phục bài làm nháp từ phiên trước!");
        } else {
            userAnswers = {};
            timerSeconds = exam.timeLimit;
        }

        renderExamDOM(exam);
        renderPalette(exam);
        updateProgress();
        updateTimerDisplay();
        startTimer();
    }

    function renderExamDOM(exam) {
        const main = document.getElementById("examContentContainer");
        if (!main) return;

        let html = "";
        exam.sections.forEach(sec => {
            html += `
                <section class="exam-section-card" id="${sec.id}">
                    <div class="section-header">
                        <div class="sec-title-group">
                            <div class="sec-badge-num">${sec.partNumber}</div>
                            <h2 class="sec-title-text">${sec.partTitle}</h2>
                        </div>
                        <span class="sec-weight-badge">${sec.badge}</span>
                    </div>
                    <div class="sec-desc-text">${sec.partDesc}</div>
            `;

            // If reading section, render reading passage box first
            if (sec.readingPassage) {
                const p = sec.readingPassage;
                html += `
                    <div class="passage-card">
                        <div class="passage-title">
                            <span class="jp-text">${p.title}</span>
                            <div style="display:flex; gap:8px;">
                                <button type="button" class="btn-speak" onclick="speakJapanese(decodeURIComponent('${encodeURIComponent(p.content)}'))">
                                    🔊 Nghe Bài Đọc (Tokyo)
                                </button>
                                <button type="button" class="btn-toggle-trans" onclick="togglePassageTrans('${sec.id}')">
                                    📜 Xem Dịch
                                </button>
                            </div>
                        </div>
                        <div class="passage-body jp-text">${p.content}</div>
                        <div class="passage-translation" id="trans_${sec.id}">
                            ${p.translation.replace(/\\n/g, '<br>')}
                        </div>
                    </div>
                `;
            }

            // Render groups or direct items
            if (sec.groups) {
                sec.groups.forEach(grp => {
                    html += `
                        <div class="group-divider">
                            <div class="group-title">${grp.groupTitle}</div>
                            <div class="group-instruction">${grp.groupInstruction}</div>
                        </div>
                    `;
                    grp.items.forEach(item => {
                        html += renderQuestionItem(item);
                    });
                });
            } else if (sec.items) {
                sec.items.forEach(item => {
                    html += renderQuestionItem(item);
                });
            }

            html += `</section>`;
        });

        main.innerHTML = html;

        // Restore UI state for rendered items
        restoreItemsUI();
    }

    function renderQuestionItem(item) {
        const ans = userAnswers[item.id] || {};
        let qHtml = `
            <div class="q-item-card" id="q_card_${item.id}">
                <div class="q-meta-row">
                    <span class="q-number-badge">CÂU ${item.id}</span>
                    <button type="button" class="btn-speak" onclick="speakQuestionAudio(${item.id})">
                        🔊 Phát âm
                    </button>
                </div>
        `;

        if (item.type === "mc") {
            qHtml += `
                <div class="q-prompt-jp jp-text">${item.prompt}</div>
                <div class="q-prompt-vi">${item.promptVi || ''}</div>
                <div class="options-grid">
                    ${item.options.map((opt, oIdx) => `
                        <label class="option-label" id="opt_lbl_${item.id}_${oIdx}" onclick="handleSelectOption(${item.id}, ${oIdx})">
                            <input type="radio" name="opt_${item.id}" value="${oIdx}">
                            <div class="option-radio-mark">${['A', 'B', 'C', 'D'][oIdx]}</div>
                            <span class="option-text-jp jp-text">${opt}</span>
                        </label>
                    `).join("")}
                </div>
            `;
        } else if (item.type === "star") {
            qHtml += `
                <div class="q-prompt-vi">${item.promptVi || ''}</div>
                <div class="star-container">
                    <div class="star-sentence-box jp-text">
                        <span>${item.sentencePre}</span>
                        <div class="star-slot" id="star_slot_${item.id}_0" onclick="removeStarSlot(${item.id}, 0)">___ 1 ___</div>
                        <div class="star-slot" id="star_slot_${item.id}_1" onclick="removeStarSlot(${item.id}, 1)">___ 2 ___</div>
                        <div class="star-slot slot-star" id="star_slot_${item.id}_2" onclick="removeStarSlot(${item.id}, 2)">★ ___ 3 ___</div>
                        <div class="star-slot" id="star_slot_${item.id}_3" onclick="removeStarSlot(${item.id}, 3)">___ 4 ___</div>
                        <span>${item.sentencePost}</span>
                    </div>

                    <div style="font-size:0.82rem; font-weight:700; color:#92400e; margin-bottom:8px;">
                        👉 Bấm lần lượt 4 cụm từ dưới đây để điền vào 4 vị trí:
                    </div>

                    <div class="star-pool-box" id="star_pool_${item.id}">
                        ${item.parts.map(p => `
                            <button type="button" class="star-pill jp-text" id="star_pill_${item.id}_${p.id}" onclick="placeStarPart(${item.id}, ${p.id})">
                                <strong>[${p.id}]</strong> ${p.text}
                            </button>
                        `).join("")}
                    </div>

                    <div class="star-actions">
                        <button type="button" class="btn-reset-star" onclick="resetStarOrder(${item.id})">
                            🔄 Xếp lại từ đầu
                        </button>
                        <span style="font-size:0.82rem; color:#78350f;">
                            Chọn đáp án ở vị trí ngôi sao (★):
                        </span>
                    </div>
                </div>

                <div class="options-grid">
                    ${item.parts.map(p => `
                        <label class="option-label" id="opt_lbl_${item.id}_${p.id}" onclick="handleSelectStarRadio(${item.id}, ${p.id})">
                            <input type="radio" name="opt_${item.id}" value="${p.id}">
                            <div class="option-radio-mark">${p.id}</div>
                            <span class="option-text-jp jp-text">${p.text}</span>
                        </label>
                    `).join("")}
                </div>
            `;
        } else if (item.type === "trans") {
            qHtml += `
                <div class="q-prompt-jp jp-text" style="font-size:1.05rem;">${item.prompt}</div>
                <div class="trans-input-box">
                    <input type="text" class="trans-textarea jp-text" id="trans_input_${item.id}" 
                           placeholder="${item.placeholder}" 
                           oninput="handleTransInput(${item.id}, this.value)">
                    <div class="trans-btn-row">
                        <button type="button" class="btn-trans-check" onclick="checkTranslationSingle(${item.id})">
                            🔍 Kiểm Tra Bản Dịch
                        </button>
                    </div>
                </div>
            `;
        } else if (item.type === "essay") {
            qHtml += `
                <div class="q-prompt-jp jp-text" style="font-size:1.1rem; color:#4338ca;">${item.prompt}</div>
                <div class="q-prompt-vi">${item.promptVi || ''}</div>
                <div class="hint-pills-row">
                    ${(item.hints || []).map(h => `<span class="hint-pill">${h}</span>`).join("")}
                </div>
                <div class="essay-box">
                    <textarea class="essay-textarea jp-text" id="essay_input_${item.id}" 
                              placeholder="${item.placeholder}" 
                              oninput="handleEssayInput(${item.id}, this.value)"></textarea>
                    <div class="essay-meta-row">
                        <span id="essay_count_${item.id}">Số ký tự: 0</span>
                        <button type="button" class="btn-trans-check" onclick="toggleEssayModel(${item.id})">
                            💡 Xem Câu Mẫu & Chấm Can-do
                        </button>
                    </div>
                </div>
                <div class="essay-model-card" id="essay_model_${item.id}">
                    <div class="model-header">
                        <span>🌟 CÂU TRẢ LỜI MẪU CAN-DO (Chuẩn Marugoto A2):</span>
                        <button type="button" class="btn-speak" onclick="speakJapanese(decodeURIComponent('${encodeURIComponent(item.modelAnswer)}'))">
                            🔊 Nghe đọc mẫu
                        </button>
                    </div>
                    <div class="model-text-jp jp-text">${item.modelAnswer}</div>
                    <div class="model-text-vi">${item.modelVi}</div>
                    <div class="model-rubric"><strong>📌 Tiêu chí:</strong> ${item.rubric}</div>
                </div>
            `;
        }

        // Explanation container (hidden initially)
        qHtml += `
            <div class="explain-box" id="explain_${item.id}">
                <div id="explain_content_${item.id}"></div>
            </div>
        </div>`;

        return qHtml;
    }

    // 5. Restore UI from state
    function restoreItemsUI() {
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode) || EXAMS_DATA[0];
        getAllItems(exam).forEach(item => {
            const state = userAnswers[item.id];
            if (!state) return;

            if (item.type === "mc") {
                if (typeof state.value === "number") {
                    const lbl = document.getElementById(`opt_lbl_${item.id}_${state.value}`);
                    if (lbl) {
                        lbl.classList.add("selected");
                        const inp = lbl.querySelector("input");
                        if (inp) inp.checked = true;
                    }
                }
            } else if (item.type === "star") {
                if (state.starOrder && state.starOrder.length > 0) {
                    renderStarOrderSlots(item.id, state.starOrder);
                }
                if (typeof state.value === "number") {
                    const lbl = document.getElementById(`opt_lbl_${item.id}_${state.value}`);
                    if (lbl) {
                        lbl.classList.add("selected");
                        const inp = lbl.querySelector("input");
                        if (inp) inp.checked = true;
                    }
                }
            } else if (item.type === "trans") {
                const inp = document.getElementById(`trans_input_${item.id}`);
                if (inp && state.value) {
                    inp.value = state.value;
                }
            } else if (item.type === "essay") {
                const inp = document.getElementById(`essay_input_${item.id}`);
                const cnt = document.getElementById(`essay_count_${item.id}`);
                if (inp && state.value) {
                    inp.value = state.value;
                    if (cnt) cnt.textContent = `Số ký tự: ${state.value.length}`;
                }
            }

            if (isImmediateMode || isExamSubmitted) {
                showItemExplanation(item.id);
            }
        });
    }

    // 6. Palette Render
    function renderPalette(exam) {
        const container = document.getElementById("paletteGroupsContainer");
        if (!container) return;

        let html = "";
        exam.sections.forEach(sec => {
            const items = getSectionItems(sec);
            html += `
                <div class="palette-sec-row">
                    <span class="palette-sec-name">${sec.partTitle.split('(')[0].trim()}</span>
                    <div class="palette-bubbles">
                        ${items.map(it => {
                            const isAnswered = isItemAnswered(it.id);
                            const isStar = it.type === "star";
                            const isEssay = it.type === "essay";
                            return `
                                <a href="#q_card_${it.id}" class="q-bubble ${isAnswered ? 'answered' : ''} ${isStar ? 'is-star' : ''} ${isEssay ? 'is-essay' : ''}" id="palette_bubble_${it.id}">
                                    ${it.id}
                                </a>
                            `;
                        }).join("")}
                    </div>
                </div>
            `;
        });

        container.innerHTML = html;
    }

    function updatePaletteBubble(itemId) {
        const b = document.getElementById(`palette_bubble_${itemId}`);
        if (!b) return;
        if (isItemAnswered(itemId)) {
            b.classList.add("answered");
        } else {
            b.classList.remove("answered");
        }
    }

    function isItemAnswered(itemId) {
        const s = userAnswers[itemId];
        if (!s) return false;
        if (typeof s.value === "number") return true;
        if (typeof s.value === "string" && s.value.trim().length > 0) return true;
        return false;
    }

    function updateProgress() {
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode) || EXAMS_DATA[0];
        const all = getAllItems(exam);
        const total = all.length;
        let answered = 0;
        all.forEach(it => {
            if (isItemAnswered(it.id)) answered++;
        });

        const pct = Math.round((answered / total) * 100);
        const fill = document.getElementById("progressBarFill");
        const txt = document.getElementById("progressText");
        if (fill) fill.style.width = `${pct}%`;
        if (txt) txt.textContent = `${answered} / ${total} câu (${pct}%)`;
    }

    // 7. Interactive Input Handlers
    function handleSelectOption(itemId, oIdx) {
        if (isExamSubmitted) return;
        const card = document.getElementById(`q_card_${itemId}`);
        if (!card) return;

        // Clear other selections in this question
        card.querySelectorAll(".option-label").forEach(l => l.classList.remove("selected"));

        const lbl = document.getElementById(`opt_lbl_${itemId}_${oIdx}`);
        if (lbl) {
            lbl.classList.add("selected");
            const inp = lbl.querySelector("input");
            if (inp) inp.checked = true;
        }

        userAnswers[itemId] = {
            ...(userAnswers[itemId] || {}),
            value: oIdx
        };

        updatePaletteBubble(itemId);
        updateProgress();
        saveDraft();

        if (isImmediateMode) {
            showItemExplanation(itemId);
        }
    }

    // Star Ranking Slot Interactivity
    function placeStarPart(itemId, partId) {
        if (isExamSubmitted) return;
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
        const item = getAllItems(exam).find(it => it.id === itemId);
        if (!item) return;

        let currentOrder = (userAnswers[itemId] && userAnswers[itemId].starOrder) ? [...userAnswers[itemId].starOrder] : [];
        if (currentOrder.includes(partId)) return;
        if (currentOrder.length >= 4) return;

        currentOrder.push(partId);
        renderStarOrderSlots(itemId, currentOrder);

        // If slot 3 (star position index 2) is filled, auto-select radio
        let selectedValue = (userAnswers[itemId] && typeof userAnswers[itemId].value === "number") ? userAnswers[itemId].value : null;
        if (currentOrder.length >= 3) {
            selectedValue = currentOrder[2]; // slot 3 is the star
            handleSelectStarRadio(itemId, selectedValue, false);
        }

        userAnswers[itemId] = {
            ...(userAnswers[itemId] || {}),
            starOrder: currentOrder,
            value: selectedValue
        };

        updatePaletteBubble(itemId);
        updateProgress();
        saveDraft();

        if (isImmediateMode && currentOrder.length === 4) {
            showItemExplanation(itemId);
        }
    }

    function removeStarSlot(itemId, slotIdx) {
        if (isExamSubmitted) return;
        let currentOrder = (userAnswers[itemId] && userAnswers[itemId].starOrder) ? [...userAnswers[itemId].starOrder] : [];
        if (slotIdx >= currentOrder.length) return;

        currentOrder.splice(slotIdx, 1);
        renderStarOrderSlots(itemId, currentOrder);

        userAnswers[itemId] = {
            ...(userAnswers[itemId] || {}),
            starOrder: currentOrder
        };

        updatePaletteBubble(itemId);
        updateProgress();
        saveDraft();
    }

    function resetStarOrder(itemId) {
        if (isExamSubmitted) return;
        renderStarOrderSlots(itemId, []);
        const card = document.getElementById(`q_card_${itemId}`);
        if (card) {
            card.querySelectorAll(".option-label").forEach(l => l.classList.remove("selected"));
            card.querySelectorAll("input[type='radio']").forEach(i => i.checked = false);
        }

        userAnswers[itemId] = {
            ...(userAnswers[itemId] || {}),
            starOrder: [],
            value: null
        };

        updatePaletteBubble(itemId);
        updateProgress();
        saveDraft();
    }

    function renderStarOrderSlots(itemId, order) {
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
        const item = getAllItems(exam).find(it => it.id === itemId);
        if (!item) return;

        for (let i = 0; i < 4; i++) {
            const slot = document.getElementById(`star_slot_${itemId}_${i}`);
            if (!slot) continue;
            if (i < order.length) {
                const partId = order[i];
                const part = item.parts.find(p => p.id === partId);
                slot.textContent = part ? `[${part.id}] ${part.text}` : `[${partId}]`;
                slot.classList.add("filled");
            } else {
                slot.textContent = (i === 2) ? `★ ___ 3 ___` : `___ ${i+1} ___`;
                slot.classList.remove("filled");
            }
        }

        // Toggle disabled pills
        item.parts.forEach(p => {
            const pill = document.getElementById(`star_pill_${itemId}_${p.id}`);
            if (pill) {
                if (order.includes(p.id)) {
                    pill.classList.add("placed");
                } else {
                    pill.classList.remove("placed");
                }
            }
        });
    }

    function handleSelectStarRadio(itemId, partId, doSave = true) {
        if (isExamSubmitted) return;
        const card = document.getElementById(`q_card_${itemId}`);
        if (!card) return;

        card.querySelectorAll(".option-label").forEach(l => l.classList.remove("selected"));
        const lbl = document.getElementById(`opt_lbl_${itemId}_${partId}`);
        if (lbl) {
            lbl.classList.add("selected");
            const inp = lbl.querySelector("input");
            if (inp) inp.checked = true;
        }

        userAnswers[itemId] = {
            ...(userAnswers[itemId] || {}),
            value: partId
        };

        updatePaletteBubble(itemId);
        updateProgress();
        if (doSave) saveDraft();

        if (isImmediateMode) {
            showItemExplanation(itemId);
        }
    }

    // Translation Handlers
    function handleTransInput(itemId, val) {
        userAnswers[itemId] = {
            ...(userAnswers[itemId] || {}),
            value: val
        };
        updatePaletteBubble(itemId);
        updateProgress();
        saveDraft();
    }

    function checkTranslationSingle(itemId) {
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
        const item = getAllItems(exam).find(it => it.id === itemId);
        if (!item) return;

        const val = (userAnswers[itemId] && userAnswers[itemId].value) ? userAnswers[itemId].value.trim() : "";
        if (!val) {
            alert("Vui lòng nhập câu dịch trước khi kiểm tra!");
            return;
        }

        const isMatch = evaluateTranslation(item, val);
        userAnswers[itemId].isCorrect = isMatch;
        userAnswers[itemId].checked = true;

        showItemExplanation(itemId);
    }

    function evaluateTranslation(item, userStr) {
        if (!userStr) return false;
        const norm = s => s.toLowerCase().replace(/[\\s、。,.?!！？「」『』〜~]/g, '');
        const cleanUser = norm(userStr);

        if (item.dir === "vi_to_ja") {
            if (item.acceptable) {
                return item.acceptable.some(acc => norm(acc) === cleanUser || cleanUser.includes(norm(acc)) || norm(acc).includes(cleanUser));
            }
            return false;
        } else {
            // ja_to_vi: check keywords
            const userLower = userStr.toLowerCase();
            const keywords = item.keywords || [];
            let matched = 0;
            keywords.forEach(kw => {
                if (userLower.includes(kw.toLowerCase())) matched++;
            });
            return matched >= Math.ceil(keywords.length * 0.6);
        }
    }

    // Essay Handlers
    function handleEssayInput(itemId, val) {
        userAnswers[itemId] = {
            ...(userAnswers[itemId] || {}),
            value: val
        };
        const cnt = document.getElementById(`essay_count_${itemId}`);
        if (cnt) cnt.textContent = `Số ký tự: ${val.length}`;
        updatePaletteBubble(itemId);
        updateProgress();
        saveDraft();
    }

    function toggleEssayModel(itemId) {
        const m = document.getElementById(`essay_model_${itemId}`);
        if (m) {
            m.classList.toggle("show");
        }
    }

    function togglePassageTrans(secId) {
        const t = document.getElementById(`trans_${secId}`);
        if (t) t.classList.toggle("show");
    }

    // 8. Explanation Engine
    function showItemExplanation(itemId) {
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
        const item = getAllItems(exam).find(it => it.id === itemId);
        if (!item) return;

        const box = document.getElementById(`explain_${itemId}`);
        const content = document.getElementById(`explain_content_${itemId}`);
        if (!box || !content) return;

        let isCorrect = false;
        let rightAnsText = "";
        const state = userAnswers[itemId] || {};

        if (item.type === "mc") {
            isCorrect = (state.value === item.correct);
            rightAnsText = `Phương án ${['A','B','C','D'][item.correct]}: ${item.options[item.correct]}`;
        } else if (item.type === "star") {
            isCorrect = (state.value === item.correctOption);
            rightAnsText = `Ngôi sao (★) là phương án [${item.correctOption}]: ${item.parts.find(p => p.id === item.correctOption).text}`;
        } else if (item.type === "trans") {
            isCorrect = (state.isCorrect !== undefined) ? state.isCorrect : evaluateTranslation(item, state.value || "");
            rightAnsText = item.standard;
        } else if (item.type === "essay") {
            isCorrect = (state.value && state.value.trim().length >= 10);
            rightAnsText = "Đã hoàn thành bài tự luận Can-do!";
        }

        box.className = `explain-box show ${isCorrect ? 'correct' : 'wrong'}`;

        let detailHtml = `
            <div style="font-weight:800; font-size:0.95rem; margin-bottom:6px;">
                ${isCorrect ? '✅ CHÍNH XÁC!' : '❌ CHƯA CHÍNH XÁC!'} 
                ${!isCorrect ? `<span style="font-weight:600; color:#1e1b4b; margin-left:8px;">Đáp án đúng: <strong>${rightAnsText}</strong></span>` : ''}
            </div>
        `;

        if (item.type === "star" && item.fullSentence) {
            detailHtml += `<div style="font-size:0.95rem; font-weight:700; color:#92400e; margin-bottom:6px;">
                🌟 Câu hoàn chỉnh: <em>${item.fullSentence}</em>
            </div>`;
        }

        if (item.explain) {
            detailHtml += `<div style="margin-top:6px; line-height:1.6;">${item.explain}</div>`;
        }

        if (item.type === "trans" && !isCorrect) {
            detailHtml += `
                <div style="margin-top:10px; padding:10px 14px; background:#fef3c7; border:1px solid #f59e0b; border-radius:8px; display:flex; align-items:center; justify-content:space-between; gap:10px; flex-wrap:wrap;">
                    <span style="font-size:0.85rem; color:#92400e; font-weight:600;">💡 Bạn dùng từ đồng nghĩa hoặc câu dịch tự nhiên theo cách khác?</span>
                    <button type="button" onclick="overrideTransCorrect(${item.id})" style="background:#f59e0b; color:#fff; border:none; padding:6px 14px; border-radius:6px; font-weight:700; font-size:0.83rem; cursor:pointer;">
                        🎯 Tôi Thấy Tôi Viết Đúng (Ghi Nhận Điểm)
                    </button>
                </div>
            `;
        }

        content.innerHTML = detailHtml;
    }

    function overrideTransCorrect(itemId) {
        userAnswers[itemId] = userAnswers[itemId] || {};
        userAnswers[itemId].isCorrect = true;
        userAnswers[itemId].checked = true;
        showToast("🎯 Đã ghi nhận bản dịch của bạn là ĐÚNG (+điểm)!");
        showItemExplanation(itemId);
        updatePaletteBubble(itemId);
        updateProgress();
        saveDraft();
    }

    function toggleImmediateMode() {
        const chk = document.getElementById("immediateCheckToggle");
        isImmediateMode = chk ? chk.checked : false;
        if (isImmediateMode) {
            showToast("⚡ Đã bật Chế độ kiểm tra ngay (Luyện tập)");
            const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
            getAllItems(exam).forEach(it => {
                if (isItemAnswered(it.id)) {
                    showItemExplanation(it.id);
                }
            });
        } else {
            showToast("🔒 Đã chuyển về Chế độ làm bài thi chuẩn");
            if (!isExamSubmitted) {
                document.querySelectorAll(".explain-box").forEach(b => b.classList.remove("show"));
            }
        }
    }

    // 9. Audio TTS Helper
    function speakQuestionAudio(itemId) {
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
        const item = getAllItems(exam).find(it => it.id === itemId);
        if (!item) return;

        let textToRead = "";
        if (item.type === "mc") {
            textToRead = item.prompt;
        } else if (item.type === "star") {
            textToRead = item.fullSentence || `${item.sentencePre} ${item.sentencePost}`;
        } else if (item.type === "trans") {
            textToRead = item.dir === "ja_to_vi" ? item.prompt : item.standard;
        } else if (item.type === "essay") {
            textToRead = item.prompt;
        }

        speakJapanese(textToRead);
    }

    // 10. Exam Submission & Scoring Engine
    function submitExam(isAuto = false) {
        const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
        const allItems = getAllItems(exam);

        if (!isAuto) {
            let unanswered = 0;
            allItems.forEach(it => {
                if (!isItemAnswered(it.id)) unanswered++;
            });

            if (unanswered > 0) {
                if (!confirm(`Bạn vẫn còn ${unanswered} câu chưa hoàn thành. Bạn có chắc chắn muốn nộp bài thi ngay không?`)) {
                    return;
                }
            } else {
                if (!confirm("Bạn đã hoàn thành tất cả câu hỏi! Bạn có muốn nộp bài để xem kết quả chi tiết không?")) {
                    return;
                }
            }
        }

        stopTimer();
        isExamSubmitted = true;

        // Calculate scores
        // Part 1: Vocab (10 items x 2.5 = 25 pts)
        // Part 2: Kanji (10 items x 2.0 = 20 pts)
        // Part 3: Grammar (12 items = 6x2.5 + 4x2.5 + 2x2.5 = 30 pts)
        // Part 4: Reading (2 items x 5.0 = 10 pts)
        // Part 5: Essay (2 items x 7.5 = 15 pts)
        // Total = 100 pts

        let totalScore = 0;
        let sectionScores = {
            sec1_vocab: { score: 0, max: 25, title: "Từ Vựng" },
            sec2_kanji: { score: 0, max: 20, title: "Kanji" },
            sec3_grammar: { score: 0, max: 30, title: "Ngữ Pháp" },
            sec4_reading: { score: 0, max: 10, title: "Đọc Hiểu" },
            sec5_essay: { score: 0, max: 15, title: "Tự Luận" }
        };

        allItems.forEach(item => {
            const st = userAnswers[item.id] || {};
            let isCorrect = false;

            if (item.type === "mc") {
                isCorrect = (st.value === item.correct);
            } else if (item.type === "star") {
                isCorrect = (st.value === item.correctOption);
            } else if (item.type === "trans") {
                isCorrect = (st.isCorrect !== undefined) ? st.isCorrect : evaluateTranslation(item, st.value || "");
            } else if (item.type === "essay") {
                isCorrect = (st.value && st.value.trim().length >= 10);
            }

            st.isCorrect = isCorrect;
            userAnswers[item.id] = st;

            if (isCorrect) {
                let pts = 0;
                if (item.id <= 10) pts = 2.5; // Vocab
                else if (item.id <= 20) pts = 2.0; // Kanji
                else if (item.id <= 32) pts = 2.5; // Grammar
                else if (item.id <= 34) pts = 5.0; // Reading
                else pts = 7.5; // Essay

                totalScore += pts;

                if (item.id <= 10) sectionScores.sec1_vocab.score += pts;
                else if (item.id <= 20) sectionScores.sec2_kanji.score += pts;
                else if (item.id <= 32) sectionScores.sec3_grammar.score += pts;
                else if (item.id <= 34) sectionScores.sec4_reading.score += pts;
                else sectionScores.sec5_essay.score += pts;
            }
        });

        totalScore = Math.round(totalScore * 10) / 10;
        const scoreOutOf10 = Math.round((totalScore / 10) * 10) / 10;
        const timeSpentSec = exam.timeLimit - timerSeconds;
        const m = Math.floor(timeSpentSec / 60);
        const s = timeSpentSec % 60;
        const timeSpentStr = `${m}m ${s}s`;

        // Save to History
        const record = {
            id: Date.now(),
            code: currentExamCode,
            examName: exam.name,
            totalScore: totalScore,
            scoreOutOf10: scoreOutOf10,
            timeSpent: timeSpentStr,
            date: new Date().toLocaleDateString("vi-VN", { hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit', year: 'numeric' })
        };
        saveHistory(record);
        updateHistoryBadge();

        // Render Result Modal
        showResultModal(totalScore, scoreOutOf10, timeSpentStr, sectionScores);
    }

    function showResultModal(score100, score10, timeStr, secScores) {
        const modal = document.getElementById("resultModal");
        if (!modal) return;

        const trophy = document.getElementById("modalTrophy");
        const bigScore = document.getElementById("modalScoreBig");
        const subScore = document.getElementById("modalScoreSub");
        const ratingPill = document.getElementById("modalRatingPill");
        const breakdown = document.getElementById("modalBreakdownGrid");
        const feedback = document.getElementById("modalFeedbackMsg");

        bigScore.textContent = `${score100} / 100`;
        subScore.textContent = `Điểm hệ số 10: ${score10.toFixed(1)} • Thời gian làm bài: ${timeStr}`;

        if (score100 >= 90) {
            trophy.textContent = "🏆";
            ratingPill.className = "modal-rating-pill rating-gold";
            ratingPill.textContent = "🌟 XUẤT SẮC (S GRADE)";
            feedback.textContent = "Quá đỉnh! Bạn đã nắm trọn vẹn 100% ngữ pháp, từ vựng và kỹ năng Can-do chuẩn thi giữa kỳ Marugoto A2-1!";
        } else if (score100 >= 80) {
            trophy.textContent = "🥇";
            ratingPill.className = "modal-rating-pill rating-green";
            ratingPill.textContent = "✨ GIỎI (A GRADE)";
            feedback.textContent = "Rất tốt! Bạn làm chủ hầu hết kiến thức bài 1-8. Chỉ cần chú ý thêm một vài câu bẫy nhỏ để đạt điểm tuyệt đối!";
        } else if (score100 >= 65) {
            trophy.textContent = "🥈";
            ratingPill.className = "modal-rating-pill rating-blue";
            ratingPill.textContent = "👍 KHÁ (B GRADE)";
            feedback.textContent = "Bạn đã đạt mức khá! Hãy bấm nút 'Xem Lại Bài Làm' bên dưới để ôn kỹ lại các câu sai và ghi nhớ kiến thức nhé.";
        } else {
            trophy.textContent = "💪";
            ratingPill.className = "modal-rating-pill rating-orange";
            ratingPill.textContent = "📚 CẦN CỐ GẮNG (C GRADE)";
            feedback.textContent = "Đừng nản lòng! Bạn hãy xem lại từng câu giải thích chi tiết, ôn lại từ vựng & ngữ pháp rồi bấm Làm lại đề nhé!";
        }

        let bdHtml = "";
        for (let k in secScores) {
            const sec = secScores[k];
            const p = Math.round((sec.score / sec.max) * 100);
            bdHtml += `
                <div class="breakdown-item">
                    <div class="breakdown-title">${sec.title}</div>
                    <div class="breakdown-score">${sec.score} <span style="font-size:0.8rem; color:#94a3b8;">/ ${sec.max}đ</span></div>
                    <div style="font-size:0.75rem; color:${p >= 80 ? '#10b981' : (p >= 60 ? '#f59e0b' : '#ef4444')}; font-weight:700; margin-top:2px;">
                        ${p}%
                    </div>
                </div>
            `;
        }
        breakdown.innerHTML = bdHtml;

        modal.classList.add("show");
    }

    function closeResultModal() {
        const modal = document.getElementById("resultModal");
        if (modal) modal.classList.remove("show");
    }

    function enterReviewMode() {
        closeResultModal();
        document.body.classList.add("review-mode");

        const exam = EXAMS_DATA.find(e => e.code === currentExamCode);
        const allItems = getAllItems(exam);

        allItems.forEach(item => {
            const st = userAnswers[item.id] || {};
            showItemExplanation(item.id);

            // Highlight options
            if (item.type === "mc") {
                const rightLbl = document.getElementById(`opt_lbl_${item.id}_${item.correct}`);
                if (rightLbl) rightLbl.classList.add("is-correct-ans");
                if (typeof st.value === "number" && st.value !== item.correct) {
                    const wrongLbl = document.getElementById(`opt_lbl_${item.id}_${st.value}`);
                    if (wrongLbl) wrongLbl.classList.add("is-wrong-ans");
                }
            } else if (item.type === "star") {
                const rightLbl = document.getElementById(`opt_lbl_${item.id}_${item.correctOption}`);
                if (rightLbl) rightLbl.classList.add("is-correct-ans");
                if (typeof st.value === "number" && st.value !== item.correctOption) {
                    const wrongLbl = document.getElementById(`opt_lbl_${item.id}_${st.value}`);
                    if (wrongLbl) wrongLbl.classList.add("is-wrong-ans");
                }
            }
        });

        // Scroll smoothly to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showToast("🔍 Đang ở Chế độ Xem Lại Chi Tiết (Review Mode)");
    }

    function confirmResetExam() {
        if (confirm("Bạn có chắc chắn muốn làm lại đề thi này từ đầu không?")) {
            clearDraft(currentExamCode);
            closeResultModal();
            loadExam(currentExamCode);
        }
    }

    // 11. Storage Helpers
    function saveDraft() {
        try {
            const data = {
                userAnswers,
                timerSeconds,
                updatedAt: Date.now()
            };
            localStorage.setItem(STORAGE_KEY_PREFIX + currentExamCode, JSON.stringify(data));
        } catch (e) {}
    }

    function loadDraft(code) {
        try {
            const s = localStorage.getItem(STORAGE_KEY_PREFIX + code);
            return s ? JSON.parse(s) : null;
        } catch (e) {
            return null;
        }
    }

    function clearDraft(code) {
        try {
            localStorage.removeItem(STORAGE_KEY_PREFIX + code);
        } catch (e) {}
    }

    function saveHistory(record) {
        try {
            let hist = getHistory();
            hist.unshift(record);
            if (hist.length > 20) hist = hist.slice(0, 20);
            localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(hist));
        } catch (e) {}
    }

    function getHistory() {
        try {
            const s = localStorage.getItem(HISTORY_STORAGE_KEY);
            return s ? JSON.parse(s) : [];
        } catch (e) {
            return [];
        }
    }

    function updateHistoryBadge() {
        const hist = getHistory();
        const b = document.getElementById("historyCountBadge");
        if (b) b.textContent = hist.length;
    }

    function openHistoryModal() {
        const m = document.getElementById("historyModal");
        const list = document.getElementById("historyListContainer");
        if (!m || !list) return;

        const hist = getHistory();
        if (hist.length === 0) {
            list.innerHTML = `<div style="text-align:center; padding:30px; color:#94a3b8;">Chưa có lần thi nào được lưu. Hãy bấm Nộp bài thi để lưu kết quả!</div>`;
        } else {
            list.innerHTML = hist.map(h => `
                <div class="history-row">
                    <div>
                        <div style="font-weight:800; color:#1e1b4b;">${h.examName}</div>
                        <div style="font-size:0.8rem; color:#64748b;">${h.date} • Thời gian: ${h.timeSpent}</div>
                    </div>
                    <div style="text-align:right;">
                        <span style="font-size:1.3rem; font-weight:900; color:${h.totalScore >= 80 ? '#10b981' : (h.totalScore >= 65 ? '#f59e0b' : '#ef4444')};">
                            ${h.totalScore}
                        </span>
                        <span style="font-size:0.85rem; color:#94a3b8;">/100đ</span>
                    </div>
                </div>
            `).join("");
        }

        m.classList.add("show");
    }

    function closeHistoryModal() {
        const m = document.getElementById("historyModal");
        if (m) m.classList.remove("show");
    }

    function clearAllHistory() {
        if (confirm("Bạn có chắc chắn muốn xóa toàn bộ lịch sử thi không?")) {
            localStorage.removeItem(HISTORY_STORAGE_KEY);
            updateHistoryBadge();
            openHistoryModal();
        }
    }

    function showToast(msg) {
        const t = document.getElementById("toastNotify");
        const m = document.getElementById("toastMsg");
        if (!t || !m) return;
        m.textContent = msg;
        t.classList.add("show");
        setTimeout(() => {
            t.classList.remove("show");
        }, 3000);
    }

    // 12. Utility Extractors
    function getAllItems(exam) {
        let items = [];
        exam.sections.forEach(sec => {
            items = items.concat(getSectionItems(sec));
        });
        return items;
    }

    function getSectionItems(sec) {
        let items = [];
        if (sec.groups) {
            sec.groups.forEach(g => {
                items = items.concat(g.items);
            });
        } else if (sec.items) {
            items = items.concat(sec.items);
        }
        return items;
    }
    </script>
    <script src="../assets/js/nav-dropdown.js"></script>
</body>
</html>
'''

with open('tests/De_Thi_Midterm_A2_1.html', 'w', encoding='utf-8') as f:
    f.write(HTML_TEMPLATE)

print("Created tests/De_Thi_Midterm_A2_1.html successfully!")
print(f"File size: {os.path.getsize('tests/De_Thi_Midterm_A2_1.html')} bytes")
