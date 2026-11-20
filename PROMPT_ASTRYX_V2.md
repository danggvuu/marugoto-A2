# 🏛️ ĐẠI KẾ HOẠCH ĐẬP ĐI XÂY LẠI TOÀN BỘ DỰ ÁN VỚI META ASTRYX DESIGN SYSTEM (REACT 19 + STYLEX)

> **Dành cho AI Agent (jcode / GPT-6.1 Sol)**:
> Người dùng đã yêu cầu **ĐẬP ĐI XÂY LẠI TOÀN BỘ (Full Architecture Rewrite)** dự án trên nhánh `feat/astryx-v2`. 
> Chúng ta sẽ chuyển đổi toàn bộ 59 trang HTML tĩnh và 85 tệp JavaScript cũ thành một **Single Page Application (SPA)** hiện đại bậc nhất, ứng dụng trọn vẹn **Meta Astryx Design System** (`@astryxdesign/core`, `@astryxdesign/theme-neutral`, `@stylexjs/stylex`) kết hợp **React 19**, **TypeScript** và **Vite**.
>
> *(Lưu ý: Nhánh `main` đã được commit an toàn, nhánh `feat/astryx-v2` hoàn toàn tự do để tái cấu trúc toàn diện).*

---

## 🧭 1. KIẾN TRÚC MỤC TIÊU CỦA ỨNG DỤNG MỚI

```
nhật/
├── index.html                 # Entry HTML cho Vite SPA
├── vite.config.ts             # Cấu hình Vite + React 19 + StyleX
├── tsconfig.json              # TypeScript compiler config
├── package.json               # Dependencies: React 19, Astryx, StyleX, React Router...
├── src/
│   ├── main.tsx               # App entry point
│   ├── App.tsx                # Routing & Theme Provider
│   ├── styles/
│   │   ├── tokens.stylex.ts   # StyleX design tokens mở rộng từ Astryx
│   │   └── global.css         # Reset & Astryx core CSS
│   ├── layouts/
│   │   ├── AppShell.tsx       # Header, Responsive Sidebar Rail, Footer
│   │   ├── Header.tsx         # Logo, Dark/Light Mode Switcher, Quick Search
│   │   └── NavRail.tsx        # Thanh điều hướng nhanh cấp độ (A1, A2-1, A2-2)
│   ├── components/
│   │   ├── common/            # Nút bấm, Badge, Modal, Tooltip của Astryx
│   │   ├── flashcard/         # Thẻ học từ vựng 3D Flip Card, Audio Speech, Autoplay
│   │   ├── grammar/           # Khối công thức ngữ pháp Accordion, ví dụ song ngữ Nhật-Việt
│   │   ├── kanji/             # Thẻ Kanji chi tiết, âm Hán Việt, cách nhớ, nét viết
│   │   ├── quiz/              # Trắc nghiệm 15 câu, chấm điểm tức thì, giải thích chi tiết
│   │   └── typing/            # Studio luyện gõ phím tiếng Nhật (Romaji -> Kana/Kanji)
│   ├── pages/
│   │   ├── HomePage.tsx       # Dashboard tổng quan, tiến độ học, chọn lộ trình
│   │   ├── LessonPage.tsx     # Trang bài học đa năng (dùng chung cho cả 36 bài A2-1 & A2-2)
│   │   ├── KanjiHubPage.tsx   # Trung tâm tra cứu & luyện 291 từ Kanji (121 A2-1 + 170 A2-2)
│   │   ├── ExamPage.tsx       # Trung tâm đề thi JLPT tổng hợp & Mini Test
│   │   └── KaiwaPage.tsx      # Luyện phản xạ giao tiếp Kaiwa 5 phút
│   ├── services/
│   │   ├── speech.ts          # Web Speech API chuẩn giọng Nhật (ja-JP)
│   │   ├── progress.ts        # Quản lý lưu tiến độ học tập vào LocalStorage
│   │   └── dataLoader.ts      # Bộ nạp dữ liệu chuẩn từ thư mục data/
│   └── types/                 # Interface cho Vocab, Grammar, Kanji, Quiz
└── data/                      # TẬP DỮ LIỆU NGUỒN CHUẨN (GIỮ NGUYÊN ĐỂ SPA ĐỌC)
    ├── vocab_a2_2_official.json       # 382 từ vựng chuẩn 18 bài A2-2
    ├── kanji_vocab_a2_2_official.json # 170 mục Kanji chuẩn A2-2
    └── master_vocab_enriched.json     # Dữ liệu từ vựng A1 và A2-1
```

---

## 📦 2. BỘ DEPENDENCIES CẦN CÀI ĐẶT

Tại thư mục gốc dự án:
```bash
npm init -y
npm install react@^19.0.0 react-dom@^19.0.0 react-router-dom@^6.28.0
npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex lucide-react canvas-confetti
npm install -D vite @vitejs/plugin-react typescript @types/react @types/react-dom @types/canvas-confetti
```

---

## ⚡ 3. CÁC TÍNH NĂNG CỐT LÕI CẦN TRIỂN KHAI

### ① Dashboard Trang Chủ (`HomePage.tsx`)
- Thống kê tiến độ trực quan: Số từ vựng đã học, số câu trắc nghiệm đã làm, số chữ Hán đã nhớ.
- Phân loại rõ ràng 3 cấp độ:
  - **Marugoto A1**: Khởi động căn bản.
  - **Marugoto A2-1 (Bài 1–18)**: Giao tiếp trung cấp 1.
  - **Marugoto A2-2 (Bài 1–18)**: Chinh phục N4 thực chiến (382 từ vựng, 170 Kanji).
- Bộ lọc bài học nhanh kèm thanh tìm kiếm tức thời theo từ khoá tiếng Nhật hoặc tiếng Việt.

### ② Bộ Điều Khiển Bài Học Toàn Năng (`LessonPage.tsx`)
Thay vì viết 36 file HTML rời rạc, xây dựng 1 Component bài học duy nhất nhận `topicId` và `lessonId` qua Route (`/lessons/:level/:lessonNum`):
1. **Hero Banner**:
   - Tiêu đề bài học, chủ đề Topic, câu châm ngôn bài học có phát âm tiếng Nhật.
   - Thống kê nhanh: Số thẻ flashcard, số cấu trúc ngữ pháp, số chữ Hán.
2. **Flashcard Studio**:
   - Dùng Astryx Card với hiệu ứng lật 3D CSS transform mượt mà.
   - Các chế độ: Tự động lật, Lật ngẫu nhiên (Shuffle), Phát âm tự động khi chuyển thẻ (`ja-JP`).
   - Hiển thị badge loại từ, âm Hán Việt và icon minh họa.
3. **Cẩm Nang Ngữ Pháp (Grammar Hub)**:
   - Trình bày dạng Accordion / Cards của Astryx.
   - Công thức ngữ pháp đóng khung rõ ràng, ví dụ hội thoại có thể bấm nghe từng câu một.
4. **Kho Chữ Hán Của Bài (Kanji Grid)**:
   - Hiển thị các chữ Hán trong bài học kèm cách đọc On/Kun, số nét và mẹo nhớ.
5. **Đấu Trường Trắc Nghiệm (Interactive Quiz Engine)**:
   - Bộ 15 câu hỏi trắc nghiệm chia đều 4 đáp án.
   - Hiệu ứng chọn đáp án (đổi màu xanh khi đúng, đỏ khi sai, hiện giải thích ngữ pháp / từ vựng ngay lập tức).
   - Nổ pháo hoa `canvas-confetti` khi hoàn thành bài đạt điểm cao và lưu kết quả vào tiến độ học.

### ③ Trung Tâm Tra Cứu Chữ Hán (`KanjiHubPage.tsx`)
- Tổng hợp toàn bộ 291 mục Kanji (121 từ A2-1 + 170 từ A2-2).
- Bộ lọc theo bài học (Bài 1 -> 18), lọc theo cấp độ (A2-1, A2-2).
- Chế độ Luyện Flashcard Kanji riêng biệt để ôn thi cấp tốc.

### ④ Trung Tâm Đề Thi & Luyện Tập (`ExamPage.tsx`)
- Đề thi tổng hợp JLPT A2 (Bao gồm các đề M111 -> M115 đã chuẩn hoá đáp án cân bằng).
- Mini Test 11–14 và Mini Test 15–18.
- Đồng hồ bấm giờ tính thời gian làm bài, tự động nộp bài khi hết giờ và xem lại đáp án chi tiết.

### ⑤ Studio Luyện Gõ Tiếng Nhật (`TypingStudio`)
- Luyện gõ từ vựng theo bài: Hiện Romaji, yêu cầu người học gõ đúng Kana/Kanji để tăng tốc độ phản xạ bàn phím.

---

## 🎯 4. HƯỚNG DẪN THỰC THI TỪNG BƯỚC CHO JCODE

1. **Bước 1 - Dọn dẹp & Khởi tạo môi trường Vite**:
   - Di chuyển các file HTML tĩnh cũ sang thư mục lưu trữ `legacy_html/` (để tránh xung đột với `index.html` của Vite SPA).
   - Tạo `package.json`, cài đặt các dependencies (React 19, Astryx, StyleX, TypeScript, Vite).
   - Thiết lập `vite.config.ts`, `tsconfig.json` và `index.html` gốc làm cổng vào cho SPA.
2. **Bước 2 - Thiết lập Core UI & Routing**:
   - Cài đặt Theme Dark/Light của `@astryxdesign/theme-neutral`.
   - Dựng Layout chính (`AppShell`): Header, Sidebar danh sách bài học, Breadcrumb.
   - Cấu hình React Router cho các đường dẫn chính (`/`, `/lessons/:level/:id`, `/kanji`, `/tests`, `/kaiwa`).
3. **Bước 3 - Triển khai Component Đa Năng**:
   - Xây dựng component `FlashcardDeck`, `GrammarSection`, `KanjiCard`, `QuizEngine`, `AudioButton`.
   - Kết nối `dataLoader.ts` để đọc dữ liệu từ `data/vocab_a2_2_official.json` và `data/kanji_vocab_a2_2_official.json`.
4. **Bước 4 - Hoàn thiện các trang chức năng**:
   - Trang chủ (`HomePage`), Trang bài học (`LessonPage`), Trang tra cứu Kanji (`KanjiHubPage`), Trang luyện thi (`ExamPage`).
5. **Bước 5 - Kiểm tra & Đóng gói**:
   - Chạy `npm run build` để đảm bảo TypeScript compile 0 lỗi và bundle Vite đóng gói sạch sẽ.
   - Chạy `npm run dev` để kiểm tra trải nghiệm thực tế trên trình duyệt (`http://localhost:5173`).

---

*Chỉ dẫn này đã được lập trình chi tiết để bạn (jcode) tự chủ thực hiện toàn bộ việc đập đi xây lại dự án.*
