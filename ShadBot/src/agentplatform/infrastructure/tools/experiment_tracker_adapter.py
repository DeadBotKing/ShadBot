"""
ShadBot Agent Platform

Experiment tracker adapter.
"""

from __future__ import annotations

from agentplatform.domain.experiments import (
    ExperimentRecord,
)
from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .experiment_tracker import (
    ExperimentTracker,
)


class ExperimentTrackerAdapter(ToolContract):
    """
    Adapter for experiment tracking.
    """

    def __init__(self) -> None:
        self._tracker = ExperimentTracker()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.EXPERIMENT_TRACKING

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        parameters_raw = payload.get(
            "parameters",
            {},
        )

        if not isinstance(
            parameters_raw,
            dict,
        ):
            parameters_raw = {}

        metrics_raw = payload.get(
            "metrics",
            {},
        )

        if not isinstance(
            metrics_raw,
            dict,
        ):
            metrics_raw = {}

        record = ExperimentRecord(
            name=str(
                payload.get(
                    "name",
                    "",
                ),
            ),
            hypothesis=str(
                payload.get(
                    "hypothesis",
                    "",
                ),
            ),
            parameters=parameters_raw,
            metrics={str(key): float(value) for key, value in metrics_raw.items()},
            result=str(
                payload.get(
                    "result",
                    "",
                ),
            ),
        )

        return self._tracker.execute(
            record,
        )
