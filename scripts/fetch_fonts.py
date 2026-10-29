#!/usr/bin/env python3
"""Download the two document fonts and convert them to TrueType.

The document uses Be Vietnam Pro (body, tables, cover) and Lora (literary
passages and model essays). Neither ships with the operating system, so the
build pulls both from the npm registry as @fontsource packages, unpacks the
WOFF2 subsets, and merges each subset into one TrueType file per weight.
Typst cannot read WOFF2, and it cannot follow the unicode-range splitting that
@fontsource uses, so the merge step is required.

Output: build/fonts/*.ttf

Usage:
    python3 scripts/fetch_fonts.py            # fetch and convert
    python3 scripts/fetch_fonts.py --check    # only report what is missing
"""

from __future__ import annotations

import argparse
import io
import sys
import tarfile
import urllib.request
from pathlib import Path

from fontTools import merge as ftmerge
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "build" / "fonts"
TMP = ROOT / "build" / "_subsets"

# name, npm package, subsets to merge, weights to build, styles to build
FAMILIES = [
    (
        "be-vietnam-pro",
        "@fontsource/be-vietnam-pro",
        ["latin", "latin-ext", "vietnamese"],
        [400, 500, 600, 700],
        ["normal", "italic"],
    ),
    (
        "lora",
        "@fontsource/lora",
        ["latin", "latin-ext", "vietnamese"],
        [400, 600, 700],
        ["normal", "italic"],
    ),
]

WEIGHT_NAMES = {400: "", 500: " Medium", 600: " SemiBold", 700: " Bold"}
REGISTRY = "https://registry.npmjs.org"


def fetch_tarball(package: str) -> bytes:
    """Read the tarball of the pinned release of an npm package."""
    slug = package.replace("/", "%2f")
    import json

    with urllib.request.urlopen(f"{REGISTRY}/{slug}", timeout=60) as response:
        meta = json.load(response)
    version = "5.3.0"
    url = meta["versions"][version]["dist"]["tarball"]
    with urllib.request.urlopen(url, timeout=120) as response:
        return response.read()


def unpack(tarball: bytes, target: Path) -> None:
    """Unpack an npm tarball, dropping its leading `package/` folder.

    Files are written one at a time instead of using extractall, so no member
    can escape `target` through a `..` path and no Python-version difference in
    tarfile filters matters.
    """
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(tarball)) as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            parts = Path(member.name).parts
            if len(parts) < 2 or ".." in parts:
                continue
            destination = target.joinpath(*parts[1:])
            destination.parent.mkdir(parents=True, exist_ok=True)
            source = archive.extractfile(member)
            if source is not None:
                destination.write_bytes(source.read())


def flatten_woff2(path: Path) -> Path:
    """Rewrite one WOFF2 subset as a plain TrueType file Typst can read."""
    font = TTFont(str(path))
    font.flavor = None
    TMP.mkdir(parents=True, exist_ok=True)
    flat = TMP / (path.stem + ".ttf")
    font.save(str(flat))
    return flat


def build_one(family: str, subsets: list[str], weight: int, style: str) -> Path | None:
    parts = []
    for subset in subsets:
        woff = ROOT / "build" / family / "files" / f"{family}-{subset}-{weight}-{style}.woff2"
        if woff.exists():
            parts.append(str(flatten_woff2(woff)))
    if not parts:
        return None

    if len(parts) == 1:
        font = TTFont(parts[0])
    else:
        merger = ftmerge.Merger()
        merger.recalcTimestamp = False
        font = merger.merge(parts)

    italic = style == "italic"
    display_family = {"be-vietnam-pro": "Be Vietnam Pro", "lora": "Lora"}[family]
    suffix = WEIGHT_NAMES[weight] + (" Italic" if italic else "")
    names = font["name"]
    for name_id, value in ((1, display_family + suffix), (4, display_family + suffix), (16, display_family)):
        names.setName(value, name_id, 3, 1, 0x409)
    names.setName(suffix.strip() or "Regular", 17, 3, 1, 0x409)

    os2 = font["OS/2"]
    os2.usWeightClass = weight
    os2.fsSelection = (1 if italic else 0) | (0x40 if weight == 400 and not italic else 0) | (0x20 if weight >= 700 else 0)
    font["head"].macStyle = (2 if italic else 0) | (1 if weight >= 700 else 0)

    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f"{family}-{weight}-{style}.ttf"
    font.save(str(target))
    return target


def expected_files() -> list[Path]:
    return [
        OUT / f"{family}-{weight}-{style}.ttf"
        for family, _, _, weights, styles in FAMILIES
        for weight in weights
        for style in styles
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report missing fonts and exit")
    args = parser.parse_args()

    missing = [path for path in expected_files() if not path.exists()]
    if args.check:
        if missing:
            print("Missing fonts:")
            for path in missing:
                print(f"  {path.relative_to(ROOT)}")
            return 1
        print(f"All {len(expected_files())} font files are present.")
        return 0

    if not missing:
        print(f"All {len(expected_files())} font files are already present.")
        return 0

    for family, package, subsets, weights, styles in FAMILIES:
        target_dir = ROOT / "build" / family
        if not target_dir.exists():
            print(f"Downloading {package} ...")
            unpack(fetch_tarball(package), target_dir)
        built = 0
        for weight in weights:
            for style in styles:
                if build_one(family, subsets, weight, style) is not None:
                    built += 1
        print(f"  {family}: wrote {built} TrueType files")

    still_missing = [path for path in expected_files() if not path.exists()]
    if still_missing:
        print("Build incomplete:", file=sys.stderr)
        for path in still_missing:
            print(f"  {path}", file=sys.stderr)
        return 1
    print("Fonts ready in build/fonts/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
