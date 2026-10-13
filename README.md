# tech-business-skills

**Your translator between engineering and business.**

Claude Skills that help tech leads — especially new ones — turn incidents, metrics, tech debt and projects into reports leadership acts on: every item flagged as highlight, lowlight or risk, every risk with a clear ask, and every claim backed by a number. No made-up numbers.

---

## Why this exists

People get promoted for being great engineers. Then nobody teaches them to talk to finance, defend a budget, or explain why a refactor matters.

The result is reports like *"migrated service X, fixed 14 bugs, attended 6 meetings"* — true, busy, and meaningless to the people who decide priorities and money.

These skills don't just write the report for you. They **ask the questions a senior leader would ask** — *"What changed after that shipped? For whom? What would it have cost not to do it?"* — so you learn to translate your own work.

## What's inside

| Skill | What it does |
|---|---|
| [`tech-to-business-report`](tech-to-business-report/) | Turns technical work (a week, a month, a project, an incident) into a one-page report: each item labeled HIGHLIGHT / LOWLIGHT / RISK, told in STAR form, translated to business impact, and tracked against SMART goals. |

More skills will be added one at a time, each in its own folder.

## How it works

**1. Every item gets one of three labels.**

| Label | Meaning |
|---|---|
| **[H] HIGHLIGHT** | Something good already happened, with a measurable result |
| **[L] LOWLIGHT** | Something bad already happened: cause, impact, what you learned |
| **[R] RISK: Low / Medium / High** | Something could happen (or an opportunity could be lost) — always with an **ASK** |

If it's not one of the three, it doesn't go in the report. No "FYI" padding.

**2. Every item climbs the translation ladder.**

```
Output           →  Outcome                 →  Business impact
what I did          what changed               money, customers, risk, speed
"fixed 14 bugs"     "search tickets −62%"      "≈ 0.5 support FTE freed"
```

**3. The assistant knows your role.** It uses role cards (based on the role-based roadmaps of [roadmap.sh](https://roadmap.sh/roadmaps), plus SRE and Tech Lead) to ask the right questions: features and bugs for developers, exposure windows for security, audience reach and adoption for developer relations, and so on.

**4. It never invents numbers.** Missing data shows up as `[MISSING: what — where to get it]`, and the report is marked as a draft until you fill it in.

---

## Install

### Claude on the web or the desktop app (no code)

1. Open **[Customize → Plugins](https://claude.ai/customize/plugins)**.
2. Click **Add → Add marketplace** and paste:
   ```
   MaisfloroTech/tech-business-skills
   ```
3. Find **Tech Business Skills** in the list and click **Add**.

Done. It updates on its own when new skills are published, and it's also available in Claude Code if you sign in with the same account.

### Claude Code (one command)

Inside a Claude Code session:

```
/plugin install tech-business-skills --marketplace MaisfloroTech/tech-business-skills
```

Or from your terminal:

```bash
claude plugin install tech-business-skills --marketplace MaisfloroTech/tech-business-skills
```

Works in the terminal and in the **Code** tab of the desktop app. Needs a recent Claude Code version; if the command isn't recognized, run `claude update` first.

> **Even easier:** just tell Claude Code *"install the plugin tech-business-skills from the marketplace MaisfloroTech/tech-business-skills"* and it runs the command for you.

<details>
<summary><b>Other ways to install</b> (if the options above don't work for you)</summary>

**Upload the skill as a zip (web or desktop)**

1. Download `tech-to-business-report.zip` from the [latest release](../../releases/latest). Don't unzip it.
2. In Claude, go to **Customize → Skills**, choose **Upload skill** and select the zip.

You need to repeat this for every update.

**Copy the skill folder (Claude Code)**

```bash
git clone https://github.com/MaisfloroTech/tech-business-skills.git
mkdir -p ~/.claude/skills
cp -r tech-business-skills/tech-to-business-report ~/.claude/skills/
```

</details>

**Requirements:** a paid Claude plan (Pro, Max, Team or Enterprise). On Team and Enterprise plans an admin may need to allow adding marketplaces, and can also install the plugin for the whole organization so everyone reports with the same standard.

## Use it

Start a new chat and write something like:

> *Help me write my report for this week. I'm a backend developer and it goes to my director.*

Then paste your notes, ticket titles or numbers — messy is fine. Claude asks you for your role, the audience and whatever is missing, and gives you the one-pager back.

You don't need to name the skill: asking for a report, a status update or "how do I explain this to the business" is enough. To call it explicitly, type `/` and pick **tech-to-business-report** (in Claude Code: `/tech-business-skills:tech-to-business-report`).

**Languages.** The skill answers in the language you write in. Write in Spanish and you get the questions and the report in Spanish; write in English and you get English. You can also mix: *"talk to me in Spanish but write the report in English"*. Labels (HIGHLIGHT, LOWLIGHT, RISK) stay in English by default because they are a shared vocabulary; ask if you want them translated.

> **¿Hablas español?** Instálalo igual que arriba y escríbele en español, por ejemplo: *"Ayúdame con mi reporte de este mes. Soy desarrolladora backend y va para mi directora."* Te va a hacer las preguntas y entregar el reporte en español.

If it helped you, [give the repo a star](https://github.com/MaisfloroTech/tech-business-skills) — it's how we know people are using it.

## For teams and companies

Use this repo as a **template** to create your own private copy, then:

- Add your own examples (with your real metrics) to `references/example.md`.
- Adjust the goal thresholds or labels to match how your leadership already reports.
- Distribute the zip to your team, or install it workspace-wide on Team/Enterprise plans.

Keep real company data in your private copy only.

---

## Repository structure

One folder per skill. Each folder is self-contained, so it can be zipped and uploaded as is.

```
tech-business-skills/
├── tech-to-business-report/
│   ├── SKILL.md                    # what the skill does and the step-by-step method
│   └── references/
│       ├── labels.md               # HIGHLIGHT / LOWLIGHT / RISK and severity
│       ├── translation-ladder.md   # output → outcome → business impact
│       ├── honesty-rules.md        # no invented numbers, [MISSING: ...]
│       ├── roles/                  # role cards, grouped in 8 families
│       ├── template.md             # the one-pager format
│       └── example.md              # a full worked example (fictional data)
├── .claude-plugin/                 # makes the repo installable as a plugin (one line to add each new skill)
├── .github/                        # CI, release automation and the build script
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

The method files (`labels.md`, `translation-ladder.md`, `honesty-rules.md`, `roles/`) are shared: every skill carries an identical copy. CI checks that they never drift apart.

## Roadmap

Next skills will follow the same method, one folder each. Ideas under consideration:

- Business case for technical debt
- Incident postmortem for leadership
- Translating a technical metric into business impact
- Budget and headcount justification

The method isn't limited to engineering. Role cards for other functions can be added over time.

Have a role or a skill you need? [Open an issue](../../issues).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The most valuable contributions are **role cards** and **before/after examples** with fictional data.

## License

[MIT](LICENSE)
