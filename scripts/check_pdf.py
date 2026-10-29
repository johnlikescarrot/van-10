#!/usr/bin/env python3
"""Kiểm tra cấu trúc đề và khả năng trích xuất văn bản của PDF."""
from pathlib import Path
import re
import pymupdf

root = Path(__file__).resolve().parent.parent
src = (root / "src/main.typ").read_text(encoding="utf-8")
pdf = root / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"
practice = src.split("= V. Ba đề luyện 90 phút", 1)[1].split("= VI. Đáp án", 1)[0]
tests = re.split(r"(?m)^== Đề [123]\. ", practice)[1:]
assert len(tests) == 3, "Phải có ba đề luyện"
for index, test in enumerate(tests, 1):
    questions = re.findall(r"\*Câu (\d+)(?:\s|\.|\()", test)
    assert questions == [str(n) for n in range(1, 11)], (index, questions)
    assert "Câu 11:" in test and "90 phút" in test, index
    for question in re.split(r"\*Câu \d+\.\*", test)[1:9]:
        assert all(f"{letter}. " in question for letter in "ABCD"), index
    assert "Bản kể lại" in test, index
assert sum([0.25, 0.50, 1, 1.25, 0.50, 0.25, 0.25]) == 4
with pymupdf.open(pdf) as doc:
    assert len(doc) >= 10
    text = "\n".join(p.get_text() for p in doc)
    for word in ["Ma trận", "Nữ thần Lúa", "Thần Mưa", "Mặt Trời", "hướng dẫn chấm", "Nguồn và phạm vi sử dụng"]:
        assert word.lower() in text.lower(), word
    assert "�" not in text
    assert len(doc.get_toc()) >= 7
    assert sum(len(p.get_links()) for p in doc) >= 6
    for i, page in enumerate(doc, 1):
        for x0, y0, x1, y1, *_ in page.get_text("blocks"):
            assert x0 >= 0 and y0 >= 0 and x1 <= page.rect.width and y1 <= page.rect.height, i
    print(f"Đạt: {len(doc)} trang, 3 đề, mục lục, liên kết và văn bản PDF.")
