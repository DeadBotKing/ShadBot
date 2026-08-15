"""
ShadBot Agent Platform

Unit tests for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4
from agentplatform.application.brain.task_intake_layer import (
    TaskDiscovery,
    TaskIntakeService,
    TaskNormalizer,
    TaskParser,
    TaskReader,
    TaskStateManager,
)


def test_task_discovery_finds_task_md(tmp_path: Path) -> None:
    task_file = tmp_path / "task.md"
    task_file.write_text("# Task\nDesc", encoding="utf-8")
    found = TaskDiscovery().discover_task_file(tmp_path)
    assert found == task_file


def test_task_parser_extracts_sections() -> None:
    content = "# Create Auth Service\n\nImplement enterprise JWT auth.\n\n## Requirements\n- JWT token"
    parsed = TaskParser().parse(content)
    assert parsed.title == "Create Auth Service"
    assert "JWT" in parsed.description
    assert "requirements" in parsed.sections


def test_task_normalizer_converts_to_agent_task() -> None:
    parsed = TaskParser().parse("# My Task\n\nMy desc.")
    norm = TaskNormalizer().normalize(parsed)
    assert norm.task.title == "My Task"
    assert norm.task_id == norm.task.id


def test_task_state_manager_tracks_status() -> None:
    mgr = TaskStateManager()
    tid = uuid4()
    mgr.set_status(tid, "INGESTED")
    state = mgr.get_status(tid)
    assert state is not None
    assert state.status == "INGESTED"


def test_task_intake_service_ingests_and_reports(tmp_path: Path) -> None:
    task_file = tmp_path / "Tasks" / "task.md"
    task_file.parent.mkdir(parents=True)
    task_file.write_text("# Enterprise Task\n\nBuild trading engine.", encoding="utf-8")

    service = TaskIntakeService()
    norm = service.intake_from_workspace(tmp_path)
    assert norm.task.title == "Enterprise Task"

    report = service.report_completion(norm.task_id, True, "All tests passed")
    assert report.completed is True
    assert report.final_status == "COMPLETED"
