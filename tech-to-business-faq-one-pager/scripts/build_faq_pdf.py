#!/usr/bin/env python3
"""Build a one-page FAQ PDF with Build to Lead branding.

Usage:
  python build_faq_pdf.py faq.json output.pdf [--page a4|letter]

The JSON spec (see SKILL.md for the full description):
{
  "language": "es" | "en",
  "title": "...", "subtitle": "...",
  "version": "1.0", "updated": "2026-10-13", "owner": "...",
  "at_a_glance": [{"label": "...", "value": "..."}],          # up to 4
  "faqs": [{"w": "what|why|who|when|where|how|limits|help", "q": "...", "a": "..."}],
  "can": ["..."], "cannot": ["..."],
  "help": {"contact": "...", "channel": "...", "hours": "...", "response_time": "...", "escalation": "..."}
}

Everything must fit on ONE page. The script shrinks text slightly if needed and
fails with a clear message if the content is still too long.
UPPERCASE placeholders like ENTER_DATE or INGRESA_FECHA are highlighted.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

try:
    from reportlab.lib.colors import HexColor, white
    from reportlab.lib.pagesizes import A4, LETTER
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas
    from reportlab.platypus import Paragraph
except ImportError:  # pragma: no cover
    sys.exit("reportlab is required: pip install reportlab")

# --- Build to Lead brand --------------------------------------------------
NAVY = HexColor("#171A30")
TEAL = HexColor("#204B4C")
TERRACOTTA = HexColor("#A97F6A")
GRAY = HexColor("#4E4F52")
TEAL_TINT = HexColor("#E6EEEE")
TERRA_TINT = HexColor("#F4ECE8")
RULE = HexColor("#D5DADA")
PLACEHOLDER_BG = "#F2D9CC"

LOGO = Path(__file__).resolve().parent.parent / "assets" / "build-to-lead-logo.png"

LABELS = {
    "es": {
        "eyebrow": "PREGUNTAS FRECUENTES",
        "glance": "EN UN VISTAZO",
        "can": "Sí puedes",
        "cannot": "No puedes / límites",
        "rules": "LAS REGLAS DEL JUEGO",
        "help": "¿NECESITAS AYUDA?",
        "contact": "Contacto",
        "channel": "Canal",
        "hours": "Horario",
        "response_time": "Tiempo de respuesta",
        "escalation": "Si es urgente",
        "made": "Hecho con",
        "by": "por Build to Lead",
        "version": "Versión",
        "updated": "Actualizado",
        "owner": "Responsable",
        "w": {"what": "QUÉ", "why": "POR QUÉ", "who": "QUIÉN", "when": "CUÁNDO",
              "where": "DÓNDE", "how": "CÓMO", "limits": "LÍMITES", "help": "AYUDA"},
    },
    "en": {
        "eyebrow": "FREQUENTLY ASKED QUESTIONS",
        "glance": "AT A GLANCE",
        "can": "You can",
        "cannot": "You can't / limits",
        "rules": "THE RULES OF THE GAME",
        "help": "NEED HELP?",
        "contact": "Contact",
        "channel": "Channel",
        "hours": "Hours",
        "response_time": "Response time",
        "escalation": "If it's urgent",
        "made": "Made with",
        "by": "by Build to Lead",
        "version": "Version",
        "updated": "Updated",
        "owner": "Owner",
        "w": {"what": "WHAT", "why": "WHY", "who": "WHO", "when": "WHEN",
              "where": "WHERE", "how": "HOW", "limits": "LIMITS", "help": "HELP"},
    },
}

PLACEHOLDER_RE = re.compile(r"\b[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ0-9]*(?:_[A-ZÁÉÍÓÚÑ0-9]+)+\b")


def rich(text: str) -> str:
    """Escape text for reportlab and highlight UPPERCASE_PLACEHOLDERS."""
    safe = escape(str(text))
    return PLACEHOLDER_RE.sub(
        lambda m: f'<font backColor="{PLACEHOLDER_BG}" color="#7A4A35"><b>{m.group(0)}</b></font>', safe
    )


class Styles:
    def __init__(self, scale: float):
        s = scale
        self.q = ParagraphStyle("q", fontName="Helvetica-Bold", fontSize=9.6 * s, leading=12 * s, textColor=NAVY)
        self.a = ParagraphStyle("a", fontName="Helvetica", fontSize=8.9 * s, leading=11.6 * s, textColor=GRAY)
        self.tag = ParagraphStyle("tag", fontName="Helvetica-Bold", fontSize=6.6 * s, leading=8 * s, textColor=TEAL)
        self.item = ParagraphStyle("item", fontName="Helvetica", fontSize=8.6 * s, leading=11 * s, textColor=NAVY)
        self.help = ParagraphStyle("help", fontName="Helvetica", fontSize=8.6 * s, leading=11.2 * s, textColor=white)
        self.glance_label = ParagraphStyle("gl", fontName="Helvetica-Bold", fontSize=6.6, leading=8, textColor=TERRACOTTA)
        self.glance_value = ParagraphStyle("gv", fontName="Helvetica-Bold", fontSize=9.2, leading=11.2, textColor=NAVY)
        self.title = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=22, leading=25, textColor=NAVY)
        self.subtitle = ParagraphStyle("st", fontName="Helvetica", fontSize=10.5, leading=13.5, textColor=GRAY)


def para_h(p: Paragraph, width: float) -> float:
    return p.wrap(width, 10_000)[1]


def draw_heart(c: canvas.Canvas, x: float, y: float, size: float, color) -> None:
    c.saveState()
    c.setFillColor(color)
    s = size
    p = c.beginPath()
    p.moveTo(x + s / 2, y)
    p.curveTo(x + s * 0.05, y + s * 0.35, x - s * 0.05, y + s * 0.9, x + s * 0.27, y + s * 0.95)
    p.curveTo(x + s * 0.42, y + s * 0.98, x + s * 0.5, y + s * 0.82, x + s / 2, y + s * 0.75)
    p.curveTo(x + s * 0.5, y + s * 0.82, x + s * 0.58, y + s * 0.98, x + s * 0.73, y + s * 0.95)
    p.curveTo(x + s * 1.05, y + s * 0.9, x + s * 0.95, y + s * 0.35, x + s / 2, y)
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()


def draw_check(c, x, y, s, color):
    c.saveState(); c.setStrokeColor(color); c.setLineWidth(1.6); c.setLineCap(1)
    c.line(x, y + s * 0.5, x + s * 0.38, y + s * 0.12); c.line(x + s * 0.38, y + s * 0.12, x + s, y + s * 0.9)
    c.restoreState()


def draw_cross(c, x, y, s, color):
    c.saveState(); c.setStrokeColor(color); c.setLineWidth(1.6); c.setLineCap(1)
    c.line(x + s * 0.1, y + s * 0.1, x + s * 0.9, y + s * 0.9); c.line(x + s * 0.1, y + s * 0.9, x + s * 0.9, y + s * 0.1)
    c.restoreState()


def build(spec: dict, out: Path, pagesize) -> None:
    lang = spec.get("language", "en").lower()[:2]
    L = LABELS.get(lang, LABELS["en"])
    W, H = pagesize
    M = 34  # margin
    inner = W - 2 * M

    faqs = spec.get("faqs", [])
    can = spec.get("can", [])
    cannot = spec.get("cannot", [])
    help_ = spec.get("help", {})
    glance = spec.get("at_a_glance", [])[:4]

    header_h = 92
    glance_h = 44 if glance else 0
    footer_h = 30

    scales = [round(1.3 - i * 0.02, 2) for i in range(28)]  # 1.30 → 0.76, largest that fits wins
    fq_w = (inner - 18) / 2
    col_w = (inner - 12) / 2
    hw = inner - 120

    def layout(scale):
        st = Styles(scale)
        gap = 9 * scale

        def list_h(items):
            return sum(para_h(Paragraph(rich(i), st.item), col_w - 26 - 2 * scale) + 3 * scale for i in items)
        rules_h = (max(list_h(can), list_h(cannot)) + 30 * scale) if (can or cannot) else 0

        help_rows = [(L[k], help_[k]) for k in ["contact", "channel", "hours", "response_time", "escalation"] if help_.get(k)]
        help_lines = [Paragraph(f"<b>{escape(k)}:</b> {rich(v)}", st.help) for k, v in help_rows]
        help_h = 0
        if help_lines:
            help_h = max(sum(para_h(p, hw / 2 - 8) for p in help_lines[::2]),
                         sum(para_h(p, hw / 2 - 8) for p in help_lines[1::2])) + 26

        blocks = []
        for f in faqs:
            tag = Paragraph(escape(L["w"].get(f.get("w", ""), "").upper()), st.tag)
            q = Paragraph(rich(f.get("q", "")), st.q)
            a = Paragraph(rich(f.get("a", "")), st.a)
            h = para_h(tag, fq_w) + 1.5 + para_h(q, fq_w) + 2 + para_h(a, fq_w)
            blocks.append([tag, q, a, h])

        # split into two columns in order, balancing heights
        total = sum(b[3] + gap for b in blocks)
        col1, acc = [], 0
        for b in blocks:
            if not col1 or acc + (b[3] + gap) / 2 <= total / 2:
                col1.append(b); acc += b[3] + gap
            else:
                break
        col2 = blocks[len(col1):]
        faq_h = max(sum(b[3] + gap for b in col1), sum(b[3] + gap for b in col2)) - gap if blocks else 0
        return st, gap, rules_h, help_lines, help_h, col1, col2, faq_h

    top_y = H - M - header_h - (glance_h + 18 if glance else 10)   # first FAQ starts here
    floor_y = M + footer_h + 6                                        # nothing goes below
    for scale in scales:
        st, gap, rules_h, help_lines, help_h, col1, col2, faq_h = layout(scale)
        used = faq_h + (14 + rules_h if rules_h else 0) + (10 + help_h if help_h else 0)
        if used <= top_y - floor_y:
            break
    else:
        over = int(used - (top_y - floor_y))
        sys.exit(f"ERROR: content doesn't fit on one page (~{over} pt too long). "
                 "Shorten answers, remove a question, or trim the rules lists, then run again.")

    # spread leftover space a little between FAQs so the page breathes, keep the rest at the bottom
    leftover = (top_y - floor_y) - used
    n_rows = max(len(col1), len(col2), 1)
    extra = min(leftover * 0.6 / n_rows, 10)
    gap += extra
    faq_h += extra * (n_rows - 1)

    c = canvas.Canvas(str(out), pagesize=pagesize)
    c.setTitle(spec.get("title", "FAQ"))
    c.setAuthor("Build to Lead")
    c.setSubject(L["eyebrow"])

    # top accent bar
    c.setFillColor(TEAL); c.rect(0, H - 6, W, 6, fill=1, stroke=0)
    c.setFillColor(TERRACOTTA); c.rect(0, H - 6, W * 0.22, 6, fill=1, stroke=0)

    # logo, top-right corner (always)
    logo_h = 70
    if LOGO.exists():
        img = ImageReader(str(LOGO)); iw, ih = img.getSize()
        lw = logo_h * iw / ih
        c.drawImage(img, W - M - lw, H - M - logo_h + 8, lw, logo_h, mask="auto")
        text_w = inner - lw - 18
    else:
        text_w = inner

    # header text
    y = H - M - 4
    c.setFillColor(TERRACOTTA); c.setFont("Helvetica-Bold", 7.5)
    c.drawString(M, y, L["eyebrow"])
    tp = Paragraph(rich(spec.get("title", "")), Styles(1).title)
    th = para_h(tp, text_w); tp.drawOn(c, M, y - 6 - th)
    sp = Paragraph(rich(spec.get("subtitle", "")), Styles(1).subtitle)
    sh = para_h(sp, text_w); sp.drawOn(c, M, y - 10 - th - sh)

    # rule under header
    hy = H - M - header_h + 4
    c.setStrokeColor(RULE); c.setLineWidth(0.8); c.line(M, hy, W - M, hy)

    # at a glance
    if glance:
        gy = hy - 8 - glance_h
        n = len(glance); gw = (inner - 6 * (n - 1)) / n
        for i, g in enumerate(glance):
            gx = M + i * (gw + 6)
            c.setFillColor(TEAL_TINT); c.roundRect(gx, gy, gw, glance_h, 5, fill=1, stroke=0)
            c.setFillColor(TEAL); c.rect(gx, gy, 3, glance_h, fill=1, stroke=0)
            lp = Paragraph(escape(g.get("label", "")).upper(), st.glance_label)
            vp = Paragraph(rich(g.get("value", "")), st.glance_value)
            lh = para_h(lp, gw - 16); vh = para_h(vp, gw - 16)
            lp.drawOn(c, gx + 10, gy + glance_h - 8 - lh)
            vp.drawOn(c, gx + 10, gy + glance_h - 10 - lh - vh)

    # FAQs in two columns
    top = top_y

    def draw_col(blocks, x):
        yy = top
        for tag, q, a, h in blocks:
            th_ = para_h(tag, fq_w); tag.drawOn(c, x, yy - th_); yy -= th_ + 1.5
            qh = para_h(q, fq_w); q.drawOn(c, x, yy - qh); yy -= qh + 2
            ah = para_h(a, fq_w); a.drawOn(c, x, yy - ah); yy -= ah + gap
    draw_col(col1, M)
    draw_col(col2, M + fq_w + 18)
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    c.line(M + fq_w + 9, top, M + fq_w + 9, top - faq_h)

    # rules of the game
    ry = top - faq_h - 14 - rules_h
    if rules_h:
        for i, (items, title, tint, color, mark) in enumerate([
            (can, L["can"], TEAL_TINT, TEAL, draw_check),
            (cannot, L["cannot"], TERRA_TINT, TERRACOTTA, draw_cross),
        ]):
            bx = M + i * (col_w + 12)
            c.setFillColor(tint); c.roundRect(bx, ry, col_w, rules_h, 6, fill=1, stroke=0)
            c.setFillColor(color); c.setFont("Helvetica-Bold", 9 * scale)
            c.drawString(bx + 12, ry + rules_h - 16 * scale, title)
            yy = ry + rules_h - 24 * scale
            for it in items:
                indent = 22 + 2 * scale
                p = Paragraph(rich(it), st.item); ph = para_h(p, col_w - 26 - 2 * scale)
                mark(c, bx + 12, yy - 9 * scale, 7 * scale, color)
                p.drawOn(c, bx + indent, yy - ph); yy -= ph + 3 * scale

    # help band
    if help_h:
        by = (ry if rules_h else top - faq_h) - 10 - help_h
        c.setFillColor(NAVY); c.roundRect(M, by, inner, help_h, 6, fill=1, stroke=0)
        c.setFillColor(TERRACOTTA); c.setFont("Helvetica-Bold", 9.5)
        c.drawString(M + 14, by + help_h - 18, L["help"])
        x1 = M + 120; colw2 = (inner - 120) / 2 - 8
        for col, items in enumerate([help_lines[::2], help_lines[1::2]]):
            yy = by + help_h - 13
            for p in items:
                ph = para_h(p, colw2); p.drawOn(c, x1 + col * (colw2 + 8), yy - ph); yy -= ph

    # footer
    fy = M + 8
    c.setStrokeColor(RULE); c.setLineWidth(0.6); c.line(M, fy + 14, W - M, fy + 14)
    c.setFont("Helvetica-Bold", 8); c.setFillColor(NAVY)
    made = L["made"] + " "; c.drawString(M, fy, made)
    mw = c.stringWidth(made, "Helvetica-Bold", 8)
    draw_heart(c, M + mw, fy - 0.5, 8, TERRACOTTA)
    c.setFillColor(TEAL); c.drawString(M + mw + 11, fy, L["by"])
    meta = []
    for k in ["owner", "version", "updated"]:
        if spec.get(k):
            meta.append(f"{L[k]}: {spec[k]}")
    c.setFont("Helvetica", 7.5); c.setFillColor(GRAY)
    c.drawRightString(W - M, fy, "  ·  ".join(meta))

    c.showPage(); c.save()


def main() -> int:
    ap = argparse.ArgumentParser(description="Build a one-page FAQ PDF with Build to Lead branding")
    ap.add_argument("spec", help="FAQ JSON file")
    ap.add_argument("output", help="output PDF path")
    ap.add_argument("--page", choices=["a4", "letter"], default="a4")
    a = ap.parse_args()
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    build(spec, Path(a.output), A4 if a.page == "a4" else LETTER)
    print(f"PDF created: {a.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
