# Business language

Business readers don't always speak technical. The **title** of an item must be in business words; the **body** can mention the technical component in plain words, but leads with what it means for the business.

## Titles: technical → business

| Technical (don't use as title) | Business title |
|---|---|
| Database downsize, rightsizing, instance change, reserved instances, cloud cost | **Infrastructure optimization** |
| Migration to new cluster / cloud / version | **Platform modernization** |
| Outage, downtime, incident, 5xx errors | **Service interruption** |
| Latency, p95, performance tuning, caching | **Faster experience for customers** |
| Load test, autoscaling, capacity planning | **Peak readiness** (e.g. "Black Friday readiness") |
| Patching, vulnerabilities, CVEs, hardening | **Security strengthening** |
| Security breach, data exposure | **Security incident** |
| Backups, disaster recovery, failover | **Business continuity** |
| CI/CD, pipelines, deploy automation | **Faster delivery** |
| Monitoring, alerting, observability | **Early problem detection** |
| Refactor, tech debt | **Platform maintainability** (say what it unblocks) |
| Bug fixes | **Product quality** |
| New feature shipped | the feature's name in customer words (e.g. "Search filters for customers") |
| Data pipelines, ETL, warehouse | **Data availability for decisions** |
| SSO, IAM, access control | **Access security** |
| Audit, SOC 2, ISO, compliance work | **Compliance** |
| Docs, talks, workshops, community | **Product adoption** |

If none fits, ask: *"What would the CFO or a customer call this?"*

## Words to translate in the body

| Instead of | Say |
|---|---|
| vCPU, cores, RAM, nodes, instances | "server size", "capacity" — and give the % change |
| p95, latency, ms | "response time", "how fast pages load" |
| 5xx, error rate | "failed requests", "customers who couldn't <action>" |
| SLA / SLO / uptime | "availability for our customers" (keep the % if relevant) |
| MTTR | "time to recover" |
| CVE, critical vulnerability | "critical security gap" |
| Deploy, release | "update", "change" |
| Rollback | "we reverted the change" |
| Maintenance window | "planned maintenance window" |

Spell out any acronym a business reader may not know, once.

## Sentence shape for a HIGHLIGHT

> On **<date>**, we carried out **<business action>** on **<component, plain words>**, **<technical change as a % or simple number>**, generating **<business result with a number>** (**<% of current total, if known>**). **<Follow-up that reassures the business: monitoring, availability for customers, next step>.**

Example:

> 🟢 **[HIGHLIGHT] Infrastructure optimization:** On Oct 11 we optimized the infrastructure of our main database, reducing its size by 25% and generating savings of USD 1,200/month (≈ USD 14,400/year, 12% of its current cost). We're monitoring closely after the change to ensure availability for our customers.

## Percentages

- **Size or capacity reduction**: compute it from before → after (32 → 24 = 25%).
- **% of current cost**: only if the user gave the current total. Otherwise leave it out; don't invent a total.
- Words like "significant" are fine **only next to the number**, never instead of it.
