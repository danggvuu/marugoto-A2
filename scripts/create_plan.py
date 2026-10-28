import os

base_dir = "Ke_Hoach_10_Ngay"
os.makedirs(base_dir, exist_ok=True)

days_content = {
    1: """# Ngày 1: Tăng tốc
## 1. Từ vựng (A1 Bài 8 nửa cuối, Bài 9, Bài 10 nửa đầu)
*Bài 8:* (Review các từ: ほん, カップ, にんぎょう... và học tiếp)
- P に すんでいます: Đang sống tại địa điểm P
- N と すんでいます: Đang sống cùng N
- ひとりで すんでいます: Đang sống một mình
- N が あります: Có N (Đồ vật)
- N が います: Có N (Con người, động vật)
- ともだち: Bạn bè
- でも、～: Nhưng
- あそびに きて ください。: Hãy đến chơi

*Bài 9:* なんじに おきますか。
- あさ: Sáng / ひる: Trưa / よる／ばん: Tối
- ごぜん: AM / ごご: PM
- あさごはん / ひるごはん / ばんごはん: Bữa sáng/trưa/tối
- いちにち: Một ngày / まいにち: Mỗi ngày / まいあさ: Mỗi sáng / まいばん: Mỗi tối
- いま: Bây giờ / うち: Nhà
- しんぶん: Báo / かいしゃ: Công ty / がっこう: Trường học
- おんがく: Âm nhạc / かじ: Việc nhà / にっき: Nhật ký / ブログ: Blog
- うんどう: Vận động / さんぽ: Đi dạo
- ～じ: ... giờ / なんじ？: Mấy giờ / ～ふん／ぷん: ... phút
- ～じかん: ... tiếng / ～ごろ: Khoảng...
- おきます: Thức dậy / たべます: Ăn / よみます: Đọc
- ききます: Nghe / かきます: Viết / みます: Xem
- します: Làm / いきます: Đi / かえります: Về / きます: Đến
- はいります: Vào / あびます: Tắm / ねます: Ngủ
- いそがしい: Bận rộn

*Bài 10:* いつが いいですか。 (Phần 1)
- きのう: Hôm qua / きょう: Hôm nay / あした: Ngày mai
- せんしゅう: Tuần trước / こんしゅう: Tuần này / らいしゅう: Tuần sau
- Thứ trong tuần: げつようび (T2), かようび (T3), すいようび (T4), もくようび (T5), きんようび (T6), どようび (T7), にちようび (CN)
- しゅうまつ: Cuối tuần / たんじょうび: Sinh nhật
- ～にち: Ngày... / ～がつ: Tháng...

## 2. Ngữ pháp trọng tâm
**Bài 8:** 
1. `Nがあります / います` (Diễn tả sự tồn tại)
   - Có đồ vật/cây cối: `N が あります` (VD: テレビがあります)
   - Có người/động vật: `N が います` (VD: いぬがいます)
2. `[Địa điểm] に N があります/います` (Ở đâu có cái gì/ai)

**Bài 9:**
1. Trợ từ chỉ thời gian `に`: `[Thời gian] に Vます` (Lúc mấy giờ làm gì. VD: 7時に おきます - Thức dậy lúc 7 giờ).
2. Trợ từ `を`: `N を Vます` (Chỉ đối tượng tác động của hành động. VD: ごはんを たべます - Ăn cơm).
3. Động từ đi lại: `[Địa điểm] に いきます / きます / かえります` (Đi/Đến/Về đâu).

**Bài 10:**
1. Thời gian tương đối (hôm nay, ngày mai, tuần này...) KHÔNG đi với trợ từ `に`.
""",
    2: """# Ngày 2: Chạy đà
## 1. Từ vựng (A1 Bài 10 nửa cuối, Bài 11)
*Bài 10 (Tiếp):*
- パーティー: Bữa tiệc / バースデーパーティー: Tiệc sinh nhật
- コンサート: Buổi hòa nhạc
- かいもの（を）します: Mua sắm
- べんきょう（を）します: Học tập
- テニス（をします）: Tennis
- しょくじ（を）します: Dùng bữa
- P に きます: Đến địa điểm P
- だいじょうぶ（な）: Ổn, được
- だめ（な）: Không được
- びょういん: Bệnh viện / はくぶつかん: Bảo tàng / びじゅつかん: Bảo tàng mỹ thuật / がっこう: Trường học / すいぞくかん: Thủy cung
- いつ？: Khi nào? / いつが いいですか。: Khi nào thì được? / いつでも いいです。: Khi nào cũng được
- ざんぎょう（を）します: Làm tăng ca
- ～じかん: ... tiếng / ～ぐらい: Khoảng... (số lượng)
- ときどき: Thỉnh thoảng / インターネット: Internet
- いっしゅうかん: Một tuần / スケジュール: Lịch trình

*Bài 11:* しゅみは なんですか。
- しゅみ: Sở thích
- スポーツ: Thể thao / えいが: Phim / おんがく: Âm nhạc / どくしょ: Đọc sách
- ダンス: Nhảy / え: Tranh / いけばな: Cắm hoa / おりがみ: Xếp giấy
- ぶんがく: Văn học / しょうせつ: Tiểu thuyết / まんが: Truyện tranh
- ファンタジー: Kỳ ảo / ミステリー: Bí ẩn / さどう: Trà đạo
- がいこくご: Ngoại ngữ / れんあい: Tình cảm
- ホラー: Kinh dị / コメディ: Hài / アクション: Hành động
- アニメ: Anime / ドラマ: Phim bộ
- クラシック: Nhạc cổ điển / ジャズ: Jazz / ロック: Rock / ポップス: Pop
- うた: Bài hát / ギター: Ghita / ピアノ: Piano
- サッカー: Bóng đá / やきゅう: Bóng chày / テニス: Tennis / じゅうどう: Judo
- ほんを よみます: Đọc sách / えいがを みます: Xem phim / おんがくを ききます: Nghe nhạc
- スポーツ（を） します: Chơi thể thao / えを かきます: Vẽ tranh / しゃしんを とります: Chụp ảnh
- ゆっくりします: Thư giãn / こうえんを さんぽします: Đi dạo / やすみます: Nghỉ ngơi
- はなします: Nói chuyện / いいます: Nói
- そと: Ngoài / ひ: Ngày / やすみの ひ: Ngày nghỉ / えき: Nhà ga / ざっし: Tạp chí / てら: Chùa / メール: Mail / ゲーム: Game
- ときどき: Thỉnh thoảng / ぜんぜん（－）: Hoàn toàn không...
- だいすき（な）: Rất thích
- どんな ＋ N ？: N như thế nào? / みせます: Cho xem

## 2. Ngữ pháp trọng tâm
**Bài 10:**
1. Rủ rê/Đề nghị: `Vませんか` (Cùng làm V nhé? VD: いっしょに ごはんを たべませんか)
2. Thống nhất lịch hẹn: `いつがいいですか` (Khi nào thì được?)

**Bài 11:**
1. Nói về sở thích: `わたしの しゅみは N です` (Sở thích của tôi là N).
2. Tần suất: `よく / ときどき / あまり(~ない) / ぜんぜん(~ない)`. (Lưu ý あまり và ぜんぜん đi với thể phủ định).
""",
    3: """# Ngày 3: Duy trì nhịp độ
## 1. Từ vựng (A1 Bài 12, Bài 13 nửa đầu)
*Bài 12:* いっしょに いきませんか。
- イベント: Sự kiện / まつり: Lễ hội / ショー: Buổi diễn / しあい: Trận đấu / はなびたいかい: Lễ hội pháo hoa / コンサート: Hòa nhạc
- たいこ: Trống / かぶき: Kịch Kabuki / すもう: Sumo
- はなみ: Ngắm hoa anh đào / チケット: Vé / ポスター: Áp phích / カレンダー: Lịch
- Thời gian (tháng, năm): せんげつ(Tháng trước) / こんげつ(Tháng này) / らいげつ(Tháng sau) / きょねん(Năm ngoái) / ことし(Năm nay) / らいねん(Năm sau)
- ～ねん: Năm... / ～がつ: Tháng... / ～にち／～か: Ngày... / なんがつ: Tháng mấy / なんにち: Ngày bao nhiêu
- たぶん: Có lẽ / もちろん: Đương nhiên
- たのしみです: Mong chờ / みに いきます: Đi xem / いっしょに: Cùng nhau
- ざんねん（な）: Đáng tiếc / むりょう: Miễn phí
- また こんど: Hẹn lần sau / いきましょう: Cùng đi nào / たんじょうび: Sinh nhật / しゅくじつ: Ngày lễ
- コンテスト: Cuộc thi / こくさいホール: Hội trường quốc tế / げんき（な）: Khỏe mạnh

*Bài 13:* どうやって いきますか。 (Phần 1)
- まち: Thành phố / のりもの: Phương tiện giao thông
- バイク: Xe máy / じてんしゃ: Xe đạp / バス: Xe bus / くるま: Xe oto / タクシー: Taxi
- でんしゃ: Tàu điện / ちかてつ: Tàu điện ngầm / ひこうき: Máy bay
- あるいて いきます: Đi bộ
- に のります: Lên (xe) / を おります: Xuống (xe)
- えき: Ga / くうこう: Sân bay / びょういん: Bệnh viện / ホテル: Khách sạn / ぎんこう: Ngân hàng / スーパー: Siêu thị / とうきょうタワー: Tháp Tokyo
- はやい: Nhanh / おそい: Chậm

## 2. Ngữ pháp trọng tâm
**Bài 12:**
1. Mời mọc nhiệt tình: `Vましょう` (Chúng ta cùng làm V đi!).
2. Rủ rê mềm mỏng: `Vませんか` (Có muốn làm V cùng không?).
3. Đáp lại lời mời: Tích cực (`いいですね`); Từ chối khéo (`...は ちょっと...`).

**Bài 13:**
1. Phương tiện di chuyển: `[Phương tiện] で いきます/きます/かえります` (Đi bằng phương tiện gì).
2. Trợ từ lên/xuống xe: `[Phương tiện] に のります` (Lên xe) / `[Phương tiện] を おります` (Xuống xe).
""",
    4: """# Ngày 4: Vượt dốc
## 1. Từ vựng (A1 Bài 13 nửa cuối, Bài 14, Bài 15 nửa đầu)
*Bài 13 (Tiếp):*
- たかい: Đắt / やすい: Rẻ / べんり: Tiện lợi / ふべん: Bất tiện
- とおい: Xa / ちかい: Gần / つかれます: Mệt mỏi
- らく（な）: Nhàn nhã / たいへん（な）: Vất vả
- バスのりば: Bến xe buýt / バスてい: Trạm dừng bus / サイン: Tín hiệu / カード: Thẻ / げんきん: Tiền mặt
- おきゃくさん: Khách hàng / もう いちど: Một lần nữa
- ともだちに あいます: Gặp bạn / どうやって？: Bằng cách nào?

*Bài 14:* ゆうめいな おてらです。
- ばしょ: Địa điểm / ところ: Nơi
- ぎんこう: Ngân hàng / おてら: Chùa / じんじゃ: Đền / ビル: Tòa nhà / とおり: Đường phố / デパート: Trung tâm thương mại / みせ: Cửa hàng / きっさてん: Quán cafe / コンビニ: Cửa hàng tiện lợi / こうばん: Đồn cảnh sát / ちず: Bản đồ
- ゆうめい（な）: Nổi tiếng / にぎやか（な）: Náo nhiệt / しずか（な）: Yên tĩnh
- たかい: Cao / ひくい: Thấp
- みぎ: Phải / ひだり: Trái / まえ: Trước / うしろ: Sau / なか: Trong / となり: Cạnh bên
- みぎに いきます: Sang phải / ひだりに いきます: Sang trái / まっすぐ いきます: Đi thẳng
- もしもし: Alo
- へいじつ: Ngày thường / きゅうじつ: Ngày nghỉ / えいぎょうじかん: Thời gian bán hàng / ていきゅうび: Ngày nghỉ cố định / ねんじゅうむきゅう: Cả năm không nghỉ
- たくさん: Nhiều / わたしたち: Chúng ta

*Bài 15:* かわいい (Phần 1)
- ふく: Quần áo / シャツ: Áo sơ mi / Tシャツ: Áo phông
- かさ: Ô / とけい: Đồng hồ / えはがき: Bưu thiếp / ハンカチ: Khăn tay
- バッグ: Túi / くつ: Giày / ぼうし: Mũ / さいふ: Ví
- おさけ: Rượu / じしょ: Từ điển / でんしじしょ: Kim từ điển
- はな: Hoa / もの: Đồ vật / アクセサリー: Phụ kiện
- クッキー: Bánh quy / チョコレート: Socola / ティーカップ: Tách trà
- ノート: Vở / ビデオカメラ: Máy quay / マウス: Chuột máy tính

## 2. Ngữ pháp trọng tâm
**Bài 13:**
1. Hỏi cách đi: `どうやって いきますか` (Đi bằng cách nào/Đường nào).
2. Điểm xuất phát - kết thúc: `A から B まで` (Từ A đến B).

**Bài 14:**
1. Tính từ đuôi な (な-Adjectives) và Tính từ đuôi い (い-Adjectives).
   - Bổ nghĩa cho danh từ: `Adj-な + N`, `Adj-い + N` (VD: ゆうめいな おてら - Ngôi chùa nổi tiếng).
2. Vị trí: `N の [みぎ/ひだり/まえ/うしろ/なか/となり]` (Phía phải/trái/trước/sau... của N).
""",
    5: """# Ngày 5: Cột mốc giữa chặng
## 1. Từ vựng (A1 Bài 15 nửa cuối, Bài 16)
*Bài 15 (Tiếp):*
- はし: Đũa / はしおき: Gác đũa / みみかき: Lấy ráy tai / にんじゃ: Ninja / しゅりけん: Phi tiêu
- リスト: Danh sách / プレゼント: Món quà / おみやげ: Quà lưu niệm
- Đếm đồ vật: ～こ (cái nhỏ), ～まい (tờ/cái mỏng), ～ほん (cái dài), ～さつ (quyển/cuốn)
- Tính từ: かっこいい (Ngầu), すごい (Tuyệt vời), おもしろい (Thú vị), かわいい (Dễ thương), おしゃれ（な） (Sành điệu), すてき（な） (Tuyệt vời), にほんてき（な） (Đậm chất Nhật)
- ほしい: Muốn có / あげます: Tặng / もらいます: Nhận / プレゼントします: Tặng quà
- かいます: Mua / かえます: Có thể mua / つかいます: Sử dụng

*Bài 16:* これ、ください。
- ふく: Quần áo / パンツ/ズボン: Quần / ジーンズ: Quần jeans / スカート: Chân váy
- コート: Áo khoác dài / ジャケット: Áo khoác ngắn / スーツ: Vest / ワンピース: Váy liền / くつした: Tất / ネクタイ: Cà vạt / スカーフ: Khăn quàng
- めがね: Kính
- Kích cỡ: サイズ (Size), エス (S), エム (M), エル (L)
- Màu sắc: いろ (Màu), あか (Đỏ), くろ (Đen), しろ (Trắng), あお (Xanh dương), みどり (Xanh lá), きいろ (Vàng), ピンク (Hồng), オレンジ (Cam), ちゃいろ (Nâu), グレー (Xám)
- Động từ mặc/đeo: シャツを きます (Mặc áo), ジーンズを はきます (Mặc quần), めがねを かけます (Đeo kính)
- Đếm tiền: ～ひゃく (trăm), ～せん (nghìn), ～まん (vạn), ～えん (Yên)
- ほか: Khác / まあまあ: Tàm tạm / にあいます: Hợp / どれ？: Cái nào?
- きて みても いいですか: Mặc thử được không?
- Nを ください: Lấy cho tôi N

## 2. Ngữ pháp trọng tâm
**Bài 15:**
1. Số đếm đồ vật: Đặt số lượng NGAY TRƯỚC động từ. (VD: Tシャツを 2まい かいます - Mua 2 cái áo phông).
2. Tính từ chỉ cảm xúc: `N が ほしいです` (Muốn có N).
3. Động từ cho/nhận: 
   - `[Người nhận] に あげます` (Tặng cho ai)
   - `[Người cho] に/から もらいます` (Nhận từ ai)

**Bài 16:**
1. Đại từ chỉ định: `これ / それ / あれ` (Cái này / Cái đó / Cái kia) và `このN / そのN / あのN`.
2. Yêu cầu khi mua hàng: `Nを ください` (Cho tôi lấy N).
3. Hỏi giá: `いくらですか` (Bao nhiêu tiền?).
""",
    6: """# Ngày 6: Xong chặng A1 - Sang trang mới
## 1. Từ vựng (A1 Bài 17, Bài 18, A2.1 Bài 1)
*Bài 17:* たのしかったです
- じゃあ、いいです: Vậy thì thôi/không cần đâu
- おきゃくさん: Khách hàng / てんいん: Nhân viên / ねだん: Giá cả / しょうひん: Sản phẩm
- ともだちに あいます: Gặp bạn / あそびます: Chơi / うたいます: Hát / カラオケをします: Hát Karaoke / アルバイトをします: Làm thêm / そうじをします: Dọn dẹp / せんたくをします: Giặt giũ
- つかれます: Mệt / かちます: Thắng
- たのしい: Vui vẻ / うれしい: Hạnh phúc / おおい: Nhiều (người) / すばらしい: Tuyệt vời / いそがしい: Bận rộn / おもしろい: Thú vị / たいへん（な）: Vất vả
- まあまあ: Tàm tạm / どこにも いきません: Không đi đâu cả / なにも しません: Không làm gì cả
- また: Lại / いちばん: Nhất

*Bài 18:* つぎは きょうとに いきたいです。
- とても: Rất / まご: Cháu / ショッピングセンター: Trung tâm thương mại / バーベキュー: BBQ
- でかけます: Ra ngoài / りょこうします: Du lịch / かいます: Mua / ホテルに とまります: Trọ lại khách sạn / やすみます: Nghỉ ngơi / つりを します: Câu cá / やまのぼりを します: Leo núi
- やまに のぼります: Leo núi / きょうと: Kyoto / てんぷら: Tempura / ふね: Thuyền / しんかんせん: Shinkansen / かぶき: Kabuki / きもの: Kimono
- なつやすみ: Nghỉ hè / アイスクリーム: Kem
- ながい: Dài / みじかい: Ngắn / おもしろい: Thú vị / つまらない: Nhàm chán / むずかしい: Khó / やさしい: Dễ / かんたん（な）: Đơn giản
- まず: Đầu tiên / つぎ: Tiếp theo / それから: Sau đó / でも: Nhưng / にもつ: Hành lý / パスポート: Hộ chiếu / スーツケース: Vali / ビザ: Visa

*A2.1 Bài 1:* 東京に すんでいます。
- Gia đình: りょうしん (Bố mẹ), きょうだい (Anh em), しまい (Chị em), しんせき (Họ hàng), そふ (Ông), そぼ (Bà), おじ (Chú), おば (Cô), おっと/ごしゅじん (Chồng), つま/おくさん (Vợ), むすこ (Con trai), むすめ (Con gái)
- わたしたち: Chúng tôi / イタリア: Ý / ブラジル: Brazil / オーストラリア: Úc / オペラ: Opera

## 2. Ngữ pháp trọng tâm
**Bài 17 & 18 (Ôn tập quá khứ & Thể TAI):**
1. Thời quá khứ của Tính từ:
   - い-Adj: `~かったです` (VD: たのしかったです)
   - な-Adj / Danh từ: `~でした` (VD: たいへんでした)
2. Mong muốn làm gì: `V-ます + たいです` (VD: いきたいです - Muốn đi).

**A2.1 Bài 1:**
1. Trạng thái tiếp diễn / Kết quả thói quen: `Vています` (VD: 東京にすんでいます - Đang sống ở Tokyo; けっこんしています - Đã kết hôn).
""",
    7: """# Ngày 7: Tiến vào A2.1
## 1. Từ vựng (A2.1 Bài 1 nửa cuối, Bài 2, Bài 3)
*A2.1 Bài 1 (Tiếp):*
- すみます -> すんでいます: Sinh sống
- はたらきます: Làm việc / おしえます: Dạy / かいご: Điều dưỡng
- ところ: Nơi / けっこんします: Kết hôn

*A2.1 Bài 2:* しゅみは クラシックを 聞くことです。
- りょうりを つくります: Nấu ăn / きってを あつめます: Sưu tập tem
- ともだちに なります: Trở thành bạn / うたいます: Hát / およぎます: Bơi / すいえい: Bơi lội / ドライブ: Lái xe đi dạo
- ひま（な）: Rảnh rỗi / わかい: Trẻ / きって: Tem / コイン: Đồng xu / おかし: Bánh kẹo / たこあげ: Thả diều / コメント: Bình luận / チキン: Thịt gà
- しょうかいします: Giới thiệu / じこしょうかい: Giới thiệu bản thân
- とくい（な）: Giỏi / しあい: Trận đấu / えんげき: Kịch / あみもの: Đan len / ガーデニング: Làm vườn / サイクリング: Đạp xe
- フルーツ: Trái cây / チェス: Cờ vua / ざんぎょう: Tăng ca / ぎゅうどん: Cơm bò / いろいろ（な）: Nhiều, đa dạng

*A2.1 Bài 3:* 日本はいま、はるです。
- きせつ: Mùa / てんき: Thời tiết
- はる: Xuân / なつ: Hè / あき: Thu / ふゆ: Đông
- あつい: Nóng / むしあつい: Oi bức / さむい: Lạnh / すずしい: Mát mẻ / あたたかい: Ấm áp
- あめ: Mưa / あめが ふります: Mưa rơi / うき: Mùa mưa / かんき: Mùa khô / つゆ: Mùa mưa (Nhật) / ゆき: Tuyết / ゆきが ふります: Tuyết rơi
- ～ど: ...độ / きおん: Nhiệt độ / しょうがつ: Tết
- はなが さきます: Hoa nở / はなみ: Ngắm hoa / にゅうがくしき: Lễ nhập học
- ひまわり: Hoa hướng dương / あじさい: Cẩm tú cầu / たんぼ: Đồng lúa / すいか: Dưa hấu / ゆかた: Yukata
- もみじ: Lá phong / つきみ: Ngắm trăng / ぶどう: Nho
- スキー: Trượt tuyết / こたつ: Bàn sưởi / みかん: Quýt / なべりょうり: Lẩu / セーター: Áo len
- うみ: Biển / やま: Núi / かわ: Sông / だんだん: Dần dần / にがて（な）: Kém, sợ / なります: Trở nên / だいたい: Đại khái

## 2. Ngữ pháp trọng tâm
**A2.1 Bài 2:** Danh từ hóa động từ: `V-る こと です`.
- Dùng để nói sở thích: `わたしの しゅみは [V-る]ことです` (Sở thích của tôi là làm V. VD: えいがを みることです).

**A2.1 Bài 3:**
1. Sự thay đổi: `Adj-い -> く なります` / `Adj-な -> に なります` (Trở nên... VD: あつくなります - Trở nên nóng).
2. So sánh nhất: `A と B と C で、[A/B/C] が いちばん Adj です` (Trong số A,B,C thì cái nào... nhất).
""",
    8: """# Ngày 8: Nước rút
## 1. Từ vựng (A2.1 Bài 4, Bài 5, Bài 6 nửa đầu)
*A2.1 Bài 4:* いい てんきですね。
- はれ / はれます: Trời quang / くもり / くもります: Nhiều mây / あめが やみます: Tạnh mưa / ゆきが つもります: Tuyết phủ
- かぜ: Gió / かぜが ふきます: Gió thổi / たいふう: Bão / ゆきだるま: Người tuyết
- そら: Bầu trời / くも: Mây / つき: Trăng / ほし: Sao / ほしが でます: Sao hiện
- ごぜんちゅう: Ban ngày / いちにちじゅう: Cả ngày / いちねんじゅう: Cả năm
- せかい: Thế giới / てんきよほう: Dự báo thời tiết
- げんき（な）: Khỏe mạnh / きもちが いい: Sảng khoái / つよい: Mạnh / よわい: Yếu
- でかけます: Ra ngoài / おかげさまで: Ơn trời / ひさしぶりです: Lâu không gặp

*A2.1 Bài 5:* この こうえんは ひろくて、きれいです。
- ばしょ: Địa điểm / ところ: Nơi / このあたり: Khu vực này
- どうぶつえん: Sở thú / ゆうえんち: Công viên giải trí / でんきてん: Cửa hàng điện / こうきょ: Hoàng cung / いざかや: Quán nhậu / うおいちば: Chợ cá / ゲームセンター: Game center
- ひろい: Rộng / せまい: Hẹp / ちかい: Gần / とおい: Xa / べんり: Tiện lợi / ふべん: Bất tiện
- はやい: Nhanh / おそい: Chậm / あかるい: Sáng / くらい: Tối / おおい: Nhiều / すくない: Ít / あぶない: Nguy hiểm
- おとな: Người lớn / わかいひと: Người trẻ
- にんき（があります）: Phổ biến, được chuộng / おすすめ: Gợi ý, tiến cử / ジョギング: Chạy bộ / ぜひ: Nhất định / ぜひ～てください: Nhất định hãy...

*A2.1 Bài 6:* まっすぐ 行ってください (Phần 1)
- たてもの: Tòa nhà / ビル: Tòa nhà / ゆうびんきょく: Bưu điện / たいしかん: Đại sứ quán / びじゅつかん: Bảo tàng mỹ thuật / はくぶつかん: Bảo tàng
- みち: Đường / とおり: Đường phố / はし: Cây cầu / こうさてん: Ngã tư / かど: Góc / しんごう: Đèn giao thông
- ひとつめの: Cái thứ nhất / ふたつめの: Cái thứ hai

## 2. Ngữ pháp trọng tâm
**A2.1 Bài 4:**
- Cụm danh từ bổ nghĩa: `[Câu ngắn bổ nghĩa] + N`. (VD: わたしが よくいく みせ - Quán tôi hay đi).

**A2.1 Bài 5:** Nối tính từ.
- `Adj-い -> ~くて` (VD: ひろくて、あかるいです - Vừa rộng vừa sáng).
- `Adj-な -> ~で` (VD: きれいで、しずかです - Vừa đẹp vừa yên tĩnh).
- `N -> ~で`
""",
    9: """# Ngày 9: Về đích
## 1. Từ vựng (A2.1 Bài 6 nửa cuối, Bài 7, Bài 8)
*A2.1 Bài 6 (Tiếp):*
- みぎ: Phải / みだり: Trái / まっすぐ: Thẳng
- はしを わたります: Qua cầu / まがります: Rẽ
- こうさてんを ひだり／みぎに まがります: Rẽ trái/phải ở ngã tư
- みえます: Có thể nhìn thấy / きこえます: Có thể nghe thấy
- たかい: Cao / ひくい: Thấp / まるい: Tròn / しろい: Trắng / くろい: Đen / あかい: Đỏ / あおい: Xanh / ほそながい: Thon dài

*A2.1 Bài 7:* 10時でも いいですか。
- おくれます: Muộn / まちます: Chờ / まちがえます: Nhầm lẫn / とまります: Dừng lại / まよいます: Lạc đường
- でかけます: Đi ra ngoài / きを つけます: Cẩn thận / れんらくします: Liên lạc / つきます: Đến nơi
- まちあわせ: Cuộc hẹn / じゅうたい: Tắc đường / じこ: Sự cố / ロビー: Sảnh / いりぐち: Lối vào / ほんや: Tiệm sách
- ちこくします: Đến muộn / はやく ＋ V: Làm V sớm / たのしみ: Mong đợi / りゆう: Lý do

*A2.1 Bài 8:* もうやけいを見に行きましたか。
- すいぞくかん: Thủy cung / やたい: Quầy hàng lưu động / タワー: Tháp / すいじょうバス: Bus dưới nước / れきし: Lịch sử / どうぶつ: Động vật / やけい: Cảnh đêm
- かんこう: Tham quan / かんこうち: Điểm tham quan
- せかい: Thế giới / せかいいち: Nhất thế giới
- りょうがえ: Đổi tiền / おすすめ: Gợi ý / ライトアップ: Lên đèn / めずらしい: Hiếm / ちず: Bản đồ / てんぷら: Tempura / ふね: Thuyền
- まだ: Vẫn chưa / もう～Vました: Đã làm V rồi
- よてい: Dự định / イルカ: Cá heo / カラオケ: Karaoke / ショー: Show diễn / スカイツリー: Skytree
- こんばん: Tối nay / おみやげ: Quà / しょくじの まえ: Trước bữa ăn / しょくじの あと: Sau bữa ăn / あとで: Sau đó

## 2. Ngữ pháp trọng tâm
**A2.1 Bài 6:**
1. Chỉ đường: `V-てください` (Xin hãy...). (VD: まっすぐ いってください - Hãy đi thẳng).
2. Tả ngoại hình/đặc điểm: `N が Adj です` (VD: あかい ぼうしです - Mũ màu đỏ).

**A2.1 Bài 7:** Xin phép & Xin lỗi
1. `V-ても いいですか`: Làm V có được không? (VD: 10じでも いいですか).
2. Thể て form để chỉ nguyên nhân (VD: じこが あって、おくれました - Vì có sự cố nên đến muộn).

**A2.1 Bài 8:**
1. Đi đâu để làm gì: `[Địa điểm] へ [V-bỏます] に いきます` (VD: やけいを みに いきます - Đi xem cảnh đêm).
2. `もう V-ましたか` (Đã làm V chưa?) -> `はい、もう V-ました` / `いいえ、まだです`.
""",
    10: """# Ngày 10: Chốt hạ
## 1. Từ vựng (A2.1 Bài 9, Bài 10)
*A2.1 Bài 9:* 日本語は はつおんが かんたんです。
- しょうがっこう / ちゅうがっこう / こうこう / だいがく / だいがくいん: Cấp 1 / Cấp 2 / Cấp 3 / Đại học / Cao học
- じゅぎょう: Giờ học / クラス: Lớp học
- おしえます: Dạy / はなします: Nói / かきます: Viết / ききます: Nghe / よみます: Đọc
- はつおん: Phát âm / もじ: Ký tự / ぶん: Câu văn / ぶんぽう: Ngữ pháp / たんご: Từ vựng / いみ: Ý nghĩa / がいこくご: Ngoại ngữ
- いままでに: Đến nay
- れんしゅうします: Luyện tập / おぼえます: Ghi nhớ / わすれます: Quên
- かします: Cho mượn / かります: Đi mượn / つかえます (つかいます): Sử dụng
- にて います: Giống / ちがいます: Khác / おなじ: Giống hệt
- しつもん: Câu hỏi / こたえ: Trả lời / しゅくだい: Bài tập
- じしょ: Từ điển / リスト: Danh sách / でんわばんごう: Số điện thoại
- チェックします: Kiểm tra / かんたん（な）: Đơn giản / むずかしい: Khó / せつめいします: Giải thích / てつだいます: Giúp đỡ / みせます: Cho xem / スピーチ: Phát biểu / ちゃわん: Bát

*A2.1 Bài 10:* 日本語は はつおんが かんたんです。(Phần cuối)
- きょうみが あります: Có hứng thú / りゅうがくします: Du học / しゅっちょうします: Công tác / つうやくします: Phiên dịch nói / ほんやくします: Biên dịch viết
- ならいます: Học (có người dạy) / でんわします: Gọi điện
- ぶんか: Văn hóa / しょうらい: Tương lai / サイト: Website / ことば: Ngôn từ / せいかつ: Sinh hoạt / うた: Bài hát / おどり: Nhảy múa / きっぷ: Vé
- かんこうきゃく: Khách du lịch / どうしたんですか: Bị sao vậy?
- まいつき: Mỗi tháng / まいとし: Mỗi năm / ～かい: ...lần
- いちにち: 1 ngày / いっしゅかん: 1 tuần / いっかげつ: 1 tháng / いちねん: 1 năm
- ガイド: Hướng dẫn viên

## 2. Ngữ pháp trọng tâm
**A2.1 Bài 9:**
1. Cấu trúc mô tả đặc điểm của một bộ phận/khía cạnh: `A は B が Adj です`
   - VD: 日本語は はつおんが かんたんです。(Tiếng Nhật thì phát âm đơn giản).
2. `V-て くださいませんか`: Nhờ vả lịch sự hơn `V-て ください`.

**A2.1 Bài 10:**
1. Khả năng: `V-る ことが できます` (Có thể làm V).
2. Tần suất hành động: `[Khoảng thời gian] に [Số lần] 回 V-ます` (VD: 1週間に 1回 - 1 lần 1 tuần).

**CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH TOÀN BỘ FILE TỪ VỰNG MARUGOTO N5!**
"""
}

for i in range(1, 11):
    folder_name = os.path.join(base_dir, f"Ngay_{i}")
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, f"Noi_dung_hoc_Ngay_{i}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(days_content[i])

print(f"Created {base_dir} with 10 folders and markdown files.")
