import subprocess
from typing import List, Optional

class EngineerAgent:
    """
    Concrete implementation of the Engineer Agent for the ShadBot Agent Platform.
    This agent is responsible for performing engineering tasks such as running scripts,
    compiling code, and other related activities.
    """

    def run_script(self, script_path: str, args: Optional[List[str]] = None) -> str:
        """
        Run a shell script using subprocess and return the output.

        :param script_path: Path to the shell script to be executed.
        :param args: Optional list of arguments to pass to the script.
        :return: Output from the script execution.
        """
        if args is None:
            args = []

        try:
            result = subprocess.run(
                [script_path] + args,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace"
            )
            return result.stdout
        except Exception as e:
            raise RuntimeError(f"Error running script {script_path}: {e}") from e

    def compile_code(self, code_path: str) -> str:
        """
        Compile a piece of code using subprocess and return the output.

        :param code_path: Path to the code file to be compiled.
        :return: Output from the compilation process.
        """
        try:
            result = subprocess.run(
                ["python", "-m compileall", code_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace"
            )
            return result.stdout
        except Exception as e:
            raise RuntimeError(f"Error compiling code {code_path}: {e}") from e

    def run_python_script(self, script_path: str, args: Optional[List[str]] = None) -> str:
        """
        Run a Python script using subprocess and return the output.

        :param script_path: Path to the Python script to be executed.
        :param args: Optional list of arguments to pass to the script.
        :return: Output from the script execution.
        """
        if args is None:
            args = []

        try:
            result = subprocess.run(
                ["python", script_path] + args,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace"
            )
            return result.stdout
        except Exception as e:
            raise RuntimeError(f"Error running Python script {script_path}: {e}") from e

# Example usage
if __name__ == "__main__":
    agent = EngineerAgent()
    print(agent.run_script("example.sh", ["arg1", "arg2"]))
    print(agent.compile_code("path/to/code.py"))
    print(agent.run_python_script("example.py", ["arg1", "arg2"]))