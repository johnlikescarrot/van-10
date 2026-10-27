# -*- coding: utf-8 -*-
"""
Builder: Markdown-lite -> PDF (ReportLab) cho Đề cương ôn tập Giữa kì I Ngữ văn 10.
Chạy:  python3 build_pdf.py
"""
import os, re, glob, sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, PageBreak,
                                NextPageTemplate, Flowable, Preformatted)
from reportlab.platypus.tableofcontents import TableOfContents

BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "fonts")
CONTENT = os.path.join(BASE, "content")
OUT = os.path.join(os.path.dirname(BASE),
                   "DE-CUONG-ON-TAP-GIUA-KI-1-NGU-VAN-10-KNTT-2026-2027.pdf")

# ---------------------------------------------------------------- fonts
def reg(name, file):
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, file)))

reg("BVP", "BeVietnamPro-Regular.ttf")
reg("BVP-I", "BeVietnamPro-Italic.ttf")
reg("BVP-M", "BeVietnamPro-Medium.ttf")
reg("BVP-SB", "BeVietnamPro-SemiBold.ttf")
reg("BVP-B", "BeVietnamPro-Bold.ttf")
reg("BVP-BI", "BeVietnamPro-BoldItalic.ttf")
reg("BVP-XB", "BeVietnamPro-ExtraBold.ttf")
reg("BVP-MONO", "RobotoMono.ttf")
reg("SYM", "DejaVuSans.ttf")
pdfmetrics.registerFontFamily("BVP", normal="BVP", bold="BVP-B",
                              italic="BVP-I", boldItalic="BVP-BI")

# ---------------------------------------------------------------- palette
NAVY      = colors.HexColor("#12395C")
NAVY_D    = colors.HexColor("#0B2439")
TEAL      = colors.HexColor("#0E6E6E")
ACCENT    = colors.HexColor("#B8462B")   # terracotta
AMBER     = colors.HexColor("#8A5A00")
GREEN     = colors.HexColor("#1B6B4A")
INK       = colors.HexColor("#1C1C1C")
GREY      = colors.HexColor("#5A6672")
LIGHT     = colors.HexColor("#EEF3F8")
LIGHT2    = colors.HexColor("#F7F9FB")
CREAM     = colors.HexColor("#FDF6E8")
MINT      = colors.HexColor("#EAF4EF")
ROSE      = colors.HexColor("#FBEDE9")
RULE      = colors.HexColor("#C9D4DE")

PW, PH = A4
LM, RM, TM, BM = 1.9*cm, 1.7*cm, 2.15*cm, 1.75*cm

# ---------------------------------------------------------------- styles
def S(name, **kw):
    base = dict(fontName="BVP", fontSize=10.2, leading=15.4, textColor=INK,
                alignment=TA_JUSTIFY, spaceAfter=5.5)
    base.update(kw)
    return ParagraphStyle(name, **base)

ST = {}
ST["body"]    = S("body", spaceBefore=1)
ST["bodyc"]   = S("bodyc", alignment=TA_CENTER)
ST["lead"]    = S("lead", fontName="BVP-M", fontSize=11.2, leading=17.5,
                  textColor=NAVY_D, spaceAfter=9)
ST["h1"]      = S("h1", fontName="BVP-XB", fontSize=22, leading=26,
                  textColor=colors.white, alignment=TA_LEFT, spaceAfter=0)
ST["h1sub"]   = S("h1sub", fontName="BVP-M", fontSize=11, leading=16,
                  textColor=colors.HexColor("#D6E4F0"), alignment=TA_LEFT, spaceAfter=0)
ST["h1s"]     = S("h1s", fontName="BVP-B", fontSize=15.2, leading=20.5,
                  textColor=NAVY, alignment=TA_LEFT, spaceBefore=13, spaceAfter=8)
ST["h2"]      = S("h2", fontName="BVP-B", fontSize=12.4, leading=17,
                  textColor=NAVY, alignment=TA_LEFT, spaceBefore=12, spaceAfter=5)
ST["h3"]      = S("h3", fontName="BVP-B", fontSize=11.8, leading=16,
                  textColor=TEAL, alignment=TA_LEFT, spaceBefore=11, spaceAfter=5)
ST["h4"]      = S("h4", fontName="BVP-SB", fontSize=10.6, leading=15,
                  textColor=ACCENT, alignment=TA_LEFT, spaceBefore=8, spaceAfter=3.5)
ST["quote"]   = S("quote", fontName="BVP-I", fontSize=10.0, leading=15.2,
                  textColor=colors.HexColor("#243746"), spaceAfter=0)
ST["qsb"]     = S("qsb", fontName="BVP-SB", fontSize=10.0, leading=15.2,
                  textColor=NAVY_D, spaceAfter=0)
ST["cell"]    = S("cell", fontSize=9.0, leading=12.9, spaceAfter=0, alignment=TA_LEFT)
ST["cellb"]   = S("cellb", fontName="BVP-SB", fontSize=9.0, leading=12.9,
                  spaceAfter=0, alignment=TA_LEFT, textColor=NAVY_D)
ST["cellc"]   = S("cellc", fontSize=9.0, leading=12.9, spaceAfter=0, alignment=TA_CENTER)
ST["cellcb"]  = S("cellcb", fontName="BVP-SB", fontSize=9.0, leading=12.9,
                  spaceAfter=0, alignment=TA_CENTER, textColor=colors.white)
ST["bul"]     = S("bul", fontSize=10.2, leading=15.2, leftIndent=14, bulletIndent=3,
                  spaceAfter=3.2)
ST["toc0"]    = S("toc0", fontName="BVP-B", fontSize=11, leading=18, textColor=NAVY,
                  alignment=TA_LEFT, spaceBefore=7, spaceAfter=0)
ST["toc1"]    = S("toc1", fontName="BVP", fontSize=9.8, leading=14.6, textColor=INK,
                  alignment=TA_LEFT, leftIndent=12, spaceAfter=0)
ST["small"]   = S("small", fontName="BVP-I", fontSize=8.6, leading=12.2,
                  textColor=GREY, spaceAfter=3)
ST["psg"]     = S("psg", fontSize=10.35, leading=16.6, spaceAfter=7.5,
                  textColor=colors.HexColor("#22303C"))
ST["psgt"]    = S("psgt", fontName="BVP-B", fontSize=11.4, leading=16, spaceAfter=9,
                  textColor=NAVY, alignment=TA_CENTER)
ST["code"]    = ParagraphStyle("code", fontName="BVP-MONO", fontSize=8.0, leading=12.2,
                               textColor=colors.HexColor("#1E3A52"), alignment=TA_LEFT)
ST["cap"]     = S("cap", fontName="BVP-M", fontSize=8.8, leading=12.4,
                  textColor=GREY, alignment=TA_LEFT, spaceBefore=2, spaceAfter=8)

# ---------------------------------------------------------------- inline markup
def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(t):
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+?)`", r'<font color="#B8462B">\1</font>', t)
    # các ký hiệu không có trong BeVietnamPro -> font dự phòng DejaVuSans
    t = re.sub(r"([\u2190-\u21FF\u25A0-\u25FF\u2600-\u27BF\u2B00-\u2BFF])",
               r'<font name="SYM">\1</font>', t)
    return t

# ---------------------------------------------------------------- flowables
class HRule(Flowable):
    def __init__(self, w=None, color=RULE, thickness=0.7, space=6):
        Flowable.__init__(self); self.w=w; self.color=color; self.t=thickness; self.space=space
    def wrap(self, aw, ah):
        self._aw = self.w or aw
        return (self._aw, self.t + self.space)
    def draw(self):
        self.canv.setStrokeColor(self.color); self.canv.setLineWidth(self.t)
        self.canv.line(0, self.space, self._aw, self.space)

class PartBand(Flowable):
    """Dải màu mở đầu mỗi phần."""
    def __init__(self, kicker, title, sub=""):
        Flowable.__init__(self)
        self.kicker=kicker; self.title=title; self.sub=sub
    def wrap(self, aw, ah):
        self._aw=aw
        self._h = 3.55*cm if not self.sub else 3.95*cm
        return (aw, self._h)
    def draw(self):
        c=self.canv; w=self._aw; h=self._h
        c.setFillColor(NAVY); c.rect(0,0,w,h,stroke=0,fill=1)
        c.setFillColor(ACCENT); c.rect(0,h-4.5,w,4.5,stroke=0,fill=1)
        c.setFillColor(colors.white); c.setFont("BVP-SB", 8.6)
        c.drawString(0.55*cm, h-1.05*cm, self.kicker.upper())
        c.setFillColor(colors.HexColor("#A9C4DC")); c.setFont("BVP-M", 8.6)
        c.drawRightString(w-0.55*cm, h-1.05*cm, "NGỮ VĂN 10 · KẾT NỐI TRI THỨC")
        c.setFillColor(colors.white); c.setFont("BVP-XB", 19.5)
        y = h-2.05*cm
        # wrap title if long
        words=self.title.split(); line=""; lines=[]
        for wd in words:
            test=(line+" "+wd).strip()
            if c.stringWidth(test,"BVP-XB",19.5) > w-1.1*cm and line:
                lines.append(line); line=wd
            else: line=test
        lines.append(line)
        for ln in lines:
            c.drawString(0.55*cm, y, ln); y-=0.82*cm
        if self.sub:
            c.setFillColor(colors.HexColor("#CFE0EE")); c.setFont("BVP-I", 9.4)
            c.drawString(0.55*cm, max(0.5*cm, y+0.12*cm), self.sub)

def callout(lines, bg=LIGHT, bar=TEAL, style="quote"):
    rows=[]
    for ln in lines:
        rows.append([Paragraph(inline(ln), ST[style])])
    t = Table(rows, colWidths=[PW-LM-RM-0.1*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),bg),
        ("LINEBEFORE",(0,0),(0,-1),2.6,bar),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
    ]))
    return t

# ---------------------------------------------------------------- markdown-lite parsing
def parse_table_rows(block):
    rows=[]
    for line in block:
        s=line.strip()
        if not s.startswith("|"): continue
        cells=[c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells): continue
        rows.append(cells)
    return rows

def build_table(rows, avail):
    ncol=max(len(r) for r in rows)
    rows=[r+[""]*(ncol-len(r)) for r in rows]
    # weights from content length
    w=[]
    for i in range(ncol):
        body=[len(r[i]) for r in rows[1:]] or [10]
        avg=sum(body)/len(body)
        w.append(min(max(avg*0.55 + 5, 9), 46))
    tot=sum(w); widths=[avail*x/tot for x in w]
    # min width guard
    minw=1.35*cm
    widths=[max(x,minw) for x in widths]
    sc=avail/sum(widths); widths=[x*sc for x in widths]
    data=[]
    for ri,r in enumerate(rows):
        out=[]
        for ci,c in enumerate(r):
            st = ST["cellcb"] if ri==0 else (ST["cellb"] if ci==0 else ST["cell"])
            out.append(Paragraph(inline(c) if c else " ", st))
        data.append(out)
    t=Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style=[
        ("BACKGROUND",(0,0),(-1,0),NAVY),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("GRID",(0,0),(-1,-1),0.45,RULE),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
        ("TOPPADDING",(0,0),(-1,-1),4.5),("BOTTOMPADDING",(0,0),(-1,-1),4.5),
    ]
    for i in range(1,len(data)):
        if i%2==0:
            style.append(("BACKGROUND",(0,i),(-1,i),LIGHT2))
    t.setStyle(TableStyle(style))
    return t

def parse_md(text):
    """Trả về list flowable."""
    flow=[]
    lines=text.split("\n")
    i=0
    while i < len(lines):
        ln=lines[i]
        s=ln.rstrip()
        if not s.strip():
            i+=1; continue

        # page break marker
        if s.strip() in ("[PB]", "\\pagebreak"):
            flow.append(PageBreak()); i+=1; continue
        if s.strip() == "[TOC]":
            i+=1; continue
        if s.strip() == "---":
            flow.append(HRule(color=RULE, space=5)); i+=1; continue

        # part band:  @@ KICKER | TITLE | SUB
        if s.startswith("@@"):
            body=s[2:].strip()
            parts=[p.strip() for p in body.split("|")]
            kicker=parts[0] if len(parts)>0 else ""
            title=parts[1] if len(parts)>1 else ""
            sub=parts[2] if len(parts)>2 else ""
            flow.append(PageBreak())
            band=PartBand(kicker,title,sub)
            band._nav=("PART", title)
            flow.append(band)
            flow.append(Spacer(1,14))
            i+=1; continue

        # fenced code block
        if s.strip().startswith("```"):
            i += 1
            buf=[]
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i].rstrip("\n")); i+=1
            i += 1
            pre=Preformatted("\n".join(buf), ST["code"])
            t=Table([[pre]], colWidths=[PW-LM-RM])
            t.setStyle(TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#F4F7FA")),
                ("LINEBEFORE",(0,0),(0,-1),2.2,NAVY),
                ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),8),
                ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),
            ]))
            flow.append(Spacer(1,4)); flow.append(t); flow.append(Spacer(1,10))
            continue

        # headings
        m=re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl=len(m.group(1)); txt=m.group(2).strip()
            if lvl==1:
                p1=Paragraph('<font color="#B8462B">▍</font> '+inline(txt), ST["h1s"])
                p1._nav=("H1", txt)
                flow.append(p1)
            elif lvl==2:
                flow.append(_heading(txt, ST["h2"], 2, nav=("H2", txt)))
            elif lvl==3:
                flow.append(_heading(txt, ST["h3"], 3, nav=("H3", txt)))
            else:
                flow.append(Paragraph(inline(txt), ST["h4"]))
            i+=1; continue

        # callouts
        if s.startswith(">>"):
            buf=[]
            while i<len(lines) and lines[i].startswith(">>"):
                buf.append(lines[i][2:].strip()); i+=1
            flow.append(Spacer(1,3)); flow.append(callout(buf, CREAM, ACCENT, "quote"))
            flow.append(Spacer(1,8)); continue
        if s.startswith("!!"):
            buf=[]
            while i<len(lines) and lines[i].startswith("!!"):
                buf.append(lines[i][2:].strip()); i+=1
            flow.append(Spacer(1,3)); flow.append(callout(buf, MINT, GREEN, "quote"))
            flow.append(Spacer(1,8)); continue
        if s.startswith(">") and not s.startswith(">>"):
            buflines=[]
            while i<len(lines) and lines[i].startswith(">") and not lines[i].startswith(">>"):
                t=lines[i][1:].strip(); buflines.append(t); i+=1
            # gộp thành các đoạn, dòng ">" trống = ngắt đoạn
            paras=[]; cur=[]
            for t in buflines:
                if t=="":
                    if cur: paras.append(" ".join(cur)); cur=[]
                else: cur.append(t)
            if cur: paras.append(" ".join(cur))
            if paras:
                flow.append(Spacer(1,3)); flow.append(callout(paras, LIGHT, TEAL, "quote"))
                flow.append(Spacer(1,8))
            continue

        # khối ngữ liệu (văn bản trích) :  %%  /  %%! tiêu đề /  %% trống
        if s.strip().startswith("%%"):
            blk=[]
            while i<len(lines) and lines[i].strip().startswith("%%"):
                blk.append(lines[i].strip()); i+=1
            rows=[]
            cur=[]
            def flush():
                if cur:
                    rows.append([Paragraph(inline(" ".join(cur)), ST["psg"])])
                    del cur[:]
            for b in blk:
                body=b[2:].strip()
                if body.startswith("!"):
                    flush()
                    rows.append([Paragraph(inline(body[1:].strip()), ST["psgt"])])
                elif body=="":
                    flush()
                else:
                    cur.append(body)
            flush()
            if not rows: continue
            t=Table(rows, colWidths=[PW-LM-RM-0.1*cm])
            t.setStyle(TableStyle([
                ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#FBF7EF")),
                ("BOX",(0,0),(-1,-1),0.6,colors.HexColor("#D9C9A8")),
                ("LEFTPADDING",(0,0),(-1,-1),14),("RIGHTPADDING",(0,0),(-1,-1),14),
                ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
                ("TOPPADDING",(0,0),(-1,0),12),("BOTTOMPADDING",(0,-1),(-1,-1),12),
                ("VALIGN",(0,0),(-1,-1),"TOP"),
            ]))
            flow.append(Spacer(1,4)); flow.append(t); flow.append(Spacer(1,11))
            continue

        # tables
        if s.strip().startswith("|"):
            buf=[]
            while i<len(lines) and lines[i].strip().startswith("|"):
                buf.append(lines[i]); i+=1
            rows=parse_table_rows(buf)
            if rows:
                flow.append(Spacer(1,2))
                flow.append(build_table(rows, PW-LM-RM))
                flow.append(Spacer(1,9))
            continue

        # bullets
        if re.match(r"^\s*[-•]\s+", s):
            buf=[]
            while i<len(lines) and (re.match(r"^\s*[-•]\s+", lines[i]) or
                                    (lines[i].startswith("   ") and lines[i].strip() and not lines[i].strip().startswith(("|","#")))):
                buf.append(lines[i]); i+=1
            items=[]
            for b in buf:
                mm=re.match(r"^\s*[-•]\s+(.*)$", b)
                if mm: items.append(("•", mm.group(1)))
                else: items.append((None, b.strip()))
            for mark,txt in items:
                if mark:
                    flow.append(Paragraph(inline(txt), ST["bul"], bulletText="•"))
                else:
                    flow.append(Paragraph(inline(txt), S("sub", fontSize=10.2, leading=15.2,
                                                         leftIndent=26, spaceAfter=3.2)))
            flow.append(Spacer(1,3)); continue

        # MCQ options A. B. C. D.
        if re.match(r"^[A-D]\.\s", s):
            while i < len(lines) and re.match(r"^[A-D]\.\s", lines[i].strip()):
                mm=re.match(r"^([A-D])\.\s+(.*)$", lines[i].strip())
                flow.append(Paragraph('<b>%s.</b>&nbsp;&nbsp;' % mm.group(1) + inline(mm.group(2)),
                            S("opt", fontSize=10.2, leading=15.0,
                              leftIndent=21, firstLineIndent=-14, spaceAfter=2.6)))
                i+=1
            flow.append(Spacer(1,3)); continue

        # numbered
        if re.match(r"^\s*\d+[\.\)]\s+", s):
            while i<len(lines) and re.match(r"^\s*\d+[\.\)]\s+", lines[i]):
                mm=re.match(r"^\s*(\d+)[\.\)]\s+(.*)$", lines[i])
                flow.append(Paragraph(inline(mm.group(2)), ST["bul"], bulletText=mm.group(1)+"."))
                i+=1
            flow.append(Spacer(1,3)); continue

        # paragraph (join following non-empty, non-special lines)
        buf=[s.strip()]
        i+=1
        while i<len(lines):
            nx=lines[i]
            if (not nx.strip()) or nx.strip().startswith(("|","#",">","!!","@@","[PB]","---")) \
               or re.match(r"^\s*[-•]\s+", nx) or re.match(r"^\s*\d+[\.\)]\s+", nx):
                break
            buf.append(nx.strip()); i+=1
        txt=" ".join(buf)
        st = ST["lead"] if txt.startswith("**") and txt.endswith("**") and False else ST["body"]
        flow.append(Paragraph(inline(txt), st))
    return flow

def _heading(txt, style, level, nav=None):
    p=Paragraph(inline(txt), style)
    if nav: p._nav = nav
    return p

class TOCPlaceholder(Flowable):
    pass
TOC_PLACEHOLDER = TOCPlaceholder()

# ---------------------------------------------------------------- doc template
class DeCuongDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=LM, rightMargin=RM,
                                 topMargin=TM, bottomMargin=BM,
                                 title="Đề cương ôn tập Giữa kì I – Ngữ văn 10 (KNTT) 2026–2027",
                                 author="Biên soạn tự động – Arena Agent",
                                 subject="Đề cương ôn tập Ngữ văn 10 – Truyện thần thoại",
                                 **kw)
        frame=Frame(LM, BM, PW-LM-RM, PH-TM-BM, id="main",
                    leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        cover_frame=Frame(LM, BM, PW-LM-RM, PH-TM-BM, id="cover",
                          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self.draw_cover),
            PageTemplate(id="body", frames=[frame], onPage=self.draw_body),
        ])
        self.toc_entries=[]

    # -- page furniture
    def draw_cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(colors.white); canv.rect(0,0,PW,PH,stroke=0,fill=1)

        band_h = 10.15*cm
        canv.setFillColor(NAVY); canv.rect(0, PH-band_h, PW, band_h, stroke=0, fill=1)
        canv.setFillColor(ACCENT); canv.rect(0, PH-band_h-0.16*cm, PW, 0.16*cm, stroke=0, fill=1)
        # decorative faint rings bottom-right of band
        canv.saveState()
        canv.setStrokeColor(colors.HexColor("#1D4870")); canv.setLineWidth(1.1)
        for r in (2.2, 3.1, 4.0, 4.9):
            canv.circle(PW+0.6*cm, PH-band_h+0.4*cm, r*cm, stroke=1, fill=0)
        canv.restoreState()

        canv.setFillColor(colors.HexColor("#8FB4D2")); canv.setFont("BVP-SB", 9.4)
        canv.drawString(LM, PH-2.35*cm, "TÀI LIỆU ÔN THI  ·  LỚP 10  ·  CHƯƠNG TRÌNH GDPT 2018")
        canv.setStrokeColor(colors.HexColor("#3D6A93")); canv.setLineWidth(0.8)
        canv.line(LM, PH-2.72*cm, PW-RM, PH-2.72*cm)

        canv.setFillColor(colors.white)
        canv.setFont("BVP-ExtraBold" if False else "BVP-XB", 46)
        canv.drawString(LM-0.12*cm, PH-4.35*cm, "ĐỀ CƯƠNG")
        canv.setFont("BVP-XB", 27.5)
        canv.drawString(LM-0.06*cm, PH-5.55*cm, "ÔN TẬP GIỮA HỌC KÌ I")
        canv.setFillColor(colors.HexColor("#F2C879")); canv.setFont("BVP-B", 33)
        canv.drawString(LM-0.1*cm, PH-6.85*cm, "NGỮ VĂN 10")
        canv.setFillColor(colors.HexColor("#D3E3F0")); canv.setFont("BVP-M", 12)
        canv.drawString(LM-0.05*cm, PH-7.75*cm, "Bộ sách KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
        canv.setFillColor(colors.HexColor("#9DBFD8")); canv.setFont("BVP-M", 11)
        canv.drawString(LM-0.05*cm, PH-8.45*cm, "Năm học 2026 – 2027   ·   Thời gian làm bài: 90 phút")

        # --- four stat cards
        cy = PH-9.55*cm
        cards=[("11","câu hỏi"),("6,0","điểm Đọc hiểu"),("4,0","điểm Viết"),("90","phút")]
        cw = (PW-LM-RM-3*0.32*cm)/4.0
        for i,(num,lab) in enumerate(cards):
            x = LM + i*(cw+0.32*cm)
            canv.setFillColor(colors.HexColor("#1B4A73"))
            canv.roundRect(x, cy-1.02*cm, cw, 1.02*cm, 0.14*cm, stroke=0, fill=1)
            canv.setFillColor(colors.white); canv.setFont("BVP-XB", 17)
            canv.drawString(x+0.34*cm, cy-0.62*cm, num)
            canv.setFillColor(colors.HexColor("#A9C4DC")); canv.setFont("BVP-M", 7.6)
            canv.drawString(x+0.34*cm, cy-0.88*cm, lab)

        # --- middle info block
        y=PH-12.35*cm
        canv.setFillColor(NAVY); canv.setFont("BVP-B", 12.6)
        canv.drawString(LM, y, "NỘI DUNG TRỌNG TÂM")
        canv.setStrokeColor(ACCENT); canv.setLineWidth(1.6)
        canv.line(LM, y-0.22*cm, LM+2.0*cm, y-0.22*cm)
        y-=0.95*cm
        items=[("Thể loại","Truyện thần thoại – ngữ liệu NGOÀI sách giáo khoa"),
               ("Cấu trúc đề","8 câu trắc nghiệm + 2 câu tự luận đọc hiểu + 1 bài viết"),
               ("Thang điểm","Đọc hiểu 6,0 điểm  ·  Viết 4,0 điểm  ·  Tổng 10 điểm"),
               ("Trọng số tư duy","Biết 40%  ·  Hiểu 30%  ·  Vận dụng 30%"),
               ("Kĩ năng viết","Nghị luận phân tích, đánh giá một tác phẩm truyện")]
        for k,v in items:
            canv.setFillColor(TEAL); canv.setFont("BVP-SB", 10.4)
            canv.drawString(LM, y, "▪")
            canv.setFillColor(NAVY_D); canv.setFont("BVP-SB", 10.2)
            canv.drawString(LM+0.48*cm, y, k)
            canv.setFont("BVP", 10.3); canv.setFillColor(colors.HexColor("#2B3540"))
            canv.drawString(LM+4.15*cm, y, v)
            y-=0.66*cm

        # --- footer band
        canv.setFillColor(LIGHT); canv.rect(0,0,PW,3.15*cm,stroke=0,fill=1)
        canv.setFillColor(TEAL); canv.rect(0,3.15*cm,PW,0.1*cm,stroke=0,fill=1)
        canv.setFillColor(GREY); canv.setFont("BVP-I", 8.7)
        canv.drawString(LM, 2.0*cm, "Biên soạn bám sát MA TRẬN và BẢN ĐẶC TẢ đề kiểm tra giữa kì I môn Ngữ văn 10, năm học 2026–2027.")
        canv.drawString(LM, 1.52*cm, "Toàn bộ 11 câu hỏi của đề minh hoạ đều có đáp án, thang điểm và hướng dẫn chấm chi tiết.")
        canv.setFont("BVP-SB", 8.7); canv.setFillColor(NAVY)
        canv.drawString(LM, 0.85*cm, "LƯU HÀNH NỘI BỘ  ·  DÙNG CHO HỌC SINH TỰ ÔN TẬP")
        canv.restoreState()

    def draw_body(self, canv, doc):
        canv.saveState()
        # header
        canv.setFont("BVP-M", 7.9); canv.setFillColor(GREY)
        canv.drawString(LM, PH-1.42*cm, "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I · NGỮ VĂN 10 · KẾT NỐI TRI THỨC")
        canv.drawRightString(PW-RM, PH-1.42*cm, "NĂM HỌC 2026 – 2027")
        canv.setStrokeColor(RULE); canv.setLineWidth(0.6)
        canv.line(LM, PH-1.62*cm, PW-RM, PH-1.62*cm)
        canv.setStrokeColor(ACCENT); canv.setLineWidth(1.4)
        canv.line(LM, PH-1.62*cm, LM+2.2*cm, PH-1.62*cm)
        # footer
        canv.setStrokeColor(RULE); canv.setLineWidth(0.6)
        canv.line(LM, BM-0.55*cm, PW-RM, BM-0.55*cm)
        canv.setFont("BVP", 8.2); canv.setFillColor(GREY)
        canv.drawString(LM, BM-1.0*cm, "Truyện thần thoại · Đọc hiểu & Viết")
        canv.setFont("BVP-SB", 9); canv.setFillColor(NAVY)
        canv.drawRightString(PW-RM, BM-1.03*cm, "Trang %d" % doc.page)
        canv.restoreState()

    # -- bookmarks + toc
    def afterFlowable(self, flowable):
        nav=getattr(flowable,"_nav",None)
        if not nav: return
        kind,txt=nav
        txt=re.sub(r"<[^>]+>","",txt)
        key="h%d"%len(self.toc_entries)
        self.canv.bookmarkPage(key)
        depth={"PART":0,"H1":1,"H2":1,"H3":2}[kind]
        self.canv.addOutlineEntry(txt, key, level=depth, closed=(depth>0))
        if depth<=1 and kind in ("PART","H1"):
            self.notify("TOCEntry", (0 if kind=="PART" else 1, txt, self.page, key))

# ---------------------------------------------------------------- TOC
class MyTOC(TableOfContents):
    def __init__(self):
        TableOfContents.__init__(self, levelStyles=[ST["toc0"], ST["toc1"]],
                                 dotsMinLevel=0, rightColumnWidth=1.6*cm)

# ---------------------------------------------------------------- main
def collect():
    files=sorted(glob.glob(os.path.join(CONTENT,"*.md")))
    flow=[]
    for idx,f in enumerate(files):
        with open(f, encoding="utf-8") as fh:
            content=fh.read()
        part=parse_md(content)
        if idx>0:
            flow.append(NextPageTemplate("body"))
        flow.extend(part)
    return flow

def build():
    flow=collect()
    toc=MyTOC()
    out=[NextPageTemplate("body"), PageBreak()]
    out.append(Paragraph("MỤC LỤC", ST["h1s"]))
    out.append(HRule(color=ACCENT, thickness=1.4, space=8))
    out.append(toc)
    out.extend(flow)
    doc=DeCuongDoc(OUT)
    doc.multiBuild(out)
    print("OK ->", OUT)

if __name__=="__main__":
    build()
