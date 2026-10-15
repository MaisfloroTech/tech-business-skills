# Contributing

Thanks for helping technical people speak business.

## Ground rules

- **Fictional data only.** No real company, customer, person or figure in examples. No screenshots or images (CI rejects them).
- **No invented "industry averages".** If a skill needs a number, it asks the user for it.
- **Short beats complete.** These skills exist to make reports shorter and sharper; the files should be too.
- Write in English. Skills already talk to users in their own language.

## Add or improve a role card

Role cards live in `<skill>/references/roles/`. Each role belongs to one family file.

1. Edit the family file in **one** skill folder (for example `tech-to-business-short-report/references/roles/security.md`).
2. Follow the card format in `roles/README.md`: Produces / Serves / If it stops, the ladder, typical risks, red flag.
3. Write definitions in your own words; link to roadmap.sh instead of copying it.
4. Propagate the change to the other skills that use role cards (the short report and the SMART objectives) and check it:

```bash
python .github/scripts/skills.py sync --from tech-to-business-short-report
python .github/scripts/skills.py validate
```

## Add a new skill

Every skill follows the same structure. Use this checklist and copy from the existing skills; don't invent a new layout.

### 1. The skill itself

- [ ] **Folder** at the top level, named `tech-to-business-<what-it-makes>` in `kebab-case`.
- [ ] **`SKILL.md`** with frontmatter:

  ```yaml
  ---
  name: tech-to-business-<what-it-makes>   # must match the folder name
  description: What it does AND when Claude should use it, ending with "Works best when the user starts with their role ("I'm a…" / "Soy…"). Never invents …" (max 1024 characters, no angle brackets).
  ---
  ```

- [ ] **Same sections as the others:** a one-paragraph intro and a bold one-liner (*"One X, one Y, done well."*), `## Language`, `## Flow` (1. ask once · 2. write · 3. deliver), rules, and examples in English and Spanish.
- [ ] **The role comes first.** If the message doesn't start with "I'm a…" / "Soy…", the one question round opens with the role, and the answer ends with the tip to start with it next time.
- [ ] **One round of questions, at most.** If the user gave enough, answer right away.
- [ ] **Nothing invented.** Anything missing becomes an UPPERCASE placeholder in the user's language (`ENTER_DATE` / `INGRESA_FECHA`).
- [ ] **Language:** answers in the language the user writes in; English and Spanish are first-class.
- [ ] **One input, one output.** If the user brings several, do the most important and offer the next.
- [ ] **Method files:** if it translates work into business impact (like the report and the objectives), add it to `SHARED_SKILLS` in `.github/scripts/skills.py` and run `python .github/scripts/skills.py sync --from tech-to-business-short-report`. Otherwise give it its own `references/` (like the FAQ). The traffic-light labels belong only to the short report.
- [ ] **Files it builds** (Word, etc.) come from a script in `scripts/`, carry the Build to Lead branding and work from the extracted zip.

### 2. Its README (for people, not for Claude)

- [ ] **`README.md` inside the skill folder**, same layout as the other three:
  1. `[← All skills · Todos los skills](../README.md)` and the language switch: **[🇺🇸 English 🇬🇧](#english)** · **[🇪🇸 Español 🌎](#espanol)**
  2. `<a id="english"></a>`, `# 🇺🇸 English 🇬🇧`, the English banner, `## <emoji> Skill N · <Name>`, the skill id, a one-line *in → out*, and "Not installed yet? Install in 1 minute" (`../README.md#install-en`).
  3. What it does (emoji bullets), examples by role (extra ones in `<details>`), and **🚀 Use it**, starting with the role.
  4. `<a id="espanol"></a>`, `# 🇪🇸 Español 🌎`, the line of Spanish-speaking LATAM flags, the Spanish banner and **the same content fully in Spanish**, examples included (inputs and outputs), with `Responsable:` and `INGRESA_…` placeholders. Link to `../README.md#install-es`.
- [ ] **Each language shows only its own examples and files.**
- [ ] **Banners:** add the skill to `JOBS` in `.github/banner/skills.py` (English and Spanish texts: left = the painful "before", right = the result, footer = `Skill N · <Name>` + one line), run `python3 .github/banner/skills.py`, look at both images, and add `.github/assets/skill-N-en.png` and `skill-N-es.png` to `ALLOWED_IMAGES` and `.gitignore`.

### 3. Wire it into the repo

- [ ] Add the folder to `skills` in `.claude-plugin/plugin.json`, and mention it in the plugin description in `.claude-plugin/marketplace.json`.
- [ ] Add its **card in "Pick a skill"** in the main `README.md`, in **both** the English and Spanish sections (title, one line, when to use it, "See it in action →" / "Míralo en acción →"). Keep the main README short.
- [ ] Update the tree in **What's inside** below.

### 4. Check before publishing

- [ ] `python .github/scripts/skills.py build` and `claude plugin validate .` pass.
- [ ] The skill works from its extracted zip, and a clean install works:
  `claude plugin marketplace add MaisfloroTech/tech-business-skills` then `claude plugin install tech-business-skills@tech-business-skills`.
- [ ] Test it in Claude with one English and one Spanish message that start with the role, and one that doesn't.
- [ ] Fictional data only, in examples and banners.

## What's inside

```
tech-business-skills/
├── README.md                           short landing page: install, role, language
├── tech-to-business-short-report/      📄 Skill 1 (one folder per skill)
│   ├── README.md                       docs and examples for people (not loaded by Claude)
│   ├── SKILL.md                        the method Claude follows
│   └── references/
│       ├── labels.md                   HIGHLIGHT / LOWLIGHT / RISK (this skill only)
│       ├── translation-ladder.md       output → outcome → impact
│       ├── honesty-rules.md            no invented numbers or facts
│       ├── business-language.md        technical → business titles and words
│       └── roles/                      role cards in 8 families
├── tech-to-business-smart-objectives/  🎯 Skill 2: same shared files as Skill 1, no labels
├── tech-to-business-faq-one-pager/     📘 Skill 3
│   ├── scripts/build_faq.py            builds the branded one-page Word document
│   ├── assets/                         Build to Lead logo
│   ├── examples/                       example FAQs in Spanish and English
│   └── references/                     its own: plain language, honesty rules, diagram example
├── .claude-plugin/                     makes the repo installable in one step
└── .github/                            CI, releases and README assets
```

## Releases (maintainers)

Push a version tag and GitHub Actions publishes a release with one zip per skill:

```bash
git tag v1.0.0
git push origin v1.0.0
```

## Images

Images are blocked by CI so nothing private gets committed by accident. The only exceptions are listed by exact path in `ALLOWED_IMAGES` in `.github/scripts/skills.py` (and in `.gitignore`): the Build to Lead logo, the README previews of the example FAQ documents (fictional data) and the README banners. The main banner is built from `.github/banner/banner.html` (`python3 .github/banner/render.py`); the six skill banners (English and Spanish) from `.github/banner/skills.py` (`python3 .github/banner/skills.py`). Both need Playwright. Adding a new image means adding its exact path to both lists, on purpose.
