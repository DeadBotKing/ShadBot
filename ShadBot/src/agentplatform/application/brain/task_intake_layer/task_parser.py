"""
ShadBot Agent Platform

Task Parser component for 5.14 Task Intake Layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ParsedTaskMetadata:
    title: str
    description: str
    sections: dict[str, str] = field(default_factory=dict)


class TaskParser:
    """
    Parses markdown content from task.md into structured sections.
    """

    def parse(self, markdown_content: str) -> ParsedTaskMetadata:
        lines = markdown_content.splitlines()
        title = "Untitled Task"
        desc_lines: list[str] = []
        sections: dict[str, str] = {}
        current_section = "description"

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("# ") and title == "Untitled Task":
                title = stripped[2:].strip()
            elif stripped.startswith("## "):
                current_section = stripped[3:].strip().lower()
                sections[current_section] = ""
            else:
                if current_section == "description":
                    desc_lines.append(line)
                else:
                    sections[current_section] = (sections.get(current_section, "") + "\n" + line).strip()

        description = "\n".join(desc_lines).strip() or "No description provided."
        return ParsedTaskMetadata(
            title=title,
            description=description,
            sections=sections,
        )
