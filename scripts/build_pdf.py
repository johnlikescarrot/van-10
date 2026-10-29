#!/usr/bin/env python3
"""Build and check the study guide PDF.

The document is written in Typst and lives in `src/`. This script compiles it,
then checks the result before overwriting the published file at the repo root:

  * the fonts the design system asks for are embedded (Be Vietnam Pro, Lora);
  * every Vietnamese character in the source has a real glyph, so nothing
    silently falls back to a system font;
  * the PDF outline and page count are sane.

Usage:
    python3 scripts/build_pdf.py            # build and publish
    python3 scripts/build_pdf.py --dry-run  # build to build/out.pdf only
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import typst
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "main.typ"
FONTS = ROOT / "build" / "fonts"
STAGING = ROOT / "build" / "out.pdf"
PUBLISHED = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"

REQUIRED_FONTS = ("BeVietnamPro", "Lora")
MIN_PAGES = 60


def vietnamese_letters() -> set[str]:
    """The letters used to write Vietnamese, lowercase and deduplicated.

    Vietnamese is written with the Latin alphabet plus precomposed tone and
    circumflex/horn marks, so the set is small and closed. The range covers
    Latin-1 Supplement through Latin Extended Additional, which holds every
    precomposed letter the language needs.
    """
    letters: set[str] = set()
    for code in range(0x00C0, 0x1F00):
        char = chr(code)
        if unicodedata.combining(char):
            continue
        name = unicodedata.name(char, "")
        if "LATIN" in name and ("WITH" in name or char in "đĐ"):
            letters.add(char.lower())
    letters.update("ăâđêôơư")
    return letters


def check_glyph_coverage() -> list[str]:
    """Report source characters the built fonts cannot draw."""
    from fontTools.ttLib import TTFont

    covered: set[str] = set()
    for path in sorted(FONTS.glob("*.ttf")):
        cmap = TTFont(str(path)).getBestCmap()
        covered.update(chr(code) for code in cmap)

    problems: list[str] = []
    letters = vietnamese_letters()
    for source in sorted((ROOT / "src").glob("*.typ")):
        text = source.read_text(encoding="utf-8")
        missing = sorted({c for c in text if c.lower() in letters and c not in covered})
        if missing:
            problems.append(f"{source.name}: no glyph for {' '.join(missing)}")
    return problems


def check_pdf(path: Path) -> tuple[int, list[str]]:
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    problems: list[str] = []

    if pages < MIN_PAGES:
        problems.append(f"only {pages} pages; expected at least {MIN_PAGES}")
    if not reader.outline:
        problems.append("no PDF outline (bookmarks) was written")

    raw = path.read_bytes()
    embedded = {name.decode() for name in re.findall(rb"/BaseFont\s*/([A-Za-z0-9+\-]+)", raw)}
    joined = "".join(embedded)
    for font in REQUIRED_FONTS:
        if font not in joined:
            problems.append(f"font {font} is not embedded; found {sorted(embedded)}")

    return pages, problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="do not overwrite the published PDF")
    args = parser.parse_args()

    subprocess.run([sys.executable, str(ROOT / "scripts" / "fetch_fonts.py")], check=True)

    glyph_problems = check_glyph_coverage()
    for problem in glyph_problems:
        print(f"  glyph warning: {problem}")

    print("Compiling src/main.typ ...")
    typst.compile(str(SRC), output=str(STAGING), font_paths=[str(FONTS)])

    pages, problems = check_pdf(STAGING)
    print(f"  {pages} pages, {STAGING.stat().st_size:,} bytes")
    for problem in problems:
        print(f"  ERROR: {problem}")
    if problems:
        return 1

    if args.dry_run:
        print(f"Dry run: left the build at {STAGING.relative_to(ROOT)}")
        return 0

    PUBLISHED.write_bytes(STAGING.read_bytes())
    print(f"Published {PUBLISHED.name} ({pages} pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
