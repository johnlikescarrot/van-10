# Đề cương ôn tập GIỮA HỌC KÌ I — Ngữ văn 10 (Kết nối tri thức với cuộc sống)

**Năm học 2026 – 2027** · Biên soạn bám sát **ma trận + bản đặc tả** trong file
`MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx` của nhà trường.

---

## 📥 Bản in sẵn

| Tệp | Mô tả |
|---|---|
| [`output/De-cuong-on-tap-Giua-ki-1-Ngu-van-10.docx`](output/De-cuong-on-tap-Giua-ki-1-Ngu-van-10.docx) | **Bản hoàn chỉnh để in** — bìa, mục lục, 7 phần, 83 bảng, đánh số trang (A4, Times New Roman 12.5) |

Dựng lại bản in sau khi sửa Markdown:

```bash
pip install python-docx
python3 build_docx.py
```

---

## 📚 Cấu trúc tài liệu

| Phần | Tệp | Nội dung | Dùng để |
|---|---|---|---|
| **I** | [`de-cuong/01-the-loai-than-thoai-va-truyen-ke.md`](de-cuong/01-the-loai-than-thoai-va-truyen-ke.md) | Thể loại thần thoại, 6 khái niệm gốc của truyện kể, hệ thống 4 văn bản SGK, mở rộng ngoài SGK, bảng so sánh 5 thể loại | Học nền, chống mất điểm 40% "Biết" |
| **II** | [`de-cuong/02-ky-nang-doc-hieu-va-dang-cau-hoi.md`](de-cuong/02-ky-nang-doc-hieu-va-dang-cau-hoi.md) | 12 dạng câu hỏi đọc hiểu + khung trả lời + câu mẫu + 10 lỗi mất điểm | Luyện phản xạ làm bài |
| **III** | [`de-cuong/03-thuc-hanh-tieng-viet-tu-han-viet.md`](de-cuong/03-thuc-hanh-tieng-viet-tu-han-viet.md) | Từ Hán Việt: khái niệm, phân loại, sắc thái, 4 lỗi, 60 yếu tố gốc, bài tập + đáp án | Trắc nghiệm + nâng cấp câu văn |
| **IV** | [`de-cuong/04-ky-nang-viet-nghi-luan.md`](de-cuong/04-ky-nang-viet-nghi-luan.md) | Dàn ý vạn năng, 7 nhóm luận điểm, 12 câu hỏi tự vấn, 2 bài viết mẫu, kho dẫn chứng | Ăn trọn 40% điểm Viết |
| **V** | [`de-cuong/05-de-kiem-tra-chuan-ma-tran-va-dap-an.md`](de-cuong/05-de-kiem-tra-chuan-ma-tran-va-dap-an.md) | **Đề 11 câu dựng đúng 100% ma trận** + đáp án chi tiết + rubric + bảng tự chấm | Làm thử, tự chấm |
| **VI** | [`de-cuong/06-bo-de-luyen-tap.md`](de-cuong/06-bo-de-luyen-tap.md) | 3 đề nữa (Nữ thần Mặt Trời – Mặt Trăng; Cóc kiện Trời; Prô-mê-tê) + đáp án | Luyện thêm |
| **VII** | [`de-cuong/07-so-tay-ghi-nho-va-lich-on.md`](de-cuong/07-so-tay-ghi-nho-va-lich-on.md) | Lịch ôn 7 ngày, 6 trang ghi nhớ in dán, 40 flashcard, sơ đồ tư duy, checklist, phụ lục Bài 2 | Ôn nước rút |

---

## ⚠️ Về "đề và đáp án" trong file nguồn

File `.docx` nguồn **chỉ chứa ma trận và bản đặc tả**, **không chứa đề bài, ngữ liệu hay câu hỏi cụ thể** (đã kiểm tra toàn bộ `word/document.xml`: 3.616 ký tự, 2 bảng, 0 tệp đính kèm).

Vì vậy **Phần V** không "chép lại đề" mà **dựng lại một đề hoàn chỉnh**:

- đúng **11 câu** (6 TN nhận biết + 2 TN thông hiểu + 1 TL thông hiểu + 1 TL vận dụng + 1 TL viết);
- đúng **tỉ lệ 60% Đọc hiểu / 40% Viết**, đúng **4 mức độ 40–30–30**;
- bám **từng dòng** yêu cầu trong bản đặc tả (có bảng đối chiếu từng câu);
- dùng **ngữ liệu ngoài SGK** đúng như ma trận quy định;
- kèm **đáp án chi tiết, thang điểm từng ý, hướng dẫn chấm và rubric**.

Đây là dạng đề mà bất kỳ giáo viên nào bám ma trận này cũng sẽ ra — nên dùng để luyện là luyện đúng hướng. Nếu trường đã phát đề in sẵn, hãy đối chiếu cấu trúc: sẽ trùng khớp.

---

## 🎯 Ba con số cần nhớ

| Con số | Ý nghĩa |
|---|---|
| **11** | Số câu của đề (8 TN + 2 TL đọc hiểu + 1 TL viết) |
| **60/40** | 60% Đọc hiểu (thần thoại, ngữ liệu ngoài SGK) — 40% Viết (nghị luận về tác phẩm truyện) |
| **4** | Bốn thứ đề đọc hiểu luôn hỏi: **thời gian – không gian – cốt truyện – nhân vật** |

---

## 🔧 Cấu trúc kho

```
van-10/
├── MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx   ← nguồn
├── de-cuong/              ← 7 phần Markdown (nguồn biên soạn)
├── output/                ← bản .docx để in
├── build_docx.py          ← script dựng bản in
└── README.md
```
