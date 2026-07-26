"""
ShadBot Project Intelligence

Pipeline Integration Test
"""

from pathlib import Path
from unittest.mock import Mock

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.application.git.models.git_status import (
    GitStatus,
)
from projectintelligence.application.knowledge.architecture_context_builder import (
    ArchitectureContextBuilder,
)
from projectintelligence.application.knowledge.change_context_builder import (
    ChangeContextBuilder,
)
from projectintelligence.application.knowledge.dependency_context_builder import (
    DependencyContextBuilder,
)
from projectintelligence.application.knowledge.knowledge_builder import (
    KnowledgeBuilder,
)
from projectintelligence.application.knowledge.technology_context_builder import (
    TechnologyContextBuilder,
)
from projectintelligence.application.pipeline.project_intelligence_pipeline import (
    ProjectIntelligencePipeline,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


def test_project_intelligence_pipeline_integration() -> None:
    project = ProjectEntity(
        name="TestProject",
        workspace=Path("."),
    )

    workspace_scanner = Mock()
    snapshot_builder = Mock()
    language_detector = Mock()
    framework_detector = Mock()
    dependency_analyzer = Mock()
    git_analyzer = Mock()

    workspace_scanner.scan.return_value = [
        "main.py",
    ]

    snapshot_builder.build.return_value = ProjectSnapshot(
        project_id=project.project_id,
        workspace=project.workspace,
    )

    language_detector.detect.return_value = [
        "Python",
    ]

    framework_detector.detect.return_value = [
        "Django",
    ]

    dependency_analyzer.analyze.return_value = {
        "django": "5",
    }

    git_analyzer.analyze.return_value = GitContext(
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

    knowledge_builder = KnowledgeBuilder(
        architecture_builder=ArchitectureContextBuilder(),
        technology_builder=TechnologyContextBuilder(),
        dependency_builder=DependencyContextBuilder(),
        change_builder=ChangeContextBuilder(),
    )

    pipeline = ProjectIntelligencePipeline(
        workspace_scanner=workspace_scanner,
        snapshot_builder=snapshot_builder,
        language_detector=language_detector,
        framework_detector=framework_detector,
        dependency_analyzer=dependency_analyzer,
        git_analyzer=git_analyzer,
        knowledge_builder=knowledge_builder,
    )

    result = pipeline.run(project)

    assert result.success is True
    assert result.snapshot is not None
    assert result.context is not None
    assert result.git_context.status.current_branch == "main"
