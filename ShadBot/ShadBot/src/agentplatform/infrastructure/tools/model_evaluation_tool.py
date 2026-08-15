"""
ShadBot Agent Platform

Model evaluation tool.
"""

from __future__ import annotations

from agentplatform.domain.model_evaluation import (
    EvaluationResult,
)


class ModelEvaluationTool:
    """
    Evaluate ML model performance.
    """

    def execute(
        self,
        model_name: str,
        metrics: dict[str, float],
    ) -> EvaluationResult:
        """
        Analyze model metrics.
        """

        issues: list[str] = []

        if (
            metrics.get(
                "accuracy",
                1.0,
            )
            < 0.8
        ):
            issues.append(
                "Low accuracy detected.",
            )

        if (
            metrics.get(
                "loss",
                0.0,
            )
            > 0.5
        ):
            issues.append(
                "High loss detected.",
            )

        recommendation = "Improve model." if issues else "Model performance acceptable."

        return EvaluationResult(
            model_name=model_name,
            metrics=metrics,
            issues=issues,
            recommendation=recommendation,
        )
