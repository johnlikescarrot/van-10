#import "template.typ": *

// Thẻ chú giải tầng bậc dùng trong bài văn mẫu chú giải (5.11)
#let tier-tag(code, note) = box(
  fill: rgb("#EEF4FB"),
  stroke: 0.5pt + c-blue-bdr,
  radius: 3pt,
  inset: (x: 5pt, y: 2pt),
  baseline: 14%,
  text(font: font-sans, size: 7.4pt, weight: "bold", fill: c-indigo)[#code · #note]
) + h(4pt)

#part-banner(
  "PHẦN V",
  "Chuyên Đề Viết Nghị Luận Phân Tích, Đánh Giá Tác Phẩm Truyện (4,0 Điểm)",
  "5 yêu cầu chuẩn SGK tr. 29 – 34 • Quy trình 4 bước & chỉnh sửa 2 cấp độ • Mô hình Ngôi Đền 5 Tầng • Kĩ thuật P–E–E–V • Kho ngôn ngữ nghị luận • 10 lỗi chí mạng & bài văn mẫu chú giải"
)

= 5.1. Năm Yêu Cầu Bắt Buộc Của Kiểu Bài (SGK Ngữ văn 10 KNTT, tr. 29 – 34)

Kiểu bài #strong[nghị luận phân tích, đánh giá một tác phẩm truyện] đòi hỏi người viết làm đồng thời hai việc: bóc tách tác phẩm thành các yếu tố để xem chúng được tạo dựng ra sao, rồi đứng ra nhận xét giá trị của những yếu tố ấy. SGK *Kết nối tri thức* (tr. 29) chốt lại thành #strong[năm yêu cầu]. Năm yêu cầu này vừa là khung làm bài, vừa là thang chấm của giám khảo:

#study-table(
  (0.6fr, 2.2fr, 2.6fr, 1.9fr),
  ("YC", "Yêu cầu theo SGK", "Hiểu đúng để làm bài", "Lỗi tương ứng nếu bỏ sót"),

  [*1*],
  [Giới thiệu ngắn gọn về tác phẩm truyện (nhan đề, tên tác giả,...) và ý kiến khái quát của người viết về tác phẩm.],
  [Nêu đủ ba thông tin: *tên truyện + xuất xứ/người sưu tầm + thể loại (thần thoại suy nguyên hay sáng tạo)*. Câu cuối cùng của đoạn mở bài phải là một nhận định khái quát (luận đề) về *chủ đề* và *đặc sắc nghệ thuật*.],
  [Mất điểm *Biết* (0,75đ): mở bài chỉ kể lể cảm xúc, không gọi tên truyện, không nêu luận đề.],

  [*2*],
  [Tóm tắt tác phẩm truyện (vừa đủ để người đọc nắm được nội dung chính).],
  [Gói trong *4–6 câu*, đúng ngôi thứ ba, giữ những chi tiết sẽ dùng đến ở phần phân tích. Chỉ tóm tắt, chưa bình luận.],
  [Tóm tắt chiếm quá nửa bài; chép lại lời thoại; xen cảm nghĩ cá nhân vào đoạn tóm tắt.],

  [*3*],
  [Phân tích cụ thể, rõ ràng về tác phẩm truyện (chủ đề, nét đặc sắc về hình thức nghệ thuật và tác dụng của chúng) với những cứ liệu sinh động.],
  [Đây là trọng tâm của bài. Mỗi luận điểm cần đi theo một vòng: *nhận xét → dẫn chữ → giải mã → chỉ ra tác dụng*. Cứ liệu phải là câu, cụm từ trích từ văn bản.],
  [Nêu nhận xét chung chung không có dẫn chứng; kể lại truyện thay vì phân tích.],

  [*4*],
  [Đánh giá về tác phẩm truyện dựa trên các lí lẽ và bằng chứng thuyết phục.],
  [Trả lời câu hỏi: truyện hay ở chỗ nào, vì sao hay, còn điểm nào hạn chế. Có thể đối sánh với một văn bản cùng thể loại hoặc nêu cách hiểu riêng có căn cứ.],
  [Chỉ khen bằng tính từ suông (*“hay”, “đặc sắc”, “ý nghĩa”*) mà không lí giải.],

  [*5*],
  [Khẳng định giá trị của tác phẩm truyện.],
  [Chốt lại giá trị bằng những tiêu chí đo được: mức độ phổ biến, sức sống lâu bền trong đời sống hôm nay, khả năng tái sinh trong các hình thức nghệ thuật khác, bài học cho người đọc trẻ.],
  [Kết bài lặp lại nguyên văn mở bài, không mở ra được điều gì mới.],
)

#formula-box(title: "THỨ TỰ TRIỂN KHAI LUẬN ĐIỂM: CHỌN MỘT TRONG HAI, GIỮ NGUYÊN ĐẾN CUỐI BÀI")[
  Bài văn mẫu trong SGK (*Giá trị hay là sự vô giá của quà tặng trong truyện ngắn “Quà Giáng sinh” của O. Hen-ry*) đi từ #strong[các yếu tố nghệ thuật sang giá trị nội dung]: tóm tắt → phân tích cốt truyện, nhân vật, tình huống, lời thoại → phân tích đoạn kết → tác dụng của ngôi kể thứ ba → xác định chủ đề → mở rộng chủ đề → kết luận.

  Mô hình *Ngôi Đền 5 Tầng* dưới đây đi theo hướng ngược lại: #strong[chủ đề trước, nghệ thuật sau]. Cả hai cách đều được chấp nhận, vì Bản đặc tả chỉ yêu cầu phân tích được *cả nội dung, chủ đề lẫn hình thức nghệ thuật* và thể hiện được mối liên hệ giữa chúng. Điều giám khảo trừ điểm là việc #strong[đổi trật tự giữa chừng]: đang nói nghệ thuật lại quay sang chủ đề rồi lại quay về nghệ thuật, khiến Thân bài thiếu mạch logic.
]

= 5.2. Quy Trình 4 Bước: Từ Chuẩn Bị Đến Chỉnh Sửa (Đúng Quy Trình SGK, tr. 33 – 34)

Nhiều học sinh đạt điểm trung bình ở Câu 11 vì lao vào viết ngay khi vừa đọc xong đề. Bốn bước dưới đây lấy từ phần *Thực hành viết* của SGK và được chia nhỏ thành thao tác làm trong phòng thi:

#study-table(
  (0.75fr, 1.9fr, 3.0fr, 1.65fr),
  ("Bước", "Tên bước (SGK)", "Thao tác cụ thể trong phòng thi", "Thời lượng khuyến nghị"),

  [*1*],
  [*Chuẩn bị viết*],
  [Đọc kĩ ngữ liệu, gạch chân 5 yếu tố: *thời gian – không gian – nhân vật – chi tiết kì ảo – câu kết giải thích hiện tượng*. Xác định ngay truyện thuộc nhóm *suy nguyên* hay *sáng tạo*.],
  [3 – 4 phút],

  [*2*],
  [*Tìm ý, lập dàn ý*],
  [Trả lời nhanh 6 câu hỏi gợi ý của SGK (khung dưới) ra giấy nháp, rồi xếp các ý vào 3 phần Mở – Thân – Kết. Dàn ý phải ghi sẵn 2–3 cụm từ sẽ trích dẫn cho mỗi luận điểm.],
  [5 – 6 phút],

  [*3*],
  [*Viết*],
  [Viết theo dàn ý đã lập. Ưu tiên hoàn thành trọn vẹn 3 phần; câu văn chưa đẹp có thể sửa ở bước 4. Giữ nhịp: mỗi đoạn Thân bài 6 – 10 câu, bắt đầu bằng một câu chủ đề rõ ràng.],
  [45 – 50 phút],

  [*4*],
  [*Chỉnh sửa, hoàn thiện*],
  [Rà soát theo *hai cấp độ* (bảng dưới) + một lượt rà chính tả, từ Hán Việt, dấu ngoặc kép ở các câu trích.],
  [4 – 5 phút],
)

== A. Sáu Câu Hỏi Tìm Ý (Khung SGK tr. 33 — Trả Lời Ra Nháp Trước Khi Lập Dàn Ý)

#formula-box(title: "6 CÂU HỎI TÌM Ý — ĐIỀN RA NHÁP ĐỂ CÓ NGAY KHUNG BÀI 4,0 ĐIỂM")[
  1. *Vì sao em chọn tác phẩm này để phân tích, đánh giá? Điều gì khiến em yêu thích tác phẩm?* → Trả lời bằng 1 câu, dùng làm câu dẫn của Mở bài.
  2. *Câu chuyện trong truyện diễn ra như thế nào?* → Ghi 4–6 mốc sự việc theo trục: bối cảnh → nhiệm vụ/biến cố của thần → kì tích → kết quả còn lưu lại đến nay. Đây chính là đoạn Tóm tắt.
  3. *Chủ đề của truyện là gì?* → Ghi 2 tầng: tầng cắt nghĩa tự nhiên + tầng khát vọng, bài học nhân sinh.
  4. *Truyện có những nét đặc sắc nào về nghệ thuật (cốt truyện, tình huống, nhân vật, ngôi kể, lời thoại, chi tiết kì ảo...)?* → Chọn 3–4 phương diện mạnh nhất, mỗi phương diện kèm 1 dẫn chứng.
  5. *Những câu, đoạn nào cần được trích dẫn và phân tích?* → Khoanh tròn 3–5 cụm từ đắt giá trong ngữ liệu; tuyệt đối không chép cả đoạn dài.
  6. *Cần nhận xét, đánh giá như thế nào về thành công hay hạn chế của tác phẩm?* → Viết 2 ý: thành công nổi bật nhất + một điểm nhìn cá nhân (hoặc một giới hạn của cách lí giải cổ sơ khi đặt cạnh khoa học hôm nay).
]

== B. Khung Dàn Ý Ba Phần & Bảng Kiểm Chỉnh Sửa Hai Cấp Độ

#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  block(fill: c-bg-neutral, stroke: 0.8pt + c-indigo, radius: 5pt, inset: 10pt, width: 100%)[
    #text(weight: "bold", fill: c-indigo, size: 9.5pt)[KHUNG DÀN Ý 3 PHẦN]
    #v(3pt)
    #set text(size: 8.9pt)
    - *Mở bài (1 đoạn):* Dẫn dắt → Giới thiệu nhan đề, thể loại, xuất xứ → Nêu luận đề (nhận định khái quát về chủ đề + nghệ thuật).
    - *Thân bài (4–5 đoạn):*
      + *Đoạn 1:* Khái quát phân loại + Tóm tắt (4–6 câu).
      + *Đoạn 2–3:* Phân tích, đánh giá *chủ đề* theo 2 tầng nghĩa.
      + *Đoạn 4:* Phân tích, đánh giá *đặc sắc nghệ thuật* (3–4 phương diện), luôn chỉ ra tác dụng với chủ đề.
      + *Đoạn 5:* Đánh giá mở rộng, đối sánh liên văn bản, ý kiến cá nhân.
    - *Kết bài (1 đoạn):* Tóm lược nhận định → Khẳng định giá trị (độ phổ biến, sức sống, khả năng tái sinh) → Bài học cho bản thân.
  ],
  block(fill: c-bg-neutral, stroke: 0.8pt + c-purple, radius: 5pt, inset: 10pt, width: 100%)[
    #text(weight: "bold", fill: c-purple, size: 9.5pt)[BẢNG KIỂM CHỈNH SỬA 2 CẤP ĐỘ (SGK tr. 34)]
    #v(3pt)
    #set text(size: 8.9pt)
    *Cấp độ 1 — Ý lớn:*
    - Mỗi ý trong dàn ý đã thành một đoạn văn sáng rõ, mạch lạc chưa?
    - Thứ tự các đoạn đã hợp lí chưa (tóm tắt → chủ đề → nghệ thuật → đánh giá)? Nếu chưa, sắp xếp lại.
    - Có đoạn nào lạc sang kể lể không? Bỏ ngay.

    *Cấp độ 2 — Chi tiết:*
    - Mỗi luận điểm đã có ít nhất 01 chi tiết cụ thể từ văn bản chưa? Chưa thì bổ sung.
    - Chính tả, ngữ pháp, dấu câu đúng chưa?
    - Từ Hán Việt: từ nào chưa rõ nghĩa thì tra lại hoặc thay bằng từ khác.
  ],
)

= 5.3. Bản Chất Hai Thao Tác & Thang Chấm 4,0 Điểm Chi Tiết

#strong[Phân tích] là chia tách tác phẩm thành các yếu tố (*chủ đề, không gian – thời gian, cốt truyện, chi tiết kì ảo, nhân vật, ngôi kể, lời văn*) để chỉ ra chúng biểu hiện cụ thể ra sao qua bằng chứng văn bản. #strong[Đánh giá] là nhận xét cái hay, cái đẹp, tác dụng thẩm mĩ và giá trị nhận thức – văn hoá của các yếu tố ấy theo chuẩn mực thể loại thần thoại và góc nhìn của người viết.

#study-table(
  (1.5fr, 3.75fr, 0.85fr, 1.0fr),
  ("Tiêu chí chấm", "Yêu cầu cụ thể bài làm phải đạt được", "Điểm", "Mức"),

  [*a. Cấu trúc bài viết*],
  [Đủ 3 phần *Mở bài – Thân bài – Kết bài*. Thân bài tách thành 4–5 đoạn, mỗi đoạn có câu chủ đề. Dung lượng theo yêu cầu của đề (thường 600 – 800 chữ); vùng an toàn 600 – 900 chữ.],
  align(center)[*0,25đ*], align(center)[Biết],

  [*b. Giới thiệu \& tóm tắt*],
  [Gọi đúng nhan đề, thể loại (*thần thoại suy nguyên / sáng tạo*), xuất xứ; nêu luận đề đánh giá khái quát; tóm tắt cốt truyện cô đọng 4–6 câu, đúng ngôi thứ ba.],
  align(center)[*0,75đ*], align(center)[Biết],

  [*c. Triển khai luận điểm*],
  [• *Chủ đề (0,75đ):* Gọi đúng hai tầng nghĩa (cắt nghĩa hiện tượng + khát vọng/bài học nhân sinh) và phân tích qua căn cứ cụ thể trong văn bản.\
   • *Hình thức nghệ thuật (1,00đ):* Phân tích và chỉ rõ tác dụng của không gian – thời gian thần thoại, cốt truyện đơn tuyến, chi tiết kì ảo phóng đại, nhân vật thần linh (quyền năng + nét đời thường), ngôi kể thứ ba và ngôn ngữ dân gian.\
   • *Đánh giá tổng hợp & đối sánh (0,50đ):* Bình giá thành công/hạn chế, đối sánh với một thần thoại khác, nêu quan điểm đồng tình hay phản biện có lí lẽ.],
  align(center)[*2,25đ*], align(center)[Hiểu \& Vận dụng],

  [*d. Chính tả \& ngữ pháp*],
  [Đúng chính tả, dùng từ Hán Việt đúng nghĩa và đúng ngữ cảnh, đặt câu đúng ngữ pháp, liên kết đoạn chặt chẽ.],
  align(center)[*0,25đ*], align(center)[Hiểu],

  [*e. Sáng tạo*],
  [Có suy nghĩ riêng sâu sắc; vận dụng khéo nhận định lí luận văn học; diễn đạt giàu hình ảnh và cảm xúc chân thành.],
  align(center)[*0,50đ*], align(center)[Vận dụng],
)

= 5.4. Mô Hình “Ngôi Đền 5 Tầng” — Dàn Ý Vạn Năng Cho Mọi Truyện Thần Thoại

#block(
  width: 100%,
  fill: white,
  stroke: 1pt + c-indigo,
  radius: 6pt,
  inset: 11pt,
  breakable: false,
)[
  #align(center)[
    #text(weight: "bold", size: 9.8pt, fill: c-navy)[SƠ ĐỒ “NGÔI ĐỀN 5 TẦNG” TRIỂN KHAI BÀI VĂN NGHỊ LUẬN 4,0 ĐIỂM]
  ]
  #v(6pt)
  #grid(
    columns: (1fr,),
    row-gutter: 5pt,
    block(fill: rgb("#14284B"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: rgb("#FCD34D"))[TẦNG 1 — MỞ BÀI (1 đoạn • 70–100 chữ):] #text(size: 8.4pt, fill: white)[Dẫn dắt từ sức quyến rũ của thần thoại → Giới thiệu nhan đề, xuất xứ/dân tộc, tiểu loại → Nêu luận đề: nhận định khái quát về *chủ đề* và *đặc sắc nghệ thuật*.]
    ],
    block(fill: rgb("#EFF8FF"), stroke: 0.7pt + rgb("#84CAFF"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: rgb("#175CD3"))[TẦNG 2 — KHÁI QUÁT & TÓM TẮT (Đoạn 1 Thân bài • 90–120 chữ):] #text(size: 8.4pt, fill: c-ink)[Xác định phân loại (*suy nguyên / sáng tạo*) và đề tài → Tóm tắt mạch sự kiện trong 4–6 câu, giữ đúng những chi tiết sẽ phân tích ở tầng trên.]
    ],
    block(fill: rgb("#FFFAEB"), stroke: 0.7pt + rgb("#FDB022"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: rgb("#B54708"))[TẦNG 3 — PHÂN TÍCH, ĐÁNH GIÁ CHỦ ĐỀ (Đoạn 2–3 Thân bài • 220–280 chữ):] #text(size: 8.4pt, fill: c-ink)[(1) Truyện cắt nghĩa hiện tượng tự nhiên, đặc điểm loài vật hay phong tục nào qua lăng kính *vạn vật hữu linh*? (2) Truyện gửi gắm khát vọng, bài học ứng xử gì của người xưa?]
    ],
    block(fill: rgb("#F4F3FF"), stroke: 0.7pt + rgb("#9B8AFB"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: c-purple)[TẦNG 4 — PHÂN TÍCH, ĐÁNH GIÁ NGHỆ THUẬT (Đoạn 4 Thân bài • 250–320 chữ):] #text(size: 8.4pt, fill: c-ink)[Triển khai theo công thức *5K*: (a) *Không gian vũ trụ – Thời gian phiếm chỉ cổ sơ*; (b) *Cốt truyện đơn tuyến & chi tiết kì ảo phóng đại*; (c) *Nghệ thuật khắc họa nhân vật thần linh* (quyền năng kì vĩ + nét tính cách đời thường); (d) *Ngôi kể thứ ba toàn tri & ngôn ngữ dân gian*. Mỗi phương diện phải chỉ ra tác dụng với chủ đề.]
    ],
    block(fill: rgb("#ECFDF3"), stroke: 0.7pt + rgb("#6CE9A6"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: c-jade)[TẦNG 5 — ĐÁNH GIÁ MỞ RỘNG & KẾT BÀI (2 đoạn cuối • 150–200 chữ):] #text(size: 8.4pt, fill: c-ink)[Đối sánh nhanh với *Thần Trụ Trời / Thần Sét / Tê-dê* để làm rõ nét riêng; bàn giá trị của thông điệp trong đời sống hôm nay → Khẳng định giá trị và rút bài học cho bản thân.]
    ]
  )
]

= 5.5. Kĩ Thuật Viết Đoạn “P – E – E – V” & Sáu Kiểu Câu Chủ Đề

Lỗi khiến nhiều bài chỉ dừng ở 2,0/4,0 điểm là #strong[biến bài nghị luận thành bài kể lại truyện]. Mỗi đoạn Thân bài phải lắp đủ #strong[bốn mắt xích P – E – E – V]:

#study-table(
  (0.85fr, 1.5fr, 2.9fr, 3.0fr),
  ("Mắt xích", "Tên đầy đủ", "Nhiệm vụ", "Câu mẫu"),

  [*P*], [*Point (Câu chủ đề)*],
  [Mở đầu bằng một nhận xét về phương diện sắp phân tích. Không kể sự việc.],
  [Nghệ thuật xây dựng nhân vật thần linh là phương diện làm nên sức hấp dẫn riêng của truyện.],

  [*E*], [*Evidence (Bằng chứng)*],
  [Trích 2–3 cụm từ đắt giá trong ngoặc kép, đúng nguyên văn ngữ liệu.],
  [Chỉ bằng một chi tiết *“bà mẹ phải trát cho nữ thần một lần tro vào mặt”*, người xưa đã lí giải xong cả sắc sáng dịu mát lẫn những vết mờ trên bề mặt Mặt Trăng.],

  [*E*], [*Explanation (Giải mã)*],
  [Giải thích vì sao chi tiết ấy được hư cấu, nó dựa trên quan sát thực tế nào, thuộc thủ pháp gì (nhân hóa, phóng đại, so sánh...).],
  [Đằng sau cách lí giải ấy là thói quan sát tỉ mỉ của cư dân làm ruộng: tro bếp là vật quen thuộc nhất trong mỗi gian nhà Việt, nên nó được mượn để hình dung những đám mờ trên vầng trăng.],

  [*V*], [*Value (Bình giá)*],
  [Nêu giá trị của thủ pháp đối với chủ đề và cảm nhận của người viết.],
  [Cách nhân hóa ấy kéo bầu trời xuống ngang tầm mái nhà, khiến thần thoại Việt Nam mang giọng điệu hóm hỉnh, đằm thắm rất riêng.],
)

#formula-box(title: "6 KIỂU CÂU CHỦ ĐỀ (P) — THAY ĐỔI ĐỂ CÁC ĐOẠN KHÔNG RẬP KHUÔN")[
  1. *Trực tiếp:* “Điểm sáng nhất của truyện nằm ở nghệ thuật xây dựng tình huống truyện.”
  2. *Từ nhan đề:* “Ngay từ nhan đề, truyện đã cho thấy mục đích cắt nghĩa nguồn gốc của [...]”
  3. *Từ chi tiết:* “Một chi tiết nhỏ nhưng mở ra cả chủ đề của truyện là [...]”
  4. *Từ đối sánh:* “Cùng cắt nghĩa hiện tượng tự nhiên, song truyện chọn một lối lí giải rất khác với [...]”
  5. *Từ câu hỏi:* “Vì sao người xưa lại hình dung [...] bằng hình ảnh [...]?”
  6. *Từ nhận định:* “Có ý kiến cho rằng mỗi chi tiết hoang đường đều chứa một hạt nhân quan sát thực tế; chi tiết [...] là một minh chứng.”
]

= 5.6. Kĩ Thuật Tóm Tắt Truyện Thần Thoại (Đoạn 1 Thân Bài)

Đoạn tóm tắt là nơi học sinh mất điểm âm thầm nhất: viết quá dài, lẫn bình luận, hoặc kể sai mạch nhân quả. Hãy tóm tắt theo đúng #strong[4 mốc] và giữ trong 4–6 câu:

#study-table(
  (0.9fr, 2.0fr, 3.4fr),
  ("Mốc", "Nội dung cần có", "Câu hỏi gợi ý khi viết"),

  [*Mốc 1*], [Bối cảnh cổ sơ & nhân vật thần],
  [Câu chuyện mở ra ở đâu, vào thuở nào, vị thần ấy là ai?],

  [*Mốc 2*], [Nhiệm vụ hoặc biến cố],
  [Vị thần được giao việc gì, hay chuyện gì xảy ra khiến thần phải hành động?],

  [*Mốc 3*], [Kì tích / hành động chính],
  [Thần đã làm gì (nặn, đắp, vá, lấy lửa, tu bổ, trừng phạt...)?],

  [*Mốc 4*], [Kết quả còn lưu lại hôm nay],
  [Hệ quả nào giải thích được đặc điểm của tự nhiên, loài vật, phong tục hiện tại?],
)

#trap-box(title: "4 LỖI TÓM TẮT & CÁCH CHỮA NHANH")[
  1. *Tóm tắt theo cảm hứng, thiếu mốc 4:* Bỏ câu kết giải thích hiện tượng là bỏ luôn chìa khóa chủ đề. Hãy chắc chắn đoạn tóm tắt khép lại bằng hệ quả còn lưu truyền (*“Từ đó...”, “Vì thế ngày nay...”*).
  2. *Chép lại lời thoại nguyên văn:* Đổi lời thoại thành lời kể gián tiếp.
  3. *Xen bình luận:* Đoạn tóm tắt chỉ trả lời “chuyện gì xảy ra”. Mọi nhận xét để dành cho các đoạn sau.
  4. *Viết quá dài:* Quá 8 câu là đã lấn mất dung lượng phân tích. Chuẩn an toàn: 4–6 câu, khoảng 90 – 120 chữ.
]

= 5.7. Kho Ngôn Ngữ Nghị Luận: Từ Ngữ & Cấu Trúc Câu Ăn Điểm

Giám khảo đọc hàng trăm bài có cùng một dàn ý. Thứ phân biệt bài 3,0 với bài 4,0 nằm ở #strong[vốn từ và nhịp câu]. Kho dưới đây đủ dùng cho mọi truyện thần thoại:

#study-table(
  (1.25fr, 3.1fr, 3.1fr),
  ("Nhóm", "Từ ngữ nên dùng", "Cấu trúc câu nên dùng"),

  [*Động từ phân tích*],
  [thể hiện, bộc lộ, khắc họa, phản ánh, cắt nghĩa, lí giải, gửi gắm, làm nổi bật, tô đậm, soi chiếu, khơi gợi, hé mở, dẫn dắt, xoay quanh, xây dựng, tổ chức, miêu tả.],
  [• “Qua chi tiết ..., tác giả dân gian đã thể hiện ...”\
   • “Chi tiết ... soi chiếu cách nhìn của người xưa về ...”],

  [*Động từ đánh giá*],
  [khẳng định, ngợi ca, đề cao, trân trọng, ghi nhận, nhìn nhận, nhìn nhận lại, cộng hưởng, tiếp nối, vẫn giữ nguyên giá trị, còn nguyên ý nghĩa.],
  [• “Có thể khẳng định ...”\
   • “Đặt cạnh ..., truyện vẫn giữ được nét riêng là ...”],

  [*Từ nối đoạn & ý*],
  [Trước hết; Kế đến; Đáng chú ý hơn; Bên cạnh đó; Ở một phương diện khác; Từ đó có thể thấy; Như vậy; Xét về ...; Khép lại ...],
  [• “Bên cạnh việc cắt nghĩa tự nhiên, truyện còn hướng tới ...”\
   • “Từ cách lí giải ấy, có thể thấy ...”],

  [*Câu chốt luận điểm*],
  [Điều đáng nói là; Cốt lõi của vấn đề nằm ở; Đọc đến đây, người đọc mới thấy hết; Càng đọc, càng nhận ra.],
  [• “Điều đáng nói là cách lí giải hồn nhiên ấy lại trùng khớp với ...”],
)

#trap-box(title: "10 TỪ SÁO RỖNG NÊN THAY (GIÁM KHẢO ĐỌC RẤT NHIỀU LẦN MỖI NGÀY)")[
  #study-table(
    (2.0fr, 2.6fr, 2.4fr),
    ("Nên tránh", "Vì sao", "Thay bằng"),
    [*vô cùng / cực kì / vô giá*], [Trạng từ cường điệu không chứa thông tin.], [rất (hoặc bỏ hẳn), nêu con số, nêu sự thật],
    [*để lại ấn tượng sâu sắc*], [Cụm từ đúc sẵn, ai cũng viết.], [Nêu cụ thể ấn tượng gì, ở chi tiết nào],
    [*đánh dấu bước ngoặt*], [Lạm dụng cho mọi sự kiện.], [Chỉ sự thay đổi cụ thể xảy ra],
    [*bức tranh tuyệt đẹp*], [Ẩn dụ cũ, dùng cho mọi thứ.], [Miêu tả trực tiếp cảnh vật, chi tiết],
    [*bản anh hùng ca hào hùng*], [Dùng cả cho chuyện nặn vịt, sửa chó.], [Nêu đúng giọng điệu truyện: hóm hỉnh, mộc mạc, kì vĩ...],
    [*góp phần làm nên*], [Cụm từ đệm hay gặp trong văn mạng.], [Nêu thẳng tác dụng],
    [*hạt nhân / điểm nhấn / mảnh ghép*], [Ẩn dụ vay mượn, lặp lại liên tục.], [Nói thẳng: chi tiết cốt lõi, chi tiết then chốt],
    [*một cách sâu sắc / triệt để*], [Trạng từ rỗng.], [Bỏ đi, thay bằng hệ quả cụ thể],
    [*không chỉ ... mà còn ...*], [Cấu trúc rập khuôn, lặp lại cả bài.], [Viết hai câu riêng, hoặc dùng “bên cạnh đó”, “hơn nữa”],
    [*em xin khẳng định rằng*], [Công thức lớp 9, nặng tính đọc văn mẫu.], [Bắt đầu bằng nhận định ngay: “Giá trị lớn nhất của truyện là ...”],
  )
]

= 5.8. Bốn Khuôn Mở Bài & Ba Khuôn Kết Bài

== A. Bốn Khuôn Mở Bài (Chọn 1 – 2 Khuôn Thuộc Kĩ, Tránh Viết Y Hệt Cả Lớp)

- #strong[Khuôn 1 — Đi từ nhận định của C. Mác về “tuổi thơ nhân loại” (giàu chất lí luận):]
  *“Bàn về sức quyến rũ của thần thoại cổ đại, C. Mác từng viết rằng đó là ‘thời thơ ấu bình thường của nhân loại’, nơi vẻ đẹp hồn nhiên của trí tưởng tượng nguyên sơ tỏa sáng mãi qua hàng ngàn năm. Trở về buổi bình minh ấy qua kho tàng thần thoại [Việt Nam / Hy Lạp / Trung Hoa], người đọc bắt gặp truyện [Tên tác phẩm]. Bằng cốt truyện kì ảo giàu sức gợi, tác phẩm cắt nghĩa sinh động [hiện tượng/nguồn gốc] và gửi gắm khát vọng nhân sinh của người xưa.”*

- #strong[Khuôn 2 — Đi từ tư duy “vạn vật hữu linh” (bám chặt đặc trưng thể loại):]
  *“Thuở hồng hoang, khi ánh sáng khoa học chưa chạm tới những bí ẩn của vũ trụ, con người nguyên thủy nhìn thế giới bằng niềm tin rằng vạn vật đều có linh hồn. Từ mảnh đất của trí tưởng tượng ấy, biết bao thiên thần thoại ra đời, trong đó có [Tên tác phẩm] thuộc kho tàng thần thoại [tên dân tộc]. Truyện hấp dẫn người đọc nhờ sự hòa quyện giữa chủ đề [nêu gọn chủ đề] và những nét đặc sắc về hình thức nghệ thuật tự sự dân gian.”*

- #strong[Khuôn 3 — Đi từ nhận định của M. Gorki về thần thoại (hợp truyện sáng tạo văn hoá):]
  *“Theo M. Gorki, thần thoại ra đời từ sự phản ánh thiên nhiên và cuộc đấu tranh với thiên nhiên trong trí tưởng tượng của người tiền sử. Đứng trước vũ trụ mênh mông đầy biến động, tổ tiên nhân loại gửi ước mơ làm chủ thế giới vào những hình tượng thần linh bất tử. [Tên tác phẩm] là một câu chuyện như thế: đáng nhớ ở chiều sâu chủ đề và ở vẻ đẹp của nghệ thuật trần thuật dân gian.”*

- #strong[Khuôn 4 — Mở bài trực tiếp (an toàn nhất khi sát giờ):]
  *“Trong kho tàng truyện kể dân gian [Việt Nam / thế giới], thần thoại mở đầu như chiếc nôi nuôi dưỡng trí tưởng tượng của con người thời cổ đại. Một trong những truyện thần thoại ngoài chương trình SGK để lại ấn tượng sâu sắc là [Tên tác phẩm] ([ghi nguồn trích dẫn]). Tác phẩm thể hiện chủ đề [nêu chủ đề] qua hệ thống hình thức nghệ thuật đặc trưng của thể loại.”*

== B. Ba Khuôn Kết Bài (Khẳng Định Giá Trị Theo Tiêu Chí Đo Được)

- #strong[Khuôn 1 — Khẳng định bằng sức sống lâu bền:] Nhắc lại lí do truyện còn được kể hôm nay: có mặt trong sách giáo khoa, được dựng thành phim, kịch, tranh, trở thành chất liệu của văn học hiện đại.
- #strong[Khuôn 2 — Khẳng định bằng bài học cho người trẻ:] Từ thông điệp của truyện rút ra một hành động cụ thể của bản thân (giữ gìn môi trường, biết ơn người đi trước, kiên trì trước thử thách, sống có trách nhiệm với cộng đồng).
- #strong[Khuôn 3 — Khẳng định bằng giới hạn và giá trị còn lại:] Thẳng thắn nhìn nhận cách lí giải của người xưa đã bị khoa học vượt qua, rồi chỉ ra giá trị còn nguyên: vẻ đẹp trí tưởng tượng, bản sắc văn hoá, bài học ứng xử.

#trap-box(title: "ĐỪNG BIẾN MỞ BÀI THÀNH BÀI MẪU CỦA NGƯỜI KHÁC")[
  Một lớp 40 học sinh nộp 40 bài có cùng đoạn mở bài thì không ai đạt điểm Sáng tạo. Hãy giữ lại cấu trúc của khuôn (dẫn dắt → giới thiệu → luận đề) rồi #strong[thay hai chi tiết]: câu dẫn dắt nói về hiện tượng của truyện em sắp phân tích, và luận đề nêu đúng chủ đề riêng của truyện ấy. Hai thay đổi nhỏ đủ để đoạn mở bài mang dấu ấn cá nhân.
]

= 5.9. Kho Nhận Định Lí Luận Văn Học & Quy Tắc Dẫn

Chỉ dẫn nhận định khi em nhớ chắc nội dung. Dẫn sai một nhận định khiến giám khảo mất niềm tin vào toàn bộ phần lí luận của bài. Bảng dưới chia làm hai nhóm: nhóm có thể kiểm chứng và nhóm nên dùng như một cách diễn đạt của riêng em.

#study-table(
  (1.5fr, 3.4fr, 2.1fr),
  ("Tác giả / Nguồn", "Nguyên văn hoặc tinh thần nhận định", "Vị trí vận dụng"),

  [*C. Mác*],
  [“Thần thoại là tự nhiên và các hình thái xã hội đã được trí tưởng tượng dân gian chế biến đi một cách vô ý thức bằng nghệ thuật.”],
  [Phân tích thủ pháp kì ảo và việc nhân hóa tự nhiên.],

  [*C. Mác*],
  [Thần thoại mang “sức hấp dẫn vĩnh cửu” của một giai đoạn “một đi không trở lại” trong tuổi thơ nhân loại.],
  [Mở bài hoặc Kết bài, khi khẳng định sức sống thần thoại.],

  [*M. Gorki*],
  [Thần thoại phản ánh thiên nhiên và cuộc đấu tranh với thiên nhiên trong trí tưởng tượng nghệ thuật của người tiền sử.],
  [Luận điểm về khát vọng chinh phục tự nhiên.],

  [*Hê-ghen (G. W. F. Hegel)*],
  [Nhân vật là trung tâm để tư tưởng của tác phẩm bừng sáng.],
  [Mở đoạn phân tích hình tượng nhân vật thần linh.],

  [*Lê-ô-nốp (L. Leonov)*],
  [Mỗi tác phẩm là một phát minh về hình thức và một khám phá về nội dung.],
  [Câu chuyển ý từ phần Chủ đề sang phần Nghệ thuật.],

  [*SGK Ngữ văn 10, KNTT*],
  [Thần thoại là thể loại truyện kể xa xưa nhất, thể hiện quan niệm về vũ trụ và khát vọng chinh phục thế giới tự nhiên của con người thời nguyên thủy.],
  [Dùng ở Tầng 2 để xác định thể loại, an toàn tuyệt đối vì đúng sách giáo khoa.],
)

#callout(
  title: "CÁCH VIẾT CÂU NHẬN ĐỊNH KHI KHÔNG CHẮC VỀ NGUỒN",
  tone: "gold",
  icon: "★"
)[
  Thay vì gán một câu nói cho một học giả mà em không kiểm chứng được, hãy viết theo cách chủ động: *“Thường khi đọc thần thoại, ta có cảm giác mỗi chi tiết hoang đường đều ẩn chứa một hạt nhân quan sát thực tế”* hoặc *“Có ý kiến cho rằng vẻ đẹp của thần thoại nằm ở sự hồn nhiên chứ không nằm ở độ chính xác”*. Câu văn vẫn mang tầm khái quát, lại không có rủi ro sai nguyên văn.
]

= 5.10. Mười Lỗi Chí Mạng Trong Bài Văn 4,0 Điểm & Cách Chữa

#study-table(
  (0.55fr, 2.0fr, 2.6fr, 2.65fr),
  ("STT", "Lỗi", "Biểu hiện cụ thể", "Cách chữa"),

  [*1*], [*Kể lại truyện thay vì nghị luận*],
  [Hơn nửa Thân bài thuật lại sự việc theo trình tự thời gian.],
  [Mỗi đoạn phải có câu chủ đề là một nhận xét; sự việc chỉ xuất hiện trong câu dẫn chứng.],

  [*2*], [*Tóm tắt quá dài*],
  [Đoạn tóm tắt chiếm nửa trang giấy.],
  [Giữ đúng 4–6 câu (90 – 120 chữ).],

  [*3*], [*Bỏ quên nghệ thuật*],
  [Chỉ phân tích nội dung, chủ đề.],
  [Đề yêu cầu rõ “những nét đặc sắc về hình thức nghệ thuật”. Dành ít nhất 35 – 40% dung lượng Thân bài cho nghệ thuật.],

  [*4*], [*Nghệ thuật rời rạc, không gắn chủ đề*],
  [Liệt kê “ngôi thứ ba, phóng đại, không gian rộng” như một danh sách.],
  [Sau mỗi phương diện, thêm một câu chỉ tác dụng: thủ pháp này làm nổi bật chủ đề ra sao.],

  [*5*], [*Chê người xưa bằng chuẩn khoa học hôm nay*],
  [Viết “mê tín”, “ngu ngốc”, “vô lí”.],
  [Đặt tác phẩm vào bối cảnh nhận thức buổi bình minh nhân loại để trân trọng cách lí giải của tổ tiên.],

  [*6*], [*Nhầm người sưu tầm thành tác giả*],
  [Gọi Nguyễn Đổng Chi, Nguyễn Văn Khoả là “tác giả”.],
  [Ghi đúng: tác giả sáng tạo là *tập thể nhân dân thời cổ đại*; Nguyễn Đổng Chi là *nhà nghiên cứu sưu tầm, biên soạn*.],

  [*7*], [*Thiếu đoạn đánh giá & ý kiến cá nhân*],
  [Bài kết thúc ngay sau phần phân tích.],
  [Luôn có 1 đoạn đối sánh và rút bài học trước Kết bài (đây là vùng điểm Vận dụng 2,0đ).],

  [*8*], [*Thân bài dính thành một khối*],
  [3 trang giấy không xuống đoạn.],
  [Tách 4–5 đoạn, mỗi đoạn mở đầu bằng một câu chủ đề viết cách dòng.],

  [*9*], [*Trích dẫn sai hoặc chép cả đoạn*],
  [Đặt ngoặc kép cho cả đoạn văn, hoặc trích sai vài chữ.],
  [Chỉ trích 3–8 chữ đắt giá; đọc lại đối chiếu ngữ liệu trước khi nộp.],

  [*10*], [*Sai dung lượng & trình bày*],
  [Dưới 500 chữ, hoặc viết không chấm câu, sai chính tả hàng loạt.],
  [Dưới 500 chữ là thiếu ý; trên 1.000 chữ dễ lan sang kể lể. Bảy bài mẫu ở Phần VI được viết đầy đủ (~1.000 – 1.100 chữ) để em có nhiều ý mà chọn lọc — khi làm bài thật, giữ lại 4–5 luận điểm mạnh nhất cho vừa tầm 600 – 800 chữ. Dành 5 phút cuối rà chính tả, dấu thanh, từ Hán Việt.],
)

= 5.11. Bài Văn Mẫu Chú Giải Theo 5 Tầng (Thần Thoại “Cuộc Tu Bổ Lại Các Giống Vật”)

Bài dưới đây được chú giải từng đoạn theo mô hình 5 Tầng để học sinh thấy rõ một bài 4,0 điểm vận hành ra sao. Thẻ bên trái mỗi đoạn cho biết: đoạn ấy thuộc tầng nào, làm nhiệm vụ gì, ăn bao nhiêu điểm.

#essay-box(title: "BÀI VĂN NGHỊ LUẬN MẪU CHÚ GIẢI (~940 CHỮ — LẤY NGỮ LIỆU TỪ ĐỀ SỐ 04, PHẦN VI)")[
  #tier-tag("T1", "Mở bài · luận đề · 0,75đ")C. Mác từng nói về thần thoại như “thời thơ ấu bình thường của nhân loại”, một thời mà con người lí giải thế giới bằng trí tưởng tượng hồn nhiên trước khi khoa học xuất hiện. Trong kho tàng thần thoại Việt Nam, cách lí giải ấy có lúc diễn ra rất vui mắt, chẳng hạn ở truyện *Cuộc tu bổ lại các giống vật*. Chỉ bằng một mạch kể ngắn về lần Trời sai ba thiên thần xuống sửa lại những con vật còn dang dở, tác giả dân gian vừa cắt nghĩa đặc điểm của một số loài vật gần gũi với nhà nông, vừa gửi gắm quan niệm về trách nhiệm và lòng nhân ái với muôn loài. Hai trục giá trị ấy chính là chủ đề và đặc sắc nghệ thuật của văn bản.

  #tier-tag("T2", "Tóm tắt 4 mốc · 0,25đ")Chuyện kể rằng thuở mới nặn ra vạn vật, Ngọc Hoàng làm việc vội vã lại thiếu nguyên liệu, nên nhiều con vật bị khuyết chân, cụt cánh, đi đứng khó khăn. Thấy vậy, Trời sai ba thiên thần xuống hạ giới tu bổ. Các vị chắp thêm chân thứ tư cho chó bằng một chiếc chân ghế, chân thứ hai cho vịt, và lấy chân hương lắp cho chim chiền chiện. Lần sửa chữa vội ấy để lại dấu vết trong tập tính của từng loài: chó và vịt thường co một chân khi ngủ, còn chim chiền chiện mỗi lần đậu lại thử chân ba lần như sợ gãy.

  #tier-tag("T3", "Chủ đề · 0,75đ")Trước hết, chủ đề của truyện nằm ở cách người xưa cắt nghĩa hình hài và tập tính của muôn vật. Đứng trước muôn vàn đặc điểm của thế giới sống, câu hỏi của họ không phải là “con vật này là gì” mà là “vì sao nó lại như thế này”. Truyện trả lời bằng một chuỗi suy luận ngược: từ chỗ chó thường co một chân khi nằm, người xưa hình dung chú chó ấy có một chiếc chân ghế lắp thêm, kém chắc chắn nên phải nhấc lên; từ dáng đậu rụt rè của chim chiền chiện, họ nghĩ đến đôi chân hương nhỏ xíu, dễ gãy. Cách lí giải ấy sai về mặt sinh học, nhưng lại cho thấy một năng lực rất đáng quý: năng lực quan sát tỉ mỉ và thói quen đi tìm nguyên nhân của mọi hiện tượng. Đó là mầm mống của tư duy khoa học, chỉ là nó được bọc trong lớp vỏ thần thoại.

  #tier-tag("T3", "Tầng nghĩa nhân sinh")Bên cạnh việc cắt nghĩa tự nhiên, truyện còn gửi gắm một bài học ứng xử. Thế giới trong truyện không hoàn hảo ngay từ đầu: Trời làm vội, vật bị khuyết, rồi mới có một cuộc đi sửa chữa. Hình ảnh ba thiên thần cặm cụi lắp từng chiếc chân cho con vật nhỏ bé là lời nhắc về sự cần cù, cẩn trọng và trách nhiệm với sản phẩm của mình. Lòng nhân ái của người xưa cũng thể hiện ở chỗ họ không bỏ mặc những sinh linh dị dạng, mà tìm cách để chúng sống được, chạy được, bay được. Đặt trong bối cảnh cư dân làm ruộng quanh năm đối mặt với nắng mưa, thái độ ấy chính là sự trân trọng từng con vật gắn bó với đời sống nhà nông.

  #tier-tag("T4", "Nghệ thuật · 1,00đ")Để làm bừng sáng chủ đề ấy, tác giả dân gian sử dụng hệ thống hình thức nghệ thuật mang đậm dấu ấn thể loại. Không gian của truyện trải từ Thiên đình xuống hạ giới, còn thời gian thì phiếm chỉ cổ sơ, không gắn với một triều đại nào, nên câu chuyện mang tầm vóc của một sự kiện thuở khai thiên. Trên nền ấy, cốt truyện được tổ chức đơn tuyến theo quan hệ nhân quả: vật bị khuyết → Trời sai đi sửa → kết quả còn lưu lại thành tập tính. Mỗi chi tiết kì ảo trong cốt truyện đều bám vào một quan sát thực tế, nên truyện lí giải tự nhiên mà vẫn có sức thuyết phục theo lô-gích riêng của người xưa.

  #tier-tag("T4", "Chi tiết & ngôn ngữ")Đáng chú ý nhất là vật liệu mà trí tưởng tượng dân gian chọn: chân ghế, chân hương. Đó là những vật dụng có ngay trong gian nhà Việt, hằng ngày ở dưới mắt người kể chuyện. Nhờ thế, thần thoại Việt Nam mang giọng điệu hóm hỉnh, mộc mạc, khác hẳn với vẻ uy nghi tráng lệ của thần thoại Hy Lạp hay quy mô đồ sộ của thần thoại Trung Hoa. Ngôi kể thứ ba toàn tri cho phép người kể bao quát cả cõi trời lẫn mặt đất, còn lời kể thì ngắn gọn, nhịp nhanh, không mở rộng thành những đoạn miêu tả cầu kì, đúng với đặc trưng của truyện kể dân gian được truyền miệng qua nhiều thế hệ.

  #tier-tag("T5", "Đánh giá · 0,50đ")Đặt cạnh *Thần Trụ Trời* hay *Thần Sét* trong SGK *Kết nối tri thức*, truyện có cùng mục đích cắt nghĩa nguồn gốc nhưng chọn một hướng đi khác: hai truyện kia dựng lên những hình tượng khổng lồ, còn truyện này nhỏ nhặt, sát với bếp núc và sân nhà. Sự khác biệt ấy làm rõ bản sắc thần thoại Việt Nam: cư dân lúa nước nhìn vũ trụ bằng con mắt của người làm ruộng, nên thần linh của họ cũng thân thuộc như hàng xóm. Ngày nay, khi sinh học đã giải thích cặn kẽ cấu tạo của từng loài, giá trị của truyện không nằm ở lời giải thích mà nằm ở thái độ sống: nhìn thấy điều chưa ổn thì sửa, thấy sinh linh yếu thế thì giúp, và luôn giữ sự tò mò trước thế giới xung quanh.

  #tier-tag("T5", "Kết bài · 0,50đ")Khép lại truyện *Cuộc tu bổ lại các giống vật*, người đọc hôm nay vẫn mỉm cười trước cách người xưa lí giải đôi chân của con chó hay con chim chiền chiện. Truyện còn được kể, được đưa vào sách, được các em học sinh đọc lại mỗi năm, bởi nó lưu giữ một phần trí tưởng tượng nguyên sơ của dân tộc và một bài học giản dị: làm việc gì cũng cần đến nơi đến chốn, và sự tử tế với muôn loài là thước đo của con người.
]
