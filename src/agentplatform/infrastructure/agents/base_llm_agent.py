"""
Agent Platform

Base LLM Agent implementation.
"""

from __future__ import annotations

from abc import abstractmethod

from agentplatform.application.brain import AgentBrain
from agentplatform.application.memory import MemoryService
from agentplatform.application.tooling import ToolExecutor
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_agent import BaseAgent


class BaseLLMAgent(BaseAgent):
    """
    Base implementation for every LLM-powered agent.
    """

    def __init__(
        self,
        role: AgentRole,
        brain: AgentBrain,
        tool_executor: ToolExecutor | None = None,
        memory_service: MemoryService | None = None,
    ) -> None:
        self._role = role
        self._brain = brain
        self._tool_executor = tool_executor
        self._memory_service = memory_service

    @property
    def role(self) -> AgentRole:
        return self._role

    @property
    def brain(self) -> AgentBrain:
        return self._brain

    @property
    def tool_executor(self) -> ToolExecutor | None:
        return self._tool_executor

    @property
    def memory_service(self) -> MemoryService | None:
        return self._memory_service

    def think(
        self,
        context: AgentExecutionContext,
    ) -> str:
        """
        Execute LLM reasoning.
        """

        return self._brain.think(
            self._role,
            context,
        )

    @abstractmethod
    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Agent-specific implementation.
        """
        raise NotImplementedError
