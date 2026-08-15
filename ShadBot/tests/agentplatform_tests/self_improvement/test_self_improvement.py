"""
ShadBot Agent Platform

Unit tests for Phase 10 Self Improvement System.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.orchestration import AgentOrchestrator
from agentplatform.application.self_improvement import (
    BrainEvolutionManager,
    ExperimentEngine,
    PerformanceTracker,
    ProposalGenerator,
    ReflectionAnalyzer,
    SelfImprovementServiceLayer,
)
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult


def test_reflection_analyzer_and_tracker() -> None:
    res = AgentResult(True, "ok")
    ana = ReflectionAnalyzer().analyze([res])
    trend = PerformanceTracker().track(ana)
    assert ana.success_ratio == 1.0
    assert trend.status == "IMPROVING"


def test_experiment_engine_and_proposal_gen() -> None:
    exp = ExperimentEngine().create_experiment("Hypothesis A")
    assert exp.is_safe is True
    prop = ProposalGenerator().generate(exp)
    assert prop.approved_for_evolution is True


def test_brain_evolution_manager_evolves() -> None:
    exp = ExperimentEngine().create_experiment("Hypothesis A")
    prop = ProposalGenerator().generate(exp)
    rep = BrainEvolutionManager().evolve(prop)
    assert rep.evolved is True
    assert "1.1-evolved" in rep.version


def test_self_improvement_service_executes_cycle() -> None:
    service = SelfImprovementServiceLayer()
    ana, trend, exp, prop, evo = service.run_improvement_cycle([AgentResult(True, "ok")])
    assert evo.evolved is True
    assert prop.approved_for_evolution is True


def test_self_improvement_models_to_dict() -> None:
    res = AgentResult(True, "ok")
    ana = ReflectionAnalyzer().analyze([res])
    trend = PerformanceTracker().track(ana)
    exp = ExperimentEngine().create_experiment("Hypothesis B")
    prop = ProposalGenerator().generate(exp)
    evo = BrainEvolutionManager().evolve(prop)

    ana_dict = ana.to_dict()
    trend_dict = trend.to_dict()
    exp_dict = exp.to_dict()
    prop_dict = prop.to_dict()
    evo_dict = evo.to_dict()

    assert isinstance(ana_dict, dict) and "success_ratio" in ana_dict
    assert isinstance(trend_dict, dict) and trend_dict["status"] == "IMPROVING"
    assert isinstance(exp_dict, dict) and exp_dict["experiment_id"] == str(exp.experiment_id)
    assert isinstance(prop_dict, dict) and prop_dict["proposal_id"] == str(prop.proposal_id)
    assert isinstance(evo_dict, dict) and evo_dict["evolved"] is True


def test_self_improvement_service_get_cycle_summary() -> None:
    service = SelfImprovementServiceLayer()
    summary = service.get_cycle_summary([AgentResult(True, "ok")])
    assert isinstance(summary, dict)
    assert "reflection_analysis" in summary
    assert "performance_trend" in summary
    assert "controlled_experiment" in summary
    assert "improvement_proposal" in summary
    assert "brain_evolution" in summary
    assert summary["brain_evolution"]["evolved"] is True


class FakeAgent:
    name = "architect"

    def run(self, context: AgentExecutionContext):
        return AgentResult(
            success=True,
            message="Architecture completed.",
            data={"agent": "architect", "architecture_plan": "plan"},
        )


class FakeExecutionService:
    def execute(self, agent, context):
        return agent.run(context)


def test_orchestrator_integrates_self_improvement() -> None:
    orchestrator = AgentOrchestrator(execution_service=FakeExecutionService())  # type: ignore[arg-type]
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Test Self Improvement in Orchestrator",
        task_title="Test Task",
        metadata={},
    )
    results = orchestrator.execute_pipeline([FakeAgent()], context)  # type: ignore[list-item]
    assert len(results) == 1
    assert "self_improvement_report" in context.metadata
    report = context.metadata["self_improvement_report"]
    assert report["brain_evolution"]["evolved"] is True
    assert report["reflection_analysis"]["success_ratio"] == 1.0

