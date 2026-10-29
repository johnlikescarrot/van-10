# Đề cương ôn tập Giữa học kì I — Ngữ văn 10

**Bộ sách Kết nối tri thức với cuộc sống · Năm học 2026–2027**

Đây là tài liệu tự học được đối chiếu với tệp `MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx` trong kho. Tài liệu giúp học sinh ôn theo phạm vi, cấu trúc và mức độ nhận thức của ma trận; **không thay thế** hướng dẫn của giáo viên, tổ chuyên môn hoặc đề kiểm tra chính thức.

## PDF phát hành

- [`DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf`](./DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf)

PDF có thể được tái tạo từ mã nguồn Typst và phông chữ được kèm trong kho.

## Phạm vi đã đối chiếu

| Phần | Theo ma trận gốc | Cách tài liệu hỗ trợ ôn tập |
| --- | --- | --- |
| Đọc hiểu | Thần thoại ngoài sách giáo khoa; 6 câu TNKQ Nhận biết, 2 câu TNKQ Thông hiểu, 1 câu tự luận Thông hiểu, 1 câu tự luận Vận dụng; 6,0 điểm | Tri thức thể loại, tiếng Việt, 40 câu luyện tập và 6 đề minh họa |
| Viết | Bài văn nghị luận phân tích, đánh giá một tác phẩm truyện; 4,0 điểm, tích hợp Nhận biết – Thông hiểu – Vận dụng | Dàn ý linh hoạt, bài tập lập luận, bảng tự rà và bài tham khảo |
| Toàn bài | 90 phút, 11 câu, 10,0 điểm; Nhận biết 40%, Thông hiểu 30%, Vận dụng 30% | Gợi ý phân bổ thời gian và lộ trình tự học 7 ngày |

Ma trận không ấn định cách đánh số câu, dung lượng bài viết, cách ghép ngữ liệu hay rubric điểm nhỏ. Các cách trình bày, mốc số dòng và biểu điểm trong đề cương chỉ phục vụ luyện tập.

## Nội dung

1. **Phần I — Ma trận và bản đặc tả:** đọc đúng cấu trúc 90 phút, ánh xạ 13 chỉ báo Đọc hiểu và 9 yêu cầu Viết.
2. **Phần II — Tri thức truyện kể và thần thoại:** công cụ đọc cốt truyện, người kể, nhân vật, chủ đề và khẩu quyết 5K–1C nhất quán.
3. **Phần III — Tiếng Việt:** từ Hán Việt, phương thức biểu đạt, biện pháp tu từ, mạch lạc và liên kết.
4. **Phần IV — Kĩ năng Đọc hiểu:** cách kiểm tra phương án, khung trả lời tự luận và 40 câu luyện tập.
5. **Phần V — Kĩ năng Viết:** chuyển chi tiết thành lập luận, dàn ý năm tầng, bảng tự rà; có ví dụ chuyển giao từ *Chữ người tử tù*.
6. **Phần VI — Sáu đề minh họa:** 66 câu hỏi cùng đáp án gợi ý và bài viết tham khảo. Toàn bộ ngữ liệu trong khung đề là bản **biên soạn lại** từ mô-típ thần thoại để luyện thao tác đọc văn bản mới.
7. **Phần VII — Tự học:** lịch 7 ngày, 24 thẻ tự kiểm và checklist trước khi nộp bài.
8. **Phần VIII — Nguồn và kiểm định:** tuyên bố phạm vi, ngữ liệu, đáp án gợi ý, nhật kí đối chiếu và giấy phép phông chữ.

## Nguồn và cách dùng có trách nhiệm

- Tệp ma trận trong kho là nguồn quyết định cấu trúc đánh giá.
- SGK *Ngữ văn 10, Tập một — Kết nối tri thức với cuộc sống* là nguồn tham chiếu kiến thức và kĩ năng.
- Các mô-típ thần thoại được đối chiếu với danh mục ở Phần VIII của PDF. Đề cương không tuyên bố các ngữ liệu luyện tập là trích dẫn nguyên văn.
- Đáp án, bài mẫu và mức chia ý là **gợi ý tự học**. Một cách lí giải khác vẫn có giá trị nếu bám sát ngữ liệu và lập luận hợp lí.

## Tái tạo PDF

Yêu cầu: Node.js 20+ và npm.

```bash
npm ci
npm run verify
```

- `npm run build` biên dịch `src/main.typ` thành PDF đích.
- `npm run check` kiểm tra chữ ký PDF, kích thước tối thiểu và trailer PDF.
- Trình biên dịch được ghim tại `@myriaddreamin/typst-ts-node-compiler@0.7.0`; quá trình build coi mọi cảnh báo Typst là lỗi.

## Cấu trúc kho

```text
.
├── DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf
├── MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx
├── package.json / package-lock.json
├── scripts/
│   ├── build-pdf.mjs
│   └── check-pdf.mjs
└── src/
    ├── main.typ
    ├── template.typ
    ├── part1_matrix.typ … part8_memory_kit.typ
    ├── part9_sources_quality.typ
    └── fonts/                 # Be Vietnam Pro, Lora, DejaVu Sans và giấy phép đi kèm
```

## Phông chữ

`src/fonts/` chứa Be Vietnam Pro và Lora theo **SIL Open Font License 1.1**, cùng DejaVu Sans theo giấy phép Bitstream Vera/DejaVu để hiển thị ổn định các kí hiệu chuyên dụng. Bản sao giấy phép được kèm ngay trong thư mục đó để bản PDF có thể tái tạo ổn định trên máy khác.
