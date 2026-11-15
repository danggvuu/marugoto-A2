# Kiểm tra lại dự án Nhật — bản đang chỉnh sửa

> **Cập nhật sau sửa:** Các lỗi thao tác bên dưới là kết quả của lượt audit trước, không phải danh sách lỗi còn mở.
> Commit `75579bf` đã sửa lỗi biến/hàm không tồn tại và giữ mảnh xếp câu. Lượt sửa tiếp theo đã:
> - Sửa thứ tự reset/render khi lọc và lưu phân trang từ vựng/Kanji.
> - Lưu phiên thi theo mã đề (mode, deadline, tạm dừng, đáp án, trạng thái đã nộp); chuyển đổi draft cũ.
> - Khóa lời giải, bản dịch và bộ lọc sai trước nộp; sửa xem lại bài và ngăn nộp lặp.
> - Sửa chọn hoạt động mới nhất và chuyển đổi nhãn bỏ qua trong checkpoint cũ mà không xóa lịch sử.
> - Rút gọn tab/hero mobile, đổi hàng từ vựng mobile thành thẻ có Kana và nút thao tác,
>   thêm mục lục/chế độ học từng phần, làm rõ đây là bài tự luyện Marugoto chứ không phải chứng nhận JLPT.
> - Đưa đề tổng hợp vào build; controller JS chỉ có một source để không bị generator cũ ghi đè.
>
> Kết quả sau sửa: **28/28 regression checks**, **14/14 browser tests** và build trong bản sao tạm đều đạt;
> không có chênh lệch HTML/JS giữa source hiện tại và kết quả build.
> Browser suite bao gồm smoke test 38 trang và các viewport 360, 390, 768, 1440px trên các trang đại diện.
> Chạy lại bằng `node tests/run_regression_tests.js` và `python3 tests/test_browser.py`.
> Những kiểm tra này không thay cho thẩm định toàn bộ nội dung tiếng Nhật/PDF hoặc kiểm tra Safari/iOS thật.

Ngày kiểm tra: 2026-11-15. Đây là kiểm tra working tree hiện tại, không chỉ commit HEAD. Không sửa code ứng dụng hoặc ghi đè công việc đang có.

## Phạm vi và kết quả

- Mở 38 trang ứng dụng trong Chrome headless, viewport 390×844. 37 trang không có pageerror lúc tải; kho từ vựng có lỗi runtime.
- Kiểm tra cú pháp 57 JavaScript: đạt.
- Kiểm tra tham chiếu file local và cân bằng script trên 38 HTML: đạt.
- `node tests/run_regression_tests.js`: 28 đạt, 0 thất bại. Một số test chỉ dò source nên không kiểm chứng đầy đủ hành vi.
- Chạy `scripts/build_all.py` trong bản sao tạm: đạt, không có khác biệt HTML/JS sau build. Build hiện tại chưa gọi các generator của đề tổng hợp mới.
- Browser tests bổ sung: phân trang/lọc từ vựng, reload Kanji, chọn và xếp câu đề tổng hợp, đổi mode thi, checkpoint cũ/mới, nút tiếp tục học.
- Không coi smoke test là thẩm định mọi đáp án tiếng Nhật, nội dung PDF, hiệu năng máy thật hay mọi trạng thái giao diện.

## Các cải thiện đã xác nhận

- Trang chủ có lối vào học rõ hơn, phần lộ trình đã thu gọn.
- Checkpoint pill gọn hơn, không phơi nút xóa thường trực.
- Kana thay thế trên mobile đã hiển thị (`.sub-kana-mobile` có computed display `block`).
- Kanji phân trang hoạt động: chiều dài document trong lượt đo mobile khoảng 16.110px, giảm nhiều so với khoảng 184.046px trước đó.
- Câu bỏ qua mới không còn đổ nhãn vào ô nhập khi chuyển sang danh sách cần ôn.
- Hướng dẫn shortcut đã chuyển sang Alt+S. Trong phép thử chuyển thủ công sau câu đúng, timer không làm tăng index thêm sau đó.

## Lỗi còn tồn tại, theo ưu tiên

### 1. P1 — Kho từ vựng dừng khởi tạo vì biến không tồn tại

**Vị trí:** `assets/js/vocab-hub.js:622`.

`selectedLevelScope` và `currentSearchQuery` được đọc nhưng không được khai báo trong controller. Mở trang với storage sạch phát sinh `ReferenceError: selectedLevelScope is not defined`.

**Tác động:** bảng chỉ render 50 từ đầu, thanh phân trang rỗng. Người dùng không có đường qua UI để xem phần còn lại; các bước khởi tạo sau lỗi có thể không chạy.

**Sửa:** dùng trạng thái thực đang có (`selectedLessons`, giá trị search input và bộ lọc tương ứng), không khai báo biến giả chỉ để hết lỗi. Test mở trang với storage sạch và checkpoint cũ, chuyển tới trang cuối.

### 2. P1 — Xóa bộ lọc gọi sai tên hàm

**Vị trí:** `assets/js/vocab-hub.js:545–557`.

`clearAllFilters()` gọi `renderActiveChips()` và `applyFilters()`, nhưng controller hiện dùng `renderActiveChipsBar()` và `applyFilter()`. Browser đã tái hiện lỗi `renderActiveChips is not defined`.

**Sửa:** nối với state/ID/hàm hiện có, xác minh nút reset lọc trả về toàn bộ từ và đồng bộ UI.

### 3. P1 — Đề tổng hợp không xếp được bốn mảnh câu

**Vị trí:** `assets/js/pages/de_thi_tong_hop_11_18.js:345–435`.

`placeStarPart()` lấy thứ tự từ `userAnswers`; `updateStarUI()` lại xóa `userAnswers[qId]` mỗi khi chưa đủ bốn mảnh.

**Tái hiện:** câu ★ đầu tiên, bấm mảnh 1 rồi mảnh 2. Chỉ mảnh 2 nằm ở ô đầu, các ô còn lại trống, state của câu là undefined.

**Sửa:** luôn lưu `starOrder`, kể cả 0–3 mảnh. Chỉ đặt `checked=true` khi đủ bốn mảnh. Test thêm/gỡ/reset, reload với ba mảnh và chấm điểm sau hoàn thành.

### 4. P2 — Reload đề tổng hợp tự về ôn luyện và reset thời gian

**Vị trí:** controller mới: `26`, `115–135`, `618–622`.

Draft chỉ chứa câu trả lời, không chứa mode, thời gian, trạng thái nộp bài.

**Tái hiện:** chuyển sang thi thử, đặt đồng hồ 123 giây, chọn một đáp án và reload. Bài nhập được giữ nhưng mode trở lại ôn luyện, timer về 2.700 giây.

**Sửa:** lưu/khôi phục versioned state theo mã đề, phân biệt bắt đầu lại với tiếp tục. Nếu timer cần chạy khi rời trang, dùng deadline thay vì chỉ `seconds--`.

### 5. P2 — Chế độ thi vẫn mở được lời giải và biết số câu sai

**Vị trí:** controller mới: `526–542`, `657–668`.

`toggleAllExplanations()` không kiểm tra mode hoặc trạng thái nộp. `updatePaletteFilterCounts()` vẫn cập nhật số sai trong mode thi.

**Tái hiện:** `isImmediateMode=false`, chọn đáp án và mở lời giải: explanation hiện `block`.

**Sửa:** vô hiệu hóa các thao tác tiết lộ đáp án trong thi thử trước nộp, gồm xem tất cả lời giải và lọc câu sai. Kiểm tra cả UI lẫn handler.

### 6. P2 — Nút “Xem lại bài làm” lại ẩn lời giải

**Vị trí:** controller mới: `781–785`.

`enterReviewMode()` gán `allExplained=true`, sau đó gọi hàm toggle khiến giá trị thành false và ẩn lời giải.

**Sửa:** dùng hàm `setExplanationsVisible(true)` rõ nghĩa; không dùng toggle khi cần một trạng thái xác định.

### 7. P2 — “Tiếp tục học” chọn nhầm hoạt động cũ

**Vị trí:** `assets/js/pages/index_hub.js:249–312`.

Typing Studio có `savedAt` nhưng không được so sánh; `latestTime` vẫn bằng 0 sau khi tìm thấy Studio. Mọi checkpoint trang có timestamp dương sẽ ghi đè dù cũ hơn.

**Tái hiện:** Studio vừa có hoạt động mới, lesson 1 có checkpoint timestamp 1. Nút tiếp tục vẫn trỏ lesson 1.

**Sửa:** chuẩn hóa timestamp và loại hoạt động từ các module; bỏ qua state chỉ mở menu/không có tiến độ học; link vào đúng mode/tab.

### 8. P2 — Checkpoint cũ vẫn hiện “(Đã bỏ qua)” trong ô nhập

**Vị trí:** `assets/js/typing-studio.js:79` và `973–980`.

Bản sửa xử lý `wasSkipped=true` cho dữ liệu mới, nhưng dữ liệu cũ chỉ có `lastInput: '(Đã bỏ qua)'`.

**Tái hiện:** lưu history kiểu cũ rồi reload: ô nhập vẫn chứa `(Đã bỏ qua)`.

**Sửa:** migration khi restore: nhận diện sentinel cũ, đặt `wasSkipped=true`, xóa nội dung nhãn khỏi input/draft. Không cần xóa toàn bộ tiến độ.

### 9. P2 — Phân trang từ vựng và state không đồng bộ sau lọc

**Vị trí:** `assets/js/vocab-hub.js:513–515`.

`renderTable()` chạy trước khi `vocabCurrentPage=1`.

**Phép thử chẩn đoán:** tạm cấp hai biến thiếu trong context trình duyệt, không sửa file, để đi qua lỗi số 1. Tới trang 10 rồi tìm `a`: state bằng 1 nhưng bảng/pagination vẫn ghi mục 451–500.

**Sửa:** reset số trang trước render. Test lọc từ trang cuối và bấm Tiếp ngay sau tìm kiếm.

### 10. P3 — Reload Kanji không giữ trang đang xem

**Vị trí:** `assets/js/kanji-a2.js:89–105,477–495`.

Từ trang 2, reload về trang 1. Mode grid/cards và vị trí phân trang chưa được tích hợp đầy đủ với checkpoint.

**Sửa:** lưu mode, page hoặc ID chữ đang xem; clamp hợp lệ khi đổi bộ lọc và khôi phục vị trí phù hợp.

## Frontend còn cần cải tiến

- Mobile Kanji vẫn dành gần hết màn hình đầu cho hero, bốn tab lớn, bộ lọc và hướng dẫn; chữ cần học ở phía dưới.
- Kho từ vựng đã đưa export vào nhóm phụ, nhưng đầu trang vẫn nhiều tầng điều khiển. Ưu tiên đưa kết quả đầu tiên lên sớm hơn.
- Bài học L15 vẫn dài khoảng 37.399px trong lượt đo mobile; cần mục lục gọn, chia phần hoặc thu gọn phần bổ trợ mà không làm mất nội dung.
- Đề tổng hợp mới có hero mobile gần 600px, nhiều badge và đoạn giới thiệu dài; đề bài bị đẩy xuống sâu.
- Nhãn “JLPT A2.1”/“đạt chuẩn JLPT A2.1” dễ gây hiểu nhầm: nên phân biệt trình độ Marugoto/CEFR A2 với cấp thi JLPT. Không khẳng định sẵn sàng thi chính thức chỉ dựa trên điểm bài tự biên soạn.
- Chưa thấy bằng chứng cho các tuyên bố “100% nguyên bản”, “100% giải thích” hoặc “chuẩn” trên hero; cần đối chiếu dữ liệu/PDF hoặc dùng nhãn thận trọng.

## Thứ tự sửa và nghiệm thu

1. Sửa lỗi khởi tạo kho từ vựng, reset filter và xếp câu ★.
2. Bảo toàn phiên thi và khóa lời giải trong mode thi.
3. Sửa resume, migration checkpoint cũ và lưu phân trang.
4. Rút gọn hero/tab/filter trên mobile.
5. Bổ sung browser regression cho tất cả lỗi trên; sau đó mới mở rộng test hình ảnh và accessibility.

Không chạy generator trực tiếp lên working tree trước khi kiểm tra diff. Tích hợp generator của đề tổng hợp mới vào quy trình build có kiểm chứng, tránh để file phát hành và nguồn generator lệch nhau.
