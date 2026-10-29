#!/usr/bin/env python3
"""Biên dịch đề cương từ nguồn Typst."""
from pathlib import Path
import typst

root = Path(__file__).resolve().parent.parent
src = root / "src" / "main.typ"
out = root / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"
typst.compile(str(src), output=str(out), root=str(root))
print(f"Đã tạo {out.name}")
