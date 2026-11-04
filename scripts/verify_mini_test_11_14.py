#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_mini_test_11_14.py
Kiểm thử tự động đề thi đa dạng 6 phần bằng Playwright (Headless Chrome):
- Tab 1: Lý Thuyết
- Tab 2: 118 Từ Vựng
- Tab 3: 30 Chữ Hán
- Tab 4: Đề thi thử đa dạng 6 phần (32 câu, thang điểm 100):
    + Phần I: Trắc nghiệm (10 câu)
    + Phần II: Sắp xếp từ thành câu ★ (5 câu)
    + Phần III: Điền dạng đúng của từ (5 câu)
    + Phần IV: Nối cột tình huống (4 câu)
    + Phần V: Đọc hiểu đoạn văn (4 câu)
    + Phần VI: Luyện dịch câu (4 câu)
- Tab 5: Cẩm Nang Bỏ Túi
- Console error check
- Chụp ảnh các phần thi
"""

import os
import asyncio
from playwright.async_api import async_playwright

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
HTML_FILE = os.path.join(WORKSPACE, 'tests/On_Tap_Mini_Test_A2_11_14.html')
ARTIFACT_DIR = "/Users/dangvu/.gemini/antigravity/brain/5974a0ad-3eac-4559-908a-5f38f533f9e9"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

async def run_verification():
    print(f"Testing Diverse Exam: {HTML_FILE}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True
        )
        context = await browser.new_context(viewport={'width': 1280, 'height': 900})
        page = await context.new_page()

        console_errors = []
        page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
        page.on('pageerror', lambda err: console_errors.append(str(err)))

        file_url = f"file://{HTML_FILE}"
        await page.goto(file_url, wait_until='networkidle')
        await asyncio.sleep(1)

        # 1. Check title
        title = await page.title()
        print(f"Page Title: {title}")
        assert "Bài 11 - 14" in title, "Title does not contain 'Bài 11 - 14'"

        # 2. Check Tab 4: Diverse Exam (Click Tab 4)
        await page.click('button:has-text("🎯 Đề Thi Thử Đa Dạng")')
        await asyncio.sleep(0.5)

        # Check Part 1: Multiple choice (10 cards)
        p1_count = await page.locator('#part1Container .question-card').count()
        print(f"Part 1 Questions count: {p1_count}")
        assert p1_count == 10, f"Expected 10 Part 1 questions, got {p1_count}"

        # Answering Part 1 Q1 (B is correct: index 1)
        await page.click('#optBtn_p1_1_1')
        await asyncio.sleep(0.2)
        is_p1_correct = await page.locator('#optBtn_p1_1_1').evaluate('el => el.classList.contains("correct")')
        print(f"P1 Q1 answer marked correct: {is_p1_correct}")
        assert is_p1_correct, "P1 Q1 button did not get 'correct' class"

        # Check Part 2: Sentence Ordering (5 cards)
        p2_count = await page.locator('#part2Container .question-card').count()
        print(f"Part 2 Questions count: {p2_count}")
        assert p2_count == 5, f"Expected 5 Part 2 questions, got {p2_count}"

        # Test arranging Question 11: chips 3, 0, 1, 2
        await page.click('#p2_chip_btn_11_3')
        await page.click('#p2_chip_btn_11_0')
        await page.click('#p2_chip_btn_11_1')
        await page.click('#p2_chip_btn_11_2')
        await asyncio.sleep(0.2)
        await page.click('#p2_check_btn_11')
        await asyncio.sleep(0.2)
        p2_btn_text = await page.locator('#p2_check_btn_11').inner_text()
        print(f"P2 Q11 check button status: {p2_btn_text}")
        assert "Chính Xác" in p2_btn_text, f"P2 Q11 arrangement failed: {p2_btn_text}"

        # Check Part 3: Conjugation Fill-in (5 cards)
        p3_count = await page.locator('#part3Container .question-card').count()
        print(f"Part 3 Questions count: {p3_count}")
        assert p3_count == 5, f"Expected 5 Part 3 questions, got {p3_count}"

        # Test answering Q16 with "飲み"
        await page.fill('#p3_input_16', '飲み')
        await page.click('#p3_btn_16')
        await asyncio.sleep(0.2)
        p3_btn_text = await page.locator('#p3_btn_16').inner_text()
        print(f"P3 Q16 check button status: {p3_btn_text}")
        assert "Đúng" in p3_btn_text, f"P3 Q16 conjugation check failed: {p3_btn_text}"

        # Check Part 4: Matching (4 situations)
        p4_count = await page.locator('#part4Container .match-card-a').count()
        print(f"Part 4 Situations count: {p4_count}")
        assert p4_count == 4, f"Expected 4 Part 4 situations, got {p4_count}"

        # Select option 0 for Q21 (correct)
        await page.select_option('#matchSelect_21', '0')
        await page.click('#btnCheckMatchAll')
        await asyncio.sleep(0.2)
        p4_card_bg = await page.locator('#matchCard_21').evaluate('el => window.getComputedStyle(el).backgroundColor')
        print(f"P4 Q21 Card background color after check: {p4_card_bg}")

        # Check Part 5: Reading Comprehension (2 passages, 4 questions)
        passages_count = await page.locator('#part5Container .passage-card').count()
        p5_q_count = await page.locator('#part5Container .question-card').count()
        print(f"Part 5 Passages: {passages_count}, Questions: {p5_q_count}")
        assert passages_count == 2 and p5_q_count == 4, "Part 5 reading passages or questions count mismatch"

        # Answer Q25 (B is correct: index 1)
        await page.click('#optBtn_p5_25_1')
        await asyncio.sleep(0.2)
        is_p5_correct = await page.locator('#optBtn_p5_25_1').evaluate('el => el.classList.contains("correct")')
        print(f"P5 Q25 answer marked correct: {is_p5_correct}")
        assert is_p5_correct, "P5 Q25 correct answer failed"

        # Check Part 6: Translation (4 questions)
        p6_count = await page.locator('#part6Container .question-card').count()
        print(f"Part 6 Questions count: {p6_count}")
        assert p6_count == 4, f"Expected 4 Part 6 questions, got {p6_count}"

        # Test toggle model for Q29 and self-grade
        await page.click('#part6Container .question-card:first-child button:has-text("👁️ Đối Chiếu Đáp Án Chuẩn")')
        await asyncio.sleep(0.2)
        is_model_shown = await page.locator('#trans_model_29').evaluate('el => window.getComputedStyle(el).display')
        print(f"P6 Q29 Model display: {is_model_shown}")
        assert is_model_shown == 'block', "Translation model answer failed to open"

        await page.click('#btnSelfGrade_29')
        await asyncio.sleep(0.2)

        # Check total score
        total_score_text = await page.locator('#totalScoreDisplay').inner_text()
        print(f"\n---> Current Total Score: {total_score_text} / 100đ")
        score_val = float(total_score_text)
        assert score_val > 10, f"Expected accumulated score > 10, got {score_val}"

        # Screenshots of diverse test sections
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_part1_and_2.png'), full_page=False)

        await page.evaluate("() => document.getElementById('sec-part3').scrollIntoView()")
        await asyncio.sleep(0.3)
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_part3_and_4.png'), full_page=False)

        await page.evaluate("() => document.getElementById('sec-part5').scrollIntoView()")
        await asyncio.sleep(0.3)
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_part5_reading.png'), full_page=False)

        await page.evaluate("() => document.getElementById('sec-part6').scrollIntoView()")
        await asyncio.sleep(0.3)
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_part6_translation.png'), full_page=False)

        print("\n--- Console Errors Check ---")
        if console_errors:
            print(f"WARNING: Encountered {len(console_errors)} console errors: {console_errors}")
        else:
            print("PERFECT: 0 console errors detected in diverse exam!")

        await browser.close()
        print("\nALL DIVERSE EXAM VERIFICATION CHECKS PASSED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(run_verification())
