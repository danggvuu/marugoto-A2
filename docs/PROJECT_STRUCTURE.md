# Cấu trúc dự án

Website static **HTML/CSS/JavaScript thuần**, có **18 bài Marugoto A2.1 + 18 bài A2.2**. Không có backend hoặc bước biên dịch TypeScript/React để chạy website. Xem [README](../README.md#build-và-kiểm-tra) để chạy local, build và kiểm thử.

## Vai trò thư mục

| Đường dẫn | Trách nhiệm |
| --- | --- |
| `index.html`, các HTML tại root | Trang chủ, từ vựng A1/A2.1, Kanji, ngữ pháp, Kaiwa và 3D |
| `lessons/Marugoto_A2_Lesson_1.html` … `Marugoto_A2_Lesson_18.html` | 18 trang A2.1 |
| `lessons/Marugoto_A2_2_Lesson_1.html` … `Marugoto_A2_2_Lesson_18.html` | 18 trang A2.2 |
| `tests/` | HTML đề ôn tập dành cho người học, **không phải test tự động** |
| `assets/nav.js` | Điều hướng chung; danh sách A2.2 được generator cập nhật |
| `assets/css/`, `assets/js/` | Giao diện, logic dùng chung, controller từng trang và từng bài |
| `assets/data/`, `assets/img/`, `assets/js/vendor/` | Dữ liệu JS trình duyệt nạp, ảnh và thư viện bên thứ ba |
| `data/` | JSON nguồn/tham chiếu và dữ liệu trung gian cho generator/QA, không phải kho dữ liệu runtime chính |
| `scripts/`, `scripts/a2_2/` | Generator Python, nguồn nội dung và kiểm tra build |
| `qa/regression/` | Kiểm tra Node.js về logic, nội dung và phạm vi dữ liệu |
| `qa/browser/`, `qa/requirements-browser.txt` | Browser tests Python + Playwright và dependency riêng cho test |
| `docs/pdf/` | PDF nguồn phục vụ học và đối chiếu |
| `docs/reviews/` | Báo cáo rà soát theo thời điểm viết |
| `docs/Ke_Hoach_10_Ngay/` | Lộ trình ôn tập 10 ngày |
| `artifacts/`, `data/extracted/` (tùy chọn) | Thư mục output tạo khi kiểm tra/trích xuất cục bộ, được Git bỏ qua |

## Sửa đúng nguồn

### Bài học A2.1

- Trang tại `lessons/Marugoto_A2_Lesson_*.html`; JS tại `assets/js/lessons/lesson_01.js` đến `lesson_18.js`.
- Nội dung lý thuyết/quiz đã biên tập bài 3–18 nằm trong `scripts/lesson_content_review.py`; `scripts/build_lesson_content.py` cập nhật các trang/JS hiện có, không tạo lại toàn bộ website.
- Phạm vi đối chiếu: [báo cáo chất lượng nội dung](reviews/CONTENT_QUALITY_2026_11.md).

### Bài học A2.2

- Pipeline chính: `scripts/a2_2/build_all_a2_2.py`.
- `scripts/a2_2/topic_01.py` đến `topic_09.py`: dữ liệu theo 9 chủ đề; `scripts/a2_2/official_curriculum.py`: ghi đè ngữ pháp, quiz và gắn danh sách Kanji tham chiếu.
- `data/kanji_vocab_a2_2_official.json`: danh sách Kanji tham chiếu mà build bài học nạp trực tiếp. `data/vocab_a2_2_official.json` được mini test A2.2 nạp; từ vựng từng bài nằm trong các module `topic_*.py`.
- Khi cập nhật bộ từ vựng, xem `scripts/a2_2/build_full_439_vocab.py` và `scripts/a2_2/update_official_pdf_vocab.py` để đồng bộ JSON và module chủ đề; bước này không tự chạy trong build tổng. `scripts/a2_2/generator_core.py` giữ template HTML và JS.
- Build sinh lại 18 HTML A2.2, 18 file `assets/js/lessons/lesson_a2_2_*.js`, `data/kanji_vocab_a2_2.json`; đồng thời cập nhật `assets/data/kanji_a2_data.js`, `kanji_a2.html` và danh sách A2.2 trong `assets/nav.js`.
- Kho từ vựng chung vẫn dùng `assets/data/master_vocab_a1_a2.js` cho A1/A2.1; từ vựng A2.2 được học trong từng trang bài học.

### Đề tổng hợp và bài ôn

| Phần | Nguồn cần sửa |
| --- | --- |
| Dữ liệu đề gốc A2.1 bài 11–18 | `scripts/generate_11_18_exam.py` |
| Bộ đề bổ sung và kiểm tra cấu trúc | `scripts/build_full_exam_11_18_system.py` |
| HTML đề tổng hợp | `scripts/build_tong_hop_11_18_page.py` |
| Controller đề tổng hợp | `assets/js/pages/de_thi_tong_hop_11_18.js`, chỉnh trực tiếp; `scripts/build_tong_hop_11_18_js.py` chỉ kiểm tra cú pháp, không sinh đè |
| Kiểm tra riêng Từ vựng & Kanji 11–18 | `scripts/build_vocab_kanji_check_11_18.py`, controller `assets/js/pages/vocab-kanji-check-11-18.js` |
| Mini test A2.1 bài 11–14/15–18 | `scripts/build_mini_test_11_14.py`, `scripts/build_mini_test_15_18.py` và các module dữ liệu được import |
| Mini test A2.2 bài 1–4 | `scripts/build_mini_test_a2_2_1_4.py` |
| Luyện nhập kana A2.2 bài 1–4, mỗi bài 20 câu | `scripts/a2_2/kana_review_content.py`; hiển thị và lưu tiến độ trong controller `assets/js/mini-test-a2-2-1-4.js` |

`tests/*.html` là URL lịch sử đang được điều hướng và checkpoint sử dụng. Giữ nguyên đường dẫn để bảo toàn bookmark và tiến độ; không chuyển chúng sang `qa/`.

## Build và QA

Tại root:

```sh
python3 scripts/build_all.py
# Chỉ kiểm tra, không chạy generator:
python3 scripts/build_all.py --check-only
```

`build_all.py` vừa **ghi lại đầu ra** vừa kiểm tra 69 trang HTML/88 JS và chạy các regression về runtime, nội dung, checkpoint, phiên thi, Kanji, 3D cùng script build phụ. `--check-only` chạy cùng kiểm tra nhưng bỏ qua generator; đầu ra A2.2 vẫn phải khớp nguồn hiện tại. Danh sách `BUILDERS` và `REGRESSION_CHECKS` trong script xác định pipeline chính thức, không mặc định mọi generator đều nằm trong build tổng.

Browser tests và cài môi trường: [hướng dẫn trong README](../README.md#3-browser-tests). Test kỹ thuật không thay thế kiểm tra đáp án với tài liệu học hoặc thử bàn phím/IME thực tế.

## Nguyên tắc giữ cấu trúc

1. Sửa nguồn generator trước đầu ra, build lại và xem `git diff`.
2. Giữ ID câu hỏi và khóa `localStorage`; cần migration nếu thay đổi cấu trúc checkpoint hoặc URL.
3. Không để screenshot/OCR/output tạm ở root; dùng `artifacts/` hoặc `data/extracted/`.
4. Không di chuyển/xóa dữ liệu nguồn, thư viện vendor hoặc tài liệu học khi chưa kiểm tra toàn bộ nơi tham chiếu.
5. Báo cáo trong `docs/reviews/` có thể nhắc đường dẫn cũ tại thời điểm audit; không dùng chúng để suy ra cấu trúc runtime hiện tại.
