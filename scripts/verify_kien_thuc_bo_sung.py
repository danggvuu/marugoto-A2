#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for kien_thuc_bo_sung.html and navigation across pages.
"""

import os
from playwright.sync_api import sync_playwright

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ARTIFACT_DIR = "/Users/dangvu/.gemini/antigravity/brain/5974a0ad-3eac-4559-908a-5f38f533f9e9"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        )
        context = browser.new_context(viewport={'width': 1280, 'height': 800})
        page = context.new_page()

        # 1. Open kien_thuc_bo_sung.html
        url = f"file://{WORKSPACE}/kien_thuc_bo_sung.html"
        print(f"Loading {url}...")
        page.goto(url, wait_until='networkidle')

        # Check title
        assert "Kiến Thức Bổ Sung" in page.title()
        print("✓ Page title verified.")

        # Check header
        assert page.locator("h1:has-text('TỔNG HỢP TOÀN BỘ KIẾN THỨC BỔ SUNG')").is_visible()

        # Check all 9 topics exist
        for i in range(1, 10):
            topic_sel = f"#topic-{i}"
            assert page.locator(topic_sel).is_visible(), f"Topic {i} not found"
            print(f"✓ Topic {i} verified.")

        # Test furigana toggle
        ruby_rt = page.locator("ruby rt").first
        assert ruby_rt.is_visible()
        page.locator("button:has-text('Bật / Tắt Cách Đọc')").click()
        # Should now be hidden
        assert not ruby_rt.is_visible()
        page.locator("button:has-text('Bật / Tắt Cách Đọc')").click()
        assert ruby_rt.is_visible()
        print("✓ Furigana toggle verified.")

        # Test mini quiz
        quiz_opt_b = page.locator("#q1-opts button:has-text('B. で')")
        quiz_opt_b.click()
        assert page.locator("#q1-feedback").is_visible()
        assert "Chính xác" in page.locator("#q1-feedback").inner_text()
        print("✓ Mini quiz interactive test verified.")

        # Take screenshot of the top view
        ss_path = os.path.join(ARTIFACT_DIR, "kien_thuc_bo_sung_top.png")
        page.screenshot(path=ss_path)
        print(f"Saved screenshot: {ss_path}")

        # Scroll down and screenshot topic 6 & 7
        page.locator("#topic-7").scroll_into_view_if_needed()
        ss_topic7 = os.path.join(ARTIFACT_DIR, "kien_thuc_bo_sung_topic7.png")
        page.screenshot(path=ss_topic7)
        print(f"Saved screenshot: {ss_topic7}")

        # 2. Check navigation from index.html to kien_thuc_bo_sung.html
        index_url = f"file://{WORKSPACE}/index.html"
        page.goto(index_url, wait_until='networkidle')
        ktbs_btn = page.locator("a:has-text('Kiến Thức Bổ Sung')")
        assert ktbs_btn.is_visible()
        ktbs_btn.click()
        page.wait_for_load_state('networkidle')
        assert "kien_thuc_bo_sung.html" in page.url
        print("✓ Navigation link from index.html verified.")

        # 3. Check navigation from a lesson page
        lesson_url = f"file://{WORKSPACE}/lessons/Marugoto_A2_Lesson_1.html"
        page.goto(lesson_url, wait_until='networkidle')
        ktbs_lesson_btn = page.locator("a:has-text('Kiến Thức Bổ Sung')")
        assert ktbs_lesson_btn.is_visible()
        ktbs_lesson_btn.click()
        page.wait_for_load_state('networkidle')
        assert "kien_thuc_bo_sung.html" in page.url
        print("✓ Navigation link from Lesson 1 verified.")

        browser.close()
    print("\nALL VERIFICATIONS PASSED!")

if __name__ == '__main__':
    run()
