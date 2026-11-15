# Rà soát code Marugoto A1–A2

Ngày: 2026-11-15. Commit được kiểm tra: `9370f8c`.

## Kết luận

Ứng dụng có nội dung phong phú, chia module tương đối rõ và chạy được trên trình duyệt. Ưu tiên cao nhất là sửa bộ chấm bài, bộ chia động từ và vòng đời checkpoint: các lỗi này ảnh hưởng trực tiếp đến kết quả học. Sau đó tối ưu tài nguyên 3D và gom logic dùng chung.

## Phạm vi và kiểm tra đã chạy

- Kiểm kê 47 HTML, 55 JavaScript (gồm 2 file vendor), 27 CSS, 6 Python và 8 JSON.
- Rà cấu trúc, các engine dùng chung, controller bài học/đề thi, cách tổ chức dữ liệu và generator. Không coi việc kiểm tra code là thẩm định toàn bộ nội dung giáo trình/PDF.
- Kiểm tra tham chiếu file local trên cả 47 HTML: không phát hiện đường dẫn file bị thiếu. Kiểm tra này không xác nhận mọi hash điều hướng hay tài nguyên ngoài mạng.
- `node --check` đạt trên cả 55 JS; parse AST đạt trên 6 Python.
- Smoke test 37 trang ứng dụng bằng Chrome headless qua HTTP local: không có `pageerror` lúc tải; không ghi nhận HTTP response >=400 trong lượt chạy. Đo chiều rộng tại 1280px và 390px không phát hiện document tràn ngang; đây chưa phải kiểm tra đầy đủ mọi trạng thái giao diện.
- Build 3 generator trong bản sao tạm: đạt kiểm tra và không tạo khác biệt HTML/JS so với bản hiện tại. Riêng đường dẫn ghi cứng trong generator cram đã được chuyển sang bản sao tạm để phép thử không ghi nhầm vào repo gốc; xem R11.
- Bộ chấm mới chấp nhận đáp án mẫu và các biến thể khai báo của 112 câu + 121 mục Kanji. Không thấy ID câu trùng hoặc phần tử `traps[].wrong` được chấp nhận trong dữ liệu đã kiểm tra. Đây là kiểm tra tính nhất quán, không chứng minh mọi quy tắc ngữ pháp đều đúng.
- Tái hiện các lỗi dưới đây bằng trình duyệt hoặc Node. Các phép thử thời gian dùng clock của Playwright; dữ liệu trình duyệt là context tạm.

## Lỗi cần sửa

### R1 — P1: Bộ chấm dịch chấp nhận câu thiếu nội dung, thậm chí chỉ dấu câu

**Vị trí:** `assets/js/pages/dich_cau_1_10.js:300–315,384–385`; `assets/js/pages/de_thi_midterm_a2_1.js:793–802`.

**Đã tái hiện:**

- Bài dịch L1–10, các câu 1–4: nhập `は` trả về 100%.
- Midterm M101, câu 31 và 32: nhập `。` trả về đúng.

**Nguyên nhân:** dùng `target.includes(user)` để chấm đúng toàn câu. Ở Midterm, dấu câu bị chuẩn hóa thành chuỗi rỗng và mọi chuỗi đều `includes('')`.

**Cải tiến:** từ chối chuỗi rỗng sau chuẩn hóa; bỏ phép so khớp chuỗi con cho đáp án hoàn chỉnh; dùng đáp án/biến thể được khai báo và bộ chấm chung. Nếu dùng từ khóa để phản hồi một phần, không coi đó là xác nhận toàn câu đúng.

**Nghiệm thu:** dấu câu, một trợ từ, câu thiếu mệnh đề hoặc sai phủ định/thì không được điểm tối đa; các biến thể hợp lệ vẫn được nhận.

### R2 — P1: Verb Lab sinh cách chia sai cho động từ cơ bản

**Vị trí:** `assets/js/pages/the_ta.js:309–455`.

**Đã tái hiện:**

| Nhập | Kết quả hiện tại | Kết quả đúng cần có |
|---|---|---|
| `かう` | `かうます`, `かうた` | `かいます`, `かった` |
| `はなす` | `はなすて`, `はなすた` | `はなして`, `はなした` |
| `およぐ` | `およぐた` | `およいだ` |
| `かします` | Nhóm 3, `かする`, `かしない` | Nhóm 1, `かす`, `かさない` |

**Nguyên nhân:** coi mọi đuôi `します` là suru; thiếu quy tắc cho nhiều đuôi thể từ điển và fallback chỉ nối hậu tố.

**Cải tiến:** dùng từ điển động từ có nhóm, cách đọc và ngoại lệ làm nguồn chuẩn; xử lý đủ godan/ichidan/suru/kuru; đầu vào mơ hồ hoặc ngoài phạm vi cần được nhận diện thay vì sinh kết quả đoán như đáp án chuẩn.

### R3 — P1: Khôi phục checkpoint có thể vô hiệu hóa âm thanh, cuộn và alert

**Vị trí:** `assets/js/checkpoint-sync.js:222–253,595–607`.

**Đã tái hiện:** ở `the_ru.html`, bấm chấm bài, chuyển sang tab lý thuyết rồi reload. Sau khi restore hoàn tất, `window.speakText`, `window.scrollTo`, `window.alert` đều trở thành `function () {}`.

**Nguyên nhân:** nhiều lần `withSilentUI()` chạy chồng nhau; lần sau ghi nhớ hàm no-op do lần trước đặt. Timer khôi phục sau cùng lại ghi no-op trở lại.

**Cải tiến:** dùng cờ/counter restore và truyền tùy chọn im lặng vào renderer/audio; tránh thay thế các hàm global. Nếu còn cần override tạm, quản lý một snapshot gốc và chỉ khôi phục khi toàn bộ tác vụ restore đã kết thúc.

### R4 — P2: “Xóa checkpoint” không xóa tiến độ Typing Studio

**Vị trí:** `assets/js/typing-studio.js:9,26–76`; `assets/js/mini-test-15-18.js:932–935`; `assets/js/cram-kanji.js:2–7`.

**Đã tái hiện:** làm đúng một câu, bấm nút xóa checkpoint và xác nhận. Sau reload, history vẫn có một câu; key `marugoto_typing_studio_v2` còn tồn tại.

**Nguyên nhân:** key của Studio không nằm trong danh sách extra keys của trang. Studio và coordinator còn lưu hai bản của cùng `tpState`.

**Cải tiến:** thống nhất nơi sở hữu state và registry các key. Xác định rõ Studio là tiến độ dùng chung hay theo trang, rồi làm cho thao tác reset và thông báo đúng với phạm vi đó.

### R5 — P2: Lọc bảng TA/NAI làm mất câu trả lời đang nhập

**Vị trí:** `assets/js/pages/the_ta.js:104–162`; `assets/js/pages/the_nai.js:16–86`.

**Đã tái hiện trên TA:** nhập `かいた`, tìm từ khóa không có kết quả rồi xóa bộ lọc: ô trước đó trở thành rỗng.

**Nguyên nhân:** mỗi lần lọc đều xóa `tbody` và tạo input mới, không render từ state câu trả lời. Cơ chế checkpoint chỉ restore lúc khởi động nên không giải quyết việc rerender trong phiên.

**Cải tiến:** quản lý `answersByVerbId`, cập nhật khi nhập, render theo ID; hoặc lọc bằng cách ẩn/hiện hàng. Điểm số khi lọc cũng cần xác định rõ tính trên bộ lọc hay toàn bộ bài.

### R6 — P2: Tự chuyển câu có thể bỏ qua thêm một câu

**Vị trí:** `assets/js/typing-studio.js:999–1000,1082–1087,1255–1308`.

**Đã tái hiện:** bật tự chuyển, trả lời đúng câu đầu rồi bấm câu tiếp ngay. Index chuyển `0 → 1`, sau timer lại thành `2`.

**Nguyên nhân:** `setTimeout(skipTypingWord, 900)` không lưu ID để hủy và không kiểm tra câu/mode đã đổi.

**Cải tiến:** quản lý timer và token của câu đang chấm; hủy khi chuyển câu, đổi mode/bộ lọc, gõ lại hoặc reset.

### R7 — P2: Thống kê cuối vòng và danh sách ôn lại không nhất quán

**Vị trí:** `assets/js/typing-studio.js:345–351,1055–1059,1208–1218,1291–1299`.

**Đã tái hiện:** xem đáp án câu đầu, nhảy tới câu cuối và kết thúc vòng. Modal báo `111 Đúng • 1 Chưa chuẩn` dù 111 câu chưa được trả lời. Bấm ôn lại một câu thì danh sách trống và báo đã làm đúng hết.

**Nguyên nhân:**

- Số đúng được tính bằng `total - wrongCount`, tính cả câu chưa làm.
- Tổng kết tính `reveal` là cần ôn, nhưng bộ lọc ôn lại chỉ lấy `err`.

**Cải tiến:** đếm rõ `ok`, `err`, `reveal`, `unanswered`; thống nhất tiêu chí “cần ôn lại” ở tổng kết, badge và queue. Chỉ xác nhận hoàn thành khi mọi mục có trạng thái phù hợp.

### R8 — P2: 3D tiếp tục render sau khi đóng và tích lũy geometry

**Vị trí:** `assets/js/vocab-3d-engine.js:1133–1158,1179–1187,1242–1246`.

**Đã đo trên Lesson 12:**

- Ban đầu: 4 geometry.
- Sau 20 lần chuyển từ: 91 geometry.
- Đóng modal: geometry vẫn là 91; render frame tiếp tục tăng `54 → 67` trong 200ms đồng hồ thử nghiệm.

**Nguyên nhân:** bỏ model khỏi scene nhưng không dispose geometry/material/texture; đóng modal không dừng animation loop.

**Cải tiến:** dispose tài nguyên thuộc model cũ, tránh dispose nhầm tài nguyên dùng chung; dừng/resume RAF theo modal và visibility; lazy-load thư viện/model khi người học mở 3D.

### R9 — P2: Chế độ thi từ vựng vẫn lộ đáp án ngay

**Vị trí:** `assets/js/vocab-hub.js:929–979`.

**Đã tái hiện:** đặt `quizSettings.mode = 'test'`, chọn sai câu đầu; nút đáp án đúng vẫn có class `correct`, bộ đếm sai tăng ngay.

**Nguyên nhân:** tô đúng/sai và cập nhật thống kê trước nhánh kiểm tra mode; mode chỉ quyết định banner và tự chuyển câu.

**Cải tiến:** test mode lưu lựa chọn nhưng chỉ hiển thị đúng/sai sau nộp bài; practice mode giữ phản hồi ngay. Cần lưu từng đáp án theo question ID nếu muốn xem lại bài thi đầy đủ.

### R10 — P2: Bộ chấm mới chưa chuẩn hóa Unicode đầy đủ

**Vị trí:** `assets/js/jp-typing-grader.js:49–73`.

**Đã tái hiện:** cùng câu `がっこうにいきます`, dạng NFC được nhận nhưng dạng NFD bị từ chối; Katakana half-width `ｶﾞｯｺｳﾆｲｷﾏｽ` cũng không được nhận.

**Cải tiến:** chuẩn hóa `NFKC` trước khi chuyển Katakana → Hiragana; kiểm tra cả đáp án và bài nhập bằng cùng pipeline. Bổ sung test với dakuten kết hợp, ký tự full-width và half-width.

### R11 — P2: Generator phụ thuộc đường dẫn tuyệt đối của máy hiện tại

**Vị trí:** `scripts/build_cram_kanji_11_18.py:4`.

`WORKSPACE = '/Users/dangvu/Downloads/nhật'`.

**Ảnh hưởng:** clone hoặc đổi tên thư mục có thể đọc/ghi nhầm vào repo cũ nếu nó còn tồn tại; máy khác sẽ lỗi đường dẫn.

**Cải tiến:** lấy root từ `Path(__file__).resolve().parents[1]` như cách các builder khác suy ra đường dẫn. Thêm phép build ở một thư mục tạm khác và so sánh artifact.

## Các cải tiến kiến trúc và trải nghiệm

### A. Một nguồn dữ liệu và engine dùng chung

- `lesson_01.js`–`lesson_09.js` lặp cấu trúc Verb Lab, flashcard và quiz; L11–18 cũng lặp renderer, hội thoại và checkpoint tương tự. Tách dữ liệu từng lesson khỏi `lesson-engine`.
- Chuẩn hóa schema câu hỏi: `id`, loại câu, prompt, accepted answers, giải thích, trọng số. Các bộ chấm hiện có chính sách dung sai khác nhau.
- Gom kiến thức động từ vào một nguồn có nhóm/ngoại lệ, dùng cho cả bảng học, Verb Lab và chấm bài.
- Duy trì ID ổn định và version/migration cho state khi cập nhật nội dung.

### B. Lưu tiến độ nhẹ và dễ khôi phục

- Đã đo 10 sự kiện nhập trong Studio gây 20 lần `localStorage.setItem`, ghi tổng 30.880 đơn vị độ dài chuỗi trong trạng thái thử nghiệm. Đây là độ dài JS string, không phải phép đo byte lưu trên đĩa.
- Debounce ghi nháp và chỉ ghi state cần thiết; flush ở `pagehide`/`visibilitychange`. Hiển thị lỗi lưu thay vì vẫn ngụ ý tiến độ đã an toàn.
- Thêm xuất/nhập backup JSON, sau đó mới cân nhắc đồng bộ nhiều thiết bị.
- Thay cơ chế replay click và quét toàn bộ DOM bằng restore state có kiểm soát cho các module phức tạp.

### C. CSS và điều hướng

- `site-theme.css` có 765 lần `!important`; CSS nhúng trong `nav.js` có thêm 276. Nên đưa navbar CSS vào file riêng, dùng token và scope component để giảm xung đột.
- Navbar dùng `role="dialog"`/`aria-modal="true"` nhưng chưa quản lý focus đầy đủ. Thêm focus ban đầu, giữ focus trong modal, trả focus lúc đóng.
- Nhiều thẻ tương tác dùng `div` + click. Dùng button/link và trạng thái ARIA tương ứng.
- Studio chặn Tab để bỏ qua câu (`typing-studio.js:1343–1345`); nên dùng phím tắt riêng để Tab vẫn điều hướng được.
- Mục “Thể TE” trong `assets/nav.js:14` vẫn trỏ `index.html`, trong khi index hiện là hub. Cần cập nhật nhãn/đích theo cấu trúc mới.

### D. Kiểm thử và build

- Thư mục `tests/` hiện chứa các trang đề thi học tập; chưa thấy bộ test tự động chuyên cho logic ứng dụng.
- `build_all.py` kiểm tra 37 trang và 53 JS; nên dùng discovery nhất quán để bao phủ docs HTML và vendor JS khi cần.
- Đưa những ca lỗi R1–R10 vào regression tests: đặc biệt chấm sai, reset/reload, lọc không mất bài, auto-advance và thống kê.
- Dùng fake clock kiểm tra timer khi tab bị treo/ẩn. Midterm và mini-test 11–14 đếm bằng `seconds--`, trong khi đề 5–8 đã dùng thời gian thực; nên thống nhất cách tính deadline.
- Chạy build, validation schema, unit test và một số browser smoke test trong CI.

### E. Nâng chất lượng học sau khi sửa lõi

1. Dashboard “tiếp tục học”, số câu chưa làm và nhóm lỗi thường gặp.
2. Ôn cách quãng dựa trên lịch sử trả lời, thay vì chỉ một nhãn “đã thuộc”.
3. Thống kê theo kỹ năng: trợ từ, chia động từ, đọc Kanji, dịch câu.
4. Offline có chủ đích: dùng vendor local sẵn có cho demo 3D; cache app/data và chọn fallback cho TTS/SVG.

## Thứ tự thực hiện đề xuất

1. **Độ chính xác:** R1, R2, R10; thiết lập regression tests cho chấm và chia động từ.
2. **Tiến độ và luồng học:** R3–R7, R9; thống nhất state và reset.
3. **Hiệu năng và vận hành:** R8, R11; debounce autosave, bổ sung CI.
4. **Bảo trì và tính năng:** engine bài học dùng chung, CSS, accessibility, dashboard và ôn cách quãng.

Mỗi bước cần có tiêu chí nghiệm thu cụ thể, tránh gộp thay đổi giao diện lớn với sửa bộ chấm hoặc chuyển đổi dữ liệu tiến độ.
