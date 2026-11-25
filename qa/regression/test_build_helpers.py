"""Focused build-helper regressions; every generated file stays in a temp workspace."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dontwritebytecode = True
ROOT = Path(__file__).resolve().parents[2]


def load_append_helper():
    spec = importlib.util.spec_from_file_location(
        "review_append_kanji", ROOT / "scripts/append_a2_2_kanji.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def runtime_items(path):
    source = path.read_text(encoding="utf-8")
    return json.loads(re.search(r"var VOCAB_121_DATA = (\[.*?\]);", source)[1])


class BuildHelpersTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="marugoto helpers ")
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        for name in ("data/kanji_vocab_a2_2.json", "assets/data/kanji_a2_data.js", "kanji_a2.html"):
            dest = self.workspace / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, dest)
        self.helper = load_append_helper()
        self.root_patch = patch.object(self.helper, "ROOT", self.workspace)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def sync(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.helper.update_kanji_data_js()
            self.helper.update_kanji_html()

    def test_append_keeps_all_18_lessons_and_a2_1_and_is_idempotent(self):
        path = self.workspace / "assets/data/kanji_a2_data.js"
        original = runtime_items(path)
        self.sync()
        updated = runtime_items(path)
        non_a2_2 = lambda items: [item for item in items if not str(item["lesson"]).startswith("A2-2")]
        self.assertEqual(non_a2_2(original), non_a2_2(updated))
        source = json.loads((self.workspace / "data/kanji_vocab_a2_2.json").read_text(encoding="utf-8"))
        expected = [(f"A2-2 L{number}", item["word"], item["kana"], item["mean"])
                    for number in range(1, 19) for item in source[f"lesson_{number}"]]
        actual = [(item["lesson"], item["kanji"], item["kana"], item["vi"])
                  for item in updated if str(item["lesson"]).startswith("A2-2")]
        self.assertEqual(expected, actual)
        self.assertEqual(len(expected), 181)
        snapshots = {name: (self.workspace / name).read_bytes()
                     for name in ("assets/data/kanji_a2_data.js", "kanji_a2.html")}
        self.sync()
        for name, snapshot in snapshots.items():
            self.assertEqual((self.workspace / name).read_bytes(), snapshot)

    def test_incomplete_source_does_not_truncate_runtime(self):
        path = self.workspace / "data/kanji_vocab_a2_2.json"
        source = json.loads(path.read_text(encoding="utf-8"))
        del source["lesson_18"]
        path.write_text(json.dumps(source), encoding="utf-8")
        runtime = self.workspace / "assets/data/kanji_a2_data.js"
        before = runtime.read_bytes()
        with self.assertRaises(KeyError):
            self.helper.update_kanji_data_js()
        self.assertEqual(runtime.read_bytes(), before)

    def test_html_counts_follow_full_source(self):
        path = self.workspace / "kanji_a2.html"
        html = path.read_text(encoding="utf-8")
        html = re.sub(r"\(\d+\)", "(0)", html)
        html = html.replace("302 Mục Từ Kanji", "0 Mục Từ Kanji")
        html = html.replace("181 mục Kanji A2-2", "0 mục Kanji A2-2")
        path.write_text(html, encoding="utf-8")
        self.sync()
        html = path.read_text(encoding="utf-8")
        self.assertIn("302 Mục Từ Kanji", html)
        self.assertIn("Tất Cả (302)", html)
        self.assertIn("Trọn Bộ A2-2 (181)", html)
        self.assertIn("181 mục Kanji A2-2 bài 1–18.", html)
        source = json.loads((self.workspace / "data/kanji_vocab_a2_2.json").read_text(encoding="utf-8"))
        for number in range(1, 19):
            self.assertIn(f"Bài {number} ({len(source[f'lesson_{number}'])})</button>", html)

    def test_legacy_cli_and_main_delegate_from_unrelated_cwd(self):
        script = self.workspace / "scripts/build_a2_2_lessons.py"
        script.parent.mkdir()
        shutil.copyfile(ROOT / "scripts/build_a2_2_lessons.py", script)
        builder = self.workspace / "scripts/a2_2/build_all_a2_2.py"
        builder.parent.mkdir()
        # Stub only the canonical builder; execute the actual compatibility entry
        # point without invoking generators or relying on PYTHONPATH/cwd.
        builder.write_text(
            'from pathlib import Path\n'
            'def main():\n'
            '    path = Path(__file__).resolve().parents[2] / "canonical-called.txt"\n'
            '    path.write_text("all 18 lessons", encoding="utf-8")\n', encoding="utf-8")
        cwd = self.workspace / "unrelated cwd"
        cwd.mkdir()
        env = dict(os.environ)
        env.pop("PYTHONPATH", None)
        commands = [
            [sys.executable, "-B", str(script)],
            [sys.executable, "-B", "-c",
             'import runpy, sys; runpy.run_path(sys.argv[1])["main"]()', str(script)],
        ]
        marker = self.workspace / "canonical-called.txt"
        for command in commands:
            with self.subTest(command=command):
                subprocess.run(command, cwd=cwd, env=env, check=True,
                               capture_output=True, text=True, timeout=30)
                self.assertEqual(marker.read_text(encoding="utf-8"), "all 18 lessons")
                marker.unlink()


if __name__ == "__main__":
    unittest.main()
