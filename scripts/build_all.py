#!/usr/bin/env python3
"""
build_all.py
One-command build & integrity verification for the Marugoto A1-A2 Review Hub.
1. Runs all active page generators cleanly with -W error semantics.
2. Verifies balanced <script> tags, missing local asset href/src references,
   and `node --check` syntax across all JavaScript files.
"""

import argparse
import glob
import os
import re
import subprocess
import sys

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILDERS = [
    "scripts/build_lesson_content.py",
    "scripts/a2_2/build_all_a2_2.py",
    "scripts/build_mini_test_a2_2_1_4.py",
    "scripts/build_mini_test_15_18.py",
    "scripts/build_mini_test_11_14.py",
    "scripts/build_cram_kanji_11_18.py",
    "scripts/build_vocab_kanji_check_11_18.py",
    "scripts/build_full_exam_11_18_system.py",
    "scripts/build_tong_hop_11_18_page.py",
    "scripts/build_tong_hop_11_18_js.py",
]
REGRESSION_CHECKS = [
    ("Runtime regressions", ["node", "qa/regression/run_regression_tests.js"]),
    ("Content integrity", ["node", "qa/regression/content_integrity.js"]),
    ("Vocabulary Kanji scope", ["node", "qa/regression/vocab_kanji_scope.js"]),
    ("A2-2 content", ["node", "qa/regression/a2_2_content.js"]),
    ("Kaiwa scope", ["node", "qa/regression/kaiwa_scope.js"]),
    ("Review state recovery", ["node", "qa/regression/review_state_recovery.js"]),
    ("Review exam recovery", ["node", "qa/regression/review_exam_recovery.js"]),
    ("Review lesson fixes", ["node", "qa/regression/review_lesson_fixes.js", "--check-generated"]),
    ("Review 3D build lifecycle", ["node", "qa/regression/review_build_3d.js"]),
    ("Build helper regressions", [sys.executable, "-B", "qa/regression/test_build_helpers.py"]),
]


def run_builders():
    for rel in BUILDERS:
        full = os.path.join(WORKSPACE, rel)
        print(f"Running {rel}...")
        subprocess.run([sys.executable, "-B", "-W", "error", full], check=True, cwd=WORKSPACE)


def verify_html_integrity():
    html_files = sorted(
        glob.glob(os.path.join(WORKSPACE, "*.html"))
        + glob.glob(os.path.join(WORKSPACE, "lessons/*.html"))
        + glob.glob(os.path.join(WORKSPACE, "tests/*.html"))
        + glob.glob(os.path.join(WORKSPACE, "docs/Ke_Hoach_10_Ngay/**/*.html"), recursive=True)
    )
    errors = []
    for path in html_files:
        rel_html = os.path.relpath(path, WORKSPACE)
        html_dir = os.path.dirname(path)
        with open(path, encoding="utf-8") as source:
            s = source.read()

        opens = len(re.findall(r"<script(?:\s|>)", s))
        closes = len(re.findall(r"</script>", s))
        if opens != closes:
            errors.append(f"{rel_html}: unbalanced <script> ({opens} open vs {closes} close)")
        if len(re.findall(r"</html\s*>", s, re.I)) != 1:
            errors.append(f"{rel_html}: expected one HTML document")
        scripts = [url.split("?")[0] for url in re.findall(r'<script\b[^>]*\bsrc=["\']([^"\']+)', s, re.I)]
        if len(scripts) != len(set(scripts)):
            errors.append(f"{rel_html}: duplicate script imports")

        for attr in ("src", "href"):
            for m in re.finditer(rf'\b{attr}=["\']([^"\']+)["\']', s):
                target = m.group(1)
                if target.startswith(("http://", "https://", "#", "mailto:", "javascript:", "data:")):
                    continue
                target_clean = target.split("?")[0].split("#")[0]
                if not target_clean:
                    continue
                resolved = os.path.normpath(os.path.join(html_dir, target_clean))
                if not os.path.exists(resolved):
                    errors.append(f"{rel_html}: broken {attr}='{target}' (missing {os.path.relpath(resolved, WORKSPACE)})")

    if errors:
        raise AssertionError("HTML integrity check failed:\n  " + "\n  ".join(errors))
    print(f"HTML integrity OK across {len(html_files)} pages (0 broken links, balanced scripts).")


def verify_all_js():
    js_files = sorted(glob.glob(os.path.join(WORKSPACE, "assets/**/*.js"), recursive=True))
    for js_path in js_files:
        subprocess.run(["node", "--check", js_path], check=True)
    print(f"Node JS syntax check OK across {len(js_files)} JS files.")


def run_regression_checks():
    for name, command in REGRESSION_CHECKS:
        print(f"Running {name}...", flush=True)
        subprocess.run(command, check=True, cwd=WORKSPACE)


def main():
    parser = argparse.ArgumentParser(
        description="Build the site and run its integrity and regression checks."
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="run read-only integrity and regression checks without running generators",
    )
    args = parser.parse_args()

    if not args.check_only:
        run_builders()
    verify_html_integrity()
    verify_all_js()
    run_regression_checks()
    if args.check_only:
        print("ALL READ-ONLY QA CHECKS PASSED!")
    else:
        print("ALL BUILD & INTEGRITY CHECKS PASSED!")


if __name__ == "__main__":
    main()
