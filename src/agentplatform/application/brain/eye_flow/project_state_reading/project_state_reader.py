"""
ShadBot Agent Platform

Project State Reader
"""

from __future__ import annotations

from datetime import datetime, timezone

from agentplatform.application.brain.eye_flow.environment_understanding import (
    EnvironmentAnalyzer,
)
from agentplatform.application.brain.eye_flow.workspace_observation import (
    WorkspaceObservationRequest,
    WorkspaceObserver,
)

from .project_state import (
    ProjectFilesystemState,
    ProjectLifecycleState,
    ProjectState,
    ProjectStateStatus,
)
from .project_state_request import ProjectStateRequest
from .project_state_result import ProjectStateResult


class ProjectStateReader:
    """
    Builds a semantic project state from previously collected Eye Flow data.

    Responsibilities:
    - validate the project request,
    - observe the workspace,
    - understand the environment,
    - normalize the collected information,
    - construct an immutable ProjectState.

    Explicitly does not:
    - modify the workspace,
    - execute commands,
    - inspect source-code semantics,
    - perform reasoning,
    - create plans,
    - assign agents,
    - make execution decisions.
    """

    def __init__(
        self,
        workspace_observer: WorkspaceObserver,
        environment_analyzer: EnvironmentAnalyzer,
    ) -> None:
        self._workspace_observer = workspace_observer
        self._environment_analyzer = environment_analyzer

    def read(
        self,
        request: ProjectStateRequest,
    ) -> ProjectStateResult:
        """
        Read and construct the current semantic project state.
        """

        self._validate_request(request)

        observation = self._workspace_observer.observe(
            WorkspaceObservationRequest(
                project_id=request.project_id,
                workspace_path=request.workspace_path,
                recursive=request.recursive,
            ),
        )

        environment = self._environment_analyzer.analyze(
            request.workspace_path,
        )

        lifecycle_state = self._resolve_lifecycle_state(
            project_exists=observation.workspace_path.exists(),
        )

        filesystem_state = self._resolve_filesystem_state(
            file_count=observation.total_files,
            project_exists=observation.workspace_path.exists(),
        )

        status = self._resolve_status(
            lifecycle_state=lifecycle_state,
            filesystem_state=filesystem_state,
            environment_detected=environment.detected,
        )

        runtime_versions = tuple(
            sorted(
                environment.profile.runtime_versions.items(),
            ),
        )

        state = ProjectState(
            project_id=request.project_id,
            project_name=request.project_name,
            project_path=request.project_path,
            project_type=request.project_type,
            project_version=request.project_version,
            lifecycle_state=lifecycle_state,
            filesystem_state=filesystem_state,
            status=status,
            workspace_file_count=observation.total_files,
            workspace_directory_count=observation.total_directories,
            operating_system=environment.profile.operating_system,
            languages=tuple(
                environment.profile.languages,
            ),
            frameworks=tuple(
                environment.profile.frameworks,
            ),
            tools=tuple(
                environment.profile.tools,
            ),
            runtime_versions=runtime_versions,
            observed_at=datetime.now(
                timezone.utc,
            ),
        )

        return ProjectStateResult(
            state=state,
        )

    @staticmethod
    def _validate_request(
        request: ProjectStateRequest,
    ) -> None:
        """
        Validate mandatory project-state input.
        """

        if not request.project_name.strip():
            raise ValueError(
                "Project name cannot be empty.",
            )

        if not request.project_type.strip():
            raise ValueError(
                "Project type cannot be empty.",
            )

        if not request.project_version.strip():
            raise ValueError(
                "Project version cannot be empty.",
            )

        if not request.project_path:
            raise ValueError(
                "Project path cannot be empty.",
            )

        if not request.workspace_path:
            raise ValueError(
                "Workspace path cannot be empty.",
            )

    @staticmethod
    def _resolve_lifecycle_state(
        project_exists: bool,
    ) -> ProjectLifecycleState:
        """
        Resolve the project lifecycle state.
        """

        if project_exists:
            return ProjectLifecycleState.AVAILABLE

        return ProjectLifecycleState.UNAVAILABLE

    @staticmethod
    def _resolve_filesystem_state(
        file_count: int,
        project_exists: bool,
    ) -> ProjectFilesystemState:
        """
        Resolve the filesystem state.
        """

        if not project_exists:
            return ProjectFilesystemState.UNAVAILABLE

        if file_count == 0:
            return ProjectFilesystemState.EMPTY

        return ProjectFilesystemState.POPULATED

    @staticmethod
    def _resolve_status(
        lifecycle_state: ProjectLifecycleState,
        filesystem_state: ProjectFilesystemState,
        environment_detected: bool,
    ) -> ProjectStateStatus:
        """
        Resolve the overall project state status.
        """

        if lifecycle_state is ProjectLifecycleState.UNAVAILABLE:
            return ProjectStateStatus.UNAVAILABLE

        if filesystem_state is ProjectFilesystemState.UNAVAILABLE:
            return ProjectStateStatus.UNAVAILABLE

        if not environment_detected:
            return ProjectStateStatus.DEGRADED

        return ProjectStateStatus.READY