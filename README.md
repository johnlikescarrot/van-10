# van-10 — Đề cương ôn tập Giữa học kì 1 Ngữ văn 10 (Kết nối tri thức)

Bộ tài liệu ôn thi được biên soạn **bám sát ma trận** trong file
`MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx`.

> **Nội dung:** ~27.700 từ · 6 phần · **6 đề đầy đủ (66 câu)** · 59 bảng · 3 bài văn mẫu · 10 dàn ý chi tiết.
> **Bản in:** [`DE-CUONG-ON-TAP-GIUA-KI-1-VAN-10.docx`](DE-CUONG-ON-TAP-GIUA-KI-1-VAN-10.docx) (A4, Times New Roman 13, có trang bìa + mục lục + 59 bảng).

## Điểm quan trọng nhất rút ra từ ma trận

File ma trận **chỉ có ma trận + đặc tả, không kèm câu hỏi cụ thể**. Từ đó suy ra cấu trúc đề:

- **11 câu / 10 điểm / 90 phút**, ngữ liệu đọc hiểu **hoàn toàn ngoài SGK**.
- Đọc hiểu 60%: 6 TN (Biết) + 2 TN (Hiểu) + 1 TL (Hiểu) + 1 TL (Vận dụng).
- Viết 40%: 1 bài nghị luận phân tích, đánh giá tác phẩm truyện.
- Tỉ lệ tư duy: **40% Biết – 30% Hiểu – 30% Vận dụng** (câu Viết được "trải" điểm ở cả 3 mức — xem Phần 1, mục 1.1.C).
- Dòng "tỉ lệ điểm từng loại câu hỏi" trong file gốc bị **lệch cột**, không khớp tổng 60/40; tài liệu đã hiệu chỉnh và giải thích cách chuẩn hoá.

Vì vậy bộ tài liệu **tự soạn 6 đề hoàn chỉnh đúng ma trận** (kèm đáp án) để luyện, thay vì sao chép đề có sẵn.

## Cấu trúc tài liệu

| Phần | Nội dung | Tệp |
|:---:|---|---|
| 1 | Giải mã ma trận & nền tảng thể loại thần thoại | [`docs/phan-1-…`](docs/phan-1-giai-ma-ma-tran-va-nen-tang-the-loai.md) |
| 2 | Hệ thống tác phẩm trọng tâm + 9 truyện mở rộng | [`docs/phan-2-…`](docs/phan-2-he-thong-tac-pham.md) |
| 3 | Kĩ năng đọc hiểu + **Đề số 1** + đáp án chi tiết | [`docs/phan-3-…`](docs/phan-3-ky-nang-doc-hieu-va-de-so-1.md) |
| 4 | **05 đề luyện tập** (Đề 2–6) + đáp án | [`docs/phan-4-…`](docs/phan-4-bo-nam-de-luyen-tap.md) |
| 5 | Chuyên đề **Viết**: nghị luận phân tích, đánh giá tác phẩm truyện | [`docs/phan-5-…`](docs/phan-5-chuyen-de-viet-nghi-luan.md) |
| 6 | Sổ tay ghi nhớ, 30 thẻ nhớ, kế hoạch ôn 7 ngày, checklist | [`docs/phan-6-…`](docs/phan-6-so-tay-ghi-nho-va-ke-hoach-on.md) |

### Nội dung nổi bật

- **Bộ 8 dấu hiệu thi pháp thần thoại** + *câu hỏi thi tương ứng* + *mẫu câu trả lời* (Phần 1).
- **Bảng phân biệt 5 thể loại** dễ nhầm: thần thoại – truyền thuyết – cổ tích – sử thi – truyền kì.
- **Hồ sơ 7 ô** cho từng tác phẩm: Thần Trụ Trời, Thần Sét, Thần Gió, Tản Viên từ Phán sự lục, Chữ người tử tù, Tê-dê.
- **9 truyện mở rộng** hay thành ngữ liệu đề thi (Prô-mê-tê, Nữ Oa, Bàn Cổ, Hậu nghệ, Đi san mặt đất, Nữ thần Mặt Trời – Mặt Trăng, Ông Trời, Thần Tử – Thần Sinh, Nữ thần Lúa).
- **6 đề**: mỗi đề 11 câu, có giải thích **từng phương án trắc nghiệm**, bài trả lời mẫu cho câu tự luận, dàn ý 4 luận điểm cho bài viết.
- **3 bài văn mẫu hoàn chỉnh** (~600 chữ/bài) + rubric 5 mức + 10 lỗi "giết điểm".

## Dựng lại bản .docx

```bash
pip install python-docx
python3 tools/build_docx.py
```

Script đọc 6 tệp Markdown trong `docs/` theo thứ tự, chuyển thành `.docx` khổ A4
(Times New Roman 13, tiêu đề có màu và đường kẻ, bảng kẻ khung, đánh số trang).
Sửa nội dung Markdown rồi chạy lại là bản in được cập nhật.

## Cấu trúc đề thi (tóm tắt)

| Câu | Hình thức | Mức độ | Điểm |
|:---:|:---:|:---:|:---:|
| 1–6 | TN | Biết | 0,5 × 6 = 3,0 |
| 7–8 | TN | Hiểu | 0,5 × 2 = 1,0 |
| 9 | TL | Hiểu | 1,0 |
| 10 | TL | Vận dụng | 1,0 |
| 11 | TL | Viết | 4,0 |
| | | **Tổng** | **10,0** |
