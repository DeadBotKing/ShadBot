"""
ShadBot Agent Platform

Hyperparameter search tool.
"""

from __future__ import annotations

from agentplatform.domain.experiments import (
    HyperparameterExperiment,
)


class HyperparameterSearchTool:
    """
    Designs hyperparameter experiments.
    """

    def execute(
        self,
        model_name: str,
        parameters: dict[str, object],
        metric: str,
    ) -> HyperparameterExperiment:
        """
        Create experiment definition.
        """

        return HyperparameterExperiment(
            model_name=model_name,
            parameters=parameters,
            expected_metric=metric,
            notes="Experiment created for optimization loop.",
        )
