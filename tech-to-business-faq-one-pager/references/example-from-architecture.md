# Example: from an architecture diagram to a FAQ

Fictional data. Shows how to turn a technical input into a FAQ for non-technical readers.

## Input

The user attaches an architecture diagram:

> Student → WhatsApp → Twilio WhatsApp API → **"Grades lookup bot"** (Amazon Lex) → Moodle function (AWS Lambda) → Moodle REST Web Services. The Lambda reads its configuration from AWS Secrets Manager and sends logs to Amazon CloudWatch.

And writes:

> *"Soy staff engineer en la universidad y estoy desplegando una nueva integración de un chatbot (adjunto la arquitectura). Estará disponible a partir del 30 de octubre de 2026 para todos los estudiantes y les ayudará a encontrar información relevante a sus horarios y salones de clase asociados. Cualquier duda deberán consultarlo con el equipo de operaciones directamente en el sistema de tickets corporativo. En caso de dudas el equipo de operaciones me escalará los requerimientos. Estaré monitoreando el comportamiento en la semana de marcha blanca."*

## What to take from the diagram

| From the diagram | Goes in the FAQ as |
|---|---|
| WhatsApp | "En WhatsApp" — it's what students touch |
| Moodle | "el campus virtual de la universidad" — where the information comes from |
| Twilio, Amazon Lex, AWS Lambda, Secrets Manager, CloudWatch | **Nothing.** Internal; students don't need it |
| Bot name "Grades lookup" | **Mismatch** with the text (schedules and classrooms) → follow the text, flag it |

## What's missing (placeholders)

WhatsApp number, how students identify themselves, availability hours of the bot, link to the ticket system, support hours, response time, any other limit, and the project owner's name.

## Output (JSON for `build_faq.py`)

See `examples/faq-example-chatbot-es.json`. Key choices:

- **Title in student words:** "Asistente de horarios por WhatsApp", not "Integración chatbot Lex-Moodle".
- **Owner vs. support:** the engineering team owns it (footer); students go to **Operations** for help, and Operations escalates to engineering.
- **Marcha blanca** is explained in plain words in the "when" answer: the first week is monitored closely.
- **Limits** only state what the user said (it answers schedules and classrooms). Anything else is a placeholder, not a guess.

## Closing lines

> Reemplaza los campos en mayúscula antes de compartirlo (están resaltados en el documento).
> Ojo: en el diagrama el bot se llama "Consulta Calificaciones", pero me dijiste horarios y salones; usé horarios y salones. Confírmalo.
> ¿Los estudiantes tienen acceso al sistema de tickets corporativo? Si es solo interno, conviene darles otro canal.
> ¿Quieres usar el logo de tu empresa en vez del de Build to Lead? Envíamelo en PNG o JPG y regenero el documento.
