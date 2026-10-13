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

Pick the place where you use Claude. You install it once; after that Claude uses it automatically whenever you ask for a report.

| You use Claude in... | Difficulty | Go to |
|---|---|---|
| The browser (claude.ai) | Easy, no code | [Claude on the web](#claude-on-the-web) |
| The desktop app (Mac / Windows) | Easy, no code | [Claude Desktop](#claude-desktop) |
| The terminal | Technical | [Claude Code](#claude-code) |

> **Before you start:** skills need a paid Claude plan (Pro, Max, Team or Enterprise). Skills you upload are private to your account, and they don't sync between web/desktop and Claude Code — install it in each place you use.

### Claude on the web

1. Open the [**latest release**](../../releases/latest) of this repo.
2. Under **Assets**, click **`tech-to-business-report.zip`** to download it. **Don't unzip it.**
3. Go to [claude.ai](https://claude.ai) and open the section where your **skills** are managed (in settings or the customize menu).
4. Choose **Upload skill** and select the zip you downloaded.
5. Make sure the skill is switched **on**.

Can't find skills or the upload button? Your account may need skills or code execution turned on first. Menus change between versions, so check [Anthropic's Help Center](https://support.claude.com) and search for "skills".

### Claude Desktop

Same steps as the web, inside the app:

1. Download **`tech-to-business-report.zip`** from the [**latest release**](../../releases/latest). **Don't unzip it.**
2. Open the Claude desktop app and go to the section where your **skills** are managed.
3. Choose **Upload skill**, select the zip and make sure it's switched **on**.

### Claude Code

```bash
# 1. Download the repo
git clone https://github.com/MaisfloroTech/tech-business-skills.git

# 2. Install the skill for all your projects
mkdir -p ~/.claude/skills
cp -r tech-business-skills/tech-to-business-report ~/.claude/skills/

#    ...or only for one project
mkdir -p <your-project>/.claude/skills
cp -r tech-business-skills/tech-to-business-report <your-project>/.claude/skills/
```

Restart Claude Code. Type `/skills` to check it's listed, or call it directly with `/tech-to-business-report`.

In Claude Code the skill can read files, so you can point it at your data:

> *Write my monthly report from `metrics/october.csv` and the incidents in `postmortems/`.*

### Updating

- **Web / Desktop:** download the new zip from the latest release and upload it again, replacing the old one.
- **Claude Code:** `cd tech-business-skills && git pull`, then copy the folder again.

## Use it

Start a new chat and write something like:

> *Help me write my report for this week. I'm a backend developer and it goes to my director.*

Then paste your notes, ticket titles or numbers — messy is fine. Claude asks you for your role, the audience and whatever is missing, and gives you the one-pager back.

You don't need to name the skill: asking for a report, a status update or "how do I explain this to the business" is enough.

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
