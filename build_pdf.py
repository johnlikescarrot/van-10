from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, KeepTogether, HRFlowable)

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'ON_TAP_GIUA_KI_NGU_VAN_10_KNTT_2026-2027.md'
OUT = ROOT / 'CAM_NANG_ON_TAP_GIUA_KI_NGU_VAN_10_KNTT_2026-2027.pdf'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DV', FONT))
pdfmetrics.registerFont(TTFont('DV-Bold', BOLD))
pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-Bold', italic='DV', boldItalic='DV-Bold')

NAVY = colors.HexColor('#15345B')
TEAL = colors.HexColor('#168C8C')
INK = colors.HexColor('#263447')
MUTED = colors.HexColor('#66758A')
PALE = colors.HexColor('#EAF3F6')
PALEBLUE = colors.HexColor('#EDF2FA')
GOLD = colors.HexColor('#F2B84B')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle', fontName='DV-Bold', fontSize=27, leading=34,
                          textColor=colors.white, alignment=TA_LEFT, spaceAfter=9))
styles.add(ParagraphStyle(name='CoverSub', fontName='DV', fontSize=13, leading=20,
                          textColor=colors.HexColor('#DDEAF4'), alignment=TA_LEFT))
styles.add(ParagraphStyle(name='CoverInfo', fontName='DV-Bold', fontSize=10, leading=15,
                          textColor=colors.white))
styles.add(ParagraphStyle(name='H1x', fontName='DV-Bold', fontSize=18, leading=24,
                          textColor=NAVY, spaceBefore=4, spaceAfter=11, keepWithNext=True))
styles.add(ParagraphStyle(name='H2x', fontName='DV-Bold', fontSize=13.3, leading=18,
                          textColor=TEAL, spaceBefore=11, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name='H3x', fontName='DV-Bold', fontSize=10.5, leading=14.5,
                          textColor=NAVY, spaceBefore=8, spaceAfter=4, keepWithNext=True))
styles.add(ParagraphStyle(name='Bodyx', fontName='DV', fontSize=8.65, leading=13.1,
                          textColor=INK, spaceAfter=5.3, allowWidows=0, allowOrphans=0))
styles.add(ParagraphStyle(name='Bulletx', parent=styles['Bodyx'], leftIndent=12, firstLineIndent=-8,
                          bulletIndent=0, spaceAfter=3.2))
styles.add(ParagraphStyle(name='Quote', fontName='DV', fontSize=8.8, leading=13.4,
                          textColor=NAVY, leftIndent=7, rightIndent=7, spaceBefore=5, spaceAfter=7,
                          backColor=PALE, borderColor=TEAL, borderWidth=0.7, borderPadding=7))
styles.add(ParagraphStyle(name='TableHead', fontName='DV-Bold', fontSize=7.3, leading=10,
                          textColor=colors.white))
styles.add(ParagraphStyle(name='TableCell', fontName='DV', fontSize=7.15, leading=10,
                          textColor=INK))
styles.add(ParagraphStyle(name='Small', fontName='DV', fontSize=7.4, leading=10.5,
                          textColor=MUTED, spaceAfter=4))
styles.add(ParagraphStyle(name='Foot', fontName='DV', fontSize=7.2, leading=9,
                          textColor=MUTED))


def inline(s: str) -> str:
    s = s.strip()
    # Escape source text first, then apply a minimal, safe markdown inline subset.
    s = escape(s, {'"': '&quot;'})
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<link href="\2" color="#168C8C">\1</link>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', s)
    s = s.replace('  ', ' ')
    return s


def split_table(lines):
    rows=[]
    for line in lines:
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if cells and all(re.fullmatch(r':?-{3,}:?', c.replace(' ', '')) for c in cells):
            continue
        rows.append(cells)
    return rows


def draw_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    if doc.page == 1:
        # Minimal cover accents behind the content.
        canvas.setFillColor(NAVY)
        canvas.rect(0, h-14*mm, w, 14*mm, stroke=0, fill=1)
        canvas.setFillColor(TEAL)
        canvas.rect(0, h-17*mm, w, 3*mm, stroke=0, fill=1)
    else:
        canvas.setStrokeColor(colors.HexColor('#D8E1EA'))
        canvas.setLineWidth(.5)
        canvas.line(18*mm, h-15*mm, w-18*mm, h-15*mm)
        canvas.setFont('DV-Bold', 7.2)
        canvas.setFillColor(NAVY)
        canvas.drawString(19*mm, h-12*mm, 'CẨM NANG ÔN TẬP · NGỮ VĂN 10')
        canvas.setFont('DV', 7.1)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(w-19*mm, h-12*mm, 'Kết nối tri thức · Giữa kì I 2026–2027')
        canvas.setStrokeColor(colors.HexColor('#D8E1EA'))
        canvas.line(18*mm, 14*mm, w-18*mm, 14*mm)
        canvas.setFont('DV', 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawString(19*mm, 9*mm, 'Tài liệu luyện tập · Ngữ liệu đề thi chính thức có thể khác')
        canvas.drawRightString(w-19*mm, 9*mm, f'{doc.page}')
    canvas.restoreState()


def make_cover(story):
    story.append(Spacer(1, 38*mm))
    box = Table([
        [Paragraph('CẨM NANG<br/>ÔN TẬP', styles['CoverTitle'])],
        [Paragraph('GIỮA KÌ I · NGỮ VĂN 10', styles['CoverSub'])],
        [Spacer(1, 7*mm)],
        [Paragraph('KẾT NỐI TRI THỨC VỚI CUỘC SỐNG', styles['CoverInfo'])],
        [Paragraph('Năm học 2026–2027  ·  Thời lượng bài kiểm tra: 90 phút', styles['CoverSub'])],
    ], colWidths=[165*mm])
    box.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), NAVY),
        ('BOX',(0,0),(-1,-1),0, NAVY),
        ('LEFTPADDING',(0,0),(-1,-1),14*mm),('RIGHTPADDING',(0,0),(-1,-1),14*mm),
        ('TOPPADDING',(0,0),(-1,-1),8*mm),('BOTTOMPADDING',(0,0),(-1,-1),8*mm),
        ('LINEBELOW',(0,1),(-1,1),2,GOLD),
    ]))
    story.append(box)
    story.append(Spacer(1, 13*mm))
    story.append(Paragraph('<b>TRỌNG TÂM</b> &nbsp; Đọc hiểu truyện thần thoại ngoài sách giáo khoa · '
                           'Viết bài nghị luận phân tích, đánh giá một truyện',
                           ParagraphStyle('cover_note', fontName='DV', fontSize=11, leading=18,
                                          textColor=INK, alignment=TA_LEFT)))
    story.append(Spacer(1, 8*mm))
    story.append(HRFlowable(width='100%', thickness=1, color=TEAL, spaceBefore=2, spaceAfter=7*mm))
    story.append(Paragraph('Bám sát ma trận được cung cấp · Hệ thống kiến thức · Ngân hàng câu hỏi có đáp án · '
                           'Hai đề luyện hoàn chỉnh · Bài làm tham khảo',
                           ParagraphStyle('cover_desc', fontName='DV', fontSize=9.5, leading=15,
                                          textColor=MUTED)))
    story.append(Spacer(1, 13*mm))
    story.append(PageBreak())


def build():
    text = SRC.read_text(encoding='utf-8').splitlines()
    story=[]
    make_cover(story)
    i=0
    first_h1=True
    while i < len(text):
        line=text[i].rstrip()
        if not line.strip():
            i+=1; continue
        if line.startswith('# '):
            title=line[2:].strip()
            if first_h1:
                # Metadata lines after title are presented as a compact intro.
                story.append(Paragraph(inline(title), styles['H1x']))
                first_h1=False
            else:
                if not title.startswith('3. Kĩ thuật trả lời theo bốn mức độ'):
                    story.append(PageBreak())
                story.append(Paragraph(inline(title), styles['H1x']))
            i+=1; continue
        if line.startswith('## '):
            story.append(Paragraph(inline(line[3:]), styles['H2x']))
            i+=1; continue
        if line.startswith('### '):
            story.append(Paragraph(inline(line[4:]), styles['H3x']))
            i+=1; continue
        if line.strip() == '---':
            story.append(HRFlowable(width='100%', thickness=.6, color=colors.HexColor('#D5DEE8'),
                                    spaceBefore=4, spaceAfter=7))
            i+=1; continue
        if line.lstrip().startswith('|'):
            block=[]
            while i < len(text) and text[i].strip().startswith('|'):
                block.append(text[i]); i+=1
            rows=split_table(block)
            if rows:
                n=len(rows[0])
                data=[]
                for ri,row in enumerate(rows):
                    row=row + ['']*(n-len(row))
                    data.append([Paragraph(inline(cell), styles['TableHead'] if ri==0 else styles['TableCell']) for cell in row[:n]])
                usable=174*mm
                # Equal widths except first column slightly narrower on 5-column tables.
                if n==5:
                    widths=[27*mm, 31*mm, 31*mm, 31*mm, 54*mm]
                elif n==4:
                    widths=[34*mm, 43*mm, 49*mm, 48*mm]
                else:
                    widths=[usable/n]*n
                tbl=Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
                tbl.setStyle(TableStyle([
                    ('BACKGROUND',(0,0),(-1,0),NAVY),
                    ('GRID',(0,0),(-1,-1),.35,colors.HexColor('#C8D3DF')),
                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                    ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
                    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
                    ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALEBLUE]),
                ]))
                story.append(KeepTogether([tbl,Spacer(1,6)]))
            continue
        if line.startswith('>'):
            quote=[]
            while i < len(text) and text[i].lstrip().startswith('>'):
                quote.append(text[i].lstrip()[1:].strip()); i+=1
            story.append(Paragraph(inline(' '.join(quote)), styles['Quote']))
            continue
        if line.startswith('- '):
            story.append(Paragraph('•&nbsp;&nbsp;'+inline(line[2:]), styles['Bulletx']))
            i+=1; continue
        m=re.match(r'^(\d+)\.\s+(.*)$', line)
        if m:
            story.append(Paragraph(f'<b>{m.group(1)}.</b>&nbsp;&nbsp;'+inline(m.group(2)), styles['Bulletx']))
            i+=1; continue
        # Normal paragraphs: collect adjacent plain lines, preserving explicit two-space breaks as spaces.
        parts=[line.strip()]
        i+=1
        while i < len(text):
            nxt=text[i].rstrip()
            if (not nxt.strip() or nxt.startswith('#') or nxt.strip()=='---' or nxt.startswith('>')
                or nxt.lstrip().startswith('|') or nxt.startswith('- ') or re.match(r'^\d+\.\s+',nxt)):
                break
            parts.append(nxt.strip())
            i+=1
        para=' '.join(parts)
        # Cover lead text uses a subtly distinct style.
        if first_h1 and 'Kết nối tri thức' in para:
            story.append(Paragraph(inline(para), styles['Small']))
        else:
            story.append(Paragraph(inline(para), styles['Bodyx']))

    doc=SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
                          topMargin=21*mm, bottomMargin=20*mm,
                          title='Cẩm nang ôn tập giữa kì I Ngữ văn 10 Kết nối tri thức 2026–2027',
                          author='Cẩm nang ôn tập theo ma trận do người học cung cấp',
                          subject='Đọc hiểu thần thoại ngoài SGK và nghị luận phân tích truyện')
    doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
    print(f'Created {OUT} ({OUT.stat().st_size:,} bytes)')

if __name__=='__main__':
    build()
