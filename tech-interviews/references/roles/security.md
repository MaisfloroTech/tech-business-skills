# Security

People who reduce the chance and the cost of bad things happening. Their business levers: **exposure reduced, incidents contained, compliance kept, and the business able to say yes to customers and auditors.**

Security is hard to report because success is "nothing happened". Measure exposure and time, not activity.

Family-wide ladder:

| Step | Ask for |
|---|---|
| Output | Vulnerabilities closed, controls implemented, policies written, trainings run, tools deployed |
| Outcome | Mean time to remediate by severity, open critical/high exposure (count and days open), coverage (% of assets scanned / with control X), phishing click rate, detection and response time |
| Business impact | Probability and cost of an incident reduced, audit/certification status, customer security reviews passed, deals unblocked, regulatory fines avoided, business downtime avoided |

---

### Cyber Security
- **Produces:** vulnerability management, detection and response, security controls, awareness, compliance evidence.
- **Serves:** the whole company, customers, auditors and regulators.
- **If it stops:** exposure grows silently until an incident or a failed audit.
- **Ask especially for:** critical/high vulnerabilities open and their age, MTTR by severity vs policy, incidents and containment time, % of assets covered, audit findings open.
- **Typical risks:** unpatched critical exposure on an internet-facing asset, third-party/supplier breach, upcoming audit with open findings, credentials or access not reviewed.
- **Red flag:** "closed 300 vulnerabilities" without severity, exposure time, or how much of the attack surface is still open.

### DevSecOps
- **Produces:** security built into the delivery pipeline: scanning, secrets management, policy as code, secure defaults.
- **Serves:** engineering teams (so they ship safely without slowing down) and the security team.
- **If it stops:** vulnerabilities reach production and are found late, when they cost more to fix.
- **Ask especially for:** % of repos/pipelines with security checks, vulnerabilities caught before production vs after, time to fix findings in the pipeline, secrets exposed, pipeline time added by checks.
- **Typical risks:** security gates bypassed under deadline pressure, leaked secrets, vulnerable dependencies in core services.
- **Red flag:** "added a scanner" without findings caught or developer friction measured.
