#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for all 18 Web Bai Hoc lessons and the global navigation dropdown.
"""

import os
import sys
from playwright.sync_api import sync_playwright

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ARTIFACT_DIR = "/Users/dangvu/.gemini/antigravity/brain/5974a0ad-3eac-4559-908a-5f38f533f9e9"

def run_verification():
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        # Listen to console errors
        def on_console(msg):
            if msg.type == 'error':
                print(f"Console error: {msg.text}")
                errors.append(msg.text)
        page.on('console', on_console)

        # 1. Open Tu_Vung page
        tu_vung_url = f"file://{WORKSPACE}/Tu_Vung_Marugoto_A1_16_A2_1_10.html"
        print(f"Loading {tu_vung_url}...")
        page.goto(tu_vung_url, wait_until='networkidle')

        # Click Web Bai Hoc dropdown
        dropdown_btn = page.locator("button:has-text('Web Bài Học')")
        dropdown_btn.click()
        page.wait_for_selector("#lessonsDropdownMenu.show", timeout=3000)

        # Count links in dropdown
        menu_links = page.locator("#lessonsDropdownMenu a.hub-drop-link")
        count = menu_links.count()
        print(f"Dropdown link count: {count}")
        assert count == 18, f"Expected 18 links, got {count}"

        # Capture dropdown screenshot
        ss_dropdown = os.path.join(ARTIFACT_DIR, "nav_dropdown_18_lessons.png")
        page.screenshot(path=ss_dropdown)
        print(f"Saved dropdown screenshot to: {ss_dropdown}")

        # 2. Test clicking Lesson 1
        lesson1_link = page.locator("#lessonsDropdownMenu a:has-text('Bài 1:')")
        lesson1_link.click()
        page.wait_for_load_state('networkidle')
        print(f"Current URL: {page.url}")
        assert "Marugoto_A2_Lesson_1.html" in page.url

        # Check Lesson 1 components
        assert page.locator("h1:has-text('CHINH PHỤC TOÀN DIỆN BÀI 1')").is_visible()
        assert page.locator(".flashcard-grid").is_visible()
        assert page.locator("#sec-grammar1").is_visible()
        assert page.locator("#sec-verb-lab").is_visible()
        assert page.locator("#sec-kanji").is_visible()
        assert page.locator("#sec-quiz").is_visible()

        ss_lesson1 = os.path.join(ARTIFACT_DIR, "lesson_1_full_view.png")
        page.screenshot(path=ss_lesson1)
        print(f"Saved Lesson 1 screenshot to: {ss_lesson1}")

        # 3. Test Lesson 5 via navbar dropdown
        page.locator("button:has-text('Web Bài Học')").click()
        page.wait_for_selector("#lessonsDropdownMenu.show", timeout=3000)
        page.locator("#lessonsDropdownMenu a:has-text('Bài 5:')").click()
        page.wait_for_load_state('networkidle')
        print(f"Current URL: {page.url}")
        assert "Marugoto_A2_Lesson_5.html" in page.url
        assert page.locator("h1:has-text('CHINH PHỤC TOÀN DIỆN BÀI 5')").is_visible()

        ss_lesson5 = os.path.join(ARTIFACT_DIR, "lesson_5_full_view.png")
        page.screenshot(path=ss_lesson5)
        print(f"Saved Lesson 5 screenshot to: {ss_lesson5}")

        # 4. Test Lesson 9 via navbar dropdown
        page.locator("button:has-text('Web Bài Học')").click()
        page.wait_for_selector("#lessonsDropdownMenu.show", timeout=3000)
        page.locator("#lessonsDropdownMenu a:has-text('Bài 9:')").click()
        page.wait_for_load_state('networkidle')
        print(f"Current URL: {page.url}")
        assert "Marugoto_A2_Lesson_9.html" in page.url
        assert page.locator("h1:has-text('CHINH PHỤC TOÀN DIỆN BÀI 9')").is_visible()

        ss_lesson9 = os.path.join(ARTIFACT_DIR, "lesson_9_full_view.png")
        page.screenshot(path=ss_lesson9)
        print(f"Saved Lesson 9 screenshot to: {ss_lesson9}")

        # 5. Test Lesson 13 (one of the original lessons 10-18)
        page.locator("button:has-text('Web Bài Học')").click()
        page.wait_for_selector("#lessonsDropdownMenu.show", timeout=3000)
        page.locator("#lessonsDropdownMenu a:has-text('Bài 13:')").click()
        page.wait_for_load_state('networkidle')
        print(f"Current URL: {page.url}")
        assert "Marugoto_A2_Lesson_13.html" in page.url
        assert page.locator("h1:has-text('CHINH PHỤC TOÀN DIỆN BÀI 13')").is_visible()

        # 6. Verify all 18 lessons can be loaded with status 200 / valid page title
        print("\nVerifying all 18 lessons load properly...")
        for i in range(1, 19):
            lesson_url = f"file://{WORKSPACE}/lessons/Marugoto_A2_Lesson_{i}.html"
            page.goto(lesson_url, wait_until='domcontentloaded')
            title = page.title()
            assert f"Bài {i}" in title, f"Lesson {i} title mismatch: {title}"
            assert page.locator(f"h1:has-text('BÀI {i}')").is_visible()
            print(f"✓ Lesson {i} OK: {title}")

        browser.close()

    print("\nALL 18 LESSONS AND GLOBAL DROPDOWN NAVIGATION VERIFIED SUCCESSFULLY!")

if __name__ == '__main__':
    run_verification()
