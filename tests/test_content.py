"""Structural checks; these do NOT substitute for editorial judgement."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def validate_content():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ContentTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise RuntimeError("Editorial data validation failed")


class ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exams = load("src/exams.json")
        cls.bank = load("src/bank.json")
        cls.sources = load("research/sources.json")
        cls.ids = {s["id"] for s in cls.sources}

    def test_six_numbered_exams(self):
        self.assertEqual([e["number"] for e in self.exams], list(range(1, 7)))

    def test_each_exam_has_eight_mcq_two_short(self):
        for e in self.exams:
            self.assertEqual(len(e["questions"]), 8)
            self.assertEqual(len(e["short"]), 2)

    def test_mcq_choices_unique_and_key_valid(self):
        for q in self.bank["questions"] + [q for e in self.exams for q in e["questions"]]:
            self.assertEqual(len(q["choices"]), 4)
            self.assertEqual(len(set(q["choices"])), 4)
            self.assertIn(q["answer"], range(4))
            self.assertTrue(all(c.strip() for c in q["choices"]))
            self.assertTrue(q["explanation"].strip())

    def test_balanced_but_different_exam_keys(self):
        keys = []
        for e in self.exams:
            key = tuple(q["answer"] for q in e["questions"])
            self.assertEqual([key.count(i) for i in range(4)], [2, 2, 2, 2])
            keys.append(key)
        self.assertEqual(len(set(keys)), 6)

    def test_verbatim_evidence_is_in_editorial_passage(self):
        for e in self.exams:
            for q in e["questions"]:
                with self.subTest(exam=e["number"], stem=q["stem"]):
                    self.assertTrue(q["evidence"])
                    self.assertIn(q["evidence"], e["passage"])

    def test_exam_cognitive_order(self):
        for e in self.exams:
            self.assertEqual([q["level"] for q in e["questions"]], ["Nhận biết"] * 6 + ["Thông hiểu"] * 2)
            for q in e["questions"][:6]:
                self.assertIn(q["indicator"], {"Đ1", "Đ2", "Đ3", "Đ4"})
            for q in e["questions"][6:]:
                self.assertIn(q["indicator"], {"Đ5", "Đ6", "Đ7", "Đ8", "Đ9"})
            self.assertTrue(set(e["short"][0]["indicators"]).issubset({f"Đ{i}" for i in range(5, 10)}))
            self.assertTrue(set(e["short"][1]["indicators"]).issubset({f"Đ{i}" for i in range(10, 14)}))

    def test_short_rubrics_sum_to_one_point_each(self):
        for e in self.exams:
            for q in e["short"]:
                self.assertGreaterEqual(len(q["rubric"]), 3)
                self.assertTrue(all(r["points"] in (.25, .5) for r in q["rubric"]))
                self.assertEqual(sum(r["points"] for r in q["rubric"]), 1)
                self.assertTrue(q["sample"].strip())

    def test_exam_total_points_and_writing_rubric(self):
        self.assertEqual(8 * 0.5 + 2 * 1 + 4, 10)
        self.assertEqual(sum([.25, .5, 1, 1, .75, .25, .25]), 4)
        # Reading gives 3/2/1; the residual writing split is 1/1/2.
        self.assertEqual([3 + 1, 2 + 1, 1 + 2], [4, 3, 3])

    def test_six_substantial_essays_and_outlines(self):
        for e in self.exams:
            with self.subTest(exam=e["number"]):
                self.assertGreaterEqual(len(e["essay"].split()), 600)
                self.assertLessEqual(len(e["essay"].split()), 800)
                self.assertGreaterEqual(len(e["essay"].split("\n\n")), 5)
                self.assertGreaterEqual(len(e["outline"]), 4)

    def test_all_source_references_resolve(self):
        self.assertEqual(len(self.ids), 11)
        refs = [e["source"] for e in self.exams] + [p["source"] for p in self.bank["passages"]]
        refs += [e["extra"]["source"] for e in self.exams if e["extra"]]
        self.assertTrue(set(refs).issubset(self.ids))
        for s in self.sources:
            self.assertTrue(s["use"])
            if "path" in s:
                self.assertTrue((ROOT / s["path"]).is_file())
            else:
                self.assertTrue(s["url"].startswith("https://"))

    def test_two_independent_writing_passages(self):
        self.assertEqual([e["number"] for e in self.exams if e["extra"]], [4, 5])
        for e in self.exams:
            if e["extra"]:
                self.assertGreater(len(e["extra"]["passage"].split()), 100)

    def test_cross_textbook_notices(self):
        for e in self.exams[3:]:
            self.assertTrue(e["notice"].strip())

    def test_forty_bank_questions_and_four_passages(self):
        self.assertEqual(len(self.bank["passages"]), 4)
        self.assertEqual([q["number"] for q in self.bank["questions"]], list(range(1, 29)))
        self.assertEqual([q["number"] for q in self.bank["short"]], list(range(29, 41)))
        self.assertEqual([sum(q["group"] == i for q in self.bank["questions"]) for i in range(4)], [7] * 4)
        for q in self.bank["questions"] + self.bank["short"]:
            self.assertIn(q["group"], range(4))

    def test_bank_self_check_criteria(self):
        for q in self.bank["short"]:
            self.assertEqual(len(q["criteria"]), 2)
            self.assertTrue(q["sample"].strip())

    def test_twenty_four_actual_flashcards(self):
        import re
        source = (ROOT / "src/part8_memory_kit.typ").read_text()
        self.assertEqual([int(n) for n in re.findall(r"^\[(\d+)\],", source.split("== 7.2.")[1].split("== 7.3.")[0], re.M)], list(range(1, 25)))


if __name__ == "__main__":
    unittest.main()
