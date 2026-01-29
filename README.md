# ReliantAI

**ReliantAI** is a production-grade **AI Governance & Reliability Platform** that provides enterprises with a trust layer for monitoring, evaluating, and auditing AI/ML systems across their lifecycle.

As organizations rapidly deploy **LLMs, ML pipelines, and AI agents**, ReliantAI ensures that AI systems remain **reliable, explainable, auditable, and compliant**—before failures impact customers, revenue, or regulators.

---

## The Problem

Enterprises are deploying AI systems at scale, but lack answers to critical questions:

- Are AI outputs reliable and factually grounded?
- Are models compliant with regulatory and internal policies?
- Can AI decisions be audited and explained?
- Is model behavior drifting over time?
- What is the business and regulatory risk of AI failures?

Existing tools focus on **model training or infrastructure**, but **there is no unified trust layer for AI governance and reliability**.

> There is no “Snowflake for AI governance” — yet.

---

## The Solution

ReliantAI provides an **AI Governance + Reliability Platform** that:

- ✔ Continuously monitors AI output quality  
- ✔ Detects hallucinations, risk signals, and behavioral drift  
- ✔ Tracks lineage from **data → model → output**  
- ✔ Generates audit- and regulator-ready compliance reports  
- ✔ Produces real-time AI **Trust Scores** for operational and executive visibility  

ReliantAI operates as a **sidecar observability platform**, ensuring minimal latency and zero disruption to inference workflows.

---

## High-Level Architecture
Client AI Apps (Chatbots / AI Agents / Internal APIs)
|
ReliantAI SDK
|
Ingestion Gateway
|
-----------------------
| |
Evaluation Engine Metadata Store
| |
Rule Engine Postgres / S3
LLM-as-Judge |
Statistical Models |
| |
Trust Scoring Audit Logs
|
Dashboards & Compliance Reports

## LLM-as-Judge (Live Mode)

This project supports a live LLM-based evaluator (OpenAI / Azure / Bedrock).
For security reasons, live API keys are not included.

To enable live mode:
1. Create a `.env` file
2. Add `OPENAI_API_KEY=...`
3. Swap `llm_judge.py` with `llm_judge_openai.py`



## MVP Scope

The initial MVP focuses on demonstrating measurable AI trust and auditability:

- Ingest AI interaction logs from:
  - OpenAI
  - AWS Bedrock
  - Azure OpenAI
- Evaluate outputs using:
  - Deterministic rules
  - LLM-based semantic evaluation
- Detect reliability anomalies and drift
- Visualize trust metrics and risk trends
- Auto-generate compliance reports (PDF)

---
> ReliantAI is designed for regulated and high-stakes industries such as
> finance, insurance, healthcare, and enterprise AI platforms.


## How TrustLayer Evaluates AI Reliability

TrustLayer AI evaluates AI outputs using a **multi-layer pipeline** designed for enterprise auditability:

1) **Rule Engine (Deterministic)**
- Fast checks for policy violations, sensitive leakage patterns, empty/low-quality outputs, and overconfidence language.

2) **LLM-as-Judge (Semantic Evaluation)**
- A structured rubric scores accuracy/plausibility, completeness, uncertainty handling, safety, and explanation quality.

3) **Drift Detection (Behavior Over Time)**
- Detects changes in reliability trends and embedding-based shifts compared to a baseline.

### Trust Score (MVP)
TrustLayer produces a final **Trust Score (0–100)** per interaction by combining:
- judge metrics (accuracy, completeness, uncertainty, safety)
- deterministic rule flags
- drift alerts

This provides a single reliability signal for dashboards and compliance reporting.

