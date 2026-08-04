"""
ShadBot Agent Platform

Default agent capability registration.
"""

from __future__ import annotations

from agentplatform.application.capabilities import (
    CapabilityRegistry,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.capabilities import (
    Capability,
    CapabilityType,
)


def register_default_capabilities(
    registry: CapabilityRegistry,
) -> CapabilityRegistry:
    """
    Register default capabilities for built-in agents.
    """

    engineer_capabilities = [
        Capability(
            CapabilityType.CODE_GENERATION,
            "Generate production code.",
        ),
        Capability(
            CapabilityType.CODE_REFACTORING,
            "Refactor existing code.",
        ),
        Capability(
            CapabilityType.TEST_GENERATION,
            "Create automated tests.",
        ),
        Capability(
            CapabilityType.DEBUGGING,
            "Analyze and fix software issues.",
        ),
    ]

    architect_capabilities = [
        Capability(
            CapabilityType.ARCHITECTURE_DESIGN,
            "Design software architecture.",
        ),
        Capability(
            CapabilityType.TECHNOLOGY_SELECTION,
            "Select suitable technologies.",
        ),
        Capability(
            CapabilityType.SYSTEM_ANALYSIS,
            "Analyze system structure.",
        ),
    ]

    researcher_capabilities = [
        Capability(
            CapabilityType.SYSTEM_ANALYSIS,
            "Research and analyze technical information.",
        ),
    ]

    reviewer_capabilities = [
        Capability(
            CapabilityType.CODE_REVIEW,
            "Review code quality and correctness.",
        ),
        Capability(
            CapabilityType.DEBUGGING,
            "Identify defects and problems.",
        ),
    ]

    assignments = {
        AgentRole.ENGINEER: engineer_capabilities,
        AgentRole.ARCHITECT: architect_capabilities,
        AgentRole.RESEARCHER: researcher_capabilities,
        AgentRole.REVIEWER: reviewer_capabilities,
    }

    for role, capabilities in assignments.items():
        for capability in capabilities:
            registry.register(
                role,
                capability,
            )

    return registry
