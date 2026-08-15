"""
ShadBot Agent Platform

Retraining tool adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .retraining_tool import (
    RetrainingTool,
)


class RetrainingToolAdapter(ToolContract):
    """
    Adapter for model retraining.
    """

    def __init__(self) -> None:
        self._tool = RetrainingTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.MODEL_TRAINING

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        epochs_value = payload.get(
            "epochs",
            1,
        )

        epochs = (
            int(epochs_value)
            if isinstance(
                epochs_value,
                (int, str),
            )
            else 1
        )

        result = self._tool.execute(
            str(
                payload.get(
                    "model_name",
                    "",
                ),
            ),
            epochs,
        )

        return {
            "id": str(result.id),
            "model_name": result.model_name,
            "success": result.success,
            "epochs": result.epochs,
            "message": result.message,
        }
