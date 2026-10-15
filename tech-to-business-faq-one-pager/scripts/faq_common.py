"""Shared brand, labels and helpers for the Build to Lead FAQ one-pager."""
from __future__ import annotations

import re
from pathlib import Path

# Build to Lead brand colors (hex, no '#')
BRAND = {
    "navy": "171A30",
    "teal": "204B4C",
    "terracotta": "A97F6A",
    "gray": "4E4F52",
    "teal_tint": "E6EEEE",
    "terra_tint": "F4ECE8",
    "rule": "D5DADA",
    "placeholder_bg": "F2D9CC",
    "placeholder_fg": "7A4A35",
}

DEFAULT_LOGO = Path(__file__).resolve().parent.parent / "assets" / "build-to-lead-logo.png"
LOGO_MAX_H = 70   # points
LOGO_MAX_W = 150  # points

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


def labels(spec: dict) -> dict:
    return LABELS.get(str(spec.get("language", "en")).lower()[:2], LABELS["en"])


def resolve_logo(logo: str | None) -> Path:
    """Return the logo to use: a custom one if given and valid, otherwise Build to Lead's."""
    if logo:
        p = Path(logo).expanduser()
        if not p.is_file():
            raise SystemExit(f"ERROR: logo not found: {p}")
        if p.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            raise SystemExit("ERROR: the logo must be a PNG or JPG file (convert SVG or other formats first).")
        return p
    return DEFAULT_LOGO


def logo_box(width_px: int, height_px: int) -> tuple[float, float]:
    """Fit any logo into the corner box, keeping its proportions."""
    scale = min(LOGO_MAX_H / height_px, LOGO_MAX_W / width_px)
    return width_px * scale, height_px * scale


W_TAGS = ("what", "why", "who", "when", "where", "how", "limits", "help")
SENTENCE_RE = re.compile(r"[.!?](?:\s|$)")


def check_spec(spec: dict) -> list[str]:
    """Content checks that don't need LibreOffice: catch a page that will run long or miss a W."""
    warnings = []
    faqs = spec.get("faqs", [])
    if not 6 <= len(faqs) <= 10:
        warnings.append(f"{len(faqs)} questions; use 6-10.")
    missing = [w for w in W_TAGS[:6] if w not in {f.get("w") for f in faqs}]
    if missing:
        warnings.append(f"no question tagged: {', '.join(missing)}.")
    for i, f in enumerate(faqs, 1):
        n = len(SENTENCE_RE.findall(str(f.get("a", "")).strip() + " "))
        if n > 3:
            warnings.append(f"answer {i} has {n} sentences; keep it to 1-3.")
    if len(spec.get("at_a_glance", [])) != 4:
        warnings.append("'at_a_glance' needs exactly 4 facts.")
    for key in ("can", "cannot"):
        if len(spec.get(key, [])) > 5:
            warnings.append(f"'{key}' has more than 5 items.")
    if not spec.get("help"):
        warnings.append("the help block is empty.")
    return warnings


def split_placeholders(text: str):
    """Yield (chunk, is_placeholder) pieces of text."""
    pos = 0
    for m in PLACEHOLDER_RE.finditer(text):
        if m.start() > pos:
            yield text[pos:m.start()], False
        yield m.group(0), True
        pos = m.end()
    if pos < len(text):
        yield text[pos:], False
