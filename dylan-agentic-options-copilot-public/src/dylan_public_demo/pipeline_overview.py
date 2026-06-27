"""Sanitized public demo of the D.Y.L.A.N. control flow.

This file is not the private trading system. It is a review scaffold that
shows the high-level agentic workflow without proprietary strategy logic,
prompts, provider integrations, or broker execution.
"""

from dataclasses import dataclass, asdict
from typing import Literal

Status = Literal["PASS", "REJECT", "ESCALATE"]

@dataclass(frozen=True)
class DemoInput:
    symbol: str
    data_quality: str
    candidate_context: str

@dataclass(frozen=True)
class DemoDecision:
    status: Status
    reason: str
    human_approval_required: bool = True


def data_completeness_guardrail(payload: DemoInput) -> None:
    if payload.data_quality != "fresh":
        raise ValueError("Data is not fresh; fail closed.")


def deterministic_risk_review(payload: DemoInput) -> DemoDecision:
    if not payload.candidate_context:
        return DemoDecision("REJECT", "missing_candidate_context")
    return DemoDecision("PASS", "demo_candidate_passed_sanitized_review")


def final_validator(decision: DemoDecision) -> DemoDecision:
    if not decision.human_approval_required:
        raise ValueError("Human approval must remain required.")
    return decision


def run_demo() -> dict:
    payload = DemoInput(symbol="DEMO", data_quality="fresh", candidate_context="sanitized_example")
    data_completeness_guardrail(payload)
    decision = deterministic_risk_review(payload)
    validated = final_validator(decision)
    return {
        "workflow": "retrieve -> check -> reason -> validate -> respond",
        "input": asdict(payload),
        "decision": asdict(validated),
        "note": "Sanitized demonstration only; not trading advice or a trading system.",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_demo(), indent=2))
