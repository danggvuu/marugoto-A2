"""Marugoto A2-2 grammar and kanji scope based on Japan Foundation references."""

from __future__ import annotations

import html
import json
from pathlib import Path


LESSON_CONTENT = {
    1: {
        "title": "いいなまえですね", "quote": "いいなまえですね",
        "subtitle": "Nói ý nghĩa tên, giới thiệu địa danh/người bằng という và bổ nghĩa danh từ bằng thể thông thường.",
        "sections": [
            ("N という意味 / N というところ", "Giải thích ý nghĩa và nêu tên một địa điểm.", "N1 という意味です。／N1 というところに住んでいます。", [("「あきこ」は「明るい子」という意味です。", "Akiko có nghĩa là “đứa trẻ tươi sáng”."), ("さいたまというところに住んでいます。", "Tôi sống ở một nơi tên là Saitama.")]),
            ("Thể thông thường + danh từ", "Mệnh đề thể thông thường đứng trước danh từ để bổ nghĩa cho danh từ đó.", "V thể thông thường ＋ N", [("先週買った本です。", "Đây là quyển sách tôi mua tuần trước."), ("私が好きなスポーツはテニスです。", "Môn thể thao tôi thích là quần vợt.")]),
        ],
        "links": ["Nという意味・ところ", "Thể thông thường ＋ N"],
    },
    2: {
        "title": "めがねをかけている人です", "quote": "めがねをかけている人です",
        "subtitle": "Miêu tả ngoại hình/trạng thái, nhận diện người bằng mệnh đề bổ nghĩa, nói ấn tượng với そう và dùng trạng từ ～く／～に.",
        "sections": [
            ("Tính chất + danh từ / Vている + danh từ", "Dùng mệnh đề trước danh từ để mô tả và nhận diện người.", "かみが長い人／歌を歌っている人", [("かみが長い人です。", "Đó là người có mái tóc dài."), ("歌を歌っている人です。", "Đó là người đang hát.")]),
            ("～そうです／～そうな N", "そう diễn tả ấn tượng nhìn thấy; tính từ な bỏ な trước そう.", "い形容詞 bỏ い ＋ そう／な形容詞 ＋ そう", [("やさしそうな人です。", "Trông có vẻ là người hiền."), ("上手そうです。", "Trông có vẻ giỏi.")]),
            ("Tính từ làm trạng từ: ～く／～に", "Dùng dạng trạng từ để mô tả cách thực hiện hành động.", "い形容詞: ～く／な形容詞: ～に", [("短く切ります。", "Cắt ngắn."), ("おいしそうに食べています。", "Đang ăn trông ngon lành.")]),
        ],
        "links": ["Mệnh đề bổ nghĩa danh từ", "～そうです", "Trạng từ ～く／～に"],
    },
    3: {
        "title": "おすすめは何ですか", "quote": "おすすめは何ですか",
        "subtitle": "Nêu lý do với ので, danh từ hóa với の, giới hạn/chọn chủ đề bằng なら và diễn tả phân phối với ずつ.",
        "sections": [
            ("Lý do: ～ので", "Nêu nguyên nhân một cách mềm mại.", "普通形 ＋ ので", [("この店はおいしいので、よく来ます。", "Vì quán này ngon nên tôi thường đến."), ("人気があるので、予約しました。", "Vì nổi tiếng nên tôi đã đặt chỗ.")]),
            ("Danh từ hóa: ～のは", "Dùng の để biến mệnh đề thành chủ đề/danh từ.", "普通形 ＋ のは ＋ N です", [("私が好きなのは、ステーキです。", "Món tôi thích là bít tết.")]),
            ("Chủ đề/điều kiện: ～なら", "Nêu lựa chọn phù hợp với chủ đề được nhắc đến.", "N ＋ なら", [("野菜なら、このサラダがいいですよ。", "Nếu chọn rau thì món salad này ngon đấy.")]),
            ("Phân phối: ～ずつ", "Chỉ chia đều theo số lượng hoặc từng lượt.", "Số lượng ＋ ずつ", [("一つずつください。", "Cho tôi mỗi thứ một phần."), ("二人ずつ座ってください。", "Xin hãy ngồi mỗi nhóm hai người.")]),
        ],
        "links": ["～ので", "～のは", "～なら", "～ずつ"],
    },
    4: {
        "title": "どうやって食べますか", "quote": "どうやって食べますか",
        "subtitle": "Nói điều cấm với ～てはいけません, trình tự với ～てから, cách làm không kèm hành động với ～ないで và kết quả với ～と.",
        "sections": [
            ("Cấm/không được: ～てはいけません", "Nêu quy định hoặc điều không được phép làm.", "Vて ＋ はいけません／だめです", [("ここで食べてはいけません。", "Không được ăn ở đây."), ("飲んじゃだめです。", "Không được uống.")]),
            ("Trình tự: ～てから", "Hành động sau bắt đầu sau khi hành động trước hoàn tất.", "Vて ＋ から", [("乾杯してから、飲みましょう。", "Sau khi cụng ly, chúng ta hãy uống.")]),
            ("Không làm V: ～ないで", "Diễn tả làm việc khác mà không thực hiện hành động V.", "Vない ＋ で", [("何もつけないで食べます。", "Tôi ăn mà không chấm gì."), ("箸を使わないで食べます。", "Tôi ăn mà không dùng đũa.")]),
            ("Điều kiện/kết quả: ～と", "Nêu kết quả thường xảy ra khi thực hiện hành động trước.", "Vる ＋ と", [("マヨネーズをつけて食べると、おいしいです。", "Chấm mayonnaise vào ăn thì ngon.")]),
        ],
        "links": ["～てはいけません", "～てから", "～ないで", "～と"],
    },
    5: {
        "title": "ぼうしを持っていったほうがいいです", "quote": "ぼうしを持っていったほうがいいです",
        "subtitle": "Đưa lời khuyên với ～た／ないほうがいい và nói thời điểm xảy ra hành động bằng ～とき.",
        "sections": [
            ("Đưa lời khuyên: ～ほうがいい", "Dùng thể た để khuyên nên làm và thể ない để khuyên không nên làm.", "Vた ＋ ほうがいい／Vない ＋ ほうがいい", [("ぼうしを持っていったほうがいいと思います。", "Tôi nghĩ bạn nên mang theo mũ."), ("9月は行かないほうがいいですよ。", "Tháng 9 thì bạn không nên đi.")]),
            ("Thời điểm: ～とき", "Mô tả việc xảy ra vào lúc làm hành động khác.", "Vる／Vた ＋ とき", [("沖縄に行くとき、船で行きました。", "Khi đi Okinawa, tôi đã đi bằng tàu."), ("旅行に行ったとき、写真を撮りました。", "Khi đi du lịch, tôi đã chụp ảnh.")]),
        ],
        "links": ["～ほうがいい", "～とき"],
    },
    6: {
        "title": "イルカのショーが見られます", "quote": "イルカのショーが見られます",
        "subtitle": "Dùng thể khả năng để nói điều có thể làm/xem và nối các lý do hoặc trải nghiệm bằng ～し.",
        "sections": [
            ("Thể khả năng", "Diễn tả năng lực hoặc điều kiện cho phép thực hiện hành động.", "Nhóm 1: u → eる／Nhóm 2: る → られる／する → できる", [("おしろの中が見られます。", "Có thể tham quan bên trong lâu đài."), ("ここでイルカのショーが見られます。", "Ở đây có thể xem biểu diễn cá heo.")]),
            ("Liệt kê lý do/đặc điểm: ～し", "Nêu nhiều lý do hoặc đặc điểm, thường dẫn đến kết luận.", "普通形 ＋ し、普通形 ＋ し", [("おどりも見たし、音楽も聞いたし、楽しめました。", "Tôi vừa xem múa vừa nghe nhạc nên đã rất vui."), ("海もきれいだし、食べ物もおいしいです。", "Biển đẹp mà đồ ăn cũng ngon.")]),
        ],
        "links": ["Thể khả năng", "～し"],
    },
    7: {
        "title": "雨がふったら、どうしますか", "quote": "雨がふったら、どうしますか",
        "subtitle": "Nói năng lực bằng thể khả năng và nêu điều kiện giả định với ～たら.",
        "sections": [
            ("Thể khả năng", "Nói về khả năng hoặc điều có thể thực hiện.", "話す → 話せる／する → できる", [("パウロさんは日本語が話せます。", "Paulo nói được tiếng Nhật."), ("日本語が話せる人です。", "Đó là người nói được tiếng Nhật.")]),
            ("Điều kiện: ～たら", "Nêu tình huống giả định hoặc việc xảy ra sau khi hoàn tất hành động.", "Vた ＋ ら", [("雨がふったら、ホールでぼんおどりをします。", "Nếu trời mưa, chúng ta sẽ tổ chức múa Bon trong hội trường."), ("時間があったら、行きましょう。", "Nếu có thời gian thì cùng đi nhé.")]),
        ],
        "links": ["Thể khả năng", "～たら"],
    },
    8: {
        "title": "コンサートはもう始まりましたか", "quote": "コンサートはもう始まりましたか",
        "subtitle": "Phân biệt もう／まだ khi nói tiến độ và đặt câu hỏi gián tiếp bằng mệnh đề thường + か.",
        "sections": [
            ("Tiến độ: もう／まだ", "もう hỏi việc đã xảy ra chưa; まだ dùng trong câu phủ định để nói vẫn chưa.", "もう ＋ Vましたか／まだ ＋ Vていません", [("準備はもう終わりましたか。", "Việc chuẩn bị xong chưa?"), ("いいえ、まだ終わっていません。", "Chưa, vẫn chưa xong.")]),
            ("Câu hỏi gián tiếp: ～か", "Đặt câu hỏi dạng mệnh đề trước 知っていますか／分かりますか.", "疑問詞 ＋ 普通形 ＋ か", [("コンサートが何時に始まるか、知っていますか。", "Bạn có biết hòa nhạc bắt đầu lúc mấy giờ không?"), ("店がどこにあるか、分かりますか。", "Bạn có biết cửa hàng ở đâu không?")]),
        ],
        "links": ["もう／まだ", "Câu hỏi gián tiếp ～か"],
    },
    9: {
        "title": "お正月休みは何をしましたか", "quote": "お正月休みは何をしましたか",
        "subtitle": "Kể trạng thái/khoảng thời gian trong quá khứ, dùng thể khả năng để nói cảm xúc và phân biệt しか／だけ.",
        "sections": [
            ("Trạng thái kéo dài trong quá khứ: ～ていました", "Diễn tả trạng thái hoặc hoạt động kéo dài trong một khoảng thời gian đã qua.", "Vていました", [("休みはメキシコに帰っていました。", "Trong kỳ nghỉ tôi đã về Mexico."), ("休みの間、家族と過ごしていました。", "Trong kỳ nghỉ tôi ở bên gia đình.")]),
            ("Khả năng + cảm xúc", "Dùng thể khả năng để nói vui vì làm được hoặc tiếc vì không làm được.", "V khả năng て／なくて ＋ よかった／残念でした", [("親に会えて、よかったです。", "Tôi vui vì đã gặp được cha mẹ."), ("友だちに会えなくて、残念でした。", "Tôi tiếc vì không gặp được bạn.")]),
            ("Giới hạn: しか／だけ", "しか đi với vị ngữ phủ định; だけ đi với vị ngữ khẳng định.", "N ＋ しか ＋ phủ định／N ＋ だけ", [("休みは3日しかありませんでした。", "Kỳ nghỉ chỉ có 3 ngày."), ("休みは3日間だけでした。", "Kỳ nghỉ chỉ kéo dài 3 ngày.")]),
        ],
        "links": ["～ていました", "Thể khả năng + cảm xúc", "しか／だけ"],
    },
    10: {
        "title": "いいことがあるといいですね", "quote": "いいことがあるといいですね",
        "subtitle": "Nói mục đích/kết quả mong muốn với ように, liệt kê ví dụ bằng ～たり và diễn đạt lời ước.",
        "sections": [
            ("Mục đích/kết quả mong muốn: ～ように", "Nêu điều mong muốn đạt được hoặc tránh xảy ra.", "V khả năng／Vない ＋ ように", [("わかい人が楽しめるように、イベントがあります。", "Có các sự kiện để người trẻ có thể vui chơi."), ("おくれないように、早く行きましょう。", "Cùng đi sớm để không bị muộn.")]),
            ("Liệt kê ví dụ: ～たり", "Nêu một vài hành động tiêu biểu, không hàm ý liệt kê hết.", "Vた ＋ り、Vた ＋ り します", [("願い事を書いたりして、楽しみます。", "Mọi người viết điều ước và làm những việc khác để vui chơi.")]),
            ("Ước mong: ～ように願います", "Nói điều mình cầu mong sẽ xảy ra hoặc không xảy ra.", "Vる／Vない ＋ ように願います", [("いいことがあるように願います。", "Tôi cầu mong có chuyện tốt xảy ra."), ("悪いことが起こらないように祈りました。", "Tôi đã cầu nguyện để chuyện xấu không xảy ra.")]),
        ],
        "links": ["～ように", "～たり", "～ように願う"],
    },
    11: {
        "title": "掃除機がこわれてしまったんです", "quote": "掃除機がこわれてしまったんです",
        "subtitle": "Diễn tả sự thay đổi với ～なくなる, sự cố đáng tiếc với ～てしまう, làm việc khác mà không làm V với ～ないで và mốc đến khi với ～まで.",
        "sections": [
            ("Thay đổi: ～なくなります", "Nói một trạng thái hoặc khả năng không còn như trước.", "Vない: bỏ い, đổi thành く ＋ なります", [("せんぷう機が動かなくなりました。", "Quạt đã không chạy nữa."), ("使えなくなりました。", "Đã trở nên không dùng được.")]),
            ("Sự cố/tiếc nuối: ～てしまう", "Diễn tả việc đã lỡ xảy ra hoặc kết thúc ngoài ý muốn.", "Vて ＋ しまいました／しまったんです", [("せんぷう機が動かなくなってしまいました。", "Quạt đã bị hỏng mất rồi."), ("電子レンジがこわれてしまったんです。", "Lò vi sóng bị hỏng mất rồi.")]),
            ("Không làm V: ～ないで／～まで", "～ないで diễn tả không thực hiện hành động; ～まで nêu mốc thời gian đến khi.", "Vない ＋ で／Vる ＋ まで", [("時間を気にしないで買い物できます。", "Có thể mua sắm mà không phải bận tâm về thời gian."), ("電子レンジが届くまで、1週間かかりました。", "Mất một tuần cho đến khi lò vi sóng được giao tới.")]),
        ],
        "links": ["～なくなる", "～てしまう", "～ないで／～まで"],
    },
    12: {
        "title": "こっちの方が安いです", "quote": "こっちの方が安いです",
        "subtitle": "Nói mức độ quá mức với ～すぎる, khả năng sử dụng thuận/khó với ～やすい／にくい và so sánh hai lựa chọn.",
        "sections": [
            ("Mức độ quá mức: ～すぎる", "Diễn tả quá nhiều/quá mức.", "い形容詞 bỏ い／な形容詞 bỏ な／Vます bỏ ます ＋ すぎる", [("このアイロンは重すぎます。", "Bàn ủi này nặng quá."), ("高すぎて、買えません。", "Đắt quá nên tôi không mua được.")]),
            ("Dễ/khó làm: ～やすい／にくい", "Gắn sau gốc masu để nói việc gì dễ hoặc khó thực hiện.", "Vます bỏ ます ＋ やすい／にくい", [("軽くて、使いやすいです。", "Nhẹ và dễ sử dụng."), ("重くて、使いにくいです。", "Nặng và khó sử dụng.")]),
            ("So sánh hai lựa chọn", "Dùng どちら để hỏi; の方が nêu lựa chọn có đặc điểm hơn.", "AとBと、どちらが～ですか。／Aの方が～です。", [("AモデルとBモデルと、どちらが安いですか。", "Giữa mẫu A và mẫu B, mẫu nào rẻ hơn?"), ("Bの方が安いです。", "Mẫu B rẻ hơn.")]),
        ],
        "links": ["～すぎる", "～やすい／にくい", "So sánh ～の方が"],
    },
    13: {
        "title": "この寺は14世紀に建てられました", "quote": "この寺は14世紀に建てられました",
        "subtitle": "Nói về Kyoto với いつ～ても, diễn tả nhóm người cùng làm bằng で và dùng thể bị động để nói công trình được xây dựng.",
        "sections": [
            ("Dù lúc nào: いつ～ても", "Diễn tả kết quả không đổi dù thời điểm thay đổi.", "いつ ＋ Vても", [("京都はいつ来ても、楽しめます。", "Đến Kyoto lúc nào cũng vui."), ("いつ見ても、きれいです。", "Lúc nào nhìn cũng đẹp.")]),
            ("Cùng nhau: ～と二人で", "で chỉ nhóm người cùng thực hiện hành động.", "Người ＋ と ＋ số người ＋ で", [("妹と二人で京都に来ました。", "Tôi đã đến Kyoto cùng em gái, hai chị em."), ("友だちと二人で見学しました。", "Tôi đã tham quan cùng một người bạn.")]),
            ("Thể bị động", "Dùng thể bị động để nói chủ thể chịu tác động hoặc công trình được xây dựng bởi ai.", "Vる → Vられる／Vう → Vわれる", [("京都は8世紀の終わりに天皇によってつくられました。", "Kyoto được xây dựng vào cuối thế kỷ thứ 8 bởi Thiên hoàng."), ("この寺は14世紀に建てられました。", "Ngôi chùa này được xây vào thế kỷ 14.")]),
        ],
        "links": ["いつ～ても", "～と二人で", "Thể bị động"],
    },
    14: {
        "title": "この絵は日本で一番古いマンガだそうです", "quote": "この絵は日本で一番古いマンガだそうです",
        "subtitle": "Truyền đạt thông tin nghe được với そうです, nói mục đích với ために và mô tả trạng thái đã được chuẩn bị bằng ～てあります.",
        "sections": [
            ("Nghe nói: ～そうです", "Dẫn lại thông tin nghe được; với danh từ/tính từ な dùng だそうです.", "普通形 ＋ そうです", [("この絵は日本で一番古いマンガだそうです。", "Nghe nói bức tranh này là truyện tranh cổ nhất Nhật Bản."), ("このお寺は有名だそうです。", "Nghe nói ngôi chùa này nổi tiếng.")]),
            ("Mục đích: ～ために", "Nêu mục đích của hành động hoặc đối tượng được phục vụ.", "Vる／Nの ＋ ために", [("イベントを知らせるために、カレンダーを作ります。", "Tôi làm lịch để thông báo sự kiện."), ("おみやげを買いたい人のために、店があります。", "Có cửa hàng dành cho người muốn mua quà lưu niệm.")]),
            ("Trạng thái chuẩn bị sẵn: ～てあります", "Diễn tả kết quả của hành động có chủ ý và trạng thái vẫn còn.", "Vて ＋ あります", [("受付にイベントカレンダーがおいてあります。", "Lịch sự kiện đã được đặt sẵn ở quầy tiếp tân.")]),
        ],
        "links": ["～そうです", "～ために", "～てあります"],
    },
    15: {
        "title": "会議室の電気がついたままです", "quote": "会議室の電気がついたままです",
        "subtitle": "Diễn tả trạng thái còn nguyên với ～たまま, thói quen chủ động với ～ようにしている và công dụng phù hợp với ～のにいい.",
        "sections": [
            ("Trạng thái giữ nguyên: ～たまま", "Trạng thái sau một hành động vẫn tiếp tục không đổi.", "Vた ＋ まま", [("会議室の電気がついたままです。", "Đèn phòng họp vẫn đang bật."), ("ドアが開いたままです。", "Cửa vẫn đang mở.")]),
            ("Duy trì thói quen: ～ようにしています", "Nói về điều mình chủ động cố gắng duy trì thường xuyên.", "Vる／Vない ＋ ようにしています", [("自分のはしを使うようにしています。", "Tôi cố gắng dùng đũa của mình."), ("わりばしを使わないようにしています。", "Tôi cố gắng không dùng đũa dùng một lần.")]),
            ("Công dụng phù hợp: ～のにいい", "Nêu việc gì hữu ích/thích hợp để đạt mục đích.", "Vる ＋ のにいいです", [("自分のはしは、ごみをへらすのにいいです。", "Đũa cá nhân hữu ích để giảm rác.")]),
        ],
        "links": ["～たまま", "～ようにしています", "～のにいい"],
    },
    16: {
        "title": "服が着られなくなりました", "quote": "服が着られなくなりました",
        "subtitle": "Nói một việc không còn làm được bằng thể khả năng phủ định + なる, đặt điều kiện với たら và chuyển đổi công dụng bằng NをNにする.",
        "sections": [
            ("Không còn làm được: ～なくなりました", "Dùng thể khả năng phủ định để nói vật không còn dùng/mặc được nữa.", "V khả năng phủ định ＋ なりました", [("服が着られなくなりました。", "Tôi không mặc vừa quần áo đó nữa."), ("バッグが使えなくなりました。", "Cái túi không dùng được nữa.")]),
            ("Điều kiện: ～たら", "Nêu việc sẽ làm khi điều kiện được đáp ứng.", "Vた ＋ ら", [("服が着られなくなったら、どうしますか。", "Nếu không mặc vừa quần áo nữa thì bạn sẽ làm gì?"), ("使わなくなったら、売ります。", "Nếu không dùng nữa thì tôi sẽ bán.")]),
            ("Chuyển thành: NをNにする", "Diễn tả biến đổi một vật thành vật/công dụng khác.", "N1 を N2 にします", [("ネクタイをバッグにしました。", "Tôi đã biến chiếc cà vạt thành túi."), ("ペットボトルをふくにしました。", "Họ đã biến chai nhựa thành quần áo.")]),
        ],
        "links": ["Thể khả năng phủ định + なる", "～たら", "NをNにする"],
    },
    17: {
        "title": "この人、しっていますか", "quote": "この人、しっていますか",
        "subtitle": "Nói thông tin nghe được với そう, nối trình tự với てから, nêu mốc cuối cùng với まで và phỏng đoán với かもしれません.",
        "sections": [
            ("Nghe nói: ～そうです", "Dẫn lại thông tin được nghe về một người/sự việc.", "普通形 ＋ そうです", [("この歌手は2回目の結婚をするそうです。", "Nghe nói ca sĩ này sẽ kết hôn lần thứ hai."), ("この人は有名だそうです。", "Nghe nói người này nổi tiếng.")]),
            ("Trình tự: ～てから／mốc đến: ～まで", "Nêu việc xảy ra sau một mốc hoặc tiếp diễn đến một mốc cuối.", "Vて ＋ から／Vる ＋ まで", [("画家になってから、フランスに行きました。", "Sau khi trở thành họa sĩ, ông ấy đã đến Pháp."), ("なくなるまで、フランスで絵をかきました。", "Ông ấy vẽ tranh ở Pháp cho đến khi qua đời.")]),
            ("Phỏng đoán: ～かもしれません", "Nói khả năng có thể đúng nhưng chưa chắc chắn.", "普通形 ＋ かもしれません", [("この画家は一番有名かもしれません。", "Họa sĩ này có lẽ là nổi tiếng nhất.")]),
        ],
        "links": ["～そうです", "～てから／～まで", "～かもしれません"],
    },
    18: {
        "title": "どんな子どもでしたか", "quote": "どんな子どもでしたか",
        "subtitle": "Hồi tưởng thời thơ ấu, dùng thể bị động để nói điều người khác làm với mình và diễn tả sự thay đổi/khả năng bằng ようになる.",
        "sections": [
            ("Thể bị động", "Dùng khi chủ thể nhận tác động từ người khác.", "Vる → Vられる／Vう → Vわれる", [("私は母にしかられました。", "Tôi bị mẹ mắng."), ("私は先生に絵をほめられました。", "Tôi được giáo viên khen tranh.")]),
            ("Thay đổi: ～ようになりました／～なくなりました", "Diễn tả thói quen hoặc trạng thái thay đổi theo thời gian.", "Vる ＋ ようになりました／Vなく ＋ なりました", [("朝早く起きるようになりました。", "Tôi đã bắt đầu dậy sớm."), ("夜テレビを見なくなりました。", "Tôi đã không còn xem TV vào buổi tối.")]),
            ("Thay đổi khả năng: ～ようになりました／～なくなりました", "Dùng thể khả năng để nói nay làm được hoặc không còn làm được việc gì.", "V thể khả năng ＋ ようになりました／V khả năng phủ định ＋ なりました", [("病気がよくなって、何でも食べられるようになりました。", "Bệnh đã đỡ nên tôi đã có thể ăn mọi thứ."), ("しゅうしょくしてから、友だちにあまり会えなくなりました。", "Sau khi đi làm, tôi không còn gặp bạn bè thường xuyên được nữa.")]),
        ],
        "links": ["Thể bị động", "～ようになる／～なくなる", "Thể khả năng + ～ようになる"],
    },
}


QUIZ_OVERRIDES = {
    (1, 10): ("「自己紹介」の読み方はどれですか。", ["じこしょうかい", "じこしょかい", "じしょうかい", "じこしょうがい"], "自己紹介 is included in the official Kanji list for Lesson 1."),
    (1, 11): ("「本屋」はどんな店ですか。", ["本を売る店", "魚を売る店", "服を作る店", "薬を作る店"], "本屋 means a bookstore."),
    (1, 12): ("「近く」の読み方はどれですか。", ["ちかく", "きんく", "ちかぐ", "きんじょ"], "近く is read ちかく."),
    (1, 14): ("「～番目（１番目）」の読み方はどれですか。", ["～ばんめ（いちばんめ）", "～ばんご（いちばんご）", "～ばんめ（いちばんもく）", "～ばんもく（いちばんめ）"], "The official list gives ～ばんめ（いちばんめ）."),
    (2, 11): ("「上手」の読み方はどれですか。", ["じょうず", "じょうて", "うわて", "かみて"], "上手 is read じょうず in this lesson."),
    (2, 12): ("「歌います」の意味はどれですか。", ["Hát", "Nhảy", "Viết", "Đọc"], "歌います means to sing."),
    (3, 6): ("「牛肉」の意味はどれですか。", ["Thịt bò", "Thịt gà", "Cá", "Rau"], "牛肉 is an official Kanji word in Lesson 3."),
    (3, 8): ("「地方」の読み方はどれですか。", ["ちほう", "じほう", "ちかた", "じかた"], "地方 is read ちほう."),
    (3, 10): ("「生（なま）」の意味はどれですか。", ["Sống, tươi", "Nấu chín", "Đắng", "Mặn"], "生（なま）means raw or fresh."),
    (3, 13): ("「冷たい」の読み方はどれですか。", ["つめたい", "あつい", "さむい", "あたたかい"], "冷たい is read つめたい."),
    (4, 6): ("「塩」の読み方はどれですか。", ["しお", "えん", "しょ", "しん"], "塩 is read しお."),
    (4, 9): ("「熱い」は何について使いますか。", ["熱い食べ物・物", "暑い天気", "冷たい飲み物", "長い時間"], "熱い describes hot objects or food; 暑い describes hot weather."),
    (4, 10): ("「食べ方」の読み方はどれですか。", ["たべかた", "たべほう", "しょくべかた", "たべがた"], "食べ方 is read たべかた."),
    (4, 13): ("「入れます」の読み方はどれですか。", ["いれます", "はいれます", "いります", "いられます"], "入れます is read いれます."),
    (5, 6): ("「木」の読み方はどれですか。", ["き", "もり", "しま", "ふね"], "木 is read き in the official list."),
    (5, 8): ("「予約します」の意味はどれですか。", ["Đặt trước", "Lái xe", "Trở về", "Ngủ"], "予約します means to make a reservation."),
    (5, 12): ("「船」の読み方はどれですか。", ["ふね", "ふな", "せん", "みなと"], "船 is read ふね."),
    (5, 14): ("「運転します」の意味はどれですか。", ["Lái xe", "Đặt chỗ", "Bơi", "Đến nơi"], "運転します means to drive."),
    (6, 4): ("「観光地」の読み方はどれですか。", ["かんこうち", "かんこち", "かんこうじ", "かんきょうち"], "観光地 is read かんこうち."),
    (6, 7): ("「料金」の意味はどれですか。", ["Giá, phí", "Miễn phí", "Không khí", "Động vật"], "料金 means a price or fee."),
    (6, 8): ("「無料」の読み方はどれですか。", ["むりょう", "むれい", "ぶりょう", "ぶれい"], "無料 is read むりょう."),
    (6, 10): ("「空気」の読み方はどれですか。", ["くうき", "そらき", "くき", "からき"], "空気 is read くうき."),
    (6, 13): ("「一年中」の意味はどれですか。", ["Quanh năm", "Một năm trước", "Một ngày", "Giữa năm"], "一年中 means all year round."),
    (7, 5): ("「受付」の読み方はどれですか。", ["うけつけ", "うけづけ", "うけつき", "うけづき"], "受付 is read うけつけ."),
    (7, 8): ("「中止します」の意味はどれですか。", ["Hủy bỏ", "Bắt đầu", "Tập trung", "Dạy"], "中止します means to cancel."),
    (7, 10): ("「集まります」の読み方はどれですか。", ["あつまります", "あつまりです", "しゅうまります", "あつめます"], "集まります is read あつまります."),
    (7, 12): ("「教えます」の読み方はどれですか。", ["おしえます", "おぼえます", "おしいます", "おしります"], "教えます is read おしえます."),
    (7, 14): ("「始まります」の意味はどれですか。", ["Bắt đầu", "Kết thúc", "Hủy bỏ", "Tập hợp"], "始まります means to start."),
    (8, 5): ("「会場」の読み方はどれですか。", ["かいじょう", "かいば", "えじょう", "かいしょう"], "会場 is read かいじょう."),
    (8, 7): ("「参加者」の意味はどれですか。", ["Người tham gia", "Người biểu diễn", "Người bán hàng", "Khách mời"], "参加者 means a participant."),
    (8, 9): ("「入場料」の読み方はどれですか。", ["にゅうじょうりょう", "にゅうじょうりょ", "いりばりょう", "にゅうじょうきん"], "入場料 is read にゅうじょうりょう."),
    (8, 11): ("「決めます」の読み方はどれですか。", ["きめます", "きります", "しめます", "はじめます"], "決めます is read きめます."),
    (8, 15): ("「急ぎます」の意味はどれですか。", ["Vội, gấp", "Bắt đầu", "Quyết định", "Tham gia"], "急ぎます means to hurry."),
    (9, 5): ("「正月」の読み方はどれですか。", ["しょうがつ", "せいげつ", "しょうつき", "まさつき"], "正月 is read しょうがつ."),
    (9, 7): ("「親」の意味はどれですか。", ["Cha mẹ", "Con cái", "Bạn bè", "Thầy cô"], "親 means parent(s)."),
    (9, 9): ("「年末」の意味はどれですか。", ["Cuối năm", "Đầu năm", "Năm ngoái", "Năm sau"], "年末 means the end of the year."),
    (9, 12): ("「年始」の読み方はどれですか。", ["ねんし", "ねんまつ", "としはじめ", "ねんじ"], "年始 is read ねんし."),
    (9, 15): ("「喜びます」の読み方はどれですか。", ["よろこびます", "かなしみます", "いそぎます", "いわいます"], "喜びます is read よろこびます."),
    (10, 5): ("「幸せ」の意味はどれですか。", ["Hạnh phúc", "Kỳ thi", "Người lớn", "Điều ước"], "幸せ means happiness."),
    (10, 7): ("「願い事」の読み方はどれですか。", ["ねがいごと", "ねがいもの", "がんじごと", "ねがごと"], "願い事 is read ねがいごと."),
    (10, 9): ("「合格」の読み方はどれですか。", ["ごうかく", "ごうがく", "こうかく", "ごうけつ"], "合格 is read ごうかく."),
    (10, 12): ("「成長」の意味はどれですか。", ["Sự trưởng thành, phát triển", "Cuối năm", "Lời chúc", "Phí vào cửa"], "成長 means growth."),
    (10, 15): ("「大人」の読み方はどれですか。", ["おとな", "おおひと", "だいじん", "たいにん"], "大人 is read おとな."),
    (11, 4): ("「電子レンジ」の読み方はどれですか。", ["でんしレンジ", "でんじレンジ", "でんしれんき", "でんきレンジ"], "電子レンジ is read でんしレンジ."),
    (11, 7): ("「調子」の意味はどれですか。", ["Tình trạng", "Sản phẩm", "Nhân viên", "Suy nghĩ"], "調子 means condition or state."),
    (11, 10): ("「動きます」の読み方はどれですか。", ["うごきます", "うごかします", "はたらきます", "うごります"], "動きます is read うごきます."),
    (11, 12): ("「商品」の意味はどれですか。", ["Sản phẩm, hàng hóa", "Tình trạng", "Đồ điện", "Âm thanh"], "商品 means a product or goods."),
    (11, 15): ("「店員」の読み方はどれですか。", ["てんいん", "てんにん", "みせいん", "ていいん"], "店員 is read てんいん."),
    (12, 10): ("「省エネ」の意味はどれですか。", ["Tiết kiệm năng lượng", "Sản xuất tại Nhật", "Chức năng", "Hài lòng"], "省エネ means energy saving."),
    (12, 13): ("「機能」の読み方はどれですか。", ["きのう", "きの", "きこう", "きよう"], "機能 is read きのう."),
    (12, 15): ("「日本製」の読み方はどれですか。", ["にほんせい", "にっぽんせい", "にほんしょう", "にほんせ"], "日本製 is read にほんせい."),
    (13, 5): ("「歴史」の読み方はどれですか。", ["れきし", "れっし", "れきじ", "れっじ"], "歴史 is read れきし."),
    (13, 7): ("「お寺」の意味はどれですか。", ["Chùa", "Đền Thần đạo", "Bảo tàng", "Cung điện"], "お寺 means a Buddhist temple."),
    (13, 9): ("「～世紀」の読み方はどれですか。", ["～せいき", "～せき", "～せいぎ", "～よき"], "～世紀 is read ～せいき."),
    (13, 12): ("「日本的」の意味はどれですか。", ["Mang tính Nhật Bản", "Trung tâm", "Lịch sử", "Phật giáo"], "日本的 means Japanese-style/Japanese in character."),
    (13, 15): ("「京都」の読み方はどれですか。", ["きょうと", "きょと", "けいと", "きょうど"], "京都 is read きょうと."),
    (14, 4): ("「博物館」の読み方はどれですか。", ["はくぶつかん", "はくものかん", "はくぶつがん", "はくもつかん"], "博物館 is read はくぶつかん."),
    (14, 6): ("「禁止」の意味はどれですか。", ["Cấm", "Giải thích", "Cần thiết", "Dụng cụ"], "禁止 means prohibition."),
    (14, 8): ("「道具」の読み方はどれですか。", ["どうぐ", "どうく", "みちぐ", "とうぐ"], "道具 is read どうぐ."),
    (14, 10): ("「説明」の読み方はどれですか。", ["せつめい", "せつみょう", "せつない", "せつねい"], "説明 is read せつめい."),
    (14, 12): ("「必要」の意味はどれですか。", ["Cần thiết", "Cấm", "Ăn uống", "Dụng cụ"], "必要 means necessary."),
    (14, 14): ("「～階」の読み方はどれですか。", ["～かい", "～がい", "～だん", "～けん"], "～階 is read ～かい in the example ２階."),
    (15, 4): ("「会議室」の読み方はどれですか。", ["かいぎしつ", "かいぎへや", "かいきしつ", "かいぎじつ"], "会議室 is read かいぎしつ."),
    (15, 6): ("「寒い」の意味はどれですか。", ["Lạnh (thời tiết)", "Nóng (đồ vật)", "Nhiệt độ", "Phòng họp"], "寒い describes cold weather."),
    (15, 8): ("「油」の読み方はどれですか。", ["あぶら", "あぶる", "ゆ", "あぶれ"], "油 is read あぶら."),
    (15, 10): ("「温度」の読み方はどれですか。", ["おんど", "おんと", "ぬくど", "おんどう"], "温度 is read おんど."),
    (15, 12): ("「紙」の意味はどれですか。", ["Giấy", "Dầu", "Nhiệt độ", "Hoạt động"], "紙 means paper."),
    (15, 15): ("「～度」の読み方はどれですか。", ["～ど", "～と", "～たび", "～どん"], "The counter 度 is read ど in 28度."),
    (16, 4): ("「自転車」の読み方はどれですか。", ["じてんしゃ", "じどうしゃ", "してんしゃ", "じてんじゃ"], "自転車 is read じてんしゃ."),
    (16, 6): ("「服」の意味はどれですか。", ["Quần áo", "Xe đạp", "Ô tô", "Giấy"], "服 means clothes."),
    (16, 8): ("「自動車」の読み方はどれですか。", ["じどうしゃ", "じてんしゃ", "じどうじゃ", "しどうしゃ"], "自動車 is read じどうしゃ."),
    (16, 10): ("「変わります」の読み方はどれですか。", ["かわります", "かえります", "かわれます", "へんわります"], "変わります is read かわります."),
    (16, 12): ("「売ります」の意味はどれですか。", ["Bán", "Cho mượn", "Trả lại", "Thay đổi"], "売ります means to sell."),
    (16, 15): ("「子ども用」の意味はどれですか。", ["Dành cho trẻ em", "Trẻ nhỏ", "Xe trẻ em", "Đồ trẻ em đã dùng"], "子ども用 means for children."),
    (17, 8): ("「生まれます」の意味はどれですか。", ["Được sinh ra", "Lớn lên", "Tốt nghiệp", "Thành công"], "生まれます means to be born."),
    (17, 10): ("「選手」の読み方はどれですか。", ["せんしゅ", "せんて", "えらびて", "せんじゅ"], "選手 is read せんしゅ."),
    (17, 12): ("「病気」の意味はどれですか。", ["Bệnh, ốm", "Giấc mơ", "Tác phẩm", "Cuộc đời"], "病気 means illness."),
    (17, 15): ("「入学」の読み方はどれですか。", ["にゅうがく", "にゅうこう", "いりがく", "にゅうかく"], "入学 is read にゅうがく."),
    (18, 4): ("「生活」の読み方はどれですか。", ["せいかつ", "せいがつ", "しょうかつ", "せいけつ"], "生活 is read せいかつ."),
    (18, 7): ("「不便」の意味はどれですか。", ["Bất tiện", "Tiện lợi", "Hạnh phúc", "Kỷ niệm"], "不便 means inconvenient."),
    (18, 9): ("「映画」の読み方はどれですか。", ["えいが", "えいか", "えが", "えいげ"], "映画 is read えいが."),
    (18, 11): ("「両親」の読み方はどれですか。", ["りょうしん", "りょうおや", "ふたおや", "りょしん"], "両親 is read りょうしん."),
    (18, 14): ("「選びます」の意味はどれですか。", ["Chọn", "Ngủ", "Thay đổi", "Hồi tưởng"], "選びます means to choose."),
    (1, 2): ("さいたま [____] ところに住んでいます。", ["という", "ので", "しか", "まで"], "N1 というところ giới thiệu tên địa điểm: さいたまというところ."),
    (1, 3): ("私は山田さんという [____] を知っています。", ["人", "意味", "ところ", "ため"], "N1というN2 giới thiệu người/vật có tên là N1."),
    (2, 8): ("あの人は元気 [____] です。", ["そう", "よう", "ため", "しか"], "N／な形容詞 + そう diễn tả ấn tượng: 元気そうです."),
    (2, 14): ("りんごを [____] 切ります。", ["小さく", "小さい", "小さな", "小さくて"], "い形容詞 chuyển sang trạng từ bằng cách đổi い thành く: 小さく切ります."),
    (3, 1): ("この店はおいしい [____]、よく来ます。", ["ので", "のは", "なら", "ずつ"], "ので nối lý do với kết quả: ngon nên thường đến."),
    (3, 2): ("私が好きな [____]、ステーキです。", ["のは", "ので", "なら", "ずつ"], "のは danh từ hóa mệnh đề làm chủ đề câu."),
    (3, 4): ("野菜 [____]、このサラダがいいですよ。", ["なら", "ので", "のは", "ずつ"], "なら nêu gợi ý theo chủ đề được nhắc tới."),
    (3, 9): ("コーヒーを二つ [____] お願いします。", ["ずつ", "ので", "なら", "のは"], "ずつ diễn tả phân chia theo từng đơn vị."),
    (3, 15): ("一つ [____] お願いします。", ["ずつ", "ので", "なら", "のは"], "ずつ diễn tả phân chia theo từng đơn vị."),
    (4, 1): ("ここで写真を [____] いけません。", ["撮っては", "撮らないで", "撮ってから", "撮ると"], "Vてはいけません diễn tả điều bị cấm."),
    (4, 2): ("飲み物は乾杯 [____]、飲みましょう。", ["してから", "しないで", "しては", "すると"], "Vてから nối hai hành động theo thứ tự."),
    (4, 3): ("何も [____] 食べます。", ["つけないで", "つけては", "つけると", "つけてから"], "Vないで diễn tả làm việc khác mà không thực hiện hành động V."),
    (4, 12): ("ここでは魚を [____] はいけません。", ["食べて", "食べないで", "食べると", "食べてから"], "食べてはいけません nghĩa là không được ăn."),
    (4, 15): ("しょうゆをつけて食べる [____]、おいしいです。", ["と", "まで", "しか", "ので"], "Vると nêu kết quả thường xảy ra."),
    (5, 4): ("沖縄に [____] とき、船で行きました。", ["行く", "行った", "行って", "行かない"], "Vるとき nêu thời điểm đi Okinawa."),
    (6, 1): ("おしろの中が [____]。", ["見られます", "見たり", "見ること", "見たし"], "見られます là thể khả năng của 見る."),
    (6, 2): ("今日のツアーはおどりも見た [____]、音楽も聞いたし、楽しめました。", ["し", "たり", "ので", "なら"], "～し liệt kê nhiều lý do/đặc điểm; mỗi vế dùng し."),
    (6, 5): ("ここではイルカのショーを [____]。", ["見られます", "見ますこと", "見たり", "見て"], "見られます diễn tả có thể xem."),
    (6, 11): ("沖縄旅行はどうでしたか。海が青くて、とても [____]。", ["きれいでした", "きれいだったです", "きれいですた", "きれいだでした"], "な形容詞 きれい quá khứ lịch sự là きれいでした."),
    (6, 14): ("この水族館では、イルカのショーが [____]。", ["見られます", "見たり", "見るし", "見て"], "Thể khả năng của 見る là 見られる／見られます."),
    (7, 2): ("日本語が [____] 人と話しました。", ["話せる", "話したら", "話して", "話すと"], "話す có thể dạng khả năng là 話せる."),
    (8, 3): ("コンサートが何時に始まる [____]、知っていますか。", ["か", "と", "ので", "まで"], "Câu hỏi gián tiếp dùng mệnh đề thường + か."),
    (8, 12): ("準備は [____] 終わりましたか。", ["もう", "まだ", "まで", "しか"], "もう hỏi xem việc đã hoàn tất hay chưa."),
    (9, 1): ("休みはメキシコに [____]。", ["帰っていました", "帰りました", "帰って", "帰ります"], "Vていました diễn tả việc đã ở/đang làm trong một khoảng thời gian đã qua."),
    (9, 4): ("私の休みは3日間 [____] でした。", ["だけ", "しか", "でも", "ので"], "だけ đi với vị ngữ khẳng định để nói chỉ có."),
    (9, 2): ("親に [____]、よかったです。", ["会えて", "会って", "会う", "会った"], "会える là thể khả năng; 会えてよかった diễn tả vui vì gặp được."),
    (9, 3): ("友だちに [____]、残念でした。", ["会えなくて", "会わないで", "会って", "会うので"], "会えなくて残念 diễn tả tiếc vì không gặp được."),
    (9, 11): ("今年は休みが3日 [____] ありませんでした。", ["しか", "だけ", "でも", "ので"], "しか đi cùng vị ngữ phủ định để nói chỉ có."),
    (10, 1): ("若い人が楽しめる [____]、イベントがあります。", ["ように", "ので", "なら", "まで"], "V khả năng + ように nêu mục đích/kết quả mong muốn."),
    (10, 2): ("七夕のとき、願い事を書いたり [____]、楽しみます。", ["して", "する", "した", "しない"], "Liệt kê ví dụ: Vたりして楽しみます."),
    (10, 3): ("いいことがある [____] 願います。", ["ように", "ので", "しか", "まで"], "Vるように願う diễn tả điều mong ước."),
    (10, 14): ("パーティーの時間におくれない [____]、早く行きましょう。", ["ように", "ので", "なら", "まで"], "Vないように nêu điều cần tránh để đạt mục đích."),
    (11, 2): ("ネットショッピングは時間を気に [____] 買い物できます。", ["しないで", "しなくて", "しない", "しなかった"], "Vないで買い物できます: có thể mua sắm mà không bận tâm thời gian."),
    (11, 5): ("せんぷう機が [____] なりました。", ["動かなく", "動かないで", "動いて", "動くまで"], "Vなくなる diễn tả trạng thái không còn hoạt động."),
    (11, 9): ("電子レンジがとどく [____]、1週間かかりました。", ["まで", "しか", "そう", "なら"], "まで nêu mốc thời gian cho đến khi hàng được giao."),
    (12, 4): ("このアイロンは重 [____]、使いにくいです。", ["すぎて", "やすくて", "にくくて", "すぎる"], "い形容詞 bỏ い + すぎて: 重すぎて."),
    (12, 8): ("このアイロンは軽くて、[____] やすいです。", ["使い", "使って", "使う", "使った"], "Vます bỏ ます + やすい: 使いやすい."),
    (13, 1): ("京都はいつ来て [____]、楽しめます。", ["も", "は", "か", "まで"], "いつVても diễn tả dù đến lúc nào thì kết quả vẫn vậy."),
    (13, 2): ("妹と [____] 京都に来ました。", ["二人で", "二人を", "二人に", "二人が"], "で đánh dấu nhóm người cùng thực hiện hành động."),
    (13, 3): ("京都は8世紀の終わりに天皇によって [____]。", ["つくられました", "つくりました", "つくって", "つくる"], "つくられました là thể bị động: được xây dựng."),
    (13, 14): ("京都はいつ来ても [____]。", ["楽しめます", "楽しみます", "楽しんで", "楽しむ"], "いつ来ても楽しめます diễn tả Kyoto luôn thú vị dù đến lúc nào."),
    (13, 11): ("この金閣寺は足利義満によって [____]。", ["建てられました", "建てました", "建てて", "建てる"], "建てられました là thể bị động: được xây dựng."),
    (14, 1): ("この絵は日本で一番古いマンガだ [____]。", ["そうです", "ようです", "ためです", "あります"], "Danh từ + だそうです dẫn lại thông tin nghe được."),
    (14, 2): ("イベントを知らせる [____]、カレンダーを作ります。", ["ために", "ように", "ので", "まで"], "Vるために nêu mục đích của hành động."),
    (14, 11): ("受付にイベントカレンダーがおいて [____]。", ["あります", "います", "します", "なります"], "Vてあります diễn tả vật được chuẩn bị/đặt sẵn và trạng thái còn đó."),
    (15, 1): ("会議室の電気が [____] ままです。", ["ついた", "つけて", "つく", "ついて"], "Vたまま diễn tả trạng thái tiếp tục giữ nguyên."),
    (15, 2): ("私は自分のはしを使う [____] しています。", ["ように", "ために", "ので", "まで"], "Vるようにしています nói về thói quen mình cố gắng duy trì."),
    (15, 11): ("会議室の電気を消す [____] しています。", ["ように", "ために", "ので", "まで"], "Vるようにしています diễn tả thói quen được duy trì."),
    (15, 14): ("自分のはしは、ごみをへらす [____] いいです。", ["のに", "ので", "なら", "まで"], "Vるのにいい nêu công dụng phù hợp."),
    (16, 1): ("服が着られなく [____]。", ["なりました", "しました", "あります", "いました"], "Thể khả năng phủ định + なる: không còn mặc được nữa."),
    (16, 2): ("服が着られなくなった [____]、どうしますか。", ["ら", "ので", "まで", "そう"], "Vたら nêu điều kiện: nếu không mặc được nữa thì làm gì?"),
    (16, 3): ("ゆうこさんはネクタイをバッグ [____] しました。", ["に", "で", "を", "が"], "NをNにする diễn tả biến vật này thành vật khác."),
    (16, 11): ("服が着られなくなった [____]、フリーマーケットで売ります。", ["ら", "ので", "まで", "そう"], "Vたら nêu điều kiện: nếu không mặc được nữa thì bán."),
    (17, 1): ("この歌手は2回目の結婚をする [____] です。", ["そう", "よう", "まで", "しか"], "普通形 + そうです dẫn lại thông tin nghe được."),
    (17, 2): ("この人は画家になって [____]、フランスに行きました。", ["から", "まで", "そう", "しか"], "Vてから nêu hành động xảy ra sau khi trở thành họa sĩ."),
    (17, 3): ("画家はなくなる [____]、フランスで絵をかきました。", ["まで", "から", "そう", "しか"], "まで nêu mốc cuối cùng của hành động."),
    (17, 4): ("この画家は一番有名 [____] しれません。", ["かも", "ので", "まで", "しか"], "かもしれません diễn tả phỏng đoán chưa chắc chắn."),
    (18, 1): ("私は母に [____]。", ["しかられました", "しからせました", "しかりました", "しかって"], "しかられました là thể bị động: bị mẹ mắng."),
    (18, 2): ("朝早く起きるように [____]。", ["なりました", "しました", "あります", "いました"], "Vるようになりました diễn tả thói quen mới hình thành."),
    (18, 5): ("夜テレビを見 [____] なりました。", ["なく", "ないで", "なくて", "ない"], "Vなくなりました diễn tả một việc không còn xảy ra."),
}

GRAMMAR_OVERRIDE_IDS = {
    (1, 1), (1, 2), (1, 3), (1, 6), (1, 13), (2, 1), (2, 2), (2, 3), (2, 5), (2, 6), (2, 8), (2, 14), (2, 15),
    (3, 1), (3, 2), (3, 4), (3, 9), (3, 15),
    (4, 1), (4, 2), (4, 3), (4, 5), (4, 12), (4, 15), (5, 1), (5, 2), (5, 4), (5, 9),
    (6, 1), (6, 2), (6, 5), (6, 11), (6, 14), (7, 1), (7, 2), (7, 4), (7, 13), (8, 1), (8, 2), (8, 3), (8, 12),
    (9, 1), (9, 2), (9, 3), (9, 4), (9, 11), (10, 1), (10, 2), (10, 3), (10, 14),
    (11, 1), (11, 2), (11, 5), (11, 9), (12, 1), (12, 2), (12, 4), (12, 8), (12, 9),
    (13, 1), (13, 2), (13, 3), (13, 11), (13, 14), (14, 1), (14, 2), (14, 11),
    (15, 1), (15, 2), (15, 11), (15, 14), (16, 1), (16, 2), (16, 3), (16, 11),
    (17, 1), (17, 2), (17, 3), (17, 4), (18, 1), (18, 2), (18, 5), (18, 12),
}


def _render_section(index: int, section: tuple) -> str:
    title, description, formula, examples = section
    example_html = "\n".join(
        f'''<div class="example-item"><div class="ex-text-wrap">
            <div class="ex-jp">{html.escape(jp)}</div>
            <div class="ex-vi">{html.escape(vi)}</div>
        </div></div>'''
        for jp, vi in examples
    )
    return f'''<section class="content-section" id="sec-grammar{index}">
        <div class="section-header">
            <h2 class="section-title"><span>📘</span> {index}. {html.escape(title)}</h2>
            <span class="section-tag">Ngữ pháp Marugoto</span>
        </div>
        <p style="margin-bottom:16px;color:#334155">{html.escape(description)}</p>
        <div class="grammar-card"><div class="rule-box" style="border-left-color:#4f46e5">
            <div class="rule-formula" style="color:#3730a3">{html.escape(formula)}</div>
        </div><div class="example-list">{example_html}</div></div>
    </section>'''


def _official_kanji_question(question_id: int, items: list[dict], index: int) -> tuple[str, list[str], str]:
    item = items[index % len(items)]
    use_reading = question_id % 2 == 0
    field = "kana" if use_reading else "mean"
    answer = item[field]
    options = [answer]
    for offset in range(1, len(items) + 1):
        candidate = items[(index + offset) % len(items)][field]
        if candidate not in options:
            options.append(candidate)
        if len(options) == 4:
            break
    if len(options) < 4:
        raise ValueError(f"Not enough distinct official Kanji choices for {item['word']}")
    if use_reading:
        question = f"Từ Kanji 「{item['word']}」 có cách đọc nào?"
        explain = f"{item['word']} đọc là 「{item['kana']}」 theo danh sách Kanji chính thức của bài học này."
    else:
        question = f"Từ Kanji 「{item['word']}」 có nghĩa là gì?"
        explain = f"{item['word']} nghĩa là {item['mean']}."
    return question, options, explain


def apply_official_curriculum(lessons: list[dict], root: Path) -> None:
    official_kanji = json.loads((root / "data/kanji_vocab_a2_2_official.json").read_text(encoding="utf-8"))
    for cfg in lessons:
        number = cfg["num"]
        content = LESSON_CONTENT[number]
        cfg["title"] = content["title"]
        cfg["quote"] = content["quote"]
        cfg["subtitle"] = content["subtitle"]
        cfg["grammar"] = [_render_section(i, section) for i, section in enumerate(content["sections"], 1)]
        cfg["section_links"] = [
            f'<a href="#sec-grammar{i}" class="sec-link">{i}. {html.escape(label)}</a>'
            for i, label in enumerate(content["links"], 1)
        ]
        cfg["kanji_list"] = official_kanji[f"lesson_{number}"]
        cfg["kanji_cards"] = cfg["kanji_list"]
        cfg["morph_labels"] = {
            "form1": "Ví dụ chia thể (bổ trợ)",
            "form2": "Thể quá khứ ngắn",
            "form3": "Thể từ điển",
        }
        kanji_question_index = 0
        for question in cfg["quiz"]:
            replacement = QUIZ_OVERRIDES.get((number, question["id"]))
            if replacement:
                question["q"], question["options"], question["explain"] = replacement
                question["correct"] = 0
                if (number, question["id"]) in GRAMMAR_OVERRIDE_IDS:
                    question["category"] = "Ngữ pháp"
            if question["category"] == "Chữ Hán":
                scope_word = cfg["kanji_list"][kanji_question_index % len(cfg["kanji_list"])]["word"]
                question["q"], question["options"], question["explain"] = _official_kanji_question(
                    question["id"], cfg["kanji_list"], kanji_question_index
                )
                question["correct"] = 0
                question["scopeKanji"] = scope_word
                kanji_question_index += 1
            if (number, question["id"]) in GRAMMAR_OVERRIDE_IDS:
                question["category"] = "Ngữ pháp"
                question["grammarScope"] = "official"
            if question["category"] == "Ngữ pháp":
                question["grammarScope"] = "official"
        if number == 17:
            # This biography sentence is useful vocabulary practice, not one of
            # the lesson's listed grammar patterns.
            next(q for q in cfg["quiz"] if q["id"] == 11)["category"] = "Từ vựng"
