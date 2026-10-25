# Bản in (A4) – sinh tự động

| Tệp | Dùng để |
|---|---|
| `De-cuong-on-tap-GK1-Ngu-van-10.docx` | In toàn bộ đề cương (8 phần, có bìa – mục lục – số trang) |
| `De-minh-hoa-va-dap-an-GK1.docx` | In riêng 3 đề minh hoạ + đáp án để làm bài 90 phút |

**Sinh lại:**

```bash
pip install python-docx
python3 tools/build_docx.py
```

Cấu hình in gợi ý: A4 · lề trên/dưới 2 cm · trái 2,8 cm · phải 2 cm · Times New Roman 13 · giãn dòng 1,18.
Không sửa trực tiếp các tệp `.docx` trong thư mục này — sửa Markdown trong `de-cuong-on-tap/` rồi chạy lại script.
