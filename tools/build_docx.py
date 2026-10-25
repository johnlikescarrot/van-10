#!/usr/bin/env python3
"""Dựng bản .docx tổng hợp "Đề cương ôn tập giữa kì I - Ngữ văn 10 (KNTT)".

Cách dùng:  python3 tools/build_docx.py
Yêu cầu:    pandoc (gói pypandoc-binary), python-docx
"""
import os
import subprocess
import sys

import pypandoc
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DOCX = os.path.join(ROOT, "DE-CUONG-ON-TAP-GIUA-KI-1-NGU-VAN-10-KNTT.docx")
REF_DOCX = os.path.join(ROOT, "tools", "reference.docx")
TMP_MD = os.path.join(ROOT, "tools", "_combined.md")

ORDER = [
    "00-phan-tich-ma-tran-va-chien-luoc-on-tap.md",
    "01-tri-thuc-nen-ve-truyen-than-thoai.md",
    "02-ba-truyen-than-thoai-viet-nam.md",
    "03-te-de-va-than-thoai-hy-lap.md",
    "04-tan-vien-tu-phan-su-luc-va-chu-nguoi-tu-tu.md",
    "05-tieng-viet-tu-han-viet-va-ky-nang-doc-hieu.md",
    "06-ky-nang-viet-nghi-luan-phan-tich-danh-gia-truyen.md",
    "07-so-do-tu-duy-va-meo-ghi-nho.md",
    "08-de-minh-hoa-va-dap-an.md",
]

PAGE_BREAK = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'

COVER = """---
title: "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I"
subtitle: "MÔN NGỮ VĂN – LỚP 10"
---

::: {custom-style="CoverInfo"}
**Bộ sách: Kết nối tri thức với cuộc sống**

**Năm học: 2026 – 2027**

**Thời gian làm bài kiểm tra: 90 phút**

**Cấu trúc đề: 8 câu trắc nghiệm + 2 câu tự luận ngắn + 1 bài viết – 10 điểm**
:::

::: {custom-style="CoverNote"}
*Tài liệu được biên soạn trên cơ sở ma trận và bản đặc tả đề kiểm tra giữa kì I (Ngữ văn 10, năm học 2026–2027) đang lưu hành, đồng thời mở rộng phạm vi kiến thức ra toàn bộ Bài 1 – Sức hấp dẫn của truyện kể và các kĩ năng đọc hiểu – viết – tiếng Việt có liên quan.*

*Nội dung gồm: hệ thống kiến thức trọng tâm, bảng biểu – sơ đồ – mẹo ghi nhớ, hệ thống câu hỏi – đáp án và 02 đề minh họa hoàn chỉnh kèm đáp án chi tiết, biểu điểm.*
:::
"""

TOC_MD = """# MỤC LỤC

| Phần | Nội dung chính |
|---|---|
| **Phần 0** | Giải mã ma trận – bản đặc tả; suy ra cấu trúc đề 90 phút; 13 yêu cầu cần đạt → 13 dạng câu hỏi; lộ trình ôn tập |
| **Phần 1** | Tri thức nền: thần thoại, truyện truyền kì, truyện ngắn; 6 đặc trưng thể loại; bối cảnh lịch sử – văn hoá |
| **Phần 2** | Ba truyện thần thoại Việt Nam: *Thần Trụ Trời*, *Thần Sét*, *Thần Gió* – tóm tắt, nhân vật, nghệ thuật, câu hỏi – đáp án, bảng so sánh |
| **Phần 3** | *Tê-dê* và thần thoại Hy Lạp; quan niệm về người anh hùng; so sánh thần thoại Việt Nam – Hy Lạp |
| **Phần 4** | *Tản Viên từ Phán sự lục* (Nguyễn Dữ) và *Chữ người tử tù* (Nguyễn Tuân) |
| **Phần 5** | Từ Hán Việt; 8 dạng câu hỏi đọc hiểu và công thức trả lời |
| **Phần 6** | Kĩ năng viết nghị luận phân tích, đánh giá tác phẩm truyện: dàn ý, câu mẫu, bài mẫu, rubric |
| **Phần 7** | Sơ đồ tư duy, bảng tổng hợp, 10 câu thần chú, flashcard, kế hoạch ôn 7 ngày, bí kíp phòng thi |
| **Phần 8** | **02 đề minh họa + đáp án chi tiết, biểu điểm** (đúng cấu trúc ma trận) |

**Hướng dẫn sử dụng:** (1) đọc Phần 0 để biết “học gì – bỏ gì”; (2) học theo thứ tự Phần 1 → Phần 6, tự kiểm tra bằng ô **CHỐT 30 GIÂY** cuối mỗi phần; (3) làm Phần 8 khi đã học xong, bấm giờ 90 phút; (4) trước ngày thi đọc Phần 7.

**Lưu ý về nguồn tài liệu:** văn bản gốc chỉ gồm *mục tiêu – ma trận – bản đặc tả*, **không có đề và câu hỏi**. Vì vậy, toàn bộ yêu cầu cần đạt của bản đặc tả đã được chuyển thành hệ thống câu hỏi – đáp án, và 02 đề minh họa ở Phần 8 được biên soạn đúng cấu trúc ma trận để bạn có đề luyện kèm đáp án.
"""


def _set_style_font(style, name="Times New Roman", size=None, bold=None, color=None):
    f = style.font
    f.name = name
    if size:
        f.size = Pt(size)
    if bold is not None:
        f.bold = bold
    if color:
        f.color.rgb = RGBColor(*color)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is not None:
        for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
            rfonts.set(qn("w:" + attr), name)


def make_reference_doc():
    """reference.docx: Times New Roman 13pt, giãn dòng 1.3, tiêu đề có màu."""
    with open(REF_DOCX, "wb") as fh:
        subprocess.run(
            [pypandoc.get_pandoc_path(), "--print-default-data-file", "reference.docx"],
            stdout=fh,
            check=True,
        )
    doc = Document(REF_DOCX)
    styles = doc.styles

    normal = styles["Normal"]
    _set_style_font(normal, size=13)
    pf = normal.paragraph_format
    pf.line_spacing = 1.3
    pf.space_after = Pt(4)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    headings = {
        "Title": (22, True, (0x8B, 0x1A, 0x1A)),
        "Subtitle": (15, False, (0x55, 0x55, 0x55)),
        "Heading 1": (16, True, (0x8B, 0x1A, 0x1A)),
        "Heading 2": (14, True, (0x1F, 0x3B, 0x73)),
        "Heading 3": (13, True, (0x2E, 0x4E, 0x2E)),
        "Heading 4": (13, True, (0x33, 0x33, 0x33)),
    }
    for name, (size, bold, color) in headings.items():
        if name in [s.name for s in styles]:
            _set_style_font(styles[name], size=size, bold=bold, color=color)

    for name in ("Source Code", "Verbatim Char"):
        if name in [s.name for s in styles]:
            _set_style_font(styles[name], name="Courier New", size=8.5)

    if "Table Text" in [s.name for s in styles]:
        st = styles["Table Text"]
        _set_style_font(st, size=10)
        st.paragraph_format.line_spacing = 1.05
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for style_name, size in (("CoverInfo", 13), ("CoverNote", 12)):
        try:
            st = styles.add_style(style_name, 1)
        except Exception:
            st = styles[style_name]
        _set_style_font(st, size=size)
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        st.paragraph_format.space_after = Pt(10)

    doc.save(REF_DOCX)


def build_markdown():
    parts = [COVER, PAGE_BREAK, TOC_MD, "\n"]
    for name in ORDER:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            sys.exit(f"Thiếu tệp: {name}")
        text = open(path, encoding="utf-8").read().strip()
        parts += [PAGE_BREAK, text, "\n\n"]
    md = "\n".join(parts)
    with open(TMP_MD, "w", encoding="utf-8") as fh:
        fh.write(md)
    return TMP_MD


def _page_field(paragraph):
    run = paragraph.add_run()
    for kind, text in (
        ("begin", None),
        ("instr", "PAGE"),
        ("separate", None),
        ("text", "1"),
        ("end", None),
    ):
        if kind == "text":
            el = OxmlElement("w:t")
            el.text = text
        elif kind == "instr":
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        else:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        run._r.append(el)


def post_process(path):
    doc = Document(path)

    for sec in doc.sections:
        sec.page_width = Cm(21)
        sec.page_height = Cm(29.7)
        sec.left_margin = Cm(2.0)
        sec.right_margin = Cm(2.0)
        sec.top_margin = Cm(1.8)
        sec.bottom_margin = Cm(1.8)
        footer = sec.footer
        fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        fp.text = ""
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fp.add_run("Đề cương ôn tập giữa kì I – Ngữ văn 10 (KNTT)  |  Trang ")
        _page_field(fp)

    for table in doc.tables:
        table.autofit = True
        for row in table.rows:
            trPr = row._tr.get_or_add_trPr()
            if not trPr.findall(qn("w:tblHeader")):
                trPr.append(OxmlElement("w:tblHeader"))
            for cell in row.cells:
                for p in cell.paragraphs:
                    p.paragraph_format.line_spacing = 1.05
                    p.paragraph_format.space_after = Pt(0)
                    for r in p.runs:
                        r.font.size = Pt(10)
                        if not r.font.name:
                            r.font.name = "Times New Roman"

    for p in doc.paragraphs:
        for r in p.runs:
            if not r.font.name:
                r.font.name = "Times New Roman"

    doc.save(path)


def main():
    make_reference_doc()
    md = build_markdown()
    pypandoc.convert_file(
        md,
        "docx",
        outputfile=OUT_DOCX,
        extra_args=[
            f"--reference-doc={REF_DOCX}",
            "-f", "markdown+pipe_tables+raw_attribute+fenced_divs",
            "--metadata", "lang=vi",
        ],
    )
    post_process(OUT_DOCX)
    print(f"Đã tạo: {OUT_DOCX} ({os.path.getsize(OUT_DOCX)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
