#!/usr/bin/env python3
"""Build the Build to Lead FAQ one-pager as an editable Word document (.docx).

Usage:
  python build_faq.py faq.json OUTPUT.docx [--page a4|letter] [--logo my-logo.png]

Examples:
  python build_faq.py faq.json /mnt/user-data/outputs/faq-data-portal.docx
  python build_faq.py faq.json faq-deploy.docx --page letter --logo company-logo.png
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ensure(module: str, package: str) -> None:
    try:
        __import__(module)
    except ImportError:
        print(f"Installing {package}...", file=sys.stderr)
        cmd = [sys.executable, "-m", "pip", "install", "--quiet", package]
        if subprocess.run(cmd).returncode != 0:
            subprocess.run(cmd + ["--break-system-packages"], check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", help="FAQ JSON file")
    ap.add_argument("output", help="output .docx path")
    ap.add_argument("--page", choices=["a4", "letter"], default="a4")
    ap.add_argument("--logo", help="PNG/JPG to replace the Build to Lead logo")
    a = ap.parse_args()

    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    out = Path(a.output)
    if out.suffix.lower() != ".docx":
        out = out.with_suffix(".docx")
    out.parent.mkdir(parents=True, exist_ok=True)

    ensure("docx", "python-docx")
    sys.path.insert(0, str(HERE))
    import build_faq_docx
    build_faq_docx.build_fitted(spec, out, a.page, a.logo)
    print(f"Word document created: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
