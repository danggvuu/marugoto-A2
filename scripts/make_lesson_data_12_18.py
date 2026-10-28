# -*- coding: utf-8 -*-
"""
make_lesson_data_12_18.py
Generates the complete lesson_data_12_18.py containing comprehensive data
for Marugoto A2-2 Lessons 12 to 18.
"""

import json

def get_svg(title, emoji, color1="#059669", color2="#047857"):
    safe_id = "".join(c for c in title if c.isalnum()) or "icon"
    return (
        f'<svg viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg">'
        f'<defs><linearGradient id="g_{safe_id}" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0%" stop-color="{color1}"/><stop offset="100%" stop-color="{color2}"/>'
        f'</linearGradient></defs>'
        f'<rect width="240" height="120" rx="14" fill="url(#g_{safe_id})"/>'
        f'<circle cx="120" cy="50" r="30" fill="rgba(255,255,255,0.2)"/>'
        f'<text x="120" y="60" text-anchor="middle" font-size="34">{emoji}</text>'
        f'<text x="120" y="105" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800" font-family="system-ui, -apple-system, sans-serif">{title}</text>'
        f'</svg>'
    )

print("Helper defined.")
