"""Verify rendered content, font embedding, navigation and page bounds; write QA JSON.

No automated check can prove literary correctness or replace visual review.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import unicodedata
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"


def normalized(value):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", value).replace("\u00ad", "")).strip()


def validate(path):
    doc = pymupdf.open(path)
    assert 35 <= len(doc) <= 90, f"Unexpected page count: {len(doc)}"
    assert not doc.is_encrypted
    texts = []
    font_ids = set()
    internal = external = 0
    per_page = []
    for i, page in enumerate(doc):
        w, h = page.rect.width, page.rect.height
        assert abs(w - 595.28) < 1 and abs(h - 841.89) < 1, f"Non-A4 page {i+1}"
        text = page.get_text()
        assert len(text.strip()) > 100, f"Empty/near-empty page {i+1}"
        assert "\ufffd" not in text, f"Replacement glyph on page {i+1}"
        # Clip running header/footer so paragraphs spanning pages can be checked.
        clip = page.rect if i == 0 else pymupdf.Rect(0, 50, w, h - 45)
        texts.append(page.get_text(clip=clip))
        per_page.append({"page": i + 1, "extracted_characters": len(text)})
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if not span["text"].strip():
                        continue
                    x0, y0, x1, y1 = span["bbox"]
                    assert x0 >= -1 and y0 >= -1 and x1 <= w + 1 and y1 <= h + 1, (i + 1, span)
                    if i > 0 and y0 > 50 and y1 < h - 40:
                        assert x0 >= 47 and x1 <= w - 47, f"Body crosses side margin on page {i+1}"
        font_ids.update(f[0] for f in page.get_fonts())
        for link in page.get_links():
            if link["kind"] == pymupdf.LINK_GOTO:
                assert 0 <= link["page"] < len(doc)
                internal += 1
            elif link["kind"] == pymupdf.LINK_URI:
                assert link["uri"].startswith("https://")
                external += 1
    for font_id in font_ids:
        assert doc.extract_font(font_id)[3], f"Unembedded font {font_id}"
    flat = normalized("\n".join(texts))
    exams = json.loads((ROOT / "src/exams.json").read_text())
    bank = json.loads((ROOT / "src/bank.json").read_text())
    # Exact normalized prose checks catch missing last paragraphs, not just headings.
    rendered_paragraphs = 0
    for e in exams:
        for field in ("passage", "essay"):
            for paragraph in e[field].split("\n\n"):
                assert normalized(paragraph) in flat, f"Missing {field} paragraph, exam {e['number']}"
                rendered_paragraphs += 1
        for q in e["questions"]:
            assert normalized(q["stem"]) in flat
            for c in q["choices"]:
                assert normalized(c) in flat
        for q in e["short"]:
            assert normalized(q["stem"]) in flat
            assert normalized(q["sample"]) in flat
        if e["extra"]:
            assert normalized(e["extra"]["passage"]) in flat
    for p in bank["passages"]:
        assert normalized(p["text"]) in flat
    for q in bank["questions"] + bank["short"]:
        assert normalized(q["stem"]) in flat
        if "sample" in q:
            assert normalized(q["sample"]) in flat
    for n in range(1, 7):
        assert f"Đáp án đề {n}" in flat
        assert f"Bài viết tham khảo đề {n}" in flat
    toc = doc.get_toc()
    assert len(toc) >= 60
    for _, title, page in toc:
        assert 1 <= page <= len(doc), (title, page)
    summary_pages = [i + 1 for i, t in enumerate(texts) if "7.4. Trang tóm lược trước giờ kiểm tra" in t]
    # The TOC has an entry too; the final occurrence is the actual one-page sheet.
    summary = texts[summary_pages[-1] - 1]
    assert "Trước khi nộp:" in summary and "90 phút" in summary
    assert internal >= 40 and external == 10
    report = {
        "pdf": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "pages": len(doc), "paper": "A4", "bookmarks": len(toc),
        "internal_links": internal, "external_source_links": external,
        "embedded_fonts": len(font_ids),
        "essays_word_counts_whitespace": [len(e["essay"].split()) for e in exams],
        "exact_rendered_paragraphs_passage_and_essay": rendered_paragraphs,
        "bank_mcq": len(bank["questions"]), "bank_written": len(bank["short"]),
        "summary_page": summary_pages[-1],
        "checks": "passed: full prose/choice presence, evidence schema separately, A4, bounds, embedded fonts, valid navigation, no blank pages or replacement glyphs",
        "limits": "Does not establish literary correctness, uniqueness of every interpretation, psychometric difficulty, live URL availability, or official approval.",
        "page_character_counts": per_page,
    }
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--report", type=Path, default=ROOT / "research/qa-report.json")
    args = parser.parse_args()
    report = validate(args.pdf.resolve())
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "page_character_counts"}, ensure_ascii=False, indent=2))
