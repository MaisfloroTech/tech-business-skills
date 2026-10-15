# Architecture & Leadership

People whose output is mostly other people's output: decisions, direction, teams. Their business levers: **better decisions earlier, teams that deliver, and capacity for what the business needs next.**

This is where new leaders most often get stuck reporting their own hands-on work instead of what their team and decisions changed.

---

### Software Architect
- **Produces:** technical direction, architecture decisions, standards.
- **Serves:** engineering teams and leadership.
- **If it stops:** systems grow inconsistent, expensive and hard to change; the same problems get solved five times.
- **Ladder:**
  - Output: decisions documented (ADRs), reviews done, standards defined.
  - Outcome: teams adopting the decision, incidents or rework avoided, time to build similar features, systems retired.
  - Business impact: cost avoided (infra, licenses, rework), time to market for the next initiatives, risk reduced.
- **Typical risks:** a critical system at end-of-life, architecture that won't support the next 12 months of growth, key knowledge in one person.
- **Red flag:** reporting diagrams and meetings instead of decisions and their consequences.

### Engineering Manager
- **Produces:** a team that delivers: hiring, growth, process, priorities.
- **Serves:** the team, product, leadership.
- **If it stops:** delivery becomes unpredictable, people leave, priorities drift.
- **Ladder:**
  - Output: hires made, 1:1s, plans, process changes.
  - Outcome: delivery predictability (committed vs delivered), team health (attrition, engagement), time to productivity of new hires, on-call load.
  - Business impact: goals delivered on time, cost of attrition avoided, capacity available for new priorities.
- **Typical risks:** key person leaving, team overloaded, hiring behind plan, a commitment the team cannot meet.
- **Red flag:** reporting the team's tasks without the commitment they served.

### Tech Lead
*Not a separate roadmap on roadmap.sh, but a common first leadership role.*
- **Produces:** technical decisions for a team, unblocking, quality bar.
- **Serves:** the team and its product goals.
- **If it stops:** the team stalls on decisions, quality drops, rework grows.
- **Ladder:**
  - Output: reviews, designs, decisions, pairing.
  - Outcome: team throughput and cycle time, defects, decisions made without escalation.
  - Business impact: the team's goal delivered, rework and incidents avoided.
- **Typical risks:** the tech lead as bottleneck, technical debt slowing the roadmap, unclear ownership.
- **Red flag:** reporting only personal coding output.
