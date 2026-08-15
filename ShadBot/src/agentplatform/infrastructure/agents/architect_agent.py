"""
ShadBot Agent Platform

Enterprise Architect Agent.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from uuid import uuid4

from agentplatform.application.brain import (
    AgentBrain,
)
from agentplatform.application.memory import (
    MemoryService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.architecture_plan import (
    ArchitecturePlan,
    FilePlan,
    ImplementationStep,
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

from .base_llm_agent import BaseLLMAgent


class ArchitectAgent(BaseLLMAgent):
    """
    Responsible for system architecture.

    Responsibilities:
    - Architecture design
    - Technology selection
    - System analysis
    - Feasibility analysis
    - Architecture validation
    """

    def __init__(
        self,
        role: AgentRole | None = None,
        brain: AgentBrain | None = None,
        tool_executor: ToolExecutor | None = None,
        memory_service: MemoryService | None = None,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            role=role or AgentRole.ARCHITECT,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
            capabilities=[
                Capability(
                    CapabilityType.ARCHITECTURE_DESIGN,
                    "Design enterprise software architecture.",
                ),
                Capability(
                    CapabilityType.TECHNOLOGY_SELECTION,
                    "Select appropriate technologies.",
                ),
                Capability(
                    CapabilityType.SYSTEM_ANALYSIS,
                    "Analyze complete system structure.",
                ),
                Capability(
                    CapabilityType.ARCHITECTURE_UNDERSTANDING,
                    "Understand existing architecture.",
                ),
                Capability(
                    CapabilityType.FEASIBILITY_ANALYSIS,
                    "Evaluate technical feasibility.",
                ),
                Capability(
                    CapabilityType.INNOVATION_ANALYSIS,
                    "Analyze innovative architecture approaches.",
                ),
            ],
        )

        self._role = role or AgentRole.ARCHITECT
        self._brain = brain
        self._tool_executor = tool_executor
        self._memory_service = memory_service

    @property
    def name(self) -> str:
        return "architect"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute architecture workflow.
        """

        summary = (
            self._brain.reason(
                self._role,
                context,
            )
            if self._brain
            else "Architecture plan generated."
        )

        file_plans = self._extract_file_plans(context, summary)

        plan = ArchitecturePlan(
            plan_id=uuid4(),
            task_id=context.task_id,
            summary=summary,
            file_plan=file_plans,
            dependency_plan=(),
            interface_plan=(),
            implementation_order=(
                ImplementationStep(
                    order=1,
                    description="Create core domain structure.",
                ),
            ),
            acceptance_criteria=(),
            constraints=("Architect does not generate source code",),
        )

        return AgentResult(
            success=True,
            message="Architecture plan generated.",
            data={
                "agent": self.name,
                "role": self._role.value,
                "architecture_plan": plan,
            },
        )

    def _extract_file_plans(
        self,
        context: AgentExecutionContext,
        summary: str,
    ) -> tuple[FilePlan, ...]:
        plans: list[FilePlan] = []

        is_self_hosting = (
            "ShadBot Agent Platform" in context.task_title
            or (context.target_project and "ShadBotCore" in str(context.target_project.name))
            or len(context.metadata.get("project_docs_summary", {}).get("doc_files", [])) >= 10
        )

        if is_self_hosting:
            core_modules = [
                ("src/agentplatform/domain/agents/agent_role.py", "Agent identity and role enumeration (Phase 2)"),
                ("src/agentplatform/domain/contracts/agent_contract.py", "Base abstract contract for agents (Phase 2)"),
                ("src/agentplatform/domain/architecture_plan/architecture_plan.py", "Architecture plan domain entity (Phase 5)"),
                ("src/agentplatform/application/orchestration/agent_orchestrator.py", "Multi-agent pipeline orchestration (Phase 6)"),
                ("src/agentplatform/application/quality_gate/quality_gate_service.py", "Quality Gate System & repair loops (Phase 9)"),
                ("src/agentplatform/application/self_improvement/self_improvement_service.py", "Self Improvement System & evolution (Phase 10)"),
                ("src/agentplatform/application/platform/platform_service.py", "Platform Finalization & API Gateway (Phase 11)"),
                ("src/agentplatform/application/release/release_service.py", "Production Freeze V1.0 & SLA governance (Phase 12)"),
                ("src/agentplatform/infrastructure/agents/project_intelligence_agent.py", "Eye of the Brain and Documentation Keeper (Phase 3)"),
                ("src/agentplatform/infrastructure/agents/architect_agent.py", "Clean Architecture and system design agent (Phase 5)"),
                ("src/agentplatform/infrastructure/agents/engineer_agent.py", "Source code implementation and run.py generator (Phase 6)"),
            ]
            for m_path, m_purpose in core_modules:
                plans.append(FilePlan(path=m_path, action="create", purpose=m_purpose))
            return tuple(plans)

        if "output_file" in context.metadata:
            plans.append(
                FilePlan(
                    path=str(context.metadata["output_file"]),
                    action="create",
                    purpose="Main deliverable",
                )
            )

        py_pattern = r"['\"`]((?:src|generated|app|tests)/[a-zA-Z0-9_/]+\.py)['\"`]"
        matches = re.findall(py_pattern, context.task_description + "\n" + summary)
        for m in sorted(set(matches)):
            if not any(p.path == m for p in plans):
                plans.append(
                    FilePlan(
                        path=m,
                        action="create",
                        purpose="Extracted target module",
                    )
                )

        dir_pattern = r"['\"`]((?:src|generated|app|tests)/[a-zA-Z0-9_/]+/)['\"`]"
        dir_matches = re.findall(dir_pattern, context.task_description + "\n" + summary)
        for d in sorted(set(dir_matches)):
            if not any(p.path.startswith(d) for p in plans):
                mod_name = (
                    "market_analyzer.py"
                    if ("indicator" in d or "market" in context.task_title.lower())
                    else "service.py"
                )
                plans.append(
                    FilePlan(
                        path=f"{d}{mod_name}",
                        action="create",
                        purpose="Target service module",
                    )
                )

        if not plans and context.task_title:
            slug = re.sub(
                r"[^a-zA-Z0-9_]+",
                "_",
                context.task_title.lower(),
            ).strip("_")
            plans.append(
                FilePlan(
                    path=f"src/{slug}.py",
                    action="create",
                    purpose="Default target module",
                )
            )

        return tuple(plans)
