#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  Build script — Đề cương ôn tập Giữa kì I Ngữ văn 10 (KNTT) 2026 – 2027
#  Yêu cầu: Python >= 3.9 (dùng gói pip "typst" — không cần cài Typst CLI).
#  Cách dùng:  ./build.sh                     -> xuất PDF ở thư mục gốc repo
#              ./build.sh /tmp/out.pdf        -> xuất PDF ra đường dẫn khác
# ---------------------------------------------------------------------------
set -euo pipefail

cd "$(dirname "$0")"

OUT="${1:-DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf}"
VENV_DIR="${VENV_DIR:-.venv}"

if [ ! -x "$VENV_DIR/bin/python" ]; then
  echo "[1/3] Tạo môi trường ảo $VENV_DIR ..."
  python3 -m venv "$VENV_DIR"
  "$VENV_DIR/bin/pip" install --quiet --upgrade pip
  "$VENV_DIR/bin/pip" install --quiet typst
else
  echo "[1/3] Dùng môi trường ảo có sẵn $VENV_DIR"
fi

echo "[2/3] Biên dịch Typst -> $OUT"
"$VENV_DIR/bin/python" - "$OUT" <<'PY'
import sys, typst
out = sys.argv[1]
# font_paths: bắt buộc, vì repo tự chứa trọn bộ phông (Lora, Be Vietnam Pro).
typst.compile("src/main.typ", output=out, root=".", font_paths=["src/fonts"])
print("   -> OK:", out)
PY

echo "[3/3] Hoàn tất."
