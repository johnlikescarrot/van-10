#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create DejaVuMonoVN.ttf used for Vietnamese-aware monospaced mind maps.

DejaVu Sans Mono ships without a handful of Vietnamese precomposed glyphs.
This script copies the missing glyphs (and any composite components they
reference) from DejaVu Sans into DejaVu Sans Mono, forcing the monospace
advance width so ASCII diagrams stay aligned while Vietnamese renders fully.

Run once after copying the DejaVu TTF files into tools/fonts/:

    python tools/patch_font.py

Dependencies: fontTools (installed with matplotlib, or `pip install fonttools`).
"""
from pathlib import Path

from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
FONTS = HERE / "fonts"
MONO = FONTS / "DejaVuSansMono.ttf"
SANS = FONTS / "DejaVuSans.ttf"
OUT = FONTS / "DejaVuMonoVN.ttf"


def main() -> None:
    for path in (MONO, SANS):
        if not path.exists():
            raise SystemExit("Missing font: %s" % path)
    mono, sans = TTFont(MONO), TTFont(SANS)
    mono_cmap = mono.getBestCmap()
    sans_cmap = sans.getBestCmap()
    width = mono["hmtx"][mono_cmap[ord("A")]][0]

    # Latin Extended, Vietnamese precomposed codepoints, typography and box drawing.
    wanted = set(range(0x00C0, 0x0250)) | set(range(0x1E00, 0x1F00))
    wanted |= {
        0x2013, 0x2014, 0x2022, 0x2026, 0x2190, 0x2192,
        0x25A0, 0x2713, 0x2717, 0x2500, 0x2502, 0x251C, 0x2514,
    }
    targets = sorted(cp for cp in wanted if cp in sans_cmap and cp not in mono_cmap)

    seen = set()

    def add_glyph(name: str) -> None:
        if name in seen:
            return
        seen.add(name)
        glyph = sans["glyf"].get(name)
        if glyph is None:
            return
        if getattr(glyph, "isComposite", lambda: False)():
            for component in glyph.components:
                add_glyph(component.glyphName)
        if name not in mono["glyf"].glyphs:
            mono["glyf"].glyphs[name] = glyph
            mono.setGlyphOrder(list(mono.getGlyphOrder()) + [name])
        mono["hmtx"][name] = (width, 0)

    for cp in targets:
        add_glyph(sans_cmap[cp])
        for table in mono["cmap"].tables:
            table.cmap[cp] = sans_cmap[cp]

    mono.save(OUT)
    print("Wrote %s (%d copied glyphs, %d codepoints)." % (OUT, len(seen), len(targets)))


if __name__ == "__main__":
    main()
