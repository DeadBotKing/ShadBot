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
from projectintelligence.application.git.mapping.git_context_mapper import (
    GitContextMapper,
)
from projectintelligence.application.git.services.git_analyzer import (
    GitAnalyzer,
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
    git_analyzer: GitAnalyzer
    knowledge_builder: KnowledgeBuilder
    git_context_mapper: GitContextMapper

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

        git_context = self.git_analyzer.analyze()

        git_state = self.git_context_mapper.map(
            git_context,
        )

        context = self.knowledge_builder.build(
            snapshot,
            git_context,
        )

        context.git_state = git_state

        return PipelineResult(
            snapshot=snapshot,
            context=context,
            git_context=git_context,
        )
