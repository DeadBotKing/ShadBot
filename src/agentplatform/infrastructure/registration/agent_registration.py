"""
Agent Platform

Default agent registration.
"""

from __future__ import annotations

import os

from agentplatform.application.brain import AgentBrain
from agentplatform.application.llm import LLMProvider
from agentplatform.application.memory import MemoryService
from agentplatform.application.registry import AgentRegistry
from agentplatform.application.tooling import ToolExecutor
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
from agentplatform.infrastructure.llm import RoutedLLMProvider
from agentplatform.infrastructure.memory import (
    InMemoryMemoryRepository,
)


def register_default_agents(
    registry: AgentRegistry,
    tool_executor: ToolExecutor,
) -> AgentRegistry:
    """
    Register built-in agents.
    """

    use_router = os.getenv("SHADBOT_ENABLE_MODEL_ROUTING", "0") == "1"

    llm: LLMProvider

    if use_router:
        llm = RoutedLLMProvider()
    else:
        from agentplatform.infrastructure.llm import OllamaProvider

        llm = OllamaProvider(
            model="qwen2.5-coder:7b",
        )

    brain = AgentBrain(
        llm=llm,
    )

    memory_repository = InMemoryMemoryRepository()

    memory_service = MemoryService(
        repository=memory_repository,
    )

    registry.register(
        AgentRole.ARCHITECT,
        ArchitectAgent(
            role=AgentRole.ARCHITECT,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        ),
    )

    registry.register(
        AgentRole.RESEARCHER,
        ResearcherAgent(
            role=AgentRole.RESEARCHER,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        ),
    )

    registry.register(
        AgentRole.ENGINEER,
        EngineerAgent(
            brain=brain,
            tool_executor=tool_executor,
        ),
    )

    registry.register(
        AgentRole.REVIEWER,
        ReviewerAgent(
            brain=brain,
            memory_service=memory_service,
        ),
    )

    return registry
