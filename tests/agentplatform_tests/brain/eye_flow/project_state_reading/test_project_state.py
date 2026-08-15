"""
ShadBot Agent Platform

Project State tests.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from agentplatform.application.brain.eye_flow.project_state_reading import (
    ProjectFilesystemState,
    ProjectLifecycleState,
    ProjectState,
    ProjectStateStatus,
)


def test_project_state_exposes_derived_properties() -> None:
    project_id = uuid4()

    state = ProjectState(
        project_id=project_id,
        project_name="TestProject",
        project_path=Path("projects/TestProject"),
        project_type="python",
        project_version="1.0.0",
        lifecycle_state=ProjectLifecycleState.AVAILABLE,
        filesystem_state=ProjectFilesystemState.POPULATED,
        status=ProjectStateStatus.READY,
        workspace_file_count=10,
        workspace_directory_count=3,
        operating_system="Windows",
        languages=("Python",),
        frameworks=("Django",),
        tools=("pytest", "ruff"),
        runtime_versions=(
            ("python", "3.14.6"),
        ),
        observed_at=datetime.now(timezone.utc),
    )

    assert state.project_id == project_id
    assert state.is_available is True
    assert state.is_ready is True
    assert state.has_files is True
    assert state.runtime_version_map == {
        "python": "3.14.6",
    }