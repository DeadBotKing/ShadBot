"""
ShadBot Agent Platform

Improvement loop adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .improvement_loop_tool import (
    ImprovementLoopTool,
)


class ImprovementLoopAdapter(ToolContract):
    """
    Adapter for ML improvement loop.
    """

    def __init__(self) -> None:
        self._tool = ImprovementLoopTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.MODEL_EVALUATION

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        iteration_value = payload.get(
            "iteration",
            1,
        )

        previous_score_value = payload.get(
            "previous_score",
            0,
        )

        current_score_value = payload.get(
            "current_score",
            0,
        )

        iteration = (
            int(iteration_value)
            if isinstance(
                iteration_value,
                (int, str),
            )
            else 1
        )

        previous_score = (
            float(previous_score_value)
            if isinstance(
                previous_score_value,
                (int, float, str),
            )
            else 0.0
        )

        current_score = (
            float(current_score_value)
            if isinstance(
                current_score_value,
                (int, float, str),
            )
            else 0.0
        )

        result = self._tool.execute(
            str(
                payload.get(
                    "model_name",
                    "",
                ),
            ),
            iteration,
            previous_score,
            current_score,
        )

        return {
            "id": str(result.id),
            "model_name": result.model_name,
            "iteration": result.iteration,
            "improved": result.improved,
            "decision": result.decision,
        }
