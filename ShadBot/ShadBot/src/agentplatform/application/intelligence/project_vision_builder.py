"""
ShadBot Agent Platform

Project vision builder.
"""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from agentplatform.domain.intelligence import (
    ArchitectureState,
    ChangeState,
    DevelopmentState,
    ProjectIdentity,
    ProjectVision,
    QualityState,
    RuntimeState,
    TechnologyState,
)


class ProjectVisionBuilder:
    """
    Builds immutable project vision objects.
    """

    def build(
        self,
        project_id: UUID,
        project_path: str,
        data: dict[str, object],
    ) -> ProjectVision:
        """
        Create project vision from intelligence data.
        """

        return ProjectVision(
            identity=ProjectIdentity(
                project_id=project_id,
                name=str(
                    data.get(
                        "name",
                        "",
                    ),
                ),
                path=project_path,
            ),
            architecture=ArchitectureState(
                description=str(
                    data.get(
                        "architecture_description",
                        "",
                    ),
                ),
                modules=self._tuple(
                    data.get(
                        "modules",
                        [],
                    ),
                ),
                patterns=self._tuple(
                    data.get(
                        "patterns",
                        [],
                    ),
                ),
                dependencies=self._dict(
                    data.get(
                        "dependencies",
                        {},
                    ),
                ),
            ),
            technologies=TechnologyState(
                languages=self._tuple(
                    data.get(
                        "languages",
                        [],
                    ),
                ),
                frameworks=self._tuple(
                    data.get(
                        "frameworks",
                        [],
                    ),
                ),
                tools=self._tuple(
                    data.get(
                        "tools",
                        [],
                    ),
                ),
                databases=self._tuple(
                    data.get(
                        "databases",
                        [],
                    ),
                ),
            ),
            development=DevelopmentState(
                completed_tasks=self._tuple(
                    data.get(
                        "completed_tasks",
                        [],
                    ),
                ),
                pending_tasks=self._tuple(
                    data.get(
                        "pending_tasks",
                        [],
                    ),
                ),
                active_tasks=self._tuple(
                    data.get(
                        "active_tasks",
                        [],
                    ),
                ),
                decisions=self._tuple(
                    data.get(
                        "decisions",
                        [],
                    ),
                ),
            ),
            quality=QualityState(
                tests_status=str(
                    data.get(
                        "tests_status",
                        "unknown",
                    ),
                ),
                validation_status=str(
                    data.get(
                        "validation_status",
                        "unknown",
                    ),
                ),
                known_issues=self._tuple(
                    data.get(
                        "known_issues",
                        [],
                    ),
                ),
                risks=self._tuple(
                    data.get(
                        "risks",
                        [],
                    ),
                ),
            ),
            runtime=RuntimeState(
                health_status=str(
                    data.get(
                        "health_status",
                        "unknown",
                    ),
                ),
                performance_notes=self._tuple(
                    data.get(
                        "performance_notes",
                        [],
                    ),
                ),
                runtime_errors=self._tuple(
                    data.get(
                        "runtime_errors",
                        [],
                    ),
                ),
            ),
            changes=ChangeState(
                changed_files=self._tuple(
                    data.get(
                        "changed_files",
                        [],
                    ),
                ),
                commits=self._tuple(
                    data.get(
                        "commits",
                        [],
                    ),
                ),
                summary=str(
                    data.get(
                        "change_summary",
                        "",
                    ),
                ),
            ),
            recommendations=self._tuple(
                data.get(
                    "recommendations",
                    [],
                ),
            ),
            generated_at=datetime.now(
                timezone.utc,
            ),
        )

    @staticmethod
    def _tuple(
        value: object,
    ) -> tuple[str, ...]:

        if not isinstance(
            value,
            list,
        ):
            return ()

        return tuple(str(item) for item in value)

    @staticmethod
    def _dict(
        value: object,
    ) -> dict[str, str]:

        if not isinstance(
            value,
            dict,
        ):
            return {}

        return {str(key): str(item) for key, item in value.items()}
