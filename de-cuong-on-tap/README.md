# Đề cương ôn tập Giữa học kì I – Ngữ văn 10 (Kết nối tri thức) 2026–2027

Sản phẩm: **[`pdf/De_cuong_on_tap_Giua_ki_I_Ngu_van_10_KNTT_2026-2027.pdf`](pdf/De_cuong_on_tap_Giua_ki_I_Ngu_van_10_KNTT_2026-2027.pdf)** (38 trang A4).

## Giải trình quan trọng về nguồn câu hỏi – đáp án

File gốc `MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx` **chỉ chứa Ma trận và Bản đặc tả** (bản thiết kế đề), **không chứa sẵn đề thi hay đáp án**. Đề thi thật dùng **ngữ liệu truyện thần thoại ngoài sách giáo khoa** do nhà trường chọn sau, nên không thể tồn tại “đáp án của đề thật” trước khi thi.

Vì vậy, tài liệu này:

1. Tái lập **chính xác 100% cấu trúc đề** từ Ma trận – Bản đặc tả: 11 câu (8 TNKQ + 2 tự luận đọc hiểu + 1 bài nghị luận), thang điểm 10 (Đọc hiểu 60% – Viết 40%), cấp độ Biết 40% – Hiểu 30% – Vận dụng 30%.
2. Dựng **hai đề minh hoạ 11 câu kèm đáp án và giải thích đầy đủ** trên hai ngữ liệu thần thoại *ngoài SGK* tiêu biểu (**Nữ Oa vá trời** – Trung Hoa; **Lạc Long Quân – Âu Cơ** – Việt Nam), cùng ngân hàng 12 câu trắc nghiệm lí thuyết thể loại. Đây là đề *minh hoạ luyện tập*, không phải đề thi thật của nhà trường.
3. Trang bị bộ khung kiến thức và phương pháp để học sinh giải mã **mọi** ngữ liệu thần thoại tương tự trong đề thật.

## Cấu trúc 8 phần

| Phần | Nội dung |
|---|---|
| 1 | Giải mã Ma trận & Bản đặc tả, cấu trúc 11 câu |
| 2 | Lí thuyết chuyên sâu truyện thần thoại (định nghĩa, phân loại, 6 đặc trưng, phân biệt thể loại) |
| 3 | Kĩ năng đọc hiểu 4 bước + phân tích mẫu *Nữ Oa vá trời* |
| 4 | Ngữ liệu *Lạc Long Quân – Âu Cơ* và ranh giới thần thoại/truyền thuyết |
| 5 | Hai đề minh hoạ 11 câu chuẩn ma trận + toàn bộ đáp án, giải thích |
| 6 | Chuyên đề Viết: nghị luận phân tích, đánh giá tác phẩm truyện (4 điểm) |
| 7 | Bài văn mẫu hoàn chỉnh + thang điểm chấm mẫu |
| 8 | Sổ tay ghi nhớ (20 flashcard), bảng từ khoá, lộ trình 7 ngày, chiến thuật 90 phút |

## Cách dựng lại PDF

Yêu cầu: Python 3.11+. Bộ font DejaVu (đầy đủ italic) được cài qua `matplotlib`; xuất PDF bằng `fpdf2`.

```bash
python3 -m venv .venv
.venv/bin/pip install fpdf2 matplotlib pymupdf
.venv/bin/python de-cuong-on-tap/bo-go/build_pdf.py
```

Mã nguồn nội dung đặt trong `bo-go/`: `pdf_engine.py` (engine bố cục), `part01..part09` (nội dung từng phần), `reading_texts.py` (ngữ liệu), `build_pdf.py` (trình điều phối, render hai lượt để mục lục có số trang chính xác).

## Phạm vi bám sách

Lí thuyết bám SGK **Ngữ văn 10 Kết nối tri thức với cuộc sống, Tập 1**, Bài 1 *Sức hấp dẫn của truyện kể* (chùm *Truyện về các vị thần sáng tạo thế giới* sưu tầm theo Nguyễn Đổng Chi; thực hành đọc *Tê-dê*). Hai ngữ liệu minh hoạ đều nằm ngoài SGK đúng yêu cầu của Bản đặc tả.
