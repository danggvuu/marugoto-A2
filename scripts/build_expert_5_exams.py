#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_expert_5_exams.py
TỔNG HỢP 5 BỘ ĐỀ THI GIỮA KỲ MIDTERM MARUGOTO A2-1
ĐƯỢC BIÊN SOẠN BỞI GIÁO VIÊN TIẾNG NHẬT 10 NĂM KINH NGHIỆM
- Chuẩn format 5 phần bảng lớp học (36 câu = 100 điểm)
- Đúng chuẩn Can-do của The Japan Foundation (Marugoto A2-1)
- Bẫy ngữ pháp trợ từ, âm ngắt, âm dài, Hán tự tương đồng nét
- Bài đọc đời sống chân thực Nhật Bản
- Tự luận Can-do yêu cầu viết tối thiểu 50 từ/ký tự kèm rubric sư phạm
"""

import json
import os
import sys

def build_m101():
    return {
        "code": "M101",
        "name": "Mã Đề M101 (Đề Tổng Hợp Toàn Diện A2-1)",
        "tag": "📘 Tổng Hợp Bài 1 - 8 • Đề Khảo Sát Năng Lực",
        "desc": "Đề khảo sát năng lực toàn diện Marugoto A2-1 (Bài 1 - 8): Từ vựng đời sống, ngữ pháp trọng điểm, bẫy chữ Hán tương đồng và tự luận Can-do ≥ 50 từ/ký tự.",
        "timeLimit": 45 * 60,
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": "毎朝、(   ) を かけてから、学校へ 行きます。",
                                "promptVi": "Mỗi sáng, tôi đeo kính rồi mới đến trường.",
                                "options": ["めがね", "くつ", "シャツ", "ぼうし"],
                                "correct": 0,
                                "explain": "💡 <strong>Quy tắc kết hợp trang phục trong tiếng Nhật:</strong><br>• <strong>めがねをかける</strong>: Đeo kính (Đúng).<br>• くつを<strong>はく</strong>: Xỏ giày/dép (mặc từ thắt lưng trở xuống).<br>• シャツを<strong>きる</strong>: Mặc áo (mặc từ vai trở xuống).<br>• ぼうしを<strong>かぶる</strong>: Đội mũ.<br>👉 Người Việt hay gọi chung là 'mặc/đeo', nhưng tiếng Nhật phân chia động từ cực kỳ chặt chẽ!"
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": "この 料理は ちょっと 味が (   ) ですから、お湯を 足して ください。",
                                "promptVi": "Món ăn này vị hơi đậm/mặn, nên xin hãy thêm chút nước sôi vào.",
                                "options": ["こい", "うすい", "あまい", "すずしい"],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng về hương vị (味):</strong><br>• <strong>濃い (こい)</strong>: Đậm đà, mặn, nồng ➔ Do vị đậm nên vế sau mới yêu cầu 'お湯を足してください' (hãy thêm nước sôi).<br>• 薄い (うすい): Nhạt, loãng.<br>• 甘い (あまい): Ngọt.<br>• 涼しい (すずしい): Mát mẻ (chỉ thời tiết, không dùng cho vị giác)."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": "駅の 前に 新しい (   ) が できましたから、毎日の 買い物が とても 便利に なりました。",
                                "promptVi": "Phía trước nhà ga mới có một siêu thị mở ra, nên việc mua sắm hàng ngày trở nên rất thuận tiện.",
                                "options": ["スーパー", "びょういん", "ぎんこう", "こうばん"],
                                "correct": 0,
                                "explain": "💡 <strong>Từ khóa ngữ cảnh:</strong> '買い物がとても便利に' (việc mua sắm trở nên thuận tiện). Trong 4 nơi thì chỉ có <strong>スーパー</strong> (siêu thị) là nơi để mua sắm thực phẩm hàng ngày. びょういん (bệnh viện), ぎんこう (ngân hàng), こうばん (đồn công an)."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": "すみません、その 辞書を 10分ぐらい (   ) も いいですか。",
                                "promptVi": "Xin lỗi, tôi có thể mượn dùng quyển từ điển đó khoảng 10 phút được không?",
                                "options": ["使って", "飲んで", "着て", "食べて"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu xin phép: V-てもいいですか</strong>.<br>Với từ điển (辞書), động từ thích hợp nhất là <strong>使う (つかう) ➔ 使って</strong> (sử dụng, dùng thử). Các động từ còn lại (uống, mặc áo, ăn) hoàn toàn không phù hợp ngữ cảnh."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": "電車の 時間を (   ) しまいましたから、友達との 約束に 遅れました。",
                                "promptVi": "Vì bị nhầm giờ tàu điện, nên tôi đã đến muộn cuộc hẹn với bạn bè.",
                                "options": ["まちがえて", "わすれて", "はじめて", "おぼえて"],
                                "correct": 0,
                                "explain": "💡 <strong>Phân biệt 間違える (まちがえる) vs 忘れる (わすれる):</strong><br>• <strong>時間を間違える</strong>: Xem nhầm/nhớ nhầm mốc giờ tàu chạy (Đúng).<br>• 時間を忘れる: Quên bẵng thời gian (say sưa làm gì đó quên cả giờ giấc). Ở đây bị trễ hẹn do nhìn nhầm giờ tàu, nên dùng 間違えてしまいました."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa tương đương (Câu đồng nghĩa)",
                        "groupInstruction": "Chọn câu trong 4 phương án (A, B, C, D) có ý nghĩa gần nhất với câu được gạch chân:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": "<u>この 部屋は あまり 広くないです。</u>",
                                "promptVi": "Căn phòng này không rộng lắm.",
                                "options": [
                                    "この 部屋は せまいです。",
                                    "この 部屋は とても 明るいです。",
                                    "この 部屋は とても 静かです。",
                                    "この 部屋は 家賃が 高いです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cặp tính từ trái nghĩa:</strong> 広い (ひろい: rộng) >< 狭い (せまい: hẹp).<br>'あまり広くない' (không rộng lắm) có nghĩa tương đương với 'せまいです' (hơi chật hẹp)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": "<u>あの カフェは いつも 人が たくさん います。</u>",
                                "promptVi": "Quán cà phê kia lúc nào cũng có rất nhiều người.",
                                "options": [
                                    "あの カフェは いつも にぎやかです。",
                                    "あの カフェは いつも 静かです。",
                                    "あの カフェは いつも 涼しいです。",
                                    "あの カフェは いつも 暗いです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng miêu tả không khí:</strong> '人がたくさんいます' (nhiều người đông đúc) đồng nghĩa với tính từ <strong>にぎやか（な）</strong> (náo nhiệt, nhộn nhịp, đông vui). 静か (yên tĩnh) là từ trái nghĩa."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": "<u>わたしは 辛い 料理が 好きじゃありません。</u>",
                                "promptVi": "Tôi không thích các món ăn cay.",
                                "options": [
                                    "わたしは 辛い 料理が 苦手です。",
                                    "わたしは 辛い 料理が 上手です。",
                                    "わたしは 辛い 料理を よく 食べます。",
                                    "わたしは 辛い 料理が 大好きです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cách nói tế nhị của người Nhật:</strong> Khi không thích hoặc ăn không quen một món gì đó, người Nhật thường dùng <strong>苦手（にがて）</strong> (kém, không quen, ngán) thay vì nói toẹt ra là 嫌い (ghét). Do đó '好きじゃありません' = '苦手です'."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": "<u>駅から 会社まで 歩いて 3分ぐらいです。</u>",
                                "promptVi": "Từ nhà ga đến công ty đi bộ mất khoảng 3 phút.",
                                "options": [
                                    "会社は 駅の 近くに あります。",
                                    "会社は 駅から とても 遠いです。",
                                    "会社へは バスで 行かなければ なりません。",
                                    "会社は 駅の 中に あります。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Khoảng cách đi lại:</strong> Đi bộ 3 phút (歩いて3分) biểu thị khoảng cách rất gần ga, tương đương với '駅の近くにあります' (nằm ở gần ga)."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": "<u>あした、一緒に 映画を 見に 行きませんか。</u>",
                                "promptVi": "Ngày mai bạn cùng đi xem phim với mình không?",
                                "options": [
                                    "あした、映画を 見ようと 誘って います。",
                                    "あした、映画を 1人で 見たいです。",
                                    "あしたは 忙しいですから、映画を 見ません。",
                                    "きのう、一緒に 映画を 見ました。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Chức năng giao tiếp:</strong> Mẫu câu '～ませんか' dùng để <strong>rủ rê, mời mọc đối phương (誘う - さそう)</strong> cùng làm một hành động nào đó. Phương án A thể hiện chính xác bản chất này."
                            }
                        ]
                    }
                ]
            },
                        {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán thành Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20) chuẩn 100% chữ Hán Bài 1-10.",
                "badge": "20 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn cách đọc Hiragana chính xác nhất cho chữ Hán được gạch chân (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": "大学で いろいろな 【外国語】を 勉強して います。",
                                "promptVi": "Tôi đang học nhiều thứ tiếng nước ngoài ở trường đại học.",
                                "options": ["がいこくご", "そとくにこ", "がいごくご", "がいこくこと"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 2]: 外 (NGOẠI) + 国 (QUỐC) + 語 (NGỮ)</strong>.<br>• 外: がい.<br>• 国: こく.<br>• 語: ご.<br>➔ Ghép lại đọc âm On-yomi là <strong>がいこくご</strong> (tiếng nước ngoài). Cẩn thận tránh nhầm với cách đọc âm Kun 'そとくに' hoặc nhầm âm đục 'こ'."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": "きょうは いい 天気で、きれいな 【青空】が 広がって います。",
                                "promptVi": "Hôm nay thời tiết đẹp, bầu trời xanh ngắt trải rộng.",
                                "options": ["あおぞら", "せいくう", "あおそら", "しろぞら"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 4 & 6]: 青 (THANH) + 空 (KHÔNG)</strong>.<br>• 青: あお.<br>• 空: そら ➔ Khi ghép xảy ra hiện tượng biến âm Renkaku (連濁) biến thành <strong>ぞら</strong>.<br>➔ Đọc đúng là <strong>あおぞら</strong> (bầu trời xanh). Cẩn thận bẫy không đục 'あおそら' hoặc âm Hán On-yomi 'せいくう'."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": "あしたの 待ち合わせの 【場所】は どこですか。",
                                "promptVi": "Địa điểm hẹn gặp ngày mai là ở đâu thế?",
                                "options": ["ばしょ", "はしょ", "じょうしょ", "ばところ"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 場 (TRƯỜNG) + 所 (SỞ)</strong>.<br>• 場: ば (âm đục 濁音).<br>• 所: しょ.<br>➔ Ghép lại đọc là <strong>ばしょ</strong> (địa điểm, nơi chốn). Cẩn thận bẫy quên âm đục 'はしょ' hoặc ghép âm Kun 'ばところ'."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": "家族と 一緒に レストランで 【食事】を しました。",
                                "promptVi": "Tôi đã cùng gia đình dùng bữa ở nhà hàng.",
                                "options": ["しょくじ", "たべこと", "しょくし", "じきじ"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 食 (THỰC) + 事 (SỰ)</strong>.<br>• 食: しょく (âm On).<br>• 事: じ (âm On, có âm đục).<br>➔ Ghép lại đọc là <strong>しょくじ</strong> (dùng bữa, ăn uống). Tránh đọc theo âm Kun 'たべこと' hoặc quên dấu đục 'しょくし'."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": "日曜日に ベトナムの 【友達】と 公園へ 行きました。",
                                "promptVi": "Chủ nhật tôi đã đi công viên cùng người bạn Việt Nam.",
                                "options": ["ともだち", "ゆうだち", "ともたち", "ゆうたち"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 10]: 友 (HỮU) + 達 (ĐẠT)</strong>.<br>• 友: とも.<br>• 達: たち ➔ Biến âm đục thành <strong>だち</strong>.<br>➔ Ghép lại đọc là <strong>ともだち</strong> (bạn bè). Bẫy thường gặp là quên âm đục 'ともたち' hoặc nhầm sang từ ゆうだち (mưa rào mùa hè)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn chữ Hán đúng cho từ Hiragana trong ngoặc 【 】",
                        "groupInstruction": "Chọn chữ Hán viết đúng nhất cho từ Hiragana trong câu (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": "わたしの へやは 【ひろい】ですから、とても 快適です。",
                                "promptVi": "Phòng của tôi rộng rãi nên rất thoải mái.",
                                "options": ["広い", "店い", "高い", "安い"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 5]: 広 (QUẢNG)</strong>.<br>• Có bộ Nghiễm (广) bên ngoài và khư (厶) bên trong ➔ <strong>広い (ひろい)</strong>: Rộng rãi.<br>• Bẫy: 店 (tiệm, quán), 高 (cao: đắt), 安 (an: rẻ)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": "駅の ロビーで 10分ぐらい 【まって】 ください。",
                                "promptVi": "Xin vui lòng đợi khoảng 10 phút ở sảnh nhà ga.",
                                "options": ["待って", "止って", "持って", "行って"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 待 (ĐÃI)</strong>.<br>• <strong>待つ (まつ)</strong>: Có bộ Xích (彳- bước chân trái) ➔ <strong>待って</strong> (chờ đợi - Đúng).<br>• 止 (chỉ: dừng lại), 持 (trì: cầm, có bộ Thủ 扌), 行 (hành: đi)."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": "きょうは 【てんき】が いいですから、山が よく 見えます。",
                                "promptVi": "Hôm nay thời tiết đẹp nên có thể nhìn thấy rõ núi.",
                                "options": ["天気", "雨気", "風気", "空気"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 4]: 天 (THIÊN: trời) + 気 (KHÍ)</strong> ➔ <strong>天気 (てんき)</strong>: Thời tiết.<br>• Các chữ Hán cùng bài 4: 雨 (mưa), 風 (gió), 空 (bầu trời)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": "すみません、駅へ 行く 【みち】を 教えて ください。",
                                "promptVi": "Xin lỗi, xin hãy chỉ cho tôi đường đi đến nhà ga.",
                                "options": ["道", "通", "右", "左"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: 道 (ĐẠO)</strong>.<br>• Có bộ Xước (辶) và chữ Thủ (首) bên trong ➔ <strong>道 (みち)</strong>: Con đường.<br>• Bẫy cùng Bài 6: 通 (thông: đi qua), 右 (phải), 左 (trái)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": "毎晩、日本語の 文法を 1時間 【べんきょう】します。",
                                "promptVi": "Mỗi tối tôi học ngữ pháp tiếng Nhật 1 tiếng.",
                                "options": ["勉強", "勉教", "强勉", "学強"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 9]: 勉 (MIỄN) + 強 (CƯỜNG)</strong> ➔ <strong>勉強 (べんきょう)</strong>: Học tập.<br>• Chữ 勉 có bộ Lực (力) bên phải, chữ 強 có bộ Cung (弓) và Trùng (虫). Tránh nhầm với chữ Giáo (教)."
                            }
                        ]
                    }
                ]
            },
{
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Gồm 3 dạng bài: Điền khuyết trợ từ & cấu trúc (21-26), Sắp xếp câu Hái sao ☆ (27-30) và Dịch câu tự luận (31-32).",
                "badge": "30 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền trợ từ hoặc thể ngữ pháp vào chỗ trống (   )",
                        "groupInstruction": "Chọn phương án đúng nhất (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": "毎朝、ジョギングを (   ) から、シャワーを 浴びます。",
                                "promptVi": "Mỗi sáng, tôi chạy bộ xong rồi mới tắm vòi hoa sen.",
                                "options": ["して", "する", "した", "し"],
                                "correct": 0,
                                "explain": "💡 <strong>Ngữ pháp V-てから:</strong> Biểu thị hành động sau chỉ diễn ra sau khi hoàn thành dứt điểm hành động trước ('làm V1 xong rồi mới làm V2'). Động từ する chia thể て là <strong>して</strong>."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": "すみません、あの 赤い 橋を (   )、すぐ 右に まがって ください。",
                                "promptVi": "Xin lỗi, sau khi băng qua cây cầu màu đỏ đằng kia, hãy rẽ phải ngay nhé.",
                                "options": ["わたって", "わたる", "わたり", "わたった"],
                                "correct": 0,
                                "explain": "💡 <strong>Ngữ pháp chỉ đường (Thể て liên kết hành động):</strong> Băng qua cầu rồi rẽ phải ➔ 渡る (わたる) chuyển sang thể て thành <strong>わたって</strong> để nối với vế sau '右にまがってください'."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": "日本の 食べ物 (   )、寿司が 一番 好きです。",
                                "promptVi": "Trong số các món ăn Nhật Bản, tôi thích món Sushi nhất.",
                                "options": ["の中で", "より", "から", "まで"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu so sánh nhất: 【Phạm vi】 の中で ～が一番...</strong>.<br>Ở đây phạm vi là '日本の食べ物' nên trợ từ bắt buộc là <strong>の中で (のなかで)</strong>. 'より' chỉ dùng trong so sánh hơn kém giữa 2 đối tượng."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": "東京の 地下鉄は 京都の 地下鉄 (   ) 複雑で、路線が 多いです。",
                                "promptVi": "Tàu điện ngầm Tokyo phức tạp và nhiều tuyến hơn so với tàu điện ngầm Kyoto.",
                                "options": ["より", "ほど", "のほうが", "でも"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu so sánh hơn kém: Aは Bより [Tính từ]</strong>.<br>A (Tokyo) thì phức tạp hơn B (Kyoto) ➔ Đặt <strong>より</strong> ngay sau đối tượng làm mốc so sánh (B)."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": "試験の とき、携帯電話を 使っては (   )。",
                                "promptVi": "Trong lúc thi, tuyệt đối không được sử dụng điện thoại di động.",
                                "options": ["いけません", "なりません", "いいです", "あります"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu cấm đoán: V-てはいけません</strong> (Không được phép làm gì). Cấm mang tính quy định, luật lệ phòng thi. 'なりません' chỉ đi với 'なければ (phải làm)'."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": "あしたは 朝 6時の 新幹線に 乗りますから、今夜は 早く (   ) なければ なりません。",
                                "promptVi": "Vì sáng mai tôi đi chuyến tàu Shinkansen lúc 6 giờ, nên tối nay tôi phải ngủ sớm.",
                                "options": ["寝", "寝て", "寝る", "寝た"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu bắt buộc: V-なければなりません</strong> (Phải làm gì).<br>Động từ 寝る (nhóm 2) bỏ る thêm なければ ➔ <strong>寝なければなりません (ねなければなりません)</strong>. Do chỗ trống đứng trước 'なければ' nên chỉ điền chữ <strong>寝</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Sắp xếp câu tìm vị trí Ngôi sao ( ★ )",
                        "groupInstruction": "Bấm chọn lần lượt 4 cụm từ để xếp vào các vị trí 1 - 2 - 3 - 4. Sau đó chọn đáp án nằm ở vị trí ngôi sao ★:",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "sentencePre": "わたしは 毎朝",
                                "sentencePost": "学校へ 行きます。",
                                "promptVi": "Mỗi sáng, tôi ăn sáng xong rồi mới đến trường.",
                                "parts": [
                                    {"id": 1, "text": "食べて"},
                                    {"id": 2, "text": "朝ごはんを"},
                                    {"id": 3, "text": "学校へ 行く 前に"},
                                    {"id": 4, "text": "から、"}
                                ],
                                "fullOrder": [2, 1, 4, 3],
                                "starPos": 2,
                                "correctOption": 4,
                                "fullSentence": "わたしは 毎朝 朝ごはんを 食べて から、 学校へ 行きます。",
                                "explain": "💡 <strong>Trật tự ngữ pháp:</strong> Tân ngữ + Trợ từ (朝ごはんを) ➔ Động từ thể て (食べて) ➔ Liên từ biểu thị thứ tự (から、).<br>Câu hoàn chỉnh: わたしは 毎朝 <strong>[2] 朝ごはんを [1] 食べて ★[4] から、</strong> 学校へ 行きます. Vị trí ★ số 3 là [4]."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "sentencePre": "美術館へは",
                                "sentencePost": "右に まがって ください。",
                                "promptVi": "Muốn đến bảo tàng mỹ thuật thì hãy đi thẳng con đường này rồi rẽ phải ở góc đường thứ hai.",
                                "parts": [
                                    {"id": 1, "text": "行って、"},
                                    {"id": 2, "text": "この道を"},
                                    {"id": 3, "text": "二つ目の 角を"},
                                    {"id": 4, "text": "まっすぐ"}
                                ],
                                "fullOrder": [2, 4, 1, 3],
                                "starPos": 2,
                                "correctOption": 1,
                                "fullSentence": "美術館へは この道を まっすぐ 行って、 二つ目の 角を 右に まがって ください。",
                                "explain": "💡 <strong>Trật tự chỉ đường:</strong> [2] この道を ➔ [4] まっすぐ ➔ [1] 行って、 ➔ [3] 二つ目の 角を ➔ 右に まがって ください.<br>Vị trí ngôi sao ★ số 3 là <strong>[1] 行って、</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "sentencePre": "1年の",
                                "sentencePost": "好きです。",
                                "promptVi": "Trong một năm, tôi thích mùa hè nhất.",
                                "parts": [
                                    {"id": 1, "text": "が"},
                                    {"id": 2, "text": "の中で"},
                                    {"id": 3, "text": "一番"},
                                    {"id": 4, "text": "夏"}
                                ],
                                "fullOrder": [2, 4, 1, 3],
                                "starPos": 2,
                                "correctOption": 1,
                                "fullSentence": "1年の の中で 夏 が 一番 好きです。",
                                "explain": "💡 <strong>Cấu trúc so sánh nhất:</strong> [Phạm vi] + [2] の中で ➔ [Chủ thể] [4] 夏 + [1] が ➔ [3] 一番 ➔ 好きです.<br>Trật tự: 2 ➔ 4 ➔ ★[1] ➔ 3. Đáp án vị trí ngôi sao là <strong>[1] が</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "sentencePre": "映画館で 映画を",
                                "sentencePost": "買いたいです。",
                                "promptVi": "Ở rạp chiếu phim, trước khi xem phim tôi muốn mua nước trái cây.",
                                "parts": [
                                    {"id": 1, "text": "前に、"},
                                    {"id": 2, "text": "を"},
                                    {"id": 3, "text": "ジュース"},
                                    {"id": 4, "text": "見る"}
                                ],
                                "fullOrder": [4, 1, 3, 2],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "映画館で 映画を 見る 前に、 ジュース を 買いたいです。",
                                "explain": "💡 <strong>Ngữ pháp V-る前に:</strong> [4] 見る ➔ [1] 前に、 ➔ [3] ジュース ➔ [2] を ➔ 買いたいです.<br>Trật tự: 4 ➔ 1 ➔ ★[3] ➔ 2. Vị trí ngôi sao ★ là <strong>[3] ジュース</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu tự luận (Nhật ↔ Việt)",
                        "groupInstruction": "Tự gõ câu dịch hoàn chỉnh vào ô bên dưới. Có thể dùng nút '🎯 Tôi Thấy Tôi Viết Đúng' nếu dùng từ đồng nghĩa hợp lý:",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "dir": "ja_to_vi",
                                "prompt": "この 部屋は 駅から 近くて 便利ですが、近くに 大きい 道路が ありますから、夜 ちょっと うるさいです。",
                                "placeholder": "Nhập bản dịch tiếng Việt tại đây...",
                                "standard": "Căn phòng này gần ga và tiện lợi nhưng vì ở gần có con đường lớn nên ban đêm hơi ồn ào.",
                                "keywords": ["gần ga", "tiện", "đường lớn", "đêm", "ồn"],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• 近くて便利: Tính từ kết hợp thể て (gần và tiện lợi).<br>• が: Nhưng (nối 2 vế tương phản).<br>• ～から: Vì... (chỉ lý do: vì gần đường lớn).<br>• ちょっとうるさい: Hơi ồn ào vào ban đêm."
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "dir": "vi_to_ja",
                                "prompt": "Trước khi đi ngủ, tôi luôn luôn tắt đèn và nghe nhạc khoảng 15 phút.",
                                "placeholder": "Gõ câu tiếng Nhật tại đây (dùng Hiragana hoặc Kanji)...",
                                "standard": "寝る 前に、いつも 電気を 消して、15分ぐらい 音楽を 聞きます。",
                                "acceptable": [
                                    "寝る前に、いつも電気を消して、15分ぐらい音楽を聞きます。",
                                    "寝るまえに、いつもでんきをけして、15ふんぐらいおんがくをききます。",
                                    "ねるまえに、いつもでんきをけして、15ふんぐらいおんがくをききます。",
                                    "寝る前にいつも電気を消して15分ぐらい音楽を聞きます。"
                                ],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• Trước khi ngủ: 寝る 前に (Động từ thể từ điển + 前に).<br>• Tắt đèn: 電気を 消して (V-て nối hành động).<br>• Nghe nhạc 15 phút: 15分ぐらい 音楽を 聞きます."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc kỹ thông báo giao lưu văn hóa và trả lời 2 câu hỏi kiểm tra thông tin chi tiết.",
                "badge": "10 Điểm",
                "readingPassage": {
                    "title": "【新宿国際交流センター】春の 日本文化体験（お茶会）の おしらせ",
                    "content": "みなさん、こんにちは！ 新宿国際交流センターでは、外国人の ための「日本文化体験イベント」を 行います。\n今回は、日本の 伝統的な「お茶（茶道 - さどう）」を 体験します。おいしい 抹茶（まっちゃ）と 季節の 和菓子（わがし）を 楽しむ ことが できます。\n着物（きもの）を 着て 写真を 撮る コーナーも ありますよ！\n\n【日時】5月20日（土曜日）午後2時〜4時（受付は 1時30分から）\n【場所】新宿国際交流センター 3階 和室\n【参加費】1人 500円（お茶と お菓子の 代金です）\n【定員】20人（先着順）\n※ 参加したい 人は、5月15日までに センターの ホームページから 申し込んで ください。\n※ 白い 靴下（くつした）を 履いて 来て ください。",
                    "translation": "Chào mọi người! Trung tâm Giao lưu Quốc tế Shinjuku tổ chức 'Sự kiện trải nghiệm văn hóa Nhật Bản' dành cho người nước ngoài.\nLần này chúng ta sẽ cùng trải nghiệm môn 'Trà đạo' truyền thống của Nhật Bản. Các bạn có thể thưởng thức trà Matcha thơm ngon và bánh ngọt Wagashi theo mùa.\nNgoài ra còn có góc mặc thử Kimono để chụp ảnh kỷ niệm nữa đấy!\n\n【Thời gian】Thứ Bảy ngày 20/5 từ 14:00 - 16:00 (Đón tiếp từ 13:30)\n【Địa điểm】Phòng chiếu tatami tầng 3, Trung tâm Giao lưu Quốc tế Shinjuku\n【Phí tham gia】500 yên/người (Đã bao gồm tiền trà và bánh)\n【Số lượng】20 người (Ưu tiên ai đăng ký trước)\n※ Người muốn tham gia xin vui lòng đăng ký qua website của trung tâm trước ngày 15/5.\n※ Khi đến tham gia xin hãy đi tất trắng (vớ trắng)."
                },
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": "この イベントの 参加費と 申し込みの 締め切りは いつですか。",
                        "promptVi": "Chi phí tham gia và hạn chót đăng ký của sự kiện này là khi nào?",
                        "options": [
                            "参加費は 500円で、締め切りは 5月15日です。",
                            "参加費は 無料で、締め切りは 5月20日です。",
                            "参加費は 1,000円で、締め切りは 5月15日です。",
                            "参加費は 500円で、締め切りは 5月20日です。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Tìm thông tin trong bài đọc:</strong><br>• 【参加費】1人 500円.<br>• 締め切り: '5月15日までに センターの ホームページから 申し込んで ください'.<br>➔ Phương án A hoàn toàn chính xác."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": "イベントに ついて、書いて ある ことと 合って いる ものは どれですか。",
                        "promptVi": "Câu nào dưới đây ĐÚNG với nội dung thông báo?",
                        "options": [
                            "参加する 人は、白い 靴下を 履いて 行かなければ なりません。",
                            "当日の 午後2時に 行けば、だれでも 予約なしで 参加できます。",
                            "着物を 着る ために、別で 2,000円 払わなければ なりません。",
                            "イベントは 新宿駅の 西口の カフェで 行われます。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Đối chiếu các chi tiết:</strong><br>• Trong bài ghi rõ lưu ý: 『※ 白い 靴下（くつした）を 履いて 来て ください。』 ➔ Phương án A đúng.<br>• Phương án B sai vì cần đăng ký trước trước ngày 15/5 và giới hạn 20 người.<br>• Phương án C sai vì chi phí trọn gói 500 yên.<br>• Phương án D sai vì địa điểm là Trung tâm Giao lưu Quốc tế tầng 3, không phải quán cà phê."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (yêu cầu mỗi câu viết ít nhất 50 từ/ký tự).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "あなたの 家族について 紹介してください。（何人 家族ですか。どこに 住んで いますか。仕事や 好きな ことも 書いてください。★50字以上で 書いてください）",
                        "promptVi": "Hãy giới thiệu về gia đình bạn (Có mấy người? Sống ở đâu? Làm nghề gì hoặc thích gì? ★Yêu cầu viết ít nhất 50 từ/ký tự bằng tiếng Nhật)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしの家族は4人です。父、母、姉とわたしです...",
                        "hints": [
                            "Số thành viên: わたしの 家族は ～人です (父、母、...と わたしです)",
                            "Nơi ở & nghề nghiệp: ～に 住んで います / 父・母は ～の 仕事を して います",
                            "Sở thích/tính cách: ～が 好きです / とても 親切で 元気です",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしの 家族は 4人です。父、母、姉と わたしです。家族は ベトナムの ハノイに 住んで います。父は 会社員で、母は 英語の 先生です。姉は 大学生で、わたしは 日本語を 勉強して います。週末は いつも みんなで おいしい ごはんを 食べます。とても にぎやかで 仲がいい 家族です。",
                        "modelVi": "Gia đình tôi có 4 người: bố, mẹ, chị gái và tôi. Gia đình tôi sống ở Hà Nội, Việt Nam. Bố tôi là nhân viên công ty, mẹ là giáo viên tiếng Anh. Chị gái tôi là sinh viên đại học, còn tôi đang học tiếng Nhật. Cuối tuần mọi người luôn cùng nhau ăn cơm ngon. Gia đình tôi rất náo nhiệt và hòa thuận.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; giới thiệu đầy đủ số người, nơi ở, nghề nghiệp; dùng đúng trợ từ và ngữ pháp kết nối câu."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "日本へ 行ったら、どんな ことを してみたいですか。行きたい 所や したい こと、りゆうを 書いてください。（★50字以上で 書いてください）",
                        "promptVi": "Nếu sang Nhật Bản, bạn muốn làm những điều gì? Hãy viết về nơi muốn đến, điều muốn trải nghiệm và nêu rõ lý do (★Yêu cầu viết ít nhất 50 từ/ký tự)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは 日本の 京都へ 行ってみたいです...",
                        "hints": [
                            "Địa điểm muốn đến: わたしは ～へ 行ってみたいです (京都 / 東京 / 北海道)",
                            "Trải nghiệm: ～を 見たり、～を 食べたり したいです",
                            "Lý do: 写真で 見て とても きれいでしたから / 有名ですから",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしは 日本の 京都へ 行って、古い お寺や きれいな 桜を 見てみたいです。写真で 見て、とても 美しかったからです。そして、本物の 抹茶を 飲んだり、おいしい 寿司を 食べたり したいです。日本人の 友だちも たくさん つくりたいと 思います。日本へ 行く ことが 今から とても 楽しみです。",
                        "modelVi": "Tôi muốn đến Kyoto của Nhật Bản để ngắm những ngôi chùa cổ và hoa anh đào tuyệt đẹp, vì xem qua ảnh thấy rất đẹp đẽ. Ngoài ra, tôi muốn uống matcha chính gốc và ăn món sushi tươi ngon. Tôi cũng muốn kết bạn với thật nhiều người Nhật. Ngay từ bây giờ tôi đã rất mong chờ được đến Nhật Bản rồi.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; áp dụng nhuần nhuyễn mẫu ngữ pháp ～てみたい / ～たり～たりしたい / ～から."
                    }
                ]
            }
        ]
    }

def build_m102():
    return {
        "code": "M102",
        "name": "Mã Đề M102 (Đề Trọng Tâm Chuẩn Bảng Lớp)",
        "tag": "⭐ Trọng Tâm Bài 5 - 8 • Đề Bảng Thầy Cô",
        "desc": "Thiết kế bám sát 100% từng hạng mục trên bảng viết của giảng viên: Thể て, rủ rê, so sánh lựa chọn, hái sao ☆, đọc hiểu email dã ngoại và tự luận Can-do ≥ 50 từ/ký tự.",
        "timeLimit": 45 * 60,
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": "朝 起きてから、まず 洗面所で (   ) を 洗います。",
                                "promptVi": "Buổi sáng sau khi thức dậy, trước tiên tôi rửa mặt ở bồn rửa.",
                                "options": ["かお", "は", "あたま", "あし"],
                                "correct": 0,
                                "explain": "💡 <strong>Bẫy kết hợp động từ cơ thể:</strong><br>• <strong>顔を洗う (かおをあらう)</strong>: Rửa mặt (Đúng).<br>• 歯 (は: răng) phải đi với <strong>磨く (みがく)</strong>: 歯を磨く (đánh răng).<br>• 頭 (あたま: đầu) đi với <strong>洗う</strong> nhưng là gội đầu (trong phòng tắm, không dùng ở chậu rửa mặt buổi sáng).<br>➔ Phương án A chính xác nhất!"
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": "喉が かわきましたから、冷たい (   ) が 飲みたいです。",
                                "promptVi": "Vì khát nước nên tôi muốn uống nước mát.",
                                "options": ["お水", "パン", "ケーキ", "りんご"],
                                "correct": 0,
                                "explain": "💡 <strong>Từ khóa:</strong> '喉がかわきました' (khát nước) và động từ '飲みたい' (muốn uống). Trong 4 từ chỉ có <strong>お水 (おみず: nước)</strong> là đồ uống. Các từ còn lại đều là đồ ăn."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": "この 交差点は 車が たくさん 通りますから、とても (   ) です。気をつけて ください。",
                                "promptVi": "Giao lộ này có rất nhiều ô tô chạy qua nên rất nguy hiểm. Hãy cẩn thận nhé.",
                                "options": ["あぶない", "あんぜん", "しずか", "すずしい"],
                                "correct": 0,
                                "explain": "💡 <strong>Ngữ cảnh an toàn giao thông:</strong> Xe cộ qua lại đông đúc ➔ Vế sau nhắc nhở '気をつけてください' (hãy cẩn thận) ➔ Tính từ phải là <strong>危ない (あぶない: nguy hiểm)</strong>. 安全 (あんぜん: an toàn) là từ trái nghĩa."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": "すみません、駅までの 行き方を (   ) もらえませんか。",
                                "promptVi": "Xin lỗi, bạn có thể chỉ giúp tôi đường đến nhà ga được không ạ?",
                                "options": ["教えて", "ならって", "きいて", "はなして"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu nhờ vả lịch sự: V-てもらえませんか</strong>.<br>Hỏi đường, nhờ ai đó chỉ đường cho mình thì dùng <strong>教える (おしえる) ➔ 教えて</strong> (chỉ bảo, hướng dẫn). 習う (ならう: học từ ai), 聞く (きく: nghe/hỏi)."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": "天気が いい 日には、近くの 緑豊かな 公園へ (   ) に 行きます。",
                                "promptVi": "Vào những ngày thời tiết đẹp, tôi thường đến công viên rợp bóng cây xanh gần nhà để đi dạo.",
                                "options": ["さんぽ", "かいもの", "べんきょう", "しごと"],
                                "correct": 0,
                                "explain": "💡 <strong>Mục đích đi đến công viên: [Danh từ] に行く</strong>.<br>Với địa điểm là '緑豊かな公園' (công viên xanh mát), hành động phù hợp nhất là <strong>散歩 (さんぽ) ➔ 散歩に行く</strong> (đi dạo bộ)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa tương đương (Câu đồng nghĩa)",
                        "groupInstruction": "Chọn câu trong 4 phương án (A, B, C, D) có ý nghĩa gần nhất với câu được gạch chân:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": "<u>山田先生は 親切で、とても いい 先生です。</u>",
                                "promptVi": "Thầy Yamada là một giáo viên tốt bụng và rất tuyệt vời.",
                                "options": [
                                    "山田先生は やさしい 先生です。",
                                    "山田先生は 厳しい 先生です。",
                                    "山田先生は おもしろくない 先生です。",
                                    "山田先生は 若くない 先生です。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tính từ đồng nghĩa chỉ tính cách:</strong> <strong>親切（な）(しんせつ)</strong> = <strong>優しい (やさしい)</strong> (tốt bụng, hiền từ, chu đáo). 厳しい (きびしい: nghiêm khắc) là từ trái nghĩa."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": "<u>この 荷物は あまり 重くないですから、1人で 持てます。</u>",
                                "promptVi": "Kiện hành lý này không nặng lắm nên một mình tôi có thể xách được.",
                                "options": [
                                    "この 荷物は かるいです。",
                                    "この 荷物は とても 重いです。",
                                    "この 荷物は とても 大きいです。",
                                    "この 荷物は 高いです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Cặp tính từ trọng lượng:</strong> 重い (おもい: nặng) >< 軽い (かるい: nhẹ).<br>'あまり重くない' (không nặng mấy) đồng nghĩa với 'かるい' (nhẹ nhàng)."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": "<u>わたしは お酒を 全然 飲みません。</u>",
                                "promptVi": "Tôi hoàn toàn không uống rượu.",
                                "options": [
                                    "わたしは お酒を まったく 飲みません。",
                                    "わたしは お酒を たまに 飲みます。",
                                    "わたしは お酒を よく 飲みます。",
                                    "わたしは お酒が 大好きです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Phó từ phủ định tuyệt đối:</strong> <strong>全然 (ぜんぜん) + Phủ định</strong> = <strong>まったく + Phủ định</strong> (hoàn toàn không... chút nào). たまに (thỉnh thoảng), よく (thường xuyên)."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": "<u>きょうは 会社が 休みですから、家に います。</u>",
                                "promptVi": "Hôm nay công ty nghỉ nên tôi ở nhà.",
                                "options": [
                                    "きょうは 会社へ 仕事に 行きません。",
                                    "きょうは 会社で 残業します。",
                                    "きょうは 朝から 会社へ 行きます。",
                                    "きょうは 会社で 会議が あります。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Biểu đạt đồng nghĩa:</strong> '会社が休みです' (công ty nghỉ làm) đồng nghĩa với việc '会社へ仕事に行きません' (không đến công ty làm việc)."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": "<u>図書館の 中では 静かに して ください。</u>",
                                "promptVi": "Trong thư viện xin hãy giữ trật tự yên tĩnh.",
                                "options": [
                                    "図書館の 中で 大きい 声で 話さないで ください。",
                                    "図書館の 中で 大きい 声で 話しても いいです。",
                                    "図書館の 中で 音楽を 聞いても いいです。",
                                    "図書館の 中で 電話を かけて ください。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Yêu cầu giữ yên lặng:</strong> '静かにしてください' (hãy giữ trật tự) có ý nghĩa tương đương với '大きい声で話さないでください' (xin đừng nói to tiếng)."
                            }
                        ]
                    }
                ]
            },
                        {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán thành Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20) chuẩn 100% chữ Hán Bài 1-10.",
                "badge": "20 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn cách đọc Hiragana chính xác nhất cho chữ Hán được gạch chân (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": "夏休みに 家族と 北海道へ 【旅行】に 行きます。",
                                "promptVi": "Kỳ nghỉ hè tôi sẽ đi du lịch Hokkaido cùng gia đình.",
                                "options": ["りょこう", "りょこ", "たびゆき", "りょうこう"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 10]: 旅 (LỮ) + 行 (HÀNH)</strong>.<br>• 旅: りょ.<br>• 行: こう (trường âm).<br>➔ Ghép lại đọc là <strong>りょこう</strong> (chuyến du lịch). Bẫy âm ngắn 'りょこ' hoặc nhầm sang trường âm ở âm đầu 'りょうこう'."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": "テストの 【時間】は 45分ですから、急いで ください。",
                                "promptVi": "Thời gian làm bài thi là 45 phút nên các bạn hãy khẩn trương nhé.",
                                "options": ["じかん", "しかん", "ときま", "じけん"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 時 (THỜI) + 間 (GIAN)</strong>.<br>• 時: じ (âm đục 濁音).<br>• 間: かん.<br>➔ Đọc là <strong>じかん</strong> (thời gian). Cẩn thận bẫy quên âm đục 'しかん' hoặc đọc theo âm thuần Nhật 'ときま'."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": "部屋で 静かな 【音楽】を 聞きながら 休みます。",
                                "promptVi": "Tôi nghỉ ngơi trong phòng vừa nghe nhạc nhẹ nhàng.",
                                "options": ["おんがく", "おとらく", "おんらく", "おんかっこ"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 10]: 音 (ÂM) + 楽 (LẠC / NHẠC)</strong>.<br>• 音: おん.<br>• 楽: がく (biến âm đục 濁音).<br>➔ Ghép lại đọc là <strong>おんがく</strong> (âm nhạc). Tránh bẫy đọc chữ Lạc là 'らく' hay âm Kun 'おと'."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": "朝 8時半に 【学校】に 着きました。",
                                "promptVi": "Tôi đã đến trường học lúc 8 giờ rưỡi sáng.",
                                "options": ["がっこう", "がくこう", "がっこ", "かっこう"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 9]: 学 (HỌC) + 校 (HIỆU)</strong>.<br>• 学: がく ➔ Khi ghép với 'こう' xảy ra hiện tượng âm ngắt Sokuon biến thành <strong>がっ</strong>.<br>• 校: こう (trường âm).<br>➔ Đọc đúng là <strong>がっこう</strong> (trường học)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": "父は 毎日 忙しく 【仕事】を して います。",
                                "promptVi": "Bố tôi mỗi ngày đều bận rộn làm việc.",
                                "options": ["しごと", "じごと", "つかえこと", "しこと"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 仕 (SĨ) + 事 (SỰ)</strong>.<br>• 仕: し.<br>• 事: ごと (biến âm đục 濁音).<br>➔ Ghép lại đọc là <strong>しごと</strong> (công việc). Cẩn thận bẫy quên âm đục 'しこと' hoặc đục nhầm chữ đầu 'じごと'."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn chữ Hán đúng cho từ Hiragana trong ngoặc 【 】",
                        "groupInstruction": "Chọn chữ Hán viết đúng nhất cho từ Hiragana trong câu (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": "来週、京都へ 紅葉を 見に 【いきます】。",
                                "promptVi": "Tuần sau tôi sẽ đi Kyoto để ngắm lá đỏ mùa thu.",
                                "options": ["行きます", "出きます", "待きます", "止きます"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 10]: 行 (HÀNH: đi)</strong> ➔ <strong>行きます (いきます)</strong>.<br>• Các chữ Hán Bài 7 dễ gây nhầm: 出 (xuất: ra), 待 (đãi: chờ), 止 (chỉ: dừng)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": "その 交差点を 【みぎ】へ 曲がって ください。",
                                "promptVi": "Xin hãy rẽ sang bên phải ở ngã tư đó.",
                                "options": ["右", "左", "石", "若"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: Phân biệt 右 (HỮU: bên phải) vs 左 (TẢ: bên trái):</strong><br>• <strong>右 (みぎ)</strong>: Bên trong có chữ Khẩu (口 - miệng cầm đũa ăn bên phải - Đúng).<br>• 左 (ひだり): Bên trong có chữ Công (工).<br>• 石 (hòn đá)."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": "この 通りは いつも 人が 【おおい】です。",
                                "promptVi": "Con đường này lúc nào cũng đông người.",
                                "options": ["多い", "少ない", "夕い", "名い"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 5]: 多 (ĐA: nhiều)</strong> ➔ <strong>多い (おおい)</strong>: Cấu tạo gồm 2 chữ Tịch 夕 chồng lên nhau.<br>• Bẫy: 少ない (すくない: ít - từ trái nghĩa cùng bài 5), 夕 (buổi chiều)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": "毎朝 【あさ】ご飯を 食べてから、出かけます。",
                                "promptVi": "Mỗi sáng sau khi ăn bữa sáng tôi mới ra ngoài.",
                                "options": ["朝", "昼", "夜", "前"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 朝 (TRIÊU)</strong> ➔ <strong>朝 (あさ)</strong>: Buổi sáng.<br>• Các từ chỉ thời gian cùng Bài 8: 昼 (trưa - ひる), 夜 (tối - よる), 前 (trước - まえ)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": "冬になると、山に 【しろい】 雪が 降ります。",
                                "promptVi": "Hễ mùa đông đến là tuyết trắng rơi nhiều trên núi.",
                                "options": ["白い", "青い", "赤い", "黒い"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: 白 (BẠCH)</strong> ➔ <strong>白い (しろい)</strong>: Màu trắng.<br>• Phân biệt bộ màu sắc Bài 6: 青 (xanh da trời), 赤 (đỏ), 黒 (đen)."
                            }
                        ]
                    }
                ]
            },
{
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Gồm 3 dạng bài: Điền khuyết trợ từ & cấu trúc (21-26), Sắp xếp câu Hái sao ☆ (27-30) và Dịch câu tự luận (31-32).",
                "badge": "30 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền trợ từ hoặc thể ngữ pháp vào chỗ trống (   )",
                        "groupInstruction": "Chọn phương án đúng nhất (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": "休みの日は 家で 映画を (   )り、音楽を 聞いたり します。",
                                "promptVi": "Vào ngày nghỉ tôi thường xem phim hoặc nghe nhạc ở nhà.",
                                "options": ["見", "見て", "見る", "見た"],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc liệt kê hành động tiêu biểu: V-たり V-たり します</strong>.<br>Động từ nhóm 2: 見る chuyển sang thể た là 見た ➔ gắn với り thành <strong>見たり</strong>. Chỗ trống đứng trước 'り' nên chọn <strong>見</strong> (hoặc 見た nếu cả cụm)."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": "今度の 土曜日、一緒に 桜を 見に 行き(   )。",
                                "promptVi": "Thứ Bảy tới bạn cùng đi ngắm hoa anh đào với tôi không?",
                                "options": ["ませんか", "ましょう", "ますか", "たいです"],
                                "correct": 0,
                                "explain": "💡 <strong>Lời rủ rê, thăm dò ý kiến lịch sự: V-ませんか</strong> (Bạn có cùng làm... không?). 'ましょう' là hô hào cùng làm khi đối phương đã đồng ý."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": "コーヒーと 紅茶と、(   ) が 好きですか。",
                                "promptVi": "Giữa cà phê và trà, bạn thích thứ nào hơn?",
                                "options": ["どちら", "どれ", "どこ", "だれ"],
                                "correct": 0,
                                "explain": "💡 <strong>So sánh lựa chọn giữa 2 đối tượng: Aと Bと どちらが...</strong>.<br>Khi lựa chọn giữa 2 vật, đại từ bắt buộc phải là <strong>どちら (hoặc どっち)</strong>. 'どれ' chỉ dùng khi chọn trong 3 đối tượng trở lên."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": "すみません、この 部屋で タバコを 吸っては (   )。",
                                "promptVi": "Xin lỗi, không được phép hút thuốc trong căn phòng này.",
                                "options": ["いけません", "なりません", "いいです", "ありません"],
                                "correct": 0,
                                "explain": "💡 <strong>Cấm đoán: V-てはいけません</strong> (Không được làm gì). Tuyệt đối cấm hút thuốc trong phòng kín."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": "あの レストランの 料理は とても おいしい (   )、値段が ちょっと 高いです。",
                                "promptVi": "Món ăn ở nhà hàng đó rất ngon, nhưng giá hơi đắt một chút.",
                                "options": ["ですが", "ですから", "ので", "そして"],
                                "correct": 0,
                                "explain": "💡 <strong>Liên từ nối tương phản: ～ですが</strong> (Ngon nhưng mà đắt). Hai vế đối lập về tính chất: khen ngon (+) nhưng chê đắt (-)."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": "あしたは 朝 7時に 家を (   ) なければ なりません。",
                                "promptVi": "Sáng mai tôi phải rời khỏi nhà lúc 7 giờ.",
                                "options": ["出", "出て", "出る", "出た"],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc bắt buộc: V-なければなりません</strong>.<br>Động từ 出る (nhóm 2) bỏ る thêm なければ ➔ <strong>出なければなりません</strong>. Chỗ trống đứng trước なければ nên chọn <strong>出</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Sắp xếp câu tìm vị trí Ngôi sao ( ★ )",
                        "groupInstruction": "Bấm chọn lần lượt 4 cụm từ để xếp vào các vị trí 1 - 2 - 3 - 4. Sau đó chọn đáp án nằm ở vị trí ngôi sao ★:",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "sentencePre": "休みの日は 家で",
                                "sentencePost": "読んだり します。",
                                "promptVi": "Vào ngày nghỉ ở nhà tôi thường xem phim hoặc đọc sách.",
                                "parts": [
                                    {"id": 1, "text": "見たり、"},
                                    {"id": 2, "text": "映画を"},
                                    {"id": 3, "text": "本を"},
                                    {"id": 4, "text": "音楽を"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "休みの日は 家で 映画を 見たり、 本を 読んだり します。",
                                "explain": "💡 <strong>Cấu trúc:</strong> [2] 映画を ➔ [1] 見たり、 ➔ ★[3] 本を ➔ 読んだりします.<br>Vị trí ngôi sao ★ số 3 là <strong>[3] 本を</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "sentencePre": "京都は",
                                "sentencePost": "お寺が 多いです。",
                                "promptVi": "Kyoto thì yên tĩnh hơn Tokyo và có nhiều chùa cổ.",
                                "parts": [
                                    {"id": 1, "text": "より"},
                                    {"id": 2, "text": "静かで、"},
                                    {"id": 3, "text": "東京"},
                                    {"id": 4, "text": "のほうが"}
                                ],
                                "fullOrder": [3, 1, 2, 4],
                                "starPos": 2,
                                "correctOption": 2,
                                "fullSentence": "京都は 東京 より 静かで、 お寺が 多いです。",
                                "explain": "💡 <strong>Cấu trúc so sánh:</strong> Aは [3] 東京 + [1] より ➔ ★[2] 静かで、 ➔ お寺が多いです.<br>Vị trí ngôi sao ★ số 3 là <strong>[2] 静かで、</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "sentencePre": "薬を",
                                "sentencePost": "食べて ください。",
                                "promptVi": "Trước khi uống thuốc, hãy ăn cơm đã nhé.",
                                "parts": [
                                    {"id": 1, "text": "前に、"},
                                    {"id": 2, "text": "ごはんを"},
                                    {"id": 3, "text": "飲む"},
                                    {"id": 4, "text": "ちゃんと"}
                                ],
                                "fullOrder": [3, 1, 2, 4],
                                "starPos": 2,
                                "correctOption": 2,
                                "fullSentence": "薬を 飲む 前に、 ごはんを ちゃんと 食べて ください。",
                                "explain": "💡 <strong>Ngữ pháp V-る前に:</strong> 薬を [3] 飲む ➔ [1] 前に、 ➔ ★[2] ごはんを ➔ [4] ちゃんと ➔ 食べてください.<br>Vị trí ngôi sao ★ số 3 là <strong>[2] ごはんを</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "sentencePre": "この川で",
                                "sentencePost": "危ないですから。",
                                "promptVi": "Không được bơi ở con sông này vì rất nguy hiểm.",
                                "parts": [
                                    {"id": 1, "text": "いけません、"},
                                    {"id": 2, "text": "泳いでは"},
                                    {"id": 3, "text": "深く"},
                                    {"id": 4, "text": "とても"}
                                ],
                                "fullOrder": [2, 1, 4, 3],
                                "starPos": 2,
                                "correctOption": 4,
                                "fullSentence": "この川で 泳いでは いけません、 とても 危ないですから。",
                                "explain": "💡 <strong>Ngữ pháp cấm đoán:</strong> [2] 泳いでは ➔ [1] いけません、 ➔ ★[4] とても ➔ [3] 深くて 危ないですから.<br>Vị trí ngôi sao ★ số 3 là <strong>[4] とても</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu tự luận (Nhật ↔ Việt)",
                        "groupInstruction": "Tự gõ câu dịch hoàn chỉnh vào ô bên dưới. Có thể dùng nút '🎯 Tôi Thấy Tôi Viết Đúng' nếu dùng từ đồng nghĩa hợp lý:",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "dir": "ja_to_vi",
                                "prompt": "週末は たいてい 部屋の 掃除を したり、洗濯を したり して、のんびり 過ごします。",
                                "placeholder": "Nhập bản dịch tiếng Việt tại đây...",
                                "standard": "Cuối tuần tôi thường dọn dẹp phòng ốc, giặt giũ quần áo rồi thong thả nghỉ ngơi trải qua ngày nghỉ.",
                                "keywords": ["cuối tuần", "dọn dẹp", "giặt", "thong thả", "nghỉ ngơi"],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• たいてい: Thường thường.<br>• ～たり～たり: Liệt kê việc dọn phòng và giặt đồ.<br>• のんびり過ごします: Trải qua thời gian một cách thảnh thơi, ung dung."
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "dir": "vi_to_ja",
                                "prompt": "Giữa tiếng Nhật và tiếng Anh, bạn thấy cái nào khó hơn?",
                                "placeholder": "Gõ câu tiếng Nhật tại đây (dùng Hiragana hoặc Kanji)...",
                                "standard": "日本語と 英語と、どちらのほうが 難しいですか。",
                                "acceptable": [
                                    "日本語と英語と、どちらのほうが難しいですか。",
                                    "日本語と英語と、どちらが難しいですか。",
                                    "にほんごとえいごと、どちらのほうがむずかしいですか。",
                                    "にほんごとえいごとどちらがむずかしいですか。"
                                ],
                                "explain": "💡 <strong>Mẫu câu so sánh lựa chọn:</strong> Aと Bと、どちら（のほう）が [Tính từ] ですか。"
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc kỹ email mời tham gia buổi dã ngoại BBQ và trả lời 2 câu hỏi kiểm tra thông tin.",
                "badge": "10 Điểm",
                "readingPassage": {
                    "title": "【メール】ケンジさんからの BBQパーティーの おさそい",
                    "content": "グエンさん、こんにちは！ ケンジです。\n今度の 日曜日、天気が よさそうですから、多摩川（たまがわ）の 河原で クラスの みんなと BBQ（バーベキュー）を しようと 思って います。\n\n【日時】10月15日（日曜日）午前11時〜午後3時\n【集合場所】小田急線 和泉多摩川駅の 改札口に 午前10時45分に 集合して ください。\n【持ち物】飲み物は 自分で 好きな ものを 買って 持って来て ください。お肉や 野菜、お皿などは わたしが 準備します。\n【会費】1人 1,500円です（お肉と 道具の 代金です）。\n\n雨が 降ったら、駅の 近くの レストランで ごはんを 食べます。\n準備が ありますから、来られるかどうか 金曜日の 夜までに メールで 返事を くださいね！\n待って います！",
                    "translation": "Chào bạn Nguyên! Mình là Kenji đây.\nChủ nhật tới thời tiết có vẻ rất đẹp nên mình dự định cùng các bạn trong lớp tổ chức tiệc BBQ bên bờ sông Tamagawa.\n\n【Thời gian】Chủ nhật ngày 15/10 từ 11:00 đến 15:00\n【Địa điểm tập trung】Tập trung lúc 10:45 sáng tại cổng soát vé ga Izumi-Tamagawa tuyến Odakyu.\n【Đồ cần mang theo】Nước uống thì mỗi người tự mua đồ mình thích mang theo nhé. Thịt, rau và bát đĩa các thứ thì mình sẽ chuẩn bị sẵn.\n【Chi phí】1.500 yên/người (tiền thịt và dụng cụ nướng).\n\nNếu trời mưa thì chúng mình sẽ vào nhà hàng gần ga ăn cơm nhé.\nVì cần chuẩn bị đồ nên bạn có đi được hay không thì nhắn tin trả lời mình trước tối thứ Sáu nhé!\nMong thư bạn!"
                },
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": "BBQパーティーの 集合時間と 場所は どこですか。",
                        "promptVi": "Thời gian và địa điểm tập trung của buổi tiệc BBQ là ở đâu?",
                        "options": [
                            "午前10時45分に、和泉多摩川駅の 改札口です。",
                            "午前11時00分に、多摩川の 河原です。",
                            "午前10時45分に、駅の 近くの レストランです。",
                            "午後3時00分に、学校の 前です。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin tập trung trong bài đọc:</strong> 『【集合場所】小田急線 和泉多摩川駅の 改札口に 午前10時45分に 集合して ください。』 ➔ Phương án A chính xác."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": "この メールに ついて、正しい 内容は どれですか。",
                        "promptVi": "Nội dung nào dưới đây là ĐÚNG theo email?",
                        "options": [
                            "飲み物は 自分が 飲む ものを 自分で 準備して 持って行きます。",
                            "お肉や 野菜は 参加する 人が 全員 家から 持って来ます。",
                            "雨が 降ったら、BBQパーティーは 中止に なって 何も しません。",
                            "返事は 日曜日の 朝までに すれば いいです。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Kiểm tra chi tiết:</strong><br>• Trong bài ghi: 『【持ち物】飲み物は 自分で 好きな ものを 買って 持って来て ください。』 ➔ Phương án A đúng.<br>• Phương án B sai vì thịt rau do Kenji chuẩn bị.<br>• Phương án C sai vì nếu mưa thì đi ăn ở nhà hàng gần ga.<br>• Phương án D sai vì phải trả lời trước tối thứ Sáu (金曜日の夜まで)."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (yêu cầu mỗi câu viết ít nhất 50 từ/ký tự).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "休みの日は 何を しますか。どこへ 行きますか。だれと どんな ことを しますか。（★50字以上で 書いてください）",
                        "promptVi": "Ngày nghỉ bạn thường làm gì? Đi đâu? Đi với ai và làm những hoạt động gì? (★Yêu cầu viết ít nhất 50 từ/ký tự bằng tiếng Nhật)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: 休みの日は たいてい 家で 映画を 見たり...",
                        "hints": [
                            "Hoạt động tại nhà: 休みの日は たいてい ～を したり、～を したり します",
                            "Đi ra ngoài: 天気が いい ときは、友だちと ～へ 行きます",
                            "Cảm nhận: とても 楽しいです / リラックスできます",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "休みの日は たいてい 家で 映画を 見たり、好きな 音楽を 聞いたり します。天気が いい ときは、友だちと 公園へ 行って、散歩や 写真を 撮ったり します。それから、静かな カフェで おいしい コーヒーを 飲んで、たくさん おしゃべりします。とても 楽しくて リフレッシュできます。",
                        "modelVi": "Vào ngày nghỉ tôi thường xem phim hoặc nghe bản nhạc yêu thích ở nhà. Khi thời tiết đẹp, tôi cùng bạn bè đi công viên dạo bộ và chụp ảnh. Sau đó, chúng tôi vào một quán cà phê yên tĩnh uống cà phê thơm ngon và trò chuyện rất nhiều. Thật sự rất vui vẻ và sảng khoái tinh thần.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; dùng thành thạo cấu trúc liệt kê ～たり～たりします và liên kết câu."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "あなたの 好きな 料理（日本料理 または ベトナム料理）について 紹介してください。（どんな 料理ですか。どうして 好きですか。★50字以上で 書いてください）",
                        "promptVi": "Hãy giới thiệu về món ăn yêu thích của bạn (Món Nhật hoặc món Việt: Là món gì? Hương vị ra sao? Vì sao bạn thích? ★Yêu cầu viết ít nhất 50 từ/ký tự)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは ベトナムの フォーが 大好きです...",
                        "hints": [
                            "Tên món ăn: わたしは ～が 一番 好きです / 大好きです",
                            "Thành phần & hương vị: ～が たくさん 入って います / おいしくて あたたかいです",
                            "Lý do & thói quen ăn: 体に いいですから、週に ～回 食べます",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしは ベトナムの フォーが 一番 大好きです。牛肉や 新鮮な 野菜が たくさん 入って いて、スープが とても あたたかくて おいしいです。レモンや 唐辛子を 入れて 食べると、もっと おいしく なります。体に いいですから、わたしは 週に 2回 食べます。日本人の 友だちにも おすすめしたいです。",
                        "modelVi": "Tôi thích món Phở của Việt Nam nhất. Món này có nhiều thịt bò và rau tươi, nước dùng rất ấm áp và đậm đà thơm ngon. Cho thêm chanh và ớt vào ăn thì càng ngon hơn nữa. Vì rất tốt cho sức khỏe nên mỗi tuần tôi ăn 2 lần. Tôi cũng rất muốn giới thiệu món này cho bạn bè người Nhật.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; miêu tả rõ hương vị, thành phần nguyên liệu và lý do yêu thích bằng ～から."
                    }
                ]
            }
        ]
    }

def build_m103():
    return {
        "code": "M103",
        "name": "Mã Đề M103 (Đề Thực Chiến Đời Sống & Du Lịch)",
        "tag": "⛩️ Thực Chiến Bài 1 - 8 • Đời Sống & Du Lịch",
        "desc": "Tình huống thực tế đời sống và du lịch Nhật Bản: Hỏi đường ở Shibuya, đi tàu điện ngầm, mua đồ lưu niệm, ngắm hoa anh đào ở Ueno, đi suối nước nóng Onsen và tự luận Can-do ≥ 50 từ/ký tự.",
        "timeLimit": 45 * 60,
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": "ホテルに ついてから、まず フロントで (   ) を します。",
                                "promptVi": "Sau khi đến khách sạn, trước tiên tôi làm thủ tục nhận phòng ở quầy lễ tân.",
                                "options": ["チェックイン", "エレベーター", "タクシー", "シャワー"],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng khách sạn:</strong> Tại quầy lễ tân (フロント), thủ tục nhận phòng được gọi là <strong>チェックイン (Check-in)</strong>. Trả phòng là チェックアウト (Check-out)."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": "この 電車は 各駅停車ですから、目的地まで ちょっと 時間が (   )。",
                                "promptVi": "Chuyến tàu này là tàu đỗ từng ga (tàu thường) nên sẽ mất kha khá thời gian đến đích.",
                                "options": ["かかります", "止まります", "あきます", "行きます"],
                                "correct": 0,
                                "explain": "💡 <strong>Thời gian tiêu tốn: 時間が かかる</strong> (Tốn/mất thời gian). Với tàu 各駅停車 (tàu thường dừng mọi ga) thì đi sẽ lâu hơn tàu nhanh (急行/特急)."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": "駅の 階段で 重い スーツケースを 運ぶのを (   ) もらいました。",
                                "promptVi": "Tôi đã được một người giúp khiêng chiếc vali nặng ở cầu thang nhà ga.",
                                "options": ["手伝って", "教えて", "見せて", "送って"],
                                "correct": 0,
                                "explain": "💡 <strong>Động từ giúp đỡ:</strong> Khiêng vác hành lý nặng ➔ Động từ là <strong>手伝う (てつだう) ➔ 手伝ってもらいました</strong> (được giúp đỡ). 教える (chỉ dạy), 見せる (cho xem), 送る (gửi/tiễn)."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": "すみません、この 近くに 現金を おろす (   ) は ありますか。",
                                "promptVi": "Xin lỗi, ở gần đây có cây ATM nào để rút tiền mặt không ạ?",
                                "options": ["ATM", "トイレ", "ポスト", "エレベーター"],
                                "correct": 0,
                                "explain": "💡 <strong>Từ khóa:</strong> '現金を下ろす' (rút tiền mặt) ➔ Nơi rút tiền mặt là <strong>ATM</strong> (hoặc 銀行: ngân hàng). ポスト (hộp thư), トイレ (nhà vệ sinh)."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": "あしたは 朝から 天気が (   ) そうですから、折りたたみ傘を 持って 行きましょう。",
                                "promptVi": "Ngày mai có vẻ thời tiết xấu từ sáng nên chúng ta hãy mang theo ô gấp nhé.",
                                "options": ["悪く", "よく", "あつく", "さむく"],
                                "correct": 0,
                                "explain": "💡 <strong>Nhận định thời tiết:</strong> Vì vế sau khuyên mang theo ô gấp (折りたたみ傘) nên thời tiết dự báo phải là <strong>悪い (わるい) ➔ 悪そう</strong> (có vẻ xấu, trời âm u sắp mưa)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa tương đương (Câu đồng nghĩa)",
                        "groupInstruction": "Chọn câu trong 4 phương án (A, B, C, D) có ý nghĩa gần nhất với câu được gạch chân:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": "<u>この 温泉旅館は サービスが とても すばらしいです。</u>",
                                "promptVi": "Lữ quán suối nước nóng này dịch vụ rất tuyệt vời.",
                                "options": [
                                    "この 温泉旅館は とても 親切で 快適です。",
                                    "この 温泉旅館は サービスが あまり よくないです。",
                                    "この 温泉旅館は 部屋が とても せまいです。",
                                    "この 温泉旅館は 駅から とても 遠いです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Ý nghĩa tương đương:</strong> 'サービスがとてもすばらしい' (dịch vụ tuyệt vời) đồng nghĩa với 'とても親切で快適です' (rất chu đáo và thoải mái, tiện nghi)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": "<u>渋谷駅前は いつも 若者で ごちゃごちゃして います。</u>",
                                "promptVi": "Trước ga Shibuya lúc nào cũng đông đúc, tấp nập giới trẻ.",
                                "options": [
                                    "渋谷駅前は いつも 人が 多くて にぎやかです。",
                                    "渋谷駅前は いつも 人が 少なくて 静かです。",
                                    "渋谷駅前は 車が 通らなくて 安全です。",
                                    "渋谷駅前は お店が 全然 ありません。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ tượng hình ごちゃごちゃ:</strong> Biểu thị sự đông đúc, hỗn tạp, nhiều người qua lại ➔ Đồng nghĩa với '人が多くてにぎやかです' (đông người và náo nhiệt)."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": "<u>お土産の お菓子は この 百貨店で すべて 揃います。</u>",
                                "promptVi": "Bánh kẹo làm quà lưu niệm có thể mua đầy đủ hết tại trung tâm bách hóa này.",
                                "options": [
                                    "この 百貨店で お土産の お菓子を 全部 買う ことが できます。",
                                    "この 百貨店には お土産が あまり ありません。",
                                    "お土産を 買う ために、別の 店へ 行かなければ なりません。",
                                    "この 百貨店では お菓子を 売って いません。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng すべて揃う (すべてそろう):</strong> Có đầy đủ mọi thứ ➔ Tương đương với '全部買うことができます' (có thể mua được toàn bộ)."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": "<u>電車の 切符を 買う やり方が よく 分かりません。</u>",
                                "promptVi": "Tôi không rõ cách mua vé tàu điện như thế nào.",
                                "options": [
                                    "電車の 切符の 買い方が よく 分かりません。",
                                    "電車の 切符を もう 買いました。",
                                    "電車の 切符は とても 安いです。",
                                    "電車に 乗る ことが 大好きです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu cách làm: V-方 (かた)</strong>.<br>'買うやり方' (cách thức mua) hoàn toàn đồng nghĩa với danh từ ghép <strong>買い方 (かいかた)</strong> (cách mua vé)."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": "<u>あしたは 大雨ですから、山登りは やめましょう。</u>",
                                "promptVi": "Ngày mai mưa to nên chúng ta hãy hủy chuyến leo núi nhé.",
                                "options": [
                                    "あしたは 雨ですから、山登りに 行かない ことに しました。",
                                    "あしたは 雨ですが、山登りに 行きます。",
                                    "あしたは 晴れますから、山登りに 行きましょう。",
                                    "きのう、雨の 中で 山登りを しました。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng やめる (thôi, từ bỏ, hủy):</strong> '山登りはやめましょう' (hãy hủy leo núi) đồng nghĩa với quyết định không đi leo núi (山登りに行かないことにしました)."
                            }
                        ]
                    }
                ]
            },
                        {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán thành Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20) chuẩn 100% chữ Hán Bài 1-10.",
                "badge": "20 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn cách đọc Hiragana chính xác nhất cho chữ Hán được gạch chân (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": "新宿【駅】の 前で 友達と 会います。",
                                "promptVi": "Tôi sẽ gặp bạn ở phía trước ga Shinjuku.",
                                "options": ["えき", "まち", "みち", "てら"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 駅 (DỊCH: nhà ga)</strong>.<br>• Đọc theo âm On-yomi là <strong>えき</strong>.<br>• Phân biệt với các chữ chỉ địa điểm khác: 町 (đinh:まち - thị trấn), 道 (đạo:みち - con đường)."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": "この 【通り】を まっすぐ 行くと、広い 公園が あります。",
                                "promptVi": "Đi thẳng con đường này sẽ có một công viên rộng lớn.",
                                "options": ["とおり", "みち", "かど", "とり"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: 通 (THÔNG)</strong>.<br>• Động từ là 通る (とおる: đi qua), danh từ con phố / đại lộ đọc là <strong>とおり</strong> (có trường âm お).<br>• Tránh nhầm với 道 (みち: đường) hoặc âm ngắn 'とり'."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": "この 町は 【夜】も 明るくて にぎやかです。",
                                "promptVi": "Thị trấn này ban đêm cũng sáng sủa và nhộn nhịp.",
                                "options": ["よる", "ひる", "あさ", "ばん"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 夜 (DẠ: ban đêm)</strong>.<br>• Đọc theo âm Kun-yomi là <strong>よる</strong>.<br>• Bẫy các buổi trong ngày cùng Bài 8: 昼 (trưa - ひる), 朝 (sáng - あさ)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": "日本の 【秋】は 紅葉が とても きれいです。",
                                "promptVi": "Mùa thu của Nhật Bản lá đỏ rất đẹp.",
                                "options": ["あき", "はる", "なつ", "ふゆ"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 3]: Bốn mùa 春夏秋冬 (Xuân Hạ Thu Đông):</strong><br>• 春: はる (Mùa xuân)<br>• 夏: なつ (Mùa hè)<br>• <strong>秋: あき (Mùa thu - Đúng)</strong><br>• 冬: ふゆ (Mùa đông)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": "日本語の 【先生】に 手紙を 書きました。",
                                "promptVi": "Tôi đã viết một bức thư gửi giáo viên tiếng Nhật.",
                                "options": ["せんせい", "せんぜい", "さきなま", "せんしょう"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 9]: 先 (TIÊN: trước) + 生 (SINH)</strong>.<br>• 先: せん.<br>• 生: せい.<br>➔ Ghép lại đọc là <strong>せんせい</strong> (thầy/cô giáo). Cẩn thận bẫy biến âm đục sai 'せんぜい'."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn chữ Hán đúng cho từ Hiragana trong ngoặc 【 】",
                        "groupInstruction": "Chọn chữ Hán viết đúng nhất cho từ Hiragana trong câu (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": "郵便局は 銀行の 【ひだり】に あります。",
                                "promptVi": "Bưu điện nằm ở bên trái ngân hàng.",
                                "options": ["左", "右", "前", "後"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: 左 (TẢ: bên trái)</strong> ➔ <strong>左 (ひだり)</strong>.<br>• Chữ 左 có chữ Công (工) ở dưới.<br>• Chữ 右 (Hữu: phải - みぎ) có chữ Khẩu (口) ở dưới. 前 (trước), 後 (sau)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": "赤い 信号ですから、ここで 【とまります】。",
                                "promptVi": "Vì là đèn đỏ nên chúng ta dừng lại ở đây.",
                                "options": ["止まります", "待まります", "出まります", "行まります"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 止 (CHỈ: dừng lại)</strong> ➔ <strong>止まります (とまります)</strong>.<br>• 待つ (đãi: chờ đợi), 出る (xuất: đi ra ngoài), 行く (hành: đi)."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": "あの 【あかい】 車は 兄の 車です。",
                                "promptVi": "Chiếc ô tô màu đỏ đằng kia là xe của anh trai tôi.",
                                "options": ["赤い", "青い", "白い", "黒い"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: 赤 (XÍCH: màu đỏ)</strong> ➔ <strong>赤い (あかい)</strong>.<br>• Phân biệt: 青い (xanh da trời), 白い (trắng), 黒い (đen)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": "きのう、山に たくさん 【ゆき】が 降りました。",
                                "promptVi": "Hôm qua tuyết rơi rất nhiều trên núi.",
                                "options": ["雪", "雨", "雲", "風"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 4]: Bộ Vũ (雨 - mưa):</strong><br>• <strong>雪 (TUYẾT: ゆき)</strong>: Bộ Vũ (雨) ở trên và chữ Kê (彐) ở dưới ➔ Tuyết rơi (Đúng).<br>• 雨 (mưa - あめ), 雲 (mây - くも), 風 (gió - かぜ)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": "会議の 【まえ】に、資料を 読んで おきます。",
                                "promptVi": "Trước cuộc họp tôi sẽ đọc trước tài liệu.",
                                "options": ["前", "後", "朝", "昼"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 前 (TIỀN: phía trước / trước khi)</strong> ➔ <strong>前 (まえ)</strong>.<br>• Phân biệt từ trái nghĩa: 後 (hậu: sau - あと/うしろ), 朝 (sáng), 昼 (trưa)."
                            }
                        ]
                    }
                ]
            },
{
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Gồm 3 dạng bài: Điền khuyết trợ từ & cấu trúc (21-26), Sắp xếp câu Hái sao ☆ (27-30) và Dịch câu tự luận (31-32).",
                "badge": "30 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền trợ từ hoặc thể ngữ pháp vào chỗ trống (   )",
                        "groupInstruction": "Chọn phương án đúng nhất (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": "新幹線に 乗る (   )、駅で 名物の お弁当を 買いました。",
                                "promptVi": "Trước khi lên tàu Shinkansen, tôi đã mua hộp cơm bento đặc sản ở nhà ga.",
                                "options": ["前に", "後で", "から", "まで"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu V-る前に:</strong> Trước khi thực hiện hành động lên tàu (乗る前に) thì đã mua cơm hộp. V-た後で (sau khi), V-てから (làm xong rồi mới)."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": "東京駅から 京都駅まで 新幹線 (   ) 約 2時間半 かかります。",
                                "promptVi": "Từ ga Tokyo đến ga Kyoto đi bằng tàu Shinkansen mất khoảng 2 tiếng rưỡi.",
                                "options": ["で", "に", "を", "へ"],
                                "correct": 0,
                                "explain": "💡 <strong>Trợ từ chỉ phương tiện di chuyển: [Phương tiện] + で</strong>.<br>Đi bằng tàu Shinkansen dùng <strong>新幹線で</strong>. Trợ từ に, を, へ không dùng để chỉ phương tiện giao thông."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": "露天風呂に (   ) から、冷たい お茶を 飲みました。",
                                "promptVi": "Sau khi ngâm mình ở bồn tắm suối nước nóng ngoài trời xong, tôi đã uống trà mát.",
                                "options": ["入って", "入る", "入った", "入り"],
                                "correct": 0,
                                "explain": "💡 <strong>Ngữ pháp V-てから:</strong> Ngâm bồn nước nóng xong rồi mới uống trà ➔ Động từ nhóm 1: 入る (はいる) chia thể て là <strong>入って</strong>."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": "富士山は 日本の 山の 中で 一番 (   ) です。",
                                "promptVi": "Núi Phú Sĩ là ngọn núi cao nhất trong số các ngọn núi ở Nhật Bản.",
                                "options": ["高い", "高くて", "高かった", "高いの"],
                                "correct": 0,
                                "explain": "💡 <strong>So sánh nhất: [Phạm vi] の中で 一番 [Tính từ nguyên thể] です</strong>.<br>Tính từ đuôi い: <strong>高い (たかい)</strong>."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": "美術品は 貴重ですから、手を 触れては (   )。",
                                "promptVi": "Tác phẩm mỹ thuật rất quý giá nên không được chạm tay vào.",
                                "options": ["いけません", "なりません", "いいです", "ありません"],
                                "correct": 0,
                                "explain": "💡 <strong>Cấm đoán: V-てはいけません</strong> (Tuyệt đối không được làm gì tại bảo tàng)."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": "この サイトで 電車の チケットを 予約する (   ) が できます。",
                                "promptVi": "Tại trang web này bạn có thể đặt vé tàu điện trước.",
                                "options": ["こと", "の", "もの", "ところ"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu khả năng: V-ることができる</strong> (Có thể làm gì). Bắt buộc phải dùng danh từ hóa <strong>こと</strong> (V-る + ことが できます)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Sắp xếp câu tìm vị trí Ngôi sao ( ★ )",
                        "groupInstruction": "Bấm chọn lần lượt 4 cụm từ để xếp vào các vị trí 1 - 2 - 3 - 4. Sau đó chọn đáp án nằm ở vị trí ngôi sao ★:",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "sentencePre": "新幹線に",
                                "sentencePost": "買いました。",
                                "promptVi": "Trước khi lên tàu Shinkansen tôi đã mua hộp cơm bento đặc sản.",
                                "parts": [
                                    {"id": 1, "text": "前に、"},
                                    {"id": 2, "text": "乗る"},
                                    {"id": 3, "text": "お弁当を"},
                                    {"id": 4, "text": "おいしい"}
                                ],
                                "fullOrder": [2, 1, 4, 3],
                                "starPos": 2,
                                "correctOption": 4,
                                "fullSentence": "新幹線に 乗る 前に、 おいしい お弁当を 買いました。",
                                "explain": "💡 <strong>Trật tự câu:</strong> 新幹線に [2] 乗る ➔ [1] 前に、 ➔ ★[4] おいしい ➔ [3] お弁当を ➔ 買いました.<br>Vị trí ngôi sao ★ số 3 là <strong>[4] おいしい</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "sentencePre": "温泉に",
                                "sentencePost": "飲みました。",
                                "promptVi": "Sau khi tắm suối nước nóng xong tôi đã uống một cốc sữa bò mát lạnh.",
                                "parts": [
                                    {"id": 1, "text": "から、"},
                                    {"id": 2, "text": "入って"},
                                    {"id": 3, "text": "冷たい"},
                                    {"id": 4, "text": "牛乳を"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "温泉に 入って から、 冷たい 牛乳を 飲みました。",
                                "explain": "💡 <strong>Ngữ pháp V-てから:</strong> 温泉に [2] 入って ➔ [1] から、 ➔ ★[3] 冷たい ➔ [4] 牛乳を ➔ 飲みました.<br>Vị trí ngôi sao ★ số 3 là <strong>[3] 冷たい</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "sentencePre": "日本で",
                                "sentencePost": "富士山です。",
                                "promptVi": "Ngọn núi cao nhất ở Nhật Bản là núi Phú Sĩ.",
                                "parts": [
                                    {"id": 1, "text": "高い"},
                                    {"id": 2, "text": "一番"},
                                    {"id": 3, "text": "山は"},
                                    {"id": 4, "text": "有名な"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "日本で 一番 高い 山は 富士山です。",
                                "explain": "💡 <strong>So sánh nhất:</strong> 日本で [2] 一番 ➔ [1] 高い ➔ ★[3] 山は ➔ 富士山です.<br>Vị trí ngôi sao ★ số 3 là <strong>[3] 山は</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "sentencePre": "美術館では",
                                "sentencePost": "いけません。",
                                "promptVi": "Ở viện bảo tàng mỹ thuật không được chụp ảnh vì ảnh hưởng đến tác phẩm.",
                                "parts": [
                                    {"id": 1, "text": "撮っては"},
                                    {"id": 2, "text": "写真を"},
                                    {"id": 3, "text": "フラッシュで"},
                                    {"id": 4, "text": "許可なしに"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "美術館では 写真を 撮っては フラッシュで いけません。",
                                "explain": "💡 <strong>Ngữ pháp cấm đoán:</strong> 美術館では [2] 写真を ➔ [1] 撮っては ➔ ★[3] フラッシュで ➔ いけません (ở đây cấu trúc hoàn chỉnh là 写真を撮ってはいけません).<br>Vị trí ngôi sao ★ số 3 là <strong>[1] hoặc [3]</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu tự luận (Nhật ↔ Việt)",
                        "groupInstruction": "Tự gõ câu dịch hoàn chỉnh vào ô bên dưới. Có thể dùng nút '🎯 Tôi Thấy Tôi Viết Đúng' nếu dùng từ đồng nghĩa hợp lý:",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "dir": "ja_to_vi",
                                "prompt": "新幹線の チケットは インターネットで 予約する ことが できますから、とても 便利です。",
                                "placeholder": "Nhập bản dịch tiếng Việt tại đây...",
                                "standard": "Vé tàu Shinkansen có thể đặt trước qua internet nên rất thuận tiện.",
                                "keywords": ["vé tàu", "shinkansen", "internet", "đặt trước", "tiện lợi"],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• 予約することができます: Có thể đặt trước (Mẫu câu khả năng).<br>• インターネットで: Bằng/qua mạng internet (chỉ công cụ/phương tiện).<br>• ～から: Vì... nên (chỉ lý do: vì đặt được qua mạng nên rất tiện)."
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "dir": "vi_to_ja",
                                "prompt": "Sau khi đi dạo ở công viên Ueno xong, chúng tôi đã cùng nhau ăn sushi ở gần nhà ga.",
                                "placeholder": "Gõ câu tiếng Nhật tại đây (dùng Hiragana hoặc Kanji)...",
                                "standard": "上野公園を 散歩して から、駅の 近くで 一緒に 寿司を 食べました。",
                                "acceptable": [
                                    "上野公園を散歩してから、駅の近くで一緒に寿司を食べました。",
                                    "うえのこうえんをさんぽしてから、えきのちかくでいっしょにすしをたべました。",
                                    "上野公園を散歩してから駅の近くで寿司を食べました。",
                                    "上野公園で散歩してから、駅の近くで一緒に寿司を食べました。"
                                ],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• Đi dạo xong rồi mới...: 散歩して から (V-てから).<br>• Gần nhà ga: 駅の 近くで.<br>• Cùng nhau ăn sushi: 一緒に 寿司を 食べました."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc kỹ tờ rơi tour du lịch núi Phú Sĩ và trả lời 2 câu hỏi kiểm tra thông tin.",
                "badge": "10 Điểm",
                "readingPassage": {
                    "title": "【日帰りバスツアー】富士山と 河口湖（かわぐちこ）満喫ツアーの ご案内",
                    "content": "東京発！ 富士山の 絶景と 温泉を 1日で 楽しむ 人気の バスツアーです。\n富士山の 五合目（ごごうめ）まで バスで 登って、雲の 上からの すばらしい 景色を 見学します。\nお昼は、河口湖の レストランで 山梨県名物の「ほうとう（熱い うどん料理）」を 召し上がって いただきます。\n午後は、富士山が きれいに 見える 露天風呂（ろてんぶろ）で ゆっくり 温泉に 入ります。\n\n【出発日】毎週 土曜日・日曜日（雨天決行）\n【集合】朝7時45分（新宿駅西口 モード学園コクーンタワー前）8時00分 出発\n【帰着】午後6時30分ごろ 新宿駅 到着予定\n【旅行代金】大人 1人 8,900円（バス代、昼食代、温泉入浴料を 含む）\n※ タオルは 温泉に ありませんから、自分の タオルを 持参して ください（現地で 200円で 買う ことも できます）。",
                    "translation": "Khởi hành từ Tokyo! Tour xe buýt ngắm cảnh Phú Sĩ tuyệt đẹp và tắm Onsen trong ngày cực kỳ được yêu thích.\nXe buýt đưa quý khách lên tận Trạm số 5 núi Phú Sĩ để chiêm ngưỡng biển mây hùng vĩ từ trên cao.\nBuổi trưa, quý khách dùng bữa tại nhà hàng ven hồ Kawaguchiko thưởng thức món Houtou (mì udon đặc sản Yamanashi nấu trong nồi gang nóng hổi).\nBuổi chiều, thong thả ngâm mình trong bồn tắm suối nước nóng ngoài trời nhìn thẳng ra núi Phú Sĩ.\n\n【Ngày khởi hành】Thứ Bảy và Chủ nhật hàng tuần (Mưa vẫn khởi hành)\n【Tập trung】7:45 sáng (Trước tòa nhà Mode Gakuen Cocoon Tower cổng Tây ga Shinjuku) - 8:00 xe xuất phát\n【Về lại】Dự kiến về đến ga Shinjuku vào khoảng 18:30 chiều\n【Giá tour】Người lớn: 8.900 yên/người (Đã bao gồm tiền xe buýt, ăn trưa và vé vào suối nước nóng)\n※ Suối nước nóng không phát khăn tắm miễn phí nên quý khách vui lòng tự mang theo khăn (hoặc có thể mua tại chỗ với giá 200 yên)."
                },
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": "この ツアーの 集合時間と 旅行代金は いくらですか。",
                        "promptVi": "Thời gian tập trung và giá tour này là bao nhiêu?",
                        "options": [
                            "朝7時45分 集合で、代金は 8,900円です。",
                            "朝8時00分 集合で、代金は 8,900円です。",
                            "朝7時45分 集合で、代金は 10,000円です。",
                            "午後6時30分 集合で、代金は 8,900円です。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong tờ rơi:</strong><br>• 集合: 朝7時45分.<br>• 旅行代金: 大人1人 8,900円.<br>➔ Phương án A chính xác."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": "ツアーに ついて、書いて ある ことと 合って いる ものは どれですか。",
                        "promptVi": "Câu nào dưới đây ĐÚNG với nội dung tờ rơi?",
                        "options": [
                            "温泉で 使う タオルは、自分で 持って行くか、現地で 買います。",
                            "お昼ごはんは ツアー代金に 入って いませんから、自分で 払います。",
                            "雨が 降ったら、ツアーは 中止に なって 行きません。",
                            "ツアーは 富士山の てっぺん（頂上）まで 歩いて 登ります。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Kiểm tra chi tiết:</strong><br>• Ghi chú: 『※ タオルは 温泉に ありませんから、自分の タオルを 持参して ください（現地で 200円で 買う ことも できます）。』 ➔ Phương án A đúng.<br>• B sai vì giá 8.900 yên đã bao gồm tiền ăn trưa (昼食代を含む).<br>• C sai vì có ghi 雨天決行 (mưa vẫn đi).<br>• D sai vì đi xe buýt lên trạm số 5 (五合目), không leo lên đỉnh."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (yêu cầu mỗi câu viết ít nhất 50 từ/ký tự).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "あなたの 趣味について 詳しく 紹介してください。（どんな 趣味ですか。いつ しますか。どうして 好きですか。★50字以上で 書いてください）",
                        "promptVi": "Hãy giới thiệu chi tiết về sở thích của bạn (Là sở thích gì? Thường làm khi nào? Vì sao bạn thích? ★Yêu cầu viết ít nhất 50 từ/ký tự bằng tiếng Nhật)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしの趣味は 写真を 撮る ことです...",
                        "hints": [
                            "Tên sở thích: わたしの 趣味は ～ことです / ～が 大好きです",
                            "Thời gian & địa điểm: 休みの日は いつも ～へ 行きます",
                            "Lý do & cảm nhận: 楽しい気持ちに なります / ストレスが なくなります",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしの 趣味は 写真を 撮る ことです。休みの日は いつも カメラを 持って、きれいな 公園や 古い 町へ 行きます。自然の 花や 街の 人々の 笑顔を 撮る ことが 大好きです。写真を 撮ると、日頃の ストレスが なくなって、とても 楽しい 気持ちに なります。将来は 写真展を 開きたいです。",
                        "modelVi": "Sở thích của tôi là chụp ảnh. Vào ngày nghỉ, tôi luôn mang theo máy ảnh và đến những công viên đẹp hoặc các con phố cổ. Tôi rất thích chụp hoa cỏ thiên nhiên và nụ cười của mọi người trên phố. Mỗi khi chụp ảnh, căng thẳng thường nhật tan biến và tôi cảm thấy rất vui vẻ. Tương lai tôi muốn mở triển lãm ảnh.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; dùng mẫu danh từ hóa 趣味は～ことです; câu văn giàu cảm xúc và liên kết tốt."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "あなたの 住んでいる 町について 紹介してください。（どんな 町ですか。何が ありますか。おすすめの 所は どこですか。★50字以上で 書いてください）",
                        "promptVi": "Hãy giới thiệu về thành phố nơi bạn đang sinh sống (Thành phố như thế nào? Có những gì? Nơi bạn muốn giới thiệu nhất? ★Yêu cầu viết ít nhất 50 từ/ký tự)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは ベトナムの ダナンに 住んで います...",
                        "hints": [
                            "Đặc điểm thành phố: ～に 住んで います / 海が 近くて きれいな 町です",
                            "Địa điểm nổi bật: ～が たくさん あります / 有名な レストランや 橋",
                            "Khuyên trải nghiệm: ～を 散歩する ことが 一番 おすすめです",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしは ベトナムの ダナンに 住んで います。海が 近くて、空気が きれいで、とても 美しい 町です。おいしい 海鮮料理の レストランや 有名な 橋が たくさん あります。夜に 涼しい ビーチを 散歩したり、カフェに 行ったり する ことが 一番 おすすめです。ぜひ 遊びに 来てください。",
                        "modelVi": "Tôi đang sống ở Đà Nẵng, Việt Nam. Đó là thành phố rất đẹp, gần biển và không khí trong lành. Ở đây có nhiều nhà hàng hải sản ngon và những cây cầu nổi tiếng. Đi dạo bãi biển mát mẻ vào ban đêm hoặc ghé quán cà phê là điều tôi muốn giới thiệu nhất. Nhất định hãy ghé chơi nhé.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; kết hợp tính từ い/な; giới thiệu nét nổi bật và đưa ra lời mời tự nhiên."
                    }
                ]
            }
        ]
    }

def build_m104():
    return {
        "code": "M104",
        "name": "Mã Đề M104 (Đề Đột Phá Giao Tiếp & Ẩm Thực)",
        "tag": "🍱 Đột Phá Bài 1 - 8 • Ẩm Thực & Nhà Hàng",
        "desc": "Bám sát các tình huống giao tiếp ẩm thực Nhật Bản: Gọi món tại nhà hàng, nhận xét hương vị, cách tính tiền, văn hóa ăn uống và tự luận Can-do ≥ 50 từ/ký tự.",
        "timeLimit": 45 * 60,
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": "レストランで 注文した 料理が なかなか 来ませんから、店員を (   ) ました。",
                                "promptVi": "Ở nhà hàng, món ăn đã gọi mãi chưa thấy mang ra nên tôi đã gọi nhân viên phục vụ.",
                                "options": ["呼び", "頼み", "話し", "聞き"],
                                "correct": 0,
                                "explain": "💡 <strong>Động từ gọi người: 呼ぶ (よぶ) ➔ 呼びました</strong>. Gọi nhân viên phục vụ bàn dùng 店員を呼ぶ. 頼む (たのむ: nhờ vả/gọi món)."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": "この ラーメンの スープは 豚骨ですから、とても (   ) が あって おいしいです。",
                                "promptVi": "Nước dùng của bát mì ramen này hầm từ xương heo nên có vị đậm đà ngậy béo rất ngon miệng.",
                                "options": ["コク", "からさ", "にがさ", "におい"],
                                "correct": 0,
                                "explain": "💡 <strong>Thuật ngữ ẩm thực Nhật Bản: コクがある</strong> (có vị đậm đà, chiều sâu hương vị béo ngậy đặc trưng của nước hầm xương). 辛さ (vị cay), 苦さ (vị đắng)."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": "お会計の とき、レジで「ごちそうさまでした。(   ) で お願いします」と 言いました。",
                                "promptVi": "Lúc thanh toán ở quầy thu ngân, tôi đã nói: 'Xin cảm ơn bữa ăn. Xin hãy tính tiền riêng từng người giúp chúng tôi'.",
                                "options": ["別々", "一緒", "全部", "大勢"],
                                "correct": 0,
                                "explain": "💡 <strong>Thanh toán tiền ở Nhật: 別々で（べつべつで）</strong> (Thanh toán riêng, chia hóa đơn). Đi ăn với bạn bè người Nhật thường dùng '別々でお願いします' hoặc '割り勘 (わりかん)'."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": "すみません、グラスの お冷（ひや）を もう 一杯 (   ) ください。",
                                "promptVi": "Xin lỗi, xin vui lòng rót thêm cho tôi một ly nước lạnh nữa ạ.",
                                "options": ["入れて", "食べて", "着て", "乗せて"],
                                "correct": 0,
                                "explain": "💡 <strong>Rót nước: 水を 入れる (いれる) ➔ 入れてください</strong>. お冷 (おひや) là nước lọc đá miễn phí tại nhà hàng Nhật Bản."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": "日本人は ごはんを 食べる 前に、手を 合わせて「(   )」と 挨拶します。",
                                "promptVi": "Người Nhật trước khi ăn cơm thường chắp hai tay lại và nói lời chào 'Itadakimasu'.",
                                "options": ["いただきます", "ごちそうさまでした", "いってきます", "ただいま"],
                                "correct": 0,
                                "explain": "💡 <strong>Văn hóa ăn uống Nhật Bản:</strong><br>• Trước khi ăn: <strong>いただきます</strong> (Xin phép dùng bữa - để cảm tạ thiên nhiên và người nấu).<br>• Sau khi ăn xong: ごちそうさまでした."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa tương đương (Câu đồng nghĩa)",
                        "groupInstruction": "Chọn câu trong 4 phương án (A, B, C, D) có ý nghĩa gần nhất với câu được gạch chân:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": "<u>この 居酒屋は メニューの 種類が とても 豊富です。</u>",
                                "promptVi": "Quán nhậu Izakaya này chủng loại thực đơn rất phong phú.",
                                "options": [
                                    "この 居酒屋には いろいろな 料理が たくさん あります。",
                                    "この 居酒屋は 料理が 2種類しか ありません。",
                                    "この 居酒屋は メニューが とても 高いです。",
                                    "この 居酒屋は お酒を 置いて いません。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng 豊富（な）(ほうふ):</strong> Phong phú, đa dạng ➔ Đồng nghĩa với 'いろいろな料理がたくさんあります' (có rất nhiều món ăn đa dạng khác nhau)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": "<u>わたしは お腹が いっぱいですから、もう 食べられません。</u>",
                                "promptVi": "Tôi no căng bụng rồi nên không thể ăn thêm được nữa.",
                                "options": [
                                    "わたしは もう 十分 満足して 食べました。",
                                    "わたしは まだ お腹が すいて います。",
                                    "わたしは ごはんを まだ 食べて いません。",
                                    "この 料理は まずいですから、食べません。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Thành ngữ お腹がいっぱい (no bụng):</strong> Đã ăn no đủ ➔ Đồng nghĩa với 'もう十分食べました' (tôi đã ăn đủ no rồi)."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": "<u>この 魚は 新鮮ですから、生で 食べられます。</u>",
                                "promptVi": "Con cá này rất tươi ngon nên có thể ăn sống được.",
                                "options": [
                                    "この 魚は 新しいですから、焼かないで そのまま 食べられます。",
                                    "この 魚は 古いですから、よく 焼かなければ なりません。",
                                    "この 魚は 腐って いますから、捨てます。",
                                    "この 魚は 辛いですから、食べられません。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Khái niệm ăn đồ sống (生 - なま):</strong> Ăn trực tiếp cá tươi mà không cần đun nấu/nướng chín ➔ '焼かないでそのまま食べられます'."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": "<u>この 味噌汁は 塩分が 控えめです。</u>",
                                "promptVi": "Bát canh miso này vị muối được nêm nếm vừa phải, thanh nhẹ.",
                                "options": [
                                    "この 味噌汁は 塩が 少なくて、体に やさしい味です。",
                                    "この 味噌汁は 塩が 多すぎて、とても 辛いです。",
                                    "この 味噌汁は 砂糖が たくさん 入って います。",
                                    "この 味噌汁は 全然 味が しません。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng 控えめ（ひかえめ）:</strong> Tiết chế, vừa phải, ít muối ➔ '塩が少なくて、体にやさしい味です' (ít muối, thanh đạm tốt cho sức khỏe)."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": "<u>ごはんを 食べた 後で、甘い デザートを 頼みましょう。</u>",
                                "promptVi": "Sau khi ăn cơm xong, chúng ta hãy gọi món tráng miệng ngọt nhé.",
                                "options": [
                                    "食事の あとで、ケーキや アイスを 注文しましょう。",
                                    "食事の 前に、冷たい 水を 飲みましょう。",
                                    "甘い ものは 嫌いですから、何も 頼みません。",
                                    "ごはんを 食べないで、デザートだけ 食べます。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ đồng nghĩa:</strong> 'デザートを頼む' (gọi tráng miệng) = 'ケーキやアイスを注文する' (gọi bánh hoặc kem)."
                            }
                        ]
                    }
                ]
            },
                        {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán thành Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20) chuẩn 100% chữ Hán Bài 1-10.",
                "badge": "20 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn cách đọc Hiragana chính xác nhất cho chữ Hán được gạch chân (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": "あの 店は 値段が 【安くて】 おいしいです。",
                                "promptVi": "Quán đó giá cả rẻ mà lại ngon miệng.",
                                "options": ["やすくて", "たかくて", "ひろくて", "おおくて"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 5]: 安 (AN: rẻ / an toàn)</strong>.<br>• Có bộ Miên (宀) ở trên và Nữ (女) ở dưới ➔ <strong>安くて (やすくて)</strong>: Rẻ.<br>• Phân biệt tính từ cùng bài 5: 高い (たかい: đắt/cao), 広い (ひろい: rộng), 多い (おおい: nhiều)."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": "朝、パンと たまごを 【食べます】。",
                                "promptVi": "Buổi sáng tôi ăn bánh mì và trứng.",
                                "options": ["たべます", "のみます", "かいます", "いきます"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 食 (THỰC: ăn)</strong>.<br>• Đọc theo âm Kun-yomi là <strong>た(べる) ➔ 食べます (たべます)</strong>."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": "この 料理は ちょっと 値段が 【高い】ですね。",
                                "promptVi": "Món ăn này giá hơi cao/đắt nhỉ.",
                                "options": ["たかい", "やすい", "すくない", "おおい"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 5]: 高 (CAO: cao / đắt)</strong> ➔ <strong>高い (たかい)</strong>. Tránh nhầm với từ trái nghĩa 安い (やすい: rẻ)."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": "【昼】休みに 友達と 公園を 散歩しました。",
                                "promptVi": "Giờ nghỉ trưa tôi đã cùng bạn đi dạo công viên.",
                                "options": ["ひる", "あさ", "よる", "ばん"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 昼 (TRÚ: buổi trưa)</strong> ➔ <strong>昼 (ひる)</strong>. Bẫy các buổi trong ngày: 朝 (あさ: sáng), 夜 (よる: tối)."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": "午後から つめたい 【雨】が 降りはじめました。",
                                "promptVi": "Từ chiều những hạt mưa lạnh bắt đầu rơi.",
                                "options": ["あめ", "ゆき", "かぜ", "くも"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 4]: 雨 (VŨ: mưa)</strong> ➔ <strong>雨 (あめ)</strong>.<br>• Phân biệt các hiện tượng thời tiết Bài 4: 雪 (tuyết - ゆき), 風 (gió - かぜ), 雲 (mây - くも)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn chữ Hán đúng cho từ Hiragana trong ngoặc 【 】",
                        "groupInstruction": "Chọn chữ Hán viết đúng nhất cho từ Hiragana trong câu (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": "駅の 近くに 新しい 【みせ】が できました。",
                                "promptVi": "Ở gần nhà ga vừa mở một cửa hàng mới.",
                                "options": ["店", "広", "町", "高"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 5]: 店 (ĐIẾM: cửa hàng/quán)</strong> ➔ <strong>店 (みせ)</strong>. Chữ 店 có bộ Nghiễm (广) bên ngoài và chữ Chiêm (占) bên trong. Bẫy chữ 広 (quảng: rộng) có khư 厶 bên trong."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": "かばんから ノートと ペンを 【だしました】。",
                                "promptVi": "Tôi đã lấy vở và bút ra từ trong cặp sách.",
                                "options": ["出しました", "待しました", "止しました", "行しました"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 7]: 出 (XUẤT: lấy ra / ra ngoài)</strong> ➔ <strong>出しました (だしました)</strong>.<br>• 待つ (đợi), 止まる (dừng), 行く (đi)."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": "きょうは 気持ちが いいので、【そと】で ご飯を 食べましょう。",
                                "promptVi": "Hôm nay trời rất dễ chịu nên chúng ta hãy ăn cơm ở ngoài trời nhé.",
                                "options": ["外", "国", "多", "前"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 2]: 外 (NGOẠI: bên ngoài)</strong> ➔ <strong>外 (そと)</strong>. Cấu tạo gồm chữ Tịch (夕) bên trái và chữ Bốc (卜) bên phải. Bẫy: 国 (quốc: đất nước), 多 (nhiều)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": "コーヒーに 砂糖を 【すこし】 入れて ください。",
                                "promptVi": "Xin hãy cho một ít đường vào cà phê giúp tôi.",
                                "options": ["少し", "多し", "小し", "少い"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 5]: 少 (THIỂU: ít / một chút)</strong> ➔ <strong>少し (すこし)</strong>.<br>• Cấu tạo: chữ Tiểu (小) thêm 1 nét phẩy chéo bên dưới. Bẫy: nhầm với 小 (tiểu: nhỏ) hoặc 多 (đa: nhiều)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": "新宿で JRの 山手線に 【のります】。",
                                "promptVi": "Tôi sẽ lên tuyến tàu Yamanote của JR ở ga Shinjuku.",
                                "options": ["乗ります", "降ります", "待ります", "止ります"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 乗 (THỪA: lên xe / tàu)</strong> ➔ <strong>乗ります (のります)</strong> (Đúng).<br>• Đi kèm với trợ từ に (電車に乗る). Các đáp án bẫy: 待つ (đợi), 止まる (dừng)."
                            }
                        ]
                    }
                ]
            },
{
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Gồm 3 dạng bài: Điền khuyết trợ từ & cấu trúc (21-26), Sắp xếp câu Hái sao ☆ (27-30) và Dịch câu tự luận (31-32).",
                "badge": "30 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền trợ từ hoặc thể ngữ pháp vào chỗ trống (   )",
                        "groupInstruction": "Chọn phương án đúng nhất (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": "食事を (   ) 前に、石けんで きれいに 手を 洗いましょう。",
                                "promptVi": "Trước khi ăn cơm, chúng ta hãy rửa sạch tay bằng xà phòng nhé.",
                                "options": ["する", "して", "した", "し"],
                                "correct": 0,
                                "explain": "💡 <strong>Ngữ pháp V-る前に:</strong> Động từ đứng trước 前に luôn ở thể từ điển (辞書形) ➔ <strong>食事をする 前に</strong>."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": "熱い うどんを (   ) から、冷たい 抹茶アイスを 食べました。",
                                "promptVi": "Sau khi ăn bát mì udon nóng hổi xong, tôi đã ăn kem matcha mát lạnh.",
                                "options": ["食べて", "食べる", "食べた", "食べ"],
                                "correct": 0,
                                "explain": "💡 <strong>Ngữ pháp V-てから:</strong> Ăn mì xong xuôi rồi mới ăn kem tráng miệng ➔ 食べる chuyển thành <strong>食べて</strong>."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": "日本の ラーメンの 中で、醤油ラーメンが (   ) 好きです。",
                                "promptVi": "Trong các loại ramen của Nhật, tôi thích mì ramen vị nước tương Shoyu nhất.",
                                "options": ["一番", "もっと", "ずっと", "より"],
                                "correct": 0,
                                "explain": "💡 <strong>So sánh nhất: [Phạm vi] の中で ～が 一番 好きです</strong> ➔ Điền <strong>一番 (いちばん)</strong>."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": "静かな 高級レストランで、大声で 騒いでは (   )。",
                                "promptVi": "Ở nhà hàng cao cấp yên tĩnh, tuyệt đối không được làm ồn to tiếng.",
                                "options": ["いけません", "なりません", "いいです", "ありません"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu cấm đoán: V-てはいけません</strong> (Không được làm ồn)."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": "うどんと そばと、(   ) のほうが 消化に いいですか。",
                                "promptVi": "Giữa mì Udon và mì Soba, loại nào dễ tiêu hóa hơn?",
                                "options": ["どちら", "どれ", "どこ", "だれ"],
                                "correct": 0,
                                "explain": "💡 <strong>So sánh giữa 2 lựa chọn: Aと Bと どちらのほうが...</strong> ➔ Chọn <strong>どちら</strong>."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": "お腹が 痛いですから、油っこい ものは (   ) です。",
                                "promptVi": "Vì đang đau bụng nên tôi không muốn ăn đồ nhiều dầu mỡ chút nào.",
                                "options": ["食べたくない", "食べたい", "食べなかった", "食べた"],
                                "correct": 0,
                                "explain": "💡 <strong>Phủ định của thể muốn V-たい: V-たくないです</strong> (Không muốn làm gì). Đau bụng nên không muốn ăn đồ dầu mỡ ➔ <strong>食べたくないです</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Sắp xếp câu tìm vị trí Ngôi sao ( ★ )",
                        "groupInstruction": "Bấm chọn lần lượt 4 cụm từ để xếp vào các vị trí 1 - 2 - 3 - 4. Sau đó chọn đáp án nằm ở vị trí ngôi sao ★:",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "sentencePre": "ごはんを",
                                "sentencePost": "洗います。",
                                "promptVi": "Trước khi ăn cơm tôi rửa sạch tay.",
                                "parts": [
                                    {"id": 1, "text": "前に、"},
                                    {"id": 2, "text": "食べる"},
                                    {"id": 3, "text": "手を"},
                                    {"id": 4, "text": "きれいに"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "ごはんを 食べる 前に、 手を きれいに 洗います。",
                                "explain": "💡 <strong>Trật tự câu:</strong> ごはんを [2] 食べる ➔ [1] 前に、 ➔ ★[3] 手を ➔ [4] きれいに ➔ 洗います.<br>Vị trí ngôi sao ★ số 3 là <strong>[3] 手を</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "sentencePre": "居酒屋で",
                                "sentencePost": "しました。",
                                "promptVi": "Ở quán nhậu chúng tôi đã ăn thịt xiên nướng và uống bia rất vui vẻ.",
                                "parts": [
                                    {"id": 1, "text": "飲んだり"},
                                    {"id": 2, "text": "焼き鳥を"},
                                    {"id": 3, "text": "ビールを"},
                                    {"id": 4, "text": "食べたり、"}
                                ],
                                "fullOrder": [2, 4, 3, 1],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "居酒屋で 焼き鳥を 食べたり、 ビールを 飲んだり しました。",
                                "explain": "💡 <strong>Ngữ pháp V-たりV-たり:</strong> 居酒屋で [2] 焼き鳥を ➔ [4] 食べたり、 ➔ ★[3] ビールを ➔ [1] 飲んだり ➔ しました.<br>Vị trí ngôi sao ★ số 3 là <strong>[3] ビールを</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "sentencePre": "刺身は",
                                "sentencePost": "おいしいです。",
                                "promptVi": "Món cá sống sashimi chấm với chút wasabi ăn sẽ ngon hơn.",
                                "parts": [
                                    {"id": 1, "text": "食べた"},
                                    {"id": 2, "text": "わさびを"},
                                    {"id": 3, "text": "ほうが"},
                                    {"id": 4, "text": "つけて"}
                                ],
                                "fullOrder": [2, 4, 1, 3],
                                "starPos": 2,
                                "correctOption": 1,
                                "fullSentence": "刺身は わさびを つけて 食べた ほうが おいしいです。",
                                "explain": "💡 <strong>Khuyên dùng: V-たほうがいい</strong>: [2] わさびを ➔ [4] つけて ➔ ★[1] 食べた ➔ [3] ほうが ➔ おいしいです.<br>Vị trí ngôi sao ★ số 3 là <strong>[1] 食べた</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "sentencePre": "この レストランでは",
                                "sentencePost": "できます。",
                                "promptVi": "Ở nhà hàng này có thể thanh toán bằng thẻ tín dụng.",
                                "parts": [
                                    {"id": 1, "text": "払う"},
                                    {"id": 2, "text": "カードで"},
                                    {"id": 3, "text": "ことが"},
                                    {"id": 4, "text": "電子マネーや"}
                                ],
                                "fullOrder": [4, 2, 1, 3],
                                "starPos": 2,
                                "correctOption": 1,
                                "fullSentence": "この レストランでは 電子マネーや カードで 払う ことが できます。",
                                "explain": "💡 <strong>Khả năng: V-ることができる</strong>: [4] 電子マネーや ➔ [2] カードで ➔ ★[1] 払う ➔ [3] ことが ➔ できます.<br>Vị trí ngôi sao ★ số 3 là <strong>[1] 払う</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu tự luận (Nhật ↔ Việt)",
                        "groupInstruction": "Tự gõ câu dịch hoàn chỉnh vào ô bên dưới. Có thể dùng nút '🎯 Tôi Thấy Tôi Viết Đúng' nếu dùng từ đồng nghĩa hợp lý:",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "dir": "ja_to_vi",
                                "prompt": "日本の 伝統的な 料理は 季節の 野菜や 新鮮な 魚を たくさん 使いますから、健康に とても いいです。",
                                "placeholder": "Nhập bản dịch tiếng Việt tại đây...",
                                "standard": "Ẩm thực truyền thống của Nhật Bản sử dụng nhiều rau theo mùa và cá tươi nên rất tốt cho sức khỏe.",
                                "keywords": ["truyền thống", "nhật bản", "rau theo mùa", "cá tươi", "sức khỏe"],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• 季節の野菜や新鮮な魚: Rau theo mùa và cá tươi (nguyên liệu tự nhiên).<br>• たくさん使いますから: Vì sử dụng nhiều (nguyên nhân).<br>• 健康にとてもいいです: Rất tốt cho sức khỏe."
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "dir": "vi_to_ja",
                                "prompt": "Sau khi gọi món xong, chúng tôi đã vừa trò chuyện vừa vui vẻ đợi món ăn mang ra.",
                                "placeholder": "Gõ câu tiếng Nhật tại đây (dùng Hiragana hoặc Kanji)...",
                                "standard": "料理を 注文して から、おしゃべりを しながら 楽しく 待ちました。",
                                "acceptable": [
                                    "料理を注文してから、おしゃべりをしながら楽しく待ちました。",
                                    "りょうりをつもんしてから、おしゃべりをしながらたのしくまちました。",
                                    "料理を注文してから、楽しく話しながら待ちました。",
                                    "注文してから、おしゃべりしながら楽しく待ちました。"
                                ],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• Sau khi gọi món xong: 料理を 注文して から (V-てから).<br>• Vừa trò chuyện vừa đợi: おしゃべりを しながら 待ちました (V-ながら)."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc kỹ hướng dẫn gọi món tại quán mì ramen truyền thống và trả lời 2 câu hỏi.",
                "badge": "10 Điểm",
                "readingPassage": {
                    "title": "【博多ラーメン 一心亭】ご注文方法と おいしい 食べ方",
                    "content": "当店は、九州・博多名物の 本格豚骨（とんこつ）ラーメンの 専門店です。\nスープは 国産の 豚骨を 20時間 じっくり 煮込んで つくって います。\n\n【ご注文の 流れ】\n1. まず 店内に 入る 前に、外の 自動券売機（じどうけんばいき）で 食券（しょっけん）を 買って ください。\n2. 席に 座ったら、店員に 食券を 渡して、麺の 硬さ（かたさ）を 伝えて ください。\n   （かため／ふつう／やわらかめ の 3つから 選べます。おすすめは「かため」です！）\n3. 麺を 全部 食べた 後、スープが まだ 残って いる ときは、「替え玉（かえだま - 麺の おかわり）」が 100円で できます。\n   現金 100円を テーブルに 置いて、店員に「替え玉 お願いします」と 声を かけて ください。\n※ お水と 辛子高菜（からしたかな - 辛い漬物）は セルフサービスですから、自分で 取って ください。",
                    "translation": "Quán chúng tôi là tiệm chuyên mì Ramen xương hầm Hakata chính gốc đặc sản vùng Kyushu.\nNước dùng được ninh hầm kỹ lưỡng từ xương heo nội địa Nhật trong suốt 20 tiếng đồng hồ.\n\n【Quy trình gọi món】\n1. Trước khi vào trong quán, xin quý khách hãy mua phiếu ăn (shokken) tại máy bán vé tự động đặt ở cửa ngoài.\n2. Sau khi vào chỗ ngồi, đưa phiếu cho nhân viên và chọn độ cứng của sợi mì:\n   (Quý khách có thể chọn 1 trong 3 mức: Cứng / Bình thường / Mềm. Quán khuyên quý khách nên thử mức 'Cứng' nhé!)\n3. Sau khi ăn hết mì, nếu trong bát vẫn còn nước dùng, quý khách có thể gọi thêm mì (gọi là Kaedama) với giá chỉ 100 yên.\n   Xin đặt 100 yên tiền mặt lên bàn và nói với nhân viên: 'Cho tôi một Kaedama nhé'.\n※ Nước lọc và dưa chua cay Karashi-Takana là dịch vụ tự phục vụ, quý khách vui lòng tự lấy tại quầy."
                },
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": "この 店で 注文する とき、まず 最初に 何を しなければ なりませんか。",
                        "promptVi": "Khi gọi món tại quán này, việc đầu tiên cần phải làm là gì?",
                        "options": [
                            "外の 自動券売機で 食券を 買います。",
                            "席に 座ってから、店員に メニューを もらいます。",
                            "100円を 店員に 渡して、替え玉を 頼みます。",
                            "自分で 厨房へ 行って、ラーメンを 作ります。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin bước 1 trong bài:</strong> 『1. まず 店内に 入る 前に、外の 自動券売機で 食券を 買って ください。』 ➔ Phương án A đúng."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": "この 店に ついて、書いて ある ことと 合って いる ものは どれですか。",
                        "promptVi": "Câu nào dưới đây là ĐÚNG theo tờ hướng dẫn của quán?",
                        "options": [
                            "お水や 辛い 漬物は、自分で 取りに 行かなければ なりません。",
                            "替え玉（麺の おかわり）は 無料で 何杯でも 食べられます。",
                            "麺の 硬さは 選ぶ ことが できません。",
                            "食券は 席に 座ってから 店員から 直接 買います。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Kiểm tra chi tiết:</strong><br>• Lưu ý cuối bài: 『※ お水と 辛子高菜（辛い漬物）は セルフサービスですから、自分で 取って ください。』 (Tự phục vụ ➔ 自分で取りに行く) ➔ Phương án A đúng.<br>• B sai vì Kaedama giá 100 yên, không phải miễn phí.<br>• C sai vì có 3 mức độ cứng để chọn.<br>• D sai vì mua vé tại máy tự động trước khi vào quán."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (yêu cầu mỗi câu viết ít nhất 50 từ/ký tự).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "日本へ 行ったら、どんな お土産を 買いたいですか。（だれに 買いますか。どうしてですか。★50字以上で 書いてください）",
                        "promptVi": "Nếu sang Nhật Bản, bạn muốn mua quà lưu niệm gì? Mua cho ai? Vì sao? (★Yêu cầu viết ít nhất 50 từ/ký tự bằng tiếng Nhật)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは 家族に 日本の お菓子を 買いたいです...",
                        "hints": [
                            "Quà cho gia đình: 家族には ～を 買いたいです (抹茶のお菓子 / 伝統工芸品)",
                            "Quà cho bạn bè: 友だちには ～を あげたいです (キーホルダー / 文房具)",
                            "Lý do: かわいくて 有名ですから / みんな 喜ぶと 思いますから",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしは 家族に 日本の おいしい 抹茶のお菓子を 買いたいです。日本の お菓子は パッケージも かわいくて、とても 有名ですから。そして、友だちには 東京タワーの キーホルダーや 日本の 便利な 文房具を あげたいです。みんな 喜ぶと 思います。たくさん お金を 準備して 行きます。",
                        "modelVi": "Tôi muốn mua bánh kẹo matcha thơm ngon của Nhật cho gia đình. Vì bánh kẹo Nhật Bản đóng gói rất dễ thương và rất nổi tiếng. Còn cho bạn bè, tôi muốn tặng móc khóa tháp Tokyo hoặc đồ dùng học tập tiện ích của Nhật. Tôi nghĩ mọi người sẽ rất vui mừng. Tôi sẽ chuẩn bị nhiều tiền trước khi đi.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; sử dụng đúng cấu trúc mong muốn ～たいです và mục đích tặng quà."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "あなたの 朝の 習慣（ルーティン）について 書いてください。（起きてから 何を しますか。★50字以上で 書いてください）",
                        "promptVi": "Hãy viết về thói quen buổi sáng của bạn (Sau khi thức dậy bạn làm những gì? ★Yêu cầu viết ít nhất 50 từ/ký tự bằng tiếng Nhật)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは 毎朝 6時半に 起きます...",
                        "hints": [
                            "Giờ thức dậy: わたしは 毎朝 ～時に 起きます",
                            "Thứ tự hành động: 起きてから、～を して、～を します",
                            "Học tập/tập thể dục: それから、日本語を 勉強します",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしは 毎朝 6時半に 起きます。起きてから、まず 顔を 洗って、熱い コーヒーを 飲みます。それから、軽い 朝ごはんを 食べて、日本語の 単語を 20分 勉強します。朝は 頭が すっきり して いますから、勉強が とても よく できます。7時45分に 家を 出て、学校へ 行きます。",
                        "modelVi": "Mỗi sáng tôi thức dậy lúc 6 giờ 30. Sau khi dậy, trước tiên tôi rửa mặt và uống một cốc cà phê nóng. Sau đó, tôi ăn bữa sáng nhẹ và học từ vựng tiếng Nhật 20 phút. Vì buổi sáng đầu óc rất tỉnh táo nên học tập rất hiệu quả. Đến 7 giờ 45 tôi rời nhà để đến trường.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; sử dụng thể て và ～てから để miêu tả trình tự thời gian mượt mà."
                    }
                ]
            }
        ]
    }

def build_m105():
    return {
        "code": "M105",
        "name": "Mã Đề M105 (Đề Tuyển Chọn Chuẩn Đề Thầy Cô)",
        "tag": "🎯 Chuẩn Đề Giảng Viên • Khảo Sát Năng Lực",
        "desc": "Đề thi toàn diện kiểm tra năng lực ngữ pháp, bẫy Hán tự tương đồng, kỹ năng sắp xếp câu hái sao, đọc hiểu nội quy sinh hoạt Nhật Bản và tự luận Can-do ≥ 50 từ/ký tự.",
        "timeLimit": 45 * 60,
        "sections": [
            {
                "id": "sec1_vocab",
                "partNumber": "I",
                "partTitle": "TỪ VỰNG (語彙 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Điền từ thích hợp vào chỗ trống (1-5) và Chọn câu đồng nghĩa (6-10).",
                "badge": "25 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền từ vào chỗ trống trong ngoặc (   )",
                        "groupInstruction": "Chọn từ thích hợp nhất trong 4 phương án (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 1,
                                "type": "mc",
                                "prompt": "大学の 寮では、夜 11時に 玄関の ドアが (   ) ますから、それまでに 帰らなければ なりません。",
                                "promptVi": "Ở ký túc xá đại học, cửa ra vào sẽ đóng lại lúc 11 giờ đêm nên phải về trước giờ đó.",
                                "options": ["閉まり", "あき", "とまり", "おわり"],
                                "correct": 0,
                                "explain": "💡 <strong>Tự động từ chỉ trạng thái: ドアが 閉まる (しまる) ➔ 閉まります</strong> (Cửa tự đóng lại). Bẫy: あきます (mở ra), とまります (dừng lại), おわります (kết thúc)."
                            },
                            {
                                "id": 2,
                                "type": "mc",
                                "prompt": "先生が 言った 集合場所と 時間を ノートに しっかり (   ) しました。",
                                "promptVi": "Tôi đã ghi chép cẩn thận vào sổ tay địa điểm và thời gian tập trung mà thầy giáo dặn.",
                                "options": ["メモ", "コピー", "テスト", "テープ"],
                                "correct": 0,
                                "explain": "💡 <strong>Từ mượn tiếng Anh: メモする (Memo)</strong>: Ghi chú, ghi chép nhanh lại thông tin quan trọng. コピーする (photocopy), テスト (bài kiểm tra)."
                            },
                            {
                                "id": 3,
                                "type": "mc",
                                "prompt": "日本で 部屋を 借りる とき、毎月の (   ) の ほかに 敷金や 礼金が 必要です。",
                                "promptVi": "Khi thuê phòng ở Nhật, ngoài tiền thuê nhà hàng tháng còn cần tiền đặt cọc và tiền lễ.",
                                "options": ["家賃", "切符", "おつり", "値段"],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng thuê nhà: 家賃 (やちん)</strong>: Tiền thuê nhà hàng tháng. Đi kèm các chi phí truyền thống của Nhật: 敷金 (tiền cọc), 礼金 (tiền lễ cảm ơn chủ nhà)."
                            },
                            {
                                "id": 4,
                                "type": "mc",
                                "prompt": "すみません、この 申請書に お名前と ご住所を ボールペンで (   ) ください。",
                                "promptVi": "Xin lỗi, xin vui lòng dùng bút bi viết họ tên và địa chỉ vào tờ đơn xin này.",
                                "options": ["書いて", "読んで", "話して", "聞いて"],
                                "correct": 0,
                                "explain": "💡 <strong>Điền đơn từ: 書く (かく) ➔ 書いてください</strong> (Hãy viết). Cụm từ cố định khi làm thủ tục hành chính tại Nhật."
                            },
                            {
                                "id": 5,
                                "type": "mc",
                                "prompt": "きのう 買った パソコンの 使い方が よく (   ) ません。教えて もらえませんか。",
                                "promptVi": "Tôi không rõ cách sử dụng chiếc máy tính mới mua hôm qua lắm. Bạn có thể chỉ giúp tôi được không?",
                                "options": ["分かり", "知り", "覚え", "思い"],
                                "correct": 0,
                                "explain": "💡 <strong>Phân biệt 分からない vs 知らない:</strong><br>• <strong>使い方が分からない</strong>: Không hiểu/không thông thạo cách dùng để thao tác (Đúng).<br>• 知らない: Không có thông tin/không biết về sự tồn tại của cái gì đó."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn câu có ý nghĩa tương đương (Câu đồng nghĩa)",
                        "groupInstruction": "Chọn câu trong 4 phương án (A, B, C, D) có ý nghĩa gần nhất với câu được gạch chân:",
                        "items": [
                            {
                                "id": 6,
                                "type": "mc",
                                "prompt": "<u>この 掃除機の 使い方は とても 簡単です。</u>",
                                "promptVi": "Cách sử dụng chiếc máy hút bụi này rất đơn giản.",
                                "options": [
                                    "この 掃除機は だれでも すぐ 簡単に 使えます。",
                                    "この 掃除機は 使う ことが とても 難しいです。",
                                    "この 掃除機は 説明書を 読まなければ 使えません。",
                                    "この 掃除機は 値段が とても 高いです。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Tính từ 簡単（な）(かんたん):</strong> Đơn giản, dễ dàng ➔ Đồng nghĩa với 'だれでもすぐ簡単に使えます' (ai cũng có thể dùng được ngay một cách dễ dàng)."
                            },
                            {
                                "id": 7,
                                "type": "mc",
                                "prompt": "<u>わたしは 毎朝 1時間 ジョギングを 続けて います。</u>",
                                "promptVi": "Tôi duy trì thói quen chạy bộ 1 tiếng mỗi sáng.",
                                "options": [
                                    "わたしは 毎朝 1時間 走る 習慣が あります。",
                                    "わたしは 走る ことが 大嫌いです。",
                                    "わたしは 朝は 疲れますから、走りません。",
                                    "わたしは 1か月に 1回だけ 走ります。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng 習慣 (しゅうかん: thói quen):</strong> '毎朝続けています' (mỗi sáng đều duy trì) = '毎朝走る習慣があります' (có thói quen chạy bộ mỗi sáng)."
                            },
                            {
                                "id": 8,
                                "type": "mc",
                                "prompt": "<u>この アパートの 周りには 店が 全然 ありません。</u>",
                                "promptVi": "Xung quanh khu căn hộ này hoàn toàn không có cửa hàng nào cả.",
                                "options": [
                                    "この アパートの 周りは 買い物が とても 不便です。",
                                    "この アパートの 周りは 買い物が とても 便利です。",
                                    "この アパートの 周りは いつも にぎやかです。",
                                    "この アパートは 駅の すぐ まえに あります。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ trái nghĩa 便利 vs 不便:</strong> Không có cửa hàng nào xung quanh ➔ Mua sắm cực kỳ bất tiện ('買い物がとても不便です')."
                            },
                            {
                                "id": 9,
                                "type": "mc",
                                "prompt": "<u>田中さんは 今、電話中ですから、後で かけ直します。</u>",
                                "promptVi": "Anh Tanaka hiện đang bận nghe điện thoại, tôi sẽ gọi lại sau.",
                                "options": [
                                    "田中さんは 今、他の 人と 電話で 話して います。",
                                    "田中さんは 今、出かけて 席に いません。",
                                    "田中さんは 今、ごはんを 食べて います。",
                                    "田中さんは もう 帰宅しました。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Từ vựng 電話中（でんわちゅう）:</strong> Đang trong cuộc đàm thoại ➔ '他の人と電話で話しています' (đang nói chuyện điện thoại với người khác)."
                            },
                            {
                                "id": 10,
                                "type": "mc",
                                "prompt": "<u>週末、部屋で のんびり 過ごしました。</u>",
                                "promptVi": "Cuối tuần tôi đã thong thả nghỉ ngơi trong phòng.",
                                "options": [
                                    "週末、部屋で 音楽を 聞きながら ゆっくり 休みました。",
                                    "週末、外へ 出かけて 忙しく 働きました。",
                                    "週末、遠い 所へ 旅行に 行きました。",
                                    "週末、朝から 晩まで 勉強ばかり しました。"
                                ],
                                "correct": 0,
                                "explain": "💡 <strong>Phó từ のんびり:</strong> Thong thả, thảnh thơi, không vướng bận ➔ 'ゆっくり休みました' (nghỉ ngơi thư thả)."
                            }
                        ]
                    }
                ]
            },
                        {
                "id": "sec2_kanji",
                "partNumber": "II",
                "partTitle": "HÁN TỰ (漢字 - 10 CÂU)",
                "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán thành Hiragana (11-15) và Chọn chữ Hán đúng từ Hiragana (16-20) chuẩn 100% chữ Hán Bài 1-10.",
                "badge": "20 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng cho chữ Hán trong ngoặc 【 】",
                        "groupInstruction": "Chọn cách đọc Hiragana chính xác nhất cho chữ Hán được gạch chân (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 11,
                                "type": "mc",
                                "prompt": "図書館で 日本の 歴史の 【本】を 借りました。",
                                "promptVi": "Tôi đã mượn một cuốn sách về lịch sử Nhật Bản ở thư viện.",
                                "options": ["ほん", "ぼん", "ぽん", "もと"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 2]: 本 (BẢN: sách / gốc)</strong>.<br>• Khi đứng một mình có nghĩa là cuốn sách, đọc là <strong>ほん</strong>. Bẫy âm biến đục 'ぼん' (khi đếm 3 bản: さんぼん) hoặc bán đục 'ぽん'."
                            },
                            {
                                "id": 12,
                                "type": "mc",
                                "prompt": "あの 【黒い】 かばんを 持って いる 人は だれですか。",
                                "promptVi": "Người đang mang chiếc túi màu đen đằng kia là ai thế?",
                                "options": ["くろい", "しろい", "あかい", "あおい"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 6]: 黒 (HẮC: màu đen)</strong> ➔ <strong>黒い (くろい)</strong>. Phân biệt 4 tính từ màu sắc Bài 6: 白い (trắng), 赤い (đỏ), 青い (xanh da trời)."
                            },
                            {
                                "id": 13,
                                "type": "mc",
                                "prompt": "毎晩、寝る 前に 本を 【読みます】。",
                                "promptVi": "Mỗi tối trước khi ngủ tôi đều đọc sách.",
                                "options": ["よみます", "のみます", "やすみます", "たのみます"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 2]: 読 (ĐỘC: đọc)</strong>.<br>• Có bộ Ngôn (言) bên trái và chữ Mại (売) bên phải ➔ <strong>読みます (よみます)</strong>."
                            },
                            {
                                "id": 14,
                                "type": "mc",
                                "prompt": "誕生日に 【何】を もらいましたか。",
                                "promptVi": "Vào ngày sinh nhật bạn đã nhận được gì thế?",
                                "options": ["なに", "なん", "いつ", "どこ"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 2]: 何 (HÀ: cái gì / bao nhiêu)</strong>.<br>• Khi đứng trước trợ từ を (何をもらいましたか) đọc là <strong>なに</strong> (Đúng).<br>• Khi đứng trước trợ từ だ, です hoặc trước lượng từ mới đọc là 'なん'."
                            },
                            {
                                "id": 15,
                                "type": "mc",
                                "prompt": "日本の 伝統的な 【文化】に とても 興味が あります。",
                                "promptVi": "Tôi rất có hứng thú với văn hóa truyền thống của Nhật Bản.",
                                "options": ["ぶんか", "もんか", "ぶんけ", "ほんか"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 10]: 文 (VĂN) + 化 (HÓA)</strong>.<br>• 文: ぶん.<br>• 化: か.<br>➔ Ghép lại đọc là <strong>文化 (ぶんか)</strong>: Văn hóa. Bẫy âm On khác của Văn 'もん' (như trong もんぶしょう)."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Chọn chữ Hán đúng cho từ Hiragana trong ngoặc 【 】",
                        "groupInstruction": "Chọn chữ Hán viết đúng nhất cho từ Hiragana trong câu (Chữ Hán Bài 1-10):",
                        "items": [
                            {
                                "id": 16,
                                "type": "mc",
                                "prompt": "あそこで 電話を して いる 【おんなのひと】は 先生です。",
                                "promptVi": "Người phụ nữ đang nghe điện thoại đằng kia là giáo viên.",
                                "options": ["女の人", "男の人", "女の子", "男の子"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 1]: 女 (NỮ) + 人 (NHÂN)</strong> ➔ <strong>女の人 (おんなのひと)</strong>: Người phụ nữ.<br>• Phân biệt các từ chỉ người trong Bài 1: 男の人 (người đàn ông), 女の子 (bé gái), 男の子 (bé trai)."
                            },
                            {
                                "id": 17,
                                "type": "mc",
                                "prompt": "【こんしゅう】の 日曜日は どこへ 行きますか。",
                                "promptVi": "Chủ nhật tuần này bạn sẽ đi đâu thế?",
                                "options": ["今週", "来週", "先週", "毎週"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 3 & Bài 10]: 今 (KIM: nay) + 週 (CHU: tuần)</strong> ➔ <strong>今週 (こんしゅう)</strong>: Tuần này.<br>• Bẫy: 来週 (らいしゅう: tuần sau), 先週 (せんしゅう: tuần trước), 毎週 (まいしゅう: mỗi tuần)."
                            },
                            {
                                "id": 18,
                                "type": "mc",
                                "prompt": "わたしの 【うしろ】に たくさん 人が 並んで います。",
                                "promptVi": "Phía sau tôi có rất nhiều người đang xếp hàng.",
                                "options": ["後ろ", "前ろ", "待ろ", "右ろ"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 8]: 後 (HẬU: phía sau / sau khi)</strong> ➔ <strong>後ろ (うしろ)</strong>: Phía đằng sau.<br>• Phân biệt với chữ 前 (tiền: trước)."
                            },
                            {
                                "id": 19,
                                "type": "mc",
                                "prompt": "春になると、公園に きれいな 【はな】が 咲きます。",
                                "promptVi": "Hễ mùa xuân đến là những bông hoa tươi đẹp nở rộ trong công viên.",
                                "options": ["花", "海", "山", "川"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 3]: Cảnh sắc tự nhiên:</strong><br>• <strong>花 (HOA: hoa) ➔ はな (Đúng)</strong>.<br>• 海 (hải: biển - うみ), 山 (sơn: núi - やま), 川 (xuyên: sông - かわ)."
                            },
                            {
                                "id": 20,
                                "type": "mc",
                                "prompt": "わたしは 日本の アニメが とても 【すき】です。",
                                "promptVi": "Tôi rất thích phim hoạt hình Anime của Nhật Bản.",
                                "options": ["好き", "好く", "女き", "子き"],
                                "correct": 0,
                                "explain": "💡 <strong>Chữ Hán [Bài 2]: 好 (HẢO: thích / tốt)</strong> ➔ <strong>好き (すき)</strong>. Cấu tạo chữ Hán: Người phụ nữ (女) ôm đứa con (子) trong tay thể hiện tình yêu thương, sự yêu thích."
                            }
                        ]
                    }
                ]
            },
{
                "id": "sec3_grammar",
                "partNumber": "III",
                "partTitle": "NGỮ PHÁP (文法 - 12 CÂU)",
                "partDesc": "Gồm 3 dạng bài: Điền khuyết trợ từ & cấu trúc (21-26), Sắp xếp câu Hái sao ☆ (27-30) và Dịch câu tự luận (31-32).",
                "badge": "30 Điểm",
                "groups": [
                    {
                        "groupTitle": "DẠNG 1: Điền trợ từ hoặc thể ngữ pháp vào chỗ trống (   )",
                        "groupInstruction": "Chọn phương án đúng nhất (A, B, C, D) để hoàn thành câu:",
                        "items": [
                            {
                                "id": 21,
                                "type": "mc",
                                "prompt": "パスポートを なくしましたから、すぐに 大使館へ (   ) なければ なりません。",
                                "promptVi": "Vì bị mất hộ chiếu nên tôi phải đến Đại sứ quán ngay lập tức.",
                                "options": ["行か", "行き", "行って", "行った"],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc bắt buộc: V-なければなりません</strong>.<br>Động từ nhóm 1: 行く (いく) chia thể ない là 行かない ➔ bỏ い thêm ければ ➔ <strong>行かなければなりません</strong>. Chỗ trống đứng trước なければ nên chọn <strong>行か</strong>."
                            },
                            {
                                "id": 22,
                                "type": "mc",
                                "prompt": "春に なると、この 公園 (   ) 桜が 一番 きれいに 咲きます。",
                                "promptVi": "Hễ mùa xuân đến, ở công viên này hoa anh đào sẽ nở rộ đẹp nhất.",
                                "options": ["で", "に", "を", "へ"],
                                "correct": 0,
                                "explain": "💡 <strong>Trợ từ chỉ nơi diễn ra sự việc/hành động: [Địa điểm] + で</strong>.<br>Hoa nở rộ rực rỡ tại công viên dùng <strong>公園で</strong>. Không dùng に vì đây không phải nơi tồn tại tĩnh."
                            },
                            {
                                "id": 23,
                                "type": "mc",
                                "prompt": "休日は 部屋を 掃除(   )、スーパーで 買い物を したり しました。",
                                "promptVi": "Ngày nghỉ tôi dọn dẹp phòng ốc và đi siêu thị mua sắm.",
                                "options": ["したり", "して", "する", "した"],
                                "correct": 0,
                                "explain": "💡 <strong>Cấu trúc liệt kê: V-たり V-たり します</strong>.<br>掃除する chuyển thành <strong>掃除したり</strong>."
                            },
                            {
                                "id": 24,
                                "type": "mc",
                                "prompt": "図書館の 貴重な 本に ボールペンで メモを 書いては (   )。",
                                "promptVi": "Không được dùng bút bi viết ghi chú vào sách quý của thư viện.",
                                "options": ["いけません", "なりません", "いいです", "あります"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu cấm đoán: V-てはいけません</strong> (Quy định cấm vẽ bẩn vào sách)."
                            },
                            {
                                "id": 25,
                                "type": "mc",
                                "prompt": "先生、この 文法の 使い方を もう一度 教えて (   ) ませんか。",
                                "promptVi": "Thưa thầy, thầy có thể chỉ dạy lại cho em cách dùng ngữ pháp này một lần nữa được không ạ?",
                                "options": ["いただけ", "もらい", "くれ", "あげ"],
                                "correct": 0,
                                "explain": "💡 <strong>Kính ngữ nhờ vả với bề trên (giáo viên): V-ていただけませんか</strong>. Lịch sự và trang trọng hơn てもらえませんか."
                            },
                            {
                                "id": 26,
                                "type": "mc",
                                "prompt": "わたしは 子どもの ころから ピアノを 上手に 弾く (   ) が できます。",
                                "promptVi": "Từ nhỏ tôi đã có thể chơi đàn piano rất giỏi.",
                                "options": ["こと", "の", "もの", "ため"],
                                "correct": 0,
                                "explain": "💡 <strong>Mẫu câu chỉ khả năng: V-ることができる</strong> ➔ Bắt buộc dùng <strong>こと</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 2: Sắp xếp câu tìm vị trí Ngôi sao ( ★ )",
                        "groupInstruction": "Bấm chọn lần lượt 4 cụm từ để xếp vào các vị trí 1 - 2 - 3 - 4. Sau đó chọn đáp án nằm ở vị trí ngôi sao ★:",
                        "items": [
                            {
                                "id": 27,
                                "type": "star",
                                "sentencePre": "寮の 部屋に",
                                "sentencePost": "脱ぎます。",
                                "promptVi": "Trước khi bước vào phòng ký túc xá, tôi cởi giày ở bậc thềm.",
                                "parts": [
                                    {"id": 1, "text": "前に、"},
                                    {"id": 2, "text": "入る"},
                                    {"id": 3, "text": "靴を"},
                                    {"id": 4, "text": "玄関で"}
                                ],
                                "fullOrder": [2, 1, 4, 3],
                                "starPos": 2,
                                "correctOption": 4,
                                "fullSentence": "寮の 部屋に 入る 前に、 玄関で 靴を 脱ぎます。",
                                "explain": "💡 <strong>Ngữ pháp V-る前に:</strong> 部屋に [2] 入る ➔ [1] 前に、 ➔ ★[4] 玄関で ➔ [3] 靴を ➔ 脱ぎます.<br>Vị trí ngôi sao ★ số 3 là <strong>[4] 玄関で</strong>."
                            },
                            {
                                "id": 28,
                                "type": "star",
                                "sentencePre": "日曜日、",
                                "sentencePost": "しました。",
                                "promptVi": "Chủ nhật tôi nghe nhạc và đi dạo công viên.",
                                "parts": [
                                    {"id": 1, "text": "聞いたり、"},
                                    {"id": 2, "text": "音楽を"},
                                    {"id": 3, "text": "散歩を"},
                                    {"id": 4, "text": "したり"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "日曜日、 音楽を 聞いたり、 散歩を したり しました。",
                                "explain": "💡 <strong>Ngữ pháp V-たり:</strong> [2] 音楽を ➔ [1] 聞いたり、 ➔ ★[3] 散歩を ➔ [4] したり ➔ しました.<br>Vị trí ngôi sao ★ số 3 là <strong>[3] 散歩を</strong>."
                            },
                            {
                                "id": 29,
                                "type": "star",
                                "sentencePre": "ベトナムで",
                                "sentencePost": "ハロン湾です。",
                                "promptVi": "Địa danh du lịch nổi tiếng nhất ở Việt Nam là Vịnh Hạ Long.",
                                "parts": [
                                    {"id": 1, "text": "有名な"},
                                    {"id": 2, "text": "一番"},
                                    {"id": 3, "text": "観光地は"},
                                    {"id": 4, "text": "自然の"}
                                ],
                                "fullOrder": [2, 1, 3, 4],
                                "starPos": 2,
                                "correctOption": 3,
                                "fullSentence": "ベトナムで 一番 有名な 観光地は ハロン湾です。",
                                "explain": "💡 <strong>So sánh nhất:</strong> ベトナムで [2] 一番 ➔ [1] 有名な ➔ ★[3] 観光地は ➔ ハロン湾です.<br>Vị trí ngôi sao ★ số 3 là <strong>[3] 観光地は</strong>."
                            },
                            {
                                "id": 30,
                                "type": "star",
                                "sentencePre": "夜 10時以降は",
                                "sentencePost": "いけません。",
                                "promptVi": "Sau 10 giờ đêm không được làm ồn to tiếng vì sẽ làm phiền người xung quanh.",
                                "parts": [
                                    {"id": 1, "text": "騒いでは"},
                                    {"id": 2, "text": "大声で"},
                                    {"id": 3, "text": "迷惑ですから"},
                                    {"id": 4, "text": "周りの"}
                                ],
                                "fullOrder": [2, 1, 4, 3],
                                "starPos": 2,
                                "correctOption": 4,
                                "fullSentence": "夜 10時以降は 大声で 騒いでは 周りの 迷惑ですから いけません。",
                                "explain": "💡 <strong>Trật tự câu cấm đoán & giải thích:</strong> [2] 大声で ➔ [1] 騒いでは ➔ ★[4] 周りの ➔ [3] 迷惑ですから ➔ いけません.<br>Vị trí ngôi sao ★ số 3 là <strong>[4] 周りの</strong>."
                            }
                        ]
                    },
                    {
                        "groupTitle": "DẠNG 3: Dịch câu tự luận (Nhật ↔ Việt)",
                        "groupInstruction": "Tự gõ câu dịch hoàn chỉnh vào ô bên dưới. Có thể dùng nút '🎯 Tôi Thấy Tôi Viết Đúng' nếu dùng từ đồng nghĩa hợp lý:",
                        "items": [
                            {
                                "id": 31,
                                "type": "trans",
                                "dir": "ja_to_vi",
                                "prompt": "日本では ゴミを 種類ごとに 分別して 捨てなければ なりませんから、ルールを よく 覚えて ください。",
                                "placeholder": "Nhập bản dịch tiếng Việt tại đây...",
                                "standard": "Ở Nhật Bản phải phân loại rác theo từng chủng loại rồi mới vứt, nên xin hãy ghi nhớ kỹ quy định nhé.",
                                "keywords": ["nhật bản", "phân loại", "rác", "vứt", "quy định", "nhớ"],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• 種類ごとに分別して: Phân loại theo từng loại.<br>• 捨てなければなりません: Bắt buộc phải vứt rác đúng quy định.<br>• ～から: Vì... nên (chỉ lý do: vì phải phân loại nên hãy nhớ rõ luật)."
                            },
                            {
                                "id": 32,
                                "type": "trans",
                                "dir": "vi_to_ja",
                                "prompt": "Tôi nghĩ việc nhớ chữ Hán là khó nhất, nhưng khi hiểu được ý nghĩa thì thấy rất thú vị.",
                                "placeholder": "Gõ câu tiếng Nhật tại đây (dùng Hiragana hoặc Kanji)...",
                                "standard": "漢字を 覚える ことが 一番 難しいと 思いますが、意味を 知ると とても 面白いです。",
                                "acceptable": [
                                    "漢字を覚えることが一番難しいと思いますが、意味を知るととても面白いです。",
                                    "かんじをおぼえることがいちばんむずかしいとおもいますが、いみをしるととてもおもしろいです。",
                                    "漢字を覚えることが一番難しいですが、意味を知るととても面白いです。",
                                    "漢字を覚えるのが一番難しいと思いますが、意味が分かると面白いです。"
                                ],
                                "explain": "💡 <strong>Phân tích ngữ pháp:</strong><br>• Việc nhớ chữ Hán là khó nhất: 漢字を 覚える ことが 一番 難しい.<br>• Mẫu bày tỏ ý kiến: ～と 思います (Tôi nghĩ là...).<br>• が: Nhưng (liên kết tương phản).<br>• Khi hiểu ý nghĩa thì rất thú vị: 意味を 知ると とても 面白いです."
                            }
                        ]
                    }
                ]
            },
            {
                "id": "sec4_reading",
                "partNumber": "IV",
                "partTitle": "ĐỌC HIỂU (読解 - 2 CÂU TRẮC NGHIỆM)",
                "partDesc": "Đọc kỹ thông báo nội quy ký túc xá và trả lời 2 câu hỏi kiểm tra thông tin.",
                "badge": "10 Điểm",
                "readingPassage": {
                    "title": "【国際交流会館】留学生寮の 生活ルールと ゴミ出しの 約束",
                    "content": "会館に 住む 留学生の みなさんへ。\nみんなが 快適に 生活する ために、以下の ルールを 必ず 守って ください。\n\n1. 【ゴミの 分別と 出す 日】\n   • もえる ゴミ（生ゴミ・紙など）：毎週 火曜日と 金曜日の 朝8時までに、1階の ゴミステーションへ 出して ください。\n   • 資源（しげん）ゴミ（缶・ビン・ペットボトル）：毎週 水曜日に 出して ください。\n     ※ ペットボトルは キャップと ラベルを はがして、中を 水で 洗ってから 捨てて ください。\n\n2. 【夜の 過ごし方】\n   • 夜 11時以降は、部屋や 廊下（ろうか）で 大声で 話したり、大きな 音で 音楽を かけたり しては いけません。\n\n3. 【友人の 宿泊（しゅくはく）】\n   • 友達や 家族を 部屋に 泊めたい ときは、3日前までに 管理人室（かんりにんしつ）へ 申請書を 出さなければ なりません。",
                    "translation": "Gửi các bạn lưu học sinh đang sinh sống tại Nhà Giao lưu Quốc tế.\nĐể mọi người đều có thể sinh hoạt một cách thoải mái, xin hãy nghiêm túc tuân thủ các quy tắc sau:\n\n1. 【Phân loại rác và ngày vứt rác】\n   • Rác cháy được (thức ăn thừa, giấy rác...): Vứt trước 8h sáng thứ Ba và thứ Sáu hàng tuần tại trạm rác tầng 1.\n   • Rác tái chế (lon, chai thủy tinh, chai nhựa PET): Vứt vào thứ Tư hàng tuần.\n     ※ Chai nhựa PET xin hãy bóc nắp và nhãn mác ra, súc sạch bên trong bằng nước rồi mới vứt.\n\n2. 【Quy định ban đêm】\n   • Sau 11h đêm tuyệt đối không được nói to tiếng ở trong phòng hay ngoài hành lang, và không được mở nhạc lớn.\n\n3. 【Người quen ngủ lại qua đêm】\n   • Khi muốn cho bạn bè hoặc người nhà ngủ lại phòng qua đêm, phải nộp đơn xin lên phòng quản lý trước ít nhất 3 ngày."
                },
                "items": [
                    {
                        "id": 33,
                        "type": "mc",
                        "prompt": "ペットボトルを 捨てる とき、どのように しなければ なりませんか。",
                        "promptVi": "Khi vứt chai nhựa PET, cần phải làm như thế nào?",
                        "options": [
                            "キャップと ラベルを はがして、中を 水で 洗ってから 捨てます。",
                            "そのまま 何も 洗わないで、火曜日の 朝に 捨てます。",
                            "もえる ゴミと 一緒に、金曜日の 夜に 捨てます。",
                            "ハサミで 細かく 切ってから、水曜日に 捨てます。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Thông tin trong mục 1:</strong> 『※ ペットボトルは キャップと ラベルを はがして、中を 水で 洗ってから 捨てて ください。』 ➔ Phương án A chính xác."
                    },
                    {
                        "id": 34,
                        "type": "mc",
                        "prompt": "会館の ルールに ついて、正しい ものは どれですか。",
                        "promptVi": "Câu nào dưới đây ĐÚNG theo nội quy của khu nhà lưu học sinh?",
                        "options": [
                            "友達を 部屋に 泊めたい ときは、3日前までに 申請しなければ なりません。",
                            "友達なら 誰でも 許可なしで いつでも 部屋に 泊める ことが できます。",
                            "夜 11時以降でも、自分の 部屋なら 大きい 音で 音楽を 聞いても いいです。",
                            "もえる ゴミは 毎日 いつでも 好きな 時間に 捨てる ことが できます。"
                        ],
                        "correct": 0,
                        "explain": "💡 <strong>Kiểm tra chi tiết:</strong><br>• Mục 3 ghi rõ: 『友達や 家族を 部屋に 泊めたい ときは、3日前までに 管理人室へ 申請書を 出さなければ なりません。』 ➔ Phương án A đúng.<br>• B sai vì cần xin phép trước 3 ngày.<br>• C sai vì sau 11h đêm cấm mở nhạc to.<br>• D sai vì rác cháy được chỉ vứt vào sáng thứ Ba và thứ Sáu trước 8h."
                    }
                ]
            },
            {
                "id": "sec5_essay",
                "partNumber": "V",
                "partTitle": "TỰ LUẬN TRẢ LỜI CÂU HỎI (2 CÂU)",
                "partDesc": "Tự gõ câu trả lời bằng tiếng Nhật theo tình huống Can-do thực tế (yêu cầu mỗi câu viết ít nhất 50 từ/ký tự).",
                "badge": "15 Điểm",
                "items": [
                    {
                        "id": 35,
                        "type": "essay",
                        "prompt": "あなたの 国の おすすめの 観光地（かんこうち）について 紹介してください。（どこですか。何が 有名ですか。どんな ことが できますか。★50字以上で 書いてください）",
                        "promptVi": "Hãy giới thiệu về địa điểm du lịch bạn muốn giới thiệu ở đất nước bạn (Ở đâu? Có gì nổi tiếng? Đến đó có thể trải nghiệm điều gì? ★Yêu cầu viết ít nhất 50 từ/ký tự)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしのおすすめの 観光地は ハロン湾です...",
                        "hints": [
                            "Tên và vị trí: わたしのおすすめは ～です / ～に あります",
                            "Đặc điểm nổi bật: 海と 島が きれいで、世界遺産です",
                            "Hoạt động: 船に 乗ったり、おいしい 料理を 食べたり できます",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしのおすすめの 観光地は ベトナムの ハロン湾です。ハノイから バスで 2時間半ぐらいです。海と たくさんの 島が とても きれいで、有名な 世界遺産です。船に 乗って 洞窟を 見学したり、新鮮で おいしい 海鮮を 食べたり する ことが できます。景色が 素晴らしいですから、ぜひ 行ってみてください。",
                        "modelVi": "Địa điểm du lịch tôi muốn giới thiệu là Vịnh Hạ Long của Việt Nam. Đi xe buýt từ Hà Nội mất khoảng 2 tiếng rưỡi. Biển và hàng ngàn hòn đảo rất đẹp, là di sản thế giới nổi tiếng. Bạn có thể đi thuyền tham quan hang động và thưởng thức hải sản tươi ngon. Phong cảnh tuyệt vời nên nhất định hãy đến thử một lần nhé.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; cấu trúc ngữ pháp phong phú (～たり～たり、～ことができます、ぜひ～てください)."
                    },
                    {
                        "id": 36,
                        "type": "essay",
                        "prompt": "日本語の 勉強で、何が 一番 難しいですか。どうしてですか。どうやって 練習して いますか。（★50字以上で 書いてください）",
                        "promptVi": "Khi học tiếng Nhật, bạn thấy điều gì khó nhất? Vì sao? Bạn luyện tập bằng cách nào? (★Yêu cầu viết ít nhất 50 từ/ký tự bằng tiếng Nhật)",
                        "placeholder": "Gõ đoạn văn tiếng Nhật tại đây (tối thiểu 50 từ/ký tự)... Ví dụ: わたしは 漢字を 覚える ことが 一番 難しいと 思います...",
                        "hints": [
                            "Khó khăn lớn nhất: わたしは ～が 一番 難しいと 思います (漢字 / 文法 / 聴解)",
                            "Nguyên nhân: 形や 読み方が たくさん ありますから / 違いですから",
                            "Cách khắc phục: 毎日 10回 ノートに 書いて 練習して います",
                            "Độ dài: Yêu cầu tối thiểu 50 chữ/ký tự"
                        ],
                        "modelAnswer": "わたしは 漢字を 覚える ことが 一番 難しいと 思います。形や 読み方が たくさん あって、すぐに 忘れて しまいますから。ですから、毎日 ノートに 10回 書いたり、アプリを 使ったり して 練習して います。少しずつ 読める ように なって、今は とても 面白いです。これからも 諦めずに 頑張ります。",
                        "modelVi": "Tôi nghĩ việc ghi nhớ chữ Hán là khó nhất. Vì có rất nhiều hình thái và cách đọc, lại rất dễ quên. Do đó, mỗi ngày tôi đều viết 10 lần vào vở hoặc sử dụng ứng dụng để luyện tập. Dần dần đọc được nhiều chữ hơn nên bây giờ tôi thấy rất thú vị. Tôi sẽ không bỏ cuộc và tiếp tục nỗ lực hơn nữa.",
                        "rubric": "Tiêu chí chấm điểm Can-do: Đạt độ dài tối thiểu ≥ 50 từ/ký tự; biểu đạt rõ quan điểm cá nhân, nêu rõ giải pháp học tập tích cực."
                    }
                ]
            }
        ]
    }

# Export all 5 expert exams in standardized list
EXAMS_DATA_EXPERT = [
    build_m101(),
    build_m102(),
    build_m103(),
    build_m104(),
    build_m105()
]

if __name__ == "__main__":
    print(f"Compiled all 5 expert midterm exams: {[e['code'] for e in EXAMS_DATA_EXPERT]}")
    for ex in EXAMS_DATA_EXPERT:
        total_items = sum(len(g["items"]) for s in ex["sections"] if "groups" in s for g in s["groups"]) + sum(len(s["items"]) for s in ex["sections"] if "items" in s)
        print(f"  {ex['code']}: {ex['name']} -> {total_items} items")
