from __future__ import annotations
from typing import Any, Dict

from .rule_engine import run_rules
from .scoring_engine import compute_trust_score

def evaluate_interaction(event: Dict[str, Any]) -> Dict[str, Any]:
    prompt = event.get("prompt_text", "") or ""
    response = event.get("response_text", "") or ""

    rule_score, flags, signals = run_rules(prompt, response)

    # Day 3: no LLM-as-Judge yet (we add on Day 4)
    trust_score, severity = compute_trust_score(
        rule_score=rule_score,
        flags=flags,
        signals=signals,
        judge_scores=None,
    )

    result = {
        "interaction_id": event.get("interaction_id"),
        "timestamp_utc": event.get("timestamp_utc"),
        "model_provider": event.get("model_provider"),
        "model_name": event.get("model_name"),
        "environment": event.get("environment"),
        "application": event.get("application"),
        "use_case": event.get("use_case"),
        "rule_score": rule_score,
        "flags": flags,
        "signals": signals,
        "trust_score_0_100": trust_score,
        "severity": severity,
    }
    return result
