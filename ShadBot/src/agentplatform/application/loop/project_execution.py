"""
ShadBot Agent Platform

Project execution orchestration.
"""

from __future__ import annotations

from pathlib import Path
from uuid import UUID

from agentplatform.application.loop.agent_execution_loop import (
    AgentExecutionLoop,
)
from agentplatform.application.roadmap import (
    PhaseManager,
)
from agentplatform.application.tasks import (
    ProjectTaskRepository,
    ProjectTaskService,
    TaskLifecycleManager,
    TaskResultEvaluator,
    TaskSelector,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tasks import (
    AgentTask,
    TaskType,
)
from agentplatform.infrastructure.roadmap import (
    YamlRoadmapLoader,
)
from agentplatform.infrastructure.tasks import (
    YamlTaskLoader,
)


class ProjectExecutionService:
    """
    Executes project tasks through agent platform.
    """

    def __init__(
        self,
        execution_loop: AgentExecutionLoop,
        lifecycle_manager: TaskLifecycleManager | None = None,
        result_evaluator: TaskResultEvaluator | None = None,
        task_repository: ProjectTaskRepository | None = None,
        task_selector: TaskSelector | None = None,
        phase_manager: PhaseManager | None = None,
        roadmap_loader: YamlRoadmapLoader | None = None,
        task_service: ProjectTaskService | None = None,
    ) -> None:
        self._execution_loop = execution_loop
        self._lifecycle = lifecycle_manager or TaskLifecycleManager()
        self._result_evaluator = result_evaluator or TaskResultEvaluator()
        self._task_repository = task_repository or ProjectTaskRepository()
        self._task_selector = task_selector or TaskSelector()
        self._phase_manager = phase_manager or PhaseManager()
        self._roadmap_loader = roadmap_loader or YamlRoadmapLoader()
        self._task_service = task_service or ProjectTaskService(
            loader=YamlTaskLoader(),
        )

    def execute_project(
        self,
        project_path: Path,
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute active project task.
        """

        phases = self._roadmap_loader.load(
            project_path,
        )

        active_phase = self._phase_manager.get_active_phase(
            phases,
        )

        if active_phase is None:
            return []

        tasks = self._task_service.get_tasks(
            project_path,
        )

        selected_task = self._task_selector.select_next(
            tasks,
            active_phase.id,
        )

        if selected_task is None:
            return []

        task = AgentTask(
            id=UUID(selected_task.id),
            title=selected_task.title,
            description=selected_task.description,
            task_type=TaskType(
                selected_task.task_type,
            ),
        )

        running_task = self._lifecycle.mark_running(
            task,
        )

        context = AgentExecutionContext(
            project_id=context.project_id,
            task_id=running_task.id,
            instructions=(f"Execute task: {running_task.title}"),
            workspace=context.workspace,
            target_project=context.target_project,
            task_title=running_task.title,
            task_description=running_task.description,
            task_type=running_task.task_type.value,
            intelligence_context=context.intelligence_context,
            metadata={
                **context.metadata,
                "task_status": running_task.status.value,
                "workspace": "ShadBotWorkspace",
                "project": project_path.name,
                # Explicit gate target. The orchestrator prefers
                # target_project.path, but keeping this in sync guarantees the
                # deterministic gate can never fall back to the platform root.
                "project_path": str(project_path.resolve()),
            },
            memory_context=context.memory_context,
            execution_id=context.execution_id,
            created_at=context.created_at,
        )

        results = self._execution_loop.execute(
            running_task,
            context,
        )

        if self._result_evaluator.is_successful(
            results,
        ):
            completed_task = self._lifecycle.mark_completed(
                running_task,
            )

            context.metadata.update(
                {
                    "task_status": completed_task.status.value,
                }
            )

            self._task_repository.archive_completed(
                project_path,
            )
        else:
            context.metadata.update(
                {
                    "task_status": "failed",
                }
            )

            self._task_repository.archive_failed(
                project_path,
            )

        return results
