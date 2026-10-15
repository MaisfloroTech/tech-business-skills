# Technical topics by role

What to probe in a technical interview for each role, grouped in the same families as `roles/`. Role names follow the role-based roadmaps on [roadmap.sh](https://roadmap.sh/roadmaps), plus SRE and Tech Lead. The topics are our own summary of what each role works with; for the full learning path of a role, see its roadmap.

Each role has:

- **Probe:** the technical areas the questions should cover (pick the ones that match the job, not all).
- **Design exercise:** an architecture or design problem for block 3.
- **Hands-on:** a troubleshooting scenario for block 2.

Calibrate depth to seniority: junior explains how it works and uses it correctly; mid owns a piece end to end and debugs it; senior designs across components and weighs trade-offs; lead/staff sets direction, standards and evolution across teams.

---

## Product Engineering

### Frontend
- **Probe:** HTML semantics and accessibility, CSS layout, JavaScript and TypeScript fundamentals, a component framework (React, Vue, Angular…), state management, rendering strategies (client, server, static), web performance (Core Web Vitals, bundle size, caching), browser APIs, security (XSS, CSP, CORS), testing.
- **Design exercise:** the front end of a product page or checkout that loads fast on mobile, works offline-tolerant and is accessible.
- **Hands-on:** a page got 2 seconds slower after a release; how do you find why?

### Backend
- **Probe:** API design (REST, GraphQL, gRPC), relational and NoSQL databases (modeling, indexes, transactions, isolation), caching, authentication and authorization, queues and async processing, idempotency, concurrency, testing, observability, scaling patterns.
- **Design exercise:** a service that takes orders or payments at peak traffic without losing or duplicating any.
- **Hands-on:** p95 latency of an endpoint doubled and the database CPU is at 90%; walk through it.

### Full Stack
- **Probe:** everything end to end at moderate depth: front-end rendering and state, API design, database modeling, authentication, deployment, basic cloud and CI/CD, testing across layers.
- **Design exercise:** a small product from scratch (sign-up, a core feature, payments or notifications), from screen to database.
- **Hands-on:** a form saves in the UI but the data never shows up for other users; where do you look first?

### Android
- **Probe:** Kotlin, app architecture (MVVM/MVI), lifecycle, Jetpack libraries, concurrency (coroutines, Flow), local storage, networking and offline sync, performance (startup, memory, jank), permissions, testing, Play Store release.
- **Design exercise:** an app screen that works offline and syncs when the connection comes back, without conflicts.
- **Hands-on:** crash rate jumped on a specific Android version after the last release.

### iOS
- **Probe:** Swift, SwiftUI/UIKit, app lifecycle, concurrency (async/await, actors), memory management, persistence, networking and offline, performance, push notifications, testing, App Store review and release.
- **Design exercise:** a feed that loads instantly, caches images and updates in the background.
- **Hands-on:** the app is killed in the background more often since the last update; how do you investigate?

### Game Developer
- **Probe:** a game engine (Unity, Unreal, Godot), game loop, rendering pipeline, physics, math for games (vectors, matrices, quaternions), performance and frame budget, memory, input, asset pipeline, multiplayer basics.
- **Design exercise:** the architecture of a level with many entities that must hold 60 fps on mid-range hardware.
- **Hands-on:** frame rate drops in one area of a level; how do you find the cause?

### Server Side Game Developer
- **Probe:** networking protocols (TCP/UDP), state synchronization, latency compensation, authoritative servers, matchmaking, scaling game servers, persistence, anti-cheat, live operations.
- **Design exercise:** a matchmaking and game-session service for a launch weekend.
- **Hands-on:** players in one region report rubber-banding and desyncs.

### Blockchain
- **Probe:** blockchain fundamentals (consensus, transactions, gas), smart contracts (Solidity or similar), common vulnerabilities (reentrancy, overflow, access control), testing and audits, upgradeability, oracles, wallets and keys, layer 2.
- **Design exercise:** a contract that holds user funds safely and can be upgraded without risk.
- **Hands-on:** a contract call fails only on mainnet and costs far more gas than in tests.

### Forward Deployed Engineer
- **Probe:** integrating a product into a customer's systems (APIs, data pipelines, auth/SSO), scripting, debugging in environments you don't control, data mapping, security and compliance basics, turning one-off work into reusable code.
- **Design exercise:** integrating the product with a customer's legacy system and identity provider.
- **Hands-on:** the integration works in the customer's test environment but fails in their production.

---

## Platform & Reliability

### DevOps
- **Probe:** Linux, networking basics, containers and Kubernetes, infrastructure as code (Terraform or similar), CI/CD design, a cloud provider, secrets management, configuration, observability, deployment strategies (blue-green, canary).
- **Design exercise:** a CI/CD pipeline and environments for 30 services, with safe rollbacks.
- **Hands-on:** deployments to production started failing randomly; the pipeline is green.

### SRE (Site Reliability Engineering)
- **Probe:** SLIs, SLOs and error budgets, observability (metrics, logs, traces), alert design, incident response, capacity planning and load testing, failure modes and resilience patterns (timeouts, retries, circuit breakers), Kubernetes and cloud, postmortems, toil reduction.
- **Design exercise:** making a critical service survive a 3x traffic peak and the loss of a zone.
- **Hands-on:** error rate is at 8% and rising; walk through the first 30 minutes.

### Network Engineer
- **Probe:** TCP/IP, routing (BGP, OSPF), switching and VLANs, DNS, load balancing, VPNs, firewalls, cloud networking (VPC, peering, transit), troubleshooting tools, high availability.
- **Design exercise:** connecting offices and two cloud regions with redundancy and secure access.
- **Hands-on:** one site can reach a service intermittently; others can't reproduce it.

### PostgreSQL / DBA
- **Probe:** data modeling and normalization, indexes and query plans, transactions and locking, vacuum and bloat, replication and failover, backups and point-in-time recovery, partitioning, connection pooling, upgrades, security.
- **Design exercise:** high availability and backup strategy for a database that can't lose a minute of data.
- **Hands-on:** a query that took 50 ms now takes 8 seconds; nothing in the code changed.

### MLOps
- **Probe:** model training and deployment pipelines, feature stores, experiment tracking, model registry, serving (batch, online), monitoring (drift, data quality), reproducibility, GPU/compute management, CI/CD for models.
- **Design exercise:** a pipeline that retrains, validates and safely deploys a model weekly.
- **Hands-on:** a model's accuracy in production dropped over three weeks while offline metrics look fine.

### Inference Engineering
- **Probe:** model serving frameworks, batching, quantization, caching, GPU utilization and memory, latency vs throughput, autoscaling, cost per request, fallbacks and rate limits.
- **Design exercise:** serving a large model to thousands of users with a latency target and a cost ceiling.
- **Hands-on:** p99 latency spikes every few minutes under steady load.

---

## Security

### Cyber Security
- **Probe:** threat modeling, vulnerability management, network and endpoint security, identity and access (IAM, MFA, least privilege), logging and detection (SIEM), incident response, cloud security, common attacks (phishing, ransomware, web OWASP Top 10), compliance frameworks.
- **Design exercise:** securing access to production systems for 200 engineers and contractors.
- **Hands-on:** an alert shows logins to an admin account from two countries in one hour.

### DevSecOps
- **Probe:** security in CI/CD (SAST, DAST, dependency and container scanning), secrets management, infrastructure as code security, supply chain (SBOM, signing), Kubernetes and cloud hardening, policy as code, shifting left without blocking delivery.
- **Design exercise:** a secure pipeline that blocks critical issues but doesn't slow every team down.
- **Hands-on:** a leaked API key is found in a public repository's history.

---

## Data & AI

### Data Analyst
- **Probe:** SQL (joins, window functions, aggregation), data cleaning, statistics basics, spreadsheets, a BI tool, metric definitions, A/B test reading, visualization, data quality checks.
- **Design exercise:** defining and building the metrics for a new product's weekly report.
- **Hands-on:** two reports show different revenue numbers for the same week.

### BI Analyst
- **Probe:** dimensional modeling (facts, dimensions, star schema), SQL, semantic layers, BI tools, dashboard design, refresh and performance, governance and access, metric consistency.
- **Design exercise:** the data model and dashboards for a monthly finance close.
- **Hands-on:** a dashboard takes 40 seconds to load and finance uses it every morning.

### Data Engineer
- **Probe:** batch and streaming pipelines, orchestration, data modeling, warehouses and lakehouses, file formats and partitioning, data quality and contracts, schema evolution, idempotent loads, cost and performance, governance.
- **Design exercise:** a pipeline that brings sales from 5 sources into the warehouse every hour, reliably.
- **Hands-on:** the daily pipeline finished "successfully" but loaded half the rows.

### AI and Data Scientist
- **Probe:** statistics and probability, experiment design, feature engineering, supervised and unsupervised models, model evaluation and validation, bias and leakage, Python data stack, communicating uncertainty.
- **Design exercise:** an experiment to measure whether a new recommendation model increases sales.
- **Hands-on:** a model scores 98% accuracy offline; you suspect something is wrong.

### Machine Learning
- **Probe:** ML algorithms and when to use them, training at scale, evaluation metrics, overfitting and regularization, feature pipelines, deep learning basics, deployment and monitoring, drift, reproducibility.
- **Design exercise:** a fraud detection model that works in real time with very few positive examples.
- **Hands-on:** the model in production behaves differently from the one you validated.

### AI Engineer
- **Probe:** using LLMs through APIs, prompt design, retrieval-augmented generation (embeddings, vector search, chunking), tool use and agents, evaluation of LLM outputs, guardrails and safety, latency and cost, data privacy.
- **Design exercise:** an assistant that answers questions from the company's documents with sources and without leaking private data.
- **Hands-on:** answers were good in testing but users report confident wrong answers.

---

## Quality

### QA
- **Probe:** test strategy and the test pyramid, test design techniques, automation frameworks (UI, API), test data, CI integration, flaky tests, performance and load testing basics, exploratory testing, bug reporting and risk-based testing.
- **Design exercise:** a test strategy for a release that touches payments, with two weeks to ship.
- **Hands-on:** 15% of the automated suite fails randomly and the team stopped trusting it.

---

## Product & Design

### Product Manager
- **Probe (technical side):** how the system works at a high level, APIs and integrations, data and metrics instrumentation, technical debt and its cost, estimation and dependencies, experimentation, working with engineering on trade-offs.
- **Design exercise:** scoping the first version of a feature that depends on two other teams' APIs.
- **Hands-on:** the feature launched but the adoption metric reads zero; is it the feature or the tracking?

### Product Design
- **Probe (technical side):** design systems and components, prototyping tools, handoff to engineering, accessibility standards, responsive design, design tokens, constraints of the platform, usability testing.
- **Design exercise:** designing a flow that engineering can build with existing components in one sprint.
- **Hands-on:** the built screen looks different from the design on half the devices.

### UX Design
- **Probe (technical side):** research methods, information architecture, interaction design, usability testing, accessibility, analytics and funnels, prototyping, working within technical constraints.
- **Design exercise:** redesigning an onboarding flow with a measurable drop-off problem.
- **Hands-on:** usability tests say the flow is clear, but analytics show 60% abandon at one step.

---

## Architecture & Leadership

### Software Architect
- **Probe:** architecture styles (monolith, microservices, event-driven), domain modeling and boundaries, integration patterns, data consistency, scalability and resilience, security architecture, architecture decision records, evolution and migration strategies, cloud architecture.
- **Design exercise:** splitting a monolith (or not) for a company that needs teams to deploy independently.
- **Hands-on:** two services keep breaking each other on every release; what's wrong with the design?

### Engineering Manager
- **Probe (technical side):** system design at a high level, delivery metrics (DORA), technical debt management, incident and on-call practices, code review and quality practices, estimation, hiring for technical skills.
- **Design exercise:** setting up on-call, incident response and quality gates for a team that just took over a critical system.
- **Hands-on:** lead time doubled over the last quarter; how do you find why?

### Tech Lead
- **Probe:** system design, code quality and review, architecture decisions and their documentation, technical debt prioritization, mentoring through code, delivery practices, observability, cross-team technical alignment.
- **Design exercise:** a design for a feature that spans three services owned by two teams.
- **Hands-on:** the team keeps reopening the same bugs in one module.

---

## Communication & Growth

### Developer Relations
- **Probe (technical side):** the product's APIs and SDKs in depth, building demos and sample apps, writing technical content, developer experience (onboarding, docs, errors), community tooling, measuring developer adoption.
- **Design exercise:** a "first 10 minutes" developer onboarding for the product's API.
- **Hands-on:** developers sign up but few make a second API call.

### Technical Writer
- **Probe (technical side):** reading code and APIs, docs-as-code (Markdown, Git, static site generators), API reference (OpenAPI), information architecture, style guides, versioning docs, measuring doc quality.
- **Design exercise:** the documentation structure for a new public API with three audiences.
- **Hands-on:** support keeps getting the same question that the docs supposedly answer.

### SEO
- **Probe (technical side):** crawling and indexing, site architecture and internal links, rendering (JavaScript SEO), Core Web Vitals, structured data, redirects and migrations, log analysis, search console data.
- **Design exercise:** a site migration plan that keeps organic traffic.
- **Hands-on:** organic traffic to one section dropped 40% after a release.
