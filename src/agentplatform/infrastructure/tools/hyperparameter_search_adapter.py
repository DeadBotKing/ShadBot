"""
ShadBot Agent Platform

Hyperparameter search adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .hyperparameter_search_tool import (
    HyperparameterSearchTool,
)


class HyperparameterSearchAdapter(ToolContract):
    """
    Adapter for hyperparameter experiments.
    """

    def __init__(self) -> None:
        self._tool = HyperparameterSearchTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.EXPERIMENT_DESIGN

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        parameters = payload.get(
            "parameters",
            {},
        )

        if not isinstance(
            parameters,
            dict,
        ):
            parameters = {}

        result = self._tool.execute(
            str(
                payload.get(
                    "model_name",
                    "",
                ),
            ),
            parameters,
            str(
                payload.get(
                    "metric",
                    "accuracy",
                ),
            ),
        )

        return {
            "experiment_id": str(result.id),
            "model_name": result.model_name,
            "parameters": result.parameters,
            "metric": result.expected_metric,
            "notes": result.notes,
        }
