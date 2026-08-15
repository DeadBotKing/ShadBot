"""
ShadBot Agent Platform

Repair Loop Trigger component for Phase 9 Quality Gate System.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .quality_report import CompleteQualityReport


@dataclass(frozen=True, slots=True)
class RepairLoopDecision:
    trigger_repair: bool
    target_agent: str
    repair_instructions: str

    def to_dict(self) -> dict[str, object]:
        return {
            "trigger_repair": self.trigger_repair,
            "target_agent": self.target_agent,
            "repair_instructions": self.repair_instructions,
        }


class RepairLoopManager:
    """
    Decides whether to trigger an automatic repair loop when quality checks fail.
    """

    def decide(self, report: CompleteQualityReport) -> RepairLoopDecision:
        if report.approved:
            return RepairLoopDecision(
                False,
                "none",
                "Quality Gate passed; no repair required.",
            )

        failed = [
            check.check_name
            for check in report.check_results
            if not check.skipped and not check.passed
        ]

        skipped = [
            check.check_name for check in report.check_results if check.skipped
        ]

        if not failed:
            # Nothing actually failed: the gate proved nothing because every
            # check was skipped. Repairing code would be wrong; the environment
            # needs fixing instead.
            return RepairLoopDecision(
                trigger_repair=False,
                target_agent="none",
                repair_instructions=(
                    "Quality Gate is inconclusive: no check could be executed "
                    f"(skipped: {', '.join(skipped) or 'all'}). "
                    "Install the quality tooling before trusting this result."
                ),
            )

        instructions = f"Fix failing quality checks: {', '.join(failed)}"

        if skipped:
            instructions += f" (not verified: {', '.join(skipped)})"

        return RepairLoopDecision(
            trigger_repair=True,
            target_agent="engineer",
            repair_instructions=instructions,
        )
