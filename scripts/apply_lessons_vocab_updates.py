# -*- coding: utf-8 -*-
import json
import re
import os
import subprocess

from generate_all_lesson_vocab import (
    vocab_11, vocab_12, vocab_13, vocab_14,
    vocab_15, vocab_16, vocab_17, vocab_18
)

lesson_vocab_map = {
    12: vocab_12,
    13: vocab_13,
    14: vocab_14,
    15: vocab_15,
    16: vocab_16,
    17: vocab_17,
    18: vocab_18
}

# 1. Update data_lesson_12.py through data_lesson_18.py
for num, vocab in lesson_vocab_map.items():
    fname = f"data_lesson_{num}.py"
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    v_idx = content.find('"vocab": [')
    vl_idx = content.find('"verb_lab":')
    if v_idx != -1 and vl_idx != -1:
        vocab_json_str = '"vocab": ' + json.dumps(vocab, ensure_ascii=False, indent=8) + ',\n\n    '
        new_content = content[:v_idx] + vocab_json_str + content[vl_idx:]
        with open(fname, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {fname} with {len(vocab)} official items!")
    else:
        print(f"Error finding indices in {fname}!")

# 2. Update Marugoto_A2_Lesson_11.html
with open("Marugoto_A2_Lesson_11.html", "r", encoding="utf-8") as f:
    l11_html = f.read()

v11_start = l11_html.find("const VOCAB_DATA = [")
v11_end = l11_html.find("const VERB_MORPH_DATA = [")
if v11_start != -1 and v11_end != -1:
    new_v11_str = "const VOCAB_DATA = " + json.dumps(vocab_11, ensure_ascii=False) + ";\n        "
    l11_html = l11_html[:v11_start] + new_v11_str + l11_html[v11_end:]
    
    # Update count labels in HTML
    l11_html = re.sub(r'28 Từ Vựng', '27 Từ Vựng', l11_html)
    l11_html = re.sub(r'Tất cả \(28\)', 'Tất cả (27)', l11_html)
    l11_html = re.sub(r'Đã thuộc: 0 / 28', 'Đã thuộc: 0 / 27', l11_html)
    l11_html = l11_html.replace(
        '<div class="stat-number">28</div>',
        '<div class="stat-number">27</div>'
    )

    with open("Marugoto_A2_Lesson_11.html", "w", encoding="utf-8") as f:
        f.write(l11_html)
    print("Updated Marugoto_A2_Lesson_11.html with 27 official items!")
else:
    print("Error finding VOCAB_DATA in Marugoto_A2_Lesson_11.html!")

# 3. Regenerate Lessons 12 to 18
print("Regenerating Lessons 12 to 18 HTML files...")
subprocess.run(["python3", "build_all_lessons_12_to_18.py"], check=True)

# 4. Synchronize clean navigation
print("Synchronizing clean navigation across all files...")
subprocess.run(["python3", "sync_clean_navigation.py"], check=True)

print("ALL LESSON VOCABULARIES UPDATED & SYNCHRONIZED SUCCESSFULLY!")
