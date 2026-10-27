#!/usr/bin/env python3
"""Build the printable Vietnamese revision guide from the checked-in Markdown.

Usage: python tools/build_pdf.py
The PDF is intentionally checked in as the user-facing deliverable.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

from markdown_it import MarkdownIt
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    BaseDocTemplate, CondPageBreak, Flowable, Frame, LongTable, PageBreak,
    PageTemplate, Paragraph, Spacer, TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'de-cuong'
FONTS = ROOT / 'fonts'
OUTPUT = ROOT / 'DE-CUONG-ON-TAP-NGU-VAN-10-GIUA-KI-I-2026-2027.pdf'
FILES = [CONTENT / name for name in (
    '01-nen-tang.md', '02-ky-nang-va-ghi-nho.md',
    '03-nam-de-luyen.md', '04-dap-an-va-bai-viet.md',
)]
PAGE_W, PAGE_H = A4
LEFT, RIGHT, TOP, BOTTOM = 49, 49, 56, 54
WIDTH = PAGE_W - LEFT - RIGHT
HEIGHT = PAGE_H - TOP - BOTTOM
NAVY = colors.HexColor('#142f43')
INK = colors.HexColor('#243745')
TEAL = colors.HexColor('#147b75')
GOLD = colors.HexColor('#d8aa55')
PALE = colors.HexColor('#eaf4f1')
MIST = colors.HexColor('#f3f6f7')
GRAY = colors.HexColor('#647682')
WHITE = colors.white


def register_fonts() -> None:
    for name in ('DejaVuSans', 'DejaVuSans-Bold', 'DejaVuSerif', 'DejaVuSerif-Bold'):
        pdfmetrics.registerFont(TTFont(name, str(FONTS / f'{name}.ttf')))
    # The distributed set has regular/bold; use these as legible fallbacks for italic.
    pdfmetrics.registerFontFamily('DejaVuSerif', normal='DejaVuSerif', bold='DejaVuSerif-Bold',
                                  italic='DejaVuSerif', boldItalic='DejaVuSerif-Bold')
    pdfmetrics.registerFontFamily('DejaVuSans', normal='DejaVuSans', bold='DejaVuSans-Bold',
                                  italic='DejaVuSans', boldItalic='DejaVuSans-Bold')


def make_styles() -> dict[str, ParagraphStyle]:
    body = ParagraphStyle('BodyVN', fontName='DejaVuSerif', fontSize=10.0, leading=15.2,
                          textColor=INK, alignment=TA_LEFT, spaceAfter=7.0,
                          allowWidows=0, allowOrphans=0, splitLongWords=True)
    return {
        'body': body,
        'small': ParagraphStyle('SmallVN', parent=body, fontName='DejaVuSans',
                                fontSize=8.5, leading=12.6, textColor=GRAY, spaceAfter=8),
        'chapter': ParagraphStyle('ChapterVN', fontName='DejaVuSans-Bold', fontSize=18.5,
                                  leading=26, textColor=NAVY, spaceBefore=4, spaceAfter=15,
                                  keepWithNext=True),
        'h2': ParagraphStyle('Heading2VN', fontName='DejaVuSans-Bold', fontSize=12.8,
                             leading=18, textColor=TEAL, spaceBefore=12, spaceAfter=7,
                             keepWithNext=True),
        'h3': ParagraphStyle('Heading3VN', fontName='DejaVuSans-Bold', fontSize=11,
                             leading=15.5, textColor=NAVY, spaceBefore=10, spaceAfter=6,
                             keepWithNext=True),
        'question': ParagraphStyle('QuestionVN', parent=body, fontName='DejaVuSans',
                                   fontSize=9.6, leading=14.2, spaceBefore=7, spaceAfter=4,
                                   keepWithNext=True),
        'options': ParagraphStyle('OptionsVN', parent=body, fontName='DejaVuSans',
                                  fontSize=9.2, leading=13.7, leftIndent=12, spaceAfter=6),
        'list': ParagraphStyle('ListVN', parent=body, leftIndent=19, firstLineIndent=-15,
                               spaceAfter=4.5),
        'table': ParagraphStyle('CellVN', fontName='DejaVuSans', fontSize=8.4,
                                leading=12, textColor=INK, spaceAfter=0,
                                splitLongWords=True, allowWidows=0, allowOrphans=0),
        'tablehead': ParagraphStyle('CellHeadVN', fontName='DejaVuSans-Bold', fontSize=8.4,
                                    leading=12, textColor=WHITE, spaceAfter=0,
                                    splitLongWords=True),
        'toc_title': ParagraphStyle('ContentsTitleVN', fontName='DejaVuSans-Bold',
                                    fontSize=22, leading=29, textColor=NAVY, spaceAfter=12),
        'toc_0': ParagraphStyle('TOC0', fontName='DejaVuSans-Bold', fontSize=10.4,
                                leading=15.5, textColor=NAVY, leftIndent=0, firstLineIndent=0,
                                rightIndent=25, spaceBefore=6),
        'toc_1': ParagraphStyle('TOC1', fontName='DejaVuSans', fontSize=8.6,
                                leading=12.6, textColor=GRAY, leftIndent=13, firstLineIndent=0,
                                rightIndent=25, spaceBefore=1),
    }


class Cover(Flowable):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = WIDTH, HEIGHT - 5

    def draw(self) -> None:
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(GOLD)
        c.roundRect(0, h - 31, 115, 3, 1.5, fill=1, stroke=0)
        c.setFont('DejaVuSans-Bold', 9)
        c.drawString(0, h - 57, 'HỌC LIỆU ÔN TẬP  •  2026–2027')
        c.setFillColor(WHITE)
        c.setFont('DejaVuSans-Bold', 33)
        c.drawString(0, h - 133, 'ĐỀ CƯƠNG')
        c.drawString(0, h - 181, 'NGỮ VĂN 10')
        c.setFillColor(GOLD)
        c.setFont('DejaVuSans-Bold', 24)
        c.drawString(0, h - 226, 'GIỮA KÌ I')
        c.setFillColor(colors.HexColor('#c8dcdf'))
        c.setFont('DejaVuSans', 13)
        c.drawString(0, h - 258, 'Kết nối tri thức với cuộc sống')

        # A calm, vector-only visual: three labeled study pillars.
        y = h - 355
        c.setStrokeColor(colors.HexColor('#426171'))
        c.line(0, y + 37, w, y + 37)
        c.line(0, y - 27, w, y - 27)
        for i, (number, label) in enumerate((('01', 'ĐỌC HIỂU'), ('02', 'VIẾT'), ('03', 'LUYỆN ĐỀ'))):
            x = i * (w / 3) + 4
            if i:
                c.setStrokeColor(colors.HexColor('#426171'))
                c.line(x - 13, y - 17, x - 13, y + 26)
            c.setFillColor(GOLD)
            c.setFont('DejaVuSans-Bold', 10)
            c.drawString(x, y + 13, number)
            c.setFillColor(WHITE)
            c.setFont('DejaVuSans-Bold', 10)
            c.drawString(x, y - 8, label)

        c.setFillColor(colors.HexColor('#254758'))
        c.roundRect(0, 97, w, 104, 9, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('DejaVuSans-Bold', 12)
        c.drawString(18, 173, '90 PHÚT  /  11 CÂU  /  10 ĐIỂM')
        c.setFont('DejaVuSans', 9.5)
        c.setFillColor(colors.HexColor('#d6e5e6'))
        c.drawString(18, 149, 'Bám ma trận và bản đặc tả gốc')
        c.drawString(18, 132, '05 đề luyện · 55 câu hỏi · đáp án và bài viết mẫu')
        c.drawString(18, 115, '50 thẻ tự kiểm · nguồn tham khảo có dẫn xuất xứ')
        c.setFont('DejaVuSans', 8.3)
        c.setFillColor(colors.HexColor('#c8dcdf'))
        c.drawString(0, 52, 'TÀI LIỆU LUYỆN TẬP • KHÔNG PHẢI ĐỀ/ĐÁP ÁN CHÍNH THỨC')
        c.setStrokeColor(GOLD)
        c.line(0, 38, w, 38)


def page_chrome(canvas, doc) -> None:
    canvas.saveState()
    if doc.page == 1:
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    else:
        canvas.setFillColor(GRAY)
        canvas.setFont('DejaVuSans-Bold', 7.3)
        canvas.drawString(LEFT, PAGE_H - 31, 'NGỮ VĂN 10  /  GIỮA KÌ I')
        canvas.setFont('DejaVuSans', 7.3)
        canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 31, 'KẾT NỐI TRI THỨC  •  2026–2027')
        canvas.setStrokeColor(colors.HexColor('#d8e4e5'))
        canvas.line(LEFT, PAGE_H - 39, PAGE_W - RIGHT, PAGE_H - 39)
        canvas.line(LEFT, 38, PAGE_W - RIGHT, 38)
        canvas.setFont('DejaVuSans', 7.3)
        canvas.setFillColor(GRAY)
        canvas.drawString(LEFT, 24, 'HỌC LIỆU LUYỆN TẬP • KHÔNG PHẢI ĐỀ CHÍNH THỨC')
        canvas.setFont('DejaVuSans-Bold', 8.2)
        canvas.setFillColor(TEAL)
        canvas.drawRightString(PAGE_W - RIGHT, 24, str(doc.page))
    canvas.restoreState()


class BookDocTemplate(BaseDocTemplate):
    def afterFlowable(self, flowable) -> None:
        if not hasattr(flowable, '_bookmark'):
            return
        key = flowable._bookmark
        label = flowable._outline_title
        level = flowable._outline_level
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(label, key, level=level, closed=False)
        self.notify('TOCEntry', (level, label, self.page, key))


def inline_markup(token) -> str:
    parts: list[str] = []
    links: list[bool] = []
    for child in token.children or []:
        typ = child.type
        if typ in ('text', 'code_inline'):
            parts.append(escape(unicodedata.normalize('NFC', child.content)))
        elif typ in ('softbreak', 'hardbreak'):
            parts.append('<br/>')
        elif typ == 'strong_open':
            parts.append('<b>')
        elif typ == 'strong_close':
            parts.append('</b>')
        elif typ == 'em_open':
            parts.append('<i>')
        elif typ == 'em_close':
            parts.append('</i>')
        elif typ == 'link_open':
            href = child.attrGet('href') or ''
            allowed = href.startswith(('https://', 'http://'))
            links.append(allowed)
            if allowed:
                parts.append(f'<link href={quoteattr(href)} color="#147b75">')
        elif typ == 'link_close':
            if links.pop():
                parts.append('</link>')
        elif typ == 'html_inline':
            parts.append(escape(child.content))
    return ''.join(parts)


def table_widths(header: list[str]) -> list[float]:
    n = len(header)
    if n == 2:
        weights = [0.27, 0.73]
    elif n == 3:
        if header[0] == 'Mã':
            weights = [0.10, 0.46, 0.44]
        elif header[0] == 'Nhóm':
            weights = [0.18, 0.70, 0.12]
        else:
            weights = [0.22, 0.39, 0.39]
    elif n == 4:
        weights = [0.17, 0.29, 0.29, 0.25]
    else:
        weights = [1 / n] * n
    return [WIDTH * weight for weight in weights]


def parse_table(tokens, start: int, styles):
    i = start + 1
    rows: list[list[str]] = []
    plain_header: list[str] = []
    current = None
    while i < len(tokens) and tokens[i].type != 'table_close':
        tok = tokens[i]
        if tok.type == 'tr_open':
            current = []
        elif tok.type == 'inline' and current is not None:
            current.append(inline_markup(tok))
            if not rows:
                plain_header.append(tok.content)
        elif tok.type == 'tr_close':
            rows.append(current)
            current = None
        i += 1
    if not rows:
        raise ValueError('Empty Markdown table')
    n = len(rows[0])
    if any(len(row) != n for row in rows):
        raise ValueError('Malformed Markdown table')
    cells = [[Paragraph(value, styles['tablehead'] if r == 0 else styles['table'])
              for value in row] for r, row in enumerate(rows)]
    table = LongTable(cells, colWidths=table_widths(plain_header), repeatRows=1,
                      splitByRow=1, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, MIST]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 0), (-1, 0), 0.4, NAVY),
        ('LINEBELOW', (0, 1), (-1, -1), 0.35, colors.HexColor('#e2e9ea')),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return table, i + 1


def markdown_flowables(text: str, styles):
    md = MarkdownIt('commonmark', {'breaks': True}).enable('table')
    tokens = md.parse(unicodedata.normalize('NFC', text))
    result = []
    list_stack: list[dict] = []
    pending_bullet = None
    counter = 0
    i = 0
    has_chapter = False
    while i < len(tokens):
        tok = tokens[i]
        if tok.type == 'heading_open':
            level = int(tok.tag[1])
            inline = tokens[i + 1]
            title = inline.content
            if level == 1:
                if has_chapter:
                    # Keep answers separate from printable papers; elsewhere avoid
                    # wasting a near-empty page at the end of a chapter.
                    if title.startswith('PHẦN 7'):
                        result.append(PageBreak())
                    else:
                        result.append(CondPageBreak(165))
                has_chapter = True
            # Each full practice paper begins on a fresh page for independent printing.
            if level == 2 and re.match(r'^ĐỀ [1-5] ·', title):
                result.append(PageBreak())
            style = styles['chapter' if level == 1 else 'h2' if level == 2 else 'h3']
            para = Paragraph(inline_markup(inline), style)
            if level <= 2:
                counter += 1
                para._bookmark = f'heading-{counter:03d}'
                para._outline_title = title
                para._outline_level = level - 1
            result.append(para)
            i += 3
            continue
        if tok.type == 'table_open':
            table, i = parse_table(tokens, i, styles)
            result.extend((table, Spacer(1, 9)))
            continue
        if tok.type in ('bullet_list_open', 'ordered_list_open'):
            list_stack.append({'kind': tok.type, 'next': int(tok.attrGet('start') or 1)})
        elif tok.type == 'list_item_open':
            top = list_stack[-1]
            if top['kind'] == 'ordered_list_open':
                pending_bullet = f"{top['next']}."
                top['next'] += 1
            else:
                pending_bullet = '•'
        elif tok.type in ('bullet_list_close', 'ordered_list_close'):
            list_stack.pop()
        elif tok.type == 'paragraph_open':
            inline = tokens[i + 1]
            raw = inline.content
            html = inline_markup(inline)
            if pending_bullet is not None:
                html = f'<font color="#147b75"><b>{escape(pending_bullet)}</b></font>  ' + html
                style = styles['list']
                pending_bullet = None
            elif raw.startswith('**Câu ') and re.match(r'\*\*Câu (?:[1-9]|10|11)\b', raw):
                style = styles['question']
            elif re.match(r'^A\. ', raw) and ('\nB. ' in raw or '\nC. ' in raw):
                style = styles['options']
            elif raw.startswith('*Nguồn tham khảo'):
                style = styles['small']
            else:
                style = styles['body']
            result.append(Paragraph(html, style))
            i += 3
            continue
        i += 1
    return result


def invariant_canvas(*args, **kwargs):
    """Keep PDF timestamps and identifiers stable for reproducible builds."""
    kwargs['invariant'] = 1
    return Canvas(*args, **kwargs)


def build() -> None:
    register_fonts()
    styles = make_styles()
    source = '\n\n'.join(path.read_text(encoding='utf-8') for path in FILES)
    doc = BookDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
                          topMargin=TOP, bottomMargin=BOTTOM,
                          title='Đề cương ôn tập Ngữ văn 10 giữa kì I 2026–2027',
                          author='Học liệu ôn tập theo ma trận gốc',
                          subject='Thần thoại, đọc hiểu và nghị luận phân tích tác phẩm truyện',
                          allowSplitting=1)
    frame = Frame(LEFT, BOTTOM, WIDTH, HEIGHT, leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0, id='page-frame')
    doc.addPageTemplates(PageTemplate(id='book', frames=[frame], onPage=page_chrome))
    toc = TableOfContents()
    toc.levelStyles = [styles['toc_0'], styles['toc_1']]
    toc.dotsMinLevel = 0
    story = [Cover(), PageBreak(), Paragraph('MỤC LỤC', styles['toc_title']),
             Paragraph('Chọn một mục để chuyển tới nội dung tương ứng.', styles['small']), toc,
             PageBreak()]
    story.extend(markdown_flowables(source, styles))
    doc.multiBuild(story, maxPasses=6, canvasmaker=invariant_canvas)
    print(f'Created: {OUTPUT}')


if __name__ == '__main__':
    build()
