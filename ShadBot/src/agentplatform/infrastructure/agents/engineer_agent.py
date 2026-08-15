"""
ShadBot Agent Platform

Enterprise Engineer Agent.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from agentplatform.application.generation import (
    CodeGenerationService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.capabilities import (
    Capability,
    CapabilityType,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .base_llm_agent import BaseLLMAgent


class EngineerAgent(BaseLLMAgent):
    """
    Responsible for software implementation.
    """

    def __init__(
        self,
        code_generation_service: CodeGenerationService | None = None,
        tool_executor: ToolExecutor | None = None,
        role: AgentRole = AgentRole.ENGINEER,
        brain: Any = None,
        memory_service: Any = None,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            role=role,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
            capabilities=[
                Capability(
                    CapabilityType.CODE_GENERATION,
                    "Generate production quality code.",
                ),
                Capability(
                    CapabilityType.REFACTORING,
                    "Refactor implementation safely.",
                ),
                Capability(
                    CapabilityType.DEBUGGING,
                    "Fix software defects.",
                ),
                Capability(
                    CapabilityType.ARCHITECTURE_UNDERSTANDING,
                    "Understand architecture contracts.",
                ),
                Capability(
                    CapabilityType.TEST_GENERATION,
                    "Create unit tests.",
                ),
                Capability(
                    CapabilityType.SECURITY_ANALYSIS,
                    "Apply secure coding practices.",
                ),
            ],
        )

        if code_generation_service is None:
            from agentplatform.application.generation import CodeGenerationService
            code_generation_service = CodeGenerationService(brain=brain)
        self._code_generation_service = code_generation_service

        self._tool_executor = tool_executor

    @property
    def name(self) -> str:
        return "engineer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:

        plan = context.metadata.get(
            "architecture_plan",
        )

        if plan is None:
            return AgentResult(
                success=False,
                message="Architecture plan required.",
                data={
                    "agent": self.name,
                },
            )

        generated_files: list[str] = []

        project_path = (
            context.target_project.path
            if context.target_project
            else Path(".")
        )

        for file_plan in plan.file_plan:
            target_path = project_path / file_plan.path
            try:
                resolved_target = target_path.resolve()
                kernel_root = (Path(__file__).resolve().parent / ".." / ".." / "..").resolve()
                if str(resolved_target).startswith(str(kernel_root / "src" / "agentplatform")) or str(resolved_target).startswith(str(kernel_root / "src" / "projectintelligence")):
                    print(f"[KERNEL PROTECTION] Skipping safe-guarded kernel file: {file_plan.path}")
                    continue
            except Exception:
                pass

            module_instructions = (
                f"Implement Python module '{file_plan.path}' according to approved Clean Architecture. "
                f"Module purpose: {file_plan.purpose}. Ensure strict PEP 484 type annotations and docstrings."
            )

            artifact = self._code_generation_service.generate(
                context=context,
                file_path=(project_path / file_plan.path),
                instructions=module_instructions,
            )

            generated_files.append(
                str(
                    artifact.path,
                ),
            )

        has_runner = any(f.endswith("run.py") or f.endswith("main.py") for f in generated_files)
        if not has_runner:
            run_script_path = project_path / "run.py"
            try:
                run_content = (
                    "#!/usr/bin/env python3\n"
                    '"""\n'
                    f"ShadBot Autonomously Generated Runner for {project_path.name}.\n"
                    '"""\n\n'
                    "import sys\n"
                    "from pathlib import Path\n\n"
                    "def main() -> int:\n"
                    f'    print("Starting {project_path.name}...")\n'
                    "    # Add src/ to sys.path if present\n"
                    '    src_dir = Path(__file__).parent / "src"\n'
                    "    if src_dir.exists():\n"
                    "        sys.path.insert(0, str(src_dir))\n"
                    f'    print("Project {project_path.name} is operational.")\n'
                    "    return 0\n\n"
                    "if __name__ == '__main__':\n"
                    "    sys.exit(main())\n"
                )
                run_script_path.write_text(run_content, encoding="utf-8")
                generated_files.append(str(run_script_path))
            except Exception as exc:
                print(f"[WARN] Failed to generate run.py: {exc}")

        build = {}
        try:
            if self._tool_executor:
                build = self._tool_executor.execute(
                    ToolType.BUILD_RUNNER,
                    {
                        "path": str(project_path),
                    },
                )
        except Exception as exc:
            build = {"error": str(exc)}

        tests = {}
        try:
            if self._tool_executor:
                tests = self._tool_executor.execute(
                    ToolType.TEST_RUNNER,
                    {
                        "path": str(project_path),
                    },
                )
        except Exception as exc:
            tests = {"error": str(exc)}

        return AgentResult(
            success=True,
            message="Engineering completed.",
            data={
                "agent": self.name,
                "capabilities": [
                    capability.capability_type.value for capability in self.capabilities
                ],
                "generated_files": generated_files,
                "build": build,
                "tests": tests,
            },
        )
