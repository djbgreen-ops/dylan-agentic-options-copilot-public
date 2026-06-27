# Architecture Overview

D.Y.L.A.N. is organized as a controlled agentic workflow rather than a single prompt response.

## Core loop

retrieve → check → reason → validate → respond

## Public high-level components

1. Input and data completeness guardrail
2. Tool/data quality check
3. Structured candidate reasoning
4. Deterministic risk review
5. Deterministic final validation
6. Human approval / escalation
7. Structured trace log
8. Journal and feedback loop

## Important safety boundary

Memory and retrieval provide context only. They do not override current market data, deterministic validators, or risk controls.

## Proprietary boundary

The private system includes proprietary strategy logic and prompts that are not part of this public repository.
