# Đề cương ôn tập giữa kì I Ngữ văn 10

**Bộ sách:** Kết nối tri thức với cuộc sống · **Năm học:** 2026–2027

[Tải đề cương PDF](DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf)

Tài liệu ôn đọc hiểu thần thoại và viết bài phân tích, đánh giá truyện theo `MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx` trong kho. Nội dung gồm kiến thức nền, hướng dẫn làm bài, câu hỏi tự kiểm tra, ba đề luyện có đáp án và một bài viết tham khảo. Các ngữ liệu luyện đề được biên soạn lại từ những nguồn được ghi trong PDF; không phải trích dẫn nguyên văn.

Ma trận quy định 90 phút, đọc hiểu 60% và viết 40%, gồm 8 câu trắc nghiệm, 2 câu đọc hiểu tự luận và 1 bài viết. Ma trận **không** quy định điểm từng câu, số chữ bài viết hoặc số ngữ liệu: biểu điểm, dung lượng và cách dùng chung một ngữ liệu trong các đề là phương án luyện tập. Áp dụng hướng dẫn riêng của giáo viên nếu có.

Bản cập nhật thay bản 65 trang trước bằng bản biên tập lại. Những nội dung không có căn cứ đủ chắc, biểu điểm được khẳng định là chính thức, trích dẫn chưa kiểm chứng và các đề cũ không được giữ trong ấn bản mới. Có thể xem phiên bản trước trong lịch sử Git.

## Biên dịch và kiểm tra

Cần Python 3 và phông DejaVu Sans có hỗ trợ tiếng Việt. Từ thư mục gốc:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/build.py
```

Mã nguồn tài liệu trong `src/main.typ`, `guide.typ`, `extra.typ`, `practice.typ`, `answers.typ`, `references.typ` và `styles.typ`. Tập lệnh biên dịch PDF, kiểm tra thứ tự câu, số câu trắc nghiệm, các phần chính, bookmark và chữ ngoài trang. Các kiểm tra này không thay thế việc đọc soát nội dung và bố cục.
