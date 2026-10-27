#!/usr/bin/env python3
"""Structural and reproducibility checks for the study guide and PDF."""
from __future__ import annotations

import re
import unicodedata
import unittest
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from pypdf import PdfReader
from reportlab.pdfbase.ttfonts import TTFontFace

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / 'MA TRẬN KIỂM TRA GIỮA KÌ 1 NGỮ VĂN 10 NĂM 2026-2027.docx'
PDF = ROOT / 'DE-CUONG-ON-TAP-NGU-VAN-10-GIUA-KI-I-2026-2027.pdf'
PAPERS = (ROOT / 'de-cuong/03-nam-de-luyen.md').read_text(encoding='utf-8')
SOLUTIONS = (ROOT / 'de-cuong/04-dap-an-va-bai-viet.md').read_text(encoding='utf-8')
RECALL = (ROOT / 'de-cuong/02-ky-nang-va-ghi-nho.md').read_text(encoding='utf-8')
W = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Expected answer contents, not just letters: catches mismatched keys after option edits.
EXPECTED = {
    1: ['Sau những trận lụt lớn, người sống sót phải gây dựng lại cuộc sống.',
        'Nữ thần Lúa.', 'Tự tìm đường về nhà.', 'Cầm chổi đánh vào bông lúa.',
        'Gặt, mang lúa về phơi, xay, giã.', 'Cúng hồn lúa hoặc cúng cơm mới sau thu hoạch.',
        'Gợi cách người xưa hình dung về lúa, công việc làm ra hạt gạo và sự trân trọng lương thực.',
        'Làm rõ bước ngoặt, qua đó gợi sự vất vả và ý nghĩa của lao động.'],
    2: ['Thuở xưa, không ghi niên đại cụ thể.', 'Hình rồng.', 'Từ sông và biển.',
        'Ba đợt.', 'Cá chép.', 'Con người có nước dùng, ruộng đồng và cây cỏ tươi tốt.',
        'Vì việc phân phối nước rất nặng, một mình thần khó cáng đáng.',
        'Tạo tiến trình thử thách và làm nổi bật chiến thắng của cá chép.'],
    3: ['Mặt Trời, Mặt Trăng và những hiện tượng gắn với hai thiên thể.', 'Luân phiên đi xem xét thế gian.',
        'Vì tốp người khiêng trẻ hay la cà.', 'Là chàng trai thân hình to lớn sống dưới đất.',
        'Ném cát về phía nàng.', 'Bay lên cao, về sau không sà thấp và dịu hơn.',
        'Độ dài ngắn khác nhau của ngày theo cách hình dung trong truyện.',
        'Thiên thể được hình dung gần gũi như người có cử động, qua đó cắt nghĩa các hình dạng trăng.'],
    4: ['Trời – đất trong thuở rất xa xưa, không có niên đại cụ thể.', 'Trụ chống trời gãy, trời nứt và đất rạn.',
        'Nữ Oa.', 'Đá năm màu được luyện chảy.', 'Bốn chân của một con rùa khổng lồ.',
        'Nữ Oa luyện đá năm màu để vá các vết nứt trên trời.', 'Khắc phục tai họa, khôi phục điều kiện sống.',
        'Ca ngợi khát vọng khắc phục tai họa và gìn giữ sự sống qua hành động của nữ thần.'],
    5: ['Hy Lạp.', 'Dớt (Zeus).', 'Lửa.', 'Sưởi ấm và nấu nướng.',
        'Bị xiềng trên núi và bị đại bàng hành hạ.', 'Dòng Titan.',
        'Là vị thần đem lại lửa cho con người và chịu trừng phạt.',
        'Mối liên hệ giữa hành động vì con người và cái giá nhân vật phải chịu.'],
}


def paper_sections():
    parts = re.split(r'(?=^## ĐỀ \d+ ·)', PAPERS, flags=re.M)
    return {int(re.match(r'## ĐỀ (\d+)', p).group(1)): p
            for p in parts if p.startswith('## ĐỀ')}


def question_blocks(paper):
    pattern = (r'^\*\*Câu (\d+) (\[[^\n]+\])\.\*\* ([^\n]+)\n\n'
               r'(.*?)(?=^\*\*Câu \d+|^\*\*II\.|\Z)')
    return {int(m.group(1)): (m.group(2), m.group(3), m.group(4))
            for m in re.finditer(pattern, paper, flags=re.M | re.S)}


def normalize(s):
    return ' '.join(unicodedata.normalize('NFC', s).split())


class MatrixTest(unittest.TestCase):
    def test_source_matrix_and_specification(self):
        with zipfile.ZipFile(DOCX) as archive:
            root = ET.fromstring(archive.read('word/document.xml'))
        tables = root.findall('.//w:tbl', W)
        self.assertEqual(len(tables), 2)
        rows = tables[0].findall('w:tr', W)
        cells = rows[3].findall('w:tc', W)
        values = [''.join(x.text or '' for x in c.findall('.//w:t', W)).strip() for c in cells]
        self.assertEqual(values[1:4], ['ĐỌC HIỂU', 'Truyện thần thoại', '6'])
        self.assertEqual(values[4:10], ['0', '2', '1', '0', '1', '60'])
        writing = [''.join(x.text or '' for x in c.findall('.//w:t', W)).strip()
                   for c in rows[4].findall('w:tc', W)]
        self.assertEqual(writing[-1], '40')
        self.assertEqual(writing.count('1*'), 3)
        spec = ''.join(x.text or '' for x in tables[1].findall('.//w:t', W))
        self.assertIn('Thần thoại (ngữ liệu ngoài sách giáo khoa)', spec)
        self.assertIn('11', spec)
        body = ''.join(x.text or '' for x in root.findall('.//w:t', W))
        self.assertIn('90 phút', body)


class PapersTest(unittest.TestCase):
    def test_five_complete_papers_and_levels(self):
        sections = paper_sections()
        self.assertEqual(sorted(sections), [1, 2, 3, 4, 5])
        for number, paper in sections.items():
            with self.subTest(paper=number):
                all_nums = [int(n) for n in re.findall(r'^\*\*Câu (\d+)(?: |\.)', paper, re.M)]
                self.assertEqual(all_nums, list(range(1, 12)))
                blocks = question_blocks(paper)
                self.assertEqual(sorted(blocks), list(range(1, 11)))
                for q in range(1, 11):
                    level, stem, block = blocks[q]
                    self.assertGreater(len(stem), 15, f'Missing question stem: paper {number}, question {q}')
                    expected_level = 'Biết' if q <= 6 else ('Hiểu' if q <= 9 else 'Vận dụng')
                    self.assertIn(expected_level, level)
                    if q <= 8:
                        self.assertIn('0,5 điểm', level)
                        options = re.findall(r'^([A-D])\. (.+?)\s*$', block, re.M)
                        self.assertEqual([x[0] for x in options], list('ABCD'))
                        self.assertEqual(len({x[1] for x in options}), 4)
                    else:
                        self.assertIn('1,0 điểm', level)
                self.assertRegex(paper, r'\*\*Câu 11\.\*\* Viết bài văn nghị luận')
                self.assertIn('**II. VIẾT (4,0 điểm)**', paper)
                self.assertIn('phỏng kể', paper)
        self.assertEqual(8 * .5 + 1 + 1 + 4, 10)

    def test_all_mcq_keys_match_question_options(self):
        for number, paper in paper_sections().items():
            match = re.search(r'## 7\.' + str(number) + r'\..*?\*\*Trắc nghiệm:\*\* (.*?)\n\n',
                              SOLUTIONS, re.S)
            self.assertIsNotNone(match, f'No key for paper {number}')
            keys = {int(q): label for q, label in re.findall(r'(\d+) \*\*([A-D])\*\*', match.group(1))}
            self.assertEqual(sorted(keys), list(range(1, 9)))
            blocks = question_blocks(paper)
            for q, expected in enumerate(EXPECTED[number], 1):
                options = dict(re.findall(r'^([A-D])\. (.+?)\s*$', blocks[q][2], re.M))
                with self.subTest(paper=number, question=q):
                    self.assertEqual(options[keys[q]].removesuffix('\\'), expected)

    def test_written_answers_models_and_flashcards(self):
        for number in range(1, 6):
            match = re.search(r'## 7\.' + str(number) + r'\..*?(?=\n## 7\.|\n# PHẦN 8)',
                              SOLUTIONS, re.S)
            self.assertIsNotNone(match)
            sec = match.group()
            for q in (9, 10, 11):
                self.assertIn(f'**Câu {q} –', sec)
            self.assertIn('**Trả lời mẫu:**', sec)
            model = re.search(r'### Bài viết mẫu Đề ' + str(number) + r'\s+(.*)', sec, re.S)
            self.assertIsNotNone(model)
            self.assertTrue(450 <= len(model.group(1).split()) <= 650)
        section = RECALL.split('## 5.3.', 1)[1]
        cards = re.findall(r'^(\d+)\. \*\*Hỏi:\*\*.*?\*\*Đáp:\*\* .+', section, re.M)
        self.assertEqual([int(x) for x in cards], list(range(1, 51)))


class PdfTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reader = PdfReader(PDF)
        cls.extracted = normalize('\n'.join(page.extract_text() or '' for page in cls.reader.pages))

    def test_pdf_contains_every_question_and_disclaimer(self):
        self.assertGreaterEqual(len(self.reader.pages), 20)
        self.assertNotIn('\ufffd', self.extracted)
        self.assertIn('không chứa đề thi', self.extracted)
        self.assertIn('không phải đề hoặc đáp án chính thức', self.extracted)
        self.assertIn('55 câu hỏi', self.extracted)
        for paper in paper_sections().values():
            for _, stem, _ in question_blocks(paper).values():
                self.assertIn(normalize(stem), self.extracted)
            stem = re.search(r'\*\*Câu 11\.\*\* ([^\n]+)', paper).group(1)
            # Markdown italic markers do not appear in rendered PDF text.
            self.assertIn(normalize(stem.replace('*', '')), self.extracted)
        for number in range(1, 6):
            self.assertIn(f'Bài viết mẫu Đề {number}', self.extracted)
        for index, page in enumerate(self.reader.pages[1:], 2):
            self.assertGreater(len(page.extract_text() or ''), 250, f'Almost-empty page {index}')

    def test_bookmarks_and_clickable_links(self):
        names = []
        def visit(outline):
            for item in outline:
                if isinstance(item, list):
                    visit(item)
                else:
                    names.append(item.title)
                    self.assertLess(self.reader.get_destination_page_number(item), len(self.reader.pages))
        visit(self.reader.outline)
        for n in range(1, 9):
            self.assertTrue(any(name.startswith(f'PHẦN {n} ·') for name in names))
        for n in range(1, 6):
            self.assertTrue(any(name.startswith(f'ĐỀ {n} ·') for name in names))
        self.assertGreater(sum(len(p.get('/Annots', [])) for p in self.reader.pages), 30)

    def test_vietnamese_fonts_cover_source_and_are_embedded(self):
        source = unicodedata.normalize('NFC', '\n'.join(
            p.read_text(encoding='utf-8') for p in (ROOT / 'de-cuong').glob('*.md')))
        for name in ('DejaVuSans', 'DejaVuSans-Bold', 'DejaVuSerif', 'DejaVuSerif-Bold'):
            face = TTFontFace(str(ROOT / 'fonts' / (name + '.ttf')))
            missing = sorted({c for c in source if c not in '\n\r\t' and ord(c) not in face.charToGlyph})
            self.assertEqual(missing, [], name)
        embedded = set()
        for page in self.reader.pages:
            fonts = page['/Resources'].get('/Font', {})
            for ref in fonts.values():
                font = ref.get_object()
                base = str(font.get('/BaseFont', ''))
                if 'DejaVu' not in base:
                    continue
                descriptor = font.get('/FontDescriptor')
                self.assertIsNotNone(descriptor)
                descriptor = descriptor.get_object()
                self.assertTrue(any(key in descriptor for key in ('/FontFile', '/FontFile2', '/FontFile3')))
                embedded.add(base.split('+')[-1])
        self.assertEqual(embedded, {'DejaVuSans', 'DejaVuSans-Bold', 'DejaVuSerif', 'DejaVuSerif-Bold'})


if __name__ == '__main__':
    unittest.main(verbosity=2)
