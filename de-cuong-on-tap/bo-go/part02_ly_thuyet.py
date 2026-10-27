# -*- coding: utf-8 -*-
"""Phần 2: Lí thuyết chuyên sâu về truyện thần thoại (bộ khung dùng cho mọi ngữ liệu)."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)


def build(doc):
    doc.h1("PHẦN 2", "Lí thuyết chuyên sâu truyện thần thoại")

    doc.para(
        "Đây là **“bộ khung vạn năng”**: dù đề thi cho ngữ liệu thần thoại nào (Việt Nam, Hy Lạp, Trung Hoa…), "
        "bạn vẫn giải mã được bằng hệ thống khái niệm dưới đây. Hãy học theo cấu trúc "
        "*định nghĩa → phân loại → đặc trưng → giá trị → phân biệt thể loại*.",
        family="sans")

    # ------------------------------------------------ định nghĩa
    doc.h2("2.1. Định nghĩa truyện thần thoại")
    doc.box("info", [
        "**Truyện thần thoại** là loại truyện dân gian ra đời sớm nhất, kể về các vị thần và những sự kiện "
        "xảy ra vào *thời điểm khởi nguyên* (thời gian thần thoại), nhằm **giải thích nguồn gốc thế giới, "
        "muôn loài, con người, các hiện tượng tự nhiên và phong tục**, đồng thời thể hiện khát vọng chinh phục "
        "tự nhiên và ước mơ về sức mạnh, công lí của con người thời cổ đại.",
    ])
    doc.para(
        "Từ gốc *“thần thoại”* (tiếng Hy Lạp *mythos*) nghĩa là **lời kể thiêng liêng, truyện kể về thần**. "
        "Người nguyên thủy chưa có khoa học nên dùng trí tưởng tượng và niềm tin tín ngưỡng để lí giải thế giới xung quanh: "
        "vì sao có sấm sét, vì sao trời cao đất dày, vì sao người Việt xưng là *con Rồng cháu Tiên*… "
        "Mọi câu trả lời đều được hình tượng hoá thành các vị thần và truyện kể.")

    doc.h3("Vì sao thần thoại ra đời?")
    doc.bullets([
        "**Lí do nhận thức:** trình độ nhận thức còn thấp, con người bất lực trước tự nhiên, cần cách giải thích "
        "cho các hiện tượng bí ẩn (mưa gió, sấm chớp, lũ lụt, mặt trời mọc lặn…).",
        "**Lí do tín ngưỡng – tôn giáo:** niềm tin vào thế lực thần linh, thờ tự tổ tiên, vật tổ (totem).",
        "**Lí do tinh thần:** nhu cầu gửi gắm khát vọng chế ngự tự nhiên, bảo vệ cộng đồng, khẳng định giá trị con người.",
    ])

    # ------------------------------------------------ phân loại
    doc.h2("2.2. Phân loại thần thoại (3 nhóm cần nhớ)")
    doc.data_table(
        ["Nhóm thần thoại", "Đối tượng phản ánh", "Ví dụ tiêu biểu"],
        [
            ["1. Thần thoại suy nguyên\n(giải thích nguồn gốc)",
             "Lí giải nguồn gốc vũ trụ, trời đất, muôn loài, con người, các hiện tượng tự nhiên, phong tục, tập quán.",
             "Thần Trụ Trời, Thần Sét, Thần Gió (VN); Nữ Oa vá trời, Bàn Cổ khai thiên (Trung Hoa); Prô-mê-tê lấy lửa (Hy Lạp)."],
            ["2. Thần thoại sáng tạo\n(anh hùng văn hoá)",
             "Kể các thần/anh hùng dạy nghề, diệt yêu quái, sáng tạo ra văn hoá, lập trật tự cho thế giới.",
             "Thần Nông dạy trồng trọt; Tô Vũ, các thần dạy chữ, dạy dệt vải; Héc-quyn (Hércules) lập 12 kì công."],
            ["3. Thần thoại nguồn gốc dân tộc\n(giao thoa truyền thuyết)",
             "Kể về tổ tiên thần kì, nguồn gốc cộng đồng/dân tộc, gắn với ý thức cội nguồn.",
             "Lạc Long Quân – Âu Cơ (con Rồng cháu Tiên); truyện các bậc vua Hùng; thần thoại vật tổ các dân tộc thiểu số."],
        ],
        widths=[38, 70, 68], size=8.6)
    doc.box("tip", [
        "**Mẹo nhận diện:** cứ truyện nào nhằm **GIẢI THÍCH “vì sao/nguồn gốc”** một sự vật, hiện tượng, cộng đồng "
        "thì thuộc thần thoại suy nguyên/nguồn gốc; truyện kể nhân vật **DẠY NGHỀ, DIỆT YÊU, LẬP TRẬT TỰ** thì thuộc nhóm sáng tạo.",
    ])

    # ------------------------------------------------ đặc trưng
    doc.h2("2.3. Sáu đặc trưng cốt lõi của truyện thần thoại")

    doc.h3("① Thời gian và không gian thần thoại")
    doc.bullets([
        "**Thời gian thần thoại** là thời điểm *khởi nguyên, hồng hoang*: “thuở xửa thuở xưa”, “ngày mới khai thiên lập địa”, "
        "“trời đất còn hỗn độn”… — một thời gian chưa có lịch sử thành văn, gắn với quá trình hình thành thế giới.",
        "**Không gian thần thoại** mang tầm vũ trụ, rộng lớn và thần kì: trời – đất chưa phân, thiên giới – trần gian – thuỷ phủ, "
        "bốn cực tứ phương, núi Bất Chu chống trời, Ký Châu…; không gian vừa cụ thể vừa huyền ảo.",
        "Thời gian, không gian không đo bằng đơn vị thực (ngày, năm) mà bằng **trình tự sáng tạo thế giới** "
        "(trước hết có trời đất, rồi có muôn vật, rồi có con người…).",
    ])

    doc.h3("② Nhân vật thần thoại")
    doc.bullets([
        "Chủ yếu là **thần linh, người khổng lồ, loài vật thần, tổ tiên thần kì** (Rồng, Tiên); mang nhiều sức mạnh phi thường, "
        "hình dạng kì lạ (thần Gió không đầu, thần Trụ Trời thân thể khổng lồ…).",
        "Nhiều nhân vật **không có tên riêng cụ thể** mà được gọi theo *chức năng – vai trò*: Thần Trụ Trời, Thần Sét, Thần Gió, "
        "Thần Đếm Cát, Thần Đào Sông…",
        "Nhân vật thường là **hiện thân của các lực lượng tự nhiên** hoặc **biểu tượng cho ước mơ, phẩm chất của cộng đồng** "
        "(Nữ Oa biểu tượng lòng nhân ái, tinh thần cứu thế; Lạc Long Quân – Âu Cơ biểu tượng cội nguồn dân tộc).",
        "Được lí tưởng hoá, ít miêu tả tâm lí phức tạp như nhân vật văn học written (văn học viết sau này).",
    ])

    doc.h3("③ Cốt truyện, sự kiện, câu chuyện")
    doc.bullets([
        "Cốt truyện thường **đơn giản, tuyến tính**, xoay quanh các sự kiện lớn lao tầm vũ trụ: *khai thiên lập địa, tạo dựng muôn loài, "
        "vá trời chống lũ, diệt trừ tai ương, dạy nghề lập cư*…",
        "Giàu **yếu tố kì ảo, hoang đường, biến hoá thần kì**: luyện đá vá trời, đẻ bọc trăm trứng, húc gãy cột chống trời…",
        "Mỗi sự kiện thường gắn với việc **lí giải nguồn gốc một sự vật/hiện tượng** (sấm sét là tiếng quát của Thần Sét; "
        "gió bão là hơi thở của Thần Gió…).",
        "Kết cấu thường theo trình tự thời gian, có hiện tượng *lặp lại, công thức hoá* (số ba, số bốn, số trăm…).",
    ])

    doc.h3("④ Đề tài và chi tiết tiêu biểu")
    doc.bullets([
        "Đề tài lớn: **nguồn gốc vũ trụ – muôn loài – con người; nguồn gốc hiện tượng tự nhiên; nguồn gốc nghề nghiệp, phong tục, "
        "lễ hội; nguồn gốc dân tộc**.",
        "Chi tiết tiêu biểu mang tính biểu tượng: *cột chống trời, đá ngũ sắc, bọc trăm trứng, chân rùa thần, rồng đen, "
        "cây cột núi Bất Chu*… Học sinh cần chỉ ra được chi tiết và **lí giải ý nghĩa** của nó.",
    ])

    doc.h3("⑤ Lời người kể chuyện và lời nhân vật")
    doc.bullets([
        "**Lời người kể chuyện** (thường ở ngôi thứ ba, toàn tri): dẫn dắt, thuật lại sự việc, giới thiệu nhân vật, "
        "xen lẫn lời bình luận, giải thích; giọng điệu trang trọng, thành kính, ngợi ca.",
        "**Lời nhân vật:** đối thoại, độc thoại thể hiện hành động, tính cách (lời tuyên bố của thần, lời căn dặn tổ tiên…).",
        "Việc chọn **ngôi kể thứ ba toàn tri** giúp người kể bao quát được cả vũ trụ, cả quá trình khai sinh thế giới — "
        "phù hợp với tầm vóc thần thoại và tạo độ tin cậy, thiêng liêng cho câu chuyện.",
    ])

    doc.h3("⑥ Chủ đề, tư tưởng, thông điệp")
    doc.bullets([
        "Phản ánh **quan niệm vũ trụ sơ khai** và cách lí giải thế giới bằng tưởng tượng của người nguyên thủy.",
        "Thể hiện **khát vọng chinh phục tự nhiên, chế ngự tai ương, bảo vệ sự sống và cộng đồng**.",
        "Ca ngợi **lòng dũng cảm, tinh thần hi sinh, trách nhiệm với cộng đồng, trí tuệ và cần cù sáng tạo**.",
        "Gửi gắm niềm tin vào **cái thiện, công lí, sự chiến thắng của sự sống trước hủy diệt**; bồi đắp ý thức về cội nguồn.",
    ])

    # ------------------------------------------------ nghệ thuật
    doc.h2("2.4. Đặc trưng nghệ thuật & giá trị")
    doc.h3("a) Đặc trưng nghệ thuật")
    doc.bullets([
        "**Tính nguyên hợp (tổng hòa):** trong thần thoại hoà trộn yếu tố nghệ thuật, tôn giáo, triết học, lịch sử, khoa học sơ khai "
        "và tri thức dân gian — ranh giới các lĩnh vực chưa tách bạch.",
        "**Tưởng tượng phóng khoáng, phóng đại, nhân hoá, thần thánh hoá** các lực lượng tự nhiên.",
        "Sử dụng nhiều **yếu tố kì ảo, hoang đường, biểu tượng, điển tích**; ngôn ngữ mộc mạc, giàu hình ảnh.",
        "Kết cấu tự sự theo trình tự thời gian, có công thức lặp; giọng kể ngợi ca, trang trọng.",
    ])
    doc.h3("b) Giá trị của thần thoại")
    doc.data_table(
        ["Loại giá trị", "Biểu hiện cụ thể"],
        [
            ["Giá trị nhận thức", "Kho tri thức sơ khai, bách khoa thư của người cổ đại về vũ trụ, tự nhiên, con người, lịch sử, phong tục."],
            ["Giá trị giáo dục", "Bài học về lòng dũng cảm, hi sinh vì cộng đồng, tinh thần trách nhiệm, khát vọng sống đẹp, ý thức cội nguồn."],
            ["Giá trị thẩm mĩ", "Vẻ đẹp hồn nhiên, trí tưởng tượng bay bổng, hình tượng kì vĩ, cảm hứng ngợi ca con người và sự sống."],
            ["Giá trị văn học – văn hoá", "Là mảnh đất nuôi dưỡng sử thi, truyền thuyết, văn học viết sau này (cảm hứng, đề tài, hình tượng, điển tích)."],
        ],
        widths=[40, 136], size=9.0)

    # ------------------------------------------------ phân biệt
    doc.h2("2.5. Bảng phân biệt thần thoại với các thể loại gần giống (cực dễ thi)")
    doc.data_table(
        ["Tiêu chí", "Thần thoại", "Sử thi", "Truyền thuyết", "Cổ tích"],
        [
            ["Nhân vật chính", "Thần linh, tổ tiên thần kì", "Anh hùng mang yếu tố thần kì",
             "Người/anh hùng lịch sử được thần kì hoá", "Người thường, muông vật, nhân vật chức năng"],
            ["Thời gian", "Khởi nguyên, hồng hoang", "Thời cổ đại, gắn lịch sử bộ tộc/dân tộc",
             "Gắn mốc lịch sử, triều đại, địa danh", "Thời gian ước lệ “ngày xưa”, phi lịch sử"],
            ["Mục đích chính", "Giải thích nguồn gốc thế giới, hiện tượng, cội nguồn",
             "Ca ngợi chiến công, công cuộc dựng nước/giữ nước", "Giải thích địa danh, phong tục, sự kiện lịch sử",
             "Thể hiện ước mơ công lí, thưởng thiện phạt ác"],
            ["Yếu tố nổi bật", "Kì ảo, thiêng liêng, tín ngưỡng vũ trụ", "Hùng tráng, không khí cộng đồng, chiến trận",
             "Yếu tố lịch sử + tín ngưỡng thờ tự", "Kì ảo tưởng tượng, kết cấu số 3, kết thúc có hậu"],
            ["Ví dụ (KNTT 10)", "Thần Trụ Trời, Thần Sét, Thần Gió", "Héc-to từ biệt…, Đăm Săn…",
             "(liên hệ) Tản Viên, Thánh Gióng", "(liên hệ) Tấm Cám, Cây tre trăm đốt"],
        ],
        widths=[26, 38, 38, 38, 36], size=8.0)
    doc.box("warn", [
        "**Bẫy thường gặp:** nhiều bạn gộp chung *thần thoại – truyền thuyết – cổ tích*. Hãy nhớ câu chốt: "
        "**thần thoại hỏi “VÌ SAO có thế giới?”; truyền thuyết hỏi “ĐỊA DANH/sự kiện này từ đâu?”; "
        "cổ tích kể “ƯỚC MƠ công lí” và luôn *kết thúc có hậu*; sử thi hát “CHIẾN CÔNG của anh hùng cộng đồng”.**",
    ])

    # ------------------------------------------------ liên hệ SGK
    doc.h2("2.6. Hệ thống văn bản trong SGK KNTT 10 – Bài 1 (nền tảng đối chiếu)")
    doc.para(
        "Chùm *Truyện về các vị thần sáng tạo thế giới* (thần thoại Việt Nam, sưu tầm theo **Nguyễn Đổng Chi**, "
        "tác giả bộ *Lược truyện các truyện cổ tích Việt Nam* được tặng Giải thưởng Hồ Chí Minh) gồm ba truyện:")
    doc.data_table(
        ["Truyện", "Sự kiện chính", "Hiện tượng được lí giải"],
        [
            ["Thần Trụ Trời",
             "Một vị thần khổng lồ đào đất, đá đắp cột chống trời, đội tách trời – đất; sau phá cột, ném đất đá tạo núi, đảo, biển.",
             "Sự hình thành trời, đất, núi non, sông biển (khai thiên lập địa)."],
            ["Thần Sét (Thiên Lôi)",
             "Vị thần mặt mũi nanh ác, tiếng quát dữ dội, thay Ngọc Hoàng thi hành luật pháp ở hạ giới; nóng nảy nhưng sợ tiếng gà, sợ thần Cường Bạo.",
             "Nguồn gốc sấm sét; quan niệm về sự trừng phạt, công lí thần linh."],
            ["Thần Gió",
             "Vị thần hình dạng kì quặc (không đầu), hít vào thở ra tạo gió, phối hợp thần Mưa, thần Sét; gắn truyện đứa con bị đày.",
             "Nguồn gốc gió, lốc, bão và tập tính một số loài cây (ngải tướng quân)."],
        ],
        widths=[30, 96, 50], size=8.4)
    doc.para(
        "Ngoài ra, mục *Thực hành đọc* giới thiệu truyện **Tê-dê** (trích *Thần thoại Hy Lạp*, Ê-đi Ha-min-tơn kể). "
        "Hãy nắm chắc ba truyện này làm “mẫu chuẩn” để khi gặp ngữ liệu mới (như *Nữ Oa vá trời*, *Lạc Long Quân – Âu Cơ* "
        "trong Phần 3, Phần 4), bạn tự tin đối chiếu các đặc trưng thể loại.")

    doc.box("memory", [
        "**Từ Hán Việt trong bài (thường xuất hiện ở câu trắc nghiệm):** "
        "*khai thiên lập địa* (mở trời dựng đất), *hồng hoang* (thời cổ xưa hỗn độn), *vũ trụ*, *ngũ sắc* (năm màu), "
        "*thần thoại, sử thi, truyền thuyết, cổ tích, cốt truyện, nhân vật, đề tài, chủ đề, thông điệp, nghị luận*. "
        "Học đúng nghĩa Hán Việt để không chọn nhầm phương án.",
    ])

    # ------------------------------------------------ mind map
    doc.h2("2.7. Sơ đồ tư duy tổng hợp “Bản đồ thần thoại”")
    doc.tree([
        "# TRUYỆN THẦN THOẠI — truyện dân gian sớm nhất, kể về thần, giải thích nguồn gốc",
        "├─ 1. PHÂN LOẠI",
        "│   ├─ Suy nguyên: nguồn gốc vũ trụ, hiện tượng (Thần Trụ Trời, Nữ Oa vá trời)",
        "│   ├─ Sáng tạo: dạy nghề, diệt yêu, lập trật tự (Thần Nông, Héc-quyn)",
        "│   └─ Nguồn gốc dân tộc: tổ tiên thần kì (Lạc Long Quân – Âu Cơ)",
        "├─ 2. THỜI GIAN – KHÔNG GIAN: hồng hoang, khởi nguyên; vũ trụ, thiên – địa, tứ cực",
        "├─ 3. NHÂN VẬT: thần linh khổng lồ, phi thường; gọi theo chức năng; biểu tượng ước mơ cộng đồng",
        "├─ 4. CỐT TRUYỆN: đơn giản, tuyến tính; sự kiện tầm vũ trụ; giàu kì ảo, hoang đường",
        "├─ 5. LỜI KỂ: ngôi 3 toàn tri; lời người kể (trang trọng) + lời nhân vật (đối thoại)",
        "├─ 6. CHỦ ĐỀ – THÔNG ĐIỆP: khát vọng chinh phục tự nhiên, hi sinh, cứu đời, ý thức cội nguồn",
        "└─ 7. GIÁ TRỊ: nhận thức – giáo dục – thẩm mĩ – nuôi dưỡng văn học sau này",
    ])
