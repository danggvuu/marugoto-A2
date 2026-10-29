import fitz
import re
import json

doc = fitz.open('/tmp/marugoto_vocab.pdf')

lessons = {}

# Page 1-24: A1
# Page 25-46: A2
current_level = "A1"
current_lesson_key = "A1_LESSON_3"

for page_idx in range(len(doc)):
    page_num = page_idx + 1
    if page_num >= 25:
        current_level = "A2"
    
    text = doc[page_idx].get_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check for LESSON header
        m_head = re.match(r'LESSON\s+([0-9０-９]+)', line, re.IGNORECASE)
        if m_head:
            num = m_head.group(1).translate(str.maketrans('０１２３４５６７８９', '0123456789'))
            current_lesson_key = f"{current_level}_LESSON_{num}"
            if current_lesson_key not in lessons:
                lessons[current_lesson_key] = []
            i += 1
            continue
        
        # Check for number
        m_num = re.match(r'^([0-9]+)\.?$', line)
        if m_num and current_lesson_key:
            item_no = int(m_num.group(1))
            word = ""
            meaning = ""
            
            # next line could be word
            if i + 1 < len(lines) and not re.match(r'^[0-9]+\.?$', lines[i+1]) and not re.match(r'LESSON\s+[0-9]', lines[i+1], re.I):
                word = lines[i+1]
                i += 1
            # next line could be meaning
            if i + 1 < len(lines) and not re.match(r'^[0-9]+\.?$', lines[i+1]) and not re.match(r'LESSON\s+[0-9]', lines[i+1], re.I):
                meaning = lines[i+1]
                i += 1
                # Check for continuation lines
                while i + 1 < len(lines):
                    next_l = lines[i+1]
                    if re.match(r'^[0-9]+\.?$', next_l) or re.match(r'LESSON\s+[0-9]', next_l, re.I) or next_l in ['No.', 'Từ vựng', 'Ý nghĩa']:
                        break
                    # If line looks like a continuation of meaning
                    meaning += ' ' + next_l
                    i += 1
            
            if word and word not in ['No.', 'Từ vựng', 'Ý nghĩa']:
                if current_lesson_key not in lessons:
                    lessons[current_lesson_key] = []
                lessons[current_lesson_key].append({
                    'no': item_no,
                    'word': word,
                    'meaning': meaning
                })
        i += 1

print(f"Total lessons: {len(lessons)}")
for k, v in sorted(lessons.items()):
    if v:
        print(f"{k}: {len(v)} words. Sample: {v[0]['word']} -> {v[0]['meaning']}")
    else:
        print(f"{k}: 0 words")

with open('/tmp/padlet_vocab_a1_a2.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

