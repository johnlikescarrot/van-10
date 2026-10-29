#import "template.typ": *

#part-banner(
  "PHẦN V",
  "Viết Bài Văn Phân Tích, Đánh Giá Một Tác Phẩm Truyện",
  "Đọc yêu cầu • Lập luận có bằng chứng • Phân tích chủ đề và nghệ thuật • Đánh giá có căn cứ"
)

= 5.1. Hiểu đúng nhiệm vụ viết 4,0 điểm

Bản đặc tả yêu cầu một bài nghị luận phân tích, đánh giá tác phẩm truyện; trong phạm vi kiểm tra này, ngữ liệu luyện tập hướng tới thần thoại ngoài sách giáo khoa. Bài viết không chỉ kể lại chuyện hoặc nêu cảm nghĩ chung chung. Người viết cần trả lời hai câu hỏi gắn với nhau:

- *Tác phẩm nói gì?* — xác định chủ đề, các nhận thức/khát vọng được gửi gắm và dẫn chứng tiêu biểu.
- *Tác phẩm được kể bằng cách nào?* — phân tích cốt truyện, tình huống, nhân vật, chi tiết kì ảo, người kể chuyện, không gian – thời gian, ngôn ngữ; sau đó chỉ ra tác dụng của chúng.

#callout(title: "ĐỌC ĐỀ TRƯỚC KHI LẬP DÀN Ý", tone: "blue", icon: "i")[
  Khoanh ba từ khóa trong đề: *đối tượng* (tác phẩm/đoạn trích nào), *thao tác* (phân tích, đánh giá, làm rõ...) và *phạm vi* (chủ đề, những nét đặc sắc về hình thức nghệ thuật, hoặc một phương diện cụ thể). Nếu đề cho đoạn trích, chỉ dùng những chi tiết có trong đoạn trích; không thêm tình tiết theo trí nhớ mơ hồ.
]

#study-table(
  (1.45fr, 3.55fr, 1.55fr),
  ("Thành phần cần có", "Dấu hiệu của bài làm có căn cứ", "Liên hệ Ma trận"),
  [*Giới thiệu và khái quát*], [Nêu đúng nhan đề, thể loại/nguồn gốc khi đề cho; tóm tắt rất ngắn mạch sự kiện để tạo nền cho phân tích.], [Nhận biết: bài viết tích hợp 1,0 điểm.],
  [*Phân tích chủ đề*], [Nêu một nhận định khái quát rồi giải thích bằng sự kiện, nhân vật hoặc chi tiết; phân biệt đề tài với chủ đề.], [Thông hiểu: bài viết tích hợp 1,0 điểm.],
  [*Phân tích hình thức nghệ thuật*], [Chọn vài thủ pháp thật sự nổi bật, gọi tên đúng, chỉ ra chi tiết và giải thích chúng góp phần làm rõ chủ đề như thế nào.], [Thông hiểu và Vận dụng.],
  [*Đánh giá và quan điểm*], [Nhận xét giá trị nhận thức, văn hóa, thẩm mĩ; nêu góc nhìn riêng hợp lí, có thể liên hệ ngắn khi phù hợp.], [Vận dụng: bài viết tích hợp 2,0 điểm.],
  [*Diễn đạt*], [Bố cục rõ; dùng từ đúng nghĩa; đoạn văn liên kết; trích dẫn chính xác từ ngữ liệu đề cho.], [Giáo viên quyết định rubric chi tiết.]
)

Các mốc 1,0 – 1,0 – 2,0 ở bảng trên là mức phân bố theo Ma trận. Ma trận không chia sẵn điểm cho mở bài, chính tả, số chữ hay từng luận điểm. Vì thế, mọi bảng tự chấm trong đề cương chỉ hỗ trợ học sinh rà ý; đáp án và hướng dẫn chấm của giáo viên là căn cứ khi kiểm tra chính thức.

= 5.2. Dàn ý năm tầng: linh hoạt, không phải khuôn mẫu bắt buộc

#block(
  width: 100%,
  fill: white,
  stroke: 1pt + c-indigo,
  radius: 6pt,
  inset: 11pt,
  breakable: false,
)[
  #align(center)[
    #text(weight: "bold", size: 9.8pt, fill: c-navy)[SƠ ĐỒ NĂM TẦNG TRIỂN KHAI BÀI VĂN PHÂN TÍCH, ĐÁNH GIÁ TÁC PHẨM TRUYỆN]
  ]
  #v(6pt)
  #grid(
    columns: (1fr,),
    row-gutter: 5pt,
    block(fill: rgb("#14284B"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: rgb("#FCD34D"))[TẦNG 1 — MỞ BÀI:] #text(size: 8.4pt, fill: white)[Dẫn vào vừa đủ; giới thiệu tác phẩm và nêu luận đề bao quát về chủ đề cùng một vài nét nghệ thuật đáng chú ý.]
    ],
    block(fill: rgb("#EFF8FF"), stroke: 0.7pt + rgb("#84CAFF"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: rgb("#175CD3"))[TẦNG 2 — KHÁI QUÁT:] #text(size: 8.4pt, fill: c-ink)[Xác định thể loại/đề tài nếu có cơ sở; tóm tắt mạch sự kiện bằng vài câu, chỉ giữ chi tiết sẽ được phân tích.]
    ],
    block(fill: rgb("#FFFAEB"), stroke: 0.7pt + rgb("#FDB022"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: rgb("#B54708"))[TẦNG 3 — PHÂN TÍCH CHỦ ĐỀ:] #text(size: 8.4pt, fill: c-ink)[Trả lời: truyện cắt nghĩa hiện tượng, nhận thức đời sống hay gửi gắm khát vọng gì? Mỗi ý cần một hoặc hai bằng chứng từ văn bản.]
    ],
    block(fill: rgb("#F4F3FF"), stroke: 0.7pt + rgb("#9B8AFB"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: c-purple)[TẦNG 4 — PHÂN TÍCH NGHỆ THUẬT:] #text(size: 8.4pt, fill: c-ink)[Chọn 2–3 phương diện nổi bật: cốt truyện, tình huống, nhân vật, chi tiết kì ảo, không–thời gian, người kể, ngôn ngữ... Đừng liệt kê; mỗi thủ pháp phải được nối với ý nghĩa.]
    ],
    block(fill: rgb("#ECFDF3"), stroke: 0.7pt + rgb("#6CE9A6"), radius: 4pt, inset: (x: 10pt, y: 6pt), width: 100%)[
      #text(weight: "bold", size: 8.6pt, fill: c-jade)[TẦNG 5 — ĐÁNH GIÁ VÀ KẾT BÀI:] #text(size: 8.4pt, fill: c-ink)[Khái quát giá trị của tác phẩm; liên hệ hoặc đối sánh ngắn khi làm sáng rõ nhận xét; khẳng định lại luận đề bằng một câu kết gọn, không lặp nguyên văn mở bài.]
    ]
  )
]

#mnemonic-box(title: "MẸO LẬP DÀN Ý TRONG 3 PHÚT: 1 – 2 – 3")[
  Viết nháp *1 luận đề* cho cả bài; chọn *2 trục* (chủ đề và nghệ thuật); dưới mỗi trục ghi *3 bằng chứng ngắn* từ ngữ liệu. Nếu không tìm được bằng chứng, hãy đổi hoặc thu hẹp luận điểm trước khi viết.
]

= 5.3. Biến chi tiết thành lập luận: P – E – E – V

Một đoạn phân tích có thể triển khai theo bốn mắt xích sau. Không cần lặp nguyên công thức ở mọi đoạn, nhưng cần giữ quan hệ giữa nhận định và bằng chứng.

1. #strong[P — Point / Luận điểm:] Câu đầu nêu điều cần chứng minh. Ví dụ: *“Chi tiết ngọn lửa trong truyện vừa mở ra ước mơ no ấm, vừa cho thấy sự trân trọng của cư dân xưa đối với phát hiện về lửa.”*
2. #strong[E — Evidence / Bằng chứng:] Nhắc chính xác chi tiết hoặc cụm từ then chốt; chỉ trích dẫn ngắn, không chép cả đoạn văn.
3. #strong[E — Explanation / Giải thích:] Lí giải chi tiết ấy gợi ra điều gì, có tác dụng gì trong mạch truyện; tránh dừng ở câu “làm cho câu văn sinh động”.
4. #strong[V — Valuation / Bình giá:] Đặt nhận xét vào chủ đề hoặc giá trị của tác phẩm. Ví dụ: *“Nhờ vậy, tưởng tượng kì ảo không tách rời đời sống mà lưu giữ kinh nghiệm và khát vọng của cộng đồng.”*

#formula-box(title: "CÂU NỐI TỪ NGHỆ THUẬT SANG Ý NGHĨA")[
  “Chi tiết/cách kể ấy không chỉ ... mà còn ...”; “Từ hình thức hư cấu này, người kể dân gian làm nổi bật ...”; “Sự đối lập giữa ... và ... khiến chủ đề ... trở nên rõ hơn.”
]

= 5.4. Bốn cách mở bài và ba cách kết bài an toàn

Các khuôn dưới đây là câu gợi ý do đề cương soạn. Hãy thay từ trong ngoặc bằng thông tin có trong đề, rút ngắn hoặc đổi giọng văn cho tự nhiên; không cần cố dùng câu dẫn hoa mĩ.

== A. Mở bài

- #strong[Mở từ giá trị trí tưởng tượng:] *“Từ rất sớm, con người đã dùng những câu chuyện kì ảo để hình dung về thế giới và chính mình. Trong dòng chảy ấy, [tên tác phẩm] gây ấn tượng bởi câu chuyện về [sự kiện/nhân vật], qua đó gợi lên [chủ đề]. Tác phẩm còn hấp dẫn ở [hai nét nghệ thuật].”*
- #strong[Mở từ đặc trưng thể loại:] *“Thần thoại đưa thiên nhiên và khát vọng con người vào thế giới của các vị thần. [Tên tác phẩm] là một truyện như vậy: bằng [chi tiết/cốt truyện nổi bật], văn bản vừa cắt nghĩa [hiện tượng] vừa bộc lộ [nhận thức/ước mơ] qua cách kể giàu màu sắc kì ảo.”*
- #strong[Mở từ tình huống truyện:] *“Một tình huống giàu nghịch lí thường làm người đọc chú ý vì nó buộc nhân vật bộc lộ lựa chọn. Từ tình huống [nêu thật ngắn], [tên tác phẩm] mở ra suy ngẫm về [chủ đề], đồng thời thể hiện bút pháp [nét nghệ thuật].”*
- #strong[Mở trực tiếp:] *“[Tên tác phẩm] thuộc [thể loại/nguồn gốc nếu đề cho] kể về [mạch sự kiện ngắn]. Qua văn bản, người đọc nhận ra [luận đề], được thể hiện thuyết phục bằng [hai phương diện nghệ thuật].”*

== B. Kết bài

- *“Từ câu chuyện về [nhân vật/sự kiện], tác phẩm làm sáng rõ [chủ đề]. Sức sống của truyện nằm ở chỗ những chi tiết kì ảo vẫn dẫn người đọc hôm nay trở về với một khát vọng rất người: [khát vọng].”*
- *“Nhờ [nét nghệ thuật 1] và [nét nghệ thuật 2], [tên tác phẩm] không chỉ kể một câu chuyện xưa mà còn lưu giữ cách cộng đồng nhìn nhận thế giới. Đó là giá trị đáng trân trọng của văn bản.”*
- *“Khép lại trang truyện, [hình ảnh/chi tiết] còn ở lại như một gợi nhắc về [bài học]. Tuy vậy, bài học ấy chỉ có ý nghĩa khi được rút ra từ những chứng cứ cụ thể của văn bản.”*

= 5.5. Tám câu bình giá tự soạn — dùng như điểm tựa, không dùng như trích dẫn

Không ghi tên học giả cho những câu chưa đối chiếu được văn bản gốc. Tám câu dưới đây do đề cương biên soạn, học sinh có thể diễn đạt lại theo ngữ liệu:

#study-table(
  (0.75fr, 4.25fr, 1.7fr),
  ("", "Câu bình giá gợi ý", "Nên dùng khi"),
  [1], [Chi tiết kì ảo làm cho cách lí giải tự nhiên trở nên giàu hình ảnh, đồng thời cho thấy trí tưởng tượng của cộng đồng.], [Phân tích thần thoại suy nguyên.],
  [2], [Nhân vật không chỉ có quyền năng khác thường; qua hành động của họ, người xưa gửi gắm mong muốn chế ngự những bất trắc của đời sống.], [Phân tích nhân vật thần linh.],
  [3], [Cốt truyện gọn giúp sự kiện trung tâm nổi bật, từ đó ý nghĩa cắt nghĩa hiện tượng được tập trung hơn.], [Phân tích kết cấu.],
  [4], [Không gian rộng và thời gian cổ sơ làm cho công việc của nhân vật mang tầm vóc của một cuộc kiến tạo thế giới.], [Phân tích không–thời gian.],
  [5], [Cách kể mộc mạc không làm câu chuyện đơn giản đi; trái lại, nó khiến trí tưởng tượng kì vĩ gần với kinh nghiệm sống của cộng đồng.], [Phân tích ngôn ngữ/người kể.],
  [6], [Giá trị của truyện không nằm ở việc giải thích khoa học chính xác mà ở việc lưu giữ một cách nhìn giàu khát vọng về thiên nhiên và con người.], [Đánh giá giá trị nhận thức.],
  [7], [Một đối sánh chỉ đáng dùng khi nó làm sáng rõ nét riêng của văn bản đang phân tích, không phải để khoe thêm dẫn chứng.], [Đoạn đánh giá mở rộng.],
  [8], [Nhận xét cá nhân thuyết phục nhất khi trở lại với một chi tiết cụ thể thay vì dùng lời khen chung chung.], [Rà soát trước khi kết bài.]
)

= 5.6. Ví dụ chuyển giao kĩ năng: *Chữ người tử tù* của Nguyễn Tuân

Văn bản này thuộc Bài 1 của *Ngữ văn 10, Kết nối tri thức với cuộc sống*, nhưng khác với ngữ liệu thần thoại của ma trận giữa kì: đây là truyện ngắn hiện đại. Học nó để thấy cùng một thao tác phân tích có thể áp dụng linh hoạt cho nhiều tác phẩm truyện, chứ không để thay thế phạm vi ngữ liệu kiểm tra.

#callout(title: "LUẬN ĐỀ MẪU", tone: "purple", icon: "✦")[
  *Chữ người tử tù* tôn vinh vẻ đẹp của tài hoa, khí phách và thiên lương; thành công ấy được tạo nên bởi tình huống truyện đối nghịch, thủ pháp tương phản và cảnh cho chữ giàu ý nghĩa biểu tượng.
]

#study-table(
  (1.25fr, 2.85fr, 2.6fr),
  ("Luận điểm", "Bằng chứng nên chọn", "Hướng phân tích và đánh giá"),
  [*Tình huống truyện*], [Người quản ngục ở phía quyền lực nhưng kính trọng người tử tù; Huấn Cao là người bị giam nhưng giữ phẩm giá và quyền chủ động tinh thần.], [Nghịch lí ấy làm căng thẳng câu chuyện, tạo điều kiện để vẻ đẹp nhân cách của cả hai nhân vật được bộc lộ.],
  [*Hình tượng Huấn Cao*], [Tài viết chữ, khí phách không khuất phục và sự trân trọng tấm lòng biết yêu cái đẹp.], [Không tách tài với tâm: tài hoa chỉ có ý nghĩa khi gắn với thiên lương và lựa chọn hướng thiện.],
  [*Cảnh cho chữ*], [Không gian đề lao tối tăm đối lập với ánh sáng, mùi thơm và hành động sáng tạo chữ viết.], [Tương phản làm nổi bật sự chiến thắng về tinh thần của cái đẹp, cái thiện trước môi trường tăm tối.],
  [*Nghệ thuật*], [Ngôn ngữ cổ kính, chi tiết tương phản, nhịp kể dồn về cảnh cho chữ.], [Hình thức nghệ thuật không chỉ trang trí mà tổ chức chủ đề; đây là điều cần chỉ ra trong mọi bài phân tích truyện.]
)

#trap-box(title: "KHI VIẾT VỀ CHỮ NGƯỜI TỬ TÙ")[
  Không kể lại dài dòng toàn bộ câu chuyện; không gắn vào tác phẩm những câu nói không nhớ chính xác; không nhầm việc ca ngợi cái đẹp với phủ nhận hiện thực nhà tù. Hãy chọn một chi tiết, nêu tác dụng và quay lại luận đề về tài hoa, khí phách, thiên lương.
]

= 5.7. Bảng tự rà trước khi nộp bài

#study-table(
  (0.55fr, 4.8fr, 1.35fr),
  ("", "Câu hỏi tự kiểm", "Tự đánh dấu"),
  [□], [Tôi đã trả lời đúng yêu cầu đề và nêu được một luận đề rõ trong mở bài.], [Có / Cần sửa],
  [□], [Tôi tóm tắt ngắn, không biến bài phân tích thành bài kể chuyện.], [Có / Cần sửa],
  [□], [Mỗi luận điểm lớn có dẫn chứng cụ thể, sau dẫn chứng có giải thích.], [Có / Cần sửa],
  [□], [Tôi phân tích cả chủ đề và một số nét nghệ thuật theo đúng yêu cầu đề.], [Có / Cần sửa],
  [□], [Tôi dùng từ “chủ đề”, “đề tài”, “ngôi kể”, “chi tiết” đúng nghĩa và không khẳng định điều văn bản không cho biết.], [Có / Cần sửa],
  [□], [Đoạn đánh giá của tôi có căn cứ từ văn bản; phần liên hệ không dài hơn phần phân tích.], [Có / Cần sửa],
  [□], [Tôi đã đọc lại chính tả, dấu câu, tên tác phẩm và thông tin nguồn gốc.], [Có / Cần sửa]
)

#trap-box(title: "BẢY LỖI CẦN TRÁNH")[
  1. Tóm tắt quá dài; 2. Kể tên thủ pháp mà không phân tích tác dụng; 3. Dùng lời khen chung chung như “rất hay, rất đặc sắc”; 4. Ép mọi truyện vào cùng một khuôn; 5. Gán câu trích dẫn chưa kiểm chứng cho tác giả/học giả; 6. Áp đặt chuẩn khoa học hiện đại để phủ nhận giá trị văn hóa của thần thoại; 7. Chép bài mẫu thay vì dùng bài mẫu để học cách lập luận.
]
