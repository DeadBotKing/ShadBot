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
            return RepairLoopDecision(False, "none", "Quality Gate passed; no repair required.")
        failed = [c.check_name for c in report.check_results if not c.passed]
        return RepairLoopDecision(
            trigger_repair=True,
            target_agent="engineer",
            repair_instructions=f"Fix failing quality checks: {', '.join(failed)}",
        )
