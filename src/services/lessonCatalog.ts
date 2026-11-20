export interface LessonMeta {
  level: 'A2-1' | 'A2-2';
  number: number;
  topic: string;
  title: string;
  subtitle: string;
  quote: string;
  icon: string;
}

const a2_1: Array<[string, string, string, string]> = [
  ['Nơi ở & Gia đình', 'Nơi ở và công việc của tôi', 'あねは ちゅうごくに すんでいます', '🌸'],
  ['Sở thích & Ngôn ngữ', 'Nói về sở thích và khả năng', 'ギターが できます', '🎨'],
  ['Mùa & Khí hậu', 'Bốn mùa ở Nhật Bản', '日本はいま、はるです', '🍁'],
  ['Thời tiết & Dự báo', 'Kể về thời tiết và kế hoạch', 'あしたは はれるでしょう', '⛅'],
  ['Phố xá & Nơi chốn', 'Miêu tả khu phố', 'この町は しずかです', '🏙️'],
  ['Chỉ đường & Ngã rẽ', 'Hỏi và chỉ đường', 'まっすぐ 行ってください', '🗺️'],
  ['Hẹn gặp & Giờ giấc', 'Sắp xếp thời gian gặp nhau', '何時に 会いましょうか', '⏰'],
  ['Sự kiện & Mời mọc', 'Mời bạn tham gia sự kiện', 'いっしょに 行きませんか', '⛩️'],
  ['Học tập & Phát âm', 'Nói về cách học tiếng Nhật', '日本語を 勉強しています', '🗣️'],
  ['Ngoại ngữ & Văn hóa', 'Chia sẻ trải nghiệm giao lưu', '日本語で 話します', '🌟'],
  ['Dã ngoại & Ăn uống', 'Cùng chuẩn bị buổi dã ngoại', 'おべんとうを 持っていきます', '🍱'],
  ['Món ăn ngày đặc biệt', 'Nấu và chia sẻ món ăn', 'お祝いの 料理を 作ります', '🍜'],
  ['Đi công tác & Gặp gỡ', 'Hành trình và công việc', '空港で 会いましょう', '✈️'],
  ['Quy tắc nơi làm việc', 'Trao đổi phép lịch sự tại công ty', '会社で 写真を 撮ってもいいですか', '💻'],
  ['Sức khỏe & Thể dục', 'Thói quen bảo vệ sức khỏe', '体操すると いいですよ', '🏥'],
  ['Tập luyện & Vận động', 'Nói về vận động thường ngày', '毎日 歩いています', '🏃'],
  ['Quà tặng & Kỷ niệm', 'Chúc mừng và trao quà', 'お祝いを あげます', '🎁'],
  ['Tiệc tùng & Sự kiện', 'Kể chuyện và gặp gỡ', 'パーティーを しました', '👘'],
];

const a2_2: Array<[string, string, string, string, string]> = [
  ['新しい友だち', 'Tên gọi', 'Giới thiệu tên, quê quán và ý nghĩa tên mình.', 'いいなまえですね', '🌸'],
  ['新しい友だち', 'Miêu tả người', 'Nhận diện và miêu tả người qua trang phục, vẻ ngoài.', 'めがねをかけている人です', '👓'],
  ['店で食べる', 'Món ăn gợi ý', 'Gọi món và chia sẻ khẩu vị ở nhà hàng Nhật.', 'おすすめは何ですか', '🍲'],
  ['店で食べる', 'Cách ăn', 'Xin bỏ nguyên liệu và hỏi cách dùng món.', 'どうやって食べますか', '🥢'],
  ['沖縄旅行', 'Lời khuyên du lịch', 'Chuẩn bị và hỏi lời khuyên trước chuyến đi Okinawa.', 'ぼうしを持っていったほうがいいです', '✈️'],
  ['沖縄旅行', 'Xem biểu diễn cá heo', 'Kể trải nghiệm du lịch và điều có thể làm.', 'イルカのショーが見られます', '🐬'],
  ['日本まつり', 'Nếu trời mưa', 'Trao đổi kế hoạch khi thời tiết thay đổi.', '雨がふったら、どうしますか', '🏮'],
  ['日本まつり', 'Hòa nhạc đã bắt đầu chưa', 'Hỏi thời gian, địa điểm và chương trình lễ hội.', 'コンサートはもう始まりましたか', '🎆'],
  ['とくべつな日', 'Kỳ nghỉ Tết', 'Kể về cách đón năm mới và những việc đã làm.', 'お正月はどうしていましたか', '🎍'],
  ['とくべつな日', 'Cầu mong điều tốt', 'Nói về điều ước và phong tục theo mùa.', 'いいことがありますように', '🎂'],
  ['ネットショッピング', 'Đồ gia dụng bị hỏng', 'Mô tả vấn đề của đồ điện và nhờ hỗ trợ.', 'そうじきがこわれてしまったんです', '🧹'],
  ['ネットショッピング', 'So sánh & Mua sắm online', 'So sánh tính năng, giá và lựa chọn sản phẩm.', 'こっちのほうが安いです', '🏷️'],
  ['れきしと文化の町', 'Lịch sử Kyoto', 'Tìm hiểu lịch sử và văn hóa ở một thành phố.', 'このおてらは14せいきにたてられました', '🏯'],
  ['れきしと文化の町', 'Nghe kể về tranh', 'Nghe và truyền đạt điều được kể lại.', 'この絵はとてもゆうめいだそうです', '🖼️'],
  ['せいかつとエコ', 'Tiết kiệm năng lượng', 'Trao đổi việc sử dụng năng lượng và bảo vệ môi trường.', '電気がついたままですよ', '🌱'],
  ['せいかつとエコ', 'Chợ trời', 'Nói về đồ dùng không cần và hoạt động tái sử dụng.', 'フリーマーケットで売ります', '♻️'],
  ['じんせい', 'Nhân vật nổi tiếng', 'Miêu tả người và thành tựu của họ.', 'この人、しっていますか', '🌟'],
  ['じんせい', 'Bạn đã từng là đứa trẻ thế nào?', 'Kể lại tính cách, trải nghiệm và kỷ niệm thời nhỏ.', 'どんな子どもでしたか', '🧸'],
];

export const lessonCatalog: LessonMeta[] = [
  ...a2_1.map(([topic, title, quote, icon], index) => ({
    level: 'A2-1' as const,
    number: index + 1,
    topic,
    title,
    subtitle: `Bài ${index + 1} Marugoto A2-1 · ${title}`,
    quote,
    icon,
  })),
  ...a2_2.map(([topic, title, subtitle, quote, icon], index) => ({
    level: 'A2-2' as const,
    number: index + 1,
    topic,
    title,
    subtitle,
    quote,
    icon,
  })),
];
