"""
ShadBot Agent Platform

Brain context adapter.
"""

from __future__ import annotations

from agentplatform.domain.context import (
    AgentExecutionContext,
    BrainContext,
)


class BrainContextAdapter:
    """
    Converts runtime execution context
    into cognitive brain context.
    """

    def adapt(
        self,
        execution_context: AgentExecutionContext,
        brain_context: BrainContext,
    ) -> BrainContext:
        """
        Merge runtime and cognitive context.
        """

        return BrainContext(
            project_id=execution_context.project_id,
            project_intelligence=(brain_context.project_intelligence),
            memory_context=(
                execution_context.memory_context or brain_context.memory_context
            ),
            goal_context=(brain_context.goal_context),
            attention_context=(brain_context.attention_context),
            planning_context=(brain_context.planning_context),
            reasoning_context=(brain_context.reasoning_context),
            decision_context=(brain_context.decision_context),
            reflection_context=(brain_context.reflection_context),
            validation_context=(brain_context.validation_context),
            profile_context=(brain_context.profile_context),
            learning_context=(brain_context.learning_context),
        )
