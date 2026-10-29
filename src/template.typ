// ============================================================================
// HỆ THỐNG ĐỊNH DẠNG HỌC THUẬT & TỐI ƯU GHI NHỚ (DESIGN SYSTEM)
// Đề cương ôn tập Giữa kì I Ngữ văn 10 - Kết nối tri thức (2026-2027)
// ============================================================================

#let c-navy      = rgb("#14284B")
#let c-indigo    = rgb("#1E4976")
#let c-blue-soft = rgb("#EEF4FB")
#let c-blue-bdr  = rgb("#B8D0EB")

#let c-red       = rgb("#B42318")
#let c-red-soft  = rgb("#FEF3F2")
#let c-red-bdr   = rgb("#FECDCA")

#let c-amber     = rgb("#B54708")
#let c-gold      = rgb("#D97706")
#let c-gold-soft = rgb("#FFFAEB")
#let c-gold-bdr  = rgb("#FEDF89")

#let c-teal      = rgb("#0F6CBD")
#let c-jade      = rgb("#0E6F5C")
#let c-jade-soft = rgb("#ECFDF3")
#let c-jade-bdr  = rgb("#ABEFC6")

#let c-purple      = rgb("#5925DC")
#let c-purple-soft = rgb("#F4F3FF")
#let c-purple-bdr  = rgb("#D9D6FE")

#let c-slate      = rgb("#344054")
#let c-muted      = rgb("#667085")
#let c-bg-neutral = rgb("#F8FAFC")
#let c-border     = rgb("#D0D5DD")
#let c-ink        = rgb("#182230")

#let font-sans  = ("Be Vietnam Pro", "DejaVu Sans")
#let font-serif = ("Lora", "DejaVu Serif")

// Nhãn cấp độ nhận thức (Badges)
#let badge(label, bg: c-blue-soft, fg: c-indigo, bdr: c-blue-bdr) = box(
  fill: bg,
  stroke: 0.6pt + bdr,
  radius: 3pt,
  inset: (x: 5pt, y: 2pt),
  baseline: 15%,
  text(font: font-sans, size: 7.8pt, weight: "bold", fill: fg, label)
)

#let badge-biet = badge("NHẬN BIẾT", bg: rgb("#EFF8FF"), fg: rgb("#175CD3"), bdr: rgb("#B2DDFF"))
#let badge-hieu = badge("THÔNG HIỂU", bg: rgb("#FFFAEB"), fg: rgb("#B54708"), bdr: rgb("#FEDF89"))
#let badge-vd   = badge("VẬN DỤNG", bg: rgb("#ECFDF3"), fg: rgb("#067647"), bdr: rgb("#ABEFC6"))

// Hộp Khẩu quyết ghi nhớ nhanh (Mnemonic Hook)
#let mnemonic-box(title: "KHẨU QUYẾT GHI NHỚ TỐC ĐỘ CAO", body) = block(
  width: 100%,
  fill: c-gold-soft,
  stroke: (left: 3.5pt + c-gold, top: 0.6pt + c-gold-bdr, right: 0.6pt + c-gold-bdr, bottom: 0.6pt + c-gold-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: false,
  above: 9pt,
  below: 9pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-amber, tracking: 0.3pt)[★ #upper(title)]
  #v(4pt)
  #set text(size: 9.6pt, fill: c-ink)
  #body
]

// Hộp Cảnh báo Bẫy Phòng Thi (Exam Trap Box)
#let trap-box(title: "CẢNH BÁO BẪY MẤT ĐIỂM PHÒNG THI", body) = block(
  width: 100%,
  fill: c-red-soft,
  stroke: (left: 3.5pt + c-red, top: 0.6pt + c-red-bdr, right: 0.6pt + c-red-bdr, bottom: 0.6pt + c-red-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: false,
  above: 9pt,
  below: 9pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-red, tracking: 0.3pt)[▲ #upper(title)]
  #v(4pt)
  #set text(size: 9.5pt, fill: c-ink)
  #body
]

// Hộp Công thức Làm bài / Khung Tư duy (Formula Box)
#let formula-box(title: "CÔNG THỨC TƯ DUY & KĨ THUẬT LÀM BÀI", breakable-box: false, body) = block(
  width: 100%,
  fill: c-blue-soft,
  stroke: (left: 3.5pt + c-indigo, top: 0.6pt + c-blue-bdr, right: 0.6pt + c-blue-bdr, bottom: 0.6pt + c-blue-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: breakable-box,
  above: 9pt,
  below: 9pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-indigo, tracking: 0.3pt)[◆ #upper(title)]
  #v(4pt)
  #set text(size: 9.6pt, fill: c-ink)
  #body
]

// Hộp Đáp án / Hướng dẫn chấm chuẩn (Answer & Rubric Box)
#let answer-box(title: "ĐÁP ÁN & HƯỚNG DẪN CHẤM CHI TIẾT", body) = block(
  width: 100%,
  fill: c-jade-soft,
  stroke: (left: 3.5pt + c-jade, top: 0.6pt + c-jade-bdr, right: 0.6pt + c-jade-bdr, bottom: 0.6pt + c-jade-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: true,
  above: 8pt,
  below: 10pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-jade, tracking: 0.3pt)[✓ #upper(title)]
  #v(4pt)
  #set text(size: 9.5pt, fill: c-ink)
  #body
]

// Khung Ngữ liệu Văn bản Đọc hiểu / Đề văn (Literary Passage Box)
#let passage-box(title: none, source: none, body) = block(
  width: 100%,
  fill: rgb("#FCFBF7"),
  stroke: 0.8pt + rgb("#D6D0C4"),
  radius: 5pt,
  inset: (x: 13pt, y: 11pt),
  breakable: true,
  above: 9pt,
  below: 9pt,
)[
  #if title != none [
    #align(center)[
      #text(font: font-serif, size: 11pt, weight: "bold", fill: c-navy)[#upper(title)]
    ]
    #v(4pt)
  ]
  #set text(font: font-serif, size: 9.8pt, fill: rgb("#1F242D"))
  #set par(leading: 0.68em, first-line-indent: 1.2em, spacing: 0.65em, justify: true)
  #body
  #if source != none [
    #v(4pt)
    #align(right)[
      #text(font: font-serif, size: 8.8pt, style: "italic", fill: c-slate)[(#source)]
    ]
  ]
]

// Khung Bài văn nghị luận mẫu hoàn chỉnh
#let essay-box(title: "BÀI VĂN NGHỊ LUẬN MẪU HOÀN CHỈNH", body) = block(
  width: 100%,
  fill: rgb("#FAFBFF"),
  stroke: (left: 3pt + c-purple, top: 0.6pt + c-purple-bdr, right: 0.6pt + c-purple-bdr, bottom: 0.6pt + c-purple-bdr),
  radius: (right: 5pt),
  inset: (x: 13pt, y: 11pt),
  breakable: true,
  above: 9pt,
  below: 11pt,
)[
  #text(font: font-sans, size: 8.6pt, weight: "bold", fill: c-purple, tracking: 0.3pt)[✦ #upper(title)]
  v(5pt)
  #set text(font: font-serif, size: 9.8pt, fill: rgb("#1D2433"))
  #set par(leading: 0.68em, first-line-indent: 1.4em, spacing: 0.65em, justify: true)
  #body
]

// Hộp Callout đa năng (dùng cho Tóm lược toàn năng & Hướng dẫn Flashcard)
#let callout(title: "", tone: "primary", icon: "◆", breakable-box: true, body) = {
  let (bg, bdr, accent) = if tone == "gold" {
    (c-gold-soft, c-gold-bdr, c-amber)
  } else if tone == "danger" {
    (c-red-soft, c-red-bdr, c-red)
  } else if tone == "success" {
    (c-jade-soft, c-jade-bdr, c-jade)
  } else {
    (c-blue-soft, c-blue-bdr, c-indigo)
  }
  block(
    width: 100%,
    fill: bg,
    stroke: (left: 3.5pt + accent, top: 0.6pt + bdr, right: 0.6pt + bdr, bottom: 0.6pt + bdr),
    radius: (right: 5pt),
    inset: (x: 11pt, y: 9pt),
    breakable: breakable-box,
    above: 8pt,
    below: 8pt,
  )[
    #text(font: font-sans, size: 8.6pt, weight: "bold", fill: accent, tracking: 0.3pt)[#icon #upper(title)]
    #v(4pt)
    #set text(size: 9.4pt, fill: c-ink)
    #body
  ]
}

// Tiêu đề Phần lớn (Part Banner)
#let part-banner(num, title, subtitle) = {
  pagebreak(weak: true)
  place(hide(heading(level: 1, offset: 0)[#num — #title]))
  block(
    width: 100%,
    fill: c-navy,
    radius: 6pt,
    inset: (x: 16pt, y: 14pt),
    below: 14pt,
    breakable: false,
  )[
    #grid(
      columns: (auto, 1fr),
      column-gutter: 12pt,
      align: (center + horizon, left + horizon),
      box(
        fill: rgb("#F59E0B"),
        radius: 4pt,
        inset: (x: 9pt, y: 6pt),
        text(font: font-sans, size: 9.5pt, weight: "bold", fill: c-navy)[#num]
      ),
      [
        #text(font: font-sans, size: 13.5pt, weight: "bold", fill: white)[#upper(title)]
        #v(3pt)
        #text(font: font-sans, size: 8.8pt, fill: rgb("#D0E2FF"))[#subtitle]
      ]
    )
  ]
}

// Header thẻ Đề kiểm tra
#let exam-header(num, subtitle, model-type) = {
  if num != "01" { pagebreak(weak: true) }
  place(hide(heading(level: 2, offset: 0)[Đề minh họa số #num: #subtitle (#model-type)]))
  block(
    width: 100%,
    fill: rgb("#F0F5FF"),
    stroke: 1.2pt + c-indigo,
    radius: 6pt,
    inset: (x: 14pt, y: 11pt),
    below: 10pt,
    breakable: false,
  )[
    #grid(
      columns: (1fr, auto),
      column-gutter: 12pt,
      align: (left + horizon, right + horizon),
      [
        #text(font: font-sans, size: 8.2pt, weight: "bold", fill: c-indigo, tracking: 0.4pt)[ĐỀ KIỂM TRA GIỮA HỌC KÌ I — MÔN NGỮ VĂN 10 (NĂM HỌC 2026 – 2027)]
        #v(3pt)
        #text(font: font-sans, size: 13pt, weight: "bold", fill: c-navy)[ĐỀ MINH HỌA SỐ #num: #upper(subtitle)]
      ],
      box(
        fill: c-navy,
        radius: 4pt,
        inset: (x: 8pt, y: 5pt),
        align(center)[
          #text(font: font-sans, size: 8pt, weight: "bold", fill: rgb("#FCD34D"))[THỜI GIAN: 90 PHÚT]\
          #text(font: font-sans, size: 7.5pt, fill: white)[#model-type]
        ]
      )
    )
  ]
}

// Bảng tiêu chuẩn có header lặp lại khi sang trang
#let study-table(cols, headers, ..cells) = {
  set text(size: 8.9pt)
  table(
    columns: cols,
    stroke: 0.5pt + c-border,
    inset: (x: 6.5pt, y: 5.5pt),
    fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-bg-neutral },
    align: (x, y) => if y == 0 { center + horizon } else { left + top },
    table.header(
      ..headers.map(h => text(font: font-sans, weight: "bold", size: 8.6pt, fill: white)[#h])
    ),
    ..cells
  )
}

// Cấu hình toàn văn bản & Trang bìa
#let project-doc(body) = {
  set document(
    title: "Đề cương ôn tập Giữa kì I Ngữ văn 10 - Kết nối tri thức (2026-2027)",
    author: "Tài liệu tự học Ngữ văn 10",
    date: datetime(year: 2026, month: 10, day: 29),
  )

  set page(
    paper: "a4",
    margin: (top: 20mm, bottom: 19mm, left: 17mm, right: 17mm),
    header: context {
      if counter(page).get().first() > 1 [
        #set text(font: font-sans, size: 7.8pt, fill: c-muted)
        #grid(
          columns: (1fr, auto),
          [ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I NGỮ VĂN 10 • KẾT NỐI TRI THỨC VỚI CUỘC SỐNG],
          [*NĂM HỌC 2026 – 2027*]
        )
        #v(-4pt)
        #line(length: 100%, stroke: 0.5pt + c-border)
      ]
    },
    footer: context {
      if counter(page).get().first() > 1 [
        #line(length: 100%, stroke: 0.5pt + c-border)
        #v(3pt)
        #set text(font: font-sans, size: 7.8pt, fill: c-muted)
        #grid(
          columns: (1fr, auto),
          [Theo ma trận được cung cấp • 90 phút • 11 câu • Thang điểm 10],
          text(weight: "bold", fill: c-navy)[Trang #counter(page).display("1 / 1", both: true)]
        )
      ]
    }
  )

  set text(font: font-sans, lang: "vi", size: 9.8pt, fill: c-ink)
  set par(leading: 0.62em, spacing: 0.78em, justify: true)
  set heading(offset: 1)
  show raw: set text(font: font-sans, size: 9.1pt, weight: "semibold", fill: c-indigo)

  show outline.entry.where(level: 1): it => {
    v(5pt, weak: true)
    strong(text(fill: c-navy, size: 9.6pt, it))
  }

  show heading.where(level: 2): it => {
    v(6pt)
    block(
      breakable: false,
      below: 7pt,
      [
        #text(font: font-sans, size: 12pt, weight: "bold", fill: c-navy)[#it.body]
        #v(2pt)
        #line(length: 100%, stroke: 1.2pt + c-indigo)
      ]
    )
  }

  show heading.where(level: 3): it => {
    v(5pt)
    block(
      breakable: false,
      below: 5pt,
      text(font: font-sans, size: 10.6pt, weight: "bold", fill: c-indigo)[▸ #it.body]
    )
  }

  show heading.where(level: 4): it => {
    v(3pt)
    block(
      breakable: false,
      below: 4pt,
      text(font: font-sans, size: 9.9pt, weight: "bold", fill: c-amber)[• #it.body]
    )
  }

  // Cover and navigation use the same embedded fonts as the body.
  page(header: none, footer: none)[
    #v(15mm)
    #text(size: 10pt, weight: "bold", fill: c-indigo)[KẾT NỐI TRI THỨC VỚI CUỘC SỐNG]
    #v(12mm)
    #text(size: 30pt, weight: "bold", fill: c-navy)[ĐỀ CƯƠNG ÔN TẬP]
    #v(5mm)
    #text(size: 23pt, weight: "bold", fill: c-navy)[GIỮA HỌC KÌ I]
    #v(8mm)
    #line(length: 55mm, stroke: 3pt + c-gold)
    #v(8mm)
    #text(size: 25pt, weight: "bold", fill: c-indigo)[NGỮ VĂN 10]
    #v(4mm)
    #text(size: 13pt)[Năm học 2026–2027]
    #v(18mm)
    #formula-box(title: "Phạm vi theo ma trận được cung cấp")[
      *90 phút • 11 câu • 10 điểm*\
      Đọc hiểu thần thoại: *6 điểm* (8 trắc nghiệm + 2 tự luận).\
      Viết bài nghị luận phân tích, đánh giá truyện thần thoại: *4 điểm*.
    ]
    #v(6mm)
    #text(size: 11pt)[Tri thức thể loại và tiếng Việt\
      Kĩ năng đọc hiểu, viết và tự sửa bài\
      40 câu luyện • 6 đề kèm đáp án • 6 bài tham khảo\
      Lịch ôn tập và bảng nguồn đối chiếu]
    #v(1fr)
    #line(length: 100%, stroke: 0.6pt + c-border)
    #v(4mm)
    #text(size: 9pt, fill: c-muted)[Bản biên tập ngày 29/10/2026. Tài liệu tự học, không phải đề thi hoặc đáp án chính thức. Phạm vi áp dụng và giới hạn nguồn được ghi ở Phần I và phụ lục.]
  ]

  text(size: 16pt, weight: "bold", fill: c-navy)[Cách dùng tài liệu]
  v(5pt)
  [Đọc Phần I để biết phạm vi. Ôn Phần II–III rồi tự làm câu hỏi ở Phần IV. Học cách lập luận ở Phần V trước khi làm sáu đề ở Phần VI. Che đáp án khi làm; sau mỗi đề, ghi lại lỗi và làm lại câu sai. Phần VII có lịch ôn và thẻ tự hỏi; phụ lục có nguồn và phiếu chữa bài.]

  v(8pt)
  text(size: 14pt, weight: "bold", fill: c-navy)[Mục lục]
  block[
    #set text(size: 8.7pt)
    #set par(leading: 0.4em, spacing: 0.4em)
    #outline(title: none, indent: 1.2em, depth: 2)
  ]

  body
}
