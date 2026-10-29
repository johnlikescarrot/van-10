# Đề cương ôn tập giữa học kì I môn Ngữ văn 10 – Kết nối tri thức với cuộc sống (Năm học 2026–2027)

Tài liệu ôn tập toàn diện môn **Ngữ văn 10 (Chương trình GDPT 2018 – Bộ sách Kết nối tri thức với cuộc sống)** phục vụ kì kiểm tra đánh giá giữa học kì I năm học **2026–2027**, biên soạn bám sát tuyệt đối từng chỉ báo trong `MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx` và sách giáo khoa *Ngữ văn 10, Tập một* (Bài 1, Bài 2, Bài 3).

## Tệp tài liệu chính thức (PDF xuất bản – 58 trang A4)

- **Bản PDF hoàn chỉnh:** [`DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf`](./DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf)
- **Định dạng:** A4 chuẩn in ấn học thuật (58 trang, nhúng đầy đủ bộ phông chữ tiếng Việt *Be Vietnam Pro* và *Lora*, không đứt gãy bảng biểu hay câu hỏi trắc nghiệm qua trang).

## Cấu trúc 7 phần trọng tâm của đề cương

| Phần | Nội dung chuyên đề | Trang |
|---|---|---:|
| **Bìa & Mục lục** | Tóm tắt cấu trúc đề 90 phút, hướng dẫn khai thác tài liệu và mục lục tổng quát | 1–2 |
| **Phần I** | **Phân tích Ma trận, Bản đặc tả và chiến lược làm bài 90 phút:** Giải mã 22 chỉ báo đánh giá (CB1–CB22), cơ cấu điểm đến từng `0,25đ`, hai phương án kết nối ngữ liệu (Phương án A & B) và lịch trình `10 + 15 + 60 + 5 = 90 phút` | 3–6 |
| **Phần II** | **Tri thức ngữ văn nền tảng, thể loại thần thoại và kho 16 ngữ liệu mở rộng:** Hệ thống hóa Bài 1–3 SGK KNTT, công thức `5K–1C`, bảng phân biệt 5 thể loại tự sự (*thần thoại, sử thi, truyền thuyết, cổ tích, truyền kì*), 4 văn bản Bài 1 SGK và hồ sơ 16 thần thoại ngoài SGK (Việt, Mường, Lô Lô, Khơ-mú, Hy Lạp, Trung Quốc) | 7–13 |
| **Phần III** | **Thực hành tiếng Việt toàn diện nửa đầu Học kì I:** Sử dụng từ Hán Việt (Bài 1, tr. 28–29), 6 biện pháp tu từ với quy trình phân tích 3 tầng, lỗi dùng từ & trật tự từ (Bài 2, tr. 64–65), lỗi mạch lạc & liên kết văn bản (Bài 3, tr. 87–89) | 14–17 |
| **Phần IV** | **Chiến thuật giải nhanh Đọc hiểu & Ngân hàng 50 câu hỏi theo chỉ báo:** 4 bẫy phương án nhiễu trắc nghiệm, công thức `GỌI – TRÍCH – GIẢI – CHỐT` (Câu 9), cấu trúc 4 nhịp đoạn văn 150 chữ (Câu 10), cùng 36 câu TNKQ + 14 câu TL có đáp án chi tiết | 18–26 |
| **Phần V** | **Cẩm nang viết bài văn nghị luận phân tích, đánh giá một tác phẩm truyện (4,0 điểm):** Đối chiếu 5 yêu cầu SGK (tr. 29–34), phân tích bài mẫu *Quà Giáng sinh* (O. Hen-ry) và *Chữ người tử tù* (Nguyễn Tuân), hai mô hình bố cục Thân bài linh hoạt, 4 Mở bài, 3 Kết bài, 8 nhận định lí luận xác thực và bảng rèn giọng văn tự nhiên tránh khuôn sáo | 27–30 |
| **Phần VI** | **Bộ 07 đề thi thử chuẩn ma trận 2026–2027 (77 câu hỏi):** Bao phủ cả Phương án A & B, cả thần thoại văn xuôi và thần thoại văn vần (*Đi san mặt đất*), kèm hướng dẫn chấm từng `0,25đ`, đoạn mẫu Câu 10 và 07 bài văn tham khảo hoàn chỉnh | 31–53 |
| **Phần VII** | **Bộ công cụ ôn tập thông minh & Trang tổng hợp trước giờ thi:** Lộ trình ôn ngắt quãng 7 ngày, 30 thẻ tự kiểm tra (Active Recall), tờ tóm tắt cốt lõi in rời trên 1 trang độc lập (trang 57) và bảng kiểm 5 phút + nhật kí tự chấm 07 đề (trang 58) | 54–58 |

## Cấu trúc mã nguồn Typst (`src/`)

- `src/main.typ`: Tệp gốc kết nối toàn bộ các chương mục.
- `src/template.typ`: Hệ thống định dạng trang in A4, bảng biểu chống cắt dòng lẻ và khung câu hỏi trắc nghiệm 1 cột / 2 cột không đứt trang.
- `src/part1_matrix.typ` → `src/part8_memory_kit.typ`: Tám mô-đun nội dung tương ứng từ Phần I đến Phần VII.
