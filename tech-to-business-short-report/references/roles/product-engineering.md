# Product Engineering

People who build what customers or internal users touch. Their business levers: **features that get used, quality customers feel, and speed of delivery.**

Family-wide ladder:

| Step | Ask for |
|---|---|
| Output | Features shipped, bugs fixed, releases, PRs merged |
| Outcome | Adoption / usage of the feature, error rate, crash-free rate, performance (p95, load time), tickets about the area, cycle time |
| Business impact | Conversion, activation, retention, revenue from the feature, support cost avoided, deals or customers unblocked |

---

### Frontend
- **Produces:** the interfaces users see and interact with on the web.
- **Serves:** end users, product, design.
- **If it stops:** the product feels slow or broken; users drop off before converting.
- **Ask especially for:** load time / Core Web Vitals, funnel step conversion, front-end error rate, accessibility issues closed.
- **Typical risks:** performance regression on key pages, browser/device breakage, design debt slowing every feature.
- **Red flag:** "migrated to framework X" with no user-facing or delivery-speed result.

### Backend
- **Produces:** APIs, business logic, data flows behind the product.
- **Serves:** front-end and mobile teams, integrations, partners.
- **If it stops:** features cannot ship, integrations fail, data becomes inconsistent.
- **Ask especially for:** API latency and error rate, throughput at peak, integration success rate, incidents in owned services.
- **Typical risks:** a service that does not scale for an upcoming peak, fragile third-party dependency, data integrity issues.
- **Red flag:** "refactored service X" without saying what became faster, cheaper or safer.

### Full Stack
- **Produces:** end-to-end features, from UI to data.
- **Serves:** product and end users.
- **If it stops:** whole features stall, not just one layer.
- **Ask especially for:** time from idea to production, feature adoption, defects found after release.
- **Typical risks:** single person owning too much (bus factor), shortcuts piling up as debt.
- **Red flag:** listing every task touched instead of the 1–2 features that moved a number.

### Android / iOS
- **Produces:** mobile apps.
- **Serves:** mobile users, often the highest-engagement segment.
- **If it stops:** store ratings drop, crashes rise, mobile users churn.
- **Ask especially for:** crash-free sessions, store rating, app start time, adoption of new version, mobile conversion.
- **Typical risks:** store policy changes, OS updates breaking the app, release review delays before a launch date.
- **Red flag:** "released version 4.2" without what changed for users.

### Game Developer / Server Side Game Developer
- **Produces:** gameplay, game systems; on the server side, matchmaking, game state, multiplayer infrastructure.
- **Serves:** players, live-ops, monetization teams.
- **If it stops:** players leave; live events fail; in-game revenue drops.
- **Ask especially for:** retention (D1/D7/D30), session length, concurrent players, match failure rate, in-game purchase conversion, server cost per player.
- **Typical risks:** launch/event capacity, cheating/exploits, performance on target hardware.
- **Red flag:** reporting content or systems built without player behaviour data.

### Blockchain
- **Produces:** smart contracts, on-chain integrations, wallet and protocol features.
- **Serves:** users transacting, partners, the protocol's treasury.
- **If it stops:** transactions fail or become expensive; security exposure grows.
- **Ask especially for:** transaction success rate, fees/gas cost per transaction, value secured, audit findings closed, active wallets.
- **Typical risks:** contract vulnerabilities (losses are usually irreversible), regulatory change, dependency on a bridge or oracle.
- **Red flag:** "deployed contract" with no audit status or usage.

### Forward Deployed Engineer
- **Produces:** working solutions inside a customer's environment, often custom integrations.
- **Serves:** specific customers and the sales/success teams.
- **If it stops:** deployments stall, customers don't reach value, renewals are at risk.
- **Ask especially for:** time to first value for the customer, usage after go-live, deals or renewals tied to the deployment, product feedback that became roadmap.
- **Typical risks:** customer environment blockers, scope creep, one-off code that the product cannot maintain.
- **Red flag:** reporting hours on site instead of what the customer can now do.
