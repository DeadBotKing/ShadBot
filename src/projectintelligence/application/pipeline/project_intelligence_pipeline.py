"""
ShadBot Project Intelligence

Project Intelligence Pipeline
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.contracts.analysis.dependency_analyzer import (
    IDependencyAnalyzer,
)
from projectintelligence.application.contracts.analysis.framework_detector import (
    IFrameworkDetector,
)
from projectintelligence.application.contracts.analysis.language_detector import (
    ILanguageDetector,
)
from projectintelligence.application.contracts.project.workspace_scanner import (
    IWorkspaceScanner,
)
from projectintelligence.application.contracts.snapshot.snapshot_builder import (
    ISnapshotBuilder,
)
from projectintelligence.application.knowledge.knowledge_builder import (
    KnowledgeBuilder,
)
from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


@dataclass(slots=True)
class ProjectIntelligencePipeline:
    """
    Executes the complete Project Intelligence pipeline.
    """

    workspace_scanner: IWorkspaceScanner
    snapshot_builder: ISnapshotBuilder
    language_detector: ILanguageDetector
    framework_detector: IFrameworkDetector
    dependency_analyzer: IDependencyAnalyzer
    knowledge_builder: KnowledgeBuilder

    def run(
        self,
        project: ProjectEntity,
    ) -> PipelineResult:
        """
        Execute the Project Intelligence pipeline.
        """

        files = self.workspace_scanner.scan(
            project.workspace,
        )

        snapshot = self.snapshot_builder.build(
            project,
        )

        snapshot.detected_languages = self.language_detector.detect(
            files,
        )

        snapshot.detected_frameworks = self.framework_detector.detect(
            files,
        )

        snapshot.dependencies = self.dependency_analyzer.analyze(
            files,
        )

        context = self.knowledge_builder.build(
            snapshot,
        )

        return PipelineResult(
            snapshot=snapshot,
            context=context,
        )
