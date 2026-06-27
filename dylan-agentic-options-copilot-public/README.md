# D.Y.L.A.N. — Dynamic Yield Logic & Analysis Navigator

**Capstone public repository — sanitized review version**

D.Y.L.A.N. is an agentic options trade co-pilot designed to support structured analysis, risk review, validation, journaling, and pre-paper-trading evaluation. This public repository is intentionally limited: it explains the architecture and shows a simplified demo pipeline without exposing proprietary trading strategy details, prompts, paid-data integrations, credentials, or broker execution logic.

## Problem

Options traders often combine market context, chart structure, option-chain data, risk constraints, and journaling manually. That creates room for incomplete setups, inconsistent sizing, weak documentation, and overconfidence. D.Y.L.A.N. addresses the process problem: how to move from a trade idea to a structured, auditable, human-reviewed decision package.

## Intended user

The intended user is a disciplined options trader or investor who wants decision support, not autonomous execution. The system is designed for supervised analysis and pre-paper-trading evaluation.

## Architecture overview

The private project uses a staged workflow:

```text
retrieve → check → reason → validate → respond
```

Major components include:

- data/tool quality checks
- opportunity/candidate evaluation
- structured agent reasoning
- deterministic risk review
- deterministic final validation
- human approval / escalation
- trace logging
- journal and feedback loop
- backtest and paper-package evaluation gates

## Public release boundary

This repository does **not** include:

- proprietary trading strategy rules
- private prompts
- paid data-provider implementation details
- API keys or credentials
- broker execution code
- live trading logic
- enough information to reproduce the full D.Y.L.A.N. trading process

## What is included

- high-level architecture overview
- sanitized demo pipeline
- sample terminal summary artifact
- evaluation summary
- safety and reliability notes
- instructions for technical review

## Setup

This public demo requires Python 3.11+.

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python src/dylan_public_demo/pipeline_overview.py
```

The demo prints a simplified, synthetic decision trace. It is **not** a trading system.

## Evaluation summary

The private capstone evaluation completed a BT0–BT10 backtest arc. Publicly shareable summary:

- production regression suite remained green at 55/55
- prompt hashes remained stable at 9/9
- preliminary replay kept realized, modeled, excluded, and sensitivity outcomes separate
- no backtest artifact authorizes paper trading or live capital

## Current status

```text
production_candidate / backtest_required / paper_trade_required / live_capital_not_approved
```

## Repository review path

1. Read `docs/architecture_overview.md`.
2. Review `src/dylan_public_demo/pipeline_overview.py`.
3. Review `sample_artifacts/sanitized_terminal_summary.json`.
4. Review `docs/evaluation_summary.md` and `docs/safety_reliability.md`.

## Capstone report link

Add this repository URL to the final capstone report before submission:

https://github.com/dennisbgreen/dylan-agentic-options-copilot-public
