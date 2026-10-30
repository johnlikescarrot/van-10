"""Build đề cương Ngữ văn 10 (KNTT) — chạy từ thư mục gốc repo.

    python3 build.py

Yêu cầu: pip install typst pymupdf
"""
import typst
import pymupdf

OUT = "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"

pdf = typst.compile("src/main.typ", root="src", font_paths=["fonts"])
open(OUT, "wb").write(pdf)

d = pymupdf.open(OUT)
d.set_metadata({
    "title": "Đề cương ôn tập Giữa kì I Ngữ văn 10 – Kết nối tri thức (2026–2027)",
    "author": "Tài liệu Ôn tập Chuyên sâu Ngữ văn 10 – GDPT 2018",
    "subject": (
        "Đề cương ôn tập giữa học kì I môn Ngữ văn lớp 10, bộ Kết nối tri thức với "
        "cuộc sống, năm học 2026–2027: ma trận – bản đặc tả, thần thoại, tiếng Việt, "
        "kĩ năng đọc hiểu, kĩ năng viết, 8 đề minh họa, hệ thống ghi nhớ."
    ),
    "keywords": (
        "Ngữ văn 10, Kết nối tri thức, giữa kì 1, thần thoại, đề cương ôn tập, "
        "ma trận đề, 2026-2027"
    ),
    "creator": "Typst 0.15.0",
    "producer": "Typst 0.15.0",
})
d.saveIncr()
d.close()

check = pymupdf.open(OUT)
print(f"{OUT}: {check.page_count} trang, {len(check.get_toc())} bookmark")
