"""
ShadBot Agent Platform

Unit tests for Phase 9 Quality Gate System.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4
from agentplatform.application.orchestration import AgentOrchestrator
from agentplatform.application.quality_gate import (
    ArchitectureValidator,
    BlackValidator,
    DeterministicQualityGate,
    MypyValidator,
    PytestValidator,
    QualityGateServiceLayer,
    RepairLoopManager,
    RuffValidator,
    SecurityValidator,
)
from agentplatform.domain.context import AgentExecutionContext


def test_individual_validators_pass() -> None:
    assert PytestValidator().validate(".").passed is True
    assert RuffValidator().validate(".").passed is True
    assert BlackValidator().validate(".").passed is True
    assert MypyValidator().validate(".").passed is True
    assert SecurityValidator().validate(".").passed is True
    assert ArchitectureValidator().validate(".").passed is True


def test_repair_loop_manager_decides() -> None:
    service = QualityGateServiceLayer()
    rep, dec = service.validate_project(uuid4(), ".")
    assert rep.approved is True
    assert dec.trigger_repair is False


def test_quality_gate_service_orchestrates_all() -> None:
    service = QualityGateServiceLayer()
    pid = uuid4()
    rep, dec = service.validate_project(pid, ".")
    assert rep.project_id == pid
    assert rep.overall_score == 1.0
    assert len(rep.check_results) == 6


def test_deterministic_quality_gate_and_report_to_dict() -> None:
    gate = DeterministicQualityGate()
    report = gate.verify_deterministic(Path("."))
    assert report.passed is True
    assert report.syntax_valid is True
    assert report.tests_passed is True
    report_dict = report.to_dict()
    assert isinstance(report_dict, dict)
    assert report_dict["passed"] is True
    assert "summary" in report_dict


def test_quality_report_and_check_result_to_dict() -> None:
    service = QualityGateServiceLayer()
    pid = uuid4()
    rep, dec = service.validate_project(pid, ".")
    rep_dict = rep.to_dict()
    dec_dict = dec.to_dict()
    assert isinstance(rep_dict, dict)
    assert isinstance(dec_dict, dict)
    assert rep_dict["report_id"] == str(rep.report_id)
    assert rep_dict["project_id"] == str(pid)
    assert isinstance(rep_dict["check_results"], list)
    assert dec_dict["trigger_repair"] is False


class FakeAgent:
    name = "architect"

    def run(self, context: AgentExecutionContext):
        from agentplatform.domain.results import AgentResult

        return AgentResult(
            success=True,
            message="Architecture completed.",
            data={"agent": "architect", "architecture_plan": "plan"},
        )


class FakeExecutionService:
    def execute(self, agent, context):
        return agent.run(context)


def test_orchestrator_integrates_quality_gate() -> None:
    orchestrator = AgentOrchestrator(execution_service=FakeExecutionService())  # type: ignore[arg-type]
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Test Quality Gate in Orchestrator",
        task_title="Test Task",
        metadata={},
    )
    results = orchestrator.execute_pipeline([FakeAgent()], context)  # type: ignore[list-item]
    assert len(results) == 1
    assert "deterministic_gate_report" in context.metadata
    assert "quality_gate_report" in context.metadata
    assert context.metadata["deterministic_gate_report"]["passed"] is True
    assert context.metadata["quality_gate_report"]["approved"] is True

