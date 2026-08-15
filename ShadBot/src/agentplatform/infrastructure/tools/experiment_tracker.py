"""
ShadBot Agent Platform

Experiment tracker tool.
"""

from __future__ import annotations

from agentplatform.domain.experiments import ExperimentRecord


class ExperimentTracker:
    """
    Track experiments and results.
    """

    def __init__(self) -> None:
        self._experiments: list[ExperimentRecord] = []

    def execute(
        self,
        record: ExperimentRecord,
    ) -> dict[str, object]:
        """
        Store experiment result.
        """

        self._experiments.append(
            record,
        )

        return {
            "experiment_id": str(
                record.id,
            ),
            "stored": True,
            "count": len(
                self._experiments,
            ),
        }

    def history(self) -> list[ExperimentRecord]:
        """
        Return experiment history.
        """

        return list(
            self._experiments,
        )
