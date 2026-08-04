"""
ShadBot Agent Platform

Agent brain coordinator.
"""

from __future__ import annotations

from collections.abc import Sequence

from agentplatform.application.brain.brain_decision import (
    BrainDecision,
)
from agentplatform.application.brain.brain_memory import (
    BrainMemory,
)
from agentplatform.application.brain.brain_planning import (
    BrainPlanning,
)
from agentplatform.application.brain.brain_reasoning import (
    BrainReasoning,
)
from agentplatform.application.brain.brain_reflection import (
    BrainReflection,
)
from agentplatform.application.brain.brain_validation import (
    BrainValidation,
)
from agentplatform.application.decision import (
    DecisionResult,
)
from agentplatform.application.planning import (
    AgentExecutionPlan,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tasks import (
    AgentTask,
)


class AgentBrain:
    """
    Coordinates agent cognitive capabilities.
    """

    def __init__(
        self,
        reasoning: BrainReasoning,
        planning: BrainPlanning | None = None,
        memory: BrainMemory | None = None,
        reflection: BrainReflection | None = None,
        decision: BrainDecision | None = None,
        validation: BrainValidation | None = None,
    ) -> None:
        self._reasoning = reasoning
        self._planning = planning or BrainPlanning()
        self._memory = memory
        self._reflection = reflection or BrainReflection()
        self._decision = decision or BrainDecision()
        self._validation = validation or BrainValidation()

    def think(
        self,
        role: AgentRole,
        context: AgentExecutionContext,
    ) -> str:
        """
        Execute reasoning.
        """

        return self._reasoning.reason(
            role,
            context,
        )

    def plan(
        self,
        task: AgentTask,
    ) -> AgentExecutionPlan:
        """
        Create execution plan.
        """

        return self._planning.plan(
            task,
        )

    def remember_context(
        self,
        context: AgentExecutionContext,
    ) -> dict[str, object]:
        """
        Retrieve memory context.
        """

        if self._memory is None:
            return {}

        return self._memory.retrieve(
            context,
        )

    def reflect(
        self,
        results: list[AgentResult],
    ) -> dict[str, object]:
        """
        Analyze execution.
        """

        return self._reflection.reflect(
            results,
        )

    def decide(
        self,
        results: Sequence[AgentResult],
    ) -> DecisionResult:
        """
        Decide next execution action.
        """

        return self._decision.decide(
            results,
        )

    def validate(
        self,
        results: list[AgentResult],
    ) -> dict[str, object]:
        """
        Validate execution.
        """

        return self._validation.validate(
            results,
        )
