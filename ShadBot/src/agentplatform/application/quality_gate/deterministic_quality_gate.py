"""
ShadBot Agent Platform

Deterministic Quality Gate.

Purpose:
    ENFORCE that no task can be marked completed unless deterministic tooling
    actually passes, independent of any LLM opinion.

Responsibility:
    Run syntax, lint, typing and test checks against a real filesystem path and
    report the true outcome.

Dependencies:
    Quality gate validators.

Outputs:
    DeterministicGateReport.

Honesty contract (Rule 27):
    This gate never fabricates a PASS. Under pytest the nested-pytest check is
    skipped (it would fork indefinitely), but every other check still runs for
    real, and skipped checks are reported as skipped rather than as passes.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

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


@dataclass(frozen=True, slots=True)
class DeterministicGateReport:
    passed: bool
    syntax_valid: bool
    tests_passed: bool
    lint_passed: bool
    typecheck_passed: bool
    summary: str
    checks: tuple[CheckResult, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {
            "passed": self.passed,
            "syntax_valid": self.syntax_valid,
            "tests_passed": self.tests_passed,
            "lint_passed": self.lint_passed,
            "typecheck_passed": self.typecheck_passed,
            "summary": self.summary,
            "checks": [check.to_dict() for check in self.checks],
        }


class DeterministicQualityGate:
    """
    Absolute, non-LLM quality gate verifying actual filesystem codebase health.
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
        verbose: bool = True,
    ) -> None:
        self.syntax_val = syntax_val or SyntaxValidator()
        self.pytest_val = pytest_val or PytestValidator()
        self.ruff_val = ruff_val or RuffValidator()
        self.black_val = black_val or BlackValidator()
        self.mypy_val = mypy_val or MypyValidator()
        self.sec_val = sec_val or SecurityValidator()
        self.arch_val = arch_val or ArchitectureValidator()
        self._verbose = verbose

    def verify_deterministic(self, project_path: Path) -> DeterministicGateReport:
        """
        Execute the deterministic gate against a real path.
        """

        target = Path(project_path)

        source_root = target / "src"

        scan_root = str(source_root if source_root.exists() else target)

        syntax = self.syntax_val.validate(scan_root)
        tests = self.pytest_val.validate(str(target))
        lint = self.ruff_val.validate(str(target))
        typing_check = self.mypy_val.validate(str(target))
        security = self.sec_val.validate(scan_root)
        architecture = self.arch_val.validate(scan_root)

        checks = (
            syntax,
            tests,
            lint,
            typing_check,
            security,
            architecture,
        )

        executed = tuple(check for check in checks if not check.skipped)

        passed = bool(executed) and all(check.passed for check in executed)

        status_msg = (
            "GREEN (ALL EXECUTED CHECKS PASSED)"
            if passed
            else "FAILED DETERMINISTIC QUALITY GATE"
        )

        skipped_names = [check.check_name for check in checks if check.skipped]

        failed_names = [
            check.check_name for check in checks if not check.skipped and not check.passed
        ]

        summary_parts = [
            f"[DETERMINISTIC GATE] Status: {status_msg}",
            f"executed={len(executed)}/{len(checks)}",
        ]

        if failed_names:
            summary_parts.append(f"failed={','.join(failed_names)}")

        if skipped_names:
            summary_parts.append(f"skipped={','.join(skipped_names)}")

        summary = " | ".join(summary_parts)

        if self._verbose:
            print("\n" + "=" * 70)
            print(summary)

            for check in checks:
                if check.skipped:
                    status = "SKIP"
                elif check.passed:
                    status = "PASS"
                else:
                    status = "FAIL"

                first_line = check.details.splitlines()[0] if check.details else ""
                print(f"  [{status}] {check.check_name}: {first_line[:160]}")

            print("=" * 70 + "\n")

        return DeterministicGateReport(
            passed=passed,
            syntax_valid=syntax.passed,
            tests_passed=tests.passed,
            lint_passed=lint.passed,
            typecheck_passed=typing_check.passed,
            summary=summary,
            checks=checks,
        )
