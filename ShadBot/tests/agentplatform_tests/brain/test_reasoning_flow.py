"""
ShadBot Agent Platform

Unit tests for 5.5 Reasoning Flow.
"""

from __future__ import annotations

from uuid import uuid4

from agentplatform.application.brain.reasoning_flow import (
    DecisionSupport,
    ProblemAnalyzer,
    ReasoningEngine,
    ReasoningTrace,
)


def test_problem_analyzer_identifies_problem_options_risks() -> None:
    analyzer = ProblemAnalyzer()
    res = analyzer.analyze("Implement authentication service")
    assert res.problem == "Implement authentication service"
    assert len(res.options) >= 1
    assert len(res.risks) >= 1


def test_reasoning_trace_records_steps() -> None:
    trace = ReasoningTrace()
    step1 = trace.record_step("Check architecture", "Layered")
    step2 = trace.record_step("Check security", "JWT")
    assert len(trace.get_steps()) == 2
    assert step1.step_number == 1
    assert step2.step_number == 2
    assert "2 reasoning steps" in trace.summary()


def test_decision_support_evaluates_options() -> None:
    support = DecisionSupport()
    evals = support.evaluate_options(["Option A", "Option B"])
    assert len(evals) == 2
    assert evals[0].recommended is True
    assert evals[1].recommended is False


def test_reasoning_engine_executes_complete_reasoning() -> None:
    engine = ReasoningEngine()
    out = engine.execute_reasoning("Design scalable API", trace_id=uuid4())
    assert out["selected_option"] is not None
    assert "analysis" in out
    assert "evaluations" in out
    assert "3 reasoning steps" in out["trace_summary"]
