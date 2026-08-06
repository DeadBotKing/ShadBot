"""
ShadBot Agent Platform

Capability Tool Mapping
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentplatform.domain.agents import (
    AgentCapability,
)
from agentplatform.domain.tools import (
    ToolType,
)


@dataclass(slots=True)
class CapabilityToolMapping:
    """
    Maps agent capabilities to available tool types.

    Responsibilities:
    - Define capability requirements.
    - Resolve allowed tool categories.
    - Maintain capability/tool relationship.
    """

    mappings: dict[
        AgentCapability,
        set[ToolType],
    ] = field(
        default_factory=dict,
    )

    def register(
        self,
        capability: AgentCapability,
        tool_types: set[ToolType],
    ) -> None:
        """
        Register tool mapping for capability.
        """

        self.mappings[capability] = set(
            tool_types,
        )

    def get_tools(
        self,
        capability: AgentCapability,
    ) -> set[ToolType]:
        """
        Get tools assigned to capability.
        """

        return set(
            self.mappings.get(
                capability,
                set(),
            ),
        )

    def supports(
        self,
        capability: AgentCapability,
        tool_type: ToolType,
    ) -> bool:
        """
        Check capability-tool compatibility.
        """

        return tool_type in self.mappings.get(
            capability,
            set(),
        )

    def remove(
        self,
        capability: AgentCapability,
    ) -> None:
        """
        Remove capability mapping.
        """

        self.mappings.pop(
            capability,
            None,
        )

    def clear(
        self,
    ) -> None:
        """
        Clear all mappings.
        """

        self.mappings.clear()

    def load_defaults(
        self,
    ) -> None:
        """
        Register enterprise default mappings.
        """

        self.register(
            AgentCapability.CODE_GENERATION,
            {
                ToolType.FILE_SYSTEM,
                ToolType.CODE_EXECUTION,
                ToolType.PATCH_APPLIER,
            },
        )

        self.register(
            AgentCapability.CODE_REFACTORING,
            {
                ToolType.CODE_SEARCH,
                ToolType.PATCH_APPLIER,
                ToolType.STATIC_ANALYZER,
            },
        )

        self.register(
            AgentCapability.TEST_GENERATION,
            {
                ToolType.TEST_RUNNER,
                ToolType.CODE_EXECUTION,
            },
        )

        self.register(
            AgentCapability.CODE_REVIEW,
            {
                ToolType.STATIC_ANALYZER,
                ToolType.CODE_SEARCH,
            },
        )

        self.register(
            AgentCapability.ARCHITECTURE_ANALYSIS,
            {
                ToolType.PROJECT_ANALYZER,
                ToolType.DOCUMENTATION_ANALYSIS,
            },
        )

        self.register(
            AgentCapability.DEPENDENCY_ANALYSIS,
            {
                ToolType.PROJECT_ANALYZER,
                ToolType.STATIC_ANALYZER,
            },
        )

        self.register(
            AgentCapability.RESEARCH,
            {
                ToolType.RESEARCH,
                ToolType.TECHNOLOGY_COMPARISON,
            },
        )

        self.register(
            AgentCapability.FEATURE_ENGINEERING,
            {
                ToolType.DATASET_MANAGER,
                ToolType.EXPERIMENT_DESIGN,
            },
        )

        self.register(
            AgentCapability.MODEL_EVALUATION,
            {
                ToolType.MODEL_EVALUATION,
                ToolType.METRICS_COLLECTOR,
            },
        )
