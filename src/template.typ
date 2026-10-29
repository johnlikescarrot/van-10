// ============================================================================
// HỆ THỐNG ĐỊNH DẠNG HỌC THUẬT (DESIGN SYSTEM)
// Đề cương ôn tập Giữa học kì I Ngữ văn 10 - Kết nối tri thức (2026-2027)
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

#let font-sans  = ("Be Vietnam Pro",)
#let font-serif = ("Lora",)

// Chấm vuông vector nhỏ thay cho kí hiệu Unicode để không rơi phông dự phòng
#let tag-dot(col) = box(
  width: 5pt,
  height: 5pt,
  radius: 1.2pt,
  fill: col,
  baseline: -12%,
)

// Nhãn cấp độ nhận thức (Badges)
#let badge(label, bg: c-blue-soft, fg: c-indigo, bdr: c-blue-bdr) = box(
  fill: bg,
  stroke: 0.6pt + bdr,
  radius: 3pt,
  inset: (x: 5pt, y: 2pt),
  baseline: 15%,
  text(font: font-sans, size: 7.6pt, weight: "bold", fill: fg, label)
)

#let badge-biet = badge("NHẬN BIẾT", bg: rgb("#EFF8FF"), fg: rgb("#175CD3"), bdr: rgb("#B2DDFF"))
#let badge-hieu = badge("THÔNG HIỂU", bg: rgb("#FFFAEB"), fg: rgb("#B54708"), bdr: rgb("#FEDF89"))
#let badge-vd   = badge("VẬN DỤNG", bg: rgb("#ECFDF3"), fg: rgb("#067647"), bdr: rgb("#ABEFC6"))

// Hộp Ghi nhớ trọng tâm
#let mnemonic-box(title: "Ghi nhớ trọng tâm", breakable-box: false, body) = block(
  width: 100%,
  fill: c-gold-soft,
  stroke: (left: 3.5pt + c-gold, top: 0.6pt + c-gold-bdr, right: 0.6pt + c-gold-bdr, bottom: 0.6pt + c-gold-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: breakable-box,
  above: 8pt,
  below: 8pt,
)[
  #tag-dot(c-amber) #h(4pt) #text(font: font-sans, size: 8.6pt, weight: "bold", fill: c-amber, tracking: 0.2pt)[#upper(title)]
  #v(4pt)
  #set text(size: 9.5pt, fill: c-ink)
  #body
]

// Hộp Lưu ý tránh nhầm lẫn
#let trap-box(title: "Lưu ý tránh nhầm lẫn trong phòng thi", breakable-box: false, body) = block(
  width: 100%,
  fill: c-red-soft,
  stroke: (left: 3.5pt + c-red, top: 0.6pt + c-red-bdr, right: 0.6pt + c-red-bdr, bottom: 0.6pt + c-red-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: breakable-box,
  above: 8pt,
  below: 8pt,
)[
  #tag-dot(c-red) #h(4pt) #text(font: font-sans, size: 8.6pt, weight: "bold", fill: c-red, tracking: 0.2pt)[#upper(title)]
  #v(4pt)
  #set text(size: 9.4pt, fill: c-ink)
  #body
]

// Hộp Phương pháp & Khung kĩ năng
#let formula-box(title: "Phương pháp làm bài", breakable-box: false, body) = block(
  width: 100%,
  fill: c-blue-soft,
  stroke: (left: 3.5pt + c-indigo, top: 0.6pt + c-blue-bdr, right: 0.6pt + c-blue-bdr, bottom: 0.6pt + c-blue-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: breakable-box,
  above: 8pt,
  below: 8pt,
)[
  #tag-dot(c-indigo) #h(4pt) #text(font: font-sans, size: 8.6pt, weight: "bold", fill: c-indigo, tracking: 0.2pt)[#upper(title)]
  #v(4pt)
  #set text(size: 9.5pt, fill: c-ink)
  #body
]

// Hộp Đáp án & Hướng dẫn chấm
#let answer-box(title: "Đáp án và hướng dẫn chấm chi tiết", body) = block(
  width: 100%,
  fill: c-jade-soft,
  stroke: (left: 3.5pt + c-jade, top: 0.6pt + c-jade-bdr, right: 0.6pt + c-jade-bdr, bottom: 0.6pt + c-jade-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 9pt),
  breakable: true,
  above: 8pt,
  below: 10pt,
)[
  #tag-dot(c-jade) #h(4pt) #text(font: font-sans, size: 8.6pt, weight: "bold", fill: c-jade, tracking: 0.2pt)[#upper(title)]
  #v(4pt)
  #set text(size: 9.4pt, fill: c-ink)
  #body
]

// Khung Ngữ liệu Văn bản Đọc hiểu / Đề văn
#let passage-box(title: none, source: none, body) = block(
  width: 100%,
  fill: rgb("#FCFBF7"),
  stroke: 0.8pt + rgb("#D6D0C4"),
  radius: 5pt,
  inset: (x: 13pt, y: 10pt),
  breakable: true,
  above: 8pt,
  below: 8pt,
)[
  #if title != none [
    #align(center)[
      #text(font: font-serif, size: 10.8pt, weight: "bold", fill: c-navy)[#upper(title)]
    ]
    #v(4pt)
  ]
  #set text(font: font-serif, size: 9.7pt, fill: rgb("#1F242D"))
  #set par(leading: 0.66em, first-line-indent: 1.2em, spacing: 0.62em, justify: true)
  #body
  #if source != none [
    #v(4pt)
    #align(right)[
      #text(font: font-serif, size: 8.7pt, style: "italic", fill: c-slate)[(#source)]
    ]
  ]
]

// Khung Bài văn nghị luận tham khảo hoàn chỉnh
#let essay-box(title: "Bài văn nghị luận tham khảo hoàn chỉnh", body) = block(
  width: 100%,
  fill: rgb("#FAFBFF"),
  stroke: (left: 3pt + c-purple, top: 0.6pt + c-purple-bdr, right: 0.6pt + c-purple-bdr, bottom: 0.6pt + c-purple-bdr),
  radius: (right: 5pt),
  inset: (x: 13pt, y: 10pt),
  breakable: true,
  above: 8pt,
  below: 10pt,
)[
  #tag-dot(c-purple) #h(4pt) #text(font: font-sans, size: 8.6pt, weight: "bold", fill: c-purple, tracking: 0.2pt)[#upper(title)]
  #v(5pt)
  #set text(font: font-serif, size: 9.7pt, fill: rgb("#1D2433"))
  #set par(leading: 0.66em, first-line-indent: 1.4em, spacing: 0.62em, justify: true)
  #body
]

// Hộp Callout đa năng
#let callout(title: "", tone: "primary", breakable-box: true, body) = {
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
    above: 7pt,
    below: 7pt,
  )[
    #tag-dot(accent) #h(4pt) #text(font: font-sans, size: 8.6pt, weight: "bold", fill: accent, tracking: 0.2pt)[#upper(title)]
    #v(4pt)
    #set text(size: 9.3pt, fill: c-ink)
    #body
  ]
}

// Tiêu đề Phần lớn (Part Banner) - dùng chuẩn chữ hoa đầu câu trong Mục lục
#let part-banner(num, title, subtitle) = {
  pagebreak(weak: true)
  place(hide(heading(level: 1, offset: 0)[#num: #title]))
  block(
    width: 100%,
    fill: c-navy,
    radius: 6pt,
    inset: (x: 16pt, y: 13pt),
    below: 13pt,
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
        text(font: font-sans, size: 9.2pt, weight: "bold", fill: c-navy)[#num]
      ),
      [
        #text(font: font-sans, size: 13pt, weight: "bold", fill: white)[#upper(title)]
        #v(3pt)
        #text(font: font-sans, size: 8.6pt, fill: rgb("#D0E2FF"))[#subtitle]
      ]
    )
  ]
}

// Header Đề kiểm tra minh họa
#let exam-header(num, subtitle, model-type, break-before: true) = {
  if break-before { pagebreak(weak: true) }
  place(hide(heading(level: 2, offset: 0)[Đề minh họa số #num: #subtitle (#model-type)]))
  block(
    width: 100%,
    fill: rgb("#F0F5FF"),
    stroke: 1.1pt + c-indigo,
    radius: 6pt,
    inset: (x: 14pt, y: 10pt),
    below: 9pt,
    breakable: false,
  )[
    #grid(
      columns: (1fr, auto),
      column-gutter: 12pt,
      align: (left + horizon, right + horizon),
      [
        #text(font: font-sans, size: 8pt, weight: "bold", fill: c-indigo, tracking: 0.3pt)[ĐỀ KIỂM TRA GIỮA HỌC KÌ I • MÔN NGỮ VĂN 10 (NĂM HỌC 2026–2027)]
        #v(3pt)
        #text(font: font-sans, size: 12.4pt, weight: "bold", fill: c-navy)[ĐỀ MINH HỌA SỐ #num: #upper(subtitle)]
      ],
      box(
        fill: c-navy,
        radius: 4pt,
        inset: (x: 8pt, y: 5pt),
        align(center)[
          #text(font: font-sans, size: 7.9pt, weight: "bold", fill: rgb("#FCD34D"))[THỜI GIAN: 90 PHÚT]\
          #text(font: font-sans, size: 7.4pt, fill: white)[#model-type]
        ]
      )
    )
  ]
}

// Bảng tiêu chuẩn (tắt căn đều hai bên trong ô hẹp để tránh giãn chữ xấu)
#let study-table(cols, headers, ..cells) = {
  set text(size: 8.8pt)
  set par(justify: false, leading: 0.55em, spacing: 0.42em)
  table(
    columns: cols,
    stroke: 0.5pt + c-border,
    inset: (x: 6.5pt, y: 5.2pt),
    fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-bg-neutral },
    align: (x, y) => if y == 0 { center + horizon } else { left + top },
    table.header(
      ..headers.map(h => text(font: font-sans, weight: "bold", size: 8.4pt, fill: white)[#h])
    ),
    ..cells
  )
}

// Cấu hình toàn văn bản & Trang bìa
#let project-doc(body) = {
  set document(
    title: "Đề cương ôn tập Giữa học kì I Ngữ văn 10 - Kết nối tri thức với cuộc sống (2026-2027)",
    author: "Tài liệu ôn tập Ngữ văn 10 - Chương trình GDPT 2018",
  )

  set page(
    paper: "a4",
    margin: (top: 19.5mm, bottom: 18.5mm, left: 17mm, right: 17mm),
    header: context {
      if counter(page).get().first() > 1 [
        #set text(font: font-sans, size: 7.7pt, fill: c-muted)
        #grid(
          columns: (1fr, auto),
          [ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I NGỮ VĂN 10 • KẾT NỐI TRI THỨC VỚI CUỘC SỐNG],
          [*NĂM HỌC 2026–2027*]
        )
        #v(-4pt)
        #line(length: 100%, stroke: 0.5pt + c-border)
      ]
    },
    footer: context {
      if counter(page).get().first() > 1 [
        #line(length: 100%, stroke: 0.5pt + c-border)
        #v(3pt)
        #set text(font: font-sans, size: 7.7pt, fill: c-muted)
        #grid(
          columns: (1fr, auto),
          [Biên soạn theo Ma trận và Bản đặc tả kiểm tra Giữa kì I (90 phút • 11 câu • Thang điểm 10,0)],
          text(weight: "bold", fill: c-navy)[Trang #counter(page).display("1 / 1", both: true)]
        )
      ]
    }
  )

  set text(font: font-sans, lang: "vi", size: 9.7pt, fill: c-ink)
  set par(leading: 0.62em, spacing: 0.74em, justify: true)
  set list(marker: ([•], [–], [•]))
  set heading(offset: 1)
  show raw: set text(font: font-sans, size: 9pt, weight: "semibold", fill: c-indigo)

  show outline.entry.where(level: 1): it => {
    v(4.5pt, weak: true)
    strong(text(fill: c-navy, size: 9.4pt, it))
  }

  show heading.where(level: 2): it => {
    v(6pt)
    block(
      breakable: false,
      below: 6pt,
      [
        #text(font: font-sans, size: 11.6pt, weight: "bold", fill: c-navy)[#it.body]
        #v(2pt)
        #line(length: 100%, stroke: 1.1pt + c-indigo)
      ]
    )
  }

  show heading.where(level: 3): it => {
    v(4.5pt)
    block(
      breakable: false,
      below: 4.5pt,
      [
        #box(width: 4pt, height: 8.5pt, radius: 1pt, fill: c-indigo, baseline: 10%)
        #h(5pt)
        #text(font: font-sans, size: 10.3pt, weight: "bold", fill: c-indigo)[#it.body]
      ]
    )
  }

  show heading.where(level: 4): it => {
    v(3pt)
    block(
      breakable: false,
      below: 3.5pt,
      [
        #tag-dot(c-amber)
        #h(4pt)
        #text(font: font-sans, size: 9.7pt, weight: "bold", fill: c-amber)[#it.body]
      ]
    )
  }

  // ==================== TRANG BÌA (COVER PAGE) ====================
  page(margin: 0mm, header: none, footer: none)[
    #box(width: 100%, height: 100%, fill: c-navy)[
      #place(top + left, rect(width: 100%, height: 8mm, fill: rgb("#F59E0B")))
      #place(top + right, dx: -12mm, dy: 18mm,
        circle(radius: 42mm, fill: rgb("#1E3A6D"), stroke: 0.8pt + rgb("#2E5496"))
      )
      #place(bottom + left, dx: -18mm, dy: 18mm,
        circle(radius: 55mm, fill: rgb("#1A335E"), stroke: 0.8pt + rgb("#2B4C85"))
      )

      #pad(x: 20mm, top: 25mm, bottom: 18mm)[
        #set par(justify: false, leading: 0.58em)
        #box(
          fill: rgb("#1E3A6D"),
          stroke: 0.8pt + rgb("#F59E0B"),
          radius: 4pt,
          inset: (x: 10pt, y: 5pt),
          text(font: font-sans, size: 8.6pt, weight: "bold", fill: rgb("#FCD34D"), tracking: 0.5pt)[
            CHƯƠNG TRÌNH GDPT 2018 • BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
          ]
        )

        #v(13mm)
        #text(font: font-sans, size: 11.2pt, weight: "semibold", fill: rgb("#93C5FD"), tracking: 0.8pt)[
          TÀI LIỆU HỆ THỐNG HÓA KIẾN THỨC VÀ LUYỆN ĐỀ NỬA ĐẦU HỌC KÌ I
        ]
        #v(5mm)
        #text(font: font-sans, size: 24.5pt, weight: "bold", fill: white)[
          ĐỀ CƯƠNG ÔN TẬP\
          GIỮA HỌC KÌ I • NGỮ VĂN 10
        ]
        #v(4mm)
        #line(length: 76mm, stroke: 2.5pt + rgb("#F59E0B"))
        #v(5mm)
        #text(font: font-serif, size: 11.5pt, style: "italic", fill: rgb("#E2E8F0"))[
          Bám sát Ma trận và Bản đặc tả kiểm tra Giữa kì I năm học 2026–2027:\
          Đọc hiểu truyện thần thoại ngoài SGK và Nghị luận phân tích, đánh giá một tác phẩm truyện
        ]

        #v(11mm)
        #block(
          width: 100%,
          fill: white,
          radius: 8pt,
          inset: 13pt,
          stroke: 1.2pt + rgb("#F59E0B"),
        )[
          #text(font: font-sans, size: 8.8pt, weight: "bold", fill: c-navy, tracking: 0.3pt)[
            CẤU TRÚC ĐỀ KIỂM TRA THEO MA TRẬN NĂM HỌC 2026–2027 (THỜI GIAN: 90 PHÚT)
          ]
          #v(8pt)
          #grid(
            columns: (1fr, 1fr, 1fr, 1fr),
            column-gutter: 8pt,
            block(fill: c-blue-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 14.5pt, weight: "bold", fill: c-indigo)[6,0đ (60%)]\
                #text(size: 7.9pt, weight: "bold", fill: c-navy)[PHẦN ĐỌC HIỂU]\
                #text(size: 7.3pt, fill: c-slate)[8 TNKQ + 2 Tự luận\ Thần thoại ngoài SGK]
              ]
            ],
            block(fill: c-purple-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 14.5pt, weight: "bold", fill: c-purple)[4,0đ (40%)]\
                #text(size: 7.9pt, weight: "bold", fill: c-navy)[PHẦN VIẾT]\
                #text(size: 7.3pt, fill: c-slate)[01 Bài văn nghị luận\ Chủ đề & Nghệ thuật]
              ]
            ],
            block(fill: c-gold-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 14.5pt, weight: "bold", fill: c-amber)[40–30–30]\
                #text(size: 7.9pt, weight: "bold", fill: c-navy)[TỈ LỆ TƯ DUY]\
                #text(size: 7.3pt, fill: c-slate)[Biết 40% • Hiểu 30%\ Vận dụng 30%]
              ]
            ],
            block(fill: c-jade-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 14.5pt, weight: "bold", fill: c-jade)[116 CÂU]\
                #text(size: 7.9pt, weight: "bold", fill: c-navy)[NGÂN HÀNG & 6 ĐỀ]\
                #text(size: 7.3pt, fill: c-slate)[Đủ đáp án, giải nhiễu\ & 7 bài văn tham khảo]
              ]
            ]
          )
        ]

        #v(9mm)
        #grid(
          columns: (1fr, 1fr),
          column-gutter: 11pt,
          row-gutter: 8pt,
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[PHẦN I & II • MA TRẬN & TRI THỨC THẦN THOẠI]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[Giải mã 22 chỉ báo đánh giá, 6 đặc trưng và 10 mô-típ thần thoại, phân biệt 5 thể loại tự sự, hồ sơ 15 thần thoại ngoài SGK.]
          ],
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[PHẦN III & IV • TIẾNG VIỆT & KĨ NĂNG ĐỌC HIỂU]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[Tích hợp Tiếng Việt Bài 1–2–3 (từ Hán Việt, lỗi dùng từ, trật tự từ, mạch lạc – liên kết) và 50 câu luyện theo 13 chỉ báo.]
          ],
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[PHẦN V • KĨ NĂNG VIẾT NGHỊ LUẬN (TR. 29–34)]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[Giải mã bài tham khảo Quà Giáng sinh, quy trình 4 bước viết, dàn ý truyện thần thoại ngoài SGK và bài tham khảo Chữ người tử tù.]
          ],
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[PHẦN VI & VII • 06 ĐỀ 90 PHÚT & 30 THẺ ÔN TẬP]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[06 đề đủ hai phương án ngữ liệu kèm hướng dẫn chấm từng 0,25đ, 06 bài văn mẫu, kế hoạch ôn 7 ngày và tờ tóm tắt 1 trang.]
          ],
        )

        #v(1fr)
        #line(length: 100%, stroke: 0.6pt + rgb("#3B5B8C"))
        #v(4mm)
        #grid(
          columns: (1fr, auto),
          text(size: 8.3pt, fill: rgb("#CBD5E1"))[Tài liệu biên soạn phục vụ dạy học và ôn tập kiểm tra định kì môn Ngữ văn lớp 10],
          text(size: 8.8pt, weight: "bold", fill: rgb("#FCD34D"))[NĂM HỌC 2026–2027]
        )
      ]
    ]
  ]

  // ==================== TRANG HƯỚNG DẪN TRA CỨU & MỤC LỤC ====================
  block(
    width: 100%,
    fill: c-blue-soft,
    stroke: 0.8pt + c-blue-bdr,
    radius: 6pt,
    inset: 11pt,
    below: 11pt,
  )[
    #text(size: 9.6pt, weight: "bold", fill: c-navy)[HƯỚNG DẪN SỬ DỤNG ĐỀ CƯƠNG HIỆU QUẢ]
    #v(4pt)
    #set text(size: 8.9pt)
    #set par(justify: false, leading: 0.56em)
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 12pt,
      row-gutter: 5pt,
      [*1. Nắm cấu trúc đề trước khi ôn (Phần I):* Xem bảng quy đổi điểm 11 câu và 22 chỉ báo để biết rõ trọng tâm câu hỏi trắc nghiệm, tự luận ngắn và bài nghị luận 4,0 điểm.],
      [*2. Học lí thuyết qua bảng đối chiếu (Phần II & III):* Đối chiếu 6 đặc trưng thần thoại, 5 thể loại tự sự và 3 bài Thực hành tiếng Việt nửa đầu Học kì I để tránh nhầm khái niệm.],
      [*3. Luyện kĩ năng đọc – viết đúng chuẩn SGK (Phần IV & V):* Thực hành 50 câu theo chỉ báo, nắm vững bài học Viết trang 29–34 SGK trước khi bắt tay vào giải đề tổng hợp.],
      [*4. Bấm giờ làm đề và tự kiểm tra (Phần VI & VII):* Làm tối thiểu 2 đề trong đúng 90 phút theo mốc `12 – 18 – 55 – 5`, sau đó tự chấm bằng biểu điểm 0,25 và ôn 30 thẻ câu hỏi.]
    )
  ]

  block(
    width: 100%,
    inset: (y: 3pt),
  )[
    #text(size: 12pt, weight: "bold", fill: c-navy)[MỤC LỤC TỔNG QUÁT]
    #v(2pt)
    #line(length: 100%, stroke: 1.1pt + c-indigo)
    #v(4pt)
    #set text(size: 9pt)
    #outline(title: none, indent: 1.2em, depth: 2)
  ]

  body
}
