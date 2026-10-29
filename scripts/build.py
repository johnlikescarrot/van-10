#!/usr/bin/env python3
"""Biên dịch và kiểm định chất lượng Đề cương ôn tập Giữa kì I Ngữ văn 10 KNTT (2026-2027)."""

from __future__ import annotations

import glob
import pathlib
import re
import sys

import pymupdf
import typst

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_MAIN = ROOT / "src" / "main.typ"
FONT_DIR = ROOT / "fonts"
OUT_PDF = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"

BANNED_PATTERNS = [
    ("Em-dash (—)", r"—"),
    ("Kí hiệu rơi phông dự phòng", r"[★▲◆✓✦▸⟹→]"),
    ("Công thức cũ 5K-1C", r"5K\s*[–-]\s*1C"),
    ("Từ ngữ cường điệu AI", r"(?i)\b(siêu tốc|vạn năng|bất bại|tuyệt chiêu|toàn bích|tuyệt mĩ|lắp rap|ăn chắc)\b"),
    ("Thuật ngữ tiếng Anh sáo rỗng", r"(?i)(Dual[- ]Coding|Cognitive Retention|Error Inoculation|Active Recall|Master Cheat Sheet|Spaced Repetition)"),
]


def audit_sources() -> list[str]:
    issues: list[str] = []
    for path_str in sorted(glob.glob(str(ROOT / "src" / "*.typ"))):
        path = pathlib.Path(path_str)
        text = path.read_text(encoding="utf-8")
        for label, pat in BANNED_PATTERNS:
            matches = list(re.finditer(pat, text))
            if matches:
                sample = matches[0].group(0)
                line_no = text[: matches[0].start()].count("\n") + 1
                issues.append(f"{path.name}:{line_no}: phát hiện {label} -> {sample!r}")

        # Đếm số từ các bài văn tham khảo trong essay-box
        for m in re.finditer(r'#essay-box\(title:\s*"([^"]+)"\)\[(.*?)\n\]', text, flags=re.S):
            title, body = m.group(1), m.group(2)
            clean = re.sub(r"[*_\[\]#\"“”(),.;:?!–-]", " ", body)
            words = [w for w in clean.split() if w]
            print(f"  [Bài văn] {title}: {len(words)} tiếng")
            if not (550 <= len(words) <= 950):
                issues.append(f"{path.name}: Độ dài '{title}' ({len(words)} tiếng) nằm ngoài ngưỡng 550-950 tiếng")
    return issues


def build_and_verify() -> int:
    print("1. Kiểm tra mã nguồn Typst...")
    issues = audit_sources()
    if issues:
        for item in issues:
            print("  LỖI:", item, file=sys.stderr)
        return 1

    print("2. Biên dịch PDF bằng Typst...")
    pdf_bytes = typst.compile(str(SRC_MAIN), font_paths=[str(FONT_DIR)])
    OUT_PDF.write_bytes(pdf_bytes)
    print(f"  Đã xuất {OUT_PDF.name} ({len(pdf_bytes) / 1024:.1f} KB)")

    print("3. Kiểm định phông chữ nhúng và bố cục trang PDF...")
    doc = pymupdf.open(str(OUT_PDF))
    fonts: set[str] = set()
    sparse_pages: list[tuple[int, int]] = []
    for idx, page in enumerate(doc):
        for f in page.get_fonts():
            fonts.add(f[3])
        char_count = len(page.get_text("text").strip())
        if char_count < 800 and idx > 0:
            sparse_pages.append((idx + 1, char_count))

    clean_fonts = sorted(f.split("+", 1)[-1] for f in fonts)
    print(f"  Tổng số trang: {len(doc)}")
    print(f"  Phông chữ nhúng ({len(clean_fonts)}): {', '.join(clean_fonts)}")

    fallback_fonts = [f for f in clean_fonts if any(k in f for k in ("DejaVu", "Libertinus", "Fallback"))]
    if fallback_fonts:
        print(f"  LỖI: Phát hiện phông dự phòng ngoài ý muốn: {fallback_fonts}", file=sys.stderr)
        return 1

    if sparse_pages:
        print(f"  CẢNH BÁO các trang ít chữ (<350 kí tự): {sparse_pages}")
    else:
        print("  Tất cả các trang nội dung đều có mật độ trình bày cân đối.")

    toc = doc.get_toc()
    print(f"  Số mục đánh dấu (PDF Bookmarks): {len(toc)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(build_and_verify())
