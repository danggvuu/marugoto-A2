/* Extracted page script for tests/On_Tap_Mini_Test_A2_1_4.html */
// Dữ liệu nhúng trực tiếp
const rawVocab = [{"l": "A2-1", "jp": "りょうしん", "vi": "Bố mẹ"}, {"l": "A2-1", "jp": "きょうだい", "vi": "Anh chị em"}, {"l": "A2-1", "jp": "しまい", "vi": "Chị em gái"}, {"l": "A2-1", "jp": "しんせき", "vi": "Họ hàng"}, {"l": "A2-1", "jp": "そふ/おじいさん", "vi": "Ông"}, {"l": "A2-1", "jp": "そぼ/おばあさん", "vi": "Bà"}, {"l": "A2-1", "jp": "おじ/おじさん", "vi": "Chú, bác trai"}, {"l": "A2-1", "jp": "おば/おばさん", "vi": "Cô, bác gái, dì"}, {"l": "A2-1", "jp": "おっと/ごしゅじん", "vi": "Chồng mình / Chồng người khác"}, {"l": "A2-1", "jp": "つま/おくさん", "vi": "Vợ mình / Vợ người khác"}, {"l": "A2-1", "jp": "むすこ/むすこさん", "vi": "Con trai mình / Con trai người khác"}, {"l": "A2-1", "jp": "むすめ/むすめさん", "vi": "Con gái mình / Con gái người khác"}, {"l": "A2-1", "jp": "わたしたち", "vi": "Chúng tôi"}, {"l": "A2-1", "jp": "イタリア", "vi": "Nước Ý"}, {"l": "A2-1", "jp": "ブラジル", "vi": "Nước Brazil"}, {"l": "A2-1", "jp": "オーストラリア", "vi": "Nước Úc"}, {"l": "A2-1", "jp": "オペラ", "vi": "Opera"}, {"l": "A2-1", "jp": "すみます/すんでいます", "vi": "Sinh sống"}, {"l": "A2-1", "jp": "はたらきます", "vi": "Làm việc"}, {"l": "A2-1", "jp": "おしえます", "vi": "Dạy, chỉ cho biết"}, {"l": "A2-1", "jp": "かいご", "vi": "Điều dưỡng"}, {"l": "A2-1", "jp": "ところ", "vi": "Nơi"}, {"l": "A2-1", "jp": "けっこん(します)", "vi": "Kết hôn"}, {"l": "A2-2", "jp": "(りょうりを)つくります", "vi": "Làm, nấu (món ăn)"}, {"l": "A2-2", "jp": "(きってを)あつめます", "vi": "Sưu tập (tem)"}, {"l": "A2-2", "jp": "ともだちに なります", "vi": "Trở thành bạn bè"}, {"l": "A2-2", "jp": "うたいます", "vi": "Hát"}, {"l": "A2-2", "jp": "およぎます", "vi": "Bơi"}, {"l": "A2-2", "jp": "すいえい", "vi": "Việc bơi lội"}, {"l": "A2-2", "jp": "ドライブ", "vi": "Lái xe đi chơi"}, {"l": "A2-2", "jp": "ひま(な)", "vi": "Rảnh rỗi"}, {"l": "A2-2", "jp": "わかい", "vi": "Trẻ"}, {"l": "A2-2", "jp": "きって", "vi": "Tem"}, {"l": "A2-2", "jp": "コイン", "vi": "Đồng xu"}, {"l": "A2-2", "jp": "おかし", "vi": "Bánh kẹo"}, {"l": "A2-2", "jp": "たこあげ", "vi": "Thả diều"}, {"l": "A2-2", "jp": "コメント", "vi": "Nhận xét, bình luận"}, {"l": "A2-2", "jp": "チキン", "vi": "Thịt gà"}, {"l": "A2-2", "jp": "しょうかい(します)", "vi": "Giới thiệu"}, {"l": "A2-2", "jp": "じこしょうかい", "vi": "Giới thiệu bản thân"}, {"l": "A2-2", "jp": "とくい(な)", "vi": "Giỏi, thành thạo"}, {"l": "A2-2", "jp": "しあい", "vi": "Trận đấu"}, {"l": "A2-2", "jp": "えんげき", "vi": "Kịch"}, {"l": "A2-2", "jp": "あみもの", "vi": "Đan móc len"}, {"l": "A2-2", "jp": "ガーデニング", "vi": "Làm vườn"}, {"l": "A2-2", "jp": "サイクリング", "vi": "Đạp xe dạo"}, {"l": "A2-2", "jp": "フルーツ", "vi": "Trái cây, hoa quả"}, {"l": "A2-2", "jp": "フルーツケーキ", "vi": "Bánh trái cây"}, {"l": "A2-2", "jp": "チェス", "vi": "Cờ vua"}, {"l": "A2-2", "jp": "ざんぎょう", "vi": "Tăng ca, OT"}, {"l": "A2-2", "jp": "ぎゅうどん", "vi": "Cơm thịt bò kiểu Nhật"}, {"l": "A2-2", "jp": "いろいろ(な)", "vi": "Nhiều, đa dạng"}, {"l": "A2-3", "jp": "きせつ", "vi": "Mùa"}, {"l": "A2-3", "jp": "てんき", "vi": "Thời tiết"}, {"l": "A2-3", "jp": "はる", "vi": "Mùa xuân"}, {"l": "A2-3", "jp": "なつ", "vi": "Mùa hè"}, {"l": "A2-3", "jp": "あき", "vi": "Mùa thu"}, {"l": "A2-3", "jp": "ふゆ", "vi": "Mùa đông"}, {"l": "A2-3", "jp": "あつい", "vi": "Nóng"}, {"l": "A2-3", "jp": "むしあつい", "vi": "Nóng nồm, ẩm, oi bức"}, {"l": "A2-3", "jp": "さむい", "vi": "Lạnh"}, {"l": "A2-3", "jp": "すずしい", "vi": "Mát mẻ"}, {"l": "A2-3", "jp": "あたたかい", "vi": "Ấm áp"}, {"l": "A2-3", "jp": "あめ", "vi": "Mưa"}, {"l": "A2-3", "jp": "あめが ふります", "vi": "Mưa rơi"}, {"l": "A2-3", "jp": "うき", "vi": "Mùa mưa (nhiệt đới)"}, {"l": "A2-3", "jp": "かんき", "vi": "Mùa khô"}, {"l": "A2-3", "jp": "つゆ", "vi": "Mùa mưa đầu hè (Nhật Bản)"}, {"l": "A2-3", "jp": "ゆき", "vi": "Tuyết"}, {"l": "A2-3", "jp": "ゆきが ふります", "vi": "Tuyết rơi"}, {"l": "A2-3", "jp": "~ど", "vi": "... độ"}, {"l": "A2-3", "jp": "きおん", "vi": "Nhiệt độ không khí"}, {"l": "A2-3", "jp": "(お)しょうがつ", "vi": "Tết Dương Lịch"}, {"l": "A2-3", "jp": "はなが さきます", "vi": "Hoa nở"}, {"l": "A2-3", "jp": "(お)はなみ", "vi": "Ngắm hoa anh đào"}, {"l": "A2-3", "jp": "にゅうがくしき", "vi": "Lễ nhập học"}, {"l": "A2-3", "jp": "ひまわり", "vi": "Hoa hướng dương"}, {"l": "A2-3", "jp": "あじさい", "vi": "Hoa cẩm tú cầu"}, {"l": "A2-3", "jp": "たんぼ", "vi": "Đồng lúa"}, {"l": "A2-3", "jp": "すいか", "vi": "Dưa hấu"}, {"l": "A2-3", "jp": "ゆかた", "vi": "Bộ Yukata (Kimono mùa hè)"}, {"l": "A2-3", "jp": "もみじ", "vi": "Lá phong"}, {"l": "A2-3", "jp": "つきみ", "vi": "Trung thu, ngắm trăng"}, {"l": "A2-3", "jp": "ぶどう", "vi": "Nho"}, {"l": "A2-3", "jp": "スキー", "vi": "Trượt tuyết"}, {"l": "A2-3", "jp": "こたつ", "vi": "Bàn sưởi"}, {"l": "A2-3", "jp": "みかん", "vi": "Quả quýt"}, {"l": "A2-3", "jp": "なべりょうり", "vi": "Lẩu"}, {"l": "A2-3", "jp": "セーター", "vi": "Áo len"}, {"l": "A2-3", "jp": "うみ", "vi": "Biển"}, {"l": "A2-3", "jp": "やま", "vi": "Núi"}, {"l": "A2-3", "jp": "かわ", "vi": "Sông"}, {"l": "A2-3", "jp": "だんだん", "vi": "Dần dần"}, {"l": "A2-3", "jp": "にがて(な)", "vi": "Tệ, kém, không hợp..."}, {"l": "A2-3", "jp": "なります", "vi": "Trở nên, trở thành"}, {"l": "A2-3", "jp": "だいたい", "vi": "Đại khái"}, {"l": "A2-4", "jp": "はれ/はれます", "vi": "Trời đẹp, quang đãng"}, {"l": "A2-4", "jp": "くもり/くもります", "vi": "Âm u, nhiều mây"}, {"l": "A2-4", "jp": "あめが やみます", "vi": "Mưa tạnh"}, {"l": "A2-4", "jp": "ゆきが つもります", "vi": "Tuyết chất dày, chất đống"}, {"l": "A2-4", "jp": "かぜ", "vi": "Gió"}, {"l": "A2-4", "jp": "かぜが ふきます", "vi": "Gió thổi"}, {"l": "A2-4", "jp": "たいふう", "vi": "Bão"}, {"l": "A2-4", "jp": "ゆきだるま", "vi": "Người tuyết"}, {"l": "A2-4", "jp": "そら", "vi": "Bầu trời"}, {"l": "A2-4", "jp": "くも", "vi": "Mây"}, {"l": "A2-4", "jp": "つき", "vi": "Trăng"}, {"l": "A2-4", "jp": "ほし", "vi": "Sao"}, {"l": "A2-4", "jp": "ほしが でます", "vi": "Sao xuất hiện trên trời"}, {"l": "A2-4", "jp": "ごぜんちゅう", "vi": "Ban ngày"}, {"l": "A2-4", "jp": "いちにちじゅう", "vi": "Cả ngày"}, {"l": "A2-4", "jp": "いちねんじゅう", "vi": "Cả năm"}, {"l": "A2-4", "jp": "せかい", "vi": "Thế giới"}, {"l": "A2-4", "jp": "てんきよほう", "vi": "Dự báo thời tiết"}, {"l": "A2-4", "jp": "げんき(な)", "vi": "Khỏe mạnh"}, {"l": "A2-4", "jp": "きもちが いい", "vi": "Sảng khoái, dễ chịu"}, {"l": "A2-4", "jp": "つよい", "vi": "Mạnh"}, {"l": "A2-4", "jp": "よわい", "vi": "Yếu"}, {"l": "A2-4", "jp": "でかけます", "vi": "Ra ngoài"}, {"l": "A2-4", "jp": "おかげさまで", "vi": "Ơn trời"}, {"l": "A2-4", "jp": "(お)ひさしぶりです", "vi": "Đã lâu không gặp"}];
const rawKanji = [{"char": "秋", "hv": "Thu", "lesson": "L3", "lessonName": "Bài 3", "strokes": 9, "meaning": "Mùa thu", "kun": "あき、 とき", "on": "しゅう", "examples": [{"word": "秋", "reading": "あき", "vi": "Mùa thu"}, {"word": "秋分", "reading": "しゅうぶん", "vi": "Thu phân"}], "formula": "禾 (Lúa) ＋ 火 (Lửa)", "strokeGuide": "Trái trước phải sau: Viết bộ Hòa (禾 - 5 nét) bên trái trước, bộ Hỏa (火 - 4 nét) bên phải sau.", "mnemonic": "Bông lúa vàng ươm (禾) chín rộ bên ngọn lửa (火) sưởi ấm mùa thu hoạch."}, {"char": "冬", "hv": "Đông", "lesson": "L3", "lessonName": "Bài 3", "strokes": 5, "meaning": "Mùa đông", "kun": "ふゆ", "on": "とう", "examples": [{"word": "冬", "reading": "ふゆ", "vi": "Mùa đông"}, {"word": "春夏秋冬", "reading": "しゅんかしゅうとう", "vi": "Xuân hạ thu đông"}], "formula": "夂 (Đi chậm) ＋ 冫(Băng tuyết)", "strokeGuide": "Trên trước dưới sau: Viết bộ Truy (夂 - 3 nét) ở trên trước, hai nét chấm băng (冫) ở dưới cùng.", "mnemonic": "Mùa đông đường đóng băng trơn trượt (冫) nên phải bước đi chậm chạp kẻo ngã."}, {"char": "春", "hv": "Xuân", "lesson": "L3", "lessonName": "Bài 3", "strokes": 9, "meaning": "Mùa xuân", "kun": "はる", "on": "しゅん", "examples": [{"word": "春", "reading": "はる", "vi": "Mùa xuân"}, {"word": "青春", "reading": "せいしゅん", "vi": "Thanh xuân"}], "formula": "三 (Ba) ＋ 人 (Người) ＋ 日 (Mặt trời)", "strokeGuide": "Trên trước dưới sau: Viết 3 nét ngang ➔ nét phẩy & mác bao lấy bộ Nhật (日 - 4 nét) ở dưới.", "mnemonic": "Ba người (三人) cùng dạo chơi dưới ánh mặt trời (日) ấm áp của mùa xuân."}, {"char": "夏", "hv": "Hạ", "lesson": "L3", "lessonName": "Bài 3", "strokes": 10, "meaning": "Mùa hè", "kun": "なつ", "on": "か、 げ", "examples": [{"word": "夏", "reading": "なつ", "vi": "Mùa hè"}, {"word": "夏休み", "reading": "なつやすみ", "vi": "Nghỉ hè"}], "formula": "頁 (Đầu) ＋ 夂 (Chân đi)", "strokeGuide": "Trên trước dưới sau: Nét ngang đầu tiên ➔ chữ Tự (目) ở giữa ➔ bộ Truy (夂) ở dưới cùng.", "mnemonic": "Mùa hè nóng bức, người ta đội mũ che đầu và rảo bước (夂) đi biển."}, {"char": "今", "hv": "Kim", "lesson": "L3", "lessonName": "Bài 3", "strokes": 4, "meaning": "Bây giờ, hiện tại", "kun": "いま", "on": "こん、 きん", "examples": [{"word": "今", "reading": "いま", "vi": "Bây giờ"}, {"word": "今日", "reading": "きょう", "vi": "Hôm nay"}, {"word": "今月", "reading": "こんげつ", "vi": "Tháng này"}], "formula": "𠆢 (Mái) ＋ 一 ＋ 乛", "strokeGuide": "Phẩy trước mác sau tạo mái 𠆢 ➔ nét ngang ngắn ➔ nét ngang gập ở dưới cùng.", "mnemonic": "Chiếc đồng hồ cát đang đọng lại thời khắc quý giá ngay bây giờ."}, {"char": "花", "hv": "Hoa", "lesson": "L3", "lessonName": "Bài 3", "strokes": 7, "meaning": "Bông hoa", "kun": "はな", "on": "か", "examples": [{"word": "花", "reading": "はな", "vi": "Hoa"}, {"word": "お花見", "reading": "おはなみ", "vi": "Ngắm hoa anh đào"}], "formula": "艹 (Cỏ) ＋ 化 (Biến hóa)", "strokeGuide": "Trên trước dưới sau: Viết bộ Thảo (艹 - 3 nét) ở trên trước, chữ Hóa (化 - 4 nét) ở dưới sau.", "mnemonic": "Cây cỏ (艹) biến hóa (化) kỳ diệu nở thành những bông hoa rực rỡ."}, {"char": "海", "hv": "Hải", "lesson": "L3", "lessonName": "Bài 3", "strokes": 9, "meaning": "Biển", "kun": "うみ", "on": "かい", "examples": [{"word": "海", "reading": "うみ", "vi": "Biển"}], "formula": "氵(Nước) ＋ 毎 (Mỗi)", "strokeGuide": "Trái trước phải sau: 3 chấm thủy (氵) bên trái trước, chữ Mỗi (毎 - 6 nét) bên phải sau.", "mnemonic": "Nước (氵) từ mỗi (毎) con sông ngày đêm đổ ra biển cả."}, {"char": "山", "hv": "Sơn", "lesson": "L3", "lessonName": "Bài 3", "strokes": 3, "meaning": "Núi", "kun": "やま", "on": "さん", "examples": [{"word": "山", "reading": "やま", "vi": "Núi"}], "formula": "Chữ tượng hình 3 đỉnh núi", "strokeGuide": "Giữa trước hai bên sau: Viết nét sổ thẳng cao ở giữa trước ➔ nét sổ gập trái-dưới ➔ nét sổ phải.", "mnemonic": "Vẽ lại hình ảnh 3 ngọn núi cao chót vót đứng cạnh nhau."}, {"char": "川", "hv": "Xuyên", "lesson": "L3", "lessonName": "Bài 3", "strokes": 3, "meaning": "Sông", "kun": "かわ", "on": "せん", "examples": [{"word": "川", "reading": "かわ", "vi": "Con sông"}], "formula": "Chữ tượng hình 3 dòng chảy", "strokeGuide": "Trái sang phải: Nét phẩy cong bên trái ➔ nét sổ ngắn ở giữa ➔ nét sổ dài bên phải.", "mnemonic": "Hình vẽ 3 dòng nước chảy xiết song song uốn lượn thành sông."}, {"char": "私", "hv": "Tư", "lesson": "L1", "lessonName": "Bài 1", "strokes": 7, "meaning": "Tôi, riêng tư", "kun": "わたし", "on": "し", "examples": [{"word": "私", "reading": "わたし", "vi": "Tôi"}], "formula": "禾 (Lúa) ＋ 厶 (Riêng tư)", "strokeGuide": "Trái trước phải sau: Bộ Hòa (禾 - 5 nét) bên trái trước, bộ Khư (厶 - 2 nét) bên phải sau.", "mnemonic": "Bông lúa (禾) là tài sản riêng (厶) của chính Tôi."}, {"char": "父", "hv": "Phụ", "lesson": "L1", "lessonName": "Bài 1", "strokes": 4, "meaning": "Bố, cha", "kun": "ちち、 とう", "on": "ふ", "examples": [{"word": "父", "reading": "ちち", "vi": "Bố mình"}, {"word": "お父さん", "reading": "おとうさん", "vi": "Bố người khác"}], "formula": "八 ＋ 乂", "strokeGuide": "Trên trước dưới sau, Phẩy trước mác sau: Hai nét chấm hai bên trên ➔ nét phẩy ➔ nét mác giao nhau.", "mnemonic": "Hình ảnh người cha uy nghiêm trụ cột của gia đình."}, {"char": "母", "hv": "Mẫu", "lesson": "L1", "lessonName": "Bài 1", "strokes": 5, "meaning": "Mẹ", "kun": "はは、 かあ", "on": "ぼ", "examples": [{"word": "母", "reading": "はは", "vi": "Mẹ mình"}, {"word": "お母さん", "reading": "おかあさん", "vi": "Mẹ người khác"}], "formula": "Chữ tượng hình", "mnemonic": "Người mẹ ôm con và cho con bú (hai dấu chấm là bầu sữa mẹ).", "strokeGuide": "Khung ngoài trước ➔ chấm trên ➔ nét ngang cắt giữa ➔ chấm dưới."}, {"char": "子", "hv": "Tử", "lesson": "L1", "lessonName": "Bài 1", "strokes": 3, "meaning": "Con cái, trẻ em", "kun": "こ", "on": "し、 す", "examples": [{"word": "子ども", "reading": "こども", "vi": "Trẻ con, con cái"}], "formula": "了 ＋ 一", "strokeGuide": "Nét ngang gập trên (1) ➔ nét cong móc dọc (2) ➔ nét ngang dài cắt qua cuối cùng (3).", "mnemonic": "Em bé quấn tã đang giang rộng hai cánh tay."}, {"char": "男", "hv": "Nam", "lesson": "L1", "lessonName": "Bài 1", "strokes": 7, "meaning": "Đàn ông, nam giới", "kun": "おとこ", "on": "だん、 なん", "examples": [{"word": "男", "reading": "おとこ", "vi": "Đàn ông"}, {"word": "男の人", "reading": "おとこのひと", "vi": "Người đàn ông"}], "formula": "田 (Ruộng) ＋ 力 (Sức lực)", "strokeGuide": "Trên trước dưới sau: Viết bộ Điền (田 - 5 nét) ở trên trước, bộ Lực (力 - 2 nét) ở dưới sau.", "mnemonic": "Người bỏ sức lực (力) làm việc ngoài đồng ruộng (田) là người Đàn ông."}, {"char": "女", "hv": "Nữ", "lesson": "L1", "lessonName": "Bài 1", "strokes": 3, "meaning": "Phụ nữ, nữ giới", "kun": "おんな", "on": "じょ", "examples": [{"word": "女", "reading": "おんな", "vi": "Phụ nữ"}, {"word": "女の人", "reading": "おんなのひと", "vi": "Người phụ nữ"}], "formula": "Chữ tượng hình", "strokeGuide": "Nét phẩy gập (く) trước ➔ nét phẩy cong (丿) ➔ nét ngang dài (一) trên cùng khóa lại.", "mnemonic": "Hình dáng người phụ nữ ngồi bắt chéo chân duyên dáng."}, {"char": "人", "hv": "Nhân", "lesson": "L1", "lessonName": "Bài 1", "strokes": 2, "meaning": "Con người", "kun": "ひと", "on": "じん、 にん", "examples": [{"word": "人", "reading": "ひと", "vi": "Người"}, {"word": "何人", "reading": "なんにん", "vi": "Mấy người"}, {"word": "日本人", "reading": "にほんじん", "vi": "Người Nhật"}], "formula": "丿 ＋ 乀", "strokeGuide": "Phẩy trước mác sau: Nét phẩy dài bên trái (1) ➔ nét mác tựa vào bên phải (2).", "mnemonic": "Hai con người nương tựa vào nhau mà sống."}, {"char": "国", "hv": "Quốc", "lesson": "L2", "lessonName": "Bài 2", "strokes": 8, "meaning": "Đất nước", "kun": "くに", "on": "こく", "examples": [{"word": "国", "reading": "くに", "vi": "Đất nước"}, {"word": "外国", "reading": "がいこく", "vi": "Nước ngoài"}], "formula": "囗 (Biên giới) ＋ 玉 (Ngọc)", "strokeGuide": "Vào nhà trước đóng cửa sau: Viết 2 nét khung ngoài ➔ viết chữ Ngọc (玉 - 5 nét) ở trong ➔ nét ngang đáy đóng lại cuối cùng.", "mnemonic": "Biên giới bao quanh (囗) bảo vệ viên ngọc quý (玉) của Đất nước."}, {"char": "外", "hv": "Ngoại", "lesson": "L2", "lessonName": "Bài 2", "strokes": 5, "meaning": "Bên ngoài", "kun": "そと", "on": "がい", "examples": [{"word": "外", "reading": "そと", "vi": "Bên ngoài"}, {"word": "外国", "reading": "がいこく", "vi": "Nước ngoài"}], "formula": "夕 (Tối) ＋ 卜 (Bói)", "strokeGuide": "Trái trước phải sau: Bộ Tịch (夕 - 3 nét) bên trái trước, bộ Bốc (卜 - 2 nét) bên phải sau.", "mnemonic": "Buổi tối (夕) đi ra bên ngoài xem bói (卜)."}, {"char": "語", "hv": "Ngữ", "lesson": "L2", "lessonName": "Bài 2", "strokes": 14, "meaning": "Ngôn ngữ, tiếng", "kun": "かた-る", "on": "ご", "examples": [{"word": "日本語", "reading": "にほんご", "vi": "Tiếng Nhật"}, {"word": "英語", "reading": "えいご", "vi": "Tiếng Anh"}, {"word": "中国語", "reading": "ちゅうごくご", "vi": "Tiếng Trung"}], "formula": "言 (Lời nói) ＋ 五 (Năm) ＋ 口 (Miệng)", "strokeGuide": "Trái trước phải sau: Bộ Ngôn (言 - 7 nét) bên trái ➔ chữ Ngũ (五 - 4 nét) trên ➔ bộ Khẩu (口 - 3 nét) dưới.", "mnemonic": "Lời nói (言) giao tiếp qua năm cái miệng (五口) thành Ngôn ngữ."}, {"char": "本", "hv": "Bản", "lesson": "L2", "lessonName": "Bài 2", "strokes": 5, "meaning": "Sách, gốc rễ", "kun": "もと", "on": "ほん", "examples": [{"word": "本", "reading": "ほん", "vi": "Quyển sách"}, {"word": "日本", "reading": "にほん", "vi": "Nhật Bản"}], "formula": "木 (Cây) ＋ 一 (Gốc)", "strokeGuide": "Viết chữ Mộc (木 - 4 nét: ngang, sổ, phẩy, mác) trước ➔ gạch ngang nhỏ ở gốc cuối cùng.", "mnemonic": "Gỗ từ gốc cây (木) đem làm giấy đóng thành Sách (本)."}, {"char": "読", "hv": "Độc", "lesson": "L2", "lessonName": "Bài 2", "strokes": 14, "meaning": "Đọc sách", "kun": "よ-む", "on": "どく", "examples": [{"word": "読みます", "reading": "よみます", "vi": "Đọc"}, {"word": "読書", "reading": "どくしょ", "vi": "Việc đọc sách"}], "formula": "言 (Lời nói) ＋ 売 (Bán)", "strokeGuide": "Trái trước phải sau: Bộ Ngôn (言 - 7 nét) bên trái ➔ chữ Mại (売 - 7 nét) bên phải.", "mnemonic": "Cất tiếng (言) đọc to chữ nghĩa."}, {"char": "好", "hv": "Hảo", "lesson": "L2", "lessonName": "Bài 2", "strokes": 6, "meaning": "Thích, yêu thích", "kun": "す-き", "on": "こう", "examples": [{"word": "好き", "reading": "すき", "vi": "Thích"}], "formula": "女 (Phụ nữ) ＋ 子 (Con)", "strokeGuide": "Trái trước phải sau: Bộ Nữ (女 - 3 nét) bên trái trước, bộ Tử (子 - 3 nét) bên phải sau.", "mnemonic": "Mẹ (女) ôm con (子) là điều tốt đẹp đáng yêu thích."}, {"char": "何", "hv": "Hà", "lesson": "L2", "lessonName": "Bài 2", "strokes": 7, "meaning": "Cái gì", "kun": "なに、 なん", "on": "か", "examples": [{"word": "何", "reading": "なに", "vi": "Cái gì"}, {"word": "何人", "reading": "なんにん", "vi": "Mấy người"}], "formula": "亻(Người) ＋ 可", "strokeGuide": "Trái trước phải sau: Bộ Nhân đứng (亻 - 2 nét) trước ➔ chữ Khả (可 - 5 nét) bên phải.", "mnemonic": "Người (亻) đang mang vác cái gì trên vai?"}, {"char": "天", "hv": "Thiên", "lesson": "L4", "lessonName": "Bài 4", "strokes": 4, "meaning": "Trời, bầu trời", "kun": "あめ", "on": "てん", "examples": [{"word": "天気", "reading": "てんき", "vi": "Thời tiết"}], "formula": "一 ＋ 大 (Đại)", "strokeGuide": "Nét ngang trên cùng ➔ nét ngang thứ hai ngắn hơn ➔ nét phẩy ➔ nét mác.", "mnemonic": "Phía trên con người to lớn (大) là Bầu trời."}, {"char": "気", "hv": "Khí", "lesson": "L4", "lessonName": "Bài 4", "strokes": 6, "meaning": "Khí, tinh thần", "kun": "き", "on": "き", "examples": [{"word": "天気", "reading": "てんき", "vi": "Thời tiết"}, {"word": "元気", "reading": "げんき", "vi": "Khỏe mạnh"}], "formula": "气 ＋ 〆", "strokeGuide": "Ngoài trước trong sau: Viết 4 nét bộ Khí (气) ở trên và bao ngoài trước ➔ chữ 〆 (phẩy, chấm) ở trong sau.", "mnemonic": "Hơi nước và năng lượng lan tỏa trong không trung."}, {"char": "晴", "hv": "Tình", "lesson": "L4", "lessonName": "Bài 4", "strokes": 12, "meaning": "Trời nắng, quang đãng", "kun": "は-れ", "on": "せい", "examples": [{"word": "晴れ", "reading": "はれ", "vi": "Trời nắng đẹp"}], "formula": "日 (Mặt trời) ＋ 青 (Xanh)", "strokeGuide": "Trái trước phải sau: Bộ Nhật (日 - 4 nét) bên trái ➔ chữ Thanh (青 - 8 nét) bên phải.", "mnemonic": "Mặt trời (日) tỏa nắng trên nền trời xanh (青)."}, {"char": "雨", "hv": "Vũ", "lesson": "L4", "lessonName": "Bài 4", "strokes": 8, "meaning": "Cơn mưa", "kun": "あめ", "on": "う", "examples": [{"word": "雨", "reading": "あめ", "vi": "Mưa"}], "formula": "Chữ tượng hình hạt mưa", "strokeGuide": "Nét ngang trên ➔ khung bao ➔ nét sổ giữa ➔ 4 dấu chấm hạt mưa hai bên.", "mnemonic": "Bốn hạt mưa rơi qua khung cửa sổ."}, {"char": "雪", "hv": "Tuyết", "lesson": "L4", "lessonName": "Bài 4", "strokes": 11, "meaning": "Tuyết", "kun": "ゆき", "on": "せつ", "examples": [{"word": "雪", "reading": "ゆき", "vi": "Tuyết"}], "formula": "雨 (Mưa) ＋ 彐 (Chổi)", "strokeGuide": "Trên trước dưới sau: Bộ Vũ (雨 - 8 nét) ở trên ➔ bộ Kệ (彐 - 3 nét) ở dưới.", "mnemonic": "Mưa (雨) đông cứng thành tuyết phải dùng chổi (彐) quét."}, {"char": "雲", "hv": "Vân", "lesson": "L4", "lessonName": "Bài 4", "strokes": 12, "meaning": "Đám mây", "kun": "くも", "on": "うん", "examples": [{"word": "雲", "reading": "くも", "vi": "Mây"}], "formula": "雨 (Mưa) ＋ 云 (Cuộn)", "strokeGuide": "Trên trước dưới sau: Bộ Vũ (雨 - 8 nét) ở trên ➔ chữ Vân (云 - 4 nét) ở dưới.", "mnemonic": "Hơi mưa (雨) cuộn tròn (云) thành đám mây."}, {"char": "風", "hv": "Phong", "lesson": "L4", "lessonName": "Bài 4", "strokes": 9, "meaning": "Cơn gió", "kun": "かぜ", "on": "ふう", "examples": [{"word": "風", "reading": "かぜ", "vi": "Gió"}], "formula": "几 (Khung) ＋ 虫 (Côn trùng)", "strokeGuide": "Ngoài trước trong sau: Viết khung bộ Kỷ (几 - 2 nét) bao ngoài trước ➔ nét phẩy + bộ Trùng (虫) bên trong.", "mnemonic": "Gió thổi lồng lộng cuốn côn trùng bay đi."}, {"char": "空", "hv": "Không", "lesson": "L4", "lessonName": "Bài 4", "strokes": 8, "meaning": "Bầu trời", "kun": "そら", "on": "くう", "examples": [{"word": "空", "reading": "そら", "vi": "Bầu trời"}, {"word": "空港", "reading": "くうこう", "vi": "Sân bay"}], "formula": "穴 (Hang) ＋ 工 (Thợ)", "strokeGuide": "Trên trước dưới sau: Bộ Huyệt (穴 - 5 nét) ở trên ➔ bộ Công (工 - 3 nét) ở dưới.", "mnemonic": "Ngước nhìn lên khoảng không bầu trời rộng lớn."}];
const quizData = [{"id": 1, "category": "Trợ từ", "lesson": "A2-1", "q": "東京 [____] すんでいます。", "options": ["に", "で", "を", "へ"], "correct": 0, "explain": "Động từ 「すんでいます」 (sinh sống) biểu thị nơi cư trú cố định, luôn đi với trợ từ 「に」."}, {"id": 2, "category": "Trợ từ", "lesson": "A2-1", "q": "父は 病院 [____] 働いています。", "options": ["で", "に", "を", "が"], "correct": 0, "explain": "「はたらいています」 là hành động làm việc diễn ra tại một địa điểm, đi với trợ từ 「で」 (Phân biệt với nơi cư trú: に すんでいます)."}, {"id": 3, "category": "Ngữ pháp", "lesson": "A2-1", "q": "田中さんの 奥さんを 知っていますか。ー いいえ、[____]。", "options": ["知りません", "知っていません", "知りませんでした", "知らなくなります"], "correct": 0, "explain": "Dạng phủ định của 「知っています」 đặc biệt luôn là 「知りません」 (KHÔNG dùng 「知っていません」)."}, {"id": 4, "category": "Ngữ pháp", "lesson": "A2-1", "q": "姉は まだ [____]。", "options": ["結婚していません", "結婚しませんでした", "結婚しません", "結婚しています"], "correct": 0, "explain": "Chưa kết hôn (đang độc thân) diễn tả trạng thái hiện tại chưa xảy ra, chuẩn ngữ pháp là 「けっこんしていません」."}, {"id": 5, "category": "Từ vựng / Xưng hô", "lesson": "A2-1", "q": "[____] は おいくつですか。ー 50さいです。", "options": ["お父さん", "父", "おっと", "そふ"], "correct": 0, "explain": "Khi hỏi hoặc nói về bố của người khác một cách lịch sự, phải dùng 「お父さん」. Từ 「父 (ちち)」 chỉ dùng để gọi bố của chính mình với người ngoài."}, {"id": 6, "category": "Từ vựng / Xưng hô", "lesson": "A2-1", "q": "私の [____] は 料理が 上手です。", "options": ["母", "お母さん", "妻さん", "娘さん"], "correct": 0, "explain": "Khi nói về mẹ của chính mình với người ngoài, dùng cách xưng hô khiêm nhường là 「母 (はは)」."}, {"id": 7, "category": "Ngữ pháp", "lesson": "A2-2", "q": "私の 趣味は 料理を [____] ことです。", "options": ["つくる", "つくります", "つくって", "つくり"], "correct": 0, "explain": "Cấu trúc nói về sở thích: 「[V thể từ điển (RU)] + こと です」. 「つくります」 nhóm 1 chuyển thành thể từ điển là 「つくる」."}, {"id": 8, "category": "Ngữ pháp", "lesson": "A2-2", "q": "弟の 趣味は 切手を [____] ことです。", "options": ["あつめる", "あつまる", "あつめます", "あつめて"], "correct": 0, "explain": "Sưu tập tem là 「切手を あつめる」. Động từ nhóm 2 「あつめます」 bỏ -masu thêm -ru thành 「あつめる」."}, {"id": 9, "category": "Trợ từ", "lesson": "A2-2", "q": "私は 水泳 [____] 得意です。", "options": ["が", "を", "に", "で"], "correct": 0, "explain": "Diễn tả năng khiếu, sở trường / sở đoản (得意、苦手、上手、下手) luôn đi kèm trợ từ 「が」."}, {"id": 10, "category": "Ngữ pháp", "lesson": "A2-2", "q": "[____] とき、よく 映画を 見ます。", "options": ["暇な", "暇の", "暇で", "暇"], "correct": 0, "explain": "「ひま」 là tính từ đuôi -na, khi đứng trước danh từ 「とき」 (khi/lúc) phải giữ nguyên 「な」 ➔ 「暇な とき」 (Khi rảnh rỗi)."}, {"id": 11, "category": "Ngữ pháp", "lesson": "A2-3", "q": "秋になると、だんだん [____] なります。", "options": ["すずしく", "すずしい", "すずしに", "すずしくて"], "correct": 0, "explain": "Tính từ đuôi -i đi với động từ 「なります」 thì bỏ 「い」 thêm 「く」 ➔ 「すずしく なります」 (trở nên mát mẻ)."}, {"id": 12, "category": "Ngữ pháp", "lesson": "A2-3", "q": "春になって、庭の 花が [____] なりました。", "options": ["きれいに", "きれいく", "きれいな", "きれいで"], "correct": 0, "explain": "Tính từ đuôi -na đi với động từ 「なります」 thì bỏ 「な」 thêm 「に」 ➔ 「きれいに なります」 (trở nên xinh đẹp)."}, {"id": 13, "category": "Ngữ pháp", "lesson": "A2-3", "q": "来月、二十歳 (20 tuổi) [____] なります。", "options": ["に", "で", "を", "が"], "correct": 0, "explain": "Danh từ đi với động từ biến đổi trạng thái 「なります」 luôn kết hợp với trợ từ 「に」 ➔ 「N に なります」."}, {"id": 14, "category": "So sánh", "lesson": "A2-3", "q": "ベトナムは 日本 [____] あついです。", "options": ["より", "ほど", "のほうが", "から"], "correct": 0, "explain": "Cấu trúc so sánh hơn: 「A は B より [Tính từ] です」 (A thì... hơn B). Ở đây: Việt Nam nóng hơn Nhật Bản."}, {"id": 15, "category": "So sánh", "lesson": "A2-3", "q": "春と 秋と [____] が 好きですか。", "options": ["どちら", "どれ", "なに", "だれ"], "correct": 0, "explain": "Khi hỏi lựa chọn giữa 2 đối tượng, dùng từ để hỏi 「どちら」 (hoặc văn nói 「どっち」). Dùng 「どれ」 khi có từ 3 đối tượng trở lên."}, {"id": 16, "category": "So sánh", "lesson": "A2-3", "q": "1年の [____] で、夏が いちばん 暑いです。", "options": ["なか", "まえ", "あと", "うえ"], "correct": 0, "explain": "Cấu trúc so sánh nhất trong một phạm vi: 「[Phạm vi] の なかで、～が いちばん [Tính từ]」 (Trong số 1 năm, mùa hè nóng nhất)."}, {"id": 17, "category": "Trợ từ", "lesson": "A2-4", "q": "外は 強い 風 [____] ふいています。", "options": ["が", "を", "に", "で"], "correct": 0, "explain": "Hiện tượng tự nhiên khách quan (gió thổi, mưa rơi, tuyết rơi) luôn đi với trợ từ 「が」 ➔ 「風が ふきます」."}, {"id": 18, "category": "Từ vựng", "lesson": "A2-4", "q": "やっと 雨が [____] ましたね。出かけましょう。", "options": ["やみ", "ふり", "つもり", "おち"], "correct": 0, "explain": "Mưa tạnh là 「雨が やみます」. 「ふります」 là mưa rơi, 「つもります」 là tuyết chất đống."}, {"id": 19, "category": "Từ vựng", "lesson": "A2-4", "q": "冬の 北海道は 雪が たくさん [____]。", "options": ["つもります", "やみます", "なります", "ふきます"], "correct": 0, "explain": "Tuyết tích tụ, chất thành đống dày trên mặt đất dùng động từ 「雪が つもります」."}, {"id": 20, "category": "Giao tiếp xã giao", "lesson": "A2-4", "q": "お久しぶりです。お元気ですか。ー ええ、[____] 元気です。", "options": ["おかげさまで", "どういたしまして", "ごちそうさまでした", "こちらこそ"], "correct": 0, "explain": "Lời đáp lễ phép khi được người khác hỏi thăm sức khỏe: 「おかげさまで、元気です」 (Ơn trời / Nhờ phúc của bạn tôi vẫn khỏe)."}, {"id": 21, "category": "Thời gian", "lesson": "A2-4", "q": "昨日は 日曜日でしたから、[____] 家で ゲームを しました。", "options": ["一日中 (いちにちじゅう)", "午前中 (ごぜんちゅう)", "一年中 (いちねんじゅう)", "今月中 (こんげつちゅう)"], "correct": 0, "explain": "「いちにちじゅう」 (一日中) nghĩa là suốt cả ngày. 「ごぜんちゅう」 là suốt buổi sáng."}, {"id": 22, "category": "Kanji", "lesson": "A2-1", "q": "Chữ Hán 「私」 có âm Hán Việt là gì?", "options": ["Tư", "Nhân", "Tự", "Huynh"], "correct": 0, "explain": "Chữ 私 có âm Hán Việt là 「Tư」 (riêng tư, tôi), cách đọc Kunyomi là わたし."}, {"id": 23, "category": "Kanji", "lesson": "A2-2", "q": "Từ 「読みます」 có cách đọc Hiragana là gì?", "options": ["よみます", "のみます", "やすみます", "かきます"], "correct": 0, "explain": "Chữ 読 (Độc) có cách đọc Kunyomi là 「よ-む」 ➔ 「よみます」 (đọc sách)."}, {"id": 24, "category": "Kanji", "lesson": "A2-2", "q": "Từ 「がいこく」 (nước ngoài) được viết bằng chữ Hán nào?", "options": ["外国", "国外", "外語", "本国"], "correct": 0, "explain": "「がいこく」 ghép từ chữ 外 (Ngoại - ngoài) và chữ 国 (Quốc - đất nước) ➔ 外国."}, {"id": 25, "category": "Kanji", "lesson": "A2-3", "q": "Chữ Hán 「秋」 có cách đọc Hiragana và ý nghĩa là gì?", "options": ["あき - Mùa thu", "はる - Mùa xuân", "なつ - Mùa hè", "ふゆ - Mùa đông"], "correct": 0, "explain": "Chữ 秋 (Thu) đọc là 「あき」, nghĩa là Mùa thu (Chiết tự: Cây lúa 禾 chín đỏ như ngọn lửa 火 vào mùa thu)."}, {"id": 26, "category": "Kanji", "lesson": "A2-4", "q": "Các chữ Hán 「雪」 (Tuyết) và 「雲」 (Vân) đều có bộ thủ nào ở trên cùng?", "options": ["Bộ Vũ 雨 (Mưa)", "Bộ Thiên 天 (Trời)", "Bộ Phong 風 (Gió)", "Bộ Không 空 (Bầu trời)"], "correct": 0, "explain": "Cả 2 chữ 雪 và 雲 đều có bộ thủ là chữ 雨 (Vũ - mưa) ở phần trên, tượng trưng cho các hiện tượng khí tượng."}, {"id": 27, "category": "Kanji", "lesson": "A2-4", "q": "Chữ Hán 「天気」 (Thiên Khí) có cách đọc và nghĩa là gì?", "options": ["てんき - Thời tiết", "でんき - Điện năng", "げんき - Khỏe mạnh", "くうき - Không khí"], "correct": 0, "explain": "「てんき」 ghép từ 天 (Thiên) + 気 (Khí) mang nghĩa Thời tiết."}, {"id": 28, "category": "Kanji", "lesson": "A2-2", "q": "Chữ 「何」 trong 「何時」 (Mấy giờ) được đọc là gì?", "options": ["なん (なんじ)", "なに (なにじ)", "いつ (いつじ)", "どこ (どこじ)"], "correct": 0, "explain": "Trước phụ âm dòng 'd' (じ), chữ 何 được đọc biến âm thành 「なん」 ➔ 「なんじ」 (Mấy giờ)."}, {"id": 29, "category": "Văn hóa", "lesson": "A2-3", "q": "Hoạt động ngắm lá phong mùa thu ở Nhật Bản được gọi là gì?", "options": ["もみじ", "おはなみ", "つきみ", "おしょうがつ"], "correct": 0, "explain": "Lá phong đỏ mùa thu là 「もみじ」 (hoặc 「もみじがり」). 「おはなみ」 là ngắm hoa anh đào mùa xuân."}, {"id": 30, "category": "Văn hóa", "lesson": "A2-3", "q": "Chiếc bàn sưởi ấm truyền thống phủ chăn của Nhật vào mùa đông gọi là gì?", "options": ["こたつ", "なべ", "セーター", "ゆかた"], "correct": 0, "explain": "Chiếc bàn có gắn hệ thống sưởi dưới gầm và phủ chăn ấm gọi là 「こたつ」 (bàn sưởi)."}];

// Trạng thái ứng dụng
let currentVocabFilter = 'ALL';
let currentKanjiFilter = 'ALL';
let isMeaningHidden = false;
let userAnswers = {};

// Switch Main Tabs
function switchMainTab(tabId) {
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));

    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Render Vocab
function renderVocab(list) {
    const container = document.getElementById('vocabContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy từ vựng phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map((item, idx) => `
        <div class="vocab-card">
            <div class="vocab-top">
                <span class="vocab-badge">${item.l}</span>
                <button class="sound-btn" onclick="speakText('${item.jp.replace(/'/g, "\'")}')" title="Nghe phát âm">🔊</button>
            </div>
            <div class="vocab-jp jp-text">${item.jp}</div>
            <div class="vocab-vi ${isMeaningHidden ? 'hidden-meaning' : ''}" title="${isMeaningHidden ? 'Bấm để xem' : ''}" onclick="this.classList.toggle('hidden-meaning')">
                ${item.vi}
            </div>
        </div>
    `).join('');
}

function filterVocab(lesson, btn) {
    currentVocabFilter = lesson;
    if (btn) {
        btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    applyVocabFilter();
}

function handleVocabSearch() {
    applyVocabFilter();
}

let currentFilteredVocab = [...rawVocab];

function applyVocabFilter() {
    const keyword = document.getElementById('vocabSearchInput').value.trim().toLowerCase();
    let filtered = rawVocab;
    if (currentVocabFilter !== 'ALL') {
        filtered = filtered.filter(v => v.l === currentVocabFilter);
    }
    if (keyword) {
        filtered = filtered.filter(v => 
            v.jp.toLowerCase().includes(keyword) || 
            v.vi.toLowerCase().includes(keyword)
        );
    }
    currentFilteredVocab = filtered;
    const countEl = document.getElementById('quizletVocabCount');
    if (countEl) countEl.innerText = filtered.length;

    renderVocab(filtered);
}

function cleanJpTermForQuizlet(str) {
    if (!str) return "";
    let s = str;
    if (s === "まいつき、まいげつ") return "まいつき";
    if (s === "まいとし、まいねん") return "まいとし";
    s = s.replace(/[~～…\.]/g, "");
    s = s.replace(/めの[nN]/g, "め");
    s = s.replace(/^[nN]が/g, "");
    s = s.replace(/^[nNpPvV][をにへとがで]/g, "");
    s = s.replace(/^[pPnN]に/g, "");
    s = s.replace(/[vV]ましょう/g, "ましょう");
    s = s.replace(/[vV]ました/g, "");
    s = s.replace(/[vV]$/g, "");
    s = s.replace(/てください$/g, "");
    s = s.replace(/\([^)]*を\)/g, "").replace(/（[^）]*を）/g, "");
    s = s.replace(/\(お\)/g, "お").replace(/（お）/g, "お");
    s = s.replace(/\(します\)/g, "します").replace(/（します）/g, "します");
    s = s.replace(/\(さん\)/g, "").replace(/（さん）/g, "");
    s = s.replace(/\(な\)/g, "").replace(/（な）/g, "");
    s = s.replace(/[\(\)（）]/g, "");
    if (s.includes("/") || s.includes("／")) {
        s = s.split(/[\/／]/)[0];
    }
    s = s.replace(/[NPVnvp]/g, "");
    s = s.replace(/[。、,，\?？!！]/g, "");
    s = s.replace(/[\s　]+/g, "");
    return s.trim();
}

function formatQuizletVocabLine(item) {
    const term = cleanJpTermForQuizlet(item.kana || item.kanji || item.jp);
    let def = item.vi;
    if (item.jp && item.jp.includes('/')) {
        const alt = item.jp.split('/')[1].trim();
        def = `${item.vi} (hoặc ${alt})`;
    }
    return `${term}\t${def}`;
}

function copyVocabQuizletFormat() {
    if (!currentFilteredVocab || currentFilteredVocab.length === 0) {
        showToast("Không có từ vựng nào để sao chép!");
        return;
    }
    const text = currentFilteredVocab.map(formatQuizletVocabLine).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy ${currentFilteredVocab.length} từ vựng chuẩn Quizlet (Gõ mượt, không khoảng trắng, không ~)!`);
    }).catch(() => {
        fallbackCopyText(text, currentFilteredVocab.length);
    });
}

function copyFull121QuizletFormat() {
    const text = rawVocab.map(formatQuizletVocabLine).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        showToast(`✅ Đã copy toàn bộ 121 từ vựng (Bài 1 - 4) chuẩn Quizlet (Gõ mượt, không khoảng trắng, không ~)!`);
    }).catch(() => {
        fallbackCopyText(text, 121);
    });
}

function fallbackCopyText(text, count) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast(`✅ Đã copy ${count} từ vựng chuẩn Quizlet (Gõ mượt, không khoảng trắng, không ~)!`);
}

function showToast(msg) {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => { toast.style.display = 'none'; }, 2800);
}

function toggleHideMeaning() {
    isMeaningHidden = !isMeaningHidden;
    const btn = document.getElementById('hideMeaningBtn');
    if (isMeaningHidden) {
        btn.classList.add('active');
        btn.innerHTML = '👁️ Đang ẩn nghĩa (Chạm vào thẻ để xem)';
    } else {
        btn.classList.remove('active');
        btn.innerHTML = '👁️ Ẩn nghĩa tiếng Việt (Tự dò)';
    }
    document.querySelectorAll('.vocab-vi').forEach(el => {
        if (isMeaningHidden) el.classList.add('hidden-meaning');
        else el.classList.remove('hidden-meaning');
    });
}

// Render Kanji
function renderKanji(list) {
    const container = document.getElementById('kanjiContainer');
    if (!list || list.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--gray-500);">Không tìm thấy chữ Hán phù hợp.</div>';
        return;
    }

    container.innerHTML = list.map(item => `
        <div class="kanji-card">
            <div class="kanji-header">
                <div class="kanji-char-box jp-text">${item.char}</div>
                <div class="kanji-meta">
                    <div class="kanji-hv">${item.hv}</div>
                    <div class="kanji-meaning">${item.meaning}</div>
                    <div class="kanji-sub-row">
                        <span class="kanji-tag">${item.lessonName}</span>
                        <span class="kanji-tag">${item.strokes} nét</span>
                    </div>
                </div>
            </div>

            <div class="kanji-detail-box">
                <div class="kanji-reading-item">
                    <strong>KUN:</strong> <span class="jp-text">${item.kun || '—'}</span>
                </div>
                <div class="kanji-reading-item">
                    <strong>ON:</strong> <span class="jp-text">${item.on || '—'}</span>
                </div>
                <div class="kanji-reading-item">
                    <strong>Chiết tự:</strong> <span>${item.formula}</span>
                </div>
            </div>

            <div class="kanji-mnemonic">
                💡 <strong>Mẹo nhớ:</strong> ${item.mnemonic}
            </div>

            <ul class="kanji-words">
                ${(item.examples || []).map(ex => `
                    <li class="kanji-word-item">
                        <span class="kw-jp jp-text">${ex.word} (${ex.reading})</span>
                        <span class="kw-vi">${ex.vi}</span>
                    </li>
                `).join('')}
            </ul>
        </div>
    `).join('');
}

function filterKanji(lesson, btn) {
    currentKanjiFilter = lesson;
    if (btn) {
        btn.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    applyKanjiFilter();
}

function handleKanjiSearch() {
    applyKanjiFilter();
}

function applyKanjiFilter() {
    const keyword = document.getElementById('kanjiSearchInput').value.trim().toLowerCase();
    let filtered = rawKanji;
    if (currentKanjiFilter !== 'ALL') {
        filtered = filtered.filter(k => k.lesson === currentKanjiFilter);
    }
    if (keyword) {
        filtered = filtered.filter(k => 
            k.char.includes(keyword) ||
            k.hv.toLowerCase().includes(keyword) ||
            k.meaning.toLowerCase().includes(keyword) ||
            (k.kun && k.kun.toLowerCase().includes(keyword)) ||
            (k.on && k.on.toLowerCase().includes(keyword))
        );
    }
    renderKanji(filtered);
}

// Speech Synthesis (Unified via audio-engine.js)

// Render Quiz Questions
function renderQuiz() {
    const container = document.getElementById('questionsContainer');
    container.innerHTML = quizData.map((item, idx) => `
        <div class="question-card" id="qCard_${item.id}">
            <div class="q-header">
                <span class="q-num">Câu ${idx + 1} / ${quizData.length}</span>
                <span class="q-category">${item.lesson} • ${item.category}</span>
            </div>
            <div class="q-text jp-text">${item.q}</div>
            <div class="options-list">
                ${item.options.map((opt, oIdx) => `
                    <button class="opt-btn" id="optBtn_${item.id}_${oIdx}" onclick="selectAnswer(${item.id}, ${oIdx})">
                        <span class="opt-key">${['A', 'B', 'C', 'D'][oIdx]}</span>
                        <span class="jp-text">${opt}</span>
                    </button>
                `).join('')}
            </div>
            <div class="q-explain" id="explain_${item.id}">
                💡 <strong>Giải thích chi tiết:</strong> ${item.explain}
            </div>
        </div>
    `).join('');
}

function selectAnswer(qId, selectedIdx) {
    if (userAnswers[qId] !== undefined) return; // Đã trả lời rồi thì không đổi

    userAnswers[qId] = selectedIdx;
    const qItem = quizData.find(q => q.id === qId);
    const correctIdx = qItem.correct;

    // Vô hiệu hóa các nút trong câu
    qItem.options.forEach((_, idx) => {
        const btn = document.getElementById(`optBtn_${qId}_${idx}`);
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.add('correct');
        } else if (idx === selectedIdx) {
            btn.classList.add('wrong');
        }
    });

    // Hiển thị giải thích
    const explainEl = document.getElementById(`explain_${qId}`);
    explainEl.style.display = 'block';

    // Cập nhật điểm
    updateScore();
}

function updateScore() {
    let correctCount = 0;
    let answeredCount = Object.keys(userAnswers).length;

    quizData.forEach(q => {
        if (userAnswers[q.id] === q.correct) {
            correctCount++;
        }
    });

    const percent = Math.round((correctCount / quizData.length) * 100);
    document.getElementById('scoreDisplay').innerText = correctCount;
    document.getElementById('quizProgressText').innerText = 
        `Đã làm: ${answeredCount}/${quizData.length} câu • Tỷ lệ đúng: ${percent}%`;

    if (answeredCount === quizData.length) {
        let rank = "🏆 XUẤT SẮC!";
        if (percent < 60) rank = "⚠️ CẦN ÔN TẬP THÊM!";
        else if (percent < 80) rank = "👍 KHÁ TỐT!";
        else if (percent < 90) rank = "🌟 RẤT GIỎI!";

        document.getElementById('quizStatusTitle').innerText = 
            `HOÀN THÀNH: ${correctCount}/${quizData.length} ĐIỂM (${percent}%) - ${rank}`;
    }
}

function resetQuiz() {
    userAnswers = {};
    document.getElementById('scoreDisplay').innerText = '0';
    document.getElementById('quizStatusTitle').innerText = 'Bài Thi Thử Mini Test (30 Câu)';
    document.getElementById('quizProgressText').innerText = `Đã làm: 0/${quizData.length} câu • Điểm số: 0%`;
    renderQuiz();
    window.scrollTo({ top: document.getElementById('tab-quiz').offsetTop - 60, behavior: 'smooth' });
}

// Khởi tạo ban đầu
document.addEventListener('DOMContentLoaded', () => {
    applyVocabFilter();
    renderKanji(rawKanji);
    renderQuiz();
});



