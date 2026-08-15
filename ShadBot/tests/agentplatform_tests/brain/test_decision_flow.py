"""
ShadBot Agent Platform

Unit tests for 5.6 Decision Flow.
"""

from __future__ import annotations

from agentplatform.application.brain.decision_flow import (
    DecisionApproval,
    DecisionEvaluator,
    DecisionFlowService,
    DecisionGenerator,
)


def test_decision_generator_creates_alternatives() -> None:
    gen = DecisionGenerator()
    alts = gen.generate(["Use Django", "Use FastAPI"])
    assert len(alts) == 2
    assert alts[0].title == "Use Django"


def test_decision_evaluator_scores_alternatives() -> None:
    gen = DecisionGenerator()
    alts = gen.generate(["Option 1", "Option 2"])
    evaluator = DecisionEvaluator()
    scored = evaluator.evaluate(alts)
    assert len(scored) == 2
    assert scored[0].score >= scored[1].score


def test_decision_approval_checks_threshold() -> None:
    gen = DecisionGenerator()
    alts = gen.generate(["Option 1"])
    scored = DecisionEvaluator().evaluate(alts)
    res = DecisionApproval().approve(scored[0])
    assert res.approved is True


def test_decision_flow_service_orchestrates_decision() -> None:
    service = DecisionFlowService()
    pkg = service.decide(["Clean Architecture", "Monolith"])
    assert pkg.approved is True
    assert pkg.selected_title == "Clean Architecture"
