#!/usr/bin/env python3
"""Validate, sync and package the skills in this repo.

Every top-level folder that contains a SKILL.md is a skill.

Usage:
  python .github/scripts/skills.py validate          # checks used by CI
  python .github/scripts/skills.py build             # zips each skill into dist/<name>.zip
  python .github/scripts/skills.py sync --from NAME  # copy the shared method files from one skill to all others
"""
from __future__ import annotations

import argparse
import filecmp
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"

# Files every skill carries so it stays self-contained. Edit them in one skill,
# then run `sync --from <that-skill>` to propagate.
SHARED = [
    "references/labels.md",
    "references/translation-ladder.md",
    "references/honesty-rules.md",
    "references/business-language.md",
    "references/roles",
]

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
BLOCKED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic", ".heif", ".bmp", ".tiff"}
IGNORED_DIRS = {".git", "dist", "node_modules", "__pycache__"}


def skills() -> list[Path]:
    return sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name not in IGNORED_DIRS and (p / "SKILL.md").exists()
    )


def frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter delimited by '---'")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def shared_files(skill: Path) -> list[Path]:
    files: list[Path] = []
    for rel in SHARED:
        path = skill / rel
        if path.is_dir():
            files += sorted(f.relative_to(skill) for f in path.rglob("*") if f.is_file())
        else:
            files.append(Path(rel))
    return files


def validate() -> int:
    errors: list[str] = []
    found = skills()
    if not found:
        errors.append("no skills found (a skill is a top-level folder with a SKILL.md)")

    names: set[str] = set()
    for skill in found:
        where = skill.name
        try:
            meta = frontmatter(skill / "SKILL.md")
        except ValueError as exc:
            errors.append(f"{where}: {exc}")
            continue

        name = meta.get("name", "")
        description = meta.get("description", "")
        if not name:
            errors.append(f"{where}: frontmatter has no 'name'")
        elif name != skill.name:
            errors.append(f"{where}: name '{name}' must match the folder name")
        elif not NAME_RE.match(name) or len(name) > MAX_NAME:
            errors.append(f"{where}: name must be lowercase letters, numbers and hyphens, max {MAX_NAME} chars")
        if name in names:
            errors.append(f"{where}: duplicate skill name '{name}'")
        names.add(name)

        if not description:
            errors.append(f"{where}: frontmatter has no 'description'")
        elif len(description) > MAX_DESCRIPTION:
            errors.append(f"{where}: description is {len(description)} chars, max {MAX_DESCRIPTION}")
        elif "<" in description or ">" in description:
            errors.append(f"{where}: description must not contain angle brackets")

        body = (skill / "SKILL.md").read_text(encoding="utf-8")
        for ref in sorted(set(re.findall(r"`(references/[^`\s]+)`", body))):
            if not (skill / ref).exists():
                errors.append(f"{where}: SKILL.md points to {ref}, which does not exist")

        for rel in SHARED:
            if not (skill / rel).exists():
                errors.append(f"{where}: missing shared file {rel} (run sync)")

    # Shared method files must be identical in every skill.
    if len(found) > 1:
        base = found[0]
        for other in found[1:]:
            for rel in set(shared_files(base)) | set(shared_files(other)):
                a, b = base / rel, other / rel
                if not a.exists() or not b.exists() or not filecmp.cmp(a, b, shallow=False):
                    errors.append(f"{rel} differs between {base.name} and {other.name} (run sync)")

    # Every skill must be listed in the plugin manifest so plugin installs pick it up.
    manifest = ROOT / ".claude-plugin" / "plugin.json"
    if manifest.exists():
        listed = json.loads(manifest.read_text(encoding="utf-8")).get("skills", [])
        listed = {str(Path(x)).strip("./") for x in ([listed] if isinstance(listed, str) else listed)}
        for skill in found:
            if skill.name not in listed:
                errors.append(f"{skill.name}: not listed in .claude-plugin/plugin.json \"skills\"")
    else:
        errors.append(".claude-plugin/plugin.json is missing")

    # No images anywhere in the repo, so nothing private gets committed by accident.
    for path in ROOT.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file() and path.suffix.lower() in BLOCKED_EXTENSIONS:
            errors.append(f"{path.relative_to(ROOT)}: images are not allowed in this repo")

    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print(f"OK: {len(found)} skill(s) valid: {', '.join(s.name for s in found)}")
    return 1 if errors else 0


def build() -> int:
    if validate():
        return 1
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for skill in skills():
        target = DIST / f"{skill.name}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
            for file in sorted(skill.rglob("*")):
                if file.is_file() and not file.name.startswith("."):
                    zf.write(file, Path(skill.name) / file.relative_to(skill))
        print(f"built {target.relative_to(ROOT)}")
    return 0


def sync(source_name: str) -> int:
    source = ROOT / source_name
    if source not in skills():
        print(f"ERROR: '{source_name}' is not a skill folder")
        return 1
    for skill in skills():
        if skill == source:
            continue
        for rel in SHARED:
            src, dst = source / rel, skill / rel
            if dst.exists():
                shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst) if src.is_dir() else shutil.copy2(src, dst)
        print(f"synced shared files {source.name} -> {skill.name}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("build")
    sync_parser = sub.add_parser("sync")
    sync_parser.add_argument("--from", dest="source", required=True)
    args = parser.parse_args()
    if args.command == "validate":
        return validate()
    if args.command == "build":
        return build()
    return sync(args.source)


if __name__ == "__main__":
    sys.exit(main())
