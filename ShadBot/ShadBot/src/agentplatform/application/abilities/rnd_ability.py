"""
ShadBot Agent Platform

R&D Agent Ability
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
class RNDAbility:
    """
    Built-in ability for R&D agents.

    Responsible for:

    - research exploration
    - experiment design
    - technology evaluation
    - innovation analysis
    - feasibility studies

    R&D agents explore and recommend.
    They do not directly implement production code.
    """

    executor: CapabilityExecutor

    ROLE = AgentRole.RND

    CAPABILITIES = frozenset(
        {
            AgentCapability.RESEARCH,
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

    def research(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute research exploration.
        """

        return self.executor.execute(
            capability=AgentCapability.RESEARCH,
            agent=agent,
            context=context,
        )

    def evaluate_experiment(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> object:
        """
        Execute experiment evaluation.
        """

        return self.executor.execute(
            capability=AgentCapability.MODEL_EVALUATION,
            agent=agent,
            context=context,
        )

    def run_research_cycle(
        self,
        *,
        agent: RuntimeAgent,
        context: BrainContext,
    ) -> dict[str, object]:
        """
        Execute R&D workflow.

        Includes:
        - research phase
        - experiment evaluation phase
        """

        research_result = self.research(
            agent=agent,
            context=context,
        )

        experiment_result = self.evaluate_experiment(
            agent=agent,
            context=context,
        )

        return {
            "research": research_result,
            "experiment": experiment_result,
        }

    def validate(
        self,
        agent: RuntimeAgent,
    ) -> bool:
        """
        Validate R&D runtime ability.
        """

        if agent.role != self.ROLE:
            return False

        return all(
            agent.supports(
                capability,
            )
            for capability in self.CAPABILITIES
        )
