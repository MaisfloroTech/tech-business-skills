# Plain language for the FAQ

The people reading this FAQ **use** the thing; they didn't build it. Write for them: what they see, what they can do, who helps them. Not how it works inside.

## Questions: the way a user asks them

| Don't write | Write |
|---|---|
| Access provisioning process | How do I get access? |
| Service availability window | When can I use it? |
| Rate limits and quotas | How much can I use it? |
| Incident escalation path | What do I do if it stops working? |
| Scope and non-goals | What can't I do with it? |
| Data retention policy | How long is my information kept? |

## Words to translate in the answers

| Instead of | Say |
|---|---|
| Deploy, release, rollout | "launch", "update", "it's available from…" |
| Downtime, outage, 5xx errors | "when it's not working", "if you can't <action>" |
| Maintenance window | "planned maintenance", with day and hours |
| SLA / SLO / uptime | "available <hours/days>", "we answer within <time>" |
| Latency, timeout | "it may take a few seconds", "if it doesn't respond" |
| Authentication, SSO, IAM, credentials | "sign in with your <company> account", "who can use it" |
| Endpoint, API, URL | "the link", "the page", "the address" |
| Ticket, incident | "request", "report a problem" |
| Quota, rate limit, throttling | "up to <number> per <day/month>" |
| Deprecated, end-of-life | "will stop working on <date>", "use <new thing> instead" |

Spell out any acronym the reader may not know, once. Keep the product's own name even if it's technical; that's what users will search for.

## Keep internal components out

Lambda, API Gateway, queues, databases, Kubernetes, Secrets Manager, vendor APIs… are how the team built it, not what the reader uses. Mention only what the reader sees or touches ("WhatsApp", "the portal", "the virtual campus").

## Tone

- Second person ("you" / "tú"), friendly, short.
- Answers of 1–3 sentences. If it needs more, it's a separate question.
- Say what to do, not only what's forbidden: "You can't delete reports, but you can archive them."
