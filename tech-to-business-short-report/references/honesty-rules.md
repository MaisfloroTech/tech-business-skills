# Honesty rules

These skills make technical work *sound* like business. That is exactly why they can be dangerous: a polished report with an invented number can reach an executive committee and damage the person who sent it.

These rules are not optional.

## 1. Never invent numbers

Every number in a report comes from the writer, from a file or tool they provided, or from arithmetic on those. Not from estimates the assistant makes, "industry averages", or plausible-sounding guesses.

## 2. Mark what is missing, visibly

When a needed number is not available, write it in the report as:

```
[MISSING: <what is missing> — <who or where it could come from>]
```

Examples:
- `[MISSING: revenue per hour on checkout — ask Finance or the product analytics dashboard]`
- `[MISSING: number of customers affected — check support tickets tagged with the incident ID]`

A visible gap is a feature. It teaches the writer what they need to go find, and it stops a fabricated figure from travelling upward. A report can be shared with gaps marked as "draft"; it should not be sent as final with gaps.

## 3. Show your arithmetic

If a number in the report was calculated (savings, percentages, annualized values), keep the inputs and formula next to it or in a note. The reader must be able to check it in under a minute.

## 4. Separate fact from estimate from opinion

- Fact: measured. Write it plainly.
- Estimate: say so and say how: "≈ 40 h/month (estimated from 3 sample weeks)".
- Opinion / expectation: attribute it: "The team expects...", "Customer said...".

## 5. Don't upgrade the evidence

"One customer mentioned it" is not "customers want it". "Latency improved in staging" is not "latency improved". "Should reduce incidents" is not "reduced incidents". Keep claims at the level the evidence supports.

## 6. Bad news is reported at the same size as it happened

Do not soften a lowlight into a highlight, or shrink a High risk to Medium because it feels uncomfortable. Leaders lose trust in reports that are always green.

## 7. Confidential data stays out of examples

When the writer shares real data to build a report, use it only for that report. Do not reuse names of customers, people or figures in examples, templates or anything meant to be shared.
