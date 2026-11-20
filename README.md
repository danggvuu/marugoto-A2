# Marugoto Astryx V2

Ứng dụng học tiếng Nhật bằng tiếng Việt đang được chuyển sang **React 19, TypeScript, Vite, Meta Astryx và StyleX** trên nhánh `feat/astryx-v2`. `index.html` ở thư mục gốc là entry của SPA. Bộ HTML cũ được lưu riêng tại `legacy_html/`, không phải các trang bọc SPA.

> Nội dung và đề trong dự án phục vụ tự luyện, không phải đề thi hoặc chứng nhận JLPT chính thức. Kiểm tra kỹ thuật không chứng minh mọi nội dung tiếng Nhật hoặc đáp án đều đúng.

## Chạy ứng dụng

Cần Node.js tương thích với Vite 8 và npm. Cài dependencies, rồi chạy từ thư mục dự án:

```sh
npm install
npm run dev
```

Mở địa chỉ Vite in trong terminal. Các route được khai báo trong `src/App.tsx`:

- `/`: dashboard.
- `/lessons/a2-1/1` hoặc `/lessons/a2-2/1`: bài học; thay số cuối bằng bài 1–18.
- `/kanji`: trung tâm Kanji.
- `/tests`: luyện thi.
- `/kaiwa`: luyện hội thoại.
- `/legacy_html/index.html`: kho HTML gốc, gồm A1 và các chuyên đề cũ.

Build và xem bản production:

```sh
npm run build
npm run preview
```

Triển khai **toàn bộ `dist/`**, bao gồm `dist/legacy_html/`. Với hosting tĩnh, cấu hình fallback về `index.html` cho route SPA, nhưng phải ưu tiên file tĩnh có thật, đặc biệt `/legacy_html/**`. Dự án hiện sử dụng URL từ gốc website, không được kiểm chứng cho triển khai dưới một subpath.

## Kho HTML cũ

Kho gồm **59 trang HTML**: 12 trang ở gốc kho, 36 bài học và 11 trang đề/ôn tập. Các bản HTML cũ đã được gỡ khỏi gốc dự án, `lessons/` và `tests/`; `index.html` gốc dành cho SPA. Kho giữ nguyên tên file và cấu trúc thư mục con, kèm **126 tệp assets** và **5 PDF được HTML liên kết**.

Các đường dẫn đại diện khi server chạy:

- `/legacy_html/index.html`
- `/legacy_html/lessons/Marugoto_A2_Lesson_1.html`
- `/legacy_html/lessons/Marugoto_A2_2_Lesson_1.html`
- `/legacy_html/tests/De_Thi_Tong_Hop_JLPT_A2_11_18.html`
- `/legacy_html/Tu_Vung_Marugoto_A1_16_A2_1_10.html`
- `/legacy_html/kanji_a2.html`
- `/legacy_html/Tong_Hop_Ngu_Phap_Marugoto_A1_A2.html`
- `/legacy_html/demo_3d.html`

`scripts/legacyArchive.ts` cung cấp hai plugin đã được nối vào Vite: `legacyArchive()` phục vụ trực tiếp file gốc trong dev, `legacyArchiveBuild()` sao chép nguyên kho vào output build. HTML không được xử lý như entry React. Các import `?raw` của Vite vẫn đi qua cơ chế nạp dữ liệu bình thường.

`assets/` ở gốc được giữ làm nguồn tái tạo dữ liệu. SPA đọc JSON bài học, ngữ pháp và Mini Test đã trích xuất, không nạp nguyên HTML hay thực thi mã JavaScript bài học cũ. `npm run extract-data` tái tạo các JSON này từ nguồn trong repository. Bản sao `legacy_html/assets/` dành riêng cho trang lưu trữ. Nếu cập nhật nội dung cũ, chủ động đồng bộ tài nguyên tương ứng và kiểm tra lại kho. Không chạy các generator cũ như một phần build SPA: một số script trước đây ghi HTML vào vị trí gốc/`lessons/`/`tests/` và chưa được chuyển toàn bộ sang vị trí archive.

## Kiểm tra kho lưu trữ

```sh
# Đếm trang, kiểm tra tất cả liên kết/tài nguyên local khai báo trong HTML
node scripts/check_legacy_archive.mjs

# Kiểm tra thêm toàn bộ 190 tệp HTTP, so sánh từng byte với bản gốc
# Dùng địa chỉ và cổng server thực tế đang chạy
node scripts/check_legacy_archive.mjs http://127.0.0.1:5173

# Sau npm run build, chạy npm run preview rồi kiểm tra cổng preview
node scripts/check_legacy_archive.mjs http://127.0.0.1:4173
```

### Trạng thái đã kiểm chứng ngày 2026-11-20

- `npm run build` hoàn tất: TypeScript và Vite build thành công. Route được tách bằng lazy import; chunk dữ liệu dùng chung vẫn lớn và còn cảnh báo Vite, chưa phải xác nhận tối ưu hiệu năng.
- React 19 + Astryx Neutral + StyleX, chuyển sáng/tối thay đổi màu thực tế và được lưu. React Router 7 được dùng thay 6 để tránh các cảnh báo bảo mật từ dependency audit.
- 36 route bài học có từ vựng, ngữ pháp và 15 câu quiz mỗi bài. Dữ liệu A2-2 giữ direct JSON imports: 382 từ và 170 mục Kanji. Kanji Hub có tổng 291 mục, với 121 mục A2-1 thuộc nguồn Bài 11–18, không tự thêm Kanji cho Bài 1–10.
- Phòng thi gồm các mã đề tổng hợp cùng Mini Test 11–14 và năm mã Mini Test 15–18. Điểm phần trăm chỉ tính câu chọn có đáp án hợp lệ. Phần tự luận/ghép hội thoại cho nhập câu trả lời và tự đối chiếu, không giả lập chấm tự động.
- `npm run test:e2e`: **12/12 bài kiểm thử Chrome đạt**, gồm kiểm tra bất biến dữ liệu 36 bài học, Mini Test, chấm điểm đúng 100% theo đáp án nguồn và mô phỏng hết giờ. Các route chính cũng được mở trực tiếp trên production preview, không ghi nhận lỗi JavaScript runtime.
- `npm audit --audit-level=moderate`: không phát hiện lỗ hổng trong dependency đã cài ở lần kiểm tra này.
- Kiểm tra tĩnh kho: đủ 59 HTML, **161 đường dẫn local khác nhau**, không thiếu file được tham chiếu trong thuộc tính HTML được kiểm tra.
- Kiểm tra HTTP ở Vite dev và production preview: **190/190 tệp** trả HTTP 200 và nội dung trùng từng byte với kho nguồn. Điều này phát hiện trường hợp fallback SPA trả HTTP 200 nhưng sai nội dung.
- Kiểm tra trên không xác nhận mọi tương tác của 59 trang, fragment `#...`, tài nguyên từ dịch vụ ngoài, hay tính đúng đắn học thuật. Chưa coi toàn bộ regression/browser test cũ là đã chạy cho V2.

## Cấu trúc chính

```text
.
├── index.html                  # Entry SPA
├── src/                        # React pages, components, services, styles
├── data/                       # JSON nguồn cho bộ nạp SPA
├── assets/                     # JavaScript/dữ liệu cũ còn được import
├── legacy_html/                # 59 HTML gốc
│   ├── assets/                 # CSS, JavaScript và dữ liệu cho kho
│   ├── docs/pdf/               # 5 PDF được HTML liên kết
│   ├── lessons/                # 36 trang bài học
│   └── tests/                  # 11 trang đề/ôn tập
├── scripts/legacyArchive.ts    # Vite static archive plugins
├── scripts/check_legacy_archive.mjs
├── qa/                         # Kiểm tra cũ, không mặc định chứng minh V2
└── docs/                       # Tài liệu và tư liệu nguồn
```

## Kiểm thử SPA

```sh
npm run typecheck
npm run test:e2e
npm run test:archive
npm audit --audit-level=moderate
```

Bộ Playwright dùng Chrome đã cài trên máy (`channel: 'chrome'`), chạy Vite dev tại cổng 5178 nếu chưa có server. Có thể cài Chrome cho Playwright bằng `npx playwright install chrome` nếu máy chưa có. Các bài kiểm tra bao phủ dashboard, màu theme, 36 deep links, flip/autoplay, yêu cầu Speech API `ja-JP`, quiz chấm tức thì và lưu tiến độ, typing, Kanji canvas/bộ lọc, Kaiwa, điều hướng mobile, dữ liệu lưu lỗi, chấm điểm đề và tự nộp theo thời gian. Kiểm thử phát âm xác nhận lời gọi API, không xác nhận âm thanh nghe được hay chất lượng giọng đọc.

## Dữ liệu trình duyệt và kết nối mạng

Tiến độ được lưu trong `localStorage` của origin hiện tại. Cổng hoặc hostname khác có vùng lưu khác; xóa dữ liệu website có thể làm mất tiến độ. Không có đồng bộ tài khoản. Việc giữ HTML trong kho không tự chứng minh tương thích toàn bộ checkpoint giữa giao diện cũ và SPA mới.

Font ngoài, dữ liệu nét Kanji và phát âm có thể phụ thuộc mạng hoặc giọng đọc được cài trên thiết bị. Không coi SPA hoặc kho HTML là ứng dụng offline hoàn toàn.

## Tài liệu nguồn

- `PROMPT_ASTRYX_V2.md`: yêu cầu tái cấu trúc V2.
- `docs/PROJECT_STRUCTURE.md` và `docs/reviews/`: tài liệu/báo cáo của cấu trúc cũ; kiểm tra lại phạm vi trước khi áp dụng vào SPA.
