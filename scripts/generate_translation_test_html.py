#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
from build_lesson_1_10_translation_test import QUESTIONS_DATA

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="referrer" content="no-referrer">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✍️ Ôn Tập Dịch Câu Lesson 1 – 10 (Marugoto A2-1) • Chấm Điểm Thông Minh</title>
    <meta name="description" content="Hệ thống 40 câu luyện dịch Việt - Nhật trọn bộ Lesson 1 đến Lesson 10 Marugoto A2-1 (Topic 1 - 5). Chấm điểm thông minh, công bằng, linh hoạt, kèm phát âm Tokyo và giải thích cặn kẽ.">
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
            min-width: 280px;
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
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 45%, #312e81 100%);
            color: white;
            border-radius: var(--radius-lg);
            padding: 32px 28px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-md);
            position: relative;
            overflow: hidden;
        }

        .hero-banner::after {
            content: '翻訳練習';
            position: absolute;
            right: 25px;
            bottom: -25px;
            font-family: 'Noto Sans JP', sans-serif;
            font-size: 6.5rem;
            font-weight: 900;
            color: rgba(255, 255, 255, 0.04);
            pointer-events: none;
            line-height: 1;
        }

        .hero-badge {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            font-size: 0.82rem;
            font-weight: 800;
            padding: 4px 14px;
            border-radius: var(--radius-full);
            box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4);
            display: inline-block;
            margin-bottom: 10px;
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

        .hero-desc {
            font-size: 0.96rem;
            opacity: 0.94;
            max-width: 900px;
            margin-bottom: 18px;
            line-height: 1.6;
        }

        .hero-features {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .feature-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.84rem;
            font-weight: 600;
            backdrop-filter: blur(4px);
        }

        /* Fair Grading Callout */
        .fair-grading-card {
            background: #ffffff;
            border-radius: var(--radius-lg);
            border: 2px solid #818cf8;
            padding: 18px 22px;
            margin-bottom: 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.08);
        }

        .fair-left {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .fair-icon {
            font-size: 2.2rem;
            background: #eef2ff;
            width: 52px;
            height: 52px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .fair-title {
            font-weight: 800;
            color: #1e1b4b;
            font-size: 1.05rem;
            margin-bottom: 3px;
        }

        .fair-sub {
            font-size: 0.88rem;
            color: #475569;
            line-height: 1.5;
        }

        .fair-tags {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .fair-tag {
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 5px 12px;
            font-size: 0.8rem;
            font-weight: 700;
            color: #334155;
        }

        /* Filter Tabs */
        .filter-card {
            background: white;
            border-radius: var(--radius-lg);
            padding: 14px 20px;
            margin-bottom: 22px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }

        .filter-label {
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--gray-500);
            text-transform: uppercase;
            white-space: nowrap;
            margin-right: 6px;
        }

        .filter-btn {
            background: var(--gray-100);
            border: 1.5px solid var(--gray-300);
            border-radius: 9999px;
            padding: 8px 16px;
            font-size: 0.84rem;
            font-weight: 700;
            color: var(--gray-700);
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
        }

        .filter-btn:hover {
            border-color: var(--primary);
            color: var(--primary);
            background: var(--primary-light);
        }

        .filter-btn.active {
            background: var(--primary);
            border-color: var(--primary);
            color: white;
            box-shadow: 0 2px 8px rgba(79, 70, 229, 0.3);
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

        .progress-box {
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;
            min-width: 220px;
            max-width: 420px;
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

        .btn-action-primary {
            background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
            color: white;
            border: none;
            border-radius: var(--radius-full);
            padding: 10px 22px;
            font-size: 0.92rem;
            font-weight: 800;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 7px;
        }

        .btn-action-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(79, 70, 229, 0.4);
        }

        .btn-action-secondary {
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

        .btn-action-secondary:hover {
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
        }

        .palette-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(36px, 1fr));
            gap: 6px;
        }

        .q-bubble {
            height: 34px;
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
            border-color: #6366f1;
            background: #e0e7ff;
            color: #3730a3;
        }

        .q-bubble.graded-perfect {
            background: var(--success-light);
            border-color: var(--success);
            color: #065f46;
        }

        .q-bubble.graded-partial {
            background: var(--warning-light);
            border-color: var(--warning);
            color: #92400e;
        }

        .q-bubble.graded-wrong {
            background: var(--accent-light);
            border-color: var(--accent);
            color: #991b1b;
        }

        /* Question Cards */
        .q-card {
            background: white;
            border-radius: var(--radius-lg);
            padding: 22px 24px;
            margin-bottom: 22px;
            box-shadow: var(--shadow-sm);
            border: 1.5px solid var(--gray-200);
            transition: all 0.2s ease;
        }

        .q-card:hover {
            border-color: #cbd5e1;
        }

        .q-card.status-perfect {
            border-color: #10b981;
            background: #fafdfb;
        }

        .q-card.status-partial {
            border-color: #f59e0b;
            background: #fffdf9;
        }

        .q-card.status-wrong {
            border-color: #f43f5e;
            background: #fffafa;
        }

        .q-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            gap: 10px;
            flex-wrap: wrap;
        }

        .q-card-badge-group {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .q-card-num {
            background: var(--primary);
            color: white;
            font-size: 0.85rem;
            font-weight: 800;
            padding: 4px 12px;
            border-radius: 8px;
        }

        .q-card-topic {
            background: #f1f5f9;
            color: #475569;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
        }

        .q-score-badge {
            font-size: 0.85rem;
            font-weight: 800;
            padding: 4px 12px;
            border-radius: 9999px;
            display: none;
        }

        .q-score-badge.show { display: inline-block; }
        .score-100 { background: #d1fae5; color: #065f46; border: 1px solid #a7f3d0; }
        .score-85 { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
        .score-50 { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
        .score-0 { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }

        .q-prompt-vi {
            font-size: 1.05rem;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.6;
            margin-bottom: 14px;
            white-space: pre-line;
        }

        /* Dialogue Input Styling */
        .dialogue-turn-box {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 10px;
        }

        .speaker-badge {
            font-weight: 800;
            font-size: 0.95rem;
            width: 32px;
            height: 32px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            margin-top: 6px;
        }

        .speaker-a { background: #e0e7ff; color: #4338ca; border: 1px solid #c7d2fe; }
        .speaker-b { background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }

        .input-jp {
            width: 100%;
            padding: 12px 16px;
            border-radius: 10px;
            border: 1.5px solid var(--gray-300);
            font-size: 1.05rem;
            color: var(--dark);
            outline: none;
            transition: all 0.2s ease;
            background: white;
        }

        .input-jp:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
        }

        .textarea-jp {
            min-height: 90px;
            resize: vertical;
            line-height: 1.6;
        }

        /* Card Action Bar */
        .q-card-actions {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 14px;
            gap: 10px;
            flex-wrap: wrap;
        }

        .card-actions-left {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .btn-card-check {
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        .btn-card-check:hover {
            background: var(--primary-dark);
        }

        .btn-card-hint {
            background: var(--gray-100);
            color: var(--gray-700);
            border: 1px solid var(--gray-300);
            border-radius: 8px;
            padding: 8px 14px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .btn-card-hint:hover {
            background: var(--gray-200);
        }

        .btn-card-speak {
            background: white;
            color: var(--primary);
            border: 1.5px solid #c7d2fe;
            border-radius: 8px;
            padding: 8px 14px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        .btn-card-speak:hover {
            background: var(--primary-light);
        }

        .btn-self-override {
            background: #fffbeb;
            border: 1.5px solid #f59e0b;
            color: #b45309;
            border-radius: 8px;
            padding: 8px 14px;
            font-size: 0.82rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s ease;
            display: none;
            align-items: center;
            gap: 5px;
        }

        .btn-self-override:hover {
            background: #fef3c7;
            transform: translateY(-1px);
        }

        .btn-self-override.show {
            display: inline-flex;
        }

        /* Result & Explanation Feedback Box */
        .feedback-box {
            margin-top: 14px;
            padding: 16px 20px;
            border-radius: 12px;
            background: #f8fafc;
            border: 1.5px solid var(--gray-200);
            display: none;
            animation: fadeIn 0.25s ease;
        }

        .feedback-box.show {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .feedback-header {
            font-weight: 800;
            font-size: 0.95rem;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .model-answer-title {
            font-size: 0.8rem;
            font-weight: 800;
            color: var(--gray-500);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 4px;
        }

        .model-ja-text {
            font-size: 1.15rem;
            font-weight: 700;
            color: #1e1b4b;
            line-height: 1.7;
            margin-bottom: 4px;
        }

        .model-hira-text {
            font-size: 0.88rem;
            color: #64748b;
            margin-bottom: 10px;
        }

        .grammar-note {
            background: white;
            border-radius: 8px;
            padding: 10px 14px;
            border-left: 3px solid var(--primary);
            font-size: 0.86rem;
            color: var(--gray-700);
            line-height: 1.6;
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
            margin-bottom: 20px;
        }

        .modal-actions {
            display: flex;
            gap: 12px;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 24px;
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
            .hero-banner { padding: 24px 20px; }
            .hero-banner h1 { font-size: 1.45rem; }
            .control-bar { padding: 12px 14px; top: 10px; }
            .progress-box { order: 3; min-width: 100%; max-width: 100%; }
            .q-card { padding: 18px 16px; }
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
                <a href="De_Thi_Midterm_A2_1.html" class="hub-drop-link">🎯 Đề Thi Giữa Kỳ Midterm (Bảng M102)</a>
                <a href="On_Tap_Dich_Cau_Lesson_1_10.html" class="hub-drop-link active">✍️ Luyện Dịch Câu Bài 1 - 10 (40 Câu)</a>
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
            <span class="hero-badge">MARUGOTO PLUS A2-1 • TOPIC 1 ~ TOPIC 5</span>
            <h1>
                ✍️ Trọn Bộ 40 Câu Luyện Dịch Việt ➔ Nhật (Lesson 1 - 10)
            </h1>
            <p class="hero-desc">
                Hệ thống luyện dịch câu toàn diện chuẩn giáo trình Marugoto A2-1 và web chính thức Marugoto Plus. Chấm điểm thông minh, công bằng, linh hoạt theo ngữ nghĩa và trợ từ, có Tokyo Audio TTS phát âm từng câu và nút tự duyệt điểm khi bạn dùng từ đồng nghĩa hợp lệ!
            </p>
            <div class="hero-features">
                <span class="feature-pill">🎯 40 Câu Chuẩn Kiến Thức L1-L10</span>
                <span class="feature-pill">⚖️ Thuật Toán Chấm Điểm Công Bằng</span>
                <span class="feature-pill">🔊 Giọng Bản Xứ Tokyo TTS</span>
                <span class="feature-pill">💾 Tự Động Lưu Nháp Trình Duyệt</span>
            </div>
        </header>

        <!-- Fair Grading Callout -->
        <div class="fair-grading-card">
            <div class="fair-left">
                <div class="fair-icon">⚖️</div>
                <div>
                    <div class="fair-title">Cơ Chế Chấm Điểm Công Bằng & Linh Hoạt (Không Chấm Máy Móc)</div>
                    <div class="fair-sub">
                        Hệ thống chấp nhận cả <strong>Kanji</strong> lẫn <strong>Hiragana</strong>, bỏ qua khoảng cách và dấu câu, tự nhận diện cấu trúc ngữ pháp tương đương. Nếu bạn dùng từ vựng đồng nghĩa tự nhiên, bạn có thể bấm nút <strong>🎯 Tôi Thấy Mình Đúng</strong> để tự nhận trọn vẹn điểm!
                    </div>
                </div>
            </div>
            <div class="fair-tags">
                <span class="fair-tag">✓ Không phạt thiếu dấu cách/chấm câu</span>
                <span class="fair-tag">✓ Hỗ trợ cả chữ Hán & Hiragana</span>
                <span class="fair-tag">✓ Đối chiếu hội thoại A/B độc lập</span>
                <span class="fair-tag">✓ Quyền tự quyết điểm số</span>
            </div>
        </div>

        <!-- Filter Tabs -->
        <div class="filter-card">
            <span class="filter-label">LỌC CHỦ ĐỀ:</span>
            <button type="button" class="filter-btn active" onclick="filterTopic('all')">Tất Cả (40 Câu)</button>
            <button type="button" class="filter-btn" onclick="filterTopic('topic1')">Topic 1: Gia Đình & Nơi Sống</button>
            <button type="button" class="filter-btn" onclick="filterTopic('topic2')">Topic 2: Thói Quen & Ngoại Ngữ</button>
            <button type="button" class="filter-btn" onclick="filterTopic('topic3')">Topic 3: Nơi Chốn & Chỉ Đường</button>
            <button type="button" class="filter-btn" onclick="filterTopic('topic4')">Topic 4: Mua Sắm & Quà Tặng</button>
            <button type="button" class="filter-btn" onclick="filterTopic('topic5')">Topic 5: Ẩm Thực, Khí Hậu & So Sánh</button>
        </div>

        <!-- Sticky Control Bar -->
        <div class="control-bar">
            <div class="progress-box">
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" id="progressBarFill"></div>
                </div>
                <span class="progress-text" id="progressText">0 / 40 câu đã làm (0%)</span>
            </div>

            <div class="control-actions">
                <button type="button" class="btn-action-secondary" onclick="unlockAllAnswers()">
                    👁️ Xem Toàn Bộ Đáp Án Mẫu
                </button>
                <button type="button" class="btn-action-secondary" onclick="confirmResetAll()">
                    🔄 Làm Lại Từ Đầu
                </button>
                <button type="button" class="btn-action-primary" onclick="gradeAllQuestions()">
                    ✅ Chấm Toàn Bộ 40 Câu
                </button>
            </div>
        </div>

        <!-- Quick Question Navigation Palette -->
        <div class="q-palette-card">
            <div class="q-palette-header">
                <span class="q-palette-title">🧭 BẢNG ĐIỀU HƯỚNG CÂU HỎI (Bấm để nhảy nhanh)</span>
                <div style="font-size:0.82rem; color:#64748b;">
                    <span style="color:#10b981;">● Xanh: 100%</span> • 
                    <span style="color:#f59e0b;">● Vàng: Khá</span> • 
                    <span style="color:#6366f1;">● Tím: Đã gõ</span> • 
                    <span style="color:#94a3b8;">● Xám: Chưa làm</span>
                </div>
            </div>
            <div class="palette-grid" id="paletteGrid">
                <!-- Rendered dynamically -->
            </div>
        </div>

        <!-- Question Cards List -->
        <main id="questionsContainer">
            <!-- Rendered dynamically -->
        </main>
    </div>

    <!-- RESULT MODAL -->
    <div class="modal-overlay" id="resultModal">
        <div class="modal-card">
            <button type="button" class="modal-close-btn" onclick="closeResultModal()">✕</button>
            <div style="font-size:3.5rem; margin-bottom:8px;">🏆</div>
            <div class="modal-score-big" id="modalScoreBig">92 / 100</div>
            <div class="modal-score-sub" id="modalScoreSub">Hoàn thành 40 / 40 câu dịch Marugoto L1 - 10</div>
            
            <p style="font-size:0.95rem; color:#475569; line-height:1.6;" id="modalFeedbackText">
                Chúc mừng bạn đã hoàn thành bài luyện dịch! Toàn bộ câu hỏi đã được hiển thị câu mẫu chuẩn và giải thích chi tiết.
            </p>

            <div class="modal-actions">
                <button type="button" class="btn-modal-action btn-modal-review" onclick="closeResultModal()">
                    🔍 Xem Lại Bài Làm
                </button>
                <button type="button" class="btn-modal-action btn-modal-retry" onclick="confirmResetAll()">
                    🔄 Làm Lại
                </button>
            </div>
        </div>
    </div>

    <!-- TOAST NOTIFICATION -->
    <div class="toast-notify" id="toastNotify">
        <span>💾</span>
        <span id="toastMsg">Đã tự động lưu nháp câu trả lời</span>
    </div>

    <!-- AUDIO ENGINE (Dual Tokyo Speech) -->
    <script src="../assets/js/audio-engine.js"></script>

    <!-- QUESTIONS DATA & CONTROLLER JS -->
    <script>
    const QUESTIONS = ''' + json.dumps(QUESTIONS_DATA, ensure_ascii=False) + ''';
    ''' + '''
    let userAnswers = {}; // { [id]: { text, textA, textB, score, status, selfApproved } }
    let activeFilter = "all";
    const STORAGE_KEY = "marugoto_l1_l10_translation_draft_v1";

    // 1. Initialization
    document.addEventListener("DOMContentLoaded", () => {
        loadDraft();
        renderPalette();
        renderQuestions();
        updateProgress();
    });

    // 2. Draft Storage
    function saveDraft() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(userAnswers));
            showToast("💾 Đã tự động lưu bài làm");
        } catch (e) {}
    }

    function loadDraft() {
        try {
            const s = localStorage.getItem(STORAGE_KEY);
            if (s) {
                userAnswers = JSON.parse(s);
            }
        } catch (e) {}
    }

    function confirmResetAll() {
        if (confirm("Bạn có chắc chắn muốn xóa tất cả câu trả lời và làm lại từ đầu không?")) {
            userAnswers = {};
            localStorage.removeItem(STORAGE_KEY);
            closeResultModal();
            renderPalette();
            renderQuestions();
            updateProgress();
            showToast("🔄 Đã làm mới toàn bộ bài làm");
        }
    }

    // 3. Render Palette
    function renderPalette() {
        const grid = document.getElementById("paletteGrid");
        if (!grid) return;
        grid.innerHTML = QUESTIONS.map(q => {
            const st = userAnswers[q.id] || {};
            let statusClass = "";
            if (st.selfApproved || st.score === 100) {
                statusClass = "graded-perfect";
            } else if (st.score >= 50) {
                statusClass = "graded-partial";
            } else if (st.score !== undefined && st.score < 50) {
                statusClass = "graded-wrong";
            } else if (isItemFilled(q.id)) {
                statusClass = "answered";
            }

            return `
                <a href="#q_card_${q.id}" class="q-bubble ${statusClass}" id="palette_bubble_${q.id}">
                    ${q.id}
                </a>
            `;
        }).join("");
    }

    function updatePaletteBubble(qId) {
        const b = document.getElementById(`palette_bubble_${qId}`);
        if (!b) return;
        const st = userAnswers[qId] || {};
        b.className = "q-bubble";
        if (st.selfApproved || st.score === 100) {
            b.classList.add("graded-perfect");
        } else if (st.score >= 50) {
            b.classList.add("graded-partial");
        } else if (st.score !== undefined && st.score < 50) {
            b.classList.add("graded-wrong");
        } else if (isItemFilled(qId)) {
            b.classList.add("answered");
        }
    }

    function isItemFilled(qId) {
        const st = userAnswers[qId];
        if (!st) return false;
        if (st.text && st.text.trim().length > 0) return true;
        if ((st.textA && st.textA.trim().length > 0) || (st.textB && st.textB.trim().length > 0)) return true;
        return false;
    }

    function updateProgress() {
        const total = QUESTIONS.length;
        let filledCount = 0;
        QUESTIONS.forEach(q => {
            if (isItemFilled(q.id)) filledCount++;
        });

        const pct = Math.round((filledCount / total) * 100);
        const fill = document.getElementById("progressBarFill");
        const txt = document.getElementById("progressText");
        if (fill) fill.style.width = `${pct}%`;
        if (txt) txt.textContent = `${filledCount} / ${total} câu đã làm (${pct}%)`;
    }

    // 4. Render Questions
    function renderQuestions() {
        const main = document.getElementById("questionsContainer");
        if (!main) return;

        let html = "";
        QUESTIONS.forEach(q => {
            const isHidden = !matchFilter(q, activeFilter);
            const st = userAnswers[q.id] || {};

            let cardStatusClass = "";
            let scoreBadgeHtml = "";
            if (st.selfApproved || st.score === 100) {
                cardStatusClass = "status-perfect";
                scoreBadgeHtml = `<span class="q-score-badge score-100 show">🌟 100% Xuất sắc</span>`;
            } else if (st.score >= 80) {
                cardStatusClass = "status-perfect";
                scoreBadgeHtml = `<span class="q-score-badge score-85 show">👍 ${st.score}% Rất tốt</span>`;
            } else if (st.score >= 50) {
                cardStatusClass = "status-partial";
                scoreBadgeHtml = `<span class="q-score-badge score-50 show">⚠️ ${st.score}% Khá</span>`;
            } else if (st.score !== undefined) {
                cardStatusClass = "status-wrong";
                scoreBadgeHtml = `<span class="q-score-badge score-0 show">❌ Cần xem lại</span>`;
            }

            html += `
                <div class="q-card ${cardStatusClass}" id="q_card_${q.id}" style="${isHidden ? 'display:none;' : ''}">
                    <div class="q-card-header">
                        <div class="q-card-badge-group">
                            <span class="q-card-num">CÂU ${q.id}</span>
                            <span class="q-card-topic">${q.topic}</span>
                        </div>
                        <div id="score_badge_${q.id}">
                            ${scoreBadgeHtml}
                        </div>
                    </div>

                    <div class="q-prompt-vi">${q.vi}</div>
            `;

            // Inputs
            if (q.type === "dialogue") {
                html += `
                    <div class="dialogue-turn-box">
                        <div class="speaker-badge speaker-a">A</div>
                        <input type="text" class="input-jp jp-text" id="input_${q.id}_a" 
                               placeholder="Nhập câu tiếng Nhật của A..." 
                               value="${escapeHtml(st.textA || '')}"
                               oninput="handleInputDialogue(${q.id}, 'A', this.value)">
                    </div>
                    <div class="dialogue-turn-box">
                        <div class="speaker-badge speaker-b">B</div>
                        <input type="text" class="input-jp jp-text" id="input_${q.id}_b" 
                               placeholder="Nhập câu tiếng Nhật của B..." 
                               value="${escapeHtml(st.textB || '')}"
                               oninput="handleInputDialogue(${q.id}, 'B', this.value)">
                    </div>
                `;
            } else if (q.type === "paragraph") {
                html += `
                    <textarea class="input-jp textarea-jp jp-text" id="input_${q.id}" 
                              placeholder="Nhập đoạn văn tiếng Nhật..." 
                              oninput="handleInputSingle(${q.id}, this.value)">${escapeHtml(st.text || '')}</textarea>
                `;
            } else {
                html += `
                    <input type="text" class="input-jp jp-text" id="input_${q.id}" 
                           placeholder="Nhập câu tiếng Nhật..." 
                           value="${escapeHtml(st.text || '')}"
                           oninput="handleInputSingle(${q.id}, this.value)">
                `;
            }

            // Action row
            html += `
                <div class="q-card-actions">
                    <div class="card-actions-left">
                        <button type="button" class="btn-card-check" onclick="checkSingleQuestion(${q.id})">
                            🔍 Kiểm Tra Câu Này
                        </button>
                        <button type="button" class="btn-card-hint" onclick="toggleHint(${q.id})">
                            💡 Gợi Ý & Đáp Án Mẫu
                        </button>
                        <button type="button" class="btn-card-speak" onclick="speakQuestionModel(${q.id})">
                            🔊 Nghe Tiếng Nhật (Tokyo)
                        </button>
                    </div>
                    <div>
                        <button type="button" class="btn-self-override ${st.score !== undefined && st.score < 100 && !st.selfApproved ? 'show' : ''}" 
                                id="btn_self_${q.id}" onclick="selfApproveQuestion(${q.id})">
                            🎯 Tôi Viết Đúng (Nhận Điểm)
                        </button>
                    </div>
                </div>

                <!-- Feedback & Model Answer -->
                <div class="feedback-box ${st.score !== undefined || st.showModel ? 'show' : ''}" id="feedback_${q.id}">
                    <div id="feedback_content_${q.id}">
                        ${renderFeedbackContent(q, st)}
                    </div>
                </div>
            </div>`;
        });

        main.innerHTML = html;
    }

    function renderFeedbackContent(q, st) {
        if (!st.score && !st.showModel && !st.selfApproved) {
            return `
                <div class="model-answer-title">🌟 CÂU MẪU CHUẨN MARUGOTO:</div>
                <div class="model-ja-text jp-text">${renderModelSentence(q)}</div>
                <div class="model-hira-text jp-text">${renderModelHiragana(q)}</div>
                <div class="grammar-note"><strong>📌 Trọng tâm ngữ pháp:</strong> ${q.grammarPoint}</div>
            `;
        }

        let evalMsg = "";
        let evalColor = "#10b981";
        if (st.selfApproved) {
            evalMsg = "🎯 Bạn đã tự duyệt câu này là chính xác!";
            evalColor = "#b45309";
        } else if (st.score === 100) {
            evalMsg = "🌟 Xuất sắc! Câu dịch chính xác hoàn hảo chuẩn Marugoto.";
            evalColor = "#059669";
        } else if (st.score >= 80) {
            evalMsg = `👍 Rất tốt (${st.score}%)! Đúng ngữ nghĩa và cấu trúc, có thể khác nhẹ cách diễn đạt.`;
            evalColor = "#0284c7";
        } else if (st.score >= 50) {
            evalMsg = `⚠️ Khá (${st.score}%)! Bạn đã viết đúng một số từ khóa, hãy so sánh với câu mẫu bên dưới nhé.`;
            evalColor = "#d97706";
        } else {
            evalMsg = "❌ Cần xem lại! Hãy đọc kỹ câu mẫu và giải thích bên dưới để ôn lại cấu trúc.";
            evalColor = "#dc2626";
        }

        return `
            <div style="font-size:0.95rem; font-weight:800; color:${evalColor}; margin-bottom:10px;">
                ${evalMsg}
            </div>
            <div class="model-answer-title">🌟 CÂU MẪU CHUẨN MARUGOTO:</div>
            <div class="model-ja-text jp-text">${renderModelSentence(q)}</div>
            <div class="model-hira-text jp-text">${renderModelHiragana(q)}</div>
            <div class="grammar-note"><strong>📌 Trọng tâm ngữ pháp:</strong> ${q.grammarPoint}</div>
        `;
    }

    function renderModelSentence(q) {
        if (q.type === "dialogue") {
            return `A: ${q.modelA}<br>B: ${q.modelB}`;
        }
        return q.modelJa;
    }

    function renderModelHiragana(q) {
        if (q.type === "dialogue") {
            return `A: ${q.modelHiraganaA}<br>B: ${q.modelHiraganaB}`;
        }
        return q.modelHiragana || "";
    }

    // 5. Input Handlers
    function handleInputSingle(qId, val) {
        userAnswers[qId] = {
            ...(userAnswers[qId] || {}),
            text: val
        };
        updatePaletteBubble(qId);
        updateProgress();
        saveDraft();
    }

    function handleInputDialogue(qId, speaker, val) {
        userAnswers[qId] = userAnswers[qId] || {};
        if (speaker === "A") userAnswers[qId].textA = val;
        if (speaker === "B") userAnswers[qId].textB = val;
        updatePaletteBubble(qId);
        updateProgress();
        saveDraft();
    }

    // 6. Intelligent Fair Grading Algorithm
    function normalizeJp(s) {
        if (!s) return "";
        return s
            .toLowerCase()
            .replace(/[\\s、。,.?!！？「」『』〜~・（）\(\)]/g, "")
            .replace(/[A-Za-z]/g, ch => ch.toLowerCase());
    }

    // Helper: Match text against target with に/へ particle tolerance and minor variation tolerance
    function isTextFuzzyMatch(userNorm, targetNorm) {
        if (!userNorm || !targetNorm) return false;
        if (userNorm === targetNorm || userNorm.includes(targetNorm) || targetNorm.includes(userNorm)) return true;
        // Trợ từ chuyển động: に <-> へ tương đương hoàn toàn
        const userAlt = userNorm.replace(/へ/g, 'に');
        const targetAlt = targetNorm.replace(/へ/g, 'に');
        if (userAlt === targetAlt || userAlt.includes(targetAlt) || targetAlt.includes(userAlt)) return true;
        // ですが <-> んですが tương đương
        const userDesu = userAlt.replace(/んですが/g, 'ですが');
        const targetDesu = targetAlt.replace(/んですが/g, 'ですが');
        if (userDesu === targetDesu || userDesu.includes(targetDesu) || targetDesu.includes(userDesu)) return true;
        return false;
    }

    function evaluateAnswer(q, userState) {
        const normAcceptable = (q.acceptable || []).map(normalizeJp);

        if (q.type === "dialogue") {
            const rawA = userState.textA || "";
            const rawB = userState.textB || "";
            const normA = normalizeJp(rawA);
            const normB = normalizeJp(rawB);

            if (!rawA.trim() && !rawB.trim()) {
                return 0;
            }

            // Direct acceptable check for dialogue
            const accListA = (q.acceptableA || []).map(normalizeJp);
            const accListB = (q.acceptableB || []).map(normalizeJp);
            const matchAccA = accListA.some(acc => isTextFuzzyMatch(normA, acc));
            const matchAccB = accListB.some(acc => isTextFuzzyMatch(normB, acc));

            if (matchAccA && matchAccB) {
                return 100;
            }

            // Keyword count for A with Kanji & Hiragana support + に/へ particle tolerance
            const kwA = q.keywordsA || [];
            const kwHiraA = q.keywordsHiraA || [];
            let matchA = matchAccA ? kwA.length : 0;
            if (!matchAccA) {
                for (let i = 0; i < kwA.length; i++) {
                    const k1 = normalizeJp(kwA[i]);
                    const k2 = kwHiraA[i] ? normalizeJp(kwHiraA[i]) : "";
                    if (isTextFuzzyMatch(normA, k1) || (k2 && isTextFuzzyMatch(normA, k2))) {
                        matchA++;
                    }
                }
            }

            // Keyword count for B with Kanji & Hiragana support + に/へ particle tolerance
            const kwB = q.keywordsB || [];
            const kwHiraB = q.keywordsHiraB || [];
            let matchB = matchAccB ? kwB.length : 0;
            if (!matchAccB) {
                for (let i = 0; i < kwB.length; i++) {
                    const k1 = normalizeJp(kwB[i]);
                    const k2 = kwHiraB[i] ? normalizeJp(kwHiraB[i]) : "";
                    if (isTextFuzzyMatch(normB, k1) || (k2 && isTextFuzzyMatch(normB, k2))) {
                        matchB++;
                    }
                }
            }

            const ratioA = kwA.length > 0 ? (matchA / kwA.length) : (normA.length > 3 ? 1 : 0);
            const ratioB = kwB.length > 0 ? (matchB / kwB.length) : (normB.length > 3 ? 1 : 0);
            const totalRatio = (ratioA + ratioB) / 2;

            if (totalRatio >= 0.70 || (matchAccA && ratioB >= 0.6) || (matchAccB && ratioA >= 0.6)) return 100;
            if (totalRatio >= 0.50) return 85;
            if (totalRatio >= 0.35) return 50;
            return 25;
        } else {
            const raw = userState.text || "";
            const norm = normalizeJp(raw);
            if (!raw.trim()) return 0;

            // Direct acceptable match with particle equivalence
            if (normAcceptable.some(acc => isTextFuzzyMatch(norm, acc))) {
                return 100;
            }

            // Keyword matching with Kanji and Hiragana support
            const kws = q.keywords || [];
            const kwsHira = q.keywordsHira || [];
            let matches = 0;

            for (let i = 0; i < kws.length; i++) {
                const k1 = normalizeJp(kws[i]);
                const k2 = kwsHira[i] ? normalizeJp(kwsHira[i]) : "";
                if (isTextFuzzyMatch(norm, k1) || (k2 && isTextFuzzyMatch(norm, k2))) {
                    matches++;
                }
            }

            const ratio = kws.length > 0 ? (matches / kws.length) : 1;
            if (ratio >= 0.75) return 100;
            if (ratio >= 0.55) return 85;
            if (ratio >= 0.35) return 50;
            return 20;
        }
    }

    function checkSingleQuestion(qId) {
        const q = QUESTIONS.find(item => item.id === qId);
        if (!q) return;

        const st = userAnswers[qId] || {};
        const score = evaluateAnswer(q, st);
        st.score = score;
        st.showModel = true;
        userAnswers[qId] = st;

        updateQuestionCardUI(qId);
        updatePaletteBubble(qId);
        updateProgress();
        saveDraft();
    }

    function updateQuestionCardUI(qId) {
        const q = QUESTIONS.find(item => item.id === qId);
        const st = userAnswers[qId] || {};
        const card = document.getElementById(`q_card_${qId}`);
        const badgeBox = document.getElementById(`score_badge_${qId}`);
        const feedbackBox = document.getElementById(`feedback_${qId}`);
        const feedbackContent = document.getElementById(`feedback_content_${qId}`);
        const selfBtn = document.getElementById(`btn_self_${qId}`);

        if (!card) return;

        card.className = "q-card";
        if (st.selfApproved || st.score === 100) {
            card.classList.add("status-perfect");
            if (badgeBox) badgeBox.innerHTML = `<span class="q-score-badge score-100 show">🌟 100% Xuất sắc</span>`;
        } else if (st.score >= 80) {
            card.classList.add("status-perfect");
            if (badgeBox) badgeBox.innerHTML = `<span class="q-score-badge score-85 show">👍 ${st.score}% Rất tốt</span>`;
        } else if (st.score >= 50) {
            card.classList.add("status-partial");
            if (badgeBox) badgeBox.innerHTML = `<span class="q-score-badge score-50 show">⚠️ ${st.score}% Khá</span>`;
        } else if (st.score !== undefined) {
            card.classList.add("status-wrong");
            if (badgeBox) badgeBox.innerHTML = `<span class="q-score-badge score-0 show">❌ Cần xem lại</span>`;
        }

        if (feedbackBox && feedbackContent) {
            feedbackContent.innerHTML = renderFeedbackContent(q, st);
            feedbackBox.classList.add("show");
        }

        // Show self override button if graded < 100
        if (selfBtn) {
            if (st.score !== undefined && st.score < 100 && !st.selfApproved) {
                selfBtn.classList.add("show");
            } else {
                selfBtn.classList.remove("show");
            }
        }
    }

    function selfApproveQuestion(qId) {
        userAnswers[qId] = {
            ...(userAnswers[qId] || {}),
            selfApproved: true,
            score: 100
        };
        updateQuestionCardUI(qId);
        updatePaletteBubble(qId);
        saveDraft();
        showToast("🎯 Đã tự duyệt điểm 100% cho câu " + qId);
    }

    function toggleHint(qId) {
        const q = QUESTIONS.find(item => item.id === qId);
        if (!q) return;
        const st = userAnswers[qId] || {};
        st.showModel = !st.showModel;
        userAnswers[qId] = st;

        const fb = document.getElementById(`feedback_${qId}`);
        const fc = document.getElementById(`feedback_content_${qId}`);
        if (fb && fc) {
            fc.innerHTML = renderFeedbackContent(q, st);
            fb.classList.toggle("show");
        }
    }

    function unlockAllAnswers() {
        QUESTIONS.forEach(q => {
            userAnswers[q.id] = {
                ...(userAnswers[q.id] || {}),
                showModel: true
            };
            const fb = document.getElementById(`feedback_${q.id}`);
            const fc = document.getElementById(`feedback_content_${q.id}`);
            if (fb && fc) {
                fc.innerHTML = renderFeedbackContent(q, userAnswers[q.id]);
                fb.classList.add("show");
            }
        });
        showToast("👁️ Đã hiển thị toàn bộ 40 câu mẫu chuẩn");
    }

    function gradeAllQuestions() {
        let totalScore = 0;
        QUESTIONS.forEach(q => {
            const st = userAnswers[q.id] || {};
            let s = 0;
            if (st.selfApproved) {
                s = 100;
            } else {
                s = evaluateAnswer(q, st);
            }
            st.score = s;
            st.showModel = true;
            userAnswers[q.id] = st;
            updateQuestionCardUI(q.id);
            updatePaletteBubble(q.id);
            totalScore += s;
        });

        const avgScore = Math.round(totalScore / QUESTIONS.length);
        const scoreOutOf10 = (avgScore / 10).toFixed(1);

        saveDraft();
        updateProgress();

        // Show Modal
        const modal = document.getElementById("resultModal");
        const big = document.getElementById("modalScoreBig");
        const sub = document.getElementById("modalScoreSub");
        const msg = document.getElementById("modalFeedbackText");

        if (big) big.textContent = `${avgScore} / 100`;
        if (sub) sub.textContent = `Điểm hệ số 10: ${scoreOutOf10} • Đã chấm toàn bộ 40 câu`;
        if (msg) {
            if (avgScore >= 85) {
                msg.textContent = "🌟 Quá xuất sắc! Bạn đã làm chủ hoàn hảo năng lực dịch thuật và ngữ pháp Marugoto A2-1 từ Bài 1 đến Bài 10!";
            } else if (avgScore >= 70) {
                msg.textContent = "👍 Rất tốt! Bạn nắm vững hầu hết các mẫu câu trọng điểm. Hãy xem lại các câu chưa tròn điểm và bấm nút 'Tôi thấy mình đúng' nếu bạn dùng từ đồng nghĩa nhé.";
            } else {
                msg.textContent = "💪 Bạn đã hoàn thành bài tập! Hãy cuộn qua từng câu để so sánh với câu mẫu và ghi nhớ những cấu trúc quan trọng nhé.";
            }
        }

        if (modal) modal.classList.add("show");
    }

    function closeResultModal() {
        const modal = document.getElementById("resultModal");
        if (modal) modal.classList.remove("show");
    }

    // 7. Tokyo Audio TTS Helper
    function speakQuestionModel(qId) {
        const q = QUESTIONS.find(item => item.id === qId);
        if (!q) return;

        let text = "";
        if (q.type === "dialogue") {
            text = `${q.modelA}。${q.modelB}`;
        } else {
            text = q.modelJa;
        }

        speakJapanese(text);
    }

    // 8. Filter by Topic
    function filterTopic(topicKey) {
        activeFilter = topicKey;
        document.querySelectorAll(".filter-btn").forEach(btn => btn.classList.remove("active"));
        if (window.event && window.event.target) {
            window.event.target.classList.add("active");
        }

        QUESTIONS.forEach(q => {
            const card = document.getElementById(`q_card_${q.id}`);
            if (card) {
                card.style.display = matchFilter(q, topicKey) ? "block" : "none";
            }
        });
    }

    function matchFilter(q, key) {
        if (key === "all") return true;
        if (key === "topic1" && q.topic.includes("Topic 1")) return true;
        if (key === "topic2" && q.topic.includes("Topic 2")) return true;
        if (key === "topic3" && q.topic.includes("Topic 3")) return true;
        if (key === "topic4" && q.topic.includes("Topic 4")) return true;
        if (key === "topic5" && q.topic.includes("Topic 5")) return true;
        return false;
    }

    function escapeHtml(str) {
        if (!str) return "";
        return str
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
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

    // Dropdown Toggles for Hub Nav
    function toggleTestsDropdown(e) {
        if (e) e.stopPropagation();
        const m = document.getElementById('testsDropdownMenu');
        if (m) m.classList.toggle('show');
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
    }
    function toggleLessonsDropdown(e) {
        if (e) e.stopPropagation();
        const m = document.getElementById('lessonsDropdownMenu');
        if (m) m.classList.toggle('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    }
    window.addEventListener('click', () => {
        const lm = document.getElementById('lessonsDropdownMenu');
        if (lm) lm.classList.remove('show');
        const tm = document.getElementById('testsDropdownMenu');
        if (tm) tm.classList.remove('show');
    });
    </script>
</body>
</html>
'''

with open('tests/On_Tap_Dich_Cau_Lesson_1_10.html', 'w', encoding='utf-8') as f:
    f.write(HTML_TEMPLATE)

print("Created tests/On_Tap_Dich_Cau_Lesson_1_10.html successfully!")
print(f"File size: {os.path.getsize('tests/On_Tap_Dich_Cau_Lesson_1_10.html')} bytes")
