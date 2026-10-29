"""Rebuild editorial JSON and compile the publication offline from pinned dependencies."""
from pathlib import Path
import argparse
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    import typst
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf")
    args = parser.parse_args()
    # author scripts use repository-relative output paths.
    import os
    os.chdir(ROOT)
    for name in ("author_exams.py", "author_bank.py"):
        runpy.run_path(str(ROOT / "scripts" / name), run_name="__main__")
    from tests.test_content import validate_content
    validate_content()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        typst.compile(str(ROOT / "src/main.typ"), output=str(output), root=str(ROOT),
                      font_paths=[str(ROOT / "assets/fonts")], ignore_system_fonts=True)
    except typst.TypstError as exc:
        print(exc.diagnostic, file=sys.stderr)
        raise
    print(f"Compiled: {output}")


if __name__ == "__main__":
    main()
