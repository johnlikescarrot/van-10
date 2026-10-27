# -*- coding: utf-8 -*-
"""Dựng PDF đề cương ôn tập giữa kì 1 - Ngữ văn 10 (Kết nối tri thức)."""
import glob, os
from renderer import PDF, Renderer

BASE = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE, "content")
OUT = os.path.join(BASE, "..", "de-cuong-on-tap-giua-ki-1-ngu-van-10.pdf")


def cover(pdf: PDF):
    pdf.add_page()
    # khung trang bìa
    pdf.set_draw_color(23, 71, 113)
    pdf.set_line_width(1.2)
    pdf.rect(10, 10, pdf.w - 20, pdf.h - 20, style="D")
    pdf.set_line_width(0.4)
    pdf.rect(12.5, 12.5, pdf.w - 25, pdf.h - 25, style="D")
    pdf.set_y(38)
    pdf.set_font("DVS", "B", 13)
    pdf.set_text_color(176, 82, 12)
    pdf.cell(0, 8, "SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG • NĂM HỌC 2026 – 2027", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_font("DVS", "B", 30)
    pdf.set_text_color(23, 71, 113)
    pdf.multi_cell(0, 14, "ĐỀ CƯƠNG ÔN TẬP\nKIỂM TRA GIỮA KÌ 1", align="C")
    pdf.ln(2)
    pdf.set_font("DVS", "B", 22)
    pdf.set_text_color(176, 82, 12)
    pdf.cell(0, 12, "MÔN: NGỮ VĂN – LỚP 10", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_font("DVS", "", 12)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 6.5, "Biên soạn bám sát MA TRẬN – BẢN ĐẶC TẢ của nhà trường\n"
                           "(Đọc hiểu: TRUYỆN THẦN THOẠI – ngữ liệu ngoài SGK • Viết: NGHỊ LUẬN PHÂN TÍCH,\n"
                           "ĐÁNH GIÁ MỘT TÁC PHẨM TRUYỆN • Thời gian làm bài: 90 phút)", align="C")
    pdf.ln(8)
    # hộp điểm nhấn
    y = pdf.get_y()
    pdf.set_fill_color(235, 241, 248)
    pdf.set_draw_color(110, 150, 190)
    pdf.rect(30, y, pdf.w - 60, 46, style="DF")
    pdf.set_xy(34, y + 5)
    pdf.set_font("DVS", "B", 12)
    pdf.set_text_color(23, 71, 113)
    pdf.cell(pdf.w - 68, 7, "TÀI LIỆU NÀY CÓ GÌ?", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DVS", "", 10.5)
    pdf.set_text_color(40, 40, 40)
    for t in ["✦ Hệ thống kiến thức Bài 1 – Bài 3 đầy đủ, sơ đồ hoá, dễ ghi nhớ",
              "✦ Lý thuyết thần thoại chuyên sâu + hướng dẫn đọc hiểu từng văn bản",
              "✦ Ngân hàng 100+ câu hỏi: trắc nghiệm, đọc hiểu, tự luận – CÓ ĐÁP ÁN VÀ GIẢI THÍCH",
              "✦ 02 đề thi thử đúng cấu trúc ma trận + hướng dẫn chấm chi tiết",
              "✦ Công cụ ghi nhớ nhanh, lộ trình ôn 7 ngày, bí quyết phòng thi"]:
        pdf.cell(0, 6, t, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(pdf.h - 46)
    pdf.set_font("DVS", "", 10)
    pdf.set_text_color(110, 110, 110)
    pdf.cell(0, 6, "Tài liệu lưu hành nội bộ phục vụ ôn tập – Biên soạn trên nền tảng mã nguồn mở", align="C", new_x="LMARGIN", new_y="NEXT")


def main():
    files = sorted(glob.glob(os.path.join(CONTENT_DIR, "*.md")))
    texts = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            texts.append(fh.read())

    # lượt 1: đo số trang mục lục
    pdf = PDF()
    r = Renderer(pdf)
    cover(pdf)
    r.toc_pages = 2
    for t in texts:
        r.render_text(t)
    # ước lượng số trang mục lục theo số đầu mục
    n_entries = sum(1 for lvl, _, _ in r.toc if lvl != 4)
    # Page references are measured in the first content pass, which starts
    # after the cover. The final pass inserts the cover plus the TOC pages.
    r.toc_pages = (1 if n_entries <= 38 else 2)
    r.toc_entries = r.toc
    r.toc = []

    # lượt 2: dựng thật (có mục lục)
    pdf = PDF()
    r2 = Renderer(pdf)
    r2.toc_pages = r.toc_pages
    r2.toc = r.toc_entries
    cover(pdf)
    r2.render_toc()
    for t in texts:
        r2.render_text(t)
    pdf.output(os.path.abspath(OUT))
    print("OK:", os.path.abspath(OUT), "| pages:", pdf.page_no())


if __name__ == "__main__":
    main()
