"""
ShadBot Agent Platform

Unit tests for 5.11 Learning Flow.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.brain.learning_flow import (
    ExperienceExtractor,
    LearningFlowService,
    PatternRecognizer,
    StrategyImprover,
)
from agentplatform.domain.results import AgentResult
from agentplatform.infrastructure.memory import InMemoryMemoryRepository


def test_experience_extractor_extracts_lesson() -> None:
    res = AgentResult(success=True, message="ok", data={"agent": "architect"})
    exps = ExperienceExtractor().extract([res])
    assert len(exps) == 1
    assert exps[0].success is True
    assert exps[0].reusable_pattern is not None


def test_pattern_recognizer_counts_occurrences() -> None:
    res = AgentResult(success=True, message="ok", data={"agent": "architect"})
    exps = ExperienceExtractor().extract([res, res])
    pats = PatternRecognizer().recognize(exps)
    assert len(pats) == 1
    assert pats[0].occurrence_count == 2


def test_strategy_improver_selects_top_pattern() -> None:
    res = AgentResult(success=True, message="ok", data={"agent": "architect"})
    pats = PatternRecognizer().recognize(ExperienceExtractor().extract([res]))
    strat = StrategyImprover().improve(pats)
    assert "Layered" in strat.preferred_pattern


def test_learning_flow_service_updates_knowledge_repo() -> None:
    repo = InMemoryMemoryRepository()
    service = LearningFlowService(repository=repo)
    project_id = uuid4()
    res = AgentResult(success=True, message="ok", data={"agent": "architect"})
    pkg = service.learn(project_id, [res])
    assert pkg.knowledge_report.updated_records == 1
    assert len(repo.get_project_memory(project_id)) == 1
