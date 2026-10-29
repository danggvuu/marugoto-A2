import fitz
import re
import json

doc = fitz.open('/tmp/marugoto_vocab.pdf')

full_text = ''
for i, page in enumerate(doc):
    full_text += f'\n<<<PAGE_{i+1}>>>\n' + page.get_text()

# Split by LESSON
chunks = re.split(r'(LESSON\s+[0-9０-９]+[^<\n]*)', full_text, flags=re.IGNORECASE)

lessons_parsed = {}
current_lesson_title = "INTRO"

for chunk in chunks:
    m_head = re.match(r'LESSON\s+([0-9０-９]+)[・\s\.\-]*(.*)', chunk.strip(), re.IGNORECASE)
    if m_head:
        num = m_head.group(1)
        # convert fullwidth to halfwidth
        num = num.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
        title = m_head.group(2).strip()
        current_lesson_title = f"LESSON {num}"
        continue

    # Parse entries in chunk
    # Looking for:
    # 1. \n word \n meaning
    # or number. \n word \n meaning
    lines = [l.strip() for l in chunk.split('\n') if l.strip()]
    
    # Filter out page markers and table headers
    filtered_lines = []
    for l in lines:
        if l.startswith('<<<PAGE_') or l in ['No.', 'Từ vựng', 'Ý nghĩa']:
            continue
        filtered_lines.append(l)

    entries = []
    i = 0
    while i < len(filtered_lines):
        m_num = re.match(r'^([0-9]+)\.?$', filtered_lines[i])
        if m_num:
            item_no = int(m_num.group(1))
            word = ""
            meaning = ""
            if i + 1 < len(filtered_lines) and not re.match(r'^[0-9]+\.?$', filtered_lines[i+1]):
                word = filtered_lines[i+1]
                i += 1
            if i + 1 < len(filtered_lines) and not re.match(r'^[0-9]+\.?$', filtered_lines[i+1]):
                meaning = filtered_lines[i+1]
                i += 1
                # If meaning continues onto next line before next number
                while i + 1 < len(filtered_lines) and not re.match(r'^[0-9]+\.?$', filtered_lines[i+1]):
                    # Check if next line looks like a separate word or continuation
                    if re.match(r'^[A-Z0-9]', filtered_lines[i+1]) or 'LESSON' in filtered_lines[i+1]:
                        break
                    meaning += ' ' + filtered_lines[i+1]
                    i += 1
            entries.append({'no': item_no, 'word': word, 'meaning': meaning})
        i += 1

    if entries:
        if current_lesson_title not in lessons_parsed:
            lessons_parsed[current_lesson_title] = []
        lessons_parsed[current_lesson_title].extend(entries)

print(f"Total lesson sections parsed: {len(lessons_parsed)}")
for l_title, items in lessons_parsed.items():
    print(f"{l_title}: {len(items)} items. Sample: {items[0] if items else ''}")

with open('/tmp/padlet_vocab_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(lessons_parsed, f, ensure_ascii=False, indent=2)

