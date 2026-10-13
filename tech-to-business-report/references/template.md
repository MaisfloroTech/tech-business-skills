# One-pager template

Copy this structure exactly. Remove the `<!-- -->` comments.

```markdown
# <Team / area> — <Report type, e.g. Weekly / Monthly / Project / Incident report> — <period or date>
**Overall status:** <RISK: High | LOWLIGHT | RISK: Medium | RISK: Low | HIGHLIGHT>
<!-- Only if any [MISSING] remains: -->
**DRAFT** — missing: <item 1>, <item 2>

## Need to know

**[R-High] <Topic> (<owner>, <what's at stake>):** <Situation, 1 clause>. <What could happen, with a number>. Probability: <low/medium/high + why>. Mitigation: <what's being done>.
ACTION: <next step> — <owner>, <date>. **ASK:** <what you need from the reader, by when>

**[L] <Topic> (<owner>, <what was affected>):** <Situation>. <What happened and the measurable impact>. <Action taken>. Learned/changed: <one line>.
ACTION: <next step> — <owner>, <date>

**[H] <Topic> (<owner>, <what it moved>):** <Situation and the goal (task)>. <Action>. <Result: before → after, and why it matters to the business>.

## Goal tracking

| Goal (SMART) | Unit | Target | Due | Expected to date | Actual | % of expected | Status |
|---|---|---|---|---|---|---|---|
| <specific goal> | <unit> | <target> | <date> | <value> | <value> | <%> | On track / At risk / Off track |

Status: On track ≥ 100% · At risk 80–99% · Off track < 80% of expected to date.
<!-- Add notes for "lower is better" or threshold goals, and if linear progress was assumed. -->

---
Legend: [H] Highlight · [L] Lowlight · [R] Risk (Low / Medium / High)
```

## How STAR maps into one item

| STAR | In the item | Ladder step |
|---|---|---|
| Situation | The context, one clause | — |
| Task | The goal it served (ideally a SMART goal from the table) | — |
| Action | What was done | Output |
| Result | What changed + what it means for the business, with a number | Outcome → Business impact |

For a RISK, "Result" becomes the impact *if nothing changes*, plus probability, mitigation and ASK.

## Item checklist

| Label | Must have |
|---|---|
| [H] | ≥ 1 measurable result, ideally before → after |
| [L] | Cause, measurable impact, what was learned or changed, ACTION |
| [R-Low/Medium/High] | Probability, impact, mitigation, owner, ACTION, **ASK** |

## Length

- 3–8 items.
- Max 4 lines per item.
- One page total, including the goal table.
