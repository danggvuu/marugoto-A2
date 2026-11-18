import json
import os
import re

WORKSPACE = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Import the base sections we defined for DEGOC
from generate_11_18_exam import degoc_sections

# Let's create a builder for the 5 additional exams (M111, M112, M113, M114, M115)
# Each exam will have exactly the same structure:
# Part 1: Kanji (10) + Vocab (12) = 22
# Part 2: Grammar (35)
# Part 3: Reading (8)
# Part 4: Star order (6)
# Total = 71 questions

def create_mock_exam(code, title, tag, desc, seed_offset):
    # We will curate 71 high quality questions per exam
    sections = []
    
    # KANJI POOL for Lessons 11-18:
    kanji_items_bank = [
        # (Kanji, Sentence, Correct, Options, Vi, Explain)
        ("計画", "来週の 旅行の <u>計画</u> を 立てました。", 0, ["けいかく", "けいかん", "かいかく", "けいがく"], 
         "Tôi đã lập kế hoạch cho chuyến du lịch tuần tới.", "計画 ➔ けいかく (Kế hoạch - Bài 18)."),
        ("案内", "友達に 京都の 町を <u>案内</u> しました。", 0, ["あんない", "あない", "あんうち", "あんめい"], 
         "Tôi đã hướng dẫn (dẫn đường) bạn bè tham quan thành phố Kyoto.", "案内 ➔ あんない (Hướng dẫn/dẫn đường - Bài 13)."),
        ("連絡", "遅れる ときは、必ず 会社に <u>連絡</u> して ください。", 0, ["れんらく", "れんろく", "れんがく", "ろんらく"], 
         "Khi đến muộn, nhất định hãy liên lạc cho công ty.", "連絡 ➔ れんらく (Liên lạc - Bài 18)."),
        ("準備", "パーティーの <u>準備</u> を 手伝って ください。", 0, ["じゅんび", "しゅんび", "じゅんひ", "じゅんぴ"], 
         "Hãy giúp tôi một tay chuẩn bị cho bữa tiệc.", "準備 ➔ じゅんび (Chuẩn bị - Bài 11/13)."),
        ("予約", "人気の レストランを <u>予約</u> しました。", 0, ["よやく", "あらかじめやく", "よてい", "ゆうやく"], 
         "Tôi đã đặt chỗ trước ở nhà hàng được yêu thích.", "予約 ➔ よやく (Đặt trước - Bài 11)."),
        ("経験", "日本で 働いた <u>経験</u> が あります。", 0, ["けいけん", "けいかん", "きょうけん", "けいげん"], 
         "Tôi đã có kinh nghiệm làm việc ở Nhật Bản.", "経験 ➔ けいけん (Kinh nghiệm - Bài 12/15)."),
        ("習慣", "毎朝 水を 一杯 飲む <u>習慣</u> が あります。", 0, ["しゅうかん", "じゅうかん", "しゅかん", "しゅうけん"], 
         "Tôi có thói quen uống một cốc nước mỗi buổi sáng.", "習慣 ➔ しゅうかん (Thói quen/tập quán - Bài 16)."),
        ("相談", "体調が 悪いときは、医者に <u>相談</u> します。", 0, ["そうだん", "しょうだん", "そだん", "そうだつ"], 
         "Khi sức khỏe không tốt, tôi sẽ tham vấn/hỏi ý kiến bác sĩ.", "相談 ➔ そうだん (Thảo luận/tham vấn - Bài 16)."),
        ("遠慮", "どうぞ <u>遠慮</u> しないで 食べて ください。", 0, ["えんりょ", "おんりょ", "えんろ", "えんりょう"], 
         "Xin mời cứ tự nhiên dùng bữa, đừng ngại ngùng nhé.", "遠慮 ➔ えんりょ (Khách khí/ngại ngùng - Bài 12)."),
        ("複雑", "この 機械の 使い方は とても <u>複雑</u> です。", 0, ["ふくざつ", "ふくさつ", "ふくぞう", "ぶくざつ"], 
         "Cách sử dụng chiếc máy móc này rất phức tạp.", "複雑 ➔ ふくざつ (Phức tạp - Bài 18)."),
        ("参加", "マラソン大会に <u>参加</u> したいです。", 0, ["さんか", "さんけい", "まいか", "さんしゃ"], 
         "Tôi muốn tham gia vào đại hội chạy marathon.", "参加 ➔ さんか (Tham gia - Bài 13/16)."),
        ("招待", "結婚式に <u>招待</u> されました。", 0, ["しょうたい", "じょうたい", "しょうだい", "せいたい"], 
         "Tôi đã được mời tham dự lễ kết hôn.", "招待 ➔ しょうたい (Chiêu đãi/mời - Bài 13)."),
        ("世話", "先生には 大変 お<u>世話</u> に なりました。", 0, ["せわ", "よわ", "せいふ", "せいわ"], 
         "Tôi đã được thầy cô giáo giúp đỡ chăm sóc rất nhiều.", "お世話 ➔ おせわ (Chăm sóc/giúp đỡ - Bài 14/18)."),
        ("残業", "今夜は 仕事が 多いので <u>残業</u> します。", 0, ["ざんぎょう", "さんぎょう", "ざんごう", "のこりぎょう"], 
         "Tối nay vì việc nhiều nên tôi sẽ làm thêm giờ.", "残業 ➔ ざんぎょう (Làm thêm giờ/OT - Bài 18)."),
        ("無理", "体に <u>無理</u> を しないで ください。", 0, ["むり", "ぶり", "むらい", "むりん"], 
         "Xin đừng quá sức / làm điều quá sức đối với cơ thể.", "無理 ➔ むり (Quá sức/vô lý - Bài 16).")
    ]
    
    # The five generated sets use only the curated L11-L18 study bank below.
    # Keep the source PDF exam separate; it is the original material.
    kanji_items_bank = [
        ("計画", "来週の 旅行の <u>計画</u> を 立てました。", 0, ["けいかく", "けいがく", "けいかん", "かいかく"], "Tôi đã lập kế hoạch cho chuyến du lịch tuần tới.", "計画（けいかく）: kế hoạch."),
        ("料理", "日本の <u>料理</u> が 好きです。", 0, ["りょうり", "りょり", "りょうい", "りょくり"], "Tôi thích món ăn Nhật.", "料理（りょうり）: món ăn, nấu ăn."),
        ("発音", "日本語の <u>発音</u> を 練習します。", 0, ["はつおん", "はっおん", "はついん", "はちおん"], "Tôi luyện phát âm tiếng Nhật.", "発音（はつおん）: phát âm."),
        ("結婚", "友達が <u>結婚</u> しました。", 0, ["けっこん", "けつこん", "けっこう", "けんこん"], "Bạn tôi đã kết hôn.", "結婚（けっこん）: kết hôn."),
        ("大切", "健康は <u>大切</u> です。", 0, ["たいせつ", "だいせつ", "たいきり", "おおせつ"], "Sức khỏe rất quan trọng.", "大切（たいせつ）: quan trọng, quý giá."),
        ("健康", "毎日 運動して、<u>健康</u> に なりました。", 0, ["けんこう", "けんごう", "げんこう", "けんこ"], "Tôi đã khỏe mạnh hơn nhờ tập thể dục mỗi ngày.", "健康（けんこう）: khỏe mạnh, sức khỏe."),
        ("自分", "これは <u>自分</u> で 作りました。", 0, ["じぶん", "しぶん", "じほん", "じもん"], "Tôi tự mình làm việc này.", "自分（じぶん）: bản thân, tự mình."),
        ("毎日", "<u>毎日</u> 日本語を 勉強します。", 0, ["まいにち", "まいひ", "まいじつ", "まいび"], "Tôi học tiếng Nhật mỗi ngày.", "毎日（まいにち）: mỗi ngày."),
        ("週末", "<u>週末</u> に 友達と 会います。", 0, ["しゅうまつ", "しゅまつ", "しゅうばつ", "しゅうげつ"], "Cuối tuần tôi gặp bạn.", "週末（しゅうまつ）: cuối tuần."),
        ("誕生日", "今日は 私の <u>誕生日</u> です。", 0, ["たんじょうび", "たんじょび", "たんせいび", "たんしょうひ"], "Hôm nay là sinh nhật tôi.", "誕生日（たんじょうび）: sinh nhật."),
        ("走ります", "毎朝 公園を <u>走ります</u>。", 0, ["はしります", "はじります", "そうります", "はします"], "Mỗi sáng tôi chạy trong công viên.", "走ります（はしります）: chạy."),
        ("着ます", "冬に コートを <u>着ます</u>。", 0, ["きます", "きります", "つきます", "ちゃくます"], "Mùa đông tôi mặc áo khoác.", "着ます（きます）: mặc."),
        ("電車", "<u>電車</u> で 会社へ 行きます。", 0, ["でんしゃ", "でんじゃ", "てんしゃ", "でんちゃ"], "Tôi đi tàu điện đến công ty.", "電車（でんしゃ）: tàu điện."),
        ("送ります", "母に 写真を <u>送ります</u>。", 0, ["おくります", "おぐります", "そうります", "おくれます"], "Tôi gửi ảnh cho mẹ.", "送ります（おくります）: gửi."),
        ("思います", "大切だと <u>思います</u>。", 0, ["おもいます", "おぼいます", "おもいします", "しもいます"], "Tôi nghĩ là quan trọng.", "思います（おもいます）: nghĩ."),
    ]

    # We select 10 kanji items based on seed_offset
    kanji_items = []
    for i in range(10):
        k_idx = (seed_offset * 2 + i) % len(kanji_items_bank)
        word, prompt, corr, opts, pVi, exp = kanji_items_bank[k_idx]
        kanji_items.append({
            "id": i + 1,
            "type": "mc",
            "prompt": prompt,
            "promptVi": pVi,
            "targetWord": word,
            "options": opts,
            "correct": corr,
            "explain": f"💡 <strong>Giải thích chữ Hán:</strong><br>• {exp}"
        })
        
    # VOCAB POOL: only terms present in A2-11..18 master vocabulary.
    vocab_items_bank = [
        ("料理", "日本の (   ) が 好きです。", 0, ["料理", "計画", "健康", "発音"], "Tôi thích món ăn Nhật.", "料理: món ăn, nấu ăn."),
        ("お酒", "健康のために、(   )を あまり 飲みません。", 0, ["お酒", "電車", "週末", "計画"], "Vì sức khỏe nên tôi không uống nhiều rượu.", "お酒: rượu, đồ uống có cồn."),
        ("発音", "日本語の (   ) を 練習します。", 0, ["発音", "料理", "結婚", "計画"], "Tôi luyện phát âm tiếng Nhật.", "発音: phát âm."),
        ("お祝い", "友達の 結婚の (   ) を します。", 0, ["お祝い", "お酒", "電車", "週末"], "Tôi chúc mừng đám cưới của bạn.", "お祝い: chúc mừng, quà mừng."),
        ("家族", "週末は (   ) と 食事を します。", 0, ["家族", "計画", "発音", "料理"], "Cuối tuần tôi ăn cơm cùng gia đình.", "家族: gia đình."),
        ("健康", "毎日 運動して、(   ) に なりたいです。", 0, ["健康", "結婚", "電車", "誕生日"], "Tôi muốn khỏe mạnh nhờ tập thể dục mỗi ngày.", "健康: sức khỏe, khỏe mạnh."),
        ("週末", "(   ) に 友達と 会います。", 0, ["週末", "毎日", "誕生日", "料理"], "Cuối tuần tôi gặp bạn.", "週末: cuối tuần."),
        ("誕生日", "今日は 母の (   ) です。", 0, ["誕生日", "結婚", "お祝い", "計画"], "Hôm nay là sinh nhật mẹ.", "誕生日: sinh nhật."),
        ("大切", "家族は とても (   ) です。", 0, ["大切", "健康", "有名", "週末"], "Gia đình rất quan trọng.", "大切: quan trọng, quý giá."),
        ("電車", "(   ) で 会社へ 行きます。", 0, ["電車", "料理", "お酒", "発音"], "Tôi đi tàu điện đến công ty.", "電車: tàu điện."),
        ("走ります", "毎朝 公園を (   )。", 0, ["走ります", "送ります", "思います", "着ます"], "Mỗi sáng tôi chạy trong công viên.", "走ります: chạy."),
        ("思います", "大切だと (   )。", 0, ["思います", "送ります", "走ります", "着ます"], "Tôi nghĩ là quan trọng.", "思います: nghĩ."),
    ]
    
    vocab_items = []
    for j in range(12):
        v_idx = (seed_offset + j) % len(vocab_items_bank)
        word, prompt, corr, opts, pVi, exp = vocab_items_bank[v_idx]
        q_num = 11 + j
        if q_num > 20:
            q_num += 3 # match numbering 24, 25
        vocab_items.append({
            "id": q_num,
            "type": "mc",
            "prompt": prompt,
            "promptVi": pVi,
            "options": opts,
            "correct": corr,
            "explain": f"💡 <strong>Giải thích từ vựng:</strong><br>• {exp}"
        })
        
    part1 = {
        "id": f"sec1_{code}",
        "partNumber": "I",
        "partTitle": "PHẦN 1: CHỮ HÁN & TỪ VỰNG (文字・語彙 - 22 CÂU)",
        "partDesc": "Gồm 2 dạng bài: Đọc chữ Hán (Câu 1-10) và Điền từ vựng thích hợp (Câu 11-20, 24, 25).",
        "badge": "25 Điểm",
        "groups": [
            {
                "groupTitle": "DẠNG 1: Chọn cách đọc Hiragana đúng nhất của chữ Hán gạch chân (Câu 1 - 10)",
                "groupInstruction": "Chọn 1 đáp án đúng nhất trong 4 phương án:",
                "items": kanji_items
            },
            {
                "groupTitle": "DẠNG 2: Chọn từ vựng thích hợp điền vào chỗ trống trong ngoặc (   ) (Câu 11 - 20, 24, 25)",
                "groupInstruction": "Chọn từ có ý nghĩa và ngữ cảnh chính xác nhất:",
                "items": vocab_items
            }
        ]
    }
    
    # GRAMMAR POOL (35 questions)
    grammar_items_bank = [
        # (Prompt, PromptVi, Correct, Options, Explain)
        ("ピクニックに 果物を 切って (   )。", "Tôi cắt sẵn hoa quả mang đi dã ngoại.", 0, ["いきます", "きます", "みます", "います"], "V-ていきます (Bài 11): Chuẩn bị rồi mang đi theo."),
        ("初めて 日本の 料理を (   )。とても おいしかったです。", "Lần đầu tiên tôi thử món ăn Nhật. Rất ngon.", 0, ["食べてみました", "食べていました", "食べすぎました", "食べたことがあります"], "V-てみる ➔ てみました: đã thử ăn (bài 11)."),
        ("肉と 魚と (   ) が 好きですか。", "Thịt và cá, bạn thích món nào hơn?", 0, ["どちら", "どこ", "だれ", "いつ"], "A と B と どちら (Bài 11): So sánh giữa 2 lựa chọn."),
        ("日曜日なら、(   ) 会えますよ。時間がありますから。", "Nếu là Chủ nhật thì lúc nào tôi cũng gặp được, vì tôi có thời gian.", 0, ["いつでも", "どこでも", "だれでも", "なんでも"], "いつでも (Bài 11): Bất cứ lúc nào."),
        ("この スープは (   ) そうですね。", "Bát súp này trông có vẻ nóng hổi đấy nhỉ.", 1, ["あつい", "あつ", "あつく", "あつかった"], "Tính từ đuôi い bỏ い + そうです (Bài 12): 熱い ➔ あつそうです."),
        ("この 部屋は 明る (   )、広いですね。", "Căn phòng này vừa sáng sủa lại vừa rộng rãi.", 0, ["くて", "で", "に", "の"], "Nối tính từ đuôi い: 明るい ➔ 明るくて (Bài 12)."),
        ("この 靴は 重く (   )、歩きやすいです。", "Đôi giày này không bị nặng và rất dễ đi.", 1, ["ないで", "なくて", "なかった", "ない"], "Nối tính từ phủ định: 重くない ➔ 重くなくて (Bài 12)."),
        ("京都の お寺は 静か (   )、きれいです。", "Chùa ở Kyoto vừa yên tĩnh lại vừa đẹp đẽ.", 1, ["くて", "で", "に", "の"], "Nối tính từ đuôi な: 静か ➔ 静かで (Bài 12)."),
        ("日本へ 行ったことが (   )。", "Tôi đã từng đi Nhật Bản.", 0, ["あります", "います", "します", "なります"], "V-た ことが あります: nói về kinh nghiệm đã từng (bài 13)."),
        ("昨日の 夜は お酒を 飲み (   ) ました。", "Tối hôm qua tôi đã uống quá nhiều rượu.", 2, ["すぎる", "すぎて", "すぎ", "すぎた"], "V-bỏ ます + すぎました (Bài 13): 飲みすぎました (uống quá mức)."),
        ("この ズボンは 少し (   ) すぎます。", "Chiếc quần này hơi dài quá.", 2, ["長い", "長く", "長", "長さ"], "Tính từ đuôi い bỏ い + すぎます (Bài 13): 長い ➔ 長すぎます."),
        ("結婚して ちょうど ５年 (   )。", "Chúng tôi kết hôn tính đến nay vừa tròn 5 năm.", 0, ["になります", "があります", "にします", "をします"], "Khoảng thời gian + になります (Bài 13): Đã đạt mốc."),
        ("ここで 写真を 撮って (   ) ですか。", "Tôi chụp ảnh ở đây có được phép không?", 0, ["もいい", "はいけない", "といい", "ください"], "V-てもいいですか (Bài 13): Xin phép làm việc gì."),
        ("出かける (   )、窓を 閉めて ください。", "Trước khi ra ngoài, xin hãy đóng cửa sổ lại.", 0, ["まえに", "あとで", "までに", "あと"], "V-る まえに (Bài 14): Trước khi làm V."),
        ("頭が 痛い ときは、薬を 飲む (   ) いいですよ。", "Khi bị đau đầu, bạn nên uống thuốc thì tốt đấy.", 1, ["が", "と", "を", "で"], "V-るといいですよ (Bài 14): Khuyên nhủ nên làm gì."),
        ("夜遅く 電話を かけ (   ) ください。", "Xin đừng gọi điện thoại vào lúc đêm muộn.", 0, ["ないで", "なくて", "ないと", "ませんで"], "V-ないでください (Bài 14): Xin đừng làm V."),
        ("週末は 映画を 見たり 買い物を (   )。", "Cuối tuần tôi khi thì xem phim khi thì đi mua sắm.", 0, ["したりします", "したりあります", "したりになります", "したりです"], "～たり～たりします (Bài 15): Liệt kê hành động."),
        ("あそこで 本を (   ) 人は 田中さんです。", "Người đang đọc sách đằng kia là anh Tanaka.", 0, ["読んでいる", "読みたい", "読んで", "読みます"], "Định ngữ: V-ている + N ➔ 読んでいる人 (Bài 15)."),
        ("どうして 試験を 受けなかった (   ) か。", "Tại sao bạn lại không tham gia kỳ thi vậy?", 0, ["んです", "です", "ます", "でした"], "Thể ngắn + んですか (Bài 16): Hỏi giải thích lý do."),
        ("これは 父が (   ) 時計です。", "Đây là chiếc đồng hồ bố tôi đã mua.", 0, ["買った", "買います", "買って", "買うです"], "Định ngữ quá khứ: V-た + N ➔ 父が買った時計 (Bài 15)."),
        ("明日は 天気が (   ) と 思います。", "Tôi nghĩ rằng ngày mai thời tiết sẽ đẹp.", 0, ["いい", "いいだ", "よく", "いいな"], "Tính từ い giữ nguyên trước と思います: いいと思います (Bài 18). Không thêm だ."),
        ("社長は 「来月 出張する」(   )。", "Giám đốc đã nói rằng 'Tháng sau tôi sẽ đi công tác'.", 0, ["と言いました", "と思いました", "といいでした", "んです"], "Trích dẫn: 「...」と言いました (Bài 18)."),
        ("この 料理は 自分 (   ) 作ったんです。", "Món ăn này là do tự tay tôi nấu đấy.", 2, ["が", "に", "で", "と"], "Phương thức: 自分で (tự mình làm - Bài 14)."),
        ("のど (   ) かわきました。お茶を 飲みたいです。", "Tôi khát nước quá. Tôi muốn uống trà.", 0, ["が", "に", "で", "と"], "Cụm cố định: のどがかわく (Bài 11/16)."),
        ("夏 (   ) 冬 (   ) どちらが 過ごしやすいですか。", "Mùa hè và mùa đông, mùa nào dễ chịu hơn?", 0, ["と・と", "に・が", "で・で", "が・に"], "A と B と どちら (Bài 11): So sánh 2 mùa."),
        ("この 歌手は 若い 人 (   ) 人気 (   ) あります。", "Ca sĩ này rất được giới trẻ yêu mến.", 0, ["に・が", "で・に", "が・で", "と・に"], "～に 人気がある: Được yêu thích bởi đối tượng nào (Bài 11)."),
        ("冷蔵庫の 中 (   ) 牛乳 (   ) ありますか。", "Trong tủ lạnh có sữa tươi không?", 0, ["に・が", "で・に", "が・で", "と・が"], "[Nơi chốn] に [Vật] が あります (Bài 11)."),
        ("来月 ハノイ (   ) 引っ越しします。", "Tháng sau tôi chuyển nhà đến Hà Nội.", 0, ["に", "で", "が", "を"], "Đích đến di chuyển: ハノイに 引っ越す (Bài 18)."),
        ("３か月前 (   ) 日本語の 勉強 (   ) 始めました。", "Cách đây 3 tháng tôi đã bắt đầu học tiếng Nhật.", 0, ["に・を", "で・が", "に・で", "が・に"], "３か月前に日本語の勉強を始めました. に chỉ thời điểm, を đánh dấu tân ngữ 勉強."),
        ("暑いですね。窓を (   ) も いいですか。", "Trời nóng quá. Tôi mở cửa sổ có được không?", 0, ["あけて", "あける", "あけた", "あけない"], "V-てもいいですか: あけてもいいですか (Bài 13)."),
        ("風邪を ひいたときは、暖かくして (   ) いいですよ。", "Khi bị cảm cúm, bạn nên giữ ấm cơ thể thì tốt đấy.", 0, ["ねると", "ねても", "ねたことが", "ねないで"], "V-るといいですよ: ねるといいですよ (Bài 14/16)."),
        ("日曜日は 音楽を (   )、掃除を し (   ) しました。", "Chủ nhật tôi khi thì nghe nhạc, khi thì dọn dẹp nhà cửa.", 0, ["聴いたり・たり", "聴いて・て", "聴く・く", "聴いた・た"], "～たり～たりしました (Bài 16)."),
        ("毎日 スマホ (   ) ゲームをして、頭 (   ) 痛いです。", "Ngày nào cũng chơi game bằng điện thoại nên đầu tôi bị đau.", 0, ["で・が", "に・に", "が・で", "と・に"], "Phương tiện: スマホで; Trạng thái: 頭が痛い (Bài 16)."),
        ("大学を 卒業 (   ) とき、先生 (   ) 手紙を 書きました。", "Khi tốt nghiệp đại học, tôi đã viết thư cho thầy giáo.", 0, ["した・に", "の・で", "する・が", "して・に"], "Động từ quá khứ 卒業したとき; Viết cho ai: 先生に (Bài 14)."),
        ("会議 (   ) 日時は 明日 (   ) いいと 思います。", "Thời gian họp thì tôi nghĩ là ngày mai sẽ tiện nhất.", 0, ["の・が", "が・に", "に・で", "で・の"], "会議の日時; 明日がいいと思います (Bài 18).")
    ]
    
    grammar_items = []
    for g in range(35):
        g_idx = (seed_offset * 3 + g) % len(grammar_items_bank)
        prompt, pVi, corr, opts, exp = grammar_items_bank[g_idx]
        grammar_items.append({
            "id": 26 + g,
            "type": "mc",
            "prompt": prompt,
            "promptVi": pVi,
            "options": opts,
            "correct": corr,
            "explain": f"💡 <strong>Giải thích ngữ pháp:</strong><br>• {exp}"
        })
        if g_idx in (20, 28):
            grammar_items[-1]["contentRevision"] = 2
        
    part2 = {
        "id": f"sec2_{code}",
        "partNumber": "II",
        "partTitle": "PHẦN 2: NGỮ PHÁP TRỌNG TÂM (文法 - 35 CÂU)",
        "partDesc": "Khảo sát toàn diện 35 mẫu ngữ pháp cốt lõi từ Bài 11 đến Bài 18 (Câu 26 đến Câu 60).",
        "badge": "40 Điểm",
        "groups": [
            {
                "groupTitle": "Chọn phương án đúng nhất (1, 2, 3 hoặc 4) để hoàn thành câu:",
                "groupInstruction": "Đọc kỹ câu hỏi và chú ý các dạng chia động từ, tính từ và trợ từ liên kết:",
                "items": grammar_items
            }
        ]
    }
    
    # READING POOL (8 questions across 3 passages)
    passages = [
        {
            "groupTitle": "BÀI ĐỌC 1: Lối Sống Lành Mạnh & Thể Thao (健康な生活)",
            "groupInstruction": "Đọc đoạn văn sau và trả lời các câu hỏi 1, 2, 3, 4:",
            "passage": "私は健康のために、毎朝30分散歩をしています。朝早く起きるのは大変ですが、空気がきれいで気持ちがいいです。雨の日は散歩を休んで、家でストレッチや軽い体操をします。\n朝ごはんを食べる前に、必ずコップ一杯の水を飲みます。前は朝ごはんを食べないことが多かったですが、今は毎朝しっかり食べるようにしています。体調がとてもよくなりました。\n週末は時間がありますから、自転車で少し遠い公園まで行って、景色を楽しんでいます。",
            "passageVi": "Để giữ gìn sức khỏe, mỗi buổi sáng tôi đi dạo bộ 30 phút. Dậy sớm buổi sáng tuy có vất vả nhưng không khí trong lành rất sảng khoái. Những ngày mưa tôi nghỉ đi dạo và ở nhà tập giãn cơ hoặc thể dục nhẹ nhàng.\nTrước khi ăn sáng, tôi luôn luôn uống một cốc nước. Trước đây tôi hay bỏ bữa sáng, nhưng bây giờ sáng nào tôi cũng ăn uống đầy đủ. Sức khỏe của tôi đã tốt lên rất nhiều.\nCuối tuần vì có thời gian rảnh nên tôi đạp xe đến công viên ở hơi xa một chút và ngắm cảnh sắc thiên nhiên.",
            "items": [
                {
                    "id": 61,
                    "type": "mc",
                    "prompt": "1. 雨の日、「私」は 何を しますか。",
                    "promptVi": "Vào những ngày trời mưa, nhân vật 'Tôi' làm gì?",
                    "options": ["雨の中でも散歩します。", "家でストレッチや体操をします。", "一日中寝ています。", "公園まで自転車で行きます。"],
                    "correct": 1,
                    "explain": "💡 Căn cứ câu: '雨の日は散歩を休んで、家でストレッチや軽い体操をします' ➔ Chọn đáp án 2."
                },
                {
                    "id": 62,
                    "type": "mc",
                    "prompt": "2. 朝ごはんを 食べる 前に、何を しますか。",
                    "promptVi": "Trước khi ăn bữa sáng, nhân vật 'Tôi' làm việc gì?",
                    "options": ["コップ一杯の水を飲みます。", "薬を飲みます。", "散歩を始めます。", "コーヒーを飲みます。"],
                    "correct": 0,
                    "explain": "💡 Căn cứ câu: '朝ごはんを食べる前に、必ずコップ一杯の水を飲みます' ➔ Chọn đáp án 1."
                },
                {
                    "id": 63,
                    "type": "mc",
                    "prompt": "3. 朝ごはんを しっかり 食べて、どう なりましたか。",
                    "promptVi": "Sau khi duy trì ăn sáng đầy đủ thì kết quả thế nào?",
                    "options": ["体調がとてもよくなりました。", "体重が増えすぎました。", "朝起きられなくなりました。", "病気になりました。"],
                    "correct": 0,
                    "explain": "💡 Căn cứ câu: '体調がとてもよくなりました' ➔ Chọn đáp án 1."
                },
                {
                    "id": 64,
                    "type": "mc",
                    "prompt": "4. 週末、「私」は 何を しますか。",
                    "promptVi": "Vào dịp cuối tuần, nhân vật 'Tôi' làm gì?",
                    "options": ["自転車で遠い公園へ行きます。", "一日中仕事をします。", "友だちと買い物をします。", "家でテレビを見ます。"],
                    "correct": 0,
                    "explain": "💡 Căn cứ câu: '週末は...自転車で少し遠い公園まで行って、景色を楽しんでいます' ➔ Chọn đáp án 1."
                }
            ]
        },
        {
            "groupTitle": "BÀI ĐỌC 2: Tiệc Mừng Thăng Chức Đồng Nghiệp (昇進のお祝い)",
            "groupInstruction": "Đọc đoạn văn sau và trả lời các câu hỏi 1, 2:",
            "passage": "来週、先輩の田中さんが課長に昇進します。課のみんなでお祝いをすることになりました。佐藤さんは「居酒屋で飲み会をしよう」と言いましたが、鈴木さんは「田中さんはお酒をあまり飲まないから、おいしいレストランで食事をするほうがいい」と言いました。\n話し合って、駅前の日本料理の店で食事会をして、みんなで記念のネクタイをプレゼントすることに決めました。",
            "passageVi": "Tuần tới, anh Tanaka tiền bối sẽ được thăng chức lên Trưởng phòng. Mọi người trong phòng quyết định sẽ tổ chức chúc mừng. Anh Sato bảo 'Đi nhậu ở quán Izakaya đi', nhưng chị Suzuki nói 'Anh Tanaka ít khi uống rượu nên đi ăn ở nhà hàng ngon thì hơn'.\nSau khi bàn bạc, cả nhóm quyết định mở tiệc ăn uống tại quán món Nhật trước nhà ga và cùng nhau tặng một chiếc cà vạt làm kỷ niệm.",
            "items": [
                {
                    "id": 65,
                    "type": "mc",
                    "prompt": "1. みんなは 田中さんのために どこへ 行くことに しましたか。",
                    "promptVi": "Mọi người quyết định sẽ đi đâu để mừng anh Tanaka?",
                    "options": ["駅前の居酒屋", "駅前の日本料理の店", "田中さんの家", "カラオケボックス"],
                    "correct": 1,
                    "explain": "💡 Căn cứ: '駅前の日本料理の店で食事会をして' ➔ Chọn đáp án 2 (Quán món Nhật trước ga)."
                },
                {
                    "id": 66,
                    "type": "mc",
                    "prompt": "2. みんなは 田中さんに 何を プレゼントしますか。",
                    "promptVi": "Mọi người sẽ tặng món quà gì cho anh Tanaka?",
                    "options": ["お酒", "高級な時計", "記念のネクタイ", "万年筆"],
                    "correct": 2,
                    "explain": "💡 Căn cứ: 'みんなで記念のネクタイをプレゼントすることに決めました' ➔ Chọn đáp án 3 (Cà vạt kỷ niệm)."
                }
            ]
        },
        {
            "groupTitle": "BÀI ĐỌC 3: Chuyến Công Tác & Sự Cố Máy Bay (出張とフライト)",
            "groupInstruction": "Đọc đoạn văn sau và trả lời các câu hỏi 1, 2:",
            "passage": "昨日、東京から福岡へ飛行機で出張しました。天気が悪くて、出発が1時間遅れました。福岡空港に着いたあと、すぐにタクシーで取引先の会社へ向かいました。時間に間に合って、大事な会議を無事に終えることができました。\n夜は現地の美味しいラーメンを食べて、ホテルでゆっくり休みました。",
            "passageVi": "Hôm qua, tôi đi máy bay từ Tokyo đến Fukuoka công tác. Vì thời tiết xấu nên chuyến bay xuất phát muộn 1 tiếng. Sau khi đến sân bay Fukuoka, tôi lập tức đi taxi tới công ty đối tác. May mắn là kịp giờ và tôi đã hoàn thành buổi họp quan trọng suôn sẻ.\nBuổi tối tôi ăn món mì ramen thơm ngon của địa phương rồi về khách sạn nghỉ ngơi thoải mái.",
            "items": [
                {
                    "id": 67,
                    "type": "mc",
                    "prompt": "1. 飛行機が 遅れた 理由は 何ですか。",
                    "promptVi": "Lý do máy bay bị chậm khởi hành là gì?",
                    "options": ["飛行機が故障したから", "天気が悪かったから", "空港が混んでいたから", "会議が長引いたから"],
                    "correct": 1,
                    "explain": "💡 Căn cứ câu: '天気が悪くて、出発が1時間遅れました' ➔ Chọn đáp án 2 (Do thời tiết xấu)."
                },
                {
                    "id": 68,
                    "type": "mc",
                    "prompt": "2. 会議は どうでしたか。",
                    "promptVi": "Buổi họp diễn ra như thế nào?",
                    "options": ["時間に遅れて怒られた。", "中止になった。", "時間に間に合って無事に終わった。", "取引先が来なかった。"],
                    "correct": 2,
                    "explain": "💡 Căn cứ câu: '時間に間に合って、大事な会議を無事に終えることができました' ➔ Chọn đáp án 3 (Kịp giờ và kết thúc an toàn/suôn sẻ)."
                }
            ]
        }
    ]
    
    part3 = {
        "id": f"sec3_{code}",
        "partNumber": "III",
        "partTitle": "PHẦN 3: ĐỌC HIỂU ĐOẠN VĂN (読解 - 8 CÂU)",
        "partDesc": "Gồm 3 bài khóa đời sống: Sức khỏe, Thăng chức đồng nghiệp, Đi công tác.",
        "badge": "20 Điểm",
        "groups": passages
    }
    
    # STAR ORDER POOL (6 items)
    star_items_bank = [
        # (Prompt, PromptVi, Parts, CorrectOrder, CorrectStarIdx, Explain)
        ("朝 起きて _________ ________ ____★____ _________。",
         "Sáng dậy sau khi uống một cốc nước tôi bắt đầu đi bộ.",
         ["散歩を", "水を", "飲んだあとで", "始めます"],
         [1, 2, 0, 3], 0,
         "Thứ tự: 朝起きて ➔ [2 水を] [3 飲んだあとで] [1 ★散歩を] [4 始めます]。Vị trí ★ là 1. 散歩を."),
         
        ("来週は _________ ________ ____★____ _________ と言っていました。",
         "Giám đốc đã nói rằng tuần sau trời sẽ trở nên lạnh hơn.",
         ["寒く", "天気が", "なると", "社長は"],
         [3, 1, 0, 2], 0,
         "Thứ tự: 来週は ➔ [4 社長は] [2 天気が] [1 ★寒く] [3 なると] と言っていました。Vị trí ★ là 1. 寒く."),
         
        ("この カバンは _________ ________ ____★____ _________ んです。",
         "Chiếc cặp này là tôi tự tay mua bằng tiền làm thêm đấy.",
         ["アルバイトの", "自分で", "お金で", "買った"],
         [0, 2, 1, 3], 1,
         "Thứ tự: このカバンは ➔ [1 アルバイトの] [3 お金で] [2 ★自分で] [4 買った] んです。Vị trí ★ là 2. 自分で."),
         
        ("京都へ _________ ________ ____★____ _________ ことがあります。",
         "Tôi đã từng đi du lịch Kyoto cùng gia đình một lần.",
         ["家族と", "一度", "旅行した", "いっしょに"],
         [1, 0, 3, 2], 3,
         "Thứ tự: 京都へ ➔ [2 一度] [1 家族と] [4 ★いっしょに] [3 旅行した] ことがあります。Vị trí ★ là 4. いっしょに."),
         
        ("風邪を _________ ________ ____★____ _________ といいですよ。",
         "Khi bị cảm cúm thì nên uống nhiều nước ấm rồi nghỉ ngơi thì tốt đấy.",
         ["暖かくして", "ひいたときは", "ゆっくり", "休む"],
         [1, 0, 2, 3], 2,
         "Thứ tự: 風邪を ➔ [2 ひいたときは] [1 暖かくして] [3 ★ゆっくり] [4 休む] といいですよ。Vị trí ★ là 3. ゆっくり."),
         
        ("会議の _________ ________ ____★____ _________ と思います。",
         "Địa điểm của cuộc họp thì tôi nghĩ phòng họp số 2 là tốt nhất.",
         ["場所は", "第2会議室が", "いい", "明日の"],
         [3, 0, 1, 2], 1,
         "Thứ tự: 会議の ➔ [4 明日の] [1 場所は] [2 ★第2会議室が] [3 いい] と思います。Vị trí ★ là 2. 第2会議室が.")
    ]
    
    star_items = []
    for s in range(6):
        prompt, pVi, parts, cOrder, cIdx, exp = star_items_bank[s]
        star_items.append({
            "id": 69 + s,
            "type": "star",
            "prompt": prompt,
            "promptVi": pVi,
            "parts": parts,
            "options": parts,
            "correctOrder": cOrder,
            "correct": cIdx,
            "explain": f"💡 <strong>Giải thích sắp xếp câu:</strong><br>• {exp}"
        })
        
    part4 = {
        "id": f"sec4_{code}",
        "partNumber": "IV",
        "partTitle": "PHẦN 4: BÀI TẬP SẮP XẾP TÌM DẤU SAO ★ (6 CÂU)",
        "partDesc": "Sắp xếp 4 phương án thành câu hoàn chỉnh và xác định vị trí của dấu sao ★.",
        "badge": "15 Điểm",
        "groups": [
            {
                "groupTitle": "Chọn phương án đúng ứng với vị trí dấu sao ★:",
                "groupInstruction": "Sắp xếp 4 từ/cụm từ theo đúng thứ tự ngữ pháp:",
                "items": star_items
            }
        ]
    }
    
    return {
        "code": code,
        "name": title,
        "tag": tag,
        "desc": desc,
        "timeLimit": 2700, # 45 minutes
        "sections": [part1, part2, part3, part4]
    }

# 1. DEGOC
degoc_exam = {
    "code": "DEGOC",
    "name": "Đề từ tài liệu PDF — Marugoto A2.1 bài 11–18",
    "tag": "📑 Chuyển từ tài liệu PDF",
    "desc": "71 câu ôn tập: chữ Hán, từ vựng, ngữ pháp, đọc hiểu và xếp câu. Khi cần, hãy đối chiếu với tài liệu PDF đính kèm.",
    "timeLimit": 2700,
    "sections": degoc_sections
}

# 2. Five brand new mock exams
mock_101 = create_mock_exam("M111", "Mã Đề M111 (Ôn tập A2.1)", "🎯 Tự luyện • M111", "Ôn cấu trúc V-ていきます/きます, ～そうです, ～すぎます và đọc hiểu.", 1)
mock_102 = create_mock_exam("M112", "Mã Đề M112 (Ôn tập tổng hợp)", "📘 Tự luyện • M112", "Ôn trợ từ に, で, と, を, cách đọc chữ Hán và đọc hiểu.", 2)
mock_103 = create_mock_exam("M113", "Mã Đề M113 (Ngữ pháp & Kanji)", "📚 Tự luyện • M113", "Luyện tính từ phủ định ～くなくて, định ngữ V-ている/V-た và xếp câu.", 3)
mock_104 = create_mock_exam("M114", "Mã Đề M114 (Đọc hiểu & giao tiếp)", "🗣️ Tự luyện • M114", "Ôn các tình huống đời sống và công việc trong bài 11–18.", 4)
mock_105 = create_mock_exam("M115", "Mã Đề M115 (Ôn tập cuối bài 11–18)", "📝 Tự luyện • M115", "Bài tự luyện tổng hợp; điểm không quy đổi thành kết quả thi JLPT chính thức.", 5)

ALL_EXAMS = [degoc_exam, mock_101, mock_102, mock_103, mock_104, mock_105]

for exam in ALL_EXAMS:
    counts = [sum(len(group["items"]) for group in section["groups"]) for section in exam["sections"]]
    if counts != [22, 35, 8, 6]:
        raise ValueError(f"{exam['code']}: invalid section counts {counts}")
    items = [item for section in exam["sections"] for group in section["groups"] for item in group["items"]]
    if len({item["id"] for item in items}) != len(items):
        raise ValueError(f"{exam['code']}: duplicate question IDs")
    for item in items:
        if not 0 <= item["correct"] < len(item["options"]):
            raise ValueError(f"{exam['code']} question {item['id']}: invalid correct option")
        if item["type"] == "star" and (
            sorted(item["correctOrder"]) != [0, 1, 2, 3] or item["correctOrder"][2] != item["correct"]
        ):
            raise ValueError(f"{exam['code']} question {item['id']}: inconsistent star order")

# Export to assets/data/de_thi_tong_hop_11_18_data.js
data_js_path = os.path.join(WORKSPACE, "assets/data/de_thi_tong_hop_11_18_data.js")
with open(data_js_path, "w", encoding="utf-8") as f:
    f.write("/* DATA ENGINE FOR DE THI TONG HOP JLPT A2.1 (BAI 11 - 18) */\n")
    f.write("window.DE_THI_TONG_HOP_DATA = ")
    json.dump(ALL_EXAMS, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated {len(ALL_EXAMS)} exams into {data_js_path}")
