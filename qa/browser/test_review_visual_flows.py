"""Real-browser regressions for review issues #7, #8, #9 and #11.

Run: PYTHONDONTWRITEBYTECODE=1 python3 qa/browser/test_review_visual_flows.py
Requires Python Playwright and Chromium or installed Chrome. CHROME_PATH works
as in test_browser.py. No CDN, real profile, or saved user checkpoint is used.
3D tests use the bundled real Three.js renderer, never a fake renderer. They
explicitly skip if this browser has no WebGL, rather than claiming GPU coverage.
"""
import re
import unittest
from urllib.parse import urlparse

from playwright.sync_api import expect

try:
    from . import test_browser as harness
except ImportError:
    import test_browser as harness


WIDTHS = (360, 1440)
SVG_PATTERN = re.compile(r"https://.*/[0-9a-f]{5}\.svg(?:\?.*)?$")
LESSON_COUNTS = (7, 7, 9, 8, 7, 8, 8, 9, 6, 11, 6, 7, 9, 8, 9, 10, 8, 7)


def stroke_svg(path):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 109 109">'
            f'<g><path d="{path}"/></g></svg>')


class ReviewVisualFlows(unittest.TestCase):
    # Reuse the local HTTP server and browser fallback without inheriting and
    # accidentally running all of StudyFlows' unrelated tests a second time.
    setUpClass = classmethod(harness.StudyFlows.setUpClass.__func__)
    tearDownClass = classmethod(harness.StudyFlows.tearDownClass.__func__)

    def setUp(self):
        self.context = self.browser.new_context(
            viewport={"width": WIDTHS[0], "height": 900}, reduced_motion="reduce")
        self.context.route("https://**/*", lambda route: route.abort())
        self.context.add_init_script("localStorage.clear()")
        self.page = self.context.new_page()
        self.page.set_default_timeout(10000)
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))
        self.page.on("dialog", lambda dialog: dialog.accept())

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [], "Uncaught browser errors")

    def go(self, path, width):
        self.page.set_viewport_size({"width": width, "height": 900})
        self.page.goto(self.base + path, wait_until="load")

    def grid_chars(self):
        return self.page.locator("#cardsContainer .k-tile-char").all_text_contents()

    def assert_grid(self, expected):
        tiles = self.page.locator("#cardsContainer .kanji-compact-tile")
        expect(tiles).to_have_count(len(expected))
        self.assertEqual(self.grid_chars(), expected)
        self.assertTrue(tiles.evaluate_all("""els => els.every(el => {
            const box = el.getBoundingClientRect();
            return box.width > 0 && box.height > 0 &&
                getComputedStyle(el).visibility !== 'hidden';
        })"""), "Filtered Kanji must be rendered, not just present in JS data")

    def test_144_kanji_schema_pagination_and_lesson_filters(self):
        for width in WIDTHS:
            with self.subTest(width=width):
                self.go("kanji_a2.html", width)
                expect(self.page.locator("#tabCountCards")).to_have_text("144")
                result = self.page.evaluate(r"""() => ({
                    keys: kanjiData.map(k => `${k.lesson}:${k.char}`),
                    chars: kanjiData.map(k => k.char),
                    invalid: kanjiData.filter(k =>
                        !/^\p{Script=Han}$/u.test(k.char) ||
                        !Number.isInteger(k.strokes) || k.strokes <= 0 ||
                        !/^L(?:[1-9]|1[0-8])$/.test(k.lesson) ||
                        ['hv', 'meaning', 'kun', 'on', 'lessonName',
                         'formula', 'strokeGuide', 'mnemonic'].some(
                            key => typeof k[key] !== 'string') ||
                        !k.meaning.trim() || !k.hv.trim() ||
                        !(k.kun.trim() || k.on.trim()) ||
                        !Array.isArray(k.examples) || !k.examples.length ||
                        k.examples.some(ex => ['word', 'reading', 'vi'].some(
                            key => typeof ex[key] !== 'string' || !ex[key].trim()))
                    ).map(k => k.char)
                })""")
                self.assertEqual(result["invalid"], [])
                self.assertEqual(len(result["chars"]), 144)
                # Some characters intentionally recur in different lessons.
                self.assertEqual(len(set(result["keys"])), 144)
                seen = []
                for start in range(0, 144, 24):
                    expected = result["chars"][start:start + 24]
                    self.assert_grid(expected)
                    seen.extend(self.grid_chars())
                    next_button = self.page.locator("#kanjiPaginationTop").get_by_role(
                        "button", name="Tiếp →", exact=True)
                    if start + 24 < 144:
                        next_button.click()
                    else:
                        expect(next_button).to_be_disabled()
                self.assertEqual(seen, result["chars"])

                # Public range controls select each of the 18 lessons, including
                # data formerly missing/invalid in the last lessons.
                self.page.locator("#btnToggleDrawer").click()
                for lesson, count in enumerate(LESSON_COUNTS, 1):
                    self.page.locator("#rangeStartBar").select_option(f"L{lesson}")
                    self.page.locator("#rangeEndBar").select_option(f"L{lesson}")
                    self.page.locator(".btn-range-apply").click()
                    expected = self.page.evaluate(
                        "lesson => kanjiData.filter(k => k.lesson === lesson).map(k => k.char)",
                        f"L{lesson}")
                    self.assertEqual(len(expected), count)
                    expect(self.page.locator("#tabCountCards")).to_have_text(str(count))
                    self.assert_grid(expected)
                self.page.locator("#preset-all").click()
                self.page.locator("#searchInput").fill(result["chars"][-1])
                expect(self.page.locator("#tabCountCards")).to_have_text("1")
                self.assert_grid([result["chars"][-1]])
                self.page.locator("#searchClearBtn").click()
                expect(self.page.locator("#tabCountCards")).to_have_text("144")
                self.assert_grid(result["chars"][:24])

    def install_real_renderer_probe(self):
        return self.page.evaluate("""() => {
            const canvas = document.createElement('canvas');
            const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
            if (!gl) return false;
            gl.getExtension('WEBGL_lose_context')?.loseContext();
            const probe = window.__review3D = {
                renders: 0, renderers: 0, meshes: 0, drawCalls: 0,
                nonUniformPixels: false, pending: new Set(), rotations: []
            };
            const raf = window.requestAnimationFrame.bind(window);
            const cancel = window.cancelAnimationFrame.bind(window);
            window.requestAnimationFrame = callback => {
                let id = raf(time => {
                    probe.pending.delete(id);
                    callback(time);
                });
                if (callback.name === 'animate') probe.pending.add(id);
                return id;
            };
            window.cancelAnimationFrame = id => {
                probe.pending.delete(id);
                return cancel(id);
            };
            const RealRenderer = THREE.WebGLRenderer;
            THREE.WebGLRenderer = class extends RealRenderer {
                constructor(options) {
                    super(options);
                    probe.renderers++;
                    const render = this.render.bind(this);
                    this.render = (scene, camera) => {
                        render(scene, camera);
                        probe.renders++;
                        probe.drawCalls = this.info.render.calls;
                        let meshes = 0;
                        scene.traverse(obj => { if (obj.isMesh) meshes++; });
                        probe.meshes = meshes;
                        const model = scene.children.find(obj => obj.isGroup);
                        if (model) probe.rotations.push(model.rotation.y);
                        if (!probe.nonUniformPixels) {
                            const context = this.getContext();
                            const pixels = new Uint8Array(
                                context.drawingBufferWidth * context.drawingBufferHeight * 4);
                            context.readPixels(0, 0, context.drawingBufferWidth,
                                context.drawingBufferHeight, context.RGBA,
                                context.UNSIGNED_BYTE, pixels);
                            for (let i = 4; i < pixels.length; i += 4) {
                                if (pixels[i] !== pixels[0] || pixels[i+1] !== pixels[1] ||
                                    pixels[i+2] !== pixels[2] || pixels[i+3] !== pixels[3]) {
                                    probe.nonUniformPixels = true;
                                    break;
                                }
                            }
                        }
                    };
                }
            };
            return true;
        }""")

    def exercise_3d_lesson(self, lesson):
        for width in WIDTHS:
            with self.subTest(lesson=lesson, width=width):
                self.go(f"lessons/Marugoto_A2_Lesson_{lesson}.html", width)
                grid_id = "flashcardGrid" if lesson == 10 else "flashcardsGrid"
                trigger = self.page.locator(f"#{grid_id} .fc-3d-stage").first
                expect(trigger).to_be_visible()
                self.page.clock.install()
                if not self.install_real_renderer_probe():
                    self.skipTest("Real browser has no WebGL context. No renderer is mocked.")
                previous_overflow = self.page.evaluate("document.body.style.overflow")
                expected = self.page.evaluate("({kana: VOCAB_DATA[0].kana || VOCAB_DATA[0].jp, count: VOCAB_DATA.length})")
                for cycle in range(2):
                    before_renders = self.page.evaluate("""() => {
                        __review3D.rotations = [];
                        __review3D.nonUniformPixels = false;
                        return __review3D.renders;
                    }""")
                    trigger.click()
                    self.page.clock.run_for(150)
                    expect(self.page.locator("#vocab3DModal")).to_have_class(re.compile(r"\bshow\b"))
                    expect(self.page.locator("#v3dCanvas")).to_be_visible()
                    expect(self.page.locator("#v3dKana")).to_have_text(expected["kana"])
                    expect(self.page.locator("#v3dCounter")).to_have_text(f'1 / {expected["count"]}')
                    state = self.page.evaluate("""() => ({
                        renders: __review3D.renders, renderers: __review3D.renderers,
                        meshes: __review3D.meshes, drawCalls: __review3D.drawCalls,
                        pixels: __review3D.nonUniformPixels,
                        pending: __review3D.pending.size,
                        animated: new Set(__review3D.rotations).size > 1,
                        width: v3dCanvas.width, height: v3dCanvas.height
                    })""")
                    self.assertGreater(state["renders"], before_renders + 1)
                    self.assertEqual(state["renderers"], 1, "Reopen must reuse the WebGL context")
                    self.assertGreater(state["meshes"], 1)
                    self.assertGreater(state["drawCalls"], 0)
                    self.assertTrue(state["pixels"], "Real framebuffer must contain rendered geometry")
                    self.assertTrue(state["animated"])
                    self.assertEqual(state["pending"], 1, "Exactly one 3D animation RAF")
                    self.assertGreater(state["width"], 0)
                    self.assertGreater(state["height"], 0)
                    if cycle == 0:
                        self.page.locator(".v3d-close-btn").click()
                    else:
                        self.page.keyboard.press("Escape")
                    expect(self.page.locator("#vocab3DModal")).not_to_have_class(re.compile(r"\bshow\b"))
                    self.assertEqual(self.page.evaluate("__review3D.pending.size"), 0)
                    closed_renders = self.page.evaluate("__review3D.renders")
                    self.page.clock.run_for(500)
                    self.assertEqual(self.page.evaluate("__review3D.renders"), closed_renders,
                                     "Close must stop rendering, not only hide the canvas")
                    self.assertEqual(self.page.evaluate("document.body.style.overflow"), previous_overflow)

    def test_lesson10_3d_click_renders_and_close_stops_loop(self):
        self.exercise_3d_lesson(10)

    def test_lesson18_3d_click_renders_and_close_stops_loop(self):
        self.exercise_3d_lesson(18)

    def test_menu_reanchors_after_dock_and_syncs_scroll_lock_on_resize(self):
        self.go('index.html', 1440)
        self.page.evaluate("window.scrollTo({top: 400, behavior: 'instant'})")
        expect(self.page.locator('body')).to_have_class(re.compile(r'\bis-hub-docked\b'))
        self.page.locator('#globalHubDock button[onclick*="toggleFormsDropdown"]').click()
        menu = self.page.locator('#formsDropdownMenu')
        expect(menu).to_have_class(re.compile(r'\bshow\b'))
        self.assertEqual(menu.evaluate('el => getComputedStyle(el).position'), 'fixed')
        self.page.keyboard.press('Escape')
        self.page.evaluate("window.scrollTo({top: 0, behavior: 'instant'})")
        expect(self.page.locator('body')).not_to_have_class(re.compile(r'\bis-hub-docked\b'))
        self.page.locator('#hubBtnForms').click()
        self.assertEqual(menu.evaluate('el => getComputedStyle(el).position'), 'absolute')
        self.assertGreaterEqual(menu.bounding_box()['x'], 0)

        self.page.set_viewport_size({'width': 390, 'height': 844})
        expect(self.page.locator('body')).to_have_class(re.compile(r'\bhub-menu-open\b'))
        self.assertEqual(self.page.evaluate('document.body.style.overflow'), 'hidden')
        expect(menu).to_be_visible()
        self.page.set_viewport_size({'width': 1440, 'height': 900})
        expect(self.page.locator('body')).not_to_have_class(re.compile(r'\bhub-menu-open\b'))
        self.assertEqual(self.page.evaluate('document.body.style.overflow'), '')
        self.page.keyboard.press('Escape')
        expect(menu).not_to_have_class(re.compile(r'\bshow\b'))

    def test_mobile_menu_obeys_reduced_motion_and_preserves_existing_overflow(self):
        self.go('index.html', 390)
        self.page.evaluate("document.body.style.overflow = 'auto'")
        self.page.locator('#hubBtnForms').click()
        for selector in ('#formsDropdownMenu', '#hubNavBackdrop'):
            self.assertEqual(self.page.locator(selector).evaluate(
                'el => getComputedStyle(el).transitionDuration'), '0s')
        self.page.keyboard.press('Escape')
        self.assertEqual(self.page.evaluate('document.body.style.overflow'), 'auto')

    def test_lesson_morph_keeps_icons_and_reaches_both_anchors(self):
        self.go('lessons/Marugoto_A2_Lesson_1.html', 1440)
        self.page.wait_for_selector('#lessonSidebarRail', state='attached')
        self.page.emulate_media(reduced_motion='no-preference')
        self.page.evaluate("window.scrollTo({top: 400, behavior: 'instant'})")
        self.page.wait_for_function("document.body.classList.contains('is-morphing-to-dock')")
        samples = self.page.evaluate('''() => {
            const glider = document.getElementById('lessonMorphGlider');
            const animations = glider.getAnimations({subtree: true});
            animations.forEach(animation => animation.pause());
            const at = time => {
                animations.forEach(animation => { animation.currentTime = time; });
                const rect = glider.getBoundingClientRect();
                return {x: rect.x, y: rect.y, width: rect.width,
                    opacity: +getComputedStyle(glider.querySelector('.glider-layer-dock')).opacity};
            };
            const nav = document.querySelector('.section-nav').getBoundingClientRect();
            const dock = document.querySelector('#lessonSidebarRail .macos-sidebar-box').getBoundingClientRect();
            const result = {nav: {x: nav.x, y: nav.y}, dock: {x: dock.x, y: dock.y},
                start: at(0), middle: at(180), end: at(399), inert: glider.inert,
                iconHeight: glider.querySelector('.lesson-rail-link').getBoundingClientRect().height};
            animations.forEach(animation => animation.play());
            return result;
        }''')
        self.assertAlmostEqual(samples['start']['x'], samples['nav']['x'], delta=1)
        self.assertAlmostEqual(samples['start']['y'], samples['nav']['y'], delta=1)
        self.assertAlmostEqual(samples['end']['x'], samples['dock']['x'], delta=1)
        self.assertAlmostEqual(samples['end']['y'], samples['dock']['y'], delta=1)
        self.assertGreater(samples['middle']['opacity'], 0.5)
        self.assertGreater(samples['iconHeight'], 40)
        self.assertTrue(samples['inert'])
        self.page.wait_for_function("!document.body.classList.contains('is-morphing-to-dock')")
        self.assertEqual(self.page.evaluate('lessonMorphGlider.getAnimations({subtree: true}).length'), 0)
        self.page.evaluate("window.scrollTo({top: 0, behavior: 'instant'})")
        self.page.wait_for_function("!document.body.classList.contains('is-scrolled-dock')")
        expect(self.page.locator('.section-nav')).to_be_visible()
        self.page.emulate_media(reduced_motion='reduce')
        self.page.evaluate("window.scrollTo({top: 400, behavior: 'instant'})")
        expect(self.page.locator('body')).to_have_class(re.compile(r'\bis-scrolled-dock\b'))
        self.assertEqual(self.page.evaluate('lessonMorphGlider.getAnimations({subtree: true}).length'), 0)

    def test_lesson_rail_supports_external_nav_and_flashcard_keyboard(self):
        for lesson in (1, 10, 11, 18):
            with self.subTest(lesson=lesson):
                self.go(f'lessons/Marugoto_A2_Lesson_{lesson}.html', 1440)
                self.page.wait_for_selector('#lessonSidebarRail', state='attached')
                self.page.locator('#sec-vocab').scroll_into_view_if_needed()
                self.page.locator('body').click(position={'x': 5, 'y': 5})
                self.page.keyboard.press('ArrowRight')
                expect(self.page.locator('#sec-vocab .flashcard.active-card')).to_have_count(1)
                card = self.page.locator('#sec-vocab .flashcard.active-card')
                was_flipped = 'flipped' in (card.get_attribute('class') or '').split()
                self.page.keyboard.press('Space')
                self.assertNotEqual('flipped' in (card.get_attribute('class') or '').split(), was_flipped)
        self.assertEqual(self.page_errors, [])

    def test_demo_lighting_reset_and_lantern_canvas_selection(self):
        self.go('demo_3d.html', 1440)
        self.page.wait_for_function('typeof renderer !== "undefined" && renderer?.info.render.calls > 0')
        night_color = self.page.evaluate('scene.background.getHex()')
        self.page.locator('#btnNightMode').click()
        self.assertNotEqual(self.page.evaluate('scene.background.getHex()'), night_color)
        self.page.locator('#btnNightMode').click()
        self.assertEqual(self.page.evaluate('scene.background.getHex()'), night_color)
        reset = self.page.locator('#bottomDock [onclick="resetView()"]')
        self.page.locator('#btnCinematic').click()
        reset.click()
        self.assertFalse(self.page.evaluate('isCinematic || isTransitioning'))
        self.page.locator('#pill-lantern').click()
        reset.click()
        self.assertFalse(self.page.evaluate('isCinematic || isTransitioning'))
        distance = self.page.evaluate('''async () => {
            const before = camera.position.clone();
            for (let i = 0; i < 5; i++) await new Promise(resolve => requestAnimationFrame(resolve));
            return before.distanceTo(camera.position);
        }''')
        self.assertLess(distance, 0.001)
        point = self.page.evaluate('''() => {
            const position = new THREE.Vector3(0, 2.32, 0);
            models.lanterns[0].localToWorld(position).project(camera);
            return {x: (position.x + 1) * innerWidth / 2, y: (1 - position.y) * innerHeight / 2};
        }''')
        self.page.mouse.click(point['x'], point['y'])
        expect(self.page.locator('#cardKanji')).to_have_text('燈籠')
        expect(self.page.locator('#vocabModal')).to_be_visible()
        self.assertEqual(self.page_errors, [])

    def test_out_of_order_svg_cannot_overwrite_new_filtered_character(self):
        old_path, new_path = "M10 10 L90 90", "M90 10 L10 90"
        for width in WIDTHS:
            with self.subTest(width=width):
                pending = []
                self.page.route(SVG_PATTERN, lambda route: pending.append(route))
                self.go("kanji_a2.html", width)
                chars = self.page.evaluate("[kanjiData[0].char, kanjiData[1].char]")
                self.page.locator("#searchInput").fill(chars[0])
                expect(self.page.locator("#tabCountCards")).to_have_text("1")
                self.page.locator("#btnViewCards").click()
                card = self.page.locator("#cardsContainer .kanji-card").first
                card.scroll_into_view_if_needed()
                self.page.wait_for_function("() => kanjiPlayers[0]?.char === filteredKanji[0].char")
                old_hex = f"{ord(chars[0]):05x}.svg"
                new_hex = f"{ord(chars[1]):05x}.svg"

                def pending_for(filename):
                    return next((route for route in pending
                                 if urlparse(route.request.url).path.endswith('/' + filename)), None)

                # A browser round trip pumps route callbacks without fixed sleeps.
                with self.page.expect_request(lambda request: request.url.endswith(new_hex)):
                    self.page.locator("#searchInput").fill(chars[1])
                    expect(self.page.locator("#tabCountCards")).to_have_text("1")
                    self.page.locator("#cardsContainer .kanji-card").first.scroll_into_view_if_needed()
                self.page.wait_for_function("() => kanjiPlayers[0]?.char === filteredKanji[0].char")
                self.assertIsNotNone(pending_for(old_hex), "Old SVG fetch must still be in flight")
                self.assertIsNotNone(pending_for(new_hex), "New filtered SVG must be requested")
                pending_for(new_hex).fulfill(status=200, content_type="image/svg+xml",
                                            headers={"Access-Control-Allow-Origin": "*"},
                                            body=stroke_svg(new_path))
                active = self.page.locator("#kanji-svg-container-0 .active-strokes path")
                expect(active).to_have_attribute("d", new_path)
                old_response = pending_for(old_hex)
                # Wait for the stale fetch continuation, not merely route.fulfill().
                old_response.fulfill(status=200, content_type="image/svg+xml",
                                     headers={"Access-Control-Allow-Origin": "*"},
                                     body=stroke_svg(old_path))
                self.page.wait_for_function("char => svgCache.has(char)", arg=chars[0])
                self.page.evaluate("() => new Promise(resolve => requestAnimationFrame(() => resolve()))")
                expect(active).to_have_attribute("d", new_path)
                expect(self.page.locator(".kanji-badge")).to_have_text(chars[1])
                self.assertEqual(self.page.evaluate("kanjiPlayers[0].char"), chars[1])
                self.assertEqual(self.page.locator("#kanji-svg-container-0 svg").count(), 1)
                self.page.unroute(SVG_PATTERN)


if __name__ == "__main__":
    unittest.main(verbosity=2)
