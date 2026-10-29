#import "template.typ": *
#let sources = json("../research/sources.json")
#part-banner("PHỤ LỤC", "Nguồn đối chiếu và ghi chú biên soạn", "Kiểm tra ngày 29/10/2026. Mã S1–S11 được dùng trong các phần và ngữ liệu.")

== A. Cách dùng nguồn

Ưu tiên S1 cho cấu trúc ôn tập. S2 là bài hướng dẫn thứ cấp để đối chiếu yêu cầu viết, không thay thế bản SGK của học sinh. S3 là văn bản quản lí qua bản đăng lại. S4–S11 là các bản kể hoặc hướng dẫn phổ thông trên web, dùng để chọn tình tiết cho bản luyện do người biên soạn diễn đạt lại; không phải khảo cứu văn bản học hay xác minh một ấn bản sách.

Những câu hỏi, đáp án, thang tự chấm, bài viết tham khảo, lịch học và thẻ tự hỏi do người biên soạn xây dựng. Các cụm đặt trong ngoặc kép ở đáp án đề là bằng chứng lấy từ bản luyện đi kèm. Không chép bài văn mẫu của các website. Không đưa những danh ngôn chưa xác minh vào đề cương.

== B. Danh mục có liên kết

Bấm tên nguồn để mở trang đối chiếu. Tên tệp của S1 được ghi ngay dưới mục; toàn bộ URL và ghi chú sử dụng có trong tệp nghiên cứu kèm mã nguồn.

#for s in sources {
  block(above: 10pt, below: 10pt)[
    *#s.id.* #if "url" in s { link(s.url, s.title) } else { s.title }\
    #text(size: 9pt, fill: muted)[#s.kind · kiểm tra #s.checked]

    #s.use
    #if "path" in s { parbreak(); text(size: 8.5pt)[Tệp: #s.path] }
  ]
}

== C. Phạm vi còn phải đối chiếu với giáo viên

Không có hướng dẫn chấm chính thức, đề kiểm tra thật, tên đơn vị ban hành ma trận hoặc danh sách ngữ liệu dự kiến trong tệp cung cấp. Không suy đoán các thông tin đó. Việc rút gọn giúp tự luyện nhưng làm giảm độ dài, độ phức tạp so với nhiều bản truyện đầy đủ; cần luyện thêm văn bản chưa đọc theo nguồn giáo viên chọn.

Bản cập nhật này là một mốc xuất bản đã kiểm tra, không phải cam kết rằng sẽ không bao giờ cần sửa. Khi nhà trường thay đổi phạm vi, cấu trúc hoặc hướng dẫn, cập nhật theo thông báo mới. Có thể báo lỗi bằng cách ghi rõ trang, câu, bằng chứng và cách sửa đề xuất.
