from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock
from uuid import uuid4

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.application.git.models.git_status import (
    GitStatus,
)
from projectintelligence.application.knowledge.knowledge_builder import (
    KnowledgeBuilder,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


def test_knowledge_builder_builds_project_context() -> None:
    snapshot = ProjectSnapshot(
        project_id=uuid4(),
        workspace=Path("."),
    )

    architecture_builder = Mock()
    technology_builder = Mock()
    dependency_builder = Mock()
    change_builder = Mock()

    git_context = GitContext(
        status=GitStatus(
            is_repository=True,
            is_dirty=False,
            ahead=0,
            behind=0,
            current_branch="main",
        ),
        current_commit=None,
        branches=(),
        changes=(),
        recent_commits=(),
    )

    architecture_builder.build.return_value = [
        "architecture",
    ]

    technology_builder.build.return_value = [
        "Python",
    ]

    dependency_builder.build.return_value = [
        "Django",
    ]

    change_builder.build.return_value = {
        "changed_files": [],
    }

    builder = KnowledgeBuilder(
        architecture_builder=architecture_builder,
        technology_builder=technology_builder,
        dependency_builder=dependency_builder,
        change_builder=change_builder,
    )

    context = builder.build(
        snapshot,
        git_context,
    )

    assert context.architecture_context == [
        "architecture",
    ]

    assert context.technology_context == [
        "Python",
    ]

    assert context.dependency_context == [
        "Django",
    ]

    assert context.change_context == {
        "changed_files": [],
    }

    architecture_builder.build.assert_called_once_with(
        snapshot,
    )

    technology_builder.build.assert_called_once_with(
        snapshot,
    )

    dependency_builder.build.assert_called_once_with(
        snapshot,
    )

    change_builder.build.assert_called_once_with(
        snapshot,
        git_context,
    )
