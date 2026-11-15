# Marugoto A1–A2 Interactive Study Hub

Nền tảng ôn tập Marugoto A1 (L3–18) & A2-1 (L1–18): Từ vựng, Kanji, Ngữ pháp, Luyện gõ phản xạ tiếng Nhật thông minh (tự lưu checkpoint `localStorage`), và Bộ Đề Thi Thử 100 điểm.

## Cấu trúc dự án

```text
.
├── index.html                        # Cổng chính
├── Tu_Vung_Marugoto_A1_16_A2_1_10.html
├── Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html
├── kanji_a2.html
├── kien_thuc_bo_sung.html
├── the_nai.html / the_ta.html / the_ru.html
├── demo_3d.html
├── lessons/                          # 18 trang bài học Marugoto A2 (Lesson 1..18)
├── tests/                            # Đề thi thử, dịch câu & Luyện gõ L11–18
│   └── On_Tap_Mini_Test_A2_15_18.html#typing
├── assets/
│   ├── nav.js                        # Thanh điều hướng dùng chung & tải checkpoint-sync
│   ├── css/                          # Stylesheet dùng chung & theo module
│   │   ├── pages/                    # CSS tách riêng cho từng trang
│   │   └── *.css
│   ├── js/                           # Engine JS thuần đã chuẩn hóa
│   │   ├── jp-typing-grader.js       # Bộ chấm tiếng Nhật linh hoạt (đảo phó từ/bổ ngữ, Katakana, số, suru-V)
│   │   ├── typing-studio.js          # Studio luyện gõ Câu (112 câu L11-18) / Kanji (119 chữ) / Từ vựng
│   │   ├── typing-practice.js        # Luyện gõ từ vựng trong các bài Lesson 1..18
│   │   ├── checkpoint-sync.js        # Tự động lưu & khôi phục bài làm qua localStorage
│   │   ├── audio-engine.js           # Phát âm Web Speech API tiếng Nhật
│   │   ├── lessons/                  # JS & data của từng bài Lesson 1..18
│   │   └── pages/                    # JS tách riêng cho từng trang
│   └── data/                         # Dữ liệu JSON-JS đã tách khỏi HTML (chạy tốt cả file:// & http://)
├── data/                             # Dữ liệu JSON gốc phục vụ script build
├── docs/                             # Kế hoạch ôn 10 ngày & tài liệu PDF
│   └── pdf/                          # Giáo trình Wordbook & PDF L11–L18 trên lớp
└── scripts/                          # Bộ generator Python chuẩn
    ├── build_all.py                  # Chạy build + kiểm tra toàn vẹn HTML/JS/asset
    ├── build_mini_test_15_18.py
    ├── build_mini_test_11_14.py
    ├── build_cram_kanji_11_18.py
    ├── l15_18_typing_data.py
    └── mini_test_15_18_exams.py
```

## Cách chạy & kiểm tra trên máy

1. **Mở server local để test:**
   ```zsh
   python3 -m http.server 8000
   ```
   Sau đó truy cập `http://localhost:8000/tests/On_Tap_Mini_Test_A2_15_18.html#typing`.

2. **Build lại đề thi / dữ liệu luyện gõ & kiểm tra toàn vẹn source:**
   ```zsh
    python3 scripts/build_all.py
    ```

3. **Kiểm tra logic và luồng sử dụng trên trình duyệt:**
   ```zsh
   node tests/run_regression_tests.js
   python3 -m pip install -r tests/requirements-browser.txt
   python3 -m playwright install chromium
   python3 tests/test_browser.py
   ```
   Browser tests dùng server local và profile tạm, không đụng đến tiến độ học trên trình duyệt của bạn.
   Có thể dùng Google Chrome đã cài thay cho Chromium. Để chọn binary khác, đặt `CHROME_PATH`.
   Để xuất ảnh kiểm tra responsive, đặt `MARUGOTO_SCREENSHOTS_DIR` trỏ tới thư mục ảnh mong muốn.

## Nguồn build và tiến độ học

- `scripts/build_all.py` bao gồm cả dữ liệu và trang đề tổng hợp bài 11–18.
- Controller `assets/js/pages/de_thi_tong_hop_11_18.js` là source được chỉnh trực tiếp.
  Script `build_tong_hop_11_18_js.py` chỉ kiểm tra cú pháp, không ghi đè controller bằng bản sao cũ.
- Phiên thi tổng hợp lưu theo mã đề, gồm đáp án, các mảnh câu đang xếp, chế độ,
  thời gian và trạng thái nộp. Đồng hồ tiếp tục tính khi rời trang, trừ khi đã bấm tạm dừng.
- Checkpoint cũ được giữ và chuyển đổi khi đọc; không cần xóa toàn bộ lịch sử để cập nhật.
- Trong bài học có mục **“Mục lục & học theo từng phần”**: chọn xem một phần hoặc toàn bài.
