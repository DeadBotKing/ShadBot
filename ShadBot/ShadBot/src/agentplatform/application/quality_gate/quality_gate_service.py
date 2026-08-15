"""
ShadBot Agent Platform

Unified Quality Gate Service for Phase 9 Quality Gate System.

Purpose:
    Run every deterministic quality validator against a project and produce a
    truthful, auditable verdict.

Responsibility:
    Aggregation and scoring only. Each individual verdict is owned by its
    validator.

Dependencies:
    Quality gate validators, quality report model, repair loop manager.

Outputs:
    CompleteQualityReport plus a RepairLoopDecision.

Honesty contract (Rule 27):
    - A check that could not run is reported as skipped, never as a pass.
    - `approved` is True only when at least one check executed AND every
      executed check passed.
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
    SyntaxValidator,
)


class QualityGateServiceLayer:
    """
    Orchestrates syntax, testing, linting, formatting, static typing, security,
    and architecture validation.
    """

    def __init__(
        self,
        syntax_val: SyntaxValidator | None = None,
        pytest_val: PytestValidator | None = None,
        ruff_val: RuffValidator | None = None,
        black_val: BlackValidator | None = None,
        mypy_val: MypyValidator | None = None,
        sec_val: SecurityValidator | None = None,
        arch_val: ArchitectureValidator | None = None,
        repair_mgr: RepairLoopManager | None = None,
    ) -> None:
        self.syntax_val = syntax_val or SyntaxValidator()
        self.pytest_val = pytest_val or PytestValidator()
        self.ruff_val = ruff_val or RuffValidator()
        self.black_val = black_val or BlackValidator()
        self.mypy_val = mypy_val or MypyValidator()
        self.sec_val = sec_val or SecurityValidator()
        self.arch_val = arch_val or ArchitectureValidator()
        self.repair_mgr = repair_mgr or RepairLoopManager()

    def validate_project(
        self,
        project_id: UUID,
        project_path: str,
    ) -> tuple[CompleteQualityReport, RepairLoopDecision]:
        """
        Execute every quality check and aggregate a truthful report.
        """

        checks: tuple[CheckResult, ...] = (
            self.syntax_val.validate(project_path),
            self.pytest_val.validate(project_path),
            self.ruff_val.validate(project_path),
            self.black_val.validate(project_path),
            self.mypy_val.validate(project_path),
            self.sec_val.validate(project_path),
            self.arch_val.validate(project_path),
        )

        executed = tuple(check for check in checks if not check.skipped)

        # An empty gate proves nothing, so it must not be reported as approved.
        approved = bool(executed) and all(check.passed for check in executed)

        overall_score = (
            round(sum(check.score for check in executed) / len(executed), 2)
            if executed
            else 0.0
        )

        report = CompleteQualityReport(
            report_id=uuid4(),
            project_id=project_id,
            approved=approved,
            overall_score=overall_score,
            check_results=checks,
            repair_required=not approved,
        )

        decision = self.repair_mgr.decide(report)

        return report, decision

    def format_summary(self, report: CompleteQualityReport) -> str:
        """
        Render a human readable audit line per check.
        """

        lines = [
            f"QUALITY GATE | approved={report.approved} "
            f"score={report.overall_score}",
        ]

        for check in report.check_results:
            if check.skipped:
                status = "SKIP"
            elif check.passed:
                status = "PASS"
            else:
                status = "FAIL"

            lines.append(f"  [{status}] {check.check_name}: {check.details.splitlines()[0][:160]}")

        return "\n".join(lines)
