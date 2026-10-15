# Designing the 20 questions

The goal: find out **how deep the candidate really goes technically**, and check that they still connect their work to the business. **80% technical, 20% business:** 16 technical questions and 4 business questions.

## One use case, all the way through

Write **one case for the role** (3–4 sentences): a realistic technical situation the person would face in the job, with enough detail to design and debug against (scale, constraints, what already exists). Blocks 2–4 come back to it.

- Use the leader's context (product, stack, scale, the real challenge). If they gave little, write a plausible case for that role and say it's a proposal.
- The case can be fictional but must read as a case, not as facts about the leader's company. Unknown company facts become placeholders (`ENTER_STACK` / `INGRESA_STACK`).
- Give it numbers the candidate can reason with ("about 2,000 orders a minute at lunch peak", "30 services"), clearly inside the case.

## Five blocks, four questions each

| # | Block | Type | What it reveals |
|---|---|---|---|
| 1 | **Fundamentals** | technical | Do they understand how the core tools of the role work, not only how to use them? |
| 2 | **Hands-on and troubleshooting** | technical | Can they find a problem methodically, from symptom to cause, in a real system? |
| 3 | **Architecture and design** | technical | Can they design a solution for the case and defend it? |
| 4 | **Scale, reliability and security** | technical | What breaks first at 10x, how it fails, how it's protected, what it costs? |
| 5 | **Business and teamwork** | business (STAR) | Do they connect technical decisions to customers, money, risk and time, and work well with others? |

Pick the topics from `technical-topics.md` for the role: block 1 from **Probe**, block 2 from **Hands-on**, block 3 from **Design exercise**.

### Block 1 · Fundamentals
Questions that test understanding, not trivia. Ask *how it works*, *when you would not use it*, *what goes wrong*.
- ❌ *"What is an index?"*
- ✅ *"An index made a read query faster but inserts got slower. Explain why, and how you'd decide whether to keep it."*

### Block 2 · Hands-on and troubleshooting
Two **scenarios** ("p95 doubled, CPU at 90%, walk me through it") and two **real cases** from their experience ("Tell me about the hardest bug you've chased"). Listen for method: hypotheses, data, narrowing down, verifying the fix.

### Block 3 · Architecture and design
- **Question 9 is the design exercise** for the case: mark it `"big": true` so it gets a large box to take notes on what the candidate draws or describes. Let them draw on a whiteboard or shared screen.
- Questions 10–12 dig into **their** design: the data model, what happens when a component fails, how it evolves or what they'd change with twice the budget or half the time.

### Block 4 · Scale, reliability and security
Push the design and the case: 10x traffic, a dependency down, a security threat specific to the role, cost and performance. One question can ask for a real experience with scale or an incident.

### Block 5 · Business and teamwork (the 20%)
Four questions marked `"type": "experience"` (a real past case, evaluated with STAR) or `"type": "business"` (applied to the case). Two of each:
- The business cost or impact of a technical decision they made.
- Explaining a technical trade-off to someone non-technical (product, leadership).
- Prioritizing technical debt against features.
- Disagreeing with a decision and committing.

## Writing each question

- **One question, one idea.** Max 2 sentences (the design exercise may use 3). Open, never yes/no.
- **Calibrate to seniority.** Junior: explain and use correctly. Mid: own and debug a component end to end. Senior: design across components and weigh trade-offs. Lead/Staff: direction, standards, evolution across teams.
- **Stay in the role's real stack** when the leader gave one; otherwise stay tool-agnostic (concepts over brand names).
- **No trick questions or puzzles** unrelated to the job (no "reverse a linked list" for a DevOps role).

## The dig-deeper line

One follow-up that goes **one level down**: *"How does that work internally?"*, *"What happens if that fails?"*, *"What would you measure to know it worked?"*, *"What did you try first that didn't work?"*. For business questions, aim it at the STAR letter people skip (usually Action or Result).

## The expected-answer line

One short line (max ~20 words) with **what a strong answer includes**: the concepts, the trade-offs, the edge cases. Signals, not a script; tools only when the stack makes them the point.

- ✅ *"Idempotency key per order, at-least-once delivery, dedup on write; names the race between retry and timeout."*
- ❌ *"They should use Kafka."*

## Fair and legal

Only ask about the job. Never about age, family, pregnancy, religion, nationality, health, sexual orientation, politics or anything unrelated to doing the work. If the leader asks for something like that, leave it out and say why in one line.
