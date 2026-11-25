# Marugoto A1–A2 Study Hub

Website tự học tiếng Nhật bằng tiếng Việt, chạy bằng **HTML, CSS và JavaScript thuần**. Dự án có **36 trang bài học: 18 bài Marugoto A2.1 và 18 bài A2.2**, cùng kho từ vựng A1/A2.1, Kanji, ngữ pháp, luyện gõ, Kaiwa và đề ôn tập.

Không cần backend, tài khoản hay npm để chạy website. Tiến độ lưu bằng `localStorage` trên trình duyệt. Các bài tập phục vụ tự luyện, **không phải đề thi hoặc chứng nhận JLPT chính thức**.

## Chạy nhanh

Cần **Python 3** và trình duyệt hiện đại. Tại thư mục dự án:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Truy cập **http://localhost:8000/**. Không cần build trước khi học bằng các file đã có; nên dùng HTTP server thay vì mở bằng `file://`.

## Nội dung chính

| Phần | Phạm vi |
| --- | --- |
| Bài học | A2.1 bài 1–18 và A2.2 bài 1–18; lý thuyết, từ vựng, Kanji và bài tự luyện |
| Kho từ vựng | A1 bài 3–18 và A2.1 bài 1–18; tìm kiếm, lọc bài, flashcard và quiz |
| A2.2 | Từ vựng nằm trong từng bài học; 439 thẻ từ vựng, 270 câu quiz và 181 mục từ Kanji trên 18 bài |
| Kanji | Tra cứu, lọc bài A2.1/A2.2, thứ tự nét SVG và tập viết |
| Ngữ pháp và Typing Studio | Mẫu câu, chia động từ, Verb Lab, luyện dịch và gõ tiếng Nhật |
| Đề ôn tập | Mini test A2.1, Midterm, tổng hợp A2.1 bài 11–18 và mini test A2.2 bài 1–4 |
| Kaiwa và 3D Lab | Luyện hội thoại theo chủ đề và không gian tương tác bằng Three.js |

### Đường dẫn nhanh

- [Trang chủ](index.html)
- [Bắt đầu A2.1](lessons/Marugoto_A2_Lesson_1.html) · [Bắt đầu A2.2](lessons/Marugoto_A2_2_Lesson_1.html)
- [Kho từ vựng A1/A2.1](Tu_Vung_Marugoto_A1_16_A2_1_10.html) · [Kanji & luyện viết](kanji_a2.html)
- [Ngữ pháp](Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html) · [Luyện gõ](tests/On_Tap_Mini_Test_A2_15_18.html#typing)
- [Tổng hợp A2.1 bài 11–18](tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html) · [Kiểm tra riêng Từ vựng & Kanji 11–18](tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html#vocab-kanji-check)
- [Mini test A2.2 bài 1–4](tests/On_Tap_Mini_Test_A2_2_1_4.html)
- [Kaiwa 5 phút](Luyen_Kaiwa_5_Phut.html) · [3D Lab](demo_3d.html)

## Tiến độ và kết nối mạng

- Tiến độ chỉ thuộc **trình duyệt, thiết bị và origin hiện tại**, chưa đồng bộ tài khoản. `localhost`, `127.0.0.1` và các cổng khác nhau có vùng lưu riêng.
- Xóa dữ liệu website, dùng cửa sổ riêng tư hoặc chặn storage có thể làm mất tiến độ. Đọc phạm vi và xác nhận trước khi làm lại hoặc xóa checkpoint.
- Đề tổng hợp 11–18 lưu phiên riêng theo mã đề. Đồng hồ vẫn tính khi rời trang, trừ khi đã tạm dừng; chế độ thi chỉ mở lời giải sau khi nộp.
- Kiểm tra riêng Từ vựng & Kanji 11–18 lọc theo bài/loại, chấm ngay và ôn câu sai. Phiên lưu riêng, không cộng vào đề 71 câu; mở tab này tạm dừng đồng hồ đề tổng hợp. Kanji được giới hạn cả từ đích lẫn đáp án nhiễu theo tập chữ bài 11–18.
- Nội dung chính là file local, nhưng font, dịch vụ phát âm và dữ liệu nét Kanji có thể cần mạng. Giọng đọc phụ thuộc thiết bị; không coi đây là ứng dụng offline hoàn toàn.

## Cấu trúc dự án

```text
.
├── index.html                 # Trang chủ
├── *.html                     # Tra cứu, ngữ pháp, Kaiwa, 3D
├── lessons/                   # 18 trang A2.1 + 18 trang A2.2
├── tests/                     # Trang đề ôn tập cho người học
├── assets/                    # CSS, JS, dữ liệu runtime, ảnh và vendor
├── data/                      # JSON nguồn và dữ liệu trung gian cho công cụ
├── scripts/                   # Generator Python và kiểm tra build
│   └── a2_2/                  # Nguồn nội dung và generator 18 bài A2.2
├── qa/                        # Kiểm thử tự động, không phải tests/*.html
│   ├── regression/            # Node.js: logic, nội dung và phạm vi dữ liệu
│   ├── browser/               # Python + Playwright
│   └── requirements-browser.txt
├── docs/                      # Tài liệu kỹ thuật, PDF, lộ trình và báo cáo
└── artifacts/                 # Output tạo khi thử local, được Git bỏ qua
```

Chi tiết vai trò thư mục và nguồn biên tập: [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md). Giữ URL HTML và ID checkpoint cũ khi chưa có kế hoạch chuyển tiếp/migration.

## Build và kiểm tra

Chạy các lệnh dưới đây tại thư mục gốc. **Python 3 và Node.js** phải có trong `PATH`; Playwright chỉ cần cho browser tests.

### 1. Build dữ liệu và trang được sinh

```sh
python3 scripts/build_all.py
```

Pipeline hiện tại:

1. Cập nhật nội dung A2.1 bài 3–18; sinh 18 bài A2.2 cùng JS bài học, đồng bộ Kanji và điều hướng A2.2.
2. Sinh mini test A2.2 bài 1–4, mini test A2.1 bài 11–14/15–18, ôn Kanji cấp tốc, kiểm tra Từ vựng & Kanji và đề tổng hợp 11–18.
3. Kiểm tra tham chiếu local, cấu trúc HTML và `script` tại root, `lessons/`, `tests/` và lộ trình 10 ngày; chạy `node --check` cho JS trong `assets/`.
4. Chạy toàn bộ regression về nội dung, checkpoint, phiên thi, timer, Kanji, vòng đời 3D và các script build phụ.

**Build ghi lại các file đầu ra**, gồm cả một số file dùng chung. Xem `git diff` sau khi chạy. Không phải mọi script trong `scripts/` đều được gọi bởi pipeline này.

### 2. Regression checks không sinh lại trang

```sh
python3 scripts/build_all.py --check-only
```

Lệnh này không chạy generator hoặc ghi lại trang/dữ liệu. Nó kiểm tra HTML/JS, chạy các regression cũ và mới, xác nhận đầu ra A2.2 khớp nguồn; test script phụ chỉ ghi vào workspace tạm. Có thể chạy riêng từng file trong `qa/regression/` khi debug. Các test gồm hành vi controller và một số kiểm tra dò source, không thay thế kiểm tra trên trình duyệt hay đối chiếu nội dung tiếng Nhật.

### 3. Browser tests

Khuyến nghị tạo môi trường riêng:

```sh
python3 -m venv .venv
```

Kích hoạt trên macOS/Linux:

```sh
source .venv/bin/activate
```

Hoặc Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cài và chạy:

```sh
python -m pip install -r qa/requirements-browser.txt
python -m playwright install chromium
python -m unittest discover -s qa/browser -p 'test_*.py' -v
```

Test tự mở HTTP server và browser context tạm, không dùng tiến độ trong profile cá nhân. Nếu thiếu Chromium của Playwright, test thử dùng Google Chrome đã cài. Bộ test gồm điều hướng A2.2, flashcard, quiz/Verb Lab, Kanji, lọc/phân trang, checkpoint, xếp câu, timer và khóa lời giải. Smoke test mở toàn bộ 69 trang ở 360 và 1440px, phát hiện lỗi JS, HTTP local và tràn ngang; trang đại diện còn được kiểm tra ở 390 và 768px.

`test_review_visual_flows.py` kiểm tra filter/paging Kanji, response SVG đảo thứ tự và mở/đóng 3D bằng renderer Three.js thật. Nếu browser không hỗ trợ WebGL, test 3D báo **skip**, không coi là đã kiểm chứng GPU. Chạy suite bằng lệnh discovery phía trên để không bỏ sót file test này.

| Biến môi trường | Ý nghĩa |
| --- | --- |
| `CHROME_PATH` | Đường dẫn binary Chrome/Chromium tùy chỉnh |
| `MARUGOTO_SCREENSHOTS_DIR` | Thư mục lưu ảnh responsive |

Ví dụ macOS/Linux:

```sh
MARUGOTO_SCREENSHOTS_DIR=artifacts/screenshots/latest python -m unittest discover -s qa/browser -p 'test_*.py' -v
```

## Chỉnh sửa và đóng góp

- Sửa đúng nguồn theo [quy ước cấu trúc](docs/PROJECT_STRUCTURE.md), rồi build nếu thay đổi phần được sinh. Không chỉ sửa HTML/JS đầu ra vì lần build sau có thể ghi đè.
- Trước khi gửi thay đổi: chạy build, regression và browser tests; xem `git diff`, thử desktop/mobile, bàn phím/IME, chấm bài, reload và làm lại.
- Giữ ID câu hỏi và migration checkpoint khi đổi dữ liệu. Đối chiếu đáp án với tài liệu học, không suy ra độ chính xác học thuật chỉ từ test kỹ thuật.
- PDF nguồn ở `docs/pdf/`, báo cáo ở `docs/reviews/`, ảnh thử nghiệm ở `artifacts/screenshots/`.

## Tài liệu kỹ thuật

- [Quy ước cấu trúc dự án](docs/PROJECT_STRUCTURE.md)
- [Rà soát code ban đầu](docs/reviews/CODE_REVIEW.md)
- [Kiểm tra lại và kết quả sửa](docs/reviews/RECHECK_CURRENT.md)
- [Đối chiếu chất lượng nội dung A2.1](docs/reviews/CONTENT_QUALITY_2026_11.md)
- [Các lỗi đã sửa và kiểm chứng ngày 25/11/2026](docs/reviews/FIXES_2026_11_25.md)

Các báo cáo rà soát phản ánh thời điểm viết, không thay thế mô tả cấu trúc hiện tại.
