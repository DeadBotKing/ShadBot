"""
ShadBot Agent Platform

Agent Platform bootstrap.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.decision import (
    DecisionEngine,
)
from agentplatform.application.loop import (
    AgentExecutionLoop,
)
from agentplatform.application.registry import (
    AgentRegistry,
)
from agentplatform.application.retry import (
    RetryEngine,
    RetryPolicy,
)
from agentplatform.application.runtime import (
    AgentRuntimeService,
)
from agentplatform.application.runtime.retry_coordinator import (
    RetryCoordinator,
)
from agentplatform.infrastructure.registration import (
    register_default_agents,
)


@dataclass(slots=True)
class AgentPlatformBootstrap:
    """
    Composition root for Agent Platform.

    Responsible for building the complete
    dependency graph.
    """

    def build(self) -> AgentExecutionLoop:
        """
        Build configured Agent execution loop.
        """

        registry = AgentRegistry()

        register_default_agents(
            registry,
        )

        runtime = AgentRuntimeService(
            registry=registry,
        )

        decision_engine = DecisionEngine()

        retry_policy = RetryPolicy(
            max_retries=3,
        )

        retry_engine = RetryEngine(
            policy=retry_policy,
        )

        retry_coordinator = RetryCoordinator(
            retry_engine=retry_engine,
        )

        return AgentExecutionLoop(
            runtime=runtime,
            decision_engine=decision_engine,
            retry_coordinator=retry_coordinator,
        )
