#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Vietnamese Grade-10 Literature midterm revision PDF.

The script concatenates the Markdown chapters in ``docs/``, produces one editable
combined Markdown file, and renders a print-ready A4 PDF with embedded DejaVu
fonts (full Vietnamese diacritic coverage), automatic table of contents, page
numbers, headers, footers, tables, call-outs and monospaced mind maps.

Usage:
    python tools/build_pdf.py
    python tools/build_pdf.py --docs docs --out path/to/output.pdf

Dependencies (install into a virtual environment):
    pip install reportlab
"""
from __future__ import annotations

import argparse
import html
import os
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as canvaslib
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "tools" / "fonts"

PRIMARY = colors.HexColor("#14304F")
SECONDARY = colors.HexColor("#0F766E")
ACCENT = colors.HexColor("#B45309")
INK = colors.HexColor("#1F2937")
MUTED = colors.HexColor("#5B6472")
LIGHT = colors.HexColor("#EAF2F1")
PALE = colors.HexColor("#F5F7FA")
RULE = colors.HexColor("#CBD5E1")
WHITE = colors.white

PAGE_W, PAGE_H = A4
LEFT_M = 19 * mm
RIGHT_M = 17 * mm
TOP_M = 20 * mm
BOTTOM_M = 18 * mm
CONTENT_W = PAGE_W - LEFT_M - RIGHT_M


def register_fonts() -> None:
    fonts = {
        "DejaVu": "DejaVuSerif.ttf",
        "DejaVu-Bold": "DejaVuSerif-Bold.ttf",
        "DejaVu-Italic": "DejaVuSerif-Italic.ttf",
        "DejaVu-BoldItalic": "DejaVuSerif-BoldItalic.ttf",
        "DejaVuSans": "DejaVuSans.ttf",
        "DejaVuSans-Bold": "DejaVuSans-Bold.ttf",
        "DejaVuMono": "DejaVuMonoVN.ttf",
    }
    missing = [str(FONT_DIR / f) for f in fonts.values() if not (FONT_DIR / f).exists()]
    if missing:
        raise SystemExit("Missing font files:\n  " + "\n  ".join(missing))
    for name, filename in fonts.items():
        pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
    pdfmetrics.registerFontFamily(
        "DejaVu",
        normal="DejaVu",
        bold="DejaVu-Bold",
        italic="DejaVu-Italic",
        boldItalic="DejaVu-BoldItalic",
    )


def make_styles() -> dict:
    base = getSampleStyleSheet()
    s = {}
    s["Body"] = ParagraphStyle(
        "Body", parent=base["Normal"], fontName="DejaVu", fontSize=10.2,
        leading=15.2, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5,
        wordWrap="LTR", allowWidows=0, allowOrphans=0,
    )
    s["BodyL"] = ParagraphStyle(
        "BodyL", parent=s["Body"], alignment=TA_LEFT,
    )
    s["H1"] = ParagraphStyle(
        "H1", parent=base["Heading1"], fontName="DejaVuSans-Bold",
        fontSize=17.5, leading=22, textColor=PRIMARY, spaceBefore=18,
        spaceAfter=10, keepWithNext=1,
    )
    s["H2"] = ParagraphStyle(
        "H2", parent=base["Heading2"], fontName="DejaVuSans-Bold",
        fontSize=13, leading=17, textColor=SECONDARY, spaceBefore=13,
        spaceAfter=6, keepWithNext=1,
    )
    s["H3"] = ParagraphStyle(
        "H3", parent=base["Heading3"], fontName="DejaVuSans-Bold",
        fontSize=11.2, leading=15, textColor=PRIMARY, spaceBefore=10,
        spaceAfter=4, keepWithNext=1,
    )
    s["H4"] = ParagraphStyle(
        "H4", parent=base["Heading4"], fontName="DejaVu-Bold",
        fontSize=10.3, leading=14, textColor=ACCENT, spaceBefore=8,
        spaceAfter=3, keepWithNext=1,
    )
    s["Bullet"] = ParagraphStyle(
        "Bullet", parent=s["BodyL"], leftIndent=13, firstLineIndent=-9,
        spaceAfter=2.5, fontSize=9.9, leading=14.2, bulletFontName="DejaVu", bulletFontSize=8.5,
    )
    s["Number"] = ParagraphStyle(
        "Number", parent=s["Bullet"], leftIndent=17, firstLineIndent=-13,
    )
    s["Quote"] = ParagraphStyle(
        "Quote", parent=s["BodyL"], fontName="DejaVu-Italic", fontSize=10,
        leading=14.8, textColor=PRIMARY, leftIndent=10, rightIndent=8,
        spaceBefore=0, spaceAfter=0,
    )
    s["Code"] = ParagraphStyle(
        "Code", parent=base["Code"], fontName="DejaVuMono", fontSize=7.7,
        leading=10.4, textColor=INK, backColor=PALE, borderPadding=7,
        borderWidth=0.5, borderColor=RULE, spaceBefore=5, spaceAfter=8,
    )
    s["Tbl"] = ParagraphStyle(
        "Tbl", parent=s["BodyL"], fontSize=8.6, leading=11.8, spaceAfter=0,
        alignment=TA_LEFT,
    )
    s["TblHead"] = ParagraphStyle(
        "TblHead", parent=s["Tbl"], fontName="DejaVuSans-Bold",
        fontSize=8.5, leading=11.5, textColor=WHITE,
    )
    s["CoverTitle"] = ParagraphStyle(
        "CoverTitle", parent=s["H1"], fontSize=25, leading=31,
        alignment=TA_CENTER, textColor=PRIMARY, spaceBefore=0, spaceAfter=10,
    )
    s["CoverSub"] = ParagraphStyle(
        "CoverSub", parent=s["Body"], fontSize=13, leading=19,
        alignment=TA_CENTER, textColor=SECONDARY, spaceAfter=7,
    )
    s["CoverSmall"] = ParagraphStyle(
        "CoverSmall", parent=s["Body"], fontSize=9.6, leading=14,
        alignment=TA_CENTER, textColor=MUTED,
    )
    s["TOCTitle"] = ParagraphStyle(
        "TOCTitle", parent=s["H1"], fontSize=19, alignment=TA_CENTER,
        spaceBefore=4, spaceAfter=14,
    )
    return s


STY = make_styles()


def _find_closing(text: str, start: int, double: bool) -> int | None:
    """Return index of the next emphasis delimiter, skipping escaped characters."""
    i = start
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            i += 2
            continue
        if text[i] == "*":
            if double and i + 1 < len(text) and text[i + 1] == "*":
                return i
            if not double and not (i + 1 < len(text) and text[i + 1] == "*") \
                    and not (i > 0 and text[i - 1] == "*"):
                return i
        i += 1
    return None


def _emphasis(text: str) -> str:
    out: list[str] = []
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == "\\" and i + 1 < n and text[i + 1] in "*_":
            out.append(text[i + 1])
            i += 2
            continue
        if c == "*":
            double = i + 1 < n and text[i + 1] == "*"
            size = 2 if double else 1
            close = _find_closing(text, i + size, double)
            if close is not None:
                inner = _emphasis(text[i + size:close])
                out.append(("<b>" if double else "<i>") + inner + ("</b>" if double else "</i>"))
                i = close + size
                continue
        out.append(c)
        i += 1
    return "".join(out)


def inline_markup(raw: str) -> str:
    """Escape HTML then translate a safe subset of Markdown inline syntax.

    A small recursive delimiter parser is used instead of flat regexes so that
    nested emphasis and stray asterisks (e.g. "1*" in the matrix) never produce
    unbalanced <b>/<i> tags in ReportLab paragraphs.
    """
    text = html.escape(raw, quote=False)
    text = text.replace("&lt;br&gt;", "<br/>").replace("&lt;br/&gt;", "<br/>")

    codes: list[str] = []

    def protect_code(match):
        codes.append(
            '<font face="DejaVuMono" size="8.4" color="#0F766E">%s</font>' % match.group(1)
        )
        return "\ue000%d\ue001" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", protect_code, text)

    links: list[str] = []

    def protect_link(match):
        links.append(
            '<link href="%s" color="#0F766E">%s</link>' % (match.group(2), match.group(1))
        )
        return "\ue002%d\ue003" % (len(links) - 1)

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", protect_link, text)
    text = _emphasis(text)
    text = re.sub(r"\ue000(\d+)\ue001", lambda m: codes[int(m.group(1))], text)
    text = re.sub(r"\ue002(\d+)\ue003", lambda m: links[int(m.group(1))], text)
    return text

def is_table_sep(line: str) -> bool:
    stripped = line.strip().strip("|").strip()
    if not stripped or "|" not in line:
        return False
    return bool(re.fullmatch(r"[\s:\-\|]+", stripped))


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)]


def build_table(rows: list[list[str]]) -> Table:
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    # Estimate column widths from the longest content in each column.
    weights = []
    for col in range(ncol):
        longest = max(
            (len(re.sub(r"[\*\`\[\]\(\)]", "", rows[r][col])) for r in range(min(len(rows), 14))),
            default=6,
        )
        weights.append(max(7.0, min(46.0, float(longest) ** 0.72)))
    total = sum(weights)
    avail = CONTENT_W - 0.0
    widths = [avail * w / total for w in weights]
    # Give narrow columns a useful minimum, then re-normalize.
    min_w = 27 if ncol <= 6 else 21
    widths = [max(min_w, w) for w in widths]
    scale = avail / sum(widths)
    widths = [w * scale for w in widths]

    data = []
    for ridx, row in enumerate(rows):
        style = STY["TblHead"] if ridx == 0 else STY["Tbl"]
        data.append([
            Paragraph(inline_markup(cell) or "&nbsp;", style) for cell in row
        ])
    tbl = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, SECONDARY),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]
    for r in range(1, len(data)):
        if r % 2 == 0:
            commands.append(("BACKGROUND", (0, r), (-1, r), PALE))
    tbl.setStyle(TableStyle(commands))
    return tbl


def parse_markdown(text: str) -> list:
    lines = text.splitlines()
    story: list = []
    i = 0
    blank_pending = False

    def add_paragraph(chunks: list[str]) -> None:
        joined = " ".join(c.strip() for c in chunks if c.strip())
        if joined:
            story.append(Paragraph(inline_markup(joined), STY["Body"]))

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if stripped == "<!-- pagebreak -->" or stripped == "\\newpage":
            story.append(PageBreak())
            i += 1
            continue
        if stripped.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            story.append(Preformatted("\n".join(code), STY["Code"]))
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and is_table_sep(lines[i + 1]):
            rows = [split_table_row(line)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_table_row(lines[i]))
                i += 1
            story.append(build_table(rows))
            story.append(Spacer(1, 7))
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            heading = m.group(2).strip()
            story.append(Paragraph(inline_markup(heading), STY["H%d" % level]))
            blank_pending = False
            i += 1
            continue
        if re.fullmatch(r"(\-\s*){3,}|(\*\s*){3,}|(_\s*){3,}", stripped):
            story.append(Spacer(1, 3))
            story.append(HRFlowable(width="100%", thickness=0.6, color=RULE))
            story.append(Spacer(1, 5))
            i += 1
            continue
        if stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            cell = Paragraph(inline_markup(" ".join(quote)), STY["Quote"])
            callout = Table([[cell]], colWidths=[CONTENT_W], hAlign="LEFT")
            callout.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("LINEBEFORE", (0, 0), (0, 0), 3, SECONDARY),
                ("LEFTPADDING", (0, 0), (-1, -1), 11),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(callout)
            story.append(Spacer(1, 8))
            continue
        list_match = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", raw)
        if list_match:
            while i < len(lines):
                lm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", lines[i])
                if not lm:
                    break
                indent = len(lm.group(1))
                marker = lm.group(2)
                content = lm.group(3).strip()
                bullet = "•" if marker in "-*+" else marker
                style = STY["Bullet"] if marker in "-*+" else STY["Number"]
                style = ParagraphStyle(
                    "list_%d_%d" % (id(style), indent), parent=style,
                    leftIndent=13 + indent * 3.2,
                    firstLineIndent=-9 if marker in "-*+" else -13,
                )
                story.append(
                    Paragraph(inline_markup(content), style, bulletText=bullet)
                )
                i += 1
            story.append(Spacer(1, 3))
            continue
        if not stripped:
            blank_pending = True
            i += 1
            continue
        # Ordinary paragraph: join wrapped lines.
        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            ns = nxt.strip()
            if (not ns or ns.startswith("#") or ns.startswith(">") or ns.startswith("|")
                    or ns.startswith("```") or re.match(r"^(\s*)([-*+]|\d+[.)])\s+", nxt)
                    or re.fullmatch(r"(\-\s*){3,}|(\*\s*){3,}|(_\s*){3,}", ns)
                    or ns.startswith("<!--")):
                break
            para.append(nxt)
            i += 1
        add_paragraph(para)
        if blank_pending:
            story.append(Spacer(1, 2))
        blank_pending = False
    return story


class NumberedCanvas(canvaslib.Canvas):
    """Canvas that knows the final page count and draws the running furniture."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_furniture(total)
            super().showPage()
        super().save()

    def draw_furniture(self, total):
        page = self._pageNumber
        w, h = PAGE_W, PAGE_H
        if page == 1:
            self.setFillColor(PRIMARY)
            self.rect(0, h - 118, w, 118, stroke=0, fill=1)
            self.setFillColor(SECONDARY)
            self.rect(0, h - 122, w, 4, stroke=0, fill=1)
            self.setFillColor(WHITE)
            self.setFont("DejaVuSans-Bold", 11)
            self.drawCentredString(w / 2, h - 40, "NĂM HỌC 2026 – 2027   •   NGỮ VĂN 10")
            self.setFont("DejaVuSans", 9.2)
            self.drawCentredString(
                w / 2, h - 62,
                "Kết nối tri thức với cuộc sống  |  Kiểm tra giữa học kì I  |  90 phút",
            )
            self.setFillColor(ACCENT)
            self.rect(0, 0, w, 7, stroke=0, fill=1)
            self.setFillColor(MUTED)
            self.setFont("DejaVu", 8.2)
            self.drawCentredString(w / 2, 22, "Ấn bản ôn tập • Tài liệu học tập nội bộ • Trang %d / %d" % (page, total))
            return
        self.setStrokeColor(RULE)
        self.setLineWidth(0.5)
        self.line(LEFT_M, h - 15 * mm, w - RIGHT_M, h - 15 * mm)
        self.setFillColor(MUTED)
        self.setFont("DejaVu", 7.8)
        self.drawString(LEFT_M, h - 13.2 * mm, "ĐỀ CƯƠNG GIỮA KÌ I • NGỮ VĂN 10 • KNTT")
        self.drawRightString(w - RIGHT_M, h - 13.2 * mm, "2026 – 2027")
        self.line(LEFT_M, 14 * mm, w - RIGHT_M, 14 * mm)
        self.drawString(LEFT_M, 10.5 * mm, "Ôn tập theo ma trận & bản đặc tả chính thức")
        self.drawRightString(w - RIGHT_M, 10.5 * mm, "Trang %d / %d" % (page, total))


class DocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            LEFT_M, BOTTOM_M, CONTENT_W, PAGE_H - TOP_M - BOTTOM_M,
            id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        self.addPageTemplates([PageTemplate(id="main", frames=[frame])])

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            name = flowable.style.name
            if name in ("H1", "H2", "H3"):
                level = {"H1": 0, "H2": 1, "H3": 2}[name]
                self.notify("TOCEntry", (level, flowable.getPlainText(), self.page))


def cover_story() -> list:
    return [
        Spacer(1, 82),
        Paragraph("ĐỀ CƯƠNG ÔN TẬP", STY["CoverTitle"]),
        Paragraph("KIỂM TRA GIỮA HỌC KÌ I", STY["CoverTitle"]),
        Spacer(1, 8),
        Paragraph("Môn Ngữ văn 10 – Bộ sách Kết nối tri thức với cuộc sống", STY["CoverSub"]),
        Paragraph("Năm học 2026 – 2027  •  Thời gian làm bài 90 phút", STY["CoverSub"]),
        Spacer(1, 16),
        Table(
            [[Paragraph(
                "Phân tích ma trận • Hệ thống tri thức thần thoại • Toàn bộ chương trình HK1 • "
                "22 chỉ báo năng lực • 5 đề mô phỏng + 1 đề dự phòng (mỗi đề 11 câu) • Ngân hàng 72 câu có đáp án • "
                "Bài viết mẫu & rubric • Lịch ôn 14 ngày",
                STY["CoverSub"],
            )]],
            colWidths=[CONTENT_W * 0.86],
            hAlign="CENTER",
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                ("BOX", (0, 0), (-1, -1), 0.8, SECONDARY),
                ("LEFTPADDING", (0, 0), (-1, -1), 14),
                ("RIGHTPADDING", (0, 0), (-1, -1), 14),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ]),
        ),
        Spacer(1, 26),
        Paragraph(
            "Biên soạn từ tệp <b>MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx</b> "
            "(gồm Ma trận và Bản đặc tả) kết hợp nghiên cứu sách giáo khoa, chương trình GDPT 2018 "
            "và các đề kiểm tra giữa kì I cùng bộ sách.",
            STY["CoverSmall"],
        ),
        Spacer(1, 8),
        Paragraph(
            "LƯU Ý: Tệp nguồn của nhà trường không kèm đề thi và đáp án. Mọi đề trong tài liệu này "
            "là đề mô phỏng được biên soạn để ôn tập, không phải đề chính thức.",
            ParagraphStyle("CoverNote", parent=STY["CoverSmall"], textColor=ACCENT),
        ),
        PageBreak(),
    ]


def toc_story() -> list:
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOC0", fontName="DejaVuSans-Bold", fontSize=10.5, leading=17,
            firstLineIndent=0, leftIndent=6, textColor=PRIMARY, spaceBefore=7,
        ),
        ParagraphStyle(
            "TOC1", fontName="DejaVu", fontSize=9.4, leading=14,
            firstLineIndent=0, leftIndent=22, textColor=INK,
        ),
        ParagraphStyle(
            "TOC2", fontName="DejaVu", fontSize=8.8, leading=12.5,
            firstLineIndent=0, leftIndent=40, textColor=MUTED,
        ),
    ]
    toc.dotsMinLevel = 0
    return [
        Paragraph("MỤC LỤC", STY["TOCTitle"]),
        Paragraph(
            "Số trang được cập nhật tự động khi tạo PDF. Dùng bản PDF để in; dùng bản Markdown "
            "trong thư mục <font face='DejaVuMono' size='8.4'>docs/</font> để chỉnh sửa nội dung.",
            ParagraphStyle("TOCNote", parent=STY["CoverSmall"], fontSize=9.2),
        ),
        Spacer(1, 14),
        toc,
        PageBreak(),
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default=str(ROOT / "docs"))
    ap.add_argument("--out", default=str(ROOT / "De-cuong-on-tap-GK1-Ngu-van-10-2026-2027.pdf"))
    ap.add_argument("--combined", default=str(ROOT / "DE-CUONG-TONG-HOP-GIUA-KI-1-NGU-VAN-10-2026-2027.md"))
    args = ap.parse_args()

    register_fonts()
    docs_dir = Path(args.docs)
    files = sorted(docs_dir.glob("*.md"))
    if not files:
        raise SystemExit("No Markdown chapters found in %s" % docs_dir)
    chapters = []
    for f in files:
        chapters.append(f.read_text(encoding="utf-8").strip())
    combined = "# ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I – NGỮ VĂN 10 (2026–2027)\n\n" \
        + "\n\n".join(chapters) + "\n"
    Path(args.combined).write_text(combined, encoding="utf-8")

    story = cover_story() + toc_story() + parse_markdown("\n\n".join(chapters))
    doc = DocTemplate(
        args.out, pagesize=A4, title="Đề cương ôn tập giữa kì I Ngữ văn 10 (2026-2027)",
        author="Tài liệu ôn tập Ngữ văn 10 – Kết nối tri thức",
        subject="Ma trận, bản đặc tả, đề mô phỏng và đáp án",
        leftMargin=LEFT_M, rightMargin=RIGHT_M, topMargin=TOP_M, bottomMargin=BOTTOM_M,
    )
    doc.multiBuild(story, canvasmaker=NumberedCanvas)
    size = os.path.getsize(args.out)
    print("Built %s (%.1f KB) from %d chapters." % (args.out, size / 1024, len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
