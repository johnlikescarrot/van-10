#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf from the Typst
sources in src/.

Environment note: Typst itself is not available here (no Rust toolchain and
GitHub release assets are blocked), so this script transpiles the Typst sources
into a ReportLab Platypus document. The design system (colors, boxes, tables,
badges, cover page, TOC, headers/footers) is ported from src/template.typ.
"""
import math
import os
import re
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, Color
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    NextPageTemplate, Table, TableStyle, HRFlowable, Flowable,
    KeepTogether,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as canvas_module

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf"
FONT_DIR = Path("/tmp/humanizer-fonts")
FONT_DIR.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt

# -----------------------------------------------------------------------------
# Colors (ported from src/template.typ)
# -----------------------------------------------------------------------------
C = {
    "navy": HexColor("#14284B"),
    "indigo": HexColor("#1E4976"),
    "blue-soft": HexColor("#EEF4FB"),
    "blue-bdr": HexColor("#B8D0EB"),
    "red": HexColor("#B42318"),
    "red-soft": HexColor("#FEF3F2"),
    "red-bdr": HexColor("#FECDCA"),
    "amber": HexColor("#B54708"),
    "gold": HexColor("#D97706"),
    "gold-soft": HexColor("#FFFAEB"),
    "gold-bdr": HexColor("#FEDF89"),
    "teal": HexColor("#0F6CBD"),
    "jade": HexColor("#0E6F5C"),
    "jade-soft": HexColor("#ECFDF3"),
    "jade-bdr": HexColor("#ABEFC6"),
    "purple": HexColor("#5925DC"),
    "purple-soft": HexColor("#F4F3FF"),
    "purple-bdr": HexColor("#D9D6FE"),
    "slate": HexColor("#344054"),
    "muted": HexColor("#667085"),
    "bg-neutral": HexColor("#F8FAFC"),
    "border": HexColor("#D0D5DD"),
    "ink": HexColor("#182230"),
    "white": white,
    "cover-dark": HexColor("#1D355E"),
    "cover-edge": HexColor("#3B5B8C"),
    "cover-gold": HexColor("#FCD34D"),
    "cover-light": HexColor("#93C5FD"),
    "cover-ice": HexColor("#E2E8F0"),
    "cover-circle1": HexColor("#1E3A6D"),
    "cover-circle1-stroke": HexColor("#2E5496"),
    "cover-circle2": HexColor("#1A335E"),
    "cover-circle2-stroke": HexColor("#2B4C85"),
}

# Badge specs: (label, background, foreground, border)
BADGE_SPECS = {
    "biet": ("TN BIẾT", HexColor("#EEF4FB"), HexColor("#1E4976"), HexColor("#B8D0EB")),
    "hieu": ("TN HIỂU", HexColor("#ECFDF3"), HexColor("#0E6F5C"), HexColor("#ABEFC6")),
    "vd":   ("VÍ DỤ",  HexColor("#FFFAEB"), HexColor("#B54708"), HexColor("#FEDF89")),
}


def co(value):
    """Resolve a color value: Color, HexColor result, named color, or hex string."""
    if isinstance(value, Color):
        return value
    if isinstance(value, str):
        if value in C:
            return C[value]
        if value.startswith("#"):
            return HexColor(value)
    return C["ink"]


# -----------------------------------------------------------------------------
# Fonts: DejaVu family + synthetically obliqued variants (fontTools)
# -----------------------------------------------------------------------------
DEJAVU = Path("/usr/share/fonts/truetype/dejavu")
FONT_DIR = Path("/tmp/van10-fonts")
FONT_DIR.mkdir(parents=True, exist_ok=True)

FONT_MAP = {
    "DejaVuSans": "DejaVuSans.ttf",
    "DejaVuSans-Bold": "DejaVuSans-Bold.ttf",
    "DejaVuSerif": "DejaVuSerif.ttf",
    "DejaVuSerif-Bold": "DejaVuSerif-Bold.ttf",
    "DejaVuSansMono": "DejaVuSansMono.ttf",
}


def slant_font(src_path, dst_path, angle=11):
    """Create a synthetically obliqued copy of a TrueType font (x' = x + y*tan(a))."""
    try:
        from fontTools.ttLib import TTFont
        from fontTools.ttLib.tables._g_l_y_f import (
            Glyph, GlyphCoordinates, ARG_1_AND_2_ARE_WORDS,
        )
        import math
    except Exception:
        return False
    try:
        font = TTFont(src_path)
        if "glyf" not in font:
            return False
        t = math.tan(math.radians(angle))
        glyf = font["glyf"]
        replaced = {}
        for name in font.getGlyphOrder():
            g = glyf[name]  # table __getitem__ triggers lazy expand
            if g.isComposite():
                for comp in g.components:
                    if comp.flags & ARG_1_AND_2_ARE_WORDS:
                        comp.x = comp.x + t * comp.y
                replaced[name] = g
            elif g.numberOfContours > 0:
                coords, endPts, flags = g.getCoordinates(glyf)
                ng = Glyph()
                ng.numberOfContours = g.numberOfContours
                ng.endPtsOfContours = list(endPts)
                ng.flags = list(flags)
                ng.coordinates = GlyphCoordinates(
                    [(x + t * y, y) for (x, y) in coords]
                )
                ng.program = getattr(g, "program", None)
                replaced[name] = ng
            else:
                replaced[name] = g
        glyf.glyphs.clear()
        glyf.glyphs.update(replaced)
        font["head"].macStyle |= 1  # italic bit
        font["post"].italicAngle = -angle
        font.save(dst_path)
        return True
    except Exception as e:  # noqa: BLE001
        print(f"WARNING: slant_font({src_path}) failed: {e}")
        return False


def register_fonts():
    for name, file in FONT_MAP.items():
        pdfmetrics.registerFont(TTFont(name, str(DEJAVU / file)))
    # Synthetic obliques so *italic* markup has a real font.
    for base in ("DejaVuSans", "DejaVuSerif"):
        for weight in ("", "-Bold"):
            src = DEJAVU / f"{base}{weight}.ttf"
            dst = FONT_DIR / f"{base}{weight}-Oblique.ttf"
            fontname = f"{base}{weight}-Oblique"
            if slant_font(src, dst):
                pdfmetrics.registerFont(TTFont(fontname, str(dst)))
            else:
                pdfmetrics.registerFont(TTFont(fontname, str(src)))
    pdfmetrics.registerFontFamily(
        "DejaVuSans",
        normal="DejaVuSans",
        bold="DejaVuSans-Bold",
        italic="DejaVuSans-Oblique",
        boldItalic="DejaVuSans-Bold-Oblique",
    )
    pdfmetrics.registerFontFamily(
        "DejaVuSerif",
        normal="DejaVuSerif",
        bold="DejaVuSerif-Bold",
        italic="DejaVuSerif-Oblique",
        boldItalic="DejaVuSerif-Bold-Oblique",
    )


register_fonts()

# Glyph-coverage safety: replace glyphs missing from a font with a fallback.
def cmap_set(fontname):
    font = pdfmetrics.getFont(fontname)
    try:
        cmap = font.getEncoding().cmapping  # may not exist
    except Exception:
        cmap = {}
    # Simpler: check via stringWidth is unreliable; use ttFont if available.
    return set()


# Known risky glyphs and safe ASCII fallbacks (used only if missing from font).
GLYPH_FALLBACK = {
    "\u2726": "*",  # ✦
    "\u25C6": "*",  # ◆
    "\u2605": "*",  # ★
    "\u25B2": "^",  # ▲
    "\u25B8": ">",  # ▸
    "\u2713": "*",  # ✓
    "\u27F9": "=>",  # ⟹
    "\u2192": "->",  # →
    "\u27F6": "=>",  # ⟶
}


def sanitize(text, fontname="DejaVuSans"):
    try:
        tt = pdfmetrics.getFont(fontname).ttFont
    except Exception:
        return text
    if "cmap" not in tt:
        return text
    cmap = tt["cmap"].getcmap(3, 1) or tt["cmap"].getcmap(0, 0) or tt["cmap"].tables[0]
    out = []
    for ch in text:
        if ord(ch) in cmap.cmap:
            out.append(ch)
        elif ch in GLYPH_FALLBACK:
            out.append(GLYPH_FALLBACK[ch])
        else:
            out.append("?")
    return "".join(out)


# -----------------------------------------------------------------------------
# Typst mini-parser
# -----------------------------------------------------------------------------
CONFIG_CALLS = {"set", "show", "import", "include", "let"}
BOX_CALLS = {
    "mnemonic-box": "mnemonic",
    "trap-box": "trap",
    "formula-box": "formula",
    "answer-box": "answer",
    "passage-box": "passage",
    "essay-box": "essay",
    "callout": "callout",
}
INLINE_CALLS = {"strong", "text", "upper", "badge-biet", "badge-hieu", "badge-vd"}


class Val:
    __slots__ = ("kind", "data")

    def __init__(self, kind, data):
        self.kind = kind
        self.data = data

    def __repr__(self):
        return f"Val({self.kind}, {self.data!r})"


def parse_size(s):
    s = s.strip()
    m = re.match(r"^([0-9]+(?:\.[0-9]+)?)(pt|mm|cm|em|fr|%)$", s)
    if not m:
        return None
    return Val("size", (float(m.group(1)), m.group(2)))


def classify_arg(s):
    s = s.strip()
    if not s:
        return None
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return Val("str", s[1:-1].replace('\\"', '"'))
    if s[0] == "[" and s[-1] == "]":
        return Val("content", s[1:-1])
    if s[0] == "(" and s[-1] == ")":
        inner = s[1:-1].strip()
        parts = split_args(inner)
        if all(":" in p and depth_colon(p) for p in parts if p.strip()):
            pairs = []
            for p in parts:
                k, _, v = p.partition(":")
                pairs.append((k.strip(), classify_arg(v.strip())))
            return Val("dict", pairs)
        return Val("array", [classify_arg(p) for p in parts if p.strip()])
    sz = parse_size(s)
    if sz:
        return sz
    low = s.lower()
    if low == "true":
        return Val("bool", True)
    if low == "false":
        return Val("bool", False)
    if low == "none":
        return Val("none", None)
    if s.startswith("#"):
        return Val("colorref", s[1:])
    if s.startswith("rgb(") and s.endswith(")"):
        inner = s[4:-1].strip()
        if inner.startswith('"') and inner.endswith('"'):
            return Val("color", inner[1:-1])
    return Val("bare", s)


def depth_colon(s):
    """True if the first ':' in s is at bracket depth 0."""
    depth = 0
    in_str = False
    for ch in s:
        if in_str:
            if ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        elif ch == ":" and depth == 0:
            return True
    return False


def split_args(inner):
    """Split top-level function-call arguments by commas at depth 0."""
    parts = []
    depth = 0
    in_str = False
    cur = []
    i = 0
    while i < len(inner):
        ch = inner[i]
        if in_str:
            cur.append(ch)
            if ch == '"':
                in_str = False
            i += 1
            continue
        if ch == '"':
            in_str = True
            cur.append(ch)
            i += 1
            continue
        if ch in "([{":
            depth += 1
            cur.append(ch)
            i += 1
            continue
        if ch in ")]}":
            depth -= 1
            cur.append(ch)
            i += 1
            continue
        if ch == "," and depth == 0:
            parts.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    if cur or parts:
        parts.append("".join(cur))
    return [p for p in parts if p.strip()]


def parse_call(text, pos):
    """Parse a call starting at text[pos] == '#'.
    Returns (node, end_pos) where node = (name, args_list, kwargs_dict).
    """
    pos += 1  # skip '#'
    m = re.match(r"[A-Za-z][A-Za-z0-9-]*", text[pos:])
    if not m:
        return None, pos
    name = m.group(0)
    pos += m.end()
    while pos < len(text) and text[pos] in " \t":
        pos += 1
    if pos >= len(text) or text[pos] not in "([{":
        return (name, [], {}), pos
    delim = text[pos]
    close = {"(": ")", "[": "]", "{": "}"}[delim]
    pos += 1
    depth = 1
    in_str = False
    start = pos
    while pos < len(text) and depth > 0:
        ch = text[pos]
        if in_str:
            if ch == '"':
                in_str = False
            pos += 1
            continue
        if ch == '"':
            in_str = True
            pos += 1
            continue
        if ch == "\\":
            pos += 2
            continue
        if ch == delim:
            depth += 1
            pos += 1
            continue
        if ch == close:
            depth -= 1
            pos += 1
            continue
        pos += 1
    inner = text[start:pos - 1]
    args, kwargs = [], {}
    for raw in split_args(inner):
        raw = raw.strip()
        if ":" in raw and depth_colon(raw):
            k, _, v = raw.partition(":")
            kwargs[k.strip()] = classify_arg(v.strip())
        else:
            v = classify_arg(raw)
            if v is not None:
                args.append(v)
    return (name, args, kwargs), pos


def balanced_call(text):
    """Return True if a '#'-call starting at index 0 of text has balanced
    brackets/parens/braces across the whole string."""
    depth = 0
    in_str = False
    i = 0
    while i < len(text):
        ch = text[i]
        if in_str:
            if ch == '"':
                in_str = False
            i += 1
            continue
        if ch == '"':
            in_str = True
            i += 1
            continue
        if ch == "\\":
            i += 2
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        i += 1
    return depth == 0


# -----------------------------------------------------------------------------
# Top-level scan: turn file text into a list of items.
# -----------------------------------------------------------------------------
HEADING_RE = re.compile(r"^(=+)\s+(.+)$")
LIST_BULLET_RE = re.compile(r"^([-•])\s+(.+)$")
LIST_NUM_RE = re.compile(r"^(\d+)\.\s+(.+)$")


def scan_items(text):
    items = []
    lines = text.split("\n")
    i = 0
    n = len(lines)

    def flush_para(buf):
        if buf:
            s = " ".join(x.strip() for x in buf).strip()
            if s:
                items.append(("para", s))
            buf.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            flush_para([])
            i += 1
            continue

        if stripped.startswith("#"):
            # Gather a possibly multi-line block call.
            buf_lines = [stripped]
            j = i + 1
            while j < n and not balanced_call(" ".join(buf_lines) + " " + lines[j].strip()):
                buf_lines.append(lines[j].strip())
                j += 1
            call_text = " ".join(buf_lines)
            node, _ = parse_call(call_text, 0)
            if node and node[0] not in CONFIG_CALLS:
                flush_para([])
                items.append(("block", node))
            i = j if j > i + 1 else i + 1
            continue

        m = HEADING_RE.match(stripped)
        if m:
            flush_para([])
            items.append(("heading", int(len(m.group(1))), sanitize(m.group(2).strip())))
            i += 1
            continue

        m = LIST_BULLET_RE.match(stripped)
        if m:
            flush_para([])
            items.append(("list", "bullet", sanitize(m.group(2).strip())))
            i += 1
            continue

        m = LIST_NUM_RE.match(stripped)
        if m:
            flush_para([])
            items.append(("list", "num", int(m.group(1)), sanitize(m.group(2).strip())))
            i += 1
            continue

        # Paragraph: consume until blank line or a line starting a new item.
        buf = [line]
        j = i + 1
        while j < n:
            nxt = lines[j]
            st = nxt.strip()
            if not st:
                break
            if (st.startswith("#") or HEADING_RE.match(st)
                    or LIST_BULLET_RE.match(st) or LIST_NUM_RE.match(st)):
                break
            buf.append(nxt)
            j += 1
        flush_para(buf)
        i = j

    return items


# -----------------------------------------------------------------------------
# Inline parse: turns a markup string into segments.
# -----------------------------------------------------------------------------
SEGMENT_CALL_RE = re.compile(r"^([A-Za-z][A-Za-z0-9-]*)\(([^()]*)\)\s*(\[.*)$", re.S)


def parse_inline(text):
    """Return a list of segments:
    ('text', text, bold, italic, opts) | ('break',) | ('badge', kind)
    | ('block', node)
    """
    segs = []
    i = 0
    n = len(text)
    bold = False
    italic = False

    def push(txt, b, it, opts=None):
        if txt != "" or opts is not None:
            segs.append(("text", txt, b, it, opts))

    while i < n:
        c = text[i]
        if c == "\\":
            nxt = text[i + 1] if i + 1 < n else ""
            if nxt == "\\":
                push("", bold, italic)
                segs.append(("break",))
                i += 2
                continue
            if nxt == "*":
                segs.append(("text", "*", bold, italic, None))
                i += 2
                continue
            if nxt == " ":
                segs.append(("text", " ", bold, italic, None))
                i += 2
                continue
            segs.append(("text", nxt, bold, italic))
            i += 2
            continue
        if c == "*":
            italic = not italic
            i += 1
            continue
        if c == "#":
            node, end = parse_call(text, i)
            if node is None:
                segs.append(("text", "#", bold, italic))
                i += 1
                continue
            name = node[0]
            if name in INLINE_CALLS:
                push("", bold, italic)
                segs.append(("call", node))
                i = end
                continue
            # Block-level call appearing inline: render as its own flowable.
            push("", bold, italic)
            segs.append(("block", node))
            i = end
            continue
        segs.append(("text", c, bold, italic, None))
        i += 1
    push("", bold, italic)
    return segs


class BadgeFlowable(Flowable):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind
        self.text, self.bg, self.fg, self.bdr = BADGE_SPECS[kind]
        self.width = 0
        self.height = 0

    def wrap(self, avail_width, avail_height):
        size = 7.8
        w = pdfmetrics.stringWidth(self.text, "DejaVuSans-Bold", size) + 10
        h = size + 4
        self.width = w
        self.height = h
        return (w, h)

    def draw(self):
        canv = self.canv
        canv.setFillColor(self.bg)
        canv.setStrokeColor(self.bdr)
        canv.setLineWidth(0.6)
        canv.roundRect(0, 0, self.width, self.height, 3, stroke=1, fill=1)
        canv.setFillColor(self.fg)
        canv.setFont("DejaVuSans-Bold", 7.8)
        canv.drawString(5, 2, self.text)


# -----------------------------------------------------------------------------
# Block rendering
# -----------------------------------------------------------------------------
class BoxFlowable(Flowable):
    """A colored box with optional left accent bar, border and rounded corners,
    containing a list of child flowables. Splits across pages by grouping
    children (each piece re-draws its own background)."""

    def __init__(self, children, spec):
        super().__init__()
        self.children = children
        self.spec = spec
        self.width = 0
        self.height = 0

    def wrap(self, avail_width, avail_height):
        pad = self.spec["pad"]
        self.max_w = avail_width - pad["l"] - pad["r"]
        total = pad["t"] + pad["b"]
        for ch in self.children:
            ch.wrap(self.max_w, avail_height - total)
            total += ch.height
        self.width = avail_width
        self.height = total
        return (avail_width, total)

    def split(self, avail_width, avail_height):
        pad = self.spec["pad"]
        limit = avail_height - pad["t"] - pad["b"]
        pieces = []
        group = []
        group_h = 0
        for ch in self.children:
            ch.wrap(self.max_w, avail_height)
            h = ch.height
            if group and group_h + h > limit:
                pieces.append(BoxFlowable(list(group), self.spec))
                group = [ch]
                group_h = h
            else:
                group.append(ch)
                group_h += h
        if group:
            pieces.append(BoxFlowable(list(group), self.spec))
        if not pieces:
            # Empty box: postpone unless it fits in the remaining space.
            self.wrap(avail_width, avail_height)
            return [] if self.height > avail_height else [self]
        # Nothing fits in the remaining space: postpone to a fresh page.
        pieces[0].wrap(avail_width, avail_height)
        if pieces[0].height > avail_height:
            return []
        return pieces

    def draw(self):
        canv = self.canv
        s = self.spec
        w, h = self.width, self.height
        pad = s["pad"]
        if s["fill"]:
            canv.setFillColor(s["fill"])
            canv.roundRect(0, 0, w, h, s["radius"], stroke=0, fill=1)
        if s["accent"]:
            canv.setFillColor(s["accent"])
            canv.rect(0, 0, s["accent_w"], h, stroke=0, fill=1)
        if s.get("stroke_w", 0):
            canv.setStrokeColor(s.get("stroke", C["border"]))
            canv.setLineWidth(s["stroke_w"])
            canv.rect(0, 0, w, h, stroke=1, fill=0)
        cx = pad["l"] + (s["accent_w"] if s["accent"] else 0)
        cy = h - pad["t"]
        for ch in self.children:
            ch.drawOn(canv, cx, cy - ch.height)
            cy -= ch.height


def box_spec(kind, **overrides):
    base = {
        "mnemonic": dict(fill=C["gold-soft"], accent=C["amber"], bdr=C["gold-bdr"],
                         stroke_w=0.6, radius=5, pad=dict(l=13, r=13, t=11, b=11), accent_w=4.5),
        "trap": dict(fill=C["red-soft"], accent=C["red"], bdr=C["red-bdr"],
                     stroke_w=0.6, radius=5, pad=dict(l=13, r=13, t=11, b=11), accent_w=4.5),
        "formula": dict(fill=C["blue-soft"], accent=C["indigo"], bdr=C["blue-bdr"],
                        stroke_w=0.6, radius=5, pad=dict(l=13, r=13, t=11, b=11), accent_w=4.5),
        "answer": dict(fill=C["jade-soft"], accent=C["jade"], bdr=C["jade-bdr"],
                       stroke_w=0.6, radius=5, pad=dict(l=13, r=13, t=10, b=12), accent_w=4.5),
        "passage": dict(fill=HexColor("#FCFBF7"), accent=None, bdr=HexColor("#D6D0C4"),
                        stroke_w=0.8, radius=5, pad=dict(l=16, r=16, t=14, b=14), accent_w=0),
        "essay": dict(fill=HexColor("#FAFBFF"), accent=C["purple"], bdr=C["purple-bdr"],
                      stroke_w=0.6, radius=5, pad=dict(l=16, r=16, t=14, b=14), accent_w=3.5),
        "callout": dict(fill=C["blue-soft"], accent=C["indigo"], bdr=C["blue-bdr"],
                        stroke_w=0.6, radius=5, pad=dict(l=13, r=13, t=11, b=11), accent_w=4.5),
    }[kind]
    base.update(overrides)
    return base


def call_to_kwargs(node):
    """Extract (name, args, kwargs) and convert colorref/size values."""
    name, args, kwargs = node
    return name, args, kwargs


def val_str(v):
    if v.kind == "str":
        return v.data
    if v.kind == "bare":
        return v.data
    if v.kind == "color":
        return v.data
    if v.kind == "colorref":
        return C.get(v.data, C["ink"])
    if v.kind == "size":
        val, unit = v.data
        if unit == "pt":
            return val
        if unit == "mm":
            return val * mm
        if unit == "em":
            return val * 9.8
        if unit == "cm":
            return val * mm * 10
        return val
    if v.kind == "bool":
        return v.data
    return str(v.data)


def parse_pad(v):
    if v.kind == "dict":
        d = dict(v.data)
        return {k: val_str(d.get(k, Val("size", (0, "pt")))) for k in ("l", "r", "t", "b")}
    if v.kind == "size":
        x = val_str(v)
        return dict(l=x, r=x, t=x, b=x)
    return dict(l=0, r=0, t=0, b=0)


def render_block(node, avail_width):
    name, args, kwargs = node

    if name == "part-banner":
        num = val_str(args[0]) if args else ""
        title = val_str(args[1]) if len(args) > 1 else ""
        subtitle = val_str(args[2]) if len(args) > 2 else ""
        return PartBannerFlowable(num, title, subtitle, avail_width)

    if name == "exam-header":
        num = val_str(args[0]) if args else ""
        subtitle = val_str(args[1]) if len(args) > 1 else ""
        model = val_str(args[2]) if len(args) > 2 else ""
        return ExamHeaderFlowable(num, subtitle, model, avail_width)

    if name == "study-table":
        return render_study_table(node, avail_width)

    if name == "grid":
        return render_grid(node, avail_width)

    if name == "pagebreak":
        return PageBreak()

    if name == "v":
        vnode = args[0] if args else Val("size", (6, "pt"))
        sz = val_str(vnode)
        return Spacer(1, max(0, sz))

    if name == "line":
        return HRFlowable(width="100%", thickness=0.5, color=C["border"],
                          spaceBefore=2, spaceAfter=2, hAlign="CENTER")

    if name == "pad":
        vnode = kwargs.get("top", args[0] if args else None)
        children = []
        if vnode:
            children.append(Spacer(1, val_str(vnode)))
        body = kwargs.get("body") or (args[1] if len(args) > 1 else None)
        if body and body.kind == "content":
            children += render_content_items(body.data, avail_width)
        if kwargs.get("bottom"):
            children.append(Spacer(1, val_str(kwargs["bottom"])))
        return children

    if name == "block":
        children = render_content_args(args, avail_width)
        spec = box_spec("callout")
        if kwargs.get("fill"):
            spec["fill"] = co(val_str(kwargs["fill"]))
        if kwargs.get("radius"):
            spec["radius"] = val_str(kwargs["radius"])
        if kwargs.get("inset"):
            spec["pad"] = parse_pad(kwargs["inset"])
        if kwargs.get("stroke"):
            spec["stroke"] = C["border"]
            spec["stroke_w"] = 0.6
        if kwargs.get("breakable") is False:
            pass
        return BoxFlowable(children, spec)

    if name in BOX_CALLS:
        kind = BOX_CALLS[name]
        title_val = kwargs.get("title")
        title = val_str(title_val) if title_val and title_val.kind == "content" else ""
        body = None
        for a in args:
            if a.kind == "content":
                body = a.data
                break
        children = render_content_items(body, avail_width) if body else []
        tone = val_str(kwargs.get("tone", Val("str", "primary")))
        icon = val_str(kwargs.get("icon", Val("str", "◆")))
        breakable = kwargs.get("breakable")
        breakable = True if breakable is None else bool(val_str(breakable) == "true")
        spec = box_spec(kind)
        if kind == "callout":
            spec = dict(spec)
            tones = {
                "gold": (C["gold-soft"], C["amber"], C["gold-bdr"]),
                "danger": (C["red-soft"], C["red"], C["red-bdr"]),
                "success": (C["jade-soft"], C["jade"], C["jade-bdr"]),
            }
            if tone in tones:
                spec["fill"], spec["accent"], spec["bdr"] = tones[tone]
            spec["pad"] = dict(l=13, r=13, t=11, b=11)
            spec["accent_w"] = 4.5
        if kind == "passage":
            source = kwargs.get("source")
            src_text = val_str(source) if source else ""
            return PassageBoxFlowable(title, src_text, children, avail_width, spec)
        if kind == "essay":
            return EssayBoxFlowable(title, children, avail_width, spec)
        return BoxFlowable(children, spec)

    # Unknown block: render as a small note paragraph so nothing is lost.
    return Paragraph(f"<i>[Khối chưa chuyển đổi: {name}]</i>",
                     ParagraphStyle("unk", fontName="DejaVuSans-Oblique",
                                    fontSize=8.5, textColor=C["muted"]))


def render_content_args(args, avail_width):
    children = []
    for a in args:
        if a.kind == "content":
            children += render_content_items(a.data, avail_width)
    return children


def render_content_items(inner_text, avail_width):
    items = scan_items(inner_text)
    flows = []
    for it in items:
        kind = it[0]
        if kind == "para":
            segs = parse_inline(it[1])
            flows += inline_flowables(segs, st_normal, avail_width)
        elif kind == "heading":
            lvl, txt = it[1], it[2]
            flows.append(render_heading(lvl, txt))
        elif kind == "list":
            if it[1] == "bullet":
                segs = parse_inline(it[2])
                flows.append(BulletFlowable(segs, avail_width))
            else:
                _, _, num, txt = it
                segs = parse_inline(txt)
                flows.append(NumberFlowable(num, segs, avail_width))
        elif kind == "block":
            flows.append(render_block(it[1], avail_width))
    return flows


class BulletFlowable(Flowable):
    """A bullet item as a Paragraph with hanging indent; wraps to multiple
    flowables if inline segments contain badges/breaks."""

    def __init__(self, segments, avail_width):
        super().__init__()
        style = ParagraphStyle("bullet", parent=st_normal,
                               leftIndent=14, firstLineIndent=-14,
                               spaceAfter=3, bulletFontName="DejaVuSans-Bold",
                               bulletFontSize=9)
        self.pieces = []
        buf = []
        for seg in segments:
            if seg[0] == "text":
                buf.append(seg)
            else:
                if buf:
                    self.pieces.append(self._para(buf, style))
                    buf = []
                if seg[0] == "break":
                    self.pieces.append(Spacer(1, 2))
                elif seg[0] == "badge":
                    self.pieces.append(BadgeFlowable(seg[1]))
                elif seg[0] == "block":
                    self.pieces.append(render_block(seg[1], avail_width))
        if buf:
            self.pieces.append(self._para(buf, style))

    def _para(self, buf, style):
        parts = []
        for seg in buf:
            _, txt, b, it, opts = seg
            markup = ""
            if b:
                markup += "<b>"
            if it:
                markup += "<i>"
            esc = sanitize(txt).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            markup += esc
            if it:
                markup += "</i>"
            if b:
                markup += "</b>"
        parts.append("".join(parts))
        return Paragraph("".join(parts), style, bulletText="•")

    def wrap(self, avail_width, avail_height):
        total = 0
        for p in self.pieces:
            p.wrap(avail_width, avail_height - total)
            total += p.height
        self.width = avail_width
        self.height = total
        return (avail_width, total)

    def draw(self):
        canv = self.canv
        y = self.height
        for p in self.pieces:
            p.drawOn(canv, 0, y - p.height)
            y -= p.height


class NumberFlowable(Flowable):
    def __init__(self, num, segments, avail_width):
        super().__init__()
        style = ParagraphStyle("num", parent=st_normal,
                               leftIndent=16, firstLineIndent=-16,
                               spaceAfter=3)
        self.num = num
        self.pieces = []
        buf = []
        for seg in segments:
            if seg[0] == "text":
                buf.append(seg)
            else:
                if buf:
                    self.pieces.append(self._para(buf, style))
                    buf = []
                if seg[0] == "break":
                    self.pieces.append(Spacer(1, 2))
                elif seg[0] == "badge":
                    self.pieces.append(BadgeFlowable(seg[1]))
                elif seg[0] == "block":
                    self.pieces.append(render_block(seg[1], avail_width))
        if buf:
            self.pieces.append(self._para(buf, style))

    def _para(self, buf, style):
        parts = []
        for seg in buf:
            _, txt, b, it, opts = seg
            markup = ""
            if b:
                markup += "<b>"
            if it:
                markup += "<i>"
            esc = sanitize(txt).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            markup += esc
            if it:
                markup += "</i>"
            if b:
                markup += "</b>"
        return Paragraph(f"{self.num}.&nbsp;&nbsp;" + "".join(parts), style)

    def wrap(self, avail_width, avail_height):
        total = 0
        for p in self.pieces:
            p.wrap(avail_width, avail_height - total)
            total += p.height
        self.width = avail_width
        self.height = total
        return (avail_width, total)

    def draw(self):
        canv = self.canv
        y = self.height
        for p in self.pieces:
            p.drawOn(canv, 0, y - p.height)
            y -= p.height


def render_heading(level, text):
    if level == 1:
        style = ParagraphStyle("h1", fontName="DejaVuSans-Bold", fontSize=12.5,
                               leading=15, textColor=C["navy"], spaceBefore=13,
                               spaceAfter=5, alignment=TA_LEFT)
        p = Paragraph(sanitize(text), style)
        p._toc = (1, text)
        return p
    if level == 2:
        style = ParagraphStyle("h2", fontName="DejaVuSans-Bold", fontSize=12,
                               leading=14.5, textColor=C["navy"], spaceBefore=11,
                               spaceAfter=3, alignment=TA_LEFT)
        p = Paragraph(sanitize(text), style)
        p._toc = (2, text)
        rule = HRFlowable(width="100%", thickness=1.2, color=C["indigo"],
                          spaceBefore=1, spaceAfter=7, hAlign="LEFT")
        return KeepTogether([p, rule])
    if level == 3:
        style = ParagraphStyle("h3", fontName="DejaVuSans-Bold", fontSize=10.6,
                               leading=13, textColor=C["indigo"], spaceBefore=7,
                               spaceAfter=3, alignment=TA_LEFT, leftIndent=6)
        return Paragraph("▸ " + sanitize(text), style)
    # level 4
    style = ParagraphStyle("h4", fontName="DejaVuSans-Bold", fontSize=9.9,
                           leading=12, textColor=C["amber"], spaceBefore=5,
                           spaceAfter=2, alignment=TA_LEFT, leftIndent=6)
    return Paragraph("• " + sanitize(text), style)


# -----------------------------------------------------------------------------
# Tables
# -----------------------------------------------------------------------------
def cell_style_for(align_horiz, is_header=False):
    base = ParagraphStyle(
        "cell",
        fontName="DejaVuSans-Bold" if is_header else "DejaVuSans",
        fontSize=8.6 if is_header else 8.9,
        leading=11.6 if is_header else 11.8,
        textColor=white if is_header else C["ink"],
        alignment=TA_CENTER if is_header else TA_LEFT,
        spaceAfter=0,
    )
    return base


def render_table_cell(value, ncols, col_index, avail_width, header=False):
    """value: Val content. Returns (flowables, colspan)."""
    colspan = 1
    if value.kind == "dict":
        pairs = dict(value.data)
        colspan = int(val_str(pairs.get("colspan", Val("size", (1, "pt")))) or 1)
        cell_val = pairs.get("_content")
        # content is passed as the unnamed 'content' arg; handle below via kwargs['content']
        return cell_val, colspan
    return value, colspan


def render_study_table(node, avail_width):
    name, args, kwargs = node
    cols_arg = args[0] if args else Val("array", [])
    headers_arg = args[1] if len(args) > 1 else Val("array", [])
    cell_vals = args[2:]

    col_specs = [c for c in cols_arg.data]

    headers = [val_str(a) if a.kind in ("str", "bare") else str(a.data)
               for a in headers_arg.data]
    ncols = len(headers)

    # Convert fr widths to points (fixed sizes fall back to equal share).
    fr_vals = [float(s.data[0]) for s in col_specs
               if s.kind == "size" and s.data[1] == "fr"]
    if fr_vals:
        total_fr = sum(fr_vals)
        frac_w = (avail_width - 6) / total_fr
        col_widths = [
            (float(s.data[0]) * frac_w if (s.kind == "size" and s.data[1] == "fr") else frac_w)
            for s in col_specs
        ]
    else:
        col_widths = [avail_width / max(ncols, 1)] * ncols

    data = []
    # Header row
    data.append([Paragraph(h, cell_style_for("center", is_header=True)) for h in headers])

    def unpack_cell(val):
        """Return (inner_text, colspan, halign) from one study-table cell Val."""
        if val.kind == "array":
            inner = val.data[0] if val.data else Val("str", "")
            return val_str(inner), 1, "left"
        s = val_str(val)
        m = re.match(r"\s*align\((left|center|right|justify)\)\[(.*)\]\s*$", s, re.S)
        if m:
            return m.group(2), 1, m.group(1)
        m = re.match(r"\s*table\.cell\(([^)]*)\)\[(.*)\]\s*$", s, re.S)
        if m:
            kwargs = {}
            for pair in split_args(m.group(1)):
                if ":" in pair:
                    k, _, v = pair.partition(":")
                    kwargs[k.strip()] = classify_arg(v.strip())
            colspan = int(val_str(kwargs.get("colspan", Val("size", (1, "pt")))) or 1)
            halign = val_str(kwargs.get("align", Val("bare", "left"))) or "left"
            return m.group(2), colspan, halign
        return s, 1, "left"

    ci = 0
    row_spans = []
    while ci < len(cell_vals):
        row_cells = []
        col = 0
        row_spans.append([])
        while col < ncols and ci < len(cell_vals):
            val = cell_vals[ci]
            ci += 1
            inner, colspan, halign = unpack_cell(val)
            row_cells.append((inner, colspan, halign))
            if colspan > 1:
                row_spans[-1].append((col, col + colspan - 1))
            col += colspan
        while col < ncols:
            row_cells.append(("", 1, "left"))
            col += 1
        data.append(row_cells)

    # Build flowables per cell and apply spans.
    flow_rows = []
    span_cmds = []
    flow_rows.append([Paragraph(h, cell_style_for("center", is_header=True)) for h in headers])
    for ridx, row in enumerate(data[1:], start=1):
        flow_row = []
        col = 0
        for cell in row:
            if isinstance(cell, str):
                flow_row.append(Paragraph(cell, cell_style_for("left")))
                col += 1
                continue
            inner, colspan, halign = cell
            segs = parse_inline(inner)
            cell_sty = ParagraphStyle(
                "cellx",
                fontName="DejaVuSans",
                fontSize=8.9,
                leading=11.8,
                textColor=C["ink"],
                alignment=TA_CENTER if halign == "center" else TA_LEFT,
                spaceAfter=1,
            )
            pieces = inline_flowables(segs, cell_sty, col_widths[col] - 13)
            flow_row.append(pieces)
            for (c0, c1) in row_spans[ridx - 1]:
                if c0 == col:
                    span_cmds.append(("SPAN", (col, ridx), (c1, ridx)))
                    col = c1 + 1
                    break
            else:
                col += 1 if colspan == 1 else colspan
        flow_rows.append(flow_row)

    table = Table(flow_rows, colWidths=col_widths, repeatRows=1,
                  hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), C["navy"]),
        ("GRID", (0, 0), (-1, -1), 0.5, C["border"]),
        ("BOX", (0, 0), (-1, -1), 0.5, C["border"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6.5),
        ("TOPPADDING", (0, 0), (-1, -1), 5.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
    ]
    for ridx in range(1, len(data)):
        if ridx % 2 == 0:
            style.append(("BACKGROUND", (0, ridx), (-1, ridx), C["bg-neutral"]))
    for cmd in span_cmds:
        style.append(cmd)
    table.setStyle(TableStyle(style))
    return table


def render_grid(node, avail_width):
    name, args, kwargs = node
    cols_spec = None
    gutter = 0
    blocks = []
    for a in args:
        if a.kind == "dict":
            pairs = dict(a.data)
            cols_spec = pairs.get("columns")
            gutter = val_str(pairs.get("column-gutter", Val("size", (0, "pt"))))
            continue
        if a.kind == "content":
            blocks += scan_items(a.data)
    # Column widths
    if cols_spec and cols_spec.kind == "array":
        specs = cols_spec.data
    else:
        specs = [Val("size", (1, "fr"))] * max(1, len(blocks))
    total_fr = sum((s.data[0] if s.kind == "size" and s.data[1] == "fr"
                    else 1) for s in specs)
    n = len(specs)
    usable = avail_width - gutter * (n - 1)
    widths = []
    for s in specs:
        if s.kind == "size" and s.data[1] == "fr":
            widths.append(s.data[0] / total_fr * usable)
        elif s.kind == "bare" and s.data == "auto":
            widths.append(40)
        else:
            widths.append(usable / n)
    # Build one-row table: each cell holds block flowables.
    cell_flows = []
    bi = 0
    for w in widths:
        cell_blocks = []
        # Consume one top-level block item per cell (grid items are blocks).
        if bi < len(blocks):
            it = blocks[bi]
            bi += 1
            if it[0] == "block":
                cell_blocks = [render_block(it[1], w - 4)]
            elif it[0] == "para":
                segs = parse_inline(it[1])
                cell_blocks = inline_flowables(segs, st_normal, w - 4)
            else:
                cell_blocks = [render_heading(it[1], it[2])]
        cell_flows.append(cell_blocks)
    table = Table([cell_flows], colWidths=widths, hAlign="LEFT")
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]
    if gutter > 0:
        # add empty spacer columns to simulate gutters
        new_widths = []
        new_cells = []
        for idx, w in enumerate(widths):
            if idx:
                new_widths.append(gutter)
                new_cells.append([])
            new_widths.append(w)
            new_cells.append(cell_flows[idx])
        widths = new_widths
        cell_flows = new_cells
        table = Table([cell_flows], colWidths=widths, hAlign="LEFT")
    table.setStyle(TableStyle(style))
    return table


# -----------------------------------------------------------------------------
# Boxes with titles
# -----------------------------------------------------------------------------
class PassgeBoxFlowable(BoxFlowable):  # placeholder name kept for clarity
    pass


class PassageBoxFlowable(Flowable):
    def __init__(self, title, source, children, avail_width, spec):
        super().__init__()
        self.title = title
        self.source = source
        self.children = children
        self.avail_width = avail_width
        self.spec = spec
        self.width = 0
        self.height = 0

    def wrap(self, avail_width, avail_height):
        pad = self.spec["pad"]
        self.max_w = avail_width - pad["l"] - pad["r"]
        title_style = ParagraphStyle("ptitle", fontName="DejaVuSerif-Bold",
                                     fontSize=11, leading=13,
                                     textColor=C["navy"], alignment=TA_CENTER)
        source_style = ParagraphStyle("psource", fontName="DejaVuSerif-Oblique",
                                      fontSize=8.8, leading=11,
                                      textColor=C["slate"], alignment=TA_RIGHT)
        h = pad["t"]
        if self.title:
            t = Paragraph(self.title.upper(), title_style)
            t.wrap(self.max_w, avail_height)
            h += 4 + t.height
        total = h + pad["b"]
        for ch in self.children:
            ch.wrap(self.max_w, avail_height - total)
            total += ch.height
        if self.source:
            s = Paragraph(f"({self.source})", source_style)
            s.wrap(self.max_w, avail_height - total)
            total += 4 + s.height
        self.width = avail_width
        self.height = total
        return (avail_width, total)

    def split(self, avail_width, avail_height):
        limit = avail_height - self.spec["pad"]["t"] - self.spec["pad"]["b"]
        if hasattr(limit, "__float__"):
            pass
        pieces = []
        group = []
        group_h = self.spec["pad"]["t"]
        if self.title:
            group.append(("title",))
            group_h += 4
        # title + body children
        body_children = list(self.children)
        src = ("source", self.source)
        queue = [("title", self.title)] + [("child", ch) for ch in body_children] + [src]
        cur = []
        cur_h = self.spec["pad"]["t"]
        for item in queue:
            if item[0] == "title":
                tstyle = ParagraphStyle("pt", fontName="DejaVuSerif-Bold", fontSize=11,
                                        leading=13, textColor=C["navy"],
                                        alignment=TA_CENTER)
                t = Paragraph(item[1].upper(), tstyle)
                t.wrap(self.max_w, avail_height)
                hh = 4 + t.height
            elif item[0] == "source":
                sstyle = ParagraphStyle("ps", fontName="DejaVuSerif-Oblique", fontSize=8.8,
                                        leading=11, textColor=C["slate"],
                                        alignment=TA_RIGHT)
                s = Paragraph(f"({item[1]})", sstyle)
                s.wrap(self.max_w, avail_height)
                hh = 4 + s.height
            else:
                ch = item[1]
                ch.wrap(self.max_w, avail_height)
                hh = ch.height
            if cur and cur_h + hh > limit:
                pieces.append(PassagePiece(cur, self.spec, self.max_w))
                cur = [item]
                cur_h = hh
            else:
                cur.append(item)
                cur_h += hh
        if cur:
            pieces.append(PassagePiece(cur, self.spec, self.max_w))
        if not pieces:
            self.wrap(self.max_w, avail_height)
            return [] if self.height > avail_height else [self]
        pieces[0].wrap(self.max_w, avail_height)
        if pieces[0].height > avail_height:
            return []
        return pieces

    def draw(self):
        canv = self.canv
        s = self.spec
        w, h = self.width, self.height
        pad = s["pad"]
        canv.setFillColor(s["fill"])
        canv.setStrokeColor(s["bdr"])
        canv.setLineWidth(s["stroke_w"])
        canv.roundRect(0, 0, w, h, s["radius"], stroke=1, fill=1)
        cy = h - pad["t"]
        cx = pad["l"]
        if self.title:
            tstyle = ParagraphStyle("ptd", fontName="DejaVuSerif-Bold", fontSize=11,
                                    leading=13, textColor=C["navy"], alignment=TA_CENTER)
            t = Paragraph(self.title.upper(), tstyle)
            t.wrap(self.max_w, cy)
            t.drawOn(canv, cx, cy - t.height)
            cy -= t.height + 4
        for ch in self.children:
            ch.drawOn(canv, cx, cy - ch.height)
            cy -= ch.height
        if self.source:
            sstyle = ParagraphStyle("psd", fontName="DejaVuSerif-Oblique", fontSize=8.8,
                                    leading=11, textColor=C["slate"], alignment=TA_RIGHT)
            s = Paragraph(f"({self.source})", sstyle)
            s.wrap(self.max_w, cy - 4)
            s.drawOn(canv, cx, cy - 4 - s.height)


class PassagePiece(Flowable):
    def __init__(self, queue, spec, max_w):
        super().__init__()
        self.queue = queue
        self.spec = spec
        self.max_w = max_w
        self.width = 0
        self.height = 0

    def wrap(self, avail_width, avail_height):
        pad = self.spec["pad"]
        h = pad["t"]
        rendered = []
        for item in self.queue:
            if item[0] == "title":
                tstyle = ParagraphStyle("ptx", fontName="DejaVuSerif-Bold", fontSize=11,
                                        leading=13, textColor=C["navy"], alignment=TA_CENTER)
                t = Paragraph(item[1].upper(), tstyle)
                t.wrap(self.max_w, avail_height)
                rendered.append(("title", t, 4 + t.height))
                h += 4 + t.height
            elif item[0] == "source":
                sstyle = ParagraphStyle("psx", fontName="DejaVuSerif-Oblique", fontSize=8.8,
                                        leading=11, textColor=C["slate"], alignment=TA_RIGHT)
                s = Paragraph(f"({item[1]})", sstyle)
                s.wrap(self.max_w, avail_height)
                rendered.append(("source", s, 4 + s.height))
                h += 4 + s.height
            else:
                ch = item[1]
                ch.wrap(self.max_w, avail_height)
                rendered.append(("child", ch, ch.height))
                h += ch.height
        h += pad["b"]
        self.rendered = rendered
        self.width = pad["l"] + self.max_w + pad["r"]
        self.height = h
        return (self.width, h)

    def draw(self):
        canv = self.canv
        s = self.spec
        pad = s["pad"]
        w, h = self.width, self.height
        canv.setFillColor(s["fill"])
        canv.setStrokeColor(s["bdr"])
        canv.setLineWidth(s["stroke_w"])
        canv.roundRect(0, 0, w, h, s["radius"], stroke=1, fill=1)
        cx = pad["l"]
        cy = h - pad["t"]
        for kind, obj, hh in self.rendered:
            if kind == "title":
                obj.drawOn(canv, cx, cy - obj.height)
                cy -= obj.height + 4
            elif kind == "source":
                obj.drawOn(canv, cx, cy - 4 - obj.height)
                cy -= obj.height + 4
            else:
                obj.drawOn(canv, cx, cy - obj.height)
                cy -= obj.height


class EssayBoxFlowable(Flowable):
    def __init__(self, title, children, avail_width, spec):
        super().__init__()
        self.title = title
        self.children = children
        self.avail_width = avail_width
        self.spec = spec
        self.width = 0
        self.height = 0

    def wrap(self, avail_width, avail_height):
        pad = self.spec["pad"]
        self.max_w = avail_width - pad["l"] - pad["r"]
        h = pad["t"]
        title_style = ParagraphStyle("etitle", fontName="DejaVuSans-Bold",
                                     fontSize=8.6, leading=10.5,
                                     textColor=C["purple"], alignment=TA_LEFT)
        t = Paragraph("✦ " + self.title.upper(), title_style)
        t.wrap(self.max_w, avail_height)
        h += 5 + t.height
        total = h + pad["b"]
        for ch in self.children:
            ch.wrap(self.max_w, avail_height - total)
            total += ch.height
        self.width = avail_width
        self.height = total
        return (avail_width, total)

    def split(self, avail_width, avail_height):
        limit = avail_height - self.spec["pad"]["t"] - self.spec["pad"]["b"]
        pieces = []
        cur = []
        cur_h = self.spec["pad"]["t"]
        title_style = ParagraphStyle("etx", fontName="DejaVuSans-Bold", fontSize=8.6,
                                     leading=10.5, textColor=C["purple"], alignment=TA_LEFT)
        t = Paragraph("✦ " + self.title.upper(), title_style)
        t.wrap(self.max_w, avail_height)
        th = 5 + t.height
        queue = [("title", t, th)] + [("child", ch, None) for ch in self.children]
        for item in queue:
            if item[0] == "title":
                _, obj, hh = item
            else:
                ch = item[1]
                ch.wrap(self.max_w, avail_height)
                hh = ch.height
            if cur and cur_h + hh > limit:
                pieces.append(EssayPiece(cur, self.spec, self.max_w))
                cur = [item]
                cur_h = hh
            else:
                cur.append(item)
                cur_h += hh
        if cur:
            pieces.append(EssayPiece(cur, self.spec, self.max_w))
        if not pieces:
            self.wrap(self.max_w, avail_height)
            return [] if self.height > avail_height else [self]
        pieces[0].wrap(self.max_w, avail_height)
        if pieces[0].height > avail_height:
            return []
        return pieces

    def draw(self):
        canv = self.canv
        s = self.spec
        pad = s["pad"]
        w, h = self.width, self.height
        canv.setFillColor(s["fill"])
        canv.setStrokeColor(s["bdr"])
        canv.setLineWidth(s["stroke_w"])
        canv.roundRect(0, 0, w, h, s["radius"], stroke=1, fill=1)
        if s["accent"]:
            canv.setFillColor(s["accent"])
            canv.rect(0, 0, s["accent_w"], h, stroke=0, fill=1)
        cx = pad["l"] + (s["accent_w"] if s["accent"] else 0)
        cy = h - pad["t"]
        title_style = ParagraphStyle("etd", fontName="DejaVuSans-Bold", fontSize=8.6,
                                     leading=10.5, textColor=C["purple"], alignment=TA_LEFT)
        t = Paragraph("✦ " + self.title.upper(), title_style)
        t.wrap(self.max_w, cy)
        t.drawOn(canv, cx, cy - t.height)
        cy -= t.height + 5
        for ch in self.children:
            ch.drawOn(canv, cx, cy - ch.height)
            cy -= ch.height


class EssayPiece(Flowable):
    def __init__(self, queue, spec, max_w):
        super().__init__()
        self.queue = queue
        self.spec = spec
        self.max_w = max_w
        self.width = 0
        self.height = 0

    def wrap(self, avail_width, avail_height):
        pad = self.spec["pad"]
        h = pad["t"]
        rendered = []
        title_style = ParagraphStyle("etpx", fontName="DejaVuSans-Bold", fontSize=8.6,
                                     leading=10.5, textColor=C["purple"], alignment=TA_LEFT)
        for item in self.queue:
            if item[0] == "title":
                obj = item[1]
                hh = item[2]
                rendered.append(("title", obj, hh))
                h += hh
            else:
                ch = item[1]
                ch.wrap(self.max_w, avail_height)
                rendered.append(("child", ch, ch.height))
                h += ch.height
        h += pad["b"]
        self.rendered = rendered
        self.width = pad["l"] + self.max_w + pad["r"]
        self.height = h
        return (self.width, h)

    def draw(self):
        canv = self.canv
        s = self.spec
        pad = s["pad"]
        w, h = self.width, self.height
        canv.setFillColor(s["fill"])
        canv.setStrokeColor(s["bdr"])
        canv.setLineWidth(s["stroke_w"])
        canv.roundRect(0, 0, w, h, s["radius"], stroke=1, fill=1)
        if s["accent"]:
            canv.setFillColor(s["accent"])
            canv.rect(0, 0, s["accent_w"], h, stroke=0, fill=1)
        cx = pad["l"] + (s["accent_w"] if s["accent"] else 0)
        cy = h - pad["t"]
        for kind, obj, hh in self.rendered:
            if kind == "title":
                obj.drawOn(canv, cx, cy - obj.height)
                cy -= obj.height + 5
            else:
                obj.drawOn(canv, cx, cy - obj.height)
                cy -= obj.height


# -----------------------------------------------------------------------------
# Part banner & exam header
# -----------------------------------------------------------------------------
class PartBannerFlowable(Flowable):
    def __init__(self, num, title, subtitle, avail_width):
        super().__init__()
        self.num = num
        self.title = title
        self.subtitle = subtitle
        self.avail_width = avail_width
        self.width = 0
        self.height = 0
        self._toc = (0, f"{num} — {title}")

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        pad_top, pad_bot, pad_side = 14, 14, 16
        title_style = ParagraphStyle("pbtitle", fontName="DejaVuSans-Bold",
                                     fontSize=13.5, leading=16, textColor=white)
        sub_style = ParagraphStyle("pbsub", fontName="DejaVuSans", fontSize=8.8,
                                   leading=11, textColor=HexColor("#D0E2FF"))
        chip_style = ParagraphStyle("pbc", fontName="DejaVuSans-Bold", fontSize=9.5,
                                    leading=12, textColor=C["navy"])
        t = Paragraph(self.title.upper(), title_style)
        t.wrap(avail_width - pad_side * 2 - 60, avail_height)
        s = Paragraph(self.subtitle, sub_style)
        s.wrap(avail_width - pad_side * 2 - 60, avail_height)
        cw = pdfmetrics.stringWidth(self.num, chip_style.fontName, chip_style.fontSize) + 18
        self.height = pad_top + max(t.height + 3 + s.height, 12 + 9.5 + 12) + pad_bot
        self._chip_w = cw
        self._title_h = t.height
        self._sub_h = s.height
        self._t_flow = t
        self._s_flow = s
        self._chip_style = chip_style
        return (avail_width, self.height)

    def draw(self):
        canv = self.canv
        w, h = self.width, self.height
        canv.setFillColor(C["navy"])
        canv.roundRect(0, 0, w, h, 6, stroke=0, fill=1)
        pad_side = 16
        pad_top = 14
        # Gold chip (number)
        chip_x = pad_side
        chip_y = h - pad_top - 21.5
        canv.setFillColor(C["cover-gold"])
        canv.roundRect(chip_x, chip_y, self._chip_w, 21.5, 4, stroke=0, fill=1)
        canv.setFillColor(C["navy"])
        canv.setFont("DejaVuSans-Bold", 9.5)
        canv.drawString(chip_x + 9, chip_y + 7, self.num)
        # Title + subtitle (right of chip)
        cx = chip_x + self._chip_w + 12
        cw_avail = w - pad_side - self._chip_w - 24
        self._t_flow.wrap(cw_avail, h)
        self._t_flow.drawOn(canv, cx, h - pad_top - self._t_flow.height)
        cy = h - pad_top - self._t_flow.height - 3
        self._s_flow.wrap(cw_avail, h)
        self._s_flow.drawOn(canv, cx, cy - self._s_flow.height)


class ExamHeaderFlowable(Flowable):
    def __init__(self, num, subtitle, model, avail_width):
        super().__init__()
        self.num = num
        self.subtitle = subtitle
        self.model = model
        self.avail_width = avail_width
        self.width = 0
        self.height = 0

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        pad = 11
        inner_w = avail_width - 2 * pad
        line1 = ParagraphStyle("eh1", fontName="DejaVuSans-Bold", fontSize=8.2,
                               leading=10.5, textColor=C["indigo"])
        line2 = ParagraphStyle("eh2", fontName="DejaVuSans-Bold", fontSize=13,
                               leading=15, textColor=C["navy"])
        p1 = Paragraph("ĐỀ KIỂM TRA GIỮA HỌC KÌ I — MÔN NGỮ VĂN 10 (NĂM HỌC 2026 – 2027)", line1)
        p2 = Paragraph(f"ĐỀ MINH HỌA SỐ {self.num}: " + self.subtitle.upper(), line2)
        p1.wrap(inner_w - 120, avail_height)
        p2.wrap(inner_w - 120, avail_height)
        self.height = 22 + p1.height + 3 + p2.height + 40
        self._p1, self._p2 = p1, p2
        self._p1w, self._p2w = p1.width, p2.width
        return (avail_width, self.height)

    def draw(self):
        canv = self.canv
        w, h = self.width, self.height
        pad = 11
        canv.setFillColor(HexColor("#F0F5FF"))
        canv.setStrokeColor(C["indigo"])
        canv.setLineWidth(1.2)
        canv.roundRect(0, 0, w, h, 6, stroke=1, fill=1)
        cx = pad
        cy = h - pad
        self._p1.drawOn(canv, cx, cy - self._p1.height)
        cy -= self._p1.height + 3
        self._p2.drawOn(canv, cx, cy - self._p2.height)
        cy -= self._p2.height + 5
        # Right chip: time + exam variant, wrapped to fit
        chip_w = 105
        chip_x = w - pad - chip_w
        canv.setFillColor(C["navy"])
        canv.roundRect(chip_x, cy - 34, chip_w, 34, 4, stroke=0, fill=1)
        canv.setFillColor(C["cover-gold"])
        canv.setFont("DejaVuSans-Bold", 7)
        canv.drawString(chip_x + 6, cy - 9, "THỜI GIAN:")
        canv.drawString(chip_x + 6, cy - 18, "90 PHÚT")
        canv.setFillColor(white)
        canv.setFont("DejaVuSans", 6.8)
        words = self.model.split()
        lines, cur = [], ""
        for wd in words:
            t = (cur + " " + wd).strip()
            if pdfmetrics.stringWidth(t, "DejaVuSans", 6.8) <= chip_w - 12:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = wd
        if cur:
            lines.append(cur)
        for k, ln in enumerate(lines[:2]):
            canv.drawString(chip_x + 6, cy - 28 - k * 8.5, ln)


# -----------------------------------------------------------------------------
# Styles
# -----------------------------------------------------------------------------
st_normal = ParagraphStyle(
    "normal", fontName="DejaVuSans", fontSize=9.8, leading=15.2,
    textColor=C["ink"], alignment=TA_JUSTIFY, spaceAfter=7,
)


# -----------------------------------------------------------------------------
# Replacement inline renderer (cleaner markup handling)
# -----------------------------------------------------------------------------
def seg_markup(seg):
    """Render one 5-tuple inline segment into ReportLab inline markup."""
    _, txt, b, it, opts = seg
    open_tags = []
    attrs = []
    if opts:
        fs = opts.get("size")
        fc = opts.get("fill")
        fw = opts.get("weight")
        ff = opts.get("font")
        if fs:
            attrs.append(f'size="{fs}"')
        if fc:
            c = co(fc)
            hexstr = c.hexval() if hasattr(c, "hexval") else str(c)
            attrs.append(f'color="{hexstr}"')
        if fw == "bold":
            open_tags.append("b")
        if it:
            open_tags.append("i")
        if ff == "serif":
            open_tags.append('font name="DejaVuSerif"')
    else:
        if b:
            open_tags.append("b")
        if it:
            open_tags.append("i")
    out = ""
    for tg in open_tags:
        tag = tg.split()[0] if " " in tg else tg
        out += f"<{tag}>"
    if attrs:
        out += f'<font {" ".join(attrs)}>'
    esc = sanitize(txt).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    out += esc
    if attrs:
        out += "</font>"
    for tg in reversed(open_tags):
        tag = tg.split()[0] if " " in tg else tg
        out += f"</{tag}>"
    return out


def inline_flowables(segments, style, avail_width):
    """Convert inline segments into a list of flowables, splitting at breaks,
    badges, inline calls (#strong, #upper, #text, #badge-*) and block calls."""
    flows = []
    buf = []

    def flush_text():
        if not buf:
            return
        p = Paragraph("".join(seg_markup(s) for s in buf), style)
        flows.append(p)
        buf.clear()

    for seg in segments:
        kind = seg[0]
        if kind == "text":
            buf.append(seg)
        elif kind == "break":
            flush_text()
            flows.append(Spacer(1, 2))
        elif kind == "badge":
            flush_text()
            flows.append(BadgeFlowable(seg[1]))
        elif kind == "call":
            flush_text()
            cname = seg[1][0]
            args = seg[1][1]
            kwargs = seg[1][2] or {}
            inner = val_str(args[0]) if args else ""
            if cname == "strong":
                markup = "".join(seg_markup(s) for s in parse_inline(inner))
                flows.append(Paragraph(f"<b>{markup}</b>", style))
            elif cname == "upper":
                flows.append(Paragraph(inner.upper(), style))
            elif cname == "text":
                attrs = []
                if "size" in kwargs:
                    attrs.append(f'size="{val_str(kwargs["size"])}"')
                if "fill" in kwargs:
                    fc = val_str(kwargs["fill"])
                    c = co(fc)
                    attrs.append(f'color="{c.hexval() if hasattr(c, "hexval") else str(c)}"')
                if kwargs.get("weight") == "bold":
                    flows.append(Paragraph(f"<b>{sanitize(inner)}</b>", style))
                elif attrs:
                    flows.append(Paragraph(
                        f'<font {" ".join(attrs)}>{sanitize(inner)}</font>', style))
                else:
                    flows.append(Paragraph(sanitize(inner), style))
            elif cname in ("badge-biet", "badge-hieu", "badge-vd"):
                flows.append(BadgeFlowable(cname[len("badge-"):]))
            else:
                flows.append(Paragraph(sanitize(inner), style))
        elif kind == "block":
            flush_text()
            flows.append(render_block(seg[1], avail_width))
    flush_text()
    return flows


class NumberedCanvas(canvas_module.Canvas):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            if self._pageNumber > 1:  # skip the cover page
                self.setFont("DejaVuSans-Bold", 7.8)
                self.setFillColor(C["navy"])
                self.drawRightString(
                    PAGE_W - 17 * mm, 12.5 * mm,
                    f"Trang {self._pageNumber} / {total}")
            canvas_module.Canvas.showPage(self)
        canvas_module.Canvas.save(self)


# -----------------------------------------------------------------------------
# Document template with TOC notifications and page decorations
# -----------------------------------------------------------------------------
class DeCuongDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        toc = getattr(flowable, "_toc", None)
        if toc is None and isinstance(flowable, KeepTogether):
            inner = getattr(flowable, "flowables", None)
            if inner:
                toc = getattr(inner[0], "_toc", None)
        if toc:
            level, text = toc
            self.notify("TOCEntry", (level, text, self.page))


def cover_decorations(canv, doc):
    canv.saveState()
    W, H = PAGE_W, PAGE_H
    canv.setFillColor(C["navy"])
    canv.rect(0, 0, W, H, stroke=0, fill=1)
    # Gold stripe at top
    canv.setFillColor(HexColor("#F59E0B"))
    canv.rect(0, H - 8 * mm, W, 8 * mm, stroke=0, fill=1)
    # Decorative circles
    canv.setFillColor(C["cover-circle1"])
    canv.setStrokeColor(C["cover-circle1-stroke"])
    canv.setLineWidth(0.8)
    canv.circle(W - 54 * mm, H - 60 * mm, 42 * mm, stroke=1, fill=1)
    canv.setFillColor(C["cover-circle2"])
    canv.setStrokeColor(C["cover-circle2-stroke"])
    canv.circle(37 * mm, 73 * mm, 55 * mm, stroke=1, fill=1)
    canv.restoreState()


def body_decorations(canv, doc):
    canv.saveState()
    W, H = PAGE_W, PAGE_H
    # Header (every body page)
    canv.setFont("DejaVuSans", 7.8)
    canv.setFillColor(C["muted"])
    canv.drawString(17 * mm, H - 13.5 * mm,
                    "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I NGỮ VĂN 10 • KẾT NỐI TRI THỨC")
    canv.setFont("DejaVuSans-Oblique", 7.8)
    canv.drawRightString(W - 17 * mm, H - 13.5 * mm, "NĂM HỌC 2026 – 2027")
    canv.setStrokeColor(C["border"])
    canv.setLineWidth(0.5)
    canv.line(17 * mm, H - 16.5 * mm, W - 17 * mm, H - 16.5 * mm)
    # Footer
    canv.setStrokeColor(C["border"])
    canv.setLineWidth(0.5)
    canv.line(17 * mm, 16.5 * mm, W - 17 * mm, 16.5 * mm)
    canv.setFont("DejaVuSans", 7.8)
    canv.setFillColor(C["muted"])
    canv.drawString(17 * mm, 13 * mm,
                    "Bám sát 100% Ma trận & Bản đặc tả Kiểm tra Giữa kì I (90 phút • 11 câu • Thang điểm 10)")
    canv.restoreState()


# -----------------------------------------------------------------------------
# Story assembly
# -----------------------------------------------------------------------------
def build_story():
    story = []

    # ---------------- Cover page ----------------
    mm_ = mm
    story.append(Spacer(1, 26 * mm_))
    # Program band
    prog = Table(
        [[Paragraph(
            'CHƯƠNG TRÌNH GDPT 2018 • BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG',
            ParagraphStyle("prog", fontName="DejaVuSans-Bold", fontSize=8.8,
                           leading=11, textColor=HexColor("#FCD34D"),
                           alignment=TA_CENTER))]],
        colWidths=[PAGE_W - 2 * 17 * mm_])
    prog.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#1E3A6D")),
        ("BOX", (0, 0), (-1, -1), 0.8, HexColor("#F59E0B")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(prog)
    story.append(Spacer(1, 14 * mm_))
    story.append(Paragraph(
        "TÀI LIỆU ÔN TẬP CHUYÊN SÂU & TỐI ƯU GHI NHỚ NHẬN THỨC",
        ParagraphStyle("cover-sub", fontName="DejaVuSans", fontSize=12,
                       leading=15, textColor=HexColor("#93C5FD"),
                       alignment=TA_CENTER, spaceAfter=0)))
    story.append(Spacer(1, 5 * mm_))
    story.append(Paragraph(
        "ĐỀ CƯƠNG ÔN TẬP<br/>GIỮA HỌC KÌ I — NGỮ VĂN 10",
        ParagraphStyle("cover-title", fontName="DejaVuSans-Bold", fontSize=25,
                       leading=31, textColor=white, alignment=TA_CENTER)))
    story.append(Spacer(1, 4 * mm_))
    story.append(HRFlowable(width=75 * mm_, thickness=2.5,
                            color=HexColor("#F59E0B"), hAlign="CENTER",
                            spaceBefore=2, spaceAfter=2))
    story.append(Spacer(1, 5 * mm_))
    story.append(Paragraph(
        "Phân tích chuyên sâu Ma trận & Bản đặc tả năm học 2026 – 2027:<br/>"
        "Đọc hiểu Truyện Thần thoại ngoài SGK & Nghị luận phân tích, đánh giá tác phẩm truyện",
        ParagraphStyle("cover-desc", fontName="DejaVuSerif-Oblique", fontSize=12,
                       leading=16, textColor=HexColor("#E2E8F0"),
                       alignment=TA_CENTER)))
    story.append(Spacer(1, 12 * mm_))

    # Matrix stat grid (4 boxes)
    def stat_box(pct, label, detail):
        return BoxFlowable([
            Paragraph(pct, ParagraphStyle("sb_pct", fontName="DejaVuSans-Bold",
                                          fontSize=15, leading=18,
                                          textColor=C["indigo"], alignment=TA_CENTER)),
            Paragraph(label, ParagraphStyle("sb_lbl", fontName="DejaVuSans-Bold",
                                            fontSize=8, leading=10,
                                            textColor=C["navy"], alignment=TA_CENTER)),
            Paragraph(detail, ParagraphStyle("sb_det", fontName="DejaVuSans",
                                             fontSize=7.4, leading=9.4,
                                             textColor=C["muted"], alignment=TA_CENTER)),
        ], box_spec("callout", fill=HexColor("#EEF4FB"), accent=C["indigo"],
                    bdr=C["blue-bdr"], radius=5,
                    pad=dict(l=10, r=10, t=8, b=8), accent_w=0))

    def stat_row():
        w = (PAGE_W - 34 * mm_ - 3 * 8 * mm_) / 4
        cells = []
        widths = []
        for i in range(4):
            if i:
                cells.append([])
                widths.append(8 * mm_)
            cells.append(stat_box("60%", "ĐỌC HIỂU (6,0đ)", "8 TNKQ + 2 Tự luận<br/>Thần thoại ngoài SGK") if i == 0 else
                          stat_box("40%", "LÀM VĂN (4,0đ)", "01 Bài văn nghị luận<br/>Phân tích, đánh giá") if i == 1 else
                          stat_box("40-30-30", "TỈ LỆ NHẬN THỨC", "Nhận biết 40% • Thông hiểu 30%<br/>Vận dụng 30%") if i == 2 else
                          stat_box("106 CÂU", "NGÂN HÀNG & 6 ĐỀ", "100% có đáp án,<br/>giải nhiễu & văn mẫu"))
            widths.append(w)
        return cells, widths

    _cells, _widths = stat_row()
    story.append(Table([_cells], colWidths=_widths, hAlign="CENTER"))
    story.append(Spacer(1, 10 * mm_))

    # Four pillars
    def pillar(title, body):
        return BoxFlowable([
            Paragraph(title, ParagraphStyle("pl_t", fontName="DejaVuSans-Bold",
                                            fontSize=8.6, leading=11,
                                            textColor=HexColor("#FCD34D"))),
            Spacer(1, 2),
            Paragraph(body, ParagraphStyle("pl_b", fontName="DejaVuSans",
                                           fontSize=8, leading=10.6,
                                           textColor=HexColor("#E2E8F0"))),
        ], box_spec("callout", fill=C["cover-dark"], accent=None, bdr=C["cover-edge"],
                    stroke_w=0.6, radius=5, pad=dict(l=10, r=10, t=9, b=9), accent_w=0))

    def pillar_row():
        w = (PAGE_W - 34 * mm_ - 3 * 12 * mm_) / 4
        cells = []
        widths = []
        items = [
            ("01. HỆ THỐNG HÓA SIÊU TRÍ NHỚ",
             "Sơ đồ hóa Dual-Coding, Khẩu quyết 5K–1C, Ma trận phân biệt 5 thể loại tự sự & 12 thần thoại ngoài SGK."),
            ("02. PHỦ KÍN 100% BẢN ĐẶC TẢ",
             "13/13 chỉ báo Đọc hiểu, chuyên đề Từ Hán Việt & Tu từ, Công thức 4 bước trả lời Tự luận đạt điểm tối đa."),
            ("03. DÀN Ý VẠN NĂNG & VĂN MẪU 4,0Đ",
             "Mô hình Ngôi Đền 5 Tầng phân tích chủ đề & nghệ thuật thần thoại kèm 06 bài văn mẫu hoàn chỉnh."),
            ("04. TRỌN BỘ CÂU HỎI & ĐÁP ÁN CHI TIẾT",
             "40 câu luyện theo chỉ báo + 06 đề thi chuẩn 90 phút (66 câu), giải thích từng phương án nhiễu & thang điểm 0,25."),
        ]
        for i, (t, b) in enumerate(items):
            if i:
                cells.append([])
                widths.append(12 * mm_)
            cells.append(pillar(t, b))
            widths.append(w)
        return cells, widths

    _cells, _widths = pillar_row()
    story.append(Table([_cells], colWidths=_widths, hAlign="CENTER"))
    story.append(Spacer(1, 70))  # flexible filler (1fr equivalent)
    story.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#3B5B8C"),
                            hAlign="CENTER", spaceBefore=2, spaceAfter=2))
    story.append(Spacer(1, 4 * mm_))
    story.append(Table(
        [[Paragraph("Biên soạn chuyên sâu theo định hướng đánh giá năng lực của Bộ GD&ĐT",
                    ParagraphStyle("cov_f1", fontName="DejaVuSans", fontSize=8.5,
                                    leading=11, textColor=HexColor("#CBD5E1"))),
          Paragraph("NĂM HỌC 2026 – 2027",
                    ParagraphStyle("cov_f2", fontName="DejaVuSans-Bold", fontSize=9,
                                   leading=11, textColor=HexColor("#FCD34D")))]],
        colWidths=[PAGE_W - 34 * mm_ - 120, 120], hAlign="CENTER"))
    story[-1].setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    story.append(NextPageTemplate("Body"))
    story.append(PageBreak())

    # ---------------- TOC page ----------------
    story.append(BoxFlowable([
        Paragraph("CẨM NANG SỬ DỤNG ĐỀ CƯƠNG THEO KHOA HỌC NHẬN THỨC (COGNITIVE RETENTION)",
                  ParagraphStyle("cg_t", fontName="DejaVuSans-Bold", fontSize=10,
                                 leading=12, textColor=C["navy"])),
        Spacer(1, 4),
    ], box_spec("callout", fill=C["blue-soft"], accent=C["indigo"],
                bdr=C["blue-bdr"], radius=6, pad=dict(l=14, r=14, t=12, b=12), accent_w=4)))
    story.append(Spacer(1, 6))
    guide_items = [
        ("Mã hóa kép (Dual Coding):", " Kết hợp bảng ma trận đối chiếu và sơ đồ cấu trúc để não bộ lưu trữ đồng thời kênh ngôn ngữ và kênh không gian."),
        ("Khẩu quyết âm vần (Chunking & Mnemonics):", " Mọi cụm kiến thức phức tạp đều được nén thành công thức ngắn gọn (5K–1C, GỌI–TRÍCH–GIẢI–CHỐT)."),
        ("Phòng vệ lỗi sai (Error Inoculation):", " Hệ thống hộp Cảnh báo bẫy phòng thi chỉ rõ các phương án nhiễu hay đánh lừa học sinh nhất."),
        ("Truy hồi chủ động (Active Recall):", " Ngân hàng 40 câu theo chỉ báo + 06 đề thi thực chiến (66 câu) + 24 thẻ Flashcards kèm lộ trình ôn 7 ngày."),
    ]
    for lead, rest in guide_items:
        story.append(Paragraph(
            f"<b>{sanitize(lead)}</b>{sanitize(rest)}",
            ParagraphStyle("gi", fontName="DejaVuSans", fontSize=9, leading=12.6,
                           textColor=C["ink"], leftIndent=10, firstLineIndent=-10,
                           spaceAfter=3, bulletText="◆")))
    story.append(Spacer(1, 10))
    story.append(Paragraph("MỤC LỤC TỔNG QUÁT",
                           ParagraphStyle("toch", fontName="DejaVuSans-Bold", fontSize=12.5,
                                          leading=15, textColor=C["navy"], spaceAfter=2)))
    story.append(HRFlowable(width="100%", thickness=1.2, color=C["indigo"],
                            spaceBefore=0, spaceAfter=6, hAlign="LEFT"))

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc0", fontName="DejaVuSans-Bold", fontSize=10,
                       leading=14, textColor=C["navy"], leftIndent=0),
        ParagraphStyle("toc1", fontName="DejaVuSans", fontSize=9.5,
                       leading=13, textColor=C["ink"], leftIndent=14),
        ParagraphStyle("toc2", fontName="DejaVuSans", fontSize=9,
                       leading=12, textColor=C["slate"], leftIndent=26),
    ]
    toc.dotsMinLevel = 0
    story.append(toc)

    story.append(PageBreak())

    # ---------------- Parts ----------------
    part_files = [
        "part1_matrix.typ", "part2_knowledge.typ", "part3_vietnamese.typ",
        "part4_reading_skills.typ", "part5_writing_skills.typ",
        "part6_exams_1_3.typ", "part7_exams_4_6.typ", "part8_memory_kit.typ",
    ]
    for idx, pf in enumerate(part_files):
        text = (SRC / pf).read_text(encoding="utf-8")
        # Drop the per-file import line (template symbols are injected below).
        text = re.sub(r'#import\s*"template\.typ"\s*:\s*\*\s*\n?', "", text)
        items = scan_items(text)
        avail = PAGE_W - 34 * mm
        flows = render_content_items(text and "", avail) if False else None
        # Build flows from items directly:
        flows = []
        for it in items:
            if it[0] == "para":
                flows += inline_flowables(parse_inline(it[1]), st_normal, avail)
            elif it[0] == "heading":
                flows.append(render_heading(it[1], it[2]))
            elif it[0] == "list":
                if it[1] == "bullet":
                    flows.append(BulletFlowable(parse_inline(it[2]), avail))
                else:
                    _, _, num, txt = it
                    flows.append(NumberFlowable(num, parse_inline(txt), avail))
            elif it[0] == "block":
                flows.append(render_block(it[1], avail))
        if idx > 0:
            story.append(PageBreak())
        story += flows
        story.append(Spacer(1, 6))

    return story


def main():
    story = build_story()
    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id="cover",
                        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    body_frame = Frame(17 * mm, 19 * mm, PAGE_W - 34 * mm, PAGE_H - 39 * mm, id="body")
    doc = DeCuongDoc(
        str(OUT), pagesize=A4,
        title="Đề cương ôn tập Giữa kì I Ngữ văn 10 - Kết nối tri thức (2026-2027)",
        author="Tài liệu Ôn tập Chuyên sâu Ngữ văn 10 - GDPT 2018",
        subject="Ôn tập Thi giữa kì I môn Ngữ văn 10 (Kết nối tri thức với cuộc sống)",
    )
    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[cover_frame], onPage=cover_decorations),
        PageTemplate(id="Body", frames=[body_frame], onPage=body_decorations),
    ])
    doc.multiBuild(story, canvasmaker=NumberedCanvas)
    print(f"Wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
