#!/usr/bin/env python3
"""
build_all.py
One-command build & integrity verification for the Marugoto A1-A2 Review Hub.
1. Runs all active page generators cleanly with -W error semantics.
2. Verifies balanced <script> tags, missing local asset href/src references,
   and `node --check` syntax across all JavaScript files.
"""

import glob
import os
import re
import subprocess
import sys

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILDERS = [
    "scripts/build_mini_test_15_18.py",
    "scripts/build_mini_test_11_14.py",
    "scripts/build_cram_kanji_11_18.py",
]


def run_builders():
    for rel in BUILDERS:
        full = os.path.join(WORKSPACE, rel)
        print(f"Running {rel}...")
        subprocess.run([sys.executable, "-W", "error", full], check=True)


def verify_html_integrity():
    html_files = sorted(
        glob.glob(os.path.join(WORKSPACE, "*.html"))
        + glob.glob(os.path.join(WORKSPACE, "lessons/*.html"))
        + glob.glob(os.path.join(WORKSPACE, "tests/*.html"))
    )
    errors = []
    for path in html_files:
        rel_html = os.path.relpath(path, WORKSPACE)
        html_dir = os.path.dirname(path)
        s = open(path, encoding="utf-8").read()

        opens = len(re.findall(r"<script(?:\s|>)", s))
        closes = len(re.findall(r"</script>", s))
        if opens != closes:
            errors.append(f"{rel_html}: unbalanced <script> ({opens} open vs {closes} close)")

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
    js_files = sorted(
        glob.glob(os.path.join(WORKSPACE, "assets/*.js"))
        + glob.glob(os.path.join(WORKSPACE, "assets/js/*.js"))
        + glob.glob(os.path.join(WORKSPACE, "assets/js/lessons/*.js"))
        + glob.glob(os.path.join(WORKSPACE, "assets/js/pages/*.js"))
        + glob.glob(os.path.join(WORKSPACE, "assets/data/*.js"))
    )
    for js_path in js_files:
        subprocess.run(["node", "--check", js_path], check=True)
    print(f"Node JS syntax check OK across {len(js_files)} JS files.")


if __name__ == "__main__":
    run_builders()
    verify_html_integrity()
    verify_all_js()
    print("ALL BUILD & INTEGRITY CHECKS PASSED!")
