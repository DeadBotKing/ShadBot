"""
ShadBot Agent Platform

Unit tests for Phase 12 Production Freeze V1.0.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.orchestration import AgentOrchestrator
from agentplatform.application.release import (
    ArchitectureFreezeManager,
    ContractFreezeManager,
    FullIntegrationVerifier,
    ProductionGovernanceManager,
    ProductionReleaseService,
)
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult


def test_full_integration_verifier_checks_phases() -> None:
    rep = FullIntegrationVerifier().verify_all()
    assert rep.all_systems_operational is True
    assert len(rep.verified_phases) == 12


def test_architecture_and_contract_freeze() -> None:
    arch = ArchitectureFreezeManager().freeze()
    cont = ContractFreezeManager().freeze_contracts()
    assert arch.is_frozen is True
    assert cont.is_frozen is True
    assert "AgentContract" in cont.frozen_contracts


def test_production_release_service_releases_v1() -> None:
    service = ProductionReleaseService()
    pkg = service.execute_release_freeze()
    assert pkg.is_production_ready is True
    assert pkg.version == "1.0.0-Enterprise-Production"
    assert "1.0-Enterprise" in pkg.governance.governance_version


def test_release_models_to_dict() -> None:
    arch = ArchitectureFreezeManager().freeze()
    cont = ContractFreezeManager().freeze_contracts()
    integ = FullIntegrationVerifier().verify_all()
    gov = ProductionGovernanceManager().establish()
    service = ProductionReleaseService()
    pkg = service.execute_release_freeze()

    assert isinstance(arch.to_dict(), dict) and arch.to_dict()["is_frozen"] is True
    assert isinstance(cont.to_dict(), dict) and "AgentContract" in cont.to_dict()["frozen_contracts"]
    assert isinstance(integ.to_dict(), dict) and integ.to_dict()["all_systems_operational"] is True
    assert isinstance(gov.to_dict(), dict) and gov.to_dict()["governance_version"] == "1.0-Enterprise"
    pkg_dict = pkg.to_dict()
    assert isinstance(pkg_dict, dict)
    assert pkg_dict["release_id"] == str(pkg.release_id)
    assert pkg_dict["is_production_ready"] is True


def test_release_service_get_release_summary() -> None:
    service = ProductionReleaseService()
    summary = service.get_release_summary()
    assert isinstance(summary, dict)
    assert summary["is_production_ready"] is True
    assert summary["version"] == "1.0.0-Enterprise-Production"
    assert "arch_freeze" in summary
    assert "contract_freeze" in summary
    assert "governance" in summary
    assert "integration_report" in summary


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


def test_orchestrator_integrates_production_release() -> None:
    orchestrator = AgentOrchestrator(execution_service=FakeExecutionService())  # type: ignore[arg-type]
    context = AgentExecutionContext(
        project_id=uuid4(),
        task_id=uuid4(),
        instructions="Test Production Release in Orchestrator",
        task_title="Test Task",
        metadata={},
    )
    results = orchestrator.execute_pipeline([FakeAgent()], context)  # type: ignore[list-item]
    assert len(results) == 1
    assert "production_release_report" in context.metadata
    report = context.metadata["production_release_report"]
    assert report["is_production_ready"] is True
    assert report["version"] == "1.0.0-Enterprise-Production"
    assert report["arch_freeze"]["is_frozen"] is True
    assert report["contract_freeze"]["is_frozen"] is True

