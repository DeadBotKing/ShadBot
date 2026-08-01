"""
Agent Platform

Default agent registration.
"""

from __future__ import annotations

from agentplatform.application.registry import AgentRegistry
from agentplatform.domain.agents import AgentRole
from agentplatform.infrastructure.agents.architect_agent import (
    ArchitectAgent,
)
from agentplatform.infrastructure.agents.engineer_agent import (
    EngineerAgent,
)
from agentplatform.infrastructure.agents.researcher_agent import (
    ResearcherAgent,
)
from agentplatform.infrastructure.agents.reviewer_agent import (
    ReviewerAgent,
)
from agentplatform.infrastructure.agents.trader_agent import (
    TraderAgent,
)


def register_default_agents(
    registry: AgentRegistry,
) -> AgentRegistry:
    """
    Register built-in agents.
    """

    registry.register(
        AgentRole.ARCHITECT,
        ArchitectAgent(),
    )

    registry.register(
        AgentRole.RESEARCHER,
        ResearcherAgent(),
    )

    registry.register(
        AgentRole.ENGINEER,
        EngineerAgent(),
    )

    registry.register(
        AgentRole.REVIEWER,
        ReviewerAgent(),
    )

    registry.register(
        AgentRole.TRADER,
        TraderAgent(),
    )

    return registry
