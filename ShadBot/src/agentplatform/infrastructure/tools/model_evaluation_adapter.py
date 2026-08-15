"""
ShadBot Agent Platform

Model evaluation adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .model_evaluation_tool import (
    ModelEvaluationTool,
)


class ModelEvaluationAdapter(ToolContract):
    """
    Adapter for model evaluation.
    """

    def __init__(self) -> None:
        self._tool = ModelEvaluationTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.MODEL_EVALUATION

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        metrics_raw = payload.get(
            "metrics",
            {},
        )

        if not isinstance(
            metrics_raw,
            dict,
        ):
            metrics_raw = {}

        result = self._tool.execute(
            str(
                payload.get(
                    "model_name",
                    "",
                ),
            ),
            {str(key): float(value) for key, value in metrics_raw.items()},
        )

        return {
            "model_name": result.model_name,
            "metrics": result.metrics,
            "issues": result.issues,
            "recommendation": result.recommendation,
        }
