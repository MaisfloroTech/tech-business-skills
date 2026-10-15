[← All skills](../README.md) · Not installed yet? [Install in 1 minute](../README.md#-install-in-claude)

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

### 🚦 The three labels

Every report item gets exactly one, picked by its **effect on the business**, not by how technical it was.

| | Label | Meaning | Examples |
|---|---|---|---|
| 🟢 | **[HIGHLIGHT]** | Something **good for the business** already happened | Money saved or earned, happier customers, time saved, risk reduced, incidents avoided |
| 🟠 | **[RISK – LOW / MEDIUM / HIGH]** | Something **could** hurt the business, or an opportunity could be lost | A peak the system may not hold, a deadline at risk, rising costs, someone key leaving |
| 🔴 | **[LOWLIGHT]** | Something **bad for the business** already happened | Outage customers noticed, lost revenue, security incident, missed commitment |

Need budget, people or a decision? Write the risk of **not** getting it, then the **ASK**. If it isn't good, bad or a risk for the business, it doesn't go in. No "FYI" padding.

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


### 🪜 From "what I did" to "why it matters"

| | 🔧 Output<br>*what I did* | 📈 Outcome<br>*what changed* | 💼 Business impact<br>*why anyone cares* |
|---|---|---|---|
| **👩‍💻 Developer** | Shipped search filters, fixed 14 bugs | 38% of searches use filters; search tickets 120 → 45/month | ~75 fewer tickets/month ≈ half a support person freed |
| **🎤 Developer Relations** | Gave 12 talks and 4 workshops | 340 sign-ups from the target audience, 60 active accounts | New active users at a fraction of paid acquisition cost |
| **🛡️ Cyber Security** | Closed 300 vulnerabilities | Critical exposure window down from 45 to 9 days | Audit passed with zero critical findings; enterprise deal unblocked |
| **⚙️ SRE / DevOps** | Rightsized cloud resources, added alerting | Monthly bill USD 41k → 34.5k; payment errors detected in 4 min (was 20) | ≈ USD 78k/year saved; issues caught before customers notice |
| **📊 Data Engineer** | Migrated 20 pipelines | Data freshness from 24h to 1h; zero failed loads this month | Sales sees yesterday's numbers this morning, not tomorrow |

*All figures are fictional examples.*

The skills know **31+ roles** (based on the role-based roadmaps of [roadmap.sh](https://roadmap.sh/roadmaps), plus SRE and Tech Lead), so they know which numbers matter for yours. A useful question for any role: **what breaks, and for whom, if you stop doing your job for a month?** That's usually your business impact.

### 🇪🇸 En español

Escríbele en español, empezando por tu rol, y te entrega el reporte en español. También puedes mezclar: *"háblame en español pero el reporte en inglés para mi jefe global"*. Las etiquetas (HIGHLIGHT, LOWLIGHT, RISK) quedan en inglés por defecto porque son vocabulario común entre equipos; si las quieres traducidas, pídelo.
