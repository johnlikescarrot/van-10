#import "template.typ": *
#let letters = ("A", "B", "C", "D")
#let paragraphs(value) = {
  for p in value.trim().split("\n\n") {
    block(above: 5pt, below: 5pt, breakable: true)[#text(p.trim())]
  }
}
#let options(q) = {
  for (i, c) in q.choices.enumerate() {
    block(above: 2pt, below: 2pt)[#letters.at(i). #c]
  }
}
#let source-note(id) = [Bản kể rút gọn do người biên soạn diễn đạt lại theo nguồn #id ở danh mục cuối tài liệu; không phải trích nguyên văn. Chỉ dùng bản in ở đây để trả lời.]

#let render-exam(e) = {
  pagebreak(weak: true)
  heading(level: 2)[Đề #e.number. #e.title]
  text(size: 9pt, fill: muted)[Tự luyện 90 phút · Đọc hiểu 6,0đ · Viết 4,0đ]
  if e.notice != "" { note(title: "Phạm vi ngữ liệu", e.notice) }
  heading(level: 3)[I. Đọc hiểu (6,0 điểm)]
  passage(e.title.split(" / ").first(), source-note(e.source), paragraphs(e.passage))
  [Chọn một đáp án cho mỗi câu 1–8; mỗi câu đúng được 0,5 điểm.]
  for (i, q) in e.questions.enumerate() {
    block(breakable: false, above: 9pt, below: 7pt)[
      *Câu #(i + 1).* #q.stem
      #options(q)
    ]
  }
  for (i, q) in e.short.enumerate() {
    block(above: 9pt, below: 9pt)[*Câu #(i + 9) (1,0 điểm).* #q.stem]
  }
  heading(level: 3)[II. Viết (4,0 điểm)]
  if e.extra != none {
    passage(e.extra.title, source-note(e.extra.source), paragraphs(e.extra.passage))
  }
  let title = if e.extra == none { e.title } else { e.extra.title }
  [*Câu 11.* Viết bài văn khoảng 600–800 chữ phân tích, đánh giá chủ đề và một số nét đặc sắc về hình thức nghệ thuật của truyện *#title* theo bản kể trong đề. Dung lượng này là yêu cầu tự luyện, không phải quy định của ma trận gốc.]
  v(8pt)
  line(length: 100%, stroke: 0.5pt + rgb("cad5db"))
  text(size: 9pt, fill: muted)[Dừng ở đây nếu đang bấm giờ. Chỉ mở phần đáp án sau khi hoàn thành bài.]
}

#let render-answer(e, newpage: true) = {
  if newpage { pagebreak(weak: true) }
  set text(size: 9.8pt)
  set par(leading: 0.5em)
  heading(level: 2)[Đáp án đề #e.number]
  [*Trắc nghiệm:* Mỗi câu đúng 0,5 điểm, tổng 4,0 điểm. Mức nhận thức ghi dưới đây phục vụ cấu trúc bộ đề: câu 1–6 nhận biết; câu 7–8 thông hiểu.]
  for (i, q) in e.questions.enumerate() {
    block(above: 5pt, below: 5pt)[
      *Câu #(i+1): #letters.at(q.answer)* · #q.indicator · #q.level\
      *Căn cứ trong bản kể:* “#q.evidence”.\
      #q.explanation
    ]
  }
  for (i, q) in e.short.enumerate() {
    heading(level: 3)[Câu #(i+9) · #q.indicators.join(", ") · 1,0 điểm]
    for r in q.rubric { block(above: 2pt, below: 2pt)[#str(r.points).replace(".", ",") đ: #r.text] }
    note(title: "Một cách trả lời", q.sample)
  }
  heading(level: 3)[Câu 11 · Gợi ý triển khai và chấm bài]
  [Dùng thang tự chấm ở mục 5.6, tổng 4,0 điểm. Các hướng phân tích sau là gợi ý, không phải những câu chữ phải chép.]
  for item in e.outline { block(above: 3pt, below: 3pt)[• #item] }
  [Chấp nhận cách hiểu khác có bằng chứng và lí lẽ. Không đòi hỏi đủ mọi ý trong bài tham khảo. Với câu 9–10, cho điểm phần đạt theo các ý nêu trên; không bắt buộc trùng mẫu và không thưởng cho việc chỉ viết dài. Với mục 0,5 điểm, có thể cho 0,25 điểm khi mới đạt một phần yêu cầu.]
  heading(level: 3)[Bài viết tham khảo đề #e.number]
  text(size: 9pt, fill: muted)[Bài do người biên soạn viết cho bản kể trong đề; dùng để quan sát lập luận, không học thuộc.]
  paragraphs(e.essay)
}
