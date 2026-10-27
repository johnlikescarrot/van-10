# -*- coding: utf-8 -*-
"""Phần 7: Bài văn mẫu hoàn chỉnh (Nữ Oa) + đoạn mẫu (Lạc Long Quân) + thang điểm."""
from pdf_engine import (NAVY, TEAL, GOLD, CRIMSON, GREEN, PURPLE, GREY,
                        FILL_NAVY, FILL_TEAL, CONTENT_W, ML)


def build(doc):
    doc.h1("PHẦN 7", "Bài văn mẫu hoàn chỉnh & thang điểm chấm mẫu")

    doc.para(
        "Dưới đây là **bài văn nghị luận mẫu trọn vẹn** phân tích, đánh giá truyện *Nữ Oa vá trời*, "
        "viết đúng cấu trúc và đủ ba cấp độ của Bản đặc tả. Hãy học *cách triển khai ý, cách kết hợp lí lẽ – dẫn chứng* "
        "chứ không thuộc lòng; trong phòng thi, tuỳ thời gian có thể rút gọn còn khoảng 700–900 chữ.")

    doc.h2("7.1. BÀI VĂN MẪU: PHÂN TÍCH, ĐÁNH GIÁ TRUYỆN “NỮ OA VÁ TRỜI”")

    doc.h3("Mở bài")
    doc.para(
        "Thần thoại là thể loại mở đầu cho đời sống tinh thần của nhân loại, nơi con người cổ đại gửi gắm cách giải thích "
        "thế giới và những khát vọng lớn lao nhất. Trong kho tàng thần thoại phương Đông, truyện *Nữ Oa vá trời* của người "
        "Trung Hoa cổ là một tác phẩm giàu sức sống. Bằng trí tưởng tượng kì diệu, truyện không chỉ lí giải một cách hình tượng "
        "về cấu trúc vũ trụ mà còn dựng lên hình tượng một nữ thần cứu thế, qua đó bày tỏ niềm tin vào sức mạnh, trí tuệ và "
        "trách nhiệm của con người trước cộng đồng. Phân tích, đánh giá tác phẩm, ta thấy rõ những giá trị nội dung và nghệ thuật đặc sắc ấy.",
        gap=1.0)

    doc.h3("Thân bài")
    doc.para(
        "**Trước hết, *Nữ Oa vá trời* mang đầy đủ những đặc trưng cốt lõi của thần thoại suy nguyên.** Truyện mở ra ở thời "
        "khởi nguyên, sau khi nữ thần Nữ Oa nặn đất tạo người, trong một không gian vũ trụ có vòm trời chống bằng cột, có núi "
        "Bất Chu ở tây bắc, có Ký Châu và tứ phương. Tai hoạ bắt đầu từ cuộc chiến giữa thuỷ thần Cung Công và hoả thần Chúc "
        "Dung: Cung Công thua trận, uất giận húc vào núi Bất Chu làm gãy cột chống trời, khiến trời thủng, đất nứt, lửa thiêu, "
        "lũ ngập, thú dữ hoành hành. Cách mở truyện cho thấy người cổ đại đã hình tượng hoá các lực lượng tự nhiên đối kháng "
        "thành những vị thần và giải thích tai ương bằng một chuỗi quan hệ nhân quả thần thoại. Chính từ hiện trường hỗn loạn ấy, "
        "hình tượng Nữ Oa hiện ra như một vị cứu tinh.", gap=1.0)
    doc.para(
        "**Giá trị sâu sắc nhất của tác phẩm tập trung ở hình tượng Nữ Oa và chuỗi hành động cứu thế của bà.** Trước nỗi đau "
        "của muôn loài (“vô cùng đau xót”), nữ thần không hề do dự mà một mình gánh trọng trách vá trời. Bốn hành động được kể "
        "lần lượt như những kì công: luyện đá ngũ sắc thành keo để vá lỗ thủng; chặt bốn chân rùa thần làm bốn cột chống ở tứ "
        "phương; giết rồng đen ở Ký Châu, đuổi thú dữ; đốt lau lách thành tro ngăn dòng lũ. Mỗi chi tiết đều mang ý nghĩa biểu "
        "tượng: đá ngũ sắc nung chảy là sự biến cải vật chất tự nhiên nhờ lao động và trí tuệ; bốn chân rùa chống trời gợi sự "
        "vững bền của tứ cực vũ trụ; tro lau lách ngăn lũ thể hiện óc quan sát, kinh nghiệm ứng phó với thiên nhiên. Đặc biệt, "
        "Nữ Oa chiến thắng không bằng vũ khí hay quyền năng tuyệt đối mà bằng sự mưu trí, cần cù, bền bỉ. Bà vừa là đấng sáng tạo "
        "(nặn đất sinh người), vừa là vị cứu tinh (vá trời cứu người), trở thành hình tượng người mẹ vĩ đại – biểu tượng của "
        "tình yêu thương và trách nhiệm với cộng đồng.", gap=1.0)
    doc.para(
        "**Từ hình tượng Nữ Oa, truyện gửi gắm nhiều thông điệp nhân văn bền vững.** Thứ nhất, tác phẩm ngợi ca tinh thần dám "
        "gánh vác, dám hi sinh vì lợi ích chung: khi cộng đồng lâm nạn, người có năng lực phải đứng lên thay vì thờ ơ. Thứ hai, "
        "nó thể hiện khát vọng chinh phục tự nhiên và niềm tin vào chiến thắng tất yếu của sự sống, cái thiện trước hủy diệt, "
        "cái ác – kết thúc truyện, trời lành, đất bằng, muôn loài hồi sinh. Thứ ba, truyện đề cao lao động sáng tạo và vai trò "
        "của người phụ nữ: nữ thần vừa sinh thành vừa che chở, một hình ảnh người mẹ – nữ anh hùng hiếm có trong văn minh cổ. "
        "Những thông điệp này vượt ra ngoài chức năng giải thích thế giới để trở thành bài học đạo đức cho mọi thời đại.", gap=1.0)
    doc.para(
        "**Về hình thức, *Nữ Oa vá trời* chinh phục người đọc bằng những đặc sắc nghệ thuật của thể loại.** Tác giả dân gian vận "
        "dụng trí tưởng tượng phóng đại, thần thánh hoá và nhân hoá mạnh mẽ, tạo ra hàng loạt chi tiết kì ảo (luyện đá vá trời, "
        "chân rùa làm trụ) nhưng vẫn hợp với lô-gích cảm xúc và quan niệm của người nguyên thủy. Nhân vật được lí tưởng hoá, mang "
        "tầm vóc vũ trụ. Ngôi kể thứ ba toàn tri giúp người kể bao quát cả thiên giới lẫn trần gian, vừa thuật lại sự việc vừa "
        "bộc lộ thái độ ngợi ca, thành kính (“người đời đời nhớ ơn”). Kết cấu ba chặng *tai hoạ – cứu thế – hồi sinh* chặt chẽ, "
        "kết hợp nghệ thuật liệt kê, điệp cấu trúc khiến bốn kì công của Nữ Oa nổi lên như một bản anh hùng ca; ngôn ngữ trang "
        "trọng, giàu hình ảnh, biểu tượng cũng góp phần tạo vẻ đẹp hùng tráng, thiêng liêng.", gap=1.0)
    doc.para(
        "**Đánh giá tổng thể, tác phẩm có giá trị nhiều mặt và vẫn nguyên tính thời sự.** Đó là giá trị nhận thức về quan niệm "
        "vũ trụ sơ khai, giá trị giáo dục về trách nhiệm và lòng nhân ái, giá trị thẩm mĩ qua hình tượng kì vĩ. Hơn nghìn năm "
        "trôi qua, hôm nay những “Nữ Oa vá trời” hiện thân nơi người lính cứu hoả lao vào biển lửa, nơi y bác sĩ giữa đại dịch, "
        "nơi bộ đội và nhân dân chống bão lũ, nơi các nhà khoa học âm thầm ứng phó biến đổi khí hậu. Riêng với em, bài học về "
        "trách nhiệm cộng đồng bắt đầu từ những hành động nhỏ: giúp đỡ bạn khó khăn, giữ gìn môi trường, sẵn sàng nhận phần việc "
        "chung. Em hoàn toàn đồng tình với thông điệp của truyện, bởi một xã hội tốt đẹp chỉ được “vá” nên từ sự chung tay của "
        "từng cá nhân có trách nhiệm.", gap=1.0)

    doc.h3("Kết bài")
    doc.para(
        "Tóm lại, *Nữ Oa vá trời* là một viên ngọc trong kho tàng thần thoại nhân loại, kết tinh trí tưởng tượng và khát vọng "
        "của con người cổ đại. Từ câu chuyện luyện đá vá trời, tác phẩm để lại hình tượng người mẹ vĩ đại, bài học về trí tuệ, "
        "lòng dũng cảm và trách nhiệm với cộng đồng cùng những đặc sắc nghệ thuật đặc trưng của thể loại. Đọc truyện, thế hệ hôm "
        "nay không chỉ hiểu thêm cách người xưa lí giải thế giới mà còn tìm thấy động lực để sống có trách nhiệm, biết cống hiến "
        "cho cộng đồng – đó chính là sức sống lâu bền của một thần thoại giàu giá trị nhân văn.", gap=1.0)

    # ------------------------------------------------ thang điểm
    doc.h2("7.2. Thang điểm chấm mẫu cho câu Viết (4,0 điểm)")
    doc.data_table(["Tiêu chí đánh giá", "Biểu hiện cụ thể", "Điểm"],
        [
            ["1. Cấu trúc & mở bài", "Đúng cấu trúc nghị luận; giới thiệu đủ tên tác phẩm, thể loại, xuất xứ; nêu rõ vấn đề nghị luận.", "0,5"],
            ["2. Triển khai thân bài", "Có hệ thống luận điểm về nội dung, nghệ thuật, chủ đề; phân tích sâu, có dẫn chứng tiêu biểu, chính xác.", "2,0"],
            ["3. Lí lẽ – đánh giá – liên hệ", "Kết hợp chặt chẽ lí lẽ và dẫn chứng; có đánh giá, quan điểm cá nhân, liên hệ thực tế (tầng Vận dụng).", "0,75"],
            ["4. Kết bài", "Khái quát được giá trị, nêu bài học; kết thúc ấn tượng, không lặp ý khô khan.", "0,5"],
            ["5. Chính tả, dùng từ, sáng tạo", "Đảm bảo chính tả, ngữ pháp; văn viết mạch lạc, có nét sáng tạo trong diễn đạt.", "0,25"],
        ], widths=[40, 112, 24], size=8.5)
    doc.box("tip", [
        "**Vì sao bài mẫu trên đạt điểm cao:** (1) đúng cấu trúc, mỗi đoạn một luận điểm rõ; (2) dẫn chứng *trúng và đủ* "
        "(đá ngũ sắc, chân rùa, rồng đen, tro lau, câu chữ trong truyện); (3) luôn *phân tích ý nghĩa* sau mỗi dẫn chứng, không kể lại; "
        "(4) có cả tầng đánh giá – liên hệ – quan điểm cá nhân; (5) nhiều từ nối tạo mạch lạc.",
    ])

    # ------------------------------------------------ đoạn mẫu Lạc Long
    doc.h2("7.3. Đoạn văn mẫu phân tích chi tiết “cái bọc trăm trứng” (Lạc Long Quân – Âu Cơ)")
    doc.para(
        "Trong *Lạc Long Quân – Âu Cơ*, chi tiết cái bọc trăm trứng nở ra trăm người con trai là sáng tạo nghệ thuật giàu ý nghĩa "
        "biểu tượng nhất. Trước hết, hình ảnh “một bọc” duy nhất nhấn mạnh rằng mọi người Việt đều sinh ra từ cùng một nguồn cội, "
        "bình đẳng và gắn bó máu thịt, không phân biệt sang hèn. Trăm quả trứng nở trăm người con khôi ngô, khoẻ mạnh lại gợi tả "
        "sự đông đúc, nòi giống hùng cường và sức sống mãnh liệt của cộng đồng. Bằng yếu tố kì ảo đặc trưng của thần thoại, "
        "tác giả dân gian đã hình tượng hoá niềm tin thiêng liêng về tổ tiên chung, làm cơ sở cho danh hiệu *con Rồng cháu Tiên*. "
        "Chi tiết này, cùng với lời dặn “hễ có việc gì thì cứu giúp lẫn nhau”, trở thành hạt giống tinh thần nuôi dưỡng truyền "
        "thống đại đoàn kết, tương thân tương ái của dân tộc Việt Nam ngàn đời sau. Với em, đó là lời nhắc mỗi cá nhân phải "
        "biết tôn trọng, yêu thương và sát cánh cùng đồng bào mọi vùng miền.", gap=1.0)
    doc.box("warn", [
        "**Lưu ý trình bày:** tuyệt đối không pha từ ngoại lai, từ ngữ mạng, tiếng lóng trong bài văn nghị luận; "
        "dành 3–5 phút cuối giờ rà soát lỗi chính tả, dấu câu, từ Hán Việt và những câu thiếu chủ ngữ trước khi nộp bài.",
    ])
