"""
ShadBot Project Intelligence

Runtime Host
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.bootstrap.project_intelligence_bootstrap import (
    ProjectIntelligenceBootstrap,
)
from projectintelligence.application.models.results.runtime_result import (
    RuntimeResult,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.runtime.runtime_configuration import (
    RuntimeConfiguration,
)
from projectintelligence.runtime.runtime_exception_handler import (
    RuntimeExceptionHandler,
)
from projectintelligence.runtime.runtime_lifecycle import (
    RuntimeLifecycle,
)
from projectintelligence.runtime.runtime_validator import (
    RuntimeValidator,
)


@dataclass(slots=True)
class RuntimeHost:
    """
    Hosts a single Project Intelligence runtime execution.

    Responsible only for coordinating runtime execution.
    Contains no business logic.
    """

    bootstrap: ProjectIntelligenceBootstrap

    validator: RuntimeValidator

    exception_handler: RuntimeExceptionHandler

    lifecycle: RuntimeLifecycle

    def execute(
        self,
        configuration: RuntimeConfiguration,
    ) -> RuntimeResult:
        """
        Execute Project Intelligence for a single workspace.
        """

        self.lifecycle.mark_starting()

        try:
            self.validator.validate(
                configuration,
            )

            project = ProjectEntity(
                name=configuration.resolved_project_name,
                workspace=configuration.workspace,
                repository_path=configuration.workspace,
            )

            engine = self.bootstrap.build(
                project=project,
            )

            self.lifecycle.mark_running()

            result = engine.execute(
                project=project,
            )

            self.lifecycle.mark_completed()

            return result

        except Exception as exception:
            self.lifecycle.mark_failed()

            self.exception_handler.handle(
                exception,
            )

            raise
