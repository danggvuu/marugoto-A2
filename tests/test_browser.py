"""Browser regressions for study flows. Run: python3 tests/test_browser.py

Requires Playwright and Chromium (or installed Google Chrome).
Optional: CHROME_PATH=/path/to/chrome, MARUGOTO_SCREENSHOTS_DIR=/path/to/output.
The server and isolated browser contexts never touch real user checkpoints.
"""
import functools
import http.server
import os
from pathlib import Path
import threading
import unittest

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
EXAM = "tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html"
VOCAB = "Tu_Vung_Marugoto_A1_16_A2_1_10.html"
TYPING = "tests/On_Tap_Mini_Test_A2_15_18.html#typing"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class StudyFlows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = http.server.ThreadingHTTPServer(
            ("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(ROOT))
        )
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}/"
        cls.pw = sync_playwright().start()
        path = os.environ.get("CHROME_PATH")
        if path:
            cls.browser = cls.pw.chromium.launch(executable_path=path)
        else:
            try:
                cls.browser = cls.pw.chromium.launch()
            except Exception:
                cls.browser = cls.pw.chromium.launch(channel="chrome")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.context = self.browser.new_context(viewport={"width": 390, "height": 844})
        # Network failures must not prevent local study flows.
        self.context.route("https://**/*", lambda route: route.abort())
        self.page = self.context.new_page()
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.clock.install()

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [], "Uncaught browser errors")

    def go(self, path):
        self.page.goto(self.base + path)
        self.page.clock.run_for(400)

    def reload(self):
        self.page.reload()
        self.page.clock.run_for(400)

    def test_vocab_paginate_search_clear_and_restore(self):
        self.go(VOCAB)
        self.assertEqual(self.page.locator("#vocabTableBody tr").count(), 50)
        self.assertIn("1217", self.page.locator("#vocabPaginationBar").inner_text())
        self.page.locator('[onclick="setVocabPage(2)"]').first.click()
        self.reload()
        self.assertEqual(self.page.evaluate("vocabCurrentPage"), 2)
        self.page.evaluate("setVocabPage(10)")
        self.page.locator("#searchInput").fill("a")
        self.page.clock.run_for(200)
        self.assertEqual(self.page.evaluate("vocabCurrentPage"), 1)
        self.assertIn("1–50", self.page.locator("#vocabPaginationBar").inner_text())
        self.page.locator("#searchInput").fill("zzzzzzzzzz")
        self.page.clock.run_for(200)
        self.page.locator("#vocabPaginationBar button").click()
        self.assertEqual(self.page.locator("#searchInput").input_value(), "")
        self.assertEqual(self.page.evaluate("selectedLessons.size"), 34)
        self.assertEqual(self.page.locator(".sub-kana-mobile").first.evaluate(
            "(el) => getComputedStyle(el).display"), "block")
        self.assertTrue(self.page.locator(".btn-stroke-model").first.evaluate(
            "(el) => { const r=el.getBoundingClientRect(); return r.left >= 0 && r.right <= innerWidth; }"))

    def test_vocab_test_restore_never_reveals_correct_answer(self):
        self.go(VOCAB)
        self.page.evaluate("quizSettings.mode='test';switchView('view-quiz')")
        self.page.locator("#quiz-opt-0").click()
        # Reload inside the auto-advance window.
        self.page.reload()
        self.page.clock.run_for(50)
        self.assertEqual(self.page.locator("#quizOptions .correct, #quizOptions .wrong").count(), 0)
        self.page.clock.run_for(500)
        self.assertEqual(self.page.evaluate("quizSession.currentIndex"), 1)

    def test_kanji_page_view_and_detail_restore(self):
        self.go("kanji_a2.html")
        self.page.evaluate("setKanjiViewMode('grid');setKanjiPage(2)")
        self.reload()
        self.assertEqual(self.page.evaluate("kanjiCurrentPage"), 2)
        self.assertEqual(self.page.evaluate("kanjiViewMode"), "grid")
        self.page.locator(".k-tile-btn-detail").first.click()
        index = self.page.locator(".kanji-card").first.get_attribute("data-index")
        self.assertEqual(index, "24")
        self.reload()
        self.assertEqual(self.page.evaluate("kanjiViewMode"), "cards")
        self.assertEqual(self.page.locator(".kanji-card").first.get_attribute("data-index"), "24")

    def test_legacy_skip_migrates_without_deleting_other_history(self):
        self.go(TYPING)
        self.page.evaluate("""() => {
            const items=getFilteredTypingPool();
            tpState.history[items[0].id]={status:'err',lastInput:'(Đã bỏ qua)',whyWrong:[]};
            tpState.history[items[1].id]={status:'ok',lastInput:items[1].hira,whyWrong:[]};
            tpState.drafts[items[0].id]='(Đã bỏ qua)';
            manualSaveTypingProgress();
        }""")
        self.reload()
        self.assertEqual(self.page.locator("#tpCardInput").input_value(), "")
        self.assertEqual(self.page.evaluate("Object.keys(tpState.history).length"), 2)
        self.assertTrue(self.page.evaluate("tpState.history[getFilteredTypingPool()[0].id].wasSkipped"))

    def test_resume_uses_timestamp_and_ignores_tab_only_state(self):
        self.go("index.html")
        self.page.evaluate("""() => {
            localStorage.setItem('marugoto_typing_studio_v2', JSON.stringify({
                version:2,savedAt:Date.now(),mode:'kanji',history:{one:{status:'ok'}}
            }));
            localStorage.setItem('marugoto_cp_v1::lessons/Marugoto_A2_Lesson_1.html::inputs',
                JSON.stringify({t:1,d:{answer:'abc'}}));
            localStorage.setItem('marugoto_cp_v1::the_ru.html::tab',
                JSON.stringify({t:Date.now()+1000,d:{idx:1}}));
        }""")
        self.reload()
        self.assertEqual(self.page.locator("#hubResumeBtn").get_attribute("href"), TYPING)
        self.assertIn("Kanji", self.page.locator("#hubResumeBtn").inner_text())

    def test_star_partial_complete_remove_and_reload(self):
        self.go(EXAM)
        self.page.evaluate("placeStarPart(69,0);placeStarPart(69,1);placeStarPart(69,2)")
        self.reload()
        self.assertEqual(self.page.evaluate("userAnswers[69].starOrder"), [0, 1, 2])
        self.assertFalse(self.page.evaluate("!!userAnswers[69].checked"))
        self.page.evaluate("placeStarPart(69,3)")
        self.assertTrue(self.page.evaluate("userAnswers[69].checked"))
        self.page.evaluate("removeStarSlot(69,1)")
        self.assertEqual(self.page.evaluate("userAnswers[69].starOrder"), [0, 2, 3])
        self.assertFalse(self.page.evaluate("!!userAnswers[69].checked"))

    def test_exam_mode_running_timer_and_pause_survive_reload(self):
        self.go(EXAM)
        self.page.locator("#btnToggleMode").click()
        self.page.clock.run_for(7000)
        self.page.evaluate("handleSelectOption(1,0)")
        before = self.page.evaluate("timerSeconds")
        self.reload()
        after = self.page.evaluate("timerSeconds")
        self.assertFalse(self.page.evaluate("isImmediateMode"))
        self.assertTrue(self.page.evaluate("isTimerRunning"))
        self.assertLessEqual(after, before)
        self.assertGreater(after, before - 3)
        self.page.locator("#btnTimerPause").click()
        paused = self.page.evaluate("timerSeconds")
        self.page.clock.run_for(9000)
        self.reload()
        self.assertEqual(self.page.evaluate("timerSeconds"), paused)
        self.assertFalse(self.page.evaluate("isTimerRunning"))

    def test_test_mode_no_answers_until_submit_and_review_is_readonly(self):
        self.go(EXAM)
        self.page.locator("#btnToggleMode").click()
        self.page.evaluate("handleSelectOption(1,0);toggleAllExplanations();filterPalette('wrong');toggleSingleVi(1)")
        self.assertEqual(self.page.locator("#explain_box_1").evaluate("(el)=>el.style.display"), "none")
        self.assertTrue(self.page.locator("#filterBtnWrong").is_disabled())
        self.assertNotIn("0", self.page.locator("#filterBtnWrong").inner_text())
        self.page.locator(".btn-bottom-submit").click()
        self.page.locator(".btn-modal-review").first.click()
        self.assertEqual(self.page.locator("#explain_box_1").evaluate("(el)=>el.style.display"), "block")
        original = self.page.evaluate("userAnswers[1].value")
        self.page.evaluate("handleSelectOption(1,3);submitExam(true)")
        self.assertEqual(self.page.evaluate("userAnswers[1].value"), original)
        self.assertEqual(self.page.evaluate("JSON.parse(localStorage.getItem(HISTORY_STORAGE_KEY)).length"), 1)
        self.reload()
        self.assertTrue(self.page.evaluate("isExamSubmitted"))
        self.assertTrue(self.page.locator('input[name="opt_1"]').first.is_disabled())

    def test_legacy_exam_draft_and_expired_timer(self):
        # Seed on another page: the exam intentionally flushes its draft on pagehide.
        self.go("index.html")
        self.page.evaluate("""() => {
            localStorage.setItem('marugoto_tonghop_11_18_draft_DEGOC',JSON.stringify({
                1:{value:0,checked:true,isCorrect:false},69:{starOrder:[0,1]}
            }));
        }""")
        self.go(EXAM)
        self.assertEqual(self.page.evaluate("userAnswers[69].starOrder"), [0, 1])
        self.assertTrue(self.page.evaluate("userAnswers[1].isCorrect"))
        answers = self.page.evaluate("userAnswers")
        self.go("index.html")
        self.page.evaluate("""(answers) => {
            localStorage.setItem('marugoto_tonghop_11_18_draft_DEGOC', JSON.stringify({
                version:2, userAnswers:answers, isImmediateMode:false, isExamSubmitted:false,
                isTimerRunning:true, timerSeconds:5, timerDeadline:Date.now()-1000
            }));
        }""", answers)
        self.go(EXAM)
        self.assertTrue(self.page.evaluate("isExamSubmitted"))
        self.assertEqual(self.page.evaluate("timerSeconds"), 0)

    def test_per_exam_state_is_independent(self):
        self.go(EXAM)
        self.page.evaluate("handleSelectOption(1,0);toggleExamMode();switchExam('M111')")
        self.assertEqual(self.page.evaluate("Object.keys(userAnswers).length"), 0)
        self.page.evaluate("handleSelectOption(2,1);switchExam('DEGOC')")
        self.assertEqual(self.page.evaluate("userAnswers[1].value"), 0)
        self.assertFalse(self.page.evaluate("isImmediateMode"))

    def test_all_exam_sets_have_consistent_ids_and_score_full_marks(self):
        self.go(EXAM)
        results = self.page.evaluate("""() => window.DE_THI_TONG_HOP_DATA.map(exam => {
            if (currentExamCode !== exam.code) switchExam(exam.code);
            const items = getExamItems();
            items.forEach(item => {
                if (item.type === 'star') {
                    item.correctOrder.forEach(index => placeStarPart(item.id, index));
                } else handleSelectOption(item.id, item.correct);
            });
            submitExam(true);
            const result = {code:exam.code, total:items.length,
                unique:new Set(items.map(item=>item.id)).size,
                score:Number(document.getElementById('modalScoreNumber').textContent)};
            closeScoreModal();
            return result;
        })""")
        for result in results:
            with self.subTest(exam=result["code"]):
                self.assertEqual(result["total"], 71)
                self.assertEqual(result["unique"], 71)
                self.assertEqual(result["score"], 100)

    def test_lesson_focus_view_and_anchor_navigation(self):
        self.go("lessons/Marugoto_A2_Lesson_15.html")
        self.page.wait_for_selector("#lessonOutline")
        self.page.locator("#lessonOutline summary").click()
        self.page.locator("#lessonOutline button[aria-pressed]").click()
        self.assertEqual(self.page.locator("section.content-section:not(.lesson-focus-hidden)").count(), 1)
        self.page.locator("#lessonSectionSelect").select_option("sec-vocab")
        self.assertFalse(self.page.locator("#sec-vocab").evaluate("(el)=>el.classList.contains('lesson-focus-hidden')"))
        self.page.evaluate("location.hash='sec-quiz'")
        self.page.clock.run_for(100)
        self.assertEqual(self.page.locator("#lessonSectionSelect").input_value(), "sec-quiz")
        self.page.locator("#lessonOutline button[aria-pressed]").click()
        self.assertEqual(self.page.locator(".lesson-focus-hidden").count(), 0)

    def test_storage_unavailable_does_not_break_exam(self):
        self.context.add_init_script("""Storage.prototype.setItem=function(){throw new Error('blocked')};
            Storage.prototype.getItem=function(){throw new Error('blocked')};""")
        self.go(EXAM)
        self.page.evaluate("handleSelectOption(1,0);placeStarPart(69,0);toggleExamMode()")
        self.assertEqual(self.page.evaluate("userAnswers[69].starOrder"), [0])

    def test_smoke_all_pages_and_responsive_views(self):
        files = sorted([*ROOT.glob("*.html"), *ROOT.glob("lessons/*.html"), *ROOT.glob("tests/*.html")])
        for file in files:
            with self.subTest(page=file.name):
                self.go(file.relative_to(ROOT).as_posix())
                self.assertEqual(self.errors, [])
        sample = ["index.html", VOCAB, "kanji_a2.html", EXAM, "lessons/Marugoto_A2_Lesson_15.html"]
        directory = os.environ.get("MARUGOTO_SCREENSHOTS_DIR")
        for width, height in [(360, 800), (390, 844), (768, 1024), (1440, 900)]:
            self.page.set_viewport_size({"width": width, "height": height})
            for path in sample:
                with self.subTest(width=width, page=path):
                    self.go(path)
                    self.assertLessEqual(self.page.evaluate("document.documentElement.scrollWidth"), width + 1)
                    if directory:
                        output = Path(directory)
                        output.mkdir(parents=True, exist_ok=True)
                        self.page.screenshot(path=str(output / f"{Path(path).stem}-{width}.png"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
