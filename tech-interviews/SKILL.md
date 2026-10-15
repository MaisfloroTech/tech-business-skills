---
name: tech-interviews
description: Prepares a technical job interview, 80% technical and 20% business, for the role being hired (roadmap.sh roles, plus SRE and Tech Lead). Writes one realistic use case and 20 questions in 5 blocks (fundamentals, hands-on troubleshooting, an architecture design exercise, scale-reliability-security, and business), each with a deep-dive follow-up and one line on what a strong answer includes. Technical answers are scored with a C·R·E·H rubric (correct, reasoning, edge cases, hands-on) and business answers with STAR. Delivers a branded Build to Lead fillable PDF of about 3 pages to record answers, scores and a final recommendation. Use this whenever a leader or interviewer needs a technical interview, technical screen, system design interview, interview questions or scorecard for a technical role. For an interview focused on business thinking, use tech-to-business-interviews. Works best when the user starts with their role ("I'm a…" / "Soy…"). Never invents facts about the company.
---

# Tech interviews

A technical interview has to answer one question: **how deep does this person really go?** Most interviews stay at the surface: tool names, definitions, puzzles. This skill prepares an interview that digs: the fundamentals of the role, real troubleshooting, an architecture exercise on a realistic case, what breaks at scale, and a short business block so you also know whether they connect their work to the company. It writes **one use case and 20 questions** (**80% technical, 20% business**), each with a **deep-dive follow-up** and a short line on **what a strong answer includes**, and delivers it as a **branded, fillable PDF** where the interviewer records answers and scores.

**One role, one interview, done well.**

For an interview focused on **business thinking** (STAR on every question), use the sibling skill `tech-to-business-interviews`.

## Language

Answer and write the guide in the language the user writes in. The PDF supports **Spanish (`"es"`) and English (`"en"`)** for its fixed labels; for any other language, write the content in that language and use `"en"` labels. Missing data goes in as UPPERCASE placeholders in the user's language.

## Flow

### 1. Ask once, only if needed

**The role always comes first.** If the user's message doesn't start by saying who they are, your one question round **opens with the role**, phrased so they learn the habit:
> *"First: who are you? Start with **"I'm a…"** or **"My role is…"** (e.g. "I'm the tech lead"). Then…"*
> (Spanish: *"Primero: ¿quién eres? Empieza con **"Soy…"** o **"Mi rol es…"** (por ejemplo "Soy tech lead"). Luego…"*)

If the user already gave enough, **build the guide right away**. Otherwise ask, in **one short message**, only for what's missing:

1. **Their role** (who interviews) and **the role being hired**, with **seniority** (junior, mid, senior, lead).
2. **The stack and the product:** languages, cloud, databases, the system the person will work on.
3. **The real technical challenge** of the first months (a migration, a scale problem, a new service…). It becomes the use case.
4. Optional: interview length, topics that matter most, topics to skip.

Never ask a second round. If the role and seniority are there, you have enough: propose a plausible case and say it's a proposal. **Anything about the company you don't know** goes in as an UPPERCASE placeholder, never as a guess: `ENTER_STACK`, `ENTER_VOLUME` (Spanish: `INGRESA_STACK`, `INGRESA_VOLUMEN`).

### 2. Know the role

Read `references/technical-topics.md` and find the role being hired. Its **Probe**, **Hands-on** and **Design exercise** are the raw material for blocks 1, 2 and 3. Calibrate depth to the seniority.

For block 5 (business), read `references/roles/README.md` and **only the matching family file**: its *Ask especially for*, *Typical risks* and *Red flag* tell you what business sense looks like for that role. If the role isn't listed anywhere, use the closest one and the three questions in `roles/README.md`.

### 3. Write the guide

Read `references/question-design.md` (case, blocks, how to write each question) and `references/evaluation.md` (how answers are scored).

- **One use case** of 3–4 sentences, technical and concrete, with numbers the candidate can reason with, clearly inside the case.
- **20 questions in 5 blocks of 4**, always in this order:
  1. Fundamentals (technical)
  2. Hands-on and troubleshooting (technical)
  3. Architecture and design (technical; **question 9 is the design exercise**, marked `"big": true`)
  4. Scale, reliability and security (technical)
  5. Business and teamwork (**the 20%**: every question marked `"type": "experience"` or `"type": "business"`, so it's scored with STAR)
- **Technical questions test understanding**: how it works, when not to use it, what breaks. No trivia, no puzzles unrelated to the job.
- **Dig deeper:** one follow-up per question that goes one level down (mechanism, failure, measurement).
- **Strong answer:** one short line (max ~20 words) with the concepts, trade-offs and edge cases of a strong answer.
- **Fair questions only:** about the job, never about age, family, religion, nationality, health or other personal topics (see `references/honesty-rules.md`).

### 4. Build the PDF

Write the content to a JSON file and run the bundled script. Its path is relative to the folder that contains this SKILL.md:

```bash
python <this-skill-folder>/scripts/build_interview.py interview.json <output-folder>/tech-interview-<role>.pdf --page a4
```

- The script installs `reportlab` if it's missing.
- **Always set `"mode": "technical"`** in the JSON: technical questions get the **C · R · E · H** rubric (Spanish PDF: **C · R · B · P**), and questions typed `experience` or `business` get **STAR**.
- Save the file where the user can download it (for example `/mnt/user-data/outputs/` if it exists) and share it.
- Use `--page letter` if the user is in the US or Canada or asks for Letter; otherwise A4.
- **Deliver the PDF.** It's the editable format: the interviewer types the candidate's answers (including notes on the design they draw), ticks the letters heard, scores each question 1–4 and fills in the final recommendation, in any PDF reader.
- It runs about **3–4 pages**: the cover block (candidate, interviewer, date, the case and the rubric), the 20 questions and the final assessment.
- The document always has a logo in the top-right corner (**Build to Lead's by default**), the Build to Lead colors and the footer **"Made with ♥ by Build to Lead" / "Hecho con ♥ por Build to Lead"**. Never remove the footer.
- **Custom logo:** if the user gives you their own logo (PNG or JPG), pass it with `--logo path/to/logo.png`. If they send another format, ask for a PNG or JPG.
- If you can't run code in this environment, give the guide in Markdown in the same order and say the fillable PDF needs code execution turned on.

JSON format:

```json
{
  "mode": "technical",
  "language": "en",
  "role": "Senior Backend Engineer",
  "team": "Orders team",
  "duration": "75 min",
  "case": "3–4 sentences: the system, the scale, the constraint, the challenge.",
  "focus": ["APIs and data consistency", "Scaling at peak"],
  "blocks": [
    {
      "title": "Fundamentals",
      "questions": [
        {"q": "The question.", "deep": "The follow-up.", "expect": "What a strong answer includes."}
      ]
    },
    {
      "title": "Architecture and design",
      "questions": [
        {"q": "The design exercise for the case.", "deep": "…", "expect": "…", "big": true}
      ]
    },
    {
      "title": "Business and teamwork",
      "questions": [
        {"q": "Tell me about a time…", "deep": "…", "expect": "…", "type": "experience"},
        {"q": "In our case, how would you explain…", "deep": "…", "expect": "…", "type": "business"}
      ]
    }
  ]
}
```

`focus` is optional (up to 3 short items: the technical areas this role must master). Five blocks, four questions each. Complete examples: `examples/tech-interview-example-en.json` and `examples/tech-interview-example-es.json`. The script warns if the guide doesn't have 20 questions in 5 blocks, if the business share isn't about 4 questions, or if a line runs long.

### 5. Close

After sharing the PDF, keep it short:

1. One line on how to use it: *"Type the answers in the boxes, tick the letters you heard and score each question 1–4. Question 9 is the design exercise: let them draw it."*
2. If you proposed the case or left placeholders, say it in one line so they adjust it.
3. **Offer to replace the logo**, once: *"Want your company's logo instead of Build to Lead's? Send it as PNG or JPG and I'll regenerate the PDF."* (Spanish: *"¿Quieres el logo de tu empresa en vez del de Build to Lead? Envíamelo en PNG o JPG y regenero el PDF."*)

If the user didn't state their role up front, add one line, in their language: *"Tip: start your next message with "I'm a…" / "My role is…" and you'll get it in one shot."* (Spanish: *"Tip: empieza tu próximo mensaje con "Soy…" / "Mi rol es…" y lo tendrás a la primera."*)

The first time in a conversation, add once, in the user's language: a short invitation to star https://github.com/MaisfloroTech/tech-business-skills if it helped. Never star the repo on the user's behalf unless they explicitly say yes.

## Example

**User:** *"I'm the tech lead. I'm hiring a senior backend engineer for our food delivery app. Python and PostgreSQL on AWS. Orders spike at lunch and we've had duplicated orders."*

You have the role, the seniority, the stack and the challenge: build it right away. Case: the order service at lunch peak, retries creating duplicates, a dependency on the payment provider. Then 20 questions, for example:

> **9 · Architecture and design** (design exercise, large box)
> Design the order placement flow for 2,000 orders a minute at peak, so a retry from the app or a slow payment provider never creates a duplicate order or charge.
> *Dig deeper:* Walk me through what happens if the payment provider times out after charging.
> *Strong answer:* Idempotency keys, clear order states, outbox or queue, reconciliation with the provider; draws it end to end.

Full guides: `examples/tech-interview-example-en.json` (senior backend, food delivery) and `examples/tech-interview-example-es.json` (DevOps semi senior, retail, in Spanish).

## Rules

- **Never invent facts about the company** (see `references/honesty-rules.md`).
- **80/20:** 16 technical questions, 4 business ones. Don't let the business block grow.
- **Understanding over trivia.** If a question can be answered by memorizing a definition, rewrite it.
- **One role per guide.** If the user brings several, do the most important one and offer the next.
- **Same guide, same scale** for every candidate for the role.
- Don't reuse a user's or a candidate's real names, systems or figures in anything meant for others.
