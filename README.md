# Đề cương ôn tập Giữa kì I – Ngữ văn 10 (Kết nối tri thức) 2026–2027

Bộ tài liệu ôn thi được biên soạn **bám sát Ma trận và Bản đặc tả** trong tệp
`MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx` (tài liệu của giáo viên).

## Sản phẩm chính

| Tệp | Nội dung |
|---|---|
| **`DE-CUONG-ON-TAP-GIUA-KI-1-NGU-VAN-10-KNTT-2026-2027.pdf`** | **Bản PDF hoàn chỉnh, 61 trang** – đề cương ôn tập đầy đủ (đọc hiểu, viết, đề minh hoạ + đáp án, công cụ ghi nhớ) |
| `de-cuong/content/*.md` | Nguồn Markdown của từng phần (chỉnh sửa nội dung tại đây) |
| `de-cuong/build_pdf.py` | Script dựng PDF (ReportLab, Markdown-lite → PDF) |
| `de-cuong/fonts/` | Font nhúng: Be Vietnam Pro (văn bản), Roboto Mono (sơ đồ), DejaVu Sans (ký hiệu) |

## Cấu trúc tài liệu (11 phần)

1. **Phần 1** – Giải mã ma trận & bản đặc tả; phân bổ 90 phút; thang điểm 11 câu suy ra từ hai ràng buộc 60/40 và 40-30-30.
2. **Phần 2** – Truyện kể & thần thoại: 6 khái niệm nền, 4 đặc trưng, phân biệt với truyền thuyết/cổ tích, bối cảnh lịch sử – văn hoá.
3. **Phần 3** – Hệ thống tác phẩm Bài 1 (KNTT): Thần Trụ Trời, Thần Sét, Thần Gió, Tản Viên từ Phán sự lục, Chữ người tử tù, Tê-dê + bảng đối sánh.
4. **Phần 4** – Ngân hàng ngữ liệu ngoài SGK: quy trình "bóc" văn bản, **Thần Mưa** (nguyên văn + phân tích 6 đặc trưng + 10 câu hỏi có đáp án), 9 truyện mở rộng, bảng tra 20 truyện.
5. **Phần 5** – 10 dạng câu hỏi đọc hiểu và công thức trả lời, kèm bài mẫu từng thang điểm.
6. **Phần 6** – **Đề minh hoạ số 1 đúng ma trận (11 câu)** + đáp án, thang điểm, bài làm tham khảo cho câu 9, 10, 11.
7. **Phần 6B** – Hai đề tự luyện (Thần Sét, Nữ Oa vá trời) + đáp án chi tiết.
8. **Phần 7** – Chuyên đề Viết: cấu trúc, công thức 4 đoạn, **2 bài văn mẫu hoàn chỉnh**, kho từ ngữ, 8 lỗi thường gặp.
9. **Phần 8** – Thực hành tiếng Việt (từ Hán Việt), biện pháp tu từ, bài tập có đáp án.
10. **Phần 9** – Bộ công cụ ghi nhớ: 10 câu thần chú, "phao" 1 tờ, kế hoạch 14/7/3 ngày, 40 flashcard, checklist.
11. **Phụ lục** – Bảng đối chiếu từng yêu cầu của bản đặc tả với vị trí đáp ứng; kiểm tra tỉ lệ điểm; nguồn tham khảo.

## Dựng lại PDF

```bash
pip install reportlab
python3 de-cuong/build_pdf.py
```

Script đọc toàn bộ `de-cuong/content/*.md` theo thứ tự tên tệp, dựng mục lục tự động,
bookmark và xuất PDF ra thư mục gốc của repo.

### Cú pháp Markdown-lite dùng trong `content/`

| Cú pháp | Kết quả |
|---|---|
| `@@ KICKER \| TIÊU ĐỀ \| PHỤ ĐỀ` | Trang bìa phần (page break + dải màu) |
| `#`, `##`, `###`, `####` | Tiêu đề cấp 1–4 (cấp 1–3 vào mục lục & bookmark) |
| `> ...` | Hộp ghi chú (xanh) |
| `>> ...` | Hộp nhấn mạnh (kem) |
| `!! ...` | Hộp kết luận (xanh lá) |
| `%% ...` | Khối ngữ liệu trích dẫn (nền kem, viền) — `%%!` là tiêu đề khối, `%%` trống là ngắt đoạn |
| `\| bảng \|` | Bảng có tiêu đề hàng, kẻ ô, xen kẽ màu |
| `- mục` | Gạch đầu dòng |
| ```` ``` ```` | Khối sơ đồ (font mono) |
| `A. ...` | Phương án trắc nghiệm |
| `---` | Đường kẻ ngang |

## Kiểm chứng độ khớp với ma trận

| Ràng buộc của ma trận | Kết quả trong đề minh hoạ |
|---|---|
| Đọc hiểu 60% – Viết 40% | 6,0 – 4,0 ✔ |
| Biết 40% – Hiểu 30% – Vận dụng 30% | 4,0 – 3,0 – 3,0 ✔ |
| 11 câu: 8 TN + 2 TL đọc hiểu + 1 bài viết | 6 TN (Biết) + 2 TN (Hiểu) + 1 TL (Hiểu) + 1 TL (Vận dụng) + 1 bài viết ✔ |
| Ngữ liệu ngoài SGK, thể loại thần thoại | *Thần Mưa* (đề 1), *Thần Sét* (đề 2), *Nữ Oa vá trời* (đề 3) ✔ |
