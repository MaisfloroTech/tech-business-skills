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
4. Propagate the change to every skill and check it:

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

3. Copy the shared method files into it:

   ```bash
   python .github/scripts/skills.py sync --from tech-to-business-short-report
   ```

4. Write the skill's method and a short example in its `SKILL.md`. Keep it short: people want results, not interviews. Every skill **asks for the role first** ("I'm a…" / "My role is…") and uses the role cards, and every example input starts with the role.
5. Add the folder to the `skills` list in `.claude-plugin/plugin.json`, so people who installed the plugin get it automatically:

   ```json
   "skills": ["./tech-to-business-short-report", "./my-new-skill"]
   ```

6. Run `python .github/scripts/skills.py build` (CI runs the same check) and `claude plugin validate .`, then test it in Claude before opening a PR.
7. In `README.md`, mark it ✅ Available in **The skills** table and add its own big section (`# <emoji> Skill N · <Name>`) after the previous skill, following the same layout: what it does, an example, how to use it.

## Releases (maintainers)

Push a version tag and GitHub Actions publishes a release with one zip per skill:

```bash
git tag v1.0.0
git push origin v1.0.0
```
