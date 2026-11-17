/**
 * MARUGOTO A2.1 & A2-2 KAIWA INTERVIEW TOPICS DATA
 * Chuẩn bị cho bài thi vấn đáp Kaiwa 5 phút với giáo viên tiếng Nhật.
 * Câu mẫu rút gọn theo ngữ pháp A1–A2.1 đến bài 18,
 * kèm từ vựng A2-2 bài 1–2. Không dùng mẫu nâng cao trong câu học thuộc.
 *  1. Bảo vệ sức khoẻ (Bài 15 & 16)
 *  2. Hỏi han về sức khỏe & Lời khuyên (Bài 15 & 16)
 *  3. Trao đổi về tiệc chúc mừng (Bài 17 & 18)
 *  4. Kinh nghiệm đi Nhật (Slide câu hỏi cô giáo & Từ vựng Bài 11-12, A2-2)
 */

window.KAIWA_TOPICS_DATA = [
    {
        id: "topic1",
        num: 1,
        title: "Bảo Vệ Sức Khoẻ",
        titleJp: "けんこうを まもる (健康管理)",
        badge: "Chủ Đề 1 • Bài 15 & 16",
        lessonRef: "Marugoto A2.1 — Bài 15 & 16 (Sức khỏe & Thói quen)",
        image: "assets/img/kaiwa/topic1_bao_ve_suc_khoe.jpg",
        desc: "Luyện nói về vận động, giấc ngủ, ăn uống và làm thêm giờ bằng ～ています, Nのために, ～から, thời gian và tần suất.",
        coreQuestions: [
            {
                id: 1,
                qJp: "けんこうの ために、何を していますか。",
                qVi: "Để bảo vệ sức khỏe, bạn đang làm những gì?",
                intent: "Giáo viên muốn đánh giá cấu trúc mục đích 「〜のために」 và thói quen đang duy trì 「〜ています」.",
                mindmap: [
                    "Vận động (運動): Chạy bộ (走ります / ジョギング), đi dạo (散歩します), tập thể dục (運動します)",
                    "Giấc ngủ (睡眠): Ngủ sớm (早く寝ます), ngủ 7-8 tiếng (7〜8時間寝ます)",
                    "Ăn uống: Ăn nhiều rau (野菜をたくさん食べます), ăn hoa quả (果物を食べます), uống nhiều nước (水をたくさん飲みます)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Chạy bộ & Ăn nhiều rau (Rất dễ nhớ)",
                        jp: "毎朝、30分ぐらい 走っています。それから、野菜を たくさん 食べています。",
                        vi: "Mỗi sáng em chạy bộ khoảng 30 phút ạ. Ngoài ra, em ăn rất nhiều rau củ.",
                        keyPoints: "Dùng thể tiếp diễn 「〜ています」 diễn tả thói quen đều đặn hàng ngày (走っています, 食べています)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Ngủ sớm & Đi dạo công viên (Từ quen thuộc)",
                        jp: "夜は いつも 早く 寝ています。毎日 7時間ぐらい 寝ます。それから、週末に 公園を 散歩します。",
                        vi: "Buổi tối em luôn đi ngủ sớm. Mỗi ngày em ngủ khoảng 7 tiếng. Ngoài ra, cuối tuần em đi dạo ở công viên.",
                        keyPoints: "Dùng thể tiếp diễn 「寝ています」 diễn tả thói quen sinh hoạt tốt và từ quen thuộc 「早く」."
                    }
                ],
                vocab: [
                    { jp: "けんこう (健康)", vi: "Sức khỏe (Bài 15 & A2-2 L1)" },
                    { jp: "走ります (はしります)", vi: "Chạy bộ (Bài 16)" },
                    { jp: "散歩します (さんぽします)", vi: "Đi bộ dạo (Bài 16)" },
                    { jp: "野菜 (やさい)", vi: "Rau củ (Bài 12)" },
                    { jp: "早く寝ます (はやくねます)", vi: "Ngủ sớm (Bài 15)" }
                ]
            },
            {
                id: 2,
                qJp: "どのぐらい していますか。",
                qVi: "Bạn làm việc đó bao lâu / tuần mấy lần?",
                intent: "Giáo viên kiểm tra cách nói khoảng thời gian (〜時間/〜分), tần suất (週に〜回) hoặc thời gian đã bắt đầu (〜年前から).",
                mindmap: [
                    "Tần suất: 1週間に3回 (1 tuần 3 lần), 毎日 (mỗi ngày), 週末だけ (chỉ cuối tuần)",
                    "Thời gian: 30分ぐらい (khoảng 30 phút), 1年前から (từ 1 năm trước)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Nói tần suất tuần 3 lần (Chuẩn A2)",
                        jp: "1週間に 3回ぐらい 走っています。1回に 30分ぐらいです。",
                        vi: "Một tuần tôi chạy khoảng 3 lần. Mỗi lần khoảng 30 phút.",
                        keyPoints: "Cụm tần suất chuẩn sách Marugoto: 「1週間に〜回」(いっしゅうかんに〜かい)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Nói thời gian duy trì",
                        jp: "去年の 4月から 走っています。もう 1年ぐらいに なります。",
                        vi: "Tôi chạy bộ từ tháng 4 năm ngoái. Đến nay đã khoảng một năm rồi.",
                        keyPoints: "Mốc thời gian + から; khoảng thời gian + になります (bài 14)."
                    }
                ],
                vocab: [
                    { jp: "1週間に (いっしゅうかんに)", vi: "Trong 1 tuần..." },
                    { jp: "〜回 (かい)", vi: "Lần (số lần)" },
                    { jp: "1年ぐらいに なります", vi: "Đến nay đã khoảng một năm" }
                ]
            },
            {
                id: 3,
                qJp: "ビールや お酒は 飲みますか。",
                qVi: "Bạn có uống bia hay rượu không?",
                intent: "Kiểm tra cách trả lời mức độ: ときどき (thỉnh thoảng), あまり〜ない (không lắm), 全然〜ない (hoàn toàn không).",
                mindmap: [
                    "Uống ít: ときどき飲みます (thỉnh thoảng uống), 週末だけ (chỉ cuối tuần), 1杯だけ (chỉ 1 ly)",
                    "Không uống: 全然飲みません (hoàn toàn không uống), お酒が弱いです (tửu lượng yếu)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Thỉnh thoảng uống 1 ly vào cuối tuần",
                        jp: "はい、ときどき 飲みます。でも、健康のために、あまり たくさん 飲みません。週末に 1杯だけです。",
                        vi: "Vâng, thỉnh thoảng tôi có uống. Nhưng vì sức khỏe, tôi không uống nhiều. Cuối tuần chỉ 1 ly thôi.",
                        keyPoints: "Kết hợp 「ときどき」 và giới hạn 「〜だけ」(chỉ 1 ly)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Không uống vì không thích rượu",
                        jp: "いいえ、全然 飲みません。お酒が あまり 好きじゃないですから、水や お茶を 飲みます。",
                        vi: "Dạ không, tôi hoàn toàn không uống vì không thích rượu lắm. Tôi uống nước hoặc trà.",
                        keyPoints: "Dùng あまり + phủ định để nói không thích lắm và nối lý do bằng ～ですから."
                    }
                ],
                vocab: [
                    { jp: "ときどき", vi: "Thỉnh thoảng" },
                    { jp: "全然〜ない (ぜんぜん)", vi: "Hoàn toàn không..." },
                    { jp: "頭が痛い (あたまがいたい)", vi: "Đau đầu (Bài 15)" },
                    { jp: "〜杯 (はい)", vi: "Ly, chén, cốc" }
                ]
            },
            {
                id: 4,
                qJp: "どうしてですか。",
                qVi: "Tại sao lại như vậy?",
                intent: "Kiểm tra cách giải thích nguyên nhân bằng mẫu câu 「〜から」(bởi vì...).",
                mindmap: [
                    "Lý do sức khỏe: 体によくないですから (vì không tốt cho cơ thể), 健康が一番ですから (vì sức khỏe là số 1)",
                    "Lý do vui vẻ: 友達と話します。楽しいですから (nói chuyện với bạn bè, vì rất vui)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Vì sức khỏe là quan trọng nhất (Dùng từ A2-2)",
                        jp: "健康が 一番 大切ですから。お酒は あまり 飲みません。",
                        vi: "Vì sức khỏe là quan trọng nhất. Tôi không uống rượu nhiều.",
                        keyPoints: "Lý do + ですから. Trả lời bằng hai câu ngắn, không cần câu điều kiện."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Gặp bạn cuối tuần rất vui",
                        jp: "週末に 友達と 会います。一緒に 飲んだり、話したり します。とても 楽しいですから。",
                        vi: "Cuối tuần tôi gặp bạn. Chúng tôi uống nước, nói chuyện với nhau. Vì rất vui.",
                        keyPoints: "Vた + り、Vた + りします để kể hoạt động tiêu biểu (bài 16)."
                    }
                ],
                vocab: [
                    { jp: "体によくない (からだによくない)", vi: "Không tốt cho cơ thể" },
                    { jp: "一番 (いちばん)", vi: "Nhất, số 1 (Bài 1 A2-2)" },
                    { jp: "話したり します (はなしたり します)", vi: "Nói chuyện và làm một số hoạt động khác" }
                ]
            },
            {
                id: 5,
                qJp: "よく 残業を しますか。",
                qVi: "Bạn có hay làm thêm giờ không?",
                intent: "Kiểm tra từ vựng 残業 (ざんぎょう) và thói quen sinh hoạt công sở.",
                mindmap: [
                    "Ít khi làm thêm: あまりしません (ít làm), 早く帰ります (về sớm)",
                    "Chỉ làm khi bận: 忙しい時だけします (chỉ làm khi bận)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Ít khi làm thêm, luôn về nhà sớm",
                        jp: "いいえ、あまり しません。健康のために、いつも 早く 帰っています。",
                        vi: "Dạ không, em ít khi làm thêm lắm ạ. Để giữ sức khỏe, em luôn về nhà sớm.",
                        keyPoints: "Dùng từ cực kỳ quen thuộc: 早く帰る (về sớm) và thể tiếp diễn 「〜ています」."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Thỉnh thoảng làm thêm vì nhiều việc",
                        jp: "はい、ときどき します。仕事が 多いですから。でも、いつも 7時ごろ 帰ります。",
                        vi: "Vâng, thỉnh thoảng tôi làm thêm vì nhiều việc. Nhưng thường tôi về lúc khoảng 7 giờ.",
                        keyPoints: "ときどき (thỉnh thoảng), ～から (vì) và giờ + ごろ (khoảng)."
                    }
                ],
                vocab: [
                    { jp: "残業 (ざんぎょう)", vi: "Làm thêm giờ (Bài 16)" },
                    { jp: "忙しい (いそがしい)", vi: "Bận rộn" },
                    { jp: "早く帰る (はやくかえる)", vi: "Về sớm" }
                ]
            }
        ],
        fullDialogue: [
            { speaker: "sensei", name: "Sensei", jp: "こんにちは。今日は 健康の 話を しましょう。", vi: "Chào em. Hôm nay chúng ta nói chuyện về sức khỏe nhé." },
            { speaker: "gakusei", name: "Bạn", jp: "はい、先生。よろしくお願いします！", vi: "Dạ vâng thưa cô. Em xin phép bắt đầu ạ!" },
            { speaker: "sensei", name: "Sensei", jp: "まず、けんこうの ために、何を していますか。", vi: "Trước tiên, để giữ sức khỏe, em đang làm những gì?" },
            { speaker: "gakusei", name: "Bạn", jp: "毎朝、30分ぐらい 走っています。それから、野菜を たくさん 食べています。", vi: "Mỗi sáng em chạy bộ khoảng 30 phút ạ. Ngoài ra, em ăn rất nhiều rau củ." },
            { speaker: "sensei", name: "Sensei", jp: "走っているんですね、いいですね！どのぐらい していますか。", vi: "Em chạy bộ à, tốt quá! Em làm việc đó bao lâu rồi / tuần mấy lần?" },
            { speaker: "gakusei", name: "Bạn", jp: "1週間に 3回ぐらい 走っています。去年の 4月からです。", vi: "Dạ một tuần em chạy khoảng 3 lần. Em bắt đầu từ tháng 4 năm ngoái ạ." },
            { speaker: "sensei", name: "Sensei", jp: "素晴らしいですね。ところで、ビールや お酒は 飲みますか。", vi: "Tuyệt vời quá. Nhân tiện, em có uống bia hay rượu không?" },
            { speaker: "gakusei", name: "Bạn", jp: "いいえ、全然 飲みません。お酒が あまり 好きじゃないですから。", vi: "Dạ không, em hoàn toàn không uống vì không thích rượu lắm ạ." },
            { speaker: "sensei", name: "Sensei", jp: "そうなんですね。普段、よく 残業を しますか。", vi: "Vậy à. Ngày thường em có hay làm thêm giờ không?" },
            { speaker: "gakusei", name: "Bạn", jp: "いいえ、あまり しません。健康が 一番 大切ですから、いつも 早く 帰っています。", vi: "Dạ không, em ít làm thêm. Vì sức khỏe quan trọng nhất nên em thường về sớm ạ." },
            { speaker: "sensei", name: "Sensei", jp: "いいですね。ありがとうございました。", vi: "Tốt đấy. Cảm ơn em nhé." },
            { speaker: "gakusei", name: "Bạn", jp: "先生、ありがとうございました。", vi: "Em cảm ơn cô ạ." }
        ]
    },
    {
        id: "topic2",
        num: 2,
        title: "Hỏi Han Về Sức Khỏe",
        titleJp: "健康について 気遣う・アドバイス",
        badge: "Chủ Đề 2 • Bài 15 & 16",
        lessonRef: "Marugoto A2.1 — Bài 15 (Triệu chứng, Đau ốm & Lời khuyên)",
        image: "assets/img/kaiwa/topic2_hoi_han_suc_khoe.jpg",
        desc: "Giao tiếp khi có người bị ốm/mệt tại trường học hoặc nơi làm việc: hỏi han triệu chứng, kiểm tra uống thuốc, đề nghị giúp đỡ và đưa lời khuyên về sớm nghỉ ngơi.",
        coreQuestions: [
            {
                id: 1,
                qJp: "顔色が 良くないですね。どうしたんですか。",
                qVi: "Sắc mặt bạn không được tốt nhỉ. Bạn bị sao thế?",
                intent: "Kiểm tra cách mô tả triệu chứng bệnh bằng đuôi giải thích lý do 「〜んです」 (Bài 15).",
                mindmap: [
                    "Đau đầu + sốt nhẹ: 頭が痛い (đau đầu), 熱がある (bị sốt)",
                    "Cảm cúm + đau họng: 風邪をひいた (bị cảm), 喉が痛い (đau họng), 咳が出る (bị ho)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Bị đau đầu và hơi sốt (Bài 15)",
                        jp: "きのうから ちょっと 頭が 痛くて、熱も 少し あるんです。",
                        vi: "Từ hôm qua tôi hơi bị đau đầu, và cũng hơi bị sốt một chút.",
                        keyPoints: "Dùng thể nối tính từ 「〜くて」 và đuôi giải thích tình trạng 「〜んです」 (Bài 15)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Bị cảm cúm, đau họng mỏi mệt",
                        jp: "風邪を ひきました。のどが 痛いんです。少し 疲れています。",
                        vi: "Tôi bị cảm. Cổ họng tôi đau. Tôi cũng hơi mệt.",
                        keyPoints: "Dùng ～ました để kể việc đã xảy ra và ～んです để giải thích tình trạng (bài 15)."
                    }
                ],
                vocab: [
                    { jp: "どうしたんですか", vi: "Bạn bị làm sao thế?" },
                    { jp: "頭が痛い (あたまがいたい)", vi: "Đau đầu (Bài 15)" },
                    { jp: "熱がある (ねつがある)", vi: "Bị sốt (Bài 15)" },
                    { jp: "喉が痛い (のどがいたい)", vi: "Đau họng (Bài 15)" },
                    { jp: "風邪をひく (かぜをひく)", vi: "Bị cảm cúm (Bài 15)" }
                ]
            },
            {
                id: 2,
                qJp: "くすりは 飲みましたか。",
                qVi: "Bạn đã uống thuốc chưa?",
                intent: "Kiểm tra cách nói đã làm gì / chưa làm gì (〜ました / まだ〜ていません).",
                mindmap: [
                    "Đã uống rồi: はい、飲みました (vâng, đã uống), 朝ご飯のあとで (sau bữa sáng)",
                    "Chưa uống: いいえ、まだです (chưa), 帰りに買います (lúc về sẽ mua)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Đã uống thuốc cảm sau bữa sáng",
                        jp: "はい、朝ご飯の あとで 風邪の 薬を 飲みました。",
                        vi: "Dạ rồi, sau bữa sáng tôi đã uống thuốc cảm rồi.",
                        keyPoints: "Cụm danh từ + のあとで (sau khi...) và 薬を飲む (uống thuốc)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Chưa uống, lát về sẽ mua",
                        jp: "いいえ、まだです。薬を 持っていませんから、帰りに 買って 飲みます。",
                        vi: "Dạ chưa. Vì tôi không mang theo thuốc nên lúc về tôi sẽ mua uống.",
                        keyPoints: "Cấu trúc rất cơ bản: 持っていません (không có mang theo), 買って飲みます (mua rồi uống)."
                    }
                ],
                vocab: [
                    { jp: "薬 (くすり)", vi: "Thuốc (Bài 15)" },
                    { jp: "風邪薬 (かぜぐすり)", vi: "Thuốc cảm cúm" },
                    { jp: "まだ〜ていません", vi: "Vẫn chưa làm..." }
                ]
            },
            {
                id: 3,
                qJp: "何か てつだいましょうか。",
                qVi: "Tôi giúp bạn việc gì nhé?",
                intent: "Kiểm tra mẫu đề nghị giúp đỡ 「〜ましょうか」 và cách tiếp nhận hoặc từ chối lịch sự.",
                mindmap: [
                    "Nhờ giúp việc nhỏ: このコピーをお願いします (xin nhờ photo tập tài liệu này)",
                    "Tự lo được: 大丈夫です (tôi ổn), もうすぐ終わりますから (vì sắp xong việc rồi)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Nhờ photo tài liệu",
                        jp: "ありがとうございます。じゃ、この コピーを お願いします。",
                        vi: "Cảm ơn bạn. Vậy xin lỗi, bạn photocopy giúp tôi tài liệu này được không?",
                        keyPoints: "N + をお願いします: nhờ làm một việc, ngắn gọn và lịch sự."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Cảm ơn và báo sắp xong việc rồi",
                        jp: "ありがとうございます。でも、もうすぐ 終わりますから 大丈夫です。",
                        vi: "Cảm ơn bạn nhiều. Nhưng sắp xong rồi nên tôi không sao đâu.",
                        keyPoints: "Trả lời ngắn gọn, lịch sự: 「大丈夫です」(tôi ổn, không sao)."
                    }
                ],
                vocab: [
                    { jp: "手伝います (てつだいます)", vi: "Giúp đỡ (Bài 13)" },
                    { jp: "コピー", vi: "Photocopy tài liệu" },
                    { jp: "大丈夫 (だいじょうぶ)", vi: "Không sao, ổn" }
                ]
            },
            {
                id: 4,
                qJp: "今日は 無理を しないで、早く かえると いいですよ。",
                qVi: "Hôm nay bạn đừng làm quá sức, nên về sớm thì tốt đấy.",
                intent: "Khảo sát cách tiếp nhận lời khuyên 「〜といいですよ」(bạn nên... thì tốt đấy).",
                mindmap: [
                    "Đồng ý về sớm: はい、そうします (vâng, tôi sẽ làm vậy), 早く寝ます (về ngủ sớm)",
                    "Nói với giáo viên/sếp: 先生/部長に話します (thưa với cô giáo / sếp)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Đồng ý về sớm uống thuốc đi ngủ",
                        jp: "はい、ありがとうございます。そうします。今日は 早く 帰って 寝ます。",
                        vi: "Vâng, cảm ơn bạn nhiều. Tôi sẽ làm vậy. Hôm nay tôi sẽ về sớm rồi ngủ.",
                        keyPoints: "Mẫu đồng ý tiếp thu lời khuyên kinh điển: 「そうします」(tôi sẽ làm như vậy)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Xin phép về sớm một chút",
                        jp: "ありがとうございます。先生に 話して、少し 早く 帰ります。",
                        vi: "Cảm ơn bạn. Tôi sẽ thưa với thầy cô để xin phép về sớm một chút.",
                        keyPoints: "Dễ nói, tự nhiên và đúng phép tắc."
                    }
                ],
                vocab: [
                    { jp: "無理をしないで (むりをしないで)", vi: "Đừng cố quá sức (Bài 15)" },
                    { jp: "早く帰る (はやくかえる)", vi: "Về sớm" },
                    { jp: "〜といいですよ", vi: "Nên làm ~ thì tốt đấy" }
                ]
            },
            {
                id: 5,
                qJp: "お大事に してくださいね。",
                qVi: "Chúc bạn mau khỏe lại nhé.",
                intent: "Câu chúc sức khỏe kinh điển trong tiếng Nhật khi tạm biệt người ốm.",
                mindmap: [
                    "Đáp lại: ありがとうございます (cảm ơn bạn), また明日 (hẹn gặp lại ngày mai)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách đáp chuẩn mực và ấm áp",
                        jp: "ありがとうございます。また 明日。",
                        vi: "Cảm ơn bạn nhiều nhé. Hẹn gặp lại vào ngày mai.",
                        keyPoints: "Ngắn gọn, chân thành, phát âm to rõ ràng."
                    }
                ],
                vocab: [
                    { jp: "お大事に (おだいじに)", vi: "Chúc bạn mau khỏe! (Bài 15)" }
                ]
            }
        ],
        fullDialogue: [
            { speaker: "sensei", name: "Đồng nghiệp", jp: "顔色が 良くないですね。どうしたんですか。", vi: "Sắc mặt bạn trông không được tốt nhỉ. Bạn bị làm sao thế?" },
            { speaker: "gakusei", name: "Bạn", jp: "きのうから ちょっと 頭が 痛くて、熱も 少し あるんです。", vi: "Từ hôm qua tôi hơi bị đau đầu, và cũng hơi bị sốt một chút." },
            { speaker: "sensei", name: "Đồng nghiệp", jp: "大変ですね！薬は もう 飲みましたか。", vi: "Thế thì mệt quá! Bạn đã uống thuốc chưa?" },
            { speaker: "gakusei", name: "Bạn", jp: "はい、朝 ご飯の あとで 風邪の 薬を 飲みました。", vi: "Dạ rồi, sau bữa sáng tôi đã uống thuốc cảm rồi." },
            { speaker: "sensei", name: "Đồng nghiệp", jp: "そうですか。何か 手伝いましょうか。", vi: "Vậy à. Tôi có giúp được việc gì cho bạn không?" },
            { speaker: "gakusei", name: "Bạn", jp: "ありがとうございます。でも、もうすぐ 終わりますから 大丈夫です。", vi: "Cảm ơn bạn nhiều. Nhưng sắp xong rồi nên tôi không sao đâu." },
            { speaker: "sensei", name: "Đồng nghiệp", jp: "今日は 無理を しないで、早く 帰ると いいですよ。", vi: "Hôm nay bạn đừng cố làm quá sức, nên về sớm nghỉ ngơi thì tốt hơn đấy." },
            { speaker: "gakusei", name: "Bạn", jp: "はい、そうします。今日は 早く 帰って、ゆっくり 寝ます。", vi: "Vâng, tôi sẽ làm vậy. Hôm nay tôi sẽ về sớm rồi nghỉ ngơi ngủ một giấc." },
            { speaker: "sensei", name: "Đồng nghiệp", jp: "ええ、お大事に してくださいね。", vi: "Ừ, chúc bạn mau chóng khỏe lại nhé." },
            { speaker: "gakusei", name: "Bạn", jp: "ありがとうございます。また 明日。", vi: "Cảm ơn bạn. Hẹn gặp lại ngày mai." }
        ]
    },
    {
        id: "topic3",
        num: 3,
        title: "Trao Đổi Về Chúc Mừng",
        titleJp: "お祝いについて 話し合う (結婚・パーティー)",
        badge: "Chủ Đề 3 • Bài 17 & 18",
        lessonRef: "Marugoto A2.1 — Bài 17 & 18 (Kỷ niệm, Chúc mừng & Tặng quà)",
        image: "assets/img/kaiwa/topic3_trao_doi_chuc_mung.jpg",
        desc: "Bàn kế hoạch tiệc cưới, quà tặng, số người và địa điểm bằng ～ませんか, ～ましょう, ～と思います và ～ないでください.",
        coreQuestions: [
            {
                id: 1,
                qJp: "レーさんの 結婚の お祝いパーティー、どうしましょうか。",
                qVi: "Tiệc mừng kết hôn của chị Lê, chúng mình tính sao đây?",
                intent: "Mở đầu thảo luận kế hoạch bằng mẫu rủ rê 「〜ましょうか / 〜ませんか」.",
                mindmap: [
                    "Thời gian & ý tưởng: 来週の金曜日 (thứ 6 tuần sau), レストランでする (làm ở nhà hàng), ご飯を食べる (cùng đi ăn)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Tối thứ 6 tuần sau mở tiệc ở nhà hàng",
                        jp: "来週の 金曜日の 夜、みんなで レストランで パーティーを しませんか。",
                        vi: "Tối thứ Sáu tuần sau, mọi người cùng tổ chức tiệc ở nhà hàng nhé?",
                        keyPoints: "Dùng mẫu rủ rê lịch sự 「〜ませんか」(cùng làm ~ không?)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Sau giờ làm cùng đi ăn mừng",
                        jp: "仕事の あとで、みんなで お祝いの ご飯を 食べに 行きましょう。",
                        vi: "Sau giờ làm, mọi người cùng đi ăn một bữa cơm chúc mừng nhé.",
                        keyPoints: "Cấu trúc mục đích di chuyển: V(bỏ masu) + に行きます."
                    }
                ],
                vocab: [
                    { jp: "お祝い (おいわい)", vi: "Chúc mừng (Bài 17)" },
                    { jp: "結婚 (けっこん)", vi: "Kết hôn (Bài 17-18)" },
                    { jp: "パーティーをします", vi: "Tổ chức tiệc" }
                ]
            },
            {
                id: 2,
                qJp: "プレゼントは 何を あげますか。",
                qVi: "Chúng mình sẽ tặng quà gì bây giờ?",
                intent: "Kiểm tra từ vựng món quà và mẫu đưa ra gợi ý 「〜はどうですか」.",
                mindmap: [
                    "Gợi ý quà: 時計 (đồng hồ - Bài 17), お花 (hoa), ネクタイ (cà vạt - Bài 17 & A2-2 L2)",
                    "Cách mua: みんなでお金を出す (mọi người cùng góp tiền mua)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Tặng đồng hồ hoặc hoa",
                        jp: "時計や お花は どうですか。きれいな お花が いいと 思います。きっと 喜びますよ。",
                        vi: "Đồng hồ hay hoa thì sao? Tôi nghĩ hoa đẹp là lựa chọn tốt. Chắc chị ấy sẽ vui lắm.",
                        keyPoints: "～はどうですか để gợi ý; ～と思います để nêu ý kiến (bài 18)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Cùng góp tiền mua đồ dùng cho nhà mới",
                        jp: "みんなで お金を 出して、新しい 家で 使う 物を 買いましょう。",
                        vi: "Mọi người cùng góp tiền, mua đồ dùng trong nhà mới cho chị ấy nhé.",
                        keyPoints: "Cụm từ dễ nhớ: お金を出す (góp tiền), 買いましょう (cùng mua nào)."
                    }
                ],
                vocab: [
                    { jp: "プレゼント", vi: "Quà tặng" },
                    { jp: "時計 (とけい)", vi: "Đồng hồ (Bài 17)" },
                    { jp: "お花 (おはな)", vi: "Bông hoa" },
                    { jp: "喜びます (よろこびます)", vi: "Vui mừng (Bài 18)" }
                ]
            },
            {
                id: 3,
                qJp: "何人ぐらい 参加しますか。",
                qVi: "Khoảng bao nhiêu người sẽ tham gia?",
                intent: "Hỏi số lượng người tham gia (何人 - なんにん) và cách ước lượng khoảng chừng.",
                mindmap: [
                    "Khoảng 8 đến 10 người: 8人か10人ぐらい",
                    "Cả nhóm mình: チームの全員 / 全部で7人"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Khoảng 8 đến 10 người",
                        jp: "たぶん 8人か 10人ぐらい 来ると 思います。",
                        vi: "Tôi nghĩ chắc khoảng 8 đến 10 người sẽ đến.",
                        keyPoints: "Dùng cách đếm người: 8人 (はちにん), 10人 (じゅうにん) và 〜と思います."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Cả nhóm tất cả là 7 người",
                        jp: "私たちの チームの みんなで、全部で 7人です。",
                        vi: "Cả nhóm chúng ta, tất cả là 7 người.",
                        keyPoints: "Dùng chữ 全部 (ぜんぶ - tất cả, toàn bộ - Bài 1 A2-2)."
                    }
                ],
                vocab: [
                    { jp: "何人 (なんにん)", vi: "Mấy người" },
                    { jp: "参加します (さんかします)", vi: "Tham gia" },
                    { jp: "全部で (ぜんぶで)", vi: "Tổng cộng, tất cả (Bài 1 A2-2)" }
                ]
            },
            {
                id: 4,
                qJp: "場所は どこで しますか。",
                qVi: "Chúng mình tổ chức ở đâu?",
                intent: "Hỏi và giải thích lý do chọn địa điểm thuận tiện.",
                mindmap: [
                    "Gần công ty / gần ga: 会社の近く (gần công ty), 駅から近い (gần ga)",
                    "Quán ăn ngon: おいしい日本料理の店 (quán món Nhật ngon)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Nhà hàng gần công ty vì gần ga tiện lợi",
                        jp: "会社の 近くの レストランが いいと 思います。駅から 近いですから、便利です。",
                        vi: "Tôi nghĩ nhà hàng gần công ty là tốt nhất. Vì gần nhà ga nên rất thuận tiện.",
                        keyPoints: "Áp dụng chữ 近い (ちかい - gần - Bài 1 A2-2) và 便利 (thuận tiện)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Đặt quán món Nhật ngon",
                        jp: "おいしい 日本料理の 店を 予約しましょう。",
                        vi: "Chúng ta hãy đặt một quán món Nhật ngon nhé.",
                        keyPoints: "Từ ngữ đơn giản: 日本料理の店, 予約します (đặt bàn)."
                    }
                ],
                vocab: [
                    { jp: "近く (ちかく) / 近い (ちかい)", vi: "Gần (Bài 1 A2-2)" },
                    { jp: "便利（な） (べんり)", vi: "Thuận tiện" },
                    { jp: "予約します (よやくします)", vi: "Đặt chỗ" }
                ]
            },
            {
                id: 5,
                qJp: "レーさんに もう 言いましたか。",
                qVi: "Bạn đã nói với chị Lê chưa?",
                intent: "Kiểm tra thì quá khứ/hiện tại và ứng dụng từ vựng 'Bí mật' (秘密) của A2-2.",
                mindmap: [
                    "Chưa nói - bí mật: いいえ、まだです (chưa), 秘密です (bí mật), サプライズ (bất ngờ)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Chưa, là bí mật đấy, đừng nói nhé!",
                        jp: "いいえ、まだです。秘密ですから、まだ 言わないでくださいね。サプライズに しましょう！",
                        vi: "Chưa, vẫn chưa đâu! Vì là bí mật nên bạn đừng nói vội nhé. Hãy tạo bất ngờ nha!",
                        keyPoints: "Dùng ngay chữ 秘密 (ひみつ - bí mật - Từ vựng Bài 1 A2-2 vừa học!). Rất ấn tượng!"
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Mới nói giờ tiệc, quà thì giữ bí mật",
                        jp: "はい、金曜日に パーティーを すると 言いました。プレゼントは 秘密です。",
                        vi: "Rồi, tôi đã nói: 'Tiệc vào thứ Sáu.' Còn quà tặng là bí mật.",
                        keyPoints: "Tiếp tục dùng từ 秘密 (bí mật - A2-2 L1) một cách thông minh."
                    }
                ],
                vocab: [
                    { jp: "秘密 (ひみつ)", vi: "Bí mật (Bài 1 A2-2)" },
                    { jp: "言わないでください", vi: "Xin đừng nói" },
                    { jp: "サプライズ", vi: "Bất ngờ (Surprise)" }
                ]
            }
        ],
        fullDialogue: [
            { speaker: "sensei", name: "Tanaka", jp: "レーさんの 結婚の お祝いパーティー、どうしましょうか。", vi: "Tiệc mừng kết hôn của chị Lê, chúng mình tính sao đây?" },
            { speaker: "gakusei", name: "Bạn", jp: "来週の 金曜日の 夜、みんなで レストランで パーティーを しませんか。", vi: "Tối thứ Sáu tuần sau, mọi người cùng tổ chức tiệc ở nhà hàng nhé?" },
            { speaker: "sensei", name: "Tanaka", jp: "いいですね！プレゼントは 何を あげますか。", vi: "Ý kiến hay đấy! Thế mình tặng quà gì bây giờ?" },
            { speaker: "gakusei", name: "Bạn", jp: "時計や お花は どうですか。みんなで お金を 出して 買いましょう。", vi: "Đồng hồ hoặc hoa thì sao? Mọi người cùng góp tiền mua chung nhé." },
            { speaker: "sensei", name: "Tanaka", jp: "いいですね！何人ぐらい 参加しますか。", vi: "Hay đấy! Khoảng bao nhiêu người sẽ tham gia nhỉ?" },
            { speaker: "gakusei", name: "Bạn", jp: "私たちの チームの みんなで、全部で 8人ぐらいです。", vi: "Cả nhóm chúng ta, tất cả là khoảng 8 người." },
            { speaker: "sensei", name: "Tanaka", jp: "じゃ、場所は どこが いいですか。", vi: "Vậy địa điểm ở đâu thì tiện nhỉ?" },
            { speaker: "gakusei", name: "Bạn", jp: "会社の 近くの レストランが いいと 思います。駅から 近いですから、便利です。", vi: "Tôi nghĩ nhà hàng gần công ty là tốt nhất. Vì gần ga nên rất thuận tiện." },
            { speaker: "sensei", name: "Tanaka", jp: "なるほど！ところで、レーさんに もう 言いましたか。", vi: "Hợp lý quá! Nhân tiện, bạn đã nói với chị Lê chưa?" },
            { speaker: "gakusei", name: "Bạn", jp: "いいえ、まだです。秘密ですから、まだ 言わないでくださいね。サプライズに しましょう！", vi: "Chưa, vẫn chưa đâu! Là bí mật đấy nên bạn đừng nói vội nhé. Hãy tạo bất ngờ nha!" },
            { speaker: "sensei", name: "Tanaka", jp: "ふふ、分かりました。楽しみに しています！", vi: "Haha, tôi hiểu rồi. Háo hức chờ đến hôm đó quá!" }
        ]
    },
    {
        id: "topic4",
        num: 4,
        title: "Kinh Nghiệm Đi Nhật",
        titleJp: "にほんへの りょこう・けいけん (日本旅行・経験)",
        badge: "Chủ Đề 4 • Slide Cô Giáo",
        lessonRef: "Marugoto A2.1 — Mong muốn (bài 10), kinh nghiệm (bài 13), liệt kê (bài 16)",
        image: "assets/img/kaiwa/topic4_kinh_nghiem.jpg",
        desc: "Luyện 7 câu hỏi về đi Nhật, địa điểm, món ăn và quà tặng bằng ～たことがあります, ～たいです, ～たり～たり và ～から.",
        coreQuestions: [
            {
                id: 1,
                qJp: "日本に 行ったことが ありますか。",
                qVi: "Bạn đã từng đi Nhật Bản chưa?",
                intent: "Luyện mẫu kinh nghiệm 「V-たことが あります / ありません」 (bài 13).",
                mindmap: [
                    "Chưa từng đi: いいえ、まだ行ったことがありません (chưa từng đi), いつか行きたいです (muốn đi một ngày nào đó)",
                    "Đã từng đi: はい、一度行ったことがあります (đã từng đi 1 lần), 2年前に行きました (đi 2 năm trước)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Chưa từng đi, nhưng rất muốn đi",
                        jp: "いいえ、まだ 行ったことが ありません。でも、日本が 大好きですから、いつか ぜひ 行きたいです。",
                        vi: "Dạ chưa, em chưa từng đi Nhật bao giờ ạ. Nhưng vì em rất yêu thích Nhật Bản nên nhất định một ngày nào đó muốn đến thăm.",
                        keyPoints: "Mẫu chuẩn: まだ V-たことがありません và mong muốn ぜひ〜たいです."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Đã từng đi du lịch 1 lần",
                        jp: "はい、一度 行ったことが あります。2年前に 旅行で 行きました。",
                        vi: "Dạ rồi, em từng đi một lần rồi ạ. Em đi du lịch cách đây 2 năm.",
                        keyPoints: "Dùng 一度 (いちど - một lần) và mốc thời gian 2年前."
                    }
                ],
                vocab: [
                    { jp: "行ったことがある (いったことがある)", vi: "Đã từng đi (Bài 13)" },
                    { jp: "一度 (いちど)", vi: "Một lần" },
                    { jp: "ぜひ", vi: "Nhất định" }
                ]
            },
            {
                id: 2,
                qJp: "どこに 行きましたか／行きたいですか。",
                qVi: "Bạn đã đi đâu / muốn đi những đâu?",
                intent: "Hỏi địa điểm và hoạt động muốn trải nghiệm tại Nhật.",
                mindmap: [
                    "Tokyo & Kyoto: 東京で買い物 (mua sắm ở Tokyo), 京都でお寺を見る (ngắm chùa ở Kyoto)",
                    "Hokkaido: 北海道で雪を見る (ngắm tuyết ở Hokkaido)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Đi Tokyo mua sắm & Kyoto ngắm chùa",
                        jp: "東京と 京都に 行きたいです。東京で 買い物を して、京都で 古い お寺や 神社を 見たいです。",
                        vi: "Em muốn đi Tokyo và Kyoto ạ. Ở Tokyo em muốn mua sắm, còn ở Kyoto muốn ngắm các ngôi đền chùa cổ kính.",
                        keyPoints: "Nối hành động bằng thể Te: 買い物をして、見たいです."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Đi Hokkaido ngắm tuyết và ăn ramen",
                        jp: "北海道へ 行きたいです。冬に 雪を 見たり、ラーメンを 食べたり したいです。",
                        vi: "Em muốn đi Hokkaido ạ. Em muốn ngắm tuyết rơi vào mùa đông và ăn mì ramen.",
                        keyPoints: "Liệt kê bằng V-たり V-たり (bài 16); したいです nói mong muốn."
                    }
                ],
                vocab: [
                    { jp: "東京 (とうきょう)", vi: "Tokyo" },
                    { jp: "京都 (きょうと)", vi: "Kyoto" },
                    { jp: "お寺 (おてら)", vi: "Chùa cổ" },
                    { jp: "神社 (じんじゃ)", vi: "Đền thờ thần đạo" }
                ]
            },
            {
                id: 3,
                qJp: "日本の 何が 一番 好きですか。",
                qVi: "Bạn thích điều gì nhất ở nước Nhật?",
                intent: "Kiểm tra mẫu so sánh nhất 「〜が一番好きです」 (dùng 一番 của Bài 1 A2-2!).",
                mindmap: [
                    "Ẩm thực & Anime: 食べ物 (đồ ăn), アニメ, ラーメン, 寿司 (sushi)",
                    "Văn hóa & Con người: 文化 (văn hóa), 優しい人々 (con người tốt bụng)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Thích đồ ăn và anime nhất (Ramen, sushi)",
                        jp: "日本の 食べ物と アニメが 一番 好きです。特に ラーメンと 寿司が 大好きです。",
                        vi: "Em thích đồ ăn và anime Nhật Bản nhất ạ. Đặc biệt em rất mê món mì ramen và sushi.",
                        keyPoints: "Dùng chữ 一番 (nhất, số 1 - Bài 1 A2-2) và từ nối 特に (đặc biệt là)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Thích văn hóa và con người hiền lành",
                        jp: "日本の 文化と、優しい 人々が 一番 好きです。",
                        vi: "Em thích văn hóa Nhật Bản và những con người hiền lành, tốt bụng nhất ạ.",
                        keyPoints: "Dùng chữ 優しい (やさしい - hiền lành, tốt bụng - Từ vựng Bài 1 A2-2!)."
                    }
                ],
                vocab: [
                    { jp: "一番 (いちばん)", vi: "Nhất, số một (Bài 1 A2-2)" },
                    { jp: "特に (とくに)", vi: "Đặc biệt là" },
                    { jp: "優しい (やさしい)", vi: "Hiền lành, tốt bụng (Bài 1 A2-2)" }
                ]
            },
            {
                id: 4,
                qJp: "どこに 一番 行きたいですか。",
                qVi: "Bạn muốn đến nơi nào nhất?",
                intent: "Hỏi địa điểm số một muốn đặt chân tới và lý do.",
                mindmap: [
                    "Kyoto: 有名ですから (vì rất nổi tiếng), きれいですから (vì rất đẹp)",
                    "Núi Phú Sĩ (富士山): 一番高い山 (ngọn núi cao nhất)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Muốn đi Kyoto nhất vì nổi tiếng và đẹp",
                        jp: "京都に 一番 行きたいです。京都は とても 有名で、きれいですから。",
                        vi: "Em muốn đi Kyoto nhất ạ. Bởi vì Kyoto rất nổi tiếng và phong cảnh rất đẹp.",
                        keyPoints: "Dùng chữ 有名 (ゆうめい - nổi tiếng - Từ vựng Bài 1 A2-2!)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Muốn ngắm núi Phú Sĩ ở cự ly gần",
                        jp: "富士山に 一番 行きたいです。日本の 一番 高い 山を 近くで 見たいです。",
                        vi: "Em muốn đi núi Phú Sĩ nhất ạ. Em muốn ngắm ngọn núi cao nhất nước Nhật ở cự ly gần.",
                        keyPoints: "Dùng chữ 一番 (nhất) và 近い (gần - Bài 1 A2-2)."
                    }
                ],
                vocab: [
                    { jp: "有名（な） (ゆうめい)", vi: "Nổi tiếng (Bài 1 A2-2)" },
                    { jp: "富士山 (ふじさん)", vi: "Núi Phú Sĩ" },
                    { jp: "近くで (ちかくで)", vi: "Ở cự ly gần (Bài 1 A2-2)" }
                ]
            },
            {
                id: 5,
                qJp: "どうしてですか。",
                qVi: "Tại sao bạn lại muốn đến đó?",
                intent: "Giải thích nguyên nhân bằng mẫu 「〜からです / 〜から」.",
                mindmap: [
                    "Về Kyoto: Phố cổ đẹp, có hứng thú với văn hóa Nhật Bản (興味があります)",
                    "Về con người: Người Nhật rất hiền lành và tốt bụng (優しい)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách 1: Xem trên ảnh thấy đẹp và có hứng thú với văn hóa",
                        jp: "写真や テレビで 見ました。街が とても きれいですから。日本の 歴史や 文化に 興味が あります。",
                        vi: "Em đã xem trên ảnh và tivi. Vì thành phố rất đẹp. Em cũng hứng thú với lịch sử và văn hóa Nhật Bản.",
                        keyPoints: "Dùng chữ 興味 (きょうみ - hứng thú: 興味があります - Từ vựng Bài 1 A2-2!)."
                    },
                    {
                        level: "easy",
                        tag: "Cách 2: Muốn gặp người Nhật hiền lành, tốt bụng",
                        jp: "日本の 人は 親切だと 思います。日本の 人と 会って、話したいです。",
                        vi: "Em nghĩ người Nhật tốt bụng. Em muốn gặp và nói chuyện với người Nhật.",
                        keyPoints: "Tính từ な + だと思います (bài 18); V bỏ ます + たいです để nói mong muốn."
                    }
                ],
                vocab: [
                    { jp: "興味 (きょうみ)", vi: "Hứng thú, quan tâm (Bài 1 A2-2)" },
                    { jp: "優しい (やさしい)", vi: "Tốt bụng, hiền lành (Bài 1 A2-2)" },
                    { jp: "話したい (はなしたい)", vi: "Muốn nói chuyện" }
                ]
            },
            {
                id: 6,
                qJp: "日本で 何を 食べたいですか／食べましたか。",
                qVi: "Ở Nhật bạn muốn ăn (hoặc đã ăn) món ăn gì?",
                intent: "Hỏi về trải nghiệm ẩm thực Nhật Bản quen thuộc.",
                mindmap: [
                    "Ramen & Sushi: 本場のラーメン (ramen chuẩn vị), 寿司 (sushi)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách trả lời: Muốn ăn ramen và sushi ở Nhật",
                        jp: "日本の 店で ラーメンと 寿司を 食べたいです。ベトナムでも ときどき 食べます。とても 好きです。",
                        vi: "Em muốn ăn ramen và sushi ở quán tại Nhật. Ở Việt Nam em cũng thỉnh thoảng ăn. Em rất thích hai món này.",
                        keyPoints: "食べます bỏ ます + たいです thành 食べたいです (muốn ăn)."
                    }
                ],
                vocab: [
                    { jp: "ラーメン", vi: "Mì ramen" },
                    { jp: "寿司 (すし)", vi: "Món sushi" },
                    { jp: "食べたい (たべたい)", vi: "Muốn ăn" }
                ]
            },
            {
                id: 7,
                qJp: "日本で お土産は 何を 買いたいですか。",
                qVi: "Ở Nhật bạn muốn mua món quà lưu niệm gì?",
                intent: "Kiểm tra từ vựng quà tặng cho gia đình và bạn bè.",
                mindmap: [
                    "Quà cho gia đình & bạn bè: 家族にお菓子 (bánh kẹo cho gia đình), お守り (bùa may mắn), お茶 (trà)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cách trả lời: Mua bánh kẹo cho gia đình và bùa may mắn",
                        jp: "家族や 友達に 日本の お菓子や お茶を 買いたいです。それから、かわいい お守りも 買いたいです。",
                        vi: "Em muốn mua bánh kẹo và trà Nhật Bản cho gia đình và bạn bè ạ. Ngoài ra em cũng muốn mua bùa may mắn xinh xắn nữa.",
                        keyPoints: "Dùng chữ 家族 (かぞく - gia đình - Từ vựng Bài 2 A2-2!) và お土産 (quà lưu niệm)."
                    }
                ],
                vocab: [
                    { jp: "お土産 (おみやげ)", vi: "Quà lưu niệm" },
                    { jp: "家族 (かぞく)", vi: "Gia đình (Bài 2 A2-2)" },
                    { jp: "お菓子 (おかし)", vi: "Bánh kẹo" },
                    { jp: "お守り (おまもり)", vi: "Bùa may mắn" }
                ]
            }
        ],
        fullDialogue: [
            { speaker: "sensei", name: "Sensei", jp: "こんにちは。今日は 日本の 旅行について 話しましょう。", vi: "Chào em. Hôm nay chúng ta nói về chuyến đi Nhật nhé." },
            { speaker: "gakusei", name: "Bạn", jp: "はい、先生！よろしくお願いします。", vi: "Dạ vâng thưa cô! Em xin phép bắt đầu ạ." },
            { speaker: "sensei", name: "Sensei", jp: "まず、日本に 行ったことが ありますか。", vi: "Trước hết, em đã từng đi Nhật Bản chưa?" },
            { speaker: "gakusei", name: "Bạn", jp: "いいえ、まだ 行ったことが ありません。でも、日本が 大好きですから、いつか ぜひ 行きたいです。", vi: "Dạ chưa, em chưa từng đi Nhật bao giờ ạ. Nhưng vì em rất yêu thích Nhật Bản nên một ngày nào đó nhất định em muốn đến thăm." },
            { speaker: "sensei", name: "Sensei", jp: "そうなんですね。どこに 行きたいですか。", vi: "Vậy à. Em muốn đi những đâu?" },
            { speaker: "gakusei", name: "Bạn", jp: "東京と 京都に 行きたいです。東京で 買い物を します。京都で 古い お寺を 見たいです。", vi: "Dạ em muốn đi Tokyo và Kyoto. Em sẽ mua sắm ở Tokyo và muốn xem chùa cổ ở Kyoto ạ." },
            { speaker: "sensei", name: "Sensei", jp: "いいですね！では、日本の 何が 一番 好きですか。", vi: "Tuyệt quá! Thế trong những điều của nước Nhật, em thích điều gì nhất?" },
            { speaker: "gakusei", name: "Bạn", jp: "日本の 食べ物が 一番 好きです。ラーメンと 寿司が 大好きです。", vi: "Dạ em thích đồ ăn Nhật nhất. Em rất thích ramen và sushi ạ." },
            { speaker: "sensei", name: "Sensei", jp: "ふふ、ラーメンと 寿司ですか、おいしいですね。では、どこに 一番 行きたいですか。", vi: "Haha, ramen và sushi à, ngon tuyệt đấy. Vậy trong các nơi, em muốn đến nơi nào nhất?" },
            { speaker: "gakusei", name: "Bạn", jp: "京都に 一番 行きたいです。京都は とても 有名で、きれいですから。", vi: "Dạ em muốn đến Kyoto nhất ạ. Bởi vì Kyoto rất nổi tiếng và phong cảnh rất đẹp ạ." },
            { speaker: "sensei", name: "Sensei", jp: "どうして 京都が いいんですか。", vi: "Tại sao em lại muốn đi Kyoto đến vậy?" },
            { speaker: "gakusei", name: "Bạn", jp: "写真で 見ました。街が とても きれいですから。日本の 歴史や 文化に 興味が あります。", vi: "Dạ em đã xem trên ảnh. Vì thành phố rất đẹp. Em cũng hứng thú với lịch sử và văn hóa Nhật Bản ạ." },
            { speaker: "sensei", name: "Sensei", jp: "素晴らしいですね！お土産は 何を 買いたいですか。", vi: "Thật tuyệt vời! Em có muốn mua quà gì về không?" },
            { speaker: "gakusei", name: "Bạn", jp: "家族や 友達に 日本の お菓子と お茶を たくさん 買って 帰りたいです！", vi: "Dạ em muốn mua thật nhiều bánh kẹo và trà Nhật Bản về làm quà cho gia đình và bạn bè ạ!" },
            { speaker: "sensei", name: "Sensei", jp: "とても 上手でした。日本へ 行けると いいですね。", vi: "Em trả lời rất giỏi. Mong em có thể đi Nhật nhé." },
            { speaker: "gakusei", name: "Bạn", jp: "はい！先生、ありがとうございました。", vi: "Dạ vâng. Em cảm ơn cô ạ." }
        ]
    }
];

window.KAIWA_TIPS = [
    {
        title: "1. Kỹ thuật Aizuchi (Phản ứng tự nhiên)",
        desc: "Người Nhật đặc biệt chú trọng sự lắng nghe. Khi cô giáo đặt câu hỏi hoặc nói chuyện, đừng bao giờ ngồi im phăng phắc. Hãy gật đầu nhẹ và dùng các thán từ tự nhiên:",
        phrases: [
            { jp: "ええ、そうですね。", vi: "Dạ, đúng vậy ạ." },
            { jp: "なるほど。", vi: "Ra là như thế ạ." },
            { jp: "それは 大変ですね。", vi: "Thế thì vất vả/mệt quá ạ." },
            { jp: "いいですね！", vi: "Tuyệt quá ạ!" }
        ]
    },
    {
        title: "2. Mẹo câu giờ thông minh (Filler words)",
        desc: "Khi cô giáo hỏi một câu bất ngờ và bạn cần 2-3 giây để suy nghĩ từ vựng, tuyệt đối TRÁNH im lặng đáng sợ. Hãy dùng các từ đệm câu giờ của người bản xứ:",
        phrases: [
            { jp: "ええと… そうですね…", vi: "À thì... để em xem nào..." },
            { jp: "実は… (じつは…)", vi: "Thực ra thì là..." },
            { jp: "そうですね、私は…", vi: "Vâng, em thì..." }
        ]
    },
    {
        title: "3. Công thức trả lời điểm 10 (Tránh cộc lốc)",
        desc: "Không bao giờ trả lời chỉ với 1 từ 'Hai' hoặc 'Iie'. Hãy luôn áp dụng công thức 3 vế:",
        formula: "[Khẳng định / Phủ định] ➔ [Chi tiết hành động / Tần suất] ➔ [Lý do: 〜から]",
        example: "VD: 「はい、ときどき 飲みます。でも、健康が 一番 大切ですから、たくさん 飲みません。」"
    },
    {
        title: "4. Kỹ thuật hỏi lại lịch sự khi không nghe rõ",
        desc: "Nếu lỡ cô giáo nói nhanh hoặc bạn nghe sót từ, đừng đoán mò hay sợ hãi. Hãy mỉm cười và nhờ cô nhắc lại một cách lịch sự:",
        phrases: [
            { jp: "すみません、もう一度 お願いします。", vi: "Xin lỗi cô, cô có thể nhắc lại một lần nữa được không ạ?" },
            { jp: "すみません、もう少し ゆっくり 話してください。", vi: "Xin lỗi cô, xin cô nói chậm hơn một chút ạ." }
        ]
    },
    {
        title: "5. Nụ cười và Ánh mắt (Ngôn ngữ cơ thể)",
        desc: "Nói đủ nghe, giữ tốc độ vừa phải và nhìn giáo viên khi trò chuyện. Chưa nhớ từ thì dùng câu ngắn hoặc nhờ cô nhắc lại; không cần cố dùng mẫu khó."
    }
];
