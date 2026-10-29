# Đề cương ôn tập giữa học kì I — Ngữ văn 10 KNTT, 2026–2027

[Tải PDF 100 trang](./DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf)

Tài liệu luyện tập theo hồ sơ **Ma trận, bản đặc tả đề kiểm tra giữa kì I lớp 10** đính kèm trong repository. Đây không phải đề thi hoặc hướng dẫn chấm do Bộ GD&ĐT ban hành.

## Nội dung

- Nguyên văn mục tiêu, ma trận và 22 yêu cầu cần đạt: 13 Đọc hiểu, 9 Viết.
- Cơ cấu 90 phút, 11 câu, 10 điểm: Đọc hiểu 6 điểm (8 trắc nghiệm, 2 tự luận); Viết 4 điểm. Ngữ liệu thần thoại ngoài SGK; tỉ lệ nhận thức 40%–30%–30%.
- Tri thức truyện kể, phân biệt thể loại, 18 ngữ liệu chọn luyện, 9 mô-típ, bảng đối sánh và ranh giới thể loại.
- Tiếng Việt, 36 nhóm mục từ, 20 câu tự kiểm tra.
- Ngân hàng 60 câu Đọc hiểu: 44 trắc nghiệm và 16 tự luận.
- Phương pháp nghị luận, bốn khuôn mở bài, ba khuôn kết bài, 20 gợi ý đề văn, cách dùng dẫn chứng và sửa bài.
- Tám đề luyện 90 phút có đáp án và bài văn tham khảo, gồm hai đề mới về Bàn Cổ và Nàng Bân / Thần Lửa.
- Lộ trình bảy ngày, 40 thẻ ghi nhớ, bảng đáp án tổng hợp, từ điển thuật ngữ và nguồn đối chiếu.

Các biểu điểm nhỏ, số dòng, số đoạn và độ dài bài mẫu là **gợi ý luyện tập**, không phải quy định trong DOCX. Khi thi phải ưu tiên đề và hướng dẫn của giáo viên. Các truyện có nhiều dị bản; dùng đúng ngữ liệu trong đề. Tài liệu không dự đoán tần suất ra đề và không bảo đảm mức điểm.

## Biên dịch PDF

Python 3.11 trở lên; cần truy cập npm registry lần đầu để tải phông chữ.

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 scripts/check_content.py
python3 scripts/build_pdf.py
```

Bộ dựng dùng Typst qua Python. `fetch_fonts.py` tải Be Vietnam Pro và Lora phiên bản Fontsource 5.3.0, ghép các tập con Latin/Vietnamese thành TrueType. Phông và tệp trung gian nằm trong `build/`, không đưa vào Git. PDF xuất bản nằm ở thư mục gốc. Dùng `--dry-run` để chỉ dựng `build/out.pdf`.

Kiểm tra tự động gồm số thứ tự câu hỏi, số đề, bảng đáp án tổng hợp khớp đáp án chi tiết, kí tự tiếng Việt, phông nhúng và mục lục PDF. Những kiểm tra này không thay thế phản biện chuyên môn từng câu hỏi.

## Mã nguồn

`src/main.typ` ghép bảy phần nội dung và phụ lục. Các tệp `part6` đến `part8` chứa tám đề; `part9_memory_kit.typ` là Phần VII; `part10_appendix.typ` là phụ lục. `template.typ` quy định bìa, bảng, hộp nội dung, mục lục và đánh số trang tự động.

## Nguồn và giới hạn

DOCX gốc là căn cứ chính. Yêu cầu kiểu bài Viết được đối chiếu với phần bài học VietJack do người dùng cung cấp. Nguồn trực tuyến được ghi trong Phụ lục C của PDF; bản kể tóm lược được nhận diện riêng. Chưa đối chiếu từng trang của mọi tuyển tập bản in. Các nhận định dẫn theo ý không nên học thuộc như nguyên văn trích dẫn.
