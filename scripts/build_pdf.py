#!/usr/bin/env python3
"""Compile the Typst sources into the review-outline PDF.

Run: python3 scripts/build_pdf.py
Requires: pip install typst==0.13.1
Fonts are read from ~/.fonts-collect (Be Vietnam Pro, Lora) with DejaVu as a fallback.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"
FONT_DIRS = [
    Path.home() / ".fonts-collect",
    Path("/usr/share/fonts/truetype/dejavu"),
]

try:
    import typst
except ImportError:
    sys.exit("Install the compiler first: pip install typst==0.13.1")


def main() -> int:
    font_paths = [str(p) for p in FONT_DIRS if p.is_dir()]
    start = time.time()
    typst.compile(str(SRC / "main.typ"), output=str(OUT), root=str(ROOT), font_paths=font_paths)
    size_mb = OUT.stat().st_size / 1_000_000
    print(f"Built {OUT.name}: {size_mb:.2f} MB in {time.time() - start:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
