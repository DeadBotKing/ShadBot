"""
ShadBot Agent Platform

Agent brain coordinator.
"""

from __future__ import annotations

from collections.abc import Sequence
from uuid import UUID

from agentplatform.application.brain.brain_decision import (
    BrainDecision,
)
from agentplatform.application.brain.brain_planning import (
    BrainPlanning,
)
from agentplatform.application.brain.brain_profile import (
    BrainProfile,
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
from agentplatform.application.context import (
    BrainContextFactory,
)
from agentplatform.application.decision import (
    DecisionResult,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.context import (
    BrainContext,
)
from agentplatform.domain.planning import (
    ExecutionPlan,
    PlanningRequest,
)
from agentplatform.domain.results import (
    AgentResult,
)


class AgentBrain:
    """
    Main cognitive coordinator.
    """

    def __init__(
        self,
        reasoning: BrainReasoning,
        context_factory: BrainContextFactory,
        planning: BrainPlanning | None = None,
        reflection: BrainReflection | None = None,
        decision: BrainDecision | None = None,
        validation: BrainValidation | None = None,
        profile: BrainProfile | None = None,
    ) -> None:

        self._reasoning = reasoning
        self._context_factory = context_factory
        self._planning = planning or BrainPlanning()
        self._reflection = reflection or BrainReflection()
        self._decision = decision or BrainDecision()
        self._validation = validation or BrainValidation()
        self._profile = profile

    def build_context(
        self,
        project_id: UUID,
    ) -> BrainContext:
        """
        Create cognitive context.
        """

        return self._context_factory.create(
            project_id,
        )

    def think(
        self,
        role: AgentRole,
        context: BrainContext,
    ) -> str:
        """
        Execute reasoning using full brain context.
        """

        return self._reasoning.reason(
            role,
            context,
        )

    def plan(
        self,
        request: PlanningRequest,
    ) -> ExecutionPlan:
        """
        Create execution plan.
        """

        return self._planning.plan(
            request,
        )

    def reflect(
        self,
        results: list[AgentResult],
    ) -> dict[str, object]:

        return self._reflection.reflect(
            results,
        )

    def decide(
        self,
        results: Sequence[AgentResult],
    ) -> DecisionResult:

        return self._decision.decide(
            results,
        )

    def validate(
        self,
        results: list[AgentResult],
    ) -> dict[str, object]:

        return self._validation.validate(
            results,
        )

    @property
    def profile(
        self,
    ) -> BrainProfile | None:

        return self._profile
