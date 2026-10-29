#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_expert_5_exams.py
Tập hợp trọn bộ 5 đề thi Midterm Marugoto A2-1 (M101 - M105)
Chuẩn Giáo viên Tiếng Nhật 10 năm kinh nghiệm - Nghiêm ngặt 100% 86 chữ Hán Bài 1 - 10.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from exam_m101_data import build_m101
from exam_m102_data import build_m102
from exam_m103_data import build_m103
from exam_m104_data import build_m104
from exam_m105_data import build_m105

EXAMS_DATA_EXPERT = [
    build_m101(),
    build_m102(),
    build_m103(),
    build_m104(),
    build_m105()
]

if __name__ == "__main__":
    print(f"Expert Exams Suite loaded: {len(EXAMS_DATA_EXPERT)} exams.")
    for e in EXAMS_DATA_EXPERT:
        total_q = sum(len(g.get("items", [])) for s in e["sections"] for g in s.get("groups", [])) + sum(len(s.get("items", [])) for s in e["sections"])
        print(f" - [{e['code']}] {e['name']}: {total_q} questions")
