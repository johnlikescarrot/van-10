# -*- coding: utf-8 -*-
"""Phần 8: Sổ tay ghi nhớ tối ưu, flashcard, kế hoạch 7 ngày, chiến thuật phòng thi."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)


def build(doc):
    doc.h1("PHẦN 8", "Sổ tay ghi nhớ tối ưu & lộ trình về đích")

    doc.para(
        "Phần cuối biến toàn bộ kiến thức trên thành **hệ thống ghi nhớ dài hạn** và **kế hoạch hành động cụ thể**. "
        "Học đúng phương pháp sẽ giúp bạn nhớ lâu hơn mà tốn ít thời gian hơn.", family="sans")

    # ------------------------------------------------ nguyên tắc ghi nhớ
    doc.h2("8.1. Bốn nguyên tắc ghi nhớ khoa học")
    doc.numbered([
        "**Chủ động gợi nhớ (Active Recall):** thay vì đọc lại nhiều lần, hãy *tự hỏi – tự trả lời*. "
        "Đóng tài liệu, viết ra những gì nhớ được; chỗ nào quên mới xem lại. Đây là cách hiệu quả nhất để đưa kiến thức vào trí nhớ dài hạn.",
        "**Lặp lại ngắt quãng (Spaced Repetition):** ôn lại sau 1 ngày – 3 ngày – 7 ngày. "
        "Mỗi lần ôn đúng thời điểm sắp quên sẽ gia cố trí nhớ mạnh gấp nhiều lần lần đọc liền mạch.",
        "**Sơ đồ hoá & kể chuyện:** gắn kiến thức rời rạc vào *sơ đồ tư duy* và *câu chuyện* "
        "(nhớ Nữ Oa qua 4 việc “luyện đá – chống cột – diệt long – chặn lũ”). Não nhớ hình ảnh và câu chuyện tốt hơn định nghĩa khô khan.",
        "**Học bằng tay:** vừa đọc vừa *viết tóm tắt, vẽ mind map, tự đặt câu hỏi*. "
        "Kiến thức được viết ra bằng tay có tỉ lệ giữ lại cao hơn hẳn việc chỉ đọc thụ động.",
    ])
    doc.box("tip", [
        "**Quy trình mỗi buổi học 45 phút:** 5 phút xem lại bài cũ (gợi nhớ) → 25 phút học nội dung mới → "
        "10 phút tự kiểm tra bằng flashcard/câu hỏi → 5 phút ghi chú chỗ yếu cần ôn lại. Kết thúc bằng một lượt kể lại bằng miệng.",
    ])

    # ------------------------------------------------ bảng tra nhanh
    doc.h2("8.2. Bảng tra nhanh “từ khoá vàng” trước giờ thi")
    doc.data_table(["Khái niệm", "Chốt ghi nhớ tức thì"],
        [
            ["Thần thoại", "Truyện dân gian sớm nhất, kể về THẦN, thời KHỞI NGUYÊN, giải thích NGUỒN GỐC thế giới."],
            ["3 nhóm thần thoại", "Suy nguyên (giải thích) – Sáng tạo (dạy nghề, diệt yêu) – Nguồn gốc dân tộc (tổ tiên)."],
            ["Thời gian – không gian", "Hồng hoang, khởi nguyên; vũ trụ, thiên – địa, tứ cực, núi chống trời."],
            ["Nhân vật", "Thần linh khổng lồ, phi thường; thường gọi theo CHỨC NĂNG; biểu tượng ước mơ cộng đồng."],
            ["Cốt truyện", "Đơn giản, tuyến tính; sự kiện tầm vũ trụ; nhiều kì ảo, hoang đường."],
            ["Ngôi kể", "Ngôi thứ ba TOÀN TRI; giọng trang trọng, ngợi ca; lời người kể + lời nhân vật."],
            ["Chủ đề chung", "Khát vọng chinh phục tự nhiên, cứu đời, cái thiện thắng cái ác, ý thức cội nguồn."],
            ["Nữ Oa vá trời", "Luyện đá – chống cột (chân rùa) – diệt long – chặn lũ; hình tượng người mẹ cứu thế."],
            ["Lạc Long Quân – Âu Cơ", "Rồng – Tiên, bọc trăm trứng, chia 50–50; con Rồng cháu Tiên, đại đoàn kết."],
            ["Phân biệt nhanh", "Thần thoại ‘vì sao?’ – Sử thi ‘chiến công’ – Truyền thuyết ‘địa danh/lịch sử’ – Cổ tích ‘ước mơ, có hậu’."],
        ], widths=[42, 134], size=8.7)

    # ------------------------------------------------ flashcards
    doc.h2("8.3. Bộ 20 thẻ ghi nhớ (flashcard) — luyện Active Recall")
    doc.para("Cách dùng: đọc mặt trước, tự trả lời, rồi lật mặt sau đối chiếu; thẻ nào sai để riêng ôn lại mỗi ngày.",
             size=9.6, family="sans")
    cards = [
        ("Thần thoại là gì?", "Truyện dân gian ra đời sớm nhất, kể về thần và sự kiện khởi nguyên, giải thích nguồn gốc thế giới, thể hiện khát vọng chinh phục tự nhiên."),
        ("Thần thoại suy nguyên là gì?", "Nhóm thần thoại giải thích nguồn gốc vũ trụ, muôn loài, hiện tượng tự nhiên, phong tục (VD: Thần Trụ Trời, Nữ Oa vá trời)."),
        ("Thần thoại sáng tạo là gì?", "Kể thần/anh hùng dạy nghề, diệt yêu quái, sáng tạo văn hoá, lập trật tự (VD: Thần Nông dạy trồng trọt)."),
        ("Thời gian thần thoại có gì đặc biệt?", "Là thời khởi nguyên, hồng hoang, chưa có lịch sử cụ thể, gắn quá trình hình thành thế giới."),
        ("Không gian thần thoại thường ra sao?", "Rộng tầm vũ trụ, thần kì: trời – đất chưa phân, thiên giới, thuỷ phủ, tứ cực, núi chống trời."),
        ("Vì sao nhân vật thần thường gọi theo chức năng?", "Tên gọi gắn trực tiếp vai trò giải thích một hiện tượng/lực lượng tự nhiên (Thần Sét, Thần Gió, Thần Trụ Trời)."),
        ("‘Tính nguyên hợp’ trong thần thoại?", "Sự hoà trộn nghệ thuật, tôn giáo, triết học, lịch sử và tri thức sơ khai trong một thể thống nhất."),
        ("Ngôi kể thường dùng và tác dụng?", "Ngôi thứ ba toàn tri → bao quát vũ trụ, khách quan, trang trọng, thiêng liêng, tạo niềm tin."),
        ("Lời người kể và lời nhân vật khác nhau thế nào?", "Lời người kể dẫn dắt, thuật việc, bình luận; lời nhân vật là đối thoại/độc thoại thể hiện tính cách."),
        ("Yếu tố kì ảo có vai trò gì?", "Hình tượng hoá cách giải thích thế giới và khát vọng chinh phục tự nhiên của người cổ đại."),
        ("Thần thoại khác sử thi ở điểm nào?", "Thần thoại: thần linh, giải thích nguồn gốc. Sử thi: anh hùng cộng đồng, chiến công, lịch sử bộ tộc/dân tộc."),
        ("Thần thoại khác truyền thuyết thế nào?", "Truyền thuyết gắn nhân vật/địa danh/sự kiện lịch sử, có dấu vết thật; thần thoại tập trung giải thích nguồn gốc bằng tưởng tượng."),
        ("Thần thoại khác cổ tích ra sao?", "Cổ tích hư cấu, thưởng thiện phạt ác, kết thúc có hậu, không nhằm giải thích nguồn gốc thế giới."),
        ("Nêu 4 việc Nữ Oa làm để cứu thế.", "Luyện đá ngũ sắc vá trời; chặt chân rùa làm cột; giết rồng đen, đuổi thú dữ; đốt tro lau lách ngăn lũ."),
        ("Vì sao trời bị thủng trong truyện Nữ Oa?", "Cung Công thua Chúc Dung, húc đầu vào núi Bất Chu làm gãy cột chống trời."),
        ("Nữ Oa tượng trưng cho điều gì?", "Người mẹ vĩ đại: lòng nhân ái, trách nhiệm cộng đồng, trí tuệ, cần cù, dám hi sinh cứu đời."),
        ("Ý nghĩa chi tiết bọc trăm trứng?", "Mọi người Việt cùng một cội nguồn, bình đẳng, đoàn kết máu thịt; nòi giống đông đúc, hùng cường."),
        ("Vì sao Lạc Long Quân – Âu Cơ chia con?", "Khác nết: Rồng ở thuỷ phủ, Tiên quen non cao; chia 50 lên núi – 50 về biển nhưng hẹn cứu giúp nhau."),
        ("‘Con Rồng cháu Tiên’ thể hiện điều gì?", "Ý thức cội nguồn chung, niềm tự hào dân tộc và tinh thần đại đoàn kết, non sông thống nhất."),
        ("Bài học vận dụng chung từ hai truyện?", "Trách nhiệm với cộng đồng, đoàn kết tương thân tương ái, dùng trí tuệ và lao động vượt khó, giữ gìn cội nguồn."),
    ]
    for i, (front, back) in enumerate(cards, 1):
        doc.flashcard(i, front, back)

    # ------------------------------------------------ kế hoạch 7 ngày
    doc.h2("8.4. Lộ trình ôn tập 7 ngày (mỗi ngày 60–90 phút)")
    doc.data_table(["Ngày", "Mục tiêu", "Nội dung chính", "Sản phẩm tự kiểm tra"],
        [
            ["Ngày 1", "Nắm ‘bản thiết kế’ đề thi", "Đọc kĩ Phần 1: ma trận, bản đặc tả, cấu trúc 11 câu.", "Tự vẽ lại bảng cấu trúc đề từ trí nhớ."],
            ["Ngày 2", "Chốt lí thuyết thể loại", "Học Phần 2: định nghĩa, phân loại, 6 đặc trưng, phân biệt 4 thể loại.", "Vẽ mind map thần thoại; làm 12 câu lí thuyết."],
            ["Ngày 3", "Luyện đọc hiểu ngữ liệu 1", "Phân tích *Nữ Oa vá trời* (Phần 3); học quy trình 4 bước.", "Điền bảng phân tích ngữ liệu tự làm."],
            ["Ngày 4", "Luyện đọc hiểu ngữ liệu 2", "Phân tích *Lạc Long Quân – Âu Cơ* (Phần 4); so sánh hai truyện.", "Viết đoạn so sánh 150 chữ."],
            ["Ngày 5", "Giải trọn đề minh hoạ", "Làm Đề 1, Đề 2 (Phần 5) như thi thật, tự chấm theo đáp án.", "Chấm điểm, ghi 3 lỗi cần sửa."],
            ["Ngày 6", "Chinh phục câu viết 4 điểm", "Học Phần 6, 7: dàn ý, công thức đoạn, đọc kĩ bài văn mẫu.", "Viết 1 bài nghị luận hoàn chỉnh."],
            ["Ngày 7", "Tổng ôn & vào ‘trạng thái thi’", "Học flashcard Phần 8, bảng từ khoá; xem lại lỗi; ngủ sớm.", "Tự kể lại toàn bộ kiến thức bằng miệng."],
        ], widths=[18, 40, 70, 48], size=8.3)
    doc.box("memory", [
        "**Nguyên tắc 3 lần chạm:** mỗi kiến thức quan trọng phải được gặp lại ít nhất 3 lần (học – tự kiểm tra – ôn lại). "
        "Đừng tham học nội dung mới mà bỏ qua bước gợi nhớ; chính việc ‘quên rồi nhớ lại’ làm trí nhớ bền chắc.",
    ])

    # ------------------------------------------------ chiến thuật 90 phút
    doc.h2("8.5. Chiến thuật phân bổ thời gian trong 90 phút làm bài")
    doc.data_table(["Giai đoạn", "Thời lượng", "Việc cần làm"],
        [
            ["Đọc đề & định hướng", "5 phút", "Đọc toàn bộ câu hỏi; xác định ngữ liệu thuộc nhóm thần thoại nào; gạch từ khoá yêu cầu."],
            ["Trắc nghiệm (câu 1–8)", "12–15 phút", "Đọc ngữ liệu, khoanh vùng dữ liệu; loại nhanh phương án sai; đánh dấu câu phân vân để quay lại."],
            ["Tự luận đọc hiểu (9–10)", "18–20 phút", "Làm câu Thông hiểu trước (tóm tắt, phân tích); câu Vận dụng đảm bảo bộ ba bài học – liên hệ – hành động."],
            ["Viết nghị luận (câu 11)", "40–45 phút", "Lập dàn ý 7 phút; viết 28–30 phút; đủ mở – thân – kết, mỗi đoạn một luận điểm, có dẫn chứng + đánh giá."],
            ["Rà soát", "5–7 phút", "Kiểm tra chính tả, dấu câu, từ Hán Việt; bỏ sót câu trắc nghiệm nào không; trình bày sạch sẽ."],
        ], widths=[40, 24, 112], size=8.5)
    doc.box("warn", [
        "**Hai sai lầm ‘đốt điểm’ phổ biến:** (1) dành quá nhiều thời gian cho câu trắc nghiệm khó khiến bài viết bị dở dang "
        "— hãy tạm bỏ qua và quay lại sau; (2) viết câu nghị luận *không lập dàn ý* dẫn đến lan man, thiếu luận điểm. "
        "Câu viết 4 điểm xứng đáng nhận quỹ thời gian lớn nhất.",
    ])

    doc.h2("8.6. Checklist 10 điều trước khi nộp bài")
    doc.numbered([
        "Đã điền đủ thông tin cá nhân, số báo danh.",
        "Mọi câu trắc nghiệm đều được tô/chọn, không để trống (chọn bừa còn hơn bỏ trống).",
        "Câu tóm tắt đúng trình tự sự kiện, không thêm tình tiết bịa đặt.",
        "Câu Vận dụng có đủ BÀI HỌC – LIÊN HỆ THỰC TẾ – HÀNH ĐỘNG CỦA EM.",
        "Bài nghị luận đủ 3 phần, có câu chủ đề cho mỗi đoạn thân bài.",
        "Mỗi luận điểm đều có DẪN CHỨNG từ ngữ liệu kèm theo phân tích.",
        "Có đoạn đánh giá, thể hiện quan điểm cá nhân (điểm Vận dụng của câu viết).",
        "Không nhầm tên nhân vật, địa danh, chi tiết giữa các truyện.",
        "Không còn lỗi chính tả, dùng từ, dấu câu; không dùng tiếng lóng, từ ngoại lai.",
        "Chữ viết rõ ràng, trình bày sạch, gạch chân ý chính nếu cần.",
    ])

    doc.spacer(3)
    doc.box("info", [
        "**Lời kết:** Ma trận cho thấy đề thi không đánh đố bằng kiến thức hóc búa, mà kiểm tra năng lực *đọc – hiểu – nghĩ – viết* "
        "trên một thể loại đã được học bài bản. Nắm vững bộ khung thần thoại, luyện đọc hiểu có phương pháp và viết bài có dàn ý, "
        "bạn hoàn toàn tự tin chinh phục mức điểm 8–10. Chúc bạn ôn thi hiệu quả và thành công!",
    ])
