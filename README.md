# Đề cương ôn tập giữa kì I Ngữ văn 10 – Kết nối tri thức

[**Mở tài liệu PDF**](DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf) · Năm học 2026–2027

Tài liệu gồm kiến thức truyện thần thoại, tiếng Việt hỗ trợ, kĩ năng đọc hiểu và viết, sáu đề luyện có đáp án, thẻ ghi nhớ và một bài mẫu ngắn. Phần hướng dẫn đầu tài liệu giải thích phạm vi sử dụng và giới hạn của các nguồn.

## Căn cứ và lưu ý

Ma trận và bản đặc tả trong tệp DOCX của kho quy định đọc hiểu thần thoại ngoài SGK và viết bài phân tích, đánh giá truyện thần thoại ngoài SGK. Ma trận nêu 6 câu trắc nghiệm nhận biết, 2 câu trắc nghiệm thông hiểu, 1 câu tự luận thông hiểu, 1 câu tự luận vận dụng và 1 bài viết; tỉ lệ đọc/viết là 60/40.

Thời gian **90 phút**, cách chia điểm từng câu, dung lượng và rubric của các đề trong tài liệu là **gợi ý luyện tập**, không phải thông số đã được ma trận ấn định. Ưu tiên hướng dẫn của giáo viên. Các đoạn truyện và nguồn in kế thừa từ phiên bản trước chưa được đối chiếu đầy đủ với bản in: để trích dẫn chính xác cần kiểm tra bản sách hoặc dùng đúng văn bản của đề. Các bài mẫu là gợi ý và một số bài dài hơn dung lượng đề luyện; không nên học thuộc máy móc.

Phụ lục PDF nêu thêm các nguồn được đối chiếu, ngày tra cứu, cách lập luận và bài mẫu ngắn dùng ngữ liệu đề số 01.

## Biên dịch

Nguồn nằm trong `src/`, bắt đầu từ `src/main.typ`. Cần Typst và phông DejaVu Sans, DejaVu Serif có hỗ trợ tiếng Việt. Ví dụ với Python và gói `typst`:

```bash
python -m pip install typst
python -c 'import typst; typst.compile("src/main.typ", output="DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf", root=".")'
```

Kiểm tra PDF đã tạo về số trang, mục lục, chữ tiếng Việt và ngắt trang trước khi phát hành. Không sửa riêng PDF mà bỏ qua mã nguồn.
