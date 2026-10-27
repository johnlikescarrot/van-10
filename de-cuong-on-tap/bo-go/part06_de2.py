# -*- coding: utf-8 -*-
"""Phần 5 (2/2): Đề minh họa số 2 — Lạc Long Quân – Âu Cơ — + ngân hàng lí thuyết."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)
from reading_texts import LAC_LONG


def build(doc):
    doc.add_page()
    doc.h2("5.3. ĐỀ MINH HOẠ SỐ 2 — NGỮ LIỆU “LẠC LONG QUÂN – ÂU CƠ”")
    doc.reading_card("ĐỌC HIỂU (6,0 điểm) — Ngữ liệu ngoài SGK",
                     "Lạc Long Quân – Âu Cơ (Con Rồng cháu Tiên)",
                     "Theo Lĩnh Nam chích quái (thuật lại)", LAC_LONG)

    doc.h3("Phần I. Trắc nghiệm (4,0 điểm — mỗi câu 0,5 điểm)")
    doc.mcq(1, "NHẬN BIẾT", "Truyện *Lạc Long Quân – Âu Cơ* thuộc nhóm thần thoại nào?",
            ["Thần thoại sáng tạo (anh hùng văn hoá)",
             "Thần thoại suy nguyên giải thích hiện tượng tự nhiên",
             "Thần thoại nguồn gốc dân tộc",
             "Thần thoại về các vị thần sáng tạo vũ trụ"])
    doc.mcq(2, "NHẬN BIẾT", "Lạc Long Quân và Âu Cơ được giới thiệu cùng thuộc dòng dõi thần linh nào?",
            ["Dòng dõi Thần Nông", "Dòng dõi Thần Trụ Trời", "Dòng dõi Ngọc Hoàng", "Dòng dõi thần Biển"])
    doc.mcq(3, "NHẬN BIẾT", "Sự kiện kì ảo nào xảy ra sau khi Lạc Long Quân và Âu Cơ kết duyên?",
            ["Âu Cơ sinh ra một cái bọc chứa trăm trứng, nở thành trăm người con trai",
             "Hai người cùng nhau dựng thành Phong Châu trong một đêm",
             "Một góc trời bị sụp do gãy cột chống",
             "Rồng đen xuất hiện gây ra thuỷ tai"])
    doc.mcq(4, "NHẬN BIẾT", "Vì sao Lạc Long Quân và Âu Cơ lại chia nhau các con?",
            ["Vì hai người xảy ra xung đột, cãi nhau",
             "Vì khác nết: Rồng thường ở thuỷ phủ, Tiên quen non cao, khó sum họp dài lâu",
             "Vì có chiến tranh giữa các bộ tộc",
             "Vì các người con chủ động đòi đi khai hoang"])
    doc.mcq(5, "NHẬN BIẾT", "Người con trưởng ở lại Phong Châu xưng hiệu gì và lập ra nước nào?",
            ["An Dương Vương, nước Âu Lạc", "Hùng Vương, nước Văn Lang",
             "Kinh Dương Vương, nước Xích Quỷ", "Thục Phán, thành Cổ Loa"])
    doc.mcq(6, "NHẬN BIẾT", "Chi tiết “năm mươi con theo mẹ lên núi, năm mươi con theo cha về biển” gắn với ý niệm nào?",
            ["Sự chia rẽ, phân tán của dân tộc",
             "Non – biển một nhà, thống nhất trong đa dạng",
             "Một cuộc di cư bắt buộc vì thiên tai",
             "Sự phân hoá giàu nghèo trong xã hội"])
    doc.mcq(7, "THÔNG HIỂU", "Tên gọi “con Rồng cháu Tiên” thể hiện điều gì trong ý thức của người Việt?",
            ["Một thói mê tín, dị đoan cần loại bỏ",
             "Ý thức về cội nguồn chung và niềm tự hào dân tộc",
             "Sự phụ thuộc hoàn toàn vào thần linh",
             "Quan niệm phân biệt đẳng cấp dòng giống"])
    doc.mcq(8, "THÔNG HIỂU", "Lời dặn “hễ có việc gì thì cứu giúp lẫn nhau” của Lạc Long Quân gợi bài học đạo đức gì?",
            ["Mỗi vùng miền nên sống tách biệt để giữ bản sắc",
             "Tinh thần tương thân tương ái, đoàn kết giúp đỡ nhau khi hoạn nạn",
             "Chọn nơi ở thuận tiện nhất cho cá nhân",
             "Không cần gắn bó với cộng đồng rộng lớn"])

    doc.h3("Phần II. Tự luận đọc hiểu (2,0 điểm)")
    doc.tl_question(9, "THÔNG HIỂU",
        "Phân tích ý nghĩa biểu tượng của cặp hình tượng Rồng – Tiên và chi tiết cái bọc trăm trứng trong truyện.")
    doc.tl_question(10, "VẬN DỤNG",
        "Truyện *Lạc Long Quân – Âu Cơ* gợi cho em suy nghĩ gì về truyền thống đại đoàn kết dân tộc trong cuộc sống hôm nay? "
        "Trách nhiệm của riêng em là gì?")

    doc.h3("Phần III. Viết (4,0 điểm)")
    doc.tl_question(11, "VIẾT — BIẾT/HIỂU/VẬN DỤNG",
        "Viết bài văn nghị luận phân tích, đánh giá tác phẩm truyện *Lạc Long Quân – Âu Cơ* "
        "(làm rõ nội dung, nét đặc sắc nghệ thuật, chủ đề và bài học về cội nguồn, đoàn kết dân tộc).")

    # ============================================================ ĐÁP ÁN ĐỀ 2
    doc.h2("5.4. ĐÁP ÁN VÀ GIẢI CHI TIẾT ĐỀ SỐ 2")
    doc.data_table(["Câu", "1", "2", "3", "4", "5", "6", "7", "8"],
                   [["Đáp án", "C", "A", "A", "B", "B", "B", "B", "B"]],
                   widths=[28] + [18.5] * 8, size=9.5)
    doc.h3("Giải thích chi tiết")
    doc.numbered([
        "**Đáp án C — Thần thoại nguồn gốc dân tộc.** Truyện giải thích nguồn gốc tổ tiên, danh hiệu cộng đồng "
        "(con Rồng cháu Tiên), gắn với việc dựng nước Văn Lang.",
        "**Đáp án A.** Cả Kinh Dương Vương (cha Lạc Long Quân) lẫn Đế Lai (cha Âu Cơ) đều được kể là dòng dõi Thần Nông — "
        "cách truyện cổ tạo sự đồng nguồn cho cộng đồng.",
        "**Đáp án A.** Bọc trăm trứng nở trăm con là chi tiết kì ảo trung tâm, biểu tượng sự đồng nguồn, đông đúc, thuần nhất.",
        "**Đáp án B.** Lạc Long Quân tự nêu lí do khác nết (Rồng – thuỷ phủ, Tiên – non cao); đây không phải mâu thuẫn mà là "
        "cách phân bố không gian sinh tồn núi – biển.",
        "**Đáp án B.** Con trưởng ở Phong Châu xưng Hùng Vương, lập nước Văn Lang, truyền 18 đời — mốc huyền sử mở đầu lịch sử dân tộc.",
        "**Đáp án B.** Sự phân chia 50 – 50 cùng lời hẹn cứu giúp nhau khẳng định non – biển là hai nhánh của một cộng đồng, "
        "thống nhất trong đa dạng.",
        "**Đáp án B.** Danh hiệu tự gọi thể hiện ý thức chung về cội nguồn và niềm tự hào, tự tôn dân tộc, không phải mê tín hay đẳng cấp.",
        "**Đáp án B.** Lời dặn tổ tiên là khuôn vàng thước ngọc về tình tương thân tương ái, đoàn kết khi gặp việc lớn, hoạn nạn.",
    ])
    doc.h3("Gợi ý đáp án câu tự luận")
    doc.data_table(["Câu", "Các ý cần đạt", "Điểm"],
        [
            ["9", "• Rồng (Lạc Long Quân): biểu tượng sức mạnh bản địa phía Nam, gắn biển, thuỷ phủ, người cha dân tộc.\n"
                  "• Tiên (Âu Cơ): gắn non cao, nông nghiệp, sự sinh thành, người mẹ dân tộc.\n"
                  "• Bọc trăm trứng: mọi người Việt cùng một cội nguồn, bình đẳng, đoàn kết máu thịt.\n"
                  "→ Hình tượng hoà trộn yếu tố kì ảo và dấu vết lịch sử, thể hiện quan niệm về tổ tiên và non sông thống nhất.",
             "1,0"],
            ["10", "• Nêu được ý nghĩa: đại đoàn kết toàn dân, các dân tộc anh em, đồng bào – kiều bào là sức mạnh vượt qua "
                  "thiên tai, dịch bệnh, ngoại xâm (0,5đ).\n"
                  "• Liên hệ và trách nhiệm bản thân cụ thể: tôn trọng khác biệt vùng miền, giúp đỡ bạn bè, không chia rẽ, "
                  "học tập xây dựng quê hương (0,5đ).",
             "1,0"],
        ], widths=[14, 138, 24], size=8.4)

    # ============================================================ NGÂN HÀNG LÍ THUYẾT
    doc.h2("5.5. Ngân hàng 12 câu trắc nghiệm lí thuyết thể loại (không phụ thuộc ngữ liệu)")
    doc.para(
        "Đề thi có thể dành vài câu hỏi cho tri thức thể loại chung. Bộ câu này giúp bạn “phủ” mọi khả năng; "
        "tự làm trước rồi đối chiếu đáp án ở cuối.", family="sans")
    doc.mcq(1, "NHẬN BIẾT", "Đặc điểm nổi bật nhất về thời gian trong truyện thần thoại là gì?",
            ["Thời gian lịch sử cụ thể, có năm tháng rõ ràng",
             "Thời gian khởi nguyên, hồng hoang, gắn quá trình hình thành thế giới",
             "Thời gian hiện đại, gắn máy móc công nghiệp",
             "Thời gian ước lệ “ngày xưa” như truyện cổ tích"])
    doc.mcq(2, "NHẬN BIẾT", "Nhân vật chính trong truyện thần thoại chủ yếu là ai?",
            ["Người nông dân lao động bình thường", "Thần linh, người khổng lồ, tổ tiên thần kì",
             "Anh hùng lịch sử có thật", "Con vật nuôi trong gia đình"])
    doc.mcq(3, "NHẬN BIẾT", "Mục đích cốt lõi của truyện thần thoại là gì?",
            ["Giải trí, mua vui sau giờ lao động",
             "Giải thích nguồn gốc thế giới, muôn loài, hiện tượng tự nhiên và cội nguồn cộng đồng",
             "Ghi chép chính xác các sự kiện lịch sử",
             "Phê phán trực tiếp chế độ phong kiến"])
    doc.mcq(4, "NHẬN BIẾT", "“Tính nguyên hợp” trong thần thoại nghĩa là gì?",
            ["Sự hoà trộn nghệ thuật, tôn giáo, triết học, lịch sử, tri thức sơ khai trong một thể thống nhất",
             "Sự trùng lặp y nguyên các motip trong nhiều truyện",
             "Việc dùng duy nhất một loại nhân vật",
             "Cách kể chỉ có một người kể"])
    doc.mcq(5, "NHẬN BIẾT", "Truyện nào sau đây thuộc thể loại thần thoại đã học trong SGK KNTT 10?",
            ["*Tản Viên từ Phán sự lục*", "*Thần Sét*", "*Chữ người tử tù*", "*Héc-to từ biệt Ăng-đrô-mác*"])
    doc.mcq(6, "NHẬN BIẾT", "Thần thoại về các vị thần dạy nghề, diệt yêu quái, lập trật tự thuộc nhóm nào?",
            ["Thần thoại suy nguyên", "Thần thoại sáng tạo (anh hùng văn hoá)",
             "Thần thoại nguồn gốc dân tộc", "Truyền thuyết địa danh"])
    doc.mcq(7, "THÔNG HIỂU", "Vì sao nhân vật thần thoại thường được gọi theo chức năng (Thần Trụ Trời, Thần Sét, Thần Gió)?",
            ["Vì người nguyên thủy quên đặt tên riêng",
             "Vì tên gọi gắn trực tiếp với vai trò giải thích một hiện tượng/lực lượng tự nhiên",
             "Vì các thần không được phép có tên riêng",
             "Vì để tránh trùng tên với người thường"])
    doc.mcq(8, "THÔNG HIỂU", "Điểm khác biệt căn bản giữa thần thoại và sử thi là gì?",
            ["Thần thoại có nhân vật thần linh, giải thích nguồn gốc; sử thi lấy anh hùng cộng đồng và chiến công làm trung tâm",
             "Thần thoại dài hơn sử thi",
             "Sử thi có yếu tố kì ảo còn thần thoại thì không",
             "Thần thoại chỉ có ở phương Đông"])
    doc.mcq(9, "THÔNG HIỂU", "Tác dụng chính của việc dùng ngôi kể thứ ba toàn tri trong thần thoại là gì?",
            ["Làm câu chuyện trở nên bí mật, khó hiểu",
             "Giúp người kể bao quát cả vũ trụ, quá trình khai sinh thế giới, tạo giọng điệu khách quan, thiêng liêng",
             "Để giấu bớt thông tin với người đọc",
             "Phản ánh giới hạn nhận biết của con người"])
    doc.mcq(10, "THÔNG HIỂU", "Chi tiết kì ảo trong thần thoại (luyện đá vá trời, bọc trăm trứng) có vai trò gì?",
            ["Chỉ để gây giật gân, hấp dẫn",
             "Hình tượng hoá cách giải thích thế giới và khát vọng chinh phục tự nhiên của người cổ đại",
             "Chứng minh các sự kiện lịch sử là có thật",
             "Thể hiện sự xa rời đời sống hiện thực"])
    doc.mcq(11, "THÔNG HIỂU", "Phát biểu nào đúng nhất về giá trị giáo dục của thần thoại?",
            ["Không còn ý nghĩa trong đời sống hiện đại",
             "Bồi đắp lòng dũng cảm, tinh thần cộng đồng, trách nhiệm và ý thức cội nguồn",
             "Chỉ dạy các nghi lễ tôn giáo",
             "Chỉ phục vụ nhà nghiên cứu văn hoá"])
    doc.mcq(12, "VẬN DỤNG", "Khi gặp một truyện kể về vị thần khai sinh dòng sông, dùng trí tưởng tượng để giải thích vì sao sông chảy, "
            "em xếp truyện đó vào thể loại nào?",
            ["Truyện cười", "Thần thoại suy nguyên", "Truyện ngắn hiện thực", "Kịch bản chèo"])

    doc.h3("Đáp án ngân hàng lí thuyết")
    doc.data_table(["Câu", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                   [["Đáp án", "B", "B", "B", "A", "B", "B", "B", "A", "B", "B", "B", "B"]],
                   widths=[20] + [13] * 12, size=8.8)
    doc.box("memory", [
        "**Mẹo “tăng tốc” trắc nghiệm:** (1) Đọc trước câu hỏi để định hướng đọc ngữ liệu; (2) loại ngay phương án sai thể loại "
        "hoặc trái ngữ liệu; (3) cảnh giác từ tuyệt đối hoá (*chỉ, duy nhất, không bao giờ*); (4) với câu “vì sao/nhằm mục đích gì”, "
        "chọn phương án gắn với **chức năng thể loại** (giải thích thế giới, khát vọng chinh phục tự nhiên, giáo dục cộng đồng).",
    ])
