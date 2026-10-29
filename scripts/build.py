#!/usr/bin/env python3
"""Build the study guide and check its structure and PDF text."""
from pathlib import Path
import re
import sys
import typst
import pymupdf

root = Path(__file__).resolve().parent.parent
source = root / 'src' / 'practice.typ'
pdf = root / 'DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf'
text = source.read_text(encoding='utf-8')
parts = re.split(r'(?m)^== Đề [123]\.', text)[1:]
if len(parts) != 3:
    sys.exit('Expected three practice exams')
for number, part in enumerate(parts, 1):
    questions = [int(x) for x in re.findall(r'#q\((\d+)\)', part)]
    if questions != list(range(1, 12)):
        sys.exit(f'Exam {number}: expected questions 1–11, got {questions}')
    if part.count('#opts[') != 8:
        sys.exit(f'Exam {number}: expected eight multiple-choice questions')
typst.compile(str(root / 'src' / 'main.typ'), output=str(pdf), root=str(root))
with pymupdf.open(pdf) as doc:
    full = '\n'.join(page.get_text() for page in doc)
    for phrase in ('Phạm vi và cách sử dụng', 'Ba đề luyện tập', 'Đáp án và hướng dẫn tự chấm', 'Bài viết tham khảo', 'Tài liệu tham khảo'):
        if phrase not in full:
            sys.exit(f'Missing PDF text: {phrase}')
    if not doc.get_toc():
        sys.exit('PDF bookmarks missing')
    for page in doc:
        if '\ufffd' in page.get_text():
            sys.exit(f'Invalid glyph on page {page.number + 1}')
        for block in page.get_text('blocks'):
            if block[0] < -1 or block[1] < -1 or block[2] > page.rect.width + 1 or block[3] > page.rect.height + 1:
                sys.exit(f'Text outside page {page.number + 1}')
    print(f'Built {pdf.name}: {len(doc)} pages, {len(doc.get_toc())} bookmarks; structure and PDF text OK')
