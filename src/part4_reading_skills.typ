#import "template.typ": *
#import "assessment.typ": options, letters, paragraphs, source-note
#let bank = json("bank.json")
#part-banner("PHẦN IV", "Kĩ năng đọc hiểu và 40 câu luyện", "28 câu trắc nghiệm, 12 câu tự luận. Có ngữ liệu, đáp án và tiêu chí tự kiểm tra.")

#set text(size: 10pt)
#set par(leading: 0.55em)

== 4.1. Làm trắc nghiệm bằng căn cứ

Đọc câu hỏi trước khi chọn đáp án. Khoanh các từ *theo văn bản, chủ yếu, không, đúng nhất*. Với câu nhận biết, tìm câu hoặc chi tiết tương ứng. Với câu thông hiểu, kiểm tra nhận xét có giải thích được các chi tiết chính hay chỉ nói đúng một phần nhỏ.

Loại phương án vì *trái văn bản, thêm dữ kiện, nhầm vai trò, khái quát quá mức* hoặc *không trả lời điều được hỏi*. Không chọn theo độ dài đáp án, số lần xuất hiện chữ B, hay một từ khoá thần thoại đứng riêng. Các phương án trong tài liệu cố ý có cả lỗi ghép dị bản và lỗi suy rộng để luyện cách kiểm tra.

== 4.2. Trả lời tự luận đúng lệnh

*Nhận diện / chỉ ra:* trả lời thẳng, đưa dấu hiệu nếu cần. *Tóm tắt:* giữ sự việc chính và quan hệ trước sau, không bình luận. *Lí giải / phân tích:* nêu nhận xét, bằng chứng rồi giải thích chức năng. *Bài học / tác động:* nêu điều rút ra, căn cứ trong truyện và việc có thể làm. *Đánh giá:* nêu quan điểm, lí lẽ và giới hạn cần thiết.

Không dùng một công thức cố định cho mọi câu 9 hoặc 10. Nếu đề hỏi người kể, không trả lời thành bài học đạo đức; nếu đề hỏi tác động bản thân, không chỉ chép chủ đề. Số câu, số dòng chỉ tuân theo lệnh đề. Nhiều câu tự luận ngắn có thể trả lời bằng các ý rõ; chỉ bắt buộc đoạn liền khi đề yêu cầu đoạn văn.

#note(title: "Tự kiểm tra một câu phân tích")[
  Tôi đã trả lời đúng động từ của câu hỏi chưa? Có chi tiết nào làm căn cứ? Tôi đã nói chi tiết ấy có tác dụng gì chưa? Có phần nào lấy từ bản khác hoặc suy rộng quá mức không?
]

== 4.3. Ngữ liệu cho ngân hàng câu hỏi

Bốn đoạn sau do người biên soạn rút gọn từ các bản kể dùng trong bộ đề. Chúng là ngữ liệu luyện thao tác, không phải bốn trích dẫn nguyên văn sách. Mỗi câu ghi A, B, C hoặc D để chỉ đoạn cần đọc; các câu 1–7 dùng A, 8–14 dùng B, 15–21 dùng C, 22–28 dùng D.

#for p in bank.passages {
  passage(p.title, source-note(p.source), text(p.text))
  v(6pt)
}

== 4.4. Câu 1–28: trắc nghiệm

#for q in bank.questions {
  block(breakable: false, above: 9pt, below: 7pt)[
    *Câu #q.number* (#("ABCD".at(q.group))). #q.stem
    #options(q)
  ]
}

== 4.5. Câu 29–40: tự luận

Các câu này luyện riêng từng kĩ năng, không phải một bài kiểm tra 90 phút. Làm 3–4 câu mỗi buổi rồi tự đối chiếu tiêu chí.

#for q in bank.short {
  block(above: 8pt, below: 8pt)[*Câu #q.number* (#("ABCD".at(q.group))). #q.stem]
}

#pagebreak()
== 4.6. Đáp án và căn cứ câu 1–28

#for q in bank.questions {
  block(above: 6pt, below: 6pt)[*#q.number. #letters.at(q.answer)* · #q.indicator. #q.explanation]
}

== 4.7. Hướng dẫn câu 29–40

Tự kiểm tra theo hai tiêu chí mỗi câu; mỗi tiêu chí có thể ghi *đạt / cần sửa*. Các câu này không có điểm chính thức. Một cách diễn đạt khác vẫn đạt nếu trả lời đúng, có căn cứ.

#for q in bank.short {
  block(above: 9pt, below: 8pt)[
    *Câu #q.number* · #q.indicators.join(", ")\
    *Tiêu chí:* #q.criteria.join(" ")

    #q.sample
  ]
}
