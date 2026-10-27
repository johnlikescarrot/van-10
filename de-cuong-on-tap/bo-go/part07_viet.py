# -*- coding: utf-8 -*-
"""Phần 6: Chuyên đề Viết — nghị luận phân tích, đánh giá tác phẩm truyện (thần thoại)."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)


def build(doc):
    doc.h1("PHẦN 6", "Chuyên đề Viết: nghị luận phân tích, đánh giá tác phẩm truyện")

    doc.para(
        "Câu viết chiếm **4,0/10 điểm** và là thước đo năng lực tư duy – diễn đạt. Phần này biến yêu cầu trừu tượng "
        "trong Bản đặc tả thành **quy trình thao tác cụ thể, có công thức, có dàn ý mẫu** để bạn viết chắc tay với bất kì "
        "tác phẩm thần thoại nào.")

    # ------------------------------------------------ bản chất
    doc.h2("6.1. Bản chất của dạng bài nghị luận phân tích, đánh giá tác phẩm truyện")
    doc.bullets([
        "**Phân tích:** chia tác phẩm thành các bộ phận (đề tài, chủ đề, nhân vật, cốt truyện, chi tiết, nghệ thuật, lời kể…) "
        "và xem xét chúng trong mối liên hệ để làm rõ đặc sắc, ý nghĩa.",
        "**Đánh giá:** nhận xét, bày tỏ quan điểm về giá trị (nội dung, nghệ thuật), mức độ hay – chưa hay, ý nghĩa với người đọc; "
        "có thể bày tỏ sự đồng tình/không đồng tình với thông điệp.",
        "**Nghị luận:** dùng *lí lẽ* và *dẫn chứng* để bảo vệ luận điểm, không phải kể lại truyện hay bộc lộ cảm xúc tuỳ tiện.",
        "Với tác phẩm *truyện (thần thoại)*, trọng tâm là: **đề tài – chủ đề – thông điệp, nhân vật, chi tiết tiêu biểu, "
        "đặc trưng thể loại và nghệ thuật kể chuyện, bài học cho hôm nay**.",
    ])
    doc.box("warn", [
        "**Khác biệt sống còn:** bài *tự sự* kể lại “chuyện gì xảy ra”; bài *nghị luận văn học* trả lời “tác phẩm *có giá trị gì*, "
        "*vì sao hay*, *nói lên điều gì* và *có ý nghĩa ra sao*”. Cứ kể lại truyện mà không phân tích, đánh giá là mất từ một nửa "
        "số điểm câu 11.",
    ])

    # ------------------------------------------------ yêu cầu 3 mức
    doc.h2("6.2. Yêu cầu theo ba cấp độ (đối chiếu Bản đặc tả)")
    doc.data_table(["Cấp độ", "Bạn phải thể hiện được", "Đặt ở đâu trong bài"],
        [
            ["BIẾT", "Giới thiệu đủ tên tác phẩm, tác giả/dân gian, thể loại, xuất xứ; khái quát nội dung.",
             "Chủ yếu ở MỞ BÀI và câu dẫn thân bài."],
            ["HIỂU", "Triển khai luận điểm; phân tích nội dung, nghệ thuật, chủ đề; kết hợp lí lẽ – dẫn chứng chặt chẽ; "
             "đúng cấu trúc, chính tả, ngữ pháp.", "THÂN BÀI (các đoạn văn nghị luận)."],
            ["VẬN DỤNG", "Nêu bài học; đồng tình/không đồng tình thông điệp; đánh giá giá trị; quan điểm cá tính, sáng tạo; "
             "liên hệ thực tế.", "Cuối thân bài và KẾT BÀI."],
        ], widths=[22, 108, 46], size=8.6)

    # ------------------------------------------------ cấu trúc
    doc.h2("6.3. Cấu trúc chuẩn ba phần và “công thức” viết từng đoạn")
    doc.h3("① Mở bài (khoảng 4–6 câu) — giới thiệu + nêu vấn đề")
    doc.numbered([
        "**Dẫn dắt:** nêu vị trí, sức hấp dẫn của thần thoại nói chung (1 câu).",
        "**Giới thiệu tác phẩm:** tên truyện, thể loại, nguồn gốc/xuất xứ, hoàn cảnh (1–2 câu).",
        "**Khái quát nội dung:** tóm tắt một câu về đề tài, ấn tượng chung (1 câu).",
        "**Nêu luận đề:** khẳng định sẽ phân tích, đánh giá những nét đặc sắc nội dung – nghệ thuật và chủ đề (1 câu).",
    ])
    doc.box("tip", [
        "**Câu mở bài “ăn điểm”:** *“Trong thế giới thần thoại nhân loại, những câu chuyện về các vị thần cứu thế luôn có sức sống "
        "kì diệu. Nữ Oa vá trời — thần thoại Trung Hoa — là một trong số đó: tác phẩm không chỉ giải thích tưởng tượng về vũ trụ mà "
        "còn dựng lên hình tượng người mẹ vĩ đại và khát vọng chinh phục tự nhiên của con người.”*",
    ])

    doc.h3("② Thân bài (3–5 đoạn) — mỗi đoạn một luận điểm")
    doc.para("Mỗi đoạn văn theo **công thức 4 thành phần**:")
    doc.data_table(["Thành phần", "Vai trò", "Ví dụ minh hoạ (Nữ Oa)"],
        [
            ["Câu chủ đề", "Nêu luận điểm của đoạn", "“Nữ Oa là hình tượng người mẹ vĩ đại được dựng lên qua các hành động cứu thế.”"],
            ["Lí lẽ", "Giải thích, triển khai luận điểm", "Người mẹ vừa sinh thành vừa che chở; hành động cứu người thể hiện trách nhiệm, lòng nhân ái."],
            ["Dẫn chứng", "Trích/thuật lại chi tiết tiêu biểu trong truyện",
             "Bà luyện đá ngũ sắc vá trời, chặt chân rùa làm trụ, giết rồng đen, đốt tro ngăn lũ; ‘vô cùng đau xót’, ‘mỉm cười’."],
            ["Phân tích – đánh giá", "Chỉ ra ý nghĩa, giá trị, liên hệ",
             "Bốn việc làm cho thấy trí tuệ, cần cù, dám hi sinh; hình tượng nâng cao vai trò người phụ nữ và tinh thần cộng đồng."],
        ], widths=[28, 52, 96], size=8.4)
    doc.para("Hệ thống luận điểm gợi ý cho bài phân tích một truyện thần thoại:")
    doc.bullets([
        "**Luận điểm 1 — Đề tài, cốt truyện và không gian – thời gian thần thoại** (thời khởi nguyên, không gian vũ trụ, cốt truyện cứu thế/khai sinh).",
        "**Luận điểm 2 — Nhân vật và chi tiết tiêu biểu** (đặc điểm, hành động, ý nghĩa biểu tượng).",
        "**Luận điểm 3 — Chủ đề, tư tưởng, thông điệp** (khát vọng chinh phục tự nhiên, trách nhiệm cộng đồng, cái thiện thắng cái ác…).",
        "**Luận điểm 4 — Đặc sắc nghệ thuật** (tưởng tượng phóng đại, yếu tố kì ảo, ngôi kể toàn tri, ngôn ngữ biểu tượng, kết cấu).",
        "**Luận điểm 5 — Đánh giá, liên hệ, quan điểm cá nhân** (giá trị lâu bền, bài học cho hôm nay, đồng tình với thông điệp).",
    ])

    doc.h3("③ Kết bài (khoảng 3–5 câu) — khái quát + nâng cấp")
    doc.numbered([
        "Khái quát lại giá trị nội dung và nghệ thuật nổi bật của tác phẩm (1–2 câu).",
        "Khẳng định chủ đề, thông điệp và sức sống lâu bền (1 câu).",
        "Nêu bài học, tác động với bản thân và liên hệ hiện tại; câu kết mở rộng, ấn tượng (1–2 câu).",
    ])

    # ------------------------------------------------ quy trình
    doc.h2("6.4. Quy trình 5 bước viết bài trong phòng thi (khoảng 50 phút)")
    doc.data_table(["Bước", "Thao tác", "Thời gian"],
        [
            ["1. Đọc – xác định", "Đọc kĩ đề, xác định thể loại, phạm vi yêu cầu (toàn tác phẩm hay một khía cạnh).", "3–5 phút"],
            ["2. Lập dàn ý", "Ghi nhanh luận điểm, lí lẽ, dẫn chứng theo khung mở – thân – kết.", "7–10 phút"],
            ["3. Viết thô", "Viết liền mạch, ưu tiên đủ ý, đúng cấu trúc; mỗi đoạn một luận điểm.", "25–30 phút"],
            ["4. Chỉnh sửa", "Kiểm tra chính tả, dùng từ, câu, liên kết; bổ sung dẫn chứng còn thiếu.", "5–7 phút"],
            ["5. Hoàn thiện", "Trình bày sạch đẹp, đoạn rõ ràng, chữ dễ đọc; kiểm tra thời gian.", "2–3 phút"],
        ], widths=[28, 118, 30], size=8.6)

    # ------------------------------------------------ dàn ý 2 truyện
    doc.h2("6.5. Dàn ý chi tiết vận dụng cho hai ngữ liệu")
    doc.h3("Dàn ý A — Phân tích, đánh giá truyện “Nữ Oa vá trời”")
    doc.bullets([
        "**Mở bài:** giới thiệu thần thoại Trung Hoa *Nữ Oa vá trời*; nêu luận đề: tác phẩm đặc sắc ở hình tượng nữ thần cứu thế, "
        "nghệ thuật kì ảo và thông điệp về trách nhiệm, khát vọng chinh phục tự nhiên.",
        "**Thân bài 1:** hoàn cảnh ra đời hành động cứu thế — cột chống trời gãy, trần gian lâm hoạ (không gian – thời gian thần thoại).",
        "**Thân bài 2:** bốn hành động “luyện đá – chống cột – diệt long – chặn lũ” → trí tuệ, cần cù, dũng cảm, lòng nhân ái; "
        "ý nghĩa biểu tượng từng chi tiết.",
        "**Thân bài 3:** chủ đề, thông điệp (người mẹ vĩ đại, cái thiện thắng tai ương, lao động sáng tạo chế ngự tự nhiên).",
        "**Thân bài 4:** đặc sắc nghệ thuật (tưởng tượng phóng đại, nhân hoá thần linh, ngôi kể toàn tri, kết cấu ba chặng, ngôn ngữ biểu tượng).",
        "**Thân bài 5:** đánh giá giá trị, liên hệ những người “vá trời” hôm nay; quan điểm cá nhân.",
        "**Kết bài:** khẳng định sức sống và bài học lâu bền của tác phẩm.",
    ])
    doc.h3("Dàn ý B — Phân tích, đánh giá truyện “Lạc Long Quân – Âu Cơ”")
    doc.bullets([
        "**Mở bài:** giới thiệu truyện trong *Lĩnh Nam chích quái*, thể thần thoại nguồn gốc; nêu luận đề về cội nguồn và đoàn kết dân tộc.",
        "**Thân bài 1:** cặp tổ tiên thần kì Rồng – Tiên và biểu tượng non – biển.",
        "**Thân bài 2:** chi tiết bọc trăm trứng và sự chia con 50 – 50; lời dặn tương thân tương ái.",
        "**Thân bài 3:** chủ đề nguồn gốc dân tộc, tư tưởng non sông thống nhất, ý thức “con Rồng cháu Tiên”.",
        "**Thân bài 4:** nghệ thuật hư trộn kì ảo – lịch sử, hệ biểu tượng, giọng kể thành kính.",
        "**Thân bài 5:** đánh giá, liên hệ truyền thống đại đoàn kết hôm nay; trách nhiệm của thế hệ trẻ.",
        "**Kết bài:** khẳng định ý nghĩa “tấm giấy khai sinh tinh thần” của dân tộc.",
    ])

    # ------------------------------------------------ lỗi
    doc.h2("6.6. Lỗi thường gặp và cách sửa")
    doc.data_table(["Lỗi thường gặp", "Hậu quả", "Cách khắc phục"],
        [
            ["Kể lại truyện thay vì phân tích", "Mất điểm nặng ở tầng Hiểu – Vận dụng",
             "Mỗi dẫn chứng phải theo sau bằng câu phân tích, đánh giá ý nghĩa."],
            ["Thiếu/ sai dẫn chứng", "Luận điểm thiếu sức thuyết phục",
             "Trích đúng chi tiết tiêu biểu (đá ngũ sắc, bọc trăm trứng…); không bịa chi tiết."],
            ["Luận điểm rời rạc, thiếu liên kết", "Bài lỏng lẻo, khó theo dõi",
             "Dùng câu chuyển ý, từ nối (trước hết, bên cạnh đó, hơn nữa, vì vậy, tóm lại…)."],
            ["Đánh giá chung chung, không quan điểm", "Mất điểm Vận dụng",
             "Nêu rõ đồng tình/không đồng tình; đánh giá cụ thể có căn cứ; liên hệ thực tế."],
            ["Nhầm thể loại", "Sai định hướng toàn bài",
             "Nhớ dấu hiệu: thần thoại hỏi ‘vì sao/nguồn gốc’, nhân vật thần, thời khởi nguyên."],
            ["Lỗi chính tả, dùng từ, ngữ pháp", "Trừ điểm trình bày",
             "Kiểm tra từ Hán Việt, dấu câu; viết câu đủ chủ – vị; đọc lại sau khi viết."],
        ], widths=[44, 44, 88], size=8.4)
    doc.box("memory", [
        "**Tủ từ nối “vàng” cho bài nghị luận:** *trước hết – bên cạnh đó – mặt khác – hơn nữa – không những… mà còn – "
        "điều này cho thấy – có thể thấy – xét cho cùng – tóm lại – vì vậy*. Lạm dụng từ nối cũng không tốt; dùng đúng chỗ, tiết chế.",
    ])
