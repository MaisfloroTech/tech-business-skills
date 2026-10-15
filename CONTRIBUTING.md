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

1. Create a top-level folder named in `kebab-case` (lowercase, hyphens), e.g. `my-new-skill/`.
2. Add a `SKILL.md` with frontmatter:

   ```yaml
   ---
   name: my-new-skill     # must match the folder name
   description: What it does AND when Claude should use it (max 1024 characters, no angle brackets).
   ---
   ```

3. Decide what method it needs. If it translates work into business impact (like the report and the objectives), add it to `SHARED_SKILLS` in `.github/scripts/skills.py` and copy the shared files into it:

   ```bash
   python .github/scripts/skills.py sync --from tech-to-business-short-report
   ```

   If it does something different (like the FAQ one-pager), give it its own `references/` and leave it out of `SHARED_SKILLS`. Don't copy the traffic-light labels into a skill that doesn't write reports.

4. Write the skill's method and a short example in its `SKILL.md`. Keep it short: people want results, not interviews. Every skill **asks for the role first** ("I'm a…" / "My role is…"), and every example input starts with the role.
5. Add the folder to the `skills` list in `.claude-plugin/plugin.json`, so people who installed the plugin get it automatically:

   ```json
   "skills": ["./tech-to-business-short-report", "./my-new-skill"]
   ```

6. Run `python .github/scripts/skills.py build` (CI runs the same check) and `claude plugin validate .`, then test it in Claude before opening a PR.
7. Add a `README.md` inside the skill folder (what it does, examples, how to use it; copy the layout of the existing ones) and a card for it in **Pick a skill** in the main `README.md`. Keep the main README short: details live in each skill's README.

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

Images are blocked by CI so nothing private gets committed by accident. The only exceptions are listed by exact path in `ALLOWED_IMAGES` in `.github/scripts/skills.py` (and in `.gitignore`): the Build to Lead logo and the README previews of the example FAQ documents, which use fictional data. Adding a new image means adding its exact path to both lists, on purpose.
