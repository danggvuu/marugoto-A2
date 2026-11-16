# Sửa ánh xạ nút phát âm — 16/11/2026

## Lỗi đã tái hiện

1. Mở kho từ vựng → Flashcard → Xáo trộn → quay về Bảng từ → mở Nét viết.
   Bảng còn hàng `自己紹介`, nhưng modal lấy phần tử mới tại index đó: `名前`,
   rồi nút phát âm modal gửi `なまえ`. Đã sửa bằng cách render bảng theo cùng
   danh sách hiện tại khi xáo trộn/quay về bảng.
2. Widget nét chữ có thể nhận kết quả tải SVG cũ sau khi đổi sang chữ mới.
   Thêm mã yêu cầu cho cả widget và modal; kết quả cũ không được ghi đè chữ mới.
   Mở rộng widget dùng đúng mục đang hiển thị, không dùng mục modal trước đó.

## Sửa cách chọn text

- Nút từ vựng của lesson 10–18, các mini-test, quiz từ vựng, luyện gõ và 3D vocab
  ưu tiên trường Kana có sẵn.
- Typing Studio dùng `hira` cho mẫu câu, `kana` cho từ/Kanji khi có dữ liệu.
- Nút ví dụ Kanji gửi `ex.reading`, không để TTS đoán âm của `ex.word`.
- Nút âm Kun/On bỏ dấu ngắt okurigana (`は-れる → はれる`) và tách các cách đọc
  bằng dấu ngắt câu. Âm trống không phát.
- Khi bấm ký tự Kanji, tooltip ghi rõ nhóm âm Kun/On được đọc. Không mặc định
  một chữ Hán chỉ có một âm đọc duy nhất.
- Chuẩn hóa HTML ruby dùng furigana đã ghi rõ, ví dụ
  `<ruby>生<rt>なま</rt></ruby>たまご → なまたまご`.
- 3D Lab đồng bộ mục đang hiển thị với mục của nút đọc, ưu tiên Kana.

## Kiểm chứng

Browser tests chặn và ghi text truyền đi để kiểm tra:

- Bảng → xáo trộn → phân trang → lọc → modal → đọc đúng mục.
- Nút từ vựng trên 18 bài; mở tab từ vựng thật trước khi click nút mini-test.
- Nút đọc ví dụ Kanji sau đổi trang/bộ lọc.
- Đổi mode/câu trong Typing Studio, đổi mã đề, chuyển card 3D.
- Payload thực gửi tới URL TTS và Web Speech fallback; callback cũ không đọc chen
  sau khi người dùng chọn một từ khác.
- Kết quả tải nét cũ không ghi đè chữ vừa chọn.

Các test xác nhận **đúng text/cách đọc gửi vào bộ tổng hợp**, không phải nghe và
chấm chất lượng âm thanh của mọi giọng trên mọi thiết bị. Nếu text đúng nhưng
âm thực nghe sai, cần chữ cụ thể, tên trang và trình duyệt/giọng để đối chiếu tiếp.
Lượt kiểm tra trước chỉ so chuỗi trong DOM, có selector rỗng và bỏ sót API
`AudioEngine.speak`; không dùng kết quả đó làm bằng chứng toàn bộ voice đúng.
