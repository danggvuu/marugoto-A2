# Quy ước cấu trúc dự án

## Tách website, nguồn dữ liệu và công cụ

| Thư mục | Trách nhiệm |
| --- | --- |
| Root HTML, `lessons/`, `tests/` | Trang người dùng mở trên trình duyệt |
| `assets/` | CSS, JS và dữ liệu được website tải |
| `data/` | Dữ liệu nguồn; `data/extracted/` dành cho trích xuất tạm |
| `scripts/` | Generator và kiểm tra build |
| `qa/` | Test tự động và dependency dành riêng cho test |
| `docs/` | Tài liệu, PDF và báo cáo rà soát |
| `artifacts/` | Ảnh/kết quả kiểm tra cục bộ, được Git bỏ qua |

## Vì sao vẫn giữ `tests/*.html`?

Đây là tên thư mục lịch sử của **đề luyện tập**, không phải unit test. Đường dẫn
đang được dùng trong thanh điều hướng, generator, bookmark và khóa `localStorage`.
Lượt sắp xếp này giữ nguyên chúng để bảo toàn link và tiến độ.

Test tự động được chuyển sang:

- `qa/regression/run_regression_tests.js`
- `qa/browser/test_browser.py`
- `qa/requirements-browser.txt`

## Các đường dẫn đã chuyển

| Trước | Sau |
| --- | --- |
| `tests/run_regression_tests.js` | `qa/regression/run_regression_tests.js` |
| `tests/test_browser.py` | `qa/browser/test_browser.py` |
| `tests/requirements-browser.txt` | `qa/requirements-browser.txt` |
| `docs/CODE_REVIEW.md` | `docs/reviews/CODE_REVIEW.md` |
| `docs/RECHECK_CURRENT.md` | `docs/reviews/RECHECK_CURRENT.md` |
| `De_on_tap_JLPT_A2_Bai_11-18.pdf` | `docs/pdf/De_on_tap_JLPT_A2_Bai_11-18.pdf` |
| `extracted_pdf_test.txt` | `data/extracted/extracted_pdf_test.txt` |
| `screenshots/` | `artifacts/screenshots/` |

File trích xuất và screenshot được giữ lại trên máy, không xóa. Các đường dẫn
nhắc tới vị trí cũ trong nội dung báo cáo lịch sử chỉ là ghi nhận tại thời điểm audit.

## Nguyên tắc thêm file

1. Không để screenshot, bản OCR hoặc output thử nghiệm ở root.
2. Không dùng cùng tên cho test tự động và trang đề thi.
3. Không di chuyển thư viện vendor hoặc tài liệu học khi chưa kiểm tra nơi dùng.
4. Giữ generator và đầu ra đồng bộ; build rồi kiểm tra `git diff`.
5. Khi đổi URL trang học, cần kế hoạch chuyển tiếp link và migration checkpoint,
   không chỉ sửa tên thư mục.
