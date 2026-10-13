<div align="center">

# 🌉 tech-business-skills

### Your translator between engineering and business

Claude Skills that help tech leads turn incidents, metrics, tech debt and projects<br>into reports leadership actually reads, and acts on.

**🟢 Highlights · 🔴 Lowlights · 🟠 Risks · 📏 SMART goals · 🚫 No made-up numbers**

[⚡ Install in 1 minute](#-install-in-1-minute) · [👀 See an example](#-what-a-report-looks-like) · [🇪🇸 Español](#-hablas-español)

</div>

---

## 😩 The problem

You got promoted because you're great at the technical stuff. Then one day your director asks for "a quick update for the leadership meeting", and you write this:

> *Migrated three services to the new cluster. Fixed 14 bugs. Implemented alerting for payments. Attended the architecture review. Worked on performance.*

Everything is true. You worked hard. And the people reading it have **no idea why any of it matters.**

Meanwhile, they're asking themselves:

- 💸 *Did this make us money, or save us money?*
- 👥 *Did customers notice?*
- 🔥 *Is anything about to break?*
- 🙋 *Do they need something from me?*

Nobody teaches technical people to answer those questions. Big companies have whole rituals for it (weekly business reviews, highlights and lowlights, one-pagers). New leaders usually learn it the hard way: in a meeting where the CFO asks *"so what?"* and there's no good answer.

**This repo is the shortcut.**

## 💡 What it does

It's not a template you fill in. It's a coach that **asks you the questions a senior leader would ask**, until your work speaks business.

```
You:     "I fixed 14 bugs in search."
Claude:  "Nice. How many support tickets about search came in before and after?"
You:     "Around 120 a month before, 45 now."
Claude:  "That's 75 fewer tickets a month. Do you know the average cost of handling one?"
You:     "No idea."
Claude:  "I'll mark it as [MISSING: cost per ticket — ask Support Ops]
          so it doesn't look invented. Want to keep going?"
```

Then it gives you a **one-page report** a busy executive can read in two minutes.

## 🪜 From "what I did" to "why it matters"

Every item climbs the same ladder:

| | 🔧 Output<br>*what I did* | 📈 Outcome<br>*what changed* | 💼 Business impact<br>*why anyone cares* |
|---|---|---|---|
| **👩‍💻 Developer** | Shipped search filters, fixed 14 bugs | 38% of searches use filters; search tickets 120 → 45/month | ~75 fewer tickets/month ≈ half a support person freed |
| **🎤 Developer Relations** | Gave 12 talks and 4 workshops | 340 sign-ups from the target audience, 60 active accounts | New active users at a fraction of paid acquisition cost |
| **🛡️ Cyber Security** | Closed 300 vulnerabilities | Critical exposure window down from 45 to 9 days | Audit passed with zero critical findings; enterprise deal unblocked |
| **⚙️ SRE / DevOps** | Rightsized cloud resources, added alerting | Monthly bill USD 41k → 34.5k; payment errors detected in 4 min (was 20) | ≈ USD 78k/year saved; issues caught before customers notice |
| **📊 Data Engineer** | Migrated 20 pipelines | Data freshness from 24h to 1h; zero failed loads this month | Sales sees yesterday's numbers this morning, not tomorrow |

*All figures in this README are fictional examples.*

The skill knows **31+ roles** (based on the role-based roadmaps of [roadmap.sh](https://roadmap.sh/roadmaps), plus SRE and Tech Lead), so it asks the *right* questions for yours. Not in the list? It asks you three things and figures it out:

1. What do you produce?
2. Who uses it?
3. **What breaks, and for whom, if you stop doing it for a month?** ← that's usually your business impact

## 🏷️ Only three labels

Every item gets exactly one. If it isn't one of these, it doesn't go in the report. No "FYI" padding.

| | Label | Meaning | Must include |
|---|---|---|---|
| 🟢 | **HIGHLIGHT** | Something good **already happened** | A measurable result |
| 🔴 | **LOWLIGHT** | Something bad **already happened** | Cause, impact, what you learned |
| 🟠 | **RISK** Low · Medium · High | Something **could happen**, or an opportunity could be lost | Probability, impact, mitigation and an **ASK** |

💬 *Need budget, people or a decision?* Write it as a risk: what happens if you **don't** get it, and what you need from the reader, by when.

## 👀 What a report looks like

```markdown
# Payments Platform — Weekly report — Week of Oct 5
Overall status: RISK: High

## Need to know

[R-High] Black Friday capacity (Platform, highest-revenue day of the year):
Last year's peak was 3x normal traffic; we have never tested above 2x.
Probability of degradation: high without a test. Mitigation: test plan ready.
ACTION: run 3x load test — Platform, by Oct 30.
ASK: approve a temporary performance environment by Oct 16.

[L] Checkout outage, Tuesday (Platform, ~1,100 failed checkouts):
25 min of failed checkouts after DB connections maxed out during a release.
Rolled back. Revenue impact: [MISSING: revenue per minute — ask Finance].
Learned: connection limits are now checked in the release pipeline.

[H] Cloud cost down USD 6.5k/month (Platform, infrastructure budget):
Rightsizing cut the bill from USD 41k to 34.5k (−16%), permanent.
≈ USD 78k/year at current usage.

## Goal tracking
| Goal (SMART)                          | Target | Expected | Actual | Status    |
|---------------------------------------|--------|----------|--------|-----------|
| Checkout availability ≥ 99.9% in Q4   | 99.9%  | 99.9%    | 99.82% | Off track |
| Cut cloud cost by USD 8k/month in Q4  | 8,000  | 2,700    | 6,500  | On track  |
```

Short. Labeled. Every claim has a number, or an honest `[MISSING]`.
👉 Full worked example: [`references/example.md`](tech-to-business-report/references/example.md)

## ⚡ Install in 1 minute

### 💻 Claude on the web or the desktop app (no code)

1. Open **[Customize → Plugins](https://claude.ai/customize/plugins)**.
2. Click **Add → Add marketplace** and paste:
   ```
   MaisfloroTech/tech-business-skills
   ```
3. Find **Tech Business Skills** and click **Add**. ✅

It updates on its own when new skills are published, and it also shows up in Claude Code if you use the same account.

### ⌨️ Claude Code (one command)

```
/plugin install tech-business-skills --marketplace MaisfloroTech/tech-business-skills
```

Or just tell Claude Code: *"install the plugin tech-business-skills from the marketplace MaisfloroTech/tech-business-skills"*. If the command isn't recognized, run `claude update` first.

<details>
<summary>🧰 <b>Other ways to install</b></summary>

**Upload the skill as a zip (web or desktop)**

1. Download `tech-to-business-report.zip` from the [latest release](../../releases/latest). Don't unzip it.
2. In Claude, go to **Customize → Skills**, choose **Upload skill** and select the zip.

You'll need to repeat this for every update.

**Copy the folder (Claude Code)**

```bash
git clone https://github.com/MaisfloroTech/tech-business-skills.git
mkdir -p ~/.claude/skills
cp -r tech-business-skills/tech-to-business-report ~/.claude/skills/
```

</details>

> 📝 You need a paid Claude plan (Pro, Max, Team or Enterprise). On Team and Enterprise, an admin may need to allow adding marketplaces, and can install it for the whole organization so everyone reports with the same standard.

## 🚀 Use it

Start a new chat and say something like:

> *"Help me write my report for this month. I'm a backend developer and it goes to my director."*

Then paste whatever you have: notes, ticket titles, numbers, a CSV. **Messy is fine.** Claude asks for what's missing and hands you the one-pager.

You don't need to name the skill. To call it explicitly, type `/` and pick **tech-to-business-report** (in Claude Code: `/tech-business-skills:tech-to-business-report`).

Works for a week, a month, a quarter, a project or a single incident.

## 🇪🇸 ¿Hablas español?

Instálalo igual que arriba y escríbele en español:

> *"Ayúdame con mi reporte de este mes. Soy desarrolladora backend y va para mi directora."*

Te hace las preguntas y te entrega el reporte en español. También puedes mezclar: *"háblame en español pero el reporte en inglés para mi jefe global"*. Las etiquetas (HIGHLIGHT, LOWLIGHT, RISK) quedan en inglés por defecto porque son vocabulario común entre equipos; si las quieres traducidas, pídelo.

The skill answers in whatever language you write in.

## 🛡️ The honesty promise

This skill makes technical work *sound* like business. That's exactly why it has rules:

- 🚫 **It never invents numbers.** No "industry averages", no plausible guesses.
- 🕳️ **Gaps stay visible** as `[MISSING: what — where to get it]`, and the report is marked **DRAFT** until you fill them.
- 🧮 **It shows its math** for anything calculated.
- 📉 **Bad news stays the size it was.** No turning lowlights into highlights.

A report with an honest gap is better than a polished one that falls apart at the first question.

## 🏢 For teams and companies

Click **Use this template** to create your own private copy, then:

- Add examples with your real metrics (in your private copy only).
- Tune labels and goal thresholds to how your leadership already reports.
- Install it for the whole organization from Claude's admin settings.

## 🗺️ What's next

One skill today, more on the way, each in its own folder:

- [x] 📄 **Tech-to-business report**: the one-pager
- [ ] 🧱 Business case for technical debt
- [ ] 🚨 Incident postmortem for leadership
- [ ] 💰 Budget and headcount justification
- [ ] 🔢 Translate any technical metric into business impact

Need a role or a skill that isn't here? [Open an issue](../../issues) 💬

## 🤝 Contributing

The most valuable contributions are **role cards** and **before/after examples** (fictional data only). See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📁 What's inside

```
tech-business-skills/
├── tech-to-business-report/      ← one folder per skill
│   ├── SKILL.md                  the method, step by step
│   └── references/
│       ├── labels.md             HIGHLIGHT / LOWLIGHT / RISK
│       ├── translation-ladder.md output → outcome → impact
│       ├── honesty-rules.md      no invented numbers
│       ├── roles/                role cards in 8 families
│       ├── template.md           the one-pager format
│       └── example.md            a full worked example
├── .claude-plugin/               makes it installable in one step
└── .github/                      CI and releases
```

---

<div align="center">

⭐ **If this helped you sound more like business and less like a changelog, give it a star.**<br>
It's how we know it's reaching the people who need it.

Made with ☕ by [MaisfloroTech](https://github.com/MaisfloroTech) · [MIT License](LICENSE)

</div>
