"""
Agent Platform

Default agent registration.
"""

from __future__ import annotations

import os

from agentplatform.application.brain.brain_reasoning import (
    BrainReasoning,
)
from agentplatform.application.generation import (
    CodeGenerationService,
)
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
from agentplatform.infrastructure.agents.ml_scientist_agent import (
    MLScientistAgent,
)
from agentplatform.infrastructure.agents.project_intelligence_agent import (
    ProjectIntelligenceAgent,
)
from agentplatform.infrastructure.agents.qa_agent import (
    QAAgent,
)
from agentplatform.infrastructure.agents.researcher_agent import (
    ResearcherAgent,
)
from agentplatform.infrastructure.agents.reviewer_agent import (
    ReviewerAgent,
)
from agentplatform.infrastructure.agents.rnd_agent import (
    RND_Agent,
)
from agentplatform.infrastructure.agents.runtime_observer_agent import (
    RuntimeObserverAgent,
)
from agentplatform.infrastructure.brain.agent_brain_factory import (
    AgentBrainFactory,
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

    reasoning = BrainReasoning(
        llm=llm,
    )

    brain_factory = AgentBrainFactory(
        reasoning=reasoning,
    )

    memory_repository = InMemoryMemoryRepository()

    memory_service = MemoryService(
        repository=memory_repository,
    )

    architect_brain = brain_factory.create(
        AgentRole.ARCHITECT,
    )

    researcher_brain = brain_factory.create(
        AgentRole.RESEARCHER,
    )

    engineer_brain = brain_factory.create(
        AgentRole.ENGINEER,
    )

    reviewer_brain = brain_factory.create(
        AgentRole.REVIEWER,
    )

    ml_scientist_brain = brain_factory.create(
        AgentRole.ML_SCIENTIST,
    )

    registry.register(
        AgentRole.PROJECT_INTELLIGENCE,
        ProjectIntelligenceAgent(
            tool_executor=tool_executor,
        ),
    )

    registry.register(
        AgentRole.ARCHITECT,
        ArchitectAgent(
            role=AgentRole.ARCHITECT,
            brain=architect_brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        ),
    )

    registry.register(
        AgentRole.RESEARCHER,
        ResearcherAgent(
            role=AgentRole.RESEARCHER,
            brain=researcher_brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        ),
    )

    registry.register(
        AgentRole.RND,
        RND_Agent(
            tool_executor=tool_executor,
        ),
    )

    registry.register(
        AgentRole.QA,
        QAAgent(
            tool_executor=tool_executor,
        ),
    )

    registry.register(
        AgentRole.ML_SCIENTIST,
        MLScientistAgent(
            tool_executor=tool_executor,
        ),
    )

    registry.register(
        AgentRole.ENGINEER,
        EngineerAgent(
            code_generation_service=CodeGenerationService(
                brain=engineer_brain,
            ),
            tool_executor=tool_executor,
        ),
    )

    registry.register(
        AgentRole.REVIEWER,
        ReviewerAgent(
            brain=reviewer_brain,
            memory_service=memory_service,
            tool_executor=tool_executor,
        ),
    )

    registry.register(
        AgentRole.RUNTIME_OBSERVER,
        RuntimeObserverAgent(
            tool_executor=tool_executor,
        ),
    )

    return registry
