"""
ShadBot Agent Platform

Enterprise Architect Agent.
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

from .base_agent import BaseAgent


class ArchitectAgent(BaseAgent):
    """
    Responsible for system architecture.

    Responsibilities:
    - Architecture design
    - Technology selection
    - System analysis
    - Feasibility analysis
    - Architecture validation
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
                    CapabilityType.ARCHITECTURE_DESIGN,
                    "Design enterprise software architecture.",
                ),
                Capability(
                    CapabilityType.TECHNOLOGY_SELECTION,
                    "Select appropriate technologies.",
                ),
                Capability(
                    CapabilityType.SYSTEM_ANALYSIS,
                    "Analyze complete system structure.",
                ),
                Capability(
                    CapabilityType.ARCHITECTURE_UNDERSTANDING,
                    "Understand existing architecture.",
                ),
                Capability(
                    CapabilityType.FEASIBILITY_ANALYSIS,
                    "Evaluate technical feasibility.",
                ),
                Capability(
                    CapabilityType.INNOVATION_ANALYSIS,
                    "Analyze innovative architecture approaches.",
                ),
            ],
        )

        self._role = role
        self._brain = brain
        self._tool_executor = tool_executor
        self._memory_service = memory_service

    @property
    def name(self) -> str:
        return "architect"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute architecture workflow.
        """

        analysis = self._tool_executor.execute(
            "project_analyzer",
            {
                "action": "architecture_analysis",
            },
        )

        reasoning = self._brain.reason(
            context,
        )

        return AgentResult(
            success=True,
            message="Architecture workflow completed.",
            data={
                "agent": self.name,
                "role": self._role.value,
                "capabilities": [
                    capability.capability_type.value for capability in self.capabilities
                ],
                "analysis": analysis,
                "reasoning": reasoning,
            },
        )
