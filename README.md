# Đề cương Ngữ văn 10 – giữa kì I 2026–2027

**[Mở đề cương PDF](DE-CUONG-ON-TAP-NGU-VAN-10-GIUA-KI-I-2026-2027.pdf)** · A4, 34 trang, có mục lục và liên kết nguồn có thể bấm, phông tiếng Việt nhúng trong PDF.

Tài liệu đối chiếu trực tiếp tệp ma trận và bản đặc tả trong kho, gắn với Bài 1 của Ngữ văn 10 *Kết nối tri thức với cuộc sống*. Nội dung gồm bản đồ các yêu cầu, kiến thức thần thoại và truyện kể, kĩ năng đọc – viết, lịch ôn, 50 thẻ tự kiểm, **5 đề luyện (55 câu hỏi) có đầy đủ đáp án, hướng dẫn chấm và 5 bài viết mẫu**.

> **Giới hạn quan trọng:** Tệp DOCX có mục tiêu, ma trận và bản đặc tả, nhưng không cung cấp đề thi, ngữ liệu, câu hỏi hoặc đáp án chính thức. Đề, ngữ liệu phỏng kể, đáp án, bài mẫu và cách phân điểm cụ thể trong PDF đều do người biên soạn xây dựng để luyện tập, không phải đề thi thật. Các văn bản có dị bản; câu hỏi được giải theo chính bản kể trong từng đề.

## Cấu trúc nguồn

- `MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx`: tài liệu gốc, giữ nguyên.
- `de-cuong/01-nen-tang.md`: phân tích ma trận, bảng đối chiếu và tri thức nền.
- `de-cuong/02-ky-nang-va-ghi-nho.md`: phương pháp, viết và 50 thẻ ghi nhớ.
- `de-cuong/03-nam-de-luyen.md`: 5 đề luyện tự biên soạn.
- `de-cuong/04-dap-an-va-bai-viet.md`: đáp án, 5 bài mẫu và nguồn nghiên cứu.
- `tools/build_pdf.py`: tạo lại PDF; `fonts/` chứa phông DejaVu và giấy phép.
- `tests/test_document.py`: đối chiếu DOCX, 55 câu, phương án đúng, PDF và phông.

## Tạo và kiểm tra PDF

Cần Python 3.11 trở lên. Từ thư mục gốc của kho:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tools/build_pdf.py
.venv/bin/python tests/test_document.py
```

Trình tạo sử dụng các tệp Markdown và phông có sẵn trong kho; không cần truy cập các trang tham khảo khi dựng PDF. PDF được dựng với siêu dữ liệu ổn định để cùng phiên bản phụ thuộc cho kết quả lặp lại. Các bài viết, đáp án mở và rubric là gợi ý, không thay thế hướng dẫn thực tế của giáo viên.
