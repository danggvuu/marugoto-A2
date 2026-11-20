# -*- coding: utf-8 -*-
"""
Generate official Marugoto A2-2 vocabulary dataset from authentic PDF curriculum
(439 items total across 18 lessons) and sync all topic files (topic_02.py through topic_09.py).
"""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.a2_2.build_full_439_vocab import FULL_OFFICIAL_VOCAB

OFFICIAL_VOCAB = FULL_OFFICIAL_VOCAB


def sync_to_data_file():
    data_path = ROOT / "data/vocab_a2_2_official.json"
    formatted = {f"lesson_{num}": items for num, items in OFFICIAL_VOCAB.items()}
    data_path.write_text(json.dumps(formatted, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {data_path} with all 18 lessons ({sum(len(v) for v in OFFICIAL_VOCAB.values())} total items)!")


def replace_vocab_in_topic(topic_num):
    topic_file = ROOT / f"scripts/a2_2/topic_{topic_num:02d}.py"
    if not topic_file.exists():
        print(f"Skip {topic_file} (not found)")
        return

    content = topic_file.read_text(encoding="utf-8")
    la = topic_num * 2 - 1
    lb = topic_num * 2

    # Replace L{la}_VOCAB = [ ... ]
    vocab_a_code = f"L{la}_VOCAB = " + json.dumps(OFFICIAL_VOCAB[la], ensure_ascii=False, indent=4)
    pattern_a = rf"L{la}_VOCAB\s*=\s*\[.*?\]\n"
    content, count_a = re.subn(pattern_a, vocab_a_code + "\n", content, flags=re.S)

    # Replace L{lb}_VOCAB = [ ... ]
    vocab_b_code = f"L{lb}_VOCAB = " + json.dumps(OFFICIAL_VOCAB[lb], ensure_ascii=False, indent=4)
    pattern_b = rf"L{lb}_VOCAB\s*=\s*\[.*?\]\n"
    content, count_b = re.subn(pattern_b, vocab_b_code + "\n", content, flags=re.S)

    if count_a == 1 and count_b == 1:
        topic_file.write_text(content, encoding="utf-8")
        print(f"Updated {topic_file.name}: L{la} ({len(OFFICIAL_VOCAB[la])} items), L{lb} ({len(OFFICIAL_VOCAB[lb])} items)")
    else:
        print(f"Warning: count_a={count_a}, count_b={count_b} for {topic_file.name}")


def main():
    sync_to_data_file()
    for t in range(2, 10):
        replace_vocab_in_topic(t)


if __name__ == "__main__":
    main()
