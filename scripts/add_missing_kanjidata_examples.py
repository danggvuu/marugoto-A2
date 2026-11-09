import json
import re

def main():
    with open('kanji_a2.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Dictionary of char -> list of example dicts to append if not already present
    additions = {
        '料': [
            {'word': '資料', 'reading': 'しりょう', 'vi': 'Tài liệu, dữ liệu'}
        ],
        '味': [
            {'word': '地味', 'reading': 'じみ', 'vi': 'Giản dị, mộc mạc, đơn giản'}
        ],
        '出': [
            {'word': '出します', 'reading': 'だします', 'vi': 'Gửi đi, nộp bài, đưa ra'}
        ],
        '着': [
            {'word': '着物', 'reading': 'きもの', 'vi': 'Bộ trang phục kimono truyền thống'}
        ],
        '自': [
            {'word': '自然', 'reading': 'しぜん', 'vi': 'Tự nhiên, thiên nhiên'}
        ],
        '電': [
            {'word': '電子レンジ', 'reading': 'でんしレンジ', 'vi': 'Lò vi sóng'}
        ],
        '気': [
            {'word': '病気', 'reading': 'びょうき', 'vi': 'Bệnh tật, ốm đau'},
            {'word': '人気', 'reading': 'にんき', 'vi': 'Được yêu thích, ưa chuộng'}
        ],
        '体': [
            {'word': '全体', 'reading': 'ぜんたい', 'vi': 'Toàn bộ, tổng thể'}
        ],
        '手': [
            {'word': '歌手', 'reading': 'かしゅ', 'vi': 'Ca sĩ'},
            {'word': '運転手', 'reading': 'うんてんしゅ', 'vi': 'Tài xế, người lái xe'}
        ],
        '毎': [
            {'word': '毎月', 'reading': 'まいつき', 'vi': 'Mỗi tháng, hàng tháng'}
        ],
        '外': [
            {'word': '外食', 'reading': 'がいしょく', 'vi': 'Ăn ngoài tiệm, ăn tiệm'}
        ],
        '計': [
            {'word': '計ります', 'reading': 'はかります', 'vi': 'Cân đo, đo lường'},
            {'word': '会計', 'reading': 'かいけい', 'vi': 'Thanh toán, kế toán, tính tiền'}
        ],
        '作': [
            {'word': '作家', 'reading': 'さっか', 'vi': 'Tác giả, nhà văn'}
        ],
        '社': [
            {'word': '会社員', 'reading': 'かいしゃいん', 'vi': 'Nhân viên công ty'},
            {'word': '入社', 'reading': 'にゅうしゃ', 'vi': 'Vào làm ở công ty'},
            {'word': '神社', 'reading': 'じんじゃ', 'vi': 'Đền thờ Thần đạo'}
        ]
    }

    modified_count = 0
    for char, ex_list in additions.items():
        # Find the kanjiData entry for this char
        # e.g. char: "料"
        char_pattern = rf'(char:\s*\"{char}\".*?examples:\s*\[)(.*?)(\])'
        match = re.search(char_pattern, html, re.DOTALL)
        if match:
            existing_examples = match.group(2)
            new_ex_str = ""
            for ex in ex_list:
                if ex['word'] not in existing_examples:
                    new_ex_str += f',\n                {{ word: "{ex["word"]}", reading: "{ex["reading"]}", vi: "{ex["vi"]}" }}'
                    modified_count += 1
            if new_ex_str:
                replaced_block = match.group(1) + existing_examples + new_ex_str + "\n            " + match.group(3)
                html = html[:match.start()] + replaced_block + html[match.end():]
                print(f"Added {len(ex_list)} example(s) for char '{char}'")

    print(f"Total new examples injected: {modified_count}")
    with open('kanji_a2.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
