# -*- coding: utf-8 -*-
"""
Engine xuất PDF tiếng Việt cho Đề cương ôn tập Ngữ văn 10 (KNTT).
Dùng fpdf2 + font DejaVu (hỗ trợ đầy đủ dấu tiếng Việt).
Cách dùng: xem build_pdf.py
"""
import glob
import os
import re
from fpdf import FPDF
from fpdf.fonts import FontFace

# Bộ token markdown nội bộ: **bold**, *italic*, _italic_ (hỗ trợ lồng nhau)
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.S)
_ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)([^*\n]+?)\*(?!\*)|(?<!_)_([^_\n]+?)_(?!_)")


def _find_font_dir():
    """Ưu tiên bộ DejaVu đầy đủ (có italic) trong matplotlib; fallback font hệ thống."""
    candidates = sorted(glob.glob(
        os.path.join(os.path.dirname(__import__("fpdf").__file__), "..", "..",
                     "matplotlib", "mpl-data", "fonts", "ttf")
    ))
    candidates += [
        "/home/user/van-10/.venv/lib/python3.11/site-packages/matplotlib/mpl-data/fonts/ttf",
        "/usr/share/fonts/truetype/dejavu",
    ]
    for c in candidates:
        if os.path.isfile(os.path.join(c, "DejaVuSans-Oblique.ttf")):
            return c
    return candidates[-1]


FONT_DIR = _find_font_dir()

# ---------------------------------------------------------------- bảng màu
INK      = (33, 37, 45)      # chữ chính
NAVY     = (20, 52, 84)      # tiêu đề cấp 1, bìa
TEAL     = (11, 104, 108)    # tiêu đề cấp 2
GOLD     = (170, 110, 22)    # hộp ghi nhớ
CRIMSON  = (176, 42, 42)     # hộp cảnh báo/lưu ý
GREEN    = (30, 115, 70)     # hộp mẹo
PURPLE   = (92, 62, 140)     # hộp thông tin
GREY     = (90, 98, 110)

FILL_NAVY    = (231, 238, 246)
FILL_TEAL    = (228, 242, 242)
FILL_GOLD    = (252, 244, 228)
FILL_CRIMSON = (252, 234, 233)
FILL_GREEN   = (232, 245, 237)
FILL_PURPLE  = (240, 236, 248)
FILL_GREY    = (244, 246, 248)

BOX_STYLE = {
    "info":    {"accent": PURPLE,  "fill": FILL_PURPLE,  "icon": "▶", "label": "THÔNG TIN"},
    "memory":  {"accent": GOLD,    "fill": FILL_GOLD,    "icon": "★", "label": "GHI NHỚ"},
    "tip":     {"accent": GREEN,   "fill": FILL_GREEN,   "icon": "✓", "label": "MẸO LÀM BÀI"},
    "warn":    {"accent": CRIMSON, "fill": FILL_CRIMSON, "icon": "!", "label": "LƯU Ý"},
    "note":    {"accent": TEAL,    "fill": FILL_TEAL,    "icon": "▪", "label": "GHI CHÚ"},
}

MM_W, MM_H = 210, 297
ML, MR, MT, MB = 17, 17, 18, 17
CONTENT_W = MM_W - ML - MR   # 176 mm


class Doc(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(ML, MT, MR)
        self.set_auto_page_break(auto=True, margin=MB)
        self.set_title("Đề cương ôn tập Giữa học kì I Ngữ văn 10 (Kết nối tri thức) 2026-2027")
        self.set_author("Tài liệu biên soạn theo Ma trận & Bản đặc tả của nhà trường")
        self.set_creator("fpdf2 - DejaVu fonts")
        # font sans
        self.add_font("sans", "",       f"{FONT_DIR}/DejaVuSans.ttf")
        self.add_font("sans", "B",      f"{FONT_DIR}/DejaVuSans-Bold.ttf")
        self.add_font("sans", "I",      f"{FONT_DIR}/DejaVuSans-Oblique.ttf")
        self.add_font("sans", "BI",     f"{FONT_DIR}/DejaVuSans-BoldOblique.ttf")
        # font serif (nội dung văn bản đọc)
        self.add_font("serif", "",      f"{FONT_DIR}/DejaVuSerif.ttf")
        self.add_font("serif", "B",     f"{FONT_DIR}/DejaVuSerif-Bold.ttf")
        self.add_font("serif", "I",     f"{FONT_DIR}/DejaVuSerif-Italic.ttf")
        self.add_font("serif", "BI",    f"{FONT_DIR}/DejaVuSerif-BoldItalic.ttf")
        self.alias_nb_pages()
        self.toc_entries = []          # [(level, title, page_no)]
        self._in_cover = True
        self.section_title = ""
        self.chrome_start_page = 1     # header/footer chỉ hiện từ trang này

    # ------------------------------------------------ header / footer
    def header(self):
        if self._in_cover or self.page_no() < self.chrome_start_page:
            return
        self.set_font("sans", "", 7.6)
        self.set_text_color(*GREY)
        self.set_y(9)
        self.cell(0, 5, "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  ·  NGỮ VĂN 10 (KẾT NỐI TRI THỨC)  ·  2026–2027",
                  align="L")
        self.set_y(13.2)
        self.set_draw_color(*NAVY)
        self.set_line_width(0.25)
        self.line(ML, 13.2, MM_W - MR, 13.2)

    def footer(self):
        if self._in_cover or self.page_no() < self.chrome_start_page:
            return
        self.set_y(-12.5)
        self.set_draw_color(210, 214, 220)
        self.set_line_width(0.2)
        self.line(ML, self.get_y(), MM_W - MR, self.get_y())
        self.set_y(-11)
        self.set_font("sans", "", 8)
        self.set_text_color(*GREY)
        self.cell(0, 5, f"Trang {self.page_no()} / {{nb}}", align="C")

    # ------------------------------------------------ tiện ích hạ tầng
    def _space_left(self):
        return MM_H - MB - self.get_y()

    def ensure_space(self, need_mm):
        if self._space_left() < need_mm:
            self.add_page()

    @staticmethod
    def _has_italic(text):
        return bool(_ITALIC_RE.search(text))

    def _emit_italic(self, text, family, size, h, base_style=""):
        """In một đoạn không chứa **bold**; bóc *italic* / _italic_ (kế thừa style gốc)."""
        pos = 0
        for m in _ITALIC_RE.finditer(text):
            if m.start() > pos:
                self.set_font(family, base_style, size)
                self.write(h, text[pos:m.start()])
            inner = m.group(1) if m.group(1) is not None else m.group(2)
            style = "BI" if "B" in base_style else "I"
            self.set_font(family, style, size)
            self.write(h, inner)
            pos = m.end()
        if pos < len(text):
            self.set_font(family, base_style, size)
            self.write(h, text[pos:])

    def _emit_rich(self, text, family, size, h):
        """Bóc **bold** trước; phần trong bold vẫn tiếp tục bóc italic (hỗ trợ lồng nhau)."""
        pos = 0
        for m in _BOLD_RE.finditer(text):
            if m.start() > pos:
                self._emit_italic(text[pos:m.start()], family, size, h, "")
            self._emit_italic(m.group(1), family, size, h, "B")
            pos = m.end()
        if pos < len(text):
            self._emit_italic(text[pos:], family, size, h, "")

    def rich_text(self, text, size, family="serif", h=None, width=None, align="J",
                  x=None, color=INK):
        """Render chuỗi hỗ trợ **bold**, *italic*, _italic_; tự xuống đoạn theo \\n."""
        if h is None:
            h = size * 0.52
        if width is None:
            width = CONTENT_W
        if x is not None:
            self.set_x(x)
        self.set_text_color(*color)
        for paragraph in text.split("\n"):
            if paragraph == "":
                self.ln(h)
                continue
            if not self._has_italic(paragraph):
                # không có italic: tận dụng multi_cell để được căn đều (justify)
                self.set_font(family, "", size)
                self.multi_cell(width, h, paragraph, align=align, markdown=True)
            else:
                # có italic: parser đệ quy + write() (tự xuống dòng theo lề phải)
                self.set_font(family, "", size)
                self._emit_rich(paragraph, family, size, h)
                self.ln(h)

    def _rich_multi(self, text, size, family="serif", h=None, align="J", indent=0, color=INK):
        if h is None:
            h = size * 0.52
        self.rich_text(text, size, family=family, h=h,
                       width=CONTENT_W - indent, x=ML + indent if indent else None,
                       align=align, color=color)

    # ------------------------------------------------ tiêu đề
    def h1(self, chip, title):
        self.add_page()
        self.toc_entries.append((1, f"{chip}. {title}".strip(". "), self.page_no()))
        self.section_title = title
        y0 = self.get_y() + 2
        self.set_fill_color(*NAVY)
        self.rect(ML, y0, 18, 11, style="F")
        self.set_font("sans", "B", 9.2)
        self.set_text_color(255, 255, 255)
        self.set_xy(ML, y0 + 1.7)
        self.cell(18, 8, chip, align="C")
        self.set_xy(ML + 21, y0 + 0.9)
        self.set_font("sans", "B", 16)
        self.set_text_color(*NAVY)
        self.multi_cell(CONTENT_W - 21, 8, title.upper(), align="L")
        self.ln(1.5)
        self.set_draw_color(*GOLD)
        self.set_line_width(0.7)
        self.line(ML, self.get_y(), MM_W - MR, self.get_y())
        self.ln(3.2)

    def h2(self, title):
        self.ensure_space(16)
        self.toc_entries.append((2, title, self.page_no()))
        self.ln(1.2)
        self.set_font("sans", "B", 13)
        self.set_text_color(*TEAL)
        self.multi_cell(CONTENT_W, 6.6, title, align="L")
        self.ln(0.8)
        self.set_draw_color(*TEAL)
        self.set_line_width(0.35)
        self.line(ML, self.get_y(), ML + 26, self.get_y())
        self.ln(2.4)

    def h3(self, title):
        self.ensure_space(11)
        self.ln(0.6)
        self.set_font("sans", "B", 11)
        self.set_text_color(*NAVY)
        self.multi_cell(CONTENT_W, 5.8, title, align="L")
        self.ln(1.1)

    # ------------------------------------------------ khối văn bản
    def para(self, text, size=10.4, family="serif", align="J", indent=0, gap=1.4):
        self.ensure_space(10)
        self._rich_multi(text, size, family=family, align=align, indent=indent)
        self.ln(gap)

    def bullets(self, items, size=10.2, level=0, gap=0.9):
        """items: list chuỗi (hỗ trợ markdown ** **). level đổi ký hiệu & thụt lề."""
        markers = ["●", "–", "▪", "·"]
        mcolors = [TEAL, GOLD, GREY, GREY]
        indent = 5 + level * 6
        mark = markers[min(level, 3)]
        for it in items:
            self.set_font("sans", "B", size)
            line_h = size * 0.52
            # đo chiều cao cần thiết
            x0 = ML + indent
            self.set_xy(x0, self.get_y())
            start_y = self.get_y()
            self.set_font("serif", "", size)
            # in marker
            self.set_font("sans", "B", size - 0.5)
            self.set_text_color(*mcolors[min(level, 3)])
            self.set_xy(ML + indent - 4.6, start_y)
            self.cell(4, line_h, mark)
            self.set_text_color(*INK)
            self.set_xy(x0, start_y)
            self.rich_text(it, size, family="serif", h=line_h,
                           width=CONTENT_W - indent, x=x0)
            self.ln(gap)
        self.ln(0.8)

    def numbered(self, items, size=10.2, prefix="", gap=1.1):
        for i, it in enumerate(items, 1):
            line_h = size * 0.52
            tag = f"{prefix}{i}."
            self.ensure_space(9)
            y0 = self.get_y()
            self.set_font("sans", "B", size)
            w_tag = self.get_string_width(tag) + 2.4
            self.set_text_color(*TEAL)
            self.set_xy(ML, y0)
            self.cell(w_tag, line_h, tag)
            self.set_text_color(*INK)
            self.set_xy(ML + w_tag, y0)
            self.rich_text(it, size, family="serif", h=line_h,
                           width=CONTENT_W - w_tag, x=ML + w_tag)
            self.ln(gap)
        self.ln(0.8)

    # ------------------------------------------------ hộp thông điệp
    def box(self, kind, content, title=None):
        """content: str hoặc list[str] (mỗi phần tử một đoạn)."""
        st = BOX_STYLE[kind]
        if title is None:
            title = st["label"]
        if isinstance(content, str):
            content = [content]
        size = 9.9
        line_h = size * 0.52
        pad = 3.2
        inner_w = CONTENT_W - 9 - pad * 2
        # đo chiều cao (bề rộng write thực tế tại vị trí in = CONTENT_W - 5 - pad)
        dummy = self._measure(content, size, line_h, CONTENT_W - 5 - pad)
        title_h = 6.2
        total_h = dummy + title_h + pad * 2
        self.ensure_space(total_h + 3)
        x0, y0 = ML, self.get_y()
        # nền + viền trái
        self.set_fill_color(*st["fill"])
        self.rect(x0, y0, CONTENT_W, total_h, style="F")
        self.set_fill_color(*st["accent"])
        self.rect(x0, y0, 2.4, total_h, style="F")
        # tiêu đề hộp
        self.set_xy(x0 + 5, y0 + 1.6)
        self.set_font("sans", "B", 9.6)
        self.set_text_color(*st["accent"])
        self.cell(inner_w, 5, f'{st["icon"]}  {title}')
        # nội dung
        cy = y0 + title_h
        for block in content:
            self.set_xy(x0 + 5 + pad, cy)
            self.rich_text(block, size, family="serif", h=line_h,
                           width=inner_w - pad, x=x0 + 5 + pad, color=INK)
            cy = self.get_y() + 0.8
        self.set_y(y0 + total_h + 2.2)

    def _measure(self, blocks, size, line_h, width):
        """Ước lượng chiều cao khối văn bản (có biên phòng ngừa ~6%)."""
        import math
        total = 0
        for b in blocks:
            for sub in b.split("\n"):
                est = max(1, math.ceil(self.get_string_width_safe(sub, size) / width * 1.06))
                total += est * line_h
            total += 0.8
        return total

    def get_string_width_safe(self, text, size):
        self.set_font("serif", "", size)
        # bỏ ký hiệu markdown khi đo
        clean = text.replace("**", "").replace("*", "")
        return self.get_string_width(clean)

    # ------------------------------------------------ bảng
    @staticmethod
    def _clean_cell(text):
        """Bảng fpdf2 chỉ hỗ trợ **bold**; hạ *italic*/_italic_ xuống chữ thường, giữ dấu * đơn (footnote)."""
        s = str(text)
        s = re.sub(r"\*\*([^*]+?)\*\*", r"\1", s)
        s = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"\1", s)
        s = re.sub(r"(?<!_)_([^_\n]+?)_(?!_)", r"\1", s)
        return s

    def data_table(self, headers, rows, widths=None, size=9.3, header_fill=NAVY,
                   zebra=FILL_GREY, align_headers="C"):
        if widths is None:
            widths = [CONTENT_W / len(headers)] * len(headers)
        headers = [self._clean_cell(h) for h in headers]
        rows = [[self._clean_cell(c) for c in r] for r in rows]
        head_style = FontFace(emphasis="BOLD", color=(255, 255, 255), fill_color=header_fill)
        self.ensure_space(18)
        self.set_font("serif", "", size)
        self.set_text_color(*INK)
        # Reset màu nền ngữ cảnh: chế độ ROWS tô dòng lẻ bằng fill_color của document
        self.set_fill_color(255, 255, 255)
        with self.table(
            col_widths=widths,
            headings_style=head_style,
            line_height=size * 0.55,
            width=CONTENT_W,
            markdown=True,
            cell_fill_color=zebra,
            cell_fill_mode="ROWS",
            borders_layout="ALL",
            padding=(1.6, 2.2),
            first_row_as_headings=True,
            text_align="L",
        ) as table:
            table.row(headers)
            for r in rows:
                table.row([str(c) for c in r])
        self.ln(2.6)

    # ------------------------------------------------ thẻ ngữ liệu đọc
    def reading_card(self, tag, title, source, paragraphs):
        size = 10.3
        line_h = size * 0.54
        pad = 4
        inner_w = CONTENT_W - pad * 2
        blocks = [f"**{title}**"] + [f"_{source}_"] + paragraphs
        # đoạn in tại x0+pad nên bề rộng write thực tế = CONTENT_W - pad
        height = self._measure(blocks, size, line_h, CONTENT_W - pad) + 9
        self.ensure_space(min(height + 4, 200))
        x0, y0 = ML, self.get_y()
        # nếu card quá cao so với phần còn lại nhưng vừa cả trang -> cho sang trang
        if height > self._space_left() - 2:
            self.add_page()
            y0 = self.get_y()
        self.set_fill_color(*FILL_GREY)
        self.rect(x0, y0, CONTENT_W, height, style="F")
        self.set_fill_color(*NAVY)
        self.rect(x0, y0, CONTENT_W, 7.6, style="F")
        self.set_xy(x0 + 3.5, y0 + 1.5)
        self.set_font("sans", "B", 9.8)
        self.set_text_color(255, 255, 255)
        self.cell(0, 5, tag)
        cy = y0 + 10
        self.set_xy(x0 + pad, cy)
        self.set_font("serif", "B", size + 1.2)
        self.set_text_color(*NAVY)
        self.multi_cell(inner_w, 6, title, align="C")
        self.ln(0.6)
        self.rich_text(source, size - 1, family="serif", h=line_h,
                       width=inner_w, align="C", color=GREY)
        self.ln(1.4)
        for p in paragraphs:
            self.rich_text(p, size, family="serif", h=line_h,
                           width=inner_w, x=x0 + pad, align="J", color=INK)
            self.ln(1.3)
        self.set_y(y0 + height + 3)

    # ------------------------------------------------ câu hỏi trắc nghiệm
    def mcq(self, idx, level_tag, question, options, size=10.1):
        line_h = size * 0.53
        self.ensure_space(22)
        y0 = self.get_y()
        # nhãn mức độ
        self.set_font("sans", "B", 8.2)
        tag_w = self.get_string_width(level_tag) + 5
        self.set_fill_color(*TEAL if "HIỂU" in level_tag else NAVY)
        self.set_text_color(255, 255, 255)
        self.set_xy(ML, y0)
        self.cell(tag_w, 5, level_tag, fill=True, align="C")
        self.set_xy(ML + tag_w + 2, y0)
        self.rich_text(f"Câu {idx}. {question}", size, family="sans", h=5.2,
                       width=CONTENT_W - tag_w - 2, x=ML + tag_w + 2,
                       align="L", color=NAVY)
        self.ln(0.6)
        letters = ["A", "B", "C", "D"]
        for j, opt in enumerate(options):
            self.ensure_space(7)
            self.set_x(ML + 4)
            self.set_font("sans", "B", size)
            self.set_text_color(*CRIMSON)
            self.cell(6, line_h, f"{letters[j]}.")
            self.rich_text(opt, size, family="serif", h=line_h,
                           width=CONTENT_W - 10, x=ML + 10, align="J", color=INK)
            self.ln(0.35)
        self.ln(1.6)

    def tl_question(self, idx, level_tag, question, size=10.3):
        self.ensure_space(16)
        self.set_font("sans", "B", 8.2)
        tag_w = self.get_string_width(level_tag) + 5
        self.set_fill_color(*GOLD if "VẬN DỤNG" in level_tag else GREEN)
        self.set_text_color(255, 255, 255)
        self.cell(tag_w, 5, level_tag, fill=True, align="C")
        self.ln(6.2)
        self.rich_text(f"Câu {idx}. {question}", size, family="sans", h=5.6,
                       width=CONTENT_W, align="L", color=NAVY)
        self.ln(2.2)

    # ------------------------------------------------ sơ đồ cây (mind map)
    def tree(self, lines, size=9.2):
        line_h = size * 0.62
        h = len(lines) * line_h + 4
        self.ensure_space(min(h + 4, 60))
        x0, y0 = ML, self.get_y()
        self.set_fill_color(*FILL_NAVY)
        self.rect(x0, y0, CONTENT_W, h, style="F")
        self.set_xy(x0 + 3, y0 + 2)
        for ln in lines:
            bold = ln.startswith("#")
            text = ln.lstrip("# ")
            self.set_font("sans", "B" if bold else "", size)
            self.set_text_color(*NAVY if bold else INK)
            self.set_x(x0 + 3.4)
            self.multi_cell(CONTENT_W - 6, line_h, text, align="L")
        self.set_y(y0 + h + 2.4)

    # ------------------------------------------------ thẻ ghi nhớ 2 mặt
    def flashcard(self, idx, front, back):
        size = 9.9
        line_h = size * 0.52
        h1 = self._measure([front], size, line_h, CONTENT_W - 5) + 4
        h2 = self._measure([back], size, line_h, CONTENT_W - 5) + 4
        need = h1 + h2 + 3
        self.ensure_space(need + 4)
        x0, y0 = ML, self.get_y()
        # mặt trước
        self.set_fill_color(*FILL_NAVY)
        self.rect(x0, y0, CONTENT_W, h1, style="F")
        self.set_fill_color(*NAVY)
        self.rect(x0, y0, 2.2, h1, style="F")
        self.set_xy(x0 + 5, y0 + 1.4)
        self.rich_text(f"THẺ {idx} – MẶT TRƯỚC (Câu hỏi): {front}", size - 0.6,
                       family="sans", h=line_h, width=CONTENT_W - 8,
                       x=x0 + 5, align="L", color=NAVY)
        # mặt sau
        y1 = y0 + h1 + 1.2
        self.set_fill_color(*FILL_GREEN)
        self.rect(x0, y1, CONTENT_W, h2, style="F")
        self.set_fill_color(*GREEN)
        self.rect(x0, y1, 2.2, h2, style="F")
        self.set_xy(x0 + 5, y1 + 1.4)
        self.set_font("sans", "B", size - 0.6)
        self.set_text_color(*GREEN)
        self.multi_cell(CONTENT_W - 8, line_h, "MẶT SAU (Đáp án):", align="L")
        self.rich_text(back, size, family="serif", h=line_h,
                       width=CONTENT_W - 8, x=x0 + 5, align="J", color=INK)
        self.set_y(y1 + h2 + 2.6)

    def spacer(self, mm=2):
        self.ln(mm)
