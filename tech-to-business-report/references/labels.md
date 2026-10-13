# Labels

Every item in a report carries exactly one label, and is 3–4 lines max. The label tells the reader, in two seconds, whether to keep reading and what to do about it.

There are only three. Fewer labels means less arguing about which one to use.

| Label | What it is | What it must contain |
|---|---|---|
| **[H] HIGHLIGHT** | Something good that **already happened** | At least one measurable result |
| **[L] LOWLIGHT** | Something bad that **already happened** (incident, delay, missed goal) | Cause, measurable impact, what was learned or changed |
| **[R] RISK: Low / Medium / High** | Something that **could happen**: a threat, or an opportunity that could be lost | Probability, impact, mitigation, owner, **ask** |

## Rules

1. **If it is not a highlight, a lowlight or a risk, it does not go in the report.**
   There is no "FYI" label on purpose. Reporting everything you did to prove you were busy is noise. Context belongs inside an item, not as its own item.

2. **Lowlight and risk are not the same.**
   A lowlight already happened. A risk has not happened yet. Mixing them leaves the reader unsure whether they are putting out a fire or preventing one.

3. **Every risk has an ask.** Always. Even if the ask is
   `ASK: none for now, monitoring until <date>`.
   A risk without mitigation, owner and ask is not a report, it is shared anxiety.

4. **Decisions and requests live inside risks.** If you need budget, people, priority or approval, write the risk of *not* getting it:
   - Bad: "We need approval for two more engineers."
   - Good: "[R-High] Delivery of <goal> slips by ~6 weeks if the team stays at 4 people. ASK: approve 2 hires before <date>."

5. **Opportunities are risks too.** If something good could be lost by not acting, label it as a risk:
   "[R-Medium] We lose the chance to <opportunity> if we don't <action> before <date>. ASK: ..."
   This keeps people from feeling they can only ask for help when things go wrong.

6. **A High risk almost always needs an ask aimed at the reader.** If a risk is High and you are asking nobody for anything, either it is not that high, or you are not escalating what you should.

7. **The label must match the content.** A lowlight that describes good news is a mislabel. A highlight with no number is an opinion. Check both before sending.

8. **The assistant picks the label; the writer can change it.** Don't stop to ask about labels.

## Risk severity

Use the higher of the two scores below. If unsure, ask the writer for the worst realistic case, not the worst imaginable one.

| Severity | Probability | Business impact if it happens |
|---|---|---|
| **High** | Likely, or already starting | Hits revenue, customers, legal/compliance, or a committed goal in a way leadership would notice |
| **Medium** | Plausible | Noticeable cost, delay or degradation, contained to one team, product or customer segment |
| **Low** | Unlikely | Small, recoverable, mostly internal |

Mapping from other vocabularies people may use:

- *Blocker* → a **High** risk that is already materializing.
- *Challenge* / *concern* → a **Low** or **Medium** risk.
- *Issue* → a **lowlight** if it already hurt something, a **risk** if it hasn't yet.
- *FYI* / *info* → not an item. Fold it into the context of a related item, or drop it.

## Overall status

A report has one overall status at the top: the **most severe** item inside it.

Order of severity: `RISK: High` > `LOWLIGHT` > `RISK: Medium` > `RISK: Low` > `HIGHLIGHT`.

A report whose overall status is HIGHLIGHT tells the reader "all good, read when you can". A report whose overall status is RISK: High tells them "read this now".
