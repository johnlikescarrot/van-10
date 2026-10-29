#!/usr/bin/env python3
"""Build the study guide from its Typst sources and bundled fonts."""
from pathlib import Path
import typst

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"

if __name__ == "__main__":
    typst.compile(
        str(ROOT / "src/main.typ"),
        output=str(OUTPUT),
        root=str(ROOT),
        font_paths=[str(ROOT / "fonts")],
    )
    print(f"Built {OUTPUT.name}")
