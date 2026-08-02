"""
Agent Platform

Reviewer agent implementation.
"""

from __future__ import annotations

from agentplatform.application.brain import AgentBrain
from agentplatform.application.memory import (
    MemoryExtractor,
    MemoryService,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.review import ReviewResult

from .base_agent import BaseAgent


class ReviewerAgent(BaseAgent):
    """
    Responsible for reviewing implementations and decisions.
    """

    def __init__(
        self,
        brain: AgentBrain | None = None,
        memory_service: MemoryService | None = None,
        memory_extractor: MemoryExtractor | None = None,
    ) -> None:
        self._brain = brain
        self._memory_service = memory_service
        self._memory_extractor = memory_extractor or MemoryExtractor()

    @property
    def name(self) -> str:
        return "reviewer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        if self._brain is None:
            return AgentResult(
                success=False,
                message="Agent brain is not configured.",
                data={
                    "agent": self.name,
                },
            )

        response = self._brain.think(
            AgentRole.REVIEWER,
            context,
        )

        review = ReviewResult(
            approved=True,
            issues=[],
            suggestions=[response],
        )

        if self._memory_service:
            memories = self._memory_extractor.extract(
                context.project_id,
                review,
            )

            for memory in memories:
                self._memory_service.remember(
                    project_id=memory.project_id,
                    content=memory.content,
                    source=memory.source,
                    confidence=memory.confidence,
                )

        return AgentResult(
            success=True,
            message="Review completed.",
            approved=review.approved,
            data={
                "agent": self.name,
                "review": review,
            },
        )
