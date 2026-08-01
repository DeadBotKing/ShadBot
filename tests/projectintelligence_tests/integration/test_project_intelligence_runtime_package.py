"""
ShadBot Project Intelligence

Runtime Package Integration Test
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from projectintelligence.application.package.package_generation_service import (
    PackageGenerationService,
)
from projectintelligence.application.runtime.project_intelligence_runtime_service import (
    ProjectIntelligenceRuntimeService,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.package.package_builder import (
    PackageBuilder,
)
from projectintelligence.package.package_writer import (
    PackageWriter,
)


class FakePipeline:
    """
    Minimal pipeline double for runtime integration.
    """

    def run(
        self,
        project: ProjectEntity,
    ) -> object:
        return object()


def test_runtime_generates_project_package(
    tmp_path: Path,
) -> None:
    """
    Runtime service should generate intelligence package.
    """

    runtime = ProjectIntelligenceRuntimeService(
        pipeline=FakePipeline(),
        package_service=PackageGenerationService(
            builder=PackageBuilder(
                writer=PackageWriter(),
            ),
        ),
    )

    project = ProjectEntity(
        project_id=uuid4(),
        name="RuntimeTestProject",
        workspace=tmp_path,
    )

    runtime.execute(
        project=project,
        output_directory=tmp_path / "output",
    )

    package_directory = tmp_path / "output" / "RuntimeTestProject"

    assert package_directory.exists()
    assert (package_directory / "metadata.json").exists()
    assert (package_directory / "manifest.json").exists()
