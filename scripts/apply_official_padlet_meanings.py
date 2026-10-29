import json
import re
import glob

# Load extracted Padlet dictionary
with open('/tmp/padlet_vocab_complete.json') as f:
    padlet_data = json.load(f)

# Add Lesson 15 and Lesson 17 manually transcribed from PDF images
padlet_data['A2_LESSON_15'] = [
    {'no': 1, 'word': 'あたま', 'meaning': 'Đầu'},
    {'no': 2, 'word': 'かお', 'meaning': 'Khuôn mặt'},
    {'no': 3, 'word': 'め', 'meaning': 'Mắt'},
    {'no': 4, 'word': 'はな', 'meaning': 'Mũi'},
    {'no': 5, 'word': 'くち', 'meaning': 'Miệng'},
    {'no': 6, 'word': 'は', 'meaning': 'Răng'},
    {'no': 7, 'word': 'みみ', 'meaning': 'Tai'},
    {'no': 8, 'word': 'かみ', 'meaning': 'Tóc'},
    {'no': 9, 'word': 'からだ', 'meaning': 'Cơ thể'},
    {'no': 10, 'word': 'くび', 'meaning': 'Cổ'},
    {'no': 11, 'word': 'かた', 'meaning': 'Vai'},
    {'no': 12, 'word': 'むね', 'meaning': 'Ngực'},
    {'no': 13, 'word': 'おなか', 'meaning': 'Bụng'},
    {'no': 14, 'word': 'せなか', 'meaning': 'Lưng'},
    {'no': 15, 'word': 'こし', 'meaning': 'Eo, lưng dưới'},
    {'no': 16, 'word': 'て', 'meaning': 'Bàn tay'},
    {'no': 17, 'word': 'うで', 'meaning': 'Cánh tay'},
    {'no': 18, 'word': 'ゆび', 'meaning': 'Ngón...'},
    {'no': 19, 'word': 'あし', 'meaning': 'Chân'},
    {'no': 20, 'word': 'ちょうし', 'meaning': 'Tình trạng'},
    {'no': 21, 'word': 'たいちょう', 'meaning': 'Tình trạng cơ thể'},
    {'no': 22, 'word': '～が いたい', 'meaning': '～đau'},
    {'no': 23, 'word': 'きもちが いい', 'meaning': 'Tâm trạng tốt'},
    {'no': 24, 'word': 'たいちょうが いい', 'meaning': 'Tình trạng sức khỏe tốt'},
    {'no': 25, 'word': 'たいちょうが わるい', 'meaning': 'Tình trạng sức khỏe xấu'},
    {'no': 26, 'word': 'ねられません', 'meaning': 'Không ngủ được'},
    {'no': 27, 'word': 'つかれます', 'meaning': 'Mệt mỏi'},
    {'no': 28, 'word': 'うでを あげます', 'meaning': 'Nâng cánh tay'},
    {'no': 29, 'word': 'かたを まわします', 'meaning': 'Xoay vai'},
    {'no': 30, 'word': 'くびを まげます', 'meaning': 'Bẻ cổ'},
    {'no': 31, 'word': 'いきを すいます', 'meaning': 'Hít vào'},
    {'no': 32, 'word': 'いきを はきます', 'meaning': 'Thở ra'},
    {'no': 33, 'word': 'しんこきゅう', 'meaning': 'Hít thở sâu'},
    {'no': 34, 'word': 'けんこう', 'meaning': 'Sức khỏe'},
    {'no': 35, 'word': 'たいそう', 'meaning': 'Tập thể dục'},
    {'no': 36, 'word': 'アドバイス', 'meaning': 'Lời khuyên'},
    {'no': 37, 'word': 'ストレス', 'meaning': 'Stress, căng thẳng'},
    {'no': 38, 'word': 'さいきん', 'meaning': 'Gần đây'},
    {'no': 39, 'word': 'きゅうに', 'meaning': 'Đột ngột'},
    {'no': 40, 'word': 'こうやって', 'meaning': 'Làm như thế này'},
    {'no': 41, 'word': 'まず', 'meaning': 'Đầu tiên'},
    {'no': 42, 'word': 'つぎ（に）', 'meaning': 'Tiếp theo'},
    {'no': 43, 'word': 'さいご（に）', 'meaning': 'Cuối cùng'},
    {'no': 44, 'word': 'けんこうだいいち', 'meaning': 'Sức khỏe là số 1'},
    {'no': 45, 'word': 'Nを おします', 'meaning': 'Bấm N'},
    {'no': 46, 'word': 'ツボ', 'meaning': 'Huyệt'},
    {'no': 47, 'word': 'マッサージ', 'meaning': 'Mát xa'},
    {'no': 48, 'word': 'リラックス', 'meaning': 'Thư giãn (Relax)'},
    {'no': 49, 'word': 'エレベーター', 'meaning': 'Cầu thang máy'},
    {'no': 50, 'word': 'ブルーベリー', 'meaning': 'Quả việt quất'},
    {'no': 51, 'word': 'ねむい', 'meaning': 'Buồn ngủ'},
    {'no': 52, 'word': 'ねつが あります', 'meaning': 'Sốt'},
    {'no': 53, 'word': 'かぜ（を ひきます）', 'meaning': 'Bị cảm'},
    {'no': 54, 'word': 'むりを します', 'meaning': 'Làm quá sức'},
    {'no': 55, 'word': 'どうしたんですか。', 'meaning': 'Bạn bị sao vậy? (hỏi thăm)'},
    {'no': 56, 'word': 'くすり', 'meaning': 'Thuốc'},
    {'no': 57, 'word': 'できるだけ', 'meaning': 'Càng... càng tốt, trong phạm vi có thể'}
]

padlet_data['A2_LESSON_17'] = [
    {'no': 1, 'word': 'おいわい', 'meaning': 'Chúc mừng'},
    {'no': 2, 'word': 'にゅうがく', 'meaning': 'Nhập học'},
    {'no': 3, 'word': 'そつぎょう', 'meaning': 'Tốt nghiệp'},
    {'no': 4, 'word': 'しゅうしょく', 'meaning': 'Bắt đầu đi làm'},
    {'no': 5, 'word': 'しゅっさん', 'meaning': 'Sinh con'},
    {'no': 6, 'word': 'あかちゃん', 'meaning': 'Em bé'},
    {'no': 7, 'word': 'うまれます', 'meaning': 'Được sinh ra'},
    {'no': 8, 'word': 'けっこん', 'meaning': 'Kết hôn'},
    {'no': 9, 'word': 'ははの ひ', 'meaning': 'Ngày của mẹ (Chủ nhật thứ 2 của tháng 5)'},
    {'no': 10, 'word': 'ちちの ひ', 'meaning': 'Ngày của bố (Chủ nhật thứ 3 của tháng 6)'},
    {'no': 11, 'word': 'クリスマス', 'meaning': 'Giáng sinh'},
    {'no': 12, 'word': 'バレンタイン・デー', 'meaning': 'Ngày Valentine'},
    {'no': 13, 'word': 'ネックレス', 'meaning': 'Vòng cổ'},
    {'no': 14, 'word': 'セーター', 'meaning': 'Áo len'},
    {'no': 15, 'word': 'おもちゃ', 'meaning': 'Đồ chơi'},
    {'no': 16, 'word': 'あみもの', 'meaning': 'Đồ đan len'},
    {'no': 17, 'word': 'にんぎょう', 'meaning': 'Búp bê'},
    {'no': 18, 'word': '（シャツを）きます', 'meaning': 'Mặc (áo)'},
    {'no': 19, 'word': 'へやに かざります', 'meaning': 'Trang trí trong phòng'},
    {'no': 20, 'word': 'しごとで つかいます', 'meaning': 'Sử dụng trong công việc'},
    {'no': 21, 'word': 'にあいます', 'meaning': '~ hợp'},
    {'no': 22, 'word': 'あそびます', 'meaning': 'Chơi'},
    {'no': 23, 'word': 'きに いります', 'meaning': 'Thích'},
    {'no': 24, 'word': '～とか～とか', 'meaning': 'Chẳng hạn như ~ như ~'},
    {'no': 25, 'word': 'めいしいれ', 'meaning': 'Hộp đựng danh thiếp'},
    {'no': 26, 'word': 'ペア', 'meaning': 'Cặp, đôi'},
    {'no': 27, 'word': 'おなじ', 'meaning': 'Giống'},
    {'no': 28, 'word': 'たとえば', 'meaning': 'Ví dụ'},
    {'no': 29, 'word': 'しゅうかん', 'meaning': 'Thói quen'}
]

# Clean specific items
for x in padlet_data.get('A2_LESSON_5', []):
    if x['no'] == 31:
        x['word'] = 'ぜひ～てください'
        x['meaning'] = 'Nhất định hãy...'

for x in padlet_data.get('A2_LESSON_18', []):
    if x['no'] == 9:
        x['word'] = 'あかちゃんの ものが ひつようです'
        x['meaning'] = 'Đồ dùng của em bé là cần thiết'

# Save complete padlet dict
with open('/tmp/padlet_vocab_complete.json', 'w', encoding='utf-8') as f:
    json.dump(padlet_data, f, ensure_ascii=False, indent=2)

def update_html_lesson(lesson_num):
    fn = f'lessons/Marugoto_A2_Lesson_{lesson_num}.html'
    key = f'A2_LESSON_{lesson_num}'
    if key not in padlet_data:
        print(f"Skipping {fn}: not in padlet_data")
        return

    padlet_list = padlet_data[key]
    padlet_map = {item['no']: item['meaning'] for item in padlet_list}

    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    m = re.search(r'const VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)
    if not m:
        m = re.search(r'var VOCAB_DATA\s*=\s*(\[.*?\]);', c, flags=re.DOTALL)
    if not m:
        print(f"No VOCAB_DATA in {fn}")
        return

    data = json.loads(m.group(1))
    updated_count = 0
    for it in data:
        item_id = it.get('id')
        if item_id in padlet_map:
            official_vi = padlet_map[item_id]
            # Update vi
            it['vi'] = official_vi
            updated_count += 1

    new_json = json.dumps(data, ensure_ascii=False)
    c = c[:m.start(1)] + new_json + c[m.end(1):]

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"[{fn}] Updated {updated_count} words with official Padlet meanings!")

for l in range(10, 19):
    update_html_lesson(l)

