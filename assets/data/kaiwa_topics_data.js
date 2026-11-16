/**
 * MARUGOTO A2.1 KAIWA INTERVIEW TOPICS DATA
 * Chuẩn bị cho bài thi vấn đáp Kaiwa 5 phút với giáo viên tiếng Nhật.
 * Bao gồm 3 chủ đề trọng tâm:
 *  1. Bảo vệ sức khoẻ (健康を守る)
 *  2. Hỏi han về sức khỏe (健康について気遣う・アドバイス)
 *  3. Trao đổi về chúc mừng (お祝いについて話し合う)
 */

window.KAIWA_TOPICS_DATA = [
    {
        id: "topic1",
        num: 1,
        title: "Bảo Vệ Sức Khoẻ",
        titleJp: "けんこうを まもる (健康管理)",
        badge: "Chủ Đề 1 • Bài 15",
        lessonRef: "Marugoto A2.1 — Bài 15 (Sức khỏe & Thói quen)",
        image: "assets/img/kaiwa/topic1_bao_ve_suc_khoe.jpg",
        desc: "Khảo sát thói quen sinh hoạt lành mạnh, vận động, giấc ngủ, chế độ ăn uống cân bằng, thói quen uống rượu bia và làm thêm giờ.",
        coreQuestions: [
            {
                id: 1,
                qJp: "けんこうの ために、何を していますか。",
                qVi: "Để bảo vệ sức khỏe, bạn đang làm những gì?",
                intent: "Giáo viên muốn đánh giá cấu trúc mục đích 「〜のために」 và thói quen đang duy trì 「〜ています」 hoặc 「〜ように しています」.",
                mindmap: [
                    "Vận động (運動): Chạy bộ (ジョギング), đi bộ (散歩), tập gym (ジム)",
                    "Giấc ngủ (睡眠): Ngủ đủ 7-8 tiếng (7〜8時間寝る), giấc ngủ chất lượng (質の良い睡眠)",
                    "Ăn uống (食事): Bữa ăn cân bằng (バランスのとれた食事), ăn nhiều rau (野菜をたくさん食べる)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cơ bản (A2.1)",
                        jp: "毎朝、30分ぐらい ジョギングを しています。それから、野菜を たくさん 食べるように しています。",
                        vi: "Mỗi sáng tôi chạy bộ khoảng 30 phút. Ngoài ra, tôi cố gắng ăn nhiều rau củ.",
                        keyPoints: "Dùng thể tiếp diễn 「〜ています」 và mẫu 「〜ようにしています」 để thể hiện sự cố gắng tạo thói quen."
                    },
                    {
                        level: "advanced",
                        tag: "Tự nhiên / Mở rộng (A2+)",
                        jp: "ええと、健康のために、質の良い睡眠を とるように 心がけています。毎晩 11時に寝て、7時間半ぐらい 寝ています。それから、毎週末 公園で 軽く運動を しています。",
                        vi: "À, để bảo vệ sức khỏe, tôi luôn chú trọng có một giấc ngủ chất lượng. Mỗi tối tôi đi ngủ lúc 11 giờ và ngủ khoảng 7 tiếng rưỡi. Ngoài ra, cuối tuần nào tôi cũng vận động nhẹ ở công viên.",
                        keyPoints: "Thêm từ liên kết tự nhiên 「ええと」, cụm từ đắt giá 「質の良い睡眠」 và 「心がけています」 (luôn để tâm chú ý)."
                    }
                ],
                vocab: [
                    { jp: "けんこう (健康)", vi: "Sức khỏe" },
                    { jp: "質の良い睡眠", vi: "Giấc ngủ chất lượng tốt" },
                    { jp: "バランスのとれた食事", vi: "Bữa ăn cân bằng dinh dưỡng" },
                    { jp: "軽い運動", vi: "Vận động nhẹ nhàng" }
                ]
            },
            {
                id: 2,
                qJp: "どのぐらい していますか。",
                qVi: "Bạn làm việc đó bao lâu / tuần mấy lần?",
                intent: "Giáo viên kiểm tra cách nói khoảng thời gian (〜時間/〜分), tần suất (週に〜回) hoặc thời gian đã bắt đầu (〜年前から).",
                mindmap: [
                    "Tần suất: 週に3回 (3 lần/tuần), 毎朝 (mỗi sáng), 週末だけ (chỉ cuối tuần)",
                    "Khoảng thời gian: 30分ぐらい (khoảng 30 phút), 1時間 (1 tiếng)",
                    "Thâm niên: 半年前から (từ nửa năm trước), 1年ぐらい続けている (đã duy trì 1 năm)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cơ bản (A2.1)",
                        jp: "1週間に 3回ぐらい しています。1回に 30分ぐらい 走ります。",
                        vi: "Tôi chạy khoảng 3 lần một tuần. Mỗi lần chạy khoảng 30 phút.",
                        keyPoints: "Cấu trúc tần suất chuẩn: 「1週間に〜回」."
                    },
                    {
                        level: "advanced",
                        tag: "Tự nhiên / Mở rộng (A2+)",
                        jp: "去年の 4月から 始めて、もう 1年ぐらい 続けています。忙しい時でも、週に 2回は 必ず 走るように しています。",
                        vi: "Tôi bắt đầu từ tháng 4 năm ngoái, đến nay đã duy trì được khoảng 1 năm rồi. Ngay cả khi bận rộn, tôi cũng cố gắng chạy ít nhất 2 lần một tuần.",
                        keyPoints: "Dùng cấu trúc 「〜から始めて、〜続けています」 thể hiện tính kiên trì, rất được giáo viên đánh giá cao."
                    }
                ],
                vocab: [
                    { jp: "1週間に (いっしゅうかんに)", vi: "Trong một tuần..." },
                    { jp: "続けています (つづけています)", vi: "Đang tiếp tục / duy trì" },
                    { jp: "必ず (かならず)", vi: "Nhất định / chắc chắn" }
                ]
            },
            {
                id: 3,
                qJp: "ビールは 飲みますか。",
                qVi: "Bạn có uống bia (rượu bia) không?",
                intent: "Đánh giá khả năng dùng trạng từ tần suất: よく (thường xuyên), ときどき (thỉnh thoảng), あまり (không mấy khi), 全然 (hoàn toàn không).",
                mindmap: [
                    "Có uống vừa phải: ときどき / 週末に友達と1杯だけ (thỉnh thoảng, cuối tuần 1 ly với bạn)",
                    "Không uống: 全然飲みません / お酒が弱いです (hoàn toàn không uống, tửu lượng yếu)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Nếu có uống vừa phải",
                        jp: "はい、ときどき 飲みます。でも、健康のために、たくさん 飲みません。週末に 1杯か2杯だけです。",
                        vi: "Vâng, thỉnh thoảng tôi có uống. Nhưng vì sức khỏe nên tôi không uống nhiều. Cuối tuần chỉ uống 1 hoặc 2 cốc thôi.",
                        keyPoints: "Nhấn mạnh uống có kiểm soát 「〜だけ」 để gắn với chủ đề sức khỏe."
                    },
                    {
                        level: "advanced",
                        tag: "Nếu không uống",
                        jp: "いいえ、全然 飲みません。お酒が あまり 強くないですから、飲み会の 時も お茶や 水を 飲んでいます。",
                        vi: "Dạ không, tôi hoàn toàn không uống. Vì tôi không giỏi uống rượu nên ngay cả khi đi liên hoan tôi cũng chỉ uống trà hoặc nước lọc.",
                        keyPoints: "Dùng 「お酒が強くない」 thay vì nói cộc lốc 「きらい」 để nghe lịch sự, tự nhiên hơn."
                    }
                ],
                vocab: [
                    { jp: "ときどき", vi: "Thỉnh thoảng" },
                    { jp: "全然〜ない (ぜんぜん)", vi: "Hoàn toàn không..." },
                    { jp: "お酒が弱い (おさけがよわい)", vi: "Tửu lượng yếu / không uống được rượu" }
                ]
            },
            {
                id: 4,
                qJp: "どうしてですか。",
                qVi: "Tại sao lại như vậy?",
                intent: "Kiểm tra kỹ năng giải thích nguyên nhân lý do bằng cấu trúc 「〜から / 〜ですから」 hoặc 「〜と、〜になりますから」.",
                mindmap: [
                    "Lý do không uống / uống ít: Uống nhiều hôm sau mệt (次の日に体がだるい), có hại cho dạ dày (胃に悪い)",
                    "Lý do thỉnh thoảng uống: Vui vẻ khi trò chuyện với bạn (友達と話すのが楽しい), giải tỏa stress (ストレス解消)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Giải thích lý do bảo vệ sức khỏe",
                        jp: "ビールを たくさん 飲むと、次の日に 体の調子が 悪くなりますから。健康が 一番 大切ですから。",
                        vi: "Vì nếu uống nhiều bia, ngày hôm sau cơ thể sẽ mệt mỏi. Sức khỏe là quan trọng nhất mà.",
                        keyPoints: "Mẫu câu điều kiện hễ-thì: 「V-ると、〜」 kết hợp giải thích lý do 「〜から」."
                    },
                    {
                        level: "advanced",
                        tag: "Giải thích lý do thư giãn",
                        jp: "週末に 仲の良い友達と 話しながら 飲むと、リラックスできますから。1週間の ストレス解消に なります。",
                        vi: "Vì vừa uống vừa trò chuyện cùng bạn thân vào cuối tuần giúp tôi thư giãn. Đó là cách giải tỏa căng thẳng sau một tuần làm việc.",
                        keyPoints: "Cấu trúc vừa làm A vừa làm B: 「V-ながら」 rất tự nhiên ở cấp độ A2."
                    }
                ],
                vocab: [
                    { jp: "体の調子 (からだのちょうし)", vi: "Tình trạng sức khỏe / cơ thể" },
                    { jp: "ストレス解消 (ストレスかいしょう)", vi: "Giải tỏa căng thẳng" },
                    { jp: "リラックスする", vi: "Thư giãn" }
                ]
            },
            {
                id: 5,
                qJp: "よく ざんぎょうを しますか。",
                qVi: "Bạn có thường làm thêm giờ (tăng ca) không?",
                intent: "Hỏi về môi trường học tập/làm việc và quản lý thời gian nghỉ ngơi.",
                mindmap: [
                    "Không hay làm: あまりしません (ít khi), 定時に帰ります (về đúng giờ)",
                    "Thỉnh thoảng bận: 忙しい時だけ (chỉ khi bận), 月に2〜3回 (2-3 lần/tháng)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cơ bản (A2.1)",
                        jp: "いいえ、あまり しません。健康のために、定時に 帰るように しています。",
                        vi: "Dạ không, tôi không hay làm thêm. Vì sức khỏe, tôi cố gắng về đúng giờ.",
                        keyPoints: "Cụm từ 「定時に帰る」 (về đúng giờ tan sở/tan học) là từ vựng rất chuẩn."
                    },
                    {
                        level: "advanced",
                        tag: "Tự nhiên / Mở rộng (A2+)",
                        jp: "仕事が 忙しい時は 週に 1回か2回 しますが、あまり 残業は しません。夜遅くまで 残業すると 睡眠不足に なりますから、できるだけ 早く帰るように しています。",
                        vi: "Khi công việc bận rộn thì mỗi tuần tôi làm thêm 1-2 lần, nhưng nhìn chung tôi không hay tăng ca. Vì làm thêm đến khuya sẽ bị thiếu ngủ nên tôi cố gắng về nhà sớm nhất có thể.",
                        keyPoints: "Dùng từ vựng 「睡眠不足 (thiếu ngủ)」 và liên từ 「できるだけ (hết sức có thể)」."
                    }
                ],
                vocab: [
                    { jp: "残業 (ざんぎょう)", vi: "Làm thêm giờ / tăng ca" },
                    { jp: "定時 (ていじ)", vi: "Đúng giờ quy định" },
                    { jp: "睡眠不足 (すいみんぶそく)", vi: "Thiếu ngủ" },
                    { jp: "できるだけ", vi: "Hết sức có thể / cố gắng tối đa" }
                ]
            }
        ],
        fullDialogue: [
            { speaker: "sensei", name: "Sensei (Cô giáo)", jp: "こんにちは。今日は 健康についての お話を 聞かせてくださいね。", vi: "Chào em. Hôm nay em hãy chia sẻ về chủ đề sức khỏe nhé." },
            { speaker: "gakusei", name: "Bạn (Học sinh)", jp: "はい、先生。よろしくお願いします！", vi: "Vâng thưa cô, em xin phép bắt đầu ạ!" },
            { speaker: "sensei", name: "Sensei", jp: "まず、けんこうの ために、何を していますか。", vi: "Trước hết, để bảo vệ sức khỏe, em đang làm những gì?" },
            { speaker: "gakusei", name: "Bạn", jp: "ええと、毎朝 30分ぐらい ジョギングを しています。それから、バランスのとれた食事と、質の良い睡眠を とるように 心がけています。", vi: "Dạ, mỗi sáng em chạy bộ khoảng 30 phút. Ngoài ra, em luôn cố gắng ăn uống cân bằng và ngủ đủ giấc chất lượng ạ." },
            { speaker: "sensei", name: "Sensei", jp: "ジョギングですか、いいですね！どのぐらい していますか。", vi: "Chạy bộ à, tốt quá! Em tập thói quen này bao lâu rồi?" },
            { speaker: "gakusei", name: "Bạn", jp: "去年の春から 始めて、もう 1年ぐらい 続けています。週に 3回は 必ず 走っています。", vi: "Em bắt đầu từ mùa xuân năm ngoái, đến nay đã duy trì được khoảng 1 năm rồi ạ. Mỗi tuần em đều chạy ít nhất 3 lần." },
            { speaker: "sensei", name: "Sensei", jp: "素晴らしいですね。ところで、ビールや お酒は 飲みますか。", vi: "Tuyệt vời quá. Tiện đây cho cô hỏi, em có uống bia rượu không?" },
            { speaker: "gakusei", name: "Bạn", jp: "いいえ、全然 飲みません。お酒が あまり 強くないですから。", vi: "Dạ không, em hoàn toàn không uống ạ. Vì tửu lượng của em không tốt." },
            { speaker: "sensei", name: "Sensei", jp: "そうなんですね。どうして 飲まないように しているんですか。", vi: "Vậy à. Tại sao em lại chọn không uống rượu bia?" },
            { speaker: "gakusei", name: "Bạn", jp: "お酒を 飲むと、頭が 痛くなって 次の日に 勉強が できませんから。健康が 一番 大切ですから。", vi: "Dạ vì nếu uống rượu vào, em sẽ bị đau đầu và ngày hôm sau không thể học được. Sức khỏe vẫn là quan trọng nhất ạ." },
            { speaker: "sensei", name: "Sensei", jp: "なるほど、その通りですね。では、普段 よく ざんぎょうや 夜遅くまでの 勉強を しますか。", vi: "Ra là vậy, đúng thế thật. Thế bình thường em có hay thức khuya làm việc hoặc học bài không?" },
            { speaker: "gakusei", name: "Bạn", jp: "いいえ、あまり しません。夜遅くまで 勉強すると 睡眠不足に なりますから、毎日 11時前には 寝るように しています。", vi: "Dạ không, em không hay thức khuya. Vì học muộn sẽ bị thiếu ngủ nên mỗi ngày em đều cố gắng đi ngủ trước 11 giờ ạ." },
            { speaker: "sensei", name: "Sensei", jp: "とても 良い生活習慣ですね。しっかりと 答えられました。ありがとうございます！", vi: "Thói quen sinh hoạt của em rất tốt. Em đã trả lời rất lưu loát và rõ ràng. Cảm ơn em nhé!" },
            { speaker: "gakusei", name: "Bạn", jp: "どうも ありがとうございました！", vi: "Em cảm ơn cô nhiều ạ!" }
        ]
    },
    {
        id: "topic2",
        num: 2,
        title: "Hỏi Han Về Sức Khỏe",
        titleJp: "けんこうについて きづかう・アドバイス",
        badge: "Chủ Đề 2 • Bài 16",
        lessonRef: "Marugoto A2.1 — Bài 16 (Thăm hỏi & Lời khuyên sức khỏe)",
        image: "assets/img/kaiwa/topic2_hoi_han_suc_khoe.jpg",
        desc: "Thực hành hỏi thăm khi đồng nghiệp/bạn bè bị ốm, mệt mỏi, đau đầu, sốt; đề nghị giúp đỡ và đưa ra lời khuyên nghỉ ngơi hợp lý.",
        coreQuestions: [
            {
                id: 1,
                qJp: "どうしたんですか。",
                qVi: "Bạn bị làm sao thế? / Có chuyện gì vậy?",
                intent: "Đánh giá cách diễn đạt tình trạng sức khỏe, triệu chứng bằng thể 「〜んです」 (giải thích lý do/tình trạng).",
                mindmap: [
                    "Đau đầu: 頭が痛いんです (ズキズキ痛い)",
                    "Bị sốt: 熱があるんです (38度あります)",
                    "Đau bụng: お腹が痛いんです / 気持ちが悪いんです",
                    "Cảm cúm: 風邪をひいたんです / 喉が痛いんです",
                    "Mệt mỏi: 最近残業が多くて、とても疲れているんです"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Đau đầu & sốt nhẹ",
                        jp: "きのうから ちょっと 頭が 痛くて、熱も あるんです。",
                        vi: "Từ hôm qua tôi hơi bị đau đầu, và người cũng có chút sốt nữa.",
                        keyPoints: "Dùng thể nối 「〜て」 để liên kết 2 triệu chứng và kết thúc bằng 「〜んです」."
                    },
                    {
                        level: "advanced",
                        tag: "Cảm cúm & đau họng",
                        jp: "実は、きのうの夜から 風邪を ひいてしまって、喉が 痛くて 声が 出にくいんです。体も 少し だるいです。",
                        vi: "Thực ra là từ tối qua tôi lỡ bị cảm mất rồi, họng đau nên khó phát ra tiếng. Cả người cũng hơi uể oải nữa.",
                        keyPoints: "Thêm từ mở đầu tự nhiên 「実は (thực ra là)」 và cấu trúc khó làm gì 「〜にくい」."
                    }
                ],
                vocab: [
                    { jp: "どうしたんですか", vi: "Có chuyện gì thế? / Bị làm sao vậy?" },
                    { jp: "頭が痛い (あたまがいたい)", vi: "Đau đầu" },
                    { jp: "熱がある (ねつがある)", vi: "Bị sốt" },
                    { jp: "喉が痛い (のどがいたい)", vi: "Đau họng" },
                    { jp: "体がだるい", vi: "Cơ thể uể oải, rã rời" }
                ]
            },
            {
                id: 2,
                qJp: "くすりは 飲みましたか。",
                qVi: "Bạn đã uống thuốc chưa?",
                intent: "Kiểm tra cách dùng phó từ thời gian: もう (đã rồi), まだ (vẫn chưa) và trợ từ liên kết.",
                mindmap: [
                    "Đã uống: はい、朝飲みました (đã uống ban sáng), 病院の薬を飲みました",
                    "Chưa uống: いいえ、まだ飲んでいません (chưa uống), 薬を持っていません (không có sẵn thuốc)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Đã uống thuốc",
                        jp: "はい、朝 ご飯の あとで 風邪薬を 飲みました。でも、まだ あまり よくなりません。",
                        vi: "Vâng, sáng nay sau bữa ăn tôi đã uống thuốc cảm rồi. Nhưng vẫn chưa thấy đỡ lắm.",
                        keyPoints: "Cụm từ 「ご飯のあとで」 (sau bữa ăn) và liên từ đối lập 「でも (nhưng)」."
                    },
                    {
                        level: "advanced",
                        tag: "Chưa uống thuốc",
                        jp: "いいえ、まだ 飲んでいません。薬を 持っていませんから、帰りに 薬局で 買って 飲もうと 思います。",
                        vi: "Chưa, tôi vẫn chưa uống. Vì không mang sẵn thuốc theo nên lúc về tôi định ghé hiệu thuốc mua rồi uống.",
                        keyPoints: "Cấu trúc dự định 「V-ようと思っています」 kết hợp với từ chỉ địa điểm mua thuốc 「薬局 (やっきょく)」."
                    }
                ],
                vocab: [
                    { jp: "風邪薬 (かぜぐすり)", vi: "Thuốc cảm" },
                    { jp: "薬局 (やっきょく)", vi: "Hiệu thuốc / Nhà thuốc" },
                    { jp: "よくなります", vi: "Trở nên đỡ hơn / khỏe hơn" }
                ]
            },
            {
                id: 3,
                qJp: "何か てつだいましょうか。",
                qVi: "Tôi có thể giúp gì cho bạn không?",
                intent: "Học sinh có thể đóng vai người tiếp nhận lời đề nghị (cảm ơn và nhờ vả lịch sự), hoặc đóng vai người đi hỏi han bạn bè.",
                mindmap: [
                    "Đồng ý nhờ vả: ありがとうございます。じゃ、〜をお願いしてもいいですか",
                    "Từ chối khéo: お気遣いありがとうございます。でも大丈夫です"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cảm ơn và nhờ giúp",
                        jp: "ありがとうございます。じゃ、すみませんが、この 書類の コピーを お願いしても いいですか。",
                        vi: "Cảm ơn bạn nhiều. Vậy xin lỗi làm phiền bạn photo giúp tôi tập tài liệu này được không?",
                        keyPoints: "Cấu trúc xin phép lịch sự: 「V-てもいいですか」."
                    },
                    {
                        level: "advanced",
                        tag: "Từ chối khéo léo, tự làm được",
                        jp: "お気遣い ありがとうございます。でも、もうすぐ 終わりますから 大丈夫ですよ。お気持ちだけで 嬉しいです。",
                        vi: "Cảm ơn bạn đã quan tâm. Nhưng việc này sắp xong rồi nên tôi ổn. Chỉ cần tấm lòng của bạn là tôi thấy vui rồi.",
                        keyPoints: "Mẫu câu giao tiếp chuẩn Nhật: 「お気遣いありがとうございます (Cảm ơn vì đã chu đáo quan tâm)」."
                    }
                ],
                vocab: [
                    { jp: "手伝います (てつだいます)", vi: "Giúp đỡ" },
                    { jp: "書類 (しょるい)", vi: "Tài liệu / giấy tờ" },
                    { jp: "お気遣い (おきづかい)", vi: "Sự chu đáo / quan tâm" }
                ]
            },
            {
                id: 4,
                qJp: "早く かえると いいですよ。",
                qVi: "Bạn nên về nhà sớm đi thì tốt đấy.",
                intent: "Mẫu câu đưa ra lời khuyên nhẹ nhàng 「V-ると いいですよ」 (Nếu làm... thì tốt đấy - Bài 16).",
                mindmap: [
                    "Đồng ý tiếp thu: ええ、そうします (vâng, tôi sẽ làm vậy)",
                    "Cảm ơn vì lời khuyên: ありがとうございます (cảm ơn bạn)",
                    "Kế hoạch nghỉ ngơi: 帰ってすぐ寝ます (về nhà sẽ ngủ ngay)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Tiếp thu lời khuyên",
                        jp: "ええ、そうします。今日の 仕事が 終わったら、すぐ 帰って ゆっくり 休もうと 思います。ありがとうございます。",
                        vi: "Vâng, tôi sẽ làm vậy. Xong công việc hôm nay là tôi sẽ về ngay để nghỉ ngơi thật thoải mái. Cảm ơn bạn nhé.",
                        keyPoints: "Mẫu đáp lại lời khuyên chuẩn: 「ええ、そうします (Vâng, tôi sẽ làm thế)」."
                    },
                    {
                        level: "advanced",
                        tag: "Đóng vai người khuyên lại",
                        jp: "ええ、ありがとうございます。先生（同僚）も 無理を しないでくださいね。帰ったら 暖かくして ぐっすり 寝ます。",
                        vi: "Dạ vâng, em cảm ơn cô ạ. Cô (bạn) cũng đừng làm việc quá sức nhé. Về nhà em sẽ giữ ấm rồi ngủ một giấc thật ngon.",
                        keyPoints: "Thêm lời khuyên ngược lại 「無理をしないでくださいね」 và từ láy tượng hình 「ぐっすり (ngon giấc)」."
                    }
                ],
                vocab: [
                    { jp: "〜といいですよ", vi: "Nên làm... thì tốt đấy (lời khuyên)" },
                    { jp: "ゆっくり休む", vi: "Nghỉ ngơi thong thả / thoải mái" },
                    { jp: "無理をしない (むりをしない)", vi: "Không làm việc quá sức" },
                    { jp: "暖かくする (あたたかくする)", vi: "Giữ ấm cơ thể" }
                ]
            },
            {
                id: 5,
                qJp: "どうしてですか。",
                qVi: "Tại sao lại như vậy? (Tại sao khuyên về sớm? / Tại sao bị ốm?)",
                intent: "Hỏi sâu về nguyên nhân khuyên nhủ hoặc lý do phát sinh bệnh tật.",
                mindmap: [
                    "Lý do khuyên: Trông sắc mặt rất nhợt nhạt (顔色が悪い), cố quá sẽ ngất (無理すると倒れる)",
                    "Lý do bị ốm: Thời tiết đổi mùa đột ngột (急に寒くなった), ngủ quên bật điều hòa (エアコンをつけっぱなし)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Nếu giải thích vì sao khuyên về sớm",
                        jp: "顔色が とても 悪いですから。無理を して 倒れたら 大変ですから、早く帰って 病院に 行ったほうが いいですよ。",
                        vi: "Vì sắc mặt bạn trông xanh xao lắm. Nếu cố quá mà ngất xỉu thì nguy hiểm, nên về sớm rồi đi khám bệnh là tốt nhất đấy.",
                        keyPoints: "Mẫu khuyên răn mạnh hơn: 「V-たほうがいいですよ」."
                    },
                    {
                        level: "advanced",
                        tag: "Nếu giải thích vì sao bị ốm",
                        jp: "最近、急に 気温が 下がって 寒くなりましたから。きのう エアコンを つけたまま 寝てしまって、風邪を ひいたようです。",
                        vi: "Vì dạo gần đây nhiệt độ đột ngột giảm mạnh và trời trở lạnh. Tối qua tôi lỡ để nguyên điều hòa rồi ngủ quên mất, hình như đã bị cảm rồi.",
                        keyPoints: "Mẫu câu phán đoán nhẹ nhàng 「〜ようです」 và trạng thái 「V-たまま」."
                    }
                ],
                vocab: [
                    { jp: "顔色が悪い (かおいろがわるい)", vi: "Sắc mặt nhợt nhạt / xanh xao" },
                    { jp: "倒れます (たおれます)", vi: "Ngã / xỉu / kiệt sức ngã gục" },
                    { jp: "急に (きゅうに)", vi: "Đột ngột / bất ngờ" },
                    { jp: "病院に行ったほうがいい", vi: "Nên đi bệnh viện khám thì hơn" }
                ]
            }
        ],
        fullDialogue: [
            { speaker: "sensei", name: "Sensei", jp: "あれ、ダンさん、顔色が 悪いですね。どうしたんですか。", vi: "Ủa, Dan ơi, sắc mặt em trông nhợt nhạt thế. Em bị làm sao vậy?" },
            { speaker: "gakusei", name: "Bạn", jp: "実は、きのうの夜から ちょっと 頭が 痛くて、熱も 37度5分 あるんです。", vi: "Thực ra là từ tối qua em hơi bị đau đầu, và đang sốt 37 độ 5 nữa ạ." },
            { speaker: "sensei", name: "Sensei", jp: "まあ、それは 大変ですね！くすりは もう 飲みましたか。", vi: "Trời, thế thì mệt rồi! Em đã uống thuốc gì chưa?" },
            { speaker: "gakusei", name: "Bạn", jp: "はい、朝 ご飯を 食べてから、風邪薬を 飲みました。でも、まだ 効いていないようです。", vi: "Dạ rồi, sáng sau khi ăn cơm em đã uống thuốc cảm. Nhưng hình như thuốc vẫn chưa ngấm lắm ạ." },
            { speaker: "sensei", name: "Sensei", jp: "そうですか。辛そうですね。何か てつだいましょうか。", vi: "Vậy à. Trông em vất vả quá. Cô có thể giúp gì cho em không?" },
            { speaker: "gakusei", name: "Bạn", jp: "先生、ありがとうございます。この 授業の プリントを あとで メールで 送っていただけると 助かります。", vi: "Dạ em cảm ơn cô ạ. Nếu sau giờ học cô gửi tài liệu bài học qua email giúp em thì tốt quá ạ." },
            { speaker: "sensei", name: "Sensei", jp: "ええ、もちろんですよ。無理を しないで、早く かえると いいですよ。", vi: "Ừ, đương nhiên rồi. Đừng cố quá nhé, em nên xin về sớm nghỉ ngơi đi." },
            { speaker: "gakusei", name: "Bạn", jp: "ええ、そうします。どうして 先生は 私が 具合が 悪いと 分かったんですか。", vi: "Vâng, em sẽ làm vậy ạ. Cơ mà sao cô biết em đang thấy không khỏe thế ạ?" },
            { speaker: "sensei", name: "Sensei", jp: "声が いつもより 小さくて、元気が なさそうでしたから。今日は 暖かくして ゆっくり 休んでくださいね。", vi: "Vì giọng em nhỏ hơn bình thường và trông thiếu sức sống hẳn. Hôm nay nhớ giữ ấm và nghỉ ngơi thật nhiều nhé." },
            { speaker: "gakusei", name: "Bạn", jp: "はい、本当に ありがとうございます。お先に 失礼します！", vi: "Vâng, em thực sự cảm ơn cô rất nhiều ạ. Em xin phép về trước ạ!" }
        ]
    },
    {
        id: "topic3",
        num: 3,
        title: "Trao Đổi Về Chúc Mừng",
        titleJp: "お祝いについて はなしあう (結婚パーティー)",
        badge: "Chủ Đề 3 • Bài 17-18",
        lessonRef: "Marugoto A2.1 — Bài 17 & 18 (Quà tặng, Sự kiện & Tiệc tùng)",
        image: "assets/img/kaiwa/topic3_trao_doi_chuc_mung.jpg",
        desc: "Thảo luận lên kế hoạch tổ chức tiệc mừng kết hôn cho anh/chị Lê (レーさん): quà tặng, số lượng người tham gia, địa điểm tổ chức và giữ bí mật bất ngờ (Surprise).",
        coreQuestions: [
            {
                id: 1,
                qJp: "レーさんの 結婚の お祝いパーティー、どうしますか。",
                qVi: "Tiệc chúc mừng kết hôn của anh Lê, chúng mình làm thế nào đây?",
                intent: "Đánh giá khả năng đề xuất ý kiến, rủ rê hợp tác bằng cấu trúc 「V-ましょう / V-ませんか」 và 「〜はどうですか」.",
                mindmap: [
                    "Tổ chức tiệc ăn uống: みんなで食事会をしましょう (cùng tổ chức tiệc ăn uống)",
                    "Thời gian: 来週の金曜日の夜 (tối thứ 6 tuần sau), 週末 (cuối tuần)",
                    "Hình thức: Bí mật làm bất ngờ (サプライズパーティーにしましょう)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cơ bản (A2.1)",
                        jp: "来週の 金曜日の 夜に、みんなで レストランで お祝いの 食事会を しませんか。",
                        vi: "Tối thứ sáu tuần sau, mọi người cùng tổ chức một bữa tiệc ăn uống chúc mừng ở nhà hàng nhé?",
                        keyPoints: "Mẫu câu rủ rê thân thiện: 「V-ませんか」."
                    },
                    {
                        level: "advanced",
                        tag: "Tự nhiên / Mở rộng (A2+)",
                        jp: "そうですね！レーさんのために サプライズパーティーを 開きましょう。来週の 金曜日の 夜なら、みんな 集まりやすいと 思います。",
                        vi: "Ý kiến hay đó! Chúng mình hãy tổ chức một bữa tiệc bất ngờ (surprise party) cho anh Lê đi. Tôi nghĩ tối thứ sáu tuần sau thì mọi người sẽ dễ tập hợp đông đủ nhất.",
                        keyPoints: "Dùng từ mượn tiếng Anh phổ biến trong văn hóa Nhật 「サプライズパーティー」 và đuôi khả năng 「集まりやすい」."
                    }
                ],
                vocab: [
                    { jp: "お祝いパーティー (おいわいパーティー)", vi: "Tiệc chúc mừng" },
                    { jp: "結婚 (けっこん)", vi: "Kết hôn / đám cưới" },
                    { jp: "サプライズ", vi: "Bất ngờ (Surprise)" },
                    { jp: "集まります (あつまります)", vi: "Tập hợp / tụ họp" }
                ]
            },
            {
                id: 2,
                qJp: "プレゼントは 何を あげますか。",
                qVi: "Chúng ta sẽ tặng món quà gì cho anh ấy?",
                intent: "Kiểm tra động từ cho tặng 「あげる」 và đưa ra gợi ý đồ vật phù hợp với cuộc sống mới của người mới cưới.",
                mindmap: [
                    "Đồ gia dụng (家電): コーヒーメーカー (máy pha cà phê), 電子レンジ (lò vi sóng)",
                    "Đồ dùng gia đình: ペアの食器セット (bộ bát đĩa đôi), タオルセット (bộ khăn cao cấp)",
                    "Kỷ niệm: フォトアルバム (album ảnh), 花束 (bó hoa)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cơ bản (A2.1)",
                        jp: "新しい 生活で 使える 家電が いいと 思います。例えば、コーヒーメーカーはどうですか。",
                        vi: "Tôi nghĩ đồ điện gia dụng dùng cho cuộc sống mới sẽ rất tốt. Ví dụ như máy pha cà phê thì sao?",
                        keyPoints: "Dùng 「例えば (ví dụ như)」 và mẫu gợi ý 「〜はどうですか」."
                    },
                    {
                        level: "advanced",
                        tag: "Tự nhiên / Mở rộng (A2+)",
                        jp: "みんなで お金を 出し合って、ペアの 食器セットか コーヒーメーカーを 贈るのは どうでしょうか。それから、みんなの お祝いメッセージカードも 一緒に 渡しましょう。",
                        vi: "Hay là cả nhóm mình cùng góp tiền, mua tặng anh ấy một bộ bát đĩa đôi hoặc máy pha cà phê nhé? Ngoài ra, chúng mình cũng chuẩn bị thêm tấm thiệp ghi lời chúc của tất cả mọi người nữa.",
                        keyPoints: "Cụm từ rất chuẩn: 「お金を出し合う (góp tiền chung)」 và hành động ý nghĩa 「メッセージカードを渡す」."
                    }
                ],
                vocab: [
                    { jp: "プレゼントをあげる", vi: "Tặng quà" },
                    { jp: "生活で使えるもの", vi: "Đồ dùng hữu ích trong cuộc sống" },
                    { jp: "コーヒーメーカー", vi: "Máy pha cà phê" },
                    { jp: "ペアの食器 (ペアのしょっき)", vi: "Bộ bát đĩa đồ đôi dành cho vợ chồng" },
                    { jp: "お金を出し合う (おあかねをだしあう)", vi: "Cùng nhau góp tiền" }
                ]
            },
            {
                id: 3,
                qJp: "何人 参加しますか。",
                qVi: "Có bao nhiêu người tham gia?",
                intent: "Kiểm tra số từ đếm người (ひとり、ふたり、〜にん) và cách ước lượng chừng chừng (〜ぐらい / 〜人ほど).",
                mindmap: [
                    "Khoảng 10 người: 10人ぐらい (だいたい10人)",
                    "Thành phần: クラスメイト8人と先生2人 (8 bạn trong lớp và 2 giáo viên)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cơ bản (A2.1)",
                        jp: "クラスの みんなと 先生で、全部で 10人ぐらい 参加します。",
                        vi: "Các bạn trong lớp và thầy cô, tổng cộng khoảng 10 người tham gia.",
                        keyPoints: "Sử dụng 「全部で (tổng cộng)」 và lượng từ 「〜人ぐらい」."
                    },
                    {
                        level: "advanced",
                        tag: "Tự nhiên / Mở rộng (A2+)",
                        jp: "今のところ、クラスメイトが 8人、先生が 2人で、だいたい 10人から 12人ぐらいに なると 思います。",
                        vi: "Tính đến hiện tại thì có 8 bạn cùng lớp và 2 thầy cô, em nghĩ sẽ tầm khoảng 10 đến 12 người ạ.",
                        keyPoints: "Cụm từ 「今のところ (tính đến thời điểm này)」 và khoảng ước tính 「10人から12人ぐらい」."
                    }
                ],
                vocab: [
                    { jp: "参加します (さんかします)", vi: "Tham gia" },
                    { jp: "全部で (ぜんぶで)", vi: "Tổng cộng" },
                    { jp: "今のところ (いまのところ)", vi: "Tính đến hiện tại / hiện giờ" }
                ]
            },
            {
                id: 4,
                qJp: "どこで しますか。",
                qVi: "Tổ chức tiệc ở đâu?",
                intent: "Hỏi về địa điểm tổ chức sự kiện (trợ từ で) và nêu lý do chọn địa điểm đó (gần ga, đồ ăn ngon, có phòng riêng).",
                mindmap: [
                    "Quán Việt Nam: ベトナム料理店 (đồ ăn hợp khẩu vị, anh Lê thích)",
                    "Quán Nhật / Izakaya: 居酒屋 (ấm cúng, có phòng riêng 個室)",
                    "Gần ga / gần trường: 駅の近く / 大学の近く (thuận tiện đi lại 交通が便利)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Cơ bản (A2.1)",
                        jp: "大学の 近くの ベトナム料理の レストランで します。広くて 料理も 美味しいですから。",
                        vi: "Tổ chức ở nhà hàng món Việt gần trường đại học. Vì ở đó rộng rãi và đồ ăn cũng rất ngon.",
                        keyPoints: "Mẫu câu nêu địa điểm 「〜でします」 kèm lý do 「〜ですから」."
                    },
                    {
                        level: "advanced",
                        tag: "Tự nhiên / Mở rộng (A2+)",
                        jp: "駅前の『サイゴン・カフェ』という レストランは どうでしょうか。個室が あって 静かですし、レーさんの 好きな ベトナム料理も 楽しめますよ。",
                        vi: "Nhà hàng tên là 'Saigon Cafe' ở trước nhà ga thì thế nào ạ? Ở đó có phòng riêng yên tĩnh, lại còn được thưởng thức những món Việt mà anh Lê rất thích nữa.",
                        keyPoints: "Cấu trúc gọi tên 「〜という」, liệt kê lý do 「〜ですし、〜ですし」 và thể khả năng 「楽しめます」."
                    }
                ],
                vocab: [
                    { jp: "駅前 (えきまえ)", vi: "Khu vực trước nhà ga" },
                    { jp: "個室 (こしつ)", vi: "Phòng riêng biệt" },
                    { jp: "予約します (よやくします)", vi: "Đặt chỗ / đặt bàn trước" }
                ]
            },
            {
                id: 5,
                qJp: "レーさんに 言いましたか。",
                qVi: "Bạn đã nói với anh Lê chưa?",
                intent: "Kiểm tra cách dùng 「まだ〜ていません」 và lý do muốn giữ bí mật tạo bất ngờ (サプライズ).",
                mindmap: [
                    "Chưa nói (Bí mật): いいえ、まだ言っていません (chưa nói, muốn làm bất ngờ 内緒)",
                    "Đã dò hỏi ngày rảnh: 予定だけ聞きました (chỉ mới hỏi lịch xem có rảnh không)"
                ],
                sampleAnswers: [
                    {
                        level: "basic",
                        tag: "Giữ bí mật làm bất ngờ (Khuyên dùng)",
                        jp: "いいえ、まだ 言っていません！サプライズパーティーに したいですから、当日まで 内緒に しましょう！",
                        vi: "Chưa, tôi vẫn chưa nói đâu! Vì muốn làm một bữa tiệc bất ngờ (surprise) nên chúng mình hãy giữ bí mật đến đúng hôm đó nhé!",
                        keyPoints: "Từ vựng cực đắt giá: 「内緒 (ないしょ - giữ bí mật)」 và 「当日 (とうじつ - ngày diễn ra)」."
                    },
                    {
                        level: "advanced",
                        tag: "Đã hỏi lịch kín đáo",
                        jp: "パーティーのことは まだ 内緒ですが、来週の 金曜日の 予定だけ そっと 聞きました。『夜は 空いている』と 言っていましたので、バッチリです！",
                        vi: "Chuyện tiệc tùng thì tôi vẫn giữ bí mật, nhưng tôi đã kín đáo hỏi lịch tối thứ sáu tuần sau rồi. Anh ấy bảo 'tối đó rảnh rỗi' nên mọi thứ hoàn hảo luôn!",
                        keyPoints: "Từ tượng trưng tinh tế: 「そっと (kín đáo/nhẹ nhàng)」 và từ cảm thán khẩu ngữ 「バッチリです (chuẩn không cần chỉnh/hoàn hảo)」."
                    }
                ],
                vocab: [
                    { jp: "内緒 (ないしょ)", vi: "Bí mật / không nói cho ai biết" },
                    { jp: "当日 (とうじつ)", vi: "Ngày diễn ra sự kiện" },
                    { jp: "そっと", vi: "Kín đáo, khéo léo, nhẹ nhàng" },
                    { jp: "空いている (あいている)", vi: "Trống lịch / đang rảnh" }
                ]
            }
        ],
        fullDialogue: [
            { speaker: "sensei", name: "Sensei", jp: "もうすぐ レーさんの 結婚式ですね。お祝いパーティーはどうしますか。", vi: "Sắp đến đám cưới của bạn Lê rồi nhỉ. Tiệc chúc mừng các em tính thế nào rồi?" },
            { speaker: "gakusei", name: "Bạn", jp: "はい！来週の 金曜日の 夜に、みんなで お祝いの 食事会を 開こうと 計画しています。", vi: "Dạ! Tối thứ sáu tuần sau, chúng em đang lên kế hoạch cùng nhau mở một bữa tiệc ăn uống chúc mừng ạ." },
            { speaker: "sensei", name: "Sensei", jp: "いいですね！プレゼントは 何を あげるんですか。", vi: "Hay quá! Các em định tặng quà gì cho bạn ấy?" },
            { speaker: "gakusei", name: "Bạn", jp: "新しい 生活で 使える コーヒーメーカーを 贈ろうと 思っています。それから、クラスみんなの メッセージカードも 渡します。", vi: "Dạ tụi em định tặng một chiếc máy pha cà phê dùng cho cuộc sống mới. Ngoài ra còn tặng cả thiệp chúc mừng của cả lớp nữa ạ." },
            { speaker: "sensei", name: "Sensei", jp: "心のこもった 素敵なプレゼントですね。何人ぐらい 参加する予定ですか。", vi: "Món quà thật ấm áp và ý nghĩa. Dự kiến có khoảng bao nhiêu người tham gia vậy em?" },
            { speaker: "gakusei", name: "Bạn", jp: "クラスメイトが 8人と、先生方にも 2人 来ていただいて、全部で 10人か11人に なります。", vi: "Dạ có 8 bạn trong lớp và tụi em cũng kính mời 2 thầy cô nữa, tổng cộng sẽ tầm 10 hoặc 11 người ạ." },
            { speaker: "sensei", name: "Sensei", jp: "パーティーは どこで しますか。", vi: "Thế bữa tiệc sẽ tổ chức ở đâu?" },
            { speaker: "gakusei", name: "Bạn", jp: "駅の近くの『ハノイ・キッチン』という レストランで します。個室を 予約しましたので、ゆっくり お祝いが できます。", vi: "Dạ tổ chức ở quán 'Hanoi Kitchen' gần ga ạ. Tụi em đã đặt phòng riêng rồi nên có thể chúc mừng thoải mái và ấm cúng." },
            { speaker: "sensei", name: "Sensei", jp: "よく 準備しましたね。もう レーさんに 言いましたか。", vi: "Chuẩn bị chu đáo quá. Thế các em đã nói cho Lê biết chưa?" },
            { speaker: "gakusei", name: "Bạn", jp: "いいえ、まだ 言っていません！サプライズに したいですから、金曜日まで 内緒なんです。", vi: "Dạ chưa, tụi em vẫn chưa nói đâu ạ! Vì muốn tạo bất ngờ cho bạn ấy nên tụi em giữ bí mật tuyệt đối đến thứ sáu ạ." },
            { speaker: "sensei", name: "Sensei", jp: "ふふ、サプライズですね！きっと レーさんも 喜んでくれますよ。楽しみに していますね。", vi: "Haha, một bất ngờ thú vị đấy! Nhất định Lê sẽ vui lắm cho mà xem. Cô cũng rất mong chờ đấy." },
            { speaker: "gakusei", name: "Bạn", jp: "はい！先生も ぜひ 一緒に 楽しんでくださいね。ありがとうございました！", vi: "Dạ vâng! Hôm đó cô cùng tham gia chung vui với chúng em nhé. Em cảm ơn cô ạ!" }
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
            { jp: "そうですね、私の場合は…", vi: "Vâng, đối với trường hợp của em thì..." }
        ]
    },
    {
        title: "3. Công thức trả lời điểm 10 (Tránh cộc lốc)",
        desc: "Không bao giờ trả lời chỉ với 1 từ 'Hai' hoặc 'Iie'. Hãy luôn áp dụng công thức 3 vế:",
        formula: "[Khẳng định / Phủ định] ➔ [Chi tiết hành động / Tần suất] ➔ [Lý do: 〜から / 〜ので]",
        example: "VD: 「はい、ときどき 飲みます。でも、健康が 一番 大切ですから、たくさん 飲みません。」"
    },
    {
        title: "4. Kỹ thuật hỏi lại lịch sự khi không nghe rõ",
        desc: "Nếu lỡ cô giáo nói nhanh hoặc bạn nghe sót từ, đừng đoán mò hay sợ hãi. Hãy mỉm cười và nhờ cô nhắc lại một cách lịch sự:",
        phrases: [
            { jp: "すみません、もう一度 お願いします。", vi: "Xin lỗi cô, cô có thể nhắc lại một lần nữa được không ạ?" },
            { jp: "すみません、もう少し ゆっくり お願いできますか。", vi: "Xin lỗi cô, cô có thể nói chậm lại một chút giúp em được không ạ?" }
        ]
    },
    {
        title: "5. Nụ cười và Ánh mắt (Ngôn ngữ cơ thể)",
        desc: "Trong bài thi vấn đáp Kaiwa 5 phút, độ tự tin và nụ cười chiếm tới 30% ấn tượng của giám khảo. Luôn nhìn thẳng vào mắt giáo viên (Eye contact), nói to rõ ràng, không nhìn xuống đất hay nhìn lên trần nhà."
    }
];
