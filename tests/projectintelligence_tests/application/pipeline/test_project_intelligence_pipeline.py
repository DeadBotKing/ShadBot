from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock
from uuid import uuid4

from projectintelligence.application.pipeline.project_intelligence_pipeline import (
    ProjectIntelligencePipeline,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


def test_project_intelligence_pipeline_executes_all_steps() -> None:

    project = Mock(spec=ProjectEntity)

    project.project_id = uuid4()
    project.workspace = Path(".")

    workspace_scanner = Mock()
    snapshot_builder = Mock()
    language_detector = Mock()
    framework_detector = Mock()
    dependency_analyzer = Mock()
    git_analyzer = Mock()
    knowledge_builder = Mock()
    git_context_mapper = Mock()

    files = ["main.py"]

    snapshot = ProjectSnapshot(
        project_id=project.project_id,
        workspace=project.workspace,
    )

    context = ProjectContext(
        project_id=project.project_id,
    )

    git_context = Mock()

    workspace_scanner.scan.return_value = files
    snapshot_builder.build.return_value = snapshot

    language_detector.detect.return_value = ["Python"]
    framework_detector.detect.return_value = ["Django"]
    dependency_analyzer.analyze.return_value = ["Django"]

    git_analyzer.analyze.return_value = git_context

    knowledge_builder.build.return_value = context

    pipeline = ProjectIntelligencePipeline(
        workspace_scanner=workspace_scanner,
        snapshot_builder=snapshot_builder,
        language_detector=language_detector,
        framework_detector=framework_detector,
        dependency_analyzer=dependency_analyzer,
        git_analyzer=git_analyzer,
        git_context_mapper=git_context_mapper,
        knowledge_builder=knowledge_builder,
    )

    result = pipeline.run(
        project,
    )

    assert result.success is True
    assert result.snapshot is snapshot
    assert result.context is context
    assert result.git_context is git_context

    workspace_scanner.scan.assert_called_once()
    snapshot_builder.build.assert_called_once()
    language_detector.detect.assert_called_once()
    framework_detector.detect.assert_called_once()
    dependency_analyzer.analyze.assert_called_once()
    git_analyzer.analyze.assert_called_once()
    knowledge_builder.build.assert_called_once()
