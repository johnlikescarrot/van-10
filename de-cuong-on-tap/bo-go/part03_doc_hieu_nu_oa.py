# -*- coding: utf-8 -*-
"""Phần 3: Kĩ năng đọc hiểu thần thoại + ngữ liệu mẫu Nữ Oa vá trời (ngoài SGK)."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)


def build(doc):
    doc.h1("PHẦN 3", "Kĩ năng đọc hiểu & ngữ liệu mẫu “Nữ Oa vá trời”")

    doc.para(
        "Phần này trang bị **quy trình đọc hiểu bốn bước** và **bộ câu hỏi định hướng theo đúng ba cấp độ** "
        "trong Bản đặc tả, sau đó áp dụng toàn bộ vào một truyện thần thoại *ngoài sách giáo khoa* tiêu biểu: "
        "*Nữ Oa vá trời*. Học xong, bạn có thể chuyển quy trình này sang bất kì ngữ liệu nào trong đề thi thật.")

    # ------------------------------------------------ quy trình
    doc.h2("3.1. Quy trình đọc hiểu thần thoại 4 bước (làm trong 5–7 phút)")
    doc.numbered([
        "**Đọc toàn văn – xác định “danh tính” văn bản:** thể loại (thần thoại suy nguyên/sáng tạo/nguồn gốc), "
        "xuất xứ (dân tộc, bộ sưu tập), đề tài chung.",
        "**Gạch chân – đánh dấu yếu tố hình thức:** các mốc *thời gian, không gian*; tên *nhân vật*; "
        "các *sự kiện, chi tiết tiêu biểu*; dấu hiệu *lời người kể – lời nhân vật*.",
        "**Tóm tắt cốt truyện theo mô hình AI – LÀM GÌ – VÌ SAO – KẾT QUẢ:** "
        "nhân vật chính là ai, hành động chính, nguyên nhân, diễn biến, kết cục.",
        "**Rút chủ đề – thông điệp – nghệ thuật – liên hệ:** văn bản muốn nói điều gì, "
        "bằng cách kể nào, bài học cho bản thân và cuộc sống hôm nay.",
    ])
    doc.box("tip", [
        "**Mẹo phòng thi:** luôn dành 1 phút *đọc câu hỏi trước khi đọc kĩ văn bản*. "
        "Vừa đọc vừa khoanh vùng sẵn dữ liệu cho từng câu, tránh đọc đi đọc lại nhiều lần mất thời gian.",
    ])

    # ------------------------------------------------ bộ câu hỏi định hướng
    doc.h2("3.2. Bộ câu hỏi định hướng theo 3 cấp độ (áp dụng cho MỌI truyện thần thoại)")
    doc.data_table(
        ["Cấp độ", "Câu hỏi định hướng cần tự trả lời được"],
        [
            ["NHẬN BIẾT",
             "• Truyện thuộc thể loại gì? Nhóm thần thoại nào (suy nguyên/sáng tạo/nguồn gốc)?\n"
             "• Câu chuyện xảy ra vào thời gian, không gian nào? Dấu hiệu nhận biết?\n"
             "• Nhân vật chính là ai? Đặc điểm hình dáng, sức mạnh, vai trò?\n"
             "• Các sự kiện chính diễn ra theo trình tự nào? Chi tiết tiêu biểu là gì?\n"
             "• Đề tài của truyện là gì? Bối cảnh lịch sử – văn hoá gợi lên ra sao?"],
            ["THÔNG HIỂU",
             "• Tóm tắt cốt truyện trong một đoạn văn ngắn.\n"
             "• Phân tích tính cách, vai trò, ý nghĩa của nhân vật chính.\n"
             "• Chủ đề, tư tưởng, thông điệp của truyện? Căn cứ nào xác định (chi tiết, hình tượng)?\n"
             "• Tác dụng của ngôi kể thứ ba/lời người kể chuyện và lời nhân vật?\n"
             "• Ý nghĩa, tác dụng của đề tài và các chi tiết tiêu biểu (đá ngũ sắc, cột trời…)?"],
            ["VẬN DỤNG",
             "• Rút ra bài học về cách nghĩ, cách ứng xử từ văn bản.\n"
             "• Truyện tác động thế nào đến nhận thức, tình cảm, quan niệm của riêng em?\n"
             "• Vận dụng bối cảnh lịch sử – văn hoá để lí giải thông điệp.\n"
             "• Đồng tình/không đồng tình với thông điệp nào? Đánh giá hình tượng, chi tiết theo quan điểm cá nhân.\n"
             "• Liên hệ với đời sống hiện tại (thiên tai, trách nhiệm cộng đồng, người “vá trời” thời bình…)."],
        ],
        widths=[26, 150], size=8.7)

    # ================= NGỮ LIỆU NỮ OA
    doc.h2("3.3. NGỮ LIỆU MINH HỌA: NỮ OA VÁ TRỜI")
    doc.reading_card(
        "NGỮ LIỆU NGOÀI SGK — THẦN THOẠI TRUNG HOA",
        "Nữ Oa vá trời",
        "Thần thoại Trung Hoa (thuật lại theo truyện dân gian)",
        [
            "Thuở vũ trụ mới hình thành, nữ thần **Nữ Oa** đã nặn đất tạo ra loài người, dạy người cách sinh sống, "
            "canh tác. Một năm, *thuỷ thần Cung Công* và *hoả thần Chúc Dung* gây cuộc chiến dữ dội. Chúc Dung thắng trận; "
            "Cung Công vừa thẹn vừa uất, điên cuồng lao đầu vào **núi Bất Chu** – vốn là một cây cột chống trời ở phía tây bắc. "
            "Cột chống trời gãy đổ, một góc vòm trời sụp xuống, hở một lỗ thủng lớn.",
            "Tức thì tai hoạ giáng xuống trần gian: trời rách toang, đất nứt lở, lửa rừng bừng cháy, "
            "nước lũ từ trên trời tuôn xuống mênh mông; *rồng đen* cùng thú dữ hung hãn săn đuổi con người. "
            "Muôn loài lâm vào cảnh nước sôi lửa bỏng.",
            "Chứng kiến cảnh tượng ấy, Nữ Oa vô cùng đau xót, quyết tâm cứu thế gian. Bà bay khắp nơi tìm cho bằng được "
            "những viên **đá ngũ sắc** (đá năm màu), chất thành núi rồi đốt lửa thiêng nung luyện cho đá chảy ra một thứ keo đặc, "
            "dùng để hàn gắn, vá lại từng lỗ thủng trên vòm trời. Để chống đỡ bầu trời, bà chặt **bốn chân của con rùa thần "
            "khổng lồ** dựng thành bốn cây cột ở bốn phương. Bà lại giết **con rồng đen ở Ký Châu**, đuổi sạch thú dữ; "
            "rồi gom *cỏ lau, lau lách* đốt thành tro, dùng tro lấp những chỗ trũng, ngăn dòng nước lũ.",
            "Trời lại được vá lành, đất đai bằng phẳng, mùa màng tốt tươi, con người và muôn vật được hồi sinh. "
            "Nữ Oa kiệt sức nhưng mỉm cười nhìn thế gian trở về yên vui. Từ đó, người đời đời nhớ ơn nữ thần "
            "đã một tay cứu vớt loài người.",
        ])

    # ------------------------------------------------ phân tích
    doc.h2("3.4. Phân tích mẫu ngữ liệu theo từng trục kiến thức")

    doc.h3("① Thể loại, đề tài, thời gian – không gian")
    doc.bullets([
        "**Thể loại:** truyện *thần thoại suy nguyên* (có yếu tố thần thoại cứu thế/sáng tạo) của Trung Hoa. "
        "Truyện vừa giải thích tưởng tượng về cấu trúc vũ trụ (vòm trời có cột chống), vừa kể một thần linh cứu nhân loại.",
        "**Đề tài:** cuộc chiến chống tai ương vũ trụ và khát vọng bảo vệ sự sống, cứu vớt con người.",
        "**Thời gian:** thời khởi nguyên, *sau khi Nữ Oa tạo ra loài người* – thời gian thần thoại, không có năm tháng cụ thể.",
        "**Không gian:** tầm vũ trụ – vòm trời có lỗ thủng, cột chống trời, **núi Bất Chu** (tây bắc), **Ký Châu**, "
        "bốn phương tứ cực; không gian vừa cụ thể (địa danh) vừa thần kì (thiên – địa giao nhau).",
    ])

    doc.h3("② Hệ thống nhân vật")
    doc.data_table(
        ["Nhân vật", "Bản chất / vai trò", "Ý nghĩa biểu tượng"],
        [
            ["Nữ Oa", "Nữ thần vừa nặn đất tạo người, vừa vá trời cứu thế; hành động dứt khoát, bền bỉ, vị tha.",
             "Hình tượng người mẹ vĩ đại; lòng nhân ái, trách nhiệm, trí tuệ và tinh thần hi sinh vì cộng đồng."],
            ["Cung Công – Chúc Dung", "Thuỷ thần và hoả thần đánh nhau; Cung Công thua nên húc gãy cột trời, gây hoạ.",
             "Hiện thân các lực lượng tự nhiên đối kháng; sự hỗn loạn, tai ương khách quan đe doạ con người."],
            ["Rùa thần, rồng đen, thú dữ", "Rùa hiến chân làm cột chống trời; rồng đen, thú dữ bị tiêu diệt/đuổi đi.",
             "Vật liệu & chướng ngại trong công cuộc cứu thế; chiến thắng của cái thiện, trật tự trở lại."],
        ],
        widths=[34, 76, 66], size=8.5)

    doc.h3("③ Cốt truyện và các chi tiết tiêu biểu")
    doc.para("Cốt truyện đơn giản, tuyến tính, gồm ba chặng:")
    doc.numbered([
        "**Tai hoạ ập xuống:** cột chống trời gãy → trời thủng, đất nứt, lửa – nước – thú dữ vây hãm con người.",
        "**Nữ Oa ra tay cứu thế với bốn hành động:** (1) luyện **đá ngũ sắc** vá trời; (2) chặt **bốn chân rùa thần** "
        "làm cột chống trời tứ phương; (3) giết **rồng đen ở Ký Châu**, đuổi thú dữ; (4) đốt **lau lách thành tro** ngăn lũ.",
        "**Thế giới hồi sinh:** trời lành, đất bằng, muôn loài an cư; Nữ Oa được đời đời ghi ơn.",
    ])
    doc.box("memory", [
        "**Nhớ nhanh 4 việc Nữ Oa làm bằng câu đếm:** “**Luyện đá – Chống cột – Diệt long – Chặn lũ**”. "
        "Bốn chi tiết kì ảo này chính là “mỏ vàng” cho cả câu trắc nghiệm lẫn câu tự luận phân tích.",
    ])

    doc.h3("④ Lời người kể chuyện và lời nhân vật")
    doc.bullets([
        "Truyện chủ yếu dùng **lời người kể chuyện ở ngôi thứ ba, toàn tri**: người kể biết hết hành động lẫn tâm trạng "
        "(“Nữ Oa vô cùng đau xót”, “mỉm cười nhìn thế gian”), bao quát cả trời lẫn đất.",
        "Giọng kể **trang trọng, thành kính, ngợi ca**, thể hiện thái độ biết ơn của cộng đồng với vị nữ thần cứu thế.",
        "Tác dụng: tạo độ tin cậy, thiêng liêng; giúp tái hiện hiện trường vũ trụ rộng lớn mà một nhân vật hữu hạn không thể bao quát.",
    ])

    doc.h3("⑤ Chủ đề, tư tưởng, thông điệp")
    doc.bullets([
        "**Chủ đề:** cuộc đấu tranh của con người (thông qua hình tượng nữ thần) để chinh phục tự nhiên, chế ngự tai ương, "
        "bảo vệ sự sống và lập lại trật tự thế giới.",
        "**Thông điệp 1 – Trách nhiệm và lòng nhân ái:** khi cộng đồng lâm nạn, cần biết đứng ra gánh vác sứ mệnh, "
        "dám hi sinh vì mọi người.",
        "**Thông điệp 2 – Sức mạnh của trí tuệ và lao động:** Nữ Oa chiến thắng không bằng vũ khí mà bằng sự mưu trí, cần cù, "
        "biết tận dụng vật chất tự nhiên (đá, chân rùa, tro lau).",
        "**Thông điệp 3 – Khát vọng và niềm tin:** con người luôn khao khát chinh phục tự nhiên, tin vào chiến thắng tất yếu "
        "của sự sống, cái thiện trước hủy diệt, cái ác.",
        "**Thông điệp 4 – Hình tượng người mẹ:** Nữ Oa vừa *sinh thành* (nặn người) vừa *cứu rỗi* (vá trời), "
        "tiêu biểu cho tình mẹ bao la và vai trò sáng tạo của người phụ nữ.",
    ])

    doc.h3("⑥ Đặc sắc nghệ thuật và giá trị")
    doc.bullets([
        "**Tưởng tượng phóng đại, thần thánh hoá, nhân hoá** các lực lượng tự nhiên (thuỷ thần, hoả thần, rùa thần, rồng).",
        "**Yếu tố kì ảo, hoang đường** đậm đặc (luyện đá vá trời, chân rùa làm cột) nhưng gắn với cách giải thích thế giới hợp logic riêng.",
        "Kết cấu ba phần chặt chẽ; nghệ thuật **liệt kê, điệp cấu trúc** qua bốn hành động; ngôn ngữ trang trọng, giàu hình ảnh, biểu tượng.",
        "**Giá trị:** nhận thức (quan niệm vũ trụ sơ khai), giáo dục (trách nhiệm, lòng nhân ái, dũng cảm), thẩm mĩ "
        "(hình tượng nữ thần kì vĩ) và văn hoá (Nữ Oa là biểu tượng quan trọng trong văn minh Trung Hoa và văn minh Đông Á).",
    ])

    # ------------------------------------------------ vận dụng
    doc.h2("3.5. Câu hỏi Vận dụng mẫu (luyện cho câu 10 trong đề)")
    doc.tl_question("VD", "VẬN DỤNG CAO",
        "Truyện *Nữ Oa vá trời* gợi cho em bài học gì về trách nhiệm của mỗi cá nhân trước cộng đồng? "
        "Hãy liên hệ với những con người “vá trời” trong cuộc sống hôm nay.")
    doc.h3("Gợi ý triển khai (đủ ý để đạt điểm tối đa)")
    doc.bullets([
        "**Bài học rút ra:** khi cộng đồng gặp hoạn nạn, không thể thờ ơ; mỗi người cần biết đặt lợi ích chung lên trên, "
        "dám đứng ra gánh vác việc khó, dùng trí tuệ và sự bền bỉ để vượt qua thử thách (như Nữ Oa một mình gánh bốn việc lớn).",
        "**Liên hệ đời sống:** những “Nữ Oa thời bình” là lính cứu hoả lao vào biển lửa, bộ đội, y bác sĩ giữa đại dịch, "
        "người dân và chính quyền chống bão lũ, nhà khoa học ứng phó biến đổi khí hậu, thầy cô lặng lẽ “vá” những khoảng trống tri thức…",
        "**Quan điểm cá nhân:** em đồng tình sâu sắc; với riêng em, “vá trời” bắt đầu từ những việc nhỏ: giúp đỡ bạn khó khăn, "
        "giữ gìn môi trường, có tinh thần phục vụ, sẵn sàng nhận phần việc chung thay vì đổ lỗi hay trốn tránh.",
    ])
    doc.box("warn", [
        "**Lỗi dễ mất điểm ở câu Vận dụng:** chỉ kể lại truyện hoặc nêu khẩu hiệu chung chung mà *không có liên hệ cụ thể* "
        "và *không bày tỏ quan điểm riêng*. Luôn đảm bảo bộ ba: **BÀI HỌC → LIÊN HỆ THỰC TẾ → HÀNH ĐỘNG CỦA EM**.",
    ])
