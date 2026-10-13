# Example: tech-to-business one-pager

All names, companies and figures below are **fictional**. This example covers one week; the same format works for a month, a quarter, a project or an incident.

## Writer

- **Role:** Platform & Reliability (SRE lead).
- **Definition:** "We keep the payments platform up and fast. Product teams and, indirectly, every paying customer depend on it. If we stop for a month, outages last longer, they repeat, and customers find them before we do."
- **Audience:** Director of Engineering and the VP of Product.

## Raw material the writer pasted

> - outage tue checkout ~25 min, db connections maxed, rolled back
> - finished alerting on payment errors
> - black friday in 6 weeks, load test not done, need perf env
> - moved 3 services to new cluster
> - cloud bill down after rightsizing
> - on-call: Ana leaving end of month
> - wrote runbooks

## What the assistant asked (abridged)

- Tuesday outage: *how many checkouts failed or were delayed, and do you know revenue per minute at that hour?* → "about 1,100 failed checkouts; revenue per minute — I don't know." → `[MISSING]`.
- Alerting: *since it went live, did it catch anything before customers did?* → "Yes, Thursday, payment-provider errors, 4 min to detect vs ~20 min before."
- Cluster migration and runbooks: *what changed for the business?* → "Nothing visible yet." → dropped from the report (no highlight, lowlight or risk).
- Cloud bill: *before and after?* → "USD 41k → 34.5k per month, permanent."
- Black Friday: *what happens if the load test isn't done?* → "Last year peak was 3x normal; we've never tested above 2x."
- Ana leaving: *who covers on-call?* → "Nobody yet. Rotation goes from 5 to 4 people."

## Resulting report

```markdown
# Payments Platform — Weekly report — Week of 2026-10-05
**Overall status:** RISK: High
**DRAFT** — missing: revenue per minute at checkout peak

## Need to know

**[R-High] Black Friday capacity (Platform, peak sales day of the year):** Last year's peak was 3x normal traffic; we have never tested above 2x. Probability of degradation at peak: high without a test. Impact: checkout slowdown or outage on the highest-revenue day. Mitigation: load-test plan ready, blocked on a performance environment.
ACTION: run 3x load test — Platform, by 2026-10-30. **ASK:** approve a temporary performance environment (≈ 2 weeks) by 2026-10-16.

**[L] Checkout outage, Tuesday (Platform, ~1,100 failed checkouts):** 25 minutes of failed checkouts after database connections maxed out during a release. Rolled back. Revenue impact: [MISSING: revenue per minute at that hour — ask Finance/analytics]. Learned: connection limits now checked in the release pipeline.
ACTION: add connection-pool alert — Platform, by 2026-10-12.

**[R-Medium] On-call coverage drops from 5 to 4 people (Platform, response time to incidents):** One engineer leaves at month end; no replacement yet. Each person goes from 1 week in 5 to 1 week in 4 on call, during the peak season. Mitigation: borrowing one engineer from the Core team is being discussed.
ACTION: confirm interim cover — Platform lead, by 2026-10-20. **ASK:** support for the cross-team loan if Core pushes back.

**[H] Cloud cost down USD 6.5k/month (Platform, infrastructure budget):** Rightsizing cut the monthly bill from USD 41k to 34.5k (−16%), permanent. ≈ USD 78k/year at current usage.

**[H] Payment errors now detected in 4 minutes (Platform, checkout reliability):** New alerting caught a payment-provider issue on Thursday in 4 min vs ~20 min before, before any customer report.

## Goal tracking

| Goal (SMART) | Unit | Target | Due | Expected to date | Actual | % of expected | Status |
|---|---|---|---|---|---|---|---|
| Checkout availability ≥ 99.9% in Q4 | % | 99.9 | 2026-12-31 | 99.9 | 99.82 | — | Off track |
| Reduce monthly cloud cost by USD 8k in Q4 | USD/month saved | 8,000 | 2026-12-31 | 2,700 | 6,500 | 241% | On track |
| Load test at 3x peak before Black Friday | test done | 1 | 2026-10-30 | 0.5 | 0 | 0% | Off track |

Status: On track ≥ 100% · At risk 80–99% · Off track < 80% of expected to date. Availability is a threshold goal: below target = Off track. Expected to date assumes linear progress.

---
Legend: [H] Highlight · [L] Lowlight · [R] Risk (Low / Medium / High)
```

## Coaching notes the assistant gave

1. The cloud-cost highlight is the strongest item: before → after, annualized, permanent. Use it as the model.
2. The outage lowlight is incomplete without revenue per minute. Ask Finance once; you'll reuse that number in every incident report.
3. The Black Friday risk has a clear ask with a date. Keep doing that.
