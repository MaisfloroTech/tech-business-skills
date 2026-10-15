# Designing the 20 questions

The goal: **technical questions that make the candidate reveal how they think about the business.** Not trivia, not "what is Kubernetes". Questions where a strong answer naturally talks about customers, money, risk or time.

## One use case, all the way through

Write **one case for the role** (3–4 sentences): a realistic situation the person would face in the job, with a business stake. Every question connects to it or to the candidate's real past experience with something like it.

- Use the leader's context (industry, product, team, stack, the real challenge). If they gave little, write a plausible case for that role and say it's a proposal they can adjust.
- A case can be fictional, but it must **read as a case**, never as facts about the leader's company. Don't invent the company's numbers; use placeholders (`ENTER_…` / `INGRESA_…`) or round illustrative numbers clearly inside the case ("imagine checkout fails for 20 minutes on a peak day").
- Make the stake explicit: what the business loses if it goes wrong (sales, customers, compliance, time to market, cost).

Good case (SRE, e-commerce): *"Our checkout handles most of the company's revenue. Last month it went down 25 minutes during a campaign, and Black Friday is in six weeks. Leadership wants to know whether we're ready and what it will cost to be."*

## Five blocks, four questions each

| # | Block | What it reveals |
|---|---|---|
| 1 | **Understand the business** | Do they ask *why* before *how*? Do they know who pays for the system and what breaks for whom? |
| 2 | **Design and trade-offs** | Can they choose between options by cost, risk and customer impact, not only by technical taste? |
| 3 | **Execution and incidents** | What did they actually do under pressure? How did they protect customers and communicate? |
| 4 | **Impact and metrics** | Can they climb from output → outcome → business impact (`translation-ladder.md`)? |
| 5 | **Stakeholders and communication** | Can they explain it to leadership, ask for budget, say no, and own a decision? |

Within each block, mix:

- **2 experience questions** (STAR): *"Tell me about a time you…"*. Real past cases.
- **2 case questions** (applied to the use case): *"In our case, how would you… and how would you explain it to the CFO?"*

## Writing each question

- **Technical on the surface, business underneath.** Name the real technical topic of the role (SLOs, schema changes, model drift, caching, pipelines…) and ask for the business side in the same breath.
  - ❌ *"How do you configure alerting?"*
  - ✅ *"Tell me about alerts you designed that caught a problem before customers did. How did you decide what was worth waking someone up for, and what did it save?"*
- **One question, one idea.** Max 2 sentences. Open ("how", "why", "tell me about"), never yes/no.
- **Calibrate to seniority.** Junior: their own tasks and learning. Mid: owning a piece end to end. Senior: trade-offs across teams and money. Lead/Staff: strategy, influence, budget, people.
- **Use the role card** (`roles/`): its *Ask especially for*, *Typical risks* and *Red flag* are the best raw material.

## The dig-deeper line

One STAR follow-up per question, aimed at the letter people usually skip (A or R): *"What did you discard and why?"*, *"What number moved, and what did it mean for customers?"*

## The expected-answer line

One short line (max ~20 words) with **what a strong answer includes**, so any interviewer can score it the same way. Signals, not a script:

- ✅ *"Ties alerts to customer impact and revenue per minute; names a real case and the time to detect before vs after."*
- ❌ *"They should say they use Prometheus."* (a tool, not a signal)

## Fair and legal

Only ask about the job. Never about age, family, pregnancy, religion, nationality, health, sexual orientation, politics or anything unrelated to doing the work. If the leader asks for something like that, leave it out and say why in one line.
