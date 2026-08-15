"""
ShadBot Agent Platform

ML Scientist Agent Ability
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.agents import (
    RuntimeAgent,
)
from agentplatform.application.capabilities import (
    CapabilityExecutor,
)
from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)
from agentplatform.domain.context import (
    BrainContext,
)


@dataclass(slots=True)
class MLScientistAbility:
    """
    Built-in ability for ML Scientist agents.

    Responsible for:

    - feature engineering analysis
    - model evaluation
    - experiment execution
    - training improvement analysis
    - ML research workflows

    This ability improves ML systems.
    It does not directly own model implementation.
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.ML_SCIENTIST

    CAPABILITIES = frozenset(
        {
            AgentCapability.FEATURE_ENGINEERING,
            AgentCapability.MODEL_EVALUATION,
        }
    )

    def supports(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Check capability support.
        """

        return capability in self.CAPABILITIES

    def analyze_features(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute feature engineering analysis.
        """

        return self.executor.execute(
            capability=AgentCapability.FEATURE_ENGINEERING,
            agent=agent,
            context=context,
        )

    def evaluate_model(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute model evaluation.
        """

        return self.executor.execute(
            capability=AgentCapability.MODEL_EVALUATION,
            agent=agent,
            context=context,
        )

    def run_analysis_cycle(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> dict[str, object]:
        """
        Execute ML scientist analysis workflow.

        Includes:
        - feature analysis
        - model evaluation
        """

        feature_analysis = self.analyze_features(
            agent=agent,
            context=context,
        )

        model_evaluation = self.evaluate_model(
            agent=agent,
            context=context,
        )

        return {
            "feature_analysis": feature_analysis,
            "model_evaluation": model_evaluation,
        }

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate ML Scientist runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
