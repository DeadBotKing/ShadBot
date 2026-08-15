"""
ShadBot Project Intelligence

Project Scanner Pipeline
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


@dataclass(slots=True)
class ProjectScannerPipeline:
    """
    Defines the dependencies required for the project scanning pipeline.

    The orchestration logic will be implemented by the scanner service.
    """

    workspace_scanner: IWorkspaceScanner
    language_detector: ILanguageDetector
    framework_detector: IFrameworkDetector
    dependency_analyzer: IDependencyAnalyzer
    snapshot_builder: ISnapshotBuilder
