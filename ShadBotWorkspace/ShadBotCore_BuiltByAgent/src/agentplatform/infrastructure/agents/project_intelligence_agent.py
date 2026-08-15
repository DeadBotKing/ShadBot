from dataclasses import dataclass, field
import subprocess
from typing import List

@dataclass(frozen=True)
class ProjectIntelligenceAgent:
    """
    Eye of the Brain and Documentation Keeper (Phase 3)

    Concrete I/O: filesystem, HTTP, subprocess, database.
    May import from domain/ and application/.
    Never use shell=True. Pass argument lists to subprocess.
    Any subprocess call must pass encoding="utf-8", errors="replace".
    """
    project_path: str

    def fetch_project_files(self) -> List[str]:
        """
        Fetches a list of files in the project directory.

        Returns:
            List[str]: A list of file paths within the project.
        """
        try:
            result = subprocess.run(
                ["ls", self.project_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace"
            )
            return result.stdout.splitlines()
        except Exception as e:
            raise RuntimeError(f"Failed to fetch project files: {e}") from e

    def parse_documentation(self, file_path: str) -> str:
        """
        Parses the documentation from a given file.

        Args:
            file_path (str): The path to the file containing documentation.

        Returns:
            str: The parsed documentation content.
        """
        try:
            with open(file_path, 'r', encoding="utf-8", errors="replace") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Documentation file not found: {file_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to parse documentation: {e}") from e

    def update_documentation(self, file_path: str, content: str) -> None:
        """
        Updates the documentation in a given file.

        Args:
            file_path (str): The path to the file containing documentation.
            content (str): The new content for the documentation.
        """
        try:
            with open(file_path, 'w', encoding="utf-8", errors="replace") as file:
                file.write(content)
        except Exception as e:
            raise RuntimeError(f"Failed to update documentation: {e}") from e

    def generate_documentation_summary(self) -> str:
        """
        Generates a summary of the project documentation.

        Returns:
            str: A summary of the project documentation.
        """
        files = self.fetch_project_files()
        summaries = []
        for file_path in files:
            if file_path.endswith('.md') or file_path.endswith('.rst'):
                content = self.parse_documentation(file_path)
                # Implement summary logic here
                summaries.append(f"Summary of {file_path}:\n{content[:100]}...\n")
        return "\n".join(summaries)

# Example usage:
if __name__ == "__main__":
    agent = ProjectIntelligenceAgent(project_path="/path/to/project")
    summary = agent.generate_documentation_summary()
    print(summary)