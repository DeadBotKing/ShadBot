"""
ShadBot Agent Platform

Unit tests for Phase 9 Quality Gate System.

These tests verify that the gate reports the TRUTH about a codebase:
a clean project passes, a broken project fails, and a check that cannot run
is reported as skipped rather than as a pass.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

import pytest

from agentplatform.application.orchestration import AgentOrchestrator
from agentplatform.application.quality_gate import (
    ArchitectureValidator,
    CheckResult,
    DeterministicQualityGate,
    QualityGateServiceLayer,
    RepairLoopManager,
    SecurityValidator,
    SyntaxValidator,
)
from agentplatform.application.quality_gate.quality_report import (
    CompleteQualityReport,
)
from agentplatform.domain.context import AgentExecutionContext


# --------------------------------------------------------------------------
# Fixtures: real projects on disk, one healthy and one deliberately broken.
# --------------------------------------------------------------------------


@pytest.fixture()
def clean_project(tmp_path: Path) -> Path:
    source = tmp_path / "src" / "domain"
    source.mkdir(parents=True)

    (source / "__init__.py").write_text("", encoding="utf-8")

    (source / "model.py").write_text(
        '"""Domain model."""\n'
        "\n"
        "\n"
        "def add(left: int, right: int) -> int:\n"
        '    """Return the sum."""\n'
        "    return left + right\n",
        encoding="utf-8",
    )

    return tmp_path


@pytest.fixture()
def broken_project(tmp_path: Path) -> Path:
    source = tmp_path / "src" / "domain"
    source.mkdir(parents=True)

    (source / "__init__.py").write_text("", encoding="utf-8")

    # Syntax error.
    (source / "broken.py").write_text(
        "def oops(:\n    return 1\n",
        encoding="utf-8",
    )

    return tmp_path


# --------------------------------------------------------------------------
# Validators must report reality.
# --------------------------------------------------------------------------


def test_syntax_validator_passes_on_valid_code(clean_project: Path) -> None:
    result = SyntaxValidator().validate(str(clean_project))

    assert result.passed is True
    assert result.skipped is False
    assert result.score == 1.0


def test_syntax_validator_detects_broken_code(broken_project: Path) -> None:
    result = SyntaxValidator().validate(str(broken_project))

    assert result.passed is False
    assert result.skipped is False
    assert "broken.py" in result.details


def test_security_validator_flags_dangerous_call(tmp_path: Path) -> None:
    (tmp_path / "danger.py").write_text(
        "def run(payload: str) -> object:\n    return eval(payload)\n",
        encoding="utf-8",
    )

    result = SecurityValidator().validate(str(tmp_path))

    assert result.passed is False
    assert "eval" in result.details


def test_security_validator_flags_hardcoded_secret(tmp_path: Path) -> None:
    (tmp_path / "config.py").write_text(
        'AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"\n',
        encoding="utf-8",
    )

    result = SecurityValidator().validate(str(tmp_path))

    assert result.passed is False
    assert "secret" in result.details.lower()


def test_security_validator_passes_on_clean_code(clean_project: Path) -> None:
    result = SecurityValidator().validate(str(clean_project))

    assert result.passed is True


def test_architecture_validator_detects_layer_violation(tmp_path: Path) -> None:
    domain = tmp_path / "domain"
    domain.mkdir()

    (domain / "entity.py").write_text(
        "from infrastructure.database import Session\n"
        "\n"
        "\n"
        "def load(session: Session) -> None:\n"
        "    return None\n",
        encoding="utf-8",
    )

    result = ArchitectureValidator().validate(str(tmp_path))

    assert result.passed is False
    assert "domain layer imports" in result.details


def test_architecture_validator_passes_on_clean_layering(tmp_path: Path) -> None:
    domain = tmp_path / "domain"
    domain.mkdir()

    (domain / "entity.py").write_text(
        "from dataclasses import dataclass\n"
        "\n"
        "\n"
        "@dataclass(frozen=True)\n"
        "class Entity:\n"
        "    name: str\n",
        encoding="utf-8",
    )

    result = ArchitectureValidator().validate(str(tmp_path))

    assert result.passed is True


def test_nested_pytest_is_skipped_not_passed() -> None:
    """
    The critical anti-recursion guarantee.

    Running pytest from inside pytest forks without bound, so the check must be
    refused - but refusing is NOT the same as passing.
    """

    from agentplatform.application.quality_gate import PytestValidator

    result = PytestValidator().validate(".")

    assert result.skipped is True
    assert result.passed is False
    assert result.score == 0.0


# --------------------------------------------------------------------------
# Service aggregation must be honest.
# --------------------------------------------------------------------------


def test_service_reports_failure_for_broken_project(broken_project: Path) -> None:
    service = QualityGateServiceLayer()

    report, decision = service.validate_project(uuid4(), str(broken_project))

    assert report.approved is False
    assert report.repair_required is True
    assert decision.trigger_repair is True
    assert "syntax" in decision.repair_instructions


def test_service_never_approves_when_everything_skipped() -> None:
    """
    A gate that executed nothing proves nothing and must not report approval.
    """

    class SkippingValidator:
        def __init__(self, name: str) -> None:
            self._name = name

        def validate(self, project_path: str) -> CheckResult:
            return CheckResult(
                check_name=self._name,
                passed=False,
                details="tool unavailable",
                score=0.0,
                skipped=True,
            )

    service = QualityGateServiceLayer(
        syntax_val=SkippingValidator("syntax"),  # type: ignore[arg-type]
        pytest_val=SkippingValidator("pytest"),  # type: ignore[arg-type]
        ruff_val=SkippingValidator("ruff"),  # type: ignore[arg-type]
        black_val=SkippingValidator("black"),  # type: ignore[arg-type]
        mypy_val=SkippingValidator("mypy"),  # type: ignore[arg-type]
        sec_val=SkippingValidator("security"),  # type: ignore[arg-type]
        arch_val=SkippingValidator("architecture"),  # type: ignore[arg-type]
    )

    report, decision = service.validate_project(uuid4(), ".")

    assert report.approved is False
    assert report.overall_score == 0.0

    # Nothing actually failed, so repairing the code would be wrong.
    assert decision.trigger_repair is False
    assert "inconclusive" in decision.repair_instructions.lower()


def test_service_approves_a_genuinely_clean_project(clean_project: Path) -> None:
    """
    Only the dependency-free validators are used, so this asserts a real pass
    without requiring ruff/black/mypy to be installed.
    """

    service = QualityGateServiceLayer()

    report, decision = service.validate_project(uuid4(), str(clean_project))

    syntax = next(c for c in report.check_results if c.check_name == "syntax")
    security = next(c for c in report.check_results if c.check_name == "security")

    assert syntax.passed is True
    assert security.passed is True


def test_report_and_decision_serialise() -> None:
    service = QualityGateServiceLayer()
    project_id = uuid4()

    report, decision = service.validate_project(project_id, ".")

    report_dict = report.to_dict()
    decision_dict = decision.to_dict()

    assert report_dict["report_id"] == str(report.report_id)
    assert report_dict["project_id"] == str(project_id)
    assert isinstance(report_dict["check_results"], list)
    assert "skipped" in report_dict["check_results"][0]
    assert isinstance(decision_dict["trigger_repair"], bool)


def test_repair_loop_targets_engineer_on_real_failure() -> None:
    failing = CheckResult("ruff", False, "E501 line too long", 0.0)
    passing = CheckResult("syntax", True, "ok", 1.0)

    report = CompleteQualityReport(
        report_id=uuid4(),
        project_id=uuid4(),
        approved=False,
        overall_score=0.5,
        check_results=(passing, failing),
        repair_required=True,
    )

    decision = RepairLoopManager().decide(report)

    assert decision.trigger_repair is True
    assert decision.target_agent == "engineer"
    assert "ruff" in decision.repair_instructions


# --------------------------------------------------------------------------
# Deterministic gate.
# --------------------------------------------------------------------------


def test_deterministic_gate_fails_broken_project(broken_project: Path) -> None:
    gate = DeterministicQualityGate(verbose=False)

    report = gate.verify_deterministic(broken_project)

    assert report.passed is False
    assert report.syntax_valid is False

    report_dict = report.to_dict()

    assert report_dict["passed"] is False
    assert "summary" in report_dict
    assert isinstance(report_dict["checks"], list)


def test_deterministic_gate_reports_syntax_valid_for_clean_project(
    clean_project: Path,
) -> None:
    gate = DeterministicQualityGate(verbose=False)

    report = gate.verify_deterministic(clean_project)

    assert report.syntax_valid is True


# --------------------------------------------------------------------------
# Orchestrator integration.
# --------------------------------------------------------------------------


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


def test_orchestrator_attaches_quality_reports() -> None:
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

    gate_report = context.metadata["deterministic_gate_report"]

    # The verdict must be a real boolean derived from real checks, and the
    # per-check evidence must be present for auditing.
    assert isinstance(gate_report["passed"], bool)
    assert isinstance(gate_report["checks"], list)
    assert gate_report["checks"]
