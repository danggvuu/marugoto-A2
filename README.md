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

`assets/` ở gốc vẫn được giữ vì bộ nạp dữ liệu SPA sử dụng một phần JavaScript nguồn. Bản sao `legacy_html/assets/` dành riêng cho trang lưu trữ. Nếu cập nhật nội dung cũ, chủ động đồng bộ tài nguyên tương ứng và kiểm tra lại kho. Không chạy các generator cũ như một phần build SPA: một số script trước đây ghi HTML vào vị trí gốc/`lessons/`/`tests/` và chưa được chuyển toàn bộ sang vị trí archive.

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

- `npm run build` hoàn tất: TypeScript và Vite build thành công. Build còn cảnh báo bundle JavaScript lớn, chưa phải xác nhận tối ưu hiệu năng.
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

## Dữ liệu trình duyệt và kết nối mạng

Tiến độ được lưu trong `localStorage` của origin hiện tại. Cổng hoặc hostname khác có vùng lưu khác; xóa dữ liệu website có thể làm mất tiến độ. Không có đồng bộ tài khoản. Việc giữ HTML trong kho không tự chứng minh tương thích toàn bộ checkpoint giữa giao diện cũ và SPA mới.

Font ngoài, dữ liệu nét Kanji và phát âm có thể phụ thuộc mạng hoặc giọng đọc được cài trên thiết bị. Không coi SPA hoặc kho HTML là ứng dụng offline hoàn toàn.

## Tài liệu nguồn

- `PROMPT_ASTRYX_V2.md`: yêu cầu tái cấu trúc V2.
- `docs/PROJECT_STRUCTURE.md` và `docs/reviews/`: tài liệu/báo cáo của cấu trúc cũ; kiểm tra lại phạm vi trước khi áp dụng vào SPA.
