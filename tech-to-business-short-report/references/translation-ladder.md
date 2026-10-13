# The translation ladder

Technical people usually report what they **did**. The business cares about what **changed** and what that **means** in money, customers, risk or time.

Every item climbs the same three steps:

| Step | Question | Example (developer) |
|---|---|---|
| **1. Output** | What did I do or produce? | Shipped the new search filters; fixed 14 bugs |
| **2. Outcome** | What changed because of it? | 38% of searches now use filters; support tickets about search dropped from 120 to 45 per month |
| **3. Business impact** | Why does the business care? | ~75 fewer tickets/month ≈ 0.5 support FTE freed; search-to-purchase rate up 1.2 points |

**Rule: an item that stops at Output is not ready.** Ask for the next step. If the writer does not have the data, mark it `[MISSING: ...]` and say where it could come from (see `honesty-rules.md`). Never fill the gap yourself.

## The four currencies of business impact

Almost every business impact ends up in one of these. When stuck, ask "which of these does it touch?"

| Currency | Sounds like | Typical evidence |
|---|---|---|
| **Revenue / growth** | More customers, more usage, more sales, faster deals | Conversion, activation, retention, expansion, pipeline influenced, deals unblocked |
| **Cost / efficiency** | Spend less, do more with the same team | Cloud cost, hours saved, tickets avoided, headcount not needed, vendor cost |
| **Risk / trust** | Avoid losses, keep promises, stay compliant | Incidents avoided or shortened, SLA met, audit findings, exposure window, customer escalations |
| **Speed / capacity** | Deliver sooner, react faster | Lead time, time to market, deploy frequency, onboarding time, decision time |

## Questions that climb the ladder

Use these in the conversation. Pick the ones that fit; do not fire all of them.

**From output to outcome**
- After this shipped, what is different? For whom?
- How do you know it is being used / it worked? What number moved?
- What was the number before? What is it now?

**From outcome to business impact**
- Which of the four currencies does this touch?
- Who outside the team would notice if this had not been done? What would they say?
- What would it have cost (money, customers, time) to *not* do this?
- Is there a number someone in finance, sales or support already tracks that this moved?

**The key question for any role**
- *What breaks, and for whom, if you stop doing this for a month?*
  The answer is almost always the business impact.

## Turning outcomes into money (only with the writer's numbers)

These are formulas, not data. Use them only with inputs the writer gives you, and show the formula so the reader can check it.

- **Time saved** = hours saved per occurrence × occurrences per period × loaded hourly cost
- **Downtime cost** = minutes of impact × revenue or transactions per minute affected × % of users affected
- **Tickets avoided** = tickets before − tickets after × average handling cost per ticket
- **Cloud savings** = monthly cost before − monthly cost after (annualize only if the change is permanent)
- **Delay cost** = value per week of the thing being delayed × weeks of delay

If an input is unknown, keep the formula and mark the input: `[MISSING: average cost per support ticket — ask Support Ops]`.

## Words that signal you are still at Output

Watch for these. They usually mean the item needs one more step:
"implemented", "migrated", "refactored", "attended", "delivered", "worked on", "improved" (without a number), "aligned", "supported", "had a good meeting", "strengthened the relationship".

None of them are wrong. They are just not finished.
