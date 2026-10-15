#!/usr/bin/env python3
"""Build the Build to Lead interview guide as a fillable PDF.

Usage:
  python build_interview.py interview.json OUTPUT.pdf [--page a4|letter] [--logo my-logo.png]

The PDF has fields the interviewer fills in any PDF reader: candidate, interviewer and
date; a note box, the evaluation letters heard and a 1-4 score for each question; and a
final assessment with a recommendation.

Two modes, set with "mode" in the JSON (shared by tech-to-business-interviews and
tech-interviews; keep both copies identical with `skills.py sync`):
  "business"  (default) every question is evaluated with STAR.
  "technical" technical questions use the C·R·E·H rubric (correct, reasoning, edge cases,
              hands-on); questions with "type": "experience" or "business" use STAR.
              A question with "big": true gets a tall answer box (architecture exercise).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_LOGO = HERE.parent / "assets" / "build-to-lead-logo.png"
# Footer of every page: "Made with ♥ by @build2lead.club and @maisfloro.tech", both linked to Instagram
INSTAGRAM = [("@build2lead.club", "https://www.instagram.com/build2lead.club/"),
             ("@maisfloro.tech", "https://www.instagram.com/maisfloro.tech/")]


def ensure(module: str, package: str) -> None:
    try:
        __import__(module)
    except ImportError:
        print(f"Installing {package}...", file=sys.stderr)
        cmd = [sys.executable, "-m", "pip", "install", "--quiet", package]
        if subprocess.run(cmd).returncode != 0:
            subprocess.run(cmd + ["--break-system-packages"], check=True)


# ---------------------------------------------------------------- brand and labels
BRAND = {
    "navy": "#171A30", "teal": "#204B4C", "terra": "#A97F6A", "gray": "#4E4F52",
    "teal_tint": "#E6EEEE", "terra_tint": "#F4ECE8", "rule": "#D5DADA",
    "ph_bg": "#F2D9CC", "ph_fg": "#7A4A35", "field": "#FBFAF8",
}

LABELS = {
    "en": {
        "eyebrow": "INTERVIEW GUIDE  ·  STAR DEEP DIVE",
        "candidate": "CANDIDATE", "interviewer": "INTERVIEWER", "date": "DATE",
        "case": "THE CASE", "focus": "What this role protects",
        "how": "HOW TO EVALUATE",
        "star": [("S", "Situation", "a real case, with its business stake"),
                 ("T", "Task", "what was theirs to solve, and the goal"),
                 ("A", "Action", "what they did and why, options discarded"),
                 ("R", "Result", "what changed, in numbers, for the business")],
        "scale": "Score: 4 strong (full STAR + business impact)  ·  3 good  ·  2 partial  ·  1 weak",
        "eyebrow_tech": "TECHNICAL INTERVIEW GUIDE  ·  DEEP DIVE",
        "tech": [("C", "Correct", "accurate, no hand-waving"),
                 ("R", "Reasoning", "explains why and weighs trade-offs"),
                 ("E", "Edge cases", "failure modes, limits, scale"),
                 ("H", "Hands-on", "has done it, with real details")],
        "scale_tech": "Score: 4 expert (all four, holds up when you dig)  ·  3 solid  ·  2 basic  ·  1 gaps"
                      "   |   Business questions (marked STAR): Situation, Task, Action, Result",
        "dig": "Dig deeper:", "expect": "Strong answer:",
        "notes": "Candidate's answer", "heard": "Heard", "score": "Score",
        "final": "FINAL ASSESSMENT", "strengths": "Strengths", "concerns": "Concerns",
        "avg": "Average score (1-4)", "next": "Next step",
        "rec": "Recommendation", "recs": ["Strong yes", "Yes", "No", "Strong no"],
        "made": "Made with", "by": "by", "and": "and", "page": "Page",
    },
    "es": {
        "eyebrow": "GUÍA DE ENTREVISTA  ·  PROFUNDIZACIÓN STAR",
        "candidate": "CANDIDATO/A", "interviewer": "ENTREVISTADOR/A", "date": "FECHA",
        "case": "EL CASO", "focus": "Lo que este rol protege",
        "how": "CÓMO EVALUAR",
        "star": [("S", "Situación", "un caso real, con lo que estaba en juego"),
                 ("T", "Tarea", "qué le tocaba resolver y la meta"),
                 ("A", "Acción", "qué hizo y por qué, qué descartó"),
                 ("R", "Resultado", "qué cambió, en números, para el negocio")],
        "scale": "Puntaje: 4 fuerte (STAR completo + impacto en negocio)  ·  3 bueno  ·  2 parcial  ·  1 débil",
        "eyebrow_tech": "GUÍA DE ENTREVISTA TÉCNICA  ·  PROFUNDIZACIÓN",
        "tech": [("C", "Correcto", "preciso, sin vaguedades"),
                 ("R", "Razonamiento", "explica el por qué y los trade-offs"),
                 ("B", "Casos borde", "fallas, límites, escala"),
                 ("P", "Práctica", "lo ha hecho, con detalles reales")],
        "scale_tech": "Puntaje: 4 experto (las cuatro, resiste al profundizar)  ·  3 sólido  ·  2 básico  ·  1 brechas"
                      "   |   Preguntas de negocio (marcadas STAR): Situación, Tarea, Acción, Resultado",
        "dig": "Profundiza:", "expect": "Respuesta fuerte:",
        "notes": "Respuesta del candidato/a", "heard": "Escuché", "score": "Puntaje",
        "final": "EVALUACIÓN FINAL", "strengths": "Fortalezas", "concerns": "Dudas o alertas",
        "avg": "Puntaje promedio (1-4)", "next": "Siguiente paso",
        "rec": "Recomendación", "recs": ["Sí, sin duda", "Sí", "No", "No, sin duda"],
        "made": "Hecho con", "by": "por", "and": "y", "page": "Página",
    },
}

PLACEHOLDER_RE = re.compile(r"[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ0-9]*(?:_[A-ZÁÉÍÓÚÑ0-9]+)+")
# Characters outside the PDF standard fonts' encoding
REPLACE = {"→": "->", "←": "<-", "≈": "~", "≥": ">=", "≤": "<=", "✓": "OK", "·": "·", "‑": "-"}


def clean(text) -> str:
    text = str(text or "").strip()
    for a, b in REPLACE.items():
        text = text.replace(a, b)
    return text.encode("cp1252", "replace").decode("cp1252")


BUSINESS_TYPES = {"experience", "business"}


def is_technical(spec: dict) -> bool:
    return str(spec.get("mode", "business")).lower() == "technical"


def check(spec: dict) -> list[str]:
    warnings = []
    if is_technical(spec):
        biz = sum(1 for b in spec.get("blocks", []) for q in b.get("questions", [])
                  if str(q.get("type", "technical")).lower() in BUSINESS_TYPES)
        if not 3 <= biz <= 5:
            warnings.append(f"{biz} business questions; a technical interview is ~80/20, so use about 4.")
    blocks = spec.get("blocks", [])
    if len(blocks) != 5:
        warnings.append(f"{len(blocks)} blocks; use 5.")
    total = 0
    for i, b in enumerate(blocks, 1):
        qs = b.get("questions", [])
        total += len(qs)
        if len(qs) != 4:
            warnings.append(f"block {i} has {len(qs)} questions; use 4.")
        for q in qs:
            for key in ("q", "deep", "expect"):
                if not str(q.get(key, "")).strip():
                    warnings.append(f"a question in block {i} has no '{key}'.")
            if len(str(q.get("q", ""))) > (320 if q.get("big") else 230):
                warnings.append(f"a question in block {i} is long; keep it to 2 sentences.")
            if len(str(q.get("expect", "")).split()) > 24:
                warnings.append(f"a strong-answer line in block {i} is long; keep it to ~20 words.")
    if total != 20:
        warnings.append(f"{total} questions; use 20.")
    if not str(spec.get("case", "")).strip():
        warnings.append("the case is empty.")
    return warnings


# ---------------------------------------------------------------- drawing helpers
class Doc:
    def __init__(self, path: Path, spec: dict, page: str, logo: Path):
        from reportlab.lib.pagesizes import A4, LETTER
        from reportlab.pdfgen import canvas
        from reportlab.lib.colors import HexColor
        from reportlab.pdfbase.pdfmetrics import stringWidth

        self.C = {k: HexColor(v) for k, v in BRAND.items()}
        self.white = HexColor("#FFFFFF")
        self.sw = stringWidth
        self.size = A4 if page == "a4" else LETTER
        self.W, self.H = self.size
        self.M = 38
        self.bottom = 54
        self.c = canvas.Canvas(str(path), pagesize=self.size)
        self.c.setTitle(clean(f"{spec.get('role', '')} - interview"))
        self.c.setAuthor("Build to Lead")
        self.spec = spec
        self.L = LABELS.get(str(spec.get("language", "en")).lower()[:2], LABELS["en"])
        self.logo = logo
        self.page_no = 1
        self.tech = is_technical(spec)
        self.y = self.H - self.M

    # text ------------------------------------------------------------
    def wrap(self, text: str, font: str, size: float, width: float, first_indent: float = 0) -> list[list[str]]:
        words, lines, cur, cur_w = clean(text).split(), [], [], first_indent
        space = self.sw(" ", font, size)
        for w in words:
            ww = self.sw(w, font, size)
            if cur and cur_w + space + ww > width:
                lines.append(cur)
                cur, cur_w = [w], ww
            else:
                cur_w += (space if cur else 0) + ww
                cur.append(w)
        if cur:
            lines.append(cur)
        return lines

    def text(self, text, x, y, width, font="Helvetica", size=9, leading=None, color="navy",
             prefix=None, prefix_font="Helvetica-Bold", prefix_color="terra") -> float:
        """Draw wrapped text (optional bold prefix on the first line), highlighting PLACEHOLDERS.
        Returns the y below the last line."""
        leading = leading or size * 1.28
        c = self.c
        indent = 0
        if prefix:
            indent = self.sw(clean(prefix) + " ", prefix_font, size)
        lines = self.wrap(text, font, size, width, indent)
        if not lines and prefix:
            lines = [[]]
        space = self.sw(" ", font, size)
        for i, words in enumerate(lines):
            cx = x
            if i == 0 and prefix:
                c.setFont(prefix_font, size)
                c.setFillColor(self.C[prefix_color])
                c.drawString(cx, y, clean(prefix))
                cx += indent
            for w in words:
                ww = self.sw(w, font, size)
                core = w.strip(".,;:()¿?¡!\"'")
                if core and PLACEHOLDER_RE.fullmatch(core):
                    c.setFillColor(self.C["ph_bg"])
                    c.rect(cx - 1, y - size * 0.25, ww + 2, size * 1.15, stroke=0, fill=1)
                    c.setFillColor(self.C["ph_fg"])
                    c.setFont("Helvetica-Bold", size)
                else:
                    c.setFillColor(self.C[color])
                    c.setFont(font, size)
                c.drawString(cx, y, w)
                cx += ww + space
            y -= leading
        return y

    def height(self, text, font, size, width, leading=None, prefix=None, prefix_font="Helvetica-Bold") -> float:
        leading = leading or size * 1.28
        indent = self.sw(clean(prefix) + " ", prefix_font, size) if prefix else 0
        return max(1, len(self.wrap(text, font, size, width, indent))) * leading

    # page ------------------------------------------------------------
    def footer(self):
        c, L = self.c, self.L
        c.setStrokeColor(self.C["rule"])
        c.setLineWidth(0.6)
        c.line(self.M, 36, self.W - self.M, 36)
        c.setFont("Helvetica", 7.5)
        c.setFillColor(self.C["gray"])
        c.drawString(self.M, 24, clean(f"{self.spec.get('role', '')}  ·  {L['page']} {self.page_no}"))
        made, by, conj = clean(L["made"]) + " ", " " + clean(L["by"]) + " ", " " + clean(L["and"]) + " "
        (h1, u1), (h2, u2) = INSTAGRAM
        f, fb, size = "Helvetica", "Helvetica-Bold", 7.5
        heart_w = 7
        w = (self.sw(made, f, size) + heart_w + self.sw(by, f, size) + self.sw(h1, fb, size)
             + self.sw(conj, f, size) + self.sw(h2, fb, size))
        x = self.W - self.M - w
        c.setFillColor(self.C["gray"])
        c.setFont(f, size)
        c.drawString(x, 24, made)
        x += self.sw(made, f, size)
        self.heart(x + heart_w / 2, 26.6, 2.9)
        x += heart_w
        for text, url in ((by, None), (h1, u1), (conj, None), (h2, u2)):
            font = fb if url else f
            c.setFont(font, size)
            c.setFillColor(self.C["terra" if url else "gray"])
            c.drawString(x, 24, text)
            tw = self.sw(text, font, size)
            if url:
                c.linkURL(url, (x, 21, x + tw, 32), relative=0, thickness=0)
            x += tw

    def heart(self, cx: float, cy: float, r: float):
        c = self.c
        p = c.beginPath()
        p.moveTo(cx, cy - r * 1.05)
        p.curveTo(cx - r * 1.9, cy + r * 0.05, cx - r * 0.95, cy + r * 1.45, cx, cy + r * 0.55)
        p.curveTo(cx + r * 0.95, cy + r * 1.45, cx + r * 1.9, cy + r * 0.05, cx, cy - r * 1.05)
        p.close()
        c.setFillColor(self.C["terra"])
        c.drawPath(p, stroke=0, fill=1)

    def new_page(self):
        self.footer()
        self.c.showPage()
        self.page_no += 1
        self.y = self.H - self.M

    def need(self, h: float):
        if self.y - h < self.bottom:
            self.new_page()

    def field(self, name, x, y, w, h, multiline=False, tooltip=""):
        self.c.acroForm.textfield(
            name=name, tooltip=tooltip, x=x, y=y, width=w, height=h,
            borderColor=self.C["rule"], fillColor=self.C["field"], textColor=self.C["navy"],
            borderWidth=0.7, fontName="Helvetica", fontSize=8 if multiline else 9,
            fieldFlags="multiline" if multiline else "", forceBorder=True)

    # sections --------------------------------------------------------
    def header(self):
        c, L, s, M = self.c, self.L, self.spec, self.M
        from reportlab.lib.utils import ImageReader
        img = ImageReader(str(self.logo))
        iw, ih = img.getSize()
        scale = min(56 / ih, 130 / iw)
        lw, lh = iw * scale, ih * scale
        c.drawImage(img, self.W - M - lw, self.H - M - lh + 4, lw, lh, mask="auto")

        y = self.H - M - 8
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(self.C["terra"])
        c.drawString(M, y, clean(L["eyebrow_tech" if self.tech else "eyebrow"]))
        y -= 24
        c.setFont("Helvetica-Bold", 21)
        c.setFillColor(self.C["navy"])
        c.drawString(M, y, clean(s.get("role", "")))
        y -= 15
        sub = "  ·  ".join(clean(v) for v in (s.get("team"), s.get("duration")) if v)
        if sub:
            c.setFont("Helvetica", 9.5)
            c.setFillColor(self.C["gray"])
            c.drawString(M, y, sub)
        y -= 20

        # candidate / interviewer / date
        cols = [(L["candidate"], "candidate", 0.42), (L["interviewer"], "interviewer", 0.36), (L["date"], "date", 0.22)]
        x, total, gap = M, self.W - 2 * M, 10
        for label, name, frac in cols:
            w = (total - gap * 2) * frac
            c.setFont("Helvetica-Bold", 6.8)
            c.setFillColor(self.C["terra"])
            c.drawString(x, y, clean(label))
            self.field(name, x, y - 21, w, 17, tooltip=clean(label))
            x += w + gap
        y -= 36

        # the case
        inner = self.W - 2 * M - 24
        case_h = self.height(s.get("case", ""), "Helvetica", 9.2, inner, 12)
        focus = [clean(f) for f in s.get("focus", [])][:3]
        focus_h = 15 if focus else 0
        box_h = 16 + 8 + case_h + focus_h + 8
        c.setFillColor(self.C["teal_tint"])
        c.roundRect(M, y - box_h, self.W - 2 * M, box_h, 6, stroke=0, fill=1)
        c.setFillColor(self.C["teal"])
        c.rect(M, y - box_h, 3.5, box_h, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(M + 12, y - 14, clean(L["case"]))
        ty = self.text(s.get("case", ""), M + 12, y - 28, inner, size=9.2, leading=12)
        if focus:
            self.text("  ·  ".join(focus), M + 12, ty - 3, inner, font="Helvetica", size=8.2,
                      color="teal", prefix=clean(L["focus"]) + ":", prefix_color="teal")
        y -= box_h + 10

        # how to evaluate (STAR)
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(self.C["terra"])
        c.drawString(M, y, clean(L["how"]))
        y -= 6
        colw = (self.W - 2 * M - 3 * 8) / 4
        for i, (letter, name, desc) in enumerate(L["tech" if self.tech else "star"]):
            x = M + i * (colw + 8)
            c.setFillColor(self.C["terra_tint"])
            c.roundRect(x, y - 40, colw, 36, 5, stroke=0, fill=1)
            c.setFillColor(self.C["terra"])
            c.circle(x + 13, y - 22, 8, stroke=0, fill=1)
            c.setFillColor(self.white)
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(x + 13, y - 25.2, letter)
            c.setFillColor(self.C["navy"])
            c.setFont("Helvetica-Bold", 8)
            c.drawString(x + 26, y - 15, clean(name))
            self.text(desc, x + 26, y - 25, colw - 30, size=6.9, leading=8.2, color="gray")
        y -= 50
        c.setFont("Helvetica", 7.4)
        c.setFillColor(self.C["gray"])
        for i, line in enumerate(clean(L["scale_tech" if self.tech else "scale"]).split("   |   ")):
            c.drawString(M, y - i * 10, line.strip())
            if i:
                y -= 10
        self.y = y - 12

    def block_title(self, n: int, title: str):
        c, M = self.c, self.M
        self.need(22 + 64)
        y = self.y
        c.setFillColor(self.C["teal"])
        c.roundRect(M, y - 16, self.W - 2 * M, 17, 4, stroke=0, fill=1)
        c.setFillColor(self.white)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(M + 9, y - 11, clean(f"{n}  ·  {title}").upper())
        self.y = y - 22

    def radio(self, name, value, x, y, size, color, tooltip):
        """A clean round option: the circle is drawn on the page, the button itself is transparent
        (the built-in circle appearance renders badly in some readers)."""
        from reportlab.lib.colors import transparent
        c = self.c
        c.setStrokeColor(self.C[color])
        c.setLineWidth(0.8)
        c.circle(x + size / 2, y + size / 2, size / 2, stroke=1, fill=0)
        c.acroForm.radio(name=name, value=value, x=x, y=y, size=size, shape="square", buttonStyle="circle",
                         borderWidth=0, borderColor=transparent, fillColor=transparent,
                         textColor=self.C[color], selected=False, tooltip=tooltip)

    def checks_row(self, n: int, x: float, y: float, letters: str = "STAR"):
        """'Heard S T A R · Score 1 2 3 4' on one line starting at x, baseline y."""
        c, L = self.c, self.L
        c.setFont("Helvetica-Bold", 6.6)
        c.setFillColor(self.C["gray"])
        c.drawString(x, y, clean(L["heard"]))
        x += self.sw(clean(L["heard"]) + "  ", "Helvetica-Bold", 6.6)
        for letter in letters:
            c.acroForm.checkbox(name=f"q{n}_{letter}", x=x, y=y - 2.5, size=9, buttonStyle="check",
                                borderColor=self.C["teal"], fillColor=self.white, textColor=self.C["teal"],
                                borderWidth=0.8, forceBorder=True, tooltip=f"{n}. {letter}")
            c.setFont("Helvetica-Bold", 7.2)
            c.setFillColor(self.C["teal"])
            c.drawString(x + 11.5, y, letter)
            x += 23
        x += 8
        c.setFont("Helvetica-Bold", 6.6)
        c.setFillColor(self.C["gray"])
        c.drawString(x, y, clean(L["score"]))
        x += self.sw(clean(L["score"]) + "  ", "Helvetica-Bold", 6.6)
        for v in "1234":
            self.radio(f"q{n}_score", v, x, y - 2.5, 9, "terra", f"{n}. {v}")
            c.setFont("Helvetica-Bold", 7.2)
            c.setFillColor(self.C["terra"])
            c.drawString(x + 11.5, y, v)
            x += 22

    def question(self, n: int, q: dict):
        c, L, M = self.c, self.L, self.M
        left_x = M + 24
        left_w = 292
        right_x = left_x + left_w + 12
        right_w = self.W - M - right_x
        h_q = self.height(q.get("q"), "Helvetica-Bold", 8.6, left_w, 10.6)
        h_d = self.height(q.get("deep"), "Helvetica", 7.6, left_w, 9.2, prefix=L["dig"])
        h_e = self.height(q.get("expect"), "Helvetica-Oblique", 7.6, left_w, 9.2, prefix=L["expect"])
        left_h = h_q + 2 + h_d + 1 + h_e + 12
        row_h = max(left_h, 48) + 3
        if q.get("big"):
            row_h = max(row_h, 150)
        star_q = (not self.tech) or str(q.get("type", "technical")).lower() in BUSINESS_TYPES
        letters = "STAR" if star_q else "".join(t[0] for t in L["tech"])
        self.need(row_h + 6)
        y = self.y

        c.setFillColor(self.C["terra"])
        c.circle(M + 8, y - 3, 8, stroke=0, fill=1)
        c.setFillColor(self.white)
        c.setFont("Helvetica-Bold", 7.6 if n < 10 else 7)
        c.drawCentredString(M + 8, y - 5.8, str(n))

        ty = self.text(q.get("q"), left_x, y - 6, left_w, font="Helvetica-Bold", size=8.6, leading=10.6)
        ty = self.text(q.get("deep"), left_x, ty - 2, left_w, size=7.6, leading=9.2, color="gray",
                       prefix=L["dig"], prefix_color="terra")
        ty = self.text(q.get("expect"), left_x, ty - 1, left_w, font="Helvetica-Oblique", size=7.6, leading=9.2,
                       color="gray", prefix=L["expect"], prefix_color="teal")
        self.checks_row(n, left_x, y - row_h + 6, letters)

        # answer box, as tall as the question row
        c.setFont("Helvetica-Bold", 6)
        c.setFillColor(self.C["terra"])
        c.drawString(right_x, y + 1.5, clean(L["notes"]).upper())
        self.field(f"q{n}_answer", right_x, y - row_h + 2, right_w, row_h - 1, multiline=True,
                   tooltip=clean(f"{n}. {L['notes']}"))

        self.y = y - row_h - 2
        c.setStrokeColor(self.C["rule"])
        c.setLineWidth(0.5)
        c.line(M, self.y, self.W - M, self.y)
        self.y -= 8

    def final(self):
        c, L, M = self.c, self.L, self.M
        total_w = self.W - 2 * M
        if self.y - 148 < self.bottom - 12:   # the final block may use a little of the bottom margin
            self.new_page()
        y = self.y - 4
        c.setFillColor(self.C["navy"])
        c.roundRect(M, y - 17, total_w, 18, 4, stroke=0, fill=1)
        c.setFillColor(self.white)
        c.setFont("Helvetica-Bold", 8.4)
        c.drawString(M + 9, y - 11.5, clean(L["final"]))
        y -= 28
        half = (total_w - 12) / 2
        for i, (label, name) in enumerate(((L["strengths"], "strengths"), (L["concerns"], "concerns"))):
            x = M + i * (half + 12)
            c.setFont("Helvetica-Bold", 6.8)
            c.setFillColor(self.C["terra"])
            c.drawString(x, y, clean(label).upper())
            self.field(name, x, y - 44, half, 40, multiline=True, tooltip=clean(label))
        y -= 58
        c.setFont("Helvetica-Bold", 6.8)
        c.setFillColor(self.C["terra"])
        c.drawString(M, y, clean(L["avg"]).upper())
        self.field("average_score", M, y - 21, 90, 17, tooltip=clean(L["avg"]))
        rx = M + 110
        c.drawString(rx, y, clean(L["rec"]).upper())
        x = rx
        for i, r in enumerate(L["recs"]):
            self.radio("recommendation", f"r{i}", x, y - 17, 10, "teal", clean(r))
            c.setFont("Helvetica-Bold", 8)
            c.setFillColor(self.C["navy"])
            c.drawString(x + 13, y - 14.5, clean(r))
            x += 13 + self.sw(clean(r), "Helvetica-Bold", 8) + 16
            c.setFillColor(self.C["terra"])
            c.setFont("Helvetica-Bold", 6.8)
        y -= 36
        c.setFont("Helvetica-Bold", 6.8)
        c.setFillColor(self.C["terra"])
        c.drawString(M, y, clean(L["next"]).upper())
        self.field("next_step", M, y - 21, total_w, 17, tooltip=clean(L["next"]))
        self.y = y - 30

    def build(self):
        self.header()
        n = 0
        for b, block in enumerate(self.spec.get("blocks", []), 1):
            self.block_title(b, block.get("title", ""))
            for q in block.get("questions", []):
                n += 1
                self.question(n, q)
        self.final()
        self.footer()
        self.c.save()
        return self.page_no


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", help="interview JSON file")
    ap.add_argument("output", help="output .pdf path")
    ap.add_argument("--page", choices=["a4", "letter"], default="a4")
    ap.add_argument("--logo", help="PNG/JPG to replace the Build to Lead logo")
    a = ap.parse_args()

    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    logo = DEFAULT_LOGO
    if a.logo:
        logo = Path(a.logo).expanduser()
        if not logo.is_file():
            raise SystemExit(f"ERROR: logo not found: {logo}")
        if logo.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            raise SystemExit("ERROR: the logo must be a PNG or JPG file (convert SVG or other formats first).")
    out = Path(a.output)
    if out.suffix.lower() != ".pdf":
        out = out.with_suffix(".pdf")
    out.parent.mkdir(parents=True, exist_ok=True)

    for w in check(spec):
        print(f"WARNING: {w}", file=sys.stderr)
    ensure("reportlab", "reportlab")
    pages = Doc(out, spec, a.page, logo).build()
    print(f"PDF created: {out} ({pages} pages, fillable)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
