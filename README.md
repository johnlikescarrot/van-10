# Ôn tập giữa kì I Ngữ văn 10 — Kết nối tri thức, 2026–2027

**[Mở PDF hoàn chỉnh](./DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf)** · 49 trang A4 · bản biên tập ngày 29/10/2026.

Tài liệu tự luyện được viết lại và đối chiếu với ma trận DOCX trong kho. Đây **không phải** đề thi, hướng dẫn chấm chính thức hoặc dự báo đề của nhà trường. Đáp án chi tiết và các bài tham khảo do người biên soạn xây dựng.

## Nội dung

1. **Đọc ma trận:** 90 phút; đọc hiểu 6,0 điểm, viết 4,0 điểm; 8 câu trắc nghiệm, 2 câu tự luận đọc hiểu, 1 bài viết. Bản đồ 13 yêu cầu đọc và 9 yêu cầu viết dùng mã biên tập để tiện theo dõi.
2. **Tri thức Ngữ văn:** khái niệm truyện kể, người kể/ngôi kể/điểm nhìn, thần thoại và các thể loại gần nhau; đối chiếu các văn bản Bài 1 KNTT.
3. **Tiếng Việt:** các cặp từ dễ lẫn, 16 mục từ hỗ trợ, phân tích nghệ thuật, mạch lạc, liên kết và 6 bài tập sửa câu.
4. **Đọc hiểu:** 4 đoạn kể ngắn đi kèm **28 câu TN + 12 câu TL**; đáp án giải thích, bài trả lời tham khảo và tiêu chí tự kiểm tra đặt riêng sau câu hỏi.
5. **Viết:** 5 yêu cầu kiểu bài, quy trình tìm ý–viết–sửa, đọc bài tham khảo *Quà Giáng sinh*, cách triển khai đoạn, mở/kết và thang tự chấm 4 điểm.
6. **6 đề tự luyện:** mỗi đề có ngữ liệu, 8 TN + 2 TL + 1 bài viết; cả 6 đề đặt trước phần đáp án; có bằng chứng cho 48 đáp án TN, thang chấm TL, 6 dàn ý và **6 bài viết hoàn chỉnh**. Mỗi bài 600–800 đơn vị tách bằng khoảng trắng.
7. **Bộ tự kiểm tra:** lịch 7 ngày có sản phẩm đầu ra, 24 cặp hỏi–đáp, phiếu sửa lỗi, checklist và trang tóm lược một trang (trang 47).
8. **Phụ lục nguồn:** S1–S11, phân biệt nguồn gốc/nguồn thứ cấp, bản kể và giới hạn đối chiếu.

PDF có mục lục bấm được, 94 bookmark, số trang và phông tiếng Việt nhúng. Thiết kế sử dụng Be Vietnam Pro (kèm giấy phép OFL); kí hiệu được bổ sung bằng phông dự phòng nhúng của Typst.

## Những giới hạn được nêu rõ trong PDF

- Các ngữ liệu là **bản kể rút gọn, diễn đạt lại**, không phải trích nguyên văn sách in. Không gán tên người sưu tầm thành tác giả dân gian hoặc viện một ấn bản chưa kiểm tra.
- *Cuộc tu bổ lại các giống vật* và *Prô-mê-tê và loài người* có trong SGK Chân trời sáng tạo. *Ông Đùng, bà Đùng* có giao thoa thể loại và đã xuất hiện ở cấp học khác. Đề 4–6 vì vậy dùng để chuyển giao kĩ năng, **không được quảng bá là ngữ liệu ngoài mọi SGK**.
- Dung lượng 600–800 chữ, cách chia từng điểm nhỏ và gợi ý thời gian là thiết kế tự luyện; ma trận gốc không cung cấp các quy định chi tiết đó.
- Ngữ liệu ngắn và một số phương án nhiễu rõ giúp luyện thao tác cơ bản; bộ đề chưa được thử nghiệm độ khó trên nhóm học sinh. Nên luyện thêm văn bản dài, chưa đọc do giáo viên chọn.

## Dựng và kiểm tra

Cần Python 3.11 trở lên. Không cần cài Typst CLI hoặc tải phông khi dựng; phông và giấy phép đã ở `assets/fonts/`.

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt

# Kiểm tra dữ liệu biên tập độc lập
.venv/bin/python -m unittest discover -s tests -v

# Tạo lại JSON, chạy 15 kiểm tra dữ liệu, rồi dựng PDF đúng tên
.venv/bin/python scripts/build.py

# Kiểm tra PDF đã xuất và ghi báo cáo có SHA-256
.venv/bin/python scripts/validate_pdf.py
```

Có thể xuất bản nháp ngoài Git:

```bash
.venv/bin/python scripts/build.py --output build/review.pdf
.venv/bin/python scripts/validate_pdf.py build/review.pdf --report build/qa-report.json
```

`validate_pdf.py` kiểm tra sự hiện diện đầy đủ của đoạn văn, câu hỏi, phương án và bài tham khảo; A4; phông nhúng; biên trang; liên kết và bookmark; không có trang trắng hoặc kí tự thay thế. Những kiểm tra đó **không** tự xác nhận tính đúng đắn của mọi cách hiểu văn học, độ khó chuẩn hoá hoặc khả năng truy cập URL tại mọi thời điểm. Báo cáo xuất bản nằm ở [`research/qa-report.json`](research/qa-report.json).

## Tổ chức mã nguồn

```text
src/main.typ                   Tệp dựng chính
src/template.typ               Bìa, kiểu chữ, bảng, hộp và điều hướng
src/part1_matrix.typ …          Bảy phần nội dung
src/assessment.typ             Bộ dựng ngữ liệu, đề và đáp án
src/exams.json, src/bank.json   Dữ liệu sinh từ hai script biên soạn
src/sources.typ                Phụ lục S1–S11
scripts/author_exams.py         Nguồn biên tập sáu đề, đáp án và bài viết
scripts/author_bank.py          Nguồn biên tập 40 câu
scripts/build.py               Dựng bản xuất bản
scripts/validate_pdf.py         Kiểm tra PDF
research/sources.json          Liên kết, loại nguồn và cách dùng
research/EDITORIAL_REVIEW.md   Nhật kí đối chiếu và các sửa đổi quan trọng
research/matrix-extracted.txt  Văn bản trích từ DOCX để kiểm tra chéo
tests/test_content.py          15 kiểm tra cấu trúc, điểm và nội dung dữ liệu
assets/fonts/                  Be Vietnam Pro + giấy phép OFL
```

Sửa nội dung đề/ngân hàng ở `scripts/author_*.py` rồi dựng lại; không sửa riêng JSON vì lần dựng sau sẽ ghi đè. Giữ nguyên DOCX gốc làm căn cứ. Kiểm tra lại bố cục và báo cáo sau mỗi lần sửa trước khi thay PDF xuất bản.
