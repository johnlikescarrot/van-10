# -*- coding: utf-8 -*-
"""Phần 1: Giải mã Ma trận & Bản đặc tả — bám sát file .docx của nhà trường."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)


def build(doc):
    doc.h1("PHẦN 1", "Giải mã Ma trận & Bản đặc tả đề thi")

    doc.para(
        "Mọi chiến lược ôn tập hiệu quả đều bắt đầu từ việc **đọc đúng “bản thiết kế”** của đề thi. "
        "Phần này phân tích trực tiếp *Ma trận, Bản đặc tả đề kiểm tra giữa học kì I lớp 10* "
        "(năm học 2026–2027, thời gian làm bài **90 phút**) để bạn biết chính xác: "
        "thi bao nhiêu câu, hỏi nội dung gì, ở cấp độ tư duy nào và chiếm bao nhiêu điểm.")

    # ------------------------------------------------ mục tiêu
    doc.h2("1.1. Mục tiêu của đề kiểm tra (trích từ Bản đặc tả)")
    doc.h3("a) Về năng lực")
    doc.bullets([
        "Thu thập thông tin để đánh giá mức độ đạt chuẩn **kiến thức, kĩ năng** đối với các nội dung "
        "**Đọc hiểu** và **Viết** trọng tâm trong nửa đầu học kì I, chương trình Ngữ văn 10.",
        "Phát huy **năng lực tư duy, năng lực sử dụng ngôn ngữ và năng lực sáng tạo** của học sinh.",
        "Đánh giá năng lực **đọc hiểu một văn bản ngoài sách giáo khoa**; kĩ năng **viết bài văn nghị luận "
        "phân tích, đánh giá một tác phẩm văn học (ngoài sách giáo khoa)**; kĩ năng trình bày, diễn đạt "
        "rõ ràng, đúng quy cách.",
    ])
    doc.h3("b) Về phẩm chất")
    doc.para(
        "Hình thành quan điểm tích cực trước những vấn đề cần nghị luận; có ý thức sống lành mạnh, "
        "có tâm hồn phong phú.")

    doc.box("info", [
        "**Hai trục năng lực xuyên suốt đề thi:** (1) ĐỌC HIỂU – 60% điểm; (2) VIẾT – 40% điểm. "
        "Cả hai trục đều dùng **ngữ liệu ngoài sách giáo khoa** thuộc thể loại **truyện thần thoại**.",
    ])

    # ------------------------------------------------ ma trận
    doc.h2("1.2. Ma trận đề kiểm tra (tái lập chính xác)")
    doc.data_table(
        ["Kĩ năng", "Nội dung/đơn vị kiến thức", "Biết\n(TNKQ / TL)", "Hiểu\n(TNKQ / TL)",
         "Vận dụng\n(TNKQ / TL)", "Tổng % điểm"],
        [
            ["ĐỌC HIỂU", "Truyện thần thoại", "6 / 0", "2 / 1", "0 / 1", "60%"],
            ["VIẾT", "Viết văn bản nghị luận phân tích, đánh giá tác phẩm truyện",
             "0 / 1*", "0 / 1*", "0 / 1*", "40%"],
        ],
        widths=[24, 52, 25, 25, 28, 22], size=8.6)
    doc.para(
        "Ghi chú: dấu * ở phần Viết nghĩa là **một bài viết tự luận duy nhất** được chấm theo cả ba cấp độ "
        "Biết – Hiểu – Vận dụng trong cùng một sản phẩm (mở bài/thân bài/kết bài và các tầng phân tích).",
        size=9.2, family="sans")

    doc.h3("Tỉ lệ điểm theo loại câu hỏi và theo cấp độ tư duy")
    doc.data_table(
        ["Tiêu chí", "Số liệu trong Bản đặc tả", "Diễn giải dễ hiểu"],
        [
            ["Điểm TNKQ (trắc nghiệm)", "30%", "8 câu trắc nghiệm, mỗi câu 0,5 điểm = 4,0 điểm quy đổi 30%"],
            ["Điểm tự luận Đọc hiểu", "30% (10% + 20%)", "2 câu tự luận: 1 câu Thông hiểu (1đ) + 1 câu Vận dụng (1đ)"],
            ["Điểm bài viết (Viết)", "40%", "1 bài nghị luận phân tích, đánh giá tác phẩm truyện (4đ)"],
            ["Cấp độ BIẾT", "40%", "Chủ yếu là 6 câu TNKQ nhận biết + yêu cầu giới thiệu tác phẩm trong bài viết"],
            ["Cấp độ HIỂU", "30%", "2 câu TNKQ thông hiểu + 1 câu tự luận + tầng phân tích trong bài viết"],
            ["Cấp độ VẬN DỤNG", "30%", "1 câu tự luận vận dụng + tầng đánh giá, liên hệ, sáng tạo trong bài viết"],
        ],
        widths=[42, 40, 94], size=8.8)

    # ------------------------------------------------ cấu trúc 11 câu
    doc.h2("1.3. Đề thi sẽ trông như thế nào? — Cấu trúc 11 câu")
    doc.data_table(
        ["Câu", "Hình thức", "Cấp độ", "Nội dung kiểm tra (theo Bản đặc tả)", "Điểm"],
        [
            ["1–6", "TNKQ", "Nhận biết (Biết)",
             "Nhận biết không gian, thời gian; đặc điểm cốt truyện, sự kiện, nhân vật; đề tài, chi tiết tiêu biểu; bối cảnh lịch sử – văn hoá",
             "6 × 0,5"],
            ["7–8", "TNKQ", "Thông hiểu (Hiểu)",
             "Hiểu ý nghĩa chi tiết, hình tượng, thông điệp; phân biệt lựa chọn đúng dựa trên ngữ liệu",
             "2 × 0,5"],
            ["9", "Tự luận", "Thông hiểu (Hiểu)",
             "Tóm tắt cốt truyện; phân tích nhân vật; nêu chủ đề/thông điệp và căn cứ; tác dụng ngôi kể, lời kể",
             "1,0"],
            ["10", "Tự luận", "Vận dụng",
             "Rút bài học cách nghĩ, cách ứng xử; ý nghĩa tác phẩm với bản thân; đánh giá chi tiết, hình tượng, thông điệp",
             "1,0"],
            ["11", "Tự luận (Viết)", "Biết – Hiểu – Vận dụng",
             "Viết bài nghị luận phân tích, đánh giá tác phẩm truyện (thần thoại, ngữ liệu ngoài SGK)",
             "4,0"],
        ],
        widths=[14, 22, 32, 86, 22], size=8.4)

    doc.box("memory", [
        "**Công thức nhớ nhanh cấu trúc: “8 TN – 2 TL – 1 văn”.** "
        "Tổng 11 câu; thời gian 90 phút; thang điểm 10 (Đọc hiểu 6đ + Viết 4đ).",
        "**Tỉ lệ vàng 40 – 30 – 30:** cứ 10 điểm thì 4 điểm Nhận biết, 3 điểm Thông hiểu, 3 điểm Vận dụng. "
        "Muốn đạt 8+, không được bỏ qua tầng Vận dụng (câu 10 và phần đánh giá – liên hệ trong câu 11).",
    ])

    # ------------------------------------------------ bản đặc tả chi tiết
    doc.h2("1.4. Bản đặc tả: “Lộ trình” những gì bạn PHẢI làm được")
    doc.h3("a) Đọc hiểu — Thần thoại (ngữ liệu ngoài SGK)")
    doc.data_table(
        ["Cấp độ", "Yêu cầu cần đạt (đọc nguyên văn tinh thần Bản đặc tả)"],
        [
            ["NHẬN BIẾT",
             "• Nhận biết không gian, thời gian trong truyện thần thoại.\n"
             "• Nhận biết đặc điểm cốt truyện, sự kiện, câu chuyện, nhân vật.\n"
             "• Nhận biết đề tài, chi tiết tiêu biểu, đặc trưng của truyện thần thoại.\n"
             "• Nhận biết bối cảnh lịch sử – văn hoá được thể hiện trong truyện."],
            ["THÔNG HIỂU",
             "• Tóm tắt được cốt truyện.\n"
             "• Hiểu, phân tích nhân vật; lí giải vị trí, vai trò, ý nghĩa nhân vật.\n"
             "• Nêu chủ đề, tư tưởng, thông điệp; phân tích căn cứ xác định chủ đề.\n"
             "• Lí giải tác dụng việc chọn nhân vật người kể chuyện; lời người kể, lời nhân vật.\n"
             "• Lí giải ý nghĩa, tác dụng của đề tài, chi tiết tiêu biểu, đặc trưng thể loại."],
            ["VẬN DỤNG",
             "• Rút bài học về cách nghĩ, cách ứng xử do văn bản gợi ra.\n"
             "• Nêu ý nghĩa/tác động của tác phẩm với nhận thức, tình cảm, quan niệm bản thân.\n"
             "• Vận dụng hiểu biết về bối cảnh lịch sử – văn hoá để lí giải ý nghĩa, thông điệp.\n"
             "• Đánh giá ý nghĩa, giá trị của thông điệp, chi tiết, hình tượng theo quan điểm cá nhân."],
        ],
        widths=[28, 148], size=8.8)

    doc.h3("b) Viết — Nghị luận phân tích, đánh giá một tác phẩm truyện")
    doc.data_table(
        ["Cấp độ", "Yêu cầu cần đạt"],
        [
            ["BIẾT",
             "• Giới thiệu đầy đủ thông tin chính: tên tác phẩm, tác giả (hoặc dân gian), thể loại…\n"
             "• Trình bày những nội dung khái quát của tác phẩm."],
            ["HIỂU",
             "• Triển khai vấn đề nghị luận thành các luận điểm phù hợp.\n"
             "• Phân tích đặc sắc nội dung, hình thức nghệ thuật và chủ đề.\n"
             "• Kết hợp lí lẽ và dẫn chứng để tạo tính chặt chẽ, logic.\n"
             "• Đảm bảo cấu trúc văn nghị luận; chuẩn chính tả, ngữ pháp tiếng Việt."],
            ["VẬN DỤNG",
             "• Nêu bài học rút ra từ tác phẩm.\n"
             "• Thể hiện sự đồng tình/không đồng tình với thông điệp của tác giả.\n"
             "• Đánh giá ý nghĩa, giá trị nội dung và hình thức tác phẩm.\n"
             "• Thể hiện quan điểm, cá tính; sáng tạo trong cách diễn đạt."],
        ],
        widths=[28, 148], size=8.8)

    doc.box("warn", [
        "**Điểm mấu chốt nhiều học sinh bỏ sót:** ngữ liệu đọc hiểu và tác phẩm dùng để viết đều "
        "**NGOÀI SÁCH GIÁO KHOA**. Điều đó nghĩa là đề thi *không* kiểm tra trí nhớ thuộc lòng một truyện cụ thể, "
        "mà kiểm tra **năng lực vận dụng tri thức thể loại** để xử lí một truyện thần thoại bất kì. "
        "Vì vậy, học chắc “bộ khung” thần thoại (Phần 2) và kĩ năng đọc – viết (Phần 3, Phần 6) quan trọng hơn học vẹt.",
    ])

    doc.h2("1.5. Ba sự thật then chốt về kì thi này")
    doc.numbered([
        "**Chỉ có MỘT thể loại làm trung tâm: truyện thần thoại.** Mọi câu hỏi, từ trắc nghiệm đến bài văn 4 điểm, "
        "đều quy về việc hiểu và phân tích thần thoại. Đầu tư sâu một thể loại sẽ trả trọn điểm cả bài.",
        "**Ngữ liệu ngoài SGK nhưng “vũ khí” thì nằm trong SGK.** Bạn dùng tri thức về thời gian – không gian, "
        "nhân vật, cốt truyện, lời kể, chủ đề (học ở Bài 1 – *Sức hấp dẫn của truyện kể*) để giải mã một truyện mới.",
        "**Điểm cao thuộc về kĩ năng chứ không phải trí nhớ.** Câu Vận dụng và bài viết đòi hỏi phân tích, đánh giá, "
        "liên hệ cá nhân — những năng lực chỉ hình thành qua luyện tập có phương pháp (xem Phần 8, lộ trình 7 ngày).",
    ])
