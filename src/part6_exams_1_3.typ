#import "template.typ": *
#import "assessment.typ": render-exam
#let exams = json("exams.json")
#part-banner("PHẦN VI", "Sáu đề tự luyện 90 phút", "Làm đề trước, đọc đáp án sau. Mỗi đề có 8 câu trắc nghiệm, 2 câu tự luận và 1 bài viết.")

== 6.1. Chọn đề và ghi kết quả

Đề 1–3 dùng một ngữ liệu cho cả đọc hiểu và viết. Đề 4–5 có văn bản riêng cho phần viết. Đề 6 dùng một ngữ liệu. Đây là hai cách tổ chức để luyện tập, không kèm dự báo xác suất ra thi.

Đề 4 và 6 có truyện trong SGK Chân trời sáng tạo; Đề 5 có truyện đã xuất hiện ở cấp học khác và có phân loại giao thoa. Dùng các đề đó để luyện chuyển giao kĩ năng. Không dùng cả sáu đề như một tập ngữ liệu đủ điều kiện mới hoàn toàn cho kiểm tra chính thức. Nếu giáo viên yêu cầu ngoài mọi SGK hoặc ngoài toàn bộ văn bản từng học, cần chọn nguồn khác đã đối chiếu.

Các bản kể ngắn giúp tập trung vào thao tác phân tích. Độ dài và độ khó này không dự báo độ dài ngữ liệu hoặc mức độ của đề trường. Khi đã làm tốt, nên nhờ giáo viên giao thêm một văn bản dài, nguyên bản và chưa đọc để tự kiểm tra khả năng chuyển giao.

*Phiếu ghi kết quả:* Đề … / ngày … / TN … trên 4 / TL … trên 2 / viết … trên 4 / tổng … trên 10 / thời gian … / lỗi cần làm lại …

#for e in exams.slice(0, 3) { render-exam(e) }
