"""
Eye of the Brain and Documentation Keeper (Phase 3)

This module implements the Project Intelligence Agent, which is responsible for
collecting, analyzing, and presenting project intelligence data.
"""

from typing import Optional, List
import subprocess
from agentplatform.domain.agents.agent_role import AgentRole
from agentplatform.domain.contracts.agent_contract import AgentContract
from agentplatform.domain.architecture_plan.architecture_plan import ArchitecturePlan
from agentplatform.application.orchestration.agent_orchestrator import AgentOrchestrator
from agentplatform.application.quality_gate.quality_gate_service import QualityGateService
from agentplatform.application.self_improvement.self_improvement_service import SelfImprovementService
from agentplatform.application.platform.platform_service import PlatformService
from agentplatform.application.release.release_service import ReleaseService

class ProjectIntelligenceAgent(AgentContract):
    """
    Concrete implementation of the Project Intelligence Agent.
    """

    def __init__(self, orchestrator: AgentOrchestrator,
                 quality_gate: QualityGateService,
                 improvement_service: SelfImprovementService,
                 platform_service: PlatformService,
                 release_service: ReleaseService):
        """
        Initialize the Project Intelligence Agent.

        :param orchestrator: The agent orchestrator.
        :param quality_gate: The quality gate service.
        :param improvement_service: The self-improvement service.
        :param platform_service: The platform service.
        :param release_service: The release service.
        """
        self._orchestrator = orchestrator
        self._quality_gate = quality_gate
        self._improvement_service = improvement_service
        self._platform_service = platform_service
        self._release_service = release_service

    def analyze_project(self, project_path: str) -> None:
        """
        Analyze the given project.

        :param project_path: The path to the project.
        """
        # Collect data using subprocess
        result = subprocess.run(['git', 'log'], cwd=project_path,
                                encoding="utf-8", errors="replace")
        commit_history = result.stdout

        # Process the commit history
        commits = commit_history.splitlines()
        self._orchestrator.process_commits(commits)

    def generate_report(self, project_path: str) -> Optional[str]:
        """
        Generate a report for the given project.

        :param project_path: The path to the project.
        :return: A report string or None if an error occurs.
        """
        try:
            self.analyze_project(project_path)
            report = f"Report for {project_path}: Analysis complete."
            return report
        except Exception as e:
            print(f"Error generating report: {e}")
            return None

    def improve_codebase(self, project_path: str) -> None:
        """
        Improve the codebase of the given project.

        :param project_path: The path to the project.
        """
        # Example improvement: run quality gate checks
        result = self._quality_gate.run_checks(project_path)
        if not result.success:
            improvements = self._improvement_service.suggest_improvements(result.errors)
            self.apply_improvements(project_path, improvements)

    def apply_improvements(self, project_path: str, improvements: List[str]) -> None:
        """
        Apply the given improvements to the codebase.

        :param project_path: The path to the project.
        :param improvements: A list of improvement suggestions.
        """
        for improvement in improvements:
            try:
                subprocess.run(['git', 'checkout', '-b', 'improvements'],
                                cwd=project_path, encoding="utf-8", errors="replace")
                subprocess.run(['echo', improvement], cwd=project_path,
                                encoding="utf-8", errors="replace")
                subprocess.run(['git', 'add', '.'], cwd=project_path,
                                encoding="utf-8", errors="replace")
                subprocess.run(['git', 'commit', '-m', improvement],
                                cwd=project_path, encoding="utf-8", errors="replace")
                subprocess.run(['git', 'push', 'origin', 'improvements'],
                                cwd=project_path, encoding="utf-8", errors="replace")
            except Exception as e:
                print(f"Error applying improvements: {e}")