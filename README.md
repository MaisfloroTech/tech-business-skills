<div align="center">

# 🌉 tech-business-skills

### Your translator between engineering and business

Claude Skills that help tech leads turn incidents, metrics, tech debt and projects<br>into reports leadership actually reads, and acts on.

**🟢 Highlights · 🔴 Lowlights · 🟠 Risks · ✂️ 3–4 lines each · 🚫 No made-up numbers**

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

Nobody teaches technical people to answer those questions. Big companies have whole rituals for it (weekly business reviews, highlights and lowlights). New leaders usually learn it the hard way: in a meeting where the CFO asks *"so what?"* and there's no good answer.

**This repo is the shortcut.**

## 💡 What it does

You tell it your **role** and paste what happened (notes, tickets, a few numbers). It asks **once** for any basic number that's missing, and gives you back short updates the business understands:

- 🎯 **One topic, one item.** One thing, done well. No splitting a single change into five bullets.
- ✂️ **3–4 lines.** No essays, no one-pagers.
- 🚦 **A traffic light** the business reads in a second: 🟢 good, 🟠 watch out, 🔴 bad.
- ❓ **Answers the 6 questions** any business reader asks: what, why, when, where, who and how.
- 🗣️ **Business words, not jargon:** "Infrastructure optimization, 25% smaller", not "DB downsized to 24 vCPU".
- 💼 **Business first:** money, customers, risk or speed, with a number.
- 🔮 **Risks anticipated:** if your notes hint at something that could go wrong, it flags it before it becomes a fire.
- 🙋 **Every risk ends with an ask:** what you need, from whom, by when.

No long interviews. One round of questions at most, then your report.

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

The skill knows **31+ roles** (based on the role-based roadmaps of [roadmap.sh](https://roadmap.sh/roadmaps), plus SRE and Tech Lead), so it knows which numbers matter for yours. A useful question for any role: **what breaks, and for whom, if you stop doing your job for a month?** That's usually your business impact.

## 🚦 Only three labels, with a traffic light

Every item gets exactly one, picked by its **effect on the business**, not by how technical it was.

| | Label | Meaning | Examples |
|---|---|---|---|
| 🟢 | **[HIGHLIGHT]** | Something **good for the business** already happened | Money saved or earned, happier customers, time saved, risk reduced, incidents avoided |
| 🟠 | **[RISK – LOW / MEDIUM / HIGH]** | Something **could** hurt the business, or an opportunity could be lost | A peak the system may not hold, a deadline at risk, rising costs, someone key leaving |
| 🔴 | **[LOWLIGHT]** | Something **bad for the business** already happened | Outage customers noticed, lost revenue, security incident, missed commitment |

Every 🟠 RISK ends with an **ASK**: what you need, from whom, by when. Need budget, people or a decision? Write the risk of **not** getting it.

If it isn't good, bad or a risk for the business, it doesn't go in the report. No "FYI" padding.

## ❓ The 6 questions every item answers

Anyone in the business will ask these. Every item answers them, woven into 3–4 lines:

| | Question | In the example below |
|---|---|---|
| 📌 | **What?** | Optimized the infrastructure, USD 1,200/month saved |
| 🎯 | **Why?** | To reduce operating costs |
| 📅 | **When?** | On Oct 11 |
| 📍 | **Where?** | Our main database |
| 👥 | **Who?** | The SRE team; customers kept safe |
| 🛠️ | **How?** | Planned 2-hour maintenance window, monitoring after the change |

## 👀 What a report looks like

### One topic → one item

**You write:**

> *SRE. Downsized the main database from 32 to 24 vCPU on Oct 11, saves about USD 1,200/month. The database costs ~USD 10,000/month. 2-hour maintenance window.*

**You get:**

> 🟢 **[HIGHLIGHT] Infrastructure optimization:** On Oct 11, the SRE team optimized the infrastructure of our main database to reduce operating costs, reducing its size by 25% and generating savings of USD 1,200/month (≈ USD 14,400/year, 12% of its current cost). The change was made in a planned 2-hour maintenance window, and we're monitoring closely to ensure availability for our customers.

Saving money is good for the business, so it's a 🟢 HIGHLIGHT. The title is in business words (*Infrastructure optimization*, not *DB downsize*), "32 → 24 vCPU" becomes "25% smaller", and it closes by reassuring the reader about customers instead of adding a separate scary bullet.

### Several topics → several items

**You write:**

> *SRE. Checkout down 25 min Tuesday Oct 7, ~1,100 failed payments, DB connections maxed in a release; we rolled back and added a connection check to releases. Black Friday is Nov 27, never load-tested above 2x, last year's peak was 3x. Need a perf environment approved by Oct 16 to test before Oct 30.*

**You get:**

> **Overall: 🟠 RISK – HIGH**
>
> 🟠 **[RISK – HIGH] Black Friday readiness:** on Black Friday (Nov 27), our checkout could slow down or fail for customers on the highest-revenue day of the year. Last year's peak was 3 times normal traffic and the SRE team has only tested up to 2 times.
> **ASK:** approve a temporary test environment by Oct 16 so we can validate before Oct 30.
>
> 🔴 **[LOWLIGHT] Service interruption:** On Oct 7, customers couldn't pay in checkout for 25 minutes (~1,100 failed payments). An update overloaded the database; the SRE team reverted it and now checks every update for this before release.

The Black Friday comment was a side note in the input; the skill turned it into the first thing leadership reads.

## ⚡ Install in 1 minute

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
<summary>🧰 <b>Other ways to install</b></summary>

**Upload the skill as a zip (web or desktop)**

1. Download `tech-to-business-short-report.zip` from the [latest release](../../releases/latest). Don't unzip it.
2. In Claude, go to **Customize → Skills**, choose **Upload skill** and select the zip.

You'll need to repeat this for every update.

**Copy the folder (Claude Code)**

```bash
git clone https://github.com/MaisfloroTech/tech-business-skills.git
mkdir -p ~/.claude/skills
cp -r tech-business-skills/tech-to-business-short-report ~/.claude/skills/
```

</details>

> 📝 You need a paid Claude plan (Pro, Max, Team or Enterprise). On Team and Enterprise, an admin may need to allow adding marketplaces, and can install it for the whole organization so everyone reports with the same standard.

## 🚀 Use it

Start a new chat and say something like:

> *"Help me write my report for this month. I'm a backend developer and it goes to my director."*

Then paste whatever you have: notes, ticket titles, numbers. **Messy is fine.** Claude asks once for any missing basic number and hands you the report.

You don't need to name the skill. To call it explicitly, type `/` and pick **tech-to-business-short-report** (in Claude Code: `/tech-business-skills:tech-to-business-short-report`).

Works for a week, a month, a project or a single incident.

## 🇪🇸 ¿Hablas español?

Instálalo igual que arriba y escríbele en español:

> *"Ayúdame con mi reporte de este mes. Soy desarrolladora backend y va para mi directora."*

Te hace las preguntas y te entrega el reporte en español. También puedes mezclar: *"háblame en español pero el reporte en inglés para mi jefe global"*. Las etiquetas (HIGHLIGHT, LOWLIGHT, RISK) quedan en inglés por defecto porque son vocabulario común entre equipos; si las quieres traducidas, pídelo.

The skill answers in whatever language you write in.

## 🛡️ The honesty promise

This skill makes technical work *sound* like business. That's exactly why it has rules:

- 🚫 **It never invents numbers.** No "industry averages", no plausible guesses.
- 🕳️ **Gaps stay visible** as UPPERCASE placeholders (`USD ENTER_AMOUNT`, `INGRESA_FECHA`), so you just replace them before sending.
- 🧮 **It shows its math** for anything calculated.
- 📉 **Bad news stays the size it was.** No turning lowlights into highlights.

A report with an honest gap is better than a polished one that falls apart at the first question.

## 🏢 For teams and companies

Click **Use this template** to create your own private copy, then:

- Add examples with your real metrics (in your private copy only).
- Tune the labels to how your leadership already reports.
- Install it for the whole organization from Claude's admin settings.

## 🗺️ What's next

One skill today, more on the way, each in its own folder:

- [x] 📄 **Tech-to-business short report**: short updates with highlights, lowlights and risks
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
├── tech-to-business-short-report/  ← one folder per skill
│   ├── SKILL.md                  the method and an example
│   └── references/
│       ├── labels.md             HIGHLIGHT / LOWLIGHT / RISK
│       ├── translation-ladder.md output → outcome → impact
│       ├── honesty-rules.md      no invented numbers
│       ├── business-language.md  technical → business titles and words
│       └── roles/                role cards in 8 families
├── .claude-plugin/               makes it installable in one step
└── .github/                      CI and releases
```

---

<div align="center">

⭐ **If this helped you sound more like business and less like a changelog, give it a star.**<br>
It's how we know it's reaching the people who need it.

Made with ☕ by [@maisfloro.tech](https://www.maisfloro.com/)

</div>
