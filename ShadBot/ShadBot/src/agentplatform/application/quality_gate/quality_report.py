"""
ShadBot Agent Platform

Quality Report model for Phase 9 Quality Gate System.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from .validators import CheckResult


@dataclass(frozen=True, slots=True)
class CompleteQualityReport:
    report_id: UUID
    project_id: UUID
    approved: bool
    overall_score: float
    check_results: tuple[CheckResult, ...]
    repair_required: bool
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, object]:
        return {
            "report_id": str(self.report_id),
            "project_id": str(self.project_id),
            "approved": self.approved,
            "overall_score": self.overall_score,
            "check_results": [c.to_dict() for c in self.check_results],
            "repair_required": self.repair_required,
            "timestamp": self.timestamp,
        }
