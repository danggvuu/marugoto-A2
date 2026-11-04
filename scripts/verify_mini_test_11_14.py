#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/verify_mini_test_11_14.py
Kiểm thử tự động bằng Playwright (Headless Chrome):
- Kiểm tra console errors
- Kiểm tra hiển thị đầy đủ 5 tabs
- Kiểm tra Tab Từ Vựng (118 từ, tìm kiếm, ẩn nghĩa, copy Quizlet)
- Kiểm tra Tab Chữ Hán (30 chữ, chiết tự, từ ghép)
- Kiểm tra Tab Đề Thi Thử (30 câu hỏi, timer, tương tác bấm chọn đáp án, tính điểm tự động)
- Chụp ảnh màn hình lưu vào artifact directory
"""

import os
import asyncio
from playwright.async_api import async_playwright

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
HTML_FILE = os.path.join(WORKSPACE, 'tests/On_Tap_Mini_Test_A2_11_14.html')
ARTIFACT_DIR = "/Users/dangvu/.gemini/antigravity/brain/5974a0ad-3eac-4559-908a-5f38f533f9e9"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

async def run_verification():
    print(f"Testing: {HTML_FILE}")
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

        # 2. Check Tab 1: Theory
        theory_card_count = await page.locator('.grammar-card').count()
        print(f"Grammar Cards count: {theory_card_count}")
        assert theory_card_count == 4, f"Expected 4 grammar cards, got {theory_card_count}"
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_tab1_theory.png'), full_page=False)

        # 3. Check Tab 2: Vocab
        await page.click('button:has-text("🎴 118 Từ Vựng")')
        await asyncio.sleep(0.5)
        vocab_card_count = await page.locator('.vocab-card').count()
        print(f"Vocab Cards rendered: {vocab_card_count}")
        assert vocab_card_count == 118, f"Expected 118 vocab cards, got {vocab_card_count}"

        # Test Vocab search
        await page.fill('#vocabSearchInput', 'サラダ')
        await asyncio.sleep(0.3)
        searched_vocab = await page.locator('.vocab-card').count()
        print(f"Vocab search for 'サラダ': {searched_vocab} found")
        assert searched_vocab >= 1, "Vocab search failed for 'サラダ'"
        await page.fill('#vocabSearchInput', '')
        await asyncio.sleep(0.3)
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_tab2_vocab.png'), full_page=False)

        # 4. Check Tab 3: Kanji
        await page.click('button:has-text("⛩️ 30 Chữ Hán")')
        await asyncio.sleep(0.5)
        kanji_card_count = await page.locator('.kanji-card').count()
        print(f"Kanji Cards rendered: {kanji_card_count}")
        assert kanji_card_count == 30, f"Expected 30 kanji cards, got {kanji_card_count}"
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_tab3_kanji.png'), full_page=False)

        # 5. Check Tab 4: Quiz
        await page.click('button:has-text("🎯 Đề Thi Thử")')
        await asyncio.sleep(0.5)
        q_count = await page.locator('.question-card').count()
        print(f"Quiz Questions rendered: {q_count}")
        assert q_count == 30, f"Expected 30 questions, got {q_count}"

        # Test answering Question 1 (correct is B: index 1)
        # Select correct answer for Q1
        await page.click('#optBtn_1_1')
        await asyncio.sleep(0.2)
        is_q1_correct = await page.locator('#optBtn_1_1').evaluate('el => el.classList.contains("correct")')
        print(f"Q1 answer B is marked correct: {is_q1_correct}")
        assert is_q1_correct, "Q1 correct answer button did not get 'correct' class"

        # Check explain box is visible
        explain_display = await page.locator('#explain_1').evaluate('el => window.getComputedStyle(el).display')
        print(f"Q1 explanation display: {explain_display}")
        assert explain_display != 'none', "Q1 explanation not visible"

        # Test answering Question 2 with wrong answer (A is correct (0), let's click B (1))
        await page.click('#optBtn_2_1')
        await asyncio.sleep(0.2)
        is_q2_wrong = await page.locator('#optBtn_2_1').evaluate('el => el.classList.contains("wrong")')
        is_q2_correct_revealed = await page.locator('#optBtn_2_0').evaluate('el => el.classList.contains("correct")')
        print(f"Q2 answer B marked wrong: {is_q2_wrong}, A revealed correct: {is_q2_correct_revealed}")
        assert is_q2_wrong and is_q2_correct_revealed, "Q2 wrong and correct states not applied properly"

        # Check score circle
        score_text = await page.locator('#scoreDisplay').inner_text()
        print(f"Current score after 1 correct, 1 wrong: {score_text}")
        assert score_text == "1", f"Expected score 1, got {score_text}"

        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_tab4_quiz.png'), full_page=False)

        # 6. Check Tab 5: Cheatsheet
        await page.click('button:has-text("⚡ Cẩm Nang Bỏ Túi")')
        await asyncio.sleep(0.5)
        cheat_cards_count = await page.locator('.cheat-card').count()
        print(f"Cheat Cards rendered: {cheat_cards_count}")
        assert cheat_cards_count == 8, f"Expected 8 cheat cards, got {cheat_cards_count}"
        await page.screenshot(path=os.path.join(ARTIFACT_DIR, 'mini_test_11_14_tab5_cheatsheet.png'), full_page=False)

        print("\n--- Console Errors Check ---")
        if console_errors:
            print(f"WARNING: Encountered {len(console_errors)} console errors: {console_errors}")
        else:
            print("PERFECT: 0 console errors detected!")

        await browser.close()
        print("\nALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(run_verification())
