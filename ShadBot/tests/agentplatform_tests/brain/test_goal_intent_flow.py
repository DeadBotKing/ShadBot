"""
ShadBot Agent Platform

Unit tests for 5.12 Goal & Intent Flow.
"""

from __future__ import annotations

from agentplatform.application.brain.goal_intent_flow import (
    GoalAligner,
    GoalIntentService,
    IntentCorrector,
    IntentDetector,
    PriorityManager,
)


def test_intent_detector_identifies_intent() -> None:
    det = IntentDetector()
    res_test = det.detect("Please verify and test module")
    assert "Verification" in res_test.primary_intent
    res_arch = det.detect("Design clean architecture")
    assert "Architecture" in res_arch.primary_intent


def test_intent_corrector_preserves_high_confidence() -> None:
    intent = IntentDetector().detect("Design clean architecture")
    corr = IntentCorrector().correct(intent)
    assert corr.was_corrected is False


def test_goal_aligner_combines_vision() -> None:
    intent = IntentDetector().detect("Build service")
    aligned = GoalAligner().align(intent, "ShadBotCore")
    assert "ShadBotCore" in aligned.goal_title
    assert aligned.is_aligned is True


def test_priority_manager_sets_critical_timeout() -> None:
    prio = PriorityManager().prioritize(True)
    assert prio.priority_level == "CRITICAL"
    assert prio.execution_timeout_seconds == 300


def test_goal_intent_service_executes_pipeline() -> None:
    service = GoalIntentService()
    pkg = service.process("Design architecture for Meryx", "Meryx")
    assert pkg.aligned.is_aligned is True
    assert pkg.priority.priority_level == "CRITICAL"
