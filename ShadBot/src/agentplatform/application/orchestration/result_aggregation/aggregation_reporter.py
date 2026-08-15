"""
ShadBot Agent Platform

Aggregation Reporter component for 6.5 Result Aggregation.
"""

from __future__ import annotations

from .final_result_builder import AggregatedResultPackage


class AggregationReporter:
    """
    Formats an aggregated result package into an enterprise summary report.
    """

    def report(self, package: AggregatedResultPackage) -> str:
        status = "PASSED" if package.success else "FAILED"
        lines = [
            f"=== Aggregation Report ({status}) ===",
            f"ID: {package.aggregation_id}",
            f"Success Ratio: {package.evaluation.success_ratio * 100}%",
            f"Message: {package.message}",
            f"Conflicts: {package.conflict_report.resolved_notes}",
        ]
        return "\n".join(lines)
