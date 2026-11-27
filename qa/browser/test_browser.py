"""Browser regressions for study flows. Run: python3 qa/browser/test_browser.py

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

ROOT = Path(__file__).resolve().parents[2]
EXAM = "tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html"
VOCAB = "Tu_Vung_Marugoto_A1_16_A2_1_10.html"
TYPING = "tests/On_Tap_Mini_Test_A2_15_18.html#typing"
MIDTERM = "tests/De_Thi_Midterm_A2_1.html#M101"
CRAM = "tests/On_Tap_Cap_Toc_Kanji_11_18_NPBS14.html"


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

    def test_a2_2_lesson_links_and_local_dependencies(self):
        vocab_counts = [20, 17, 21, 23]
        for entry in ["index.html", "lessons/Marugoto_A2_Lesson_1.html"]:
            self.go(entry)
            for lesson in range(1, 5):
                link = self.page.locator(f'#lessonsDropdownMenu a[href$="Marugoto_A2_2_Lesson_{lesson}.html"]')
                self.assertEqual(link.count(), 1)
                self.assertEqual(self.page.request.get(link.evaluate("(el)=>el.href")).status, 200)
        for lesson in range(1, 5):
            self.go(f"lessons/Marugoto_A2_2_Lesson_{lesson}.html")
            self.assertEqual(self.page.locator("#flashcardGrid .fc-item").count(), vocab_counts[lesson - 1])
            missing = self.page.evaluate("""async () => {
                const urls=[...document.querySelectorAll('script[src],link[rel="stylesheet"]')]
                    .map(el=>el.src || el.href).filter(url=>url.startsWith(location.origin));
                return (await Promise.all(urls.map(async url=>({url,status:(await fetch(url)).status}))))
                    .filter(result=>result.status!==200);
            }""")
            self.assertEqual(missing, [])

    def test_a2_2_flashcards_audio_typing_and_responsive_layout(self):
        vocab_counts = [20, 17, 21, 23]
        for lesson in range(1, 5):
            self.go(f"lessons/Marugoto_A2_2_Lesson_{lesson}.html")
            self.page.evaluate("() => {window.__spoken=[];window.speakText=text=>__spoken.push(text);}")
            cards = self.page.locator("#flashcardGrid .fc-item")
            expected = self.page.evaluate("VOCAB_DATA.map(item=>item.kana)")
            for i, kana in enumerate(expected):
                cards.nth(i).focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.evaluate("__spoken.at(-1)"), kana)
            self.assertEqual(self.page.locator(".fc-romaji").count(), len(expected))
            for width in [360, 390, 768, 1440]:
                with self.subTest(lesson=lesson, width=width):
                    self.page.set_viewport_size({"width": width, "height": 900})
                    self.assertEqual(self.page.evaluate("document.documentElement.scrollWidth"), width)
                    self.assertEqual(self.page.locator("#flashcardGrid").evaluate("(el)=>getComputedStyle(el).display"), "grid")
                    self.assertTrue(cards.evaluate_all("""els=>els.every(card=>{
                        const svg=card.querySelector('svg').getBoundingClientRect();
                        const copy=card.querySelector('.fc-content').getBoundingClientRect();
                        return svg.bottom <= copy.top+1 && card.scrollWidth <= card.clientWidth;
                    })"""))
            self.page.locator("#tpCardInput").fill(expected[0])
            self.page.locator("#tpCardCheckBtn").click()
            self.assertIn("Chính xác", self.page.locator("#sec-typing-practice").inner_text())
            self.page.locator("#tpBtnModeTable").click()
            self.assertTrue(self.page.locator("#tpTableModeView").is_visible())
            self.reload()
            self.assertTrue(self.page.locator("#tpTableModeView").is_visible())

    def test_a2_2_quiz_and_verb_lab_restore(self):
        for lesson in range(1, 5):
            self.go(f"lessons/Marugoto_A2_2_Lesson_{lesson}.html")
            verbs = self.page.evaluate("VERB_DATA")
            for i, verb in enumerate(verbs):
                self.page.locator(".btn-verb-chip").nth(i).click()
                for selector, key in [("#morphMasu", "masu"), ("#morphTe", "te"), ("#morphTeIki", "form1"), ("#morphTeKi", "form2"), ("#morphMashou", "form3")]:
                    self.assertEqual(self.page.locator(selector).inner_text(), verb[key])
            result = self.page.evaluate("""() => {
                const boxes=[...document.querySelectorAll('#quizContainer .quiz-card')];
                QUIZ_DATA.forEach((q,i)=>boxes[i].querySelectorAll('.quiz-opt')[q.correct].click());
                return {correct:boxes.filter(el=>el.querySelector('.correct')).length,
                    positions:[...new Set(QUIZ_DATA.map(q=>q.correct))].length};
            }""")
            self.assertEqual(result, {"correct": 20 if lesson <= 4 else 15, "positions": 4})
            self.reload()
            quiz_count = 20 if lesson <= 4 else 15
            self.assertEqual(self.page.locator("#quizContainer button.correct").count(), quiz_count)
            self.assertEqual(self.page.locator("#quizContainer button:disabled").count(), quiz_count * 4)

    def test_a2_2_kanji_filters_audio_and_restore(self):
        self.go("kanji_a2.html")
        self.page.locator('[onclick="switchTab(\\\'tab-vocab-11-18\\\')"]').click()
        official_counts = [8, 13, 18, 10, 11, 11, 9, 8, 8, 9, 11, 10, 11, 7, 9, 9, 10, 9]
        for lesson, count in enumerate(official_counts, 1):
            self.page.locator(f'.filter-121-btn[onclick="filter121Vocab(\'A2-2 L{lesson}\', this)"]').click()
            self.assertEqual(self.page.locator("#table121Body tr").count(), count)
            self.page.evaluate("() => {window.__spoken=[];window.speakText=text=>__spoken.push(text);}")
            expected = self.page.locator("#table121Body tr").first.locator("td").nth(3).inner_text()
            self.page.locator("#table121Body .btn-sound-small").first.click()
            self.assertEqual(self.page.evaluate("__spoken.at(-1)"), expected)
            self.reload()
            self.assertEqual(self.page.evaluate("current121Lesson"), f"A2-2 L{lesson}")
            self.assertEqual(self.page.locator("#table121Body tr").count(), count)

    def test_lesson_morph_respects_reduced_motion(self):
        self.page.set_viewport_size({"width": 1440, "height": 900})
        self.page.emulate_media(reduced_motion="reduce")
        self.go("lessons/Marugoto_A2_Lesson_1.html")
        self.page.evaluate("window.scrollTo(0, 300); window.dispatchEvent(new Event('scroll'))")
        self.page.clock.run_for(50)
        state = self.page.evaluate("""() => ({
            docked: document.body.classList.contains('is-scrolled-dock'),
            morphing: document.body.classList.contains('is-morphing-to-dock') ||
                document.body.classList.contains('is-morphing-to-top'),
            cssTransitionsReduced: [
                document.querySelector('.section-nav'),
                document.querySelector('.lesson-sidebar-rail .macos-sidebar-box')
            ].every(element => parseFloat(getComputedStyle(element).transitionDuration) <= 0.00001),
            activeMorphAnimations: document.getAnimations().filter(animation => {
                const element = animation.effect && animation.effect.target;
                return element && (element.classList.contains('lesson-morph-glider') ||
                    element.classList.contains('glider-layer-top') ||
                    element.classList.contains('glider-layer-dock')) && animation.playState === 'running';
            }).length
        })""")
        self.assertTrue(state["docked"])
        self.assertFalse(state["morphing"])
        self.assertTrue(state["cssTransitionsReduced"])
        self.assertEqual(state["activeMorphAnimations"], 0)

    def test_shortcuts_dialog_traps_and_restores_focus(self):
        self.go("lessons/Marugoto_A2_Lesson_1.html")
        self.page.evaluate("""() => {
            const trigger = document.createElement('button');
            trigger.id = 'testShortcutsTrigger';
            document.body.appendChild(trigger);
            trigger.focus();
            window.toggleShortcutsModal(true);
        }""")
        self.page.clock.run_for(20)
        modal = self.page.locator(".lesson-shortcuts-modal")
        self.assertEqual(self.page.evaluate("document.activeElement.id"), "btnCloseShortcuts")
        self.assertEqual(modal.get_attribute("aria-hidden"), "false")
        self.assertFalse(modal.evaluate("el => el.inert"))
        self.page.keyboard.press("Tab")
        self.assertEqual(self.page.evaluate("document.activeElement.id"), "btnCloseShortcuts")
        self.page.keyboard.press("Escape")
        self.assertEqual(modal.get_attribute("aria-hidden"), "true")
        self.assertTrue(modal.evaluate("el => el.inert"))
        self.assertEqual(self.page.evaluate("document.activeElement.id"), "testShortcutsTrigger")

    def test_reset_is_page_scoped_and_tutha_lab_uses_valid_sentences(self):
        self.go("lessons/Marugoto_A2_2_Lesson_1.html")
        with self.page.expect_navigation():
            self.page.evaluate("""() => {
            localStorage.setItem('marugoto_typing_studio_v2', JSON.stringify({ history: { otherPage: { status: 'ok' } } }));
            localStorage.setItem('marugoto_cp_v1::lessons/Marugoto_A2_2_Lesson_1.html::typing_practice',
                JSON.stringify({ t: 1, d: { currentIndex: 2 } }));
            MarugotoCheckpoint.silentClearPage();
            }""")
        self.page.clock.run_for(400)
        self.assertIsNotNone(self.page.evaluate("localStorage.getItem('marugoto_typing_studio_v2')"))
        self.assertIsNone(self.page.evaluate(
            "localStorage.getItem('marugoto_cp_v1::lessons/Marugoto_A2_2_Lesson_1.html::typing_practice')"))
        self.go("tu_tha_dong_tu.html")
        expected = {
            "te_iru": ["ドアが あいています。", "私が ドアを あけています。"],
            "te_aru": [None, "ドアが あけてあります。"],
            "ta": ["ドアが あきました。", "私が ドアを あけました。"],
        }
        for tense in ["te_iru", "te_aru", "ta"]:
            self.page.evaluate("(tense) => setLabTense(tense, null)", tense)
            for index, selector in enumerate(["#labJiCard .lab-sentence-jp", "#labTaCard .lab-sentence-jp"]):
                text = self.page.locator(selector).inner_text()
                if expected[tense][index]:
                    self.assertEqual(text, expected[tense][index])
        self.page.evaluate("selectQuizAnswer(1,1);gradeQuiz()")
        with self.page.expect_navigation():
            self.page.evaluate("() => {MarugotoCheckpoint.silentClearPage();}")
        self.page.clock.run_for(400)
        self.assertIsNone(self.page.evaluate("localStorage.getItem('marugoto_tu_tha_checkpoint_v1')"))
        self.assertEqual(self.page.locator(".quiz-opt-btn.selected").count(), 0)
        self.go(TYPING)
        self.page.evaluate("localStorage.setItem('marugoto_typing_studio_v2', '{}')")
        with self.page.expect_navigation():
            self.page.evaluate("() => {MarugotoCheckpoint.silentClearPage();}")
        self.page.clock.run_for(400)
        saved = self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_typing_studio_v2') || '{}')")
        self.assertEqual(saved.get("history", {}), {})

    def test_lesson10_and_grammar_survive_blocked_storage(self):
        self.context.add_init_script("""Storage.prototype.setItem=function(){throw new Error('blocked')};
            Storage.prototype.getItem=function(){throw new Error('blocked')};""")
        for page in ["lessons/Marugoto_A2_Lesson_10.html", "Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html"]:
            with self.subTest(page=page):
                self.go(page)
                self.assertEqual(self.errors, [])
                if "Lesson_10" in page:
                    self.assertGreater(self.page.locator("#flashcardGrid > *").count(), 0)
                    self.assertEqual(self.page.locator("#quizContainer > *").count(), 15)
                else:
                    self.assertGreater(self.page.locator("[id^='grammarCard_']").count(), 0)

    def test_kaiwa_session_timer_topic_and_single_script(self):
        self.go("Luyen_Kaiwa_5_Phut.html")
        self.assertEqual(self.page.locator("script[src*='kaiwa-studio.js']").count(), 1)
        self.page.evaluate("KaiwaStudio.switchMode('simulator');KaiwaStudio.toggleTimer()")
        self.page.clock.run_for(30000)
        remaining = self.page.locator("#kaiwaTimerClock").inner_text()
        self.assertEqual(remaining, "04:30")
        self.reload()
        self.assertEqual(self.page.locator("#kaiwaTimerClock").inner_text(), "04:30")
        self.page.evaluate("KaiwaStudio.switchTopic('topic2')")
        self.page.evaluate("location.hash='topic1'")
        self.page.clock.run_for(100)
        self.assertIn("Chủ Đề 1:", self.page.locator(".active-banner-title").inner_text())
        self.page.evaluate("KaiwaStudio.toggleViewOption('answers')")
        self.assertEqual(self.page.locator("#sampleAnswersWrap").evaluate("(el)=>getComputedStyle(el).display"), "none")
        self.reload()
        self.page.evaluate("KaiwaStudio.switchMode('simulator')")
        self.assertEqual(self.page.locator("#sampleAnswersWrap").evaluate("(el)=>getComputedStyle(el).display"), "none")
        self.page.evaluate("KaiwaStudio.toggleTimer()")
        paused = self.page.locator("#kaiwaTimerClock").inner_text()
        self.page.clock.run_for(10000)
        self.reload()
        self.assertEqual(self.page.locator("#kaiwaTimerClock").inner_text(), paused)
        self.page.evaluate("KaiwaStudio.toggleTimer()")
        # Jump without interval ticks: the next tick must catch up to real elapsed time.
        self.page.clock.fast_forward(600000)
        self.assertEqual(self.page.locator("#kaiwaTimerClock").inner_text(), "00:00")
        self.reload()
        self.assertEqual(self.page.locator("#kaiwaTimerClock").inner_text(), "00:00")
        self.page.evaluate("KaiwaStudio.resetTimer()")
        self.assertEqual(self.page.locator("#kaiwaTimerClock").inner_text(), "05:00")
        self.page.evaluate("KaiwaStudio.toggleTimer()")
        with self.page.expect_navigation():
            self.page.evaluate("() => {MarugotoCheckpoint.silentClearPage();}")
        self.page.clock.run_for(400)
        saved = self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_kaiwa_session_v1'))")
        self.assertIsNone(saved["deadline"])
        self.assertEqual(saved["timerRemaining"], 300)
        self.assertTrue(saved["showAnswers"])

    def test_tutha_all_lab_pairs_and_balanced_quiz(self):
        self.go("tu_tha_dong_tu.html")
        result = self.page.evaluate("""() => {
            const counts=[0,0,0,0];
            TU_THA_QUIZ_DATA.forEach(q=>counts[q.answer]++);
            const failures=[];
            TU_THA_PAIRS_DATA.forEach((pair,index)=>{
                const frame=TU_THA_LAB_FRAMES[index];
                openPairInLab(pair.id);
                for(const tense of ['te_iru','te_aru','ta']){
                    setLabTense(tense,null);
                    for(const role of ['ji','ta']){
                        if(tense==='te_aru' && (role==='ji'||!frame.aru))continue;
                        const form=tense==='ta'?pair[role].masu.replace('ます','ました')
                            :pair[role].te+(tense==='te_iru'?'います':'あります');
                        const expected=(tense==='te_aru'?frame.aru:frame[role])+' '+form+'。';
                        const selector=role==='ji'?'#labJiCard':'#labTaCard';
                        const actual=document.querySelector(selector+' .lab-sentence-jp').textContent;
                        if(actual!==expected)failures.push({id:pair.id,tense,role,actual,expected});
                    }
                }
            });
            return {counts,failures};
        }""")
        self.assertEqual(result, {"counts": [5, 5, 5, 5], "failures": []})
        self.reload()
        self.assertEqual(self.page.locator("#labPairSelect").input_value(), "50")
        self.assertIn("'ta'", self.page.locator(".lab-tense-pill.active").get_attribute("onclick"))

    def test_full_review_has_all_study_tabs_and_preserves_exam(self):
        self.go(EXAM)
        self.assertEqual(self.page.locator(".vkc-panels button").count(), 7)
        self.page.evaluate("handleSelectOption(1,0);toggleExamMode()")
        for view in ["theory", "vocab", "kanji", "typing", "cheatsheet"]:
            self.page.locator(f'[data-review-view="{view}"]').click()
            self.page.clock.run_for(400)
            self.assertTrue(self.page.locator("#review-" + view).is_visible())
            self.assertFalse(self.page.evaluate("isTimerRunning"))
            self.assertFalse(self.page.locator("#fullExamPanel").is_visible())
            for width in [360, 390, 768, 1440]:
                self.page.set_viewport_size({"width": width, "height": 900})
                self.page.clock.run_for(100)
                self.assertLessEqual(self.page.evaluate("document.documentElement.scrollWidth"), width + 1)
        self.assertEqual(self.page.locator("#review-theory .grammar-card").count(), 8)
        self.page.locator("#showFullExam").click()
        self.assertTrue(self.page.evaluate("isTimerRunning"))
        self.assertEqual(self.page.evaluate("Object.keys(userAnswers)"), ["1"])
        self.assertEqual(self.page.locator("#examSectionsContainer .q-item-card").count(), 71)
        self.page.locator("#showVocabCheck").click()
        self.assertFalse(self.page.evaluate("isTimerRunning"))
        self.assertTrue(self.page.locator("#vocabKanjiCheck").is_visible())

    def test_full_review_vocab_kanji_filters_audio_copy_and_restore(self):
        self.go(EXAM + "#review-vocab")
        self.assertIn("253", self.page.locator("#reviewVocabCount").inner_text())
        self.page.locator("#reviewVocabLesson").select_option("A2-11")
        self.assertTrue(self.page.locator("#reviewVocabBody tr").evaluate_all(
            "(rows)=>rows.every(row=>row.cells[0].textContent==='Bài 11')"))
        self.page.evaluate("() => {window.__spoken=[];window.speakText=text=>__spoken.push(text);}")
        expected = self.page.locator("#reviewVocabBody tr").first.locator("td").nth(1).inner_text()
        self.page.locator("#reviewVocabBody button").first.click()
        self.assertEqual(self.page.evaluate("__spoken.at(-1)"), expected)
        self.page.locator("#reviewHideMeaning").click()
        self.assertGreater(self.page.locator(".review-masked").count(), 0)
        self.page.evaluate("""() => {
            window.__copied='';
            Object.defineProperty(navigator, 'clipboard', {configurable:true,
                value:{writeText:async text=>{window.__copied=text;}}});
        }""")
        self.page.locator("#reviewCopyVocab").click()
        self.assertIn(expected + "\t", self.page.evaluate("__copied"))
        self.reload()
        self.assertEqual(self.page.locator("#reviewVocabLesson").input_value(), "A2-11")
        self.assertGreater(self.page.locator(".review-masked").count(), 0)
        self.page.locator("#reviewVocabSearch").fill("zzzzzz")
        self.assertIn("Không có từ", self.page.locator("#reviewVocabBody").inner_text())
        self.page.locator('[data-review-view="kanji"]').click()
        self.assertEqual(self.page.locator("#reviewKanjiGrid .review-kanji-card").count(), 64)
        self.page.locator("#reviewKanjiLesson").select_option("L11")
        self.assertEqual(self.page.locator("#reviewKanjiGrid .review-kanji-card").count(), 6)
        self.assertTrue(self.page.locator("#reviewKanjiGrid").evaluate("""el=>{
            const allowed=new Set(REVIEW_11_18_DATA.KANJI_DATA.map(item=>item.char));
            return [...el.querySelectorAll('[data-kana] span')].every(node=>
                [...node.textContent.replace(/々/g,'').matchAll(/\\p{Script=Han}/gu)].every(m=>allowed.has(m[0])));
        }"""))

    def test_full_review_typing_modes_scope_restore_and_isolated_reset(self):
        self.go(EXAM + "#review-typing")
        self.assertTrue(self.page.locator("#review-typing").is_visible())
        for mode in ["sentence", "kanji", "vocab"]:
            self.page.locator("#tpModeBtn_" + mode).click()
            self.page.locator("#typingFilterGroup button").filter(has_text="Bài 11 (").click()
            self.assertIn("A2-11" if mode != "kanji" else "Bài 11", self.page.locator("#tpCardBadge").inner_text())
        self.page.locator("#tpCardInput").fill("test draft")
        self.page.clock.run_for(500)
        self.reload()
        self.assertEqual(self.page.locator("#tpCardInput").input_value(), "test draft")
        self.assertIsNotNone(self.page.evaluate("localStorage.getItem('marugoto_review_11_18_typing_v1')"))
        self.assertIsNone(self.page.evaluate("localStorage.getItem('marugoto_typing_studio_v2')"))
        self.page.evaluate("""() => {
            localStorage.setItem('marugoto_typing_studio_v2', JSON.stringify({marker:'preserve'}));
        }""")
        with self.page.expect_navigation():
            self.page.evaluate("() => {MarugotoCheckpoint.silentClearPage();}")
        self.page.clock.run_for(400)
        self.assertEqual(self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_typing_studio_v2')).marker"), "preserve")

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

    def start_scoped_check(self, lesson="all", mode="mixed", direction="forward", count="10"):
        self.go(EXAM + "#vocab-kanji-check")
        if not self.page.locator("#vkcSettings").evaluate("(el) => el.open"):
            self.page.locator("#vkcSettings > summary").click()
        self.page.locator("#vkcLesson").select_option(lesson)
        self.page.locator("#vkcMode").select_option(mode)
        self.page.locator("#vkcDirection").select_option(direction)
        self.page.locator("#vkcCount").select_option(count)
        self.page.locator("#vocabKanjiCheck .vkc-start").click()

    def scoped_snapshot(self):
        return self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_vocab_kanji_check_11_18_v1'))")

    def test_scoped_check_limits_all_questions_and_distractors(self):
        for mode in ["vocab", "kanji", "mixed"]:
            for direction in ["forward", "reverse"]:
                with self.subTest(mode=mode, direction=direction):
                    self.start_scoped_check("A2-11", mode, direction, "all")
                    snapshot = self.scoped_snapshot()
                    self.assertGreater(len(snapshot["session"]["questions"]), 0)
                    valid = self.page.evaluate(r"""() => {
                        const d=VOCAB_KANJI_CHECK_DATA;
                        const s=JSON.parse(localStorage.getItem('marugoto_vocab_kanji_check_11_18_v1')).session;
                        const allowed=new Set(d.allowedKanji);
                        return s.questions.every(q=>{
                            const item=[...d.vocab,...d.kanji].find(x=>x.id===q.id);
                            return item.lesson==='A2-11' && new Set(q.options).size===4 &&
                                (s.settings.mode==='mixed'||q.id.startsWith(s.settings.mode+':')) &&
                                [item.id.startsWith('kanji:')?item.jp:item.kana,...q.options]
                                    .every(text=>[...text.replace(/々/g,'').matchAll(/\p{Script=Han}/gu)].every(m=>allowed.has(m[0])));
                        });
                    }""")
                    self.assertTrue(valid)

    def test_scoped_check_reload_completion_retry_and_audio(self):
        self.start_scoped_check()
        self.assertFalse(self.page.locator(".vkc-next").is_visible())
        self.page.locator(".vkc-option").first.click()
        snapshot = self.scoped_snapshot()
        self.reload()
        self.assertEqual(self.scoped_snapshot()["session"], snapshot["session"])
        self.assertEqual(self.page.locator(".vkc-option:disabled").count(), 4)
        self.page.evaluate("() => {window.__spoken=[];window.speakText=text=>__spoken.push(text);}")
        self.page.locator(".vkc-speak").click()
        self.assertEqual(self.page.evaluate("__spoken[0]"), self.page.evaluate("""() => {
            const id=JSON.parse(localStorage.getItem('marugoto_vocab_kanji_check_11_18_v1')).session.questions[0].id;
            return [...VOCAB_KANJI_CHECK_DATA.vocab,...VOCAB_KANJI_CHECK_DATA.kanji].find(x=>x.id===id).kana;
        }"""))
        self.page.locator(".vkc-next").click()
        for _ in range(9):
            wrong = self.page.evaluate("""() => {
                const s=JSON.parse(localStorage.getItem('marugoto_vocab_kanji_check_11_18_v1')).session;
                const q=s.questions[s.index];
                const item=[...VOCAB_KANJI_CHECK_DATA.vocab,...VOCAB_KANJI_CHECK_DATA.kanji].find(x=>x.id===q.id);
                return q.options.findIndex(x=>x!==item.kana);
            }""")
            self.page.locator(f'.vkc-option[data-index="{wrong}"]').click()
            self.page.locator(".vkc-next").click()
        self.assertTrue(self.page.locator(".vkc-finished").is_visible())
        snapshot = self.scoped_snapshot()
        self.assertEqual(snapshot["session"]["index"], 10)
        wrong_ids = {q["id"] for q in snapshot["session"]["questions"]}
        self.reload()
        self.assertTrue(self.page.locator(".vkc-finished").is_visible())
        self.page.locator("#vkcRetryWrong").click()
        retried = self.scoped_snapshot()["session"]
        self.assertGreaterEqual(len(retried["questions"]), 9)
        self.assertTrue({q["id"] for q in retried["questions"]}.issubset(wrong_ids))

    def test_scoped_check_isolated_from_exam_and_pauses_timer(self):
        self.go(EXAM)
        self.page.evaluate("handleSelectOption(1,0);toggleExamMode()")
        self.page.locator("#showVocabCheck").click()
        self.assertFalse(self.page.evaluate("isTimerRunning"))
        remaining = self.page.evaluate("timerSeconds")
        self.page.clock.run_for(5000)
        self.assertEqual(self.page.evaluate("timerSeconds"), remaining)
        self.page.locator(".vkc-start").click()
        self.page.locator(".vkc-option").first.click()
        self.page.locator("#showFullExam").click()
        self.assertTrue(self.page.evaluate("isTimerRunning"))
        self.assertEqual(self.page.evaluate("Object.keys(userAnswers)"), ["1"])
        self.page.locator("#showVocabCheck").click()
        self.assertEqual(self.page.locator(".vkc-option:disabled").count(), 4)

    def test_scoped_check_rejects_out_of_scope_snapshot(self):
        self.start_scoped_check()
        self.page.evaluate("""() => {
            const key='marugoto_vocab_kanji_check_11_18_v1';
            const value=JSON.parse(localStorage.getItem(key));
            value.session.questions[0].options[0]='外国語';
            localStorage.setItem(key,JSON.stringify(value));
        }""")
        self.reload()
        self.assertEqual(self.page.locator(".vkc-option").count(), 0)
        self.assertIn("Bắt đầu", self.page.locator("#vkcCard").inner_text())

    def test_scoped_check_workspace_layout_and_feedback(self):
        for width in [360, 390, 768, 1440]:
            with self.subTest(width=width):
                self.page.set_viewport_size({"width": width, "height": 900})
                self.start_scoped_check("all", "kanji", "reverse", "all")
                self.assertFalse(self.page.locator("#vkcSettings").evaluate("(el) => el.open"))
                self.assertFalse(self.page.locator(".vkc-feedback").is_visible())
                self.assertFalse(self.page.locator(".vkc-next").is_visible())
                self.assertEqual(self.page.locator(".vkc-progress").get_attribute("value"), "0")
                self.assertRegex(self.page.locator(".vkc-question-meta > span").last.inner_text(), r"^Bài 1[1-8]$")
                self.assertNotIn("A2-", self.page.locator(".vkc-question-meta").inner_text())
                self.assertEqual(self.page.locator("#vkcCard h3").evaluate(
                    "(el) => el === document.activeElement"), True)
                self.assertTrue(self.page.evaluate("""() => {
                    const root=document.querySelector('#vocabKanjiCheck');
                    return document.documentElement.scrollWidth === innerWidth &&
                        [...root.querySelectorAll('.vkc-option, .vkc-card')].every(el => {
                            const r=el.getBoundingClientRect();
                            return r.left >= 0 && r.right <= innerWidth && el.scrollWidth <= el.clientWidth;
                        });
                }"""))
                # Pick the correct answer, then verify explicit text, not just color.
                answer = self.page.evaluate("""() => {
                    const s=JSON.parse(localStorage.getItem('marugoto_vocab_kanji_check_11_18_v1')).session;
                    const q=s.questions[0];
                    const item=VOCAB_KANJI_CHECK_DATA.kanji.find(x=>x.id===q.id);
                    return q.options.indexOf(item.jp);
                }""")
                self.page.locator(f'.vkc-option[data-index="{answer}"]').click()
                self.assertIn("Chính xác", self.page.locator(".vkc-feedback").inner_text())
                self.assertEqual(self.page.locator(".vkc-option.is-correct").count(), 1)
                self.assertEqual(self.page.locator(".vkc-progress").get_attribute("value"), "1")
                self.assertEqual(self.page.locator(".vkc-option.is-correct").evaluate(
                    "(el) => getComputedStyle(el).opacity"), "1")
                self.assertTrue(self.page.locator(".vkc-next").evaluate("(el) => el === document.activeElement"))
                self.page.locator(".vkc-next").click()
                self.assertFalse(self.page.locator(".vkc-feedback").is_visible())
                self.assertEqual(self.page.locator(".vkc-progress").get_attribute("value"), "1")
                # Editing filters must not mutate the current session.
                before = self.scoped_snapshot()["session"]
                self.page.locator("#vkcSettings > summary").click()
                self.page.locator("#vkcMode").select_option("vocab")
                self.assertEqual(self.page.locator("#vkcDirection option").first.inner_text(), "Nghĩa Việt → Kana")
                self.assertEqual(self.scoped_snapshot()["session"], before)
                if not self.page.locator(".vkc-about").evaluate("(el) => el.open"):
                    self.page.locator(".vkc-about > summary").click()
                self.assertIn("64 chữ", self.page.locator(".vkc-about").inner_text())
                self.page.locator(".vkc-about > summary").click()
                self.assertFalse(self.page.locator(".vkc-about > div").is_visible())
                self.page.evaluate("localStorage.removeItem('marugoto_vocab_kanji_check_11_18_v1')")

    def test_scoped_check_perfect_result_and_new_round_controls(self):
        self.start_scoped_check("A2-11", "kanji", "forward", "all")
        total = len(self.scoped_snapshot()["session"]["questions"])
        for _ in range(total):
            answer = self.page.evaluate("""() => {
                const s=JSON.parse(localStorage.getItem('marugoto_vocab_kanji_check_11_18_v1')).session;
                const q=s.questions[s.index];
                return q.options.indexOf(VOCAB_KANJI_CHECK_DATA.kanji.find(x=>x.id===q.id).kana);
            }""")
            self.page.locator(f'.vkc-option[data-index="{answer}"]').click()
            self.page.locator(".vkc-next").click()
        self.assertIn("100%", self.page.locator(".vkc-result-ring").inner_text())
        self.assertTrue(self.page.locator("#vkcRetryWrong").is_disabled())
        self.reload()
        self.assertIn("100%", self.page.locator(".vkc-result-ring").inner_text())
        self.page.locator("#vkcRestart").click()
        self.assertTrue(self.page.locator("#vkcSettings").evaluate("(el) => el.open"))
        self.assertEqual(self.page.locator("#vkcLesson").evaluate("(el) => el === document.activeElement"), True)
        self.page.locator("#vkcCount").select_option("10")
        self.page.locator(".vkc-start").click()
        self.assertEqual(self.scoped_snapshot()["session"]["index"], 0)
        self.assertEqual(self.page.locator(".vkc-score").inner_text(), "✓ 0 đúng")

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

    def test_vocab_audio_uses_displayed_kana_not_ambiguous_kanji(self):
        for path, selector in [
            ("tests/On_Tap_Mini_Test_A2_11_14.html", "#vocabContainer .sound-btn"),
            ("tests/On_Tap_Mini_Test_A2_15_18.html", "#vocabGridContainer .audio-btn"),
        ]:
            with self.subTest(page=path):
                self.go(path)
                self.page.locator('button[onclick="switchMainTab(\\\'tab-vocab\\\')"]').click()
                self.page.evaluate("""() => {
                    window.__spoken = [];
                    window.speakText = text => window.__spoken.push(String(text));
                    window.speakJapanese = window.speakText;
                }""")
                button = self.page.locator(selector).first
                expected = self.page.evaluate("""() => {
                    const item = typeof rawVocab !== 'undefined' ? rawVocab[0] : VOCAB_DATA[0];
                    return item.kana || item.jp || item.kanji;
                }""")
                button.click()
                spoken = self.page.evaluate("window.__spoken.at(-1)")
                self.assertTrue(spoken, "audio button did not dispatch text")
                self.assertEqual(spoken, expected)

    def test_audio_mapping_after_shuffle_pagination_filter_and_modal(self):
        self.go(VOCAB)
        self.page.evaluate("""() => {
            fetchKanjiSvg = async () => null;
            window.__spoken=[];
            window.speakJapanese=text=>__spoken.push(String(text));
            window.speakText=window.speakJapanese;
            switchView('view-flashcard');
            const original=Math.random;
            Math.random=()=>0;
            shuffleCards();
            Math.random=original;
            switchView('view-table');
        }""")
        for setup in ["setVocabPage(1)", "setVocabPage(2)", "selectLevelScope('A2_2')"]:
            self.page.evaluate(setup)
            row = self.page.locator("#vocabTableBody tr").filter(has=self.page.locator(".btn-stroke-model")).first
            visible_word = row.locator(".kanji-word").inner_text()
            expected_kana = row.locator(".col-kana .kana-word").text_content()
            row.locator(".btn-speak-inline").click()
            self.assertEqual(self.page.evaluate("__spoken.at(-1)"), expected_kana)
            row.locator(".btn-stroke-model").click()
            self.assertEqual(self.page.locator("#motionWordKanji").inner_text(), visible_word)
            self.page.locator(".btn-motion-speak").click()
            self.assertEqual(self.page.evaluate("__spoken.at(-1)"), expected_kana)
            self.page.evaluate("closeStrokeModel()")

    def test_kanji_audio_uses_readings_after_filter_and_page_change(self):
        self.go("kanji_a2.html")
        self.page.evaluate("""() => {
            window.__spoken=[];
            window.speakJapanese=text=>__spoken.push(String(text));
            window.speakText=window.speakJapanese;
            setKanjiViewMode('cards');setKanjiPage(2);
        }""")
        for setup in ["", "selectPreset('L11_18')"]:
            if setup:
                self.page.evaluate(setup)
            result = self.page.evaluate("""() => {
                const cards=[...document.querySelectorAll('.kanji-card')];
                return cards.map(card=>{
                    const item=filteredKanji[Number(card.dataset.index)];
                    const buttons=card.querySelectorAll('.example-line button');
                    const spoken=[...buttons].map(b=>{b.click();return __spoken.at(-1)});
                    return {expected:item.examples.map(e=>e.reading),spoken};
                });
            }""")
            self.assertGreater(len(result), 0)
            for card in result:
                self.assertEqual(card["spoken"], card["expected"])
        self.page.evaluate("speakKanjiReadings('は-れる、は-らす');")
        self.assertEqual(self.page.evaluate("__spoken.at(-1)"), "はれる。はらす")

    def test_each_lesson_vocab_audio_dispatches_kana(self):
        for n in range(1, 19):
            with self.subTest(lesson=n):
                self.go(f"lessons/Marugoto_A2_Lesson_{n}.html")
                result = self.page.evaluate("""() => {
                    window.__spoken=[];
                    window.speakText=text=>__spoken.push(String(text));
                    window.speakJapanese=window.speakText;
                    const buttons=[...document.querySelectorAll('#sec-vocab button[onclick*="speakText"]')]
                        .filter(b=>!b.getAttribute('onclick').includes('exJp'));
                    const cards=[...document.querySelectorAll('#flashcardGrid .fc-item')];
                    // Rich cards have two buttons per item: word and example.
                    if (cards.length) cards.forEach(c=>c.click());
                    else buttons.filter((_,i)=>i%2===0).forEach(b=>b.click());
                    return {spoken:__spoken,expected:VOCAB_DATA.map(v=>v.kana||v.jp)};
                }""")
                self.assertGreater(len(result["spoken"]), 0)
                self.assertEqual(result["spoken"], result["expected"])

    def test_audio_transport_ruby_normalization_and_cancelled_fallback(self):
        self.go(VOCAB)
        self.page.evaluate("""() => {
            window.__audio=[];
            window.__utterances=[];
            window.Audio=class {
                constructor(){__audio.push(this)}
                play(){return Promise.resolve()}
                pause(){this.paused=true}
                load(){}
                removeAttribute(){}
            };
            speechSynthesis.speak=u=>__utterances.push(u.text);
            speechSynthesis.cancel=()=>{};
            AudioEngine.speak('<ruby>生<rt>なま</rt></ruby>たまご');
        }""")
        self.assertEqual(self.page.evaluate("new URL(__audio[0].src).searchParams.get('q')"), "なまたまご")
        self.page.evaluate("""() => {
            window.__oldError=__audio[0].onerror;
            AudioEngine.speak('なまえ');
            __oldError();
        }""")
        self.page.clock.run_for(100)
        self.assertEqual(self.page.evaluate("__utterances.length"), 0)
        self.assertTrue(self.page.evaluate("__audio[0].paused"))
        self.page.clock.run_for(2700)
        self.assertEqual(self.page.evaluate("__utterances"), ["なまえ"])

    def test_motion_requests_cannot_replace_newer_character(self):
        self.go(VOCAB)
        result = self.page.evaluate("""async () => {
            const pending={};
            fetchKanjiSvg=char=>new Promise(resolve=>pending[char]=resolve);
            const one=currentFiltered[0],two=currentFiltered[1];
            const a=loadMiniMotionChar('自',one);
            const b=loadMiniMotionChar('名',two);
            pending['名'](null);await b;
            pending['自'](null);await a;
            return {heading:document.getElementById('miniMotionChar').textContent,
                drawing:document.getElementById('miniSvgContainer').textContent};
        }""")
        self.assertEqual(result["heading"], "名")
        self.assertEqual(result["drawing"], "名")

    def test_typing_studio_voice_tracks_current_item_and_mode(self):
        self.go(TYPING)
        self.page.evaluate("""() => {
            window.__spoken=[];
            AudioEngine.speak=text=>__spoken.push(String(text));
        }""")
        for mode in ["sentence", "kanji", "vocab"]:
            for index in [0, 3]:
                with self.subTest(mode=mode, index=index):
                    result = self.page.evaluate(r"""({mode,index}) => {
                        switchTypingMode(mode);
                        jumpToTypingItem(index);
                        const item=getFilteredTypingPool()[index];
                        document.getElementById('tpCardSpeakBtn').click();
                        return {spoken:__spoken.at(-1),expected:mode==='sentence'
                            ? item.hira.replace(/[（(]\\s*[／/][^）)]*[）)]/g,'').trim()
                            : (item.kana||item.jp||item.kanji)};
                    }""", {"mode": mode, "index": index})
                    self.assertEqual(result["spoken"], result["expected"])

    def test_exam_speaker_reaches_actual_transport_after_switching_sets(self):
        self.go(EXAM)
        self.page.evaluate("""() => {
            window.__audio=[];
            window.Audio=class {
                constructor(){__audio.push(this)}
                play(){return Promise.resolve()}
                pause(){}
                load(){}
                removeAttribute(){}
            };
        }""")
        for code in ["DEGOC", "M111", "M115"]:
            self.page.evaluate("(code)=>{if(currentExamCode!==code)switchExam(code)}", code)
            result = self.page.evaluate("""() => {
                const q=getExamItems()[0];
                const button=document.querySelector(`#q_card_${q.id} .btn-speak`);
                button.click();
                return {spoken:new URL(__audio.at(-1).src).searchParams.get('q'),
                    expected:AudioEngine.clean(q.prompt)};
            }""")
            self.assertTrue(result["spoken"])
            self.assertEqual(result["spoken"], result["expected"])

    def test_3d_vocab_audio_matches_current_card(self):
        self.go("lessons/Marugoto_A2_Lesson_12.html")
        self.page.evaluate("""() => {window.__spoken=[];window.speakText=text=>__spoken.push(String(text));openVocab3D(0)}""")
        self.page.clock.run_for(100)
        for change in ["", "next3DVocab()", "next3DVocab()", "prev3DVocab()"]:
            if change:
                self.page.evaluate(change)
            expected = self.page.locator("#v3dKana").text_content()
            self.page.locator("#v3dSpeakBtn").click()
            self.assertEqual(self.page.evaluate("__spoken.at(-1)"), expected)
        self.page.evaluate("closeVocab3DModal()")

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
        files = sorted([*ROOT.glob('*.html'), *ROOT.glob('lessons/*.html'),
                        *ROOT.glob('tests/*.html'), *ROOT.glob('docs/Ke_Hoach_10_Ngay/**/*.html')])
        local_failures = []
        self.page.on('response', lambda response: local_failures.append(
            f'{response.status} {response.url}')
            if response.url.startswith(self.base) and response.status >= 400 else None)
        for width in (360, 1440):
            self.page.set_viewport_size({'width': width, 'height': 900})
            for file in files:
                with self.subTest(width=width, page=file.relative_to(ROOT).as_posix()):
                    self.go(file.relative_to(ROOT).as_posix())
                    self.assertEqual(self.errors, [])
                    self.assertEqual(local_failures, [], 'Failed local page or asset requests')
                    self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), width + 1)
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

    def test_reviewed_lesson_quizzes_grade_and_restore_correct_choices(self):
        for lesson in range(1, 19):
            with self.subTest(lesson=lesson):
                self.go(f"lessons/Marugoto_A2_Lesson_{lesson}.html")
                result = self.page.evaluate("""() => {
                    const items = typeof QUIZ_DATA !== 'undefined' ? QUIZ_DATA : QUIZ_QUESTIONS;
                    const boxes = [...document.querySelectorAll('#quizContainer .quiz-card')];
                    if (boxes.length !== items.length) throw new Error('Missing rendered quiz cards');
                    items.forEach((q, i) => {
                        const buttons = boxes[i].querySelectorAll('.quiz-opt,.quiz-opt-btn');
                        buttons[q.correct].click();
                    });
                    return {questions:items.length,
                        correct:boxes.filter(b=>b.querySelector('button.correct')).length,
                        disabled:boxes.every(b=>[...b.querySelectorAll('.quiz-opt,.quiz-opt-btn')].every(x=>x.disabled))};
                }""")
                self.assertEqual(result["questions"], 15)
                self.assertEqual(result["correct"], 15)
                self.assertTrue(result["disabled"])
                self.reload()
                self.assertEqual(self.page.locator("#quizContainer button.correct").count(), 15)

    def test_old_quiz_clicks_do_not_answer_revised_lesson(self):
        self.go("index.html")
        self.page.evaluate("""() => {
            localStorage.setItem('marugoto_cp_v1::lessons/Marugoto_A2_Lesson_3.html::clicks',
                JSON.stringify({t:1,d:['oc::checkQuizAnswer(this,0,0)']}));
            localStorage.setItem('marugoto_cp_v1::lessons/Marugoto_A2_Lesson_3.html::typing_practice',
                JSON.stringify({t:1,d:{currentIndex:2,correctCount:2}}));
        }""")
        self.go("lessons/Marugoto_A2_Lesson_3.html")
        self.assertEqual(self.page.locator("#quizContainer button:disabled").count(), 0)
        self.assertTrue(self.page.evaluate("!!localStorage.getItem('marugoto_cp_v1::lessons/Marugoto_A2_Lesson_3.html::typing_practice')"))

    def test_corrected_exam_questions_require_new_attempt(self):
        self.go(EXAM + "#M111")
        question_id = self.page.evaluate("getExamItems().find(q=>q.contentRevision>=2).id")
        self.page.evaluate("(id)=>handleSelectOption(id,0)", question_id)
        self.reload()
        self.assertTrue(self.page.evaluate("(id)=>!!userAnswers[id]", question_id))
        self.go("index.html")
        self.page.evaluate("""(id) => {
            const key='marugoto_tonghop_11_18_draft_M111';
            const saved=JSON.parse(localStorage.getItem(key));
            delete saved.userAnswers[id].contentRevision;
            localStorage.setItem(key,JSON.stringify(saved));
        }""", question_id)
        self.go(EXAM + "#M111")
        self.assertFalse(self.page.evaluate("(id)=>!!userAnswers[id]", question_id))

    def test_balanced_exam_answers_and_revised_star_restore(self):
        self.go(EXAM + '#M111')
        distributions = self.page.evaluate("""() => DE_THI_TONG_HOP_DATA.filter(e=>e.code!=='DEGOC').map(e=>{
            const counts=[0,0,0,0];
            getExamItems(e).forEach(q=>counts[q.correct]++);
            return counts;
        })""")
        for counts in distributions:
            self.assertEqual(sorted(counts), [17, 18, 18, 18])
        star = self.page.evaluate("getExamItems().find(q=>q.type==='star')")
        self.page.evaluate("q=>q.correctOrder.forEach(i=>placeStarPart(q.id,i))", star)
        self.reload()
        saved = self.page.evaluate("id=>userAnswers[id]", star['id'])
        self.assertTrue(saved['isCorrect'])
        self.assertEqual(saved['starOrder'], star['correctOrder'])
        self.assertEqual(saved['contentRevision'], 3)
        self.go('index.html')
        self.page.evaluate("""() => {
            const key='marugoto_tonghop_11_18_draft_M111';
            const saved=JSON.parse(localStorage.getItem(key));
            Object.values(saved.userAnswers).forEach(a=>{a.contentRevision=2;});
            saved.isExamSubmitted=true;
            localStorage.setItem(key,JSON.stringify(saved));
        }""")
        self.go(EXAM + '#M111')
        self.assertEqual(self.page.evaluate('Object.keys(userAnswers).length'), 0)
        self.assertFalse(self.page.evaluate('isExamSubmitted'))

    def test_cram_typing_tab_preserves_existing_studio_history(self):
        self.go(TYPING)
        saved = self.page.evaluate("""() => {
            switchTypingMode('kanji');
            const item=getFilteredTypingPool()[0];
            tpState.history[item.id]={status:'ok',lastInput:item.hira,whyWrong:[]};
            tpState.drafts[item.id]=item.hira;
            manualSaveTypingProgress();
            return JSON.parse(localStorage.getItem('marugoto_typing_studio_v2'));
        }""")
        self.assertTrue(saved["history"])
        self.go(CRAM)
        self.page.locator(".tab-nav [onclick=\"switchMainTab('tab-typing')\"]").click()
        restored = self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_typing_studio_v2'))")
        self.assertEqual(restored["history"], saved["history"])
        self.assertEqual(restored["drafts"], saved["drafts"])
        self.reload()
        self.assertEqual(self.page.evaluate("tpState.history"), saved["history"])
        self.go(TYPING)
        self.assertEqual(self.page.evaluate("tpState.history"), saved["history"])

    def test_cram_hidden_meanings_can_be_revealed_and_restore_on_reload(self):
        self.go(CRAM)
        meanings = self.page.locator('#vocabContainer .vc-vi')
        self.assertGreater(meanings.count(), 1)
        self.page.locator('#btnHideMeaning').click()
        self.assertEqual(meanings.first.evaluate('el=>getComputedStyle(el).filter'), 'blur(5px)')
        self.assertEqual(meanings.nth(1).evaluate('el=>getComputedStyle(el).filter'), 'blur(5px)')
        meanings.first.click()
        self.assertEqual(meanings.first.evaluate('el=>el.style.filter'), 'none')
        self.assertEqual(meanings.nth(1).evaluate('el=>el.style.filter'), 'blur(5px)')
        self.reload()
        self.assertTrue(self.page.evaluate('isMeaningHidden'))
        self.assertEqual(meanings.first.evaluate('el=>getComputedStyle(el).filter'), 'blur(5px)')
        self.page.locator('#btnHideMeaning').click()
        self.assertEqual(meanings.first.evaluate('el=>getComputedStyle(el).filter'), 'none')

    def test_cram_filtered_checkpoint_restores_card_tab_and_answers(self):
        self.go(CRAM)
        self.page.locator('[onclick="filterVocabByLesson(11, this)"]').click()
        before = self.page.evaluate("""() => {
            nextCramCard();nextCramCard();nextCramCard();
            const question=NPBS_CHALLENGES[0];
            answerNpbsChallenge(question.id,question.correct);
            switchMainTab('tab-cram');
            return {lesson:currentLessonFilter,index:cramIndex,answers:npbsUserAnswers,tab:currentTab};
        }""")
        self.reload()
        after = self.page.evaluate("""() => ({
            lesson:currentLessonFilter,index:cramIndex,answers:npbsUserAnswers,tab:currentTab
        })""")
        self.assertEqual(after, before)
        self.assertTrue(self.page.locator('[onclick="filterVocabByLesson(11, this)"]').evaluate(
            "el=>el.classList.contains('active')"))
        self.assertTrue(self.page.locator('#tab-cram').is_visible())

    def test_checkpoint_repeated_restore_preserves_scroll_globals(self):
        self.go('the_ru.html')
        original = self.page.evaluate('String(Element.prototype.scrollIntoView)')
        self.page.locator('[onclick="gradeAll()"]').click()
        self.page.locator("[onclick=\"switchTab('tab-theory')\"]").click()
        self.reload()
        self.page.clock.run_for(1200)
        self.assertTrue(self.page.locator('#tab-theory').is_visible())
        self.assertEqual(self.page.evaluate('String(Element.prototype.scrollIntoView)'), original)

    def test_midterm_regrades_edited_translations_on_submission(self):
        self.go(MIDTERM)
        reference = self.page.evaluate("""() => getAllItems(EXAMS_DATA.find(e=>e.code===currentExamCode))
            .find(q=>q.id===31).reference""")
        for initial, edited, expected in [('。', reference, True), (reference, '。', False)]:
            with self.subTest(correct=expected):
                self.page.evaluate("closeResultModal();clearDraft('M101');loadExam('M101')")
                self.page.locator('#trans_input_31').fill(initial)
                self.page.evaluate('checkTranslationSingle(31)')
                self.page.locator('#trans_input_31').fill(edited)
                self.page.evaluate('submitExam(true)')
                self.assertEqual(self.page.evaluate('userAnswers[31].isCorrect'), expected)
                self.assertEqual(self.page.locator('#modalScoreBig').inner_text(),
                                 '2.5 / 100' if expected else '0 / 100')

    def test_midterm_submission_and_pause_survive_reload(self):
        self.go(MIDTERM)
        self.page.evaluate('handleSelectOption(1,2);submitExam(true)')
        self.reload()
        self.assertTrue(self.page.evaluate('isExamSubmitted'))
        self.assertFalse(self.page.evaluate('isTimerRunning'))
        self.page.evaluate('handleSelectOption(1,0)')
        self.assertEqual(self.page.evaluate('userAnswers[1].value'), 2)
        self.page.evaluate('resetCurrentExam()')
        self.page.clock.run_for(2000)
        self.page.evaluate('toggleTimer()')
        paused = self.page.evaluate('timerSeconds')
        self.page.clock.run_for(5000)
        self.reload()
        self.assertFalse(self.page.evaluate('isExamSubmitted'))
        self.assertFalse(self.page.evaluate('isTimerRunning'))
        self.assertEqual(self.page.evaluate('timerSeconds'), paused)

    def test_midterm_timeout_stays_submitted_after_reload(self):
        self.go(MIDTERM)
        self.page.evaluate('stopTimer();timerSeconds=1;startTimer()')
        self.page.clock.run_for(2500)
        self.assertTrue(self.page.evaluate('isExamSubmitted'))
        self.reload()
        self.assertTrue(self.page.evaluate('isExamSubmitted'))
        self.assertFalse(self.page.evaluate('isTimerRunning'))
        self.assertEqual(self.page.evaluate('timerSeconds'), 0)

    def test_midterm_checkpoint_clear_removes_draft_not_other_page_history(self):
        self.go(MIDTERM)
        self.page.evaluate("""() => {
            handleSelectOption(1,2);
            localStorage.setItem('marugoto_typing_studio_v2',JSON.stringify({marker:'keep'}));
            localStorage.setItem('marugoto_midterm_history_v1',JSON.stringify([{marker:'keep'}]));
        }""")
        with self.page.expect_navigation():
            self.page.evaluate('MarugotoCheckpoint.silentClearPage()')
        self.page.clock.run_for(400)
        self.assertEqual(self.page.evaluate('Object.keys(userAnswers)'), [])
        self.assertEqual(self.page.evaluate("""() => {
            const draft=JSON.parse(localStorage.getItem('marugoto_midterm_draft_M101')||'{}');
            return draft.userAnswers||{};
        }"""), {})
        self.assertEqual(self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_typing_studio_v2')).marker"), 'keep')
        self.assertEqual(self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_midterm_history_v1'))[0].marker"), 'keep')

    def test_midterm_legacy_draft_still_restores_answers(self):
        self.go('index.html')
        self.page.evaluate("""() => localStorage.setItem('marugoto_midterm_draft_M101',JSON.stringify({
            userAnswers:{1:{value:2}},timerSeconds:1234,updatedAt:Date.now()
        }))""")
        self.go(MIDTERM)
        self.assertEqual(self.page.evaluate('userAnswers[1].value'), 2)
        self.assertFalse(self.page.evaluate('isExamSubmitted'))
        self.page.evaluate('handleSelectOption(1,0)')
        self.assertEqual(self.page.evaluate('userAnswers[1].value'), 0)

    def test_mini_test_timers_start_on_demand_and_pause_away_from_quiz(self):
        for path, study_tab, quiz_tab in [
            ('tests/On_Tap_Mini_Test_A2_11_14.html', 'tab-theory', 'tab-quiz'),
            ('tests/On_Tap_Mini_Test_A2_2_1_4.html', 'tab-theory', 'tab-quiz'),
        ]:
            with self.subTest(page=path):
                self.go(path)
                self.assertFalse(self.page.evaluate('timerStarted'))
                self.assertFalse(self.page.evaluate('isTimerRunning'))
                self.page.clock.run_for(10000)
                self.assertEqual(self.page.evaluate('totalSeconds'), 2700)

                self.page.evaluate(f"switch{'MainTab' if '11_14' in path else 'Tab'}('{quiz_tab}')")
                self.page.evaluate('toggleTimer()')
                self.assertTrue(self.page.evaluate('timerStarted'))
                self.page.clock.run_for(3000)
                remaining = self.page.evaluate('totalSeconds')
                self.assertEqual(remaining, 2697)

                self.page.evaluate(f"switch{'MainTab' if '11_14' in path else 'Tab'}('{study_tab}')")
                self.assertFalse(self.page.evaluate('isTimerRunning'))
                self.page.clock.run_for(5000)
                self.assertEqual(self.page.evaluate('totalSeconds'), remaining)

                self.page.evaluate(f"switch{'MainTab' if '11_14' in path else 'Tab'}('{quiz_tab}')")
                self.assertFalse(self.page.evaluate('isTimerRunning'))
                self.page.evaluate('toggleTimer()')
                self.page.clock.run_for(2000)
                self.assertEqual(self.page.evaluate('totalSeconds'), remaining - 2)

    def test_a2_2_review_canonical_content_supplements_and_restore(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html')
        self.assertEqual(self.page.evaluate('rawKanji.length'), 62)
        self.assertEqual(self.page.evaluate('rawVocab.length'), 81)
        self.page.locator('button[onclick*="tab-theory"]').click()
        self.assertEqual(self.page.locator('.review-grammar-section').count(), 15)
        self.assertEqual(self.page.locator('#theory-b4 .contraction-table tbody tr').count(), 10)
        self.assertTrue(self.page.get_by_text('Câu luyện dịch • Đáp án tham khảo').count() >= 15)

        self.page.evaluate("switchTab('tab-vocab');window.__spoken=[];window.speakText=text=>__spoken.push(text)")
        self.page.locator('#vocabContainer .sound-btn').first.click()
        self.assertTrue(self.page.evaluate("__spoken.at(-1).length > 0"))
        self.page.evaluate("switchTab('tab-kanji')")
        self.page.locator('#kanjiFilterGroup button[onclick*="SUPPLEMENT"]').click()
        self.assertEqual(self.page.locator('#kanjiContainer .kanji-card').count(), 13)
        self.assertIn('紹介', self.page.locator('#kanjiContainer').inner_text())
        self.assertIn('歌手', self.page.locator('#kanjiContainer').inner_text())
        self.page.evaluate("""() => {
            window.__copied = '';
            Object.defineProperty(navigator, 'clipboard', {
                configurable: true,
                value: {writeText(text) { window.__copied = text; return Promise.resolve(); }}
            });
            copyKanjiQuizletTabFormat();
        }""")
        self.assertEqual(len(self.page.evaluate('__copied.trim().split("\\n")')), 13)

        for tab in ['tab-theory', 'tab-vocab', 'tab-kanji', 'tab-quiz', 'tab-kana', 'tab-cheat']:
            self.page.evaluate(f"switchTab('{tab}')")
            self.assertEqual(self.page.locator('.tab-panel.active').get_attribute('id'), tab)

        self.page.set_viewport_size({'width': 360, 'height': 900})
        self.page.evaluate("switchTab('tab-theory')")
        layout = self.page.evaluate("""() => ({
            pageWidth: document.documentElement.scrollWidth,
            viewportWidth: innerWidth,
            tableWidth: document.querySelector('#theory-b4 .contraction-table-wrap').clientWidth,
            tableScrollWidth: document.querySelector('#theory-b4 .contraction-table-wrap').scrollWidth
        })""")
        self.assertEqual(layout['pageWidth'], layout['viewportWidth'])
        self.assertLessEqual(layout['tableWidth'], layout['viewportWidth'])
        self.assertGreater(layout['tableScrollWidth'], layout['tableWidth'])
        self.page.set_viewport_size({'width': 1440, 'height': 900})
        self.assertEqual(self.page.evaluate('document.documentElement.scrollWidth'), 1440)

        self.page.evaluate("switchTab('tab-quiz')")
        self.page.locator('#optBtn_p1_1_0').click()
        self.page.locator('#p3_input_16').fill('買った')
        self.page.locator('#trans_input_29').fill('あそこで先生と話している人です。')
        self.page.evaluate("setPart6Score(29, 2.5);switchTab('tab-quiz');toggleTimer()")
        self.page.clock.run_for(2500)
        self.page.evaluate("switchTab('tab-theory')")
        remaining = self.page.evaluate('totalSeconds')
        self.reload()
        self.assertEqual(self.page.evaluate('currentTab'), 'tab-theory')
        self.assertEqual(self.page.evaluate('currentKanjiFilter'), 'SUPPLEMENT')
        self.assertEqual(self.page.evaluate('p1Answers[1]'), 0)
        self.assertEqual(self.page.locator('#p3_input_16').input_value(), '買った')
        self.assertEqual(self.page.locator('#trans_input_29').input_value(), 'あそこで先生と話している人です。')
        self.assertEqual(self.page.evaluate('p6SelfScores[29]'), 2.5)
        self.assertFalse(self.page.evaluate('isTimerRunning'))
        self.assertEqual(self.page.evaluate('totalSeconds'), remaining)
        self.page.evaluate("switchTab('tab-quiz');toggleTimer()")
        self.assertTrue(self.page.evaluate('isTimerRunning'))

    def test_exercise_controls_and_panels_do_not_move_on_hover_or_press(self):
        for path, selector in [
            ('tests/On_Tap_Mini_Test_A2_2_1_4.html#tab-kana', '.kana-review-input'),
            ('tests/On_Tap_Mini_Test_A2_2_1_4.html', '#optBtn_p1_1_0'),
            ('lessons/Marugoto_A2_2_Lesson_1.html', '.quiz-opt'),
            (TYPING, '#tpCardInput'),
        ]:
            with self.subTest(page=path):
                self.go(path)
                if selector == '#optBtn_p1_1_0':
                    self.page.evaluate("switchTab('tab-quiz')")
                control = self.page.locator(selector).first
                control.scroll_into_view_if_needed()
                control.hover()
                self.page.mouse.down()
                try:
                    moving = control.evaluate("""el => {
                        const moving = [];
                        for (let node = el; node && node !== document.body; node = node.parentElement) {
                            const style = getComputedStyle(node);
                            if (style.transform !== 'none' || style.animationName !== 'none') {
                                moving.push({className: node.className, transform: style.transform, animation: style.animationName});
                            }
                        }
                        return moving;
                    }""")
                    self.assertEqual(moving, [])
                finally:
                    self.page.mouse.up()
                if path == TYPING:
                    control.fill('wrong answer')
                    self.page.locator('#tpCardCheckBtn').click()
                    self.assertIn('wrong', control.get_attribute('class'))
                elif 'Lesson_1' in path:
                    self.assertEqual(control.evaluate("el=>el.classList.contains('aui-shake')||el.classList.contains('aui-check-pop')"), False)
                control.evaluate("el=>el.classList.add('aui-shake','aui-check-pop')")
                self.assertEqual(control.evaluate('el=>getComputedStyle(el).animationName'), 'none')
                self.assertEqual(control.evaluate('el=>getComputedStyle(el).transform'), 'none')

    def test_a2_2_practice_regions_stay_still_during_real_interactions(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html#tab-kana')

        def assert_stationary(control, label):
            control.scroll_into_view_if_needed()
            self.page.mouse.move(0, 0)
            self.page.clock.run_for(300)
            before = control.evaluate("""element => {
                const rect = element.getBoundingClientRect();
                return {x: rect.x + scrollX, y: rect.y + scrollY,
                    width: rect.width, height: rect.height};
            }""")
            control.hover()
            self.page.mouse.down()
            try:
                self.page.clock.run_for(80)
                after = control.evaluate("""element => {
                    const rect = element.getBoundingClientRect();
                    return {x: rect.x + scrollX, y: rect.y + scrollY,
                        width: rect.width, height: rect.height};
                }""")
                self.assertEqual(before, after, f'{label} moved under the pointer')
                moving_ancestors = control.evaluate("""element => {
                    const moved = [];
                    for (let node = element; node; node = node.parentElement) {
                        const style = getComputedStyle(node);
                        if (style.transform !== 'none' || style.translate !== 'none' ||
                            style.scale !== 'none' || style.rotate !== 'none' ||
                            style.animationName !== 'none' || style.transitionProperty !== 'none') {
                            moved.push({tag: node.tagName, id: node.id, className: node.className,
                                transform: style.transform, translate: style.translate, scale: style.scale,
                                rotate: style.rotate, animation: style.animationName,
                                transition: style.transitionProperty});
                        }
                        if (node.id === 'tab-kana' || node.id === 'tab-quiz' ||
                            node.classList.contains('tab-nav-wrapper') || node === document.body) break;
                    }
                    return moved;
                }""")
                self.assertEqual(moving_ancestors, [], f'{label} or an exercise ancestor animates')
            finally:
                self.page.mouse.up()

        self.page.set_viewport_size({'width': 390, 'height': 844})
        assert_stationary(self.page.locator('[data-kana-lesson="2"]'), 'Kana lesson filter')
        self.page.locator('[data-kana-lesson="2"]').click()
        assert_stationary(self.page.locator('.kana-review-input'), 'Kana answer input')
        assert_stationary(self.page.locator('[data-kana-action="check"]'), 'Kana check button')
        self.page.locator('.kana-review-input').fill('したがきをほぞんします')
        self.page.locator('[data-kana-action="check"]').click()
        self.assertIn('Chưa đúng', self.page.locator('.kana-review-status').inner_text())
        assert_stationary(self.page.locator('[data-kana-action="reveal"]'), 'Kana reveal button')
        self.assertTrue(self.page.locator('.kana-review-answer').is_visible())
        assert_stationary(self.page.locator('#kanaNextBtn'), 'Kana next button')
        self.assertEqual(self.page.locator('#kanaQuestionPosition').inner_text(), 'Câu 2 / 20')
        assert_stationary(self.page.locator('#kanaPreviousBtn'), 'Kana previous button')
        self.assertEqual(self.page.locator('#kanaQuestionPosition').inner_text(), 'Câu 1 / 20')
        self.assertTrue(self.page.locator('.kana-review-answer').is_visible())
        self.assertEqual(self.page.locator('[data-kana-action="check"]').inner_text(), 'Câu tiếp')
        assert_stationary(self.page.locator('[data-kana-action="check"]'), 'Kana primary next action')
        self.assertEqual(self.page.locator('#kanaQuestionPosition').inner_text(), 'Câu 2 / 20')
        assert_stationary(self.page.locator('button[onclick="resetKanaLesson()"]'), 'Kana reset button')
        self.assertEqual(self.page.locator('#kanaQuestionPosition').inner_text(), 'Câu 1 / 20')
        self.assertEqual(self.page.locator('.kana-review-question').count(), 1)
        self.assertEqual(self.page.locator('.kana-review-input').input_value(), '')
        self.assertEqual(self.page.locator('#toast').evaluate('el=>getComputedStyle(el).animationName'), 'none')

        assert_stationary(self.page.locator('.tab-btn[onclick*="tab-quiz"]'), 'Exam tab')
        self.page.locator('.tab-btn[onclick*="tab-quiz"]').click()
        self.assertEqual(self.page.locator('#tab-quiz').evaluate('el=>getComputedStyle(el).animationName'), 'none')
        self.page.set_viewport_size({'width': 1440, 'height': 900})

        controls = [
            ('#optBtn_p1_1_0', 'Multiple-choice option'),
            ('#part2Container button[onclick^="handlePart2ChipClick"]', 'Sentence-order chip'),
            ('#part2Container button[onclick^="checkPart2Explicit"]', 'Sentence-order check button'),
            ('#part2Container button[onclick^="resetPart2Question"]', 'Sentence-order reset button'),
            ('#p3_btn_16', 'Conjugation check button'),
            ('#part4Container .opt-btn', 'Matching option'),
            ('#part5Container .opt-btn', 'Reading-comprehension option'),
            ('#p6_score_0_29', 'Translation score control'),
            ('#timerToggleBtn', 'Timer control'),
            'button[onclick="submitAndGradeExam()"]',
        ]
        for control in controls:
            selector, label = control if isinstance(control, tuple) else (control, 'Exam grading control')
            locator = self.page.locator(selector)
            self.assertGreater(locator.count(), 0, f'Missing {label}')
            assert_stationary(locator.first, label)

        self.page.locator('#optBtn_p1_1_0').click()
        self.assertTrue(self.page.locator('#optBtn_p1_1_0.correct, #optBtn_p1_1_0.wrong').count())
        self.assertEqual(self.page.locator('#p1_exp_1').evaluate('el=>getComputedStyle(el).animationName'), 'none')
        self.page.locator('#part2Container button[onclick^="handlePart2ChipClick"]').first.click()
        self.assertTrue(self.page.locator('#part2Container .word-chip.selected').count())
        self.page.locator('button[onclick="submitAndGradeExam()"]').click()
        self.assertEqual(self.page.locator('#scoreModal').evaluate('el=>getComputedStyle(el).animationName'), 'none')
        self.assertEqual(self.page.evaluate('getComputedStyle(document.documentElement).scrollBehavior'), 'auto')

        for width in [360, 768, 1440]:
            self.page.set_viewport_size({'width': width, 'height': 900})
            self.assertEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)
            for selector in ['#tab-kana', '#tab-quiz']:
                audit = self.page.locator(selector).evaluate("""root => {
                    const elements = [root, ...root.querySelectorAll('*')];
                    return elements.filter(element => {
                        const style = getComputedStyle(element);
                        return style.animationName !== 'none' || style.transitionProperty !== 'none' ||
                            style.transform !== 'none' || style.translate !== 'none' ||
                            style.scale !== 'none' || style.rotate !== 'none' || style.willChange !== 'auto';
                    }).slice(0, 10).map(element => ({id:element.id, className:element.className,
                        animation:getComputedStyle(element).animationName,
                        transition:getComputedStyle(element).transitionProperty,
                        transform:getComputedStyle(element).transform}));
                }""")
                self.assertEqual(audit, [], f'Motion styles remain inside {selector} at {width}px')

    def assert_kana_question(self, item, position):
        card = self.page.locator('.kana-review-question')
        self.assertEqual(card.count(), 1, 'Only the current kana question belongs in the DOM')
        self.assertTrue(card.is_visible())
        self.assertEqual(card.get_attribute('data-kana-id'), item['id'])
        self.assertEqual(card.locator('#kanaQuestionPosition.q-num').inner_text(), f'Câu {position} / 20')
        self.assertEqual(card.locator('.kana-review-prompt').inner_text(), item['vi'])
        self.assertEqual(self.page.locator('.kana-review-input').count(), 1)
        self.assertEqual(card.locator('.kana-review-input').evaluate('el=>el.tagName'), 'TEXTAREA')
        self.assertEqual(card.locator('#kanaPreviousBtn').is_disabled(), position == 1)
        self.assertEqual(card.locator('#kanaNextBtn').is_disabled(), position == 20)
        return card

    def test_a2_2_kana_practice_redesign_layout_progress_and_checkpoint(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html#tab-kana')
        first_item = self.page.evaluate('kanaReviewLessons[0].items[0]')
        self.assert_kana_question(first_item, 1)
        self.assertEqual(self.page.locator('.kana-review-entry').count(), 0)
        self.assertEqual(self.page.locator('.tab-btn[onclick*="tab-kana"]').count(), 1)
        self.assertEqual(self.page.locator('button[onclick*="gradeKanaLesson"]').count(), 0)
        self.assertEqual(self.page.get_by_role('button', name='Chấm 20 câu', exact=True).count(), 0)
        self.assertEqual(self.page.evaluate('typeof gradeKanaLesson'), 'undefined')
        for selector in [
            'link[href$="kana-review-practice.css?v=5"]',
            'script[src$="mini-test-a2-2-1-4.js?v=6"]',
            'script[src$="mini_a2_2_1_4_data.js?v=4"]',
        ]:
            self.assertEqual(self.page.locator(selector).count(), 1)
        self.assertEqual(self.page.locator('.kana-review-title').inner_text(), 'Luyện viết câu tiếng Nhật')
        self.assertEqual(self.page.locator('#kanaLessonFilters button').count(), 4)
        self.assertEqual(self.page.locator('#kanaLessonGrammar span').count(), 3)
        self.assertIn('N1 という N2', self.page.locator('#kanaLessonGrammar').inner_text())
        progress = self.page.locator('.kana-review-progress-track')
        self.assertEqual(progress.get_attribute('role'), 'progressbar')
        self.assertEqual(progress.get_attribute('aria-valuemin'), '0')
        self.assertEqual(progress.get_attribute('aria-valuemax'), '20')
        self.assertEqual(progress.get_attribute('aria-valuenow'), '0')
        self.assertEqual(progress.get_attribute('aria-valuetext'), '0 / 20 câu đúng')
        self.assertEqual(self.page.locator('.kana-review-heading').evaluate('el=>getComputedStyle(el).backgroundImage'), 'none')
        self.assertEqual(self.page.locator('.kana-review-heading').evaluate('el=>getComputedStyle(el).padding'), '0px')

        for width in [360, 390, 768, 879, 880, 1024, 1440]:
            self.page.set_viewport_size({'width': width, 'height': 900})
            self.assert_kana_question(first_item, 1)
            self.assertEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)
            self.assertEqual(self.page.locator('#kanaLessonFilters').evaluate('el=>getComputedStyle(el).display'), 'grid')
            for selector in ['#kanaLessonFilters', '.kana-review-summary', '.kana-review-question',
                             '.kana-review-input', '#kanaPreviousBtn', '#kanaNextBtn',
                             '[data-kana-action="check"]', '[data-kana-action="reveal"]']:
                self.assertTrue(self.page.locator(selector).evaluate(
                    'el=>{const r=el.getBoundingClientRect();return r.left>=0&&r.right<=innerWidth+1&&el.scrollWidth<=el.clientWidth+1}'),
                    f'{selector} exceeds viewport at {width}px')

            filter_first = self.page.locator('#kanaLessonFilters button').nth(0).bounding_box()
            filter_second = self.page.locator('#kanaLessonFilters button').nth(1).bounding_box()
            if width <= 640:
                filter_third = self.page.locator('#kanaLessonFilters button').nth(2).bounding_box()
                self.assertEqual(filter_first['y'], filter_second['y'])
                self.assertGreater(filter_third['y'], filter_first['y'])
            else:
                self.assertEqual(filter_first['y'], filter_second['y'])

        self.page.set_viewport_size({'width': 390, 'height': 844})
        answer = first_item['jp']
        self.page.locator('.kana-review-input').fill(answer)
        self.page.locator('[data-kana-action="check"]').click()
        self.assertIn('is-correct', self.assert_kana_question(first_item, 1).get_attribute('class'))
        self.assertEqual(progress.get_attribute('aria-valuenow'), '1')
        self.assertEqual(progress.get_attribute('aria-valuetext'), '1 / 20 câu đúng')
        self.assertEqual(self.page.locator('#kanaReviewProgressBar').evaluate('el=>el.style.width'), '5%')
        self.assertTrue(self.page.locator('.kana-review-question').evaluate(
            'el=>getComputedStyle(el).borderTopColor === "rgb(4, 120, 87)"'))
        self.assertEqual(self.page.locator('.kana-review-heading').evaluate('el=>getComputedStyle(el).textAlign'), 'left')
        self.assertEqual(self.page.locator('[data-kana-action="check"]').inner_text(), 'Câu tiếp')
        self.page.locator('[data-kana-action="reveal"]').click()
        self.assertTrue(self.page.locator('.kana-review-answer').is_visible())
        self.assertEqual(self.page.locator('.kana-review-answer-jp').inner_text(), answer)
        self.assertEqual(self.page.locator('.kana-review-answer-grammar').inner_text(), first_item['grammar'])

        directory = os.environ.get('MARUGOTO_SCREENSHOTS_DIR')
        if directory:
            output = Path(directory)
            output.mkdir(parents=True, exist_ok=True)
            for width, height, name in [(1440, 900, 'desktop'), (390, 844, 'mobile')]:
                self.page.set_viewport_size({'width': width, 'height': height})
                self.assert_kana_question(first_item, 1)
                self.assertTrue(self.page.locator('.kana-review-answer').is_visible())
                self.page.evaluate('window.scrollTo(0, 0)')
                self.page.screenshot(path=str(output / f'kana-single-{name}.png'), full_page=True)

        filter_button = self.page.locator('[data-kana-lesson="2"]')
        focus_style = filter_button.evaluate("""el => {
            el.focus({focusVisible: true});
            const style = getComputedStyle(el);
            return {width:el.getBoundingClientRect().height, outline:style.outlineStyle,
                outlineWidth:style.outlineWidth, pressed:el.getAttribute('aria-pressed')};
        }""")
        self.assertGreaterEqual(focus_style['width'], 44)
        self.assertEqual(focus_style['outline'], 'solid')
        self.assertEqual(focus_style['outlineWidth'], '2px')

        filter_button.click()
        self.assert_kana_question(self.page.evaluate('kanaReviewLessons[1].items[0]'), 1)
        self.assertIn('Vている + N', self.page.locator('#kanaLessonGrammar').inner_text())
        self.reload()
        self.assertEqual(self.page.locator('[data-kana-lesson="2"]').get_attribute('aria-pressed'), 'true')
        self.page.locator('[data-kana-lesson="1"]').click()
        self.assert_kana_question(first_item, 1)
        self.assertEqual(self.page.locator('.kana-review-input').input_value(), answer)
        self.assertIn('is-correct', self.page.locator('.kana-review-question').get_attribute('class'))
        self.assertTrue(self.page.locator('.kana-review-answer').is_visible())

        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html')
        self.page.set_viewport_size({'width': 390, 'height': 844})
        self.page.locator('.tab-btn[onclick*="tab-quiz"]').click()
        self.page.locator('.tab-btn[onclick*="tab-kana"]').click()
        self.assertTrue(self.page.locator('#tab-kana').is_visible())
        self.assertEqual(self.page.locator('.kana-review-entry').count(), 0)
        nav_bottom = self.page.locator('.tab-nav-wrapper').evaluate('el=>el.getBoundingClientRect().bottom')
        heading_top = self.page.locator('.kana-review-heading').evaluate('el=>el.getBoundingClientRect().top')
        self.assertGreaterEqual(heading_top, nav_bottom, 'The sticky tab bar must not cover the kana heading')

    def test_a2_2_review_kana_single_card_answers_variants_and_katakana(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html#tab-kana')
        self.assertTrue(self.page.locator('#tab-kana').is_visible())
        lessons = self.page.evaluate('kanaReviewLessons')
        self.assertEqual([lesson['lesson'] for lesson in lessons], [1, 2, 3, 4])
        self.assertEqual([len(lesson['items']) for lesson in lessons], [20] * 4)
        self.assertEqual(len({item['id'] for lesson in lessons for item in lesson['items']}), 80)
        accepted_count = 0
        for lesson in lessons:
            number = lesson['lesson']
            self.page.locator(f'[data-kana-lesson="{number}"]').click()
            for index, item in enumerate(lesson['items']):
                with self.subTest(lesson=number, question=index + 1):
                    self.assertTrue(item['vi'] and item['jp'] and item['grammar'])
                    card = self.assert_kana_question(item, index + 1)
                    answer_input = card.locator('.kana-review-input')
                    primary = card.locator('[data-kana-action="check"]')
                    self.assertEqual(primary.inner_text(), 'Kiểm tra')
                    for answer in [item['jp'], *item.get('accepted', [])]:
                        # Submit every canonical answer and real accepted variant through the visible textarea.
                        answer_input.fill(f'  {answer}　')
                        self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Chưa chấm')
                        self.assertTrue(card.locator('.kana-review-answer').is_hidden())
                        self.assertEqual(primary.inner_text(), 'Kiểm tra')
                        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), f'Đúng {index} / 20 câu')
                        if index % 2:
                            answer_input.press('Enter')
                        else:
                            primary.click()
                        self.assert_kana_question(item, index + 1)
                        self.assertIn('is-correct', card.get_attribute('class'))
                        self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Đúng')
                        self.assertIn('Chính xác', card.locator('.kana-review-feedback').inner_text())
                        self.assertTrue(card.locator('.kana-review-answer').is_hidden())
                        self.assertEqual(primary.inner_text(), 'Về câu đầu' if index == 19 else 'Câu tiếp')
                        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), f'Đúng {index + 1} / 20 câu')
                    accepted_count += len(item.get('accepted', []))
                    if index in [9, 19]:
                        self.page.locator('#kanaPreviousBtn').click()
                        self.assert_kana_question(lesson['items'][index - 1], index)
                        self.assertEqual(self.page.locator('.kana-review-status').inner_text(), 'Đúng')
                        self.page.locator('#kanaNextBtn').click()
                        self.assert_kana_question(item, index + 1)
                        self.reload()
                        self.assert_kana_question(item, index + 1)
                        self.assertEqual(primary.inner_text(), 'Về câu đầu' if index == 19 else 'Câu tiếp')
                        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), f'Đúng {index + 1} / 20 câu')
                    if (index + number) % 2:
                        answer_input.press('Enter')
                    else:
                        primary.click()
            with self.subTest(lesson=number, state='wrapped and restored'):
                self.assert_kana_question(lesson['items'][0], 1)
                self.assertIn('is-correct', self.page.locator('.kana-review-question').get_attribute('class'))
                self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 20 / 20 câu')
                self.assertEqual(self.page.locator('.kana-review-progress-track').get_attribute('aria-valuenow'), '20')
                self.assertEqual(self.page.locator('.kana-review-progress-track').get_attribute('aria-valuetext'), '20 / 20 câu đúng')
                self.assertEqual(self.page.locator('#kanaReviewProgressBar').evaluate('el=>el.style.width'), '100%')
                self.reload()
                self.assertEqual(self.page.evaluate('kanaLesson'), number)
                self.assert_kana_question(lesson['items'][0], 1)
                self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 20 / 20 câu')
        self.assertGreater(accepted_count, 0, 'Exercise actual alternate answers, not just canonical strings')
        saved = self.page.evaluate("JSON.parse(localStorage.getItem('marugoto_mini_a2_2_1_4_cp_v1'))")
        self.assertEqual(len(saved['kanaAnswers']), 80)
        self.assertTrue(all(answer['checked'] for answer in saved['kanaAnswers'].values()))
        self.assertEqual(saved['kanaQuestionByLesson'], {str(lesson['lesson']): lesson['items'][0]['id'] for lesson in lessons})

        self.page.locator('[data-kana-lesson="2"]').click()
        index = self.page.evaluate('kanaReviewLessons[1].items.findIndex(item => /[ァ-ヶ]/.test(item.jp))')
        self.assertGreaterEqual(index, 0)
        for _ in range(index):
            self.page.locator('#kanaNextBtn').click()
        item = lessons[1]['items'][index]
        hira = self.page.evaluate("item => item.jp.replace(/[ァ-ヶ]/g, char => String.fromCharCode(char.charCodeAt(0)-0x60))", item)
        self.assertNotEqual(hira, item['jp'])
        card = self.assert_kana_question(item, index + 1)
        card.locator('.kana-review-input').fill(hira)
        card.locator('.kana-review-input').press('Enter')
        self.assertIn('Chưa đúng', card.locator('.kana-review-status').inner_text())
        self.assertIn('katakana', card.locator('.kana-review-feedback').inner_text())
        self.assertTrue(card.locator('.kana-review-answer').is_hidden())
        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 19 / 20 câu')
        card.locator('[data-kana-action="reveal"]').click()
        self.assertEqual(card.locator('.kana-review-answer-jp').inner_text(), item['jp'])
        self.assertEqual(card.locator('.kana-review-answer-grammar').inner_text(), item['grammar'])
        card.locator('.kana-review-input').fill(item['jp'])
        self.assertTrue(card.locator('.kana-review-answer').is_hidden())
        self.assertEqual(card.locator('[data-kana-action="reveal"]').get_attribute('aria-expanded'), 'false')
        self.assertEqual(card.locator('[data-kana-action="check"]').inner_text(), 'Kiểm tra')
        card.locator('[data-kana-action="check"]').click()
        self.assertEqual(card.locator('.kana-review-input').input_value(), item['jp'])
        self.assertIn('is-correct', card.get_attribute('class'))
        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 20 / 20 câu')

    def test_a2_2_review_kana_enter_ime_empty_and_invalid_answers(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html#tab-kana')
        items = self.page.evaluate('kanaReviewLessons[0].items')
        card = self.assert_kana_question(items[0], 1)
        answer_input = card.locator('.kana-review-input')
        primary = card.locator('[data-kana-action="check"]')
        for empty in ['', ' \n　 ']:
            answer_input.fill(empty)
            for action in ['click', 'Enter', 'Enter']:
                with self.subTest(empty=repr(empty), action=action):
                    if action == 'click':
                        primary.click()
                    else:
                        answer_input.press(action)
                    self.assert_kana_question(items[0], 1)
                    self.assertIn('chưa nhập', card.locator('.kana-review-feedback').inner_text())
                    self.assertEqual(primary.inner_text(), 'Kiểm tra')
                    self.assertTrue(card.locator('.kana-review-answer').is_hidden())
                    self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 0 / 20 câu')

        for invalid in ['私', 'watashi']:
            with self.subTest(invalid=invalid):
                answer_input.fill(invalid)
                self.assertEqual(primary.inner_text(), 'Kiểm tra')
                answer_input.press('Enter')
                self.assert_kana_question(items[0], 1)
                self.assertIn('is-wrong', card.get_attribute('class'))
                self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Chưa đúng')
                self.assertIn('không nhập Kanji hoặc romaji', card.locator('.kana-review-feedback').inner_text())
                self.assertTrue(card.locator('.kana-review-answer').is_hidden())
                self.assertEqual(primary.inner_text(), 'Câu tiếp')
                answer_input.press('Enter')
                self.assert_kana_question(items[1], 2)
                self.page.locator('#kanaPreviousBtn').click()
                self.assert_kana_question(items[0], 1)
                self.assertEqual(answer_input.input_value(), invalid)

        answer_input.fill(items[0]['jp'])
        answer_input.press('End')
        answer_input.press('Shift+Enter')
        self.assertIn('\n', answer_input.input_value())
        self.assert_kana_question(items[0], 1)
        self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Chưa chấm')
        self.assertEqual(primary.inner_text(), 'Kiểm tra')
        answer_input.fill(items[0]['jp'])
        for expected_status in ['Chưa chấm', 'Đúng']:
            for event in [{'isComposing': True, 'keyCode': 13}, {'isComposing': False, 'keyCode': 229}]:
                with self.subTest(status=expected_status, event=event):
                    answer_input.dispatch_event('keydown', {'key': 'Enter', 'code': 'Enter', **event})
                    self.assert_kana_question(items[0], 1)
                    self.assertEqual(answer_input.input_value(), items[0]['jp'])
                    self.assertEqual(card.locator('.kana-review-status').inner_text(), expected_status)
                    self.assertEqual(primary.inner_text(), 'Kiểm tra' if expected_status == 'Chưa chấm' else 'Câu tiếp')
            if expected_status == 'Chưa chấm':
                answer_input.press('Enter')
                self.assertIn('is-correct', card.get_attribute('class'))
                self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 1 / 20 câu')
        answer_input.press('Enter')
        self.assert_kana_question(items[1], 2)
        self.assertTrue(answer_input.evaluate('el=>el===document.activeElement'))
        self.assertEqual(answer_input.input_value(), '')
        for _ in range(2):
            answer_input.press('Enter')
            self.assert_kana_question(items[1], 2)
            self.assertEqual(primary.inner_text(), 'Kiểm tra')
        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 1 / 20 câu')

    def test_a2_2_review_kana_drafts_reset_and_timer_stay_scoped(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html')
        self.page.locator('#optBtn_p1_1_0').click()
        self.page.locator('#p3_input_16').fill('買った')
        self.page.locator('#p3_btn_16').click()
        self.page.locator('#trans_input_29').fill('あそこでせんせいとはなしているひとです。')
        self.page.locator('#p6_score_25_29').click()
        self.page.locator('#timerToggleBtn').click()
        self.page.clock.run_for(2000)
        self.page.locator('.tab-btn[onclick*="tab-kana"]').click()
        remaining = self.page.evaluate('totalSeconds')
        self.assertFalse(self.page.evaluate('isTimerRunning'))
        self.page.clock.run_for(3000)
        self.assertEqual(self.page.evaluate('totalSeconds'), remaining)
        lessons = self.page.evaluate('kanaReviewLessons')
        card = self.assert_kana_question(lessons[0]['items'][0], 1)
        card.locator('.kana-review-input').fill(lessons[0]['items'][0]['jp'])
        card.locator('[data-kana-action="check"]').click()
        card.locator('[data-kana-action="check"]').click()
        card = self.assert_kana_question(lessons[0]['items'][1], 2)
        card.locator('.kana-review-input').fill('したがきをほぞんします')
        card.locator('[data-kana-action="reveal"]').click()
        self.assertTrue(card.locator('.kana-review-answer').is_visible())
        self.assertEqual(card.locator('[data-kana-action="check"]').inner_text(), 'Câu tiếp')
        self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Chưa chấm')
        card.locator('.kana-review-input').press('Enter')
        self.assert_kana_question(lessons[0]['items'][2], 3)
        self.page.locator('.kana-review-input').fill('まだかいています')

        self.page.locator('[data-kana-lesson="2"]').click()
        for index in range(2):
            card = self.assert_kana_question(lessons[1]['items'][index], index + 1)
            card.locator('.kana-review-input').fill(lessons[1]['items'][index]['jp'])
            card.locator('.kana-review-input').press('Enter')
            self.page.locator('#kanaNextBtn').click()
        self.assert_kana_question(lessons[1]['items'][2], 3)
        self.page.locator('.kana-review-input').fill('watashi')
        self.page.locator('[data-kana-action="check"]').click()
        self.page.locator('#kanaNextBtn').click()
        self.assert_kana_question(lessons[1]['items'][3], 4)
        self.page.locator('.kana-review-input').fill('べつのしたがきです')

        for number, position in [(3, 2), (4, 3)]:
            self.page.locator(f'[data-kana-lesson="{number}"]').click()
            for _ in range(position - 1):
                self.page.locator('#kanaNextBtn').click()
            item = lessons[number - 1]['items'][position - 1]
            card = self.assert_kana_question(item, position)
            card.locator('.kana-review-input').fill(item['jp'])
            card.locator('[data-kana-action="check"]').click()
        self.page.locator('[data-kana-action="reveal"]').click()
        checkpoint = "JSON.parse(localStorage.getItem('marugoto_mini_a2_2_1_4_cp_v1'))"
        saved = self.page.evaluate(checkpoint)
        positions = {str(number): lessons[number - 1]['items'][position - 1]['id']
                     for number, position in [(1, 3), (2, 4), (3, 2), (4, 3)]}
        self.assertEqual(saved['kanaQuestionByLesson'], positions)
        self.reload()
        self.assertEqual(self.page.evaluate('kanaLesson'), 4)
        self.assertEqual(self.page.evaluate(checkpoint)['kanaAnswers'], saved['kanaAnswers'])
        self.assertEqual(self.page.evaluate(checkpoint)['kanaQuestionByLesson'], positions)
        self.assertTrue(self.page.locator('.kana-review-answer').is_visible())
        for number, position, draft, correct in [
            (1, 3, 'まだかいています', 1),
            (2, 4, 'べつのしたがきです', 2),
            (3, 2, lessons[2]['items'][1]['jp'], 1),
            (4, 3, lessons[3]['items'][2]['jp'], 1),
        ]:
            with self.subTest(lesson=number, state='restored'):
                self.page.locator(f'[data-kana-lesson="{number}"]').click()
                self.assert_kana_question(lessons[number - 1]['items'][position - 1], position)
                self.assertEqual(self.page.locator('.kana-review-input').input_value(), draft)
                self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), f'Đúng {correct} / 20 câu')
                self.assertEqual(self.page.locator('.kana-review-status').inner_text(), 'Chưa chấm' if number <= 2 else 'Đúng')

        self.page.locator('[data-kana-lesson="1"]').click()
        self.page.locator('#kanaPreviousBtn').click()
        card = self.assert_kana_question(lessons[0]['items'][1], 2)
        self.assertEqual(card.locator('.kana-review-input').input_value(), 'したがきをほぞんします')
        self.assertTrue(card.locator('.kana-review-answer').is_visible())
        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 1 / 20 câu')
        card.locator('.kana-review-input').fill('なおしたしたがきです')
        self.assertTrue(card.locator('.kana-review-answer').is_hidden())
        self.assertEqual(card.locator('[data-kana-action="check"]').inner_text(), 'Kiểm tra')
        edited = self.page.evaluate(checkpoint)['kanaAnswers'][lessons[0]['items'][1]['id']]
        self.assertFalse(edited['checked'])
        self.assertFalse(edited['revealed'])
        before_reset = self.page.evaluate(checkpoint)
        self.page.get_by_role('button', name='Làm lại bài này', exact=True).click()
        self.assert_kana_question(lessons[0]['items'][0], 1)
        after_reset = self.page.evaluate(checkpoint)
        lesson_ids = {item['id'] for item in lessons[0]['items']}
        self.assertEqual(after_reset['kanaAnswers'], {key: value for key, value in before_reset['kanaAnswers'].items() if key not in lesson_ids})
        self.assertEqual(after_reset['kanaQuestionByLesson'], {**before_reset['kanaQuestionByLesson'], '1': lessons[0]['items'][0]['id']})
        for key in ['p1Answers', 'p2Selected', 'p2Graded', 'p3Inputs', 'p3Graded', 'p4Selected',
                    'p4Graded', 'p5Answers', 'p6Drafts', 'p6SelfScores', 'totalSeconds', 'timerStarted', 'isTimerRunning']:
            self.assertEqual(after_reset[key], before_reset[key], f'Kana reset changed exam field {key}')
        self.reload()
        self.assert_kana_question(lessons[0]['items'][0], 1)
        self.assertEqual(self.page.locator('.kana-review-input').input_value(), '')
        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 0 / 20 câu')
        self.assertEqual(self.page.locator('.kana-review-status').inner_text(), 'Chưa chấm')
        self.assertTrue(self.page.locator('.kana-review-answer').is_hidden())
        self.page.locator('#kanaNextBtn').click()
        self.assert_kana_question(lessons[0]['items'][1], 2)
        self.assertEqual(self.page.locator('.kana-review-input').input_value(), '')
        self.assertTrue(self.page.locator('.kana-review-answer').is_hidden())
        self.page.locator('[data-kana-lesson="2"]').click()
        self.assert_kana_question(lessons[1]['items'][3], 4)
        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 2 / 20 câu')
        self.page.locator('#kanaPreviousBtn').click()
        self.assertEqual(self.page.locator('.kana-review-input').input_value(), 'watashi')
        self.assertEqual(self.page.locator('.kana-review-status').inner_text(), 'Chưa đúng')
        self.assertEqual(self.page.evaluate('p1Answers[1]'), 0)
        self.assertEqual(self.page.evaluate('totalSeconds'), remaining)
        self.page.locator('.tab-btn[onclick*="tab-quiz"]').click()
        self.reload()
        self.assertEqual(self.page.locator('.tab-panel.active').get_attribute('id'), 'tab-quiz')
        self.assertEqual(self.page.locator('#p3_input_16').input_value(), '買った')
        self.assertEqual(self.page.locator('#trans_input_29').input_value(), 'あそこでせんせいとはなしているひとです。')
        self.assertEqual(self.page.evaluate('p6SelfScores[29]'), 2.5)
        self.assertFalse(self.page.evaluate('isTimerRunning'))
        self.assertEqual(self.page.evaluate('totalSeconds'), remaining)
        self.page.locator('#timerToggleBtn').click()
        self.page.clock.run_for(2000)
        self.assertEqual(self.page.evaluate('totalSeconds'), remaining - 2)
        self.page.locator('.tab-btn[onclick*="tab-kana"]').click()
        self.page.clock.run_for(3000)
        self.assertFalse(self.page.evaluate('isTimerRunning'))
        self.assertEqual(self.page.evaluate('totalSeconds'), remaining - 2)

    def test_a2_2_review_kana_legacy_checkpoint_defaults_positions_and_keeps_grades(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html#tab-kana')
        lessons = self.page.evaluate('kanaReviewLessons')
        for number in [1, 2]:
            self.page.locator(f'[data-kana-lesson="{number}"]').click()
            card = self.assert_kana_question(lessons[number - 1]['items'][0], 1)
            card.locator('.kana-review-input').fill(lessons[number - 1]['items'][0]['jp'])
            card.locator('[data-kana-action="check"]').click()
            self.page.locator('#kanaNextBtn').click()
            card = self.assert_kana_question(lessons[number - 1]['items'][1], 2)
            card.locator('.kana-review-input').fill('watashi')
            card.locator('.kana-review-input').press('Enter')
            card.locator('[data-kana-action="reveal"]').click()
            self.page.locator('#kanaNextBtn').click()
            self.assert_kana_question(lessons[number - 1]['items'][2], 3)
            self.page.locator('.kana-review-input').fill('ふるいしたがきです')
        checkpoint = "JSON.parse(localStorage.getItem('marugoto_mini_a2_2_1_4_cp_v1'))"
        saved = self.page.evaluate(checkpoint)
        self.page.evaluate("""() => {
            const key = 'marugoto_mini_a2_2_1_4_cp_v1';
            const saved = JSON.parse(localStorage.getItem(key));
            delete saved.kanaQuestionByLesson;
            localStorage.setItem(key, JSON.stringify(saved));
        }""")
        self.reload()
        self.assertEqual(self.page.evaluate('kanaLesson'), 2)
        for number in [2, 1, 3, 4]:
            with self.subTest(lesson=number):
                self.page.locator(f'[data-kana-lesson="{number}"]').click()
                card = self.assert_kana_question(lessons[number - 1]['items'][0], 1)
                self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), f'Đúng {1 if number <= 2 else 0} / 20 câu')
                if number <= 2:
                    self.assertIn('is-correct', card.get_attribute('class'))
                    self.assertEqual(card.locator('.kana-review-input').input_value(), lessons[number - 1]['items'][0]['jp'])
                    self.page.locator('#kanaNextBtn').click()
                    card = self.assert_kana_question(lessons[number - 1]['items'][1], 2)
                    self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Chưa đúng')
                    self.assertEqual(card.locator('.kana-review-input').input_value(), 'watashi')
                    self.assertTrue(card.locator('.kana-review-answer').is_visible())
                    self.page.locator('#kanaNextBtn').click()
                    card = self.assert_kana_question(lessons[number - 1]['items'][2], 3)
                    self.assertEqual(card.locator('.kana-review-input').input_value(), 'ふるいしたがきです')
                    self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Chưa chấm')
        self.assertEqual(self.page.evaluate(checkpoint)['kanaAnswers'], saved['kanaAnswers'])
        self.reload()
        self.page.locator('[data-kana-lesson="1"]').click()
        self.assert_kana_question(lessons[0]['items'][2], 3)
        self.assertEqual(self.page.locator('.kana-review-input').input_value(), 'ふるいしたがきです')

    def test_a2_2_review_kana_content_changes_keep_only_unchanged_grades(self):
        self.go('tests/On_Tap_Mini_Test_A2_2_1_4.html#tab-kana')
        items = self.page.evaluate('kanaReviewLessons[0].items')
        for index in range(2):
            card = self.assert_kana_question(items[index], index + 1)
            card.locator('.kana-review-input').fill(items[index]['jp'])
            card.locator('[data-kana-action="check"]').click()
            if index == 0:
                card.locator('[data-kana-action="check"]').click()
        self.page.locator('#kanaPreviousBtn').click()
        self.page.locator('[data-kana-action="reveal"]').click()
        draft = self.page.locator('.kana-review-input').input_value()

        def revise_prompt(route):
            response = route.fetch()
            route.fulfill(response=response, body=response.text() + '\nwindow.MINI_A2_2_1_4_DATA.kanaReviewLessons[0].items[0].vi += " (Nội dung mới)";')

        self.page.route('**/assets/data/mini_a2_2_1_4_data.js?*', revise_prompt)
        self.reload()
        changed_item = {**items[0], 'vi': items[0]['vi'] + ' (Nội dung mới)'}
        card = self.assert_kana_question(changed_item, 1)
        self.assertEqual(card.locator('.kana-review-input').input_value(), draft)
        self.assertEqual(self.page.locator('#kanaReviewProgress').inner_text(), 'Đúng 1 / 20 câu')
        self.assertTrue(card.locator('.kana-review-answer').is_hidden())
        self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Chưa chấm')
        self.assertEqual(card.locator('[data-kana-action="check"]').inner_text(), 'Kiểm tra')
        self.page.locator('#kanaNextBtn').click()
        card = self.assert_kana_question(items[1], 2)
        self.assertEqual(card.locator('.kana-review-input').input_value(), items[1]['jp'])
        self.assertEqual(card.locator('.kana-review-status').inner_text(), 'Đúng')
        self.assertIn('is-correct', card.get_attribute('class'))
        self.page.locator('#kanaPreviousBtn').click()
        self.assert_kana_question(changed_item, 1)
        self.assertEqual(self.page.locator('.kana-review-input').input_value(), draft)

    def test_timed_mini_tests_restart_timer_after_expiry(self):
        for path, reset in [
            ('tests/On_Tap_Mini_Test_A2_11_14.html', 'resetAllExam'),
            ('tests/On_Tap_Mini_Test_A2_2_1_4.html', 'resetExamSuite'),
        ]:
            with self.subTest(page=path):
                self.go(path)
                if '11_14' in path:
                    self.page.evaluate("switchMainTab('tab-quiz')")
                self.page.evaluate('toggleTimer();totalSeconds=1')
                self.page.clock.run_for(2500)
                self.page.evaluate(reset+'()')
                self.assertEqual(self.page.evaluate('totalSeconds'), 2700)
                self.page.clock.run_for(5000)
                self.assertEqual(self.page.evaluate('totalSeconds'), 2695)

    def test_all_kanji_entries_remain_visible_in_all_lessons_filter(self):
        self.go('kanji_a2.html')
        result = self.page.evaluate("""() => {
            selectPreset('ALL');
            return {total:kanjiData.length,visible:filteredKanji.length,
                invalid:kanjiData.filter(item=>!KANJI_LESSON_ORDER.includes(item.lesson))};
        }""")
        self.assertEqual(result, {'total': 144, 'visible': 144, 'invalid': []})

    def test_kanji_late_svg_response_cannot_replace_new_character(self):
        self.go('kanji_a2.html')
        applied = self.page.evaluate("""async () => {
            const pending=[];const applied=[];
            fetchKanjiSvg=char=>new Promise(resolve=>pending.push({char,resolve}));
            setupSvgPlayer=(index,svg)=>applied.push({index,svg});
            const oldItem=kanjiData[0];
            const newItem=kanjiData.find(item=>item.char!==oldItem.char);
            kanjiViewMode='cards';kanjiCurrentPage=1;
            filteredKanji=[oldItem];renderCards(filteredKanji);initKanjiPlayer(oldItem,0);
            filteredKanji=[newItem];renderCards(filteredKanji);initKanjiPlayer(newItem,0);
            pending[1].resolve('<svg id="moon"></svg>');await Promise.resolve();
            pending[0].resolve('<svg id="day"></svg>');await Promise.resolve();
            return applied;
        }""")
        self.assertEqual(applied, [{'index': 0, 'svg': '<svg id="moon"></svg>'}])

    def test_lesson_3d_buttons_bind_current_vocab_indices(self):
        for lesson in range(10, 19):
            with self.subTest(lesson=lesson):
                self.go(f'lessons/Marugoto_A2_Lesson_{lesson}.html')
                result = self.page.evaluate("""() => {
                    const opened=[];window.openVocab3D=index=>opened.push(index);
                    const cards=[...document.querySelectorAll('#flashcardGrid .fc-3d-stage, #flashcardsGrid .fc-3d-stage')];
                    cards.forEach(card=>card.click());
                    return {opened,total:VOCAB_DATA.length};
                }""")
                self.assertGreater(result['total'], 0)
                self.assertEqual(result['opened'], list(range(result['total'])))

    def test_a2_2_adjective_question_and_verb_lab_labels(self):
        self.go('lessons/Marugoto_A2_2_Lesson_14.html')
        sentence = self.page.evaluate("""() => {
            const question=QUIZ_DATA.find(q=>q.id===7);
            return question.q.replace('[____]',question.options[question.correct]).replace(/\\s+/g,'');
        }""")
        self.assertIn('すばらしかったです', sentence)
        self.assertNotIn('すばらしかったでした', sentence)
        for lesson in [5, 6]:
            with self.subTest(lesson=lesson):
                self.go(f'lessons/Marugoto_A2_2_Lesson_{lesson}.html')
                label = self.page.locator('#morphTeKi').evaluate(
                    "el=>el.parentElement.querySelector('.morph-label').textContent")
                self.assertNotIn('quá khứ', label.lower())

    def test_a2_2_revised_question_drops_only_its_stale_checkpoint(self):
        self.go('index.html')
        self.page.evaluate("""() => {
            localStorage.setItem('marugoto_cp_v1::lessons/Marugoto_A2_2_Lesson_14.html::clicks',
                JSON.stringify({t:1,d:[
                    "oc::checkQuizAnswer(this,0,0,'a22-reviewed-v2')",
                    "oc::checkQuizAnswer(this,6,0,'a22-reviewed-v2')"
                ]}));
        }""")
        self.go('lessons/Marugoto_A2_2_Lesson_14.html')
        cards = self.page.locator('#quizContainer .quiz-card')
        self.assertEqual(cards.nth(0).locator('button:disabled').count(), 4)
        self.assertEqual(cards.nth(6).locator('button:disabled').count(), 0)
        correct = self.page.evaluate('QUIZ_DATA[6].correct')
        cards.nth(6).locator('.quiz-opt').nth(correct).click()
        self.reload()
        self.assertEqual(cards.nth(0).locator('button:disabled').count(), 4)
        self.assertEqual(cards.nth(6).locator('button.correct').count(), 1)

    def test_a2_2_sentence_and_kanji_typing_checkpoint_and_responsive_layout(self):
        expected_kanji_counts = [16, 18, 18, 10]
        for lesson in range(1, 5):
            with self.subTest(lesson=lesson):
                self.go(f'lessons/Marugoto_A2_2_Lesson_{lesson}.html')
                self.assertEqual(self.page.locator('.sentence-practice-card:not(.sentence-practice-kanji-card)').count(), 40)
                self.assertEqual(self.page.locator('.sentence-practice-kanji-card').count(), expected_kanji_counts[lesson - 1])
                self.assertTrue(self.page.locator('.sentence-practice-answer').first.is_hidden())

                for width in [360, 390, 768, 1440]:
                    self.page.set_viewport_size({'width': width, 'height': 900})
                    self.assertEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)
                    self.assertTrue(self.page.locator('.sentence-practice-entry').first.evaluate(
                        "el=>{const r=el.getBoundingClientRect();return r.left>=0&&r.right<=innerWidth+1}"))

                first = self.page.locator('.sentence-practice-card:not(.sentence-practice-kanji-card)').first
                expected_sentence = self.page.evaluate('SENTENCE_PRACTICE_DATA[0].jp')
                first.locator('.sentence-practice-input').fill(expected_sentence)
                first.locator('.sentence-practice-input').evaluate(
                    "el=>el.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',keyCode:229,which:229,isComposing:true,bubbles:true}))")
                self.assertIn('Chưa gõ', first.locator('.sentence-practice-status').inner_text())
                first.locator('.sentence-practice-check').click()
                self.assertIn('Đúng', first.locator('.sentence-practice-status').inner_text())
                self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '1 / 40')

                kanji_card = self.page.locator('.sentence-practice-kanji-card').first
                kanji_answer = self.page.evaluate("""() => {
                    const item=KANJI_PRACTICE_DATA[0];
                    return {word:item.word,kana:item.kana};
                }""")
                self.assertIsNotNone(kanji_answer['kana'])
                kanji_card.locator('.sentence-practice-input').fill(kanji_answer['kana'])
                kanji_card.locator('.sentence-practice-check').click()
                self.assertIn('Chưa đúng', kanji_card.locator('.sentence-practice-status').inner_text())
                self.assertIn('Kanji', kanji_card.locator('.sentence-practice-feedback').inner_text())
                kanji_card.locator('.sentence-practice-input').fill(kanji_answer['word'])
                kanji_card.locator('.sentence-practice-check').click()
                self.assertIn('Đúng', kanji_card.locator('.sentence-practice-status').inner_text())

                second = self.page.locator('.sentence-practice-card:not(.sentence-practice-kanji-card)').nth(1)
                second.locator('.sentence-practice-input').fill('下書きを保存します')
                second.locator('.sentence-practice-reveal').click()
                self.assertEqual(second.locator('.sentence-practice-input').input_value(), '下書きを保存します')
                self.assertTrue(second.locator('.sentence-practice-answer').is_visible())
                self.reload()
                first = self.page.locator('.sentence-practice-card:not(.sentence-practice-kanji-card)').first
                second = self.page.locator('.sentence-practice-card:not(.sentence-practice-kanji-card)').nth(1)
                self.assertIn('Đúng', first.locator('.sentence-practice-status').inner_text())
                self.assertEqual(second.locator('.sentence-practice-input').input_value(), '下書きを保存します')
                self.assertTrue(second.locator('.sentence-practice-answer').is_visible())
                self.assertIn('Đúng', self.page.locator('.sentence-practice-kanji-card').first.locator('.sentence-practice-status').inner_text())

                self.page.locator('#sentenceReset').click()
                self.assertEqual(first.locator('.sentence-practice-input').input_value(), '')
                self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '0 / 40')
                self.reload()
                self.assertEqual(self.page.locator('.sentence-practice-card:not(.sentence-practice-kanji-card)').first.locator('.sentence-practice-input').input_value(), '')
                self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '0 / 40')
                kanji_card = self.page.locator('.sentence-practice-kanji-card').first
                self.assertEqual(kanji_card.locator('.sentence-practice-input').input_value(), '')
                self.assertEqual(self.page.locator('#kanjiPracticeProgress').inner_text(), f'0 / {expected_kanji_counts[lesson - 1]}')
                first = self.page.locator('.sentence-practice-card:not(.sentence-practice-kanji-card)').first
                first.locator('.sentence-practice-input').fill(expected_sentence)
                first.locator('.sentence-practice-check').click()
                self.reload()
                self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '1 / 40')

    def test_a2_2_sentence_typing_migrates_legacy_and_invalidates_only_changed_content(self):
        self.go('lessons/Marugoto_A2_2_Lesson_1.html')
        self.page.evaluate("""() => {
            const legacy = {
                revision: 'a2-2-typing40-v1',
                items: {
                    1: {draft: SENTENCE_PRACTICE_DATA[0].jp, status: 'correct', feedback: 'Chính xác.'},
                    11: {draft: '私はこの国際交流が好きです。', status: 'correct', feedback: 'Chính xác.'}
                },
                kanjiItems: {[KANJI_PRACTICE_DATA[0].id]: {draft: KANJI_PRACTICE_DATA[0].word, status: 'correct'}},
                showAllAnswers: false
            };
            MarugotoCheckpoint.save('typing_sentences_a2_2_v1', legacy);
            MarugotoCheckpoint.save('inputs', {'id::sentencePracticeInput1': '古い下書き'});
        }""")
        self.reload()
        first = self.page.locator('#sentencePracticeInput1')
        changed = self.page.locator('#sentencePracticeInput11')
        expected = self.page.evaluate('SENTENCE_PRACTICE_DATA[0].jp')
        self.assertEqual(first.input_value(), expected)
        self.assertIn('Đúng', first.locator('xpath=ancestor::article').locator('.sentence-practice-status').inner_text())
        self.assertEqual(changed.input_value(), '私はこの国際交流が好きです。')
        self.assertIn('Chưa gõ', changed.locator('xpath=ancestor::article').locator('.sentence-practice-status').inner_text())
        self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '1 / 40')
        self.assertEqual(self.page.locator('#kanjiPracticeProgress').inner_text(), '1 / 16')

        # Persist content signatures, then change just one prompt in the delivered lesson data.
        second = self.page.locator('#sentencePracticeInput2')
        second.fill(self.page.evaluate('SENTENCE_PRACTICE_DATA[1].jp'))
        second.locator('xpath=ancestor::article').locator('.sentence-practice-check').click()

        def change_prompt(route):
            response = route.fetch()
            route.fulfill(response=response, body=response.text() + '\nSENTENCE_PRACTICE_DATA[0].vi = "Changed prompt";')

        self.page.route('**/assets/js/lessons/lesson_a2_2_01.js?*', change_prompt)
        self.reload()
        first = self.page.locator('#sentencePracticeInput1')
        self.assertEqual(first.input_value(), expected)
        self.assertIn('Chưa gõ', first.locator('xpath=ancestor::article').locator('.sentence-practice-status').inner_text())
        self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '1 / 40')
        self.assertIn('Đúng', self.page.locator('#sentencePracticeInput2').locator('xpath=ancestor::article').locator('.sentence-practice-status').inner_text())
        self.assertEqual(self.page.locator('#kanjiPracticeProgress').inner_text(), '1 / 16')

        # A reset must also ignore snapshots left behind by the older generic input saver.
        self.page.locator('#sentenceReset').click()
        self.reload()
        self.assertEqual(self.page.locator('#sentencePracticeInput1').input_value(), '')
        self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '0 / 40')
        self.assertEqual(self.page.locator('#kanjiPracticeProgress').inner_text(), '0 / 16')

    def test_a2_2_sentence_typing_uses_one_key_before_checkpoint_engine_loads(self):
        self.go('lessons/Marugoto_A2_2_Lesson_1.html')
        expected = self.page.evaluate('SENTENCE_PRACTICE_DATA[0].jp')
        self.page.evaluate("""() => {
            localStorage.setItem(MarugotoCheckpoint.getKey('typing_sentences_a2_2_v1'), JSON.stringify({
                t: 12344,
                d: {revision: 'a2-2-typing40-v1', items: {}}
            }));
            localStorage.setItem(`marugoto_cp_v1::${location.pathname}::typing_sentences_a2_2_v1`, JSON.stringify({
                t: 12345,
                d: {revision: 'a2-2-typing40-v1', items: {1: {draft: SENTENCE_PRACTICE_DATA[0].jp, status: 'correct'}}}
            }));
        }""")
        self.page.route('**/checkpoint-sync.js?*', lambda route: route.abort())
        self.reload()
        self.assertEqual(self.page.locator('#sentencePracticeInput1').input_value(), expected)
        self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '1 / 40')
        self.assertIsNone(self.page.evaluate('localStorage.getItem(`marugoto_cp_v1::${location.pathname}::typing_sentences_a2_2_v1`)'))
        first = self.page.locator('#sentencePracticeInput1')
        first.fill(expected)
        first.locator('xpath=ancestor::article').locator('.sentence-practice-check').click()
        self.page.unroute('**/checkpoint-sync.js?*')
        self.reload()
        self.assertEqual(self.page.locator('#sentencePracticeInput1').input_value(), expected)
        self.assertEqual(self.page.locator('#sentencePracticeProgress').inner_text(), '1 / 40')
        self.assertEqual(self.page.evaluate("MarugotoCheckpoint.load('typing_sentences_a2_2_v1').items[1].status"), 'correct')


if __name__ == "__main__":
    unittest.main(verbosity=2)
