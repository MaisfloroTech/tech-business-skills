<div align="center">

# 🌉 tech-business-skills

### Your translator between engineering and business

A growing collection of Claude Skills that help tech leads explain technical work<br>in the language leadership actually reads, and acts on.

**🚦 Traffic-light labels · 🗣️ Business words, not jargon · 🚫 No made-up numbers**

[🧰 The skills](#-the-skills) · [⚡ Install](#-install-once-get-every-skill) · [📄 Skill 1: Short report](#-skill-1--tech-to-business-short-report) · [🎯 Skill 2: SMART objectives](#-skill-2--tech-to-business-smart-objectives) · [🇪🇸 Español](#-hablas-español)

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

Nobody teaches technical people to answer those questions. New leaders usually learn it the hard way: in a meeting where the CFO asks *"so what?"* and there's no good answer.

**This repo is the shortcut**, one skill at a time.

---

## 🧰 The skills

| # | Skill | What it does | Status |
|:-:|---|---|:-:|
| 1 | 📄 [**Tech-to-business short report**](#-skill-1--tech-to-business-short-report)<br>`tech-to-business-short-report` | Turns a technical change, incident or risk into a 3–4 line business update with a traffic light, numbers and an owner | ✅ Available |
| 2 | 🎯 [**Tech-to-business SMART objectives**](#-skill-2--tech-to-business-smart-objectives)<br>`tech-to-business-smart-objectives` | Turns a technical initiative into one quarterly SMART objective, starting with planning, with 1–3 specific objectives and an owner | ✅ Available |

More skills are on the way. Install once and every new skill arrives automatically.
Need one that isn't here? [Open an issue](../../issues) 💬

---

## ⚡ Install once, get every skill

### 💻 Claude on the web or the desktop app (no code)

1. Open **[Customize → Plugins](https://claude.ai/customize/plugins)**.
2. Click **Add → Add marketplace**.
3. When it asks for the marketplace source, paste this **GitHub repository** URL:
   ```
   https://github.com/MaisfloroTech/tech-business-skills
   ```
   *(the short form `MaisfloroTech/tech-business-skills` also works)*
4. Find **Tech Business Skills** in the plugin list and click **Add**. ✅

It updates on its own when new skills are published, and it also shows up in Claude Code if you use the same account.

### ⌨️ Claude Code (one command)

```
/plugin install tech-business-skills --marketplace MaisfloroTech/tech-business-skills
```

Or just tell Claude Code: *"install the plugin tech-business-skills from the marketplace MaisfloroTech/tech-business-skills"*. If the command isn't recognized, run `claude update` first.

<details>
<summary>🧰 <b>Other ways to install</b> (one skill at a time)</summary>

**Upload a skill as a zip (web or desktop)**

1. Download the skill's zip (for example `tech-to-business-short-report.zip`) from the [latest release](../../releases/latest). Don't unzip it.
2. In Claude, go to **Customize → Skills**, choose **Upload skill** and select the zip.

You'll need to repeat this for every update and every new skill.

**Copy a skill folder (Claude Code)**

```bash
git clone https://github.com/MaisfloroTech/tech-business-skills.git
mkdir -p ~/.claude/skills
cp -r tech-business-skills/tech-to-business-short-report ~/.claude/skills/
```

</details>

> 📝 You need a paid Claude plan (Pro, Max, Team or Enterprise). On Team and Enterprise, an admin may need to allow adding marketplaces, and can install it for the whole organization so everyone reports with the same standard.

---

<div align="center">

# 📄 Skill 1 · Tech-to-business short report

**`tech-to-business-short-report`**

*One technical topic in → one 3–4 line business update out.*

</div>

You tell it your **role** and what happened (notes, tickets, a few numbers). It asks **once**, only if something basic is missing, and gives you back:

- 🎯 **One topic, one item.** One thing, done well. No splitting a single change into five bullets.
- ✂️ **3–4 lines.** No essays, no one-pagers.
- 🚦 **A traffic light** the business reads in a second: 🟢 good, 🟠 watch out, 🔴 bad.
- ❓ **The 6 questions answered:** what, why, when, where, who and how.
- 🗣️ **Business words:** "Infrastructure optimization, 25% smaller", not "DB downsized to 24 vCPU".
- 🔮 **Risks anticipated:** if your notes hint at something that could go wrong, it flags it before it becomes a fire.
- 🙋 **Every risk ends with an ask:** what you need, from whom, by when.
- 👤 **Every item has an owner:** the team or person the business can go to with questions.

### ❓ The 6 questions every item answers

| | Question | In the first example below |
|---|---|---|
| 📌 | **What?** | Optimized the infrastructure, USD 1,200/month saved |
| 🎯 | **Why?** | To reduce operating costs |
| 📅 | **When?** | On Oct 11 |
| 📍 | **Where?** | Our main database |
| 👥 | **Who?** | The SRE team, named as **Owner** so the business knows who to ask |
| 🛠️ | **How?** | Planned 2-hour maintenance window, monitoring after the change |

### 👀 Example: one topic → one item

**You write:**

> *SRE. Downsized the main database from 32 to 24 vCPU on Oct 11, saves about USD 1,200/month. The database costs ~USD 10,000/month. 2-hour maintenance window.*

**You get:**

> 🟢 **[HIGHLIGHT] Infrastructure optimization:** On Oct 11, the SRE team optimized the infrastructure of our main database to reduce operating costs, reducing its size by 25% and generating savings of USD 1,200/month (≈ USD 14,400/year, 12% of its current cost). The change was made in a planned 2-hour maintenance window, and we're monitoring closely to ensure availability for our customers.<br>
> **Owner:** SRE team

Saving money is good for the business, so it's a 🟢 HIGHLIGHT. The title is in business words, "32 → 24 vCPU" becomes "25% smaller", and it closes by reassuring the reader about customers.

### 👀 Example: several topics → several items

**You write:**

> *SRE. Checkout down 25 min Tuesday Oct 7, ~1,100 failed payments, DB connections maxed in a release; we rolled back and added a connection check to releases. Black Friday is Nov 27, never load-tested above 2x, last year's peak was 3x.*

**You get:**

> **Overall: 🟠 RISK – HIGH**
>
> 🟠 **[RISK – HIGH] Black Friday readiness:** on Black Friday (Nov 27), our checkout could slow down or fail for customers on the highest-revenue day of the year. Last year's peak was 3 times normal traffic and the SRE team has only tested up to 2 times.<br>
> **ASK:** ENTER_WHAT_YOU_NEED_AND_BY_WHEN.<br>
> **Owner:** SRE team
>
> 🔴 **[LOWLIGHT] Service interruption:** On Oct 7, customers couldn't pay in checkout for 25 minutes (~1,100 failed payments). An update overloaded the database; the SRE team reverted it and now checks every update for this before release.<br>
> **Owner:** SRE team

The Black Friday comment was a side note in the input; the skill turned it into the first thing leadership reads. You didn't say what you need, so instead of inventing an ask it leaves **ENTER_WHAT_YOU_NEED_AND_BY_WHEN** for you to replace.

### 🚀 Use it

Start a new chat and say something like:

> *"I'm a backend developer. Turn this into an update for my director: …"*

Paste whatever you have: notes, ticket titles, numbers. **Messy is fine.**

You don't need to name the skill. To call it explicitly, type `/` and pick **tech-to-business-short-report** (in Claude Code: `/tech-business-skills:tech-to-business-short-report`). Works for a single change, an incident, a week or a project.

---

<div align="center">

# 🎯 Skill 2 · Tech-to-business SMART objectives

**`tech-to-business-smart-objectives`**

*One technical initiative in → one quarterly objective the business can approve and track.*

</div>

Writing quarterly objectives is the task everyone postpones, and most technical objectives end up like this:

> *"Improve the data platform."* · *"Work on the migration."* · *"Optimize monitoring."*

No number, no date, no owner, no business reason, and no plan. This skill fixes that:

- 🗺️ **Planning comes first.** Every objective starts with *"Plan and implement…"*, because nothing moves without a plan.
- 📏 **SMART by design:** specific, measurable, achievable in one quarter, relevant to the business, time-bound.
- ❓ **The 6 questions answered:** what, why, when, where, who and how.
- 🧩 **One main objective + 1–3 specific ones:** planning first, then execution, then validation, each with a deliverable, a number and a date.
- 👤 **A clear owner**, so everyone knows who answers for it.
- ✅ **A SMART check** at the end that shows which letter still needs your input.

### 👀 Example: with gaps → placeholders

**You write:**

> *"I'm the data lead. Plan and implement the migration (phase 1 of 4) of our current data lake, with the Data, Infrastructure and Development teams. Deliverables: plan, dates, architecture, documentation and X migrated flows. It's for Q1."*

**You get:**

> 🎯 **Data platform modernization · Q1**
>
> Plan and implement phase 1 (of 4) of the migration of our current data lake to ENTER_TARGET_PLATFORM, together with the Data, Infrastructure and Development teams, migrating ENTER_NUMBER data flows by ENTER_DATE, to ENTER_BUSINESS_REASON.
>
> **Owner:** Data team (ENTER_OWNER)
>
> **Specific objectives:**
> 1. 🗺️ **Planning:** deliver the migration plan with dates, target architecture and documentation, approved by Data, Infrastructure and Development, by ENTER_DATE.
> 2. 🛠️ **Execution:** migrate ENTER_NUMBER phase-1 data flows to the new platform, meeting ENTER_SUCCESS_CRITERIA, by ENTER_DATE.
> 3. ✅ **Validation:** deliver the documentation of the migrated flows and the new architecture by ENTER_DATE.
>
> SMART: S ✓ · M ⚠️ ENTER_NUMBER · A ✓ · R ⚠️ ENTER_BUSINESS_REASON · T ⚠️ ENTER_DATE

It didn't know the target platform, the number of flows, the dates or **why** the business needs this, so it left them in UPPERCASE for you instead of guessing. The ⚠️ in the SMART check shows exactly what makes it not-yet-SMART.

### 👀 Example: complete

**You write:**

> *"SRE lead (Ana Pérez). Q3 2026, due Sep 25. Move 40 services' alerting from emails to on-call paging with runbooks, with the Backend and Support teams. Plan approved by Jul 17, all services moved by Aug 28. Today customers report 60% of incidents before we notice; goal is under 20%."*

**You get:**

> 🎯 **Early problem detection · Q3 2026**
>
> Plan and implement on-call paging with runbooks for our 40 production services, together with the Backend and Support teams, so we detect problems before customers do, reducing customer-reported incidents from 60% to under 20% by Sep 25, 2026.
>
> **Owner:** SRE team (Ana Pérez)
>
> **Specific objectives:**
> 1. 🗺️ **Planning:** deliver the rollout plan, alert ownership per service and runbook template, approved by SRE, Backend and Support, by Jul 17.
> 2. 🛠️ **Execution:** move all 40 services from email alerts to on-call paging, each with a runbook, by Aug 28.
> 3. ✅ **Validation:** customer-reported incidents below 20% of all incidents, by Sep 25.
>
> SMART: S ✓ · M ✓ · A ✓ · R ✓ · T ✓

### 🚀 Use it

> *"Help me write my Q1 objective. I'm a backend developer and I want to …"*

Or in Spanish: *"Ayúdame a redactar mi objetivo del Q1. Soy desarrolladora backend y quiero …"*

To call it explicitly, type `/` and pick **tech-to-business-smart-objectives** (in Claude Code: `/tech-business-skills:tech-to-business-smart-objectives`). One objective per answer; ask again for the next one.

---

## 🧭 How every skill thinks

These rules are shared by every skill in the repo, current and future.

### 🚦 Three labels, with a traffic light

Every item gets exactly one, picked by its **effect on the business**, not by how technical it was.

| | Label | Meaning | Examples |
|---|---|---|---|
| 🟢 | **[HIGHLIGHT]** | Something **good for the business** already happened | Money saved or earned, happier customers, time saved, risk reduced, incidents avoided |
| 🟠 | **[RISK – LOW / MEDIUM / HIGH]** | Something **could** hurt the business, or an opportunity could be lost | A peak the system may not hold, a deadline at risk, rising costs, someone key leaving |
| 🔴 | **[LOWLIGHT]** | Something **bad for the business** already happened | Outage customers noticed, lost revenue, security incident, missed commitment |

Need budget, people or a decision? Write the risk of **not** getting it, then the **ASK**. If it isn't good, bad or a risk for the business, it doesn't go in. No "FYI" padding.

### 🪜 From "what I did" to "why it matters"

| | 🔧 Output<br>*what I did* | 📈 Outcome<br>*what changed* | 💼 Business impact<br>*why anyone cares* |
|---|---|---|---|
| **👩‍💻 Developer** | Shipped search filters, fixed 14 bugs | 38% of searches use filters; search tickets 120 → 45/month | ~75 fewer tickets/month ≈ half a support person freed |
| **🎤 Developer Relations** | Gave 12 talks and 4 workshops | 340 sign-ups from the target audience, 60 active accounts | New active users at a fraction of paid acquisition cost |
| **🛡️ Cyber Security** | Closed 300 vulnerabilities | Critical exposure window down from 45 to 9 days | Audit passed with zero critical findings; enterprise deal unblocked |
| **⚙️ SRE / DevOps** | Rightsized cloud resources, added alerting | Monthly bill USD 41k → 34.5k; payment errors detected in 4 min (was 20) | ≈ USD 78k/year saved; issues caught before customers notice |
| **📊 Data Engineer** | Migrated 20 pipelines | Data freshness from 24h to 1h; zero failed loads this month | Sales sees yesterday's numbers this morning, not tomorrow |

*All figures in this README are fictional examples.*

The skills know **31+ roles** (based on the role-based roadmaps of [roadmap.sh](https://roadmap.sh/roadmaps), plus SRE and Tech Lead), so they know which numbers matter for yours. A useful question for any role: **what breaks, and for whom, if you stop doing your job for a month?** That's usually your business impact.

### 🛡️ The honesty promise

These skills make technical work *sound* like business. That's exactly why they have rules:

- 🚫 **They never invent numbers** or facts. No "industry averages", no plausible guesses.
- 🕳️ **Anything you didn't say becomes an UPPERCASE placeholder** (`USD ENTER_AMOUNT`, `INGRESA_FECHA`, `ENTER_WHAT_YOU_NEED_AND_BY_WHEN`). You replace them before sending.
- 🧮 **They show their math** for anything calculated.
- 📉 **Bad news stays the size it was.** No turning lowlights into highlights.

A report with an honest gap is better than a polished one that falls apart at the first question.

### 🇪🇸 ¿Hablas español?

Instálalo igual que arriba y escríbele en español:

> *"Soy desarrolladora backend. Conviértelo en una actualización para mi directora: …"*

Te responde y te entrega el reporte en español. También puedes mezclar: *"háblame en español pero el reporte en inglés para mi jefe global"*. Las etiquetas (HIGHLIGHT, LOWLIGHT, RISK) quedan en inglés por defecto porque son vocabulario común entre equipos; si las quieres traducidas, pídelo.

Every skill answers in whatever language you write in.

---

## 🏢 For teams and companies

Click **Use this template** to create your own private copy, then:

- Add examples with your real metrics (in your private copy only).
- Tune the labels to how your leadership already reports.
- Install it for the whole organization from Claude's admin settings.

## 🤝 Contributing

The most valuable contributions are **role cards**, **before/after examples** (fictional data only) and **ideas for the next skill**. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📁 What's inside

```
tech-business-skills/
├── tech-to-business-short-report/  📄 Skill 1 (one folder per skill)
│   ├── SKILL.md                    the method and examples
│   └── references/
│       ├── labels.md               HIGHLIGHT / LOWLIGHT / RISK
│       ├── translation-ladder.md   output → outcome → impact
│       ├── honesty-rules.md        no invented numbers or facts
│       ├── business-language.md    technical → business titles and words
│       └── roles/                  role cards in 8 families
├── tech-to-business-smart-objectives/  🎯 Skill 2
│   ├── SKILL.md
│   └── references/                 same shared method files
├── .claude-plugin/                 makes the repo installable in one step
└── .github/                        CI and releases
```

---

<div align="center">

⭐ **If this helped you sound more like business and less like a changelog, give it a star.**<br>
It's how we know it's reaching the people who need it.

Made with ☕ by [@maisfloro.tech](https://www.maisfloro.com/)

</div>
