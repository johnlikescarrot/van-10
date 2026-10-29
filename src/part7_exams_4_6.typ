#import "template.typ": *
#import "assessment.typ": render-exam, render-answer
#let exams = json("exams.json")
#for e in exams.slice(3) { render-exam(e) }

#pagebreak()
== 6.2. Đáp án, hướng dẫn và bài viết tham khảo

Đáp án trắc nghiệm dựa vào chính bản kể của từng đề. “Căn cứ” là cụm từ có trong bản kể rút gọn ở đây, không phải lời trích từ một ấn bản sách. Các bài viết tham khảo đều nằm trong khoảng 600–800 đơn vị tách bằng khoảng trắng; cách đếm này giúp kiểm tra dung lượng, không thay quy định của người ra đề.

Thang chấm tự luận chỉ là đề xuất dùng cho tài liệu. Chấp nhận câu trả lời khác có lí lẽ, không trái văn bản; không trừ điểm vì học sinh không dùng từ hoa mĩ, không trích danh ngôn hoặc không so sánh truyện khác.

#for (i, e) in exams.enumerate() { render-answer(e, newpage: i > 0) }
