# Marugoto A1–A2 Study Hub

Website tự học tiếng Nhật bằng tiếng Việt, gồm bài học Marugoto, tra cứu từ vựng, Kanji, ngữ pháp, luyện gõ và đề ôn tập.

Ứng dụng chạy bằng **HTML, CSS và JavaScript thuần**, không cần backend hay tài khoản. Tiến độ được lưu trên trình duyệt bằng `localStorage`.

> Các đề trong dự án phục vụ tự luyện Marugoto A2.1, **không phải đề thi hoặc chứng nhận JLPT chính thức**.

## Chạy nhanh

Cần **Python 3** và trình duyệt hiện đại. Mở terminal tại thư mục dự án:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Truy cập **http://localhost:8000/**.

Không cần cài thư viện để học. Nên dùng server local thay vì mở trực tiếp bằng `file://`, vì một số chức năng phụ thuộc chính sách bảo mật của trình duyệt.

## Có gì trong ứng dụng?

| Chức năng | Nội dung |
| --- | --- |
| Bài học | 18 bài Marugoto A2-1, có mục lục và chế độ học từng phần |
| Từ vựng | Kho A1 bài 3–18 và A2-1 bài 1–18; tìm kiếm, chọn bài, phân trang, flashcard và quiz |
| Kanji | Tra nghĩa, cách đọc, thứ tự nét SVG và tập viết trực tiếp |
| Ngữ pháp | Tổng hợp mẫu câu, bài tập chia động từ và Verb Lab |
| Typing Studio | Luyện dịch câu, đọc Kanji, gõ từ vựng và ôn lại mục cần luyện |
| Đề ôn tập | Mini test, Midterm và bộ tổng hợp bài 11–18 có chấm điểm, lời giải và lịch sử |
| 3D Lab | Không gian văn hóa Nhật tương tác bằng Three.js |

### Vào thẳng các phần chính

- [Trang chủ](index.html)
- [Bài học đầu tiên](lessons/Marugoto_A2_Lesson_1.html)
- [Kho từ vựng](Tu_Vung_Marugoto_A1_16_A2_1_10.html)
- [Kanji & luyện viết](kanji_a2.html)
- [Ngữ pháp](Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html)
- [Luyện gõ câu và Kanji](tests/On_Tap_Mini_Test_A2_15_18.html#typing)
- [Đề tổng hợp Marugoto A2.1 bài 11–18](tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html)
- [3D Lab](demo_3d.html)

## Tiến độ và phiên thi

- Lưu trên **trình duyệt, thiết bị và origin hiện tại**; chưa có đồng bộ tài khoản hay nhiều thiết bị.
- Dùng cùng địa chỉ khi quay lại học. `localhost`, `127.0.0.1` và cổng khác nhau có vùng lưu riêng.
- Xóa dữ liệu website, dùng cửa sổ riêng tư hoặc chặn storage có thể làm tiến độ không được giữ.
- Trong đề tổng hợp 11–18, mỗi mã đề có phiên riêng: đáp án, mảnh xếp câu, chế độ, thời gian và trạng thái nộp.
- Đồng hồ thi tổng hợp tiếp tục tính khi rời trang, **trừ khi đã bấm tạm dừng**.
- Chế độ ôn luyện có phản hồi ngay; chế độ thi tổng hợp mở lời giải sau khi nộp.
- “Làm lại” và xóa checkpoint có ảnh hưởng tới dữ liệu đã lưu; đọc phạm vi và xác nhận trước khi xóa.

### Kết nối mạng

Nội dung và bài tập được phục vụ từ file local. Font, phát âm qua dịch vụ ngoài và dữ liệu nét Kanji có thể cần mạng. Phát âm còn phụ thuộc giọng tiếng Nhật được hỗ trợ trên máy; khi không tải được SVG, giao diện có chữ tĩnh và tùy chọn thử lại. Không nên coi đây là ứng dụng offline hoàn toàn.

## Cấu trúc thư mục

```text
.
├── index.html                 # Trang chủ
├── *.html                     # Các trang tra cứu/ngữ pháp/3D chính
├── lessons/                   # 18 trang bài học
├── tests/                     # Trang đề ôn tập cho người học, không phải test tự động
├── assets/
│   ├── nav.js                 # Điều hướng chung
│   ├── css/                   # CSS dùng chung, theo module và pages/
│   ├── data/                  # Dữ liệu JS được trình duyệt nạp
│   └── js/
│       ├── lessons/           # Controller và dữ liệu từng bài
│       ├── pages/             # Controller từng trang
│       └── vendor/            # Thư viện bên thứ ba
├── data/                      # JSON nguồn phục vụ xây dựng dữ liệu
│   └── extracted/             # Bản trích xuất tạm, không đưa vào Git
├── scripts/                   # Generator Python và kiểm tra build
├── qa/                        # Kiểm thử tự động, tách khỏi trang đề thi
│   ├── regression/            # Kiểm tra logic và quy tắc chống tái phát lỗi
│   ├── browser/               # Kiểm thử thao tác bằng Playwright
│   └── requirements-browser.txt
├── docs/
│   ├── pdf/                   # Tài liệu học và PDF nguồn của đề
│   ├── reviews/               # Báo cáo rà soát code/UX
│   ├── Ke_Hoach_10_Ngay/      # Lộ trình ôn tập
│   └── kanjiupdate/           # Ảnh tư liệu Kanji
└── artifacts/                 # Screenshot/kết quả thử local, không đưa vào Git
    └── screenshots/
```

Giữ nguyên tên/đường dẫn HTML đang chạy để không làm hỏng bookmark, link và khóa checkpoint cũ. Chỉ đổi vị trí file khi cập nhật đầy đủ nơi tham chiếu.

## Build và kiểm tra

### 1. Build dữ liệu và trang được sinh

Cần Python 3 và **Node.js** trong `PATH`:

```sh
python3 scripts/build_all.py
```

Lệnh này:

1. Sinh lại mini test 11–14, mini test 15–18, ôn Kanji cấp tốc và đề tổng hợp 11–18.
2. Kiểm tra tham chiếu file local và cặp thẻ `script` trong các trang ứng dụng.
3. Chạy `node --check` cho JavaScript trong `assets/`.

**Build có ghi lại các file được sinh.** Sau khi chạy, xem `git diff` để chắc chắn thay đổi đúng dự kiến. Kiểm tra link/cú pháp không thay thế kiểm tra thao tác thực tế.

### 2. Regression checks

```sh
node qa/regression/run_regression_tests.js
node qa/regression/content_integrity.js
```

Bao gồm kiểm tra bộ chấm, chuẩn hóa Unicode, chia động từ và một số kiểm tra cấu trúc source. Những kiểm tra dò source không chứng minh toàn bộ hành vi đúng trên trình duyệt.

### 3. Browser tests

Khuyến nghị dùng môi trường Python riêng:

```sh
python3 -m venv .venv
```

Kích hoạt môi trường:

```sh
# macOS / Linux
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

Cài và chạy:

```sh
python -m pip install -r qa/requirements-browser.txt
python -m playwright install chromium
python qa/browser/test_browser.py
```

Test tự mở HTTP server và browser context tạm, không dùng tiến độ học trong profile trình duyệt của bạn. Có thể dùng Google Chrome đã cài nếu Chromium của Playwright chưa có.

Các luồng được kiểm tra gồm phân trang, lọc, checkpoint cũ, xếp câu, đổi mã đề, timer, khóa lời giải và smoke test các trang. Các trang đại diện còn được kiểm tra ở chiều rộng 360, 390, 768 và 1440px.

Tùy chọn:

| Biến môi trường | Ý nghĩa |
| --- | --- |
| `CHROME_PATH` | Đường dẫn binary Chrome/Chromium tùy chỉnh |
| `MARUGOTO_SCREENSHOTS_DIR` | Thư mục lưu ảnh responsive |

Ví dụ trên macOS/Linux:

```sh
MARUGOTO_SCREENSHOTS_DIR=artifacts/screenshots/latest python qa/browser/test_browser.py
```

## Chỉnh sửa đúng nguồn

- **Controller/giao diện:** sửa file tương ứng trong `assets/js/`, `assets/css/` và HTML.
- **Trang do generator sinh:** sửa template trong `scripts/` trước, rồi build lại. Không chỉ sửa HTML đầu ra vì lần build tiếp theo sẽ ghi đè.
- **Đề tổng hợp 11–18:**
  - `generate_11_18_exam.py`: dữ liệu đề chuyển từ PDF.
  - `build_full_exam_11_18_system.py`: dữ liệu bộ đề bổ sung và kiểm tra cấu trúc.
  - `build_tong_hop_11_18_page.py`: template HTML.
  - `assets/js/pages/de_thi_tong_hop_11_18.js`: controller chuẩn, chỉnh trực tiếp.
  - `build_tong_hop_11_18_js.py`: chỉ xác nhận cú pháp controller, không sinh đè JS.
- **Dữ liệu tiến độ:** giữ ID câu và có migration nếu đổi cấu trúc checkpoint.
- **Nội dung đã biên tập Bài 3–18:** các ghi đè lý thuyết/quiz nằm trong `scripts/lesson_content_review.py`;
  `scripts/build_lesson_content.py` cập nhật vào trang hiện tại và được gọi bởi `build_all.py`.
  Câu hỏi là bài tự luyện theo chủ điểm, không phải đề chính thức. Chi tiết phạm vi đã đối chiếu:
  [báo cáo chất lượng nội dung](docs/reviews/CONTENT_QUALITY_2026_11.md).
- **Tài nguyên local:** để PDF trong `docs/pdf/`, báo cáo trong `docs/reviews/`, ảnh thử nghiệm trong `artifacts/screenshots/`.

## Trước khi gửi thay đổi

- Chạy build, regression checks và browser tests.
- Kiểm tra desktop/mobile, menu, tab, tìm kiếm và điều hướng bằng bàn phím.
- Thử nhập tiếng Nhật bằng IME, chấm bài, reload và làm lại.
- Đảm bảo dữ liệu mới không làm mất checkpoint cũ.
- Đối chiếu nội dung/đáp án với tài liệu học. Test kỹ thuật không xác nhận mọi câu tiếng Nhật hoặc tính tương đương với đề thi chính thức.

## Tài liệu kỹ thuật

- [Quy ước cấu trúc dự án](docs/PROJECT_STRUCTURE.md)
- [Rà soát code ban đầu](docs/reviews/CODE_REVIEW.md)
- [Kiểm tra lại và kết quả sửa](docs/reviews/RECHECK_CURRENT.md)
