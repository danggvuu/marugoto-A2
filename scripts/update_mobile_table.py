# -*- coding: utf-8 -*-
with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update mobile CSS
old_mobile_col = '''.col-stt {
                display: none !important;
            }

            .col-lesson {
                width: 62px !important;
                padding: 10px 4px !important;
                text-align: center;
            }

            .col-jp {
                width: 46% !important;
                padding: 10px 8px !important;
            }'''

new_mobile_col = '''.col-stt {
                display: none !important;
            }

            .col-lesson {
                width: 56px !important;
                padding: 8px 2px !important;
                text-align: center;
                font-size: 0.75rem !important;
            }

            .col-kanji {
                width: 34% !important;
                padding: 8px 4px !important;
                font-size: 0.98rem !important;
            }

            .col-kana, .col-hv {
                display: none !important;
            }

            .col-vi {
                width: auto !important;
                padding: 8px 6px !important;
                font-size: 0.85rem !important;
            }

            .col-actions {
                width: 76px !important;
                padding: 8px 2px !important;
            }

            .sub-kana-mobile {
                display: block !important;
                font-size: 0.72rem;
                color: #64748b;
                margin-top: 2px;
                line-height: 1.2;
            }
            .badge-hv-mobile {
                display: inline-block;
                font-size: 0.68rem;
                font-weight: 700;
                color: #0284c7;
            }'''

if old_mobile_col in text:
    text = text.replace(old_mobile_col, new_mobile_col)
    print('Updated mobile column CSS!')

desktop_rule = '''
    .sub-kana-mobile {
        display: none;
    }
'''
if '.sub-kana-mobile {' not in text:
    text = text.replace('</style>', f'{desktop_rule}\n</style>', 1)

old_render_kanji = '''                    <td class="col-kanji">
                        <span class="kanji-word ${hasKanji ? 'clickable-kanji' : ''}" onclick="event.stopPropagation(); ${hasKanji ? `openStrokeModel(${idx})` : ''}" title="${hasKanji ? 'Click để xem chuyển động nét Kanji' : ''}">
                            ${item.kanji}
                        </span>
                    </td>'''

new_render_kanji = '''                    <td class="col-kanji">
                        <span class="kanji-word ${hasKanji ? 'clickable-kanji' : ''}" onclick="event.stopPropagation(); ${hasKanji ? `openStrokeModel(${idx})` : ''}" title="${hasKanji ? 'Click để xem chuyển động nét Kanji' : ''}">
                            ${item.kanji}
                        </span>
                        <div class="sub-kana-mobile">${item.kana !== item.kanji ? item.kana : ''} ${item.hv ? `<span class="badge-hv-mobile">${item.hv}</span>` : ''}</div>
                    </td>'''

if old_render_kanji in text:
    text = text.replace(old_render_kanji, new_render_kanji)
    print('Updated renderTable with sub-kana-mobile!')

with open('Tu_Vung_Marugoto_A1_16_A2_1_10.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
