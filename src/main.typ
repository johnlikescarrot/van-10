#set document(title: "Đề cương ôn tập giữa kì I Ngữ văn 10 Kết nối tri thức 2026–2027", author: "Tài liệu ôn tập Ngữ văn 10")
#set page(paper: "a4", margin: (x: 21mm, top: 20mm, bottom: 20mm), header: context [#set text(size: 8pt, fill: rgb("#64748b")); NGỮ VĂN 10 · KẾT NỐI TRI THỨC #h(1fr) ÔN TẬP GIỮA KÌ I], footer: context [#set text(size: 8pt, fill: rgb("#64748b")); 2026–2027 #h(1fr) #counter(page).display()])
#set text(font: "DejaVu Sans", lang: "vi", size: 10pt, fill: rgb("#202c3b"))
#set par(justify: true, leading: 0.68em, spacing: 0.8em)
#set heading(numbering: none)
#show heading.where(level: 1): it => block(above: 13pt, below: 7pt, breakable: false)[#text(size: 15pt, weight: "bold", fill: rgb("#164b73"))[#it.body] #v(3pt) #line(length: 100%, stroke: 1pt + rgb("#4a9b9a"))]
#show heading.where(level: 2): it => block(above: 8pt, below: 4pt, breakable: false)[#text(size: 11.3pt, weight: "bold", fill: rgb("#17645f"))[#it.body]]
#import "styles.typ": *
#align(center)[
  #v(26mm)
  #text(size: 12pt, weight: "bold", fill: rgb("#17645f"))[KẾT NỐI TRI THỨC VỚI CUỘC SỐNG]
  #v(12mm)
  #text(size: 25pt, weight: "bold", fill: rgb("#164b73"))[ĐỀ CƯƠNG ÔN TẬP\ GIỮA HỌC KÌ I]
  #v(7mm)
  #text(size: 19pt, weight: "bold")[NGỮ VĂN 10]
  #v(5mm)
  #text(size: 13pt)[NĂM HỌC 2026–2027]
  #v(15mm)
  #line(length: 65%, stroke: 2pt + rgb("#36938d"))
  #v(12mm)
  #text(size: 11pt)[Đọc hiểu thần thoại ngoài SGK\ Viết bài nghị luận phân tích, đánh giá truyện\ Ba đề luyện tập và hướng dẫn tự chấm]
  #v(19mm)
  #text(size: 9pt)[Biên soạn theo ma trận trong kho tài liệu.\ Điểm chi tiết của đề luyện là phương án minh họa.]
]
#pagebreak()
#outline(title: [Mục lục], depth: 2, indent: auto)
#pagebreak()
#include "guide.typ"
#include "extra.typ"
#include "practice.typ"
#include "answers.typ"
#include "references.typ"
