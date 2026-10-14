# Labels

Every report item carries exactly one label, written as a **full word** with its **traffic light**. Business readers scan the color first, then the word.

| Light | Label | What it is | Must contain |
|---|---|---|---|
| 🟢 | **[HIGHLIGHT]** | Something **good for the business** that already happened | At least one measurable result |
| 🔴 | **[LOWLIGHT]** | Something **bad for the business** that already happened | Measurable impact, cause, what changed so it doesn't repeat |
| 🟠 | **[RISK – LOW]** · **[RISK – MEDIUM]** · **[RISK – HIGH]** | Something that **could** hurt the business, or an opportunity that could be lost | Impact if it happens, why it could happen, **ASK** |

Always write the full words: `[HIGHLIGHT]`, `[LOWLIGHT]`, `[RISK – HIGH]`. Never abbreviations like `[H]`, `[L]` or `[R-High]`.

## How to pick the label: what is good, medium or bad for a business

Pick the label by the **main business effect** of what happened, not by how technical or risky the work felt.

### 🟢 Good for the business → HIGHLIGHT

- **Money saved:** lower cloud or infrastructure cost, fewer licenses, cheaper vendor, less overtime.
- **Money earned:** more sales, conversion or revenue, a deal closed or unblocked, upsell enabled.
- **Customers happier or retained:** fewer complaints or tickets, better ratings, lower churn, faster response.
- **Time saved:** manual work automated, faster delivery, shorter lead time, faster onboarding.
- **Risk reduced:** vulnerabilities closed, single points of failure removed, backups tested, audit passed, compliance achieved.
- **Reliability improved:** fewer or shorter incidents, SLA met, problems detected before customers notice.
- **Capacity gained:** the business can grow, launch or absorb a peak without new spend.

### 🟠 Could go either way → RISK

- **Something can break:** capacity near its limit, an upcoming traffic peak, an untested change, end-of-life systems.
- **Something can be late:** a deadline at risk, a dependency on another team or vendor, a blocked decision.
- **Something can cost more:** costs trending up, a contract renewal, usage growing faster than budget.
- **Something depends on people:** one person holds key knowledge, someone is leaving, the team is overloaded.
- **Exposure that hasn't been exploited (yet):** open vulnerabilities, pending audit findings, missing controls.
- **An opportunity can be lost:** a deal, a launch window or a saving that disappears if nobody acts by a date.

### 🔴 Bad for the business → LOWLIGHT

- **Customers hit:** outage, degradation, failed transactions, data issues they noticed.
- **Money lost:** lost revenue, SLA penalties, unplanned spend, cost overrun.
- **Security or compliance event:** breach, data exposure, failed audit, regulatory issue.
- **Commitment missed:** a deadline, goal or promise to a customer that was not met.
- **Trust damaged:** escalations, a lost customer or deal, bad press.

## Rules

1. **One topic → one item, one label.** A single change or event is told as **one** item, even if it has a side effect to watch. Mention what you're watching inside the same item, as the closing follow-up sentence; don't split it into a second item.
   - A cost saving is a 🟢 HIGHLIGHT. If it also needs monitoring, say so in its closing sentence ("We're monitoring closely after the change to ensure availability for our customers."). It does **not** become a separate RISK item.
   - Create a separate RISK item only when the risk is a **different topic** from what the user reported, or when the risk is bigger than the result itself.

2. **If it is not good, bad or a risk for the business, it doesn't go in the report.** No "FYI". Context goes inside an item.

3. **Lowlight and risk are not the same.** A lowlight already happened. A risk hasn't happened yet.

4. **Every risk ends with an ASK.** Even `ASK: none for now, monitoring until <date>`.

5. **Requests live inside risks.** Need budget, people or a decision? Write the risk of *not* getting it, then the ASK.

6. **Opportunities are risks too.** "We lose <opportunity> if we don't <action> by <date>."

7. **A HIGH risk almost always needs an ask aimed at the reader.**

8. **The label must match the business effect.** Good news labeled LOWLIGHT, or a HIGHLIGHT with no number, is wrong.

9. **The assistant picks the label; the writer can change it.** Don't stop to ask about labels.

## Risk severity

| Severity | Probability | Business impact if it happens |
|---|---|---|
| **HIGH** | Likely, or already starting | Hits revenue, customers, compliance or a committed goal in a way leadership would notice |
| **MEDIUM** | Plausible | Noticeable cost, delay or degradation, contained to one team, product or segment |
| **LOW** | Unlikely | Small, recoverable, mostly internal |

Other words people use: *blocker* → RISK – HIGH already materializing. *Challenge / concern* → RISK – LOW or MEDIUM. *Issue* → LOWLIGHT if it already hurt something, RISK if not yet.

## Overall status (only when there are several items)

With two or more items, start with `Overall:` and the most severe label:
🟠 RISK – HIGH > 🔴 LOWLIGHT > 🟠 RISK – MEDIUM > 🟠 RISK – LOW > 🟢 HIGHLIGHT.

With a single item, skip the overall line: the item's own light says it.
