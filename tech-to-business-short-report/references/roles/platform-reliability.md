# Platform & Reliability

People who keep systems running, fast and affordable, and who make other teams faster. Their business levers: **availability customers feel, cost, and delivery speed for everyone else.**

Their work is mostly invisible when it goes well. That makes measuring it explicitly even more important.

Family-wide ladder:

| Step | Ask for |
|---|---|
| Output | Migrations, automations, pipelines, alerts, runbooks, capacity changes |
| Outcome | Availability vs SLO, incidents (count, severity), MTTR / time to detect, deploy frequency, lead time, change failure rate, cost per unit (request, customer, environment) |
| Business impact | Revenue protected (downtime avoided × revenue per minute), SLA penalties avoided, cloud spend saved, engineering hours freed, faster time to market |

---

### DevOps
- **Produces:** CI/CD, infrastructure as code, environments, developer tooling.
- **Serves:** every engineering team.
- **If it stops:** deployments slow down or break; teams wait on each other.
- **Ask especially for:** deploy frequency, lead time for changes, pipeline duration, change failure rate, environment provisioning time.
- **Typical risks:** single pipeline as a bottleneck, unmanaged secrets, manual steps nobody else knows.
- **Red flag:** "automated X" without hours saved or deployments made faster.

### SRE (Site Reliability Engineering)
*Not a separate roadmap on roadmap.sh, but a common role.*
- **Produces:** SLOs, observability, incident response, reliability improvements.
- **Serves:** customers (indirectly), product teams, leadership.
- **If it stops:** incidents last longer, recur, and are discovered by customers first.
- **Ask especially for:** SLO attainment, error budget burn, incidents by severity, MTTD/MTTR, repeat incidents, toil hours.
- **Typical risks:** upcoming traffic peak, missing on-call coverage, a known single point of failure, alert fatigue.
- **Red flag:** reporting "99.9% uptime" without saying what the target was or what each minute down costs.

### Network Engineer
- **Produces:** connectivity, network design, VPNs, load balancing, DNS, edge.
- **Serves:** every system and office that needs to talk to another.
- **If it stops:** everything stops, often all at once.
- **Ask especially for:** network availability, latency between regions/sites, bandwidth cost, time to provision connectivity, security events at the edge.
- **Typical risks:** single carrier/link, end-of-life equipment, certificate or DNS expiry.
- **Red flag:** "upgraded equipment" without the outage risk it removed.

### PostgreSQL / DBA
- **Produces:** reliable, fast, recoverable databases.
- **Serves:** every service that stores data, and anyone who needs it back after a failure.
- **If it stops:** slow queries degrade the product; a bad failure can lose data.
- **Ask especially for:** query latency on critical paths, replication lag, backup success and **tested** restore time (RPO/RTO), storage growth and cost.
- **Typical risks:** untested backups, storage running out, major version end-of-life, one large table blocking growth.
- **Red flag:** "backups are configured" without a restore test date.

### MLOps
- **Produces:** pipelines to train, deploy, monitor and retrain models.
- **Serves:** data scientists, ML and AI engineers, products using models.
- **If it stops:** models go stale or fail silently; experiments take weeks to reach production.
- **Ask especially for:** time from experiment to production, model drift alerts, training cost, inference availability.
- **Typical risks:** silent model degradation, GPU capacity or cost spikes, no rollback for models.
- **Red flag:** reporting pipelines built without time-to-production or cost figures.

### Inference Engineering
- **Produces:** fast, cheap, reliable serving of AI models.
- **Serves:** products and users calling models in real time.
- **If it stops:** AI features get slow or expensive enough to be switched off.
- **Ask especially for:** latency (time to first token, p95), throughput, cost per 1k requests or per user, GPU utilization, error/timeout rate.
- **Typical risks:** cost growing faster than usage, provider rate limits, capacity for launches.
- **Red flag:** optimizations reported in milliseconds with no cost or user-experience translation.
