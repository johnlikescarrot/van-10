# Đề cương ôn tập kiểm tra giữa học kì I — Ngữ văn 10 (2026–2027)

Tài liệu ôn tập chuyên sâu, biên soạn từ tệp **MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx** trong repo, đối chiếu với SGK *Ngữ văn 10 – Kết nối tri thức với cuộc sống*, chương trình GDPT 2018 và các đề kiểm tra giữa kì I cùng bộ sách.

## 📄 Bản phát hành chính

**[`De-cuong-on-tap-GK1-Ngu-van-10-2026-2027.pdf`](De-cuong-on-tap-GK1-Ngu-van-10-2026-2027.pdf)** — ấn bản A4, 83 trang, phông chữ DejaVu nhúng (hiển thị đầy đủ dấu tiếng Việt), có bìa, mục lục tự động, đánh số trang, bảng màu, sơ đồ tư duy và khung gọi nhớ. Đây là file để **in và học**.

Bản Markdown tổng hợp để chỉnh sửa: [`DE-CUONG-TONG-HOP-GIUA-KI-1-NGU-VAN-10-2026-2027.md`](DE-CUONG-TONG-HOP-GIUA-KI-1-NGU-VAN-10-2026-2027.md). Từng chương nằm trong thư mục [`docs/`](docs/).

## Nội dung chính

| Phần | Nội dung |
|---|---|
| 1 | Giải mã ma trận & bản đặc tả: suy luận cấu trúc **11 câu / 10 điểm / 90 phút**, mã hóa **22 chỉ báo năng lực**, chiến lược làm bài, 7 điểm mù thường gặp |
| 2 | Khoa học ghi nhớ: gọi nhớ chủ động, lặp lại ngắt quãng, đan xen, mã hóa kép; **lịch ôn 14 ngày**, 20 thẻ nhớ lõi, bảng chẩn đoán lỗi |
| 3 | Tri thức Ngữ văn: 10 khái niệm gốc, 9 đặc trưng thần thoại, tư duy vạn vật hữu linh, công cụ **7 tầng đọc**, bảng so sánh 6 thể loại, đối chiếu 3 hệ thần thoại, 10 mô-típ, bối cảnh lịch sử – văn hóa |
| 4 | **Toàn bộ chương trình học kì I**: bản đồ 5 bài học, 19 văn bản / 9 thể loại, 4 nội dung thực hành tiếng Việt, 5 kiểu bài viết, hoạt động nói – nghe, bản đồ liên kết chủ đề |
| 5 | Biến 22 chỉ báo thành công cụ trả lời: quy trình 7 bước đọc, khung K–G–D–B, 5 bước loại trừ TNKQ, 5 căn cứ xác định chủ đề, cấu trúc câu vận dụng |
| 6 | Viết bài nghị luận phân tích – đánh giá tác phẩm truyện (4,0 điểm): cấu trúc 6 đoạn, 8 nhóm luận điểm, 20 câu mở / chuyển / kết, **3 bài mẫu hoàn chỉnh**, rubric 4,0 điểm, 15 lỗi thường gặp |
| 7 | **Ngân hàng 72 câu hỏi có đáp án**: 60 TNKQ + 12 tự luận ngắn, gắn mã chỉ báo, kèm giải thích phương án nhiễu |
| 8–10 | **5 đề kiểm tra mô phỏng đủ 11 câu** (60/40, 90 phút) + **1 đề dự phòng**: ngữ liệu thần thoại ngoài SGK (*Ông Trời, Bàn Cổ, Nữ thần Mặt Trời và Mặt Trăng, Prô-mê-tê, Cóc kiện Trời, Nữ thần Lúa, Thần Nông*); mỗi đề có đáp án giải thích từng phương án, thang điểm từng ý và bài viết mẫu |
| 11 | Lịch ôn bản in, 40 thẻ ghi nhớ, sơ đồ tư duy A4, checklist 3 thời điểm, từ Hán Việt & lỗi chính tả, bảng tự chấm 11 câu, danh mục tài liệu tham khảo |

## Phát hiện quan trọng từ tệp nguồn

Tệp DOCX của nhà trường **chỉ gồm 3 nội dung**: mục tiêu đề kiểm tra, ma trận và bản đặc tả. **Không có đề thi, ngữ liệu hay đáp án**. Vì vậy:

- Mọi đề trong tài liệu này là **đề mô phỏng phục vụ ôn tập**, không phải đề chính thức.
- Cấu trúc 11 câu / 10 điểm được **suy luận** từ các tỉ lệ 60/40, 30/10/10/20/30 và 40/30/30 trong ma trận; điểm chi tiết từng câu có thể do tổ chuyên môn điều chỉnh.
- Ngữ liệu thần thoại được **kể lại / biên soạn lại** từ các cốt truyện dân gian phổ biến; nguồn tham khảo được ghi rõ ở Phần 11.7.

## Cách tạo lại PDF

```bash
python3 -m venv .venv
.venv/bin/pip install reportlab
.venv/bin/python tools/build_pdf.py
```

`tools/build_pdf.py` đọc các chương trong `docs/`, ghi bản Markdown tổng hợp và dựng PDF. Phông chữ nằm trong `tools/fonts/` (giấy phép `LICENSE_DEJAVU.txt`); `tools/patch_font.py` tạo lại `DejaVuMonoVN.ttf` — biến thể DejaVu Sans Mono được bổ sung glyph tiếng Việt để các sơ đồ ASCII vẫn thẳng cột.

## Cấu trúc repo

```
De-cuong-on-tap-GK1-Ngu-van-10-2026-2027.pdf   ← bản PDF phát hành
DE-CUONG-TONG-HOP-GIUA-KI-1-NGU-VAN-10-2026-2027.md
docs/00 … docs/10                               ← 11 chương Markdown
tools/build_pdf.py                              ← trình dựng PDF
tools/patch_font.py                             ← tạo font mono có dấu tiếng Việt
tools/fonts/                                    ← DejaVu TTF + giấy phép
MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx  ← nguồn
```

> Theo yêu cầu của người dùng, mọi thay đổi được gửi qua **pull request** và **không được merge**.
