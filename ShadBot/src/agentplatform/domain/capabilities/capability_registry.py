"""
ShadBot Agent Platform

Capability registry.
"""

from __future__ import annotations

from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.capabilities.agent_capability import (
    AgentCapability,
)
from agentplatform.domain.capabilities.capability import (
    Capability,
)
from agentplatform.domain.capabilities.capability_type import (
    CapabilityType,
)


class CapabilityRegistry:
    """
    Registry for agent capabilities.
    """

    def __init__(self) -> None:
        self._capabilities: list[AgentCapability] = []

        self._register_defaults()

    def register(
        self,
        agent_capability: AgentCapability,
    ) -> None:
        """
        Register capability assignment.
        """

        self._capabilities.append(
            agent_capability,
        )

    def get_for_agent(
        self,
        role: AgentRole,
    ) -> list[Capability]:
        """
        Return capabilities assigned to agent.
        """

        return [
            item.capability for item in self._capabilities if item.agent_role == role
        ]

    def _register_defaults(
        self,
    ) -> None:
        """
        Register platform default capabilities.
        """

        defaults: dict[
            AgentRole,
            list[tuple[CapabilityType, str]],
        ] = {
            AgentRole.ARCHITECT: [
                (
                    CapabilityType.ARCHITECTURE_DESIGN,
                    "Design software architecture.",
                ),
                (
                    CapabilityType.REQUIREMENT_ANALYSIS,
                    "Analyze requirements.",
                ),
            ],
            AgentRole.ENGINEER: [
                (
                    CapabilityType.IMPLEMENTATION,
                    "Implement software changes.",
                ),
                (
                    CapabilityType.REFACTORING,
                    "Refactor source code.",
                ),
            ],
            AgentRole.REVIEWER: [
                (
                    CapabilityType.CODE_REVIEW,
                    "Review source code.",
                ),
            ],
            AgentRole.RESEARCHER: [
                (
                    CapabilityType.RESEARCH,
                    "Perform technical research.",
                ),
            ],
            AgentRole.PROJECT_INTELLIGENCE: [
                (
                    CapabilityType.WORKSPACE_SCAN,
                    "Analyze project workspace.",
                ),
                (
                    CapabilityType.DEPENDENCY_ANALYSIS,
                    "Analyze project dependencies.",
                ),
                (
                    CapabilityType.ARCHITECTURE_UNDERSTANDING,
                    "Understand project architecture.",
                ),
                (
                    CapabilityType.KNOWLEDGE_GENERATION,
                    "Generate project knowledge.",
                ),
            ],
            AgentRole.QA: [
                (
                    CapabilityType.TESTING,
                    "Execute software tests.",
                ),
                (
                    CapabilityType.VALIDATION,
                    "Validate implementation.",
                ),
            ],
            AgentRole.RUNTIME_OBSERVER: [
                (
                    CapabilityType.RUNTIME_MONITORING,
                    "Observe runtime behaviour.",
                ),
            ],
            AgentRole.ML_SCIENTIST: [
                (
                    CapabilityType.MODEL_EVALUATION,
                    "Evaluate ML models.",
                ),
                (
                    CapabilityType.EXPERIMENT_DESIGN,
                    "Design ML experiments.",
                ),
            ],
        }

        for role, capabilities in defaults.items():
            for capability_type, description in capabilities:
                self.register(
                    AgentCapability(
                        agent_role=role,
                        capability=Capability(
                            capability_type=capability_type,
                            description=description,
                        ),
                    )
                )
