[← All skills](../README.md) · Not installed yet? [Install in 1 minute](../README.md#-install-in-claude)

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

How it climbs from "what I did" to "why it matters": see the [translation ladder](../tech-to-business-short-report/README.md#-from-what-i-did-to-why-it-matters).


