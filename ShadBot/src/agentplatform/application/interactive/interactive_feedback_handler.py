"""
ShadBot Agent Platform

Interactive Feedback Handler service.
"""

from __future__ import annotations

from uuid import UUID, uuid4
from agentplatform.domain.interactive import InteractiveActionType
from agentplatform.domain.tasks import AgentTask, TaskType
from .conversational_intent_detector import ConversationalIntent


class InteractiveFeedbackHandler:
    """
    Translates detected conversational intent into actionable AgentTasks or responses.
    """

    def handle_feedback(self, intent: ConversationalIntent) -> tuple[AgentTask | None, str]:
        if intent.action_type == InteractiveActionType.EXPLANATION:
            return None, f"Explanation request for: {intent.clean_instruction}"

        title = f"Interactive Co-Pilot: {intent.action_type.value}"
        desc = intent.clean_instruction
        if intent.target_file:
            desc += f"\nTarget file: {intent.target_file}"

        task_type_map = {
            InteractiveActionType.BUG_FIX: TaskType.IMPLEMENTATION,
            InteractiveActionType.FEATURE_ADDITION: TaskType.IMPLEMENTATION,
            InteractiveActionType.REFACTORING: TaskType.IMPLEMENTATION,
            InteractiveActionType.OPTIMIZATION: TaskType.IMPLEMENTATION,
        }
        tt = task_type_map.get(intent.action_type, TaskType.IMPLEMENTATION)

        task = AgentTask(
            id=uuid4(),
            title=title,
            description=desc,
            task_type=tt,
        )
        return task, f"Task created: {title}"
