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
  #v(5pt)
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
    author: "Tài liệu tự học Ngữ văn 10 - phiên bản kiểm định",
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
          [Đối chiếu Ma trận & Bản đặc tả Giữa kì I (90 phút • 11 câu • thang điểm 10)],
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

  // ==================== TRANG BÌA (COVER PAGE) ====================
  page(margin: 0mm, header: none, footer: none)[
    #box(width: 100%, height: 100%, fill: c-navy)[
      // Dải trang trí hình học học thuật phía trên
      #place(top + left, rect(width: 100%, height: 8mm, fill: rgb("#F59E0B")))
      #place(top + right, dx: -12mm, dy: 18mm,
        circle(radius: 42mm, fill: rgb("#1E3A6D"), stroke: 0.8pt + rgb("#2E5496"))
      )
      #place(bottom + left, dx: -18mm, dy: 18mm,
        circle(radius: 55mm, fill: rgb("#1A335E"), stroke: 0.8pt + rgb("#2B4C85"))
      )

      #pad(x: 20mm, top: 26mm, bottom: 18mm)[
        #box(
          fill: rgb("#1E3A6D"),
          stroke: 0.8pt + rgb("#F59E0B"),
          radius: 4pt,
          inset: (x: 10pt, y: 5pt),
          text(font: font-sans, size: 8.8pt, weight: "bold", fill: rgb("#FCD34D"), tracking: 0.6pt)[
            CHƯƠNG TRÌNH GDPT 2018 • BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
          ]
        )

        #v(14mm)
        #text(font: font-sans, size: 12pt, weight: "semibold", fill: rgb("#93C5FD"), tracking: 1pt)[
          TÀI LIỆU TỰ HỌC CÓ HƯỚNG DẪN VÀ KIỂM ĐỊNH PHẠM VI
        ]
        #v(5mm)
        #text(font: font-sans, size: 25pt, weight: "bold", fill: white)[
          ĐỀ CƯƠNG ÔN TẬP\
          GIỮA HỌC KÌ I — NGỮ VĂN 10
        ]
        #v(4mm)
        #line(length: 75mm, stroke: 2.5pt + rgb("#F59E0B"))
        #v(5mm)
        #text(font: font-serif, size: 12pt, style: "italic", fill: rgb("#E2E8F0"))[
          Phân tích chuyên sâu Ma trận & Bản đặc tả năm học 2026 – 2027:\
          Đọc hiểu Truyện Thần thoại ngoài SGK & Nghị luận phân tích, đánh giá tác phẩm truyện
        ]

        #v(12mm)
        // Hộp thông số Ma trận trung tâm trên trang bìa
        #block(
          width: 100%,
          fill: white,
          radius: 8pt,
          inset: 14pt,
          stroke: 1.2pt + rgb("#F59E0B"),
        )[
          #text(font: font-sans, size: 9pt, weight: "bold", fill: c-navy, tracking: 0.4pt)[
            CẤU TRÚC THAM KHẢO THEO MA TRẬN NĂM HỌC 2026 – 2027 (90 PHÚT)
          ]
          #v(8pt)
          #grid(
            columns: (1fr, 1fr, 1fr, 1fr),
            column-gutter: 8pt,
            block(fill: c-blue-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 15pt, weight: "bold", fill: c-indigo)[60%]\
                #text(size: 8pt, weight: "bold", fill: c-navy)[ĐỌC HIỂU (6,0đ)]\
                #text(size: 7.4pt, fill: c-slate)[8 TNKQ + 2 Tự luận\ Thần thoại ngoài SGK]
              ]
            ],
            block(fill: c-purple-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 15pt, weight: "bold", fill: c-purple)[40%]\
                #text(size: 8pt, weight: "bold", fill: c-navy)[LÀM VĂN (4,0đ)]\
                #text(size: 7.4pt, fill: c-slate)[01 Bài văn nghị luận\ Phân tích, đánh giá]
              ]
            ],
            block(fill: c-gold-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 15pt, weight: "bold", fill: c-amber)[40-30-30]\
                #text(size: 8pt, weight: "bold", fill: c-navy)[TỈ LỆ NHẬN THỨC]\
                #text(size: 7.4pt, fill: c-slate)[Biết 40% • Hiểu 30%\ Vận dụng 30%]
              ]
            ],
            block(fill: c-jade-soft, radius: 5pt, inset: 8pt, width: 100%)[
              #align(center)[
                #text(size: 15pt, weight: "bold", fill: c-jade)[106 CÂU]\
                #text(size: 8pt, weight: "bold", fill: c-navy)[NGÂN HÀNG & 6 ĐỀ]\
                #text(size: 7.4pt, fill: c-slate)[Có đáp án gợi ý,\ tự chấm & văn mẫu]
              ]
            ]
          )
        ]

        #v(10mm)
        // Các trụ cột nổi bật của đề cương
        #grid(
          columns: (1fr, 1fr),
          column-gutter: 12pt,
          row-gutter: 8pt,
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.6pt, weight: "bold", fill: rgb("#FCD34D"))[01. HỆ THỐNG HÓA KIẾN THỨC]\
            #text(size: 8pt, fill: rgb("#E2E8F0"))[Sơ đồ hóa kiến thức, khẩu quyết 5K–1C, ma trận phân biệt 5 thể loại tự sự & 12 ngữ liệu mở rộng.]
          ],
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.6pt, weight: "bold", fill: rgb("#FCD34D"))[02. ĐỐI CHIẾU 22 CHỈ BÁO]\
            #text(size: 8pt, fill: rgb("#E2E8F0"))[13 chỉ báo Đọc hiểu, 9 yêu cầu Viết, chuyên đề Từ Hán Việt và tu từ.]
          ],
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.6pt, weight: "bold", fill: rgb("#FCD34D"))[03. DÀN Ý LINH HOẠT & VĂN MẪU]\
            #text(size: 8pt, fill: rgb("#E2E8F0"))[Mô hình Ngôi Đền 5 Tầng phân tích chủ đề & nghệ thuật thần thoại kèm 06 bài viết tham khảo.]
          ],
          block(fill: rgb("#1D355E"), stroke: 0.6pt + rgb("#3B5B8C"), radius: 5pt, inset: 9pt, width: 100%)[
            #text(size: 8.6pt, weight: "bold", fill: rgb("#FCD34D"))[04. CÂU HỎI VÀ ĐÁP ÁN GỢI Ý]\
            #text(size: 8pt, fill: rgb("#E2E8F0"))[40 câu luyện theo chỉ báo + 06 đề minh họa 90 phút (66 câu), kèm lí giải và gợi ý tự chấm.]
          ],
        )

        #v(1fr)
        #line(length: 100%, stroke: 0.6pt + rgb("#3B5B8C"))
        #v(4mm)
        #grid(
          columns: (1fr, auto),
          text(size: 8.5pt, fill: rgb("#CBD5E1"))[Biên soạn theo Ma trận, Bản đặc tả và ngữ liệu luyện tập tự biên soạn],
          text(size: 9pt, weight: "bold", fill: rgb("#FCD34D"))[NĂM HỌC 2026 – 2027]
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
    inset: 9pt,
    below: 8pt,
  )[
    #text(size: 9.3pt, weight: "bold", fill: c-navy)[CẨM NANG SỬ DỤNG ĐỀ CƯƠNG: HỌC CHỦ ĐỘNG, KIỂM TRA CÓ CĂN CỨ]
    #v(3pt)
    #set text(size: 8.4pt)
    Đề cương gợi ý bốn cách học chủ động. Hãy chọn cách phù hợp với thời gian và thói quen của mình; hiệu quả đến từ việc tự trả lời, nhận phản hồi và sửa lỗi đều đặn:
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 10pt,
      row-gutter: 3pt,
      [*1. Kết hợp chữ và sơ đồ:* Dùng bảng đối chiếu, sơ đồ và từ khóa để nhìn rõ quan hệ giữa các ý.],
      [*2. Gom nhóm từ khóa:* Nén kiến thức thành công thức ngắn (*5K–1C*, *GỌI–TRÍCH–GIẢI–CHỐT*) rồi tự giải thích lại bằng lời của mình.],
      [*3. Phân tích lỗi sai:* Đọc lí do vì sao một phương án chưa đúng, rồi tìm bằng chứng trong ngữ liệu.],
      [*4. Tự truy hồi:* Làm ngân hàng câu hỏi, đề minh họa và thẻ ôn khi chưa xem đáp án; quay lại lỗi sai sau một hoặc hai ngày.]
    )
  ]

  block(
    width: 100%,
    inset: (y: 4pt),
  )[
    #text(size: 11.5pt, weight: "bold", fill: c-navy)[MỤC LỤC TỔNG QUÁT]
    #v(1pt)
    #line(length: 100%, stroke: 1.2pt + c-indigo)
    #v(3pt)
    #set text(size: 8.7pt)
    #outline(title: none, indent: 1.1em, depth: 2)
  ]

  body
}
