<div align="center">

# 🌉 tech-business-skills

### Your translator between engineering and business

A growing collection of Claude Skills that help tech leads explain technical work<br>in the language leadership actually reads, and acts on.

**🚦 Traffic-light labels · 🗣️ Business words, not jargon · 🚫 No made-up numbers**

👋 **Start every message with your role:** *"I'm a…"* / *"Soy…"*

[🧰 The skills](#-the-skills) · [⚡ Install](#-install-once-get-every-skill) · [📄 Skill 1: Short report](#-skill-1--tech-to-business-short-report) · [🎯 Skill 2: SMART objectives](#-skill-2--tech-to-business-smart-objectives) · [📘 Skill 3: FAQ one-pager](#-skill-3--tech-to-business-faq-one-pager) · [🇪🇸 Español](#-hablas-español)

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
| 3 | 📘 [**Tech-to-business FAQ one-pager**](#-skill-3--tech-to-business-faq-one-pager)<br>`tech-to-business-faq-one-pager` | Turns something new you built into a friendly one-page FAQ (the rules of the game), delivered as an editable, branded Word document | ✅ Available |

More skills are on the way. Install once and every new skill arrives automatically.
Need one that isn't here? [Open an issue](../../issues) 💬

> [!IMPORTANT]
> ## 👋 Always start with your role
>
> Begin every message with **"I'm a…"** or **"My role is…"**
> En español: **"Soy…"** o **"Mi rol es…"**
>
> *"**I'm a backend developer.** …"* · *"**My role is SRE lead.** …"* · *"**Soy líder de datos.** …"*
>
> Your role decides which numbers matter (bugs and adoption for a developer, availability and cost for SRE, exposure for security…). Say it first and you get your answer in one shot, without extra questions.


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

> *"I'm an SRE. Downsized the main database from 32 to 24 vCPU on Oct 11, saves about USD 1,200/month. The database costs ~USD 10,000/month. 2-hour maintenance window."*

**You get:**

> 🟢 **[HIGHLIGHT] Infrastructure optimization:** On Oct 11, the SRE team optimized the infrastructure of our main database to reduce operating costs, reducing its size by 25% and generating savings of USD 1,200/month (≈ USD 14,400/year, 12% of its current cost). The change was made in a planned 2-hour maintenance window, and we're monitoring closely to ensure availability for our customers.<br>
> **Owner:** SRE team

Saving money is good for the business, so it's a 🟢 HIGHLIGHT. The title is in business words, "32 → 24 vCPU" becomes "25% smaller", and it closes by reassuring the reader about customers.

### 👀 Example: several topics → several items

**You write:**

> *"I'm an SRE. Checkout down 25 min Tuesday Oct 7, ~1,100 failed payments, DB connections maxed in a release; we rolled back and added a connection check to releases. Black Friday is Nov 27, never load-tested above 2x, last year's peak was 3x."*

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

### 👀 More examples by role

<details>
<summary><b>👩‍💻 Backend developer → 🟢 HIGHLIGHT</b></summary>

**You write:**

> *"I'm a backend developer. On Oct 9 we released the new search filters in the web store, together with Product and Support. Search-related support tickets dropped from 120 to 45 per month."*

**You get:**

```
🟢 [HIGHLIGHT] Better search for customers: On Oct 9, the backend team released new search filters in our web store, together with the Product and Support teams. Since then, support tickets about search dropped from 120 to 45 per month (−63%), so customers find products with less help.
Owner: Backend team (ENTER_OWNER)
```

---

</details>

<details>
<summary><b>🛡️ Cybersecurity → 🟠 RISK – HIGH</b></summary>

**You write:**

> *"My role is security analyst. 3 critical vulnerabilities on the customer portal have been open for 30 days; our policy is 15. The patch needs a 1-hour downtime that Product hasn't approved yet. SOC 2 audit is on Nov 20."*

**You get:**

```
🟠 [RISK – HIGH] Customer portal security: three critical security gaps on our customer portal have been open for 30 days, twice our 15-day policy, and could be flagged in the SOC 2 external security audit on Nov 20. Fixing them needs a 1-hour planned downtime of the portal.
ASK: Product team to approve the 1-hour maintenance window by ENTER_DATE.
Owner: Security team (ENTER_OWNER)
```

---

</details>

<details>
<summary><b>📊 Data engineer → 🔴 LOWLIGHT</b></summary>

**You write:**

> *"I'm a data engineer. On Oct 6 the daily sales pipeline failed and the sales dashboard was 2 days out of date; the commercial team built the weekly forecast with old data. A source system changed its schema without notice. We added schema checks and alerts."*

**You get:**

```
🔴 [LOWLIGHT] Data availability for decisions: On Oct 6, our daily sales data stopped updating, so the sales dashboard was 2 days out of date and the commercial team built the weekly forecast with old data. A source system changed its data format without notice; the data engineering team added automatic format checks and alerts.
Owner: Data Engineering team (ENTER_OWNER)
```

---

</details>

<details>
<summary><b>📊 Data analyst / BI → 🟢 HIGHLIGHT (en español)</b></summary>

**You write:**

> *"Soy analista de BI. El 2 de octubre publicamos el tablero automático de cierre mensual para Finanzas. Antes armaban el reporte a mano en 5 días, en el cierre de septiembre les tomó 1 día."*

**You get:**

```
🟢 [HIGHLIGHT] Cierre mensual más rápido para Finanzas: El 2 de octubre, el equipo de BI publicó un tablero automático de cierre mensual para Finanzas, que antes armaba el reporte a mano. En el cierre de septiembre, el reporte pasó de 5 días a 1 (−80%), liberando 4 días de trabajo del equipo de Finanzas cada mes.
Responsable: Equipo de BI (INGRESA_RESPONSABLE)
```

</details>

### 🚀 Use it

Start a new chat and **begin with your role** ("I'm a…" / "My role is…"):

> *"**I'm a backend developer.** Turn this into an update for my director: …"*

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
- 👩‍💻 **Tailored to your role:** a developer is measured by features adopted and bugs reduced, SRE by availability and cost, security by exposure closed, DevRel by reach and adoption. It picks the right measure for yours.
- 📏 **SMART by design:** specific, measurable, achievable in one quarter, relevant to the business, time-bound.
- ❓ **The 6 questions answered:** what, why, when, where, who and how.
- 🧩 **One main objective + 1–3 specific ones:** planning first, then execution, then validation, each with a deliverable, a number and a date.
- 👤 **A clear owner**, so everyone knows who answers for it.
- 📈 **Expected business impact in %** (optional): performance, cost, development lifecycle, availability, security risk, customers, revenue or team time, computed from your numbers.
- ✅ **A SMART check** at the end that shows which letter still needs your input.

### 👀 Example: with gaps → placeholders

**You write:**

> *"I'm the data lead. Plan and implement the migration (phase 1 of 4) of our current data lake, with the Data, Infrastructure and Development teams. Deliverables: plan, dates, architecture, documentation and X migrated flows. It's for Q1."*

**You get:**

> 🎯 **Data platform modernization · Q1**
>
> Plan and implement phase 1 (of 4) of the migration of our current data lake to ENTER_TARGET_PLATFORM, together with the Data, Infrastructure and Development teams, migrating ENTER_NUMBER data flows by ENTER_DATE, to ENTER_BUSINESS_REASON.
>
> 📈 **Business impact (expected):** ENTER_PERCENT% less time to get data available · ENTER_PERCENT% lower data platform cost
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

> *"I'm Ana Pérez, my role is SRE lead. Q3 2026, due Sep 25. Move 40 services' alerting from emails to on-call paging with runbooks, with the Backend and Support teams. Plan approved by Jul 17, all services moved by Aug 28. Today customers report 60% of incidents before we notice; goal is under 20%."*

**You get:**

> 🎯 **Early problem detection · Q3 2026**
>
> Plan and implement on-call paging with runbooks for our 40 production services, together with the Backend and Support teams, so we detect problems before customers do, reducing customer-reported incidents from 60% to under 20% by Sep 25, 2026.
>
> 📈 **Business impact (expected):** ~67% lower share of incidents reported by customers first (60% → under 20%)
>
> **Owner:** SRE team (Ana Pérez)
>
> **Specific objectives:**
> 1. 🗺️ **Planning:** deliver the rollout plan, alert ownership per service and runbook template, approved by SRE, Backend and Support, by Jul 17.
> 2. 🛠️ **Execution:** move all 40 services from email alerts to on-call paging, each with a runbook, by Aug 28.
> 3. ✅ **Validation:** customer-reported incidents below 20% of all incidents, by Sep 25.
>
> SMART: S ✓ · M ✓ · A ✓ · R ✓ · T ✓

### 👀 More examples by role

<details>
<summary><b>👩‍💻 Frontend developer</b></summary>

**You write:**

> *"I'm a frontend developer. Q2. The checkout page takes 6 seconds to load on mobile, and 70% of our traffic is mobile. Goal: under 3 seconds by June 15, with Design and Backend. We'll measure mobile checkout conversion."*

**You get:**

```
🎯 Faster checkout for mobile customers · Q2

Plan and implement performance improvements to our mobile checkout page, together with the Design and Backend teams, reducing its load time from 6 to under 3 seconds by June 15, because 70% of our traffic comes from mobile, and measuring the effect on mobile checkout conversion (today: ENTER_PERCENT).

📈 Business impact (expected): 50% faster mobile checkout (6 → 3 s) · ENTER_PERCENT% higher mobile checkout conversion

Owner: Frontend team (ENTER_OWNER)

Specific objectives:
1. 🗺️ Planning: deliver the improvement plan with priorities and dates, approved by Frontend, Design and Backend, by ENTER_DATE.
2. 🛠️ Execution: mobile checkout page loads in under 3 seconds, by June 15.
3. ✅ Validation: report mobile checkout conversion before vs. after the change, by ENTER_DATE.
```

SMART: S ✓ · M ✓ · A ✓ · R ✓ · T ⚠️ ENTER_DATE

</details>

<details>
<summary><b>🛡️ Cybersecurity (en español)</b></summary>

**You write:**

> *"Soy analista de ciberseguridad. Q4. Hoy tenemos 120 vulnerabilidades críticas abiertas en servidores expuestos a internet, en promedio 45 días abiertas. Queremos que no quede ninguna crítica con más de 15 días antes del 15 de diciembre, junto a Infraestructura y Desarrollo, para llegar bien a la auditoría ISO 27001 de enero."*

**You get:**

```
🎯 Fortalecimiento de la seguridad · Q4

Planear e implementar la remediación de las 120 vulnerabilidades críticas abiertas en nuestros servidores expuestos a internet, junto a los equipos de Infraestructura y Desarrollo, pasando de 45 días promedio de exposición a ninguna crítica con más de 15 días abierta antes del 15 de diciembre, para llegar preparados a la auditoría ISO 27001 (certificación de seguridad) de enero.

📈 Impacto en el negocio (esperado): al menos 67% menos tiempo de exposición a vulnerabilidades críticas (45 → máximo 15 días)

Responsable: Equipo de Ciberseguridad (INGRESA_RESPONSABLE)

Objetivos específicos:
1. 🗺️ Planificación: entregar el plan de remediación con prioridades, responsables y ventanas de mantenimiento, aprobado por Ciberseguridad, Infraestructura y Desarrollo, antes del INGRESA_FECHA.
2. 🛠️ Ejecución: remediar las 120 vulnerabilidades críticas, sin ninguna con más de 15 días abierta, antes del 15 de diciembre.
3. ✅ Validación: entregar la evidencia de remediación para la auditoría ISO 27001 antes del INGRESA_FECHA.
```

SMART: S ✓ · M ✓ · A ✓ · R ✓ · T ⚠️ INGRESA_FECHA

</details>

<details>
<summary><b>📊 BI analyst</b></summary>

**You write:**

> *"I'm a BI analyst. Q1 2027. Finance builds the monthly close report by hand in spreadsheets and it takes 5 days. I want an automated dashboard so it takes 1 day, by March 20, with Finance and Data Engineering."*

**You get:**

```
🎯 Faster monthly close for Finance · Q1 2027

Plan and implement an automated monthly close dashboard for the Finance team, together with Finance and Data Engineering, reducing the time to prepare the monthly close report from 5 days to 1 by March 20, 2027, freeing 4 days of Finance's work every month.

📈 Business impact (expected): 80% less time to close the month (5 → 1 day) · 4 days of Finance's work freed per month

Owner: BI team (ENTER_OWNER)

Specific objectives:
1. 🗺️ Planning: agree the report's metrics, data sources and delivery dates, approved by Finance and Data Engineering, by ENTER_DATE.
2. 🛠️ Execution: publish the automated monthly close dashboard, by ENTER_DATE.
3. ✅ Validation: Finance closes one month using the dashboard in 1 day, by March 20, 2027.
```

SMART: S ✓ · M ✓ · A ✓ · R ✓ · T ⚠️ ENTER_DATE

</details>

<details>
<summary><b>🧠 Machine learning engineer</b></summary>

**You write:**

> *"My role is ML engineer. Q3. Our fraud model catches 70% of fraudulent payments; we want 85% without blocking more than 1% of legitimate payments. With Payments and Risk teams."*

**You get:**

```
🎯 Fraud prevention · Q3

Plan and implement improvements to our payments fraud detection model, together with the Payments and Risk teams, increasing detected fraudulent payments from 70% to 85% while keeping wrongly blocked legitimate payments at or below 1%, by ENTER_DATE, to ENTER_BUSINESS_REASON.

📈 Business impact (expected): ~21% more fraudulent payments detected (70% → 85%) · USD ENTER_AMOUNT in fraud losses avoided

Owner: ML team (ENTER_OWNER)

Specific objectives:
1. 🗺️ Planning: deliver the model improvement plan, data needed and success thresholds, approved by Payments and Risk, by ENTER_DATE.
2. 🛠️ Execution: put the improved model in production, by ENTER_DATE.
3. ✅ Validation: 85% of fraudulent payments detected with at most 1% of legitimate payments blocked, by ENTER_DATE.
```

SMART: S ✓ · M ✓ · A ✓ · R ⚠️ ENTER_BUSINESS_REASON (e.g. fraud losses in USD) · T ⚠️ ENTER_DATE

</details>

### 🚀 Use it

Start a new chat and **begin with your role** ("I'm a…" / "My role is…"):

> *"**I'm a backend developer.** Help me write my Q1 objective: I want to …"*

Or in Spanish: *"**Soy desarrolladora backend.** Ayúdame a redactar mi objetivo del Q1: quiero …"*

To call it explicitly, type `/` and pick **tech-to-business-smart-objectives** (in Claude Code: `/tech-business-skills:tech-to-business-smart-objectives`). One objective per answer; ask again for the next one.

---

<div align="center">

# 📘 Skill 3 · Tech-to-business FAQ one-pager

**`tech-to-business-faq-one-pager`**

*Something new you built in → one friendly page of FAQs out, as an editable Word document.*

</div>

You launched a new tool, platform or process. Now people ask the same things over and over: *since when does it work? what can I do with it? what can't I? who do I call when it breaks?* Technical people rarely write that down. This skill does it for you:

- ❓ **The 6 questions answered:** what it is, why it exists, who it's for, when it's available, where to find it and how to start.
- 🎮 **The rules of the game:** what you **can** do, what you **can't**, and the limits.
- 🆘 **Help, clearly:** who to contact, which channel, what hours, how fast they answer, and what to do if it's urgent.
- 👀 **At a glance:** four boxes with the key facts at the top.
- 📝 **An editable Word document (.docx)** on one page, so your team can adjust it before sharing.
- 🎨 **Build to Lead design**: brand colors, the logo in the corner and *"Made with ♥ by Build to Lead"* in the footer, in **Spanish or English**.
- 🔄 **Your logo, if you want:** at the end, Claude offers to swap the Build to Lead logo for your company's (PNG or JPG).
- 🕳️ **Missing data is highlighted** (`INGRESA_FECHA`, `ENTER_OWNER`), so you see at a glance what to fill in.

### 👀 What you get

<table>
<tr>
<td width="50%"><a href=".github/assets/faq-example-es.docx"><img src=".github/assets/faq-example-es.png" alt="FAQ one-pager example in Spanish"></a><p align="center"><b>🇪🇸 Español</b> · <a href=".github/assets/faq-example-es.docx">Word</a></p></td>
<td width="50%"><a href=".github/assets/faq-example-en.docx"><img src=".github/assets/faq-example-en.png" alt="FAQ one-pager example in English"></a><p align="center"><b>🇬🇧 English</b> · <a href=".github/assets/faq-example-en.docx">Word</a></p></td>
</tr>
</table>

*Fictional examples.*

### 🚀 Use it

Start a new chat and **begin with your role** ("I'm a…" / "My role is…"):

> *"**I'm a platform engineer.** We're launching a one-click deploy pipeline on Nov 10 for all product teams. Make me the FAQ document: …"*

Or in Spanish: *"**Soy ingeniera de datos.** Vamos a lanzar un portal de autoservicio de datos el 3 de noviembre. Hazme el documento de preguntas frecuentes: …"*

Add whatever you know: dates, who it's for, limits, support channel. Claude asks once for what's missing and gives you the Word file. Want your own logo? Send it when Claude offers, or attach it from the start. To call it explicitly, type `/` and pick **tech-to-business-faq-one-pager** (in Claude Code: `/tech-business-skills:tech-to-business-faq-one-pager`).

> 📝 The Word file is created with code, so **code execution must be on** in Claude (it's needed for skills anyway). Without it, you get the same FAQ as text.

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

Instálalo igual que arriba y escríbele en español, **empezando siempre por tu rol** ("Soy…" / "Mi rol es…"):

> *"**Mi rol es desarrolladora backend.** Conviértelo en una actualización para mi directora: …"*

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
├── tech-to-business-faq-one-pager/     📘 Skill 3
│   ├── SKILL.md
│   ├── scripts/build_faq.py        builds the branded one-page Word document
│   ├── assets/                     Build to Lead logo
│   ├── examples/                   example FAQs in Spanish and English
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
