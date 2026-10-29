#!/usr/bin/env python3
"""Check source structure, practice keys, model length, and exported PDF."""
from collections import Counter
from pathlib import Path
import re
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check_sources():
    counts = []
    for name in ("part6_exams_1_3.typ", "part7_exams_4_6.typ"):
        source = (ROOT / "src" / name).read_text(encoding="utf-8")
        exams = re.split(r"(?=#exam-header\()", source)[1:]
        require(len(exams) == 3, f"Expected three exams in {name}")
        for exam in exams:
            questions = re.findall(r"(?m)^\*Câu (\d+)\*", exam)
            require(questions == [str(n) for n in range(1, 12)], "Exam must have questions 1–11")
            require(len(re.findall(r"(?m)^\*Câu [1-6]\* #badge-biet\.", exam)) == 6,
                    "Expected six recognition questions")
            require(len(re.findall(r"(?m)^\*Câu [78]\* #badge-hieu\.", exam)) == 2,
                    "Expected two comprehension MCQs")
            keys = re.findall(r"\[\*([1-8])\*\], \[\*([ABCD])\*\]", exam)
            require([int(n) for n, _ in keys] == list(range(1, 9)), "Missing or duplicate key")
            require(Counter(k for _, k in keys) == Counter(A=2, B=2, C=2, D=2),
                    "Each exam should have two correct answers per letter")
            for question in re.finditer(
                r"\*Câu ([1-8])\* #badge-(?:biet|hieu)\..*?\n\n", exam, re.S
            ):
                require(re.findall(r"(?m)^([ABCD])\. ", question[0]) == list("ABCD"),
                        "MCQ needs four ordered choices")
            essay = exam.split("#essay-box(", 1)[1].split(")[", 1)[1].rsplit("]", 1)[0]
            count = len(essay.split())
            require(600 <= count <= 800, f"Model essay outside practice target: {count}")
            counts.append(count)
            require("rubric ở mục 5.7" in exam, "Use the shared writing rubric")
    require(len(counts) == 6, "Expected six model essays")
    print(f"Source checks: 6 exams × 11 questions; essay lengths: {counts}")
    require(8 * .5 + 2 * 1 + 4 == 10, "Practice point total must equal ten")
    require(sum((.25, .25, 1, 1, .75, .5, .25)) == 4, "Writing rubric must total four")


def check_pdf():
    doc = pymupdf.open(PDF)
    require(len(doc) >= 40, "Unexpectedly short PDF")
    require(bool(doc.get_toc()), "PDF needs bookmarks")
    links = sum(len(page.get_links()) for page in doc)
    require(links >= 20, "PDF needs navigation and source links")
    all_text = []
    fonts = set()
    for number, page in enumerate(doc, 1):
        require(abs(page.rect.width - 595.28) < 2 and abs(page.rect.height - 841.89) < 2,
                f"Page {number} is not A4")
        text = page.get_text()
        require(len(text.strip()) > 500, f"Blank or nearly blank page {number}")
        require("\ufffd" not in text, f"Replacement character on page {number}")
        all_text.append(text)
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            require(x0 >= -1 and y0 >= -1 and x1 <= page.rect.width + 1
                    and y1 <= page.rect.height + 1, f"Text outside page {number}")
        for font in page.get_fonts():
            fonts.add(font[0])
    for xref in fonts:
        require(bool(doc.extract_font(xref)[3]), f"Font {xref} is not embedded")
    text = "\n".join(all_text)
    for token in ("5.7.", "8.1.", "8.3.", "S11", "Nữ Oa", "Prô-mê-tê"):
        require(token in text, f"Missing expected PDF text: {token}")
    for token in ("CHUẨN ĐIỂM TUYỆT ĐỐI", "99% truyện", "~70% ĐỀ THI"):
        require(token not in text, f"Unsupported promise still present: {token}")
    print(f"PDF checks: {len(doc)} A4 pages, {len(doc.get_toc())} bookmarks, "
          f"{links} links, {len(fonts)} embedded font resources; no blank pages or out-of-page text")


if __name__ == "__main__":
    check_sources()
    check_pdf()
