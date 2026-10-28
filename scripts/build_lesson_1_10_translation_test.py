#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for tests/On_Tap_Dich_Cau_Lesson_1_10.html
Ôn tập Từ Vựng, Ngữ Pháp, Chữ Hán Lesson 1 - Lesson 10 (Marugoto A2-1 / Elementary 1 A2, Topic 1 ~ Topic 5).
Hệ thống 40 câu tự luận dịch Việt -> Nhật với chấm điểm thông minh, công bằng, linh hoạt,
hỗ trợ nghe phát âm Tokyo TTS, giải thích ngữ pháp và nút tự duyệt điểm.
"""

import json

QUESTIONS_DATA = [
    {
        "id": 1,
        "type": "single",
        "vi": "Công viên Ueno rất rộng và nổi tiếng. Bên trong có sở thú.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Tính từ đuôi い nối bằng ～くて (広い ➔ 広くて). Động từ tồn tại đồ vật/địa điểm vô tri dùng あります (動物園が あります).",
        "modelJa": "上野公園は とても 広くて、有名です。中に 動物園が あります。",
        "modelHiragana": "うえのこうえんは とても ひろくて、ゆうめいです。なかに どうぶつえんが あります。",
        "acceptable": [
            "上野公園はとても広くて、有名です。中に動物園があります。",
            "上野公園はとても広くて有名です。中に動物園があります。",
            "うえのこうえんはとてもひろくて、ゆうめいです。なかにどうぶつえんがあります。",
            "上野公園は広くて、とても有名です。中に動物園があります。",
            "上野公園はとても広くて有名です。中には動物園があります。",
            "上野公園はすごく広くて有名です。中に動物園があります。"
        ],
        "keywords": ["上野公園", "広くて", "有名", "中", "動物園", "あります"],
        "keywordsHira": ["うえのこうえん", "ひろくて", "ゆうめい", "なか", "どうぶつえん", "あります"]
    },
    {
        "id": 2,
        "type": "single",
        "vi": "Akihabara có nhiều cửa hàng điện tử nên rất tiện lợi.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Mẫu câu chỉ nguyên nhân lý do: ～から / ～ので (ありますから / あるので). Cửa hàng điện tử: 電気屋 (でんきや) hoặc 電器店.",
        "modelJa": "秋葉原は 電器屋が たくさん ありますから、とても 便利です。",
        "modelHiragana": "あきはばらは でんきやが たくさん ありますから、とても べんりです。",
        "acceptable": [
            "秋葉原は電器屋がたくさんありますから、とても便利です。",
            "秋葉原は電気屋がたくさんありますから、とても便利です。",
            "秋葉原には電気屋がたくさんあるので、とても便利です。",
            "あきはばらはでんきやがたくさんありますから、とてもべんりです。",
            "秋葉原は電気屋が多いですから、とても便利です。",
            "秋葉原は電気の店がたくさんあって、とても便利です。"
        ],
        "keywords": ["秋葉原", "電器屋", "たくさん", "ありますから", "便利"],
        "keywordsHira": ["あきはばら", "でんきや", "たくさん", "ありますから", "べんり"]
    },
    {
        "id": 3,
        "type": "single",
        "vi": "Ở khu vực này có nhiều cửa hàng thời trang dễ thương.",
        "topic": "Topic 4: Mua sắm & Quà tặng (Bài 7-8)",
        "grammarPoint": "Địa điểm + に (tồn tại). Khu vực này: このエリア / このへん / このあたり. Cửa hàng thời trang: ファッションの店 / 服の店.",
        "modelJa": "この エリアに かわいい ファッションの 店が たくさん あります。",
        "modelHiragana": "この えりあに かわいい ふぁっしょんの みせが たくさん あります。",
        "acceptable": [
            "このエリアにかわいいファッションの店がたくさんあります。",
            "このへんにかわいいファッションの店がたくさんあります。",
            "このあたりにかわいい服の店がたくさんあります。",
            "このエリアにはかわいい服屋がたくさんあります。",
            "この場所に可愛いファッションの店がたくさんあります。"
        ],
        "keywords": ["この", "かわいい", "ファッション", "店", "たくさん", "あります"],
        "keywordsHira": ["この", "かわいい", "ふぁっしょん", "みせ", "たくさん", "あります"]
    },
    {
        "id": 4,
        "type": "single",
        "vi": "Siêu thị ở gần nhà ga.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Vị trí gần: ～の 近く (ちかく) hoặc ～の そば. [Chủ ngữ] は [Địa điểm] の 近くに あります.",
        "modelJa": "スーパーは 駅の 近くに あります。",
        "modelHiragana": "すーぱーは えきの ちかくに あります。",
        "acceptable": [
            "スーパーは駅の近くにあります。",
            "スーパーは駅の近くです。",
            "駅の近くにスーパーがあります。",
            "スーパーは駅のそばにあります。",
            "すーぱーはえきのちかくにあります。"
        ],
        "keywords": ["スーパー", "駅", "近く", "あります"],
        "keywordsHira": ["すーぱー", "えき", "ちかく", "あります"]
    },
    {
        "id": 5,
        "type": "single",
        "vi": "Bạn có nhìn thấy cây cầu màu đỏ ở đằng kia không?",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Động từ tự nhiên nhìn thấy: 見えます (みえます). Cây cầu màu đỏ: 赤い 橋 (あかい はし).",
        "modelJa": "あそこに 赤い 橋が 見えますか。",
        "modelHiragana": "あそこに あかい はしが みえますか。",
        "acceptable": [
            "あそこに赤い橋が見えますか。",
            "あそこの赤い橋が見えますか。",
            "あそこに赤い橋が見えますか？",
            "あそこにあかいはしがみえますか。",
            "あそこに赤い橋がありますか。"
        ],
        "keywords": ["あそこ", "赤い", "橋", "見えますか"],
        "keywordsHira": ["あそこ", "あかい", "はし", "みえますか"]
    },
    {
        "id": 6,
        "type": "dialogue",
        "vi": "A: Tôi muốn đi đến viện bảo tàng Asahi, đi như thế nào ?\nB: Đi thẳng con đường này. Sau đó, hãy rẽ phải ở góc đường thứ nhất. Bảo tàng ở bên tay trái.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Hỏi đường: ～へ 行きたいんですが、どうやって 行けば いいですか. Chỉ đường: まっすぐ 行って ください (đi thẳng), ～つ目の 角を 右へ 曲がって ください (rẽ phải ở góc thứ...), 左側に あります (ở bên trái).",
        "modelA": "朝日美術館へ 行きたいんですが、どうやって 行けば いいですか。",
        "modelB": "この 道を まっすぐ 行って ください。それから、1つ目の 角を 右へ まがって ください。美術館は 左側に あります。",
        "modelHiraganaA": "あさひびじゅつかんへ いきたいんですが、どうやって いけば いいですか。",
        "modelHiraganaB": "この みちを まっすぐ いって ください。それから、ひとつめの かどを みぎへ まがって ください。びじゅつかんは ひだりがわに あります。",
        "keywordsA": ["美術館", "行きたい", "どうやって"],
        "keywordsB": ["まっすぐ", "1つ目", "角", "右", "まがって", "左側", "あります"]
    },
    {
        "id": 7,
        "type": "dialogue",
        "vi": "A: Ngày mai mấy giờ gặp nhau thế?\nB: 9h sáng tại cổng tây ga Shinjuku nhé.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Hẹn giờ: 何時に 会いますか (なんじにあいますか). Cổng tây: 西口 (にしぐち).",
        "modelA": "あした 何時に 会いますか。",
        "modelB": "午前9時に 新宿駅の 西口で 会いましょう（西口ね）。",
        "modelHiraganaA": "あした なんじに あいますか。",
        "modelHiraganaB": "ごぜんくじに しんじゅくえきの にしぐちで あいましょう。",
        "keywordsA": ["あした", "何時", "会いますか"],
        "keywordsB": ["9時", "新宿駅", "西口"]
    },
    {
        "id": 8,
        "type": "single",
        "vi": "Bạn có nhìn thấy tòa nhà hình tròn, thú vị ở đằng kia không?",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Nối tính từ: 丸い ➔ 丸くて (hình tròn), 面白い (thú vị). Tòa nhà: 建物 (たてもの) hoặc ビル. Động từ nhìn thấy: 見えますか.",
        "modelJa": "あそこに 丸くて、面白い 建物が 見えますか。",
        "modelHiragana": "あそこに まるくて、おもしろい たてものが みえますか。",
        "acceptable": [
            "あそこに丸くて、面白い建物が見えますか。",
            "あそこに丸くて面白い建物が見えますか。",
            "あそこにまるくて、おもしろいたてものがみえますか。",
            "あそこに丸くて面白いビルが見えますか。",
            "あそこの丸くて面白い建物が見えますか。"
        ],
        "keywords": ["あそこ", "丸くて", "面白い", "建物", "見えますか"],
        "keywordsHira": ["あそこ", "まるくて", "おもしろい", "たてもの", "みえますか"]
    },
    {
        "id": 9,
        "type": "single",
        "vi": "Ở cạnh nhà tôi có tòa nhà màu xanh, thon dài.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Bên cạnh: となり (隣) / 横 (よこ). Thon dài: 細長い (ほそながい). Màu xanh: 青い ➔ 青くて (xanh da trời) hoặc 緑で (xanh lá).",
        "modelJa": "わたしの 家の となりに、青くて 細長い 建物が あります。",
        "modelHiragana": "わたしの いえの となりに、あおくて ほそながい たてものが あります。",
        "acceptable": [
            "わたしの家のとなりに、青くて細長い建物があります。",
            "うちのとなりに青くて細長いビルがあります。",
            "わたしのいえのとなりに、あおくてほそながいたてものがあります。",
            "家の隣に青くて細長い建物があります。",
            "私の家のとなりに緑で細長い建物があります。"
        ],
        "keywords": ["家", "となり", "青くて", "細長い", "建物", "あります"],
        "keywordsHira": ["いえ", "となり", "あおくて", "ほそながい", "たてもの", "あります"]
    },
    {
        "id": 10,
        "type": "dialogue",
        "vi": "A: Abe san, mình xin lỗi vì đến muộn nhé. Mình bị nhầm thời gian cuộc hẹn…\nB: Không sao đâu. Mình cũng hay bị nhầm lắm. Thế chúng ta đi thôi nhỉ.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Xin lỗi vì đến muộn: 遅れて すみません (おくれてすみません). Nhầm thời gian hẹn: 約束の 時間を 間違えました (まちがえました). Không sao: 大丈夫ですよ (だいじょうぶですよ).",
        "modelA": "安部さん、遅れて すみません。約束の 時間を 間違えました…",
        "modelB": "大丈夫ですよ。わたしも よく 間違えますから。じゃあ、行きましょうか。",
        "modelHiraganaA": "あべさん、おくれて すみません。やくそくの じかんを まちがえました…",
        "modelHiraganaB": "だいじょうぶですよ。わたしも よく まちがえますから。じゃあ、いきましょうか。",
        "keywordsA": ["遅れて", "すみません", "約束", "時間", "間違え"],
        "keywordsB": ["大丈夫", "よく", "行きましょう"]
    },
    {
        "id": 11,
        "type": "dialogue",
        "vi": "A: Tôi muốn giỏi tiếng nhật thì phải học như thế nào?\nB: Hãy thường xuyên nói tiếng nhật. Và nhớ nhiều từ vựng và ngữ pháp.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Muốn trở nên giỏi: 上手に なりたい (じょうずになりたい). Khuyên nhủ lịch sự: ～て ください. Nhớ: 覚えて (おぼえて). Từ vựng: 言葉 / 単語. Ngữ pháp: 文法 (ぶんぽう).",
        "modelA": "日本語が 上手に なりたいんですが、どうやって 勉強すれば いいですか。",
        "modelB": "いつも 日本語を 話して ください。そして、言葉と 文法を たくさん 覚えて ください。",
        "modelHiraganaA": "にほんごが じょうずに なりたいんですが、どうやって べんきょうすれば いいですか。",
        "modelHiraganaB": "いつも にほんごを はなして ください。そして、ことばと ぶんぽうを たくさん おぼえて ください。",
        "keywordsA": ["日本語", "上手", "なりたい", "勉強"],
        "keywordsB": ["話して", "言葉", "文法", "覚えて"]
    },
    {
        "id": 12,
        "type": "dialogue",
        "vi": "A: Cho đến bây giờ bạn đã học ngoại ngữ nào rồi?\nB: Tôi đã học tiếng Anh, tiếng Trung và tiếng Ý.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Cho đến bây giờ: 今まで (いままで). Ngoại ngữ: 外国語 (がいこくご). Liệt kê: と... と...",
        "modelA": "今まで どんな 外国語を 勉強しましたか（習いましたか）。",
        "modelB": "英語と 中国語と イタリア語を 勉強しました（習いました）。",
        "modelHiraganaA": "いままで どんな がいこくごを べんきょうしましたか。",
        "modelHiraganaB": "えいごと ちゅうごくごと イタリアごを べんきょうしました。",
        "keywordsA": ["今まで", "外国語", "勉強しました"],
        "keywordsB": ["英語", "中国語", "イタリア語"]
    },
    {
        "id": 13,
        "type": "single",
        "vi": "Trước khi xem phim, tôi muốn đi quán cà phê mua nước.",
        "topic": "Topic 2: Thói quen sinh hoạt (Bài 3-4)",
        "grammarPoint": "Mẫu câu V-ru + まえに (Trước khi làm V): 映画を 見る まえに. Đi đâu làm gì: カフェへ 行って 飲み物を 買いたいです.",
        "modelJa": "映画を 見る まえに、カフェへ 行って 飲み物を 買いたいです。",
        "modelHiragana": "えいがを みる まえに、かふぇへ いって のみものを かいたいです。",
        "acceptable": [
            "映画を見るまえに、カフェへ行って飲み物を買いたいです。",
            "映画を見る前に、カフェに行って飲み物を買いたいです。",
            "えいがをみるまえに、カフェへいってのみものをかいたいです。",
            "映画を見る前に、喫茶店へ行って飲み物を買いたいです。",
            "映画を見るまえに、カフェで水を買いたいです。"
        ],
        "keywords": ["映画", "見る", "まえに", "カフェ", "飲み物", "買いたい"],
        "keywordsHira": ["えいが", "みる", "まえに", "かふぇ", "のみもの", "かいたい"]
    },
    {
        "id": 14,
        "type": "dialogue",
        "vi": "A: Xin lỗi, có thể cho tôi mượn quyển từ điển đó được không?\nB: Được chứ, bạn hãy dùng đi.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Nhờ vả / xin phép: ～て もらえませんか (貸して もらえませんか) hoặc ～ても いいですか (借りても いいですか). Mời dùng: どうぞ 使って ください.",
        "modelA": "すみません、その 辞書を 貸して もらえませんか（借りても いいですか）。",
        "modelB": "いいですよ、どうぞ 使って ください。",
        "modelHiraganaA": "すみません、その じしょを かして もらえませんか。",
        "modelHiraganaB": "いいですよ、どうぞ つかって ください。",
        "keywordsA": ["辞書", "貸して", "借りて"],
        "keywordsB": ["いいですよ", "どうぞ", "使って"]
    },
    {
        "id": 15,
        "type": "dialogue",
        "vi": "A: Việc học tiếng Trung thế nào?\nB: Khó nhưng chữ tiếng Trung thú vị. Vì khác với tiếng Anh.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Khó nhưng thú vị: 難しいですが、面白いです. Khác với: ～と 違います (ちがいます).",
        "modelA": "中国語の 勉強は どうですか。",
        "modelB": "難しいですが、中国語の 漢字（文字）は 面白いです。英語と 違いますから。",
        "modelHiraganaA": "ちゅうごくごの べんきょうは どうですか。",
        "modelHiraganaB": "むずかしいですが、ちゅうごくごの かんじは おもしろいです。えいごと ちがいますから。",
        "keywordsA": ["中国語", "勉強", "どうですか"],
        "keywordsB": ["難しい", "漢字", "面白い", "英語", "違い"]
    },
    {
        "id": 16,
        "type": "dialogue",
        "vi": "A: Chị gái bạn đang sống ở đâu?\nB: Chị tôi đang sống ở Bắc Kinh Trung Quốc. Bây giờ, chị ấy đang làm việc tại công ty trò chơi.",
        "topic": "Topic 1: Gia đình (Bài 1-2)",
        "grammarPoint": "Đang sống ở đâu: [Địa điểm] に 住んで います (すんでいます). Đang làm việc: [Công ty] で 働いて います (はたらいています).",
        "modelA": "お姉さんは どこに 住んで いますか。",
        "modelB": "姉は 中国の 北京に 住んで います。今、ゲームの 会社で 働いて います。",
        "modelHiraganaA": "おねえさんは どこに すんで いますか。",
        "modelHiraganaB": "あねは ちゅうごくの ぺきんに すんで います。いま、げーむの かいしゃで はたらいて います。",
        "keywordsA": ["お姉さん", "どこ", "住んで"],
        "keywordsB": ["中国", "北京", "住んで", "ゲーム", "会社", "働いて"]
    },
    {
        "id": 17,
        "type": "single",
        "vi": "Ngày mai chúng ta hẹn gặp nhau vào lúc 10h tại sảnh khách sạn nhé.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Sảnh khách sạn: ホテルの ロビー. Hẹn gặp nhau: 待ち合わせましょう (まちあわせましょう) hoặc 会いましょう.",
        "modelJa": "あした 10時に ホテルの ロビーで 待ち合わせましょう（会いましょう）。",
        "modelHiragana": "あした じゅうじに ほてるの ろびーで まちあわせましょう。",
        "acceptable": [
            "あした10時にホテルのロビーで待ち合わせましょう。",
            "明日10時にホテルのロビーで会いましょう。",
            "あした10じにホテルのロビーでまちあわせましょう。",
            "あした10時にホテルのロビーで会いましょうね。",
            "あした午前10時にホテルのロビーで会いましょう。"
        ],
        "keywords": ["あした", "10時", "ホテル", "ロビー", "待ち合わせ", "会いましょう"],
        "keywordsHira": ["あした", "じゅうじ", "ほてる", "ろびー", "まちあわせ", "あいましょう"]
    },
    {
        "id": 18,
        "type": "dialogue",
        "vi": "A: Xin lỗi, bạn có thể chỉ cho tôi cách sử dụng kim từ điển này không?\nB: Kim từ điển à? ừ...m tôi cũng không biết rõ lắm. Xin lỗi nhé.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Kim từ điển (từ điển điện tử): 電子辞書 (でんしじしょ). Cách dùng: 使い方 (つかいかた). Không biết rõ: よく 分かりません / 知りません.",
        "modelA": "すみません、この 電子辞書の 使い方を 教えて もらえませんか（ください）。",
        "modelB": "電子辞書ですか。うーん、わたしも よく 分かりません。すみませんね。",
        "modelHiraganaA": "すみません、この でんしじしょの つかいかたを おしえて もらえませんか。",
        "modelHiraganaB": "でんしじしょですか。うーん、わたしも よく わかりません。すみませんね。",
        "keywordsA": ["電子辞書", "使い方", "教えて"],
        "keywordsB": ["電子辞書", "よく", "分かりません", "知りません"]
    },
    {
        "id": 19,
        "type": "dialogue",
        "vi": "A: Dịp sinh nhật năm ngoái, bạn đã nhận được gì thế?\nB: Tôi đã nhận được chiếc áo phông rất dễ thương ạ.",
        "topic": "Topic 4: Mua sắm & Quà tặng (Bài 7-8)",
        "grammarPoint": "Năm ngoái: 去年 (きょねん). Sinh nhật: 誕生日 (たんじょうび). Nhận được: もらいました. Áo phông: Tシャツ.",
        "modelA": "去年の 誕生日に 何を もらいましたか。",
        "modelB": "とても かわいい Tシャツを もらいました。",
        "modelHiraganaA": "きょねんの たんじょうびに なにを もらいましたか。",
        "modelHiraganaB": "とても かわいい てぃーしゃつを もらいました。",
        "keywordsA": ["去年", "誕生日", "何", "もらいましたか"],
        "keywordsB": ["かわいい", "Tシャツ", "もらいました"]
    },
    {
        "id": 20,
        "type": "dialogue",
        "vi": "A: Ôi, đồng hồ đẹp quá. Bạn nhận được từ ai vậy?\nB: À, cái này tôi đã mua ở Osaka đấy.",
        "topic": "Topic 4: Mua sắm & Quà tặng (Bài 7-8)",
        "grammarPoint": "Đồng hồ: 時計 (とけい). Đẹp/tuyệt vời: すてきな / きれいな. Nhận từ ai: だれに（だれから） もらいましたか.",
        "modelA": "わあ、すてきな（きれいな） 時計ですね。だれに もらいましたか。",
        "modelB": "あ、これは 大阪で 買いましたよ。",
        "modelHiraganaA": "わあ、すてきな とけいですね。だれに もらいましたか。",
        "modelHiraganaB": "あ、これは おおさかで かいましたよ。",
        "keywordsA": ["時計", "すてき", "きれい", "だれ", "もらいました"],
        "keywordsB": ["大阪", "買いました"]
    },
    {
        "id": 21,
        "type": "dialogue",
        "vi": "A: Cậu muốn có gì?\nB: Tớ muốn có chiếc áo sơ mi trắng.",
        "topic": "Topic 4: Mua sắm & Quà tặng (Bài 7-8)",
        "grammarPoint": "Muốn có đồ vật gì: [Đồ vật] が ほしいです. Áo sơ mi trắng: 白い シャツ (しろい シャツ).",
        "modelA": "何が ほしいですか。",
        "modelB": "白い シャツが ほしいです。",
        "modelHiraganaA": "なにが ほしいですか。",
        "modelHiraganaB": "しろい しゃつが ほしいです。",
        "keywordsA": ["何", "ほしい"],
        "keywordsB": ["白い", "シャツ", "ほしい"]
    },
    {
        "id": 22,
        "type": "dialogue",
        "vi": "A: Cậu muốn uống gì?\nB: Tớ muốn uống café lạnh.",
        "topic": "Topic 5: Ẩm thực & Nhà hàng (Bài 9-10)",
        "grammarPoint": "Muốn uống: 飲みたい (のみたい). Cà phê lạnh: 冷たい コーヒー (つめたい コーヒー) hoặc アイスコーヒー.",
        "modelA": "何を 飲みたいですか。",
        "modelB": "冷たい コーヒー（アイスコーヒー）を 飲みたいです。",
        "modelHiraganaA": "なにを のみたいですか。",
        "modelHiraganaB": "つめたい こーひーを のみたいです。",
        "keywordsA": ["何", "飲みたい"],
        "keywordsB": ["冷たい", "アイスコーヒー", "コーヒー", "飲みたい"]
    },
    {
        "id": 23,
        "type": "dialogue",
        "vi": "A: Mẹ bạn là người như thế nào ?\nB: Là người rất dễ thương và tốt bụng.",
        "topic": "Topic 1: Gia đình (Bài 1-2)",
        "grammarPoint": "Mẹ của bạn: お母さん (おかあさん). Người như thế nào: どんな 人 (どんなひと). Tốt bụng: 親切 (しんせつ) hoặc 優しい (やさしい).",
        "modelA": "お母さんは どんな 人ですか。",
        "modelB": "とても かわいくて、親切な（優しい） 人です。",
        "modelHiraganaA": "おかあさんは どんな ひとですか。",
        "modelHiraganaB": "とても かわいくて、しんせつな（やさしい） ひとです。",
        "keywordsA": ["お母さん", "どんな", "人"],
        "keywordsB": ["かわいくて", "親切", "優しい", "人"]
    },
    {
        "id": 24,
        "type": "dialogue",
        "vi": "A: Trong 1 năm, bạn thích mùa nào nhất?\nB: Tôi thích mùa hè nhất, vì tôi thích kem. Và tôi sợ lạnh ><”",
        "topic": "Topic 5: Thời tiết & Bốn mùa (Bài 9-10)",
        "grammarPoint": "So sánh nhất trong phạm vi: 1年で いつ / どの季節が 一番 好きですか. Mùa hè: 夏 (なつ). Sợ lạnh / kém chịu lạnh: 寒さに 弱いです / 寒がりです / 寒いのが 苦手です.",
        "modelA": "1年で いつ（どの 季節が） 一番 好きですか。",
        "modelB": "夏が 一番 好きです。アイスクリームが 好きですから。それに、寒さに 弱いですから（寒がりですから）。",
        "modelHiraganaA": "いちねんで いつ いちばん すきですか。",
        "modelHiraganaB": "なつが いちばん すきです。あいすくりーむが すきですから。さむがりですから。",
        "keywordsA": ["1年", "季節", "一番", "好き"],
        "keywordsB": ["夏", "一番", "好き", "アイス", "寒"]
    },
    {
        "id": 25,
        "type": "dialogue",
        "vi": "A: Kyoto là 1 thành phố như nào ạ?\nB: Kyoto là thành phố rất đẹp và có nhiều ngôi chùa cổ.",
        "topic": "Topic 3: Nơi chốn & Thành phố (Bài 5)",
        "grammarPoint": "Thành phố như thế nào: どんな 町 (どんなまち). Ngôi chùa cổ: 古い お寺 (ふるい おてら).",
        "modelA": "京都は どんな 町ですか。",
        "modelB": "京都は とても きれいで、古い お寺が たくさん ある 町です。",
        "modelHiraganaA": "きょうとは どんな まちですか。",
        "modelHiraganaB": "きょうとは とても きれいで、ふるい おてらが たくさん ある まちです。",
        "keywordsA": ["京都", "どんな", "町"],
        "keywordsB": ["きれいで", "古い", "お寺", "たくさん", "町"]
    },
    {
        "id": 26,
        "type": "dialogue",
        "vi": "A: Anh đã đến Việt Nam chưa ạ?\nB: Anh chưa. Năm sau, anh rất muốn đi thử.",
        "topic": "Topic 5: Du lịch & Trải nghiệm (Bài 9-10)",
        "grammarPoint": "Đã từng đi: 行ったことが ありますか. Chưa: まだです. Đi thử: 行ってみたい (いってみたい). Năm sau: 来年 (らいねん).",
        "modelA": "ベトナムへ 行ったことが ありますか（もう ベトナムへ 行きましたか）。",
        "modelB": "いいえ、まだです。来年、ぜひ 行ってみたいです。",
        "modelHiraganaA": "べとなむへ いったことが ありますか。",
        "modelHiraganaB": "いいえ、まだです。らいねん、ぜひ いってみたいです。",
        "keywordsA": ["ベトナム", "行った", "ありますか"],
        "keywordsB": ["まだ", "来年", "行ってみたい"]
    },
    {
        "id": 27,
        "type": "dialogue",
        "vi": "A: Mai bạn ngắm tháp Tokyo với tôi không? Cảnh đêm đẹp lắm đó.\nB: Tất nhiên rồi, cùng đi thôi.",
        "topic": "Topic 3: Nơi chốn (Bài 5)",
        "grammarPoint": "Rủ rê: ～ませんか (見ませんか). Cảnh đêm: 夜景 (やけい). Tất nhiên: もちろんです. Cùng đi: 一緒に 行きましょう (いっしょに いきましょう).",
        "modelA": "あした わたしと 東京タワーを 見ませんか。夜景が とても きれいですよ。",
        "modelB": "もちろんです、一緒に 行きましょう。",
        "modelHiraganaA": "あした わたしと とうきょうたわーを みませんか。やけいが とても きれいですよ。",
        "modelHiraganaB": "もちろんです、いっしょに いきましょう。",
        "keywordsA": ["あした", "東京タワー", "見ませんか", "夜景", "きれい"],
        "keywordsB": ["もちろん", "一緒", "行きましょう"]
    },
    {
        "id": 28,
        "type": "single",
        "vi": "Tokyo thì đông người hơn Okinawa.",
        "topic": "Topic 5: So sánh (Bài 9-10)",
        "grammarPoint": "Mẫu so sánh hơn: [A] の ほうが [B] より [Tính từ] です (東京の ほうが 沖縄より 人が 多いです).",
        "modelJa": "東京の ほうが 沖縄より 人が 多いです。",
        "modelHiragana": "とうきょうの ほうが おきなわより ひとが おおいです。",
        "acceptable": [
            "東京のほうが沖縄より人が多いです。",
            "東京は沖縄より人が多いです。",
            "沖縄より東京のほうが人が多いです。",
            "とうきょうのほうがおきなわよりひとがおおいです。",
            "東京は沖縄より人がたくさんいます。"
        ],
        "keywords": ["東京", "沖縄", "より", "ほう", "人", "多い"],
        "keywordsHira": ["とうきょう", "おきなわ", "より", "ほう", "ひと", "おおい"]
    },
    {
        "id": 29,
        "type": "single",
        "vi": "Ở Nhật Bản, ở đâu là lạnh nhất? …Hokkaidou thì lạnh nhất Nhật Bản đấy.",
        "topic": "Topic 5: So sánh nhất (Bài 9-10)",
        "grammarPoint": "So sánh nhất: [Phạm vi] で どこが 一番 [Tính từ] ですか (日本で どこが 一番 寒いですか).",
        "modelJa": "日本で どこが 一番 寒いですか。…北海道が 日本で 一番 寒いですよ。",
        "modelHiragana": "にほんで どこが いちばん さむいですか。ほっかいどうが にほんで いちばん さむいですよ。",
        "acceptable": [
            "日本でどこが一番寒いですか。北海道が日本で一番寒いですよ。",
            "日本でどこが一番寒いですか。…北海道が一番寒いです。",
            "にほんでどこがいちばんさむいですか。ほっかいどうがいちばんさむいですよ。"
        ],
        "keywords": ["日本", "どこ", "一番", "寒い", "北海道"],
        "keywordsHira": ["にほん", "どこ", "いちばん", "さむい", "ほっかいどう"]
    },
    {
        "id": 30,
        "type": "single",
        "vi": "Giữa Pokemon và Doraemon, bạn thích cái nào hơn?\nMình thích Doraemon hơn. Vì Doremon có túi thần kỳ. ※ふしぎ（な）／ポケット",
        "topic": "Topic 5: So sánh (Bài 9-10)",
        "grammarPoint": "So sánh 2 đối tượng: [A] と [B] と、どちらが（どっちが） 好きですか. Túi thần kỳ: 不思議な ポケット (ふしぎなぽけっと).",
        "modelJa": "ポケモンと ドラえもんと、どちらが 好きですか。ドラえもんの ほうが 好きです。不思議な ポケットが ありますから。",
        "modelHiragana": "ぽけもんと どらえもんと、どちらが すきですか。どらえもんの ほうが すきです。ふしぎな ぽけっとが ありますから。",
        "acceptable": [
            "ポケモンとドラえもんと、どちらが好きですか。ドラえもんのほうが好きです。不思議なポケットがありますから。",
            "ポケモンとドラえもんと、どっちが好きですか。ドラえもんのほうが好きです。ふしぎなポケットがあるからです。",
            "ポケモンとドラえもん、どちらが好きですか。ドラえもんのほうが好きです。ドラえもんは不思議なポケットがありますから。"
        ],
        "keywords": ["ポケモン", "ドラえもん", "どちら", "好き", "ほう", "不思議", "ポケット"],
        "keywordsHira": ["ぽけもん", "どらえもん", "どちら", "すき", "ほう", "ふしぎ", "ぽけっと"]
    },
    {
        "id": 31,
        "type": "single",
        "vi": "Bạn có thể chỉ cho tôi cách làm món ăn Việt Nam không?",
        "topic": "Topic 5: Ẩm thực (Bài 9-10)",
        "grammarPoint": "Cách làm: 作り方 (つくりかた). Nhờ vả lịch sự: 教えて もらえませんか (おしえてもらえませんか) hoặc 教えて ください.",
        "modelJa": "ベトナム料理の 作り方を 教えて もらえませんか（教えて ください）。",
        "modelHiragana": "べとなむりょうりの つくりかたを おしえて もらえませんか。",
        "acceptable": [
            "ベトナム料理の作り方を教えてもらえませんか。",
            "ベトナム料理の作り方を教えてください。",
            "ベトナムの料理の作り方を教えてもらえませんか。",
            "べとなむりょうりのつくりかたをおしえてもらえませんか。",
            "ベトナム料理の作り方を教えてくれますか。"
        ],
        "keywords": ["ベトナム料理", "作り方", "教えて", "もらえませんか"],
        "keywordsHira": ["べとなむりょうり", "つくりかた", "おしえて", "もらえませんか"]
    },
    {
        "id": 32,
        "type": "paragraph",
        "vi": "Thành phố của tôi thì có nhiều người nước ngoài. Trong thành phố, có trung tâm văn hóa Nhật Bản. Tôi đang học tiếng Nhật 1 tuần 3 lần ở trung tâm. Và tôi thích món ăn Nhật Bản, nên tôi đến nhà hàng ăn 1 tháng 5 lần. Một ngày nào đó, tôi muốn đi du học ở Nhật Bản.",
        "topic": "Topic 1-5: Đoạn văn tổng hợp",
        "grammarPoint": "Tần suất: 1週間に 3回 (いっしゅうかんに さんかい), 1か月に 5回 (いっかげつに ごかい). Đi làm gì: 食べに 行きます. Đi du học: 留学したい (りゅうがくしたい).",
        "modelJa": "わたしの 町には 外国人が たくさん います。町の中に 日本文化センターが あります。わたしは センターで 1週間に 3回 日本語を 勉強して います。そして、日本料理が 好きですから、1か月に 5回 レストランへ 食べに 行きます。いつか、日本へ 留学したいです。",
        "modelHiragana": "わたしの まちには がいこくじんが たくさん います。まちの なかに にほんぶんかせんたーが あります。わたしは せんたーで いっしゅうかんに さんかい にほんごを べんきょうして います。そして、にほんりょうりが すきですから、いっかげつに ごかい れすとらんへ たべに いきます。いつか、にほんへ りゅうがくしたいです。",
        "acceptable": [
            "わたしの町には外国人がたくさんいます。町の中に日本文化センターがあります。わたしはセンターで1週間に3回日本語を勉強しています。そして、日本料理が好きですから、1か月に5回レストランへ食べに行きます。いつか、日本へ留学したいです。"
        ],
        "keywords": ["町", "外国人", "たくさん", "日本文化センター", "1週間", "3回", "勉強", "日本料理", "1か月", "5回", "食べに", "留学"],
        "keywordsHira": ["まち", "がいこくじん", "たくさん", "にほんぶんかせんたー", "いっしゅうかん", "さんかい", "べんきょう", "にほんりょうり", "いっかげつ", "ごかい", "たべに", "りゅうがく"]
    },
    {
        "id": 33,
        "type": "paragraph",
        "vi": "Hà Nội thì khoảng tháng 9 sẽ chuyển sang mùa thu. Mùa thu của Hà Nội thì đẹp và yên bình. Tôi thường đến phố cổ để chụp ảnh. Khoảng tháng 12, trời trở lạnh nên  tôi không hay ra ngoài lắm ☹ Buổi đêm, đường phố cũng trở nên yên tĩnh hơn.",
        "topic": "Topic 5: Khí hậu & Bốn mùa (Bài 9-10)",
        "grammarPoint": "Chuyển sang mùa thu: 秋に なります (あきになります). Trở lạnh: 寒く なります (さむくなります). Yên tĩnh hơn: もっと 静かに なります. Không hay ra ngoài lắm: あまり 外へ 出かけません.",
        "modelJa": "ハノイは 9月ごろ 秋に なります。ハノイの 秋は きれいで、平和です（静かです）。わたしは よく 旧市街（古い町）へ 写真を 撮りに 行きます。12月ごろ、寒くなりますから、あまり 外へ 出かけません。夜は、通りも もっと 静かに なります。",
        "modelHiragana": "はのいは くがつごろ あきに なります。はのいの あきは きれいで、へいわです。わたしは よく きゅうしがいへ しゃしんを とりに いきます。じゅうにがつごろ、さむくなりますから、あまり そとへ でかけません。よるは、とおりも もっと しずかに なります。",
        "acceptable": [
            "ハノイは9月ごろ秋になります。ハノイの秋はきれいで、静かです。わたしはよく古い町へ写真を撮りに行きます。12月ごろ、寒くなりますから、あまり外へ出かけません。夜は、道ももっと静かになります。"
        ],
        "keywords": ["ハノイ", "9月", "秋", "なります", "きれい", "写真", "撮りに", "12月", "寒く", "あまり", "出かけません", "夜", "静か"],
        "keywordsHira": ["はのい", "くがつ", "あき", "なります", "きれい", "しゃしん", "とりに", "じゅうにがつ", "さむく", "あまり", "でかけません", "よる", "しずか"]
    },
    {
        "id": 34,
        "type": "single",
        "vi": "Vì lạc đường, nên tôi đã không thể làm được bài kiểm tra tiếng Nhật.",
        "topic": "Topic 3: Nơi chốn & Chỉ đường (Bài 5)",
        "grammarPoint": "Lạc đường: 道に 迷いました (みちに まよいました). Không thể làm bài kiểm tra: 日本語の テストが できませんでした (hoặc 受けられませんでした).",
        "modelJa": "道に 迷いましたから、日本語の テストが できませんでした。",
        "modelHiragana": "みちに まよいましたから、にほんごの てすとが できませんでした。",
        "acceptable": [
            "道に迷いましたから、日本語のテストができませんでした。",
            "道に迷ったので、日本語のテストができませんでした。",
            "道に迷って、日本語のテストができませんでした。",
            "みちにまよいましたから、にほんごのてすとができませんでした。",
            "道に迷いましたから、日本語の試験を受けられませんでした。"
        ],
        "keywords": ["道に", "迷い", "日本語", "テスト", "できませんでした"],
        "keywordsHira": ["みちに", "まよい", "にほんご", "てすと", "できませんでした"]
    },
    {
        "id": 35,
        "type": "single",
        "vi": "Vì bão, nên tàu điện và xe bus dừng chạy.",
        "topic": "Topic 5: Thời tiết (Bài 9-10)",
        "grammarPoint": "Chỉ nguyên nhân thiên tai: [Danh từ] で (台風で). Dừng chạy: 止まりました (とまりました).",
        "modelJa": "台風で、電車と バスが 止まりました。",
        "modelHiragana": "たいふうで、でんしゃと ばすが とまりました。",
        "acceptable": [
            "台風で、電車とバスが止まりました。",
            "台風ですから、電車とバスが止まりました。",
            "台風なので、電車とバスが止まりました。",
            "たいふうで、でんしゃとばすがとまりました。",
            "台風で電車もバスも止まりました。"
        ],
        "keywords": ["台風", "電車", "バス", "止まりました"],
        "keywordsHira": ["たいふう", "でんしゃ", "ばす", "とまりました"]
    },
    {
        "id": 36,
        "type": "single",
        "vi": "Tiếng Pháp thì phát âm không đơn giản.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Phát âm: 発音 (はつおん). Đơn giản: 簡単 (かんたん). Phủ định tính từ đuôi な: 簡単では ありません / 簡単じゃ ありません.",
        "modelJa": "フランス語は 発音が 簡単では ありません（簡単じゃ ありません）。",
        "modelHiragana": "ふらんすごは はつおんが かんたんでは ありません。",
        "acceptable": [
            "フランス語は発音が簡単ではありません。",
            "フランス語は発音が簡単じゃありません。",
            "ふらんすごははつおんがかんたんではありません。",
            "フランス語の発音は簡単ではありません。",
            "フランス語は発音がシンプルではありません。"
        ],
        "keywords": ["フランス語", "発音", "簡単", "ありません"],
        "keywordsHira": ["ふらんすご", "はつおん", "かんたん", "ありません"]
    },
    {
        "id": 37,
        "type": "single",
        "vi": "Tiếng Việt thì việc nói chuyện khó.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Danh từ hóa động từ: V-ru + こと / の (話す こと / 話すの). Khó: 難しい (むずかしい).",
        "modelJa": "ベトナム語は 話す ことが 難しいです（話すのが 難しいです）。",
        "modelHiragana": "べとなむごは はなす ことが むずかしいです。",
        "acceptable": [
            "ベトナム語は話すことが難しいです。",
            "ベトナム語は話すのが難しいです。",
            "べとなむごははなすことがむずかしいです。",
            "ベトナム語は会話が難しいです。",
            "ベトナム語は話すことがむずかしいです。"
        ],
        "keywords": ["ベトナム語", "話す", "こと", "難しい"],
        "keywordsHira": ["べとなむご", "はなす", "こと", "むずかしい"]
    },
    {
        "id": 38,
        "type": "single",
        "vi": "Tiếng Nhật thì việc viết chữ Hán thú vị.",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Danh từ hóa động từ: 漢字を 書く こと (かんじを かく こと). Thú vị: 面白い (おもしろい).",
        "modelJa": "日本語は 漢字を 書く ことが 面白いです（書くのが 面白いです）。",
        "modelHiragana": "にほんごは かんじを かく ことが おもしろいです。",
        "acceptable": [
            "日本語は漢字を書くことが面白いです。",
            "日本語は漢字を書くのが面白いです。",
            "にほんごはかんじをかくことがおもしろいです。",
            "日本語は漢字を書くことがおもしろいです。"
        ],
        "keywords": ["日本語", "漢字", "書く", "こと", "面白い"],
        "keywordsHira": ["にほんご", "かんじ", "かく", "こと", "おもしろい"]
    },
    {
        "id": 39,
        "type": "paragraph",
        "vi": "Bây giờ, tôi đang học tiếng Nhật ở trường đại học. Tiếng Nhật thì từ vựng nhiều. Và tôi kém việc đọc câu văn tiếng Nhật : (",
        "topic": "Topic 2: Học ngoại ngữ (Bài 4)",
        "grammarPoint": "Đang học ở đại học: 大学で 勉強して います. Từ vựng nhiều: 単語（言葉）が 多いです. Kém việc đọc: 読む ことが 下手です / 苦手です.",
        "modelJa": "今、大学で 日本語を 勉強して います。日本語は 単語が 多いです。そして、日本語の 文を 読む ことが 下手です（苦手です）。",
        "modelHiragana": "いま、だいがくで にほんごを べんきょうして います。にほんごは たんごが おおいです。そして、にほんごの ぶんを よむ ことが へたです。",
        "acceptable": [
            "今、大学で日本語を勉強しています。日本語は単語が多いです。そして、日本語の文を読むことが下手です。",
            "今、大学で日本語を勉強しています。日本語は言葉が多いです。そして、日本語の文章を読むのが苦手です。",
            "いま、だいがくでにほんごをべんきょうしています。にほんごはことばがおおいです。そして、にほんごのぶんをよむことがへたです。"
        ],
        "keywords": ["今", "大学", "勉強して", "単語", "多い", "文", "読む", "こと", "下手", "苦手"],
        "keywordsHira": ["いま", "だいがく", "べんきょうして", "たんご", "おおい", "ぶん", "よむ", "こと", "へた", "にがて"]
    },
    {
        "id": 40,
        "type": "single",
        "vi": "Sở thích của tôi là đọc truyện tranh. Tôi đang sưu tầm nhiều truyện tranh của Nhật Bản.",
        "topic": "Topic 2: Sở thích (Bài 3)",
        "grammarPoint": "Sở thích là V: 趣味は ～ことです. Sưu tầm / thu thập: 集めて います (あつめています). Truyện tranh: マンガ.",
        "modelJa": "わたしの 趣味は マンガを 読む ことです。日本の マンガを たくさん 集めて います。",
        "modelHiragana": "わたしの しゅみは まんがを よむ ことです。にほんの まんがを たくさん あつめて います。",
        "acceptable": [
            "わたしの趣味はマンガを読むことです。日本のマンガをたくさん集めています。",
            "私の趣味は漫画を読むことです。日本の漫画をたくさん集めています。",
            "わたしのしゅみはまんがをよむことです。にほんのまんがをたくさんあつめています。"
        ],
        "keywords": ["趣味", "マンガ", "読む", "ことです", "日本", "たくさん", "集めて"],
        "keywordsHira": ["しゅみ", "まんが", "よむ", "ことです", "にほん", "たくさん", "あつめて"]
    }
]

print(f"Loaded {len(QUESTIONS_DATA)} comprehensive translation practice questions.")
