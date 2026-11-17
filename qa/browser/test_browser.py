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
        for entry in ["index.html", "lessons/Marugoto_A2_Lesson_1.html"]:
            self.go(entry)
            for lesson in [1, 2]:
                link = self.page.locator(f'#lessonsDropdownMenu a[href$="Marugoto_A2_2_Lesson_{lesson}.html"]')
                self.assertEqual(link.count(), 1)
                self.assertEqual(self.page.request.get(link.evaluate("(el)=>el.href")).status, 200)
        for lesson in [1, 2]:
            self.go(f"lessons/Marugoto_A2_2_Lesson_{lesson}.html")
            self.assertEqual(self.page.locator("#flashcardGrid .fc-item").count(), 20 if lesson == 1 else 17)
            missing = self.page.evaluate("""async () => {
                const urls=[...document.querySelectorAll('script[src],link[rel="stylesheet"]')]
                    .map(el=>el.src || el.href).filter(url=>url.startsWith(location.origin));
                return (await Promise.all(urls.map(async url=>({url,status:(await fetch(url)).status}))))
                    .filter(result=>result.status!==200);
            }""")
            self.assertEqual(missing, [])

    def test_a2_2_flashcards_audio_typing_and_responsive_layout(self):
        for lesson in [1, 2]:
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
        for lesson in [1, 2]:
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
            self.assertEqual(result, {"correct": 15, "positions": 4})
            self.reload()
            self.assertEqual(self.page.locator("#quizContainer button.correct").count(), 15)
            self.assertEqual(self.page.locator("#quizContainer button:disabled").count(), 60)

    def test_a2_2_kanji_filters_audio_and_restore(self):
        self.go("kanji_a2.html")
        self.page.locator('[onclick="switchTab(\\\'tab-vocab-11-18\\\')"]').click()
        for lesson, count in [(1, 15), (2, 16)]:
            self.page.locator(f'.filter-121-btn[onclick*="A2-2 L{lesson}"]').click()
            self.assertEqual(self.page.locator("#table121Body tr").count(), count)
            self.page.evaluate("() => {window.__spoken=[];window.speakText=text=>__spoken.push(text);}")
            expected = self.page.locator("#table121Body tr").first.locator("td").nth(3).inner_text()
            self.page.locator("#table121Body .btn-sound-small").first.click()
            self.assertEqual(self.page.evaluate("__spoken.at(-1)"), expected)
            self.reload()
            self.assertEqual(self.page.evaluate("current121Lesson"), f"A2-2 L{lesson}")
            self.assertEqual(self.page.locator("#table121Body tr").count(), count)

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
        question_id = self.page.evaluate("getExamItems().find(q=>q.contentRevision===2).id")
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
