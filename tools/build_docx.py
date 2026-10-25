#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh bản in DOCX (A4, Times New Roman 13) từ các tệp Markdown trong de-cuong-on-tap/.

Cách dùng:
    python3 tools/build_docx.py

Kết quả:
    xuat-ban/De-cuong-on-tap-GK1-Ngu-van-10.docx   (toàn bộ đề cương)
    xuat-ban/De-minh-hoa-va-dap-an-GK1.docx        (chỉ đề + đáp án, để in làm bài)
"""

import os
import re
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "de-cuong-on-tap")
OUT = os.path.join(ROOT, "xuat-ban")

FONT = "Times New Roman"
FONT_MONO = "Consolas"
BODY_SIZE = 13
TABLE_SIZE = 10.5
MONO_SIZE = 8

ACCENT = RGBColor(0x1F, 0x3B, 0x73)      # xanh đậm
ACCENT2 = RGBColor(0x8B, 0x1A, 0x1A)     # đỏ nâu
GREY = RGBColor(0x44, 0x44, 0x44)

# Thay các ký tự emoji/ký hiệu khó in bằng ký hiệu an toàn với mọi font
SYMBOL_MAP = {
    "\U0001F4CC": "►",   # 📌
    "\u26A0": "▲",       # ⚠
    "\u2705": "✓",       # ✅
    "\u2B1C": "☐",       # ⬜
    "\U0001F4CA": "►",   # 📊
}

FILES = [
    ("00-tong-quan-va-chien-luoc.md", "PHẦN 1"),
    ("01-nen-tang-the-loai-truyen-va-than-thoai.md", "PHẦN 2"),
    ("02-tac-pham-trong-tam.md", "PHẦN 3"),
    ("03-de-minh-hoa-va-dap-an.md", "PHẦN 4"),
    ("04-ky-nang-doc-hieu-va-viet.md", "PHẦN 5"),
    ("05-he-thong-hoa-de-nho.md", "PHẦN 6"),
    ("06-ngan-hang-trac-nghiem.md", "PHẦN 7"),
    ("07-de-thi-thu-nang-cao.md", "PHẦN 8"),
]

EXAM_ONLY = ["03-de-minh-hoa-va-dap-an.md", "07-de-thi-thu-nang-cao.md"]


# ----------------------------------------------------------------------------- utils
def clean(text: str) -> str:
    for k, v in SYMBOL_MAP.items():
        text = text.replace(k, v)
    return text.replace("\u00a0", " ")


def set_run_font(run, name=FONT, size=None, bold=None, italic=None, color=None):
    run.font.name = name
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(attr), name)


TOKEN_RE = re.compile(r"(\*\*.+?\*\*|`.+?`|(?<!\*)\*(?!\s)[^*]+?(?<!\s)\*)")


def add_inline(par, text, size=BODY_SIZE, base_bold=False, base_italic=False, color=None,
               mono_size=None):
    """Thêm text có **đậm**, *nghiêng*, `code` vào paragraph."""
    text = clean(text)
    pos = 0
    for m in TOKEN_RE.finditer(text):
        if m.start() > pos:
            r = par.add_run(text[pos:m.start()])
            set_run_font(r, FONT, size, base_bold, base_italic, color)
        tok = m.group(0)
        if tok.startswith("**"):
            r = par.add_run(tok[2:-2])
            set_run_font(r, FONT, size, True, base_italic, color)
        elif tok.startswith("`"):
            r = par.add_run(tok[1:-1])
            set_run_font(r, FONT_MONO, mono_size or max(8, size - 2), base_bold, base_italic, color)
        else:
            r = par.add_run(tok[1:-1])
            set_run_font(r, FONT, size, base_bold, True, color)
        pos = m.end()
    if pos < len(text):
        r = par.add_run(text[pos:])
        set_run_font(r, FONT, size, base_bold, base_italic, color)


def shade(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def set_cell_margins(table, top=40, bottom=40, left=80, right=80):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for tag, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{tag}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)


def no_split_rows(table):
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        el = OxmlElement("w:cantSplit")
        trPr.append(el)


def layout_table(table, parsed, text_width_cm=16.2):
    """Chia độ rộng cột theo độ dài nội dung, tổng đúng bề rộng trang."""
    ncols = len(parsed[0])
    weights = []
    for c in range(ncols):
        longest = max(len(re.sub(r"[*`]", "", row[c])) for row in parsed)
        weights.append(max(6, min(longest, 90)))
    total = float(sum(weights))
    widths = [max(1.5, text_width_cm * w / total) for w in weights]
    scale = text_width_cm / sum(widths)
    widths = [w * scale for w in widths]

    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for ci, w in enumerate(widths):
        table.columns[ci].width = Cm(w)
        for cell in table.columns[ci].cells:
            cell.width = Cm(w)


def add_bottom_border(par, color="1F3B73", size=8):
    pPr = par._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), color)
    borders.append(bottom)
    pPr.append(borders)


def keep_with_next(par):
    pPr = par._p.get_or_add_pPr()
    el = OxmlElement("w:keepNext")
    pPr.append(el)


def add_page_number_footer(section, title):
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(title + "  ·  Trang ")
    set_run_font(r, FONT, 9, color=GREY)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run_in = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "18")
    rpr.append(sz)
    run_in.append(rpr)
    t = OxmlElement("w:t")
    t.text = "1"
    run_in.append(t)
    fld.append(run_in)
    p._p.append(fld)


# ----------------------------------------------------------------------------- parsing
def parse_blocks(lines):
    """Chia markdown thành các block: heading, paragraph, list, table, code, quote, hr."""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        raw = line.rstrip("\n")

        if not raw.strip():
            i += 1
            continue

        # code fence
        if raw.strip().startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i].rstrip("\n"))
                i += 1
            i += 1
            blocks.append(("code", buf))
            continue

        # horizontal rule
        if re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", raw):
            blocks.append(("hr", raw))
            i += 1
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", raw)
        if m:
            blocks.append(("h%d" % len(m.group(1)), m.group(2).strip()))
            i += 1
            continue

        # table
        if raw.lstrip().startswith("|"):
            rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            blocks.append(("table", rows))
            continue

        # blockquote
        if raw.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]).rstrip())
                i += 1
            blocks.append(("quote", buf))
            continue

        # list
        if re.match(r"^\s*([-*+]|\d+[.)])\s+", raw):
            items = []
            while i < n and re.match(r"^\s*([-*+]|\d+[.)])\s+", lines[i]) and not lines[
                i
            ].lstrip().startswith("|"):
                items.append(lines[i].rstrip("\n"))
                i += 1
            blocks.append(("list", items))
            continue

        # paragraph (gộp các dòng liền nhau)
        buf = [raw]
        i += 1
        while i < n:
            nxt = lines[i]
            s = nxt.strip()
            if (
                not s
                or s.startswith("#")
                or s.startswith("|")
                or s.startswith(">")
                or s.startswith("```")
                or re.match(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$", nxt)
                or re.match(r"^\s*([-*+]|\d+[.)])\s+", nxt)
            ):
                break
            buf.append(nxt.rstrip("\n"))
            i += 1
        blocks.append(("para", " ".join(x.strip() for x in buf)))
    return blocks


def split_table_row(row):
    row = row.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    cells = []
    buf = ""
    in_code = False
    for ch in row:
        if ch == "`":
            in_code = not in_code
            buf += ch
        elif ch == "|" and not in_code:
            cells.append(buf.strip())
            buf = ""
        else:
            buf += ch
    cells.append(buf.strip())
    return cells


def is_separator(cells):
    return all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cells if c != "")


# ----------------------------------------------------------------------------- render
class Builder:
    def __init__(self, title, subtitle):
        self.doc = Document()
        self.title = title
        self.subtitle = subtitle
        self.first_h1 = True
        self._setup()

    def _setup(self):
        doc = self.doc
        sec = doc.sections[0]
        sec.page_height = Cm(29.7)
        sec.page_width = Cm(21)
        sec.top_margin = Cm(2.0)
        sec.bottom_margin = Cm(2.0)
        sec.left_margin = Cm(2.8)
        sec.right_margin = Cm(2.0)

        style = doc.styles["Normal"]
        style.font.name = FONT
        style.font.size = Pt(BODY_SIZE)
        pf = style.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(5)
        pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
        pf.line_spacing = 1.18
        rpr = style.element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.append(rfonts)
        for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            rfonts.set(qn(attr), FONT)

    # ---- cover
    def cover(self, lines):
        doc = self.doc
        for _ in range(3):
            doc.add_paragraph()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("ĐỀ CƯƠNG ÔN TẬP")
        set_run_font(r, FONT, 30, True, color=ACCENT)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("GIỮA HỌC KÌ I")
        set_run_font(r, FONT, 26, True, color=ACCENT)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("NGỮ VĂN 10")
        set_run_font(r, FONT, 34, True, color=ACCENT2)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("Bộ sách Kết nối tri thức với cuộc sống")
        set_run_font(r, FONT, 15, False, True, GREY)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_bottom_border(p, "1F3B73", 12)

        for _ in range(2):
            doc.add_paragraph()

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("Năm học 2026 – 2027")
        set_run_font(r, FONT, 14, True)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("Thời gian làm bài: 90 phút")
        set_run_font(r, FONT, 13, color=GREY)

        for _ in range(3):
            doc.add_paragraph()

        for line in lines:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_inline(p, line, size=11, color=GREY)

        doc.add_page_break()

    # ---- toc
    def toc(self, entries):
        doc = self.doc
        p = doc.add_paragraph()
        r = p.add_run("MỤC LỤC")
        set_run_font(r, FONT, 18, True, color=ACCENT)
        add_bottom_border(p)
        doc.add_paragraph()

        for level, text in entries:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(2)
            if level == 1:
                p.paragraph_format.space_before = Pt(8)
                add_inline(p, text, size=12.5, base_bold=True, color=ACCENT)
            else:
                p.paragraph_format.left_indent = Cm(0.8)
                add_inline(p, text, size=11.5)
        doc.add_page_break()

    # ---- blocks
    def heading(self, level, text):
        doc = self.doc
        text = clean(text)
        if level == 1:
            p = doc.add_paragraph()
            if self.first_h1:
                self.first_h1 = False
            else:
                p.paragraph_format.page_break_before = True
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(10)
            add_inline(p, text, size=19, base_bold=True, color=ACCENT)
            add_bottom_border(p, "1F3B73", 12)
            p.style = doc.styles["Heading 1"]
            for r in p.runs:
                set_run_font(r, FONT, 19, True, color=ACCENT)
        elif level == 2:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            add_inline(p, text, size=15, base_bold=True, color=ACCENT2)
            p.style = doc.styles["Heading 2"]
            for r in p.runs:
                set_run_font(r, FONT, 15, True, color=ACCENT2)
        elif level == 3:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            add_inline(p, text, size=13.5, base_bold=True, color=RGBColor(0x00, 0x33, 0x66))
            p.style = doc.styles["Heading 3"]
            for r in p.runs:
                set_run_font(r, FONT, 13.5, True, color=RGBColor(0x00, 0x33, 0x66))
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            add_inline(p, text, size=BODY_SIZE, base_bold=True)
        keep_with_next(p)

    def para(self, text, quote=False):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if quote:
            p.paragraph_format.left_indent = Cm(0.6)
            p.paragraph_format.right_indent = Cm(0.3)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            add_inline(p, text, size=12, base_italic=False, color=RGBColor(0x22, 0x22, 0x22))
            pPr = p._p.get_or_add_pPr()
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:color"), "auto")
            shd.set(qn("w:fill"), "F2F5FA")
            pPr.append(shd)
        else:
            add_inline(p, text)

    def list_block(self, items):
        for raw in items:
            m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", raw)
            indent, marker, content = m.group(1), m.group(2), m.group(3)
            level = len(indent) // 2
            p = self.doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(0.65 + 0.6 * level)
            p.paragraph_format.first_line_indent = Cm(-0.45)
            p.paragraph_format.space_after = Pt(2)
            if content.startswith("[ ]"):
                bullet = "☐ "
                content = content[3:].strip()
            elif content.startswith("[x]") or content.startswith("[X]"):
                bullet = "✓ "
                content = content[3:].strip()
            elif marker in "-*+":
                bullet = "• " if level == 0 else "– "
            else:
                bullet = marker + " "
            r = p.add_run(bullet)
            set_run_font(r, FONT, BODY_SIZE)
            add_inline(p, content)

    def code(self, lines):
        if not lines:
            return
        tbl = self.doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Cm(16.2)
        cell = tbl.cell(0, 0)
        cell.width = Cm(16.2)
        no_split_rows(tbl)
        shade(cell, "F7F7F4")
        cell.paragraphs[0].text = ""
        for idx, line in enumerate(lines):
            p = cell.paragraphs[0] if idx == 0 else cell.add_paragraph()
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            r = p.add_run(line if line else " ")
            set_run_font(r, FONT_MONO, MONO_SIZE)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(2)

    def quote_block(self, lines):
        text = " ".join(x.strip() for x in lines if x.strip())
        if not text:
            return
        # Tách các dòng có "- " thành list để giữ cấu trúc
        if text.count(" - ") > 2 or re.search(r"(?:\A| - )\d+\.", text):
            self.para(text, quote=True)
        else:
            self.para(text, quote=True)

    def table(self, rows):
        parsed = [split_table_row(r) for r in rows]
        parsed = [c for c in parsed if not is_separator(c)]
        if not parsed:
            return
        ncols = max(len(c) for c in parsed)
        parsed = [c + [""] * (ncols - len(c)) for c in parsed]

        tbl = self.doc.add_table(rows=len(parsed), cols=ncols)
        tbl.style = "Table Grid"
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_cell_margins(tbl)
        layout_table(tbl, parsed)
        no_split_rows(tbl)

        for ri, cells in enumerate(parsed):
            for ci, text in enumerate(cells):
                cell = tbl.cell(ri, ci)
                cell.text = ""
                p = cell.paragraphs[0]
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.line_spacing = 1.05
                size = TABLE_SIZE if ncols <= 5 else max(9, TABLE_SIZE - 1)
                if ri == 0:
                    add_inline(p, text, size=size, base_bold=True,
                               color=RGBColor(0xFF, 0xFF, 0xFF))
                    shade(cell, "1F3B73")
                else:
                    add_inline(p, text, size=size)
                    if ri % 2 == 0:
                        shade(cell, "F4F6FA")
        sp = self.doc.add_paragraph()
        sp.paragraph_format.space_after = Pt(2)

    def hr(self):
        p = self.doc.add_paragraph()
        add_bottom_border(p, "BBBBBB", 6)
        p.paragraph_format.space_after = Pt(6)

    def render_file(self, path):
        with open(path, encoding="utf8") as f:
            lines = f.readlines()
        for kind, payload in parse_blocks(lines):
            if kind == "h1":
                self.heading(1, payload)
            elif kind == "h2":
                self.heading(2, payload)
            elif kind == "h3":
                self.heading(3, payload)
            elif kind in ("h4", "h5", "h6"):
                self.heading(4, payload)
            elif kind == "para":
                self.para(payload)
            elif kind == "quote":
                self.quote_block(payload)
            elif kind == "list":
                self.list_block(payload)
            elif kind == "table":
                self.table(payload)
            elif kind == "code":
                self.code(payload)
            elif kind == "hr":
                self.hr()

    def save(self, path):
        sec = self.doc.sections[0]
        add_page_number_footer(sec, self.title)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.doc.save(path)
        return path


def collect_toc(paths):
    entries = []
    for p in paths:
        with open(p, encoding="utf8") as f:
            for line in f:
                m = re.match(r"^(#{1,2})\s+(.*)$", line)
                if m:
                    entries.append((len(m.group(1)), clean(m.group(2).strip())))
    return entries


def build(file_specs, out_name, title, cover_lines, with_toc=True):
    b = Builder(title, "")
    b.cover(cover_lines)
    paths = [os.path.join(SRC, f) for f, _ in file_specs]
    if with_toc:
        b.toc(collect_toc(paths))
    for p in paths:
        b.render_file(p)
    out = b.save(os.path.join(OUT, out_name))
    print(f"  ✓ {out}  ({os.path.getsize(out) / 1024:.0f} KB)")
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    print("Đang sinh bản in DOCX…")
    build(
        FILES,
        "De-cuong-on-tap-GK1-Ngu-van-10.docx",
        "Đề cương ôn tập Giữa kì I – Ngữ văn 10",
        [
            "Biên soạn bám sát **Ma trận – Bản đặc tả** của nhà trường",
            "(tệp: *MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027*)",
            "",
            "8 phần · 11 câu hỏi minh hoạ kèm đáp án · 80 câu trắc nghiệm",
            "3 đề thi thử · hệ thống ghi nhớ · kĩ năng làm bài",
        ],
    )

    exam_specs = [(f, "") for f in EXAM_ONLY]
    build(
        exam_specs,
        "De-minh-hoa-va-dap-an-GK1.docx",
        "Đề minh hoạ & đáp án – Giữa kì I Ngữ văn 10",
        [
            "3 đề minh hoạ đầy đủ **11 câu / 10 điểm / 90 phút**",
            "Ngữ liệu **ngoài sách giáo khoa** · đáp án chi tiết · thang điểm",
            "",
            "Dùng để **in và làm bài** trước khi thi",
        ],
    )
    print("Xong.")


if __name__ == "__main__":
    sys.exit(main())
