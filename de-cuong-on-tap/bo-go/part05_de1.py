# -*- coding: utf-8 -*-
"""Phần 5 (1/2): Đề minh họa số 1 — ngữ liệu Nữ Oa vá trời — đủ 11 câu + đáp án."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)
from reading_texts import NU_OA


def build(doc):
    doc.h1("PHẦN 5", "Bộ đề minh hoạ chuẩn ma trận — toàn bộ câu hỏi & đáp án")

    doc.para(
        "Phần này gồm **hai đề minh hoạ 11 câu** được dựng *đúng từng ô của Ma trận và Bản đặc tả* "
        "(8 câu trắc nghiệm + 2 câu tự luận đọc hiểu + 1 bài viết), mỗi đề có **đáp án và giải thích đầy đủ**. "
        "Hãy làm như một bài thi thật (bấm giờ 90 phút), sau đó mới đối chiếu phần giải chi tiết.")
    doc.box("info", [
        "**Thang điểm mỗi đề:** câu 1–8 trắc nghiệm: 0,5 điểm/câu (tổng 4,0đ → quy đổi 30% theo ma trận); "
        "câu 9, 10 tự luận: 1,0 điểm/câu; câu 11 viết: 4,0 điểm. Tổng 10 điểm. "
        "Cấp độ: 6 câu Nhận biết (1–6), 2 câu Thông hiểu (7–8), câu 9 Thông hiểu, câu 10 Vận dụng, câu 11 tích hợp cả ba cấp độ.",
    ])

    # ============================================================ ĐỀ 1
    doc.h2("5.1. ĐỀ MINH HOẠ SỐ 1 — NGỮ LIỆU “NỮ OA VÁ TRỜI”")
    doc.reading_card("ĐỌC HIỂU (6,0 điểm) — Ngữ liệu ngoài SGK",
                     "Nữ Oa vá trời",
                     "Thần thoại Trung Hoa (thuật lại theo truyện dân gian)", NU_OA)

    doc.h3("Phần I. Trắc nghiệm (4,0 điểm — mỗi câu 0,5 điểm)")
    doc.mcq(1, "NHẬN BIẾT", "Truyện *Nữ Oa vá trời* thuộc thể loại nào sau đây?",
            ["Sử thi", "Truyện thần thoại", "Truyền thuyết", "Truyện cổ tích"])
    doc.mcq(2, "NHẬN BIẾT", "Yếu tố nào thể hiện đặc điểm thời gian, không gian thần thoại trong truyện?",
            ["Thời Trần, kinh thành Thăng Long với các cung điện",
             "Thời khởi nguyên sau khi Nữ Oa tạo ra loài người; vòm trời có cột chống, núi Bất Chu, vùng Ký Châu",
             "Thời hiện đại với thành phố đông đúc, máy móc",
             "Thời phong kiến với làng mạc, đồng ruộng Việt Nam"])
    doc.mcq(3, "NHẬN BIẾT", "Nguyên nhân trực tiếp làm vòm trời xuất hiện lỗ thủng là gì?",
            ["Nữ Oa luyện đá làm nứt vỡ bầu trời",
             "Rồng đen cắn thủng vòm trời",
             "Cung Công thua trận, húc đầu vào núi Bất Chu làm gãy cột chống trời",
             "Chúc Dung dùng lửa thiêu đốt làm thủng trời"])
    doc.mcq(4, "NHẬN BIẾT", "Nhân vật nào sau đây KHÔNG xuất hiện trong truyện?",
            ["Cung Công", "Chúc Dung", "Thần Trụ Trời", "Rùa thần khổng lồ"])
    doc.mcq(5, "NHẬN BIẾT", "Nữ Oa dùng vật liệu nào để hàn gắn, vá các lỗ thủng trên vòm trời?",
            ["Đá ngũ sắc được nung chảy thành keo", "Vàng, bạc nung nóng chảy",
             "Đất sét trộn nước", "Gỗ của những cây thần"])
    doc.mcq(6, "NHẬN BIẾT", "Để chống đỡ bầu trời sau khi vá, Nữ Oa đã làm gì?",
            ["Đắp lại núi Bất Chu thành cột", "Chặt bốn chân rùa thần làm bốn cột chống ở bốn phương",
             "Dùng chính thân mình đội trời", "Nhờ các vị thần khác xây cột"])
    doc.mcq(7, "THÔNG HIỂU", "Chi tiết Nữ Oa đốt lau lách thành tro để ngăn dòng nước lũ chủ yếu gợi lên điều gì?",
            ["Một phép thuật thần linh mơ hồ, không thực tế",
             "Sự kết hợp trí tuệ, quan sát tự nhiên và lao động sáng tạo của con người thời cổ",
             "Tín ngưỡng thờ lửa của người nguyên thủy",
             "Sự bất lực, phó mặc của con người trước thiên nhiên"])
    doc.mcq(8, "THÔNG HIỂU", "Vì sao Nữ Oa được xem là hình tượng “người mẹ vĩ đại” trong truyện?",
            ["Vì bà là vị nữ thần quyền lực cai quản cả thiên giới",
             "Vì bà vừa nặn đất tạo ra con người, vừa xả thân cứu con người khỏi tai hoạ",
             "Vì bà sinh ra trăm người con trai",
             "Vì bà nắm quyền thưởng phạt thần linh"])

    doc.h3("Phần II. Tự luận đọc hiểu (2,0 điểm)")
    doc.tl_question(9, "THÔNG HIỂU",
        "Tóm tắt cốt truyện *Nữ Oa vá trời* (khoảng 6–8 câu); trong đó nêu một chi tiết tiêu biểu và lí giải ý nghĩa của chi tiết ấy.")
    doc.tl_question(10, "VẬN DỤNG",
        "Truyện gợi cho em thông điệp sâu sắc nhất về trách nhiệm của cá nhân trước cộng đồng là gì? "
        "Hãy liên hệ với những con người “vá trời” trong cuộc sống hôm nay.")

    doc.h3("Phần III. Viết (4,0 điểm)")
    doc.tl_question(11, "VIẾT — BIẾT/HIỂU/VẬN DỤNG",
        "Viết bài văn nghị luận phân tích, đánh giá tác phẩm truyện *Nữ Oa vá trời* "
        "(làm rõ nét đặc sắc về nội dung, hình thức nghệ thuật và chủ đề; nêu bài học, thể hiện quan điểm cá nhân).")

    # ============================================================ ĐÁP ÁN ĐỀ 1
    doc.h2("5.2. ĐÁP ÁN VÀ GIẢI CHI TIẾT ĐỀ SỐ 1")
    doc.h3("Bảng đáp án trắc nghiệm nhanh")
    doc.data_table(["Câu", "1", "2", "3", "4", "5", "6", "7", "8"],
                   [["Đáp án", "B", "B", "C", "C", "A", "B", "B", "B"]],
                   widths=[28] + [18.5] * 8, size=9.5)

    doc.h3("Giải thích chi tiết từng câu trắc nghiệm")
    doc.numbered([
        "**Đáp án B — Truyện thần thoại.** Vì truyện kể về các vị thần (Nữ Oa, Cung Công, Chúc Dung), sự kiện thời khởi nguyên, "
        "dùng yếu tố kì ảo để giải thích thế giới và thể hiện khát vọng chinh phục tự nhiên. Loại A (sử thi lấy anh hùng cộng đồng "
        "làm trung tâm), C (truyền thuyết gắn lịch sử – địa danh cụ thể), D (cổ tích hư cấu, thưởng thiện phạt ác, kết thúc có hậu).",
        "**Đáp án B.** Thời gian khởi nguyên, không gian vũ trụ có cột chống trời, núi Bất Chu, Ký Châu là dấu hiệu kinh điển của "
        "thời gian – không gian thần thoại. Các phương án còn lại gắn không gian, thời gian lịch sử/hiện đại.",
        "**Đáp án C.** Văn bản nêu rõ Cung Công thua trận, uất giận nên húc đầu vào núi Bất Chu làm gãy cột chống trời → trời thủng. "
        "Đây là sự kiện mở màn cho chuỗi tai hoạ.",
        "**Đáp án C — Thần Trụ Trời.** Đây là nhân vật trong thần thoại Việt Nam thuộc SGK (chùm *Truyện về các vị thần sáng tạo thế giới*), "
        "không có trong *Nữ Oa vá trời*. Các nhân vật A, B, D đều xuất hiện trong ngữ liệu.",
        "**Đáp án A.** Nữ Oa tìm đá ngũ sắc, nung chảy thành keo để vá trời. Đây là chi tiết kì ảo tiêu biểu, dễ nhớ nhất của truyện.",
        "**Đáp án B.** Bà chặt bốn chân rùa thần làm bốn cột chống ở tứ phương — chi tiết thể hiện trí tưởng tượng phóng đại và "
        "biểu tượng bốn cực vũ trụ.",
        "**Đáp án B — Thông hiểu ý nghĩa chi tiết.** Việc dùng tro lau lách ngăn lũ cho thấy người cổ đại quan sát, tận dụng vật liệu "
        "gần gũi để chế ngự tự nhiên; đó là trí tuệ và lao động sáng tạo, không phải sự phó mặc hay phép thuật mơ hồ.",
        "**Đáp án B.** Nữ Oa vừa *sinh thành* (nặn đất tạo người) vừa *cứu rỗi* (vá trời, diệt trừ tai hoạ), nên là biểu tượng người mẹ "
        "vĩ đại, bao dung và có trách nhiệm với “con cái” của mình.",
    ])

    doc.h3("Gợi ý đáp án câu tự luận (Câu 9 – 1,0 điểm)")
    doc.data_table(["Ý cần đạt", "Điểm"],
        [
            ["Tóm tắt đủ ba chặng: (1) Cung Công gãy cột chống trời → tai hoạ; (2) Nữ Oa lần lượt luyện đá ngũ sắc vá trời, "
             "chặt chân rùa làm cột, giết rồng đen, đốt tro ngăn lũ; (3) trời lành, đất bằng, muôn loài hồi sinh.", "0,5"],
            ["Nêu đúng một chi tiết tiêu biểu và giải thích ý nghĩa biểu tượng (vd: đá ngũ sắc → trí tuệ, lao động sáng tạo; "
             "chân rùa làm cột → sự vững bền, bốn cực vũ trụ; rồng đen → tai hoạ/cái ác bị chế ngự).", "0,5"],
        ], widths=[150, 26], size=8.8)
    doc.box("tip", [
        "**Mẫu tóm tắt đạt điểm:** *“Thuỷ thần Cung Công thua trận húc gãy cột chống trời khiến trần gian lâm hoạ. "
        "Thương loài người, nữ thần Nữ Oa luyện đá ngũ sắc vá trời, chặt chân rùa thần làm trụ, giết rồng đen, đốt tro ngăn lũ. "
        "Thế giới hồi sinh, con người được cứu vớt.”* — gọn, đủ sự kiện, đúng trình tự.",
    ])

    doc.h3("Gợi ý đáp án câu Vận dụng (Câu 10 – 1,0 điểm)")
    doc.data_table(["Ý cần đạt", "Điểm"],
        [
            ["Nêu rõ thông điệp: trách nhiệm gánh vác việc chung, lòng nhân ái, dám hi sinh vì cộng đồng; "
             "thắng lợi nhờ trí tuệ và sự bền bỉ chứ không chỉ nhờ sức mạnh.", "0,5"],
            ["Liên hệ cụ thể, thuyết phục: lính cứu hoả, bộ đội, y bác sĩ, người chống bão lũ, nhà khoa học ứng phó biến đổi khí hậu…; "
             "có quan điểm và hành động của bản thân.", "0,5"],
        ], widths=[150, 26], size=8.8)

    doc.h3("Định hướng cho câu Viết (Câu 11 – 4,0 điểm)")
    doc.bullets([
        "Xem **dàn ý chi tiết, quy trình và thang điểm** ở **Phần 6** và **bài văn mẫu hoàn chỉnh** ở **Phần 7**.",
        "Bài viết phải đủ ba phần (mở – thân – kết), phân tích cả *nội dung lẫn nghệ thuật*, có dẫn chứng từ ngữ liệu, "
        "có đánh giá và quan điểm cá nhân; tuyệt đối không chỉ kể lại truyện.",
    ])
