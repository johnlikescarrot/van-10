# Đề cương ôn tập giữa học kì I — Ngữ văn 10 KNTT

Năm học **2026–2027** · Bản biên tập **29/10/2026**.

## Tải PDF

[**DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf**](./DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf)

Bản hiện tại có **60 trang A4**, mục lục có liên kết, 65 mục đánh dấu điều hướng và phông chữ tiếng Việt được nhúng. Thiết kế dùng nền sáng để đọc và in thuận tiện.

## Phạm vi

Căn cứ chính là tệp `MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx` trong kho:

| Phần | Yêu cầu | Điểm |
|---|---|---:|
| Đọc hiểu | Thần thoại ngoài SGK; 6 câu TN nhận biết, 2 câu TN thông hiểu, 1 câu TL thông hiểu, 1 câu TL vận dụng | 6,0 |
| Viết | Một bài nghị luận phân tích, đánh giá chủ đề và nghệ thuật truyện thần thoại ngoài SGK | 4,0 |
| Tổng | 90 phút; nhận biết 40%, thông hiểu 30%, vận dụng 30% | 10,0 |

Đây là tài liệu tự học theo **ma trận được cung cấp**, không phải đề thi, đáp án chính thức hoặc ma trận chung của Bộ GD&ĐT. Mức 0,5 điểm mỗi câu TN, cách đánh số câu, số chữ, lịch làm bài và rubric chi tiết là lựa chọn của bộ đề luyện. Khi thi phải theo yêu cầu giáo viên và đề thực tế.

“Ngoài SGK” ở đây là ngoài văn bản học của **Ngữ văn 10 Kết nối tri thức**. Một số truyện luyện có trong bộ Chân trời sáng tạo hoặc SGK lớp khác; không gọi chúng là ngoài mọi SGK.

## Nội dung

1. **Ma trận:** cơ cấu câu hỏi, điểm và bảng đối chiếu các yêu cầu.
2. **Tri thức truyện và thần thoại:** thuật ngữ, thể loại, văn bản liên hệ và bản đồ mô-típ.
3. **Tiếng Việt:** từ Hán Việt, tu từ, mạch lạc và liên kết.
4. **Đọc hiểu:** cách tìm bằng chứng; 40 câu luyện kèm đáp án.
5. **Viết:** yêu cầu kiểu bài; đọc bài tham khảo *Quà Giáng sinh*; phiếu tìm ý; hai cách lập dàn ý; đoạn phân tích; rubric tự chấm; quy trình sửa bài.
6. **Sáu đề luyện:** 66 câu, đáp án và sáu bài tham khảo khoảng 600–620 đơn vị cách nhau bằng khoảng trắng. Các bài mẫu được viết lại để minh họa lập luận, không để học thuộc.
7. **Ôn tập:** lịch bảy ngày, 24 thẻ tự hỏi và bảng tóm tắt.
8. **Phụ lục:** 11 nhóm nguồn, giới hạn đối chiếu, phiếu chữa đề và danh sách kiểm tra trước khi nộp.

## Những điểm sửa quan trọng

- Phân biệt dữ kiện ma trận gốc với hướng dẫn do người biên soạn đề xuất.
- Bỏ tỉ lệ ra đề, thống kê trí nhớ, cam kết điểm số và các danh ngôn thiếu nguồn kiểm chứng.
- Không đồng nhất ngôi thứ ba với toàn tri, người kể với tác giả/người sưu tầm.
- Sửa phần giải nghĩa yếu tố “nhân”, ví dụ dùng “yếu điểm” và nhận định máy móc rằng “đề cập đến” là thừa từ.
- Viết lại chuyên đề viết và sáu bài tham khảo, thống nhất rubric tự luyện 4 điểm.
- Cân lại vị trí đáp án đúng trong 48 câu TN của sáu đề; mỗi đề có hai đáp án A, B, C, D.
- Ghi rõ dị bản, ngữ liệu có biên tập và nguồn thứ cấp; không nhận là đã kiểm chứng trực tiếp các sách in.
- Không tiếp nhận lỗi trong bài mẫu được cung cấp rằng Huấn Cao là đại diện cái ác vì mang án tử tù.

Đọc [nhật kí đối chiếu](docs/RESEARCH_AND_REVIEW.md) để biết căn cứ và giới hạn. Không có cam kết rằng tài liệu đã được thẩm định độc lập bởi giáo viên hoặc sẽ không bao giờ cần đính chính.

## Dựng lại PDF

Cần Python 3.11 trở lên. Typst chạy qua gói Python đã ghim phiên bản; không cần cài riêng CLI, TeX hoặc tải phông chữ khi dựng.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python scripts/check.py
```

Phông **Be Vietnam Pro** và **Lora** nằm trong `fonts/`, kèm giấy phép SIL Open Font License của từng họ. Các tệp nguồn Typst nằm trong `src/`; `src/main.typ` ghép toàn bộ tài liệu. Sửa tệp nguồn, rồi dựng và kiểm tra lại PDF cùng tên ở thư mục gốc.

## Kiểm tra

`scripts/check.py` kiểm tra:

- sáu đề, mỗi đề đủ câu 1–11; đủ bốn lựa chọn cho từng câu TN và đủ khóa đáp án;
- số câu theo nhóm nhận biết/thông hiểu; phân bố vị trí đáp án;
- sáu bài tham khảo trong khoảng 600–800 đơn vị tách bằng khoảng trắng;
- tổng điểm đề luyện và tổng rubric viết;
- khổ A4, mục đánh dấu, liên kết, nhúng phông, trang gần trống, kí tự lỗi và chữ vượt biên trang.

Đây là kiểm tra cấu trúc và xuất bản, **không chứng minh mọi diễn giải văn học hoặc đáp án đều đúng**. Cần đọc duyệt nội dung và xem trang sau mỗi lần sửa lớn. CI dựng PDF và chạy các kiểm tra này cho PR; có thể tải bản dựng trong artifact của workflow.
