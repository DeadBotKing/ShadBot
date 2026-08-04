"""
ShadBot Agent Platform

Agent Platform bootstrap.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agentplatform.application.brain import (
    AgentBrain,
    BrainReasoning,
)
from agentplatform.application.execution import (
    AgentExecutionService,
)
from agentplatform.application.loop import (
    AgentExecutionLoop,
)
from agentplatform.application.monitoring import (
    ExecutionEventBus,
)
from agentplatform.application.monitoring.listeners import (
    ConsoleExecutionListener,
)
from agentplatform.application.orchestration import (
    AgentOrchestrator,
)
from agentplatform.application.prompt import (
    PromptBuilder,
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
from agentplatform.application.tasks import (
    ProjectTaskService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
    ToolRegistry,
)
from agentplatform.application.validation import (
    ValidationEngine,
)
from agentplatform.application.workspace import (
    WorkspaceRegistry,
)
from agentplatform.domain.workspace import (
    Project,
    Workspace,
)
from agentplatform.infrastructure.llm import (
    OllamaProvider,
)
from agentplatform.infrastructure.registration import (
    register_default_agents,
    register_default_tools,
)
from agentplatform.infrastructure.tasks import (
    YamlTaskLoader,
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

        tool_registry = ToolRegistry()

        register_default_tools(
            tool_registry,
        )

        tool_executor = ToolExecutor(
            tool_registry,
        )

        workspace_registry = WorkspaceRegistry()

        workspace_root = Path(
            "..",
            "ShadBotWorkspace",
        ).resolve()

        for project in (
            workspace_root / "Meryx",
            workspace_root / "Trader",
        ):
            project.mkdir(
                parents=True,
                exist_ok=True,
            )

        workspace_registry.register(
            Workspace(
                name="ShadBotWorkspace",
                root_path=workspace_root,
                projects=(
                    Project(
                        name="Meryx",
                        path=workspace_root / "Meryx",
                        project_type="software",
                    ),
                    Project(
                        name="Trader",
                        path=workspace_root / "Trader",
                        project_type="trading",
                    ),
                ),
            ),
        )

        event_bus = ExecutionEventBus()

        event_bus.subscribe(
            ConsoleExecutionListener(),
        )

        register_default_agents(
            registry,
            tool_executor,
        )

        # dispatcher = AgentDispatcher(
        #     registry,
        # )

        execution_service = AgentExecutionService(
            event_bus=event_bus,
        )

        orchestrator = AgentOrchestrator(
            execution_service=execution_service,
        )

        runtime = AgentRuntimeService(
            registry=registry,
            tool_executor=tool_executor,
            orchestrator=orchestrator,
            workspace_registry=workspace_registry,
        )

        retry_policy = RetryPolicy(
            max_retries=3,
        )

        retry_engine = RetryEngine(
            policy=retry_policy,
        )

        retry_coordinator = RetryCoordinator(
            retry_engine=retry_engine,
        )

        task_loader = YamlTaskLoader()

        project_task_service = ProjectTaskService(
            loader=task_loader,
        )

        llm = OllamaProvider(
            model="qwen2.5-coder:7b",
        )

        brain_reasoning = BrainReasoning(
            llm=llm,
            prompt_builder=PromptBuilder(),
        )

        brain = AgentBrain(
            reasoning=brain_reasoning,
        )

        validation_engine = ValidationEngine()

        return AgentExecutionLoop(
            brain=brain,
            runtime=runtime,
            retry_coordinator=retry_coordinator,
            validation_engine=validation_engine,
            task_service=project_task_service,
        )
