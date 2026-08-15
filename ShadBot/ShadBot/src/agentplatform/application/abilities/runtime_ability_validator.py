"""
ShadBot Agent Platform

Runtime Ability Validator
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.agents import (
    AgentCapability,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .agent_capability_binding import (
    AgentCapabilityBinding,
)
from .capability_tool_binding import (
    CapabilityToolBinding,
)
from .tool_execution_binding import (
    ToolExecutionBinding,
)


@dataclass(slots=True)
class RuntimeAbilityValidator:
    """
    Validates runtime agent ability chain.
    """

    capability_binding: AgentCapabilityBinding

    capability_tool_binding: CapabilityToolBinding

    tool_execution_binding: ToolExecutionBinding

    def validate_capability(
        self,
        capability: AgentCapability,
    ) -> bool:
        """
        Validate capability availability.
        """

        return self.capability_binding.has(
            capability,
        )

    def validate_tool_access(
        self,
        capability: AgentCapability,
        tool_type: ToolType,
    ) -> bool:
        """
        Validate capability can access tool.
        """

        return self.validate_capability(
            capability,
        ) and self.capability_tool_binding.can_use(
            capability,
            tool_type,
        )

    def validate_execution(
        self,
        capability: AgentCapability,
        tool_type: ToolType,
    ) -> bool:
        """
        Validate full execution chain.
        """

        return self.validate_tool_access(
            capability,
            tool_type,
        ) and self.tool_execution_binding.can_execute(
            tool_type,
        )

    def validate_required_capabilities(
        self,
        required: set[AgentCapability],
    ) -> bool:
        """
        Validate required capabilities.
        """

        return self.capability_binding.validate(
            required,
        )
