# -*- coding: utf-8 -*-
"""
Renderer: chuyển văn bản đánh dấu đơn giản (markdown-like) thành PDF tiếng Việt.
Hỗ trợ:
  # H1 (sang trang mới)  ## H2  ### H3  #### H4
  - gạch đầu dòng; + gạch đầu dòng cấp 2
  | bảng (dòng đầu là tiêu đề, dòng thứ 2 là ---)
  > hộp ghi chú (vàng nhạt) ; >> hộp đáp án (xanh nhạt)
  **đậm** trong dòng
  @@PAGEBREAK@@ sang trang thủ công
  @@NOBREAK@@ đầu file: H1 không sang trang
"""
import re
from fpdf import FPDF

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"

# Màu sắc chủ đạo
C_PRIMARY = (23, 71, 113)      # xanh navy
C_ACCENT = (176, 82, 12)       # cam đất
C_GREEN = (21, 101, 59)
C_GRAY = (110, 110, 110)
C_NOTE_BG = (255, 247, 222)
C_NOTE_LINE = (214, 178, 66)
C_ANS_BG = (232, 245, 233)
C_ANS_LINE = (76, 153, 94)
C_BOX_BG = (235, 241, 248)
C_BOX_LINE = (110, 150, 190)
C_TH_BG = (23, 71, 113)
C_ROW_ALT = (244, 247, 250)

SUBTITLE = "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ 1 – NGỮ VĂN 10 – KẾT NỐI TRI THỨC"


class PDF(FPDF):
    def __init__(self, doc_title=SUBTITLE):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.doc_title = doc_title
        self.part_title = ""
        self.show_header = False
        self.add_font("DVS", "", FONT_DIR + "DejaVuSans.ttf")
        self.add_font("DVS", "B", FONT_DIR + "DejaVuSans-Bold.ttf")
        self.add_font("DVSer", "", FONT_DIR + "DejaVuSerif.ttf")
        self.add_font("DVSer", "B", FONT_DIR + "DejaVuSerif-Bold.ttf")
        self.set_auto_page_break(True, margin=18)

    def header(self):
        if self.page_no() == 1 or not self.show_header:
            return
        self.set_font("DVS", "", 7.5)
        self.set_text_color(*C_GRAY)
        self.set_xy(15, 8)
        self.cell(self.epw, 4, self.doc_title, align="C")
        self.set_draw_color(*C_BOX_LINE)
        self.set_line_width(0.2)
        self.line(15, 13, self.w - 15, 13)
        self.set_y(18)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-13)
        self.set_font("DVS", "", 8)
        self.set_text_color(*C_GRAY)
        self.cell(0, 5, f"– {self.page_no()} –", align="C")


class Renderer:
    def __init__(self, pdf: PDF):
        self.pdf = pdf
        self.toc = []          # (level, text, page)
        self.collecting = False

    # ---------- tiện ích ----------
    def _rich(self, text):
        """Chia chuỗi thành [(bold, segment)]; bỏ dấu * đơn dùng cho chữ nghiêng."""
        text = re.sub(r"(?<!\*)\*(?!\*)", "", text)
        parts = re.split(r"\*\*", text)
        out = []
        for i, p in enumerate(parts):
            if p:
                out.append((i % 2 == 1, p))
        return out

    def _write_rich(self, text, size=10.5, lh=5.0, align="J", indent=0, color=(30, 30, 30), serif=False):
        fam = "DVSer" if serif else "DVS"
        segs = self._rich(text)
        x0 = self.pdf.l_margin + indent
        w = self.pdf.epw - indent
        # đo chiều cao
        total_w = 0
        line_h = lh
        self.pdf.set_font(fam, "B", size)
        # dùng write() với dry_run qua get_string_width để tính số dòng
        widths = []
        for bold, s in segs:
            self.pdf.set_font(fam, "B" if bold else "", size)
            widths.append(self.pdf.get_string_width(s))
        est_lines = max(1, int(sum(widths) / max(w, 1)) + 1)
        h = est_lines * line_h + 1
        y0 = self.pdf.get_y()
        if y0 + h > self.pdf.page_break_trigger:
            self.pdf.add_page()
            y0 = self.pdf.get_y()
        self.pdf.set_xy(x0, y0)
        for bold, s in segs:
            self.pdf.set_font(fam, "B" if bold else "", size)
            self.pdf.set_text_color(*color)
            self.pdf.write(line_h, s)
        self.pdf.ln(line_h * 0.9)

    def _box(self, text, bg, line, size=10.5, indent=0):
        fam = "DVS"
        x0 = self.pdf.l_margin + indent
        w = self.pdf.epw - indent - 6
        self.pdf.set_font(fam, "", size)
        # tính chiều cao
        plain = text.replace("**", "")
        n_lines = 1
        cur = 0
        line_h = 5.0
        for word in plain.split(" "):
            ww = self.pdf.get_string_width(word + " ")
            if cur + ww > w - 4:
                n_lines += 1
                cur = ww
            else:
                cur += ww
        h = n_lines * line_h + 6
        if self.pdf.get_y() + h > self.pdf.page_break_trigger:
            self.pdf.add_page()
        y0 = self.pdf.get_y()
        self.pdf.set_fill_color(*bg)
        self.pdf.set_draw_color(*line)
        self.pdf.set_line_width(0.5)
        self.pdf.rect(x0, y0, w + 6, h, style="DF")
        self.pdf.set_xy(x0 + 4, y0 + 3)
        for bold, s in self._rich(text):
            self.pdf.set_font(fam, "B" if bold else "", size)
            self.pdf.set_text_color(30, 30, 30)
            self.pdf.write(line_h, s)
        self.pdf.set_y(y0 + h + 2.5)

    # ---------- thành phần ----------
    def h1(self, text, newpage=True):
        # Avoid leaving a short callout alone on an otherwise blank page when
        # the previous section ended after an automatic page break.
        if newpage and (self.pdf.page_no() <= 2 or self.pdf.get_y() > 130):
            self.pdf.add_page()
        self.pdf.set_font("DVS", "B", 15)
        self.pdf.set_text_color(*C_PRIMARY)
        y = self.pdf.get_y()
        self.pdf.set_xy(self.pdf.l_margin, y)
        self.pdf.multi_cell(self.pdf.epw, 7.5, text, align="L")
        self.pdf.set_draw_color(*C_ACCENT)
        self.pdf.set_line_width(0.8)
        self.pdf.line(self.pdf.l_margin, self.pdf.get_y() + 1, self.pdf.l_margin + self.pdf.epw, self.pdf.get_y() + 1)
        self.pdf.ln(4)
        self.toc.append((1, text, self.pdf.page_no()))
        self.pdf.part_title = text

    def h2(self, text):
        if self.pdf.get_y() > 250:
            self.pdf.add_page()
        self.pdf.ln(1.5)
        self.pdf.set_font("DVS", "B", 12.5)
        self.pdf.set_text_color(*C_PRIMARY)
        self.pdf.set_x(self.pdf.l_margin)
        self.pdf.multi_cell(self.pdf.epw, 6.5, text, align="L")
        self.pdf.ln(1.5)
        self.toc.append((2, text, self.pdf.page_no()))

    def h3(self, text):
        if self.pdf.get_y() > 255:
            self.pdf.add_page()
        self.pdf.ln(1)
        self.pdf.set_font("DVS", "B", 11)
        self.pdf.set_text_color(*C_ACCENT)
        self.pdf.set_x(self.pdf.l_margin)
        self.pdf.multi_cell(self.pdf.epw, 6, text, align="L")
        self.pdf.ln(1)
        self.toc.append((3, text, self.pdf.page_no()))

    def h4(self, text):
        if self.pdf.get_y() > 258:
            self.pdf.add_page()
        self.pdf.ln(0.5)
        self._write_rich("**" + text + "**", size=10.5, color=C_GREEN)
        self.toc.append((4, text, self.pdf.page_no()))

    def para(self, text):
        self._write_rich(text)

    def bullet(self, text, level=0):
        mark = "•" if level == 0 else "–"
        indent = 3 + level * 5
        self._write_rich(f"{mark}  {text}", indent=indent)

    def numbered(self, text):
        m = re.match(r"(\d+)\.\s+(.*)", text)
        num, rest = m.group(1), m.group(2)
        self._write_rich(f"**{num}.** {rest}", indent=3)

    def note(self, text):
        self._box("★ " + text, C_NOTE_BG, C_NOTE_LINE)

    def answer(self, text):
        self._box(text, C_ANS_BG, C_ANS_LINE)

    def infobox(self, text):
        self._box(text, C_BOX_BG, C_BOX_LINE)

    def table(self, rows):
        if len(rows) > 2 and set(rows[1][0]) <= set("-: "):
            header, body = rows[0], rows[2:]
        else:
            header, body = rows[0], rows[1:]
        n = len(header)
        # ước lượng độ rộng cột theo nội dung
        self.pdf.set_font("DVS", "", 9.5)
        maxw = [0] * n
        for r in [header] + body:
            for i, c in enumerate(r[:n]):
                maxw[i] = max(maxw[i], self.pdf.get_string_width(c) + 6)
        total = sum(maxw) or 1
        widths = [max(12, w / total * self.pdf.epw) for w in maxw]
        scale = self.pdf.epw / sum(widths)
        widths = [w * scale for w in widths]
        line_h = 4.6
        # chiều cao mỗi hàng
        def row_h(cells):
            h = line_h + 3
            for i, c in enumerate(cells[:n]):
                c = c.replace("**", "")
                wtxt = max(widths[i] - 3, 5)
                lines = 1
                cur = 0
                for word in c.split(" "):
                    ww = self.pdf.get_string_width(word + " ")
                    if cur + ww > wtxt:
                        lines += 1
                        cur = ww
                    else:
                        cur += ww
                h = max(h, lines * line_h + 3)
            return h
        def draw_row(cells, y, fill=None, bold=False, color=(20, 20, 20)):
            self.pdf.set_font("DVS", "B" if bold else "", 9.5)
            self.pdf.set_text_color(*color)
            hh = row_h(cells)
            if y + hh > self.pdf.page_break_trigger:
                self.pdf.add_page()
                y = self.pdf.get_y()
                if fill:
                    pass
            if fill:
                self.pdf.set_fill_color(*fill)
            self.pdf.set_draw_color(160, 170, 180)
            self.pdf.set_line_width(0.15)
            x = self.pdf.l_margin
            for i, c in enumerate(cells[:n]):
                self.pdf.rect(x, y, widths[i], hh, style="D" + ("F" if fill else ""))
                self.pdf.set_xy(x + 1.5, y + 1.5)
                self.pdf.multi_cell(widths[i] - 3, line_h, c.replace("**", ""), align="L")
                x += widths[i]
            return y + hh
        y = self.pdf.get_y()
        y = draw_row(header, y, fill=C_TH_BG, bold=True, color=(255, 255, 255))
        for j, r in enumerate(body):
            y = draw_row(r, y, fill=C_ROW_ALT if j % 2 == 0 else None)
        self.pdf.set_y(y + 3)

    # ---------- nạp nội dung ----------
    def render_text(self, text):
        lines = text.split("\n")
        i = 0
        nobreak_first = text.lstrip().startswith("@@NOBREAK@@")
        first_h1_done = False
        while i < len(lines):
            line = lines[i].rstrip()
            s = line.strip()
            if s.startswith("@@NOBREAK@@"):
                i += 1
                continue
            if s == "@@PAGEBREAK@@":
                self.pdf.add_page()
                i += 1
                continue
            if not s:
                i += 1
                continue
            if s.startswith("|"):
                tbl = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                    tbl.append(cells)
                    i += 1
                self.table(tbl)
                continue
            if s.startswith("#### "):
                self.h4(s[5:].strip())
            elif s.startswith("### "):
                self.h3(s[4:].strip())
            elif s.startswith("## "):
                self.h2(s[3:].strip())
            elif s.startswith("# "):
                nb = (not first_h1_done) and nobreak_first
                self.h1(s[2:].strip(), newpage=not nb)
                first_h1_done = True
            elif s.startswith(">> "):
                self.answer(s[3:].strip())
            elif s.startswith("> "):
                self.note(s[2:].strip())
            elif s.startswith("+ "):
                self.bullet(s[2:].strip(), level=1)
            elif s.startswith("- "):
                self.bullet(s[2:].strip())
            elif re.match(r"\d+\.\s", s):
                self.numbered(s)
            else:
                self.para(s)
            i += 1

    def render_toc(self):
        self.pdf.add_page()
        self.pdf.set_font("DVS", "B", 16)
        self.pdf.set_text_color(*C_PRIMARY)
        self.pdf.cell(0, 10, "MỤC LỤC", align="C", new_x="LMARGIN", new_y="NEXT")
        self.pdf.ln(3)
        offset = self.toc_pages  # content page offset after cover and TOC
        for lvl, text, page in self.toc:
            if lvl == 4:
                continue
            ind = {1: 0, 2: 6, 3: 12}[lvl]
            size = {1: 10.2, 2: 9.4, 3: 8.8}[lvl]
            bold = lvl == 1
            if self.pdf.get_y() > 270:
                self.pdf.add_page()
            self.pdf.set_font("DVS", "B" if bold else "", size)
            self.pdf.set_text_color(*(C_PRIMARY if lvl == 1 else (40, 40, 40)))
            start_x = self.pdf.l_margin + ind
            right_x = self.pdf.l_margin + self.pdf.epw
            page_text = str(page + offset)
            page_w = self.pdf.get_string_width(page_text)
            max_title_w = right_x - start_x - page_w - 14
            title = text.replace("**", "")
            while title and self.pdf.get_string_width(title) > max_title_w:
                title = title[:-1]
            if title != text.replace("**", "") and len(title) > 3:
                title = title[:-3].rstrip() + "..."
            title_w = self.pdf.get_string_width(title)
            y = self.pdf.get_y()
            self.pdf.set_xy(start_x, y)
            self.pdf.set_text_color(*(C_PRIMARY if lvl == 1 else (40, 40, 40)))
            self.pdf.cell(title_w + 1, 5.6, title, new_x="RIGHT")
            dot_x = self.pdf.get_x()
            num_x = right_x - page_w
            gap = max(0, num_x - dot_x - 2)
            self.pdf.set_text_color(155, 155, 155)
            self.pdf.set_xy(dot_x, y)
            dots = ". " * max(0, int(gap / self.pdf.get_string_width(". ")))
            self.pdf.cell(gap, 5.6, dots)
            self.pdf.set_text_color(100, 100, 100)
            self.pdf.set_xy(num_x, y)
            self.pdf.cell(page_w, 5.6, page_text, align="R", new_x="LMARGIN", new_y="NEXT")
