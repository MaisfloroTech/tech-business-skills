# Honesty rules

These skills make technical work *sound* like business. That is exactly why they can be dangerous: a polished report with an invented number can reach an executive committee and damage the person who sent it.

These rules are not optional.

## 1. Never invent numbers

Every number in a report comes from the writer, from a file or tool they provided, or from arithmetic on those. Not from estimates the assistant makes, "industry averages", or plausible-sounding guesses.

## 2. Leave a visible placeholder for what is missing

When anything the report needs is not available — a number, a date, the reason, the team, the mitigation, the ask — write the sentence as if you had it and put an **UPPERCASE placeholder** where it goes, in the user's language, so they only have to replace it:

- English: `(current monthly cost: USD ENTER_AMOUNT)`, `ENTER_DATE`, `ENTER_NUMBER_OF_CUSTOMERS`, `ENTER_REASON`, `ENTER_MITIGATION`, `ENTER_WHAT_YOU_NEED_AND_BY_WHEN`
- Spanish: `(costo mensual actual: USD INGRESA_MONTO)`, `INGRESA_FECHA`, `INGRESA_CANTIDAD_DE_CLIENTES`, `INGRESA_MOTIVO`, `INGRESA_MITIGACION`, `INGRESA_QUE_NECESITAS_Y_PARA_CUANDO`

Example:

> 🟢 [HIGHLIGHT] Infrastructure optimization: On Oct 11 we optimized the infrastructure of our main database, reducing its size by 25% (current monthly cost: USD ENTER_AMOUNT) and generating savings of USD 1,200/month (≈ USD 14,400/year). We're monitoring closely after the change to ensure availability for our customers.

The placeholder is a feature: it shows exactly what to fill in, and it stops an invented figure from travelling upward. Never replace it with a guess. A report with placeholders is a draft; it should not be sent until they're filled.

**Rule of thumb:** if you're about to write something the user didn't tell you (a plan, a date, a cause, a request, a team), it's a placeholder. The only things you may add yourself are arithmetic on the user's numbers and plain-language rewording.

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
