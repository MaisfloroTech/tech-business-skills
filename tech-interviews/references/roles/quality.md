# Quality

### QA (Quality Assurance)
- **Produces:** test strategy, automated and exploratory testing, release confidence.
- **Serves:** engineering teams, product, and ultimately customers who don't hit bugs.
- **If it stops:** bugs reach customers; releases slow down because nobody trusts them.

| Step | Ask for |
|---|---|
| Output | Test cases, automated tests, test runs, bugs reported |
| Outcome | Defects escaped to production (by severity), automated coverage of critical flows, time to run regression, release rollback rate |
| Business impact | Customer-facing incidents avoided, support tickets avoided, faster releases (time to market), cost of fixing bugs earlier vs later |

- **Typical risks:** a critical flow without automated tests before a launch, flaky tests that teams start to ignore, regression testing that takes days.
- **Red flag:** "found 80 bugs" or "wrote 500 tests" without escaped defects or release speed. Finding many bugs late is not a highlight.
