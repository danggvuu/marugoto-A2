#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/update_strictly_l1_10_kanji.py
Cập nhật 100% chữ Hán trong Phần II của 5 mã đề M101 - M105 theo chuẩn giáo trình Marugoto A2-1 Bài 1 - 10
"""

import re

SEC2_M101 = '''            {
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
            }'''

SEC2_M102 = '''            {
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
            }'''

SEC2_M103 = '''            {
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
            }'''

SEC2_M104 = '''            {
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
            }'''

SEC2_M105 = '''            {
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
            }'''

def main():
    with open('scripts/build_expert_5_exams.py', 'r', encoding='utf-8') as f:
        content = f.read()

    new_secs = [SEC2_M101, SEC2_M102, SEC2_M103, SEC2_M104, SEC2_M105]

    # Pattern matching sec2_kanji block
    pattern = r'\{\s*\"id\":\s*\"sec2_kanji\".*?\}\s*\]\s*\}\s*,\s*(?=\{\s*\"id\":\s*\"sec3_grammar\")'

    matches = list(re.finditer(pattern, content, flags=re.DOTALL))
    if len(matches) != 5:
        print(f"Error: Expected 5 sec2_kanji blocks, found {len(matches)}")
        return

    # Replace from back to front
    for i in range(4, -1, -1):
        m = matches[i]
        content = content[:m.start()] + new_secs[i] + ',\n' + content[m.end():]

    with open('scripts/build_expert_5_exams.py', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully replaced all 5 Part II Kanji sections with 100% strictly Lessons 1-10 Kanji!")

if __name__ == '__main__':
    main()
