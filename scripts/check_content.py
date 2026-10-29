#!/usr/bin/env python3
"""Check numbering and shared answer keys before publishing the PDF."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'src'

def read(name): return (SRC/name).read_text(encoding='utf-8')
def answers(text): return re.findall(r'\[\*(\d+)\*\], \[\*([A-D])\*\],', text)

bank=read('part4_reading_skills.typ')
assert [int(n) for n,a in answers(bank)] == list(range(21,65))
assert len(re.findall(r'^\*Câu \d+\.\*',bank,re.M))==44
assert len(re.findall(r'^- \*Câu \d+ \(',bank,re.M))==16
assert len(answers(read('part3_vietnamese.typ')))==20
appendix=read('part10_appendix.typ')
for fname in ['part3_vietnamese.typ','part4_reading_skills.typ']:
 key=', '.join(f'{n}-{a}' for n,a in answers(read(fname)))
 assert key in appendix, f'Appendix mismatch: {fname}'
count=0
for fname in ['part6_exams_1_3.typ','part7_exams_4_6.typ','part8_exams_7_8.typ']:
 text=read(fname);pairs=answers(text)
 count+=text.count('#exam-header(')
 for k in range(0,len(pairs),8):
  assert [int(n) for n,a in pairs[k:k+8]]==list(range(1,9))
  assert ', '.join(f'{n}-{a}' for n,a in pairs[k:k+8]) in appendix
assert count==8
for p in SRC.glob('*.typ'):
 assert '\\n' not in p.read_text(),f'Literal newline escape in {p.name}'
print('Content checks passed: 20 language questions, 60 reading questions, 8 exams; answer keys match.')
