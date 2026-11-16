# Rà soát và nâng chất lượng nội dung — 16/11/2026

## Phạm vi thực hiện

- Viết lại **21 mục lý thuyết** ở Bài 3–9 theo các chủ điểm trong mục lục Marugoto A2-1.
- Thay các câu chia động từ chung chung ở cuối quiz Bài 3–9 bằng **49 câu ngữ pháp/giao tiếp gắn với bài**. Mỗi bài hiện có 8 câu từ vựng và 7 câu ứng dụng.
- Biên soạn **56 câu ví dụ Nhật–Việt** cho 8 từ đầu mỗi bài 3–9.
- Bỏ ví dụ tạo máy móc `Xを勉強します` trong dữ liệu bài 1–9 khi chưa có ví dụ phù hợp, thay vì hiển thị chúng như câu mẫu.
- Sửa các câu quiz Bài 2, 10–13, 15–18 có lỗi ghép đáp án, yêu cầu thiếu rõ ràng hoặc phương án nhiễu cũng đúng.
- Cân bằng vị trí đáp án trong 270 câu quiz bài 1–18 bằng thứ tự cố định có seed. Mỗi vị trí xuất hiện 3–4 lần/bài, không đổi lại mỗi lần reload.
- Đối chiếu số nét của **144 mục / 137 chữ Kanji khác nhau** với snapshot từ KanjiAPI: số nét trong dữ liệu nguồn khớp. Sửa một số nhãn cách đọc, không thay hàng loạt những cách đọc hiếm chỉ vì ít gặp.
- Sửa hai lỗi câu hỏi trong ngân hàng đề tổng hợp bổ sung M111–M115.

Các câu mới là **bài tự biên soạn theo chủ điểm**, không phải trích nguyên văn bài kiểm tra của Japan Foundation.

## Nguồn đã dùng

1. [Mục lục Rikai](../pdf/R_contents_eng.pdf), trang 1, các hàng A2-1 Lesson 3–18.
   Đã đọc ảnh trang để tránh dựa vào text bị lỗi mã font.
2. [Mục lục Katsudoo](../pdf/K_contents_eng.pdf), trang 1: mục tiêu giao tiếp và mẫu diễn đạt của từng bài.
3. KanjiAPI: `https://kanjiapi.dev/v1/kanji/{chữ}`. Truy cập 16/11/2026.
   Snapshot số nét và các chỉnh sửa cách đọc được ghi tại
   [`data/kanji_reference_checks.json`](../../data/kanji_reference_checks.json).

Các PDF ngữ pháp tiếng Việt L1–4, L5–8, L9–10 trong máy là bản ảnh; không coi kết quả trích text rỗng là đã kiểm chứng nội dung từng trang. Lần này dùng mục lục Rikai/Katsudoo để đối chiếu phạm vi chủ điểm, không tuyên bố đã duyệt toàn bộ sách.

## Những chỉnh sửa chuyên môn đáng chú ý

| Vị trí | Trước | Sau |
| --- | --- | --- |
| L3–9 lý thuyết | “Cấu trúc cốt lõi Bài…”, thiếu công thức thực tế | Công thức, cách dùng, câu mẫu, bản dịch và lỗi cần tránh |
| L3–9 ví dụ | `暑いを勉強します`, `遅れますを勉強します`… | Câu có ngữ cảnh; bỏ ví dụ giả còn lại |
| L2 Q11 | Coi `こと` là sai trong `覚える…が大変です` | Làm rõ mẫu `の`, không dùng `こと` làm nhiễu |
| L2 Q13 | `とき` và `ころ` cùng có thể đúng | Yêu cầu mẫu `とき`, thay lựa chọn gây mơ hồ |
| L11 Q15 | `お[願い]いします` lặp `い` | Điền một chữ `願` → `お願いします` |
| L12 Q1 | Coi dạng nghe nói `おいしいそうです` như lỗi chia | Nêu rõ phán đoán vẻ ngoài, thay nhiễu |
| L12 Q7 | Đánh sai `に似ています` dù hợp lệ | Giữ mẫu `と似ています` trong Katsudoo, bỏ `に` khỏi nhiễu |
| L15 Q1 | `痛いです` bị chấm sai dù là câu đúng | Yêu cầu dùng `んです`, thay nhiễu sai cấu trúc |
| L16 | Hiểu `たり` là luôn luân phiên; lời khuyên bằng た dễ bị hiểu là quá khứ | Giải thích liệt kê hoạt động tiêu biểu; ghi rõ た trong lời khuyên không chỉ việc đã xảy ra |
| L17 | Liệt kê quà thiếu rõ tân ngữ; vai cho/nhận dễ nhầm | `絵とか時計をあげます`; giải thích `父にもらう` và `父がくれる` |
| M111–M115 | `天気がいいだと思います` | `天気がいいと思います` |
| M111–M115 | `日本語の勉強をを始めました` khi ghép lựa chọn | Bỏ を cố định trước chỗ trống |
| Kanji | `駅` có Kun `えき`; `先` có `ま` cụt; âm ghép bị ghi như âm On độc lập | 駅: không có Kun, On えき; 先: さき/まず; bổ sung chuẩn 歩/結 |

Không sửa `毎` từ 6 nét sang số khác: nguồn đối chiếu xác nhận **毎 có 6 nét**. Không kết luận `Nと似ています` là sai; cả と và に có thể dùng, tùy cách diễn đạt.

## Giới hạn kết luận

- Kết quả quiz không đủ để tuyên bố đã “thành thạo toàn bộ bài”; thông báo thành công đã chuyển sang “làm tốt quiz”.
- Kiểm tra kỹ thuật xác nhận cấu trúc và hồi quy các lỗi đã biết, không chứng minh mọi câu trong toàn website chỉ có một đáp án đúng.
- Mẹo nhớ/chiết tự giúp học không nhất thiết là giải thích từ nguyên khoa học.
- Chưa thẩm định toàn bộ bản dịch, âm Hán Việt và mọi câu của các đề cũ. Các phần ngoài danh sách trên cần tiếp tục duyệt có nguồn, không gắn nhãn “đã kiểm chứng 100%”.

## Bảo toàn tiến độ

- Đường dẫn trang, ID từ vựng và ID ô luyện gõ giữ nguyên.
- Quiz sửa nội dung hoặc đổi vị trí đáp án dùng chữ ký click có phiên bản `content-2026-11-16`.
  Click cũ không tự chấm một câu mới; dữ liệu khác của trang vẫn được giữ.
- Hai câu đã sửa trong đề tổng hợp dùng `contentRevision`. Chỉ đáp án cũ của các câu đó cần làm lại; đáp án các câu khác vẫn khôi phục.

## Chỉnh sửa và kiểm tra sau này

```sh
python3 scripts/build_all.py
node qa/regression/run_regression_tests.js
node qa/regression/content_integrity.js
python3 qa/browser/test_browser.py
```

- Sửa nội dung được biên tập trong `scripts/lesson_content_review.py`, rồi chạy `build_lesson_content.py` hoặc `build_all.py`.
- Các quiz/cách đọc chưa có override vẫn giữ nguồn hiện tại trong file JS tương ứng; không viết đè tùy tiện toàn bộ kho từ vựng.
- Validator dừng khi thiếu khai báo quiz, JS không parse được, đáp án trùng sau bỏ ruby, vị trí đáp án lệch, lý thuyết còn placeholder hoặc số nét lệch snapshot.
- Browser test chấm các lựa chọn đúng đã cân bằng trên cả 18 bài và reload, đồng thời kiểm tra click cũ không áp vào nội dung mới.
