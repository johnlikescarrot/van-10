# -*- coding: utf-8 -*-
"""
Build cuốn Đề cương ôn tập Giữa học kì I Ngữ văn 10 (KNTT) 2026–2027.
Hai lượt render: lượt 1 lấy số trang từng phần; lượt 2 in bìa + mục lục + nội dung.
Chạy:  .venv/bin/python de-cuong-on-tap/bo-go/build_pdf.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_engine import (Doc, CONTENT_W, ML, MR, MM_W, MM_H, INK, NAVY, TEAL, GOLD,
                        CRIMSON, GREEN, PURPLE, GREY, FILL_NAVY, FILL_TEAL,
                        FILL_GOLD, FILL_GREY, FILL_GREEN)
import part01_giai_ma
import part02_ly_thuyet
import part03_doc_hieu_nu_oa
import part04_lac_long_quan
import part05_de1
import part06_de2
import part07_viet
import part08_van_mau
import part09_so_tay

MODULES = [
    part01_giai_ma, part02_ly_thuyet, part03_doc_hieu_nu_oa, part04_lac_long_quan,
    part05_de1, part06_de2, part07_viet, part08_van_mau, part09_so_tay,
]

OUT = "/home/user/van-10/de-cuong-on-tap/pdf/De_cuong_on_tap_Giua_ki_I_Ngu_van_10_KNTT_2026-2027.pdf"

DESC = {
    1: "Mục tiêu, ma trận, bản đặc tả và cấu trúc 11 câu của đề thi",
    2: "Định nghĩa, phân loại, 6 đặc trưng, giá trị & cách phân biệt thể loại",
    3: "Quy trình đọc hiểu 4 bước và phân tích mẫu truyện Nữ Oa vá trời",
    4: "Thần thoại nguồn gốc Lạc Long Quân – Âu Cơ và ranh giới thể loại",
    5: "Hai đề minh hoạ 11 câu chuẩn ma trận, đáp án & giải thích đầy đủ",
    6: "Cách viết bài nghị luận phân tích, đánh giá tác phẩm truyện (4 điểm)",
    7: "Bài văn mẫu hoàn chỉnh, thang điểm chấm và đoạn văn mẫu",
    8: "Flashcard, bảng từ khoá, lộ trình 7 ngày & chiến thuật làm bài 90 phút",
}


def build_content(doc):
    for m in MODULES:
        m.build(doc)


# ---------------------------------------------------------------- trang bìa
def _center_line(doc, y, text, family, style, size, color, h=None):
    doc.set_xy(ML, y)
    doc.set_font(family, style, size)
    doc.set_text_color(*color)
    doc.multi_cell(CONTENT_W, h or size * 0.5, text, align="C")


def draw_cover(doc):
    doc.add_page()
    doc.set_auto_page_break(False)   # tự bố trí tuyệt đối trên trang bìa
    # dải navy trên cùng
    doc.set_fill_color(*NAVY)
    doc.rect(0, 0, MM_W, 78, style="F")
    # đường vàng ngăn cách
    doc.set_fill_color(*GOLD)
    doc.rect(0, 78, MM_W, 2.2, style="F")
    # nhãn nhỏ
    _center_line(doc, 22, "TÀI LIỆU ÔN TẬP CHUYÊN SÂU", "sans", "B", 13, (255, 255, 255), h=8)
    _center_line(doc, 33, "Biên soạn bám sát Ma trận & Bản đặc tả của nhà trường",
                 "sans", "", 10.5, (214, 226, 240), h=7)

    # khối tiêu đề
    _center_line(doc, 96, "NGỮ VĂN 10", "sans", "B", 30, NAVY, h=14)
    _center_line(doc, 120, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I", "sans", "B", 17, TEAL, h=10)
    _center_line(doc, 136, "Bộ sách Kết nối tri thức với cuộc sống  ·  Năm học 2026 – 2027",
                 "sans", "", 12, GREY, h=7)
    # gạch trang trí
    doc.set_draw_color(*GOLD)
    doc.set_line_width(0.8)
    doc.line(ML + 45, 152, MM_W - MR - 45, 152)

    # hộp thông tin cấu trúc
    box_y = 162
    doc.set_fill_color(*FILL_NAVY)
    doc.rect(ML, box_y, CONTENT_W, 58, style="F")
    doc.set_fill_color(*NAVY)
    doc.rect(ML, box_y, 2.4, 58, style="F")
    info = [
        ("Thời gian làm bài", "90 phút  ·  11 câu  ·  thang điểm 10"),
        ("Trục năng lực", "Đọc hiểu 60%  +  Viết 40%"),
        ("Cấp độ tư duy", "Biết 40%  –  Hiểu 30%  –  Vận dụng 30%"),
        ("Ngữ liệu trọng tâm", "Truyện thần thoại ngoài sách giáo khoa"),
        ("Hình thức", "8 câu trắc nghiệm  ·  2 câu tự luận  ·  1 bài nghị luận"),
    ]
    cy = box_y + 5.5
    for k, v in info:
        doc.set_xy(ML + 7, cy)
        doc.set_font("sans", "B", 10.2)
        doc.set_text_color(*NAVY)
        doc.cell(52, 9, k + ":")
        doc.set_font("sans", "", 10.2)
        doc.set_text_color(*INK)
        doc.cell(CONTENT_W - 59, 9, v)
        cy += 9.6

    # hộp cam kết
    pledge_y = 228
    doc.set_fill_color(*FILL_GOLD)
    doc.rect(ML, pledge_y, CONTENT_W, 30, style="F")
    doc.set_fill_color(*GOLD)
    doc.rect(ML, pledge_y, 2.4, 30, style="F")
    doc.set_xy(ML + 7, pledge_y + 3)
    doc.set_font("sans", "B", 10.5)
    doc.set_text_color(*GOLD)
    doc.cell(60, 6, "CAM KẾT NỘI DUNG")
    doc.set_xy(ML + 7, pledge_y + 10.5)
    doc.set_font("serif", "", 9.8)
    doc.set_text_color(*INK)
    doc.multi_cell(CONTENT_W - 14, 5.2,
        "Toàn bộ câu hỏi, đáp án, dàn ý và bài văn mẫu được dựng đúng từng ô của Ma trận – Bản đặc tả; "
        "lí thuyết bám sách Kết nối tri thức; ngữ liệu thần thoại ngoài SGK kèm phân tích mẫu và phương pháp ghi nhớ tối ưu.",
        align="J")

    # dải chân trang bìa
    doc.set_fill_color(*NAVY)
    doc.rect(0, MM_H - 20, MM_W, 20, style="F")
    _center_line(doc, MM_H - 15.5,
                 "Học chắc bộ khung thể loại  ·  Luyện đọc hiểu có phương pháp  ·  Viết bài có dàn ý",
                 "sans", "", 9.6, (255, 255, 255), h=6)
    _center_line(doc, MM_H - 9.2,
                 "Tài liệu lưu hành nội bộ phục vụ học tập — 2026",
                 "sans", "", 8.6, (200, 214, 230), h=5.5)
    doc.set_auto_page_break(True, margin=17)


# ---------------------------------------------------------------- mục lục
def draw_toc(doc, toc, offset):
    doc.add_page()
    doc.set_auto_page_break(False)
    doc.set_xy(ML, 22)
    doc.set_font("sans", "B", 19)
    doc.set_text_color(*NAVY)
    doc.multi_cell(CONTENT_W, 11, "MỤC LỤC", align="C")
    doc.ln(4)
    doc.set_draw_color(*GOLD)
    doc.set_line_width(0.7)
    doc.line(ML, doc.get_y(), MM_W - MR, doc.get_y())
    doc.ln(6)
    for idx, (title, page) in enumerate(toc, 1):
        pageno = page + offset
        # dòng tên phần + số trang (cùng một hàng, rồi mới xuống hàng)
        doc.set_x(ML)
        doc.set_font("sans", "B", 11.6)
        doc.set_text_color(*NAVY)
        doc.cell(148, 8.4, title)
        doc.set_text_color(*TEAL)
        doc.cell(CONTENT_W - 148, 8.4, str(pageno), align="R")
        doc.ln(8.4)
        # mô tả ngắn
        doc.set_x(ML + 2)
        doc.set_font("sans", "I", 8.8)
        doc.set_text_color(*GREY)
        doc.multi_cell(CONTENT_W - 2, 5.4, DESC.get(idx, ""), align="L")
        # đường kẻ dưới
        doc.ln(1.6)
        doc.set_draw_color(223, 227, 233)
        doc.set_line_width(0.25)
        doc.line(ML, doc.get_y(), MM_W - MR, doc.get_y())
        doc.ln(4.4)
    # ghi chú
    doc.ln(3)
    note_y = doc.get_y()
    doc.set_fill_color(*FILL_GREEN)
    doc.rect(ML, note_y, CONTENT_W, 18, style="F")
    doc.set_fill_color(*GREEN)
    doc.rect(ML, note_y, 2.4, 18, style="F")
    doc.set_xy(ML + 7, note_y + 2.4)
    doc.set_font("sans", "B", 9.6)
    doc.set_text_color(*GREEN)
    doc.cell(60, 5.4, "CÁCH DÙNG HIỆU QUẢ")
    doc.set_xy(ML + 7, note_y + 8.6)
    doc.set_font("serif", "", 9.4)
    doc.set_text_color(*INK)
    doc.multi_cell(CONTENT_W - 14, 5,
        "Học lần lượt từ Phần 1 đến Phần 8; đối chiếu flashcard hằng ngày và bấm giờ làm hai đề minh hoạ như thi thật.",
        align="J")
    doc.set_auto_page_break(True, margin=17)


def main():
    # ---- lượt 1: lấy số trang từng phần
    d1 = Doc()
    d1._in_cover = False
    d1.chrome_start_page = 1
    build_content(d1)
    toc = [(t, p) for (lvl, t, p) in d1.toc_entries if lvl == 1]
    content_pages = d1.page_no()

    # ---- lượt 2: bìa + mục lục + nội dung
    d2 = Doc()
    d2.chrome_start_page = 3
    draw_cover(d2)                 # trang 1
    draw_toc(d2, toc, offset=2)    # trang 2
    d2._in_cover = False
    build_content(d2)              # từ trang 3
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    d2.output(OUT)
    print("Số phần (mục lục):", len(toc))
    print("Trang phần nội dung (lượt 1):", content_pages)
    print("Tổng trang PDF (lượt 2):", d2.page_no())
    print("Đã xuất:", OUT)


if __name__ == "__main__":
    main()
