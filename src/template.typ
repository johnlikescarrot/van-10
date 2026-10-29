// ============================================================================
// HỆ THỐNG ĐỊNH DẠNG HỌC THUẬT (DESIGN SYSTEM)
// Đề cương ôn tập Giữa học kì I Ngữ văn 10 - Kết nối tri thức (2026-2027)
// ============================================================================

#let c-navy      = rgb("#14284B")
#let c-indigo    = rgb("#1E4976")
#let c-blue-soft = rgb("#EEF4FB")
#let c-blue-bdr  = rgb("#B8D0EB")

#let c-red       = rgb("#B42318")
#let c-crimson   = c-red
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

// Nhãn cấp độ nhận thức
#let badge(label, bg: c-blue-soft, fg: c-indigo, bdr: c-blue-bdr) = box(
  fill: bg,
  stroke: 0.6pt + bdr,
  radius: 3pt,
  inset: (x: 5pt, y: 1.8pt),
  baseline: 15%,
  text(font: font-sans, size: 7.5pt, weight: "bold", fill: fg, label)
)

#let badge-biet = badge("NHẬN BIẾT", bg: rgb("#EFF8FF"), fg: rgb("#175CD3"), bdr: rgb("#B2DDFF"))
#let badge-hieu = badge("THÔNG HIỂU", bg: rgb("#FFFAEB"), fg: rgb("#B54708"), bdr: rgb("#FEDF89"))
#let badge-vd   = badge("VẬN DỤNG", bg: rgb("#ECFDF3"), fg: rgb("#067647"), bdr: rgb("#ABEFC6"))

#let render-level-badge(lvl) = {
  if lvl == none { none } else if type(lvl) == str {
    if lvl.starts-with("NHẬN BIẾT") {
      badge(lvl, bg: rgb("#EFF8FF"), fg: rgb("#175CD3"), bdr: rgb("#B2DDFF"))
    } else if lvl.starts-with("THÔNG HIỂU") {
      badge(lvl, bg: rgb("#FFFAEB"), fg: rgb("#B54708"), bdr: rgb("#FEDF89"))
    } else {
      badge(lvl, bg: rgb("#ECFDF3"), fg: rgb("#067647"), bdr: rgb("#ABEFC6"))
    }
  } else { lvl }
}

// Hàm trình bày câu hỏi Trắc nghiệm khách quan (không bị ngắt đôi sang trang)
#let mcq-1col(num, level, stem, a, b, c, d) = block(
  width: 100%,
  breakable: false,
  above: 6.5pt,
  below: 6.5pt,
)[
  #set par(spacing: 0.42em, leading: 0.56em)
  *Câu #num.* #render-level-badge(level) #h(2pt) #stem
  #v(2.5pt)
  #pad(left: 8pt)[
    *A.* #a\
    *B.* #b\
    *C.* #c\
    *D.* #d
  ]
]

#let mcq-2col(num, level, stem, a, b, c, d) = block(
  width: 100%,
  breakable: false,
  above: 6.5pt,
  below: 6.5pt,
)[
  #set par(spacing: 0.42em, leading: 0.56em)
  *Câu #num.* #render-level-badge(level) #h(2pt) #stem
  #v(2.5pt)
  #pad(left: 8pt)[
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 14pt,
      row-gutter: 4pt,
      [*A.* #a], [*B.* #b],
      [*C.* #c], [*D.* #d],
    )
  ]
]

// Hộp Ghi nhớ nhanh
#let mnemonic-box(title: "GHI NHỚ CỐT LÕI", body) = block(
  width: 100%,
  fill: c-gold-soft,
  stroke: (left: 3.5pt + c-gold, top: 0.6pt + c-gold-bdr, right: 0.6pt + c-gold-bdr, bottom: 0.6pt + c-gold-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 8.5pt),
  breakable: false,
  above: 8pt,
  below: 8pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-amber, tracking: 0.3pt)[★ #upper(title)]
  #v(4pt)
  #set text(size: 9.5pt, fill: c-ink)
  #body
]

// Hộp Lưu ý lỗi thường gặp trong phòng thi
#let trap-box(title: "LƯU Ý TRÁNH NHẦM LẪN TRONG PHÒNG THI", breakable-box: false, body) = block(
  width: 100%,
  fill: c-red-soft,
  stroke: (left: 3.5pt + c-red, top: 0.6pt + c-red-bdr, right: 0.6pt + c-red-bdr, bottom: 0.6pt + c-red-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 8.5pt),
  breakable: breakable-box,
  above: 8pt,
  below: 8pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-red, tracking: 0.3pt)[▲ #upper(title)]
  #v(4pt)
  #set text(size: 9.4pt, fill: c-ink)
  #body
]

// Hộp Phương pháp & Kĩ thuật làm bài
#let formula-box(title: "PHƯƠNG PHÁP & KĨ THUẬT LÀM BÀI", breakable-box: false, body) = block(
  width: 100%,
  fill: c-blue-soft,
  stroke: (left: 3.5pt + c-indigo, top: 0.6pt + c-blue-bdr, right: 0.6pt + c-blue-bdr, bottom: 0.6pt + c-blue-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 8.5pt),
  breakable: breakable-box,
  above: 8pt,
  below: 8pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-indigo, tracking: 0.3pt)[◆ #upper(title)]
  #v(4pt)
  #set text(size: 9.5pt, fill: c-ink)
  #body
]

// Hộp Đáp án & Hướng dẫn chấm
#let answer-box(title: "ĐÁP ÁN & HƯỚNG DẪN CHẤM CHI TIẾT", body) = block(
  width: 100%,
  fill: c-jade-soft,
  stroke: (left: 3.5pt + c-jade, top: 0.6pt + c-jade-bdr, right: 0.6pt + c-jade-bdr, bottom: 0.6pt + c-jade-bdr),
  radius: (right: 5pt),
  inset: (x: 11pt, y: 8.5pt),
  breakable: true,
  above: 8pt,
  below: 10pt,
)[
  #text(font: font-sans, size: 8.5pt, weight: "bold", fill: c-jade, tracking: 0.3pt)[✓ #upper(title)]
  #v(4pt)
  #set text(size: 9.4pt, fill: c-ink)
  #body
]

// Khung Ngữ liệu văn bản
#let passage-box(title: none, source: none, is-verse: false, body) = block(
  width: 100%,
  fill: rgb("#FCFBF7"),
  stroke: 0.8pt + rgb("#D6D0C4"),
  radius: 5pt,
  inset: (x: 13pt, y: 10.5pt),
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
  #set par(
    leading: 0.66em,
    first-line-indent: if is-verse { 0em } else { 1.2em },
    spacing: 0.62em,
    justify: not is-verse,
  )
  #body
  #if source != none [
    #v(4pt)
    #align(right)[
      #text(font: font-serif, size: 8.7pt, style: "italic", fill: c-slate)[(#source)]
    ]
  ]
]

// Khung Bài văn nghị luận tham khảo hoàn chỉnh
#let essay-box(title: "BÀI VIẾT THAM KHẢO HOÀN CHỈNH", body) = block(
  width: 100%,
  fill: rgb("#FAFBFF"),
  stroke: (left: 3pt + c-purple, top: 0.6pt + c-purple-bdr, right: 0.6pt + c-purple-bdr, bottom: 0.6pt + c-purple-bdr),
  radius: (right: 5pt),
  inset: (x: 12pt, y: 9pt),
  breakable: true,
  above: 7pt,
  below: 8pt,
)[
  #text(font: font-sans, size: 8.4pt, weight: "bold", fill: c-purple, tracking: 0.3pt)[✦ #upper(title)]
  #v(4pt)
  #set text(font: font-serif, size: 9.45pt, fill: rgb("#1D2433"))
  #set par(leading: 0.60em, first-line-indent: 1.4em, spacing: 0.50em, justify: true)
  #body
]

// Hộp Callout đa năng
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
    inset: (x: 11pt, y: 8.5pt),
    breakable: breakable-box,
    above: 7pt,
    below: 7pt,
  )[
    #text(font: font-sans, size: 8.5pt, weight: "bold", fill: accent, tracking: 0.3pt)[#icon #upper(title)]
    #v(4pt)
    #set text(size: 9.3pt, fill: c-ink)
    #body
  ]
}

// Tiêu đề Phần lớn (Part Banner) - giữ chuẩn câu tiếng Việt trong Mục lục
#let part-banner(num, title, subtitle) = {
  pagebreak(weak: true)
  place(hide(heading(level: 1, offset: 0)[#num: #title]))
  block(
    width: 100%,
    fill: c-navy,
    radius: 6pt,
    inset: (x: 15pt, y: 13pt),
    below: 12pt,
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
        #text(font: font-sans, size: 8.7pt, fill: rgb("#D0E2FF"))[#subtitle]
      ]
    )
  ]
}

#let skill-box = formula-box
#let sample-essay-box = essay-box

// Header thẻ Đề kiểm tra
#let exam-header(num, subtitle, model-type) = {
  block(
    width: 100%,
    fill: rgb("#F0F5FF"),
    stroke: 1.1pt + c-indigo,
    radius: 6pt,
    inset: (x: 13pt, y: 10pt),
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
        #text(font: font-sans, size: 11.4pt, weight: "bold", fill: c-navy)[ĐỀ SỐ 0#num: #subtitle]
      ],
      box(
        fill: c-navy,
        radius: 4pt,
        inset: (x: 8pt, y: 5pt),
        align(center)[
          #text(font: font-sans, size: 7.9pt, weight: "bold", fill: rgb("#FCD34D"))[THỜI GIAN: 90 PHÚT]\
          #text(font: font-sans, size: 7.3pt, fill: white)[#model-type]
        ]
      )
    )
  ]
}

// Bảng tiêu chuẩn học thuật (chống đứt dòng lẻ sang trang)
#let study-table(cols, headers, breakable-rows: false, ..cells) = {
  set text(size: 8.8pt)
  show table.cell: set block(breakable: breakable-rows)
  table(
    columns: cols,
    stroke: 0.5pt + c-border,
    inset: (x: 6pt, y: 5pt),
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
    title: "Đề cương ôn tập giữa học kì I Ngữ văn 10 - Kết nối tri thức (2026-2027)",
    author: "Tài liệu ôn tập Ngữ văn 10 - Chương trình GDPT 2018",
  )

  set page(
    paper: "a4",
    margin: (top: 19mm, bottom: 18mm, left: 16.5mm, right: 16.5mm),
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
          [Bám sát Ma trận & Bản đặc tả Giữa kì I (90 phút • 11 câu • Thang điểm 10,0)],
          text(weight: "bold", fill: c-navy)[Trang #counter(page).display("1 / 1", both: true)]
        )
      ]
    }
  )

  set text(font: font-sans, lang: "vi", size: 9.6pt, fill: c-ink)
  set par(leading: 0.6em, spacing: 0.72em, justify: true)
  set heading(offset: 1)
  show raw: set text(font: font-sans, size: 9pt, weight: "semibold", fill: c-indigo)

  show outline.entry.where(level: 1): it => {
    v(4.5pt, weak: true)
    strong(text(fill: c-navy, size: 9.2pt, it))
  }

  show heading.where(level: 2): it => {
    v(5pt)
    block(
      breakable: false,
      below: 6pt,
      [
        #text(font: font-sans, size: 11.4pt, weight: "bold", fill: c-navy)[#it.body]
        #v(2pt)
        #line(length: 100%, stroke: 1.1pt + c-indigo)
      ]
    )
  }

  show heading.where(level: 3): it => {
    v(4pt)
    block(
      breakable: false,
      below: 4.5pt,
      text(font: font-sans, size: 10.2pt, weight: "bold", fill: c-indigo)[▸ #it.body]
    )
  }

  show heading.where(level: 4): it => {
    v(3pt)
    block(
      breakable: false,
      below: 3.5pt,
      text(font: font-sans, size: 9.6pt, weight: "bold", fill: c-amber)[• #it.body]
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
        #text(font: font-sans, size: 11.5pt, weight: "semibold", fill: rgb("#93C5FD"), tracking: 0.8pt)[
          TÀI LIỆU HỆ THỐNG HÓA KIẾN THỨC, KĨ NĂNG & ĐỀ LUYỆN TẬP TOÀN DIỆN
        ]
        #v(5mm)
        #text(font: font-sans, size: 24.5pt, weight: "bold", fill: white)[
          ĐỀ CƯƠNG ÔN TẬP\
          GIỮA HỌC KÌ I • NGỮ VĂN 10
        ]
        #v(4mm)
        #line(length: 75mm, stroke: 2.5pt + rgb("#F59E0B"))
        #v(5mm)
        #text(font: font-serif, size: 11.6pt, style: "italic", fill: rgb("#E2E8F0"))[
          Bám sát Ma trận và Bản đặc tả năm học 2026–2027:\
          Đọc hiểu truyện thần thoại ngoài SGK & Viết bài văn nghị luận phân tích, đánh giá tác phẩm truyện
        ]

        #v(11mm)
        // Hộp thông số Ma trận trung tâm trên trang bìa
        #block(
          width: 100%,
          fill: white,
          radius: 8pt,
          inset: 13pt,
          stroke: 1.2pt + rgb("#F59E0B"),
        )[
          #text(font: font-sans, size: 8.8pt, weight: "bold", fill: c-navy, tracking: 0.3pt)[
            CẤU TRÚC ĐỀ KIỂM TRA CHUẨN MA TRẬN NĂM HỌC 2026–2027 (THỜI GIAN: 90 PHÚT)
          ]
          #v(8pt)
          #table(
            columns: (1fr, 1fr, 1fr, 1fr),
            stroke: none,
            gutter: 7pt,
            inset: 8pt,
            fill: (x, y) => (c-blue-soft, c-purple-soft, c-gold-soft, c-jade-soft).at(x),
            align: center + horizon,
            [
              #text(size: 14.5pt, weight: "bold", fill: c-indigo)[60%]\
              #text(size: 7.9pt, weight: "bold", fill: c-navy)[ĐỌC HIỂU (6,0đ)]\
              #text(size: 7.3pt, fill: c-slate)[8 TNKQ + 2 Tự luận\ Thần thoại ngoài SGK]
            ],
            [
              #text(size: 14.5pt, weight: "bold", fill: c-purple)[40%]\
              #text(size: 7.9pt, weight: "bold", fill: c-navy)[PHẦN VIẾT (4,0đ)]\
              #text(size: 7.3pt, fill: c-slate)[01 Bài văn nghị luận\ Chủ đề & Nghệ thuật]
            ],
            [
              #text(size: 14.5pt, weight: "bold", fill: c-amber)[40–30–30]\
              #text(size: 7.9pt, weight: "bold", fill: c-navy)[CẤP ĐỘ TƯ DUY]\
              #text(size: 7.3pt, fill: c-slate)[Biết 40% • Hiểu 30%\ Vận dụng 30%]
            ],
            [
              #text(size: 14.5pt, weight: "bold", fill: c-jade)[127 CÂU]\
              #text(size: 7.9pt, weight: "bold", fill: c-navy)[NGÂN HÀNG & 7 ĐỀ]\
              #text(size: 7.3pt, fill: c-slate)[Đủ đáp án, giải nhiễu\ & 07 bài văn tham khảo]
            ],
          )
        ]

        #v(9mm)
        // Các trụ cột nội dung của đề cương (căn đều chiều cao tuyệt đối)
        #table(
          columns: (1fr, 1fr),
          stroke: 0.6pt + rgb("#3B5B8C"),
          gutter: 9pt,
          inset: 9pt,
          fill: rgb("#1D355E"),
          align: left + top,
          [
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[I. NỀN TẢNG THỂ LOẠI & 16 TÁC PHẨM MỞ RỘNG]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[Hệ thống hóa Tri thức ngữ văn Bài 1 KNTT, công thức 5K–1C, bảng phân biệt 5 thể loại tự sự và hồ sơ 16 thần thoại ngoài SGK trọng tâm.]
          ],
          [
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[II. TIẾNG VIỆT BÀI 1–2–3 & ĐỌC HIỂU 22 CHỈ BÁO]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[Từ Hán Việt, 6 biện pháp tu từ, lỗi dùng từ, trật tự từ, mạch lạc – liên kết và 50 câu hỏi luyện tập phủ kín toàn bộ chỉ báo đặc tả.]
          ],
          [
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[III. CHUYÊN ĐỀ VIẾT CHUẨN SGK TR. 29–34]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[Giải phẫu bài viết tham khảo SGK, quy trình 4 bước viết, hai mô hình lập luận Thân bài và kĩ năng diễn đạt tự nhiên, tránh khuôn sáo.]
          ],
          [
            #text(size: 8.5pt, weight: "bold", fill: rgb("#FCD34D"))[IV. BỘ 07 ĐỀ THỰC CHIẾN & HỆ THỐNG ÔN NHANH]\
            #v(2pt)
            #text(size: 7.9pt, fill: rgb("#E2E8F0"))[07 đề thi 90 phút (cả văn xuôi và văn vần, Phương án A & B), biểu điểm 0,25đ, 07 bài văn hoàn chỉnh, 30 thẻ tự kiểm tra & bảng tổng kết 1 trang.]
          ],
        )

        #v(1fr)
        #line(length: 100%, stroke: 0.6pt + rgb("#3B5B8C"))
        #v(4mm)
        #grid(
          columns: (1fr, auto),
          text(size: 8.4pt, fill: rgb("#CBD5E1"))[Biên soạn bám sát Chương trình Giáo dục phổ thông 2018 & SGK Ngữ văn 10 Kết nối tri thức],
          text(size: 8.8pt, weight: "bold", fill: rgb("#FCD34D"))[NĂM HỌC 2026–2027]
        )
      ]
    ]
  ]

  // ==================== TRANG MỤC LỤC & HƯỚNG DẪN SỬ DỤNG ====================
  block(
    width: 100%,
    fill: c-blue-soft,
    stroke: 0.8pt + c-blue-bdr,
    radius: 6pt,
    inset: 11pt,
    below: 10pt,
  )[
    #text(size: 9.6pt, weight: "bold", fill: c-navy)[HƯỚNG DẪN KHAI THÁC ĐỀ CƯƠNG HIỆU QUẢ]
    #v(3.5pt)
    #set text(size: 8.8pt)
    Tài liệu được tổ chức từ nhận diện cấu trúc đề thi, củng cố nền tảng kiến thức đến thực hành giải đề bấm giờ để học sinh nắm vững bản chất, nhớ lâu và xử lí trọn vẹn bài thi trong 90 phút:
    #v(2pt)
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 12pt,
      row-gutter: 4.5pt,
      [*1. Bảng đối chiếu trực quan:* Đặt các khái niệm dễ nhầm cạnh nhau (*đề tài – chủ đề, câu chuyện – cốt truyện, 5 thể loại tự sự*) để phân biệt nhanh ngay từ lần đọc đầu.],
      [*2. Công thức ghi nhớ ngắn gọn:* Nén các đặc trưng và bước làm bài thành cụm từ khóa thống nhất xuyên suốt tài liệu (*5K–1C*, *GỌI–TRÍCH–GIẢI–CHỐT*).],
      [*3. Nhận diện bẫy câu hỏi:* Chỉ rõ cơ chế tạo phương án nhiễu trong trắc nghiệm và những lỗi diễn đạt sáo rỗng, lạc đề học sinh thường mắc ở bài viết 4,0 điểm.],
      [*4. Tự kiểm tra chủ động:* Tự giải 50 câu ngân hàng, bấm giờ làm 07 đề minh họa và che cột đáp án ở 30 thẻ hỏi đáp cuối sách trước khi đối chiếu lời giải.]
    )
  ]

  block(
    width: 100%,
    inset: (y: 2pt),
  )[
    #text(size: 12pt, weight: "bold", fill: c-navy)[MỤC LỤC TỔNG QUÁT]
    #v(2pt)
    #line(length: 100%, stroke: 1.1pt + c-indigo)
    #v(3pt)
    #set text(size: 8.8pt)
    #outline(title: none, indent: 1.1em, depth: 2)
  ]

  body
}
