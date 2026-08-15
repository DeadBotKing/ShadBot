"""
ShadBot Agent Platform

Unified Quality Gate Service for Phase 9 Quality Gate System.
"""

from __future__ import annotations

from uuid import UUID, uuid4
from .quality_report import CompleteQualityReport
from .repair_loop import RepairLoopDecision, RepairLoopManager
from .validators import (
    ArchitectureValidator,
    BlackValidator,
    CheckResult,
    MypyValidator,
    PytestValidator,
    RuffValidator,
    SecurityValidator,
)


class QualityGateServiceLayer:
    """
    Orchestrates unit testing, linting, formatting, static typing, security, and architecture validation.
    """

    def __init__(
        self,
        pytest_val: PytestValidator | None = None,
        ruff_val: RuffValidator | None = None,
        black_val: BlackValidator | None = None,
        mypy_val: MypyValidator | None = None,
        sec_val: SecurityValidator | None = None,
        arch_val: ArchitectureValidator | None = None,
        repair_mgr: RepairLoopManager | None = None,
    ) -> None:
        self.pytest_val = pytest_val or PytestValidator()
        self.ruff_val = ruff_val or RuffValidator()
        self.black_val = black_val or BlackValidator()
        self.mypy_val = mypy_val or MypyValidator()
        self.sec_val = sec_val or SecurityValidator()
        self.arch_val = arch_val or ArchitectureValidator()
        self.repair_mgr = repair_mgr or RepairLoopManager()

    def validate_project(self, project_id: UUID, project_path: str) -> tuple[CompleteQualityReport, RepairLoopDecision]:
        checks = (
            self.pytest_val.validate(project_path),
            self.ruff_val.validate(project_path),
            self.black_val.validate(project_path),
            self.mypy_val.validate(project_path),
            self.sec_val.validate(project_path),
            self.arch_val.validate(project_path),
        )
        approved = all(c.passed for c in checks)
        avg_score = round(sum(c.score for c in checks) / len(checks), 2)
        report = CompleteQualityReport(
            report_id=uuid4(),
            project_id=project_id,
            approved=approved,
            overall_score=avg_score,
            check_results=checks,
            repair_required=not approved,
        )
        decision = self.repair_mgr.decide(report)
        return report, decision
