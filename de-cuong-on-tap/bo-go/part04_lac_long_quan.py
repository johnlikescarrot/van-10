# -*- coding: utf-8 -*-
"""Phần 4: Ngữ liệu Lạc Long Quân – Âu Cơ (thần thoại nguồn gốc dân tộc, ngoài SGK)."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)


def build(doc):
    doc.h1("PHẦN 4", "Ngữ liệu thứ hai: “Lạc Long Quân – Âu Cơ”")

    doc.para(
        "Nếu *Nữ Oa vá trời* đại diện cho thần thoại **suy nguyên – cứu thế**, thì *Lạc Long Quân – Âu Cơ* "
        "là mẫu mực của thần thoại **nguồn gốc dân tộc**. Truyện nằm trong bộ *Lĩnh Nam chích quái* "
        "(Trần Thế Pháp, thế kỉ XIV) và được nhắc lại trong *Đại Việt sử kí toàn thư* — "
        "nơi cội nguồn của tín ngưỡng **con Rồng cháu Tiên**.",
        family="sans")

    # ------------------------------------------------ ngữ liệu
    doc.h2("4.1. NGỮ LIỆU: LẠC LONG QUÂN – ÂU CƠ")
    doc.reading_card(
        "NGỮ LIỆU NGOÀI SGK — THẦN THOẠI NGUỒN GỐC VIỆT NAM",
        "Lạc Long Quân – Âu Cơ (Con Rồng cháu Tiên)",
        "Theo Lĩnh Nam chích quái (thuật lại)",
        [
            "Ngày xưa, **Kinh Dương Vương** lấy con gái thần hồ là Thần Long, sinh ra **Lạc Long Quân**, tên Sùng Lãm, "
            "vốn là giống Rồng, cai quản vùng Lạc Việt. Lạc Long Quân sức khỏe phi thường, thông hiểu thuỷ tính, "
            "dạy dân đánh cá, trồng trọt và cách phòng chống thuỷ quái.",
            "Bấy giờ **Đế Lai** dẫn con gái là **Âu Cơ** – một nàng tiên xinh đẹp, giỏi giang, thuộc dòng Thần Nông – "
            "đi tuần phương Nam. Lạc Long Quân gặp Âu Cơ, hai người đem lòng cảm mến rồi kết duyên. Chẳng bao lâu, "
            "Âu Cơ sinh ra **một cái bọc, trong bọc có trăm quả trứng, nở ra trăm người con trai**, ai cũng khôi ngô, khoẻ mạnh.",
            "Một thời gian sau, Lạc Long Quân vốn là loài Rồng thường dưới thuỷ phủ, còn Âu Cơ là tiên quen sống nơi non cao, "
            "tập quán khác nhau, khó sum họp dài lâu. Lạc Long Quân bèn nói với Âu Cơ: “*Ta là giống Rồng, nàng là giống Tiên, "
            "khó thể ở cùng nhau mãi được. Nay hãy chia các con, năm mươi người theo nàng lên núi, năm mươi người theo ta về biển, "
            "hễ có việc gì thì cứu giúp lẫn nhau*”.",
            "Trăm người con từ đó toả đi khắp non nước. Người con trưởng ở lại đất **Phong Châu**, được tôn làm vua, "
            "xưng là **Hùng Vương**, đặt tên nước là **Văn Lang**, nối ngôi truyền được mười tám đời. Người Việt từ đó "
            "vẫn tự hào gọi nhau là **con Rồng cháu Tiên**, cùng một bọc sinh ra.",
        ])

    # ------------------------------------------------ phân tích
    doc.h2("4.2. Phân tích ngữ liệu theo bộ khung thể loại")
    doc.h3("① Thể loại – đề tài – thời gian – không gian")
    doc.bullets([
        "**Thể loại:** *thần thoại nguồn gốc dân tộc*, nằm ở **ranh giới với truyền thuyết** vì đã gắn với nhân vật, "
        "địa danh, triều đại có dáng dấp lịch sử (Hùng Vương, nước Văn Lang, đất Phong Châu).",
        "**Đề tài:** nguồn gốc tổ tiên và sự hình thành cộng đồng người Việt; mối quan hệ gắn bó núi – biển, miền ngược – miền xuôi.",
        "**Thời gian:** thời dựng nước đầu tiên, một “thuở” huyền sử, mốc mở đầu của dòng lịch sử dân tộc (mười tám đời Hùng Vương).",
        "**Không gian:** vùng *Lạc Việt* phương Nam; cặp không gian biểu tượng **non cao – biển thẳm**, quy tụ về *Phong Châu*; "
        "không gian rộng cả nước, mang ý nghĩa lãnh thổ – cương vực.",
    ])

    doc.h3("② Nhân vật và chi tiết kì ảo tiêu biểu")
    doc.data_table(
        ["Yếu tố", "Đặc điểm", "Ý nghĩa biểu tượng"],
        [
            ["Lạc Long Quân", "Con Kinh Dương Vương, giống Rồng, sống nơi biển, dạy dân nghề, trị thuỷ quái.",
             "Sức mạnh bản địa phía Nam, người cha của dân tộc, gắn với biển và văn minh sông nước."],
            ["Âu Cơ", "Nàng tiên dòng Thần Nông, sống nơi non cao, sinh ra cái bọc trăm trứng.",
             "Người mẹ dân tộc, gắn với núi, nông nghiệp và sự sinh thành, nuôi dưỡng."],
            ["Cái bọc trăm trứng", "Một bọc nở trăm người con trai khôi ngô.",
             "Sự đồng nguồn, thuần nhất, đông đúc; mọi người Việt cùng một mẹ, một cội nguồn."],
            ["Chia con 50 – 50", "Năm mươi con lên núi, năm mươi con về biển, hẹn cứu giúp nhau.",
             "Tư thế non – biển một nhà, thống nhất trong đa dạng; lời hẹn tương thân tương ái."],
        ],
        widths=[34, 72, 70], size=8.5)

    doc.h3("③ Chủ đề, tư tưởng, thông điệp")
    doc.bullets([
        "**Giải thích nguồn gốc dân tộc:** người Việt có chung tổ tiên thần kì (Rồng – Tiên), nên tự gọi là *con Rồng cháu Tiên* "
        "— một cách tự xác định danh hiệu đầy tự hào.",
        "**Củng cố tinh thần đoàn kết cùng huyết thống:** “cùng một bọc sinh ra” nên mọi người cùng một dân tộc, "
        "phải yêu thương, đùm bọc, giúp đỡ nhau (lời hẹn *cứu giúp lẫn nhau*).",
        "**Tư tưởng non sông thống nhất:** núi và biển, miền ngược và miền xuôi là hai nhánh của một cộng đồng, "
        "không thể chia cắt; ý thức bảo vệ toàn vẹn lãnh thổ, cương vực.",
        "**Công ơn tổ tiên và ý thức tự tôn:** biết ơn các bậc tiền nhân dựng nước, tự hào về cội nguồn văn hiến.",
    ])

    doc.h3("④ Đặc sắc nghệ thuật & giá trị")
    doc.bullets([
        "**Yếu tố kì ảo, hoang đường** (kết duyên Rồng – Tiên, đẻ bọc trăm trứng) hòa quyện với dấu vết lịch sử (Hùng Vương, Văn Lang).",
        "**Hệ biểu tượng đậm đặc:** Rồng (biển, sức mạnh, bản địa), Tiên (núi, sinh thành), bọc trăm trứng (đoàn kết, đồng nguồn).",
        "Giọng kể trang trọng, thành kính; ngôn ngữ gần với sử ca, có lời thoại trực tiếp thể hiện lời răn dạy tổ tiên.",
        "**Giá trị:** là “tấm giấy khai sinh tinh thần” của dân tộc, nuôi dưỡng lòng yêu nước, tự hào dân tộc, tinh thần đại đoàn kết; "
        "là kho đề tài, hình tượng cho văn học nghệ thuật ngàn năm sau.",
    ])

    # ------------------------------------------------ ranh giới thể loại
    doc.h2("4.3. Làm rõ ranh giới: Thần thoại nguồn gốc và Truyền thuyết")
    doc.data_table(
        ["Bình diện", "Yếu tố thần thoại (mạnh)", "Yếu tố truyền thuyết (có mặt)"],
        [
            ["Nhân vật", "Rồng, Tiên, tổ tiên thần kì, đẻ bọc trăm trứng", "Vua Hùng, Kinh Dương Vương gắn mốc trị vì, dựng nước"],
            ["Sự kiện", "Kết duyên thần kì, sinh nở phi thường", "Lập nước Văn Lang, đóng đô Phong Châu, truyền 18 đời"],
            ["Mục đích", "Giải thích nguồn gốc cộng đồng bằng tưởng tượng", "Gắn với lịch sử, địa danh, tín ngưỡng thờ Hùng Vương"],
        ],
        widths=[30, 73, 73], size=8.6)
    doc.box("info", [
        "**Kết luận an toàn khi làm bài:** gọi *Lạc Long Quân – Âu Cơ* là **thần thoại nguồn gốc dân tộc** "
        "(cách gọi chính yếu, đúng tinh thần Bản đặc tả), đồng thời ghi chú truyện *mang yếu tố truyền thuyết* vì gắn với "
        "lịch sử dựng nước. Tránh gọi tuyệt đối là “cổ tích” (cổ tích không nhằm giải thích nguồn gốc dân tộc và thường hư cấu thuần túy).",
    ])

    # ------------------------------------------------ vận dụng
    doc.h2("4.4. Câu hỏi Vận dụng mẫu & hướng triển khai")
    doc.tl_question("VD", "VẬN DỤNG CAO",
        "Chi tiết cái bọc trăm trứng và lời dặn “hễ có việc gì thì cứu giúp lẫn nhau” trong truyện *Lạc Long Quân – Âu Cơ* "
        "có ý nghĩa như thế nào đối với truyền thống đoàn kết của dân tộc Việt Nam hôm nay?")
    doc.bullets([
        "**Giải mã biểu tượng:** bọc trăm trứng nở trăm con = mọi người Việt đồng một cội nguồn, bình đẳng và gắn bó máu thịt; "
        "lời dặn của Lạc Long Quân là “di chúc” về tình tương thân, tương ái.",
        "**Ý nghĩa hiện tại:** đoàn kết toàn dân, đoàn kết các dân tộc anh em, đồng bào trong nước và kiều bào; "
        "sức mạnh đại đoàn kết khi chống giặc ngoại xâm, khi ứng phó thiên tai, dịch bệnh, khi xây dựng và bảo vệ Tổ quốc.",
        "**Hành động của em:** tôn trọng, giúp đỡ bạn bè mọi vùng miền; không phân biệt, kích động chia rẽ; "
        "tự hào và giữ gìn bản sắc; học tập để góp sức xây dựng quê hương, đất nước.",
    ])
    doc.box("memory", [
        "**Cặp ngữ liệu nên học song hành:** *Nữ Oa vá trời* (thần thoại cứu thế – Trung Hoa) và *Lạc Long Quân – Âu Cơ* "
        "(thần thoại nguồn gốc – Việt Nam). Cả hai đều tôn vinh **trách nhiệm với cộng đồng và sự gắn bó máu thịt**, "
        "giúp bạn vừa luyện đọc hiểu, vừa có sẵn dẫn chứng liên hệ so sánh khi làm bài.",
    ])
