# 🚀 CHỈ ĐẪN NÂNG CẤP DỰ ÁN V2 VỚI META ASTRYX DESIGN SYSTEM (REACT 19 + STYLEX)

> **Dành cho AI Agent (jcode / GPT-6.1 Sol)**:
> Đọc kỹ toàn bộ tệp tài liệu này trước khi thực thi. Đây là kế hoạch nâng cấp giao diện v2 của ứng dụng học tiếng Nhật Marugoto sang **Astryx Design System** chính thức của Meta (`@astryxdesign/core`, `@astryxdesign/theme-neutral`, `@stylexjs/stylex`).

---

## 🎯 1. NGUYÊN TẮC CỐT LÕI (BẮT BUỘC TUÂN THỦ)

1. **BẢO TOÀN DỰ ÁN HIỆN TẠI (V1 ZERO-BREAKAGE)**:
   - Toàn bộ website v1 hiện tại (các tệp `index.html`, thư mục `lessons/`, `assets/`, `scripts/`, `qa/`) **KHÔNG ĐƯỢC PHÉP XOÁ HOẶC LÀM HỎNG**.
   - Mọi mã nguồn của phiên bản v2 sẽ được xây dựng độc lập trong thư mục con: `v2/`.
   - Khi chạy `python3 scripts/build_all.py` ở thư mục gốc, toàn bộ bài học và kiểm thử của v1 vẫn phải chạy đạt 100% PASS.

2. **TÁI SỬ DỤNG NGUỒN DỮ LIỆU ĐÃ CHUẨN HOÁ**:
   - Tái sử dụng dữ liệu từ v1 thay vì hardcode lại:
     - Từ vựng A2-2 chính thức (382 thẻ): `../data/vocab_a2_2_official.json`
     - Chữ Hán A2-2 chính thức (170 chữ Hán): `../data/kanji_vocab_a2_2_official.json`
     - Từ vựng phong phú A1 & A2-1: `../data/master_vocab_enriched.json`

---

## 🛠️ 2. CÔNG NGHỆ & THƯ VIỆN YÊU CẦU

- **Framework**: React 19 (`react@^19.0.0`, `react-dom@^19.0.0`)
- **Language**: TypeScript (`typescript`, `@types/react`, `@types/react-dom`)
- **Bundler**: Vite (`vite`, `@vitejs/plugin-react`)
- **Design System của Meta**:
  - `@astryxdesign/core` (Hệ thống component cốt lõi của Meta)
  - `@astryxdesign/theme-neutral` (Bộ design token và theme)
  - `@stylexjs/stylex` (Styling engine compile-time của Meta)
  - `@astryxdesign/cli` (Tùy chọn, phục vụ swizzling hoặc sinh component)
- **Icons / UI Utils**: `lucide-react` (nếu cần bổ sung icon phụ trợ)

---

## 📋 3. PHẠM VI TRIỂN KHAI CHO GIAI ĐOẠN 1 (PROTOTYPE SCOPE)

Xây dựng ứng dụng hoàn chỉnh trong thư mục `v2/` gồm các màn hình và thành phần sau:

### A. Khởi tạo Dự án `v2/`
1. Khởi tạo Vite project với template React + TypeScript tại thư mục `v2/`.
2. Cài đặt các dependencies:
   ```bash
   cd v2
   npm install react@^19.0.0 react-dom@^19.0.0
   npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex lucide-react
   npm install -D vite @vitejs/plugin-react typescript @types/react @types/react-dom
   ```
3. Cấu hình Vite (`vite.config.ts`), import stylesheet cơ sở của Astryx (`@astryxdesign/core/dist/index.css` hoặc qua StyleX).

### B. Layout Tổng thể (App Shell)
- **App Header**:
  - Logo ứng dụng học tiếng Nhật Marugoto A1–A2.
  - Tab chuyển đổi cấp độ: A1, A2-1, A2-2.
  - Nút chuyển đổi Dark / Light mode (sử dụng tokens của `@astryxdesign/theme-neutral`).
- **Sidebar / Navigation Rail**:
  - Danh sách bài học theo Topic (Topic 1 đến Topic 9 của A2-2).
  - Trạng thái hoàn thành bài học (lưu qua `localStorage`).

### C. Màn hình Bài học Mẫu: Marugoto A2-2 Bài 1 (Lesson 1 Prototype)
Trang học bài mẫu với giao diện Astryx hiện đại, bao gồm:
1. **Hero Header**:
   - Tên bài: 「いいなまえですね」
   - Câu trích dẫn kèm nút phát âm (Web Speech API tiếng Nhật `ja-JP`).
   - Badge thống kê: Số từ vựng, điểm Kanji, cấu trúc ngữ pháp.
2. **Flashcard Studio**:
   - Sử dụng Card component của Astryx với hiệu ứng lật 3D mượt mà.
   - Hiển thị đầy đủ: Chữ Hán, Kana, Romaji, Nghĩa tiếng Việt, Audio phát âm tự động khi chuyển thẻ.
   - Điều hướng: Thẻ trước, Thẻ sau, Tự động chạy (Auto-play), Xáo trộn (Shuffle).
3. **Cẩm nang Ngữ pháp (Grammar Explorer)**:
   - Trình bày dạng Accordion / Tabs chuẩn Astryx:
     - ① `N という意味` (Ý nghĩa của tên gọi)
     - ② `N1 という N2` (Giới thiệu tên người/địa danh)
     - ③ `Thể thông thường ＋ N` (Mệnh đề định ngữ)
   - Bảng công thức và hội thoại ví dụ mẫu song ngữ Nhật - Việt có nút nghe từng câu.
4. **Kho chữ Hán (Kanji Detail Cards)**:
   - Các chữ Hán chính thức của Bài 1 (紹介, 自己紹介, 名前, 有名, 意味, 本屋, 近所, 住所...).
   - Hiển thị âm Hán Việt, cách đọc On/Kun, số nét và từ vựng ví dụ.
5. **Interactive Quiz Engine (Phòng Luyện Thi 15 Câu)**:
   - Lấy đúng bộ câu hỏi quiz của Bài 1 (Chữ Hán, Ngữ pháp, Từ vựng, Hội thoại).
   - Chọn đáp án 4 lựa chọn (A, B, C, D) với phản hồi tức thì (xanh khi đúng, đỏ khi sai).
   - Giải thích chi tiết cho từng câu hỏi và hiển thị bảng tổng kết điểm số.

---

## 🧪 4. KIỂM THỬ & TIÊU CHÍ HOÀN THÀNH (ACCEPTANCE CRITERIA)

Một phiên làm việc thành công khi:
1. Thư mục `v2/` độc lập, chạy được lệnh:
   ```bash
   cd v2
   npm run build # Build thành công không có lỗi TypeScript / JSX
   ```
2. Khởi chạy dev server:
   ```bash
   npm run dev # Mở được http://localhost:5173 trên trình duyệt
   ```
3. Giao diện hiển thị đúng các component chuẩn của Meta Astryx (nút bấm, card, modal/dialog, typography, spacing).
4. Các tính năng tương tác (Lật thẻ flashcard, Phát âm giọng Nhật Web Speech API, Làm quiz tính điểm) hoạt động trơn tru.
5. Chạy kiểm tra lại thư mục gốc:
   ```bash
   cd ..
   python3 scripts/build_all.py # Vẫn PASS 100% toàn bộ 103 regression tests
   ```

---

*Tài liệu được khởi tạo trên nhánh `feat/astryx-v2` phục vụ cho AI Agent `jcode` tiếp quản và thực hiện.*
