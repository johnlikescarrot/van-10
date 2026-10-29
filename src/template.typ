#let navy = rgb("18344b")
#let teal = rgb("126a70")
#let muted = rgb("52616b")
#let pale = rgb("edf5f5")

#let note(title: "Lưu ý", body) = block(
  width: 100%, inset: 11pt, fill: pale,
  stroke: (left: 2pt + teal), radius: 3pt,
  breakable: true, above: 9pt, below: 9pt,
)[*#title*\ #body]

#let study-table(columns, headers, ..cells) = {
  set text(size: 9pt)
  table(
    columns: columns, inset: 6pt, stroke: 0.4pt + rgb("cad5db"),
    fill: (x, y) => if y == 0 { navy } else if calc.odd(y) { rgb("f4f7f8") },
    table.header(..headers.map(h => text(fill: white, weight: "bold", h))),
    ..cells.pos(),
  )
}

#let part-banner(number, title, subtitle) = {
  pagebreak(weak: true)
  text(size: 9pt, fill: teal, weight: "bold", number)
  heading(level: 1, title)
  text(size: 10pt, fill: muted, subtitle)
  v(8pt)
}

#let passage(title, source, body) = block(
  width: 100%, inset: 12pt, fill: rgb("faf8f2"),
  stroke: 0.5pt + rgb("d4cdbc"), radius: 3pt, breakable: false,
)[
  *#title*

  #body

  #text(size: 8.5pt, fill: muted)[#source]
]

#let project-doc(body) = {
  set document(title: "Đề cương ôn tập giữa kì I Ngữ văn 10 KNTT 2026–2027", date: datetime(year: 2026, month: 10, day: 29))
  set page(paper: "a4", margin: (top: 20mm, bottom: 20mm, x: 19mm),
    header: context {
      if counter(page).get().first() > 1 {
        set text(size: 7.5pt, fill: muted)
        [NGỮ VĂN 10 · KẾT NỐI TRI THỨC #h(1fr) GIỮA KÌ I · 2026–2027]
        line(length: 100%, stroke: 0.4pt + rgb("cad5db"))
      }
    },
    footer: context {
      if counter(page).get().first() > 1 {
        set text(size: 8pt, fill: muted)
        [Tài liệu tự học · Không thay thế hướng dẫn của nhà trường #h(1fr) #counter(page).display("1 / 1", both: true)]
      }
    },
  )
  set text(font: "Be Vietnam Pro", lang: "vi", size: 10.5pt, fill: rgb("20303c"))
  set par(justify: true, leading: 0.65em, spacing: 0.7em)
  set heading(numbering: none)
  show heading.where(level: 1): set text(size: 19pt, fill: navy)
  show heading.where(level: 2): set text(size: 13pt, fill: teal)
  show heading.where(level: 3): set text(size: 11pt, fill: navy)
  show link: set text(fill: teal)
  show outline.entry: set text(size: 9pt)

  page(header: none, footer: none, margin: 0mm)[
    #rect(width: 100%, height: 100%, fill: navy, stroke: none)[
      #pad(x: 23mm, top: 28mm)[
        #text(size: 10pt, fill: rgb("a5d8d5"))[KẾT NỐI TRI THỨC VỚI CUỘC SỐNG]
        #v(24mm)
        #text(size: 31pt, weight: "bold", fill: white)[ĐỀ CƯƠNG\ ÔN TẬP GIỮA KÌ I]
        #v(8mm)
        #text(size: 24pt, weight: "bold", fill: rgb("f1ce81"))[NGỮ VĂN 10]
        #v(6mm)
        #text(size: 14pt, fill: white)[Năm học 2026–2027]
        #v(15mm)
        #line(length: 60mm, stroke: 2pt + rgb("f1ce81"))
        #v(9mm)
        #text(size: 12pt, fill: white)[Đọc hiểu thần thoại\ Viết bài nghị luận phân tích, đánh giá tác phẩm truyện]
        #v(17mm)
        #block(fill: rgb("24465b"), inset: 13pt, width: 100%, radius: 4pt)[
          #text(size: 11pt, fill: white)[90 phút · 11 câu · 10 điểm\ 40 câu luyện kĩ năng · 6 đề tự luyện\ Đáp án có căn cứ · Bài viết tham khảo]
        ]
        #v(14mm)
        #text(size: 9pt, fill: rgb("cfdee5"))[Bản biên tập ngày 29/10/2026\ Căn cứ ma trận được cung cấp trong kho tài liệu.\ Các đề và thang chấm chi tiết là tài liệu luyện tập.]
      ]
    ]
  ]

  heading(level: 1, outlined: false)[Cách dùng đề cương]
  [Nếu còn một tuần, học theo lịch ở Phần VII. Nếu chỉ còn một buổi, đọc Phần I, mục 5.2 và trang tóm lược cuối tài liệu, sau đó làm một đề trong 90 phút. Che đáp án trước khi làm; ghi lại lỗi và tự trả lời lại vào hôm sau.]
  note(title: "Phạm vi và mức độ xác nhận")[
    Ma trận gốc trong kho quy định đọc hiểu thần thoại và viết nghị luận về tác phẩm truyện thần thoại ngoài SGK. Tài liệu này không phải đề thi hoặc hướng dẫn chấm do Bộ GD&ĐT hay một nhà trường ban hành. Những mốc thời gian, dung lượng và mức điểm nhỏ dùng để tự luyện đều được ghi là gợi ý.

    Các văn bản luyện tập là bản kể rút gọn do người biên soạn diễn đạt lại từ nguồn được nêu ở cuối tài liệu; không phải bản chép nguyên văn SGK hay sách in. Đề 4, 5, 6 có ngữ liệu từng xuất hiện trong SGK khác hoặc cấp học khác, chỉ dùng để chuyển giao kĩ năng; không gọi chúng là ngữ liệu mới tuyệt đối.
  ]
  [*Ba việc cần làm:* (1) đối chiếu đề cương của giáo viên; (2) học cách chỉ ra bằng chứng trong văn bản; (3) tự viết và sửa bài, không học thuộc bài mẫu.]
  heading(level: 1, outlined: false)[Mục lục]
  outline(title: none, depth: 2, indent: 10pt)
  body
}
