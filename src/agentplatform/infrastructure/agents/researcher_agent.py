"""
ShadBot Agent Platform

Enterprise Researcher Agent.
"""

from __future__ import annotations

from agentplatform.application.brain import (
    AgentBrain,
)
from agentplatform.application.memory import (
    MemoryService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.capabilities import (
    Capability,
    CapabilityType,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .base_agent import BaseAgent


class ResearcherAgent(BaseAgent):
    """
    Responsible for technical research.

    Responsibilities:
    - Technical research
    - Technology investigation
    - Documentation analysis
    - Feasibility analysis
    - Knowledge generation
    """

    def __init__(
        self,
        role: AgentRole,
        brain: AgentBrain,
        tool_executor: ToolExecutor,
        memory_service: MemoryService,
    ) -> None:

        super().__init__(
            capabilities=[
                Capability(
                    CapabilityType.RESEARCH,
                    "Perform technical research.",
                ),
                Capability(
                    CapabilityType.TECHNOLOGY_RESEARCH,
                    "Investigate technologies and frameworks.",
                ),
                Capability(
                    CapabilityType.DOCUMENTATION_ANALYSIS,
                    "Analyze technical documentation.",
                ),
                Capability(
                    CapabilityType.FEASIBILITY_ANALYSIS,
                    "Analyze technical feasibility.",
                ),
                Capability(
                    CapabilityType.KNOWLEDGE_GENERATION,
                    "Generate reusable technical knowledge.",
                ),
                Capability(
                    CapabilityType.SYSTEM_ANALYSIS,
                    "Analyze technical systems.",
                ),
            ],
        )

        self._role = role
        self._brain = brain
        self._tool_executor = tool_executor
        self._memory_service = memory_service

    @property
    def name(self) -> str:
        return "researcher"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute research workflow.
        """

        research = self._tool_executor.execute(
            ToolType.RESEARCH,
            {
                "query": context.metadata,
            },
        )

        documentation = self._tool_executor.execute(
            ToolType.DOCUMENTATION_ANALYSIS,
            {
                "context": context.metadata,
            },
        )

        reasoning = self._brain.reason(
            context,
        )

        return AgentResult(
            success=True,
            message="Research workflow completed.",
            data={
                "agent": self.name,
                "role": self._role.value,
                "capabilities": [
                    capability.capability_type.value for capability in self.capabilities
                ],
                "research": research,
                "documentation": documentation,
                "reasoning": reasoning,
            },
        )
