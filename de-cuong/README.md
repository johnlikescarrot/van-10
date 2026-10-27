# Nguồn đề cương Ngữ văn 10

- `content/*.md`: nội dung nguồn theo từng chương, có thể chỉnh sửa.
- `renderer.py`: dựng bảng, hộp ghi nhớ, đề mục và mục lục sang PDF Unicode tiếng Việt.
- `build.py`: tạo `../de-cuong-on-tap-giua-ki-1-ngu-van-10.pdf`.

## Dựng lại PDF

Yêu cầu Python 3 và `fpdf2`:

```bash
python3 -m pip install fpdf2
cd de-cuong
python3 build.py
```

PDF được tạo sẵn ở thư mục gốc để tải xuống/in ngay. Nội dung các ngữ liệu luyện tập ngoài SGK là bản phỏng thuật/biên soạn phục vụ ôn kĩ năng, không phải câu hỏi hoặc đề thi chính thức.
